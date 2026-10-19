#!/usr/bin/env python3
"""Regenerate build.py + demos for the 9 remaining batch-9 language pairs
from the PROVEN Serbian build.py via tokenization.

Reads META from gen_builds.py (only the intact META dict), tokenizes the
Serbian build.py, swaps the _cfg/DBCFG prose spans for parameterized
versions, then emits per-language build.py + demos files.
"""
import ast
import os
import re

COMMON = os.path.dirname(os.path.abspath(__file__))
CODE = "/home/hatch/workspace/jah-databases/code"

# ---- load META from gen_builds.py (only the intact META dict) ----
gsrc = open(os.path.join(COMMON, "gen_builds.py")).read()
mstart = gsrc.index("META = {")
mend = gsrc.index("\n}\n\nBUILD_TMPL")
META = ast.literal_eval(gsrc[mstart + len("META = "):mend + len("\n}")].strip())
print("META languages:", sorted(META))

# ---- tokenize the proven Serbian build.py ----
src = open(os.path.join(CODE, "language-serbian-build", "build.py")).read()

REPLS = [
    ("language-serbian-signature", "@@SLUG_SIG@@"),
    ("language-serbian-build", "@@BUILD_DIR@@"),
    ("entries_language_serbian", "@@ENTRIES_MOD@@"),
    ("demos_language_serbian", "@@DEMOS_MOD@@"),
    ("language-serbian", "@@SLUG_PUB@@"),
    ("JAH-LSRPS-", "@@PREFIXS@@"),
    ("JAH-LSRP-", "@@PREFIX@@"),
    ("JAH Serbian Language Archivist (Signature)",
     "JAH @@LANG@@ Language Archivist (Signature)"),
    ("JAH Serbian Language Archivist", "JAH @@LANG@@ Language Archivist"),
    ("serbian-study", "@@SLUG@@-study"),
    ("serbian-demo", "@@SLUG@@-demo"),
    ("/tmp/langsr_check_", "/tmp/lang@@SLUG@@_check_"),
    ("Serbian", "@@LANG@@"),
    ("serbian", "@@SLUG@@"),
]
for old, new in REPLS:
    assert old in src, "missing literal for tokenization: %r" % old
    src = src.replace(old, new)
assert "Serbian" not in src and "serbian" not in src.replace("@@SLUG@@", ""), \
    "leftover serbian literal"

# ---- swap the _cfg prose span for a parameterized version ----
cstart = src.index("def _cfg(")
cend = src.index("DBCFG = {}")
NEW_CFG = '''SIG_FLAVOR = "@@SIG_FLAVOR@@"
PUB_DETAIL = "@@PUB_DETAIL@@"
SCRIPT_PHRASE = "@@SCRIPT_PHRASE@@"
SCRIPT_SHORT = "@@SCRIPT_SHORT@@"
ROLE_DETAIL = "@@ROLE_DETAIL@@"

def _cfg(slug, name, tagline, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature @@LANG@@ "
                "Method: " + SIG_FLAVOR + ", the whole language taught as "
                "Signature science. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked @@LANG@@ language "
                "teaching: " + PUB_DETAIL + " - every record carrying "
                "@@LANG@@ content in " + SCRIPT_SHORT + " plus example "
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
        "search_ph": "Search @@LANG@@ letters, words, verbs, tenses, phrases, grammar, dialogues...",
        "chat_ph": "Ask about @@LANG@@...",
        "archive_blurb": ("Seeded %s @@LANG@@ language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \\u00b7 Compounded \\u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled @@LANG@@ language studies. Seeded archive records are the authoritative entries.",
        "greet": ("I am the %s. Ask me about @@LANG@@ - from " + SCRIPT_PHRASE + " and sounds through core words, grammar, and everyday sentences to stories, idioms, and conversations.") % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "@@SLUG@@-study", "gen_demo_kind": "@@SLUG@@-demo",
        "source": source,
    }

'''
src = src[:cstart] + NEW_CFG + src[cend:]

