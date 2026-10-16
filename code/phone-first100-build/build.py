#!/usr/bin/env python3
"""Build the smartphone first-100 tools archive for JAH Databases.

4 section DBs (paste sections S1-S4), each with a PUBLIC and a SIGNATURE
version -> 8 DBs, 200 records (100 entries x 2).

Entries 101-255 were already built as 18 DBs in phase A (slugs phone-*);
this set (1-100) is NEW and uses non-colliding slugs.

Public version: the tool as it exists when a phone performs it (src
public-harvest, honest capability/limits, phone-as-instrument framing).
Signature version: his original Signature engineering writeup + working demo
(src signature, titles suffixed " (Signature Edition)").

Every record: description + how-it-works + key points + requirements +
citations + working demonstration code (real, runnable, stdlib-only Python;
hardware-dependent demos use clearly-labeled simulated device interfaces;
vision/sensor demos use clearly-labeled synthetic input data).

6 titles collide (normalized) with records in OTHER databases
(computer-utilities, hardware-interfaces-lab, electrical-electronic-testing,
wireless-radio-em-instruments, optical-imaging-inspection). Those records get
the "Smartphone " title prefix so the whole-system dedupe gate stays green
while no pasted entry is dropped; the `name` field stays verbatim.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base

sys.path.insert(0, HERE)
from entries_first100 import FIRST100_ENTRIES

# Point the shared helpers at OUR db config (they read the module global).
DBCFG = {}
CIT = {}

SECTIONS = [
 ("phone-sensor-tools", "The Smartphone Sensor and Measurement Tools Database",
  "Everyday sensor instruments a phone performs through programming: compass, magnetometry, motion, audio, light, and location sensing.",
  "sensor and measurement tool record", "JAH-PST-", "JAH Sensor Tool Archivist",
  "sensor archivist — phone-performed measurement instruments",
  "Sensor and measurement instruments (standard instrumentation literature)."),
 ("phone-optical-inspection", "The Smartphone Optical and Inspection Tools Database",
  "Camera instruments a phone performs through programming: inspection, OCR, defect detection, tracking, and environmental vision.",
  "optical and inspection tool record", "JAH-POI-", "JAH Optical Inspection Archivist",
  "optical archivist — camera-based inspection instruments",
  "Optical inspection and imaging (standard imaging literature)."),
 ("phone-wireless-comms", "The Smartphone Wireless and Communications Tools Database",
  "Radio and network instruments a phone performs through programming: wireless surveys, network diagnostics, and hardware-interface consoles.",
  "wireless and communications tool record", "JAH-PWC-", "JAH Wireless Comms Archivist",
  "wireless archivist — radio and network instruments",
  "Wireless and network engineering (standard networking literature)."),
 ("phone-diagnostic-computing", "The Smartphone Diagnostic and Computing Tools Database",
  "Bench and computing instruments a phone performs through programming: test-equipment interfaces, cryptography, AI assistance, and the unified multi-tool platform.",
  "diagnostic and computing tool record", "JAH-PDC-", "JAH Diagnostic Computing Archivist",
  "diagnostics archivist — phone-performed test and computing instruments",
  "Diagnostics and computing (standard electronics and computer science literature)."),
]

for (slug, name, tagline, rk, prefix, ai, role, citation) in SECTIONS:
    DBCFG[slug] = base._cfg(slug, name, tagline, rk, prefix, ai, role, None, citation, "public")
    DBCFG[slug + "-signature"] = base._cfg(
        slug + "-signature", name.replace(" Database", " Signature Database"),
        tagline, rk, prefix[:-1] + "G-",
        ai + " (Signature)", role + " — Signature editions",
        None, citation, "signature")
    CIT[slug] = citation
    CIT[slug + "-signature"] = citation + " Signature editions are original Signature engineering."

base.DBCFG = DBCFG

# Titles that collide (normalized) with records in other databases.
TITLE_PREFIX = {
    "3D Object Scanner", "Wi-Fi Signal Strength Meter", "Bluetooth Device Scanner",
    "Digital Multimeter Interface", "Signal Generator Controller", "File Hash Calculator",
}

def demo_netinfo(name, rid, group, points, req):
    return base._hdr(name, rid, group) + '''\
"""Real network-interface enumeration on loopback only — demonstrates the
interface-inspection logic for ''' + name.replace('"""', '"') + '''. No external
host is touched; real OS network APIs are exercised locally."""
import socket
def main():
    host = socket.gethostname()
    print("hostname:", host)
    infos = socket.getaddrinfo("localhost", None, type=socket.SOCK_STREAM)
    addrs = sorted({i[4][0] for i in infos})
    print("localhost addresses:", addrs)
    assert addrs, "no loopback addresses found"
    for fam, label in ((socket.AF_INET, "IPv4"), (socket.AF_INET6, "IPv6")):
        try:
            s = socket.socket(fam, socket.SOCK_STREAM)
            s.bind(("localhost", 0))
            print("%s loopback bind OK, ephemeral port %d" % (label, s.getsockname()[1]))
            s.close()
        except OSError as e:
            print("%s loopback unavailable: %s" % (label, e))
    print("OK: %s enumerated real local network interfaces" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''

base.DEMOS["netinfo"] = demo_netinfo

def build_records(slug, source):
    cfg = DBCFG[slug]
    base_slug = slug[:-len("-signature")] if source == "signature" else slug
    entries = [e for e in FIRST100_ENTRIES if e[0] == base_slug]
    recs = []
    for (sec, name, desc, points, demo_kind, req) in entries:
        if name in TITLE_PREFIX:
            title = "Smartphone " + name
        else:
            title = name
        if source == "signature":
            title = title + " (Signature Edition)"
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
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
            "how_it_works": base.how_it_works(name, sec, req, source == "signature"),
            "key_points": list(points),
            "requirements": req,
            "standards": ["Documented behavior for " + sec.replace("-", " ")],
            "citations": CIT[slug],
            "src": "signature" if source == "signature" else "public-harvest",
        }
        demo_fn = base.DEMOS.get(demo_kind, base.demo_report)
        program = demo_fn(name, rid, sec, points, req)
        sim = "; simulated device interface — connect compatible hardware for live use" if demo_kind == "simhw" else ""
        syn = ("; synthetic input data — connect a real camera/sensor for live input"
               if demo_kind in ("vision", "sensors") else "")
        note = "Working demonstration program (real, runnable Python%s%s)." % (sim, syn)
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program, "note": note}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    return recs

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
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    import subprocess
    markers = {"simhw": "SIMULATED DEVICE INTERFACE", "vision": "SYNTHETIC INPUT DATA",
               "sensors": "SYNTHETIC SENSOR STREAM", "geo": "Real positioning math",
               "dsp": "dft_mag", "stats": "random.gauss", "socket": "socket.getaddrinfo",
               "pipeline": "def clean(rec)", "algo": "def bfs(", "text": "Counter(",
               "report": "INFO = {", "fileops": "TemporaryDirectory", "hash": "hashlib.new(",
               "netinfo": "gethostname"}
    # fill markers for archetypes used by this build that base never executes
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
    # only require the archetypes this build actually uses
    used = set()
    for recs in built.values():
        for r in recs:
            prog = r["demo"]["program"]
            for k, m in markers.items():
                if m in prog:
                    used.add(k)
    assert used <= done, "not all used archetypes executed: %s" % (used - done)
    print("demo execution: %d archetypes ran OK" % len(done), flush=True)

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

    entries_m = [base.manifest_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [base.api_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases, %d records" % (len(built), total))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
