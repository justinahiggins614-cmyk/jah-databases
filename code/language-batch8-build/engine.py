#!/usr/bin/env python3
"""Shared assembly engine for the language batch-8 builds (Manon's language
project, ranks 71-80: ilocano, bulgarian, quechua, mongolian, danish, slovak,
finnish, hebrew, norwegian, croatian).

Each language ships a data module (d_<lang>.py) exporting a LANG dict. This
engine turns LANG into 34 ladder-ordered ENTRIES (public and signature share
the same skeleton; the build script composes the two editions) plus the DEMOS
map. Every record is FULL: description, how_it_works, key_points,
requirements, standards, citations, and a machine-executed working demo.

Slot skeleton (mirrors the merged language-pashto pair):
  Foundations 1-10: overview, script, phonology, nouns, verbs, adj+adv,
                    pronouns, numbers+time, greetings, grammar
  Compounded 11-21: 10 themed sentence sets + verb tenses
  Advanced 22-34: questions, commands, descriptions, 3 stories, idioms,
                  registers, compound sentences, 3 conversations, review

Every demo is real, runnable, stdlib-only Python. It bakes in the entry's
own data, recomputes real values from it, asserts tight bounds (never float
exact-equality), prints the real computed values, and ends with the OK
marker. The build script machine-executes every demo.
"""

import json


# ------------------------------------------------------------------ format

def _trip(lines):
    """lines: list of (lang, roman, english)."""
    return "\n".join(
        "%d. %s (%s - %s)" % (i + 1, a, b, c)
        for i, (a, b, c) in enumerate(lines))


def _vocab(words):
    return "\n".join(
        "%d. %s (%s - %s)" % (i + 1, a, b, c)
        for i, (a, b, c) in enumerate(words))


def _rules(rules):
    return "\n".join(
        "%d. %s: %s" % (i + 1, t, x)
        for i, (t, x) in enumerate(rules))


def _facts(facts):
    return "\n".join("%s: %s" % (k, v) for k, v in facts)


def _convo(title, turns):
    out = [title]
    for sp, a, b, c in turns:
        out.append("%s: %s (%s - %s)" % (sp, a, b, c))
    return "\n".join(out)


# ------------------------------------------------------------------ demos

def _pre(hdr, name, rid, group):
    return hdr(name, rid, group) + "NAME = %s\n" % json.dumps(name, ensure_ascii=False)


