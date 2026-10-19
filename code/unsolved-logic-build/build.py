#!/usr/bin/env python3
"""Build the Unsolved Logic databases for JAH Databases (unsolved-problems
SOLVED series, 2026-10-17).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,602 databases)
PLUS every shard index in jah-databases-data-1 (1,049 index files):
zero 'unsolved-logic' slugs/names; ID prefixes JAH-USLG- and JAH-USLGS-
verified free in manifest id_prefix values AND in every shard index file
(zero hits). The 68 titles were run through the whole-system dedupe gate
before authoring: zero collisions.

This build creates two NEW databases, 34 ladder-ordered records each:

  unsolved-logic             - The Unsolved Logic Database
                               (public: 34 real, famous unsolved problems
                               of logic - fact-checked - from the liar
                               paradox to optimal proof systems)
  unsolved-logic-signature   - The Unsolved Logic Signature Database
                               (signature: the Signature system's
                               proposed solution approach to each of the
                               same 34 problems - ALWAYS labeled
                               "Signature-generated proposed solution -
                               not established science", never presented
                               as established science)

34 records each, ladder_rank 1-34 non-decreasing, tiers
foundations -> compounded -> advanced; shard index written in ladder order.

Pipeline replicates code/combat-judo-build/build.py exactly for page
structure: build_page + build_gen_js from numbering-build, sweep pass,
Exhaustive pill + merger button + tab guard carried over from the template.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never git commits or
pushes. The merger owns those. This script writes only:
  db/unsolved-logic/ + db/unsolved-logic-signature/ (index.html + gen-*.js)
  jah-databases-data-1/data/unsolved-logic[-signature]/ (index.jsonl.gz + chunks)
  ~/workspace/hidden_files/missing-builds/fragments/unsolved-logic.json

Demos: every record ships a solution-explorer walkthrough - a real,
runnable, stdlib-only Python program with adjustable assumptions,
step-by-step reasoning, and confirm/refute panels. Machine-executed by
this build: each prints real computed values, asserts tight bounds, and
ends with the OK marker.

No website references. No Facebook. Screened content.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/unsolved-logic.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_unsolved_logic import ENTRIES, SIG_LABEL, SIG_TAIL
from demos_unsolved_logic import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature proposed solutions - the Signature system "
                "proposed solution approach to each of the 34 problems, "
                "every one opened with the exact label 'Signature-"
                "generated proposed solution - not established science', "
                "laid out step by step with assumptions, reasoning path, "
                "confirming and refuting evidence, and what it does NOT "
                "claim. Clearly labeled Signature work, never presented "
                "as established science.")
    pub_line = ("Public records - 34 real, famous unsolved problems of "
                "logic, fact-checked: the limits of proof systems, "
                "independence results beyond ZFC, the nature of truth in "
                "paraconsistent logics, automated theorem-proving "
                "completeness, and the P vs NP connection to proof "
                "complexity. Every record carries the problem statement, "
                "its background and history, why it matters, and a "
                "pointer to the Signature edition's proposed solution "
                "approach.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(the liar, sorites, what truth is, Curry, Yablo, "
              "Grelling-Nelson, Berry, unexpected hanging, lottery, "
              "ravens, preface, Moore) -> Compounded (true "
              "contradictions, v-Curry, liar's revenge, naive truth, "
              "natural incompleteness, Hilbert's program, continuum "
              "hypothesis, fragments of choice, large cardinals, "
              "relevance logic R, higher-order proof search, the Frege "
              "barrier) -> Advanced (circuit lower bounds in weak "
              "theories, determinacy, inner models, forcing axioms, "
              "axiom justification, singular cardinals, Hilbert's 24th "
              "problem, categoricity, constructive content, optimal "
              "proof systems).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record is the full file: problem, background, "
                  "why it matters, the Signature solution treatment, and a working "
                  "solution-explorer demonstration program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature proposed solutions organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search liar paradox, sorites, truth, Curry, Yablo, continuum hypothesis, large cardinals, paraconsistent, proof complexity, P vs NP, determinacy, forcing axioms...",
        "chat_ph": "Ask about unsolved problems of logic...",
        "archive_blurb": ("Seeded %s unsolved-logic records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature proposed-solution" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, problem, background, why_it_matters, "
                   "signature_solution, description, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Paradoxes of Truth \u00b7 Paradoxes of Vagueness and Reason \u00b7 Paraconsistency and Truth \u00b7 Incompleteness and Axioms \u00b7 Proof, Computation, and Automation \u00b7 Set-Theoretic Frontiers \u00b7 Foundations of Proof - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved-logic studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about the great unsolved problems of logic - from the liar and sorites paradoxes through paraconsistency and truth, incompleteness and independence beyond ZFC, automated proof search, proof complexity and its P vs NP connection, to determinacy, forcing axioms, and optimal proof systems." % ai,
        "gen_fields": ["Paradoxes of Truth", "Paradoxes of Vagueness and Reason",
                       "Paraconsistency and Truth", "Incompleteness and Axioms",
                       "Proof, Computation, and Automation",
                       "Set-Theoretic Frontiers", "Foundations of Proof"],
        "gen_kind": "unsolved-logic-study", "gen_demo_kind": "unsolved-logic-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["unsolved-logic"] = _cfg(
    "unsolved-logic", "Unsolved Logic Database",
    "The great unsolved problems of logic: the limits of proof systems, "
    "independence beyond ZFC, the nature of truth in paraconsistent "
    "logics, automated theorem-proving completeness, and the P vs NP "
    "connection to proof complexity - 34 famous open problems, "
    "fact-checked, taught along the ladder from foundations to advanced.",
    "unsolved problem record", "JAH-USLG-", "JAH Unsolved Logic Archivist",
    "unsolved logic archivist - teaching the 34 great open problems of "
    "logic from the liar paradox to optimal proof systems; problem "
    "statements fact-checked, backgrounds and stakes fully laid out; "
    "teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math - using only archive "
    "data from this system",
    "public")
DBCFG["unsolved-logic-signature"] = _cfg(
    "unsolved-logic-signature", "Unsolved Logic Signature Database",
    "The Signature system's proposed solution approaches to the 34 great "
    "unsolved problems of logic - every solution opened with the exact "
    "label 'Signature-generated proposed solution - not established "
    "science', laid out step by step with assumptions, reasoning, "
    "confirming and refuting evidence, and honest limits. Clearly "
    "labeled Signature work, never presented as established science.",
    "unsolved problem record", "JAH-USLGS-", "JAH Unsolved Logic Archivist (Signature)",
    "unsolved logic archivist - Signature editions: the Signature "
    "system proposed solution approaches to the 34 problems, each "
    "opened with the exact honesty label Signature-generated proposed "
    "solution - not established science, and honest about what is not "
    "claimed; teaches progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles using "
    "only archive data from this system",
    "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"
assert len(ENTRIES) == 34, "need exactly 34 entries"


def _sig_solution_text(e):
    parts = [SIG_LABEL]
    parts.append("Assumptions:")
    parts.extend("  " + a for a in e["assumptions"])
    parts.append("Reasoning path:")
    parts.extend("  " + s for s in e["steps"])
    parts.append("What would confirm it:")
    parts.extend("  [+] " + c for c in e["confirm"])
    parts.append("What would refute it:")
    parts.extend("  [-] " + r for r in e["refute"])
    parts.append("What it does NOT claim:")
    parts.extend("  [x] " + n for n in e["not_claims"])
    return "\n".join(parts)


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    refused = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            refused.append(title)
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            signature_solution = _sig_solution_text(e)
            description = (SIG_LABEL + " " + e["problem"] + " " +
                           e["why_it_matters"])
            how = e["background"] + "\n\n" + signature_solution
            key_points = list(e["steps"])
            requirements = list(e["assumptions"])
            standards = [
                "Signature-generated proposed solution - not established science.",
                "Open problem in established science; the approach claims no proof and no peer acceptance.",
                "Honesty rule: where the answer is 'we do not know', the record says so.",
            ]
            citations = list(e["citations"]) + [SIG_TAIL]
            src = "signature"
        else:
            signature_solution = (SIG_LABEL + " See the Signature edition (" +
                                  title + " (Signature Edition)) for the full "
                                  "proposed solution approach. " + e["sig_pointer"])
            description = e["problem"] + " " + e["why_it_matters"]
            how = e["background"]
            key_points = [e["sig_pointer"]]
            requirements = [
                "No prerequisites - each record states its problem plainly.",
                "Each record is self-contained: problem, background, and stakes.",
            ]
            standards = [
                "Open problem - unsolved in established science as of 2026.",
                "Problem statements fact-checked against the logic literature.",
            ]
            citations = list(e["citations"])
            src = "public-harvest"
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "problem": e["problem"],
            "background": e["background"],
            "why_it_matters": e["why_it_matters"],
            "signature_solution": signature_solution,
            "description": description,
            "how_it_works": how,
            "key_points": key_points,
            "requirements": requirements,
            "standards": standards,
            "citations": citations,
            "src": src,
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          key_points, "; ".join(requirements))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Solution-explorer walkthrough (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    assert ranks == list(range(1, 35)), "ladder ranks must be 1..34 for %s" % slug
    return recs, refused


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
    all_refused = []
    for slug in ("unsolved-logic", "unsolved-logic-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        recs, refused = build_records(slug, source)
        built[slug] = recs
        all_refused.extend(refused)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "problem", "background",
                      "why_it_matters", "signature_solution", "description",
                      "how_it_works", "key_points", "requirements", "standards",
                      "citations", "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            assert len(r["background"].split(". ")) >= 3, "background too thin in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
                assert SIG_LABEL.lower() in r["signature_solution"].lower(), \
                    "sig label missing in %s" % r["id"]
                assert SIG_LABEL.lower() in r["description"].lower(), \
                    "sig label missing in description %s" % r["id"]
            else:
                assert r["src"] == "public-harvest"
                assert SIG_LABEL.lower() in r["signature_solution"].lower(), \
                    "sig pointer label missing in %s" % r["id"]
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
        assert "public-synthetic-intelligence" not in page, "slug leftover in %s" % slug
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
        assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # JS hygiene: node --check on extracted inline page scripts + gen-*.js
    for slug in built:
        ddir = os.path.join(REPO, "db", slug)
        page = open(os.path.join(ddir, "index.html"), encoding="utf-8").read()
        scripts = re.findall(r"<script>(.*?)</script>", page, re.S)
        assert scripts, "no inline scripts found in %s" % slug
        for i, body in enumerate(scripts):
            tmp = "/tmp/ul_jscheck_%s_%d.js" % (slug.replace("-", "_"), i)
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(body)
            p = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
            assert p.returncode == 0, "node --check failed page script %d of %s: %s" % (i, slug, p.stderr[:500])
        gp = os.path.join(ddir, "gen-%s.js" % slug)
        p = subprocess.run(["node", "--check", gp], capture_output=True, text=True)
        assert p.returncode == 0, "node --check failed %s: %s" % (gp, p.stderr[:500])
        print("js hygiene: %s page scripts + gen js node-clean" % slug, flush=True)

    # Fragment for the merger (merger owns manifest.json / api.json / restamp).
    def frag(slug, source):
        cfg = DBCFG[slug]
        url = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        return {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": url,
            "record_count": len(built[slug]),
            "status": "live",
            "full_records": len(built[slug]),
            "index": url,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": source,
        }
    fragment = {
        "public": frag("unsolved-logic", "public-harvest"),
        "signature": frag("unsolved-logic-signature", "signature"),
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("gate refusals during build: %d" % len(all_refused), flush=True)
    for t in all_refused:
        print("  refused: %s" % t, flush=True)
    print("DONE: %d records across 2 databases; merger verifies live." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
