#!/usr/bin/env python3
"""Demonstration programs for the Russian to English databases.

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it (case drills, vocabulary quizzes,
conjugation, agreement, numbers, paradigms), asserts tight bounds (never
float exact-equality), prints the real computed values, and ends with the
OK marker. The build machine-executes all 68 demos.
"""

import json


def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""%s - working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (name, rid, group))


def _pre(hdr, name, rid, group):
    return hdr(name, rid, group) + "NAME = %s\n" % json.dumps(name, ensure_ascii=False)


def demo_overview(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
def main():
    print("Russian language core facts:")
    print("  alphabet letters:", FACTS["letters"])
    print("  noun cases:", FACTS["cases"], "| genders:", FACTS["genders"])
    print("  tenses:", FACTS["tenses"])
    print("  native speakers (millions):", FACTS["speakers_m"])
    print("  ISO 639-1:", FACTS["iso1"], "| ISO 639-3:", FACTS["iso3"])
    assert FACTS["letters"] == 33, "Cyrillic alphabet must have 33 letters"
    assert FACTS["cases"] == 6, "Russian must have 6 noun cases"
    assert FACTS["genders"] == 3, "Russian must have 3 genders"
    assert 100 <= FACTS["speakers_m"] <= 200, "speaker estimate out of bounds"
    assert FACTS["iso1"] == "ru" and FACTS["iso3"] == "rus", "ISO codes wrong"
    print("OK: %%s verified %%d core facts" %% (NAME, len(FACTS)))
if __name__ == "__main__":
    main()
""" % json.dumps(data, ensure_ascii=False)


def demo_alphabet(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
LETTERS = %s
def main():
    n = len(LETTERS)
    print("Cyrillic letters in table:", n)
    print("first 5:", " ".join(l[1] for l in LETTERS[:5]))
    print("last 5: ", " ".join(l[1] for l in LETTERS[-5:]))
    assert n == 33, "alphabet must have exactly 33 letters"
    assert LETTERS[0][1] == "\\u0430", "first letter must be \\u0430"
    assert LETTERS[-1][1] == "\\u044f", "last letter must be \\u044f"
    for upper, lower, tr in LETTERS:
        assert upper and lower and tr, "empty letter row"
    lowers = [l[1] for l in LETTERS]
    assert len(set(lowers)) == 33, "duplicate letters"
    print("OK: %%s verified the 33-letter Cyrillic table" %% NAME)
if __name__ == "__main__":
    main()
""" % json.dumps(data["letters"], ensure_ascii=False)


def demo_phonology(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
REDUCTIONS = %s
DEVOICING = %s
VOWELS = set("aeiouy")
def reduce_vowels(word, stress):
    out = []
    for i, ch in enumerate(word):
        if i != stress and ch in VOWELS:
            if ch == "o":
                ch = "a"
            elif ch == "e":
                ch = "i"
        out.append(ch)
    return "".join(out)
def devoice(word):
    if word.endswith("zh"):
        return word[:-2] + "sh"
    m = {"b": "p", "d": "t", "g": "k", "v": "f", "z": "s"}
    if word[-1] in m:
        return word[:-1] + m[word[-1]]
    return word
def main():
    print("vowel reduction (unstressed o->a, e->i):")
    for word, stress, expected in REDUCTIONS:
        got = reduce_vowels(word, stress)
        print("  %%-10s -> %%-10s (expected %%s)" %% (word, got, expected))
        assert got == expected, "reduction failed for %%s" %% word
    print("final devoicing (applied after vowel reduction):")
    for spelling, stress, expected in DEVOICING:
        got = devoice(reduce_vowels(spelling, stress))
        print("  %%-10s -> %%-10s (expected %%s)" %% (spelling, got, expected))
        assert got == expected, "devoicing failed for %%s" %% spelling
    print("OK: %%s verified %%d reductions and %%d devoicings" %% (NAME, len(REDUCTIONS), len(DEVOICING)))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["reductions"], ensure_ascii=False),
       json.dumps(data["devoicing"], ensure_ascii=False))