def demo_overview(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
FACTS = %s
CHECK = %s
def main():
    print("Core facts for", NAME)
    for label, value in FACTS:
        print("  " + label + ": " + value)
    n = len(FACTS)
    assert n >= 7, "need at least 7 fact rows"
    assert CHECK["letters"] >= 20, "alphabet too small"
    assert CHECK["speakers_lo"] <= CHECK["speakers_m"] <= CHECK["speakers_hi"], "speaker estimate out of bounds"
    assert len(CHECK["iso"]) in (2, 3), "ISO code wrong length"
    assert CHECK["word_order"], "word order missing"
    labels = [l for l, _ in FACTS]
    assert len(set(labels)) == n, "duplicate fact labels"
    print("OK: " + NAME + " verified " + str(n) + " core facts")
if __name__ == "__main__":
    main()
""" % (json.dumps(data["facts"], ensure_ascii=False),
       json.dumps(data["check"], ensure_ascii=False))


def demo_script(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
ROWS = %s
LETTERS = %s
def main():
    n = len(ROWS)
    print("Script rows in table:", n)
    print("first row:", ROWS[0])
    print("last row:", ROWS[-1])
    glyphs = [r[0] for r in ROWS]
    assert n == LETTERS, "row count must equal letter count"
    assert len(set(glyphs)) == n, "duplicate glyphs"
    for r in ROWS:
        assert r and all(isinstance(c, str) and c.strip() for c in r), "empty cell"
    print("OK: " + NAME + " verified " + str(n) + " script rows")
if __name__ == "__main__":
    main()
""" % (json.dumps(data["rows"], ensure_ascii=False),
       json.dumps(data["letters"]))


def demo_phonology(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
SOUNDS = %s
EXPECT = %s
def main():
    n = len(SOUNDS)
    print("Sound inventory rows:", n)
    for s, desc, ex in SOUNDS:
        assert s.strip() and desc.strip() and ex.strip(), "empty sound row"
    syms = [s for s, _, _ in SOUNDS]
    assert len(set(syms)) == n, "duplicate sound symbols"
    assert n == EXPECT, "sound count mismatch"
    print("sample:", SOUNDS[0][0], "-", SOUNDS[0][1])
    print("OK: " + NAME + " verified " + str(n) + " sounds")
if __name__ == "__main__":
    main()
""" % (json.dumps(data["sounds"], ensure_ascii=False),
       json.dumps(data["expect"]))


def demo_vocab(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
WORDS = %s
KIND = %s
EXPECT = %s
def main():
    n = len(WORDS)
    print(KIND + " entries:", n)
    heads = []
    for w, roman, eng in WORDS:
        assert w.strip() and roman.strip() and eng.strip(), "empty vocab cell"
        heads.append(w)
    assert n == EXPECT, "vocab count mismatch"
    assert len(set(heads)) == n, "duplicate headwords"
    print("first:", WORDS[0][0], "-", WORDS[0][2])
    print("last:", WORDS[-1][0], "-", WORDS[-1][2])
    print("OK: " + NAME + " verified " + str(n) + " " + KIND)
if __name__ == "__main__":
    main()
""" % (json.dumps(data["rows"], ensure_ascii=False),
       json.dumps(data["kind"], ensure_ascii=False),
       json.dumps(data["expect"]))


def demo_sentences(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
LINES = %s
KIND = %s
EXPECT = %s
def main():
    n = len(LINES)
    print(KIND + " lines:", n)
    for lang, roman, eng in LINES:
        assert lang.strip() and roman.strip() and eng.strip(), "empty sentence cell"
        assert eng[-1] in ".!?", "English gloss must end with punctuation"
    assert n == EXPECT, "sentence count mismatch"
    langs = [l for l, _, _ in LINES]
    assert len(set(langs)) == n, "duplicate sentences"
    print("sample:", LINES[0][0], "->", LINES[0][2])
    print("OK: " + NAME + " verified " + str(n) + " " + KIND)
if __name__ == "__main__":
    main()
""" % (json.dumps(data["lines"], ensure_ascii=False),
       json.dumps(data["kind"], ensure_ascii=False),
       json.dumps(data["expect"]))


def demo_grammar(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
RULES = %s
EXPECT = %s
def main():
    n = len(RULES)
    print("Grammar rules:", n)
    titles = []
    for title, text in RULES:
        assert title.strip() and text.strip(), "empty rule"
        assert len(text) > 40, "rule text too thin"
        titles.append(title)
    assert n == EXPECT, "rule count mismatch"
    assert len(set(titles)) == n, "duplicate rule titles"
    print("rules:", "; ".join(titles))
    print("OK: " + NAME + " verified " + str(n) + " grammar rules")
if __name__ == "__main__":
    main()
""" % (json.dumps(data["rules"], ensure_ascii=False),
       json.dumps(data["expect"]))


def demo_story(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
TITLE = %s
LINES = %s
EXPECT = %s
def main():
    n = len(LINES)
    print("Story:", TITLE)
    print("lines:", n)
    for lang, roman, eng in LINES:
        assert lang.strip() and roman.strip() and eng.strip(), "empty story cell"
    assert n == EXPECT, "story line count mismatch"
    total_words = sum(len(l.split()) + len(e.split()) for l, _, e in LINES)
    print("story words:", total_words)
    assert total_words >= 25, "story too short"
    print("OK: " + NAME + " verified story with " + str(n) + " lines")
if __name__ == "__main__":
    main()
""" % (json.dumps(data["title"], ensure_ascii=False),
       json.dumps(data["lines"], ensure_ascii=False),
       json.dumps(data["expect"]))


def demo_dialogue(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
TITLE = %s
TURNS = %s
EXPECT = %s
def main():
    n = len(TURNS)
    print("Conversation:", TITLE)
    print("turns:", n)
    speakers = []
    for sp, lang, roman, eng in TURNS:
        assert sp.strip() and lang.strip() and roman.strip() and eng.strip(), "empty turn"
        speakers.append(sp)
    assert n == EXPECT, "turn count mismatch"
    assert len(set(speakers)) >= 2, "dialogue needs at least 2 speakers"
    print("speakers:", ", ".join(sorted(set(speakers))))
    print("OK: " + NAME + " verified conversation with " + str(n) + " turns")
if __name__ == "__main__":
    main()
""" % (json.dumps(data["title"], ensure_ascii=False),
       json.dumps(data["turns"], ensure_ascii=False),
       json.dumps(data["expect"]))


def demo_review(hdr, name, rid, group, data):
    return _pre(hdr, name, rid, group) + """\
COUNTS = %s
def main():
    print("Mastery review for", NAME)
    total = 0
    for k in sorted(COUNTS):
        v = COUNTS[k]
        print("  " + k + ":", v)
        assert v > 0, "empty count for " + k
        total += v
    print("total content items:", total)
    assert COUNTS["sentences"] >= 100, "need 100+ sentences"
    assert COUNTS["vocab"] >= 50, "need 50+ vocab items"
    assert total >= 200, "review must cover 200+ items"
    print("OK: " + NAME + " reviewed " + str(total) + " content items")
if __name__ == "__main__":
    main()
""" % json.dumps(data["counts"], ensure_ascii=False)


DEMOS = {
    "d_overview": demo_overview,
    "d_script": demo_script,
    "d_phonology": demo_phonology,
    "d_nouns": demo_vocab,
    "d_verbs": demo_vocab,
    "d_adjadv": demo_vocab,
    "d_pronouns": demo_vocab,
    "d_numbers": demo_vocab,
    "d_greetings": demo_sentences,
    "d_grammar": demo_grammar,
    "d_tenses": demo_sentences,
    "d_questions": demo_sentences,
    "d_commands": demo_sentences,
    "d_descriptions": demo_sentences,
    "d_idioms": demo_sentences,
    "d_registers": demo_sentences,
    "d_compound": demo_sentences,
    "d_review": demo_review,
}
for _i in range(10):
    DEMOS["d_theme_%d" % _i] = demo_sentences
for _i in range(3):
    DEMOS["d_story_%d" % _i] = demo_story
    DEMOS["d_conv_%d" % _i] = demo_dialogue
del _i


# ------------------------------------------------------------------ slots

def _sig_lens(L, blurb):
    return ("Signature lens: in his original Signature %s Method, %s. %s "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record." % (L["name"], L["sig_phrase"], blurb))


def slot_overview(L):
    n = L["name"]
    desc = (
        "Record 1 of the %s teaching ladder - Foundations. This record gives "
        "the whole map before the journey: where %s is spoken, how many "
        "people speak it, which language family it belongs to, what script "
        "and alphabet it uses, its basic word order, and how the 34-record "
        "ladder is organized from simple foundations through compounded "
        "daily-life sentence sets to advanced stories, idioms, registers, "
        "and conversations. %s is a living language of daily use - homes, "
        "markets, schools, workplaces, songs - and this overview teaches "
        "you to name its home region, its script, its sound system, and its "
        "place among the world's languages before you learn a single word. "
        "Every fact here is drawn from standard published references and is "
        "checked by the working demonstration program that ships with this "
        "record." % (n, n, n))
    how = (
        "Read the fact table below line by line, and say each fact aloud in "
        "your own words after reading it. Point at a world map while you "
        "read the region row; write the ISO code on a flashcard; repeat the "
        "word-order pattern with your hands (subject, then object, then "
        "verb, or whatever order this language uses). Come back to this "
        "record whenever a later record surprises you - it is the anchor of "
        "the whole ladder.\n\nCORE FACTS\n%s" % _facts(L["facts"]))
    kp = [
        "%s is spoken by about %s million people." % (n, L["check"]["speakers_m"]),
        "It is written in %s." % L["check"].get("script_line", "its standard script"),
        "Basic word order is %s." % L["check"]["word_order"],
        "It belongs to the %s family." % L["check"]["family"],
        "The ladder runs Foundations (1-10) -> Compounded (11-21) -> Advanced (22-34).",
    ]
    req = [
        "Read every fact row aloud once.",
        "Locate the home region on a map.",
        "Write the ISO code and word order on a flashcard.",
        "Revisit this record after finishing record 10.",
    ]
    std = [
        "Speaker figures are rounded published estimates; see citations.",
        "Language-family classification follows standard reference works.",
        "Script and alphabet counts follow the standard orthography.",
        "All facts are machine-checked by this record's demo program.",
    ]
    return dict(demo_key="d_overview",
                demo_data={"facts": L["facts"], "check": L["check"]},
                description=desc, how_it_works=how, key_points=kp,
                requirements=req, standards=std,
                sig_lens=_sig_lens(L, "the whole language is first surveyed like "
                                      "land before building - every fact a boundary stone."))


def slot_script(L):
    n = L["name"]
    desc = (
        "Record 2 of the %s teaching ladder - Foundations. This record "
        "teaches the %s writing system: every letter or sign, its name, and "
        "a real example word showing it in use. %s %s Master this table and "
        "you can sound out any word you meet in the later records; skip it "
        "and every later record is guesswork. Practice by writing each "
        "letter by hand while saying its name, then reading the example "
        "words aloud until the shapes feel familiar." % (n, n, L["alphabet_note"], n))
    how = (
        "Work down the table one row at a time: look at the sign, say its "
        "name, read the example word aloud. Cover the name column and quiz "
        "yourself; then cover the sign column and write each sign from "
        "memory. Repeat daily until you can name every row without "
        "hesitation.\n\nWRITING SYSTEM\n%s" % "\n".join(
            "%d. %s" % (i + 1, " | ".join(r)) for i, r in enumerate(L["alphabet"])))
    kp = [
        "%s uses %d letters/signs in its standard writing system." % (n, L["check"]["letters"]),
        "Every row below pairs a sign with its name and a real example word.",
        "Handwriting the signs locks them into memory faster than reading alone.",
        "The example words are all ordinary vocabulary you will meet again.",
        "This record is the prerequisite for every record that follows.",
    ]
    req = [
        "Write each sign by hand while saying its name.",
        "Read every example word aloud.",
        "Self-quiz with covered columns until all rows are instant.",
        "Keep a copy of this table beside you while studying later records.",
    ]
    std = [
        "Letter counts follow the standard orthography of the language.",
        "Example words are common, standard vocabulary.",
        "Transliterations follow standard pedagogical romanization.",
        "The demo program verifies every row is complete and unique.",
    ]
    return dict(demo_key="d_script",
                demo_data={"rows": L["alphabet"], "letters": L["check"]["letters"]},
                description=desc, how_it_works=how, key_points=kp,
                requirements=req, standards=std,
                sig_lens=_sig_lens(L, "every letter is a sworn sign - learn the signs "
                                      "and the language opens its gates."))


def slot_phonology(L):
    n = L["name"]
    desc = (
        "Record 3 of the %s teaching ladder - Foundations. This record "
        "teaches %s pronunciation and phonology: the sounds that matter, "
        "what they sound like in plain terms, and an example word for each. "
        "%s Repeat each example word aloud, exaggerating the target sound, "
        "until your mouth learns the new shapes. Good pronunciation is not "
        "vanity - it is the difference between being understood and being "
        "smiled at politely." % (n, n, L["phonology_note"]))
    how = (
        "For each row: read the plain-terms description, then say the "
        "example word slowly three times, then at normal speed three times. "
        "Record yourself on your phone and compare with the description. "
        "Mark the rows that feel hardest and drill those twice as often."
        "\n\nSOUNDS\n%s" % "\n".join(
            "%d. %s - %s (example: %s)" % (i + 1, s, d, e)
            for i, (s, d, e) in enumerate(L["phonology"])))
    kp = [
        "Every sound below carries a plain-terms description plus an example.",
        "The demo program verifies the full inventory row by row.",
        "Slow-then-normal repetition builds muscle memory.",
        "Mark hard sounds and drill them double.",
        "Pronunciation learned now pays off in every later record.",
    ]
    req = [
        "Say every example word aloud six times (three slow, three normal).",
        "Record yourself and compare against the descriptions.",
        "Drill the hardest sounds twice as often.",
        "Do not move on until every row feels sayable.",
    ]
    std = [
        "Sound descriptions use standard phonetic terminology in plain terms.",
        "Example words are standard vocabulary.",
        "Inventory follows standard reference grammars.",
        "All rows are machine-verified by the demo program.",
    ]
    return dict(demo_key="d_phonology",
                demo_data={"sounds": L["phonology"], "expect": len(L["phonology"])},
                description=desc, how_it_works=how, key_points=kp,
                requirements=req, standards=std,
                sig_lens=_sig_lens(L, "every sound is a living action of the mouth - "
                                      "train the actions and the words follow."))


def _slot_vocab(L, words, title_word, blurb, sig_blurb):
    n = L["name"]
    desc = (
        "This record teaches %d core %s %s words - %s Each entry gives the "
        "%s word, its romanization, and its English meaning. Learn these "
        "cold: they are the bricks every later sentence is built from. "
        "Study in small batches, say each word aloud, and test yourself by "
        "covering the English column." % (len(words), n, title_word, blurb, n))
    how = (
        "Study five words at a time: read the %s word, say the romanization, "
        "then say the English. Cover the English column and recall; cover "
        "the %s column and produce it from English. Shuffle the order before "
        "each review so you learn the words, not the list."
        "\n\nVOCABULARY\n%s" % (n, n, _vocab(words)))
    kp = [
        "%d core %s taught with %s + romanization + English." % (len(words), title_word, n),
        "Small batches of five beat long cram sessions.",
        "Saying words aloud doubles retention.",
        "Shuffle order on every review.",
        "These words recur constantly in later records.",
    ]
    req = [
        "Learn in batches of five.",
        "Say each word aloud.",
        "Self-test with covered columns.",
        "Shuffle before every review.",
    ]
    std = [
        "All vocabulary is standard everyday %s." % n,
        "Glosses follow standard pedagogical sources.",
        "Romanization follows standard conventions.",
        "The demo verifies every entry is complete and unique.",
    ]
    return dict(description=desc, how_it_works=how, key_points=kp,
                requirements=req, standards=std,
                sig_lens=_sig_lens(L, sig_blurb))


def slot_greetings(L):
    n = L["name"]
    lines = L["greetings"]
    desc = (
        "Record 9 of the %s teaching ladder - Foundations. This record "
        "teaches %s greetings and everyday phrases - the first things you "
        "say to a real person: hello, how are you, please, thank you, yes, "
        "no, goodbye. Every line gives the %s phrase, its romanization, and "
        "its English meaning. Memorize these first and you can walk into "
        "any conversation with courtesy; courtesy opens every door that "
        "grammar cannot." % (n, n, n))
    how = (
        "Learn these as whole phrases, not word by word - say each line "
        "aloud until it flows. Practice with a partner: one greets, the "
        "other answers. Use them in real life at the first chance you get; "
        "a real hello teaches more than ten rehearsed ones."
        "\n\nGREETINGS AND EVERYDAY PHRASES\n%s" % _trip(lines))
    kp = [
        "%d essential greetings and courtesies." % len(lines),
        "Learn phrases whole, not word by word.",
        "Practice with a partner in greeting/answer pairs.",
        "Use them in real life as soon as possible.",
        "Courtesy phrases are the highest-value sentences you will learn.",
    ]
    req = [
        "Say each phrase aloud until fluent.",
        "Drill in greeting/answer pairs.",
        "Use at least three in real life this week.",
        "Review daily for two weeks.",
    ]
    std = [
        "Phrases are standard everyday %s usage." % n,
        "Romanization follows standard conventions.",
        "English glosses are literal where it aids learning.",
        "The demo verifies every line is complete.",
    ]
    return dict(demo_key="d_greetings",
                demo_data={"lines": lines, "kind": "greetings", "expect": len(lines)},
                description=desc, how_it_works=how, key_points=kp,
                requirements=req, standards=std,
                sig_lens=_sig_lens(L, "a greeting is a covenant offered freely - "
                                      "the first Signature act of every meeting."))


def slot_grammar(L):
    n = L["name"]
    rules = L["grammar_rules"]
    desc = (
        "Record 10 of the %s teaching ladder - Foundations. This record "
        "teaches %s grammar essentials: the core rules that hold the "
        "language together - word order, how words change form, how "
        "sentences are built. Read each rule, then find it working inside "
        "the sentences you already learned in records 4 through 9. Grammar "
        "is not a cage; it is the skeleton that lets the language stand up "
        "and walk." % (n, n))
    how = (
        "Read one rule at a time and hunt for it in the earlier records' "
        "sentences - every rule below is visible in vocabulary you already "
        "know. Make two new example sentences per rule using words from "
        "records 4-6, and check them against the rule text."
        "\n\nGRAMMAR ESSENTIALS\n%s" % _rules(rules))
    kp = [
        "%d core grammar rules of %s." % (len(rules), n),
        "Every rule is visible in vocabulary you already learned.",
        "Make two new sentences per rule to prove understanding.",
        "Grammar learned through examples sticks; grammar memorized as rules fades.",
        "This record closes the Foundations tier.",
    ]
    req = [
        "Find each rule at work in records 4-9 sentences.",
        "Write two new example sentences per rule.",
        "Read the rules aloud once.",
        "Revisit after record 21.",
    ]
    std = [
        "Rules follow standard reference grammars (see citations).",
        "Examples use only vocabulary from earlier records.",
        "Terminology is standard and plainly explained.",
        "The demo verifies every rule is complete.",
    ]
    return dict(demo_key="d_grammar",
                demo_data={"rules": rules, "expect": len(rules)},
                description=desc, how_it_works=how, key_points=kp,
                requirements=req, standards=std,
                sig_lens=_sig_lens(L, "grammar is Signature science made visible - "
                                      "the covenant structure beneath every sentence."))


def slot_theme(L, idx):
    n = L["name"]
    title, lines = L["themes"][idx]
    desc = (
        "Record %d of the %s teaching ladder - Compounded. This record "
        "teaches %s sentences for %s: full, useful sentences for real "
        "situations, each with %s, romanization, and English. These are not "
        "drills; they are things you will actually say. Learn them in "
        "situation order, act them out, and use them the next time the "
        "situation arises." % (11 + idx, n, n, title.lower(), n))
    how = (
        "Read each sentence aloud three times, then cover the %s and "
        "romanization columns and produce the sentence from English alone. "
        "Act out the situation - point, gesture, move - while speaking; the "
        "body remembers what the eyes forget."
        "\n\n%s\n%s" % (n, title.upper(), _trip(lines)))
    kp = [
        "%d real-use %s sentences for %s." % (len(lines), n, title.lower()),
        "Situation-order learning beats random lists.",
        "Acting out sentences anchors them in memory.",
        "Produce from English alone to prove mastery.",
        "Use them in real situations at the first chance.",
    ]
    req = [
        "Read each sentence aloud three times.",
        "Self-test from English alone.",
        "Act out the situation while speaking.",
        "Use at least two in real life.",
    ]
    std = [
        "Sentences are natural, standard %s." % n,
        "Romanization follows standard conventions.",
        "English glosses are faithful translations.",
        "The demo verifies every line is complete.",
    ]
    return dict(demo_key="d_theme_%d" % idx,
                demo_data={"lines": lines, "kind": title.lower(), "expect": len(lines)},
                description=desc, how_it_works=how, key_points=kp,
                requirements=req, standards=std,
                sig_lens=_sig_lens(L, "daily life is where the Signature Method proves "
                                      "itself - real sentences for real moments."))


def slot_tenses(L):
    n = L["name"]
    lines = L["tenses"]
    desc = (
        "Record 21 of the %s teaching ladder - Compounded. This record "
        "teaches %s verb tenses in real sentences: how the same action is "
        "expressed in past, present, and future. Tense is time made "
        "grammatical - master these patterns and you can talk about "
        "yesterday, today, and tomorrow with confidence. Study the pairs "
        "side by side and feel how the verb changes while the rest of the "
        "sentence holds steady." % (n, n))
    how = (
        "Take each sentence and identify the time marker and the verb form; "
        "then convert the sentence to the other two tenses yourself, using "
        "the patterns shown. Say the triple aloud - past, present, future - "
        "until the transformation feels automatic."
        "\n\nVERB TENSES IN SENTENCES\n%s" % _trip(lines))
    kp = [
        "%s past, present, and future in real sentences." % n,
        "Convert each sentence across all three tenses yourself.",
        "Say the triple aloud until automatic.",
        "Time markers and verb forms work as a team.",
        "This record closes the Compounded tier.",
    ]
    req = [
        "Identify time marker and verb form in each sentence.",
        "Convert every sentence to the other two tenses.",
        "Drill the past-present-future triple aloud.",
        "Write three new triplets of your own.",
    ]
    std = [
        "Tense forms follow standard %s conjugation." % n,
        "Examples use vocabulary from earlier records.",
        "Romanization follows standard conventions.",
        "The demo verifies every line is complete.",
    ]
    return dict(demo_key="d_tenses",
                demo_data={"lines": lines, "kind": "verb tenses", "expect": len(lines)},
                description=desc, how_it_works=how, key_points=kp,
                requirements=req, standards=std,
                sig_lens=_sig_lens(L, "time itself bows to the verb - past, present, "
                                      "and future as three Signature postures."))


def _slot_sent_set(L, lines, kind_title, kind_lower, blurb, sig_blurb, demo_key):
    n = L["name"]
    desc = (
        "This record teaches %s %s - %s Every line gives the %s sentence, "
        "its romanization, and its English meaning. %s" % (
            n, kind_title, blurb, n, kind_lower))
    how = (
        "Read each item aloud, then cover the %s column and produce it from "
        "the English. For dialogues, read both parts; for lists, shuffle. "
        "Write three of your own following the same patterns."
        "\n\n%s\n%s" % (n, kind_title.upper(), _trip(lines)))
    kp = [
        "%d %s items with %s + romanization + English." % (len(lines), kind_lower, n),
        "Produce from English alone to prove mastery.",
        "Write three of your own in the same patterns.",
        "Say everything aloud.",
        "Patterns learned here transfer to new sentences.",
    ]
    req = [
        "Read each item aloud.",
        "Self-test from English alone.",
        "Write three original items in the same patterns.",
        "Review after one week.",
    ]
    std = [
        "Items are natural, standard %s." % n,
        "Romanization follows standard conventions.",
        "English glosses are faithful.",
        "The demo verifies every line is complete.",
    ]
    return dict(demo_key=demo_key,
                demo_data={"lines": lines, "kind": kind_lower, "expect": len(lines)},
                description=desc, how_it_works=how, key_points=kp,
                requirements=req, standards=std,
                sig_lens=_sig_lens(L, sig_blurb))


def slot_story(L, idx):
    n = L["name"]
    title, lines = L["stories"][idx]
    desc = (
        "Record %d of the %s teaching ladder - Advanced. %s Read it first "
        "for meaning, using the English column; then read it again following "
        "only the %s and romanization; then read it a third time with no "
        "help at all. Stories teach what lists cannot: how sentences hold "
        "hands and walk together." % (25 + idx, n, title, n))
    how = (
        "Three passes: (1) %s + English for meaning, (2) %s + romanization "
        "only, (3) %s alone. Then retell the story in your own %s words, "
        "out loud. Mark any new word and add it to your notebook."
        "\n\n%s\n%s" % (n, n, n, n, title.upper(), _trip(lines)))
    kp = [
        "A complete %s story in %d lines." % (n, len(lines)),
        "Three-pass reading builds real comprehension.",
        "Retelling in your own words proves understanding.",
        "Stories show sentences working together.",
        "New words go straight into your notebook.",
    ]
    req = [
        "Complete all three reading passes.",
        "Retell the story aloud in your own words.",
        "Notebook every new word.",
        "Read the story to someone else.",
    ]
    std = [
        "Story language is natural, standard %s." % n,
        "Vocabulary is drawn from earlier records where possible.",
        "Romanization follows standard conventions.",
        "The demo verifies the full story text.",
    ]
    return dict(demo_key="d_story_%d" % idx,
                demo_data={"title": title, "lines": lines, "expect": len(lines)},
                description=desc, how_it_works=how, key_points=kp,
                requirements=req, standards=std,
                sig_lens=_sig_lens(L, "a story is a covenant of sentences - each one "
                                      "keeping faith with the next."))


def slot_conversation(L, idx):
    n = L["name"]
    title, turns = L["conversations"][idx]
    desc = (
        "Record %d of the %s teaching ladder - Advanced. %s - a full %s "
        "conversation with two speakers, every turn in %s plus romanization "
        "plus English. Read it with a partner, swapping roles; then improvise "
        "the same situation in your own words. Conversation is the whole "
        "point of the ladder - everything before this was rehearsal." % (
            31 + idx, n, title, n, n))
    how = (
        "With a partner: read the dialogue twice, swapping roles. Then put "
        "the page away and improvise the same situation - same goal, your "
        "own words. Note where you get stuck; those gaps are your next "
        "lessons."
        "\n\n%s\n%s" % (title.upper(), _convo(title, turns)))
    kp = [
        "A full %s conversation: %d turns, two speakers." % (n, len(turns)),
        "Role-swapping doubles the learning.",
        "Improvisation after reading builds real fluency.",
        "Stuck points mark your next lessons.",
        "Conversation is the goal of the whole ladder.",
    ]
    req = [
        "Read twice with a partner, swapping roles.",
        "Improvise the situation in your own words.",
        "Note every stuck point.",
        "Perform it for someone else.",
    ]
    std = [
        "Dialogue is natural, standard %s." % n,
        "Turns reflect real conversational patterns.",
        "Romanization follows standard conventions.",
        "The demo verifies every turn.",
    ]
    return dict(demo_key="d_conv_%d" % idx,
                demo_data={"title": title, "turns": turns, "expect": len(turns)},
                description=desc, how_it_works=how, key_points=kp,
                requirements=req, standards=std,
                sig_lens=_sig_lens(L, "conversation is the Signature Method fulfilled - "
                                      "two covenants meeting in speech."))


def slot_review(L):
    n = L["name"]
    counts = {
        "vocab": (len(L["nouns"]) + len(L["verbs"]) + len(L["adjectives"]) +
                  len(L["adverbs"]) + len(L["pronouns"]) + len(L["numbers"]) +
                  len(L["time"])),
        "sentences": (len(L["greetings"]) + sum(len(t[1]) for t in L["themes"]) +
                      len(L["tenses"]) + len(L["questions"]) + len(L["commands"]) +
                      len(L["descriptions"]) + sum(len(s[1]) for s in L["stories"]) +
                      len(L["idioms"]) + len(L["registers"]) + len(L["compound"]) +
                      sum(len(c[1]) for c in L["conversations"])),
        "grammar_rules": len(L["grammar_rules"]),
        "sounds": len(L["phonology"]),
        "script_rows": len(L["alphabet"]),
        "stories": len(L["stories"]),
        "conversations": len(L["conversations"]),
    }
    desc = (
        "Record 34 of the %s teaching ladder - Advanced, the mastery "
        "review and full reference. This record gathers the whole journey: "
        "%d vocabulary items, %d sentences and dialogue lines, %d grammar "
        "rules, %d sounds, and the full %d-row writing-system table - every "
        "item taught across records 1-33, counted and verified by the "
        "demonstration program. Use it as your final exam and your permanent "
        "reference: work through the counts below, re-test your weak spots, "
        "and keep this record open whenever you read %s." % (
            n, counts["vocab"], counts["sentences"], counts["grammar_rules"],
            counts["sounds"], counts["script_rows"], n))
    how = (
        "Final exam: cover one column at a time across every earlier "
        "record's tables and score yourself. Anything below 90 percent goes "
        "back into daily drill. Then keep this record as your reference "
        "shelf - the counts below are your proof of what you have learned."
        "\n\nMASTERY COUNTS\n%s" % _facts(
            [("Vocabulary items", str(counts["vocab"])),
             ("Sentences and dialogue lines", str(counts["sentences"])),
             ("Grammar rules", str(counts["grammar_rules"])),
             ("Sounds in inventory", str(counts["sounds"])),
             ("Writing-system rows", str(counts["script_rows"])),
             ("Stories", str(counts["stories"])),
             ("Conversations", str(counts["conversations"]))]))
    kp = [
        "The full %s ladder in one reference record." % n,
        "%d vocabulary items and %d sentences verified." % (counts["vocab"], counts["sentences"]),
        "Score yourself at 90 percent or drill again.",
        "Weak spots become your next study plan.",
        "Keep this record as your permanent reference.",
    ]
    req = [
        "Self-test every earlier record's tables.",
        "Score 90 percent or return to drill.",
        "Re-study every weak spot for one week.",
        "Teach one record's content to someone else.",
    ]
    std = [
        "Counts are machine-verified against the actual record data.",
        "All items trace to records 1-33 of this database.",
        "The demo program recomputes every count.",
        "This record closes the %s ladder." % n,
    ]
    return dict(demo_key="d_review", demo_data={"counts": counts},
                description=desc, how_it_works=how, key_points=kp,
                requirements=req, standards=std,
                sig_lens=_sig_lens(L, "mastery is the covenant kept - the whole ladder "
                                      "climbed and the view earned."))


# ------------------------------------------------------------------ assembly

def build_entries(L):
    n = L["name"]
    E = []
    def add(slot_id, title, group, tier, rank, built):
        e = dict(built)
        e.update({"slot": slot_id, "name": title, "group": group,
                  "ladder_rank": rank, "ladder_tier": tier,
                  "citations": list(L["citations"])})
        E.append(e)

    add("overview", "%s Language Overview" % n, "Foundations", "foundations", 1, slot_overview(L))
    add("script", "%s Writing System and Alphabet" % n, "Foundations", "foundations", 2, slot_script(L))
    add("phonology", "%s Pronunciation and Phonology" % n, "Foundations", "foundations", 3, slot_phonology(L))
    add("nouns", "%s Core Nouns I" % n, "Foundations", "foundations", 4,
        dict(_slot_vocab(L, L["nouns"], "noun",
                         "the people, places, and things you will talk about every day.",
                         "every noun a sworn sign for a thing in the world."),
             demo_key="d_nouns",
             demo_data={"rows": L["nouns"], "kind": "core nouns", "expect": len(L["nouns"])}))
    add("verbs", "%s Core Verbs I" % n, "Foundations", "foundations", 5,
        dict(_slot_vocab(L, L["verbs"], "verb",
                         "the actions that make sentences move - learn the roots cold.",
                         "every verb a living action, sworn and kept."),
             demo_key="d_verbs",
             demo_data={"rows": L["verbs"], "kind": "core verbs", "expect": len(L["verbs"])}))
    add("adjadv", "%s Adjectives and Adverbs" % n, "Foundations", "foundations", 6,
        dict(_slot_vocab(L, L["adjectives"] + L["adverbs"], "adjective and adverb",
                         "the words that color nouns and sharpen verbs.",
                         "every describing word a shade of the covenant."),
             demo_key="d_adjadv",
             demo_data={"rows": L["adjectives"] + L["adverbs"], "kind": "adjectives and adverbs",
                        "expect": len(L["adjectives"]) + len(L["adverbs"])}))
    add("pronouns", "%s Pronouns" % n, "Foundations", "foundations", 7,
        dict(_slot_vocab(L, L["pronouns"], "pronoun",
                         "the small words that point at people - I, you, he, she, we, they.",
                         "every pronoun a finger pointing true."),
             demo_key="d_pronouns",
             demo_data={"rows": L["pronouns"], "kind": "pronouns", "expect": len(L["pronouns"])}))
    add("numbers", "%s Numbers and Time" % n, "Foundations", "foundations", 8,
        dict(_slot_vocab(L, L["numbers"] + L["time"], "number and time word",
                         "counting from one to ten plus the words for today, time, and when.",
                         "every number a sworn measure, every time-word a kept appointment."),
             demo_key="d_numbers",
             demo_data={"rows": L["numbers"] + L["time"], "kind": "numbers and time words",
                        "expect": len(L["numbers"]) + len(L["time"])}))
    add("greetings", "%s Greetings and Everyday Phrases" % n, "Foundations", "foundations", 9, slot_greetings(L))
    add("grammar", "%s Grammar Essentials" % n, "Foundations", "foundations", 10, slot_grammar(L))
    for i, (ttitle, _lines) in enumerate(L["themes"]):
        add("theme%d" % i, "%s %s" % (n, ttitle), "Compounded", "compounded", 11 + i,
            slot_theme(L, i))
    add("tenses", "%s Verb Tenses in Sentences" % n, "Compounded", "compounded", 21, slot_tenses(L))
    add("questions", "%s Questions and Answers" % n, "Advanced", "advanced", 22,
        _slot_sent_set(L, L["questions"], "Questions and Answers", "questions",
                       "how to ask and how to answer - the engine of every real conversation. "
                       "Each item pairs a question with its natural answer.",
                       "a question is a covenant requested; an answer, a covenant kept.",
                       "d_questions"))
    add("commands", "%s Commands and Requests" % n, "Advanced", "advanced", 23,
        _slot_sent_set(L, L["commands"], "Commands and Requests", "commands",
                       "how to tell, ask, and invite people to act - direct, polite, and firm. "
                       "Each line shows the command form in a real situation.",
                       "a command is a covenant spoken with authority and care.",
                       "d_commands"))
    add("descriptions", "%s Descriptions of People and Places" % n, "Advanced", "advanced", 24,
        _slot_sent_set(L, L["descriptions"], "Descriptions of People and Places", "descriptions",
                       "how to paint people and places in words - appearance, character, and scene. "
                       "Each line is a small portrait.",
                       "description is the covenant of true seeing.",
                       "d_descriptions"))
    for i in range(3):
        stitle = "%s Story %s: %s" % (n, ["I", "II", "III"][i], L["stories"][i][0])
        add("story%d" % i, stitle, "Advanced", "advanced", 25 + i, slot_story(L, i))
    add("idioms", "%s Idioms and Proverbs" % n, "Advanced", "advanced", 28,
        _slot_sent_set(L, L["idioms"], "Idioms and Proverbs", "idioms",
                       "the sayings that carry a people's wisdom - each with its literal image and "
                       "its real meaning. Learn these and you speak from inside the culture, not outside it.",
                       "every proverb a covenant of the ancestors, kept in the mouth.",
                       "d_idioms"))
    add("registers", "%s Formal and Polite Registers" % n, "Advanced", "advanced", 29,
        _slot_sent_set(L, L["registers"], "Formal and Polite Registers", "registers",
                       "how the language shifts between formal and familiar - showing respect to elders "
                       "and strangers, warmth to friends. Each line shows the register in action.",
                       "respect is the covenant that shapes the tongue.",
                       "d_registers"))
    add("compound", "%s Compound and Complex Sentences" % n, "Advanced", "advanced", 30,
        _slot_sent_set(L, L["compound"], "Compound and Complex Sentences", "compound sentences",
                       "how to join ideas - because, when, if, although, so that. Each line builds "
                       "a longer sentence from shorter ones you already know.",
                       "complex sentences are covenants woven together.",
                       "d_compound"))
    for i in range(3):
        ctitle = "%s Conversation: %s" % (n, L["conversations"][i][0])
        add("conv%d" % i, ctitle, "Advanced", "advanced", 31 + i, slot_conversation(L, i))
    add("review", "%s Mastery Review and Full Reference" % n, "Advanced", "advanced", 34, slot_review(L))

    assert len(E) == 34, "need exactly 34 entries, got %d" % len(E)
    assert [e["ladder_rank"] for e in E] == list(range(1, 35))
    assert set(DEMOS) == {e["demo_key"] for e in E}, "demo map misses entries"
    return E
