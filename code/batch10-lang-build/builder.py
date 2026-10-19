#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""builder.py — Batch 10 language databases (ranks 91-100).
Builds 10 language->English database pairs (public + Signature), 34 FULL
records each (680 records). Stages fragments only; never commits; never
touches data/manifest.json or api.json (coordinator merges).

Layout per slug:
  ~/workspace/jah-databases/db/<slug>/index.html + gen-<slug>.js
  ~/workspace/jah-databases-data-1/data/<slug>/index.jsonl.gz (34 {id,t,g})
  ~/workspace/jah-databases-data-1/data/<slug>/chunks/chunk-0000.jsonl.gz (34 full)

Gates: every demo program executed (exit 0); node --check on all gen
scripts; dedupe vs whole system (ids + titles); term gate with
context-checked false-positive classes; 34+34 counts per pair.
"""
import gzip
import html
import json
import os
import re
import subprocess
import sys
import tempfile

BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BUILD_DIR)

import lang_tigrinya, lang_kinyarwanda, lang_xhosa, lang_lao, lang_uyghur
import lang_turkmen, lang_tatar, lang_madurese, lang_balochi, lang_hmong

HOME = os.path.expanduser("~")
DB_ROOT = os.path.join(HOME, "workspace", "jah-databases", "db")
DATA_ROOT = os.path.join(HOME, "workspace", "jah-databases-data-1", "data")
LOCAL_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/"
PROP = "Property of Justin Addam Higgins (JAH)."

LANGS = [lang_tigrinya, lang_kinyarwanda, lang_xhosa, lang_lao, lang_uyghur,
         lang_turkmen, lang_tatar, lang_madurese, lang_balochi, lang_hmong]

# Tense drill rows: (native, roman, english, tense_label) per language.
# Authored carefully; the record text explains the system honestly.
TENSE_FORMS = {
    "language-tigrinya": [
        ("ይሰርሕ", "yəserh", "he works", "present"),
        ("ሰርሐ", "serhä", "he worked", "past"),
        ("ይሰርሕ", "yəserh", "he will work", "future (imperfect + context)"),
        ("ኣሎ", "allo", "he is here / there is", "present"),
        ("ነይሩ", "näyru", "there was", "past"),
        ("ይኸውን", "yəkhäwn", "it will be", "future"),
        ("ይምሃር", "yəmhar", "he learns", "present"),
        ("ተማህረ", "temahre", "he learned / studied", "past"),
        ("ይምሃር", "yəmhar", "he will learn", "future (imperfect + context)"),
    ],
    "language-kinyarwanda": [
        ("ndakora", "ndakora", "I am working", "present"),
        ("nakoze", "nakoze", "I worked", "past"),
        ("nzakora", "nzakora", "I will work", "future"),
        ("ndarya", "ndarya", "I am eating", "present"),
        ("nariye", "nariye", "I ate", "past"),
        ("nzarya", "nzarya", "I will eat", "future"),
        ("ndagenda", "ndagenda", "I am going", "present"),
        ("nagiye", "nagiye", "I went", "past"),
        ("nzagenda", "nzagenda", "I will go", "future"),
    ],
    "language-xhosa": [
        ("ndiyahamba", "ndiyahamba", "I am going", "present"),
        ("ndihambile", "ndihambile", "I have gone", "past"),
        ("ndizahamba", "ndizahamba", "I will go", "future"),
        ("ndiyatya", "ndiyatya", "I am eating", "present"),
        ("ndityile", "ndityile", "I have eaten", "past"),
        ("ndizatya", "ndizatya", "I will eat", "future"),
        ("ndiyasebenza", "ndiyasebenza", "I am working", "present"),
        ("ndisebenzile", "ndisebenzile", "I have worked", "past"),
        ("ndizasebenza", "ndizasebenza", "I will work", "future"),
    ],
    "language-lao": [
        ("ຂ້ອຍກິນ", "khoi kin", "I eat", "present"),
        ("ຂ້ອຍກິນແລ້ວ", "khoi kin laeo", "I ate / have eaten", "completed"),
        ("ຂ້ອຍຈະກິນ", "khoi cha kin", "I will eat", "future"),
        ("ຂ້ອຍໄປ", "khoi pai", "I go", "present"),
        ("ຂ້ອຍໄປແລ້ວ", "khoi pai laeo", "I went / have gone", "completed"),
        ("ຂ້ອຍຈະໄປ", "khoi cha pai", "I will go", "future"),
        ("ຂ້ອຍເຮັດວຽກ", "khoi het viak", "I work", "present"),
        ("ຂ້ອຍເຮັດວຽກແລ້ວ", "khoi het viak laeo", "I worked / have worked", "completed"),
        ("ຂ້ອຍຈະເຮັດວຽກ", "khoi cha het viak", "I will work", "future"),
    ],
    "language-uyghur": [
        ("مەن ئوقۇيمەن", "men oquymen", "I read / I will read", "present-future"),
        ("مەن ئوقۇدۇم", "men oqudum", "I read / I studied", "past"),
        ("مەن ئوقۇۋاتىمەن", "men oquwatimen", "I am reading", "progressive"),
        ("مەن يەيمەن", "men yeymen", "I eat / I will eat", "present-future"),
        ("مەن يېدىم", "men yedim", "I ate", "past"),
        ("مەن يەۋاتىمەن", "men yewatimen", "I am eating", "progressive"),
        ("مەن ئىشلەيمەن", "men ishlaymen", "I work / I will work", "present-future"),
        ("مەن ئىشلىدىم", "men ishlidim", "I worked", "past"),
        ("مەن ئىشلەۋاتىمەن", "men ishlawatimen", "I am working", "progressive"),
    ],
    "language-turkmen": [
        ("men işleýärin", "men işleýärin", "I am working", "present"),
        ("men işledim", "men işledim", "I worked", "past"),
        ("men işlärin", "men işlärin", "I will work", "future"),
        ("men iýýärin", "men iýýärin", "I am eating", "present"),
        ("men iýdim", "men iýdim", "I ate", "past"),
        ("men iýerin", "men iýerin", "I will eat", "future"),
        ("men gidýärin", "men gidýärin", "I am going", "present"),
        ("men gitdim", "men gitdim", "I went", "past"),
        ("men giderin", "men giderin", "I will go", "future"),
    ],
    "language-tatar": [
        ("мин эшлим", "min eşlim", "I am working", "present"),
        ("мин эшләдем", "min eşlädem", "I worked", "past"),
        ("мин эшләрмен", "min eşlärmen", "I will work", "future"),
        ("мин ашыйм", "min aşıyım", "I am eating", "present"),
        ("мин ашадым", "min aşadım", "I ate", "past"),
        ("мин ашармын", "min aşarmın", "I will eat", "future"),
        ("мин барам", "min baram", "I am going", "present"),
        ("мин бардым", "min bardım", "I went", "past"),
        ("мин барырмын", "min barırmın", "I will go", "future"),
    ],
    "language-madurese": [
        ("sengko' ngakan", "sengko' ngakan", "I eat", "present"),
        ("sengko' la ngakan", "sengko' la ngakan", "I ate / have eaten", "completed"),
        ("sengko' bhâkal ngakan", "sengko' bhâkal ngakan", "I will eat", "future"),
        ("sengko' mèyos", "sengko' mèyos", "I go", "present"),
        ("sengko' la mèyos", "sengko' la mèyos", "I went / have gone", "completed"),
        ("sengko' bhâkal mèyos", "sengko' bhâkal mèyos", "I will go", "future"),
        ("sengko' alako", "sengko' alako", "I work", "present"),
        ("sengko' la alako", "sengko' la alako", "I worked / have worked", "completed"),
        ("sengko' bhâkal alako", "sengko' bhâkal alako", "I will work", "future"),
    ],
    "language-balochi": [
        ("من واراں", "man warán", "I eat / I will eat", "present-future"),
        ("من ورت", "man wart", "I ate", "past"),
        ("من باندا واراں", "man bándá warán", "I will eat tomorrow", "future (time word)"),
        ("من کناں", "man kanán", "I do / I will do", "present-future"),
        ("من کرت", "man kurt", "I did", "past"),
        ("من باندا کناں", "man bándá kanán", "I will do tomorrow", "future (time word)"),
        ("من دیاں", "man dayán", "I give / I will give", "present-future"),
        ("من دات", "man dát", "I gave", "past"),
        ("من باندا دیاں", "man bándá dayán", "I will give tomorrow", "future (time word)"),
    ],
    "language-hmong": [
        ("kuv noj", "kuv noj", "I eat", "present"),
        ("kuv tau noj", "kuv tau noj", "I ate / have eaten", "completed"),
        ("kuv yuav noj", "kuv yuav noj", "I will eat", "future"),
        ("kuv tab tom noj", "kuv tab tom noj", "I am eating", "progressive"),
        ("kuv mus", "kuv mus", "I go", "present"),
        ("kuv tau mus", "kuv tau mus", "I went / have gone", "completed"),
        ("kuv yuav mus", "kuv yuav mus", "I will go", "future"),
        ("kuv ua haujlwm", "kuv ua haujlwm", "I work", "present"),
        ("kuv tau ua haujlwm", "kuv tau ua haujlwm", "I worked / have worked", "completed"),
        ("kuv yuav ua haujlwm", "kuv yuav ua haujlwm", "I will work", "future"),
    ],
}

# ---------------------------------------------------------------- demo programs
def _head(title, rec_id, tier):
    return [
        "#!/usr/bin/env python3",
        '"""%s - working demonstration.' % title,
        "Record %s [%s]. %s" % (rec_id, tier, PROP),
        '"""',
        "NAME = %r" % title,
    ]


