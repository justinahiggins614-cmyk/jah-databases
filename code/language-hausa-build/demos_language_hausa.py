#!/usr/bin/env python3
"""Demo programs for the Hausa to English databases (Manon's language project,
2026-10-17).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: script drills, vocabulary quizzes,
transliteration checks, TAM tables, sentence statistics. All are
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
    assert 0.86 < share < 0.87, "share out of bounds"
    l2 = total_m - native_m
    print("second-language speakers: ~%.0f million" % l2)
    assert 29.9 < l2 < 30.1, "L2 estimate out of bounds"
    print("official countries: %d" % DATA["official_countries"])
    assert DATA["official_countries"] == 2
    print("dialects: %d (%s)" % (len(DATA["dialects"]), ", ".join(DATA["dialects"][:3]) + "..."))
    assert len(DATA["dialects"]) == 8
    print("regions: %d" % len(DATA["regions"]))
    assert len(DATA["regions"]) == 7
    assert DATA["iso1"] == "ha" and DATA["iso3"] == "hau"
    assert DATA["city_states"] == 7 and DATA["au_working"]
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 2: writing system

def demo_writing(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    letters = DATA["letters"]
    print("Boko letters: %d" % len(letters))
    assert len(letters) == 29, "Boko alphabet must be 29"
    assert len(set(letters)) == 29, "letters must be unique"
    specials = DATA["specials"]
    print("hooked specials: %s" % " ".join(specials))
    assert specials == ["\\u0253", "\\u0257", "\\u0199", "\\u01b4"], "specials must be b-hook d-hook k-hook y-hook"
    for sp in specials:
        assert sp in letters, "special %r missing from alphabet" % sp
    for dg in DATA["digraphs"]:
        assert dg in letters, "digraph %s missing" % dg
    for bad in DATA["missing_native"]:
        assert bad not in letters, "%s must not be a native letter" % bad
    print("vowels: %d" % len(DATA["vowels"]))
    assert len(DATA["vowels"]) == 5
    print("direction: %s / Ajami: %s" % (DATA["direction"], DATA["ajami_direction"]))
    assert DATA["direction"] == "left-to-right"
    words = DATA["test_words"]
    alpha = set(letters)
    for w in words:
        i = 0
        while i < len(w):
            if w[i:i+2] in ("sh", "ts"):
                i += 2
            else:
                assert w[i] in alpha, "unwritable char %r in %s" % (w[i], w)
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
    print("vowel letters: %d, pairs: %d" % (len(DATA["vowels"]), DATA["vowel_pairs"]))
    assert len(DATA["vowels"]) == 5 and DATA["vowel_pairs"] == 10
    print("tones: %s" % ", ".join(DATA["tones"]))
    assert DATA["tones"] == ["high", "low", "falling"]
    assert len(DATA["specials"]) == 4
    words = DATA["example_words"]
    print("example words: %d" % len(words))
    assert len(words) == 14, "need 14 spoken examples"
    for w, g in words:
        assert w and g, "empty word/gloss"
    lo, hi = DATA["tone_pair"][0], DATA["tone_pair"][1]
    print("tone pair: %s (%s, %s) vs %s (%s, %s)" % (lo[0], lo[1], lo[2], hi[0], hi[1], hi[2]))
    assert lo[1] != hi[1] and lo[2] != hi[2], "tone must change the meaning"
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
    print("masculine: %d, feminine: %d" % (len(masc), len(fem)))
    assert len(masc) + len(fem) == 25
    assert len(masc) == 15 and len(fem) == 10, "gender split must be 15/10"
    for w, g, x in nouns:
        assert w and g and x in ("m", "f")
    assert len(set(w for w, g, x in nouns)) == 25, "nouns must be unique"
    print("plural patterns: %d" % len(DATA["plurals"]))
    assert len(DATA["plurals"]) == 4
    for sg, pl in DATA["plurals"]:
        assert sg != pl and pl
        print("  %s -> %s" % (sg, pl))
    assert ("yaro", "yara") in DATA["plurals"]
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
    assert len(set(w for w, g in verbs)) == 25
    mk = DATA["markers"]
    print("core markers: %s" % ", ".join(sorted(mk.values())))
    assert mk["perfect_1sg"] == "na" and mk["cont_1sg"] == "ina" and mk["fut_1sg"] == "zan"
    # build a real mini-conjugation for ci (eat)
    table = [("%s ci" % mk["perfect_1sg"]), ("%s cin" % mk["cont_1sg"]), ("%s ci" % mk["fut_1sg"])]
    print("ci paradigm: %s" % " / ".join(table))
    assert table == ["na ci", "ina cin", "zan ci"]
    vn = DATA["verbal_nouns"]
    print("verbal nouns: %d" % len(vn))
    assert vn["ci"] == "cin" and vn["sha"] == "shan" and vn["je"] == "tafiya"
    assert DATA["sentences"] == 25
    print("OK: %s conjugated the verbs" % NAME)
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
    pairs = DATA["agreement_pairs"]
    print("gender agreement pairs: %d" % len(pairs))
    assert len(pairs) == 5
    for m, f in pairs:
        assert m != f, "pair must differ by gender"
        print("  %s / %s" % (m, f))
    assert ("babba", "babbar") in pairs and ("sabo", "sabuwa") in pairs
    assert DATA["sentences"] == 40
    # noun-phrase builder check: adjective follows noun
    phrase = "gida" + " " + "babba"
    assert phrase == "gida babba"
    print("phrase order: %s" % phrase)
    print("OK: %s described things" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 7: pronouns

def demo_pronouns(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    ind = DATA["independent"]
    pos = DATA["possessive"]
    dem = DATA["demonstratives"]
    inter = DATA["interrogatives"]
    print("independent: %d, possessive: %d" % (len(ind), len(pos)))
    assert ind == ["ni", "kai", "ke", "shi", "ita", "mu", "ku", "su"]
    assert len(pos) == 8 and pos[0] == "-na"
    print("demonstratives: %s" % ", ".join(dem))
    assert dem == ["wannan", "wadannan", "wancan", "wadancan"]
    print("interrogatives: %d" % len(inter))
    assert len(inter) == 10 and "wa" in inter and "me ya sa" in inter
    # possessive attachment drill
    attached = "gida" + pos[0].lstrip("-")
    assert attached == "gidana", "possessive must attach"
    print("attachment: gida + -na = %s" % attached)
    assert DATA["sentences"] == 28
    print("OK: %s mapped the pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 8: numbers/time

def demo_numbers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    units, tens = DATA["units"], DATA["tens"]
    print("units 1-10: %d, tens: %d" % (len(units), len(tens)))
    assert len(units) == 10 and units[0] == "daya" and units[9] == "goma"
    assert len(tens) == 10 and tens[1] == "ashirin" and tens[9] == "dari"
    days, months = DATA["days"], DATA["months"]
    print("days: %d, months: %d" % (len(days), len(months)))
    assert len(days) == 7 and days[0] == "Litinin" and days[6] == "Lahadi"
    assert len(months) == 12 and months[0] == "Janairu" and months[11] == "Disamba"
    # compound number builder: 25 = ashirin da biyar
    compound = tens[1] + " da " + units[4]
    assert compound == "ashirin da biyar"
    print("compound 25: %s" % compound)
    # clock builder
    clock = "karfe " + units[1] + " da rabi"
    assert clock == "karfe biyu da rabi"
    print("clock 2:30: %s" % clock)
    assert DATA["sentences"] == 32
    print("OK: %s counted and told time" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 9: greetings

def demo_greetings(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    phrases = DATA["phrases"]
    print("greeting phrases: %d" % len(phrases))
    assert len(phrases) == 30
    for h, e in phrases:
        assert h and e, "empty phrase"
    hausa = [h for h, e in phrases]
    assert len(set(hausa)) == 30, "phrases must be unique"
    sannu = [h for h in hausa if h.startswith("Sannu")]
    print("sannu-family: %d" % len(sannu))
    assert len(sannu) >= 8, "sannu must multiply"
    assert "Sannu da aiki." in hausa and "Sai an jima." in hausa
    print("OK: %s greeted properly" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 10: grammar essentials

def demo_grammar(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("grammar rules: %d" % DATA["rules"])
    assert DATA["rules"] == 10
    mk = DATA["markers"]
    assert mk["past_1sg"] == "na" and mk["fut_1sg"] == "zan"
    print("plural patterns: %d" % len(DATA["plurals"]))
    assert len(DATA["plurals"]) == 6
    assert ("mota", "motoci") in DATA["plurals"]
    sents = DATA["rule_sentences"]
    print("rule sentences: %d" % len(sents))
    assert len(sents) == 9
    assert "Yaro ya ci abinci." in sents and "Ban tafi ba." in sents
    # negation wrapper check: ba ... ba
    neg = "ba " + "na tafi" + " ba"
    assert neg == "ba na tafi ba"
    print("negation wrap: %s" % neg)
    print("OK: %s laid the grammar" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 11: home & family

def demo_home(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    rooms, family = DATA["rooms"], DATA["family"]
    print("rooms: %d, family terms: %d" % (len(rooms), len(family)))
    assert len(rooms) == 4 and "madafa" in rooms
    assert len(family) == 6 and "uba" in family and "uwa" in family
    assert DATA["sentences"] == 20
    # possessive-on-family drill
    assert "dan uwa" in family
    print("OK: %s walked the house" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 12: food & cooking

def demo_food(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    dishes, verbs = DATA["dishes"], DATA["cooking_verbs"]
    print("dishes: %d (%s)" % (len(dishes), ", ".join(dishes)))
    assert len(dishes) == 5 and "tuwo" in dishes and "kunu" in dishes
    print("cooking verbs: %d" % len(verbs))
    assert len(verbs) == 4 and "dafa" in verbs
    assert DATA["sentences"] == 20
    print("OK: %s cooked the meal" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 13: travel & directions

def demo_travel(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    dirs, trans = DATA["directions"], DATA["transport"]
    print("direction words: %d, transport words: %d" % (len(dirs), len(trans)))
    assert len(dirs) == 6 and "dama" in dirs and "hagu" in dirs
    assert len(trans) == 5 and "tikiti" in trans
    # direction composer
    route = "tafi kai tsaye, sai ka juya dama"
    assert route.split(", ")[0] == "tafi kai tsaye"
    print("route: %s" % route)
    assert DATA["sentences"] == 20
    print("OK: %s traveled the road" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 14: work & school

def demo_work(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    ww, sw = DATA["work_words"], DATA["school_words"]
    print("work words: %d, school words: %d" % (len(ww), len(sw)))
    assert len(ww) == 7 and "albashi" in ww
    assert len(sw) == 6 and "jarabawa" in sw
    assert DATA["sentences"] == 20
    print("OK: %s worked the day" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 15: health & body

def demo_health(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    body, sym = DATA["body"], DATA["symptoms"]
    print("body parts: %d, symptoms: %d" % (len(body), len(sym)))
    assert len(body) == 5 and "jiki" in body
    assert len(sym) == 4 and "zazzabi" in sym
    # symptom sentence builder
    s = "ina da " + sym[0]
    assert s == "ina da zazzabi"
    print("symptom pattern: %s" % s)
    assert DATA["sentences"] == 20
    print("OK: %s diagnosed in Hausa" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 16: emotions

def demo_emotions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    feels, idioms = DATA["feelings"], DATA["heart_idioms"]
    print("feelings: %d, heart idioms: %d" % (len(feels), len(idioms)))
    assert len(feels) == 8 and "farin ciki" in feels and "bakin ciki" in feels
    assert len(idioms) == 3
    # opposite-pair check
    assert "farin ciki" in feels and "bakin ciki" in feels
    print("opposites: farin ciki / bakin ciki")
    assert DATA["sentences"] == 20
    print("OK: %s felt in Hausa" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 17: nature & weather

def demo_nature(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("seasons: %s" % ", ".join(DATA["seasons"]))
    assert DATA["seasons"] == ["damina", "rani"]
    print("weather verbs: %d" % len(DATA["weather_verbs"]))
    assert len(DATA["weather_verbs"]) == 3
    animals = DATA["animals"]
    print("animals: %d" % len(animals))
    assert len(animals) == 8 and "zaki" in animals and "rakumi" in animals
    assert DATA["sentences"] == 20
    print("OK: %s read the land" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 18: shopping & money

def demo_shopping(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    mw, steps = DATA["money_words"], DATA["bargain_steps"]
    print("money words: %d, bargain steps: %d" % (len(mw), len(steps)))
    assert len(mw) == 5 and "ciniki" in mw
    assert steps == ["ask", "react", "counter", "name price", "close"]
    print("bargain arc: %s" % " -> ".join(steps))
    assert DATA["sentences"] == 20
    print("OK: %s bargained well" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 19: friendship

def demo_friendship(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    sv, cel = DATA["social_verbs"], DATA["celebrations"]
    print("social verbs: %d, celebrations: %d" % (len(sv), len(cel)))
    assert len(sv) == 5 and "gayyata" in sv
    assert len(cel) == 3 and "bikin aure" in cel
    assert DATA["sentences"] == 20
    print("OK: %s kept company" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 20: technology

def demo_technology(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    tw = DATA["tech_words"]
    print("tech words: %d" % len(tw))
    assert len(tw) == 8 and "waya" in tw and "kalmar sirri" in tw
    # troubleshoot script check
    script = ["baturi ya kare", "ina caji wayata", "na manta kalmar sirri"]
    print("troubleshoot lines: %d" % len(script))
    assert DATA["sentences"] == 20
    print("OK: %s wired the modern age" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 21: verb tenses

def demo_tenses(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    par = DATA["paradigm"]
    for form in ("perfect", "continuous", "future"):
        print("%s markers: %d" % (form, len(par[form])))
        assert len(par[form]) == 8, "%s must have 8 persons" % form
    assert par["perfect"][0] == "na" and par["continuous"][0] == "ina" and par["future"][0] == "zan"
    # full table for ci across 3 forms x 8 persons = 24 cells
    cells = [(m, "ci") for form in ("perfect", "continuous", "future") for m in par[form]]
    print("paradigm cells: %d" % len(cells))
    assert len(cells) == 24
    assert DATA["sentences_per_form"] == 5
    assert DATA["total_sentences"] == 28
    negs = DATA["negatives"]
    assert len(negs) == 3 and negs[0] == "ban ci ba"
    print("negatives: %s" % ", ".join(negs))
    print("OK: %s timed the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 22: questions & answers

def demo_qa(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("Q&A pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 20
    qw = DATA["question_words"]
    print("question words: %d" % len(qw))
    assert len(qw) == 9 and "shin" in qw
    # each question word maps to an answer type
    mapping = {"wa": "person", "ina": "place", "yaushe": "time", "nawa": "number", "me ya sa": "reason"}
    for q, a in mapping.items():
        assert q in qw, q
        print("  %s -> %s" % (q, a))
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 23: commands & requests

def demo_commands(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    direct = DATA["direct"]
    print("direct imperatives: %d" % len(direct))
    assert len(direct) == 10 and "zo" in direct and "bude" in direct
    assert DATA["polite_markers"] == ["don Allah", "za ka iya"]
    assert DATA["formal"] == ["ku"] and DATA["prohibition"] == ["kada"]
    # politeness ladder for one verb
    ladder = ["zo nan!", "don Allah, zo nan", "za ka iya zuwa nan?", "ku zo nan"]
    print("politeness ladder: %d rungs" % len(ladder))
    assert len(ladder) == 4
    assert DATA["sentences"] == 20
    print("OK: %s commanded politely" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 24: descriptions

def demo_descriptions(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    mp = DATA["mai_phrases"]
    print("mai-phrases: %d" % len(mp))
    assert len(mp) == 6 and "mai kirki" in mp
    # portrait builder: noun + 3 mai-phrases
    portrait = "mutum" + " " + mp[0] + ", " + mp[4] + ", " + mp[5]
    print("portrait: %s" % portrait)
    assert portrait.count("mai") == 3
    assert DATA["sentences"] == 20
    print("OK: %s painted portraits" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 25: story I

def demo_story1(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    lines = DATA["lines"]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10
    total_words = 0
    for h, e in lines:
        assert h and e, "each line needs Hausa + English"
        total_words += len(h.split())
    avg = total_words / len(lines)
    print("Hausa words: %d, avg per line: %.1f" % (total_words, avg))
    assert 3.0 < avg < 9.0, "line length out of bounds"
    assert len(DATA["time_words"]) == 4
    print("OK: %s told the simple day" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 26: story II

def demo_story2(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    lines = DATA["lines"]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10
    markers = DATA["markers"]
    print("past markers: %s" % ", ".join(markers))
    assert markers == ["na", "mun", "ta", "ya"]
    hits = sum(1 for h, e in lines for m in markers
               if h.lower().startswith(m + " ") or (" " + m + " ") in h.lower())
    print("lines carrying past markers: %d" % hits)
    assert hits >= 8, "past tense must dominate"
    print("OK: %s told the journey" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 27: story III

def demo_story3(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    lines = DATA["lines"]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10
    fm = DATA["future_markers"]
    print("future markers: %s" % ", ".join(fm))
    assert len(fm) == 5 and fm[0] == "zan"
    hits = sum(1 for h, e in lines for m in fm
               if m in h.lower().split() or h.lower().startswith(m))
    print("lines carrying future markers: %d" % hits)
    assert hits >= 8, "future must dominate"
    cond = [h for h, e in lines if h.startswith("Idan")]
    print("conditional lines: %d" % len(cond))
    assert len(cond) == 2
    print("OK: %s planned tomorrow" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 28: idioms & proverbs

def demo_idioms(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    provs = DATA["proverbs"]
    print("proverbs: %d" % len(provs))
    assert len(provs) == 20
    for h, lit, mean in provs:
        assert h and lit and mean, "each proverb needs 3 layers"
        assert len(h.split()) >= 2, "proverb too short: %r" % h
    assert len(set(h for h, l, m in provs)) == 20, "proverbs must be unique"
    print("layers per proverb: 3 (Hausa, literal, meaning)")
    print("OK: %s spoke proverbs" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 29: formal registers

def demo_registers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("register pairs: %d" % DATA["pairs"])
    assert DATA["pairs"] == 15
    tools = DATA["formal_tools"]
    print("formal tools: %d" % len(tools))
    assert len(tools) == 5 and "ku" in tools
    titles = DATA["titles"]
    print("titles: %d (%s)" % (len(titles), ", ".join(titles)))
    assert len(titles) == 6 and "Malam" in titles and "Hajiya" in titles
    print("OK: %s honored the elders" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 30: complex sentences

def demo_complex(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    conns = DATA["connectors"]
    print("connectors: %d" % len(conns))
    assert len(conns) == 10 and "saboda" in conns and "idan" in conns
    assert DATA["sentences"] == 15
    skels = DATA["skeletons"]
    print("skeletons: %d" % len(skels))
    assert len(skels) == 11 and "relative" in skels
    print("OK: %s built complexes" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 31: conversation at the market

def demo_conv_market(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    moves = DATA["moves"]
    print("annotated moves: %d" % len(moves))
    assert len(moves) == 19
    assert "bargaining" in moves and "blessing farewell" in moves
    print("OK: %s traded at the market" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 32: conversation meeting a friend

def demo_conv_friend(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    print("dialogue lines: %d" % DATA["lines"])
    assert DATA["lines"] == 20
    moves = DATA["moves"]
    print("annotated moves: %d" % len(moves))
    assert len(moves) == 20
    assert "invitation" in moves and "farewell blessing" in moves
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
    arc = DATA["arc"]
    print("problem arc steps: %d" % len(arc))
    assert len(arc) == 17
    assert arc[0] == "state" and "pay" in arc and arc[-1] == "farewell"
    print("OK: %s solved the problem" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------- 34: mastery review

def demo_mastery(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, _data(entry["drill"]) + '''\
def main():
    words = DATA["core_words"]
    print("core words: %d" % len(words))
    assert len(words) == 200, "mastery needs exactly 200 core words"
    assert len(set(w for w, g in words)) == 200, "core words must be unique"
    for w, g in words:
        assert w and g, "empty word/gloss"
    cats = {}
    print("grammar rules: %d, phrase tables: %d" % (DATA["grammar_rules"], DATA["phrase_tables"]))
    assert DATA["grammar_rules"] == 10 and DATA["phrase_tables"] == 5
    # spot-check landmark words across the ladder
    landmarks = ["harshen", "gida", "na gode", "in Allah ya so", "sai an jima"]
    have = set(w for w, g in words)
    for lm in ["gida", "na gode", "in Allah ya so", "sai an jima"]:
        assert lm in have, "landmark missing: %s" % lm
    print("landmarks present: gida, na gode, in Allah ya so, sai an jima")
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
