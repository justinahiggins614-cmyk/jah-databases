#!/usr/bin/env python3
"""PHASE O — intelligence scales (Manon's order: "Super Intelligence database and
all scales of intelligence to God mode").

7 compound databases (public-harvest + signature records in each), one per
intelligence scale; records = ABILITIES of that scale. Plus complementary
filings into existing swarm-intelligence DBs.

Canon: code/dbtype-build pattern (template page, gzipped index chunks in
jah-databases-data-1, unique ID prefixes, manifest/api.json entries, dedupe
gate, sweep patch, generator JS). No website references, no Facebook, no
banned phrases. AGI/superintelligence entries are descriptive frameworks.
"""
import gzip
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

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
GATE = DedupeGate(os.path.join(SHARD, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_o import ENTRIES_O, FILE_O

# ---- reuse the proven demo library from the dbtype build
spec = importlib.util.spec_from_file_location(
    "dbb", os.path.join(REPO, "code", "dbtype-build", "build.py"))
dbb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dbb)
DEMOS = dbb.DEMOS
DEMO_NOTE = dbb.DEMO_NOTE
check_record = dbb.check_record
write_gz_jsonl = dbb.write_gz_jsonl
gz_jsonl_rows = dbb.gz_jsonl_rows
next_id = dbb.next_id

# ============================================================ record assembly (abilities)
def how_it_works_pub(name, desc, points):
    return ("In real-world study, %s works as follows. %s The operating principles are: %s"
            % (name, desc, " ".join("%s." % p for p in points)))

def how_it_works_sig(name, desc, points):
    return ("The Signature edition of %s is an original Signature ability design: "
            "it specifies how the ability manifests, how to develop or build it, and the "
            "working demonstration as a complete design in the Signature system. %s "
            "The Signature design principles are: %s"
            % (name, desc, " ".join("%s." % p for p in points)))

def build_record_o(title, name, group, desc, points, req, standards, citations,
                   src, demo_kind, rid):
    if src == "signature":
        title = title + " (Signature Edition)"
        description = ("Signature original ability design: " + desc +
                       " Key aspects include: " + "; ".join(points) + "." +
                       " Designed in the Signature system as an original ability design.")
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

# ============================================================ database configs
CATS = [
    ("animal", "animal-intelligence", "The Animal & Biological Intelligence Database",
     "Animal and biological intelligence: instinct, tool use, social cognition, and the minds of crows, whales, and octopuses — plus Signature editions.",
     "animal intelligence ability", "JAH-ANII-", "JAH Animal Intelligence Archivist",
     "animal intelligence archivist — biological cognition and Signature ability designs",
     "Ethology (standard animal cognition literature)."),
    ("human", "human-intelligence", "The Human Intelligence Database",
     "Human intelligence scales: IQ bands, multiple intelligences, emotional intelligence, savant abilities, and genius-level creativity — plus Signature editions.",
     "human intelligence ability", "JAH-HUMI-", "JAH Human Intelligence Archivist",
     "human intelligence archivist — cognitive abilities and Signature ability designs",
     "Psychometrics (standard intelligence-research literature)."),
    ("narrow", "artificial-narrow-intelligence", "The Artificial Narrow Intelligence Database",
     "Artificial narrow intelligence, per domain: vision, language, robotics, games, and science — each ability documented with how it works and how to build it — plus Signature editions.",
     "narrow AI ability", "JAH-NARAI-", "JAH Narrow AI Archivist",
     "narrow AI archivist — domain AI abilities and Signature ability designs",
     "Machine learning (standard AI literature)."),
    ("agi", "artificial-general-intelligence", "The Artificial General Intelligence Database",
     "Artificial general intelligence scales: reasoning, planning, transfer learning, and the abilities a general mind needs — plus Signature editions.",
     "AGI ability", "JAH-AGII-", "JAH AGI Archivist",
     "AGI archivist — general cognitive abilities and Signature ability designs",
     "AGI research (standard general-intelligence literature)."),
    ("super", "superintelligence", "The Superintelligence Database",
     "Superintelligence scales: recursive self-improvement, whole-brain emulation scenarios, and alignment frameworks — descriptive, scholarly, plus Signature editions.",
     "superintelligence ability", "JAH-SUPRI-", "JAH Superintelligence Archivist",
     "superintelligence archivist — advanced intelligence frameworks and Signature ability designs",
     "Superintelligence theory (standard literature)."),
    ("collective", "collective-intelligence", "The Collective & Swarm Intelligence Database",
     "Collective and swarm intelligence: hive minds, markets, scientific collaboration, and crowds — how groups become smarter than individuals — plus Signature editions.",
     "collective intelligence ability", "JAH-COLI-", "JAH Collective Intelligence Archivist",
     "collective intelligence archivist — group cognition and Signature ability designs",
     "Collective intelligence (standard literature)."),
    ("godmode", "cosmic-godmode-intelligence", "The Cosmic & God-Mode Intelligence Database",
     "Cosmic and God-mode intelligence — the top scale: omniscience-class integration, reality modeling, planetary stewardship, and the Signature God-mode concept.",
     "god-mode intelligence ability", "JAH-GODI-", "JAH God-Mode Intelligence Archivist",
     "god-mode intelligence archivist — cosmic-scale frameworks and the Signature God-mode concept",
     "Systems theory and Signature canon (standard literature)."),
]

def _cfg(scale, slug, name, tagline, rk, prefix, ai, role, citation):
    return {
        "name": name, "tagline": tagline, "record_kind": rk,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": ("%s Every record carries the full entry: description, how it manifests, "
                   "how to develop or build it, key points, requirements, standards, "
                   "citations, and a working demonstration program." % tagline),
        "sig_type": "Public records and Signature originals organized in the Signature system",
        "search_ph": "Search %s..." % rk,
        "chat_ph": "Ask about %s..." % rk,
        "archive_blurb": "Seeded public-record and Signature-original %s, marching toward one million records." % rk,
        "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "fields": "intelligence-scale abilities",
        "gen_desc": ("Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries."),
        "greet": "I am the %s. Ask me about %s." % (ai, rk),
        "gen_fields": ["intelligence-scale abilities"], "gen_kind": slug,
        "gen_demo_kind": "python", "source": "public+signature",
    }

