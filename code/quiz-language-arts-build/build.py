#!/usr/bin/env python3
"""Build the Language Arts Quiz databases for JAH Databases
(Manon's 2026-10-17 16:15 orders: "Test then quiz databases with answers at
bottom").

Verified 2026-10-17: RAW dedupe-gate sweep of all 68 titles (34 public + 34
" (Signature Edition)") against the whole system (data/dedupe/exact): zero
collisions, zero refusals. ID prefixes JAH-QZLA- (public) and JAH-QZLAS-
(signature) verified free in the manifest id_prefix values and in every
shard index file across jah-databases-data-1 (zero hits).

So this build creates two NEW databases, 34 ladder-ordered records each:

  quiz-language-arts             - The Language Arts Quiz Database
                                   (public-harvest: real, verified language
                                   arts quizzes - vocabulary, grammar,
                                   spelling and punctuation, literature,
                                   wordplay and puzzles, reading and
                                   rhetoric, poetry and prosody. EVERY record
                                   is one complete quiz of ten questions with
                                   the ANSWERS AT THE BOTTOM of the record,
                                   ladder-ordered easy -> medium -> hard.)
  quiz-language-arts-signature  - The Language Arts Quiz Signature Database
                                   (his original Signature Quizmaster Method:
                                   the same ladder through the Signature lens;
                                   src signature, titles suffixed " (Signature
                                   Edition)", never presented as authentic
                                   public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every demo is a real quiz runner (see demos_quiz_language_arts.py): it prints
the ten questions, grades a simulated run, prints the real computed score,
asserts tight bounds (never float exact-equality), prints the answer key at
the bottom, and ends with the OK marker. All 68 demos are machine-executed
here, and demo stdout is cross-checked against entry text (Q1 and A1 must
appear verbatim).

This build NEVER touches data/manifest.json, api.json, the hub index.html,
README.md, or docs/AI_ACCESS.md, and never commits or pushes - the merger
handles those.

Never the words "bat belt" anywhere. No website references. No Facebook.
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
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/quiz-language-arts.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_quiz_language_arts import ENTRIES, SIG_TAIL, HOW_TAKE, REQ
from demos_quiz_language_arts import DEMOS

# ---------------------------------------------------------------- DB config

GEN_FIELDS = ["Vocabulary", "Grammar", "Spelling and Punctuation",
              "Literature", "Wordplay and Puzzles", "Reading and Rhetoric",
              "Poetry and Prosody"]


def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Quizmaster "
                "Method: every question a trial of the tongue, every answer a "
                "sealed mark of mastery, the ladder the climb every mind must "
                "make, the same easy-to-hard ladder seen through the Signature "
                "lens. Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, verified language arts quizzes: "
                "vocabulary (synonyms, antonyms, prefixes, suffixes, confused "
                "words), grammar (parts of speech, sentences, agreement, "
                "tenses, modifiers, subjunctive), spelling and punctuation "
                "(spelling, plurals, apostrophes, commas), literature "
                "(childrens classics, literary terms, opening lines, American "
                "classics, Shakespeare, movements), wordplay and puzzles "
                "(anagrams, palindromes, riddles, cryptic wordplay), reading "
                "and rhetoric (figurative language, rhetorical devices, "
                "inference), poetry and prosody (forms, meter, sound devices) "
                "- every record one complete quiz of ten questions with the "
                "answers at the bottom, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(rungs 1-3: easy synonyms and antonyms, parts of speech, "
              "simple sentences, subject-verb agreement, prefixes, basic "
              "spelling, plurals, anagrams, figurative language) -> "
              "Compounded (rungs 4-7: confused words, suffixes, pronoun "
              "agreement, verb tenses, apostrophes, commas, tricky spellings, "
              "literary terms, opening lines, American classics, palindromes, "
              "riddles, cryptic wordplay, rhetorical devices, inference) -> "
              "Advanced (rungs 8-10: advanced and graduate vocabulary, "
              "dangling modifiers, subjunctive and parallelism, Shakespeare, "
              "literary movements, poetry forms, meter and sound devices).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record is one complete quiz: ten questions "
                  "with the answers at the bottom of the record, plus how to "
                  "take it, scoring guidance, standards, citations, and a "
                  "working quiz-runner demonstration program.%s"
                  % (tagline, sig_line if source == "signature" else pub_line,
                     ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search synonyms, antonyms, prefixes, grammar, spelling, punctuation, literature, Shakespeare, anagrams, riddles, figurative language, poetry, meter...",
        "chat_ph": "Ask about language arts quizzes...",
        "archive_blurb": ("Seeded %s language arts quiz records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced - "
                          "every quiz ten questions with the answers at the bottom of the record."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, quiz (10 questions + "
                   "answer key at the bottom), src, ladder_rank, ladder_tier, demo"),
        "fields": "Vocabulary \u00b7 Grammar \u00b7 Spelling and Punctuation \u00b7 Literature \u00b7 Wordplay and Puzzles \u00b7 Reading and Rhetoric \u00b7 Poetry and Prosody - each field opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled language arts quizzes. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about language arts quizzes - from easy synonyms, antonyms, parts of speech, simple sentences, and basic spelling, through prefixes, confused words, pronoun agreement, verb tenses, apostrophes, commas, literary terms, opening lines, anagrams, riddles, and rhetorical devices, to advanced vocabulary, subjunctive mood, Shakespeare, literary movements, poetry forms, and meter." % ai,
        "gen_fields": GEN_FIELDS,
        "gen_kind": "quiz-study", "gen_demo_kind": "quiz-runner",
        "source": source,
    }


CIT_PUB = ("Language arts standards (standard references: Merriam-Webster's "
           "Collegiate Dictionary, 11th ed., 2003; The Chicago Manual of "
           "Style, 18th ed., University of Chicago Press, 2024; Purdue "
           "University Online Writing Lab (OWL) grammar and punctuation "
           "guides; Common Core State Standards for English Language Arts; "
           "The Norton Anthology of English Literature, W. W. Norton; MLA "
           "Handbook, 9th ed., 2021; The Princeton Encyclopedia of Poetry "
           "and Poetics, 4th ed., Princeton University Press, 2012; Oxford "
           "English Dictionary, Oxford University Press).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Quizmaster Method - every question a trial of the "
                     "tongue, every answer a sealed mark of mastery - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["quiz-language-arts"] = _cfg(
    "quiz-language-arts", "The Language Arts Quiz Database",
    "Test yourself across the whole language arts: real, verified quizzes on "
    "vocabulary, grammar, spelling and punctuation, literature, wordplay and "
    "puzzles, reading and rhetoric, poetry and prosody - every record one "
    "complete quiz of ten questions with the answers at the bottom, "
    "ladder-ordered from easy to hard.",
    "quiz record", "JAH-QZLA-", "JAH Language Arts Quizmaster",
    "language arts quizmaster - vocabulary, grammar, spelling and punctuation, "
    "literature, wordplay and puzzles, reading and rhetoric, poetry and "
    "prosody; every quiz ten questions with the answers at the bottom of the "
    "record; teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
    CIT_PUB, "public")
DBCFG["quiz-language-arts-signature"] = _cfg(
    "quiz-language-arts-signature", "The Language Arts Quiz Signature Database",
    "His original Signature Quizmaster Method: every question a trial of the "
    "tongue, every answer a sealed mark of mastery, the ladder the climb "
    "every mind must make. The same easy-to-hard quiz ladder - vocabulary, "
    "grammar, spelling and punctuation, literature, wordplay, rhetoric, "
    "poetry - seen through the Signature lens, every quiz ten questions with "
    "the answers at the bottom. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "quiz record", "JAH-QZLAS-", "JAH Language Arts Quizmaster (Signature)",
    "language arts quizmaster - Signature editions: his original Signature "
    "Quizmaster Method, every question a trial of the tongue and every answer "
    "a sealed mark of mastery, clearly labeled Signature-made and never "
    "presented as authentic public record; every quiz ten questions with the "
    "answers at the bottom of the record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
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
        qlines = ["QUESTIONS - answer all ten, then check the key at the "
                  "bottom of this record."]
        for i, (q, _a, _x) in enumerate(e["qa"], 1):
            qlines.append("%d. %s" % (i, q))
        alines = ["ANSWERS - at the bottom of this record, as ordered. No "
                  "peeking until you finish the questions."]
        for i, (_q, a, x) in enumerate(e["qa"], 1):
            alines.append("Answer %d: %s - %s" % (i, a, x))
        description = e["intro"] + "\n\n" + "\n".join(qlines)
        if sig:
            description = ("Signature original interpretation. " + e["sig_lens"]
                           + " " + description)
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": HOW_TAKE,
            "key_points": alines,
            "requirements": list(REQ),
            "standards": list(e["standards"]),
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
                       "note": "Working quiz-runner demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def node_check(path, label):
    p = subprocess.run(["node", "--check", path], capture_output=True,
                       text=True, timeout=60)
    assert p.returncode == 0, "node --check failed for %s: %s" % (label, p.stderr[-800:])
    print("  node --check OK: %s" % label, flush=True)


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
    for slug in ("quiz-language-arts", "quiz-language-arts-signature"):
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
            assert len(r["key_points"]) == 11, "answer key must be header + 10 in %s" % r["id"]
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

    # machine-execute all demos + cross-check demo stdout vs entry text
    qa_by_name = {e["name"]: e["qa"] for e in ENTRIES}
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
            assert "ANSWER KEY" in p.stdout, "demo missing answer key %s" % r["id"]
            q1, a1 = qa_by_name[r["name"]][0][0], qa_by_name[r["name"]][0][1]
            assert q1 in p.stdout, "Q1 text drift in demo %s" % r["id"]
            assert a1 in p.stdout, "A1 text drift in demo %s" % r["id"]
    print("demo execution: all %d demos ran OK, stdout cross-checked vs entries" % total, flush=True)

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
        assert "mergePanel" in page, "mergePanel missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "Search synonyms, antonyms" in page, "field search placeholder missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "universal build" not in page.lower(), "field leftover in %s" % slug
        assert "universal-build" not in page, "slug leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        # apostrophe hygiene on JS-facing strings
        for k in ("ai", "role", "greet", "search_ph"):
            assert "'" not in DBCFG[slug][k], "apostrophe in %s of %s" % (k, slug)
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
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)
        # node --check on extracted inline page scripts + gen js
        blocks = re.findall(r"<script([^>]*)>(.*?)</script>", page, flags=re.S)
        for i, (attrs, s) in enumerate(blocks):
            if "src=" in attrs or "ld+json" in attrs:
                continue
            if not s.strip():
                continue
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
                tf.write(s)
                tpath = tf.name
            try:
                node_check(tpath, "%s inline script %d" % (slug, i))
            finally:
                os.unlink(tpath)
        node_check(gpath, "gen-%s.js" % slug)

    # fragment for the merger
    frag = {
        "public": {
            "slug": "quiz-language-arts",
            "name": "The Language Arts Quiz Database",
            "tagline": DBCFG["quiz-language-arts"]["tagline"],
            "record_kind": "quiz record",
            "id_prefix": "JAH-QZLA-",
            "ai_name": "JAH Language Arts Quizmaster",
            "local_index": SHARD_BASE + "/data/quiz-language-arts/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/quiz-language-arts/index.jsonl.gz",
            "chunk_pattern": "data/quiz-language-arts/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "quiz-language-arts-signature",
            "name": "The Language Arts Quiz Signature Database",
            "tagline": DBCFG["quiz-language-arts-signature"]["tagline"],
            "record_kind": "quiz record",
            "id_prefix": "JAH-QZLAS-",
            "ai_name": "JAH Language Arts Quizmaster (Signature)",
            "local_index": SHARD_BASE + "/data/quiz-language-arts-signature/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/quiz-language-arts-signature/index.jsonl.gz",
            "chunk_pattern": "data/quiz-language-arts-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)

    print("built %d databases, %d records; manifest/api/hub untouched (merger owns them)" % (len(built), total))
    print("DONE - do NOT claim live; the merger verifies.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
