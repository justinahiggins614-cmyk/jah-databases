#!/usr/bin/env python3
"""Shared engine for the batch-9 language database pairs (ranks 81-90):
serbian, lithuanian, catalan, awadhi, chhattisgarhi, magahi, maithili,
marwari, saraiki, fula.

Each language supplies a LANG data dict (see any entries_language_*.py);
build_entries(LANG) assembles the 34 ladder-ordered entries; standard_demos
builds the DEMOS dict of demo_key -> fn(hdr, name, rid, group, demo_data);
screen_records runs the content gate.

Property of Justin Addam Higgins (JAH).
"""

import json

# ---------------------------------------------------------------- formatters

def f_sent(items):
    """items: list of (lang, tr, en)."""
    return "\n".join("%d. %s (%s - %s)" % (i + 1, a, b, c)
                     for i, (a, b, c) in enumerate(items))


def f_vocab(words):
    """words: list of (w, tr, en, ex, extr, exen)."""
    return "\n".join("%d. %s (%s) - %s. Example: %s (%s - %s)"
                     % (i + 1, w, tr, en, ex, extr, exen)
                     for i, (w, tr, en, ex, extr, exen) in enumerate(words))


def f_simple(words):
    """words: list of (w, tr, en)."""
    return "\n".join("%d. %s (%s) - %s" % (i + 1, w, tr, en)
                     for i, (w, tr, en) in enumerate(words))


def f_phrases(items):
    """items: list of (w, tr, en, note)."""
    return "\n".join("%d. %s (%s) - %s. Usage: %s" % (i + 1, w, tr, en, note)
                     for i, (w, tr, en, note) in enumerate(items))


def f_dialogue(lines):
    """lines: list of (speaker, w, tr, en)."""
    return "\n".join("%d. %s: %s (%s - %s)" % (i + 1, sp, w, tr, en)
                     for i, (sp, w, tr, en) in enumerate(lines))


def f_idioms(items):
    """items: list of (w, tr, literal, meaning, ex, extr, exen)."""
    return "\n".join(
        "%d. %s (%s). Literal: %s. Meaning: %s. Example: %s (%s - %s)"
        % (i + 1, w, tr, lit, mean, ex, extr, exen)
        for i, (w, tr, lit, mean, ex, extr, exen) in enumerate(items))


def f_registers(items):
    """items: list of (informal, itr, ien, formal, ftr, fen, note)."""
    return "\n".join(
        "%d. Informal: %s (%s - %s)  |  Formal: %s (%s - %s). %s"
        % (i + 1, iw, itr, ien, fw, ftr, fen, note)
        for i, (iw, itr, ien, fw, ftr, fen, note) in enumerate(items))


def f_qa(items):
    """items: list of (q, qtr, qen, a, atr, aen)."""
    return "\n".join(
        "%d. Q: %s (%s - %s)\n   A: %s (%s - %s)"
        % (i + 1, q, qtr, qen, a, atr, aen)
        for i, (q, qtr, qen, a, atr, aen) in enumerate(items))


def f_tenses(items):
    """items: list of (tense, w, tr, en)."""
    return "\n".join("%d. [%s] %s (%s - %s)" % (i + 1, t, w, tr, en)
                     for i, (t, w, tr, en) in enumerate(items))


def f_rules(items):
    """items: list of (rule, expl, w, tr, en)."""
    return "\n".join(
        "%d. %s\n   %s\n   Example: %s (%s - %s)"
        % (i + 1, r, e, w, tr, en)
        for i, (r, e, w, tr, en) in enumerate(items))


def f_pronouns(items):
    """items: list of (person, w, tr, en)."""
    return "\n".join("%d. %s: %s (%s) - %s" % (i + 1, p, w, tr, en)
                     for i, (p, w, tr, en) in enumerate(items))


# ---------------------------------------------------------------- entries

