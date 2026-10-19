#!/usr/bin/env python3
"""Demo programs for the Hakka Chinese to English databases (Manon's language
project, 2026-10-17, batch 4 rank 31/100).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: script drills, vocabulary quizzes,
tone checks, aspect tables, sentence statistics. All are machine-executed
by build.py before writing: each prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker.

Demo signature: fn(hdr, name, rid, group, entry) where entry is the full
entry dict (drill data included).
"""

import json

_PREAMBLE = "import json\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name))


def _data(drill):
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
    assert 0.54 < share < 0.55, "share out of bounds"
    assert DATA["iso3"] == "hak", "ISO 639-3 must be hak"
    assert DATA["iso1"] is None, "Hakka has no ISO 639-1 code"
    assert DATA["glottolog"] == "hakk1236"
    print("iso3: hak, glottolog: hakk1236, no iso1")
    assert DATA["tones"] == 6
    print("tones: %d" % DATA["tones"])
    print("romanizations: %d (%s)" % (len(DATA["romanizations"]), DATA["romanizations"][1][:5]))
    assert len(DATA["romanizations"]) == 4
    assert len(DATA["dialects"]) == 6
    assert len(DATA["regions"]) == 8
    assert DATA["official_taiwan"] is True
    assert DATA["romanization_year"] == 1960
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 2: writing

