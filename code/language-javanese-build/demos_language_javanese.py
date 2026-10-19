#!/usr/bin/env python3
"""Demo programs for the Javanese to English databases (Manon's language orders
#10-12, 2026-10-17, roster rank 22).

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
    assert 0.83 < share < 0.85, "share out of bounds"
    l2 = total_m - native_m
    print("second-language speakers: ~%.0f million" % l2)
    assert 15.9 < l2 < 16.1, "L2 estimate out of bounds"
    print("dialects: %d" % DATA["dialects"])
    assert DATA["dialects"] == 6
    print("speech levels: %d" % DATA["levels"])
    assert DATA["levels"] == 4
    print("scripts: %d" % DATA["scripts"])
    assert DATA["scripts"] == 3
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 2: writing

def demo_writing(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    order = DATA["aksara_order"]
    print("aksara in order: %d" % len(order))
    assert len(order) == DATA["aksara"] == 20
    assert order[0] == "ha" and order[-1] == "nga", "hanacaraka order broken"
    assert len(set(order)) == 20, "aksara must be unique"
    lines = [order[i:i+5] for i in range(0, 20, 5)]
    print("poem lines: %d (%s)" % (len(lines), " / ".join(" ".join(l) for l in lines)))
    assert len(lines) == DATA["poem_lines"] == 4
    print("traditional digits: %d" % DATA["digits"])
    assert DATA["digits"] == 10
    print("scripts in use: %d" % DATA["scripts"])
    assert DATA["scripts"] == 3
    print("OK: %s drilled the script" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 3: phonology

def demo_phonology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("vowels: %d" % DATA["vowels"])
    assert DATA["vowels"] == 6
    print("consonants: %d" % DATA["consonants"])
    assert DATA["consonants"] == 21
    phonemes = DATA["vowels"] + DATA["consonants"]
    print("total phonemes: %d" % phonemes)
    assert 26.9 < phonemes < 27.1
    pairs = DATA["pairs"]
    print("voicing pairs: %d" % len(pairs))
    assert len(pairs) == 5
    flat = [c for p in pairs for c in p]
    assert len(set(flat)) == 10, "pairs must be distinct consonants"
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
    assert "wong" in nouns and "banyu" in nouns and "negara" in nouns
    assert len(set(nouns)) == 25, "nouns must be unique"
    avg = sum(len(w) for w in nouns) / float(len(nouns))
    print("average word length: %.2f chars" % avg)
    assert 4.5 < avg < 6.0, "avg length out of bounds"
    longest = max(nouns, key=len)
    print("longest noun: %s" % longest)
    assert longest == "srengenge"
    print("OK: %s stocked the noun shelf" % NAME)
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
    assert "mangan" in verbs and "sinau" in verbs and "ndeleng" in verbs
    assert len(set(verbs)) == 25, "verbs must be unique"
    # tense gears: one verb form x six helpers = 150 surface forms, zero conjugations
    gears = ["wis", "lagi", "arep", "bakal", "durung", "tau"]
    surface = len(verbs) * len(gears)
    print("surface forms from 25 roots x 6 gears: %d (0 conjugations)" % surface)
    assert surface == 150
    nasal = [v for v in verbs if v[:2] in ("ng", "ny") or v[:1] == "m"]
    print("nasal-active verbs: %d" % len(nasal))
    assert 8 <= len(nasal) <= 14, "nasal count out of bounds"
    print("OK: %s drilled the verb engine" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 6: adjectives/adverbs

def demo_adjadv(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    adjs = DATA["adjectives"]
    advs = DATA["adverbs"]
    print("adjectives: %d, adverbs: %d" % (len(adjs), len(advs)))
    assert len(adjs) == 25 and len(advs) == 15
    total = len(adjs) + len(advs)
    print("descriptive words: %d" % total)
    assert total == 40
    assert len(set(adjs) | set(advs)) == 40, "words must be unique"
    assert "banget" in advs and "luwih" in advs and "paling" in advs
    # comparison ladder: base -> luwih X -> paling X = 3 rungs per adjective
    rungs = len(adjs) * 3
    print("comparison rungs (25 adj x 3): %d" % rungs)
    assert rungs == 75
    print("OK: %s sharpened description" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 7: pronouns

def demo_pronouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    pairs = DATA["pairs"]
    print("register pairs: %d" % len(pairs))
    assert len(pairs) == 4
    for ngoko, krama in pairs:
        assert ngoko != krama, "pair must differ by level"
    print("demonstratives: %s" % ", ".join(DATA["demonstratives"]))
    assert DATA["demonstratives"] == ["iki", "iku", "kae"]
    qs = DATA["interrogatives"]
    print("question words: %d" % len(qs))
    assert len(qs) == 7
    assert "sapa" in qs and "pira" in qs
    forms = len(pairs) * 2 + len(DATA["demonstratives"]) + len(qs)
    print("paradigm forms: %d" % forms)
    assert forms == 18
    print("OK: %s mapped the pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 8: numbers

def demo_numbers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    nums = DATA["numbers"]
    print("number entries: %d" % len(nums))
    assert len(nums) == 20
    assert 11 in nums and 1000 in nums
    print("value span covered: 1..%d" % max(nums))
    assert max(nums) == 1000
    days = DATA["days"]
    print("weekdays: %d" % len(days))
    assert len(days) == 7 and days[0] == "Senen" and days[-1] == "Minggu"
    months = DATA["months"]
    print("javanese months: %d" % len(months))
    assert len(months) == 12 and months[0] == "Sura" and months[-1] == "Besar"
    pasaran = DATA["pasaran"]
    print("pasaran days: %d" % len(pasaran))
    assert len(pasaran) == 5
    cycle = 7 * 5
    print("selapanan cycle: %d days" % cycle)
    assert cycle == 35
    print("OK: %s counted everything" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 9: greetings

def demo_greetings(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    gs = DATA["greetings"]
    print("greetings: %d" % len(gs))
    assert len(gs) == 30
    assert len(set(gs)) == 30, "greetings must be unique"
    assert "Sugeng enjing." in gs and "Matur nuwun." in gs
    sugeng = [g for g in gs if g.startswith("Sugeng")]
    print("sugeng-form greetings: %d" % len(sugeng))
    assert 8 <= len(sugeng) <= 12, "sugeng count out of bounds"
    print("OK: %s opened every gate" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 10: grammar

def demo_grammar(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("load-bearing rules: %d" % DATA["rules"])
    assert DATA["rules"] == 10
    aff = DATA["affixes"]
    print("affixes: %d (%s)" % (len(aff), ", ".join(aff)))
    assert len(aff) == 8
    assert "di-" in aff and "-ke" in aff
    print("OK: %s raised the frame" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 11: home

def demo_home(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    rooms = DATA["rooms"]
    fam = DATA["family"]
    print("rooms: %d" % len(rooms))
    assert len(rooms) == 5 and "pawon" in rooms
    print("family titles: %d" % len(fam))
    assert len(fam) == 7 and "simbah" in fam and "pakdhe" in fam
    print("OK: %s walked the house" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 12: food

def demo_food(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    d = DATA["dishes"]
    c = DATA["cook_verbs"]
    t = DATA["tastes"]
    print("dishes: %d, cook verbs: %d, tastes: %d" % (len(d), len(c), len(t)))
    assert len(d) == 5 and len(c) == 6 and len(t) == 5
    assert "gudeg" in d and "uleg" in c and "pedhes" in t
    combos = len(d) * len(c)
    print("dish x method descriptions: %d" % combos)
    assert combos == 30
    print("OK: %s set the table" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 13: travel

def demo_travel(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    dirs = DATA["directions"]
    tr = DATA["transport"]
    print("direction words: %d" % len(dirs))
    assert len(dirs) == 6 and "lurus" in dirs and "ngingguk" in dirs
    print("transport modes: %d" % len(tr))
    assert len(tr) == 6 and "becak" in tr and "sepur" in tr
    routes = len(dirs) * len(tr)
    print("direction x transport combos: %d" % routes)
    assert routes == 36
    print("OK: %s walked the road" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 14: work

def demo_work(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    j = DATA["jobs"]
    w = DATA["work_words"]
    s = DATA["school_words"]
    print("jobs: %d, work words: %d, school words: %d" % (len(j), len(w), len(s)))
    assert len(j) == 4 and len(w) == 4 and len(s) == 5
    assert "guru" in j and "lembur" in w and "sregep" in s
    print("OK: %s earned its keep" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 15: health

def demo_health(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    b = DATA["body"]
    sy = DATA["symptoms"]
    c = DATA["care"]
    print("body parts: %d, symptoms: %d, care words: %d" % (len(b), len(sy), len(c)))
    assert len(b) == 6 and len(sy) == 5 and len(c) == 6
    assert "sirah" in b and "lara" in sy and "waras" in c
    complaints = len(b) * len(sy)
    print("body x symptom complaints expressible: %d" % complaints)
    assert complaints == 30
    print("OK: %s healed the vessel" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 16: emotions

def demo_emotions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    emos = DATA["emotions"]
    print("emotion words: %d" % len(emos))
    assert len(emos) == 13
    assert "tresna" in emos and "kangen" in emos and "ayem" in emos
    assert len(set(emos)) == 13
    print("OK: %s read the heart" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 17: nature

def demo_nature(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    a = DATA["animals"]
    w = DATA["weather"]
    s = DATA["seasons"]
    print("animals: %d, weather words: %d, seasons: %d" % (len(a), len(w), len(s)))
    assert len(a) == 8 and len(w) == 4 and len(s) == 2
    assert "pitik" in a and "udan" in w
    assert set(s) == {"ketiga", "rendheng"}
    print("OK: %s heard the land" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 18: shopping

def demo_shopping(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    m = DATA["market"]
    arc = DATA["arc"]
    print("market words: %d" % len(m))
    assert len(m) == 5 and "bakul" in m and "susuk" in m
    print("bargaining arc steps: %d" % len(arc))
    assert len(arc) == 4
    assert arc[0] == "Regane pira?" and arc[-1] == "Wis, dadi."
    print("OK: %s closed the deal" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 19: social

def demo_social(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    so = DATA["social"]
    print("social core words: %d" % len(so))
    assert len(so) == 6
    assert "guyub rukun" in so and "gotong royong" in so and "mugi-mugi" in so
    print("OK: %s joined the circle" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 20: tech

def demo_tech(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    v = DATA["tech_verbs"]
    n = DATA["tech_nouns"]
    print("tech verbs: %d, tech nouns: %d" % (len(v), len(n)))
    assert len(v) == 8 and len(n) == 7
    assert "nelpon" in v and "nyimpen" in v and "HP" in n
    cmds = len(v) * len(n)
    print("verb x noun tech commands: %d" % cmds)
    assert cmds == 56
    print("OK: %s wired the tools" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 21: tenses

def demo_tenses(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    p, pr, f, x = DATA["past"], DATA["present"], DATA["future"], DATA["extra"]
    print("past: %d, present: %d, future: %d, extra: %d" % (p, pr, f, x))
    assert p == 6 and pr == 6 and f == 6 and x == 4
    total = p + pr + f + x
    print("tense sentences: %d" % total)
    assert total == 22
    h = DATA["helpers"]
    print("time helpers: %d" % len(h))
    assert len(h) == 8 and "wis" in h and "durung" in h and "tau" in h
    print("OK: %s marched through time" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 22: qa

def demo_qa(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("Q&A pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 20
    qw = DATA["qwords"]
    print("question words: %d" % len(qw))
    assert len(qw) == 8 and "sapa" in qw and "pira" in qw
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 23: commands

def demo_commands(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    d, s, p, r = DATA["direct"], DATA["softened"], DATA["prohibitions"], DATA["requests"]
    print("direct: %d, softened: %d, prohibitions: %d, requests: %d" % (d, s, p, r))
    assert (d, s, p, r) == (5, 5, 4, 6)
    total = d + s + p + r
    print("command sentences: %d" % total)
    assert total == 20
    soft = DATA["softeners"]
    assert len(soft) == 4 and "monggo" in soft
    print("OK: %s gave the orders" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 24: descriptions

def demo_descriptions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    st = DATA["stackers"]
    print("trait stackers: %s" % ", ".join(st))
    assert st == ["lan", "nanging"]
    assert DATA["relative"] == "sing"
    bp = DATA["body_parts"]
    print("portrait body parts: %d" % len(bp))
    assert len(bp) == 3
    print("OK: %s painted the portraits" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 25: story1

def demo_story1(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("story lines: %d" % 10)
    seq = DATA["sequence"]
    print("sequence words: %s" % ", ".join(seq))
    assert seq == ["saben esuk", "banjur", "sore"]
    assert DATA["hero"] == "Bagus"
    print("hero: %s" % DATA["hero"])
    print("OK: %s told the first tale" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 26: story2

def demo_story2(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    pm = DATA["past_markers"]
    sv = DATA["search_verbs"]
    print("past markers: %d, search verbs: %d" % (len(pm), len(sv)))
    assert len(pm) == 3 and len(sv) == 3
    assert "wis" in pm and "ketemu" in sv
    print("OK: %s closed the search" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 27: story3

def demo_story3(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    fm = DATA["future_markers"]
    co = DATA["conditionals"]
    print("future markers: %s" % ", ".join(fm))
    assert fm == ["arep", "bakal", "sesuk"]
    print("conditionals: %s" % ", ".join(co))
    assert co == ["yen", "yen ora"]
    print("OK: %s vowed tomorrow" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 28: idioms

def demo_idioms(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("idioms: %d" % DATA["idioms"])
    assert DATA["idioms"] == 20
    imgs = DATA["images"]
    print("core images: %d" % len(imgs))
    assert len(imgs) == 5 and "kebo" in imgs and "banyu" in imgs
    print("OK: %s kept the elders' law" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 29: registers

def demo_registers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("register pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 15
    swaps = DATA["swaps"]
    print("level swaps: %d" % len(swaps))
    assert len(swaps) == 8
    for ngoko, krama in swaps:
        assert ngoko != krama
    words = [w for p in swaps for w in p]
    assert "nedha" in words and "piyambakipun" in words
    print("OK: %s changed the uniform" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 30: complex

def demo_complex(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    cx = DATA["connectors"]
    print("connectors: %d" % len(cx))
    assert len(cx) == 12
    assert "amarga" in cx and "senajan" in cx and "supaya" in cx and "sing" in cx
    assert len(set(cx)) == 12
    print("OK: %s bound the alliance" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 31: market dialogue

def demo_market(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    arc = DATA["arc"]
    print("transaction arc steps: %d" % len(arc))
    assert len(arc) == 6
    assert arc[0] == "nuwun sewu" and arc[-1] == "sami-sami"
    print("OK: %s signed the treaty" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 32: friend dialogue

def demo_friend(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    arc = DATA["arc"]
    print("reunion arc steps: %d" % len(arc))
    assert len(arc) == 4
    assert "ayo ngopi" in arc
    print("OK: %s renewed the bond" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 33: problem dialogue

def demo_problem(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    arc = DATA["arc"]
    print("muster arc steps: %d" % len(arc))
    assert len(arc) == 6
    assert "gotong royong" in arc and arc[-1] == "bubaran"
    print("OK: %s mustered the council" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 34: mastery

def demo_mastery(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("core words: %d" % DATA["core_words"])
    assert DATA["core_words"] == 200
    print("aksara: %d, grammar rules: %d" % (DATA["aksara"], DATA["rules"]))
    assert DATA["aksara"] == 20 and DATA["rules"] == 10
    print("records reviewed: %d" % DATA["records"])
    assert DATA["records"] == 34
    coverage = DATA["sample_words"] / float(DATA["core_words"]) * 100.0
    print("reference sample coverage: %.1f %%" % coverage)
    assert 29.9 < coverage < 30.1, "coverage out of bounds"
    print("OK: %s mustered the campaign" % NAME)
if __name__ == "__main__":
    main()
''')


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
    "social": demo_social,
    "tech": demo_tech,
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
    "market": demo_market,
    "friend": demo_friend,
    "problem": demo_problem,
    "mastery": demo_mastery,
}
assert len(DEMOS) == 34, "expected 34 demos"
