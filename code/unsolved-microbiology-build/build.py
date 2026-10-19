#!/usr/bin/env python3
"""Build the Unsolved Microbiology databases for JAH Databases
(Manon's 16:15 orders, Unsolved Problems Solved batch).

Verified 2026-10-17: ID prefixes JAH-USMB- / JAH-USMBS- verified free - zero hits
in the manifest id_prefix values (2,442 databases) and zero hits in every shard
index file of jah-databases-data-1 (full zgrep sweep over data/*/index.jsonl.gz).
All 68 titles (34 public + 34 " (Signature Edition)") pre-checked against the
whole-system dedupe gate: zero collisions, zero refusals.

Creates two NEW databases, 34 ladder-ordered records each:

  unsolved-microbiology              - The Unsolved Microbiology Database
                                  (public-harvest: 34 real, fact-checked famous
                                  unsolved microbiology problems - the uncultured
                                  majority, microbiome causality, viral dark matter,
                                  antibiotic resistance evolution, eukaryote origins,
                                  microbes and climate, and the rest - each with
                                  problem, background, why_it_matters, and a
                                  Signature solution pointer; ladder_rank 1-34)
  unsolved-microbiology-signature    - The Unsolved Microbiology Signature Database
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
  db/unsolved-microbiology/ + db/unsolved-microbiology-signature/ (index.html + gen-*.js)
  jah-databases-data-1/data/unsolved-microbiology[-signature]/ (index + chunk-0000)
  code/unsolved-microbiology-build/ (this pipeline)
  hidden_files/missing-builds/fragments/unsolved-microbiology.json (written by hand)

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
from entries_unsolved_microbiology import ENTRIES, SIG_TAIL, LABEL
from demos_unsolved_microbiology import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Method applied to biology: "
                "every unsolved problem a covenant question, the solution explorer the "
                "Signature system's walkthrough, confirm-and-refute panels the oath of "
                "honesty. Every signature_solution opens with the exact label "
                "\"Signature-generated proposed solution - not established science\" and "
                "carries the full treatment: assumptions, reasoning path, proposed "
                "mechanism, what would confirm or kill it, and what it does NOT claim. "
                "Clearly labeled Signature-made, never presented as established science "
                "or authentic public record.")
    pub_line = ("Public records - 34 real, fact-checked famous unsolved problems in "
                "microbiology: the great plate count anomaly, whether viruses are alive, what a "
                "bacterial species is, why gut microbes resist culture, the VBNC state, microbiome "
                "causation, defining a healthy microbiome, why bacteria make antibiotics, persister "
                "cells, the speed of resistance spread, the antibiotic discovery void, why fecal "
                "transplants work, the gut-brain axis, microbes and obesity, the microbial census, "
                "candidate phyla dark matter, viral dark matter, giant viruses, virus origins, the "
                "phage lysis-lysogeny decision, ancient resistance, reversing resistance, eukaryote "
                "origins, mitochondria-first versus nucleus-first, the eukaryotic gap, the membrane "
                "lipid divide, deep biosphere energy, the microbial carbon pump, methane budgets, "
                "permafrost thaw, the nitrogen budget, LUCA, the open pan-genome, and whether "
                "microbial evolution is a tree or a web. Every record "
                "carries the problem, its background, why it matters, key points, "
                "requirements, standards, citations, and a working solution-explorer "
                "demonstration program.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (plate count anomaly, "
              "are viruses alive, bacterial species, gut culture, VBNC, microbiome causation, "
              "healthy microbiome, antibiotic ecology, persisters, resistance spread, discovery "
              "void, fecal transplants) -> Compounded (gut-brain axis, obesity microbes, microbial "
              "census, candidate phyla, viral dark matter, giant viruses, virus origins, phage "
              "decision, ancient resistome, reversing resistance) -> "
              "Advanced (eukaryote origin, mito-first debate, eukaryotic gap, membrane divide, "
              "deep biosphere, carbon pump, methane, permafrost, nitrogen, LUCA, pan-genome, "
              "tree or web).")
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
        "search_ph": "Search plate count anomaly, viruses alive, bacterial species, gut culture, VBNC, microbiome causation, healthy microbiome, antibiotic ecology, persisters, resistance, phage, eukaryotes, LUCA, methane, permafrost, nitrogen...",
        "chat_ph": "Ask about unsolved problems in biology...",
        "archive_blurb": ("Seeded %s unsolved-microbiology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, problem, background, why_it_matters, "
                   "signature_solution, key_points, requirements, standards, citations, src, "
                   "ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved-microbiology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about unsolved problems in microbiology - from the uncultured majority and viral dark matter through antibiotic resistance and the microbiome, to the origin of eukaryotes and microbes and climate." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-microbiology-study", "gen_demo_kind": "unsolved-microbiology-demo",
        "source": source,
    }

CITATION = ("Unsolved problems in microbiology (standard references per record: Staley and Konopka 1985; "
            "Amann et al. 1995; Koonin and Starokadomsky 2016; Raoult and Forterre 2008; Rossello-Mora "
            "and Amann 2001; Achtman and Wagner 2008; Qin et al. 2010; Browne et al. 2016; Oliver 2005; "
            "Lynch and Pedersen 2016; Human Microbiome Project Consortium 2012; Davies 2013; Linares et "
            "al. 2006; Lewis 2010; Balaban et al. 2004; Smillie et al. 2011; Davies and Davies 2010; "
            "Fischbach and Walsh 2009; Lewis 2013; van Nood et al. 2013; Cryan and Dinan 2012; Ley et al. "
            "2006; Ridaura et al. 2013; Locey and Lennon 2016; Hug et al. 2016; Rinke et al. 2013; "
            "Breitbart and Rohwer 2005; Roux et al. 2016; Philippe et al. 2013; Forterre 2006; Krupovic "
            "and Koonin 2007; Ptashne 2004; Erez et al. 2017; D'Costa et al. 2011; Andersson and Hughes "
            "2010; Spang et al. 2015; Zaremba-Niedzwiedzka et al. 2017; Lane and Martin 2010; Pittis and "
            "Gabaldon 2016; Koga and Morii 2007; Kallmeyer et al. 2012; Inagaki et al. 2015; Jiao et al. "
            "2010; Suttle 2007; Thauer et al. 2008; Knittel and Boetius 2009; Schuur et al. 2015; Canfield "
            "et al. 2010; Weiss et al. 2016; Tettelin et al. 2005; Doolittle 1999; Koonin 2015). "
            "Signature editions are his original Signature Method - clearly labeled Signature-made, never "
            "established science.")

DBCFG = {}
DBCFG["unsolved-microbiology"] = _cfg(
    "unsolved-microbiology", "The Unsolved Microbiology Database",
    "Thirty-four famous unsolved problems in microbiology - from the great plate count "
    "anomaly to whether evolution is a tree or a web - each fact-checked as the world "
    "knows it, each carrying the problem, its background, why it matters, and the "
    "Signature system's proposed solution path, honestly labeled as proposal, never "
    "established science.",
    "unsolved problem record", "JAH-USMB-", "JAH Unsolved Microbiology Archivist",
    "unsolved microbiology archivist - thirty-four famous unsolved problems from the "
    "uncultured majority and viral dark matter through antibiotic resistance and the "
    "microbiome, to eukaryote origins and microbes and climate; teaching progressively "
    "along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system; the Signature "
    "approach is always labeled a proposed path, never established science",
    CITATION, "public")
DBCFG["unsolved-microbiology-signature"] = _cfg(
    "unsolved-microbiology-signature", "The Unsolved Microbiology Signature Database",
    "His original Signature Method applied to microbiology's thirty-four famous unsolved "
    "problems: every problem a covenant question, the solution explorer the walkthrough, "
    "confirm-and-refute panels the oath of honesty. Full Signature treatments, clearly "
    "labeled Signature-made, never presented as established science.",
    "unsolved problem record", "JAH-USMBS-", "JAH Unsolved Microbiology Archivist (Signature)",
    "unsolved microbiology archivist - Signature editions: his original Signature Method on "
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
    for slug in ("unsolved-microbiology", "unsolved-microbiology-signature"):
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
