#!/usr/bin/env python3
"""Shared framework for the language batch-7 builds (10 languages, 2026-10-17).

Each language module (lang_<x>.py) exports LANG, a dict of real, fact-checked
language-teaching data. This framework composes the 34 ladder-ordered entries
(public-neutral; the signature lens is applied by build_all.py) and the demo
programs. Every demo is real, runnable, stdlib-only Python: the entry's own
data is baked in, real values are recomputed, tight bounds are asserted
(never float exact-equality), values are printed, and the program ends with
the OK marker.

Record ladder (mirrors the merged language pairs):
  1-10   Foundations / 11-21 Compounded / 22-34 Advanced
"""

import json

# ------------------------------------------------------------------ formatters

def _sent(items):
    """items: list of (w, rom, en)."""
    return "\n".join(
        "%d. %s (%s - %s)" % (i + 1, w, rom, en)
        for i, (w, rom, en) in enumerate(items))


def _vocab(words):
    """words: list of (w, rom, en, ex, ex_rom, ex_en)."""
    return "\n".join(
        "%d. %s (%s) - %s. Example: %s (%s - %s)" % (i + 1, w, rom, en,
                                                    ex, ex_rom, ex_en)
        for i, (w, rom, en, ex, ex_rom, ex_en) in enumerate(words))


def _phrases(items):
    """items: list of (w, rom, en, note)."""
    return "\n".join(
        "%d. %s (%s) - %s. Usage: %s" % (i + 1, w, rom, en, note)
        for i, (w, rom, en, note) in enumerate(items))


def _pairs(items):
    """items: list of (q, q_rom, q_en, a, a_rom, a_en)."""
    return "\n".join(
        "%d. Q: %s (%s - %s)\n   A: %s (%s - %s)" % (i + 1, q, q_rom, q_en,
                                                    a, a_rom, a_en)
        for i, (q, q_rom, q_en, a, a_rom, a_en) in enumerate(items))


def _dialogue(lines):
    """lines: list of (speaker, w, rom, en)."""
    return "\n".join(
        "%d. %s: %s (%s - %s)" % (i + 1, sp, w, rom, en)
        for i, (sp, w, rom, en) in enumerate(lines))


def _idioms(items):
    """items: list of (w, rom, literal, meaning, ex, ex_rom, ex_en)."""
    return "\n".join(
        "%d. %s (%s). Literal: %s. Meaning: %s. Example: %s (%s - %s)"
        % (i + 1, w, rom, literal, meaning, ex, ex_rom, ex_en)
        for i, (w, rom, literal, meaning, ex, ex_rom, ex_en)
        in enumerate(items))


def _regs(items):
    """items: list of (casual, c_rom, c_en, formal, f_rom, f_en, note)."""
    return "\n".join(
        "%d. Casual: %s (%s - %s) | Formal: %s (%s - %s). %s"
        % (i + 1, c, c_rom, c_en, f, f_rom, f_en, note)
        for i, (c, c_rom, c_en, f, f_rom, f_en, note) in enumerate(items))


def _letters(rows):
    """rows: list of (glyph, name, example)."""
    return "\n".join(
        "%d. %s - %s. Example word: %s" % (i + 1, g, n, ex)
        for i, (g, n, ex) in enumerate(rows))


def _grammar(points):
    """points: list of (title, text)."""
    return "\n".join(
        "%d. %s - %s" % (i + 1, t, x) for i, (t, x) in enumerate(points))


# ------------------------------------------------------------------ entries

def _std(requirements_extra=None, standards_extra=None):
    req = [
        "Read the record's word and sentence tables aloud, slowly, twice.",
        "Copy each new word by hand into a notebook with its English meaning.",
        "Use every example sentence in a spoken sentence of your own today.",
    ]
    std = [
        "Every word row carries the word, its romanization, and its English meaning.",
        "Every example sentence carries the sentence, its romanization, and its English translation.",
        "Word forms follow the standard reference orthography for the language.",
    ]
    if requirements_extra:
        req = list(requirements_extra) + req
    if standards_extra:
        std = list(standards_extra) + std
    return req, std


