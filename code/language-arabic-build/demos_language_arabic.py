#!/usr/bin/env python3
"""Demo programs for the Arabic to English databases (Manon's language orders
#10-11, 2026-10-17, roster rank 5).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: script drills, vocabulary quizzes,
transliteration checks, conjugation tables, sentence statistics. All are
machine-executed by build.py before writing: each prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with the
OK marker.

Demo signature: fn(hdr, name, rid, group, entry) where entry is the full
entry dict (drill data included).
"""

import json

_PREAMBLE = "import json\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name))


def _data(drill):
    # repr keeps Python literals (True/False, tuples) valid in the demo program.
    return "DATA = %r\n" % (drill,)


# ---------------------------------------------------------------- 1: overview

def demo_overview(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    native_m = float(DATA["native_m"])
    total_m = float(DATA["total_m"])
    world_m = 8100.0
    share = native_m / world_m * 100.0
    print("native speakers: %.0f million" % native_m)
    print("share of world population: %.2f %%" % share)
    assert 3.8 < share < 4.0, "share out of bounds"
    per_country = native_m / float(DATA["official_countries"])
    print("official countries: %d" % DATA["official_countries"])
    print("average per official country: %.1f million" % per_country)
    assert 12.0 < per_country < 12.3, "per-country out of bounds"
    l2 = total_m - native_m
    print("second-language speakers: ~%.0f million" % l2)
    assert 84.9 < l2 < 85.1, "L2 estimate out of bounds"
    print("UN official languages: %d (Arabic is one)" % DATA["un_langs"])
    assert DATA["un_langs"] == 6
    assert DATA["letters"] == 28
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 2: writing system

def demo_writing(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    tlin = DATA["tlin"]
    print("letters in map: %d" % len(tlin))
    assert len(tlin) == 28, "alphabet must be 28"
    assert len(set(tlin.values())) == 28, "transliterations must be unique"
    assert len(DATA["letters"]) == 28
    rj = DATA["right_joiners"]
    print("right-joining-only letters: %d (%s)" % (len(rj), " ".join(rj)))
    assert len(rj) == 6
    def tr(word):
        return "".join(tlin.get(ch, "?") for ch in word)
    for ar, exp in DATA["map_tests"]:
        got = tr(ar)
        print("  %s -> %s" % (ar, got))
        assert "?" not in got, "unmapped letter in %s" % ar
        assert got == exp, "transliteration mismatch for %s" % ar
    indic = DATA["numerals"]
    assert len(indic) == 10
    def to_indic(s):
        return "".join(indic[int(c)] if c.isdigit() else c for c in s)
    got = to_indic("2026")
    print("2026 in Arabic-Indic digits: %s" % got)
    assert got == "٢٠٢٦", "indic conversion failed"
    print("OK: %s drilled the script" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 3: phonology

def demo_phonology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("consonants: %d" % DATA["consonants"])
    assert DATA["consonants"] == 28
    print("short vowels: %d, long vowels: %d" % (DATA["short_vowels"], DATA["long_vowels"]))
    assert DATA["short_vowels"] == 3 and DATA["long_vowels"] == 3
    emph = DATA["emphatics"]
    print("emphatic consonants: %d (%s)" % (len(emph), " ".join(emph)))
    assert len(emph) == 4 and set(emph) == set(["ص", "ض", "ط", "ظ"])
    ex = DATA["examples"]
    print("spoken examples: %d" % len(ex))
    assert len(ex) >= 10, "need 10+ spoken examples"
    for w in ex:
        assert len(w) == 3 and all(w), "bad example row %r" % (w,)
    long_v = sum(1 for w in ex if any(c in w[1] for c in ("ā", "ī", "ū")))
    print("examples with long vowels: %d" % long_v)
    assert 6 <= long_v <= 8
    print("OK: %s trained the ear" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 4: nouns

def demo_nouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
DIACRITICS = "ًٌٍَُِّْـٰ"
def strip(s):
    return "".join(c for c in s if c not in DIACRITICS)
def main():
    items = DATA["items"]
    print("nouns: %d" % len(items))
    assert len(items) == DATA["count"] == 25
    fem = sum(1 for w in items if w[0].endswith("ة"))
    masc = len(items) - fem
    print("masculine: %d, feminine: %d" % (masc, fem))
    assert masc + fem == 25 and 5 <= fem <= 7
    for w in items:
        ar, tlin, en, xa, xt, xe = w
        assert all([ar, tlin, en, xa, xt, xe]), "empty field in %r" % (w,)
        xs, a = strip(xa), strip(ar)
        # allow the definite article and the hamzat-wasl merge (امرأة -> المرأة)
        core = a[1:] if a.startswith("ا") else a
        assert a in xs or core in xs, "example lacks the noun: %s" % ar
    print("every example sentence contains its noun: 25/25")
    print("OK: %s quizzed the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 5: verbs

def demo_verbs(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
DIACRITICS = "ًٌٍَُِّْـٰ"
def strip(s):
    return "".join(c for c in s if c not in DIACRITICS)
def main():
    items = DATA["items"]
    print("verbs: %d" % len(items))
    assert len(items) == DATA["count"] == 25
    for w in items:
        assert len(w) == 6 and all(w), "bad verb row"
    r1, r2, r3 = DATA["root"]
    stem = r1 + r2 + r3
    suf = DATA["past_suffixes"]
    persons = DATA["past_persons"]
    print("past-tense persons: %d" % len(suf))
    assert len(suf) == len(persons) == 9
    table = {p: strip(stem + s) for p, s in zip(persons, suf)}
    spot = {k: strip(v) for k, v in DATA["past_spot"].items()}
    for p, exp in spot.items():
        got = table[p]
        print("  kataba %-7s -> %s" % (p, got))
        assert got == exp, "conjugation mismatch for %s" % p
    print("OK: %s conjugated the past tense" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 6: adjectives & adverbs

def demo_adjadv(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    adjs = DATA["adjectives"]; advs = DATA["adverbs"]
    print("adjectives: %d, adverbs: %d" % (len(adjs), len(advs)))
    assert len(adjs) == DATA["adj_count"] == 25
    assert len(advs) == DATA["adv_count"] == 15
    def fem_of(masc):
        # hamza-seat rule: -يء -> -يئة (بطيء -> بطيئة); otherwise + ة
        if masc.endswith("يء"):
            return masc[:-1] + "ئة"
        return masc + "ة"
    regular = sum(1 for w in adjs if w[3] == fem_of(w[0]))
    print("feminine derivation rule holds: %d/25" % regular)
    assert regular == 25, "feminine derivation broke"
    for w in adjs + advs:
        assert all(w), "empty field in %r" % (w,)
    print("every entry carries an example sentence: 40/40")
    print("OK: %s drilled agreement" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 7: pronouns

def demo_pronouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    per, pos, dem, inter = (DATA["personal"], DATA["possessive"],
                            DATA["demonstrative"], DATA["interrogative"])
    c12, c8, c6, c8b = DATA["counts"]
    print("personal: %d, possessive: %d, demonstrative: %d, interrogative: %d"
          % (len(per), len(pos), len(dem), len(inter)))
    assert (len(per), len(pos), len(dem), len(inter)) == (c12, c8, c6, c8b)
    assert (c12, c8, c6, c8b) == (12, 8, 6, 8)
    forms = [w[0] for w in per]
    assert "أنتما" in forms and "هما" in forms, "dual pronouns missing"
    print("dual forms present: أنتما, هما")
    assert all(w[0].startswith("كتاب") for w in pos), "possessive base broke"
    print("possessive suffixes attach to كتاب: 8/8")
    for w in dem + inter:
        assert len(w) == 6 and all(w), "bad row %r" % (w,)
    print("demonstratives + interrogatives carry examples: 14/14")
    print("OK: %s mapped the pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 8: numbers & time

def demo_numbers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    checks = [("1-10", DATA["n1_10"], 10), ("11-19", DATA["n11_19"], 9),
              ("tens", DATA["tens"], 10), ("ordinals", DATA["ordinals"], 10),
              ("days", DATA["days"], 7), ("months", DATA["months"], 12),
              ("seasons", DATA["seasons"], 4), ("sentences", DATA["sentences"], 6)]
    for label, rows, exp in checks:
        print("  %-9s %d" % (label, len(rows)))
        assert len(rows) == exp, "%s count wrong" % label
    indic = DATA["indic"]
    def to_indic(s):
        return "".join(indic[int(c)] if c.isdigit() else c for c in s)
    assert to_indic("123") == "١٢٣"
    assert to_indic("100") == "١٠٠"
    print("Arabic-Indic conversion: 123 -> ١٢٣, 100 -> ١٠٠")
    assert DATA["n1_10"][0][0] == "واحد" and DATA["tens"][-2][0] == "مائة"
    print("OK: %s counted to one hundred" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 9: greetings

def demo_greetings(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    items = DATA["items"]
    print("phrases: %d" % len(items))
    assert len(items) == DATA["count"] == 30
    cats = {}
    for w in items:
        assert len(w) == 5 and all(w), "bad greeting row"
        cats[w[3]] = cats.get(w[3], 0) + 1
    print("categories: %s" % cats)
    assert cats == DATA["cats"] == {"greeting": 14, "farewell": 4, "politeness": 12}
    pairs = [("صباح الخير", "صباح النور"), ("مساء الخير", "مساء النور"),
             ("السلام عليكم", "وعليكم السلام")]
    have = set(w[0] for w in items)
    for a, b in pairs:
        assert a in have and b in have, "pair broken: %s/%s" % (a, b)
    print("call-and-response pairs intact: 3/3")
    print("OK: %s drilled the greetings" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 10: grammar

def demo_grammar(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    rules = DATA["rules"]
    print("grammar rules: %d" % len(rules))
    assert len(rules) == DATA["count"] == 10
    assert DATA["vso"].startswith("كتبَ"), "VSO example must start with the verb"
    print("VSO example starts with the verb: %s" % DATA["vso"])
    neg = DATA["neg"]
    print("negation particles: %s" % " ".join(neg))
    assert neg == ["لا", "لم", "لن"]
    cases = DATA["cases"]
    assert len(cases) == 3
    print("case endings: nominative %s, accusative %s, genitive %s" % tuple(cases))
    print("OK: %s enforced the ten rules" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 11-20: themed sentence sets

def _demo_theme(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    sents = DATA["sentences"]
    print("sentences: %d" % len(sents))
    assert len(sents) == DATA["count"] == 20
    for s in sents:
        assert len(s) == 3 and all(s), "bad sentence row"
    words = [len(s[0].split()) for s in sents]
    avg = sum(words) / float(len(words))
    print("words per sentence: min %d, max %d, avg %.1f" % (min(words), max(words), avg))
    assert 2.5 < avg < 9.0, "avg sentence length out of bounds"
    kws = DATA["keywords"]
    cov = sum(1 for s in sents if any(k in s[0] for k in kws))
    print("theme keyword coverage: %d/20" % cov)
    assert 5 <= cov <= 20, "keyword coverage out of bounds"
    print("OK: %s drilled the theme" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_home(hdr, name, rid, group, entry):
    return _demo_theme(hdr, name, rid, group, entry)


def demo_food(hdr, name, rid, group, entry):
    return _demo_theme(hdr, name, rid, group, entry)


def demo_travel(hdr, name, rid, group, entry):
    return _demo_theme(hdr, name, rid, group, entry)


def demo_work(hdr, name, rid, group, entry):
    return _demo_theme(hdr, name, rid, group, entry)


def demo_health(hdr, name, rid, group, entry):
    return _demo_theme(hdr, name, rid, group, entry)


def demo_emotions(hdr, name, rid, group, entry):
    return _demo_theme(hdr, name, rid, group, entry)


def demo_nature(hdr, name, rid, group, entry):
    return _demo_theme(hdr, name, rid, group, entry)


def demo_shopping(hdr, name, rid, group, entry):
    return _demo_theme(hdr, name, rid, group, entry)


def demo_social(hdr, name, rid, group, entry):
    return _demo_theme(hdr, name, rid, group, entry)


def demo_tech(hdr, name, rid, group, entry):
    return _demo_theme(hdr, name, rid, group, entry)


# ---------------------------------------------------------------- 21: tenses

def demo_tenses(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    past, pres, fut = DATA["past"], DATA["present"], DATA["future"]
    for label, rows in (("past", past), ("present", pres), ("future", fut)):
        print("  %-7s sentences: %d" % (label, len(rows)))
        assert len(rows) == 6, "%s must have 6 sentences" % label
        for s in rows:
            assert len(s) == 3 and all(s), "bad row"
    fut_ok = sum(1 for s in fut
                 if s[0].startswith("س") or "سوف" in s[0] or s[0].startswith("لن"))
    print("future sentences with future marker: %d/6" % fut_ok)
    assert fut_ok == 6
    table = DATA["table"]
    print("present-tense persons: %d" % len(table))
    assert len(table) == DATA["persons"] == 13
    spot = {p: a for p, t, a in table}
    assert spot["هو"] == "يكتبُ" and spot["أنا"] == "أكتبُ" and spot["هم"] == "يكتبونَ"
    print("spot check: هو -> يكتبُ, أنا -> أكتبُ, هم -> يكتبونَ")
    print("OK: %s mastered the tenses" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 22: questions & answers

def demo_qa(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    pairs = DATA["pairs"]
    print("Q/A pairs: %d" % len(pairs))
    assert len(pairs) == DATA["count"] == 20
    qwords = DATA["qwords"]
    ok = 0
    for p in pairs:
        assert len(p) == 6 and all(p), "bad pair row"
        q = p[0]
        if any(q.startswith(w) for w in qwords):
            ok += 1
    print("questions opening with a question word: %d/20" % ok)
    assert ok == 20, "every question must open with a question word"
    print("OK: %s ran the inquisition" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 23: commands

def demo_commands(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    items = DATA["items"]
    print("commands: %d" % len(items))
    assert len(items) == DATA["count"] == 20
    formal = sum(1 for w in items if w[3])
    informal = len(items) - formal
    print("formal: %d, informal: %d" % (formal, informal))
    assert (formal, informal) == (DATA["formal"], DATA["informal"]) == (8, 12)
    for w in items:
        assert len(w) == 5 and all([w[0], w[1], w[2], w[4]]), "bad command row"
    neg = [w for w in items if "لا تتأخرْ" in w[0]]
    assert len(neg) == 1, "negative command missing"
    print("negative command present: لا تتأخرْ")
    print("OK: %s issued the orders" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 24: descriptions

def demo_descriptions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    items = DATA["items"]
    print("descriptions: %d" % len(items))
    assert len(items) == DATA["count"] == 20
    for s in items:
        assert len(s) == 3 and all(s), "bad row"
    words = [len(s[0].split()) for s in items]
    avg = sum(words) / float(len(words))
    print("words per description: min %d, max %d, avg %.1f" % (min(words), max(words), avg))
    assert 3.0 < avg < 9.0
    pivots = sum(1 for s in items if "لكن" in s[0])
    print("descriptions with لكن pivot: %d" % pivots)
    assert pivots >= 1
    print("OK: %s painted the portraits" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 25-27: stories

def _demo_story(hdr, name, rid, group, entry, markers, mlabel):
    body = _data(entry["drill"]) + '''\
def main():
    sents = DATA["sentences"]
    print("story sentences: %d" % len(sents))
    assert len(sents) == DATA["count"] == 10
    for s in sents:
        assert len(s) == 3 and all(s), "bad story row"
    words = [len(s[0].split()) for s in sents]
    total = sum(words)
    avg = total / float(len(words))
    print("total words: %d, avg per sentence: %.1f" % (total, avg))
    assert 40 <= total <= 120 and 4.0 < avg < 12.0
    marks = __MARKERS__
    hit = sum(1 for s in sents if any(m in s[0] for m in marks))
    print("__MLABEL__ marker coverage: %d/10" % hit)
    assert hit >= __THRESH__, "tense markers missing"
    print("OK: %s told the story" % NAME)
if __name__ == "__main__":
    main()
'''
    body = body.replace("__MARKERS__", json.dumps(markers, ensure_ascii=False))
    body = body.replace("__MLABEL__", mlabel)
    body = body.replace("__THRESH__", "2" if mlabel != "future/conditional" else "6")
    return _wrap(hdr, name, rid, group, body)


def demo_story1(hdr, name, rid, group, entry):
    return _demo_story(hdr, name, rid, group, entry, ["ثم", "بعدَ", "عندَ"], "chain-word")


def demo_story2(hdr, name, rid, group, entry):
    return _demo_story(hdr, name, rid, group, entry, ["في", "بعدَ", "عندَ"], "time-anchor")


def demo_story3(hdr, name, rid, group, entry):
    return _demo_story(hdr, name, rid, group, entry,
                       ["سأ", "سوف", "ست", "سن", "إذا", "لو"], "future/conditional")


# ---------------------------------------------------------------- 28: idioms

def demo_idioms(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    items = DATA["items"]
    print("idioms: %d" % len(items))
    assert len(items) == DATA["count"] == 20
    for w in items:
        assert len(w) == 6 and all(w), "idiom missing literal/meaning/example"
    longest = max(items, key=lambda w: len(w[0]))
    print("longest idiom: %s (%d chars)" % (longest[0], len(longest[0])))
    assert 20 <= len(longest[0]) <= 60
    print("every idiom has literal + meaning + example: 20/20")
    print("OK: %s quoted the wisdom" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 29: registers

def demo_registers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    pairs = DATA["pairs"]
    print("register pairs: %d" % len(pairs))
    assert len(pairs) == DATA["count"] == 15
    for p in pairs:
        assert len(p) == 4 and all(p), "bad register row"
        assert p[0] != p[2], "formal and informal must differ"
    formal_marks = sum(1 for p in pairs
                       if any(m in p[0] for m in ("حضرت", "أود", "أرجو", "يرجى", "يُرجى", "نرجو", "برجاء")))
    print("formal lines with register markers: %d/15" % formal_marks)
    assert formal_marks >= 5
    print("OK: %s changed uniforms" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 30: complex sentences

def demo_complex(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
DIACRITICS = "ًٌٍَُِّْـٰ"
def strip(s):
    return "".join(c for c in s if c not in DIACRITICS)
def main():
    items = DATA["items"]
    print("complex sentences: %d" % len(items))
    assert len(items) == DATA["count"] == 15
    for w in items:
        assert len(w) == 4 and all(w), "bad row"
        conn = strip(w[3].split("(")[0].strip())
        sent = strip(w[0])
        assert conn and conn in sent, "connector %r not in sentence" % w[3]
    print("every sentence contains its named connector: 15/15")
    rel = sum(1 for w in items if "الذي" in w[0] or "التي" in w[0])
    print("relative-clause sentences: %d" % rel)
    assert rel == 2
    print("OK: %s bound the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 31-33: dialogues

def _demo_dialog(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    lines = DATA["lines"]
    print("dialogue lines: %d" % len(lines))
    assert len(lines) == DATA["count"] == 20
    speakers = {}
    for l in lines:
        assert len(l) == 5 and all(l), "bad dialogue row"
        speakers[l[0]] = speakers.get(l[0], 0) + 1
    print("speakers: %s" % speakers)
    assert len(speakers) == 2, "dialogue needs exactly two speakers"
    counts = sorted(speakers.values())
    assert counts[1] - counts[0] <= 4, "dialogue unbalanced"
    qs = sum(1 for l in lines if "؟" in l[1])
    print("lines with questions: %d" % qs)
    assert qs >= 3
    print("OK: %s held the conversation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_market(hdr, name, rid, group, entry):
    return _demo_dialog(hdr, name, rid, group, entry)


def demo_friend(hdr, name, rid, group, entry):
    return _demo_dialog(hdr, name, rid, group, entry)


def demo_problem(hdr, name, rid, group, entry):
    return _demo_dialog(hdr, name, rid, group, entry)


# ---------------------------------------------------------------- 34: mastery

def demo_mastery(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    words = DATA["words200"]
    print("core words: %d" % len(words))
    assert len(words) == DATA["count"] == 200
    for w in words:
        assert len(w) == 3 and all(w), "bad word row"
    uniq = len(set(w[0] for w in words))
    print("unique Arabic forms: %d" % uniq)
    assert 195 <= uniq <= 200, "word list has too many duplicates"
    print("alphabet letters: %d" % DATA["alphabet"])
    assert DATA["alphabet"] == 28
    rules = DATA["grammar_rules"]
    print("grammar rules: %d" % len(rules))
    assert len(rules) == 10
    print("OK: %s passed the final muster" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_overview, "writing": demo_writing,
    "phonology": demo_phonology, "nouns1": demo_nouns,
    "verbs1": demo_verbs, "adjadv": demo_adjadv,
    "pronouns": demo_pronouns, "numbers": demo_numbers,
    "greetings": demo_greetings, "grammar": demo_grammar,
    "home": demo_home, "food": demo_food, "travel": demo_travel,
    "work": demo_work, "health": demo_health, "emotions": demo_emotions,
    "nature": demo_nature, "shopping": demo_shopping,
    "social": demo_social, "tech": demo_tech, "tenses": demo_tenses,
    "qa": demo_qa, "commands": demo_commands,
    "descriptions": demo_descriptions, "story1": demo_story1,
    "story2": demo_story2, "story3": demo_story3,
    "idioms": demo_idioms, "registers": demo_registers,
    "complex": demo_complex, "market": demo_market,
    "friend": demo_friend, "problem": demo_problem,
    "mastery": demo_mastery,
}