# ---- swap the two DBCFG calls for parameterized versions ----
dstart = src.index('DBCFG["@@SLUG_PUB@@"] = _cfg(')
dend = src.index("base.DBCFG = DBCFG")
NEW_DBCFG_CALLS = '''DBCFG["@@SLUG_PUB@@"] = _cfg(
    "@@SLUG_PUB@@", "The @@LANG@@ Language Database",
    "Learn @@LANG@@ from the ground up: the language overview, " + SCRIPT_PHRASE + ", "
    "pronunciation and phonology, core vocabulary with sentences, grammar essentials, "
    "and themed sentence sets for daily life - every record carrying @@LANG@@ in "
    + SCRIPT_SHORT + " plus example sentences, taught progressively along the ladder.",
    "@@PREFIX@@", "JAH @@LANG@@ Language Archivist",
    "@@LANG@@ language archivist - " + ROLE_DETAIL + "; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, "
    "pronunciation, usage, grammar, culture - using only archive data from "
    "this system",
    "public")
DBCFG["@@SLUG_SIG@@"] = _cfg(
    "@@SLUG_SIG@@", "The @@LANG@@ Language Signature Database",
    "His original Signature @@LANG@@ Method: " + SIG_FLAVOR + " - the full ladder from the language "
    "overview through the script, sounds, words, and grammar, through "
    "daily-life sentences, to stories, idioms, registers, and conversations, "
    "reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "@@PREFIXS@@", "JAH @@LANG@@ Language Archivist (Signature)",
    "@@LANG@@ language archivist - Signature editions: his original "
    "Signature @@LANG@@ Method, " + SIG_FLAVOR + ", clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles using only archive data from this "
    "system",
    "signature")

'''
src = src[:dstart] + NEW_DBCFG_CALLS + src[dend:]
assert "@@" in src

DEMOS_TMPL = '''#!/usr/bin/env python3
"""Demo map for the @@LANG@@ Language databases. Auto-built from langkit."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "lang-batch9-common"))
import langkit
from @@ENTRIES_MOD@@ import ENTRIES

DEMOS = langkit.standard_demos(ENTRIES)
'''


def emit(slug, m):
    build_dir = os.path.join(CODE, "language-%s-build" % slug)
    os.makedirs(build_dir, exist_ok=True)
    params = dict(m)
    params.update({
        "LANG": m["Lang"],
        "SIG_FLAVOR": m["sig_flavor"],
        "PUB_DETAIL": m["pub_detail"],
        "SCRIPT_PHRASE": m["script_phrase"],
        "SCRIPT_SHORT": m["script_short"],
        "ROLE_DETAIL": m["role_detail"],
        "SLUG": slug,
        "SLUG_PUB": "language-" + slug,
        "SLUG_SIG": "language-" + slug + "-signature",
        "BUILD_DIR": "language-%s-build" % slug,
        "ENTRIES_MOD": "entries_language_" + slug,
        "DEMOS_MOD": "demos_language_" + slug,
    })

    def sub(t):
        for k, v in params.items():
            t = t.replace("@@%s@@" % k, v)
        return t

    out = sub(src)
    assert "@@" not in out, "unreplaced token in %s build.py" % slug
    assert "Serbian" not in out and "serbian" not in out, "serbian leftover"
    bpath = os.path.join(build_dir, "build.py")
    with open(bpath, "w", encoding="utf-8") as f:
        f.write(out)
    dpath = os.path.join(build_dir, "demos_language_%s.py" % slug)
    with open(dpath, "w", encoding="utf-8") as f:
        f.write(sub(DEMOS_TMPL))
    # syntax check both
    for p in (bpath, dpath):
        ast.parse(open(p, encoding="utf-8").read())
    print("staged + syntax OK:", build_dir)


if __name__ == "__main__":
    for slug, m in META.items():
        emit(slug, m)
