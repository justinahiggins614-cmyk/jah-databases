#!/usr/bin/env python3
"""Build the Unsolved Philosophy databases for JAH Databases
(Manon's 2026-10-17 16:15 orders, Unsolved Problems Solved series batch 1).

Two NEW databases, 34 ladder-ordered records each:

  unsolved-philosophy            - The Unsolved Philosophy Database
  unsolved-philosophy-signature  - The Unsolved Philosophy Signature Database

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles registration. It only creates:
  db/unsolved-philosophy/ + db/unsolved-philosophy-signature/
  code/unsolved-philosophy-build/
  <shard-repo>/data/unsolved-philosophy[-signature]/
  ~/workspace/hidden_files/missing-builds/fragments/unsolved-philosophy.json

Page structure and pipeline replicate
code/component-parts-catalog-build/build.py exactly.
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
FRAG_DIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_unsolved_philosophy import ENTRIES, SIG_TAIL, SIG_LABEL
from demos_unsolved_philosophy import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Resolution "
                "Method applied to each problem: fix the problem in exact "
                "record form, enumerate the live candidate resolutions, "
                "score each by explanatory coverage, predictive grip, and "
                "internal consistency, stress the winner against its "
                "strongest objection, and publish the scorecard with the "
                "assumptions visible. Every solution labeled "
                "Signature-generated proposed solution, never presented as "
                "established positions.")
    pub_line = ("Public records - the field's real, famous, fact-checked "
                "unsolved problems: the meaning of life, the amoralist's "
                "challenge, skepticism, free will, personal identity, other "
                "minds, truth, the liar paradox, Zeno's paradoxes, the "
                "sorites paradox, beauty, art, justice, the state, the "
                "simulation hypothesis, the ethics of belief, induction, "
                "the is-ought gap, moral realism, moral luck, the Gettier "
                "problem, the Munchhausen trilemma, the mind-body problem, "
                "the hard problem of consciousness, the Chinese room, "
                "intentionality, perception, causation, time, Newcomb's "
                "problem, Sleeping Beauty, scientific realism, "
                "underdetermination, and Leibniz's question - every record "
                "carrying the problem, its background, why it matters, and "
                "a short pointer to the Signature solution, organized in "
                "the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(meaning of life, why be moral, skepticism, free will, the "
              "self, other minds, truth, the liar paradox, Zeno, the "
              "sorites, beauty) -> Compounded (art, justice, the state, "
              "the simulation hypothesis, the ethics of belief, induction, "
              "the is-ought gap, moral realism, moral luck, Gettier, the "
              "Munchhausen trilemma, the mind-body problem) -> Advanced "
              "(the hard problem of consciousness, the Chinese room, "
              "intentionality, perception, causation, time, Newcomb's "
              "problem, Sleeping Beauty, scientific realism, "
              "underdetermination, Leibniz's question).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": ("%s - %s Every record carries the full entry: problem, "
                   "background, why it matters, the Signature solution, "
                   "key points, requirements, standards, citations, and a "
                   "working solution-explorer demonstration program.%s"
                   % (tagline, sig_line if source == "signature" else pub_line, ladder)),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": ("Search meaning of life, free will, consciousness, truth, "
                       "justice, induction, time, the self, Newcomb, Sleeping Beauty, "
                       "simulation, moral luck, Gettier, causation..."),
        "chat_ph": "Ask about the unsolved problems of philosophy...",
        "archive_blurb": ("Seeded %s unsolved philosophy records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, problem, background, why_it_matters, "
                   "signature_solution, description, key_points, requirements, "
                   "standards, citations, src, branch, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved philosophy studies. Seeded archive records are the authoritative entries.",
        "greet": ("I am the %s. Ask me about the great unsolved problems of philosophy - "
                  "from the meaning of life, morality, skepticism, free will, and the self, "
                  "through truth, paradoxes, beauty, art, justice, and the state, to "
                  "consciousness, time, causation, decision, and the Signature proposed "
                  "solutions for each." % ai),
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-philosophy-study", "gen_demo_kind": "unsolved-philosophy-demo",
        "source": source,
    }

CIT_PUB = ("Unsolved problems of philosophy (standard references: Plato "
           "Republic c. 380 BCE; Aristotle Metaphysics and Nicomachean "
           "Ethics c. 350 BCE; Descartes Meditations 1641; Locke Essay 1689; "
           "Hume Treatise 1739-1740 and Enquiry 1748; Kant Critique of Pure "
           "Reason 1781; Mill Utilitarianism 1863; Frege 'On Sense and "
           "Reference' 1892; Russell 'On Denoting' 1905; Wittgenstein "
           "Tractatus 1921 and Philosophical Investigations 1953; Popper "
           "Logic of Scientific Discovery 1959; Quine 'Two Dogmas' 1951; "
           "Kuhn Structure of Scientific Revolutions 1962; Rawls A Theory "
           "of Justice 1971; Nozick Anarchy, State, and Utopia 1974; "
           "Parfit Reasons and Persons 1984; Nagel 'What Is It Like to Be "
           "a Bat?' 1974; Chalmers 'Facing Up to the Problem of "
           "Consciousness' 1995; Searle 'Minds, Brains, and Programs' 1980; "
           "Bostrom 'Are You Living in a Computer Simulation?' 2003; "
           "Gettier 'Is Justified True Belief Knowledge?' 1963; Stanford "
           "Encyclopedia of Philosophy).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Resolution Method applied to each problem - clearly "
                     "labeled Signature-made, every solution a labeled "
                     "proposal, never presented as established positions.")

DBCFG = {}
DBCFG["unsolved-philosophy"] = _cfg(
    "unsolved-philosophy", "The Unsolved Philosophy Database",
    "The great unsolved problems of philosophy - real, famous, "
    "fact-checked open problems across ethics, metaphysics, epistemology, "
    "philosophy of mind, logic, aesthetics, political philosophy, and "
    "philosophy of science - every record carrying the problem, its "
    "background, why it matters, and a pointer to the Signature proposed "
    "solution, taught progressively along the ladder.",
    "unsolved problem record", "JAH-USPL-", "JAH Unsolved Philosophy Archivist",
    "unsolved philosophy archivist - the great open problems of philosophy "
    "across ethics, metaphysics, epistemology, mind, logic, aesthetics, "
    "political philosophy, and philosophy of science; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from this "
    "system",
    CIT_PUB, "public")
DBCFG["unsolved-philosophy-signature"] = _cfg(
    "unsolved-philosophy-signature", "The Unsolved Philosophy Signature Database",
    "His original Signature Resolution Method applied to the great unsolved "
    "problems of philosophy: fix each problem in exact record form, "
    "enumerate the live candidate resolutions, score each by explanatory "
    "coverage, predictive grip, and consistency, stress the winner against "
    "its strongest objection, and publish the scorecard with the "
    "assumptions visible. Clearly labeled Signature-made, every solution a "
    "labeled proposal, never presented as established positions.",
    "unsolved problem record", "JAH-USPLS-", "JAH Unsolved Philosophy Archivist (Signature)",
    "unsolved philosophy archivist - Signature editions: his original "
    "Signature Resolution Method applied to each great open problem, "
    "clearly labeled Signature-made and never presented as established "
    "positions; teaches progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
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
            signature_solution = e["sig_full"]
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["problem"] + " " + e["background"] + " "
                           + e["why_it_matters"])
            how = signature_solution
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            signature_solution = SIG_LABEL + " " + e["sig_pointer"]
            description = e["problem"] + " " + e["background"] + " " + e["why_it_matters"]
            how = signature_solution
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "problem": e["problem"],
            "background": e["background"],
            "why_it_matters": e["why_it_matters"],
            "signature_solution": signature_solution,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "branch": e["branch"],
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working solution-explorer demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def node_check_scripts(page, gen_js, slug):
    blocks = []
    for m in re.finditer(r"<script([^>]*)>(.*?)</script>", page, re.S):
        attrs, body = m.group(1), m.group(2)
        if "src=" in attrs:
            continue
        if "ld+json" in attrs:
            continue
        if not body.strip():
            continue
        blocks.append(body)
    blocks.append(gen_js)
    for i, b in enumerate(blocks):
        p = os.path.join(HERE, ".check-%s-%d.js" % (slug, i))
        with open(p, "w", encoding="utf-8") as f:
            f.write(b)
        r = subprocess.run(["node", "--check", p], capture_output=True, text=True)
        assert r.returncode == 0, "node --check failed block %d of %s: %s" % (i, slug, r.stderr[-500:])
        os.remove(p)
    print("  node --check: %d script blocks clean for %s" % (len(blocks), slug), flush=True)


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
    for slug in ("unsolved-philosophy", "unsolved-philosophy-signature"):
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
            for k in ("id", "t", "g", "name", "title", "problem", "background",
                      "why_it_matters", "signature_solution", "description",
                      "how_it_works", "key_points", "requirements", "standards",
                      "citations", "src", "branch", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            assert r["signature_solution"].startswith(SIG_LABEL), "label missing in %s" % r["id"]
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
        assert "public-synthetic-intelligence" not in page, "slug leftover in %s" % slug
        assert "component parts" not in page.lower(), "field leftover in %s" % slug
        assert "component-parts" not in page, "slug leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["branch"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        node_check_scripts(page, gen_js, slug)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # fragment for the merger (registration data only; merger writes manifest/api)
    os.makedirs(FRAG_DIR, exist_ok=True)
    frag = {
        "public": {
            "slug": "unsolved-philosophy",
            "name": "The Unsolved Philosophy Database",
            "tagline": DBCFG["unsolved-philosophy"]["tagline"],
            "record_kind": "unsolved problem record",
            "id_prefix": "JAH-USPL-",
            "ai_name": "JAH Unsolved Philosophy Archivist",
            "local_index": SHARD_BASE + "/data/unsolved-philosophy/index.jsonl.gz",
            "record_count": 34,
            "status": "built-not-live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/unsolved-philosophy/index.jsonl.gz",
            "chunk_pattern": "data/unsolved-philosophy/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "unsolved-philosophy-signature",
            "name": "The Unsolved Philosophy Signature Database",
            "tagline": DBCFG["unsolved-philosophy-signature"]["tagline"],
            "record_kind": "unsolved problem record",
            "id_prefix": "JAH-USPLS-",
            "ai_name": "JAH Unsolved Philosophy Archivist (Signature)",
            "local_index": SHARD_BASE + "/data/unsolved-philosophy-signature/index.jsonl.gz",
            "record_count": 34,
            "status": "built-not-live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/unsolved-philosophy-signature/index.jsonl.gz",
            "chunk_pattern": "data/unsolved-philosophy-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    fpath = os.path.join(FRAG_DIR, "unsolved-philosophy.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fpath)
    print("built-not-live: merger must register manifest/api.json, restamp, commit, push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
