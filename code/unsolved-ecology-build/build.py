#!/usr/bin/env python3
"""Build the Unsolved Ecology databases for JAH Databases
(Manon's 16:15 orders, Unsolved Problems Solved batch).

Verified 2026-10-17: ID prefixes JAH-USCY- / JAH-USCYS- verified free - zero hits
in the manifest id_prefix values (2,602 databases) and zero hits in every shard
index and chunk file of jah-databases-data-1 (full grep sweep over
data/*/index.jsonl.gz and data/*/chunks/*.jsonl.gz).
All 68 titles (34 public + 34 " (Signature Edition)") pre-checked against the
whole-system dedupe gate: zero collisions, zero refusals.

Creates two NEW databases, 34 ladder-ordered records each:

  unsolved-ecology              - The Unsolved Ecology Database
                                  (public-harvest: 34 real, fact-checked famous
                                  unsolved ecology problems - predicting ecosystem
                                  collapse, the biodiversity-function relationship,
                                  trophic cascade mechanics, why rainforests are
                                  hyperdiverse, microbial ecosystem roles,
                                  restoration success principles, and the rest -
                                  each with problem, background, why_it_matters,
                                  and a Signature solution pointer; ladder_rank 1-34)
  unsolved-ecology-signature    - The Unsolved Ecology Signature Database
                                  (Signature originals: the same 34 problems
                                  through the Signature lens, titles suffixed
                                  " (Signature Edition)", src signature, every
                                  signature_solution opening with the EXACT
                                  label "Signature-generated proposed solution
                                  - not established science", full treatment
                                  with assumptions, reasoning path, mechanism,
                                  confirm/refute evidence, and what it does NOT
                                  claim; honesty rule enforced - never proof,
                                  never peer acceptance, never speculation as
                                  settled)

CONCURRENCY: this builder NEVER touches data/manifest.json, api.json,
index.html (hub), README.md, or docs/AI_ACCESS.md, and NEVER git commits or
pushes. A merger handles registration. Outputs only:
  db/unsolved-ecology/ + db/unsolved-ecology-signature/ (index.html + gen-*.js)
  jah-databases-data-1/data/unsolved-ecology[-signature]/ (index + chunk-0000)
  code/unsolved-ecology-build/ (this pipeline)
  hidden_files/missing-builds/fragments/unsolved-ecology.json (written by hand)

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_unsolved_ecology import ENTRIES, SIG_TAIL, LABEL
from demos_unsolved_ecology import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Method applied to ecology: "
                "every unsolved problem a field question, the solution explorer the "
                "Signature system's walkthrough, confirm-and-refute panels the oath of "
                "honesty. Every signature_solution opens with the exact label "
                "\"Signature-generated proposed solution - not established science\" and "
                "carries the full treatment: assumptions, reasoning path, proposed "
                "mechanism, what would confirm or kill it, and what it does NOT claim. "
                "Clearly labeled Signature-made, never presented as established science "
                "or authentic public record.")
    pub_line = ("Public records - 34 real, fact-checked famous unsolved problems in "
                "ecology: why the tropics hold so many species, what sets species "
                "richness, why invasions succeed or fail, predator-prey cycles, sudden "
                "collapse, extinction, the biodiversity-function relationship, microbial "
                "roles, forests that never return, food-web stability, dispersal, "
                "restoration, trophic cascades, disturbance, productivity, neutral vs "
                "niche theory, the plankton paradox, disease dilution, forest carbon, "
                "diversity-stability, metacommunities, plant-soil feedbacks, early "
                "warnings, ecological memory, forecasting collapse, rainforest "
                "hyperdiversity, uncultured microbes, metabolic scaling, novel "
                "ecosystems, May's paradox, rare species, cross-ecosystem subsidies, "
                "valuing ecosystem services, and a unified theory of ecology. Every "
                "record carries the problem, its background, why it matters, key "
                "points, requirements, standards, citations, and a working "
                "solution-explorer demonstration program.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (tropics, "
              "species-area, invasions, predator-prey, collapse, extinction, "
              "biodiversity-function, microbes, forest return, food webs, dispersal, "
              "restoration) -> Compounded (trophic cascades, disturbance, "
              "productivity, neutral-niche, plankton, dilution, forest carbon, "
              "diversity-stability, metacommunity, Janzen-Connell, early warning, "
              "legacy) -> Advanced (collapse forecasting, rainforest hyperdiversity, "
              "uncultured microbes, metabolic scaling, novel ecosystems, May's "
              "paradox, rare species, subsidies, service valuation, unified theory).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: problem, background, "
                  "why it matters, the Signature solution approach, key points, "
                  "requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search tropics, species-area, invasions, predator-prey, collapse, extinction, biodiversity function, microbes, food webs, dispersal, restoration, cascades, disturbance, productivity, neutral theory, plankton, dilution, carbon, stability, metacommunity, Janzen-Connell, early warning, legacy, rainforest, metabolic scaling, novel ecosystems, rare species, subsidies...",
        "chat_ph": "Ask about unsolved problems in ecology...",
        "archive_blurb": ("Seeded %s unsolved-ecology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, problem, background, why_it_matters, "
                   "signature_solution, key_points, requirements, standards, citations, src, "
                   "ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved-ecology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about unsolved problems in ecology - from why the tropics are rich and how food webs hold together through trophic cascades, collapse prediction, and restoration, to rainforest hyperdiversity, microbial roles, and what a unified theory of ecology would look like." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-ecology-study", "gen_demo_kind": "unsolved-ecology-demo",
        "source": source,
    }

CITATION = ("Unsolved problems in ecology (standard references per record: von Humboldt 1807; "
            "Arrhenius 1921; MacArthur and Wilson 1967; Elton 1958; Lotka 1925; Volterra 1926; "
            "Scheffer et al. 2001; Holling 1973; Pimm et al. 2014; Tilman et al. 1997; Cardinale et al. "
            "2012; van der Heijden et al. 2008; Falkowski et al. 2008; May 1972; Dunne et al. 2002; "
            "Nathan et al. 2002; Suding et al. 2004; Hairston, Smith and Slobodkin 1960; Estes et al. "
            "2011; Connell 1978; Lindeman 1942; Hubbell 2001; Hutchinson 1961; Ostfeld and Keesing "
            "2012; Pan et al. 2011; Leibold et al. 2004; Janzen 1970; Connell 1971; Carpenter et al. "
            "2011; Peterson 2002; Clark et al. 2001; Gentry 1988; Rappe and Giovannoni 2003; Brown et al. "
            "2004; Hobbs et al. 2006; Allesina and Tang 2012; Lyons et al. 2005; Polis et al. 1997; "
            "Costanza et al. 1997; Daily 1997; Loreau 2010; Harte 2011). Signature editions are his "
            "original Signature Method - clearly labeled Signature-made, never established science.")

DBCFG = {}
DBCFG["unsolved-ecology"] = _cfg(
    "unsolved-ecology", "The Unsolved Ecology Database",
    "Thirty-four famous unsolved problems in ecology - from why the tropics are rich to "
    "whether collapse can be predicted - each fact-checked as the world knows it, each "
    "carrying the problem, its background, why it matters, and the Signature system's "
    "proposed solution path, honestly labeled as proposal, never established science.",
    "unsolved problem record", "JAH-USCY-", "JAH Unsolved Ecology Archivist",
    "unsolved ecology archivist - thirty-four famous unsolved problems from tropical "
    "richness and species-area through food webs, cascades, collapse, restoration, and "
    "microbial roles, to rainforest hyperdiversity and a unified theory of ecology; "
    "teaching progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system; the Signature "
    "approach is always labeled a proposed path, never established science",
    CITATION, "public")
DBCFG["unsolved-ecology-signature"] = _cfg(
    "unsolved-ecology-signature", "The Unsolved Ecology Signature Database",
    "His original Signature Method applied to ecology's thirty-four famous unsolved "
    "problems: every problem a field question, the solution explorer the walkthrough, "
    "confirm-and-refute panels the oath of honesty. Full Signature treatments, clearly "
    "labeled Signature-made, never presented as established science.",
    "unsolved problem record", "JAH-USCYS-", "JAH Unsolved Ecology Archivist (Signature)",
    "unsolved ecology archivist - Signature editions: his original Signature Method on "
    "the thirty-four famous unsolved problems, clearly labeled Signature-made and never "
    "presented as established science; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only archive data from "
    "this system",
    CITATION, "signature")

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
        sol = LABEL + " " + (e["sol_sig"] if sig else e["sol_public"])
        # sol_sig already opens with LABEL; avoid doubling it
        if sig and sol.count(LABEL) > 1:
            sol = e["sol_sig"]
        if sig:
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["description"])
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "problem": e["problem"],
            "background": e["background"],
            "why_it_matters": e["why_it_matters"],
            "signature_solution": sol,
            "how_it_works": sol,
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
                       "note": "Working solution-explorer walkthrough (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def node_check_js(path, label):
    """node --check every page <script> except ld+json blocks (JSON, not JS).
    Pure-JS files (gen-*.js) are checked whole."""
    src = open(path, encoding="utf-8").read()
    blocks = re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                        src, flags=re.S)
    if not blocks:
        blocks = [src]  # pure JS file, no script tags
    n = 0
    for i, b in enumerate(blocks):
        if not b.strip():
            continue
        n += 1
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
            f.write(b)
            tmp = f.name
        p = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
        os.unlink(tmp)
        assert p.returncode == 0, "node --check failed %s block %d: %s" % (label, i, p.stderr[-500:])
    assert n > 0, "no checkable scripts in %s" % label
    print("node --check: %s (%d script blocks) clean" % (label, n), flush=True)


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
    for slug in ("unsolved-ecology", "unsolved-ecology-signature"):
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
            for k in ("id", "t", "g", "name", "title", "description", "problem",
                      "background", "why_it_matters", "signature_solution",
                      "how_it_works", "key_points", "requirements", "standards",
                      "citations", "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert len(r["background"]) > 200 and len(r["why_it_matters"]) > 100, \
                "thin unsolved fields in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            assert LABEL in r["signature_solution"], "honesty label missing in %s" % r["id"]
            assert r["signature_solution"].startswith(LABEL), \
                "label not opening in %s" % r["id"]
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
    tier_name = {"foundations": "Foundations", "compounded": "Compounded",
                 "advanced": "Advanced"}
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "mergePanel" in page, "mergePanel missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "universal build" not in page.lower(), "field leftover in %s" % slug
        assert "public-synthetic-intelligence" not in page, "slug leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(tier_name[r["ladder_tier"]], []).append(
                "%s - %s" % (r["t"], tier_name[r["ladder_tier"]]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
        assert "public-synthetic-intelligence" not in gen_js, "slug leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        node_check_js(gpath, "gen-%s.js" % slug)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # JS hygiene on the finished pages (ld+json excluded inside node_check_js)
    for slug in built:
        node_check_js(os.path.join(REPO, "db", slug, "index.html"), "db/%s/index.html" % slug)

    print("manifest/api/README/docs updates SKIPPED by concurrency rule - merger handles registration.")
    print("DONE: 2 databases, %d records, 0 commits." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
