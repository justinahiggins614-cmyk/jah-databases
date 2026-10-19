#!/usr/bin/env python3
"""Build the Marathi Language databases for JAH Databases
(2026-10-17 language project, batch 2, ranks 11-20).

Pipeline replicates code/component-parts-catalog-build/build.py EXACTLY
for page structure and pipeline (same base builders, same sweep, same
dedupe gate, same shard layout, same page/gen-js flow).

Verified 2026-10-17: RAW SWEEP of the full manifest (2,410 databases)
PLUS every shard index title in jah-databases-data-1 (825 index files):
zero 'language-marathi*' slugs/names; zero 'marathi language' title
collisions. ID prefixes JAH-LMAR- (public) and JAH-LMARS- (signature)
verified free in manifest id_prefix values and in every shard index file
(zero hits).

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-marathi              - Marathi Language Database
                                  (public-harvest: real, fact-checked Marathi
                                  linguistic data - मराठी, Indo-European >
                                  Indo-Iranian > Indo-Aryan, ISO 639-1 mr,
                                  ISO 639-3 mar - every record carrying
                                  Marathi script + transliteration + English
                                  + example sentences; standard references
                                  Dhongde & Wali 2009, Masica 1991,
                                  Molesworth 1857; ISO 639; Unicode
                                  Devanagari block)
  language-marathi-signature    - Marathi Language Signature Database
                                  (his original Signature language
                                  instrument: Marathi re-taught as a working
                                  system he commands; src signature, titles
                                  suffixed " (Signature Edition)", clearly
                                  labeled Signature-made, never presented as
                                  authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10
non-decreasing, ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_marathi.py): pronunciation drills, script
quizzes, flashcard checks, conjugation tables, agreement checks, quiz
scoring. Every demo prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker; the build
machine-executes all 68 demos.

Per concurrency rules: this build NEVER touches data/manifest.json,
api.json, index.html, README.md, or docs/AI_ACCESS.md, and NEVER commits
or pushes. A merger handles those. It only creates db/language-marathi[/-signature]/,
code/language-marathi-build/, the data-1 shards, and the fragment file.

Never the words "bat belt" anywhere. No website references. No Facebook.
Screened 2026-10-17: nothing hate-adjacent, profane, or inappropriate;
no religious talk.
"""
import importlib.util
import json
import os
import subprocess
import sys

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
from entries_language_marathi import ENTRIES, SIG_TAIL
from demos_language_marathi import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature language "
                "instrument: Marathi re-taught as a working system he "
                "commands, every speaker count a measure of the instrument's "
                "reach, every dialect another string he can play, every rule "
                "a control he operates. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Marathi linguistic data: "
                "मराठी, Indo-European > Indo-Iranian > Indo-Aryan, ISO 639-1 "
                "mr, ISO 639-3 mar, about 99 million native speakers, official "
                "language of Maharashtra - every record carrying Marathi "
                "script, transliteration, English translation, and example "
                "sentences, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system, pronunciation, core nouns, "
              "core verbs, adjectives and adverbs, pronouns, numbers and "
              "time, greetings, grammar essentials) -> Compounded (home and "
              "family, food and cooking, travel and directions, work and "
              "school, health and body, emotions and feelings, nature and "
              "weather, shopping and money, friendship and social life, "
              "technology and communication) -> Advanced (verb tenses, "
              "questions and answers, commands and requests, descriptions, "
              "three short stories, idioms and proverbs, formal registers, "
              "complex sentences, three conversations, mastery review).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Marathi alphabet, Devanagari, pronunciation, nouns, verbs, grammar, phrases, conversations, idioms...",
        "chat_ph": "Ask about the Marathi language...",
        "archive_blurb": ("Seeded %s Marathi language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Marathi language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Marathi - from the alphabet and sounds through nouns, verbs, grammar, and everyday phrases, to stories, idioms, conversations, and full mastery." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "marathi-language-study", "gen_demo_kind": "marathi-language-demo",
        "source": source,
    }

CIT_PUB = ("Marathi linguistics (standard references: Dhongde, R. V. & Wali, "
           "Kashi. Marathi. John Benjamins; 2009; Masica, Colin P. The "
           "Indo-Aryan Languages. Cambridge University Press; 1991; "
           "Molesworth, J. T. A Dictionary, Marathi and English. 2nd ed. "
           "Bombay Education Society; 1857; ISO 639-1:2002 code 'mr'; ISO "
           "639-3:2007 code 'mar'; Unicode Standard, Devanagari block "
           "U+0900-U+097F).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "language instrument - Marathi re-taught as a working "
                     "system he commands - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["language-marathi"] = _cfg(
    "language-marathi", "Marathi Language Database",
    "Learn Marathi from zero to mastery: real, fact-checked Marathi "
    "linguistic data - Devanagari script, sounds, core vocabulary, grammar, "
    "everyday phrases, stories, idioms, and conversations - every record "
    "carrying Marathi script, transliteration, English translation, and "
    "example sentences, taught progressively along the ladder.",
    "language learning record", "JAH-LMAR-", "JAH Marathi Language Tutor",
    "Marathi language tutor - teaching Marathi from the alphabet and sounds "
    "through nouns, verbs, grammar, and everyday phrases, to stories, idioms, "
    "and conversations; teaching progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, how-to - using only "
    "archive data from this system",
    CIT_PUB, "public")
DBCFG["language-marathi-signature"] = _cfg(
    "language-marathi-signature", "Marathi Language Signature Database",
    "His original Signature language instrument: Marathi re-taught as a "
    "working system he commands - the full ladder from alphabet and sounds "
    "through vocabulary and grammar to stories, idioms, and conversations, "
    "reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "language learning record", "JAH-LMARS-", "JAH Marathi Language Tutor (Signature)",
    "Marathi language tutor - Signature editions: his original Signature "
    "language instrument, Marathi re-taught as a working system he commands, "
    "clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, how-to - using only archive data from "
    "this system",
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
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
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
    for slug in ("language-marathi", "language-marathi-signature"):
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
        assert "synthetic intelligence" not in gen_js.lower(), "template leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # NOTE: manifest.json / api.json / restamp / commit / push are handled by
    # the merger per concurrency rules - this build deliberately stops here.
    print("records built: %d databases, %d records; merger handles manifest/api/restamp/commit" % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
