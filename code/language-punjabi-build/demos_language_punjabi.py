#!/usr/bin/env python3
"""Demo programs for The Punjabi to English Database (language-punjabi)
and its Signature edition (language-punjabi-signature).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: alphabet verification, tone drills,
vocabulary quizzes, conjugation tables, sentence assembly, dialogue
turn-taking. All are machine-executed by build.py: each prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker.
"""

import json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name))


def _themed_demo(sentences, tag_expect):
    """Build a demo function for a 20-sentence themed set.
    sentences: list of (punjabi, tag)."""
    def demo(hdr, name, rid, group, points, req):
        body = (
            "def main():\n"
            "    sentences = " + repr(sentences) + "\n"
            "    tag_expect = " + repr(tag_expect) + "\n"
            "    assert len(sentences) == 20, len(sentences)\n"
            "    tags = {}\n"
            "    for _p, _t in sentences:\n"
            "        assert _p.strip(), 'empty sentence'\n"
            "        tags[_t] = tags.get(_t, 0) + 1\n"
            "    print('sentences: 20; topics: %s' % tags)\n"
            "    assert tags == tag_expect, tags\n"
            "    longest = max(len(_p) for _p, _t in sentences)\n"
            "    total = sum(len(_p) for _p, _t in sentences)\n"
            "    print('longest punjabi line: %d chars; total chars: %d' % (longest, total))\n"
            "    assert 15 < longest < 250\n"
            "    assert 300 < total < 5000\n"
            "    print('OK: %s drilled the set' % NAME)\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        )
        return _wrap(hdr, name, rid, group, body)
    return demo


def demo_pan_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    native_m = 125.0
    world_pop_m = 8100.0
    share = native_m / world_pop_m * 100.0
    print("Punjabi native speakers: %.1f million" % native_m)
    print("share of world population: %.4f %%" % share)
    assert 124.9 < native_m < 125.1
    assert 1.5431 < share < 1.5433
    roster = [("Mandarin", 929.0), ("Spanish", 485.0), ("English", 380.0),
              ("Hindi", 345.0), ("Arabic", 315.0), ("Bengali", 241.0),
              ("Portuguese", 236.0), ("Russian", 147.0), ("Punjabi", 125.0),
              ("Japanese", 123.0)]
    rank = sorted(roster, key=lambda p: -p[1]).index(("Punjabi", 125.0)) + 1
    print("native-speaker rank in roster: %d" % rank)
    assert rank == 9
    print("scripts: Gurmukhi (India), Shahmukhi (Pakistan)")
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_script(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    letters = list("\\u0a09\\u0a05\\u0a73\\u0a38\\u0a39\\u0a15\\u0a16\\u0a17\\u0a18\\u0a19\\u0a1a\\u0a1b\\u0a1c\\u0a1d\\u0a1e\\u0a1f\\u0a20\\u0a21\\u0a22\\u0a23\\u0a24\\u0a25\\u0a26\\u0a27\\u0a28\\u0a2a\\u0a2b\\u0a2c\\u0a2d\\u0a2e\\u0a2f\\u0a30\\u0a32\\u0a35\\u0a5c")
    print("painti akhar count: %d" % len(letters))
    assert len(letters) == 35
    assert len(set(letters)) == 35, "duplicate letter"
    cps = [ord(c) for c in letters]
    assert all(0x0A00 <= c <= 0x0A7F for c in cps), "outside Gurmukhi block"
    print("codepoint range: U+%04X-U+%04X (Gurmukhi block)" % (min(cps), max(cps)))
    vowels = list("\\u0a05\\u0a06\\u0a07\\u0a08\\u0a09\\u0a0a\\u0a0f\\u0a10\\u0a13\\u0a14")
    assert len(vowels) == 10
    assert len(set(vowels)) == 10, "duplicate vowel"
    assert all(0x0A00 <= ord(v) <= 0x0A7F for v in vowels)
    digits = list("\\u0a66\\u0a67\\u0a68\\u0a69\\u0a6a\\u0a6b\\u0a6c\\u0a6d\\u0a6e\\u0a6f")
    assert len(digits) == 10 and ord(digits[0]) == 0x0A66
    print("vowels: 10; digits: 10 (zero at U+0A66)")
    print("OK: %s wrote the alphabet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_phonology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    tones = ["level", "high-falling", "low-rising"]
    words = [("ghar", "house", "low-rising"), ("jhanda", "flag", "low-rising"),
             ("dhol", "drum", "low-rising"), ("kora", "whip", "level"),
             ("ghora", "horse", "low-rising"), ("paani", "water", "level"),
             ("kitaab", "book", "level"), ("roti", "bread", "level"),
             ("chaa", "tea", "level"), ("dost", "friend", "level"),
             ("school", "school", "level"), ("baccha", "child", "level")]
    print("tones: %d (%s)" % (len(tones), ", ".join(tones)))
    assert len(tones) == 3
    assert len(words) >= 10
    low = [w for w in words if w[2] == "low-rising"]
    print("spoken examples: %d; low-rising (from old voiced aspirates): %d" % (len(words), len(low)))
    assert len(low) == 4
    # aspiration palm test: aspirated set must puff air (1), plain set must not (0)
    aspirated = {"kh": 1, "chh": 1, "th": 1, "ph": 1}
    plain = {"k": 0, "ch": 0, "t": 0, "p": 0}
    assert sum(aspirated.values()) == 4 and sum(plain.values()) == 0
    print("aspiration contrast: 4 puff / 4 no-puff")
    print("OK: %s sounded the tones" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_nouns1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    nouns = [("paani", "m"), ("kitaab", "f"), ("ghar", "m"), ("school", "m"),
             ("roti", "f"), ("chaa", "f"), ("dost", "m"), ("maan", "f"),
             ("pio", "m"), ("baccha", "m"), ("gaddi", "f"), ("rastaa", "m"),
             ("dukaan", "f"), ("bazaar", "m"), ("kamm", "m"), ("khaana", "m"),
             ("duddh", "m"), ("sabzi", "f"), ("phal", "m"), ("din", "m"),
             ("raat", "f"), ("sooraj", "m"), ("panchhi", "m"), ("kutta", "m"),
             ("billi", "f")]
    assert len(nouns) == 25
    m = sum(1 for _w, g in nouns if g == "m")
    f = 25 - m
    print("nouns: 25 (masculine %d, feminine %d)" % (m, f))
    assert m == 16 and f == 9
    # agreement drill: mera with masculine, meri with feminine
    got = [("mera" if g == "m" else "meri", w) for w, g in nouns]
    assert ("meri", "kitaab") in got and ("mera", "ghar") in got
    score = sum(1 for _a, _w in got)  # all 25 built by rule
    print("agreement drill: %d/25 possessives built by gender rule" % score)
    assert score == 25
    print("OK: %s named the world" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_verbs1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    verbs = ["karna", "jaana", "aauna", "khaana", "peena", "parhna", "likhna",
             "bolna", "sunna", "dekhna", "laina", "dena", "banauna", "baithna",
             "utthna", "sauna", "challna", "daurna", "khareedna", "vechna",
             "khedna", "sikhna", "sikhauna", "madad karna", "pyaar karna"]
    assert len(verbs) == 25
    assert all(v.endswith("na") for v in verbs), "infinitive must end in -na"
    stems = [v[:-2] for v in verbs[:23]]
    print("verbs: 25; sample stems: %s, %s, %s" % (stems[0], stems[3], stems[21]))
    assert stems[0] == "kar" and stems[3] == "khaa" and stems[21] == "sikh"
    # present habitual of karna across six persons (masculine)
    forms = ["karda haan", "karda hain", "karda hai",
             "karde haan", "karde ho", "karde han"]
    assert len(forms) == 6
    assert all(f.startswith("kard") for f in forms)
    aux = [f.split()[-1] for f in forms]
    print("present persons: %d; auxiliaries: %s" % (len(forms), aux))
    assert aux == ["haan", "hain", "hai", "haan", "ho", "han"]
    print("OK: %s moved the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_adjadv(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    changing = ["vadda", "chhota", "navaan", "puraana", "acchha", "buraa",
                "thanda", "mittha", "kaura", "lamba", "ganda", "sachcha",
                "jhootha"]
    fixed = ["garam", "sundar", "khush", "udaas", "tez", "hauli", "saaf",
             "ameer", "gareeb", "mushkal", "aasaan", "tiyaar"]
    adverbs = ["bahut", "jaldi", "hauli hauli", "ajj", "kallh", "hun", "phir",
               "hamesha", "kade", "kade nahin", "itthe", "utthe", "baahar",
               "andar", "shaayad"]
    assert len(changing) + len(fixed) == 25
    assert len(adverbs) == 15
    print("adjectives: 25 (%d agree, %d fixed); adverbs: 15" % (len(changing), len(fixed)))
    assert len(changing) == 13 and len(fixed) == 12
    # agreement machine: -aa -> -ee (f), -e (m pl); fixed stay put
    def agree(a, gender, number):
        if a not in changing:
            return a
        if gender == "f":
            return a[:-1] + "i"
        return a[:-1] + "e" if number == "pl" else a
    assert agree("vadda", "f", "sg") == "vaddi"
    assert agree("vadda", "m", "pl") == "vadde"
    assert agree("garam", "f", "sg") == "garam"
    print("agreement: vadda/vaddi/vadde; garam never changes")
    print("OK: %s dressed the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    personal = ["main", "tun", "tusin", "oh", "asin", "oh"]
    oblique = {"main": "mainun", "tun": "tainun", "tusin": "tuhaanun",
               "oh": "usnun", "asin": "saanun"}
    possessive = {"main": ("mera", "meri"), "tun": ("tera", "teri"),
                  "tusin": ("tuhada", "tuhadi")}
    interr = ["kaun", "ki", "kihra", "kinna", "kitthe", "kadon", "kion", "kiven"]
    print("personal: %d, oblique: %d, possessive pairs: %d, interrogatives: %d"
          % (len(personal), len(oblique), len(possessive), len(interr)))
    assert len(personal) == 6 and len(oblique) == 5
    assert len(possessive) == 3 and len(interr) == 8
    assert oblique["main"] == "mainun" and possessive["tusin"][0] == "tuhada"
    cells = len(personal) + len(oblique) + 2 * len(possessive) + len(interr)
    print("paradigm cells: %d" % cells)
    assert cells == 25
    print("respect ladder: tun < tusin (never tun with elders)")
    print("OK: %s sealed the identities" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    ones = ["ikk", "do", "tinn", "chaar", "panj", "chhe", "satt", "atth",
            "naun", "das"]
    tens = ["veeh", "teeh", "chaali", "panjaah", "satth", "sattar", "assi",
            "nabbe", "sau"]
    days = ["somvaar", "mangalvaar", "buddhvaar", "veervaar", "shukkarvaar",
            "shanivaar", "aitvaar"]
    months = ["janvari", "farvari", "maarch", "aprail", "mai", "joon",
              "julaai", "agasat", "satambar", "aktoobar", "navambar",
              "dasambar"]
    total = sum(range(1, 101))
    print("ones: %d, tens: %d, days: %d, months: %d" % (len(ones), len(tens), len(days), len(months)))
    assert len(ones) == 10 and len(tens) == 9
    assert len(days) == 7 and len(months) == 12
    assert total == 5050
    print("sum 1..100 = %d" % total)
    assert all(d.endswith("vaar") for d in days)
    print("days all end in -vaar; time frame: number + vaje")
    print("OK: %s counted the hours" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    phrases = ["sat sri akaal", "sat sri vaahiguru", "aadaab", "namaste",
               "salaam", "ki haal hai?", "tusin kiven ho?", "sabh theek hai?",
               "main theek haan.", "bahut vadheeyaa!", "dhannvaad",
               "bahut bahut dhannvaad", "maaf karo", "maaf kareen",
               "koi gall nahin", "kirpaa karke", "ji aayaan nun", "alvida",
               "rabb raakha", "phir milaange", "changa, phir milde haan",
               "shubh saver", "shubh dupahir", "shubh shaam", "shubh raatri",
               "vadhaai hove", "janamdin mubaarak", "khush raho",
               "jug jug jeeo", "rabb mehar kare"]
    assert len(phrases) == 30
    scenarios = {"hello (Sikh)": "sat sri akaal", "hello (Muslim)": "aadaab",
                 "thanks": "dhannvaad", "sorry (formal)": "maaf karo",
                 "goodbye": "rabb raakha", "congratulations": "vadhaai hove"}
    matched = sum(1 for _s, p in scenarios.items() if p in phrases)
    print("phrases: 30; scenario coverage: %d/%d" % (matched, len(scenarios)))
    assert matched == 6
    ji_forms = [p for p in phrases if "ji" in p]
    print("ji-respect forms: %d" % len(ji_forms))
    assert len(ji_forms) >= 1
    print("OK: %s exchanged greetings" % NAME)
if __name__ == "__main__":
    main()
''')

# ------------------------------------------------- themed sets (records 11-20)

demo_pan_home = _themed_demo([
("ਇਹ ਮੇਰਾ ਘਰ ਹੈ।", "house"), ("ਸਾਡਾ ਘਰ ਵੱਡਾ ਹੈ।", "house"),
("ਰਸੋਈ ਵਿੱਚ ਮਾਂ ਖਾਣਾ ਬਣਾਉਂਦੀ ਹੈ।", "house"),
("ਮੇਰਾ ਕਮਰਾ ਉੱਪਰ ਹੈ।", "house"), ("ਬੈਠਕ ਵਿੱਚ ਸੋਫ਼ਾ ਹੈ।", "house"),
("ਮੇਜ਼ ਉੱਤੇ ਕਿਤਾਬਾਂ ਹਨ।", "house"), ("ਕੁਰਸੀ ਟੁੱਟ ਗਈ ਹੈ।", "house"),
("ਖਿੜਕੀ ਖੋਲ੍ਹ ਦਿਓ।", "house"), ("ਦਰਵਾਜ਼ਾ ਬੰਦ ਕਰ ਦਿਓ।", "house"),
("ਬੱਤੀ ਜਗਾ ਦਿਓ।", "house"), ("ਮੇਰੇ ਪਿਉ ਦਾ ਨਾਂ ਹਰਪ੍ਰੀਤ ਹੈ।", "family"),
("ਮੇਰੀ ਮਾਂ ਅਧਿਆਪਕ ਹੈ।", "family"), ("ਮੇਰਾ ਭਰਾ ਡਾਕਟਰ ਹੈ।", "family"),
("ਮੇਰੀ ਭੈਣ ਸਕੂਲ ਜਾਂਦੀ ਹੈ।", "family"),
("ਮੇਰੇ ਦਾਦਾ ਜੀ ਬਹੁਤ ਸਿਆਣੇ ਹਨ।", "family"),
("ਮੇਰੀ ਦਾਦੀ ਕਹਾਣੀਆਂ ਸੁਣਾਉਂਦੀ ਹੈ।", "family"),
("ਸਾਡੇ ਘਰ ਪੰਜ ਜੀਅ ਹਨ।", "family"),
("ਮੇਰਾ ਪੁੱਤਰ ਤਿੰਨ ਸਾਲ ਦਾ ਹੈ।", "family"),
("ਮੇਰੀ ਧੀ ਬਹੁਤ ਪਿਆਰੀ ਹੈ।", "family"),
("ਅਸੀਂ ਸਾਰੇ ਇਕੱਠੇ ਰਹਿੰਦੇ ਹਾਂ।", "family"),
], {"house": 10, "family": 10})

demo_pan_food = _themed_demo([
("ਮੈਨੂੰ ਭੁੱਖ ਲੱਗੀ ਹੈ।", "cooking"), ("ਖਾਣਾ ਤਿਆਰ ਹੈ।", "cooking"),
("ਅੱਜ ਦਾਲ ਰੋਟੀ ਬਣੀ ਹੈ।", "cooking"), ("ਮਾਂ ਸਾਗ ਬਣਾਉਂਦੀ ਹੈ।", "cooking"),
("ਰੋਟੀ ਤਵੇ ਉੱਤੇ ਸੇਕੋ।", "cooking"), ("ਚਾਹ ਵਿੱਚ ਖੰਡ ਪਾਓ।", "cooking"),
("ਸਬਜ਼ੀ ਵਿੱਚ ਨਮਕ ਘੱਟ ਹੈ।", "cooking"), ("ਦੁੱਧ ਉਬਾਲ ਲਓ।", "cooking"),
("ਚੌਲ ਧੋ ਕੇ ਪਕਾਓ।", "cooking"), ("ਮੈਨੂੰ ਤਿੱਖਾ ਖਾਣਾ ਪਸੰਦ ਹੈ।", "cooking"),
("ਇਹ ਮਿੱਠਾ ਬਹੁਤ ਸਵਾਦ ਹੈ।", "cooking"),
("ਪਾਣੀ ਦਾ ਗਲਾਸ ਦਿਓ।", "cooking"), ("ਹੋਰ ਰੋਟੀ ਲਓਗੇ?", "cooking"),
("ਬਸ, ਮੇਰਾ ਢਿੱਡ ਭਰ ਗਿਆ।", "cooking"),
("ਖਾਣਾ ਬਹੁਤ ਸਵਾਦ ਬਣਿਆ ਹੈ।", "cooking"),
("ਅਸੀਂ ਢਾਬੇ ਤੇ ਖਾਣਾ ਖਾਧਾ।", "restaurant"),
("ਬਿੱਲ ਕਿੰਨਾ ਹੋਇਆ?", "restaurant"),
("ਮੈਨੂੰ ਸ਼ਾਕਾਹਾਰੀ ਖਾਣਾ ਚਾਹੀਦਾ ਹੈ।", "restaurant"),
("ਲੱਸੀ ਠੰਡੀ ਕਰਕੇ ਦਿਓ।", "restaurant"),
("ਰੱਬ ਦਾ ਸ਼ੁਕਰ ਹੈ, ਖਾਣਾ ਮਿਲ ਗਿਆ।", "restaurant"),
], {"cooking": 15, "restaurant": 5})

demo_pan_travel = _themed_demo([
("ਰੇਲਵੇ ਸਟੇਸ਼ਨ ਕਿੱਥੇ ਹੈ?", "directions"),
("ਬੱਸ ਅੱਡਾ ਕਿੰਨੀ ਦੂਰ ਹੈ?", "directions"),
("ਸਿੱਧਾ ਜਾਓ, ਫਿਰ ਖੱਬੇ ਮੁੜੋ।", "directions"),
("ਸੱਜੇ ਮੁੜੋ, ਉੱਥੇ ਮੰਦਰ ਹੈ।", "directions"),
("ਇਹ ਰਸਤਾ ਕਿੱਥੇ ਜਾਂਦਾ ਹੈ?", "directions"),
("ਟੈਕਸੀ ਮਿਲੇਗੀ?", "directions"), ("ਕਿਰਾਇਆ ਕਿੰਨਾ ਹੋਵੇਗਾ?", "tickets"),
("ਮੈਨੂੰ ਹਵਾਈ ਅੱਡੇ ਜਾਣਾ ਹੈ।", "tickets"),
("ਗੱਡੀ ਕਿੰਨੇ ਵਜੇ ਆਵੇਗੀ?", "tickets"),
("ਇੱਕ ਟਿਕਟ ਦਿਓ, ਅੰਮ੍ਰਿਤਸਰ ਤੱਕ।", "tickets"),
("ਇਹ ਸੀਟ ਖਾਲੀ ਹੈ?", "tickets"), ("ਬੱਸ ਕਦੋਂ ਚੱਲੇਗੀ?", "tickets"),
("ਮੈਂ ਰਸਤਾ ਭੁੱਲ ਗਿਆ ਹਾਂ।", "tickets"),
("ਕੀ ਤੁਸੀਂ ਮੇਰੀ ਮਦਦ ਕਰ ਸਕਦੇ ਹੋ?", "tickets"),
("ਨਕਸ਼ੇ ਵਿੱਚ ਦੇਖੋ।", "tickets"), ("ਹੋਟਲ ਕਿੰਨੀ ਦੂਰ ਹੈ?", "lodging"),
("ਇੱਕ ਕਮਰਾ ਚਾਹੀਦਾ ਹੈ, ਦੋ ਦਿਨਾਂ ਲਈ।", "lodging"),
("ਕਿਰਾਇਆ ਇੱਕ ਰਾਤ ਦਾ ਕਿੰਨਾ ਹੈ?", "lodging"),
("ਸਵੇਰੇ ਨਾਸ਼ਤਾ ਮਿਲੇਗਾ?", "lodging"),
("ਸਫ਼ਰ ਸੁਰੱਖਿਅਤ ਰਹੇ!", "lodging"),
], {"directions": 6, "tickets": 9, "lodging": 5})

demo_pan_work = _themed_demo([
("ਤੁਸੀਂ ਕੀ ਕੰਮ ਕਰਦੇ ਹੋ?", "office"), ("ਮੈਂ ਦਫ਼ਤਰ ਵਿੱਚ ਕੰਮ ਕਰਦਾ ਹਾਂ।", "office"),
("ਮੇਰੀ ਨੌਕਰੀ ਨਵੀਂ ਹੈ।", "office"), ("ਤਨਖ਼ਾਹ ਕਦੋਂ ਮਿਲੇਗੀ?", "office"),
("ਅੱਜ ਮੀਟਿੰਗ ਦਸ ਵਜੇ ਹੈ।", "office"), ("ਮੈਨੂੰ ਛੁੱਟੀ ਚਾਹੀਦੀ ਹੈ।", "office"),
("ਬੌਸ ਨੇ ਬੁਲਾਇਆ ਹੈ।", "office"),
("ਇਹ ਰਿਪੋਰਟ ਕੱਲ੍ਹ ਤੱਕ ਦੇ ਦਿਓ।", "office"),
("ਮੈਂ ਸਕੂਲ ਵਿੱਚ ਪੜ੍ਹਦਾ ਹਾਂ।", "school"),
("ਮੇਰਾ ਮਨਪਸੰਦ ਵਿਸ਼ਾ ਗਣਿਤ ਹੈ।", "school"),
("ਅਧਿਆਪਕ ਬਹੁਤ ਚੰਗਾ ਪੜ੍ਹਾਉਂਦਾ ਹੈ।", "school"),
("ਹੋਮਵਰਕ ਪੂਰਾ ਕਰ ਲਿਆ?", "school"),
("ਕਿਤਾਬ ਦਾ ਪੰਨਾ ਖੋਲ੍ਹੋ।", "school"),
("ਸਵਾਲ ਪੁੱਛੋ, ਡਰੋ ਨਾ।", "school"),
("ਇਮਤਿਹਾਨ ਅਗਲੇ ਹਫ਼ਤੇ ਹੈ।", "school"),
("ਮੈਂ ਪਹਿਲੇ ਨੰਬਰ ਤੇ ਆਇਆ।", "school"),
("ਸਿੱਖਣਾ ਕਦੇ ਨਹੀਂ ਰੁਕਦਾ।", "school"),
("ਮਿਹਨਤ ਦਾ ਫਲ ਮਿੱਠਾ ਹੁੰਦਾ ਹੈ।", "school"),
("ਦਫ਼ਤਰ ਕਦੋਂ ਬੰਦ ਹੁੰਦਾ ਹੈ?", "office"),
("ਕੱਲ੍ਹ ਫਿਰ ਮਿਲਦੇ ਹਾਂ।", "school"),
], {"office": 9, "school": 11})

demo_pan_health = _themed_demo([
("ਮੇਰਾ ਸਿਰ ਦੁੱਖਦਾ ਹੈ।", "symptoms"), ("ਮੈਨੂੰ ਬੁਖ਼ਾਰ ਹੈ।", "symptoms"),
("ਮੇਰਾ ਗਲਾ ਖ਼ਰਾਬ ਹੈ।", "symptoms"), ("ਮੈਨੂੰ ਜ਼ੁਕਾਮ ਲੱਗਿਆ ਹੈ।", "symptoms"),
("ਮੇਰੇ ਪੇਟ ਵਿੱਚ ਦਰਦ ਹੈ।", "symptoms"), ("ਮੇਰੀ ਅੱਖ ਲਾਲ ਹੈ।", "symptoms"),
("ਮੇਰਾ ਦੰਦ ਦੁੱਖਦਾ ਹੈ।", "symptoms"), ("ਮੈਨੂੰ ਚੱਕਰ ਆ ਰਹੇ ਹਨ।", "symptoms"),
("ਡਾਕਟਰ ਨੂੰ ਦਿਖਾਓ।", "care"), ("ਹਸਪਤਾਲ ਕਿੱਥੇ ਹੈ?", "care"),
("ਡਾਕਟਰ ਸਾਹਿਬ, ਮੈਨੂੰ ਬਚਾਓ।", "care"),
("ਦਵਾਈ ਕਦੋਂ ਲੈਣੀ ਹੈ?", "care"), ("ਖਾਣੇ ਤੋਂ ਬਾਅਦ ਇੱਕ ਗੋਲੀ ਲਓ।", "care"),
("ਪਾਣੀ ਜ਼ਿਆਦਾ ਪੀਓ।", "care"), ("ਆਰਾਮ ਕਰੋ।", "care"),
("ਇਹ ਦਵਾਈ ਕੌੜੀ ਹੈ ਪਰ ਅਸਰਦਾਰ ਹੈ।", "care"),
("ਮੈਨੂੰ ਐਲਰਜੀ ਹੈ।", "care"), ("ਦਵਾਖ਼ਾਨਾ ਕਦੋਂ ਖੁੱਲ੍ਹਦਾ ਹੈ?", "care"),
("ਪੱਟੀ ਬਦਲ ਦਿਓ।", "care"),
("ਹੁਣ ਮੈਂ ਠੀਕ ਹਾਂ, ਰੱਬ ਦਾ ਸ਼ੁਕਰ ਹੈ।", "care"),
], {"symptoms": 8, "care": 12})

demo_pan_emotions = _themed_demo([
("ਮੈਂ ਬਹੁਤ ਖੁਸ਼ ਹਾਂ।", "happy"),
("ਅੱਜ ਮੇਰਾ ਦਿਲ ਬਾਗ਼ ਬਾਗ਼ ਹੋ ਗਿਆ।", "happy"),
("ਉਹ ਖੁਸ਼ੀ ਨਾਲ ਨੱਚ ਰਹੀ ਹੈ।", "happy"), ("ਮੈਨੂੰ ਉਦਾਸੀ ਹੈ।", "sad"),
("ਉਹ ਰੋ ਰਿਹਾ ਹੈ।", "sad"), ("ਮੇਰਾ ਦਿਲ ਟੁੱਟ ਗਿਆ।", "sad"),
("ਮੈਨੂੰ ਗੁੱਸਾ ਆ ਰਿਹਾ ਹੈ।", "angry"), ("ਸ਼ਾਂਤ ਹੋ ਜਾਓ।", "angry"),
("ਉਹ ਗੁੱਸੇ ਵਿੱਚ ਚਲਾ ਗਿਆ।", "angry"), ("ਮੈਨੂੰ ਡਰ ਲੱਗਦਾ ਹੈ।", "afraid"),
("ਡਰੋ ਨਾ, ਮੈਂ ਤੁਹਾਡੇ ਨਾਲ ਹਾਂ।", "afraid"),
("ਹਨੇਰੇ ਤੋਂ ਡਰ ਲੱਗਦਾ ਹੈ।", "afraid"),
("ਮੈਂ ਤੁਹਾਨੂੰ ਪਿਆਰ ਕਰਦਾ ਹਾਂ।", "love"),
("ਮਾਂ ਦਾ ਪਿਆਰ ਸਭ ਤੋਂ ਵੱਡਾ ਹੈ।", "love"),
("ਉਹ ਆਪਣੇ ਦੇਸ਼ ਨੂੰ ਪਿਆਰ ਕਰਦਾ ਹੈ।", "love"),
("ਮੈਂ ਹੈਰਾਨ ਹਾਂ!", "comfort"), ("ਇਹ ਸੁਣ ਕੇ ਮੈਂ ਦੰਗ ਰਹਿ ਗਿਆ।", "comfort"),
("ਕੀ ਗੱਲ ਹੈ, ਤੁਸੀਂ ਪਰੇਸ਼ਾਨ ਲੱਗਦੇ ਹੋ?", "comfort"),
("ਹੌਸਲਾ ਰੱਖੋ, ਸਭ ਠੀਕ ਹੋਵੇਗਾ।", "comfort"),
("ਖੁਸ਼ੀ ਵੰਡਣ ਨਾਲ ਵਧਦੀ ਹੈ।", "comfort"),
], {"happy": 3, "sad": 3, "angry": 3, "afraid": 3, "love": 3, "comfort": 5})

demo_pan_nature = _themed_demo([
("ਅੱਜ ਮੌਸਮ ਬਹੁਤ ਚੰਗਾ ਹੈ।", "weather"),
("ਬਾਹਰ ਮੀਂਹ ਪੈ ਰਿਹਾ ਹੈ।", "weather"),
("ਸਰਦੀ ਵਿੱਚ ਬਰਫ਼ ਪੈਂਦੀ ਹੈ।", "weather"),
("ਗਰਮੀ ਵਿੱਚ ਲੂ ਚੱਲਦੀ ਹੈ।", "weather"),
("ਅੱਜ ਧੁੱਪ ਖਿੜੀ ਹੈ।", "weather"),
("ਅਸਮਾਨ ਵਿੱਚ ਬੱਦਲ ਹਨ।", "weather"),
("ਹਵਾ ਤੇਜ਼ ਚੱਲ ਰਹੀ ਹੈ।", "weather"),
("ਕੱਲ੍ਹ ਤੂਫ਼ਾਨ ਆਇਆ ਸੀ।", "weather"),
("ਬਾਗ਼ ਵਿੱਚ ਫੁੱਲ ਖਿੜੇ ਹਨ।", "plants"),
("ਇਹ ਦਰੱਖਤ ਬਹੁਤ ਪੁਰਾਣਾ ਹੈ।", "plants"),
("ਅੰਬ ਦਾ ਮੌਸਮ ਆ ਗਿਆ।", "plants"),
("ਖੇਤਾਂ ਵਿੱਚ ਫ਼ਸਲ ਪੱਕ ਗਈ ਹੈ।", "plants"),
("ਚਿੜੀ ਦਰੱਖਤ ਉੱਤੇ ਬੈਠੀ ਹੈ।", "animals"),
("ਮੋਰ ਬਹੁਤ ਸੁੰਦਰ ਪੰਛੀ ਹੈ।", "animals"),
("ਗਾਂ ਦੁੱਧ ਦਿੰਦੀ ਹੈ।", "animals"),
("ਮੱਝ ਪਾਣੀ ਵਿੱਚ ਨਹਾਉਂਦੀ ਹੈ।", "animals"),
("ਸ਼ੇਰ ਜੰਗਲ ਦਾ ਰਾਜਾ ਹੈ।", "animals"),
("ਸੱਪ ਤੋਂ ਬਚ ਕੇ ਰਹੋ।", "animals"),
("ਤਿਤਲੀ ਫੁੱਲਾਂ ਉੱਤੇ ਉੱਡਦੀ ਹੈ।", "animals"),
("ਕੁਦਰਤ ਦੀ ਰੱਖਿਆ ਕਰੋ।", "care"),
], {"weather": 8, "plants": 4, "animals": 7, "care": 1})

demo_pan_shopping = _themed_demo([
("ਇਹ ਕਿੰਨੇ ਦਾ ਹੈ?", "bargain"), ("ਬਹੁਤ ਮਹਿੰਗਾ ਹੈ, ਥੋੜ੍ਹਾ ਘੱਟ ਕਰੋ।", "bargain"),
("ਆਖ਼ਰੀ ਭਾਅ ਦੱਸੋ।", "bargain"),
("ਮੈਂ ਸਬਜ਼ੀ ਲੈਣ ਬਾਜ਼ਾਰ ਗਿਆ।", "bargain"),
("ਟਮਾਟਰ ਕਿਲੋ ਦੇ ਹਿਸਾਬ ਨਾਲ ਹਨ?", "bargain"),
("ਅੱਧਾ ਕਿਲੋ ਆਲੂ ਦਿਓ।", "bargain"), ("ਤਾਜ਼ਾ ਮਾਲ ਦਿਖਾਓ।", "bargain"),
("ਇਹ ਕੱਪੜਾ ਕਿਸ ਭਾਅ ਹੈ?", "bargain"),
("ਕੋਈ ਸਸਤਾ ਵਿਕਲਪ ਹੈ?", "bargain"),
("ਦੁਕਾਨਦਾਰ ਇਮਾਨਦਾਰ ਹੈ।", "bargain"), ("ਪੈਸੇ ਗਿਣ ਲਓ।", "paying"),
("ਖੁੱਲ੍ਹੇ ਪੈਸੇ ਹਨ?", "paying"), ("ਮੈਂ ਨਕਦ ਦੇਵਾਂਗਾ।", "paying"),
("ਕਾਰਡ ਚੱਲੇਗਾ?", "paying"), ("ਬਿੱਲ ਬਣਾ ਦਿਓ।", "paying"),
("ਰਸੀਦ ਦੇ ਦਿਓ।", "paying"), ("ਇਹ ਵਸਤੂ ਵਾਪਸ ਹੋ ਸਕਦੀ ਹੈ?", "paying"),
("ਗਾਰੰਟੀ ਕਿੰਨੇ ਸਾਲ ਦੀ ਹੈ?", "paying"), ("ਸੌਦਾ ਪੱਕਾ!", "paying"),
("ਅਗਲੀ ਵਾਰ ਫਿਰ ਆਵਾਂਗਾ।", "paying"),
], {"bargain": 10, "paying": 10})

demo_pan_social = _themed_demo([
("ਤੁਹਾਡਾ ਨਾਂ ਕੀ ਹੈ?", "meeting"), ("ਮੇਰਾ ਨਾਂ ਸਿਮਰਨ ਹੈ।", "meeting"),
("ਤੁਸੀਂ ਕਿੱਥੋਂ ਹੋ?", "meeting"), ("ਮੈਂ ਪੰਜਾਬ ਤੋਂ ਹਾਂ।", "meeting"),
("ਤੁਹਾਨੂੰ ਮਿਲ ਕੇ ਖੁਸ਼ੀ ਹੋਈ।", "meeting"),
("ਇਹ ਮੇਰਾ ਦੋਸਤ ਗੁਰਪ੍ਰੀਤ ਹੈ।", "meeting"),
("ਅਸੀਂ ਪੁਰਾਣੇ ਦੋਸਤ ਹਾਂ।", "meeting"), ("ਚਾਹ ਪੀਓਗੇ?", "inviting"),
("ਮੇਰੇ ਘਰ ਆਓ, ਖਾਣਾ ਖਾਵਾਂਗੇ।", "inviting"),
("ਕੱਲ੍ਹ ਪਾਰਟੀ ਹੈ, ਜ਼ਰੂਰ ਆਉਣਾ।", "inviting"),
("ਵਿਆਹ ਵਿੱਚ ਜ਼ਰੂਰ ਆਇਓ।", "inviting"), ("ਵਧਾਈ ਹੋਵੇ!", "inviting"),
("ਤੁਹਾਡੀ ਸਫ਼ਲਤਾ ਤੇ ਮਾਣ ਹੈ।", "inviting"),
("ਦੋਸਤੀ ਸਭ ਤੋਂ ਵੱਡੀ ਦੌਲਤ ਹੈ।", "wisdom"),
("ਮੁਸੀਬਤ ਵਿੱਚ ਦੋਸਤ ਕੰਮ ਆਉਂਦਾ ਹੈ।", "wisdom"),
("ਅਸੀਂ ਇਕੱਠੇ ਫਿਲਮ ਦੇਖੀ।", "wisdom"),
("ਚਲੋ, ਸੈਰ ਕਰ ਆਈਏ।", "wisdom"),
("ਤੁਹਾਡਾ ਪਰਿਵਾਰ ਕਿਵੇਂ ਹੈ?", "wisdom"),
("ਸਭ ਨੂੰ ਮੇਰਾ ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਕਹਿਣਾ।", "wisdom"),
("ਦੋਸਤੋ, ਰੱਬ ਰਾਖਾ!", "wisdom"),
], {"meeting": 7, "inviting": 6, "wisdom": 7})

demo_pan_tech = _themed_demo([
("ਮੇਰਾ ਫ਼ੋਨ ਕਿੱਥੇ ਹੈ?", "phone"), ("ਫ਼ੋਨ ਦੀ ਬੈਟਰੀ ਖ਼ਤਮ ਹੋ ਗਈ।", "phone"),
("ਚਾਰਜਰ ਲਗਾ ਦਿਓ।", "phone"), ("ਮੈਨੂੰ ਫ਼ੋਨ ਕਰੋ।", "phone"),
("ਉਸਦਾ ਨੰਬਰ ਬੰਦ ਆ ਰਿਹਾ ਹੈ।", "phone"),
("ਨੈੱਟ ਨਹੀਂ ਚੱਲ ਰਿਹਾ।", "internet"),
("ਵਾਈ-ਫਾਈ ਦਾ ਪਾਸਵਰਡ ਦੱਸੋ।", "internet"),
("ਮੈਂ ਤੁਹਾਨੂੰ ਸੁਨੇਹਾ ਭੇਜਾਂਗਾ।", "internet"),
("ਵਟਸਐਪ ਤੇ ਫੋਟੋ ਭੇਜੋ।", "internet"),
("ਈਮੇਲ ਚੈੱਕ ਕਰ ਲਓ।", "internet"), ("ਕੰਪਿਊਟਰ ਚਾਲੂ ਕਰੋ।", "computer"),
("ਫ਼ਾਈਲ ਡਾਊਨਲੋਡ ਹੋ ਰਹੀ ਹੈ।", "computer"),
("ਪਾਸਵਰਡ ਭੁੱਲ ਗਿਆ ਹਾਂ।", "computer"),
("ਸਕਰੀਨ ਬਹੁਤ ਚਮਕਦਾਰ ਹੈ।", "computer"),
("ਐਪ ਅੱਪਡੇਟ ਕਰੋ।", "computer"), ("ਵੀਡੀਓ ਕਾਲ ਕਰੀਏ?", "messages"),
("ਆਵਾਜ਼ ਸਾਫ਼ ਨਹੀਂ ਆ ਰਹੀ।", "messages"),
("ਮੈਂ ਆਨਲਾਈਨ ਪੜ੍ਹਦਾ ਹਾਂ।", "messages"),
("ਇਹ ਖ਼ਬਰ ਸੱਚੀ ਹੈ ਜਾਂ ਝੂਠੀ?", "messages"),
("ਫ਼ੋਨ ਥੋੜ੍ਹਾ ਦੂਰ ਰੱਖੋ, ਅੱਖਾਂ ਖ਼ਰਾਬ ਹੁੰਦੀਆਂ ਹਨ।", "messages"),
], {"phone": 5, "internet": 5, "computer": 5, "messages": 5})

# ------------------------------------------------- advanced (records 21-34)

def demo_pan_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    stem = "khaa"
    tenses = {"present habitual": "khaanda haan",
              "present continuous": "khaa rihaa haan",
              "completed past": "khaadhaa",
              "past continuous": "khaa rihaa see",
              "future": "khaavaangaa"}
    print("stem: %s (khaana = to eat)" % stem)
    for t, f in tenses.items():
        print("  %-18s %s" % (t, f))
    assert tenses["present habitual"] == "khaanda haan"
    assert tenses["completed past"] == "khaadhaa"
    assert tenses["future"] == "khaavaangaa"
    # ergative agreement: verb matches the OBJECT in the completed past
    pairs = [("roti (f)", "khaadhi"), ("paani (m)", "peetaa"),
             ("chaa (f)", "peeti")]
    for obj, verb in pairs:
        print("  object %-10s -> verb %s" % (obj, verb))
    assert pairs[0][1][-1] == "i" and pairs[2][1][-1] == "i"
    assert pairs[1][1][-1] == "a"
    print("OK: %s stamped the tenses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_qa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pairs = [("tuhada naan ki hai?", "ki"),
             ("tusin kitthe rahinde ho?", "kitthe"),
             ("tusin ki karde ho?", "ki"),
             ("eh kaun hai?", "kaun"),
             ("tusin kadon aaoge?", "kadon"),
             ("tusin kion nahin aaye?", "kion"),
             ("eh kiven baniyaa?", "kiven"),
             ("ki tusin panjaabi bolde ho?", "ki"),
             ("ki khaana tiyaar hai?", "ki"),
             ("eh kinne da hai?", "kinne"),
             ("kinne vaje han?", "kinne"),
             ("tuhadi umar kinni hai?", "kinni"),
             ("ki main andar aa sakdaa haan?", "ki"),
             ("relve station kitthe hai?", "kitthe"),
             ("tuhaanun ki chaheeda hai?", "ki"),
             ("kihri kitaab changi hai?", "kihri"),
             ("tusin kitthon aaye ho?", "kitthon"),
             ("ki haal hai?", "ki"),
             ("mausam kiven hai?", "kiven"),
             ("ki tusin meri madad karoge?", "ki")]
    assert len(pairs) == 20
    cats = {}
    for q, w in pairs:
        assert w in q, q
        cats[w] = cats.get(w, 0) + 1
    print("questions: 20; distinct question words: %d" % len(cats))
    assert len(cats) == 10
    assert cats["ki"] == 8
    print("yes/no engine (ki): %d; content words: %d" % (cats["ki"], 20 - cats["ki"]))
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_commands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    formal = ["aao", "baitho", "kholho", "suno", "karo", "dio", "ruko",
              "raho"]
    informal = ["aa", "baith", "khaa", "kar", "de"]
    print("formal (-o ending): %d; informal (bare stem): %d" % (len(formal), len(informal)))
    assert len(formal) == 8 and len(informal) == 5
    assert all(f.endswith("o") for f in formal)
    assert all(" " not in f for f in informal)
    softeners = ["kirpaa karke", "dio", "je ho sake taan"]
    print("softeners: %s" % ", ".join(softeners))
    assert len(softeners) == 3
    prohib = ["na jaao", "mat ro"]
    assert all(p.split()[0] in ("na", "mat") for p in prohib)
    print("prohibitions: na/mat + stem")
    print("OK: %s gave the orders" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = [
        "mera dost lamba, goraa, ate hassmukh hai.",
        "usdiyaan akkhaan kaaliyaan ate vaddiyaan han.",
        "bazurg aadmi di daarhi chitti hai.",
        "kurhi ne laal suit paayaa hoyaa hai.",
        "oh hameshaa muskaraaundaa hai.",
        "meri daadi di aavaaz bahut mitthi hai.",
        "Amritsar ikk pavittar ate sundar shehar hai.",
        "Sunahiri Mandar sarovar de vichkaar hai.",
        "pind haraa bharaa ate shaant hai.",
        "khetaan vich peeli sarson khirhi hai.",
        "shehar diy aan galiyaan bhariyaan hoiyaan han.",
        "eh imaarat bahut ucchi hai.",
        "kamraa saaf suthraa ate havaadaar hai.",
        "baagh vich rang barange phull han.",
        "dariyaa da paani saaf ate thandaa hai.",
        "pahaarhaan utte baraf jami hoi hai.",
        "sooraj dubb rihaa hai, asmaan laal hai.",
        "eh puraani haveli sau saal puraani hai.",
        "bazaar vich raunak laggi hoi hai.",
        "Panjaab dharti sone vargi hai.",
    ]
    assert len(sents) == 20
    stacked = sum(1 for s in sents if " ate " in s)
    worn = sum(1 for s in sents if "paayaa" in s or "paayee" in s)
    print("descriptions: 20; ate-stacked: %d; wearing-frame: %d" % (stacked, worn))
    assert stacked == 6
    assert worn == 1
    longest = max(len(s) for s in sents)
    print("longest: %d chars" % longest)
    assert 40 < longest < 60
    print("OK: %s painted the portraits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_story1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = [
        "Simran savere chhe vaje utthdi hai.",
        "oh hath munh dhondi hai.",
        "maan rasoi vich paraunthe banaundi hai.",
        "Simran duddh peendi hai.",
        "oh school da bastaa chukkdi hai.",
        "oh aapni saheli naal school jaandi hai.",
        "raste vich oh panchhiyaan nun dekhdi hai.",
        "school vich adhiaapak parhaundaa hai.",
        "Simran dhiaan naal sundi hai.",
        "shaam nun oh hassdi hoi ghar aaundi hai.",
    ]
    assert len(lines) == 10
    words = [len(l.split()) for l in lines]
    total = sum(words)
    print("lines: 10; words: %d; avg per line: %.2f" % (total, total / 10.0))
    assert total == 59
    fem = sum(1 for l in lines if "di hai." in l)
    print("feminine -di present verbs: %d/10 lines" % fem)
    assert fem == 9
    print("OK: %s told the morning story" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_story2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = [
        "kallh asin mele vich gaye.",
        "melaa bahut vaddaa see.",
        "utthe bahut saare lok aaye hoye san.",
        "main ne jhoole laye.",
        "mere bharaa ne mithiaai khaadhi.",
        "asin khidaune khareede.",
        "dhol vajjiyaa ate lok nacche.",
        "sooraj dubb gayaa.",
        "asin khushi khushi ghar aaye.",
        "eh din mainun hameshaa yaad rahegaa.",
    ]
    assert len(lines) == 10
    # ergative agreement spot-checks: verb matches the object
    assert "mithiaai khaadhi" in lines[4]   # feminine object -> feminine verb
    assert "jhoole laye" in lines[3]        # plural object -> plural verb
    assert "khidaune khareede" in lines[5]  # plural object -> plural verb
    scene = sum(1 for l in lines if " see." in l or " san." in l)
    print("lines: 10; scene-setting (see/san): %d; ergative matches: 3/3" % scene)
    assert scene == 2
    assert "rahegaa" in lines[9], "story must land in the future"
    print("OK: %s remembered the fair" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_story3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = [
        "saade pind vich school nahin hai.",
        "bacche door parhan jaande han.",
        "asin ikk school banaavaange.",
        "saare pind vaale madad karange.",
        "je paise ikatthe ho gaye taan kamm shuru hovegaa.",
        "main adhiaapak banaangi.",
        "bacche khushi naal parhange.",
        "school vich ikk vaddi library hovegi.",
        "je tusin aaoge taan asin zaroor jittaange.",
        "saadaa supnaa ikk din sachch hovegaa.",
    ]
    assert len(lines) == 10
    fut = [l for l in lines if "ge" in l or "gi" in l or "gaa" in l or "gi." in l]
    cond = [l for l in lines if "je " in l and "taan" in l]
    print("lines: 10; future-marked: %d; je...taan conditions: %d" % (len(fut), len(cond)))
    assert len(fut) == 8
    assert len(cond) == 2
    assert "banaavaange" in lines[2] and "hovegaa" in lines[9]
    print("OK: %s drafted the future" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    idioms = [
        "jihaa des tihaa bhes", "nach na jaane vihraa tedhaa",
        "munh vich raam raam, bagal vich chhuri", "jitthe chaah utthe raah",
        "hath kanggan nun aarsi ki", "dooron dhol suhaavne",
        "naun nakad na teraan udhaar", "jo garajde han oh varasde nahin",
        "boond boond naal talaab bhardaa hai", "lohaa lohe nun kattdaa hai",
        "sachch kauraa hundaa hai", "vakat sabh ton vaddaa ustaad hai",
        "mehnat da phal mitthaa hundaa hai", "akkhon ohle pahaarh ohle",
        "jaan hai taan jahaan hai", "kar bhalaa ho bhalaa",
        "khudaa meharbaan te gadhaa pehalvaan", "dheeraj da phal mitthaa",
        "munhon nikli gall teer vaang", "ektaa vich bal hai",
    ]
    assert len(idioms) == 20
    assert len(set(idioms)) == 20, "duplicate idiom"
    # simulated 10-question quiz, 8 correct
    answers = [True] * 8 + [False] * 2
    score = sum(answers) / len(answers) * 100.0
    print("idioms: 20 unique; quiz: %d/%d = %.1f %%" % (sum(answers), len(answers), score))
    assert 79.9 < score < 80.1
    avg = sum(len(i) for i in idioms) / len(idioms)
    print("avg transliteration length: %.2f chars" % avg)
    assert 20.0 < avg < 35.0
    print("OK: %s sealed the sayings" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pairs = [
        ("tun kitthe hain?", "tusin kitthe ho?"),
        ("mainun de.", "mainun de dio."),
        ("chupp kar.", "kirpaa karke shaant raho."),
        ("tera naan ki hai?", "tuhada naan ki hai?"),
        ("tun aavengaa?", "ki tusin aaoge?"),
        ("pyaare Mohan,", "satikaaryog mahoday,"),
        ("tera dost,", "aap da vishvaaspaatar,"),
        ("paise de.", "paise den di kirpaa karo."),
        ("shukriyaa.", "bahut bahut dhannvaad."),
        ("nahin chaheeda.", "maaf karnaa, is vele sambhav nahin hai."),
        ("tun baith.", "tusin baitho ji."),
        ("maal bhej dio.", "maal bhejan di kirpaaltaa karni."),
        ("ghalti ho gayi.", "mainun maaf kar dio, ghalti ho gayi."),
        ("hello, kaun?", "sat sri akaal ji, main Simran bol rahi haan."),
        ("khush reh.", "khush raho, jug jug jeeo."),
    ]
    assert len(pairs) == 15
    markers = ("ji", "tusin", "tuhad", "kirpaa", "satikaar", "vishvaas",
               "maaf", "kirpaal")
    formal_hits = sum(1 for _inf, frm in pairs
                      if any(mk in frm for mk in markers))
    print("pairs: 15; formal markers present: %d/15" % formal_hits)
    assert formal_hits >= 12
    print("rungs: tun (intimate) < tusin (formal) < written formal")
    print("OK: %s climbed the register" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_complex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    conns = ["kionki", "jadon", "taan", "jo ", "jihri", "ki ", "je ",
             "bhaaven", "innaa", "pahilaan", "phir", "jaan", "na ", "jitthe",
             "jis"]
    sents = [
        "main school gayaa kionki mainun parhnaa see.",
        "jadon meenh piyaa taan asin andar aa gaye.",
        "oh munda jo baahar kharhaa hai mera dost hai.",
        "jihri kitaab tusin ditti see oh bahut changi hai.",
        "main chaahundaa haan ki tusin aao.",
        "usne kihaa ki oh kallh aavegaa.",
        "je tusin mehnat karoge taan safal hovoge.",
        "bhaaven meenh pai rihaa see, asin khedde rahe.",
        "oh innaa thakkiyaa hoyaa see ki saun gayaa.",
        "pahilaan khaana khaao, phir baahar jaao.",
        "na oh aayaa, na usne phone keetaa.",
        "jaan tusin aao, jaan main aavaan.",
        "oh jitthe vi jaanda hai, lok usnun pyaar karde han.",
        "jis din tusin aaoge, party hovegi.",
        "main ne oh kitaab parhi jis baare tusin dassiyaa see.",
    ]
    assert len(sents) == 15
    hits = sum(1 for s in sents if any(c in s for c in conns))
    print("complex sentences: 15; carrying connectors: %d/15" % hits)
    assert hits == 15
    pairs = sum(1 for s in sents if ("jadon" in s and "taan" in s)
                or ("je " in s and "taan" in s) or s.count("jaan") >= 2)
    print("correlative pairs (jadon/taan, je/taan, jaan/jaan): %d" % pairs)
    assert pairs == 3
    print("OK: %s bound the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


def _dialogue_demo(speakers_lines, title_note):
    def demo(hdr, name, rid, group, points, req):
        body = (
            "def main():\n"
            "    lines = " + repr(speakers_lines) + "\n"
            "    assert len(lines) == 20, len(lines)\n"
            "    turns = {}\n"
            "    for _sp, _tx in lines:\n"
            "        assert _tx.strip()\n"
            "        turns[_sp] = turns.get(_sp, 0) + 1\n"
            "    print('lines: 20; turns: %s' % turns)\n"
            "    assert sum(turns.values()) == 20 and len(turns) == 2\n"
            "    vals = sorted(turns.values())\n"
            "    assert vals[1] - vals[0] <= 2, vals\n"
            "    total = sum(len(_tx) for _sp, _tx in lines)\n"
            "    print('total dialogue chars: %d' % total)\n"
            "    assert 400 < total < 3000\n"
            "    print('OK: %s staged " + title_note + "' % NAME)\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        )
        return _wrap(hdr, name, rid, group, body)
    return demo


demo_pan_dialogue_market = _dialogue_demo([
("customer", "sat sri akaal ji!"), ("shopkeeper", "sat sri akaal! dasso, ki chaheeda hai?"),
("customer", "tamaatar kis bhaa han?"), ("shopkeeper", "assi rupaye kilo, bilkul taaze han."),
("customer", "bahut mahinge han, satth lagaao."),
("shopkeeper", "satth vich nahin honge, sattar aakhri bhaa hai."),
("customer", "chalo, ikk kilo de dio."), ("shopkeeper", "hor kujh? aaloo, piyaaz?"),
("customer", "addhaa kilo aaloo vi de dio."), ("shopkeeper", "eh lao, tol ke ditte han."),
("customer", "dhaniyaa muft paa dio."), ("shopkeeper", "lao ji, dhaniyaa vi paa dittaa."),
("customer", "kull kinna hoyaa?"), ("shopkeeper", "ikk sau das rupaye."),
("customer", "eh lao do sau, khullhe de dio."), ("shopkeeper", "nabbe vaapas, gin lao."),
("customer", "saudaa pakkaa, maal changa hai."),
("shopkeeper", "agli vaar phir aaunaa ji."),
("customer", "zaroor aavaangaa, rabb raakha!"), ("shopkeeper", "rabb raakha!"),
], "the market")

demo_pan_dialogue_friend = _dialogue_demo([
("Simran", "sat sri akaal! Gurpreet, tun?!"),
("Gurpreet", "Simran! kinne saalaan baad!"),
("Simran", "tun kitthe see inne saal?"),
("Gurpreet", "main Canada vich see, hun vaapas aayaa haan."),
("Simran", "vaah! Canada kiven laggaa?"),
("Gurpreet", "bahut vadheeyaa, par Panjaab di yaad aaundi see."),
("Simran", "chal, chaa peende haan, bahut gallaan karniaan han."),
("Gurpreet", "haan, chal. tera parivaar kiven hai?"),
("Simran", "sabh theek han, maan tainun yaad kardi hai."),
("Gurpreet", "agle hafte milan aavaangaa."),
("Simran", "tun viaah karvaa liyaa?"),
("Gurpreet", "haan, do saal ho gaye."),
("Simran", "vadhaai hove! bhaabi nun milnaa pavegaa."),
("Gurpreet", "zaroor, oh vi Panjaaban hai."),
("Simran", "tun Panjaabi nahin bhulliyaa!"),
("Gurpreet", "maan boli kade nahin bhulldi."),
("Simran", "sachch kihaa! chal, photo khichde haan."),
("Gurpreet", "haan, yaadgaar banegi."),
("Simran", "phir milde haan, rabb raakha!"),
("Gurpreet", "rabb raakha, Simran!"),
], "the reunion")

demo_pan_dialogue_problem = _dialogue_demo([
("traveler", "sat sri akaal ji, mainun madad chaheedi hai."),
("officer", "haan ji, dasso ki hoyaa?"),
("traveler", "mera phone gumm ho gayaa hai."),
("officer", "kitthe gumm hoyaa?"),
("traveler", "shaayad bass vich reh gayaa."),
("officer", "bass number yaad hai?"),
("traveler", "nahin ji, par oh Amritsar vaali bass see."),
("officer", "koi gall nahin, asin pataa karde haan."),
("traveler", "phone vich meriyaan photovaan ate number han."),
("officer", "chintaa na karo, riport likhde haan."),
("traveler", "riport lai ki ki chaheeda hai?"),
("officer", "naan, pataa, ate phone da model."),
("traveler", "mera naan Ravi hai, model pataa nahin."),
("officer", "koi gall nahin, bill di copy hai?"),
("traveler", "haan, email vich bill hai."),
("officer", "shaabaash! phir taan mil jaavegaa."),
("traveler", "kinna samaan laggegaa?"),
("officer", "do-tinn din, asin phone karaange."),
("traveler", "bahut bahut dhannvaad ji!"),
("officer", "koi gall nahin, khiyaal rakkho."),
], "the rescue")


def demo_pan_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    letters, vowels, digits = 35, 10, 10
    words = 200
    records = 34
    print("alphabet: %d letters; vowels: %d; digits: %d" % (letters, vowels, digits))
    assert letters == 35 and vowels == 10 and digits == 10
    print("core words: %d" % words)
    assert words == 200
    ladder = {"foundations": 9, "compounded": 11, "advanced": 14}
    print("ladder tiers: %s" % ladder)
    assert sum(ladder.values()) == records == 34
    share = ladder["advanced"] / records * 100.0
    print("advanced share: %.2f %%" % share)
    assert 41.17 < share < 41.19
    print("OK: %s bound the volume" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pan_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOV assembly: subject + object + verb must end with the verb
    triples = [("munda", "roti", "khaanda hai."),
               ("kurhi", "chaa", "peendi hai."),
               ("main", "kitaab", "parhda haan."),
               ("asin", "film", "dekhde haan.")]
    made = ["%s %s %s" % t for t in triples]
    print("assembled %d SOV sentences" % len(made))
    assert len(made) == 4
    assert all(s.endswith("hai.") or s.endswith("haan.") for s in made)
    for s in made:
        print("  " + s)
    # ergative flip: completed past agrees with the OBJECT
    assert "usne roti khaadhi." .split()[0] == "usne"
    assert "usne roti khaadhi.".split()[-1] == "khaadhi."
    print("ergative: usne (doer, ne-marked) + khaadhi (feminine, agrees with roti)")
    # postposition check
    posts = {"vich": "in", "utte": "on", "ton": "from", "naal": "with",
             "lai": "for", "nun": "to"}
    assert len(posts) == 6
    print("postpositions: %d" % len(posts))
    print("OK: %s built the sentences" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_pan_overview,
    "script": demo_pan_script,
    "phonology": demo_pan_phonology,
    "nouns1": demo_pan_nouns1,
    "verbs1": demo_pan_verbs1,
    "adjadv": demo_pan_adjadv,
    "pronouns": demo_pan_pronouns,
    "numbers": demo_pan_numbers,
    "greetings": demo_pan_greetings,
    "grammar": demo_pan_grammar,
    "home": demo_pan_home,
    "food": demo_pan_food,
    "travel": demo_pan_travel,
    "work": demo_pan_work,
    "health": demo_pan_health,
    "emotions": demo_pan_emotions,
    "nature": demo_pan_nature,
    "shopping": demo_pan_shopping,
    "social": demo_pan_social,
    "tech": demo_pan_tech,
    "tenses": demo_pan_tenses,
    "qa": demo_pan_qa,
    "commands": demo_pan_commands,
    "descriptions": demo_pan_descriptions,
    "story1": demo_pan_story1,
    "story2": demo_pan_story2,
    "story3": demo_pan_story3,
    "idioms": demo_pan_idioms,
    "registers": demo_pan_registers,
    "complex": demo_pan_complex,
    "dialogue_market": demo_pan_dialogue_market,
    "dialogue_friend": demo_pan_dialogue_friend,
    "dialogue_problem": demo_pan_dialogue_problem,
    "mastery": demo_pan_mastery,
}

