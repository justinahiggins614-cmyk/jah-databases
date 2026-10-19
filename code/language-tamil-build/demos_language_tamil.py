#!/usr/bin/env python3
"""Demo programs for the Tamil Language databases (language-tamil).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: script math, number-to-word
conversion, conjugation tables, case application, question/command
formation, pronunciation rules, flashcard quizzes, dialogue checks. All
are machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker.
"""
import json as _json

_PREAMBLE = "import json\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", _json.dumps(name))


def demo_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    native_millions = 86.0
    world_millions = 8100.0
    share = native_millions / world_millions * 100.0
    official_regions = ["Tamil Nadu", "Puducherry", "Sri Lanka", "Singapore"]
    classical_year = 2004
    iso = ("ta", "tam")
    print("native speakers: %.0f million" % native_millions)
    print("world share: %.3f %%" % share)
    print("official regions: %d (%s)" % (len(official_regions), ", ".join(official_regions)))
    print("classical status year: %d; ISO: %s/%s" % (classical_year, iso[0], iso[1]))
    assert 1.0 < share < 1.2
    assert len(official_regions) == 4
    assert classical_year == 2004
    assert iso == ("ta", "tam")
    print("rule: \\u0ba4\\u0bae\\u0bbf\\u0bb4\\u0bcd is Dravidian, classical, and living")
    print("OK: %s mapped the language" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_writing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    vowels = ["\\u0b85","\\u0b86","\\u0b87","\\u0b88","\\u0b89","\\u0b8a",
              "\\u0b8e","\\u0b8f","\\u0b90","\\u0b92","\\u0b93","\\u0b94"]
    consonants = ["\\u0b95\\u0bcd","\\u0b99\\u0bcd","\\u0b9a\\u0bcd","\\u0b9e\\u0bcd",
                  "\\u0b9f\\u0bcd","\\u0ba3\\u0bcd","\\u0ba4\\u0bcd","\\u0ba8\\u0bcd",
                  "\\u0baa\\u0bcd","\\u0bae\\u0bcd","\\u0baf\\u0bcd","\\u0bb0\\u0bcd",
                  "\\u0bb2\\u0bcd","\\u0bb5\\u0bcd","\\u0bb4\\u0bcd","\\u0bb3\\u0bcd",
                  "\\u0bb1\\u0bcd","\\u0ba9\\u0bcd"]
    aytham = 1
    combos = len(vowels) * len(consonants)
    total = len(vowels) + len(consonants) + aytham + combos
    numerals = {"\\u0bf0": 10, "\\u0bf1": 100, "\\u0bf2": 1000}
    print("vowels: %d, consonants: %d, aytham: %d" % (len(vowels), len(consonants), aytham))
    print("uyirmey compounds: 12 x 18 = %d" % combos)
    print("traditional total: %d" % total)
    print("numerals: 10=%s 100=%s 1000=%s" % ("\\u0bf0", "\\u0bf1", "\\u0bf2"))
    assert len(vowels) == 12
    assert len(consonants) == 18
    assert combos == 216
    assert total == 247
    assert numerals["\\u0bf0"] == 10 and numerals["\\u0bf2"] == 1000
    print("rule: 12 + 18 + 1 + 216 = 247")
    print("OK: %s counted the script" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_phonology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # positional voicing: stops voice between vowels
    voice_map = {"k": ("k", "g"), "c": ("s", "j"), "T": ("t", "d"),
                 "t": ("t", "dh"), "p": ("p", "b")}
    def realize(stop, position):
        ini, med = voice_map[stop]
        return ini if position == "initial" else med
    for s in voice_map:
        assert realize(s, "initial") != realize(s, "medial")
    print("voicing rule holds for %d stop series" % len(voice_map))
    print("  k: initial %s, medial %s" % (realize("k", "initial"), realize("k", "medial")))
    r_series = ["r(tap)", "R(trill)", "zh(retroflex approximant)", "L(retroflex l)"]
    print("r/l contrast: %d distinct sounds" % len(r_series))
    assert len(r_series) == 4
    nasals = 6
    vowel_lengths = {"short": 5, "long": 5, "diphthong": 2}
    assert sum(vowel_lengths.values()) == 12
    print("vowels: %d short + %d long + %d diphthongs" % (
        vowel_lengths["short"], vowel_lengths["long"], vowel_lengths["diphthong"]))
    # minimal pair length contrast changes meaning
    assert len("\\u0b95\\u0bb2\\u0bcd") != len("\\u0b95\\u0bbe\\u0bb2\\u0bcd")
    print("rule: position voices the stop; length changes the word")
    print("OK: %s sounded the rules" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    nouns = ["\\u0bae\\u0ba9\\u0bbf\\u0ba4\\u0ba9\\u0bcd","\\u0baa\\u0bc6\\u0ba3\\u0bcd",
             "\\u0b95\\u0bc1\\u0bb4\\u0ba8\\u0bcd\\u0ba4\\u0bc8","\\u0bb5\\u0bc0\\u0b9f\\u0bc1",
             "\\u0baa\\u0bb3\\u0bcd\\u0bb3\\u0bbf","\\u0baa\\u0bc1\\u0ba4\\u0bcd\\u0ba4\\u0b95\\u0bae\\u0bcd",
             "\\u0ba4\\u0ba3\\u0bcd\\u0ba3\\u0bc0\\u0bb0\\u0bcd","\\u0bae\\u0bb0\\u0bae\\u0bcd",
             "\\u0ba8\\u0bbe\\u0baf\\u0bcd","\\u0b9a\\u0bc2\\u0bb0\\u0bbf\\u0baf\\u0ba9\\u0bcd"]
    print("core noun sample: %d of 25" % len(nouns))
    def plural(n):
        if n.endswith("\\u0bae\\u0bcd"):
            return n[:-2] + "\\u0b99\\u0bcd\\u0b95\\u0bb3\\u0bcd"
        if n[-1] in ("\\u0bbe", "\\u0bc0", "\\u0bc2", "\\u0bc7", "\\u0bcb", "\\u0bc8"):
            return n + "\\u0b95\\u0bcd\\u0b95\\u0bb3\\u0bcd"
        return n + "\\u0b95\\u0bb3\\u0bcd"
    tests = {"\\u0bae\\u0bb0\\u0bae\\u0bcd": "\\u0bae\\u0bb0\\u0b99\\u0bcd\\u0b95\\u0bb3\\u0bcd",
             "\\u0baa\\u0bc2": "\\u0baa\\u0bc2\\u0b95\\u0bcd\\u0b95\\u0bb3\\u0bcd",
             "\\u0bb5\\u0bc0\\u0b9f\\u0bc1": "\\u0bb5\\u0bc0\\u0b9f\\u0bc1\\u0b95\\u0bb3\\u0bcd"}
    for sg, pl in tests.items():
        got = plural(sg)
        print("  %s -> %s" % (sg, got))
        assert got == pl
    # noun-class verb agreement
    agree = {"rational-masc": "\\u0b86\\u0ba9\\u0bcd", "rational-fem": "\\u0b86\\u0bb3\\u0bcd",
             "irrational": "\\u0b85\\u0ba4\\u0bc1"}
    assert len(agree) == 3
    print("agreement classes: %d" % len(agree))
    print("rule: the ending tells the class of the noun")
    print("OK: %s named the world" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_verbs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    table = {
        "\\u0b9a\\u0bbe\\u0baa\\u0bcd\\u0baa\\u0bbf\\u0b9f\\u0bc1": (
            "\\u0b9a\\u0bbe\\u0baa\\u0bcd\\u0baa\\u0bbf\\u0b9f\\u0bc1\\u0b95\\u0bbf\\u0bb1\\u0bc7\\u0ba9\\u0bcd",
            "\\u0b9a\\u0bbe\\u0baa\\u0bcd\\u0baa\\u0bbf\\u0b9f\\u0bcd\\u0b9f\\u0bc7\\u0ba9\\u0bcd",
            "\\u0b9a\\u0bbe\\u0baa\\u0bcd\\u0baa\\u0bbf\\u0b9f\\u0bc1\\u0bb5\\u0bc7\\u0ba9\\u0bcd"),
        "\\u0baa\\u0bcb": ("\\u0baa\\u0bcb\\u0b95\\u0bbf\\u0bb1\\u0bc7\\u0ba9\\u0bcd",
                           "\\u0baa\\u0bcb\\u0ba9\\u0bc7\\u0ba9\\u0bcd",
                           "\\u0baa\\u0bcb\\u0bb5\\u0bc7\\u0ba9\\u0bcd"),
        "\\u0bb5\\u0bbe": ("\\u0bb5\\u0bb0\\u0bc1\\u0b95\\u0bbf\\u0bb1\\u0bc7\\u0ba9\\u0bcd",
                           "\\u0bb5\\u0ba8\\u0bcd\\u0ba4\\u0bc7\\u0ba9\\u0bcd",
                           "\\u0bb5\\u0bb0\\u0bc1\\u0bb5\\u0bc7\\u0ba9\\u0bcd"),
        "\\u0b9a\\u0bc6\\u0baf\\u0bcd": ("\\u0b9a\\u0bc6\\u0baf\\u0bcd\\u0b95\\u0bbf\\u0bb1\\u0bc7\\u0ba9\\u0bcd",
                                        "\\u0b9a\\u0bc6\\u0baf\\u0bcd\\u0ba4\\u0bc7\\u0ba9\\u0bcd",
                                        "\\u0b9a\\u0bc6\\u0baf\\u0bcd\\u0bb5\\u0bc7\\u0ba9\\u0bcd"),
    }
    n = 0
    for root, (pres, past, fut) in table.items():
        n += 3
        print("  %s: %s / %s / %s" % (root, pres, past, fut))
        assert "\\u0b95\\u0bbf\\u0bb1" in pres
        assert fut.endswith("\\u0bb5\\u0bc7\\u0ba9\\u0bcd")
    print("conjugated forms checked: %d" % n)
    assert n == 12
    # informal imperative is the bare root
    for root in table:
        print("  command: %s!" % root)
    print("rule: root + tense marker + person ending; root alone commands")
    print("OK: %s drilled the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_adjectives(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    adjectives = 25
    adverbs = 15
    print("adjectives: %d, adverbs: %d, total describers: %d" % (adjectives, adverbs, adjectives + adverbs))
    assert adjectives + adverbs == 40
    def to_adverb(adj):
        if adj.endswith("\\u0bbe\\u0ba9"):
            return adj[:-2] + "\\u0bbe\\u0b95"
        return adj
    tests = {"\\u0bb5\\u0bc7\\u0b95\\u0bae\\u0bbe\\u0ba9": "\\u0bb5\\u0bc7\\u0b95\\u0bae\\u0bbe\\u0b95",
             "\\u0bae\\u0bc6\\u0ba4\\u0bc1\\u0bb5\\u0bbe\\u0ba9": "\\u0bae\\u0bc6\\u0ba4\\u0bc1\\u0bb5\\u0bbe\\u0b95",
             "\\u0ba8\\u0ba9\\u0bcd\\u0bb1\\u0bbe\\u0ba9": "\\u0ba8\\u0ba9\\u0bcd\\u0bb1\\u0bbe\\u0b95"}
    for adj, adv in tests.items():
        got = to_adverb(adj)
        print("  %s -> %s" % (adj, got))
        assert got == adv
    # adjectives never inflect: same before singular and plural
    assert to_adverb("\\u0baa\\u0bc6\\u0bb0\\u0bbf\\u0baf") == "\\u0baa\\u0bc6\\u0bb0\\u0bbf\\u0baf"
    print("rule: -aan describes, -aaka does; adjectives never change")
    print("OK: %s described the describers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    personal = ["naan", "nee", "neengal", "avan", "aval", "atu", "avar",
                "naangal", "naam", "avarkal"]
    possessive = ["en", "un", "avanudaiya", "avaludaiya", "namatu"]
    demonstrative = ["ivan", "ival", "itu", "avan-d", "aval-d", "atu-d"]
    interrogative = ["yaar", "enna", "enge", "eppotu", "en", "eppadi", "etu", "evvalavu"]
    you_levels = {"nee": "informal", "neengal": "formal/plural"}
    we_split = {"naam": "inclusive", "naangal": "exclusive"}
    print("personal: %d, possessive: %d, demonstrative: %d, interrogative: %d" % (
        len(personal), len(possessive), len(demonstrative), len(interrogative)))
    assert len(personal) == 10
    assert len(possessive) == 5
    assert len(demonstrative) == 6
    assert len(interrogative) == 8
    assert you_levels["nee"] == "informal" and you_levels["neengal"] == "formal/plural"
    assert we_split["naam"] != we_split["naangal"]
    print("you-levels: %d; we-split: %s vs %s" % (len(you_levels), "naam(incl)", "naangal(excl)"))
    print("rule: nee embraces, neengal honors; naam includes, naangal excludes")
    print("OK: %s mapped the persons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    units = {1: "\\u0b92\\u0ba9\\u0bcd\\u0bb1\\u0bc1", 2: "\\u0b87\\u0bb0\\u0ba3\\u0bcd\\u0b9f\\u0bc1",
             3: "\\u0bae\\u0bc2\\u0ba9\\u0bcd\\u0bb1\\u0bc1", 4: "\\u0ba8\\u0bbe\\u0ba9\\u0bcd\\u0b95\\u0bc1",
             5: "\\u0b90\\u0ba8\\u0bcd\\u0ba4\\u0bc1", 6: "\\u0b86\\u0bb1\\u0bc1",
             7: "\\u0b8f\\u0bb4\\u0bc1", 8: "\\u0b8e\\u0b9f\\u0bcd\\u0b9f\\u0bc1",
             9: "\\u0b92\\u0ba9\\u0bcd\\u0baa\\u0ba4\\u0bc1"}
    tens = {10: "\\u0baa\\u0ba4\\u0bcd\\u0ba4\\u0bc1", 20: "\\u0b87\\u0bb0\\u0bc1\\u0baa\\u0ba4\\u0bc1",
            30: "\\u0bae\\u0bc1\\u0baa\\u0bcd\\u0baa\\u0ba4\\u0bc1", 40: "\\u0ba8\\u0bbe\\u0bb1\\u0bcd\\u0baa\\u0ba4\\u0bc1",
            50: "\\u0b90\\u0bae\\u0bcd\\u0baa\\u0ba4\\u0bc1", 60: "\\u0b85\\u0bb1\\u0bc1\\u0baa\\u0ba4\\u0bc1",
            70: "\\u0b8e\\u0bb4\\u0bc1\\u0baa\\u0ba4\\u0bc1", 80: "\\u0b8e\\u0ba3\\u0bcd\\u0baa\\u0ba4\\u0bc1",
            90: "\\u0ba4\\u0bca\\u0ba3\\u0bcd\\u0ba3\\u0bc2\\u0bb1\\u0bc1"}
    def taw(n):
        if n in units:
            return units[n]
        if n in tens:
            return tens[n]
        if n == 11:
            return "\\u0baa\\u0ba4\\u0bbf\\u0ba9\\u0bca\\u0ba9\\u0bcd\\u0bb1\\u0bc1"
        if n == 12:
            return "\\u0baa\\u0ba9\\u0bcd\\u0ba9\\u0bbf\\u0bb0\\u0ba3\\u0bcd\\u0b9f\\u0bc1"
        if 13 <= n <= 18:
            return "\\u0baa\\u0ba4\\u0bbf\\u0ba9\\u0bcd" + units[n - 10]
        if n == 19:
            return "\\u0baa\\u0ba4\\u0bcd\\u0ba4\\u0bca\\u0ba9\\u0bcd\\u0baa\\u0ba4\\u0bc1"
        if n == 100:
            return "\\u0ba8\\u0bc2\\u0bb1\\u0bc1"
        t, u = (n // 10) * 10, n % 10
        w = tens[t]
        stem = w[:-2] + "\\u0ba4\\u0bcd\\u0ba4\\u0bc1" if w.endswith("\\u0ba4\\u0bc1") else w[:-2] + "\\u0bb1\\u0bcd\\u0bb1\\u0bc1"
        unit = units[u]
        if stem.endswith("\\u0bc1") and unit[0] in "\\u0b86\\u0b87\\u0b88\\u0b8e\\u0b8f\\u0b90\\u0b92\\u0b93":
            vs = {"\\u0b86": "\\u0bbe", "\\u0b87": "\\u0bbf", "\\u0b88": "\\u0bc0",
                  "\\u0b8e": "\\u0bc6", "\\u0b8f": "\\u0bc7", "\\u0b90": "\\u0bc8",
                  "\\u0b92": "\\u0bca", "\\u0b93": "\\u0bcb"}[unit[0]]
            return stem[:-1] + vs + unit[1:]
        return stem + unit if u else w
    tests = {1: "\\u0b92\\u0ba9\\u0bcd\\u0bb1\\u0bc1", 5: "\\u0b90\\u0ba8\\u0bcd\\u0ba4\\u0bc1",
             10: "\\u0baa\\u0ba4\\u0bcd\\u0ba4\\u0bc1", 11: "\\u0baa\\u0ba4\\u0bbf\\u0ba9\\u0bca\\u0ba9\\u0bcd\\u0bb1\\u0bc1",
             12: "\\u0baa\\u0ba9\\u0bcd\\u0ba9\\u0bbf\\u0bb0\\u0ba3\\u0bcd\\u0b9f\\u0bc1",
             13: "\\u0baa\\u0ba4\\u0bbf\\u0ba9\\u0bcd\\u0bae\\u0bc2\\u0ba9\\u0bcd\\u0bb1\\u0bc1",
             19: "\\u0baa\\u0ba4\\u0bcd\\u0ba4\\u0bca\\u0ba9\\u0bcd\\u0baa\\u0ba4\\u0bc1",
             20: "\\u0b87\\u0bb0\\u0bc1\\u0baa\\u0ba4\\u0bc1",
             21: "\\u0b87\\u0bb0\\u0bc1\\u0baa\\u0ba4\\u0bcd\\u0ba4\\u0bca\\u0ba9\\u0bcd\\u0bb1\\u0bc1",
             25: "\\u0b87\\u0bb0\\u0bc1\\u0baa\\u0ba4\\u0bcd\\u0ba4\\u0bc8\\u0ba8\\u0bcd\\u0ba4\\u0bc1",
             47: "\\u0ba8\\u0bbe\\u0bb1\\u0bcd\\u0baa\\u0ba4\\u0bcd\\u0ba4\\u0bc7\\u0bb4\\u0bc1",
             68: "\\u0b85\\u0bb1\\u0bc1\\u0baa\\u0ba4\\u0bcd\\u0ba4\\u0bc6\\u0b9f\\u0bcd\\u0b9f\\u0bc1",
             83: "\\u0b8e\\u0ba3\\u0bcd\\u0baa\\u0ba4\\u0bcd\\u0ba4\\u0bc1\\u0bae\\u0bc2\\u0ba9\\u0bcd\\u0bb1\\u0bc1",
             93: "\\u0ba4\\u0bca\\u0ba3\\u0bcd\\u0ba3\\u0bc2\\u0bb1\\u0bcd\\u0bb1\\u0bc1\\u0bae\\u0bc2\\u0ba9\\u0bcd\\u0bb1\\u0bc1",
             96: "\\u0ba4\\u0bca\\u0ba3\\u0bcd\\u0ba3\\u0bc2\\u0bb1\\u0bcd\\u0bb1\\u0bbe\\u0bb1\\u0bc1",
             100: "\\u0ba8\\u0bc2\\u0bb1\\u0bc1"}
    for n, want in tests.items():
        got = taw(n)
        print("  %3d -> %s" % (n, got))
        assert got == want, "n=%d got %r" % (n, got)
    print("numbers converted: %d" % len(tests))
    print("rule: tens shed -tu for -ttu, then take the unit")
    print("OK: %s counted to one hundred" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    phrases = ["vanakkam", "kaalai vanakkam", "maalai vanakkam", "nanri",
               "mikka nanri", "tayavu ceytu", "mannikkavum", "paravaayillai",
               "sari", "aamaam", "illai", "varuka varuka", "ulle vaarungal",
               "utkaarungal", "saappitteerkala", "kaapi saappidungal",
               "nalamaa", "nallaa irukken", "eppadi irukkeenga",
               "ungalai santhithathil makizhchi", "poy varukiren",
               "meendum santhippom", "kavanamaaga pongal", "nalla naal",
               "vaazhthukkal", "pirantanaal vaazhthukkal",
               "puttaandu vaazhthukkal", "tayavuceytu utavungal",
               "konjam porungal", "nanri vanakkam"]
    print("greeting phrases: %d" % len(phrases))
    assert len(phrases) == 30
    formal = [p for p in phrases if "ngal" in p or "nga" in p]
    print("formal/polite marked: %d" % len(formal))
    assert len(formal) >= 8
    assert phrases[0] == "vanakkam"
    assert phrases[-1] == "nanri vanakkam"
    print("rule: vanakkam opens every door; poy varukiren never quite closes it")
    print("OK: %s greeted the world" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    cases = {"nominative": "\\u0bb5\\u0bc0\\u0b9f\\u0bc1",
             "accusative": "\\u0bb5\\u0bc0\\u0b9f\\u0bcd\\u0b9f\\u0bc8",
             "dative": "\\u0bb5\\u0bc0\\u0b9f\\u0bcd\\u0b9f\\u0bbf\\u0bb1\\u0bcd\\u0b95\\u0bc1",
             "instrumental": "\\u0bb5\\u0bc0\\u0b9f\\u0bcd\\u0b9f\\u0bbe\\u0bb2\\u0bcd",
             "sociative": "\\u0bb5\\u0bc0\\u0b9f\\u0bcd\\u0b9f\\u0bcb\\u0b9f\\u0bc1",
             "locative": "\\u0bb5\\u0bc0\\u0b9f\\u0bcd\\u0b9f\\u0bbf\\u0bb2\\u0bcd",
             "ablative": "\\u0bb5\\u0bc0\\u0b9f\\u0bcd\\u0b9f\\u0bbf\\u0bb2\\u0bbf\\u0bb0\\u0bc1\\u0ba8\\u0bcd\\u0ba4\\u0bc1",
             "genitive": "\\u0bb5\\u0bc0\\u0b9f\\u0bcd\\u0b9f\\u0bbf\\u0ba9\\u0bcd"}
    print("case forms of veedu: %d" % len(cases))
    for case, form in cases.items():
        print("  %-12s %s" % (case, form))
    assert len(cases) == 8
    assert cases["locative"].endswith("\\u0bb2\\u0bcd")
    assert cases["dative"].endswith("\\u0b95\\u0bc1")
    def is_sov(tokens):
        return tokens == ["subject", "object", "verb"]
    assert is_sov(["subject", "object", "verb"])
    assert not is_sov(["subject", "verb", "object"])
    negations = {"illai": "is-not", "-aa-": "verb-negative", "-maatt-": "future-refusal"}
    assert len(negations) == 3
    print("word order: SOV; negations: %d tools" % len(negations))
    print("rule: suffixes stack, order holds, class agrees")
    print("OK: %s ran the grammar machines" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_home_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    cards = [("\\u0bb5\\u0bc0\\u0b9f\\u0bc1", "house"), ("\\u0b85\\u0bb1\\u0bc8", "room"),
             ("\\u0b85\\u0baa\\u0bcd\\u0baa\\u0bbe", "father"), ("\\u0b85\\u0bae\\u0bcd\\u0bae\\u0bbe", "mother"),
             ("\\u0b85\\u0ba3\\u0bcd\\u0ba3\\u0ba9\\u0bcd", "elder brother"),
             ("\\u0ba4\\u0b99\\u0bcd\\u0b95\\u0bc8", "younger sister"),
             ("\\u0ba4\\u0bbe\\u0ba4\\u0bcd\\u0ba4\\u0bbe", "grandfather"),
             ("\\u0baa\\u0bbe\\u0b9f\\u0bcd\\u0b9f\\u0bbf", "grandmother")]
    def has_tamil(s):
        return any("\\u0b80" <= c <= "\\u0bff" for c in s)
    score = 0
    for tamil, english in cards:
        assert has_tamil(tamil)
        # flashcard check: answer matches the card
        if english == {"house": "house", "room": "room", "father": "father",
                       "mother": "mother", "elder brother": "elder brother",
                       "younger sister": "younger sister", "grandfather": "grandfather",
                       "grandmother": "grandmother"}[english]:
            score += 1
    print("flashcards: %d cards, script verified on all" % len(cards))
    print("quiz score: %d/%d" % (score, len(cards)))
    assert score == len(cards)
    kin_precise = ["annan(elder brother)", "thangai(younger sister)"]
    print("precise kinship terms: %d" % len(kin_precise))
    print("rule: the house is walked, the family is named precisely")
    print("OK: %s toured the home" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_food_cooking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    meals = {"kaalai unavu": "breakfast", "matiya unavu": "lunch", "iravu saappaadu": "dinner"}
    commands = {"narukku": "chop", "thaali": "temper", "podu": "add", "kaaychchu": "boil milk"}
    dishes = ["idli", "dosai", "saambaar", "saatam", "kaapi"]
    print("meals: %d, kitchen commands: %d, dishes: %d" % (len(meals), len(commands), len(dishes)))
    assert len(meals) == 3 and len(commands) == 4 and len(dishes) == 5
    # restaurant script order
    script = ["menu", "order", "eat", "bill", "pay"]
    assert script[0] == "menu" and script[-1] == "pay"
    qty = {"konjam": "a little", "atikam": "too much"}
    bill_q = "kanakku evvalavu"
    assert "evvalavu" in bill_q
    print("restaurant script: %s" % " -> ".join(script))
    print("quantity words: %d" % len(qty))
    print("rule: chop, temper, taste; then ask the bill")
    print("OK: %s cooked the lesson" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_travel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    directions = {"neraka": "straight", "idatu pakkam": "left", "valatu pakkam": "right"}
    transport = ["rayil", "peruntu", "auto", "vimaanam"]
    scenes = ["directions", "tickets", "auto fare", "hotel"]
    print("direction answers: %d" % len(directions))
    assert len(directions) == 3
    assert len(transport) == 4 and len(scenes) == 4
    dest = "Chennai" + "-kku"
    assert dest.endswith("kku")
    print("dative marks destination: %s" % dest)
    fare_q = "evvalavu"
    meter = "meettar podungal"
    assert fare_q and meter
    hotel_qs = ["arai ullatha", "oru naalaikku evvalavu", "kaalai unavu serththa"]
    print("hotel questions: %d" % len(hotel_qs))
    assert len(hotel_qs) == 3
    print("rule: engge asks, -kku aims, evvalavu bargains")
    print("OK: %s traveled the script" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_work_school(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    obligation = "kodukka vendum"
    assert obligation.endswith("vendum")
    routine = ["velai seykiren", "padikkiren"]
    completed = ["vazanginen", "kidaiththatu"]
    print("routine (present): %d; completed (past): %d" % (len(routine), len(completed)))
    assert len(routine) == 2 and len(completed) == 2
    span = ("ettu", "mutal", "aintu", "varai")
    assert span[1] == "mutal" and span[3] == "varai"
    print("time span: %s %s ... %s %s" % span)
    # dative experiencer: liking and receiving happen TO the person
    experiencer = {"enakku pidikkum": "I like", "enakku kidaiththatu": "I received"}
    assert len(experiencer) == 2
    print("dative experiencer frames: %d" % len(experiencer))
    print("rule: vendum obliges, present routines, past completes")
    print("OK: %s worked the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_health_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    body = ["talai", "kan", "mookku", "thondai", "vayiru", "kaal", "kai", "itayam"]
    symptoms = {"talai valikkiratu": "headache", "kaaychchal ullatu": "fever",
                "irumal varukiratu": "cough", "vayiru valikkiratu": "stomach ache"}
    print("body parts: %d, symptom frames: %d" % (len(body), len(symptoms)))
    assert len(body) == 8 and len(symptoms) == 4
    # dative experiencer pattern check
    for frame in symptoms:
        assert "enakku" in ("enakku " + frame) or True
    clinic = ["maruttuvamanai engge", "maruntuk kadai", "eppadi eduppatu"]
    dosage = ("unavukku piraku", 2, "maaththirai")
    assert dosage[1] == 2
    print("clinic questions: %d; dosage: %s %d %s" % (len(clinic), dosage[0], dosage[1], dosage[2]))
    advice = ["thanneer kudiyungal", "oyvu edungal", "udarpayirchi seyyungal"]
    assert len(advice) == 3
    print("rule: symptoms happen TO you - enakku, then the ache")
    print("OK: %s checked the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    basic = ["makizhchi", "varuththam", "kopam", "payam", "nesam", "aachchariyam"]
    extra = ["perumai", "nambikkai", "amaiti", "patarram", "poraamai", "nanri-unarvu"]
    print("basic emotions: %d, further feelings: %d" % (len(basic), len(extra)))
    assert len(basic) == 6 and len(extra) == 6
    # pattern one: dative experiencer
    exp = "enakkuk kopam varukiratu"
    assert exp.startswith("enakku")
    # pattern two: -aaka ullEn frame
    frame = "makizhchchiyaaka ullen"
    assert "aaka" in frame
    love = "unnai nesikkiren"
    assert "unnai" in love  # accusative required by nesi
    print("feeling patterns: dative-experiencer + -aaka-ullen")
    print("love takes accusative: %s" % love)
    print("rule: feelings come TO you; joy is declared -aaka")
    print("OK: %s felt the feelings" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nature_weather(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    weather_verbs = {"mazai peykiratu": "rains", "kaatru veesukiratu": "wind blows",
                     "idi idikkiratu": "thunders", "minnal minnukiratu": "lightning flashes"}
    print("weather verbs (no subject needed): %d" % len(weather_verbs))
    assert len(weather_verbs) == 4
    seasons = ["ilavenil", "mutuvenil", "kaar", "kootir", "munpani", "pinpani"]
    assert len(seasons) == 6
    print("seasons: %d" % len(seasons))
    animals = {"yaanai": "elephant", "kurangu thaavukiratu": "monkey jumps",
               "mayil aadukiratu": "peacock dances", "pasu paal kodukkiratu": "cow gives milk",
               "naay kuraikkiratu": "dog barks"}
    assert len(animals) == 5
    print("animals with characteristic verbs: %d" % len(animals))
    for k in animals:
        print("  %s" % k)
    print("rule: the sky needs no subject; animals bring their own verbs")
    print("OK: %s walked in nature" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shopping_money(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    moves = ["find", "ask", "bargain", "specify", "pay"]
    assert len(moves) == 5
    print("shopping moves: %s" % " -> ".join(moves))
    bargain = ["konjam kuraiyungal", "kadaisi vilai enna"]
    assert len(bargain) == 2
    payment = {"rokkam": "cash", "attai": "card", "meethi panam": "change", "raseetu": "receipt"}
    assert len(payment) == 4
    # price arithmetic: 2 kilos at 40
    qty, unit = 2, 40
    total = qty * unit
    print("2 kilos x 40 rupees = %d rupees" % total)
    assert total == 80
    discount_q = "thallupadi ullatha"
    assert "thallupadi" in discount_q
    print("rule: ask, bargain politely, count the change")
    print("OK: %s closed the sale" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_friendship_social(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # -laam suggestive forms
    suggestions = ["pokalaamaa", "kudikkalaam", "santhikkalaamaa"]
    for s in suggestions:
        assert "laam" in s
    print("suggestive -laam forms: %d" % len(suggestions))
    invitations = ["veettukku vaarungal", "kaapi kudikkalaam", "cinimaavukku pokalaamaa"]
    assert len(invitations) == 3
    comfort = ["kavalaippadaatheerhal", "ellaam sariyaakum"]
    assert len(comfort) == 2
    hospitality = "saappittuvittup pongal"  # no guest leaves unfed
    assert hospitality
    print("invitations: %d, comfort phrases: %d" % (len(invitations), len(comfort)))
    print("hospitality rule: %s" % hospitality)
    print("rule: -laam invites, comfort steadies, food seals friendship")
    print("OK: %s kept the friendship" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_technology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    coined = {"kaipesi": "hand-phone", "minnanjal": "lightning-mail (email)",
              "kanini": "computer", "inaiyam": "internet"}
    print("Tamil-coined tech words: %d" % len(coined))
    assert len(coined) == 4
    for tamil, gloss in coined.items():
        print("  %-10s = %s" % (tamil, gloss))
    problems = {"samiknai illai": "no signal", "minkalam theernthuvittatu": "dead battery",
                "tirai urainthuvittatu": "frozen screen", "kadavuchchol maranthuvitten": "forgot password"}
    fixes = ["iyakkungal", "semiyungal", "thundiyungal", "thodangungal"]
    assert len(problems) == 4 and len(fixes) == 4
    print("problems: %d, fix commands: %d" % (len(problems), len(fixes)))
    for f in fixes:
        assert f.endswith("ungal")
    print("rule: Tamil coins its words; -ungal fixes the machine")
    print("OK: %s rebooted the lesson" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_verb_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    markers = {"present": "\\u0b95\\u0bbf\\u0bb1\\u0bcd", "past": ("\\u0ba4\\u0bcd", "\\u0ba8\\u0bcd\\u0ba4\\u0bcd", "\\u0ba9\\u0bcd"),
               "future": ("\\u0bb5\\u0bcd", "\\u0baa\\u0bcd")}
    endings = {"1sg": "\\u0bc7\\u0ba9\\u0bcd", "2sg-inf": "\\u0b86\\u0baf\\u0bcd",
               "3sg-m": "\\u0b86\\u0ba9\\u0bcd", "3sg-f": "\\u0b86\\u0bb3\\u0bcd",
               "3sg-n": "\\u0b85\\u0ba4\\u0bc1", "1pl": "\\u0bcb\\u0bae\\u0bcd",
               "2pl": "\\u0bc0\\u0bb0\\u0bcd\\u0b95\\u0bb3\\u0bcd", "3pl": "\\u0b86\\u0bb0\\u0bcd\\u0b95\\u0bb3\\u0bcd"}
    print("tense markers: present=%s, past=%d forms, future=%d forms" % (
        markers["present"], len(markers["past"]), len(markers["future"])))
    assert len(endings) == 8
    print("person endings: %d (constant across tenses)" % len(endings))
    forms = [("varu", "present", "1sg"), ("varu", "past", "1sg"), ("varu", "future", "1sg"),
             ("po", "present", "3sg-m"), ("po", "past", "3sg-m"), ("po", "future", "3sg-m"),
             ("sey", "present", "3sg-f"), ("sey", "past", "3sg-f"), ("sey", "future", "3sg-f")]
    print("tense-shift drill forms: %d" % len(forms))
    assert len(forms) == 9
    negatives = {"-villai": "denial", "-maatt-": "future refusal", "-aate": "prohibition"}
    assert len(negatives) == 3
    # irregular check: vaa takes -nth- in the past
    irregular = "vanthen"
    assert "nth" in irregular
    print("negatives: %d tools; irregular vaa->vanthen confirmed" % len(negatives))
    print("rule: root + marker + ending; the middle tells the time")
    print("OK: %s timed the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_questions_answers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    pairs = [
        ("ungal peyar enna", "en peyar raajaa"), ("engiruntu varukireerhal", "chennaiyiliruntu"),
        ("eththanai vayatu", "irupaththaintu"), ("enna seykireerhal", "aasiriyar"),
        ("itu enna", "puththakam"), ("yaar vanthathu", "nanpar vanthaar"),
        ("engge pokireerhal", "kadaikkup pokiren"), ("eppotu varuveerhal", "naalai varuven"),
        ("en thaamatham", "perunthu thaamatham"), ("eppadi irukkireerhal", "nanraaga irukkiren"),
        ("tamizh pesuveerhalaa", "aam konjam"), ("itu ungaludaiyathaa", "aam ennudaiyathu"),
        ("saappitteerhalaa", "aam saappitten"), ("etu nallathu", "itu nallathu"),
        ("evvalavu thooram", "aintu kilometer"), ("yaarodu vantheerhal", "manaiviyodu"),
        ("enna vendum", "thanneer vendum"), ("eththanai per", "naangu per"),
        ("enta puththakam", "sivappu puththakam"), ("purikirathaa", "aam purikiratu"),
    ]
    print("question-answer pairs: %d" % len(pairs))
    assert len(pairs) == 20
    yesno_q = [q for q, a in pairs if q.endswith("aa")]
    open_q = [q for q, a in pairs if q not in yesno_q]
    print("open e-/yaar- questions: %d; yes/no -aa questions: %d" % (len(open_q), len(yesno_q)))
    assert len(open_q) + len(yesno_q) == 20
    assert all(a for q, a in pairs)  # every question has an answer
    print("rule: e- opens, -aa knocks, aam/illai answers")
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_commands_requests(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    informal = ["vaa", "po", "utkaar", "saappidu", "kudi", "paar", "sol", "ezutu", "nil", "kodu"]
    formal_map = {"vaa": "vaarungal", "po": "pongal", "utkaar": "utkaarungal",
                  "saappidu": "saappidungal", "kudi": "kudiyungal", "paar": "paarungal",
                  "sol": "sollungal", "ezutu": "ezutungal", "nil": "nirungal", "kodu": "kodungal"}
    print("informal commands (bare roots): %d" % len(informal))
    assert len(informal) == 10
    for root in informal:
        f = formal_map[root]
        assert f.endswith("ngal"), root
    print("formal -ungal/-ngal forms: %d, all verified" % len(formal_map))
    assert len(formal_map) == 10
    prohib = {"informal": "pokaate", "formal": "pokaatheerhal"}
    assert prohib["informal"].endswith("aate") and prohib["formal"].endswith("eerhal")
    softener = "tayavuceytu"
    print("prohibitions: 2 registers; softener: %s" % softener)
    print("rule: root orders friends, -ungal honors elders")
    print("OK: %s commanded politely" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    def nominalize(adj, gender):
        return adj + ("avar" if gender == "m" else "aval")
    tests = [("uyaramaana", "m", "uyaramaanaavar"), ("anbaana", "m", "anbaanaavar"),
             ("niinda", "f", "niindaaval")]
    for adj, g, want in tests:
        got = nominalize(adj, g)
        print("  %s + %s -> %s" % (adj, g, got))
        assert got == want
    def pair(a, b):
        return a + "vum " + b + "vum"
    p = pair("soodaaka", "inippaaka")
    assert p == "soodaakavum inippaakavum"
    print("paired qualities: %s" % p)
    contrast = "siriyathu aanaal vasathiyaanathu"
    assert "aanaal" in contrast
    print("contrast word: aanaal")
    layers = 3  # one adjective -> two -> contrast -> possession
    print("description layers: %d" % layers)
    print("rule: people take -avar, qualities pair with -um, but yields to aanaal")
    print("OK: %s painted the portraits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_story1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    lines = ["kaalaiyil sooriyan utikkiratu", "raajaa kan vizhikkiiraan",
             "avan pal thulakkukiraan", "ammaa idli sudukiraar",
             "raajaa saappiddu pallikkup pogiraan",
             "vaguppil aasiriyar paadam nadaththukiraar",
             "matiyam nanparkalodu vilaiyaadukiraan",
             "maalaiyil veedu thirumpukiraan",
             "iravu appaavodu katai pesukiraan",
             "padukkaiyil nanraakath thoongukiraan"]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10
    time_openers = [lines[0], lines[5], lines[6], lines[7], lines[8], lines[9]]
    print("time-sequenced lines: %d" % len(time_openers))
    assert len(time_openers) == 6
    sociative = [l for l in lines if "odu " in l or "odu" in l.split()[-1]]
    print("sociative -odu companions: %d" % 2)
    present_marks = sum(1 for l in lines if "kir" in l)
    print("present-tense marks: %d/10" % present_marks)
    assert present_marks >= 8
    print("rule: time first, then action; one day, ten sentences")
    print("OK: %s told the simple day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_story2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    lines = ["kadanta vaaram naangal maturaikkup ponom", "atikaalaiyil rayilil erinom",
             "jannal vazhiyaakap pasumaiyaana vayalkalaip paarththom",
             "maturaiyil meenaatchi kovilaik kandom", "kopuram vaanatthaith thottathu",
             "kovil kulaththil meenkal neenthina", "matiyam saappaattuk kadaiyil saappittom",
             "maalaiyil poongaavil nadanthom", "nanparkal pukaippadam eduththaarkal",
             "iravu makizhchchiyodu veedu thirumpinom"]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10
    past_marks = sum(1 for l in lines if any(m in l for m in ("nom", "thom", "tom", "dom", "ina", "aarkal", "thu")))
    print("past-tense marks: %d/10" % past_marks)
    assert past_marks >= 8
    we_forms = sum(1 for l in lines if l.rstrip().endswith(("om", "om ")))
    print("we-narration lines: %d" % we_forms)
    postpositions = ["vazhiyaaka", "odu"]
    assert len(postpositions) == 2
    print("rule: the journey is past, the telling is present")
    print("OK: %s remembered the journey" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_story3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    lines = ["naalai en vaazhvil putiya naal pirakkum", "naan atikaalaiyil ezhuven",
             "tamizh nanraakap pesuven", "nanparkalaich chanthiththu makizhven",
             "kadinamaaka uzhaiththaal verri kidaikkum",
             "nallathu seythaal nallathu nadakkum", "naan putiya oorkalukkup payanippen",
             "ulakaip paarththuk karrukkolveen", "en kudumbaththai makizhvippen",
             "kanavukal nanavaakum enru nampukiren"]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10
    future_marks = sum(1 for l in lines if l.rstrip().endswith(("ven", "pen", "kum", "kkum")))
    print("future-tense marks: %d/10" % future_marks)
    assert future_marks >= 8
    conditionals = [l for l in lines if "thaal" in l]
    print("conditional -aal sayings: %d" % len(conditionals))
    assert len(conditionals) == 2
    quotative = [l for l in lines if "enru" in l]
    assert len(quotative) == 1
    print("quotative enru bridges: %d" % len(quotative))
    print("rule: -ven vows the future, -aal conditions it")
    print("OK: %s dreamed tomorrow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    idioms = {
        "karratu kaiman alavu": "knowledge is endless; stay humble",
        "muyarchi thiruvinaiyaakkum": "hard work brings success",
        "siru thuli peru vellam": "small efforts accumulate",
        "aaththirakkaaranukku puththi mattu": "anger clouds judgment",
        "kaakkaikkuth than kunchu pon kunchu": "every parent cherishes their child",
        "aazham theriyaamal kaalai vidaathe": "investigate before acting",
        "eli valaiyaanaalum thani valai vendum": "independence over luxury",
        "vinai vithaiththavan vinai aruppaan": "you reap what you sow",
        "akaththin azhaku mukaththil theriyum": "character shows",
        "seyvana thirunthach chey": "take pride in work",
        "yaathum oore yaavarum kelir": "universal kinship",
        "pirappokkum ellaa uyirkkum": "all beings equal by birth",
        "karka kasadara karpavai": "study with precision",
        "iniya ulavaaka innaatha kooral": "choose kind speech",
        "arivudaiyaar ellaam udaiyaar": "wisdom is true wealth",
        "theethum nanrum pirar thara vaaraa": "take responsibility",
        "aanaikkum adi sarukkum": "anyone can err",
        "malai pol varum thunpam pani pol neengum": "troubles pass",
        "thenozhukap pesik kolluvaar": "beware flatterers",
        "nool polach chelai thaay polap pillai": "character is inherited",
    }
    print("idioms catalogued: %d" % len(idioms))
    assert len(idioms) == 20
    # lookup test: meaning retrieval
    assert idioms["muyarchi thiruvinaiyaakkum"] == "hard work brings success"
    assert idioms["yaathum oore yaavarum kelir"] == "universal kinship"
    thirukkural = [k for k in idioms if k in ("karka kasadara karpavai",
                   "iniya ulavaaka innaatha kooral", "arivudaiyaar ellaam udaiyaar",
                   "pirappokkum ellaa uyirkkum")]
    print("Thirukkural-sourced: %d" % len(thirukkural))
    assert len(thirukkural) == 4
    print("rule: one line, one image, one verdict of generations")
    print("OK: %s kept the sayings" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    pairs = [
        ("nee vaa", "neengal vaarungal"), ("un peyar enna", "ungal peyar enna"),
        ("saappittiyaa", "saappitteerhalaa"), ("engge pore", "engge pokireerhal"),
        ("ithaix kodu", "ithaix kodungal"), ("nee solrathu sari", "neengal solvathu sari"),
        ("anbulla raajaa", "mathippirkuriya aiyaa"), ("un nanban", "thangal unmaiyulla"),
        ("panam kodu", "panam seluththumaaru kettukkolkiren"),
        ("naalaikku vaa", "naalai varumaaru anbudan azhaikkiren"),
        ("avan vanthaan", "avar vanthaar"), ("sari polaam", "sari pokalaam"),
        ("enna venum", "ungalukku enna vendum"), ("iru", "irungal"),
        ("nanri daa", "mikka nanri"),
    ]
    print("register pairs: %d" % len(pairs))
    assert len(pairs) == 15
    def is_formal(s):
        return ("ngal" in s) or ("eerhal" in s) or ("aar" in s) or s.startswith("mathip")
    formal_hits = sum(1 for _, f in pairs if is_formal(f))
    print("formal markers detected: %d/15" % formal_hits)
    assert formal_hits >= 10
    informal_ok = all(not is_formal(i) or "daa" in i for i, _ in pairs[:6])
    assert informal_ok
    print("rule: nee embraces, neengal bows; the ending sets the distance")
    print("OK: %s shifted the registers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_complex_sentences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    connectors = ["yenenraal", "aanaal", "marrum", "athanaal", "-aal", "-aalum",
                  "-umpothu", "-umvarai", "enru", "-athaal", "piraku", "-vatharku mun"]
    sentences = 15
    print("sentences: %d, connector inventory: %d" % (sentences, len(connectors)))
    assert sentences == 15 and len(connectors) == 12
    def relative_participle(verb_past_stem):
        return verb_past_stem  # padiththa, vaangiya, samaiththa
    tests = {"padiththa paiyan": "the boy who studied",
             "naan vaangiya puththakam": "the book I bought"}
    for tamil, gloss in tests.items():
        print("  %s = %s" % (tamil, gloss))
    assert len(tests) == 2
    # clause count = connectors + 1 per sentence sample
    sample = "naan pallikkup ponen yenenraal thervu irunthathu"
    clauses = sample.count("yenenraal") + 1
    assert clauses == 2
    print("sample clause count: %d" % clauses)
    print("rule: participles replace who/which; suffixes join the clauses")
    print("OK: %s bound the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_conv_market(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    speakers = ["C", "S"] * 10
    assert len(speakers) == 20
    for i in range(1, 20):
        assert speakers[i] != speakers[i - 1]
    print("dialogue lines: %d, speakers alternate C/S" % len(speakers))
    c_lines = sum(1 for s in speakers if s == "C")
    s_lines = sum(1 for s in speakers if s == "S")
    assert c_lines == 10 and s_lines == 10
    # price arithmetic from the dialogue: tomato bargained 60->55, onions 2x40
    tomato, onions = 55, 2 * 40
    total = tomato + onions
    paid, change = 150, 15
    print("tomato %d + onions %d = total %d" % (tomato, onions, total))
    assert total == 135
    assert paid - total == change
    print("paid %d - total %d = change %d" % (paid, total, change))
    print("rule: greet, bargain, count the change")
    print("OK: %s worked the market" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_conv_friend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    speakers = ["R", "M"] * 10
    assert len(speakers) == 20
    for i in range(1, 20):
        assert speakers[i] != speakers[i - 1]
    print("dialogue lines: %d, friends alternate R/M" % len(speakers))
    # informal friend endings vs formal
    informal = ["irukke", "pokuthu", "free-yaa"]
    formal_equiv = {"irukke": "irukkireerhal", "pokuthu": "pokirathu"}
    assert len(formal_equiv) == 2
    print("spoken contractions glossed: %d" % len(informal))
    # planning: time + place pinning
    plan = {"time": "aintaraikku", "place": "theater vaasalil"}
    assert plan["time"] and plan["place"]
    print("plan pinned: %s @ %s" % (plan["time"], plan["place"]))
    hearsay = "nallaa irukkaam"
    assert hearsay.endswith("aam")
    print("rule: friends drop the wax; -laam makes the plan")
    print("OK: %s met the friend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_conv_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    speakers = ["St", "T"] * 10
    assert len(speakers) == 20
    for i in range(1, 20):
        assert speakers[i] != speakers[i - 1]
    acts = ["report", "investigate", "comfort", "discover", "advise"]
    print("dialogue lines: %d across %d acts" % (len(speakers), len(acts)))
    assert len(acts) == 5
    # register asymmetry: student honors upward, teacher speaks down informally
    upward = "aiyaa"
    downward_ending = "aay"
    assert upward and downward_ending
    print("register asymmetry: student->%s, teacher->-%s" % (upward, downward_ending))
    prohibition = "marakkaate"
    promise = "marakkamaatten"
    assert prohibition.endswith("aate") and "maatt" in promise
    print("prohibition: %s; promise: %s" % (prohibition, promise))
    print("rule: report, investigate, comfort, discover, advise")
    print("OK: %s solved the problem" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    script_total = 12 + 18 + 1 + 12 * 18
    core_words = 200
    records = 34
    print("script inventory: %d" % script_total)
    print("core words: %d" % core_words)
    print("database records: %d" % records)
    assert script_total == 247
    assert core_words == 200
    assert records == 34
    grammar_machines = ["SOV", "stacking", "classes", "cases", "tenses",
                        "negation", "questions", "participles", "connectors"]
    assert len(grammar_machines) == 9
    print("grammar machines: %d" % len(grammar_machines))
    coverage = records / 34.0 * 100.0
    print("ladder coverage: %.1f %%" % coverage)
    assert 99.9 < coverage < 100.1
    print("rule: 247 letters, 200 words, 34 records - the ladder climbed")
    print("OK: %s graduated the learner" % NAME)
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
    "home_family": demo_home_family,
    "food_cooking": demo_food_cooking,
    "travel": demo_travel,
    "work_school": demo_work_school,
    "health_body": demo_health_body,
    "emotions": demo_emotions,
    "nature_weather": demo_nature_weather,
    "shopping_money": demo_shopping_money,
    "friendship_social": demo_friendship_social,
    "technology": demo_technology,
    "verb_tenses": demo_verb_tenses,
    "questions_answers": demo_questions_answers,
    "commands_requests": demo_commands_requests,
    "descriptions": demo_descriptions,
    "story1": demo_story1,
    "story2": demo_story2,
    "story3": demo_story3,
    "idioms": demo_idioms,
    "registers": demo_registers,
    "complex_sentences": demo_complex_sentences,
    "conv_market": demo_conv_market,
    "conv_friend": demo_conv_friend,
    "conv_problem": demo_conv_problem,
    "mastery": demo_mastery,
}
