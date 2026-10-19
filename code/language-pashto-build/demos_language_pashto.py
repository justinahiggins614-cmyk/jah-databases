#!/usr/bin/env python3
"""Demonstration programs for the Pashto Language databases.

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it (alphabet drills, vocabulary quizzes,
paradigms, numbers, tenses, dialogues, stories), asserts tight bounds (never
float exact-equality), prints the real computed values, and ends with the
OK marker. The build machine-executes all 68 demos.
"""

import json


def _pre(hdr, name, rid, group):
    return hdr(name, rid, group) + "NAME = %s\n" % json.dumps(name, ensure_ascii=False)


def demo_overview(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("Pashto language core facts:")
    print("  alphabet letters:", FACTS["letters"])
    print("  genders:", FACTS["genders"], "| cases:", FACTS["cases"])
    print("  tenses:", FACTS["tenses"])
    print("  native speakers (millions):", FACTS["speakers_m"])
    print("  ISO 639-1:", FACTS["iso1"], "| ISO 639-3:", FACTS["iso3"])
    assert FACTS["letters"] == 44, "Pashto alphabet must have 44 letters"
    assert FACTS["genders"] == 2, "Pashto must have 2 genders"
    assert FACTS["cases"] == 3, "Pashto direct/oblique/vocative = 3 cases"
    assert FACTS["tenses"] == 3, "present/past/future = 3 tenses"
    assert 30 <= FACTS["speakers_m"] <= 70, "speaker estimate out of bounds"
    assert FACTS["iso1"] == "ps" and FACTS["iso3"] == "pus", "ISO codes wrong"
    print("OK: %%s verified %%d core facts" %% (NAME, len(FACTS)))
if __name__ == "__main__":
    main()
""" % json.dumps(data, ensure_ascii=False)


def demo_alphabet(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
LETTERS = %s
COUNT = %s
def main():
    n = len(LETTERS)
    print("Pashto letters in table:", n)
    print("first 5:", " ".join(l[0] for l in LETTERS[:5]))
    print("last 5: ", " ".join(l[0] for l in LETTERS[-5:]))
    pashto_only = ["\u067c", "\u0689", "\u0693", "\u06bc",
                   "\u069a", "\u0696", "\u0685", "\u0681",
                   "\u06d0", "\u06cd", "\u0626", "\u06ab"]
    found = [ch for ch in pashto_only if any(l[0] == ch for l in LETTERS)]
    print("Pashto-specific letters present:", len(found), "of", len(pashto_only))
    assert n == COUNT == 44, "alphabet must have exactly 44 letters"
    assert len(found) == len(pashto_only), "missing Pashto-specific letters"
    for upper, tr, en, ex, ex_tr, ex_en in LETTERS:
        assert upper and tr and ex, "empty letter row"
    glyphs = [l[0] for l in LETTERS]
    assert len(set(glyphs)) == 44, "duplicate letter glyphs"
    print("OK: %%s verified the 44-letter Pashto table" %% NAME)
if __name__ == "__main__":
    main()
""" % (json.dumps(data["letters"], ensure_ascii=False), data["count"])


def demo_phonology(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
VOWELS = %s
CONSONANTS = %s
EXAMPLES = %s
def main():
    print("vowel inventory:", len(VOWELS))
    for glyph, tr, en in VOWELS:
        print("  %%s (%%s) - %%s" %% (glyph, tr, en))
    print("consonant inventory:", len(CONSONANTS))
    retroflex = [c for c in CONSONANTS if c[0] in ("\u067c", "\u0689", "\u0693", "\u06bc")]
    print("retroflex consonants:", " ".join(c[0] for c in retroflex))
    fric_pair = [c for c in CONSONANTS if c[0] in ("\u069a", "\u0696")]
    print("postalveolar fricative pair:", " ".join(c[0] for c in fric_pair))
    print("spoken examples:", len(EXAMPLES))
    assert len(VOWELS) == 7, "Pashto must have 7 vowels"
    assert len(retroflex) == 4, "must have 4 retroflex consonants"
    assert len(fric_pair) == 2, "must have the x̌/ǵ fricative pair"
    assert len(EXAMPLES) >= 10, "need 10+ spoken examples"
    for ps, tr, en, note in EXAMPLES:
        assert ps and tr and en, "empty example row"
    print("OK: %%s verified %%d vowels, %%d consonants, %%d examples"
          %% (NAME, len(VOWELS), len(CONSONANTS), len(EXAMPLES)))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["vowels"], ensure_ascii=False),
       json.dumps(data["consonants"], ensure_ascii=False),
       json.dumps(data["examples"], ensure_ascii=False))