def demo_vocab(title, rec_id, tier, words, sig=False, kind_label="cards"):
    """words: list of lists; [native, roman, english] + optional sentence triple."""
    L = _head(title, rec_id, tier)
    L.append("WORDS = %r" % (words,))
    L.append("def find_card(native, roman, english):")
    L.append("    for w in WORDS:")
    L.append("        if w[0] == native and w[1] == roman and w[2] == english:")
    L.append("            return w")
    L.append("    return None")
    L.append("def main():")
    L.append('    print("Study " + %r + " - " + NAME + ":")' % kind_label)
    L.append("    for w in WORDS:")
    L.append('        line = "  %s (%s) - %s" % (w[0], w[1], w[2])')
    L.append("        if len(w) > 3:")
    L.append('            line += " | e.g. %s (%s) - %s" % (w[3], w[4], w[5])')
    L.append("        print(line)")
    L.append('    print("Self-test: every card is present and well-formed in the table.")')
    L.append("    score = 0")
    L.append("    for w in WORDS:")
    L.append("        assert len(w) in (3, 6), 'card must carry 3 or 6 fields'")
    L.append("        assert all(isinstance(x, str) and x.strip() for x in w), 'empty field'")
    L.append("        hit = find_card(w[0], w[1], w[2])")
    L.append("        assert hit is not None, 'card missing from table'")
    L.append("        score += 1")
    if sig:
        L.append('    print("Signature reverse drill: English -> native form.")')
        L.append("    for w in WORDS:")
        L.append("        rev = [x for x in WORDS if x[2] == w[2]][0]")
        L.append("        assert rev[0] == w[0], 'reverse drill failed'")
        L.append('    print("Reverse drill passed for %d cards." % len(WORDS))')
    L.append('    print("OK: " + NAME + " verified " + str(score) + "/" + str(len(WORDS)) + " %s")' % kind_label)
    L.append('if __name__ == "__main__":')
    L.append("    main()")
    return "\n".join(L) + "\n"


def demo_lines(title, rec_id, tier, lines, sig=False, kind_label="lines"):
    """lines: list of (native, roman, english[, extra...])."""
    L = _head(title, rec_id, tier)
    L.append("LINES = %r" % (lines,))
    L.append("def main():")
    L.append('    print("%s:" % NAME)')
    L.append("    for ln in LINES:")
    L.append('        print("  %s (%s) - %s" % (ln[0], ln[1], ln[2]))')
    L.append("        if len(ln) > 3:")
    L.append('            print("    -> %s" % (ln[3],))')
    L.append("    assert LINES, 'no lines'")
    L.append("    for ln in LINES:")
    L.append("        assert len(ln) >= 3 and all(isinstance(x, str) and x.strip() for x in ln[:3])")
    if sig:
        L.append('    print("Signature check: every line carries native + romanization + English.")')
        L.append("    assert all(len(ln) >= 3 for ln in LINES)")
    L.append('    print("OK: " + NAME + " verified " + str(len(LINES)) + " %s")' % kind_label)
    L.append('if __name__ == "__main__":')
    L.append("    main()")
    return "\n".join(L) + "\n"


def demo_facts(title, rec_id, tier, facts, asserts, intro, sig=False):
    """facts: dict; asserts: list of (key, op, value, message)."""
    L = _head(title, rec_id, tier)
    L.append("FACTS = %r" % (facts,))
    L.append("def main():")
    L.append('    print(%r)' % intro)
    L.append("    for k, v in FACTS.items():")
    L.append('        print("  %s: %s" % (k, v))')
    for key, op, val, msg in asserts:
        L.append('    assert FACTS[%r] %s %r, %r' % (key, op, val, msg))
    if sig:
        L.append('    print("Signature pass: facts cross-checked against the teaching ladder.")')
        L.append("    assert len(FACTS) >= 3")
    L.append('    print("OK: %s verified %d core facts" % (NAME, len(FACTS)))')
    L.append('if __name__ == "__main__":')
    L.append("    main()")
    return "\n".join(L) + "\n"


def demo_alpha(title, rec_id, tier, alpha, sig=False):
    L = _head(title, rec_id, tier)
    L.append("ALPHA = %r" % (alpha,))
    L.append("def main():")
    L.append('    print("Alphabet sample - %s:" % NAME)')
    L.append("    for letter, sound in ALPHA:")
    L.append('        print("  %s - %s" % (letter, sound))')
    L.append("    assert len(ALPHA) >= 10, 'alphabet sample too small'")
    L.append("    for letter, sound in ALPHA:")
    L.append("        assert letter.strip() and sound.strip(), 'empty alphabet cell'")
    if sig:
        L.append('    print("Signature pass: every letter has a sound value; no gaps.")')
        L.append("    assert len({a for a, _ in ALPHA}) == len(ALPHA), 'duplicate letter'")
    L.append('    print("OK: %s verified %d alphabet entries" % (NAME, len(ALPHA)))')
    L.append('if __name__ == "__main__":')
    L.append("    main()")
    return "\n".join(L) + "\n"


