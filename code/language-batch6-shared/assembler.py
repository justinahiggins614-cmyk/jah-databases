#!/usr/bin/env python3
"""Shared assembler for JAH Databases language batch 6 (ranks 51-60).
Builds 10 language -> English database PAIRS (public + Signature editions),
34 FULL records each, mirroring db/language-pashto(+signature) structure.

Never commits. Never touches data/manifest.json or api.json.
Property of Justin Addam Higgins (JAH).
"""
import json, gzip, os, re, subprocess, sys, html as htmlmod

DB_ROOT = os.path.expanduser("~/workspace/jah-databases/db")
DATA_ROOT = os.path.expanduser("~/workspace/jah-databases-data-1/data")
CODE_ROOT = os.path.expanduser("~/workspace/jah-databases/code")
MANIFEST = os.path.expanduser("~/workspace/jah-databases/data/manifest.json")
TEMPLATE_PUB = os.path.join(DB_ROOT, "language-pashto", "index.html")
TEMPLATE_SIG = os.path.join(DB_ROOT, "language-pashto-signature", "index.html")
GEN_PUB = os.path.join(DB_ROOT, "language-pashto", "gen-language-pashto.js")
GEN_SIG = os.path.join(DB_ROOT, "language-pashto-signature", "gen-language-pashto-signature.js")

TIERS = ["Foundations", "Compounded", "Advanced"]
TOPIC_DEFS = [
    ("overview",    "Foundations", "{N} Language Overview"),
    ("alphabet",    "Foundations", "{N} Writing System and Alphabet"),
    ("phonology",   "Foundations", "{N} Pronunciation and Phonology"),
    ("nouns",       "Foundations", "{N} Core Nouns I"),
    ("verbs",       "Foundations", "{N} Core Verbs I"),
    ("adjectives",  "Foundations", "{N} Adjectives and Adverbs"),
    ("pronouns",    "Foundations", "{N} Pronouns"),
    ("numbers",     "Foundations", "{N} Numbers and Time"),
    ("greetings",   "Foundations", "{N} Greetings and Everyday Phrases"),
    ("grammar",     "Foundations", "{N} Grammar Essentials"),
    ("home",        "Compounded",  "{N} at Home and with Family"),
    ("food",        "Compounded",  "{N} Food and Cooking"),
    ("travel",      "Compounded",  "{N} Travel and Directions"),
    ("work",        "Compounded",  "{N} Work and School"),
    ("health",      "Compounded",  "{N} Health and the Body"),
    ("emotions",    "Compounded",  "{N} Emotions and Feelings"),
    ("nature",      "Compounded",  "{N} Nature and Weather"),
    ("shopping",    "Compounded",  "{N} Shopping and Money"),
    ("social",      "Compounded",  "{N} Friendship and Social Life"),
    ("technology",  "Compounded",  "{N} Technology and Communication"),
    ("tenses",      "Compounded",  "{N} Verb Tenses in Sentences"),
    ("questions",   "Advanced",    "{N} Questions and Answers"),
    ("commands",    "Advanced",    "{N} Commands and Requests"),
    ("descriptions","Advanced",    "{N} Descriptions of People and Places"),
    ("story1",      "Advanced",    "{N} Story I: {S1}"),
    ("story2",      "Advanced",    "{N} Story II: {S2}"),
    ("story3",      "Advanced",    "{N} Story III: {S3}"),
    ("idioms",      "Advanced",    "{N} Idioms and Proverbs"),
    ("registers",   "Advanced",    "{N} Formal and Polite Registers"),
    ("complex",     "Advanced",    "{N} Compound and Complex Sentences"),
    ("conv1",       "Advanced",    "{N} Conversation: At the Market"),
    ("conv2",       "Advanced",    "{N} Conversation: Meeting a Friend"),
    ("conv3",       "Advanced",    "{N} Conversation: Solving a Problem"),
    ("mastery",     "Advanced",    "{N} Mastery Review and Full Reference"),
]
assert len(TOPIC_DEFS) == 34

GEN_TOPIC_TITLES = [
    "{N} Language Overview", "{N} Writing System and Alphabet",
    "{N} Pronunciation and Phonology", "{N} Core Nouns I", "{N} Core Verbs I",
    "{N} Adjectives and Adverbs", "{N} Pronouns", "{N} Numbers and Time",
    "{N} Greetings and Everyday Phrases", "{N} Grammar Essentials",
    "{N} at Home and with Family", "{N} Food and Cooking", "{N} Travel and Directions",
    "{N} Work and School", "{N} Health and the Body", "{N} Emotions and Feelings",
    "{N} Nature and Weather", "{N} Shopping and Money", "{N} Friendship and Social Life",
    "{N} Technology and Communication", "{N} Verb Tenses in Sentences",
    "{N} Questions and Answers", "{N} Commands and Requests",
    "{N} Descriptions of People and Places", "{N} Story I: {S1}", "{N} Story II: {S2}",
    "{N} Story III: {S3}", "{N} Idioms and Proverbs", "{N} Formal and Polite Registers",
    "{N} Compound and Complex Sentences", "{N} Conversation: At the Market",
    "{N} Conversation: Meeting a Friend", "{N} Conversation: Solving a Problem",
    "{N} Mastery Review and Full Reference",
]

# ---------------------------------------------------------------- content helpers
def triples_lines(triples, numbered=True):
    out = []
    for i, t in enumerate(triples, 1):
        lang, rom, eng = t[0], (t[1] if len(t) > 1 else ""), (t[2] if len(t) > 2 else "")
        mid = (" " + rom) if rom and rom != lang else ""
        out.append(("%d. %s%s - %s" % (i, lang, mid, eng)) if numbered else ("%s%s - %s" % (lang, mid, eng)))
    return "\n".join(out)

def demo_program(title, rec_id, tier, kind, data_lines, note):
    """Build an executable Python demo program. data_lines: list of strings."""
    safe_title = title.replace('"', "'")
    body = "\n".join("    %r," % ln for ln in data_lines)
    return (
        "#!/usr/bin/env python3\n"
        '"""%s - working demonstration.\n'
        "Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"
        '"""\n'
        "DATA = [\n%s\n]\n"
        "NOTE = %r\n"
        "def main():\n"
        "    assert DATA, 'demo data empty'\n"
        "    shown = 0\n"
        "    for line in DATA:\n"
        "        assert isinstance(line, str) and line.strip(), 'blank demo line'\n"
        "        print(line)\n"
        "        shown += 1\n"
        "    assert shown == len(DATA)\n"
        "    print('Checked %%d %s lines. DEMO OK' %% shown)\n"
        "main()\n" % (safe_title, rec_id, tier, body, note, kind)
    )

