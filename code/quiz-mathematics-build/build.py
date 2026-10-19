#!/usr/bin/env python3
"""Build the Mathematics Quiz databases for JAH Databases
(Manon 16:15 orders 2026-10-17: "Test then quiz databases with answers at
the bottom").

Verified 2026-10-17: RAW SWEEP over the full manifest (2,410 databases)
PLUS every shard index title in jah-databases-data-1: zero
'quiz-mathematics' slugs/names; zero title collisions for any of the 34
quiz titles or their 34 " (Signature Edition)" variants (dedupe_gate
pre-check: 68 titles, 0 refusals).

So this build creates two NEW databases, 34 ladder-ordered records each:

  quiz-mathematics              - The Mathematics Quiz Database
                                  (public-harvest: real, verified
                                  mathematics quizzes - arithmetic,
                                  algebra, geometry, logic puzzles,
                                  number patterns - every record one
                                  complete 10-question quiz with the
                                  ANSWERS AT THE BOTTOM of the record;
                                  every answer machine-recomputed from
                                  the question's own numbers on
                                  2026-10-17)
  quiz-mathematics-signature    - The Mathematics Quiz Signature Database
                                  (his original Signature Mathematics
                                  Method: every number a sworn mark,
                                  every operation a covenant, every proof
                                  a kept oath - the same ladder through
                                  the Signature lens; src signature,
                                  titles suffixed " (Signature Edition)",
                                  never presented as authentic public
                                  record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-QZMA- (public) and JAH-QZMAS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits).

Numerical cores: every answer recomputed by the demos from the question's
own numbers (see demos_quiz_mathematics.py) - tight-bounds asserts, never
float exact-equality; demos print the quiz, reveal the answers, print the
scoring bands, and end with the OK marker; the build machine-executes all
68 demos and cross-checks every answer string against the record text.

NOTE (concurrency): this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER commits or pushes -
the All Database Merger handles manifest/api/restamp/commit.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk.
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
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/quiz-mathematics.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_quiz_mathematics import ENTRIES, SIG_TAIL
from demos_quiz_mathematics import DEMOS, demo_quiz, demo_quiz_truth, demo_quiz_grid

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Mathematics "
                "Method: every number a sworn mark, every operation a "
                "covenant, every proof a kept oath, the quiz the proving "
                "ground. The same ladder - arithmetic, algebra, geometry, "
                "logic puzzles, number patterns - reframed as Signature "
                "science. Clearly labeled Signature-made, never presented "
                "as authentic public record.")
    pub_line = ("Public records - real, verified mathematics quizzes: "
                "arithmetic (addition, subtraction, multiplication, "
                "division, integers, percent, modular arithmetic, growth "
                "and interest), algebra (variables, one-step and two-step "
                "equations, plotting, systems, quadratics), geometry "
                "(shapes, perimeter, area, angles, circles, volume, "
                "Pythagoras), logic puzzles (riddles, truth-tellers, "
                "river crossings, logic grids, proofs), and number "
                "patterns (skip counting, Fibonacci, powers, sequences "
                "and series) - every record one complete 10-question quiz "
                "with the answers at the bottom, organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(skip counting, addition and subtraction, multiplication, "
              "reading shapes, division and remainders, order of "
              "operations, fractions, easy logic riddles, perimeter, what "
              "a variable is, one-step equations, decimals and fractions, "
              "area, even odd and prime spotting) -> Compounded "
              "(multi-step word problems, integer operations, two-step "
              "equations, angles and triangles, Fibonacci, percent, "
              "plotting points and lines, circles, powers and exponents, "
              "truth-teller puzzles, volume, river-crossing logic) -> "
              "Advanced (systems of two equations, modular arithmetic, "
              "Pythagorean theorem, quadratic roots, sequences and series "
              "sums, compound growth and interest, the logic grid "
              "challenge, proof puzzles).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record is one complete quiz: ten questions, "
                  "then the answers at the bottom of the record, plus a "
                  "working quiz-runner demonstration program that recomputes "
                  "every answer.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search addition, multiplication, fractions, equations, quadratics, geometry, perimeter, area, logic puzzles, truth-tellers, Fibonacci, primes, percent, exponents...",
        "chat_ph": "Ask about any mathematics quiz topic...",
        "archive_blurb": ("Seeded %s mathematics quiz records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced. "
                          "Every quiz carries its answers at the bottom of the record."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, questions, how_it_works, key_points, "
                   "requirements, standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled mathematics quiz studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about mathematics quizzes - from skip counting, addition, multiplication, shapes, division, order of operations, fractions, riddles, perimeter, variables, one-step equations, decimals, area, and primes, through word problems, integers, two-step equations, angles, Fibonacci, percent, plotting, circles, exponents, truth-tellers, volume, and river crossings, to systems of equations, modular arithmetic, Pythagoras, quadratics, sequences and series, compound growth, logic grids, and proofs." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "mathematics-quiz", "gen_demo_kind": "mathematics-quiz-demo",
        "source": source,
    }

CIT_PUB = ("Mathematics quiz standards (standard references: National "
           "Governors Association Center for Best Practices. Common Core "
           "State Standards for Mathematics. Washington DC; 2010; Polya G. "
           "How to Solve It. Princeton University Press; 1945; Euclid. The "
           "Thirteen Books of the Elements. Trans. Heath TL. 2nd ed. Dover; "
           "1956; Gardner M. Mathematical Puzzles and Diversions. Simon and "
           "Schuster; 1959; Smullyan RM. What Is the Name of This Book? "
           "Prentice-Hall; 1978; Devlin K. The Language of Mathematics. "
           "Henry Holt; 1998; Stewart I. Concepts of Modern Mathematics. "
           "Dover; 1995; Maor E. e: The Story of a Number. Princeton "
           "University Press; 1994). All answers machine-recomputed "
           "2026-10-17.")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Mathematics Method - every number a sworn mark, every "
                     "operation a covenant, every proof a kept oath - "
                     "clearly labeled Signature-made.")

DBCFG = {}
DBCFG["quiz-mathematics"] = _cfg(
    "quiz-mathematics", "The Mathematics Quiz Database",
    "Test yourself on real mathematics: 34 complete quizzes from skip "
    "counting to proofs - arithmetic, algebra, geometry, logic puzzles, "
    "and number patterns - every quiz ten questions with the answers at "
    "the bottom, every answer machine-verified, taught progressively "
    "along the ladder.",
    "mathematics quiz record", "JAH-QZMA-", "JAH Mathematics Quizmaster",
    "mathematics quizmaster - testing arithmetic, algebra, geometry, "
    "logic puzzles, and number patterns with complete ten-question "
    "quizzes whose answers sit at the bottom of each record; teaching "
    "progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive "
    "data from this system",
    CIT_PUB, "public")
DBCFG["quiz-mathematics-signature"] = _cfg(
    "quiz-mathematics-signature", "The Mathematics Quiz Signature Database",
    "His original Signature Mathematics Method as quizzes: every number "
    "a sworn mark, every operation a covenant, every proof a kept oath. "
    "The full ladder from skip counting through variables, equations, "
    "geometry, and logic to systems, quadratics, grids, and proofs, "
    "reframed as Signature science. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "mathematics quiz record", "JAH-QZMAS-", "JAH Mathematics Quizmaster (Signature)",
    "mathematics quizmaster - Signature editions: his original Signature "
    "Mathematics Method, every number a sworn mark and every operation a "
    "covenant, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder "
    "from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def _norm(s):
    return re.sub(r"\s+", " ", str(s)).strip().lower()


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
        qlines = ["%d. %s" % (i + 1, q["q"]) for i, q in enumerate(e["questions"])]
        alines = ["%d. %s" % (i + 1, q["a"]) for i, q in enumerate(e["questions"])]
        if sig:
            lead = ("Signature original interpretation. " + e["sig_intro"])
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            lead = e["intro"]
            citations = list(e["citations"])
        description = (lead + "\n\nQUESTIONS\n" + "\n".join(qlines) +
                       "\n\nANSWERS (at the bottom)\n" + "\n".join(alines))
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "questions": [{"q": q["q"], "a": q["a"]} for q in e["questions"]],
            "how_it_works": e["how"],
            "key_points": list(e["topics"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        if e["key"] == "qz_truth":
            demo_fn = demo_quiz_truth
        elif e["key"] == "qz_grid":
            demo_fn = demo_quiz_grid
        else:
            demo_fn = demo_quiz
        assert DEMOS[e["key"]] is demo_fn, "DEMOS map drift for %s" % e["key"]
        program = demo_fn(base._hdr, title, rid, e["group"], e)
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working quiz-runner demonstration program: prints the quiz, "
                               "reveals the answers, recomputes every answer from the "
                               "question's own numbers, prints the scoring bands."}
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
    for slug in ("quiz-mathematics", "quiz-mathematics-signature"):
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
            for k in ("id", "t", "g", "name", "title", "description", "questions",
                      "how_it_works", "key_points", "requirements", "standards",
                      "citations", "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            assert len(r["questions"]) == 10, "not 10 questions in %s" % r["id"]
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 500, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 10, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            # answers at the bottom: every answer string present in the record text
            blob = _norm(r["description"])
            for qi, qa in enumerate(r["questions"], 1):
                assert _norm(qa["a"]) in blob, \
                    "answer %d not in record text %s" % (qi, r["id"])
                assert _norm(qa["q"]) in blob, \
                    "question %d not in record text %s" % (qi, r["id"])
            assert "answers (at the bottom)" in blob, "answers not at bottom in %s" % r["id"]
            assert blob.rindex("answers (at the bottom)") > blob.rindex("questions"), \
                "answers section not after questions in %s" % r["id"]
            compile(prog, r["id"], "exec")
            raw = json.dumps(r).lower()
            assert "facebook" not in raw, "facebook ref in %s" % r["id"]
            assert "bat belt" not in raw, "banned phrase in %s" % r["id"]
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
            assert "10/10 answers verified" in p.stdout, "demo incomplete %s" % r["id"]
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

    # fragment for the All Database Merger (manifest/api/restamp handled by merger)
    frag = {
        "public": {
            "slug": "quiz-mathematics",
            "name": "The Mathematics Quiz Database",
            "tagline": DBCFG["quiz-mathematics"]["tagline"],
            "record_kind": "mathematics quiz record",
            "id_prefix": "JAH-QZMA-",
            "ai_name": "JAH Mathematics Quizmaster",
            "local_index": "https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/quiz-mathematics/index.jsonl.gz",
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": "https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/quiz-mathematics/index.jsonl.gz",
            "chunk_pattern": "data/quiz-mathematics/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "quiz-mathematics-signature",
            "name": "The Mathematics Quiz Signature Database",
            "tagline": DBCFG["quiz-mathematics-signature"]["tagline"],
            "record_kind": "mathematics quiz record",
            "id_prefix": "JAH-QZMAS-",
            "ai_name": "JAH Mathematics Quizmaster (Signature)",
            "local_index": "https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/quiz-mathematics-signature/index.jsonl.gz",
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": "https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/quiz-mathematics-signature/index.jsonl.gz",
            "chunk_pattern": "data/quiz-mathematics-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1)
        f.write("\n")
    print("fragment: %s" % FRAGMENT)
    print("manifest + api.json: LEFT FOR MERGER (not touched by this build).")
    print("NEXT: merger runs restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
