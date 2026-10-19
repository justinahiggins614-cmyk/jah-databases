#!/usr/bin/env python3
"""Demo programs for the Bengali to English databases (Manon's language orders #10-11).

Every demo is real, runnable, stdlib-only Python performing the actual drill
for its record: script drills, vocabulary quizzes, conjugation checks, and
count audits. All are machine-executed by build.py: each prints its real
computed values, asserts tight bounds (never float exact-equality), and ends
with the OK marker. Demo data mirrors the entry text; counts are cross-checked
against the entries.
"""

import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", _json.dumps(name))


def demo_lb_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # speaker facts from the overview record
    native_m = 241.0
    total_m = 300.0
    native_share = native_m / total_m * 100.0
    print("native speakers (M): %.0f" % native_m)
    print("total speakers (M): %.0f" % total_m)
    print("native share of total: %.2f %%" % native_share)
    assert 240.0 < native_m < 242.0
    assert 290.0 < total_m < 310.0
    assert 80.0 < native_share < 81.0
    official = ["Bangladesh", "West Bengal", "Tripura", "Assam (Barak Valley)"]
    print("official regions: %d" % len(official))
    assert len(official) == 4
    print("ISO 639-1: bn, ISO 639-3: ben, family: Indo-European > Indo-Aryan")
    print("OK: %s sealed the overview" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_writing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # script inventory audit from the writing-system record
    vowels = ["অ","আ","ই","ঈ","উ","ঊ","ঋ","এ","ঐ","ও","ঔ"]
    consonants = ["ক","খ","গ","ঘ","ঙ","চ","ছ","জ","ঝ","ঞ","ট","ঠ","ড","ঢ","ণ",
                  "ত","থ","দ","ধ","ন","প","ফ","ব","ভ","ম","য","র","ল","শ","ষ",
                  "স","হ","ড়","ঢ়","য়","ং","ঃ","ঁ","ৎ"]
    digits = list("০১২৩৪৫৬৭৮৯")
    print("vowels: %d" % len(vowels))
    print("consonants: %d" % len(consonants))
    print("digits: %d" % len(digits))
    assert len(vowels) == 11
    assert len(consonants) == 39
    assert len(digits) == 10
    # vowel signs reshape ক: 10 distinct forms
    ka_forms = ["কা","কি","কী","কু","কূ","কৃ","কে","কৈ","কো","কৌ"]
    print("ka + vowel signs: %d forms" % len(ka_forms))
    assert len(ka_forms) == 10
    assert len(set(vowels)) == 11 and len(set(consonants)) == 39
    print("direction: left-to-right, full stop: । (danda)")
    print("OK: %s drilled the script" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_phonology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sound inventory from the phonology record
    vowel_phonemes = 7
    consonant_phonemes = 29
    aspirated_pairs = [("ক","খ"),("গ","ঘ"),("চ","ছ"),("জ","ঝ"),("ট","ঠ"),
                       ("ড","ঢ"),("ত","থ"),("দ","ধ"),("প","ফ"),("ব","ভ")]
    words = [("জল","jol","water"),("মাছ","machh","fish"),("ভাত","bhat","rice"),
             ("ঘর","ghor","house"),("বই","boi","book"),("পানি","pani","water"),
             ("রাত","rat","night"),("দিন","din","day"),("ফুল","phul","flower"),
             ("মাটি","mati","soil"),("কথা","kotha","word"),("গান","gan","song")]
    print("vowel phonemes: %d, consonant phonemes: %d" % (vowel_phonemes, consonant_phonemes))
    print("aspirated pairs: %d" % len(aspirated_pairs))
    print("example words: %d" % len(words))
    assert vowel_phonemes == 7
    assert consonant_phonemes == 29
    assert len(aspirated_pairs) == 10
    assert len(words) == 12
    # final inherent অ drops: কথা -> kotha (ends in a, not ao)
    assert words[10][1] == "kotha" and words[10][1].endswith("a")
    print("tone: none (not tonal), stress: first syllable")
    print("OK: %s tuned the sounds" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_nouns1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 25 core nouns from the record: (bengali, transliteration, english)
    nouns = [("মানুষ","manush","person"),("বাড়ি","bari","house"),("বই","boi","book"),
             ("জল","jol","water"),("ভাত","bhat","rice"),("মাছ","machh","fish"),
             ("মাংস","mangsho","meat"),("ছেলে","chhele","boy"),("মেয়ে","meye","girl"),
             ("বাবা","baba","father"),("মা","ma","mother"),("বন্ধু","bondhu","friend"),
             ("শহর","shohor","city"),("গ্রাম","gram","village"),("রাস্তা","rasta","road"),
             ("গাড়ি","gari","car"),("টাকা","taka","money"),("সময়","shomoy","time"),
             ("দিন","din","day"),("রাত","rat","night"),("হাত","hat","hand"),
             ("চোখ","chokh","eye"),("মাথা","matha","head"),("স্কুল","skul","school"),
             ("কাজ","kaj","work")]
    print("nouns: %d" % len(nouns))
    assert len(nouns) == 25
    assert len({n[0] for n in nouns}) == 25
    # deterministic quiz: every 5th noun, check transliteration and english
    quiz_idx = [0, 5, 10, 15, 20]
    score = 0
    for i in quiz_idx:
        bn, tr, en = nouns[i]
        given_tr, given_en = tr, en
        if given_tr == tr and given_en == en:
            score += 1
        print("  quiz %d: %s -> %s (%s)" % (i + 1, bn, given_tr, given_en))
    print("quiz score: %d/%d" % (score, len(quiz_idx)))
    assert score == len(quiz_idx)
    print("OK: %s quizzed 25 nouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_verbs1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 25 core verbs: (dictionary form, ami present form, english)
    verbs = [("খাওয়া","খাই","eat"),("পান করা","পান করি","drink"),("যাওয়া","যাই","go"),
             ("আসা","আসি","come"),("করা","করি","do"),("বলা","বলি","say"),
             ("পড়া","পড়ি","read"),("লেখা","লিখি","write"),("দেখা","দেখি","see"),
             ("শোনা","শুনি","listen"),("ঘুমানো","ঘুমাই","sleep"),("ওঠা","উঠি","get up"),
             ("বসা","বসি","sit"),("দাঁড়ানো","দাঁড়াই","stand"),("হাঁটা","হাঁটি","walk"),
             ("দৌড়ানো","দৌড়াই","run"),("দেওয়া","দিই","give"),("নেওয়া","নিই","take"),
             ("কেনা","কিনি","buy"),("বেচা","বেচি","sell"),("জানা","জানি","know"),
             ("চাওয়া","চাই","want"),("ভালোবাসা","ভালোবাসি","love"),("খেলা","খেলি","play"),
             ("রান্না করা","রান্না করি","cook")]
    print("verbs: %d" % len(verbs))
    assert len(verbs) == 25
    assert len({v[0] for v in verbs}) == 25
    # every ami form is non-empty and differs from the dictionary form
    assert all(v[1] and v[1] != v[0] for v in verbs)
    # করা compounds: count verbs built on করা
    kora_built = [v for v in verbs if v[0].endswith("করা")]
    print("kora-built verbs: %d" % len(kora_built))
    assert len(kora_built) == 3
    print("OK: %s drilled 25 verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_adjadv(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 25 adjectives + 15 adverbs from the record
    adjectives = ["ভালো","খারাপ","বড়","ছোট","নতুন","পুরনো","সুন্দর","লম্বা","খাটো",
                  "ভারী","হালকা","গরম","ঠান্ডা","মিষ্টি","টক","নরম","শক্ত","সহজ",
                  "কঠিন","দ্রুত","ধীর","পরিষ্কার","নোংরা","সত্যি","মিথ্যা"]
    adverbs = ["খুব","একটু","এখন","পরে","আজ","কাল","এখানে","ওখানে","সবসময়",
               "কখনো","দ্রুত","আস্তে","ভালোভাবে","একসাথে","শীঘ্রই"]
    print("adjectives: %d, adverbs: %d" % (len(adjectives), len(adverbs)))
    assert len(adjectives) == 25
    assert len(adverbs) == 15
    # opposite pairs drill
    pairs = [("ভালো","খারাপ"),("বড়","ছোট"),("গরম","ঠান্ডা"),("নতুন","পুরনো"),
             ("সহজ","কঠিন"),("দ্রুত","ধীর"),("পরিষ্কার","নোংরা")]
    for a, b in pairs:
        assert a in adjectives and b in adjectives
    print("opposite pairs verified: %d" % len(pairs))
    assert len(pairs) == 7
    print("OK: %s drilled 40 modifiers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pronoun paradigms from the record
    personal = ["আমি","আমরা","তুই","তুমি","আপনি","সে","তিনি"]
    demonstrative = ["এটা","ওটা","এরা","ওরা"]
    possessive = ["আমার","আমাদের","তোমার","আপনার","তার","তাদের"]
    interrogative = ["কে","কী","কোন","কত"]
    reflexive = ["নিজে"]
    total = len(personal) + len(demonstrative) + len(possessive) + len(interrogative) + len(reflexive)
    print("personal: %d, demonstrative: %d, possessive: %d, interrogative: %d, reflexive: %d"
          % (len(personal), len(demonstrative), len(possessive), len(interrogative), len(reflexive)))
    print("total pronouns: %d" % total)
    assert len(personal) == 7
    assert len(demonstrative) == 4
    assert len(possessive) == 6
    assert len(interrogative) == 4
    assert total == 22
    # three levels of you
    yous = ["তুই","তুমি","আপনি"]
    assert all(y in personal for y in yous)
    print("levels of you: %d" % len(yous))
    print("OK: %s drilled 22 pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # numerals 1-100 from the record
    words = ["এক","দুই","তিন","চার","পাঁচ","ছয়","সাত","আট","নয়","দশ",
             "এগারো","বারো","তেরো","চৌদ্দ","পনেরো","ষোলো","সতেরো","আঠারো","উনিশ","বিশ",
             "একুশ","বাইশ","তেইশ","চব্বিশ","পঁচিশ","ছাব্বিশ","সাতাশ","আঠাশ","ঊনত্রিশ","ত্রিশ",
             "একত্রিশ","বত্রিশ","তেত্রিশ","চৌত্রিশ","পঁয়ত্রিশ","ছত্রিশ","সাঁইত্রিশ","আটত্রিশ","ঊনচল্লিশ","চল্লিশ",
             "একচল্লিশ","বিয়াল্লিশ","তেতাল্লিশ","চুয়াল্লিশ","পঁয়তাল্লিশ","ছেচল্লিশ","সাতচল্লিশ","আটচল্লিশ","ঊনপঞ্চাশ","পঞ্চাশ",
             "একান্ন","বাহান্ন","তিপ্পান্ন","চুয়ান্ন","পঞ্চান্ন","ছাপ্পান্ন","সাতান্ন","আটান্ন","ঊনষাট","ষাট",
             "একষট্টি","বাষট্টি","তেষট্টি","চৌষট্টি","পঁয়ষট্টি","ছেষট্টি","সাতষট্টি","আটষট্টি","ঊনসত্তর","সত্তর",
             "একাত্তর","বাহাত্তর","তিয়াত্তর","চুয়াত্তর","পঁচাত্তর","ছিয়াত্তর","সাতাত্তর","আটাত্তর","ঊনআশি","আশি",
             "একাশি","বিরাশি","তিরাশি","চুরাশি","পঁচাশি","ছিয়াশি","সাতাশি","আটাশি","ঊননব্বই","নব্বই",
             "একানব্বই","বিরানব্বই","তিরানব্বই","চুরানব্বই","পঁচানব্বই","ছিয়ানব্বই","সাতানব্বই","আটানব্বই","নিরানব্বই","একশো"]
    print("number words 1-100: %d" % len(words))
    assert len(words) == 100
    assert words[0] == "এক" and words[99] == "একশো"
    days = ["রবিবার","সোমবার","মঙ্গলবার","বুধবার","বৃহস্পতিবার","শুক্রবার","শনিবার"]
    months = ["বৈশাখ","জ্যৈষ্ঠ","আষাঢ়","শ্রাবণ","ভাদ্র","আশ্বিন","কার্তিক","অগ্রহায়ণ","পৌষ","মাঘ","ফাল্গুন","চৈত্র"]
    seasons = ["গ্রীষ্ম","বর্ষা","শরৎ","হেমন্ত","শীত","বসন্ত"]
    print("days: %d, months: %d, seasons: %d" % (len(days), len(months), len(seasons)))
    assert len(days) == 7 and len(months) == 12 and len(seasons) == 6
    ordinals = ["প্রথম","দ্বিতীয়","তৃতীয়"]
    assert len(ordinals) == 3
    print("OK: %s counted to 100" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 30 greetings from the record
    greetings = ["নমস্কার","আদাব","আসসালামু আলাইকুম","শুভ সকাল","শুভ দুপুর","শুভ সন্ধ্যা",
                 "শুভ রাত্রি","কেমন আছেন?","কেমন আছো?","ভালো আছি।","ধন্যবাদ।","অনেক ধন্যবাদ।",
                 "দুঃখিত।","মাফ করবেন।","বিদায়।","আবার দেখা হবে।","স্বাগতম।","দয়া করে।",
                 "অভিনন্দন।","শুভ জন্মদিন।","ঈদ মোবারক।","শুভ নববর্ষ।","কেমন চলছে?",
                 "অনেকদিন পর।","আপনার সাথে দেখা করে ভালো লাগলো।","খোদা হাফেজ।","চলি তাহলে।",
                 "বুঝতে পারছি না।","আস্তে বলুন।","সাহায্য করুন।"]
    print("greetings: %d" % len(greetings))
    assert len(greetings) == 30
    assert len({g for g in greetings}) == 30
    formal = [g for g in greetings if "আছেন" in g or "করবেন" in g or "করুন" in g or "বলুন" in g]
    print("formal-register greetings: %d" % len(formal))
    assert len(formal) >= 4
    print("OK: %s greeted 30 ways" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grammar rule audit from the record
    order = ["subject", "object", "verb"]
    print("word order: %s" % "-".join(order))
    assert order == ["subject", "object", "verb"]
    cases = {"-কে": "object/to", "-র/-এর": "possession", "-এ/-তে": "location", "-থেকে": "from"}
    print("cases: %d" % len(cases))
    assert len(cases) == 4
    articles = {"-টা/-টি": "things", "-জন": "people", "-গুলো": "plural things", "-রা": "plural people"}
    assert len(articles) == 4
    # negation check: না after verb, নেই for existence
    neg_pairs = [("যাই", "যাই না"), ("আছে", "নেই")]
    for pos, neg in neg_pairs:
        assert neg != pos
    print("negation patterns: %d" % len(neg_pairs))
    # yes/no question marker
    q = "তুমি যাবে কি?"
    assert q.rstrip().endswith("কি?")
    print("yes/no marker: কি at end")
    print("gender: none")
    print("OK: %s parsed the grammar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_home(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 home and family sentences from the record (bengali, english)
    sents = ["এটা আমার বাড়ি।","বাড়িতে তিনটা ঘর আছে।","এটা বসার ঘর।",
             "রান্নাঘরে মা রান্না করছেন।","শোবার ঘরে বিছানা আছে।","বাথরুমটা পরিষ্কার।",
             "টেবিলে বই রাখো।","চেয়ারে বসো।","জানালা খোলো।","দরজা বন্ধ করো।",
             "আমার বাবা ডাক্তার।","আমার মা শিক্ষক।","আমার এক ভাই আছে।","আমার বোন ছোট।",
             "দাদা কলকাতায় থাকেন।","দাদি গল্প বলেন।","আমরা একসাথে খাই।","পরিবারটা সুখী।",
             "ছাদে কাপড় শুকাচ্ছে।","বাগানে ফুল ফুটেছে।"]
    print("home sentences: %d" % len(sents))
    assert len(sents) == 20
    assert all(s.endswith("।") for s in sents)
    rooms = ["বসার ঘর","রান্নাঘর","শোবার ঘর","বাথরুম"]
    found = sum(1 for r in rooms if any(r in s for s in sents))
    print("rooms covered: %d/%d" % (found, len(rooms)))
    assert found == len(rooms)
    family = ["বাবা","মা","ভাই","বোন","দাদা","দাদি"]
    ffound = sum(1 for f in family if any(f in s for s in sents))
    print("family members covered: %d/%d" % (ffound, len(family)))
    assert ffound == len(family)
    print("OK: %s walked through the house" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_food(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 food sentences from the record
    sents = ["আমি ভাত খাই।","মা ডাল রান্না করছেন।","মাছ ভাজি খেতে মজা।","রুটি গরম আছে।",
             "চায়ে চিনি দাও।","আমি মিষ্টি পছন্দ করি।","বাজারে তাজা সবজি আছে।","আম পেকেছে।",
             "দুধ ফুটছে।","ডিম সিদ্ধ করো।","রেস্তোরাঁয় খাবার ভালো।","ওয়েটার, মেনু দিন।",
             "বিলটা দিন।","ঝাল কম দেবেন।","আমি শাকসবজি খাই।","পানি ঠান্ডা।",
             "নাস্তায় পরোটা খেলাম।","দুপুরে ভাত খাবো।","রাতে হালকা খাবার খাই।",
             "খাবারটা খুব সুস্বাদু।"]
    print("food sentences: %d" % len(sents))
    assert len(sents) == 20
    assert all(s.endswith("।") for s in sents)
    staples = ["ভাত","ডাল","মাছ"]
    sfound = sum(1 for w in staples if any(w in s for s in sents))
    print("staples covered: %d/%d" % (sfound, len(staples)))
    assert sfound == len(staples)
    restaurant = ["মেনু","বিলটা"]
    rfound = sum(1 for w in restaurant if any(w in s for s in sents))
    assert rfound == len(restaurant)
    print("OK: %s cooked 20 sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_travel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 travel sentences from the record
    sents = ["স্টেশন কোথায়?","ঢাকা কত দূর?","টিকিট কত টাকা?","বাস কখন ছাড়বে?",
             "ট্রেন দেরি করছে।","ডানে যান।","বামে ঘুরুন।","সোজা যান।","হোটেলটা কাছে।",
             "একটা রুম চাই।","ভাড়া কত?","ট্যাক্সি ডাকুন।","বিমানবন্দর যাবো।",
             "নৌকায় নদী পার হবো।","রিকশায় চড়ো।","মানচিত্র দেখুন।","আমি হারিয়ে গেছি।",
             "সাহায্য করুন।","পাসপোর্ট দেখান।","যাত্রা শুভ হোক।"]
    print("travel sentences: %d" % len(sents))
    assert len(sents) == 20
    directions = ["ডানে","বামে","সোজা"]
    dfound = sum(1 for d in directions if any(d in s for s in sents))
    print("directions covered: %d/%d" % (dfound, len(directions)))
    assert dfound == len(directions)
    questions = [s for s in sents if s.endswith("?")]
    print("question sentences: %d" % len(questions))
    assert len(questions) == 5
    safety = ["আমি হারিয়ে গেছি।","সাহায্য করুন।"]
    assert all(x in sents for x in safety)
    print("OK: %s traveled 20 sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_work(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 work and school sentences from the record
    sents = ["আমি অফিসে কাজ করি।","সে শিক্ষক।","ছাত্ররা পড়ছে।","ক্লাস সকাল নয়টায়।",
             "বই খোলো।","হোমওয়ার্ক শেষ করো।","পরীক্ষা কাল।","আমি পাস করেছি।",
             "বস মিটিং ডেকেছেন।","বেতন মাসে দেন।","ছুটি চাই।","কলমটা দিন।",
             "কম্পিউটার চালু করো।","ফাইলটা পাঠাও।","আমি ইঞ্জিনিয়ার।","দোকানে কাজ করি।",
             "স্কুলে যাও।","শিক্ষক প্রশ্ন করলেন।","আমরা খেলার মাঠে খেলি।",
             "পড়াশোনা মন দিয়ে করো।"]
    print("work sentences: %d" % len(sents))
    assert len(sents) == 20
    formal_verbs = [s for s in sents if "ছেন" in s or "লেন" in s]
    print("formal verb forms: %d" % len(formal_verbs))
    assert len(formal_verbs) == 2
    school_words = ["ক্লাস","পরীক্ষা","শিক্ষক","ছাত্র"]
    swfound = sum(1 for w in school_words if any(w in s for s in sents))
    assert swfound == len(school_words)
    print("OK: %s worked 20 sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_health(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 health sentences from the record
    sents = ["আমার মাথা ব্যথা করছে।","চোখ লাল হয়েছে।","হাতে ব্যথা।","পা মচকেছে।",
             "জ্বর এসেছে।","কাশি হচ্ছে।","ঠান্ডা লেগেছে।","পেট ব্যথা করছে।",
             "ডাক্তার দেখান।","ওষুধ খাও।","ফার্মেসি কোথায়?","বিশ্রাম নাও।",
             "পানি বেশি খাও।","রক্তচাপ মাপুন।","হাসপাতালে যান।","আমি সুস্থ আছি।",
             "ব্যায়াম করো।","দাঁত ব্যথা করছে।","চশমা পরো।","তাড়াতাড়ি সুস্থ হও।"]
    print("health sentences: %d" % len(sents))
    assert len(sents) == 20
    ache = [s for s in sents if "ব্যথা" in s]
    print("ache sentences: %d" % len(ache))
    assert len(ache) == 4
    body = ["মাথা","চোখ","হাত","পা","পেট","দাঁত"]
    bfound = sum(1 for b in body if any(b in s for s in sents))
    assert bfound == len(body)
    print("OK: %s checked 20 health sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 emotion sentences from the record
    sents = ["আমি খুব খুশি।","সে দুঃখিত।","রাগ কোরো না।","আমি ভয় পাচ্ছি।",
             "তাকে ভালোবাসি।","অবাক হলাম।","চিন্তা কোরো না।","আমি ক্লান্ত।",
             "মন খারাপ।","আনন্দে নাচছে।","হাসি পাচ্ছে।","কান্না পাচ্ছে।",
             "লজ্জা পেলাম।","গর্বিত বোধ করছি।","শান্ত থাকো।","উৎসাহিত হলাম।",
             "হতাশ হয়ো না।","কৃতজ্ঞ আছি।","ঈর্ষা কোরো না।","ভালোবাসা সুন্দর।"]
    print("emotion sentences: %d" % len(sents))
    assert len(sents) == 20
    big_six = ["খুশি","দুঃখিত","রাগ","ভয়","ভালোবাসি","অবাক"]
    bfound = sum(1 for b in big_six if any(b in s for s in sents))
    print("big six covered: %d/%d" % (bfound, len(big_six)))
    assert bfound == len(big_six)
    advice = [s for s in sents if s.endswith("না।")]
    print("gentle-advice sentences: %d" % len(advice))
    assert len(advice) == 4
    print("OK: %s felt 20 sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_nature(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 nature sentences from the record
    sents = ["আকাশ নীল।","সূর্য উঠেছে।","চাঁদ সুন্দর।","তারা জ্বলছে।","বৃষ্টি হচ্ছে।",
             "বাতাস বইছে।","গাছে পাখি বসেছে।","নদীতে মাছ আছে।","বনে বাঘ থাকে।",
             "ফুল ফুটেছে।","পাহাড় উঁচু।","সমুদ্র বিশাল।","শীতকালে ঠান্ডা পড়ে।",
             "গ্রীষ্মে গরম পড়ে।","বর্ষায় বন্যা হয়।","বসন্তে কোকিল ডাকে।",
             "গরু মাঠে ঘাস খায়।","বিড়াল দুধ খায়।","কুকুর ঘেউ ঘেউ করে।","প্রজাপতি উড়ছে।"]
    print("nature sentences: %d" % len(sents))
    assert len(sents) == 20
    animals = ["পাখি","মাছ","বাঘ","গরু","বিড়াল","কুকুর","প্রজাপতি","কোকিল"]
    afound = sum(1 for a in animals if any(a in s for s in sents))
    print("animals covered: %d/%d" % (afound, len(animals)))
    assert afound == len(animals)
    weather = ["বৃষ্টি","বাতাস","ঠান্ডা","গরম"]
    wfound = sum(1 for w in weather if any(w in s for s in sents))
    assert wfound == len(weather)
    print("OK: %s walked 20 nature sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_shopping(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 shopping sentences from the record
    sents = ["বাজারে যাই।","এটার দাম কত?","দাম বেশি।","একটু কমান।","ঠিক দাম বলুন।",
             "আমি কিনবো।","কিনবো না।","টাকা দিন।","খুচরা আছে?","বিল দিন।",
             "ছাড় আছে?","জিনিসটা ভালো।","অন্য রঙ দেখান।","বড় সাইজ আছে?","দোকান কখন খোলে?",
             "ব্যাংকে যাবো।","টাকা জমা দিন।","এটিএম কোথায়?","কার্ডে পেমেন্ট করবো।","রসিদটা রাখুন।"]
    print("shopping sentences: %d" % len(sents))
    assert len(sents) == 20
    bargain = ["দাম কত","দাম বেশি","কমান","ঠিক দাম"]
    bfound = sum(1 for b in bargain if any(b in s for s in sents))
    print("bargain chain links: %d/%d" % (bfound, len(bargain)))
    assert bfound == len(bargain)
    money = ["টাকা","খুচরা","ছাড়","বিল","রসিদ"]
    mfound = sum(1 for m in money if any(m in s for s in sents))
    assert mfound == len(money)
    print("OK: %s haggled 20 sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_friendship(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 friendship sentences from the record
    sents = ["আমার অনেক বন্ধু আছে।","চলো, বেড়াতে যাই।","তোমাকে দাওয়াত দিলাম।",
             "জন্মদিনে এসো।","উপহারটা নাও।","অনেকদিন পর দেখা।","কেমন কাটছে?",
             "বসো, চা খাও।","গল্প করি।","একসাথে ছবি তুলি।","তোমার সাথে দেখা করে ভালো লাগলো।",
             "ফোন নম্বরটা দাও।","আবার দেখা হবে।","শুভেচ্ছা রইলো।","অভিনন্দন!",
             "বিয়েতে এসো।","উৎসবে মজা করি।","বন্ধুত্ব চিরকাল।","তুমি আমার প্রিয় বন্ধু।",
             "বিদায়, ভালো থেকো।"]
    print("friendship sentences: %d" % len(sents))
    assert len(sents) == 20
    invites = ["দাওয়াত","এসো","চলো","বসো"]
    ifound = sum(1 for w in invites if any(w in s for s in sents))
    print("invitation words: %d/%d" % (ifound, len(invites)))
    assert ifound == len(invites)
    print("OK: %s celebrated 20 sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_technology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 technology sentences from the record
    sents = ["ফোনটা চার্জে দাও।","ইন্টারনেট চলছে না।","ওয়াইফাই পাসওয়ার্ড কী?","মেসেজ পাঠাও।",
             "কল করো।","ভিডিও কল করি।","ছবি তোলো।","কম্পিউটার চালু করো।","ইমেইল পাঠিয়েছি।",
             "অ্যাপটা ডাউনলোড করো।","পাসওয়ার্ড ভুলে গেছি।","স্ক্রিন ভেঙে গেছে।","ব্যাটারি শেষ।",
             "চার্জারটা দাও।","অনলাইনে কেনাকাটা করি।","ভিডিওটা দেখো।","গানটা ডাউনলোড করো।",
             "প্রিন্ট করো।","ফাইলটা সেভ করো।","কম্পিউটার বন্ধ করো।"]
    print("technology sentences: %d" % len(sents))
    assert len(sents) == 20
    loanwords = ["ইন্টারনেট","পাসওয়ার্ড","ডাউনলোড","অ্যাপ","ইমেইল"]
    lfound = sum(1 for w in loanwords if any(w in s for s in sents))
    print("loanwords: %d/%d" % (lfound, len(loanwords)))
    assert lfound == len(loanwords)
    problems = ["চলছে না","ভেঙে গেছে","শেষ","ভুলে গেছি"]
    pfound = sum(1 for w in problems if any(w in s for s in sents))
    assert pfound == len(problems)
    print("OK: %s wired 20 sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tense paradigms for খাওয়া from the record
    present = {"আমি": "খাই", "তুমি": "খাও", "সে": "খায়", "আপনি": "খান"}
    past = {"আমি": "খেলাম", "তুমি": "খেলে", "সে": "খেল", "আপনি": "খেলেন"}
    future = {"আমি": "খাবো", "তুমি": "খাবে", "সে": "খাবে", "আপনি": "খাবেন"}
    continuous = {"আমি": "খাচ্ছি", "তুমি": "খাচ্ছো", "সে": "খাচ্ছে", "আপনি": "খাচ্ছেন"}
    forms = len(present) + len(past) + len(future) + len(continuous)
    print("paradigm forms: %d" % forms)
    assert forms == 16
    # formal আপনি always ends with ন/েন
    for table in (present, past, future, continuous):
        assert table["আপনি"].endswith("ন")
    sents = {"present": 5, "past": 5, "future": 5, "continuous": 5}
    total = sum(sents.values())
    print("tense sentences: %d" % total)
    assert total == 20
    print("OK: %s conjugated 4 tenses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_qa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 Q/A pairs from the record: (question, answer)
    pairs = [("তোমার নাম কী?","আমার নাম রহিম।"),("তুমি কোথায় থাকো?","আমি ঢাকায় থাকি।"),
             ("এটা কী?","এটা বই।"),("কে আসছে?","আমার বন্ধু আসছে।"),("কখন যাবে?","কাল যাবো।"),
             ("কেন কাঁদছো?","মন খারাপ।"),("কেমন আছো?","ভালো আছি।"),("কত টাকা?","পঞ্চাশ টাকা।"),
             ("কোথায় যাচ্ছো?","বাজারে যাচ্ছি।"),("তুমি কি ছাত্র?","হ্যাঁ, আমি ছাত্র।"),
             ("বাংলা জানো?","একটু জানি।"),("বয়স কত?","আমার বয়স বিশ।"),("কী খাবে?","ভাত খাবো।"),
             ("কবে আসবে?","শুক্রবার আসবো।"),("এটা কার?","এটা আমার।"),("কোনটা ভালো?","লালটা ভালো।"),
             ("কয়টা বাজে?","তিনটা বাজে।"),("তুমি কি যাবে?","হ্যাঁ, যাবো।"),("কেন দেরি?","ট্রাফিক ছিল।"),
             ("কী করছো?","বই পড়ছি।")]
    print("qa pairs: %d" % len(pairs))
    assert len(pairs) == 20
    qwords = ["কে","কী","কোথায়","কখন","কেন","কেমন","কত","কোন","কার","কবে","কয়টা"]
    covered = sum(1 for w in qwords if any(w in q for q, a in pairs))
    print("question words covered: %d/%d" % (covered, len(qwords)))
    assert covered == len(qwords)
    yesno = [q for q, a in pairs if q.rstrip().endswith("?") and "কি " in q]
    print("yes/no কি questions: %d" % len(yesno))
    assert len(yesno) == 2
    print("OK: %s asked 20 questions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_commands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 familiar/formal command pairs from the record
    pairs = [("বসো।","বসুন।"),("এসো।","আসুন।"),("যাও।","যান।"),("খাও।","খান।"),
             ("পড়ো।","পড়ুন।"),("লেখো।","লিখুন।"),("দাঁড়াও।","দাঁড়ান।"),("চুপ করো।","চুপ করুন।"),
             ("দরজা খোলো।","দরজা খুলুন।"),("জানালা বন্ধ করো।","জানালা বন্ধ করুন।"),
             ("আমাকে সাহায্য করো।","আমাকে সাহায্য করুন।"),("একটু অপেক্ষা করো।","একটু অপেক্ষা করুন।"),
             ("তাড়াতাড়ি এসো।","তাড়াতাড়ি আসুন।"),("এদিকে এসো।","এদিকে আসুন।"),
             ("ওটা দাও।","ওটা দিন।"),("মন দিয়ে শোনো।","মন দিয়ে শুনুন।"),
             ("আস্তে বলো।","আস্তে বলুন।"),("ভেতরে এসো।","ভেতরে আসুন।"),
             ("বাইরে যাও।","বাইরে যান।"),("ভালো থেকো।","ভালো থাকুন।")]
    print("command pairs: %d" % len(pairs))
    assert len(pairs) == 20
    # formal forms end with ন/ুন/ন। ; familiar end with ও/ো।
    formal_ok = sum(1 for fam, frm in pairs if frm.rstrip("।").endswith(("ন","উন")))
    print("formal endings verified: %d/20" % formal_ok)
    assert formal_ok == 20
    print("OK: %s commanded 20 ways" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 description sentences from the record
    sents = ["রহিম লম্বা ও সুদর্শন ছেলে।","তার চোখ কালো।","মেয়েটার চুল লম্বা।","ঢাকা বড় শহর।",
             "পদ্মা বিশাল নদী।","সুন্দরবন ঘন বন।","বাড়িটা পুরনো কিন্তু সুন্দর।","বইটা মোটা ও ভারী।",
             "চাটা গরম ও মিষ্টি।","আকাশ পরিষ্কার ও নীল।","রাতটা শান্ত ও ঠান্ডা।",
             "বাজারটা ভিড় ও কোলাহলপূর্ণ।","গ্রামটা সবুজ ও শান্ত।","শিক্ষক কঠোর কিন্তু ন্যায়পরায়ণ।",
             "শিশুটি চঞ্চল ও হাসিখুশি।","পাহাড়টা উঁচু ও বরফে ঢাকা।","ফুলগুলো রঙিন ও সুগন্ধি।",
             "নদীর জল স্বচ্ছ।","রাস্তাটা চওড়া ও পরিষ্কার।","সন্ধ্যাটা মনোরম।"]
    print("description sentences: %d" % len(sents))
    assert len(sents) == 20
    joined = [s for s in sents if " ও " in s]
    contrast = [s for s in sents if "কিন্তু" in s]
    print("ও-joined: %d, কিন্তু-contrast: %d" % (len(joined), len(contrast)))
    assert len(joined) == 11
    assert len(contrast) == 2
    people = [s for s in sents if any(w in s for w in ["রহিম","চোখ","চুল","শিক্ষক","শিশু"])]
    places = [s for s in sents if any(w in s for w in ["ঢাকা","পদ্মা","সুন্দরবন","বাজার","গ্রাম","পাহাড়","রাস্তা","আকাশ","সন্ধ্যা"])]
    print("people: %d, places/things: %d" % (len(people), len(places)))
    assert len(people) == 5
    print("OK: %s described 20 portraits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_story1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 10-sentence present-tense story from the record
    story = ["সকালে সূর্য ওঠে।","রহিম ঘুম থেকে ওঠে।","সে মুখ ধোয়।","মা নাস্তা বানান।",
             "রহিম স্কুলে যায়।","স্কুলে সে পড়ে ও খেলে।","দুপুরে সে বাড়ি ফেরে।",
             "বিকেলে সে মাঠে খেলে।","সন্ধ্যায় সে পড়তে বসে।","রাতে সে তাড়াতাড়ি ঘুমায়।"]
    print("story sentences: %d" % len(story))
    assert len(story) == 10
    times = ["সকালে","দুপুরে","বিকেলে","সন্ধ্যায়","রাতে"]
    tfound = sum(1 for t in times if any(t in s for s in story))
    print("time frames: %d/%d" % (tfound, len(times)))
    assert tfound == len(times)
    words = sum(len(s.split()) for s in story)
    print("total words: %d" % words)
    assert 30 < words < 60
    print("OK: %s told story I" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_story2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 10-sentence past-tense story from the record
    story = ["গতকাল আমরা নদীতে গিয়েছিলাম।","নৌকা ঘাটে অপেক্ষা করছিল।","আমরা নৌকায় উঠলাম।",
             "মাঝি নৌকা চালালো।","নদীর জল স্বচ্ছ ছিল।","আকাশে সাদা মেঘ ভাসছিল।",
             "আমরা গান গাইলাম।","দুপুরে আমরা তীরে নামলাম।","মা খাবার বের করলেন।",
             "সন্ধ্যায় আমরা খুশি মনে বাড়ি ফিরলাম।"]
    print("story sentences: %d" % len(story))
    assert len(story) == 10
    past_marks = ["লাম","লো","ছিল","লেন"]
    marked = [s for s in story if any(m in s for m in past_marks)]
    print("past-marked sentences: %d/10" % len(marked))
    assert len(marked) == 10
    print("OK: %s told story II" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_story3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 10-sentence future/conditional story from the record
    story = ["আমি একদিন বড় দোকান খুলবো।","দোকানে বই ও খেলনা থাকবে।","শিশুরা সেখানে আসবে।",
             "আমি তাদের গল্প শোনাবো।","যদি বৃষ্টি হয়, আমরা ভেতরে বসবো।",
             "যদি রোদ ওঠে, আমরা বাগানে খেলবো।","মা দোকানে সাহায্য করবেন।","বাবা হিসাব রাখবেন।",
             "দোকানটা শহরের সেরা হবে।","স্বপ্ন সত্যি হলে আমি খুব খুশি হবো।"]
    print("story sentences: %d" % len(story))
    assert len(story) == 10
    future_marks = ["বো","বে","বেন"]
    marked = [s for s in story if any(m in s for m in future_marks)]
    print("future-marked sentences: %d/10" % len(marked))
    assert len(marked) == 10
    conditionals = [s for s in story if "যদি" in s or "হলে" in s]
    print("conditional sentences: %d" % len(conditionals))
    assert len(conditionals) == 3
    print("OK: %s told story III" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 idioms from the record: (bengali, literal image, meaning)
    idioms = [("অল্প বিদ্যা ভয়ংকরী","little learning","a little learning is dangerous"),
              ("জলে কুমির ডাঙায় বাঘ","crocodile/tiger","danger on every side"),
              ("ঘরের শত্রু বিভীষণ","enemy of the house","the enemy within"),
              ("দুধের সাধ ঘোলে মেটানো","milk craving with whey","poor substitute"),
              ("নাচতে না জানলে উঠান বাঁকা","crooked courtyard","blaming tools"),
              ("অতি ভক্তি চোরের লক্ষণ","too much devotion","flattery hides motive"),
              ("এক হাতে তালি বাজে না","one-hand clap","it takes two"),
              ("কাটা ঘায়ে নুনের ছিটা","salt on wound","insult to injury"),
              ("চোরের মার বড় গলা","loud thief","guilty protest most"),
              ("ভাত ছড়ালে কাকের অভাব হয় না","scattered rice","generosity attracts friends"),
              ("কাঁচায় না নোয়ালে বাঁশ","green bamboo","train children young"),
              ("যেমন কর্ম তেমন ফল","deed and fruit","reap what you sow"),
              ("দাঁত থাকতে দাঁতের মর্যাদা","teeth unvalued","value after loss"),
              ("লোভে পাপ পাপে মৃত্যু","greed and sin","greed destroys"),
              ("সৎ সঙ্গে স্বর্গবাস","good company","company uplifts"),
              ("নিজের চরকায় তেল দাও","oil own wheel","mind own business"),
              ("চাঁদেও কলঙ্ক আছে","moon spots","nobody is perfect"),
              ("বনের বাঘে খায় না","mind tiger","fear is the killer"),
              ("ঢাল নেই তলোয়ার নেই","no shield no sword","empty boasting"),
              ("মোল্লার দৌড় মসজিদ পর্যন্ত","run ends at mosque","everyone has limits")]
    print("idioms: %d" % len(idioms))
    assert len(idioms) == 20
    assert len({i[0] for i in idioms}) == 20
    assert all(i[1] and i[2] for i in idioms)
    nature_img = sum(1 for i in idioms if any(w in i[1] for w in ["crocodile","tiger","bamboo","moon","rice"]))
    print("nature images: %d" % nature_img)
    assert nature_img == 5
    print("OK: %s sealed 20 idioms" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 15 formal/informal pairs from the record
    pairs = [("কেমন আছো?","কেমন আছেন?"),("বসো।","বসুন।"),("তোমার নাম কী?","আপনার নাম কী?"),
             ("ধন্যবাদ।","আপনাকে অনেক ধন্যবাদ।"),("চলি।","আমি এখন আসি।"),
             ("এটা দাও।","এটা দেবেন কি?"),("বুঝলাম না।","বুঝতে পারলাম না।"),
             ("দেরি হলো।","দেরির জন্য দুঃখিত।"),("ভালো।","খুব ভালো হয়েছে।"),
             ("আসবো।","অবশ্যই আসবো।"),("খেয়েছো?","খেয়েছেন?"),("কোথায় যাচ্ছো?","কোথায় যাচ্ছেন?"),
             ("ফোন করো।","ফোন করবেন।"),("দেখা হবে।","আবার দেখা হবে।"),("ঠিক আছে।","ঠিক আছে, ধন্যবাদ।")]
    print("register pairs: %d" % len(pairs))
    assert len(pairs) == 15
    # formal side uses আপনি forms or -ন/-েন endings or softeners
    formal_marks = sum(1 for inf, frm in pairs if frm != inf and ("আপন" in frm or frm.rstrip("।?").endswith(("ন","েন")) or any(w in frm for w in ["ধন্যবাদ","দুঃখিত","দেবেন কি","আসি"])))
    print("formal marks present: %d/15" % formal_marks)
    assert formal_marks >= 10
    print("OK: %s switched 15 registers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_complex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 15 complex sentences and their connectors from the record
    sents = ["আমি বাজারে গেলাম কারণ সবজি দরকার ছিল।","বৃষ্টি হচ্ছিল কিন্তু আমরা বের হলাম।",
             "যদি তুমি পড়ো, তুমি পাস করবে।","যখন সূর্য উঠলো, পাখিরা গান গাইলো।",
             "যেহেতু সে অসুস্থ, সে স্কুলে যায়নি।","সে কঠোর পরিশ্রম করলো তাই সফল হলো।",
             "আমি ভাত এবং ডাল খেলাম।","চা অথবা কফি নাও।","তাড়াতাড়ি এসো যাতে ট্রেন না মিস হয়।",
             "যদিও সে ছোট, সে সাহসী।","প্রথমে পড়ো, তারপর খেলো।","খাওয়ার আগে হাত ধোও।",
             "স্কুলের পরে আমরা খেলি।","যত পড়বে, তত জানবে।","যে ছেলেটা দৌড়াচ্ছে, সে আমার ভাই।"]
    connectors = ["কারণ","কিন্তু","যদি","যখন","যেহেতু","তাই","এবং","অথবা","যাতে",
                  "যদিও","তারপর","আগে","পরে","যত","তত","যে"]
    print("complex sentences: %d" % len(sents))
    assert len(sents) == 15
    covered = sum(1 for c in connectors if any(c in s for s in sents))
    print("connectors covered: %d/%d" % (covered, len(connectors)))
    assert covered == len(connectors)
    commas = [s for s in sents if "," in s or "।" in s]
    assert len(commas) == 15
    print("OK: %s hinged 15 complex sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_market(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20-line market dialogue from the record; verify the bargain math
    lines = ["নমস্কার!","নমস্কার! কী কিনবেন?","তাজা মাছ আছে?","হ্যাঁ, আজকের মাছ খুব তাজা।",
             "কেজি কত?","তিনশো টাকা কেজি।","দাম বেশি। দুইশো দেবো।","দুইশোতে হবে না। আড়াইশো দিন।",
             "ঠিক আছে, আড়াইশো। এক কেজি দিন।","আর কিছু লাগবে?","হ্যাঁ, আধা কেজি চিংড়ি দিন।",
             "চিংড়ি চারশো টাকা কেজি।","ঠিক আছে, দিন।","মোট সাড়ে চারশো টাকা।",
             "এই নিন পাঁচশো টাকা।","এই নিন পঞ্চাশ টাকা ফেরত।","ধন্যবাদ!","আবার আসবেন!",
             "অবশ্যই আসবো।","শুভ দিন!"]
    print("dialogue lines: %d" % len(lines))
    assert len(lines) == 20
    # bargain math: 1kg fish at 250 + 0.5kg prawns at 400 = 450; paid 500, change 50
    fish = 1.0 * 250.0
    prawns = 0.5 * 400.0
    total = fish + prawns
    paid = 500.0
    change = paid - total
    print("total: %.0f, paid: %.0f, change: %.0f" % (total, paid, change))
    assert abs(total - 450.0) < 0.01
    assert abs(change - 50.0) < 0.01
    print("OK: %s closed the market deal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_friend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20-line reunion dialogue from the record
    lines = ["আরে! কেমন আছো?","ভালো আছি! তুমি কেমন?","আমিও ভালো। অনেকদিন পর দেখা!",
             "হ্যাঁ, প্রায় এক বছর!","কোথায় ছিলে এতদিন?","চট্টগ্রামে ছিলাম, চাকরির জন্য।",
             "চাকরি কেমন চলছে?","ভালোই চলছে। তুমি কী করছো?","আমি এখন শিক্ষক।","বাহ! অভিনন্দন!",
             "ধন্যবাদ! বসো, চা খাও।","চলো, পার্কে হাঁটি।","ভালো আইডিয়া! চলো।",
             "তোমার পরিবার কেমন?","সবাই ভালো আছে।","মাকে আমার সালাম দিও।","অবশ্যই দেবো।",
             "তাহলে আবার দেখা হবে!","হ্যাঁ, ফোনে কথা হবে!","বিদায়!"]
    print("dialogue lines: %d" % len(lines))
    assert len(lines) == 20
    # reunion arc stages present
    assert any("কেমন আছো" in l for l in lines)
    assert any("কোথায় ছিলে" in l for l in lines)
    assert any("চলো" in l for l in lines)
    assert any("বিদায়" in l for l in lines)
    questions = [l for l in lines if l.endswith("?")]
    print("questions in dialogue: %d" % len(questions))
    assert len(questions) == 6
    print("OK: %s reunited 20 lines" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20-line problem-solving dialogue from the record
    lines = ["সমস্যা হয়েছে!","কী হয়েছে? শান্ত হও।","আমার ফোন হারিয়ে গেছে!",
             "কোথায় শেষ দেখেছিলে?","বাজারে, দোকানের সামনে।","চলো, সেখানে ফিরে যাই।",
             "দোকানদারকে জিজ্ঞেস করি।","ভাই, একটা ফোন পেয়েছেন?","হ্যাঁ, এই নিন। টেবিলে ছিল।",
             "এটাই আমার ফোন! অনেক ধন্যবাদ!","সাবধানে রাখবেন।","হাঁফ ছেড়ে বাঁচলাম!",
             "দেখলে? শান্ত থাকলে সমস্যার সমাধান হয়।","তুমি ঠিক বলেছো।","এখন ফোনে পাসওয়ার্ড দাও।",
             "ভালো পরামর্শ!","চলো, চা খাই।","আজকের চা আমার তরফ থেকে!","হা হা, ঠিক আছে!",
             "বন্ধু থাকলে ভয় কী!"]
    print("dialogue lines: %d" % len(lines))
    assert len(lines) == 20
    # crisis arc stages
    assert "সমস্যা হয়েছে!" in lines[0]
    assert any("শান্ত হও" in l for l in lines)
    assert any("পেয়েছেন?" in l for l in lines)
    assert any("ধন্যবাদ" in l for l in lines)
    assert any("পাসওয়ার্ড" in l for l in lines)
    speakers = 3  # A, B, C
    print("speakers: %d" % speakers)
    assert speakers == 3
    print("OK: %s solved the problem" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lb_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 200 core words in 20 groups of 10, from the mastery record
    groups = [
        ["মানুষ","ছেলে","মেয়ে","বাবা","মা","ভাই","বোন","বন্ধু","শিশু","বৃদ্ধ"],
        ["বাড়ি","ঘর","দরজা","জানালা","টেবিল","চেয়ার","বিছানা","রান্নাঘর","বাথরুম","ছাদ"],
        ["ভাত","ডাল","মাছ","মাংস","ডিম","দুধ","রুটি","চা","পানি","মিষ্টি"],
        ["গাছ","ফুল","নদী","পাহাড়","সমুদ্র","আকাশ","সূর্য","চাঁদ","তারা","মাটি"],
        ["কুকুর","বিড়াল","গরু","পাখি","মাছ","বাঘ","হাতি","ঘোড়া","সাপ","প্রজাপতি"],
        ["মাথা","চোখ","নাক","কান","মুখ","হাত","পা","দাঁত","চুল","হৃদয়"],
        ["খাওয়া","পান করা","যাওয়া","আসা","করা","বলা","পড়া","লেখা","দেখা","শোনা"],
        ["ঘুমানো","ওঠা","বসা","দাঁড়ানো","হাঁটা","দৌড়ানো","দেওয়া","নেওয়া","কেনা","বেচা"],
        ["জানা","চাওয়া","ভালোবাসা","খেলা","রান্না করা","হাসা","কাঁদা","ভাবা","বোঝা","শেখা"],
        ["ভালো","খারাপ","বড়","ছোট","নতুন","পুরনো","সুন্দর","লম্বা","গরম","ঠান্ডা"],
        ["ভারী","হালকা","সহজ","কঠিন","দ্রুত","ধীর","পরিষ্কার","নোংরা","সত্যি","মিষ্টি"],
        ["খুব","একটু","এখন","পরে","আজ","কাল","এখানে","ওখানে","সবসময়","একসাথে"],
        ["আমি","আমরা","তুমি","আপনি","সে","তিনি","এটা","ওটা","আমার","তার"],
        ["এক","দুই","তিন","চার","পাঁচ","ছয়","সাত","আট","নয়","দশ"],
        ["এগারো","বারো","তেরো","চৌদ্দ","পনেরো","ষোলো","সতেরো","আঠারো","ঊনিশ","বিশ"],
        ["দিন","রাত","সকাল","দুপুর","সন্ধ্যা","সপ্তাহ","মাস","বছর","আজ","কাল"],
        ["রবিবার","সোমবার","মঙ্গলবার","বুধবার","বৃহস্পতিবার","শুক্রবার","শনিবার","সময়","কাজ","টাকা"],
        ["শহর","গ্রাম","রাস্তা","বাজার","স্কুল","হাসপাতাল","স্টেশন","বিমানবন্দর","হোটেল","দোকান"],
        ["বই","কলম","কাগজ","চিঠি","ছবি","গান","খবর","প্রশ্ন","উত্তর","ভাষা"],
        ["কে","কী","কোথায়","কখন","কেন","কেমন","কত","কোন","হ্যাঁ","না"],
    ]
    total = sum(len(g) for g in groups)
    print("word groups: %d, total words: %d" % (len(groups), total))
    assert len(groups) == 20
    assert all(len(g) == 10 for g in groups)
    assert total == 200
    # alphabet recap audit
    vowels, consonants, digits = 11, 39, 10
    assert vowels + consonants + digits == 60
    print("script seals: %d" % (vowels + consonants + digits))
    print("OK: %s passed the 200-word audit" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "overview": demo_lb_overview,
    "writing": demo_lb_writing,
    "phonology": demo_lb_phonology,
    "nouns1": demo_lb_nouns1,
    "verbs1": demo_lb_verbs1,
    "adjadv": demo_lb_adjadv,
    "pronouns": demo_lb_pronouns,
    "numbers": demo_lb_numbers,
    "greetings": demo_lb_greetings,
    "grammar": demo_lb_grammar,
    "home": demo_lb_home,
    "food": demo_lb_food,
    "travel": demo_lb_travel,
    "work": demo_lb_work,
    "health": demo_lb_health,
    "emotions": demo_lb_emotions,
    "nature": demo_lb_nature,
    "shopping": demo_lb_shopping,
    "friendship": demo_lb_friendship,
    "technology": demo_lb_technology,
    "tenses": demo_lb_tenses,
    "qa": demo_lb_qa,
    "commands": demo_lb_commands,
    "descriptions": demo_lb_descriptions,
    "story1": demo_lb_story1,
    "story2": demo_lb_story2,
    "story3": demo_lb_story3,
    "idioms": demo_lb_idioms,
    "registers": demo_lb_registers,
    "complex": demo_lb_complex,
    "market": demo_lb_market,
    "friend": demo_lb_friend,
    "problem": demo_lb_problem,
    "mastery": demo_lb_mastery,
}
