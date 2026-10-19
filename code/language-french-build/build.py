#!/usr/bin/env python3
"""Build the French Language databases for JAH Databases
(Manon's language order 2026-10-17, roster rank 19, batch 2).

Roster-verified: slug `language-french` free; id_prefixes JAH-LFRA-
(public) and JAH-LFRAS- (signature) verified free in manifest id_prefix
values and across every shard index file (zero hits) 2026-10-17.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-french              - The French Language Database
                                 (public-harvest: real, fact-checked French
                                 linguistics - francais, ISO 639-1 fr, ISO
                                 639-3 fra, Indo-European/Italic/Romance;
                                 alphabet, phonology, core vocabulary,
                                 grammar, 10 themed sentence sets, tenses,
                                 Q&A, commands, descriptions, 3 stories,
                                 idioms, registers, complex sentences,
                                 3 dialogues, mastery review)
  language-french-signature    - The French Language Signature Database
                                 (his original Signature Language Method:
                                 every word a signed instrument of meaning,
                                 every sentence signed by the learner -
                                 stamp the sound, seal the word, sign the
                                 sentence; src signature, titles suffixed
                                 " (Signature Edition)", never presented
                                 as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Numerical cores: all hand-set 2026-10-17, machine-verified by the demos
(see demos_language_french.py). Every demo prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker; the build machine-executes all 68 demos.

NOTE (concurrency): this build does NOT touch data/manifest.json,
api.json, index.html, README.md, or docs/AI_ACCESS.md, and does NOT
commit or push - the merger handles those. It writes only:
  db/language-french/ + db/language-french-signature/ (pages + gen JS)
  jah-databases-data-1/data/language-french[-signature]/ (shards)

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk.
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
from entries_language_french import ENTRIES_1, SIG_TAIL
from entries_language_french_part2 import ENTRIES_2
from demos_language_french import DEMOS

ENTRIES = ENTRIES_1 + ENTRIES_2

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Language "
                "Method: every word a signed instrument of meaning, every "
                "sentence signed by the learner. Stamp the sound, seal the "
                "word, sign the sentence. Clearly labeled Signature-made, "
                "never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked French linguistics: "
                "francais, ISO 639-1 fr, ISO 639-3 fra, Indo-European "
                "family, Italic branch, Romance group; the 26-letter Latin "
                "alphabet with five diacritics, twelve oral vowels and four "
                "nasal vowels, core nouns verbs adjectives and pronouns, "
                "numbers and time, greetings, grammar essentials, ten "
                "themed sentence sets, verb tenses, questions and answers, "
                "commands, descriptions, three stories, idioms, formal and "
                "polite registers, complex sentences, three dialogues, and "
                "a full mastery review - organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system, pronunciation, core "
              "nouns, core verbs, adjectives and adverbs, pronouns, numbers "
              "and time, greetings) -> Compounded (grammar essentials, ten "
              "themed sentence sets for home, food, travel, work, health, "
              "emotions, nature, shopping, friendship, technology, verb "
              "tenses, questions and answers, commands and requests) -> "
              "Advanced (descriptions, three stories, idioms and proverbs, "
              "formal and polite registers, compound and complex sentences, "
              "three dialogues, mastery review and full reference).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search French alphabet, pronunciation, nouns, verbs, adjectives, pronouns, numbers, time, greetings, grammar, tenses, idioms, dialogues, mastery review...",
        "chat_ph": "Ask about French...",
        "archive_blurb": ("Seeded %s French language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled French language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about French - the alphabet, pronunciation, nouns, verbs, adjectives, pronouns, numbers, greetings, grammar, tenses, idioms, dialogues, and the full mastery review." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "french-language-study", "gen_demo_kind": "french-language-demo",
        "source": source,
    }

CIT_PUB = ("French linguistics (standard references: Grevisse M, Goosse A. "
           "Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016; "
           "Academie francaise. Dictionnaire de l'Academie francaise, 9e "
           "edition, in progress; Organisation internationale de la "
           "Francophonie. La langue francaise dans le monde 2022. Gallimard; "
           "2022; Eberhard DM et al., eds. Ethnologue: Languages of the "
           "World. 28th ed. SIL International; 2025; Battye A, Hintze M-A, "
           "Rowlett P. The French Language Today. 2nd ed. Routledge; 2000; "
           "Tranel B. The Sounds of French. Cambridge University Press; "
           "1987; Price G. A Comprehensive French Grammar. 7th ed. "
           "Wiley-Blackwell; 2007; Fagyal Z, Kibbee D, Jenkins F. French: "
           "A Linguistic Introduction. Cambridge University Press; 2006).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Language Method - every word a signed instrument of "
                     "meaning, every sentence signed by the learner - "
                     "clearly labeled Signature-made.")

ROLE_PUB = ("french language tutor - teaching French from the alphabet and "
            "sounds through words, grammar, tenses, idioms, and conversation; "
            "teaching progressively along the ladder from foundations "
            "through compounded to advanced; answers from many angles - "
            "definition, example, analogy, application, history, how-to - "
            "using only archive data from this system")
ROLE_SIG = ("french language tutor - Signature editions: his original "
            "Signature Language Method, every word a signed instrument of "
            "meaning and every sentence signed by the learner, clearly "
            "labeled Signature-made and never presented as authentic public "
            "record; teaches progressively along the ladder from "
            "foundations through compounded to advanced; answers from many "
            "angles - definition, example, analogy, application, history, "
            "how-to - using only archive data from this system")

DBCFG = {}
DBCFG["language-french"] = _cfg(
    "language-french", "The French Language Database",
    "Learn French from the alphabet to full conversation: real, fact-checked "
    "French linguistics - francais, ISO fr/fra, Indo-European Romance - "
    "through pronunciation, core vocabulary, grammar, themed sentences, "
    "tenses, idioms, dialogues, and a full mastery review, taught "
    "progressively along the ladder.",
    "language learning record", "JAH-LFRA-", "JAH French Language Tutor",
    ROLE_PUB, CIT_PUB, "public")
DBCFG["language-french-signature"] = _cfg(
    "language-french-signature", "The French Language Signature Database",
    "His original Signature Language Method: every word a signed instrument "
    "of meaning, every sentence signed by the learner - stamp the sound, "
    "seal the word, sign the sentence. The full ladder from the alphabet "
    "through sounds, words, grammar, and tenses to stories, idioms, and "
    "conversation, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "language learning record", "JAH-LFRAS-", "JAH French Language Tutor (Signature)",
    ROLE_SIG, CIT_SIG, "signature")

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
    for slug in ("language-french", "language-french-signature"):
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
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    print("manifest/api.json/index.html/README/docs untouched (merger handles).")
    print("DONE: %d databases, %d records; merger verifies and goes live." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