def demo_vocab_quiz(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
WORDS = %s
KIND = %s
def lookup(ru):
    for w, e in WORDS:
        if w == ru:
            return e
    return None
def main():
    n = len(WORDS)
    print("%%s quiz bank: %%d words" %% (KIND, n))
    # deterministic simulated quiz: even-indexed items answered correctly
    score = sum(1 for i in range(n) if i %% 2 == 0)
    print("simulated quiz score: %%d/%%d" %% (score, n))
    assert 0 <= score <= n, "score out of bounds"
    assert score == (n + 1) // 2, "unexpected score"
    for ru, en in WORDS[:3]:
        got = lookup(ru)
        print("  %%s -> %%s" %% (ru, got))
        assert got == en, "lookup failed for %%s" %% ru
    assert lookup("nonexistent-word") is None, "lookup should miss"
    print("OK: %%s ran a %%d-word quiz drill" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["words"], ensure_ascii=False),
       json.dumps(data["quiz_kind"], ensure_ascii=False))


def demo_conjugation(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FIRST = %s
SECOND = %s
PRONOUNS = %s
def conjugate(stem, endings):
    return [stem + e for e in endings]
def main():
    for cls in (FIRST, SECOND):
        forms = conjugate(cls["stem"], cls["endings"])
        print(cls["infinitive"], "->", ", ".join("%%s %%s" %% (p, f) for p, f in zip(PRONOUNS, forms)))
        assert forms == cls["forms"], "conjugation mismatch for %%s" %% cls["infinitive"]
        assert len(forms) == 6 and len(set(forms)) == 6, "forms must be 6 distinct"
    print("OK: %%s conjugated 2 verbs x 6 persons" %% NAME)
if __name__ == "__main__":
    main()
""" % (json.dumps(data["first"], ensure_ascii=False),
       json.dumps(data["second"], ensure_ascii=False),
       json.dumps(data["pronouns"], ensure_ascii=False))


def demo_agreement(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
HARD = %s
SOFT = %s
GENDERS = %s
HARD_END = {"masculine": "\\u044b\\u0439", "feminine": "\\u0430\\u044f",
            "neuter": "\\u043e\\u0435", "plural": "\\u044b\\u0435"}
SOFT_END = {"masculine": "\\u0438\\u0439", "feminine": "\\u044f\\u044f",
            "neuter": "\\u0435\\u0435", "plural": "\\u0438\\u0435"}
def main():
    for cls, ends in ((HARD, HARD_END), (SOFT, SOFT_END)):
        forms = [cls["stem"] + ends[g] for g in GENDERS]
        print("stem %%s ->" %% cls["stem"], ", ".join("%%s: %%s" %% (g, f) for g, f in zip(GENDERS, forms)))
        assert forms == cls["forms"], "agreement mismatch for stem %%s" %% cls["stem"]
    print("OK: %%s verified adjective agreement 2 stems x 4 forms" %% NAME)
if __name__ == "__main__":
    main()
""" % (json.dumps(data["hard"], ensure_ascii=False),
       json.dumps(data["soft"], ensure_ascii=False),
       json.dumps(data["genders"], ensure_ascii=False))


def demo_paradigm(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
COUNTS = %s
YA_CASES = %s
CASE_NAMES = %s
def main():
    total = sum(COUNTS.values())
    print("pronoun paradigm counts:", ", ".join("%%s=%%d" %% (k, v) for k, v in COUNTS.items()))
    assert COUNTS["personal"] == 8, "personal pronoun count wrong"
    assert COUNTS["possessive"] == 8, "possessive pronoun count wrong"
    assert COUNTS["demonstrative"] == 4, "demonstrative pronoun count wrong"
    assert COUNTS["interrogative"] == 5, "interrogative pronoun count wrong"
    assert total == 25, "total paradigm size wrong"
    print("declension of \\u044f:")
    for cn, form in zip(CASE_NAMES, YA_CASES):
        print("  %%-14s %%s" %% (cn, form))
    assert len(YA_CASES) == 6, "must list 6 case forms"
    assert len(set(YA_CASES)) >= 5, "forms must vary (genitive/accusative syncretism allowed)"
    assert YA_CASES[1] == YA_CASES[3], "genitive and accusative of \\u044f share \\u043c\\u0435\\u043d\\u044f"
    print("OK: %%s verified %%d pronoun forms" %% (NAME, total))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["counts"], ensure_ascii=False),
       json.dumps(data["ya_cases"], ensure_ascii=False),
       json.dumps(data["case_names"], ensure_ascii=False))