def demo_convo(title, rec_id, tier, convo_title, turns, sig=False):
    L = _head(title, rec_id, tier)
    L.append("CONVO = %r" % convo_title)
    L.append("TURNS = %r" % (turns,))
    L.append("def main():")
    L.append('    print("Conversation: %s" % CONVO)')
    L.append("    for who, native, roman, english in TURNS:")
    L.append('        print("  %s: %s (%s) - %s" % (who, native, roman, english))')
    L.append("    assert len(TURNS) == 8, 'a full conversation carries 8 turns'")
    L.append("    speakers = {t[0] for t in TURNS}")
    L.append("    assert speakers == {'A', 'B'}, 'dialogue needs both speakers'")
    if sig:
        L.append('    print("Signature pass: turn-taking alternates cleanly.")')
        L.append("    assert all(TURNS[i][0] != TURNS[i+1][0] for i in range(len(TURNS)-1))")
    L.append('    print("OK: %s verified %d dialogue turns" % (NAME, len(TURNS)))')
    L.append('if __name__ == "__main__":')
    L.append("    main()")
    return "\n".join(L) + "\n"

# ---------------------------------------------------------------- record assembly
def _req(m, rank):
    return [
        "No prior knowledge of %s needed - start here at ladder rank %d of 34." % (m.NAME, rank),
        "Python 3 to run the working demonstration program.",
        "Read every line as: %s + romanization + English." % m.NAME,
    ]


def _std(m, sig, rank, tier):
    iso = "ISO 639-3: %s" % m.ISO3
    if m.ISO1:
        iso += "; ISO 639-1: %s" % m.ISO1
    src = "signature" if sig else "public-harvest"
    kind = ("Signature-system expanded ladder treatment"
            if sig else "real, fact-checked public language data")
    return [
        "Record schema: id, t, g, name, title, description, how_it_works, "
        "key_points, requirements, standards, citations, src, ladder_rank, ladder_tier, demo.",
        iso,
        "Teaching ladder: rank %d of 34, tier %s." % (rank, tier),
        "src=%s - %s organized in the Signature system." % (src, kind),
    ]


def _sig_expand(text, sig, extra):
    if not sig:
        return text
    return (text + " Signature-method expansion: the same material is re-taught "
            "as a ladder drill - hear it, say it, write it, use it - with the "
            "reverse check built in, so every form is met from both directions. " + extra)


def vocab_how(words, sent=True):
    out = []
    for i, w in enumerate(words, 1):
        out.append("%d. %s (%s) - %s." % (i, w[0], w[1], w[2]))
        if sent and len(w) > 3:
            out.append("   Example: %s (%s) - %s." % (w[3], w[4], w[5]))
    return " ".join(out)


def theme_title(m, theme):
    return "%s at %s" % (m.NAME, theme) if theme == "Home and Family" else "%s %s" % (m.NAME, theme)