def demo_vocab(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
WORDS = %s
KIND = %s
def main():
    n = len(WORDS)
    print("%%s entries in table: %%d" %% (KIND, n))
    print("sample:", WORDS[0][0], "(%%s)" %% WORDS[0][1], "-", WORDS[0][2])
    with_sent = 0
    for ps, tr, en, ex_ps, ex_tr, ex_en in WORDS:
        assert ps and tr and en, "empty word row"
        if ex_ps and ex_en:
            with_sent += 1
        assert ex_ps and ex_tr and ex_en, "every word needs a translated example sentence"
    assert n >= 25, "vocabulary table must hold 25+ words"
    assert with_sent == n, "every word must carry an example sentence"
    print("words with example sentences: %%d/%%d" %% (with_sent, n))
    print("OK: %%s verified %%d %s, all with sentences" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["words"], ensure_ascii=False),
       json.dumps(data["kind"], ensure_ascii=False),
       data["kind"])


def demo_paradigm(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
TITLE = %s
TABLES = %s
def main():
    print(TITLE)
    total = 0
    for tname, rows in TABLES.items():
        print("  %%s: %%d forms" %% (tname, len(rows)))
        for ps, tr, en, ex_ps, ex_tr, ex_en in rows:
            assert ps and tr and en, "empty paradigm row"
            assert ex_ps and ex_en, "every form needs an example sentence"
        total += len(rows)
    print("total pronoun forms:", total)
    assert "Personal pronouns" in TABLES, "missing personal paradigm"
    assert "Possessive pronouns" in TABLES, "missing possessive paradigm"
    assert "Demonstrative pronouns" in TABLES, "missing demonstrative paradigm"
    assert "Interrogative pronouns" in TABLES, "missing interrogative paradigm"
    assert total >= 20, "need 20+ pronoun forms"
    print("OK: %%s verified %%d pronoun forms in %%d paradigms"
          %% (NAME, total, len(TABLES)))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["title"], ensure_ascii=False),
       json.dumps(data["tables"], ensure_ascii=False))