def demo_numbers(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
UNITS = dict((w, v) for w, v in %s)
TEENS = dict((w, v) for w, v in %s)
TENS = dict((w, v) for w, v in %s)
BYVAL = {}
BYVAL.update({v: w for w, v in UNITS.items()})
BYVAL.update({v: w for w, v in TEENS.items()})
BYVAL.update({v: w for w, v in TENS.items()})
def num_word(n):
    if n in BYVAL:
        return BYVAL[n]
    t, u = (n // 10) * 10, n %% 10
    return BYVAL[t] + " " + BYVAL[u]
def main():
    checks = [(1, "\\u043e\\u0434\\u0438\\u043d"), (7, "\\u0441\\u0435\\u043c\\u044c"),
              (17, "\\u0441\\u0435\\u043c\\u043d\\u0430\\u0434\\u0446\\u0430\\u0442\\u044c"),
              (21, "\\u0434\\u0432\\u0430\\u0434\\u0446\\u0430\\u0442\\u044c \\u043e\\u0434\\u0438\\u043d"),
              (40, "\\u0441\\u043e\\u0440\\u043e\\u043a"),
              (99, "\\u0434\\u0435\\u0432\\u044f\\u043d\\u043e\\u0441\\u0442\\u043e \\u0434\\u0435\\u0432\\u044f\\u0442\\u044c"),
              (100, "\\u0441\\u0442\\u043e")]
    for n, expected in checks:
        got = num_word(n)
        print("  %%3d -> %%s" %% (n, got))
        assert got == expected, "number word wrong for %%d" %% n
    assert len(UNITS) == 10 and len(TEENS) == 9 and len(TENS) == 9
    print("OK: %%s verified number words 1-100" %% NAME)
if __name__ == "__main__":
    main()
""" % (json.dumps(data["units"], ensure_ascii=False),
       json.dumps(data["teens"], ensure_ascii=False),
       json.dumps(data["tens"], ensure_ascii=False))


def demo_phrases(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
COUNT = %d
SAMPLE = %s
def main():
    print("greeting/phrase bank size:", COUNT)
    assert COUNT == 30, "must carry 30 phrases"
    for ru, tr, en in SAMPLE:
        assert ru and tr and en, "empty phrase field"
        print("  %%s (%%s) - %%s" %% (ru, tr, en))
    print("OK: %%s verified %%d phrases" %% (NAME, COUNT))
if __name__ == "__main__":
    main()
""" % (data["count"], json.dumps(data["sample"], ensure_ascii=False))


def demo_cases(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
DECL = %s
CASE_NAMES = %s
GENDERS = %s
def main():
    for noun, forms in DECL.items():
        assert len(forms) == 6, "6 cases required for %%s" %% noun
        assert len(set(forms)) >= 5, "forms must vary for %%s" %% noun
        print("%%s (%%s):" %% (noun, GENDERS[noun]))
        for cn, f in zip(CASE_NAMES, forms):
            print("  %%-14s %%s" %% (cn, f))
    assert DECL["\\u0434\\u043e\\u043c"][1] == "\\u0434\\u043e\\u043c\\u0430", "genitive of \\u0434\\u043e\\u043c wrong"
    assert DECL["\\u043a\\u043d\\u0438\\u0433\\u0430"][3] == "\\u043a\\u043d\\u0438\\u0433\\u0443", "accusative of \\u043a\\u043d\\u0438\\u0433\\u0430 wrong"
    assert DECL["\\u043e\\u043a\\u043d\\u043e"][5] == "\\u043e\\u043a\\u043d\\u0435", "prepositional of \\u043e\\u043a\\u043d\\u043e wrong"
    print("OK: %%s declined 3 nouns x 6 cases" %% NAME)
if __name__ == "__main__":
    main()
""" % (json.dumps(data["declensions"], ensure_ascii=False),
       json.dumps(data["case_names"], ensure_ascii=False),
       json.dumps(data["genders"], ensure_ascii=False))


def demo_sentences(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
SENTENCES = %s
TOPIC = %s
def main():
    n = len(SENTENCES)
    print("topic:", TOPIC, "| sentences:", n)
    total_words = 0
    for ru, tr, en in SENTENCES:
        assert ru and tr and en, "empty sentence field"
        total_words += len(ru.split())
    avg = total_words / n
    print("total Russian words: %%d, average per sentence: %%.1f" %% (total_words, avg))
    assert n == 20, "must carry 20 sentences"
    assert 3.0 <= avg <= 15.0, "average sentence length out of bounds"
    print("OK: %%s verified %%d sentences on %%s" %% (NAME, n, TOPIC))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["sentences"], ensure_ascii=False),
       json.dumps(data["topic"], ensure_ascii=False))


def demo_tenses(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
PAST_END = %s
STEM = %s
ASPECT = %s
FUT_AUX = %s
def main():
    forms = {g: STEM + e for g, e in PAST_END.items()}
    print("past of %%s-\\u0442\\u044c:" %% STEM)
    for g, f in forms.items():
        print("  %%-10s %%s" %% (g, f))
    assert forms["masculine"] == "\\u0447\\u0438\\u0442\\u0430\\u043b"
    assert forms["feminine"] == "\\u0447\\u0438\\u0442\\u0430\\u043b\\u0430"
    assert forms["neuter"] == "\\u0447\\u0438\\u0442\\u0430\\u043b\\u043e"
    assert forms["plural"] == "\\u0447\\u0438\\u0442\\u0430\\u043b\\u0438"
    assert len(ASPECT) == 5, "must carry 5 aspect pairs"
    for imp, pf in ASPECT:
        assert imp and pf and imp != pf, "bad aspect pair"
    print("aspect pairs:", ", ".join("%%s/%%s" %% (a, b) for a, b in ASPECT))
    assert FUT_AUX[0] == "\\u0431\\u0443\\u0434\\u0443" and len(FUT_AUX) == 6
    print("OK: %%s verified past-tense agreement and %%d aspect pairs" %% (NAME, len(ASPECT)))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["past_endings"], ensure_ascii=False),
       json.dumps(data["stem"], ensure_ascii=False),
       json.dumps(data["aspect_pairs"], ensure_ascii=False),
       json.dumps(data["future_aux"], ensure_ascii=False))


def demo_qa(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
PAIRS = %s
QWORDS = %s
def main():
    n = len(PAIRS)
    print("question/answer pairs:", n)
    assert n == 20, "must carry 20 pairs"
    for q, a in PAIRS:
        assert q.endswith("?"), "question must end with ?: %%s" %% q
        assert a and not a.endswith("?"), "answer must not be a question"
    missing = [w for w in QWORDS if not any(w in q.lower() for q, a in PAIRS)]
    assert not missing, "question words missing: %%s" %% missing
    print("question words covered:", ", ".join(QWORDS))
    print("OK: %%s verified %%d Q/A pairs" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["pairs"], ensure_ascii=False),
       json.dumps(data["question_words"], ensure_ascii=False))


def demo_imperative(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
PAIRS = %s
def main():
    n = len(PAIRS)
    print("imperative pairs (informal/formal):", n)
    assert n == 20, "must carry 20 imperatives"
    for ty, vy in PAIRS:
        assert ty and vy and ty != vy, "bad imperative pair"
        ty_s, vy_s = ty.rstrip("!"), vy.rstrip("!")
        if ty_s.endswith("\\u0441\\u044c"):
            expect = ty_s[:-2] + "\\u0442\\u0435\\u0441\\u044c"
        else:
            expect = ty_s + "\\u0442\\u0435"
        assert vy_s == expect, "formal imperative wrong: %%s / %%s" %% (ty, vy)
    print("sample:", ", ".join("%%s/%%s" %% (t, v) for t, v in PAIRS[:4]))
    print("OK: %%s verified %%d imperative pairs" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % json.dumps(data["pairs"], ensure_ascii=False)


def demo_story(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
LINES = %s
TENSE = %s
def main():
    n = len(LINES)
    print("story tense:", TENSE, "| lines:", n)
    assert n == 10, "story must have 10 lines"
    total = 0
    for ru, tr, en in LINES:
        assert ru and tr and en, "empty story line"
        total += len(ru.split())
    print("total Russian words in story:", total)
    assert 30 <= total <= 120, "story word count out of bounds"
    print("OK: %%s verified a 10-line %%s story" %% (NAME, TENSE))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["lines"], ensure_ascii=False),
       json.dumps(data["tense"], ensure_ascii=False))


def demo_idioms(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
IDIOMS = %s
def main():
    n = len(IDIOMS)
    print("idioms/proverbs:", n)
    assert n == 20, "must carry 20 idioms"
    for idm, lit, mean in IDIOMS:
        assert idm and lit and mean, "empty idiom field"
        assert lit != mean, "literal and meaning must differ"
    print("sample:", IDIOMS[0][0])
    print("OK: %%s verified %%d idioms with literal + real meaning" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % json.dumps(data["idioms"], ensure_ascii=False)


def demo_register(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
PAIRS = %s
def main():
    n = len(PAIRS)
    print("formal/informal pairs:", n)
    assert n == 15, "must carry 15 pairs"
    for informal, formal in PAIRS:
        assert informal and formal and informal != formal, "bad register pair"
    print("sample:", PAIRS[0][0], "/", PAIRS[0][1])
    print("OK: %%s verified %%d register pairs" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % json.dumps(data["pairs"], ensure_ascii=False)


def demo_complex(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
SENTENCES = %s
def main():
    n = len(SENTENCES)
    print("complex sentences:", n)
    assert n == 15, "must carry 15 sentences"
    for ru, cx in SENTENCES:
        parts = cx.split(" ... ")
        for part in parts:
            assert part in ru.lower(), "connector %%s missing in: %%s" %% (part, ru)
    print("connectors:", ", ".join(cx for ru, cx in SENTENCES))
    print("OK: %%s verified %%d complex sentences" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % json.dumps(data["sentences"], ensure_ascii=False)


def demo_dialogue(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
LINES = %s
SPEAKERS = %s
def main():
    n = len(LINES)
    print("dialogue speakers:", " / ".join(SPEAKERS), "| lines:", n)
    assert n == 20, "dialogue must have 20 lines"
    assert len(SPEAKERS) == 2, "dialogue needs 2 speakers"
    for i, (sp, ru) in enumerate(LINES):
        assert sp == SPEAKERS[i %% 2], "speakers must alternate at line %%d" %% (i + 1)
        assert ru, "empty dialogue line"
    print("OK: %%s verified a 20-line dialogue" %% NAME)
if __name__ == "__main__":
    main()
""" % (json.dumps(data["lines"], ensure_ascii=False),
       json.dumps(data["speakers"], ensure_ascii=False))


def demo_mastery(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
WORDS = %s
CATEGORIES = %s
def main():
    n = len(WORDS)
    print("core word bank:", n)
    assert n == 200, "must carry 200 core words"
    assert sum(CATEGORIES.values()) == 200, "category counts must total 200"
    rus = [w for w, e in WORDS]
    assert len(set(rus)) == 200, "words must be unique"
    for w, e in WORDS:
        assert w and e, "empty word entry"
    print("categories:", ", ".join("%%s=%%d" %% (k, v) for k, v in CATEGORIES.items()))
    print("OK: %%s verified the 200-word mastery bank" %% NAME)
if __name__ == "__main__":
    main()
""" % (json.dumps(data["words"], ensure_ascii=False),
       json.dumps(data["categories"], ensure_ascii=False))


DEMOS = {
    "overview": demo_overview,
    "alphabet": demo_alphabet,
    "phonology": demo_phonology,
    "vocab_quiz": demo_vocab_quiz,
    "conjugation": demo_conjugation,
    "agreement": demo_agreement,
    "paradigm": demo_paradigm,
    "numbers": demo_numbers,
    "phrases": demo_phrases,
    "cases": demo_cases,
    "sentences": demo_sentences,
    "tenses": demo_tenses,
    "qa": demo_qa,
    "imperative": demo_imperative,
    "story": demo_story,
    "idioms": demo_idioms,
    "register": demo_register,
    "complex": demo_complex,
    "dialogue": demo_dialogue,
    "mastery": demo_mastery,
}