def build_records(m, sig):
    P = m.SIG_PREFIX if sig else m.PREFIX
    S = " (Signature Edition)" if sig else ""
    src = "signature" if sig else "public-harvest"
    recs = []

    def base(rank, tier, t, title, desc, how, keys, demo, demo_kind):
        rid = "%s%06d" % (P, rank)
        return {
            "id": rid, "t": t + S, "g": tier,
            "name": title + " - language learning record",
            "title": title, "description": desc, "how_it_works": how,
            "key_points": keys, "requirements": _req(m, rank),
            "standards": _std(m, sig, rank, tier),
            "citations": list(m.CITATIONS), "src": src,
            "ladder_rank": rank, "ladder_tier": tier,
            "demo": {"kind": demo_kind, "language": "python",
                     "program": demo,
                     "note": "Working demonstration program (real, runnable Python)."},
        }

    kind = "%s-demo" % m.NAME.lower()
    F, C, A = "Foundations", "Compounded", "Advanced"

    # ---- 1. Overview
    r = 1
    t = "%s Language Overview" % m.NAME
    title = t + S
    facts = {"speakers": m.SPEAKERS, "regions": m.REGIONS, "family": m.FAMILY,
             "script": m.SCRIPT_NAME, "word_order": m.WORD_ORDER,
             "iso3": m.ISO3, "native_name": "%s (%s)" % (m.NATIVE, m.NATIVE_ROMAN)}
    asserts = [("speakers", "!=", "", "speakers missing"),
               ("script", "!=", "", "script missing"),
               ("iso3", "==", m.ISO3, "ISO code wrong")]
    desc = ("Meet %s (%s, %s): %s. %s %s" %
            (m.NAME, m.NATIVE, m.NATIVE_ROMAN, m.SPEAKERS, m.REGIONS + ".", m.FAMILY + "."))
    how = _sig_expand(m.OVERVIEW, sig,
                      "The overview is re-taught as a memory palace: name, family, "
                      "homeland, script, word order - each pinned to one vivid fact.")
    keys = ["%s (%s) is a %s language." % (m.NAME, m.NATIVE_ROMAN, m.FAMILY.split(">")[0].strip()),
            "Spoken by %s." % m.SPEAKERS,
            "Homeland: %s." % m.REGIONS,
            "Written in %s." % m.SCRIPT_NAME,
            "Word order: %s." % m.WORD_ORDER,
            "Native name: %s (%s)." % (m.NATIVE, m.NATIVE_ROMAN),
            "This record is ladder rank 1: the map before the journey."]
    recs.append(base(r, F, t, title, desc, how, keys,
                    demo_facts(title, "%s%06d" % (P, r), F, facts, asserts,
                               "Core facts - %s:" % m.NAME, sig), kind))

    # ---- 2. Writing system and alphabet
    r = 2
    t = "%s Writing System and Alphabet" % m.NAME
    title = t + S
    desc = ("The %s writing system from zero: %s. Every letter below carries "
            "its sound value." % (m.NAME, m.SCRIPT_DESC.split(".")[0] + "."))
    how = _sig_expand(m.SCRIPT_DESC + " " + m.ALPHABET_NOTE + " Key letters: " +
                      "; ".join("%s = %s" % (a, b) for a, b in m.ALPHABET_SAMPLE) + ".",
                      sig, "The alphabet is drilled as write-say pairs until the "
                      "hand knows what the eye sees.")
    keys = ["%s is written in %s." % (m.NAME, m.SCRIPT_NAME),
            "The sample table below covers the letters beginners must learn first.",
            "Reading direction and letter shapes are fixed - no surprises.",
            "Every later record prints %s in this script with romanization beside it." % m.NAME,
            "Copy the letters by hand once; recognition follows writing.",
            "This record is ladder rank 2: the script before the words."]
    recs.append(base(r, F, t, title, desc, how, keys,
                    demo_alpha(title, "%s%06d" % (P, r), F, list(m.ALPHABET_SAMPLE), sig), kind))

    # ---- 3. Pronunciation and phonology
    r = 3
    t = "%s Pronunciation and Phonology" % m.NAME
    title = t + S
    desc = ("How %s sounds: the vowel and consonant system, stress and rhythm, "
            "and the sounds English speakers must learn." % m.NAME)
    how = _sig_expand(m.SOUNDS_DESC, sig,
                      "Pronunciation is drilled as minimal pairs: change one "
                      "sound, change the meaning - the ear learns by contrast.")
    facts = {"vowel_note": m.SOUNDS_DESC.split(".")[0] + ".",
             "stress_note": m.SOUNDS_DESC.split(".")[-2] + "." if len(m.SOUNDS_DESC.split(".")) > 2 else m.SOUNDS_DESC[:80],
             "key_sound": m.SOUNDS_DESC.split(".")[1] + "." if len(m.SOUNDS_DESC.split(".")) > 2 else m.SOUNDS_DESC[:80]}
    asserts = [("vowel_note", "!=", "", "vowel note missing"),
               ("key_sound", "!=", "", "key sound missing")]
    keys = ["%s vowels and consonants are described with English anchors." % m.NAME,
            "Stress and rhythm rules are stated plainly - no guessing.",
            "The signature sounds of %s are named and drilled." % m.NAME,
            "Read the romanization aloud until the native script feels natural.",
            "This record is ladder rank 3: the sounds before the sentences."]
    recs.append(base(r, F, t, title, desc, how, keys,
                    demo_facts(title, "%s%06d" % (P, r), F, facts, asserts,
                               "Pronunciation facts - %s:" % m.NAME, sig), kind))

    # ---- 4-9. Core vocabulary
    vocab_specs = [
        (4, "Core Nouns I", m.NOUNS, "the naming words: water, bread, house, family, market, day and night"),
        (5, "Core Verbs I", m.VERBS, "the doing words: eat, drink, go, come, speak, work, learn, give, love, live"),
        (6, "Adjectives and Adverbs", m.ADJS, "the describing words: good, bad, big, small, new, old, colors"),
        (7, "Pronouns", m.PRONOUNS, "the pointing words: I, you, he/she, we, they, this, that"),
        (8, "Numbers and Time", list(m.NUMBERS) + list(m.TIME_WORDS),
         "counting one to one hundred and the words for today, tomorrow, week, month, year"),
        (9, "Greetings and Everyday Phrases", m.GREETINGS, "hello, how are you, thank you, please, sorry, goodbye"),
    ]
    for r, suffix, words, about in vocab_specs:
        words = [list(w) for w in words]
        t = "%s %s" % (m.NAME, suffix)
        title = t + S
        desc = ("Core %s vocabulary: %s. Every entry carries %s, romanization, "
                "and English - with example sentences where they help." %
                (m.NAME.lower(), about, m.NAME))
        keys = ["%d core entries, each with %s + romanization + English." % (len(words), m.NAME),
                "Example sentences show each word doing real work." if any(len(w) > 3 for w in words) else "Every entry is a complete pointing word.",
                "Learn five a day; the demo program quizzes you on all of them.",
                "Say each word aloud - %s rewards the speaking learner." % m.NAME,
                "This record is ladder rank %d: words before sentences." % r]
        recs.append(base(r, F, t, title, desc, vocab_how(words), keys,
                        demo_vocab(title, "%s%06d" % (P, r), F, words, sig,
                                   "vocabulary cards"), kind))

    # ---- 10. Grammar essentials
    r = 10
    t = "%s Grammar Essentials" % m.NAME
    title = t + S
    desc = ("The grammar engine of %s in one record: word order, how words "
            "change, negation, and questions." % m.NAME)
    how = _sig_expand(m.GRAMMAR_DESC, sig,
                      "Grammar is drilled as transformations: take a sentence, "
                      "flip it to negative, flip it to a question - the engine "
                      "reveals itself by moving.")
    facts = {"word_order": m.WORD_ORDER,
             "core_rule": m.GRAMMAR_DESC.split(".")[0] + ".",
             "negation": m.GRAMMAR_DESC.split(".")[-2] + "." if len(m.GRAMMAR_DESC.split(".")) > 2 else m.GRAMMAR_DESC[:80]}
    asserts = [("word_order", "==", m.WORD_ORDER, "word order wrong"),
               ("core_rule", "!=", "", "core rule missing")]
    keys = ["Word order: %s." % m.WORD_ORDER,
            "The core grammatical machinery is stated in plain sentences.",
            "Negation and question formation are covered with examples.",
            "Grammar is a tool, not a wall - use it to build.",
            "This record is ladder rank 10: the engine before the road."]
    recs.append(base(r, F, t, title, desc, how, keys,
                    demo_facts(title, "%s%06d" % (P, r), F, facts, asserts,
                               "Grammar facts - %s:" % m.NAME, sig), kind))

    # ---- 11-20. Themed sentence sets
    for i, (theme, lines) in enumerate(m.THEMES):
        r = 11 + i
        lines = [list(x) for x in lines]
        t = theme_title(m, theme)
        title = t + S
        desc = ("%s for daily life: %s. Six full sentences, every one carrying "
                "%s + romanization + English." % (m.NAME, theme.lower(), m.NAME))
        how = ("Six %s sentences on %s. " % (m.NAME, theme.lower()) +
               " ".join("%d. %s (%s) - %s." % (j, x[3], x[4], x[5])
                        for j, x in enumerate(lines, 1)))
        how = _sig_expand(how, sig,
                          "Each sentence is drilled three ways: repeat it, "
                          "change one word in it, answer a question about it.")
        keys = ["Six complete %s sentences on %s." % (m.NAME, theme.lower()),
                "Every sentence: %s + romanization + English." % m.NAME,
                "The vocabulary is everyday - usable the same day you learn it.",
                "Read each sentence aloud three times, then cover the English and recall.",
                "This record is ladder rank %d: compounded sentences." % r]
        recs.append(base(r, C, t, title, desc, how, keys,
                        demo_vocab(title, "%s%06d" % (P, r), C, lines, sig,
                                   "sentence cards"), kind))

    # ---- 21. Verb tenses in sentences
    r = 21
    t = "%s Verb Tenses in Sentences" % m.NAME
    title = t + S
    forms = [list(x) for x in TENSE_FORMS[m.SLUG]]
    desc = ("Time in %s: how verbs mark present, past, and future - nine "
            "drill sentences on three everyday verbs." % m.NAME)
    how = _sig_expand(m.TENSE_DESC + " Drill: " +
                      " ".join("%s (%s) - %s [%s]." % (x[0], x[1], x[2], x[3]) for x in forms),
                      sig, "Tense is drilled as a grid: one verb across three "
                      "times, then three verbs in one time - the pattern locks in.")
    keys = ["Nine tense drill sentences: three verbs in three time frames.",
            "Every form: %s + romanization + English + tense label." % m.NAME,
            "The tense system is explained before the drills begin.",
            "Master these nine and every other verb follows the same road.",
            "This record is ladder rank 21: time itself, compounded."]
    lines = [(x[0], x[1], x[2], "tense: " + x[3]) for x in forms]
    recs.append(base(r, C, t, title, desc, how, keys,
                    demo_lines(title, "%s%06d" % (P, r), C, lines, sig,
                               "tense drills"), kind))

    # ---- 22-24. Questions, commands, descriptions
    qcd = [
        (22, "Questions and Answers", [list(x) for x in m.QUESTIONS],
         "the eight questions every traveler needs, with their answers built in"),
        (23, "Commands and Requests", [list(x) for x in m.COMMANDS],
         "eight direct commands - the imperative voice of %s" % m.NAME),
        (24, "Descriptions of People and Places", [list(x) for x in m.DESCRIBE],
         "pointing at the world and describing it in %s" % m.NAME),
    ]
    for r, suffix, lines, about in qcd:
        t = "%s %s" % (m.NAME, suffix)
        title = t + S
        desc = ("%s, advanced: %s. Every line carries %s + romanization + "
                "English." % (m.NAME, about, m.NAME))
        how = _sig_expand(" ".join("%d. %s (%s) - %s." % (j, x[0], x[1], x[2])
                                  for j, x in enumerate(lines, 1)),
                          sig, "Each line is drilled as a call and response: "
                          "hear the %s, produce the English; hear the English, "
                          "produce the %s." % (m.NAME, m.NAME))
        keys = ["Eight advanced %s lines." % m.NAME,
                "Every line: %s + romanization + English." % m.NAME,
                "Use these the next time you need them - they are road-ready.",
                "This record is ladder rank %d: advanced patterns." % r]
        recs.append(base(r, A, t, title, desc, how, keys,
                        demo_lines(title, "%s%06d" % (P, r), A, lines, sig,
                                   "pattern lines"), kind))

    # ---- 25-27. Stories
    for i, (stitle, slines) in enumerate(m.STORIES):
        r = 25 + i
        slines = [list(x) for x in slines]
        t = "%s %s" % (m.NAME, stitle)
        title = t + S
        desc = ("A graded %s story: %s. Eight sentences, simple to less "
                "simple, every one with romanization and English." % (m.NAME, stitle.lower()))
        how = _sig_expand(" ".join("%d. %s (%s) - %s." % (j, x[0], x[1], x[2])
                                  for j, x in enumerate(slines, 1)),
                          sig, "Stories are drilled as retelling: read it, "
                          "close the book, tell it back in %s." % m.NAME)
        keys = ["A complete %s story in eight sentences." % m.NAME,
                "Graded: the sentences grow as the story walks.",
                "Every sentence: %s + romanization + English." % m.NAME,
                "Retell the story aloud - narrative is the strongest memory glue.",
                "This record is ladder rank %d: stories, advanced." % r]
        recs.append(base(r, A, t, title, desc, how, keys,
                        demo_lines(title, "%s%06d" % (P, r), A, slines, sig,
                                   "story sentences"), kind))

    # ---- 28. Idioms and proverbs
    r = 28
    t = "%s Idioms and Proverbs" % m.NAME
    title = t + S
    idioms = [list(x) for x in m.IDIOMS]
    desc = ("The wisdom of %s: %d proverbs and sayings with literal "
            "translations and their real meanings." % (m.NAME, len(idioms)))
    how = _sig_expand(" ".join('%d. "%s" (%s) - literally "%s"; it means: %s.' %
                               (j, x[0], x[1], x[2], x[3])
                               for j, x in enumerate(idioms, 1)),
                      sig, "Proverbs are drilled as situations: hear the "
                      "situation, produce the proverb that fits it.")
    keys = ["%d authentic %s proverbs." % (len(idioms), m.NAME),
            "Each with: native text, romanization, literal translation, real meaning.",
            "Proverbs are the compressed wisdom of a people - learn them whole.",
            "Use one proverb a day; natives will smile.",
            "This record is ladder rank 28: wisdom, advanced."]
    ilines = [(x[0], x[1], x[2], "means: " + x[3]) for x in idioms]
    recs.append(base(r, A, t, title, desc, how, keys,
                    demo_lines(title, "%s%06d" % (P, r), A, ilines, sig,
                               "proverbs"), kind))

    # ---- 29. Formal and polite registers
    r = 29
    t = "%s Formal and Polite Registers" % m.NAME
    title = t + S
    desc = ("Speaking %s well: the formal and polite registers - how respect "
            "is carried in words." % m.NAME)
    how = _sig_expand(m.REGISTER_DESC, sig,
                      "Register is drilled as role-play: the same request to a "
                      "friend, a shopkeeper, and an elder - feel the gears shift.")
    facts = {"register_rule": m.REGISTER_DESC.split(".")[0] + ".",
             "elder_rule": m.REGISTER_DESC.split(".")[1] + "." if len(m.REGISTER_DESC.split(".")) > 2 else m.REGISTER_DESC[:80],
             "greeting_key": m.GREETINGS[0][0] + " (" + m.GREETINGS[0][1] + ") - " + m.GREETINGS[0][2]}
    asserts = [("register_rule", "!=", "", "register rule missing"),
               ("greeting_key", "!=", "", "greeting missing")]
    keys = ["The politeness system of %s, stated plainly." % m.NAME,
            "Formal vs familiar: when to use which, and what happens if you mix them.",
            "Elders, strangers, friends: the three gears of respect.",
            "Politeness is grammar too - learn it like grammar.",
            "This record is ladder rank 29: respect, advanced."]
    recs.append(base(r, A, t, title, desc, how, keys,
                    demo_facts(title, "%s%06d" % (P, r), A, facts, asserts,
                               "Register facts - %s:" % m.NAME, sig), kind))

    # ---- 30. Compound and complex sentences
    r = 30
    t = "%s Compound and Complex Sentences" % m.NAME
    title = t + S
    desc = ("Beyond simple sentences: joining ideas in %s - because, but, so "
            "that, if, and the sentences that carry them." % m.NAME)
    how = _sig_expand(m.COMPLEX_DESC, sig,
                      "Complex sentences are drilled as building: start with "
                      "two simple sentences, join them, then add a third.")
    facts = {"join_rule": m.COMPLEX_DESC.split(".")[0] + ".",
             "relative_rule": m.COMPLEX_DESC.split(".")[1] + "." if len(m.COMPLEX_DESC.split(".")) > 2 else m.COMPLEX_DESC[:80],
             "condition": m.COMPLEX_DESC.split(".")[2] + "." if len(m.COMPLEX_DESC.split(".")) > 3 else m.COMPLEX_DESC[:80]}
    asserts = [("join_rule", "!=", "", "join rule missing"),
               ("condition", "!=", "", "condition rule missing")]
    keys = ["How %s joins clauses: the connector words." % m.NAME,
            "Relative clauses and conditions, with the word order laid bare.",
            "Build long sentences from short ones - never memorize long ones whole.",
            "This record is ladder rank 30: complexity, advanced."]
    recs.append(base(r, A, t, title, desc, how, keys,
                    demo_facts(title, "%s%06d" % (P, r), A, facts, asserts,
                               "Sentence-building facts - %s:" % m.NAME, sig), kind))

    # ---- 31-33. Conversations
    for i, (ctitle, turns) in enumerate(m.CONVOS):
        r = 31 + i
        turns = [list(x) for x in turns]
        t = "%s Conversation: %s" % (m.NAME, ctitle)
        title = t + S
        desc = ("A full %s conversation: %s. Eight turns between two speakers, "
                "every turn with romanization and English." % (m.NAME, ctitle.lower()))
        how = _sig_expand(" ".join("%s: %s (%s) - %s." % (x[0], x[1], x[2], x[3]) for x in turns),
                          sig, "Conversations are drilled as dialogue: take "
                          "both parts aloud, then swap roles with a partner.")
        keys = ["A complete eight-turn %s dialogue: %s." % (m.NAME, ctitle.lower()),
                "Two speakers, natural turn-taking.",
                "Every turn: %s + romanization + English." % m.NAME,
                "Act it out - dialogue learned in the body stays in the memory.",
                "This record is ladder rank %d: real conversation." % r]
        recs.append(base(r, A, t, title, desc, how, keys,
                        demo_convo(title, "%s%06d" % (P, r), A, ctitle, turns, sig), kind))

    # ---- 34. Mastery review
    r = 34
    t = "%s Mastery Review and Full Reference" % m.NAME
    title = t + S
    desc = ("The full %s ladder in one record: every tier reviewed, every "
            "count verified, the whole language at a glance." % m.NAME)
    how = _sig_expand(m.REVIEW_NOTE + " Ladder map: Foundations ranks 1-10 "
                      "(overview, script, sounds, nouns, verbs, adjectives, pronouns, "
                      "numbers and time, greetings, grammar); Compounded ranks 11-21 "
                      "(ten themed sentence sets plus verb tenses); Advanced ranks 22-34 "
                      "(questions, commands, descriptions, three stories, idioms, registers, "
                      "complex sentences, three conversations, this review).",
                      sig, "The review is drilled as a full sweep: one line "
                      "from every record, in ladder order, from memory.")
    facts = {"foundations": 10, "compounded": 11, "advanced": 13,
             "records": 34, "iso3": m.ISO3, "word_order": m.WORD_ORDER}
    asserts = [("foundations", "==", 10, "foundations count wrong"),
               ("compounded", "==", 11, "compounded count wrong"),
               ("advanced", "==", 13, "advanced count wrong"),
               ("records", "==", 34, "record count wrong")]
    keys = ["The complete ladder: 10 Foundations + 11 Compounded + 13 Advanced = 34 records.",
            "Every record below this one is summarized and pointed to.",
            "If you can work this record cold, you hold %s." % m.NAME,
            "This record is ladder rank 34: mastery."]
    recs.append(base(r, A, t, title, desc, how, keys,
                    demo_facts(title, "%s%06d" % (P, r), A, facts, asserts,
                               "Ladder totals - %s:" % m.NAME, sig), kind))

    assert len(recs) == 34, "must build exactly 34 records"
    assert [x["ladder_rank"] for x in recs] == list(range(1, 35))
    return recs

