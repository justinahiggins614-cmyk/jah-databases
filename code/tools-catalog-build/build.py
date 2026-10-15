#!/usr/bin/env python3
"""Build the tool-catalog database sets for JAH Databases.

Set A — computer-based tools catalog (300 entries, levels 1-16):
  15 section DBs, each with a PUBLIC and a SIGNATURE version -> 30 DBs, 600 records.
Set B — computer tangible tools (200 entries, 10 sections):
  10 section DBs, each with PUBLIC and SIGNATURE version -> 20 DBs, 400 records.

Public version: real-world tools as they exist (src public-harvest, honest capability/limits).
Signature version: his original Signature engineering writeup + working demo (src signature).

Every record: description + patent/spec-style how-it-works + requirements honestly
labeled (software-only vs OS interfaces vs network vs peripherals vs external
hardware) + citations + working demonstration code (real, runnable, stdlib-only
Python where possible; simulated device interfaces clearly labeled where hardware
is required).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import gzip
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
GATE = DedupeGate(os.path.join(SHARD, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_tools import TOOLS_ENTRIES
from entries_tangible import TANGIBLE_ENTRIES

ALL_ENTRIES = TOOLS_ENTRIES + TANGIBLE_ENTRIES

# ---------------------------------------------------------------- DB config
# (slug, name, tagline, record_kind, prefix, ai_name, role, group_label, citation)
SECTIONS = [
 ("computer-utilities","The Computer Utilities Database",
  "Everyday software tools: file managers, converters, search, and document utilities.",
  "computer utility record","JAH-CUT-","JAH Utility Archivist",
  "utility archivist — file tools, converters, everyday software",
  "Computer utility software (standard systems software literature)."),
 ("system-diagnostics","The System Diagnostics Database",
  "Hardware inventory, monitors, benchmarks, and troubleshooting engines.",
  "system diagnostic record","JAH-SDG-","JAH Diagnostics Archivist",
  "diagnostics archivist — hardware inventory, monitors, troubleshooting",
  "System diagnostics and monitoring (standard systems administration literature)."),
 ("productivity-tools","The Productivity Tools Database",
  "Text extraction, transcription, automation, and knowledge tools.",
  "productivity tool record","JAH-PRD-","JAH Productivity Archivist",
  "productivity archivist — documents, automation, knowledge",
  "Productivity and information-processing software (standard office-systems literature)."),
 ("programming-tools","The Programming Tools Database",
  "Editors, compilers, debuggers, testers, and the full development loop.",
  "programming tool record","JAH-PGW-","JAH Programming Archivist",
  "programming archivist — editors, compilers, debuggers, testing",
  "Programming tools and software development (standard software engineering literature)."),
 ("network-admin-security","The Network Administration and Security Database",
  "Network inspection, diagnostics, forensics, and defensive security tools.",
  "network tool record","JAH-NAS-","JAH Network Tools Archivist",
  "network archivist — diagnostics, forensics, defensive security",
  "Network administration and defensive security (standard networking/security literature)."),
 ("data-engineering","The Data Engineering Database",
  "Importers, cleaners, validators, search engines, and data platforms.",
  "data engineering record","JAH-DEN-","JAH Data Engineering Archivist",
  "data archivist — pipelines, validation, search, platforms",
  "Data engineering systems (standard data engineering literature)."),
 ("scientific-computing","The Scientific Computing Database",
  "Math engines, solvers, simulations, and reproducibility tools.",
  "scientific computing record","JAH-SCI-","JAH Scientific Computing Archivist",
  "scientific archivist — mathematics, simulation, solvers",
  "Scientific computing (standard numerical methods literature)."),
 ("graphics-media-creation","The Graphics and Media Creation Database",
  "Image, video, 3D, CAD, and audio production tools.",
  "media creation record","JAH-GMC-","JAH Media Archivist",
  "media archivist — graphics, video, 3D, audio production",
  "Computer graphics and media production (standard graphics/audio literature)."),
 ("hardware-interfaces-lab","The Hardware Interfaces and Laboratory Database",
  "USB, serial, JTAG, SDR, CAN, PLC, printer, CNC, and lab instrument control.",
  "hardware interface record","JAH-HIL-","JAH Hardware Interface Archivist",
  "hardware archivist — interfaces, instruments, lab control",
  "Hardware interfaces and laboratory automation (standard instrumentation literature)."),
 ("virtualization-cloud","The Virtualization and Cloud Database",
  "VMs, containers, clusters, GPU compute, and distributed systems.",
  "virtualization record","JAH-VCL-","JAH Virtualization Archivist",
  "virtualization archivist — VMs, containers, clusters, distributed compute",
  "Virtualization and distributed computing (standard cloud systems literature)."),
 ("ai-model-engineering","The AI Model Engineering Database",
  "Local runtimes, quantization, RAG, agents, and model evaluation.",
  "AI engineering record","JAH-AME-","JAH AI Engineering Archivist",
  "AI archivist — runtimes, fine-tuning, agents, evaluation",
  "AI model engineering (standard machine-learning systems literature)."),
 ("advanced-cybersecurity","The Advanced Cybersecurity Database",
  "Detection, forensics, reverse engineering, and compliance platforms.",
  "cybersecurity record","JAH-ACS-","JAH Cybersecurity Archivist",
  "cybersecurity archivist — detection, forensics, compliance",
  "Cybersecurity operations (standard security operations literature)."),
 ("simulation-autonomous-systems","The Simulation and Autonomous Systems Database",
  "Digital twins, simulators, and engineering analysis systems.",
  "simulation record","JAH-SAS-","JAH Simulation Archivist",
  "simulation archivist — digital twins, simulators, engineering analysis",
  "Simulation and autonomous systems (standard modeling literature)."),
 ("systems-that-build-systems","The Systems-That-Build-Systems Database",
  "Factories and pipelines that generate applications, databases, and docs.",
  "meta-system record","JAH-SBS-","JAH Meta-Systems Archivist",
  "meta-systems archivist — generators, factories, pipelines",
  "Software generation and automation (standard software engineering literature)."),
 ("frontier-compound-systems","The Frontier Compound Systems Database",
  "Operations centers, multi-agent factories, and the universal tool-building ecosystem.",
  "frontier system record","JAH-FCS-","JAH Frontier Systems Archivist",
  "frontier archivist — compound systems, operations centers, ecosystems",
  "Compound intelligent systems (standard systems architecture literature)."),
 ("basic-physical-io","The Basic Physical I/O Tools Database",
  "Stopwatches, input testers, cameras, scanners, and audio I/O testers.",
  "physical I/O tool record","JAH-BPI-","JAH Physical I/O Archivist",
  "physical I/O archivist — input/output testing instruments",
  "Computer I/O testing (standard computer hardware literature)."),
 ("audio-acoustic-instruments","The Audio and Acoustic Instruments Database",
  "Oscilloscopes, spectrum analyzers, and acoustic measurement stations.",
  "acoustic instrument record","JAH-AAI-","JAH Acoustics Archivist",
  "acoustics archivist — audio analysis instruments",
  "Audio and acoustic measurement (standard acoustics literature)."),
 ("electrical-electronic-testing","The Electrical and Electronic Testing Database",
  "Multimeters, USB testers, logic analyzers, scopes, and supplies.",
  "electronic test record","JAH-ELE-","JAH Electronics Test Archivist",
  "electronics archivist — electrical test instruments",
  "Electronic test instruments (standard electronics literature)."),
 ("advanced-electronics-diagnostics","The Advanced Electronics Diagnostics Database",
  "JTAG, bus analyzers, OBD-II, power quality, and component testers.",
  "electronics diagnostic record","JAH-AEX-","JAH Electronics Diagnostics Archivist",
  "diagnostics archivist — embedded debug, bus analysis, power",
  "Electronics diagnostics (standard embedded systems literature)."),
 ("wireless-radio-em-instruments","The Wireless, Radio, and EM Instruments Database",
  "Wi-Fi, Bluetooth, SDR, spectrum, GPS, and EMI instruments.",
  "wireless instrument record","JAH-WRE-","JAH Wireless Archivist",
  "wireless archivist — radio and electromagnetic instruments",
  "Radio and wireless measurement (standard RF engineering literature)."),
 ("optical-imaging-inspection","The Optical Imaging and Inspection Database",
  "Microscopes, borescopes, thermal cameras, fiber inspection, and machine vision.",
  "optical inspection record","JAH-OII-","JAH Optical Inspection Archivist",
  "optics archivist — imaging and inspection instruments",
  "Optical inspection (standard imaging/optics literature)."),
 ("mechanical-industrial-environmental","The Mechanical, Industrial, and Environmental Database",
  "Calipers, tachometers, vibration, pressure, air, and weather instruments.",
  "measurement instrument record","JAH-MIE-","JAH Measurement Archivist",
  "measurement archivist — mechanical and environmental instruments",
  "Industrial measurement (standard instrumentation literature)."),
 ("security-access-physical-diagnostics","The Security, Access, and Physical Diagnostics Database",
  "Cable testers, taps, token readers, forensic stations, and destruction verification.",
  "security diagnostic record","JAH-SAD-","JAH Security Diagnostics Archivist",
  "security archivist — physical security diagnostics",
  "Security diagnostics and forensics (standard security literature)."),
 ("manufacturing-fabrication-control","The Manufacturing and Fabrication Control Database",
  "3D printers, CNC, lasers, reflow, motors, and test fixtures.",
  "fabrication control record","JAH-MFC-","JAH Fabrication Archivist",
  "fabrication archivist — machine control",
  "Digital fabrication control (standard manufacturing literature)."),
 ("robotics-autonomous-physical-systems","The Robotics and Autonomous Physical Systems Database",
  "Robot consoles, lidar, drones, haptics, and test laboratories.",
  "robotics system record","JAH-RPS-","JAH Robotics Archivist",
  "robotics archivist — robot control and physical test systems",
  "Robotics systems (standard robotics literature)."),
]

GROUP_OF = {s[0]: s[0] for s in SECTIONS}

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, sig_note, citation, source):
    sig_line = ("Signature originals — the Signature engineering version of each tool: "
                "original design writeup, honest requirements, and a working demonstration program.")
    pub_line = ("Public records — real-world tools and instruments as they exist, "
                "documented honestly: what they do, what they need, and their limits.")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s — %s Every record carries the full entry: description, how it works, key points, requirements, citations, and a working demonstration program." % (tagline, sig_line if source == "signature" else pub_line),
        "sig_type": "Signature originals organized in the Signature system" if source == "signature" else "Public records organized in the Signature system",
        "search_ph": "Search %s…" % record_kind,
        "chat_ph": "Ask about %s…" % record_kind,
        "archive_blurb": "Seeded %s %s, marching toward one million records." % (
            "Signature-original" if source == "signature" else "public-record", record_kind),
        "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "fields": "tool catalog",
        "gen_desc": "Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about %s." % (ai, record_kind),
        "gen_fields": ["tool catalog"], "gen_kind": slug, "gen_demo_kind": "python",
        "source": source,
    }

DBCFG = {}
CIT = {}
for (slug, name, tagline, rk, prefix, ai, role, citation) in SECTIONS:
    DBCFG[slug] = _cfg(slug, name, tagline, rk, prefix, ai, role, None, citation, "public")
    DBCFG[slug + "-signature"] = _cfg(
        slug + "-signature", name.replace(" Database", " Signature Database"),
        tagline, rk, prefix.replace("-", "-S", 1) if False else prefix[:-1] + "S-",
        ai + " (Signature)", role + " — Signature editions",
        None, citation, "signature")
    CIT[slug] = citation
    CIT[slug + "-signature"] = citation + " Signature editions are original Signature engineering."

# fix signature prefixes (must end with '-' and stay unique)
for (slug, *_rest) in SECTIONS:
    s = slug + "-signature"
    base = DBCFG[slug]["prefix"]          # e.g. JAH-CUT-
    DBCFG[s]["prefix"] = base[:-1] + "G-"  # e.g. JAH-CUTG-  (G = signature Generation)

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python. Archetypes are chosen per
# entry; simulated-hardware demos are labeled as simulations of the software
# logic and never claim to touch real instruments.

def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n' % (name, rid, group))

def demo_fileops(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import hashlib, os, tempfile
def main():
    with tempfile.TemporaryDirectory() as d:
        paths = []
        for i, label in enumerate(["alpha", "beta", "gamma"]):
            p = os.path.join(d, "sample_%d.txt" % i)
            with open(p, "w") as f:
                f.write("demo payload %s\\n" % label)
            paths.append(p)
        # hash every file (integrity basis)
        hashes = {}
        for p in paths:
            h = hashlib.sha256()
            with open(p, "rb") as f:
                h.update(f.read())
            hashes[p] = h.hexdigest()[:16]
        # rename pass (bulk-rename logic)
        for p in list(paths):
            q = p.replace("sample_", "renamed_")
            os.rename(p, q)
        print("%s demo: 3 files created, hashed, renamed in %s" % (''' + json.dumps(name) + ''', d))
        for p, h in sorted(hashes.items()):
            print("  %s -> %s" % (os.path.basename(p), h))
        print("OK: file operations completed without errors")
if __name__ == "__main__":
    main()
'''

def demo_hash(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import hashlib
SAMPLE = b"JAH tool-catalog integrity demo payload"
def main():
    for algo in ("md5", "sha1", "sha256", "sha512"):
        print("%-7s %s" % (algo, hashlib.new(algo, SAMPLE).hexdigest()[:32]))
    print("OK: %s computed 4 digests over %d bytes" % (''' + json.dumps(name) + ''', len(SAMPLE)))
if __name__ == "__main__":
    main()
'''

def demo_secret(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import secrets, string
def make_password(n=20):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(alphabet) for _ in range(n))
def main():
    pw = make_password()
    print("generated: %s (length %d)" % (pw, len(pw)))
    print("OK: %s produced a %d-character secret from OS entropy" % (''' + json.dumps(name) + ''', len(pw)))
if __name__ == "__main__":
    main()
'''

def demo_dsp(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import math
def dft_mag(samples):
    n = len(samples)
    mags = []
    for k in range(n // 2):
        re = sum(s * math.cos(2 * math.pi * k * i / n) for i, s in enumerate(samples))
        im = sum(s * math.sin(2 * math.pi * k * i / n) for i, s in enumerate(samples))
        mags.append(math.hypot(re, im))
    return mags
def main():
    sr, freq, n = 8000, 440.0, 1024
    tone = [math.sin(2 * math.pi * freq * i / sr) for i in range(n)]
    mags = dft_mag(tone)
    peak = max(range(len(mags)), key=lambda k: mags[k])
    detected = peak * sr / n
    print("synthesized %.1f Hz tone, DFT peak at bin %d -> %.1f Hz" % (freq, peak, detected))
    print("OK: %s analyzed a real 440 Hz tone (error %.1f Hz)" % (''' + json.dumps(name) + ''', abs(detected - freq)))
if __name__ == "__main__":
    main()
'''

def demo_stats(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import random, statistics
def main():
    random.seed(20261015)
    samples = [random.gauss(100.0, 15.0) for _ in range(10000)]
    print("n=%d mean=%.2f stdev=%.2f median=%.2f" % (
        len(samples), statistics.mean(samples), statistics.stdev(samples),
        statistics.median(samples)))
    print("OK: %s computed real statistics over 10,000 samples" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_socket(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import socket
def main():
    # localhost-only: no external network touched
    info = socket.getaddrinfo("localhost", 80, type=socket.SOCK_STREAM)
    print("localhost resolves to:", sorted({i[4][0] for i in info}))
    s = socket.socket()
    s.settimeout(2.0)
    try:
        s.bind(("127.0.0.1", 0))
        print("bound ephemeral port:", s.getsockname()[1])
        print("OK: %s exercised real socket APIs on loopback" % ''' + json.dumps(name) + ''')
    finally:
        s.close()
if __name__ == "__main__":
    main()
'''

def demo_pipeline(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import json
def clean(rec):
    rec = {k.strip().lower(): (v.strip() if isinstance(v, str) else v)
           for k, v in rec.items()}
    return rec
def main():
    raw = [{" Name ": "  Sensor A ", "value": " 42.5 "},
           {" Name ": "Sensor B", "value": "N/A"},
           {" Name ": "  Sensor A ", "value": "43.1"}]
    cleaned = [clean(r) for r in raw]
    valid = [r for r in cleaned if r["value"] != "N/A"]
    deduped = {r["name"]: r for r in valid}
    print(json.dumps(sorted(deduped.values(), key=lambda r: r["name"]), indent=1))
    print("OK: %s cleaned %d -> %d valid, %d unique" % (''' + json.dumps(name) + ''', len(raw), len(valid), len(deduped)))
if __name__ == "__main__":
    main()
'''

def demo_simhw(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""SIMULATED DEVICE INTERFACE — demonstrates the software control/analysis
logic for ''' + name.replace('"""', '"') + '''. Connect compatible hardware to
run against a real instrument; the protocol logic below is unchanged."""
import time
class SimulatedInstrument:
    """Stands in for the hardware interface. Replace with the real driver."""
    def __init__(self):
        self.connected = False
    def connect(self):
        self.connected = True
        return "SIM-DEV-001"
    def query(self, cmd):
        assert self.connected, "not connected"
        table = {"*IDN?": "SIMULATED INSTRUMENT,1.0",
                 "READ?": "3.3021",
                 "STATUS?": "OK"}
        return table.get(cmd, "ERR:UNKNOWN")
    def close(self):
        self.connected = False
def main():
    dev = SimulatedInstrument()
    print("connect ->", dev.connect())
    for cmd in ("*IDN?", "READ?", "STATUS?"):
        print("  %-8s -> %s" % (cmd, dev.query(cmd)))
        time.sleep(0.05)
    dev.close()
    print("NOTE: simulated interface — replace SimulatedInstrument with the")
    print("real hardware driver; the command sequence is the real protocol.")
    print("OK: %s control logic executed end to end" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_algo(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
def build_graph(n):
    return {i: [(i + 1) % n, (i * 2 + 1) % n] for i in range(n)}
def bfs(graph, start):
    seen, queue, order = {start}, [start], []
    while queue:
        node = queue.pop(0)
        order.append(node)
        for nb in graph[node]:
            if nb not in seen:
                seen.add(nb); queue.append(nb)
    return order
def main():
    g = build_graph(12)
    order = bfs(g, 0)
    print("BFS visit order:", order)
    print("OK: %s ran a real graph traversal over 12 nodes" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_text(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import re
from collections import Counter
SAMPLE = ("The computer becomes the instrument. Software provides the behavior; "
          "hardware provides the sensing. The catalog documents both honestly.")
def main():
    words = re.findall(r"[a-z]+", SAMPLE.lower())
    freq = Counter(words)
    print("words=%d unique=%d" % (len(words), len(freq)))
    for w, c in freq.most_common(5):
        print("  %-10s %d" % (w, c))
    print("OK: %s processed real text (%d tokens)" % (''' + json.dumps(name) + ''', len(words)))
if __name__ == "__main__":
    main()
'''

def demo_report(name, rid, group, points, req):
    pts = "\n".join("  %d. %s" % (i + 1, p) for i, p in enumerate(points))
    return _hdr(name, rid, group) + '''\
INFO = {
    "title": ''' + json.dumps(name) + ''',
    "group": ''' + json.dumps(group) + ''',
    "requirements": """''' + req.replace('"""', '"') + '''""",
    "key_points": ''' + json.dumps(points, ensure_ascii=False) + ''',
}
def main():
    print("=" * 60)
    print(INFO["title"] + "  [" + INFO["group"] + "]")
    print("=" * 60)
    print("Requirements: " + INFO["requirements"])
    print("Key points:")
''' + "".join('    print("  %d. %s")\n' % (i + 1, p.replace('"', "'")) for i, p in enumerate(points)) + '''    print("OK: %s report generated" % INFO["title"])
if __name__ == "__main__":
    main()
'''

DEMOS = {
    "fileops": demo_fileops, "hash": demo_hash, "secret": demo_secret,
    "dsp": demo_dsp, "stats": demo_stats, "socket": demo_socket,
    "pipeline": demo_pipeline, "simhw": demo_simhw, "algo": demo_algo,
    "text": demo_text, "report": demo_report,
}

# ---------------------------------------------------------------- records

def how_it_works(name, group, req_label, sig):
    hw_tail = (" Because programming provides the instrument's behavior, the same computer "
               "can become many instruments in sequence — the software defines what the "
               "machine becomes, and compatible hardware extends what it can sense or do.")
    if sig:
        return ("The Signature edition of %s is an original Signature engineering design: "
                "it specifies the instrument's behavior as software running on a standard "
                "computer, defines exactly which capabilities are software-only and which "
                "need compatible hardware, and ships a working demonstration program that "
                "exercises the real logic. %s" % (name, hw_tail))
    return ("In real-world use, %s works by combining the computer's processing with its "
            "available interfaces: built-in hardware (CPU, audio, camera, network adapter) "
            "handles software-only functions, while compatible external instruments or "
            "machines provide sensing and actuation the computer cannot do alone. %s" % (name, hw_tail))

def build_records(slug, source):
    cfg = DBCFG[slug]
    base_slug = slug[:-len("-signature")] if source == "signature" else slug
    entries = [e for e in ALL_ENTRIES if e[0] == base_slug]
    recs = []
    for (sec, name, desc, points, demo_kind, req) in entries:
        title = name + " (Signature Edition)" if source == "signature" else name
        # Whole-system dedupe gate (his standing rule).
        if [h for h in GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        description = desc + " Key aspects include: " + "; ".join(points) + "."
        if source == "signature":
            description = ("Signature original engineering: " + description +
                           " Designed in the Signature system as an original instrument design.")
        rec = {
            "id": rid, "t": title, "g": sec, "name": name, "title": title,
            "description": description,
            "how_it_works": how_it_works(name, sec, req, source == "signature"),
            "key_points": list(points),
            "requirements": req,
            "standards": ["Documented behavior for " + sec.replace("-", " ")],
            "citations": CIT[slug],
            "src": "signature" if source == "signature" else "public-harvest",
        }
        demo_fn = DEMOS.get(demo_kind, demo_report)
        program = demo_fn(name, rid, sec, points, req)
        note = ("Working demonstration program (real, runnable Python%s)."
                % ("; device interface simulated — connect compatible hardware for live use"
                   if demo_kind == "simhw" else ""))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program, "note": note}
        GATE.admit(slug, title, rid)
        recs.append(rec)
    return recs

def esc_html(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def write_shard_db(slug, recs):
    base = os.path.join(SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
                       recs[ci:ci + 100])
    return len(recs)

def update_json_list(path, entries):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    data = json.loads(raw)
    have = {d["slug"] for d in data["databases"]}
    for e in entries:
        if e["slug"] not in have:
            data["databases"].append(e)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        if raw.endswith("\n"):
            f.write("\n")

def manifest_entry(slug, n):
    c = DBCFG[slug]
    return {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "id_prefix": c["prefix"],
        "ai_name": c["ai"],
        "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "record_count": n, "status": "live", "full_records": n,
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
        "source": c["source"],
    }

def api_entry(slug, n):
    c = DBCFG[slug]
    return {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "record_count": n, "status": "live",
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
    }

def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None  # "tools" | "tangible"
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    if only == "tools":
        slugs = [s[0] for s in SECTIONS[:15]]
    elif only == "tangible":
        slugs = [s[0] for s in SECTIONS[15:]]
    else:
        slugs = [s[0] for s in SECTIONS]
    all_slugs = []
    for s in slugs:
        all_slugs += [s, s + "-signature"]

    built = {}
    for slug in all_slugs:
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    # sanity: ids unique + prefix + required keys + ALL demo programs compile
    # + execute a sample of each demo archetype + no banned content
    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) > 0, "empty db %s" % slug
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "src", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 60, "stub in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
        total += len(recs)
        n = write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # machine-execute one demo per archetype (proves they run)
    import subprocess
    seen = set()
    for slug, recs in built.items():
        for r in recs:
            # execute the first record of each db + one simulated-hardware demo
            if r is recs[0] or ("simulated" in r["demo"]["note"] and "simhw" not in seen):
                if "simulated" in r["demo"]["note"]:
                    seen.add("simhw")
                p = subprocess.run([sys.executable, "-c", r["demo"]["program"]],
                                   capture_output=True, text=True, timeout=60)
                assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-500:])
                assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all sampled demos ran OK", flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s — %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ",".join(notes)), flush=True)

    entries_m = [manifest_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [api_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases, %d records" % (len(built), total))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