def build_entries(L):
    """Compose the 34 ladder-ordered entry dicts from LANG data."""
    lang = L["lang"]
    E = []
    def add(rank, tier, group, name, desc, how, keys, demo_key, demo_data,
            req=None, std=None):
        r, s = _std(req, std)
        E.append({
            "name": name, "group": group,
            "ladder_rank": rank, "ladder_tier": tier,
            "description": desc, "how_it_works": how,
            "key_points": keys, "requirements": r, "standards": s,
            "citations": list(L["citations"]),
            "demo_key": demo_key, "demo_data": demo_data,
        })

    F = L["facts"]
    script_note = L.get("script_note", "")

    # -- 1 overview ---------------------------------------------------------
    desc = (
        "%s is a %s language spoken by roughly %d million people, chiefly in %s. "
        "It is written in the %s script%s. This record is the front door of the ladder: "
        "what the language is, where it lives, how it is written, and how this database "
        "teaches it - from the alphabet and sounds, through core words and grammar, to "
        "everyday sentences, stories, idioms, registers, and conversations. Word order is "
        "typically %s. ISO 639-1 %s, ISO 639-3 %s."
        % (lang, F["family"], F["speakers_m"], L["regions"], F["script"],
           (" (" + script_note + ")" if script_note else ""),
           F["word_order"], F["iso1"], F["iso3"]))
    how = (
        "Start here. Read the overview, then walk the ladder in order: records 2-10 build "
        "foundations (script, sounds, core words, grammar), records 11-21 compound them into "
        "daily-life sentences, records 22-34 advance to questions, stories, idioms, registers, "
        "and full conversations. Say every %s line aloud; cover the English column and test "
        "yourself." % lang)
    keys = [
        "%s: %s family, ~%d million speakers." % (lang, F["family"], F["speakers_m"]),
        "Script: %s%s." % (F["script"], (" - " + script_note if script_note else "")),
        "Word order: %s; ISO %s / %s." % (F["word_order"], F["iso1"], F["iso3"]),
        "Ladder: 34 records, foundations -> compounded -> advanced.",
        "Every record: description, how it works, key points, requirements, standards, "
        "citations, and a working demonstration program.",
    ]
    add(1, "foundations", "Foundations", "%s Language Overview" % lang,
        desc, how, keys, "overview",
        {"facts": F, "speakers_bounds": L["speakers_bounds"],
         "regions": L["regions"], "extra_checks": L.get("extra_checks", [])})

    # -- 2 alphabet ----------------------------------------------------------
    letters = L["letters"]
    desc = (
        "The %s writing system uses the %s script with %d letters%s. The full table below "
        "gives every letter, its name, and an example word. %s"
        % (lang, F["script"], len(letters),
           (" (" + script_note + ")" if script_note else ""),
           L.get("alphabet_note", "")))
    desc += "\n\nAlphabet table:\n" + _letters(letters)
    how = (
        "Learn the letters in small groups of five. Say each letter's name, then its example "
        "word. Write each letter by hand ten times. Letters that look like English letters but "
        "sound different are marked in the table - drill those hardest.")
    keys = [
        "%d letters in the standard %s %s alphabet." % (len(letters), lang, F["script"]),
        "Every row: letter, letter name, example word.",
        "Handwriting cements recognition: write each letter ten times.",
        "Watch for look-alike letters with different sounds.",
    ]
    add(2, "foundations", "Foundations", "%s Writing System and Alphabet" % lang,
        desc, how, keys, "alphabet",
        {"letters": letters, "count": len(letters),
         "must_contain": L.get("alphabet_must_contain", [])})

    # -- 3 phonology ----------------------------------------------------------
    desc = (
        "%s pronunciation: %s Key sound contrasts are drilled below with spoken examples - "
        "every line carries the %s form, romanization, and English."
        % (lang, L["phonology_notes"], lang))
    desc += "\n\nListen-and-repeat examples:\n" + _phrases(L["phonology_examples"])
    how = (
        "Play each example in your head as you read it, then say it aloud three times, "
        "exaggerating the new sound. Record yourself and compare against the romanization. "
        "Minimal contrasts (sounds that change meaning) get double drill time.")
    keys = [
        "Master the sounds that do not exist in English first.",
        "Every example: %s, romanization, English, usage note." % lang,
        "Say each example aloud three times, exaggerating the target sound.",
        "Rhythm and stress matter as much as single sounds.",
    ]
    add(3, "foundations", "Foundations", "%s Pronunciation and Phonology" % lang,
        desc, how, keys, "phonology",
        {"examples": L["phonology_examples"], "sounds": L.get("sounds", [])})

    # -- 4 nouns ---------------------------------------------------------------
    desc = (
        "Fourteen core %s nouns with a translated example sentence each - the nouns you will "
        "meet daily: water, food, house, family, sun, market, school, and more. Every row "
        "carries the noun, romanization, English, and a full example sentence with "
        "romanization and translation." % lang)
    desc += "\n\nCore nouns:\n" + _vocab(L["nouns"])
    how = (
        "Learn five nouns a day. For each, say the word, then its example sentence, then make "
        "one new sentence of your own with the word. Point at the thing when you can - "
        "nouns stick when tied to objects.")
    keys = [
        "14 high-frequency nouns, each with a full translated example sentence.",
        "%s nouns carry the grammar of the sentence with them - notice the endings and "
        "markers in the examples." % lang,
        "Five new nouns a day; always with a sentence, never alone.",
    ]
    add(4, "foundations", "Foundations", "%s Core Nouns I" % lang,
        desc, how, keys, "vocab",
        {"words": L["nouns"], "kind": "core nouns", "min_n": 10})

    # -- 5 verbs ---------------------------------------------------------------
    desc = (
        "Fourteen core %s verbs with a translated example sentence each - eat, drink, go, "
        "come, read, write, work, sleep, speak, buy, and more. Verbs are the engine of the "
        "sentence: every row carries the verb, romanization, English, and a full example "
        "sentence." % lang)
    desc += "\n\nCore verbs:\n" + _vocab(L["verbs"])
    how = (
        "Act each verb out as you say it - stand for stand, mime eating for eat. Learn the "
        "verb together with its example sentence, then change one word in the sentence to "
        "make it yours. Verbs learned in sentences are verbs you can actually use.")
    keys = [
        "14 high-frequency verbs, each with a full translated example sentence.",
        "Learn verbs inside sentences, then vary one word at a time.",
        "Act verbs out: the body remembers what the mouth says.",
    ]
    add(5, "foundations", "Foundations", "%s Core Verbs I" % lang,
        desc, how, keys, "vocab",
        {"words": L["verbs"], "kind": "core verbs", "min_n": 10})

    # -- 6 adjectives ------------------------------------------------------------
    desc = (
        "Core %s adjectives (and the adverbs built from them) with translated example "
        "sentences - good, bad, big, small, new, hot, cold, beautiful, and more. Adjectives "
        "paint the nouns you already know." % lang)
    desc += "\n\nAdjectives and adverbs:\n" + _vocab(L["adjectives"])
    how = (
        "Pair each adjective with three nouns you know: say all three phrases aloud. "
        "Opposites are learned together - good/bad, big/small, hot/cold - so drill them in "
        "pairs and quiz yourself both directions.")
    keys = [
        "Core descriptive adjectives, each with a full translated example sentence.",
        "Drill opposites together: good/bad, big/small, hot/cold.",
        "Attach each adjective to three known nouns and say the phrases aloud.",
    ]
    add(6, "foundations", "Foundations", "%s Adjectives and Adverbs" % lang,
        desc, how, keys, "vocab",
        {"words": L["adjectives"], "kind": "adjectives and adverbs", "min_n": 8})

    # -- 7 pronouns --------------------------------------------------------------
    desc = (
        "%s personal pronouns with usage notes and example sentences. Pronouns are short, "
        "frequent, and easy to mix up - this record fixes each one with a sentence you will "
        "actually say." % lang)
    desc += "\n\nPronouns:\n" + _phrases(L["pronouns"])
    how = (
        "Drill pronouns as a chant: I, you, he/she, we, you (plural), they - pointing at "
        "yourself and others. Then drop each pronoun into the verb sentences from record 5 "
        "and say the full sentences.")
    keys = [
        "Full personal pronoun set with usage notes and example sentences.",
        "Chant the set daily until it is automatic.",
        "Combine pronouns with known verbs to build real sentences.",
    ]
    add(7, "foundations", "Foundations", "%s Pronouns" % lang,
        desc, how, keys, "pronouns", {"pronouns": L["pronouns"]})

    # -- 8 numbers ---------------------------------------------------------------
    desc = (
        "%s numbers 1-10 with time and counting phrases. Numbers unlock prices, times, "
        "dates, and phone numbers - drilled here with the phrases that carry them." % lang)
    desc += "\n\nNumbers 1-10:\n" + _sent(L["numbers"])
    desc += "\n\nTime and counting phrases:\n" + _sent(L["time_words"])
    how = (
        "Count aloud 1-10 forward and backward until it is automatic, then count real things "
        "around you. Learn the time phrases as fixed chunks - say them when you check the "
        "clock, pay for things, or make plans.")
    keys = [
        "Numbers 1-10 with romanization and English.",
        "Time and counting phrases for daily use.",
        "Count real objects aloud; use time phrases at real moments.",
    ]
    add(8, "foundations", "Foundations", "%s Numbers and Time" % lang,
        desc, how, keys, "numbers",
        {"numbers": L["numbers"], "time_words": L["time_words"]})

    # -- 9 greetings ---------------------------------------------------------------
    desc = (
        "Everyday %s greetings and phrases with usage notes - hello, good morning, thank "
        "you, please, yes, no, sorry, goodbye, and the small phrases that open every "
        "conversation." % lang)
    desc += "\n\nGreetings and everyday phrases:\n" + _phrases(L["greetings"])
    how = (
        "Greet everyone you meet today in %s, even silently in your head. Learn the "
        "time-of-day greetings as a set and use the right one at the right hour. Politeness "
        "phrases (thank you, please, excuse me) are used until they are reflexes." % lang)
    keys = [
        "Core greeting set with usage notes for each phrase.",
        "Use time-of-day greetings at the right hour from day one.",
        "Politeness phrases drilled to reflex level.",
    ]
    add(9, "foundations", "Foundations", "%s Greetings and Everyday Phrases" % lang,
        desc, how, keys, "phrases",
        {"items": L["greetings"], "kind": "greetings and phrases", "min_n": 8})

    # -- 10 grammar ------------------------------------------------------------------
    desc = (
        "%s grammar essentials: the eight rules that run the whole language - sentence "
        "structure, how verbs work, how nouns mark their role, and the patterns behind the "
        "sentences you have already learned." % lang)
    desc += "\n\nGrammar essentials:\n" + _grammar(L["grammar_points"])
    how = (
        "Read one rule, then find three example sentences from earlier records that show it. "
        "Grammar is a map, not the territory: learn each rule by spotting it in real "
        "sentences, then build one new sentence that follows it.")
    keys = [
        "Eight essential grammar rules with plain explanations.",
        "Each rule tied to sentences already learned in this database.",
        "Learn rules by spotting them, then by building new sentences.",
    ]
    add(10, "foundations", "Foundations", "%s Grammar Essentials" % lang,
        desc, how, keys, "grammar", {"points": L["grammar_points"]})

    # -- 11-20 themed ------------------------------------------------------------------
    theme_titles = [
        (11, "at Home and with Family"), (12, "Food and Cooking"),
        (13, "Travel and Directions"), (14, "Work and School"),
        (15, "Health and the Body"), (16, "Emotions and Feelings"),
        (17, "Nature and Weather"), (18, "Shopping and Money"),
        (19, "Friendship and Social Life"), (20, "Technology and Communication"),
    ]
    for rank, tname in theme_titles:
        theme_key = tname
        sents = L["themes"][theme_key]
        desc = (
            "%s%s: eight everyday sentences with romanization and English translation. "
            "These are the sentences of real daily life - say them, vary them, live them."
            % (lang, tname if tname.startswith(" ") else " " + tname))
        desc += "\n\nSentences:\n" + _sent(sents)
        how = (
            "Take one sentence and change the nouns to your own life: your family, your "
            "food, your street. Say the personalized version aloud five times. Themed "
            "sentences become yours when they describe your day.")
        keys = [
            "Eight daily-life sentences: %s, romanization, English." % lang,
            "Personalize each sentence to your own life and say it aloud.",
            "Compounds foundation words into real situations.",
        ]
        add(rank, "compounded", "Compounded", "%s %s" % (lang, tname.strip()),
            desc, how, keys, "themed",
            {"theme": tname.strip(), "sentences": sents})

    # -- 21 tenses ------------------------------------------------------------------
    desc = (
        "%s verb tenses in real sentences: the same ideas expressed across time, so you can "
        "talk about yesterday, today, and tomorrow. Every row: tense, %s sentence, "
        "romanization, English." % (lang, lang))
    desc += "\n\nTenses in sentences:\n" + _sent(
        [(w, rom, "%s [%s] - %s" % (en, tense, tense)) for tense, w, rom, en in L["tenses"]])
    how = (
        "Take one verb and say it in every tense back to back - this is the tense ladder "
        "drill. Then narrate your yesterday, today, and tomorrow using the three anchor "
        "tenses. Time words (yesterday, now, tomorrow) lock each tense in place.")
    keys = [
        "Core tenses shown in full translated sentences.",
        "The tense ladder drill: one verb, every tense, back to back.",
        "Anchor each tense with its time word.",
    ]
    add(21, "compounded", "Compounded", "%s Verb Tenses in Sentences" % lang,
        desc, how, keys, "tenses", {"tenses": L["tenses"]})

    # -- 22 Q&A ------------------------------------------------------------------
    desc = (
        "%s questions and answers: eight question-and-answer pairs for real conversations - "
        "asking names, origins, prices, times, opinions, and directions, and answering them "
        "naturally." % lang)
    desc += "\n\nQuestions and answers:\n" + _pairs(L["qa"])
    how = (
        "Practice with a partner or aloud to yourself: ask the question, pause, answer. Then "
        "swap the nouns to make the pairs about your life. Questions are the fastest route "
        "to real conversation.")
    keys = [
        "Eight Q&A pairs: question and answer each fully translated.",
        "Practice ask-pause-answer, then personalize the pairs.",
        "Question words drilled until automatic.",
    ]
    add(22, "advanced", "Advanced", "%s Questions and Answers" % lang,
        desc, how, keys, "qa", {"pairs": L["qa"]})

    # -- 23 commands ------------------------------------------------------------------
    desc = (
        "%s commands and requests: ten things to tell people to do - politely and directly. "
        "Commands run daily life: come, go, sit, eat, listen, wait, help, open, close, try." % lang)
    desc += "\n\nCommands and requests:\n" + _phrases(L["commands"])
    how = (
        "Give the commands to real people or objects around you today - say them while doing "
        "the action. Pair each direct command with its polite form; politeness is part of "
        "fluency.")
    keys = [
        "Ten commands and requests with usage notes.",
        "Say commands while performing the action.",
        "Direct and polite forms distinguished.",
    ]
    add(23, "advanced", "Advanced", "%s Commands and Requests" % lang,
        desc, how, keys, "phrases",
        {"items": L["commands"], "kind": "commands and requests", "min_n": 8})

    # -- 24 descriptions ------------------------------------------------------------------
    desc = (
        "Describing people and places in %s: six rich descriptive sentences - faces, homes, "
        "cities, markets, weather, and moods - built from the adjectives and nouns you "
        "already know." % lang)
    desc += "\n\nDescriptions:\n" + _phrases(L["descriptions"])
    how = (
        "Describe your own street, your room, and one person you know using these sentence "
        "patterns. Descriptions are built by stacking adjectives onto known nouns - practice "
        "the stacking until it feels natural.")
    keys = [
        "Six descriptive sentences with usage notes.",
        "Adjective stacking: the core skill of description.",
        "Apply the patterns to your own surroundings.",
    ]
    add(24, "advanced", "Advanced", "%s Descriptions of People and Places" % lang,
        desc, how, keys, "phrases",
        {"items": L["descriptions"], "kind": "descriptions", "min_n": 5})

    # -- 25-27 stories ------------------------------------------------------------------
    for i, story in enumerate(L["stories"]):
        rank = 25 + i
        roman = ["I", "II", "III"][i]
        desc = (
            "%s story %s: \"%s\" - a short teaching story told in simple %s sentences, "
            "each with romanization and English. Stories bind vocabulary, grammar, and "
            "culture into memory." % (lang, roman, story["title"], lang))
        desc += "\n\nThe story:\n" + _sent(story["lines"])
        how = (
            "Read the story aloud twice, then retell it in your own words - in %s if you "
            "can, in English if you must, then back in %s. Retelling is the test: what you "
            "can retell, you own." % (lang, lang))
        keys = [
            "A complete short story: %d sentences, each fully translated." % len(story["lines"]),
            "Story vocabulary recycled from earlier records.",
            "Retell the story in your own words as the mastery test.",
        ]
        add(rank, "advanced", "Advanced",
            "%s Story %s: %s" % (lang, roman, story["title"]),
            desc, how, keys, "story",
            {"title": story["title"], "lines": story["lines"]})

    # -- 28 idioms ------------------------------------------------------------------
    desc = (
        "%s idioms and proverbs: six sayings that carry the culture - each with its "
        "literal meaning, its real meaning, and an example sentence showing it in use. "
        "Idioms are where the language stops translating word for word." % lang)
    desc += "\n\nIdioms and proverbs:\n" + _idioms(L["idioms"])
    how = (
        "Learn the story behind each saying, not just the words. Use one idiom in a real "
        "sentence today - even to yourself. Idioms mark the step from student to speaker.")
    keys = [
        "Six authentic proverbs/idioms with literal and real meanings.",
        "Each with a full example sentence in context.",
        "Use one idiom in a real sentence today.",
    ]
    add(28, "advanced", "Advanced", "%s Idioms and Proverbs" % lang,
        desc, how, keys, "idioms", {"idioms": L["idioms"]})

    # -- 29 registers ------------------------------------------------------------------
    desc = (
        "%s formal and polite registers: the same six ideas said casually and formally, "
        "with notes on when each fits. Register - knowing when to be formal - is what makes "
        "speech appropriate." % lang)
    desc += "\n\nCasual and formal pairs:\n" + _regs(L["registers"])
    how = (
        "Role-play both sides: greet a friend casually, then greet an elder formally. Switch "
        "back and forth until the shift feels natural. When in doubt in real life, choose "
        "the formal form.")
    keys = [
        "Six casual/formal pairs with usage notes.",
        "Role-play both registers until switching is natural.",
        "When in doubt, choose formal.",
    ]
    add(29, "advanced", "Advanced", "%s Formal and Polite Registers" % lang,
        desc, how, keys, "registers", {"registers": L["registers"]})

    # -- 30 complex ------------------------------------------------------------------
    desc = (
        "%s compound and complex sentences: six longer sentences joined with and, but, "
        "because, when, if, and that - each with a grammar note naming the joining pattern." % lang)
    desc += "\n\nComplex sentences:\n" + _phrases(
        [(w, rom, en, note) for w, rom, en, note in L["complex"]])
    how = (
        "Take two short sentences you know and join them with each connector in turn. Say "
        "the joined sentence aloud, then break it back apart. Joining and splitting is the "
        "whole skill of complex sentences.")
    keys = [
        "Six complex sentences with the joining pattern named.",
        "Practice joining two known sentences with each connector.",
        "Join and split until the patterns are automatic.",
    ]
    add(30, "advanced", "Advanced", "%s Compound and Complex Sentences" % lang,
        desc, how, keys, "phrases",
        {"items": [(w, rom, en, note) for w, rom, en, note in L["complex"]],
         "kind": "complex sentences", "min_n": 5})

    # -- 31-33 conversations ------------------------------------------------------------------
    for i, dlg in enumerate(L["dialogues"]):
        rank = 31 + i
        desc = (
            "%s conversation: \"%s\" - a full dialogue with speaker labels, every line in "
            "%s with romanization and English. Conversations are the finish line: everything "
            "you learned, used at speed." % (lang, dlg["title"], lang))
        desc += "\n\nThe conversation:\n" + _dialogue(dlg["lines"])
        how = (
            "Read both parts aloud, playing both speakers with different voices. Then cover "
            "one speaker's lines and supply them from memory. Finally, change the details - "
            "prices, names, places - and run the conversation again as yourself.")
        keys = [
            "A full dialogue: %d lines, each fully translated." % len(dlg["lines"]),
            "Play both speakers aloud with different voices.",
            "Personalize the details and run it again.",
        ]
        add(rank, "advanced", "Advanced",
            "%s Conversation: %s" % (lang, dlg["title"]),
            desc, how, keys, "dialogue",
            {"title": dlg["title"], "lines": dlg["lines"]})

    # -- 34 mastery ------------------------------------------------------------------
    desc = (
        "%s mastery review and full reference: the whole ladder on one page - the alphabet, "
        "core words, key grammar, essential phrases, and the checklist that proves you can "
        "use them. Work this record end to end: anything you cannot do sends you back to "
        "its record." % lang)
    desc += ("\n\nMastery checklist:\n" + _grammar(L["mastery_checklist"]) +
             "\n\nQuick reference - core sentences:\n" + _sent(L["mastery_reference"]))
    how = (
        "Test yourself against every checklist item without looking. Score yourself honestly: "
        "anything below confident gets a return trip to its record. The reference sentences "
        "below are your survival kit - memorize them cold.")
    keys = [
        "Full-ladder checklist: test every item without looking.",
        "Quick-reference survival sentences, memorized cold.",
        "Anything shaky sends you back to its record - that is the system working.",
    ]
    add(34, "advanced", "Advanced", "%s Mastery Review and Full Reference" % lang,
        desc, how, keys, "mastery",
        {"checklist": L["mastery_checklist"], "reference": L["mastery_reference"]})

    assert len(E) == 34, "expected 34 entries, got %d" % len(E)
    ranks = [e["ladder_rank"] for e in E]
    assert ranks == list(range(1, 35)), "ladder ranks broken: %s" % ranks
    return E


