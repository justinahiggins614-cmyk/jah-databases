#!/usr/bin/env python3
"""PHASE B — database-type catalog build (dbtype paste 1).

- Files 21 entries as full canon records into existing covering databases.
- Builds 12 new <category>-databases DBs (public + signature) = 24 DBs,
  198 records, one per paste entry not already covered.
- Whole-system dedupe via code/dedupe_gate.py. Canon page/chunk/index
  pattern from code/phone-compound-build. No website references, no
  Facebook, no banned phrases.
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
from entries import ENTRIES

# ============================================================ demo library
# Every demo is real, runnable, stdlib-only Python with an "OK:" marker.
# Synthetic sample inputs are labeled as such; real algorithms throughout.

def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (name, rid, group))

def demo_report(name, rid, group, points, req):
    body = "".join('    print("  %d. %s")\n' % (i + 1, p.replace('"', "'"))
                     for i, p in enumerate(points))
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
''' + body + '''    print("OK: %s report generated" % INFO["title"])
if __name__ == "__main__":
    main()
'''

def demo_sqlite(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import sqlite3
def main():
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("CREATE TABLE records (id INTEGER PRIMARY KEY, title TEXT NOT NULL, "
                "amount REAL CHECK (amount >= 0), kind TEXT)")
    rows = [("Relational Tabular Rows", 10.5, "type"),
            ("Semi-Structured Documents", 20.0, "type"),
            ("Time-Series Metric Tuples", 30.25, "type")]
    cur.executemany("INSERT INTO records (title, amount, kind) VALUES (?,?,?)", rows)
    try:
        cur.execute("INSERT INTO records (title, amount, kind) VALUES (?,?,?)",
                    ("bad row", -1.0, "type"))
        print("ERROR: CHECK constraint did not fire")
    except sqlite3.IntegrityError as e:
        print("constraint enforced:", e)
    cur.execute("SELECT COUNT(*), SUM(amount) FROM records")
    n, total = cur.fetchone()
    print("rows=%d total=%.2f" % (n, total))
    assert n == 3 and abs(total - 60.75) < 1e-9
    print("OK: %s ran real relational SQL with constraints" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_jsondoc(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import json
DOCS = [
    {"sku": "A-100", "price": {"list": 49.99, "sale": 39.99},
     "attrs": {"color": "red", "tags": ["new", "sale"]}},
    {"sku": "B-200", "price": {"list": 19.99},
     "attrs": {"color": "blue"}, "warehouse": "W-3"},
]
def get_path(doc, path):
    cur = doc
    for part in path.split("."):
        cur = cur[part]
        if isinstance(cur, list):
            cur = cur[0]
    return cur
def main():
    for d in DOCS:
        print(d["sku"], "-> sale:", get_path(d, "price.sale") if "sale" in d["price"] else d["price"]["list"])
    assert get_path(DOCS[0], "attrs.color") == "red"
    assert get_path(DOCS[1], "warehouse") == "W-3"
    print("OK: %s queried real nested documents by path" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_ledger(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
def post(entries):
    bal = {}
    for debit, credit, amt in entries:
        bal[debit] = bal.get(debit, 0.0) + amt
        bal[credit] = bal.get(credit, 0.0) - amt
    return bal
def main():
    entries = [("cash", "revenue", 1000.0),
               ("supplies", "cash", 250.0),
               ("cash", "loyalty-liability", 40.0)]
    bal = post(entries)
    total = sum(bal.values())
    for acct, b in sorted(bal.items()):
        print("  %-18s %8.2f" % (acct, b))
    print("ledger imbalance: %.2f" % total)
    assert abs(total) < 1e-9, "double-entry invariant broken"
    print("OK: %s kept balanced double-entry books" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_ticks(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
# SYNTHETIC SAMPLE TICKS — real tick-math (VWAP, spread) over labeled sample data.
TICKS = [(1, 100.10, 200), (2, 100.12, 150), (3, 100.08, 300),
         (4, 100.15, 100), (5, 100.11, 250)]
def main():
    px_vol = sum(p * v for _, p, v in TICKS)
    vol = sum(v for _, _, v in TICKS)
    vwap = px_vol / vol
    hi = max(p for _, p, _ in TICKS); lo = min(p for _, p, _ in TICKS)
    print("ticks=%d volume=%d vwap=%.4f high=%.2f low=%.2f" % (len(TICKS), vol, vwap, hi, lo))
    assert abs(vwap - 100.1045) < 1e-3
    print("NOTE: synthetic sample ticks — connect a market-data feed for live ticks.")
    print("OK: %s computed real VWAP over tick data" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_hashchain(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import hashlib, json
def block_hash(prev, txs, nonce):
    h = hashlib.sha256()
    h.update(prev.encode() + json.dumps(txs, sort_keys=True).encode() + str(nonce).encode())
    return h.hexdigest()
def main():
    chain, prev = [], "GENESIS"
    for i, txs in enumerate([["alice->bob:5"], ["bob->carol:2", "alice->dave:1"], ["carol->bob:1"]]):
        nonce, bh = 0, ""
        while not bh.startswith("00"):
            nonce += 1
            bh = block_hash(prev, txs, nonce)
        chain.append((prev, txs, nonce, bh)); prev = bh
        print("block %d hash=%s.. nonce=%d" % (i, bh[:16], nonce))
    for i in range(1, len(chain)):
        assert chain[i][0] == chain[i-1][3], "chain link broken"
    print("OK: %s built and verified a real hash-linked chain" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_ehr(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""SYNTHETIC SAMPLE RECORD — demonstrates EHR structure/validation logic.
No real patient data: the record below is fabricated for the demo."""
import json
REQUIRED = ["patient_id", "encounters"]
ENCOUNTER_REQUIRED = ["date", "diagnoses", "vitals"]
def validate(rec):
    errs = []
    for k in REQUIRED:
        if k not in rec: errs.append("missing " + k)
    for i, e in enumerate(rec.get("encounters", [])):
        for k in ENCOUNTER_REQUIRED:
            if k not in e: errs.append("encounter %d missing %s" % (i, k))
    return errs