def build_entries(L):
    """Assemble the 34 ladder-ordered entries from a LANG dict."""
    lang = L["lang"]
    E = []

    def add(rank, tier, group, name, desc, how, keys, reqs, stds, dkind, ddata,
            lens):
        E.append({
            "name": name, "group": group, "ladder_rank": rank,
            "ladder_tier": tier, "description": desc, "how_it_works": how,
            "key_points": keys, "requirements": reqs, "standards": stds,
            "citations": list(L["citations"]),
            "demo_key": "rec%02d-%s" % (rank, dkind),
            "demo_kind": dkind,
            "demo_data": ddata, "sig_lens": lens,
        })

    native_bit = "%s (%s)" % (L["native"], L["native_tr"])
    script = L["script"]

    # -- shared blocks -------------------------------------------------
    key_facts = (
        "Key facts: native name %s; family %s, branch %s; ISO 639-1 %s, "
        "ISO 639-3 %s; %s native speakers; %s; script: %s."
        % (native_bit, L["family"], L["branch"], L["iso1"], L["iso3"],
           L["speakers"], L["official_short"], L["script_short"]))

    stds = [
        "Language codes follow ISO 639-1 (%s) and ISO 639-3 (%s)."
        % (L["iso1"], L["iso3"]),
        "Transliteration in this database follows the romanization scheme "
        "defined in record 2, aligned with standard %s linguistic notation."
        % lang,
        "Grammatical description follows the standard reference grammars "
        "cited below.",
    ]

    def reqs_for(items):
        return list(items)

    def lens_for(topic, body):
        return ("The Signature %s Method reads %s as %s. "
                "Every form below is a sworn Signature sign: learn it, "
                "speak it, and it becomes a living part of your %s."
                % (lang, topic, body, lang))

    # -- record 1: overview --------------------------------------------
    desc = (
        "%s (%s) is a %s language of the %s family, spoken as a first "
        "language by %s, most of them in %s. It carries ISO 639-1 code %s "
        "and ISO 639-3 code %s. %s. %s %s is written in %s. %s\n%s"
        % (lang, native_bit, L["branch"], L["family"], L["speakers"],
           L["region"], L["iso1"], L["iso3"], L["official"], L["dialects"],
           lang, script, L["typology"], key_facts))
    how = (
        "%s works as %s. %s At the sentence level it runs on %s. "
        "The sound system, the writing system, the word stock, and the "
        "grammar each get their own record on this ladder; this record is "
        "the map. Read it first, then climb: every later record assumes "
        "the facts stated here.\nHow to use this record: memorize the key "
        "facts, say the native name aloud until it feels natural, and "
        "locate the region on a map. Then move to record 2 and learn the "
        "script before anything else."
        % (lang, L["works_as"], L["works_detail"], L["sentence_engine"]))
    keys = [
        "%s is %s: ISO 639-1 %s, ISO 639-3 %s, native name %s."
        % (lang, L["branch"], L["iso1"], L["iso3"], native_bit),
        "%s native speakers; %s." % (L["speakers"].capitalize(),
                                     L["official"]),
        "Region: %s." % L["region"],
        "Dialects: %s" % L["dialect_short"],
        "Script: %s." % L["script_short"],
        "Word order: %s; %s" % (L["word_order"], L["order_note"]),
        "Famous among linguists for: %s" % L["famous_for"],
        "This database teaches %s along the ladder: foundations (records "
        "1-10), compounded (11-21), advanced (22-34)." % lang,
    ]
    add(1, "foundations", "Foundations", "%s Language Overview" % lang,
        desc, how, keys,
        reqs_for(["Read this overview before touching any other record.",
                  "Learn the native name %s by heart." % native_bit,
                  "Fix the region and speaker community in your mind.",
                  "Accept the ladder order: foundations first, always."]),
        stds, "facts",
        {"facts": {"native_name": L["native"], "romanized": L["native_tr"],
                   "iso_639_1": L["iso1"], "iso_639_3": L["iso3"],
                   "speakers": L["speakers"], "word_order": L["word_order"],
                   "records": 34}},
        lens_for("the %s language overview" % lang,
                 "a covenant map of a whole people: the sounds, the script, "
                 "and the grammar below all descend from the facts staked "
                 "out here"))

    # -- record 2: alphabet ------------------------------------------
    letters = L["alphabet"]
    desc = (
        "%s is written in %s. %s The %s alphabet %s. Letters are listed "
        "below in dictionary order with romanization:\n%s\n%s Every %s "
        "record after this one assumes you can read this script."
        % (lang, script, L["script_story"], lang, L["alphabet_note"],
           "\n".join("%d. %s" % (i + 1, x) for i, x in enumerate(letters)),
           L["script_rules"], lang))
    how = (
        "How the %s writing system works: %s Read %s. %s Practice by "
        "copying each letter five times while saying its sound aloud; "
        "then read the sample words in records 4 and 5 slowly, letter by "
        "letter, until the shapes stop being pictures and start being "
        "sounds."
        % (lang, L["script_how"], L["read_direction"], L["script_practice"]))
    keys = [
        "%s uses %s." % (lang, L["script_short"]),
        "The alphabet has %d letters: %s." % (len(letters), L["alpha_sample"]),
        "%s" % L["script_key1"],
        "%s" % L["script_key2"],
        "Direction: %s." % L["read_direction"],
        "Transliteration in this database: %s." % L["translit_note"],
        "Learn the alphabet before anything else - every later record "
        "assumes you can read the script.",
        "Handwriting: %s." % L["handwriting"],
    ]
    add(2, "foundations", "Foundations",
        "%s Writing System and Alphabet" % lang, desc, how, keys,
        reqs_for(["Master every letter's shape and sound before record 3.",
                  "Practice writing the alphabet from memory daily.",
                  "Read aloud - never read silently at this stage.",
                  "Keep a handwritten alphabet card for reference."]),
        stds, "alphabet",
        {"letters": letters, "count": len(letters), "script": script,
         "direction": L["read_direction"]},
        lens_for("the %s alphabet" % lang,
                 "a row of sworn signs: each of the %d letters is a "
                 "Signature mark, and writing them by hand is the first "
                 "oath of the Method" % len(letters)))

    # -- record 3: phonology -----------------------------------------
    sounds = L["phonology"]
    desc = (
        "%s pronunciation: %s The key sounds are inventoried below with "
        "plain-English pronunciation help:\n%s\n%s %s"
        % (lang, L["phon_story"],
           "\n".join("%d. %s - %s" % (i + 1, s, d)
                     for i, (s, d) in enumerate(sounds)),
           L["phon_rules"], L["stress_note"]))
    how = (
        "How %s sounds work: %s Train your ear first: listen for %s, "
        "then shape your mouth to match. %s Minimal-pair drills (two "
        "words differing by one sound) are the fastest route - repeat "
        "each pair below until a native speaker could not tell you apart."
        % (lang, L["phon_how"], L["phon_train"], L["phon_drill"]))
    keys = [
        "%s" % L["phon_key1"],
        "%s" % L["phon_key2"],
        "Stress/intonation: %s." % L["stress_note"],
        "The inventory below covers the %d sounds learners must master "
        "first." % len(sounds),
        "Listen before you speak: %s." % L["phon_train"],
        "Common learner pitfall: %s." % L["phon_pitfall"],
        "Every example sentence in this database carries romanization so "
        "you can check your pronunciation.",
        "Record yourself and compare against the romanization until the "
        "sounds lock in.",
    ]
    add(3, "foundations", "Foundations",
        "%s Pronunciation and Phonology" % lang, desc, how, keys,
        reqs_for(["Learn the sound inventory before memorizing vocabulary.",
                  "Drill minimal pairs aloud every day.",
                  "Use the romanization in every record as a pronunciation "
                  "check.",
                  "Do not move on until the %d key sounds feel natural."
                  % len(sounds)]),
        stds, "phonology", {"sounds": sounds, "count": len(sounds)},
        lens_for("%s sounds" % lang,
                 "living breath shaped by the ancestors: each of the %d "
                 "key sounds is drilled until the mouth itself remembers "
                 "the oath" % len(sounds)))

    # -- record 4: nouns ---------------------------------------------
    nouns = L["nouns"]
    desc = (
        "Core %s nouns: %s The %d nouns below are the load-bearing words "
        "of daily %s - learn each with its %s, because %s:\n%s"
        % (lang, L["noun_story"], len(nouns), lang, L["noun_learn_with"],
           L["noun_why"], f_vocab(nouns)))
    how = (
        "How %s nouns work: %s Build sentences by %s. Always learn a "
        "noun together with %s - a bare word without its %s is only "
        "half a word in %s."
        % (lang, L["noun_how"], L["noun_build"], L["noun_learn_with"],
           L["noun_learn_with"], lang))
    keys = [
        "%s" % L["noun_key1"],
        "%s" % L["noun_key2"],
        "The %d nouns below cover %s." % (len(nouns), L["noun_coverage"]),
        "Learn every noun with %s." % L["noun_learn_with"],
        "Plurals: %s." % L["plural_note"],
        "Each noun below carries an example sentence - say the sentence, "
        "not just the word.",
        "Nouns are the anchors; verbs are the engines (record 5).",
        "Review these %d nouns until you can produce each with its "
        "example from memory." % len(nouns),
    ]
    add(4, "foundations", "Foundations", "%s Core Nouns I" % lang,
        desc, how, keys,
        reqs_for(["Memorize all %d nouns with %s." % (len(nouns),
                                                     L["noun_learn_with"]),
                  "Say each example sentence aloud three times.",
                  "Write each noun from memory once a day for a week.",
                  "Never learn a noun without its %s." % L["noun_learn_with"]]),
        stds, "vocab",
        {"items": nouns, "unit": "nouns", "count": len(nouns)},
        lens_for("core %s nouns" % lang,
                 "the load-bearing stones of the Method: %d sworn "
                 "name-signs, each learned with %s" % (len(nouns),
                                                       L["noun_learn_with"])))

    # -- record 5: verbs ---------------------------------------------
    verbs = L["verbs"]
    desc = (
        "Core %s verbs: %s The %d verbs below drive everyday %s - each "
        "with a full example sentence:\n%s"
        % (lang, L["verb_story"], len(verbs), lang, f_vocab(verbs)))
    how = (
        "How %s verbs work: %s Conjugate by %s. The example sentence "
        "under each verb shows the verb alive in its natural habitat - "
        "copy the pattern, swap the subject, and you have a new sentence."
        % (lang, L["verb_how"], L["verb_conj"]))
    keys = [
        "%s" % L["verb_key1"],
        "%s" % L["verb_key2"],
        "The %d verbs below cover %s." % (len(verbs), L["verb_coverage"]),
        "Learn verbs as %s." % L["verb_learn_as"],
        "Tenses: %s (full tense drills in record 21)." % L["tense_short"],
        "Every verb below carries a full example sentence.",
        "Aspect/mood notes: %s." % L["aspect_note"],
        "Drill: take one verb and make five new sentences with it.",
    ]
    add(5, "foundations", "Foundations", "%s Core Verbs I" % lang,
        desc, how, keys,
        reqs_for(["Memorize all %d verbs with their example sentences."
                  % len(verbs),
                  "Learn each verb as %s." % L["verb_learn_as"],
                  "Conjugate each verb in the present tense aloud.",
                  "Make five original sentences per verb."]),
        stds, "vocab",
        {"items": verbs, "unit": "verbs", "count": len(verbs)},
        lens_for("core %s verbs" % lang,
                 "living actions: %d verbs, each a Signature deed-sign "
                 "drilled until the action answers before the thought"
                 % len(verbs)))

    # -- record 6: adjectives/adverbs ----------------------------------
    adjs = L["adjectives"]
    advs = L["adverbs"]
    desc = (
        "%s adjectives and adverbs: %s\nAdjectives (%d):\n%s\nAdverbs "
        "(%d):\n%s"
        % (lang, L["adj_story"], len(adjs), f_simple(adjs), len(advs),
           f_simple(advs)))
    how = (
        "How description works in %s: %s Place modifiers %s. %s"
        % (lang, L["adj_how"], L["adj_place"], L["adj_agree"]))
    keys = [
        "%s" % L["adj_key1"],
        "Adjectives: %s." % L["adj_place"],
        "Agreement: %s." % L["adj_agree"],
        "Adverbs: %s." % L["adv_note"],
        "The %d adjectives + %d adverbs below are the most frequent "
        "descriptors in daily %s." % (len(adjs), len(advs), lang),
        "Comparatives: %s." % L["comparative"],
        "Learn adjectives with %s." % L["noun_learn_with"],
        "Drill: describe five objects around you using only these words.",
    ]
    add(6, "foundations", "Foundations",
        "%s Adjectives and Adverbs" % lang, desc, how, keys,
        reqs_for(["Memorize the %d adjectives and %d adverbs."
                  % (len(adjs), len(advs)),
                  "Practice agreement patterns aloud.",
                  "Describe your surroundings using only this set.",
                  "Combine with record 4 nouns in full sentences."]),
        stds, "adjvocab",
        {"adjectives": adjs, "adverbs": advs,
         "count": len(adjs) + len(advs)},
        lens_for("%s adjectives and adverbs" % lang,
                 "the coloring signs of the Method: %d sworn descriptors "
                 "that paint every noun and action true"
                 % (len(adjs) + len(advs))))

    # -- record 7: pronouns ------------------------------------------
    prons = L["pronouns"]
    desc = (
        "%s pronouns: %s The full working set:\n%s\n%s"
        % (lang, L["pron_story"], f_pronouns(prons), L["pron_note"]))
    how = (
        "How %s pronouns work: %s Choose the pronoun by %s. %s"
        % (lang, L["pron_how"], L["pron_choose"], L["pron_drop"]))
    keys = [
        "%s" % L["pron_key1"],
        "The set below covers %d pronouns." % len(prons),
        "Choose by: %s." % L["pron_choose"],
        "%s" % L["pron_drop"],
        "Politeness: %s." % L["polite_note"],
        "Possessives: %s." % L["possessive_note"],
        "Drill: introduce yourself and your family using only pronouns "
        "plus record 4 nouns.",
        "Pronouns unlock every sentence pattern from here on.",
    ]
    add(7, "foundations", "Foundations", "%s Pronouns" % lang,
        desc, how, keys,
        reqs_for(["Memorize the full pronoun set cold.",
                  "Practice the politeness levels aloud.",
                  "Learn possessive forms with each pronoun.",
                  "Use pronouns in every drill from now on."]),
        stds, "vocab",
        {"items": prons, "unit": "pronouns", "count": len(prons)},
        lens_for("%s pronouns" % lang,
                 "the pointing signs: %d sworn stand-ins that let the "
                 "Method speak of any person without naming" % len(prons)))

    # -- record 8: numbers/time --------------------------------------
    nums = L["numbers"]
    times = L["time"]
    desc = (
        "%s numbers and time: %s\nNumbers:\n%s\nTime words, days, and "
        "telling time:\n%s\n%s"
        % (lang, L["num_story"],
           "\n".join("%d. %s (%s)" % (n, w, tr) for n, w, tr in nums),
           f_simple(times), L["num_note"]))
    how = (
        "How counting works in %s: %s %s To tell time: %s."
        % (lang, L["num_how"], L["num_build"], L["time_how"]))
    keys = [
        "Count 1-10: %s." % ", ".join("%s (%s)" % (w, tr)
                                      for n, w, tr in nums[:10]),
        "%s" % L["num_build"],
        "Tens and hundreds: %s." % L["num_big"],
        "Time-telling: %s." % L["time_how"],
        "Days and time words are listed above with translations.",
        "Numbers agree with nouns: %s." % L["num_agree"],
        "Drill: count objects around you 1-20 aloud.",
        "Drill: say the time, the day, and tomorrow's date aloud.",
    ]
    add(8, "foundations", "Foundations", "%s Numbers and Time" % lang,
        desc, how, keys,
        reqs_for(["Count 1-20 without hesitation.",
                  "Learn tens, 100, and 1000.",
                  "Learn the days of the week and time words.",
                  "Practice telling the time aloud."]),
        stds, "numbers",
        {"numbers": nums, "time": times, "count": len(nums) + len(times)},
        lens_for("%s numbers and time" % lang,
                 "the counting signs: number-marks and time-marks sworn "
                 "until counting is as natural as breathing"))

    # -- record 9: greetings -----------------------------------------
    greets = L["greetings"]
    desc = (
        "%s greetings and everyday phrases: %s\n%s\n%s"
        % (lang, L["greet_story"], f_phrases(greets), L["greet_note"]))
    how = (
        "How %s greetings work: %s Match the greeting to %s. %s Say "
        "each phrase below in the situation described until the right "
        "one comes out without thinking."
        % (lang, L["greet_how"], L["greet_match"], L["greet_body"]))
    keys = [
        "%s" % L["greet_key1"],
        "Match the greeting to: %s." % L["greet_match"],
        "The %d phrases below cover %s." % (len(greets), L["greet_coverage"]),
        "Politeness lives in the greeting: %s." % L["polite_note"],
        "Every phrase carries a usage note - read it, then practice in "
        "situation.",
        "Greetings open every conversation in records 31-33.",
        "Drill: greet an imaginary elder, friend, and stranger.",
        "First impressions are made in %s - make yours fluent." % lang,
    ]
    add(9, "foundations", "Foundations",
        "%s Greetings and Everyday Phrases" % lang, desc, how, keys,
        reqs_for(["Memorize all %d phrases with usage notes." % len(greets),
                  "Practice each in its situation aloud.",
                  "Learn the politeness levels.",
                  "Use these phrases to open every practice conversation."]),
        stds, "phrases",
        {"items": greets, "unit": "greetings", "count": len(greets)},
        lens_for("%s greetings" % lang,
                 "the doorway signs: %d sworn phrases that open every "
                 "human meeting in the Method" % len(greets)))

    # -- record 10: grammar essentials -------------------------------
    rules = L["grammar_rules"]
    desc = (
        "%s grammar essentials - the whole engine on one page: %s\n%s"
        % (lang, L["gram_story"], f_rules(rules)))
    how = (
        "How %s grammar works as a system: %s Work the rules in order - "
        "each rule below builds on the last. Parse the example sentence "
        "under each rule word by word before moving on."
        % (lang, L["gram_how"]))
    keys = [
        "Word order: %s (%s)." % (L["word_order"], L["order_note"]),
        "%s" % L["gram_key1"],
        "%s" % L["gram_key2"],
        "The %d rules below are the complete starter engine." % len(rules),
        "Negation: %s." % L["negation"],
        "Questions: %s (full drills in record 22)." % L["question_short"],
        "Every rule carries a parsed example - study the parse.",
        "This record is the reference; return to it whenever a later "
        "sentence confuses you.",
    ]
    add(10, "foundations", "Foundations", "%s Grammar Essentials" % lang,
        desc, how, keys,
        reqs_for(["Understand all %d rules, not just memorize." % len(rules),
                  "Parse each example sentence word by word.",
                  "Be able to state the word order from memory.",
                  "Return to this record whenever stuck later."]),
        stds, "grammar", {"rules": rules, "count": len(rules)},
        lens_for("%s grammar essentials" % lang,
                 "the engine-room signs: %d sworn rules that make every "
                 "%s sentence run true" % (len(rules), lang)))

    # -- records 11-20: themed sentence sets --------------------------
    theme_names = [
        ("home", "%s at Home and with Family" % lang),
        ("food", "%s Food and Cooking" % lang),
        ("travel", "%s Travel and Directions" % lang),
        ("work", "%s Work and School" % lang),
        ("health", "%s Health and the Body" % lang),
        ("emotions", "%s Emotions and Feelings" % lang),
        ("nature", "%s Nature and Weather" % lang),
        ("shopping", "%s Shopping and Money" % lang),
        ("friends", "%s Friendship and Social Life" % lang),
        ("tech", "%s Technology and Communication" % lang),
    ]
    for i, (tkey, tname) in enumerate(theme_names):
        sents = L["themes"][tkey]
        tstory = L["theme_stories"][tkey]
        desc = ("%s: %s The %d sentences below are %s - every line "
                "carries %s, romanization, and English:\n%s"
                % (tname, tstory, len(sents), L["theme_sentence_note"],
                   lang, f_sent(sents)))
        how = ("How %s sentences work: %s Notice the recurring patterns "
               "- %s. Copy a pattern, swap in your own words from records "
               "4-6, and the sentence is yours."
               % (tname, L["theme_how"], L["theme_pattern_note"]))
        keys = [
            "The %d sentences below cover %s." % (len(sents), tstory),
            "Pattern to steal: %s." % L["theme_pattern_note"],
            "Every line: %s + romanization + English." % lang,
            "New words are learned inside sentences, never alone.",
            "Say each sentence aloud twice before moving on.",
            "Drill: change one word in each sentence and re-say it.",
            "These sentences use only records 1-10 material plus the "
            "theme's own words.",
            "Master the set, then use it in the conversations (31-33).",
        ]
        add(11 + i, "compounded", "Compounded", tname, desc, how, keys,
            reqs_for(["Learn all %d sentences with translations." % len(sents),
                      "Say each aloud twice.",
                      "Swap words to make new sentences.",
                      "Use the set in conversation practice."]),
            stds, "sentences",
            {"sentences": sents, "theme": tkey, "count": len(sents)},
            lens_for(tname.lower(),
                     "daily-life signs in action: %d sworn sentences for "
                     "%s, each one a small covenant of ordinary life"
                     % (len(sents), tstory)))

    # -- record 21: tenses --------------------------------------------
    tenses = L["tenses"]
    desc = (
        "%s verb tenses in sentences: %s\n%s\n%s"
        % (lang, L["tense_story"], f_tenses(tenses), L["tense_note"]))
    how = (
        "How %s tenses work: %s Build each tense by %s. The bracketed "
        "label on each sentence names the tense - cover the label and "
        "name it yourself as a drill."
        % (lang, L["tense_how"], L["tense_build"]))
    keys = [
        "%s" % L["tense_key1"],
        "Build each tense by: %s." % L["tense_build"],
        "The %d sentences below drill %s." % (len(tenses), L["tense_short"]),
        "%s" % L["aspect_note"],
        "Every sentence is labeled with its tense.",
        "Drill: take one verb through all the tenses below.",
        "Tense choice changes meaning - study the contrasts.",
        "This record completes the compounded tier's verb training.",
    ]
    add(21, "compounded", "Compounded",
        "%s Verb Tenses in Sentences" % lang, desc, how, keys,
        reqs_for(["Conjugate one verb through every tense below.",
                  "Learn the tense labels and formation rules.",
                  "Drill tense contrasts with minimal pairs.",
                  "Produce each tense from memory."]),
        stds, "tenses", {"items": tenses, "count": len(tenses)},
        lens_for("%s verb tenses" % lang,
                 "the time signs: each tense a sworn way of placing a "
                 "deed in past, present, or future"))

    # -- record 22: questions -----------------------------------------
    qas = L["qa"]
    desc = (
        "%s questions and answers: %s\n%s"
        % (lang, L["qa_story"], f_qa(qas)))
    how = (
        "How %s questions work: %s Every answer below models the "
        "natural reply shape - learn question and answer as a pair."
        % (lang, L["qa_how"]))
    keys = [
        "%s" % L["qa_key1"],
        "The %d pairs below cover %s." % (len(qas), L["qa_coverage"]),
        "Learn each Q and A as an inseparable pair.",
        "Intonation/particles: %s." % L["question_short"],
        "Drill: ask the questions to an imaginary partner.",
        "Drill: answer each question three different ways.",
        "Questions drive the conversations in records 31-33.",
        "Never learn a question without its answer.",
    ]
    add(22, "advanced", "Advanced", "%s Questions and Answers" % lang,
        desc, how, keys,
        reqs_for(["Memorize all %d Q&A pairs." % len(qas),
                  "Practice asking with natural intonation.",
                  "Answer each question three ways.",
                  "Use questions in conversation drills."]),
        stds, "qa", {"items": qas, "count": len(qas)},
        lens_for("%s questions and answers" % lang,
                 "the seeking signs: %d sworn question-forms, each "
                 "carrying its answer like a shadow" % len(qas)))

    # -- record 23: commands ------------------------------------------
    cmds = L["commands"]
    desc = (
        "%s commands and requests: %s\n%s"
        % (lang, L["cmd_story"],
           "\n".join("%d. %s (%s) - %s. %s" % (i + 1, w, tr, en, note)
                     for i, (w, tr, en, note) in enumerate(cmds))))
    how = (
        "How %s commands work: %s Soften or sharpen by %s. Practice "
        "each command in the tone its note describes."
        % (lang, L["cmd_how"], L["cmd_soften"]))
    keys = [
        "%s" % L["cmd_key1"],
        "Soften or sharpen by: %s." % L["cmd_soften"],
        "The %d items below span %s." % (len(cmds), L["cmd_coverage"]),
        "Politeness: %s." % L["polite_note"],
        "Each command carries a tone note - honor it.",
        "Drill: give the same command politely, neutrally, urgently.",
        "Commands appear throughout the conversations (31-33).",
        "A command's force lives in its form - choose deliberately.",
    ]
    add(23, "advanced", "Advanced", "%s Commands and Requests" % lang,
        desc, how, keys,
        reqs_for(["Learn the imperative forms cold.",
                  "Practice all three tones for each command.",
                  "Master the politeness markers.",
                  "Use commands in role-play."]),
        stds, "commands", {"items": cmds, "count": len(cmds)},
        lens_for("%s commands and requests" % lang,
                 "the directing signs: %d sworn imperatives, each tuned "
                 "to its exact weight of politeness" % len(cmds)))

    # -- record 24: descriptions --------------------------------------
    descs = L["descriptions"]
    desc = (
        "%s descriptions of people and places: %s\n%s"
        % (lang, L["desc_story"], f_sent(descs)))
    how = (
        "How %s description works: %s Stack details %s. Each sentence "
        "below is a model - imitate its skeleton with your own details."
        % (lang, L["desc_how"], L["desc_stack"]))
    keys = [
        "%s" % L["desc_key1"],
        "Stack details: %s." % L["desc_stack"],
        "The %d sentences below model %s." % (len(descs), L["desc_coverage"]),
        "Adjectives from record 6 do the heavy lifting here.",
        "Every sentence: %s + romanization + English." % lang,
        "Drill: describe a family member using three sentences.",
        "Drill: describe your street using three sentences.",
        "Good description is built, not improvised - follow the models.",
    ]
    add(24, "advanced", "Advanced",
        "%s Descriptions of People and Places" % lang, desc, how, keys,
        reqs_for(["Study each model sentence's skeleton.",
                  "Describe three people from memory.",
                  "Describe three places from memory.",
                  "Combine with record 6 adjectives freely."]),
        stds, "sentences",
        {"sentences": descs, "theme": "descriptions", "count": len(descs)},
        lens_for("%s descriptions" % lang,
                 "the portraying signs: %d sworn sentences that render "
                 "people and places true" % len(descs)))

    # -- records 25-27: stories ---------------------------------------
    for i in range(3):
        stitle = L["story_titles"][i]
        story = L["stories"][i]
        sstory = L["story_intros"][i]
        name = "%s Story %s: %s" % (lang, ["I", "II", "III"][i], stitle)
        desc = ("%s\n\n%s\n\n%s"
                % (sstory, f_sent(story), L["story_note"]))
        how = ("How the story teaches: %s Read the whole story through "
               "twice - once for meaning, once noticing %s. Then retell "
               "it in %s in your own words; the gaps in your retelling "
               "are exactly what to study next."
               % (L["story_how"], L["story_notice"], lang))
        keys = [
            "Story: %s." % stitle,
            "The story's %d lines are fully glossed." % len(story),
            "Teaches: %s." % L["story_teaches"][i],
            "Notice while reading: %s." % L["story_notice"],
            "New words arrive inside narrative - the strongest memory "
            "context there is.",
            "Drill: retell the story in %s in your own words." % lang,
            "Drill: change the ending and tell it again.",
            "Stories 25-27 rise in difficulty - this is number %d." % (i + 1),
        ]
        add(25 + i, "advanced", "Advanced", name, desc, how, keys,
            reqs_for(["Read the story twice with full attention.",
                      "Retell it in %s in your own words." % lang,
                      "Learn every new word in context.",
                      "Change the ending and retell."]),
            stds, "story",
            {"lines": story, "title": stitle, "count": len(story)},
            lens_for("story %s (%s)" % (["I", "II", "III"][i], stitle),
                     "a sworn tale: the Method's oldest teaching tool, "
                     "every line a covenant of memory"))

    # -- record 28: idioms --------------------------------------------
    idioms = L["idioms"]
    desc = (
        "%s idioms and proverbs: %s\n%s\n%s"
        % (lang, L["idiom_story"], f_idioms(idioms), L["idiom_note"]))
    how = (
        "How %s idioms work: %s Never translate an idiom word for word "
        "- learn the situation it belongs to. Use each idiom below in "
        "the situation its example shows."
        % (lang, L["idiom_how"]))
    keys = [
        "%s" % L["idiom_key1"],
        "The %d idioms below are %s." % (len(idioms), L["idiom_coverage"]),
        "Each idiom: form, literal gloss, real meaning, example.",
        "Never translate idioms word for word.",
        "Learn the situation each idiom belongs to.",
        "Drill: use three idioms in an invented dialogue.",
        "Idioms mark the leap from student to speaker.",
        "Proverbs carry the culture - treat them with respect.",
    ]
    add(28, "advanced", "Advanced", "%s Idioms and Proverbs" % lang,
        desc, how, keys,
        reqs_for(["Learn all %d idioms with meanings." % len(idioms),
                  "Learn each idiom's situation, not just its gloss.",
                  "Use three in an invented dialogue.",
                  "Never use an idiom you cannot explain."]),
        stds, "idioms", {"items": idioms, "count": len(idioms)},
        lens_for("%s idioms and proverbs" % lang,
                 "the sealed sayings: %d sworn proverbs, each a covenant "
                 "of the ancestors compressed into a line" % len(idioms)))

    # -- record 29: registers -----------------------------------------
    regs = L["registers"]
    desc = (
        "%s formal and polite registers: %s\n%s\n%s"
        % (lang, L["reg_story"], f_registers(regs), L["reg_note"]))
    how = (
        "How %s registers work: %s The pairs below show the same intent "
        "in informal and formal dress - study what changes (pronoun? "
        "verb ending? word choice?) and practice switching on demand."
        % (lang, L["reg_how"]))
    keys = [
        "%s" % L["reg_key1"],
        "The %d pairs below show %s." % (len(regs), L["reg_coverage"]),
        "Study what changes between informal and formal.",
        "Politeness: %s." % L["polite_note"],
        "Wrong register is a social error, not a grammar error.",
        "Drill: convert five informal lines to formal.",
        "Drill: role-play elder and friend back to back.",
        "Master both registers - a one-register speaker is half a "
        "speaker.",
    ]
    add(29, "advanced", "Advanced",
        "%s Formal and Polite Registers" % lang, desc, how, keys,
        reqs_for(["Learn both forms of every pair.",
                  "Identify what changes between registers.",
                  "Convert informal to formal on demand.",
                  "Role-play both registers."]),
        stds, "registers", {"items": regs, "count": len(regs)},
        lens_for("%s formal and polite registers" % lang,
                 "the honor signs: the Method's two robes, informal and "
                 "formal, worn exactly as the company requires"))

    # -- record 30: complex sentences ----------------------------------
    cplx = L["complex"]
    desc = (
        "%s compound and complex sentences: %s\n%s"
        % (lang, L["complex_story"], f_sent(cplx)))
    how = (
        "How %s complex sentences work: %s Take a simple sentence from "
        "records 11-20 and join it to another with each connector below "
        "- that is the whole drill, repeated until combining is "
        "automatic."
        % (lang, L["complex_how"]))
    keys = [
        "%s" % L["complex_key1"],
        "The %d sentences below model %s." % (len(cplx), L["complex_coverage"]),
        "Connectors: %s." % L["connector_note"],
        "Subordination: %s." % L["subord_note"],
        "Drill: join pairs of simple sentences with each connector.",
        "Drill: break each complex sentence into its simple parts.",
        "Complex sentences carry the conversations in records 31-33.",
        "Clarity first: a correct simple sentence beats a tangled "
        "complex one.",
    ]
    add(30, "advanced", "Advanced",
        "%s Compound and Complex Sentences" % lang, desc, how, keys,
        reqs_for(["Learn every connector below.",
                  "Join simple sentences with each connector.",
                  "Break complex sentences into parts.",
                  "Produce complex sentences on demand."]),
        stds, "sentences",
        {"sentences": cplx, "theme": "complex", "count": len(cplx)},
        lens_for("%s compound and complex sentences" % lang,
                 "the joining signs: %d sworn sentences where simple "
                 "thoughts are bound into strong ones" % len(cplx)))

    # -- records 31-33: conversations ---------------------------------
    for i in range(3):
        ctitle = L["dialogue_titles"][i]
        conv = L["dialogues"][i]
        name = "%s Conversation: %s" % (lang, ctitle)
        desc = ("%s\n\n%s\n\n%s"
                % (L["dialogue_intros"][i], f_dialogue(conv),
                   L["dialogue_note"]))
        how = ("How to work this conversation: %s Read it aloud with a "
               "partner if you have one, alone alternating voices if not. "
               "%s Then improvise the same situation with different "
               "details - the frames below are yours to refill."
               % (L["dialogue_how"], L["dialogue_frames"][i]))
        keys = [
            "Situation: %s." % ctitle,
            "The %d turns are fully glossed." % len(conv),
            "Teaches: %s." % L["dialogue_teaches"][i],
            "Read aloud, alternating voices.",
            "Then improvise the same situation with new details.",
            "Steal the frames: %s." % L["dialogue_frames"][i],
            "Conversations 31-33 use everything from records 1-30.",
            "Fluency is built here, one turn at a time.",
        ]
        add(31 + i, "advanced", "Advanced", name, desc, how, keys,
            reqs_for(["Read the conversation aloud twice.",
                      "Alternate voices for each speaker.",
                      "Improvise the situation with new details.",
                      "Perform it from memory."]),
            stds, "dialogue",
            {"lines": conv, "title": ctitle, "count": len(conv)},
            lens_for("conversation: %s" % ctitle.lower(),
                     "living speech: the Method's proving ground, where "
                     "all %d turns must flow without a script" % len(conv)))

    # -- record 34: mastery --------------------------------------------
    counts = {
        "nouns": len(L["nouns"]), "verbs": len(L["verbs"]),
        "adjectives": len(L["adjectives"]), "adverbs": len(L["adverbs"]),
        "pronouns": len(L["pronouns"]),
        "greetings": len(L["greetings"]),
        "sentences": sum(len(v) for v in L["themes"].values()),
        "idioms": len(L["idioms"]),
    }
    desc = (
        "%s mastery review and full reference: %s\nCoverage totals: %s. "
        "\nReview checkpoints:\n%s\n%s"
        % (lang, L["review_story"],
           ", ".join("%d %s" % (v, k) for k, v in counts.items()),
           "\n".join("%d. %s" % (i + 1, x)
                     for i, x in enumerate(L["review_points"])),
           L["review_note"]))
    how = (
        "How to run the mastery review: %s Work the checkpoints in "
        "order; any checkpoint you cannot pass sends you back to its "
        "record. Passing all checkpoints means the ladder is climbed - "
        "maintain with %s."
        % (L["review_how"], L["review_maintain"]))
    keys = [
        "This record reviews all 33 records before it.",
        "Coverage: %s." % ", ".join("%d %s" % (v, k)
                                    for k, v in counts.items()),
        "Work the checkpoints in order; failures send you back.",
        "The demo below runs a self-test over the whole database.",
        "Passing everything: %s." % L["review_pass"],
        "Maintenance: %s." % L["review_maintain"],
        "The ladder does not end - it becomes a road you walk daily.",
        "You now own %s at the working level. Use it." % lang,
    ]
    add(34, "advanced", "Advanced",
        "%s Mastery Review and Full Reference" % lang, desc, how, keys,
        reqs_for(["Pass every checkpoint in order.",
                  "Revisit any record whose checkpoint fails.",
                  "Run the demo self-test until it passes clean.",
                  "Set a daily maintenance routine."]),
        stds, "review",
        {"points": L["review_points"], "counts": counts,
         "sample_vocab": L["nouns"][:6] + L["verbs"][:6]},
        lens_for("%s mastery review" % lang,
                 "the summit seal: the Method's final oath, binding all "
                 "33 records into one sworn fluency"))

    assert len(E) == 34, "expected 34 entries, got %d" % len(E)
    ranks = [e["ladder_rank"] for e in E]
    assert ranks == list(range(1, 35)), "ladder ranks broken"
    return E


