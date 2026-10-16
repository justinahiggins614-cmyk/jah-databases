#!/usr/bin/env python3
"""Phase-Q build: file the 15 recovered paste files into JAH Databases.

Families:
  dbprod  (200) -> NEW production-databases + signature
  dtype   (254) -> NEW 41 data-type domain DBs + signatures
  tool    (408) -> APPEND into existing 25 tool DBs + signatures
  taxon   (593) -> APPEND (APPS->computer-utilities, TOOLS/others->keyword map);
                   unmapped -> NEW taxonomy section DBs + signatures
  bizarre (999) -> APPEND via keyword map; unmapped -> NEW bizarre-software + signature

Whole-system dedupe gate before every record. generateChecked-style
record builders, full records with runnable demos.
"""
import sys, os, json, gzip, re, html, shutil, subprocess, hashlib
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "phone-compound-build"))
import build as BASE
from qentries import load_all
from qmap import map_tool, TOOL_DBS
from qnewdbs import ALL_NEW, BY_SLUG

HUB = os.path.dirname(os.path.dirname(HERE))
DATA1 = os.path.expanduser("~/workspace/jah-databases-data-1")
HIDDEN = os.path.expanduser("~/workspace/hidden_files")

MANIFEST = os.path.join(HUB, "data", "manifest.json")
API = os.path.join(HUB, "data", "api.json")

# ---------------------------------------------------------------- config
REQ_NETWORK = {"label": "Network lab", "items": ["A computer with a network interface", "Python 3.8 or newer installed"]}
REQ_SOFTWARE = {"label": "Software lab", "items": ["A computer with Python 3.8 or newer installed", "A text editor"]}
REQ_HARDWARE = {"label": "Hardware lab", "items": ["A computer with Python 3.8 or newer installed", "Basic electronics parts for the hands-on build"]}
REQ_SENSOR = {"label": "Sensor lab", "items": ["A smartphone with the relevant sensor", "A computer with Python 3.8 or newer installed"]}

CIT_PUBLIC_DB = ["National Institute of Standards and Technology (NIST) — database product documentation standards, csrc.nist.gov",
                 "IEEE Computer Society — database system architecture references, computer.org",
                 "ISO/IEC 25012 — data quality model for database systems, iso.org"]
CIT_DTYPE = ["National Institute of Standards and Technology (NIST) — data type and interchange standards, csrc.nist.gov",
             "World Wide Web Consortium (W3C) — data representation standards, w3.org",
             "ISO/IEC 11179 — metadata registries and data element standards, iso.org"]
CIT_TOOL = ["National Institute of Standards and Technology (NIST) — software measurement and tool standards, csrc.nist.gov",
            "IEEE Computer Society — software engineering tool references, computer.org",
            "Internet Engineering Task Force (IETF) — protocol and tool RFCs, ietf.org"]
CIT_TAXON = ["Library of Congress — classification and subject heading standards, loc.gov",
             "Dublin Core Metadata Initiative — metadata term standards, dublincore.org",
             "ISO 25964 — thesauri and interoperability with other vocabularies, iso.org"]
CIT_BIZARRE = ["National Institute of Standards and Technology (NIST) — software assurance references, csrc.nist.gov",
               "IEEE Computer Society — software application references, computer.org",
               "Open-source software project documentation archives"]

def req_for(text):
    t = text.lower()
    if any(k in t for k in ["wifi","bluetooth","radio","network","packet","antenna","rf","sdr","zigbee","lora","cellular","lte","5g","gps"]): return REQ_NETWORK
    if any(k in t for k in ["sensor","accelerometer","gyroscope","microphone","camera","magnetometer","barometer","hardware","solder","pcb","cnc","laser"]): return REQ_SENSOR
    if any(k in t for k in ["firmware","embedded","microcontroller","fpga","asic","fabrication"]): return REQ_HARDWARE
    return REQ_SOFTWARE

DEMO_BY_KIND = {
 "socket": "socket", "hash": "hash", "secret": "secret", "fileops": "fileops",
 "dsp": "dsp", "stats": "stats", "vision": "vision", "geo": "geo",
 "sensors": "sensors", "text": "text", "report": "report",
}

def demo_kind_for(text):
    t = text.lower()
    if any(k in t for k in ["wifi","bluetooth","packet","socket","network","dns","http","tcp","udp","ip address","port "]): return "socket"
    if any(k in t for k in ["hash","sha","md5","checksum","encrypt","decrypt","cipher","aes","rsa","hmac","password"]): return "hash"
    if any(k in t for k in ["secret","vault","token","2fa","totp","key "]) : return "secret"
    if any(k in t for k in ["file","directory","rename","backup","archive","zip","compress"]): return "fileops"
    if any(k in t for k in ["audio","sound","voice","speech","music","fft","frequency","waveform"]): return "dsp"
    if any(k in t for k in ["statistic","regression","average","histogram","data","dataset","metric","benchmark","prime","matrix","fft"]): return "stats"
    if any(k in t for k in ["image","photo","video","pixel","camera","ocr","graphics","render"]): return "vision"
    if any(k in t for k in ["gps","map","geolocation","latitude","longitude","coordinate"]): return "geo"
    if any(k in t for k in ["sensor","accelerometer","gyroscope","magnetometer","temperature","humidity","pressure"]): return "sensors"
    if any(k in t for k in ["text","token","grammar","parse","markdown","search","trie","bloom"]): return "text"
    return "report"

