#!/usr/bin/env python3
"""Demo programs for the Indonesian to English databases (Manon's language project,
2026-10-17).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: alphabet drills, vocabulary quizzes,
number builders, tense tables, sentence statistics. All are
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
    assert 0.53 < share < 0.54, "share out of bounds"
    l2 = total_m - native_m
    print("second-language speakers: ~%.0f million" % l2)
    assert 166.9 < l2 < 167.1, "L2 estimate out of bounds"
    print("islands: %d" % DATA["islands"])
    assert DATA["islands"] == 17000
    print("regional languages: %d" % DATA["regional_langs"])
    assert DATA["regional_langs"] == 700
    assert DATA["pledge_year"] == 1928 and DATA["indep_year"] == 1945
    print("regions: %d" % len(DATA["regions"]))
    assert len(DATA["regions"]) == 8
    assert DATA["iso1"] == "id" and DATA["iso3"] == "ind"
    print("registers: %d" % len(DATA["registers"]))
    assert len(DATA["registers"]) == 6
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 2: writing system

def demo_writing(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    letters = DATA["letters"]
    print("Rumi letters: %d" % len(letters))
    assert len(letters) == 26, "Indonesian alphabet must be 26"
    assert len(set(letters)) == 26, "letters must be unique"
    assert letters == sorted(letters), "alphabet must run a-z"
    print("vowels: %d" % len(DATA["vowels"]))
    assert DATA["vowels"] == ["a", "e", "i", "o", "u"]
    print("digraphs: %s" % " ".join(DATA["digraphs"]))
    assert DATA["digraphs"] == ["kh", "ng", "ny", "sy"]
    for dg in DATA["digraphs"]:
        assert len(dg) == 2, "digraph must be two letters"
    print("diphthongs: %s" % " ".join(DATA["diphthongs"]))
    assert DATA["diphthongs"] == ["ai", "au", "oi"]
    for loan in DATA["loan_letters"]:
        assert loan in letters, "loan letter %s missing" % loan
    assert DATA["direction"] == "left-to-right"
    print("reduplication example: %s" % DATA["redupe_example"])
    assert DATA["redupe_example"] == "buku-buku"
    assert DATA["eyd"] == 1972 and DATA["ebi"] == 2015
    print("OK: %s spelled the alphabet" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 3: pronunciation

def demo_pronunciation(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("vowels: %d (two-faced: %s)" % (DATA["vowel_count"], DATA["two_face_vowel"]))
    assert DATA["vowel_count"] == 5 and DATA["two_face_vowel"] == "e"
    print("tones: %d" % DATA["tones"])
    assert DATA["tones"] == 0, "Indonesian has no tones"
    print("stress rule: %s" % DATA["stress_rule"])
    assert DATA["stress_rule"] == "penultimate"
    tricky = DATA["tricky"]
    print("tricky consonants: %s" % ", ".join(tricky))
    assert "c" in tricky and "r" in tricky
    for dg, anchor in DATA["digraph_sounds"].items():
        print("  %s sounds like %s" % (dg, anchor))
    assert DATA["digraph_sounds"]["ny"] == "canyon"
    examples = DATA["examples"]
    print("spoken examples: %d" % len(examples))
    assert len(examples) == 12
    assert "terima kasih" in examples and "nyanyi" in examples
    print("OK: %s sounded the language" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 4: nouns

def demo_nouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    nouns = DATA["nouns"]
    print("core nouns: %d" % len(nouns))
    assert len(nouns) == 25, "must be 25 nouns"
    assert len(set(nouns)) == 25, "nouns must be unique"
    assert DATA["forms_per_noun"] == 1, "one invariant form"
    assert DATA["genders"] == 0 and DATA["cases"] == 0
    avg = sum(len(w) for w in nouns) / len(nouns)
    print("average noun length: %.2f letters" % avg)
    assert 4.0 < avg < 6.0, "avg length out of bounds"
    for must in ("orang", "rumah", "makanan"):
        assert must in nouns, "%s missing" % must
    print("OK: %s stocked the noun-hoard" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 5: verbs

def demo_verbs(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    verbs = DATA["verbs"]
    print("core verbs: %d" % len(verbs))
    assert len(verbs) == 25 and len(set(verbs)) == 25
    assert DATA["conjugations"] == 0, "verbs never conjugate"
    me_verbs = [v for v in verbs if v.startswith("me")]
    print("me- prefixed verbs: %d" % len(me_verbs))
    assert len(me_verbs) == DATA["me_prefix_verbs"] == 10
    roots = {"membaca": "baca", "menulis": "tulis", "membeli": "beli"}
    for full, root in roots.items():
        assert full in verbs, "%s missing" % full
        print("  %s -> root %s" % (full, root))
    for stative in ("tahu", "suka"):
        assert stative in verbs and not stative.startswith("me")
    print("OK: %s drilled the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 6: adjectives/adverbs

def demo_adjectives(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("adjectives: %d / adverbs: %d" % (DATA["adjectives"], DATA["adverbs"]))
    assert DATA["adjectives"] == 25 and DATA["adverbs"] == 15
    print("total modifiers: %d" % (DATA["adjectives"] + DATA["adverbs"]))
    assert DATA["adjectives"] + DATA["adverbs"] == 40
    assert DATA["order"] == "noun-adjective"
    assert DATA["agreement_forms"] == 0, "no agreement ever"
    print("degree words: %s" % ", ".join(DATA["degree_words"]))
    assert len(DATA["degree_words"]) == 4
    assert "sangat" in DATA["degree_words"]
    print("OK: %s graded the modifiers" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 7: pronouns

def demo_pronouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    p = DATA["personal"]
    print("personal pronouns: %d" % len(p))
    assert len(p) == 10 and len(set(p)) == 10
    assert DATA["case_forms"] == 1, "no case changes"
    for must in ("saya", "aku", "kamu", "Anda", "beliau", "kami", "kita"):
        assert must in p, "%s missing" % must
    print("possessive suffixes: %s" % " ".join(DATA["possessive_suffixes"]))
    assert DATA["possessive_suffixes"] == ["-ku", "-mu", "-nya"]
    print("demonstratives: %d" % len(DATA["demonstratives"]))
    assert len(DATA["demonstratives"]) == 5
    print("interrogatives: %d" % len(DATA["interrogatives"]))
    assert len(DATA["interrogatives"]) == 8
    assert "di mana" in DATA["interrogatives"]
    print("OK: %s mapped the pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 8: numbers

def demo_numbers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    roots = DATA["roots"]
    print("number roots: %d" % len(roots))
    assert len(roots) == 10 and roots[0] == "satu" and roots[9] == "sepuluh"
    builders = DATA["builders"]
    print("builders: %s" % ", ".join(builders))
    assert len(builders) == 6
    print("specials: %s" % ", ".join(DATA["specials"]))
    assert DATA["specials"] == ["sebelas", "seratus", "seribu"]
    # build 2026 from parts and verify against the drill reading
    parts = {"ribu": 1000, "ratus": 100, "puluh": 10}
    n = DATA["test_number"]
    thou, rem = divmod(n, 1000)
    thou_word = "dua ribu" if thou == 2 else "%s ribu" % roots[thou - 1]
    tens, ones = divmod(rem, 10)
    built = "%s %s puluh %s" % (thou_word, roots[tens - 1], roots[ones - 1])
    print("2026 reads: %s" % built)
    assert built == DATA["test_reading"], "number builder drift"
    print("days: %d / months: %d / dayparts: %d"
          % (len(DATA["days"]), DATA["months"], len(DATA["dayparts"])))
    assert len(DATA["days"]) == 7 and DATA["months"] == 12
    assert DATA["days"][0] == "Senin" and DATA["days"][-1] == "Minggu"
    print("OK: %s counted to the millions" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 9: greetings

def demo_greetings(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("phrases: %d" % DATA["phrases"])
    assert DATA["phrases"] == 30
    hours = DATA["selamat_hours"]
    print("selamat dayparts: %d" % len(hours))
    assert set(hours) == {"pagi", "siang", "sore", "malam"}
    print("farewell pair: %s" % " / ".join(DATA["farewell_pair"]))
    assert DATA["farewell_pair"] == ["selamat jalan", "selamat tinggal"]
    print("politeness softeners: %s" % ", ".join(DATA["politeness"]))
    assert len(DATA["politeness"]) == 4
    print("OK: %s greeted the day" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 10: grammar

def demo_grammar(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("load-bearing rules: %d" % DATA["rules"])
    assert DATA["rules"] == 10
    assert DATA["word_order"] == "SVO"
    assert DATA["conjugations"] == 0
    print("negators: %s" % ", ".join(DATA["negators"]))
    assert DATA["negators"] == ["tidak", "bukan", "jangan"]
    print("classifiers: %d" % len(DATA["classifiers"]))
    assert len(DATA["classifiers"]) == 6
    assert "orang" in DATA["classifiers"] and "ekor" in DATA["classifiers"]
    print("affixes: %d" % len(DATA["affixes"]))
    assert len(DATA["affixes"]) == 9
    print("place prepositions: %s" % ", ".join(DATA["place_preps"]))
    assert DATA["place_preps"] == ["di", "ke", "dari"]
    print("OK: %s raised the ten pillars" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 11: home

def demo_home(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("kinship terms: %d" % len(DATA["kinship"]))
    assert len(DATA["kinship"]) == 9
    for must in ("kakak", "adik", "kakek"):
        assert must in DATA["kinship"], "%s missing" % must
    print("rooms: %d" % len(DATA["rooms"]))
    assert len(DATA["rooms"]) == 7
    assert "ruang tamu" in DATA["rooms"] and "dapur" in DATA["rooms"]
    print("OK: %s walked through the house" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 12: food

def demo_food(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("rice trilogy: %s" % ", ".join(DATA["rice_words"]))
    assert DATA["rice_words"] == ["padi", "beras", "nasi"]
    print("dishes: %d" % len(DATA["dishes"]))
    assert len(DATA["dishes"]) == 6
    assert "rendang" in DATA["dishes"]
    print("cooking verbs: %d" % len(DATA["cooking_verbs"]))
    assert len(DATA["cooking_verbs"]) == 5
    assert all(v.startswith("me") for v in DATA["cooking_verbs"])
    print("OK: %s set the table" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_overview,
    "writing": demo_writing,
    "pronunciation": demo_pronunciation,
    "nouns": demo_nouns,
    "verbs": demo_verbs,
    "adjectives": demo_adjectives,
    "pronouns": demo_pronouns,
    "numbers": demo_numbers,
    "greetings": demo_greetings,
    "grammar": demo_grammar,
    "home": demo_home,
    "food": demo_food,
}


# ---------------------------------------------------------------- 13: travel

def demo_travel(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("compass words: %d" % len(DATA["compass"]))
    assert len(DATA["compass"]) == 7
    for must in ("kanan", "kiri", "lurus"):
        assert must in DATA["compass"]
    print("transport modes: %d" % len(DATA["transport"]))
    assert len(DATA["transport"]) == 6
    assert "ojek" in DATA["transport"]
    print("scripts: %s" % ", ".join(DATA["scripts"]))
    assert len(DATA["scripts"]) == 3
    print("OK: %s hit the road" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 14: work

def demo_work(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("workplaces: %d" % len(DATA["workplaces"]))
    assert len(DATA["workplaces"]) == 5
    print("office passives: %s" % ", ".join(DATA["passives"]))
    assert DATA["passives"] == ["dibayar", "diadakan"]
    for pv in DATA["passives"]:
        assert pv.startswith("di"), "passive must wear di-"
    assert DATA["doer_prefix"] == "pe-"
    print("OK: %s clocked in" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 15: health

def demo_health(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("body parts: %d" % len(DATA["body_parts"]))
    assert len(DATA["body_parts"]) == 7
    print("symptoms: %d" % len(DATA["symptoms"]))
    assert len(DATA["symptoms"]) == 5
    print("emergency words: %s" % ", ".join(DATA["emergency"]))
    assert len(DATA["emergency"]) == 4
    assert "ambulans" in DATA["emergency"]
    # the pain-reporting frame works for every listed body part
    frames = ["%s saya sakit" % b for b in DATA["body_parts"]]
    print("pain frames generated: %d" % len(frames))
    assert len(frames) == 7 and frames[0] == "kepala saya sakit"
    print("OK: %s ran the clinic" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 16: emotions

def demo_emotions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("emotions: %d" % len(DATA["emotions"]))
    assert len(DATA["emotions"]) == 11
    for must in ("bahagia", "sedih", "marah", "takut", "cinta"):
        assert must in DATA["emotions"]
    print("hati compounds: %s" % ", ".join(DATA["hati_compounds"]))
    assert len(DATA["hati_compounds"]) == 2
    assert DATA["reciprocal"] == "saling-"
    print("OK: %s felt everything" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 17: nature

def demo_nature(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("seasons: %s" % " / ".join(DATA["seasons"]))
    assert DATA["seasons"] == ["musim hujan", "musim kemarau"]
    print("animals: %d" % len(DATA["animals"]))
    assert len(DATA["animals"]) == 6
    assert "orangutan" in DATA["animals"]
    print("plants: %d" % len(DATA["plants"]))
    assert len(DATA["plants"]) == 3
    print("OK: %s walked the archipelago" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 18: shopping

def demo_shopping(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    script = DATA["bargain_script"]
    print("bargain beats: %d" % len(script))
    assert len(script) == 5
    assert script[0] == "Berapa harga" and script[-1] == "saya beli"
    assert DATA["currency"] == "rupiah" and DATA["thousand"] == "ribu"
    print("payment ways: %s" % ", ".join(DATA["payment"]))
    assert len(DATA["payment"]) == 3
    # change arithmetic: pay 50000 for 44000 -> 6000 back
    change = 50000 - 44000
    print("change on 50000 for 44000: %d" % change)
    assert change == 6000
    print("OK: %s closed the deal" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 19: friendship

def demo_friendship(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("social arc: %s" % " -> ".join(DATA["arc"]))
    assert len(DATA["arc"]) == 5
    print("ceremonial formulas: %d" % len(DATA["ceremonial"]))
    assert len(DATA["ceremonial"]) == 2
    assert "Turut berduka cita" in DATA["ceremonial"]
    print("mutual forms: %s" % ", ".join(DATA["mutual"]))
    assert len(DATA["mutual"]) == 2
    print("OK: %s kept the friendship" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 20: technology

def demo_technology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    print("native coinages: %d" % len(DATA["native_coinages"]))
    assert len(DATA["native_coinages"]) == 5
    for must in ("mengunduh", "tetikus", "surel", "daring"):
        assert must in DATA["native_coinages"]
    print("loanwords: %d" % len(DATA["loans"]))
    assert len(DATA["loans"]) == 4
    print("devices: %s" % ", ".join(DATA["devices"]))
    assert len(DATA["devices"]) == 3
    print("OK: %s booted up" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 21: tenses

def demo_tenses(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    t = DATA["tenses"]
    total = sum(t.values())
    print("tense sentences: %d" % total)
    assert total == 25
    for tense, n in t.items():
        assert n == 5, "%s must have 5 sentences" % tense
    m = DATA["markers"]
    assert m["present"] is None
    assert m["past"] == ["sudah", "telah"]
    assert m["progressive"] == ["sedang"]
    assert m["future"] == ["akan", "mau"]
    assert m["passive"] == ["di-"]
    print("parallel verb across tenses: %s" % DATA["parallel_verb"])
    assert DATA["parallel_verb"] == "makan"
    # the passive frame: di- + root
    passive = "di" + "baca"
    print("passive build: %s" % passive)
    assert passive == "dibaca"
    print("OK: %s bent time" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 22: qa

def demo_qa(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("Q&A pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 20
    print("question words: %d" % len(DATA["question_words"]))
    assert len(DATA["question_words"]) == 8
    for must in ("siapa", "mengapa", "berapa"):
        assert must in DATA["question_words"]
    print("yes-no markers: %s" % ", ".join(DATA["yes_no"]))
    assert DATA["yes_no"] == ["apakah", "bisakah"]
    assert DATA["full_sentence_answers"] is True
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 23: commands

def demo_commands(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    tiers = DATA["tiers"]
    print("formal markers: %s" % ", ".join(tiers["formal"]))
    assert len(tiers["formal"]) == 3
    print("everyday markers: %s" % ", ".join(tiers["everyday"]))
    assert len(tiers["everyday"]) == 3
    print("prohibition markers: %s" % ", ".join(tiers["prohibition"]))
    assert len(tiers["prohibition"]) == 2
    assert DATA["softener"] == "-lah"
    # tier sentence budget: 5 formal + 10 everyday + 5 prohibition
    budget = 5 + 10 + 5
    print("tier budget: %d" % budget)
    assert budget == DATA["sentences"] == 20
    print("OK: %s gave the orders" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 24: descriptions

def demo_descriptions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 20
    parts = DATA["people"] + DATA["places"] + DATA["things"]
    print("people %d + places %d + things %d = %d"
          % (DATA["people"], DATA["places"], DATA["things"], parts))
    assert parts == DATA["sentences"] == 20
    print("yang-clauses: %d" % DATA["yang_clauses"])
    assert DATA["yang_clauses"] == 5
    print("ber- possession forms: %d" % len(DATA["ber_forms"]))
    assert len(DATA["ber_forms"]) == 4
    assert "berkacamata" in DATA["ber_forms"]
    print("OK: %s painted the portraits" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS.update({
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
})


# ---------------------------------------------------------------- 25: story I

def demo_story1(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 10
    assert DATA["tense"] == "present-habitual"
    print("dayparts in arc: %s" % ", ".join(DATA["dayparts"]))
    assert DATA["dayparts"] == ["pagi", "siang", "sore", "malam"]
    assert DATA["new_words"] == 0, "story must reuse known words only"
    print("OK: %s told the day" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 26: story II

def demo_story2(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 10
    assert DATA["tense"] == "past"
    print("past markers: %s" % ", ".join(DATA["markers"]))
    assert len(DATA["markers"]) == 4
    assert "sudah" in DATA["markers"] and "telah" in DATA["markers"]
    print("cultural words: %s" % ", ".join(DATA["cultural_words"]))
    assert DATA["cultural_words"] == ["oleh-oleh"]
    print("OK: %s remembered the trip" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 27: story III

def demo_story3(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 10
    assert DATA["tense"] == "future-conditional"
    print("future markers: %s" % ", ".join(DATA["markers"]))
    assert len(DATA["markers"]) == 4
    assert "akan" in DATA["markers"] and "mau" in DATA["markers"]
    print("conditional branches: %d" % DATA["conditionals"])
    assert DATA["conditionals"] == 2
    print("OK: %s dreamed forward" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 28: idioms

def demo_idioms(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("sayings: %d" % DATA["sayings"])
    assert DATA["sayings"] == 20
    print("layers per saying: %d" % len(DATA["layers"]))
    assert DATA["layers"] == ["literal", "meaning", "example"]
    print("nature images: %d" % len(DATA["nature_images"]))
    assert len(DATA["nature_images"]) == 8
    for must in ("pinang", "harimau", "nasi"):
        assert must in DATA["nature_images"]
    print("OK: %s quoted the elders" % NAME)
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
    assert len(DATA["formal_markers"]) == 4
    assert "Dengan hormat" in DATA["formal_markers"]
    print("colloquial markers: %s" % ", ".join(DATA["colloquial_markers"]))
    assert DATA["colloquial_markers"] == ["gue", "lo", "nggak"]
    print("pronoun shifts: %s" % ", ".join(DATA["pronoun_shift"]))
    assert len(DATA["pronoun_shift"]) == 2
    print("OK: %s dressed for the occasion" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 30: complex sentences

def demo_complex(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("complex sentences: %d" % DATA["sentences"])
    assert DATA["sentences"] == 15
    print("connectors: %d" % len(DATA["connectors"]))
    assert len(DATA["connectors"]) == 14
    for must in ("karena", "walaupun", "sehingga", "yang", "semakin"):
        assert must in DATA["connectors"], "%s missing" % must
    print("relative patterns: %d" % DATA["relative_patterns"])
    assert DATA["relative_patterns"] == 2
    print("OK: %s joined the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 31: market conversation

def demo_convo_market(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    print("speakers: %s" % " / ".join(DATA["speakers"]))
    assert DATA["speakers"] == ["Penjual", "Pembeli"]
    print("transaction beats: %d" % len(DATA["beats"]))
    assert len(DATA["beats"]) == 12
    assert DATA["beats"][0] == "greet" and DATA["beats"][-1] == "part"
    print("address forms: %s" % ", ".join(DATA["address"]))
    assert DATA["address"] == ["Pak", "Bu"]
    print("OK: %s bargained at the market" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 32: friend conversation

def demo_convo_friend(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    print("speakers: %s" % " / ".join(DATA["speakers"]))
    assert DATA["speakers"] == ["Rina", "Dimas"]
    print("particles: %s" % ", ".join(DATA["particles"]))
    assert DATA["particles"] == ["nih", "dong", "ya"]
    print("dialogue moves: %d" % len(DATA["moves"]))
    assert len(DATA["moves"]) == 5
    print("OK: %s reunited the friends" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 33: problem conversation

def demo_convo_problem(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    print("speakers: %s" % " / ".join(DATA["speakers"]))
    assert DATA["speakers"] == ["Penghuni", "Pengelola"]
    print("template steps: %d" % len(DATA["template"]))
    assert len(DATA["template"]) == 8
    assert DATA["template"][0] == "open" and DATA["template"][-1] == "close"
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
    assert DATA["core_words"] == 200
    print("word groups: %d" % DATA["groups"])
    assert DATA["groups"] == 12
    print("grammar lines: %d" % DATA["grammar_lines"])
    assert DATA["grammar_lines"] == 10
    print("phrase tables: %d" % DATA["phrase_tables"])
    assert DATA["phrase_tables"] == 7
    print("records referenced: %d" % DATA["records_referenced"])
    assert DATA["records_referenced"] == 33
    print("OK: %s sealed the charter" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS.update({
    "story1": demo_story1,
    "story2": demo_story2,
    "story3": demo_story3,
    "idioms": demo_idioms,
    "registers": demo_registers,
    "complex": demo_complex,
    "convo_market": demo_convo_market,
    "convo_friend": demo_convo_friend,
    "convo_problem": demo_convo_problem,
    "mastery": demo_mastery,
})
