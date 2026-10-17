#!/usr/bin/env python3
"""Build the English to English databases for JAH Databases
(Manon's language orders #10-11, 2026-10-17, roster rank 3).

Creates two NEW databases, 34 ladder-ordered records each:

  language-english            - The English to English Database
                                (public-harvest: real, fact-checked English
                                pedagogy for non-native learners - the full
                                34-record ladder: overview, writing system,
                                phonology, core vocabulary with sentences,
                                grammar essentials, themed sentence sets,
                                tenses, questions, commands, descriptions,
                                stories, idioms, registers, complex
                                sentences, conversations, mastery review)
  language-english-signature  - The English to English Signature Database
                                (his original Signature learner's method:
                                the same ladder through the Signature lens -
                                alphabet as raw stock, verbs as engines,
                                grammar as the frame, idioms as shop
                                shorthand; src signature, titles suffixed
                                " (Signature Edition)", clearly labeled
                                Signature-made, never presented as authentic
                                public record)

34 records each, ladder_rank 1-10 non-decreasing, tiers
foundations/compounded/advanced; the shard index is written in ladder order
so pages present simple -> compounded -> complex.

ID prefixes: JAH-LENG- (public) and JAH-LENGS- (signature), verified free
in the manifest (2410 databases) and in every shard index file (zero hits).

Demos: 13 archetypes (ref, phonics, vocab, grammar, numbers, phrases,
sentences, story, idioms, registers, qa, dialogue, mastery), all
hand-computed 2026-10-17 and machine-verified. Every demo prints real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.

This builder NEVER touches data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md, and never commits or pushes. A merger
handles those. It also writes the merger fragment JSON.
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
FRAG_DIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(SHARD, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
import entries_language_english as e1
import entries_part2  # noqa: F401  (extends ENTRIES)
import entries_part3  # noqa: F401  (extends ENTRIES)
from entries_language_english import ENTRIES, SIG_TAIL
from demos_language_english import KINDS

DEMOS = {}
for _e in ENTRIES:
    assert _e["demo_kind"] in KINDS, "unknown demo kind %s" % _e["demo_kind"]
    DEMOS[_e["key"]] = (lambda hdr, name, rid, group, points, req, e=_e:
                        KINDS[e["demo_kind"]](hdr, name, rid, group, points,
                                             req, e["demo_data"]))

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature learner's "
                "method: the alphabet as raw stock, verbs as engines, "
                "grammar as the frame of the workshop, idioms as shop "
                "shorthand, stories as finished pieces. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked English pedagogy for "
                "non-native learners: the alphabet, the 44 sounds, core "
                "vocabulary with full example sentences, grammar "
                "essentials, themed sentence sets for daily life, verb "
                "tenses, questions and answers, commands, descriptions, "
                "stories, idioms and proverbs, formal registers, complex "
                "sentences, full conversations, and a mastery review - "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, the writing system, pronunciation and "
              "phonology, core nouns, core verbs, adjectives and adverbs, "
              "pronouns, numbers and time, greetings and everyday phrases, "
              "grammar essentials) -> Compounded (home and family, food "
              "and cooking, travel and directions, work and school, health "
              "and body, emotions and feelings, nature and weather, "
              "shopping and money, friendship and social life, technology "
              "and communication, verb tenses) -> Advanced (questions and "
              "answers, commands and requests, descriptions, three short "
              "stories, idioms and proverbs, formal and polite registers, "
              "compound and complex sentences, three conversations, "
              "mastery review and full reference).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search alphabet, pronunciation, nouns, verbs, adjectives, pronouns, numbers, greetings, grammar, tenses, idioms, stories, conversations...",
        "chat_ph": "Ask about learning English...",
        "archive_blurb": ("Seeded %s English-learning records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled English learning studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about learning English - the alphabet, pronunciation, vocabulary, grammar, tenses, idioms, stories, and conversations - from first letters to fluent sentences." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "english-lesson", "gen_demo_kind": "english-demo",
        "source": source,
    }

CIT_PUB = ("English pedagogy (standard references: Swan M. Practical English "
           "Usage. 4th ed. Oxford University Press; 2016; Huddleston R, "
           "Pullum GK. The Cambridge Grammar of the English Language. "
           "Cambridge University Press; 2002; Roach P. English Phonetics and "
           "Phonology. 4th ed. Cambridge University Press; 2009; "
           "International Phonetic Association. Handbook of the IPA. 1999; "
           "Council of Europe. CEFR Companion Volume. 2020; Cambridge "
           "English vocabulary and graded-reading guidance; Merriam-Webster "
           "dictionary and style guidance; ISO 639 language codes).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "learner's method - the alphabet as raw stock, verbs "
                     "as engines, grammar as the frame - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["language-english"] = _cfg(
    "language-english", "The English to English Database",
    "Learn English in English itself: the alphabet, the 44 sounds, core "
    "vocabulary with full example sentences, grammar essentials, themed "
    "sentence sets for daily life, tenses, idioms, stories, and full "
    "conversations - a complete 34-lesson ladder from first letters to "
    "fluent sentences, every lesson with real drills and working "
    "demonstration programs.",
    "language learning record", "JAH-LENG-", "JAH English to English Archivist",
    "english to english archivist - teaching English to learners through "
    "the full ladder: alphabet, sounds, core vocabulary with sentences, "
    "grammar essentials, themed sentence sets, tenses, questions, idioms, "
    "registers, stories, and conversations; answers from many angles - "
    "definition, example, analogy, application, how-to - using only archive "
    "data from this system",
    CIT_PUB, "public")
DBCFG["language-english-signature"] = _cfg(
    "language-english-signature", "The English to English Signature Database",
    "His original Signature learner's method: the same 34-lesson ladder "
    "through the Signature lens - the alphabet as raw stock, verbs as "
    "engines, grammar as the frame of the workshop, idioms as shop "
    "shorthand, stories as finished pieces, conversations as field jobs. "
    "Clearly labeled Signature-made, never presented as authentic public "
    "record.",
    "language learning record", "JAH-LENGS-", "JAH English to English Archivist (Signature)",
    "english to english archivist - Signature editions: his original "
    "Signature learner method, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, how-to - "
    "using only archive data from this system",
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


def write_fragment(built):
    os.makedirs(FRAG_DIR, exist_ok=True)
    def side(slug, source):
        cfg = DBCFG[slug]
        loc = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        ai = cfg["ai"]
        if source == "signature":
            name = "The English to English Signature Database"
        else:
            name = "The English to English Database"
        return {
            "slug": slug, "name": name,
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": ai,
            "local_index": loc,
            "record_count": len(built[slug]),
            "status": "live",
            "full_records": len(built[slug]),
            "index": loc,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if source == "signature" else "public-harvest",
        }
    frag = {"public": side("language-english", "public"),
            "signature": side("language-english-signature", "signature")}
    path = os.path.join(FRAG_DIR, "language-english.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % path, flush=True)
    return path


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
    for slug in ("language-english", "language-english-signature"):
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
        assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    write_fragment(built)

    # manifest/api.json updates, restamp, commit, and push belong to the merger.
    print("built %d databases, %d records; manifest/api untouched (merger's job)" % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
