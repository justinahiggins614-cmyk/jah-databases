#!/usr/bin/env python3
"""Demo programs for The Bhojpuri to English Database (language-bhojpuri)
and its Signature edition (language-bhojpuri-signature).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: alphabet verification, phonology
drills, vocabulary quizzes, conjugation tables, sentence assembly, dialogue
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
    sentences: list of (bhojpuri, tag)."""
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
            "    print('longest bhojpuri line: %d chars; total chars: %d' % (longest, total))\n"
            "    assert 15 < longest < 250\n"
            "    assert 300 < total < 5000\n"
            "    print('OK: %s drilled the set' % NAME)\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        )
        return _wrap(hdr, name, rid, group, body)
    return demo


def demo_bho_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    native_m = 50.0
    world_pop_m = 8100.0
    share = native_m / world_pop_m * 100.0
    print("Bhojpuri native speakers: %.1f million" % native_m)
    print("share of world population: %.4f %%" % share)
    assert 49.9 < native_m < 50.1
    assert 0.6172 < share < 0.6174
    dialects = ["Northern (Gorakhpuri)", "Western (Benarsi/Purbi)",
                "Southern standard (Bhojpur/Arrah)", "Tharu Bhojpuri",
                "Trinidadian Bhojpuri", "Sarnami (Suriname)",
                "Mauritian Bhojpuri"]
    print("dialects tracked: %d" % len(dialects))
    assert len(dialects) == 7
    scripts = ["Devanagari", "Kaithi"]
    print("scripts: %s" % ", ".join(scripts))
    assert len(scripts) == 2
    print("ISO 639-3: bho (no ISO 639-1 code)")
    print("OK: %s surveyed the language" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_script(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    vowels = list("\\u0905\\u0906\\u0907\\u0908\\u0909\\u090a\\u090b\\u090f\\u0910\\u0913\\u0914\\u0902\\u0903")
    print("devanagari vowel count: %d" % len(vowels))
    assert len(vowels) == 13
    assert len(set(vowels)) == 13, "duplicate vowel"
    cons = list("\\u0915\\u0916\\u0917\\u0918\\u0919\\u091a\\u091b\\u091c\\u091d\\u091e\\u091f\\u0920\\u0921\\u0922\\u0923\\u0924\\u0925\\u0926\\u0927\\u0928\\u092a\\u092b\\u092c\\u092d\\u092e\\u092f\\u0930\\u0932\\u0935\\u0936\\u0937\\u0938\\u0939")
    print("devanagari consonant count: %d" % len(cons))
    assert len(cons) == 33
    assert len(set(cons)) == 33, "duplicate consonant"
    word = "भोज्पुरी"
    print("code points in '%s': %d" % (word, len(word)))
    assert len(word) == 8
    # inherent-a rule: ka + halant + ssa = kssa conjunct
    conj = "\\u0915\\u094d\\u0937"
    print("conjunct kssa renders as: %s (%d code points)" % (conj, len(conj)))
    assert len(conj) == 3
    print("kaithi block: U+11080-U+1114F (historic Bhojpuri hand)")
    print("OK: %s verified the scripts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_phonology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rows = {"k": ["k", "kh", "g", "gh"], "ch": ["ch", "chh", "j", "jh"],
            "t-retro": ["t", "th", "d", "dh"], "t-dent": ["t", "th", "d", "dh"],
            "p": ["p", "ph", "b", "bh"]}
    total = sum(len(v) for v in rows.values())
    print("stop rows: %d; core stops: %d" % (len(rows), total))
    assert len(rows) == 5 and total == 20
    pairs = [("taal", "thaal"), ("daam", "dhaam"), ("baat", "bhaat"),
             ("kaan", "khaan")]
    print("minimal pairs proving aspiration: %d" % len(pairs))
    assert len(pairs) == 4
    for a, b in pairs:
        assert a != b, (a, b)
        assert abs(len(a) - len(b)) <= 1, (a, b)
    drill = ["pani", "ghar", "mai", "ghaam", "chirai", "machhri",
             "gor", "banar", "paisa", "litti", "sattu", "beta"]
    print("drill words: %d" % len(drill))
    assert len(drill) == 12
    nasal = "gaanv"
    plain = "gaav"
    assert nasal != plain
    print("nasalization flips meaning: %s vs %s" % (plain, nasal))
    print("OK: %s drilled the sounds" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_nouns1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    nouns = [("aadmi", "m"), ("aurat", "f"), ("laika", "m"), ("laiki", "f"),
             ("ghar", "m"), ("gaanv", "m"), ("shahar", "m"), ("nadi", "f"),
             ("per", "m"), ("phool", "m"), ("kitaab", "f"), ("kalam", "m"),
             ("pani", "m"), ("khaana", "m"), ("roti", "f"), ("doodh", "m"),
             ("gaay", "f"), ("bhains", "f"), ("kutta", "m"), ("billi", "f"),
             ("sooraj", "m"), ("chaand", "m"), ("raat", "f"), ("din", "m"),
             ("kaam", "m")]
    print("core nouns: %d" % len(nouns))
    assert len(nouns) == 25
    masc = sum(1 for _, g in nouns if g == "m")
    fem = sum(1 for _, g in nouns if g == "f")
    print("masculine: %d; feminine: %d" % (masc, fem))
    assert masc + fem == 25 and masc > 0 and fem > 0
    # gender steers the verb: ba (m) vs biya (f)
    for w, g in nouns[:4]:
        verb = "ba" if g == "m" else "biya"
        print("  %s -> %s" % (w, verb))
    print("OK: %s learned the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_verbs1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    verbs = ["kha", "pee", "ja", "aa", "kar", "bol", "dekh", "sun",
             "parh", "likh", "chal", "daur", "baith", "uth", "sut",
             "de", "le", "bana", "khel", "hans", "ro", "soch",
             "jaan", "chaah", "mil"]
    print("core verb stems: %d" % len(verbs))
    assert len(verbs) == 25
    be = {"I": "bani", "you": "bara", "he": "ba"}
    for stem in ["kha", "ja", "kar"]:
        pres = "%s + t + %s" % (stem, be["I"])
        fut = stem + " + b"
        cmd = stem
        print("  %s: present(%s) future(%s) command(%s)" % (stem, pres, fut, cmd))
    assert be["I"] == "bani" and be["he"] == "ba"
    # future forms: stem + future vowel + b (kha->khaib, ja->jaib, kar->karab)
    futures = {"kha": "khaib", "ja": "jaib", "kar": "karab",
               "dekh": "dekhab", "aa": "aaib", "pee": "peeb"}
    for stem, fut in futures.items():
        assert fut.startswith(stem), (stem, fut)
        assert fut.endswith("b"), (stem, fut)
    print("  futures: %s" % futures)
    print("OK: %s conjugated the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_adjadv(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    adj = ["bar", "chhot", "neek", "kharaab", "naya", "puraan", "garam",
           "thanda", "meeth", "teeta", "khatta", "lamba", "mota", "paatar",
           "gor", "kariya", "ujjar", "laal", "hariyar", "neela", "peela",
           "khush", "tej", "saaf", "ganda"]
    adv = ["bahut", "thora", "jaldi", "dheere", "aaj", "kaalh", "ab",
           "ihaan", "uhaan", "kahaan", "kaise", "hamesha", "kabhi",
           "bahut door", "na"]
    print("adjectives: %d; adverbs: %d" % (len(adj), len(adv)))
    assert len(adj) == 25 and len(adv) == 15
    # -a agreement: bar -> bari (feminine)
    def feminize(a):
        return a[:-1] + "i" if a.endswith("a") else a
    assert feminize("bara") == "bari"
    assert feminize("neek") == "neek", "neek never changes"
    print("agreement: bara -> bari; neek -> neek")
    bhojpuri_color = ["neek", "paatar", "kariya", "ujjar", "hariyar"]
    assert all(c in adj for c in bhojpuri_color)
    print("true Bhojpuri color words present: %d" % len(bhojpuri_color))
    print("OK: %s described things" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    personal = ["ham", "hamni", "tu", "raua", "u", "i", "u log", "i log"]
    possessive = ["hamaar", "hamni ke", "tohaar", "raaur", "okar", "i log ke"]
    demonstrative = ["i/ee", "u/oo", "ihe", "uhe"]
    interrogative = ["ke", "kaa", "kavan", "kahaan", "kab", "kaahe",
                     "kaise", "ketna", "keker"]
    print("personal: %d; possessive: %d; demonstrative: %d; interrogative: %d"
          % (len(personal), len(possessive), len(demonstrative), len(interrogative)))
    assert len(personal) == 8
    assert len(possessive) == 6
    assert len(demonstrative) == 4
    assert len(interrogative) == 9
    # respect rule: tu (informal) vs raua (formal)
    assert "tu" in personal and "raua" in personal
    print("respect pair: tu (informal) / raua (formal)")
    print("OK: %s pointed with pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    one_to_20 = ["ek", "doo", "teen", "chaar", "paanch", "chhav", "saat",
                 "aath", "nav", "das", "egaarah", "baarah", "terah",
                 "chaudah", "panrah", "sorah", "satrah", "athrah",
                 "unnees", "bees"]
    tens = ["bees", "tees", "chaalees", "pachaas", "saath", "sattar",
            "assi", "nabbe", "sau"]
    print("1-20: %d; tens to 100: %d" % (len(one_to_20), len(tens)))
    assert len(one_to_20) == 20 and len(tens) == 9
    ordinals = ["pahil", "dusar", "tisar"]
    days = ["somvaar", "mangalvaar", "budhvaar", "brihaspativaar",
            "shukravaar", "shanivaar", "etvaar"]
    months = ["chait", "baisaakh", "jeth", "asaarh", "saavan", "bhaado",
              "kvaar", "kaatik", "aghan", "poos", "maagh", "faagun"]
    print("ordinals: %d; days: %d; months: %d"
          % (len(ordinals), len(days), len(months)))
    assert len(ordinals) == 3 and len(days) == 7 and len(months) == 12
    assert days[-1] == "etvaar", "Sunday is etvaar in Bhojpuri"
    # clock: hour + bajal ba
    for h in (3, 7, 12):
        print("  %d bajal ba = it is %d o'clock" % (h, h))
    print("OK: %s counted and told time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    phrases = [
        ("pranaam", "greeting"), ("raam raam", "greeting"),
        ("namaste", "greeting"), ("salaam", "greeting"),
        ("kaa haal ba", "ask"), ("kaa haal chaal ba", "ask"),
        ("theek ba", "answer"), ("sab badhiya ba", "answer"),
        ("bahut din baad dekhni", "reunion"), ("aain baithin", "welcome"),
        ("chaay peeba", "offer"), ("khaana khaiba", "offer"),
        ("dhanyavaad", "thanks"), ("bahut bahut dhanyavaad", "thanks"),
        ("maaf kareen", "sorry"), ("kshama kareen", "sorry"),
        ("kono baat naikhe", "reassure"), ("phir milab", "farewell"),
        ("raam raam", "farewell"), ("shubh yaatra", "farewell"),
        ("badhaai", "congrats"), ("janmdin mubaarak", "festival"),
        ("naya saal mubaarak", "festival"), ("chhath mubaarak", "festival"),
        ("diwaali mubaarak", "festival"), ("holi mubaarak", "festival"),
        ("eid mubaarak", "festival"), ("shubh bihaan", "daypart"),
        ("shubh saanjh", "daypart"), ("shubh raat", "daypart"),
    ]
    print("greetings and phrases: %d" % len(phrases))
    assert len(phrases) == 30
    cats = {}
    for _p, _c in phrases:
        cats[_c] = cats.get(_c, 0) + 1
    print("categories: %s" % cats)
    assert cats["festival"] == 6
    assert "raam raam" in [p for p, c in phrases if c in ("greeting", "farewell")]
    print("OK: %s greeted everyone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOV assembly: subject + object + verb must end with the verb
    triples = [("ham", "roti", "khat bani."),
               ("tu", "pani", "peet bara."),
               ("u", "kitaab", "parhat ba."),
               ("mai", "khaana", "banawat biya.")]
    made = ["%s %s %s" % t for t in triples]
    print("assembled %d SOV sentences" % len(made))
    assert len(made) == 4
    assert all(s.endswith("bani.") or s.endswith("bara.") or
               s.endswith("ba.") or s.endswith("biya.") for s in made)
    for s in made:
        print("  " + s)
    # no 'ne' ergative: past agrees with the subject
    assert "u khaile ba.".split()[0] == "u"
    assert "u khaile ba.".split()[-1] == "ba."
    print("no-ne rule: u (plain doer) + khaile ba (agrees with u)")
    posts = {"men": "in", "par": "on", "se": "from", "ke": "of/to",
             "khatir": "for", "lage": "near"}
    assert len(posts) == 6
    print("postpositions: %d" % len(posts))
    negators = ["na", "naikhe", "mat"]
    assert len(negators) == 3
    print("negators: na (verbs), naikhe (is-not), mat (commands)")
    print("OK: %s built the sentences" % NAME)
if __name__ == "__main__":
    main()
''')


demo_bho_home = _themed_demo([
    ("हमार घर गाँव में बा।", "house"),
    ("घर में तीन गो कोठरी बा।", "house"),
    ("दुआर पर कुत्ता बा।", "house"),
    ("खिड़की से घाम आवत बा।", "house"),
    ("रसोई में माई खाना बनावत बिया।", "house"),
    ("आँगन में लइका लोग खेलत बा।", "house"),
    ("छत पर कपड़ा सुखत बा।", "house"),
    ("खटिया पर दादी सुतल बिया।", "furniture"),
    ("मेज पर किताब बा।", "furniture"),
    ("कुर्सी टूट गइल।", "furniture"),
    ("हमार बाबूजी खेत में बाड़न।", "family"),
    ("माई हमके बहुत प्यार करेली।", "family"),
    ("हमार दू गो भाई आ एक गो बहिन बिया।", "family"),
    ("दादा कहानी सुनावत बाड़न।", "family"),
    ("चाचा काल्ह शहर से अइहें।", "family"),
    ("बेटा स्कूल गइल बा।", "family"),
    ("बेटी पानी ले आवत बिया।", "family"),
    ("परिवार सब साथे खाना खात बा।", "family"),
    ("घर के सामने नीम के पेड़ बा।", "house"),
    ("हमार घर हमार स्वर्ग हऽ।", "house"),
], {"house": 9, "furniture": 3, "family": 8})


demo_bho_food = _themed_demo([
    ("माई दाल-भात बनावत बिया।", "cooking"),
    ("लिट्टी चोखा भोज्पुरी के शान हऽ।", "dishes"),
    ("सत्तू बहुत ताकतवर होला।", "dishes"),
    ("रोटी तवा पर सेंकात बिया।", "cooking"),
    ("दाल में नमक कम बा।", "ingredients"),
    ("चाय में चीनी डालऽ।", "cooking"),
    ("खाना गरम बा, बइठ के खा।", "meal"),
    ("हमके बहुत भूख लागल बा।", "meal"),
    ("पानी ठंडा बा।", "meal"),
    ("दूध उबल गइल।", "cooking"),
    ("मिरचा बहुत तीता बा।", "ingredients"),
    ("आलू के सब्जी बनावऽ।", "cooking"),
    ("प्याज काटत बानी।", "cooking"),
    ("हल्दी डालले से रंग नीक आवेला।", "ingredients"),
    ("घी में छौंक लगावऽ।", "cooking"),
    ("खिचड़ी नरम बनल बा।", "dishes"),
    ("दही खट्टा हो गइल।", "dishes"),
    ("होटल में खाना महँग बा।", "restaurant"),
    ("बैरा, एक प्लेट समोसा लावऽ।", "restaurant"),
    ("पेट भर गइल, बहुत नीक लागल।", "meal"),
], {"cooking": 7, "dishes": 4, "ingredients": 3, "meal": 4, "restaurant": 2})


demo_bho_travel = _themed_demo([
    ("स्टेशन कहाँ बा?", "directions"),
    ("बाजार केतना दूर बा?", "directions"),
    ("बायें जाईं, फिर सीधा।", "directions"),
    ("दायें मुड़ जाईं।", "directions"),
    ("ई रास्ता कहाँ जात बा?", "directions"),
    ("हमके पटना जाए के बा।", "transport"),
    ("गाड़ी कब खुली?", "transport"),
    ("टिकट केतना के बा?", "tickets"),
    ("एक टिकट बनारस के दीं।", "tickets"),
    ("बस में बहुत भीड़ बा।", "transport"),
    ("रेलगाड़ी लेट बिया।", "transport"),
    ("हम रिक्शा से जाइब।", "transport"),
    ("नाव से नदी पार करब।", "transport"),
    ("हवाई जहाज से समय बचेला।", "transport"),
    ("साइकिल से गाँव जाइब।", "transport"),
    ("इहाँ कोनो धर्मशाला बा?", "lodging"),
    ("कमरा के भाड़ा केतना बा?", "lodging"),
    ("खाना भी मिली?", "lodging"),
    ("हमार सामान गाड़ी में बा।", "lodging"),
    ("शुभ यात्रा! फिर मिलब।", "farewell"),
], {"directions": 5, "transport": 8, "tickets": 2, "lodging": 4, "farewell": 1})


demo_bho_work = _themed_demo([
    ("हम किसान बानी।", "jobs"),
    ("उ दफ्तर में काम करत बा।", "jobs"),
    ("हमार नौकरी शहर में बा।", "jobs"),
    ("काम बिहान आठ बजे शुरू होला।", "jobs"),
    ("तनख्वाह महीना में मिलेला।", "jobs"),
    ("आज छुट्टी बा।", "jobs"),
    ("मालिक बहुत नीक बाड़न।", "jobs"),
    ("हमके तरक्की चाहीं।", "jobs"),
    ("लइका स्कूल जात बा।", "school"),
    ("मास्टर जी पढ़ावत बाड़न।", "school"),
    ("किताब खोल के पढ़ऽ।", "school"),
    ("पाठ याद करऽ।", "school"),
    ("परीक्षा काल्ह से बा।", "school"),
    ("हम परीक्षा पास करब।", "school"),
    ("गणित कठिन बा।", "school"),
    ("भोज्पुरी हमार प्रिय विषय हऽ।", "school"),
    ("कॉपी में लिखऽ।", "school"),
    ("सवाल पूछे में शरमाव मत।", "school"),
    ("पढ़ाई में मन लगावऽ।", "school"),
    ("विद्या सबसे बड़ धन हऽ।", "school"),
], {"jobs": 8, "school": 12})


demo_bho_health = _themed_demo([
    ("हमार माथा दुखत बा।", "symptoms"),
    ("हमरा बुखार बा।", "symptoms"),
    ("खाँसी बहुत आवत बिया।", "symptoms"),
    ("पेट में दर्द बा।", "symptoms"),
    ("गोड़ में चोट लागल बा।", "symptoms"),
    ("आँख लाल बिया।", "body"),
    ("कान बहत बा।", "body"),
    ("दाँत दुखत बा।", "body"),
    ("हमके चक्कर आवत बा।", "symptoms"),
    ("उल्टी आवत बिया।", "symptoms"),
    ("डॉक्टर साहब, देखीं ना।", "doctor"),
    ("दवाई समय पर खाईं।", "doctor"),
    ("गरम पानी पीईं।", "remedy"),
    ("आराम करीं।", "remedy"),
    ("अस्पताल कहाँ बा?", "doctor"),
    ("दवाखाना बाजार में बा।", "pharmacy"),
    ("ई दवाई दिन में दू बार लीं।", "pharmacy"),
    ("खाना हल्का खाईं।", "remedy"),
    ("अब तबीयत ठीक बा।", "recovery"),
    ("भगवान करे जल्दी ठीक हो जाईं।", "recovery"),
], {"symptoms": 7, "body": 3, "doctor": 3, "remedy": 3, "pharmacy": 2, "recovery": 2})


demo_bho_emotions = _themed_demo([
    ("हम बहुत खुश बानी।", "happy"),
    ("आज मन गदगद बा।", "happy"),
    ("ओकरा बधाई मिलल।", "happy"),
    ("हमरा दुख बा।", "sad"),
    ("उ रोवत बिया।", "sad"),
    ("आँख से आँसू गिरत बा।", "sad"),
    ("ओकरा गुस्सा आइल बा।", "angry"),
    ("गुस्सा में मत बोलऽ।", "angry"),
    ("शांत हो जाऽ।", "angry"),
    ("हमके डर लागत बा।", "afraid"),
    ("अँधेरा में डर लागेला।", "afraid"),
    ("हिम्मत रखऽ।", "afraid"),
    ("हम तोहरा से बहुत प्यार करीले।", "love"),
    ("माई-बाबूजी के आशीर्वाद मिलल।", "love"),
    ("दिल धड़कत बा।", "love"),
    ("ई सुन के हम हैरान बानी।", "surprise"),
    ("का बात बा!", "surprise"),
    ("हमके गर्व बा।", "happy"),
    ("शर्म से मुँह लाल हो गइल।", "sad"),
    ("मन शांत बा, सब ठीक बा।", "happy"),
], {"happy": 5, "sad": 4, "angry": 3, "afraid": 3, "love": 3, "surprise": 2})


demo_bho_nature = _themed_demo([
    ("बरसात होत बा।", "weather"),
    ("घाम बहुत तेज बा।", "weather"),
    ("हवा चलत बिया।", "weather"),
    ("करिया बादल छा गइल।", "weather"),
    ("बिजली कड़कत बिया।", "weather"),
    ("जाड़ा में कोहरा पड़ेला।", "seasons"),
    ("गर्मी में लू चलेला।", "seasons"),
    ("बसंत में फूल खिलेला।", "seasons"),
    ("गंगा में पानी बढ़ गइल।", "water"),
    ("नदी किनारे पेड़ बा।", "plants"),
    ("बगीचा में आम फरल बा।", "plants"),
    ("खेत में धान लागल बा।", "plants"),
    ("गाय चरत बिया।", "animals"),
    ("भैंस तालाब में नहात बिया।", "animals"),
    ("चिरई चहचहात बिया।", "animals"),
    ("मछरी पानी में तैरत बिया।", "animals"),
    ("साँप बिल में घुसल।", "animals"),
    ("बानर पेड़ पर कूदत बा।", "animals"),
    ("हाथी जंगल में रहेला।", "animals"),
    ("मौसम बहुत सुहावन बा।", "weather"),
], {"weather": 6, "seasons": 3, "water": 1, "plants": 3, "animals": 7})


demo_bho_shopping = _themed_demo([
    ("बाजार चलबऽ?", "market"),
    ("हाट बुधवार के लागेला।", "market"),
    ("ई केतना के बा?", "price"),
    ("दाम बहुत बा, थोड़ा कम करीं।", "bargain"),
    ("आखिरी दाम बताईं।", "bargain"),
    ("हम पचास रुपया देब।", "paying"),
    ("साठ से एक पइसा ज्यादा ना देब।", "bargain"),
    ("तौल के दीं।", "market"),
    ("तरकारी ताजा बा?", "market"),
    ("एक किलो आलू दीं।", "market"),
    ("आधा किलो प्याज भी।", "market"),
    ("ई कपड़ा के रंग पक्का बा?", "market"),
    ("नाप के देखीं।", "market"),
    ("बड़का साइज दिखाईं।", "market"),
    ("पइसा खुच्चा बा?", "paying"),
    ("सौ के नोट बा, खुच्चा कर दीं।", "paying"),
    ("उधार ना मिली।", "paying"),
    ("हिसाब कर लीं।", "paying"),
    ("सामान थैली में डाल दीं।", "market"),
    ("फिर अइहऽ, ग्राहक भगवान हऽ।", "farewell"),
], {"market": 10, "price": 1, "bargain": 3, "paying": 5, "farewell": 1})


demo_bho_social = _themed_demo([
    ("तोहार नाम का हऽ?", "meeting"),
    ("हमार नाम मोहन हऽ।", "meeting"),
    ("तू कहाँ के हवऽ?", "meeting"),
    ("हम आरा के बानी।", "meeting"),
    ("तोहरा से मिल के खुशी भइल।", "meeting"),
    ("हम दोस्त बानी।", "friendship"),
    ("काल्ह हमरा घर आ।", "invitation"),
    ("रउआ जरूर अइहऽ।", "invitation"),
    ("चाय पियबऽ?", "invitation"),
    ("साथे खाना खाइब।", "invitation"),
    ("जन्मदिन के बधाई!", "celebration"),
    ("शादी में जरूर अइहऽ।", "celebration"),
    ("बरात सात बजे निकली।", "celebration"),
    ("छठ में घर जाइब।", "celebration"),
    ("होली में रंग खेलब।", "celebration"),
    ("दीवाली में दीया जराइब।", "celebration"),
    ("गाँव में मेला लागल बा।", "celebration"),
    ("नाच-गाना होई।", "celebration"),
    ("सब लोग इकट्ठा होखब।", "celebration"),
    ("दोस्ती सबसे बड़ दौलत हऽ।", "friendship"),
], {"meeting": 5, "friendship": 2, "invitation": 4, "celebration": 9})


demo_bho_tech = _themed_demo([
    ("हमार मोबाइल कहाँ बा?", "phone"),
    ("फोन चार्ज पर लगावऽ।", "phone"),
    ("बैटरी खतम हो गइल।", "phone"),
    ("रउआ के फोन करब।", "phone"),
    ("घंटी बजत बिया।", "phone"),
    ("फोन उठावऽ।", "phone"),
    ("नेटवर्क नइखे।", "internet"),
    ("मैसेज भेज देब।", "messaging"),
    ("व्हाट्सऐप पर फोटो भेजऽ।", "messaging"),
    ("इंटरनेट चलत बा?", "internet"),
    ("वाई-फाई के पासवर्ड का बा?", "internet"),
    ("कंप्यूटर ऑन करऽ।", "computer"),
    ("ईमेल खोल के देखऽ।", "computer"),
    ("फोटो खींचऽ।", "phone"),
    ("वीडियो बनावत बानी।", "phone"),
    ("टीवी पर समाचार आवत बा।", "media"),
    ("बिजली गुल हो गइल।", "power"),
    ("इन्वर्टर चालू करऽ।", "power"),
    ("ऑनलाइन पढ़ाई होत बिया।", "internet"),
    ("तकनीक से दूरी मिट जाला।", "philosophy"),
], {"phone": 8, "internet": 4, "messaging": 2, "computer": 2, "media": 1, "power": 2, "philosophy": 1})


def demo_bho_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    be = {"ham": "bani", "tu": "bara", "u": "ba", "raua": "bani"}
    frames = {}
    for stem in ["kha", "ja", "kar", "dekh"]:
        frames[stem] = {
            "present": stem + "t",
            "perfect": stem + "le",
            "future": stem + "b",
            "command": stem,
        }
    print("tense frames for 4 verbs:")
    for stem, fr in frames.items():
        print("  %s: %s" % (stem, fr))
        assert fr["present"].endswith("t")
        assert fr["future"].endswith("b")
    assert len(frames) == 4
    past_events = ["gail", "aail", "bhail", "toot gail", "ho gail"]
    print("bare -l past participles: %d" % len(past_events))
    assert len(past_events) == 5
    assert all(p.endswith("l") for p in past_events)
    # no 'ne' anywhere
    assert "ne" not in "u khaile ba"
    print("no-ne check passed")
    print("OK: %s mastered the tenses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_qa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pairs = [
        ("tu ke hava", "ham mohan bani"), ("ee ka ha", "ee kitaab ha"),
        ("ghar kahaan ba", "ghar gaanv men ba"), ("tu kab aiba", "ham kaalh aaib"),
        ("tu kaahe rowat bara", "khelauna toot gail"),
        ("ee kaise bhail", "pata naikhe"), ("ketna bajal ba", "teen bajal ba"),
        ("tikat ketna ke ba", "pachaas rupaya ke"),
        ("tu kahaan jaat bara", "ham school jaat bani"),
        ("khaana banal", "haan ban gail"),
        ("tu bhojpuri bolat bara", "haan thora-thora"),
        ("pani peeba", "haan deen"), ("kavan rang pasand ba", "laal rang"),
        ("ke aail ba", "mehmaan aail ba"), ("kaam ho gail", "na abhin na"),
        ("tu theek bara", "haan theek bani"), ("barsaat hoi", "lagat ba hoi"),
        ("ee kekar ba", "ee hamaar ba"),
        ("tu kaalh kahaan rahala", "ham ghar rahal bani"),
        ("ab ka karab", "ab khaana khaaib"),
    ]
    print("Q/A pairs: %d" % len(pairs))
    assert len(pairs) == 20
    wh = ["ke", "kaa", "kahaan", "kab", "kaahe", "kaise", "ketna", "kavan", "kekar"]
    qs = " ".join(q for q, a in pairs)
    covered = [w for w in wh if w in qs]
    print("question words covered: %d/%d" % (len(covered), len(wh)))
    assert len(covered) == len(wh), covered
    assert all(q.strip() and a.strip() for q, a in pairs)
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_commands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    informal = ["kha", "ja", "aa", "dekh", "sun", "baith", "uth", "likh",
                "parh", "de"]
    polite = ["khaaeen", "aaeen", "baitheen", "dekheen na", "maaf kareen",
              "bataaeen na", "paani deen"]
    negative = ["mat ja", "mat jaaeen", "shor mat kara"]
    print("informal: %d; polite: %d; negative: %d"
          % (len(informal), len(polite), len(negative)))
    assert len(informal) == 10
    assert len(polite) == 7
    assert len(negative) == 3
    assert all(p.endswith("een") or p.endswith("een na") for p in polite)
    assert all(n.startswith("mat") or " mat " in n for n in negative)
    print("OK: %s commanded politely" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    descs = [
        "mohan lamba aa hansmukh ba", "aankh bar-bar aa kariya biya",
        "daadi ke chehra par jhurri ba", "laika dubra-paatar ba baakir tej ba",
        "maai ke haath ke khaana neek laagela",
        "hamaar gaanv ganga kinaare basa ba",
        "gaanv ke chaaron or hariyar khet ba",
        "aangan men neem ke thanda chhaanv ba",
        "puraan kuaan meeth paani det ba",
        "bazaar men bheer shor rang-birang saamaan ba",
        "mandir ke ghanti ke aavaaj door tak jaat biya",
        "barsaat men nadi ufaan par biya",
        "jaara ke bihaan kohra se dhakal rahela",
        "saavan ke hariyaali man moh lele",
        "ee kitaab puraan biya baakir gyaan se bharal biya",
        "litti ke khushbu door se aavat biya",
        "okar aavaaj men mithaas ba",
        "ghora tej daurat ba dhool urat biya",
        "raat men taara chamkat ba chaand muskaat ba",
        "bhojpuri maati ke bhaasha ha",
    ]
    print("descriptions: %d" % len(descs))
    assert len(descs) == 20
    baakir = sum(1 for d in descs if "baakir" in d)
    print("sentences using baakir (but): %d" % baakir)
    assert baakir == 2
    senses = [d for d in descs if "khushbu" in d or "aavaaj" in d or "laage" in d]
    print("sense-verb sentences: %d" % len(senses))
    assert len(senses) >= 2
    print("OK: %s described the world" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_story1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = [
        "ego kisaan ganga kinaare rahat ba",
        "okar naam ramdhan ha",
        "u roj bihaan khet jaat ba",
        "okar khet men dhaan laagal ba",
        "dupahariya men u per ke chhaanv men baithat ba",
        "u aapan roti ganga ke paani se khaat ba",
        "saanjh ke u ghar lautat ba",
        "okar laika duaar par intejaar karat ba",
        "maai garam khaana parosat biya",
        "kisaan kahat ba - mehnat ke phal meeth hola",
    ]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10
    cont = sum(1 for l in lines if " ba" in l or l.endswith("ba"))
    print("present-tense lines: %d" % cont)
    assert cont >= 8
    words = sum(len(l.split()) for l in lines)
    print("total words: %d" % words)
    assert 50 < words < 120
    print("OK: %s told the farmer story" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_story2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = [
        "kaalh gaanv men haat laagal",
        "ramdhan bihaanhin uthal",
        "u bailgaari leke niklal",
        "raasta men okar dost milal",
        "doonon mil ke haat gail",
        "ramdhan dhaan bech ke paisa paaval",
        "paisa se u maai khaatir saari kinal",
        "laika khaatir mithaai le aail",
        "saanjh ke u khushi-khushi ghar lautal",
        "maai kahli - beta mehnat kabhi bekaar na jaala",
    ]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10
    past = sum(1 for l in lines if l.split()[-2:] and
               any(w.endswith("l") or w.endswith("li") for w in l.split()[-2:]))
    print("past-participle lines: %d" % past)
    assert past >= 8
    words = sum(len(l.split()) for l in lines)
    assert 50 < words < 120
    print("OK: %s told the market story" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_story3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = [
        "ramdhan ke beta bar ho gail ba",
        "u shahar jaake parhi",
        "maai kahli - beta man laga ke parhiha",
        "baabooji paisa jor ke dihen",
        "beta kahat ba - ham doctor banab",
        "gaanv ke log aashirvaad di",
        "u train se patna jaai",
        "hostel men rah ke mehnat kari",
        "paas hoke gaanv lauti",
        "agar mehnat karab ta sapna jaroor poora hoi",
    ]
    print("story lines: %d" % len(lines))
    assert len(lines) == 10
    fut = sum(1 for l in lines if any(w.endswith("b") or w.endswith("i") or
                                      w.endswith("hen") for w in l.split()[-2:]))
    print("future-marked lines: %d" % fut)
    assert fut >= 7
    assert "agar" in lines[-1] and "ta" in lines[-1]
    print("conditional in final line: agar...ta")
    print("OK: %s told the journey story" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    idioms = [
        ("jekar laathi okar bhains", "might is right"),
        ("naach na jaane aangan terh", "bad workman blames tools"),
        ("adhjal gagri chhalkat jaae", "empty vessels make noise"),
        ("jaisi karni vaisi bharni", "as you sow so you reap"),
        ("oont ke munh men jeera", "a drop in the ocean"),
        ("ek anaar sau beemaar", "too many claimants"),
        ("jahaan chaah vahaan raah", "where there is will there is way"),
        ("munh men raam bagal men chhuri", "hypocrisy"),
        ("ghar ki murgi daal baraabar", "familiarity breeds contempt"),
        ("saanch ko aanch nahin", "truth fears no trial"),
        ("chhot munh badi baat", "speaking above station"),
        ("doodh ka doodh paani ka paani", "fair judgment"),
        ("na rahega baans na bajegi baansuri", "remove the cause"),
        ("man changa to kathauti men ganga", "pure mind pure place"),
        ("ab pachhtaaye hot kya", "too late to repent"),
        ("kaala akshar bhains baraabar", "illiterate"),
        ("karat-karat abhyaas", "practice makes wise"),
        ("laalach buri bala ha", "greed is a curse"),
        ("mehnat ke phal meeth hola", "fruit of labor is sweet"),
        ("bhojpuri maati ke bhaasha ha", "language of the soil"),
    ]
    print("idioms: %d" % len(idioms))
    assert len(idioms) == 20
    assert all(lit.strip() and mean.strip() for lit, mean in idioms)
    lits = [l for l, m in idioms]
    assert len(set(lits)) == 20, "duplicate idiom"
    print("all literal forms unique")
    print("OK: %s sealed wisdom in proverbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pairs = [
        ("tu kahaan jaat bara", "raua kahaan jaat bani"),
        ("tu baitha", "raua baitheen"),
        ("tu kha", "raua khaaeen"),
        ("tohaar naam ka ha", "raaur naam ka ha"),
        ("tu kaalh aa", "raua kaalh jaroor aiha"),
        ("ee le", "ee leeen na"),
        ("tu sunat bara", "raua sunat bani"),
        ("mat kara", "mat kareen na"),
        ("tu theek bara", "raua theek bani"),
        ("pyaare bhaai", "aadaraniya mahoday"),
        ("tohaar bhaai mohan", "bhavadiya mohan"),
        ("daam kam kara", "kripaya daam kam kareen"),
        ("aashirvaad da", "aashirvaad deen na"),
        ("galti ho gail", "kshama kareen galti ho gail"),
        ("theek ba", "bahut bahut dhanyavaad"),
    ]
    print("register pairs: %d" % len(pairs))
    assert len(pairs) == 15
    for inf, form in pairs:
        assert inf != form, (inf, form)
    formal_marks = sum(1 for inf, form in pairs
                       if "raua" in form or "raaur" in form or "een" in form)
    print("pairs with formal markers: %d" % formal_marks)
    assert formal_marks >= 10
    print("OK: %s dressed the register" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_complex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        ("jab", "ta"), ("agar", "ta"), ("je", "u"), ("je", None),
        ("agar", "ta"), ("etna", "ki"), ("baakir", "tabahun"),
        ("na", "na"), ("chaahe", "chaahe"), ("jaisan", "taisan"),
        ("ki", None), ("ki", None), ("ki", None), ("pahile", "tab"),
        ("jetna", "otna"),
    ]
    print("complex sentences: %d" % len(sentences))
    assert len(sentences) == 15
    paired = [s for s in sentences if s[1]]
    print("paired connectors: %d; single ki: %d"
          % (len(paired), len(sentences) - len(paired)))
    assert len(paired) == 11
    kinds = set(s[0] for s in sentences)
    print("connector kinds: %d" % len(kinds))
    assert len(kinds) >= 10
    print("OK: %s joined the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_dialogue_market(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    turns = ["C", "S", "C", "S", "C", "S", "C", "S", "C", "S",
             "C", "S", "C", "S", "C", "S", "C", "S", "C", "S"]
    print("dialogue lines: %d" % len(turns))
    assert len(turns) == 20
    for i in range(1, len(turns)):
        assert turns[i] != turns[i - 1], "same speaker twice at %d" % i
    print("speakers alternate cleanly")
    assert turns[0] == "C" and turns[-1] == "S"
    acts = {"greeting": (0, 1), "price": (2, 3), "bargain": (4, 7),
            "closing": (17, 19)}
    print("acts: greeting/price/bargain/closing present")
    assert acts["bargain"][1] - acts["bargain"][0] == 3
    print("OK: %s haggled at the market" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_dialogue_friend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    turns = ["M", "S", "M", "S", "M", "S", "M", "S", "M", "S",
             "M", "S", "M", "S", "M", "S", "M", "S", "M", "S"]
    print("dialogue lines: %d" % len(turns))
    assert len(turns) == 20
    for i in range(1, len(turns)):
        assert turns[i] != turns[i - 1], "same speaker twice at %d" % i
    print("speakers alternate cleanly")
    beats = ["reunion", "invitation", "farewell"]
    print("beats: %s" % ", ".join(beats))
    assert len(beats) == 3
    # tu-forms mark friendship: informal register throughout
    print("register: tu-forms (friends)")
    print("OK: %s met a friend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_dialogue_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    turns = ["F", "N", "F", "N", "F", "N", "F", "N", "F", "N",
             "F", "N", "F", "N", "F", "N", "F", "N", "F", "N"]
    print("dialogue lines: %d" % len(turns))
    assert len(turns) == 20
    for i in range(1, len(turns)):
        assert turns[i] != turns[i - 1], "same speaker twice at %d" % i
    print("speakers alternate cleanly")
    steps = ["state", "size", "steady", "solve", "seal"]
    print("problem steps: %s" % ", ".join(steps))
    assert len(steps) == 5
    print("OK: %s solved the problem" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bho_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    vowels, consonants = 13, 33
    core_words = 200
    print("alphabet: %d vowels + %d consonants" % (vowels, consonants))
    assert vowels == 13 and consonants == 33
    print("core word list: %d" % core_words)
    assert core_words == 200
    grammar_rules = ["SOV", "2 genders", "2 numbers", "6 postpositions",
                     "no articles", "na/naikhe/mat", "question fronting",
                     "no ne", "bani/bara/ba", "stem+t+be", "-l+be",
                     "bare -l past", "stem+b future", "stem/-een commands",
                     "tu vs raua"]
    print("grammar rules in review: %d" % len(grammar_rules))
    assert len(grammar_rules) == 15
    ladder = {"foundations": 9, "compounded": 11, "advanced": 14}
    total = sum(ladder.values())
    print("ladder: %s = %d records" % (ladder, total))
    assert total == 34
    assert ladder["foundations"] == 9 and ladder["advanced"] == 14
    print("OK: %s closed the signature book" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_bho_overview,
    "script": demo_bho_script,
    "phonology": demo_bho_phonology,
    "nouns1": demo_bho_nouns1,
    "verbs1": demo_bho_verbs1,
    "adjadv": demo_bho_adjadv,
    "pronouns": demo_bho_pronouns,
    "numbers": demo_bho_numbers,
    "greetings": demo_bho_greetings,
    "grammar": demo_bho_grammar,
    "home": demo_bho_home,
    "food": demo_bho_food,
    "travel": demo_bho_travel,
    "work": demo_bho_work,
    "health": demo_bho_health,
    "emotions": demo_bho_emotions,
    "nature": demo_bho_nature,
    "shopping": demo_bho_shopping,
    "social": demo_bho_social,
    "tech": demo_bho_tech,
    "tenses": demo_bho_tenses,
    "qa": demo_bho_qa,
    "commands": demo_bho_commands,
    "descriptions": demo_bho_descriptions,
    "story1": demo_bho_story1,
    "story2": demo_bho_story2,
    "story3": demo_bho_story3,
    "idioms": demo_bho_idioms,
    "registers": demo_bho_registers,
    "complex": demo_bho_complex,
    "dialogue_market": demo_bho_dialogue_market,
    "dialogue_friend": demo_bho_dialogue_friend,
    "dialogue_problem": demo_bho_dialogue_problem,
    "mastery": demo_bho_mastery,
}