DBCFG = {}
for (scale, slug, name, tagline, rk, prefix, ai, role, citation) in CATS:
    DBCFG[slug] = _cfg(scale, slug, name, tagline, rk, prefix, ai, role, citation)

def build_new_records():
    built = {}
    for (scale, slug, _n, _t, _rk, _p, _a, _r, _c) in CATS:
        cfg = DBCFG[slug]
        group = slug
        recs = []
        for (key, escale, title, desc, points, req, standards, citations,
             demo_kind) in ENTRIES_O:
            if escale != scale:
                continue
            for src in ("public-harvest", "signature"):
                ftitle = title + " (Signature Edition)" if src == "signature" else title
                if [h for h in GATE.check(slug, ftitle) if h[0] != slug]:
                    print("  gate refused (cross-db dupe): %s" % ftitle, flush=True)
                    continue
                rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
                rec = build_record_o(title, title, group, desc, points, req,
                                     standards, citations, src, demo_kind, rid)
                check_record(rec)
                GATE.admit(slug, ftitle, rid)
                recs.append(rec)
        assert recs, "empty db " + slug
        built[slug] = recs
    return built

def write_shard_db(slug, recs):
    base = os.path.join(SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
                       recs[ci:ci + 100])
    return len(recs)

# ============================================================ complementary filings
def file_records_o():
    manifest = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    api = json.load(open(os.path.join(REPO, "api.json")))
    m_idx = {d["slug"]: d for d in manifest["databases"]}
    a_idx = {d["slug"]: d for d in api["databases"]}
    filed = []
    for (key, title, desc, points, req, standards, citations,
         demo_kind, target, src) in FILE_O:
        ftitle = title + " (Signature Edition)" if src == "signature" else title
        if [h for h in GATE.check(target, ftitle) if h[0] != target]:
            print("  gate refused (cross-db dupe): %s" % ftitle, flush=True)
            continue
        entry = m_idx[target]
        prefix = entry["id_prefix"]
        root = os.path.join(REPO, entry["local_index"].rsplit("/index.jsonl.gz", 1)[0])
        idx_path = os.path.join(root, "index.jsonl.gz")
        rows = gz_jsonl_rows(idx_path)
        if any(r.get("t") == ftitle for r in rows):
            print("  skip (already filed): %s -> %s" % (ftitle, target), flush=True)
            continue
        rid = next_id(prefix, rows[-1]["id"])
        group = "swarm-intelligence"
        rec = build_record_o(title, title, group, desc, points, req, standards,
                             citations, src, demo_kind, rid)
        check_record(rec)
        light = {"id": rid, "t": rec["t"], "g": group}
        chunks_dir = os.path.join(root, "chunks")
        chunk_files = sorted(f for f in os.listdir(chunks_dir) if f.endswith(".jsonl.gz"))
        nums = [int(re.search(r"chunk-(\d+)\.jsonl\.gz", fn).group(1)) for fn in chunk_files]
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
        GATE.admit(target, ftitle, rid)
        filed.append((target, rid, ftitle))
        print("  filed %-42s %s -> %s" % (ftitle[:42], target, rid), flush=True)
    with open(os.path.join(REPO, "data", "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
        f.write("\n")
    with open(os.path.join(REPO, "api.json"), "w", encoding="utf-8") as f:
        json.dump(api, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("filed %d records into %d databases" % (len(filed), len({t for t, _, _ in filed})))
    return filed

# ============================================================ manifest / api entries
def manifest_entry(slug, n):
    c = DBCFG[slug]
    url = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"], "local_index": url,
            "record_count": n, "status": "live", "full_records": n,
            "index": url,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "public+signature"}

def api_entry(slug, n):
    c = DBCFG[slug]
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "record_count": n, "status": "live",
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"}

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

# ============================================================ main
def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    nbspec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(nbspec)
    nbspec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    # ---- step 1: file complementary records into existing swarm DBs
    filed = file_records_o()

    # ---- step 2: build 7 new compound databases
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

    # ---- step 3: execute one demo per archetype used + compile everything
    # map: find demo kind per record by matching known markers
    markers = {"report": "INFO = {", "dsp": "dft_mag", "vision": "edge_metric",
               "sqlite": "sqlite3.connect", "sensors": "pearson(",
               "stats": "statistics.median", "text": "most_common(5)",
               "algo": "def bfs(", "memgraph": "sample episode graph",
               "selfimprove": "embedded sample function",
               "lattice": "trapdoor decode failed"}
    kinds = set()
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            for k, m in markers.items():
                if m in prog:
                    kinds.add(k)
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
    assert kinds <= done, "unexecuted kinds: %s" % (kinds - done)
    print("demo execution: %d archetypes ran OK" % len(done))

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
        field = DBCFG[slug]["fields"]
        topics = {field: ["%s — %s" % (r["t"], field) for r in recs]}
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
