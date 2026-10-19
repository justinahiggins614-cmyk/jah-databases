#!/usr/bin/env python3
"""Build the Unsolved Genetics databases for JAH Databases
(Manon's 16:15 orders, Unsolved Problems Solved series, batch 1).

Two databases, 34 ladder-ordered records each:

  unsolved-genetics             - The Unsolved Genetics Database
                                  (public-harvest: 34 real, fact-checked
                                  unsolved genetics problems - problem,
                                  background, why it matters, plus a short
                                  pointer to the Signature proposed
                                  solution)
  unsolved-genetics-signature   - The Unsolved Genetics Signature Database
                                  (the SAME 34 problems through the
                                  Signature lens; every signature_solution
                                  opens with the exact label
                                  "Signature-generated proposed solution -
                                  not established science" and carries the
                                  full treatment: assumptions, reasoning
                                  path, confirm/refute panels, and what it
                                  does NOT claim; src signature, titles
                                  suffixed " (Signature Edition)", never
                                  presented as authentic public record)

Ladder ordering (his TEACHING LADDER): rank 1 (what non-coding DNA does)
-> rank 34 (the RNA world); the shard index is written in ladder order so
pages present simple -> compounded -> complex.

ID prefixes: JAH-USGE- (public) and JAH-USGES- (signature), verified free
in the manifest id_prefix values and in every shard index file in
jah-databases-data-1 (zero hits).

Honesty rule throughout: never claim proof, never imply peer acceptance,
never present speculation as settled. No real-person DNA. No medical
claims. Nothing hate-adjacent, profane, or inappropriate; no religious
talk.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_unsolved_genetics.py). Every demo is a solution-explorer
walkthrough printing its real computed values, asserting tight bounds
(never float exact-equality), carrying confirm/refute panels, and ending
with the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or
pushes. A merger handles those. It only writes:
  db/unsolved-genetics/ + db/unsolved-genetics-signature/
  (index.html + gen-*.js each)
  jah-databases-data-1/data/unsolved-genetics[-signature]/
  (index.jsonl.gz + chunks/chunk-0000.jsonl.gz)
  hidden_files/missing-builds/fragments/unsolved-genetics.json

Never the words "bat belt" anywhere. No website references. No Facebook.
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
from entries_unsolved_genetics import ENTRIES, SIG_TAIL, SIG_LENS, HONEST_LABEL
from demos_unsolved_genetics import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature Genetics "
                "Method: every unsolved genetics problem approached as a "
                "covenant of evidence, mechanism, and testable prediction. "
                "Every solution opens with the exact label Signature-"
                "generated proposed solution - not established science, and "
                "carries assumptions, reasoning, confirm/refute panels, and "
                "what it does not claim. Clearly labeled Signature-made, "
                "never presented as authentic public record.")
    pub_line = ("Public records - 34 real, fact-checked unsolved problems "
                "of genetics, from what non-coding DNA does and missing "
                "heritability through the genotype-phenotype map, "
                "gene-environment interplay, epigenetic inheritance, the "
                "evolution of sex, and the origin of the genetic code. "
                "Every record carries the problem, its background, why it "
                "matters, and a pointer to the Signature proposed "
                "solution, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what non-coding DNA does, gene counts, genome size, the "
              "human-mouse puzzle, missing heritability, reading traits "
              "from DNA, genes meeting environment, sibling differences, "
              "persistent harmful mutations, paternal age, mutation-rate "
              "variation) -> Compounded (epigenetic inheritance, why sex "
              "exists, Lewontins paradox of variation, balancing selection, "
              "canalization, pleiotropy, regulatory networks, the splicing "
              "code, non-coding RNA dark matter, protein function, "
              "mito-nuclear coordination, telomeres) -> Advanced "
              "(chromosome numbers, horizontal transfer, behavior "
              "genetics, the omnigenic model, polygenic portability, "
              "genetic nurture, domestication, the minimal genome, genetic "
              "load, the code's origin, the RNA world).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": ("%s - %s Every record carries the full entry: problem, "
                   "background, why it matters, the Signature proposed "
                   "solution (labeled as proposed, never established "
                   "science), citations, and a working solution-explorer "
                   "demonstration program.%s"
                   % (tagline, sig_line if source == "signature" else pub_line,
                      ladder)),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search junk DNA, heritability, genotype-phenotype, epigenetics, mutation, selection, splicing, telomeres, genetic code, RNA world...",
        "chat_ph": "Ask about unsolved genetics problems...",
        "archive_blurb": ("Seeded %s unsolved genetics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, problem, background, "
                   "why_it_matters, signature_solution, citations, src, "
                   "ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved genetics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about the great unsolved problems of genetics - from non-coding DNA, gene counts, and genome size through heritability, prediction, environment, and mutation to regulation, evolution, and the origin of the genetic code itself. I answer honestly: the problems are open in established science, and the Signature approaches are proposed paths, labeled as such." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-genetics-study", "gen_demo_kind": "unsolved-genetics-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["unsolved-genetics"] = _cfg(
    "unsolved-genetics", "The Unsolved Genetics Database",
    "Thirty-four real unsolved problems of genetics - what the non-coding "
    "genome does, missing heritability, the genotype-phenotype map, "
    "gene-environment interplay, epigenetic inheritance, the evolution of "
    "sex, the origin of the genetic code - each fact-checked, each taught "
    "progressively along the ladder, each pointing to the Signature "
    "proposed solution.",
    "unsolved problem record", "JAH-USGE-", "JAH Unsolved Genetics Archivist",
    "unsolved genetics archivist - the great open problems of genetics, "
    "fact-checked and taught progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles "
    "- definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system; honest about what is open "
    "and what is proposed",
    "public")
DBCFG["unsolved-genetics-signature"] = _cfg(
    "unsolved-genetics-signature", "The Unsolved Genetics Signature Database",
    "His original Signature Genetics Method on the same thirty-four "
    "unsolved problems: every solution opens with the exact label "
    "Signature-generated proposed solution - not established science, and "
    "carries assumptions, reasoning path, confirm/refute panels, and what "
    "it does not claim. Clearly labeled Signature-made, never presented "
    "as authentic public record.",
    "unsolved problem record", "JAH-USGES-",
    "JAH Unsolved Genetics Archivist (Signature)",
    "unsolved genetics archivist - Signature editions: his original "
    "Signature Genetics Method, every unsolved problem approached as a "
    "covenant of evidence, mechanism, and testable prediction, clearly "
    "labeled Signature-made and never presented as established science; "
    "teaches progressively along the ladder; answers from many angles "
    "using only archive data from this system",
    "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def _signature_solution_full(e):
    parts = [HONEST_LABEL, ""]
    parts.append("The Signature approach, step by step:")
    for i, s in enumerate(e["sig_steps"], 1):
        parts.append("%d. %s" % (i, s))
    parts.append("")
    parts.append("Assumptions: " + "; ".join(
        "%s = %s" % (k, v) for k, v in e["sig_assumptions"].items()) + ".")
    parts.append("")
    parts.append("What would confirm this approach: " +
                 " ".join(e["sig_confirm"]))
    parts.append("")
    parts.append("What would refute or kill it: " + " ".join(e["sig_refute"]))
    parts.append("")
    parts.append("Scope - what this does not claim: " + e["sig_scope"])
    return "\n".join(parts)


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
            description = ("Signature original interpretation. " + SIG_LENS +
                           " " + e["description"])
            citations = list(e["citations"]) + [SIG_TAIL]
            signature_solution = _signature_solution_full(e)
        else:
            description = e["description"]
            citations = list(e["citations"])
            signature_solution = HONEST_LABEL + " " + e["sig_pointer"]
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "problem": e["problem"],
            "background": e["background"],
            "why_it_matters": e["why_it_matters"],
            "signature_solution": signature_solution,
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          [], "")
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Solution-explorer walkthrough: working demonstration program (real, runnable Python)."}
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
    for slug in ("unsolved-genetics", "unsolved-genetics-signature"):
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
                      "citations", "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert r["signature_solution"].startswith(HONEST_LABEL), \
                "honesty label missing at open in %s" % r["id"]
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
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # Fragment for the merger (manifest/api/restamp handled by merger).
    base_url = SHARD_BASE + "/data"
    frag = {
        "public": {
            "slug": "unsolved-genetics",
            "name": "The Unsolved Genetics Database",
            "tagline": DBCFG["unsolved-genetics"]["tagline"],
            "record_kind": "unsolved problem record",
            "id_prefix": "JAH-USGE-",
            "ai_name": "JAH Unsolved Genetics Archivist",
            "local_index": base_url + "/unsolved-genetics/index.jsonl.gz",
            "record_count": 34,
            "status": "built",
            "full_records": 34,
            "index": base_url + "/unsolved-genetics/index.jsonl.gz",
            "chunk_pattern": "data/unsolved-genetics/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "unsolved-genetics-signature",
            "name": "The Unsolved Genetics Signature Database",
            "tagline": DBCFG["unsolved-genetics-signature"]["tagline"],
            "record_kind": "unsolved problem record",
            "id_prefix": "JAH-USGES-",
            "ai_name": "JAH Unsolved Genetics Archivist (Signature)",
            "local_index": base_url + "/unsolved-genetics-signature/index.jsonl.gz",
            "record_count": 34,
            "status": "built",
            "full_records": 34,
            "index": base_url + "/unsolved-genetics-signature/index.jsonl.gz",
            "chunk_pattern": "data/unsolved-genetics-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    fpath = "/home/hatch/workspace/hidden_files/missing-builds/fragments/unsolved-genetics.json"
    os.makedirs(os.path.dirname(fpath), exist_ok=True)
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
    print("fragment: %s" % fpath)
    print("DONE: 68 records built. manifest/api/restamp/commit left to merger.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
