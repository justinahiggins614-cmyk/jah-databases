#!/usr/bin/env python3
"""PHASE H — database-type catalog build (dbtype pastes 5, 6, 7).

- Files 36 entries as full canon records into existing covering databases
  (paste 5: 12 as Signature originals; paste 7: 24 as factual public
  records, except soap-label-bleeds which is a Signature original).
  Safety: BCI/neural entries are descriptive systems documentation only —
  no medical advice, no operational attack/tradecraft content. The 3D-print
  G-code record carries actual usable directions; displayed print times are
  estimates, never validated print jobs; unmodeled real-world factors are
  disclosed in the record.
- Builds 7 new <category>-databases DB pairs (public + signature) = 14 DBs,
  78 seed records: 6 paste-6 cosmic categories (66 records: public side is
  fact-checked real-science counterparts, signature side his original
  speculative designs) + 1 static-web category (12 records).
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
from entries_h import ENTRIES, PUB
import build as B

GATE = B.GATE
GROUP = "database-types"

# ============================================================ new DB config

NEWCATS = [
    ("omniversal", "omniversal-databases",
     "The Omniversal and Cosmic-Scale Data Structures Databases Database",
     "Database types for cosmic-scale structures: timeline trees, wavefunction logs, constants registries, and entropy ledgers.",
     "omniversal data structure database type record", "JAH-OMN-", "JAH Omniversal Databases Archivist",
     "omniversal databases archivist — cosmic-scale database types",
     "Cosmology and quantum foundations (standard physics literature)."),
    ("simulation-architecture", "simulation-architecture-databases",
     "The Cosmological Simulation and Reality Architecture Databases Database",
     "Database types for reality architecture: simulation kernels, compactification configs, horizon ledgers, and wormhole logs.",
     "reality architecture database type record", "JAH-REALITY-", "JAH Reality Architecture Databases Archivist",
     "reality architecture databases archivist — simulation database types",
     "Cosmology and general relativity (standard physics literature)."),
    ("noospheric", "noospheric-matrices-databases",
     "The Metaphysical and Noospheric Matrices Databases Database",
     "Database types for consciousness matrices: noospheric caches, karmic ledgers, archetype templates, and qualia tables.",
     "noospheric matrix database type record", "JAH-NOO-", "JAH Noospheric Matrices Databases Archivist",
     "noospheric matrices databases archivist — consciousness matrix database types",
     "Psychology and philosophy of mind (standard literature)."),
    ("transdimensional", "transdimensional-topology-databases",
     "The Trans-Dimensional Topology Databases Database",
     "Database types for higher-dimensional topology: brane logs, mirror matrices, manifold charts, and void registers.",
     "trans-dimensional topology database type record", "JAH-TDT-", "JAH Trans-Dimensional Topology Databases Archivist",
     "trans-dimensional topology databases archivist — brane and manifold database types",
     "Differential geometry and cosmology (standard literature)."),
    ("temporal", "temporal-causality-databases",
     "The Causality and Temporal Control Databases Database",
     "Database types for temporal control: paradox vectors, fate intersections, reversal logs, and pruning registers.",
     "temporal causality database type record", "JAH-TCAU-", "JAH Temporal Causality Databases Archivist",
     "temporal causality databases archivist — time and causality database types",
     "General relativity and philosophy of time (standard literature)."),
    ("mathematical", "mathematical-constants-databases",
     "The Absolute Mathematical Constants Databases Database",
     "Database types for absolute constants: proof registries, transfinite maps, null states, and axiom registries.",
     "mathematical constant database type record", "JAH-MCON-", "JAH Mathematical Constants Databases Archivist",
     "mathematical constants databases archivist — foundations database types",
     "Mathematical logic and set theory (standard literature)."),
    ("static-web", "static-web-app-databases",
     "The Static Web Application Databases Database",
     "Database types for static web applications: deployment manifests, Wasm bundles, index trees, frontmatter, calculator scripts, and generator templates.",
     "static web application database type record", "JAH-STWEB-", "JAH Static Web Application Databases Archivist",
     "static web application databases archivist — static web database types",
     "Web engineering (standard web standards literature)."),
]

SIG_PREFIX = {"omniversal": "JAH-OMNG-",
              "simulation-architecture": "JAH-REALITYG-",
              "noospheric": "JAH-NOOG-",
              "transdimensional": "JAH-TDTG-",
              "temporal": "JAH-TCAUG-",
              "mathematical": "JAH-MCONG-",
              "static-web": "JAH-STWEBG-"}


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

# src per filed entry: paste-5 speculative designs + soap-label-bleeds are
# Signature originals; paste-7 technical entries are factual public records.
SIG_CATS = {"bci", "quantum-macro", "programmable-matter", "agi-consciousness"}
SIG_KEYS = {"soap-label-bleeds"}


def filed_src(key, cat):
    return "signature" if (cat in SIG_CATS or key in SIG_KEYS) else "public-harvest"


# ============================================================ filing

def file_records():
    manifest = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    api = json.load(open(os.path.join(REPO, "api.json")))
    m_idx = {d["slug"]: d for d in manifest["databases"]}
    a_idx = {d["slug"]: d for d in api["databases"]}
    filed = []
    progs = []
    for (key, cat, title, desc, points, req, standards, citations, demo_kind,
         target) in ENTRIES:
        if not target:
            continue
        src = filed_src(key, cat)
        ftitle = title + " (Signature Edition)" if src == "signature" else title
        if [h for h in GATE.check(target, ftitle) if h[0] != target]:
            print("  gate refused (cross-db dupe): %s" % ftitle, flush=True)
            continue
        entry = m_idx[target]
        prefix = entry["id_prefix"]
        root = B.shard_root_for(target, entry)
        idx_path = os.path.join(root, "index.jsonl.gz")
        rows = B.gz_jsonl_rows(idx_path)
        if any(r.get("t") == ftitle for r in rows):
            print("  skip (already filed): %s -> %s" % (ftitle, target), flush=True)
            continue
        rid = B.next_id(prefix, rows[-1]["id"])
        rec = B.build_record(title, title, GROUP, desc, points, req, standards,
                             citations, src, demo_kind, rid)
        assert rec["t"] == ftitle, "title mismatch %r vs %r" % (rec["t"], ftitle)
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
        GATE.admit(target, ftitle, rid)
        filed.append((target, rid, ftitle))
        progs.append((rid, rec["demo"]["program"]))
        print("  filed %-44s %s -> %s" % (ftitle[:44], target, rid), flush=True)
    with open(os.path.join(REPO, "data", "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
        f.write("\n")
    with open(os.path.join(REPO, "api.json"), "w", encoding="utf-8") as f:
        json.dump(api, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("filed %d records into %d databases"
          % (len(filed), len({t for t, _, _ in filed})), flush=True)
    return filed, progs


# ============================================================ new DBs

def build_new_records():
    built = {}
    for (cat, slug, _n, _t, _rk, _p, _a, _r, _c) in NEWCATS:
        for ver in ("public", "signature"):
            s = slug if ver == "public" else slug + "-signature"
            cfg = DBCFG[s]
            recs = []
            for (key, ecat, title, desc, points, req, standards, citations,
                 demo_kind, target) in ENTRIES:
                if ecat != cat or target:
                    continue
                if ver == "public":
                    p = PUB[key]
                    (ptitle, pdesc, ppoints, preq, pstandards, pcit, pdemo) = p
                    src = "public-harvest"
                    rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
                    rec = B.build_record(ptitle, ptitle, key, pdesc, ppoints, preq,
                                         pstandards, pcit, src, pdemo, rid)
                    gate_title = ptitle
                else:
                    src = "signature"
                    rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
                    rec = B.build_record(title, title, key, desc, points, req,
                                         standards, CIT[s], src, demo_kind, rid)
                    gate_title = rec["t"]
                B.check_record(rec)
                if [h for h in GATE.check(s, gate_title) if h[0] != s]:
                    print("  gate refused (cross-db dupe): %s" % gate_title, flush=True)
                    continue
                GATE.admit(s, gate_title, rid)
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


MARKERS = {"report": "INFO = {", "sqlite": "sqlite3.connect", "jsondoc": "def get_path(",
           "ledger": "def post(entries)", "ticks": "vwap", "hashchain": "block_hash(",
           "ehr": "ENCOUNTER_REQUIRED", "dicom": "REQUIRED_TAGS", "genome": "GC=",
           "geo": "point_in_polygon", "stats": "statistics.median",
           "simhw": "SIMULATED DEVICE INTERFACE", "rss": "ElementTree",
           "text": "most_common(5)", "pipeline": "def clean(rec)", "fileops": "TemporaryDirectory",
           "socket": "parse_ipv4_header", "algo": "def bfs(", "vision": "edge_metric",
           "secret": "gen_world(", "dsp": "dft_mag", "sensors": "pearson(",
           "spike": "integrate-and-fire", "dna": "quaternary-encoded",
           "tda": "persistence pairs", "poincare": "acosh(",
           "multivector": "geometric product", "riemann": "line element",
           "lattice": "Babai", "fhe": "homomorphic addition",
           "qkd": "BB84", "hologram": "interference grating",
           "plasmonic": "plasmonic waveguide", "skyrmion": "topological charge",
           "memgraph": "episodic memory", "selfimprove": "NodeTransformer",
           "neurosym": "logical inference"}


def run_demo(rid, prog, done):
    for k, m in MARKERS.items():
        if k not in done and m in prog:
            done.add(k)
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=60)
            assert p.returncode == 0, "demo failed %s: %s" % (rid, p.stderr[-500:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % rid
            print("demo ok: %-12s %s" % (k, rid), flush=True)


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

    # ---- step 1: file 36 entries into existing databases
    filed, filed_progs = file_records()
    assert len(filed) == 36, "expected 36 filed, got %d" % len(filed)

    # ---- step 2: build 14 new databases (7 categories x public+signature)
    built = build_new_records()
    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        total += len(recs)
        n = write_shard_db(slug, recs)
        print("shard: %-42s %d records" % (slug, n), flush=True)
    assert total == 78, "expected 78 seed records, got %d" % total

    # ---- step 3: execute every demo (filed + new), one run per archetype
    done = set()
    for rid, prog in filed_progs:
        run_demo(rid, prog, done)
    for slug, recs in built.items():
        for r in recs:
            run_demo(r["id"], r["demo"]["program"], done)
    for k in sorted(set(MARKERS) - done):
        prog = B.DEMOS[k]("Sample %s demo" % k, "TEST-000001", "test", ["p1"], "req")
        compile(prog, "TEST-000001", "exec")
        p = subprocess.run([sys.executable, "-c", prog],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "demo failed (direct) %s: %s" % (k, p.stderr[-500:])
        assert "OK:" in p.stdout, "demo no OK marker (direct) %s" % k
        done.add(k)
        print("demo ok: %-12s (direct)" % k, flush=True)
    assert len(done) == len(MARKERS), "not all archetypes executed: %s" % (set(MARKERS) - done)
    print("demo execution: %d archetypes ran OK" % len(done), flush=True)

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
