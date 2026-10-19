#!/usr/bin/env python3
"""Entries for the Pashto Language databases (Manon's language project,
2026-10-17).

Dedupe gate: 'pashto' zero hits across the full manifest (2,602 databases)
and zero 'JAH-LPUS-'/'JAH-LPUSS-' hits in all shard index files of
jah-databases-data-1 (checked with code/dedupe_gate.py BEFORE authoring).
ID prefixes JAH-LPUS- (public) and JAH-LPUSS- (signature) verified free:
zero hits in manifest id_prefix values and zero hits in shard record IDs.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-pashto              - The Pashto Language Database
                                 (public-harvest: real, fact-checked Pashto
                                 language teaching - overview, the
                                 Perso-Arabic writing system, pronunciation
                                 and phonology, core vocabulary with
                                 sentences, pronouns, numbers and time,
                                 greetings, grammar essentials, themed
                                 sentence sets for daily life, verb tenses,
                                 questions and answers, commands,
                                 descriptions, stories, idioms, formal and
                                 polite registers, complex sentences,
                                 conversations, and a mastery review;
                                 every record carries Pashto content in
                                 Perso-Arabic script + transliteration +
                                 English translation + example sentences;
                                 standard references Penzl 1955; Tegey and
                                 Robson 1996; Robson and Tegey 2009; ISO
                                 639 ps/pus)
  language-pashto-signature    - The Pashto Language Signature Database
                                 (his original Signature Pashto Method:
                                 every letter a sworn sign, every verb a
                                 living action, every proverb a covenant
                                 of the ancestors; src signature, titles
                                 suffixed " (Signature Edition)", never
                                 presented as authentic public record)

34 records each, ladder-ordered 1-34 (ladder_rank 1..34, ladder_tier
foundations 1-10 / compounded 11-21 / advanced 22-34); the shard index is
written in ladder order so pages present simple -> compounded -> complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_pashto.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before hand-off.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Pashto Method: "
            "every letter a sworn sign, every verb a living action, every "
            "proverb a covenant of the ancestors, the whole language "
            "taught as Signature science. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_PENZL = ("Penzl H. A Grammar of Pashto: A Descriptive Study of the "
             "Dialect of Kandahar, Afghanistan. Washington: American "
             "Council of Learned Societies; 1955.")
CIT_TEGEY = ("Tegey H, Robson B. A Reference Grammar of Pashto. "
             "Washington: Center for Applied Linguistics; 1996.")
CIT_ROBSON = ("Robson B, Tegey H. Pashto. In: Windfuhr G, editor. The "
              "Iranian Languages. London: Routledge; 2009.")
CIT_ISO = ("ISO 639-1:2002 language code ps; ISO 639-3:2007 language "
           "code pus.")
CIT_PED = ("Standard pedagogical sources for Pashto vocabulary, usage, "
           "and phraseology.")
CIT_ALL = [CIT_PENZL, CIT_TEGEY, CIT_ROBSON, CIT_ISO, CIT_PED]

ENTRIES = []


def _sent(items):
    """items: list of (pashto, translit, english)."""
    return "\n".join(
        "%d. %s (%s - %s)" % (i + 1, ps, tr, en)
        for i, (ps, tr, en) in enumerate(items))


def _vocab(words):
    """words: list of (ps, tr, en, ex_ps, ex_tr, ex_en)."""
    return "\n".join(
        "%d. %s (%s) - %s. Example: %s (%s - %s)" % (i + 1, ps, tr, en,
                                                    ex_ps, ex_tr, ex_en)
        for i, (ps, tr, en, ex_ps, ex_tr, ex_en) in enumerate(words))


def _phrases(items):
    """items: list of (ps, tr, en, note)."""
    return "\n".join(
        "%d. %s (%s) - %s. Usage: %s" % (i + 1, ps, tr, en, note)
        for i, (ps, tr, en, note) in enumerate(items))


def _pairs(items):
    """items: list of (a_ps, a_tr, a_en, b_ps, b_tr, b_en, note)."""
    return "\n".join(
        "%d. %s (%s - %s)  |  %s (%s - %s). %s"
        % (i + 1, a_ps, a_tr, a_en, b_ps, b_tr, b_en, note)
        for i, (a_ps, a_tr, a_en, b_ps, b_tr, b_en, note) in enumerate(items))


def _dialogue(lines):
    """lines: list of (speaker, ps, tr, en)."""
    return "\n".join(
        "%d. %s: %s (%s - %s)" % (i + 1, sp, ps, tr, en)
        for i, (sp, ps, tr, en) in enumerate(lines))


def _idioms(items):
    """items: list of (ps, tr, literal, meaning, ex_ps, ex_tr, ex_en)."""
    return "\n".join(
        "%d. %s (%s). Literal: %s. Meaning: %s. Example: %s (%s - %s)"
        % (i + 1, ps, tr, literal, meaning, ex_ps, ex_tr, ex_en)
        for i, (ps, tr, literal, meaning, ex_ps, ex_tr, ex_en)
        in enumerate(items))


# ---------------------------------------------------------------- record 1

FACTS_1 = {"letters": 44, "genders": 2, "cases": 3, "tenses": 3,
           "speakers_m": 50, "iso1": "ps", "iso3": "pus"}

ENTRIES.append({
    "key": "p01_overview",
    "name": "Pashto Language Overview",
    "group": "Foundations",
    "ladder_rank": 1,
    "ladder_tier": "foundations",
    "description": (
        "Pashto (پښتو, paʂto in the south and pax̌to in the north) is an "
        "Eastern Iranian language of the Indo-European family, spoken as a "
        "first language by roughly 40 to 60 million people, most of them in "
        "Afghanistan and Pakistan. It carries ISO 639-1 code ps and ISO "
        "639-3 code pus. Pashto is an official language of Afghanistan "
        "(alongside Dari) and a recognized provincial language in Pakistan "
        "in Khyber Pakhtunkhwa and Balochistan. It is also spoken in "
        "diaspora communities across the Middle East, Europe, North "
        "America, and Australia. The three traditional dialect groups are "
        "Northern (Peshawar/Yusufzai, the 'hard' Pax̌to), Southern "
        "(Kandahar, the 'soft' Paʂto), and Central (Waziristan). The "
        "standard written language rests on the Northern dialect. Pashto is "
        "written in a modified Perso-Arabic script of 44 letters, read "
        "right to left. It is famous among linguists for its retroflex "
        "consonants, its split-ergative grammar (past tenses treat the "
        "subject like an object), and a verb system built on present and "
        "past stems with the future marked by the particle به (bə).\n"
        "Key facts: native name پښتو (paʂto/pax̌to); family Indo-European, "
        "branch Indo-Iranian, group Eastern Iranian; ISO 639-1 ps, ISO 639-3 "
        "pus; roughly 40-60 million native speakers; official in "
        "Afghanistan, recognized in Pakistan; dialects Northern (hard), "
        "Southern (soft), Central; script modified Perso-Arabic, 44 letters, "
        "right to left."
    ),
    "how_it_works": (
        "Pashto works as a subject-object-verb language with two genders "
        "(masculine and feminine) and a direct/oblique case system. In the "
        "present tense it behaves like English: زه ډوډۍ خورم (zə ḍoḍəi "
        "xorəm - I eat bread) has the subject in its normal form. In the "
        "past tense it switches to ergative alignment: the doer takes the "
        "oblique form and the verb agrees with the object - ما ډوډۍ وخوړله "
        "(mā ḍoḍəi woxoṛla - I ate bread) uses ما (mā), the oblique of زه "
        "(zə, I). There are no articles; indefiniteness is shown with یو "
        "(yaw - one/a). Negation puts نه (nə) before the verb. Questions "
        "use interrogative words like څوک (tsok - who) or څه (tsə - what), "
        "or simply rising intonation. The future is built with the particle "
        "به (bə) before the present verb: زه به ځم (zə bə dzəm - I will "
        "go). Nouns pluralize in many patterns, so each noun is learned "
        "with its plural. Verbs have two stems (present and past), and the "
        "infinitive ends in -ل (-əl)."
    ),
    "key_points": [
        "Pashto is Eastern Iranian, Indo-European: ISO 639-1 ps, ISO 639-3 pus, native name پښتو (paʂto/pax̌to).",
        "Roughly 40 to 60 million native speakers; official in Afghanistan, recognized in Pakistan's Khyber Pakhtunkhwa and Balochistan.",
        "Three dialect groups: Northern 'hard' Pax̌to (Peshawar/Yusufzai, the written standard), Southern 'soft' Paʂto (Kandahar), Central (Waziristan).",
        "Modified Perso-Arabic script, 44 letters, written right to left; special retroflex and fricative letters taught letter by letter in record 2.",
        "Subject-object-verb word order; two genders (masculine, feminine); direct and oblique cases plus vocative.",
        "Split ergativity: present tense is nominative like English, but past-tense transitive clauses put the agent in the oblique case.",
        "No articles; negation with نه (nə) before the verb; future with the particle به (bə) before the present verb.",
        "Every verb has a present stem and a past stem; the infinitive ends in -ل (-əl), as in تلل (tləl - to go).",
    ],
    "requirements": [
        "Learn the 44-letter alphabet before anything else - every later record assumes you can read the script.",
        "Learn nouns with their gender and plural; gender and number control agreement everywhere.",
        "Learn verbs as present-stem/past-stem pairs, not as single words.",
        "Expect the north/south sound split (x̌/ʂ, ǵ/ʐ); both are standard and mutually understood.",
    ],
    "standards": [
        "Language codes follow ISO 639-1 (ps) and ISO 639-3 (pus).",
        "Transliteration in this database follows the romanization scheme defined in record 2, aligned with standard Pashto linguistic notation.",
        "Grammatical description follows the standard reference grammars cited below.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method begins here: the language is a sworn "
        "system of signs carried by forty to sixty million voices, and this "
        "overview is its charter. Every letter will be a sworn sign, every "
        "verb a living action, every proverb a covenant of the ancestors. "
        "Learn the charter first - family, codes, speakers, script, gender, "
        "split ergativity - and every later lesson is simply the charter "
        "unfolding, sign by sign."
    ),
    "demo_key": "overview",
    "demo_data": FACTS_1,
})

# ---------------------------------------------------------------- record 2

LETTERS_2 = [
    ("ا", "ā/alif", "a", "اړتیا", "aṛtyā", "need"),
    ("ب", "b", "b", "باغ", "bāɣ", "garden"),
    ("پ", "p", "p", "پیسې", "payse", "money"),
    ("ت", "t", "t", "تلل", "tləl", "to go"),
    ("ټ", "ṭ", "ṭ (retroflex t)", "ټوپک", "ṭopak", "rifle"),
    ("ث", "s", "s", "ثواب", "sawāb", "reward"),
    ("ج", "j", "j", "جومات", "jomāt", "mosque"),
    ("ځ", "dz", "dz (as in adze)", "ځمکه", "dzməka", "earth"),
    ("چ", "č", "ch", "چای", "čāy", "tea"),
    ("ح", "h", "h", "حال", "hāl", "condition"),
    ("خ", "x", "kh", "خبرې", "xabare", "words"),
    ("څ", "ts", "ts (as in cats)", "څښل", "tsṣ̌əl", "to drink"),
    ("د", "d", "d", "دروازه", "darwāza", "door"),
    ("ډ", "ḍ", "ḍ (retroflex d)", "ډوډۍ", "ḍoḍəi", "bread"),
    ("ذ", "z", "z", "ذخیره", "zaxira", "reserve"),
    ("ر", "r", "r", "روژه", "roža", "fast"),
    ("ړ", "ṛ", "ṛ (retroflex r)", "ړوند", "ṛund", "blind"),
    ("ز", "z", "z", "زړه", "zṛa", "heart"),
    ("ژ", "ž", "zh (as in vision)", "ژبه", "žəba", "language"),
    ("ږ", "ǵ", "ǵ (voiced x̌)", "ږیره", "ǵira", "beard"),
    ("س", "s", "s", "سړی", "saṛay", "man"),
    ("ش", "š", "sh", "شپه", "špa", "night"),
    ("ښ", "x̌", "x̌ (voiceless postalveolar)", "ښځه", "x̌əza", "woman"),
    ("ص", "s", "s", "صبر", "sabr", "patience"),
    ("ض", "z", "z", "ضرورت", "zarurat", "necessity"),
    ("ط", "t", "t", "طبیب", "tabib", "physician"),
    ("ظ", "z", "z", "ظلم", "zulm", "oppression"),
    ("ع", "ʔ", "glottal stop", "علم", "ilm", "knowledge"),
    ("غ", "ɣ", "gh", "غر", "ɣar", "mountain"),
    ("ف", "f", "f", "فکر", "fikr", "thought"),
    ("ق", "q", "q", "قلم", "qalam", "pen"),
    ("ک", "k", "k", "کتاب", "kitāb", "book"),
    ("ګ", "g", "g", "ګل", "gul", "flower"),
    ("ل", "l", "l", "لار", "lār", "road"),
    ("م", "m", "m", "مور", "mor", "mother"),
    ("ن", "n", "n", "نوم", "num", "name"),
    ("ڼ", "ṇ", "ṇ (retroflex n)", "اڼد", "aṇd", "egg"),
    ("و", "w/u/o", "w, oo, o", "ورځ", "wrədz", "day"),
    ("ه", "h/a", "h, a", "هغه", "haɣa", "he/that"),
    ("ۀ", "ə", "uh (schwa)", "خۀ", "x̌ə", "good (fem.)"),
    ("ی", "y/i", "y, ee", "یو", "yaw", "one"),
    ("ې", "e", "e (as in bed)", "لېوه", "lewə", "wolf"),
    ("ۍ", "əy", "ay", "سپوږمۍ", "spoǧməi", "moon"),
    ("ئ", "y", "y (hamza-bearer)", "ئې", "ye", "is (fem.)"),
]

ENTRIES.append({
    "key": "p02_script",
    "name": "Pashto Writing System and Alphabet",
    "group": "Foundations",
    "ladder_rank": 2,
    "ladder_tier": "foundations",
    "description": (
        "Pashto is written in a modified Perso-Arabic script, read right to "
        "left, with 44 letters: the 28 shared Arabic letters, the Persian "
        "additions پ چ ژ ګ, and 12 Pashto-specific letters - ټ ډ ړ ڼ (the "
        "retroflex series), ښ ږ (the postalveolar fricative pair), څ ځ "
        "(the affricates ts and dz), and ې ۍ ئ ۀ (the vowel carriers). The "
        "letters ټ ډ ړ ڼ ښ ږ څ ځ exist in no other major language's "
        "alphabet and are the visual signature of written Pashto. Long and "
        "short vowels are carried by ا آ و ی ې ۍ ۀ: ا and آ for a/ā, و for "
        "w, u, and o, ی for y and i, ې for e, ۍ for the diphthong əy, and ۀ "
        "for the schwa ə. Letters join within words; six letters (ا د ډ ذ ر "
        "ړ ز ژ ږ و) join only to the right. Numerals are the Eastern Arabic "
        "set ۰۱۲۳۴۵۶۷۸۹. Punctuation follows Perso-Arabic conventions: ۔ "
        "for the full stop, ، for the comma, ؛ for the semicolon, ؟ for "
        "the question mark, and « » or \" \" for quotation. The table below "
        "lists all 44 letters with transliteration and an example word each."
    ),
    "how_it_works": (
        "Read right to left, letter by letter, sounding each joined form. "
        "The six non-joining letters (ا د ډ ذ ر ړ ز ژ ږ و) break the word "
        "visually into pieces - use the breaks to find letter boundaries. "
        "Vowels are written, not guessed: ې is always the e of bed, ۀ is "
        "always the schwa ə, ۍ is the diphthong əy, so read them "
        "literally. Retroflex letters ټ ډ ړ ڼ are pronounced with the "
        "tongue tip curled back; ښ and ږ are the signature Pashto "
        "fricatives, pronounced x̌ and ǵ (in the south they soften to ʂ "
        "and ʐ, in the north they harden toward x and ɣ). څ is ts as in "
        "cats, ځ is dz as in adze. To write, start from the rightmost "
        "letter and join leftward, lifting the pen after any of the six "
        "right-joining-only letters. Numbers are written left to right "
        "within the right-to-left line, e.g. ۱۲۳."
    ),
    "key_points": [
        "44 letters, right to left; 12 letters are Pashto-specific: ټ ډ ړ ڼ ښ ږ څ ځ ې ۍ ئ ګ.",
        "Retroflex series ټ ṭ, ډ ḍ, ړ ṛ, ڼ ṇ: tongue tip curled back - the visual and audible signature of Pashto.",
        "Fricative pair ښ x̌ / ږ ǵ: soft in the south (ʂ/ʐ), hard in the north (x/ɣ); both are standard.",
        "Affricates څ ts and ځ dz; vowel carriers ې (e), ۍ (əy), ۀ (schwa ə), ئ (hamza-bearing ye).",
        "Six letters join only rightward (ا د ډ ذ ر ړ ز ژ ږ و); their gaps mark letter boundaries.",
        "Eastern Arabic numerals ۰۱۲۳۴۵۶۷۸۹; punctuation ۔ ، ؛ ؟ follows Perso-Arabic convention.",
        "Vowels are written explicitly - read ې ۍ ۀ ئ literally, never guessed.",
        "This database romanizes with x̌ ǵ ṭ ḍ ṛ ṇ ṣ̌ č ž š ə; the scheme is used on every record.",
    ],
    "requirements": [
        "Write each of the 44 letters until the retroflex and fricative shapes are automatic.",
        "Practice the right-to-left direction with joined forms, not isolated letters.",
        "Drill the ښ/ږ north-south split by ear so both dialect pronunciations are recognized.",
        "Learn the Eastern Arabic numerals ۰-۹ alongside the letters.",
    ],
    "standards": [
        "The 44-letter inventory follows the standard Pashto alphabet as codified in the cited grammars.",
        "Transliteration follows standard Pashto linguistic notation (x̌ ǵ ṭ ḍ ṛ ṇ č ž š ə).",
        "Numerals follow the Eastern Arabic set standard in Afghanistan and Pakistan.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats each of the 44 letters as a "
        "sworn sign with a fixed covenant: the retroflexes ټ ډ ړ ڼ are the "
        "four anchors of the tongue, ښ and ږ the twin winds of north and "
        "south, څ and ځ the paired gates of ts and dz. Learn the signs in "
        "order, write each until the hand remembers the covenant, and the "
        "script becomes a sealed system no eye can misread."
    ),
    "demo_key": "alphabet",
    "demo_data": {"letters": LETTERS_2, "count": 44},
})

# ---------------------------------------------------------------- record 3

PHON_3 = {
    "vowels": [
        ("ا", "a", "u in but"),
        ("آ", "ā", "a in father"),
        ("ې", "e", "e in bed"),
        ("ی", "i", "ee in see"),
        ("و", "o", "o in go"),
        ("و", "u", "oo in moon"),
        ("ۀ", "ə", "a in about"),
    ],
    "consonants": [
        ("ب", "b", "b in boy"), ("پ", "p", "p in pen"),
        ("ت", "t", "t in top"), ("ټ", "ṭ", "t with tongue curled back"),
        ("د", "d", "d in dog"), ("ډ", "ḍ", "d with tongue curled back"),
        ("ک", "k", "k in kite"), ("ګ", "g", "g in go"),
        ("ق", "q", "q - deep k in the throat"),
        ("ج", "j", "j in jam"), ("چ", "č", "ch in chair"),
        ("څ", "ts", "ts in cats"), ("ځ", "dz", "ds in adze"),
        ("س", "s", "s in sun"), ("ز", "z", "z in zoo"),
        ("ش", "š", "sh in ship"), ("ژ", "ž", "s in vision"),
        ("ښ", "x̌", "between sh and kh; south: sh-like ʂ"),
        ("ږ", "ǵ", "voiced x̌; south: zh-like ʐ"),
        ("خ", "x", "kh in loch"), ("غ", "ɣ", "voiced kh, gargled"),
        ("ف", "f", "f in fish"), ("و", "w", "w in water"),
        ("ی", "y", "y in yes"), ("ر", "r", "rolled r"),
        ("ړ", "ṛ", "retroflex flap r"), ("ل", "l", "l in lamp"),
        ("م", "m", "m in man"), ("ن", "n", "n in no"),
        ("ڼ", "ṇ", "n with tongue curled back"),
        ("ه", "h", "h in hat"), ("ع", "ʔ", "glottal stop, as in uh-oh"),
    ],
    "examples": [
        ("ښځه", "x̌əza", "woman", "the signature fricative ښ"),
        ("ډوډۍ", "ḍoḍəi", "bread", "retroflex ډ"),
        ("څښل", "tsṣ̌əl", "to drink", "affricate څ"),
        ("ځمکه", "dzməka", "earth", "affricate ځ"),
        ("ږیره", "ǵira", "beard", "voiced fricative ږ"),
        ("سپوږمۍ", "spoǧməi", "moon", "diphthong ۍ"),
        ("لمر", "lmar", "sun", "consonant cluster lm"),
        ("ورځ", "wrədz", "day", "cluster wr + dz"),
        ("پښتو", "paʂto", "Pashto", "the name of the language"),
        ("کور", "kor", "house", "plain o vowel"),
        ("اوبه", "obə", "water", "schwa ending"),
        ("ماشوم", "māšum", "child", "long ā"),
    ],
}

ENTRIES.append({
    "key": "p03_phonology",
    "name": "Pashto Pronunciation and Phonology",
    "group": "Foundations",
    "ladder_rank": 3,
    "ladder_tier": "foundations",
    "description": (
        "Pashto has 7 vowels (a ā e i o u ə) and about 30 consonants, "
        "including the retroflex series ṭ ḍ ṇ ṛ and the postalveolar "
        "fricative pair x̌/ǵ that mark the famous north-south dialect "
        "split. Southern (Kandahar) speakers pronounce ښ as ʂ and ږ as ʐ "
        "(soft, sh-like); Northern (Peshawar) speakers pronounce them "
        "closer to x and ɣ (hard). Both are fully standard. Stress most "
        "commonly falls on the final syllable of the word, with dialect "
        "variation; unlike some neighbors, Pashto has no tones. Consonant "
        "clusters are common at word beginnings (لمر lmar - sun, ورځ wrədz "
        "- day). The affricates څ (ts) and ځ (dz) are single sounds. The "
        "schwa ə (ۀ) is a full vowel, not a reduced afterthought - اوبه "
        "(obə - water) ends in a clear ə. The table below gives every sound "
        "with an English approximation, followed by 12 spoken-example words."
    ),
    "how_it_works": (
        "Build each sound from the English approximation, then adjust. For "
        "the retroflexes ټ ډ ړ ڼ, curl the tongue tip back to touch behind "
        "the tooth ridge while making t/d/r/n - the resulting hollow sound "
        "is unmistakable. For ښ, start from sh and pull the tongue slightly "
        "back and up; for ږ, do the same with voice. For څ say cats without "
        "the ca, for ځ say adze without the a. Keep the schwa ə short and "
        "central, like the a in about. Put the stress on the last syllable "
        "unless a native speaker corrects you - final stress is the safe "
        "default. Listen for the north/south split and imitate your "
        "teacher's side; do not mix ښ as ʂ in one word and x in the next. "
        "Practice the 12 example words aloud until the clusters (lm, wr, "
        "dz) flow without inserting extra vowels."
    ),
    "key_points": [
        "7 vowels: a ā e i o u ə; the schwa ə (ۀ) is a full vowel - اوبه (obə - water).",
        "Retroflex series ṭ ḍ ṇ ṛ: tongue tip curled back - ټوپک (ṭopak - rifle), ډوډۍ (ḍoḍəi - bread).",
        "Postalveolar pair ښ x̌ / ږ ǵ: soft ʂ/ʐ in the south, hard x/ɣ in the north; both standard.",
        "Affricates څ ts and ځ dz are single sounds - څښل (tsṣ̌əl - to drink), ځمکه (dzməka - earth).",
        "Stress defaults to the final syllable; Pashto has no tones.",
        "Initial consonant clusters are normal: لمر (lmar - sun), ورځ (wrədz - day).",
        "The diphthong ۍ (əy) - سپوږمۍ (spoǧməi - moon) - is a signature Pashto ending.",
        "Pick one dialect side for ښ/ږ and stay consistent while learning.",
    ],
    "requirements": [
        "Master the retroflex tongue position before moving to vocabulary records.",
        "Drill the 12 example words aloud until clusters flow without inserted vowels.",
        "Train the ear on the north/south ښ/ږ split with both pronunciations.",
        "Keep stress on the final syllable as the default.",
    ],
    "standards": [
        "Sound descriptions follow the phonological analyses in the cited grammars.",
        "The north/south realization of ښ/ږ follows the standard dialectological description.",
        "Transliteration matches the scheme fixed in record 2.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats the mouth as an instrument of "
        "seven strings (the vowels) and thirty hammers (the consonants). "
        "The retroflexes are the deep drums, ښ and ږ the twin winds, څ and "
        "ځ the paired gates. Tune each sound against its English "
        "approximation, then seal the covenant: one dialect side, final "
        "stress, no inserted vowels. A sealed instrument never misplays."
    ),
    "demo_key": "phonology",
    "demo_data": PHON_3,
})

# ---------------------------------------------------------------- record 4

NOUNS_4 = [
    ("سړی", "saṛay", "man", "دا یو ښه سړی دی", "dā yaw x̌a saṛay day", "This is a good man."),
    ("ښځه", "x̌əza", "woman", "هغه یوه مهربانه ښځه ده", "haɣa yawa mehrabāna x̌əza da", "She is a kind woman."),
    ("ماشوم", "māšum", "child", "ماشوم لوبې کوي", "māšum lobe kawi", "The child is playing."),
    ("کور", "kor", "house/home", "زموږ کور لوی دی", "zmuẓ̌ kor loy day", "Our house is big."),
    ("اوبه", "obə", "water", "اوبه ساړې دي", "obə sāṛe di", "The water is cold."),
    ("ډوډۍ", "ḍoḍəi", "bread", "مور ډوډۍ پخوي", "mor ḍoḍəi paxawi", "Mother bakes bread."),
    ("کتاب", "kitāb", "book", "دا زما کتاب دی", "dā zmā kitāb day", "This is my book."),
    ("ښوونځی", "x̌owənǵay", "school", "ماشومان ښوونځي ته ځي", "māšumān x̌owənǵi ta dzi", "The children go to school."),
    ("ښار", "x̌ār", "city", "پېښور یو لوی ښار دی", "pex̌awar yaw loy x̌ār day", "Peshawar is a big city."),
    ("کلی", "kalay", "village", "زموږ کلی ښکلی دی", "zmuẓ̌ kalay x̌kulay day", "Our village is beautiful."),
    ("لار", "lār", "road/way", "دا لار ښار ته ځي", "dā lār x̌ār ta dzi", "This road goes to the city."),
    ("ورځ", "wrədz", "day", "نن ښه ورځ ده", "nən x̌a wrədz da", "Today is a good day."),
    ("شپه", "špa", "night", "شپه تیاره ده", "špa tyāra da", "The night is dark."),
    ("لمر", "lmar", "sun", "لمر راخېژي", "lmar rāxeǵi", "The sun is rising."),
    ("سپوږمۍ", "spoǧməi", "moon", "سپوږمۍ رڼا کوي", "spoǧməi raṇā kawi", "The moon gives light."),
    ("ستوری", "storay", "star", "ستوری ځلېږي", "storay dzaleǵi", "The star is shining."),
    ("اسمان", "āsmān", "sky", "اسمان شین دی", "āsmān šin day", "The sky is blue."),
    ("ځمکه", "dzməka", "earth/land", "ځمکه شنه ده", "dzməka šna da", "The land is green."),
    ("غر", "ɣar", "mountain", "هغه غر لوړ دی", "haɣa ɣar lwaṛ day", "That mountain is high."),
    ("سیند", "sind", "river", "سیند ژور دی", "sind žwar day", "The river is deep."),
    ("ونه", "wəṇa", "tree", "دا ونه زړه ده", "dā wəṇa zaṛa da", "This tree is old."),
    ("سپی", "spay", "dog", "سپی غاپي", "spay ɣāpi", "The dog barks."),
    ("پیشو", "pišo", "cat", "پیشو شیدې څښي", "pišo šide tsṣ̌i", "The cat drinks milk."),
    ("اس", "ās", "horse", "اس چټک ځي", "ās čaṭak dzi", "The horse goes fast."),
    ("پیسې", "payse", "money", "پیسې په جېب کې دي", "payse pə jeb ke di", "The money is in the pocket."),
]

ENTRIES.append({
    "key": "p04_nouns",
    "name": "Pashto Core Nouns I",
    "group": "Foundations",
    "ladder_rank": 4,
    "ladder_tier": "foundations",
    "description": (
        "Twenty-five essential Pashto nouns - people, places, and things - "
        "each with transliteration, English meaning, and a full example "
        "sentence translated into English. The set covers the human core "
        "(سړی saṛay - man, ښځه x̌əza - woman, ماشوم māšum - child), the "
        "home (کور kor - house, ډوډۍ ḍoḍəi - bread, اوبه obə - water), "
        "learning (کتاب kitāb - book, ښوونځی x̌owənǵay - school), the "
        "landscape (ښار x̌ār - city, کلی kalay - village, لار lār - road, "
        "غر ɣar - mountain, سیند sind - river), time and sky (ورځ wrədz - "
        "day, شپه špa - night, لمر lmar - sun, سپوږمۍ spoǧməi - moon, "
        "ستوری storay - star, اسمان āsmān - sky, ځمکه dzməka - earth), and "
        "animals and value (ونه wəṇa - tree, سپی spay - dog, پیشو pišo - "
        "cat, اس ās - horse, پیسې payse - money). Note the gender pattern "
        "already visible: words ending in ی tend to be masculine (سړی, "
        "ښوونځی, سپی) and words ending in ه tend to be feminine (ښځه, "
        "ډوډۍ, ورځ, شپه, ځمکه, ونه)."
    ),
    "how_it_works": (
        "Learn each noun together with its gender and its plural - the "
        "plural is where Pashto shows its variety (کتابونه kitābuna - "
        "books, سړي saṛi - men, ښځې x̌əze - women, ورځې wrədze - days). "
        "Use the example sentence as the memory anchor: say the Pashto "
        "sentence aloud, then the English, until the noun sits inside a "
        "real utterance. Masculine nouns take دی (day - is) and feminine "
        "nouns take ده (da - is): کور لوی دی (kor loy day - the house is "
        "big) but ښځه مهربانه ده (x̌əza mehrabāna da - the woman is kind). "
        "This masculine/feminine split in the verb 'to be' is your constant "
        "gender drill - every sentence below practices it."
    ),
    "key_points": [
        "25 essential nouns: people, home, learning, landscape, sky, animals, value - each with a translated example sentence.",
        "Gender is visible in the endings: -ی often masculine, -ه often feminine; learn the exceptions as you meet them.",
        "The verb 'to be' agrees: masculine دی (day), feminine ده (da) - a built-in gender drill in every sentence.",
        "Learn every noun with its plural: کتابونه (books), سړي (men), ښځې (women), ورځې (days).",
        "Core human nouns: سړی (man), ښځه (woman), ماشوم (child); core home nouns: کور, اوبه, ډوډۍ.",
        "Landscape set: ښار, کلی, لار, غر, سیند; sky set: لمر, سپوږمۍ, ستوری, اسمان, ورځ, شپه.",
        "All 25 nouns reappear in the themed sentence records 11-20, so this record compounds forward.",
    ],
    "requirements": [
        "Say each noun inside its example sentence, not as an isolated word.",
        "Mark the gender of every noun in your notes from this record onward.",
        "Learn the plural of each noun alongside the singular.",
        "Drill دی/ده agreement until the gender of each noun is automatic.",
    ],
    "standards": [
        "Noun glosses follow standard Pashto-English lexicography.",
        "Gender assignments follow the standard grammatical description in the cited references.",
        "Example sentences use standard written Pashto (Northern-based).",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method builds the noun as the first sworn "
        "sign: each of the 25 is a named thing with a covenant of gender. "
        "Masculine signs seal with دی, feminine signs seal with ده - the "
        "seal never lies. Learn each sign with its plural shadow and its "
        "sentence dwelling, and the 25 become the foundation stones of "
        "every dwelling you will build in the language."
    ),
    "demo_key": "vocab",
    "demo_data": {"kind": "nouns", "words": NOUNS_4},
})

# ---------------------------------------------------------------- record 5

VERBS_5 = [
    ("تلل", "tləl", "to go", "زه ښوونځي ته ځم", "zə x̌owənǵi ta dzəm", "I go to school."),
    ("راتلل", "rātləl", "to come", "هغه سبا راځي", "haɣa sabā rādzi", "He is coming tomorrow."),
    ("کول", "kawəl", "to do", "ته څه کوې؟", "tə tsə kawe", "What are you doing?"),
    ("ویل", "wayəl", "to say", "هغه رښتیا وايي", "haɣa rəxtyā wāyi", "He speaks the truth."),
    ("خوړل", "xoṛəl", "to eat", "موږ ډوډۍ خورو", "muẓ̌ ḍoḍəi xoru", "We eat bread."),
    ("څښل", "tsṣ̌əl", "to drink", "زه چای څښم", "zə čāy tsṣ̌əm", "I drink tea."),
    ("لیدل", "lidəl", "to see", "زه تا وینم", "zə tā winəm", "I see you."),
    ("اورېدل", "awredəl", "to hear", "زه غږ اورم", "zə ɣaǵ awrəm", "I hear the voice."),
    ("پوهېدل", "pohedəl", "to understand", "زه پوهېږم", "zə poheǵəm", "I understand."),
    ("لوستل", "lwastəl", "to read", "هغه کتاب لولي", "haɣa kitāb loli", "He reads the book."),
    ("لیکل", "likəl", "to write", "زه لیک لیکم", "zə lik likəm", "I write a letter."),
    ("اخیستل", "axistəl", "to take", "کتاب واخله", "kitāb wāxla", "Take the book."),
    ("ورکول", "warkawəl", "to give", "هغه ماته ډالۍ راکوي", "haɣa māta ḍāləi rākawi", "He gives me a gift."),
    ("جوړول", "joṛawəl", "to make/build", "پلار کور جوړوي", "plār kor joṛawi", "Father builds the house."),
    ("کار کول", "kār kawəl", "to work", "زه په دفتر کې کار کوم", "zə pə daftar ke kār kawəm", "I work in the office."),
    ("زده کول", "zda kawəl", "to learn", "زه پښتو زده کوم", "zə paʂto zda kawəm", "I learn Pashto."),
    ("خوب کول", "xob kawəl", "to sleep", "ماشوم خوب کوي", "māšum xob kawi", "The child sleeps."),
    ("کېناستل", "kenāstəl", "to sit", "دلته کېنه", "dalta kena", "Sit here."),
    ("درېدل", "dredəl", "to stand", "هغه ودرېد", "haɣa wadred", "He stood up."),
    ("ګرځېدل", "gərdzedəl", "to walk", "موږ په باغ کې ګرځو", "muẓ̌ pə bāɣ ke gərdzu", "We walk in the garden."),
    ("مینځل", "mindzəl", "to wash", "لاسونه ومینځه", "lāsuna womindza", "Wash your hands."),
    ("پخول", "paxawəl", "to cook", "مور خواړه پخوي", "mor xwāṛə paxawi", "Mother cooks the food."),
    ("پرانیستل", "prānistəl", "to open", "دروازه پرانیزه", "darwāza prāniza", "Open the door."),
    ("تړل", "taṛəl", "to close", "کړکۍ وتړه", "kəṛkəi watṛa", "Close the window."),
    ("مرسته کول", "mrasta kawəl", "to help", "له ما سره مرسته وکړه", "lə mā sara mrasta wakṛa", "Help me."),
]

ENTRIES.append({
    "key": "p05_verbs",
    "name": "Pashto Core Verbs I",
    "group": "Foundations",
    "ladder_rank": 5,
    "ladder_tier": "foundations",
    "description": (
        "Twenty-five essential Pashto verbs - every infinitive ends in -ل "
        "(-əl) - each with transliteration, English meaning, and a full "
        "example sentence translated into English. The set covers motion "
        "(تلل tləl - to go, راتلل rātləl - to come, ګرځېدل gərdzedəl - to "
        "walk, درېدل dredəl - to stand, کېناستل kenāstəl - to sit), core "
        "actions (کول kawəl - to do, ویل wayəl - to say, اخیستل axistəl - "
        "to take, ورکول warkawəl - to give, جوړول joṛawəl - to make), the "
        "senses and mind (لیدل lidəl - to see, اورېدل awredəl - to hear, "
        "پوهېدل pohedəl - to understand, لوستل lwastəl - to read, لیکل "
        "likəl - to write, زده کول zda kawəl - to learn), the body "
        "(خوړل xoṛəl - to eat, څښل tsṣ̌əl - to drink, خوب کول xob kawəl - "
        "to sleep, مینځل mindzəl - to wash, پخول paxawəl - to cook), and "
        "daily commands (پرانیستل prānistəl - to open, تړل taṛəl - to close, "
        "مرسته کول mrasta kawəl - to help). Compound verbs with کول (to do) "
        "are everywhere in Pashto: کار کول (to work), زده کول (to learn), "
        "مرسته کول (to help) - learn the pattern once and hundreds of verbs "
        "open up."
    ),
    "how_it_works": (
        "Every verb below shows its infinitive and one living sentence. "
        "Notice how the verb sits at the END of the sentence - Pashto is "
        "subject-object-verb: زه چای څښم (zə čāy tsṣ̌əm - I drink tea) is "
        "literally 'I tea drink'. Notice the کول compounds: noun + کول "
        "makes a verb (کار + کول = to work), and the noun carries the "
        "meaning while کول carries the conjugation. Imperatives in the "
        "examples (واخله - take!, وتړه - close!, ومینځه - wash!) show the "
        "command form, built from the present stem. Learn each verb inside "
        "its sentence; record 21 will conjugate تلل fully through present, "
        "past, and future so the stem system becomes visible."
    ),
    "key_points": [
        "25 essential verbs, all infinitives ending in -ل (-əl), each with a translated example sentence.",
        "Verb-final word order: the verb sits at the end - زه چای څښم is literally 'I tea drink'.",
        "کول (kawəl - to do) builds compound verbs: کار کول (work), زده کول (learn), مرسته کول (help), خوب کول (sleep).",
        "Motion core: تلل/راتلل (go/come), ګرځېدل (walk), درېدل (stand), کېناستل (sit).",
        "Mind core: پوهېدل (understand), زده کول (learn), لوستل (read), لیکل (write), ویل (say).",
        "Command forms appear in the examples: واخله (take!), پرانیزه (open!), وتړه (close!).",
        "Record 21 conjugates these verbs through present, past, and future - the full stem system.",
    ],
    "requirements": [
        "Learn each verb with its infinitive and one full sentence, never the bare gloss.",
        "Practice the کول compound pattern until new noun+کول verbs are recognized on sight.",
        "Keep verbs at the end of your own sentences from this record onward.",
        "Drill the five imperative examples aloud as commands.",
    ],
    "standards": [
        "Verb glosses follow standard Pashto-English lexicography.",
        "Infinitives are cited in the standard -ل (-əl) form.",
        "Example sentences use standard written Pashto (Northern-based).",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats each verb as a living action "
        "with a sworn shape: the -ل infinitive is the action at rest, the "
        "sentence is the action awake. کول is the great awakener - attach "
        "it to any noun and a new action stands up. Learn the 25 actions "
        "awake inside their sentences, keep every action at the end where "
        "it belongs, and the language moves when you move it."
    ),
    "demo_key": "vocab",
    "demo_data": {"kind": "verbs", "words": VERBS_5},
})

# ---------------------------------------------------------------- record 6

ADJ_6 = [
    ("لوی", "loy", "big", "دا یو لوی کور دی", "dā yaw loy kor day", "This is a big house."),
    ("کوچنی", "kučnay", "small", "کوچنی ماشوم ژاړي", "kučnay māšum žāṛi", "The small child cries."),
    ("نوی", "naway", "new", "زما نوی کتاب ښه دی", "zmā naway kitāb x̌a day", "My new book is good."),
    ("زوړ", "zoṛ", "old", "دا زوړ کلی دی", "dā zoṛ kalay day", "This is an old village."),
    ("ښه", "x̌a", "good", "ښه سړی مرسته کوي", "x̌a saṛay mrasta kawi", "A good man helps."),
    ("بد", "bad", "bad", "بد عادت پرېږده", "bad ādat preǵda", "Leave the bad habit."),
    ("ګرم", "garam", "hot", "چای ګرم دی", "čāy garam day", "The tea is hot."),
    ("ساړه", "sāṛa", "cold", "اوبه ساړې دي", "obə sāṛe di", "The water is cold."),
    ("اوږد", "uǧd", "long", "دا یوه اوږده لار ده", "dā yawa uǧda lār da", "This is a long road."),
    ("لنډ", "lanḍ", "short", "لنډه کیسه ووایه", "lanḍa kisa wuwāya", "Tell a short story."),
    ("لوړ", "lwaṛ", "high/tall", "غر لوړ دی", "ɣar lwaṛ day", "The mountain is high."),
    ("ټیټ", "ṭiṭ", "low", "ټیټ دېوال مه جوړوه", "ṭiṭ dewāl ma joṛawa", "Do not build a low wall."),
    ("ژور", "žwar", "deep", "سیند ژور دی", "sind žwar day", "The river is deep."),
    ("درون", "drund", "heavy", "دا بکس دروند دی", "dā baks drund day", "This box is heavy."),
    ("سپک", "spak", "light", "سپکه بکس واخله", "spaka baks wāxla", "Take the light box."),
    ("چټک", "čaṭak", "fast", "اس چټک دی", "ās čaṭak day", "The horse is fast."),
    ("ورو", "wro", "slow", "ورو ګرځه", "wro gərdza", "Walk slowly."),
    ("پاک", "pāk", "clean", "لاسونه پاک دي", "lāsuna pāk di", "The hands are clean."),
    ("چټل", "čaṭal", "dirty", "چټلې جامې ومینځه", "čaṭale jāme womindza", "Wash the dirty clothes."),
    ("خوشحاله", "xošhāla", "happy", "ماشوم خوشحاله دی", "māšum xošhāla day", "The child is happy."),
    ("خفه", "xafa", "sad", "هغه نن خفه ده", "haɣa nən xafa da", "She is sad today."),
    ("ناروغ", "nāroɣ", "sick", "پلار ناروغ دی", "plār nāroɣ day", "Father is sick."),
    ("روغ", "roɣ", "healthy", "ماشوم روغ دی", "māšum roɣ day", "The child is healthy."),
    ("خوږ", "xoǵ", "sweet", "مڼه خوږه ده", "maṇa xoǵa da", "The apple is sweet."),
    ("تریخ", "trix", "bitter", "دا درمل تریخ دی", "dā darmal trix day", "This medicine is bitter."),
]

ADV_6 = [
    ("ډېر", "ḍer", "very/much", "زه ډېر خوشحاله یم", "zə ḍer xošhāla yəm", "I am very happy."),
    ("لږ", "ləǵ", "little", "لږې اوبه راکړه", "ləǵe obə rākṛa", "Give me a little water."),
    ("ژر", "žər", "soon/quickly", "ژر راشه", "žər rāša", "Come quickly."),
    ("تل", "təl", "always", "هغه تل رښتیا وايي", "haɣa təl rəxtyā wāyi", "He always speaks the truth."),
    ("هېڅکله", "heṣkala", "never", "زه هېڅکله نه ځم", "zə heṣkala nə dzəm", "I never go."),
    ("نن", "nən", "today", "نن ښه ورځ ده", "nən x̌a wrədz da", "Today is a good day."),
    ("پرون", "parun", "yesterday", "پرون باران وورېد", "parun bārān woreḏ", "It rained yesterday."),
    ("سبا", "sabā", "tomorrow", "سبا به ځو", "sabā bə dzu", "We will go tomorrow."),
    ("دلته", "dalta", "here", "دلته کېنه", "dalta kena", "Sit here."),
    ("هلته", "halta", "there", "هلته مه ځه", "halta ma dza", "Do not go there."),
    ("څنګه", "tsənga", "how", "څنګه یې؟", "tsənga ye", "How are you?"),
    ("ولې", "walə", "why", "ولې ژاړې؟", "walə žāṛe", "Why are you crying?"),
    ("کله", "kəla", "when", "کله راځې؟", "kəla rādze", "When are you coming?"),
    ("بیا", "byā", "again", "بیا ووایه", "byā wuwāya", "Say it again."),
    ("اوس", "os", "now", "اوس کار وکړه", "os kār wakṛa", "Work now."),
]

ENTRIES.append({
    "key": "p06_adjectives",
    "name": "Pashto Adjectives and Adverbs",
    "group": "Foundations",
    "ladder_rank": 6,
    "ladder_tier": "foundations",
    "description": (
        "Twenty-five adjectives and fifteen adverbs - each with "
        "transliteration, English meaning, and a full example sentence "
        "translated into English. The adjectives cover size (لوی loy - big, "
        "کوچنی kučnay - small), age (نوی naway - new, زوړ zoṛ - old), "
        "quality (ښه x̌a - good, بد bad - bad), temperature (ګرم garam - "
        "hot, ساړه sāṛa - cold), dimension (اوږد uǧd - long, لنډ lanḍ - "
        "short, لوړ lwaṛ - high, ټیټ ṭiṭ - low, ژور žwar - deep), weight "
        "(درون drund - heavy, سپک spak - light), speed (چټک čaṭak - fast, "
        "ورو wro - slow), cleanliness (پاک pāk - clean, چټل čaṭal - "
        "dirty), feeling (خوشحاله xošhāla - happy, خفه xafa - sad), health "
        "(ناروغ nāroɣ - sick, روغ roɣ - healthy), and taste (خوږ xoǵ - "
        "sweet, تریخ trix - bitter). The adverbs cover degree (ډېر ḍer - "
        "very, لږ ləǵ - little), time (ژر žər - soon, تل təl - always, "
        "هېڅکله heṣkala - never, نن nən - today, پرون parun - yesterday, "
        "سبا sabā - tomorrow, اوس os - now, بیا byā - again), place (دلته "
        "dalta - here, هلته halta - there), and question words used as "
        "adverbs (څنګه tsənga - how, ولې walə - why, کله kəla - when). "
        "Agreement rule: attributive adjectives agree with their noun in "
        "gender - لوی سړی (loy saṛay - big man, masculine) but لویه ښځه "
        "(loya x̌əza - big woman, feminine)."
    ),
    "how_it_works": (
        "Adjectives come BEFORE the noun they describe: نوی کتاب (naway "
        "kitāb - new book). In the attributive position many adjectives "
        "take a feminine form before feminine nouns: لوی/لویه (loy/loya), "
        "نوی/نوې (naway/nawe), خوږ/خوږه (xoǵ/xoǵa) - watch the sentence "
        "pairs below for the pattern. In the predicate position (after the "
        "verb 'to be') the adjective agrees with the subject's gender: "
        "کور لوی دی (kor loy day - the house is big, masculine) but ونه "
        "لویه ده (wəṇa loya da - the tree is big, feminine). Adverbs do not "
        "change: ډېر (ḍer - very) and ژر (žər - quickly) keep one form "
        "everywhere, and they sit before the word they modify: ډېر ښه "
        "(ḍer x̌a - very good). Negation wraps the verb, not the adjective: "
        "زه هېڅکله نه ځم (zə heṣkala nə dzəm - I never go)."
    ),
    "key_points": [
        "25 adjectives + 15 adverbs, each with a translated example sentence - 40 modifiers total.",
        "Adjectives precede the noun: نوی کتاب (new book); they agree in gender - لوی سړی but لویه ښځه.",
        "Predicate adjectives agree with the subject: کور لوی دی (masc.) vs ونه لویه ده (fem.).",
        "Adverbs never change form and sit before what they modify: ډېر ښه (very good).",
        "Core pairs: لوی/کوچنی, نوی/زوړ, ښه/بد, ګرم/ساړه, چټک/ورو, پاک/چټل, خوشحاله/خفه.",
        "Time adverbs نن/پرون/سبا (today/yesterday/tomorrow) anchor every tense you will learn.",
        "Question adverbs څنګه/ولې/کله (how/why/when) power record 22's questions.",
    ],
    "requirements": [
        "Learn each adjective in both masculine and feminine form where the pair is shown.",
        "Place adjectives before nouns and adverbs before verbs in your own sentences.",
        "Drill the دی/ده agreement with predicate adjectives until it is automatic.",
        "Use نن/پرون/سبا in daily practice sentences to anchor time.",
    ],
    "standards": [
        "Adjective glosses follow standard Pashto-English lexicography.",
        "Agreement patterns follow the standard grammatical description in the cited references.",
        "Example sentences use standard written Pashto (Northern-based).",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats each adjective as a color "
        "sealed onto its noun: the color shifts with the covenant of "
        "gender - لوی on a masculine stone, لویه on a feminine one - but "
        "the color itself never lies. Adverbs are the unchanging winds: "
        "ډېر, ژر, تل blow the same from every direction. Seal each of the "
        "40, pair each color with its stone, and description becomes "
        "covenant."
    ),
    "demo_key": "vocab",
    "demo_data": {"kind": "modifiers", "words": ADJ_6 + ADV_6},
})

# ---------------------------------------------------------------- record 7

PRON_7 = {
    "Personal pronouns": [
        ("زه", "zə", "I", "زه پښتو زده کوم", "zə paʂto zda kawəm", "I learn Pashto."),
        ("ته", "tə", "you (singular, familiar)", "ته څه کوې؟", "tə tsə kawe", "What are you doing?"),
        ("هغه", "haɣa", "he/she/that", "هغه ښوونکی دی", "haɣa x̌owunkay day", "He is a teacher."),
        ("موږ", "muẓ̌", "we", "موږ ملګري یو", "muẓ̌ malgəri yu", "We are friends."),
        ("تاسې", "tāsə", "you (plural/formal)", "تاسې ښه راغلاست", "tāsə x̌a rāɣlāst", "Welcome (to you)."),
        ("هغوی", "haɣwi", "they", "هغوی لوبې کوي", "haɣwi lobe kawi", "They are playing."),
    ],
    "Possessive pronouns": [
        ("زما", "zmā", "my", "دا زما کتاب دی", "dā zmā kitāb day", "This is my book."),
        ("ستا", "stā", "your (singular)", "ستا نوم څه دی؟", "stā num tsə day", "What is your name?"),
        ("د هغه", "də haɣa", "his/her", "دا د هغه کور دی", "dā də haɣa kor day", "This is his house."),
        ("زموږ", "zmuẓ̌", "our", "زموږ کلی ښکلی دی", "zmuẓ̌ kalay x̌kulay day", "Our village is beautiful."),
        ("ستاسې", "stāsə", "your (plural/formal)", "ستاسې مور ښه ده", "stāsə mor x̌a da", "Your mother is well."),
        ("د هغوی", "də haɣwi", "their", "دا د هغوی موټر دی", "dā də haɣwi moṭar day", "This is their car."),
    ],
    "Demonstrative pronouns": [
        ("دا", "dā", "this", "دا څه دی؟", "dā tsə day", "What is this?"),
        ("هغه", "haɣa", "that", "هغه لېره ده", "haɣa lera da", "That is far."),
        ("دغه", "daɣa", "this (aforementioned)", "دغه سړی زما ملګری دی", "daɣa saṛay zmā malgaray day", "This man is my friend."),
        ("دوی", "dwi", "these (people)", "دوی زده کوونکي دي", "dwi zda kawunki di", "These are students."),
        ("هغو", "haɣo", "those", "هغو ته وګوره", "haɣo ta wagora", "Look at those."),
    ],
    "Interrogative pronouns": [
        ("څوک", "tsok", "who", "څوک راغی؟", "tsok rāɣay", "Who came?"),
        ("څه", "tsə", "what", "دا څه دی؟", "dā tsə day", "What is this?"),
        ("کوم", "kum", "which", "کوم کتاب غواړې؟", "kum kitāb ɣwāṛe", "Which book do you want?"),
        ("څومره", "tsumra", "how much/many", "څومره پیسې لرې؟", "tsumra payse lare", "How much money do you have?"),
        ("چېرته", "čerta", "where", "ته چېرته ځې؟", "tə čerta dze", "Where are you going?"),
        ("کله", "kəla", "when", "کله راځې؟", "kəla rādze", "When are you coming?"),
    ],
}

ENTRIES.append({
    "key": "p07_pronouns",
    "name": "Pashto Pronouns",
    "group": "Foundations",
    "ladder_rank": 7,
    "ladder_tier": "foundations",
    "description": (
        "The full Pashto pronoun system in four paradigms, each form with "
        "transliteration, English meaning, and a translated example "
        "sentence. Personal: زه (zə - I), ته (tə - you singular familiar), "
        "هغه (haɣa - he/she), موږ (muẓ̌ - we), تاسې (tāsə - you plural and "
        "formal singular), هغوی (haɣwi - they). Possessive: زما (zmā - my), "
        "ستا (stā - your singular), د هغه (də haɣa - his/her), زموږ "
        "(zmuẓ̌ - our), ستاسې (stāsə - your plural/formal), د هغوی (də "
        "haɣwi - their). Demonstrative: دا (dā - this), هغه (haɣa - that), "
        "دغه (daɣa - this aforementioned), دوی (dwi - these people), هغو "
        "(haɣo - those). Interrogative: څوک (tsok - who), څه (tsə - what), "
        "کوم (kum - which), څومره (tsumra - how much/many), چېرته (čerta - "
        "where), کله (kəla - when). Note that هغه does triple duty as "
        "he/she, that, and (with د) his/her - context disambiguates."
    ),
    "how_it_works": (
        "Personal pronouns drop freely because the verb ending already "
        "shows the person: پوهېږم (poheǵəm - I understand) needs no زه, but "
        "زه پوهېږم adds emphasis ('I myself understand'). In past-tense "
        "transitive clauses the ergative rule changes the pronoun: زه "
        "becomes ما (mā), ته becomes تا (tā) - ما کتاب ولوست (mā kitāb "
        "walwast - I read the book). ته is familiar singular; use تاسې for "
        "elders, strangers, and groups - the politeness rule of record 29 "
        "starts here. Possessives sit before the noun like adjectives: زما "
        "کتاب (zmā kitāb - my book). هغه as 'he/she' takes masculine or "
        "feminine agreement from context: هغه ښه دی (he is good) vs هغه "
        "ښه ده (she is good). Interrogatives open the question and the verb "
        "stays at the end: ته چېرته ځې؟ (tə čerta dze - where are you "
        "going?)."
    ),
    "key_points": [
        "Four paradigms: personal, possessive, demonstrative, interrogative - 23 forms with translated sentences.",
        "ته is familiar singular; تاسې is plural AND formal singular - the politeness foundation.",
        "Pronouns drop when the verb ending is clear; kept pronouns add emphasis.",
        "Past-tense ergative shift: زه → ما, ته → تا in transitive past clauses - ما کتاب ولوست.",
        "هغه does triple duty: he/she, that, and (with د) his/her - context disambiguates.",
        "Possessives precede the noun: زما کتاب, ستاسې مور, د هغوی موټر.",
        "Interrogatives front the question with the verb at the end: څوک راغی؟ (who came?).",
    ],
    "requirements": [
        "Drill all six personal pronouns with the verb 'to be' forms (یم، یې، دی/ده، یو، یئ، دي).",
        "Practice the ما/تا ergative shift with past-tense transitive verbs.",
        "Default to تاسې with strangers and elders until invited to ته.",
        "Learn the interrogatives cold - they drive record 22.",
    ],
    "standards": [
        "Paradigms follow the standard grammatical description in the cited references.",
        "The ما/تا ergative forms follow the standard account of Pashto split ergativity.",
        "Example sentences use standard written Pashto (Northern-based).",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats the pronouns as the sworn "
        "circle of speakers: زه the self, ته the familiar, تاسې the "
        "honored, موږ the sworn company. In the past tense the circle "
        "turns - زه becomes ما, the doer bowing into the oblique before the "
        "deed is done. Learn the circle, learn the turning, and every "
        "sentence knows exactly who stands where."
    ),
    "demo_key": "paradigm",
    "demo_data": {"title": "Pashto pronoun paradigms", "tables": PRON_7},
})

# ---------------------------------------------------------------- record 8

NUM_8 = {
    "units": [
        ("یو", "yaw", "1"), ("دوه", "dwa", "2"), ("درې", "dre", "3"),
        ("څلور", "tsalor", "4"), ("پنځه", "pindzə", "5"),
        ("شپږ", "špaǵ", "6"), ("اووه", "owə", "7"), ("اته", "atə", "8"),
        ("نهه", "nəhə", "9"), ("لس", "las", "10"),
    ],
    "teens": [
        ("یوولس", "yawolas", "11"), ("دولس", "dwolas", "12"),
        ("دیارلس", "dyārlas", "13"), ("څوارلس", "tswārlas", "14"),
        ("پنځلس", "pindzəlas", "15"), ("شپاړس", "špāṛas", "16"),
        ("اووهلس", "owəlas", "17"), ("اتلس", "atlas", "18"),
        ("نولس", "nolas", "19"),
    ],
    "tens": [
        ("شل", "šəl", "20"), ("دېرش", "derš", "30"),
        ("څلوېښت", "tsalwext", "40"), ("پنځوس", "pandzos", "50"),
        ("شپېته", "špetə", "60"), ("اویا", "awyā", "70"),
        ("اتیا", "atyā", "80"), ("نوي", "nawi", "90"),
        ("سل", "səl", "100"),
    ],
    "ordinals": [
        ("لومړی", "lumṛay", "first"), ("دوهم", "dwahəm", "second"),
        ("درېیم", "dreyəm", "third"),
    ],
    "days": [
        ("شنبه", "šamba", "Saturday"), ("یکشنبه", "yakšamba", "Sunday"),
        ("دوشنبه", "dwašamba", "Monday"), ("سه شنبه", "sešamba", "Tuesday"),
        ("چهارشنبه", "čāršamba", "Wednesday"),
        ("پنجشنبه", "pandzšamba", "Thursday"), ("جمعه", "juma", "Friday"),
    ],
    "months": [
        ("حمل", "hamal", "Aries/Farvardin"), ("ثور", "sawr", "Taurus"),
        ("جوزا", "jawzā", "Gemini"), ("سرطان", "saraṭān", "Cancer"),
        ("اسد", "asad", "Leo"), ("سنبله", "sumbula", "Virgo"),
        ("میزان", "mizān", "Libra"), ("عقرب", "aqrab", "Scorpio"),
        ("قوس", "qaws", "Sagittarius"), ("جدی", "jadi", "Capricorn"),
        ("دلو", "dalw", "Aquarius"), ("حوت", "hut", "Pisces"),
    ],
    "seasons": [
        ("پسرلی", "psarlay", "spring"), ("اوړی", "oṛay", "summer"),
        ("منی", "manay", "autumn"), ("ژمی", "žmay", "winter"),
    ],
}

ENTRIES.append({
    "key": "p08_numbers",
    "name": "Pashto Numbers and Time",
    "group": "Foundations",
    "ladder_rank": 8,
    "ladder_tier": "foundations",
    "description": (
        "The complete Pashto number and time system: units 1-10 (یو yaw, "
        "دوه dwa, درې dre, څلور tsalor, پنځه pindzə, شپږ špaǵ, اووه owə, "
        "اته atə, نهه nəhə, لس las), teens 11-19, tens 20-90 plus سل "
        "(səl - 100), ordinals لومړی/دوهم/درېیم (first/second/third), the "
        "seven days (شنبه Saturday through جمعه Friday), the twelve Solar "
        "Hijri months used in Afghanistan (حمل ثور جوزا سرطان اسد سنبله "
        "میزان عقرب قوس جدی دلو حوت), and the four seasons (پسرلی spring, "
        "اوړی summer, منی autumn, ژمی winter). Compound numbers join tens "
        "and units: دېرش + درې = دېرش درې (derš dre - 33). Clock time uses "
        "بجې (baje - o'clock): درې بجې (dre baje - three o'clock), with نیم "
        "(nim - half) for half hours. Example sentences: زه شل کاله لرم "
        "(zə šəl kāla lərəm - I am twenty years old); نن دوشنبه ده (nən "
        "dwašamba da - today is Monday); سبا به جمعه وي (sabā bə juma wi - "
        "tomorrow will be Friday); اوس درې نیمې بجې دي (os dre nime baje di "
        "- it is half past three now)."
    ),
    "how_it_works": (
        "Count 1-10 until automatic, then build teens as unit+لس forms "
        "(یوولس yawolas - 11) and tens as their own roots (شل šəl - 20, "
        "دېرش derš - 30). Tens combine with units by simple juxtaposition: "
        "څلوېښت پنځه (tsalwext pindzə - 45). Ordinals for first/second/third "
        "are لومړی/دوهم/درېیم; beyond that the cardinal does the work in "
        "colloquial speech. Days are named شنبه through جمعه with the "
        "Persian-style -شنبه suffixes - جمعه (Friday) is the week's anchor "
        "day. The Solar Hijri months start with حمل at the spring equinox; "
        "learn them as the calendar of Afghanistan. For dates: د حمل لومړۍ "
        "(də hamal lumṛəi - the first of Hamal). Time of day: سهار (sahār - "
        "morning), غرمه (ɣarma - noon), ماښام (māx̌ām - evening), شپه (špa - "
        "night)."
    ),
    "key_points": [
        "1-10: یو دوه درې څلور پنځه شپږ اووه اته نهه لس; teens 11-19; tens 20-90; سل = 100.",
        "Compounds juxtapose tens and units: دېرش درې (33), څلوېښت پنځه (45).",
        "Ordinals: لومړی (first), دوهم (second), درېیم (third).",
        "Seven days شنبه-جمعه (Saturday-Friday); جمعه is the anchor day.",
        "Twelve Solar Hijri months حمل-حوت, starting at the spring equinox.",
        "Four seasons: پسرلی (spring), اوړی (summer), منی (autumn), ژمی (winter).",
        "Clock time: بجې for o'clock, نیم for half - درې نیمې بجې (half past three).",
        "Time words: سهار (morning), غرمه (noon), ماښام (evening), شپه (night).",
    ],
    "requirements": [
        "Count 1-100 aloud until the tens roots are automatic.",
        "Learn the days and months in order, reciting them as a sequence.",
        "Practice ages, prices, and clock times with real numbers daily.",
        "Write dates in the Solar Hijri order: day of month.",
    ],
    "standards": [
        "Number forms follow standard written Pashto usage.",
        "The Solar Hijri month names follow the official Afghan calendar.",
        "Day names follow standard Pashto usage in Afghanistan and Pakistan.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats numbers as the sworn measures: "
        "ten units, nine teens, eight tens, one hundred - each with a fixed "
        "name no market can change. Days march شنبه to جمعه, months حمل to "
        "حوت, seasons turn پسرلی to ژمی. Seal the measures in order and "
        "time itself becomes countable, weighable, keepable."
    ),
    "demo_key": "numbers",
    "demo_data": NUM_8,
})

# ---------------------------------------------------------------- record 9

GREET_9 = [
    ("سلام", "salām", "hello / peace", "The universal greeting; safe everywhere, every time."),
    ("سلام علیکم", "salām alaykum", "peace be upon you", "Formal hello; answered with وعلیکم السلام."),
    ("وعلیکم السلام", "wa alaykum as-salām", "and upon you be peace", "The required reply to سلام علیکم."),
    ("سهار مو په خیر", "sahār mo pə xayr", "good morning", "Morning greeting; literally 'may your morning be good'."),
    ("ماښام مو په خیر", "māx̌ām mo pə xayr", "good evening", "Evening greeting, same pattern as the morning one."),
    ("شپه مو په خیر", "špa mo pə xayr", "good night", "Said when parting at night."),
    ("څنګه یې؟", "tsənga ye", "how are you? (familiar)", "To friends and family; formal: څنګه یئ؟"),
    ("څنګه یئ؟", "tsənga yəy", "how are you? (formal)", "To elders and strangers; uses تاسې agreement."),
    ("ښه یم، مننه", "x̌a yəm, manəna", "I am well, thank you", "The standard healthy reply."),
    ("تاسو څنګه یئ؟", "tāso tsənga yəy", "and how are you? (formal)", "Returning the question politely."),
    ("مننه", "manəna", "thank you", "The everyday thanks; warm and sufficient."),
    ("ډېره مننه", "ḍera manəna", "thank you very much", "Stronger gratitude."),
    ("بښنه غواړم", "bax̌əna ɣwāṛəm", "excuse me / I am sorry", "Apology and attention-getter in one."),
    ("مهرباني وکړئ", "mehrabāni wakṛəy", "please (formal)", "Literally 'do kindness'; the polite please."),
    ("لطفاً", "lutfan", "please", "Shorter please, widely understood."),
    ("خدای پامان", "xudāy pāmān", "goodbye", "Literally 'God protect'; the standard farewell."),
    ("په مخه ښه", "pə maxa x̌a", "goodbye / farewell", "Warm parting: 'go well on your way'."),
    ("بیا به سره ګورو", "byā bə sara guru", "we will meet again", "Hopeful goodbye between friends."),
    ("ستاسو نوم څه دی؟", "stāso num tsə day", "what is your name? (formal)", "First-meeting question; familiar: ستا نوم څه دی؟"),
    ("زما نوم ... دی", "zmā num ... day", "my name is ...", "Fill in your name; the frame never changes."),
    ("له تاسو سره په خبرو خوشحاله شوم", "lə tāso sara pə xabaro xošhāla šwəm", "pleased to meet you (formal)", "Said right after introductions."),
    ("ښه راغلاست", "x̌a rāɣlāst", "welcome", "Said to arriving guests; a point of honor."),
    ("مبارک شه", "mubārak ša", "congratulations / blessed be", "For weddings, births, new things, Eids."),
    ("اختر مو مبارک شه", "axtar mo mubārak ša", "blessed Eid to you", "Eid greeting."),
    ("روژه مو قبوله شه", "roža mo qabula ša", "may your fast be accepted", "Said during Ramadan."),
    ("صحت مو ښه شه", "sihat mo x̌a ša", "get well soon", "To the sick; literally 'may your health be good'."),
    ("خدای دې وبخښه", "xudāy de wobax̌a", "God forgive him/her", "Condolence phrase."),
    ("په خیر راغلې", "pə xayr rāɣle", "welcome back (to a woman)", "Said to a returning woman; to a man: په خیر راغلی."),
    ("ستړی مه شې", "staṛay ma še", "may you not tire (to a man)", "Said to someone working; to a woman: ستړې مه شې."),
    ("کور مو اباد شه", "kor mo ābād ša", "may your home prosper", "Blessing said when leaving a host's house."),
]

ENTRIES.append({
    "key": "p09_greetings",
    "name": "Pashto Greetings and Everyday Phrases",
    "group": "Foundations",
    "ladder_rank": 9,
    "ladder_tier": "foundations",
    "description": (
        "Thirty greetings, farewells, and politeness phrases - each with "
        "transliteration, English meaning, and a usage note. The set opens "
        "with سلام (salām - hello/peace) and its formal pair سلام علیکم / "
        "وعلیکم السلام, then the time-of-day blessings سهار مو په خیر "
        "(good morning), ماښام مو په خیر (good evening), شپه مو په خیر "
        "(good night). Health inquiries come in familiar (څنګه یې؟) and "
        "formal (څنګه یئ؟) forms. Gratitude runs مننه (thank you) to ډېره "
        "مننه (thank you very much); requests use مهرباني وکړئ (please) "
        "and لطفاً; apologies use بښنه غواړم (excuse me/I am sorry). "
        "Farewells: خدای پامان (goodbye), په مخه ښه (go well), بیا به سره "
        "ګورو (we will meet again). Introductions: ستاسو نوم څه دی؟ / زما "
        "نوم ... دی / له تاسو سره په خبرو خوشحاله شوم / ښه راغلاست. "
        "Blessings for occasions: مبارک شه (congratulations), اختر مو "
        "مبارک شه (blessed Eid), روژه مو قبوله شه (Ramadan), صحت مو ښه شه "
        "(get well), خدای دې وبخښه (condolence), ستړی مه شې (to one who "
        "works), کور مو اباد شه (to a host on leaving), and the gendered "
        "welcome-back په خیر راغلی/راغلې."
    ),
    "how_it_works": (
        "Greetings in Pashto are blessings, not just hellos - سهار مو په "
        "خیر literally wishes the morning good. Always answer a greeting "
        "with its pair: سلام علیکم demands وعلیکم السلام. Match the "
        "formality: ته-forms (څنګه یې؟) for friends, تاسې-forms (څنګه یئ؟) "
        "for elders and strangers - getting this wrong is the classic "
        "beginner mistake. Stack greetings in order: greeting, health "
        "inquiry, return inquiry (تاسو څنګه یئ؟), then business. Blessings "
        "are gendered where noted: ستړی مه شې to a man, ستړې مه شې to a "
        "woman; په خیر راغلی to a man, په خیر راغلې to a woman. Use مبارک "
        "شه for every happy occasion and خدای دې وبخښه for condolences - "
        "never mix them. End visits with کور مو اباد شه to honor the host."
    ),
    "key_points": [
        "30 greetings/farewells/politeness phrases with usage notes - the social survival kit.",
        "Greetings are blessings: سهار مو په خیر wishes the morning good, not just marks the time.",
        "Always pair: سلام علیکم → وعلیکم السلام; health inquiry → return inquiry.",
        "Familiar vs formal is mandatory: څنګه یې؟ (friends) vs څنګه یئ؟ (elders/strangers).",
        "Gendered forms: ستړی/ستړې مه شې, په خیر راغلی/راغلې - match the person.",
        "Occasion blessings: مبارک شه (joy), اختر مو مبارک شه (Eid), خدای دې وبخښه (condolence).",
        "خدای پامان is the standard goodbye; کور مو اباد شه honors the host on leaving.",
    ],
    "requirements": [
        "Memorize the greeting pairs as pairs, never as isolated words.",
        "Practice the familiar/formal split aloud until it is reflexive.",
        "Use the gendered forms correctly - this is noticed immediately.",
        "Deploy one blessing per occasion for a week until each is natural.",
    ],
    "standards": [
        "Phrases follow standard Pashto usage in Afghanistan and Pakistan.",
        "Formality distinctions follow the standard ته/تاسې politeness system.",
        "Transliteration matches the scheme fixed in record 2.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats each greeting as a sworn "
        "blessing with a fixed return: سلام علیکم is a door opened, "
        "وعلیکم السلام the door held open in return. The familiar and the "
        "formal are two gates - enter the wrong gate and the covenant "
        "breaks. Seal the 30 blessings with their pairs, honor gender and "
        "occasion, and every meeting opens correctly."
    ),
    "demo_key": "phrases",
    "demo_data": {"phrases": GREET_9},
})

# ---------------------------------------------------------------- record 10

GRAMMAR_10 = [
    ("Word order is subject-object-verb: the verb comes last.",
     "زه چای څښم", "zə čāy tsṣ̌əm", "I drink tea (literally: I tea drink)."),
    ("Two genders: masculine and feminine; the verb 'to be' agrees.",
     "کور لوی دی / ښځه ښه ده", "kor loy day / x̌əza x̌a da",
     "The house is big (masc.) / The woman is good (fem.)."),
    ("Two main cases: direct and oblique; the oblique marks the past-tense agent.",
     "ما کتاب ولوست", "mā kitāb walwast", "I read the book (ما = oblique of زه)."),
    ("Split ergativity: present is nominative, past transitive is ergative.",
     "زه خورم / ما وخوړله", "zə xorəm / mā woxoṛla",
     "I eat (present) / I ate it (past, agent oblique, verb agrees with object)."),
    ("No articles; یو (one) marks indefiniteness.",
     "یو سړی راغی", "yaw saṛay rāɣay", "A man came (literally: one man came)."),
    ("Negation: نه before the verb; مه for negative commands.",
     "زه نه ځم / مه ځه", "zə nə dzəm / ma dza",
     "I do not go. / Do not go!"),
    ("Questions: interrogative word first, or rising intonation.",
     "ته چېرته ځې؟ / ښه یې؟", "tə čerta dze / x̌a ye",
     "Where are you going? / Are you well?"),
    ("Future: به before the present verb; adjectives agree in gender.",
     "زه به ځم / لویه ښځه", "zə bə dzəm / loya x̌əza",
     "I will go. / Big woman (feminine form)."),
]

ENTRIES.append({
    "key": "p10_grammar",
    "name": "Pashto Grammar Essentials",
    "group": "Foundations",
    "ladder_rank": 10,
    "ladder_tier": "foundations",
    "description": (
        "The eight load-bearing rules of Pashto grammar, each with a "
        "translated example sentence. (1) Word order is subject-object-verb "
        "- the verb comes last: زه چای څښم (zə čāy tsṣ̌əm - I drink tea). "
        "(2) Two genders, masculine and feminine, with the verb 'to be' "
        "agreeing: کور لوی دی (masculine) vs ښځه ښه ده (feminine). (3) Two "
        "main cases, direct and oblique; the oblique case marks the agent "
        "of past-tense transitive verbs: ما کتاب ولوست (mā kitāb walwast - "
        "I read the book). (4) Split ergativity: the present tense works "
        "like English (زه خورم - I eat) but the past tense of transitive "
        "verbs puts the doer in the oblique and agrees the verb with the "
        "object (ما وخوړله - I ate it). (5) No articles: یو (yaw - one) "
        "marks indefiniteness - یو سړی راغی (a man came). (6) Negation puts "
        "نه (nə) before the verb - زه نه ځم (I do not go); negative commands "
        "use مه - مه ځه (do not go!). (7) Questions front an interrogative "
        "word (ته چېرته ځې؟ - where are you going?) or use rising intonation "
        "(ښه یې؟ - are you well?). (8) The future is به + present verb - "
        "زه به ځم (I will go); adjectives agree in gender - لویه ښځه (big "
        "woman, feminine)."
    ),
    "how_it_works": (
        "Build every sentence verb-last and the grammar starts working "
        "immediately. In the present, think English with the verb moved to "
        "the end: subject, object, verb. In the past with a transitive "
        "verb, flip the subject into its oblique form (زه→ما, ته→تا) and "
        "let the verb agree with the object instead - this is the famous "
        "split ergativity, and it is completely regular once the habit "
        "forms. Negate by placing نه directly before the verb, never "
        "elsewhere. Ask by placing څوک/څه/چېرته/کله/ولې first and keeping "
        "the verb last. Mark the future with به before the present verb. "
        "Check gender on every adjective-noun pair: the feminine form "
        "usually adds ه or ې. Run the eight rules against every sentence "
        "you meet from here on - they explain nearly everything."
    ),
    "key_points": [
        "SOV: verb last, always - زه چای څښم ('I tea drink').",
        "Two genders with verb agreement: دی (masc.) vs ده (fem.).",
        "Direct/oblique cases; the oblique marks the past-tense transitive agent: ما کتاب ولوست.",
        "Split ergativity: present nominative (زه خورم), past transitive ergative (ما وخوړله).",
        "No articles; یو marks 'a/an'; نه negates before the verb; مه negates commands.",
        "Questions: interrogative first or rising intonation, verb still last.",
        "Future = به + present verb: زه به ځم; adjectives agree in gender: لویه ښځه.",
        "These eight rules explain nearly every sentence in records 11-34.",
    ],
    "requirements": [
        "Write ten original sentences and check each against all eight rules.",
        "Drill the زه→ما / ته→تا past-tense shift until it is automatic.",
        "Place نه and به correctly in fifty practice sentences.",
        "Never put the verb anywhere but last until the habit is sealed.",
    ],
    "standards": [
        "Grammatical description follows the standard reference grammars cited below.",
        "The split-ergativity account follows the standard analysis of Pashto morphosyntax.",
        "Example sentences use standard written Pashto (Northern-based).",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method seals grammar as eight covenants: the "
        "verb shall stand last; gender shall be honored in every seal; the "
        "past shall turn the doer oblique; negation shall stand before the "
        "verb; the future shall be marked with به. Eight covenants, no "
        "exceptions in the foundation. Build on them and the whole "
        "language stands; break one and the sentence falls."
    ),
    "demo_key": "grammar",
    "demo_data": {"rules": GRAMMAR_10},
})


def _S(*triples):
    return list(triples)


# ---------------------------------------------------------------- records 11-20: themed sentence sets

SENT_11 = _S(
    ("دا زموږ کور دی", "dā zmuẓ̌ kor day", "This is our house."),
    ("زما پلار ښوونکی دی", "zmā plār x̌owunkay day", "My father is a teacher."),
    ("زما مور ډوډۍ پخوي", "zmā mor ḍoḍəi paxawi", "My mother bakes bread."),
    ("زما ورور په ښار کې کار کوي", "zmā wror pə x̌ār ke kār kawi", "My brother works in the city."),
    ("زما خور ښوونځي ته ځي", "zmā xor x̌owənǵi ta dzi", "My sister goes to school."),
    ("موږ په دې کوټه کې اوسو", "muẓ̌ pə de koṭa ke osu", "We live in this room."),
    ("د خوب کوټه پورته ده", "də xob koṭa porta da", "The bedroom is upstairs."),
    ("پخلنځی کوچنی دی", "paxlandzay kučnay day", "The kitchen is small."),
    ("مېلمستون پراخ دی", "melmastun parāx day", "The guest room is spacious."),
    ("تشناب پاک دی", "tašnāb pāk day", "The bathroom is clean."),
    ("دا زما څوکۍ ده", "dā zmā tsawkəi da", "This is my chair."),
    ("کټ د کړکۍ تر څنګ دی", "kaṭ də kəṛkəi tər tsang day", "The bed is beside the window."),
    ("پر مېز کتابونه دي", "pər mez kitābuna di", "There are books on the table."),
    ("څراغ رڼا کوي", "tsrāɣ raṇā kawi", "The lamp gives light."),
    ("دروازه بنده ده", "darwāza banda da", "The door is closed."),
    ("کړکۍ پرانیستې ده", "kəṛkəi prāniste da", "The window is open."),
    ("زموږ کورنۍ لویه ده", "zmuẓ̌ koranəi loya da", "Our family is big."),
    ("نیا کیسې کوي", "nyā kise kawi", "Grandmother tells stories."),
    ("نیکه په باغ کې ګرځي", "nika pə bāɣ ke gərdzi", "Grandfather walks in the garden."),
    ("موږ ټول یو ځای ډوډۍ خورو", "muẓ̌ ṭol yaw dzāy ḍoḍəi xoru", "We all eat together."),
)

SENT_12 = _S(
    ("سهارنۍ وخوره", "sahāranəi woxora", "Eat breakfast."),
    ("مور غرمنۍ پخوي", "mor ɣarmanəi paxawi", "Mother is cooking lunch."),
    ("موږ ماښامنۍ یو ځای خورو", "muẓ̌ māx̌āmanəi yaw dzāy xoru", "We eat dinner together."),
    ("چای ګرم دی", "čāy garam day", "The tea is hot."),
    ("شیدې ساړې دي", "šide sāṛe di", "The milk is cold."),
    ("ډوډۍ تازه ده", "ḍoḍəi tāza da", "The bread is fresh."),
    ("وریجې په دې لوښي کې دي", "wriǵe pə de lox̌i ke di", "The rice is in this pot."),
    ("غوښه په تنور کې پخېږي", "ɣwaxa pə tanur ke paxeǵi", "The meat is baking in the clay oven."),
    ("سبزي ومینځه", "sabzi womindza", "Wash the vegetables."),
    ("پیاز پرې کړه", "pyāz pre kra", "Cut the onions."),
    ("مالګه ور واچوه", "mālga wər wāčawa", "Add salt to it."),
    ("اوبه وڅښه", "obə wotsṣ̌a", "Drink water."),
    ("مڼې خوږې دي", "maṇe xoǵe di", "The apples are sweet."),
    ("انګور په باغ کې دي", "angur pə bāɣ ke di", "The grapes are in the garden."),
    ("د رستورانټ خواړه ګران دي", "də rastorānṭ xwāṛə grān day", "The restaurant food is expensive."),
    ("مېلمه ته چای ورکړه", "melma ta čāy wərkṛa", "Give tea to the guest."),
    ("دسترخوان هوار کړه", "dastarxwān hawār kra", "Spread the tablecloth."),
    ("لوښي پاک دي", "lox̌i pāk di", "The dishes are clean."),
    ("نن پلو پخوو", "nən palaw paxawu", "Today we are cooking pilaf."),
    ("خواړه خوندور دي", "xwāṛə xwandawər day", "The food is delicious."),
)

SENT_13 = _S(
    ("تمځای چېرته دی؟", "tamdzāy čerta day", "Where is the station?"),
    ("هوايي ډګر لېره دی", "hawāyi ḍagar lera day", "The airport is far."),
    ("ټکټ واخله", "ṭikaṭ wāxla", "Buy a ticket."),
    ("بس کله راځي؟", "bas kəla rādzi", "When does the bus come?"),
    ("ګاډی په اتو بجو ځي", "gāḍay pə ato bajo dzi", "The vehicle leaves at eight o'clock."),
    ("دا لار کابل ته ځي", "dā lār kābal ta dzi", "This road goes to Kabul."),
    ("ښي لاس ته وګرځه", "x̌ay lās ta wəgərdza", "Turn to the right."),
    ("نیغ لاړ شه", "niɣ lāṛ ša", "Go straight ahead."),
    ("بازار ته نږدې دی", "bāzār ta naǵde day", "It is near the market."),
    ("هوټل په هغه کوڅه کې دی", "hoṭal pə haɣa kutsa ke day", "The hotel is in that street."),
    ("یوه کوټه غواړم", "yawa koṭa ɣwāṛəm", "I want a room."),
    ("یوه شپه څو ده؟", "yawa špa tso da", "How much is one night?"),
    ("تشناب چېرته دی؟", "tašnāb čerta day", "Where is the bathroom?"),
    ("نقشه راوښیه", "naqša rāwxaya", "Show me the map."),
    ("زه لاره ورکه کړې ده", "zə lāra warka kṛe da", "I am lost (I have lost the way)."),
    ("مرسته وکړه، مهرباني", "mrasta wakṛa, mehrabāni", "Help me, please."),
    ("ټکسي ودروه", "ṭaksi wadrawa", "Stop a taxi."),
    ("کرایه څومره ده؟", "kirāya tsumra da", "How much is the fare?"),
    ("دلته ودروه", "dalta wadrawa", "Stop here."),
    ("سفر مو په خیر", "safar mo pə xayr", "Have a safe journey."),
)

SENT_14 = _S(
    ("زه ښوونکی یم", "zə x̌owunkay yəm", "I am a teacher."),
    ("هغه ډاکټر دی", "haɣa ḍākṭar day", "He is a doctor."),
    ("زما ورور انجنیر دی", "zmā wror injiner day", "My brother is an engineer."),
    ("هغه په دفتر کې کار کوي", "haɣa pə daftar ke kār kawi", "He works in an office."),
    ("موږ سهار وختي پاڅو", "muẓ̌ sahār waxti pātso", "We wake up early in the morning."),
    ("کار په نهو بجو پیلېږي", "kār pə naho bajo pileǵi", "Work starts at nine o'clock."),
    ("نن غونډه لرو", "nən ɣunḍa ləru", "We have a meeting today."),
    ("دا راپور ولیکه", "dā rāpor walika", "Write this report."),
    ("ماشومان درس وايي", "māšumān dars wāyi", "The children are studying the lesson."),
    ("ښوونکی پوښتنه کوي", "x̌owunkay poxtana kawi", "The teacher asks a question."),
    ("زده کوونکی ځواب ورکوي", "zda kawunkay dzawāb warkawi", "The student gives the answer."),
    ("کتاب پرانیزه", "kitāb prāniza", "Open the book."),
    ("په تخته ولیکه", "pə taxta walika", "Write on the board."),
    ("کورنۍ دنده وکړه", "koranəi danda wakṛa", "Do the homework."),
    ("ازموینه سبا ده", "āzmoyina sabā da", "The exam is tomorrow."),
    ("زه پښتو زده کوم", "zə paʂto zda kawəm", "I am learning Pashto."),
    ("هغه انګریزي وايي", "haɣa ingrezi wāyi", "He speaks English."),
    ("ټولګی لوی دی", "ṭolgay loy day", "The classroom is big."),
    ("کتابتون چوپ دی", "kitābtun čup day", "The library is quiet."),
    ("رخصتي په جمعه ده", "ruxsati pə juma da", "The holiday is on Friday."),
)

SENT_15 = _S(
    ("زما سر خوږېږي", "zmā sar xoǵeǵi", "My head hurts."),
    ("ستونی مې درد کوي", "stunay me dard kawi", "My throat hurts."),
    ("تبه لرم", "taba lərəm", "I have a fever."),
    ("ټوخی کوم", "ṭuxay kawəm", "I am coughing."),
    ("زکام یم", "zukām yəm", "I have a cold."),
    ("مېده مې خرابه ده", "meḏa me xarāba da", "My stomach is upset."),
    ("لاس مې پرې شوی دی", "lās me pre šaway day", "My hand is cut."),
    ("پښه مې ماته شوې ده", "px̌a me māta šawe da", "My leg is broken."),
    ("سترګې مې سوري کوي", "starge me suri kawi", "My eyes burn."),
    ("ډاکټر ته لاړ شه", "ḍākṭar ta lāṛ ša", "Go to the doctor."),
    ("روغتون چېرته دی؟", "roɣtun čerta day", "Where is the hospital?"),
    ("درمل واخله", "darmal wāxla", "Take the medicine."),
    ("دا ګولۍ په ورځ کې درې ځله وخوره", "dā goləi pə wrədz ke dre dzala woxora", "Take this pill three times a day."),
    ("اوبه ډېرې وڅښه", "obə ḍere wotsṣ̌a", "Drink plenty of water."),
    ("استراحت وکړه", "istirāhat wakṛa", "Rest."),
    ("زخم پاک وساته", "zaxm pāk wasāta", "Keep the wound clean."),
    ("وینه بهېږي", "wina beheǵi", "It is bleeding."),
    ("ناروغ په کټ کې دی", "nāroɣ pə kaṭ ke day", "The patient is in bed."),
    ("درملتون نږدې دی", "darmaltun naǵde day", "The pharmacy is nearby."),
    ("خدای دې روغ کړه", "xudāy de roɣ kṛa", "May God heal you."),
)

SENT_16 = _S(
    ("زه نن ډېر خوشحاله یم", "zə nən ḍer xošhāla yəm", "I am very happy today."),
    ("هغه په خندا ده", "haɣa pə xandā da", "She is laughing."),
    ("ماشومان لوبې کوي او خوشحال دي", "māšumān lobe kawi aw xošhāl di", "The children are playing and are happy."),
    ("زه خفه یم", "zə xafa yəm", "I am sad."),
    ("ولې ژاړې؟", "walə žāṛe", "Why are you crying?"),
    ("هغه په غوسه دی", "haɣa pə ɣusa day", "He is angry."),
    ("غوسه مه کوه", "ɣusa ma kawa", "Do not get angry."),
    ("زه وېرېږم", "zə wereǵəm", "I am afraid."),
    ("مه وېرېږه، زه درسره یم", "ma wereǵa, zə darsara yəm", "Do not be afraid, I am with you."),
    ("زه له تا سره مینه لرم", "zə lə tā sara mina lərəm", "I love you."),
    ("مینه تر ټولو لویه ده", "mina tər ṭolo loya da", "Love is the greatest of all."),
    ("هغه حیران شو", "haɣa hayrān šu", "He was surprised."),
    ("زه ستړی یم", "zə staṛay yəm", "I am tired."),
    ("کرار کښېنه", "krar kṣ̌ena", "Sit calmly / calm down."),
    ("زړه مې خوشحال شو", "zṛa me xošhāl šu", "My heart became happy."),
    ("هیله لرم چې ښه به شي", "hila lərəm če x̌a bə ši", "I hope it will be fine."),
    ("اندېښنه مه کوه", "andeṣ̌na ma kawa", "Do not worry."),
    ("زه ویاړم پر تا", "zə wyāṛəm pər tā", "I am proud of you."),
    ("شرمېږه مه", "šarmeǵa ma", "Do not be shy."),
    ("خندا روغتیا ده", "xandā roɣtyā da", "Laughter is health."),
)

SENT_17 = _S(
    ("نن هوا ښه ده", "nən hawā x̌a da", "The weather is good today."),
    ("اسمان وریځ دی", "āsmān wridz day", "The sky is cloudy."),
    ("باران وریږي", "bārān wriǵi", "It is raining."),
    ("واوره ورېږي", "wāwra wreǵi", "It is snowing."),
    ("باد لګېږي", "bād lageǵi", "The wind is blowing."),
    ("هوا ګرمه ده", "hawā garma da", "The weather is hot."),
    ("هوا ساړه ده", "hawā sāṛa da", "The weather is cold."),
    ("پسرلی راغی", "psarlay rāɣay", "Spring has come."),
    ("ګلان غوړېدلي دي", "gulān ɣwoṛedəli di", "The flowers have bloomed."),
    ("ونې شنې شوې دي", "wəṇe šne šəwe di", "The trees have turned green."),
    ("په اوړي کې ګرمي وي", "pə oṛay ke garmi wi", "In summer it is hot."),
    ("په ژمي کې واوره وریږي", "pə žmay ke wāwra wreǵi", "In winter it snows."),
    ("سیند ډک دی", "sind ḍak day", "The river is full."),
    ("غرونه سپین دي", "ɣruna spin di", "The mountains are white."),
    ("مارغان الوځي", "mārɣān alwadzi", "The birds are flying."),
    ("سپي په کلي کې غاپي", "spi pə kalay ke ɣāpi", "The dogs are barking in the village."),
    ("پیشو په لمر کې پرته ده", "pišo pə lmar ke parata da", "The cat is lying in the sun."),
    ("اسونه په میدان کې ځغلي", "āsuna pə maydān ke dzɣali", "The horses are running in the field."),
    ("شپه ستوري ځلېږي", "špa stori dzaleǵi", "At night the stars shine."),
    ("سهار مرغان چغې وهي", "sahār marɣān čaɣe wahi", "In the morning the birds sing."),
)

SENT_18 = _S(
    ("بازار ته ځو", "bāzār ta dzu", "We are going to the market."),
    ("دا څومره دی؟", "dā tsumra day", "How much is this?"),
    ("ډېر ګران دی", "ḍer grān day", "It is too expensive."),
    ("ارزان یې کړه", "arzān ye kṛa", "Make it cheaper."),
    ("وروستۍ بیه ووایه", "wrustəi beya wuwāya", "Tell me the final price."),
    ("زه یې اخلم", "zə ye axləm", "I will take it."),
    ("زه یې نه اخلم", "zə ye nə axləm", "I will not take it."),
    ("پیسې ورکړه", "payse wərkṛa", "Pay the money."),
    ("باقي راکړه", "bāqi rākṛa", "Give me the change."),
    ("رسید راکړه", "rasid rākṛa", "Give me the receipt."),
    ("دا مڼې تازه دي", "dā maṇe tāze di", "These apples are fresh."),
    ("یو کیلو راوړه", "yaw kilo rāwṛa", "Bring one kilo."),
    ("کپړه وګوره", "kapṛa wagora", "Look at the cloth."),
    ("دا رنګ ښه دی", "dā rang x̌a day", "This color is good."),
    ("لوی سایز لری؟", "loy sāyz lare", "Do you have a large size?"),
    ("دوکان کله پرانیزي؟", "dukān kəla prānizi", "When does the shop open?"),
    ("نغدې پیسې لرم", "naɣde payse lərəm", "I have cash."),
    ("تخفیف شته؟", "taxfif šta", "Is there a discount?"),
    ("سبا به بیا راشم", "sabā bə byā rāšəm", "I will come again tomorrow."),
    ("مننه، خدای پامان", "manəna, xudāy pāmān", "Thank you, goodbye."),
)

SENT_19 = _S(
    ("زما ملګری راغی", "zmā malgaray rāɣay", "My friend came."),
    ("موږ ملګري یو", "muẓ̌ malgəri yu", "We are friends."),
    ("سبا زما کره راشه", "sabā zmā kara rāša", "Come to my place tomorrow."),
    ("مېلمستیا ته دې بلنه درکوم", "melmastyā ta de balna darkawəm", "I invite you to the feast."),
    ("بلنه دې ومنله", "balna de wamanla", "Accept the invitation."),
    ("په واده کې دې ګډون وکړ", "pə wāda ke de gaḍun wakṛ", "Attend the wedding."),
    ("اختر مو مبارک شه", "axtar mo mubārak ša", "Blessed Eid to you."),
    ("ډالۍ دې مبارک شه", "ḍāləi de mubārak ša", "Congratulations on the gift."),
    ("له ملګرو سره چای وڅښه", "lə malgaro sara čāy wotsṣ̌a", "Have tea with friends."),
    ("کیسې وکړئ", "kise wakṛəy", "Tell stories."),
    ("ټوکې مه کوه", "ṭoke ma kawa", "Do not joke (about it)."),
    ("رښتیا ووایه", "rəxtyā wuwāya", "Tell the truth."),
    ("ژمنه وکړه", "žəməna wakṛa", "Make a promise."),
    ("ژمنه مات مه کړه", "žəməna māt ma kṛa", "Do not break the promise."),
    ("بخښنه وغواړه", "bax̌əna woɣwāṛa", "Ask for forgiveness."),
    ("زه دې بخښم", "zə de bax̌əm", "I forgive you."),
    ("لاس سره ورکړه", "lās sara wərkṛa", "Shake hands."),
    ("غېږه ورکړه", "ɣeǵa wərkṛa", "Give a hug."),
    ("تل خوشحاله اوسه", "təl xošhāla osa", "Always stay happy."),
    ("خدای دې مل شه", "xudāy de mal ša", "May God be with you."),
)

SENT_20 = _S(
    ("تلیفون وکړه", "telifon wakṛa", "Make a phone call."),
    ("زما شمېره واخله", "zmā šmera wāxla", "Take my number."),
    ("پیغام پرېږده", "payɣām preǵda", "Leave a message."),
    ("انټرنټ کار نه کوي", "inṭarneṭ kār nə kawi", "The internet is not working."),
    ("وای فای وصل کړه", "wāy fāy wasal kṛa", "Connect the Wi-Fi."),
    ("کمپیوټر چالان کړه", "kampyuṭar čālān kṛa", "Turn on the computer."),
    ("کمپیوټر ګل کړه", "kampyuṭar gul kṛa", "Turn off the computer."),
    ("بریښنالیک واستوه", "breṣ̌nālik wāstawa", "Send an email."),
    ("عکس واخله", "aks wāxla", "Take a photo."),
    ("ویډیو جوړه کړه", "wiḍyo joṛa kṛa", "Make a video."),
    ("چارجر راوړه", "čārjar rāwṛa", "Bring the charger."),
    ("بټرۍ خلاصه شوې ده", "baṭrəi xlāsa šawe da", "The battery is dead."),
    ("سکرین مات شوی دی", "skrin māt šaway day", "The screen is broken."),
    ("غږ پورته کړه", "ɣaǵ porta kṛa", "Turn up the volume."),
    ("غږ ټیټ کړه", "ɣaǵ ṭiṭ kṛa", "Turn down the volume."),
    ("ویډیو زنګ ووهه", "wiḍyo zang wuwaha", "Make a video call."),
    ("آنلاین یم", "ānlāyn yəm", "I am online."),
    ("پاسورډ مه هېروه", "pāsworḍ ma herawa", "Do not forget the password."),
    ("فایل خوندي کړه", "fāyl xwandi kṛa", "Save the file."),
    ("کمپیوټر پوهېږم", "kampyuṭar poheǵəm", "I understand computers."),
)

THEMED = [
    ("p11_home", "Pashto at Home and with Family", SENT_11,
     "Twenty home-and-family sentences: the house, its rooms (د خوب کوټه the bedroom, پخلنځی the kitchen, مېلمستون the guest room, تشناب the bathroom), furniture (څوکۍ chair, کټ bed, مېز table, څراغ lamp, دروازه door, کړکۍ window), and the family (پلار father, مور mother, ورور brother, خور sister, نیا grandmother, نیکه grandfather) - each translated.",
     "Home is where the first covenants are sealed: learn the rooms, the furniture, and the family names until the house speaks Pashto.",
     "home-family"),
    ("p12_food", "Pashto Food and Cooking", SENT_12,
     "Twenty food-and-cooking sentences: the meals (سهارنۍ breakfast, غرمنۍ lunch, ماښامنۍ dinner), staples (ډوډۍ bread, وریجې rice, غوښه meat, سبزي vegetables), drinks (چای tea, شیدې milk, اوبه water), fruit (مڼې apples, انګور grapes), cooking actions (پخول to cook, پرې کول to cut, مینځل to wash), and the restaurant (رستورانټ, مېلمه guest, دسترخوان tablecloth) - each translated.",
     "The kitchen is the second school: learn the meals, the staples, and the cooking verbs until the table speaks Pashto.",
     "food-cooking"),
    ("p13_travel", "Pashto Travel and Directions", SENT_13,
     "Twenty travel sentences: the station (تمځای), the airport (هوايي ډګر), tickets (ټکټ), the bus (بس), directions (ښي لاس ته right, نیغ straight), lodging (هوټل hotel, کوټه room), prices (کرایه fare), and the traveler's lifelines - زه لاره ورکه کړې ده (I am lost), مرسته وکړه (help me), سفر مو په خیر (safe journey) - each translated.",
     "The road tests the language: learn the stations, the directions, and the traveler's lifelines until the journey speaks Pashto.",
     "travel-directions"),
    ("p14_work", "Pashto Work and School", SENT_14,
     "Twenty work-and-school sentences: the jobs (ښوونکی teacher, ډاکټر doctor, انجنیر engineer), the office (دفتر, غونډه meeting, راپور report), the school day (درس lesson, ټولګی classroom, کتابخانه library, ازموینه exam, کورنۍ دنده homework), and learning itself - زه پښتو زده کوم (I am learning Pashto) - each translated.",
     "Work and school are where words earn their keep: learn the jobs, the office, and the classroom until the day speaks Pashto.",
     "work-school"),
    ("p15_health", "Pashto Health and the Body", SENT_15,
     "Twenty health sentences: the body (سر head, ستونی throat, مېده stomach, لاس hand, پښه leg, سترګې eyes), symptoms (تبه fever, ټوخی cough, زکام cold, درد pain), the doctor's path (ډاکټر, روغتون hospital, درملتون pharmacy, درمل medicine, ګولۍ pill), and healing words - استراحت وکړه (rest), خدای دې روغ کړه (may God heal you) - each translated.",
     "The body speaks first in any language: learn its parts, its pains, and the healing words until care speaks Pashto.",
     "health-body"),
    ("p16_emotions", "Pashto Emotions and Feelings", SENT_16,
     "Twenty emotion sentences: joy (خوشحاله happy, خندا laughter), sorrow (خفه sad, ژړا crying), anger (غوسه anger), fear (وېره fear), love (مینه love), surprise (حیران surprised), and the comfort phrases - مه وېرېږه (do not be afraid), اندېښنه مه کوه (do not worry), زه ویاړم پر تا (I am proud of you) - each translated.",
     "Feelings are the mother tongue beneath the mother tongue: learn joy, sorrow, anger, fear, and love until the heart speaks Pashto.",
     "emotions-feelings"),
    ("p17_nature", "Pashto Nature and Weather", SENT_17,
     "Twenty nature-and-weather sentences: the sky (اسمان, وریځ cloud, باران rain, واوره snow, باد wind), the seasons (پسرلی spring, اوړی summer, ژمی winter), the land (سیند river, غرونه mountains, ګلان flowers, ونې trees), and the animals (مارغان birds, سپي dogs, پیشو cat, اسونه horses) - each translated.",
     "The land is the oldest teacher: learn the sky, the seasons, and the living things until nature speaks Pashto.",
     "nature-weather"),
    ("p18_shopping", "Pashto Shopping and Money", SENT_18,
     "Twenty market sentences: the market (بازار), the shop (دوکان), asking prices (دا څومره دی؟ - how much is this?), bargaining (ډېر ګران دی - too expensive; ارزان یې کړه - make it cheaper; وروستۍ بیه ووایه - the final price), paying (پیسې ورکړه - pay; باقي راکړه - the change; رسید receipt), and goods (مڼې apples, کپړه cloth, سایز size, تخفیف discount) - each translated.",
     "The market is the loudest classroom: learn the prices, the bargaining, and the paying until trade speaks Pashto.",
     "shopping-money"),
    ("p19_friendship", "Pashto Friendship and Social Life", SENT_19,
     "Twenty friendship sentences: meeting (زما ملګری راغی - my friend came), invitations (بلنه invitation, مېلمستیا feast), celebrations (واده wedding, اختر Eid, ډالۍ gift), and the social covenants - ژمنه وکړه (make a promise), ژمنه مات مه کړه (do not break it), بخښنه وغواړه (ask forgiveness), زه دې بخښم (I forgive you) - each translated.",
     "Friendship is a covenant renewed daily: learn the meetings, the invitations, and the promises until loyalty speaks Pashto.",
     "friendship-social"),
    ("p20_tech", "Pashto Technology and Communication", SENT_20,
     "Twenty technology sentences: the phone (تلیفون, شمېره number, پیغام message, زنګ call), the network (انټرنټ internet, وای فای Wi-Fi, آنلاین online), the computer (کمپیوټر, سکرین screen, بټرۍ battery, چارجر charger, فایل file, پاسورډ password), and media (عکس photo, ویډیو video, برېښنالیک email) - each translated.",
     "The new tools speak every language: learn the phone, the network, and the computer until the future speaks Pashto.",
     "technology-communication"),
]

for _i, (_key, _name, _sents, _desc, _sig, _kind) in enumerate(THEMED):
    ENTRIES.append({
        "key": _key,
        "name": _name,
        "group": "Compounded",
        "ladder_rank": 11 + _i,
        "ladder_tier": "compounded",
        "description": _desc,
        "how_it_works": (
            "Twenty full sentences on one theme of daily life, each with "
            "transliteration and English translation. Read the Pashto "
            "aloud first, then check the transliteration, then the English - "
            "three passes per sentence. Notice which nouns from record 4 and "
            "which verbs from record 5 reappear here: the ladder compounds, "
            "and old words do new work. Copy five sentences by hand each "
            "day; change one word in each to make it your own (زما becomes "
            "ستا, نن becomes سبا). The grammar of record 10 runs underneath "
            "every line - verb last, نه before the verb, به for the future - "
            "so each sentence is also a grammar drill."
        ),
        "key_points": [
            "20 themed sentences with transliteration and English translation - no word lists, only living sentences.",
            "Old vocabulary compounds: nouns from record 4 and verbs from record 5 do new work here.",
            "Three passes per sentence: Pashto aloud, transliteration check, English meaning.",
            "Change one word per sentence to make it yours - the fastest path to ownership.",
            "Record 10 grammar runs underneath every line: verb last, نه negation, به future.",
        ],
        "requirements": [
            "Read all 20 sentences aloud before moving to the next record.",
            "Hand-copy five sentences daily, altering one word in each.",
            "Identify the record-4 nouns and record-5 verbs inside each sentence.",
            "Use at least three sentences in real speech each day.",
        ],
        "standards": [
            "Sentences follow standard written Pashto usage.",
            "Vocabulary is consistent with records 4-9 of this database.",
            "Transliteration matches the scheme fixed in record 2.",
        ],
        "citations": list(CIT_ALL),
        "sig_lens": _sig,
        "demo_key": "sentences",
        "demo_data": {"topic": _name, "sentences": _sents},
    })

# ---------------------------------------------------------------- record 21

TENSE_21 = {
    "verb_ps": "تلل", "verb_tr": "tləl", "verb_en": "to go",
    "present": [
        ("زه ځم", "zə dzəm", "I go / I am going"),
        ("ته ځې", "tə dze", "you go (familiar)"),
        ("هغه ځي", "haɣa dzi", "he/she goes"),
        ("موږ ځو", "muẓ̌ dzu", "we go"),
        ("تاسې ځئ", "tāsə dzəy", "you go (plural/formal)"),
        ("هغوی ځي", "haɣwi dzi", "they go"),
    ],
    "past": [
        ("زه لاړم", "zə lāṛəm", "I went"),
        ("ته لاړې", "tə lāṛe", "you went (familiar)"),
        ("هغه لاړ", "haɣa lāṛ", "he went"),
        ("هغه لاړه", "haɣa lāṛa", "she went"),
        ("موږ لاړو", "muẓ̌ lāṛu", "we went"),
        ("هغوی لاړل", "haɣwi lāṛəl", "they went"),
    ],
    "future": [
        ("زه به ځم", "zə bə dzəm", "I will go"),
        ("ته به ځې", "tə bə dze", "you will go (familiar)"),
        ("هغه به ځي", "haɣa bə dzi", "he/she will go"),
        ("موږ به ځو", "muẓ̌ bə dzu", "we will go"),
        ("تاسې به ځئ", "tāsə bə dzəy", "you will go (plural/formal)"),
        ("هغوی به ځي", "haɣwi bə dzi", "they will go"),
    ],
}

ENTRIES.append({
    "key": "p21_tenses",
    "name": "Pashto Verb Tenses in Sentences",
    "group": "Compounded",
    "ladder_rank": 21,
    "ladder_tier": "compounded",
    "description": (
        "The Pashto verb system in action: the verb تلل (tləl - to go) "
        "conjugated through present, past, and future, six persons each - "
        "eighteen translated sentences total. Present uses the present stem "
        "(ځ-): زه ځم (zə dzəm - I go), ته ځې (tə dze - you go), هغه ځي "
        "(haɣa dzi - he goes), موږ ځو (muẓ̌ dzu - we go), تاسې ځئ (tāsə "
        "dzəy - you go formal), هغوی ځي (haɣwi dzi - they go). Past uses "
        "the past stem (لاړ-): زه لاړم (zə lāṛəm - I went), ته لاړې (tə "
        "lāṛe), هغه لاړ/لاړه (haɣa lāṛ/lāṛa - he/she went), موږ لاړو "
        "(muẓ̌ lāṛu), هغوی لاړل (haɣwi lāṛəl). Future is the particle به "
        "(bə) before the present: زه به ځم (zə bə dzəm - I will go), and so "
        "through all six persons. The two-stem system is the whole secret: "
        "learn the present stem and the past stem of each verb and every "
        "tense follows."
    ),
    "how_it_works": (
        "Every Pashto verb has two stems. The present stem builds the "
        "present (زه ځم) and the future (به + present: زه به ځم). The past "
        "stem builds the simple past (زه لاړم). For تلل the stems are "
        "ځ- (present) and لاړ- (past) - suppletive, a famous irregularity "
        "worth memorizing early. Person endings attach to the stem: -م for "
        "I, -ې for familiar you, no ending (or -ه for feminine) for he/she, "
        "-و for we, -ئ for formal you, -ي for they. In the past, feminine "
        "subjects mark the verb: هغه لاړه (she went) vs هغه لاړ (he went). "
        "Apply the same skeleton to کول (present stem کو-, past stem وکړ-) "
        "and خوړل (present stem خور-, past stem وخوړ-) and the system "
        "repeats across the whole verb lexicon."
    ),
    "key_points": [
        "Two stems per verb: present stem (present + future) and past stem (past) - the whole tense system.",
        "Present: stem + person endings - زه ځم, ته ځې, هغه ځي, موږ ځو, تاسې ځئ, هغوی ځي.",
        "Past: past stem + endings - زه لاړم, ته لاړې, هغه لاړ/لاړه, موږ لاړو, هغوی لاړل.",
        "Future: به + present verb - زه به ځم through all six persons.",
        "تلل is suppletive: present stem ځ-, past stem لاړ- - memorize both.",
        "Feminine past marks the verb: هغه لاړه (she went) vs هغه لاړ (he went).",
        "Same skeleton fits کول (کو-/وکړ-) and خوړل (خور-/وخوړ-) - the pattern is universal.",
    ],
    "requirements": [
        "Conjugate تلل aloud through all three tenses until the stems are automatic.",
        "Learn the two stems of every new verb from this record onward.",
        "Write ten sentences in each tense about your own yesterday, today, and tomorrow.",
        "Drill the feminine past endings with هغه لاړه until natural.",
    ],
    "standards": [
        "Conjugation follows the standard grammatical description in the cited references.",
        "The suppletive stems of تلل/راتلل are standard across dialects.",
        "Transliteration matches the scheme fixed in record 2.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats each verb as a living action "
        "with two sworn shapes: the present shape (the action awake) and "
        "the past shape (the action remembered). به is the seal of the "
        "future - press it before the present and tomorrow obeys. Learn "
        "both shapes of every action, seal the future with به, and time "
        "itself conjugates at your command."
    ),
    "demo_key": "tenses",
    "demo_data": TENSE_21,
})

# ---------------------------------------------------------------- record 22

QA_22 = [
    ("ستا نوم څه دی؟", "stā num tsə day", "What is your name?",
     "زما نوم احمد دی", "zmā num ahmad day", "My name is Ahmad.",
     "Names: سوال with څه, ځواب with the name in the same frame."),
    ("ته له کومه یې؟", "tə lə kuma ye", "Where are you from?",
     "زه له کندهاره یم", "zə lə kandahāra yəm", "I am from Kandahar.",
     "Origin: له کومه (from where) answered with له + place."),
    ("ته چېرته اوسې؟", "tə čerta ose", "Where do you live?",
     "زه په پېښور کې اوسم", "zə pə pex̌awar ke osəm", "I live in Peshawar.",
     "Residence: چېرته answered with په + place کې."),
    ("څو کلن یې؟", "tso kālən ye", "How old are you?",
     "زه شل کلن یم", "zə šəl kālən yəm", "I am twenty years old.",
     "Age: څو کلن answered with number + کلن."),
    ("ته څه کار کوې؟", "tə tsə kār kawe", "What work do you do?",
     "زه ښوونکی یم", "zə x̌owunkay yəm", "I am a teacher.",
     "Occupation: څه کار answered with the job noun."),
    ("ستا مور څنګه ده؟", "stā mor tsənga da", "How is your mother?",
     "هغه ښه ده، مننه", "haɣa x̌a da, manəna", "She is well, thank you.",
     "Family health: څنګه answered with the condition."),
    ("کله راغلې؟", "kəla rāɣle", "When did you (fem.) come?",
     "زه پرون راغلم", "zə parun rāɣləm", "I came yesterday.",
     "Past time: کله answered with پرون/نن/a date."),
    ("ولې نه راغلې؟", "walə nə rāɣle", "Why did you (fem.) not come?",
     "زه ناروغه وم", "zə nāroɣa wəm", "I was sick.",
     "Reason: ولې answered with the cause."),
    ("دا کتاب د چا دی؟", "dā kitāb də čā day", "Whose book is this?",
     "دا زما کتاب دی", "dā zmā kitāb day", "This is my book.",
     "Possession: د چا answered with the possessive."),
    ("کوم رنګ خوښوې؟", "kum rang xoṣ̌awe", "Which color do you like?",
     "شین رنګ خوښوم", "šin rang xoṣ̌awəm", "I like the blue color.",
     "Preference: کوم answered with the chosen item."),
    ("څومره وخت نیسي؟", "tsumra waxt nisi", "How much time does it take?",
     "یو ساعت نیسي", "yaw sāat nisi", "It takes one hour.",
     "Duration: څومره answered with the measure."),
    ("بجې څو دي؟", "baje tso di", "What time is it?",
     "درې بجې دي", "dre baje di", "It is three o'clock.",
     "Clock time: څو answered with number + بجې."),
    ("تمځای لېره دی؟", "tamdzāy lera day", "Is the station far?",
     "نه، نږدې دی", "na, naǵde day", "No, it is near.",
     "Yes/no with نه/هو: short answers are complete."),
    ("چای څښې؟", "čāy tsṣ̌e", "Will you have tea?",
     "هو، مننه", "ho, manəna", "Yes, thank you.",
     "Offers: هو/نه with مننه - politeness sealed."),
    ("تاسو پښتو وایئ؟", "tāso paʂto wāyəy", "Do you (formal) speak Pashto?",
     "هو، لږ لږ", "ho, ləǵ ləǵ", "Yes, a little.",
     "Ability: هو/نه with the degree - لږ لږ is honest."),
    ("دا څنګه کار کوي؟", "dā tsənga kār kawi", "How does this work?",
     "تڼۍ کېکاږه", "ṭaṇəi keṉkāǵa", "Press the button.",
     "Method: څنګه answered with the instruction."),
    ("څوک دروازه ټکوي؟", "tsok darwāza ṭakawi", "Who is knocking at the door?",
     "مېلمه دی", "melma day", "It is a guest.",
     "Identity: څوک answered with the person."),
    ("ولې ژاړې؟", "walə žāṛe", "Why are you crying?",
     "ګوته مې خوږېږي", "gota me xoǵeǵi", "My finger hurts.",
     "Feelings: ولې answered with the true cause."),
    ("سبا څه کوې؟", "sabā tsə kawe", "What are you doing tomorrow?",
     "سبا ښوونځي ته ځم", "sabā x̌owənǵi ta dzəm", "Tomorrow I go to school.",
     "Plans: future answered with به or present-for-future."),
    ("ستا خوښه څه ده؟", "stā xoṣ̌a tsə da", "What is your favorite?",
     "زما خوښه پلو دی", "zmā xoṣ̌a palaw day", "My favorite is pilaf.",
     "Favorites: the خوښه frame works for anything."),
]

ENTRIES.append({
    "key": "p22_qa",
    "name": "Pashto Questions and Answers",
    "group": "Advanced",
    "ladder_rank": 22,
    "ladder_tier": "advanced",
    "description": (
        "Twenty question-and-answer pairs covering who, what, where, when, "
        "why, and how - each pair with transliteration, English "
        "translation, and a usage note. The pairs walk through a whole "
        "first conversation: name (ستا نوم څه دی؟), origin (ته له کومه "
        "یې؟), residence (ته چېرته اوسې؟), age (څو کلن یې؟), work (ته څه "
        "کار کوې؟), family health (ستا مور څنګه ده؟), past events (کله "
        "راغلې؟ / ولې نه راغلې؟), possession (دا کتاب د چا دی؟), preference "
        "(کوم رنګ خوښوې؟), duration (څومره وخت نیسي؟), clock time (بجې څو "
        "دي؟), distance (تمځای لېره دی؟), offers (چای څښې؟), ability (تاسو "
        "پښتو وایئ؟), method (دا څنګه کار کوي؟), identity (څوک دروازه "
        "ټکوي؟), feelings (ولې ژاړې؟), plans (سبا څه کوې؟), and favorites "
        "(ستا خوښه څه ده؟)."
    ),
    "how_it_works": (
        "Each interrogative opens its question and dictates the answer's "
        "shape: څوک asks for a person, څه for a thing, چېرته for a place "
        "(answered with په/کې), کله for a time, ولې for a reason, څومره for "
        "a measure, کوم for a choice. The verb stays last in both question "
        "and answer - the SOV covenant never breaks. Yes/no questions need "
        "no special word: چای څښې؟ (will you have tea?) is answered هو/نه. "
        "Notice the feminine agreement threading through: کله راغلې؟ and "
        "ولې نه راغلې؟ mark the -ې because the one asked is a woman. "
        "Practice each pair both ways: ask it, answer it, then swap roles."
    ),
    "key_points": [
        "20 Q/A pairs across who/what/where/when/why/how - a complete first conversation.",
        "Each interrogative dictates the answer shape: چېرته→place, کله→time, ولې→reason, څومره→measure.",
        "Verb stays last in questions AND answers - the SOV covenant never breaks.",
        "Yes/no questions need no marker: چای څښې؟ → هو، مننه.",
        "Feminine agreement threads through: راغلې، نه راغلې mark the woman asked.",
        "The خوښه frame (ستا خوښه څه ده؟) asks favorites about anything.",
        "Practice both roles: ask it, answer it, swap.",
    ],
    "requirements": [
        "Memorize the six core interrogatives and their answer shapes.",
        "Role-play all 20 pairs with a partner, swapping asker and answerer.",
        "Answer every question about yourself truthfully to build fluency.",
        "Keep the verb last even when the question gets long.",
    ],
    "standards": [
        "Interrogative usage follows the standard grammatical description in the cited references.",
        "Answer patterns reflect standard Pashto conversational norms.",
        "Transliteration matches the scheme fixed in record 2.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats each question as a key and each "
        "answer as the lock it was cut for: څوک opens persons, څه opens "
        "things, چېرته opens places, کله opens times, ولې opens reasons. "
        "Twenty keys, twenty locks, each pair sealed with a usage note. "
        "Carry the keys and no door in the language stays shut."
    ),
    "demo_key": "pairs",
    "demo_data": {"kind": "questions-answers", "pairs": QA_22},
})

# ---------------------------------------------------------------- record 23

CMD_23 = [
    ("راشه", "rāša", "come! (familiar)", "راشئ", "rāšəy", "come! (formal/plural)",
     "Motion verbs: راتلل → راشه/راشئ."),
    ("ځه", "dza", "go! (familiar)", "ځئ", "dzəy", "go! (formal/plural)",
     "تلل → ځه/ځئ; the everyday dismissal and send-off."),
    ("وخوره", "woxora", "eat! (familiar)", "وخورئ", "woxorəy", "eat! (formal/plural)",
     "خوړل → وخوره/وخورئ; said to every guest."),
    ("وڅښه", "wotsṣ̌a", "drink! (familiar)", "وڅښئ", "wotsṣ̌əy", "drink! (formal/plural)",
     "څښل → وڅښه/وڅښئ; the tea command."),
    ("ووایه", "wuwāya", "say!/tell! (familiar)", "ووایئ", "wuwāyəy", "say!/tell! (formal/plural)",
     "ویل → ووایه/ووایئ; asking for speech."),
    ("واوره", "wāwra", "listen! (familiar)", "واورئ", "wāwrəy", "listen! (formal/plural)",
     "اورېدل → واوره/واورئ; commanding attention."),
    ("وګوره", "wagora", "look! (familiar)", "وګورئ", "wagorəy", "look! (formal/plural)",
     "لیدل → وګوره/وګورئ; directing the eyes."),
    ("ولیکه", "walika", "write! (familiar)", "ولیکئ", "walikəy", "write! (formal/plural)",
     "لیکل → ولیکه/ولیکئ; the classroom command."),
    ("ولوله", "walwala", "read! (familiar)", "ولولئ", "walwaləy", "read! (formal/plural)",
     "لوستل → ولوله/ولولئ; opening the book."),
    ("پرانیزه", "prāniza", "open! (familiar)", "پرانیزی", "prānizəy", "open! (formal/plural)",
     "پرانیستل → پرانیزه/پرانیزی; doors and books."),
    ("وتړه", "watṛa", "close! (familiar)", "وتړئ", "watṛəy", "close! (formal/plural)",
     "تړل → وتړه/وتړئ; windows and doors."),
    ("کېنه", "kena", "sit! (familiar)", "کېنئ", "kenəy", "sit! (formal/plural)",
     "کېناستل → کېنه/کېنئ; seating the guest."),
    ("ودرېږه", "wadreǵa", "stand up! (familiar)", "ودرېږئ", "wadreǵəy", "stand up! (formal/plural)",
     "درېدل → ودرېږه/ودرېږئ; respect and readiness."),
    ("مرسته وکړه", "mrasta wakṛa", "help! (familiar)", "مرسته وکړئ", "mrasta wakṛəy", "help! (formal/plural)",
     "مرسته کول → وکړه/وکړئ; the call for aid."),
    ("مه ځه", "ma dza", "do not go! (familiar)", "مه ځئ", "ma dzəy", "do not go! (formal/plural)",
     "Negative commands use مه + familiar/formal stem."),
    ("مه وېرېږه", "ma wereǵa", "do not fear! (familiar)", "مه وېرېږئ", "ma wereǵəy", "do not fear! (formal/plural)",
     "Comfort: مه + verb soothes in both registers."),
    ("لطفاً راشئ", "lutfan rāšəy", "please come (formal)", "مهرباني وکړئ راشئ", "mehrabāni wakṛəy rāšəy", "kindly come (very formal)",
     "مهرباني وکړئ lifts any command to high politeness."),
    ("کتاب راوړه", "kitāb rāwṛa", "bring the book (familiar)", "کتاب راوړئ", "kitāb rāwṛəy", "bring the book (formal)",
     "راوړل (to bring): راوړه/راوړئ - fetching things."),
    ("پیسې ورکړه", "payse wərkṛa", "pay! (familiar)", "پیسې ورکړئ", "payse wərkṛəy", "pay! (formal/plural)",
     "ورکول → ورکړه/ورکړئ; settling accounts."),
    ("خدای دې وساته", "xudāy de wasāta", "may God keep you (blessing)", "خدای مو وساته", "xudāy mo wasāta", "may God keep you (formal blessing)",
     "Blessing-commands: دې for familiar, مو for formal."),
]

ENTRIES.append({
    "key": "p23_commands",
    "name": "Pashto Commands and Requests",
    "group": "Advanced",
    "ladder_rank": 23,
    "ladder_tier": "advanced",
    "description": (
        "Twenty imperative pairs - every command in familiar (ته) and "
        "formal/plural (تاسې) form, each with transliteration, English, "
        "and a note. The pairs cover motion (راشه/راشئ - come!, ځه/ځئ - "
        "go!), hospitality (وخوره/وخورئ - eat!, وڅښه/وڅښئ - drink!, کېنه/کېنئ "
        "- sit!), speech (ووایه/ووایئ - say!, واوره/واورئ - listen!), "
        "senses (وګوره/وګورئ - look!), school (ولیکه/ولیکئ - write!, "
        "ولوله/ولولئ - read!), the house (پرانیزه/پرانیزی - open!, وتړه/وتړئ "
        "- close!, ودرېږه/ودرېږئ - stand up!), aid (مرسته وکړه/وکړئ - "
        "help!), prohibition (مه ځه/ځئ - do not go!, مه وېرېږه/وېرېږئ - do "
        "not fear!), escalating politeness (لطفاً راشئ, مهرباني وکړئ "
        "راشئ), fetching (کتاب راوړه/راوړئ), paying (پیسې ورکړه/ورکړئ), and "
        "blessing-commands (خدای دې وساته / خدای مو وساته)."
    ),
    "how_it_works": (
        "The familiar imperative is the present stem, often with the "
        "prefix و- (وخوره, وڅښه, ووایه, وګوره); the formal/plural adds -ئ "
        "(راشئ, ځئ, وخورئ, وکړئ). Negative commands replace everything "
        "with مه + the stem: مه ځه, مه وېرېږه. Politeness is a ladder: "
        "bare familiar (راشه) → formal (راشئ) → لطفاً + formal (لطفاً راشئ) "
        "→ مهرباني وکړئ + formal (مهرباني وکړئ راشئ). Use the familiar only "
        "with friends, family, children, and those who invite it; default "
        "to the formal with everyone else - this is the single most "
        "noticed politeness rule in the language. Blessing-commands use دې "
        "(familiar) or مو (formal): خدای دې وساته vs خدای مو وساته."
    ),
    "key_points": [
        "20 commands, each in familiar ته-form and formal/plural تاسې-form with notes.",
        "Familiar imperative = present stem (often و- prefix); formal adds -ئ.",
        "Negative commands: مه + stem - مه ځه, مه وېرېږه.",
        "Politeness ladder: راشه → راشئ → لطفاً راشئ → مهرباني وکړئ راشئ.",
        "Default to the formal with strangers and elders - the most noticed rule in the language.",
        "Blessing-commands: خدای دې وساته (familiar) vs خدای مو وساته (formal).",
        "Hospitality commands (وخوره, وڅښه, کېنه) are said to every guest - learn them first.",
    ],
    "requirements": [
        "Drill all 20 pairs aloud in both registers until the -ئ ending is automatic.",
        "Practice the politeness ladder on five commands, climbing all four rungs.",
        "Use only formal commands with elders for one full week.",
        "Master the مه prohibitions - they prevent the common mistakes.",
    ],
    "standards": [
        "Imperative forms follow the standard grammatical description in the cited references.",
        "The politeness ladder reflects standard Pashto sociolinguistic norms.",
        "Transliteration matches the scheme fixed in record 2.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats each command as a sworn order "
        "with two seals: the familiar seal for the inner circle, the "
        "formal seal for the world. مه is the seal of restraint - it "
        "forbids. The politeness ladder is the ascent from order to "
        "blessing: راشه, راشئ, لطفاً راشئ, مهرباني وکړئ راشئ. Seal each of "
        "the 20 in both forms, climb the ladder deliberately, and every "
        "request lands exactly where it should."
    ),
    "demo_key": "pairs",
    "demo_data": {"kind": "commands-requests", "pairs": CMD_23},
})

# ---------------------------------------------------------------- record 24

DESC_24 = _S(
    ("زما پلار یو پیاوړی سړی دی، اوږدې وېښتې او مهربانې سترګې لري", "zmā plār yaw pyāwaṛay saṛay day, uǧde wex̌te aw mehrabāne starge lari", "My father is a strong man, with long mustaches and kind eyes."),
    ("زما مور یوه ښکلې ښځه ده، تل موسکېږي", "zmā mor yawa x̌kule x̌əza da, təl muskeǵi", "My mother is a beautiful woman; she is always smiling."),
    ("زما ورور ځوان دی، چټک ځغلي او فوټبال خوښوي", "zmā wror dzwān day, čaṭak dzɣali aw fuṭbāl xoṣ̌awi", "My brother is young; he runs fast and likes football."),
    ("زما خور کوچنۍ ده، خو ډېره هوښیاره ده", "zmā xor kučnaəi da, xo ḍera hoṣ̌yāra da", "My sister is little, but she is very clever."),
    ("زموږ ښوونکی یو زوړ او پوه سړی دی", "zmuẓ̌ x̌owunkay yaw zoṛ aw poh saṛay day", "Our teacher is an old and wise man."),
    ("هغه نجلۍ اوږده، نرۍ او خوش اخلاقه ده", "haɣa njaləi uǧda, narəi aw xoš axlāqa da", "That girl is tall, slim, and good-mannered."),
    ("کابل یو لوی او ګڼه ګوڼه ښار دی", "kābal yaw loy aw gaṇa gūṇa x̌ār day", "Kabul is a big and crowded city."),
    ("کندهار ګرم دی، خو مېوې یې خوږې دي", "kandahār garam day, xo mewe ye xoǵe di", "Kandahar is hot, but its fruits are sweet."),
    ("پېښور تاریخي ښار دی، بازارونه یې لرغوني دي", "pex̌awar tārixi x̌ār day, bāzaruna ye larɣuni di", "Peshawar is a historic city; its bazaars are ancient."),
    ("زموږ کلی د غرونو په لمن کې پروت دی", "zmuẓ̌ kalay də ɣruno pə lman ke prot day", "Our village lies at the foot of the mountains."),
    ("سیند ژور او چټک بهېږي", "sind žwar aw čaṭak beheǵi", "The river is deep and flows fast."),
    ("باغ شین دی، ګلان پکې غوړېدلي دي", "bāɣ šin day, gulān pəke ɣwoṛedəli di", "The garden is green; flowers are blooming in it."),
    ("دا کور زوړ دی، خو دېوالونه یې ټینګ دي", "dā kor zoṛ day, xo dewāluna ye ṭing di", "This house is old, but its walls are solid."),
    ("کوټه پراخه او رڼا ده", "koṭa parāxa aw raṇā da", "The room is spacious and bright."),
    ("مېز لرګین دی او څوکۍ نرمې دي", "mez largin day aw tsawkəi narme di", "The table is wooden and the chairs are soft."),
    ("اس تور دی، سترګې یې ځلېږي", "ās tor day, starge ye dzaleǵi", "The horse is black; its eyes shine."),
    ("سپوږمۍ ګرده او ځلانده ده", "spoǧməi garda aw dzlānda da", "The moon is round and radiant."),
    ("شپه چوپه ده، یوازې سپی غاپي", "špa čupa da, yawāze spay ɣāpi", "The night is quiet; only a dog barks."),
    ("سهار تازه دی، مرغان چغې وهي", "sahār tāza day, marɣān čaɣe wahi", "The morning is fresh; the birds are singing."),
    ("ژمی سخت دی، واوره هر ځای ده", "žmay saxt day, wāwra har dzāy da", "Winter is harsh; snow is everywhere."),
)

ENTRIES.append({
    "key": "p24_descriptions",
    "name": "Pashto Descriptions of People and Places",
    "group": "Advanced",
    "ladder_rank": 24,
    "ladder_tier": "advanced",
    "description": (
        "Twenty detailed descriptive sentences - people and places painted "
        "in full color, each with transliteration and English translation. "
        "People: the father (پیاوړی سړی - strong man, with long mustaches "
        "and kind eyes), the mother (ښکلې ښځه - beautiful woman, always "
        "smiling), the brother (ځوان - young, fast runner, football lover), "
        "the sister (کوچنۍ خو هوښیاره - little but clever), the teacher "
        "(زوړ او پوه - old and wise), the girl (اوږده، نرۍ، خوش اخلاقه - "
        "tall, slim, good-mannered). Places: Kabul (لوی او ګڼه ګوڼه - big "
        "and crowded), Kandahar (ګرم - hot, with sweet fruits), Peshawar "
        "(تاریخي - historic, with ancient bazaars), the village (د غرونو "
        "په لمن کې - at the mountains' foot), the river (ژور او چټک - deep "
        "and fast), the garden (شین - green, with blooming flowers). Things: "
        "the old house with solid walls, the spacious bright room, the "
        "wooden table and soft chairs, the black horse with shining eyes, "
        "the round radiant moon, the quiet night, the fresh morning, the "
        "harsh winter."
    ),
    "how_it_works": (
        "Descriptions stack adjectives before nouns and clauses after them: "
        "یو پیاوړی سړی (a strong man) grows into یو پیاوړی سړی دی، اوږدې "
        "وېښتې او مهربانې سترګې لري (is a strong man, has long mustaches "
        "and kind eyes). Contrast with خو (but): کوچنۍ ده، خو هوښیاره ده "
        "(she is little, but she is clever); زوړ دی، خو دېوالونه یې ټینګ "
        "دي (it is old, but its walls are solid). Possession describes "
        "through لري (has): سترګې لري, دېوالونه یې ټینګ دي. Location "
        "describes through په کې (in it) and تر څنګ (beside). Build your "
        "own by taking one record-6 adjective, one record-4 noun, and one "
        "contrast or possession clause - the formula never fails."
    ),
    "key_points": [
        "20 detailed descriptions of people, places, and things - full-color sentences.",
        "Stacking formula: adjective + noun + contrast/possession/location clause.",
        "Contrast with خو (but): کوچنۍ ده، خو هوښیاره ده - the engine of interesting description.",
        "Possession describes: سترګې لري (has eyes), دېوالونه یې ټینګ دي (its walls are solid).",
        "Location describes: د غرونو په لمن کې (at the mountains' foot), پکې (in it).",
        "Cities described: Kabul, Kandahar, Peshawar - the three anchors of the Pashto world.",
        "Build your own: one adjective + one noun + one clause - the formula never fails.",
    ],
    "requirements": [
        "Describe five people you know using the stacking formula.",
        "Describe three places using contrast and location clauses.",
        "Use خو in ten original descriptive sentences.",
        "Read all 20 aloud with the descriptive rhythm - slow and painted.",
    ],
    "standards": [
        "Descriptive constructions follow standard Pashto usage.",
        "Place descriptions reflect the real cities and landscapes of the Pashto world.",
        "Transliteration matches the scheme fixed in record 2.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats description as sworn painting: "
        "each adjective a color sealed to its noun, each خو a blade that "
        "cuts the expected in two, each لري a hand placing possession "
        "where it belongs. Twenty paintings hang in this record. Study "
        "the brushwork, take up the brush, and paint your own people and "
        "places in covenant colors."
    ),
    "demo_key": "sentences",
    "demo_data": {"topic": "Pashto Descriptions of People and Places", "sentences": DESC_24},
})

# ---------------------------------------------------------------- records 25-27: stories

STORY_25 = [
    ("احمد یو شپون دی", "ahmad yaw špun day", "Ahmad is a shepherd."),
    ("هغه هر سهار وختي پاڅي", "haɣa har sahār waxti pātsi", "He wakes up early every morning."),
    ("هغه خپلې پسونه غرونو ته بیايي", "haɣa xpalə pasuna ɣruno ta byāyi", "He takes his sheep to the mountains."),
    ("لار اوږده ده، خو هغه سندرې وايي", "lār uǧda da, xo haɣa sandare wāyi", "The way is long, but he sings songs."),
    ("غرمې ته هغه د یوې ونې لاندې کېني", "ɣarme ta haɣa də yawe wəṇe lānde keni", "At noon he sits under a tree."),
    ("هغه ډوډۍ خوري او اوبه څښي", "haɣa ḍoḍəi xori aw obə tsṣ̌i", "He eats bread and drinks water."),
    ("مازدیګر هغه پسونه بېرته راولي", "māzdigar haɣa pasuna berta rāwali", "In the afternoon he brings the sheep back."),
    ("مور یې په ور کې انتظار باسي", "mor ye pə wər ke intizār bāsi", "His mother waits for him at the door."),
    ("هغه خپلې کیسې ورته کوي", "haɣa xpalə kise wərta kawi", "He tells her his stories."),
    ("شپې ته هغه خوشحاله خوب کوي", "špe ta haɣa xošhāla xob kawi", "At night he sleeps happily."),
]

STORY_26 = [
    ("پرون زموږ اوښ ورک شو", "parun zmuẓ̌ ux̌ wərk šu", "Yesterday our camel went missing."),
    ("پلار مې وختي پاڅېد او وېې لټاوه", "plār me waxti pātsed aw ye laṭāwa", "My father woke up early and searched for it."),
    ("هغه کلي ته لاړ او له خلکو یې وپوښتل", "haɣa kalay ta lāṛ aw lə xalko ye wapoxtəl", "He went to the village and asked the people."),
    ("یو سړي وویل: ما د سیند تر څنګ ولید", "yaw saṛi wuwel: mā də sind tər tsang walid", "A man said: I saw it beside the river."),
    ("پلار مې سیند ته لاړ", "plār me sind ta lāṛ", "My father went to the river."),
    ("اوښ هلته ولاړ و او اوبه یې څښلې", "ux̌ halta wlāṛ wu aw obə ye tsṣ̌əle", "The camel was standing there, drinking water."),
    ("پلار مې وخندل او اوښ یې راووست", "plār me waxandal aw ux̌ ye rāwust", "My father laughed and brought the camel back."),
    ("مور مې ډوډۍ پخه کړه او ټولو وخوړله", "mor me ḍoḍəi paxa kṛa aw ṭolo woxoṛla", "My mother cooked bread and everyone ate it."),
    ("اوښ بېرته خپل ځای ته لاړ", "ux̌ berta xpal dzāy ta lāṛ", "The camel went back to its place."),
    ("موږ ټول خوشحاله شو", "muẓ̌ ṭol xošhāla šu", "We all became happy."),
]

STORY_27 = [
    ("سبا به زموږ په کلي کې نوی ښوونځی پرانیزي", "sabā bə zmuẓ̌ pə kalay ke naway x̌owənǵay prānizi", "Tomorrow a new school will open in our village."),
    ("ټول ماشومان به هلته زده کړه کوي", "ṭol māšumān bə halta zda kṛa kawi", "All the children will study there."),
    ("که ښوونکی ښه وي، ماشومان به ډېر زده کړي", "ka x̌owunkay x̌a wi, māšumān bə ḍer zda kṛi", "If the teacher is good, the children will learn much."),
    ("زما خور به هم هلته ځي", "zmā xor bə ham halta dzi", "My sister will go there too."),
    ("هغه به کتابونه لولي او کیسې به لیکي", "haɣa bə kitābuna loli aw kise bə liki", "She will read books and write stories."),
    ("که باران ونه وریږي، موږ به په میدان کې ولوبېږو", "ka bārān wəna wriǵi, muẓ̌ bə pə maydān ke walobeǵu", "If it does not rain, we will play in the field."),
    ("پلار مې وايي: که زحمت وباسې، بریالي به شې", "plār me wāyi: ka zahmat wabāse, baryāli bə še", "My father says: if you work hard, you will succeed."),
    ("زه به هره ورځ وختي پاڅم", "zə bə hara wrədz waxti pātsəm", "I will wake up early every day."),
    ("موږ به نوی کتابتون هم جوړ کړو", "muẓ̌ bə naway kitābtun ham joṛ kṛu", "We will also build a new library."),
    ("زموږ کلی به د پوهې کور شي", "zmuẓ̌ kalay bə də pohe kor ši", "Our village will become a house of knowledge."),
]

STORIES = [
    ("p25_story1", "Pashto Story I: The Shepherd Boy", STORY_25,
     "A ten-sentence simple story in the present tense: احمد the shepherd wakes early, takes his sheep to the mountains, sings on the long way, rests under a tree at noon, eats bread, brings the flock back in the afternoon, tells his mother his stories at the door, and sleeps happily at night. Line-by-line English translation; the present tense lives inside a real day.",
     "The Signature Pashto Method tells the day as a sworn circle: dawn, mountain, noon, return, story, sleep. Ten sentences, one circle, no break. Walk the circle with احمد and the present tense walks with you.",
     "story-present"),
    ("p26_story2", "Pashto Story II: The Lost Camel", STORY_26,
     "A ten-sentence story in the past tense: yesterday the family's camel went missing, the father woke early and searched, asked in the village, learned it was seen by the river, found it drinking water, laughed and brought it back, the mother cooked bread, everyone ate, the camel returned to its place, and all were happy. Line-by-line English translation; the past tense - and the ergative ما/یې forms - live inside a real search.",
     "The Signature Pashto Method tells the search as a sworn path: loss, seeking, asking, finding, return, joy. Ten sentences, one path, the past tense marking every step. Walk the path and the past tense is yours.",
     "story-past"),
    ("p27_story3", "Pashto Story III: The New School", STORY_27,
     "A ten-sentence story in the future and conditional: tomorrow a new school will open in the village, all children will study there, if the teacher is good they will learn much, the sister will go too, she will read and write, if it does not rain they will play, the father's counsel (if you work hard, you will succeed), the resolve to wake early, the plan for a library, and the vision - the village will become a house of knowledge. Line-by-line English translation; به-futures and که-conditionals live inside a real hope.",
     "The Signature Pashto Method tells the hope as a sworn vow: tomorrow, the school, the learning, the library, the house of knowledge. Ten sentences, one vow, every به a seal on the future. Speak the vow and the future answers.",
     "story-future"),
]

for _i, (_key, _name, _lines, _desc, _sig, _kind) in enumerate(STORIES):
    ENTRIES.append({
        "key": _key,
        "name": _name,
        "group": "Advanced",
        "ladder_rank": 25 + _i,
        "ladder_tier": "advanced",
        "description": _desc,
        "how_it_works": (
            "Ten sentences, each with transliteration and a line-by-line "
            "English translation. Read the whole story in Pashto first "
            "without stopping - let the unknown words blur past. Then read "
            "sentence by sentence with the translation, finding the verbs "
            "you know from records 5 and 21 and the nouns from record 4. "
            "Then read the Pashto again: the story will now be transparent. "
            "Retell it in your own words, changing details (the shepherd "
            "becomes a farmer, the camel becomes a horse). The tense of the "
            "story - present, past, or future/conditional - is the grammar "
            "lesson; the plot is the memory palace."
        ),
        "key_points": [
            "10-sentence story with line-by-line English translation - a complete narrative, not fragments.",
            "Three-pass method: whole-story blur, sentence-by-sentence study, transparent re-read.",
            "The story's tense IS the grammar lesson: present in I, past in II, future/conditional in III.",
            "Retell with changed details to make the story yours.",
            "Find the record-4 nouns, record-5 verbs, and record-21 tenses inside every line.",
        ],
        "requirements": [
            "Read each story three times by the three-pass method.",
            "Retell each story in your own words, aloud, changing three details.",
            "Write a five-sentence continuation for one story.",
            "Identify every verb tense used in each story.",
        ],
        "standards": [
            "Stories use standard written Pashto (Northern-based).",
            "Tense usage follows the standard grammatical description.",
            "Transliteration matches the scheme fixed in record 2.",
        ],
        "citations": list(CIT_ALL),
        "sig_lens": _sig,
        "demo_key": "story",
        "demo_data": {"title": _name, "lines": _lines},
    })

# ---------------------------------------------------------------- record 28

IDIOMS_28 = [
    ("ورو ورو ځي، لرې ځي", "wro wro dzi, lare dzi",
     "Slowly he goes, far he goes", "Slow and steady wins the race.",
     "ورو ورو کار کوه، لرې به ورسې", "wro wro kār kawa, lare bə warse", "Work slowly and steadily; you will go far."),
    ("څه چې کرې، هغه به رېبې", "tsə če kare, haɣa bə rebe",
     "What you sow, that you will reap", "Actions have consequences.",
     "ښه وکړه، ښه به رېبې", "x̌a wakṛa, x̌a bə rebe", "Do good, and you will reap good."),
    ("په خوله کې شات، په زړه کې زهر", "pə xwəla ke šāt, pə zṛa ke zahar",
     "Honey in the mouth, poison in the heart", "Beware flatterers with hidden malice.",
     "د هغه په خبرو مه غولېږه", "də haɣa pə xabaro ma ɣoleǵa", "Do not be deceived by his words."),
    ("یو لاس نه غږېږي", "yaw lās nə ɣaǵeǵi",
     "One hand does not clap", "Cooperation is necessary; nothing is done alone.",
     "راځئ یو ځای کار وکړو", "rādzəy yaw dzāy kār wakṛu", "Come, let us work together."),
    ("د پوهې رڼا تر لمر روښانه ده", "də pohe raṇā tər lmar rox̌āna da",
     "The light of knowledge is brighter than the sun", "Knowledge outshines everything.",
     "کتاب ولوله، رڼا به ومومې", "kitāb walwala, raṇā bə wamume", "Read books; you will find light."),
    ("صبر د بریا کیلي ده", "sabr də baryā kili da",
     "Patience is the key to success", "Endurance wins.",
     "صبر وکړه، بریا به درشي", "sabr wakṛa, baryā bə darši", "Be patient; success will come to you."),
    ("وخت له سرو زرو ګران دی", "waxt lə sro zaro grān day",
     "Time is more precious than red gold", "Do not waste time.",
     "وخت مه ضایع کوه", "waxt ma zāyi kawa", "Do not waste time."),
    ("ملګری په تنګسا کې پېژندل کېږي", "malgaray pə tangsā ke pežandal keǵi",
     "A friend is known in hardship", "True friends appear in difficulty.",
     "هغه زما رښتینی ملګری دی", "haɣa zmā rəxtinay malgaray day", "He is my true friend."),
    ("ژبه د زړه ژباړن ده", "žəba də zṛa žbāṛən da",
     "The tongue is the translator of the heart", "Speech reveals character.",
     "ښې خبرې کوه", "x̌e xabare kawa", "Speak good words."),
    ("کار له وینا ښه دی", "kār lə winā x̌a day",
     "Deed is better than word", "Actions speak louder than words.",
     "وینه پرېږده، کار وکړه", "wina preǵda, kār wakṛa", "Leave talk; do the work."),
    ("روغتیا تر ټولو لویه شتمني ده", "roɣtyā tər ṭolo loya šətmani da",
     "Health is the greatest wealth", "Guard your health above riches.",
     "روغتیا ته پام کوه", "roɣtyā ta pām kawa", "Take care of your health."),
    ("د علم حاصل تر مال غوره دی", "də ilm hāsil tər māl ɣwara day",
     "The harvest of knowledge is better than wealth", "Learning outlasts riches.",
     "علم زده کړه", "ilm zda kṛa", "Seek knowledge."),
    ("سپی غاپي، کاروان تېرېږي", "spay ɣāpi, kārwān tereǵi",
     "The dog barks, the caravan passes", "Ignore spiteful noise; keep going.",
     "خپل کار ته دوام ورکړه", "xpal kār ta dawām wərkṛa", "Continue your work."),
    ("هر چا ته خپل وطن کشمیر دی", "har čā ta xpal watan kašmir day",
     "To everyone, their homeland is Kashmir", "Everyone loves their homeland most.",
     "وطن مو ګران دی", "watan mo grān day", "Our homeland is dear to us."),
    ("اوبه چې تېرې شي، بېرته نه راځي", "obə če tere ši, berta nə rādzi",
     "Water that has flowed does not return", "The past cannot be undone.",
     "تېر وخت هېر کړه", "ter waxt her kṛa", "Forget the past."),
    ("ګل بې اغزو نه وي", "gul be aɣzo nə wi",
     "There is no rose without thorns", "Every good has its difficulty.",
     "زحمت وباسه، ګل به ومومې", "zahmat wabāsa, gul bə wamume", "Work hard; you will find the rose."),
    ("چې چاته ګور کیني، پخپله به پکې لوېږي", "če čāta gor kini, paxpala bə pəke loweǵi",
     "Who digs a pit for another falls into it himself", "Malice backfires.",
     "هېچاته بد مه غواړه", "hečāta bad ma ɣwāṛa", "Wish ill to no one."),
    ("د مور دعا قبوله ده", "də mor duā qabula da",
     "A mother's prayer is accepted", "Honor and heed your mother.",
     "د مور خبره واوره", "də mor xabara wāwra", "Listen to your mother's word."),
    ("د سهار وختي پاڅېدل برکت دی", "də sahār waxti pātsedal barkat day",
     "Rising early in the morning is a blessing", "The early riser prospers.",
     "سهار وختي پاڅه", "sahār waxti pātsa", "Wake up early in the morning."),
    ("نیمګړی کار دوه چنده ستړیا ده", "nimgaṛay kār dwa čanda staṛyā da",
     "A half-done job is double tiredness", "Finish what you start.",
     "کار پوره کړه", "kār pura kṛa", "Complete the work."),
]

ENTRIES.append({
    "key": "p28_idioms",
    "name": "Pashto Idioms and Proverbs",
    "group": "Advanced",
    "ladder_rank": 28,
    "ladder_tier": "advanced",
    "description": (
        "Twenty Pashto idioms and proverbs - each with transliteration, "
        "literal translation, real meaning, and an example sentence "
        "translated into English. The collection carries the moral "
        "philosophy of the Pashto world: patience and steady work (ورو "
        "ورو ځي، لرې ځي - slowly he goes, far he goes; صبر د بریا کیلي "
        "ده - patience is the key to success), consequence (څه چې کرې، "
        "هغه به رېبې - what you sow, you reap; چې چاته ګور کیني، پخپله به "
        "پکې لوېږي - who digs a pit for another falls in himself), "
        "knowledge (د پوهې رڼا تر لمر روښانه ده - knowledge outshines the "
        "sun; د علم حاصل تر مال غوره دی - learning outlasts wealth), "
        "time and health (وخت له سرو زرو ګران دی - time is precious; "
        "روغتیا تر ټولو لویه شتمني ده - health is the greatest wealth), "
        "character (په خوله کې شات، په زړه کې زهر - honey in the mouth, "
        "poison in the heart; ژبه د زړه ژباړن ده - speech reveals the "
        "heart; کار له وینا ښه دی - deed beats word), friendship (ملګری په "
        "تنګسا کې پېژندل کېږي - friends are known in hardship; یو لاس نه "
        "غږېږي - one hand does not clap), perseverance (سپی غاپي، کاروان "
        "تېرېږي - the caravan passes), homeland (هر چا ته خپل وطن کشمیر "
        "دی), acceptance (اوبه چې تېرې شي، بېرته نه راځي), balance (ګل بې "
        "اغزو نه وي - no rose without thorns), blessing (د مور دعا قبوله "
        "ده; د سهار وختي پاڅېدل برکت دی), and completion (نیمګړی کار دوه "
        "چنده ستړیا ده)."
    ),
    "how_it_works": (
        "A proverb is quoted whole - never paraphrased - at the moment it "
        "fits: say ورو ورو ځي، لرې ځي to the impatient, صبر د بریا کیلي ده "
        "to the struggling, څه چې کرې، هغه به رېبې as the warning. The "
        "literal translation shows the poetry; the real meaning shows the "
        "use; the example sentence shows the proverb alive in speech. "
        "Learn five proverbs deeply rather than twenty shallowly: know the "
        "occasion for each. Drop one proverb into conversation per week - "
        "native speakers will mark you as an insider the first time you "
        "use سپی غاپي، کاروان تېرېږي correctly."
    ),
    "key_points": [
        "20 idioms/proverbs: literal translation + real meaning + example sentence each.",
        "Proverbs are quoted whole, never paraphrased - learn the exact wording.",
        "Each proverb has its occasion: impatience, struggle, warning, comfort, praise.",
        "The moral core: patience, consequence, knowledge, time, health, character, friendship.",
        "One proverb used correctly marks you as an insider - deploy weekly.",
        "Learn five deeply before adding more; occasion-knowledge beats list-knowledge.",
    ],
    "requirements": [
        "Memorize ten proverbs word-for-word with their occasions.",
        "Use one proverb in real conversation each week.",
        "Explain the literal image and the real meaning of each to a partner.",
        "Collect two new proverbs from native speakers and add them to your set.",
    ],
    "standards": [
        "Proverbs are drawn from the traditional oral literature of the Pashto-speaking world.",
        "Wording follows widely attested standard forms.",
        "Transliteration matches the scheme fixed in record 2.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats each proverb as a covenant of "
        "the ancestors, sealed in a single sentence: twenty covenants, "
        "twenty occasions, never paraphrased, never broken. Quote the "
        "covenant whole at its hour - ورو ورو ځي، لرې ځي to the hasty, "
        "صبر د بریا کیلي ده to the weary - and the ancestors speak through "
        "you."
    ),
    "demo_key": "idioms",
    "demo_data": {"idioms": IDIOMS_28},
})

# ---------------------------------------------------------------- record 29

REG_29 = [
    ("سلام، څنګه یې؟", "salām, tsənga ye", "Hi, how are you? (familiar)",
     "سلام علیکم، تاسو څنګه یئ؟", "salām alaykum, tāso tsənga yəy", "Peace be upon you, how are you? (formal)",
     "Elders and strangers get سلام علیکم and the تاسې verb form."),
    ("ستا نوم څه دی؟", "stā num tsə day", "What is your name? (familiar)",
     "ستاسو نوم څه دی؟", "stāso num tsə day", "What is your name? (formal)",
     "First meetings with non-peers always take ستاسو."),
    ("راشه، کېنه", "rāša, kena", "Come, sit (familiar)",
     "راشئ، مهرباني وکړئ کېنئ", "rāšəy, mehrabāni wakṛəy kenəy", "Please come and be seated (formal)",
     "Hosting an elder: the formal imperative plus مهرباني وکړئ."),
    ("دا راوړه", "dā rāwṛa", "Bring this (familiar)",
     "مهرباني وکړئ دا راوړئ", "mehrabāni wakṛəy dā rāwṛəy", "Kindly bring this (formal)",
     "Requests upward use مهرباني وکړئ + formal imperative."),
    ("زه نه پوهېږم", "zə nə poheǵəm", "I do not understand (plain)",
     "بښنه غواړم، زه پوه نه شوم", "bax̌əna ɣwāṛəm, zə poh nə šwəm", "Excuse me, I did not understand (formal)",
     "Formal misunderstanding admits fault with بښنه غواړم."),
    ("بیا ووایه", "byā wuwāya", "Say it again (familiar)",
     "مهرباني وکړئ بیا یې ووایئ", "mehrabāni wakṛəy byā ye wuwāyəy", "Please say it again (formal)",
     "Asking an elder to repeat: soften with مهرباني وکړئ."),
    ("زه ځم", "zə dzəm", "I am going (plain)",
     "اجازه راکړئ، زه ځم", "ijāza rākṛəy, zə dzəm", "With your permission, I am leaving (formal)",
     "Leaving elders: اجازه (permission) frames the departure."),
    ("خدای پامان", "xudāy pāmān", "Goodbye (plain)",
     "خدای مو وساته، په مخه ښه", "xudāy mo wasāta, pə maxa x̌a", "May God keep you; go well (formal)",
     "Formal farewell stacks the blessing: خدای مو وساته."),
    ("مننه", "manəna", "Thanks (plain)",
     "ډېره مننه، الله دې اجر درکړي", "ḍera manəna, allāh de ajr darkṛi", "Thank you very much; may God reward you (formal)",
     "Deep gratitude invokes the divine reward."),
    ("وبخښه", "wobax̌a", "Forgive me (familiar)",
     "بښنه غواړم، ګناه مې وبخښئ", "bax̌əna ɣwāṛəm, gunāh me wobax̌əy", "I beg pardon; forgive my fault (formal)",
     "Formal apology names the fault: ګناه مې وبخښئ."),
    ("ګران مشره", "grān mašra", "Dear elder (letter opening, familiar)",
     "قدرمن مشره، سلامونه ومنئ", "qadarman mašra, salāmuna wamanəy", "Respected elder, accept my greetings (formal letter)",
     "Letters open with قدرمن and close with احتراماً."),
    ("کار دې څنګه دی؟", "kār de tsənga day", "How is your work? (familiar)",
     "کاروبار مو څنګه دی؟", "kārubār mo tsənga day", "How is your business? (formal)",
     "Business talk uses مو and the full noun کاروبار."),
    ("پیسې راکړه", "payse rākṛa", "Give me the money (familiar)",
     "مهرباني وکړئ پیسې راکړئ", "mehrabāni wakṛəy payse rākṛəy", "Kindly give the money (formal)",
     "Money requests are always softened upward."),
    ("چوپ شه", "čup ša", "Be quiet (familiar)",
     "مهرباني وکړئ لږ چوپ شئ", "mehrabāni wakṛəy ləǵ čup šəy", "Please be a little quiet (formal)",
     "Even correction is wrapped in مهرباني وکړئ and لږ."),
    ("زه به سبا درشم", "zə bə sabā daršəm", "I will come tomorrow (plain promise)",
     "ان شاء الله سبا به خدمت ته حاضر شم", "in šā allāh sabā bə xidmat ta hāzir šəm", "God willing, tomorrow I shall present myself in service (formal)",
     "Formal promises add ان شاء الله and خدمت - service language."),
]

ENTRIES.append({
    "key": "p29_registers",
    "name": "Pashto Formal and Polite Registers",
    "group": "Advanced",
    "ladder_rank": 29,
    "ladder_tier": "advanced",
    "description": (
        "Fifteen formal-vs-informal pairs - letters, business, and elders - "
        "each with transliteration, English, and a note on the politeness "
        "mechanics. The pairs cover greeting an elder (سلام علیکم، تاسو "
        "څنګه یئ؟), asking a name (ستاسو نوم څه دی؟), seating a guest "
        "(راشئ، مهرباني وکړئ کېنئ), making requests (مهرباني وکړئ دا "
        "راوړئ), admitting misunderstanding (بښنه غواړم، زه پوه نه شوم), "
        "asking for repetition (مهرباني وکړئ بیا یې ووایئ), taking leave "
        "(اجازه راکړئ، زه ځم), formal farewell (خدای مو وساته، په مخه ښه), "
        "deep thanks (ډېره مننه، الله دې اجر درکړي), formal apology (بښنه "
        "غواړم، ګناه مې وبخښئ), letter openings (قدرمن مشره، سلامونه ومنئ), "
        "business inquiry (کاروبار مو څنګه دی؟), money requests (مهرباني "
        "وکړئ پیسې راکړئ), polite correction (مهرباني وکړئ لږ چوپ شئ), and "
        "formal promises (ان شاء الله سبا به خدمت ته حاضر شم)."
    ),
    "how_it_works": (
        "Formality in Pashto is built from four tools: (1) the تاسې pronoun "
        "and its verb endings (-ئ) instead of ته; (2) the softener مهرباني "
        "وکړئ before any request; (3) the fault-admitter بښنه غواړم when "
        "anything goes wrong; (4) elevated vocabulary - قدرمن for dear, "
        "کاروبار for business, خدمت for service, اجازه for permission, "
        "احتراماً to close a letter. Stack the tools for maximum "
        "formality: مهرباني وکړئ + formal imperative + elevated noun. "
        "Blessings scale too: مننه becomes ډېره مننه، الله دې اجر درکړي; "
        "خدای پامان becomes خدای مو وساته. With elders, default to the "
        "full stack; they will invite you down to the familiar if they "
        "wish - never climb down uninvited."
    ),
    "key_points": [
        "15 formal/informal pairs across letters, business, and elders - the complete politeness system.",
        "Four tools of formality: تاسې endings, مهرباني وکړئ, بښنه غواړم, elevated vocabulary.",
        "Maximum formality stacks all four: مهرباني وکړئ + formal imperative + قدرمن/خدمت/اجازه.",
        "Blessings scale: مننه → ډېره مننه، الله دې اجر درکړي; خدای پامان → خدای مو وساته.",
        "Letters: open قدرمن مشره، سلامونه ومنئ; close احتراماً.",
        "Default to the full stack with elders; let them invite you down to ته.",
        "Never climb down to the familiar uninvited - the cardinal rule.",
    ],
    "requirements": [
        "Perform all 15 pairs aloud, switching registers cleanly.",
        "Write a formal letter using the قدرمن opening and احتراماً close.",
        "Conduct one full conversation with an elder entirely in the formal register.",
        "List the four tools on a card and check each request against them.",
    ],
    "standards": [
        "Register distinctions follow standard Pashto sociolinguistic norms.",
        "Letter conventions follow standard Pashto epistolary practice.",
        "Transliteration matches the scheme fixed in record 2.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats register as the sworn "
        "staircase: the familiar step for the inner circle, the formal "
        "steps rising - تاسې, مهرباني وکړئ, بښنه غواړم, قدرمن - each a "
        "higher seal of honor. Fifteen pairs map the staircase. Climb "
        "deliberately, never descend uninvited, and every elder knows "
        "exactly where you stand."
    ),
    "demo_key": "pairs",
    "demo_data": {"kind": "formal-informal-registers", "pairs": REG_29},
})

# ---------------------------------------------------------------- record 30

COMPLEX_30 = [
    ("کله چې باران وریږي، ماشومان په کور کې لوبې کوي", "kəla če bārān wriǵi, māšumān pə kor ke lobe kawi", "When it rains, the children play in the house.", "Time clause [کله چې باران وریږي] + main clause [ماشومان...کوي]."),
    ("هغه سړی چې پرون راغی، زما ملګری دی", "haɣa saṛay če parun rāɣay, zmā malgaray day", "The man who came yesterday is my friend.", "Relative clause [چې پرون راغی] modifies سړی; main clause [زما ملګری دی]."),
    ("زه هغه کتاب لولم چې تا راکړ", "zə haɣa kitāb lwələm če tā rākṛ", "I am reading the book that you gave me.", "Relative clause [چې تا راکړ] modifies کتاب; verb last in both clauses."),
    ("که زحمت وباسې، بریالي به شې", "ka zahmat wabāse, baryāli bə še", "If you work hard, you will succeed.", "Conditional [که زحمت وباسې] + future result [بریالي به شې]."),
    ("که هغه راغلی وای، موږ به تللي وو", "ka haɣa rāɣalay wāy, muẓ̌ bə tlali wu", "If he had come, we would have gone.", "Counterfactual: past participle + وای in the که-clause, به + past in the result."),
    ("ځکه چې ناروغ وم، ښوونځي ته لاړ نه شوم", "dzəka če nāroɣ wəm, x̌owənǵi ta lāṛ nə šwəm", "Because I was sick, I could not go to school.", "Cause clause [ځکه چې ناروغ وم] + negated result."),
    ("هغه دومره ستړی و چې ویده شو", "haɣa dumra staṛay wu če wida šu", "He was so tired that he fell asleep.", "Result clause: دومره...چې (so...that)."),
    ("مور وویل چې ډوډۍ تیاره ده", "mor wuwel če ḍoḍəi tayāra da", "Mother said that the bread is ready.", "Reported speech: وویل + چې-clause; no tense shift needed."),
    ("زه پوهېږم چې ته رښتیا وایې", "zə poheǵəm če tə rəxtyā wāye", "I know that you are telling the truth.", "چې-clause as the object of پوهېدل."),
    ("هغه کتاب چې په مېز دی، زما دی", "haɣa kitāb če pə mez day, zmā day", "The book that is on the table is mine.", "Relative clause between noun and main verb; verb still last."),
    ("کله چې لمر راخېږي، موږ پاڅو", "kəla če lmar rāxeǵi, muẓ̌ pātso", "When the sun rises, we wake up.", "Habitual time clause + present main clause."),
    ("که څه هم ستړی یم، کار به کوم", "ka tsə ham staṛay yəm, kār bə kawəm", "Although I am tired, I will work.", "Concessive: که څه هم (although) + future resolve."),
    ("هغه ځای چې موږ اوسو، ښکلی دی", "haɣa dzāy če muẓ̌ osu, x̌kulay day", "The place where we live is beautiful.", "چې-clause of place; main adjective predicate."),
    ("څوک چې زحمت وباسي، هغه به وګټي", "tsok če zahmat wabāsi, haɣa bə wagaṭi", "Whoever works hard will win.", "Free relative: څوک چې... as the subject."),
    ("ما هغه ته وویل چې سبا راشي", "mā haɣa ta wuwel če sabā rāši", "I told him to come tomorrow.", "چې + subjunctive (راشي) for indirect commands; note ما ergative in past."),
]

ENTRIES.append({
    "key": "p30_complex",
    "name": "Pashto Compound and Complex Sentences",
    "group": "Advanced",
    "ladder_rank": 30,
    "ladder_tier": "advanced",
    "description": (
        "Fifteen long sentences with subordinate clauses - time, relative, "
        "conditional, causal, result, reported speech, and concessive - "
        "each with transliteration, English translation, and a parse note "
        "showing the clause structure. Time: کله چې باران وریږي، ماشومان "
        "په کور کې لوبې کوي (when it rains, the children play inside). "
        "Relative: هغه سړی چې پرون راغی، زما ملګری دی (the man who came "
        "yesterday is my friend); زه هغه کتاب لولم چې تا راکړ (I am reading "
        "the book you gave me). Conditional: که زحمت وباسې، بریالي به شې "
        "(if you work hard, you will succeed); the counterfactual که هغه "
        "راغلی وای، موږ به تللي وو (if he had come, we would have gone). "
        "Cause: ځکه چې ناروغ وم (because I was sick). Result: دومره...چې "
        "(so...that). Reported speech: مور وویل چې ډوډۍ تیاره ده. "
        "Concessive: که څه هم ستړی یم، کار به کوم (although tired, I will "
        "work). Free relative: څوک چې زحمت وباسي، هغه به وګټي (whoever "
        "works hard will win). Indirect command: ما هغه ته وویل چې سبا "
        "راشي - with the ergative ما on display."
    ),
    "how_it_works": (
        "چې is the great joiner: it opens relative clauses (سړی چې راغی), "
        "چې-clauses of speech and thought (وویل چې..., پوهېږم چې...), and "
        "result clauses (دومره...چې). که opens conditionals: که + present "
        "for real conditions (که زحمت وباسې، بریالي به شې), که + past "
        "participle + وای for counterfactuals (که راغلی وای...). The "
        "subordinate clause comes FIRST, the main clause second, and the "
        "verb stays last in EVERY clause - the SOV covenant compounds, "
        "never breaks. Indirect commands use چې + subjunctive: وویل چې "
        "راشي (told him to come). Reported speech needs no tense shift: "
        "وویل چې ډوډۍ تیاره ده keeps the present. Build long sentences by "
        "joining two record-11-20 sentences with چې/که/ځکه چې/کله چې."
    ),
    "key_points": [
        "15 complex sentences, each parsed: clause boundaries marked in the parse note.",
        "چې is the universal joiner: relatives, speech, thought, result - سړی چې راغی.",
        "که opens real conditionals (که زحمت وباسې، بریالي به شې) and که+وای counterfactuals.",
        "Subordinate clause first, main clause second; verb last in EVERY clause.",
        "ځکه چې (because), کله چې (when), که څه هم (although), دومره...چې (so...that).",
        "Reported speech: no tense shift - وویل چې ډوډۍ تیاره ده.",
        "Indirect commands: چې + subjunctive - وویل چې راشي; ergative ما on display.",
    ],
    "requirements": [
        "Parse all 15 sentences aloud, marking each clause boundary.",
        "Join ten pairs of simple sentences with چې/که/ځکه چې/کله چې.",
        "Write five conditionals and five reported-speech sentences of your own.",
        "Keep the verb last in every clause - check each one.",
    ],
    "standards": [
        "Clause analysis follows the standard grammatical description in the cited references.",
        "Counterfactual forms follow standard Pashto usage.",
        "Transliteration matches the scheme fixed in record 2.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method treats the complex sentence as a "
        "sworn architecture: چې the keystone joining hall to hall, که the "
        "gate of conditions, ځکه چې the foundation of causes, کله چې the "
        "arch of time. Fifteen buildings stand in this record, each with "
        "its plan drawn in the parse note. Study the plans, raise your "
        "own halls, and never let a verb stray from its final post."
    ),
    "demo_key": "sentences",
    "demo_data": {"topic": "Pashto Compound and Complex Sentences",
                  "sentences": [(a, b, c) for a, b, c, _ in COMPLEX_30],
                  "parses": [p for _, _, _, p in COMPLEX_30]},
})

# ---------------------------------------------------------------- records 31-33: dialogues

DIAL_31 = [
    ("احمد", "سلام علیکم", "salām alaykum", "Peace be upon you"),
    ("دوکاندار", "وعلیکم السلام، څه خدمت وکړم؟", "wa alaykum as-salām, tsə xidmat wakṛəm", "And upon you peace; how may I serve you?"),
    ("احمد", "دا مڼې څومره دي؟", "dā maṇe tsumra di", "How much are these apples?"),
    ("دوکاندار", "یو کیلو په پنځوس افغانۍ دی", "yaw kilo pə pandzos afɣānəi day", "One kilo is fifty afghanis."),
    ("احمد", "ډېر ګران دی، ارزان یې کړه", "ḍer grān day, arzān ye kṛa", "That is too expensive; make it cheaper."),
    ("دوکاندار", "وروستۍ بیه څلوېښت ده", "wrustəi beya tsalwext da", "The final price is forty."),
    ("احمد", "مڼې تازه دي؟", "maṇe tāze di", "Are the apples fresh?"),
    ("دوکاندار", "هو، نن سهار راغلي دي", "ho, nən sahār rāɣali di", "Yes, they arrived this morning."),
    ("احمد", "ښه، دوه کیلو راکړه", "x̌a, dwa kilo rākṛa", "Good, give me two kilos."),
    ("دوکاندار", "دا واخله، اتیا افغانۍ کېږي", "dā wāxla, atyā afɣānəi keǵi", "Take these; it comes to eighty afghanis."),
    ("احمد", "انګور هم لرې؟", "angur ham lare", "Do you also have grapes?"),
    ("دوکاندار", "هو، تور انګور دي", "ho, tor angur di", "Yes, there are black grapes."),
    ("احمد", "یو کیلو انګور هم راکړه", "yaw kilo angur ham rākṛa", "Give me one kilo of grapes too."),
    ("دوکاندار", "ټول یو سل شل کېږي", "ṭol yaw səl šəl keǵi", "The total comes to one hundred twenty."),
    ("احمد", "دا پیسې واخله", "dā payse wāxla", "Take this money."),
    ("دوکاندار", "باقي دې دا ده", "bāqi de dā da", "Here is your change."),
    ("احمد", "رسید راکړه", "rasid rākṛa", "Give me the receipt."),
    ("دوکاندار", "دا رسید دې دی", "dā rasid de day", "Here is your receipt."),
    ("احمد", "ډېره مننه، خدای پامان", "ḍera manəna, xudāy pāmān", "Thank you very much, goodbye."),
    ("دوکاندار", "په مخه ښه، بیا راشه", "pə maxa x̌a, byā rāša", "Go well; come again."),
]

DIAL_32 = [
    ("احمد", "سلام، څنګه یې؟", "salām, tsənga ye", "Hi, how are you?"),
    ("کریم", "ښه یم، ته څنګه یې؟", "x̌a yəm, tə tsənga ye", "I am well; how are you?"),
    ("احمد", "زه هم ښه یم، ډېر وخت وشو چې مو سره نه دي لیدلي", "zə ham x̌a yəm, ḍer waxt wašu če mo sara nə di lidali", "I am well too; it has been a long time since we met."),
    ("کریم", "رښتیا هم، له کومه راځې؟", "rəxtyā ham, lə kuma rādze", "Truly; where are you coming from?"),
    ("احمد", "له ښوونځي راغلم", "lə x̌owənǵi rāɣləm", "I came from school."),
    ("کریم", "درسونه څنګه دي؟", "darsuna tsənga di", "How are the lessons?"),
    ("احمد", "ښه دي، پښتو زده کوم", "x̌a di, paʂto zda kawəm", "They are good; I am learning Pashto."),
    ("کریم", "واه، دا خو ډېره ښه ده", "wāh, dā xo ḍera x̌a da", "Wow, that is very good."),
    ("احمد", "ته څه کوې نن سبا؟", "tə tsə kawe nən sabā", "What are you doing these days?"),
    ("کریم", "زه په دفتر کې کار کوم", "zə pə daftar ke kār kawəm", "I work in an office."),
    ("احمد", "کورنۍ دې څنګه ده؟", "koranəi de tsənga da", "How is your family?"),
    ("کریم", "ټول ښه دي، مننه", "ṭol x̌a di, manəna", "All are well, thank you."),
    ("احمد", "راځه چای وڅښو", "rādza čāy wotsṣ̌u", "Come, let us have tea."),
    ("کریم", "په خوښۍ سره", "pə xoṣ̌əi sara", "With pleasure."),
    ("احمد", "سبا زما کره راشه", "sabā zmā kara rāša", "Come to my place tomorrow."),
    ("کریم", "حتماً به راشم", "hatman bə rāšəm", "I will definitely come."),
    ("احمد", "مور به دې هم وویني", "mor bə de ham wawini", "Mother will see you too."),
    ("کریم", "ډېره مننه", "ḍera manəna", "Thank you very much."),
    ("احمد", "بیا به سره ګورو", "byā bə sara guru", "We will meet again."),
    ("کریم", "خدای پامان", "xudāy pāmān", "Goodbye."),
]

DIAL_33 = [
    ("احمد", "ستونزه لرو، د اوبو پمپ خراب شوی دی", "stunza ləru, də obo pamp xarāb šaway day", "We have a problem; the water pump is broken."),
    ("کریم", "کله خراب شو؟", "kəla xarāb šu", "When did it break?"),
    ("احمد", "نن سهار", "nən sahār", "This morning."),
    ("کریم", "مستري ته دې تلیفون کړی دی؟", "mistari ta de telifon kṛay day", "Have you called the mechanic?"),
    ("احمد", "هو، خو هغه په ښار کې دی", "ho, xo haɣa pə x̌ār ke day", "Yes, but he is in the city."),
    ("کریم", "تر هغه پورې څه وکړو؟", "tər haɣa pore tsə wakṛu", "What should we do until then?"),
    ("احمد", "ګاونډي ته لاړ شو او اوبه راوړو", "gāwanḍi ta lāṛ šu aw obə rāwṛu", "Let us go to the neighbor and bring water."),
    ("کریم", "ښه فکر دی، زه سطل راوړم", "x̌a fikr day, zə saṭal rāwṛəm", "Good idea; I will bring the bucket."),
    ("احمد", "زه رسۍ راوړم", "zə rasəi rāwṛəm", "I will bring the rope."),
    ("کریم", "څاه ژور دی، پام کوه", "tsāh žwar day, pām kawa", "The well is deep; be careful."),
    ("احمد", "سمه ده، ورو ورو به یې راوباسو", "sama da, wro wro bə ye rāwbāsu", "All right; we will draw it up slowly."),
    ("کریم", "اوبه راغلې", "obə rāɣle", "The water is coming up."),
    ("احمد", "ډېرې دې نه شي، بس کړه", "ḍere de nə ši, bas kṛa", "Not too much; that is enough."),
    ("کریم", "مستري راغی", "mistari rāɣay", "The mechanic has come."),
    ("احمد", "ژر یې جوړ کړ", "žər ye joṛ kṛ", "He fixed it quickly."),
    ("کریم", "اوس اوبه روانې دي", "os obə rawāne di", "Now the water is running."),
    ("احمد", "ستونزه حل شوه", "stunza hal šwa", "The problem is solved."),
    ("کریم", "له ګاونډي مننه وکړه", "lə gāwanḍi manəna wakṛa", "Thank the neighbor."),
    ("احمد", "هو، ډېره مننه ترې وکړه", "ho, ḍera manəna tre wakṛa", "Yes, thank him very much."),
    ("کریم", "کار وشو، خدای پامان", "kār wašu, xudāy pāmān", "The job is done; goodbye."),
]

DIALOGUES = [
    ("p31_market", "Pashto Conversation: At the Market", DIAL_31,
     "A twenty-line bilingual dialogue at the market: احمد greets the shopkeeper (سلام علیکم / وعلیکم السلام), asks the price of apples (دا مڼې څومره دي؟), bargains (ډېر ګران دی، ارزان یې کړه → وروستۍ بیه څلوېښت ده), checks freshness, buys two kilos, adds a kilo of grapes, pays, takes the change and receipt, thanks, and parts with خدای پامان / په مخه ښه، بیا راشه. Annotated: the bargaining ladder, the politeness of هو with مننه, the farewell pair.",
     "The Signature Pashto Method treats the market as the sworn arena of trade: greeting, price, bargain, freshness, purchase, payment, change, receipt, thanks, farewell - ten gates, twenty lines. Walk the arena and trade speaks Pashto.",
     "dialogue-market"),
    ("p32_friend", "Pashto Conversation: Meeting a Friend", DIAL_32,
     "A twenty-line bilingual dialogue between old friends: the greeting and health exchange (سلام، څنګه یې؟ / ښه یم), the long-time-no-see line (ډېر وخت وشو), where-from and what-doing, the lessons and the office, the family inquiry (کورنۍ دې څنګه ده؟), the tea invitation (راځه چای وڅښو / په خوښۍ سره), the tomorrow invitation (سبا زما کره راشه / حتماً به راشم), and the warm parting (بیا به سره ګورو / خدای پامان). Annotated: familiar register throughout, the invitation-acceptance pair, the family question as courtesy.",
     "The Signature Pashto Method treats friendship as the sworn circle renewed: greeting, health, news, family, tea, invitation, promise, parting. Twenty lines, one circle. Walk it and loyalty speaks Pashto.",
     "dialogue-friend"),
    ("p33_problem", "Pashto Conversation: Solving a Problem", DIAL_33,
     "A twenty-line bilingual dialogue solving a real problem: the water pump broke this morning, the mechanic is in the city, so احمد and کریم plan - fetch water from the neighbor's well meanwhile (ګاونډي ته لاړ شو او اوبه راوړو), bring bucket and rope, draw carefully (څاه ژور دی، پام کوه), the mechanic arrives and fixes it fast, the water runs, the problem is solved (ستونزه حل شوه), the neighbor is thanked, the job done. Annotated: problem-statement, information questions, joint planning with شو/به, caution, resolution, gratitude.",
     "The Signature Pashto Method treats the problem as the sworn test: name it, question it, plan together, act carefully, resolve it, thank the helpers. Twenty lines from ستونزه لرو to کار وشو. Pass the test and trouble itself speaks Pashto.",
     "dialogue-problem"),
]

for _i, (_key, _name, _lines, _desc, _sig, _kind) in enumerate(DIALOGUES):
    ENTRIES.append({
        "key": _key,
        "name": _name,
        "group": "Advanced",
        "ladder_rank": 31 + _i,
        "ladder_tier": "advanced",
        "description": _desc,
        "how_it_works": (
            "Twenty lines of real dialogue, each with speaker, Pashto, "
            "transliteration, and English translation. Read it as a play: "
            "take one role, read aloud, then swap roles. Cover the English "
            "and translate from the Pashto; then cover the Pashto and "
            "produce it from the English. Notice the conversational "
            "formulas - the greeting pairs, the invitation and its "
            "acceptance, the bargaining ladder, the problem-solving "
            "sequence. Memorize three lines that you will actually use "
            "this week. Then improvise the same situation with different "
            "details: different goods at the market, a different problem "
            "to solve."
        ),
        "key_points": [
            "20-line bilingual dialogue with speaker labels - a real situation, not drills.",
            "Read as a play: take a role, read aloud, swap roles.",
            "Two-way translation drill: Pashto→English, then English→Pashto from memory.",
            "Conversational formulas marked in the annotation: greetings, invitations, bargaining, planning.",
            "Memorize three lines you will use this week; improvise the situation with new details.",
        ],
        "requirements": [
            "Perform each dialogue twice, swapping roles.",
            "Translate all 20 lines both directions without the key.",
            "Improvise the same situation with three changed details.",
            "Use one line from each dialogue in real speech this week.",
        ],
        "standards": [
            "Dialogues reflect standard Pashto conversational norms.",
            "Register choices (familiar/formal) match the social situation.",
            "Transliteration matches the scheme fixed in record 2.",
        ],
        "citations": list(CIT_ALL),
        "sig_lens": _sig,
        "demo_key": "dialogue",
        "demo_data": {"title": _name, "lines": _lines},
    })

# ---------------------------------------------------------------- record 34

WORDS_34 = [
    ("زه", "zə", "I"), ("ته", "tə", "you (fam.)"), ("هغه", "haɣa", "he/she"),
    ("موږ", "muẓ̌", "we"), ("تاسې", "tāsə", "you (pl./formal)"), ("هغوی", "haɣwi", "they"),
    ("زما", "zmā", "my"), ("ستا", "stā", "your (fam.)"), ("زموږ", "zmuẓ̌", "our"),
    ("دا", "dā", "this"), ("څوک", "tsok", "who"),
    ("څه", "tsə", "what"), ("چېرته", "čerta", "where"), ("کله", "kəla", "when"),
    ("ولې", "walə", "why"), ("څنګه", "tsənga", "how"), ("څومره", "tsumra", "how much"),
    ("کوم", "kum", "which"), ("نه", "nə", "not"), ("هو", "ho", "yes"),
    ("او", "aw", "and"), ("خو", "xo", "but"), ("که", "ka", "if"),
    ("چې", "če", "that/who"), ("ځکه", "dzəka", "because"), ("تر", "tər", "than/until"),
    ("له", "lə", "from/with"), ("په", "pə", "in/on"),
    ("سره", "sara", "with"),
    ("سړی", "saṛay", "man"), ("ښځه", "x̌əza", "woman"), ("ماشوم", "māšum", "child"),
    ("پلار", "plār", "father"), ("مور", "mor", "mother"), ("ورور", "wror", "brother"),
    ("خور", "xor", "sister"), ("ملګری", "malgaray", "friend"), ("مېلمه", "melma", "guest"),
    ("ګاونډی", "gāwanḍay", "neighbor"), ("ښوونکی", "x̌owunkay", "teacher"), ("زده کوونکی", "zda kawunkay", "student"),
    ("ډاکټر", "ḍākṭar", "doctor"), ("کارګر", "kārgar", "worker"), ("دوکاندار", "dukāndār", "shopkeeper"),
    ("کور", "kor", "house"), ("کوټه", "koṭa", "room"), ("دروازه", "darwāza", "door"),
    ("کړکۍ", "kəṛkəi", "window"), ("مېز", "mez", "table"), ("څوکۍ", "tsawkəi", "chair"),
    ("کټ", "kaṭ", "bed"), ("څراغ", "tsrāɣ", "lamp"), ("کتاب", "kitāb", "book"),
    ("قلم", "qalam", "pen"), ("کاغذ", "kāɣaz", "paper"), ("لیک", "lik", "letter"),
    ("ښوونځی", "x̌owənǵay", "school"), ("کتابتون", "kitābtun", "library"), ("دفتر", "daftar", "office"),
    ("بازار", "bāzār", "market"), ("دوکان", "dukān", "shop"), ("ښار", "x̌ār", "city"),
    ("کلی", "kalay", "village"), ("لار", "lār", "road"),
    ("سیند", "sind", "river"), ("غر", "ɣar", "mountain"),
    ("باغ", "bāɣ", "garden"), ("میدان", "maydān", "field"), ("ځمکه", "dzməka", "earth"),
    ("اسمان", "āsmān", "sky"), ("لمر", "lmar", "sun"), ("سپوږمۍ", "spoǧməi", "moon"),
    ("ستوری", "storay", "star"), ("ورځ", "wrədz", "day"), ("شپه", "špa", "night"),
    ("سهار", "sahār", "morning"), ("ماښام", "māx̌ām", "evening"), ("هوا", "hawā", "weather"),
    ("باران", "bārān", "rain"), ("واوره", "wāwra", "snow"), ("باد", "bād", "wind"),
    ("اوبه", "obə", "water"), ("ډوډۍ", "ḍoḍəi", "bread"), ("وریجې", "wriǵe", "rice"),
    ("غوښه", "ɣwaxa", "meat"), ("شیدې", "šide", "milk"), ("چای", "čāy", "tea"),
    ("مڼه", "maṇa", "apple"), ("انګور", "angur", "grapes"), ("ګل", "gul", "flower"),
    ("ونه", "wəṇa", "tree"), ("سپی", "spay", "dog"), ("پیشو", "pišo", "cat"),
    ("اس", "ās", "horse"), ("اوښ", "ux̌", "camel"), ("پس", "pas", "sheep"),
    ("مارغان", "mārɣān", "birds"), ("پیسې", "payse", "money"),
    ("لوی", "loy", "big"), ("کوچنی", "kučnay", "small"), ("نوی", "naway", "new"),
    ("زوړ", "zoṛ", "old"), ("ښه", "x̌a", "good"), ("بد", "bad", "bad"),
    ("ګرم", "garam", "hot"), ("ساړه", "sāṛa", "cold"), ("اوږد", "uǧd", "long"),
    ("لنډ", "lanḍ", "short"), ("لوړ", "lwaṛ", "high"), ("ژور", "žwar", "deep"),
    ("درون", "drund", "heavy"), ("سپک", "spak", "light"), ("چټک", "čaṭak", "fast"),
    ("ورو", "wro", "slow"), ("پاک", "pāk", "clean"), ("خوشحاله", "xošhāla", "happy"),
    ("خفه", "xafa", "sad"), ("ناروغ", "nāroɣ", "sick"), ("روغ", "roɣ", "healthy"),
    ("ښکلی", "x̌kulay", "beautiful"), ("تلل", "tləl", "to go"), ("راتلل", "rātləl", "to come"),
    ("کول", "kawəl", "to do"), ("ویل", "wayəl", "to say"), ("خوړل", "xoṛəl", "to eat"),
    ("څښل", "tsṣ̌əl", "to drink"), ("لیدل", "lidəl", "to see"), ("اورېدل", "awredəl", "to hear"),
    ("پوهېدل", "pohedəl", "to understand"), ("لوستل", "lwastəl", "to read"), ("لیکل", "likəl", "to write"),
    ("اخیستل", "axistəl", "to take"), ("ورکول", "warkawəl", "to give"), ("جوړول", "joṛawəl", "to make"),
    ("کار کول", "kār kawəl", "to work"), ("زده کول", "zda kawəl", "to learn"), ("خوب کول", "xob kawəl", "to sleep"),
    ("کېناستل", "kenāstəl", "to sit"), ("ګرځېدل", "gərdzedəl", "to walk"), ("پخول", "paxawəl", "to cook"),
    ("مینځل", "mindzəl", "to wash"), ("پرانیستل", "prānistəl", "to open"), ("تړل", "taṛəl", "to close"),
    ("مرسته کول", "mrasta kawəl", "to help"), ("وخت", "waxt", "time"), ("کار", "kār", "work"),
    ("ژوند", "žwand", "life"), ("مینه", "mina", "love"), ("زړه", "zṛa", "heart"),
    ("لاس", "lās", "hand"), ("سترګې", "starge", "eyes"), ("سر", "sar", "head"),
    ("نوم", "num", "name"), ("خبره", "xabara", "word/matter"), ("کیسه", "kisa", "story"),
    ("پوښتنه", "poxtana", "question"), ("ځواب", "dzawāb", "answer"), ("ژبه", "žəba", "language"),
    ("پوهه", "poha", "knowledge"), ("ډېر", "ḍer", "very"), ("لږ", "ləǵ", "little"),
    ("ژر", "žər", "soon"), ("تل", "təl", "always"), ("نن", "nən", "today"),
    ("پرون", "parun", "yesterday"), ("سبا", "sabā", "tomorrow"), ("اوس", "os", "now"),
    ("دلته", "dalta", "here"), ("هلته", "halta", "there"), ("یو", "yaw", "one"),
    ("دوه", "dwa", "two"), ("درې", "dre", "three"), ("لس", "las", "ten"),
    ("شل", "šəl", "twenty"), ("سل", "səl", "hundred"), ("لومړی", "lumṛay", "first"),
    ("سلام", "salām", "hello"), ("مننه", "manəna", "thank you"), ("مهرباني", "mehrabāni", "kindness"),
    ("بښنه", "bax̌əna", "forgiveness"), ("خدای", "xudāy", "God"), ("برکت", "barkat", "blessing"),
    ("صبر", "sabr", "patience"), ("ډالۍ", "ḍāləi", "gift"),
    ("واده", "wāda", "wedding"), ("اختر", "axtar", "Eid"),
    ("روژه", "roža", "fast"), ("جومات", "jomāt", "mosque"), ("دعا", "duā", "prayer"),
    ("هیله", "hila", "hope"), ("ویاړ", "wyāṛ", "pride"),
    ("غوسه", "ɣusa", "anger"), ("وېره", "wera", "fear"),
    ("خوب", "xob", "sleep/dream"), ("فکر", "fikr", "thought"),
    ("تلیفون", "telifon", "telephone"), ("شمېره", "šmera", "number"), ("پیغام", "payɣām", "message"),
    ("انټرنټ", "inṭarneṭ", "internet"), ("کمپیوټر", "kampyuṭar", "computer"),
]

assert len(WORDS_34) == 200, "reference word list must hold exactly 200 words, got %d" % len(WORDS_34)

ENTRIES.append({
    "key": "p34_reference",
    "name": "Pashto Mastery Review and Full Reference",
    "group": "Advanced",
    "ladder_rank": 34,
    "ladder_tier": "advanced",
    "description": (
        "The whole database in one teaching summary: the 44-letter alphabet "
        "with the 12 Pashto-specific letters (ټ ډ ړ ڼ ښ ږ څ ځ ې ۍ ئ ګ); 200 "
        "core words with transliteration and English - pronouns, connectors, "
        "people, home, places, nature, food, animals, adjectives, verbs, "
        "time words, numbers, greetings, and the words of the heart (مینه "
        "love, زړه heart, هیله hope, صبر patience, برکت blessing); the key "
        "grammar in eight lines (SOV word order; two genders with دی/ده; "
        "direct/oblique cases; split ergativity ما/تا in the past; no "
        "articles; نه negation and مه prohibition; به future; چې/که "
        "clause-joining); the phrase tables (30 greetings, ته/تاسې "
        "politeness ladder, مهرباني وکړئ softening); the number system "
        "(1-100, ordinals, days, Solar Hijri months, seasons, clock time); "
        "the tense skeleton (present stem / past stem / به-future); and the "
        "twenty proverbs as the moral seal. Use this record as the daily "
        "drill sheet and the final exam: read a section, cover it, recite "
        "it, uncover, correct."
    ),
    "how_it_works": (
        "Work this record in layers, one per day: day one, the alphabet "
        "(write all 44); day two, the 200 words in ten groups of twenty "
        "(pronouns, connectors, people, home, places, nature, food, "
        "modifiers, verbs, time/heart); day three, the eight grammar lines "
        "(write one original sentence per line); day four, the phrase "
        "tables (perform the greetings and the politeness ladder aloud); "
        "day five, numbers and time (count 1-100, recite days and months); "
        "day six, the tense skeleton (conjugate three verbs through all "
        "tenses); day seven, the proverbs (quote ten from memory with "
        "their occasions). Then cycle again. Anything you cannot recite "
        "from memory sends you back to its record - the ladder is the "
        "curriculum and this record is its map."
    ),
    "key_points": [
        "200 core words with transliteration and English - the working vocabulary of the whole database.",
        "44-letter alphabet with the 12 Pashto-specific letters marked.",
        "Eight-line grammar: SOV, two genders, two cases, split ergativity, no articles, نه/مه, به-future, چې/که.",
        "Phrase tables: 30 greetings, the ته/تاسې ladder, مهرباني وکړئ softening, بښنه غواړم repair.",
        "Numbers 1-100, ordinals, days, Solar Hijri months, seasons, clock time - the measurable world.",
        "Tense skeleton: present stem / past stem / به + present - conjugates every verb.",
        "Seven-day drill cycle: alphabet, words, grammar, phrases, numbers, tenses, proverbs.",
        "Anything unrecitable sends you back to its record - this record is the map, the ladder is the road.",
    ],
    "requirements": [
        "Run the seven-day drill cycle twice before claiming mastery.",
        "Recite the 200 words in groups of twenty without the key.",
        "Write all 44 letters from memory, in order.",
        "Quote ten proverbs with their occasions from memory.",
    ],
    "standards": [
        "This record consolidates records 1-33; all standards there apply here.",
        "Word glosses follow standard Pashto-English lexicography.",
        "The drill cycle is the database's recommended study path.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Pashto Method seals the whole ladder in one "
        "covenant document: 200 sworn words, 44 sworn letters, eight sworn "
        "grammar lines, thirty sworn blessings, twenty sworn proverbs. "
        "This is the charter of the charter, the map of the road. Drill "
        "it in seven days, cycle it until it is bone, and the language is "
        "no longer studied - it is kept."
    ),
    "demo_key": "reference",
    "demo_data": {"letters": 44, "words": WORDS_34,
                  "rules": ["SOV word order - verb last",
                            "Two genders: masculine دی / feminine ده",
                            "Direct/oblique cases; split ergativity in past transitives",
                            "No articles; یو marks indefiniteness",
                            "نه negates, مه prohibits, به marks future",
                            "چې joins relatives/speech; که opens conditionals",
                            "ته familiar / تاسې formal-polite",
                            "Present stem / past stem per verb"]},
})

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