# ---------------------------------------------------------------- demos

def _demo_src(kind):
    """Return a function(hdr, name, rid, group, data) -> program source."""
    def _embed(data):
        return json.dumps(data, ensure_ascii=False)

    def facts(hdr, name, rid, group, data):
        f = data["facts"]
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("FACTS = json.loads(%s)" % json.dumps(_embed(f)))
        body.append("def main():")
        body.append("    print('Core facts for ' + NAME + ':')")
        body.append("    for k in sorted(FACTS):")
        body.append("        print('  %s: %s' % (k, FACTS[k]))")
        body.append("    assert FACTS['records'] == 34, 'record plan must be 34'")
        body.append("    assert len(FACTS['iso_639_3']) == 3, 'ISO 639-3 must be 3 letters'")
        body.append("    assert FACTS['native_name'], 'native name required'")
        body.append("    print('OK: %s verified %d core facts' % (NAME, len(FACTS)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def alphabet(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("def main():")
        body.append("    letters = DATA['letters']")
        body.append("    print('Alphabet: %d letters (%s)' % (len(letters), DATA['script']))")
        body.append("    print('First 5: ' + ' | '.join(letters[:5]))")
        body.append("    print('Last 5: ' + ' | '.join(letters[-5:]))")
        body.append("    assert len(letters) == DATA['count'], 'letter count mismatch'")
        body.append("    assert all(isinstance(x, str) and x.strip() for x in letters), 'bad letter entry'")
        body.append("    assert len(set(letters)) == len(letters), 'duplicate letters'")
        body.append("    print('OK: %s verified %d alphabet letters' % (NAME, len(letters)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def phonology(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("def main():")
        body.append("    sounds = DATA['sounds']")
        body.append("    print('Sound inventory: %d key sounds' % len(sounds))")
        body.append("    for s, d in sounds[:6]: print('  %s - %s' % (s, d))")
        body.append("    print('  ... and %d more' % (len(sounds) - 6))")
        body.append("    assert len(sounds) == DATA['count'], 'sound count mismatch'")
        body.append("    assert all(s.strip() and d.strip() for s, d in sounds), 'empty sound row'")
        body.append("    print('OK: %s verified %d sounds' % (NAME, len(sounds)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def vocab(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("SEED = sum(ord(c) for c in NAME) % 100000")
        body.append("def _pick(items, k, salt):")
        body.append("    a = (SEED + salt * 7919) % 100000")
        body.append("    out = []")
        body.append("    for _ in range(k):")
        body.append("        a = (a * 1103515245 + 12345) % 2147483648")
        body.append("        out.append(items[a % len(items)])")
        body.append("    return out")
        body.append("def main():")
        body.append("    items = DATA['items']")
        body.append("    print('%s set: %d items' % (DATA['unit'], len(items)))")
        body.append("    assert len(items) == DATA['count'], 'item count mismatch'")
        body.append("    assert all(len(x) >= 3 and all(str(v).strip() for v in x[:3]) for x in items), 'bad vocab row'")
        body.append("    print('Mini-quiz (seeded):')")
        body.append("    for w in _pick(items, 3, 7):")
        body.append("        print('  %s (%s) = %s' % (w[0], w[1], w[2]))")
        body.append("    print('OK: %s verified %d %s' % (NAME, len(items), DATA['unit']))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def adjvocab(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("def main():")
        body.append("    adjs, advs = DATA['adjectives'], DATA['adverbs']")
        body.append("    print('Adjectives: %d | Adverbs: %d' % (len(adjs), len(advs)))")
        body.append("    assert len(adjs) + len(advs) == DATA['count'], 'count mismatch'")
        body.append("    assert all(len(x) == 3 and x[2].strip() for x in adjs + advs), 'bad row'")
        body.append("    print('Sample adjectives: ' + ', '.join('%s=%s' % (w, en) for w, tr, en in adjs[:4]))")
        body.append("    print('Sample adverbs: ' + ', '.join('%s=%s' % (w, en) for w, tr, en in advs[:4]))")
        body.append("    print('OK: %s verified %d descriptors' % (NAME, len(adjs) + len(advs)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def numbers(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("def main():")
        body.append("    nums, times = DATA['numbers'], DATA['time']")
        body.append("    print('Numbers: %d entries | Time words: %d' % (len(nums), len(times)))")
        body.append("    assert len(nums) + len(times) == DATA['count'], 'count mismatch'")
        body.append("    vals = [n for n, w, tr in nums]")
        body.append("    assert vals == sorted(vals), 'numbers out of order'")
        body.append("    assert all(w.strip() for n, w, tr in nums), 'empty number word'")
        body.append("    one_ten = ', '.join('%d=%s' % (n, w) for n, w, tr in nums[:10])")
        body.append("    print('1-10: ' + one_ten)")
        body.append("    print('OK: %s verified %d number/time items' % (NAME, len(nums) + len(times)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def phrases(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("def main():")
        body.append("    items = DATA['items']")
        body.append("    print('%s: %d phrases' % (DATA['unit'], len(items)))")
        body.append("    assert len(items) == DATA['count'], 'count mismatch'")
        body.append("    assert all(len(x) == 4 and all(str(v).strip() for v in x) for x in items), 'bad phrase row'")
        body.append("    for w, tr, en, note in items[:4]: print('  %s (%s) - %s' % (w, tr, en))")
        body.append("    print('OK: %s verified %d phrases' % (NAME, len(items)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def grammar(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("def main():")
        body.append("    rules = DATA['rules']")
        body.append("    print('Grammar rules: %d' % len(rules))")
        body.append("    assert len(rules) == DATA['count'], 'count mismatch'")
        body.append("    assert all(len(x) == 5 and x[0].strip() and x[2].strip() for x in rules), 'bad rule row'")
        body.append("    for r, e, w, tr, en in rules[:3]: print('  %s :: %s (%s)' % (r, w, en))")
        body.append("    print('OK: %s verified %d grammar rules' % (NAME, len(rules)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def sentences(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("def main():")
        body.append("    sents = DATA['sentences']")
        body.append("    print('Sentence set [%s]: %d sentences' % (DATA['theme'], len(sents)))")
        body.append("    assert len(sents) == DATA['count'], 'count mismatch'")
        body.append("    assert all(len(x) == 3 and all(str(v).strip() for v in x) for x in sents), 'bad sentence row'")
        body.append("    for a, b, c in sents[:3]: print('  %s (%s - %s)' % (a, b, c))")
        body.append("    print('OK: %s verified %d sentences' % (NAME, len(sents)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def tenses(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("def main():")
        body.append("    items = DATA['items']")
        body.append("    print('Tense drills: %d' % len(items))")
        body.append("    assert len(items) == DATA['count'], 'count mismatch'")
        body.append("    assert all(len(x) == 4 and x[0].strip() and x[1].strip() for x in items), 'bad tense row'")
        body.append("    labels = sorted(set(x[0] for x in items))")
        body.append("    print('Tenses covered: ' + ', '.join(labels))")
        body.append("    print('OK: %s verified %d tense sentences' % (NAME, len(items)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def qa(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("def main():")
        body.append("    items = DATA['items']")
        body.append("    print('Q&A pairs: %d' % len(items))")
        body.append("    assert len(items) == DATA['count'], 'count mismatch'")
        body.append("    assert all(len(x) == 6 and x[0].strip() and x[3].strip() for x in items), 'bad qa row'")
        body.append("    q, qtr, qen, a, atr, aen = items[0]")
        body.append("    print('  Q: %s (%s)' % (q, qen))")
        body.append("    print('  A: %s (%s)' % (a, aen))")
        body.append("    print('OK: %s verified %d Q&A pairs' % (NAME, len(items)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def commands(hdr, name, rid, group, data):
        return phrases(hdr, name, rid, group,
                       {"items": data["items"], "unit": "commands",
                        "count": data["count"]})

    def story(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("def main():")
        body.append("    lines = DATA['lines']")
        body.append("    print('Story: %s (%d lines)' % (DATA['title'], len(lines)))")
        body.append("    assert len(lines) == DATA['count'], 'count mismatch'")
        body.append("    assert all(len(x) == 3 and all(str(v).strip() for v in x) for x in lines), 'bad story row'")
        body.append("    words = sum(len(x[0].split()) for x in lines)")
        body.append("    print('  %d words of narrative' % words)")
        body.append("    a, b, c = lines[0]")
        body.append("    print('  Opens: %s (%s)' % (a, c))")
        body.append("    print('OK: %s verified %d story lines' % (NAME, len(lines)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def idioms(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("def main():")
        body.append("    items = DATA['items']")
        body.append("    print('Idioms: %d' % len(items))")
        body.append("    assert len(items) == DATA['count'], 'count mismatch'")
        body.append("    assert all(len(x) == 7 and x[0].strip() and x[3].strip() for x in items), 'bad idiom row'")
        body.append("    w, tr, lit, mean, ex, extr, exen = items[0]")
        body.append("    print('  %s (%s): %s' % (w, tr, mean))")
        body.append("    print('OK: %s verified %d idioms' % (NAME, len(items)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def registers(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("def main():")
        body.append("    items = DATA['items']")
        body.append("    print('Register pairs: %d' % len(items))")
        body.append("    assert len(items) == DATA['count'], 'count mismatch'")
        body.append("    assert all(len(x) == 7 and x[0].strip() and x[3].strip() for x in items), 'bad register row'")
        body.append("    iw, itr, ien, fw, ftr, fen, note = items[0]")
        body.append("    print('  informal: %s (%s)' % (iw, ien))")
        body.append("    print('  formal:   %s (%s)' % (fw, fen))")
        body.append("    print('OK: %s verified %d register pairs' % (NAME, len(items)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def dialogue(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("def main():")
        body.append("    lines = DATA['lines']")
        body.append("    print('Dialogue: %s (%d turns)' % (DATA['title'], len(lines)))")
        body.append("    assert len(lines) == DATA['count'], 'count mismatch'")
        body.append("    assert all(len(x) == 4 and x[0].strip() and x[1].strip() for x in lines), 'bad dialogue row'")
        body.append("    speakers = sorted(set(x[0] for x in lines))")
        body.append("    print('Speakers: ' + ', '.join(speakers))")
        body.append("    assert len(speakers) >= 2, 'dialogue needs 2+ speakers'")
        body.append("    print('OK: %s verified %d dialogue turns' % (NAME, len(lines)))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    def review(hdr, name, rid, group, data):
        body = []
        body.append("import json")
        body.append("NAME = %s" % json.dumps(name))
        body.append("DATA = json.loads(%s)" % json.dumps(_embed(data)))
        body.append("SEED = sum(ord(c) for c in NAME) % 100000")
        body.append("def main():")
        body.append("    pts, counts, sample = DATA['points'], DATA['counts'], DATA['sample_vocab']")
        body.append("    total = sum(counts.values())")
        body.append("    print('Mastery review: %d checkpoints, %d items under review' % (len(pts), total))")
        body.append("    assert len(pts) >= 8, 'need 8+ checkpoints'")
        body.append("    assert total > 200, 'review must cover 200+ items'")
        body.append("    a = SEED")
        body.append("    quiz = []")
        body.append("    for _ in range(5):")
        body.append("        a = (a * 1103515245 + 12345) % 2147483648")
        body.append("        quiz.append(sample[a % len(sample)])")
        body.append("    print('Self-test sample:')")
        body.append("    for w in quiz: print('  %s (%s) = %s' % (w[0], w[1], w[2]))")
        body.append("    print('OK: %s verified mastery over %d items' % (NAME, total))")
        body.append("if __name__ == '__main__': main()")
        return hdr(name, rid, group) + "\n".join(body) + "\n"

    table = {
        "facts": facts, "alphabet": alphabet, "phonology": phonology,
        "vocab": vocab, "adjvocab": adjvocab, "numbers": numbers,
        "phrases": phrases, "grammar": grammar, "sentences": sentences,
        "tenses": tenses, "qa": qa, "commands": commands, "story": story,
        "idioms": idioms, "registers": registers, "dialogue": dialogue,
        "review": review,
    }
    if kind not in table:
        raise KeyError("unknown demo kind: %s" % kind)
    return table[kind]


def standard_demos(entries):
    """Build the DEMOS dict expected by build.py from entries."""
    demos = {}
    for e in entries:
        demos[e["demo_key"]] = _demo_src(e["demo_kind"])
    return demos


# ---------------------------------------------------------------- screen

SCREEN_TERMS = [
    # hate / extremist / sexual / profane indicators (review every hit in context)
    "kill all", "death to", "exterminate", "supremacist", "jihad",
    "porn", "xxx", "erotic", "orgasm", "masturbat", "prostitut",
    "fuck", "shit", "bitch", "bastard", "whore", "slut", "cunt",
    "nigger", "faggot", "retard", "terrorist attack", "bomb making",
    "how to kill",
]

RELIGION_FRAMING = [
    "god commands you", "god says you must", "you must pray",
    "accept jesus", "convert to", "holy war", "divine punishment",
    "scripture says you must",
]


def screen_records(records):
    """Return [(rid, field, term, snippet)] hits for manual context review."""
    hits = []
    for r in records:
        blob_fields = {
            "description": r.get("description", ""),
            "how_it_works": r.get("how_it_works", ""),
            "key_points": " ".join(r.get("key_points", [])),
        }
        for field, text in blob_fields.items():
            low = text.lower()
            for term in SCREEN_TERMS + RELIGION_FRAMING:
                if term in low:
                    i = low.index(term)
                    hits.append((r["id"], field, term,
                                 text[max(0, i - 60):i + 60].replace("\n", " ")))
    return hits