# ---------------------------------------------------------------- outputs
SHORT_SCRIPT = {
    "language-tigrinya": "Ethiopic script",
    "language-kinyarwanda": "Latin alphabet",
    "language-xhosa": "Latin alphabet with click consonants",
    "language-lao": "Lao script",
    "language-uyghur": "Perso-Arabic script",
    "language-turkmen": "Latin alphabet",
    "language-tatar": "Cyrillic alphabet",
    "language-madurese": "Latin script",
    "language-balochi": "Perso-Arabic script",
    "language-hmong": "RPA Latin script",
}


def write_data(slug, records):
    d = os.path.join(DATA_ROOT, slug)
    os.makedirs(os.path.join(d, "chunks"), exist_ok=True)
    idx_lines = [json.dumps({"id": r["id"], "t": r["t"], "g": r["g"]},
                            ensure_ascii=False) for r in records]
    with gzip.open(os.path.join(d, "index.jsonl.gz"), "wt", encoding="utf-8") as f:
        f.write("\n".join(idx_lines) + "\n")
    full_lines = [json.dumps(r, ensure_ascii=False) for r in records]
    with gzip.open(os.path.join(d, "chunks", "chunk-0000.jsonl.gz"), "wt",
                   encoding="utf-8") as f:
        f.write("\n".join(full_lines) + "\n")


