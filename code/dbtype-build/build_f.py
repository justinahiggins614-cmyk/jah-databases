#!/usr/bin/env python3
"""PHASE F — database-type catalog build (dbtype paste 3).

- Files 12 entries as full canon records into existing covering databases.
- Builds 3 new <category>-databases DBs (public + signature) = 6 DBs,
  16 records, for the 8 orphaned entries.
Safety: public-safety/forensics entries are descriptive systems documentation
only — no operational tradecraft how-tos.
- Whole-system dedupe via code/dedupe_gate.py. Canon page/chunk/index
  pattern from code/phone-compound-build. No website references, no
  Facebook, no banned phrases.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(HERE))
sys.path.insert(0, os.path.join(REPO, "code"))
from entries_f import ENTRIES
import build as B

GATE = B.GATE
GROUP = "database-types"

# ============================================================ new DB config

NEWCATS = [
    ("hospitality-events", "hospitality-events-databases",
     "The Hospitality and Event Ticketing Databases Database",
     "Database types for venues and events: seat maps, pricing tiers, and ticket validation.",
     "hospitality database type record", "JAH-HTEV-", "JAH Hospitality Events Databases Archivist",
     "hospitality events databases archivist — venue and ticketing database types",
     "Hospitality and travel operations (standard hotel, airline, and venue management literature)."),
    ("public-safety", "public-safety-databases",
     "The Public Safety and Forensics Databases Database",
     "Database types for public safety systems: identification, dispatch, and records — descriptive documentation only.",
     "public safety database type record", "JAH-PSAF-", "JAH Public Safety Databases Archivist",
     "public safety databases archivist — public safety database types",
     "Public safety systems (standard forensic science and emergency communications literature)."),
    ("communications-broadcast", "communications-broadcast-databases",
     "The Communications and Broadcast Databases Database",
     "Database types for real-time communications: captioning, playout automation, and telecom billing.",
     "communications database type record", "JAH-CBDC-", "JAH Communications Broadcast Databases Archivist",
     "communications broadcast databases archivist — broadcast database types",
     "Broadcasting and telecommunications (standard broadcast engineering and telecom literature)."),
]

SIG_PREFIX = {"hospitality-events": "JAH-HTEVG-", "public-safety": "JAH-PSAFG-",
              "communications-broadcast": "JAH-CBDCG-"}


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
for (cat, slug, name, tagline, rk, prefix, ai, role, citation) in NEWCATS:
    DBCFG[slug] = _cfg(cat, slug, name, tagline, rk, prefix, ai, role, citation, "public")
    CIT[slug] = citation
    sslug = slug + "-signature"
    DBCFG[sslug] = _cfg(cat, sslug, name.replace(" Database", " Signature Database", ),
                        tagline, rk, SIG_PREFIX[cat], ai + " (Signature)",
                        role + " — Signature editions", citation, "signature")
    CIT[sslug] = citation + " Signature editions are original Signature database technology."

NEWCAT_KEYS = {cat for (cat, *_rest) in NEWCATS}

# ============================================================ filing

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
        root = B.shard_root_for(target, entry)
        idx_path = os.path.join(root, "index.jsonl.gz")
        rows = B.gz_jsonl_rows(idx_path)
        if any(r.get("t") == title for r in rows):
            print("  skip (already filed): %s -> %s" % (title, target), flush=True)
            continue
        rid = B.next_id(prefix, rows[-1]["id"])
        rec = B.build_record(title, title, GROUP, desc, points, req, standards,
                             citations, "public-harvest", demo_kind, rid)
        B.check_record(rec)
        light = {"id": rid, "t": rec["t"], "g": GROUP}
        for k in rows[-1]:
            if k not in light:
                light[k] = rows[-1][k]
        page = os.path.join(REPO, "db", target, "index.html")
        html = open(page, encoding="utf-8").read() if os.path.exists(page) else ""
        chunks_dir = os.path.join(root, "chunks")
        chunk_files = sorted(f for f in os.listdir(chunks_dir) if f.endswith(".jsonl.gz"))
        if "Math.floor(idx/100)" in html:
            chunk_no = len(rows) // 100
            cname = "chunk-%04d.jsonl.gz" % chunk_no
            cpath = os.path.join(chunks_dir, cname)
            crows = B.gz_jsonl_rows(cpath) if os.path.exists(cpath) else []
            if len(crows) >= 100:
                chunk_no += 1
                cname = "chunk-%04d.jsonl.gz" % chunk_no
                cpath = os.path.join(chunks_dir, cname)
                crows = []
            if "c" in light:
                del light["c"]
        else:
            def cnum(fn):
                mm = re.search(r"chunk-(\d+)\.jsonl\.gz", fn)
                return int(mm.group(1)) if mm else 0
            nums = [cnum(f) for f in chunk_files]
            last_no = max(nums)
            cpath = os.path.join(chunks_dir, "chunk-%04d.jsonl.gz" % last_no)
            crows = B.gz_jsonl_rows(cpath)
            if len(crows) >= 100:
                last_no += 1
                cpath = os.path.join(chunks_dir, "chunk-%04d.jsonl.gz" % last_no)
                crows = []
            light["c"] = last_no
        crows.append(rec)
        B.write_gz_jsonl(cpath, crows)
        rows.append(light)
        B.write_gz_jsonl(idx_path, rows)
        entry["record_count"] = entry.get("record_count", 0) + 1
        if target in a_idx:
            a_idx[target]["record_count"] = a_idx[target].get("record_count", 0) + 1
        GATE.admit(target, title, rid)
        filed.append((target, rid, title))
        print("  filed %-38s %s -> %s" % (title[:38], target, rid), flush=True)
    with open(os.path.join(REPO, "data", "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
        f.write("\n")
    with open(os.path.join(REPO, "api.json"), "w", encoding="utf-8") as f:
        json.dump(api, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("filed %d records into %d databases"
          % (len(filed), len({t for t, _, _ in filed})), flush=True)
    return filed


# ============================================================ new DBs

def build_new_records():
    built = {}
    for (cat, slug, _n, _t, _rk, _p, _a, _r, _c) in NEWCATS:
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
                rec = B.build_record(title, title, key, desc, points, req, standards,
                                     CIT[s], src, demo_kind, rid)
                B.check_record(rec)
                GATE.admit(s, ftitle, rid)
                recs.append(rec)
            assert recs, "empty db " + s
            built[s] = recs
    return built


def write_shard_db(slug, recs):
    base = os.path.join(SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    B.write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        B.write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
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

    # ---- step 1: file 12 entries into existing databases
    filed = file_records()

    # ---- step 2: build 6 new databases (3 categories x public+signature)
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

    # ---- step 3: execute one demo per used archetype
    used = set()
    filed_progs = []
    for slug, recs in built.items():
        for r in recs:
            filed_progs.append((r["id"], r["demo"]["program"]))
    markers = {"report": "INFO = {", "sqlite": "sqlite3.connect", "jsondoc": "def get_path(",
               "ledger": "def post(entries)", "ticks": "vwap", "hashchain": "block_hash(",
               "ehr": "ENCOUNTER_REQUIRED", "dicom": "REQUIRED_TAGS", "genome": "GC=",
               "geo": "point_in_polygon", "stats": "statistics.median",
               "simhw": "SIMULATED DEVICE INTERFACE", "rss": "ElementTree",
               "text": "most_common(5)", "pipeline": "def clean(rec)", "fileops": "TemporaryDirectory",
               "socket": "parse_ipv4_header", "algo": "def bfs(", "vision": "edge_metric",
               "secret": "gen_world(", "dsp": "dft_mag", "sensors": "pearson("}
    done = set()
    for rid, prog in filed_progs:
        for k, m in markers.items():
            if k not in done and m in prog:
                done.add(k)
                p = subprocess.run([sys.executable, "-c", prog],
                                   capture_output=True, text=True, timeout=60)
                assert p.returncode == 0, "demo failed %s: %s" % (rid, p.stderr[-500:])
                assert "OK:" in p.stdout, "demo no OK marker %s" % rid
                print("demo ok: %-10s %s" % (k, rid), flush=True)
    print("demo execution: %d archetypes ran OK" % len(done), flush=True)
    for k in sorted(set(markers) - done):
        prog = B.DEMOS[k]("Sample %s demo" % k, "TEST-000001", "test", ["p1"], "req")
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
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w") as f:
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
