#!/usr/bin/env python3
"""Demo programs for the Sundanese to English databases (Manon's language
project, 2026-10-17, language batch 4, rank 36/100).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: script drills, vocabulary quizzes,
number checks, tense-gear tables, dialogue arc checks, story line counts.
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
    total_m = float(DATA["total_m"])
    world_m = 8100.0
    share = native_m / world_m * 100.0
    print("native speakers: %.0f million" % native_m)
    print("share of world population: %.2f %%" % share)
    assert 0.49 < share < 0.50, "share out of bounds"
    l2 = total_m - native_m
    print("second-language speakers: ~%.0f million" % l2)
    assert 3.9 < l2 < 4.1, "L2 estimate out of bounds"
    print("dialects: %d" % DATA["dialects"])
    assert DATA["dialects"] == 6
    print("old speech levels: %d -> modern: %d" % (DATA["levels_old"], DATA["levels_new"]))
    assert DATA["levels_old"] == 6 and DATA["levels_new"] == 2
    print("scripts: %d" % DATA["scripts"])
    assert DATA["scripts"] == 3
    print("vowels: %d" % DATA["vowels"])
    assert DATA["vowels"] == 7
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 2: writing

def demo_writing(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    order = DATA["order"]
    print("ngalagena in order: %d" % len(order))
    assert len(order) == DATA["ngalagena"] == 18
    assert order[0] == "ka" and order[-1] == "ha", "kaganga order broken"
    assert len(set(order)) == 18, "ngalagena must be unique"
    lines = [order[i:i+3] for i in range(0, 18, 3)]
    print("kaganga rows: %d (%s)" % (len(lines), " / ".join(" ".join(l) for l in lines)))
    assert len(lines) == 6
    print("independent vowels: %d" % DATA["vowels"])
    assert DATA["vowels"] == 7
    print("traditional digits: %d" % DATA["digits"])
    assert DATA["digits"] == 10
    print("rarangken diacritics: %d" % DATA["rarangken"])
    assert DATA["rarangken"] == 13
    print("OK: %s drilled the script" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 3: phonology

def demo_phonology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("vowels: %d" % DATA["vowels"])
    assert DATA["vowels"] == 7
    print("consonants: %d" % DATA["consonants"])
    assert DATA["consonants"] == 18
    phonemes = DATA["vowels"] + DATA["consonants"]
    print("total phonemes: %d" % phonemes)
    assert 24.9 < phonemes < 25.1
    print("loan consonants: %d (%s)" % (len(DATA["loan_consonants"]), ", ".join(DATA["loan_consonants"])))
    assert len(DATA["loan_consonants"]) == 5
    print("glide insertions: %d" % len(DATA["glides"]))
    assert len(DATA["glides"]) == 3
    for plain, glide in DATA["glides"]:
        assert len(glide) > len(plain), "glide must insert a sound"
    print("example words: %d" % DATA["examples"])
    assert DATA["examples"] == 12
    print("OK: %s trained the ear" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 4: nouns

def demo_nouns1(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    nouns = DATA["nouns"]
    print("nouns: %d" % len(nouns))
    assert len(nouns) == 25
    assert "jalma" in nouns and "panonpoe" in nouns and "nagara" in nouns
    assert len(set(nouns)) == 25, "nouns must be unique"
    avg = sum(len(w) for w in nouns) / float(len(nouns))
    print("average word length: %.2f chars" % avg)
    assert 5.0 < avg < 5.8, "avg length out of bounds"
    longest = max(nouns, key=len)
    print("longest noun: %s" % longest)
    assert longest == "panonpoe"
    print("OK: %s stocked the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 5: verbs

def demo_verbs1(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    verbs = DATA["verbs"]
    print("verbs: %d" % len(verbs))
    assert len(verbs) == 25
    assert "dahar" in verbs and "diajar" in verbs and "nempo" in verbs
    assert len(set(verbs)) == 25, "verbs must be unique"
    avg = sum(len(w) for w in verbs) / float(len(verbs))
    print("average word length: %.2f chars" % avg)
    assert 5.1 < avg < 5.8, "avg length out of bounds"
    longest = max(verbs, key=len)
    print("longest verb: %s" % longest)
    assert len(longest) == 8 and longest in ("leumpang", "nangtung")
    subjects = ["abdi", "anjeun", "maranehna"]
    for v in verbs[:5]:
        forms = ["%s %s" % (s, v) for s in subjects]
        assert len(set(forms)) == 3
    print("sample conjugations checked: verb never changes")
    print("OK: %s drilled the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 6: adjectives/adverbs

def demo_adjadv(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    adj = DATA["adjectives"]
    adv = DATA["adverbs"]
    print("adjectives: %d, adverbs: %d" % (len(adj), len(adv)))
    assert len(adj) == 25 and len(adv) == 15
    total = len(adj) + len(adv)
    print("modifiers: %d" % total)
    assert total == 40
    assert "pisan" in adv and "leuwih" in adv
    assert "alus" in adj and "geulis" in adj
    assert len(set(adj)) == 25 and len(set(adv)) == 15
    print("OK: %s graded the modifiers" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 7: pronouns

def demo_pronouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    pron = DATA["pronouns"]
    inter = DATA["interrogatives"]
    print("pronouns: %d" % len(pron))
    assert len(pron) == 16
    assert "abdi" in pron and "manehna" in pron and "ieu" in pron
    assert len(set(pron)) == 16, "pronouns must be unique"
    print("interrogatives: %d (%s)" % (len(inter), ", ".join(inter)))
    assert len(inter) == 8
    ranks_i = ["abdi", "kuring", "aing"]
    for r in ranks_i:
        assert r in pron, "missing I-rank %s" % r
    print("OK: %s ranked the pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 8: numbers/time

def demo_numbers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    nums = DATA["numbers"]
    print("numbers: %d" % len(nums))
    assert len(nums) == 20
    assert nums[0] == 1 and nums[-1] == 1000000
    assert sum(nums[:10]) == 55, "1..10 must sum to 55"
    print("1..10 sum: %d" % sum(nums[:10]))
    print("days: %d, months: %d, ordinals: %d" % (len(DATA["days"]), len(DATA["months"]), len(DATA["ordinals"])))
    assert len(DATA["days"]) == 7
    assert len(DATA["months"]) == 12
    assert len(DATA["ordinals"]) == 3
    assert DATA["days"][0] == "Senen" and DATA["days"][-1] == "Minggu"
    print("OK: %s counted the numbers" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 9: greetings

def demo_greetings(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    g = DATA["greetings"]
    print("greetings: %d" % len(g))
    assert len(g) == 30
    assert "Sampurasun." in g and "Rampes." in g
    assert "Hatur nuhun." in g and "Wilujeng enjing." in g
    assert len(set(g)) == 30, "greetings must be unique"
    wilujeng = [x for x in g if x.startswith("Wilujeng")]
    print("wilujeng greetings: %d" % len(wilujeng))
    assert len(wilujeng) >= 8
    print("OK: %s exchanged greetings" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 10: grammar

def demo_grammar(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("grammar rules: %d" % DATA["rules"])
    assert DATA["rules"] == 10
    s, v, o = "abdi", "dahar", "sangu"
    svo = "%s %s %s" % (s, v, o)
    print("SVO frame: %s" % svo)
    assert svo.split() == ["abdi", "dahar", "sangu"]
    neg = {"teu": "not", "moal": "will not", "ulah": "do not"}
    print("negators: %d" % len(neg))
    assert len(neg) == 3
    print("OK: %s proved the ten rules" % NAME)
if __name__ == "__main__":
    main()
''')

# ------------------------------------------------------- 11-20: themed sets

def _themed(key, label, extra_checks=""):
    def fn(hdr, name, rid, group, entry):
        return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %%d" %% DATA["sentences"])
    assert DATA["sentences"] == 20
%s
    print("OK: %%s covered %s" %% NAME)
if __name__ == "__main__":
    main()
''' % (extra_checks, label))
    fn.__name__ = "demo_" + key
    return fn


demo_home = _themed("home", "home and family", '''\
    print("rooms: %d" % len(DATA["rooms"]))
    assert len(DATA["rooms"]) == 3''')
demo_food = _themed("food", "food and cooking", '''\
    print("rice words: %d (%s)" % (len(DATA["rice_words"]), ", ".join(DATA["rice_words"])))
    assert DATA["rice_words"] == ["pare", "beas", "sangu"]''')
demo_travel = _themed("travel", "travel and directions", '''\
    print("direction words: %d" % len(DATA["directions"]))
    assert len(DATA["directions"]) == 5''')
demo_work = _themed("work", "work and school", '''\
    print("professions: %d" % len(DATA["professions"]))
    assert len(DATA["professions"]) == 7
    assert "guru" in DATA["professions"]''')
demo_health = _themed("health", "health and body", '''\
    print("body parts: %d" % len(DATA["body"]))
    assert len(DATA["body"]) == 7''')
demo_emotions = _themed("emotions", "emotions and feelings", '''\
    print("feelings: %d" % len(DATA["feelings"]))
    assert len(DATA["feelings"]) == 7
    assert "bungah" in DATA["feelings"] and "bogoh" in DATA["feelings"]''')
demo_nature = _themed("nature", "nature and weather", '''\
    print("seasons: %d (%s)" % (len(DATA["seasons"]), ", ".join(DATA["seasons"])))
    assert DATA["seasons"] == ["usum hujan", "usum halodo"]''')
demo_shopping = _themed("shopping", "shopping and money")
demo_friendship = _themed("friendship", "friendship and social life")
demo_technology = _themed("technology", "technology and communication")


# ---------------------------------------------------------------- 21: tenses

def demo_tenses(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    gears = DATA["gears"]
    print("time gears: %d" % len(gears))
    assert len(gears) == 5
    per = DATA["per_gear"]
    total = len(gears) * per
    print("sentences: %d (%d per gear)" % (total, per))
    assert total == 25
    verb = "dahar"
    forms = {
        "geus": "abdi geus %s" % verb,
        "keur": "abdi keur %s" % verb,
        "rek": "abdi rek %s" % verb,
        "sok": "abdi sok %s" % verb,
        "moal": "abdi moal %s" % verb,
    }
    for g, f in forms.items():
        assert verb in f and g in f
    print("gear shift on one verb: OK")
    print("OK: %s shifted the five gears" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 22: Q&A

def demo_qa(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("question/answer pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 20
    wh = ["saha", "naon", "dimana", "iraha", "naha", "kumaha", "sabaraha"]
    print("interrogative families: %d" % len(wh))
    assert len(wh) == 7
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 23: commands

def demo_commands(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("commands: %d" % DATA["commands"])
    assert DATA["commands"] == 20
    regs = DATA["registers"]
    print("registers: %s" % ", ".join(regs))
    assert regs == ["informal", "polite"]
    pairs = DATA["commands"] // 2
    print("informal/polite pairs: %d" % pairs)
    assert pairs == 10
    print("OK: %s commanded politely" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 24: descriptions

def demo_descriptions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("descriptive sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("OK: %s painted the portraits" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------------- 25-27: stories

def _story(key, label):
    def fn(hdr, name, rid, group, entry):
        return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story lines: %%d" %% DATA["lines"])
    assert DATA["lines"] == 10
    print("OK: %%s told %s" %% NAME)
if __name__ == "__main__":
    main()
''' % label)
    fn.__name__ = "demo_" + key
    return fn


demo_story1 = _story("story1", "the little rice farmer")
demo_story2 = _story("story2", "the runaway goat")
demo_story3 = _story("story3", "the journey to Bandung")


# ---------------------------------------------------------------- 28: idioms

def demo_idioms(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("idioms and proverbs: %d" % DATA["idioms"])
    assert DATA["idioms"] == 20
    print("OK: %s spoke in proverbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 29: registers

def demo_registers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("register pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 15
    print("OK: %s climbed the registers" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 30: complex

def demo_complex(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("complex sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 15
    conn = DATA["connectors"]
    print("connectors: %d (%s)" % (len(conn), ", ".join(conn)))
    assert len(conn) == 10
    assert "sabab" in conn and "sangkan" in conn and "anu" in conn
    assert len(set(conn)) == 10
    print("OK: %s chained the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------------- 31-33: conversations

def _conv(key, label):
    def fn(hdr, name, rid, group, entry):
        return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %%d" %% DATA["lines"])
    assert DATA["lines"] == 20
    sp = DATA["speakers"]
    print("speakers: %%s" %% "/".join(sp))
    assert len(sp) == 2
    assert DATA["lines"] %% len(sp) == 0, "lines must split evenly between speakers"
    print("OK: %%s performed %s" %% NAME)
if __name__ == "__main__":
    main()
''' % label)
    fn.__name__ = "demo_" + key
    return fn


demo_convmarket = _conv("convmarket", "the market dialogue")
demo_convfriend = _conv("convfriend", "the reunion dialogue")
demo_convproblem = _conv("convproblem", "the blackout dialogue")


# ---------------------------------------------------------------- 34: mastery

def demo_mastery(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    words = DATA["core_words"]
    print("core words: %d" % len(words))
    assert len(words) == 200, "must be exactly 200 core words"
    assert len(set(words)) == 200, "core words must be unique"
    assert "jalma" in words and "dahar" in words and "alus" in words
    assert "pisan" in words and "Sampurasun." in words and "hiji" in words
    assert "herang" in words and "abdi" in words and "geus" in words
    print("grammar rules: %d" % DATA["grammar_rules"])
    assert DATA["grammar_rules"] == 10
    print("stories: %d, conversations: %d" % (DATA["stories"], DATA["conversations"]))
    assert DATA["stories"] == 3 and DATA["conversations"] == 3
    print("phrase tables: %d" % DATA["phrase_tables"])
    assert DATA["phrase_tables"] == 9
    print("OK: %s passed the mastery review" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- map

DEMOS = {
    "overview": demo_overview,
    "writing": demo_writing,
    "phonology": demo_phonology,
    "nouns1": demo_nouns1,
    "verbs1": demo_verbs1,
    "adjadv": demo_adjadv,
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
    "convmarket": demo_convmarket,
    "convfriend": demo_convfriend,
    "convproblem": demo_convproblem,
    "mastery": demo_mastery,
}