SIG_LENS_OPEN = ("Signature original interpretation. The Signature {N} Method begins here - "
                 "Record {n}, {title}: every letter a sworn sign, every word a sealed token, "
                 "every sentence a working covenant. "
                 "This record reframes the same {N} ground as Signature science - the identical facts taught "
                 "through the Signature ladder: sign, token, covenant, mastery. Clearly labeled Signature-made, "
                 "never presented as authentic public record. ")

def sig_drills(name, topic_title, drills):
    lines = ["The Signature drills for \"%s\":" % topic_title]
    for i, d in enumerate(drills, 1):
        lines.append("Drill %d. %s" % (i, d))
    return "\n".join(lines)

# ---------------------------------------------------------------- record builders
def _ctx(L, edition, n, tier, title):
    return {"L": L, "edition": edition, "n": n, "tier": tier, "title": title,
            "name": L["name"], "sig": edition == "signature"}

def _wrap(L, edition, n, tier, title, description, how, key_points, requirements,
          standards, citations, demo_kind, demo_lines, demo_note):
    prefix = L["prefix_sig"] if edition == "signature" else L["prefix_pub"]
    rec_id = prefix + ("%06d" % n)
    desc = (SIG_LENS_OPEN.format(N=L["name"], n=n, title=title) + description) if edition == "signature" else description
    return {
        "id": rec_id, "t": title, "g": tier,
        "name": title, "title": title,
        "description": desc,
        "how_it_works": how,
        "key_points": key_points,
        "requirements": requirements,
        "standards": standards,
        "citations": citations,
        "src": "signature" if edition == "signature" else "public-harvest",
        "ladder_rank": n, "ladder_tier": tier.lower(),
        "demo": {"kind": "python", "language": "python",
                 "program": demo_program(title, rec_id, tier, demo_kind, demo_lines, demo_note),
                 "note": demo_note},
    }

def _std(L):
    return [
        "Language codes follow ISO 639-1 (%s) and ISO 639-3 (%s)." % (L["iso1"], L["iso3"]),
        "Romanization in this database follows the scheme defined in record 2, aligned with standard linguistic notation for %s." % L["name"],
        "Grammatical description follows the standard reference grammars cited below.",
    ]

def _req_found(L):
    return [
        "Learn the writing system in record 2 before anything else - every later record assumes you can read the script.",
        "Learn each noun with its grammar class (gender, noun class, or classifier) where the language requires it.",
        "Learn verbs with their principal parts or stem forms, not as isolated words.",
        "Say every example aloud; %s rewards the speaking mouth, not the silent eye." % L["name"],
    ]

def rec_overview(L, edition, n, tier, title):
    o = L["overview"]
    paras = o["paras"]
    description = "\n".join(paras) + "\nKey facts: " + "; ".join(o["facts"]) + "."
    how = o["how"]
    kp = o["facts"][:8]
    if edition == "signature":
        how = ("The Signature Method teaches the overview as a charter: the language is a sworn system of signs, "
               "and this record is its charter - family, codes, speakers, script, word order, and grammar in one sealed document. " + how)
        kp = ["Signature charter framing: the same public facts, sealed as the sworn starting covenant of the Signature %s Method." % L["name"]] + kp
    drills = [
        "Recite the language charter aloud: family, ISO codes, speaker count, script, word order - one breath, no notes.",
        "Write the native name of the language from memory three times.",
        "Name the dialect groups and where each is spoken, then check against the charter.",
        "Explain split features of %s grammar (word order, noun classes, verb system) to a partner in two minutes." % L["name"],
        "Map the language family tree from %s up to its top-level family on paper." % L["name"],
    ]
    if edition == "signature":
        description += "\n" + sig_drills(L["name"], title, drills)
    demo_lines = [("%d. %s" % (i + 1, f)) for i, f in enumerate(o["facts"])]
    return _wrap(L, edition, n, tier, title, description, how, kp, _req_found(L), _std(L),
                 L["citations"], "overview-facts", demo_lines,
                 "Prints the charter facts of the language overview and self-checks the list.")

def rec_alphabet(L, edition, n, tier, title):
    a = L["alphabet"]
    intro, letters, note = a["intro"], a["letters"], a["note"]
    description = intro + "\n" + "\n".join(
        "%d. %s - %s%s" % (i + 1, lt, snd, (" - example: " + ex) if ex else "")
        for i, (lt, snd, ex) in enumerate(letters)) + "\n" + note
    how = a["how"]
    kp = ["%s is written in %s." % (L["name"], a["script_short"]),
          "Study order in this record: " + ", ".join(lt for lt, _, _ in letters[:6]) + ", ... through " + letters[-1][0] + ".",
          note] + ["Each letter is learned as shape + sound + example word, never shape alone."]
    if edition == "signature":
        how = ("The Signature Method seals each letter as a sworn sign: trace it, voice it, anchor it to its example word, "
               "and the alphabet becomes thirty sworn allies instead of thirty strangers. " + how)
        kp = ["Signature alphabet framing: each letter a sworn sign, sealed by shape + sound + example."] + kp
    drills = [
        "Write the full letter sequence from memory, then check letter by letter.",
        "Voice each letter with its example word, three rounds, no hesitation.",
        "Cover the sound column and name each letter's sound from the shape alone.",
        "Dictation: a partner reads example words, you write them in the script.",
        "Speed round: name all letters and sounds against a two-minute timer.",
    ]
    if edition == "signature":
        description += "\n" + sig_drills(L["name"], title, drills)
    demo_lines = ["%d. %s = %s%s" % (i + 1, lt, snd, ("  e.g. " + ex) if ex else "")
                  for i, (lt, snd, ex) in enumerate(letters)]
    return _wrap(L, edition, n, tier, title, description, how, kp, _req_found(L), _std(L),
                 L["citations"], "alphabet", demo_lines,
                 "Prints the writing-system chart and self-checks every row.")

