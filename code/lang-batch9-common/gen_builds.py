#!/usr/bin/env python3
"""Generate build.py + demos_language_<lang>.py for the 9 remaining batch-9
language pairs from the proven Serbian build. Run once; outputs are staged
in code/language-<lang>-build/.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join("/home/hatch/workspace/jah-databases", "code")

META = {
    "lithuanian": {
        "Lang": "Lithuanian", "PREFIX": "JAH-LLIT-", "PREFIXS": "JAH-LLITS-",
        "script_phrase": "the 32-letter Latin alphabet with diacritics",
        "script_short": "Latin script with diacritics plus English translation",
        "sig_flavor": ("every letter a sworn sign from the oldest living "
                       "Indo-European tongue, every case a living relation, "
                       "every proverb a covenant of the ancestors"),
        "pub_detail": ("the language overview, the 32-letter Latin writing "
                       "system, pronunciation and phonology, core nouns "
                       "verbs adjectives and adverbs with sentences, "
                       "pronouns, numbers and time, greetings, grammar "
                       "essentials, themed sentence sets for daily life, "
                       "verb tenses, questions and answers, commands and "
                       "requests, descriptions, stories, idioms, formal and "
                       "polite registers, complex sentences, conversations, "
                       "and a mastery review"),
        "role_detail": ("teaching Lithuanian from the 32-letter alphabet "
                        "and sounds through core vocabulary, grammar, and "
                        "everyday sentences to stories, idioms, registers, "
                        "and conversations"),
    },
    "catalan": {
        "Lang": "Catalan", "PREFIX": "JAH-LCAT-", "PREFIXS": "JAH-LCATS-",
        "script_phrase": "the Latin alphabet with ç, ny, and l·l",
        "script_short": "Latin script plus English translation",
        "sig_flavor": ("every letter a sworn sign of the Catalan lands, "
                       "every verb a living action, every proverb a "
                       "covenant of the ancestors"),
        "pub_detail": ("the language overview, the Latin writing system, "
                       "pronunciation and phonology, core nouns verbs "
                       "adjectives and adverbs with sentences, pronouns, "
                       "numbers and time, greetings, grammar essentials, "
                       "themed sentence sets for daily life, verb tenses, "
                       "questions and answers, commands and requests, "
                       "descriptions, stories, idioms, formal and polite "
                       "registers, complex sentences, conversations, and a "
                       "mastery review"),
        "role_detail": ("teaching Catalan from the alphabet and sounds "
                        "through core vocabulary, grammar, and everyday "
                        "sentences to stories, idioms, registers, and "
                        "conversations"),
    },
    "awadhi": {
        "Lang": "Awadhi", "PREFIX": "JAH-LAWA-", "PREFIXS": "JAH-LAWAS-",
        "script_phrase": "the Devanagari script",
        "script_short": "Devanagari script plus transliteration plus English translation",
        "sig_flavor": ("every letter a sworn sign of Awadh, every verb a "
                       "living action, every proverb a covenant of the "
                       "ancestors"),
        "pub_detail": ("the language overview, the Devanagari writing "
                       "system, pronunciation and phonology, core nouns "
                       "verbs adjectives and adverbs with sentences, "
                       "pronouns, numbers and time, greetings, grammar "
                       "essentials, themed sentence sets for daily life, "
                       "verb tenses, questions and answers, commands and "
                       "requests, descriptions, stories, idioms, formal and "
                       "polite registers, complex sentences, conversations, "
                       "and a mastery review"),
        "role_detail": ("teaching Awadhi from the Devanagari script and "
                        "sounds through core vocabulary, grammar, and "
                        "everyday sentences to stories, idioms, registers, "
                        "and conversations"),
    },
    "chhattisgarhi": {
        "Lang": "Chhattisgarhi", "PREFIX": "JAH-LHNE-", "PREFIXS": "JAH-LHNES-",
        "script_phrase": "the Devanagari script",
        "script_short": "Devanagari script plus transliteration plus English translation",
        "sig_flavor": ("every letter a sworn sign of Chhattisgarh, every "
                       "verb a living action, every proverb a covenant of "
                       "the ancestors"),
        "pub_detail": ("the language overview, the Devanagari writing "
                       "system, pronunciation and phonology, core nouns "
                       "verbs adjectives and adverbs with sentences, "
                       "pronouns, numbers and time, greetings, grammar "
                       "essentials, themed sentence sets for daily life, "
                       "verb tenses, questions and answers, commands and "
                       "requests, descriptions, stories, idioms, formal and "
                       "polite registers, complex sentences, conversations, "
                       "and a mastery review"),
        "role_detail": ("teaching Chhattisgarhi from the Devanagari script "
                        "and sounds through core vocabulary, grammar, and "
                        "everyday sentences to stories, idioms, registers, "
                        "and conversations"),
    },
    "magahi": {
        "Lang": "Magahi", "PREFIX": "JAH-LMAG-", "PREFIXS": "JAH-LMAGS-",
        "script_phrase": "the Devanagari script",
        "script_short": "Devanagari script plus transliteration plus English translation",
        "sig_flavor": ("every letter a sworn sign of ancient Magadha, "
                       "every verb a living action, every proverb a "
                       "covenant of the ancestors"),
        "pub_detail": ("the language overview, the Devanagari writing "
                       "system, pronunciation and phonology, core nouns "
                       "verbs adjectives and adverbs with sentences, "
                       "pronouns, numbers and time, greetings, grammar "
                       "essentials, themed sentence sets for daily life, "
                       "verb tenses, questions and answers, commands and "
                       "requests, descriptions, stories, idioms, formal and "
                       "polite registers, complex sentences, conversations, "
                       "and a mastery review"),
        "role_detail": ("teaching Magahi from the Devanagari script and "
                        "sounds through core vocabulary, grammar, and "
                        "everyday sentences to stories, idioms, registers, "
                        "and conversations"),
    },
    "maithili": {
        "Lang": "Maithili", "PREFIX": "JAH-LMAI-", "PREFIXS": "JAH-LMAIS-",
        "script_phrase": "the Devanagari script (Tirhuta historical)",
        "script_short": "Devanagari script plus transliteration plus English translation",
        "sig_flavor": ("every letter a sworn sign of Mithila, every verb a "
                       "living action, every proverb a covenant of the "
                       "ancestors"),
        "pub_detail": ("the language overview, the Devanagari writing "
                       "system, pronunciation and phonology, core nouns "
                       "verbs adjectives and adverbs with sentences, "
                       "pronouns, numbers and time, greetings, grammar "
                       "essentials, themed sentence sets for daily life, "
                       "verb tenses, questions and answers, commands and "
                       "requests, descriptions, stories, idioms, formal and "
                       "polite registers, complex sentences, conversations, "
                       "and a mastery review"),
        "role_detail": ("teaching Maithili from the Devanagari script and "
                        "sounds through core vocabulary, grammar, and "
                        "everyday sentences to stories, idioms, registers, "
                        "and conversations"),
    },
    "marwari": {
        "Lang": "Marwari", "PREFIX": "JAH-LMWR-", "PREFIXS": "JAH-LMWRS-",
        "script_phrase": "the Devanagari script",
        "script_short": "Devanagari script plus transliteration plus English translation",
        "sig_flavor": ("every letter a sworn sign of Marwar, every verb a "
                       "living action, every proverb a covenant of the "
                       "ancestors"),
        "pub_detail": ("the language overview, the Devanagari writing "
                       "system, pronunciation and phonology, core nouns "
                       "verbs adjectives and adverbs with sentences, "
                       "pronouns, numbers and time, greetings, grammar "
                       "essentials, themed sentence sets for daily life, "
                       "verb tenses, questions and answers, commands and "
                       "requests, descriptions, stories, idioms, formal and "
                       "polite registers, complex sentences, conversations, "
                       "and a mastery review"),
        "role_detail": ("teaching Marwari from the Devanagari script and "
                        "sounds through core vocabulary, grammar, and "
                        "everyday sentences to stories, idioms, registers, "
                        "and conversations"),
    },
    "saraiki": {
        "Lang": "Saraiki", "PREFIX": "JAH-LSKR-", "PREFIXS": "JAH-LSKRS-",
        "script_phrase": "the Shahmukhi Perso-Arabic script",
        "script_short": "Shahmukhi script plus transliteration plus English translation",
        "sig_flavor": ("every letter a sworn sign of southern Punjab, "
                       "every verb a living action, every proverb a "
                       "covenant of the ancestors"),
        "pub_detail": ("the language overview, the Shahmukhi Perso-Arabic "
                       "writing system, pronunciation and phonology, core "
                       "nouns verbs adjectives and adverbs with sentences, "
                       "pronouns, numbers and time, greetings, grammar "
                       "essentials, themed sentence sets for daily life, "
                       "verb tenses, questions and answers, commands and "
                       "requests, descriptions, stories, idioms, formal and "
                       "polite registers, complex sentences, conversations, "
                       "and a mastery review"),
        "role_detail": ("teaching Saraiki from the Shahmukhi script and "
                        "sounds through core vocabulary, grammar, and "
                        "everyday sentences to stories, idioms, registers, "
                        "and conversations"),
    },
    "fula": {
        "Lang": "Fula", "PREFIX": "JAH-LFUL-", "PREFIXS": "JAH-LFULS-",
        "script_phrase": "the Latin alphabet (Adlam and Ajami historical)",
        "script_short": "Latin script plus English translation",
        "sig_flavor": ("every noun class a sworn sign of the Sahel, every "
                       "verb a living action in three voices, every "
                       "proverb a covenant of the ancestors"),
        "pub_detail": ("the language overview, the Latin writing system, "
                       "pronunciation and phonology, the noun-class system, "
                       "core nouns verbs adjectives and adverbs with "
                       "sentences, pronouns, numbers and time, greetings, "
                       "grammar essentials, themed sentence sets for daily "
                       "life, verb tenses, questions and answers, commands "
                       "and requests, descriptions, stories, idioms, formal "
                       "and polite registers, complex sentences, "
                       "conversations, and a mastery review"),
        "role_detail": ("teaching Fula from the alphabet and sounds through "
                        "the noun-class system, core vocabulary, grammar, "
                        "and everyday sentences to stories, idioms, "
                        "registers, and conversations"),
    },
}

BUILD_TMPL = '''#!/usr/bin/env python3
"""Build the @@Lang@@ Language database pair for JAH Databases (batch 9).