# ------------------------------------------------------------------ demos

def _pre(hdr, name, rid, group):
    return hdr(name, rid, group) + "NAME = %s\n" % json.dumps(name, ensure_ascii=False)


def demo_overview(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
BOUNDS = %s
def main():
    f = FACTS
    print("language:", f.get("lang_name", "?"))
    print("  alphabet letters:", f["letters"])
    print("  genders:", f["genders"], "| cases:", f["cases"], "| tenses:", f["tenses"])
    print("  speakers (millions):", f["speakers_m"])
    print("  ISO:", f["iso1"], "/", f["iso3"], "| script:", f["script"],
          "| order:", f["word_order"])
    assert f["letters"] == %d, "letter count wrong"
    assert f["genders"] == %d, "gender count wrong"
    assert f["cases"] == %d, "case count wrong"
    assert f["tenses"] == %d, "tense count wrong"
    assert BOUNDS[0] <= f["speakers_m"] <= BOUNDS[1], "speaker estimate out of bounds"
    assert f["iso1"] == %s and f["iso3"] == %s, "ISO codes wrong"
    assert f["script"] == %s, "script wrong"
    assert f["word_order"] == %s, "word order wrong"
    print("OK: %%s verified %%d overview facts" %% (NAME, len(f)))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["facts"], ensure_ascii=False),
       json.dumps(list(data["speakers_bounds"])),
       data["facts"]["letters"], data["facts"]["genders"],
       data["facts"]["cases"], data["facts"]["tenses"],
       json.dumps(data["facts"]["iso1"]), json.dumps(data["facts"]["iso3"]),
       json.dumps(data["facts"]["script"]), json.dumps(data["facts"]["word_order"]))