def rec_phonology(L, edition, n, tier, title):
    p = L["phonology"]
    description = p["intro"] + "\n" + "\n".join("%d. %s: %s" % (i + 1, t, d) for i, (t, d) in enumerate(p["facts"]))
    how = p["how"]
    kp = [t + ": " + d for t, d in p["facts"][:8]]
    if edition == "signature":
        how = ("The Signature Method trains the mouth before the mind: each sound is a sworn physical act - "
               "place the tongue, shape the air, seal the sound. " + how)
        kp = ["Signature sound framing: every sound a sworn physical act of tongue and air."] + kp
    drills = [
        "Minimal-pair shadowing: repeat each contrast pair until a listener cannot tell them apart.",
        "Record yourself reading the example words, compare with the descriptions, repeat.",
        "Tone/stress drill: mark the melody of each example, then reproduce it blind.",
        "Slow-motion drill: stretch each new sound to two seconds, then snap it to natural speed.",
        "Chain drill: build words sound by sound, adding one sound per round.",
    ]
    if edition == "signature":
        description += "\n" + sig_drills(L["name"], title, drills)
    demo_lines = ["%d. %s - %s" % (i + 1, t, d) for i, (t, d) in enumerate(p["facts"])]
    return _wrap(L, edition, n, tier, title, description, how, kp, _req_found(L), _std(L),
                 L["citations"], "phonology", demo_lines,
                 "Prints the sound inventory with articulation notes and self-checks the list.")

def _vocab_rec(L, edition, n, tier, title, key, intro, how_extra, demo_kind, demo_note):
    v = L[key]
    description = intro + "\n" + triples_lines(v["items"])
    how = v["how"] + " " + how_extra
    kp = ["%d core %s, each with %s, romanization, and English." % (len(v["items"]), v["label"], L["script_word"])] + v["notes"][:6]
    if edition == "signature":
        how = ("The Signature Method seals each word as a token: say it, see it, use it in a sentence within sixty seconds, "
               "or it is not sealed. " + how)
        kp = ["Signature vocabulary framing: each word a sealed token, earned by use within sixty seconds."] + kp
    drills = [
        "Sixty-second seal: use each new word in a spoken sentence within a minute of meeting it.",
        "Reverse drill: English to %s, no romanization peeking, three clean rounds." % L["name"],
        "Sentence ladder: reuse each word in a longer sentence than the last.",
        "Category sort: speak each word into its theme group from memory.",
        "Teach-back: explain five words to a partner using only %s." % L["name"],
    ]
    if edition == "signature":
        description += "\n" + sig_drills(L["name"], title, drills)
    demo_lines = triples_lines(v["items"]).split("\n")
    return _wrap(L, edition, n, tier, title, description, how, kp, _req_found(L), _std(L),
                 L["citations"], demo_kind, demo_lines, demo_note)

def rec_nouns(L, edition, n, tier, title):
    return _vocab_rec(L, edition, n, tier, title, "nouns",
                      L["nouns"]["intro"], L["nouns"].get("how_extra", ""),
                      "core-nouns", "Flashcard printer for the core noun set with self-check.")

def rec_verbs(L, edition, n, tier, title):
    return _vocab_rec(L, edition, n, tier, title, "verbs",
                      L["verbs"]["intro"], L["verbs"].get("how_extra", ""),
                      "core-verbs", "Flashcard printer for the core verb set with self-check.")

def rec_adjectives(L, edition, n, tier, title):
    v = L["adjectives"]
    items = [t for t in v["items"]]
    description = v["intro"] + "\nAdjectives:\n" + triples_lines(items[:6]) + "\nAdverbs:\n" + triples_lines(v["adverbs"])
    how = v["how"]
    kp = ["Adjectives and adverbs with %s, romanization, and English gloss." % L["script_word"]] + v["notes"][:5]
    if edition == "signature":
        how = ("The Signature Method treats modifiers as color-tokens: attach each to a noun or verb you already own. " + how)
        kp = ["Signature modifier framing: each modifier a color-token attached to a sealed word."] + kp
    drills = [
        "Attach each adjective to three different nouns aloud.",
        "Adverb ladder: act each adverb with a verb, escalating the intensity.",
        "Opposite pairs: speak each adjective with its opposite from memory.",
        "Describe the room around you using only the adjectives in this record.",
        "Modifier chain: build one sentence using three adjectives and two adverbs.",
    ]
    if edition == "signature":
        description += "\n" + sig_drills(L["name"], title, drills)
    demo_lines = (["ADJECTIVES:"] + triples_lines(items[:6]).split("\n") + ["ADVERBS:"] +
                  triples_lines(v["adverbs"]).split("\n"))
    return _wrap(L, edition, n, tier, title, description, how, kp, _req_found(L), _std(L),
                 L["citations"], "adjectives-adverbs", demo_lines,
                 "Prints adjectives and adverbs with glosses and self-checks.")

def rec_pronouns(L, edition, n, tier, title):
    return _vocab_rec(L, edition, n, tier, title, "pronouns",
                      L["pronouns"]["intro"], L["pronouns"].get("how_extra", ""),
                      "pronouns", "Printer for the pronoun chart with self-check.")

def rec_numbers(L, edition, n, tier, title):
    v = L["numbers"]
    description = v["intro"] + "\n" + triples_lines(v["items"]) + "\n" + v["time_note"]
    how = v["how"]
    kp = ["Numbers 1-10 with %s, romanization, and English." % L["script_word"], v["time_note"]] + v["notes"][:5]
    if edition == "signature":
        how = ("The Signature Method counts in ladders: 1-10 sealed first, then tens, then the clock. " + how)
        kp = ["Signature number framing: numbers sealed in ladders - units, tens, then time."] + kp
    drills = [
        "Count 1-10 forward and backward without a single pause.",
        "Clock drill: say five different times aloud from memory.",
        "Arithmetic aloud: add and subtract small numbers in %s." % L["name"],
        "Tens ladder: build 11-99 from the patterns in this record.",
        "Speed count: 1-10 against a fifteen-second timer, three clean runs.",
    ]
    if edition == "signature":
        description += "\n" + sig_drills(L["name"], title, drills)
    demo_lines = triples_lines(v["items"]).split("\n") + ["TIME: " + v["time_note"]]
    return _wrap(L, edition, n, tier, title, description, how, kp, _req_found(L), _std(L),
                 L["citations"], "numbers-time", demo_lines,
                 "Prints the number chart and time expressions with self-check.")

def rec_greetings(L, edition, n, tier, title):
    return _vocab_rec(L, edition, n, tier, title, "greetings",
                      L["greetings"]["intro"], L["greetings"].get("how_extra", ""),
                      "greetings", "Printer for greetings and everyday phrases with self-check.")

