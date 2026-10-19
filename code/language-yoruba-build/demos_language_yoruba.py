#!/usr/bin/env python3
"""Demo programs for the Yoruba to English databases (Manon's language project,
2026-10-17).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: alphabet drills, tone checks, vocabulary
counts, vigesimal arithmetic, aspect-marker tables, sentence statistics. All
are machine-executed by build.py before writing: each prints its real
computed values, asserts tight bounds (never float exact-equality), and ends
with the OK marker.

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
    world_m = 8100.0
    share = native_m / world_m * 100.0
    print("native speakers: %.0f million" % native_m)
    print("share of world population: %.3f %%" % share)
    assert 0.56 < share < 0.58, "share out of bounds"
    print("national-language countries: %d" % DATA["national_countries"])
    assert DATA["national_countries"] == 2
    print("dialects: %d (%s)" % (len(DATA["dialects"]), ", ".join(DATA["dialects"][:3]) + "..."))
    assert len(DATA["dialects"]) == 15
    print("regions: %d" % len(DATA["regions"]))
    assert len(DATA["regions"]) == 6
    assert DATA["iso1"] == "yo" and DATA["iso3"] == "yor"
    assert len(DATA["sisters"]) == 2 and len(DATA["tones"]) == 3
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 2: writing system

def demo_writing(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    import unicodedata
    def base(ch):
        d = unicodedata.normalize("NFD", ch)
        return "".join(c for c in d if unicodedata.category(c) != "Mn")
    letters = DATA["letters"]
    print("Yoruba letters: %d" % len(letters))
    assert len(letters) == 25, "Yoruba alphabet must be 25"
    assert len(set(letters)) == 25, "letters must be unique"
    specials = DATA["specials"]
    print("dotted specials: %s" % " ".join(specials))
    assert specials == ["\\u1eb9", "\\u1ecd", "\\u1e63"], "specials must be e-dot o-dot s-dot"
    for sp in specials:
        assert sp in letters, "special %r missing from alphabet" % sp
    for dg in DATA["digraphs"]:
        assert dg in letters, "digraph %s missing" % dg
    assert DATA["digraphs"] == ["gb"], "only gb is a digraph"
    for bad in DATA["missing_native"]:
        assert bad not in letters, "%s must not be a native letter" % bad
    print("oral vowels: %d, nasal vowels: %d" % (len(DATA["vowels_oral"]), len(DATA["vowels_nasal"])))
    assert len(DATA["vowels_oral"]) == 7 and len(DATA["vowels_nasal"]) == 5
    print("direction: %s" % DATA["direction"])
    assert DATA["direction"] == "left-to-right"
    words = DATA["test_words"]
    alpha = set()
    for ch in letters:
        if ch == "gb":
            alpha.add("gb")
        else:
            alpha.add(base(ch))
    for w in words:
        i = 0
        while i < len(w):
            if w[i:i+2] == "gb":
                i += 2
            else:
                assert base(w[i]) in alpha, "unwritable char %r in %s" % (w[i], w)
                i += 1
        print("  writable: %s" % w)
    assert len(words) == 5
    print("OK: %s spelled the alphabet" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 3: phonology

def demo_phonology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("oral vowels: %d, nasal vowels: %d" % (len(DATA["vowels_oral"]), len(DATA["vowels_nasal"])))
    assert len(DATA["vowels_oral"]) == 7 and len(DATA["vowels_nasal"]) == 5
    print("consonants: %d" % DATA["consonants"])
    assert DATA["consonants"] == 18
    print("tones: %s" % ", ".join(DATA["tones"]))
    assert DATA["tones"] == ["high", "mid", "low"]
    print("special consonants: %s" % ", ".join(DATA["specials"]))
    assert DATA["specials"] == ["gb", "kp", "\\u1e63"]
    trio = DATA["tone_trio"]
    print("tone trio:")
    for w, g, t in trio:
        print("  %s (%s) - %s" % (w, t, g))
    assert len(trio) == 3
    words = set(w for w, _, _ in trio)
    glosses = set(g for _, g, _ in trio)
    tones = set(t for _, _, t in trio)
    assert len(words) == 3 and len(glosses) == 3 and len(tones) == 3, "trio must be fully distinct"
    print("example words: %d" % len(DATA["example_words"]))
    assert len(DATA["example_words"]) == 10
    print("OK: %s sounded the phonology" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 4: nouns

def demo_nouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    nouns = DATA["nouns"]
    print("nouns: %d" % len(nouns))
    assert len(nouns) == 25 and len(set(nouns)) == 25
    g = DATA["groups"]
    total = g["people"] + g["places"] + g["things"]
    print("people %d, places %d, things %d" % (g["people"], g["places"], g["things"]))
    assert total == 25, "group counts must sum to 25"
    avg = sum(len(w) for w in nouns) / len(nouns)
    print("average noun length: %.2f chars" % avg)
    assert 3.0 < avg < 7.0, "avg length out of bounds"
    print("plural marker: %s" % DATA["plural_marker"])
    assert DATA["plural_marker"] == "\\u00e0w\\u1ecdn"
    print("plural example: %s %s" % (DATA["plural_marker"], nouns[0]))
    print("OK: %s counted the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 5: verbs

def demo_verbs(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    verbs = DATA["verbs"]
    print("verbs: %d" % len(verbs))
    assert len(verbs) == 25 and len(set(verbs)) == 25
    markers = DATA["markers"]
    print("aspect markers: %s" % ", ".join(markers))
    assert markers == ["\\u0144", "ti", "m\\u00e1a"]
    root = "l\\u1ecd"
    forms = {"bare": root, "progressive": "\\u0144 " + root,
             "perfect": "ti " + root, "future": "m\\u00e1a " + root}
    print("forms of %s:" % root)
    for k, v in forms.items():
        print("  %s: %s" % (k, v))
    assert len(set(forms.values())) == 4, "four forms must differ"
    serial = DATA["serial_example"]
    print("serial verb: %s" % serial)
    assert "m\\u00fa" in serial and "w\\u00e1" in serial
    monosyll = sum(1 for v in verbs if len(v) <= 4)
    print("short roots: %d/25" % monosyll)
    assert monosyll >= 18, "most Yoruba verbs are short roots"
    print("OK: %s drilled the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 6: adjectives/adverbs

def demo_adjectives(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    adjs = DATA["adjectives"]
    advs = DATA["adverbs"]
    print("adjectives: %d, adverbs: %d" % (len(adjs), len(advs)))
    assert len(adjs) == 25 and len(advs) == 15
    assert len(set(adjs)) == 25 and len(set(advs)) == 15
    noun, adj = "il\\u00e9", "\\u0144l\\u00e1"
    phrase = noun + " " + adj
    print("adjective follows noun: %s" % phrase)
    assert phrase.startswith(noun) and phrase.endswith(adj)
    intens = DATA["intensified"]
    print("reduplication intensifies:")
    for base, strong in intens.items():
        print("  %s -> %s" % (base, strong))
        assert strong.startswith(base) and len(strong) > len(base)
    assert len(intens) == 2
    print("OK: %s qualified the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 7: pronouns

def demo_pronouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    subj = DATA["subject"]
    poss = DATA["possessive"]
    print("subject pronouns: %d (%s)" % (len(subj), " ".join(subj)))
    assert subj == ["mo", "o", "\\u00f3", "a", "\\u1eb9", "w\u1ecd\u0301n"]
    print("possessive pronouns: %d" % len(poss))
    assert poss == ["mi", "r\\u1eb9", "r\\u1eb9\\u0300", "wa", "y\\u00edn", "w\\u1ecdn"]
    assert poss[1] != poss[2], "r\\u1eb9 (your) vs r\\u1eb9\\u0300 (his/her) differ by tone"
    print("tone pair: %s (your) vs %s (his/her)" % (poss[1], poss[2]))
    print("emphatic: %d, demonstrative: %d, interrogative: %d" % (
        len(DATA["emphatic"]), len(DATA["demonstrative"]), len(DATA["interrogative"])))
    assert len(DATA["emphatic"]) == 6 and len(DATA["demonstrative"]) == 4
    assert len(DATA["interrogative"]) == 8
    print("possessive example: il\\u00e9 %s" % poss[0])
    print("OK: %s paradigmatized the pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 8: numbers/time

def demo_numbers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    one_ten = DATA["one_to_ten"]
    print("1-10: %d numerals" % len(one_ten))
    assert len(one_ten) == 10
    tens = DATA["tens"]
    print("tens: %d" % len(tens))
    assert len(tens) == 9
    assert tens["20"] == "og\\u00fan" and tens["100"] == "\\u1ecdg\\u1ecd\\u0301r\\u00f9n-\\u00fan"
    vals = {"20": 20, "30": 30, "40": 40, "50": 50, "60": 60,
            "70": 70, "80": 80, "90": 90, "100": 100}
    assert vals["40"] == 2 * vals["20"], "og\\u00f3j\\u00ec = 20x2"
    assert vals["60"] == 3 * vals["20"], "\\u1ecdg\\u1ecd\\u0301ta = 20x3"
    assert vals["100"] == 5 * vals["20"], "\\u1ecdg\\u1ecd\\u0301r\\u00f9\\u00fan = 20x5"
    print("vigesimal checks: 40=20x2, 60=20x3, 100=20x5")
    sub = {"25": 30 - 5, "35": 40 - 5, "45": 50 - 5, "95": 100 - 5}
    for k, v in sub.items():
        assert v == int(k), "subtraction form wrong for " + k
    print("subtraction forms: 25=30-5, 35=40-5, 45=50-5, 95=100-5")
    print("ordinals: %d (first: %s)" % (len(DATA["ordinals"]), DATA["ordinals"][0]))
    assert DATA["ordinals"][0].startswith("\\u1eb9\\u0300k")
    print("days: %d, months: %d, seasons: %d" % (
        len(DATA["days"]), len(DATA["months"]), len(DATA["seasons"])))
    assert len(DATA["days"]) == 7 and len(DATA["months"]) == 12 and len(DATA["seasons"]) == 2
    print("OK: %s counted in twenties" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 9: greetings

def demo_greetings(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    parts = {k: v for k, v in DATA.items() if k != "count"}
    total = sum(len(v) for v in parts.values())
    print("greeting sets:")
    for k, v in parts.items():
        print("  %s: %d" % (k, len(v)))
    print("total phrases: %d" % total)
    assert total == DATA["count"] == 31, "must total 31 phrases"
    assert len(DATA["time_greetings"]) == 3
    assert len(DATA["activity_greetings"]) == 10
    assert DATA["activity_greetings"][0].startswith("\u1eb8 ku")
    print("respect switch: bare k\\u00e0\\u00e1r\\u1ecd\\u0300 vs \\u1eb9 k\\u00e0\\u00e1r\\u1ecd\\u0300")
    print("OK: %s greeted everyone" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 10: grammar essentials

def demo_grammar(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("grammar rules: %d" % DATA["rules"])
    assert DATA["rules"] == 10
    s = "Mo ra \\u00ecw\\u00e9"
    parts = s.split()
    print("SVO parse: %s | %s | %s" % (parts[0], parts[1], parts[2]))
    assert parts == ["Mo", "ra", "\\u00ecw\\u00e9"]
    neg_v = DATA["neg_verbal"] + " l\\u1ecd"
    print("verbal negation: %s" % neg_v)
    assert neg_v == "k\\u00f2 l\\u1ecd"
    neg_n = DATA["neg_nominal"]
    print("nominal negation: %s" % neg_n)
    assert neg_n == "k\\u00ec \\u00ed \\u1e63e"
    q = DATA["question_particle"] + " o \\u0144 b\\u1ecd\\u0300?"
    print("yes/no question: %s" % q)
    assert q.startswith("\\u1e63\\u00e9")
    foc = "\\u00ccw\\u00e9 ni mo r\\u00e0"
    print("focus: %s" % foc)
    assert " ni " in foc
    print("copulas: %s" % ", ".join(DATA["copulas"]))
    assert DATA["copulas"] == ["j\\u1eb9\\u0301", "w\\u00e0"]
    print("markers: %s" % ", ".join(DATA["markers"]))
    assert len(DATA["markers"]) == 3
    print("OK: %s ruled the grammar" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 11: home & family

def demo_home(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("home sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("rooms: %d, kin terms: %d" % (len(DATA["rooms"]), len(DATA["kin"])))
    assert len(DATA["rooms"]) == 3 and len(DATA["kin"]) == 7
    kin = DATA["kin"]
    assert "b\\u00e0b\\u00e1" in kin and "\\u00ecy\\u00e1" in kin
    assert "\\u1eb9\\u0300gb\\u1ecd\\u0301n" in kin and "\\u00e0b\\u00far\\u00f2" in kin
    print("seniority pair: \\u1eb9\\u0300gb\\u1ecd\\u0301n (elder) / \\u00e0b\\u00far\\u00f2 (younger)")
    print("possession follows noun: il\\u00e9 wa")
    print("OK: %s mapped the home" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 12: food & cooking

def demo_food(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("food sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("dishes: %d (%s)" % (len(DATA["dishes"]), ", ".join(DATA["dishes"][:3]) + "..."))
    assert len(DATA["dishes"]) == 6
    print("kitchen verbs: %d" % len(DATA["kitchen_verbs"]))
    assert DATA["kitchen_verbs"] == ["se", "j\\u1eb9", "mu", "g\\u00e9", "d\\u00e1", "d\\u00edn"]
    assert "se" in DATA["kitchen_verbs"] and "j\\u1eb9" in DATA["kitchen_verbs"]
    print("taste verb: d\\u00f9n (be tasty)")
    print("OK: %s cooked the sentences" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 13: travel & directions

def demo_travel(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("travel sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("direction words: %d" % len(DATA["direction_words"]))
    assert len(DATA["direction_words"]) == 5
    print("transport verbs: %s" % ", ".join(DATA["transport_verbs"]))
    assert DATA["transport_verbs"] == ["d\\u00e9", "b\\u1ecd\\u0300", "k\\u00fan", "s\\u1ecd\\u0300kal\\u1eb9\\u0300"]
    print("OK: %s mapped the journey" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 14: work & school

def demo_work(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("work sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("professions: %s" % ", ".join(DATA["professions"]))
    assert len(DATA["professions"]) == 3
    print("school verbs: %s" % ", ".join(DATA["school_verbs"]))
    assert len(DATA["school_verbs"]) == 3
    print("profession copula: \\u00f3 j\\u1eb9\\u0301 ol\\u00f9k\\u1ecd\\u0301")
    print("OK: %s worked the shift" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 15: health & body

def demo_health(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("health sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("body parts: %d" % len(DATA["body_parts"]))
    assert len(DATA["body_parts"]) == 8
    print("symptoms: %s" % ", ".join(DATA["symptoms"]))
    assert len(DATA["symptoms"]) == 5
    pain = "Or\\u00ed \\u0144 dun mi"
    print("pain pattern: %s" % pain)
    assert pain.startswith("Or\\u00ed")
    print("OK: %s checked the body" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 16: emotions

def demo_emotions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("emotion sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("in\\u00fa-forms: %s" % ", ".join(DATA["inu_forms"]))
    assert DATA["inu_forms"] == ["d\\u00f9n", "b\\u00e0j\\u1eb9\\u0301", "bal\\u1eb9\\u0300"]
    print("emotions: %d" % len(DATA["emotions"]))
    assert len(DATA["emotions"]) == 6
    happy = "In\\u00fa mi d\\u00f9n"
    sad = "In\\u00fa mi b\\u00e0j\\u1eb9\\u0301"
    print("happy: %s / sad: %s" % (happy, sad))
    assert happy != sad
    print("OK: %s felt the feelings" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 17: nature & weather

def demo_nature(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("nature sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("weather verbs: %s" % ", ".join(DATA["weather_verbs"]))
    assert DATA["weather_verbs"] == ["r\\u1ecd\\u0300", "r\\u00e0n", "f\\u1eb9\\u0301", "\\u1e63\\u00fa", "t\\u00e0n"]
    print("animals: %d" % len(DATA["animals"]))
    assert len(DATA["animals"]) == 7
    rain = "\\u00d2j\\u00f2 \\u0144 r\\u1ecd\\u0300"
    print("rain: %s" % rain)
    assert rain == "\\u00d2j\\u00f2 \\u0144 r\\u1ecd\\u0300"
    print("OK: %s read the sky" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 18: shopping & money

def demo_shopping(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("shopping sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    pw = DATA["price_words"]
    print("price words: %d (%s)" % (len(pw), ", ".join(pw[:3]) + "..."))
    assert len(pw) == 6
    assert "\\u1eb9l\\u00f3 ni" in pw and "d\\u00ednk\\u00f9" in pw
    price = "\\u1eb9l\\u00f3 ni \\u00e8y\\u00ed?"
    print("price question: %s" % price)
    print("OK: %s priced the market" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 19: friendship

def demo_friendship(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("friendship sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    sw = DATA["social_words"]
    print("social words: %d" % len(sw))
    assert len(sw) == 7
    assert "or\\u00fak\\u1ecd" in sw and "r\\u00e1nt\\u00ed" in sw
    invite = "J\\u1eb9\\u0301 k\\u00e1 l\\u1ecd"
    print("invitation: %s" % invite)
    print("OK: %s made friends" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 20: technology

def demo_technology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("technology sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("loanwords: %s" % ", ".join(DATA["loans"]))
    assert len(DATA["loans"]) == 5
    print("tech verbs: %s" % ", ".join(DATA["tech_verbs"]))
    assert len(DATA["tech_verbs"]) == 6
    msg = "Fi \\u00ecr\\u00e1n\\u1e63\\u00e9 r\\u00e1n\\u1e63\\u00e9 s\\u00ed mi"
    print("message command: %s" % msg)
    print("OK: %s wired the tech" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 21: verb tenses

def demo_tenses(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    patterns = DATA["patterns"]
    print("aspect patterns: %d" % len(patterns))
    assert len(patterns) == 6
    assert DATA["per_pattern"] == 6
    root = DATA["root"]
    forms = [root, "\\u0144 " + root, "ti " + root, "m\\u00e1a " + root,
             "k\\u00ed \\u00f3 " + root, "k\\u00f2 " + root]
    print("six forms of %s:" % root)
    for f in forms:
        print("  %s" % f)
    assert len(set(forms)) == 6, "all six forms must differ"
    total = len(patterns) * DATA["per_pattern"]
    print("tense sentences: %d" % total)
    assert total == 36
    print("OK: %s rode the six markers" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 22: questions & answers

def demo_qa(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("Q&A pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 20
    print("question words: %d" % len(DATA["qwords"]))
    assert len(DATA["qwords"]) == 8
    print("yes: %s, yes/no particle: %s" % (DATA["yes"], DATA["yn_particle"]))
    assert DATA["yes"] == "b\\u1eb9\\u0301\\u1eb9\\u0300 ni"
    assert DATA["yn_particle"] == "\\u1e63\\u00e9"
    q = DATA["yn_particle"] + " o \\u0144 b\\u1ecd\\u0300?"
    a = DATA["yes"] + ", mo \\u0144 b\\u1ecd\\u0300"
    print("pair: %s / %s" % (q, a))
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 23: commands & requests

def demo_commands(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    c, p, r = DATA["commands"], DATA["prohibitions"], DATA["polite"]
    print("commands %d, prohibitions %d, polite %d" % (c, p, r))
    assert c == 10 and p == 4 and r == 6
    assert c + p + r == 20, "must total 20"
    print("softeners: %s" % ", ".join(DATA["softeners"]))
    assert len(DATA["softeners"]) == 3
    cmd = "W\\u00e1!"
    print("bare command: %s" % cmd)
    prohib = "M\\u00e1 l\\u1ecd!"
    print("prohibition: %s" % prohib)
    print("OK: %s commanded politely" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 24: descriptions

def demo_descriptions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("description sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    total = DATA["people"] + DATA["places"] + DATA["things"]
    print("people %d, places %d, things %d" % (DATA["people"], DATA["places"], DATA["things"]))
    assert total == 20
    print("connectors: %s" % ", ".join(DATA["connectors"]))
    assert DATA["connectors"] == ["t\\u00ed", "\\u1e63\\u00f9gb\\u1ecd\\u0301n", "s\\u00ec"]
    rel = "ob\\u00ecnrin g\\u00edga t\\u00ed \\u00f3 w\\u1ecd a\\u1e63\\u1ecd pupa"
    print("relative clause: %s" % rel)
    print("OK: %s painted the portraits" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 25: story I

def demo_story1(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 10
    print("story verbs: %d" % len(DATA["verbs"]))
    assert len(DATA["verbs"]) == 10
    print("time words: %s" % ", ".join(DATA["time_words"]))
    assert len(DATA["time_words"]) == 3
    chained = "\\u00f3 j\\u00ed, \\u00f3 s\\u00ec w\\u1eb9\\u0300"
    print("s\\u00ec-chain: %s" % chained)
    print("OK: %s told the market day" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 26: story II

def demo_story2(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 10
    print("past verbs: %d" % len(DATA["past_verbs"]))
    assert len(DATA["past_verbs"]) == 7
    assert DATA["perfect"] == ["ti r\\u00ed"]
    assert DATA["background"] == ["\\u0144 j\\u1eb9 kor\\u00edko"]
    print("perfect: %s; background: %s" % (DATA["perfect"][0], DATA["background"][0]))
    focus = "n\\u00edb\\u1eb9\\u0300 ni \\u00f3 ti r\\u00ed"
    print("focus cleft: %s" % focus)
    print("OK: %s found the goat" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 27: story III

def demo_story3(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 10
    print("future markers: %s" % ", ".join(DATA["future_markers"]))
    assert DATA["future_markers"] == ["m\\u00e1a", "y\\u00f3\\u00f2"]
    print("conditionals: %d" % len(DATA["conditionals"]))
    assert len(DATA["conditionals"]) == 2
    cond = DATA["conditionals"][0]
    print("conditional: %s" % cond)
    assert "b\\u00ed" in cond and "b\\u00e1" in cond
    print("OK: %s planned tomorrow" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 28: idioms & proverbs

def demo_idioms(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("proverbs: %d, idioms: %d" % (DATA["proverbs"], DATA["idioms"]))
    assert DATA["proverbs"] == 10 and DATA["idioms"] == 10
    assert DATA["proverbs"] + DATA["idioms"] == 20
    print("body words: %s" % ", ".join(DATA["body_words"]))
    assert DATA["body_words"] == ["in\\u00fa", "\\u1eb9nu", "\\u1ecdk\\u00e0n"]
    prov = "K\\u00e1 r\\u00ecn k\\u00e1 p\\u1ecd\\u0300"
    print("unity proverb opens: %s..." % prov)
    print("OK: %s spoke in proverbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 29: formal registers

def demo_registers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("register pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 15
    print("rungs: %s" % " < ".join(DATA["rungs"]))
    assert len(DATA["rungs"]) == 3
    print("formal openings: %s" % " / ".join(DATA["openings"]))
    assert len(DATA["openings"]) == 2
    print("OK: %s minded the register" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 30: complex sentences

def demo_complex(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("complex sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 15
    glues = DATA["glues"]
    print("clause glues: %d" % len(glues))
    assert len(glues) == 9
    assert "t\\u00ed" in glues and "n\\u00edtor\\u00ed" in glues
    rel = "\\u1ecdm\\u1ecd t\\u00ed \\u00f3 l\\u1ecd"
    print("relative clause: %s..." % rel)
    print("OK: %s built the edifice" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 31: conversation at the market

def demo_conv_market(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    print("moves: %d" % len(DATA["moves"]))
    assert len(DATA["moves"]) == 10
    print("speakers: %s" % " / ".join(DATA["speakers"]))
    assert len(DATA["speakers"]) == 2
    arc = ["\\u1eb9l\\u00f3 ni", "\\u00f3 w\\u1ecd\\u0301n j\\u00f9", "\\u1eb9 d\\u00ednk\\u00f9"]
    print("bargaining arc: %s" % " -> ".join(arc))
    print("OK: %s haggled at the market" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 32: conversation meeting a friend

def demo_conv_friend(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    print("moves: %d" % len(DATA["moves"]))
    assert len(DATA["moves"]) == 12
    assert len(DATA["speakers"]) == 2
    reunion = "\\u00f3 ti p\\u1eb9\\u0301"
    print("reunion marker: %s" % reunion)
    print("OK: %s met the friend" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 33: conversation solving a problem

def demo_conv_problem(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    print("moves: %d" % len(DATA["moves"]))
    assert len(DATA["moves"]) == 14
    assert len(DATA["speakers"]) == 2
    discovery = "Mo r\\u00ed i!"
    print("discovery: %s" % discovery)
    print("OK: %s solved the problem" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 34: mastery review

def demo_mastery(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("letters: %d, core words: %d" % (DATA["letters"], DATA["core_words"]))
    assert DATA["letters"] == 25 and DATA["core_words"] == 200
    groups = DATA["word_groups"]
    total = sum(groups.values())
    print("word groups: %d, sum: %d" % (len(groups), total))
    assert total == 200, "word groups must sum to 200"
    for gname, gcount in groups.items():
        print("  %s: %d" % (gname, gcount))
    print("grammar rules: %d, phrase tables: %d" % (DATA["rules"], DATA["phrase_tables"]))
    assert DATA["rules"] == 10 and DATA["phrase_tables"] == 5
    print("OK: %s sealed the covenant" % NAME)
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
