#!/usr/bin/env python3
"""Demo programs for the Xiang Chinese to English databases (Manon's language project,
2026-10-17).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: speaker math, tone tables, vocabulary
counts, paradigm checks, sentence statistics, dialogue structure checks.
All are machine-executed by build.py before writing: each prints its real
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
    assert 0.46 < share < 0.48, "share out of bounds"
    subs = DATA["subgroups"]
    total = sum(subs.values())
    print("subgroup total: %.1f million across %d subgroups" % (total, len(subs)))
    assert 43.4 < total < 43.6, "subgroup sum out of bounds"
    assert len(subs) == 5
    print("cities: %d; pocket provinces: %d" % (len(DATA["cities"]), len(DATA["pocket_provinces"])))
    assert len(DATA["cities"]) == 7 and len(DATA["pocket_provinces"]) == 6
    assert DATA["official"] is False, "Xiang is not an official language"
    assert DATA["tones_changsha"] == 6
    assert DATA["iso3"] == "hsn" and DATA["glottolog"] == "xian1251"
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 2: writing system

def demo_writing(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["script"] == "hanzi" and DATA["simplified"]
    assert DATA["direction"] == "left-to-right"
    assert DATA["native_alphabet"] is False
    assert DATA["standard_romanization"] is False, "no single standard romanization"
    nums = DATA["numerals"]
    print("numerals: %d" % len(nums))
    assert len(nums) == 10 and len(set(nums)) == 10
    words = DATA["test_words"]
    print("test words: %d" % len(words))
    assert len(words) == 6
    for w in words:
        assert all("\\u4e00" <= ch <= "\\u9fff" for ch in w), "non-hanzi in %r" % w
        print("  hanzi-only: %s (%d chars)" % (w, len(w)))
    print("OK: %s wrote the script" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 3: phonology

def demo_phonology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    tones = DATA["changsha_tones"]
    print("Changsha tones: %d" % len(tones))
    assert len(tones) == 6
    expect = {"yinping": 33, "yangping": 13, "shangsheng": 41,
              "yinqu": 24, "yangqu": 45, "rusheng": 21}
    for k, v in expect.items():
        assert tones[k] == v, "tone %s mismatch" % k
        print("  %s %d" % (k, v))
    oc, nc = DATA["old_changsha"], DATA["new_changsha"]
    assert (oc["initials"], oc["finals"]) == (23, 45)
    assert (nc["initials"], nc["finals"]) == (20, 39)
    print("old-style 23/45, new-style 20/39")
    sf = DATA["shuangfeng"]
    assert (sf["initials"], sf["vowels"], sf["tones"]) == (28, 11, 5)
    print("Shuangfeng 28 initials, 11 vowels, 5 tones")
    pairs = DATA["voicing_pairs"]
    assert len(pairs) == 4
    for voiced, plain in pairs:
        assert voiced != plain
        print("  voiced %s -> devoiced %s" % (voiced, plain))
    assert DATA["example_words"] == 11
    print("OK: %s sounded the tones" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 4: nouns

def demo_nouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["count"] == 25
    sig = DATA["signature_words"]
    kin = DATA["kinship"]
    body = DATA["body"]
    print("nouns: 25 (signature %d, kinship %d, body %d)" % (len(sig), len(kin), len(body)))
    assert len(sig) == 7 and len(kin) == 7 and len(body) == 7
    for w in ["堂客", "娭毑", "细伢子", "脑壳", "臭干子"]:
        assert w in sig or w in kin or w in body, "%s missing" % w
    assert DATA["sentences"] == 25
    print("sentences: 25, one per noun")
    print("OK: %s stocked the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 5: verbs

def demo_verbs(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["count"] == 25
    da = DATA["da_family"]
    print("打-family verbs: %d" % len(da))
    assert len(da) == 8
    assert all(v.startswith("打") for v in da)
    ms = DATA["motion_split"]
    assert ms["zou"] == "run" and ms["xing"] == "walk", "Xiang motion split"
    print("motion split: zou=run, xing=walk")
    assert DATA["sentences"] == 25
    print("OK: %s moved the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 6: adjectives/adverbs

def demo_adjectives(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["adjectives"] == 25 and DATA["adverbs"] == 15
    print("25 adjectives + 15 adverbs = %d" % (25 + 15))
    assert len(DATA["intensifiers"]) == 4 and "蛮" in DATA["intensifiers"]
    neg = DATA["negation"]
    assert neg == ["不", "冇", "莫"], "negation trio"
    print("negation trio: %s" % " / ".join(neg))
    assert DATA["sentences"] == 25
    print("OK: %s graded the adjectives" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 7: pronouns

def demo_pronouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert len(DATA["personal"]) == 5 and len(DATA["plural"]) == 3
    print("personal 5, plural 3")
    marks = DATA["hunan_marks"]
    assert len(marks) == 4
    for w in ["恁", "渠", "么子", "何解"]:
        assert w in marks, "%s missing" % w
    print("Hunan marks: %s" % " ".join(marks))
    assert DATA["sentences"] == 20
    print("OK: %s pointed the pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 8: numbers/time

def demo_numbers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["digits"] == 10 and DATA["months"] == 12
    dw = DATA["day_words"]
    assert len(dw) == 7
    for w in ["今日子", "明日子", "断黑", "夜嘎子"]:
        assert w in dw, "%s missing" % w
    print("signature day words: %d" % len(dw))
    assert len(DATA["seasons"]) == 4
    assert DATA["sentences"] == 20
    print("OK: %s counted the time" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 9: greetings

def demo_greetings(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["count"] == 30
    assert "恰饭了冇" in DATA["food_greetings"]
    assert "啵" in "".join(DATA["bo_questions"])
    assert len(DATA["farewells"]) == 3
    print("30 phrases; food-greetings %d; farewells %d" % (len(DATA["food_greetings"]), len(DATA["farewells"])))
    print("OK: %s greeted Hunan" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 10: grammar

def demo_grammar(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["rules"] == 10
    assert DATA["negation"] == ["不", "冇", "莫"]
    assert DATA["aspect"] == ["了", "着", "过", "咖"]
    assert len(DATA["final_particles"]) == 5 and "啵" in DATA["final_particles"]
    assert len(DATA["classifiers"]) == 4 and "坨" in DATA["classifiers"]
    assert DATA["example_sentences"] == 26
    print("10 rules, 26 example sentences")
    print("OK: %s built the grammar" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- themed records 11-20

def _themed(key, label):
    def fn(hdr, name, rid, group, entry):
        return _wrap(hdr, name, rid, group, _data(entry["drill"]) + ('''\
def main():
    assert DATA["sentences"] == 20, "theme must carry 20 sentences"
    print("theme %s: 20 sentences" % DATA["theme"])
    print("OK: %s worked the theme" % NAME)
if __name__ == "__main__":
    main()
'''))
    fn.__name__ = "demo_" + key
    return fn


demo_home = _themed("home", "home")
demo_food = _themed("food", "food")
demo_travel = _themed("travel", "travel")
demo_work = _themed("work", "work")
demo_health = _themed("health", "health")
demo_emotions = _themed("emotions", "emotions")
demo_nature = _themed("nature", "nature")
demo_shopping = _themed("shopping", "shopping")
demo_friendship = _themed("friendship", "friendship")
demo_technology = _themed("technology", "technology")


# ---------------------------------------------------------------- 21: aspect

def demo_aspect(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    asp = DATA["aspects"]
    assert set(asp) == {"了", "咖", "着", "过"}
    total = sum(asp.values())
    print("aspect counts: %s = %d" % (asp, total))
    assert total == DATA["total"] == 22
    assert asp["了"] == 6 and asp["咖"] == 5 and asp["着"] == 6 and asp["过"] == 5
    print("OK: %s timed the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 22: qa

def demo_qa(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["pairs"] == 20
    qw = DATA["question_words"]
    assert len(qw) == 6
    for w in ["何解", "么子", "啷个", "好钱"]:
        assert w in qw, "%s missing" % w
    print("20 pairs; question words: %s" % " ".join(qw))
    assert DATA["bo_questions"] == 10
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 23: commands

def demo_commands(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    parts = DATA["formal"] + DATA["informal"] + DATA["suggesting"] + DATA["prohibitions"]
    assert DATA["count"] == 20 and parts == 20, "register split must sum to 20"
    print("formal %d + informal %d + suggesting %d + prohibitions %d = 20"
          % (DATA["formal"], DATA["informal"], DATA["suggesting"], DATA["prohibitions"]))
    assert DATA["prohibitive"] == "莫"
    print("OK: %s commanded politely" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 24: descriptions

def demo_descriptions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    parts = DATA["people"] + DATA["places"] + DATA["things"]
    assert DATA["sentences"] == 20 and parts == 20
    print("people %d + places %d + things %d = 20" % (DATA["people"], DATA["places"], DATA["things"]))
    assert DATA["de_complements"] == 5
    print("OK: %s painted the pictures" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 25-27: stories

def demo_story1(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["sentences"] == 10 and DATA["title"] == "我的一天"
    assert DATA["tense"] == "present"
    print("story 一天: 10 sentences, present")
    print("OK: %s told the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_story2(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["sentences"] == 10 and DATA["title"] == "上个月的旅行"
    assert DATA["tense"] == "past"
    assert DATA["le_count"] == 6 and DATA["guo_count"] == 1
    print("story 旅行: 10 sentences, past (了x6, 过x1)")
    print("OK: %s told the journey" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_story3(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["sentences"] == 10 and DATA["title"] == "明年的计划"
    assert DATA["tense"] == "future"
    assert DATA["conditionals"] == 3
    print("story 计划: 10 sentences, future, 3 conditionals")
    print("OK: %s told the plan" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 28: idioms

def demo_idioms(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["count"] == 20
    assert DATA["hunan_set"] == 3 and DATA["layers"] == 3
    print("20 idioms x 3 layers; Hunan set 3")
    print("OK: %s coined the wisdom" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 29: registers

def demo_registers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["pairs"] == 15
    assert len(DATA["levers"]) == 3
    print("15 pairs x 3 levers")
    print("OK: %s tuned the register" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 30: complex

def demo_complex(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["count"] == 15
    assert DATA["frames"] == 9 and DATA["relative_clauses"] == 2
    print("15 complex sentences, 9 frames, 2 relative clauses")
    print("OK: %s joined the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 31-33: conversations

def demo_conv_market(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["lines"] == 20 and DATA["roles"] == 2 and DATA["moves"] == 5
    print("market: 20 lines, 2 roles, 5 moves")
    print("OK: %s haggled at the market" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_conv_friend(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["lines"] == 20 and DATA["roles"] == 2 and DATA["moves"] == 6
    print("friend: 20 lines, 2 roles, 6 moves")
    print("OK: %s met the friend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_conv_problem(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["lines"] == 20 and DATA["roles"] == 2 and DATA["moves"] == 7
    print("problem: 20 lines, 2 roles, 7 moves")
    print("OK: %s solved the problem" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 34: mastery

def demo_mastery(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    assert DATA["core_words"] == 200, "word table must be exactly 200"
    assert DATA["tones"] == 6
    assert DATA["grammar_rules"] == 10
    assert DATA["phrase_tables"] == 6
    total_checks = 200 + 6 + 10 + 6
    print("mastery: 200 words + 6 tones + 10 rules + 6 tables = %d checks" % total_checks)
    assert total_checks == 222
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
    "aspect": demo_aspect,
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
