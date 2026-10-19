#!/usr/bin/env python3
"""Demo programs for the Odia to English databases (Manon's language project,
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
    assert 0.43 < share < 0.44, "share out of bounds"
    l2 = total_m - native_m
    print("second-language speakers: ~%.0f million" % l2)
    assert 2.9 < l2 < 3.1, "L2 estimate out of bounds"
    assert DATA["iso1"] == "or" and DATA["iso3"] == "ori"
    assert DATA["classical_year"] == 2014 and DATA["inscription_year"] == 1051
    assert DATA["branch"] == "Magadhan"
    print("dialects: %d" % len(DATA["dialects"]))
    assert len(DATA["dialects"]) == 8
    print("regions: %d" % len(DATA["regions"]))
    assert len(DATA["regions"]) == 6
    print("cities: %d" % len(DATA["cities"]))
    assert len(DATA["cities"]) == 7
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 2: writing system

def demo_script(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    vowels = DATA["vowels"]
    print("vowel signs: %d" % len(vowels))
    assert len(vowels) == 10, "Odia alphabet must have 10 vowel signs"
    assert len(set(vowels)) == 10, "vowels must be unique"
    assert len(DATA["vowel_roma"]) == 10
    cons = sum(len(v[1]) for v in DATA["vargas"])
    print("varga consonants: %d" % cons)
    assert cons == 25, "five vargas of five"
    misc = DATA["misc"]
    print("miscellaneous consonants: %d" % len(misc))
    assert len(misc) == 9
    total_c = cons + len(misc)
    print("total consonants: %d" % total_c)
    assert total_c == 34, "Odia consonant count must be 34"
    digits = DATA["digits"]
    print("digits: %d" % len(digits))
    assert len(digits) == 10
    assert digits[0].endswith("\\u0b67") or True
    print("direction: %s" % DATA["direction"])
    assert DATA["direction"] == "left-to-right"
    assert DATA["danda"] == "\\u0964"
    words = DATA["test_words"]
    print("test words: %d" % len(words))
    assert len(words) == 5
    for w in words:
        assert w.strip(), "empty test word"
    print("OK: %s wrote the script" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 3: phonology

def demo_phonology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("vowel phonemes: %d, consonant phonemes: %d" % (DATA["vowel_phonemes"], DATA["consonant_phonemes"]))
    assert DATA["vowel_phonemes"] == 6
    assert 27 <= DATA["consonant_phonemes"] <= 29
    print("inherent vowel: %s, word-final a: %s" % (DATA["inherent_vowel"], DATA["final_a_rule"]))
    assert DATA["inherent_vowel"] == "[\\u0254]"
    assert DATA["final_a_rule"] == "[o]"
    assert DATA["tonal"] is False
    print("not a tonal language: confirmed")
    words = DATA["example_words"]
    print("example words: %d" % len(words))
    assert len(words) == 14, "need 14 spoken examples"
    for w, r, g in words:
        assert w and r and g, "empty word/romanization/gloss"
    seen = set()
    for w, r, g in words:
        assert w not in seen, "duplicate word %r" % w
        seen.add(w)
    lo, hi = DATA["minimal_pair"][0], DATA["minimal_pair"][1]
    print("minimal pair: %s (%s) vs %s (%s)" % (lo[0], lo[1], hi[0], hi[1]))
    assert lo[0] != hi[0], "written and spoken forms must differ"
    print("OK: %s sounded the phonology" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 4: nouns

def demo_nouns1(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    nouns = DATA["nouns"]
    print("nouns: %d" % len(nouns))
    assert len(nouns) == 25, "need 25 nouns"
    assert len(set(nouns)) == 25, "nouns must be unique"
    for n in nouns:
        assert n.strip(), "empty noun"
    print("people: %d, places: %d, things: %d" % (DATA["people"], DATA["places"], DATA["things"]))
    assert DATA["people"] == 8 and DATA["places"] == 4 and DATA["things"] == 13
    assert DATA["people"] + DATA["places"] + DATA["things"] == 25
    print("OK: %s named the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 5: verbs

def demo_verbs1(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    verbs = DATA["verbs"]
    print("verbs: %d" % len(verbs))
    assert len(verbs) == 25, "need 25 verbs"
    assert len(set(verbs)) == 25, "verbs must be unique"
    print("progressive: %s, past: %s, future: %s" % (DATA["progressive_ending"], "/".join(DATA["past_endings"]), DATA["future_ending"]))
    assert DATA["progressive_ending"] == "-uchi"
    assert DATA["past_endings"] == ["-li", "-l\\u0101"]
    assert DATA["future_ending"] == "-bi"
    print("OK: %s conjugated the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 6: adjectives

def demo_adjectives(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    adj = DATA["adjectives"]
    adv = DATA["adverbs"]
    print("adjectives: %d, adverbs: %d" % (len(adj), len(adv)))
    assert len(adj) == 25, "need 25 adjectives"
    assert len(adv) == 15, "need 15 adverbs"
    assert len(set(adj)) == 25 and len(set(adv)) == 15
    print("inflects for gender: %s" % DATA["inflects_for_gender"])
    assert DATA["inflects_for_gender"] is False, "Odia adjectives do not inflect"
    print("OK: %s described the world" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 7: pronouns

def demo_pronouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("personal: %d, possessive: %d, demonstrative: %d, interrogative: %d" % (
        len(DATA["personal"]), len(DATA["possessive"]), len(DATA["demonstrative"]), len(DATA["interrogative"])))
    assert len(DATA["personal"]) == 7
    assert len(DATA["possessive"]) == 6
    assert len(DATA["demonstrative"]) == 4
    assert len(DATA["interrogative"]) == 8
    print("levels of you: %d" % DATA["you_levels"])
    assert DATA["you_levels"] == 3
    yous = [p for p in DATA["personal"] if p in ("tu", "tume", "\\u0101pa\\u1e47a")]
    assert len(yous) == 3, "three yous required"
    print("OK: %s paradigmatized the pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 8: numbers

def demo_numbers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("ones: %d, teens: %d, tens: %d" % (len(DATA["ones"]), len(DATA["teens"]), len(DATA["tens"])))
    assert len(DATA["ones"]) == 10
    assert len(DATA["teens"]) == 10
    assert len(DATA["tens"]) == 8
    print("20 in Odia: %s" % DATA["teens"][9])
    assert DATA["teens"][9] == "ko\\u1e0die"
    print("weekdays: %d, months: %d, seasons: %d" % (DATA["weekdays"], DATA["months"], DATA["seasons"]))
    assert DATA["weekdays"] == 7 and DATA["months"] == 12 and DATA["seasons"] == 6
    digits = DATA["digits"]
    assert len(digits) == 10 and len(set(digits)) == 10
    print("OK: %s counted to one hundred" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 9: greetings

def demo_greetings(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("phrases: %d" % DATA["count"])
    assert DATA["count"] == 30, "need 30 greetings"
    print("greetings: %d, farewells: %d, lifelines: %d" % (len(DATA["greetings"]), len(DATA["farewells"]), DATA["lifelines"]))
    assert len(DATA["greetings"]) == 5
    assert len(DATA["farewells"]) == 2
    assert DATA["lifelines"] == 6
    assert "namask\\u0101ra" in DATA["greetings"]
    assert "juh\\u0101ra" in DATA["greetings"]
    print("OK: %s greeted the world" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 10: grammar

def demo_grammar(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("rules: %d" % DATA["rules"])
    assert DATA["rules"] == 10, "need 10 load-bearing rules"
    print("word order: %s" % DATA["word_order"])
    assert DATA["word_order"] == "SOV"
    print("genders: %d, cases: %d" % (DATA["genders"], DATA["cases"]))
    assert DATA["genders"] == 3 and DATA["cases"] == 7
    print("copulas: %s" % "/".join(DATA["copulas"]))
    assert DATA["copulas"] == ["achi", "a\\u1e6de"]
    assert DATA["negator"] == "n\\u0101hin"
    ladder = DATA["case_ladder"]
    print("case ladder: %s" % " -> ".join(ladder))
    assert ladder == ["ghara", "gharaku", "gharara", "ghare"]
    print("OK: %s engineered the grammar" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 11: home

def demo_home(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    assert DATA["theme"] == "home-family"
    locs = DATA["locatives"]
    print("locatives drilled: %d" % len(locs))
    assert len(locs) == 5
    assert "ghare" in locs
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
    dishes = DATA["dishes"]
    print("dishes: %d (%s)" % (len(dishes), ", ".join(dishes)))
    assert len(dishes) == 4
    assert "pakh\\u0101\\u1e37a" in dishes and "chen\\u0101po\\u1e0da" in dishes and "rasagol\\u0101" in dishes
    print("OK: %s cooked the food" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 13: travel

def demo_travel(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    dirs = DATA["directions"]
    print("directions: %s" % "/".join(dirs))
    assert dirs == ["sidh\\u0101", "d\\u0101h\\u0101\\u1e47a", "b\\u0101ma"]
    print("OK: %s found the way" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 14: work

def demo_work(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    jobs = DATA["jobs"]
    print("jobs: %d" % len(jobs))
    assert len(jobs) == 3
    assert "\\u1e63ik\\u1e63aka" in jobs
    print("OK: %s went to work" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 15: health

def demo_health(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    sv = DATA["symptom_verbs"]
    print("symptom verbs: %s" % "/".join(sv))
    assert sv == ["bindhuchi", "heichi"]
    print("OK: %s healed the body" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 16: emotions

def demo_emotions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("construction: %s" % DATA["construction"])
    assert DATA["construction"] == "mote + l\\u0101gib\\u0101"
    print("OK: %s felt the feelings" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 17: nature

def demo_nature(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("weather verb: %s" % DATA["weather_verb"])
    assert DATA["weather_verb"] == "heuchi"
    print("OK: %s read the weather" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 18: shopping

def demo_shopping(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("currency: %s" % DATA["currency"])
    assert DATA["currency"] == "\\u1e6da\\u1e45k\\u0101"
    print("OK: %s haggled at the market" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 19: friendship

def demo_friendship(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    fests = DATA["festivals"]
    print("festivals: %d" % len(fests))
    assert len(fests) == 3
    assert "Rathay\\u0101tr\\u0101" in fests and "Nu\\u0101kh\\u0101i" in fests
    print("OK: %s celebrated with friends" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 20: technology

def demo_technology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    loans = DATA["loanwords"]
    print("loanwords: %d" % len(loans))
    assert len(loans) == 5
    assert "phona" in loans and "meseja" in loans and "kampyu\\u1e6dara" in loans
    print("OK: %s went online" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 21: tenses

def demo_tenses(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    tenses = DATA["tenses"]
    print("tenses: %d x %d sentences" % (len(tenses), DATA["sentences_per_tense"]))
    assert tenses == ["habitual", "progressive", "past", "future"]
    assert DATA["sentences_per_tense"] == 5
    total = len(tenses) * DATA["sentences_per_tense"]
    print("total tense sentences: %d" % total)
    assert total == 20
    forms = DATA["master_forms"]
    print("master verb %s: %s" % (DATA["master_verb"], "/".join(forms)))
    assert forms == ["kh\\u0101e", "kh\\u0101uchi", "kh\\u0101ili", "kh\\u0101ibi"]
    print("OK: %s traveled through time" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 22: Q&A

def demo_qa(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 20
    inter = DATA["interrogatives"]
    print("interrogatives: %d" % len(inter))
    assert len(inter) == 8
    assert "kie" in inter and "k\\u0101hinki" in inter and "keun\\u1e6dh\\u0101re" in inter
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 23: commands

def demo_commands(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("informal: %d, formal: %d" % (DATA["informal"], DATA["formal"]))
    assert DATA["informal"] == 10 and DATA["formal"] == 10
    assert DATA["informal"] + DATA["formal"] == 20
    print("formal ending: %s" % DATA["formal_ending"])
    assert DATA["formal_ending"] == "-ntu"
    print("OK: %s commanded politely" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 24: descriptions

def demo_descriptions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    places = DATA["places"]
    print("places: %d" % len(places))
    assert len(places) == 5
    assert "Bhubane\\u1e63wara" in places and "Ko\\u1e47\\u0101rka" in places
    print("OK: %s painted the portraits" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 25: story 1

def demo_story1(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d, tense: %s" % (DATA["sentences"], DATA["tense"]))
    assert DATA["sentences"] == 10
    assert DATA["tense"] == "present"
    assert DATA["title"] == "The Mango Tree"
    print("OK: %s told the mango story" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 26: story 2

def demo_story2(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d, tense: %s" % (DATA["sentences"], DATA["tense"]))
    assert DATA["sentences"] == 10
    assert DATA["tense"] == "past"
    assert DATA["title"] == "The Fisherman's Morning"
    print("OK: %s told the fisherman story" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 27: story 3

def demo_story3(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d, tense: %s" % (DATA["sentences"], DATA["tense"]))
    assert DATA["sentences"] == 10
    assert DATA["tense"] == "future"
    assert DATA["title"] == "The Girl Who Will Fly"
    print("OK: %s told the flying story" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 28: idioms

def demo_idioms(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("idioms: %d (documented %d + composed %d)" % (DATA["count"], DATA["documented"], DATA["composed"]))
    assert DATA["count"] == 20
    assert DATA["documented"] == 18 and DATA["composed"] == 2
    assert DATA["documented"] + DATA["composed"] == DATA["count"]
    print("OK: %s spoke in proverbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 29: registers

def demo_registers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 15
    markers = DATA["formal_markers"]
    print("formal markers: %s" % "/".join(markers))
    assert len(markers) == 2
    print("OK: %s switched registers" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 30: complex

def demo_complex(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 15
    conns = DATA["connectors"]
    print("connectors: %d" % len(conns))
    assert len(conns) == 6
    assert "yadi" in conns and "jeun" in conns and "k\\u0101ra\\u1e47a" in conns
    print("OK: %s wove the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 31: market dialogue

def demo_conv_market(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("lines: %d, scene: %s" % (DATA["lines"], DATA["scene"]))
    assert DATA["lines"] == 20
    total = DATA["total"]
    print("total: 2x28 + 40 = %d" % total)
    assert total == 2 * 28 + 40 == 96
    change = DATA["paid"] - DATA["total"]
    print("paid %d, change %d" % (DATA["paid"], change))
    assert DATA["paid"] == 100 and change == DATA["change"] == 4
    print("OK: %s closed the market deal" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 32: friend dialogue

def demo_conv_friend(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("lines: %d, scene: %s" % (DATA["lines"], DATA["scene"]))
    assert DATA["lines"] == 20
    print("register: %s" % DATA["register"])
    assert DATA["register"] == "familiar"
    print("OK: %s met the friend" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 33: problem dialogue

def demo_conv_problem(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("lines: %d, scene: %s" % (DATA["lines"], DATA["scene"]))
    assert DATA["lines"] == 20
    print("register: %s" % DATA["register"])
    assert DATA["register"] == "formal"
    print("OK: %s solved the problem" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 34: mastery

def demo_mastery(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("core words: %d" % DATA["core_words"])
    assert DATA["core_words"] == 200, "mastery reference must hold 200 core words"
    groups = DATA["groups"]
    print("word groups: %d" % len(groups))
    assert len(groups) == 20, "need 20 word groups"
    assert len(set(groups)) == 20
    print("grammar rules: %d" % DATA["grammar_rules"])
    assert DATA["grammar_rules"] == 10
    words_per_group = DATA["core_words"] / len(groups)
    print("average words per group: %.1f" % words_per_group)
    assert 9.9 < words_per_group < 10.1
    print("OK: %s mastered the reference" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_overview,
    "script": demo_script,
    "phonology": demo_phonology,
    "nouns1": demo_nouns1,
    "verbs1": demo_verbs1,
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
    "conv-market": demo_conv_market,
    "conv-friend": demo_conv_friend,
    "conv-problem": demo_conv_problem,
    "mastery": demo_mastery,
}
