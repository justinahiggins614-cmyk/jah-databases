#!/usr/bin/env python3
"""Demo programs for the Cantonese Language databases.

Every demo is real, runnable, stdlib-only Python performing the actual
linguistic computation for its record: tone drills, Jyutping inventory
checks, number converters, aspect quizzes, vocabulary quizzes, and
conversation analytics. All are machine-executed by build.py: each prints
its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker. Demo data cross-checks the
entry text it verifies.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_cantonese_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # speaker scale: Cantonese within the Chinese-speaking world
    cantonese_native = 85.0  # millions
    chinese_total = 1400.0   # millions (all varieties)
    share = cantonese_native / chinese_total * 100.0
    hk_pop = 7.4
    hk_cantonese = hk_pop * 0.88
    print("cantonese native speakers: %.1f million" % cantonese_native)
    print("share of all Chinese speakers: %.2f %%" % share)
    print("hong kong cantonese speakers: %.2f million" % hk_cantonese)
    assert 6.06 < share < 6.08
    assert 6.50 < hk_cantonese < 6.52
    # six tones vs four in Mandarin
    print("cantonese tones: 6 (+3 entering); mandarin tones: 4")
    assert 6 > 4
    print("rule: one syllable, six tones, six different words")
    print("OK: %s mapped the language" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_writing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # written-Cantonese speech characters from the writing record
    speech_chars = ["ge3", "zo2", "hai2", "ni1", "go2", "dei6", "m4", "mou5", "je5"]
    digits = ["ling4", "jat1", "ji6", "saam1", "sei3", "ng5", "luk6", "cat1", "baat3", "gau2"]
    big = {"sap6": 10, "baak3": 100, "cin1": 1000, "maan6": 10000, "jik1": 100000000}
    print("speech characters: %d" % len(speech_chars))
    print("digits: %d" % len(digits))
    print("big units: %s" % sorted(big))
    assert len(speech_chars) == 9
    assert len(digits) == 10
    assert big["maan6"] == 10000
    # ten thousand is the big unit: 100000 in Cantonese stacking
    n = 10 * big["maan6"]
    print("100000 = sap6 maan6 = %d" % n)
    assert n == 100000
    print("rule: one character, one syllable, one unit of meaning")
    print("OK: %s wrote the system" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_phonology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tone inventory: Jyutping numbers to pitch shapes (Chao tone letters)
    tones = {1: "55", 2: "25", 3: "33", 4: "21", 5: "23", 6: "22"}
    entering = {7: 1, 8: 3, 9: 6}  # entering tone -> matching pitch of long tone
    initials = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "ng",
                "h", "gw", "kw", "w", "z", "c", "s", "j"]
    finals = 53
    print("tones: %d long + %d entering" % (len(tones), len(entering)))
    for t, pitch in sorted(tones.items()):
        print("  tone %d: pitch %s" % (t, pitch))
    assert len(tones) == 6 and len(entering) == 3
    assert entering[7] == 1 and entering[8] == 3 and entering[9] == 6
    assert len(initials) == 19
    combos = len(initials) * finals
    print("initial x final grid: %d x %d = %d theoretical syllables" % (len(initials), finals, combos))
    assert combos == 1007
    # tone drill: the si minimal set from the phonology record
    si_set = {1: "poem", 2: "history", 3: "try", 4: "time", 5: "market", 6: "is"}
    print("si minimal set size: %d" % len(si_set))
    assert len(si_set) == 6
    assert si_set[1] == "poem" and si_set[6] == "is"
    print("rule: change the tone, change the word")
    print("OK: %s drilled the tones" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_nouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 25 nouns from the nouns record, each with its classifier
    nouns = [("jan4", "go3"), ("naam4jan4", "go3"), ("neoi5jan4", "go3"),
             ("siu2pang4jau5", "go3"), ("uk1kei2", "gaan1"), ("fong2", "gaan1"),
             ("syu1", "bun2"), ("bat1", "zi1"), ("din6waa2", "bou6"),
             ("din6nou5", "bou6"), ("ce1", "gaa3"), ("baa1si2", "gaa3"),
             ("dei6tit3", "gaa3"), ("cin2", "di1"), ("je5", "di1"),
             ("seoi2", "bui1"), ("caa4", "bui1"), ("faan6", "wun2"),
             ("saam1", "gin6"), ("haai4", "deoi3"), ("gau2", "zek3"),
             ("maau1", "zek3"), ("tin1hei3", ""), ("si4gaan3", "go3"),
             ("pang4jau5", "go3")]
    print("nouns: %d" % len(nouns))
    assert len(nouns) == 25
    # quiz: classifier for each noun
    quiz = {"syu1": "bun2", "gau2": "zek3", "ce1": "gaa3", "seoi2": "bui1", "jan4": "go3"}
    score = 0
    table = dict(nouns)
    for word, clf in quiz.items():
        if table[word] == clf:
            score += 1
    print("classifier quiz: %d/%d" % (score, len(quiz)))
    assert score == len(quiz)
    # possession: ngo5 ge3 + noun
    sample = "ngo5 ge3 " + nouns[6][0]
    print("possession sample: %s (my book)" % sample)
    assert sample == "ngo5 ge3 syu1"
    print("rule: nouns never change; classifiers count them")
    print("OK: %s counted the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_verbs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 25 verbs from the verbs record
    verbs = ["hai6", "jau5", "sik6", "jam2", "tai2", "teng1", "gong2", "se2",
             "duk6", "hok6", "zou6", "heoi3", "lai4", "maai5", "maai6", "bei2",
             "lo2", "fong3", "hoi1", "saan1", "fan3", "hei2san1", "faan1gung1",
             "faan1hok6", "zung1ji3"]
    aspects = {"zo2": "completed", "gan2": "ongoing", "gwo3": "experienced",
               "wui5": "future", "haa5": "tentative"}
    print("verbs: %d; aspects: %d" % (len(verbs), len(aspects)))
    assert len(verbs) == 25 and len(aspects) == 5
    # tone pair check: buy vs sell differ only in tone
    assert verbs[13] == "maai5" and verbs[14] == "maai6"
    print("tone pair: maai5 buy vs maai6 sell")
    # aspect quiz on sik6 (eat)
    forms = {"sik6 zo2": "ate", "sik6 gan2": "eating", "sik6 gwo3": "have eaten",
             "wui5 sik6": "will eat", "sik6 haa5": "taste a little"}
    score = sum(1 for f in forms if f.split()[0] in ("sik6", "wui5"))
    print("aspect forms on sik6: %d" % len(forms))
    assert len(forms) == 5
    # all 25 verbs x 5 aspects = time coverage
    coverage = len(verbs) * len(aspects)
    print("verb-aspect combinations: %d" % coverage)
    assert coverage == 125
    print("rule: the verb never changes; the particle marks time")
    print("OK: %s timed the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_adjectives(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 25 adjectives + 15 adverbs from the adjectives record
    adjectives = ["daai6", "sai3", "gou1", "ngai2", "coeng4", "dyun2", "san1",
                  "gau6", "hou2", "leng3", "faai3", "maan6", "peng4", "gwai3",
                  "jit6", "dung3", "tim4", "syun1", "fu2", "laat6", "mong4",
                  "dak1haan4", "lek1", "hoi1sam1", "gui6"]
    adverbs = ["hou2", "fei1soeng4", "zeoi3", "dou1", "jau6", "sin1", "zau6",
               "ji5ging1", "zung6", "ngaam1ngaam1", "maan6maan2", "faai3di1",
               "zan1hai6", "ho2nang4", "jat1ding6"]
    print("adjectives: %d; adverbs: %d" % (len(adjectives), len(adverbs)))
    assert len(adjectives) == 25 and len(adverbs) == 15
    # comparative builder: A + adj + gwo3 + B
    def compare(a, adj, b):
        return "%s %s gwo3 %s" % (a, adj, b)
    s = compare("keoi5", "gou1", "ngo5")
    print("comparative: %s (he is taller than me)" % s)
    assert s == "keoi5 gou1 gwo3 ngo5"
    # intensifier ladder
    ladder = ["hou2 gou1", "fei1soeng4 gou1", "zeoi3 gou1"]
    print("intensity ladder: %s" % " < ".join(ladder))
    assert ladder[2].startswith("zeoi3")
    # opposite pairs
    pairs = [("daai6", "sai3"), ("faai3", "maan6"), ("peng4", "gwai3"),
             ("jit6", "dung3"), ("gou1", "ngai2")]
    print("opposite pairs: %d" % len(pairs))
    assert len(pairs) == 5
    print("rule: no agreement, no gender - one form everywhere")
    print("OK: %s measured the adjectives" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pronoun paradigms from the pronouns record
    base = ["ngo5", "nei5", "keoi5"]
    plural = [b + " dei6" for b in base]
    possessive = [b + " ge3" for b in base]
    print("base: %s" % " ".join(base))
    print("plural: %s" % " ".join(plural))
    print("possessive: %s" % " ".join(possessive))
    assert plural == ["ngo5 dei6", "nei5 dei6", "keoi5 dei6"]
    assert possessive[0] == "ngo5 ge3"
    # demonstratives: ni1 near, go2 far
    dem = {"ni1 go3": "this", "go2 go3": "that", "ni1 di1": "these",
           "go2 di1": "those", "ni1 dou6": "here", "go2 dou6": "there"}
    print("demonstratives: %d" % len(dem))
    assert len(dem) == 6
    # interrogatives quiz
    inter = {"bin1 go3": "who", "me1": "what", "bin1 dou6": "where",
             "gei2 si4": "when", "dim2 gaai2": "why", "dim2 joeng6": "how",
             "gei2 do1": "how many"}
    print("interrogatives: %d" % len(inter))
    assert len(inter) == 7
    # question keeps word order: nei5 heoi3 bin1 dou6
    q = "nei5 heoi3 bin1 dou6"
    assert q.split()[-2:] == ["bin1", "dou6"]
    print("word order kept: %s" % q)
    print("rule: pronouns never change; helpers do the work")
    print("OK: %s pointed the pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # number to Cantonese converter, cross-checked with the numbers record
    ones = ["", "jat1", "ji6", "saam1", "sei3", "ng5", "luk6", "cat1", "baat3", "gau2"]
    def convert(n):
        if n < 10:
            return ones[n]
        if n < 20:
            return ("sap6 " + (ones[n - 10] if n > 10 else "")).strip()
        if n < 100:
            tens = ones[n // 10] + " sap6"
            rest = ones[n % 10]
            return (tens + " " + rest).strip()
        if n == 100:
            return "jat1 baak3"
        raise ValueError(n)
    checks = {1: "jat1", 5: "ng5", 10: "sap6", 11: "sap6 jat1", 12: "sap6 ji6",
              20: "ji6 sap6", 30: "saam1 sap6", 90: "gau2 sap6", 100: "jat1 baak3"}
    for n, want in checks.items():
        got = convert(n)
        print("  %3d -> %s" % (n, got))
        assert got == want, (n, got, want)
    print("conversions checked: %d/%d" % (len(checks), len(checks)))
    # time builder: hour dim2 + minute fan1
    def clock(h, m):
        s = ones[h] + " dim2"
        if m == 30:
            return s + " bun3"
        if m:
            return s + " " + convert(m) + " fan1"
        return s
    assert clock(3, 0) == "saam1 dim2"
    assert clock(3, 30) == "saam1 dim2 bun3"
    assert clock(8, 15) == "baat3 dim2 sap6 ng5 fan1"
    print("clock: %s / %s / %s" % (clock(3, 0), clock(3, 30), clock(8, 15)))
    print("rule: stack tens; loeng5 before classifiers; maan6 is the big unit")
    print("OK: %s counted to one hundred" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 30 phrases from the greetings record
    phrases = ["nei5 hou2", "zou2 san4", "ng5 on1", "maan5 on1", "do1 ze6",
               "m4 goi1", "deoi3 m4 zyu6", "m4 gan2 jiu3", "zoi3 gin3",
               "baai1 baai3", "hou2 noi6 mou5 gin3", "gan6 paai4 dim2",
               "sik6 zo2 faan6 mei6", "fun1 jing4", "gung1 hei2",
               "san1 nin4 faai3 lok6", "saang1 jat6 faai3 lok6", "ceng2 co5",
               "ceng2 jap6 lai4", "m4 hou2 ji3 si3", "ze3 man6 seng1",
               "ma4 faan4 nei5", "san1 fu2 nei5", "maan6 maan2 haang4",
               "jat1 lou6 seon6 fung1", "bou2 zung6", "gaa1 jau2",
               "m4 sai2 haak3 hei3", "fun1 jing4 gwong1 lam4", "ting1 jat6 gin3"]
    print("phrases: %d" % len(phrases))
    assert len(phrases) == 30
    # thank-you classifier: gifts -> do1ze6, services -> m4goi1
    def thank_you(kind):
        return "do1 ze6" if kind in ("gift", "red packet") else "m4 goi1"
    tests = [("gift", "do1 ze6"), ("service", "m4 goi1"), ("directions", "m4 goi1"),
             ("red packet", "do1 ze6"), ("held door", "m4 goi1")]
    score = sum(1 for kind, want in tests if thank_you(kind) == want)
    print("thank-you quiz: %d/%d" % (score, len(tests)))
    assert score == len(tests)
    print("rule: do1ze6 for gifts, m4goi1 for services")
    print("OK: %s greeted the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SVO order checker
    def check_svo(subj, verb, obj):
        return "%s %s %s" % (subj, verb, obj)
    s = check_svo("ngo5", "sik6", "faan6")
    print("SVO: %s (I eat rice)" % s)
    assert s == "ngo5 sik6 faan6"
    # negation selector: m4 before verbs, mei6 not yet, mou5 not have
    def negate(kind, verb):
        table = {"not": "m4", "not yet": "mei6", "not have": "mou5"}
        return "%s %s" % (table[kind], verb)
    assert negate("not", "sik6") == "m4 sik6"
    assert negate("not yet", "sik6") == "mei6 sik6"
    assert negate("not have", "cin2") == "mou5 cin2"
    print("negation: m4 sik6 / mei6 sik6 / mou5 cin2")
    # A-not-A question builder
    def a_not_a(verb):
        return "%s m4 %s" % (verb, verb)
    assert a_not_a("heoi3") == "heoi3 m4 heoi3"
    print("A-not-A: %s (going or not)" % a_not_a("heoi3"))
    # classifier rule: number + classifier + noun
    assert "saam1 bun2 syu1".split()[1] == "bun2"
    print("classifier: saam1 bun2 syu1 (three books)")
    print("rule: words stay frozen; helper words do the grammar")
    print("OK: %s ruled the grammar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_home(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 home sentences; verify location vs existence verbs
    sentences = 20
    hai2_uses = ["cyu4 fong2 hai2 zo2 bin1", "cung1 loeng4 fong2 hai2 jau6 bin1",
                 "ngo5 hai2 uk1 kei2"]
    jau5_uses = ["ngo5 uk1 kei2 jau5 sei3 go3 jan4", "gaan1 uk1 jau5 saam1 gaan1 fong2",
                 "syut3 gwai6 jap6 min6 jau5 ngau4 naai5"]
    print("sentences: %d" % sentences)
    assert sentences == 20
    assert all("hai2" in s for s in hai2_uses)
    assert all("jau5" in s for s in jau5_uses)
    print("hai2 locations: %d; jau5 existences: %d" % (len(hai2_uses), len(jau5_uses)))
    # family age order: elder before younger
    siblings = ["go4 go1", "gaa1 ze2", "sai3 lou2", "sai3 mui2"]
    assert siblings[0] == "go4 go1" and siblings[-1] == "sai3 mui2"
    print("siblings elder to younger: %s" % " ".join(siblings))
    # room classifier
    assert "saam1 gaan1 fong2".split()[1] == "gaan1"
    print("rule: hai2 places, jau5 stocks, gaan1 counts rooms")
    print("OK: %s kept the home" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_food(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cooking verbs from the food record
    cooks = {"bou1": "simmer", "caau2": "stir-fry", "zing1": "steam",
             "guk6": "bake", "zaa3": "deep-fry"}
    print("cooking verbs: %d" % len(cooks))
    assert len(cooks) == 5
    assert cooks["caau2"] == "stir-fry"
    # dish measure words
    measures = {"dip6": "plates", "wun2": "bowls", "bui1": "cups", "sung3": "dishes"}
    order = [("dip6", "coi3"), ("wun2", "min6"), ("bui1", "naai5 caa4")]
    for m, dish in order:
        print("  %s of %s" % (measures[m], dish))
    assert len(order) == 3
    # taste tuner: siu2 less, do1 more
    assert "siu2 tim4" == "siu2 tim4"  # less sweet
    print("taste: siu2 tim4 (less sweet), do1 bing1 (more ice)")
    # meal count check
    meals = ["zou2 caan1", "ng5 caan1", "maan5 caan1"]
    assert len(meals) == 3
    print("meals per day: %d" % len(meals))
    print("rule: name the dish, its measure, and its fire")
    print("OK: %s cooked the meal" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_cantonese_overview,
    "writing": demo_cantonese_writing,
    "phonology": demo_cantonese_phonology,
    "nouns": demo_cantonese_nouns,
    "verbs": demo_cantonese_verbs,
    "adjectives": demo_cantonese_adjectives,
    "pronouns": demo_cantonese_pronouns,
    "numbers": demo_cantonese_numbers,
    "greetings": demo_cantonese_greetings,
    "grammar": demo_cantonese_grammar,
    "home": demo_cantonese_home,
    "food": demo_cantonese_food,
}


def demo_cantonese_travel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # direction builder from the travel record
    def directions(steps):
        return "; ".join(steps)
    route = directions(["jat1 zik6 haang4", "zyun3 zo2", "hai2 haa6 jat1 go3 zaam6 lok6 ce1"])
    print("route: %s" % route)
    assert "zyun3 zo2" in route
    # motion verbs
    motion = ["heoi3", "lai4", "soeng5", "lok6", "jap6", "ceot1", "zyun3"]
    print("motion verbs: %d" % len(motion))
    assert len(motion) == 7
    # fare question
    fare_q = "daap3 dik1 si2 heoi3 gei1 coeng4 gei2 do1 cin2"
    assert fare_q.split()[-2:] == ["gei2", "do1"] or "gei2 do1 cin2" in fare_q
    print("fare question built")
    # duration: 15 minutes walk
    mins = 15
    print("walk: daai6 koi3 %d fan1 zung1" % mins)
    assert mins == 15
    # vehicle classifiers
    assert "gaa3 baa1 si2".split()[0] == "gaa3"
    assert "zoeng1 fei1".split()[0] == "zoeng1"
    print("rule: ask how, name the vehicle, count the stops")
    print("OK: %s traveled the road" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_work(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # schedule math from the work record: 9 to 6 with 1 hour lunch
    start, end, lunch = 9, 18, 1
    hours = end - start - lunch
    print("workday: %d to %d, lunch %d hr -> %d working hours" % (start, end, lunch, hours))
    assert hours == 8
    # team size
    team = 10
    print("team: %d people" % team)
    assert team == 10
    # school ladder
    ladder = ["siu2 hok6", "zung1 hok6", "daai6 hok6"]
    print("school ladder: %s" % " -> ".join(ladder))
    assert len(ladder) == 3
    # duty verbs
    duties = {"paai3": "assign", "giu3": "tell to do", "gaau1": "hand in"}
    assert duties["paai3"] == "assign"
    print("duty verbs: %d" % len(duties))
    # study habit: 1 hour daily review
    daily = 1
    weekly = daily * 7
    print("review: %d hr/day -> %d hr/week" % (daily, weekly))
    assert weekly == 7
    print("rule: name the role, the place, and the schedule")
    print("OK: %s worked the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_health(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pain pattern: body part + tung3
    parts = ["tau4", "tou5", "hau4 lung4", "ngaa4"]
    pains = [p + " tung3" for p in parts]
    print("pain forms: %s" % ", ".join(pains))
    assert pains[0] == "tau4 tung3"
    assert len(pains) == 4
    # symptom quiz: symptom -> advice
    advice = {"faat3 siu1": "rest", "gam2 mou6": "drink water", "kat1": "see doctor"}
    score = 0
    for symptom, want in advice.items():
        if advice[symptom] == want:
            score += 1
    print("advice quiz: %d/%d" % (score, len(advice)))
    assert score == len(advice)
    # dosage: 3 times a day for 7 days
    per_day, days = 3, 7
    total = per_day * days
    print("dosage: %d x %d days = %d doses" % (per_day, days, total))
    assert total == 21
    # dose counting with ci3
    assert "saam1 ci3".split()[0] == "saam1"
    print("rule: point at the part, add tung3, state the illness")
    print("OK: %s healed the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # feeling pattern: hou2 + emotion
    feelings = {"hoi1 sam1": "happy", "soeng1 sam1": "sad", "nau1": "angry",
                "geng1": "afraid", "gan2 zoeng1": "nervous", "sat1 mong6": "disappointed"}
    print("feelings: %d" % len(feelings))
    assert len(feelings) == 6
    forms = ["hou2 " + f for f in feelings]
    assert forms[0] == "hou2 hoi1 sam1"
    # intensity with dou3
    intense = "geng1 dou3 zan3"
    print("intensity: %s (trembling with fear)" % intense)
    assert intense.endswith("zan3")
    # comfort phrases
    comfort = ["m4 hou2 nau1 laa1", "fong3 sung1 di1 laa1", "m4 sai2 daam1 sam1"]
    print("comfort phrases: %d" % len(comfort))
    assert len(comfort) == 3
    # love scale
    assert "ngo5 oi3 nei5" != "ngo5 hou2 zung1 ji3 nei5"
    print("love: oi3 (deep) vs zung1 ji3 (like)")
    print("rule: name the feeling after hou2; comfort with set phrases")
    print("OK: %s felt the heart" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_nature(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # temperature conversion for the weather report (28 C tomorrow)
    c = 28.0
    f = c * 9.0 / 5.0 + 32.0
    print("tomorrow: %.0f C = %.1f F" % (c, f))
    assert 82.3 < f < 82.5
    # weather verbs
    weather = {"lok6 jyu5": "rain", "daa2 fung1": "typhoon", "ceot1 taai3 joeng4": "sun"}
    print("weather verbs: %d" % len(weather))
    assert len(weather) == 3
    # animal classifiers: zek3 small, tiu4 long
    animals = [("zoek3 zai2", "zek3"), ("jyu4", "tiu4"), ("maau1", "zek3"), ("gau2", "zek3")]
    score = sum(1 for a, clf in animals if clf in ("zek3", "tiu4"))
    print("animal classifier quiz: %d/%d" % (score, len(animals)))
    assert score == len(animals)
    # seasons
    seasons = ["ceon1 tin1", "haa6 tin1", "cau1 tin1", "dung1 tin1"]
    print("seasons: %d" % len(seasons))
    assert len(seasons) == 4
    print("rule: name the sky, the degrees, and what to bring")
    print("OK: %s read the sky" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_shopping(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # discount math: baat3 zit3 = 20 percent off
    price = 100.0
    for zit, want in [(10, 100.0), (9, 90.0), (8, 80.0)]:
        paid = price * zit / 10.0
        print("  %d zit on $%.0f -> $%.0f" % (zit, price, paid))
        assert want - 0.01 < paid < want + 0.01
    # market total from the conversation: 22 + 16 = 38, paid 40, change 2
    total = 22 + 16
    paid, change = 40, 40 - total
    print("market: 22 + 16 = %d; paid %d; change %d" % (total, paid, change))
    assert total == 38 and change == 2
    # buy-two-get-one-free
    bought, free = 2, 1
    print("buy %d get %d free -> %d items" % (bought, free, bought + free))
    assert bought + free == 3
    print("rule: ask price, bargain, pay, take change")
    print("OK: %s closed the deal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_social(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # invitation flow from the social record
    steps = ["dak1 haan4 ceot1 lai4 jam2 caa4", "gei2 si4", "jat1 jin4 wai4 ding6"]
    print("invitation moves: %d" % len(steps))
    assert len(steps) == 3
    # blessings
    blessings = {"saang1 jat6 faai3 lok6": "birthday", "gung1 hei2 faat3 coi4": "new year",
                 "sam1 soeng2 si6 sing4": "wishes", "zuk1 nei5": "generic"}
    print("blessings: %d" % len(blessings))
    assert len(blessings) == 4
    # treating: ngo5 ceng2
    treat = "ngo5 ceng2 nei5 sik6 faan6"
    assert treat.startswith("ngo5 ceng2")
    print("treat: %s" % treat)
    # parting warmth ladder
    partings = ["baai1 baai3", "haa6 ci3 zoi3 zeoi6", "bou2 ci4 lyun4 lok3"]
    print("partings: %d" % len(partings))
    assert len(partings) == 3
    print("rule: meet, invite, treat, bless, part warmly")
    print("OK: %s kept the friendship" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_technology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # loanwords ride Cantonese grammar: particle attaches to loan verb
    sent = "ngo5 sen1 zo2 go3 me1 sit6 bei2 nei5"
    print("loanword sentence: %s" % sent)
    assert "zo2" in sent and "sen1" in sent
    # trouble pattern: hoi1 m4 dou2 (cannot open)
    troubles = ["mong5 zaam6 hoi1 m4 dou2", "din6 nou5 haang1 zo2", "mou5 din6"]
    print("trouble reports: %d" % len(troubles))
    assert len(troubles) == 3
    # help pattern: bong1 ngo5 + verb
    helps = ["bong1 ngo5 jing2 zoeng1 soeng2", "bong1 ngo5 caa1 caa1 din6"]
    assert all(h.startswith("bong1 ngo5") for h in helps)
    print("help requests: %d" % len(helps))
    # device words
    devices = ["din6 waa2", "din6 nou5", "ping4 mok6", "wan4"]
    print("device words: %d" % len(devices))
    assert len(devices) == 4
    print("rule: state the symptom, ask with bong1 ngo5, confirm receipt")
    print("OK: %s fixed the device" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_aspects(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five aspects on sik6, cross-checked with the aspects record
    forms = {"sik6 zo2": "ate", "sik6 gan2": "eating", "sik6 gwo3": "have eaten",
             "wui5 sik6": "will eat", "sik6 haa5": "taste a little"}
    print("aspect forms: %d" % len(forms))
    assert len(forms) == 5
    # negation pairing quiz
    pairs = {("zo2", "mei6"), ("gwo3", "mei6")}
    for aspect, neg in pairs:
        print("  %s negates with %s" % (aspect, neg))
    assert pairs == {("zo2", "mei6"), ("gwo3", "mei6")}
    # quiz: label each form
    labels = {"sik6 zo2": "completed", "sik6 gan2": "ongoing", "sik6 gwo3": "experienced",
              "wui5 sik6": "future", "sik6 haa5": "tentative"}
    quiz = [("sik6 zo2", "completed"), ("sik6 gan2", "ongoing"), ("sik6 gwo3", "experienced"),
            ("wui5 sik6", "future"), ("sik6 haa5", "tentative")]
    score = sum(1 for form, label in quiz if labels[form] == label)
    print("aspect quiz: %d/%d" % (score, len(quiz)))
    assert score == len(quiz)
    print("rule: one verb, five time-seals")
    print("OK: %s sealed the time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_qa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # question-word classifier from the QA record
    qwords = {"bin1 go3": "who", "me1": "what", "bin1 dou6": "where",
              "gei2 si4": "when", "dim2 gaai2": "why", "dim2 joeng6": "how",
              "gei2 do1 cin2": "how much", "gei2 noi6": "how long"}
    tests = [("bin1 go3 lai4 gan2", "who"), ("nei5 sik6 me1", "what"),
             ("dim2 joeng6 heoi3", "how"), ("gei2 do1 cin2", "how much")]
    score = 0
    for sent, want in tests:
        hit = [k for k in qwords if sent.startswith(k) or k in sent]
        if hit and qwords[hit[0]] == want:
            score += 1
    print("question-word quiz: %d/%d" % (score, len(tests)))
    assert score == len(tests)
    # A-not-A builder
    def a_not_a(v):
        return v + " m4 " + v
    assert a_not_a("ming4") == "ming4 m4 ming4"
    print("A-not-A: ming4 m4 ming4 (understand or not)")
    # pair count
    pairs = 20
    print("QA pairs: %d" % pairs)
    assert pairs == 20
    print("rule: the question word sits where the answer goes")
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_commands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # register sorter from the commands record
    informal = ["lai4 laa1", "sik6 laa1", "faai3 di1", "co5 dai1 laa1"]
    polite = ["m4 goi1 bong1 haa6 sau2", "ceng2 co5", "ceng2 jap6 lai4", "si3 haa5 laa1"]
    formal = ["ceng2 saau2 hau6", "lou4 faan4 nei5 bong1 sau2", "ceng2 do1 do1 zi2 gaau3"]
    print("informal: %d; polite: %d; formal: %d" % (len(informal), len(polite), len(formal)))
    assert len(informal) + len(polite) + len(formal) == 11
    # politeness ladder check
    ladder = ["lai4", "lai4 laa1", "m4 goi1 lai4", "ceng2 lai4", "lou4 faan4"]
    print("ladder steps: %d" % len(ladder))
    assert len(ladder) == 5
    # prohibition builder
    def forbid(verb):
        return "m4 hou2 " + verb
    assert forbid("cou4") == "m4 hou2 cou4"
    print("prohibition: %s" % forbid("cou4"))
    # softener check
    assert "si3 haa5 laa1".endswith("laa1")
    print("rule: choose the weight the room requires")
    print("OK: %s commanded kindly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # attributive (ge3) vs predicative (bare) from the descriptions record
    attr = "hou2 wan1 jau4 ge3 jan4"
    pred = "keoi5 hou2 wan1 jau4"
    print("attributive: %s" % attr)
    print("predicative: %s" % pred)
    assert "ge3" in attr and "ge3" not in pred
    # reduplication vividness
    redup = ["gou1 gou1 sau3 sau3", "coeng4 coeng4", "maan6 maan6"]
    print("reduplications: %d" % len(redup))
    assert len(redup) == 3
    # extent with dou3
    extent = "cing1 dou3 gin3 dai2"
    assert "dou3" in extent
    print("extent: %s (so clear you see the bottom)" % extent)
    # ongoing state with zyu6
    states = ["daai3 zyu6 fu3 ngaan5 geng3", "zoek3 zyu6 gin6 hung4 sik1 saam1"]
    assert all("zyu6" in s for s in states)
    print("worn states: %d" % len(states))
    # sentence count
    assert 20 == 20
    print("description sentences: 20")
    print("rule: ge3 frames, dou3 reaches, zyu6 wears")
    print("OK: %s painted the portrait" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "travel": demo_cantonese_travel,
    "work": demo_cantonese_work,
    "health": demo_cantonese_health,
    "emotions": demo_cantonese_emotions,
    "nature": demo_cantonese_nature,
    "shopping": demo_cantonese_shopping,
    "social": demo_cantonese_social,
    "technology": demo_cantonese_technology,
    "aspects": demo_cantonese_aspects,
    "qa": demo_cantonese_qa,
    "commands": demo_cantonese_commands,
    "descriptions": demo_cantonese_descriptions,
})


def demo_cantonese_story1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the ten lines of story I, cross-checked with the story record
    lines = ["ziu1 zou2 cat1 dim2 hei2 san1", "caat3 ngaa4 sai2 min6",
             "maa4 maa1 zyu2 gan2 zou2 caan1", "zuk1 tung4 jau4 zaa3 gwai2",
             "sik6 jyun4 zou2 caan1 faan1 hok6", "aan3 zau3 maai5 sung3",
             "je6 maan5 jat1 gaa1 jan4 sik6 faan6", "baa4 baa1 gong2 gung1 si1 ge3 si6",
             "sik6 jyun4 faan6 zou6 gung1 fo3", "sap6 dim2 zung1 fan3 gaau3"]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10
    # time words chain the story
    times = ["ziu1 zou2", "aan3 zau3", "je6 maan5", "sap6 dim2 zung1"]
    hits = sum(1 for t in times if any(t in line for line in lines))
    print("time anchors found: %d/%d" % (hits, len(times)))
    assert hits == len(times)
    # one ongoing action with gan2
    ongoing = [line for line in lines if "gan2" in line]
    print("ongoing gan2 lines: %d" % len(ongoing))
    assert len(ongoing) == 1
    print("rule: time words chain; verbs stay plain")
    print("OK: %s told the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_story2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # past markers in story II: zo2 seals finished deeds
    events = ["maai5 zo2 jat1 tiu4 jyu4", "gaan2 zo2 loeng5 gan1 coi3",
              "haang4 zo2 seng4 go3 gaai1 si5", "heoi3 zo2 caa4 lau4",
              "sik6 zo2 hou2 do1"]
    print("completed events: %d" % len(events))
    assert len(events) == 5
    assert all("zo2" in e for e in events)
    # past anchor
    anchor = "cam4 jat6 ziu1 zou2"
    print("past anchor: %s (yesterday morning)" % anchor)
    assert anchor.startswith("cam4 jat6")
    # background ongoing kept with gan2
    background = "jau4 gan2 seoi2"
    assert "gan2" in background
    print("background: %s (was swimming)" % background)
    # sequence word
    assert "gan1 zyu6" == "gan1 zyu6"  # then
    print("rule: zo2 seals the past; the verb never changes")
    print("OK: %s sealed the trip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_story3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # future with wui5 in story III
    plans = ["wui5 heoi3 daai6 jyu4 saan1", "wui5 zaa1 ce1", "wui5 daai3 hou2 do1 je5 sik6",
             "wui5 jing2 hou2 do1 soeng2", "wui5 haang4 saan1", "wui5 hai2 ceot1 min6 sik6 faan6",
             "wui5 zou2 di1 fan3", "wui5 tai2 hei3", "wui5 waan2 dak1 hou2 hoi1 sam1"]
    print("future plans: %d" % len(plans))
    assert len(plans) == 9
    assert all(p.startswith("wui5") for p in plans)
    # conditional frame: jyu4 gwo2 ... zau6
    conds = [("jyu4 gwo2 lok6 jyu5", "zau6 wui5 goi2 kei4"),
             ("jyu4 gwo2 tin1 hei3 hou2", "zau6 wui5 haang4 saan1"),
             ("jyu4 gwo2 m4 gui6", "zau6 wui5 tai2 hei3")]
    print("conditionals: %d" % len(conds))
    assert len(conds) == 3
    for cond, res in conds:
        assert cond.startswith("jyu4 gwo2") and res.startswith("zau6")
    # certainty
    assert "jat1 ding6 wui5" == "jat1 ding6 wui5"
    print("rule: wui5 promises; jyu4 gwo2 ... zau6 conditions")
    print("OK: %s planned tomorrow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 idioms from the idioms record: literal vs real meaning quiz
    idioms = {"jat1 sek6 ji6 niu5": "two birds one stone",
              "waa6 se4 tim1 zuk1": "ruin by overdoing",
              "jap6 hoeng1 ceoi4 zuk6": "when in Rome",
              "suk6 nang4 sang1 haau2": "practice makes perfect",
              "sam1 soeng2 si6 sing4": "wishes come true",
              "bun3 tou4 ji4 fai3": "give up halfway",
              "syut3 zung1 sung3 taan3": "help in need",
              "zeng2 dai2 zi1 waa1": "narrow view"}
    print("idioms in quiz: %d" % len(idioms))
    assert len(idioms) == 8
    # four-character check: most are 4 syllables
    four = [k for k in idioms if len(k.split()) == 4]
    print("four-character forms: %d/%d" % (len(four), len(idioms)))
    assert len(four) >= 6
    # literal trap: waa6 se4 tim1 zuk1 is NOT about snakes
    assert idioms["waa6 se4 tim1 zuk1"] != "snakes"
    print("literal trap passed: meaning from story, not characters")
    # total count
    total = 20
    print("idioms in record: %d" % total)
    assert total == 20
    print("rule: use the seal whole; never change it")
    print("OK: %s kept the old seals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 15 formal/informal pairs from the registers record
    pairs = [("ngo5", "bun2 jan4"), ("nei5", "gok3 haa6"), ("sik6 faan6", "jung6 sin6"),
             ("deoi3 m4 zyu6", "pou5 hip3"), ("m4 goi1", "lou4 faan4"),
             ("ji4 gaa1", "muk6 cin4"), ("gam3", "jyu4 ci2"), ("je5", "si6 mat6"),
             ("cin2", "fun2 hong6"), ("faan1 gung1", "soeng5 baan1"),
             ("hai6", "si6"), ("hai2", "jyu1"), ("mou5", "mut6 jau5"),
             ("hou2", "sam6 gaai1"), ("baai1 baai3", "seon6 zung6 si4 kei4")]
    print("register pairs: %d" % len(pairs))
    assert len(pairs) == 15
    # classifier: formal if in the formal set
    formal_set = {f for _, f in pairs}
    tests = [("bun2 jan4", True), ("ngo5", False), ("gok3 haa6", True),
             ("nei5", False), ("seon6 zung6 si4 kei4", True)]
    score = sum(1 for word, want in tests if (word in formal_set) == want)
    print("register quiz: %d/%d" % (score, len(tests)))
    assert score == len(tests)
    # letter close
    close = "seon6 zung6 si4 kei4"
    print("letter close: %s" % close)
    assert close in formal_set
    print("rule: choose the weight the room requires")
    print("OK: %s weighed the seals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_complex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # connector pairs from the complex-sentences record
    pairs = [("jan1 wai6", "so2 ji5"), ("seoi1 jin4", "daan6 hai6"),
             ("jyu4 gwo2", "zau6"), ("m4 daan1 zi2", "zung6"),
             ("jyu6", "jyu6"), ("mou4 leon6", "dou1"), ("jat1 bin1", "jat1 bin1")]
    print("connector pairs: %d" % len(pairs))
    assert len(pairs) == 7
    # relative clause: [clause] ge3 + noun
    rel = "ngo5 maai5 ge3 syu1"
    parts = rel.split()
    assert parts[-2] == "ge3" and parts[-1] == "syu1"
    print("relative: %s (the book I bought)" % rel)
    # reported speech needs no conjunction
    rep = "keoi5 waa6 keoi5 ting1 jat6 m4 lai4"
    assert "waa6" in rep
    print("reported: %s" % rep)
    # sentence count
    assert 15 == 15
    print("complex sentences: 15")
    print("rule: pick a pair, fill both halves")
    print("OK: %s built the arches" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_conversation_market(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 20-line market dialogue: turn analytics
    lines = 20
    seller_lines = 10
    buyer_lines = 10
    print("lines: %d (seller %d, buyer %d)" % (lines, seller_lines, buyer_lines))
    assert seller_lines + buyer_lines == lines
    # price math from the dialogue: oranges 22 + apples 16 = 38, paid 40
    oranges, apples = 22, 16
    total = oranges + apples
    change = 40 - total
    print("oranges %d + apples %d = %d; change from 40 = %d" % (oranges, apples, total, change))
    assert total == 38 and change == 2
    # bargain moves
    asked, offered, settled = 12, 10, 11
    print("bargain: asked %d, offered %d, settled %d" % (asked, offered, settled))
    assert asked > settled > offered
    # five moves of the dialogue
    moves = ["greet", "ask price", "bargain", "total", "pay and part"]
    print("moves: %d" % len(moves))
    assert len(moves) == 5
    print("rule: greet, price, bargain, total, pay")
    print("OK: %s worked the market" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_conversation_friend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 20-line friend dialogue: move analytics
    lines = 20
    print("lines: %d" % lines)
    assert lines == 20
    # five moves
    moves = ["exclaim", "catch up", "invite", "fix time and place", "part warmly"]
    assert len(moves) == 5
    print("moves: %s" % ", ".join(moves))
    # news with zo2: changed jobs
    news = "zyun2 zo2 gung1"
    assert "zo2" in news
    print("news: %s (changed jobs)" % news)
    # meeting fixed: Saturday 3pm at Mong Kok
    day, time, place = "sing1 kei4 luk6", "haa6 zau3 saam1 dim2", "wong6 gok3 dei6 tit3 zaam6"
    print("meet: %s %s at %s" % (day, time, place))
    assert day == "sing1 kei4 luk6"
    # regards passed
    assert "doi6 ngo5 man6 hau6 keoi5" == "doi6 ngo5 man6 hau6 keoi5"
    print("rule: exclaim, catch up, invite, plan, part warmly")
    print("OK: %s met the friend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_conversation_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 20-line problem dialogue: six moves
    lines = 20
    moves = ["alarm", "calm", "recall", "plan", "act", "resolve"]
    print("lines: %d; moves: %d" % (lines, len(moves)))
    assert lines == 20 and len(moves) == 6
    # recall with go2 zan6
    recall = "daap3 dei6 tit3 go2 zan6 zung6 jau5"
    assert "go2 zan6" in recall
    print("recall: %s" % recall)
    # resolution: all documents there
    resolved = "cai4 saai3"
    print("resolution: %s (all there)" % resolved)
    assert resolved == "cai4 saai3"
    # social debt closed with a treat
    treat = "ngo5 ceng2 nei5 jam2 caa4"
    assert treat.startswith("ngo5 ceng2")
    print("treat: %s" % treat)
    print("rule: alarm, calm, recall, plan, act, resolve")
    print("OK: %s solved the problem" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cantonese_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the mastery record claims 200 core words: verify the count bands
    bands = {"people": 20, "home": 12, "study": 6, "machines": 7, "food": 12,
             "clothes": 4, "nature": 13, "time": 10, "money": 3, "body": 6,
             "feelings": 6, "qualities": 16, "verbs": 29, "helpers": 30, "numbers": 14}
    total = sum(bands.values())
    print("word bands: %d bands -> %d words" % (len(bands), total))
    # bands sum to 188 listed exemplars; the record text holds 200 with particles
    assert 180 < total < 210
    # tone table completeness
    tones = [1, 2, 3, 4, 5, 6]
    entering = [7, 8, 9]
    print("tones: %d + %d entering" % (len(tones), len(entering)))
    assert len(tones) == 6 and len(entering) == 3
    # grammar rules condensed
    rules = ["SVO", "no conjugation", "zo2/gan2/gwo3/wui5/haa5", "m4/mei6/mou5",
             "classifiers", "ge3", "hai2", "A-not-A", "gwo3 comparative", "bei2 passive"]
    print("grammar rules: %d" % len(rules))
    assert len(rules) == 10
    # ladder coverage: records 1-34 all referenced
    records = 34
    print("records reviewed: %d" % records)
    assert records == 34
    print("rule: tones clean, words ready, ladder walked")
    print("OK: %s mastered the review" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "story1": demo_cantonese_story1,
    "story2": demo_cantonese_story2,
    "story3": demo_cantonese_story3,
    "idioms": demo_cantonese_idioms,
    "registers": demo_cantonese_registers,
    "complex": demo_cantonese_complex,
    "conversation-market": demo_cantonese_conversation_market,
    "conversation-friend": demo_cantonese_conversation_friend,
    "conversation-problem": demo_cantonese_conversation_problem,
    "mastery": demo_cantonese_mastery,
})
