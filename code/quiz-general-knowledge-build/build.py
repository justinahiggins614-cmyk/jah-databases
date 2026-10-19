#!/usr/bin/env python3
"""Build the General Knowledge Quiz databases for JAH Databases
(Manon's 2026-10-17 16:15 order: test then quiz databases with answers at
bottom).

Verified 2026-10-17: manifest scan (2,410 databases) shows zero 'quiz*'
slugs and zero 'JAH-QZ*' id_prefix values; a full grep over every shard index
in jah-databases-data-1/data/ returned zero hits for 'JAH-QZGK'. The paste's
rule was applied by name/purpose/record schema/capabilities: a quiz database
where EVERY record is one complete 10-question quiz with the answers at the
bottom is a distinct capability - BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  quiz-general-knowledge            - The General Knowledge Quiz Database
                                      (public-harvest: real, fact-checked
                                      general-knowledge quizzes - every
                                      record one complete 10-question quiz
                                      with the answers at the bottom)
  quiz-general-knowledge-signature  - The General Knowledge Quiz Signature
                                      Database
                                      (his original Signature Quiz Method:
                                      the same teaching ladder reframed as
                                      Signature science; src signature,
                                      titles suffixed " (Signature
                                      Edition)", clearly labeled
                                      Signature-made, never presented as
                                      authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-QZGK- (public) and JAH-QZGKS- (signature), verified free
in the manifest and in every shard index (zero hits).

Numerical cores: the quiz-runner demos are machine-executed by this build -
all 68 must print real computed scores, assert tight bounds (never float
exact-equality), reveal the answers, and end with the OK marker; every demo
answer is cross-checked against the record text.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER git commits or
pushes. A merger handles those. It ONLY writes: db/quiz-general-knowledge/
+ db/quiz-general-knowledge-signature/ (index.html + gen-*.js each),
code/quiz-general-knowledge-build/*, the shard data dirs, and the fragment
file.
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

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_quiz_general_knowledge import ENTRIES, SIG_TAIL, RUBRIC
from demos_quiz_general_knowledge import DEMOS, DEMOS_SIG

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Quiz Method: "
                "the same teaching ladder from easy warm-ups through "
                "compounded trials to the grand final, reframed as Signature "
                "science - every quiz a covenant between the quizmaster and "
                "the taker, every answer a sealed verdict revealed at the "
                "bottom, every ladder rank a rung of his own design. Clearly "
                "labeled Signature-made, never presented as authentic public "
                "record.")
    pub_line = ("Public records - real, fact-checked general-knowledge "
                "quizzes: world capitals, animals, colors shapes and "
                "numbers, days months and seasons, arithmetic, famous "
                "landmarks, food and fruit, the human body, sports, music, "
                "continents and oceans, space, history, everyday science, "
                "riddles and wordplay, literature, rivers mountains and "
                "deserts, inventions, flags, the living world, art, logic "
                "puzzles, math word problems, chemistry and physics, "
                "geography, wordplay masters, quotes, technology, lateral "
                "thinking, deep science - every record one complete "
                "10-question quiz with the answers at the bottom, organized "
                "in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(easy world capitals, animal basics, colors shapes and "
              "numbers, days months and seasons, easy arithmetic, famous "
              "landmarks, food and fruit, human body basics, sports basics, "
              "music basics, continents and oceans, space basics, capitals "
              "challenge, history milestones, everyday science, starter "
              "riddles) -> Compounded (literature basics, rivers mountains "
              "and deserts, inventions and inventors, flags and nations, the "
              "living world, art and artists, logic puzzles, math word "
              "problems, history dates and events, chemistry and physics) -> "
              "Advanced (geography challenge, wordplay masters, literature "
              "quotes, technology and computers, advanced general knowledge, "
              "lateral thinking masters, deep science, the ultimate final).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full quiz: the ten questions, "
                  "how to take it, the scoring standard, citations, the answers "
                  "at the bottom, and a working quiz-runner demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search capitals, animals, arithmetic, landmarks, history, science, riddles, literature, inventions, flags, art, logic puzzles, wordplay, technology, quizzes...",
        "chat_ph": "Ask about any quiz topic or test yourself...",
        "archive_blurb": ("Seeded %s general-knowledge quiz records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced. "
                          "Every record is one complete 10-question quiz with the answers at the bottom."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled general-knowledge quizzes with answers at the bottom. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about any quiz in the archive, test yourself on capitals, animals, arithmetic, landmarks, history, science, riddles, literature, inventions, flags, art, logic, wordplay or technology, or climb the ladder from foundations through compounded to advanced." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "general-knowledge-quiz", "gen_demo_kind": "quiz-runner-demo",
        "source": source,
    }

CIT_PUB = ("General-knowledge reference (standard encyclopedic sources: "
           "Encyclopaedia Britannica; National Geographic Society; NASA; "
           "United States Geological Survey; International Olympic "
           "Committee; FIFA; NIST physical constants; IUPAC chemical data).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Quiz "
                     "Method - the same teaching ladder reframed as "
                     "Signature science - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["quiz-general-knowledge"] = _cfg(
    "quiz-general-knowledge", "The General Knowledge Quiz Database",
    "Test yourself: real, fact-checked general-knowledge quizzes, every "
    "record one complete 10-question quiz with the answers at the bottom, "
    "taught progressively along the ladder from easy warm-ups through "
    "compounded trials to the ultimate final.",
    "quiz record", "JAH-QZGK-", "JAH General Knowledge Quizmaster",
    "general knowledge quizmaster - running complete 10-question quizzes "
    "with the answers at the bottom across capitals, animals, arithmetic, "
    "landmarks, history, science, riddles, literature, inventions, flags, "
    "art, logic, wordplay and technology; teaching progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["quiz-general-knowledge-signature"] = _cfg(
    "quiz-general-knowledge-signature", "The General Knowledge Quiz Signature Database",
    "His original Signature Quiz Method: the same teaching ladder from easy "
    "warm-ups through compounded trials to the grand final, reframed as "
    "Signature science - every quiz a covenant between the quizmaster and "
    "the taker, every answer a sealed verdict revealed at the bottom. "
    "Clearly labeled Signature-made, never presented as authentic public "
    "record.",
    "quiz record", "JAH-QZGKS-", "JAH General Knowledge Quizmaster (Signature)",
    "general knowledge quizmaster - Signature editions: his original "
    "Signature Quiz Method, the same ladder reframed as Signature science, "
    "clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "public demo map misses entries"
assert set(DEMOS_SIG) == {e["key"] for e in ENTRIES}, "signature demo map misses entries"


def quiz_block(intro, qa):
    lines = [intro, "", "THE 10 QUESTIONS"]
    for i, (q, a) in enumerate(qa, 1):
        lines.append("%d. %s" % (i, q))
    lines += ["", "ANSWERS - AT THE BOTTOM"]
    for i, (q, a) in enumerate(qa, 1):
        lines.append("%d. %s" % (i, a))
    return "\n".join(lines)


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    demos = DEMOS_SIG if sig else DEMOS
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        qa = e["qa_sig"] if sig else e["qa"]
        if sig:
            description = ("Signature original interpretation. " + e["intro_sig"] + " "
                           + quiz_block(e["intro"], qa))
            how = (e["intro_sig"] + " How this quiz works: read all ten questions, "
                   "answer each from memory, then check the sealed verdicts at the "
                   "bottom. " + RUBRIC)
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = quiz_block(e["intro"], qa)
            how = ("How this quiz works: read all ten questions, answer each from "
                   "memory, then check the sealed verdicts at the bottom. " + RUBRIC)
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": ["Answer %d: %s" % (i + 1, a) for i, (q, a) in enumerate(qa)],
            "requirements": [
                "Read all ten questions before looking at the answers.",
                "Answer each question from memory, in order.",
                "Score one point per correct answer; the answers are at the bottom of the record.",
                "Spelling close enough to recognize counts as correct.",
            ],
            "standards": [
                RUBRIC,
                "Quiz standard: every record carries exactly ten questions and ten answers.",
                "Answer standard: answers are sealed at the bottom of the record, never beside the questions.",
            ],
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = demos[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          rec["key_points"], "; ".join(rec["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working quiz-runner demonstration program (real, runnable Python)."}
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
    for slug in ("quiz-general-knowledge", "quiz-general-knowledge-signature"):
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
            assert "ANSWERS - AT THE BOTTOM" in r["description"], "answers not at bottom in %s" % r["id"]
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
        sig = slug.endswith("-signature")
        for r, e in zip(recs, sorted(ENTRIES, key=lambda x: (x["ladder_rank"], ENTRIES.index(x)))):
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
            qa = e["qa_sig"] if sig else e["qa"]
            revealed = [l.split(": ", 1)[1] for l in p.stdout.splitlines()
                        if re.match(r"^A\d+: ", l)]
            assert revealed == [a for _, a in qa], \
                "demo answers != entry answers for %s" % r["id"]
    print("demo execution: all %d demos ran OK, answers cross-checked vs entry text" % total, flush=True)

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
        assert "component and parts" not in page.lower(), "field leftover in %s" % slug
        assert "component-parts-catalog" not in page, "slug leftover in %s" % slug
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
        assert "synthetic intelligence" not in gen_js.lower(), "template leftover in gen js %s" % slug
        assert "component and parts" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # NOTE: manifest.json, api.json, index.html, README.md, docs/AI_ACCESS.md
    # are owned by the merger - this build never touches them, and never
    # commits or pushes.
    print("records: %d public + %d signature = %d total" %
          (len(built["quiz-general-knowledge"]),
           len(built["quiz-general-knowledge-signature"]), total))
    print("NEXT: merger runs restamp + commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