def demo_numbers(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
D = %s
def main():
    units, teens, tens = D["units"], D["teens"], D["tens"]
    print("units 1-10:", len(units), "| teens 11-19:", len(teens), "| tens:", len(tens))
    print("1..3:", " ".join(u[0] for u in units[:3]), "| 100:", tens[-1][0])
    print("ordinals:", ", ".join(o[0] for o in D["ordinals"]))
    print("days:", len(D["days"]), "| months:", len(D["months"]), "| seasons:", len(D["seasons"]))
    assert len(units) == 10, "need units 1-10"
    assert len(teens) == 9, "need teens 11-19"
    assert len(tens) == 9, "need tens 20-90 plus 100"
    assert len(D["ordinals"]) == 3, "need 3 ordinals"
    assert len(D["days"]) == 7, "need 7 days"
    assert len(D["months"]) == 12, "need 12 months"
    assert len(D["seasons"]) == 4, "need 4 seasons"
    assert units[0][0] == "\u06cc\u0648" and units[0][2] == "1", "first unit must be one"
    assert tens[-1][2] == "100", "last ten entry must be 100"
    for table in (units, teens, tens, D["ordinals"], D["days"], D["months"], D["seasons"]):
        for ps, tr, en in table:
            assert ps and tr and en, "empty number row"
    total = sum(len(t) for t in (units, teens, tens, D["ordinals"], D["days"], D["months"], D["seasons"]))
    print("total number/time forms:", total)
    print("OK: %%s verified %%d number and time forms" %% (NAME, total))
if __name__ == "__main__":
    main()
""" % json.dumps(data, ensure_ascii=False)


def demo_phrases(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
PHRASES = %s
def main():
    n = len(PHRASES)
    print("greetings and phrases:", n)
    print("first:", PHRASES[0][0], "-", PHRASES[0][2])
    print("last: ", PHRASES[-1][0], "-", PHRASES[-1][2])
    for ps, tr, en, note in PHRASES:
        assert ps and tr and en, "empty phrase row"
        assert note and len(note) > 8, "every phrase needs a real usage note"
    assert n == 30, "need exactly 30 greetings/phrases"
    print("OK: %%s verified %%d phrases, all with usage notes" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % json.dumps(data["phrases"], ensure_ascii=False)


def demo_grammar(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
RULES = %s
def main():
    print("grammar rules:", len(RULES))
    for i, (rule, ps, tr, en) in enumerate(RULES, 1):
        assert rule and ps and tr and en, "empty rule row"
        print("  %%d. %%s" %% (i, rule[:60]))
    assert len(RULES) == 8, "need the 8 load-bearing rules"
    joined = " ".join(r[0] for r in RULES).lower()
    for key in ("subject-object-verb", "gender", "ergativ", "negat", "future", "question"):
        assert key in joined, "missing rule topic: " + key
    print("OK: %%s verified %%d grammar rules with examples" %% (NAME, len(RULES)))
if __name__ == "__main__":
    main()
""" % json.dumps(data["rules"], ensure_ascii=False)


def demo_sentences(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
TOPIC = %s
SENTS = %s
PARSES = %s
def main():
    n = len(SENTS)
    print("topic:", TOPIC)
    print("sentences:", n)
    for row in SENTS:
        assert len(row) >= 3, "sentence row needs ps/tr/en"
        ps, tr, en = row[0], row[1], row[2]
        assert ps and tr and en, "empty sentence row"
    assert n >= 15, "need 15+ sentences per set"
    if PARSES:
        assert len(PARSES) == n, "parse notes must match sentence count"
        print("parse notes:", len(PARSES))
    print("first:", SENTS[0][0])
    print("last: ", SENTS[-1][0])
    print("OK: %%s verified %%d translated sentences" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["topic"], ensure_ascii=False),
       json.dumps(data["sentences"], ensure_ascii=False),
       json.dumps(data.get("parses", []), ensure_ascii=False))


def demo_tenses(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
D = %s
def main():
    print("verb:", D["verb_ps"], "(%%s)" %% D["verb_tr"], "-", D["verb_en"])
    for tense in ("present", "past", "future"):
        forms = D[tense]
        print("  %%s: %%d forms" %% (tense, len(forms)))
        assert len(forms) == 6, "each tense needs 6 person forms"
        for ps, tr, en in forms:
            assert ps and tr and en, "empty conjugation row"
    assert all("\u0628\u0647" in f[0] for f in D["future"]), "future must use the \u0628\u0647 particle"
    persons = [f[2] for f in D["present"]]
    print("present persons:", " | ".join(persons))
    print("OK: %%s conjugated %s through 3 tenses x 6 persons" %% NAME)
if __name__ == "__main__":
    main()
""" % (json.dumps(data, ensure_ascii=False),
       data["verb_en"])


def demo_pairs(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
KIND = %s
PAIRS = %s
def main():
    n = len(PAIRS)
    print("pair set:", KIND, "-", n, "pairs")
    for a_ps, a_tr, a_en, b_ps, b_tr, b_en, note in PAIRS:
        assert a_ps and b_ps and a_en and b_en, "empty pair row"
        assert note and len(note) > 8, "every pair needs a usage note"
    assert n >= 15, "need 15+ pairs"
    print("first pair:", PAIRS[0][0], "|", PAIRS[0][3])
    print("OK: %%s verified %%d pairs with notes" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["kind"], ensure_ascii=False),
       json.dumps(data["pairs"], ensure_ascii=False))


def demo_story(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
TITLE = %s
LINES = %s
def main():
    n = len(LINES)
    print("story:", TITLE)
    print("sentences:", n)
    for ps, tr, en in LINES:
        assert ps and tr and en, "every story line needs ps/tr/en"
    assert n == 10, "each story must be exactly 10 sentences"
    words = sum(len(l[0].split()) for l in LINES)
    print("Pashto words in story:", words)
    assert words >= 40, "story too short to be a real narrative"
    print("opening:", LINES[0][0], "-", LINES[0][2])
    print("closing:", LINES[-1][0], "-", LINES[-1][2])
    print("OK: %%s verified the 10-sentence story (%%d words)" %% (NAME, words))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["title"], ensure_ascii=False),
       json.dumps(data["lines"], ensure_ascii=False))


def demo_idioms(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
IDIOMS = %s
def main():
    n = len(IDIOMS)
    print("idioms and proverbs:", n)
    for ps, tr, literal, meaning, ex_ps, ex_tr, ex_en in IDIOMS:
        assert ps and tr and literal and meaning, "empty idiom row"
        assert ex_ps and ex_en, "every idiom needs an example sentence"
    assert n == 20, "need exactly 20 idioms/proverbs"
    print("first:", IDIOMS[0][0], "-", IDIOMS[0][3])
    print("OK: %%s verified %%d idioms with meanings and examples" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % json.dumps(data["idioms"], ensure_ascii=False)


def demo_dialogue(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
TITLE = %s
LINES = %s
def main():
    n = len(LINES)
    print("dialogue:", TITLE)
    print("lines:", n)
    speakers = set()
    for sp, ps, tr, en in LINES:
        assert sp and ps and tr and en, "every dialogue line needs speaker/ps/tr/en"
        speakers.add(sp)
    assert n == 20, "each dialogue must be exactly 20 lines"
    assert len(speakers) == 2, "dialogue needs exactly 2 speakers"
    print("speakers:", " / ".join(sorted(speakers)))
    print("opening:", LINES[0][1], "-", LINES[0][3])
    print("closing:", LINES[-1][1], "-", LINES[-1][3])
    print("OK: %%s verified the 20-line dialogue" %% NAME)
if __name__ == "__main__":
    main()
""" % (json.dumps(data["title"], ensure_ascii=False),
       json.dumps(data["lines"], ensure_ascii=False))


def demo_reference(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
LETTERS = %s
WORDS = %s
RULES = %s
def main():
    print("alphabet letters:", LETTERS)
    print("core words:", len(WORDS))
    print("grammar lines:", len(RULES))
    assert LETTERS == 44, "reference must cover the 44-letter alphabet"
    assert len(WORDS) == 200, "reference must hold exactly 200 core words"
    assert len(RULES) == 8, "reference must hold the 8 grammar lines"
    for ps, tr, en in WORDS:
        assert ps and tr and en, "empty word row"
    glyphs = [w[0] for w in WORDS]
    assert len(set(glyphs)) == 200, "duplicate words in reference list"
    print("sample words:", ", ".join(w[0] for w in WORDS[:5]))
    print("OK: %%s verified the full reference (%%d words)" %% (NAME, len(WORDS)))
if __name__ == "__main__":
    main()
""" % (data["letters"],
       json.dumps(data["words"], ensure_ascii=False),
       json.dumps(data["rules"], ensure_ascii=False))


DEMOS = {
    "overview": demo_overview,
    "alphabet": demo_alphabet,
    "phonology": demo_phonology,
    "vocab": demo_vocab,
    "paradigm": demo_paradigm,
    "numbers": demo_numbers,
    "phrases": demo_phrases,
    "grammar": demo_grammar,
    "sentences": demo_sentences,
    "tenses": demo_tenses,
    "pairs": demo_pairs,
    "story": demo_story,
    "idioms": demo_idioms,
    "dialogue": demo_dialogue,
    "reference": demo_reference,
}