def rec_grammar(L, edition, n, tier, title):
    g = L["grammar"]
    parts = [g["intro"]]
    for i, (rule, expl, xl, xr, xe) in enumerate(g["rules"], 1):
        mid = (" " + xr) if xr and xr != xl else ""
        parts.append("%d. %s: %s Example: %s%s - %s" % (i, rule, expl, xl, mid, xe))
    description = "\n".join(parts)
    how = g["how"]
    kp = [r[0] + ": " + r[1] for r in g["rules"][:8]]
    if edition == "signature":
        how = ("The Signature Method treats grammar as covenant law: each rule a sealed law with a living example. " + how)
        kp = ["Signature grammar framing: each rule a sealed covenant law with a living example."] + kp
    drills = [
        "Rule-to-mouth: read each rule, then produce a new example without looking.",
        "Error hunt: take each example, break it deliberately, then repair it.",
        "Transform chain: convert each example through every rule in this record.",
        "Teach the law: explain two rules to a partner using only new examples.",
        "Speed parse: identify the rule at work in ten fresh sentences.",
    ]
    if edition == "signature":
        description += "\n" + sig_drills(L["name"], title, drills)
    demo_lines = ["%d. %s :: %s%s = %s" % (i + 1, r[0], r[2], (" [" + r[3] + "]") if r[3] and r[3] != r[2] else "", r[4])
                  for i, r in enumerate(g["rules"])]
    return _wrap(L, edition, n, tier, title, description, how, kp, _req_found(L), _std(L),
                 L["citations"], "grammar", demo_lines,
                 "Prints each grammar rule with its worked example and self-checks.")

def rec_story(L, edition, n, tier, title, story_key):
    st = L["stories"][story_key]
    description = st["intro"] + "\n" + triples_lines(st["lines"])
    how = st["how"]
    kp = ["A complete %s story in %d lines, every line carrying %s, romanization, and English." %
          (L["name"], len(st["lines"]), L["script_word"])] + st["notes"][:5]
    if edition == "signature":
        how = ("The Signature Method reads each story as a covenant of the ancestors: the plot teaches the grammar. " + how)
        kp = ["Signature story framing: plot and grammar learned together as one covenant."] + kp
    drills = [
        "Retell the story aloud in %s without looking, keeping every plot point." % L["name"],
        "Line-ladder: memorize the story three lines at a time, then join them.",
        "Voice round: give each character a different voice and perform the story.",
        "Grammar hunt: find three grammar rules from earlier records alive in the story.",
        "Sequel: continue the story with three new lines of your own in %s." % L["name"],
    ]
    if edition == "signature":
        description += "\n" + sig_drills(L["name"], title, drills)
    demo_lines = triples_lines(st["lines"]).split("\n")
    return _wrap(L, edition, n, tier, title, description, how, kp, _req_found(L), _std(L),
                 L["citations"], "story", demo_lines,
                 "Story-line printer with self-check.")

def rec_idioms(L, edition, n, tier, title):
    im = L["idioms"]
    parts = [im["intro"]]
    for i, (idiom, rom, lit, mean) in enumerate(im["items"], 1):
        mid = (" " + rom) if rom and rom != idiom else ""
        parts.append('%d. %s%s - literal: "%s" - meaning: %s' % (i, idiom, mid, lit, mean))
    description = "\n".join(parts)
    how = im["how"]
    kp = ["%d idioms and proverbs with literal gloss and real meaning." % len(im["items"])] + im["notes"][:5]
    if edition == "signature":
        how = ("The Signature Method treats each proverb as a covenant of the ancestors, sealed by use. " + how)
        kp = ["Signature idiom framing: each proverb a covenant of the ancestors."] + kp
    drills = [
        "Use each idiom in a fresh spoken sentence of your own.",
        "Literal-to-meaning: hear the literal gloss, produce the real meaning.",
        "Situation match: a partner names a situation, you answer with the fitting proverb.",
        "Story seed: build a two-sentence story around each proverb.",
        "Teach-back: explain three proverbs to a partner without translating word for word.",
    ]
    if edition == "signature":
        description += "\n" + sig_drills(L["name"], title, drills)
    demo_lines = ["%d. %s = %s" % (i + 1, it[0], it[3]) for i, it in enumerate(im["items"])]
    return _wrap(L, edition, n, tier, title, description, how, kp, _req_found(L), _std(L),
                 L["citations"], "idioms", demo_lines,
                 "Idiom printer (idiom to meaning) with self-check.")

def rec_registers(L, edition, n, tier, title):
    rg = L["registers"]
    parts = [rg["intro"]]
    for i, (il, ir, ie, fl, fr, fe) in enumerate(rg["pairs"], 1):
        imid = (" " + ir) if ir and ir != il else ""
        fmid = (" " + fr) if fr and fr != fl else ""
        parts.append("%d. Casual: %s%s - %s | Polite/formal: %s%s - %s" % (i, il, imid, ie, fl, fmid, fe))
    description = "\n".join(parts)
    how = rg["how"]
    kp = ["%d casual-vs-polite pairs showing the register ladder of %s." % (len(rg["pairs"]), L["name"])] + rg["notes"][:5]
    if edition == "signature":
        how = ("The Signature Method climbs the register ladder rung by rung: casual sealed first, polite sealed second. " + how)
        kp = ["Signature register framing: the politeness ladder climbed rung by rung."] + kp
    drills = [
        "Ladder climb: say each casual line, then its polite twin, without pause.",
        "Situation sort: a partner names elder, friend, or stranger - you pick the rung.",
        "Soften round: take each casual line and make it politer still.",
        "Role play: greet a friend, then an elder, switching rungs cleanly.",
        "Listen-and-place: hear a line, name its rung and why.",
    ]
    if edition == "signature":
        description += "\n" + sig_drills(L["name"], title, drills)
    demo_lines = ["%d. CASUAL %s = %s  |  FORMAL %s = %s" % (i + 1, p[0], p[2], p[3], p[5])
                  for i, p in enumerate(rg["pairs"])]
    return _wrap(L, edition, n, tier, title, description, how, kp, _req_found(L), _std(L),
                 L["citations"], "registers", demo_lines,
                 "Register-pair printer with self-check.")