Dedupe gate: '@@slug@@' zero hits across the full manifest; '@@PREFIX@@' /
'@@PREFIXS@@' verified free: zero hits in manifest id_prefix values and zero
hits in shard record IDs (checked with code/dedupe_gate.py BEFORE
authoring).

Two NEW databases, 34 ladder-ordered records each:
  @@slug_pub@@            - The @@Lang@@ Language Database (public-harvest)
  @@slug_sig@@  - The @@Lang@@ Language Signature Database
                                (signature)

34 records each, ladder-ordered 1-34 (foundations 1-10 / compounded 11-21 /
advanced 22-34).

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/@@slug_pub@@/index.html + gen-@@slug_pub@@.js
              db/@@slug_sig@@/index.html + gen-...js
  shard repo: data/@@slug_pub@@/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/@@slug_sig@@/... (same)
  build dir : code/@@build_dir@@/{build.py, entries_*.py, demos_*.py}
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/@@slug_pub@@.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

Never the words "bat belt" anywhere. No website references. No Facebook.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/@@slug_pub@@.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from @@entries_mod@@ import ENTRIES, SIG_TAIL, LANG
from @@demos_mod@@ import DEMOS
sys.path.insert(0, os.path.join(REPO, "code", "lang-batch9-common"))
import langkit

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature @@Lang@@ "
                "Method: @@sig_flavor@@, the whole language taught as "
                "Signature science. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked @@Lang@@ language "
                "teaching: @@pub_detail@@ - every record carrying "
                "@@Lang@@ content in @@script_short@@ plus example "
                "sentences.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system, pronunciation and "
              "phonology, core nouns, core verbs, adjectives and adverbs, "
              "pronouns, numbers and time, greetings, grammar essentials) "
              "-> Compounded (home and family, food and cooking, travel "
              "and directions, work and school, health and body, emotions "
              "and feelings, nature and weather, shopping and money, "
              "friendship and social life, technology and communication, "
              "verb tenses in sentences) -> Advanced (questions and "
              "answers, commands and requests, descriptions, three "
              "stories, idioms and proverbs, formal and polite registers, "
              "compound and complex sentences, three conversations, "
              "mastery review and full reference).")
    return {
        "name": name, "tagline": tagline, "record_kind": "language learning record",
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search @@Lang@@ letters, words, verbs, tenses, phrases, grammar, dialogues...",
        "chat_ph": "Ask about @@Lang@@...",
        "archive_blurb": ("Seeded %s @@Lang@@ language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \\u00b7 Compounded \\u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled @@Lang@@ language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about @@Lang@@ - from @@script_phrase@@ and sounds through core words, grammar, and everyday sentences to stories, idioms, and conversations." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "@@slug@@-study", "gen_demo_kind": "@@slug@@-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["@@slug_pub@@"] = _cfg(
    "@@slug_pub@@", "The @@Lang@@ Language Database",
    "Learn @@Lang@@ from the ground up: the language overview, @@script_phrase@@, "
    "pronunciation and phonology, core vocabulary with sentences, grammar essentials, "
    "and themed sentence sets for daily life - every record carrying @@Lang@@ in "
    "@@script_short@@ plus example sentences, taught progressively along the ladder.",
    "@@PREFIX@@", "JAH @@Lang@@ Language Archivist",
    "@@Lang@@ language archivist - @@role_detail@@; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, "
    "pronunciation, usage, grammar, culture - using only archive data from "
    "this system",
    "public")
DBCFG["@@slug_sig@@"] = _cfg(
    "@@slug_sig@@", "The @@Lang@@ Language Signature Database",
    "His original Signature @@Lang@@ Method: @@sig_flavor@@ - the full ladder from the language "
    "overview through the script, sounds, words, and grammar, through "
    "daily-life sentences, to stories, idioms, registers, and conversations, "
    "reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "@@PREFIXS@@", "JAH @@Lang@@ Language Archivist (Signature)",
    "@@Lang@@ language archivist - Signature editions: his original "
    "Signature @@Lang@@ Method, @@sig_flavor@@, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles using only archive data from this "
    "system",
    "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["demo_key"] for e in ENTRIES}, "demo map misses entries"


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
        demo_fn = DEMOS[e["demo_key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["demo_data"])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def _extract_scripts(page):
    """Return list of inline <script> (non-src, JS only) bodies for node --check."""
    scripts = []
    for m in re.finditer(r'<script([^>]*)>(.*?)</script>', page, re.S):
        attrs, body = m.group(1), m.group(2).strip()
        if re.search(r'\\bsrc=', attrs):
            continue
        tm = re.search(r'type="([^"]+)"', attrs)
        if tm and tm.group(1) not in ("text/javascript", "application/javascript"):
            continue
        if body:
            scripts.append(body)
    return scripts


def main():
    for slug, m in META.items():
        build_dir = os.path.join(CODE, "language-%s-build" % slug)
        os.makedirs(build_dir, exist_ok=True)
        params = dict(m)
        params["slug"] = slug
        params["slug_pub"] = "language-" + slug
        params["slug_sig"] = "language-" + slug + "-signature"
        params["build_dir"] = "language-%s-build" % slug
        params["entries_mod"] = "entries_language_" + slug
        params["demos_mod"] = "demos_language_" + slug
        def sub(t):
            for k, v in params.items():
                t = t.replace("@@%s@@" % k, v)
            return t
        assert "@@" not in sub(BUILD_TMPL), "unreplaced token in build.py"
        with open(os.path.join(build_dir, "build.py"), "w", encoding="utf-8") as f:
            f.write(sub(BUILD_TMPL))
        with open(os.path.join(build_dir, "demos_language_%s.py" % slug),
                  "w", encoding="utf-8") as f:
            f.write(sub(DEMOS_TMPL))
        print("staged", build_dir)


if __name__ == "__main__":
    main()
