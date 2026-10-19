"""Missing-key patch for Fula LANG (24 keys). Run once before ENTRIES build."""
import os

EXTRA = {
    "adj_agree": "full agreement in noun class with the noun: moƴƴo/moƴƴɓe/moƴƴnde",
    "adj_key1": "Adjectives echo the noun's class suffix: gorko moƴƴo, worɓe moƴƴɓe.",
    "adj_place": "after the noun they modify",
    "adv_note": "Adverbs never change form; 'tan' (only) follows the noun.",
    "comparative": "Comparatives use ɓuri (more): ɓuri mawɗo = bigger; ɓuri heewɗo = more.",
    "gram_how": "Fula is a class-first language: the noun's class suffix echoes through adjective, verb, and pronoun, so agreement carries the grammar.",
    "gram_key1": "Class agreement carries the grammar; aspect carries the time.",
    "gram_key2": "Noun classes and consonant mutation are the two big climbs - everything else is downhill.",
    "gram_story": "Eight rules run Fula: SVO order, 24-26 noun classes, initial mutation, agreeing adjectives, aspect-marked verbs, three voices, -aa negation, and the en/min distinction.",
    "greet_body": "Take your time - the greeting ritual is the relationship, never rush it.",
    "greet_coverage": "hello, goodbye, thanks, welcome, and how-are-you",
    "greet_match": "the time of day (waali/ñalli/hiiri) and the peace ritual",
    "negation": "-aa suffix on the verb (mi waawataa = I cannot)",
    "num_agree": "numbers follow the noun and take class agreement in some dialects",
    "num_big": "100 = teemerre, 1000 = ujunerre, million = dubuure.",
    "num_build": "6-9 = jowi + unit; 11-19 = sappo e unit; tens = cappanɗe + unit.",
    "polite_note": "Use 'on' with elders, strangers, and in service situations.",
    "possessive_note": "an (my), maa (your), makko (his/her), men (our incl.), amen (our excl.), mon (your pl.), maɓɓe (their) follow the noun.",
    "pron_choose": "inclusion (en vs min) and respect (a vs on)",
    "question_short": "question words hol/ko honɗun/honto/ndeye, or rising intonation",
    "theme_how": "Fula sentences run subject-verb-object with class agreement doing the grammatical work",
    "theme_pattern_note": "subject + verb + object, with 'ko' focusing the subject",
    "theme_sentence_note": "simple, natural, and built only from records 1-10 plus the theme's own words",
    "theme_stories": {
        "home": "family life and the household",
        "food": "meals, cooking, and eating out",
        "travel": "getting around and the road",
        "work": "jobs, school, and study",
        "health": "the body and feeling well",
        "emotions": "feelings and states of mind",
        "nature": "weather and the natural world",
        "shopping": "buying, prices, and the market",
        "friends": "friendship and social moments",
        "tech": "phones, computers, and the internet",
    },
}


def apply(lang):
    lang.update(EXTRA)