def rec_conversation(L, edition, n, tier, title, conv_key):
    cv = L["conversations"][conv_key]
    parts = [cv["intro"] + " Setting: " + cv["setting"] + "."]
    for i, (sp, lang, rom, eng) in enumerate(cv["turns"], 1):
        mid = (" " + rom) if rom and rom != lang else ""
        parts.append("%d. %s: %s%s - %s" % (i, sp, lang, mid, eng))
    description = "\n".join(parts)
    how = cv["how"]
    kp = ["A complete %d-turn %s conversation: %s." % (len(cv["turns"]), L["name"], cv["setting"])] + cv["notes"][:5]
    if edition == "signature":
        how = ("The Signature Method performs each conversation as a living covenant between speakers. " + how)
        kp = ["Signature conversation framing: dialogue performed as a living covenant."] + kp
    drills = [
        "Two-voice performance: perform the conversation with a partner, twice, swapping roles.",
        "Cover-and-continue: hide the next turn, predict it, then check.",
        "Improvise: continue the conversation three more turns of your own.",
        "Speed round: perform the whole conversation against a three-minute timer.",
        "Transform: replay the scene with one fact changed, keeping it grammatical.",
    ]
    if edition == "signature":
        description += "\n" + sig_drills(L["name"], title, drills)
    demo_lines = ["%d. %s: %s = %s" % (i + 1, t[0], t[1], t[3]) for i, t in enumerate(cv["turns"])]
    return _wrap(L, edition, n, tier, title, description, how, kp, _req_found(L), _std(L),
                 L["citations"], "conversation", demo_lines,
                 "Conversation-turn printer with self-check.")

def rec_mastery(L, edition, n, tier, title):
    m = L["mastery"]
    description = m["intro"] + "\n" + "\n".join("%d. %s: %s" % (i + 1, t, d) for i, (t, d) in enumerate(m["sections"]))
    how = m["how"]
    kp = [t + ": " + d for t, d in m["sections"][:8]]
    if edition == "signature":
        how = ("The Signature Method seals the whole ladder in one review: sign, token, covenant, mastery. " + how)
        kp = ["Signature mastery framing: the whole ladder sealed in one review."] + kp
    drills = [
        "Full-ladder recitation: name all 34 records of this database in order.",
        "Weak-rung hunt: list your three weakest topics and drill them first.",
        "Teach the ladder: explain the whole course to a partner in ten minutes.",
        "Mixed review: one sentence from every tier, spoken, no notes.",
        "Oath of mastery: perform one story and one conversation end to end.",
    ]
    if edition == "signature":
        description += "\n" + sig_drills(L["name"], title, drills)
    demo_lines = ["%d. %s - %s" % (i + 1, t, d) for i, (t, d) in enumerate(m["sections"])]
    return _wrap(L, edition, n, tier, title, description, how, kp, _req_found(L), _std(L),
                 L["citations"], "mastery", demo_lines,
                 "Mastery-review section printer with self-check.")

THEME_KEYS = ["home", "food", "travel", "work", "health", "emotions", "nature", "shopping", "social", "technology"]

def assemble_records(L, edition):
    """Build 34 full records for one edition. Returns list of dicts."""
    recs = []
    suffix = " (Signature Edition)" if edition == "signature" else ""
    story_titles = [L["stories"]["story1"]["title"], L["stories"]["story2"]["title"], L["stories"]["story3"]["title"]]
    for n, (key, tier, tplt) in enumerate(TOPIC_DEFS, 1):
        title = tplt.format(N=L["name"], S1=story_titles[0], S2=story_titles[1], S3=story_titles[2]) + suffix
        if key == "overview": r = rec_overview(L, edition, n, tier, title)
        elif key == "alphabet": r = rec_alphabet(L, edition, n, tier, title)
        elif key == "phonology": r = rec_phonology(L, edition, n, tier, title)
        elif key == "nouns": r = rec_nouns(L, edition, n, tier, title)
        elif key == "verbs": r = rec_verbs(L, edition, n, tier, title)
        elif key == "adjectives": r = rec_adjectives(L, edition, n, tier, title)
        elif key == "pronouns": r = rec_pronouns(L, edition, n, tier, title)
        elif key == "numbers": r = rec_numbers(L, edition, n, tier, title)
        elif key == "greetings": r = rec_greetings(L, edition, n, tier, title)
        elif key == "grammar": r = rec_grammar(L, edition, n, tier, title)
        elif key in THEME_KEYS:
            th = L["themes"][key]
            s = {"intro": th["intro"], "items": th["sentences"], "how": th["how"], "notes": th["notes"]}
            r = _sentences_rec_dict(L, edition, n, tier, title, s, "theme-" + key,
                                    "Sentence-set printer for %s with self-check." % th["label"],
                                    "The Signature Method treats each themed sentence as a working covenant for daily life. ")
        elif key == "tenses":
            t = L["tenses"]; s = {"intro": t["intro"], "items": t["forms"], "how": t["how"], "notes": t["notes"]}
            r = _sentences_rec_dict(L, edition, n, tier, title, s, "verb-tenses",
                                    "Tense-form printer for the model verb with self-check.",
                                    "The Signature Method treats each tense as a time-seal on the same living verb. ")
        elif key == "questions":
            s = L["questions"]; d = {"intro": s["intro"], "items": s["items"], "how": s["how"], "notes": s["notes"]}
            r = _sentences_rec_dict(L, edition, n, tier, title, d, "questions-answers",
                                    "Question-and-answer printer with self-check.",
                                    "The Signature Method treats every question as a key that opens an answer. ")
        elif key == "commands":
            s = L["commands"]; d = {"intro": s["intro"], "items": s["items"], "how": s["how"], "notes": s["notes"]}
            r = _sentences_rec_dict(L, edition, n, tier, title, d, "commands-requests",
                                    "Command-and-request printer with self-check.",
                                    "The Signature Method treats each command as a directed act, soft or firm by design. ")
        elif key == "descriptions":
            s = L["descriptions"]; d = {"intro": s["intro"], "items": s["items"], "how": s["how"], "notes": s["notes"]}
            r = _sentences_rec_dict(L, edition, n, tier, title, d, "descriptions",
                                    "Description printer with self-check.",
                                    "The Signature Method treats description as portraiture: each sentence paints one true stroke. ")
        elif key == "complex":
            s = L["complex"]; d = {"intro": s["intro"], "items": s["items"], "how": s["how"], "notes": s["notes"]}
            r = _sentences_rec_dict(L, edition, n, tier, title, d, "complex-sentences",
                                    "Complex-sentence printer with self-check.",
                                    "The Signature Method treats each complex sentence as two covenants joined by one hinge. ")
        elif key in ("story1", "story2", "story3"):
            r = rec_story(L, edition, n, tier, title, key)
        elif key == "idioms": r = rec_idioms(L, edition, n, tier, title)
        elif key == "registers": r = rec_registers(L, edition, n, tier, title)
        elif key in ("conv1", "conv2", "conv3"): r = rec_conversation(L, edition, n, tier, title, key)
        elif key == "mastery": r = rec_mastery(L, edition, n, tier, title)
        else: raise ValueError("unknown topic " + key)
        recs.append(r)
    assert len(recs) == 34
    return recs