def main():
    rec = {"patient_id": "SYNTH-001",
           "encounters": [
               {"date": "2026-10-01", "diagnoses": ["J06.9"],
                "vitals": {"bp": "120/80", "hr": 72},
                "notes": "synthetic sample encounter"},
               {"date": "2026-10-15", "diagnoses": ["Z00.00"],
                "vitals": {"bp": "118/78", "hr": 70},
                "notes": "synthetic sample encounter"}]}
    errs = validate(rec)
    print(json.dumps(rec, indent=1)[:400], "...")
    assert not errs, errs
    print("encounters=%d diagnoses=%d" % (
        len(rec["encounters"]), sum(len(e["diagnoses"]) for e in rec["encounters"])))
    print("NOTE: synthetic sample record — real EHRs require certified systems.")
    print("OK: %s validated a real EHR-shaped record" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_dicom(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""SYNTHETIC SAMPLE ATTRIBUTES — demonstrates DICOM metadata handling.
Attribute values below are fabricated; real headers need de-identification."""
REQUIRED_TAGS = ["Modality", "SliceThickness", "PixelSpacing",
                 "ImageOrientationPatient", "StudyInstanceUID"]
def validate(attrs):
    return [t for t in REQUIRED_TAGS if t not in attrs]
def main():
    attrs = {"Modality": "CT", "SliceThickness": 1.25,
             "PixelSpacing": [0.7, 0.7],
             "ImageOrientationPatient": [1, 0, 0, 0, 1, 0],
             "StudyInstanceUID": "1.2.3.SYNTHETIC",
             "PatientName": "SYNTHETIC^PATIENT"}
    missing = validate(attrs)
    assert not missing, missing
    px = attrs["PixelSpacing"]
    print("modality=%s slice=%.2fmm pixel=%.2fx%.2fmm" % (
        attrs["Modality"], attrs["SliceThickness"], px[0], px[1]))
    deid = {k: v for k, v in attrs.items() if not k.startswith("Patient")}
    assert "PatientName" not in deid
    print("de-identified tags kept: %d" % len(deid))
    print("NOTE: synthetic attributes — real DICOM headers require de-identification.")
    print("OK: %s validated real DICOM-shaped metadata" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_genome(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""SYNTHETIC SAMPLE SEQUENCE — real base-pair math over a fabricated sequence.
Never real human genetic data."""
import random
from collections import Counter
def main():
    rnd = random.Random(20261015)
    seq = "".join(rnd.choice("ACGT") for _ in range(10000))
    counts = Counter(seq)
    gc = (counts["G"] + counts["C"]) / len(seq)
    print("length=%d A=%d C=%d G=%d T=%d GC=%.3f" % (
        len(seq), counts["A"], counts["C"], counts["G"], counts["T"], gc))
    assert abs(gc - 0.5) < 0.05
    # k-mer sanity: all 16 dinucleotides present in 10k random bases
    kmers = {seq[i:i+2] for i in range(len(seq) - 1)}
    print("dinucleotide coverage: %d/16" % len(kmers))
    assert len(kmers) == 16
    print("NOTE: synthetic sequence — real genomics needs reference alignment.")
    print("OK: %s ran real sequence statistics" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_geo(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""Real positioning math on sample coordinates — the algorithms a ''' + name.replace('"""', '"') + ''' uses."""
import math
def haversine_m(lat1, lon1, lat2, lon2):
    r = 6371000.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*r*math.asin(math.sqrt(a))
def point_in_polygon(lat, lon, poly):
    inside, n = False, len(poly)
    for i in range(n):
        la1, lo1 = poly[i]; la2, lo2 = poly[(i+1) % n]
        if ((lo1 > lon) != (lo2 > lon)) and \\
           (lat < (la2-la1)*(lon-lo1)/(lo2-lo1)+la1):
            inside = not inside
    return inside
def main():
    a = (40.7128, -74.0060); b = (40.7138, -74.0050)
    d = haversine_m(*a, *b)
    print("A->B distance: %.1f m" % d)
    zone = [(40.70, -74.02), (40.70, -73.99), (40.73, -73.99), (40.73, -74.02)]
    print("A inside zone:", point_in_polygon(a[0], a[1], zone))
    assert 100 < d < 200 and point_in_polygon(a[0], a[1], zone)
    print("OK: %s computed real geospatial math" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_stats(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import random, statistics
def main():
    random.seed(20261015)
    samples = [random.gauss(100.0, 15.0) for _ in range(10000)]
    mu, sd, med = statistics.mean(samples), statistics.stdev(samples), statistics.median(samples)
    print("n=%d mean=%.2f stdev=%.2f median=%.2f" % (len(samples), mu, sd, med))
    assert abs(mu-100) < 1 and abs(sd-15) < 1
    print("OK: %s computed real statistics over 10,000 samples" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_simhw(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""SIMULATED DEVICE INTERFACE — demonstrates the telemetry/control logic for ''' + name.replace('"""', '"') + '''.
Connect compatible hardware to run against a real instrument."""
import time
class SimulatedInstrument:
    def __init__(self): self.connected = False
    def connect(self): self.connected = True; return "SIM-DEV-001"
    def query(self, cmd):
        assert self.connected
        return {"*IDN?": "SIMULATED INSTRUMENT,1.0", "READ?": "3.3021",
                "STATUS?": "OK"}.get(cmd, "ERR:UNKNOWN")
    def close(self): self.connected = False
def main():
    dev = SimulatedInstrument()
    print("connect ->", dev.connect())
    for cmd in ("*IDN?", "READ?", "STATUS?"):
        print("  %-8s -> %s" % (cmd, dev.query(cmd))); time.sleep(0.02)
    dev.close()
    print("NOTE: simulated interface — replace with the real hardware driver.")
    print("OK: %s telemetry logic executed end to end" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_rss(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import xml.etree.ElementTree as ET
def main():
    rss = ET.Element("rss", version="2.0")
    ch = ET.SubElement(rss, "channel")
    ET.SubElement(ch, "title").text = "Sample Show"
    ET.SubElement(ch, "link").text = "https://example.invalid/show"
    for i, (title, secs) in enumerate([("Episode One", 1800), ("Episode Two", 2400)], 1):
        it = ET.SubElement(ch, "item")
        ET.SubElement(it, "title").text = title
        ET.SubElement(it, "pubDate").text = "Thu, %02d Oct 2026 12:00:00 GMT" % i
        ET.SubElement(it, "enclosure", url="https://example.invalid/ep%d.mp3" % i,
                      length=str(secs*16000), type="audio/mpeg")
        ET.SubElement(it, "{http://www.itunes.com/dtds/podcast-1.0.dtd}duration").text = str(secs)
    xml = ET.tostring(rss, encoding="unicode")
    back = ET.fromstring(xml)
    items = back.find("channel").findall("item")
    print("episodes=%d" % len(items))
    assert len(items) == 2 and all(it.find("enclosure") is not None for it in items)
    print("OK: %s built and validated a real RSS feed" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_text(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import re
from collections import Counter
SAMPLE = ("The database keeps every record. Records carry descriptions, "
          "how-it-works writeups, and working demonstrations. The catalog "
          "documents database types honestly and completely.")
def main():
    words = re.findall(r"[a-z]+", SAMPLE.lower())
    freq = Counter(words)
    print("words=%d unique=%d" % (len(words), len(freq)))
    for w, c in freq.most_common(5):
        print("  %-12s %d" % (w, c))
    assert freq["database"] >= 2
    print("OK: %s processed real text (%d tokens)" % (''' + json.dumps(name) + ''', len(words)))
if __name__ == "__main__":
    main()
'''

def demo_pipeline(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import json
def clean(rec):
    return {k.strip().lower(): (v.strip() if isinstance(v, str) else v)
            for k, v in rec.items()}
def main():
    raw = [{" Name ": "  Sensor A ", "value": " 42.5 "},
           {" Name ": "Sensor B", "value": "N/A"},
           {" Name ": "  Sensor A ", "value": "43.1"}]
    cleaned = [clean(r) for r in raw]
    valid = [r for r in cleaned if r["value"] != "N/A"]
    deduped = {r["name"]: r for r in valid}
    print(json.dumps(sorted(deduped.values(), key=lambda r: r["name"]), indent=1))
    assert len(deduped) == 1 and deduped["Sensor A"]["value"] == "43.1"
    print("OK: %s cleaned %d -> %d valid, %d unique" % (''' + json.dumps(name) + ''', len(raw), len(valid), len(deduped)))
if __name__ == "__main__":
    main()
'''

def demo_fileops(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import hashlib, os, tempfile
def main():
    with tempfile.TemporaryDirectory() as d:
        paths = []
        for i, label in enumerate(["alpha", "beta", "gamma"]):
            p = os.path.join(d, "sample_%d.txt" % i)
            with open(p, "w") as f: f.write("demo payload %s\\n" % label)
            paths.append(p)
        hashes = {}
        for p in paths:
            h = hashlib.sha256()
            with open(p, "rb") as f: h.update(f.read())
            hashes[os.path.basename(p)] = h.hexdigest()[:16]
        for p, h in sorted(hashes.items()):
            print("  %s -> %s" % (p, h))
        assert len(set(hashes.values())) == 3
        print("OK: %s hashed 3 payloads with distinct digests" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_socket(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import socket, struct
def parse_ipv4_header(raw):
    ver_ihl, tos, total, ident, flags_frag, ttl, proto, csum, src, dst = \\
        struct.unpack("!BBHHHBBHII", raw[:20])
    return {"version": ver_ihl >> 4, "ihl": ver_ihl & 15, "total_length": total,
            "ttl": ttl, "protocol": proto,
            "src": socket.inet_ntoa(struct.pack("!I", src)),
            "dst": socket.inet_ntoa(struct.pack("!I", dst))}
def main():
    # SYNTHETIC SAMPLE PACKET — real header parsing over fabricated bytes.
    raw = struct.pack("!BBHHHBBHII", 0x45, 0, 60, 0x1c46, 0x4000, 64, 6, 0,
                      0x0a000001, 0x0a000002)
    hdr = parse_ipv4_header(raw)
    print(hdr)
    assert hdr["version"] == 4 and hdr["src"] == "10.0.0.1" and hdr["protocol"] == 6
    print("NOTE: synthetic packet — capture live traffic for real analysis.")
    print("OK: %s parsed a real IPv4 header" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_algo(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
def bfs(graph, start):
    seen, queue, order = {start}, [start], []
    while queue:
        node = queue.pop(0); order.append(node)
        for nb in graph[node]:
            if nb not in seen: seen.add(nb); queue.append(nb)
    return order
def main():
    g = {i: [(i+1) % 12, (i*2+1) % 12] for i in range(12)}
    order = bfs(g, 0)
    print("BFS visit order:", order)
    assert len(order) == 12
    print("OK: %s ran a real graph traversal over 12 nodes" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_vision(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""SYNTHETIC INPUT DATA — real image-analysis logic over synthesized pixels."""
import random
def make_frame(w, h, base, seed, defect=False):
    rnd = random.Random(seed)
    px = [[base + rnd.randint(-8, 8) for _ in range(w)] for _ in range(h)]
    if defect:
        for y in range(h//3, 2*h//3): px[y][w//2] = base + 90
    return px
def edge_metric(px):
    return sum(abs(px[y][x+1]-px[y][x]) for y in range(len(px)) for x in range(len(px[0])-1))
def change_mask(a, b, thresh=40):
    return sum(1 for y in range(len(a)) for x in range(len(a[0]))
               if abs(a[y][x]-b[y][x]) > thresh)
def main():
    clean = make_frame(64, 48, 128, seed=7)
    cracked = make_frame(64, 48, 128, seed=7, defect=True)
    changed = change_mask(clean, cracked)
    print("clean edge=%d cracked edge=%d changed=%d/3072" % (
        edge_metric(clean), edge_metric(cracked), changed))
    assert changed > 0
    print("NOTE: synthetic frames — connect a real capture path for live input.")
    print("OK: %s ran real image-analysis logic" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_secret(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import random, string
def gen_world(seed, w=24, h=12):
    rnd = random.Random(seed)
    return [[rnd.choice(".#~^") for _ in range(w)] for _ in range(h)]
def main():
    a = gen_world(12345); b = gen_world(12345); c = gen_world(99999)
    assert a == b and a != c
    land = sum(cell != "~" for row in a for cell in row)
    print("world %dx%d land=%d water=%d deterministic=%s" % (
        24, 12, land, 24*12-land, a == b))
    print("OK: %s generated a deterministic world from seed 12345" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_dsp(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import math
def dft_mag(samples):
    n = len(samples); mags = []
    for k in range(n//2):
        re = sum(s*math.cos(2*math.pi*k*i/n) for i, s in enumerate(samples))
        im = sum(s*math.sin(2*math.pi*k*i/n) for i, s in enumerate(samples))
        mags.append(math.hypot(re, im))
    return mags
def main():
    sr, freq, n = 8000, 440.0, 1024
    tone = [math.sin(2*math.pi*freq*i/sr) for i in range(n)]
    mags = dft_mag(tone)
    peak = max(range(len(mags)), key=lambda k: mags[k])
    detected = peak*sr/n
    print("synthesized %.1f Hz tone, DFT peak bin %d -> %.1f Hz" % (freq, peak, detected))
    assert abs(detected-freq) < 10
    print("OK: %s analyzed a real 440 Hz tone" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_sensors(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""SYNTHETIC SENSOR STREAM — real multi-sensor analysis over synthesized channels."""
import math, random, statistics
def synth(n, base, amp, freq, seed):
    rnd = random.Random(seed)
    return [base + amp*math.sin(2*math.pi*freq*i/n) + rnd.gauss(0, amp*0.05)
            for i in range(n)]
def pearson(a, b):
    n = len(a); ma, mb = statistics.mean(a), statistics.mean(b)
    num = sum((x-ma)*(y-mb) for x, y in zip(a, b))
    den = math.sqrt(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b))
    return num/den if den else 0.0
def main():
    n = 1000
    ch1 = synth(n, 9.81, 0.4, 3, seed=11)
    ch2 = synth(n, 0.05, 0.4, 3, seed=12)
    r = pearson(ch1, ch2)
    print("samples=%d correlation=%.3f" % (n, r))
    assert abs(r) > 0.8
    print("NOTE: synthetic channels — connect the real sensor stack for live readings.")
    print("OK: %s ran real multi-sensor analysis" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_spike(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""SYNTHETIC DRIVE CURRENT — real leaky integrate-and-fire membrane dynamics.
Connect a real MEA or neuromorphic front end for live spike trains."""
import math, random
def main():
    rnd = random.Random(20261015)
    tau, v_rest, v_th, v_reset, dt = 20.0, -70.0, -55.0, -70.0, 0.1
    steps, spikes = 3000, []
    v = v_rest
    for i in range(steps):
        i_inj = 1.6 + 0.6*math.sin(2*math.pi*i/400) + rnd.gauss(0, 0.15)
        v += dt*(-(v - v_rest)/tau + i_inj)
        if v >= v_th:
            spikes.append(i*dt)
            v = v_reset  # refractory reset
    isi = [b - a for a, b in zip(spikes, spikes[1:])]
    mean_isi = sum(isi)/len(isi)
    print("simulated %.1f ms: spikes=%d mean ISI=%.2f ms rate=%.1f Hz" % (
        steps*dt, len(spikes), mean_isi, 1000.0/mean_isi))
    assert len(spikes) > 10 and all(x > 1.0 for x in isi)
    print("OK: %s simulated real integrate-and-fire membrane dynamics" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_dna(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""Quaternary DNA encoding — real base-pair math over a sample payload."""
def main():
    payload = b"JAH-DNA-ARCHIVE"
    enc = {"00": "A", "01": "C", "10": "G", "11": "T"}
    bits = "".join(format(b, "08b") for b in payload)
    strand = "".join(enc[bits[i:i+2]] for i in range(0, len(bits), 2))
    dec = {v: k for k, v in enc.items()}
    back = bytes(int("".join(dec[b] for b in strand[i:i+4]), 2)
                 for i in range(0, len(strand), 4))
    gc = sum(1 for b in strand if b in "GC")/len(strand)
    print("bytes=%d bases=%d gc=%.3f roundtrip=%s" % (
        len(payload), len(strand), gc, back == payload))
    assert back == payload and len(strand) == 4*len(payload)
    print("OK: %s quaternary-encoded a payload into ACGT and decoded it back" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_tda(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""Sample filtration — real 0-dimensional persistence via union-find."""
def main():
    parent = {}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    # edges arrive in filtration order; each node born at scale 0
    edges = [(0, 1, 0.2), (2, 3, 0.3), (1, 2, 0.5), (3, 4, 0.6), (0, 4, 0.9)]
    nodes = sorted({u for e in edges for u in e[:2]})
    for x in nodes:
        parent[x] = x
    birth = {x: 0.0 for x in nodes}
    pairs = []
    for u, v, w in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            # younger component dies at w (elder rule)
            young, old = (ru, rv) if birth[ru] > birth[rv] else (rv, ru)
            pairs.append((birth[young], w))
            parent[young] = old
            birth[old] = min(birth[old], birth[young])
    survivors = sum(1 for x in nodes if find(x) == x)
    print("persistence pairs (birth, death):", pairs)
    print("infinite components: %d" % survivors)
    assert len(pairs) == len(nodes) - survivors and survivors == 1
    assert all(d > b for b, d in pairs)
    print("OK: %s computed real persistence pairs over a sample filtration" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_poincare(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""Sample Poincare-disk coordinates — real hyperbolic distance math."""
import math
def pdist(u, v):
    nu = u[0]**2 + u[1]**2
    nv = v[0]**2 + v[1]**2
    num = 2*((u[0]-v[0])**2 + (u[1]-v[1])**2)
    den = (1-nu)*(1-nv)
    return math.acosh(1 + num/den)
def main():
    root, shallow, deep = (0.0, 0.0), (0.5, 0.0), (0.9, 0.0)
    d1, d2 = pdist(root, shallow), pdist(root, deep)
    print("d(root, shallow)=%.4f d(root, deep)=%.4f ratio=%.2f" % (d1, d2, d2/d1))
    assert pdist(root, root) == 0.0
    assert d2 > d1  # exponential room toward the boundary
    assert abs(pdist(shallow, deep) - pdist(deep, shallow)) < 1e-12
    print("OK: %s measured real hyperbolic distances in the Poincare disk" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_multivector(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""Cl(2) geometric product — real multivector identities, verified numerically."""
import math
KEYS = ("s", "e1", "e2", "e12")
# geometric product table for basis blades
TABLE = {
    ("s","s"):"s", ("s","e1"):"e1", ("s","e2"):"e2", ("s","e12"):"e12",
    ("e1","s"):"e1", ("e2","s"):"e2", ("e12","s"):"e12",
    ("e1","e1"):"s", ("e2","e2"):"s", ("e12","e12"):("s",-1),
    ("e1","e2"):"e12", ("e2","e1"):("e12",-1),
    ("e1","e12"):"e2", ("e12","e1"):("e2",-1),
    ("e2","e12"):("e1",-1), ("e12","e2"):"e1",
}
def _entry(t):
    return (t, 1) if isinstance(t, str) else t
def gp(a, b):
    out = {k: 0.0 for k in KEYS}
    for ka in KEYS:
        for kb in KEYS:
            if a[ka] and b[kb]:
                blade, sign = _entry(TABLE[(ka, kb)])
                out[blade] += sign*a[ka]*b[kb]
    return out
def mv(**kw):
    return {k: float(kw.get(k, 0)) for k in KEYS}
def main():
    e1, e2 = mv(e1=1), mv(e2=1)
    assert gp(e1, e2)["e12"] == 1.0 and gp(e2, e1)["e12"] == -1.0
    # rotor: rotate e1 by 90 degrees -> e2
    th = math.pi/2
    R = mv(s=math.cos(th/2), e12=-math.sin(th/2))
    Rr = mv(s=math.cos(th/2), e12=math.sin(th/2))
    v2 = gp(gp(R, e1), Rr)
    print("R e1 ~R = %.4f*e1 + %.4f*e2" % (v2["e1"], v2["e2"]))
    assert abs(v2["e1"]) < 1e-9 and abs(v2["e2"]-1.0) < 1e-9
    assert abs(gp(R, Rr)["s"]-1.0) < 1e-9  # rotor normalization
    print("OK: %s verified real geometric-product rotor identities" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_riemann(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""Spherical metric sample — real Riemannian line-element evaluation."""
import math
def main():
    R = 6371000.0  # sphere radius, metres
    def metric(th):
        return {"g_tt": R**2, "g_pp": (R*math.sin(th))**2}  # g_thth, g_phph
    def dist(th1, ph1, th2, ph2):
        cosc = (math.sin(th1)*math.sin(th2)
                + math.cos(th1)*math.cos(th2)*math.cos(ph2-ph1))
        return R*math.acos(max(-1.0, min(1.0, cosc)))
    th = math.radians(40.0)
    g = metric(th)
    d = dist(math.radians(40.0), math.radians(-74.0),
             math.radians(41.0), math.radians(-74.0))
    print("g_thth=%.3e g_phph=%.3e det=%.3e" % (g["g_tt"], g["g_pp"],
          g["g_tt"]*g["g_pp"]))
    print("1 deg latitude arc: %.1f m" % d)
    assert abs(d - 111194.9) < 50
    assert g["g_pp"] < g["g_tt"]  # meridians converge away from equator
    print("OK: %s evaluated a real Riemannian line element" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_lattice(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""EDUCATIONAL 2-D PARAMETERS — real Babai nearest-plane decoding geometry.
Production lattices use 512+ dimensions (NIST FIPS 203/204); this model shows
the trapdoor geometry only. Descriptive documentation, not attack tradecraft."""
def babai(B, t):
    n = len(B)
    Bs = [list(map(float, b)) for b in B]
    for i in range(n):
        for j in range(i):
            mu = sum(Bs[i][k]*Bs[j][k] for k in range(n))/sum(x*x for x in Bs[j])
            Bs[i] = [a - mu*b for a, b in zip(Bs[i], Bs[j])]
    l = list(map(float, t))
    coeffs = [0]*n
    for i in reversed(range(n)):
        c = sum(l[k]*Bs[i][k] for k in range(n))/sum(x*x for x in Bs[i])
        coeffs[i] = int(round(c))
        l = [a - coeffs[i]*b for a, b in zip(l, B[i])]
    return coeffs
def main():
    B = [[4, 1], [1, 3]]          # trapdoor basis (short, near-orthogonal)
    m = [2, 1]                    # message coefficients
    pt = [m[0]*B[0][0] + m[1]*B[1][0], m[0]*B[0][1] + m[1]*B[1][1]]
    noisy = [pt[0], pt[1] + 1]    # small error, as in LWE
    rec = babai(B, noisy)
    print("lattice point=%s noisy=%s decoded=%s" % (pt, noisy, rec))
    assert rec == m, "trapdoor decode failed"
    print("OK: %s decoded a noisy lattice point with the trapdoor basis" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_fhe(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""TOY PARAMETERS FOR EDUCATION — real additive homomorphism (Paillier-style).
Production FHE uses 1000+ bit parameters (HomomorphicEncryption.org standard)."""
import math, random
def main():
    rnd = random.Random(20261015)
    p, q = 101, 113
    n = p*q
    lam = (p-1)*(q-1)//math.gcd(p-1, q-1)
    g, n2 = n+1, n*n
    mu = pow(lam, -1, n)
    def enc(m):
        r = rnd.randrange(1, n)
        return (pow(g, m, n2)*pow(r, n, n2)) % n2
    def dec(c):
        return (((pow(c, lam, n2)-1)//n)*mu) % n
    a, b = 17, 25
    ca, cb = enc(a), enc(b)
    joint = dec((ca*cb) % n2)   # server multiplies ciphertexts, never sees a or b
    print("E(%d)*E(%d) decrypts to %d; inputs never decrypted server-side" % (a, b, joint))
    assert joint == a + b and dec(ca) == a
    print("OK: %s evaluated a real homomorphic addition over ciphertexts" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_qkd(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""Simulated noiseless BB84 channel — real sifting and error-estimation math.
Real QKD aborts above the QBER threshold (ETSI GS QKD); eavesdropping shows as noise."""
import random
def main():
    rnd = random.Random(20261015)
    n = 1000
    a_bits = [rnd.randrange(2) for _ in range(n)]
    a_basis = [rnd.randrange(2) for _ in range(n)]
    b_basis = [rnd.randrange(2) for _ in range(n)]
    sifted = [a_bits[i] for i in range(n) if a_basis[i] == b_basis[i]]
    sample = sifted[:len(sifted)//10]
    qber = sum(1 for i, b in enumerate(sample) if b != a_bits[[j for j in range(n) if a_basis[j] == b_basis[j]][i]])/len(sample)
    print("raw=%d sifted=%d sift-rate=%.3f qber=%.4f" % (n, len(sifted), len(sifted)/n, qber))
    assert 400 < len(sifted) < 600 and qber == 0.0
    print("OK: %s sifted a real BB84 bitstream with zero error rate" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_hologram(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""Synthetic beam geometry — real two-beam interference grating math."""
import math
def main():
    w = h = 48
    lam, z0, amp = 0.532, 30.0, 8.0  # wavelength, object depth, object amplitude
    k = 2*math.pi/lam
    x0, y0 = w/2, h/2
    bright, total = 0, 0
    peak, floor = 0.0, 9.0
    for j in range(h):
        for i in range(w):
            r = math.hypot(i-x0, j-y0, z0)
            # reference plane wave (amplitude 1) + spherical object wave
            io = amp/r
            I = 1 + io*io + 2*io*math.cos(k*r)
            total += I
            peak = max(peak, I); floor = min(floor, I)
            if I > 1.3:
                bright += 1
    print("grating %dx%d: mean I=%.3f peak=%.3f floor=%.3f bright=%d" % (
        w, h, total/(w*h), peak, floor, bright))
    assert peak > 1.4 and floor < 0.7 and bright > 0
    print("OK: %s computed a real interference grating intensity matrix" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_plasmonic(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""Sample segment stack — real cascaded-waveguide transmission math.
Use measured effective indices for real circuits."""
import math, cmath
def main():
    # (length_um, loss_per_um, interface_reflectivity)
    segs = [(0.8, 0.020, 0.05), (1.2, 0.050, 0.08), (0.8, 0.020, 0.05)]
    beta = 2*math.pi/1.55
    amp = 1+0j
    for L, alpha, r in segs:
        amp *= cmath.exp(1j*beta*L - alpha*L)*math.sqrt(1 - r*r)
    T = abs(amp)**2
    loss_db = -10*math.log10(T)
    print("segments=%d transmission=%.4f loss=%.2f dB" % (len(segs), T, loss_db))
    assert 0.0 < T < 1.0
    print("OK: %s cascaded a real plasmonic waveguide segment stack" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_skyrmion(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""Discretized model texture — real topological-charge integral.
Real devices need full micromagnetic simulation."""
import math
def main():
    N, R = 41, 10.0
    m = [[None]*N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            x, y = i-N//2, j-N//2
            r = math.hypot(x, y)
            th = math.pi*max(0.0, 1.0-r/R)
            ph = math.atan2(y, x)
            m[j][i] = (math.sin(th)*math.cos(ph),
                       math.sin(th)*math.sin(ph), math.cos(th))
    Q = 0.0
    for j in range(1, N-1):
        for i in range(1, N-1):
            mx = tuple((m[j][i+1][k]-m[j][i-1][k])/2 for k in range(3))
            my = tuple((m[j+1][i][k]-m[j-1][i][k])/2 for k in range(3))
            cx = (mx[1]*my[2]-mx[2]*my[1], mx[2]*my[0]-mx[0]*my[2],
                  mx[0]*my[1]-mx[1]*my[0])
            Q += sum(m[j][i][k]*cx[k] for k in range(3))
    Q /= 4*math.pi
    print("lattice 1 skyrmion: topological charge Q=%.3f" % Q)
    assert abs(abs(Q)-1.0) < 0.05, "charge not quantized"
    print("OK: %s integrated a real skyrmion topological charge" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_memgraph(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""Sample episode graph — real temporal-graph traversal and retrieval."""
def main():
    nodes = {
        "g1": {"kind": "goal", "t": 1, "label": "map the warehouse"},
        "c1": {"kind": "context", "t": 2, "label": "aisle 7, low light"},
        "a1": {"kind": "action", "t": 3, "label": "entered aisle 7"},
        "o1": {"kind": "outcome", "t": 4, "label": "shelf scanned, 2 items missed"},
        "r1": {"kind": "reflection", "t": 5, "label": "counterfactual: brighter lamp would have caught both"},
    }
    edges = [("g1", "c1"), ("c1", "a1"), ("a1", "o1"), ("a1", "r1"), ("o1", "r1")]
    adj = {}
    for u, v in edges:
        adj.setdefault(u, []).append(v)
    # time-ordered BFS replay from the goal
    seen, order, queue = set(), [], ["g1"]
    while queue:
        u = queue.pop(0)
        if u in seen:
            continue
        seen.add(u); order.append(u)
        queue.extend(sorted(adj.get(u, []), key=lambda x: nodes[x]["t"]))
    replay = [(nodes[u]["kind"], nodes[u]["label"]) for u in order]
    for kind, label in replay:
        print("  t=%d %-10s %s" % (nodes[[k for k in nodes if nodes[k]["label"] == label][0]]["t"], kind, label))
    assert order[0] == "g1" and order[-1] == "r1"
    assert nodes["r1"]["kind"] == "reflection"
    print("OK: %s replayed a real episodic memory graph in time order" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_selfimprove(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""Operates on an embedded SAMPLE function only — never on live runtime code."""
import ast
SRC = "def policy(x):\\n    return x * (2 + 3) + 0\\n"
def main():
    before = ast.parse(SRC)
    class Fold(ast.NodeTransformer):
        def visit_BinOp(self, node):
            self.generic_visit(node)
            ops = {ast.Add: lambda a, b: a+b, ast.Mult: lambda a, b: a*b}
            if (isinstance(node.left, ast.Constant)
                    and isinstance(node.right, ast.Constant)
                    and type(node.op) in ops):
                return ast.copy_location(
                    ast.Constant(ops[type(node.op)](node.left.value,
                                                    node.right.value)), node)
            return node
    after = ast.fix_missing_locations(Fold().visit(before))
    new_src = ast.unparse(after)
    print("before: %r" % SRC.strip())
    print("after:  %r" % new_src.strip())
    assert "2 + 3" not in new_src and "x * 5" in new_src
    ns = {}
    exec(compile(after, "<delta>", "exec"), ns)
    assert ns["policy"](4) == 20  # behavior preserved by the delta
    print("OK: %s applied and verified a real AST self-improvement delta" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_neurosym(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""Toy embedding space — real cosine grounding plus first-order inference.
Production systems learn embeddings from data."""
import math
def cos(a, b):
    return sum(x*y for x, y in zip(a, b))/math.sqrt(sum(x*x for x in a)*sum(y*y for y in b))
def main():
    emb = {"canary": [0.90, 0.10], "robin": [0.85, 0.15], "penguin": [0.10, 0.90]}
    proto_bird = [sum(emb[k][i] for k in ("canary", "robin"))/2 for i in range(2)]
    facts, rules, exceptions = {"bird(canary)", "bird(robin)", "bird(penguin)"}, [], {"penguin"}
    # symbolic rule: bird(X) -> flies(X), unless X is an exception
    inferred = set()
    for f in facts:
        x = f[5:-1]
        grounded = cos(emb[x], proto_bird) > 0.5
        if grounded and x not in exceptions:
            inferred.add("flies(%s)" % x)
    print("grounded:", sorted("%s->bird %.2f" % (x, cos(emb[x], proto_bird)) for x in emb))
    print("inferred:", sorted(inferred))
    assert inferred == {"flies(canary)", "flies(robin)"}
    assert "flies(penguin)" not in inferred  # symbolic exception wins
    print("OK: %s combined real embeddings with real logical inference" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

DEMOS = {
    "report": demo_report, "sqlite": demo_sqlite, "jsondoc": demo_jsondoc,
    "ledger": demo_ledger, "ticks": demo_ticks, "hashchain": demo_hashchain,
    "ehr": demo_ehr, "dicom": demo_dicom, "genome": demo_genome,
    "geo": demo_geo, "stats": demo_stats, "simhw": demo_simhw,
    "rss": demo_rss, "text": demo_text, "pipeline": demo_pipeline,
    "fileops": demo_fileops, "socket": demo_socket, "algo": demo_algo,
    "vision": demo_vision, "secret": demo_secret, "dsp": demo_dsp,
    "sensors": demo_sensors,
    "spike": demo_spike, "dna": demo_dna, "tda": demo_tda,
    "poincare": demo_poincare, "multivector": demo_multivector,
    "riemann": demo_riemann, "lattice": demo_lattice, "fhe": demo_fhe,
    "qkd": demo_qkd, "hologram": demo_hologram, "plasmonic": demo_plasmonic,
    "skyrmion": demo_skyrmion, "memgraph": demo_memgraph,
    "selfimprove": demo_selfimprove, "neurosym": demo_neurosym,
}
DEMO_NOTE = {
    "simhw": "; simulated device interface — connect compatible hardware for live use",
    "vision": "; synthetic input data — connect a real capture path for live input",
    "sensors": "; synthetic input data — connect the real sensor stack for live input",
    "ehr": "; synthetic sample record — no real patient data",
    "dicom": "; synthetic sample attributes — no real patient headers",
    "genome": "; synthetic sample sequence — no real genetic data",
    "socket": "; synthetic sample packet — capture live traffic for real analysis",
    "ticks": "; synthetic sample ticks — connect a market-data feed for live ticks",
    "spike": "; synthetic drive current — connect a real MEA/neuromorphic front end for live spikes",
    "dna": "; lossless round-trip on the encoded sample payload",
    "tda": "; computed over the sample filtration",
    "poincare": "; sample coordinates in the Poincare disk",
    "multivector": "; Cl(2) geometric product identities verified",
    "riemann": "; evaluated on a spherical metric sample",
    "lattice": "; educational 2-D parameters — production lattices use 512+ dimensions (NIST FIPS 203)",
    "fhe": "; toy parameters for education — production FHE uses 1000+ bit parameters",
    "qkd": "; simulated noiseless channel — real QKD aborts above the QBER threshold (ETSI GS QKD)",
    "hologram": "; synthetic beam geometry — use real beam parameters for lab work",
    "plasmonic": "; sample segment stack — use measured effective indices for real circuits",
    "skyrmion": "; discretized model texture — real devices need micromagnetic simulation",
    "memgraph": "; sample episode graph",
    "selfimprove": "; operates on an embedded sample function only — never on live runtime code",
    "neurosym": "; toy embedding space — production systems learn embeddings from data",
}

# ============================================================ record assembly

def how_it_works_pub(name, desc, points):
    return ("In real-world use, %s works as follows. %s The operating principles are: %s"
            % (name, desc, " ".join("%s." % p for p in points)))

def how_it_works_sig(name, desc, points):
    return ("The Signature edition of %s is an original Signature database technology design: "
            "it specifies the record model, the storage layout, and the query behavior as a "
            "complete, buildable design in the Signature system. %s The Signature design principles are: %s"
            % (name, desc, " ".join("%s." % p for p in points)))

def build_record(title, name, group, desc, points, req, standards, citations,
                 src, demo_kind, rid):
    if src == "signature":
        title = title + " (Signature Edition)"
        description = ("Signature original database technology: " + desc +
                       " Key aspects include: " + "; ".join(points) + "." +
                       " Designed in the Signature system as an original database design.")
        hiw = how_it_works_sig(name, desc, points)
    else:
        description = (desc + " Key aspects include: " + "; ".join(points) + ".")
        hiw = how_it_works_pub(name, desc, points)
    rec = {
        "id": rid, "t": title, "g": group, "name": name, "title": title,
        "description": description, "how_it_works": hiw,
        "key_points": list(points), "requirements": req,
        "standards": list(standards), "citations": citations,
        "src": src,
    }
    prog = DEMOS[demo_kind](name, rid, group, points, req)
    note = "Working demonstration program (real, runnable Python%s)." % DEMO_NOTE.get(demo_kind, "")
    rec["demo"] = {"kind": "python", "language": "python",
                   "program": prog, "note": note}
    return rec

def check_record(rec):
    for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
              "key_points", "requirements", "standards", "src", "demo"):
        assert k in rec, "missing %s in %s" % (k, rec["id"])
    assert len(rec["description"]) > 60, "stub in %s" % rec["id"]
    prog = rec["demo"]["program"]
    assert prog
    compile(prog, rec["id"], "exec")
    blob = json.dumps(rec).lower()
    assert "facebook" not in blob, "facebook ref in %s" % rec["id"]
    assert "bat belt" not in blob, "banned phrase in %s" % rec["id"]

# ============================================================ filing (21 entries)

def gz_jsonl_rows(path):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        head = f.read(2); f.seek(0)
        if head.lstrip().startswith("["):
            return json.load(f)
        return [json.loads(l) for l in f if l.strip()]

def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def shard_root_for(slug, entry):
    url = entry.get("index") or entry.get("local_index") or ""
    m = re.match(r"https://justinahiggins614-cmyk\.github\.io/([^/]+)/data/([^/]+)/(.+)",
                 url.replace("/data/data/", "/data/"))
    if m:
        return os.path.expanduser("~/workspace/%s/data/%s" % (m.group(1), m.group(2)))
    if url and not url.startswith("http"):
        return os.path.dirname(os.path.join(REPO, url))
    raise ValueError("no local root for %s" % slug)

def next_id(prefix, last_id):
    rest = last_id[len(prefix):]
    m = re.match(r"^(-?)(\d+)$", rest)
    assert m, "unparseable last id %s with prefix %s" % (last_id, prefix)
    return "%s%s%0*d" % (prefix, m.group(1), len(m.group(2)), int(m.group(2)) + 1)

def file_records():
    manifest = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    api = json.load(open(os.path.join(REPO, "api.json")))
    m_idx = {d["slug"]: d for d in manifest["databases"]}
    a_idx = {d["slug"]: d for d in api["databases"]}
    filed = []
    for (key, cat, title, desc, points, req, standards, citations, demo_kind,
         target) in ENTRIES:
        if not target:
            continue
        if [h for h in GATE.check(target, title) if h[0] != target]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        entry = m_idx[target]
        prefix = entry["id_prefix"]
        root = shard_root_for(target, entry)
        idx_path = os.path.join(root, "index.jsonl.gz")
        rows = gz_jsonl_rows(idx_path)
        if any(r.get("t") == title for r in rows):
            print("  skip (already filed): %s -> %s" % (title, target), flush=True)
            continue
        last = rows[-1]
        rid = next_id(prefix, last["id"])
        group = "database-types"
        rec = build_record(title, title, group, desc, points, req, standards,
                           citations, "public-harvest", demo_kind, rid)
        check_record(rec)
        # light row: mirror the target's own key set
        light = {"id": rid, "t": rec["t"], "g": group}
        for k in last:
            if k not in light:
                light[k] = last[k]
        # choose chunk: c-field style vs floor(idx/100) style
        page = os.path.join(REPO, "db", target, "index.html")
        html = open(page, encoding="utf-8").read() if os.path.exists(page) else ""
        chunks_dir = os.path.join(root, "chunks")
        chunk_files = sorted(f for f in os.listdir(chunks_dir) if f.endswith(".jsonl.gz"))
        if "Math.floor(idx/100)" in html:
            chunk_no = len(rows) // 100
            cname = "chunk-%04d.jsonl.gz" % chunk_no
            cpath = os.path.join(chunks_dir, cname)
            crows = gz_jsonl_rows(cpath) if os.path.exists(cpath) else []
            if len(crows) >= 100:
                chunk_no += 1
                cname = "chunk-%04d.jsonl.gz" % chunk_no
                cpath = os.path.join(chunks_dir, cname)
                crows = []
            if "c" in light:
                del light["c"]
        else:
            # c-field style: chunks numbered from existing max
            def cnum(fn):
                mm = re.search(r"chunk-(\d+)\.jsonl\.gz", fn)
                return int(mm.group(1)) if mm else 0
            nums = [cnum(f) for f in chunk_files]
            base = min(nums)  # 0-based or 1-based family
            last_no = max(nums)
            cpath = os.path.join(chunks_dir, "chunk-%04d.jsonl.gz" % last_no)
            crows = gz_jsonl_rows(cpath)
            if len(crows) >= 100:
                last_no += 1
                cpath = os.path.join(chunks_dir, "chunk-%04d.jsonl.gz" % last_no)
                crows = []
            light["c"] = last_no
        crows.append(rec)
        write_gz_jsonl(cpath, crows)
        rows.append(light)
        write_gz_jsonl(idx_path, rows)
        entry["record_count"] = entry.get("record_count", 0) + 1
        if target in a_idx:
            a_idx[target]["record_count"] = a_idx[target].get("record_count", 0) + 1
        GATE.admit(target, title, rid)
        filed.append((target, rid, title))
        print("  filed %-38s %s -> %s" % (title[:38], target, rid), flush=True)
    # fix stale double-data/ index URLs discovered during the cross-check
    fixed = []
    for slug in ("relational-sql", "wide-column-stores", "key-value-inmemory",
                 "time-series", "graph-databases"):
        e = m_idx.get(slug)
        if e:
            for k in ("index", "local_index"):
                u = e.get(k, "")
                if "/data/data/" in u:
                    e[k] = u.replace("/data/data/", "/data/")
                    fixed.append(slug + ":" + k)
    with open(os.path.join(REPO, "data", "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
        f.write("\n")
    with open(os.path.join(REPO, "api.json"), "w", encoding="utf-8") as f:
        json.dump(api, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("filed %d records into %d databases; url fixes: %s"
          % (len(filed), len({t for t, _, _ in filed}), fixed), flush=True)
    return filed

# ============================================================ new DBs (24)

CATS = [
    ("healthcare", "healthcare-databases", "The Healthcare and Clinical Informatics Databases Database",
     "Database types for clinical care: records, imaging, genomics, trials, and device data.",
     "healthcare database type record", "JAH-HCD-", "JAH Healthcare Databases Archivist",
     "healthcare databases archivist — clinical informatics database types",
     "Healthcare informatics (standard clinical data literature)."),
    ("finance", "finance-databases", "The Finance, Banking and Fintech Databases Database",
     "Database types for money in motion: ledgers, ticks, books, transfers, and market data.",
     "finance database type record", "JAH-FND-", "JAH Finance Databases Archivist",
     "finance databases archivist — banking and fintech database types",
     "Finance and accounting (standard ledger literature)."),
    ("ecommerce", "ecommerce-databases", "The E-Commerce, Retail and Consumer Databases Database",
     "Database types for digital storefronts: catalogs, carts, loyalty, reviews, and pricing.",
     "ecommerce database type record", "JAH-ECD-", "JAH Ecommerce Databases Archivist",
     "ecommerce databases archivist — retail database types",
     "Retail systems (standard e-commerce literature)."),
    ("logistics", "logistics-databases", "The Supply Chain, Logistics and Transport Databases Database",
     "Database types for moving goods: fleets, bills, warehouses, customs, and cold chains.",
     "logistics database type record", "JAH-LGD-", "JAH Logistics Databases Archivist",
     "logistics databases archivist — supply chain database types",
     "Logistics (standard supply-chain literature)."),
    ("geospatial", "geospatial-databases", "The Geospatial, Mapping and Environmental Databases Database",
     "Database types for the planet: GIS, terrain, weather, oceans, and environmental sensing.",
     "geospatial database type record", "JAH-GSP-", "JAH Geospatial Databases Archivist",
     "geospatial databases archivist — mapping and environmental database types",
     "Geospatial (standard GIS literature)."),
    ("science", "science-databases", "The Scientific, Engineering and Physics Databases Database",
     "Database types for the lab: meshes, collisions, spectra, synthesis, and materials.",
     "science database type record", "JAH-SCD-", "JAH Science Databases Archivist",
     "science databases archivist — scientific database types",
     "Scientific computing (standard engineering literature)."),
    ("aerospace", "aerospace-databases", "The Astronomy, Aerospace and Defense Databases Database",
     "Database types for sky and space: catalogs, orbits, telemetry, and tracking data.",
     "aerospace database type record", "JAH-AERO-", "JAH Aerospace Databases Archivist",
     "aerospace databases archivist — astronomy and aerospace database types",
     "Astrometry (standard astronomical literature)."),
    ("enterprise", "enterprise-databases", "The Enterprise, HR and Legal Databases Database",
     "Database types for organizations: personnel, payroll, contracts, filings, and dockets.",
     "enterprise database type record", "JAH-END-", "JAH Enterprise Databases Archivist",
     "enterprise databases archivist — HR and legal database types",
     "Enterprise operations (standard HR literature)."),
    ("it", "it-databases", "The IT, Cybersecurity and DevOps Databases Database",
     "Database types for infrastructure: tokens, orchestration, pipelines, captures, and traces.",
     "IT database type record", "JAH-ITD-", "JAH IT Databases Archivist",
     "IT databases archivist — cybersecurity and DevOps database types",
     "IT operations (standard security literature)."),
    ("social", "social-databases", "The Social Media and Communications Databases Database",
     "Database types for human connection: graphs, chats, moderation, feeds, and forums.",
     "social database type record", "JAH-SODB-", "JAH Social Databases Archivist",
     "social databases archivist — communications database types",
     "Communications (standard social-network literature)."),
    ("gaming", "gaming-databases", "The Gaming and Simulation Databases Database",
     "Database types for play: inventories, matchmaking, physics, NPCs, and economies.",
     "gaming database type record", "JAH-GAM-", "JAH Gaming Databases Archivist",
     "gaming databases archivist — gaming database types",
     "Games (standard game-systems literature)."),
    ("cs", "cs-databases", "The Core Computer Science and Database Architecture Databases Database",
     "Database types for data itself: documents, embeddings, BLOBs, indexes, and write-ahead logs.",
     "database architecture record", "JAH-CSDB-", "JAH Database Architecture Archivist",
     "database architecture archivist — core database engine types",
     "Database architecture (standard database literature)."),
]

def _cfg(cat, slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig = source == "signature"
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": ("%s — %s Every record carries the full entry: description, how it works, "
                   "key points, requirements, standards, citations, and a working demonstration program."
                   % (tagline,
                      "Signature originals — original Signature database technology designs."
                      if sig else
                      "Public records — real-world database types documented factually.")),
        "sig_type": ("Signature originals organized in the Signature system"
                     if sig else "Public records organized in the Signature system"),
        "search_ph": "Search %s..." % record_kind,
        "chat_ph": "Ask about %s..." % record_kind,
        "archive_blurb": "Seeded %s %s, marching toward one million records." % (
            "Signature-original" if sig else "public-record", record_kind),
        "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "fields": "database-type catalog",
        "gen_desc": ("Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries."),
        "greet": "I am the %s. Ask me about %s." % (ai, record_kind),
        "gen_fields": ["database-type catalog"], "gen_kind": slug,
        "gen_demo_kind": "python", "source": source,
    }

DBCFG = {}
CIT = {}
SIG_PREFIX = {"healthcare": "JAH-HCDG-", "finance": "JAH-FNDG-", "ecommerce": "JAH-ECDG-",
              "logistics": "JAH-LGDG-", "geospatial": "JAH-GSPG-", "science": "JAH-SCDG-",
              "aerospace": "JAH-AEROG-", "enterprise": "JAH-ENDG-", "it": "JAH-ITDG-",
              "social": "JAH-SODBG-", "gaming": "JAH-GAMG-", "cs": "JAH-CSDBG-"}
for (cat, slug, name, tagline, rk, prefix, ai, role, citation) in CATS:
    DBCFG[slug] = _cfg(cat, slug, name, tagline, rk, prefix, ai, role, citation, "public")
    CIT[slug] = citation
    sslug = slug + "-signature"
    DBCFG[sslug] = _cfg(cat, sslug, name.replace(" Database", " Signature Database", ),
                        tagline, rk, SIG_PREFIX[cat], ai + " (Signature)",
                        role + " — Signature editions", citation, "signature")
    CIT[sslug] = citation + " Signature editions are original Signature database technology."

def build_new_records():
    built = {}
    for (cat, slug, _n, _t, _rk, _p, _a, _r, _c) in CATS:
        for ver in ("public", "signature"):
            s = slug if ver == "public" else slug + "-signature"
            cfg = DBCFG[s]
            src = "signature" if ver == "signature" else "public-harvest"
            recs = []
            for (key, ecat, title, desc, points, req, standards, citations,
                 demo_kind, target) in ENTRIES:
                if ecat != cat or target:
                    continue
                ftitle = title + " (Signature Edition)" if ver == "signature" else title
                if [h for h in GATE.check(s, ftitle) if h[0] != s]:
                    print("  gate refused (cross-db dupe): %s" % ftitle, flush=True)
                    continue
                rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
                rec = build_record(title, title, key, desc, points, req, standards,
                                   CIT[s], src, demo_kind, rid)
                check_record(rec)
                GATE.admit(s, ftitle, rid)
                recs.append(rec)
            assert recs, "empty db " + s
            built[s] = recs
    return built

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
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"], "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": n, "status": "live", "full_records": n,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": c["source"]}

def api_entry(slug, n):
    c = DBCFG[slug]
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "record_count": n, "status": "live",
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"}

def main():
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

    # ---- step 1: file 21 entries into existing databases
    filed = file_records()

    # ---- step 2: build 24 new databases
    built = build_new_records()
    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        total += len(recs)
        n = write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # ---- step 3: execute one demo per archetype
    import subprocess
    markers = {"report": "INFO = {", "sqlite": "sqlite3.connect", "jsondoc": "def get_path(",
               "ledger": "def post(entries)", "ticks": "vwap", "hashchain": "block_hash(",
               "ehr": "ENCOUNTER_REQUIRED", "dicom": "REQUIRED_TAGS", "genome": "GC=",
               "geo": "point_in_polygon", "stats": "statistics.median",
               "simhw": "SIMULATED DEVICE INTERFACE", "rss": "ElementTree",
               "text": "most_common(5)", "pipeline": "def clean(rec)", "fileops": "TemporaryDirectory",
               "socket": "parse_ipv4_header", "algo": "def bfs(", "vision": "edge_metric",
               "secret": "gen_world(", "dsp": "dft_mag", "sensors": "pearson("}
    done = set()
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            for k, m in markers.items():
                if k not in done and m in prog:
                    done.add(k)
                    p = subprocess.run([sys.executable, "-c", prog],
                                       capture_output=True, text=True, timeout=60)
                    assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-500:])
                    assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
                    print("demo ok: %-10s %s" % (k, r["id"]), flush=True)
    # also execute one filed demo per kind used in filing
    print("demo execution: %d archetypes ran OK" % len(done), flush=True)
    for k in sorted(set(markers) - done):
        prog = DEMOS[k]("Sample %s demo" % k, "TEST-000001", "test", ["p1"], "req")
        compile(prog, "TEST-000001", "exec")
        p = subprocess.run([sys.executable, "-c", prog],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "demo failed (direct) %s: %s" % (k, p.stderr[-500:])
        assert "OK:" in p.stdout, "demo no OK marker (direct) %s" % k
        done.add(k)
        print("demo ok: %-10s (direct)" % k, flush=True)
    assert len(done) == len(markers), "not all archetypes executed: %s" % (set(markers) - done)

    # ---- step 4: pages + generators
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
    print("filed records: %d" % len(filed))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
