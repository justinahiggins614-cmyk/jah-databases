#!/usr/bin/env python3
"""Build the Group F data-governance databases for JAH Databases
(115-category gap audit, priority group F: data governance for a
million-database-scale network, part 1 of 2).

Nine NEW database pairs (public + Signature editions), 34 ladder-ordered
records each:

  master-data-registry            - The Master Data Registry Database
  reference-data-registry         - The Reference Data Registry Database
  data-contract-registry          - The Data Contract Registry Database
  data-lineage-registry           - The Data Lineage Registry Database
  data-observability              - The Data Observability Database
  data-lifecycle-retention        - The Data Lifecycle Retention Database
  data-sovereignty-jurisdiction   - The Data Sovereignty Jurisdiction Database
  sensitive-data-classification   - The Sensitive Data Classification Database
  dataset-acquisition-licensing   - The Dataset Acquisition Licensing Database

plus their "-signature" Signature editions.

ID prefixes (verified free: zero hits in manifest id_prefix values, exact
and substring, and zero hits in all shard record IDs):
  public:    JAH-MDRG- JAH-RDRG- JAH-DCRG- JAH-DLRG- JAH-DOBS-
             JAH-DLRT- JAH-DSJV- JAH-SDCL- JAH-DACL-
  signature: JAH-MDRGS- JAH-RDRGS- JAH-DCRGS- JAH-DLRGS- JAH-DOBSS-
             JAH-DLRTS- JAH-DSJVS- JAH-SDCLS- JAH-DACLS-

All 9 slugs verified absent from data/manifest.json before building.
Dedupe gate: code/dedupe_gate.py checks every record title against the
whole system before admitting; cross-db duplicates are refused.

Demos: demos_groupF.py - one real runnable stdlib-only Python demo per
pair, each machine-checking the record's own demo_data with tight bounds,
ending with the OK marker. The build machine-executes all 612 demos
(34 x 18 databases).

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/<slug>/index.html + gen-<slug>.js (x18)
  shard repo: data/<slug>/index.jsonl.gz + chunks/chunk-0000.jsonl.gz (x18)
  build dir : code/groupF-build/{build.py, entries_*.py, demos_groupF.py}
  fragments : ~/workspace/hidden_files/missing-builds/fragments/groupF-<slug>.json (x9)

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

No website references. No Facebook.
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
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"
CHECKDIR = os.path.join(HERE, "node_check_tmp")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
import demos_groupF as dg
import entries_1_master, entries_1b_master, entries_1c_master
import entries_2_reference, entries_2b_reference, entries_2c_reference
import entries_3_contract, entries_3b_contract, entries_3c_contract
import entries_4_lineage, entries_4b_lineage, entries_4c_lineage
import entries_5_observability, entries_5b_observability, entries_5c_observability
import entries_6_lifecycle, entries_6b_lifecycle, entries_6c_lifecycle
import entries_7_sovereignty, entries_7b_sovereignty, entries_7c_sovereignty
import entries_8_classification, entries_8b_classification, entries_8c_classification
import entries_9_acquisition, entries_9b_acquisition, entries_9c_acquisition

# ---------------------------------------------------------------- pair table
# (slug, display name base, tagline, record_kind, prefix, ai_name, role,
#  search_ph, chat_ph, archive_blurb_mid, entry modules, demo_fn)

PAIRS = [
("master-data-registry", "Master Data Registry",
 "Canonical master data records: golden-record identity, merge and split history, survivorship rules for people, organizations, products, locations, materials, and assets.",
 "master data record", "JAH-MDRG-", "JAH Master Data Archivist",
 "master data archivist - golden-record identity, merge/split history, survivorship rules, and canonical records for people, organizations, products, locations, materials, and assets; teaching progressively along the ladder; answers from many angles using only archive data",
 "Search people, organizations, products, locations, golden records, survivorship...",
 "Ask about master data, golden records, merging...",
 "canonical master-data records with golden-record identity and survivorship",
 (entries_1_master, entries_1b_master, entries_1c_master), dg.demo_master),

("reference-data-registry", "Reference Data Registry",
 "Shared codes, controlled vocabularies, units of measure, and classifications: authoritative lists with versioning, deprecation, and supersession.",
 "reference data record", "JAH-RDRG-", "JAH Reference Data Archivist",
 "reference data archivist - shared codes, controlled vocabularies, units of measure, authoritative lists with versioning and deprecation; teaching progressively along the ladder; answers from many angles using only archive data",
 "Search country codes, units of measure, vocabularies, classifications...",
 "Ask about reference codes, vocabularies, versioning...",
 "authoritative reference lists with versioning and deprecation",
 (entries_2_reference, entries_2b_reference, entries_2c_reference), dg.demo_reference),

("data-contract-registry", "Data Contract Registry",
 "Producer and consumer data contracts: guaranteed schemas, SLAs, compatibility promises, and schema-evolution histories.",
 "data contract record", "JAH-DCRG-", "JAH Data Contract Archivist",
 "data contract archivist - producer/consumer contracts, guaranteed schemas, SLAs, compatibility promises, schema evolution; teaching progressively along the ladder; answers from many angles using only archive data",
 "Search contracts, schemas, SLAs, compatibility, schema evolution...",
 "Ask about data contracts, schemas, SLAs...",
 "producer/consumer data contracts with schemas and SLAs",
 (entries_3_contract, entries_3b_contract, entries_3c_contract), dg.demo_contract),

("data-lineage-registry", "Data Lineage Registry",
 "How raw sources become records: lineage graphs, source nodes, transformation steps, and derivation formulas.",
 "data lineage record", "JAH-DLRG-", "JAH Data Lineage Archivist",
 "data lineage archivist - lineage graphs, source nodes, transformation steps, derivation formulas, impact analysis; teaching progressively along the ladder; answers from many angles using only archive data",
 "Search lineage graphs, source nodes, transformations, derivations...",
 "Ask about data lineage, transformations, impact...",
 "lineage graphs with transformations and derivation formulas",
 (entries_4_lineage, entries_4b_lineage, entries_4c_lineage), dg.demo_lineage),

("data-observability", "Data Observability",
 "Freshness tracking, distribution-shift detection, missing-value reports, anomaly alerts, pipeline-failure records, and quality trends.",
 "data observability record", "JAH-DOBS-", "JAH Data Observability Archivist",
 "data observability archivist - freshness tracking, drift detection, anomaly alerts, pipeline failures, quality trends; teaching progressively along the ladder; answers from many angles using only archive data",
 "Search freshness, drift, anomalies, pipeline failures, quality trends...",
 "Ask about data quality, freshness, anomalies...",
 "observability records covering freshness, drift, and quality",
 (entries_5_observability, entries_5b_observability, entries_5c_observability), dg.demo_observability),

("data-lifecycle-retention", "Data Lifecycle Retention",
 "Record lifecycle: creation, revision, expiration, archival, deletion, and legal holds.",
 "data lifecycle record", "JAH-DLRT-", "JAH Data Lifecycle Archivist",
 "data lifecycle archivist - creation, revision, expiration, archival, deletion, legal holds, retention schedules; teaching progressively along the ladder; answers from many angles using only archive data",
 "Search lifecycle stages, retention schedules, legal holds, deletion...",
 "Ask about data lifecycle, retention, deletion...",
 "lifecycle records from creation through deletion",
 (entries_6_lifecycle, entries_6b_lifecycle, entries_6c_lifecycle), dg.demo_lifecycle),

("data-sovereignty-jurisdiction", "Data Sovereignty Jurisdiction",
 "Where data can be stored, processed, transferred, and governed: jurisdiction rules, residency requirements, and transfer regimes.",
 "data sovereignty record", "JAH-DSJV-", "JAH Data Sovereignty Archivist",
 "data sovereignty archivist - jurisdiction rules, residency requirements, transfer regimes, adequacy, SCCs, localization; teaching progressively along the ladder; answers from many angles using only archive data",
 "Search jurisdictions, residency, GDPR, transfers, adequacy...",
 "Ask about data sovereignty, transfers, residency...",
 "sovereignty rules for storage, processing, and transfer",
 (entries_7_sovereignty, entries_7b_sovereignty, entries_7c_sovereignty), dg.demo_sovereignty),

("sensitive-data-classification", "Sensitive Data Classification",
 "Personal, confidential, proprietary, regulated, and public categories: classification criteria, handling rules, and re-classification workflows.",
 "data classification record", "JAH-SDCL-", "JAH Data Classification Archivist",
 "data classification archivist - PII, PHI, PCI, proprietary and public categories, criteria, handling rules, re-classification; teaching progressively along the ladder; answers from many angles using only archive data",
 "Search PII, PHI, PCI, classification levels, handling rules...",
 "Ask about data classification, sensitivity, handling...",
 "classification criteria and handling rules by sensitivity level",
 (entries_8_classification, entries_8b_classification, entries_8c_classification), dg.demo_classification),

("dataset-acquisition-licensing", "Dataset Acquisition Licensing",
 "Source registry: collection methods, access conditions, license terms, renewal dates, and redistribution rights.",
 "data acquisition record", "JAH-DACL-", "JAH Data Acquisition Archivist",
 "data acquisition archivist - source registry, collection methods, license terms, renewals, redistribution rights; teaching progressively along the ladder; answers from many angles using only archive data",
 "Search sources, licenses, collection methods, renewals, redistribution...",
 "Ask about data sources, licensing, renewals...",
 "source registry with licenses, renewals, and redistribution rights",
 (entries_9_acquisition, entries_9b_acquisition, entries_9c_acquisition), dg.demo_acquisition),
]

# ---------------------------------------------------------------- DB config

def _cfg(pair, source):
    (slug, base_name, tagline, record_kind, prefix, ai, role,
     search_ph, chat_ph, blurb_mid, _mods, _demo) = pair
    sig = source == "signature"
    name = "The %s Database" % base_name if not sig else "The %s Signature Database" % base_name
    full_prefix = prefix[:-1] + ("S" if sig else "") + "-"
    sig_line = ("Signature originals - his original Signature treatment of %s, "
                "clearly labeled Signature-made, never presented as authentic "
                "public record." % blurb_mid)
    pub_line = ("Public records - real, fact-checked knowledge of %s." % blurb_mid)
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(ranks 1-12) -> Compounded (ranks 13-24) -> Advanced "
              "(ranks 25-34).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": full_prefix, "ai": ai + (" (Signature)" if sig else ""),
        "role": role + (" - Signature editions" if sig else ""),
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if sig else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if sig else
                     "Public records organized in the Signature system"),
        "search_ph": search_ph,
        "chat_ph": chat_ph,
        "archive_blurb": ("Seeded %s %s, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if sig else "public-record", blurb_mid)),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled %s. Seeded archive records are the authoritative entries." % blurb_mid,
        "greet": "I am the %s. %s" % (ai + (" (Signature)" if sig else ""), chat_ph),
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "%s-study" % slug, "gen_demo_kind": "%s-demo" % slug,
        "source": source,
    }


DBCFG = {}
PAIR_DEMO = {}
PAIR_ENTRIES = {}
for pair in PAIRS:
    slug = pair[0]
    PAIR_DEMO[slug] = pair[11]
    mods = pair[10]
    PAIR_ENTRIES[slug] = (list(mods[0].ENTRIES) + list(mods[1].APPEND)
                          + list(mods[2].APPEND))
    DBCFG[slug] = _cfg(pair, "public")
    DBCFG[slug + "-signature"] = _cfg(pair, "signature")

for slug, ents in PAIR_ENTRIES.items():
    assert len(ents) == 34, "%s: %d entries" % (slug, len(ents))
    assert [e["ladder_rank"] for e in ents] == list(range(1, 35)), "%s ranks" % slug

base.DBCFG = DBCFG

SIG_TAIL = ("Signature interpretation - original Signature-system treatment "
            "by Justin Addam Higgins; clearly labeled Signature-made, never "
            "presented as authentic public record.")


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    pair_slug = slug[:-len("-signature")] if sig else slug
    entries = PAIR_ENTRIES[pair_slug]
    demo_fn = PAIR_DEMO[pair_slug]
    ordered = sorted(enumerate(entries), key=lambda p: (p[1]["ladder_rank"], p[0]))
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
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["demo_data"])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def _extract_scripts(page):
    """Return list of inline <script> (non-src, JS only) bodies for node --check."""
    scripts = []
    for m in re.finditer(r'<script([^>]*)>(.*?)</script>', page, re.S):
        attrs, body = m.group(1), m.group(2).strip()
        if re.search(r'\bsrc=', attrs):
            continue
        tm = re.search(r'type="([^"]+)"', attrs)
        if tm and tm.group(1) not in ("text/javascript", "application/javascript"):
            continue
        if body:
            scripts.append(body)
    return scripts

def _check_prefixes_free():
    """Build-time verification: all 18 prefixes free in manifest id_prefix
    values (exact + substring) and none of the 9 slugs in the manifest."""
    manifest = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    slugs = {d["slug"] for d in manifest["databases"]}
    for pair in PAIRS:
        assert pair[0] not in slugs, "slug already in manifest: %s" % pair[0]
        assert pair[0] + "-signature" not in slugs, "slug already in manifest: %s-signature" % pair[0]
    have = [d.get("id_prefix", "") for d in manifest["databases"]]
    for pair in PAIRS:
        for sig in (False, True):
            p = pair[4][:-1] + ("S" if sig else "") + "-"
            for h in have:
                assert p != h, "prefix exact collision: %s" % p
                if h:
                    assert p not in h and h not in p, "prefix substring collision: %s vs %s" % (p, h)
    print("prefix check: all 18 prefixes free, all 18 slugs absent from manifest", flush=True)


def main():
    _check_prefixes_free()
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

    os.makedirs(CHECKDIR, exist_ok=True)

    slugs = []
    for pair in PAIRS:
        slugs.append(pair[0])
        slugs.append(pair[0] + "-signature")

    built = {}
    for slug in slugs:
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
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
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
        assert "facebook" not in gen_js.lower()
        gen_path = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(gen_js)
        # JS hygiene: node --check on extracted page scripts and gen-*.js
        scripts = _extract_scripts(page)
        assert scripts, "no inline scripts found in %s" % slug
        for i, body in enumerate(scripts):
            chk = os.path.join(CHECKDIR, "%s_%d.js" % (slug, i))
            with open(chk, "w", encoding="utf-8") as f:
                f.write(body)
            p = subprocess.run(["node", "--check", chk],
                               capture_output=True, text=True, timeout=60)
            assert p.returncode == 0, "page script %d failed node --check in %s: %s" % (i, slug, p.stderr[-500:])
        p = subprocess.run(["node", "--check", gen_path],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "gen js failed node --check in %s: %s" % (slug, p.stderr[-500:])
        print("page:  db/%s/index.html + gen-%s.js [%s] (js checked: %d page scripts + gen)"
              % (slug, slug, ", ".join(notes), len(scripts)), flush=True)

    os.makedirs(FRAGDIR, exist_ok=True)
    for pair in PAIRS:
        slug = pair[0]
        pub, sigr = DBCFG[slug], DBCFG[slug + "-signature"]
        fragment = {
            "public": {
                "slug": slug, "name": pub["name"], "tagline": pub["tagline"],
                "record_kind": pub["record_kind"], "id_prefix": pub["prefix"],
                "ai_name": pub["ai"],
                "local_index": SHARD_BASE + "/data/%s/index.jsonl.gz" % slug,
                "record_count": 34, "status": "live", "full_records": 34,
                "index": SHARD_BASE + "/data/%s/index.jsonl.gz" % slug,
                "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % slug,
                "source": "public-harvest",
            },
            "signature": {
                "slug": slug + "-signature", "name": sigr["name"],
                "tagline": sigr["tagline"], "record_kind": sigr["record_kind"],
                "id_prefix": sigr["prefix"], "ai_name": sigr["ai"],
                "local_index": SHARD_BASE + "/data/%s-signature/index.jsonl.gz" % slug,
                "record_count": 34, "status": "live", "full_records": 34,
                "index": SHARD_BASE + "/data/%s-signature/index.jsonl.gz" % slug,
                "chunk_pattern": "data/%s-signature/chunks/chunk-NNNN.jsonl.gz" % slug,
                "source": "signature",
            },
        }
        fpath = os.path.join(FRAGDIR, "groupF-%s.json" % slug)
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(fragment, f, indent=1, ensure_ascii=False)
            f.write("\n")
        print("fragment: %s" % fpath, flush=True)
    print("DONE: %d databases, %d records. Merger handles manifest/api/restamp/commit." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
