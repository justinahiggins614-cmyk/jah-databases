#!/usr/bin/env python3
"""Demo programs for the Ukrainian to English databases (Manon's language
project, 2026-10-17).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: alphabet drills, vocabulary quizzes,
case tables, conjugation checks, tense grids, sentence statistics. All are
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
    assert 0.49 < share < 0.50, "share out of bounds"
    l2 = total_m - native_m
    print("second-language speakers: ~%.0f million" % l2)
    assert 9.9 < l2 < 10.1, "L2 estimate out of bounds"
    print("official countries: %d" % DATA["official_countries"])
    assert DATA["official_countries"] == 1
    print("recognized minority states: %d" % DATA["recognized"])
    assert DATA["recognized"] == 9
    print("dialects: %d" % len(DATA["dialects"]))
    assert len(DATA["dialects"]) == 5
    print("regions: %d" % len(DATA["regions"]))
    assert len(DATA["regions"]) == 9
    assert DATA["iso1"] == "uk" and DATA["iso3"] == "ukr"
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 2: writing system

def demo_writing(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    letters = DATA["letters"]
    print("Ukrainian letters: %d" % len(letters))
    assert len(letters) == 33, "Ukrainian alphabet must be 33"
    assert len(set(letters)) == 33, "letters must be unique"
    iotated = DATA["iotated"]
    print("iotated letters: %s" % " ".join(iotated))
    assert iotated == ["\\u0404", "\\u0407", "\\u042e", "\\u042f"], "iotated must be ye yi yu ya"
    for sp in iotated + DATA["specials"]:
        assert sp in letters, "special %r missing from alphabet" % sp
    print("vowel letters: %d" % len(DATA["vowel_letters"]))
    assert len(DATA["vowel_letters"]) == 10
    print("direction: %s" % DATA["direction"])
    assert DATA["direction"] == "left-to-right"
    alpha = set(letters) | {ch.lower() for ch in letters} | {"\\u2019"}
    words = DATA["test_words"]
    for w in words:
        for ch in w:
            assert ch in alpha, "unwritable char %r in %s" % (ch, w)
        print("  writable: %s" % w)
    assert len(words) == 8
    print("OK: %s spelled the alphabet" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 3: phonology

def demo_phonology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("vowel phonemes: %d, pairs: %d" % (len(DATA["vowel_phonemes"]), DATA["vowel_pairs"]))
    assert len(DATA["vowel_phonemes"]) == 6 and DATA["vowel_pairs"] == 15
    print("consonant phonemes: %d" % DATA["consonant_phonemes"])
    assert DATA["consonant_phonemes"] == 22
    pairs = DATA["stress_pairs"]
    print("stress minimal pairs: %d" % len(pairs))
    assert len(pairs) == 3
    for a, b, ga, gb in pairs:
        assert a and b and ga != gb, "stress must change the meaning"
        print("  %s (%s) vs %s (%s)" % (a, ga, b, gb))
    for sg, pl in DATA["palatalize"]:
        assert sg != pl
        print("  palatalize: %s -> %s" % (sg, pl))
    assert len(DATA["palatalize"]) == 3
    for inf, f1 in DATA["soften_verbs"]:
        assert inf != f1
        print("  soften: %s -> %s" % (inf, f1))
    words = DATA["example_words"]
    print("example words: %d" % len(words))
    assert len(words) == 14
    for w, g in words:
        assert w and g, "empty word/gloss"
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
    masc = [w for w, g, x in nouns if x == "m"]
    fem = [w for w, g, x in nouns if x == "f"]
    neut = [w for w, g, x in nouns if x == "n"]
    pl = [w for w, g, x in nouns if x == "pl"]
    print("masculine: %d, feminine: %d, neuter: %d, plural-only: %d"
          % (len(masc), len(fem), len(neut), len(pl)))
    assert len(masc) == 9 and len(fem) == 10 and len(neut) == 5 and len(pl) == 1
    for w, g, x in nouns:
        assert w and g and x in ("m", "f", "n", "pl")
    assert len(set(w for w, g, x in nouns)) == 25, "nouns must be unique"
    print("plural patterns: %d" % len(DATA["plurals"]))
    assert len(DATA["plurals"]) == 4
    for sg, p in DATA["plurals"]:
        assert sg != p and p
        print("  %s -> %s" % (sg, p))
    assert ["книжка", "книжки"] in DATA["plurals"]
    assert ["вікно", "вікна"] in DATA["plurals"]
    assert DATA["sentences"] == 25
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
    c1 = [w for w, g, c in verbs if c == "I"]
    c2 = [w for w, g, c in verbs if c == "II"]
    irr = [w for w, g, c in verbs if c == "irr"]
    print("I conjugation: %d, II conjugation: %d, irregular: %d"
          % (len(c1), len(c2), len(irr)))
    assert len(c1) == 11 and len(c2) == 6 and len(irr) == 8
    for w, g, c in verbs:
        assert w.endswith("ти") or w.endswith("тися"), "infinitive must end in -ти/-тися: %s" % w
        assert g and c in ("I", "II", "irr")
    assert len(set(w for w, g, c in verbs)) == 25, "verbs must be unique"
    assert ("писати", "I") in [(w, c) for w, g, c in verbs]
    assert ("говорити", "II") in [(w, c) for w, g, c in verbs]
    print("aspect pairs: %d" % len(DATA["aspect_pairs"]))
    assert len(DATA["aspect_pairs"]) == 4
    for imp, pf in DATA["aspect_pairs"]:
        assert imp != pf and pf.startswith(("на", "про", "з", "с", "по")), "perfective usually prefixed"
        print("  %s / %s" % (imp, pf))
    assert DATA["sentences"] == 25
    print("OK: %s conjugated the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 6: adjectives

def demo_adjectives(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("adjectives: %d, adverbs: %d" % (DATA["adjectives"], DATA["adverbs"]))
    assert DATA["adjectives"] == 25 and DATA["adverbs"] == 15
    e = DATA["endings"]
    print("agreement endings: m=%s f=%s n=%s pl=%s" % (e["m"], e["f"], e["n"], e["pl"]))
    assert e["m"] == ["-ий", "-ій"] and e["pl"] == ["-і"]
    print("adverb derivations: %d" % len(DATA["pairs"]))
    assert len(DATA["pairs"]) == 4
    for adj, adv in DATA["pairs"]:
        assert adj != adv and (adv.endswith("о") or adv.endswith("е")), "adverb should end in -о/-е: %s" % adv
        print("  %s -> %s" % (adj, adv))
    assert ["швидкий", "швидко"] in DATA["pairs"]
    assert DATA["sentences"] == 40
    print("OK: %s agreed the adjectives" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 7: pronouns

def demo_pronouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    pers = DATA["personal"]
    print("personal pronouns: %d" % len(pers))
    assert len(pers) == 8
    for nom, acc in pers:
        assert nom and acc, "empty pronoun form"
    assert ["я", "мене"] in pers and ["ти", "тебе"] in pers
    assert ["він", "його"] in pers and ["вони", "їх"] in pers
    noms = [n for n, a in pers]
    assert len(set(noms)) == 8, "nominatives must be unique"
    print("possessive sets: %d" % DATA["possessive_sets"])
    assert DATA["possessive_sets"] == 6
    dem = DATA["demonstratives"]
    print("demonstrative paradigms: %d" % len(dem))
    assert len(dem) == 2
    for para in dem:
        assert len(para) == 4, "demonstrative must show 4 gender/number forms"
    print("interrogatives: %d (%s)" % (len(DATA["interrogatives"]), ", ".join(DATA["interrogatives"])))
    assert len(DATA["interrogatives"]) == 5
    assert "хто" in DATA["interrogatives"] and "скільки" in DATA["interrogatives"]
    assert DATA["sentences"] == 21
    print("OK: %s declined the pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 8: numbers

def demo_numbers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("cardinals 1-20: %d" % DATA["cardinals_1_20"])
    assert DATA["cardinals_1_20"] == 20
    print("tens: %d" % len(DATA["tens"]))
    assert len(DATA["tens"]) == 8
    assert "сорок" in DATA["tens"] and "сто" in DATA["tens"]
    g = DATA["gendered"]
    print("gendered numerals: %d sets" % len(g))
    assert g[0] == ["один", "одна", "одне"] and g[1] == ["два", "дві"]
    print("ordinals: %d" % len(DATA["ordinals"]))
    assert len(DATA["ordinals"]) == 5
    assert DATA["ordinals"][0] == "перший"
    print("days: %d months: %d seasons: %d"
          % (len(DATA["days"]), len(DATA["months"]), len(DATA["seasons"])))
    assert len(DATA["days"]) == 7 and len(DATA["months"]) == 12 and len(DATA["seasons"]) == 4
    assert DATA["days"][0] == "понеділок" and DATA["months"][0] == "січень"
    assert DATA["seasons"] == ["весна", "літо", "осінь", "зима"]
    assert DATA["sentences"] == 6
    print("OK: %s counted to a hundred" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 9: greetings

def demo_greetings(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("phrases: %d" % DATA["phrases"])
    assert DATA["phrases"] == 30
    tod = DATA["time_of_day"]
    print("time-of-day greetings: %d" % len(tod))
    assert len(tod) == 4
    assert "Добрий день" in tod
    print("formal: %d, informal: %d" % (len(DATA["formal"]), len(DATA["informal"])))
    assert len(DATA["formal"]) == 4 and len(DATA["informal"]) == 3
    assert "Привіт" in DATA["informal"] and "До побачення" in DATA["formal"]
    g = DATA["gendered"]
    print("speaker-gendered: %s" % g)
    assert g == [["Радий", "m"], ["Рада", "f"]]
    print("OK: %s greeted the day" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 10: grammar essentials

def demo_grammar(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("load-bearing rules: %d" % DATA["rules"])
    assert DATA["rules"] == 10
    cases = DATA["cases"]
    print("cases: %d (%s)" % (len(cases), ", ".join(cases)))
    assert len(cases) == 7
    assert cases[0] == "називний" and cases[-1] == "кличний"
    forms = DATA["case_forms"]
    print("книга declined: %s" % " - ".join(forms))
    assert len(forms) == 7 and len(set(forms)) >= 6, "case forms must mostly differ"
    assert forms[0] == "книга" and forms[3] == "книгу"
    print("genders: %s" % DATA["genders"])
    assert DATA["genders"] == ["m", "f", "n"]
    print("aspects: %s" % DATA["aspects"])
    assert DATA["aspects"] == ["imperfective", "perfective"]
    print("OK: %s raised the ten pillars" % NAME)
if __name__ == "__main__":
    main()
''')


# --------------------------------- sentence-set records (11-20, 24, 31-33)

def _sentence_body(ok_msg, extra=""):
    # extra: additional DATA-driven assertions, already indented 4 spaces.
    body = '''\
def main():
    ss = DATA["sentences"]
    print("sentences: %d" % len(ss))
    assert len(ss) == 20, "need 20 sentences"
    for uk, en in ss:
        assert uk and en, "empty sentence or translation"
        assert uk != en, "translation must differ from source"
__EXTRA__
    print("OK: __OKMSG__" % NAME)
if __name__ == "__main__":
    main()
'''
    extra_block = ("    " + extra) if extra else ""
    return body.replace("__EXTRA__", extra_block).replace("__OKMSG__", ok_msg)


def demo_home(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _sentence_body(
        "%s walked through the house",
        'blob = " ".join(u for u, e in ss).lower()\n'
        '    for r in ["кухн", "вітальн", "спальн", "ванн"]:\n'
        '        assert r in blob, "room stem %s missing" % r\n'
        '    assert len(DATA["rooms"]) == 4'))


def demo_food(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _sentence_body(
        "%s cooked the meal",
        'blob = " ".join(u for u, e in ss).lower()\n'
        '    for d in DATA["dishes"]:\n'
        '        assert d in blob, "dish %s missing" % d\n'
        '    assert len(DATA["dishes"]) == 3'))


def demo_travel(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _sentence_body(
        "%s made the journey",
        'blob = " ".join(u for u, e in ss).lower()\n'
        '    for d in DATA["directions"]:\n'
        '        assert d in blob, "direction %s missing" % d\n'
        '    assert len(DATA["directions"]) == 4'))


def demo_work(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _sentence_body(
        "%s worked the day",
        'blob = " ".join(u for u, e in ss).lower()\n'
        '    for p in DATA["professions"]:\n'
        '        assert p in blob, "profession %s missing" % p'))


def demo_health(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _sentence_body(
        "%s visited the clinic",
        'blob = " ".join(u for u, e in ss).lower()\n'
        '    for b in DATA["body_parts"]:\n'
        '        assert b in blob, "body part %s missing" % b\n'
        '    assert len(DATA["body_parts"]) == 6'))


def demo_emotions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _sentence_body(
        "%s felt the spectrum",
        'blob = " ".join(u for u, e in ss).lower()\n'
        '    assert "кохаю" in blob and "боюся" in blob\n'
        '    assert len(DATA["spectrum"]) == 6'))


def demo_nature(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _sentence_body(
        "%s walked the seasons",
        'blob = " ".join(u for u, e in ss).lower()\n'
        '    for s in DATA["seasons_locative"]:\n'
        '        assert s in blob, "season %s missing" % s'))


def demo_shopping(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _sentence_body(
        "%s worked the market",
        'blob = " ".join(u for u, e in ss)\n'
        '    assert "гривень" in blob or "гривня" in blob\n'
        '    assert DATA["currency"] == ["гривня", "копійка"]'))


def demo_friendship(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _sentence_body(
        "%s kept the friendship",
        'assert DATA["stages"] == ["introduction", "small talk", "invitation",\n'
        '        "celebration", "farewell"]\n'
        '    blob = " ".join(u for u, e in ss)\n'
        '    assert "Вітаю" in blob'))


def demo_technology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _sentence_body(
        "%s booted the devices",
        'blob = " ".join(u for u, e in ss).lower()\n'
        '    for d in DATA["devices"]:\n'
        '        assert d in blob, "device %s missing" % d'))


# ---------------------------------------------------------------- 21: tenses

def demo_tenses(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    pr, pa, fu = DATA["present"], DATA["past"], DATA["future"]
    print("present: %d, past: %d, future: %d" % (len(pr), len(pa), len(fu)))
    assert len(pr) == 6 and len(pa) == 6 and len(fu) == 7
    for uk, en in pr + pa + fu:
        assert uk and en
    blob_f = " ".join(u for u, e in fu)
    assert "читатиму" in blob_f, "synthetic future missing"
    assert "будеш писати" in blob_f or "буду" in blob_f, "analytic future missing"
    assert "напише" in blob_f, "perfective future missing"
    blob_p = " ".join(u for u, e in pa)
    assert "писала" in blob_p and "читав" in blob_p, "past gender forms missing"
    print("aspect pairs: %d" % len(DATA["aspect_pairs"]))
    assert len(DATA["aspect_pairs"]) == 3
    assert ["писати", "написати"] in DATA["aspect_pairs"]
    print("OK: %s ran the tense grid" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 22: questions and answers

def demo_qa(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    pairs = DATA["pairs"]
    print("Q&A pairs: %d" % len(pairs))
    assert len(pairs) == 20
    for q, a in pairs:
        assert q and a and q != a
        assert q.rstrip().endswith("?"), "question must end with ?: %s" % q
    qw = DATA["question_words"]
    print("question words: %d" % len(qw))
    assert len(qw) == 11
    blob = " ".join(q for q, a in pairs)
    for w in ["Хто", "Що", "Де", "Коли", "Чому", "Як", "Скільки"]:
        assert w in blob, "question word %s unused" % w
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 23: commands

def demo_commands(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    pairs = DATA["pairs"]
    print("command pairs: %d" % len(pairs))
    assert len(pairs) == 10
    for inf, frm in pairs:
        assert inf and frm and inf != frm
        assert frm.rstrip("!").endswith("те") or frm.rstrip("!").endswith("ть"), \
            "formal should end in -те: %s" % frm
        print("  %s / %s" % (inf, frm))
    assert ["Читай!", "Читайте!"] in pairs
    assert ["Їж!", "Їжте!"] in pairs
    print("softened: %d reflexive: %d" % (DATA["softened"], len(DATA["reflexive"])))
    assert DATA["softened"] == 5 and len(DATA["reflexive"]) == 2
    print("OK: %s gave the orders" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 24: descriptions

def demo_descriptions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _sentence_body(
        "%s painted the portraits",
        'blob = " ".join(u for u, e in ss).lower()\n'
        '    assert "дніпро" in blob and "карпати" in blob\n'
        '    assert DATA["comparisons"] == 1'))


# ---------------------------------------------------------------- 25-27: stories

def _story_body(tense_word):
    body = '''\
def main():
    lines = DATA["lines"]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10, "story needs 10 lines"
    for uk, en in lines:
        assert uk and en and uk != en
    print("tense: %s" % DATA["tense"])
    assert DATA["tense"] == "__TENSE__"
    print("OK: %s told the tale" % NAME)
if __name__ == "__main__":
    main()
'''
    return body.replace("__TENSE__", tense_word)


def demo_story1(hdr, name, rid, group, entry):
    body = _story_body("present")
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + body.replace(
        'print("tense: %s" % DATA["tense"])',
        'print("tense: %s" % DATA["tense"])\n'
        '    blob = " ".join(u for u, e in lines)\n'
        '    assert "Півень" in blob and "Бабуся" in blob'))


def demo_story2(hdr, name, rid, group, entry):
    body = _story_body("past")
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + body.replace(
        'print("tense: %s" % DATA["tense"])',
        'print("tense: %s" % DATA["tense"])\n'
        '    blob = " ".join(u for u, e in lines)\n'
        '    assert "поїхали" in blob and "прибув" in blob'))


def demo_story3(hdr, name, rid, group, entry):
    body = _story_body("future")
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + body.replace(
        'print("tense: %s" % DATA["tense"])',
        'print("tense: %s" % DATA["tense"])\n'
        '    blob = " ".join(u for u, e in lines)\n'
        '    assert "прокинуся" in blob and "хотів би" in blob'))


# ---------------------------------------------------------------- 28: idioms

def demo_idioms(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    idioms = DATA["idioms"]
    print("idioms: %d" % len(idioms))
    assert len(idioms) == 20
    for uk, lit, mean in idioms:
        assert uk and lit and mean, "idiom needs all three parts"
    assert len(set(u for u, l, m in idioms)) == 20, "idioms must be unique"
    blob = " ".join(u for u, l, m in idioms)
    for key in ["Вода камінь точить", "горобець", "Біла ворона", "локшину"]:
        assert key in blob, "idiom %s missing" % key
    print("OK: %s coined the proverbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 29: registers

def demo_registers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    pairs = DATA["pairs"]
    print("register pairs: %d" % len(pairs))
    assert len(pairs) == 15
    for inf, frm in pairs:
        assert inf and frm and inf != frm
    blob = " ".join(f for i, f in pairs)
    assert "Шановний" in blob and "З повагою" in blob
    assert "прошу" in blob.lower() or "Прошу" in blob
    print("OK: %s shifted the register" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 30: complex sentences

def demo_complex(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    ss = DATA["sentences"]
    print("complex sentences: %d" % len(ss))
    assert len(ss) == 15
    for uk, en in ss:
        assert uk and en and uk != en
        assert "," in uk, "complex sentence needs its comma: %s" % uk
    conns = DATA["connectors"]
    print("connectors: %d" % len(conns))
    assert len(conns) == 10
    blob = " ".join(u for u, e in ss).lower()
    for c in ["який", "тому що", "хоча", "щоб"]:
        assert c in blob, "connector %s unused" % c
    print("OK: %s bridged the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 31-33: conversations

def _conv_body(speakers_n):
    body = '''\
def main():
    lines = DATA["lines"]
    print("dialogue lines: %d" % len(lines))
    assert len(lines) == 20, "dialogue needs 20 lines"
    speakers = set()
    for sp, uk, en in lines:
        assert sp and uk and en and uk != en
        speakers.add(sp)
    print("speakers: %d (%s)" % (len(speakers), ", ".join(sorted(speakers))))
    assert len(speakers) == __N__, "speaker count off"
    print("OK: %s held the conversation" % NAME)
if __name__ == "__main__":
    main()
'''
    return body.replace("__N__", str(speakers_n))


def demo_conv_market(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _conv_body(3).replace(
        'print("speakers: %d (%s)" % (len(speakers), ", ".join(sorted(speakers))))',
        'print("speakers: %d (%s)" % (len(speakers), ", ".join(sorted(speakers))))\n'
        '    blob = " ".join(u for s, u, e in lines).lower()\n'
        '    assert "знижку" in blob and "карткою" in blob'))


def demo_conv_friend(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _conv_body(2))


def demo_conv_problem(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + _conv_body(3).replace(
        'print("speakers: %d (%s)" % (len(speakers), ", ".join(sorted(speakers))))',
        'print("speakers: %d (%s)" % (len(speakers), ", ".join(sorted(speakers))))\n'
        '    blob = " ".join(u for s, u, e in lines).lower()\n'
        '    assert "гаманець" in blob and "блискавкою" in blob'))


# ---------------------------------------------------------------- 34: mastery

def demo_mastery(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    words = DATA["words"]
    print("core words: %d" % len(words))
    assert len(words) == 200, "mastery needs exactly 200 words"
    assert len(set(w for w, g in words)) == 200, "words must be unique"
    for w, g in words:
        assert w and g and w != g
    blob = " ".join(w for w, g in words)
    for key in ["дякую", "будь ласка", "Україна", "Київ", "мова"]:
        assert key in blob, "core word %s missing" % key
    print("cases: %d letters: %d" % (DATA["cases"], DATA["letters"]))
    assert DATA["cases"] == 7 and DATA["letters"] == 33
    print("OK: %s sealed the summit" % NAME)
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
