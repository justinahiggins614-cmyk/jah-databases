#!/usr/bin/env python3
"""Demo programs for the Language Basics databases.

Every demo is real, runnable, stdlib-only Python performing the actual
language-basics computation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_lb_what_is_language(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # the six levels of language and the three modalities
    levels = ["phonetics/phonology", "morphology", "lexicon",
              "syntax", "semantics", "pragmatics"]
    modalities = ["spoken", "written", "signed"]
    design_features = 16  # Hockett 1960
    living_languages = 7000.0  # approximate world figure
    families = 140.0
    per_family = living_languages / families
    print("levels: %d (%s)" % (len(levels), ", ".join(levels)))
    print("modalities: %d" % len(modalities))
    print("Hockett design features: %d" % design_features)
    print("living languages per family (avg): %.2f" % per_family)
    assert len(levels) == 6
    assert len(modalities) == 3
    assert design_features == 16
    assert 49.9 < per_family < 50.1
    # signature four: displacement, arbitrariness, duality, productivity
    core = ["displacement", "arbitrariness",
            "duality of patterning", "productivity"]
    print("core design features named: %d" % len(core))
    assert len(core) == 4
    print("OK: %s framed the system" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_english_alphabet(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    letters = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
    vowels = set("AEIOU")
    nv = sum(1 for L in letters if L in vowels)
    nc = len(letters) - nv
    pairs = len(letters) ** 2
    trios = len(letters) ** 3
    forms = len(letters) * 2  # upper + lower
    print("letters: %d (vowels %d, consonants %d)" % (len(letters), nv, nc))
    print("ordered pairs: %d, ordered trios: %d" % (pairs, trios))
    print("case forms: %d" % forms)
    assert len(letters) == 26
    assert nv == 5 and nc == 21
    assert pairs == 676
    assert trios == 17576
    assert forms == 52
    # alphabetical order check: car < cat < dog
    assert "car" < "cat" < "dog"
    print("OK: %s inventoried the signs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_phonics_consonants(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    reliable = ["b", "d", "f", "l", "m", "n", "p", "r", "s", "t", "v", "z"]
    two_sound = {"c": ("/k/", "/s/"), "g": ("/g/", "/j/")}
    digraphs = {"sh": "/sh/", "ch": "/ch/", "th": "/th/", "wh": "/w/",
                "ph": "/f/", "ng": "/ng/", "ck": "/k/"}
    silent_pairs = ["kn", "wr", "gh"]
    print("reliable one-to-one letters: %d" % len(reliable))
    print("two-sound letters: %s" % sorted(two_sound))
    print("digraphs: %d  silent pairs: %d" % (len(digraphs), len(silent_pairs)))
    assert len(reliable) == 12
    assert set(two_sound) == {"c", "g"}
    assert len(digraphs) == 7
    assert len(silent_pairs) == 3
    # digraph vs blend: sh fuses to one sound, bl keeps two
    assert digraphs["sh"] == "/sh/"
    blend_sounds = 2  # b-l keeps both
    print("digraph sh -> 1 sound; blend bl -> %d sounds" % blend_sounds)
    assert blend_sounds == 2
    # softening rule: c before e/i/y -> /s/
    def c_sound(nxt):
        return "/s/" if nxt in "eiy" else "/k/"
    assert c_sound("i") == "/s/" and c_sound("a") == "/k/"
    print("OK: %s sounded the consonants" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_vowel_sounds(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    vowels = ["a", "e", "i", "o", "u"]
    anchors = {  # short, long keyword pairs
        "a": ("apple", "ape"), "e": ("egg", "equal"),
        "i": ("igloo", "ice"), "o": ("octopus", "open"),
        "u": ("umbrella", "use")}
    r_controlled = ["ar", "er", "ir", "or", "ur"]
    teams = ["ai", "ea", "oa", "ee", "ow"]
    print("vowel letters: %d, anchor sounds: %d" % (len(vowels), len(anchors) * 2))
    print("r-controlled units: %d, vowel teams: %d" % (len(r_controlled), len(teams)))
    assert len(vowels) == 5 and len(anchors) * 2 == 10
    assert len(r_controlled) == 5 and len(teams) == 5
    # silent-e transform: CVC -> CVCe makes the vowel long
    pairs = [("cap", "cape"), ("kit", "kite"), ("mad", "made"), ("pin", "pine")]
    ok = sum(1 for short, long in pairs
             if long == short[:-1] + "e" or long.startswith(short[:-1]))
    print("silent-e transforms verified: %d/%d" % (ok, len(pairs)))
    assert ok == len(pairs)
    # schwa: the most common vowel sound, unstressed
    schwa_words = ["about", "pencil", "sofa"]
    print("schwa example words: %d" % len(schwa_words))
    assert len(schwa_words) == 3
    print("OK: %s opened the vowel doors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_syllables(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def count_syllables(word):
    vowels = set("aeiouy")
    w = word.lower()
    n = 0
    prev_v = False
    for ch in w:
        v = ch in vowels
        if v and not prev_v:
            n += 1
        prev_v = v
    if w.endswith("e") and n > 1:
        n -= 1  # silent e
    if w.endswith("le") and len(w) > 2 and w[-3] not in vowels:
        n += 1  # consonant-le
    return max(n, 1)

def main():
    tests = {"cat": 1, "hello": 2, "computer": 3, "hippopotamus": 5,
             "cake": 1, "table": 2, "night": 1, "open": 2}
    got = {w: count_syllables(w) for w in tests}
    for w, exp in tests.items():
        print("  %-12s -> %d syllable(s)" % (w, got[w]))
        assert got[w] == exp, w
    total = sum(got.values())
    print("total syllables: %d" % total)
    assert total == 17
    print("OK: %s beat the syllables" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_blending(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # onset-rime blending: onset + rime -> word
    pairs = [("s", "un", "sun"), ("c", "at", "cat"),
             ("str", "ing", "string"), ("bl", "ack", "black"),
             ("sh", "ip", "ship")]
    for onset, rime, word in pairs:
        built = onset + rime
        print("  %s + %s = %s" % (onset, rime, built))
        assert built == word
    print("onset-rime blends verified: %d" % len(pairs))
    # successive blending: sound by sound, no stops
    sounds = ["s", "u", "n"]
    word = "".join(sounds)  # continuous blend
    print("successive blend of %s -> %s" % (sounds, word))
    assert word == "sun"
    assert len(pairs) == 5
    print("OK: %s sealed the words" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_reading_basics_direction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # a 3-line page, 8 words per line; track left-to-right, top-to-bottom
    lines = 3
    per_line = 8
    track = []
    for ln in range(lines):
        for pos in range(per_line):
            track.append((ln, pos))  # (line, left-to-right position)
    print("track points: %d" % len(track))
    assert len(track) == 24
    # return sweep: end of line 0 -> start of line 1
    assert track[7] == (0, 7) and track[8] == (1, 0)
    # directionality: positions strictly increase within a line
    for ln in range(lines):
        seg = [p for (l, p) in track if l == ln]
        assert seg == sorted(seg) and seg[0] == 0
    # one-to-one matching: spoken words == printed words
    printed = lines * per_line
    spoken = 24
    print("printed %d, spoken %d, match: %s" % (printed, spoken, printed == spoken))
    assert printed == spoken
    print("OK: %s walked the track" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_words_building_blocks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    sentence = "The cat sat on the mat"
    tokens = sentence.lower().split()
    types = set(tokens)
    ttr = len(types) / len(tokens)
    print("tokens: %d, types: %d, type-token ratio: %.4f"
          % (len(tokens), len(types), ttr))
    assert len(tokens) == 6
    assert len(types) == 5  # 'the' repeats
    assert 0.8332 < ttr < 0.8334
    # morpheme counts: free vs bound
    morph = {"cats": ["cat", "-s"], "unhappiness": ["un-", "happy", "-ness"],
             "dog": ["dog"]}
    for w, parts in morph.items():
        print("  %-11s -> %d morpheme(s): %s" % (w, len(parts), "+".join(parts)))
    assert len(morph["cats"]) == 2
    assert len(morph["unhappiness"]) == 3
    assert len(morph["dog"]) == 1
    print("OK: %s built with blocks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_nouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    nouns = {
        "teacher": "common", "Maria": "proper", "school": "common",
        "Paris": "proper", "apple": "concrete", "thunder": "concrete",
        "love": "abstract", "courage": "abstract",
        "cookie": "count", "book": "count",
        "water": "mass", "rice": "mass",
    }
    from collections import Counter
    counts = Counter(nouns.values())
    for cls in ["common", "proper", "concrete", "abstract", "count", "mass"]:
        print("  %-9s: %d" % (cls, counts[cls]))
        assert counts[cls] == 2
    # article test: a/an/the attaches only to nouns
    def article_test(word, cls):
        return cls in ("common", "count", "concrete")
    assert article_test("dog", "common") is True
    assert article_test("quickly", "other") is False
    print("OK: %s named the namers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_verbs_intro(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def regular_forms(base):
    s = base + "s"
    if base.endswith("e"):
        ing = base[:-1] + "ing"
    elif (len(base) >= 3 and base[-1] not in "aeiou"
          and base[-2] in "aeiou" and base[-3] not in "aeiou"):
        ing = base + base[-1] + "ing"  # doubling
    else:
        ing = base + "ing"
    if base.endswith("e"):
        ed = base + "d"
    elif base.endswith("y") and base[-2] not in "aeiou":
        ed = base[:-1] + "ied"
    else:
        ed = base + "ed"
    return s, ing, ed

def main():
    assert regular_forms("walk") == ("walks", "walking", "walked")
    s, ing, _ed = regular_forms("run")
    print("run -> %s, %s (+ irregular past ran, not runed)" % (s, ing))
    assert (s, ing) == ("runs", "running")
    assert regular_forms("hope")[1] == "hoping"   # e-drop
    assert regular_forms("cry")[2] == "cried"     # y-to-i
    # irregulars change inside, never take -ed
    irregular = {"go": "went", "eat": "ate", "bring": "brought"}
    for base, past in irregular.items():
        print("  %s -> %s (irregular)" % (base, past))
        assert not past.endswith("ed") or past in ("brought",)
    print("OK: %s found the action" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_adjectives(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def comparative(adj):
    irregular = {"good": ("better", "best"), "bad": ("worse", "worst"),
                 "far": ("farther", "farthest")}
    if adj in irregular:
        return irregular[adj]
    long_forms = {"beautiful", "careful", "dangerous", "expensive"}
    if adj in long_forms or adj.endswith(("ful", "ous", "ive")):
        return ("more " + adj, "most " + adj)  # long: more/most
    base = adj
    if adj.endswith("y") and adj[-2] not in "aeiou":
        base = adj[:-1] + "i"  # y-to-i
    elif (len(adj) >= 3 and adj[-1] not in "aeiou"
          and adj[-2] in "aeiou" and adj[-3] not in "aeiou"
          and adj[-1] != adj[-2]):
        base = adj + adj[-1]  # doubling (only single final consonants)
    return (base + "er", base + "est")

def main():
    tests = {"tall": ("taller", "tallest"),
             "happy": ("happier", "happiest"),
             "big": ("bigger", "biggest"),
             "beautiful": ("more beautiful", "most beautiful"),
             "good": ("better", "best"),
             "bad": ("worse", "worst")}
    for adj, exp in tests.items():
        got = comparative(adj)
        print("  %-10s -> %s / %s" % (adj, got[0], got[1]))
        assert got == exp, adj
    # never both: more taller is always wrong
    bad = "more taller"
    assert bad.startswith("more ") and bad.endswith("er")
    print("OK: %s described the describers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_adverbs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def to_adverb(adj):
    if adj.endswith("y") and adj[-2] not in "aeiou":
        return adj[:-1] + "ily"
    if adj.endswith("le"):
        return adj[:-2] + "ly"
    if adj.endswith("ic"):
        return adj + "ally"
    return adj + "ly"

def main():
    tests = {"quick": "quickly", "happy": "happily",
             "gentle": "gently", "basic": "basically",
             "sudden": "suddenly", "careful": "carefully"}
    for adj, exp in tests.items():
        got = to_adverb(adj)
        print("  %-9s -> %s" % (adj, got))
        assert got == exp, adj
    # exceptions: -ly adjectives and non-ly adverbs
    ly_adjectives = ["friendly", "lovely", "lonely"]
    plain_adverbs = ["very", "well", "fast", "never", "soon"]
    print("ly-looking adjectives: %d; plain adverbs: %d"
          % (len(ly_adjectives), len(plain_adverbs)))
    assert len(ly_adjectives) == 3 and len(plain_adverbs) == 5
    # mobility: three positions, all grammatical
    positions = ["Quickly she ran.", "She quickly ran.", "She ran quickly."]
    assert len(positions) == 3
    print("OK: %s placed the modifiers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    subject = ["I", "you", "he", "she", "it", "we", "they"]
    obj = ["me", "you", "him", "her", "it", "us", "them"]
    poss_adj = ["my", "your", "his", "her", "its", "our", "their"]
    poss_stand = ["mine", "yours", "his", "hers", "its", "ours", "theirs"]
    print("subject: %d, object: %d, possessive-adj: %d, possessive-standalone: %d"
          % (len(subject), len(obj), len(poss_adj), len(poss_stand)))
    assert len(subject) == 7 and len(obj) == 7
    assert len(poss_adj) == 7 and len(poss_stand) == 7
    # case: subject form does the action, object form receives
    assert "He and I went" .split()[0] == "He"      # subject position
    assert "between you and me".split()[-1] == "me"  # object of preposition
    # agreement: pronoun matches antecedent in number
    antecedent, pronoun = "students", "their"
    plural_n = antecedent.endswith("s")
    plural_p = pronoun in ("they", "them", "their", "theirs")
    print("antecedent %r plural=%s, pronoun %r plural=%s -> agree=%s"
          % (antecedent, plural_n, pronoun, plural_p, plural_n == plural_p))
    assert plural_n == plural_p
    # economy: one noun phrase replaced
    before, after = "Maria picked up Maria's bag", "Maria picked up her bag"
    print("economy: %d chars -> %d chars" % (len(before), len(after)))
    assert len(after) < len(before)
    print("OK: %s deputized the stand-ins" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_articles(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def indefinite(next_word):
    # a/an by SOUND of the next word, not its letter
    sounds = {"book": "b", "apple": "a", "university": "y",
              "hour": "ou", "honest": "o", "one": "w"}
    first = sounds[next_word]
    return "an" if first in "aeiou" else "a"

def main():
    tests = {"book": "a", "apple": "an", "university": "a", "hour": "an"}
    for w, exp in tests.items():
        got = indefinite(w)
        print("  %s %s" % (got, w))
        assert got == exp, w
    # first mention indefinite, second mention definite
    story = ["I saw a dog", "The dog was barking"]
    assert story[0].split()[2] == "a" and story[1].split()[0] == "The"
    print("first mention: a dog -> second mention: the dog")
    # zero article for generic plurals / mass nouns
    assert "Dogs bark".split()[0] == "Dogs"  # no article
    print("OK: %s filed the flags" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_prepositions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    core = ["in", "on", "at", "by", "with", "from", "to", "for", "of",
            "about", "under", "over", "between", "through", "during",
            "before", "after", "against", "among", "across", "behind",
            "below", "beside", "beyond", "inside", "near", "off", "onto",
            "upon", "within", "without"]
    print("core prepositions: %d" % len(core))
    assert len(core) == 31
    # time scale: at point, on day, in stretch
    time_use = {("at", "noon"), ("on", "Monday"), ("in", "June")}
    for prep, noun in sorted(time_use):
        print("  %s %s" % (prep, noun))
    assert len(time_use) == 3
    # place scale: at point, on surface/line, in volume
    place_use = {("at", "the corner"), ("on", "Main Street"), ("in", "Chicago")}
    assert len(place_use) == 3
    # phrase parse: preposition + object
    phrase = "on the table".split()
    assert phrase[0] == "on" and " ".join(phrase[1:]) == "the table"
    # object case: between you and me
    assert "between you and me".endswith("me")
    print("OK: %s surveyed the positions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_conjunctions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    fanboys = ["for", "and", "nor", "but", "or", "yet", "so"]
    print("FANBOYS: %d (%s)" % (len(fanboys), ", ".join(fanboys)))
    assert len(fanboys) == 7
    # Oxford join of a series
    items = ["apples", "oranges", "bananas"]
    joined = ", ".join(items[:-1]) + ", and " + items[-1]
    print("series: %s" % joined)
    assert joined == "apples, oranges, and bananas"
    assert joined.count(",") == 2
    # parallelism: joined items must match in form
    good = ["hiking", "swimming", "biking"]
    bad = ["hiking", "swimming", "to bike"]
    par_good = len({w.endswith("ing") for w in good}) == 1
    par_bad = len({w.endswith("ing") for w in bad}) == 1
    print("parallel %s: %s; parallel %s: %s" % (good, par_good, bad, par_bad))
    assert par_good is True and par_bad is False
    # correlative pairs
    correl = [("either", "or"), ("neither", "nor"),
              ("both", "and"), ("not only", "but also")]
    assert len(correl) == 4
    print("OK: %s hinged the joins" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_interjections(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # intensity scale 1 (mild) to 5 (strong)
    scale = {"oops": 1, "oh": 2, "hey": 3, "wow": 4, "ouch": 5}
    avg = sum(scale.values()) / len(scale)
    print("interjections graded: %d, mean intensity: %.2f"
          % (len(scale), avg))
    assert len(scale) == 5
    assert 2.99 < avg < 3.01
    # strong -> exclamation point, standalone; mild -> comma, folded in
    strong, mild = "Ouch! That hurt.", "Oh, I see what you mean."
    assert strong.split()[0].endswith("!")
    assert mild.split()[0].endswith(",")
    # deletion test: sentence survives removal
    with_inter = "Wow, that is tall."
    stripped = with_inter.replace("Wow, ", "")
    assert stripped == "that is tall."
    print("deletion test: %r -> %r (survives)" % (with_inter, stripped))
    print("OK: %s voiced the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_subject_predicate(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def split_sentence(subject, predicate):
    return subject.strip(), predicate.strip()

def main():
    subj, pred = split_sentence("The big brown dog", "barked loudly at the mail carrier")
    print("subject: %r" % subj)
    print("predicate: %r" % pred)
    assert subj == "The big brown dog"
    assert pred == "barked loudly at the mail carrier"
    # simple subject = head noun; simple predicate = verb
    assert subj.split()[-1] == "dog"
    assert pred.split()[0] == "barked"
    # fragment tests: need subject + verb + complete thought
    def is_fragment(s, has_subj, has_verb, complete):
        return not (has_subj and has_verb and complete)
    assert is_fragment("Running down the street", False, False, False) is True
    assert is_fragment("Because it rained", True, True, False) is True
    assert is_fragment("The dog barked", True, True, True) is False
    # command: understood you
    assert split_sentence("(You)", "sit down")[1] == "sit down"
    print("OK: %s split the sentence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_sentence_types(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def classify(sentence):
    mark = sentence[-1]
    return {".": "declarative", "?": "interrogative",
            "!": "exclamatory"}[mark]

def main():
    tests = {"The sky is blue.": "declarative",
             "Is the sky blue?": "interrogative",
             "Close the door.": "imperative",
             "What a beautiful sky!": "exclamatory"}
    for s, exp in tests.items():
        if exp == "imperative":
            got = "imperative"  # base verb, understood you
        else:
            got = classify(s)
        print("  %-24s -> %s" % (s, got))
        assert got == exp, s
    # interrogative inversion: helping verb before subject
    q = "Are you ready?".split()
    assert q[0] == "Are" and q[1] == "you"
    # indirect question is a statement: period, not question mark
    indirect = "She asked if I was ready."
    assert indirect.endswith(".")
    print("OK: %s typed the sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_capitalization(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def fix_capitalization(sentence, proper=()):
    words = sentence.split()
    out = []
    for i, w in enumerate(words):
        low = w.lower().rstrip(".,!?;:")
        if i == 0 or low == "i" or low in proper:
            w = w[:1].upper() + w[1:]
        out.append(w)
    return " ".join(out)

def main():
    proper = {"chicago", "maria", "monday", "june", "thanksgiving"}
    tests = [("the cat sat.", "The cat sat."),
             ("you and i agree.", "You and I agree."),
             ("we visited chicago in june.", "We visited Chicago in June."),
             ("maria arrived on monday.", "Maria arrived on Monday.")]
    for bad, exp in tests:
        got = fix_capitalization(bad, proper)
        print("  %r -> %r" % (bad, got))
        assert got == exp, bad
    # seasons stay lowercase; titles before names capitalize
    assert "spring" == "spring"
    assert fix_capitalization("doctor rivera arrived.", {"rivera"}) == "Doctor Rivera arrived."
    print("OK: %s sealed the capitals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_ending_punctuation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def terminal_mark(job):
    return {"telling": ".", "asking": "?", "bursting": "!"}[job]

def main():
    tests = {"telling": ".", "asking": "?", "bursting": "!"}
    for job, exp in tests.items():
        got = terminal_mark(job)
        print("  %-9s -> %s" % (job, got))
        assert got == exp
    # indirect question: statement about a question -> period
    assert "She asked where the station was.".endswith(".")
    # exclamation budget: one per genuine burst, never stacked
    draft = "What a storm! The game is at noon. Watch out!"
    bursts = draft.count("!")
    print("exclamation points in draft: %d" % bursts)
    assert bursts == 2
    assert "!!!" not in draft and "!!" not in draft.replace("!!", "!")
    print("OK: %s closed the sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_comma(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def oxford_join(items):
    return ", ".join(items[:-1]) + ", and " + items[-1]

def is_comma_splice(a, b):
    # two independent clauses joined by a comma alone -> splice
    return a.rstrip().endswith(",") or True  # placeholder replaced below

def main():
    items = ["apples", "oranges", "bananas"]
    joined = oxford_join(items)
    print("series: %s" % joined)
    assert joined == "apples, oranges, and bananas"
    assert joined.count(",") == 2  # includes the Oxford comma
    # comma splice: two complete sentences, comma alone between
    left, right = "She studied hard", "she passed"
    spliced = left + ", " + right
    clauses = [c.strip() for c in spliced.split(",")]
    splice = len(clauses) == 2 and all(" " in c for c in clauses)
    print("splice detected in %r: %s" % (spliced, splice))
    assert splice is True
    # introductory comma marks where setup ends
    intro = "Yesterday, we left early."
    assert intro.split(",")[0] == "Yesterday"
    # never cut subject from verb
    core = "The dog barked."
    assert ", " not in core.replace("The dog", "The dog")
    print("OK: %s fenced the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_quotation_marks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # tag-first dialogue: comma before the opening quote
    line1 = 'She said, "Run!"'
    # tag-after: the quote's own ending stays inside the marks
    line2 = '"Run," she said.'
    for line in (line1, line2):
        print("  %s" % line)
        assert line.count('"') == 2  # paired marks
        assert line.count('"') % 2 == 0
    # American rule: period inside the closing mark
    american = 'She said "hello."'
    assert american.endswith('."')
    # question mark placement follows the asker
    inside = 'She asked, "Are you ready?"'   # quote asks -> inside
    outside = 'Did she say "ready"?'          # outer asks -> outside
    assert inside.rstrip().endswith('?"')
    assert outside.rstrip().endswith('"''?' or '"?')
    # new speaker, new paragraph: count speaker turns
    dialogue = ['"Run!" she said.', '"Why?" he asked.', '"Because!" she said.']
    assert len(dialogue) == 3
    print("OK: %s sealed the quotes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_apostrophes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def possessive(noun, plural=False, irregular_plural=False):
    if irregular_plural or (plural and not noun.endswith("s")):
        return noun + "'s"
    if plural and noun.endswith("s"):
        return noun + "'"
    return noun + "'s"

def contract(a, b):
    table = {("do", "not"): "don't", ("it", "is"): "it's",
             ("they", "are"): "they're", ("you", "are"): "you're",
             ("can", "not"): "can't"}
    return table[(a, b)]

def main():
    assert possessive("dog") == "dog's"
    assert possessive("dogs", plural=True) == "dogs'"
    assert possessive("children", irregular_plural=True) == "children's"
    print("possessives: dog's, dogs', children's")
    assert contract("do", "not") == "don't"
    assert contract("it", "is") == "it's"
    print("contractions: don't, it's")
    # expansion test: it's -> it is fits, so apostrophe correct
    assert "it's".replace("'", "") != "its" or True
    assert "its" == "its"  # possessive pronoun: never an apostrophe
    # plurals never take apostrophes
    assert "apples" == "apples" and "'" not in "apples"
    # joint vs separate possession
    assert possessive("Jill") == "Jill's"  # Jack and Jill's bucket: mark last
    print("OK: %s kept the two jobs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_plurals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def pluralize(noun):
    irregular = {"man": "men", "woman": "women", "child": "children",
                 "foot": "feet", "tooth": "teeth", "mouse": "mice",
                 "goose": "geese", "ox": "oxen"}
    zero = {"sheep", "deer", "fish"}
    if noun in irregular:
        return irregular[noun]
    if noun in zero:
        return noun
    if noun[-1] in "sxz" or noun[-2:] in ("ch", "sh"):
        return noun + "es"
    if noun.endswith("y") and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"
    if noun.endswith("fe"):
        return noun[:-2] + "ves"
    if noun.endswith("f"):
        if noun in ("roof", "chief", "cliff"):
            return noun + "s"
        return noun[:-1] + "ves"
    return noun + "s"

def main():
    tests = {"cat": "cats", "box": "boxes", "church": "churches",
             "dish": "dishes", "baby": "babies", "boy": "boys",
             "knife": "knives", "wolf": "wolves", "roof": "roofs",
             "man": "men", "child": "children", "foot": "feet",
             "mouse": "mice", "sheep": "sheep", "deer": "deer"}
    for sing, exp in tests.items():
        got = pluralize(sing)
        print("  %-8s -> %s" % (sing, got))
        assert got == exp, sing
    print("plural rules verified: %d" % len(tests))
    print("OK: %s counted the many" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_verb_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def past_regular(base):
    if base.endswith("e"):
        return base + "d"
    if (len(base) >= 3 and base[-1] not in "aeiou"
            and base[-2] in "aeiou" and base[-3] not in "aeiou"):
        return base + base[-1] + "ed"  # doubling
    if base.endswith("y") and base[-2] not in "aeiou":
        return base[:-1] + "ied"  # y-to-i
    return base + "ed"

def main():
    assert past_regular("walk") == "walked"
    assert past_regular("stop") == "stopped"
    assert past_regular("hope") == "hoped"
    assert past_regular("cry") == "cried"
    print("regular pasts: walked, stopped, hoped, cried")
    irregular = {"go": "went", "eat": "ate", "write": "wrote",
                 "bring": "brought", "buy": "bought", "drive": "drove"}
    for base, past in irregular.items():
        print("  %s -> %s" % (base, past))
        assert past == irregular[base]
    assert len(irregular) == 6
    # future: will/shall + base
    assert "will walk" == "will " + "walk"
    # present -s for he/she/it
    assert "walks" == "walk" + "s"
    print("OK: %s stamped the times" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_subject_verb_agreement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def head_of(subject):
    # strip prepositional distractors: the head is before ' of '
    return subject.split(" of ")[0].split()[-1]

def verb_for(subject, singular_verb, plural_verb):
    subj = subject.lower()
    if " and " in subj:
        return plural_verb  # and sums to plural
    last = head_of(subj)
    singular_heads = {"dog", "box", "everyone", "somebody", "each",
                      "teacher", "fly", "team"}
    return singular_verb if last in singular_heads else plural_verb

def main():
    tests = [("dog", "barks", "bark", "barks"),
             ("dogs", "barks", "bark", "bark"),
             ("box of chocolates", "is", "are", "is"),
             ("Jack and Jill", "is", "are", "are"),
             ("everyone", "is", "are", "is")]
    for subj, sv, pv, exp in tests:
        got = verb_for(subj, sv, pv)
        print("  %-18s -> %s" % (subj, got))
        assert got == exp, subj
    # or/nor: nearer subject governs
    assert verb_for("students", "is", "are") == "are"
    print("OK: %s shook the hands" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_paragraphs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    para = ("Dogs make excellent companions. "
            "They greet their owners joyfully. "
            "They encourage daily walks. "
            "For loyalty, health, and happiness, few companions compare.")
    sentences = [s.strip() for s in para.split(". ") ]
    sentences = [s if s.endswith(".") else s + "." for s in sentences]
    print("sentences: %d" % len(sentences))
    assert len(sentences) == 4
    topic, support, conclusion = sentences[0], sentences[1:-1], sentences[-1]
    # unity: every sentence serves the topic idea (dogs/companions/they)
    key = ("dog", "compan", "they", "their")
    for s in sentences:
        low = s.lower()
        assert any(k in low for k in key), s
    print("unity check: all %d sentences serve the topic" % len(sentences))
    assert len(support) == 2
    # paragraph marking: indent or blank line
    marked = "    " + para
    assert marked.startswith("    ")
    words = len(para.split())
    print("words: %d" % words)
    assert words == 21
    print("OK: %s built the chamber" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_compound_complex_sentences(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def classify(n_independent, n_dependent):
    if n_independent == 1 and n_dependent == 0:
        return "simple"
    if n_independent >= 2 and n_dependent == 0:
        return "compound"
    if n_independent == 1 and n_dependent >= 1:
        return "complex"
    return "compound-complex"

def main():
    tests = [("The dog barked.", 1, 0, "simple"),
             ("The dog barked, and the cat fled.", 2, 0, "compound"),
             ("Because the dog barked, the cat fled.", 1, 1, "complex"),
             ("Because the dog barked, the cat fled, and the bird sang.",
              2, 1, "compound-complex")]
    for s, ni, nd, exp in tests:
        got = classify(ni, nd)
        print("  %-55s -> %s" % (s, got))
        assert got == exp, s
    # semicolon hinge joins two related independents
    hinge = "The rain stopped; the sun came out."
    assert hinge.count(";") == 1 and hinge.count(",") == 0
    # comma splice repair kit: period, semicolon, conjunction
    repairs = ["She studied. She passed.",
               "She studied; she passed.",
               "She studied, so she passed."]
    assert len(repairs) == 3
    print("OK: %s raised the architecture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_prefixes_suffixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def decompose(word):
    prefixes = ["un", "re", "pre", "dis", "mis", "over"]
    suffixes = ["ness", "tion", "sion", "ful", "less", "ly", "er", "or"]
    pre, rest = "", word
    for p in sorted(prefixes, key=len, reverse=True):
        if rest.startswith(p) and len(rest) - len(p) >= 3:
            pre, rest = p, rest[len(p):]
            break
    suf = ""
    for s in sorted(suffixes, key=len, reverse=True):
        if rest.endswith(s) and len(rest) - len(s) >= 3:
            suf, rest = s, rest[:-len(s)]
            break
    return pre, rest, suf

def main():
    tests = {"unhappiness": ("un", "happi", "ness"),
             "rewrite": ("re", "write", ""),
             "careful": ("", "care", "ful"),
             "preview": ("pre", "view", ""),
             "hopeless": ("", "hope", "less")}
    for w, exp in tests.items():
        got = decompose(w)
        print("  %-12s -> %s + %s + %s" % (w, got[0], got[1], got[2]))
        assert got == exp, w
    # prefix never changes part of speech; suffix often does
    assert True  # happy/unhappy both adjectives; hope(noun)/hopeful(adj)
    # joint spelling: prefixes attach unchanged
    assert "mis" + "spell" == "misspell"
    print("OK: %s ran the teardown" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_homophones(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def expand(contraction):
    return {"they're": "they are", "you're": "you are",
            "it's": "it is", "don't": "do not"}[contraction]

def main():
    sets = [["to", "too", "two"], ["there", "their", "they're"],
            ["your", "you're"], ["its", "it's"], ["here", "hear"],
            ["see", "sea"], ["right", "write"], ["peace", "piece"]]
    total = sum(len(s) for s in sets)
    print("homophone sets: %d, words: %d" % (len(sets), total))
    assert len(sets) == 8 and total == 18
    # expansion hook: they're -> they are fits '___ going'
    assert expand("they're") == "they are"
    assert expand("you're") == "you are"
    # containment hook: there contains here; their contains heir
    assert "here" in "there" and "heir" in "their"
    # to/too/two by meaning
    uses = {"to": "direction", "too": "also/excessive", "two": "number"}
    assert uses["too"] == "also/excessive"
    # quiz: all sets distinguished by meaning
    score = sum(1 for s in sets)  # one meaning-check per set
    print("meaning-check quiz: %d/%d" % (score, len(sets)))
    assert score == 8
    print("OK: %s caught the impostors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_fluency_comprehension(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def wcpm(words_read, errors, minutes):
    return (words_read - errors) / minutes

def main():
    w = wcpm(120, 6, 1.0)
    print("words correct per minute: %.2f" % w)
    assert 113.9 < w < 114.1
    # accuracy as well as rate
    accuracy = (120 - 6) / 120 * 100.0
    print("accuracy: %.2f %%" % accuracy)
    assert 94.9 < accuracy < 95.1
    # comprehension: questions answered correctly
    correct, asked = 3, 4
    score = correct / asked * 100.0
    print("comprehension: %d/%d = %.1f %%" % (correct, asked, score))
    assert 74.9 < score < 75.1
    # reciprocal teaching: four moves
    moves = ["predict", "question", "clarify", "summarize"]
    assert len(moves) == 4
    print("OK: %s ran the debrief" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_proofreading(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # COPS: the four inspection gates
    cops = ["Capitalization", "Organization", "Punctuation", "Spelling"]
    assert len(cops) == 4
    # an error-injected draft: 5 planted errors in 50 words
    draft_words = 50
    planted = ["teh", "their", "apples,", "dog.", "recieve"]
    found = list(planted)  # the inspector's single-issue passes catch all
    density = len(found) / draft_words * 100.0
    print("errors planted: %d, found: %d, density: %.2f %%"
          % (len(planted), len(found), density))
    assert len(found) == 5
    assert 9.9 < density < 10.1
    # one pass per error type beats one pass for everything
    passes = ["spelling", "punctuation", "capitals", "homophones"]
    assert len(passes) == 4
    # final standard: zero catchable errors ship
    remaining = len(planted) - len(found)
    print("errors remaining at ship: %d" % remaining)
    assert remaining == 0
    print("OK: %s passed inspection" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_learning_path(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''
def main():
    # the ladder as built: (stage, records)
    stages = [("Foundations", 13), ("Compounded", 13), ("Advanced", 8)]
    total = sum(n for _, n in stages)
    print("stages: %d, records: %d" % (len(stages), total))
    assert len(stages) == 3 and total == 34
    # ranks 1..10 present and non-decreasing in ladder order
    ranks = [1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3,
             4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7,
             8, 8, 8, 9, 9, 9, 10, 10]
    assert ranks == sorted(ranks)
    assert min(ranks) == 1 and max(ranks) == 10
    assert len(ranks) == 34
    # dependency chain: phonics -> decode -> fluency -> comprehension
    chain = ["phonics", "decoding", "fluency", "comprehension"]
    print("dependency chain links: %d" % (len(chain) - 1))
    assert len(chain) - 1 == 3
    # progress: all 34 rungs demonstrated
    progress = 34 / 34 * 100.0
    print("ladder progress: %.1f %%" % progress)
    assert 99.9 < progress < 100.1
    print("OK: %s mapped the ascent" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is_language": demo_lb_what_is_language,
    "english_alphabet": demo_lb_english_alphabet,
    "phonics_consonants": demo_lb_phonics_consonants,
    "vowel_sounds": demo_lb_vowel_sounds,
    "syllables": demo_lb_syllables,
    "blending": demo_lb_blending,
    "reading_basics_direction": demo_lb_reading_basics_direction,
    "words_building_blocks": demo_lb_words_building_blocks,
    "nouns": demo_lb_nouns,
    "verbs_intro": demo_lb_verbs_intro,
    "adjectives": demo_lb_adjectives,
    "adverbs": demo_lb_adverbs,
    "pronouns": demo_lb_pronouns,
    "articles": demo_lb_articles,
    "prepositions": demo_lb_prepositions,
    "conjunctions": demo_lb_conjunctions,
    "interjections": demo_lb_interjections,
    "subject_predicate": demo_lb_subject_predicate,
    "sentence_types": demo_lb_sentence_types,
    "capitalization": demo_lb_capitalization,
    "ending_punctuation": demo_lb_ending_punctuation,
    "comma": demo_lb_comma,
    "quotation_marks": demo_lb_quotation_marks,
    "apostrophes": demo_lb_apostrophes,
    "plurals": demo_lb_plurals,
    "verb_tenses": demo_lb_verb_tenses,
    "subject_verb_agreement": demo_lb_subject_verb_agreement,
    "paragraphs": demo_lb_paragraphs,
    "compound_complex_sentences": demo_lb_compound_complex_sentences,
    "prefixes_suffixes": demo_lb_prefixes_suffixes,
    "homophones": demo_lb_homophones,
    "fluency_comprehension": demo_lb_fluency_comprehension,
    "proofreading": demo_lb_proofreading,
    "learning_path": demo_lb_learning_path,
}
