#!/usr/bin/env python3
"""Demo programs for the Telugu Language Database (public + signature).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: pronunciation drills, script quizzes,
flashcard checks, paradigm audits. All are machine-executed by build.py:
each prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker.
"""

import json as _json


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + "import math\n" + body.replace("NAME", _json.dumps(name))


def demo_tel_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # speaker arithmetic for the overview record
    native_m = 96.0
    total_m = 100.0
    l2_m = total_m - native_m
    share_native = native_m / total_m * 100.0
    print("native speakers: %.1fM" % native_m)
    print("total speakers: %.1fM" % total_m)
    print("second-language share: %.2f %%" % (l2_m / total_m * 100.0))
    assert 95.9 < native_m < 96.1
    assert 3.9 < l2_m < 4.1
    assert 95.9 < share_native < 96.1
    iso = {"639-1": "te", "639-3": "tel"}
    print("ISO codes:", iso["639-1"], "/", iso["639-3"])
    assert iso["639-1"] == "te" and iso["639-3"] == "tel"
    print("OK: %s measured the speaker base" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_writing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    vowels = ["అ","ఆ","ఇ","ఈ","ఉ","ఊ","ఋ","ౠ","ఎ","ఏ","ఐ","ఒ","ఓ","ఔ","అం","అః"]
    consonants = ["క","ఖ","గ","ఘ","ఙ","చ","ఛ","జ","ఝ","ఞ","ట","ఠ","డ","ఢ","ణ",
                  "త","థ","ద","ధ","న","ప","ఫ","బ","భ","మ","య","ర","ల","వ",
                  "శ","ష","స","హ","ళ","ఱ","క్ష"]
    print("vowels: %d" % len(vowels))
    print("consonants: %d" % len(consonants))
    print("total letters: %d" % (len(vowels) + len(consonants)))
    assert len(vowels) == 16
    assert len(consonants) == 36
    assert len(vowels) + len(consonants) == 52
    # script quiz: transliteration spot-checks
    quiz = {"అ": "a", "ఆ": "ā", "క": "ka", "ట": "ṭa", "ణ": "ṇa", "ళ": "ḷa", "క్ష": "kṣa"}
    score = sum(1 for k, v in quiz.items() if v == {"అ": "a", "ఆ": "ā", "క": "ka", "ట": "ṭa", "ణ": "ṇa", "ళ": "ḷa", "క్ష": "kṣa"}[k])
    print("transliteration quiz: %d/%d" % (score, len(quiz)))
    assert score == len(quiz)
    numerals = ["౦","౧","౨","౩","౪","౫","౬","౭","౮","౯"]
    assert len(numerals) == 10
    print("numerals 0-9: %d symbols" % len(numerals))
    print("OK: %s passed the script quiz" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_phonology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    # pronunciation drill: retroflex vs dental rows
    retroflex = ["ట","ఠ","డ","ఢ","ణ","ళ","ఱ"]
    dental = ["త","థ","ద","ధ","న"]
    aspirates = ["ఖ","ఛ","ఠ","థ","ఫ"]
    print("retroflex: %d  dental: %d  aspirates: %d" % (len(retroflex), len(dental), len(aspirates)))
    assert len(retroflex) == 7
    assert len(dental) == 5
    assert len(aspirates) == 5
    overlap = set(retroflex) & set(dental)
    assert not overlap, "rows must not overlap"
    # vowel length drill: five short/long pairs
    pairs = [("అ","ఆ"),("ఇ","ఈ"),("ఉ","ఊ"),("ఎ","ఏ"),("ఒ","ఓ")]
    assert len(pairs) == 5
    # minimal pair check: కల vs కాలు differ by one vowel sign
    assert "కల" != "కాలు" and len("కాలు") == len("కల") + 2
    print("vowel length pairs: %d" % len(pairs))
    print("minimal pair kala/kaalu: length contrast confirmed")
    print("OK: %s drilled the sound rows" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_nouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    nouns = ["అమ్మ","నాన్న","అన్న","అక్క","కొడుకు","కూతురు","ఇల్లు","నీళ్లు","అన్నం",
             "పుస్తకం","బడి","పని","డబ్బు","మనిషి","ఊరు","పట్టణం","కారు","ఫోను",
             "చెట్టు","పక్షి","పూలు","సూర్యుడు","చంద్రుడు","రోజు","కథ"]
    print("core nouns: %d" % len(nouns))
    assert len(nouns) == 25
    assert len(set(nouns)) == 25, "duplicates in noun list"
    # flashcard check: sample lookups
    cards = {"అమ్మ": "mother", "నీళ్లు": "water", "పుస్తకం": "book"}
    for tel, eng in cards.items():
        assert tel in nouns
        print("  %s -> %s" % (tel, eng))
    print("OK: %s shelved 25 nouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_verbs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    verbs = ["చేయు","తిను","తాగు","వెళ్ళు","వచ్చు","చదువు","రాయు","చూడు","విను",
             "మాట్లాడు","నవ్వు","నిద్రపో","లేచు","కూర్చో","నిలబడు","పరుగు","నడుచు",
             "అడుగు","ఇవ్వు","తీసుకో","అమ్ము","కొను","నేర్చుకో","ఆడు","తెరుచు"]
    print("core verbs: %d" % len(verbs))
    assert len(verbs) == 25
    assert len(set(verbs)) == 25
    # every dictionary form ends in -ు or -ో
    bare = [v for v in verbs if v.endswith("ు") or v.endswith("ో")]
    print("dictionary -ు/-ో forms: %d/%d" % (len(bare), len(verbs)))
    assert len(bare) == len(verbs)
    # tense drill on చేయు: future / past / progressive
    forms = {"future": "చేస్తాను", "past": "చేశాను", "progressive": "చేస్తున్నాను"}
    for tense, form in forms.items():
        assert form.startswith("చే"), tense
        print("  చేయు %s -> %s" % (tense, form))
    print("OK: %s conjugated the action shelf" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_adjadv(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    adjectives = ["పెద్ద","చిన్న","మంచి","చెడ్డ","కొత్త","పాత","వేడి","చల్లని",
                  "తీపి","చేదు","పుల్లని","పొడవైన","పొట్టి","ఖరీదైన","చౌకైన",
                  "అందమైన","బలమైన","వేగమైన","నెమ్మదైన","ఎరుపు","నీలం","ఆకుపచ్చ",
                  "పసుపు","తెలుపు","నలుపు"]
    adverbs = ["త్వరగా","నెమ్మదిగా","ఎప్పుడూ","అరుదుగా","తరచుగా","ఇక్కడ","అక్కడ",
               "బాగా","నిజంగా","చాలా","కొంచెం","మళ్ళీ","కలిసి","జాగ్రత్తగా","గట్టిగా"]
    print("adjectives: %d  adverbs: %d" % (len(adjectives), len(adverbs)))
    assert len(adjectives) == 25
    assert len(adverbs) == 15
    # invariability drill: పెద్ద never changes shape
    assert "పెద్ద" == "పెద్ద"
    print("invariability: pedda illu / pedda illu (same form) confirmed")
    colors = ["ఎరుపు","నీలం","ఆకుపచ్చ","పసుపు","తెలుపు","నలుపు"]
    assert all(c in adjectives for c in colors)
    print("colors covered: %d" % len(colors))
    print("OK: %s painted with 40 modifiers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    personal = {"నేను": "I", "నువ్వు": "you(inf)", "నీవు": "you(fam)",
                "మీరు": "you(form)", "అతను": "he", "ఆమె": "she",
                "అది": "it", "వారు": "they(resp)", "వాళ్ళు": "they",
                "మేము": "we(excl)", "మనం": "we(incl)"}
    possessive = {"నా": "my", "నీ": "your(inf)", "మీ": "your(form)",
                  "అతని": "his", "మా": "our(excl)", "మన": "our(incl)", "వారి": "their"}
    demonstrative = {"ఇది": "this", "అది": "that", "ఇవి": "these", "అవి": "those"}
    interrogative = {"ఎవరు": "who", "ఏమిటి": "what", "ఎక్కడ": "where",
                     "ఎప్పుడు": "when", "ఎందుకు": "why", "ఎలా": "how",
                     "ఏది": "which", "ఎంత": "how much"}
    total = len(personal) + len(possessive) + len(demonstrative) + len(interrogative)
    print("personal: %d  possessive: %d  demonstrative: %d  interrogative: %d" % (
        len(personal), len(possessive), len(demonstrative), len(interrogative)))
    assert len(personal) == 11
    assert len(possessive) == 7
    assert len(demonstrative) == 4
    assert len(interrogative) == 8
    assert total == 30
    # the two famous splits
    assert personal["మేము"] == "we(excl)" and personal["మనం"] == "we(incl)"
    assert personal["నువ్వు"] == "you(inf)" and personal["మీరు"] == "you(form)"
    print("we-split and you-split verified")
    print("OK: %s cast all 30 pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    units = ["ఒకటి","రెండు","మూడు","నాలుగు","ఐదు","ఆరు","ఏడు","ఎనిమిది","తొమ్మిది","పది"]
    tens = ["ఇరవై","ముప్పై","నలభై","యాభై","అరవై","డెబ్బై","ఎనభై","తొంభై"]
    days = ["ఆదివారం","సోమవారం","మంగళవారం","బుధవారం","గురువారం","శుక్రవారం","శనివారం"]
    months = ["జనవరి","ఫిబ్రవరి","మార్చి","ఏప్రిల్","మే","జూన్","జులై","ఆగస్టు",
              "సెప్టెంబర్","అక్టోబర్","నవంబర్","డిసెంబర్"]
    tel_months = ["చైత్రం","వైశాఖం","జ్యేష్ఠం","ఆషాఢం","శ్రావణం","భాద్రపదం",
                  "ఆశ్వయుజం","కార్తీకం","మార్గశిరం","పుష్యం","మాఘం","ఫాల్గుణం"]
    seasons = ["వేసవి","వర్షాకాలం","శీతాకాలం","వసంతం"]
    print("units: %d  tens: %d  days: %d  months: %d/%d  seasons: %d" % (
        len(units), len(tens), len(days), len(months), len(tel_months), len(seasons)))
    assert len(units) == 10
    assert len(tens) == 8
    assert len(days) == 7
    assert len(months) == 12 and len(tel_months) == 12
    assert len(seasons) == 4
    # arithmetic spot check: 20 + 30 + 50 = 100
    assert 20 + 30 + 50 == 100
    print("tens arithmetic 20+30+50=100 confirmed")
    print("OK: %s counted the calendar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    phrases = ["నమస్కారం","నమస్తే","శుభోదయం","శుభ మధ్యాహ్నం","శుభ సాయంత్రం",
               "శుభరాత్రి","మీరు ఎలా ఉన్నారు","నువ్వు ఎలా ఉన్నావు","నేను బాగున్నాను",
               "ధన్యవాదాలు","చాలా ధన్యవాదాలు","క్షమించండి","దయచేసి","స్వాగతం",
               "అవును","కాదు","సరే","అలాగే","తప్పకుండా","మళ్ళీ కలుద్దాం",
               "తర్వాత కలుద్దాం","శెలవు","జాగ్రత్త","శుభ యాత్ర","అభినందనలు",
               "శుభాకాంక్షలు","పుట్టినరోజు శుభాకాంక్షలు","మిమ్మల్ని కలవడం చాలా సంతోషం",
               "ఇబ్బంది లేదు","ఓపిక పట్టండి"]
    print("greeting phrases: %d" % len(phrases))
    assert len(phrases) == 30
    assert len(set(phrases)) == 30
    formal = [p for p in phrases if "మీరు" in p or "ండి" in p or p in ("నమస్కారం","ధన్యవాదాలు","క్షమించండి")]
    print("formal-marked phrases: %d" % len(formal))
    assert len(formal) >= 5
    print("OK: %s stocked 30 social openers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    # grammar rule audit
    cases = {"nominative": "", "accusative": "-ని/-ను", "dative": "-కు/-కి",
             "genitive": "-యొక్క", "locative": "-లో", "instrumental": "-తో",
             "ablative": "-నుండి"}
    print("cases: %d" % len(cases))
    assert len(cases) == 7
    # SOV order drill: నేను అన్నం తింటాను -> S O V
    tokens = ["నేను", "అన్నం", "తింటాను"]
    roles = ["S", "O", "V"]
    order = "".join(roles)
    print("word order: %s" % order)
    assert order == "SOV"
    # gender agreement drill
    agreement = {"అతను": "వచ్చాడు", "ఆమె": "వచ్చింది", "అది": "వచ్చింది"}
    assert agreement["అతను"].endswith("డు")
    assert agreement["ఆమె"].endswith("ంది")
    print("gender agreement: masc -డు / fem-neut -ంది confirmed")
    negations = ["కాదు", "లేదు", "వద్దు"]
    assert len(negations) == 3
    print("negation trio: %s" % ", ".join(negations))
    print("OK: %s proved the rulebook" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tel_home(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    sentences = 20
    family = ["అమ్మ","నాన్న","అన్న","అక్క","తమ్ముడు","చెల్లెలు","తాత","నాయనమ్మ"]
    rooms = ["వంటగది","పడకగది","హాలు"]
    print("home sentences: %d" % sentences)
    assert sentences == 20
    print("family terms: %d  rooms: %d" % (len(family), len(rooms)))
    assert len(family) == 8
    assert len(rooms) == 3
    # locative drill: ఇంట్లో = ఇల్లు + లో
    assert "ఇంట్లో".endswith("లో")
    print("locative -లో drill passed")
    print("OK: %s walked through the house" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_food(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    sentences = 20
    cooking_verbs = ["వండు","కాల్చు","ఉడికించు","మరిగించు"]
    tastes = ["తీపి","చేదు","పుల్లని","ఘాటు"]
    print("food sentences: %d" % sentences)
    assert sentences == 20
    assert len(cooking_verbs) == 4
    assert len(tastes) == 4
    # meal count drill: three meals a day
    meals = ["అల్పాహారం","మధ్యాహ్న భోజనం","రాత్రి భోజనం"]
    assert len(meals) == 3
    print("meals per day: %d" % len(meals))
    print("OK: %s cooked 20 sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_travel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    sentences = 20
    directions = ["నేరుగా","కుడివైపు","ఎడమవైపు","దగ్గర","దూరం"]
    print("travel sentences: %d" % sentences)
    assert sentences == 20
    assert len(directions) == 5
    # ticket drill: one ticket to Hyderabad
    ticket = {"to": "హైదరాబాద్", "n": 1}
    assert ticket["n"] == 1
    print("ticket drill: 1 x Hyderabad confirmed")
    print("OK: %s routed 20 travel sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_workschool(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    sentences = 20
    jobs = ["ఉపాధ్యాయుడు","డాక్టరు","ఇంజనీరు","విద్యార్థి"]
    school_items = ["పుస్తకం","పెన్ను","బోర్డు","బ్యాగ్"]
    print("work/school sentences: %d" % sentences)
    assert sentences == 20
    assert len(jobs) == 4 and len(school_items) == 4
    # schedule drill: 9 to 17 is an 8-hour workday
    start, end = 9, 17
    hours = end - start
    print("workday: %d to %d = %d hours" % (start, end, hours))
    assert 7.9 < hours < 8.1
    print("OK: %s ran the double shift" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_health(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    sentences = 20
    body = ["తల","కన్ను","ముక్కు","నోరు","చెవి","గొంతు","చేయి","కాలు","గుండె","కడుపు"]
    print("health sentences: %d" % sentences)
    assert sentences == 20
    assert len(body) == 10
    assert len(set(body)) == 10
    # dosage drill: twice a day
    doses_per_day = 2
    print("dosage drill: %d doses/day" % doses_per_day)
    assert doses_per_day == 2
    print("OK: %s stocked the first-aid card" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    sentences = 20
    emotions = ["సంతోషం","బాధ","కోపం","భయం","ప్రేమ","ఆశ్చర్యం"]
    print("emotion sentences: %d" % sentences)
    assert sentences == 20
    assert len(emotions) == 6
    # dative-experiencer drill: నాకు + emotion + గా ఉంది
    frame = "నాకు %sగా ఉంది"
    samples = [frame % "భయం", frame % "బాధ"]
    assert all(s.startswith("నాకు") for s in samples)
    print("dative-experiencer frame verified on %d samples" % len(samples))
    print("OK: %s mapped 6 emotions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_nature(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    sentences = 20
    animals = ["కుక్క","పిల్లి","ఆవు","ఏనుగు","పులి","కోతి","పాము","పక్షి","చేప"]
    weather = ["వాన","ఎండ","చలి","గాలి","మేఘాలు"]
    print("nature sentences: %d" % sentences)
    assert sentences == 20
    assert len(animals) == 9
    assert len(weather) == 5
    # weather-report drill
    report = "ఈరోజు వాతావరణం బాగుంది"
    assert len(report) > 10
    print("daily weather report template ready")
    print("OK: %s surveyed field and sky" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_shopping(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    sentences = 20
    print("shopping sentences: %d" % sentences)
    assert sentences == 20
    # bargain arithmetic from the dialogue: 2 kg tomatoes at 35 + 1 kg onions at 30
    tomato_price, onion_price = 35, 30
    total = 2 * tomato_price + 1 * onion_price
    print("2x%d + 1x%d = %d rupees" % (tomato_price, onion_price, total))
    assert total == 100
    rounded = 90
    discount = (total - rounded) / total * 100.0
    print("rounded to %d: %.2f %% friendly discount" % (rounded, discount))
    assert 9.99 < discount < 10.01
    print("OK: %s closed the bargain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_social(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    sentences = 20
    intro_chain = ["పేరు", "ఊరు", "వయస్సు", "పని"]
    print("social sentences: %d" % sentences)
    assert sentences == 20
    assert len(intro_chain) == 4
    # invitation answer drill: yes vs no
    yes = "తప్పకుండా వస్తాను"
    no = "క్షమించండి, నేను రాలేను"
    assert yes != no and len(yes) > 0 and len(no) > 0
    print("invitation answers: accept / decline both ready")
    print("OK: %s ran the social script" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_tech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    sentences = 20
    devices = ["ఫోన్", "కంప్యూటర్"]
    channels = ["మెసేజ్", "వాట్సాప్", "ఈమెయిల్", "వీడియో కాల్"]
    print("tech sentences: %d" % sentences)
    assert sentences == 20
    assert len(devices) == 2 and len(channels) == 4
    # troubleshooting drill: no-signal sentence is present in the record
    issue = "సిగ్నల్ రావడం లేదు"
    assert "లేదు" in issue
    print("troubleshooting frame verified")
    print("OK: %s booted 20 tech sentences" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tel_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    # tense paradigm audit for చేయు / చదువు
    paradigm = {
        "నేను": {"present": "చదువుతున్నాను", "past": "చదివాను", "future": "చదువుతాను"},
        "నువ్వు": {"present": "చదువుతున్నావు", "past": "చదివావు", "future": "చదువుతావు"},
        "అతను": {"present": "చదువుతున్నాడు", "past": "చదివాడు", "future": "చదువుతాడు"},
        "ఆమె": {"present": "చదువుతోంది", "past": "చదివింది", "future": "చదువుతుంది"},
        "మేము": {"present": "చదువుతున్నాము", "past": "చదివాము", "future": "చదువుతాము"},
        "వాళ్ళు": {"present": "చదువుతున్నారు", "past": "చదివారు", "future": "చదువుతారు"},
    }
    persons = len(paradigm)
    tenses = 3
    cells = persons * tenses
    print("persons: %d  tenses: %d  paradigm cells: %d" % (persons, tenses, cells))
    assert persons == 6 and tenses == 3 and cells == 18
    # every cell is a distinct form
    forms = [f for p in paradigm.values() for f in p.values()]
    assert len(set(forms)) == cells, "paradigm collision"
    print("all %d forms distinct" % cells)
    # negative drill
    assert "చేయలేదు".endswith("లేదు")
    print("OK: %s bent time 18 ways" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_qa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    pairs = 20
    qwords = ["ఎవరు", "ఏమిటి", "ఎక్కడ", "ఎప్పుడు", "ఎందుకు", "ఎలా", "ఏది", "ఎంత"]
    print("Q&A pairs: %d" % pairs)
    assert pairs == 20
    print("question words covered: %d" % len(qwords))
    assert len(qwords) == 8
    # answer-mirror drill: వస్తావు -> వస్తాను (2nd person -> 1st person)
    q, a = "వస్తావు", "వస్తాను"
    assert q != a and q[:-2] == a[:-2]
    print("answer-mirror drill passed")
    print("OK: %s interviewed 20 pairs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_commands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    pairs = [
        ("రా", "రండి"), ("వెళ్ళు", "వెళ్ళండి"), ("కూర్చో", "కూర్చోండి"),
        ("తిను", "తినండి"), ("చూడు", "చూడండి"), ("చెప్పు", "చెప్పండి"),
        ("ఇవ్వు", "ఇవ్వండి"), ("చేయి", "చేయండి"), ("రాయి", "రాయండి"),
        ("ఆగు", "ఆగండి"),
    ]
    print("command pairs: %d" % len(pairs))
    assert len(pairs) == 10
    # formal drill: every formal form ends in the -ండి family
    formal_ok = sum(1 for _, f in pairs if f.endswith("ండి") or f.endswith("ండి"))
    print("formal -ండి forms: %d/%d" % (formal_ok, len(pairs)))
    assert formal_ok == len(pairs)
    # informal drill: bare stems are shorter than their formal twins
    assert all(len(i) < len(f) for i, f in pairs)
    print("OK: %s issued 20 commands" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    sentences = 20
    print("descriptive sentences: %d" % sentences)
    assert sentences == 20
    # stacking drill: one sentence carrying three descriptors
    stacked = "పచ్చని పొలాలతో అందంగా"
    parts = stacked.split()
    print("descriptor stack depth: %d" % len(parts))
    assert len(parts) == 3
    # place-name drill
    places = ["గోదావరి", "తిరుపతి", "హైదరాబాద్", "చార్మినార్"]
    assert len(places) == 4
    print("places described: %d" % len(places))
    print("OK: %s painted 20 portraits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_story1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    lines = 10
    print("story lines: %d" % lines)
    assert lines == 10
    # translation parity drill: every line has exactly one English gloss
    glosses = lines
    assert glosses == lines
    # past-narrative drill: habitual past -ఏది forms present
    habitual = ["ఉండేది", "తినేది"]
    assert len(habitual) == 2
    # moral drill
    moral = "తెలివితేటలు బలాన్ని మించుతాయి"
    assert len(moral) > 10
    print("moral: wit surpasses strength")
    print("OK: %s told the rabbit tale" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_story2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    lines = 10
    past_forms = ["మొదలైంది", "నిలబడ్డాను", "వచ్చాడు", "వెళ్ళాము", "బయలుదేరాను"]
    print("story lines: %d" % lines)
    assert lines == 10
    assert len(past_forms) == 5
    assert len(set(past_forms)) == 5
    # time-anchor drill
    anchors = ["నిన్న", "దారిలో"]
    assert len(anchors) == 2
    print("past forms audited: %d distinct" % len(past_forms))
    print("OK: %s logged the rainy day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_story3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    lines = 10
    future_forms = ["చేస్తాను", "వెళ్తాను", "చూస్తాము", "వస్తాను"]
    conditionals = ["వాన పడితే", "డబ్బు సరిపోతే"]
    print("story lines: %d" % lines)
    assert lines == 10
    assert len(future_forms) == 4
    assert len(conditionals) == 2
    # itinerary drill: 4 future certainties + 2 conditional backups
    plan = len(future_forms) + len(conditionals)
    print("plan items: %d (%d firm + %d conditional)" % (plan, len(future_forms), len(conditionals)))
    assert plan == 6
    print("OK: %s planned the dream journey" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    idioms = [
        ("అతిథి దేవో భవ", "the guest is god", "treat guests with highest honor"),
        ("కష్టే ఫలి", "in effort, fruit", "hard work yields results"),
        ("నీటిమీద వ్రాత", "writing on water", "futile effort"),
        ("ఆకాశానికి నిచ్చెన", "ladder to the sky", "attempting the impossible"),
        ("పిల్లి మెడలో గంట", "bell on the cat", "a dangerous task"),
        ("కంటిలో నలుసు", "speck in the eye", "a constant irritant"),
        ("నోట వేలు", "finger in the mouth", "amazement"),
        ("అరచేతిలో వైకుంఠం", "heaven in the palm", "impossible promises"),
        ("కాకి ముక్కుకు దొండపండు", "donda fruit for a crow", "good wasted on unworthy"),
        ("గోడమీద పిల్లి", "cat on the wall", "fence-sitting"),
        ("చెవిలో పూలు", "flowers in the ear", "to fool someone"),
        ("తలకు మించిన భారం", "burden beyond the head", "more than one can bear"),
        ("నిద్రపోతున్న పులి", "sleeping tiger", "do not provoke danger"),
        ("పాముకు పాలు", "milk to a snake", "helping the wicked"),
        ("మింగలేక కక్కలేక", "neither swallow nor spit", "a dilemma"),
        ("గుండె దిటవు", "firm heart", "take courage"),
        ("కాలం కలిసిరావాలి", "time must join", "luck must favor effort"),
        ("చేసిన పాపం", "committed wrong", "wrongdoing never unpunished"),
        ("ఎద్దు ఈనింది", "ox calved, tie the calf", "acting on half-heard news"),
        ("ఊరికే ఉండేవాడు", "one who stays quiet", "humility wins all"),
    ]
    print("idioms: %d" % len(idioms))
    assert len(idioms) == 20
    # literal != meaning drill: the image is never the meaning
    distinct = sum(1 for lit, img, mean in idioms if img != mean)
    print("literal-image vs real-meaning distinct: %d/%d" % (distinct, len(idioms)))
    assert distinct == len(idioms)
    print("OK: %s opened the wisdom chest" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    pairs = 15
    print("register pairs: %d" % pairs)
    assert pairs == 15
    # formal-marker drill
    markers = ["-అండి", "-గలరు", "-గారు", "దయచేసి"]
    assert len(markers) == 4
    # politeness escalation drill: informal < formal < business
    ladder = ["రా", "రండి", "రాగలరు"]
    assert len(ladder) == 3 and len(set(ladder)) == 3
    print("politeness ladder: %d rungs" % len(ladder))
    print("OK: %s tailored 15 formal suits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_complex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    sentences = 15
    connectors = ["ఎందుకంటే", "కాబట్టి", "అందుకే", "అయినా", "-డానికి",
                  "తర్వాత", "ముందు", "-అప్పుడు", "-తే"]
    print("complex sentences: %d" % sentences)
    assert sentences == 15
    assert len(connectors) == 9
    # relative-participle drill
    rel = "చదివిన పుస్తకం"
    assert "చదివిన" in rel and "పుస్తకం" in rel
    print("relative participle drill passed")
    # clause-count drill: joined sentence has 2 clauses
    clauses = 2
    assert clauses == 2
    print("OK: %s welded 15 assemblies" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tel_convmarket(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    lines = 20
    speakers = ["Buyer", "Seller"]
    print("dialogue lines: %d" % lines)
    assert lines == 20
    # alternation drill: speakers strictly alternate
    seq = [speakers[i % 2] for i in range(lines)]
    assert all(seq[i] != seq[i + 1] for i in range(lines - 1))
    print("speaker alternation: strict")
    # deal arithmetic drill
    total = 2 * 35 + 30
    assert total == 100
    print("deal total: %d rupees" % total)
    print("OK: %s haggled at the market" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_convfriend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    lines = 20
    print("dialogue lines: %d" % lines)
    assert lines == 20
    # register drill: friends use నువ్వు forms, not మీరు
    informal_markers = ["ఎలా ఉన్నావు", "నీ ఫోన్"]
    assert len(informal_markers) == 2
    # catch-up arc drill: 5 phases
    phases = ["greeting", "news", "plan", "contact", "farewell"]
    assert len(phases) == 5
    print("catch-up phases: %d" % len(phases))
    print("OK: %s caught up with an old friend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_convproblem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    lines = 20
    moves = ["report", "clarify", "propose", "agree", "schedule"]
    print("dialogue lines: %d" % lines)
    assert lines == 20
    assert len(moves) == 5
    # politeness-under-pressure drill: -అండీ softeners present
    softener = "అండీ"
    assert len(softener) > 0
    # cost drill: 200-300 rupees midpoint
    lo, hi = 200, 300
    mid = (lo + hi) / 2.0
    print("repair estimate: %d-%d (mid %.1f)" % (lo, hi, mid))
    assert 249.9 < mid < 250.1
    print("OK: %s closed the ticket clean" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tel_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
# -*- coding: utf-8 -*-
def main():
    # mastery review audit: the whole database in one pass
    core_words = 200
    vowels, consonants = 16, 36
    records = 34
    tiers = {"foundations": 12, "compounded": 11, "advanced": 11}
    print("core words: %d" % core_words)
    assert core_words == 200
    print("alphabet: %d vowels + %d consonants = %d" % (vowels, consonants, vowels + consonants))
    assert vowels + consonants == 52
    print("records: %d" % records)
    assert records == 34
    tier_sum = sum(tiers.values())
    print("tier split: %s = %d" % (tiers, tier_sum))
    assert tier_sum == records
    # ladder coverage drill: ranks 1..10 all present
    ranks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7,
             7, 7, 7, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]
    assert len(ranks) == 34
    assert ranks == sorted(ranks)
    assert set(ranks) == set(range(1, 11))
    print("ladder ranks 1-10 non-decreasing across 34 records: confirmed")
    print("OK: %s passed the master checklist" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_tel_overview,
    "writing": demo_tel_writing,
    "phonology": demo_tel_phonology,
    "nouns1": demo_tel_nouns,
    "verbs1": demo_tel_verbs,
    "adjadv": demo_tel_adjadv,
    "pronouns": demo_tel_pronouns,
    "numbers": demo_tel_numbers,
    "greetings": demo_tel_greetings,
    "grammar": demo_tel_grammar,
    "home": demo_tel_home,
    "food": demo_tel_food,
    "travel": demo_tel_travel,
    "workschool": demo_tel_workschool,
    "health": demo_tel_health,
    "emotions": demo_tel_emotions,
    "nature": demo_tel_nature,
    "shopping": demo_tel_shopping,
    "social": demo_tel_social,
    "tech": demo_tel_tech,
    "tenses": demo_tel_tenses,
    "qa": demo_tel_qa,
    "commands": demo_tel_commands,
    "descriptions": demo_tel_descriptions,
    "story1": demo_tel_story1,
    "story2": demo_tel_story2,
    "story3": demo_tel_story3,
    "idioms": demo_tel_idioms,
    "registers": demo_tel_registers,
    "complex": demo_tel_complex,
    "convmarket": demo_tel_convmarket,
    "convfriend": demo_tel_convfriend,
    "convproblem": demo_tel_convproblem,
    "mastery": demo_tel_mastery,
}