def _sentences_rec_dict(L, edition, n, tier, title, s, demo_kind, demo_note, sig_frame):
    description = s["intro"] + "\n" + triples_lines(s["items"])
    all_triples = s["items"]
    how = s["how"]
    kp = ["%d sentences, every line carrying %s, romanization, and English." % (len(all_triples), L["script_word"])] + s["notes"][:5]
    if edition == "signature":
        how = sig_frame + how
        kp = ["Signature sentence framing: " + sig_frame.strip()] + kp
    drills = [
        "Shadow round: repeat each sentence immediately after reading, matching rhythm.",
        "Cover-and-say: hide the English, produce it from the %s alone." % L["name"],
        "Transform round: change one word in each sentence and keep it grammatical.",
        "Situation round: speak each sentence as if you are really there.",
        "Memory chain: recite the set in order, then in reverse.",
    ]
    if edition == "signature":
        description += "\n" + sig_drills(L["name"], title, drills)
    demo_lines = triples_lines(all_triples).split("\n")
    return _wrap(L, edition, n, tier, title, description, how, kp, _req_found(L), _std(L),
                 L["citations"], demo_kind, demo_lines, demo_note)

TOPIC_LIST = ("the language overview, the writing system, pronunciation and phonology, core nouns verbs "
    "adjectives and adverbs with sentences, pronouns, numbers and time, greetings, grammar essentials, "
    "themed sentence sets for daily life, verb tenses, questions and answers, commands and requests, "
    "descriptions, stories, idioms, formal and polite registers, complex sentences, conversations, "
    "and a mastery review")
LADDER_LIST = ("Foundations (language overview, writing system, pronunciation and phonology, core nouns, "
    "core verbs, adjectives and adverbs, pronouns, numbers and time, greetings, grammar essentials) -> "
    "Compounded (home and family, food and cooking, travel and directions, work and school, health and body, "
    "emotions and feelings, nature and weather, shopping and money, friendship and social life, technology "
    "and communication, verb tenses in sentences) -> Advanced (questions and answers, commands and requests, "
    "descriptions, three stories, idioms and proverbs, formal and polite registers, compound and complex "
    "sentences, three conversations, mastery review and full reference)")

def page_texts(L):
    """Default per-language page prose. Content modules may override via L['page_overrides']."""
    n, sd = L["name"], L["script_desc"]
    meta_pub = ("Learn %s from the ground up: %s - every record carrying %s plus "
        "romanization plus English translation plus example sentences, taught progressively along the ladder. "
        "Property of Justin Addam Higgins." % (n, sd, n))
    hero_pub = ("Learn %s from the ground up: %s - every record carrying %s plus romanization plus "
        "English translation plus example sentences, taught progressively along the ladder. - Public records - "
        "real, fact-checked %s language teaching: %s - every record carrying %s content plus romanization "
        "plus English translation plus example sentences. Every record carries the full entry: description, "
        "how it works, key points, requirements, standards, citations, and a working demonstration program. "
        "Records are ordered by the teaching ladder: %s." % (n, sd, n, n, TOPIC_LIST, n, LADDER_LIST))
    role_pub = ("%s language archivist - teaching %s from the %s through core vocabulary, grammar, and "
        "everyday sentences to stories, idioms, registers, and conversations; teaching progressively along "
        "the ladder from foundations through compounded to advanced; answers from many angles - definition, "
        "example, pronunciation, usage, grammar, culture - using only archive data from this system"
        % (n, n, sd))
    ai_dd_pub = ("JAH %s Language Archivist - %s" % (n, role_pub))
    greet_pub = ("I am the JAH %s Language Archivist. Ask me about %s - from the %s through core words, "
        "grammar, and everyday sentences to stories, idioms, and conversations." % (n, n, sd))
    meta_sig = ("His original Signature %s Method: every letter a sworn sign, every verb a living action, "
        "every proverb a covenant of the ancestors - the full ladder from the language overview through the "
        "script, sounds, words, and grammar, through daily-life sentences, to stories, idioms, registers, and "
        "conversations, reframed as Signature science. Clearly labeled Signature-made, never presented as "
        "authentic public record. Property of Justin Addam Higgins." % n)
    hero_sig = (meta_sig + " - Signature originals - his original Signature %s Method: every letter a sworn sign, "
        "every verb a living action, every proverb a covenant of the ancestors, the whole language taught as "
        "Signature science. Clearly labeled Signature-made, never presented as authentic public record. "
        "Every record carries the full entry: description, how it works, key points, requirements, standards, "
        "citations, and a working demonstration program. Records are ordered by the teaching ladder: %s."
        % (n, LADDER_LIST))
    role_sig = ("%s language archivist - Signature editions: his original Signature %s Method, every letter a "
        "sworn sign and every verb a living action, clearly labeled Signature-made and never presented as "
        "authentic public record; teaches progressively along the ladder from foundations through compounded "
        "to advanced; answers from many angles using only archive data from this system" % (n, n))
    ai_dd_sig = ("JAH %s Language Archivist (Signature) - %s" % (n, role_sig))
    greet_sig = ("I am the JAH %s Language Archivist (Signature). Ask me about %s - from the %s through core "
        "words, grammar, and everyday sentences to stories, idioms, and conversations." % (n, n, sd))
    d = {
        "meta_pub": meta_pub, "hero_pub": hero_pub, "role_pub": role_pub, "ai_dd_pub": ai_dd_pub,
        "greet_pub": greet_pub,
        "meta_sig": meta_sig, "hero_sig": hero_sig, "role_sig": role_sig, "ai_dd_sig": ai_dd_sig,
        "greet_sig": greet_sig,
        "search_ph": "Search %s letters, words, verbs, tenses, phrases, grammar, dialogues..." % n,
        "chat_ph": "Ask about %s..." % n,
    }
    d.update(L.get("page_overrides", {}))
    return d

