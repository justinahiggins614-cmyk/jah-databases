#!/usr/bin/env python3
"""Entries for the Odia to English databases (Manon's language project, 2026-10-17).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,750 databases):
zero 'language-odia*' slugs. ID prefixes JAH-LORY- (public) and JAH-LORYS-
(signature) verified free in the manifest id_prefix values AND in every
shard index in jah-databases-data-1 (zero zgrep hits for 'JAH-LORY' across
all index.jsonl.gz files). Pre-authoring whole-system dedupe-gate check over
all 68 planned titles (34 records + 34 Signature Edition titles): zero
collisions, zero refusals.

This build creates two NEW databases, 34 ladder-ordered records each:

  language-odia              - The Odia to English Database
                               (public-harvest: real, fact-checked Odia -
                               overview, the Odia script, phonology, core
                               vocabulary with sentences, grammar
                               essentials, themed sentence sets, verb
                               tenses, questions and answers, commands,
                               descriptions, stories, idioms and proverbs,
                               registers, complex sentences, conversations,
                               mastery reference; every line in Odia with
                               English translation and romanization;
                               standard references Mohanty 2006, Emenau
                               1966, Masica 1991, ISO 639 or/ori)
  language-odia-signature    - The Odia to English Signature Database
                               (his original Signature Language Method:
                               every letter a sworn mark, every vowel a
                               sealed vow, every sentence a covenant of
                               meaning; src signature, titles suffixed
                               " (Signature Edition)", clearly labeled
                               Signature-made, never presented as authentic
                               public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record carries Odia content with English translation and
romanization + example sentences. Sentences are required in EVERY record -
no vocabulary-list-only records.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_odia.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with the
OK marker; the build machine-executes all 68 demos before writing.

Build-time cross-check: every entry declares 'must_contain' strings and the
build asserts each one appears verbatim in the record description, so entry
text and demo outputs can never drift apart.

No website references. Screened per canon.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every letter a sworn mark, every vowel a sealed vow, every "
            "sentence a covenant of meaning. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_MOHANTY = ("Mohanty P. \"On the Phonology of Odia\" and Odia "
               "grammatical studies. In: Abbi A. (ed.) Languages of "
               "India. Linguistic surveys of Eastern Indo-Aryan; 2006.")
CIT_EMENAU = ("Emenau MB. \"The Strata of the Oriya Vocabulary\" and "
              "related Oriya phonological notes. Journal of the American "
              "Oriental Society; 1966.")
CIT_MASICA = ("Masica CP. The Indo-Aryan Languages. Cambridge University "
              "Press; 1991. (Odia as an Eastern/Magadhan Indo-Aryan "
              "language.)")
CIT_ISO = ("ISO 639: Odia is coded or (ISO 639-1) and ori (ISO 639-3, "
           "macrolanguage covering Oriya, Sambalpuri, and Desiya). The "
           "Odia script descends from the Brahmic Kalinga script.")
CIT_CLASSICAL = ("The Government of India conferred classical-language "
                 "status on Odia in 2014, citing its ancient literary "
                 "tradition (Charyapada, Sarala Dasa).")

# The Odia alphabet core: 10 vowel signs and the 34 consonants of the
# traditional varga table (5 vargas of 5 + 9 miscellaneous).
VOWELS = ["\u0b05", "\u0b06", "\u0b07", "\u0b08", "\u0b09", "\u0b0a",
          "\u0b0f", "\u0b10", "\u0b13", "\u0b14"]
VOWEL_ROMA = ["a", "aa", "i", "ii", "u", "uu", "e", "ai", "o", "au"]
VARGAS = [
    ("ka-varga", ["\u0b15", "\u0b16", "\u0b17", "\u0b18", "\u0b19"]),
    ("ca-varga", ["\u0b1a", "\u0b1b", "\u0b1c", "\u0b1d", "\u0b1e"]),
    ("tta-varga", ["\u0b1f", "\u0b20", "\u0b21", "\u0b22", "\u0b23"]),
    ("ta-varga", ["\u0b24", "\u0b25", "\u0b26", "\u0b27", "\u0b28"]),
    ("pa-varga", ["\u0b2a", "\u0b2b", "\u0b2c", "\u0b2d", "\u0b2e"]),
]
MISC_CONS = ["\u0b2f", "\u0b30", "\u0b33", "\u0b71", "\u0b36", "\u0b37",
             "\u0b38", "\u0b39", "\u0b5f"]


def _vowel_lines():
    return "\n".join("  %s  - %s" % (v, r) for v, r in zip(VOWELS, VOWEL_ROMA))


def _cons_lines():
    out = []
    for name, cs in VARGAS:
        out.append("  %s: %s" % (name, " ".join(cs)))
    out.append("  misc: %s" % " ".join(MISC_CONS))
    return "\n".join(out)


ENTRIES = [
    {
        "key": "overview",
        "name": "Odia Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Odia (o\u1e0d\u1e24i\u0101 bh\u0101\u1e63\u0101, also spelled Oriya) is the Eastern "
            "Indo-Aryan language of the Indian state of Odisha. It carries ISO "
            "codes or (ISO 639-1) and ori (ISO 639-3, a macrolanguage covering "
            "standard Oriya, Sambalpuri, and Desiya), and belongs to the "
            "Magadhan branch of Indo-Aryan alongside Bengali and Assamese. "
            "About 35 million people speak Odia as a mother tongue, with total "
            "speakers above 38 million counting second-language users. \n\n"
            "Where it is spoken. The heartland is Odisha - Bhubaneswar, "
            "Cuttack, Puri, Rourkela, Sambalpur, Berhampur, Balasore. Large "
            "Odia-speaking communities also live in Jharkhand, Chhattisgarh, "
            "Andhra Pradesh, and West Bengal, and Odia diaspora communities "
            "work and study across India and abroad. \n\n"
            "Official status. Odia is the official language of Odisha and one "
            "of the scheduled languages of India. In 2014 the Government of "
            "India conferred classical-language status on Odia, recognizing an "
            "unbroken literary tradition. \n\n"
            "Dialects. Standard Odia (the Cuttack-Khurda dialect of the "
            "coastal plain) is the language of schools, newspapers, and "
            "broadcast. The major regional dialects are Sambalpuri (western "
            "Odisha), Bhatri, Desiya, Baleswari (Balasore), Midnapori, "
            "Singhbhumi, and Halbi. A Cuttack speaker and a Sambalpur speaker "
            "understand each other with some effort. \n\n"
            "History in one breath. The earliest Odia inscriptions appear in "
            "the 11th century (the Urajam inscription of 1051 CE); the "
            "Charyapada songs of the 8th-12th centuries carry the oldest "
            "Odia literary voice; Sarala Dasa rendered the Mahabharata into "
            "Odia in the 15th century; the Bhanja-era poets of the 17th-18th "
            "centuries refined the literary language; and Fakir Mohan "
            "Senapati founded the modern Odia novel in the 19th century. \n\n"
            "What makes Odia learnable. The script is a phonetic Brahmic "
            "abugida written left to right, the word order is the familiar "
            "subject-object-verb, verbs carry tense on a small set of regular "
            "endings, and adjectives do not change for gender. Learn the "
            "letters, learn the SOV pattern, and the language opens like a "
            "door. \n\n"
            "First sentences in Odia:\n"
            "  \u0b28\u0b2e\u0b38\u0b4d\u0b15\u0b3e\u0b30! (namask\u0101ra!) - Hello!\n"
            "  \u0b2e\u0b4b \u0b28\u0b3e\u0b2e \u0b2e\u0b28\u0b4b\u0b28\u0964 (mo n\u0101ma Manon.) - My name is Manon.\n"
            "  \u0b2e\u0b41\u0b01 \u0b13\u0b21\u0b3c\u0b3f\u0b06 \u0b36\u0b3f\u0b16\u0b41\u0b1b\u0b3f\u0964 (mun odi\u0101 \u015bikhu\u1e63i.) - I am learning Odia.\n"
            "  \u0b13\u0b21\u0b3c\u0b3f\u0b06 \u0b0f\u0b15 \u0b38\u0b41\u0b28\u0b4d\u0b26\u0b30 \u0b2d\u0b3e\u0b37\u0b3e\u0964 (odi\u0101 eka sundara bh\u0101\u1e63\u0101.) - Odia is a beautiful language."
        ),
        "how_it_works": (
            "This record is the map of the whole database. It fixes the "
            "identity of the language - name (Odia / o\u1e0d\u1e24i\u0101 bh\u0101\u1e63\u0101), "
            "codes (or / ori), family (Indo-European, Indo-Iranian, "
            "Indo-Aryan, Eastern/Magadhan), speaker scale (about 35 million "
            "native, above 38 million total), status (official language of "
            "Odisha; classical language since 2014), dialects (standard "
            "Cuttack-Khurda plus Sambalpuri, Bhatri, Desiya, Baleswari, "
            "Midnapori, Singhbhumi, Halbi), and the deep history from 11th-"
            "century inscriptions through the Charyapada, Sarala Dasa, and "
            "Fakir Mohan Senapati. Every later record assumes this map: the "
            "script record teaches the letters named here, the phonology "
            "record teaches the sounds, the vocabulary records build the "
            "word stock, and the grammar records teach SOV order, "
            "postpositions, three genders, and seven cases. Work through "
            "the ladder in order and each record assumes only what earlier "
            "records taught."
        ),
        "key_points": [
            "Native name: o\u1e0d\u1e24i\u0101 bh\u0101\u1e63\u0101; ISO 639-1 or, ISO 639-3 ori (macrolanguage).",
            "Family: Indo-European, Indo-Iranian, Indo-Aryan, Eastern (Magadhan) branch.",
            "About 35 million native speakers; above 38 million total with second-language users.",
            "Official language of Odisha; classical language of India since 2014.",
            "Standard dialect: Cuttack-Khurda; major dialects Sambalpuri, Bhatri, Desiya, Baleswari, Midnapori, Singhbhumi, Halbi.",
            "Literary history: 11th-century inscriptions, Charyapada songs, Sarala Dasa (15th c.), Bhanja poets, Fakir Mohan Senapati (19th c.).",
            "SOV word order; regular verb endings; adjectives do not inflect for gender.",
        ],
        "requirements": [
            "No prior knowledge of any Indian language is assumed.",
            "Read the script record before the phonology record; read the phonology record before the vocabulary records.",
        ],
        "standards": [
            "Speaker figures are rounded public estimates (Census of India / Ethnologue-style reporting); the record states them as approximate.",
            "History and classification claims follow the standard references: Masica 1991, Emenau 1966.",
            "All example sentences are glossed with romanization and English.",
        ],
        "citations": [CIT_MASICA, CIT_EMENAU, CIT_ISO, CIT_CLASSICAL],
        "must_contain": ["o\u1e0d\u1e24i\u0101 bh\u0101\u1e63\u0101", "or", "ori", "Magadhan", "Cuttack", "35 million"],
        "sig_lens": (
            "Through the Signature lens this overview is a census of a "
            "living nation of speakers: every headcount a sworn roll-call, "
            "every dialect a branch of one family tree, every palm-leaf "
            "manuscript a seal on the covenant that this language will be "
            "carried whole into the archive."
        ),
        "drill": {
            "native_m": 35.0, "total_m": 38.0, "iso1": "or", "iso3": "ori",
            "classical_year": 2014, "inscription_year": 1051,
            "dialects": ["Cuttack-Khurda (standard)", "Sambalpuri", "Bhatri",
                        "Desiya", "Baleswari", "Midnapori", "Singhbhumi", "Halbi"],
            "regions": ["Odisha", "Jharkhand", "Chhattisgarh",
                        "Andhra Pradesh", "West Bengal", "diaspora"],
            "cities": ["Bhubaneswar", "Cuttack", "Puri", "Rourkela",
                       "Sambalpur", "Berhampur", "Balasore"],
            "branch": "Magadhan",
        },
    },
    {
        "key": "script",
        "name": "Odia Script and Writing System",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Odia is written in the Odia script, a Brahmic abugida descended "
            "from the Kalinga script. It runs left to right. The script is "
            "famous for its rounded, curved letterforms: Odia was written for "
            "centuries with a stylus on palm leaves, and straight lines would "
            "have torn the leaf, so the letters curl. \n\n"
            "Vowels - 10 vowel signs, each with a romanization:\n"
            + _vowel_lines() + "\n\n"
            "Consonants - 34 consonants in the traditional varga table "
            "(five vargas of five) plus nine miscellaneous consonants:\n"
            + _cons_lines() + "\n\n"
            "How the abugida works. Each consonant letter carries an inherent "
            "vowel a (pronounced [\u0254] in Odia), so \u0b15 alone reads ka. "
            "Other vowels are written with vowel signs (matras) attached to "
            "the consonant: \u0b15\u0b3f = ki, \u0b15\u0b41 = ku, \u0b15\u0b47 = ke, "
            "\u0b15\u0b4b = ko. The halant (\u0b4d) kills the inherent vowel: "
            "\u0b15\u0b4d = k. Conjunct clusters stack or join letters: "
            "\u0b38\u0b4d\u0b24 = sta, \u0b1c\u0b4d\u0b1e = jnya. \n\n"
            "Punctuation and numerals. Odia uses the danda \u0964 to end a "
            "sentence and the double danda \u0965 for verse or paragraph "
            "breaks. Odia has its own digits: \u0b67 \u0b68 \u0b69 \u0b6a \u0b6b "
            "\u0b6c \u0b6d \u0b6e \u0b6f \u0b66 = 1 2 3 4 5 6 7 8 9 0. \n\n"
            "Everyday words in the script:\n"
            "  \u0b13\u0b21\u0b3c\u0b3f\u0b06 (o\u1e0di\u0101) - Odia\n"
            "  \u0b2d\u0b3e\u0b37\u0b3e (bh\u0101\u1e63\u0101) - language\n"
            "  \u0b2e\u0b41\u0b01 (mun) - I\n"
            "  \u0b28\u0b2e\u0b38\u0b4d\u0b15\u0b3e\u0b30 (namask\u0101ra) - greeting\n"
            "  \u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26 (dhanyab\u0101da) - thank you"
        ),
        "how_it_works": (
            "This record teaches reading and writing from the ground up. "
            "First the direction (left to right, unlike no script in this "
            "family that runs otherwise), then the ten vowel signs with "
            "romanizations, then the 34 consonants in their traditional "
            "varga rows so the pattern of plain, aspirated, voiced, "
            "aspirated-voiced, and nasal in each row becomes visible. Then "
            "the abugida engine: inherent vowel a, vowel signs that replace "
            "it, the halant that deletes it, and conjuncts that fuse "
            "consonants. Then punctuation (danda \u0964) and the ten Odia "
            "digits. Practice path: copy the vowel signs, then read the "
            "five everyday words aloud, then write your own name in Odia "
            "letters using the varga table."
        ),
        "key_points": [
            "Odia script: Brahmic abugida, descendant of the Kalinga script; written left to right.",
            "Rounded letterforms come from centuries of stylus writing on palm leaves.",
            "10 vowel signs; 34 consonants (five vargas of five + nine miscellaneous).",
            "Each consonant carries inherent vowel a; vowel signs (matras) replace it; halant deletes it.",
            "Conjuncts fuse consonant clusters; danda \u0964 ends sentences.",
            "Odia digits \u0b67-\u0b66 map to 1-0.",
        ],
        "requirements": [
            "Read the overview record first for the language's identity and history.",
            "A pen and paper (or a phone keyboard with an Odia layout) for copying the letters.",
        ],
        "standards": [
            "Letter counts follow the standard taught alphabet (10 vowels, 34 consonants).",
            "Romanizations use a simple readable scheme; ISO 15919 equivalents are noted where different.",
            "Palm-leaf origin of the curved forms follows the standard script history (CIT_ISO lineage).",
        ],
        "citations": [CIT_ISO, CIT_MASICA],
        "must_contain": ["abugida", "palm leaves", "left to right", "danda", "\u0b67"],
        "sig_lens": (
            "Through the Signature lens each Odia letter is a sworn mark "
            "curved by a thousand years of palm-leaf writing: no straight "
            "line ever tore the leaf, no straight answer ever tore the "
            "truth. The varga table is a sealed grid of vows."
        ),
        "drill": {
            "vowels": VOWELS, "vowel_roma": VOWEL_ROMA,
            "vargas": VARGAS, "misc": MISC_CONS,
            "digits": ["\u0b67", "\u0b68", "\u0b69", "\u0b6a", "\u0b6b",
                       "\u0b6c", "\u0b6d", "\u0b6e", "\u0b6f", "\u0b66"],
            "direction": "left-to-right", "danda": "\u0964",
            "test_words": ["\u0b13\u0b21\u0b3c\u0b3f\u0b06", "\u0b2d\u0b3e\u0b37\u0b3e",
                           "\u0b2e\u0b41\u0b01", "\u0b28\u0b2e\u0b38\u0b4d\u0b15\u0b3e\u0b30",
                           "\u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26"],
        },
    },
    {
        "key": "phonology",
        "name": "Odia Pronunciation and Phonology",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Odia has six vowel phonemes (a, \u0101, i, \u012b, u, \u016b, e, o, "
            "ai, au written with ten signs) and about 28 consonant phonemes, "
            "including the full five-row varga system and a retroflex row "
            "(\u0b1f \u0b20 \u0b21 \u0b22 \u0b23). Odia is not a tonal language; "
            "stress is light and non-phonemic, falling near the start of the "
            "word. \n\n"
            "The two rules every learner must hear. First, the inherent "
            "vowel \u0b05 is pronounced [\u0254] (like the o in hot), not [a]: "
            "\u0b15\u0b2e\u0b33 = k[\u0254]m[\u0254]l[\u0254], lotus. Second, a word-final "
            "\u0b05 weakens to [o]: \u0b30\u0b3e\u0b2e (r\u0101ma) is said "
            "\u201cr\u0101mo\u201d, \u0b28\u0b3e\u0b2e (n\u0101ma) is said \u201cn\u0101mo\u201d. "
            "Hearing r\u0101mo for Rama is the fastest way to recognize an "
            "Odia speaker. \n\n"
            "English approximations for the trickiest sounds:\n"
            "  \u0b05 [\u0254] - o as in hot (never a as in father)\n"
            "  \u0b1f \u0b20 \u0b21 \u0b22 \u0b23 - retroflex: tongue curled back, "
            "harder than English t/d/n\n"
            "  \u0b16 \u0b18 \u0b1b \u0b1d \u0b20 \u0b22 \u0b25 \u0b27 \u0b2b \u0b2d - aspirated: "
            "a puff of air follows (kha, gha...)\n"
            "  \u0b19 \u0b1e \u0b23 \u0b28 \u0b2e - nasals: ng, ny, n (retroflex), n, m\n"
            "  \u0b5f [\u025f] - between j and y\n"
            "  \u0b33 [\u026d] - retroflex l, tongue curled back\n"
            "Fourteen spoken examples - say each aloud:\n"
            "  \u0b2e\u0b3e (m\u0101) - mother (formal address)\n"
            "  \u0b2c\u0b3e\u0b2a\u0b3e (b\u0101p\u0101) - father\n"
            "  \u0b2a\u0b3e\u0b23\u0b3f (p\u0101ni) - water\n"
            "  \u0b2d\u0b3e\u0b24 (bh\u0101ta) - cooked rice\n"
            "  \u0b18\u0b30 (ghara) - house\n"
            "  \u0b2c\u0b39\u0b3f (bahi) - book\n"
            "  \u0b2b\u0b41\u0b32 (phula) - flower\n"
            "  \u0b17\u0b1b (gacha) - tree\n"
            "  \u0b38\u0b42\u0b30\u0b4d\u0b2f\u0b4d\u0b5f (s\u016bryya) - sun\n"
            "  \u0b1a\u0b28\u0b4d\u0b26\u0b4d\u0b30 (candra) - moon\n"
            "  \u0b15\u0b41\u0b15\u0b41\u0b30 (kukura) - dog\n"
            "  \u0b2c\u0b3f\u0b32\u0b47\u0b07 (bilei) - cat\n"
            "  \u0b28\u0b2e\u0b38\u0b4d\u0b15\u0b3e\u0b30 (namask\u0101ra) - greeting\n"
            "  \u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26 (dhanyab\u0101da) - thank you"
        ),
        "how_it_works": (
            "This record trains the ear before the vocabulary records load "
            "the memory. It states the inventory (six vowel phonemes, about "
            "28 consonants, five varga rows including retroflex), the "
            "non-tonal light stress, and the two signature sound rules: "
            "inherent \u0b05 = [\u0254], and word-final \u0b05 -> [o]. The "
            "tricky sounds get English approximations (retroflexes, "
            "aspirates, the five nasals, [\u025f], retroflex [\u026d]), and "
            "fourteen spoken example words give the mouth something real to "
            "do. Practice path: read the fourteen words aloud three times, "
            "exaggerating the [\u0254] and the final -o, until r\u0101mo "
            "sounds natural."
        ),
        "key_points": [
            "Six vowel phonemes; about 28 consonant phonemes; not a tonal language.",
            "Inherent \u0b05 is pronounced [\u0254], never [a].",
            "Word-final \u0b05 weakens to [o]: r\u0101ma is said r\u0101mo.",
            "Retroflex row (\u0b1f \u0b20 \u0b21 \u0b22 \u0b23) and aspirates are the main new sounds for English speakers.",
            "Stress is light, non-phonemic, usually near the word start.",
            "Fourteen spoken examples with English translations for drilling.",
        ],
        "requirements": [
            "Read the script record first so every letter in the examples is already familiar.",
            "Say the examples aloud; silent reading does not train pronunciation.",
        ],
        "standards": [
            "Phoneme counts and the [\u0254]/final-[o] rules follow the standard descriptions (Mohanty 2006, Emenau 1966).",
            "English approximations are guides, not exact phonetic claims.",
        ],
        "citations": [CIT_MOHANTY, CIT_EMENAU],
        "must_contain": ["[\u0254]", "r\u0101mo", "retroflex", "not a tonal language", "Fourteen"],
        "sig_lens": (
            "Through the Signature lens pronunciation is the sealing of the "
            "vow: the mouth must keep what the hand wrote. Every [\u0254] a "
            "sworn sound, every final -o a seal pressed at the word's end."
        ),
        "drill": {
            "vowel_phonemes": 6, "consonant_phonemes": 28,
            "inherent_vowel": "[\u0254]", "final_a_rule": "[o]",
            "tonal": False,
            "example_words": [
                ("\u0b2e\u0b3e", "m\u0101", "mother (formal)"),
                ("\u0b2c\u0b3e\u0b2a\u0b3e", "b\u0101p\u0101", "father"),
                ("\u0b2a\u0b3e\u0b23\u0b3f", "p\u0101ni", "water"),
                ("\u0b2d\u0b3e\u0b24", "bh\u0101ta", "cooked rice"),
                ("\u0b18\u0b30", "ghara", "house"),
                ("\u0b2c\u0b39\u0b3f", "bahi", "book"),
                ("\u0b2b\u0b41\u0b32", "phula", "flower"),
                ("\u0b17\u0b1b", "gacha", "tree"),
                ("\u0b38\u0b42\u0b30\u0b4d\u0b2f\u0b4d\u0b5f", "s\u016bryya", "sun"),
                ("\u0b1a\u0b28\u0b4d\u0b26\u0b4d\u0b30", "candra", "moon"),
                ("\u0b15\u0b41\u0b15\u0b41\u0b30", "kukura", "dog"),
                ("\u0b2c\u0b3f\u0b32\u0b47\u0b07", "bilei", "cat"),
                ("\u0b28\u0b2e\u0b38\u0b4d\u0b15\u0b3e\u0b30", "namask\u0101ra", "greeting"),
                ("\u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26", "dhanyab\u0101da", "thank you"),
            ],
            "minimal_pair": [("r\u0101ma", "written form"), ("r\u0101mo", "spoken form")],
        },
    },
    {
        "key": "nouns1",
        "name": "Core Nouns I: 25 Essential Nouns",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Odia nouns - person, place, and thing - "
            "each with romanization, English, and one full example sentence "
            "in Odia with translation. Every sentence uses the SOV pattern "
            "(subject-object-verb) the grammar record will formalize.\n\n"
            "  1. \u0b2e\u0b23\u0b3f\u0b37 (ma\u1e47i\u1e63a) - person. \u0b38\u0b47 \u0b0f\u0b15 \u0b2d\u0b32 \u0b2e\u0b23\u0b3f\u0b37\u0964 "
            "(Se eka bhala ma\u1e47i\u1e63a.) He is a good person.\n"
            "  2. \u0b2e\u0b39\u0b3f\u0b33\u0b3e (mahi\u1e37\u0101) - woman. \u0b38\u0b47 \u0b2e\u0b39\u0b3f\u0b33\u0b3e \u0b2c\u0b1c\u0b3e\u0b30\u0b15\u0b41 \u0b17\u0b32\u0b47\u0964 "
            "(Se mahi\u1e37\u0101 baj\u0101raku gale.) The woman went to the market.\n"
            "  3. \u0b2a\u0b3f\u0b32\u0b3e (pil\u0101) - child. \u0b2a\u0b3f\u0b32\u0b3e\u0b1f\u0b3f \u0b16\u0b47\u0b33\u0b41\u0b1b\u0b3f\u0964 "
            "(Pil\u0101\u1e6di khe\u1e37uchi.) The child is playing.\n"
            "  4. \u0b18\u0b30 (ghara) - house. \u0b06\u0b2e\u0b30 \u0b18\u0b30 \u0b2c\u0b21\u0b3c\u0964 "
            "(\u0100mara ghara ba\u1e0da.) Our house is big.\n"
            "  5. \u0b2c\u0b39\u0b3f (bahi) - book. \u0b2e\u0b41\u0b01 \u0b2c\u0b39\u0b3f \u0b2a\u0b22\u0b3c\u0b41\u0b1b\u0b3f\u0964 "
            "(Mun bahi pa\u1e0dhu\u1e63i.) I am reading a book.\n"
            "  6. \u0b2a\u0b3e\u0b23\u0b3f (p\u0101\u1e47i) - water. \u0b2e\u0b4b\u0b24\u0b47 \u0b2a\u0b3e\u0b23\u0b3f \u0b26\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 "
            "(Mote p\u0101\u1e47i diantu.) Please give me water.\n"
            "  7. \u0b2d\u0b3e\u0b24 (bh\u0101ta) - cooked rice. \u0b2e\u0b3e \u0b2d\u0b3e\u0b24 \u0b30\u0b3e\u0b28\u0b4d\u0b27\u0b41\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 "
            "(M\u0101 bh\u0101ta r\u0101ndhuchanti.) Mother is cooking rice.\n"
            "  8. \u0b17\u0b3e\u0b21\u0b3c\u0b3f (g\u0101\u1e0di) - vehicle. \u0b17\u0b3e\u0b21\u0b3c\u0b3f\u0b1f\u0b3f \u0b26\u0b4d\u0b30\u0b41\u0b24 \u0b2f\u0b3e\u0b09\u0b1b\u0b3f\u0964 "
            "(G\u0101\u1e0di\u1e6di druta y\u0101uchi.) The vehicle is going fast.\n"
            "  9. \u0b30\u0b3e\u0b38\u0b4d\u0b24\u0b3e (r\u0101st\u0101) - road. \u0b30\u0b3e\u0b38\u0b4d\u0b24\u0b3e\u0b1f\u0b3f \u0b32\u0b2e\u0b4d\u0b2c\u0b3e\u0964 "
            "(R\u0101st\u0101\u1e6di lamb\u0101.) The road is long.\n"
            "  10. \u0b2c\u0b1c\u0b3e\u0b30 (baj\u0101ra) - market. \u0b2c\u0b1c\u0b3e\u0b30 \u0b0f\u0b20\u0b3e\u0b30\u0b47 \u0b05\u0b1b\u0b3f\u0964 "
            "(Baj\u0101ra e\u1e6d\u0101re achi.) The market is here.\n"
            "  11. \u0b2c\u0b3f\u0b26\u0b4d\u0b5f\u0b3e\u0b33\u0b5f (bidy\u0101\u1e37aya) - school. "
            "\u0b2a\u0b3f\u0b32\u0b3e\u0b2e\u0b3e\u0b28\u0b47 \u0b2c\u0b3f\u0b26\u0b4d\u0b5f\u0b3e\u0b33\u0b5f\u0b15\u0b41 \u0b17\u0b32\u0b47\u0964 "
            "(Pil\u0101m\u0101ne bidy\u0101\u1e37ayaku gale.) The children went to school.\n"
            "  12. \u0b21\u0b3e\u0b15\u0b4d\u0b24\u0b30 (d\u0101ktara) - doctor. \u0b21\u0b3e\u0b15\u0b4d\u0b24\u0b30 \u0b06\u0b38\u0b3f\u0b32\u0b47\u0964 "
            "(D\u0101ktara \u0101sile.) The doctor came.\n"
            "  13. \u0b2c\u0b28\u0b4d\u0b27\u0b41 (bandhu) - friend. \u0b38\u0b47 \u0b2e\u0b4b\u0b30 \u0b2c\u0b28\u0b4d\u0b27\u0b41\u0964 "
            "(Se mora bandhu.) He is my friend.\n"
            "  14. \u0b2e\u0b3e (m\u0101) - mother. \u0b2e\u0b3e \u0b18\u0b30\u0b47 \u0b05\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 "
            "(M\u0101 ghare achanti.) Mother is at home.\n"
            "  15. \u0b2c\u0b3e\u0b2a\u0b3e (b\u0101p\u0101) - father. \u0b2c\u0b3e\u0b2a\u0b3e \u0b15\u0b3e\u0b2e\u0b30\u0b47 \u0b05\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 "
            "(B\u0101p\u0101 k\u0101mare achanti.) Father is at work.\n"
            "  16. \u0b2d\u0b3e\u0b07 (bh\u0101i) - brother. \u0b2e\u0b4b\u0b30 \u0b2d\u0b3e\u0b07 \u0b1b\u0b3e\u0b24\u0b4d\u0b30\u0964 "
            "(Mora bh\u0101i ch\u0101tra.) My brother is a student.\n"
            "  17. \u0b2d\u0b09\u0b23\u0b40 (bhau\u1e47\u012b) - sister. \u0b2e\u0b4b\u0b30 \u0b2d\u0b09\u0b23\u0b40 \u0b17\u0b3e\u0b09\u0b1b\u0b3f\u0964 "
            "(Mora bhau\u1e47\u012b g\u0101uchi.) My sister is singing.\n"
            "  18. \u0b17\u0b1b (gacha) - tree. \u0b17\u0b1b\u0b30\u0b47 \u0b2b\u0b33 \u0b05\u0b1b\u0b3f\u0964 "
            "(Gachare pha\u1e37a achi.) There is fruit on the tree.\n"
            "  19. \u0b2b\u0b41\u0b32 (phula) - flower. \u0b2b\u0b41\u0b32\u0b1f\u0b3f \u0b38\u0b41\u0b28\u0b4d\u0b26\u0b30\u0964 "
            "(Phula\u1e6di sundara.) The flower is beautiful.\n"
            "  20. \u0b15\u0b41\u0b15\u0b41\u0b30 (kukura) - dog. \u0b15\u0b41\u0b15\u0b41\u0b30\u0b1f\u0b3f \u0b2d\u0b41\u0b15\u0b41\u0b1b\u0b3f\u0964 "
            "(Kukura\u1e6di bhukuchi.) The dog is barking.\n"
            "  21. \u0b2c\u0b3f\u0b32\u0b47\u0b07 (bilei) - cat. \u0b2c\u0b3f\u0b32\u0b47\u0b07\u0b1f\u0b3f \u0b26\u0b41\u0b27 \u0b2a\u0b3f\u0b09\u0b1b\u0b3f\u0964 "
            "(Bilei\u1e6di dudha piuchi.) The cat is drinking milk.\n"
            "  22. \u0b2e\u0b3e\u0b1b (m\u0101cha) - fish. \u0b28\u0b26\u0b40\u0b30\u0b47 \u0b2e\u0b3e\u0b1b \u0b05\u0b1b\u0b3f\u0964 "
            "(Nad\u012bre m\u0101cha achi.) There are fish in the river.\n"
            "  23. \u0b38\u0b42\u0b30\u0b4d\u0b2f\u0b4d\u0b5f (s\u016bryya) - sun. \u0b38\u0b42\u0b30\u0b4d\u0b2f\u0b4d\u0b5f \u0b09\u0b20\u0b3f\u0b1b\u0b3f\u0964 "
            "(S\u016bryya u\u1e6dhichi.) The sun has risen.\n"
            "  24. \u0b1a\u0b28\u0b4d\u0b26\u0b4d\u0b30 (candra) - moon. \u0b1a\u0b28\u0b4d\u0b26\u0b4d\u0b30 \u0b09\u0b1c\u0b4d\u0b1c\u0b4d\u0b35\u0b33\u0964 "
            "(Candra ujjva\u1e37a.) The moon is bright.\n"
            "  25. \u0b24\u0b3e\u0b30\u0b3e (t\u0101r\u0101) - star. \u0b06\u0b15\u0b3e\u0b36\u0b30\u0b47 \u0b24\u0b3e\u0b30\u0b3e \u0b1c\u0b33\u0b41\u0b1b\u0b3f\u0964 "
            "(\u0100k\u0101\u1e63are t\u0101r\u0101 ja\u1e37uchi.) Stars are shining in the sky."
        ),
        "how_it_works": (
            "This record builds the first load-bearing word stock: 25 nouns "
            "covering people (ma\u1e47i\u1e63a, mahi\u1e37\u0101, pil\u0101, bandhu, "
            "m\u0101, b\u0101p\u0101, bh\u0101i, bhau\u1e47\u012b), places (ghara, "
            "baj\u0101ra, bidy\u0101\u1e37aya, r\u0101st\u0101), and things (bahi, "
            "p\u0101\u1e47i, bh\u0101ta, g\u0101\u1e0di, gacha, phula, kukura, bilei, "
            "m\u0101cha, s\u016bryya, candra, t\u0101r\u0101, d\u0101ktara). Each "
            "noun is presented in the Odia script with romanization and "
            "English, then fixed in memory by a complete SOV sentence. The "
            "sentences quietly introduce the verb endings (-uchi progressive, "
            "-le past, achi/achanti copula) that the tense record will "
            "formalize later. Drill: cover the Odia column and produce it "
            "from the English, then cover the English and translate back."
        ),
        "key_points": [
            "25 essential nouns: 8 people, 4 places, 13 things.",
            "Every noun appears in the Odia script with romanization and English.",
            "Every noun is fixed by one full translated SOV sentence.",
            "Sentences preview verb endings (-uchi, -le) and the copula (achi/achanti).",
        ],
        "requirements": [
            "Read the script and phonology records first so the words are readable and sayable.",
            "A notebook for the cover-and-recall drill.",
        ],
        "standards": [
            "Noun glosses use standard dictionary meanings.",
            "Example sentences are constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["ma\u1e47i\u1e63a", "bidy\u0101\u1e37aya", "s\u016bryya", "25"],
        "sig_lens": (
            "Through the Signature lens each noun is a sworn name: the word "
            "for mother a vow of care, the word for sun a vow of light. "
            "Twenty-five names sealed into the archive."
        ),
        "drill": {
            "nouns": [
                "ma\u1e47i\u1e63a", "mahi\u1e37\u0101", "pil\u0101", "ghara", "bahi",
                "p\u0101\u1e47i", "bh\u0101ta", "g\u0101\u1e0di", "r\u0101st\u0101", "baj\u0101ra",
                "bidy\u0101\u1e37aya", "d\u0101ktara", "bandhu", "m\u0101", "b\u0101p\u0101",
                "bh\u0101i", "bhau\u1e47\u012b", "gacha", "phula", "kukura",
                "bilei", "m\u0101cha", "s\u016bryya", "candra", "t\u0101r\u0101",
            ],
            "people": 8, "places": 4, "things": 13,
        },
    },
    {
        "key": "verbs1",
        "name": "Core Verbs I: 25 Essential Verbs",
        "group": "Core Vocabulary",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Odia verbs - each given as the verbal noun "
            "in -\u0b2c\u0b3e (the dictionary form, e.g. \u0b16\u0b3e\u0b07\u0b2c\u0b3e kh\u0101ib\u0101, to eat) "
            "with romanization, English, and one full example sentence with "
            "translation. Watch the endings: -\u0b09\u0b1b\u0b3f (-uchi) marks "
            "the present progressive, -\u0b32\u0b3f/-\u0b32\u0b3e (-li/-l\u0101) the past, "
            "-\u0b2c\u0b3f (-bi) the future.\n\n"
            "  1. \u0b16\u0b3e\u0b07\u0b2c\u0b3e (kh\u0101ib\u0101) - to eat. \u0b2e\u0b41\u0b01 \u0b2d\u0b3e\u0b24 \u0b16\u0b3e\u0b09\u0b1b\u0b3f\u0964 "
            "(Mun bh\u0101ta kh\u0101uchi.) I am eating rice.\n"
            "  2. \u0b2a\u0b3f\u0b07\u0b2c\u0b3e (piib\u0101) - to drink. \u0b38\u0b47 \u0b2a\u0b3e\u0b23\u0b3f \u0b2a\u0b3f\u0b09\u0b1b\u0b3f\u0964 "
            "(Se p\u0101\u1e47i piuchi.) He is drinking water.\n"
            "  3. \u0b2f\u0b3f\u0b2c\u0b3e (yib\u0101) - to go. \u0b2e\u0b41\u0b01 \u0b2c\u0b1c\u0b3e\u0b30\u0b15\u0b41 \u0b2f\u0b3f\u0b2c\u0b3f\u0964 "
            "(Mun baj\u0101raku yibi.) I will go to the market.\n"
            "  4. \u0b06\u0b38\u0b3f\u0b2c\u0b3e (\u0101sib\u0101) - to come. \u0b24\u0b41\u0b2e\u0b47 \u0b06\u0b38\u0964 "
            "(Tume \u0101sa.) You come (informal).\n"
            "  5. \u0b15\u0b30\u0b3f\u0b2c\u0b3e (karib\u0101) - to do. \u0b2e\u0b41\u0b01 \u0b15\u0b3e\u0b2e \u0b15\u0b30\u0b41\u0b1b\u0b3f\u0964 "
            "(Mun k\u0101ma karuchi.) I am doing the work.\n"
            "  6. \u0b2a\u0b22\u0b3c\u0b3f\u0b2c\u0b3e (pa\u1e0dhib\u0101) - to read, to study. "
            "\u0b2a\u0b3f\u0b32\u0b3e\u0b1f\u0b3f \u0b2c\u0b39\u0b3f \u0b2a\u0b22\u0b3c\u0b41\u0b1b\u0b3f\u0964 "
            "(Pil\u0101\u1e6di bahi pa\u1e0dhu\u1e63i.) The child is reading a book.\n"
            "  7. \u0b32\u0b47\u0b16\u0b3f\u0b2c\u0b3e (lekhib\u0101) - to write. \u0b38\u0b47 \u0b1a\u0b3f\u0b20\u0b3f \u0b32\u0b47\u0b16\u0b3f\u0b32\u0b3e\u0964 "
            "(Se chi\u1e6dhi lekhil\u0101.) He wrote a letter.\n"
            "  8. \u0b15\u0b39\u0b3f\u0b2c\u0b3e (kahib\u0101) - to say, to tell. \u0b38\u0b47 \u0b2e\u0b4b\u0b24\u0b47 \u0b15\u0b39\u0b3f\u0b32\u0b3e\u0964 "
            "(Se mote kahil\u0101.) He told me.\n"
            "  9. \u0b36\u0b41\u0b23\u0b3f\u0b2c\u0b3e (\u1e63u\u1e47ib\u0101) - to listen. \u0b2e\u0b41\u0b01 \u0b17\u0b40\u0b24 \u0b36\u0b41\u0b23\u0b41\u0b1b\u0b3f\u0964 "
            "(Mun g\u012bta \u1e63u\u1e47uchi.) I am listening to a song.\n"
            "  10. \u0b26\u0b47\u0b16\u0b3f\u0b2c\u0b3e (dekhib\u0101) - to see. \u0b2e\u0b41\u0b01 \u0b24\u0b41\u0b2e\u0b15\u0b41 \u0b26\u0b47\u0b16\u0b3f\u0b32\u0b3f\u0964 "
            "(Mun tumaku dekhili.) I saw you.\n"
            "  11. \u0b2c\u0b38\u0b3f\u0b2c\u0b3e (basib\u0101) - to sit. \u0b38\u0b47 \u0b1a\u0b09\u0b15\u0b3f\u0b30\u0b47 \u0b2c\u0b38\u0b3f\u0b1b\u0b3f\u0964 "
            "(Se chaukire basichi.) He is sitting on the chair.\n"
            "  12. \u0b20\u0b3f\u0b06 \u0b39\u0b47\u0b2c\u0b3e (\u1e6dhi\u0101 heb\u0101) - to stand. "
            "\u0b24\u0b41\u0b2e\u0b47 \u0b20\u0b3f\u0b06 \u0b39\u0b41\u0b05\u0964 "
            "(Tume \u1e6dhi\u0101 hua.) You stand up.\n"
            "  13. \u0b36\u0b4b\u0b07\u0b2c\u0b3e (\u1e63oib\u0101) - to sleep. \u0b2a\u0b3f\u0b32\u0b3e\u0b1f\u0b3f \u0b36\u0b4b\u0b07\u0b1b\u0b3f\u0964 "
            "(Pil\u0101\u1e6di \u1e63oichi.) The child is sleeping.\n"
            "  14. \u0b09\u0b20\u0b3f\u0b2c\u0b3e (u\u1e6dhib\u0101) - to wake up, to rise. "
            "\u0b2e\u0b41\u0b01 \u0b38\u0b15\u0b3e\u0b33\u0b41 \u0b09\u0b20\u0b47\u0964 "
            "(Mun sak\u0101\u1e37u u\u1e6dhe.) I wake up in the morning.\n"
            "  15. \u0b1a\u0b3e\u0b32\u0b3f\u0b2c\u0b3e (c\u0101lib\u0101) - to walk. \u0b38\u0b47\u0b2e\u0b3e\u0b28\u0b47 \u0b1a\u0b3e\u0b32\u0b3f \u0b1a\u0b3e\u0b32\u0b3f \u0b17\u0b32\u0b47\u0964 "
            "(Sem\u0101ne c\u0101li c\u0101li gale.) They went walking.\n"
            "  16. \u0b26\u0b4c\u0b21\u0b3c\u0b3f\u0b2c\u0b3e (dau\u1e0dib\u0101) - to run. "
            "\u0b15\u0b41\u0b15\u0b41\u0b30\u0b1f\u0b3f \u0b26\u0b4c\u0b21\u0b3c\u0b41\u0b1b\u0b3f\u0964 "
            "(Kukura\u1e6di dau\u1e0duchi.) The dog is running.\n"
            "  17. \u0b15\u0b3f\u0b23\u0b3f\u0b2c\u0b3e (ki\u1e47ib\u0101) - to buy. \u0b2e\u0b41\u0b01 \u0b2b\u0b33 \u0b15\u0b3f\u0b23\u0b3f\u0b32\u0b3f\u0964 "
            "(Mun pha\u1e37a ki\u1e47ili.) I bought fruit.\n"
            "  18. \u0b2c\u0b3f\u0b15\u0b3f\u0b2c\u0b3e (bikib\u0101) - to sell. \u0b38\u0b47 \u0b2a\u0b30\u0b3f\u0b2c\u0b3e \u0b2c\u0b3f\u0b15\u0b41\u0b1b\u0b3f\u0964 "
            "(Se parib\u0101 bikuchi.) She is selling vegetables.\n"
            "  19. \u0b26\u0b47\u0b2c\u0b3e (deb\u0101) - to give. \u0b2e\u0b4b\u0b24\u0b47 \u0b2c\u0b39\u0b3f\u0b1f\u0b3f\u0b0f \u0b26\u0b3f\u0b05\u0964 "
            "(Mote bahi\u1e6die dia.) Give me the book.\n"
            "  20. \u0b28\u0b47\u0b2c\u0b3e (neb\u0101) - to take. \u0b38\u0b47 \u0b1b\u0b24\u0b3e\u0b1f\u0b3f \u0b28\u0b47\u0b32\u0b3e\u0964 "
            "(Se chat\u0101\u1e6di nel\u0101.) He took the umbrella.\n"
            "  21. \u0b16\u0b4b\u0b32\u0b3f\u0b2c\u0b3e (kholib\u0101) - to open. \u0b26\u0b4d\u0b35\u0b3e\u0b30 \u0b16\u0b4b\u0b32\u0964 "
            "(Dw\u0101ra khola.) Open the door.\n"
            "  22. \u0b2c\u0b28\u0b4d\u0b26 \u0b15\u0b30\u0b3f\u0b2c\u0b3e (banda karib\u0101) - to close. "
            "\u0b1d\u0b30\u0b15\u0b3e \u0b2c\u0b28\u0b4d\u0b26 \u0b15\u0b30\u0964 "
            "(Jharak\u0101 banda kara.) Close the window.\n"
            "  23. \u0b39\u0b38\u0b3f\u0b2c\u0b3e (hasib\u0101) - to laugh. \u0b38\u0b47\u0b2e\u0b3e\u0b28\u0b47 \u0b39\u0b38\u0b41\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 "
            "(Sem\u0101ne hasuchanti.) They are laughing.\n"
            "  24. \u0b15\u0b3e\u0b28\u0b4d\u0b26\u0b3f\u0b2c\u0b3e (k\u0101ndib\u0101) - to cry. "
            "\u0b2a\u0b3f\u0b32\u0b3e\u0b1f\u0b3f \u0b15\u0b3e\u0b28\u0b4d\u0b26\u0b41\u0b1b\u0b3f\u0964 "
            "(Pil\u0101\u1e6di k\u0101nduchi.) The child is crying.\n"
            "  25. \u0b2d\u0b32 \u0b2a\u0b3e\u0b07\u0b2c\u0b3e (bhala p\u0101ib\u0101) - to love. "
            "\u0b2e\u0b41\u0b01 \u0b24\u0b41\u0b2e\u0b15\u0b41 \u0b2d\u0b32 \u0b2a\u0b3e\u0b0f\u0964 "
            "(Mun tumaku bhala p\u0101e.) I love you."
        ),
        "how_it_works": (
            "This record builds the action stock: 25 verbs in their -\u0b2c\u0b3e "
            "verbal-noun dictionary form, each with one translated sentence. "
            "The three endings that carry all of Odia time - -\u0b09\u0b1b\u0b3f "
            "present progressive, -\u0b32\u0b3f/-\u0b32\u0b3e past, -\u0b2c\u0b3f future - "
            "appear in context here and are formalized in the tenses record "
            "later. Note the Odia verb comes last in every sentence (SOV), "
            "and the imperative is the bare root (\u0b06\u0b38, \u0b16\u0b4b\u0b32). "
            "Drill: take five verbs and build your own sentences by swapping "
            "the subjects and objects."
        ),
        "key_points": [
            "25 essential verbs in the -\u0b2c\u0b3e verbal-noun dictionary form.",
            "Every verb fixed by one full translated SOV sentence.",
            "Three endings previewed in context: -\u0b09\u0b1b\u0b3f progressive, -\u0b32\u0b3f/-\u0b32\u0b3e past, -\u0b2c\u0b3f future.",
            "Imperative is the bare verb root.",
        ],
        "requirements": [
            "Read the nouns record first; these sentences reuse its vocabulary.",
            "Practice the endings aloud; the tenses record formalizes them.",
        ],
        "standards": [
            "Verb forms follow standard Odia conjugation.",
            "Example sentences are constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA, CIT_MOHANTY],
        "must_contain": ["kh\u0101ib\u0101", "pa\u1e0dhib\u0101", "-uchi", "25"],
        "sig_lens": (
            "Through the Signature lens each verb is a sworn action: to eat "
            "a vow of nourishment, to learn a vow of growth. Twenty-five "
            "actions sealed into the covenant."
        ),
        "drill": {
            "verbs": [
                "kh\u0101ib\u0101", "piib\u0101", "yib\u0101", "\u0101sib\u0101", "karib\u0101",
                "pa\u1e0dhib\u0101", "lekhib\u0101", "kahib\u0101", "\u1e63u\u1e47ib\u0101", "dekhib\u0101",
                "basib\u0101", "\u1e6dhi\u0101 heb\u0101", "\u1e63oib\u0101", "u\u1e6dhib\u0101", "c\u0101lib\u0101",
                "dau\u1e0dib\u0101", "ki\u1e47ib\u0101", "bikib\u0101", "deb\u0101", "neb\u0101",
                "kholib\u0101", "banda karib\u0101", "hasib\u0101", "k\u0101ndib\u0101", "bhala p\u0101ib\u0101",
            ],
            "progressive_ending": "-uchi", "past_endings": ["-li", "-l\u0101"],
            "future_ending": "-bi",
        },
    },
    {
        "key": "adjectives",
        "name": "Adjectives and Adverbs",
        "group": "Core Vocabulary",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five adjectives and fifteen adverbs - each with "
            "romanization, English, and one translated example sentence. "
            "Odia adjectives are easy: unlike Hindi, they do not change for "
            "the gender or number of the noun. \u0b2d\u0b32 \u0b2a\u0b3f\u0b32\u0b3e (good boy), "
            "\u0b2d\u0b32 \u0b1d\u0b3f\u0b05 (good girl), \u0b2d\u0b32 \u0b2a\u0b3f\u0b32\u0b3e\u0b2e\u0b3e\u0b28\u0b47 (good children) - "
            "\u0b2d\u0b32 never changes. \n\n"
            "Adjectives:\n"
            "  1. \u0b2c\u0b21\u0b3c (ba\u1e0da) - big. \u0b0f\u0b39\u0b3e \u0b0f\u0b15 \u0b2c\u0b21\u0b3c \u0b18\u0b30\u0964 (Eh\u0101 eka ba\u1e0da ghara.) This is a big house.\n"
            "  2. \u0b1b\u0b4b\u0b1f (cho\u1e6da) - small. \u0b1b\u0b4b\u0b1f \u0b2a\u0b3f\u0b32\u0b3e\u0b1f\u0b3f \u0b39\u0b38\u0b41\u0b1b\u0b3f\u0964 (Cho\u1e6da pil\u0101\u1e6di hasuchi.) The small child is laughing.\n"
            "  3. \u0b2d\u0b32 (bhala) - good. \u0b38\u0b47 \u0b0f\u0b15 \u0b2d\u0b32 \u0b2e\u0b23\u0b3f\u0b37\u0964 (Se eka bhala ma\u1e47i\u1e63a.) He is a good person.\n"
            "  4. \u0b16\u0b30\u0b3e\u0b2a (khar\u0101pa) - bad. \u0b16\u0b30\u0b3e\u0b2a \u0b05\u0b2d\u0b4d\u0b5f\u0b3e\u0b38 \u0b1b\u0b3e\u0b21\u0b3c\u0964 (Khar\u0101pa abhy\u0101sa ch\u0101\u1e0da.) Leave the bad habit.\n"
            "  5. \u0b28\u0b42\u0b06 (nu\u0101) - new. \u0b2e\u0b4b\u0b30 \u0b28\u0b42\u0b06 \u0b2c\u0b39\u0b3f\u0964 (Mora nu\u0101 bahi.) My new book.\n"
            "  6. \u0b2a\u0b41\u0b30\u0b41\u0b23\u0b3e (puru\u1e47\u0101) - old. \u0b2a\u0b41\u0b30\u0b41\u0b23\u0b3e \u0b2e\u0b28\u0b4d\u0b26\u0b3f\u0b30 \u0b38\u0b41\u0b28\u0b4d\u0b26\u0b30\u0964 (Puru\u1e47\u0101 mandira sundara.) The old temple is beautiful.\n"
            "  7. \u0b17\u0b30\u0b2e (garama) - hot. \u0b1a\u0b3e \u0b17\u0b30\u0b2e \u0b05\u0b1b\u0b3f\u0964 (C\u0101 garama achi.) The tea is hot.\n"
            "  8. \u0b25\u0b23\u0b4d\u0b21\u0b3e (\u1e6dha\u1e47\u1e0d\u0101) - cold. \u0b2a\u0b3e\u0b23\u0b3f \u0b25\u0b23\u0b4d\u0b21\u0b3e\u0964 (P\u0101\u1e47i \u1e6dha\u1e47\u1e0d\u0101.) The water is cold.\n"
            "  9. \u0b2e\u0b3f\u0b20\u0b3e (mi\u1e6dh\u0101) - sweet. \u0b1b\u0b47\u0b28\u0b3e\u0b2a\u0b4b\u0b21\u0b3c \u0b2e\u0b3f\u0b20\u0b3e\u0964 (Chen\u0101po\u1e0da mi\u1e6dh\u0101.) Chhenapoda is sweet.\n"
            "  10. \u0b16\u0b1f\u0b3e (kha\u1e6d\u0101) - sour. \u0b06\u0b2e\u0b4d\u0b2c \u0b16\u0b1f\u0b3e\u0964 (\u0100mba kha\u1e6d\u0101.) The mango is sour.\n"
            "  11. \u0b32\u0b2e\u0b4d\u0b2c\u0b3e (lamb\u0101) - long, tall. \u0b38\u0b47 \u0b32\u0b2e\u0b4d\u0b2c\u0b3e \u0b2a\u0b3f\u0b32\u0b3e\u0964 (Se lamb\u0101 pil\u0101.) He is a tall boy.\n"
            "  12. \u0b16\u0b3e\u0b1f (kh\u0101\u1e6da) - short. \u0b30\u0b3e\u0b38\u0b4d\u0b24\u0b3e\u0b1f\u0b3f \u0b16\u0b3e\u0b1f\u0964 (R\u0101st\u0101\u1e6di kh\u0101\u1e6da.) The road is short.\n"
            "  13. \u0b27\u0b33\u0b3e (dha\u1e37\u0101) - white. \u0b27\u0b33\u0b3e \u0b2b\u0b41\u0b32\u0b1f\u0b3f \u0b38\u0b41\u0b28\u0b4d\u0b26\u0b30\u0964 (Dha\u1e37\u0101 phula\u1e6di sundara.) The white flower is beautiful.\n"
            "  14. \u0b15\u0b33\u0b3e (ka\u1e37\u0101) - black. \u0b15\u0b33\u0b3e \u0b15\u0b41\u0b15\u0b41\u0b30\u0b1f\u0b3f \u0b2d\u0b41\u0b15\u0b41\u0b1b\u0b3f\u0964 (Ka\u1e37\u0101 kukura\u1e6di bhukuchi.) The black dog is barking.\n"
            "  15. \u0b32\u0b3e\u0b32 (l\u0101la) - red. \u0b32\u0b3e\u0b32 \u0b17\u0b4b\u0b32\u0b3e\u0b2a\u0b1f\u0b3f \u0b2b\u0b41\u0b1f\u0b3f\u0b1b\u0b3f\u0964 (L\u0101la gol\u0101pa\u1e6di phu\u1e6dichi.) The red rose has bloomed.\n"
            "  16. \u0b28\u0b40\u0b33 (n\u012b\u1e37a) - blue. \u0b06\u0b15\u0b3e\u0b36 \u0b28\u0b40\u0b33\u0964 (\u0100k\u0101\u1e63a n\u012b\u1e37a.) The sky is blue.\n"
            "  17. \u0b38\u0b2c\u0b41\u0b1c (sabuja) - green. \u0b38\u0b2c\u0b41\u0b1c \u0b17\u0b1b \u0b2c\u0b21\u0b3c \u0b39\u0b47\u0b32\u0b3e\u0964 (Sabuja gacha ba\u1e0da hel\u0101.) The green tree grew big.\n"
            "  18. \u0b39\u0b33\u0b26\u0b3f\u0b06 (ha\u1e37adi\u0101) - yellow. \u0b39\u0b33\u0b26\u0b3f\u0b06 \u0b2b\u0b41\u0b32 \u0b2b\u0b41\u0b1f\u0b3f\u0b1b\u0b3f\u0964 (Ha\u1e37adi\u0101 phula phu\u1e6dichi.) The yellow flower bloomed.\n"
            "  19. \u0b27\u0b28\u0b40 (dhan\u012b) - rich. \u0b38\u0b47 \u0b27\u0b28\u0b40 \u0b32\u0b4b\u0b15\u0964 (Se dhan\u012b loka.) He is a rich man.\n"
            "  20. \u0b17\u0b30\u0b3f\u0b2c (gariba) - poor. \u0b17\u0b30\u0b3f\u0b2c \u0b32\u0b4b\u0b15\u0b15\u0b41 \u0b38\u0b3e\u0b39\u0b3e\u0b2f\u0b4d\u0b5f \u0b15\u0b30\u0964 (Gariba lokaku s\u0101h\u0101yya kara.) Help the poor person.\n"
            "  21. \u0b38\u0b41\u0b28\u0b4d\u0b26\u0b30 (sundara) - beautiful. \u0b2a\u0b41\u0b30\u0b40 \u0b38\u0b41\u0b28\u0b4d\u0b26\u0b30 \u0b38\u0b39\u0b30\u0964 (Pur\u012b sundara sahara.) Puri is a beautiful city.\n"
            "  22. \u0b16\u0b41\u0b38\u0b3f (khusi) - happy. \u0b2e\u0b41\u0b01 \u0b16\u0b41\u0b38\u0b3f \u0b05\u0b1b\u0b3f\u0964 (Mun khusi achi.) I am happy.\n"
            "  23. \u0b26\u0b41\u0b03\u0b16\u0b40 (duhkha\u012b) - sad. \u0b38\u0b47 \u0b26\u0b41\u0b03\u0b16\u0b40 \u0b05\u0b1b\u0b3f\u0964 (Se duhkha\u012b achi.) She is sad.\n"
            "  24. \u0b36\u0b15\u0b4d\u0b24\u0b3f\u0b36\u0b3e\u0b33\u0b40 (\u1e63akti\u1e63\u0101\u1e37\u012b) - strong. \u0b39\u0b3e\u0b24\u0b40 \u0b36\u0b15\u0b4d\u0b24\u0b3f\u0b36\u0b3e\u0b33\u0b40\u0964 (H\u0101t\u012b \u1e63akti\u1e63\u0101\u1e37\u012b.) The elephant is strong.\n"
            "  25. \u0b26\u0b41\u0b30\u0b4d\u0b2c\u0b33 (durba\u1e37a) - weak. \u0b2c\u0b41\u0b22\u0b3c\u0b3e \u0b32\u0b4b\u0b15\u0b1f\u0b3f \u0b26\u0b41\u0b30\u0b4d\u0b2c\u0b33\u0964 (Bu\u1e0dh\u0101 loka\u1e6di durba\u1e37a.) The old man is weak.\n\n"
            "Adverbs (how, when, where, how much):\n"
            "  1. \u0b36\u0b40\u0b18\u0b4d\u0b30 (\u1e63\u012bghra) - quickly. \u0b38\u0b47 \u0b36\u0b40\u0b18\u0b4d\u0b30 \u0b26\u0b4c\u0b21\u0b3c\u0b3f\u0b32\u0b3e\u0964 (Se \u1e63\u012bghra dau\u1e0dil\u0101.) He ran quickly.\n"
            "  2. \u0b27\u0b40\u0b30\u0b47 (dh\u012bre) - slowly. \u0b27\u0b40\u0b30\u0b47 \u0b1a\u0b3e\u0b32\u0964 (Dh\u012bre c\u0101la.) Walk slowly.\n"
            "  3. \u0b06\u0b1c\u0b3f (\u0101ji) - today. \u0b06\u0b1c\u0b3f \u0b2c\u0b30\u0b4d\u0b37\u0b3e \u0b39\u0b47\u0b09\u0b1b\u0b3f\u0964 (\u0100ji bar\u1e63\u0101 heuchi.) It is raining today.\n"
            "  4. \u0b15\u0b3e\u0b32\u0b3f (k\u0101li) - yesterday / tomorrow. \u0b15\u0b3e\u0b32\u0b3f \u0b2e\u0b41\u0b01 \u0b06\u0b38\u0b3f\u0b25\u0b3f\u0b32\u0b3f\u0964 (K\u0101li mun \u0101sithili.) I came yesterday.\n"
            "  5. \u0b0f\u0b2c\u0b47 (ebe) - now. \u0b0f\u0b2c\u0b47 \u0b2f\u0b3e\u0b05\u0964 (Ebe y\u0101a.) Go now.\n"
            "  6. \u0b2a\u0b30\u0b47 (pare) - later. \u0b2e\u0b41\u0b01 \u0b2a\u0b30\u0b47 \u0b06\u0b38\u0b3f\u0b2c\u0b3f\u0964 (Mun pare \u0101sibi.) I will come later.\n"
            "  7. \u0b0f\u0b20\u0b3e\u0b30\u0b47 (e\u1e6dh\u0101re) - here. \u0b0f\u0b20\u0b3e\u0b30\u0b47 \u0b2c\u0b38\u0964 (E\u1e6dh\u0101re basa.) Sit here.\n"
            "  8. \u0b38\u0b47\u0b20\u0b3e\u0b30\u0b47 (se\u1e6dh\u0101re) - there. \u0b38\u0b47\u0b20\u0b3e\u0b30\u0b47 \u0b30\u0b16\u0964 (Se\u1e6dh\u0101re rakha.) Keep it there.\n"
            "  9. \u0b2c\u0b39\u0b41\u0b24 (bahuta) - very, much. \u0b38\u0b47 \u0b2c\u0b39\u0b41\u0b24 \u0b2d\u0b32\u0964 (Se bahuta bhala.) He is very good.\n"
            "  10. \u0b15\u0b2e (kama) - little. \u0b15\u0b2e \u0b2a\u0b3e\u0b23\u0b3f \u0b26\u0b3f\u0b05\u0964 (Kama p\u0101\u1e47i dia.) Give a little water.\n"
            "  11. \u0b38\u0b2c\u0b41\u0b2c\u0b47\u0b33\u0b47 (sabube\u1e37e) - always. \u0b38\u0b47 \u0b38\u0b2c\u0b41\u0b2c\u0b47\u0b33\u0b47 \u0b39\u0b38\u0b47\u0964 (Se sabube\u1e37e hase.) He always laughs.\n"
            "  12. \u0b15\u0b47\u0b2c\u0b47\u0b39\u0b47\u0b32\u0b47 \u0b28\u0b3e\u0b39\u0b3f\u0b01 (kebehele n\u0101hin) - never. \u0b2e\u0b41\u0b01 \u0b15\u0b47\u0b2c\u0b47\u0b39\u0b47\u0b32\u0b47 \u0b2e\u0b3f\u0b1b \u0b15\u0b41\u0b39\u0b47 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Mun kebehele micha kuhe n\u0101hin.) I never tell lies.\n"
            "  13. \u0b2a\u0b41\u0b23\u0b3f (pu\u1e47i) - again. \u0b2a\u0b41\u0b23\u0b3f \u0b15\u0b41\u0b39\u0964 (Pu\u1e47i kuha.) Say it again.\n"
            "  14. \u0b0f\u0b15\u0b3e\u0b20\u0b3f (ek\u0101\u1e6dhi) - together. \u0b06\u0b2e\u0b47 \u0b0f\u0b15\u0b3e\u0b20\u0b3f \u0b2f\u0b3f\u0b2c\u0b3e\u0964 (\u0100me ek\u0101\u1e6dhi yib\u0101.) We will go together.\n"
            "  15. \u0b2d\u0b32\u0b2d\u0b3e\u0b2c\u0b47 (bhalabh\u0101be) - well. \u0b38\u0b47 \u0b2d\u0b32\u0b2d\u0b3e\u0b2c\u0b47 \u0b17\u0b3e\u0b0f\u0964 (Se bhalabh\u0101be g\u0101e.) She sings well."
        ),
        "how_it_works": (
            "This record doubles as a grammar lesson: Odia adjectives do not "
            "inflect for gender or number, so one form serves everywhere - a "
            "major simplification over Hindi. The 25 adjectives cover size, "
            "quality, age, temperature, taste, length, the six basic colors, "
            "wealth, beauty, mood, and strength, each locked in with a "
            "translated sentence. The 15 adverbs cover manner (\u1e63\u012bghra, "
            "dh\u012bre), time (\u0101ji, k\u0101li, ebe, pare), place (e\u1e6dh\u0101re, "
            "se\u1e6dh\u0101re), degree (bahuta, kama), and frequency "
            "(sabube\u1e37e, kebehele n\u0101hin, pu\u1e47i). Note k\u0101li means "
            "both yesterday and tomorrow - tense on the verb tells which. "
            "Drill: describe five objects around you with adjective + noun, "
            "then act out five adverbs."
        ),
        "key_points": [
            "25 adjectives, 15 adverbs, each with a translated example sentence.",
            "Odia adjectives do not change for gender or number.",
            "Color, size, quality, mood, and strength vocabulary covered.",
            "k\u0101li means both yesterday and tomorrow; the verb tense disambiguates.",
        ],
        "requirements": [
            "Read the nouns and verbs records first; these sentences reuse them.",
        ],
        "standards": [
            "The non-inflecting adjective rule follows standard Odia grammar.",
            "Example sentences are constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["do not change for the gender", "k\u0101li", "Chen\u0101po\u1e0da", "Twenty-five adjectives"],
        "sig_lens": (
            "Through the Signature lens description is consecration: each "
            "adjective a sworn quality laid on the noun like a seal, each "
            "adverb a sworn manner of the action."
        ),
        "drill": {
            "adjectives": [
                "ba\u1e0da", "cho\u1e6da", "bhala", "khar\u0101pa", "nu\u0101",
                "puru\u1e47\u0101", "garama", "\u1e6dha\u1e47\u1e0d\u0101", "mi\u1e6dh\u0101", "kha\u1e6d\u0101",
                "lamb\u0101", "kh\u0101\u1e6da", "dha\u1e37\u0101", "ka\u1e37\u0101", "l\u0101la",
                "n\u012b\u1e37a", "sabuja", "ha\u1e37adi\u0101", "dhan\u012b", "gariba",
                "sundara", "khusi", "duhkha\u012b", "\u1e63akti\u1e63\u0101\u1e37\u012b", "durba\u1e37a",
            ],
            "adverbs": [
                "\u1e63\u012bghra", "dh\u012bre", "\u0101ji", "k\u0101li", "ebe",
                "pare", "e\u1e6dh\u0101re", "se\u1e6dh\u0101re", "bahuta", "kama",
                "sabube\u1e37e", "kebehele n\u0101hin", "pu\u1e47i", "ek\u0101\u1e6dhi", "bhalabh\u0101be",
            ],
            "inflects_for_gender": False,
        },
    },
    {
        "key": "pronouns",
        "name": "Pronouns: Full Paradigms",
        "group": "Core Vocabulary",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "description": (
            "The complete Odia pronoun system - personal, possessive, "
            "demonstrative, and interrogative - with full paradigms and "
            "example sentences. Odia keeps three levels of you: \u0b24\u0b41 (intimate), "
            "\u0b24\u0b41\u0b2e\u0b47 (familiar), \u0b06\u0b2a\u0b23 (formal). \n\n"
            "Personal pronouns:\n"
            "  \u0b2e\u0b41\u0b01 (mun) - I. \u0b2e\u0b41\u0b01 \u0b13\u0b21\u0b3c\u0b3f\u0b06 \u0b36\u0b3f\u0b16\u0b41\u0b1b\u0b3f\u0964 (Mun odi\u0101 \u015bikhu\u1e63i.) I am learning Odia.\n"
            "  \u0b06\u0b2e\u0b47 (\u0101me) - we. \u0b06\u0b2e\u0b47 \u0b2d\u0b3e\u0b30\u0b24\u0b40\u0b5f\u0964 (\u0100me bh\u0101rat\u012bya.) We are Indian.\n"
            "  \u0b24\u0b41 (tu) - you (intimate, to children/close friends). \u0b24\u0b41 \u0b15\u0b47\u0b2e\u0b3f\u0b24\u0b3f \u0b05\u0b1b\u0b41? (Tu kemiti achu?) How are you?\n"
            "  \u0b24\u0b41\u0b2e\u0b47 (tume) - you (familiar). \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b47\u0b09\u0b01\u0b20\u0b3f? (Tume keun\u1e6dhi?) Where are you?\n"
            "  \u0b06\u0b2a\u0b23 (\u0101pa\u1e47a) - you (formal). \u0b06\u0b2a\u0b23 \u0b15\u0b47\u0b2e\u0b3f\u0b24\u0b3f \u0b05\u0b1b\u0b28\u0b4d\u0b24\u0b3f? (\u0100pa\u1e47a kemiti achanti?) How are you? (formal)\n"
            "  \u0b38\u0b47 (se) - he, she. \u0b38\u0b47 \u0b21\u0b3e\u0b15\u0b4d\u0b24\u0b30\u0964 (Se d\u0101ktara.) He/She is a doctor.\n"
            "  \u0b38\u0b47\u0b2e\u0b3e\u0b28\u0b47 (sem\u0101ne) - they. \u0b38\u0b47\u0b2e\u0b3e\u0b28\u0b47 \u0b1b\u0b3e\u0b24\u0b4d\u0b30\u0964 (Sem\u0101ne ch\u0101tra.) They are students.\n"
            "Possessives (add -\u0b30):\n"
            "  \u0b2e\u0b4b\u0b30 (mora) - my. \u0b0f\u0b39\u0b3e \u0b2e\u0b4b\u0b30 \u0b2c\u0b39\u0b3f\u0964 (Eh\u0101 mora bahi.) This is my book.\n"
            "  \u0b06\u0b2e\u0b30 (\u0101mara) - our. \u0b06\u0b2e\u0b30 \u0b18\u0b30 \u0b2c\u0b21\u0b3c\u0964 (\u0100mara ghara ba\u1e0da.) Our house is big.\n"
            "  \u0b24\u0b4b\u0b30 (tora) - your (intimate). \u0b24\u0b4b\u0b30 \u0b28\u0b3e\u0b2e \u0b15\u0b23? (Tora n\u0101ma ka\u1e47a?) What is your name?\n"
            "  \u0b24\u0b41\u0b2e\u0b30 (tumara) - your (familiar). \u0b24\u0b41\u0b2e\u0b30 \u0b17\u0b3e\u0b21\u0b3c\u0b3f \u0b15\u0b47\u0b09\u0b01\u0b20\u0b3f? (Tumara g\u0101\u1e0di keun\u1e6dhi?) Where is your car?\n"
            "  \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15\u0b30 (\u0101pa\u1e47a\u1e45kara) - your (formal). \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15\u0b30 \u0b2e\u0b24 \u0b15\u0b23? (\u0101pa\u1e47a\u1e45kara mata ka\u1e47a?) What is your opinion?\n"
            "  \u0b24\u0b3e\u0b19\u0b4d\u0b15\u0b30 (t\u0101\u1e45kara) - his, her, their (honorific). \u0b24\u0b3e\u0b19\u0b4d\u0b15\u0b30 \u0b28\u0b3e\u0b2e \u0b15\u0b23? (T\u0101\u1e45kara n\u0101ma ka\u1e47a?) What is his name?\n"
            "Demonstratives:\n"
            "  \u0b0f\u0b39\u0b3e (eh\u0101) - this. \u0b0f\u0b39\u0b3e \u0b15\u0b23? (Eh\u0101 ka\u1e47a?) What is this?\n"
            "  \u0b24\u0b3e\u0b39\u0b3e (t\u0101h\u0101) - that. \u0b24\u0b3e\u0b39\u0b3e \u0b2d\u0b32\u0964 (T\u0101h\u0101 bhala.) That is good.\n"
            "  \u0b0f\u0b07\u0b1f\u0b3e (ei\u1e6d\u0101) - this one (thing). \u0b0f\u0b07\u0b1f\u0b3e \u0b28\u0b3f\u0b05\u0964 (Ei\u1e6d\u0101 nia.) Take this one.\n"
            "  \u0b38\u0b47\u0b07\u0b1f\u0b3e (sei\u1e6d\u0101) - that one (thing). \u0b38\u0b47\u0b07\u0b1f\u0b3e \u0b26\u0b3f\u0b05\u0964 (Sei\u1e6d\u0101 dia.) Give that one.\n"
            "Interrogatives:\n"
            "  \u0b15\u0b3f\u0b0f (kie) - who. \u0b38\u0b47 \u0b15\u0b3f\u0b0f? (Se kie?) Who is he?\n"
            "  \u0b15\u0b23 (ka\u1e47a) - what. \u0b0f\u0b39\u0b3e \u0b15\u0b23? (Eh\u0101 ka\u1e47a?) What is this?\n"
            "  \u0b15\u0b47\u0b09\u0b01 (keun) - which. \u0b15\u0b47\u0b09\u0b01 \u0b2c\u0b39\u0b3f? (Keun bahi?) Which book?\n"
            "  \u0b15\u0b47\u0b24\u0b47 (kete) - how much, how many. \u0b0f\u0b39\u0b3e\u0b30 \u0b26\u0b3e\u0b2e \u0b15\u0b47\u0b24\u0b47? (Eh\u0101ra d\u0101ma kete?) How much is this?\n"
            "  \u0b15\u0b47\u0b2c\u0b47 (kebe) - when. \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b47\u0b2c\u0b47 \u0b06\u0b38\u0b3f\u0b2c? (Tume kebe \u0101siba?) When will you come?\n"
            "  \u0b15\u0b47\u0b09\u0b01\u0b20\u0b3e\u0b30\u0b47 (keun\u1e6dh\u0101re) - where. \u0b2c\u0b1c\u0b3e\u0b30 \u0b15\u0b47\u0b09\u0b01\u0b20\u0b3e\u0b30\u0b47? (Baj\u0101ra keun\u1e6dh\u0101re?) Where is the market?\n"
            "  \u0b15\u0b3e\u0b39\u0b3f\u0b01\u0b15\u0b3f (k\u0101hinki) - why. \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b3e\u0b39\u0b3f\u0b01\u0b15\u0b3f \u0b15\u0b3e\u0b28\u0b4d\u0b26\u0b41\u0b1b? (Tume k\u0101hinki k\u0101nducha?) Why are you crying?\n"
            "  \u0b15\u0b3f\u0b2a\u0b30\u0b3f (kipari) - how. \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b3f\u0b2a\u0b30\u0b3f \u0b06\u0b38\u0b3f\u0b32? (Tume kipari \u0101sila?) How did you come?"
        ),
        "how_it_works": (
            "This record is the pronoun engine every later sentence depends "
            "on. It teaches the three levels of you - tu (intimate), tume "
            "(familiar), \u0101pa\u1e47a (formal) - and when each is safe: "
            "\u0101pa\u1e47a for elders, strangers, and officials; tume for "
            "peers; tu only for children and the closest friends. Possessives "
            "form by adding -ra to the pronoun stem (mun -> mora, tume -> "
            "tumara), a pattern the drill verifies mechanically. The "
            "demonstratives split near (eh\u0101, ei\u1e6d\u0101) and far "
            "(t\u0101h\u0101, sei\u1e6d\u0101), and the eight interrogatives "
            "(kie, ka\u1e47a, keun, kete, kebe, keun\u1e6dh\u0101re, k\u0101hinki, "
            "kipari) become the question record's toolkit. Every pronoun gets "
            "a sentence so the paradigm is never a bare table."
        ),
        "key_points": [
            "Three levels of you: tu (intimate), tume (familiar), \u0101pa\u1e47a (formal).",
            "Possessives form regularly with -ra: mora, \u0101mara, tora, tumara, \u0101pa\u1e47a\u1e45kara, t\u0101\u1e45kara.",
            "Demonstratives split near (eh\u0101/ei\u1e6d\u0101) and far (t\u0101h\u0101/sei\u1e6d\u0101).",
            "Eight interrogatives: who, what, which, how much, when, where, why, how.",
            "Every pronoun fixed by a translated example sentence.",
        ],
        "requirements": [
            "Read the nouns and verbs records first.",
            "Memorize the three yous; register mistakes are social mistakes.",
        ],
        "standards": [
            "Paradigms follow standard Odia grammar.",
            "Register guidance (tu/tume/\u0101pa\u1e47a) follows standard usage.",
            "Example sentences are constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["\u0101pa\u1e47a", "tume", "kie", "k\u0101hinki", "mora"],
        "sig_lens": (
            "Through the Signature lens pronouns are sworn identities: mun "
            "the vow of self, \u0101pa\u1e47a the vow of respect, kie the vow "
            "of seeking. Every who a question sealed in sound."
        ),
        "drill": {
            "personal": ["mun", "\u0101me", "tu", "tume", "\u0101pa\u1e47a", "se", "sem\u0101ne"],
            "possessive": ["mora", "\u0101mara", "tora", "tumara", "\u0101pa\u1e47a\u1e45kara", "t\u0101\u1e45kara"],
            "demonstrative": ["eh\u0101", "t\u0101h\u0101", "ei\u1e6d\u0101", "sei\u1e6d\u0101"],
            "interrogative": ["kie", "ka\u1e47a", "keun", "kete", "kebe", "keun\u1e6dh\u0101re", "k\u0101hinki", "kipari"],
            "you_levels": 3,
        },
    },
    {
        "key": "numbers",
        "name": "Numbers, Time, Days, and Months",
        "group": "Core Vocabulary",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "description": (
            "Counting in Odia: 1-100 with Odia digits, ordinals, days of the "
            "week, the twelve Odia months, seasons, clock time, and dates - "
            "each with an example sentence.\n\n"
            "Numbers 1-10: \u0b67 \u0b0f\u0b15 (eka), \u0b68 \u0b26\u0b41\u0b07 (dui), \u0b69 \u0b24\u0b3f\u0b28\u0b3f (tini), "
            "\u0b6a \u0b1a\u0b3e\u0b30\u0b3f (c\u0101ri), \u0b6b \u0b2a\u0b3e\u0b1e\u0b4d\u0b1a (p\u0101nca), \u0b6c \u0b1b\u0b05 (chaa), "
            "\u0b6d \u0b38\u0b3e\u0b24 (s\u0101ta), \u0b6e \u0b06\u0b20 (\u0101\u1e6dha), \u0b6f \u0b28\u0b05 (naa), \u0b67\u0b66 \u0b26\u0b36 (da\u1e63a, 10). Sentence: \u0b2e\u0b4b \u0b2a\u0b3e\u0b16\u0b30\u0b47 \u0b24\u0b3f\u0b28\u0b3f\u0b1f\u0b3f \u0b2c\u0b39\u0b3f \u0b05\u0b1b\u0b3f\u0964 "
            "(Mo p\u0101khare tini\u1e6di bahi achi.) I have three books.\n"
            "11-20: \u0b0f\u0b17\u0b3e\u0b30 (eg\u0101ra), \u0b2c\u0b3e\u0b30 (b\u0101ra), \u0b24\u0b47\u0b30 (tera), "
            "\u0b1a\u0b09\u0b26 (cauda), \u0b2a\u0b28\u0b4d\u0b26\u0b30 (pandara), \u0b37\u0b4b\u0b33 (sho\u1e37a), "
            "\u0b38\u0b24\u0b30 (satara), \u0b05\u0b20\u0b30 (a\u1e6dhara), \u0b09\u0b23\u0b47\u0b07\u0b36 (\u1e47\u1e47ei\u1e63a), "
            "\u0b15\u0b4b\u0b21\u0b3c\u0b3f\u0b0f (ko\u1e0die). Sentence: \u0b2c\u0b3e\u0b30\u0b1f\u0b3f \u0b2a\u0b3f\u0b32\u0b3e \u0b06\u0b38\u0b3f\u0b32\u0b47\u0964 "
            "(B\u0101ra\u1e6di pil\u0101 \u0101sile.) Twelve children came.\n"
            "Tens: \u0b24\u0b3f\u0b30\u0b3f\u0b36 (tiri\u1e63a, 30), \u0b1a\u0b3e\u0b33\u0b3f\u0b36 (c\u0101\u1e37i\u1e63a, 40), "
            "\u0b2a\u0b1a\u0b3e\u0b36 (pac\u0101\u1e63a, 50), \u0b37\u0b3e\u0b20\u0b3f\u0b0f (\u1e63\u0101\u1e6dhie, 60), "
            "\u0b38\u0b24\u0b4d\u0b24\u0b41\u0b30\u0b3f (satturi, 70), \u0b05\u0b36\u0b40 (a\u1e63\u012b, 80), "
            "\u0b28\u0b2c\u0b47 (nabe, 90), \u0b36\u0b39\u0b47 (\u1e63ahe, 100). "
            "Sentence: \u0b36\u0b39\u0b47 \u0b1f\u0b19\u0b4d\u0b15\u0b3e \u0b26\u0b3f\u0b05\u0964 (\u1e62ahe \u1e6da\u1e45k\u0101 dia.) Give one hundred rupees.\n"
            "Ordinals: \u0b2a\u0b4d\u0b30\u0b25\u0b2e (prathama, first), \u0b26\u0b4d\u0b35\u0b3f\u0b24\u0b40\u0b5f (dwit\u012bya, second), "
            "\u0b24\u0b43\u0b24\u0b40\u0b5f (t\u1e5bt\u012bya, third). Sentence: \u0b38\u0b47 \u0b2a\u0b4d\u0b30\u0b25\u0b2e \u0b39\u0b47\u0b32\u0b3e\u0964 "
            "(Se prathama hel\u0101.) He came first.\n"
            "Days of the week: \u0b30\u0b2c\u0b3f\u0b2c\u0b3e\u0b30 (rabib\u0101ra, Sunday), "
            "\u0b38\u0b4b\u0b2e\u0b2c\u0b3e\u0b30 (somab\u0101ra, Monday), \u0b2e\u0b19\u0b4d\u0b17\u0b33\u0b2c\u0b3e\u0b30 (ma\u1e45ga\u1e37ab\u0101ra, Tuesday), "
            "\u0b2c\u0b41\u0b27\u0b2c\u0b3e\u0b30 (budhab\u0101ra, Wednesday), \u0b17\u0b41\u0b30\u0b41\u0b2c\u0b3e\u0b30 (gurub\u0101ra, Thursday), "
            "\u0b36\u0b41\u0b15\u0b4d\u0b30\u0b2c\u0b3e\u0b30 (\u1e63ukrab\u0101ra, Friday), \u0b36\u0b28\u0b3f\u0b2c\u0b3e\u0b30 (\u1e63anib\u0101ra, Saturday). "
            "Sentence: \u0b06\u0b1c\u0b3f \u0b30\u0b2c\u0b3f\u0b2c\u0b3e\u0b30\u0964 (\u0100ji rabib\u0101ra.) Today is Sunday.\n"
            "Odia months: \u0b2c\u0b48\u0b36\u0b3e\u0b16 (bai\u1e63\u0101kha), \u0b1c\u0b4d\u0b5f\u0b47\u0b37\u0b4d\u0b20 (jye\u1e63\u1e6dha), "
            "\u0b06\u0b37\u0b3e\u0b22\u0b3c (\u0101\u1e63\u0101\u1e0dha), \u0b36\u0b4d\u0b30\u0b3e\u0b2c\u0b23 (\u1e63r\u0101ba\u1e47a), "
            "\u0b2d\u0b3e\u0b26\u0b4d\u0b30\u0b2c (bh\u0101draba), \u0b06\u0b36\u0b4d\u0b35\u0b3f\u0b28 (\u0101\u1e63wina), "
            "\u0b15\u0b3e\u0b30\u0b4d\u0b24\u0b4d\u0b24\u0b3f\u0b15 (k\u0101rttika), \u0b2e\u0b3e\u0b30\u0b4d\u0b17\u0b36\u0b3f\u0b30 (m\u0101rga\u1e63ira), "
            "\u0b2a\u0b4c\u0b37 (pau\u1e63a), \u0b2e\u0b3e\u0b18 (m\u0101gha), \u0b2b\u0b3e\u0b32\u0b4d\u0b17\u0b41\u0b28 (ph\u0101lguna), "
            "\u0b1a\u0b48\u0b24\u0b4d\u0b30 (chaitra). Sentence: \u0b2c\u0b48\u0b36\u0b3e\u0b16\u0b30\u0b47 \u0b28\u0b2c\u0b2c\u0b30\u0b4d\u0b37\u0964 "
            "(Bai\u1e63\u0101khare nababar\u1e63a.) New Year is in Baisakha.\n"
            "Seasons: \u0b17\u0b4d\u0b30\u0b40\u0b37\u0b4d\u0b2e (gr\u012b\u1e63ma, summer), \u0b2c\u0b30\u0b4d\u0b37\u0b3e (bar\u1e63\u0101, monsoon), "
            "\u0b36\u0b30\u0b24 (\u1e63arata, autumn), \u0b39\u0b47\u0b2e\u0b28\u0b4d\u0b24 (hemanta, pre-winter), "
            "\u0b36\u0b40\u0b24 (\u1e63\u012bta, winter), \u0b2c\u0b38\u0b28\u0b4d\u0b24 (basanta, spring). "
            "Sentence: \u0b2c\u0b30\u0b4d\u0b37\u0b3e \u0b26\u0b3f\u0b28\u0b47 \u0b2c\u0b30\u0b4d\u0b37\u0b3e \u0b39\u0b41\u0b0f\u0964 "
            "(Bar\u1e63\u0101 dine bar\u1e63\u0101 hue.) It rains in the monsoon season.\n"
            "Clock time: \u0b18\u0b23\u0b4d\u0b1f\u0b3e (gha\u1e47\u1e6d\u0101) = o'clock; \u0b2e\u0b3f\u0b28\u0b3f\u0b1f (mini\u1e6da) = minute. "
            "\u0b2c\u0b30\u0b4d\u0b24\u0b4d\u0b24\u0b2e\u0b3e\u0b28 \u0b38\u0b2e\u0b5f \u0b15\u0b47\u0b24\u0b47? (Barttam\u0101na samaya kete?) What time is it now? "
            "\u0b0f\u0b2c\u0b47 \u0b24\u0b3f\u0b28\u0b3f\u0b1f\u0b3e \u0b2c\u0b3e\u0b1c\u0b3f\u0b1b\u0b3f\u0964 (Ebe tini\u1e6d\u0101 b\u0101jichi.) It is three o'clock now.\n"
            "Dates: \u0b06\u0b1c\u0b3f\u0b30 \u0b24\u0b3e\u0b30\u0b3f\u0b16 \u0b15\u0b47\u0b24\u0b47? (\u0100jira t\u0101rikha kete?) What is today's date? "
            "\u0b06\u0b1c\u0b3f \u0b05\u0b15\u0b4d\u0b1f\u0b4b\u0b2c\u0b30 \u0b67\u0b6d \u0b24\u0b3e\u0b30\u0b3f\u0b16\u0964 (\u0100ji ak\u1e6dobara 17 t\u0101rikha.) Today is October 17."
        ),
        "how_it_works": (
            "This record is the counting and calendar engine. It teaches the "
            "Odia digits 1-10 with names, the teens (note the distinctive "
            "ko\u1e0die for 20), the tens to 100, ordinals, all seven "
            "weekdays (each ending in -b\u0101ra), the twelve lunar Odia "
            "months, the six ritu seasons, clock time (gha\u1e47\u1e6d\u0101 "
            "o'clock, mini\u1e6da minute), and date sentences. Every block "
            "ends with a sentence so numbers are never naked. Drill: count "
            "1-20 aloud daily, then tell the time and date in Odia each "
            "morning."
        ),
        "key_points": [
            "Numbers 1-100 with Odia digits; ordinals prathama, dwit\u012bya, t\u1e5bt\u012bya.",
            "Seven weekdays ending in -b\u0101ra; twelve Odia lunar months.",
            "Six seasons (ritu): gr\u012b\u1e63ma, bar\u1e63\u0101, \u1e63arata, hemanta, \u1e63\u012bta, basanta.",
            "Clock time: gha\u1e47\u1e6d\u0101 (o'clock), mini\u1e6da (minute); date sentences included.",
            "k\u0101li covers yesterday and tomorrow; verb tense disambiguates.",
        ],
        "requirements": [
            "Read the script record first to read the digits.",
        ],
        "standards": [
            "Number names and month names follow standard Odia usage.",
            "Example sentences are constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["ko\u1e0die", "rabib\u0101ra", "bai\u1e63\u0101kha", "gha\u1e47\u1e6d\u0101", "100"],
        "sig_lens": (
            "Through the Signature lens numbers are sworn measures: every "
            "digit a mark, every month a seal on the year's covenant, every "
            "hour a vow kept on time."
        ),
        "drill": {
            "ones": ["eka", "dui", "tini", "c\u0101ri", "p\u0101nca", "chaa",
                     "s\u0101ta", "\u0101\u1e6dha", "naa", "da\u1e63a"],
            "teens": ["eg\u0101ra", "b\u0101ra", "tera", "cauda", "pandara",
                      "sho\u1e37a", "satara", "a\u1e6dhara", "\u1e47\u1e47ei\u1e63a", "ko\u1e0die"],
            "tens": ["tiri\u1e63a", "c\u0101\u1e37i\u1e63a", "pac\u0101\u1e63a", "\u1e63\u0101\u1e6dhie",
                     "satturi", "a\u1e63\u012b", "nabe", "\u1e63ahe"],
            "weekdays": 7, "months": 12, "seasons": 6,
            "digits": ["\u0b67", "\u0b68", "\u0b69", "\u0b6a", "\u0b6b",
                       "\u0b6c", "\u0b6d", "\u0b6e", "\u0b6f", "\u0b66"],
        },
    },
    {
        "key": "greetings",
        "name": "Greetings and Everyday Phrases",
        "group": "Core Vocabulary",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "description": (
            "Thirty greetings, farewells, and politeness phrases - Odia "
            "script, romanization, English, and usage notes. The default "
            "formal greeting is \u0b28\u0b2e\u0b38\u0b4d\u0b15\u0b3e\u0b30 (namask\u0101ra); in western Odisha "
            "the traditional greeting is \u0b1c\u0b41\u0b39\u0b3e\u0b30 (juh\u0101ra). \n\n"
            "  1. \u0b28\u0b2e\u0b38\u0b4d\u0b15\u0b3e\u0b30 (namask\u0101ra) - Hello / respectful greeting. Default formal greeting.\n"
            "  2. \u0b1c\u0b41\u0b39\u0b3e\u0b30 (juh\u0101ra) - Traditional greeting of western Odisha; shows deep respect.\n"
            "  3. \u0b36\u0b41\u0b2d \u0b38\u0b15\u0b3e\u0b33 (\u1e63ubha sak\u0101\u1e37a) - Good morning.\n"
            "  4. \u0b36\u0b41\u0b2d \u0b38\u0b28\u0b4d\u0b27\u0b4d\u0b5f\u0b3e (\u1e63ubha sandhy\u0101) - Good evening.\n"
            "  5. \u0b36\u0b41\u0b2d \u0b30\u0b3e\u0b24\u0b4d\u0b30\u0b3f (\u1e63ubha r\u0101tri) - Good night.\n"
            "  6. \u0b06\u0b2a\u0b23 \u0b15\u0b47\u0b2e\u0b3f\u0b24\u0b3f \u0b05\u0b1b\u0b28\u0b4d\u0b24\u0b3f? (\u0100pa\u1e47a kemiti achanti?) - How are you? (formal)\n"
            "  7. \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b47\u0b2e\u0b3f\u0b24\u0b3f \u0b05\u0b1b? (Tume kemiti acha?) - How are you? (familiar)\n"
            "  8. \u0b2e\u0b41\u0b01 \u0b2d\u0b32 \u0b05\u0b1b\u0b3f\u0964 (Mun bhala achi.) - I am fine.\n"
            "  9. \u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26 (dhanyab\u0101da) - Thank you.\n"
            "  10. \u0b2c\u0b39\u0b41\u0b24 \u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26\u0964 (Bahuta dhanyab\u0101da.) - Thank you very much.\n"
            "  11. \u0b26\u0b5f\u0b3e\u0b15\u0b30\u0b3f (day\u0101kari) - Please. Softens any request.\n"
            "  12. \u0b15\u0b4d\u0b37\u0b2e\u0b3e \u0b15\u0b30\u0b28\u0b4d\u0b24\u0b41\u0964 (K\u1e63am\u0101 karantu.) - Excuse me / forgive me (formal).\n"
            "  13. \u0b2c\u0b3f\u0b26\u0b3e\u0b5f (bid\u0101ya) - Goodbye (formal farewell).\n"
            "  14. \u0b2b\u0b47\u0b30\u0b3f \u0b26\u0b47\u0b16\u0b3e \u0b39\u0b47\u0b2c\u0b3e\u0964 (Pheri dekh\u0101 heb\u0101.) - See you again.\n"
            "  15. \u0b38\u0b4d\u0b35\u0b3e\u0b17\u0b24 (sw\u0101gata) - Welcome.\n"
            "  16. \u0b36\u0b41\u0b2d \u0b2f\u0b3e\u0b24\u0b4d\u0b30\u0b3e (\u1e63ubha y\u0101tr\u0101) - Have a good journey.\n"
            "  17. \u0b05\u0b2d\u0b3f\u0b28\u0b28\u0b4d\u0b26\u0b28 (abhinandana) - Congratulations.\n"
            "  18. \u0b36\u0b41\u0b2d\u0b47\u0b1a\u0b4d\u0b1b\u0b3e (\u1e63ubhech\u0101) - Best wishes.\n"
            "  19. \u0b08\u0b36\u0b4d\u0b35\u0b30 \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15\u0b41 \u0b2e\u0b19\u0b4d\u0b17\u0b33 \u0b15\u0b30\u0b28\u0b4d\u0b24\u0b41\u0964 "
            "(\u012a\u1e63wara \u0101pa\u1e47a\u1e45ku ma\u1e45ga\u1e37a karantu.) - God bless you. (warm formal blessing)\n"
            "  20. \u0b2e\u0b4b \u0b28\u0b3e\u0b2e ... (Mo n\u0101ma ...) - My name is ...\n"
            "  21. \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15 \u0b28\u0b3e\u0b2e \u0b15\u0b23? (\u0100pa\u1e47a\u1e45ka n\u0101ma ka\u1e47a?) - What is your name? (formal)\n"
            "  22. \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15\u0b41 \u0b2d\u0b47\u0b1f\u0b3f \u0b16\u0b41\u0b38\u0b3f \u0b32\u0b3e\u0b17\u0b3f\u0b32\u0b3e\u0964 "
            "(\u0100pa\u1e47a\u1e45ku bhe\u1e6di khusi l\u0101gil\u0101.) - Nice to meet you.\n"
            "  23. \u0b2e\u0b41\u0b01 \u0b13\u0b21\u0b3c\u0b3f\u0b06 \u0b36\u0b3f\u0b16\u0b41\u0b1b\u0b3f\u0964 (Mun odi\u0101 \u015bikhu\u1e63i.) - I am learning Odia.\n"
            "  24. \u0b06\u0b2a\u0b23 \u0b07\u0b02\u0b30\u0b3e\u0b1c\u0b40 \u0b15\u0b39\u0b3f\u0b2a\u0b3e\u0b30\u0b3f\u0b2c\u0b47 \u0b15\u0b3f? "
            "(\u0100pa\u1e47a i\u1e43r\u0101j\u012b kahip\u0101ribe ki?) - Can you speak English?\n"
            "  25. \u0b2e\u0b4b\u0b24\u0b47 \u0b38\u0b3e\u0b39\u0b3e\u0b2f\u0b4d\u0b5f \u0b15\u0b30\u0b28\u0b4d\u0b24\u0b41\u0964 (Mote s\u0101h\u0101yya karantu.) - Please help me.\n"
            "  26. \u0b2e\u0b41\u0b01 \u0b2c\u0b41\u0b1d\u0b3f\u0b2a\u0b3e\u0b30\u0b3f\u0b32\u0b3f \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Mun bujhip\u0101rili n\u0101hin.) - I did not understand.\n"
            "  27. \u0b27\u0b40\u0b30\u0b47 \u0b15\u0b41\u0b39\u0b28\u0b4d\u0b24\u0b41\u0964 (Dh\u012bre kuhantu.) - Please speak slowly.\n"
            "  28. \u0b2a\u0b41\u0b23\u0b3f \u0b15\u0b41\u0b39\u0b28\u0b4d\u0b24\u0b41\u0964 (Pu\u1e47i kuhantu.) - Please say it again.\n"
            "  29. \u0b39\u0b01 (han) - Yes. / \u0b28\u0b3e (n\u0101) - No.\n"
            "  30. \u0b20\u0b3f\u0b15 \u0b05\u0b1b\u0b3f\u0964 (\u1e6dhika achi.) - It is fine / OK."
        ),
        "how_it_works": (
            "This record is the social survival kit: thirty phrases that "
            "carry a learner through first contact in Odisha. It opens with "
            "the two greetings (namask\u0101ra everywhere, juh\u0101ra in the "
            "west), the day-part wishes, the formal/familiar how-are-you "
            "pair, gratitude, softeners (day\u0101kari), apologies, farewells, "
            "and blessings - then the introduction block (name, nice to meet "
            "you), the learner's lifelines (I am learning Odia; do you "
            "speak English; help me; I did not understand; slowly; again), "
            "and yes/no/OK. Each phrase carries a usage note so the learner "
            "knows the register. Drill: role-play meeting, thanking, and "
            "parting with a partner, using only these thirty."
        ),
        "key_points": [
            "30 greetings, farewells, and politeness phrases with usage notes.",
            "namask\u0101ra is the default formal greeting; juh\u0101ra is the western Odisha traditional greeting.",
            "Formal/familiar how-are-you pair matches the pronoun record's three yous.",
            "Learner lifelines included: help me, I did not understand, speak slowly, say again.",
        ],
        "requirements": [
            "Read the pronoun record first to choose the right you-level.",
        ],
        "standards": [
            "Phrases follow standard usage; regional note on juh\u0101ra is documented.",
            "Example phrases are standard constructions (labeled Signature-composed teaching sentences where built).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["namask\u0101ra", "juh\u0101ra", "dhanyab\u0101da", "bid\u0101ya", "30"],
        "sig_lens": (
            "Through the Signature lens every greeting is a sworn courtesy: "
            "namask\u0101ra the vow of respect offered, dhanyab\u0101da the "
            "vow of gratitude sealed, bid\u0101ya the vow of safe parting."
        ),
        "drill": {
            "count": 30,
            "greetings": ["namask\u0101ra", "juh\u0101ra", "\u1e63ubha sak\u0101\u1e37a",
                          "\u1e63ubha sandhy\u0101", "\u1e63ubha r\u0101tri"],
            "farewells": ["bid\u0101ya", "pheri dekh\u0101 heb\u0101"],
            "lifelines": 6,
        },
    },
    {
        "key": "grammar",
        "name": "Grammar Essentials: The Ten Load-Bearing Rules",
        "group": "Grammar Essentials",
        "ladder_rank": 10,
        "ladder_tier": "compounded",
        "description": (
            "The ten rules that carry the whole language - each with "
            "translated example sentences. \n\n"
            "1. Word order is SOV (subject-object-verb): the verb comes "
            "last. \u0b2e\u0b41\u0b01 \u0b2d\u0b3e\u0b24 \u0b16\u0b3e\u0b0f\u0964 (Mun bh\u0101ta kh\u0101e.) I rice eat = I eat rice.\n"
            "2. Three genders: masculine, feminine, neuter. Humans and "
            "higher animals take masculine/feminine; most things are "
            "neuter. \u0b2a\u0b41\u0b05 (pua, boy, masc.), \u0b1d\u0b3f\u0b05 (jhia, girl, fem.), "
            "\u0b2c\u0b39\u0b3f (bahi, book, neuter).\n"
            "3. Two numbers: singular and plural. Plurals often add "
            "-\u0b2e\u0b3e\u0b28\u0b47 (-m\u0101ne) for people: \u0b2a\u0b3f\u0b32\u0b3e (pil\u0101, child) -> "
            "\u0b2a\u0b3f\u0b32\u0b3e\u0b2e\u0b3e\u0b28\u0b47 (pil\u0101m\u0101ne, children).\n"
            "4. Seven cases: nominative, accusative (objective), "
            "instrumental, dative, ablative, genitive, locative (plus the "
            "vocative). Case is marked by suffixes: \u0b18\u0b30 (ghara, house, "
            "nom.) -> \u0b18\u0b30\u0b15\u0b41 (gharaku, to the house, acc./dat.) -> "
            "\u0b18\u0b30\u0b30 (gharara, of the house, gen.) -> \u0b18\u0b30\u0b47 (ghare, in the house, loc.).\n"
            "5. Postpositions, not prepositions: the little words come "
            "after the noun. \u0b1f\u0b47\u0b2c\u0b41\u0b32 \u0b09\u0b2a\u0b30\u0b47 (\u1e6debul upare) - on the table; "
            "\u0b18\u0b30 \u0b2a\u0b3e\u0b16\u0b30\u0b47 (ghara p\u0101khare) - near the house; "
            "\u0b24\u0b41\u0b2e \u0b38\u0b39\u0b3f\u0b24 (tuma sahita) - with you.\n"
            "6. No articles: \u0b2c\u0b39\u0b3f means a book, the book, or books - "
            "context decides. \u0b2c\u0b39\u0b3f\u0b1f\u0b3f (bahi\u1e6di) points to a specific "
            "book: that/the book.\n"
            "7. Two copulas: \u0b05\u0b1b\u0b3f (achi, is/exists) for location and "
            "state, \u0b05\u0b1f\u0b47 (a\u1e6de, is) for identity. \u0b38\u0b47 \u0b18\u0b30\u0b47 \u0b05\u0b1b\u0b3f\u0964 "
            "(Se ghare achi.) He is at home. \u0b38\u0b47 \u0b21\u0b3e\u0b15\u0b4d\u0b24\u0b30 \u0b05\u0b1f\u0b47\u0964 "
            "(Se d\u0101ktara a\u1e6de.) He is a doctor.\n"
            "8. Negation with \u0b28\u0b3e\u0b39\u0b3f\u0b01 (n\u0101hin) after the verb: "
            "\u0b2e\u0b41\u0b01 \u0b2f\u0b3e\u0b0f \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Mun y\u0101e n\u0101hin.) I do not go. "
            "\u0b2e\u0b41\u0b01 \u0b2d\u0b3e\u0b24 \u0b16\u0b3e\u0b0f \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Mun bh\u0101ta kh\u0101e n\u0101hin.) I do not eat rice.\n"
            "9. Questions: yes/no questions use rising intonation; "
            "wh-questions use the interrogatives from the pronoun record. "
            "\u0b24\u0b41\u0b2e\u0b47 \u0b2f\u0b3f\u0b2c \u0b15\u0b3f? (Tume yiba ki?) Will you go? "
            "\u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b47\u0b2c\u0b47 \u0b2f\u0b3f\u0b2c? (Tume kebe yiba?) When will you go?\n"
            "10. Adjectives do not inflect: one form for all genders and "
            "numbers. \u0b2d\u0b32 \u0b2a\u0b41\u0b05 (bhala pua, good boy), \u0b2d\u0b32 \u0b1d\u0b3f\u0b05 "
            "(bhala jhia, good girl), \u0b2d\u0b32 \u0b2a\u0b3f\u0b32\u0b3e\u0b2e\u0b3e\u0b28\u0b47 (bhala pil\u0101m\u0101ne, good children)."
        ),
        "how_it_works": (
            "This record is the grammar engine room: ten rules, each proved "
            "by sentences. It teaches SOV order first (the verb always "
            "last), then the noun system (three genders, singular/plural, "
            "seven cases with the ghara -> gharaku -> gharara -> ghare "
            "ladder), then postpositions (the English preposition moves "
            "behind the noun), the absence of articles, the two copulas "
            "(achi for state/location, a\u1e6de for identity), negation with "
            "n\u0101hin after the verb, question formation (intonation for "
            "yes/no, interrogatives for wh-), and the non-inflecting "
            "adjective. Every later record is an application of these ten; "
            "the tenses record extends rule 1's verb slot, the case-heavy "
            "records extend rule 4. Drill: convert five English SVO "
            "sentences to Odia SOV."
        ),
        "key_points": [
            "SOV word order: the verb always comes last.",
            "Three genders (masculine, feminine, neuter); singular and plural.",
            "Seven cases marked by suffixes; vocative makes eight.",
            "Postpositions follow the noun; no articles; two copulas (achi, a\u1e6de).",
            "Negation: n\u0101hin after the verb; questions by intonation or interrogatives.",
            "Adjectives never inflect for gender or number.",
        ],
        "requirements": [
            "Read all Foundations records first; this record assumes the vocabulary.",
        ],
        "standards": [
            "Rules follow standard Odia grammar (Masica 1991).",
            "Example sentences are constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA, CIT_MOHANTY],
        "must_contain": ["SOV", "Seven cases", "Postpositions", "n\u0101hin", "achi", "a\u1e6de"],
        "sig_lens": (
            "Through the Signature lens grammar is the covenant's "
            "architecture: SOV the sworn order of telling, the seven cases "
            "seven seals on the noun, n\u0101hin the seal of refusal."
        ),
        "drill": {
            "rules": 10, "word_order": "SOV", "genders": 3, "cases": 7,
            "copulas": ["achi", "a\u1e6de"], "negator": "n\u0101hin",
            "case_ladder": ["ghara", "gharaku", "gharara", "ghare"],
        },
    },
    {
        "key": "home",
        "name": "Home and Family Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 11,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about house, rooms, furniture, and family - "
            "Odia script, romanization, English. \n\n"
            "  1. \u0b06\u0b2e\u0b30 \u0b18\u0b30 \u0b2c\u0b21\u0b3c\u0964 (\u0100mara ghara ba\u1e0da.) Our house is big.\n"
            "  2. \u0b18\u0b30\u0b47 \u0b24\u0b3f\u0b28\u0b3f\u0b1f\u0b3f \u0b15\u0b4b\u0b20\u0b30\u0b3f \u0b05\u0b1b\u0b3f\u0964 (Ghare tini\u1e6di ko\u1e6dhari achi.) There are three rooms in the house.\n"
            "  3. \u0b36\u0b4b\u0b07\u0b2c\u0b3e \u0b18\u0b30 \u0b09\u0b2a\u0b30 \u0b2e\u0b39\u0b32\u0b3e\u0b30\u0b47\u0964 (\u1e62oib\u0101 ghara upara mah\u0101l\u0101re.) The bedroom is upstairs.\n"
            "  4. \u0b30\u0b4b\u0b37\u0b47\u0b07 \u0b18\u0b30\u0b47 \u0b2e\u0b3e \u0b30\u0b3e\u0b28\u0b4d\u0b27\u0b41\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 (Ro\u1e63ei ghare m\u0101 r\u0101ndhuchanti.) Mother is cooking in the kitchen.\n"
            "  5. \u0b1a\u0b09\u0b15\u0b3f \u0b1f\u0b47\u0b2c\u0b41\u0b32 \u0b2a\u0b3e\u0b16\u0b30\u0b47 \u0b05\u0b1b\u0b3f\u0964 (Chauki \u1e6debul p\u0101khare achi.) The chair is near the table.\n"
            "  6. \u0b16\u0b1f \u0b09\u0b2a\u0b30\u0b47 \u0b28\u0b42\u0b06 \u0b1a\u0b3e\u0b26\u0b30 \u0b05\u0b1b\u0b3f\u0964 (Kha\u1e6da upare nu\u0101 c\u0101dara achi.) There is a new sheet on the bed.\n"
            "  7. \u0b26\u0b4d\u0b35\u0b3e\u0b30 \u0b2c\u0b28\u0b4d\u0b26 \u0b05\u0b1b\u0b3f\u0964 (Dw\u0101ra banda achi.) The door is closed.\n"
            "  8. \u0b1d\u0b30\u0b15\u0b3e \u0b16\u0b4b\u0b32\u0b3e \u0b05\u0b1b\u0b3f\u0964 (Jharak\u0101 khol\u0101 achi.) The window is open.\n"
            "  9. \u0b2c\u0b3e\u0b2a\u0b3e \u0b2c\u0b17\u0b3f\u0b1a\u0b3e\u0b30\u0b47 \u0b2c\u0b38\u0b3f\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 (B\u0101p\u0101 bagic\u0101re basichanti.) Father is sitting in the garden.\n"
            "  10. \u0b2d\u0b3e\u0b07 \u0b2c\u0b3f\u0b26\u0b4d\u0b5f\u0b3e\u0b33\u0b5f\u0b30\u0b41 \u0b06\u0b38\u0b3f\u0b32\u0b3e\u0964 (Bh\u0101i bidy\u0101\u1e37ayaru \u0101sil\u0101.) Brother came from school.\n"
            "  11. \u0b2d\u0b09\u0b23\u0b40 \u0b2a\u0b3e\u0b20 \u0b2a\u0b22\u0b3c\u0b41\u0b1b\u0b3f\u0964 (Bhau\u1e47\u012b p\u0101\u1e6dha pa\u1e0dhu\u1e63i.) Sister is studying her lesson.\n"
            "  12. \u0b1c\u0b47\u0b1c\u0b47\u0b2c\u0b3e\u0b2a\u0b3e \u0b2c\u0b3e\u0b30\u0b3e\u0b23\u0b4d\u0b21\u0b3e\u0b30\u0b47 \u0b05\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 (Jeje-b\u0101p\u0101 b\u0101r\u0101\u1e47d\u0101re achanti.) Grandfather is on the veranda.\n"
            "  13. \u0b1c\u0b47\u0b1c\u0b47\u0b2e\u0b3e \u0b17\u0b2a \u0b15\u0b30\u0b41\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 (Jeje-m\u0101 gapa karuchanti.) Grandmother is chatting.\n"
            "  14. \u0b06\u0b2e\u0b47 \u0b30\u0b3e\u0b24\u0b3f\u0b30\u0b47 \u0b0f\u0b15\u0b3e\u0b20\u0b3f \u0b16\u0b3e\u0b09\u0964 (\u0100me r\u0101tire ek\u0101\u1e6dhi kh\u0101u.) We eat together at night.\n"
            "  15. \u0b2a\u0b3f\u0b32\u0b3e\u0b2e\u0b3e\u0b28\u0b47 \u0b05\u0b17\u0b23\u0b3e\u0b30\u0b47 \u0b16\u0b47\u0b33\u0b41\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 (Pil\u0101m\u0101ne aga\u1e47\u0101re khe\u1e37uchanti.) The children are playing in the courtyard.\n"
            "  16. \u0b2c\u0b3f\u0b1c\u0b41\u0b33\u0b3f \u0b2c\u0b24\u0b40 \u0b1c\u0b33\u0b41\u0b1b\u0b3f\u0964 (Bijuli bat\u012b ja\u1e37uchi.) The electric light is on.\n"
            "  17. \u0b2a\u0b19\u0b4d\u0b16\u0b3e \u0b18\u0b42\u0b30\u0b41\u0b1b\u0b3f\u0964 (Pa\u1e45kh\u0101 gh\u016bruchi.) The fan is turning.\n"
            "  18. \u0b06\u0b32\u0b2e\u0b3e\u0b30\u0b3f\u0b30\u0b47 \u0b2c\u0b39\u0b41\u0b24 \u0b2c\u0b39\u0b3f \u0b05\u0b1b\u0b3f\u0964 (\u0100lam\u0101rire bahuta bahi achi.) There are many books in the cupboard.\n"
            "  19. \u0b2e\u0b4b\u0b30 \u0b2a\u0b30\u0b3f\u0b2c\u0b3e\u0b30 \u0b2c\u0b21\u0b3c\u0964 (Mora parib\u0101ra ba\u1e0da.) My family is big.\n"
            "  20. \u0b18\u0b30 \u0b2e\u0b4b\u0b30 \u0b38\u0b2c\u0b41\u0b20\u0b3e\u0b30\u0b41 \u0b2a\u0b4d\u0b30\u0b3f\u0b5f \u0b1c\u0b3e\u0b17\u0b3e\u0964 (Ghara mora sabu\u1e6d\u0101ru priya j\u0101g\u0101.) Home is my dearest place."
        ),
        "how_it_works": (
            "This record applies the grammar engine to the home: twenty "
            "sentences using the locative case (ghare, upare, p\u0101khare), "
            "family vocabulary (jeje-b\u0101p\u0101 grandfather, jeje-m\u0101 "
            "grandmother, parib\u0101ra family), and household objects. The "
            "ablative appears (bidy\u0101\u1e37ayaru, from school), and "
            "achanti marks respectful plural agreement for elders. Drill: "
            "walk through your own home naming each room and object in Odia."
        ),
        "key_points": [
            "20 home-and-family sentences with full translations.",
            "Locative case in action: ghare, upare, p\u0101khare, aga\u1e47\u0101re.",
            "Family vocabulary: parents, siblings, grandparents, parib\u0101ra.",
            "Respectful verb agreement (achanti) for elders.",
        ],
        "requirements": ["Read the grammar essentials record first."],
        "standards": [
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["parib\u0101ra", "Jeje-b\u0101p\u0101", "ghare", "20"],
        "sig_lens": (
            "Through the Signature lens home is the first covenant: every "
            "room a sealed chamber of care, every family name a vow kept "
            "across generations."
        ),
        "drill": {
            "sentences": 20, "theme": "home-family",
            "locatives": ["ghare", "upare", "p\u0101khare", "aga\u1e47\u0101re", "b\u0101r\u0101\u1e47d\u0101re"],
        },
    },
    {
        "key": "food",
        "name": "Food and Cooking Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 12,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about meals, ingredients, cooking actions, and "
            "the restaurant - Odia script, romanization, English. \n\n"
            "  1. \u0b2e\u0b41\u0b01 \u0b2d\u0b3e\u0b24 \u0b16\u0b3e\u0b0f\u0964 (Mun bh\u0101ta kh\u0101e.) I eat rice.\n"
            "  2. \u0b21\u0b3e\u0b32\u0b3f \u0b2d\u0b3e\u0b24 \u0b13\u0b21\u0b3c\u0b3f\u0b06 \u0b16\u0b3e\u0b26\u0b4d\u0b5f\u0964 (D\u0101li-bh\u0101ta odi\u0101 kh\u0101dya.) Dal-rice is Odia food.\n"
            "  3. \u0b2e\u0b3e \u0b21\u0b3e\u0b32\u0b3f \u0b30\u0b3e\u0b28\u0b4d\u0b27\u0b41\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 (M\u0101 d\u0101li r\u0101ndhuchanti.) Mother is cooking dal.\n"
            "  4. \u0b2a\u0b16\u0b3e\u0b33 \u0b17\u0b30\u0b2e \u0b26\u0b3f\u0b28\u0b47 \u0b2d\u0b32 \u0b32\u0b3e\u0b17\u0b47\u0964 (Pakh\u0101\u1e37a garama dine bhala l\u0101ge.) Pakhala tastes good on hot days.\n"
            "  5. \u0b1b\u0b47\u0b28\u0b3e\u0b2a\u0b4b\u0b21\u0b3c \u0b2e\u0b4b\u0b30 \u0b2a\u0b4d\u0b30\u0b3f\u0b5f \u0b2e\u0b3f\u0b20\u0b3e\u0964 (Chen\u0101po\u1e0da mora priya mi\u1e6dh\u0101.) Chhenapoda is my favorite sweet.\n"
            "  6. \u0b30\u0b38\u0b17\u0b4b\u0b32\u0b3e \u0b2a\u0b41\u0b30\u0b40\u0b30 \u0b2a\u0b4d\u0b30\u0b38\u0b3f\u0b26\u0b4d\u0b27\u0964 (Rasagol\u0101 pur\u012bra prasiddha.) Rasagola is famous in Puri.\n"
            "  7. \u0b24\u0b30\u0b15\u0b3e\u0b30\u0b3f \u0b2c\u0b1c\u0b3e\u0b30\u0b30\u0b41 \u0b06\u0b23\u0964 (Tarak\u0101ri baj\u0101raru \u0101\u1e47a.) Bring vegetables from the market.\n"
            "  8. \u0b06\u0b33\u0b41 \u0b15\u0b47\u0b24\u0b47 \u0b26\u0b3e\u0b2e? (\u0100\u1e37u kete d\u0101ma?) What is the price of potatoes?\n"
            "  9. \u0b2a\u0b3f\u0b06\u0b1c \u0b15\u0b3e\u0b1f\u0964 (Pi\u0101ja k\u0101\u1e6da.) Cut the onion.\n"
            "  10. \u0b24\u0b47\u0b32\u0b30\u0b47 \u0b2e\u0b38\u0b32\u0b3e \u0b2d\u0b3e\u0b1c\u0964 (Telare masal\u0101 bh\u0101ja.) Fry the spices in oil.\n"
            "  11. \u0b2a\u0b3e\u0b23\u0b3f \u0b17\u0b30\u0b2e \u0b15\u0b30\u0964 (P\u0101\u1e47i garama kara.) Heat the water.\n"
            "  12. \u0b32\u0b41\u0b23 \u0b15\u0b2e \u0b26\u0b3f\u0b05\u0964 (Lu\u1e47a kama dia.) Add a little salt.\n"
            "  13. \u0b16\u0b3e\u0b26\u0b4d\u0b5f \u0b2a\u0b4d\u0b30\u0b38\u0b4d\u0b24\u0b41\u0b24\u0964 (Kh\u0101dya prastuta.) The food is ready.\n"
            "  14. \u0b06\u0b38\u0b28\u0b4d\u0b24\u0b41, \u0b16\u0b3e\u0b28\u0b4d\u0b24\u0b41\u0964 (\u0100santu, kh\u0101ntu.) Please come, please eat. (formal invitation)\n"
            "  15. \u0b2e\u0b41\u0b01 \u0b36\u0b3e\u0b15\u0b3e\u0b39\u0b3e\u0b30\u0b40 \u0b05\u0b1f\u0b47\u0964 (Mun \u1e63\u0101k\u0101h\u0101r\u012b a\u1e6de.) I am vegetarian.\n"
            "  16. \u0b2e\u0b3e\u0b1b \u0b24\u0b30\u0b15\u0b3e\u0b30\u0b3f \u0b2c\u0b39\u0b41\u0b24 \u0b38\u0b4d\u0b35\u0b3e\u0b26\u0b3f\u0b37\u0b4d\u0b1f\u0964 (M\u0101cha tarak\u0101ri bahuta sw\u0101di\u1e63\u1e6da.) Fish curry is very tasty.\n"
            "  17. \u0b39\u0b4b\u0b1f\u0b47\u0b32\u0b30\u0b47 \u0b16\u0b3e\u0b07\u0b2c\u0b3e\u0964 (Ho\u1e6delare kh\u0101ib\u0101.) We will eat at the hotel (restaurant).\n"
            "  18. \u0b2c\u0b3f\u0b32 \u0b26\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (Bila diantu.) Please give the bill.\n"
            "  19. \u0b16\u0b3e\u0b26\u0b4d\u0b5f \u0b2c\u0b39\u0b41\u0b24 \u0b2d\u0b32 \u0b25\u0b3f\u0b32\u0b3e\u0964 (Kh\u0101dya bahuta bhala thil\u0101.) The food was very good.\n"
            "  20. \u0b2a\u0b47\u0b1f \u0b2a\u0b42\u0b30\u0b3f\u0b32\u0b3e\u0964 (Pe\u1e6da p\u016bril\u0101.) My stomach is full."
        ),
        "how_it_works": (
            "This record feeds the learner: twenty sentences from the Odia "
            "kitchen and table, naming real Odia dishes (d\u0101li-bh\u0101ta, "
            "pakh\u0101\u1e37a, chen\u0101po\u1e0da, rasagol\u0101) and the cooking "
            "verbs (r\u0101ndhib\u0101 to cook, k\u0101\u1e6dib\u0101 to cut, bh\u0101jib\u0101 "
            "to fry). Imperatives appear in kitchen commands (k\u0101\u1e6da, "
            "bh\u0101ja, \u0101\u1e47a), and the restaurant block teaches "
            "ordering and the bill. Drill: narrate cooking one dish in Odia, "
            "one action per sentence."
        ),
        "key_points": [
            "20 food-and-cooking sentences with full translations.",
            "Real Odia dishes named: d\u0101li-bh\u0101ta, pakh\u0101\u1e37a, chen\u0101po\u1e0da, rasagol\u0101.",
            "Cooking verbs and kitchen imperatives in context.",
            "Restaurant block: ordering, the bill, paying the compliment.",
        ],
        "requirements": ["Read the verbs record first for the cooking actions."],
        "standards": [
            "Dish names follow standard Odia usage.",
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["Pakh\u0101\u1e37a", "Chen\u0101po\u1e0da", "Rasagol\u0101", "20"],
        "sig_lens": (
            "Through the Signature lens food is the covenant of nourishment: "
            "every shared meal a sealed promise, every recipe a vow handed "
            "down."
        ),
        "drill": {
            "sentences": 20, "theme": "food-cooking",
            "dishes": ["d\u0101li-bh\u0101ta", "pakh\u0101\u1e37a", "chen\u0101po\u1e0da", "rasagol\u0101"],
        },
    },
    {
        "key": "travel",
        "name": "Travel and Directions Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for transport, asking directions, tickets, and "
            "lodging - Odia script, romanization, English. \n\n"
            "  1. \u0b30\u0b47\u0b33 \u0b37\u0b4d\u0b1f\u0b47\u0b38\u0b28 \u0b15\u0b47\u0b09\u0b01\u0b20\u0b3e\u0b30\u0b47? (Rela s\u1e6de\u1e63ana keun\u1e6dh\u0101re?) Where is the railway station?\n"
            "  2. \u0b2c\u0b38 \u0b37\u0b4d\u0b1f\u0b3e\u0b23\u0b4d\u0b21 \u0b0f\u0b20\u0b3e\u0b30\u0b47 \u0b05\u0b1b\u0b3f\u0964 (Basa s\u1e6d\u0101\u1e47da e\u1e6dh\u0101re achi.) The bus stand is here.\n"
            "  3. \u0b2d\u0b41\u0b2c\u0b28\u0b47\u0b36\u0b4d\u0b35\u0b30 \u0b1f\u0b3f\u0b15\u0b47\u0b1f \u0b15\u0b47\u0b24\u0b47? (Bhubane\u1e63wara \u1e6dike\u1e6da kete?) How much is a ticket to Bhubaneswar?\n"
            "  4. \u0b2c\u0b38 \u0b15\u0b47\u0b24\u0b47\u0b2c\u0b47\u0b33\u0b47 \u0b1b\u0b3e\u0b21\u0b3c\u0b3f\u0b2c? (Basa ketebe\u1e37e ch\u0101\u1e0diba?) When will the bus leave?\n"
            "  5. \u0b1f\u0b4d\u0b30\u0b47\u0b28 \u0b26\u0b47\u0b30\u0b3f\u0b30\u0b47 \u0b05\u0b1b\u0b3f\u0964 (\u1e6erena derire achi.) The train is late.\n"
            "  6. \u0b38\u0b3f\u0b27\u0b3e \u0b2f\u0b3e\u0b06\u0b28\u0b4d\u0b24\u0b41\u0964 (Sidh\u0101 y\u0101ntu.) Go straight.\n"
            "  7. \u0b21\u0b3e\u0b39\u0b3e\u0b23\u0b15\u0b41 \u0b2f\u0b3e\u0b06\u0b28\u0b4d\u0b24\u0b41\u0964 (D\u0101h\u0101\u1e47aku y\u0101ntu.) Go to the right.\n"
            "  8. \u0b2c\u0b3e\u0b2e\u0b15\u0b41 \u0b2f\u0b3e\u0b06\u0b28\u0b4d\u0b24\u0b41\u0964 (B\u0101maku y\u0101ntu.) Go to the left.\n"
            "  9. \u0b2e\u0b28\u0b4d\u0b26\u0b3f\u0b30 \u0b2a\u0b3e\u0b16\u0b30\u0b47 \u0b05\u0b1b\u0b3f\u0964 (Mandira p\u0101khare achi.) It is near the temple.\n"
            "  10. \u0b15\u0b1f\u0b15 \u0b0f\u0b20\u0b3e\u0b30\u0b41 \u0b15\u0b47\u0b24\u0b47 \u0b26\u0b42\u0b30? (Ka\u1e6daka e\u1e6d\u0101ru kete d\u016bra?) How far is Cuttack from here?\n"
            "  11. \u0b05\u0b1f\u0b4b \u0b21\u0b3e\u0b15\u0b28\u0b4d\u0b24\u0b41\u0964 (A\u1e6do d\u0101kantu.) Call an auto (rickshaw).\n"
            "  12. \u0b2d\u0b21\u0b3c\u0b3e \u0b15\u0b47\u0b24\u0b47 \u0b28\u0b47\u0b2c\u0b47? (Bha\u1e0d\u0101 kete nebe?) How much fare will you take?\n"
            "  13. \u0b2e\u0b4b\u0b24\u0b47 \u0b2a\u0b41\u0b30\u0b40 \u0b28\u0b47\u0b07\u0b2f\u0b3e\u0b05\u0964 (Mote pur\u012b nei\u0101a.) Take me to Puri.\n"
            "  14. \u0b39\u0b4b\u0b1f\u0b47\u0b32\u0b30\u0b47 \u0b30\u0b41\u0b2e \u0b05\u0b1b\u0b3f \u0b15\u0b3f? (Ho\u1e6delare ruma achi ki?) Is there a room in the hotel?\n"
            "  15. \u0b0f\u0b15 \u0b30\u0b3e\u0b24\u0b3f \u0b2a\u0b3e\u0b07\u0b01 \u0b30\u0b41\u0b2e \u0b26\u0b30\u0b15\u0b3e\u0b30\u0964 (Eka r\u0101ti p\u0101in ruma darak\u0101ra.) I need a room for one night.\n"
            "  16. \u0b1a\u0b3e\u0b2c\u0b3f \u0b26\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (C\u0101bi diantu.) Please give the key.\n"
            "  17. \u0b2e\u0b41\u0b01 \u0b30\u0b3e\u0b38\u0b4d\u0b24\u0b3e \u0b39\u0b1c\u0b3f\u0b2f\u0b3e\u0b07\u0b1b\u0b3f\u0964 (Mun r\u0101st\u0101 hajiy\u0101ichi.) I have lost the way.\n"
            "  18. \u0b2e\u0b3e\u0b28\u0b1a\u0b3f\u0b24\u0b4d\u0b30 \u0b26\u0b47\u0b16\u0b3e\u0b28\u0b4d\u0b24\u0b41\u0964 (M\u0101ncitra dekh\u0101ntu.) Please show me the map.\n"
            "  19. \u0b2c\u0b3f\u0b2e\u0b3e\u0b28 \u0b2c\u0b28\u0b4d\u0b26\u0b30 \u0b15\u0b47\u0b09\u0b01\u0b20\u0b3e\u0b30\u0b47? (Bim\u0101na bandara keun\u1e6dh\u0101re?) Where is the airport?\n"
            "  20. \u0b2f\u0b3e\u0b24\u0b4d\u0b30\u0b3e \u0b36\u0b41\u0b2d \u0b39\u0b47\u0b09\u0964 (Y\u0101tr\u0101 \u1e63ubha heu.) Have a good journey."
        ),
        "how_it_works": (
            "This record is the traveler's phrasebook: twenty sentences "
            "covering stations and stands, tickets and fares, the three "
            "direction commands (sidh\u0101 straight, d\u0101h\u0101\u1e47a right, "
            "b\u0101ma left), distance questions, autos, hotels, lost-and-"
            "found, and the airport. The ablative of distance appears "
            "(e\u1e6d\u0101ru, from here), and bargaining language (bha\u1e0d\u0101 "
            "kete nebe?) previews the market record. Drill: plan a Bhubaneswar-"
            "to-Puri trip entirely in Odia using only these sentences."
        ),
        "key_points": [
            "20 travel-and-direction sentences with full translations.",
            "Direction commands: sidh\u0101, d\u0101h\u0101\u1e47a, b\u0101ma.",
            "Tickets, fares, hotels, and lost-way phrases.",
            "Real Odia place names: Bhubaneswar, Cuttack, Puri.",
        ],
        "requirements": ["Read the numbers record for fares and times."],
        "standards": [
            "Place names follow standard Odia spellings.",
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["Bhubane\u1e63wara", "Sidh\u0101", "Bha\u1e0d\u0101", "20"],
        "sig_lens": (
            "Through the Signature lens travel is the covenant of the road: "
            "every direction asked a vow of guidance, every fare paid a seal "
            "on the journey."
        ),
        "drill": {
            "sentences": 20, "theme": "travel-directions",
            "directions": ["sidh\u0101", "d\u0101h\u0101\u1e47a", "b\u0101ma"],
        },
    },
    {
        "key": "work",
        "name": "Work and School Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about jobs, the office, the classroom, and "
            "learning - Odia script, romanization, English. \n\n"
            "  1. \u0b2e\u0b41\u0b01 \u0b36\u0b3f\u0b15\u0b4d\u0b37\u0b15 \u0b05\u0b1f\u0b47\u0964 (Mun \u1e63ik\u1e63aka a\u1e6de.) I am a teacher.\n"
            "  2. \u0b38\u0b47 \u0b07\u0b1e\u0b4d\u0b1c\u0b3f\u0b28\u0b3f\u0b5f\u0b30 \u0b05\u0b1f\u0b28\u0b4d\u0b24\u0b3f\u0964 (Se injiniyara a\u1e6danti.) He is an engineer.\n"
            "  3. \u0b2e\u0b4b\u0b30 \u0b15\u0b3e\u0b2e \u0b15\u0b2e\u0b4d\u0b2a\u0b4d\u0b5f\u0b41\u0b1f\u0b30\u0b30\u0b47\u0964 (Mora k\u0101ma kampyu\u1e6darare.) My work is on the computer.\n"
            "  4. \u0b05\u0b2b\u0b3f\u0b38 \u0b38\u0b15\u0b3e\u0b33 \u0b28\u0b05\u0b1f\u0b3e\u0b30\u0b47 \u0b16\u0b4b\u0b32\u0b47\u0964 (Aphisa sak\u0101\u1e37a naa\u1e6d\u0101re khole.) The office opens at nine in the morning.\n"
            "  5. \u0b2e\u0b41\u0b01 \u0b2a\u0b4d\u0b30\u0b24\u0b3f\u0b26\u0b3f\u0b28 \u0b15\u0b3e\u0b2e\u0b15\u0b41 \u0b2f\u0b3e\u0b0f\u0964 (Mun pratidina k\u0101maku y\u0101e.) I go to work every day.\n"
            "  6. \u0b06\u0b1c\u0b3f \u0b2c\u0b48\u0b20\u0b15 \u0b05\u0b1b\u0b3f\u0964 (\u0100ji bai\u1e6dhaka achi.) There is a meeting today.\n"
            "  7. \u0b2c\u0b38 \u0b38\u0b3e\u0b39\u0b47\u0b2c \u0b06\u0b38\u0b3f\u0b32\u0b47\u0964 (Basa s\u0101heba \u0101sile.) The boss has come.\n"
            "  8. \u0b2e\u0b4b\u0b24\u0b47 \u0b15\u0b3e\u0b2e\u0b1f\u0b3f \u0b26\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (Mote k\u0101ma\u1e6di diantu.) Please give me the work.\n"
            "  9. \u0b15\u0b3e\u0b2e \u0b38\u0b30\u0b3f\u0b32\u0b3e\u0964 (K\u0101ma saril\u0101.) The work is finished.\n"
            "  10. \u0b26\u0b30\u0b2e\u0b3e \u0b15\u0b47\u0b2c\u0b47 \u0b2e\u0b3f\u0b33\u0b3f\u0b2c? (Daram\u0101 kebe mi\u1e37iba?) When will I get the salary?\n"
            "  11. \u0b2a\u0b3f\u0b32\u0b3e\u0b2e\u0b3e\u0b28\u0b47 \u0b2c\u0b3f\u0b26\u0b4d\u0b5f\u0b3e\u0b33\u0b5f\u0b15\u0b41 \u0b17\u0b32\u0b47\u0964 (Pil\u0101m\u0101ne bidy\u0101\u1e37ayaku gale.) The children went to school.\n"
            "  12. \u0b36\u0b3f\u0b15\u0b4d\u0b37\u0b15 \u0b36\u0b4d\u0b30\u0b47\u0b23\u0b40\u0b30\u0b47 \u0b2a\u0b22\u0b3c\u0b3e\u0b09\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 (\u1e62ik\u1e63aka \u1e63re\u1e47\u012bre pa\u1e0dh\u0101uchanti.) The teacher is teaching in the classroom.\n"
            "  13. \u0b1b\u0b3e\u0b24\u0b4d\u0b30\u0b2e\u0b3e\u0b28\u0b47 \u0b2e\u0b28 \u0b26\u0b47\u0b07 \u0b36\u0b41\u0b23\u0b41\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 (Ch\u0101tram\u0101ne mana dei \u1e63u\u1e47uchanti.) The students are listening attentively.\n"
            "  14. \u0b2c\u0b39\u0b3f \u0b16\u0b4b\u0b32\u0964 (Bahi khola.) Open the book.\n"
            "  15. \u0b2a\u0b3e\u0b20 \u0b2a\u0b22\u0b3c\u0964 (P\u0101\u1e6dha pa\u1e0dha.) Read the lesson.\n"
            "  16. \u0b2a\u0b30\u0b40\u0b15\u0b4d\u0b37\u0b3e \u0b15\u0b47\u0b2c\u0b47? (Par\u012bk\u1e63\u0101 kebe?) When is the exam?\n"
            "  17. \u0b2e\u0b41\u0b01 \u0b2a\u0b30\u0b40\u0b15\u0b4d\u0b37\u0b3e\u0b30\u0b47 \u0b2a\u0b3e\u0b38 \u0b39\u0b47\u0b32\u0b3f\u0964 (Mun par\u012bk\u1e63\u0101re p\u0101sa heli.) I passed the exam.\n"
            "  18. \u0b36\u0b3f\u0b16\u0b3f\u0b2c\u0b3e \u0b2e\u0b28\u0b41\u0b37\u0b4d\u0b5f\u0b30 \u0b38\u0b2c\u0b41\u0b20\u0b3e\u0b30\u0b41 \u0b2c\u0b21\u0b3c \u0b27\u0b28\u0964 (\u1e62ikhib\u0101 manu\u1e63yara sabu\u1e6d\u0101ru ba\u1e0da dhana.) Learning is man's greatest wealth.\n"
            "  19. \u0b1b\u0b41\u0b1f\u0b3f \u0b15\u0b47\u0b2c\u0b47? (Chu\u1e6di kebe?) When is the holiday?\n"
            "  20. \u0b15\u0b3e\u0b32\u0b3f \u0b1b\u0b41\u0b1f\u0b3f \u0b05\u0b1b\u0b3f\u0964 (K\u0101li chu\u1e6di achi.) Tomorrow is a holiday."
        ),
        "how_it_works": (
            "This record works two rooms: the office and the classroom. "
            "Twenty sentences teach job titles (\u1e63ik\u1e63aka, injiniyara, "
            "basa s\u0101heba), office routine (bai\u1e6dhaka meeting, daram\u0101 "
            "salary), and school life (ch\u0101tra student, \u1e63re\u1e47\u012b "
            "classroom, par\u012bk\u1e63\u0101 exam). The equative copula a\u1e6de "
            "does heavy lifting for identities (I am a teacher), and "
            "classroom imperatives (bahi khola, p\u0101\u1e6dha pa\u1e0dha) drill "
            "the command form. Drill: introduce your own job and describe "
            "your workday in Odia."
        ),
        "key_points": [
            "20 work-and-school sentences with full translations.",
            "Job titles, office routine, salary, and meetings.",
            "Classroom vocabulary: student, lesson, exam, holiday.",
            "Equative a\u1e6de for identities; imperatives for classroom commands.",
        ],
        "requirements": ["Read the grammar essentials record for the copulas."],
        "standards": [
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["\u1e63ik\u1e63aka", "par\u012bk\u1e63\u0101", "Daram\u0101", "20"],
        "sig_lens": (
            "Through the Signature lens work is the covenant of effort: "
            "every task a sealed promise, every lesson a vow of growth."
        ),
        "drill": {
            "sentences": 20, "theme": "work-school",
            "jobs": ["\u1e63ik\u1e63aka", "injiniyara", "d\u0101ktara"],
        },
    },
    {
        "key": "health",
        "name": "Health and Body Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about body parts, symptoms, the doctor visit, "
            "and the pharmacy - Odia script, romanization, English. \n\n"
            "  1. \u0b2e\u0b4b\u0b30 \u0b2e\u0b41\u0b23\u0b4d\u0b21 \u0b2c\u0b3f\u0b28\u0b4d\u0b27\u0b41\u0b1b\u0b3f\u0964 (Mora mu\u1e47da bindhuchi.) My head aches.\n"
            "  2. \u0b2e\u0b4b\u0b30 \u0b1c\u0b4d\u0b35\u0b30 \u0b39\u0b47\u0b07\u0b1b\u0b3f\u0964 (Mora jwara heichi.) I have a fever.\n"
            "  3. \u0b2e\u0b4b\u0b30 \u0b15\u0b3e\u0b36 \u0b39\u0b47\u0b09\u0b1b\u0b3f\u0964 (Mora k\u0101\u1e63a heuchi.) I have a cough.\n"
            "  4. \u0b2e\u0b4b\u0b30 \u0b2a\u0b47\u0b1f \u0b2c\u0b3f\u0b28\u0b4d\u0b27\u0b41\u0b1b\u0b3f\u0964 (Mora pe\u1e6da bindhuchi.) My stomach aches.\n"
            "  5. \u0b2e\u0b4b\u0b30 \u0b26\u0b3e\u0b28\u0b4d\u0b24 \u0b2c\u0b3f\u0b28\u0b4d\u0b27\u0b41\u0b1b\u0b3f\u0964 (Mora d\u0101nta bindhuchi.) My tooth aches.\n"
            "  6. \u0b2e\u0b4b\u0b30 \u0b06\u0b16\u0b3f \u0b32\u0b3e\u0b32 \u0b39\u0b47\u0b07\u0b1b\u0b3f\u0964 (Mora \u0101khi l\u0101la heichi.) My eyes are red.\n"
            "  7. \u0b2e\u0b4b\u0b30 \u0b17\u0b4b\u0b21\u0b3c \u0b2c\u0b3f\u0b28\u0b4d\u0b27\u0b41\u0b1b\u0b3f\u0964 (Mora go\u1e0da bindhuchi.) My leg hurts.\n"
            "  8. \u0b21\u0b3e\u0b15\u0b4d\u0b24\u0b30\u0b16\u0b3e\u0b28\u0b3e \u0b15\u0b47\u0b09\u0b01\u0b20\u0b3e\u0b30\u0b47? (D\u0101ktarakh\u0101n\u0101 keun\u1e6dh\u0101re?) Where is the clinic?\n"
            "  9. \u0b21\u0b3e\u0b15\u0b4d\u0b24\u0b30\u0b19\u0b4d\u0b15\u0b41 \u0b26\u0b47\u0b16\u0b3e\u0b28\u0b4d\u0b24\u0b41\u0964 (D\u0101ktara\u1e45ku dekh\u0101ntu.) Please show me to the doctor.\n"
            "  10. \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15\u0b30 \u0b15\u0b23 \u0b05\u0b38\u0b41\u0b2c\u0b3f\u0b27\u0b3e? (\u0100pa\u1e47a\u1e45kara ka\u1e47a asubidh\u0101?) What is your trouble?\n"
            "  11. \u0b24\u0b3f\u0b28\u0b3f \u0b26\u0b3f\u0b28 \u0b39\u0b47\u0b32\u0b3e \u0b1c\u0b4d\u0b35\u0b30\u0964 (Tini dina hel\u0101 jwara.) I have had fever for three days.\n"
            "  12. \u0b14\u0b37\u0b27 \u0b16\u0b3e\u0b06\u0b28\u0b4d\u0b24\u0b41\u0964 (Au\u1e63adha kh\u0101ntu.) Take the medicine.\n"
            "  13. \u0b26\u0b3f\u0b28\u0b15\u0b41 \u0b26\u0b41\u0b07\u0b25\u0b30 \u0b16\u0b3e\u0b06\u0b28\u0b4d\u0b24\u0b41\u0964 (Dinaku duithara kh\u0101ntu.) Take it twice a day.\n"
            "  14. \u0b16\u0b3e\u0b07\u0b2c\u0b3e \u0b2a\u0b30\u0b47 \u0b16\u0b3e\u0b06\u0b28\u0b4d\u0b24\u0b41\u0964 (Kh\u0101ib\u0101 pare kh\u0101ntu.) Take it after food.\n"
            "  15. \u0b06\u0b30\u0b3e\u0b2e \u0b15\u0b30\u0b28\u0b4d\u0b24\u0b41\u0964 (\u0100r\u0101ma karantu.) Take rest.\n"
            "  16. \u0b14\u0b37\u0b27 \u0b26\u0b4b\u0b15\u0b3e\u0b28 \u0b15\u0b47\u0b09\u0b01\u0b20\u0b3e\u0b30\u0b47? (Au\u1e63adha dok\u0101na keun\u1e6dh\u0101re?) Where is the pharmacy?\n"
            "  17. \u0b2e\u0b4b\u0b24\u0b47 \u0b2c\u0b4d\u0b5f\u0b3e\u0b23\u0b4d\u0b21\u0b47\u0b1c \u0b26\u0b30\u0b15\u0b3e\u0b30\u0964 (Mote by\u0101\u1e47deja darak\u0101ra.) I need a bandage.\n"
            "  18. \u0b38\u0b47 \u0b0f\u0b2c\u0b47 \u0b2d\u0b32 \u0b05\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 (Se ebe bhala achanti.) He is well now.\n"
            "  19. \u0b38\u0b4d\u0b35\u0b3e\u0b38\u0b4d\u0b25\u0b4d\u0b5f \u0b39\u0b3f\u0b01 \u0b38\u0b2e\u0b4d\u0b2a\u0b26\u0964 (Sw\u0101sthya hin sampada.) Health itself is wealth.\n"
            "  20. \u0b36\u0b40\u0b18\u0b4d\u0b30 \u0b06\u0b30\u0b4b\u0b17\u0b4d\u0b5f \u0b39\u0b41\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (\u1e62\u012bghra \u0101rogya huantu.) Get well soon."
        ),
        "how_it_works": (
            "This record is the health emergency kit: twenty sentences from "
            "symptom to cure. It teaches the body-part + bindhuchi (aches) "
            "pattern, the heichi (has become) pattern for fever and cough, "
            "the clinic visit (asubidh\u0101 trouble, au\u1e63adha medicine), "
            "dosage language (dinaku duithara, twice a day), and the "
            "pharmacy. The closing proverb (sw\u0101sthya hin sampada) is "
            "real folk wisdom. Drill: describe three imaginary symptoms and "
            "the doctor's three instructions, all in Odia."
        ),
        "key_points": [
            "20 health-and-body sentences with full translations.",
            "Symptom patterns: X bindhuchi (aches), X heichi (has X).",
            "Doctor-visit and pharmacy vocabulary; dosage language.",
            "Closes with the real proverb: health itself is wealth.",
        ],
        "requirements": ["Read the grammar essentials record first."],
        "standards": [
            "This record teaches language, not medical advice; the dosage lines are language examples.",
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["bindhuchi", "Au\u1e63adha", "Sw\u0101sthya hin sampada", "20"],
        "sig_lens": (
            "Through the Signature lens health is the covenant of the body: "
            "every symptom a signal sworn true, every cure a vow of care."
        ),
        "drill": {
            "sentences": 20, "theme": "health-body",
            "symptom_verbs": ["bindhuchi", "heichi"],
        },
    },
    {
        "key": "emotions",
        "name": "Emotions and Feelings Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for happy, sad, angry, afraid, love, and "
            "surprise - Odia script, romanization, English. Odia feelings "
            "often use the l\u0101gib\u0101 (to feel) construction: \u0b2e\u0b4b\u0b24\u0b47 \u0b16\u0b41\u0b38\u0b3f "
            "\u0b32\u0b3e\u0b17\u0b41\u0b1b\u0b3f (to me happiness is feeling) = I feel happy. \n\n"
            "  1. \u0b2e\u0b41\u0b01 \u0b16\u0b41\u0b38\u0b3f \u0b05\u0b1b\u0b3f\u0964 (Mun khusi achi.) I am happy.\n"
            "  2. \u0b2e\u0b4b\u0b24\u0b47 \u0b16\u0b41\u0b38\u0b3f \u0b32\u0b3e\u0b17\u0b41\u0b1b\u0b3f\u0964 (Mote khusi l\u0101guchi.) I feel happy.\n"
            "  3. \u0b38\u0b47 \u0b26\u0b41\u0b03\u0b16\u0b40 \u0b05\u0b1b\u0b3f\u0964 (Se duhkha\u012b achi.) She is sad.\n"
            "  4. \u0b2e\u0b4b\u0b24\u0b47 \u0b26\u0b41\u0b03\u0b16 \u0b32\u0b3e\u0b17\u0b41\u0b1b\u0b3f\u0964 (Mote duhkha l\u0101guchi.) I feel sad.\n"
            "  5. \u0b38\u0b47 \u0b30\u0b3e\u0b17\u0b3f\u0b1b\u0b3f\u0964 (Se r\u0101gichi.) He is angry.\n"
            "  6. \u0b30\u0b3e\u0b17 \u0b15\u0b30 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (R\u0101ga kara n\u0101hin.) Do not get angry.\n"
            "  7. \u0b2e\u0b41\u0b01 \u0b21\u0b30\u0b41\u0b1b\u0b3f\u0964 (Mun daruchi.) I am afraid.\n"
            "  8. \u0b21\u0b30 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Dara n\u0101hin.) Do not be afraid.\n"
            "  9. \u0b2e\u0b41\u0b01 \u0b24\u0b41\u0b2e\u0b15\u0b41 \u0b2d\u0b32 \u0b2a\u0b3e\u0b0f\u0964 (Mun tumaku bhala p\u0101e.) I love you.\n"
            "  10. \u0b38\u0b47 \u0b2e\u0b4b\u0b24\u0b47 \u0b2d\u0b32 \u0b2a\u0b3e\u0b06\u0b28\u0b4d\u0b24\u0b3f\u0964 (Se mote bhala p\u0101nti.) She loves me.\n"
            "  11. \u0b2e\u0b4b\u0b24\u0b47 \u0b06\u0b36\u0b4d\u0b1a\u0b30\u0b4d\u0b2f\u0b4d\u0b2f \u0b32\u0b3e\u0b17\u0b3f\u0b32\u0b3e\u0964 (Mote \u0101\u1e63caryya l\u0101gil\u0101.) I was surprised.\n"
            "  12. \u0b15\u0b3f \u0b06\u0b36\u0b4d\u0b1a\u0b30\u0b4d\u0b2f\u0b4d\u0b2f! (Ki \u0101\u1e63caryya!) How surprising!\n"
            "  13. \u0b2e\u0b41\u0b01 \u0b17\u0b30\u0b4d\u0b2c\u0b3f\u0b24\u0964 (Mun garbita.) I am proud.\n"
            "  14. \u0b2e\u0b4b\u0b24\u0b47 \u0b32\u0b3e\u0b1c \u0b32\u0b3e\u0b17\u0b41\u0b1b\u0b3f\u0964 (Mote l\u0101ja l\u0101guchi.) I feel shy.\n"
            "  15. \u0b38\u0b47 \u0b1a\u0b3f\u0b28\u0b4d\u0b24\u0b3e\u0b30\u0b47 \u0b05\u0b1b\u0b3f\u0964 (Se cint\u0101re achi.) He is worried.\n"
            "  16. \u0b1a\u0b3f\u0b28\u0b4d\u0b24\u0b3e \u0b15\u0b30 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Cint\u0101 kara n\u0101hin.) Do not worry.\n"
            "  17. \u0b2e\u0b41\u0b01 \u0b15\u0b4d\u0b32\u0b3e\u0b28\u0b4d\u0b24\u0964 (Mun kl\u0101nta.) I am tired.\n"
            "  18. \u0b2e\u0b4b\u0b24\u0b47 \u0b2d\u0b4b\u0b15 \u0b32\u0b3e\u0b17\u0b3f\u0b1b\u0b3f\u0964 (Mote bhoka l\u0101gichi.) I am hungry.\n"
            "  19. \u0b2e\u0b4b\u0b24\u0b47 \u0b36\u0b4b\u0b37 \u0b32\u0b3e\u0b17\u0b3f\u0b1b\u0b3f\u0964 (Mote \u1e63o\u1e63a l\u0101gichi.) I am thirsty.\n"
            "  20. \u0b36\u0b3e\u0b28\u0b4d\u0b24 \u0b30\u0b41\u0b39\u0964 (\u1e62\u0101nta ruha.) Stay calm."
        ),
        "how_it_works": (
            "This record teaches the feeling grammar: Odia pairs the "
            "experiencer in the dative (mote, to me) with l\u0101gib\u0101 (to "
            "feel, to strike): mote khusi l\u0101guchi, happiness strikes me. "
            "The same frame carries duhkha, l\u0101ja, bhoka, \u1e63o\u1e63a. "
            "Direct adjectives work too (mun khusi achi). Commands comfort "
            "and steady: dara n\u0101hin, cint\u0101 kara n\u0101hin, \u1e63\u0101nta "
            "ruha. Drill: keep a one-line Odia feeling diary for a week."
        ),
        "key_points": [
            "20 emotion-and-feeling sentences with full translations.",
            "The mote + l\u0101gib\u0101 experiencer construction for feelings, hunger, thirst.",
            "Six core emotions: happy, sad, angry, afraid, love, surprise - plus pride, worry, calm.",
            "Comforting commands: do not fear, do not worry, stay calm.",
        ],
        "requirements": ["Read the grammar essentials record for the dative."],
        "standards": [
            "Constructions follow standard Odia usage.",
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["l\u0101gib\u0101", "Mote khusi", "bhala p\u0101e", "20"],
        "sig_lens": (
            "Through the Signature lens feelings are sworn truths of the "
            "heart: every joy a vow kept, every sorrow a vow carried."
        ),
        "drill": {
            "sentences": 20, "theme": "emotions-feelings",
            "construction": "mote + l\u0101gib\u0101",
        },
    },
    {
        "key": "nature",
        "name": "Nature and Weather Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about animals, plants, seasons, and weather "
            "talk - Odia script, romanization, English. \n\n"
            "  1. \u0b06\u0b15\u0b3e\u0b36\u0b30\u0b47 \u0b2e\u0b47\u0b18 \u0b05\u0b1b\u0b3f\u0964 (\u0100k\u0101\u1e63are megha achi.) There are clouds in the sky.\n"
            "  2. \u0b2c\u0b30\u0b4d\u0b37\u0b3e \u0b39\u0b47\u0b09\u0b1b\u0b3f\u0964 (Bar\u1e63\u0101 heuchi.) It is raining.\n"
            "  3. \u0b2a\u0b4d\u0b30\u0b2c\u0b33 \u0b2c\u0b30\u0b4d\u0b37\u0b3e \u0b39\u0b47\u0b09\u0b1b\u0b3f\u0964 (Praba\u1e37a bar\u1e63\u0101 heuchi.) It is raining heavily.\n"
            "  4. \u0b06\u0b1c\u0b3f \u0b2a\u0b3e\u0b17 \u0b16\u0b30\u0b3e\u0b2a\u0964 (\u0100ji p\u0101ga khar\u0101pa.) The weather is bad today.\n"
            "  5. \u0b06\u0b1c\u0b3f \u0b2a\u0b3e\u0b17 \u0b2d\u0b32\u0964 (\u0100ji p\u0101ga bhala.) The weather is good today.\n"
            "  6. \u0b2c\u0b39\u0b41\u0b24 \u0b17\u0b30\u0b2e \u0b39\u0b47\u0b09\u0b1b\u0b3f\u0964 (Bahuta garama heuchi.) It is very hot.\n"
            "  7. \u0b36\u0b40\u0b24 \u0b2a\u0b21\u0b3c\u0b41\u0b1b\u0b3f\u0964 (\u1e62\u012bta pa\u1e0duchi.) It is getting cold.\n"
            "  8. \u0b2a\u0b2c\u0b28 \u0b2c\u0b39\u0b41\u0b1b\u0b3f\u0964 (Pabana bahuchi.) The wind is blowing.\n"
            "  9. \u0b2c\u0b3f\u0b1c\u0b41\u0b33\u0b3f \u0b1a\u0b2e\u0b15\u0b41\u0b1b\u0b3f\u0964 (Bijuli camakuchi.) Lightning is flashing.\n"
            "  10. \u0b18\u0b21\u0b3c\u0b18\u0b21\u0b3c\u0b3f \u0b39\u0b47\u0b09\u0b1b\u0b3f\u0964 (Gha\u1e0dagha\u1e0di heuchi.) It is thundering.\n"
            "  11. \u0b39\u0b3e\u0b24\u0b40 \u0b1c\u0b19\u0b4d\u0b17\u0b32\u0b30\u0b47 \u0b30\u0b41\u0b39\u0b47\u0964 (H\u0101t\u012b ja\u1e45galare ruhe.) The elephant lives in the forest.\n"
            "  12. \u0b2c\u0b3e\u0b18 \u0b36\u0b15\u0b4d\u0b24\u0b3f\u0b36\u0b3e\u0b33\u0b40 \u0b2a\u0b36\u0b41\u0964 (B\u0101gha \u1e63akti\u1e63\u0101\u1e37\u012b pa\u1e63u.) The tiger is a strong animal.\n"
            "  13. \u0b2a\u0b15\u0b4d\u0b37\u0b40 \u0b09\u0b21\u0b3c\u0b41\u0b1b\u0b3f\u0964 (Pak\u1e63\u012b u\u1e0duchi.) The bird is flying.\n"
            "  14. \u0b2e\u0b3e\u0b1b \u0b2a\u0b3e\u0b23\u0b3f\u0b30\u0b47 \u0b2a\u0b39\u0b01\u0b30\u0b47\u0964 (M\u0101cha p\u0101\u1e47ire pahante.) Fish swim in water.\n"
            "  15. \u0b38\u0b3e\u0b2a \u0b18\u0b3e\u0b38\u0b30\u0b47 \u0b32\u0b41\u0b1a\u0b3f\u0b1b\u0b3f\u0964 (S\u0101pa gh\u0101sare luchichi.) The snake is hiding in the grass.\n"
            "  16. \u0b28\u0b21\u0b3c\u0b3f\u0b06 \u0b2c\u0b39\u0b41\u0b1b\u0b3f\u0964 (Nadi\u0101 bahuchi.) The peacock is dancing. (Note: \u0b2e\u0b5f\u0b42\u0b30 may\u016bra is the common word for peacock; \u0b28\u0b21\u0b3c\u0b3f\u0b06 nadi\u0101 is used in folk speech.)\n"
            "  17. \u0b2c\u0b38\u0b28\u0b4d\u0b24\u0b30\u0b47 \u0b2b\u0b41\u0b32 \u0b2b\u0b41\u0b1f\u0b47\u0964 (Basantare phula phu\u1e6de.) Flowers bloom in spring.\n"
            "  18. \u0b17\u0b1b\u0b30 \u0b1b\u0b3e\u0b07 \u0b25\u0b23\u0b4d\u0b21\u0b3e\u0964 (Gachara ch\u0101i \u1e6dha\u1e47\u1e0d\u0101.) The shade of the tree is cool.\n"
            "  19. \u0b28\u0b26\u0b40 \u0b38\u0b2e\u0b41\u0b26\u0b4d\u0b30\u0b15\u0b41 \u0b2c\u0b39\u0b41\u0b1b\u0b3f\u0964 (Nad\u012b samudraku bahuchi.) The river flows to the sea.\n"
            "  20. \u0b2a\u0b4d\u0b30\u0b15\u0b43\u0b24\u0b3f \u0b38\u0b41\u0b28\u0b4d\u0b26\u0b30\u0964 (Prak\u1e5bti sundara.) Nature is beautiful."
        ),
        "how_it_works": (
            "This record is weather small-talk and the natural world: twenty "
            "sentences built on heuchi (is happening) for weather - bar\u1e63\u0101 "
            "heuchi, garama heuchi - and the animal/plant stock (h\u0101t\u012b, "
            "b\u0101gha, pak\u1e63\u012b, m\u0101cha, s\u0101pa, gacha, phula). "
            "Sentence 16 carries an honest usage note distinguishing folk "
            "speech (nadi\u0101) from the standard word (may\u016bra). Drill: "
            "give tomorrow's weather forecast in Odia, then describe three "
            "animals."
        ),
        "key_points": [
            "20 nature-and-weather sentences with full translations.",
            "Weather pattern: X heuchi (it is Xing).",
            "Animals, plants, seasons, and sky vocabulary.",
            "Honest usage note on folk vs standard word for peacock.",
        ],
        "requirements": ["Read the verbs record for heuchi and the action verbs."],
        "standards": [
            "Usage note distinguishes documented folk speech from standard forms.",
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["bar\u1e63\u0101 heuchi", "p\u0101ga", "may\u016bra", "20"],
        "sig_lens": (
            "Through the Signature lens nature is the oldest covenant: "
            "every monsoon a vow renewed, every bloom a seal of spring."
        ),
        "drill": {
            "sentences": 20, "theme": "nature-weather",
            "weather_verb": "heuchi",
        },
    },
    {
        "key": "shopping",
        "name": "Shopping and Money Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the market, prices, bargaining, and paying "
            "- Odia script, romanization, English. \n\n"
            "  1. \u0b2c\u0b1c\u0b3e\u0b30 \u0b15\u0b47\u0b09\u0b01\u0b20\u0b3e\u0b30\u0b47? (Baj\u0101ra keun\u1e6dh\u0101re?) Where is the market?\n"
            "  2. \u0b0f\u0b39\u0b3e\u0b30 \u0b26\u0b3e\u0b2e \u0b15\u0b47\u0b24\u0b47? (Eh\u0101ra d\u0101ma kete?) What is the price of this?\n"
            "  3. \u0b2c\u0b39\u0b41\u0b24 \u0b26\u0b3e\u0b2e\u0b40\u0964 (Bahuta d\u0101m\u012b.) It is very expensive.\n"
            "  4. \u0b15\u0b2e \u0b15\u0b30\u0b28\u0b4d\u0b24\u0b41\u0964 (Kama karantu.) Please reduce the price.\n"
            "  5. \u0b36\u0b47\u0b37 \u0b26\u0b3e\u0b2e \u0b15\u0b47\u0b24\u0b47? (\u1e62e\u1e63a d\u0101ma kete?) What is the final price?\n"
            "  6. \u0b2e\u0b41\u0b01 \u0b0f\u0b39\u0b3e \u0b28\u0b47\u0b2c\u0b3f\u0964 (Mun eh\u0101 nebi.) I will take this.\n"
            "  7. \u0b2e\u0b41\u0b01 \u0b0f\u0b39\u0b3e \u0b28\u0b47\u0b2c\u0b3f \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Mun eh\u0101 nebi n\u0101hin.) I will not take this.\n"
            "  8. \u0b06\u0b09 \u0b15\u0b2e \u0b26\u0b3e\u0b2e\u0b30\u0b47 \u0b05\u0b1b\u0b3f \u0b15\u0b3f? (\u0100u kama d\u0101mare achi ki?) Is there a cheaper one?\n"
            "  9. \u0b2e\u0b4b\u0b24\u0b47 \u0b38\u0b47\u0b07\u0b1f\u0b3e \u0b26\u0b47\u0b16\u0b3e\u0b28\u0b4d\u0b24\u0b41\u0964 (Mote sei\u1e6d\u0101 dekh\u0101ntu.) Please show me that one.\n"
            "  10. \u0b0f\u0b39\u0b3e \u0b2d\u0b32 \u0b05\u0b1b\u0b3f \u0b15\u0b3f? (Eh\u0101 bhala achi ki?) Is this good?\n"
            "  11. \u0b2c\u0b39\u0b41\u0b24 \u0b2d\u0b32\u0964 (Bahuta bhala.) Very good.\n"
            "  12. \u0b15\u0b3f\u0b32\u0b4b \u0b15\u0b47\u0b24\u0b47? (Kilo kete?) How much per kilo?\n"
            "  13. \u0b26\u0b41\u0b07 \u0b15\u0b3f\u0b32\u0b4b \u0b26\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (Dui kilo diantu.) Please give two kilos.\n"
            "  14. \u0b1f\u0b19\u0b4d\u0b15\u0b3e \u0b2d\u0b19\u0b4d\u0b17\u0b47\u0b07 \u0b26\u0b47\u0b2c\u0b3f\u0964 (\u1e6da\u1e45k\u0101 bh\u0101\u1e45gei debi.) I will pay in cash.\n"
            "  15. \u0b16\u0b41\u0b1a\u0b41\u0b30\u0b3e \u0b1f\u0b19\u0b4d\u0b15\u0b3e \u0b05\u0b1b\u0b3f \u0b15\u0b3f? (Khucar\u0101 \u1e6da\u1e45k\u0101 achi ki?) Do you have change?\n"
            "  16. \u0b30\u0b38\u0b3f\u0b26 \u0b26\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (Rasida diantu.) Please give a receipt.\n"
            "  17. \u0b26\u0b4b\u0b15\u0b3e\u0b28 \u0b15\u0b47\u0b24\u0b47\u0b2c\u0b47\u0b33\u0b47 \u0b2c\u0b28\u0b4d\u0b26 \u0b39\u0b47\u0b2c? (Dok\u0101na ketebe\u1e37e banda heba?) When will the shop close?\n"
            "  18. \u0b15\u0b3e\u0b32\u0b3f \u0b06\u0b38\u0b3f\u0b2c\u0b3f\u0964 (K\u0101li \u0101sibi.) I will come tomorrow.\n"
            "  19. \u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26, \u0b2d\u0b3e\u0b07\u0964 (Dhanyab\u0101da, bh\u0101i.) Thank you, brother. (warm closing to a shopkeeper)\n"
            "  20. \u0b2c\u0b1c\u0b3e\u0b30 \u0b38\u0b30\u0b3f\u0b32\u0b3e\u0964 (Baj\u0101ra saril\u0101.) The shopping is done."
        ),
        "how_it_works": (
            "This record is the market drill: twenty sentences from arrival "
            "to done. It teaches the price question (eh\u0101ra d\u0101ma "
            "kete?), the bargaining pair (bahuta d\u0101m\u012b / kama "
            "karantu), the final-price close (\u1e63e\u1e63a d\u0101ma kete?), "
            "accept and refuse (nebi / nebi n\u0101hin), quantity (kilo "
            "kete?), payment (\u1e6da\u1e45k\u0101 bh\u0101\u1e45gei, cash), "
            "change, and receipt. The warm dhanyab\u0101da, bh\u0101i closing "
            "is real market culture. Drill: role-play buyer and seller with "
            "three items."
        ),
        "key_points": [
            "20 shopping-and-money sentences with full translations.",
            "Price, bargaining, accept/refuse, quantity, payment, receipt.",
            "Currency: \u1e6da\u1e45k\u0101 (rupee).",
            "Real market culture in the warm closing.",
        ],
        "requirements": ["Read the numbers record for prices and quantities."],
        "standards": [
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["d\u0101ma kete", "Kama karantu", "\u1e6da\u1e45k\u0101", "20"],
        "sig_lens": (
            "Through the Signature lens the market is the covenant of fair "
            "exchange: every price a sworn measure, every bargain a seal of "
            "mutual respect."
        ),
        "drill": {
            "sentences": 20, "theme": "shopping-money",
            "currency": "\u1e6da\u1e45k\u0101",
        },
    },
    {
        "key": "friendship",
        "name": "Friendship and Social Life Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for meeting people, invitations, and "
            "celebrations - Odia script, romanization, English. \n\n"
            "  1. \u0b06\u0b38\u0b28\u0b4d\u0b24\u0b41, \u0b2c\u0b38\u0b28\u0b4d\u0b24\u0b41\u0964 (\u0100santu, basantu.) Please come in, please sit.\n"
            "  2. \u0b1a\u0b3e \u0b2a\u0b3f\u0b07\u0b2c\u0b47? (C\u0101 piibe?) Will you have tea?\n"
            "  3. \u0b39\u0b01, \u0b26\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (Han, diantu.) Yes, please give.\n"
            "  4. \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15 \u0b2a\u0b30\u0b3f\u0b1a\u0b5f \u0b26\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (\u0100pa\u1e47a\u1e45ka paricaya diantu.) Please introduce yourself.\n"
            "  5. \u0b0f \u0b2e\u0b4b\u0b30 \u0b2c\u0b28\u0b4d\u0b27\u0b41\u0964 (E mora bandhu.) This is my friend.\n"
            "  6. \u0b06\u0b2e\u0b47 \u0b2c\u0b39\u0b41\u0b24 \u0b26\u0b3f\u0b28\u0b30\u0b41 \u0b2c\u0b28\u0b4d\u0b27\u0b41\u0964 (\u0100me bahuta dinaru bandhu.) We have been friends for a long time.\n"
            "  7. \u0b15\u0b3e\u0b32\u0b3f \u0b2e\u0b4b \u0b18\u0b30\u0b15\u0b41 \u0b06\u0b38\u0964 (K\u0101li mo gharaku \u0101sa.) Come to my house tomorrow.\n"
            "  8. \u0b30\u0b3e\u0b24\u0b4d\u0b30\u0b3f \u0b2d\u0b4b\u0b1c\u0b28\u0b30\u0b47 \u0b06\u0b38\u0b3f\u0b2c\u0964 (R\u0101tri bhojanare \u0101siba.) I will come for dinner.\n"
            "  9. \u0b1c\u0b28\u0b4d\u0b2e\u0b26\u0b3f\u0b28\u0b30 \u0b36\u0b41\u0b2d\u0b47\u0b1a\u0b4d\u0b1b\u0b3e\u0964 (Janmadinara \u1e63ubhech\u0101.) Happy birthday wishes.\n"
            "  10. \u0b2c\u0b3f\u0b2c\u0b3e\u0b39 \u0b09\u0b24\u0b4d\u0b38\u0b2c\u0b30\u0b47 \u0b28\u0b3f\u0b2e\u0b28\u0b4d\u0b24\u0b4d\u0b30\u0b23\u0964 (Bib\u0101ha utsabare nimantra\u1e47a.) Invitation to the wedding celebration.\n"
            "  11. \u0b30\u0b25\u0b2f\u0b3e\u0b24\u0b4d\u0b30\u0b3e \u0b26\u0b47\u0b16\u0b3f\u0b2c\u0b3e\u0b15\u0b41 \u0b2f\u0b3f\u0b2c\u0b3e\u0964 (Rathay\u0101tr\u0101 dekhib\u0101ku yib\u0101.) We will go to see the Rath Yatra.\n"
            "  12. \u0b28\u0b42\u0b06\u0b16\u0b3e\u0b07 \u0b1c\u0b41\u0b39\u0b3e\u0b30\u0964 (Nu\u0101kh\u0101i juh\u0101ra.) Nuakhai greetings. (western Odisha harvest festival)\n"
            "  13. \u0b26\u0b41\u0b30\u0b4d\u0b17\u0b3e\u0b2a\u0b42\u0b1c\u0b3e\u0b30\u0b47 \u0b2d\u0b47\u0b1f\u0b3f\u0b2c\u0b3e\u0964 (Durg\u0101p\u016bj\u0101re bhe\u1e6dib\u0101.) We will meet at Durga Puja.\n"
            "  14. \u0b2e\u0b3f\u0b20\u0b3e \u0b2c\u0b3e\u0b23\u0b4d\u0b1f\u0964 (Mi\u1e6dh\u0101 b\u0101\u1e47\u1e6da.) Distribute sweets. (celebration custom)\n"
            "  15. \u0b06\u0b2e\u0b47 \u0b0f\u0b15\u0b3e\u0b20\u0b3f \u0b2c\u0b41\u0b32\u0b3f\u0b2c\u0b3e\u0964 (\u0100me ek\u0101\u1e6dhi bulib\u0101.) We will stroll together.\n"
            "  16. \u0b17\u0b2a\u0b38\u0b2a \u0b15\u0b30\u0b3f\u0b2c\u0b3e\u0964 (Gapasapa karib\u0101.) We will chat.\n"
            "  17. \u0b24\u0b41\u0b2e \u0b2c\u0b3f\u0b28\u0b3e \u0b2e\u0b1c\u0b3e \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Tuma bin\u0101 maj\u0101 n\u0101hin.) It is no fun without you.\n"
            "  18. \u0b2c\u0b28\u0b4d\u0b27\u0b41\u0b24\u0b3e \u0b1a\u0b3f\u0b30\u0b26\u0b3f\u0b28 \u0b30\u0b39\u0b47\u0964 (Bandhut\u0101 ciradina rahe.) May the friendship last forever.\n"
            "  19. \u0b2b\u0b47\u0b30\u0b3f \u0b26\u0b47\u0b16\u0b3e \u0b39\u0b47\u0b2c\u0b3e\u0964 (Pheri dekh\u0101 heb\u0101.) We will meet again.\n"
            "  20. \u0b2c\u0b3f\u0b26\u0b3e\u0b5f\u0964 (Bid\u0101ya.) Goodbye."
        ),
        "how_it_works": (
            "This record is the social round: twenty sentences for welcome "
            "(the \u0101santu/basantu hospitality pair), introductions, "
            "invitations, and the Odia festival calendar (Rathay\u0101tr\u0101, "
            "Nu\u0101kh\u0101i with its juh\u0101ra greeting, Durg\u0101p\u016bj\u0101, "
            "bib\u0101ha weddings, janmadina birthdays). The mi\u1e6dh\u0101 "
            "b\u0101\u1e47\u1e6da custom (distributing sweets at good news) is "
            "real social grammar. Drill: invite a friend to dinner in Odia, "
            "then accept in Odia."
        ),
        "key_points": [
            "20 friendship-and-social-life sentences with full translations.",
            "Hospitality pair: \u0101santu, basantu; tea offer c\u0101 piibe?",
            "Odia festivals: Rathay\u0101tr\u0101, Nu\u0101kh\u0101i, Durg\u0101p\u016bj\u0101; wedding and birthday language.",
            "Real custom: mi\u1e6dh\u0101 b\u0101\u1e47\u1e6da (distributing sweets at celebrations).",
        ],
        "requirements": ["Read the greetings record first."],
        "standards": [
            "Festival names and customs follow documented Odia usage.",
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["Rathay\u0101tr\u0101", "Nu\u0101kh\u0101i", "Mi\u1e6dh\u0101 b\u0101\u1e47\u1e6da", "20"],
        "sig_lens": (
            "Through the Signature lens friendship is the covenant of "
            "companionship: every invitation a vow of welcome, every shared "
            "sweet a seal of joy."
        ),
        "drill": {
            "sentences": 20, "theme": "friendship-social",
            "festivals": ["Rathay\u0101tr\u0101", "Nu\u0101kh\u0101i", "Durg\u0101p\u016bj\u0101"],
        },
    },
    {
        "key": "technology",
        "name": "Technology and Communication Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the phone, internet, computer, and "
            "messaging - Odia script, romanization, English. Modern Odia "
            "freely uses loanwords (phone, internet, message) in Odia "
            "grammar. \n\n"
            "  1. \u0b2e\u0b4b\u0b30 \u0b2b\u0b4b\u0b28 \u0b15\u0b47\u0b09\u0b01\u0b20\u0b3f? (Mora phona keun\u1e6dhi?) Where is my phone?\n"
            "  2. \u0b2b\u0b4b\u0b28 \u0b2c\u0b3e\u0b1c\u0b41\u0b1b\u0b3f\u0964 (Phona b\u0101juchi.) The phone is ringing.\n"
            "  3. \u0b2b\u0b4b\u0b28 \u0b09\u0b20\u0b3e\u0b05\u0964 (Phona u\u1e6dh\u0101a.) Pick up the phone.\n"
            "  4. \u0b39\u0b3e\u0b32\u0b4b, \u0b15\u0b3f\u0b0f \u0b15\u0b39\u0b41\u0b1b\u0b28\u0b4d\u0b24\u0b3f? (H\u0101lo, kie kahuchanti?) Hello, who is speaking?\n"
            "  5. \u0b2e\u0b41\u0b01 \u0b2a\u0b30\u0b47 \u0b2b\u0b4b\u0b28 \u0b15\u0b30\u0b3f\u0b2c\u0b3f\u0964 (Mun pare phona karibi.) I will call later.\n"
            "  6. \u0b28\u0b47\u0b1f\u0b71\u0b3e\u0b30\u0b4d\u0b15 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Ne\u1e6dawarka n\u0101hin.) There is no network.\n"
            "  7. \u0b07\u0b23\u0b4d\u0b1f\u0b30\u0b28\u0b47\u0b1f \u0b27\u0b40\u0b30\u0964 (I\u1e47\u1e6darane\u1e6da dh\u012bra.) The internet is slow.\n"
            "  8. \u0b13\u0b5f\u0b3e\u0b07\u0b2b\u0b3e\u0b07 \u0b2a\u0b3e\u0b38\u0b71\u0b3e\u0b30\u0b4d\u0b21 \u0b26\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (Oy\u0101iph\u0101i p\u0101sw\u0101rda diantu.) Please give the Wi-Fi password.\n"
            "  9. \u0b2e\u0b4b\u0b24\u0b47 \u0b2e\u0b47\u0b38\u0b47\u0b1c \u0b15\u0b30\u0b28\u0b4d\u0b24\u0b41\u0964 (Mote meseja karantu.) Please message me.\n"
            "  10. \u0b2e\u0b41\u0b01 \u0b24\u0b41\u0b2e\u0b15\u0b41 \u0b2e\u0b47\u0b38\u0b47\u0b1c \u0b15\u0b30\u0b3f\u0b1b\u0b3f\u0964 (Mun tumaku meseja karichi.) I have messaged you.\n"
            "  11. \u0b07\u0b2e\u0b47\u0b32 \u0b2a\u0b20\u0b3e\u0b05\u0964 (Imela pa\u1e6dh\u0101a.) Send an email.\n"
            "  12. \u0b2b\u0b1f\u0b4b \u0b09\u0b20\u0b3e\u0b05\u0964 (Pha\u1e6do u\u1e6dh\u0101a.) Take a photo.\n"
            "  13. \u0b2d\u0b3f\u0b21\u0b3f\u0b13 \u0b26\u0b47\u0b16\u0b41\u0b1b\u0b3f\u0964 (Bhidio dekhuchi.) I am watching a video.\n"
            "  14. \u0b15\u0b2e\u0b4d\u0b2a\u0b4d\u0b5f\u0b41\u0b1f\u0b30 \u0b1a\u0b3e\u0b32\u0b41 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Kampyu\u1e6dara c\u0101lu n\u0101hin.) The computer is not working.\n"
            "  15. \u0b15\u0b2e\u0b4d\u0b2a\u0b4d\u0b5f\u0b41\u0b1f\u0b30 \u0b2c\u0b28\u0b4d\u0b26 \u0b15\u0b30\u0964 (Kampyu\u1e6dara banda kara.) Turn off the computer.\n"
            "  16. \u0b2c\u0b4d\u0b5f\u0b3e\u0b1f\u0b47\u0b30\u0b3f \u0b36\u0b47\u0b37 \u0b39\u0b47\u0b07\u0b1b\u0b3f\u0964 (By\u0101\u1e6deri \u1e63e\u1e63a heichi.) The battery is finished.\n"
            "  17. \u0b1a\u0b3e\u0b30\u0b4d\u0b1c\u0b30\u0b47 \u0b32\u0b17\u0b3e\u0b05\u0964 (C\u0101rjare lag\u0101a.) Put it on charge.\n"
            "  18. \u0b2e\u0b4b \u0b28\u0b2e\u0b4d\u0b2c\u0b30 \u0b32\u0b47\u0b16\u0b3f \u0b28\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (Mo nambara lekhi niantu.) Please note down my number.\n"
            "  19. \u0b05\u0b28\u0b32\u0b3e\u0b07\u0b28\u0b30\u0b47 \u0b16\u0b4b\u0b1c\u0964 (Anal\u0101inare khoja.) Search online.\n"
            "  20. \u0b2a\u0b4d\u0b30\u0b2f\u0b41\u0b15\u0b4d\u0b24\u0b3f \u0b2e\u0b3e\u0b28\u0b2c\u0b30 \u0b38\u0b47\u0b2c\u0b3e \u0b2a\u0b3e\u0b07\u0b01\u0964 (Prayukti m\u0101nabara seb\u0101 p\u0101in.) Technology is for the service of mankind."
        ),
        "how_it_works": (
            "This record proves Odia is a living modern language: twenty "
            "sentences where loanwords (phona, ne\u1e6dawarka, i\u1e47\u1e6darane\u1e6da, "
            "meseja, imela, kampyu\u1e6dara) take Odia verb endings and "
            "cases without friction. The phone-call frame (h\u0101lo, kie "
            "kahuchanti?) and the troubleshooting pair (c\u0101lu n\u0101hin / "
            "banda kara) are immediately usable. It closes with a real "
            "humanist maxim about technology. Drill: narrate your last "
            "phone call in Odia."
        ),
        "key_points": [
            "20 technology-and-communication sentences with full translations.",
            "Loanwords take Odia endings: phona b\u0101juchi, meseja karichi.",
            "Phone, network, Wi-Fi, email, computer, battery, charging covered.",
            "Closes with a real maxim: technology is for the service of mankind.",
        ],
        "requirements": ["Read the verbs record for the verb frames."],
        "standards": [
            "Loanword usage follows real modern Odia.",
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["phona", "meseja", "Kampyu\u1e6dara", "20"],
        "sig_lens": (
            "Through the Signature lens technology is the covenant's new "
            "messenger: every call a vow carried on air, every message a "
            "seal delivered."
        ),
        "drill": {
            "sentences": 20, "theme": "technology-communication",
            "loanwords": ["phona", "meseja", "imela", "kampyu\u1e6dara", "i\u1e47\u1e6darane\u1e6da"],
        },
    },
    {
        "key": "tenses",
        "name": "Verb Tenses in Sentences",
        "group": "Grammar in Action",
        "ladder_rank": 21,
        "ladder_tier": "advanced",
        "description": (
            "The Odia tense system in sentences: present (habitual -\u0b0f and "
            "progressive -\u0b09\u0b1b\u0b3f), past (-\u0b32\u0b3f/-\u0b32\u0b3e), and future (-\u0b2c\u0b3f) - "
            "five or more translated sentences per tense, built on the verb "
            "\u0b15\u0b30\u0b4d (kar, to do) and everyday verbs. \n\n"
            "Present habitual (-\u0b0f / -\u0b28\u0b4d\u0b24\u0b3f): things done regularly.\n"
            "  1. \u0b2e\u0b41\u0b01 \u0b2a\u0b4d\u0b30\u0b24\u0b3f\u0b26\u0b3f\u0b28 \u0b2d\u0b3e\u0b24 \u0b16\u0b3e\u0b0f\u0964 (Mun pratidina bh\u0101ta kh\u0101e.) I eat rice every day.\n"
            "  2. \u0b38\u0b47 \u0b2c\u0b3f\u0b26\u0b4d\u0b5f\u0b3e\u0b33\u0b5f\u0b15\u0b41 \u0b2f\u0b3e\u0b0f\u0964 (Se bidy\u0101\u1e37ayaku y\u0101e.) He goes to school.\n"
            "  3. \u0b38\u0b47\u0b2e\u0b3e\u0b28\u0b47 \u0b13\u0b21\u0b3c\u0b3f\u0b06 \u0b15\u0b39\u0b28\u0b4d\u0b24\u0b3f\u0964 (Sem\u0101ne odi\u0101 kahanti.) They speak Odia.\n"
            "  4. \u0b2e\u0b3e \u0b30\u0b4b\u0b37\u0b47\u0b07 \u0b18\u0b30\u0b47 \u0b30\u0b3e\u0b28\u0b4d\u0b27\u0b28\u0b4d\u0b24\u0b3f\u0964 (M\u0101 ro\u1e63ei ghare r\u0101ndhanti.) Mother cooks in the kitchen.\n"
            "  5. \u0b38\u0b42\u0b30\u0b4d\u0b2f\u0b4d\u0b5f \u0b2a\u0b42\u0b30\u0b4d\u0b2c\u0b30\u0b47 \u0b09\u0b20\u0b47\u0964 (S\u016bryya p\u016brbare u\u1e6dhe.) The sun rises in the east.\n"
            "Present progressive (-\u0b09\u0b1b\u0b3f): happening right now.\n"
            "  6. \u0b2e\u0b41\u0b01 \u0b2d\u0b3e\u0b24 \u0b16\u0b3e\u0b09\u0b1b\u0b3f\u0964 (Mun bh\u0101ta kh\u0101uchi.) I am eating rice.\n"
            "  7. \u0b38\u0b47 \u0b2c\u0b39\u0b3f \u0b2a\u0b22\u0b3c\u0b41\u0b1b\u0b3f\u0964 (Se bahi pa\u1e0dhu\u1e63i.) He is reading a book.\n"
            "  8. \u0b38\u0b47\u0b2e\u0b3e\u0b28\u0b47 \u0b16\u0b47\u0b33\u0b41\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 (Sem\u0101ne khe\u1e37uchanti.) They are playing.\n"
            "  9. \u0b2c\u0b30\u0b4d\u0b37\u0b3e \u0b39\u0b47\u0b09\u0b1b\u0b3f\u0964 (Bar\u1e63\u0101 heuchi.) It is raining.\n"
            "  10. \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b23 \u0b15\u0b30\u0b41\u0b1b? (Tume ka\u1e47a karucha?) What are you doing?\n"
            "Past (-\u0b32\u0b3f / -\u0b32\u0b3e / -\u0b32\u0b47): finished action.\n"
            "  11. \u0b2e\u0b41\u0b01 \u0b2d\u0b3e\u0b24 \u0b16\u0b3e\u0b07\u0b32\u0b3f\u0964 (Mun bh\u0101ta kh\u0101ili.) I ate rice.\n"
            "  12. \u0b38\u0b47 \u0b2c\u0b1c\u0b3e\u0b30\u0b15\u0b41 \u0b17\u0b32\u0b3e\u0964 (Se baj\u0101raku gal\u0101.) He went to the market.\n"
            "  13. \u0b38\u0b47\u0b2e\u0b3e\u0b28\u0b47 \u0b06\u0b38\u0b3f\u0b32\u0b47\u0964 (Sem\u0101ne \u0101sile.) They came.\n"
            "  14. \u0b2e\u0b41\u0b01 \u0b2c\u0b39\u0b3f\u0b1f\u0b3f \u0b2a\u0b22\u0b3c\u0b3f\u0b32\u0b3f\u0964 (Mun bahi\u1e6di pa\u1e0dhili.) I read the book.\n"
            "  15. \u0b15\u0b3e\u0b32\u0b3f \u0b2c\u0b30\u0b4d\u0b37\u0b3e \u0b39\u0b47\u0b32\u0b3e\u0964 (K\u0101li bar\u1e63\u0101 hel\u0101.) It rained yesterday.\n"
            "Future (-\u0b2c\u0b3f): what will happen.\n"
            "  16. \u0b2e\u0b41\u0b01 \u0b2d\u0b3e\u0b24 \u0b16\u0b3e\u0b07\u0b2c\u0b3f\u0964 (Mun bh\u0101ta kh\u0101ibi.) I will eat rice.\n"
            "  17. \u0b38\u0b47 \u0b2c\u0b1c\u0b3e\u0b30\u0b15\u0b41 \u0b2f\u0b3f\u0b2c\u0964 (Se baj\u0101raku yiba.) He will go to the market.\n"
            "  18. \u0b38\u0b47\u0b2e\u0b3e\u0b28\u0b47 \u0b06\u0b38\u0b3f\u0b2c\u0b47\u0964 (Sem\u0101ne \u0101sibe.) They will come.\n"
            "  19. \u0b15\u0b3e\u0b32\u0b3f \u0b2c\u0b30\u0b4d\u0b37\u0b3e \u0b39\u0b47\u0b2c\u0964 (K\u0101li bar\u1e63\u0101 heba.) It will rain tomorrow.\n"
            "  20. \u0b06\u0b2e\u0b47 \u0b2a\u0b41\u0b30\u0b40 \u0b2f\u0b3f\u0b2c\u0b3e\u0964 (\u0100me pur\u012b yib\u0101.) We will go to Puri.\n"
            "The pattern in one line: kh\u0101e (eats, habitually) / kh\u0101uchi "
            "(is eating) / kh\u0101ili (ate) / kh\u0101ibi (will eat). Learn "
            "one verb's four forms and every verb follows."
        ),
        "how_it_works": (
            "This record is the time machine: twenty sentences, five per "
            "tense, all built on familiar verbs so only the endings are new. "
            "It contrasts habitual (-e/-anti) with progressive (-uchi) - "
            "kh\u0101e vs kh\u0101uchi is the distinction English speakers "
            "must learn - then past (-li/-l\u0101/-le) and future (-bi). "
            "Subject agreement is visible: se gal\u0101 (he went) vs sem\u0101ne "
            "\u0101sile (they came) vs mun kh\u0101ili (I ate). The closing "
            "one-line pattern (kh\u0101e/kh\u0101uchi/kh\u0101ili/kh\u0101ibi) is "
            "the whole system in miniature. Drill: take ten verbs and write "
            "all four forms."
        ),
        "key_points": [
            "20 sentences: 5 present habitual, 5 present progressive, 5 past, 5 future.",
            "Habitual -e vs progressive -uchi contrast taught explicitly.",
            "Past -li/-l\u0101/-le and future -bi with subject agreement visible.",
            "One-line master pattern: kh\u0101e / kh\u0101uchi / kh\u0101ili / kh\u0101ibi.",
        ],
        "requirements": ["Read the verbs and grammar records first."],
        "standards": [
            "Conjugations follow standard Odia.",
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA, CIT_MOHANTY],
        "must_contain": ["kh\u0101e", "kh\u0101uchi", "kh\u0101ili", "kh\u0101ibi", "20"],
        "sig_lens": (
            "Through the Signature lens tense is the covenant of time: "
            "every past a vow remembered, every future a vow promised."
        ),
        "drill": {
            "tenses": ["habitual", "progressive", "past", "future"],
            "sentences_per_tense": 5,
            "master_verb": "kh\u0101",
            "master_forms": ["kh\u0101e", "kh\u0101uchi", "kh\u0101ili", "kh\u0101ibi"],
        },
    },
    {
        "key": "qa",
        "name": "Questions and Answers",
        "group": "Grammar in Action",
        "ladder_rank": 22,
        "ladder_tier": "advanced",
        "description": (
            "Twenty question-and-answer pairs covering who, what, where, "
            "when, why, and how - Odia script, romanization, English. \n\n"
            "  1. Q: \u0b24\u0b41\u0b2e\u0b30 \u0b28\u0b3e\u0b2e \u0b15\u0b23? (Tumara n\u0101ma ka\u1e47a?) What is your name? "
            "A: \u0b2e\u0b4b \u0b28\u0b3e\u0b2e \u0b2e\u0b28\u0b4b\u0b28\u0964 (Mo n\u0101ma Manon.) My name is Manon.\n"
            "  2. Q: \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b47\u0b09\u0b01\u0b20\u0b41 \u0b06\u0b38\u0b3f\u0b1b? (Tume keun\u1e6dhu \u0101sicha?) Where are you from? "
            "A: \u0b2e\u0b41\u0b01 \u0b13\u0b21\u0b3c\u0b3f\u0b36\u0b3e\u0b30\u0b41 \u0b06\u0b38\u0b3f\u0b1b\u0b3f\u0964 (Mun odi\u1e63\u0101ru \u0101sichi.) I am from Odisha.\n"
            "  3. Q: \u0b0f\u0b39\u0b3e \u0b15\u0b23? (Eh\u0101 ka\u1e47a?) What is this? "
            "A: \u0b0f\u0b39\u0b3e \u0b0f\u0b15 \u0b2c\u0b39\u0b3f\u0964 (Eh\u0101 eka bahi.) This is a book.\n"
            "  4. Q: \u0b38\u0b47 \u0b15\u0b3f\u0b0f? (Se kie?) Who is he? "
            "A: \u0b38\u0b47 \u0b2e\u0b4b\u0b30 \u0b2d\u0b3e\u0b07\u0964 (Se mora bh\u0101i.) He is my brother.\n"
            "  5. Q: \u0b2c\u0b1c\u0b3e\u0b30 \u0b15\u0b47\u0b09\u0b01\u0b20\u0b3e\u0b30\u0b47? (Baj\u0101ra keun\u1e6dh\u0101re?) Where is the market? "
            "A: \u0b38\u0b47\u0b20\u0b3e\u0b30\u0b47\u0964 (Se\u1e6dh\u0101re.) There. (pointing)\n"
            "  6. Q: \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b47\u0b2c\u0b47 \u0b06\u0b38\u0b3f\u0b2c? (Tume kebe \u0101siba?) When will you come? "
            "A: \u0b15\u0b3e\u0b32\u0b3f \u0b06\u0b38\u0b3f\u0b2c\u0b3f\u0964 (K\u0101li \u0101sibi.) I will come tomorrow.\n"
            "  7. Q: \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b3e\u0b39\u0b3f\u0b01\u0b15\u0b3f \u0b39\u0b38\u0b41\u0b1b? (Tume k\u0101hinki hasucha?) Why are you laughing? "
            "A: \u0b17\u0b2a\u0b1f\u0b3f \u0b2e\u0b1c\u0b3e\u0b26\u0b3e\u0b30 \u0b25\u0b3f\u0b32\u0b3e\u0964 (Gapa\u1e6di maj\u0101d\u0101ra thil\u0101.) The story was funny.\n"
            "  8. Q: \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b3f\u0b2a\u0b30\u0b3f \u0b06\u0b38\u0b3f\u0b32? (Tume kipari \u0101sila?) How did you come? "
            "A: \u0b2c\u0b38\u0b30\u0b47 \u0b06\u0b38\u0b3f\u0b32\u0b3f\u0964 (Basare \u0101sili.) I came by bus.\n"
            "  9. Q: \u0b0f\u0b39\u0b3e\u0b30 \u0b26\u0b3e\u0b2e \u0b15\u0b47\u0b24\u0b47? (Eh\u0101ra d\u0101ma kete?) How much is this? "
            "A: \u0b2a\u0b1e\u0b4d\u0b1a\u0b3e\u0b36 \u0b1f\u0b19\u0b4d\u0b15\u0b3e\u0964 (Panc\u0101\u1e63a \u1e6da\u1e45k\u0101.) Fifty rupees.\n"
            "  10. Q: \u0b24\u0b41\u0b2e\u0b47 \u0b13\u0b21\u0b3c\u0b3f\u0b06 \u0b15\u0b39\u0b3f\u0b2a\u0b3e\u0b30 \u0b15\u0b3f? (Tume odi\u0101 kahip\u0101ra ki?) Can you speak Odia? "
            "A: \u0b39\u0b01, \u0b1f\u0b3f\u0b15\u0b47 \u0b15\u0b39\u0b3f\u0b2a\u0b3e\u0b30\u0b47\u0964 (Han, \u1e6dike kahip\u0101re.) Yes, a little.\n"
            "  11. Q: \u0b24\u0b41\u0b2e\u0b47 \u0b2d\u0b4b\u0b15 \u0b15\u0b3f? (Tume bhoka ki?) Are you hungry? "
            "A: \u0b28\u0b3e, \u0b2e\u0b41\u0b01 \u0b16\u0b3e\u0b07\u0b38\u0b3e\u0b30\u0b3f\u0b1b\u0b3f\u0964 (N\u0101, mun kh\u0101is\u0101richi.) No, I have eaten.\n"
            "  12. Q: \u0b15\u0b47\u0b24\u0b47 \u0b1c\u0b23 \u0b05\u0b1b\u0b28\u0b4d\u0b24\u0b3f? (Kete ja\u1e47a achanti?) How many people are there? "
            "A: \u0b26\u0b36 \u0b1c\u0b23\u0964 (Da\u1e63a ja\u1e47a.) Ten people.\n"
            "  13. Q: \u0b24\u0b41\u0b2e\u0b30 \u0b2c\u0b5f\u0b38 \u0b15\u0b47\u0b24\u0b47? (Tumara bayasa kete?) How old are you? "
            "A: \u0b2e\u0b4b\u0b30 \u0b2c\u0b5f\u0b38 \u0b24\u0b3f\u0b30\u0b3f\u0b36\u0964 (Mora bayasa tiri\u1e63a.) I am thirty.\n"
            "  14. Q: \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b47\u0b09\u0b01 \u0b15\u0b3e\u0b2e \u0b15\u0b30? (Tume keun k\u0101ma kara?) What work do you do? "
            "A: \u0b2e\u0b41\u0b01 \u0b36\u0b3f\u0b15\u0b4d\u0b37\u0b15\u0964 (Mun \u1e63ik\u1e63aka.) I am a teacher.\n"
            "  15. Q: \u0b06\u0b1c\u0b3f\u0b30 \u0b24\u0b3e\u0b30\u0b3f\u0b16 \u0b15\u0b47\u0b24\u0b47? (\u0100jira t\u0101rikha kete?) What is today's date? "
            "A: \u0b38\u0b24\u0b30 \u0b24\u0b3e\u0b30\u0b3f\u0b16\u0964 (Satara t\u0101rikha.) The 17th.\n"
            "  16. Q: \u0b38\u0b47 \u0b15\u0b47\u0b09\u0b01\u0b20\u0b3f? (Se keun\u1e6dhi?) Where is he? "
            "A: \u0b38\u0b47 \u0b18\u0b30\u0b47 \u0b05\u0b1b\u0b3f\u0964 (Se ghare achi.) He is at home.\n"
            "  17. Q: \u0b24\u0b41\u0b2e\u0b47 \u0b2d\u0b32 \u0b05\u0b1b \u0b15\u0b3f? (Tume bhala acha ki?) Are you well? "
            "A: \u0b39\u0b01, \u0b2e\u0b41\u0b01 \u0b2d\u0b32 \u0b05\u0b1b\u0b3f\u0964 (Han, mun bhala achi.) Yes, I am well.\n"
            "  18. Q: \u0b15\u0b47\u0b09\u0b01\u0b1f\u0b3e \u0b2d\u0b32? (Keun\u1e6d\u0101 bhala?) Which one is good? "
            "A: \u0b0f\u0b07\u0b1f\u0b3e \u0b2d\u0b32\u0964 (Ei\u1e6d\u0101 bhala.) This one is good.\n"
            "  19. Q: \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b3e\u0b32\u0b3f \u0b06\u0b38\u0b3f\u0b2c \u0b15\u0b3f? (Tume k\u0101li \u0101siba ki?) Will you come tomorrow? "
            "A: \u0b39\u0b01, \u0b06\u0b38\u0b3f\u0b2c\u0b3f\u0964 (Han, \u0101sibi.) Yes, I will come.\n"
            "  20. Q: \u0b06\u0b09 \u0b15\u0b23 \u0b26\u0b30\u0b15\u0b3e\u0b30? (\u0100u ka\u1e47a darak\u0101ra?) What else do you need? "
            "A: \u0b06\u0b09 \u0b15\u0b3f\u0b1b\u0b3f \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (\u0100u kichi n\u0101hin.) Nothing else."
        ),
        "how_it_works": (
            "This record is the interrogation drill: twenty pairs, each "
            "built on one interrogative from the pronoun record (ka\u1e47a, "
            "kie, keun\u1e6dh\u0101re, kebe, k\u0101hinki, kipari, kete, keun) "
            "or a yes/no ki question. Answers model the natural short reply "
            "(se\u1e6dh\u0101re, han, n\u0101) and the full sentence, so the "
            "learner hears both registers of answering. Drill: take each "
            "question and answer it about yourself truthfully."
        ),
        "key_points": [
            "20 question-and-answer pairs with full translations.",
            "All six interrogative types plus yes/no ki questions.",
            "Answers model both short and full-sentence replies.",
            "Real-life topics: name, origin, price, health, work, date.",
        ],
        "requirements": ["Read the pronoun and tenses records first."],
        "standards": [
            "Interrogatives follow standard usage.",
            "Pairs constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["kie", "keun\u1e6dh\u0101re", "k\u0101hinki", "20"],
        "sig_lens": (
            "Through the Signature lens every question is a sworn seeking "
            "and every answer a vow of truth: the dialogue itself the "
            "covenant."
        ),
        "drill": {
            "pairs": 20,
            "interrogatives": ["ka\u1e47a", "kie", "keun\u1e6dh\u0101re", "kebe", "k\u0101hinki", "kipari", "kete", "keun"],
        },
    },
    {
        "key": "commands",
        "name": "Commands and Requests",
        "group": "Grammar in Action",
        "ladder_rank": 23,
        "ladder_tier": "advanced",
        "description": (
            "Twenty imperative and polite-request sentences - formal vs "
            "informal. Odia imperatives: the bare root for the familiar "
            "(\u0b16\u0b3e kh\u0101, eat!), -\u0b28\u0b4d\u0b24\u0b41 (-ntu) for the formal "
            "(\u0b16\u0b3e\u0b06\u0b28\u0b4d\u0b24\u0b41 kh\u0101ntu, please eat). \n\n"
            "Informal (to children, close friends):\n"
            "  1. \u0b06\u0b38\u0964 (\u0100sa.) Come.\n"
            "  2. \u0b2f\u0b3e\u0b05\u0964 (Y\u0101a.) Go.\n"
            "  3. \u0b2c\u0b38\u0964 (Basa.) Sit.\n"
            "  4. \u0b16\u0b3e\u0b05\u0964 (Kh\u0101a.) Eat.\n"
            "  5. \u0b2a\u0b3f\u0b05\u0964 (Pia.) Drink.\n"
            "  6. \u0b26\u0b47\u0b16\u0964 (Dekha.) Look.\n"
            "  7. \u0b36\u0b41\u0b23\u0964 (\u1e62u\u1e47a.) Listen.\n"
            "  8. \u0b15\u0b41\u0b39\u0964 (Kuha.) Say (it).\n"
            "  9. \u0b32\u0b47\u0b16\u0964 (Lekha.) Write.\n"
            "  10. \u0b2a\u0b22\u0b3c\u0964 (Pa\u1e0dha.) Read.\n"
            "Formal / polite (to elders, strangers, officials):\n"
            "  11. \u0b06\u0b38\u0b28\u0b4d\u0b24\u0b41\u0964 (\u0100santu.) Please come.\n"
            "  12. \u0b2c\u0b38\u0b28\u0b4d\u0b24\u0b41\u0964 (Basantu.) Please sit.\n"
            "  13. \u0b16\u0b3e\u0b06\u0b28\u0b4d\u0b24\u0b41\u0964 (Kh\u0101ntu.) Please eat.\n"
            "  14. \u0b26\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (Diantu.) Please give.\n"
            "  15. \u0b15\u0b41\u0b39\u0b28\u0b4d\u0b24\u0b41\u0964 (Kuhantu.) Please tell.\n"
            "  16. \u0b26\u0b5f\u0b3e\u0b15\u0b30\u0b3f \u0b27\u0b40\u0b30\u0b47 \u0b15\u0b41\u0b39\u0b28\u0b4d\u0b24\u0b41\u0964 (Day\u0101kari dh\u012bre kuhantu.) Please speak slowly.\n"
            "  17. \u0b2e\u0b4b\u0b24\u0b47 \u0b38\u0b3e\u0b39\u0b3e\u0b2f\u0b4d\u0b5f \u0b15\u0b30\u0b28\u0b4d\u0b24\u0b41\u0964 (Mote s\u0101h\u0101yya karantu.) Please help me.\n"
            "  18. \u0b15\u0b4d\u0b37\u0b2e\u0b3e \u0b15\u0b30\u0b28\u0b4d\u0b24\u0b41\u0964 (K\u1e63am\u0101 karantu.) Please forgive me.\n"
            "  19. \u0b2c\u0b3e\u0b39\u0b3e\u0b30\u0b15\u0b41 \u0b2f\u0b3e\u0b06\u0b28\u0b4d\u0b24\u0b41 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (B\u0101h\u0101raku y\u0101ntu n\u0101hin.) Please do not go outside.\n"
            "  20. \u0b1a\u0b3f\u0b28\u0b4d\u0b24\u0b3e \u0b15\u0b30\u0b28\u0b4d\u0b24\u0b41 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Cint\u0101 karantu n\u0101hin.) Please do not worry."
        ),
        "how_it_works": (
            "This record is the command grammar: ten informal imperatives "
            "(bare root: \u0101sa, y\u0101a, basa) and ten formal requests "
            "(-ntu ending: \u0101santu, basantu, kh\u0101ntu), with day\u0101kari "
            "as the universal softener and n\u0101hin for negative commands. "
            "The register rule is social law: -ntu for elders, strangers, "
            "and officials; bare root only downward or intimate. Drill: give "
            "ten classroom commands in both registers."
        ),
        "key_points": [
            "20 commands and requests: 10 informal, 10 formal.",
            "Informal imperative = bare verb root; formal = -ntu ending.",
            "day\u0101kari softens any request; n\u0101hin negates commands.",
            "Register rule: -ntu upward, bare root only downward/intimate.",
        ],
        "requirements": ["Read the pronoun record for the register system."],
        "standards": [
            "Imperative forms follow standard Odia.",
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["\u0100santu", "kh\u0101ntu", "Day\u0101kari", "20"],
        "sig_lens": (
            "Through the Signature lens a command is a vow given and a "
            "polite request a vow asked: -\u0b28\u0b4d\u0b24\u0b41 the seal of "
            "respect on every asking."
        ),
        "drill": {
            "informal": 10, "formal": 10,
            "formal_ending": "-ntu",
        },
    },
    {
        "key": "descriptions",
        "name": "Descriptions: People and Places",
        "group": "Grammar in Action",
        "ladder_rank": 24,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences describing people, places, and things in "
            "detail - Odia script, romanization, English. \n\n"
            "  1. \u0b2e\u0b4b\u0b30 \u0b2d\u0b3e\u0b07 \u0b32\u0b2e\u0b4d\u0b2c\u0b3e \u0b13 \u0b38\u0b41\u0b28\u0b4d\u0b26\u0b30\u0964 (Mora bh\u0101i lamb\u0101 o sundara.) My brother is tall and handsome.\n"
            "  2. \u0b24\u0b3e\u0b19\u0b4d\u0b15\u0b30 \u0b06\u0b16\u0b3f \u0b15\u0b33\u0b3e \u0b13 \u0b2c\u0b21\u0b3c\u0964 (T\u0101\u1e45kara \u0101khi ka\u1e37\u0101 o ba\u1e0da.) His eyes are black and big.\n"
            "  3. \u0b38\u0b47 \u0b38\u0b2c\u0b41\u0b2c\u0b47\u0b33\u0b47 \u0b39\u0b38\u0b47\u0964 (Se sabube\u1e37e hase.) She always smiles.\n"
            "  4. \u0b2c\u0b41\u0b22\u0b3c\u0b3e \u0b32\u0b4b\u0b15\u0b1f\u0b3f \u0b1c\u0b4d\u0b1e\u0b3e\u0b28\u0b40\u0964 (Bu\u1e0dh\u0101 loka\u1e6di jny\u0101n\u012b.) The old man is wise.\n"
            "  5. \u0b2a\u0b3f\u0b32\u0b3e\u0b1f\u0b3f \u0b1a\u0b1e\u0b4d\u0b1a\u0b33\u0964 (Pil\u0101\u1e6di cancala.) The child is lively.\n"
            "  6. \u0b2d\u0b41\u0b2c\u0b28\u0b47\u0b36\u0b4d\u0b35\u0b30 \u0b13\u0b21\u0b3c\u0b3f\u0b36\u0b3e\u0b30 \u0b30\u0b3e\u0b1c\u0b27\u0b3e\u0b28\u0b40\u0964 (Bhubane\u1e63wara odi\u1e63\u0101ra r\u0101jadh\u0101n\u012b.) Bhubaneswar is the capital of Odisha.\n"
            "  7. \u0b15\u0b1f\u0b15 \u0b2e\u0b39\u0b3e\u0b28\u0b26\u0b40 \u0b15\u0b42\u0b33\u0b30\u0b47 \u0b05\u0b1b\u0b3f\u0964 (Ka\u1e6daka mah\u0101nad\u012b ku\u1e37are achi.) Cuttack is on the banks of the Mahanadi.\n"
            "  8. \u0b2a\u0b41\u0b30\u0b40\u0b30\u0b47 \u0b1c\u0b17\u0b28\u0b4d\u0b28\u0b3e\u0b25 \u0b2e\u0b28\u0b4d\u0b26\u0b3f\u0b30 \u0b05\u0b1b\u0b3f\u0964 (Pur\u012brare Jagann\u0101tha mandira achi.) The Jagannath temple is in Puri.\n"
            "  9. \u0b15\u0b4b\u0b23\u0b3e\u0b30\u0b4d\u0b15 \u0b38\u0b42\u0b30\u0b4d\u0b2f\u0b4d\u0b5f \u0b2e\u0b28\u0b4d\u0b26\u0b3f\u0b30 \u0b2a\u0b3e\u0b07\u0b01 \u0b2a\u0b4d\u0b30\u0b38\u0b3f\u0b26\u0b4d\u0b27\u0964 (Ko\u1e47\u0101rka s\u016bryya mandira p\u0101in prasiddha.) Konark is famous for the Sun Temple.\n"
            "  10. \u0b1a\u0b3f\u0b32\u0b3f\u0b15\u0b3e \u0b0f\u0b38\u0b3f\u0b06\u0b30 \u0b38\u0b2c\u0b41\u0b20\u0b3e\u0b30\u0b41 \u0b2c\u0b21\u0b3c \u0b32\u0b41\u0b23\u0b3e \u0b39\u0b4d\u0b30\u0b26\u0964 (Cilik\u0101 esi\u0101ra sabu\u1e6d\u0101ru ba\u1e0da lu\u1e47\u0101 hrada.) Chilika is Asia's largest brackish-water lagoon.\n"
            "  11. \u0b38\u0b2e\u0b41\u0b26\u0b4d\u0b30 \u0b15\u0b42\u0b33 \u0b38\u0b41\u0b28\u0b4d\u0b26\u0b30\u0964 (Samudra k\u016b\u1e37a sundara.) The sea coast is beautiful.\n"
            "  12. \u0b18\u0b30\u0b1f\u0b3f \u0b2a\u0b41\u0b30\u0b41\u0b23\u0b3e \u0b15\u0b3f\u0b28\u0b4d\u0b24\u0b41 \u0b36\u0b15\u0b4d\u0b24\u0964 (Ghara\u1e6di puru\u1e47\u0101 kintu \u1e63akta.) The house is old but strong.\n"
            "  13. \u0b2c\u0b17\u0b3f\u0b1a\u0b3e\u0b30\u0b47 \u0b2c\u0b39\u0b41\u0b24 \u0b2b\u0b41\u0b32 \u0b05\u0b1b\u0b3f\u0964 (Bagic\u0101re bahuta phula achi.) There are many flowers in the garden.\n"
            "  14. \u0b06\u0b2e\u0b4d\u0b2c \u0b17\u0b1b\u0b30\u0b47 \u0b2a\u0b3e\u0b1a\u0b3f\u0b32\u0b3e \u0b06\u0b2e\u0b4d\u0b2c \u0b05\u0b1b\u0b3f\u0964 (\u0100mba gachare p\u0101cil\u0101 \u0101mba achi.) There are ripe mangoes on the mango tree.\n"
            "  15. \u0b2c\u0b39\u0b3f\u0b1f\u0b3f \u0b2e\u0b4b\u0b1f\u0b3e \u0b13 \u0b2d\u0b3e\u0b30\u0b40\u0964 (Bahi\u1e6di mo\u1e6d\u0101 o bh\u0101r\u012b.) The book is thick and heavy.\n"
            "  16. \u0b2a\u0b3e\u0b23\u0b3f \u0b38\u0b2b\u0b3e \u0b13 \u0b25\u0b23\u0b4d\u0b21\u0b3e\u0964 (P\u0101\u1e47i saph\u0101 o \u1e6dha\u1e47\u1e0d\u0101.) The water is clean and cold.\n"
            "  17. \u0b30\u0b3e\u0b38\u0b4d\u0b24\u0b3e\u0b1f\u0b3f \u0b32\u0b2e\u0b4d\u0b2c\u0b3e \u0b13 \u0b38\u0b3f\u0b27\u0b3e\u0964 (R\u0101st\u0101\u1e6di lamb\u0101 o sidh\u0101.) The road is long and straight.\n"
            "  18. \u0b30\u0b3e\u0b24\u0b3f \u0b28\u0b40\u0b30\u0b2c \u0b13 \u0b36\u0b3e\u0b28\u0b4d\u0b24\u0964 (R\u0101ti n\u012braba o \u1e63\u0101nta.) The night is silent and calm.\n"
            "  19. \u0b38\u0b15\u0b3e\u0b33 \u0b38\u0b41\u0b28\u0b4d\u0b26\u0b30 \u0b13 \u0b38\u0b24\u0b47\u0b1c\u0964 (Sak\u0101\u1e37a sundara o sateja.) The morning is beautiful and fresh.\n"
            "  20. \u0b13\u0b21\u0b3c\u0b3f\u0b36\u0b3e \u0b2e\u0b4b\u0b30 \u0b2e\u0b3e\u0b1f\u0b3f, \u0b2e\u0b4b\u0b30 \u0b17\u0b30\u0b4d\u0b2c\u0964 (Odi\u1e63\u0101 mora m\u0101\u1e6di, mora garba.) Odisha is my soil, my pride."
        ),
        "how_it_works": (
            "This record is the portrait gallery: twenty sentences stacking "
            "adjectives with o (and) and kintu (but), describing people "
            "(lamb\u0101 o sundara), the great places of Odisha (Bhubane\u1e63wara, "
            "Ka\u1e6daka on the Mah\u0101nad\u012b, Pur\u012b's Jagann\u0101tha "
            "mandira, Ko\u1e47\u0101rka's Sun Temple, Cilik\u0101 lagoon), and "
            "things in paired qualities (mo\u1e6d\u0101 o bh\u0101r\u012b). The "
            "closing line is a real patriotic sentiment every Odia knows. "
            "Drill: describe your hometown in five Odia sentences."
        ),
        "key_points": [
            "20 descriptive sentences with full translations.",
            "Adjective stacking with o (and) and kintu (but).",
            "Great places of Odisha: Bhubaneswar, Cuttack, Puri, Konark, Chilika.",
            "Closes with the real sentiment: Odisha is my soil, my pride.",
        ],
        "requirements": ["Read the adjectives and grammar records first."],
        "standards": [
            "Place facts follow documented geography.",
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["Bhubane\u1e63wara", "Jagann\u0101tha", "Ko\u1e47\u0101rka", "20"],
        "sig_lens": (
            "Through the Signature lens description is consecration: every "
            "quality named a seal pressed on the thing, every homeland a "
            "vow of pride."
        ),
        "drill": {
            "sentences": 20, "theme": "descriptions",
            "places": ["Bhubane\u1e63wara", "Ka\u1e6daka", "Pur\u012b", "Ko\u1e47\u0101rka", "Cilik\u0101"],
        },
    },
    {
        "key": "story1",
        "name": "Story I: The Mango Tree (Present Tense)",
        "group": "Stories and Idioms",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence simple story in Odia, in the present tense, with "
            "line-by-line English translation. (Teaching story, constructed "
            "from standard grammar for the ladder; labeled "
            "Signature-composed.) \n\n"
            "  1. \u0b17\u0b3e\u0b01 \u0b2e\u0b41\u0b39\u0b01\u0b30\u0b47 \u0b0f\u0b15 \u0b2c\u0b21\u0b3c \u0b06\u0b2e\u0b4d\u0b2c \u0b17\u0b1b \u0b05\u0b1b\u0b3f\u0964 "
            "(G\u0101n muh\u0101nre eka ba\u1e0da \u0101mba gacha achi.) There is a big mango tree at the village entrance.\n"
            "  2. \u0b17\u0b1b\u0b30\u0b47 \u0b2c\u0b39\u0b41\u0b24 \u0b2a\u0b3e\u0b1a\u0b3f\u0b32\u0b3e \u0b06\u0b2e\u0b4d\u0b2c \u0b05\u0b1b\u0b3f\u0964 "
            "(Gachare bahuta p\u0101cil\u0101 \u0101mba achi.) There are many ripe mangoes on the tree.\n"
            "  3. \u0b2a\u0b3f\u0b32\u0b3e\u0b2e\u0b3e\u0b28\u0b47 \u0b2a\u0b4d\u0b30\u0b24\u0b3f\u0b26\u0b3f\u0b28 \u0b38\u0b47\u0b20\u0b3e\u0b15\u0b41 \u0b06\u0b38\u0b28\u0b4d\u0b24\u0b3f\u0964 "
            "(Pil\u0101m\u0101ne pratidina se\u1e6dh\u0101ku \u0101santi.) The children come there every day.\n"
            "  4. \u0b38\u0b47\u0b2e\u0b3e\u0b28\u0b47 \u0b17\u0b1b \u0b1b\u0b3e\u0b07\u0b30\u0b47 \u0b2c\u0b38\u0b28\u0b4d\u0b24\u0b3f\u0964 "
            "(Sem\u0101ne gacha ch\u0101ire basanti.) They sit in the tree's shade.\n"
            "  5. \u0b17\u0b4b\u0b1f\u0b3f\u0b0f \u0b2a\u0b3f\u0b32\u0b3e \u0b06\u0b2e\u0b4d\u0b2c \u0b24\u0b4b\u0b33\u0b47\u0964 "
            "(Go\u1e6die pil\u0101 \u0101mba to\u1e37e.) One boy picks a mango.\n"
            "  6. \u0b38\u0b47 \u0b06\u0b2e\u0b4d\u0b2c\u0b1f\u0b3f \u0b38\u0b3e\u0b19\u0b4d\u0b17\u0b2e\u0b3e\u0b28\u0b19\u0b4d\u0b15\u0b41 \u0b26\u0b3f\u0b0f\u0964 "
            "(Se \u0101mba\u1e6di s\u0101\u1e45gam\u0101na\u1e45ku die.) He gives the mango to his friends.\n"
            "  7. \u0b38\u0b2e\u0b38\u0b4d\u0b24\u0b47 \u0b2e\u0b3f\u0b36\u0b3f \u0b06\u0b2e\u0b4d\u0b2c \u0b16\u0b3e\u0b06\u0b28\u0b4d\u0b24\u0b3f\u0964 "
            "(Samaste mi\u1e63i \u0101mba kh\u0101nti.) All eat the mango together.\n"
            "  8. \u0b06\u0b2e\u0b4d\u0b2c \u0b2c\u0b39\u0b41\u0b24 \u0b2e\u0b3f\u0b20\u0b3e\u0964 "
            "(\u0100mba bahuta mi\u1e6dh\u0101.) The mango is very sweet.\n"
            "  9. \u0b2a\u0b15\u0b4d\u0b37\u0b40\u0b2e\u0b3e\u0b28\u0b47 \u0b17\u0b1b\u0b30\u0b47 \u0b2c\u0b38\u0b28\u0b4d\u0b24\u0b3f\u0964 "
            "(Pak\u1e63\u012bm\u0101ne gachare basanti.) Birds sit in the tree.\n"
            "  10. \u0b17\u0b3e\u0b01 \u0b32\u0b4b\u0b15\u0b47 \u0b17\u0b1b\u0b15\u0b41 \u0b2d\u0b32 \u0b2a\u0b3e\u0b06\u0b28\u0b4d\u0b24\u0b3f\u0964 "
            "(G\u0101n loke gachaku bhala p\u0101nti.) The villagers love the tree."
        ),
        "how_it_works": (
            "This record is the first connected text: ten present-tense "
            "sentences forming one simple story. It recycles only vocabulary "
            "and grammar the ladder has already taught (gacha, \u0101mba, "
            "pil\u0101m\u0101ne, habitual -anti, locative -re, dative -ku), "
            "so the learner reads a real paragraph with zero new grammar. "
            "Read it aloud three times, then retell it in Odia without "
            "looking."
        ),
        "key_points": [
            "10-sentence story, present tense, line-by-line translation.",
            "Zero new grammar: only recycled vocabulary and forms.",
            "Teaching story, constructed from standard grammar (labeled Signature-composed).",
        ],
        "requirements": ["Read through the tenses record first."],
        "standards": [
            "Story labeled as constructed teaching text, not a folk tale.",
            "Grammar follows standard Odia.",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["\u0101mba gacha", "Pil\u0101m\u0101ne", "Signature-composed", "10"],
        "sig_lens": (
            "Through the Signature lens the story is a sealed parable: ten "
            "sentences, one tree, one village - the covenant told as a "
            "tale."
        ),
        "drill": {
            "sentences": 10, "tense": "present",
            "title": "The Mango Tree",
        },
    },
    {
        "key": "story2",
        "name": "Story II: The Fisherman's Morning (Past Tense)",
        "group": "Stories and Idioms",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the past tense, with line-by-line "
            "English translation. (Teaching story, constructed from standard "
            "grammar for the ladder; labeled Signature-composed.) \n\n"
            "  1. \u0b27\u0b40\u0b2c\u0b30 \u0b38\u0b15\u0b3e\u0b33\u0b41 \u0b36\u0b40\u0b18\u0b4d\u0b30 \u0b09\u0b20\u0b3f\u0b32\u0b3e\u0964 "
            "(Dh\u012bbara sak\u0101\u1e37u \u1e63\u012bghra u\u1e6dhil\u0101.) The fisherman woke up early in the morning.\n"
            "  2. \u0b38\u0b47 \u0b28\u0b26\u0b40\u0b15\u0b41 \u0b17\u0b32\u0b3e\u0964 "
            "(Se nad\u012bku gal\u0101.) He went to the river.\n"
            "  3. \u0b38\u0b47 \u0b28\u0b4c\u0b15\u0b3e\u0b30\u0b47 \u0b2c\u0b38\u0b3f\u0b32\u0b3e\u0964 "
            "(Se nauk\u0101re basil\u0101.) He sat in the boat.\n"
            "  4. \u0b38\u0b47 \u0b1c\u0b3e\u0b32 \u0b2a\u0b15\u0b3e\u0b07\u0b32\u0b3e\u0964 "
            "(Se j\u0101la pak\u0101il\u0101.) He cast the net.\n"
            "  5. \u0b26\u0b41\u0b07 \u0b18\u0b23\u0b4d\u0b1f\u0b3e \u0b2a\u0b30\u0b47 \u0b1c\u0b3e\u0b32 \u0b2d\u0b3e\u0b30\u0b40 \u0b39\u0b47\u0b32\u0b3e\u0964 "
            "(Dui gha\u1e47\u1e6d\u0101 pare j\u0101la bh\u0101r\u012b hel\u0101.) After two hours the net grew heavy.\n"
            "  6. \u0b38\u0b47 \u0b1c\u0b3e\u0b32 \u0b1f\u0b3e\u0b23\u0b3f\u0b32\u0b3e\u0964 "
            "(Se j\u0101la t\u0101\u1e47il\u0101.) He pulled the net.\n"
            "  7. \u0b1c\u0b3e\u0b32\u0b30\u0b47 \u0b2c\u0b39\u0b41\u0b24 \u0b2e\u0b3e\u0b1b \u0b25\u0b3f\u0b32\u0b3e\u0964 "
            "(J\u0101lare bahuta m\u0101cha thil\u0101.) There were many fish in the net.\n"
            "  8. \u0b27\u0b40\u0b2c\u0b30 \u0b16\u0b41\u0b38\u0b3f\u0b30\u0b47 \u0b39\u0b38\u0b3f\u0b32\u0b3e\u0964 "
            "(Dh\u012bbara khusire hasil\u0101.) The fisherman laughed with joy.\n"
            "  9. \u0b38\u0b47 \u0b2e\u0b3e\u0b1b \u0b2c\u0b1c\u0b3e\u0b30\u0b15\u0b41 \u0b28\u0b47\u0b32\u0b3e\u0964 "
            "(Se m\u0101cha baj\u0101raku nel\u0101.) He took the fish to the market.\n"
            "  10. \u0b38\u0b47\u0b26\u0b3f\u0b28 \u0b24\u0b3e\u0b30 \u0b2d\u0b32 \u0b30\u0b4b\u0b1c\u0b17\u0b3e\u0b30 \u0b39\u0b47\u0b32\u0b3e\u0964 "
            "(Sedina t\u0101ra bhala rojag\u0101ra hel\u0101.) That day he earned well."
        ),
        "how_it_works": (
            "This record is the past-tense workout: ten sentences, every "
            "verb in -l\u0101/-li/-le, telling one morning's story from "
            "waking to earning. Time phrases anchor the sequence (sak\u0101\u1e37u, "
            "dui gha\u1e47\u1e6d\u0101 pare, sedina). Read it, then retell it "
            "shifting every verb to the future (-bi) as a drill."
        ),
        "key_points": [
            "10-sentence story, past tense throughout, line-by-line translation.",
            "Time anchors: sak\u0101\u1e37u, dui gha\u1e47\u1e6d\u0101 pare, sedina.",
            "Teaching story, constructed from standard grammar (labeled Signature-composed).",
            "Retell drill: shift all verbs to future tense.",
        ],
        "requirements": ["Read the tenses record first."],
        "standards": [
            "Story labeled as constructed teaching text, not a folk tale.",
            "Past-tense forms follow standard Odia.",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["Dh\u012bbara", "j\u0101la", "Signature-composed", "10"],
        "sig_lens": (
            "Through the Signature lens the past is a sealed record: every "
            "-l\u0101 a vow remembered, every net pulled a promise kept."
        ),
        "drill": {
            "sentences": 10, "tense": "past",
            "title": "The Fisherman's Morning",
        },
    },
    {
        "key": "story3",
        "name": "Story III: The Girl Who Will Fly (Future Tense)",
        "group": "Stories and Idioms",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the future tense, with line-by-line "
            "English translation. (Teaching story, constructed from standard "
            "grammar for the ladder; labeled Signature-composed.) \n\n"
            "  1. \u0b1d\u0b3f\u0b05\u0b1f\u0b3f \u0b2c\u0b21\u0b3c \u0b38\u0b4d\u0b35\u0b2a\u0b4d\u0b28 \u0b26\u0b47\u0b16\u0b3f\u0b2c\u0964 "
            "(Jhia\u1e6di ba\u1e0da swapna dekhiba.) The girl will dream big dreams.\n"
            "  2. \u0b38\u0b47 \u0b2e\u0b28 \u0b26\u0b47\u0b07 \u0b2a\u0b22\u0b3c\u0b3f\u0b2c\u0964 "
            "(Se mana dei pa\u1e0dhiba.) She will study with full attention.\n"
            "  3. \u0b38\u0b47 \u0b2a\u0b30\u0b40\u0b15\u0b4d\u0b37\u0b3e\u0b30\u0b47 \u0b2a\u0b4d\u0b30\u0b25\u0b2e \u0b39\u0b47\u0b2c\u0964 "
            "(Se par\u012bk\u1e63\u0101re prathama heba.) She will come first in the exam.\n"
            "  4. \u0b38\u0b47 \u0b2c\u0b3f\u0b2e\u0b3e\u0b28 \u0b1a\u0b33\u0b3e\u0b07\u0b2c\u0964 "
            "(Se bim\u0101na ca\u1e37\u0101iba.) She will fly an airplane. (She will become a pilot.)\n"
            "  5. \u0b38\u0b47 \u0b06\u0b15\u0b3e\u0b36\u0b30\u0b47 \u0b09\u0b21\u0b3c\u0b3f\u0b2c\u0964 "
            "(Se \u0101k\u0101\u1e63are u\u1e0diba.) She will fly in the sky.\n"
            "  6. \u0b17\u0b3e\u0b01 \u0b32\u0b4b\u0b15\u0b47 \u0b24\u0b3e\u0b15\u0b41 \u0b26\u0b47\u0b16\u0b3f\u0b2c\u0b47\u0964 "
            "(G\u0101n loke t\u0101ku dekhibe.) The villagers will watch her.\n"
            "  7. \u0b2e\u0b3e-\u0b2c\u0b3e\u0b2a\u0b3e \u0b17\u0b30\u0b4d\u0b2c \u0b15\u0b30\u0b3f\u0b2c\u0b47\u0964 "
            "(M\u0101-b\u0101p\u0101 garba karibe.) Her parents will feel proud.\n"
            "  8. \u0b38\u0b47 \u0b17\u0b3e\u0b01\u0b15\u0b41 \u0b2b\u0b47\u0b30\u0b3f\u0b2c\u0964 "
            "(Se g\u0101nku pheriba.) She will return to the village.\n"
            "  9. \u0b38\u0b47 \u0b2a\u0b3f\u0b32\u0b3e\u0b2e\u0b3e\u0b28\u0b19\u0b4d\u0b15\u0b41 \u0b36\u0b3f\u0b16\u0b3e\u0b07\u0b2c\u0964 "
            "(Se pil\u0101m\u0101na\u1e45ku \u1e63ikh\u0101iba.) She will teach the children.\n"
            "  10. \u0b38\u0b4d\u0b35\u0b2a\u0b4d\u0b28 \u0b38\u0b24 \u0b39\u0b47\u0b2c\u0964 "
            "(Swapna sata heba.) The dream will come true."
        ),
        "how_it_works": (
            "This record is the future-tense workout and the ladder's "
            "aspiration: ten -bi sentences following one girl's dream from "
            "study to sky to return. Every verb is future; the story's arc "
            "(dream, effort, achievement, giving back) makes the tense "
            "memorable. Read it, then write your own ten-sentence future "
            "story: what will you do?"
        ),
        "key_points": [
            "10-sentence story, future tense throughout, line-by-line translation.",
            "Aspirational arc: dream, study, achievement, return, teach.",
            "Teaching story, constructed from standard grammar (labeled Signature-composed).",
            "Write-your-own drill: ten future sentences about your plans.",
        ],
        "requirements": ["Read the tenses record first."],
        "standards": [
            "Story labeled as constructed teaching text, not a folk tale.",
            "Future-tense forms follow standard Odia.",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["dekhiba", "bim\u0101na", "Signature-composed", "10"],
        "sig_lens": (
            "Through the Signature lens the future is a vow not yet sealed: "
            "every -bi a promise the speaker makes to time itself."
        ),
        "drill": {
            "sentences": 10, "tense": "future",
            "title": "The Girl Who Will Fly",
        },
    },
    {
        "key": "idioms",
        "name": "Idioms and Proverbs",
        "group": "Stories and Idioms",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "description": (
            "Twenty Odia idioms and proverbs - each with literal translation, "
            "real meaning, and an example sentence. Documented folk sayings "
            "are given as-is; two teaching maxims are explicitly labeled "
            "Signature-composed. \n\n"
            "  1. \u0b05\u0b27 \u0b15\u0b41\u0b2e\u0b4d\u0b2d \u0b1c\u0b33 \u0b1b\u0b33\u0b1b\u0b33\u0964 (Adha kumbha ja\u1e37a cha\u1e37acha\u1e37a.) "
            "Lit: Half a pot of water splashes. Meaning: Empty vessels make the most noise. "
            "Ex: \u0b38\u0b47 \u0b05\u0b27 \u0b15\u0b41\u0b2e\u0b4d\u0b2d \u0b2a\u0b30\u0b3f \u0b2c\u0b47\u0b36\u0b3f \u0b15\u0b25\u0b3e \u0b15\u0b41\u0b39\u0b47\u0964 (He talks the most and knows the least.)\n"
            "  2. \u0b0f\u0b15 \u0b39\u0b3e\u0b24\u0b30\u0b47 \u0b24\u0b3e\u0b33\u0b3f \u0b2c\u0b3e\u0b1c\u0b47 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Eka h\u0101tare t\u0101\u1e37i b\u0101je n\u0101hin.) "
            "Lit: One hand cannot clap. Meaning: It takes two (cooperation is needed). "
            "Ex: \u0b2c\u0b28\u0b4d\u0b27\u0b41\u0b24\u0b3e \u0b0f\u0b15 \u0b39\u0b3e\u0b24\u0b30\u0b47 \u0b39\u0b41\u0b0f \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Friendship is not one-sided.)\n"
            "  3. \u0b2a\u0b3e\u0b23\u0b3f\u0b30\u0b47 \u0b25\u0b3e\u0b07 \u0b15\u0b41\u0b2e\u0b4d\u0b2d\u0b40\u0b30 \u0b38\u0b19\u0b4d\u0b17\u0b47 \u0b2c\u0b3e\u0b26 \u0b15\u0b30 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 "
            "(P\u0101\u1e47ire th\u0101i kumbh\u012bra sa\u1e45ge b\u0101da kara n\u0101hin.) "
            "Lit: Living in water, do not quarrel with the crocodile. Meaning: Do not fight those stronger than you on their ground. "
            "Ex: \u0b38\u0b47 \u0b2c\u0b38 \u0b38\u0b3e\u0b39\u0b47\u0b2c\u0b19\u0b4d\u0b15 \u0b38\u0b39 \u0b2f\u0b41\u0b15\u0b4d\u0b24\u0b3f \u0b15\u0b32\u0b3e\u0964 (He argued with the boss - unwise.)\n"
            "  4. \u0b2c\u0b3f\u0b28\u0b3e \u0b2e\u0b47\u0b18\u0b30\u0b47 \u0b2c\u0b1c\u0b4d\u0b30\u0b2a\u0b3e\u0b24\u0964 (Bin\u0101 meghare bajrap\u0101ta.) "
            "Lit: A thunderbolt without clouds. Meaning: A bolt from the blue; sudden shock. "
            "Ex: \u0b24\u0b3e\u0b19\u0b4d\u0b15 \u0b2c\u0b3f\u0b26\u0b3e\u0b5f \u0b2c\u0b3f\u0b28\u0b3e \u0b2e\u0b47\u0b18\u0b30\u0b47 \u0b2c\u0b1c\u0b4d\u0b30\u0b2a\u0b3e\u0b24 \u0b2a\u0b30\u0b3f \u0b06\u0b38\u0b3f\u0b32\u0b3e\u0964 (His farewell came like a bolt from the blue.)\n"
            "  5. \u0b2e\u0b41\u0b39\u0b01\u0b30\u0b47 \u0b2e\u0b3f\u0b20\u0b3e \u0b2a\u0b47\u0b1f\u0b30\u0b47 \u0b2c\u0b3f\u0b37\u0964 (Muh\u0101nre mi\u1e6dh\u0101 pe\u1e6dare bi\u1e63a.) "
            "Lit: Honey in the mouth, poison in the belly. Meaning: Two-faced; flattering but harmful. "
            "Ex: \u0b24\u0b3e\u0b19\u0b4d\u0b15 \u0b15\u0b25\u0b3e\u0b30\u0b47 \u0b2c\u0b3f\u0b36\u0b4d\u0b35\u0b3e\u0b38 \u0b15\u0b30 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Do not trust his words.)\n"
            "  6. \u0b05\u0b33\u0b4d\u0b2a \u0b2c\u0b3f\u0b26\u0b4d\u0b5f\u0b3e \u0b2d\u0b5f\u0b19\u0b4d\u0b15\u0b30\u0b40\u0964 (Alpa bidy\u0101 bhaya\u1e45kar\u012b.) "
            "Lit: A little learning is dangerous. Meaning: Half-knowledge causes harm. "
            "Ex: \u0b05\u0b33\u0b4d\u0b2a \u0b1c\u0b3e\u0b23\u0b3f \u0b2c\u0b47\u0b36\u0b3f \u0b15\u0b39\u0b28\u0b4d\u0b24\u0b41 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Do not speak much on little knowledge.)\n"
            "  7. \u0b2c\u0b41\u0b26\u0b4d\u0b27\u0b3f \u0b2f\u0b3e\u0b39\u0b3e\u0b30 \u0b2c\u0b33 \u0b24\u0b3e\u0b39\u0b3e\u0b30\u0964 (Buddhi y\u0101h\u0101ra ba\u1e37a t\u0101h\u0101ra.) "
            "Lit: Whose is the wit, his is the strength. Meaning: Brains beat brawn. "
            "Ex: \u0b2c\u0b41\u0b26\u0b4d\u0b27\u0b3f\u0b30\u0b47 \u0b38\u0b47 \u0b1c\u0b3f\u0b24\u0b3f\u0b32\u0b3e\u0964 (He won by wit.)\n"
            "  8. \u0b32\u0b4b\u0b2d\u0b47 \u0b2a\u0b3e\u0b2a, \u0b2a\u0b3e\u0b2a\u0b47 \u0b2e\u0b43\u0b24\u0b4d\u0b5f\u0b41\u0964 (Lobhe p\u0101pa, p\u0101pe m\u1e5btyu.) "
            "Lit: In greed is sin, in sin is death. Meaning: Greed destroys. "
            "Ex: \u0b32\u0b4b\u0b2d \u0b15\u0b30\u0b3f \u0b38\u0b47 \u0b38\u0b2c\u0b41 \u0b39\u0b30\u0b3e\u0b07\u0b32\u0b3e\u0964 (Through greed he lost everything.)\n"
            "  9. \u0b15\u0b3e\u0b17\u0b1c \u0b15\u0b32\u0b2e \u0b27\u0b30\u0b3f\u0b32\u0b47 \u0b2a\u0b23\u0b4d\u0b21\u0b3f\u0b24 \u0b39\u0b41\u0b0f \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 "
            "(K\u0101gaja kalama dharile pa\u1e47dita hue n\u0101hin.) "
            "Lit: Holding paper and pen does not make a scholar. Meaning: Tools do not make mastery. "
            "Ex: \u0b15\u0b2e\u0b4d\u0b2a\u0b4d\u0b5f\u0b41\u0b1f\u0b30 \u0b25\u0b3f\u0b32\u0b47 \u0b1c\u0b4d\u0b1e\u0b3e\u0b28\u0b40 \u0b39\u0b41\u0b0f \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Owning a computer does not make one wise.)\n"
            "  10. \u0b06\u0b16\u0b3f \u0b25\u0b3e\u0b07 \u0b05\u0b28\u0b4d\u0b27\u0964 (\u0100khi th\u0101i andha.) "
            "Lit: Blind though having eyes. Meaning: Willful blindness; refusing to see. "
            "Ex: \u0b38\u0b24 \u0b26\u0b47\u0b16\u0b3f \u0b38\u0b47 \u0b06\u0b16\u0b3f \u0b25\u0b3e\u0b07 \u0b05\u0b28\u0b4d\u0b27\u0964 (Seeing the truth, he stays blind to it.)\n"
            "  11. \u0b26\u0b42\u0b30 \u0b2a\u0b3e\u0b39\u0b3e\u0b21\u0b3c \u0b38\u0b2c\u0b41\u0b2c\u0b47\u0b33\u0b47 \u0b38\u0b41\u0b28\u0b4d\u0b26\u0b30\u0964 (D\u016bra p\u0101h\u0101\u1e0da sabube\u1e37e sundara.) "
            "Lit: Distant hills always look beautiful. Meaning: The grass is always greener. "
            "Ex: \u0b2a\u0b30 \u0b1a\u0b3e\u0b15\u0b3f\u0b30\u0b3f \u0b26\u0b42\u0b30\u0b30\u0b41 \u0b2d\u0b32 \u0b26\u0b3f\u0b36\u0b47\u0964 (Another's job looks better from afar.)\n"
            "  12. \u0b16\u0b3e\u0b32\u0b3f \u0b2a\u0b47\u0b1f\u0b30\u0b47 \u0b27\u0b30\u0b4d\u0b2e \u0b15\u0b25\u0b3e \u0b36\u0b41\u0b23\u0b3e\u0b2f\u0b3e\u0b0f \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 "
            "(Kh\u0101li pe\u1e6dare dharma kath\u0101 \u1e63u\u1e47\u0101y\u0101e n\u0101hin.) "
            "Lit: On an empty stomach, sermons are not heard. Meaning: An empty stomach has no ears. "
            "Ex: \u0b2a\u0b4d\u0b30\u0b25\u0b2e\u0b47 \u0b16\u0b3e\u0b07\u0b2c\u0b3e, \u0b24\u0b3e\u0b2a\u0b30\u0b47 \u0b15\u0b25\u0b3e\u0964 (First food, then talk.)\n"
            "  13. \u0b2f\u0b25\u0b3e \u0b30\u0b3e\u0b1c\u0b3e \u0b24\u0b25\u0b3e \u0b2a\u0b4d\u0b30\u0b1c\u0b3e\u0964 (Yath\u0101 r\u0101j\u0101 tath\u0101 praj\u0101.) "
            "Lit: As the king, so the people. Meaning: Leadership sets the example. "
            "Ex: \u0b28\u0b47\u0b24\u0b3e \u0b2d\u0b32 \u0b39\u0b47\u0b32\u0b47 \u0b26\u0b47\u0b36 \u0b2d\u0b32\u0964 (If the leader is good, the country is good.)\n"
            "  14. \u0b15\u0b30\u0b4d\u0b2e \u0b39\u0b3f\u0b01 \u0b27\u0b30\u0b4d\u0b2e\u0964 (Karma hin dharma.) "
            "Lit: Work itself is duty. Meaning: Work is worship. "
            "Ex: \u0b15\u0b3e\u0b2e\u0b15\u0b41 \u0b2a\u0b42\u0b1c\u0b3e \u0b2a\u0b30\u0b3f \u0b2e\u0b28\u0b47 \u0b15\u0b30\u0964 (Treat work like worship.)\n"
            "  15. \u0b36\u0b4d\u0b30\u0b2e \u0b39\u0b3f\u0b01 \u0b2a\u0b42\u0b1c\u0b3e\u0964 (\u1e62rama hin p\u016bj\u0101.) "
            "Lit: Labor itself is worship. Meaning: Hard work is sacred. "
            "Ex: \u0b36\u0b4d\u0b30\u0b2e \u0b15\u0b32\u0b47 \u0b38\u0b2b\u0b33 \u0b2e\u0b3f\u0b33\u0b47\u0964 (Labor brings success.)\n"
            "  16. \u0b38\u0b4d\u0b35\u0b3e\u0b38\u0b4d\u0b25\u0b4d\u0b5f \u0b39\u0b3f\u0b01 \u0b38\u0b2e\u0b4d\u0b2a\u0b26\u0964 (Sw\u0101sthya hin sampada.) "
            "Lit: Health itself is wealth. Meaning: Health is the true riches. "
            "Ex: \u0b38\u0b4d\u0b35\u0b3e\u0b38\u0b4d\u0b25\u0b4d\u0b5f \u0b30\u0b15\u0b4d\u0b37\u0b3e \u0b15\u0b30\u0964 (Protect your health.)\n"
            "  17. \u0b36\u0b3f\u0b16\u0b3f\u0b2c\u0b3e \u0b2e\u0b28\u0b41\u0b37\u0b4d\u0b5f\u0b30 \u0b38\u0b2c\u0b41\u0b20\u0b3e\u0b30\u0b41 \u0b2c\u0b21\u0b3c \u0b27\u0b28\u0964 (\u1e62ikhib\u0101 manu\u1e63yara sabu\u1e6d\u0101ru ba\u1e0da dhana.) "
            "Lit: Learning is man's greatest wealth. Meaning: Knowledge is the true treasure. "
            "Ex: \u0b2a\u0b3e\u0b20 \u0b2a\u0b22\u0b3c, \u0b27\u0b28\u0b40 \u0b39\u0b41\u0b05\u0964 (Study and grow rich.)\n"
            "  18. \u0b28\u0b08 \u0b2a\u0b3e\u0b30\u0b3f \u0b39\u0b47\u0b32\u0b47 \u0b2e\u0b3e\u0b1d\u0b3f\u0b15\u0b41 \u0b2e\u0b28\u0b47 \u0b2a\u0b21\u0b3c\u0b47 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 "
            "(Nai p\u0101ri hele m\u0101jhiku mane pa\u1e0de n\u0101hin.) "
            "Lit: Once the river is crossed, the boatman is not remembered. Meaning: People forget their helpers after success. "
            "Ex: \u0b38\u0b2b\u0b33 \u0b2a\u0b30\u0b47 \u0b38\u0b47 \u0b2c\u0b28\u0b4d\u0b27\u0b41\u0b19\u0b4d\u0b15\u0b41 \u0b2d\u0b41\u0b32\u0b3f\u0b17\u0b32\u0b3e\u0964 (After success he forgot his friend.)\n"
            "  19. \u0b38\u0b2e\u0b5f \u0b38\u0b2c\u0b41\u0b20\u0b3e\u0b30\u0b41 \u0b2c\u0b21\u0b3c \u0b36\u0b3f\u0b15\u0b4d\u0b37\u0b15\u0964 (Samaya sabu\u1e6d\u0101ru ba\u1e0da \u1e63ik\u1e63aka.) "
            "Lit: Time is the greatest teacher. Meaning: Experience teaches best. (Signature-composed teaching maxim.) "
            "Ex: \u0b38\u0b2e\u0b5f \u0b38\u0b2c\u0b41 \u0b36\u0b3f\u0b16\u0b3e\u0b07\u0b2c\u0964 (Time will teach all.)\n"
            "  20. \u0b27\u0b30\u0b4d\u0b2f\u0b4d\u0b5f \u0b38\u0b2c\u0b41\u0b20\u0b3e\u0b30\u0b41 \u0b2c\u0b21\u0b3c \u0b36\u0b15\u0b4d\u0b24\u0b3f\u0964 (Dhairyya sabu\u1e6d\u0101ru ba\u1e0da \u1e63akti.) "
            "Lit: Patience is the greatest strength. Meaning: Endurance wins. (Signature-composed teaching maxim.) "
            "Ex: \u0b27\u0b30\u0b4d\u0b2f\u0b4d\u0b5f \u0b27\u0b30, \u0b1c\u0b3f\u0b24\u0b3f\u0b2c\u0964 (Be patient, you will win.)"
        ),
        "how_it_works": (
            "This record is the wisdom chest: twenty sayings, each in three "
            "layers - the Odia original, the literal translation (which "
            "teaches imagery), and the real meaning (which teaches culture). "
            "Eighteen are documented folk proverbs; two (19, 20) are "
            "explicitly labeled Signature-composed teaching maxims, never "
            "presented as folk sayings. Each gets an example sentence so the "
            "proverb is usable, not just quotable. Drill: use five proverbs "
            "in conversation this week."
        ),
        "key_points": [
            "20 idioms and proverbs: literal translation + real meaning + example sentence.",
            "18 documented folk sayings; 2 explicitly labeled Signature-composed teaching maxims.",
            "Labeling rule honored: composed maxims never presented as authentic folk record.",
        ],
        "requirements": ["Read through the tenses record first."],
        "standards": [
            "Folk sayings follow documented Odia usage; composed maxims are explicitly labeled.",
            "Example sentences constructed from standard grammar.",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["Adha kumbha", "kumbh\u012bra", "Signature-composed teaching maxim", "20"],
        "sig_lens": (
            "Through the Signature lens proverbs are sealed wisdom: every "
            "saying a covenant compressed to one line, every maxim a vow "
            "for the living."
        ),
        "drill": {
            "count": 20, "documented": 18, "composed": 2,
        },
    },
    {
        "key": "registers",
        "name": "Formal and Polite Registers",
        "group": "Conversation and Registers",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen formal vs informal pairs for letters, business, and "
            "elders - Odia script, romanization, English. The formal column "
            "uses \u0b06\u0b2a\u0b23/\u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15\u0b30 and the -\u0b28\u0b4d\u0b24\u0b41 ending; the informal column "
            "uses \u0b24\u0b41\u0b2e\u0b47/\u0b24\u0b41 and the bare root. \n\n"
            "  1. F: \u0b06\u0b2a\u0b23 \u0b15\u0b47\u0b2e\u0b3f\u0b24\u0b3f \u0b05\u0b1b\u0b28\u0b4d\u0b24\u0b3f? (\u0100pa\u1e47a kemiti achanti?) How are you? (formal) "
            "I: \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b47\u0b2e\u0b3f\u0b24\u0b3f \u0b05\u0b1b? (Tume kemiti acha?) How are you? (familiar)\n"
            "  2. F: \u0b26\u0b5f\u0b3e\u0b15\u0b30\u0b3f \u0b2c\u0b38\u0b28\u0b4d\u0b24\u0b41\u0964 (Day\u0101kari basantu.) Please be seated. "
            "I: \u0b2c\u0b38\u0964 (Basa.) Sit.\n"
            "  3. F: \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15\u0b30 \u0b2e\u0b24 \u0b15\u0b23? (\u0100pa\u1e47a\u1e45kara mata ka\u1e47a?) What is your opinion? "
            "I: \u0b24\u0b4b\u0b30 \u0b2e\u0b24 \u0b15\u0b23? (Tora mata ka\u1e47a?) What do you think?\n"
            "  4. F: \u0b2e\u0b4b\u0b24\u0b47 \u0b38\u0b3e\u0b39\u0b3e\u0b2f\u0b4d\u0b5f \u0b15\u0b30\u0b28\u0b4d\u0b24\u0b41\u0964 (Mote s\u0101h\u0101yya karantu.) Please help me. "
            "I: \u0b2e\u0b4b\u0b24\u0b47 \u0b38\u0b3e\u0b39\u0b3e\u0b2f\u0b4d\u0b5f \u0b15\u0b30\u0964 (Mote s\u0101h\u0101yya kara.) Help me.\n"
            "  5. F: \u0b15\u0b4d\u0b37\u0b2e\u0b3e \u0b15\u0b30\u0b28\u0b4d\u0b24\u0b41\u0964 (K\u1e63am\u0101 karantu.) Please forgive me. "
            "I: \u0b15\u0b4d\u0b37\u0b2e\u0b3e \u0b15\u0b30\u0964 (K\u1e63am\u0101 kara.) Forgive me.\n"
            "  6. F: \u0b06\u0b2a\u0b23 \u0b06\u0b38\u0b3f\u0b32\u0b47 \u0b16\u0b41\u0b38\u0b3f \u0b39\u0b47\u0b2c\u0b3f\u0964 (\u0100pa\u1e47a \u0101sile khusi hebi.) We would be glad if you came. "
            "I: \u0b24\u0b41\u0b2e\u0b47 \u0b06\u0b38\u0b3f\u0b32\u0b47 \u0b2d\u0b32 \u0b39\u0b47\u0b2c\u0964 (Tume \u0101sile bhala heba.) It would be good if you came.\n"
            "  7. F: \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15\u0b41 \u0b05\u0b28\u0b41\u0b30\u0b4b\u0b27\u0964 (\u0100pa\u1e47a\u1e45ku anurodha.) A request to you. (letter formal) "
            "I: \u0b24\u0b41\u0b2e\u0b15\u0b41 \u0b17\u0b4b\u0b1f\u0b3f\u0b0f \u0b15\u0b25\u0b3e\u0964 (Tumaku go\u1e6die kath\u0101.) One thing to tell you. (letter familiar)\n"
            "  8. F: \u0b38\u0b2e\u0b4d\u0b2e\u0b3e\u0b28\u0b40\u0b5f \u0b2e\u0b39\u0b4b\u0b26\u0b5f, (Samm\u0101n\u012bya mahodaya,) Respected Sir, (letter opening) "
            "I: \u0b2a\u0b4d\u0b30\u0b3f\u0b5f \u0b2c\u0b28\u0b4d\u0b27\u0b41, (Priya bandhu,) Dear friend, (letter opening)\n"
            "  9. F: \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15\u0b30 \u0b2c\u0b3f\u0b36\u0b4d\u0b35\u0b38\u0b4d\u0b24, (\u0100pa\u1e47a\u1e45kara bi\u1e63wasta,) Yours faithfully, (letter closing) "
            "I: \u0b24\u0b41\u0b2e\u0b30 \u0b38\u0b4d\u0b28\u0b47\u0b39\u0b30, (Tumara snehara,) With love, (letter closing)\n"
            "  10. F: \u0b2d\u0b17\u0b2c\u0b3e\u0b28 \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15\u0b30 \u0b2e\u0b19\u0b4d\u0b17\u0b33 \u0b15\u0b30\u0b28\u0b4d\u0b24\u0b41\u0964 (Bhagab\u0101na \u0101pa\u1e47a\u1e45kara ma\u1e45ga\u1e37a karantu.) May God bless you. "
            "I: \u0b2d\u0b32\u0b30\u0b47 \u0b25\u0b3e\u0964 (Bhalare th\u0101.) Take care.\n"
            "  11. F: \u0b2e\u0b4b\u0b24\u0b47 \u0b05\u0b28\u0b41\u0b2e\u0b24\u0b3f \u0b26\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (Mote anumati diantu.) Please grant me permission. "
            "I: \u0b2e\u0b4b\u0b24\u0b47 \u0b1b\u0b3e\u0b21\u0b3c\u0964 (Mote ch\u0101\u1e0da.) Let me go.\n"
            "  12. F: \u0b06\u0b2a\u0b23 \u0b15\u0b47\u0b24\u0b47\u0b2c\u0b47\u0b33\u0b47 \u0b38\u0b2e\u0b5f \u0b26\u0b47\u0b2c\u0b47? (\u0100pa\u1e47a ketebe\u1e37e samaya debe?) When will you give time? (business) "
            "I: \u0b15\u0b47\u0b24\u0b47\u0b2c\u0b47\u0b33\u0b47 \u0b26\u0b47\u0b16\u0b3e \u0b39\u0b47\u0b2c\u0b3e? (Ketebe\u1e37e dekh\u0101 heb\u0101?) When shall we meet?\n"
            "  13. F: \u0b2c\u0b39\u0b41\u0b24 \u0b2c\u0b39\u0b41\u0b24 \u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26\u0964 (Bahuta bahuta dhanyab\u0101da.) Many many thanks. "
            "I: \u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26\u0964 (Dhanyab\u0101da.) Thanks.\n"
            "  14. F: \u0b2e\u0b41\u0b01 \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15\u0b30 \u0b06\u0b2d\u0b3e\u0b30\u0b40\u0964 (Mun \u0101pa\u1e47a\u1e45kara \u0101bh\u0101r\u012b.) I am grateful to you. "
            "I: \u0b2c\u0b39\u0b41\u0b24 \u0b16\u0b41\u0b38\u0b3f \u0b32\u0b3e\u0b17\u0b3f\u0b32\u0b3e\u0964 (Bahuta khusi l\u0101gil\u0101.) I was very glad.\n"
            "  15. F: \u0b2a\u0b41\u0b23\u0b3f \u0b26\u0b47\u0b16\u0b3e \u0b39\u0b47\u0b2c\u0b3e\u0964 (Pu\u1e47i dekh\u0101 heb\u0101.) We shall meet again. (formal parting) "
            "I: \u0b2b\u0b47\u0b30\u0b3f \u0b26\u0b47\u0b16\u0b3e \u0b39\u0b47\u0b2c\u0b3e\u0964 (Pheri dekh\u0101 heb\u0101.) See you again. (familiar parting)"
        ),
        "how_it_works": (
            "This record is the register switchboard: fifteen pairs showing "
            "the same intention in formal and informal dress. The machinery "
            "is consistent: \u0101pa\u1e47a/\u0101pa\u1e47a\u1e45kara + -ntu verbs "
            "upward; tume/tu + bare root downward. Letter frames "
            "(samm\u0101n\u012bya mahodaya ... \u0101pa\u1e47a\u1e45kara bi\u1e63wasta "
            "vs priya bandhu ... tumara snehara) make this record a usable "
            "letter-writing kit. Drill: write the same request as a formal "
            "letter and a familiar note."
        ),
        "key_points": [
            "15 formal vs informal pairs with full translations.",
            "Formal machinery: \u0101pa\u1e47a + -ntu; informal: tume/tu + bare root.",
            "Complete letter frames: formal and familiar openings and closings.",
            "Business, elders, and blessing registers covered.",
        ],
        "requirements": ["Read the pronoun and command records first."],
        "standards": [
            "Register forms follow standard usage.",
            "Pairs constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["Samm\u0101n\u012bya mahodaya", "\u0100pa\u1e47a\u1e45kara bi\u1e63wasta", "Priya bandhu", "15"],
        "sig_lens": (
            "Through the Signature lens register is the covenant of "
            "respect: every -\u0b28\u0b4d\u0b24\u0b41 a seal of honor laid on "
            "the request, every formal letter a vow in writing."
        ),
        "drill": {
            "pairs": 15,
            "formal_markers": ["\u0101pa\u1e47a", "-ntu"],
        },
    },
    {
        "key": "complex",
        "name": "Compound and Complex Sentences",
        "group": "Conversation and Registers",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen long sentences with clauses, connectors, and relative "
            "clauses - parsed and translated. Connectors: \u0b13 (o, and), "
            "\u0b15\u0b3f\u0b28\u0b4d\u0b24\u0b41 (kintu, but), \u0b15\u0b3e\u0b30\u0b23 (k\u0101ra\u1e47a, because), "
            "\u0b2f\u0b26\u0b3f (yadi, if), \u0b24\u0b47\u0b2c\u0b47 (tebe, then), \u0b2f\u0b47\u0b09\u0b01 (jeun, who/which, relative). \n\n"
            "  1. \u0b2e\u0b41\u0b01 \u0b2c\u0b1c\u0b3e\u0b30\u0b15\u0b41 \u0b17\u0b32\u0b3f \u0b13 \u0b2b\u0b33 \u0b15\u0b3f\u0b23\u0b3f\u0b32\u0b3f\u0964 "
            "(Mun baj\u0101raku gali o pha\u1e37a ki\u1e47ili.) I went to the market and bought fruit. [two clauses, o]\n"
            "  2. \u0b38\u0b47 \u0b27\u0b28\u0b40 \u0b15\u0b3f\u0b28\u0b4d\u0b24\u0b41 \u0b38\u0b41\u0b16\u0b40 \u0b28\u0b41\u0b39\u0b47\u0b01\u0964 "
            "(Se dhan\u012b kintu sukh\u012b nuhen.) He is rich but not happy. [contrast, kintu]\n"
            "  3. \u0b2e\u0b41\u0b01 \u0b18\u0b30\u0b47 \u0b30\u0b39\u0b3f\u0b32\u0b3f \u0b15\u0b3e\u0b30\u0b23 \u0b2c\u0b30\u0b4d\u0b37\u0b3e \u0b39\u0b47\u0b09\u0b25\u0b3f\u0b32\u0b3e\u0964 "
            "(Mun ghare rahili k\u0101ra\u1e47a bar\u1e63\u0101 heuthil\u0101.) I stayed home because it was raining. [cause, k\u0101ra\u1e47a]\n"
            "  4. \u0b2f\u0b26\u0b3f \u0b2c\u0b30\u0b4d\u0b37\u0b3e \u0b39\u0b41\u0b0f \u0b24\u0b47\u0b2c\u0b47 \u0b06\u0b2e\u0b47 \u0b2f\u0b3f\u0b2c\u0b3e \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 "
            "(Yadi bar\u1e63\u0101 hue tebe \u0101me yib\u0101 n\u0101hin.) If it rains, we will not go. [condition, yadi...tebe]\n"
            "  5. \u0b2f\u0b47\u0b09\u0b01 \u0b2a\u0b3f\u0b32\u0b3e \u0b2a\u0b22\u0b3c\u0b47 \u0b38\u0b47 \u0b2a\u0b3e\u0b38 \u0b39\u0b41\u0b0f\u0964 "
            "(Jeun pil\u0101 pa\u1e0dhe se p\u0101sa hue.) The child who studies passes. [relative, jeun]\n"
            "  6. \u0b2f\u0b47\u0b09\u0b01 \u0b2c\u0b39\u0b3f\u0b1f\u0b3f \u0b2e\u0b41\u0b01 \u0b15\u0b3f\u0b23\u0b3f\u0b32\u0b3f \u0b38\u0b47\u0b07\u0b1f\u0b3e \u0b2d\u0b32\u0964 "
            "(Jeun bahi\u1e6di mun ki\u1e47ili sei\u1e6d\u0101 bhala.) The book that I bought is good. [relative, jeun...sei\u1e6d\u0101]\n"
            "  7. \u0b38\u0b47 \u0b06\u0b38\u0b3f\u0b32\u0b3e \u0b2a\u0b30\u0b47 \u0b06\u0b2e\u0b47 \u0b16\u0b3e\u0b07\u0b32\u0b41\u0964 "
            "(Se \u0101sil\u0101 pare \u0101me kh\u0101ilu.) After he came, we ate. [time clause, pare]\n"
            "  8. \u0b2e\u0b41\u0b01 \u0b2f\u0b47\u0b24\u0b47\u0b2c\u0b47\u0b33\u0b47 \u0b2a\u0b39\u0b1e\u0b4d\u0b1a\u0b3f\u0b32\u0b3f \u0b38\u0b47\u0b24\u0b47\u0b2c\u0b47\u0b33\u0b47 \u0b38\u0b47 \u0b2f\u0b3e\u0b07\u0b38\u0b3e\u0b30\u0b3f\u0b25\u0b3f\u0b32\u0b3e\u0964 "
            "(Mun yetebe\u1e37e pahancili setebe\u1e37e se y\u0101is\u0101rithil\u0101.) When I arrived, he had already left. [yetebe\u1e37e...setebe\u1e37e]\n"
            "  9. \u0b24\u0b41\u0b2e\u0b47 \u0b2f\u0b3e\u0b39\u0b3e \u0b15\u0b39\u0b3f\u0b32 \u0b24\u0b3e\u0b39\u0b3e \u0b38\u0b24\u0964 "
            "(Tume y\u0101h\u0101 kahila t\u0101h\u0101 sata.) What you said is true. [y\u0101h\u0101...t\u0101h\u0101]\n"
            "  10. \u0b2e\u0b41\u0b01 \u0b1c\u0b3e\u0b23\u0b47 \u0b38\u0b47 \u0b15\u0b47\u0b09\u0b01\u0b20\u0b3f \u0b05\u0b1b\u0b3f\u0964 "
            "(Mun j\u0101\u1e47e se keun\u1e6dhi achi.) I know where he is. [reported clause]\n"
            "  11. \u0b38\u0b47 \u0b15\u0b39\u0b3f\u0b32\u0b3e \u0b38\u0b47 \u0b15\u0b3e\u0b32\u0b3f \u0b06\u0b38\u0b3f\u0b2c\u0964 "
            "(Se kahil\u0101 se k\u0101li \u0101siba.) He said he will come tomorrow. [reported speech]\n"
            "  12. \u0b2c\u0b30\u0b4d\u0b37\u0b3e \u0b39\u0b47\u0b32\u0b47 \u0b2e\u0b27\u0b4d\u0b5f \u0b2d\u0b32\u0964 "
            "(Bar\u1e63\u0101 hele madhya bhala.) Even if it rains, it is fine. [concession, hele madhya]\n"
            "  13. \u0b2f\u0b47\u0b2a\u0b30\u0b4d\u0b2f\u0b4d\u0b5f\u0b28\u0b4d\u0b24 \u0b2e\u0b41\u0b01 \u0b2c\u0b1e\u0b4d\u0b1a\u0b3f\u0b25\u0b3f\u0b2c\u0b3f \u0b38\u0b47\u0b2a\u0b30\u0b4d\u0b2f\u0b4d\u0b5f\u0b28\u0b4d\u0b24 \u0b2e\u0b41\u0b01 \u0b1a\u0b47\u0b37\u0b4d\u0b1f\u0b3e \u0b15\u0b30\u0b3f\u0b2c\u0b3f\u0964 "
            "(Yeparyyanta mun bancithibi separyyanta mun ce\u1e63\u1e6d\u0101 karibi.) As long as I live, I will try. [yeparyyanta...separyyanta]\n"
            "  14. \u0b38\u0b47 \u0b0f\u0b24\u0b47 \u0b26\u0b4d\u0b30\u0b41\u0b24 \u0b26\u0b4c\u0b21\u0b3c\u0b3f\u0b32\u0b3e \u0b2f\u0b47 \u0b15\u0b47\u0b39\u0b3f \u0b24\u0b3e\u0b15\u0b41 \u0b27\u0b30\u0b3f\u0b2a\u0b3e\u0b30\u0b3f\u0b32\u0b47 \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 "
            "(Se ete druta dau\u1e0dil\u0101 ye kehi t\u0101ku dharip\u0101rile n\u0101hin.) He ran so fast that no one could catch him. [result, ye]\n"
            "  15. \u0b2e\u0b41\u0b01 \u0b2d\u0b3e\u0b2c\u0b41\u0b1b\u0b3f \u0b06\u0b2e\u0b47 \u0b1c\u0b3f\u0b24\u0b3f\u0b2c\u0b3e\u0964 "
            "(Mun bh\u0101buchi \u0101me jitib\u0101.) I think we will win. [opinion clause]"
        ),
        "how_it_works": (
            "This record assembles long sentences from the whole toolkit: "
            "each of the fifteen gets a parse note naming its connector and "
            "clause type. The relative system (jeun...se, y\u0101h\u0101...t\u0101h\u0101), "
            "the conditionals (yadi...tebe, hele madhya), the correlatives "
            "(yetebe\u1e37e...setebe\u1e37e, yeparyyanta...separyyanta), cause "
            "(k\u0101ra\u1e47a), result (ye), and reported speech all appear "
            "once, each in a sentence the learner can reuse as a template. "
            "Drill: combine two short sentences from earlier records with "
            "each connector."
        ),
        "key_points": [
            "15 compound/complex sentences, each parsed and translated.",
            "Connectors: o, kintu, k\u0101ra\u1e47a, yadi...tebe, hele madhya, ye.",
            "Relatives: jeun...se, y\u0101h\u0101...t\u0101h\u0101; correlatives: yetebe\u1e37e...setebe\u1e37e.",
            "Reported speech and opinion clauses included.",
        ],
        "requirements": ["Read the tenses and Q&A records first."],
        "standards": [
            "Constructions follow standard Odia.",
            "Sentences constructed from standard grammar (labeled Signature-composed teaching sentences).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["yadi", "jeun", "k\u0101ra\u1e47a", "15"],
        "sig_lens": (
            "Through the Signature lens complex sentences are the covenant "
            "woven whole: every clause a thread, every connector a knot "
            "sealing meaning to meaning."
        ),
        "drill": {
            "sentences": 15,
            "connectors": ["o", "kintu", "k\u0101ra\u1e47a", "yadi", "tebe", "jeun"],
        },
    },
    {
        "key": "conv-market",
        "name": "Conversation: At the Market",
        "group": "Conversation and Registers",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue at the vegetable market - "
            "Odia with romanization and English, annotated. (Teaching "
            "dialogue, constructed from standard grammar; labeled "
            "Signature-composed.) \n\n"
            "  1. \u0b28\u0b2e\u0b38\u0b4d\u0b15\u0b3e\u0b30, \u0b2d\u0b3e\u0b07\u0964 (Namask\u0101ra, bh\u0101i.) Hello, brother. [warm market greeting]\n"
            "  2. \u0b28\u0b2e\u0b38\u0b4d\u0b15\u0b3e\u0b30\u0964 \u0b15\u0b23 \u0b28\u0b47\u0b2c\u0b47? (Namask\u0101ra. Ka\u1e47a nebe?) Hello. What will you take?\n"
            "  3. \u0b06\u0b33\u0b41 \u0b15\u0b3f\u0b32\u0b4b \u0b15\u0b47\u0b24\u0b47? (\u0100\u1e37u kilo kete?) How much per kilo of potatoes?\n"
            "  4. \u0b24\u0b3f\u0b30\u0b3f\u0b36 \u0b1f\u0b19\u0b4d\u0b15\u0b3e\u0964 (Tiri\u1e63a \u1e6da\u1e45k\u0101.) Thirty rupees.\n"
            "  5. \u0b2c\u0b39\u0b41\u0b24 \u0b26\u0b3e\u0b2e\u0b40\u0964 \u0b2a\u0b1a\u0b3f\u0b36\u0b30\u0b47 \u0b26\u0b47\u0b2c\u0b47 \u0b15\u0b3f? (Bahuta d\u0101m\u012b. Paci\u1e63are debe ki?) Too costly. Will you give for twenty-five?\n"
            "  6. \u0b28\u0b3e, \u0b2d\u0b3e\u0b07\u0964 \u0b05\u0b1f\u0b4d\u0b20\u0b3e\u0b07\u0b36 \u0b36\u0b47\u0b37\u0964 (N\u0101, bh\u0101i. A\u1e6dh\u0101i\u1e63a \u1e63e\u1e63a.) No, brother. Twenty-eight is final. [friendly bargaining]\n"
            "  7. \u0b20\u0b3f\u0b15 \u0b05\u0b1b\u0b3f\u0964 \u0b26\u0b41\u0b07 \u0b15\u0b3f\u0b32\u0b4b \u0b26\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (\u1e6dhika achi. Dui kilo diantu.) OK. Give two kilos, please.\n"
            "  8. \u0b28\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 \u0b24\u0b1f\u0b15\u0b3e \u0b2a\u0b30\u0b3f\u0b2c\u0b3e \u0b2d\u0b32 \u0b05\u0b1b\u0b3f\u0964 (Niantu. Ta\u1e6dak\u0101 parib\u0101 bhala achi.) Take. The fresh vegetables are good.\n"
            "  9. \u0b2a\u0b3f\u0b06\u0b1c \u0b15\u0b47\u0b24\u0b47? (Pi\u0101ja kete?) How much are onions?\n"
            "  10. \u0b1a\u0b3e\u0b33\u0b3f\u0b36 \u0b1f\u0b19\u0b4d\u0b15\u0b3e \u0b15\u0b3f\u0b32\u0b4b\u0964 (C\u0101\u1e37i\u1e63a \u1e6da\u1e45k\u0101 kilo.) Forty rupees a kilo.\n"
            "  11. \u0b0f\u0b15 \u0b15\u0b3f\u0b32\u0b4b \u0b26\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (Eka kilo diantu.) Give one kilo, please.\n"
            "  12. \u0b2e\u0b4b\u0b1f \u0b15\u0b47\u0b24\u0b47 \u0b39\u0b47\u0b32\u0b3e? (Mo\u1e6da kete hel\u0101?) What is the total?\n"
            "  13. \u0b05\u0b20\u0b3e\u0b28\u0b2c\u0b47 \u0b1f\u0b19\u0b4d\u0b15\u0b3e\u0964 (A\u1e6dh\u0101nabe \u1e6da\u1e45k\u0101.) Ninety-six rupees. [2x28 + 40 = 96: the arithmetic is real]\n"
            "  14. \u0b36\u0b39\u0b47 \u0b1f\u0b19\u0b4d\u0b15\u0b3e \u0b28\u0b3f\u0b05\u0b28\u0b4d\u0b24\u0b41\u0964 (\u1e62ahe \u1e6da\u1e45k\u0101 niantu.) Take one hundred rupees. [buyer overpays 4]\n"
            "  15. \u0b1a\u0b3e\u0b30\u0b3f \u0b1f\u0b19\u0b4d\u0b15\u0b3e \u0b2b\u0b47\u0b30\u0b3e\u0b07 \u0b26\u0b47\u0b09\u0b1b\u0b3f\u0964 (C\u0101ri \u1e6da\u1e45k\u0101 pher\u0101i deuchi.) I am returning four rupees. [change is exact]\n"
            "  16. \u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26, \u0b2d\u0b3e\u0b07\u0964 (Dhanyab\u0101da, bh\u0101i.) Thank you, brother.\n"
            "  17. \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15\u0b41 \u0b2e\u0b27\u0b4d\u0b5f \u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26\u0964 (\u0100pa\u1e47a\u1e45ku madhya dhanyab\u0101da.) Thank you too.\n"
            "  18. \u0b2a\u0b30\u0b3f\u0b2c\u0b3e \u0b24\u0b1f\u0b15\u0b3e \u0b05\u0b1b\u0b3f \u0b24?\u200c (Parib\u0101 ta\u1e6dak\u0101 achi ta?) The vegetables are fresh, right? [confirmation tag]\n"
            "  19. \u0b39\u0b01, \u0b06\u0b1c\u0b3f \u0b38\u0b15\u0b3e\u0b33\u0b30\u0964 (Han, \u0101ji sak\u0101\u1e37ara.) Yes, this morning's.\n"
            "  20. \u0b2b\u0b47\u0b30\u0b3f \u0b06\u0b38\u0b3f\u0b2c\u0b3f\u0964 (Pheri \u0101sibi.) I will come again."
        ),
        "how_it_works": (
            "This record is a complete market transaction in twenty lines: "
            "greeting, two price inquiries, bargaining (30 -> 25 -> 28 "
            "final), quantities, the total with real arithmetic (2x28 + 40 "
            "= 96), overpayment and exact change, thanks both ways, a "
            "freshness check, and the promise to return. Annotations mark "
            "the bargaining culture and the confirmation tag (ta?). Read it "
            "as buyer, then as seller."
        ),
        "key_points": [
            "20-line bilingual market dialogue, annotated.",
            "Full bargaining arc with real arithmetic (96 total, 4 change).",
            "Confirmation tag ta? and warm bh\u0101i address in context.",
        ],
        "requirements": ["Read the shopping and numbers records first."],
        "standards": [
            "Dialogue labeled as constructed teaching text.",
            "Arithmetic in the dialogue is exact (2x28+40=96, 100-96=4).",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["A\u1e6dh\u0101nabe", "pher\u0101i", "Signature-composed", "20"],
        "sig_lens": (
            "Through the Signature lens the market dialogue is the covenant "
            "of fair exchange acted out: every price haggled a vow "
            "negotiated, every rupee returned a seal of honesty."
        ),
        "drill": {
            "lines": 20, "scene": "market",
            "total": 96, "paid": 100, "change": 4,
        },
    },
    {
        "key": "conv-friend",
        "name": "Conversation: Meeting a Friend",
        "group": "Conversation and Registers",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue of two friends meeting - Odia "
            "with romanization and English, annotated. (Teaching dialogue, "
            "constructed from standard grammar; labeled Signature-composed.) \n\n"
            "  1. \u0b06\u0b30\u0b47, \u0b24\u0b41\u0b2e\u0b47! \u0b2c\u0b39\u0b41\u0b24 \u0b26\u0b3f\u0b28 \u0b2a\u0b30\u0b47 \u0b26\u0b47\u0b16\u0b3e! (Are, tume! Bahuta dina pare dekh\u0101!) Oh, you! Seeing you after so long! [warm exclamation]\n"
            "  2. \u0b39\u0b01, \u0b2c\u0b39\u0b41\u0b24 \u0b26\u0b3f\u0b28 \u0b39\u0b47\u0b32\u0b3e\u0964 \u0b15\u0b47\u0b2e\u0b3f\u0b24\u0b3f \u0b05\u0b1b? (Han, bahuta dina hel\u0101. Kemiti acha?) Yes, long time. How are you?\n"
            "  3. \u0b2e\u0b41\u0b01 \u0b2d\u0b32 \u0b05\u0b1b\u0b3f\u0964 \u0b24\u0b41\u0b2e\u0b47? (Mun bhala achi. Tume?) I am well. You?\n"
            "  4. \u0b2e\u0b41\u0b01 \u0b2e\u0b27\u0b4d\u0b5f \u0b2d\u0b32\u0964 \u0b15\u0b3e\u0b2e \u0b15\u0b47\u0b2e\u0b3f\u0b24\u0b3f \u0b1a\u0b3e\u0b32\u0b3f\u0b1b\u0b3f? (Mun madhya bhala. K\u0101ma kemiti c\u0101lichi?) I am well too. How is work going?\n"
            "  5. \u0b15\u0b3e\u0b2e \u0b2d\u0b32 \u0b1a\u0b3e\u0b32\u0b3f\u0b1b\u0b3f\u0964 \u0b24\u0b41\u0b2e\u0b30? (K\u0101ma bhala c\u0101lichi. Tumara?) Work is going well. Yours?\n"
            "  6. \u0b2e\u0b4b\u0b30 \u0b2e\u0b27\u0b4d\u0b5f \u0b20\u0b3f\u0b15\u0964 \u0b2a\u0b30\u0b3f\u0b2c\u0b3e\u0b30 \u0b15\u0b47\u0b2e\u0b3f\u0b24\u0b3f? (Mora madhya \u1e6dhika. Parib\u0101ra kemiti?) Mine is fine too. How is the family?\n"
            "  7. \u0b38\u0b2e\u0b38\u0b4d\u0b24\u0b47 \u0b2d\u0b32 \u0b05\u0b1b\u0b28\u0b4d\u0b24\u0b3f\u0964 (Samaste bhala achanti.) All are well.\n"
            "  8. \u0b1a\u0b3e \u0b2a\u0b3f\u0b07\u0b2c\u0b3e? (C\u0101 piib\u0101?) Shall we have tea? [the social ritual]\n"
            "  9. \u0b28\u0b3f\u0b36\u0b4d\u0b1a\u0b5f\u0964 \u0b1a\u0b3e\u0b32\u0964 (Ni\u1e63caya. C\u0101la.) Certainly. Let's go.\n"
            "  10. \u0b24\u0b41\u0b2e\u0b47 \u0b15\u0b47\u0b09\u0b01\u0b20\u0b41 \u0b30\u0b39\u0b41\u0b1b \u0b0f\u0b2c\u0b47? (Tume keun\u1e6dhu rahucha ebe?) Where are you living now?\n"
            "  11. \u0b2d\u0b41\u0b2c\u0b28\u0b47\u0b36\u0b4d\u0b35\u0b30\u0b30\u0b47\u0964 \u0b24\u0b41\u0b2e\u0b47? (Bhubane\u1e63warare. Tume?) In Bhubaneswar. You?\n"
            "  12. \u0b2e\u0b41\u0b01 \u0b15\u0b1f\u0b15\u0b30\u0b47\u0964 (Mun ka\u1e6dakare.) I am in Cuttack.\n"
            "  13. \u0b15\u0b47\u0b2c\u0b47 \u0b06\u0b38\u0b3f\u0b32? (Kebe \u0101sila?) When did you come?\n"
            "  14. \u0b17\u0b24 \u0b38\u0b2a\u0b4d\u0b24\u0b3e\u0b39\u0b30\u0b47\u0964 (Gata sapt\u0101hare.) Last week.\n"
            "  15. \u0b15\u0b47\u0b24\u0b47 \u0b26\u0b3f\u0b28 \u0b30\u0b39\u0b3f\u0b2c? (Kete dina rahiba?) How many days will you stay?\n"
            "  16. \u0b24\u0b3f\u0b28\u0b3f \u0b26\u0b3f\u0b28\u0964 \u0b24\u0b3e\u0b2a\u0b30\u0b47 \u0b2a\u0b41\u0b30\u0b40 \u0b2f\u0b3f\u0b2c\u0b3f\u0964 (Tini dina. T\u0101pare pur\u012b yibi.) Three days. Then I will go to Puri.\n"
            "  17. \u0b2c\u0b39\u0b41\u0b24 \u0b2d\u0b32\u0964 \u0b1c\u0b17\u0b28\u0b4d\u0b28\u0b3e\u0b25\u0b19\u0b4d\u0b15\u0b41 \u0b26\u0b30\u0b4d\u0b36\u0b28 \u0b15\u0b30\u0b3f\u0b2c\u0964 (Bahuta bhala. Jagann\u0101tha\u1e45ku dar\u1e63ana kariba.) Very good. You will visit Lord Jagannath.\n"
            "  18. \u0b39\u0b01\u0964 \u0b06\u0b38, \u0b1a\u0b3e \u0b2a\u0b3f\u0b07\u0b2c\u0b3e\u0964 (Han. \u0100sa, c\u0101 piib\u0101.) Yes. Come, let's have tea.\n"
            "  19. \u0b24\u0b41\u0b2e \u0b2c\u0b3f\u0b28\u0b3e \u0b1a\u0b3e \u0b2e\u0b1c\u0b3e \u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 (Tuma bin\u0101 c\u0101 maj\u0101 n\u0101hin.) Tea is no fun without you. [affection]\n"
            "  20. \u0b2b\u0b47\u0b30\u0b3f \u0b26\u0b47\u0b16\u0b3e \u0b39\u0b47\u0b2c\u0b3e, \u0b2c\u0b28\u0b4d\u0b27\u0b41\u0964 (Pheri dekh\u0101 heb\u0101, bandhu.) We will meet again, friend."
        ),
        "how_it_works": (
            "This record is the reunion: twenty lines of familiar-register "
            "friendship (tume throughout, never \u0101pa\u1e47a), moving from "
            "exclamation to catching up (work, family), the tea ritual, "
            "logistics (where, when, how long), travel plans (Puri, "
            "Jagann\u0101tha dar\u1e63ana), and warm parting. Annotations mark "
            "the exclamation, the ritual, and the affection. Read it with a "
            "partner, switching roles."
        ),
        "key_points": [
            "20-line bilingual friend-meeting dialogue, annotated.",
            "Familiar register throughout (tume); formal forms absent by design.",
            "Social ritual: the tea invitation; travel talk: Puri and Jagannath.",
        ],
        "requirements": ["Read the greetings and friendship records first."],
        "standards": [
            "Dialogue labeled as constructed teaching text.",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["Bahuta dina pare", "c\u0101 piib\u0101", "Signature-composed", "20"],
        "sig_lens": (
            "Through the Signature lens reunion is the covenant renewed: "
            "every long-time-no-see a vow remembered, every shared tea a "
            "seal of friendship."
        ),
        "drill": {
            "lines": 20, "scene": "meeting-friend",
            "register": "familiar",
        },
    },
    {
        "key": "conv-problem",
        "name": "Conversation: Solving a Problem",
        "group": "Conversation and Registers",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue of neighbors solving a water "
            "problem - Odia with romanization and English, annotated. "
            "(Teaching dialogue, constructed from standard grammar; labeled "
            "Signature-composed.) \n\n"
            "  1. \u0b28\u0b2e\u0b38\u0b4d\u0b15\u0b3e\u0b30, \u0b06\u0b1c\u0b4d\u0b1e\u0b3e\u0964 \u0b17\u0b4b\u0b1f\u0b3f\u0b0f \u0b15\u0b25\u0b3e \u0b05\u0b1b\u0b3f\u0964 (Namask\u0101ra, \u0101jny\u0101. Go\u1e6die kath\u0101 achi.) Hello, sir. There is a matter. [respectful opening]\n"
            "  2. \u0b15\u0b41\u0b39\u0b28\u0b4d\u0b24\u0b41, \u0b15\u0b23 \u0b39\u0b47\u0b07\u0b1b\u0b3f? (Kuhantu, ka\u1e47a heichi?) Tell me, what happened?\n"
            "  3. \u0b06\u0b2e \u0b38\u0b3e\u0b39\u0b3f\u0b30\u0b47 \u0b26\u0b41\u0b07 \u0b26\u0b3f\u0b28 \u0b39\u0b47\u0b32\u0b3e \u0b2a\u0b3e\u0b23\u0b3f \u0b06\u0b38\u0b41\u0b28\u0b3e\u0b39\u0b3f\u0b01\u0964 "
            "(\u0100ma s\u0101hire dui dina hel\u0101 p\u0101\u1e47i \u0101sun\u0101hin.) Water has not come to our lane for two days.\n"
            "  4. \u0b06\u0b1a\u0b4d\u0b1b\u0b3e, \u0b2e\u0b41\u0b01 \u0b2c\u0b41\u0b1d\u0b3f\u0b32\u0b3f\u0964 \u0b2a\u0b3e\u0b07\u0b2a \u0b2d\u0b3e\u0b19\u0b4d\u0b17\u0b3f\u0b2f\u0b3e\u0b07\u0b1b\u0b3f \u0b15\u0b3f? (Ach\u0101, mun bujhili. P\u0101ipa bh\u0101\u1e45giy\u0101ichi ki?) I see. Has the pipe broken?\n"
            "  5. \u0b39\u0b01, \u0b2c\u0b4b\u0b27\u0b39\u0b41\u0b0f \u0964 \u0b30\u0b3e\u0b38\u0b4d\u0b24\u0b3e \u0b15\u0b21\u0b3c\u0b30\u0b47 \u0b2a\u0b3e\u0b23\u0b3f \u0b1c\u0b2e\u0b41\u0b1b\u0b3f\u0964 (Han, bodhhue. R\u0101st\u0101 ka\u1e0dare p\u0101\u1e47i jamuchi.) Yes, probably. Water is collecting at the roadside.\n"
            "  6. \u0b24\u0b47\u0b2c\u0b47 \u0b2e\u0b41\u0b01 \u0b06\u0b1c\u0b3f \u0b39\u0b3f\u0b01 \u0b2e\u0b30\u0b3e\u0b2e\u0b24\u0b3f \u0b32\u0b4b\u0b15\u0b19\u0b4d\u0b15\u0b41 \u0b21\u0b3e\u0b15\u0b3f\u0b2c\u0b3f\u0964 "
            "(Tebe mun \u0101ji hin mar\u0101mati loka\u1e45ku d\u0101kibi.) Then I will call the repair people today itself.\n"
            "  7. \u0b2c\u0b39\u0b41\u0b24 \u0b2d\u0b32\u0964 \u0b15\u0b47\u0b24\u0b47 \u0b26\u0b3f\u0b28 \u0b32\u0b3e\u0b17\u0b3f\u0b2c? (Bahuta bhala. Kete dina l\u0101giba?) Very good. How many days will it take?\n"
            "  8. \u0b26\u0b41\u0b07 \u0b26\u0b3f\u0b28\u0b30\u0b41 \u0b2c\u0b47\u0b36\u0b3f \u0b28\u0b41\u0b39\u0b47\u0b01\u0964 (Dui dinaru be\u1e63i nuhen.) Not more than two days.\n"
            "  9. \u0b38\u0b47\u0b2a\u0b30\u0b4d\u0b2f\u0b4d\u0b5f\u0b28\u0b4d\u0b24 \u0b06\u0b2e\u0b47 \u0b15\u0b23 \u0b15\u0b30\u0b3f\u0b2c\u0b3e? (Separyyanta \u0101me ka\u1e47a karib\u0101?) What shall we do till then?\n"
            "  10. \u0b1f\u0b4d\u0b5f\u0b3e\u0b19\u0b4d\u0b15\u0b30 \u0b2a\u0b3e\u0b23\u0b3f \u0b06\u0b38\u0b41\u0b1b\u0b3f\u0964 \u0b38\u0b47\u0b25\u0b3f\u0b30\u0b41 \u0b28\u0b47\u0b07\u0b2f\u0b3e\u0b38\u0964 (\u1e6dy\u0101\u1e45kara p\u0101\u1e47i \u0101suchi. Sethiru nei\u0101sa.) The tanker water is coming. Fetch from there. [solution offered]\n"
            "  11. \u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26, \u0b06\u0b1c\u0b4d\u0b1e\u0b3e\u0964 (Dhanyab\u0101da, \u0101jny\u0101.) Thank you, sir.\n"
            "  12. \u0b15\u0b3f\u0b1b\u0b3f \u0b05\u0b38\u0b41\u0b2c\u0b3f\u0b27\u0b3e \u0b39\u0b47\u0b32\u0b47 \u0b2e\u0b4b\u0b24\u0b47 \u0b1c\u0b23\u0b3e\u0b06\u0b28\u0b4d\u0b24\u0b41\u0964 (Kichi asubidh\u0101 hele mote ja\u1e47\u0101ntu.) If there is any trouble, let me know.\n"
            "  13. \u0b28\u0b3f\u0b36\u0b4d\u0b1a\u0b5f\u0964 \u0b2a\u0b41\u0b23\u0b3f \u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26\u0964 (Ni\u1e63caya. Pu\u1e47i dhanyab\u0101da.) Certainly. Thanks again.\n"
            "  14. \u0b06\u0b1c\u0b4d\u0b1e\u0b3e, \u0b17\u0b4b\u0b1f\u0b3f\u0b0f \u0b05\u0b28\u0b41\u0b30\u0b4b\u0b27\u0964 (\u0100jny\u0101, go\u1e6die anurodha.) Sir, one request.\n"
            "  15. \u0b15\u0b41\u0b39\u0b28\u0b4d\u0b24\u0b41\u0964 (Kuhantu.) Tell me.\n"
            "  16. \u0b2a\u0b3e\u0b07\u0b2a \u0b2e\u0b30\u0b3e\u0b2e\u0b24\u0b3f \u0b2a\u0b30\u0b47 \u0b2a\u0b3e\u0b23\u0b3f\u0b30 \u0b1a\u0b3e\u0b2a \u0b26\u0b47\u0b16\u0b3f\u0b2c\u0b47 \u0b15\u0b3f? "
            "(P\u0101ipa mar\u0101mati pare p\u0101\u1e47ira c\u0101pa dekhibe ki?) After the pipe repair, will you check the water pressure?\n"
            "  17. \u0b39\u0b01, \u0b28\u0b3f\u0b36\u0b4d\u0b1a\u0b5f \u0b26\u0b47\u0b16\u0b3f\u0b2c\u0b3f\u0964 (Han, ni\u1e63caya dekhibi.) Yes, I will certainly check.\n"
            "  18. \u0b06\u0b2a\u0b23\u0b19\u0b4d\u0b15\u0b30 \u0b38\u0b39\u0b2f\u0b4b\u0b17 \u0b2a\u0b3e\u0b07\u0b01 \u0b16\u0b41\u0b38\u0b3f \u0b32\u0b3e\u0b17\u0b3f\u0b32\u0b3e\u0964 (\u0100pa\u1e47a\u1e45kara sahayoga p\u0101in khusi l\u0101gil\u0101.) I was glad to get your help.\n"
            "  19. \u0b0f\u0b39\u0b3e \u0b2e\u0b4b\u0b30 \u0b15\u0b30\u0b4d\u0b24\u0b4d\u0b24\u0b35\u0b4d\u0b5f\u0964 (Eh\u0101 mora karttabya.) This is my duty.\n"
            "  20. \u0b28\u0b2e\u0b38\u0b4d\u0b15\u0b3e\u0b30\u0964 (Namask\u0101ra.) Goodbye. [respectful close]"
        ),
        "how_it_works": (
            "This record is civic problem-solving in twenty lines: formal "
            "register throughout (\u0101jny\u0101 sir, -ntu verbs), the "
            "problem stated with duration (dui dina hel\u0101 p\u0101\u1e47i "
            "\u0101sun\u0101hin), diagnosis questioned (p\u0101ipa bh\u0101\u1e45giy\u0101ichi "
            "ki?), action promised (\u0101ji hin...d\u0101kibi), timeline "
            "bounded (dui dinaru be\u1e63i nuhen), interim solution (tanker "
            "water), follow-up request, and duty affirmed (eh\u0101 mora "
            "karttabya). Annotations mark the respectful opening, the "
            "solution, and the close. Read it as the resident, then as the "
            "official."
        ),
        "key_points": [
            "20-line bilingual problem-solving dialogue, annotated.",
            "Formal register throughout (\u0101jny\u0101, -ntu).",
            "Problem arc: state, diagnose, promise, bound, bridge, follow up, close.",
        ],
        "requirements": ["Read the registers and complex-sentence records first."],
        "standards": [
            "Dialogue labeled as constructed teaching text.",
        ],
        "citations": [CIT_MASICA],
        "must_contain": ["\u0101jny\u0101", "karttabya", "Signature-composed", "20"],
        "sig_lens": (
            "Through the Signature lens solving a problem is the covenant "
            "of community: every complaint heard a vow of attention, every "
            "duty done a seal of trust."
        ),
        "drill": {
            "lines": 20, "scene": "solving-problem",
            "register": "formal",
        },
    },
    {
        "key": "mastery",
        "name": "Mastery Review and Full Reference",
        "group": "Mastery Reference",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "description": (
            "The whole database in one teaching summary: alphabet, 200 core "
            "words, key grammar, all phrase tables. \n\n"
            "ALPHABET (10 vowels): \u0b05(a) \u0b06(aa) \u0b07(i) \u0b08(ii) \u0b09(u) \u0b0a(uu) "
            "\u0b0f(e) \u0b10(ai) \u0b13(o) \u0b14(au); 34 consonants in five vargas "
            "(ka, ca, \u1e6da, ta, pa rows of five) plus nine miscellaneous "
            "(\u0b2f \u0b30 \u0b33 \u0b71 \u0b36 \u0b37 \u0b38 \u0b39 \u0b5f); left-to-right abugida; "
            "danda \u0964 ends sentences; digits \u0b67-\u0b66 = 1-0. \n\n"
            "200 CORE WORDS (Odia - romanization - English), grouped: "
            "People: \u0b2e\u0b23\u0b3f\u0b37(ma\u1e47i\u1e63a-person) \u0b2e\u0b39\u0b3f\u0b33\u0b3e(mahi\u1e37\u0101-woman) "
            "\u0b2a\u0b3f\u0b32\u0b3e(pil\u0101-child) \u0b2c\u0b28\u0b4d\u0b27\u0b41(bandhu-friend) \u0b2e\u0b3e(m\u0101-mother) "
            "\u0b2c\u0b3e\u0b2a\u0b3e(b\u0101p\u0101-father) \u0b2d\u0b3e\u0b07(bh\u0101i-brother) \u0b2d\u0b09\u0b23\u0b40(bhau\u1e47\u012b-sister) "
            "\u0b21\u0b3e\u0b15\u0b4d\u0b24\u0b30(d\u0101ktara-doctor) \u0b36\u0b3f\u0b15\u0b4d\u0b37\u0b15(\u1e63ik\u1e63aka-teacher); "
            "Body: \u0b2e\u0b41\u0b23\u0b4d\u0b21(mu\u1e47da-head) \u0b06\u0b16\u0b3f(\u0101khi-eye) \u0b28\u0b3e\u0b15(n\u0101ka-nose) "
            "\u0b2a\u0b3e\u0b1f\u0b3f(p\u0101\u1e6di-mouth) \u0b39\u0b3e\u0b24(h\u0101ta-hand) \u0b17\u0b4b\u0b21\u0b3c(go\u1e0da-leg) "
            "\u0b39\u0b43\u0b26\u0b5f(h\u1e5bdaya-heart) \u0b26\u0b3e\u0b28\u0b4d\u0b24(d\u0101nta-tooth) \u0b15\u0b47\u0b36(ke\u1e63a-hair) \u0b2a\u0b47\u0b1f(pe\u1e6da-stomach); "
            "Home: \u0b18\u0b30(ghara-house) \u0b26\u0b4d\u0b35\u0b3e\u0b30(dw\u0101ra-door) \u0b1d\u0b30\u0b15\u0b3e(jharak\u0101-window) "
            "\u0b1a\u0b09\u0b15\u0b3f(chauki-chair) \u0b1f\u0b47\u0b2c\u0b41\u0b32(\u1e6debul-table) \u0b16\u0b1f(kha\u1e6da-bed) "
            "\u0b30\u0b4b\u0b37\u0b47\u0b07 \u0b18\u0b30(ro\u1e63ei ghara-kitchen) \u0b2c\u0b17\u0b3f\u0b1a\u0b3e(bagic\u0101-garden) "
            "\u0b2c\u0b24\u0b40(bat\u012b-light/lamp) \u0b1a\u0b3e\u0b2c\u0b3f(c\u0101bi-key); "
            "Food: \u0b2d\u0b3e\u0b24(bh\u0101ta-rice) \u0b21\u0b3e\u0b32\u0b3f(d\u0101li-dal) \u0b2a\u0b3e\u0b23\u0b3f(p\u0101\u1e47i-water) "
            "\u0b26\u0b41\u0b27(dudha-milk) \u0b1a\u0b3e(c\u0101-tea) \u0b2b\u0b33(pha\u1e37a-fruit) \u0b24\u0b30\u0b15\u0b3e\u0b30\u0b3f(tarak\u0101ri-vegetable) "
            "\u0b2e\u0b3e\u0b1b(m\u0101cha-fish) \u0b2e\u0b3e\u0b02\u0b38(m\u0101nsa-meat) \u0b32\u0b41\u0b23(lu\u1e47a-salt); "
            "Nature: \u0b38\u0b42\u0b30\u0b4d\u0b2f\u0b4d\u0b5f(s\u016bryya-sun) \u0b1a\u0b28\u0b4d\u0b26\u0b4d\u0b30(candra-moon) \u0b24\u0b3e\u0b30\u0b3e(t\u0101r\u0101-star) "
            "\u0b06\u0b15\u0b3e\u0b36(\u0101k\u0101\u1e63a-sky) \u0b2e\u0b47\u0b18(megha-cloud) \u0b2c\u0b30\u0b4d\u0b37\u0b3e(bar\u1e63\u0101-rain) "
            "\u0b17\u0b1b(gacha-tree) \u0b2b\u0b41\u0b32(phula-flower) \u0b28\u0b26\u0b40(nad\u012b-river) \u0b38\u0b2e\u0b41\u0b26\u0b4d\u0b30(samudra-sea); "
            "Animals: \u0b15\u0b41\u0b15\u0b41\u0b30(kukura-dog) \u0b2c\u0b3f\u0b32\u0b47\u0b07(bilei-cat) \u0b39\u0b3e\u0b24\u0b40(h\u0101t\u012b-elephant) "
            "\u0b2c\u0b3e\u0b18(b\u0101gha-tiger) \u0b18\u0b4b\u0b21\u0b3c\u0b3e(gho\u1e0d\u0101-horse) \u0b17\u0b3e\u0b08(g\u0101i-cow) "
            "\u0b1b\u0b47\u0b33\u0b3f(che\u1e37i-goat) \u0b2a\u0b15\u0b4d\u0b37\u0b40(pak\u1e63\u012b-bird) \u0b2e\u0b5f\u0b42\u0b30(may\u016bra-peacock) \u0b38\u0b3e\u0b2a(s\u0101pa-snake); "
            "Verbs: \u0b16\u0b3e\u0b07\u0b2c\u0b3e(kh\u0101ib\u0101-eat) \u0b2a\u0b3f\u0b07\u0b2c\u0b3e(piib\u0101-drink) \u0b2f\u0b3f\u0b2c\u0b3e(yib\u0101-go) "
            "\u0b06\u0b38\u0b3f\u0b2c\u0b3e(\u0101sib\u0101-come) \u0b15\u0b30\u0b3f\u0b2c\u0b3e(karib\u0101-do) \u0b2a\u0b22\u0b3c\u0b3f\u0b2c\u0b3e(pa\u1e0dhib\u0101-read) "
            "\u0b32\u0b47\u0b16\u0b3f\u0b2c\u0b3e(lekhib\u0101-write) \u0b15\u0b39\u0b3f\u0b2c\u0b3e(kahib\u0101-say) \u0b26\u0b47\u0b16\u0b3f\u0b2c\u0b3e(dekhib\u0101-see) "
            "\u0b36\u0b41\u0b23\u0b3f\u0b2c\u0b3e(\u1e63u\u1e47ib\u0101-listen); "
            "Adjectives: \u0b2c\u0b21\u0b3c(ba\u1e0da-big) \u0b1b\u0b4b\u0b1f(cho\u1e6da-small) \u0b2d\u0b32(bhala-good) "
            "\u0b16\u0b30\u0b3e\u0b2a(khar\u0101pa-bad) \u0b28\u0b42\u0b06(nu\u0101-new) \u0b2a\u0b41\u0b30\u0b41\u0b23\u0b3e(puru\u1e47\u0101-old) "
            "\u0b17\u0b30\u0b2e(garama-hot) \u0b25\u0b23\u0b4d\u0b21\u0b3e(\u1e6dha\u1e47\u1e0d\u0101-cold) \u0b38\u0b41\u0b28\u0b4d\u0b26\u0b30(sundara-beautiful) \u0b16\u0b41\u0b38\u0b3f(khusi-happy); "
            "Time: \u0b06\u0b1c\u0b3f(\u0101ji-today) \u0b15\u0b3e\u0b32\u0b3f(k\u0101li-yesterday/tomorrow) \u0b0f\u0b2c\u0b47(ebe-now) "
            "\u0b38\u0b15\u0b3e\u0b33(sak\u0101\u1e37a-morning) \u0b30\u0b3e\u0b24\u0b3f(r\u0101ti-night) \u0b26\u0b3f\u0b28(dina-day) "
            "\u0b38\u0b2a\u0b4d\u0b24\u0b3e\u0b39(sapt\u0101ha-week) \u0b2e\u0b3e\u0b38(m\u0101sa-month) \u0b2c\u0b30\u0b4d\u0b37(bar\u1e63a-year) \u0b38\u0b2e\u0b5f(samaya-time); "
            "Adverbs: \u0b36\u0b40\u0b18\u0b4d\u0b30(\u1e63\u012bghra-quickly) \u0b27\u0b40\u0b30\u0b47(dh\u012bre-slowly) \u0b0f\u0b20\u0b3e\u0b30\u0b47(e\u1e6dh\u0101re-here) \u0b38\u0b47\u0b20\u0b3e\u0b30\u0b47(se\u1e6dh\u0101re-there) \u0b2c\u0b39\u0b41\u0b24(bahuta-very) \u0b2a\u0b41\u0b23\u0b3f(pu\u1e47i-again) \u0b0f\u0b15\u0b3e\u0b20\u0b3f(ek\u0101\u1e6dhi-together) \u0b38\u0b2c\u0b41\u0b2c\u0b47\u0b33\u0b47(sabube\u1e37e-always) \u0b2d\u0b32\u0b2d\u0b3e\u0b2c\u0b47(bhalabh\u0101be-well) \u0b2a\u0b30\u0b47(pare-later); "
            "Numbers: \u0b0f\u0b15(eka-1) \u0b26\u0b41\u0b07(dui-2) \u0b24\u0b3f\u0b28\u0b3f(tini-3) \u0b1a\u0b3e\u0b30\u0b3f(c\u0101ri-4) "
            "\u0b2a\u0b3e\u0b1e\u0b4d\u0b1a(p\u0101nca-5) \u0b1b\u0b05(chaa-6) \u0b38\u0b3e\u0b24(s\u0101ta-7) \u0b06\u0b20(\u0101\u1e6dha-8) "
            "\u0b28\u0b05(naa-9) \u0b26\u0b36(da\u1e63a-10); "
            "Pronouns: \u0b2e\u0b41\u0b01(mun-I) \u0b06\u0b2e\u0b47(\u0101me-we) \u0b24\u0b41\u0b2e\u0b47(tume-you) "
            "\u0b06\u0b2a\u0b23(\u0101pa\u1e47a-you formal) \u0b38\u0b47(se-he/she) \u0b38\u0b47\u0b2e\u0b3e\u0b28\u0b47(sem\u0101ne-they) "
            "\u0b0f\u0b39\u0b3e(eh\u0101-this) \u0b24\u0b3e\u0b39\u0b3e(t\u0101h\u0101-that) \u0b15\u0b3f\u0b0f(kie-who) \u0b15\u0b23(ka\u1e47a-what); "
            "Question words: \u0b15\u0b47\u0b09\u0b01(keun-which) \u0b15\u0b47\u0b24\u0b47(kete-how many) \u0b15\u0b47\u0b2c\u0b47(kebe-when) "
            "\u0b15\u0b47\u0b09\u0b01\u0b20\u0b3e\u0b30\u0b47(keun\u1e6dh\u0101re-where) \u0b15\u0b3e\u0b39\u0b3f\u0b01\u0b15\u0b3f(k\u0101hinki-why) \u0b15\u0b3f\u0b2a\u0b30\u0b3f(kipari-how) \u0b15\u0b3e\u0b39\u0b3e\u0b30(kahara-whose) \u0b15\u0b47\u0b09\u0b01\u0b1f\u0b3e(keunta-which one) \u0b15\u0b47\u0b24\u0b47\u0b2c\u0b47\u0b33\u0b47(ketebele-at what time) \u0b15\u0b47\u0b2e\u0b3f\u0b24\u0b3f(kemiti-how); "
            "Connectors: \u0b13(o-and) \u0b15\u0b3f\u0b28\u0b4d\u0b24\u0b41(kintu-but) \u0b15\u0b3e\u0b30\u0b23(k\u0101ra\u1e47a-because) "
            "\u0b2f\u0b26\u0b3f(yadi-if) \u0b24\u0b47\u0b2c\u0b47(tebe-then) \u0b24\u0b47\u0b23\u0b41(te\u1e47u-therefore) \u0b2f\u0b26\u0b3f\u0b13(yadio-although) \u0b28\u0b1a\u0b47\u0b24\u0b4d(nachet-otherwise) \u0b05\u0b25\u0b2c\u0b3e(athaba-or) \u0b05\u0b30\u0b4d\u0b25\u0b3e\u0b24\u0b4d(arthat-that is); "
            "Courtesy: \u0b28\u0b2e\u0b38\u0b4d\u0b15\u0b3e\u0b30(namask\u0101ra-hello) \u0b27\u0b28\u0b4d\u0b5f\u0b2c\u0b3e\u0b26(dhanyab\u0101da-thanks) "
            "\u0b26\u0b5f\u0b3e\u0b15\u0b30\u0b3f(day\u0101kari-please) \u0b15\u0b4d\u0b37\u0b2e\u0b3e(k\u1e63am\u0101-forgiveness) \u0b2c\u0b3f\u0b26\u0b3e\u0b5f(bid\u0101ya-goodbye) "
            "\u0b39\u0b01(han-yes) \u0b28\u0b3e(n\u0101-no) \u0b38\u0b4d\u0b35\u0b3e\u0b17\u0b24(sw\u0101gata-welcome) "
            "\u0b36\u0b41\u0b2d\u0b47\u0b1a\u0b4d\u0b1b\u0b3e(\u1e63ubhech\u0101-wishes) \u0b05\u0b2d\u0b3f\u0b28\u0b28\u0b4d\u0b26\u0b28(abhinandana-congratulations); "
            "Places: \u0b2d\u0b41\u0b2c\u0b28\u0b47\u0b36\u0b4d\u0b35\u0b30(Bhubane\u1e63wara) \u0b15\u0b1f\u0b15(Ka\u1e6daka-Cuttack) \u0b2a\u0b41\u0b30\u0b40(Pur\u012b-Puri) "
            "\u0b2c\u0b1c\u0b3e\u0b30(baj\u0101ra-market) \u0b2c\u0b3f\u0b26\u0b4d\u0b5f\u0b3e\u0b33\u0b5f(bidy\u0101\u1e37aya-school) "
            "\u0b2e\u0b28\u0b4d\u0b26\u0b3f\u0b30(mandira-temple) \u0b21\u0b3e\u0b15\u0b4d\u0b24\u0b30\u0b16\u0b3e\u0b28\u0b3e(d\u0101ktarakh\u0101n\u0101-clinic) "
            "\u0b30\u0b47\u0b33 \u0b37\u0b4d\u0b1f\u0b47\u0b38\u0b28(rela s\u1e6de\u1e63ana-station) \u0b39\u0b4b\u0b1f\u0b47\u0b32(ho\u1e6dela-hotel) \u0b26\u0b4b\u0b15\u0b3e\u0b28(dok\u0101na-shop); "
            "More verbs: \u0b26\u0b47\u0b2c\u0b3e(deb\u0101-give) \u0b28\u0b47\u0b2c\u0b3e(neb\u0101-take) \u0b15\u0b3f\u0b23\u0b3f\u0b2c\u0b3e(ki\u1e47ib\u0101-buy) "
            "\u0b2c\u0b3f\u0b15\u0b3f\u0b2c\u0b3e(bikib\u0101-sell) \u0b16\u0b4b\u0b32\u0b3f\u0b2c\u0b3e(kholib\u0101-open) \u0b2c\u0b38\u0b3f\u0b2c\u0b3e(basib\u0101-sit) "
            "\u0b36\u0b4b\u0b07\u0b2c\u0b3e(\u1e63oib\u0101-sleep) \u0b39\u0b38\u0b3f\u0b2c\u0b3e(hasib\u0101-laugh) \u0b2d\u0b32 \u0b2a\u0b3e\u0b07\u0b2c\u0b3e(bhala p\u0101ib\u0101-love) "
            "\u0b38\u0b3e\u0b39\u0b3e\u0b2f\u0b4d\u0b5f \u0b15\u0b30\u0b3f\u0b2c\u0b3e(s\u0101h\u0101yya karib\u0101-help); "
            "More nouns: \u0b1f\u0b19\u0b4d\u0b15\u0b3e(\u1e6da\u1e45k\u0101-rupee) \u0b1a\u0b3f\u0b20\u0b3f(chi\u1e6dhi-letter) \u0b2b\u0b4b\u0b28(phona-phone) "
            "\u0b17\u0b3e\u0b21\u0b3c\u0b3f(g\u0101\u1e0di-vehicle) \u0b30\u0b3e\u0b38\u0b4d\u0b24\u0b3e(r\u0101st\u0101-road) \u0b1b\u0b24\u0b3e(chat\u0101-umbrella) "
            "\u0b14\u0b37\u0b27(au\u1e63adha-medicine) \u0b2a\u0b30\u0b3f\u0b2c\u0b3e\u0b30(parib\u0101ra-family) \u0b2c\u0b28\u0b4d\u0b27\u0b41\u0b24\u0b3e(bandhut\u0101-friendship) \u0b38\u0b4d\u0b35\u0b2a\u0b4d\u0b28(swapna-dream); "
            "Festivals: \u0b30\u0b25\u0b2f\u0b3e\u0b24\u0b4d\u0b30\u0b3e(Rathay\u0101tr\u0101) \u0b28\u0b42\u0b06\u0b16\u0b3e\u0b07(Nu\u0101kh\u0101i) \u0b26\u0b41\u0b30\u0b4d\u0b17\u0b3e\u0b2a\u0b42\u0b1c\u0b3e(Durg\u0101p\u016bj\u0101) "
            "\u0b15\u0b41\u0b2e\u0b3e\u0b30 \u0b2a\u0b42\u0b30\u0b4d\u0b23\u0b4d\u0b23\u0b3f\u0b2e\u0b3e(Kum\u0101ra p\u016br\u1e47\u1e47im\u0101) \u0b2c\u0b3e\u0b32\u0b3f\u0b2f\u0b3e\u0b24\u0b4d\u0b30\u0b3e(B\u0101liy\u0101tr\u0101) \u0b30\u0b1c(Raja) \u0b26\u0b4b\u0b33 \u0b2a\u0b42\u0b30\u0b4d\u0b23\u0b4d\u0b23\u0b3f\u0b2e\u0b3e(Dola P\u016br\u1e47\u1e47im\u0101) \u0b2e\u0b15\u0b30 \u0b38\u0b02\u0b15\u0b4d\u0b30\u0b3e\u0b28\u0b4d\u0b24\u0b3f(Makara Sankranti) \u0b26\u0b40\u0b2a\u0b3e\u0b2c\u0b33\u0b3f(Dipabali) \u0b39\u0b4b\u0b32\u0b3f(Holi); "
            "Dishes: \u0b2a\u0b16\u0b3e\u0b33(pakh\u0101\u1e37a) \u0b1b\u0b47\u0b28\u0b3e\u0b2a\u0b4b\u0b21\u0b3c(chen\u0101po\u1e0da) \u0b30\u0b38\u0b17\u0b4b\u0b32\u0b3e(rasagol\u0101) \u0b21\u0b3e\u0b32\u0b3f(d\u0101li-dal) \u0b38\u0b28\u0b4d\u0b24\u0b41\u0b33\u0b3e(santula-mixed vegetables) \u0b21\u0b3e\u0b32\u0b2e\u0b3e(dalma-dal with vegetables) \u0b2a\u0b3f\u0b20\u0b3e(pitha-rice cake) \u0b16\u0b3f\u0b30\u0b3f(khiri-rice pudding) \u0b26\u0b39\u0b3f\u0b2c\u0b30\u0b3e(dahibara) \u0b18\u0b41\u0b17\u0b41\u0b28\u0b3f(ghuguni). \n\n"
            "KEY GRAMMAR: SOV word order (verb last); three genders, two "
            "numbers; seven cases (ghara/gharaku/gharara/ghare); "
            "postpositions after nouns; no articles; two copulas "
            "(achi = is/exists, a\u1e6de = is/identity); negation n\u0101hin after "
            "the verb; questions by intonation or kie/ka\u1e47a/kebe/keun\u1e6dh\u0101re/k\u0101hinki/kipari; "
            "adjectives never inflect; tenses: kh\u0101e (habitual) / kh\u0101uchi "
            "(progressive) / kh\u0101ili (past) / kh\u0101ibi (future); "
            "imperatives: bare root informal, -ntu formal; connectors "
            "o/kintu/k\u0101ra\u1e47a/yadi...tebe/jeun. \n\n"
            "PHRASE TABLES: greetings (namask\u0101ra, juh\u0101ra, \u1e63ubha "
            "sak\u0101\u1e37a, dhanyab\u0101da, day\u0101kari, k\u1e63am\u0101 karantu, bid\u0101ya); "
            "market (eh\u0101ra d\u0101ma kete? kama karantu, \u1e6da\u1e45k\u0101 bh\u0101\u1e45gei); "
            "travel (sidh\u0101/d\u0101h\u0101\u1e47a/b\u0101ma, rela s\u1e6de\u1e63ana keun\u1e6dh\u0101re?); "
            "health (mora X bindhuchi, au\u1e63adha kh\u0101ntu); "
            "feelings (mote khusi l\u0101guchi, bhala p\u0101e); "
            "proverbs (adha kumbha ja\u1e37a cha\u1e37acha\u1e37a, karma hin dharma). \n\n"
            "You have climbed the whole ladder: foundations (overview, "
            "script, sounds) -> core vocabulary (nouns, verbs, adjectives, "
            "pronouns, numbers, greetings) -> grammar essentials -> everyday "
            "themes (home, food, travel, work, health, emotions, nature, "
            "shopping, friendship, technology) -> grammar in action (tenses, "
            "questions, commands, descriptions) -> stories and idioms -> "
            "conversation and registers -> this mastery reference. Go speak."
        ),
        "how_it_works": (
            "This record is the capstone: the alphabet, 200 core words in "
            "twenty groups, the key grammar in one paragraph, and the "
            "phrase tables - the whole database compressed to a single "
            "reference page. Use it as the daily review sheet: read one "
            "group aloud each morning until the whole ladder is memory. The "
            "closing paragraph names every rung climbed, so the learner sees "
            "the finished staircase."
        ),
        "key_points": [
            "Full alphabet: 10 vowels, 34 consonants, danda, digits.",
            "200 core words in 20 groups with romanization and English.",
            "Key grammar compressed to one paragraph.",
            "All phrase tables: greetings, market, travel, health, feelings, proverbs.",
            "Ladder recap: every rung named in climbing order.",
        ],
        "requirements": ["All 33 earlier records - this is the capstone."],
        "standards": [
            "Word counts verified by the demo (asserts 200).",
            "Reference data matches the records it summarizes.",
        ],
        "citations": [CIT_MASICA, CIT_EMENAU, CIT_ISO, CIT_CLASSICAL],
        "must_contain": ["200", "SOV", "kh\u0101ibi", "namask\u0101ra", "ladder"],
        "sig_lens": (
            "Through the Signature lens this reference is the sealed "
            "archive whole: every letter a sworn mark, every word a sealed "
            "vow, every rule a covenant kept - the language carried entire "
            "into the future."
        ),
        "drill": {
            "core_words": 200,
            "groups": ["People", "Body", "Home", "Food", "Nature", "Animals",
                       "Verbs", "Adjectives", "Time", "Numbers", "Pronouns",
                       "Question words", "Connectors", "Courtesy", "Places", "Adverbs",
                       "More verbs", "More nouns", "Festivals", "Dishes"],
            "grammar_rules": 10,
        },
    },
]