def demo_writing(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    scripts = DATA["scripts"]
    print("scripts: %d" % len(scripts))
    assert len(scripts) == 5 and DATA["chosen"] == "Pinfa"
    assert DATA["direction"] == "left-to-right"
    tn = DATA["tone_numbers"]
    assert tn == {"1": "yinping", "2": "yangping", "3": "shang",
                  "4": "qu", "5": "yinru", "6": "yangru"}, "tone table wrong"
    print("tone numbers 1-6 verified")
    row = DATA["textbook_row"]
    print("textbook row: %s" % " ".join(row))
    assert row == ["fu1", "fu2", "fu3", "fu4", "fug5", "fug6"]
    nums = DATA["numerals"]
    assert len(nums) == 10
    total = sum(v for c, r, v in nums)
    assert total == 55, "digits 1-10 must sum to 55"
    print("digits 1-10 sum: %d" % total)
    assert len(DATA["test_words"]) == 4
    print("OK: %s wrote the script" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 3: phonology

def demo_phonology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("tones: %s" % ", ".join(DATA["tones"]))
    assert DATA["tones"] == ["yinping", "yangping", "shang", "qu", "yinru", "yangru"]
    assert DATA["tone_numbers"] == ["1", "2", "3", "4", "5", "6"]
    assert DATA["vowels"] == 6 and DATA["initials"] == 17
    print("vowels: 6, initials: 17")
    assert DATA["checked_finals"] == ["p", "t", "k"]
    assert DATA["nasal_finals"] == ["m", "n", "ng"]
    words = DATA["example_words"]
    print("example words: %d" % len(words))
    assert len(words) == 14
    for w, g in words:
        assert w and g, "empty word/gloss"
    a, b = DATA["tone_pair"][0], DATA["tone_pair"][1]
    print("tone pair: %s (%s) vs %s (%s)" % (a[0], a[1], b[0], b[1]))
    assert a[0] != b[0] and a[1] != b[1], "tone must change the meaning"
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
    assert len(nouns) == 25
    assert len(set(w for w, r, g in nouns)) == 25, "nouns must be unique"
    for w, r, g in nouns:
        assert w and r and g, "empty field"
    assert DATA["sentences"] == 25
    assert DATA["inflects_for_number"] is False
    have = set(w for w, r, g in nouns)
    assert "人" in have and "屋" in have and "水" in have
    print("OK: %s inventoried the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 5: verbs

def demo_verbs(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    verbs = DATA["verbs"]
    print("verbs: %d" % len(verbs))
    assert len(verbs) == 25
    assert len(set(w for w, r, g in verbs)) == 25
    assert DATA["conjugates"] is False
    a, b = DATA["tone_pair"]
    print("tone pair: %s vs %s" % (a, b))
    have = dict((w, r) for w, r, g in verbs)
    assert have["買"] == "mai1" and have["賣"] == "mai4"
    assert DATA["sentences"] == 25
    print("OK: %s drilled the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 6: adjectives

def demo_adjectives(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("adjectives: %d, adverbs: %d" % (DATA["adjectives"], DATA["adverbs"]))
    assert DATA["adjectives"] == 25 and DATA["adverbs"] == 15
    assert DATA["sentences"] == 40
    assert DATA["agreement"] is False
    print("degree words: %s" % ", ".join(DATA["degree_words"]))
    assert DATA["degree_words"] == ["dong1", "ho3", "qin3"]
    print("reduplicated: %s" % ", ".join(DATA["reduplicated"]))
    assert len(DATA["reduplicated"]) == 3
    print("OK: %s described the world" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 7: pronouns

def demo_pronouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    p = DATA["personal"]
    print("personal pronouns: %d" % len(p))
    assert len(p) == 6
    assert p[0] == "ngai2" and p[1] == "ngi2" and p[2] == "gi2"
    pm = DATA["plural_marker"]
    for plural in p[3:]:
        assert plural.endswith(pm), "plural %s missing marker %s" % (plural, pm)
    print("plural marker: %s" % pm)
    assert DATA["possessive_marker"] == "ge4"
    print("demonstratives: %d" % len(DATA["demonstratives"]))
    assert len(DATA["demonstratives"]) == 6
    print("interrogatives: %d" % len(DATA["interrogatives"]))
    assert len(DATA["interrogatives"]) == 8
    assert "mag5-ngin2" in DATA["interrogatives"]
    print("OK: %s pointed with pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 8: numbers

def demo_numbers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    digits = DATA["digits"]
    print("digits: %d" % len(digits))
    assert len(digits) == 10
    vals = [v for c, r, v in digits]
    assert vals == list(range(1, 11)), "digits must be 1-10"
    assert sum(vals) == 55
    have = dict((c, r) for c, r, v in digits)
    assert have["一"] == "yit5" and have["二"] == "ngi4" and have["十"] == "sip6"
    print("tens compounds: %d" % len(DATA["tens"]))
    assert len(DATA["tens"]) == 9
    assert DATA["classifier_two"] == "liong3"
    print("day parts: %d, week days: %d" % (len(DATA["day_parts"]), len(DATA["week"])))
    assert len(DATA["day_parts"]) == 4 and len(DATA["week"]) == 7
    assert len(DATA["deictic_days"]) == 3 and len(DATA["seasons"]) == 4
    print("OK: %s counted and timed" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 9: greetings

def demo_greetings(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("greeting phrases: %d" % DATA["phrases"])
    assert DATA["phrases"] == 30
    assert DATA["signature_greeting"] == "sit5-pon4-liau3-mau2"
    assert DATA["farewell"] == "man4-hang2"
    assert DATA["thanks"] == "do1-qia4"
    print("signature: %s" % DATA["signature_greeting"])
    assert len(DATA["categories"]) == 6
    print("OK: %s greeted the world" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 10: grammar

def demo_grammar(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("grammar rules: %d" % DATA["rules"])
    assert DATA["rules"] == 10
    print("aspects: %s" % ", ".join(DATA["aspects"]))
    assert DATA["aspects"] == ["liau3", "go4", "voi4", "gin3"]
    assert DATA["negators"] == ["m2", "mau2"]
    assert DATA["question_strategies"] == ["A-not-A", "ma1"]
    print("classifiers: %s" % ", ".join(DATA["classifiers"]))
    assert DATA["classifiers"] == ["ge4", "bun3", "zag5"]
    assert DATA["sentences"] == 14
    print("OK: %s assembled the engine" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 11: home

def demo_home(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("home sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    assert DATA["theme"] == "home"
    print("kinship terms: %d" % len(DATA["kinship"]))
    assert len(DATA["kinship"]) == 8
    assert "a1-me1" in DATA["kinship"]
    print("rooms: %s" % ", ".join(DATA["rooms"]))
    assert DATA["rooms"] == ["tang1-ha1", "fong2-gien1", "cu2-fong2"]
    print("OK: %s kept the household" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 12: food

def demo_food(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("food sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    assert DATA["theme"] == "food"
    print("signature dishes: %d" % len(DATA["dishes"]))
    assert len(DATA["dishes"]) == 3
    assert "lui2-ca2" in DATA["dishes"]
    print("taste words: %s" % ", ".join(DATA["taste_words"]))
    assert DATA["taste_words"] == ["ham2", "tiam2", "ho3-sit5"]
    print("OK: %s set the table" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 13: travel

def demo_travel(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("travel sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    assert DATA["theme"] == "travel"
    print("transport: %s" % ", ".join(DATA["transport"]))
    assert DATA["transport"] == ["fo3-ca1", "ba1-sii4", "tit5-sii4", "fi1-gi1"]
    print("question frames: %d" % len(DATA["question_frames"]))
    assert len(DATA["question_frames"]) == 4
    assert "cai4-nai3" in DATA["question_frames"]
    print("OK: %s mapped the journey" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 14: work

def demo_work(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("work sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    assert DATA["theme"] == "work"
    print("work words: %d, school words: %d" % (len(DATA["work_words"]), len(DATA["school_words"])))
    assert len(DATA["work_words"]) == 4 and len(DATA["school_words"]) == 4
    assert "kau3-shi4" in DATA["school_words"]
    print("OK: %s worked and studied" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 15: health

def demo_health(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("health sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    assert DATA["theme"] == "health"
    print("body parts: %d" % len(DATA["body_parts"]))
    assert len(DATA["body_parts"]) == 6
    assert DATA["pain_pattern"] == "tung4"
    print("symptoms: %s" % ", ".join(DATA["symptoms"]))
    assert DATA["symptoms"] == ["fat5-sau1", "gam3-mau4", "kat5"]
    print("OK: %s tended the body" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 16: emotions

def demo_emotions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("emotion sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    assert DATA["theme"] == "emotions"
    print("emotion words: %d" % len(DATA["emotion_words"]))
    assert DATA["emotion_words"] == ["fon1-hi3", "song1-xim1", "neu4",
                                    "giang1", "oi4", "ji4-ngoi4"]
    print("comfort patterns: %d" % DATA["comfort_patterns"])
    assert DATA["comfort_patterns"] == 3
    print("OK: %s felt everything" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 17: nature

def demo_nature(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("nature sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    assert DATA["theme"] == "nature"
    print("weather verbs: %s" % ", ".join(DATA["weather_verbs"]))
    assert DATA["weather_verbs"] == ["log6-sui3", "cut5-ngit5", "hi3-fung1", "da3-lui2"]
    print("animals: %d" % len(DATA["animals"]))
    assert len(DATA["animals"]) == 6
    print("OK: %s walked the countryside" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 18: shopping

def demo_shopping(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("shopping sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    assert DATA["theme"] == "shopping"
    print("bargain ladder: %s" % " -> ".join(DATA["bargain_steps"]))
    assert DATA["bargain_steps"] == ["gi3-do1-qian2", "tai4-gui4",
                                    "piang2-yit5-diam3", "siin2-gau1"]
    print("pay words: %s" % ", ".join(DATA["pay_words"]))
    assert DATA["pay_words"] == ["zau3-qian2", "set5-ka1", "hien4-gim1"]
    print("OK: %s struck the bargain" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 19: friendship

def demo_friendship(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("friendship sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    assert DATA["theme"] == "friendship"
    print("meeting script steps: %d" % DATA["meeting_script"])
    assert DATA["meeting_script"] == 4
    print("wishes: %s" % ", ".join(DATA["wishes"]))
    assert len(DATA["wishes"]) == 3
    assert DATA["social_verb"] == "liau4"
    print("OK: %s kept the fellowship" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 20: technology

def demo_technology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("technology sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    assert DATA["theme"] == "technology"
    print("phone: %s" % ", ".join(DATA["phone_words"]))
    assert DATA["phone_words"] == ["tien4-fa4", "su3-gi1", "cung1-tien4"]
    print("net: %s" % ", ".join(DATA["net_words"]))
    assert DATA["net_words"] == ["song1-miong3", "miong3-log6", "xin4-xit5"]
    print("computer: %s" % ", ".join(DATA["computer_words"]))
    assert DATA["computer_words"] == ["tien4-nau3", "da3-sii4", "cun2-dong4"]
    print("OK: %s wired the future" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 21: tenses

def demo_tenses(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("aspect patterns: %d" % len(DATA["patterns"]))
    assert DATA["patterns"] == ["bare", "gin3/cai4", "liau3", "go4", "voi4/oi4"]
    assert DATA["sentences_per"] == 5
    total = DATA["sentences_per"] * len(DATA["patterns"])
    print("total sentences: %d" % total)
    assert total == DATA["total_sentences"] == 25
    print("aspect words: %s" % ", ".join(DATA["aspect_words"]))
    assert len(DATA["aspect_words"]) == 6
    print("OK: %s marked the time" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 22: qa

def demo_qa(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("question/answer pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 20
    print("interrogatives: %d" % len(DATA["interrogatives"]))
    assert len(DATA["interrogatives"]) == 7
    assert "zo4-ma1" in DATA["interrogatives"]
    print("yes-no strategies: %s" % ", ".join(DATA["yes_no"]))
    assert DATA["yes_no"] == ["A-not-A", "ma1"]
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 23: commands

def demo_commands(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("commands: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    assert DATA["informal"] == 10 and DATA["formal"] == 10
    assert DATA["informal"] + DATA["formal"] == DATA["sentences"]
    assert DATA["politeness"] == "qiang3"
    print("forbidders: %s" % ", ".join(DATA["forbidders"]))
    assert DATA["forbidders"] == ["m2-ho3", "mog5"]
    print("OK: %s commanded politely" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 24: descriptions

def demo_descriptions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("descriptions: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("doubled adjectives: %s" % ", ".join(DATA["doubled_adjectives"]))
    assert DATA["doubled_adjectives"] == ["go1-go1-tai4-tai4"]
    print("place classifiers: %s" % ", ".join(DATA["place_classifiers"]))
    assert DATA["place_classifiers"] == ["gien1", "tiau2", "sung1"]
    print("heritage: %s" % ", ".join(DATA["heritage"]))
    assert DATA["heritage"] == ["vui2-liung2-vuk5"]
    print("OK: %s painted the portraits" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 25: story1

def demo_story1(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story lines: %d" % DATA["lines"])
    assert DATA["lines"] == 4
    assert DATA["sentences"] == 10
    assert DATA["quoted"] is True
    assert DATA["romanization"] == "Pha̍k-fa-sṳ"
    print("key words: %s" % ", ".join(DATA["key_words"]))
    assert DATA["key_words"] == ["cii4-yiu2", "zun1-ngiam2", "kien2-li4", "pin2-den3"]
    print("OK: %s read the charter" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 26: story2

def demo_story2(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story lines: %d" % DATA["lines"])
    assert DATA["lines"] == 10
    assert DATA["tense"] == "past"
    assert DATA["composed"] is True
    print("past markers: %s" % ", ".join(DATA["past_markers"]))
    assert DATA["past_markers"] == ["liau3", "dau4-liau3"]
    print("migration stops: %d" % len(DATA["stops"]))
    assert DATA["stops"] == ["Zhongyuan", "Jiangxi", "Fujian", "Guangdong"]
    print("OK: %s walked the long road" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 27: story3

def demo_story3(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story lines: %d" % DATA["lines"])
    assert DATA["lines"] == 10
    assert DATA["tense"] == "future"
    assert DATA["future_marker"] == "voi4"
    assert DATA["conditional"] == "ngiog6-he4"
    assert DATA["composed"] is True
    print("OK: %s sealed the promise" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 28: idioms

def demo_idioms(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("idioms: %d" % DATA["idioms"])
    assert DATA["idioms"] == 20
    assert DATA["quoted"] is True
    print("land vow: %s" % DATA["land_vow"])
    assert DATA["land_vow"] == "寧賣祖宗田，不忘祖宗言"
    print("speech vow: %s" % DATA["speech_vow"])
    assert DATA["speech_vow"] == "認聲不認姓"
    print("OK: %s spoke the maxims" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 29: registers

def demo_registers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("register pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 15
    print("formal markers: %s" % ", ".join(DATA["formal_markers"]))
    assert DATA["formal_markers"] == ["qiang3", "qiang3-mun4", "lo2-fan2", "siin2-mung2"]
    print("letter opening: %s" % DATA["letter_opening"])
    assert DATA["letter_opening"] == "ngin4-qi3-zhe3"
    print("OK: %s weighed the courtesies" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 30: complex

def demo_complex(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("complex sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 15
    assert DATA["parsed"] is True
    print("connectors: %d" % len(DATA["connectors"]))
    assert len(DATA["connectors"]) == 5
    assert "ngiog6-he4-qiu4" in DATA["connectors"]
    print("OK: %s raised the long-houses" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 31: conv_market

def demo_conv_market(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    assert DATA["speakers"] == ["A", "B"]
    print("market words: %s" % ", ".join(DATA["market_words"]))
    assert DATA["market_words"] == ["ngiam4", "yit5-kiung4", "su3-ang1"]
    print("arc: %s" % " -> ".join(DATA["arc"]))
    assert DATA["arc"] == ["greet", "price", "bargain", "buy", "pay", "change", "farewell"]
    print("OK: %s traded at the market" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 32: conv_friend

def demo_conv_friend(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    assert DATA["speakers"] == ["A", "B"]
    print("formulas: %s" % ", ".join(DATA["formulas"]))
    assert DATA["formulas"] == ["nai3-li1-fa4", "cii4-ga1-ngin2", "liau4"]
    print("arc: %s" % " -> ".join(DATA["arc"]))
    assert len(DATA["arc"]) == 5
    print("OK: %s met the old friend" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 33: conv_problem

def demo_conv_problem(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    assert DATA["speakers"] == ["A", "B"]
    print("repair words: %s" % ", ".join(DATA["repair_words"]))
    assert DATA["repair_words"] == ["sui3-heu2", "sui3-zat5", "sii1-fu4"]
    print("arc steps: %d" % len(DATA["arc"]))
    assert len(DATA["arc"]) == 8
    assert DATA["arc"][0] == "trouble" and DATA["arc"][-1] == "seal"
    print("OK: %s fixed the leak" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 34: mastery

def demo_mastery(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    words = DATA["core_words"]
    print("core words: %d" % len(words))
    assert len(words) == 200, "mastery needs exactly 200 core words"
    assert len(set(w for w, r, g in words)) == 200, "core words must be unique"
    for w, r, g in words:
        assert w and r and g, "empty word/gloss"
    print("grammar rules: %d, phrase tables: %d" % (DATA["grammar_rules"], DATA["phrase_tables"]))
    assert DATA["grammar_rules"] == 10 and DATA["phrase_tables"] == 5
    have = set(w for w, r, g in words)
    for lm in ["屋下", "多謝", "尞", "客家話"]:
        assert lm in have, "landmark missing: %s" % lm
    print("landmarks present: 屋下, 多謝, 尞, 客家話")
    print("OK: %s sealed the mastery" % NAME)
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
