# -*- coding: utf-8 -*-
"""Topic module: db-vocabulary-power-up. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-vocabulary-power-up", "name": "The Vocabulary Power-Up Database", "pfx": "JAH-VOCPOWUP-",
    "tagline_pub": "Vocabulary power-ups with every word mastered - definitions, synonyms, and usage: every record carrying the word, its meaning, and a check that the usage fits, taught progressively along the ladder.",
    "tagline_sig": "The Signature word-power: every word a Signature upgrade, every usage a Signature flex. The full ladder from everyday words through sharp ones to Signature-grade vocabulary. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Vocabulary Power-Up",
    "role_pub": "word coach - powering up vocabularies one word at a time",
    "role_sig": "Signature word coach - teaching Signature word-power",
    "record_kind": "vocabulary record", "record_kind_plural": "vocabulary power-ups",
    "demo_kind": "word-proof", "demo_title": "Vocabulary Study",
    "search_ph": "Search words, definitions, synonyms, vocabulary...",
    "chat_ph": "Ask for a vocabulary power-up...",
    "gen_blurb": "Generate clearly-labeled word studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded vocabulary power-ups, every usage verified, marching toward one million records. Presented in teaching-ladder order: everyday, sharp, Signature-grade.",
    "reqs": "Curiosity and a notebook for new words.",
    "stds": "Every word carries definition, synonym, and an example sentence; the demo verifies the word fits its sentence.",
    "cites": ["JAH Databases vocabulary standard v1.0"],
})


def _vu(tier, word, pos, definition, synonym, sentence):
    return T(
        tier, "Word: %s" % word,
        desc_pub='POWER WORD: %s (%s)\n\nDEFINITION: %s\n\nSYNONYM: %s\n\nIN A SENTENCE: %s'
        % (word.upper(), pos, definition, synonym, sentence),
        desc_sig='Signature word-power: %s - one more Signature word in the arsenal. The Signature edition treats every mastered word as the voice getting stronger.' % word.upper(),
        how_pub='Master it: read the definition, say the sentence aloud, then write your own sentence - using it is owning it.',
        how_sig='The Signature way: use it three times today - the word becomes yours by the third.',
        keys=['Word: %s (%s).' % (word, pos),
              'Definition: %s' % definition,
              'Synonym: %s.' % synonym,
              'Sentence: %s' % sentence],
        demo=("check", {"code": ["W = %r" % word, "S = %r" % sentence],
                        "checks": [("word_in_sentence", "W.lower() in S.lower()"),
                                   ("sentence_full", "S.endswith('.') and len(S) > 20"),
                                   ("single_word", "len(W.split()) == 1")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _vu(B, "happy", "adjective", "Feeling joy or pleasure.", "glad", "The happy child laughed at the clown."),
    _vu(B, "brave", "adjective", "Not afraid; courageous.", "bold", "The brave firefighter entered the smoke."),
    _vu(B, "quick", "adjective", "Fast; moving rapidly.", "swift", "The quick rabbit darted into the bushes."),
    _vu(B, "bright", "adjective", "Giving out much light; smart.", "shiny", "The bright sun woke the campers."),
    _vu(B, "kind", "adjective", "Friendly and generous.", "nice", "The kind neighbor shared her cookies."),
    _vu(B, "strong", "adjective", "Having great power.", "mighty", "The strong ox pulled the heavy cart."),
    _vu(B, "gentle", "adjective", "Soft and mild; not rough.", "tender", "The gentle nurse spoke softly."),
    _vu(B, "curious", "adjective", "Wanting to learn; inquisitive.", "inquisitive", "The curious kitten explored every box."),
    _vu(B, "ancient", "adjective", "Very old; from long ago.", "old", "The ancient pyramid stood in the desert."),
    _vu(B, "victory", "noun", "Winning; success in a contest.", "triumph", "The team celebrated their victory loudly."),
    _vu(B, "journey", "noun", "Traveling from one place to another.", "trip", "The journey across the desert took weeks."),
    _vu(C, "meticulous", "adjective", "Showing great attention to detail.", "thorough", "The meticulous editor caught every typo."),
    _vu(C, "resilient", "adjective", "Recovering quickly from hardship.", "tough", "The resilient town rebuilt after the storm."),
    _vu(C, "eloquent", "adjective", "Fluent and persuasive in speaking.", "articulate", "The eloquent speaker moved the crowd."),
    _vu(C, "pragmatic", "adjective", "Practical rather than idealistic.", "practical", "The pragmatic plan saved time and money."),
    _vu(C, "vivid", "adjective", "Bright, clear, and detailed.", "lively", "The vivid painting seemed almost real."),
    _vu(C, "serene", "adjective", "Calm and peaceful.", "tranquil", "The serene lake mirrored the mountains."),
    _vu(C, "diligent", "adjective", "Hardworking and careful.", "industrious", "The diligent student finished early."),
    _vu(C, "candid", "adjective", "Honest and straightforward.", "frank", "The candid review helped the author."),
    _vu(C, "innovative", "adjective", "Introducing new ideas; creative.", "inventive", "The innovative design won the prize."),
    _vu(C, "compassionate", "adjective", "Feeling sympathy for others.", "caring", "The compassionate doctor comforted the family."),
    _vu(C, "tenacious", "adjective", "Holding firmly; persistent.", "persistent", "The tenacious climber reached the summit."),
    _vu(C, "luminous", "adjective", "Glowing with light.", "glowing", "The luminous moon lit the path."),
    _vu(A, "perspicacious", "adjective", "Having keen insight; discerning.", "astute", "The perspicacious judge saw through the lies."),
    _vu(A, "sagacious", "adjective", "Wise through experience.", "wise", "The sagacious elder settled the dispute."),
    _vu(A, "ineffable", "adjective", "Too great for words.", "indescribable", "The ineffable beauty left them silent."),
    _vu(A, "petrichor", "noun", "The scent of rain on dry earth.", "rain-smell", "The petrichor after the storm was wonderful."),
    _vu(A, "sonder", "noun", "The realization that strangers have full lives.", "empathy", "A wave of sonder hit him in the crowd."),
    _vu(A, "limerence", "noun", "Involuntary infatuation.", "infatuation", "Her limerence faded into friendship."),
    _vu(A, "crepuscular", "adjective", "Active at twilight.", "twilight", "The crepuscular deer emerged at dusk."),
    _vu(A, "defenestration", "noun", "Throwing something out a window.", "window-tossing", "The defenestration of the papers shocked all."),
    _vu(A, "sesquipedalian", "adjective", "Given to long words.", "long-winded", "His sesquipedalian speech confused everyone."),
    _vu(A, "apricity", "noun", "Warmth of sun in winter.", "winter-warmth", "They basked in the apricity of noon."),
    _vu(A, "vellichor", "noun", "The scent of old books.", "book-smell", "The vellichor of the library calmed her."),
]
