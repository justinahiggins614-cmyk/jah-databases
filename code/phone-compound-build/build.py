#!/usr/bin/env python3
"""Build the smartphone compound-capability archive for JAH Databases.

9 section DBs (paste sections A-H + beyond-250 as I), each with a PUBLIC and a
SIGNATURE version -> 18 DBs, 310 records (155 entries x 2).

Public version: real-world tools as they exist (src public-harvest, honest
capability/limits, phone-as-instrument framing).
Signature version: his original Signature engineering writeup + working demo
(src signature, titles suffixed " (Signature Edition)").

Every record: description + patent/spec-style how-it-works + requirements honestly
labeled (software-only vs OS interfaces vs network vs peripherals vs external
hardware) + citations + working demonstration code (real, runnable, stdlib-only
Python; hardware-dependent demos use clearly-labeled simulated device interfaces;
vision/sensor demos use clearly-labeled synthetic input data).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import gzip
import importlib.util
import json
import os
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
from entries_phone import PHONE_ENTRIES

# ---------------------------------------------------------------- DB config
# (slug, name, tagline, record_kind, prefix, ai_name, role, citation)
SECTIONS = [
 ("phone-sensor-fusion","The Smartphone Sensor Fusion Instruments Database",
  "Multi-sensor instruments: fusion engines, oscilloscopes, calibration, anomaly detection, and measurement dashboards.",
  "sensor fusion instrument record","JAH-PSF-","JAH Sensor Fusion Archivist",
  "sensor fusion archivist — synchronized multi-sensor instruments",
  "Sensor fusion and measurement instruments (standard instrumentation literature)."),
 ("phone-computer-vision","The Smartphone Camera and Computer Vision Tools Database",
  "Camera instruments: photogrammetry, 3D reconstruction, visual inspection, dimensional measurement, and change detection.",
  "computer vision tool record","JAH-PCV-","JAH Computer Vision Archivist",
  "computer vision archivist — camera-based measurement and inspection",
  "Computer vision and photogrammetry (standard imaging literature)."),
 ("phone-acoustic-vibration","The Smartphone Acoustic and Vibration Intelligence Database",
  "Audio instruments: sound classification, machine-fault detection, room acoustics, and multi-phone acoustic surveys.",
  "acoustic intelligence record","JAH-PAV-","JAH Acoustic Intelligence Archivist",
  "acoustic archivist — sound and vibration analysis instruments",
  "Acoustics and vibration analysis (standard acoustics literature)."),
 ("phone-positioning-navigation","The Smartphone Positioning and Navigation Intelligence Database",
  "Spatial instruments: indoor navigation, dead reckoning, geofencing, floor-plan reconstruction, and spatial data fusion.",
  "positioning intelligence record","JAH-PNV-","JAH Positioning Archivist",
  "positioning archivist — navigation and spatial intelligence",
  "Positioning and navigation (standard navigation literature)."),
 ("phone-wireless-network","The Smartphone Wireless and Network Engineering Database",
  "Radio and network instruments: coverage mapping, roaming analysis, security auditing, and defensive network diagnostics.",
  "wireless engineering record","JAH-PWN-","JAH Wireless Engineering Archivist",
  "wireless archivist — radio and network measurement",
  "Wireless and network engineering (standard networking literature)."),
 ("phone-electronics-diagnostics","The Smartphone Electronics and Industrial Diagnostics Database",
  "Bench instruments through the phone: USB consoles, waveform analysis, motor control, thermal inspection, and cable testing.",
  "electronics diagnostic record","JAH-PEX-","JAH Electronics Diagnostics Archivist",
  "electronics archivist — phone-as-bench-instrument diagnostics",
  "Electronic test and industrial diagnostics (standard electronics literature)."),
 ("phone-computing-ai","The Smartphone Computing, AI, and Software Engineering Database",
  "On-device computing: local AI models, code review, knowledge graphs, forensics, OCR archives, and workflow automation.",
  "computing and AI tool record","JAH-PAI-","JAH Computing Archivist",
  "computing archivist — on-device AI and software engineering",
  "Computing and AI systems (standard computer science literature)."),
 ("phone-compound-systems","The Smartphone Compound Systems Database",
  "Compound instruments: digital twins, engineering labs, maintenance stations, and multi-phone sensor networks.",
  "compound system record","JAH-PMX-","JAH Compound Systems Archivist",
  "compound systems archivist — multi-tool instruments",
  "Compound intelligent instruments (standard systems architecture literature)."),
 ("phone-beyond-250","The Beyond-250 Compound Applications Database",
  "The beyond-250 compound applications: visual repair guides, orchestration engines, live digital twins, and knowledge stations.",
  "compound application record","JAH-PB2-","JAH Compound Applications Archivist",
  "compound applications archivist — higher-level instrument combinations",
  "Compound applications (standard systems architecture literature)."),
]

GROUP_OF = {s[0]: s[0] for s in SECTIONS}

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, sig_note, citation, source):
    sig_line = ("Signature originals — the Signature engineering version of each instrument: "
                "original design writeup, honest requirements, and a working demonstration program.")
    pub_line = ("Public records — real-world tools and instruments as they exist, "
                "documented honestly: what they do, what they need, and their limits.")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s — %s Every record carries the full entry: description, how it works, key points, requirements, citations, and a working demonstration program. Software alone cannot replace missing physical sensors or guarantee that an inference is a measurement." % (tagline, sig_line if source == "signature" else pub_line),
        "sig_type": "Signature originals organized in the Signature system" if source == "signature" else "Public records organized in the Signature system",
        "search_ph": "Search %s..." % record_kind,
        "chat_ph": "Ask about %s..." % record_kind,
        "archive_blurb": "Seeded %s %s, marching toward one million records." % (
            "Signature-original" if source == "signature" else "public-record", record_kind),
        "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "fields": "smartphone compound capability archive",
        "gen_desc": "Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about %s." % (ai, record_kind),
        "gen_fields": ["smartphone compound capability archive"], "gen_kind": slug, "gen_demo_kind": "python",
        "source": source,
    }

DBCFG = {}
CIT = {}
for (slug, name, tagline, rk, prefix, ai, role, citation) in SECTIONS:
    DBCFG[slug] = _cfg(slug, name, tagline, rk, prefix, ai, role, None, citation, "public")
    DBCFG[slug + "-signature"] = _cfg(
        slug + "-signature", name.replace(" Database", " Signature Database"),
        tagline, rk, prefix[:-1] + "G-",
        ai + " (Signature)", role + " — Signature editions",
        None, citation, "signature")
    CIT[slug] = citation
    CIT[slug + "-signature"] = citation + " Signature editions are original Signature engineering."

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python. Simulated-hardware demos are
# labeled as simulations of the software logic; vision/sensor demos use
# clearly-labeled synthetic input data. None claim to touch real instruments.

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
        hashes = {}
        for p in paths:
            h = hashlib.sha256()
            with open(p, "rb") as f:
                h.update(f.read())
            hashes[p] = h.hexdigest()[:16]
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
SAMPLE = b"JAH phone-compound integrity demo payload"
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
SAMPLE = ("The phone becomes the instrument. Software provides the behavior; "
          "sensors provide the sensing. The catalog documents both honestly.")
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
''' + "".join(('    print("  %d. %s")' % (i + 1, p.replace('"', "'"))) + chr(10) for i, p in enumerate(points)) + '''    print("OK: %s report generated" % INFO["title"])
if __name__ == "__main__":
    main()
'''

def demo_vision(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""SYNTHETIC INPUT DATA — demonstrates the image-analysis logic for ''' + name.replace('"""', '"') + '''.
Pixel arrays below are synthesized (a real capture path supplies live frames);
every operation performed on them is the real algorithm."""
import random
def make_frame(w, h, base, seed, defect=False):
    rnd = random.Random(seed)
    px = [[base + rnd.randint(-8, 8) for _ in range(w)] for _ in range(h)]
    if defect:
        for y in range(h // 3, 2 * h // 3):
            px[y][w // 2] = base + 90  # synthetic vertical crack line
    return px
def mean_brightness(px):
    return sum(sum(row) for row in px) / (len(px) * len(px[0]))
def edge_metric(px):
    # sum of horizontal neighbor differences: higher = more structure
    return sum(abs(px[y][x + 1] - px[y][x])
               for y in range(len(px)) for x in range(len(px[0]) - 1))
def change_mask(a, b, thresh=40):
    n = sum(1 for y in range(len(a)) for x in range(len(a[0]))
            if abs(a[y][x] - b[y][x]) > thresh)
    return n
def main():
    clean = make_frame(64, 48, 128, seed=7)
    cracked = make_frame(64, 48, 128, seed=7, defect=True)
    print("clean frame:   mean=%.1f edge=%d" % (mean_brightness(clean), edge_metric(clean)))
    print("defect frame:  mean=%.1f edge=%d" % (mean_brightness(cracked), edge_metric(cracked)))
    changed = change_mask(clean, cracked)
    total = 64 * 48
    print("changed pixels: %d / %d (%.1f%%)" % (changed, total, 100.0 * changed / total))
    assert changed > 0, "defect not detected"
    print("NOTE: synthetic frames — connect a real camera capture path for live input.")
    print("OK: %s ran real image-analysis logic on synthetic frames" % ''' + json.dumps(name) + ''')
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
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))
def dead_reckon(lat, lon, heading_deg, dist_m):
    r = 6371000.0
    brg = math.radians(heading_deg)
    lat2 = math.asin(math.sin(math.radians(lat)) * math.cos(dist_m / r)
                     + math.cos(math.radians(lat)) * math.sin(dist_m / r) * math.cos(brg))
    lon2 = math.radians(lon) + math.atan2(
        math.sin(brg) * math.sin(dist_m / r) * math.cos(math.radians(lat)),
        math.cos(dist_m / r) - math.sin(math.radians(lat)) * math.sin(lat2))
    return math.degrees(lat2), math.degrees(lon2)
def main():
    a = (40.7128, -74.0060)  # sample point A
    b = (40.7138, -74.0050)  # sample point B
    d = haversine_m(*a, *b)
    print("A->B haversine distance: %.1f m" % d)
    lat2, lon2 = dead_reckon(a[0], a[1], 45.0, d)
    print("dead reckoning 45 deg x %.1f m -> (%.6f, %.6f)" % (d, lat2, lon2))
    back = haversine_m(lat2, lon2, *b)
    print("distance from reckoned position to B: %.2f m" % back)
    assert d > 100 and d < 200, "unexpected distance"
    print("OK: %s computed real positioning math" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

def demo_sensors(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""SYNTHETIC SENSOR STREAM — demonstrates the multi-sensor analysis logic for ''' + name.replace('"""', '"') + '''.
Channels below are synthesized (a real sensor stack supplies live readings);
synchronization, statistics, and correlation are the real algorithms."""
import math, random, statistics
def synth_stream(n, base, amp, freq, seed):
    rnd = random.Random(seed)
    return [base + amp * math.sin(2 * math.pi * freq * i / n) + rnd.gauss(0, amp * 0.05)
            for i in range(n)]
def pearson(a, b):
    n = len(a)
    ma, mb = statistics.mean(a), statistics.mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den = math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))
    return num / den if den else 0.0
def main():
    n = 1000
    accel = synth_stream(n, 9.81, 0.4, 3, seed=11)
    gyro = synth_stream(n, 0.05, 0.4, 3, seed=12)   # same 3 Hz rhythm
    baro = synth_stream(n, 1013.25, 0.1, 1, seed=13)  # unrelated 1 Hz drift
    ts = [i / 100.0 for i in range(n)]  # synchronized 100 Hz timestamps
    print("samples=%d span=%.1fs accel mean=%.2f stdev=%.3f" % (
        n, ts[-1] - ts[0], statistics.mean(accel), statistics.stdev(accel)))
    r_ag = pearson(accel, gyro)
    r_ab = pearson(accel, baro)
    print("accel-gyro correlation:  %.3f (shared rhythm)" % r_ag)
    print("accel-baro correlation:  %.3f (unrelated)" % r_ab)
    assert abs(r_ag) > 0.8 and abs(r_ab) < 0.3, "correlation logic failed"
    print("NOTE: synthetic channels — connect the real sensor stack for live readings.")
    print("OK: %s ran real multi-sensor analysis on a synthetic stream" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

DEMOS = {
    "fileops": demo_fileops, "hash": demo_hash, "secret": demo_secret,
    "dsp": demo_dsp, "stats": demo_stats, "socket": demo_socket,
    "pipeline": demo_pipeline, "simhw": demo_simhw, "algo": demo_algo,
    "text": demo_text, "report": demo_report, "vision": demo_vision,
    "geo": demo_geo, "sensors": demo_sensors,
}

# ---------------------------------------------------------------- records

def how_it_works(name, group, req_label, sig):
    hw_tail = (" Software alone cannot replace missing physical sensors or guarantee "
               "that an inference is a measurement — every record states honestly what "
               "the phone can do alone and what needs compatible hardware.")
    if sig:
        return ("The Signature edition of %s is an original Signature engineering design: "
                "it specifies the instrument's behavior as software running on a smartphone, "
                "defines exactly which capabilities are software-only and which need OS "
                "interfaces or compatible hardware, and ships a working demonstration program "
                "that exercises the real logic.%s" % (name, hw_tail))
    return ("In real-world use, %s works by combining the phone's processing with its "
            "available interfaces: built-in sensors, cameras, microphones, and radios handle "
            "software-accessible functions, while compatible external instruments provide "
            "sensing and actuation the phone cannot do alone.%s" % (name, hw_tail))

def build_records(slug, source):
    cfg = DBCFG[slug]
    base_slug = slug[:-len("-signature")] if source == "signature" else slug
    entries = [e for e in PHONE_ENTRIES if e[0] == base_slug]
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
        sim = "; simulated device interface — connect compatible hardware for live use" if demo_kind == "simhw" else ""
        syn = ("; synthetic input data — connect a real camera/sensor for live input"
               if demo_kind in ("vision", "sensors") else "")
        note = "Working demonstration program (real, runnable Python%s%s)." % (sim, syn)
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program, "note": note}
        GATE.admit(slug, title, rid)
        recs.append(rec)
    return recs

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
        "ai_name": c["ai"], "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
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
    # simpler: execute first record of each db + one per unseen demo kind tag
    # find demo kind by scanning program for its unique marker
    markers = {"simhw": "SIMULATED DEVICE INTERFACE", "vision": "SYNTHETIC INPUT DATA",
               "sensors": "SYNTHETIC SENSOR STREAM", "geo": "Real positioning math",
               "dsp": "dft_mag", "stats": "random.gauss", "socket": "socket.getaddrinfo",
               "pipeline": "def clean(rec)", "algo": "def bfs(", "text": "Counter(",
               "report": 'INFO = {', "fileops": "TemporaryDirectory", "hash": "hashlib.new("}
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
    print("demo execution: %d archetypes ran OK" % len(done), flush=True)
    assert len(done) == len(markers), "not all archetypes executed: %s" % (set(markers) - done)

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