# ---------------------------------------------------------------- page + gen.js
def build_page(L, edition):
    name = L["name"]
    if edition == "signature":
        tpl = open(TEMPLATE_SIG, encoding="utf-8").read()
        page_title = "The %s Language Signature Database" % name
        ai_name = "JAH %s Language Archivist (Signature)" % name
        gen_ver = "jahdb-language-%s-signature-1.0" % L["slug_base"]
    else:
        tpl = open(TEMPLATE_PUB, encoding="utf-8").read()
        page_title = "The %s Language Database" % name
        ai_name = "JAH %s Language Archivist" % name
        gen_ver = "jahdb-language-%s-1.0" % L["slug_base"]
    slug = L["slug_sig"] if edition == "signature" else L["slug_pub"]
    reps = [
        ("The Pashto Language Signature Database" if edition == "signature" else "The Pashto Language Database", page_title),
        ("JAH Pashto Language Archivist (Signature)" if edition == "signature" else "JAH Pashto Language Archivist", ai_name),
        ("jahdb-language-pashto-signature-1.0" if edition == "signature" else "jahdb-language-pashto-1.0", gen_ver),
        ("gen-language-pashto-signature.js" if edition == "signature" else "gen-language-pashto.js", "gen-%s.js" % slug),
        ("language-pashto-signature" if edition == "signature" else "language-pashto", slug),
        ("Generate clearly-labeled Pashto language studies", "Generate clearly-labeled %s language studies" % name),
        ("Seeded public-record Pashto language records" if edition == "public" else "Seeded Signature-original Pashto language records",
         ("Seeded public-record %s language records" if edition == "public" else "Seeded Signature-original %s language records") % name),
    ]
    out = tpl
    for old, new in reps:
        assert old in out, "template pattern missing: %r" % old[:60]
        out = out.replace(old, new)
    # whole-line replacements for per-language prose
    P = L["page"]
    meta = P["meta_sig"] if edition == "signature" else P["meta_pub"]
    out = re.sub(r'<meta name="description" content="[^"]*">',
                 '<meta name="description" content="%s">' % meta.replace('"', "'"), out, count=1)
    out = re.sub(r'("description": ")[^"]*(",\s*"creator")',
                 lambda m: m.group(1) + meta.replace('"', "'") + m.group(2), out, count=1)
    out = re.sub(r'("name": "%s",\s*"description": ")[^"]*(")' % re.escape(page_title),
                 lambda m: m.group(1) + meta.replace('"', "'") + m.group(2), out, count=1)
    hero = P["hero_sig"] if edition == "signature" else P["hero_pub"]
    out = re.sub(r'(<h1>%s</h1>\s*<p>).*?(</p>)' % re.escape(page_title),
                 lambda m: m.group(1) + hero + m.group(2), out, count=1, flags=re.S)
    role = P["role_sig"] if edition == "signature" else P["role_pub"]
    out = re.sub(r"var ROLE='.*?';", "var ROLE='%s';" % role.replace("'", "\\'"), out, count=1, flags=re.S)
    ai_dd = P["ai_dd_sig"] if edition == "signature" else P["ai_dd_pub"]
    out = re.sub(r'(<dt>AI</dt><dd>).*?(</dd>)',
                 lambda m: m.group(1) + ai_dd + m.group(2), out, count=1, flags=re.S)
    greet = P["greet_sig"] if edition == "signature" else P["greet_pub"]
    out = re.sub(r"log\.innerHTML='<div class=\"msg a\"><div class=\"b\">'\+esc\('.*?\'\)",
                 "log.innerHTML='<div class=\"msg a\"><div class=\"b\">'+esc('%s')" % greet.replace("'", "\\'"), out, count=1, flags=re.S)
    out = re.sub(r'placeholder="Search Pashto[^"]*"',
                 'placeholder="%s"' % P["search_ph"].replace('"', "'"), out, count=1)
    out = re.sub(r'placeholder="Ask about Pashto\.\.\."',
                 'placeholder="%s"' % P["chat_ph"].replace('"', "'"), out, count=1)
    # sanity: no leftover Pashto/pashto references
    assert "Pashto" not in out and "pashto" not in out, "leftover Pashto reference in page"
    # canon markers
    assert 'id="stCount"' in out
    assert ">Exhaustive</button>" in out
    assert "All Database Merger" in out and "mergePanel" in out
    assert "minmax(120px,1fr)" in out
    assert 'pre class="codeblock"' in out
    assert "dataset.p" in out
    return out

def build_gen_js(L, edition):
    tpl = open(GEN_SIG if edition == "signature" else GEN_PUB, encoding="utf-8").read()
    name = L["name"]
    slug = L["slug_sig"] if edition == "signature" else L["slug_pub"]
    prefix = L["prefix_sig"] if edition == "signature" else L["prefix_pub"]
    gen_ver = "jahdb-%s-1.0" % slug
    suffix = " (Signature Edition)" if edition == "signature" else ""
    topics = {}
    story_titles = [L["stories"]["story1"]["title"], L["stories"]["story2"]["title"], L["stories"]["story3"]["title"]]
    for t in GEN_TOPIC_TITLES:
        title = t.format(N=name, S1=story_titles[0], S2=story_titles[1], S3=story_titles[2]) + suffix
        tier = None
        for key, tr, tplt in TOPIC_DEFS:
            cand = tplt.format(N=name, S1=story_titles[0], S2=story_titles[1], S3=story_titles[2])
            if cand == t.format(N=name, S1=story_titles[0], S2=story_titles[1], S3=story_titles[2]):
                tier = tr; break
        topics.setdefault(tier, []).append('"%s - %s"' % (title, tier))
    out = tpl
    old_prefix = "JAH-LPUSS-" if edition == "signature" else "JAH-LPUS-"
    assert old_prefix in out
    out = out.replace(old_prefix, prefix)
    old_name = "The Pashto Language Signature Database" if edition == "signature" else "The Pashto Language Database"
    new_name = "The %s Language Signature Database" % name if edition == "signature" else "The %s Language Database" % name
    assert old_name in out
    out = out.replace(old_name, new_name)
    old_ver = "jahdb-language-pashto-signature-1.0" if edition == "signature" else "jahdb-language-pashto-1.0"
    assert old_ver in out
    out = out.replace(old_ver, gen_ver)
    # replace TOPICS block
    m = re.search(r'var TOPICS=\{.*?\n\};', out, flags=re.S)
    assert m, "TOPICS block not found"
    new_topics = "var TOPICS={\n"
    for tier in TIERS:
        new_topics += ' "%s": [\n  %s\n ],\n' % (tier, ",\n  ".join(topics[tier]))
    new_topics += "};"
    out = out[:m.start()] + new_topics + out[m.end():]
    out = out.replace("# Pashto Study", "# %s Study" % name)
    out = out.replace('"pashto-demo"', '"%s-demo"' % L["slug_base"])
    out = out.replace("JAHDB.registerGenerator('language-pashto-signature'" if edition == "signature" else "JAHDB.registerGenerator('language-pashto'",
                      "JAHDB.registerGenerator('%s'" % slug)
    assert "Pashto" not in out and "pashto" not in out and "LPUS" not in out, "leftover template text in gen.js"
    assert prefix in out and gen_ver in out
    return out