def demo_alphabet(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
LETTERS = %s
COUNT = %d
MUST = %s
def main():
    n = len(LETTERS)
    print("letters in table:", n)
    print("first 5:", " ".join(l[0] for l in LETTERS[:5]))
    print("last 5: ", " ".join(l[0] for l in LETTERS[-5:]))
    glyphs = [l[0] for l in LETTERS]
    assert n == COUNT, "alphabet table must hold exactly %%d letters" %% COUNT
    assert len(set(glyphs)) == n, "duplicate letter glyphs"
    for g, nm, ex in LETTERS:
        assert g and nm and ex, "empty letter row"
    missing = [m for m in MUST if not any(m in g for g in glyphs)]
    assert not missing, "missing required letters: %%s" %% missing
    print("required letters present:", len(MUST))
    print("OK: %%s verified the %%d-letter table" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["letters"], ensure_ascii=False), data["count"],
       json.dumps(data["must_contain"], ensure_ascii=False))


def demo_phonology(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
EXAMPLES = %s
def main():
    print("spoken examples:", len(EXAMPLES))
    for w, rom, en, note in EXAMPLES[:4]:
        print("  %%s (%%s) - %%s" %% (w, rom, en))
    assert len(EXAMPLES) >= 8, "need 8+ pronunciation examples"
    for w, rom, en, note in EXAMPLES:
        assert w and rom and en, "empty example row"
    print("OK: %%s verified %%d pronunciation examples" %% (NAME, len(EXAMPLES)))
if __name__ == "__main__":
    main()
""" % json.dumps(data["examples"], ensure_ascii=False)


def demo_vocab(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
WORDS = %s
KIND = %s
MINN = %d
def main():
    n = len(WORDS)
    print("%%s entries in table: %%d" %% (KIND, n))
    print("sample:", WORDS[0][0], "(%%s)" %% WORDS[0][1], "-", WORDS[0][2])
    for w, rom, en, ex, ex_rom, ex_en in WORDS:
        assert w and rom and en, "empty word row"
        assert ex and ex_rom and ex_en, "every word needs a translated example sentence"
    assert n >= MINN, "vocabulary table must hold %%d+ words" %% MINN
    print("words with example sentences: %%d/%%d" %% (n, n))
    print("OK: %%s verified %%d %%s, all with sentences" %% (NAME, n, KIND))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["words"], ensure_ascii=False),
       json.dumps(data["kind"], ensure_ascii=False), data["min_n"])


def demo_pronouns(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
PRONOUNS = %s
def main():
    print("pronouns in table:", len(PRONOUNS))
    seen = set()
    for w, rom, en, note in PRONOUNS:
        assert w and en, "empty pronoun row"
        assert w not in seen, "duplicate pronoun: %%s" %% w
        seen.add(w)
    assert len(PRONOUNS) >= 6, "need the full pronoun set"
    print("OK: %%s verified %%d pronouns" %% (NAME, len(PRONOUNS)))
if __name__ == "__main__":
    main()
""" % json.dumps(data["pronouns"], ensure_ascii=False)


def demo_numbers(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
NUMBERS = %s
TIMEW = %s
def main():
    print("numbers 1-10:")
    for i, (w, rom, en) in enumerate(NUMBERS, 1):
        print("  %%d. %%s (%%s) - %%s" %% (i, w, rom, en))
    assert len(NUMBERS) == 10, "need exactly numbers 1-10"
    words = [w for w, _, _ in NUMBERS]
    assert len(set(words)) == 10, "duplicate number words"
    for w, rom, en in NUMBERS + TIMEW:
        assert w and en, "empty number/time row"
    assert len(TIMEW) >= 4, "need 4+ time phrases"
    print("time phrases:", len(TIMEW))
    print("OK: %%s verified numbers 1-10 and %%d time phrases" %% (NAME, len(TIMEW)))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["numbers"], ensure_ascii=False),
       json.dumps(data["time_words"], ensure_ascii=False))