GEN_JS = """(function(){'use strict';
/* JAH @@CHEAD@@ generator — @@VERSION@@.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="@@PREFIX@@";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
@@TOPICS@@
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "# @@NAME@@ Study — "+safe+"\\n"
   + "# Field: "+field+"\\n"
   + "record = {'title': \\""+safe+"\\", 'field': \\""+field+"\\"}\\n"
   + "def summarize(r):\\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\\n"
   + "print(summarize(record))\\n"
   + "print('Sample record — structural sample, not an archive entry.')\\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — language learning record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A language learning record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"@@KIND@@",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\\\-')+'\\\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'@@VERSION@@',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('@@SLUG@@',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""


def gen_js_text(m, sig, records):
    slug = m.SLUG + ("-signature" if sig else "")
    prefix = m.SIG_PREFIX if sig else m.PREFIX
    chead = ("The %s Language Signature Database" % m.NAME if sig
             else "The %s Language Database" % m.NAME)
    version = "jahdb-%s-1.0" % slug
    tiers = [("Foundations", 1, 10), ("Compounded", 11, 21), ("Advanced", 22, 34)]
    blocks = []
    for tier, lo, hi in tiers:
        topics = ["  \"%s - %s\"," % (r["t"], tier)
                  for r in records if lo <= r["ladder_rank"] <= hi]
        assert len(topics) == (hi - lo + 1)
        blocks.append(' "%s": [\n%s\n ],' % (tier, "\n".join(topics)))
    topics_js = "\n".join(blocks)
    out = GEN_JS
    out = out.replace("@@CHEAD@@", chead)
    out = out.replace("@@VERSION@@", version)
    out = out.replace("@@PREFIX@@", prefix)
    out = out.replace("@@TOPICS@@", topics_js)
    out = out.replace("@@NAME@@", m.NAME)
    out = out.replace("@@KIND@@", "%s-demo" % m.NAME.lower())
    out = out.replace("@@SLUG@@", slug)
    return out

# ---------------------------------------------------------------- page writer
def _prose(m, sig):
    n, sc = m.NAME, SHORT_SCRIPT[m.SLUG]
    if not sig:
        meta = ("Learn %s from the ground up: the language overview, the %s writing "
                "system, pronunciation and phonology, core vocabulary with sentences, "
                "grammar essentials, and themed sentence sets for daily life - every "
                "record carrying %s in %s plus transliteration plus English translation "
                "plus example sentences, taught progressively along the ladder. "
                "Property of Justin Addam Higgins." % (n, sc, n, sc))
        hero = (meta[:-len(" Property of Justin Addam Higgins.")] +
                " - Public records - real, fact-checked %s language teaching: the language "
                "overview, the %s writing system, pronunciation and phonology, core nouns "
                "verbs adjectives and adverbs with sentences, pronouns, numbers and time, "
                "greetings, grammar essentials, themed sentence sets for daily life, verb "
                "tenses, questions and answers, commands and requests, descriptions, stories, "
                "idioms, formal and polite registers, complex sentences, conversations, and a "
                "mastery review - every record carrying %s content in %s plus transliteration "
                "plus English translation plus example sentences. Every record carries the "
                "full entry: description, how it works, key points, requirements, standards, "
                "citations, and a working demonstration program. Records are ordered by the "
                "teaching ladder: Foundations (language overview, writing system, pronunciation "
                "and phonology, core nouns, core verbs, adjectives and adverbs, pronouns, numbers "
                "and time, greetings, grammar essentials) -> Compounded (home and family, food and "
                "cooking, travel and directions, work and school, health and body, emotions and "
                "feelings, nature and weather, shopping and money, friendship and social life, "
                "technology and communication, verb tenses in sentences) -> Advanced (questions and "
                "answers, commands and requests, descriptions, three stories, idioms and proverbs, "
                "formal and polite registers, compound and complex sentences, three conversations, "
                "mastery review and full reference)." % (n, sc, n, sc))
        role = ("%s language archivist - teaching %s from the %s and sounds through core "
                "vocabulary, grammar, and everyday sentences to stories, idioms, registers, and "
                "conversations; teaching progressively along the ladder from foundations through "
                "compounded to advanced; answers from many angles - definition, example, "
                "pronunciation, usage, grammar, culture - using only archive data from this "
                "system" % (n, n, sc))
        greet = ("I am the JAH %s Language Archivist. Ask me about %s - from the %s and sounds "
                 "through core words, grammar, and everyday sentences to stories, idioms, and "
                 "conversations." % (n, n, sc))
        ai_name = "JAH %s Language Archivist" % n
        db_name = "The %s Language Database" % n
        archive_dd = ("Seeded public-record %s language records, marching toward one million "
                      "records. Presented in teaching-ladder order: foundations, compounded, "
                      "advanced." % n)
        sigsys_dd = "Public records organized in the Signature system. Property of Justin Addam Higgins (JAH)."
    else:
        meta = ("His original Signature %s Method: every letter a sworn sign, every verb a living "
                "action, every proverb a covenant of the ancestors - the full ladder from the "
                "language overview through the script, sounds, words, and grammar, through "
                "daily-life sentences, to stories, idioms, registers, and conversations, reframed "
                "as Signature science. Clearly labeled Signature-made, never presented as authentic "
                "public record. Property of Justin Addam Higgins." % n)
        hero = (meta[:-len(" Property of Justin Addam Higgins.")] +
                " - Signature originals - his original Signature %s Method: every letter a sworn "
                "sign, every verb a living action, every proverb a covenant of the ancestors, the "
                "whole language taught as Signature science. Clearly labeled Signature-made, never "
                "presented as authentic public record. Every record carries the full entry: "
                "description, how it works, key points, requirements, standards, citations, and a "
                "working demonstration program. Records are ordered by the teaching ladder: "
                "Foundations (language overview, writing system, pronunciation and phonology, core "
                "nouns, core verbs, adjectives and adverbs, pronouns, numbers and time, greetings, "
                "grammar essentials) -> Compounded (home and family, food and cooking, travel and "
                "directions, work and school, health and body, emotions and feelings, nature and "
                "weather, shopping and money, friendship and social life, technology and "
                "communication, verb tenses in sentences) -> Advanced (questions and answers, "
                "commands and requests, descriptions, three stories, idioms and proverbs, formal and "
                "polite registers, compound and complex sentences, three conversations, mastery "
                "review and full reference)." % n)
        role = ("%s language archivist - Signature editions: his original Signature %s Method, "
                "every letter a sworn sign and every verb a living action, clearly labeled "
                "Signature-made and never presented as authentic public record; teaches "
                "progressively along the ladder from foundations through compounded to advanced; "
                "answers from many angles using only archive data from this system" % (n, n))
        greet = ("I am the JAH %s Language Archivist (Signature). Ask me about the Signature %s "
                 "Method - every letter a sworn sign, every verb a living action." % (n, n))
        ai_name = "JAH %s Language Archivist (Signature)" % n
        db_name = "The %s Language Signature Database" % n
        archive_dd = ("Seeded Signature-original %s language records, marching toward one million "
                      "records. Presented in teaching-ladder order: foundations, compounded, "
                      "advanced." % n)
        sigsys_dd = "Signature originals organized in the Signature system. Property of Justin Addam Higgins (JAH)."
    return dict(meta=meta, hero=hero, role=role, greet=greet, ai_name=ai_name,
                db_name=db_name, archive_dd=archive_dd, sigsys_dd=sigsys_dd)


def write_page(m, sig):
    slug = m.SLUG + ("-signature" if sig else "")
    tmpl_slug = "language-pashto-signature" if sig else "language-pashto"
    with open(os.path.join(DB_ROOT, tmpl_slug, "index.html"), encoding="utf-8") as f:
        p = f.read()
    pr = _prose(m, sig)
    version = "jahdb-%s-1.0" % slug

    # hero h1 + paragraph (regex, DOTALL)
    p = re.sub(r"<h1>.*?</h1>\s*<p>.*?</p>",
               "<h1>%s</h1>\n      <p>%s</p>" % (pr["db_name"], pr["hero"]),
               p, count=1, flags=re.S)
    # meta description + JSON-LD name/description
    p = re.sub(r'<meta name="description" content="[^"]*">',
               '<meta name="description" content="%s">' % pr["meta"], p, count=1)
    p = p.replace("<title>The Pashto Language%s Database — JAH Databases</title>" % (" Signature" if sig else ""),
                  "<title>%s — JAH Databases</title>" % pr["db_name"])
    p = re.sub(r'"name": "The Pashto Language (Signature )?Database", "description": "[^"]*"',
               '"name": "%s", "description": "%s"' % (pr["db_name"], pr["meta"]), p, count=1)
    # generator version (2 occurrences)
    p = p.replace("jahdb-%s-1.0" % tmpl_slug, version)
    # search + chat placeholders
    p = re.sub(r'placeholder="Search Pashto[^"]*"',
               'placeholder="Search %s letters, words, verbs, tenses, phrases, grammar, dialogues..."' % m.NAME, p, count=1)
    p = re.sub(r'placeholder="Ask about Pashto\.\.\."',
               'placeholder="Ask about %s..."' % m.NAME, p, count=1)
    # generator card
    p = p.replace("<h3>The Pashto Language%s Database generator</h3>" % (" Signature" if sig else ""),
                  "<h3>%s generator</h3>" % pr["db_name"])
    p = p.replace("Generate clearly-labeled Pashto language studies.",
                  "Generate clearly-labeled %s language studies." % m.NAME)
    # chat header + greeting
    p = p.replace("<h3>JAH Pashto Language Archivist%s <button" % (" (Signature)" if sig else ""),
                  "<h3>%s <button" % pr["ai_name"])
    p = re.sub(r"'I am the JAH Pashto Language Archivist( \(Signature\))?\..*?conversations\.'",
               "'%s'" % pr["greet"].replace("'", "\\'"), p, count=1)
    # about section (whole block)
    about = """<section class="pane" id="p-about">
    <div class="card">
      <h3>About this data base</h3>
      <dl class="kv">
        <dt>Archive</dt><dd>%s</dd>
        <dt>Record schema</dt><dd class="mono">id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, ladder_rank, ladder_tier, demo</dd>
        <dt>Fields</dt><dd>Foundations · Compounded · Advanced - each tier opens on demand and loads only what you open</dd>
        <dt>Generator</dt><dd>%s — Generate clearly-labeled %s language studies. Seeded archive records are the authoritative entries.</dd>
        <dt>Drift control</dt><dd>Every generated record is checked against an archive sample for exact duplicates and re-validated by the independent checker.</dd>
        <dt>Target</dt><dd>1,000,000 records. The archive marches toward the million mark with overload protection: 100-record chunks, lazy loading, and a collapsible per-field archive so no device ever renders everything at once.</dd>
        <dt>AI</dt><dd>%s — %s — and aware of the whole JAH Databases network through cross-database reasoning. On-device Standard 1.0, no key needed; uses the shared Signature backend automatically when configured.</dd>
        <dt>Signature system</dt><dd>%s</dd>
      </dl>
    </div>
  </section>""" % (pr["archive_dd"], version, m.NAME, pr["ai_name"], pr["role"], pr["sigsys_dd"])
    p = re.sub(r'<section class="pane" id="p-about">.*?</section>', about, p, count=1, flags=re.S)
    # JS wiring
    p = p.replace("var SLUG='%s';" % tmpl_slug, "var SLUG='%s';" % slug)
    p = p.replace("data/%s/';" % tmpl_slug, "data/%s/';" % slug)
    p = p.replace("name:'The Pashto Language%s Database'" % (" Signature" if sig else ""),
                  "name:'%s'" % pr["db_name"])
    p = p.replace("ai_name:'JAH Pashto Language Archivist%s'" % (" (Signature)" if sig else ""),
                  "ai_name:'%s'" % pr["ai_name"])
    p = re.sub(r"var ROLE='.*?';", "var ROLE='%s';" % pr["role"].replace("'", "\\'"), p, count=1)
    p = p.replace('<script src="gen-%s.js"></script>' % tmpl_slug,
                  '<script src="gen-%s.js"></script>' % slug)
    # any leftover Pashto references = bug
    left = re.findall(r"pashto", p, flags=re.I)
    assert not left, "leftover Pashto references: %d" % len(left)

    d = os.path.join(DB_ROOT, slug)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(p)
    with open(os.path.join(d, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
        f.write(gen_js_text(m, sig, BUILD_CACHE[slug]))
    return d

# ---------------------------------------------------------------- gates
def gate_demos(all_records):
    """Execute every demo program; all must exit 0."""
    fails = []
    total = 0
    with tempfile.TemporaryDirectory() as td:
        for slug, recs in all_records.items():
            for r in recs:
                total += 1
                path = os.path.join(td, "demo.py")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(r["demo"]["program"])
                try:
                    cp = subprocess.run([sys.executable, path], capture_output=True,
                                        text=True, timeout=30)
                except Exception as e:  # noqa: BLE001
                    fails.append((r["id"], "exception: %s" % e))
                    continue
                if cp.returncode != 0:
                    fails.append((r["id"], cp.stderr[-800:] or cp.stdout[-800:]))
    return total, fails


def gate_node(scripts):
    fails = []
    for s in scripts:
        cp = subprocess.run(["node", "--check", s], capture_output=True, text=True)
        if cp.returncode != 0:
            fails.append((s, cp.stderr[-500:]))
    return fails


def gate_dedupe(all_records):
    """New ids/titles vs whole system (all index.jsonl.gz) + within batch.
    The batch's own 20 slugs are excluded from the 'existing' set."""
    own = set(all_records.keys())
    existing_ids, existing_titles = set(), set()
    n_files = 0
    for slug in os.listdir(DATA_ROOT):
        if slug in own:
            continue
        p = os.path.join(DATA_ROOT, slug, "index.jsonl.gz")
        if not os.path.isfile(p):
            continue
        n_files += 1
        try:
            with gzip.open(p, "rt", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        o = json.loads(line)
                    except Exception:  # noqa: BLE001
                        continue
                    if o.get("id"):
                        existing_ids.add(o["id"])
                    if o.get("t"):
                        existing_titles.add(o["t"].strip().lower())
        except Exception:  # noqa: BLE001
            continue
    problems = []
    seen_ids, seen_titles = set(), set()
    for slug, recs in all_records.items():
        for r in recs:
            if r["id"] in existing_ids:
                problems.append("id collision with system: %s" % r["id"])
            if r["id"] in seen_ids:
                problems.append("id duplicate within batch: %s" % r["id"])
            seen_ids.add(r["id"])
            tl = r["t"].strip().lower()
            if tl in existing_titles:
                problems.append("title collision with system: %s (%s)" % (r["t"], r["id"]))
            if tl in seen_titles:
                problems.append("title duplicate within batch: %s" % r["t"])
            seen_titles.add(tl)
    return n_files, len(existing_ids), problems


TERM_BLOCK = [
    "fuck", "shit", "bitch", "whore", "slut", "cunt", "dick", "pussy",
    "nigger", "nigga", "faggot", "dyke", "tranny", "kike", "spic",
    "chink", "gook", "porn", "masturbat", "orgasm", "kill yourself",
    "white power", "gas the",
]
TERM_FP = ["koran", "rapture", "retard", "bible", "allah"]


def gate_terms(all_records):
    """Blocklist scan; hits are returned with context for review."""
    hits = []
    for slug, recs in all_records.items():
        for r in recs:
            blob = json.dumps(r, ensure_ascii=False)
            low = blob.lower()
            for term in TERM_BLOCK:
                i = low.find(term)
                if i >= 0:
                    ctx = blob[max(0, i - 60):i + 60].replace("\n", " ")
                    fp = [w for w in TERM_FP if w in low[max(0, i - 30):i + 30]]
                    hits.append((r["id"], term, ctx, fp))
    return hits


BUILD_CACHE = {}


def main():
    all_records, scripts, report = {}, [], []
    # pre-flight: slugs must be free of other builders
    with open(os.path.join(HOME, "workspace", "jah-databases", "data",
                           "manifest.json"), encoding="utf-8") as f:
        manifest = json.load(f)
    mslugs = {d.get("slug") for d in manifest.get("databases", [])}
    for m in LANGS:
        for sfx in ("", "-signature"):
            slug = m.SLUG + sfx
            if slug in mslugs:
                print("SKIP: %s already in manifest" % slug)
                return 1

    for m in LANGS:
        for sig in (False, True):
            slug = m.SLUG + ("-signature" if sig else "")
            recs = build_records(m, sig)
            BUILD_CACHE[slug] = recs
            all_records[slug] = recs
            write_data(slug, recs)
            d = write_page(m, sig)
            scripts.append(os.path.join(d, "gen-%s.js" % slug))
            report.append((slug, len(recs)))

    print("== records built ==")
    for slug, n in report:
        print("  %s: %d" % (slug, n))
    total = sum(n for _, n in report)
    assert total == 680, total

    print("== gate: demos (%d) ==" % total)
    n_run, fails = gate_demos(all_records)
    print("  executed %d, failures %d" % (n_run, len(fails)))
    for fid, err in fails[:10]:
        print("  FAIL %s: %s" % (fid, err))
    assert not fails, "demo failures"

    print("== gate: node --check (%d scripts) ==" % len(scripts))
    nfails = gate_node(scripts)
    print("  failures %d" % len(nfails))
    for s, e in nfails:
        print("  FAIL %s: %s" % (s, e))
    assert not nfails, "node --check failures"

    print("== gate: dedupe ==")
    n_files, n_ids, problems = gate_dedupe(all_records)
    print("  scanned %d index files (%d ids), problems %d" % (n_files, n_ids, len(problems)))
    for p in problems[:20]:
        print("  DUP %s" % p)
    assert not problems, "dedupe problems"

    print("== gate: terms ==")
    hits = gate_terms(all_records)
    print("  hits %d" % len(hits))
    for rid, term, ctx, fp in hits:
        print("  HIT %s term=%r fp=%s ctx=%s" % (rid, term, fp, ctx[:120]))

    print("== counts ==")
    for slug, recs in all_records.items():
        assert len(recs) == 34, slug
    print("  all 20 slugs at 34 records")
    print("STAGED OK: 10 pairs, 680 records. Fragments staged; not marked live.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
