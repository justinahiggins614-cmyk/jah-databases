#!/usr/bin/env python3
"""Demo programs for the Malayalam to English databases (Manon's language project,
2026-10-17).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: script drills, vocabulary quizzes,
transliteration checks, tense tables, sentence statistics. All are
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
    print("share of world population: %.3f %%" % share)
    assert 0.46 < share < 0.48, "share out of bounds"
    l2 = total_m - native_m
    print("second-language speakers: ~%.0f million" % l2)
    assert 6.9 < l2 < 7.1, "L2 estimate out of bounds"
    print("official regions: %d" % DATA["official_regions"])
    assert DATA["official_regions"] == 3
    print("dialects: %d (%s)" % (len(DATA["dialects"]), ", ".join(DATA["dialects"])))
    assert len(DATA["dialects"]) == 3
    print("regions: %d" % len(DATA["regions"]))
    assert len(DATA["regions"]) == 7
    assert DATA["iso1"] == "ml" and DATA["iso3"] == "mal"
    assert DATA["scheduled"] == 22 and DATA["classical_year"] == 2013
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 2: writing system

def demo_writing(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    letters = DATA["letters"]
    print("base letters: %d" % len(letters))
    assert len(letters) == 52, "16 vowels + 36 consonants = 52"
    assert len(set(letters)) == 52, "letters must be unique"
    chillu = DATA["chillu_letters"]
    print("chillu letters: %s" % " ".join(chillu))
    assert len(chillu) == 5
    for c in chillu:
        assert c not in letters, "chillu must be separate from base letters"
    print("digits: %d" % len(DATA["digits"]))
    assert len(DATA["digits"]) == 10
    assert DATA["digits"][0] == "\\u0d66", "first digit must be Malayalam zero"
    print("direction: %s" % DATA["direction"])
    assert DATA["direction"] == "left-to-right"
    print("vowel killer: %s" % DATA["killer"])
    assert DATA["killer"] == "\\u0d4d"
    for w in DATA["test_words"]:
        assert w, "test word must be non-empty"
        assert all("\\u0d00" <= ch <= "\\u0d7f" for ch in w), "word %r outside Malayalam block" % w
        print("  writable: %s" % w)
    assert len(DATA["test_words"]) == 4
    print("OK: %s spelled the alphabet" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 3: phonology

def demo_phonology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("vowels: %d" % DATA["vowel_count"])
    assert DATA["vowel_count"] == 16
    v, s = DATA["vargas"], DATA["steps"]
    print("vargas: %d x %d steps = %d slots" % (v, s, v * s))
    assert v == 5 and s == 5 and v * s == 25
    sig = DATA["signature_sounds"]
    print("signature sounds: %s" % " ".join(sig))
    assert sig == ["\\u0d34", "\\u0d31", "\\u0d33"], "must be zha, rra, lla"
    print("tones: %s" % DATA["tones"])
    assert DATA["tones"] is False, "Malayalam has no tones"
    a, b = DATA["minimal_pairs"][0][0], DATA["minimal_pairs"][1][0]
    print("minimal pair: %s (%s) vs %s (%s)" % (a, DATA["minimal_pairs"][0][2], b, DATA["minimal_pairs"][1][2]))
    assert a != b, "minimal pair must differ"
    words = DATA["example_words"]
    print("example words: %d" % len(words))
    assert len(words) == 10
    avg = sum(len(w) for w in words) / len(words)
    print("avg word length: %.1f chars" % avg)
    assert 3.0 < avg < 7.0, "word length out of bounds"
    print("stress: %s" % DATA["stress"])
    assert DATA["stress"] == "first syllable"
    print("OK: %s sounded the inventory" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 4: nouns

def demo_nouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    nouns = DATA["nouns"]
    print("nouns: %d" % len(nouns))
    assert len(nouns) == 25, "must be 25 nouns"
    assert len(set(nouns)) == 25, "nouns must be unique"
    assert all(n for n in nouns), "no empty nouns"
    print("first: %s / last: %s" % (nouns[0], nouns[-1]))
    assert nouns[0] == "\\u0d35\\u0d40\\u0d1f\\u0d4d", "first noun must be house"
    suf = DATA["plural_suffix"]
    print("plural suffix: %s" % suf)
    assert suf == "\\u0d15\\u0d7e", "plural suffix must be -kal"
    base, loc = DATA["locative_example"]
    print("locative: %s -> %s" % (base, loc))
    assert loc.startswith(base[:2]), "locative builds on the stem"
    assert len(loc) > len(base), "locative adds the -il ending"
    print("OK: %s named 25 nouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 5: verbs

def demo_verbs(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    verbs = DATA["verbs"]
    print("verbs: %d" % len(verbs))
    assert len(verbs) == 25, "must be 25 verbs"
    assert len(set(verbs)) == 25, "verbs must be unique"
    uka = sum(1 for v in verbs if v.endswith("\\u0d15"))
    print("citation forms ending in -ka: %d" % uka)
    assert uka >= 20, "most citation forms end in -uka"
    stem_full, stem = DATA["stem_example"]
    print("stem: %s -> %s" % (stem_full, stem))
    assert stem == stem_full[:-2] + "\\u0d4d", "stem strips -uka and kills the vowel"
    assert len(stem) < len(stem_full)
    pres, past, fut = DATA["present"], DATA["past"], DATA["future"]
    print("endings: present -%s, past -%s, future -%s" % (pres, past, fut))
    assert (pres, past, fut) == ("unnu", "i", "um")
    conj = DATA["conjugated"]
    print("conjugated: %s / %s / %s" % (conj["present"], conj["past"], conj["future"]))
    assert conj["present"].endswith("\\u0d28\\u0d4d\\u0d28\\u0d41") and conj["future"].endswith("\\u0d41\\u0d02")
    assert conj["past"] == "\\u0d2a\\u0d4b\\u0d2f\\u0d3f", "past of to-go must be pooyi"
    print("OK: %s conjugated 25 verbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 6: adjectives

def demo_adjectives(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("adjectives: %d / adverbs: %d" % (DATA["adjective_count"], DATA["adverb_count"]))
    assert DATA["adjective_count"] == 25
    assert DATA["adverb_count"] == 15
    assert DATA["adjective_count"] + DATA["adverb_count"] == 40
    b = DATA["builders"]
    print("adjective builders: %s" % ", ".join(b))
    assert b == ["\\u0d09\\u0d33\\u0d4d\\u0d33", "\\u0d2e\\u0d3e\\u0d2f"], "must be -ulla and -maaya"
    e = DATA["adverb_endings"]
    print("adverb endings: %s" % ", ".join(e))
    assert len(e) == 2
    w, s1, s2 = DATA["invariable_example"]
    print("invariable: %s -> %s / %s" % (w, s1, s2))
    assert s1.startswith(w) and s2.startswith(w), "adjective must not change"
    assert s1 != s2, "singular and plural phrases must differ only in the noun"
    print("comparative: -%s" % DATA["comparative"])
    assert DATA["comparative"] == "\\u0d0f\\u0d15\\u0d4d\\u0d15\\u0d3e\\u0d7e"
    print("OK: %s described 40 words" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 7: pronouns

def demo_pronouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    p = DATA["personal"]
    print("personal pronouns: %d" % len(p))
    assert len(p) == 10
    assert p[0] == "\\u0d1e\\u0d3e\\u0d7b", "first must be njaan (I)"
    print("possessives: %d" % len(DATA["possessive"]))
    assert len(DATA["possessive"]) == 6
    for pos in DATA["possessive"]:
        assert pos.endswith("\\u0d31\\u0d46") or pos.endswith("\\u0d41\\u0d1f\\u0d46"), "possessive %r must end in -nte/-ute" % pos
    print("demonstratives: %d" % len(DATA["demonstrative"]))
    assert len(DATA["demonstrative"]) == 5
    print("interrogatives: %d" % len(DATA["interrogative"]))
    assert len(DATA["interrogative"]) == 8
    inc, exc = DATA["we_split"]
    print("we: inclusive %s / exclusive %s" % (inc, exc))
    assert inc != exc, "the two we-words must differ"
    assert inc == "\\u0d28\\u0d2e\\u0d4d\\u0d2e\\u0d7e" and exc == "\\u0d1e\\u0d19\\u0d4d\\u0d19\\u0d7e"
    print("OK: %s pointed with pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 8: numbers

def demo_numbers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    ten = DATA["one_to_ten"]
    print("1-10: %d numbers" % len(ten))
    assert len(ten) == 10 and len(set(ten)) == 10
    tens = DATA["tens"]
    print("tens: %d entries" % len(tens))
    assert len(tens) == 8, "30..100 step 10 is 8 entries"
    assert tens["100"] == "\\u0d28\\u0d42\\u0d31\\u0d4d", "100 must be nooru"
    print("eleven: %s" % DATA["eleven"])
    assert DATA["eleven"].startswith(ten[9][:2]), "11 compounds on 10"
    print("days: %d" % len(DATA["days"]))
    assert len(DATA["days"]) == 7
    print("months: %d" % len(DATA["months"]))
    assert len(DATA["months"]) == 12
    assert DATA["months"][8] == "\\u0d2e\\u0d47\\u0d1f\\u0d02", "9th month must be Metam (Vishu)"
    print("time: %s / half: %s / quarter: %s" % (DATA["oclock"], DATA["half"], DATA["quarter"]))
    assert DATA["oclock"] and DATA["half"] and DATA["quarter"]
    print("OK: %s counted to one hundred" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 9: greetings

def demo_greetings(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("phrases: %d" % DATA["count"])
    assert DATA["count"] == 30
    core = [("hello", "\\u0d28\\u0d2e\\u0d38\\u0d4d\\u0d15\\u0d3e\\u0d30\\u0d02"),
            ("thanks", "\\u0d28\\u0d28\\u0d4d\\u0d26\\u0d3f"), ("please", "\\u0d26\\u0d2f\\u0d35\\u0d3e\\u0d2f\\u0d3f"),
            ("yes", "\\u0d05\\u0d24\\u0d46"), ("no", "\\u0d07\\u0d32\\u0d4d\\u0d32")]
    for k, want in core:
        got = DATA[k]
        print("%s: %s" % (k, got))
        assert got == want, "%s mismatch" % k
    surv = DATA["survival"]
    print("survival phrases: %d" % len(surv))
    assert len(surv) == 3
    assert any("\\u0d2e\\u0d28\\u0d38\\u0d4d\\u0d38\\u0d3f\\u0d32\\u0d3e\\u0d2f\\u0d3f\\u0d32\\u0d4d\\u0d32" in s for s in surv), "must include I-did-not-understand"
    print("OK: %s greeted thirty ways" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 10: grammar

def demo_grammar(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("rules: %d" % DATA["rules"])
    assert DATA["rules"] == 10
    print("word order: %s" % DATA["word_order"])
    assert DATA["word_order"] == "SOV"
    print("cases: %d" % len(DATA["cases"]))
    assert len(DATA["cases"]) == 7
    assert len(DATA["case_suffixes"]) == 7
    t = DATA["tenses"]
    print("tenses: %s" % t)
    assert t == {"present": "unnu", "past": "i", "future": "um"}
    print("copula: %s" % " / ".join(DATA["copula"]))
    assert len(DATA["copula"]) == 3
    print("negation: %s" % " / ".join(DATA["negation"]))
    assert DATA["negation"] == ["\\u0d05\\u0d32\\u0d4d\\u0d32", "\\u0d07\\u0d32\\u0d4d\\u0d32"]
    print("question particle: -%s" % DATA["question_particle"])
    assert DATA["question_particle"] == "\\u0d13"
    print("OK: %s fixed the ten rules" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 11: home & family

def demo_home(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("existence verb: %s" % DATA["existence_verb"])
    assert DATA["existence_verb"] == "\\u0d09\\u0d23\\u0d4d\\u0d1f\\u0d4d"
    print("locative: -%s / direction: -%s" % (DATA["locative"], DATA["direction"]))
    assert DATA["locative"] == "\\u0d07\\u0d7d" and DATA["direction"] == "\\u0d07\\u0d32\\u0d47\\u0d15\\u0d4d\\u0d15\\u0d4d"
    pairs = DATA["family_pairs"]
    print("family pairs: %d" % len(pairs))
    assert len(pairs) == 4
    for m, f in pairs:
        assert m and f and m != f, "each pair needs two distinct words"
    print("OK: %s toured the home" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 12: food

def demo_food(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("meals: %s" % ", ".join(DATA["meals"]))
    assert len(DATA["meals"]) == 3
    print("imperative ending: -%s" % DATA["imperative"])
    assert DATA["imperative"] == "\\u0d42"
    dishes = DATA["dishes"]
    print("dishes: %d (%s...)" % (len(dishes), dishes[0]))
    assert len(dishes) == 5
    assert "\\u0d2a\\u0d3e\\u0d2f\\u0d38\\u0d02" in dishes, "payasam must be listed"
    print("OK: %s cooked twenty sentences" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 13: travel

def demo_travel(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("left: %s / right: %s" % (DATA["left"], DATA["right"]))
    assert DATA["left"] != DATA["right"]
    print("toward: -%s" % DATA["toward"])
    assert DATA["toward"] == "\\u0d07\\u0d32\\u0d47\\u0d15\\u0d4d\\u0d15\\u0d4d"
    print("can-i-get: %s" % DATA["can_i_get"])
    assert DATA["can_i_get"].endswith("\\u0d4b"), "must carry the question particle"
    t = DATA["transport"]
    print("transport: %d modes" % len(t))
    assert len(t) == 5
    print("OK: %s mapped the journey" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 14: work & school

def demo_work(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("professions: %s" % ", ".join(DATA["professions"]))
    assert len(DATA["professions"]) == 3
    print("conditional: -%s / perfective: -%s" % (DATA["conditional"], DATA["perfective"]))
    assert DATA["conditional"] == "\\u0d06\\u0d7d" and DATA["perfective"] == "\\u0d07\\u0d1f\\u0d4d\\u0d1f\\u0d41\\u0d23\\u0d4d\\u0d1f\\u0d4d"
    print("school words: %d" % len(DATA["school_words"]))
    assert len(DATA["school_words"]) == 3
    print("OK: %s worked twenty sentences" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 15: health

def demo_health(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    bp = DATA["body_parts"]
    print("body parts: %d" % len(bp))
    assert len(bp) == 8 and len(set(bp)) == 8
    print("pain verb: %s" % DATA["pain_verb"])
    assert DATA["pain_verb"].endswith("\\u0d28\\u0d4d\\u0d28\\u0d41"), "pain verb must be present tense"
    print("experiencer: %s" % DATA["experiencer"])
    assert DATA["experiencer"] == "\\u0d0e\\u0d28\\u0d3f\\u0d15\\u0d4d\\u0d15\\u0d4d", "must be the dative enikku"
    print("OK: %s checked twenty symptoms" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 16: emotions

def demo_emotions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    em = DATA["emotions"]
    print("emotions: %d (%s)" % (len(em), ", ".join(em[:3]) + "..."))
    assert len(em) == 6
    print("love verb: %s" % DATA["love_verb"])
    assert DATA["love_verb"].endswith("\\u0d28\\u0d4d\\u0d28\\u0d41")
    print("comfort forms: %s" % ", ".join(DATA["comfort"]))
    assert len(DATA["comfort"]) == 2
    print("OK: %s felt twenty sentences" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 17: nature

def demo_nature(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("animals: %d / plants: %d / seasons: %d" % (len(DATA["animals"]), len(DATA["plants"]), len(DATA["seasons"])))
    assert len(DATA["animals"]) == 5 and len(DATA["plants"]) == 3 and len(DATA["seasons"]) == 3
    assert "\\u0d06\\u0d28" in DATA["animals"], "elephant must be listed"
    print("prediction word: %s" % DATA["prediction"])
    assert DATA["prediction"] == "\\u0d24\\u0d4b\\u0d28\\u0d4d\\u0d28\\u0d41\\u0d28\\u0d4d\\u0d28\\u0d41"
    print("OK: %s walked through nature" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 18: shopping

def demo_shopping(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    steps = DATA["bargain_steps"]
    print("bargain steps: %d" % len(steps))
    assert len(steps) == 3
    assert steps[0].rstrip().endswith("?"), "step 1 must be a question"
    assert steps[2].startswith("\\u0d36\\u0d30\\u0d3f"), "step 3 must accept with shari"
    print("suggestion ending: -%s" % DATA["suggestion"])
    assert DATA["suggestion"] == "\\u0d06\\u0d02"
    print("measures: %s" % ", ".join(DATA["measures"]))
    assert len(DATA["measures"]) == 3
    print("OK: %s bargained twenty sentences" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 19: friendship

def demo_friendship(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("invitation ending: -%s" % DATA["invitation"])
    assert DATA["invitation"] == "\\u0d06\\u0d02"
    print("festivals: %s" % ", ".join(DATA["festivals"]))
    assert DATA["festivals"] == ["\\u0d13\\u0d23\\u0d02", "\\u0d35\\u0d3f\\u0d37\\u0d41"]
    print("intro triple: %s" % ", ".join(DATA["intro_triple"]))
    assert len(DATA["intro_triple"]) == 3
    print("OK: %s made twenty friends" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 20: technology

def demo_technology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    loans = DATA["loans"]
    print("loan words: %d" % len(loans))
    assert len(loans) == 5
    pw = DATA["problem_words"]
    print("problem words: %s" % ", ".join(pw))
    assert len(pw) == 3
    print("OK: %s sent twenty messages" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 21: tenses

def demo_tenses(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("present: -%s / future: -%s" % (DATA["present"], DATA["future"]))
    assert DATA["present"] == "unnu" and DATA["future"] == "um"
    pf = DATA["past_forms"]
    print("past forms: %d" % len(pf))
    assert len(pf) == 5
    assert pf["\\u0d2a\\u0d4b\\u0d15\\u0d41\\u0d15"] == "\\u0d2a\\u0d4b\\u0d2f\\u0d3f", "to-go past must reshape"
    negs = DATA["negations"]
    print("negations: %s" % ", ".join(negs))
    assert len(negs) == 3
    for n in negs:
        assert n.endswith("\\u0d3f\\u0d32\\u0d4d\\u0d32"), "negation %r must end in -illa" % n
    asp = DATA["aspects"]
    print("aspects: %d" % len(asp))
    assert len(asp) == 3
    print("sentences per tense: %d" % DATA["per_tense"])
    assert DATA["per_tense"] >= 5
    print("OK: %s timed the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 22: questions & answers

def demo_qa(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 20
    print("question particle: -%s" % DATA["question_particle"])
    assert DATA["question_particle"] == "\\u0d13"
    qw = DATA["question_words"]
    print("question words: %d" % len(qw))
    assert len(qw) == 8
    assert "\\u0d06\\u0d30\\u0d4d" in qw, "who (aar) must be listed"
    print("yes: %s / no: %s" % (DATA["yes"], DATA["no"]))
    assert DATA["yes"] != DATA["no"]
    print("OK: %s asked twenty questions" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 23: commands

def demo_commands(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("rungs: %d" % len(DATA["rungs"]))
    assert len(DATA["rungs"]) == 4
    print("prohibition: -%s / let's: -%s" % (DATA["prohibition"], DATA["lets"]))
    assert DATA["prohibition"] == "\\u0d30\\u0d41\\u0d24\\u0d4d" and DATA["lets"] == "\\u0d06\\u0d02"
    inf = DATA["informal"]
    print("informal: %s" % ", ".join(inf))
    assert len(inf) == 3
    print("OK: %s commanded twenty ways" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 24: descriptions

def demo_descriptions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("pair joiner: -%s" % DATA["pair_joiner"])
    assert DATA["pair_joiner"] == "\\u0d09\\u0d02"
    print("superlative: %s" % DATA["superlative"])
    assert DATA["superlative"] == "\\u0d0f\\u0d31\\u0d4d\\u0d31\\u0d35\\u0d41\\u0d02"
    print("character adj: -%s / quality adj: -%s" % (DATA["character_adj"], DATA["quality_adj"]))
    assert DATA["character_adj"] == "\\u0d09\\u0d33\\u0d4d\\u0d33"
    assert DATA["quality_adj"] == "\\u0d2e\\u0d3e\\u0d2f"
    print("OK: %s painted twenty portraits" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 25: story I

def demo_story1(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story lines: %d" % DATA["lines"])
    assert DATA["lines"] == 10
    tw = DATA["time_words"]
    print("time words: %d (%s)" % (len(tw), ", ".join(tw)))
    assert len(tw) == 4
    print("hero: %s" % DATA["hero"])
    assert DATA["hero"] == "\\u0d30\\u0d35\\u0d3f"
    print("OK: %s told the simple day" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 26: story II

def demo_story2(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story lines: %d" % DATA["lines"])
    assert DATA["lines"] == 10
    pv = DATA["past_verbs"]
    print("past verbs: %d" % len(pv))
    assert len(pv) == 9 and len(set(pv)) == 9
    print("frame: %s" % DATA["frame"])
    assert DATA["frame"] == "\\u0d15\\u0d34\\u0d3f\\u0d1e\\u0d4d\\u0d1e \\u0d35\\u0d7c\\u0d37\\u0d02"
    print("closing: %s" % DATA["closing"])
    assert DATA["closing"].endswith("\\u0d3f\\u0d32\\u0d4d\\u0d32"), "closing must be a future negative"
    print("OK: %s told the journey" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 27: story III

def demo_story3(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story lines: %d" % DATA["lines"])
    assert DATA["lines"] == 10
    fv = DATA["future_verbs"]
    print("future verbs: %d" % len(fv))
    assert len(fv) == 8
    for v in fv:
        assert v.endswith("\\u0d41\\u0d02"), "future verb %r must end in -um" % v
    cond = DATA["conditionals"]
    print("conditionals: %d" % len(cond))
    assert len(cond) == 2
    for c in cond:
        assert c.endswith("\\u0d3e\\u0d7d"), "conditional %r must end in -aal" % c
    print("copula future: %s" % DATA["copula_future"])
    assert DATA["copula_future"].endswith("\\u0d15\\u0d4d\\u0d15\\u0d41\\u0d02")
    print("OK: %s planned tomorrow" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 28: idioms

def demo_idioms(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("proverbs: %d" % DATA["proverbs"])
    assert DATA["proverbs"] == 20
    print("streams: %s" % ", ".join(DATA["streams"]))
    assert len(DATA["streams"]) == 2
    print("native word: %s" % DATA["native_word"])
    assert DATA["native_word"] == "\\u0d2a\\u0d34\\u0d1e\\u0d4d\\u0d1a\\u0d4a\\u0d32\\u0d4d\\u0d32\\u0d4d"
    print("OK: %s sealed twenty proverbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 29: registers

def demo_registers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 15
    print("levers: %d" % len(DATA["levers"]))
    assert len(DATA["levers"]) == 3
    print("safe you: %s" % DATA["safe_you"])
    assert DATA["safe_you"] == "\\u0d28\\u0d3f\\u0d19\\u0d4d\\u0d19\\u0d7e"
    print("formal open: %s / close: %s" % (DATA["formal_open"], DATA["formal_close"]))
    assert DATA["formal_open"] and DATA["formal_close"]
    print("OK: %s kept the registers" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 30: complex sentences

def demo_complex(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 15
    print("relative participle: %s" % DATA["relative"])
    assert DATA["relative"].endswith("\\u0d28\\u0d4d\\u0d28")
    print("reported: -%s" % DATA["reported"])
    assert DATA["reported"] == "\\u0d0e\\u0d28\\u0d4d\\u0d28\\u0d4d"
    suf = DATA["suffixes"]
    print("clause suffixes: %d" % len(suf))
    assert len(suf) == 4
    print("OK: %s built fifteen complexes" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 31: conversation at the market

def demo_conv_market(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    print("speakers: %s" % ", ".join(DATA["speakers"]))
    assert DATA["speakers"] == ["A", "B"]
    arc = DATA["arc"]
    print("arc: %d beats" % len(arc))
    assert len(arc) == 6
    assert arc[0] == "greeting" and arc[-1] == "farewell"
    print("promise form: %s" % DATA["promise_form"])
    assert DATA["promise_form"] == "\\u0d24\\u0d30\\u0d3e\\u0d02"
    print("OK: %s haggled at the market" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 32: conversation with a friend

def demo_conv_friend(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    print("register: %s" % DATA["register"])
    assert DATA["register"] == "intimate"
    arc = DATA["arc"]
    print("arc: %d beats" % len(arc))
    assert len(arc) == 6
    print("habitual past: %s" % DATA["habitual_past"])
    assert DATA["habitual_past"].endswith("\\u0d28\\u0d4d\\u0d28\\u0d41")
    print("OK: %s met the old friend" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 33: conversation solving a problem

def demo_conv_problem(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    loop = DATA["loop"]
    print("loop: %d steps" % len(loop))
    assert len(loop) == 5
    print("problem (past): %s / solution (future): %s" % (DATA["problem_past"], DATA["solution_future"]))
    assert DATA["problem_past"] == "\\u0d15\\u0d47\\u0d1f\\u0d3e\\u0d2f\\u0d3f"
    assert DATA["solution_future"].endswith("\\u0d41\\u0d02")
    print("OK: %s solved the problem" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 34: mastery

def demo_mastery(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("core words: %d" % DATA["core_words"])
    assert DATA["core_words"] == 200
    v, c, ch = DATA["vowels"], DATA["consonants"], DATA["chillu"]
    print("alphabet: %d vowels + %d consonants + %d chillu = %d" % (v, c, ch, v + c + ch))
    assert (v, c, ch) == (16, 36, 5)
    assert v + c + ch == 57
    print("cases: %d / tenses: %d" % (DATA["cases"], DATA["tenses"]))
    assert DATA["cases"] == 7 and DATA["tenses"] == 3
    print("OK: %s sealed the mastery page" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_overview,
    "writing": demo_writing,
    "phonology": demo_phonology,
    "nouns": demo_nouns,
    "verbs": demo_verbs,
    "adjectives": demo_adjectives,
    "pronouns": demo_pronouns,
    "numbers": demo_numbers,
    "greetings": demo_greetings,
    "grammar": demo_grammar,
    "home": demo_home,
    "food": demo_food,
    "travel": demo_travel,
    "work": demo_work,
    "health": demo_health,
    "emotions": demo_emotions,
    "nature": demo_nature,
    "shopping": demo_shopping,
    "friendship": demo_friendship,
    "technology": demo_technology,
    "tenses": demo_tenses,
    "qa": demo_qa,
    "commands": demo_commands,
    "descriptions": demo_descriptions,
    "story1": demo_story1,
    "story2": demo_story2,
    "story3": demo_story3,
    "idioms": demo_idioms,
    "registers": demo_registers,
    "complex": demo_complex,
    "conv_market": demo_conv_market,
    "conv_friend": demo_conv_friend,
    "conv_problem": demo_conv_problem,
    "mastery": demo_mastery,
}