def demo_phrases(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
ITEMS = %s
KIND = %s
MINN = %d
def main():
    n = len(ITEMS)
    print("%%s entries: %%d" %% (KIND, n))
    for w, rom, en, note in ITEMS[:3]:
        print("  %%s (%%s) - %%s" %% (w, rom, en))
    assert n >= MINN, "need %%d+ %%s" %% (MINN, KIND)
    for w, rom, en, note in ITEMS:
        assert w and rom and en and note, "empty phrase row"
    print("OK: %%s verified %%d %%s" %% (NAME, n, KIND))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["items"], ensure_ascii=False),
       json.dumps(data["kind"], ensure_ascii=False), data["min_n"])


def demo_grammar(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
POINTS = %s
def main():
    print("grammar rules:", len(POINTS))
    for t, _x in POINTS:
        print("  -", t)
    assert len(POINTS) >= 6, "need 6+ grammar rules"
    for t, x in POINTS:
        assert t and x and len(x) > 40, "grammar rule too thin: %%s" %% t
    print("OK: %%s verified %%d grammar rules" %% (NAME, len(POINTS)))
if __name__ == "__main__":
    main()
""" % json.dumps(data["points"], ensure_ascii=False)


def demo_themed(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
THEME = %s
SENTS = %s
def main():
    n = len(SENTS)
    print("theme:", THEME, "| sentences:", n)
    print("sample:", SENTS[0][0], "-", SENTS[0][2])
    assert n >= 6, "need 6+ themed sentences"
    for w, rom, en in SENTS:
        assert w and rom and en, "empty sentence row"
        assert len(w.split()) >= 2, "sentence too short: %%s" %% w
    print("OK: %%s verified %%d sentences for %%s" %% (NAME, n, THEME))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["theme"], ensure_ascii=False),
       json.dumps(data["sentences"], ensure_ascii=False))


def demo_tenses(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
TENSES = %s
def main():
    print("tense rows:", len(TENSES))
    labels = set()
    for tense, w, rom, en in TENSES:
        print("  [%%s] %%s - %%s" %% (tense, w, en))
        assert tense and w and rom and en, "empty tense row"
        labels.add(tense)
    assert len(TENSES) >= 6, "need 6+ tense examples"
    assert len(labels) >= 3, "need 3+ distinct tenses"
    print("distinct tenses:", len(labels))
    print("OK: %%s verified %%d tense sentences" %% (NAME, len(TENSES)))
if __name__ == "__main__":
    main()
""" % json.dumps(data["tenses"], ensure_ascii=False)


def demo_qa(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
PAIRS = %s
def main():
    n = len(PAIRS)
    print("Q&A pairs:", n)
    assert n >= 6, "need 6+ Q&A pairs"
    for q, q_rom, q_en, a, a_rom, a_en in PAIRS:
        assert q and q_en and a and a_en, "empty Q&A row"
    print("sample Q:", PAIRS[0][0], "-", PAIRS[0][2])
    print("OK: %%s verified %%d Q&A pairs" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % json.dumps(data["pairs"], ensure_ascii=False)


def demo_story(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
TITLE = %s
LINES = %s
def main():
    n = len(LINES)
    print("story:", TITLE, "| lines:", n)
    assert n >= 6, "story needs 6+ lines"
    for w, rom, en in LINES:
        assert w and rom and en, "empty story line"
    words = sum(len(w.split()) for w, _r, _e in LINES)
    print("story words:", words)
    assert words >= 30, "story too short"
    print("OK: %%s verified story %%s (%%d lines)" %% (NAME, TITLE, n))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["title"], ensure_ascii=False),
       json.dumps(data["lines"], ensure_ascii=False))


def demo_idioms(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
IDIOMS = %s
def main():
    n = len(IDIOMS)
    print("idioms/proverbs:", n)
    assert n >= 5, "need 5+ idioms"
    for w, rom, literal, meaning, ex, ex_rom, ex_en in IDIOMS:
        assert w and literal and meaning, "empty idiom row"
        assert ex and ex_en, "idiom needs an example sentence"
    print("sample:", IDIOMS[0][0], "-", IDIOMS[0][3])
    print("OK: %%s verified %%d idioms/proverbs" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % json.dumps(data["idioms"], ensure_ascii=False)


def demo_registers(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
REGS = %s
def main():
    n = len(REGS)
    print("register pairs:", n)
    assert n >= 5, "need 5+ register pairs"
    for c, c_rom, c_en, f, f_rom, f_en, note in REGS:
        assert c and f and note, "empty register row"
        assert c != f, "casual and formal must differ"
    print("OK: %%s verified %%d casual/formal pairs" %% (NAME, n))
if __name__ == "__main__":
    main()
""" % json.dumps(data["registers"], ensure_ascii=False)


def demo_dialogue(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
TITLE = %s
LINES = %s
def main():
    n = len(LINES)
    print("dialogue:", TITLE, "| lines:", n)
    assert n >= 6, "dialogue needs 6+ lines"
    speakers = set()
    for sp, w, rom, en in LINES:
        assert sp and w and rom and en, "empty dialogue line"
        speakers.add(sp)
    assert len(speakers) >= 2, "dialogue needs 2+ speakers"
    print("speakers:", sorted(speakers))
    print("OK: %%s verified dialogue %%s (%%d lines)" %% (NAME, TITLE, n))
if __name__ == "__main__":
    main()
""" % (json.dumps(data["title"], ensure_ascii=False),
       json.dumps(data["lines"], ensure_ascii=False))


def demo_mastery(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
CHECK = %s
REF = %s
def main():
    print("checklist items:", len(CHECK))
    assert len(CHECK) >= 8, "need 8+ checklist items"
    for t, x in CHECK:
        assert t and x, "empty checklist row"
    assert len(REF) >= 6, "need 6+ reference sentences"
    for w, rom, en in REF:
        assert w and rom and en, "empty reference row"
    print("reference sentences:", len(REF))
    print("OK: %%s verified mastery review" %% NAME)
if __name__ == "__main__":
    main()
""" % (json.dumps(data["checklist"], ensure_ascii=False),
       json.dumps(data["reference"], ensure_ascii=False))


DEMOS = {
    "overview": demo_overview,
    "alphabet": demo_alphabet,
    "phonology": demo_phonology,
    "vocab": demo_vocab,
    "pronouns": demo_pronouns,
    "numbers": demo_numbers,
    "phrases": demo_phrases,
    "grammar": demo_grammar,
    "themed": demo_themed,
    "tenses": demo_tenses,
    "qa": demo_qa,
    "story": demo_story,
    "idioms": demo_idioms,
    "registers": demo_registers,
    "dialogue": demo_dialogue,
    "mastery": demo_mastery,
}
