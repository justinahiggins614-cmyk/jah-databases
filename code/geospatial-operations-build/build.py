#!/usr/bin/env python3
"""Build the Geospatial Operations databases for JAH Databases
(missing-115 program, Wave 1 - operational data, Manon's #1 priority).

Verified 2026-10-17 (missing-115 Wave 1): RAW SWEEP over the full manifest
(2,390 databases) PLUS every shard index title in jah-databases-data-1:
zero 'geospatial-operations' slugs/names; zero title collisions for the 34
planned titles (68 with Signature Edition suffixes) via the whole-system
dedupe gate. The one keyword near-hit, 'geospatial-databases' (JAH-GSP-),
is a meta-database of database TYPES for the planet (record_kind
'geospatial database type record') - NOT operational geospatial
computation. The paste's rule was applied by name/purpose/record
schema/capabilities: operational geospatial computation (routes,
coordinates, boundaries, terrain, proximity, spatial joins, location
uncertainty) is a distinct capability - BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  geospatial-operations            - The Geospatial Operations Database
                                     (public-harvest: real, fact-checked
                                     operational geospatial computation)
  geospatial-operations-signature  - The Geospatial Operations Signature
                                     Database
                                     (his original Signature Survey Method;
                                     src signature, titles suffixed
                                     " (Signature Edition)", never presented
                                     as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-GEOP- (public) and JAH-GEOPS- (signature), verified free
in the manifest (JAH-GEO- belongs to the Geography Atlas, JAH-GEO2- to
Geology, JAH-GEOG-PUB/SIG to the public/signature geography databases) and
in every shard index (zero hits for either prefix).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_geospatial_operations.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER git commits or
pushes. A merger handles those. It only creates new untracked paths.

Civilian operational scope only. Never the words "bat belt" anywhere.
No website references. No Facebook.
"""
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_geospatial_operations import ENTRIES, SIG_TAIL
from demos_geospatial_operations import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature Survey Method: "
                "every coordinate a sworn witness, the map the testimony, "
                "the route the sworn path, and uncertainty the honest "
                "margin. Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked operational geospatial "
                "computation: routes, coordinates, boundaries, terrain, "
                "proximity, spatial joins, and location uncertainty - map "
                "projections, geohashing and spatial indexes, routing "
                "algorithms, map-matching, GPS error budgets, coordinate "
                "systems, and spatial query patterns, organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a coordinate is, geographic vs projected coordinates, "
              "distance on a curved Earth, coordinate precision, map "
              "projections, datums, coordinate reference systems and the "
              "EPSG registry, vector boundaries, terrain basics) -> "
              "Compounded (proximity queries, spatial joins, geohashing, "
              "spatial indexes, hexagonal grids and H3, Dijkstra routing, "
              "A-star and contraction hierarchies, map-matching, GPS error "
              "budgets, coordinate transformations, raster operations, "
              "isochrones, geofencing) -> Advanced (location uncertainty, "
              "Kalman filtering, spatial query patterns at scale, "
              "viewsheds and watersheds, constrained network routing, "
              "projection math, trajectory analysis, uncertainty "
              "propagation, ITRF and plate motion, spatial data quality, "
              "real-time pipelines, the operations playbook).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search coordinates, datums, projections, geohashing, routing, map-matching, GPS error budgets, spatial joins, Kalman filters, isochrones, geofencing...",
        "chat_ph": "Ask about geospatial operations...",
        "archive_blurb": ("Seeded %s geospatial operations records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled geospatial operations studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about geospatial operations - from what a coordinate is through datums, projections, coordinate systems, boundaries, and terrain, through proximity, spatial joins, geohashing, spatial indexes, routing, map-matching, error budgets, transformations, rasters, isochrones, and geofencing, to uncertainty, Kalman filtering, query patterns at scale, viewsheds, constrained routing, projection math, trajectories, ITRF, data quality, real-time pipelines, and the operations playbook." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "geospatial-operations-study", "gen_demo_kind": "geospatial-operations-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["geospatial-operations"] = _cfg(
    "geospatial-operations", "The Geospatial Operations Database",
    "Routes, coordinates, boundaries, terrain, proximity, spatial joins, "
    "and location uncertainty: real, fact-checked operational geospatial "
    "computation - map projections, geohashing and spatial indexes, routing "
    "algorithms, map-matching, GPS error budgets, coordinate systems, and "
    "spatial query patterns - taught progressively along the ladder.",
    "geospatial operations record", "JAH-GEOP-", "JAH Geospatial Operations Archivist",
    "geospatial operations archivist - routes, coordinates, boundaries, "
    "terrain, proximity, spatial joins, and location uncertainty; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from "
    "this system",
    "public")