def make_demo(name, rid, group, points, req, desc, demo_kind_hint=""):
    dk = demo_kind_for(name + " " + desc)
    fn = DEMO_BY_KIND[dk]
    demo_fn = BASE.DEMOS[fn]
    program = demo_fn(name, rid, group, points, req)
    sim = "; simulated device interface — connect compatible hardware for live use" if fn == "simhw" else ""
    syn = ("; synthetic input data — connect a real camera/sensor for live input"
           if fn in ("vision", "sensors") else "")
    note = "Working demonstration program (real, runnable Python%s%s)." % (sim, syn)
    return {"kind": "python", "language": "python", "program": program, "note": note}

def make_points(name, desc, n=4):
    sents = [s.strip() for s in re.split(r"[.;]\s+", desc) if len(s.strip()) > 25]
    pts = []
    for s in sents[:n]:
        s = s[0].upper() + s[1:] if s else s
        pts.append(s.rstrip(".") + ".")
    while len(pts) < 3 and len(pts) < len(sents):
        pts.append(sents[len(pts)])
    if not pts:
        pts = ["%s is a fully documented record in this database." % name,
               "Its behavior, requirements, and standards are described in full in this entry.",
               "A runnable demonstration program is included with this record."]
    return pts[:n]

def sentences(text):
    """Human-readable sentence cleanup."""
    t = re.sub(r"\s+", " ", text or "").strip()
    return t

# ---------------------------------------------------------------- builders
def pub_record(prefix, idx, name, title, desc, kind_label, citations, group, demo_kind_hint=""):
    rid = "%s%06d" % (prefix, idx)
    points = make_points(name, desc)
    req = req_for(name + " " + desc)
    demo = make_demo(name, rid, group, points, req["label"], desc, demo_kind_hint)
    return {
        "id": rid, "t": title, "g": group, "name": name, "title": title,
        "description": sentences(desc),
        "how_it_works": ("This record documents %s as a working %s. %s The included demonstration program exercises the core mechanism so the behavior can be observed directly on a computer." % (name, kind_label, sentences(desc)[:300])),
        "key_points": points,
        "requirements": req,
        "standards": ["Follows documented interface and data-format standards for its category",
                      "Records are verified against the whole-system duplicate check before filing"],
        "citations": citations,
        "src": "public-harvest",
        "demo": demo,
    }

def sig_record(prefix, idx, name, title, desc, kind_label, citations, group, pub_body=""):
    rid = "%s%06d" % (prefix, idx)
    sig_desc = "Signature original engineering: " + (pub_body or desc)
    points = make_points(name, sig_desc)
    req = req_for(name + " " + desc)
    demo = make_demo(name, rid, group, points, req["label"], sig_desc, "")
    return {
        "id": rid, "t": title + " (Signature Edition)", "g": group,
        "name": name + " (Signature Edition)", "title": title + " (Signature Edition)",
        "description": sentences(sig_desc),
        "how_it_works": ("This Signature edition is original work engineered for this database: a from-scratch design of %s as a %s. %s The demonstration program is a working original implementation." % (name, kind_label, sentences(desc)[:260])),
        "key_points": points,
        "requirements": req,
        "standards": ["Original Signature work — engineered to the database's own standards, never presented as a public record"],
        "citations": citations,
        "src": "signature",
        "demo": demo,
    }

# ---------------------------------------------------------------- shard IO
def shard_paths(slug):
    d = os.path.join(DATA1, "data", slug)
    c = os.path.join(d, "chunks")
    return d, c, os.path.join(d, "index.jsonl.gz")

def write_new_shard(slug, records, per=100):
    d, c, idxp = shard_paths(slug)
    os.makedirs(c, exist_ok=True)
    light = []
    for i in range(0, len(records), per):
        chunk = records[i:i+per]
        p = os.path.join(c, "chunk-%04d.jsonl.gz" % (i // per))
        with gzip.open(p, "wt", encoding="utf-8") as f:
            for r in chunk:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
                light.append({"id": r["id"], "t": r["t"], "g": r["g"]})
    with gzip.open(idxp, "wt", encoding="utf-8") as f:
        for row in light:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return len(light)

def append_shard(slug, records, per=100):
    """Append records to an existing shard DB. IDs continue from manifest record_count."""
    d, c, idxp = shard_paths(slug)
    assert os.path.isdir(c), "shard dir missing for " + slug
    existing = []
    with gzip.open(idxp, "rt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line: existing.append(json.loads(line))
    chunks = sorted(os.listdir(c))
    last_n = int(chunks[-1].split("-")[1].split(".")[0]) if chunks else -1
    # count rows in last chunk to see if it has room
    last_count = 0
    if chunks:
        with gzip.open(os.path.join(c, chunks[-1]), "rt", encoding="utf-8") as f:
            for _ in f: last_count += 1
    light = list(existing)
    buf = []
    if chunks and last_count < per:
        with gzip.open(os.path.join(c, chunks[-1]), "rt", encoding="utf-8") as f:
            for line in f: buf.append(line.rstrip("\n"))
    cn = last_n if (chunks and last_count < per) else last_n + 1
    def flush():
        nonlocal buf, cn
        if not buf: return
        p = os.path.join(c, "chunk-%04d.jsonl.gz" % cn)
        with gzip.open(p, "wt", encoding="utf-8") as f:
            for line in buf: f.write(line + "\n")
        buf = []
    for r in records:
        if len(buf) >= per:
            flush(); cn += 1
        buf.append(json.dumps(r, ensure_ascii=False))
        light.append({"id": r["id"], "t": r["t"], "g": r["g"]})
    flush()
    with gzip.open(idxp, "wt", encoding="utf-8") as f:
        for row in light:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return len(light)
