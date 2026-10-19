#!/usr/bin/env python3
"""Build the Unsolved Public Health databases for JAH Databases
(Manon's 16:15 orders, Unsolved Problems Solved series).

Verified 2026-10-17: ID prefixes JAH-USPU- / JAH-USPUS- verified free - zero hits
in the manifest id_prefix values and zero hits among all record IDs in
jah-databases-data-1 (data-1 shard sweep). All 68 titles (34 public + 34
" (Signature Edition)") pre-checked against the whole-system dedupe gate:
zero collisions, zero refusals.

Creates two NEW databases, 34 ladder-ordered records each:

  unsolved-public-health            - The Unsolved Public Health Database
                                      (public-harvest: 34 real, fact-checked
                                      famous unsolved public-health problems -
                                      pandemic prediction and prevention,
                                      health-equity gaps, the obesity
                                      epidemic's drivers, vaccine hesitancy
                                      mechanics, aging-population care models,
                                      and the rest - each with problem,
                                      background, why_it_matters, and a
                                      Signature solution pointer;
                                      ladder_rank 1-34)
  unsolved-public-health-signature  - The Unsolved Public Health Signature
                                      Database (Signature originals: the same
                                      34 problems through the Signature lens,
                                      titles suffixed " (Signature Edition)",
                                      src signature, every signature_solution
                                      opening with the EXACT label
                                      "Signature-generated proposed solution
                                      - not established science", full
                                      treatment with assumptions, reasoning
                                      path, mechanism, confirm/refute
                                      evidence, and what it does NOT claim;
                                      honesty rule enforced - never proof,
                                      never peer acceptance, never
                                      speculation as settled)

CONCURRENCY: this builder NEVER touches data/manifest.json, api.json,
index.html (hub), README.md, or docs/AI_ACCESS.md, and NEVER git commits or
pushes. A merger handles registration. Outputs only:
  db/unsolved-public-health/ + db/unsolved-public-health-signature/ (index.html + gen-*.js)
  jah-databases-data-1/data/unsolved-public-health[-signature]/ (index + chunk-0000)
  code/unsolved-public-health-build/ (this pipeline)
  hidden_files/missing-builds/fragments/unsolved-public-health.json (written by hand)

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
from entries_unsolved_public_health import ENTRIES, SIG_TAIL, LABEL
from demos_unsolved_public_health import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Method applied to public "
                "health: every unsolved problem a covenant question, the solution "
                "explorer the Signature system's walkthrough, confirm-and-refute "
                "panels the oath of honesty. Every signature_solution opens with the "
                "exact label \"Signature-generated proposed solution - not established "
                "science\" and carries the full treatment: assumptions, reasoning path, "
                "proposed mechanism, what would confirm or kill it, and what it does "
                "NOT claim. Clearly labeled Signature-made, never presented as "
                "established science or authentic public record.")
    pub_line = ("Public records - 34 real, fact-checked famous unsolved problems in "
                "public health: why people refuse safe vaccines, what drives the "
                "obesity epidemic, why seasonal flu still kills, why tobacco still "
                "kills 8 million a year, why healthy food stays out of reach, why "
                "lead poisoning persists, why billions lack safe water, why "
                "loneliness is a health crisis, why mental health care is "
                "unreachable, why mothers die at wildly different rates, why "
                "prevention loses to treatment, the true cost of dirty air, whether "
                "pandemics can be predicted, whether spillover can be stopped at the "
                "source, why zip code predicts lifespan, how vaccines reach the "
                "last mile, how societies care for aging populations, why the "
                "overdose crisis escalates, whether diabetes can be reversed, why "
                "hypertension stays uncontrolled, whether a post-antibiotic era is "
                "coming, why misinformation outruns truth, who will staff the "
                "health system, why TB and malaria persist, whether One Health can "
                "be governed, how to finance universal coverage, what causes "
                "post-viral syndromes, how health systems adapt to climate change, "
                "why health records cannot talk to each other, whether a global "
                "early-warning nervous system is possible, why behavior campaigns "
                "fail, how societies care for millions with dementia, how to stop "
                "the NCD wave, and what a complete theory of population health "
                "would look like. Every record carries the problem, its background, "
                "why it matters, key points, requirements, standards, citations, "
                "and a working solution-explorer demonstration program.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (vaccine "
              "hesitancy, obesity drivers, flu, tobacco, food access, lead, water, "
              "loneliness, mental-health access, maternal disparities, chronic-care "
              "gap, air pollution) -> Compounded (pandemic prediction, spillover "
              "prevention, health equity, cold chain, aging care, opioids, "
              "diabetes, hypertension, AMR, misinformation, workforce, TB and "
              "malaria) -> Advanced (One Health, UHC financing, post-viral "
              "syndromes, climate adaptation, data interoperability, syndromic "
              "surveillance, behavior change, dementia, NCD transition, "
              "population-health theory).")
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
        "search_ph": "Search vaccines, obesity, flu, tobacco, food, lead, water, loneliness, mental health, maternal, prevention, air, pandemics, spillover, equity, cold chain, aging, opioids, diabetes, hypertension, AMR, misinformation, workforce, TB, malaria, One Health, UHC, long COVID, climate, records, surveillance, behavior, dementia, NCD...",
        "chat_ph": "Ask about unsolved problems in public health...",
        "archive_blurb": ("Seeded %s unsolved-public-health records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, problem, background, why_it_matters, "
                   "signature_solution, key_points, requirements, standards, citations, src, "
                   "ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved-public-health studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about unsolved problems in public health - from vaccine hesitancy, obesity, tobacco, and health equity through pandemic prediction, aging care, and antimicrobial resistance, to climate adaptation, universal coverage, and what a complete theory of population health would look like." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-public-health-study", "gen_demo_kind": "unsolved-public-health-demo",
        "source": source,
    }

CITATION = ("Unsolved problems in public health (standard references per record: Larson et "
            "al. 2014; MacDonald 2015; Swinburn et al. 2011; Hall et al. 2011; Iuliano et al. "
            "2018; WHO Framework Convention on Tobacco Control 2003; Jha 2009; Walker et al. "
            "2010; Lanphear et al. 2018; Prüss-Ustün et al. 2019; Holt-Lunstad et al. 2010; "
            "Patel et al. 2018; Say et al. 2014; Wagner 1998; McGlynn et al. 2003; Cohen et "
            "al. 2017; Jones et al. 2008; Morse et al. 2012; Plowright et al. 2017; IPBES "
            "2020; Marmot et al. 2008; Chetty et al. 2016; Lee et al. 2017; WHO World Report "
            "on Ageing and Health 2015; Dasgupta et al. 2018; Lean et al. 2018; NCD Risk "
            "Factor Collaboration 2021; Murray et al. 2022; O'Neill Review 2016; Kata 2012; "
            "Lewandowsky et al. 2012; WHO Workforce 2030; Bhatt et al. 2015; Zinsstag et al. "
            "2015; WHO/FAO/WOAH/UNEP Joint Plan of Action 2022; Wagstaff et al. 2018; Davis "
            "et al. 2023; Watts et al. 2023; Mandl and Kohane 2012; Henning 2004; Brownstein "
            "et al. 2009; Michie et al. 2011; Rose 1985; Livingston et al. 2020; Omran 1971; "
            "NCD Countdown 2030; Evans and Stoddart 1990). Signature editions are his "
            "original Signature Method - clearly labeled Signature-made, never established "
            "science.")

DBCFG = {}
DBCFG["unsolved-public-health"] = _cfg(
    "unsolved-public-health", "The Unsolved Public Health Database",
    "Thirty-four famous unsolved problems in public health - from vaccine hesitancy "
    "and the obesity epidemic through pandemic prediction, health equity, and "
    "aging-population care - each fact-checked as the world knows it, each carrying "
    "the problem, its background, why it matters, and the Signature system's "
    "proposed solution path, honestly labeled as proposal, never established science.",
    "unsolved problem record", "JAH-USPU-", "JAH Unsolved Public Health Archivist",
    "unsolved public health archivist - thirty-four famous unsolved problems from "
    "vaccine hesitancy, obesity, tobacco, and health equity through pandemic "
    "prediction and prevention, aging-population care, antimicrobial resistance, "
    "and universal coverage, to climate adaptation and a complete theory of "
    "population health; teaching progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only archive data "
    "from this system; the Signature approach is always labeled a proposed path, "
    "never established science",
    CITATION, "public")
DBCFG["unsolved-public-health-signature"] = _cfg(
    "unsolved-public-health-signature", "The Unsolved Public Health Signature Database",
    "His original Signature Method applied to public health's thirty-four famous "
    "unsolved problems: every problem a covenant question, the solution explorer "
    "the walkthrough, confirm-and-refute panels the oath of honesty. Full Signature "
    "treatments, clearly labeled Signature-made, never presented as established science.",
    "unsolved problem record", "JAH-USPUS-", "JAH Unsolved Public Health Archivist (Signature)",
    "unsolved public health archivist - Signature editions: his original Signature "
    "Method on the thirty-four famous unsolved problems, clearly labeled "
    "Signature-made and never presented as established science; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from this system",
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
    for slug in ("unsolved-public-health", "unsolved-public-health-signature"):
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