# ---------------------------------------------------------------- data writer
def write_data(slug, records):
    ddir = os.path.join(DATA_ROOT, slug)
    cdir = os.path.join(ddir, "chunks")
    os.makedirs(cdir, exist_ok=True)
    idx_path = os.path.join(ddir, "index.jsonl.gz")
    with gzip.open(idx_path, "wt", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps({"id": r["id"], "t": r["t"], "g": r["g"]}, ensure_ascii=False) + "\n")
    n_chunks = (len(records) + 99) // 100
    for c in range(n_chunks):
        cp = os.path.join(cdir, "chunk-%04d.jsonl.gz" % c)
        with gzip.open(cp, "wt", encoding="utf-8") as f:
            for r in records[c * 100:(c + 1) * 100]:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return idx_path, n_chunks

def write_db_files(L, edition, page_html, gen_js):
    slug = L["slug_sig"] if edition == "signature" else L["slug_pub"]
    ddir = os.path.join(DB_ROOT, slug)
    os.makedirs(ddir, exist_ok=True)
    with open(os.path.join(ddir, "index.html"), "w", encoding="utf-8") as f:
        f.write(page_html)
    with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
        f.write(gen_js)
    return ddir

# ---------------------------------------------------------------- gates
PROFANE = ["fuck", "shit", "bitch", "cunt", "nigger", "nigga", "faggot", "retard",
           "whore", "slut", "dick", "pussy", "asshole", "bastard"]
RELIGIOUS_CTX = ["allah", "bible", "koran", "quran", "jesus", "christ", "church",
                 "mosque", "pray", "holy", "sacred", "worship", "heaven", "hell",
                 "god", "goddess", "divine", "bless", "soul", "sin ", "prophet",
                 "scripture", "temple", "monk", "nun ", "priest", "imam", "crucifix"]

def content_gate(records):
    """Scan for profanity (hard fail) and religious-framing terms (context review)."""
    hard, ctx = [], []
    for r in records:
        blob = json.dumps(r, ensure_ascii=False).lower()
        rid = r["id"]
        for w in PROFANE:
            if re.search(r"\b" + re.escape(w) + r"\b", blob):
                hard.append((rid, w))
        for w in RELIGIOUS_CTX:
            for m in re.finditer(re.escape(w), blob):
                s = max(0, m.start() - 60); e = min(len(blob), m.end() + 60)
                ctx.append((rid, w, blob[s:e].replace("\n", " ")))
    return hard, ctx

def dedupe_within(records):
    ids = [r["id"] for r in records]
    ts = [r["t"] for r in records]
    dup_ids = sorted({i for i in ids if ids.count(i) > 1})
    dup_t = sorted({t for t in ts if ts.count(t) > 1})
    descs = [r["description"][:200] for r in records]
    dup_d = sorted({d for d in descs if descs.count(d) > 1})
    return dup_ids, dup_t, dup_d

def dedupe_cross_system(records):
    """Exact title matches anywhere else in the data-1 tree."""
    import glob
    mine = {r["t"] for r in records}
    hits = []
    for p in glob.glob(os.path.join(DATA_ROOT, "*", "index.jsonl.gz")):
        slug = os.path.basename(os.path.dirname(p))
        if slug in {r for r in ()}:
            pass
        try:
            with gzip.open(p, "rt", encoding="utf-8") as f:
                for line in f:
                    try:
                        row = json.loads(line)
                    except Exception:
                        continue
                    if row.get("t") in mine:
                        hits.append((slug, row.get("id"), row.get("t")))
        except Exception:
            continue
    return hits

def run_demos(records):
    fails = []
    for r in records:
        prog = r["demo"]["program"]
        try:
            p = subprocess.run([sys.executable, "-c", prog], capture_output=True, text=True, timeout=30)
            ok = p.returncode == 0 and "DEMO OK" in p.stdout
            if not ok:
                fails.append((r["id"], p.returncode, (p.stderr or p.stdout)[-300:]))
        except Exception as e:
            fails.append((r["id"], "exc", str(e)[:200]))
    return fails

def node_check(path):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    return p.returncode == 0, (p.stderr or "")[:300]

def manifest_prefix_ok(prefix):
    m = json.load(open(MANIFEST, encoding="utf-8"))
    for d in m["databases"]:
        q = d.get("id_prefix") or ""
        if q and (prefix == q or prefix in q or q in prefix):
            return False, d["slug"]
    return True, None

# ---------------------------------------------------------------- driver
def build_language(L, editions=("public", "signature")):
    L = dict(L); L["page"] = page_texts(L)
    report = {"lang": L["name"], "editions": {}}
    # prefix collision check first
    for ed in editions:
        prefix = L["prefix_sig"] if ed == "signature" else L["prefix_pub"]
        ok, hit = manifest_prefix_ok(prefix)
        assert ok, "prefix collision: %s vs %s" % (prefix, hit)
    for ed in editions:
        slug = L["slug_sig"] if ed == "signature" else L["slug_pub"]
        records = assemble_records(L, ed)
        assert len(records) == 34, len(records)
        # id order + uniqueness
        prefix = L["prefix_sig"] if ed == "signature" else L["prefix_pub"]
        for i, r in enumerate(records, 1):
            assert r["id"] == prefix + ("%06d" % i), r["id"]
        dup_ids, dup_t, dup_d = dedupe_within(records)
        assert not dup_ids and not dup_t and not dup_d, (dup_ids, dup_t, dup_d)
        cross = dedupe_cross_system(records)
        hard, ctx = content_gate(records)
        assert not hard, hard
        demo_fails = run_demos(records)
        assert not demo_fails, demo_fails[:3]
        page = build_page(L, ed)
        genjs = build_gen_js(L, ed)
        ddir = write_db_files(L, ed, page, genjs)
        idx_path, n_chunks = write_data(slug, records)
        ok, err = node_check(os.path.join(ddir, "gen-%s.js" % slug))
        assert ok, err
        report["editions"][ed] = {
            "slug": slug, "records": len(records), "chunks": n_chunks,
            "dir": ddir, "index": idx_path,
            "cross_system_title_hits": cross,
            "religious_ctx_hits": [(rid, w) for rid, w, _ in ctx],
            "religious_ctx_samples": ctx[:12],
            "demos": "34/34 PASS",
        }
    return report
