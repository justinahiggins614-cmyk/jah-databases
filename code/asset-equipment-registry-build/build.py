#!/usr/bin/env python3
"""Build the Asset and Equipment Registry databases for JAH Databases
(missing-115 #54, Wave 1 operational data).

Dedupe pre-check 2026-10-17: all 68 planned titles (34 public + 34
Signature Edition) run through code/dedupe_gate.py against the whole
system BEFORE authoring - zero collisions, zero refusals.

RAW SWEEP over the full manifest PLUS every shard index title in
jah-databases-data-1 PLUS the main-repo data dir: zero
'asset-equipment*' slugs/names; zero 'asset and equipment registry'
title collisions. Near-hits are IT asset-management slices inside
broader IT operations databases (no dedicated registry record schema)
and fixed-asset accounting slices inside finance databases (no
physical identification, condition, location, or maintenance history).
Paste rule applied by name/purpose/record schema/capabilities: BUILD
NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  asset-equipment-registry           - The Asset and Equipment Registry Database
                                       (public-harvest: real, fact-checked
                                       asset and equipment registry practice -
                                       identifiers, configuration, location,
                                       operating condition, warranty,
                                       maintenance history; standard
                                       references ISO 55000:2014 (revised
                                       2024), ISO 55001:2014 (revised 2024),
                                       ISO 55002:2018, ISO/IEC 19770-1:2017,
                                       ASC 360, IRS Publication 946, GASB 34,
                                       ITIL 4 configuration management, NIST
                                       SP 800-88 Rev. 1, NFPA 70B:2023, GS1
                                       General Specifications, SMRP metric
                                       definitions, IAM Anatomy v4, IEEE Std
                                       493-2007, cited per record)
  asset-equipment-registry-signature - The Asset and Equipment Registry
                                       Signature Database
                                       (his original Signature Registry
                                       Method: every asset a trust placed in
                                       the steward's hands, the registry the
                                       ledger of entrusted work, the tag the
                                       asset's true name, condition the
                                       testimony of care, maintenance the
                                       keeping of the covenant, disposal the
                                       honorable discharge; src signature,
                                       titles suffixed " (Signature
                                       Edition)", never presented as
                                       authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-AREG- (public) and JAH-AREGS- (signature), verified free
in the manifest (exact-prefix check in both directions; JAH-AST- belongs to
the unrelated space-astro/astrophysics databases) and zero hits in every
shard index of jah-databases-data-1.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_asset_equipment_registry.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER commits or pushes.
The merger owns those. Outputs: db/asset-equipment-registry[-signature]/
pages, shard data dirs, and the builder fragment.

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian operational scope only.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/asset-equipment-registry.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_asset_equipment_registry import ENTRIES, SIG_TAIL
from demos_asset_equipment_registry import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Registry "
                "Method: every asset a trust placed in the steward's hands, "
                "the registry the ledger of entrusted work, the tag the "
                "asset's true name, condition the testimony of care, "
                "maintenance the keeping of the covenant, and disposal the "
                "honorable discharge. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked asset and equipment "
                "registry practice: identifiers, asset tagging and "
                "identification, CMDB-style configuration records, location, "
                "operating condition, warranty tracking, maintenance "
                "history, depreciation schedules, lifecycle states, and "
                "calibration linkage - every record carrying the full "
                "registry anatomy, key points, requirements, standards, "
                "real citations, and a working demonstration program, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what an asset is, the register anatomy, asset tags, "
              "categories, naming and taxonomy, acquisition and "
              "capitalization, assignment and custody, condition ratings, "
              "location tracking, lifecycle states) -> Compounded (tag "
              "technologies, depreciation schedules, CMDB-style "
              "configuration records, work orders, preventive and "
              "predictive scheduling, warranty tracking, calibration, "
              "audits, utilization, spare parts, criticality, baselines) "
              "-> Advanced (reliability metrics, total cost of ownership, "
              "the ISO 55000 framework, lease versus buy, health scoring, "
              "disposal and sanitization, federation and discovery, "
              "insurance, data quality, analytics and KPIs, fleet "
              "management, building the program).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search asset tags, CMDB, depreciation, lifecycle states, warranty, calibration, work orders, MTBF, ISO 55000, audits, condition ratings...",
        "chat_ph": "Ask about asset and equipment registry practice...",
        "archive_blurb": ("Seeded %s asset and equipment registry records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled asset and equipment registry studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about asset and equipment registry practice - from what an asset is through the register anatomy, tags, categories, naming, acquisition, custody, condition, location, and lifecycle states, through tag technologies, depreciation, configuration records, work orders, maintenance scheduling, warranty, calibration, audits, utilization, spares, criticality, and baselines, to reliability metrics, total cost of ownership, ISO 55000, lease versus buy, health scoring, disposal, discovery, insurance, data quality, analytics, fleet management, and building the program." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "asset-registry-study", "gen_demo_kind": "asset-registry-demo",
        "source": source,
    }

CIT_PUB = ("Asset and equipment registry practice (standard references: "
           "ISO 55000:2014, revised 2024; ISO 55001:2014, revised 2024; ISO "
           "55002:2018; ISO/IEC 19770-1:2017; ASC 360 Property, Plant, and "
           "Equipment; IRS Publication 946; GASB Statement 34; ITIL 4, "
           "Axelos 2019; NIST SP 800-88 Rev. 1; NFPA 70B:2023; GS1 General "
           "Specifications; SMRP Best Practices metrics; Institute of Asset "
           "Management, Asset Management - An Anatomy v4, 2024; IEEE Std "
           "493-2007).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Registry Method - every asset a trust placed in the "
                     "steward's hands, the registry the ledger of entrusted "
                     "work - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["asset-equipment-registry"] = _cfg(
    "asset-equipment-registry", "The Asset and Equipment Registry Database",
    "Track every asset from acquisition to disposal: real, fact-checked "
    "asset and equipment registry practice - identifiers, asset tagging, "
    "CMDB-style configuration records, location, operating condition, "
    "warranty, maintenance history, depreciation schedules, and lifecycle "
    "states - taught progressively along the ladder.",
    "asset and equipment registry record", "JAH-AREG-", "JAH Asset and Equipment Registry Archivist",
    "asset and equipment registry archivist - identifiers, configuration, "
    "location, operating condition, warranty, and maintenance history "
    "across the asset lifecycle; teaching progressively along the ladder "
    "from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["asset-equipment-registry-signature"] = _cfg(
    "asset-equipment-registry-signature", "The Asset and Equipment Registry Signature Database",
    "His original Signature Registry Method: every asset a trust placed in "
    "the steward's hands, the registry the ledger of entrusted work, the "
    "tag the asset's true name, condition the testimony of care, "
    "maintenance the keeping of the covenant, and disposal the honorable "
    "discharge. The full ladder from what an asset is through tags, "
    "configuration, warranty, and maintenance, to reliability, ISO 55000, "
    "and the program itself, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "asset and equipment registry record", "JAH-AREGS-", "JAH Asset and Equipment Registry Archivist (Signature)",
    "asset and equipment registry archivist - Signature editions: his "
    "original Signature Registry Method, every asset a trust held by its "
    "steward and the registry the ledger of entrusted work, "
    "clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles "
    "- definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    CIT_SIG, "signature")

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
    for slug in ("asset-equipment-registry", "asset-equipment-registry-signature"):
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

    # builder fragment for the merger (manifest/api owned by merger - never touched here)
    def frag(slug, source):
        c = DBCFG[slug]
        return {
            "slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"], "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(built[slug]), "status": "live",
            "full_records": len(built[slug]),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": source,
        }
    fragment = {
        "public": frag("asset-equipment-registry", "public-harvest"),
        "signature": frag("asset-equipment-registry-signature", "signature"),
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT)
    print("DONE: %d records across 2 databases. Merger owns manifest/api/index/README/AI_ACCESS." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