DBCFG["geospatial-operations-signature"] = _cfg(
    "geospatial-operations-signature", "The Geospatial Operations Signature Database",
    "His original Signature Survey Method: every coordinate a sworn "
    "witness, the map the testimony, the route the sworn path, and "
    "uncertainty the honest margin. The full ladder from what a coordinate "
    "is through datums, projections, and terrain, through proximity, "
    "routing, and map-matching, to uncertainty, Kalman filtering, ITRF, "
    "and the operations playbook, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "geospatial operations record", "JAH-GEOPS-", "JAH Geospatial Operations Archivist (Signature)",
    "geospatial operations archivist - Signature editions: his original "
    "Signature Survey Method, every coordinate a sworn witness and "
    "uncertainty the honest margin, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
    "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["description"])
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment(built):
    frag = {"public": {
        "slug": "geospatial-operations",
        "name": "The Geospatial Operations Database",
        "tagline": DBCFG["geospatial-operations"]["tagline"],
        "record_kind": "geospatial operations record",
        "id_prefix": "JAH-GEOP-",
        "ai_name": "JAH Geospatial Operations Archivist",
        "local_index": SHARD_BASE + "/data/geospatial-operations/index.jsonl.gz",
        "record_count": 34, "status": "live", "full_records": 34,
        "index": SHARD_BASE + "/data/geospatial-operations/index.jsonl.gz",
        "chunk_pattern": "data/geospatial-operations/chunks/chunk-NNNN.jsonl.gz",
        "source": "public-harvest",
    }, "signature": {
        "slug": "geospatial-operations-signature",
        "name": "The Geospatial Operations Signature Database",
        "tagline": DBCFG["geospatial-operations-signature"]["tagline"],
        "record_kind": "geospatial operations record",
        "id_prefix": "JAH-GEOPS-",
        "ai_name": "JAH Geospatial Operations Archivist (Signature)",
        "local_index": SHARD_BASE + "/data/geospatial-operations-signature/index.jsonl.gz",
        "record_count": 34, "status": "live", "full_records": 34,
        "index": SHARD_BASE + "/data/geospatial-operations-signature/index.jsonl.gz",
        "chunk_pattern": "data/geospatial-operations-signature/chunks/chunk-NNNN.jsonl.gz",
        "source": "signature",
    }}
    assert set(built) == {"geospatial-operations", "geospatial-operations-signature"}
    assert all(len(v) == 34 for v in built.values())
    path = "/home/hatch/workspace/hidden_files/missing-builds/fragments/geospatial-operations.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % path, flush=True)


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

    built = {}
    for slug in ("geospatial-operations", "geospatial-operations-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 10, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "universal build" not in page.lower(), "field leftover in %s" % slug
        assert "universal-build" not in page, "slug leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    write_fragment(built)

    # Merger-owned files are intentionally NOT touched here:
    # data/manifest.json, api.json, index.html, README.md, docs/AI_ACCESS.md.
    # No git commit, no git push. The merger verifies and ships.
    print("records: %d (34 public + 34 signature)" % total)
    print("DONE - awaiting merger (no manifest/api edits, no commit, no push).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
