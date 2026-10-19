#!/usr/bin/env python3
"""Build the Database Federation databases for JAH Databases
(governance track, group F: data governance for a million-database-scale
network, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); no other builder writing these slugs.
ID prefixes JAH-DFED- (public) and JAH-DFEDS- (signature) verified free:
zero exact or substring hits in manifest id_prefix values and zero hits in
all shard record IDs of jah-databases-data-1. (JAH-DBF- was rejected: it
substring-collides with the existing JAH-DB prefix.) All 68 record titles
checked against the WHOLE system (exact dedupe index + live shard title
corpus of 1,143,457 titles) BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  database-federation            - The Database Federation Database
      (public-harvest: real, fact-checked federation knowledge - federated
      query patterns (scatter-gather, broadcast, chained), cross-database
      join contracts, schema mapping, identity resolution, membership,
      capability advertisement, routing, distributed search architecture,
      result merging, consistency models, federated auth, rate limiting,
      federated caching, partial failure handling, query costing, schema
      evolution, onboarding/offboarding, global optimizer, distributed
      transactions, reconciliation, governance charter, SLAs, provenance,
      analytics pipelines, multi-region topology, security, audits,
      dashboards, anti-patterns)
  database-federation-signature  - The Database Federation Signature Database
      (the Signature Federation Doctrine; src signature, titles suffixed
      " (Signature Edition)", never presented as authentic public record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_database_federation.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/database-federation/index.html + gen-...js
              db/database-federation-signature/index.html + gen-...js
  shard repo: data/database-federation/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/database-federation-signature/... (same)
  build dir : code/database-federation-build/{build.py, entries_*.py, demos_*.py}
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/database-federation.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
import pickle
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/database-federation.json"
CORPUS = "/home/hatch/workspace/hidden_files/govf2-title-corpus.pkl"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
from build_global_dedupe import norm_title
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_database_federation import ENTRIES, SIG_TAIL
from demos_database_federation import DEMOS

with open(CORPUS, "rb") as f:
    TITLE_CORPUS = pickle.load(f)

SLUG_PUB = "database-federation"
SLUG_SIG = "database-federation-signature"

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source,
         search_ph, chat_ph, archive_blurb, fields, gen_desc, gen_kind,
         gen_demo_kind, greet, pub_line, sig_line, ladder):
    pub_line = "Public records - real, fact-checked federation knowledge: federated query patterns (scatter-gather, broadcast, chained), cross-database join contracts, schema mapping, identity resolution across databases, federation membership records, capability advertisement, query routing rules, distributed search architecture, result merging and ranking, consistency models in federation, federated authentication, rate limiting across members, caching federated results, partial failure handling, federated query cost estimation, schema evolution in federation, membership onboarding and offboarding, global query optimizer, distributed transactions, eventual consistency reconciliation, federation governance charter, inter-member SLA contracts, cross-database provenance, federated analytics pipelines, multi-region federation topology, federation security model, federation audits, federation health dashboards, and federation anti-patterns."
    sig_line = "Signature originals - the Signature Federation Doctrine: many databases, one question, zero confusion; a federation is a promise between databases, and promises need contracts, witnesses, and consequences. Clearly labeled Signature-made, never presented as authentic public record."
    ladder = " Records are ordered by the teaching ladder: Foundations (federation overview, scatter-gather, broadcast, chained patterns, join contracts, schema mapping, identity resolution, membership, capability advertisement, routing rules) -> Compounded (distributed search, result merging, consistency models, federated auth, rate limiting, federated caching, partial failure, query costing, schema evolution, onboarding, offboarding) -> Advanced (global optimizer, distributed transactions, reconciliation, governance charter, SLAs, provenance, analytics pipelines, multi-region topology, security model, audit, health dashboard, anti-patterns, self-audit and mastery)."
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": search_ph, "chat_ph": chat_ph,
        "archive_blurb": archive_blurb,
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": fields, "gen_desc": gen_desc,
        "greet": greet, "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": gen_kind, "gen_demo_kind": gen_demo_kind,
        "source": source,
    }

DBCFG = {}
DBCFG[SLUG_PUB] = _cfg(
    SLUG_PUB, "The Database Federation Database",
    "Many databases, one query: federated query patterns, cross-database join contracts, distributed-search architectures, and federation membership - the discipline of asking questions that no single database can answer alone.",
    "federation record", "JAH-DFED-", "JAH Federation Archivist",
    "Federation archivist - federated query patterns, join contracts, distributed search, and membership governance; teaching progressively along the ladder from foundations through compounded to advanced; answers from many angles - patterns, contracts, topologies, failures - using only archive data from this system",
    "public",
    "Search federated queries, join contracts, membership, topologies...",
    "Ask about database federation...",
    "Seeded public-record federation records, marching toward one million records. Presented in teaching-ladder order: foundations, compounded, advanced.",
    "Foundations · Compounded · Advanced - each tier opens on demand and loads only what you open",
    "Generate clearly-labeled federation studies. Seeded archive records are the authoritative entries.",
    "federation-study", "federation-demo",
    "I am the JAH Federation Archivist. Ask me about database federation - query patterns, join contracts, distributed search, and membership.",
    "Public records - real, fact-checked federation knowledge: federated query patterns (scatter-gather, broadcast, chained), cross-database join contracts, schema mapping, identity resolution across databases, federation membership records, capability advertisement, query routing rules, distributed search architecture, result merging and ranking, consistency models in federation, federated authentication, rate limiting across members, caching federated results, partial failure handling, federated query cost estimation, schema evolution in federation, membership onboarding and offboarding, global query optimizer, distributed transactions, eventual consistency reconciliation, federation governance charter, inter-member SLA contracts, cross-database provenance, federated analytics pipelines, multi-region federation topology, federation security model, federation audits, federation health dashboards, and federation anti-patterns.", "Signature originals - the Signature Federation Doctrine: many databases, one question, zero confusion; a federation is a promise between databases, and promises need contracts, witnesses, and consequences. Clearly labeled Signature-made, never presented as authentic public record.", " Records are ordered by the teaching ladder: Foundations (federation overview, scatter-gather, broadcast, chained patterns, join contracts, schema mapping, identity resolution, membership, capability advertisement, routing rules) -> Compounded (distributed search, result merging, consistency models, federated auth, rate limiting, federated caching, partial failure, query costing, schema evolution, onboarding, offboarding) -> Advanced (global optimizer, distributed transactions, reconciliation, governance charter, SLAs, provenance, analytics pipelines, multi-region topology, security model, audit, health dashboard, anti-patterns, self-audit and mastery).")
DBCFG[SLUG_SIG] = _cfg(
    SLUG_SIG, "The Database Federation Signature Database",
    "The Signature Federation Doctrine: many databases, one question, zero confusion - the full ladder from federation foundations through distributed mechanics to advanced federation governance, reframed as Signature science. Clearly labeled Signature-made, never presented as authentic public record.",
    "federation record", "JAH-DFEDS-", "JAH Federation Archivist (Signature)",
    "Federation archivist - Signature editions: the Signature Federation Doctrine, clearly labeled Signature-made and never presented as authentic public record; teaches progressively along the ladder from foundations through compounded to advanced; answers from many angles using only archive data from this system",
    "signature",
    "Search federated queries, join contracts, membership, topologies...",
    "Ask about the Signature federation doctrine...",
    "Seeded Signature-original federation records, marching toward one million records. Presented in teaching-ladder order: foundations, compounded, advanced.",
    "Foundations · Compounded · Advanced - each tier opens on demand and loads only what you open",
    "Generate clearly-labeled Signature federation studies. Seeded archive records are the authoritative entries.",
    "federation-study", "federation-demo",
    "I am the JAH Federation Archivist (Signature). Ask me about the Signature Federation Doctrine - many databases, one question, zero confusion.",
    "Public records - real, fact-checked federation knowledge: federated query patterns (scatter-gather, broadcast, chained), cross-database join contracts, schema mapping, identity resolution across databases, federation membership records, capability advertisement, query routing rules, distributed search architecture, result merging and ranking, consistency models in federation, federated authentication, rate limiting across members, caching federated results, partial failure handling, federated query cost estimation, schema evolution in federation, membership onboarding and offboarding, global query optimizer, distributed transactions, eventual consistency reconciliation, federation governance charter, inter-member SLA contracts, cross-database provenance, federated analytics pipelines, multi-region federation topology, federation security model, federation audits, federation health dashboards, and federation anti-patterns.", "Signature originals - the Signature Federation Doctrine: many databases, one question, zero confusion; a federation is a promise between databases, and promises need contracts, witnesses, and consequences. Clearly labeled Signature-made, never presented as authentic public record.", " Records are ordered by the teaching ladder: Foundations (federation overview, scatter-gather, broadcast, chained patterns, join contracts, schema mapping, identity resolution, membership, capability advertisement, routing rules) -> Compounded (distributed search, result merging, consistency models, federated auth, rate limiting, federated caching, partial failure, query costing, schema evolution, onboarding, offboarding) -> Advanced (global optimizer, distributed transactions, reconciliation, governance charter, SLAs, provenance, analytics pipelines, multi-region topology, security model, audit, health dashboard, anti-patterns, self-audit and mastery).")


base.DBCFG = DBCFG

assert set(DEMOS) == {e["demo_key"] for e in ENTRIES}, "demo map misses entries"


def _whole_system_hit(title):
    """True if the title exists anywhere: exact index gate OR live shard corpus."""
    hx_hits = base.GATE.check("probe", title)
    if hx_hits:
        return hx_hits
    if norm_title(title) in TITLE_CORPUS:
        return [["shard-corpus", "?"]]
    return []


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        hits = _whole_system_hit(title)
        if hits:
            print("  gate refused (cross-db dupe): %s -> %s" % (title, hits[0][0]), flush=True)
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
        demo_fn = DEMOS[e["demo_key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["demo_data"])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        TITLE_CORPUS.add(norm_title(title))
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
    for slug in (SLUG_PUB, SLUG_SIG):
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
        gen_path = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(gen_js)
        # JS hygiene: node --check on extracted page scripts and gen-*.js
        scripts = _extract_scripts(page)
        assert scripts, "no inline scripts found in %s" % slug
        for i, body in enumerate(scripts):
            chk = "/tmp/govf2_check_%d.js" % i
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

    fragment = {
        "public": {
            "slug": SLUG_PUB,
            "name": DBCFG[SLUG_PUB]["name"],
            "tagline": DBCFG[SLUG_PUB]["tagline"],
            "record_kind": DBCFG[SLUG_PUB]["record_kind"],
            "id_prefix": DBCFG[SLUG_PUB]["prefix"],
            "ai_name": DBCFG[SLUG_PUB]["ai"],
            "local_index": SHARD_BASE + "/data/%s/index.jsonl.gz" % SLUG_PUB,
            "record_count": 34,
            "status": "staged",
            "full_records": 34,
            "index": SHARD_BASE + "/data/%s/index.jsonl.gz" % SLUG_PUB,
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % SLUG_PUB,
            "source": "public-harvest",
        },
        "signature": {
            "slug": SLUG_SIG,
            "name": DBCFG[SLUG_SIG]["name"],
            "tagline": DBCFG[SLUG_SIG]["tagline"],
            "record_kind": DBCFG[SLUG_SIG]["record_kind"],
            "id_prefix": DBCFG[SLUG_SIG]["prefix"],
            "ai_name": DBCFG[SLUG_SIG]["ai"],
            "local_index": SHARD_BASE + "/data/%s/index.jsonl.gz" % SLUG_SIG,
            "record_count": 34,
            "status": "staged",
            "full_records": 34,
            "index": SHARD_BASE + "/data/%s/index.jsonl.gz" % SLUG_SIG,
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % SLUG_SIG,
            "source": "signature",
        },
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("DONE: %d databases, %d records. Merger handles manifest/api/restamp/commit." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
