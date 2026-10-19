#!/usr/bin/env python3
"""Entries for the Hausa to English databases (Manon's language project, 2026-10-17).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,602 databases) PLUS
every shard index title in jah-databases-data-1 (1,052 index files): zero
'language-hausa*' slugs; ID prefixes JAH-LHAU- (public) and JAH-LHAUS-
(signature) verified free in the manifest id_prefix values AND in every
shard index (zero zgrep hits for 'JAH-LHAU' across all index.jsonl.gz
files). Pre-authoring whole-system dedupe-gate check over all 68 planned
titles (34 records + 34 Signature Edition titles): zero collisions, zero
refusals.

This build creates two NEW databases, 34 ladder-ordered records each:

  language-hausa              - The Hausa to English Database
                                (public-harvest: real, fact-checked Hausa -
                                overview, Boko writing system, phonology and
                                tone, core vocabulary with sentences, grammar
                                essentials, themed sentence sets, verb tenses
                                and the TAM system, questions and answers,
                                commands, descriptions, stories, idioms and
                                proverbs, registers, complex sentences,
                                conversations, mastery reference; every line
                                in Hausa with English translation; standard
                                references Newman 2000, Jaggar 2001,
                                Abraham 1962, Bargery 1934, ISO 639 ha/hau)
  language-hausa-signature    - The Hausa to English Signature Database
                                (his original Signature Language Method:
                                every letter a sworn mark, every tone a
                                sealed vow, every sentence a covenant of
                                meaning; src signature, titles suffixed
                                " (Signature Edition)", clearly labeled
                                Signature-made, never presented as authentic
                                public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record carries Hausa content with English translation + example
sentences. Sentences are required in EVERY record - no vocabulary-list-only
records.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_hausa.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with the
OK marker; the build machine-executes all 68 demos before writing.

Build-time cross-check: every entry declares 'must_contain' strings and the
build asserts each one appears verbatim in the record description, so entry
text and demo outputs can never drift apart.

No website references. Screened per canon.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every letter a sworn mark, every tone a sealed vow, every "
            "sentence a covenant of meaning. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_NEWMAN = ("Newman P. The Hausa Language: An Encyclopedic Reference "
              "Grammar. Yale University Press; 2000.")
CIT_JAGGAR = ("Jaggar PJ. Hausa. London Oriental and African Language "
              "Library 7. John Benjamins; 2001.")
CIT_ABRAHAM = ("Abraham RC. Dictionary of the Hausa Language. 2nd ed. "
               "Hodder and Stoughton; 1962.")
CIT_BARGERY = ("Bargery GP. A Hausa-English Dictionary and English-Hausa "
               "Vocabulary. Oxford University Press; 1934.")
CIT_ISO = ("ISO 639: Hausa is coded ha (ISO 639-1) and hau (ISO 639-3); "
           "the Boko alphabet was standardized in 1957.")
CIT_AU = ("The African Union recognizes Hausa as a working language of "
          "the Union.")

# The Boko alphabet (standard Latin script since 1957): (letter, name-note,
# sound). The four hooked letters plus the glottalized y are the signature
# marks of written Hausa.
BOKO = [
    ("a", "a as in father"), ("b", "b as in boy"), ("ɓ", "implosive b"),
    ("c", "ch as in church"), ("d", "d as in dog"), ("ɗ", "implosive d"),
    ("e", "e as in bed"), ("f", "f as in fan"), ("g", "g as in go"),
    ("h", "h as in hat"), ("i", "i as in machine"), ("j", "j as in joy"),
    ("k", "k as in kite"), ("ƙ", "ejective k, popped from the throat"),
    ("l", "l as in love"), ("m", "m as in man"), ("n", "n as in name"),
    ("o", "o as in go"), ("p", "p as in pen"), ("r", "trilled r"),
    ("s", "s as in sun"), ("sh", "sh as in ship"), ("t", "t as in top"),
    ("ts", "ts as in cats"), ("u", "u as in moon"), ("w", "w as in water"),
    ("y", "y as in yes"), ("ƴ", "glottalized y, tight in the throat"),
    ("z", "z as in zebra"),
]
SPECIALS = ["ɓ", "ɗ", "ƙ", "ƴ"]
VOWELS = ["a", "e", "i", "o", "u"]
TONES = ["high", "low", "falling"]


def _alpha_lines():
    return "\n".join(
        "  %s  - %s" % (ch, note) for ch, note in BOKO)


ENTRIES = [
    {
        "key": "overview",
        "name": "Hausa Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Hausa (harshen Hausa, literally the language of the Hausa people) "
            "is the Chadic language of the Afro-Asiatic family spoken across "
            "West Africa. It carries ISO codes ha (ISO 639-1) and hau (ISO "
            "639-3), and is the largest indigenous African language by native "
            "speakers: about 70 million people speak it as a mother tongue, "
            "with total speakers above 100 million when second-language users "
            "across the Sahel are counted. \n\n"
            "Where it is spoken. The heartland is northern Nigeria - Kano, "
            "Kaduna, Sokoto, Katsina, Zaria, Bauchi - and southern Niger - "
            "Zinder, Maradi, Tahoua, Niamey. Large Hausa-speaking communities "
            "also live in Ghana, Cameroon, Chad, Sudan, and Ivory Coast, and "
            "Hausa serves as the trade language of the whole Sahel, from "
            "Dakar market stalls to Khartoum bus stations. \n\n"
            "Official status. Hausa is an official language of Nigeria and of "
            "Niger, and a working language of the African Union. \n\n"
            "Dialects. The Kano dialect is the standard of radio, school, and "
            "print. Other major dialects are Sokoto, Katsina, Zaria, Gobirawa, "
            "Hadarawa, Aderanci (eastern Niger), and Daurawa; they fall into "
            "broad Eastern and Western groups. A Kano speaker and a Sokoto "
            "speaker understand each other with ease. \n\n"
            "History in one breath. The Hausa Bakwai - the seven true "
            "Hausa city-states of Kano, Katsina, Zazzau (Zaria), Gobir, Rano, "
            "Biram, and Daura - traded cloth, leather, and kola across the "
            "Sahara for centuries; the Sokoto Caliphate of 1804 made Hausa "
            "the language of scholarship and law from Timbuktu to Lake Chad; "
            "and the Boko alphabet was standardized in 1957, giving the "
            "language the Latin script it uses in schools today. \n\n"
            "What makes Hausa learnable. The script is phonetic Latin, the "
            "word order is the familiar subject-verb-object, there are no "
            "noun cases and no verb conjugations in the European sense - "
            "tense and aspect ride on a small set of pronoun markers like na "
            "(I did), ina (I am doing), and zan (I will do). Learn the "
            "markers, learn the tones, and the language opens like a door. \n\n"
            "First sentences in harshen Hausa:\n"
            "  Sannu! - Hello!\n"
            "  Sunana Manon. - My name is Manon.\n"
            "  Ina son harshen Hausa. - I love the Hausa language.\n"
            "  Na fara koyon Hausa yau. - I started learning Hausa today."
        ),
        "how_it_works": (
            "This record is the map of the whole database. It fixes the "
            "identity of the language - name (harshen Hausa), codes (ha / "
            "hau), family (Afro-Asiatic, Chadic, West Chadic), speaker scale "
            "(about 70 million native, above 100 million total), territory "
            "(Nigeria, Niger, and the Sahel trade zone), official standing "
            "(Nigeria, Niger, African Union), dialect landscape (Kano "
            "standard; Sokoto, Katsina, Zaria, Gobirawa, Hadarawa, Aderanci, "
            "Daurawa), and the historical arc (Hausa Bakwai city-states, "
            "Sokoto Caliphate 1804, Boko 1957). Every later record hangs "
            "facts on this frame: the alphabet record spells the Boko "
            "letters, the phonology record sounds the tones, the vocabulary "
            "records fill the word-hoard, and the grammar records assemble "
            "the engine. Work through the ladder in order and each record "
            "assumes only what earlier records taught."
        ),
        "key_points": [
            "Native name: harshen Hausa; ISO 639-1 ha, ISO 639-3 hau.",
            "Family: Afro-Asiatic, Chadic branch, West Chadic group.",
            "About 70 million native speakers; above 100 million total with second-language users.",
            "Official in Nigeria and Niger; working language of the African Union.",
            "Kano dialect is the standard; Sokoto, Katsina, Zaria, Gobirawa, Hadarawa, Aderanci, Daurawa are the other major dialects.",
            "Seven historic city-states (Hausa Bakwai); Sokoto Caliphate 1804; Boko alphabet 1957.",
            "SVO word order; tense and aspect carried by pronoun markers (na, ina, zan).",
        ],
        "requirements": [
            "No prior knowledge of any African language is assumed.",
            "Read the alphabet record before the phonology record; read the phonology record before the vocabulary records.",
        ],
        "standards": [
            "Speaker figures are rounded public estimates (Ethnologue-style reporting); the record states them as approximate.",
            "Dialect and history claims follow the standard references: Newman 2000, Jaggar 2001.",
            "All example sentences are glossed word-for-word where the grammar is new.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR, CIT_ISO, CIT_AU],
        "must_contain": ["harshen Hausa", "ha", "hau", "Chadic", "Kano", "70 million"],
        "sig_lens": (
            "Through the Signature lens this overview is a census of a "
            "living nation of speakers: every headcount a sworn roll-call, "
            "every dialect a branch of one family tree, every city-state a "
            "seal on the covenant that this language will be carried whole "
            "into the archive."
        ),
        "drill": {
            "native_m": 70.0, "total_m": 100.0, "official_countries": 2,
            "iso1": "ha", "iso3": "hau", "city_states": 7,
            "dialects": ["Kano", "Sokoto", "Katsina", "Zaria", "Gobirawa",
                         "Hadarawa", "Aderanci", "Daurawa"],
            "regions": ["Nigeria", "Niger", "Ghana", "Cameroon", "Chad",
                        "Sudan", "Ivory Coast"],
            "au_working": True,
        },
    },
    {
        "key": "writing",
        "name": "The Hausa Writing System",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Hausa is written today in Boko, the Latin-based alphabet "
            "standardized in 1957. It runs left-to-right, is fully phonetic "
            "(one letter, one sound), and uses Arabic numerals 0-9 and "
            "English-style punctuation. A second script, Ajami - Hausa "
            "written in Arabic letters - survives in religious poetry, "
            "traditional scholarship, and old manuscripts, and runs "
            "right-to-left. \n\n"
            "The Boko alphabet, letter by letter:\n"
            + _alpha_lines() + "\n\n"
            "The four hooked letters are the signature of written Hausa: ɓ "
            "and ɗ are implosives (the air is sucked inward as the sound "
            "releases), ƙ is an ejective k (a sharp pop from the throat), and "
            "ƴ is a glottalized y. The digraphs sh and ts each count as one "
            "letter. There is no q, v, or x in native Hausa words; foreign "
            "words are respelled to fit Boko. \n\n"
            "Vowels are the five a e i o u, each with a short and a long "
            "form; length can change meaning, so learners write the "
            "doubled vowel (e.g. baaba for a long baa) when a dictionary "
            "marks it. Tone - the high, low, and falling pitch patterns of "
            "the phonology record - is almost never written in daily Boko; "
            "readers know the tones from the word itself. \n\n"
            "Ajami notes. In Ajami the Arabic script is adapted to Hausa "
            "sounds: the hooked letters get their own adapted forms, short "
            "vowels are written with full vowel marks in teaching texts, and "
            "classical Hausa poems (waka) still circulate in Ajami "
            "hand-copies. \n\n"
            "Read and write these first words:\n"
            "  gida - house\n"
            "  ruwa - water\n"
            "  sanyi - cold\n"
            "  ƙasa - down, below\n"
            "  ɗan - (a) son of; child of\n"
            "  ɓera - mouse, rat"
        ),
        "how_it_works": (
            "Boko works by direct sound-to-letter mapping: learn the 29 "
            "letters (25 single letters plus the digraphs sh and ts), learn "
            "the four hooked specials ɓ ɗ ƙ ƴ, and you can read any Hausa "
            "word aloud. Because the script is phonetic, spelling drills "
            "double as pronunciation drills. Ajami is presented for reading "
            "knowledge only: recognize that right-to-left Arabic-letter text "
            "on an old manuscript or a mosque wall may be Hausa, and know "
            "the hooked letters have adapted Ajami forms. Tone marks "
            "(acute for high, grave for low, circumflex for falling) appear "
            "only in linguistic writing, never in newspapers or schoolbooks."
        ),
        "key_points": [
            "Boko: Latin alphabet standardized 1957, written left-to-right, fully phonetic.",
            "29 letters: 25 single letters plus digraphs sh and ts.",
            "Hooked specials: ɓ, ɗ (implosives), ƙ (ejective), ƴ (glottalized).",
            "No q, v, x in native words; Arabic numerals 0-9; English-style punctuation.",
            "Ajami: Hausa in Arabic script, right-to-left, used for religious and traditional literature.",
            "Tone is not marked in everyday Boko writing.",
        ],
        "requirements": [
            "Practice handwriting or typing the hooked letters ɓ ɗ ƙ ƴ until they are automatic.",
            "Read the letter table aloud top to bottom before moving to the phonology record.",
        ],
        "standards": [
            "Letter inventory follows the 1957 Boko standard as described in Newman 2000.",
            "Ajami description follows the standard account in the Hausa reference grammars.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR, CIT_ISO],
        "must_contain": ["ɓ", "ɗ", "ƙ", "ƴ", "Boko", "Ajami", "left-to-right"],
        "sig_lens": (
            "Through the Signature lens the Boko alphabet is a sworn set of "
            "marks: each hooked letter a seal pressed into the page, each "
            "digraph a paired vow, Ajami the older covenant script kept "
            "beside the new one so nothing of the tradition is lost."
        ),
        "drill": {
            "letters": [ch for ch, _ in BOKO],
            "specials": SPECIALS,
            "digraphs": ["sh", "ts"],
            "missing_native": ["q", "v", "x"],
            "vowels": VOWELS,
            "direction": "left-to-right",
            "ajami_direction": "right-to-left",
            "test_words": ["gida", "ruwa", "sanyi", "ƙasa", "ɓera"],
        },
    },
    {
        "key": "phonology",
        "name": "Hausa Pronunciation and Phonology",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Hausa pronunciation rests on three pillars: five vowels that "
            "come in short and long pairs, a consonant set with implosive "
            "and ejective sounds English lacks, and three tones - high, low, "
            "and falling - that can change a word's meaning. The rhythm is "
            "syllable-timed: every syllable gets its full weight, with no "
            "English-style stress squash. \n\n"
            "Vowels. a e i o u, each short or long: a/aa, e/ee, i/ii, o/oo, "
            "u/uu. Short a is the a of father; long aa holds it twice as "
            "long. Length matters: it can separate one word from another, so "
            "hold the long vowels honestly. \n\n"
            "Consonants. Most match English, with four to master: ɓ "
            "(implosive b - the throat pulls air inward, as in ɓera, rat), ɗ "
            "(implosive d, as in ɗan, son of), ƙ (ejective k - a sharp pop, "
            "as in ƙasa, down/below), ƴ (glottalized y, the throat tightens). "
            "There is also the glottal stop, the catch in the throat between "
            "the syllables of English uh-oh, which appears in words like "
            "sa'o'i (hours). The r is trilled, and sh and ts are single "
            "sounds. \n\n"
            "Tone. High (marked á in linguistic writing), low (à), and "
            "falling (â). Tone is part of the word: the low-toned ƙasa means "
            "down or below, while the high-toned kasa means land or country. "
            "Grammar rides on tone too - the same pronoun-verb string can "
            "mean different tenses under different tone melodies. In daily "
            "writing tone is not marked; the ear learns it word by word. \n\n"
            "Sound it out - ten spoken-example words:\n"
            "  ruwa - water\n"
            "  gida - house\n"
            "  yaro - boy\n"
            "  yarinya - girl\n"
            "  kare - dog\n"
            "  rakumi - camel\n"
            "  sanyi - cold\n"
            "  zafi - heat\n"
            "  dare - night\n"
            "  rana - day, sun\n"
            "  wata - moon, month\n"
            "  itace - tree\n"
            "  ƙasa - down, below (low tone)\n"
            "  kasa - land, country (high tone)\n"
            "Say each word slowly, hold the vowels, and tap the table once "
            "per syllable: ru-wa, gi-da, ya-ri-nya, ra-ku-mi."
        ),
        "how_it_works": (
            "Train the three pillars in order. First, the vowel pairs: "
            "record yourself saying a/aa, e/ee, i/ii, o/oo, u/uu and check "
            "the long ones are truly double. Second, the four specials ɓ ɗ "
            "ƙ ƴ plus the glottal stop and trilled r, drilled against the "
            "example words until ɓera, ɗan, ƙasa, and sa'o'i come out "
            "cleanly. Third, tone: practice the ƙasa (down, low tone) versus "
            "kasa (land, high tone) pair until the pitch difference is "
            "unmistakable, then shadow native speech - radio, songs, market "
            "talk - repeating each phrase with its melody. Because Hausa is "
            "syllable-timed, keep every syllable even; never squash "
            "unstressed syllables the English way."
        ),
        "key_points": [
            "Five vowels (a e i o u), each short and long; length can change meaning.",
            "Special consonants: implosive ɓ ɗ, ejective ƙ, glottalized ƴ, plus the glottal stop and trilled r.",
            "Three tones: high, low, falling; tone distinguishes words (ƙasa down vs kasa land).",
            "Syllable-timed rhythm; no English-style stress reduction.",
            "Tone is not marked in everyday writing; the ear learns it per word.",
        ],
        "requirements": [
            "Be able to produce ɓ ɗ ƙ ƴ distinctly before the vocabulary records.",
            "Shadow at least one stretch of spoken Hausa daily while working this record.",
        ],
        "standards": [
            "Sound inventory follows Newman 2000 and Jaggar 2001.",
            "Tone examples use the standard linguistic marking (acute high, grave low, circumflex falling).",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR],
        "must_contain": ["high", "low", "falling", "ɓera", "ƙasa", "kasa", "syllable-timed"],
        "sig_lens": (
            "Through the Signature lens each sound is a sworn mark of the "
            "mouth: the implosives drawn inward like breath taken on oath, "
            "the ejective a pop of sealing wax, the three tones three "
            "levels of vow - high sworn aloud, low sworn in counsel, "
            "falling sworn and settled."
        ),
        "drill": {
            "vowels": VOWELS,
            "vowel_pairs": 10,
            "tones": TONES,
            "specials": SPECIALS,
            "example_words": [
                ("ruwa", "water"), ("gida", "house"), ("yaro", "boy"),
                ("yarinya", "girl"), ("kare", "dog"), ("rakumi", "camel"),
                ("sanyi", "cold"), ("zafi", "heat"), ("dare", "night"),
                ("rana", "day, sun"), ("wata", "moon, month"),
                ("itace", "tree"), ("ƙasa", "down, below"),
                ("kasa", "land, country"),
            ],
            "tone_pair": [("ƙasa", "low", "down, below"),
                          ("kasa", "high", "land, country")],
        },
    },
    {
        "key": "nouns",
        "name": "Core Hausa Nouns I",
        "group": "Core Vocabulary",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Hausa nouns - people, places, and things - "
            "each with a full sentence so the word is learned in motion, "
            "never alone. Hausa nouns carry gender (masculine or feminine; "
            "many feminines end in -a, like mota, car, and kofa, door) and "
            "form plurals in several ways (yaro/yara, boy/boys; mutum/"
            "mutane, person/people; littafi/littattafai, book/books), which "
            "the grammar records take up in full. \n\n"
            "  mutum (person) - Mutum yana cikin gida. (A person is in the house.)\n"
            "  namiji (man) - Namiji ya saya mota. (The man bought a car.)\n"
            "  mace (woman) - Mace tana dafa abinci. (The woman is cooking food.)\n"
            "  yaro (boy) - Yaro yana wasa a waje. (The boy is playing outside.)\n"
            "  yarinya (girl) - Yarinya tana karanta littafi. (The girl is reading a book.)\n"
            "  gida (house) - Gida babba ne. (The house is big.)\n"
            "  kofa (door) - Kofa a bude take. (The door is open.)\n"
            "  taga (window) - Taga rufe take. (The window is closed.)\n"
            "  kujera (chair) - Kujera tana kusa da tebur. (The chair is near the table.)\n"
            "  tebur (table) - Tebur yana cikin daki. (The table is in the room.)\n"
            "  ruwa (water) - Ruwan sanyi ne. (The water is cold.)\n"
            "  abinci (food) - Abinci yana da dadi. (The food is delicious.)\n"
            "  shinkafa (rice) - Shinkafa tana cikin tukunya. (The rice is in the pot.)\n"
            "  nama (meat) - Nama yana kan tebur. (The meat is on the table.)\n"
            "  kifi (fish) - Kifi yana cikin ruwa. (The fish is in the water.)\n"
            "  mota (car) - Mota tana gudu a hanya. (The car is moving on the road.)\n"
            "  keke (bicycle) - Keke yana waje. (The bicycle is outside.)\n"
            "  kasuwa (market) - Kasuwa ta cika da mutane. (The market is full of people.)\n"
            "  makaranta (school) - Makaranta tana kusa da gari. (The school is near the town.)\n"
            "  littafi (book) - Littafi yana kan tebur. (The book is on the table.)\n"
            "  asibiti (hospital) - Asibiti yana nesa da gari. (The hospital is far from the town.)\n"
            "  masallaci (mosque) - Masallaci yana tsakiyar gari. (The mosque is in the town center.)\n"
            "  rana (day, sun) - Rana ta fito. (The sun has risen.)\n"
            "  dare (night) - Dare ya yi. (Night has fallen.)\n"
            "  itace (tree) - Itace yana cikin gona. (The tree is on the farm.)\n\n"
            "Notice the verb markers agreeing with the noun: namiji ya saya "
            "(the man bought - masculine ya), mace tana dafa (the woman is "
            "cooking - feminine tana), mota tana gudu (the car is moving - "
            "feminine tana). Gender is grammatical, not just natural, and "
            "the pronoun record maps every marker."
        ),
        "how_it_works": (
            "Learn each noun with its sentence, not as an isolated gloss: "
            "say the Hausa sentence aloud, then the English, until the pair "
            "is one memory. Watch the gender signals - the ya/tana markers "
            "on the verb and the ne/ce copula endings - and sort the nouns "
            "into masculine and feminine piles as you go: namiji, yaro, "
            "tebur, littafi on one side; mace, yarinya, mota, kofa, kasuwa "
            "on the other. Note the plural shapes given for yaro, mutum, and "
            "littafi; the grammar record systematizes them. Quiz yourself "
            "both directions: Hausa to English and English to Hausa."
        ),
        "key_points": [
            "25 essential nouns: people, places, things.",
            "Every noun learned inside a full translated sentence.",
            "Hausa nouns are masculine or feminine; many feminines end in -a.",
            "Verbs agree with noun gender (ya masculine, ta/tana feminine).",
            "Plurals take several shapes: yaro/yara, mutum/mutane, littafi/littattafai.",
        ],
        "requirements": [
            "Pronounce the hooked letters correctly in ɓ-free nouns here and in ɗan-style words elsewhere.",
            "Sort all 25 nouns by gender from memory before advancing.",
        ],
        "standards": [
            "Noun glosses follow Abraham 1962 and Bargery 1934.",
            "Sentences use standard Kano-dialect grammar per Newman 2000.",
        ],
        "citations": [CIT_ABRAHAM, CIT_BARGERY, CIT_NEWMAN],
        "must_contain": ["mutum", "yaro/yara", "mota", "Mace tana dafa abinci", "Kasuwa ta cika da mutane", "Rana ta fito"],
        "sig_lens": (
            "Through the Signature lens these twenty-five nouns are the "
            "first sworn inventory of the world: each person, place, and "
            "thing named once, named truly, and set in a sentence like a "
            "stone set in a wall - the foundation course of the whole "
            "language house."
        ),
        "drill": {
            "nouns": [
                ("mutum", "person", "m"), ("namiji", "man", "m"),
                ("mace", "woman", "f"), ("yaro", "boy", "m"),
                ("yarinya", "girl", "f"), ("gida", "house", "m"),
                ("kofa", "door", "f"), ("taga", "window", "f"),
                ("kujera", "chair", "f"), ("tebur", "table", "m"),
                ("ruwa", "water", "m"), ("abinci", "food", "m"),
                ("shinkafa", "rice", "f"), ("nama", "meat", "m"),
                ("kifi", "fish", "m"), ("mota", "car", "f"),
                ("keke", "bicycle", "m"), ("kasuwa", "market", "f"),
                ("makaranta", "school", "f"), ("littafi", "book", "m"),
                ("asibiti", "hospital", "m"), ("masallaci", "mosque", "m"),
                ("rana", "day, sun", "f"), ("dare", "night", "m"),
                ("itace", "tree", "m"),
            ],
            "plurals": [("yaro", "yara"), ("mutum", "mutane"),
                        ("littafi", "littattafai"), ("gida", "gidaje")],
            "sentences": 25,
        },
    },
]

ENTRIES.append(
    {
        "key": "verbs",
        "name": "Core Hausa Verbs I",
        "group": "Core Vocabulary",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Hausa verbs, each inside a full sentence. "
            "Hausa verbs do not conjugate the European way: the verb stem "
            "stays nearly still while small pronoun markers carry person, "
            "tense, and aspect - na ci (I ate), ina ci (I am eating), zan ci "
            "(I will eat). Master the markers and every verb below opens in "
            "all tenses at once. \n\n"
            "  je (go) - Na je kasuwa. (I went to the market.)\n"
            "  zo (come) - Yaro ya zo makaranta. (The boy came to school.)\n"
            "  ci (eat) - Na ci abinci. (I ate food.)\n"
            "  sha (drink) - Ina shan ruwa. (I am drinking water.)\n"
            "  yi (do, make) - Ta yi aiki. (She did the work.)\n"
            "  gani (see) - Na gan shi. (I saw him.)\n"
            "  ji (hear, feel) - Na ji labari. (I heard the news.)\n"
            "  fada (say, tell) - Ya fada mini gaskiya. (He told me the truth.)\n"
            "  tambaya (ask) - Na tambaye shi. (I asked him.)\n"
            "  amsa (answer) - Ta amsa tambaya. (She answered the question.)\n"
            "  rubuta (write) - Na rubuta wasika. (I wrote a letter.)\n"
            "  karanta (read) - Ina karanta littafi. (I am reading a book.)\n"
            "  koya (learn) - Yana koyon Hausa. (He is learning Hausa.)\n"
            "  koyar (teach) - Malam yana koyar da yara. (The teacher is teaching the children.)\n"
            "  aiki (work) - Suna aiki a gona. (They are working on the farm.)\n"
            "  saya (buy) - Na saya tufafi. (I bought clothes.)\n"
            "  sayar (sell) - Yana sayar da kayan marmari. (He is selling fruit.)\n"
            "  bude (open) - Ta bude kofa. (She opened the door.)\n"
            "  rufe (close) - Ya rufe taga. (He closed the window.)\n"
            "  zauna (sit, stay) - Na zauna a gida. (I stayed at home.)\n"
            "  tashi (get up) - Ya tashi da sassafe. (He got up early in the morning.)\n"
            "  kwana (sleep, spend the night) - Na kwana lafiya. (I slept well.)\n"
            "  farka (wake up) - Ta farka da wuri. (She woke up early.)\n"
            "  kawo (bring) - Ya kawo mini ruwa. (He brought me water.)\n"
            "  biya (pay) - Na biya kudi. (I paid the money.)\n\n"
            "Watch the markers do the work: na (I + completed), ina "
            "(I + ongoing), zan (I + future), ya (he + completed), yana "
            "(he + ongoing), ta (she + completed), tana (she + ongoing), "
            "suna (they + ongoing), mun (we + completed). The pronoun "
            "record lists every marker; the verb-tense record runs the "
            "whole system."
        ),
        "how_it_works": (
            "Learn each verb as a marker-plus-stem machine. Take ci (eat): "
            "say na ci, ina cin, zan ci, ka ci, kin ci, ya ci, ta ci, mun ci, "
            "kun ci, sun ci - the stem barely moves while the markers swing "
            "the meaning through person and tense. Notice the continuous "
            "uses the verbal noun (cin, shan, koyon): ina cin abinci, ina "
            "shan ruwa, yana koyon Hausa. Practice by swapping markers on "
            "one verb until the pattern is muscle memory, then walk the "
            "list verb by verb."
        ),
        "key_points": [
            "25 essential verbs, each in a full translated sentence.",
            "The verb stem is stable; pronoun markers carry tense and aspect.",
            "Core markers: na (I did), ina (I am doing), zan (I will do), ya/ta (he/she did), yana/tana (he/she is doing).",
            "The continuous tense uses the verbal noun: cin, shan, koyon.",
            "Pronoun objects attach to the verb: gan shi (saw him), tambaye shi (asked him).",
        ],
        "requirements": [
            "Recite the na/ina/zan paradigm for ci, sha, and je from memory.",
            "Know the noun genders from the nouns record - the ya/ta markers must agree.",
        ],
        "standards": [
            "Verb glosses follow Abraham 1962 and Bargery 1934.",
            "Marker analysis follows the TAM system in Newman 2000 and Jaggar 2001.",
        ],
        "citations": [CIT_ABRAHAM, CIT_BARGERY, CIT_NEWMAN, CIT_JAGGAR],
        "must_contain": ["Na ci abinci", "Ina shan ruwa", "zan ci", "Malam yana koyar da yara", "Na biya kudi"],
        "sig_lens": (
            "Through the Signature lens these twenty-five verbs are the "
            "sworn actions of the language: each one a deed named and "
            "sealed, each marker a timestamp pressed beside it - na for "
            "what is done and finished, ina for what is being done now, "
            "zan for what is vowed to be done."
        ),
        "drill": {
            "verbs": [
                ("je", "go"), ("zo", "come"), ("ci", "eat"), ("sha", "drink"),
                ("yi", "do, make"), ("gani", "see"), ("ji", "hear, feel"),
                ("fada", "say, tell"), ("tambaya", "ask"), ("amsa", "answer"),
                ("rubuta", "write"), ("karanta", "read"), ("koya", "learn"),
                ("koyar", "teach"), ("aiki", "work"), ("saya", "buy"),
                ("sayar", "sell"), ("bude", "open"), ("rufe", "close"),
                ("zauna", "sit, stay"), ("tashi", "get up"),
                ("kwana", "sleep, spend the night"), ("farka", "wake up"),
                ("kawo", "bring"), ("biya", "pay"),
            ],
            "markers": {
                "perfect_1sg": "na", "cont_1sg": "ina", "fut_1sg": "zan",
                "perfect_3sgm": "ya", "perfect_3sgf": "ta",
                "cont_3sgm": "yana", "cont_3sgf": "tana",
            },
            "verbal_nouns": {"ci": "cin", "sha": "shan", "koya": "koyon",
                             "je": "tafiya", "yi": "yi"},
            "sentences": 25,
        },
    }
)
ENTRIES.append(
    {
        "key": "adjectives",
        "name": "Hausa Adjectives and Adverbs",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five adjectives and fifteen adverbs, each in a sentence. "
            "Hausa adjectives follow the noun they describe (gida babba, a "
            "big house - literally house big) and many agree in gender with "
            "it: yaro babba (a big boy) but yarinya babbar (a big girl); "
            "dogo (tall, masculine) but doguwa (tall, feminine). Adverbs "
            "modify the verb and usually follow it. \n\n"
            "Adjectives:\n"
            "  babba (big) - Gida babba ne. (The house is big.)\n"
            "  karami (small) - Yaro karami ne. (The boy is small.)\n"
            "  dogo (tall, m) - Namiji dogo ne. (The man is tall.)\n"
            "  gajere (short) - Itace gajere ne. (The tree is short.)\n"
            "  kyakkyawa (beautiful, m) - Gari kyakkyawa ne. (The town is beautiful.)\n"
            "  mugu (bad, ugly) - Wannan aiki mugu ne. (This work is bad.)\n"
            "  sabo (new, m) - Littafi sabo ne. (The book is new.)\n"
            "  tsoho (old) - Littafin tsoho ne. (The book is old.)\n"
            "  sanyi (cold) - Ruwan sanyi ne. (The water is cold.)\n"
            "  zafi (hot) - Abincin zafi ne. (The food is hot.)\n"
            "  baki (black) - Kare baki ne. (The dog is black.)\n"
            "  fari (white) - Tufafin fari ne. (The clothes are white.)\n"
            "  ja (red) - Mota ja ce. (The car is red.)\n"
            "  kore (green) - Ganyen kore ne. (The leaf is green.)\n"
            "  lafiya (healthy, fine) - Yaro lafiya kalau. (The boy is very well.)\n"
            "  mai kudi (rich) - Mutumin mai kudi ne. (The man is rich.)\n"
            "  talaka (poor) - Talaka yana bukatar taimako. (The poor man needs help.)\n"
            "  sauki (easy) - Aikin sauki ne. (The work is easy.)\n"
            "  wahala (difficult) - Tambayar wahala ce. (The question is difficult.)\n"
            "  nisa (far) - Gari nisa ne. (The town is far.)\n"
            "  kusa (near) - Makaranta kusa ce. (The school is near.)\n"
            "  dadi (sweet, pleasant) - Mangwaro dadi ne. (The mango is sweet.)\n"
            "  daci (bitter) - Maganin daci ne. (The medicine is bitter.)\n"
            "  mai kyau (good) - Aiki mai kyau ne. (The work is good.)\n"
            "  tsada (expensive) - Abincin tsada ne. (The food is expensive.)\n\n"
            "Adverbs:\n"
            "  sosai (very) - Ina son shi sosai. (I like him very much.)\n"
            "  kadan (a little) - Na ci kadan. (I ate a little.)\n"
            "  yanzu (now) - Zo yanzu! (Come now!)\n"
            "  gobe (tomorrow) - Zan tafi gobe. (I will go tomorrow.)\n"
            "  jiya (yesterday) - Ya zo jiya. (He came yesterday.)\n"
            "  kullum (every day, always) - Yana zuwa kullum. (He comes every day.)\n"
            "  sau da yawa (often) - Tana zuwa sau da yawa. (She comes often.)\n"
            "  da sauri (quickly) - Ya gudu da sauri. (He ran quickly.)\n"
            "  a hankali (slowly, carefully) - Yi aiki a hankali. (Work carefully.)\n"
            "  tare (together) - Mun tafi tare. (We went together.)\n"
            "  shi kadai (alone) - Ya zauna shi kadai. (He sat alone.)\n"
            "  da wuri (early) - Ta tashi da wuri. (She woke up early.)\n"
            "  da daddare (at night) - Suna tafiya da daddare. (They travel at night.)\n"
            "  a nan (here) - Zauna a nan. (Sit here.)\n"
            "  a can (there) - Littafin yana a can. (The book is there.)\n\n"
            "Gender agreement in action: mota sabuwa ce (the car is new - "
            "feminine sabuwa with feminine mota) against littafi sabo ne "
            "(the book is new - masculine sabo with masculine littafi)."
        ),
        "how_it_works": (
            "Build noun phrases by placing the adjective after the noun: "
            "gida babba, mota sabuwa, yaro karami. Then practice the gender "
            "switch on the adjectives that inflect - say yaro babba / "
            "yarinya babbar, littafi sabo / mota sabuwa, namiji dogo / mace "
            "doguwa - until the feminine -r or -wa ending is automatic. For "
            "adverbs, attach them after the verb: yi aiki a hankali, gudu "
            "da sauri, tafi tare. Time adverbs (yanzu, gobe, jiya, kullum) "
            "can open or close the sentence; manner adverbs (sosai, kadan, "
            "a hankali) stay close to the verb."
        ),
        "key_points": [
            "25 adjectives + 15 adverbs, every one in a translated sentence.",
            "Adjectives follow the noun: gida babba (big house).",
            "Many adjectives agree in gender: babba/babbar, sabo/sabuwa, dogo/doguwa.",
            "The copula agrees too: ne (masculine), ce (feminine).",
            "Adverbs follow the verb; time adverbs are mobile.",
        ],
        "requirements": [
            "Produce masculine/feminine adjective pairs for at least ten adjectives from memory.",
            "Combine any noun from the nouns record with any adjective here into a correct phrase.",
        ],
        "standards": [
            "Adjective agreement described per Newman 2000 and Jaggar 2001.",
            "Glosses follow Abraham 1962.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR, CIT_ABRAHAM],
        "must_contain": ["gida babba", "yarinya babbar", "mota sabuwa ce", "Yi aiki a hankali", "sau da yawa"],
        "sig_lens": (
            "Through the Signature lens adjectives are the sworn qualities "
            "and adverbs the sworn manners: each descriptive word a seal of "
            "what a thing is, each manner word a seal of how a deed was "
            "done - the description bound to the noun it follows like a "
            "witness standing behind the accused."
        ),
        "drill": {
            "adjectives": [
                ("babba", "big"), ("karami", "small"), ("dogo", "tall, m"),
                ("gajere", "short"), ("kyakkyawa", "beautiful, m"),
                ("mugu", "bad, ugly"), ("sabo", "new, m"),
                ("tsoho", "old"), ("sanyi", "cold"), ("zafi", "hot"),
                ("baki", "black"), ("fari", "white"), ("ja", "red"),
                ("kore", "green"), ("lafiya", "healthy, fine"),
                ("mai kudi", "rich"), ("talaka", "poor"), ("sauki", "easy"),
                ("wahala", "difficult"), ("nisa", "far"), ("kusa", "near"),
                ("dadi", "sweet, pleasant"), ("daci", "bitter"),
                ("mai kyau", "good"), ("tsada", "expensive"),
            ],
            "adverbs": [
                ("sosai", "very"), ("kadan", "a little"), ("yanzu", "now"),
                ("gobe", "tomorrow"), ("jiya", "yesterday"),
                ("kullum", "every day, always"), ("sau da yawa", "often"),
                ("da sauri", "quickly"), ("a hankali", "slowly, carefully"),
                ("tare", "together"), ("shi kadai", "alone"),
                ("da wuri", "early"), ("da daddare", "at night"),
                ("a nan", "here"), ("a can", "there"),
            ],
            "agreement_pairs": [("babba", "babbar"), ("sabo", "sabuwa"),
                                ("dogo", "doguwa"), ("karami", "karama"),
                                ("kyakkyawa", "kyakkyawar")],
            "sentences": 40,
        },
    }
)
ENTRIES.append(
    {
        "key": "pronouns",
        "name": "Hausa Pronouns",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The full Hausa pronoun system: independent pronouns, the "
            "possessive suffixes, demonstratives, and interrogatives - each "
            "with sentences. These small words are the engine room of the "
            "language: the tense-aspect markers of the verb records are "
            "built on the pronouns. \n\n"
            "Independent pronouns:\n"
            "  ni (I) - Ni malami ne. (I am a teacher.)\n"
            "  kai (you, masculine) - Kai dan kasuwa ne. (You are a trader.)\n"
            "  ke (you, feminine) - Ke malama ce. (You are a teacher, f.)\n"
            "  shi (he) - Shi yana gida. (He is at home.)\n"
            "  ita (she) - Ita malama ce. (She is a teacher.)\n"
            "  mu (we) - Mu 'yan uwa ne. (We are siblings.)\n"
            "  ku (you, plural) - Ku zo nan. (You all, come here.)\n"
            "  su (they) - Su suna makaranta. (They are at school.)\n\n"
            "Possessive suffixes (attached to the noun):\n"
            "  -na (my) - Gidana yana nan. (My house is here.)\n"
            "  -nka (your, m) - Motarka tana waje. (Your car is outside.)\n"
            "  -nki (your, f) - Littafinki yana kan tebur. (Your book is on the table.)\n"
            "  -nsa (his) - Sunansa Manon. (His name is Manon.)\n"
            "  -nta (her) - Yarinyarta tana wasa. (Her daughter is playing.)\n"
            "  -mu (our) - Garinmu kyakkyawa ne. (Our town is beautiful.)\n"
            "  -nku (your, pl) - Makarantarku tana nesa. (Your school is far.)\n"
            "  -nsu (their) - Gidansu babba ne. (Their house is big.)\n\n"
            "Demonstratives:\n"
            "  wannan (this) - Wannan littafina ne. (This is my book.)\n"
            "  wadannan (these) - Wadannan littattafaina ne. (These are my books.)\n"
            "  wancan (that) - Wancan motata ce. (That is my car.)\n"
            "  wadancan (those) - Wadancan gidajensu ne. (Those are their houses.)\n\n"
            "Interrogatives:\n"
            "  wa (who) - Wa ya zo? (Who came?)\n"
            "  me, mene (what) - Me kake so? (What do you want?)\n"
            "  ina (where) - Ina makaranta? (Where is the school?)\n"
            "  yaushe (when) - Yaushe za ka tafi? (When will you go?)\n"
            "  ta yaya, ya (how) - Ta yaya kake? (How are you?)\n"
            "  me ya sa (why) - Me ya sa ka yi kuka? (Why did you cry?)\n"
            "  nawa (how many) - Yara nawa ne? (How many children?)\n"
            "  wane (which, m) - Wane littafi kake karantawa? (Which book are you reading?)"
        ),
        "how_it_works": (
            "Drill the independent pronouns as a chant - ni, kai, ke, shi, "
            "ita, mu, ku, su - then attach each possessive suffix to gida, "
            "mota, and littafi until gidana, motarka, littafinta roll off "
            "the tongue. The demonstratives pair by distance: wannan/wancan "
            "for near/far singular, wadannan/wadancan for near/far plural. "
            "The interrogatives open every question in the questions record; "
            "practice each one with a real answer: Wa ya zo? - Abokina ya "
            "zo. Ina makaranta? - Tana kusa da kasuwa."
        ),
        "key_points": [
            "8 independent pronouns: ni, kai, ke, shi, ita, mu, ku, su.",
            "Possessive suffixes attach to nouns: -na, -nka/-nki, -nsa/-nta, -mu, -nku, -nsu.",
            "Demonstratives mark near/far and singular/plural: wannan, wadannan, wancan, wadancan.",
            "Interrogatives: wa, me/mene, ina, yaushe, ta yaya/ya, me ya sa, nawa, wane.",
            "These pronouns are the base of the tense-aspect markers (na, ina, zan...).",
        ],
        "requirements": [
            "Recite all eight independent pronouns and all eight possessive suffixes from memory.",
            "Attach possessives to five new nouns without looking.",
        ],
        "standards": [
            "Pronoun paradigms follow Newman 2000 and Jaggar 2001.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR],
        "must_contain": ["Ni malami ne", "Gidana yana nan", "Wannan littafina ne", "Wa ya zo", "Me ya sa ka yi kuka"],
        "sig_lens": (
            "Through the Signature lens the pronouns are the sworn persons "
            "of the sentence: ni the witness speaking, kai and ke the ones "
            "addressed and bound, shi and ita the ones testified about, mu "
            "ku su the companies of the covenant - each one a fixed seal "
            "that the verb-markers then date and time."
        ),
        "drill": {
            "independent": ["ni", "kai", "ke", "shi", "ita", "mu", "ku", "su"],
            "possessive": ["-na", "-nka", "-nki", "-nsa", "-nta", "-mu", "-nku", "-nsu"],
            "demonstratives": ["wannan", "wadannan", "wancan", "wadancan"],
            "interrogatives": ["wa", "me", "mene", "ina", "yaushe", "ta yaya",
                               "ya", "me ya sa", "nawa", "wane"],
            "sentences": 28,
        },
    }
)
ENTRIES.append(
    {
        "key": "numbers",
        "name": "Hausa Numbers and Time",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Counting to one hundred and beyond, ordinals, the days, the "
            "months, the clock, and the calendar - each with example "
            "sentences. Hausa numbers are beautifully regular once the tens "
            "are learned. \n\n"
            "One to ten:\n"
            "  1 daya - Ina da littafi daya. (I have one book.)\n"
            "  2 biyu - Yara biyu suna wasa. (Two children are playing.)\n"
            "  3 uku - Na saya mangwaro uku. (I bought three mangoes.)\n"
            "  4 hudu - Muna da kujeru hudu. (We have four chairs.)\n"
            "  5 biyar - Yana da shekaru biyar. (He is five years old.)\n"
            "  6 shida - Karfe shida na safe. (Six o'clock in the morning.)\n"
            "  7 bakwai - Kwana bakwai a sati. (Seven days in a week.)\n"
            "  8 takwas - Ta saya kwai takwas. (She bought eight eggs.)\n"
            "  9 tara - Tara da daya goma ne. (Nine plus one is ten.)\n"
            "  10 goma - Yana da naira goma. (He has ten naira.)\n\n"
            "Teens and tens:\n"
            "  11 sha daya - Yana da shekaru sha daya. (He is eleven years old.)\n"
            "  12 sha biyu - Akwai watanni sha biyu a shekara. (There are twelve months in a year.)\n"
            "  20 ashirin - Na biya naira ashirin. (I paid twenty naira.)\n"
            "  30 talatin - Mutane talatin sun zo. (Thirty people came.)\n"
            "  40 arba'in - Yana da shanu arba'in. (He has forty cows.)\n"
            "  50 hamsin - Farashin hamsin ne. (The price is fifty.)\n"
            "  60 sittin - Minti sittin a awa daya. (Sixty minutes in one hour.)\n"
            "  70 saba'in - Tana da shekaru saba'in. (She is seventy years old.)\n"
            "  80 tamanin - Kilomita tamanin ne. (It is eighty kilometers.)\n"
            "  90 tis'in - Yana da littattafai tis'in. (He has ninety books.)\n"
            "  100 dari - Mutane dari sun hallara. (One hundred people attended.)\n"
            "  1000 dubu - Na biya dubu daya. (I paid one thousand.)\n\n"
            "Ordinals: na farko (first) - Shi ne na farko. (He is the first.); "
            "na biyu (second); na uku (third). \n\n"
            "Days of the week:\n"
            "  Litinin (Monday) - Zan tafi Litinin. (I will go on Monday.)\n"
            "  Talata (Tuesday) - Mun hadu Talata. (We met on Tuesday.)\n"
            "  Laraba (Wednesday) - Kasuwa Laraba ce. (The market is on Wednesday.)\n"
            "  Alhamis (Thursday) - Zai zo Alhamis. (He will come on Thursday.)\n"
            "  Jumma'a (Friday) - Jumma'a ranar salla ce. (Friday is the prayer day.)\n"
            "  Asabar (Saturday) - Asabar ranar hutu ce. (Saturday is the rest day.)\n"
            "  Lahadi (Sunday) - Yau Lahadi ne. (Today is Sunday.)\n\n"
            "Months: Janairu, Fabrairu, Maris, Afrilu, Mayu, Yuni, Yuli, "
            "Agusta, Satumba, Oktoba, Nuwamba, Disamba. - An haife ni a "
            "watan Janairu. (I was born in the month of January.) \n\n"
            "Clock time (karfe = o'clock):\n"
            "  Karfe daya. (It is one o'clock.)\n"
            "  Karfe biyu da rabi. (It is half past two.)\n"
            "  Karfe uku da minti goma. (It is ten minutes past three.)\n"
            "  Karfe nawa ne? (What time is it?)"
        ),
        "how_it_works": (
            "Memorize 1-10 and the tens cold; the teens are sha plus the "
            "unit (sha daya, sha biyu), and compound numbers join with da "
            "(and): ashirin da biyar (twenty-five), dari da goma (one "
            "hundred and ten). Practice the clock by saying the real time "
            "in Hausa every hour: karfe + number, da rabi for half past, da "
            "minti + number for minutes. Run the week as a chant - Litinin, "
            "Talata, Laraba, Alhamis, Jumma'a, Asabar, Lahadi - and the "
            "year as Janairu through Disamba."
        ),
        "key_points": [
            "1-10: daya, biyu, uku, hudu, biyar, shida, bakwai, takwas, tara, goma.",
            "Teens: sha + unit (sha daya); tens: ashirin, talatin, arba'in, hamsin, sittin, saba'in, tamanin, tis'in; 100 dari, 1000 dubu.",
            "Compounds join with da: ashirin da biyar (25).",
            "Days: Litinin, Talata, Laraba, Alhamis, Jumma'a, Asabar, Lahadi.",
            "Months: Janairu, Fabrairu, Maris, Afrilu, Mayu, Yuni, Yuli, Agusta, Satumba, Oktoba, Nuwamba, Disamba.",
            "Clock: karfe + number; karfe biyu da rabi (2:30).",
        ],
        "requirements": [
            "Count 1-100 aloud without hesitation.",
            "Tell the current time and today's date in Hausa.",
        ],
        "standards": [
            "Number words follow the standard Kano forms in Abraham 1962 and Newman 2000.",
        ],
        "citations": [CIT_ABRAHAM, CIT_NEWMAN],
        "must_contain": ["sha daya", "ashirin", "dari", "Karfe biyu da rabi", "Jumma'a", "Yau Lahadi ne"],
        "sig_lens": (
            "Through the Signature lens numbers are the sworn measures: "
            "each count a sealed tally, each day a dated witness, each hour "
            "a stamped hour - the language keeping its own accounts in "
            "full, the way a covenant keeps its ledger."
        ),
        "drill": {
            "units": ["daya", "biyu", "uku", "hudu", "biyar", "shida",
                      "bakwai", "takwas", "tara", "goma"],
            "tens": ["goma", "ashirin", "talatin", "arba'in", "hamsin",
                     "sittin", "saba'in", "tamanin", "tis'in", "dari"],
            "days": ["Litinin", "Talata", "Laraba", "Alhamis", "Jumma'a",
                     "Asabar", "Lahadi"],
            "months": ["Janairu", "Fabrairu", "Maris", "Afrilu", "Mayu",
                       "Yuni", "Yuli", "Agusta", "Satumba", "Oktoba",
                       "Nuwamba", "Disamba"],
            "sentences": 32,
        },
    }
)

ENTRIES.append(
    {
        "key": "greetings",
        "name": "Hausa Greetings and Everyday Phrases",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Thirty greetings, farewells, and politeness phrases with usage "
            "notes. Hausa greeting is a full social ritual: you greet the "
            "person, their work, their household, and their health before "
            "any business begins. The core word is sannu, and it multiplies "
            "into dozens of forms. \n\n"
            "  Sannu! - Hello! (the universal greeting)\n"
            "  Sannu da zuwa. - Welcome. (greeting an arrival)\n"
            "  Sannu da aiki. - Greetings on your work. (to someone working)\n"
            "  Sannu da kokari. - Greetings on your effort. (encouragement)\n"
            "  Barka da zuwa. - Welcome, blessed arrival.\n"
            "  Sannu da safe. - Good morning.\n"
            "  Sannu da rana. - Good afternoon.\n"
            "  Sannu da dare. - Good evening.\n"
            "  Ina kwana? - Good morning. (lit. how did you pass the night?)\n"
            "  Ina yini? - Good afternoon/evening. (lit. how did you pass the day?)\n"
            "  Sannu da hutu. - Happy holiday. (greeting on a day off)\n"
            "  Barka da salla. - Blessed festival. (Eid greeting)\n"
            "  Lafiya lau. - I am fine. (the standard reply)\n"
            "  Lafiya kalau. - I am very well.\n"
            "  Kana lafiya? - Are you well? (to a man)\n"
            "  Kina lafiya? - Are you well? (to a woman)\n"
            "  Sunanka me ne? - What is your name? (to a man)\n"
            "  Sunanki me ne? - What is your name? (to a woman)\n"
            "  Sunana ... - My name is ...\n"
            "  Na ji dadin haduwa da kai. - Nice to meet you. (to a man)\n"
            "  Na ji dadin haduwa da ke. - Nice to meet you. (to a woman)\n"
            "  Na gode. - Thank you.\n"
            "  Na gode sosai. - Thank you very much.\n"
            "  Madalla! - Well done! Bravo!\n"
            "  Don Allah. - Please. (lit. for God)\n"
            "  Yi hakuri. - Excuse me. / Be patient.\n"
            "  Sai wata rana. - See you another day.\n"
            "  Sai an jima. - See you soon. (lit. until after a while)\n"
            "  Allah ya kiyaye ka. - Goodbye. (lit. may God protect you, to a man)\n"
            "  Allah ya albarkace ka. - God bless you. (to a man)\n\n"
            "Usage notes. Always answer a greeting before stating business; "
            "to skip the greeting ritual is rude. Sannu da aiki is said to "
            "anyone visibly working - farmers, builders, traders. Ina kwana "
            "belongs to the morning, ina yini to the afternoon and evening. "
            "Men and women use the -ka/-ki endings to address each other: "
            "kana lafiya to a man, kina lafiya to a woman."
        ),
        "how_it_works": (
            "Practice greetings as exchanges, not single lines: one learner "
            "says Sannu da safe, the other answers Lafiya lau, sai kuma? "
            "(and you?). Chain them: arrival (Sannu da zuwa), work-greeting "
            "(Sannu da aiki), health-check (Kana lafiya?), thanks (Na gode), "
            "farewell (Sai an jima / Allah ya kiyaye ka). Drill the "
            "masculine/feminine address pairs - sunanka/sunanki, kana/kina, "
            "da kai/da ke - until the ear picks the right one without "
            "thinking."
        ),
        "key_points": [
            "30 greetings, farewells, and politeness phrases with usage notes.",
            "Sannu is the root greeting; it multiplies by occasion.",
            "Greeting is a ritual: greet, ask health, then do business.",
            "Ina kwana (morning) / ina yini (afternoon/evening) mark the day.",
            "Address endings agree with the hearer: -ka masculine, -ki feminine.",
        ],
        "requirements": [
            "Carry a full greeting exchange - hello, health, thanks, farewell - without notes.",
            "Use the correct -ka/-ki forms for men and women.",
        ],
        "standards": [
            "Greeting forms are the standard Kano-dialect forms documented in the reference grammars.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR, CIT_ABRAHAM],
        "must_contain": ["Sannu da aiki", "Ina kwana", "Lafiya lau", "Na gode sosai", "Sai an jima"],
        "sig_lens": (
            "Through the Signature lens every greeting is a sworn "
            "recognition: sannu the seal of presence, lafiya lau the seal "
            "of wellness witnessed aloud, na gode the seal of gratitude, "
            "sai an jima the seal of promised return - no one passes "
            "another in the archive unacknowledged."
        ),
        "drill": {
            "phrases": [
                ("Sannu!", "Hello!"), ("Sannu da zuwa.", "Welcome."),
                ("Sannu da aiki.", "Greetings on your work."),
                ("Sannu da kokari.", "Greetings on your effort."),
                ("Barka da zuwa.", "Welcome, blessed arrival."),
                ("Sannu da safe.", "Good morning."),
                ("Sannu da rana.", "Good afternoon."),
                ("Sannu da dare.", "Good evening."),
                ("Ina kwana?", "Good morning."),
                ("Ina yini?", "Good afternoon/evening."),
                ("Sannu da hutu.", "Happy holiday."),
                ("Barka da salla.", "Blessed festival."),
                ("Lafiya lau.", "I am fine."),
                ("Lafiya kalau.", "I am very well."),
                ("Kana lafiya?", "Are you well? (m)"),
                ("Kina lafiya?", "Are you well? (f)"),
                ("Sunanka me ne?", "What is your name? (m)"),
                ("Sunanki me ne?", "What is your name? (f)"),
                ("Sunana ...", "My name is ..."),
                ("Na ji dadin haduwa da kai.", "Nice to meet you. (m)"),
                ("Na ji dadin haduwa da ke.", "Nice to meet you. (f)"),
                ("Na gode.", "Thank you."),
                ("Na gode sosai.", "Thank you very much."),
                ("Madalla!", "Well done!"),
                ("Don Allah.", "Please."),
                ("Yi hakuri.", "Excuse me. / Be patient."),
                ("Sai wata rana.", "See you another day."),
                ("Sai an jima.", "See you soon."),
                ("Allah ya kiyaye ka.", "Goodbye. (m)"),
                ("Allah ya albarkace ka.", "God bless you. (m)"),
            ],
        },
    }
)
ENTRIES.append(
    {
        "key": "grammar",
        "name": "Hausa Grammar Essentials",
        "group": "Grammar Essentials",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The ten load-bearing rules of Hausa grammar, each with "
            "translated example sentences. Learn these ten and you can "
            "assemble correct sentences on any topic. \n\n"
            "1. Word order is subject-verb-object. Yaro ya ci abinci. "
            "(The boy ate food.) Uwa tana dafa tuwo. (Mother is cooking "
            "tuwo.) \n\n"
            "2. Tense and aspect ride on pronoun markers. Na tafi. (I went.) "
            "Ina tafiya. (I am going.) Zan tafi. (I will go.) Kan tafi. "
            "(You usually go.) Ka tafi. (You went / you go.) \n\n"
            "3. Nouns have gender: masculine or feminine. Feminine nouns "
            "often end in -a: mota (car), kofa (door), rana (sun), kasuwa "
            "(market). The verb agrees: namiji ya zo (the man came), mace "
            "ta zo (the woman came). \n\n"
            "4. Plurals take several shapes. yaro/yara (boy/boys), mutum/"
            "mutane (person/people), littafi/littattafai (book/books), gida/"
            "gidaje (house/houses), tebur/tebura (table/tables), mota/motoci "
            "(car/cars). Yara suna wasa. (The children are playing.) \n\n"
            "5. There are no articles. littafi means a book or the book as "
            "the context decides: Na saya littafi. (I bought a book.) "
            "Littafin yana nan. (The book is here - with the possessive the "
            "meaning narrows.) \n\n"
            "6. Negation wraps the verb in ba ... ba. Ban tafi ba. (I did "
            "not go.) Ba ya son tuwo. (He does not like tuwo.) Ba ruwana. "
            "(It is none of my business - lit. not my water.) \n\n"
            "7. Questions use rising intonation, question words, or the "
            "particle shin. Kana lafiya? (Are you well?) Ina makaranta? "
            "(Where is the school?) Shin za ka zo? (Will you come?) \n\n"
            "8. Adjectives follow the noun and often agree in gender. gida "
            "babba (big house), mota sabuwa (new car), yaro karami (small "
            "boy), yarinya karama (small girl). \n\n"
            "9. The copula ne (masculine) / ce (feminine) means is/are in "
            "naming sentences. Shi ne malami. (He is a teacher.) Ita ce "
            "malama. (She is a teacher.) Wannan gida ne. (This is a house.) \n\n"
            "10. Possession links noun to owner: littafin yaro (the boy's "
            "book), motar mace (the woman's car), gidajen mutane (people's "
            "houses). The link word na/ta agrees with the owned thing: "
            "littafi na yaro, mota ta mace."
        ),
        "how_it_works": (
            "Take each rule and generate five of your own sentences with it "
            "before moving on: five SVO sentences, five ba ... ba "
            "negations, five ne/ce namings, five adjective-after-noun "
            "phrases. Then combine rules: negate a tense sentence (Ban je "
            "kasuwa ba - I did not go to the market), question a naming "
            "sentence (Shin shi ne malami? - Is he the teacher?), pluralize "
            "a possessed noun (littattafan yara - the children's books). "
            "The combination drills are where the grammar becomes yours."
        ),
        "key_points": [
            "SVO word order; adjectives follow nouns.",
            "Pronoun markers carry tense/aspect: na, ina, zan, kan, ka.",
            "Masculine/feminine gender; verb and adjective agreement.",
            "Plurals: yara, mutane, littattafai, gidaje, tebura, motoci.",
            "Negation: ba ... ba wraps the verb.",
            "Questions: intonation, question words, or shin.",
            "Copula ne/ce; possession via the na/ta link.",
        ],
        "requirements": [
            "Write five correct sentences per rule from memory.",
            "Combine at least three rules in single sentences.",
        ],
        "standards": [
            "Grammar follows the standard reference analysis in Newman 2000 and Jaggar 2001.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR],
        "must_contain": ["Yaro ya ci abinci", "Ban tafi ba", "Shi ne malami", "yaro/yara", "gida babba"],
        "sig_lens": (
            "Through the Signature lens these ten rules are the ten sworn "
            "articles of sentence law: each one a covenant clause - the "
            "subject shall precede, the verb shall carry its marker-seal, "
            "the negation shall wrap both sides - so every sentence built "
            "in the archive stands lawful and whole."
        ),
        "drill": {
            "rules": 10,
            "markers": {"past_1sg": "na", "cont_1sg": "ina", "fut_1sg": "zan",
                        "habit_2sgm": "kan", "past_2sgm": "ka"},
            "plurals": [("yaro", "yara"), ("mutum", "mutane"),
                        ("littafi", "littattafai"), ("gida", "gidaje"),
                        ("tebur", "tebura"), ("mota", "motoci")],
            "rule_sentences": [
                "Yaro ya ci abinci.", "Na tafi.", "Ina tafiya.", "Zan tafi.",
                "Ban tafi ba.", "Shi ne malami.", "Ita ce malama.",
                "gida babba", "mota sabuwa",
            ],
        },
    }
)
ENTRIES.append(
    {
        "key": "home",
        "name": "Hausa Home and Family Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Twenty sentences for the house and the family: rooms, "
            "furniture, and the people who fill them. \n\n"
            "  1. Gidamu yana kusa da kasuwa. (Our house is near the market.)\n"
            "  2. Uba yana aiki a gona. (Father is working on the farm.)\n"
            "  3. Uwa tana dafa abinci a madafa. (Mother is cooking food in the kitchen.)\n"
            "  4. Yara suna wasa a farfajiya. (The children are playing in the courtyard.)\n"
            "  5. Daki nawa yana sama. (My room is upstairs.)\n"
            "  6. Kujeru suna cikin falo. (The chairs are in the sitting room.)\n"
            "  7. Gadona yana kusa da taga. (My bed is near the window.)\n"
            "  8. Dan uwana ya zo daga Kano. (My brother came from Kano.)\n"
            "  9. Yar uwata tana karatu a makaranta. (My sister is studying at school.)\n"
            "  10. Kakana yana zaune a karkashin itace. (My grandfather is sitting under the tree.)\n"
            "  11. Muna cin abincin dare tare. (We are eating dinner together.)\n"
            "  12. Ruwa yana cikin tukunya a madafa. (There is water in the pot in the kitchen.)\n"
            "  13. Fitila tana haskakawa daki. (The lamp is lighting the room.)\n"
            "  14. Kofa ta gida a bude take. (The house door is open.)\n"
            "  15. Muna da karnuka biyu a gida. (We have two dogs at home.)\n"
            "  16. Abokina ya kwana a gidanmu jiya. (My friend spent the night at our house yesterday.)\n"
            "  17. Iyayena suna son zaman gida. (My parents love staying at home.)\n"
            "  18. Yaronku yana kuka, me ya same shi? (Your child is crying, what happened to him?)\n"
            "  19. Mun gina sabon daki a bayan gida. (We built a new room behind the house.)\n"
            "  20. Gida mai dadi, gida mai albarka. (A pleasant home, a blessed home.)"
        ),
        "how_it_works": (
            "Walk through your own house naming everything in Hausa - kofa, "
            "taga, kujera, tebur, gado, fitila, madafa, falo, farfajiya - "
            "then place your family in it with sentences: ubana yana nan, "
            "uwata tana can. The possessive suffixes (-na, -nka, -mu) do "
            "heavy work here; attach them to every room and relative until "
            "gidana, dakina, dan uwana are automatic."
        ),
        "key_points": [
            "20 sentences: house, rooms, furniture, family members.",
            "Room words: daki (room), madafa (kitchen), falo (sitting room), farfajiya (courtyard).",
            "Family: uba (father), uwa (mother), dan uwa (brother), yar uwa (sister), kaka (grandparent).",
            "Possessive suffixes carry the family relations.",
        ],
        "requirements": [
            "Describe your own house and family in ten Hausa sentences.",
        ],
        "standards": [
            "Vocabulary follows Abraham 1962; sentences in standard Kano grammar.",
        ],
        "citations": [CIT_ABRAHAM, CIT_NEWMAN],
        "must_contain": ["Uwa tana dafa abinci a madafa", "Kakana yana zaune a karkashin itace", "farfajiya", "Muna cin abincin dare tare"],
        "sig_lens": (
            "Through the Signature lens the home sentences are the sworn "
            "census of the household: each room named, each relative "
            "placed, each meal witnessed - the family archive sealed under "
            "one roof."
        ),
        "drill": {
            "rooms": ["daki", "madafa", "falo", "farfajiya"],
            "family": ["uba", "uwa", "dan uwa", "yar uwa", "kaka", "jika"],
            "sentences": 20,
        },
    }
)
ENTRIES.append(
    {
        "key": "food",
        "name": "Hausa Food and Cooking Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for meals, ingredients, cooking actions, and "
            "the restaurant: the language of the Hausa kitchen, where tuwo, "
            "miya, and kunu rule the table. \n\n"
            "  1. Uwa tana dafa tuwo a madafa. (Mother is cooking tuwo in the kitchen.)\n"
            "  2. Miyan kuka tana da dadi sosai. (Baobab-leaf soup is very delicious.)\n"
            "  3. Na ci shinkafa da nama a abincin rana. (I ate rice with meat for lunch.)\n"
            "  4. Kunu mai sanyi yana kashe kishirwa. (Cold kunu quenches thirst.)\n"
            "  5. Ki kawo mini cokali da faranti. (Bring me a spoon and a plate - to a woman.)\n"
            "  6. Wannan abincin yayi zafi, a hankali. (This food is hot, carefully.)\n"
            "  7. Ina son dankali da kwai da safe. (I like potatoes and eggs in the morning.)\n"
            "  8. Ta yanka albasa da tumatir. (She chopped onions and tomatoes.)\n"
            "  9. Mun saya kayan miya a kasuwa. (We bought soup ingredients at the market.)\n"
            "  10. Gishiri kadan ya isa. (A little salt is enough.)\n"
            "  11. Mai ya yi yawa a miyar. (There is too much oil in the soup.)\n"
            "  12. Ruwa ya tafasa, sa shinkafa. (The water has boiled, add the rice.)\n"
            "  13. Yara suna cin kosai a waje. (The children are eating bean cakes outside.)\n"
            "  14. Nawa ne farashin tuwon? (How much is the tuwo?)\n"
            "  15. Mai gidan abinci ya kawo mana menu. (The restaurant owner brought us the menu.)\n"
            "  16. Muna bukatar tebur na mutane hudu. (We need a table for four people.)\n"
            "  17. Abincin ya iso, mu ci lafiya. (The food has arrived, let us eat in health.)\n"
            "  18. Na koshi, na gode. (I am full, thank you.)\n"
            "  19. Wannan magani? A'a, kayan zaki ne. (This medicine? No, it is candy.)\n"
            "  20. Kaza da shinkafa ita ce abincin da na fi so. (Chicken with rice is my favorite food.)"
        ),
        "how_it_works": (
            "Cook one Hausa dish in your head - or in your kitchen - "
            "narrating every step: na yanka albasa (I chopped the onions), "
            "na sa gishiri (I added salt), ruwa ya tafasa (the water "
            "boiled). At a restaurant, run the full script: greeting, table "
            "for four, the menu, ordering, the food has arrived, I am full, "
            "paying. Taste words (dadi, daci, zafi, sanyi) pair with every "
            "dish."
        ),
        "key_points": [
            "20 sentences: meals, ingredients, cooking actions, restaurant.",
            "Staple dishes: tuwo, miya (miyan kuka), kunu, kosai.",
            "Cooking verbs: dafa (cook), yanka (cut/chop), sa (put/add), tafasa (boil).",
            "Restaurant script: table, menu, order, eat, pay.",
            "Polite fullness: na koshi, na gode.",
        ],
        "requirements": [
            "Narrate cooking a meal in ten Hausa sentences.",
            "Order a full meal at a restaurant in Hausa.",
        ],
        "standards": [
            "Food vocabulary follows Abraham 1962; sentences in standard Kano grammar.",
        ],
        "citations": [CIT_ABRAHAM, CIT_NEWMAN],
        "must_contain": ["Miyan kuka tana da dadi sosai", "Kunu mai sanyi yana kashe kishirwa", "Na koshi, na gode", "Abincin ya iso, mu ci lafiya"],
        "sig_lens": (
            "Through the Signature lens the food sentences are the sworn "
            "record of the table: each ingredient witnessed, each pot "
            "sealed, each shared meal a covenant renewed - for in the "
            "archive, to eat together is to sign together."
        ),
        "drill": {
            "dishes": ["tuwo", "miyan kuka", "kunu", "kosai", "shinkafa"],
            "cooking_verbs": ["dafa", "yanka", "sa", "tafasa"],
            "sentences": 20,
        },
    }
)
ENTRIES.append(
    {
        "key": "travel",
        "name": "Hausa Travel and Directions Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the road: transport, asking directions, "
            "tickets, and lodging - the traveler's Hausa from Kano to "
            "Niamey. \n\n"
            "  1. Ina so in je Kano gobe da safe. (I want to go to Kano tomorrow morning.)\n"
            "  2. Mota ta tashi karfe shida. (The vehicle departs at six o'clock.)\n"
            "  3. Nawa ne kudin mota zuwa Zaria? (How much is the fare to Zaria?)\n"
            "  4. Ina tashar mota? (Where is the motor park?)\n"
            "  5. Hanya zuwa kasuwa ta ina take? (Which way is the road to the market?)\n"
            "  6. Tafi kai tsaye, sai ka juya dama. (Go straight, then turn right.)\n"
            "  7. Juya hagu a mahadar farko. (Turn left at the first junction.)\n"
            "  8. Gidan yana kusa da masallaci. (The house is near the mosque.)\n"
            "  9. Nisa ne? Ko kusa ne? (Is it far? Or near?)\n"
            "  10. Na biya kudin tikiti biyu. (I paid for two tickets.)\n"
            "  11. Jirgin sama zai tashi karfe takwas. (The airplane will depart at eight o'clock.)\n"
            "  12. Ina otal mai kyau a nan? (Is there a good hotel here?)\n"
            "  13. Ina so daki na kwana daya. (I want a room for one night.)\n"
            "  14. Dakin yana da ban daki? (Does the room have a bathroom?)\n"
            "  15. Muna bukatar jagora mai magana da Hausa. (We need a guide who speaks Hausa.)\n"
            "  16. Hanya ta lalace saboda ruwan sama. (The road is spoiled because of the rain.)\n"
            "  17. Direba, a hankali, don Allah. (Driver, slowly, please.)\n"
            "  18. Mun iso lafiya, alhamdulillah. (We arrived safely, praise God.)\n"
            "  19. Sai ka wuce gadar, gidan yana can. (Go past the bridge, the house is there.)\n"
            "  20. Tafiya mai kyau! Allah ya kiyaye hanya. (Have a good trip! May God guard the road.)"
        ),
        "how_it_works": (
            "Rehearse the travel loop in order: plan (ina so in je...), "
            "fare (nawa ne kudin mota...), directions (hanya zuwa... ta ina "
            "take?), lodging (ina so daki...), arrival (mun iso lafiya). "
            "Direction words are few and carry far: dama (right), hagu "
            "(left), kai tsaye (straight), juya (turn), wuce (pass), kusa "
            "(near), nisa (far). Practice giving directions to real places "
            "on your own map until the sequence flows."
        ),
        "key_points": [
            "20 sentences: transport, directions, tickets, lodging.",
            "Key direction words: dama, hagu, kai tsaye, juya, wuce, mahada (junction).",
            "Fare and ticket phrases: nawa ne kudin mota, na biya kudin tikiti.",
            "Lodging: daki na kwana daya; dakin yana da ban daki?",
            "Arrival blessing: mun iso lafiya, alhamdulillah.",
        ],
        "requirements": [
            "Ask for and give directions to five places in Hausa.",
            "Book transport and a hotel room in a role-play.",
        ],
        "standards": [
            "Travel vocabulary follows standard usage in the reference grammars.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR, CIT_ABRAHAM],
        "must_contain": ["Nawa ne kudin mota zuwa Zaria", "Tafi kai tsaye, sai ka juya dama", "Mun iso lafiya, alhamdulillah", "Ina tashar mota"],
        "sig_lens": (
            "Through the Signature lens the travel sentences are the sworn "
            "itinerary: each road named, each fare sealed, each arrival "
            "witnessed with alhamdulillah - the traveler's covenant that "
            "every journey in the archive is accounted for, mile by mile."
        ),
        "drill": {
            "directions": ["dama", "hagu", "kai tsaye", "juya", "wuce", "mahada"],
            "transport": ["mota", "jirgin sama", "tashar mota", "tikiti", "direba"],
            "sentences": 20,
        },
    }
)
ENTRIES.append(
    {
        "key": "work",
        "name": "Hausa Work and School Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for jobs, the office, the classroom, and "
            "learning - the working day in Hausa. \n\n"
            "  1. Ina aiki a asibiti. (I work at the hospital.)\n"
            "  2. Shi ma'aikacin banki ne. (He is a bank worker.)\n"
            "  3. Ta fara aiki karfe takwas na safe. (She starts work at eight in the morning.)\n"
            "  4. Muna da taro karfe goma. (We have a meeting at ten o'clock.)\n"
            "  5. Shugabana mutum ne mai adalci. (My boss is a just person.)\n"
            "  6. Aikin ya yi yawa yau. (There is a lot of work today.)\n"
            "  7. Na gama rahoton. (I finished the report.)\n"
            "  8. Yara suna karatu a makaranta. (The children are studying at school.)\n"
            "  9. Malam ya shiga aji. (The teacher entered the classroom.)\n"
            "  10. Dalibai suna rubuta jarabawa. (The students are writing an exam.)\n"
            "  11. Wannan darasi mai wahala ne. (This lesson is difficult.)\n"
            "  12. Na fahimci darasin yau. (I understood today's lesson.)\n"
            "  13. Ki bude littafinki shafi na goma. (Open your book to page ten - to a girl.)\n"
            "  14. Tambaya mai kyau, wanene zai amsa? (A good question, who will answer?)\n"
            "  15. Ina koyon Hausa kullum. (I am learning Hausa every day.)\n"
            "  16. Harshen Hausa yana da dadin karatu. (The Hausa language is pleasant to study.)\n"
            "  17. Mun samu hutu na mako biyu. (We got a two-week break.)\n"
            "  18. Albashina ya iso. (My salary arrived.)\n"
            "  19. Sana'ata ita ce noma. (My trade is farming.)\n"
            "  20. Ilimi shi ne gishirin rayuwa. (Knowledge is the salt of life.)"
        ),
        "how_it_works": (
            "Run your workday in Hausa from arrival to departure: na fara "
            "aiki (I started work), muna da taro (we have a meeting), na "
            "gama rahoton (I finished the report), na tafi gida (I went "
            "home). In the classroom, practice the teacher's commands - "
            "bude littafinki, rubuta, amsa tambaya - and the student's "
            "replies - na fahimta (I understood), ban fahimta ba (I did not "
            "understand). The proverb that closes the record, ilimi shi ne "
            "gishirin rayuwa, is worth memorizing whole."
        ),
        "key_points": [
            "20 sentences: jobs, office, classroom, learning.",
            "Work words: aiki, ma'aikaci, shugaba, taro, rahoton, albashi, sana'a.",
            "School words: makaranta, malam, dalibi, aji, darasi, jarabawa.",
            "Classroom commands and replies drilled as pairs.",
        ],
        "requirements": [
            "Describe your job or studies in ten Hausa sentences.",
            "Give and follow five classroom commands.",
        ],
        "standards": [
            "Vocabulary follows Abraham 1962; sentences in standard Kano grammar.",
        ],
        "citations": [CIT_ABRAHAM, CIT_NEWMAN],
        "must_contain": ["Ina aiki a asibiti", "Malam ya shiga aji", "Ilimi shi ne gishirin rayuwa", "Na fahimci darasin yau"],
        "sig_lens": (
            "Through the Signature lens the work sentences are the sworn "
            "ledger of labor: each task named, each lesson witnessed, each "
            "salary sealed - for work honestly recorded is a covenant kept "
            "with the day."
        ),
        "drill": {
            "work_words": ["aiki", "ma'aikaci", "shugaba", "taro", "rahoton", "albashi", "sana'a"],
            "school_words": ["makaranta", "malam", "dalibi", "aji", "darasi", "jarabawa"],
            "sentences": 20,
        },
    }
)

ENTRIES.append(
    {
        "key": "health",
        "name": "Hausa Health and Body Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for body parts, symptoms, the doctor visit, "
            "and the pharmacy - the language you need when it matters most. \n\n"
            "  1. Jikina yana ciwo. (My body aches.)\n"
            "  2. Ina da zazzabi. (I have a fever.)\n"
            "  3. Kaina yana ciwo sosai. (My head hurts a lot.)\n"
            "  4. Cikina yana ciwo. (My stomach hurts.)\n"
            "  5. Ina tari da mura. (I have a cough and a cold.)\n"
            "  6. Ido na yana kaikayi. (My eye is itching.)\n"
            "  7. Hakora na yana ciwo. (My tooth hurts.)\n"
            "  8. Ba na jin dadin jikina. (I do not feel well in my body.)\n"
            "  9. Ina bukatar likita. (I need a doctor.)\n"
            "  10. Asibitin yana ina? (Where is the hospital?)\n"
            "  11. Likita ya duba ni. (The doctor examined me.)\n"
            "  12. Ya rubuta mini magani. (He prescribed medicine for me.)\n"
            "  13. Ina da ciwon sanyi. (I have malaria - lit. cold sickness.)\n"
            "  14. Sha magani sau uku a rana. (Take the medicine three times a day.)\n"
            "  15. Kada ka ci abinci mai zafi. (Do not eat hot food.)\n"
            "  16. Sha ruwa mai yawa. (Drink plenty of water.)\n"
            "  17. Ina bukatar hutu na kwana biyu. (I need two days of rest.)\n"
            "  18. Marasa lafiya suna jiran likita. (The patients are waiting for the doctor.)\n"
            "  19. Kantin magani yana kusa da asibiti. (The pharmacy is near the hospital.)\n"
            "  20. Allah ya ba ka lafiya. (May God grant you health.)"
        ),
        "how_it_works": (
            "Learn the body map first - kai (head), ido (eye), hakori "
            "(tooth), ciki (stomach), jiki (body) - then hang symptoms on "
            "it: ...yana ciwo (hurts), ina da zazzabi (I have fever), ina "
            "da tari (I have cough). The doctor-visit script runs: ina "
            "bukatar likita, likita ya duba ni, ya rubuta mini magani, sha "
            "magani sau uku a rana. Practice describing three different "
            "ailments fluently; in a real clinic, clarity is care."
        ),
        "key_points": [
            "20 sentences: body parts, symptoms, doctor visit, pharmacy.",
            "Pain pattern: X yana ciwo; illness pattern: ina da X.",
            "Doctor script: need, examination, prescription, dosage.",
            "Pharmacy: kantin magani; dosage: sau uku a rana.",
            "Healing wish: Allah ya ba ka lafiya.",
        ],
        "requirements": [
            "Describe three ailments and a full doctor visit in Hausa.",
            "Name ten body parts from memory.",
        ],
        "standards": [
            "Medical vocabulary follows standard Hausa usage in the reference dictionaries.",
        ],
        "citations": [CIT_ABRAHAM, CIT_NEWMAN],
        "must_contain": ["Jikina yana ciwo", "Ina da zazzabi", "Likita ya duba ni", "Allah ya ba ka lafiya"],
        "sig_lens": (
            "Through the Signature lens the health sentences are the sworn "
            "testimony of the body: each pain named truly, each remedy "
            "sealed with its measure, each recovery wished aloud - for the "
            "archive records the body as faithfully as it records the word."
        ),
        "drill": {
            "body": ["kai", "ido", "hakori", "ciki", "jiki"],
            "symptoms": ["zazzabi", "tari", "mura", "ciwon sanyi"],
            "sentences": 20,
        },
    }
)
ENTRIES.append(
    {
        "key": "emotions",
        "name": "Hausa Emotions and Feelings Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the inner life: happiness, sadness, "
            "anger, fear, love, and surprise - feelings in Hausa, where "
            "the heart (zuciya) does much of the talking. \n\n"
            "  1. Ina farin ciki sosai yau. (I am very happy today.)\n"
            "  2. Zuciyata tana cike da murna. (My heart is full of joy.)\n"
            "  3. Ya yi dariya da karfi. (He laughed loudly.)\n"
            "  4. Ina bakin ciki. (I am sad - lit. I am in blackness of heart.)\n"
            "  5. Ta yi kuka saboda labarin. (She cried because of the news.)\n"
            "  6. Yana fushi da ni. (He is angry with me.)\n"
            "  7. Kada ka yi fushi, don Allah. (Do not be angry, please.)\n"
            "  8. Ina jin tsoro. (I feel fear.)\n"
            "  9. Kar ka ji tsoro, ina tare da kai. (Do not be afraid, I am with you.)\n"
            "  10. Ina son ka kwarai. (I love you truly - to a man.)\n"
            "  11. Soyayya tana da dadi. (Love is sweet.)\n"
            "  12. Na yi mamaki da ganin shi. (I was surprised to see him.)\n"
            "  13. Wannan abin mamaki ne! (This is surprising!)\n"
            "  14. Ina jin kunya. (I feel shy / ashamed.)\n"
            "  15. Yana alfahari da dansa. (He is proud of his son.)\n"
            "  16. Zuciyata ta yi sanyi. (I am relieved - lit. my heart cooled.)\n"
            "  17. Ina kewar gida. (I am homesick - lit. I miss home.)\n"
            "  18. Ta ji dadin kyautar. (She was pleased with the gift.)\n"
            "  19. Fushi ba ya maganin komai. (Anger cures nothing.)\n"
            "  20. Hakuri shi ne maganin zuciya. (Patience is the medicine of the heart.)"
        ),
        "how_it_works": (
            "Hausa feelings live in the zuciya (heart): farin ciki "
            "(happiness, white heart), bakin ciki (sadness, black heart), "
            "zuciyata ta yi sanyi (relief, my heart cooled). Learn the "
            "heart-idioms as whole units - never translate them word by "
            "word. Practice the emotion pairs as opposites: farin ciki / "
            "bakin ciki, murna / kuka, so / fushi, tsoro / kwanciyar hankali "
            "(calm). Then narrate your own day emotionally: da safe na ji "
            "dadin..., da rana na yi fushi saboda..., yanzu zuciyata ta yi "
            "sanyi."
        ),
        "key_points": [
            "20 sentences: happy, sad, angry, afraid, love, surprise.",
            "The heart (zuciya) carries feelings: farin ciki, bakin ciki.",
            "Idioms learned whole: zuciyata ta yi sanyi, ina kewar gida.",
            "Comfort phrases: kar ka ji tsoro, ina tare da kai.",
        ],
        "requirements": [
            "Narrate an emotional day using ten feeling sentences.",
            "Use five heart-idioms correctly in context.",
        ],
        "standards": [
            "Idioms follow documented Hausa usage in Abraham 1962 and Newman 2000.",
        ],
        "citations": [CIT_ABRAHAM, CIT_NEWMAN],
        "must_contain": ["Ina farin ciki sosai yau", "Ina bakin ciki", "Zuciyata ta yi sanyi", "Hakuri shi ne maganin zuciya"],
        "sig_lens": (
            "Through the Signature lens the emotion sentences are the sworn "
            "record of the heart: each joy sealed white, each sorrow sealed "
            "in witness, each comfort spoken as a vow - for the archive "
            "holds feelings as evidence, not as decoration."
        ),
        "drill": {
            "feelings": ["farin ciki", "bakin ciki", "murna", "fushi", "tsoro", "soyayya", "mamaki", "kunya"],
            "heart_idioms": ["zuciyata ta yi sanyi", "ina kewar gida", "hakuri shi ne maganin zuciya"],
            "sentences": 20,
        },
    }
)
ENTRIES.append(
    {
        "key": "nature",
        "name": "Hausa Nature and Weather Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for animals, plants, the seasons, and weather "
            "talk - the Sahel in Hausa, from harmattan dust to rainy-season "
            "thunder. \n\n"
            "  1. Ruwan sama yana sauka. (The rain is falling.)\n"
            "  2. Damina ta yi, gona ta yi kore. (The rainy season came, the farm turned green.)\n"
            "  3. Rani ya yi zafi sosai. (The dry season is very hot.)\n"
            "  4. Iska mai sanyi tana kadawa. (A cool wind is blowing.)\n"
            "  5. Hadari ya yi duhu. (The storm cloud darkened.)\n"
            "  6. Rana tana haskakawa. (The sun is shining.)\n"
            "  7. Wata ya fito da daddare. (The moon came out at night.)\n"
            "  8. Taurari suna kyalkyali a sama. (The stars are twinkling in the sky.)\n"
            "  9. Zaki yana cikin daji. (The lion is in the bush.)\n"
            "  10. Giwa tana shan ruwa a kogi. (The elephant is drinking water at the river.)\n"
            "  11. Rakumi yana tafiya a hamada. (The camel is walking in the desert.)\n"
            "  12. Tsuntsaye suna tashi da sassafe. (The birds rise early in the morning.)\n"
            "  13. Kifi yana cikin kogi. (The fish are in the river.)\n"
            "  14. Maciji ya shiga cikin ciyawa. (The snake entered the grass.)\n"
            "  15. Baobab itace mai girma ne. (The baobab is a huge tree.)\n"
            "  16. Furen itace suna da kyau. (The tree's flowers are beautiful.)\n"
            "  17. Gona tana bukatar ruwa. (The farm needs water.)\n"
            "  18. Manoma suna shuka da farkon damina. (Farmers plant at the start of the rains.)\n"
            "  19. Yau yanayi yayi kyau. (The weather is nice today.)\n"
            "  20. Gobe za a yi ruwan sama, in Allah ya so. (It will rain tomorrow, God willing.)"
        ),
        "how_it_works": (
            "Learn the two seasons as the frame of everything: damina "
            "(rainy season) and rani (dry/hot season), with harmattan's "
            "dusty cool winds inside rani. Hang weather verbs on the frame: "
            "ruwan sama yana sauka (rain falls), iska tana kadawa (wind "
            "blows), rana tana haskakawa (sun shines). Then stock the "
            "landscape: daji (bush), kogi (river), hamada (desert), itace "
            "(tree), ciyawa (grass) - and the animals that belong to each. "
            "Weather talk opens conversations everywhere; master yau yanayi "
            "yayi kyau and its answers."
        ),
        "key_points": [
            "20 sentences: animals, plants, seasons, weather talk.",
            "Two seasons: damina (rainy), rani (dry); harmattan winds in rani.",
            "Weather verbs: sauka (fall), kadawa (blow), haskakawa (shine).",
            "Landscape: daji, kogi, hamada, itace, ciyawa, gona.",
            "God-willing future: in Allah ya so.",
        ],
        "requirements": [
            "Describe today's weather and the season in five sentences.",
            "Name ten animals and five plants in Hausa.",
        ],
        "standards": [
            "Nature vocabulary follows Abraham 1962; sentences in standard Kano grammar.",
        ],
        "citations": [CIT_ABRAHAM, CIT_NEWMAN],
        "must_contain": ["Ruwan sama yana sauka", "Damina ta yi, gona ta yi kore", "Zaki yana cikin daji", "in Allah ya so"],
        "sig_lens": (
            "Through the Signature lens the nature sentences are the sworn "
            "survey of the land: each season dated, each animal placed in "
            "its country, each rain witnessed as it falls - the earth "
            "itself entered into the archive as evidence."
        ),
        "drill": {
            "seasons": ["damina", "rani"],
            "weather_verbs": ["sauka", "kadawa", "haskakawa"],
            "animals": ["zaki", "giwa", "rakumi", "tsuntsu", "kifi", "maciji", "kare", "kura"],
            "sentences": 20,
        },
    }
)
ENTRIES.append(
    {
        "key": "shopping",
        "name": "Hausa Shopping and Money Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the market, prices, bargaining, and "
            "paying - the commercial Hausa of Kasuwar Kano and every "
            "roadside stall. \n\n"
            "  1. Nawa ne farashin wannan? (How much is the price of this?)\n"
            "  2. Yayi tsada sosai. (It is too expensive.)\n"
            "  3. Ka rage mini kadan. (Reduce it for me a little.)\n"
            "  4. Naira dari biyu, kudin karshe? (Two hundred naira, last price?)\n"
            "  5. Ban da kudi isasshe. (I do not have enough money.)\n"
            "  6. Ina so in saya tufafi. (I want to buy clothes.)\n"
            "  7. Akwai wani mai rahusa? (Is there a cheaper one?)\n"
            "  8. Wannan sabo ne? (Is this new?)\n"
            "  9. Ina bukatar girma mai girma. (I need a large size.)\n"
            "  10. Zan gwada wannan. (I will try this on.)\n"
            "  11. Mai sayarwa ya yi mini rangwame. (The seller gave me a discount.)\n"
            "  12. Mun yi ciniki mai kyau. (We made a good bargain.)\n"
            "  13. Biya da kudi tsabar. (Pay in cash.)\n"
            "  14. Akwai canji? (Is there change?)\n"
            "  15. Ga canjin naira hamsin. (Here is fifty naira change.)\n"
            "  16. Kasuwa tana cike da mutane yau. (The market is crowded today.)\n"
            "  17. Shagunan sun bude da sassafe. (The shops opened early morning.)\n"
            "  18. Na saya kayan miya da kayan lambu. (I bought soup ingredients and vegetables.)\n"
            "  19. Wannan kaya na asali ne. (This product is genuine.)\n"
            "  20. Mun gode, sai mun dawo. (Thank you, we will return.)"
        ),
        "how_it_works": (
            "Bargaining is a dialogue with a fixed shape: ask the price "
            "(nawa ne farashin wannan?), react (yayi tsada sosai), counter "
            "(ka rage mini kadan), name your price (naira dari biyu, kudin "
            "karshe?), and close (mun yi ciniki mai kyau). Practice both "
            "sides - buyer and seller - switching roles each round. Money "
            "words: kudi (money), farashi (price), rangwame (discount), "
            "canji (change), ciniki (bargain/trade). Count money aloud in "
            "Hausa while you practice; the numbers record is the cash "
            "register."
        ),
        "key_points": [
            "20 sentences: market, prices, bargaining, paying.",
            "Bargaining shape: ask, react, counter, name price, close.",
            "Money words: kudi, farashi, rangwame, canji, ciniki.",
            "Cash phrases: biya da kudi tsabar; akwai canji?",
            "Closing courtesy: mun gode, sai mun dawo.",
        ],
        "requirements": [
            "Bargain a price down in a buyer/seller role-play.",
            "Handle paying, change, and closing in Hausa.",
        ],
        "standards": [
            "Market vocabulary follows standard Hausa commercial usage.",
        ],
        "citations": [CIT_ABRAHAM, CIT_NEWMAN],
        "must_contain": ["Nawa ne farashin wannan", "Ka rage mini kadan", "Mun yi ciniki mai kyau", "Akwai canji"],
        "sig_lens": (
            "Through the Signature lens the market sentences are the sworn "
            "articles of trade: each price named aloud, each bargain "
            "witnessed, each coin sealed in the telling - for honest trade "
            "is a covenant, and the archive keeps its books."
        ),
        "drill": {
            "money_words": ["kudi", "farashi", "rangwame", "canji", "ciniki"],
            "bargain_steps": ["ask", "react", "counter", "name price", "close"],
            "sentences": 20,
        },
    }
)
ENTRIES.append(
    {
        "key": "friendship",
        "name": "Hausa Friendship and Social Life Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for meeting people, invitations, and "
            "celebrations - the social Hausa of weddings, naming "
            "ceremonies, and long evening conversations. \n\n"
            "  1. Wannan abokina ne, sunansa Musa. (This is my friend, his name is Musa.)\n"
            "  2. Mun hadu a makaranta shekaru biyar da suka wuce. (We met at school five years ago.)\n"
            "  3. Ina gayyatar ka zuwa bikin aure na. (I am inviting you to my wedding.)\n"
            "  4. Bikin suna zai kasance gobe. (The naming ceremony will be tomorrow.)\n"
            "  5. Muna taya ka murna. (We congratulate you - to a man.)\n"
            "  6. Allah ya albarkaci aurenku. (May God bless your marriage.)\n"
            "  7. Zo mu ci abinci tare. (Come, let us eat together.)\n"
            "  8. Ina son in ziyarce ka. (I want to visit you - to a man.)\n"
            "  9. Gidanka a bude yake kullum. (Your house is always open - to a man.)\n"
            "  10. Mun yi hira mai dadi da daddare. (We had a pleasant chat at night.)\n"
            "  11. Abokai na gaskiya suna taimakon juna. (True friends help one another.)\n"
            "  12. Na amince da shawararka. (I agree with your advice.)\n"
            "  13. Kada mu yi fada, mu yi sulhu. (Let us not quarrel, let us make peace.)\n"
            "  14. Na yafe maka. (I forgive you - to a man.)\n"
            "  15. Taya murna akan sabon aiki! (Congratulations on the new job!)\n"
            "  16. Muna tare a cikin farin ciki da bakin ciki. (We are together in joy and sorrow.)\n"
            "  17. Zumunci yana da daraja. (Kinship/friendship has value.)\n"
            "  18. Ka zo da iyalinka. (Come with your family - to a man.)\n"
            "  19. Mun raba abinci da makwabta. (We shared food with the neighbors.)\n"
            "  20. Abota ta gaskiya ba ta sayuwa. (True friendship cannot be bought.)"
        ),
        "how_it_works": (
            "Social Hausa runs on invitation and blessing: practice "
            "inviting (ina gayyatar ka zuwa...), congratulating (muna taya "
            "ka murna), blessing (Allah ya albarkaci...), and reconciling "
            "(kada mu yi fada, mu yi sulhu). The key social nouns - aboki "
            "(friend), zumunci (kinship/bond), hira (chat), shawara "
            "(advice), sulhu (peace) - anchor every gathering. Learn the "
            "celebration calendar too: bikin aure (wedding), bikin suna "
            "(naming ceremony), salla (festival)."
        ),
        "key_points": [
            "20 sentences: meeting people, invitations, celebrations.",
            "Social verbs: gayyata (invite), taya murna (congratulate), ziyara (visit), yafe (forgive).",
            "Celebrations: bikin aure, bikin suna, salla.",
            "Blessings: Allah ya albarkaci aurenku.",
            "Values: zumunci, abota ta gaskiya.",
        ],
        "requirements": [
            "Invite, congratulate, and bless in three social scenarios.",
            "Narrate how you met a friend, in Hausa.",
        ],
        "standards": [
            "Social vocabulary follows standard Hausa usage in the reference dictionaries.",
        ],
        "citations": [CIT_ABRAHAM, CIT_NEWMAN],
        "must_contain": ["Ina gayyatar ka zuwa bikin aure na", "Muna taya ka murna", "Abota ta gaskiya ba ta sayuwa", "Kada mu yi fada, mu yi sulhu"],
        "sig_lens": (
            "Through the Signature lens the friendship sentences are the "
            "sworn bonds of company: each invitation a sealed summons, each "
            "blessing a vow spoken over another, each reconciliation a "
            "covenant re-signed - for friendship in the archive is not felt "
            "only, it is recorded."
        ),
        "drill": {
            "social_verbs": ["gayyata", "taya murna", "ziyara", "yafe", "sulhu"],
            "celebrations": ["bikin aure", "bikin suna", "salla"],
            "sentences": 20,
        },
    }
)
ENTRIES.append(
    {
        "key": "technology",
        "name": "Hausa Technology and Communication Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the phone, the internet, the computer, "
            "and messaging - modern Hausa, where waya (wire/phone) meets "
            "the smartphone. \n\n"
            "  1. Wayata ta yi kuka. (My phone rang - lit. cried.)\n"
            "  2. Ina magana da abokina a waya. (I am talking with my friend on the phone.)\n"
            "  3. Ka kira ni gobe da safe. (Call me tomorrow morning - to a man.)\n"
            "  4. Baturi ya kare. (The battery is dead.)\n"
            "  5. Ina caji wayata. (I am charging my phone.)\n"
            "  6. Na turo maka sako. (I sent you a message - to a man.)\n"
            "  7. Ka karanta sakona? (Did you read my message? - to a man.)\n"
            "  8. Intanet yana da sauri yau. (The internet is fast today.)\n"
            "  9. Shafin yana lodi a hankali. (The page is loading slowly.)\n"
            "  10. Na manta kalmar sirri. (I forgot the password.)\n"
            "  11. Kwamfutata tana aiki da kyau. (My computer is working well.)\n"
            "  12. Na ajiye fayil din a tebur. (I saved the file on the desktop.)\n"
            "  13. Buga maɓallin nan. (Press that button.)\n"
            "  14. Hoton ya fito fili. (The photo came out clear.)\n"
            "  15. Na dauki hoto da wayata. (I took a photo with my phone.)\n"
            "  16. Bidiyon yana daukar lokaci. (The video is taking time.)\n"
            "  17. Muna ganawa a bidiyo. (We are meeting on video.)\n"
            "  18. Rediyo yana watsa labarai. (The radio is broadcasting news.)\n"
            "  19. Talabijin ya lalace. (The television is broken.)\n"
            "  20. Fasaha tana canja rayuwarmu. (Technology is changing our lives.)"
        ),
        "how_it_works": (
            "Modern Hausa borrows and adapts: intanet, kwamfuta, fayil, "
            "bidiyo, menu - said with Hausa tones and grammar - beside home "
            "words like waya (phone), sako (message), kalmar sirri "
            "(password), maɓalli (button/key). Practice the device "
            "troubleshoot script: baturi ya kare (battery dead), ina caji "
            "(charging), shafin yana lodi a hankali (slow loading), na "
            "manta kalmar sirri (forgot password). Then run a full call in "
            "Hausa: greeting, wayata ta yi kuka, ka kira ni gobe, sai an "
            "jima."
        ),
        "key_points": [
            "20 sentences: phone, internet, computer, messaging.",
            "Core tech words: waya, sako, intanet, kwamfuta, fayil, kalmar sirri, maɓalli.",
            "Troubleshoot script: battery, charging, loading, password.",
            "Borrowed words take Hausa grammar and tones.",
        ],
        "requirements": [
            "Make a phone call and send a message entirely in Hausa.",
            "Troubleshoot a device problem in five sentences.",
        ],
        "standards": [
            "Modern vocabulary follows current standard Hausa media usage.",
        ],
        "citations": [CIT_NEWMAN, CIT_ABRAHAM],
        "must_contain": ["Wayata ta yi kuka", "Na turo maka sako", "Na manta kalmar sirri", "Fasaha tana canja rayuwarmu"],
        "sig_lens": (
            "Through the Signature lens the technology sentences are the "
            "sworn wires of the modern age: each call a voice sealed "
            "across distance, each message a letter that cannot be lost, "
            "each password a private seal - the old covenant carried on new "
            "wires."
        ),
        "drill": {
            "tech_words": ["waya", "sako", "intanet", "kwamfuta", "fayil", "kalmar sirri", "maɓalli", "baturi"],
            "sentences": 20,
        },
    }
)

ENTRIES.append(
    {
        "key": "tenses",
        "name": "Hausa Verb Tenses in Sentences",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "The Hausa tense-aspect-mood (TAM) system in sentences: "
            "completed, ongoing, future, habitual, and subjunctive - five "
            "or more translated sentences per form, all built on the verb "
            "ci (eat) and je (go) so the markers stand out clearly. \n\n"
            "Completed (perfective) - na, ka/kin, ya/ta, mun, kun, sun:\n"
            "  Na ci abinci. (I ate food.)\n"
            "  Ka je kasuwa. (You went to the market - to a man.)\n"
            "  Kin dafa tuwo. (You cooked tuwo - to a woman.)\n"
            "  Ya saya mota. (He bought a car.)\n"
            "  Ta karanta littafi. (She read a book.)\n"
            "  Mun gama aiki. (We finished work.)\n\n"
            "Ongoing (continuous/imperfective) - ina, kana/kina, yana/tana, muna, kuna, suna:\n"
            "  Ina cin abinci. (I am eating food.)\n"
            "  Kana tafiya kasuwa. (You are going to the market - to a man.)\n"
            "  Kina dafa tuwo. (You are cooking tuwo - to a woman.)\n"
            "  Yana sayar da kayan marmari. (He is selling fruit.)\n"
            "  Tana karanta littafi. (She is reading a book.)\n"
            "  Suna aiki a gona. (They are working on the farm.)\n\n"
            "Future - zan, zaka/zaki, zai/zata, zamu, zaku, zasu:\n"
            "  Zan ci abinci. (I will eat food.)\n"
            "  Zaka je Kano. (You will go to Kano - to a man.)\n"
            "  Zaki dafa tuwo. (You will cook tuwo - to a woman.)\n"
            "  Zai saya mota. (He will buy a car.)\n"
            "  Zata karanta littafi. (She will read a book.)\n"
            "  Zasu zo gobe. (They will come tomorrow.)\n\n"
            "Habitual - na kan, kana kan, yana kan (usually, used to):\n"
            "  Na kan ci tuwo da dare. (I usually eat tuwo at night.)\n"
            "  Kana kan je kasuwa kullum. (You usually go to the market daily - to a man.)\n"
            "  Yana kan tashi da sassafe. (He usually wakes early morning.)\n"
            "  Tana kan karanta da daddare. (She usually reads at night.)\n"
            "  Suna kan aiki tare. (They usually work together.)\n\n"
            "Subjunctive (wishes, purpose, commands softened) - in, ka, ya, mu:\n"
            "  Ina so in ci abinci. (I want to eat food.)\n"
            "  Zo ka ci abinci. (Come and eat food - to a man.)\n"
            "  Allah ya ba ka lafiya. (May God grant you health - to a man.)\n"
            "  Mu je kasuwa. (Let us go to the market.)\n"
            "  Ki zauna lafiya. (Stay well - to a woman.)\n\n"
            "The pattern to carry: the verb stem barely changes (ci/cin, "
            "je/tafiya); the marker before it does all the time-work. "
            "Negative forms wrap in ba ... ba: ban ci ba (I did not eat), "
            "ba na cin abinci (I am not eating), ba zan ci ba (I will not eat)."
        ),
        "how_it_works": (
            "Take one verb - ci - and run the full marker table aloud: na "
            "ci, ina cin, zan ci, na kan ci, in ci; then ka ci, kana cin, "
            "zaka ci; then ya ci, yana cin, zai ci. Do the same for je, "
            "tafiya's verb: na je, ina tafiya, zan je. Then narrate a day "
            "in three times: jiya na... (yesterday I did), yanzu ina... "
            "(now I am doing), gobe zan... (tomorrow I will do). The "
            "subjunctive is the politeness engine - practice ina so in..., "
            "mu je..., Allah ya... until wishes and purposes flow."
        ),
        "key_points": [
            "Five TAM forms: completed, ongoing, future, habitual, subjunctive - 5+ sentences each.",
            "Completed: na, ka/kin, ya/ta, mun, kun, sun.",
            "Ongoing: ina, kana/kina, yana/tana, muna, kuna, suna (+ verbal noun).",
            "Future: zan, zaka/zaki, zai/zata, zamu, zaku, zasu.",
            "Habitual: na kan (usually); subjunctive: in, ka, ya, mu (wishes/purpose).",
            "Negatives: ban ci ba; ba na cin abinci; ba zan ci ba.",
        ],
        "requirements": [
            "Conjugate ci and je through all five forms for all persons.",
            "Narrate yesterday, today, and tomorrow in Hausa.",
        ],
        "standards": [
            "TAM analysis follows Newman 2000 and Jaggar 2001.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR],
        "must_contain": ["Na ci abinci", "Ina cin abinci", "Zan ci abinci", "Na kan ci tuwo da dare", "Ina so in ci abinci"],
        "sig_lens": (
            "Through the Signature lens the tenses are the sworn times of "
            "the verb: na the seal of the finished deed, ina the seal of "
            "the deed in hand, zan the seal of the vowed deed, na kan the "
            "seal of the deed done faithfully again and again, in the seal "
            "of the deed wished and willed."
        ),
        "drill": {
            "paradigm": {
                "perfect": ["na", "ka", "kin", "ya", "ta", "mun", "kun", "sun"],
                "continuous": ["ina", "kana", "kina", "yana", "tana", "muna", "kuna", "suna"],
                "future": ["zan", "zaka", "zaki", "zai", "zata", "zamu", "zaku", "zasu"],
            },
            "sentences_per_form": 5,
            "total_sentences": 28,
            "negatives": ["ban ci ba", "ba na cin abinci", "ba zan ci ba"],
        },
    }
)
ENTRIES.append(
    {
        "key": "qa",
        "name": "Hausa Questions and Answers",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty question-and-answer pairs covering who, what, where, "
            "when, why, and how - the interrogative engine of daily Hausa. \n\n"
            "  1. Wa ya zo? - Abokina ya zo. (Who came? - My friend came.)\n"
            "  2. Me kake so? - Ina son ruwa. (What do you want? - I want water.)\n"
            "  3. Ina makaranta? - Tana kusa da kasuwa. (Where is the school? - It is near the market.)\n"
            "  4. Yaushe za ka tafi? - Zan tafi gobe da safe. (When will you go? - I will go tomorrow morning.)\n"
            "  5. Me ya sa ka yi kuka? - Na ji labari mara dadi. (Why did you cry? - I heard unpleasant news.)\n"
            "  6. Ta yaya kake? - Lafiya lau. (How are you? - I am fine.)\n"
            "  7. Nawa ne farashin? - Naira dari biyu ne. (How much is the price? - It is two hundred naira.)\n"
            "  8. Wane launi kake so? - Ina son kore. (Which color do you like? - I like green.)\n"
            "  9. Shin kana jin Hausa? - I, ina ji kadan. (Do you understand Hausa? - Yes, I understand a little.)\n"
            "  10. Yara nawa ne? - Yara uku ne. (How many children? - Three children.)\n"
            "  11. Me ya faru? - Mota ta lalace. (What happened? - The car broke down.)\n"
            "  12. Ina kake aiki? - Ina aiki a asibiti. (Where do you work? - I work at the hospital.)\n"
            "  13. Wane lokaci za mu hadu? - Karfe hudu na yamma. (What time shall we meet? - Four in the afternoon.)\n"
            "  14. Don me kake kuka? - Saboda ciwo. (Why are you crying? - Because of pain.)\n"
            "  15. Kana da waya? - I, ina da ita. (Do you have a phone? - Yes, I have it.)\n"
            "  16. Ta ina hanya zuwa gari? - Ta can, ta dama. (Which way to town? - That way, to the right.)\n"
            "  17. Me sunanka? - Sunana Aisha. (What is your name? - My name is Aisha.)\n"
            "  18. Yaushe aka haife ka? - An haife ni a Janairu. (When were you born? - I was born in January.)\n"
            "  19. Me kake ci? - Ina cin tuwo. (What are you eating? - I am eating tuwo.)\n"
            "  20. Shin lafiya? - Lafiya kalau. (Is all well? - Very well.)"
        ),
        "how_it_works": (
            "Each pair is a complete exchange: ask the question with "
            "rising intonation, answer in a full sentence, never a single "
            "word. Drill the question words until each one triggers its "
            "answer type automatically - wa wants a person, ina wants a "
            "place, yaushe wants a time, me ya sa wants a reason, nawa "
            "wants a number. Then take any sentence from any earlier record "
            "and interrogate it: turn Na je kasuwa into Ina ka je? and "
            "Yaushe ka je kasuwa?"
        ),
        "key_points": [
            "20 Q&A pairs: who, what, where, when, why, how, how much, how many.",
            "Question words: wa, me/mene, ina, yaushe, me ya sa, ta yaya, nawa, wane.",
            "Yes/no questions: rising intonation or shin.",
            "Answers are full sentences, building fluency.",
        ],
        "requirements": [
            "Ask and answer all 20 pairs from memory.",
            "Convert ten statements into questions.",
        ],
        "standards": [
            "Interrogative forms follow Newman 2000 and Jaggar 2001.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR],
        "must_contain": ["Wa ya zo", "Me kake so", "Yaushe za ka tafi", "Shin kana jin Hausa", "Ta ina hanya zuwa gari"],
        "sig_lens": (
            "Through the Signature lens each question is a sworn inquiry "
            "and each answer a sworn testimony: wa calls the witness, ina "
            "fixes the place, yaushe stamps the time, me ya sa demands the "
            "cause - the whole truth taken down in pairs."
        ),
        "drill": {
            "pairs": 20,
            "question_words": ["wa", "me", "ina", "yaushe", "me ya sa", "ta yaya", "nawa", "wane", "shin"],
        },
    }
)
ENTRIES.append(
    {
        "key": "commands",
        "name": "Hausa Commands and Requests",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty imperative and polite-request sentences, formal and "
            "informal: how Hausa tells, asks, urges, and softens. The bare "
            "verb stem commands (zo! come!), don Allah softens (don Allah, "
            "zo - please come), and the subjunctive makes wishes (Allah ya "
            "ba ka lafiya). \n\n"
            "Direct commands (informal, to one person):\n"
            "  1. Zo nan! (Come here!)\n"
            "  2. Tafi gida! (Go home!)\n"
            "  3. Zauna! (Sit down!)\n"
            "  4. Ci abinci! (Eat!)\n"
            "  5. Sha ruwa! (Drink water!)\n"
            "  6. Bude kofa! (Open the door!)\n"
            "  7. Rufe taga! (Close the window!)\n"
            "  8. Kawo mini littafi! (Bring me the book!)\n"
            "  9. Karanta! (Read!)\n"
            "  10. Rubuta sunanka! (Write your name!)\n\n"
            "Polite requests (don Allah, subjunctive softening):\n"
            "  11. Don Allah, zo nan. (Please, come here.)\n"
            "  12. Za ka iya taimaka mini? (Can you help me? - to a man.)\n"
            "  13. Don Allah, bude kofa. (Please open the door.)\n"
            "  14. Ki zauna, don Allah. (Please sit down - to a woman.)\n"
            "  15. Kawo mini ruwa, don Allah. (Bring me water, please.)\n\n"
            "Formal and plural (ku - to groups and elders):\n"
            "  16. Ku zo nan. (Come here - to a group.)\n"
            "  17. Ku zauna lafiya. (Sit well / be seated - to a group.)\n"
            "  18. Don Allah, ku yi hakuri. (Please be patient - to a group.)\n\n"
            "Prohibitions (kada - do not):\n"
            "  19. Kada ka tafi! (Do not go! - to a man.)\n"
            "  20. Kada ku yi hayaniya! (Do not make noise! - to a group.)\n\n"
            "Note the politeness ladder: bare stem (orders), don Allah "
            "(requests), za ka iya...? (asking ability), ku forms (respect "
            "to groups and elders), kada (prohibition). To an elder, Hausa "
            "prefers the request forms; the bare command is for children, "
            "close friends, and urgency."
        ),
        "how_it_works": (
            "Practice commands as actions: say bude kofa while opening a "
            "door, rufe taga while closing a window, zauna while sitting - "
            "the body remembers what the mouth says. Then climb the "
            "politeness ladder with one verb: zo nan! / don Allah, zo nan / "
            "za ka iya zuwa nan? / ku zo nan. Drill the kada prohibitions "
            "separately - kada ka tafi, kada ki yi kuka, kada ku yi "
            "hayaniya - until the negative command is as fast as the "
            "positive."
        ),
        "key_points": [
            "20 imperatives and requests: direct, polite, formal, prohibitions.",
            "Bare stem commands: zo, tafi, zauna, bude, rufe.",
            "Politeness: don Allah; za ka iya...?; ku forms for groups/elders.",
            "Prohibition: kada + subjunctive (kada ka tafi).",
            "Register rule: bare commands for urgency/intimates; requests for elders.",
        ],
        "requirements": [
            "Give ten commands as physical actions.",
            "Make the same request at four politeness levels.",
        ],
        "standards": [
            "Imperative and subjunctive forms follow Newman 2000 and Jaggar 2001.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR],
        "must_contain": ["Zo nan", "Don Allah, zo nan", "Ku zo nan", "Kada ka tafi", "Kawo mini littafi"],
        "sig_lens": (
            "Through the Signature lens commands are sworn directives: the "
            "bare stem a direct order sealed and delivered, don Allah a "
            "request sealed with reverence, kada a prohibition sealed shut - "
            "each one binding on the hearer as a signed instruction."
        ),
        "drill": {
            "direct": ["zo", "tafi", "zauna", "ci", "sha", "bude", "rufe", "kawo", "karanta", "rubuta"],
            "polite_markers": ["don Allah", "za ka iya"],
            "formal": ["ku"],
            "prohibition": ["kada"],
            "sentences": 20,
        },
    }
)
ENTRIES.append(
    {
        "key": "descriptions",
        "name": "Hausa Descriptions of People and Places",
        "group": "Grammar in Action",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences describing people, places, and things in "
            "detail: the descriptive power of Hausa, where one long "
            "sentence can paint a whole portrait. \n\n"
            "  1. Malamina mutum ne mai dogon jiki da farin hakora. (My teacher is a tall person with white teeth.)\n"
            "  2. Yarinyar tana da doguwar gashi da kyawawan idanu. (The girl has long hair and beautiful eyes.)\n"
            "  3. Tsohon yana da fararen gemu da murya mai zurfi. (The old man has a white beard and a deep voice.)\n"
            "  4. Garinmu gari ne mai cike da itatuwa da kasuwanni. (Our town is a town full of trees and markets.)\n"
            "  5. Kano birni ne mai tarihi da yawan jama'a. (Kano is a historic, populous city.)\n"
            "  6. Kogin yana gudana a hankali tsakanin duwatsu. (The river flows slowly between the rocks.)\n"
            "  7. Dajin yana da duhu da surutun tsuntsaye. (The bush is dark with the chatter of birds.)\n"
            "  8. Gidan sarki yana da manyan kofofi da fadin farfajiya. (The king's palace has grand doors and a wide courtyard.)\n"
            "  9. Tufafinta jajaye ne da zinariya a gefe. (Her clothes are red with gold at the edges.)\n"
            "  10. Mota bakar mota ce mai sauri da dadi. (The car is a black car, fast and comfortable.)\n"
            "  11. Abincin yana da dadi da kamshi mai dadi. (The food is tasty with a pleasant aroma.)\n"
            "  12. Daren yana da sanyi da shiru mai zurfi. (The night is cold with a deep silence.)\n"
            "  13. Safiyar tana da haske da iska mai dadi. (The morning is bright with a pleasant breeze.)\n"
            "  14. Yaron mai hankali ne, mai aiki tukuru. (The boy is intelligent, a hard worker.)\n"
            "  15. Macen mai kirki ce, mai tausayi da hakuri. (The woman is kind, compassionate and patient.)\n"
            "  16. Littafin yana da shafuka masu yawa da hotuna masu kyau. (The book has many pages with beautiful pictures.)\n"
            "  17. Kasuwar tana da hayaniya da launuka masu yawa. (The market is noisy with many colors.)\n"
            "  18. Gonar tana da kore da 'ya'yan itatuwa. (The farm is green with tree fruits.)\n"
            "  19. Hanya mai nisa ce amma mai kyau. (The road is long but good.)\n"
            "  20. Wannan wuri ne mai dadi da natsuwa. (This is a pleasant, peaceful place.)"
        ),
        "how_it_works": (
            "Hausa description stacks with mai (one who has / characterized "
            "by): mutum mai dogon jiki (a tall-bodied person), mace mai "
            "kirki (a kind woman), wuri mai dadi (a pleasant place). Build "
            "portraits by chaining mai-phrases and relative clauses: start "
            "with the noun, add one quality, then another, then a clause "
            "(da ...). Practice on real subjects: describe a family "
            "member, your street, the market - three mai-phrases minimum "
            "per portrait."
        ),
        "key_points": [
            "20 detailed descriptive sentences.",
            "The mai construction: mutum mai kirki (a kind person).",
            "Adjective stacking after the noun with agreement.",
            "Relative clauses extend descriptions: da ..., mai ....",
            "Portraits built by chaining: noun + quality + quality + clause.",
        ],
        "requirements": [
            "Describe a person, a place, and a thing in five sentences each.",
            "Use three mai-phrases per portrait.",
        ],
        "standards": [
            "Descriptive constructions follow Newman 2000 and Jaggar 2001.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR, CIT_ABRAHAM],
        "must_contain": ["mutum ne mai dogon jiki", "Garinmu gari ne mai cike da itatuwa", "mai kirki", "Wannan wuri ne mai dadi da natsuwa"],
        "sig_lens": (
            "Through the Signature lens descriptions are sworn portraits: "
            "each mai-phrase a seal of quality pressed beside the noun, "
            "each stacked clause another witness called - until the person "
            "or place stands in the archive fully seen, fully attested."
        ),
        "drill": {
            "mai_phrases": ["mai dogon jiki", "mai kirki", "mai dadi", "mai kyau", "mai hankali", "mai tausayi"],
            "sentences": 20,
        },
    }
)

ENTRIES.append(
    {
        "key": "story1",
        "name": "Hausa Short Story I: A Simple Day",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence simple story in Hausa with line-by-line English "
            "translation: a day in the life of a Kano schoolboy, in the "
            "present and habitual tenses. \n\n"
            "  1. Sunana Ibrahim, ina zaune a Kano. (My name is Ibrahim, I live in Kano.)\n"
            "  2. Ina tashi da sassafe kullum. (I wake up early every day.)\n"
            "  3. Ina wanka, sannan ina cin abincin safe. (I bathe, then I eat breakfast.)\n"
            "  4. Ina tafiya makaranta da kafafu. (I go to school on foot.)\n"
            "  5. Abokaina suna jirana a hanya. (My friends wait for me on the road.)\n"
            "  6. Muna karatu tare da malam. (We study with the teacher.)\n"
            "  7. Da rana muna cin abincin rana a gida. (At midday we eat lunch at home.)\n"
            "  8. Da yamma ina wasa kwallo da abokaina. (In the afternoon I play football with my friends.)\n"
            "  9. Da dare muna cin abincin dare tare da iyayena. (At night we eat dinner with my parents.)\n"
            "  10. Sannan ina kwana lafiya. (Then I sleep well.)\n\n"
            "The story skeleton: time words open each scene (da sassafe, "
            "da rana, da yamma, da dare), the continuous markers (ina, "
            "muna, suna) carry the ongoing day, and sannan (then) chains "
            "the events. Retell it changing one detail - the city, the "
            "game, the meal - and the skeleton holds."
        ),
        "how_it_works": (
            "Read the story aloud twice: first for the chain-words (da "
            "sassafe, sannan, da rana, da yamma, da dare), then for the "
            "verbs. Cover the English and translate each line back from the "
            "Hausa; cover the Hausa and rebuild each line from the "
            "English. Then retell the whole day from memory, and finally "
            "write your own ten-sentence day using the same molds: name, "
            "waking, washing, school or work, midday, afternoon, night, sleep."
        ),
        "key_points": [
            "10-sentence story with line-by-line English translation.",
            "Time words anchor scenes: da sassafe, da rana, da yamma, da dare.",
            "Continuous markers carry the day: ina, muna, suna.",
            "Chain word sannan links events.",
            "Retellable skeleton: change details, keep the molds.",
        ],
        "requirements": [
            "Retell the story from memory in Hausa.",
            "Write your own 10-sentence day on the same skeleton.",
        ],
        "standards": [
            "Story grammar follows standard Kano usage; translations are complete and literal where the grammar is new.",
        ],
        "citations": [CIT_NEWMAN],
        "must_contain": ["Sunana Ibrahim, ina zaune a Kano", "Ina tashi da sassafe kullum", "Sannan ina kwana lafiya"],
        "sig_lens": (
            "Through the Signature lens this simple day is the sworn "
            "journal of one life: each hour witnessed, each meal recorded, "
            "each companion named - the ordinary day sealed as evidence "
            "that the language lives in real mornings."
        ),
        "drill": {
            "lines": [
                ("Sunana Ibrahim, ina zaune a Kano.", "My name is Ibrahim, I live in Kano."),
                ("Ina tashi da sassafe kullum.", "I wake up early every day."),
                ("Ina wanka, sannan ina cin abincin safe.", "I bathe, then I eat breakfast."),
                ("Ina tafiya makaranta da kafafu.", "I go to school on foot."),
                ("Abokaina suna jirana a hanya.", "My friends wait for me on the road."),
                ("Muna karatu tare da malam.", "We study with the teacher."),
                ("Da rana muna cin abincin rana a gida.", "At midday we eat lunch at home."),
                ("Da yamma ina wasa kwallo da abokaina.", "In the afternoon I play football with my friends."),
                ("Da dare muna cin abincin dare tare da iyayena.", "At night we eat dinner with my parents."),
                ("Sannan ina kwana lafiya.", "Then I sleep well."),
            ],
            "time_words": ["da sassafe", "da rana", "da yamma", "da dare"],
        },
    }
)
ENTRIES.append(
    {
        "key": "story2",
        "name": "Hausa Short Story II: A Journey in the Past",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the past tense: a market journey to "
            "Zaria, told with the completed markers na, ya, mun, sun. \n\n"
            "  1. Jiya na tafi Zaria da abokina. (Yesterday I went to Zaria with my friend.)\n"
            "  2. Mun tashi da sassafe. (We set out early morning.)\n"
            "  3. Mota ta cika da fasinjoji. (The vehicle filled with passengers.)\n"
            "  4. Hanya ta yi kyau, mun iso da wuri. (The road was good, we arrived early.)\n"
            "  5. Kasuwar Zaria ta cika da mutane. (The Zaria market was full of people.)\n"
            "  6. Na saya tufafi da takalma. (I bought clothes and shoes.)\n"
            "  7. Abokina ya saya kayan marmari. (My friend bought fruit.)\n"
            "  8. Mun ci abinci a gidan abinci. (We ate food at the restaurant.)\n"
            "  9. Da yamma mun koma Kano. (In the afternoon we returned to Kano.)\n"
            "  10. Mun iso gida lafiya da dare. (We reached home safely at night.)\n\n"
            "The past-tense skeleton: jiya and da yamma stamp the time, the "
            "completed markers (na, mun, ta, ya) stamp each finished deed, "
            "and the journey runs departure-road-market-meal-return. Every "
            "verb here is done and sealed; nothing is ongoing."
        ),
        "how_it_works": (
            "Contrast this story with Story I line by line: ina tafiya "
            "(I am going) against na tafi (I went), muna ci (we are eating) "
            "against mun ci (we ate). The marker is the only thing that "
            "moves the story through time. Retell the journey in the "
            "present (yau ina tafiya Zaria...) and in the future (gobe zan "
            "tafi Zaria...), then narrate a real trip of your own in the "
            "past tense."
        ),
        "key_points": [
            "10-sentence past-tense story with line-by-line translation.",
            "Completed markers: na, mun, ta, ya, sun.",
            "Journey skeleton: departure, road, market, meal, return.",
            "Contrast drills against Story I teach the tense shift.",
        ],
        "requirements": [
            "Retell the journey in present, past, and future tenses.",
            "Narrate a real past trip in ten Hausa sentences.",
        ],
        "standards": [
            "Past-tense narrative follows standard Kano usage.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR],
        "must_contain": ["Jiya na tafi Zaria da abokina", "Mun iso gida lafiya da dare", "Kasuwar Zaria ta cika da mutane"],
        "sig_lens": (
            "Through the Signature lens this journey is the sworn travel "
            "log: each departure stamped, each arrival witnessed, each "
            "purchase sealed - the past tense a locked ledger where what "
            "is done is done and recorded."
        ),
        "drill": {
            "lines": [
                ("Jiya na tafi Zaria da abokina.", "Yesterday I went to Zaria with my friend."),
                ("Mun tashi da sassafe.", "We set out early morning."),
                ("Mota ta cika da fasinjoji.", "The vehicle filled with passengers."),
                ("Hanya ta yi kyau, mun iso da wuri.", "The road was good, we arrived early."),
                ("Kasuwar Zaria ta cika da mutane.", "The Zaria market was full of people."),
                ("Na saya tufafi da takalma.", "I bought clothes and shoes."),
                ("Abokina ya saya kayan marmari.", "My friend bought fruit."),
                ("Mun ci abinci a gidan abinci.", "We ate food at the restaurant."),
                ("Da yamma mun koma Kano.", "In the afternoon we returned to Kano."),
                ("Mun iso gida lafiya da dare.", "We reached home safely at night."),
            ],
            "markers": ["na", "mun", "ta", "ya"],
        },
    }
)
ENTRIES.append(
    {
        "key": "story3",
        "name": "Hausa Short Story III: Plans for Tomorrow",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the future and conditional: plans, "
            "hopes, and promises, told with zan, zai, and in Allah ya so. \n\n"
            "  1. Gobe zan tashi da sassafe. (Tomorrow I will wake early morning.)\n"
            "  2. Zan je kasuwa da abokina. (I will go to the market with my friend.)\n"
            "  3. Zamu saya kayan abinci na sati. (We will buy the week's food supplies.)\n"
            "  4. Zai yi ruwan sama, in Allah ya so. (It will rain, God willing.)\n"
            "  5. Idan ruwan ya sauka, zamu dawo gida da wuri. (If the rain falls, we will return home early.)\n"
            "  6. Da yamma zan karanta littafina. (In the afternoon I will read my book.)\n"
            "  7. Zata zo ta ziyarce ni. (She will come to visit me.)\n"
            "  8. Zamu ci abincin dare tare. (We will eat dinner together.)\n"
            "  9. Idan na gama, zan yi barci. (When I finish, I will sleep.)\n"
            "  10. Gobe za ta fi yau kyau, in Allah ya so. (Tomorrow will be better than today, God willing.)\n\n"
            "The future skeleton: gobe and idan open each plan, the future "
            "markers (zan, zamu, zai, zata) vow each deed, and in Allah ya "
            "so seals the plans that belong to God. Conditionals pair idan "
            "(if) with the future: idan ruwan ya sauka, zamu dawo."
        ),
        "how_it_works": (
            "Plan your own tomorrow in ten sentences on this skeleton: "
            "waking, going, buying, weather, condition, afternoon, visit, "
            "dinner, finishing, hope. Practice the idan pair until it is "
            "automatic: idan na gama, zan... (when I finish, I will...); "
            "idan ka zo, zamu... (if you come, we will...). Close every "
            "plan that depends on heaven with in Allah ya so - it is both "
            "grammar and good manners."
        ),
        "key_points": [
            "10-sentence future/conditional story with line-by-line translation.",
            "Future markers: zan, zamu, zai, zata, zasu.",
            "Conditionals: idan + completed, then future.",
            "in Allah ya so seals plans beyond human control.",
        ],
        "requirements": [
            "Plan tomorrow in ten Hausa sentences.",
            "Build five idan conditionals from your own life.",
        ],
        "standards": [
            "Future and conditional forms follow Newman 2000 and Jaggar 2001.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR],
        "must_contain": ["Gobe zan tashi da sassafe", "Idan ruwan ya sauka, zamu dawo gida da wuri", "in Allah ya so"],
        "sig_lens": (
            "Through the Signature lens these plans are sworn vows of "
            "tomorrow: each zan a promise sealed, each idan a condition "
            "witnessed, each in Allah ya so a humble clause - the future "
            "entered into the archive as intention, honestly marked as not "
            "yet done."
        ),
        "drill": {
            "lines": [
                ("Gobe zan tashi da sassafe.", "Tomorrow I will wake early morning."),
                ("Zan je kasuwa da abokina.", "I will go to the market with my friend."),
                ("Zamu saya kayan abinci na sati.", "We will buy the week's food supplies."),
                ("Zai yi ruwan sama, in Allah ya so.", "It will rain, God willing."),
                ("Idan ruwan ya sauka, zamu dawo gida da wuri.", "If the rain falls, we will return home early."),
                ("Da yamma zan karanta littafina.", "In the afternoon I will read my book."),
                ("Zata zo ta ziyarce ni.", "She will come to visit me."),
                ("Zamu ci abincin dare tare.", "We will eat dinner together."),
                ("Idan na gama, zan yi barci.", "When I finish, I will sleep."),
                ("Gobe za ta fi yau kyau, in Allah ya so.", "Tomorrow will be better than today, God willing."),
            ],
            "future_markers": ["zan", "zamu", "zai", "zata", "zasu"],
        },
    }
)

ENTRIES.append(
    {
        "key": "idioms",
        "name": "Hausa Idioms and Proverbs",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Hausa idioms and proverbs (karin magana): each with "
            "the Hausa, a literal translation, the real meaning, and an "
            "example sentence. Proverbs are the university of Hausa wisdom; "
            "speakers quote them to settle arguments, give advice, and mark "
            "a person as truly fluent. \n\n"
            "  1. Duniya makaranta ce. (Lit: The world is a school. Meaning: life teaches; learn from experience.) Ex: Ka koya daga kuskurenka, duniya makaranta ce. (Learn from your mistake; the world is a school.)\n"
            "  2. Abin da ka shuka shi zaka girba. (Lit: What you plant, you will harvest. Meaning: you reap what you sow.) Ex: Ka yi aiki tukuru, abin da ka shuka shi zaka girba. (Work hard; you reap what you sow.)\n"
            "  3. Gaskiya tafi komai. (Lit: Truth surpasses everything. Meaning: honesty wins in the end.) Ex: Ka fadi gaskiya kullum, gaskiya tafi komai. (Always tell the truth; truth surpasses everything.)\n"
            "  4. Sannu a hankali ake cin tuwo. (Lit: Slowly and carefully is how tuwo is eaten. Meaning: patience achieves; haste ruins.) Ex: Kada ka yi sauri, sannu a hankali ake cin tuwo. (Do not rush; patience achieves.)\n"
            "  5. Ruwa da mai ba su hadu. (Lit: Water and oil do not mix. Meaning: opposites cannot unite.) Ex: Gaskiya da karya kamar ruwa da mai ne, ba su hadu. (Truth and lies are like water and oil; they do not mix.)\n"
            "  6. Hankali tafi karfi. (Lit: Wisdom beats strength. Meaning: brains beat brawn.) Ex: Ka yi tunani kafin aiki, hankali tafi karfi. (Think before acting; wisdom beats strength.)\n"
            "  7. Dare daya ba ya hana safiya fitowa. (Lit: One night does not stop morning from coming. Meaning: hard times pass.) Ex: Ka yi hakuri, dare daya ba ya hana safiya fitowa. (Be patient; hard times pass.)\n"
            "  8. Kowa ya san inda takalmansa ke masa ciwo. (Lit: Everyone knows where his shoe pinches him. Meaning: each person knows his own trouble.) Ex: Kada ka yanke hukunci, kowa ya san inda takalmansa ke masa ciwo. (Do not judge; each person knows his own trouble.)\n"
            "  9. Ba a san dan uwanka ba sai ran bukata. (Lit: You do not know your brother until the day of need. Meaning: hardship reveals true friends.) Ex: A ran bukata na gane abokaina, ba a san dan uwanka ba sai ran bukata. (In need I knew my friends; hardship reveals true friends.)\n"
            "  10. Kada ka yaba wa kanka, bari wasu su yabe ka. (Lit: Do not praise yourself; let others praise you. Meaning: humility earns honor.) Ex: Yi aiki mai kyau, kada ka yaba wa kanka. (Do good work; do not praise yourself.)\n"
            "  11. Abin duniya ba ya karewa. (Lit: Worldly things never end. Meaning: desire is endless; be content.) Ex: Ka gamsu da abin da kake da shi, abin duniya ba ya karewa. (Be content with what you have; desire is endless.)\n"
            "  12. Komai nisa ya yi kusa. (Lit: However far, it draws near. Meaning: the distant goal approaches with effort.) Ex: Ka ci gaba da tafiya, komai nisa ya yi kusa. (Keep going; the goal approaches.)\n"
            "  13. Gari ya waye. (Lit: The town has dawned. Meaning: a new day has come; a fresh start.) Ex: Manta jiya, gari ya waye. (Forget yesterday; it is a new day.)\n"
            "  14. Tsuntsu mai son gida ba ya barshi. (Lit: A bird that loves home does not leave it. Meaning: love of home keeps one rooted.) Ex: Duk inda na je, gida ne mafi dadi; tsuntsu mai son gida ba ya barshi. (Wherever I go, home is sweetest; love of home keeps one rooted.)\n"
            "  15. Fushi ba ya maganin komai. (Lit: Anger cures nothing. Meaning: anger solves nothing.) Ex: Ka yi hakuri, fushi ba ya maganin komai. (Be patient; anger solves nothing.)\n"
            "  16. Ilimi shi ne gishirin rayuwa. (Lit: Knowledge is the salt of life. Meaning: learning flavors existence.) Ex: Ka karanta kullum, ilimi shi ne gishirin rayuwa. (Study daily; knowledge is the salt of life.)\n"
            "  17. Hakuri shi ne maganin zuciya. (Lit: Patience is the medicine of the heart. Meaning: patience heals.) Ex: Zuciyarka za ta yi sanyi, hakuri shi ne maganin zuciya. (Your heart will cool; patience heals.)\n"
            "  18. Abota ta gaskiya ba ta sayuwa. (Lit: True friendship cannot be bought. Meaning: loyalty is priceless.) Ex: Ka kula da abokanka, abota ta gaskiya ba ta sayuwa. (Care for your friends; loyalty is priceless.)\n"
            "  19. Mai yawan magana ba ya aikin komai. (Lit: The chatterbox does no work. Meaning: talk without action is empty.) Ex: Ka yi aiki tukuru, mai yawan magana ba ya aikin komai. (Work hard; talk without action is empty.)\n"
            "  20. Sai lokaci ya yi. (Lit: Until the time comes. Meaning: wait for the right moment.) Ex: Kada ka yi sauri, sai lokaci ya yi. (Do not rush; wait for the right moment.)"
        ),
        "how_it_works": (
            "Learn each proverb in three layers: say the Hausa until it is "
            "musical, state the literal translation, then state the real "
            "meaning - and only then use the example sentence. Proverbs are "
            "deployed, not recited: drop duniya makaranta ce when someone "
            "learns the hard way, dare daya ba ya hana safiya fitowa when "
            "someone despairs, sannu a hankali ake cin tuwo when someone "
            "rushes. Keep a proverb journal: one new karin magana per day, "
            "with a situation where you could use it."
        ),
        "key_points": [
            "20 idioms/proverbs: Hausa + literal translation + real meaning + example sentence.",
            "Proverbs settle arguments and mark true fluency.",
            "Learned in three layers: sound, literal, meaning.",
            "Deployed by situation, not recited at random.",
        ],
        "requirements": [
            "Use five proverbs correctly in conversation.",
            "Keep a proverb journal: one per day with a usage situation.",
        ],
        "standards": [
            "Proverbs are presented as documented Hausa karin magana with literal and idiomatic glosses.",
        ],
        "citations": [CIT_ABRAHAM, CIT_NEWMAN],
        "must_contain": ["Duniya makaranta ce", "Sannu a hankali ake cin tuwo", "Hankali tafi karfi", "Kowa ya san inda takalmansa ke masa ciwo"],
        "sig_lens": (
            "Through the Signature lens the proverbs are the sworn laws of "
            "the elders: each karin magana a sealed ruling, each literal "
            "image a parable-witness, each meaning a verdict - the whole "
            "moral code of the language entered as case law."
        ),
        "drill": {
            "proverbs": [
                ("Duniya makaranta ce.", "The world is a school.", "Life teaches."),
                ("Abin da ka shuka shi zaka girba.", "What you plant, you will harvest.", "You reap what you sow."),
                ("Gaskiya tafi komai.", "Truth surpasses everything.", "Honesty wins."),
                ("Sannu a hankali ake cin tuwo.", "Slowly is how tuwo is eaten.", "Patience achieves."),
                ("Ruwa da mai ba su hadu.", "Water and oil do not mix.", "Opposites cannot unite."),
                ("Hankali tafi karfi.", "Wisdom beats strength.", "Brains beat brawn."),
                ("Dare daya ba ya hana safiya fitowa.", "One night does not stop morning.", "Hard times pass."),
                ("Kowa ya san inda takalmansa ke masa ciwo.", "Everyone knows where his shoe pinches.", "Each knows his own trouble."),
                ("Ba a san dan uwanka ba sai ran bukata.", "You do not know your brother until need.", "Hardship reveals friends."),
                ("Kada ka yaba wa kanka, bari wasu su yabe ka.", "Do not praise yourself.", "Humility earns honor."),
                ("Abin duniya ba ya karewa.", "Worldly things never end.", "Be content."),
                ("Komai nisa ya yi kusa.", "However far, it draws near.", "The goal approaches."),
                ("Gari ya waye.", "The town has dawned.", "A fresh start."),
                ("Tsuntsu mai son gida ba ya barshi.", "A bird that loves home does not leave.", "Love of home roots one."),
                ("Fushi ba ya maganin komai.", "Anger cures nothing.", "Anger solves nothing."),
                ("Ilimi shi ne gishirin rayuwa.", "Knowledge is the salt of life.", "Learning flavors life."),
                ("Hakuri shi ne maganin zuciya.", "Patience is the medicine of the heart.", "Patience heals."),
                ("Abota ta gaskiya ba ta sayuwa.", "True friendship cannot be bought.", "Loyalty is priceless."),
                ("Mai yawan magana ba ya aikin komai.", "The chatterbox does no work.", "Talk without action is empty."),
                ("Sai lokaci ya yi.", "Until the time comes.", "Wait for the right moment."),
            ],
        },
    }
)
ENTRIES.append(
    {
        "key": "registers",
        "name": "Hausa Formal and Polite Registers",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen formal-versus-informal pairs for letters, business, "
            "and elders: the two voices of Hausa, plain and honored. "
            "Informal speech uses bare commands, plain pronouns, and short "
            "forms; formal speech uses ku plurals of respect, don Allah "
            "softening, titles (Malam, Alhaji, Hajiya, Sarki), and blessing "
            "formulas. \n\n"
            "  1. INF: Zo nan. / FOR: Don Allah, ku zo nan. (Come here. / Please come here - respectful.)\n"
            "  2. INF: Kawo ruwa. / FOR: Za ku iya kawo mini ruwa? (Bring water. / Could you bring me water?)\n"
            "  3. INF: Sunanka me ne? / FOR: Menene sunanku, don Allah? (What is your name? / What is your name, please - respectful.)\n"
            "  4. INF: Ina son wannan. / FOR: Ina bukatar wannan, don Allah. (I want this. / I need this, please.)\n"
            "  5. INF: Ba na so. / FOR: Yi hakuri, ba na bukata. (I do not want it. / Excuse me, I do not need it.)\n"
            "  6. INF: Tafi! / FOR: Sai mun hadu, Allah ya kiyaye hanya. (Go! / Until we meet, may God guard the road.)\n"
            "  7. INF: Yaya aiki? / FOR: Malam, yaya aikin? Allah ya taimaka. (How is work? / Sir, how is the work? May God help.)\n"
            "  8. INF: Ka yi kuskure. / FOR: Yi hakuri, akwai kuskure kadan. (You made a mistake. / Excuse me, there is a small mistake.)\n"
            "  9. INF: Ba daidai ba ne. / FOR: Yi hakuri, ban yarda ba. (It is not right. / Excuse me, I do not agree.)\n"
            "  10. INF: Na gode. / FOR: Na gode kwarai, Allah ya saka da alheri. (Thank you. / Thank you truly, may God reward with good.)\n"
            "  11. INF: Sai an jima. / FOR: Sai mun hadu lafiya, in Allah ya so. (See you soon. / Until we meet in health, God willing.)\n"
            "  12. INF: Barka da zuwa. / FOR: Barka da zuwa, Malam. Gidanka ne. (Welcome. / Welcome, sir. It is your house - i.e. make yourself at home.)\n"
            "  13. INF: Me kake so? / FOR: Menene bukatarku? (What do you want? / What is your need - respectful.)\n"
            "  14. INF: Kana lafiya? / FOR: Lafiya kalau? Allah ya kara lafiya. (Are you well? / Very well? May God increase health.)\n"
            "  15. Letter opening INF: Sannu. / FOR: Bismillah. Bayan gaisuwa ta musamman... (Hello. / In God's name. After special greetings...)\n\n"
            "Titles of respect: Malam (learned man/teacher), Mallama "
            "(learned woman), Alhaji/Hajiya (one who made pilgrimage), "
            "Sarki (king/chief), Maigida (head of household). Use them with "
            "the ku forms: Malam, ku zauna (Sir, please be seated)."
        ),
        "how_it_works": (
            "For each pair, say the informal version to a friend and the "
            "formal version to an elder - feel the register shift in your "
            "own mouth. The formal toolkit has five tools: ku instead of "
            "ka/ki, don Allah softening, titles (Malam, Hajiya), blessing "
            "formulas (Allah ya saka da alheri), and indirect phrasing "
            "(akwai kuskure kadan instead of ka yi kuskure). Write a short "
            "formal letter using the pair-15 opening and three formal "
            "requests; then rewrite it informal to a friend."
        ),
        "key_points": [
            "15 formal/informal pairs: letters, business, elders.",
            "Formal tools: ku respect plural, don Allah, titles, blessings, indirect phrasing.",
            "Titles: Malam, Mallama, Alhaji, Hajiya, Sarki, Maigida.",
            "Bare commands for intimates/urgency; requests for elders.",
        ],
        "requirements": [
            "Address an elder correctly in a five-exchange conversation.",
            "Write a formal letter and an informal note on the same topic.",
        ],
        "standards": [
            "Register description follows standard sociolinguistic accounts in the reference grammars.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR],
        "must_contain": ["Don Allah, ku zo nan", "Na gode kwarai, Allah ya saka da alheri", "Malam, ku zauna", "Yi hakuri, akwai kuskure kadan"],
        "sig_lens": (
            "Through the Signature lens the registers are the two sworn "
            "voices: the plain voice for equals, sealed direct; the honored "
            "voice for elders, sealed with blessing and title - each "
            "person addressed at exactly the height they are owed."
        ),
        "drill": {
            "pairs": 15,
            "formal_tools": ["ku", "don Allah", "titles", "blessings", "indirect phrasing"],
            "titles": ["Malam", "Mallama", "Alhaji", "Hajiya", "Sarki", "Maigida"],
        },
    }
)
ENTRIES.append(
    {
        "key": "complex",
        "name": "Hausa Compound and Complex Sentences",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen long sentences with clauses, connectors, and relative "
            "clauses - parsed and translated: the architecture of fluent "
            "Hausa. Connectors: da (and), amma (but), saboda (because), "
            "idan (if/when), ko (or), sannan (then), duk da (although), "
            "domin (so that/in order to), kafin (before), bayan (after). \n\n"
            "  1. Na tashi da sassafe, sannan na yi wanka, na ci abinci. (I woke early, then I bathed, [then] I ate. - clause chain with sannan)\n"
            "  2. Yana son tuwo amma ba ya son miya. (He likes tuwo but he does not like soup. - amma contrast)\n"
            "  3. Mun je kasuwa saboda muna bukatar kayan abinci. (We went to the market because we need food supplies. - saboda cause)\n"
            "  4. Idan ka zo gobe, zamu tafi tare. (If you come tomorrow, we will go together. - idan condition)\n"
            "  5. Ko za ka zo ko ba za ka zo ba, ni zan tafi. (Whether you come or not, I will go. - ko alternative)\n"
            "  6. Mutumin da ya zo jiya abokina ne. (The man who came yesterday is my friend. - da relative clause)\n"
            "  7. Littafin da na saya yana da dadi. (The book that I bought is interesting. - da relative clause)\n"
            "  8. Duk da ruwan sama, mun tafi aiki. (Although it rained, we went to work. - duk da concession)\n"
            "  9. Na yi aiki tukuru domin in ci jarabawa. (I worked hard so that I pass the exam. - domin purpose)\n"
            "  10. Kafin ka tafi, ka rufe kofa. (Before you go, close the door. - kafin time clause)\n"
            "  11. Bayan mun ci abinci, mun yi hira. (After we ate, we chatted. - bayan time clause)\n"
            "  12. Yaron da ke wasa a waje dan uwana ne. (The boy who is playing outside is my brother. - ke relative, ongoing)\n"
            "  13. Na san inda yake zaune. (I know where he lives. - inda clause)\n"
            "  14. Ta fada mini cewa zata zo gobe. (She told me that she will come tomorrow. - cewa reported speech)\n"
            "  15. Duk abin da ka yi, ka yi shi da gaskiya. (Whatever you do, do it with honesty. - duk abin da free relative)\n\n"
            "Parse pattern for relative clauses: noun + da/ke + clause "
            "(mutumin da ya zo = the man who came; yaron da ke wasa = the "
            "boy who is playing). Reported speech uses cewa (that): ya "
            "fada mini cewa... (he told me that...)."
        ),
        "how_it_works": (
            "Take each sentence and label its skeleton: chain, contrast, "
            "cause, condition, alternative, relative, concession, purpose, "
            "time-before, time-after, reported. Then rebuild it with your "
            "own content keeping the skeleton: keep idan ka zo gobe, zamu "
            "tafi tare and swap in idan ruwan ya sauka, zamu zauna a gida. "
            "Chain three simple sentences from earlier records into one "
            "long sentence with sannan and da. The relative clause with da "
            "is the most powerful tool here - practice it on ten nouns."
        ),
        "key_points": [
            "15 parsed complex sentences: chains, contrasts, causes, conditions, relatives.",
            "Connectors: da, amma, saboda, idan, ko, sannan, duk da, domin, kafin, bayan.",
            "Relative clauses: noun + da/ke + clause.",
            "Reported speech: cewa (that).",
        ],
        "requirements": [
            "Label the skeleton of all 15 sentences.",
            "Build ten new complex sentences on the skeletons.",
        ],
        "standards": [
            "Clause analysis follows Newman 2000 and Jaggar 2001.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR],
        "must_contain": ["Mutumin da ya zo jiya abokina ne", "Idan ka zo gobe, zamu tafi tare", "Ta fada mini cewa zata zo gobe", "Duk abin da ka yi, ka yi shi da gaskiya"],
        "sig_lens": (
            "Through the Signature lens complex sentences are sworn "
            "edifices: each clause a sealed chamber, each connector a "
            "bound joint, each relative clause a witness called by name - "
            "the whole structure standing because every joint was sealed "
            "in order."
        ),
        "drill": {
            "connectors": ["da", "amma", "saboda", "idan", "ko", "sannan", "duk da", "domin", "kafin", "bayan"],
            "sentences": 15,
            "skeletons": ["chain", "contrast", "cause", "condition", "alternative", "relative", "concession", "purpose", "time-before", "time-after", "reported"],
        },
    }
)

ENTRIES.append(
    {
        "key": "conv_market",
        "name": "Hausa Conversation: At the Market",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A 20-line bilingual dialogue at Kasuwar Kano: greeting, "
            "browsing, bargaining, paying, and parting - annotated with the "
            "grammar at work. A = Aisha (buyer), M = Musa (seller). \n\n"
            "  A1. Sannu da aiki! - Hello, greetings on your work! [greeting ritual]\n"
            "  M1. Sannu da zuwa! Lafiya lau. - Welcome! I am fine. [answer + health]\n"
            "  A2. Lafiya kalau. Ina so in saya atiku. - Very well. I want to buy cloth. [purpose]\n"
            "  M2. Ga atiku mai kyau. Dubi wannan. - Here is good cloth. Look at this. [showing]\n"
            "  A3. Wannan mai kyau ne. Nawa ne farashin? - This is good. How much is the price? [asking price]\n"
            "  M3. Naira dubu biyar ne. - It is five thousand naira. [naming price]\n"
            "  A4. Yayi tsada sosai! Ka rage mini. - Too expensive! Reduce it for me. [reacting]\n"
            "  M4. Kudin karshe naira dubu hudu. - Last price, four thousand naira. [countering]\n"
            "  A5. Naira dubu uku da dari biyar? - Three thousand two hundred? [bargaining]\n"
            "  M5. A'a, ba zai yiwu ba. Dubu hudu. - No, it cannot be. Four thousand. [holding]\n"
            "  A6. To, na amince. Ga kudi. - OK, I agree. Here is the money. [closing]\n"
            "  M6. Na gode. Akwai canji? - Thank you. Is there change? [change]\n"
            "  A7. Kudin daidai ne, babu canji. - The money is exact, no change. [exact payment]\n"
            "  M7. Madalla! Kina so wani abu? - Well done! Do you want something else? [upsell]\n"
            "  A8. I, ina so hula. Nawa ne? - Yes, I want a cap. How much? [second item]\n"
            "  M8. Hula naira dari biyar ne. - The cap is five hundred naira. [price]\n"
            "  A9. Yayi kyau. Zan saya. - Good. I will buy it. [agreeing]\n"
            "  M9. Ga hularki. Sai mun dawo! - Here is your cap. Come again! [handing over]\n"
            "  A10. Mun gode. Sai an jima! - Thank you. See you soon! [parting]\n"
            "  M10. Allah ya kiyaye hanya! - May God guard the road! [blessing farewell]\n\n"
            "Grammar at work: the greeting ritual (A1-M1), purpose with "
            "subjunctive (ina so in saya), price questions (nawa ne "
            "farashin?), bargaining imperatives (ka rage mini), agreement "
            "(na amince), and the blessing farewell (Allah ya kiyaye "
            "hanya). Act it out with a partner, swapping roles."
        ),
        "how_it_works": (
            "Memorize the dialogue in pairs of lines, then perform it with "
            "a partner - first reading, then from memory, then "
            "improvising: change the goods (atiku to takalma), change the "
            "prices, change the outcome (walk away: yayi tsada, sai an "
            "jima). The annotations name the move each line makes; learn "
            "the moves, not just the words, and you can bargain anywhere."
        ),
        "key_points": [
            "20-line bilingual market dialogue, annotated.",
            "Full bargaining arc: greet, browse, ask, react, counter, close, pay, part.",
            "Grammar moves labeled per line.",
            "Role-play both buyer and seller.",
        ],
        "requirements": [
            "Perform the dialogue from memory with a partner.",
            "Improvise a new bargaining scene with different goods.",
        ],
        "standards": [
            "Dialogue follows standard Kano market usage.",
        ],
        "citations": [CIT_ABRAHAM, CIT_NEWMAN],
        "must_contain": ["Sannu da aiki", "Nawa ne farashin", "Ka rage mini", "na amince", "Allah ya kiyaye hanya"],
        "sig_lens": (
            "Through the Signature lens this market dialogue is the sworn "
            "transcript of trade: each offer witnessed, each counter "
            "sealed, each agreement signed in coin - the whole commerce of "
            "the archive conducted aloud and recorded."
        ),
        "drill": {
            "lines": 20,
            "moves": ["greeting ritual", "purpose", "showing", "asking price", "naming price", "reacting", "countering", "bargaining", "holding", "closing", "change", "exact payment", "upsell", "second item", "price", "agreeing", "handing over", "parting", "blessing farewell"],
        },
    }
)
ENTRIES.append(
    {
        "key": "conv_friend",
        "name": "Hausa Conversation: Meeting a Friend",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A 20-line bilingual dialogue: two old friends meet on the "
            "road to the motor park - annotated. A = Aisha, B = Bala. \n\n"
            "  A1. Bala! Sannu da zuwa! - Bala! Welcome! [surprised greeting]\n"
            "  B1. Aisha! Dama ke ce! Lafiya? - Aisha! So it is you! Are you well? [recognition]\n"
            "  A2. Lafiya lau. Tun yaushe kake nan? - I am fine. Since when are you here? [catching up]\n"
            "  B2. Na dawo jiya da dare. - I returned yesterday night. [news]\n"
            "  A3. Masha Allah! Yaya tafiya? - Wonderful! How was the trip? [blessing + question]\n"
            "  B3. Tafiya ta yi kyau, alhamdulillah. - The trip was good, praise God. [answer + thanks]\n"
            "  A4. Ina iyalinka? - Where is your family? [family inquiry]\n"
            "  B4. Suna lafiya, suna gida. - They are well, at home. [family news]\n"
            "  A5. Zo mu sha shayi. - Come, let us drink tea. [invitation]\n"
            "  B5. To, mu je. Ina gidan shayi? - OK, let us go. Where is the tea house? [accepting]\n"
            "  A6. Yana kusa, ta can. - It is near, that way. [directions]\n"
            "  B6. Tun yaushe kika fara aiki a asibiti? - Since when did you start work at the hospital? [news question]\n"
            "  A7. Na fara shekara biyu da suka wuce. - I started two years ago. [career news]\n"
            "  B7. Madalla! Allah ya kara basira. - Bravo! May God increase wisdom. [praise + blessing]\n"
            "  A8. Amin. Yaya kasuwancinka? - Amen. How is your business? [return blessing + question]\n"
            "  B8. Yana tafiya a hankali. - It is going slowly. [honest answer]\n"
            "  A9. Allah ya bude hanya. - May God open the way. [blessing]\n"
            "  B9. Amin, na gode. Sai an jima? - Amen, thank you. See you soon? [thanks + parting question]\n"
            "  A10. Sai an jima, in Allah ya so! - See you soon, God willing! [parting]\n"
            "  B10. Allah ya kiyaye ki! - May God protect you! [farewell blessing]\n\n"
            "Grammar at work: recognition exclamations, tun yaushe "
            "(since when) for catching up, invitations with mu (let us), "
            "blessing exchanges (Allah ya kara basira / amin), and the "
            "God-willing close (in Allah ya so). Notice the -ka/-ki "
            "endings tracking the speakers."
        ),
        "how_it_works": (
            "This dialogue is the template for every reunion: greeting, "
            "recognition, catching up (tun yaushe...?), family inquiry, "
            "invitation, news exchange, blessings, parting. Practice it "
            "until you can run a reunion with anyone: swap in your own "
            "news (na fara aiki a..., na dawo daga...), your own family, "
            "your own invitation (zo mu ci abinci). The blessing reflex - "
            "answering every good news with Allah ya... and every blessing "
            "with amin - is the soul of the exchange."
        ),
        "key_points": [
            "20-line bilingual reunion dialogue, annotated.",
            "Reunion arc: greet, recognize, catch up, family, invite, news, bless, part.",
            "tun yaushe (since when) drives the catching-up.",
            "Blessing reflex: every good news answered with Allah ya... / amin.",
        ],
        "requirements": [
            "Perform the dialogue from memory.",
            "Run a reunion with your own news in Hausa.",
        ],
        "standards": [
            "Dialogue follows standard Kano social usage.",
        ],
        "citations": [CIT_NEWMAN, CIT_ABRAHAM],
        "must_contain": ["Tun yaushe kake nan", "Zo mu sha shayi", "Allah ya kara basira", "Allah ya kiyaye ki"],
        "sig_lens": (
            "Through the Signature lens this reunion is the sworn renewal "
            "of bond: each recognition a seal broken open, each news a "
            "testimony given, each blessing a vow spoken over a friend - "
            "the archive recording that no one returns unrecognized."
        ),
        "drill": {
            "lines": 20,
            "moves": ["surprised greeting", "recognition", "catching up", "news", "blessing + question", "answer + thanks", "family inquiry", "family news", "invitation", "accepting", "directions", "news question", "career news", "praise + blessing", "return blessing + question", "honest answer", "blessing", "thanks + parting question", "parting", "farewell blessing"],
        },
    }
)
ENTRIES.append(
    {
        "key": "conv_problem",
        "name": "Hausa Conversation: Solving a Problem",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A 20-line bilingual dialogue: a burst pipe, a landlord, and a "
            "plumber - a problem stated, negotiated, and solved, annotated. "
            "A = Aisha (tenant), L = Landlord (Maigida), P = Plumber. \n\n"
            "  A1. Maigida, sannu da aiki. Akwai matsala. - Sir, greetings. There is a problem. [respectful opening]\n"
            "  L1. Sannu, Aisha. Mene ne matsalar? - Hello, Aisha. What is the problem? [asking]\n"
            "  A2. Bututun ruwa ya fashe a madafa. - The water pipe burst in the kitchen. [stating]\n"
            "  L2. Ya fashe? Yaushe? - It burst? When? [clarifying]\n"
            "  A3. Ya fashe da safe, ruwan yana zuba. - It burst this morning, water is pouring. [detail]\n"
            "  L3. Na ji. Zan kira mai gyara. - I understand. I will call the repairman. [promising]\n"
            "  A4. Don Allah, da sauri. Abinci yana lalacewa. - Please, quickly. The food is spoiling. [urging]\n"
            "  L4. Zai zo kafin rana ta fadi. - He will come before sunset. [committing]\n"
            "  P1. Sannu! Ina bututun? - Hello! Where is the pipe? [arriving]\n"
            "  A5. Ga shi a madafa. Dubi nan. - Here it is in the kitchen. Look here. [showing]\n"
            "  P2. Na gani. Matsalar ba ta da girma. - I see it. The problem is not big. [diagnosing]\n"
            "  A6. Zaka iya gyara shi yau? - Can you fix it today? [asking ability]\n"
            "  P3. I, zan gyara shi yanzu. - Yes, I will fix it now. [agreeing]\n"
            "  P4. Na gama! Bude famfon. - Done! Open the tap. [completing]\n"
            "  A7. Ruwan yana zuwa da kyau. Madalla! - The water is coming well. Bravo! [testing + praise]\n"
            "  P5. Nawa ne kudina? Naira dubu biyu ne. - What is my fee? It is two thousand naira. [naming fee]\n"
            "  A8. Ga naira dubu biyu. Na gode sosai. - Here is two thousand naira. Thank you very much. [paying]\n"
            "  L5. Madalla, Aisha. Kira ni idan akwai wani abu. - Well done, Aisha. Call me if there is anything. [closing]\n"
            "  A9. Na gode, Maigida. Sai an jima! - Thank you, sir. See you soon! [thanks]\n"
            "  P6. Sai mun hadu lafiya! - Until we meet in health! [farewell]\n\n"
            "Grammar at work: respectful address (Maigida), problem "
            "statement with completed verbs (ya fashe), urgency with don "
            "Allah da sauri, promises with zan/zai, diagnosis, testing, "
            "payment, and the open-door close (kira ni idan akwai wani "
            "abu). The whole arc: state, clarify, promise, urge, commit, "
            "fix, test, pay, close."
        ),
        "how_it_works": (
            "Problems in Hausa follow this arc: state it plainly (akwai "
            "matsala + completed verb), give the detail, ask for speed "
            "politely, get the commitment, verify the fix, pay, close with "
            "thanks. Practice the arc on three problems of your own: a "
            "broken phone (wayata ta lalace), a missed bus (mota ta tafi), "
            "a lost key (na rasa mabudin). The landlord's close - kira ni "
            "idan akwai wani abu - is worth memorizing whole."
        ),
        "key_points": [
            "20-line trilingual-role problem-solving dialogue, annotated.",
            "Problem arc: state, clarify, promise, urge, commit, fix, test, pay, close.",
            "Respectful address to authority: Maigida + don Allah.",
            "Verification before payment: test, praise, then pay.",
        ],
        "requirements": [
            "Perform the dialogue from memory in all three roles.",
            "Solve three of your own problems on the arc.",
        ],
        "standards": [
            "Dialogue follows standard Kano usage.",
        ],
        "citations": [CIT_NEWMAN, CIT_ABRAHAM],
        "must_contain": ["Akwai matsala", "Bututun ruwa ya fashe a madafa", "Don Allah, da sauri", "Kira ni idan akwai wani abu"],
        "sig_lens": (
            "Through the Signature lens this repair is the sworn mending: "
            "each fault stated truly, each promise sealed with zan, each "
            "fix verified before the coin is paid - the archive recording "
            "that what was broken was witnessed, and what was mended was "
            "proven."
        ),
        "drill": {
            "lines": 20,
            "arc": ["state", "clarify", "promise", "urge", "commit", "arrive", "show", "diagnose", "ask ability", "agree", "complete", "test + praise", "name fee", "pay", "close", "thanks", "farewell"],
        },
    }
)
ENTRIES.append(
    {
        "key": "mastery",
        "name": "Hausa Mastery Review and Full Reference",
        "group": "Mastery Reference",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The whole database in one teaching summary: the alphabet, 200 "
            "core words, the key grammar, and all phrase tables - the "
            "mastery review that turns thirty-three records into one "
            "command of Hausa. \n\n"
            "ALPHABET (Boko, 29 letters): a b ɓ c d ɗ e f g h i j k ƙ l m "
            "n o p r s sh t ts u w y z ƴ. Specials: ɓ ɗ ƙ ƴ. Vowels a e i o "
            "u (short/long). Three tones: high, low, falling. \n\n"
            "200 CORE WORDS (Hausa - English): mutum person, namiji man, "
            "mace woman, yaro boy, yarinya girl, uba father, uwa mother, "
            "dan uwa brother, yar uwa sister, kaka grandparent, aboki friend, "
            "gida house, daki room, madafa kitchen, kofa door, taga window, "
            "kujera chair, tebur table, gado bed, fitila lamp, ruwa water, "
            "abinci food, tuwo tuwo, shinkafa rice, nama meat, kifi fish, "
            "kaza chicken, kwai egg, madara milk, gishiri salt, sukari sugar, "
            "mangwaro mango, ayaba banana, lemu orange, albasa onion, "
            "tumatir tomato, dankali potato, mota car, keke bicycle, jirgin "
            "sama airplane, hanya road, kasuwa market, shago shop, makaranta "
            "school, littafi book, alkalami pen, takarda paper, asibiti "
            "hospital, likita doctor, magani medicine, masallaci mosque, "
            "gari town, birni city, kogi river, daji bush, itace tree, "
            "fure flower, rana sun/day, dare night, safe morning, yamma "
            "afternoon, wata moon/month, tauraro star, sama sky, kasa land, "
            "iska wind, ruwan sama rain, gajimare cloud, sanyi cold, zafi heat, je go, zo come, "
            "tafi go (away), dawo return, ci eat, sha drink, yi do/make, "
            "gani see, ji hear, fada say, tambaya ask, amsa answer, rubuta "
            "write, karanta read, koya learn, koyar teach, aiki work, saya "
            "buy, sayar sell, bude open, rufe close, zauna sit/stay, tashi "
            "get up, kwana sleep, farka wake up, kawo bring, biya pay, ba "
            "give, karba receive, taimaka help, so love/want, ki refuse, "
            "fara begin, gama finish, samu get, rasa lose, manta forget, "
            "tuna remember, babba big, karami small, dogo tall, gajere "
            "short, kyakkyawa beautiful, mugu bad, sabo new, tsoho old, "
            "baki black, fari white, ja red, kore green, dadi sweet, daci "
            "bitter, sauki easy, wahala difficult, nisa far, kusa near, "
            "tsada expensive, rahusa cheap, lafiya healthy, mai kudi rich, "
            "talaka poor, ni I, kai you (m), ke you (f), shi he, ita she, "
            "mu we, ku you (pl), su they, wannan this, wancan that, wa who, "
            "me what, ina where, yaushe when, ta yaya how, me ya sa why, "
            "nawa how many, daya one, biyu two, uku three, hudu four, biyar "
            "five, shida six, bakwai seven, takwas eight, tara nine, goma "
            "ten, ashirin twenty, dari hundred, dubu thousand, yau today, "
            "jiya yesterday, gobe tomorrow, yanzu now, kullum daily, da "
            "safe in the morning, da dare at night, sosai very, kadan a "
            "little, da sauri quickly, a hankali slowly, tare together, "
            "sannu hello, na gode thank you, don Allah please, yi hakuri "
            "excuse me, sannu da zuwa welcome, sai an jima see you soon, "
            "lafiya lau fine, kwarai truly, kuma also, amma but, saboda "
            "because, idan if, da and, ko or, sannan then, in Allah ya so "
            "God willing, alhamdulillah praise God, to OK, i yes, a'a no. \n\n"
            "KEY GRAMMAR: SVO order; adjectives after nouns (gida babba); "
            "gender m/f with agreement (ya/ta, ne/ce); plurals (yara, "
            "mutane, littattafai, gidaje); no articles; negation ba ... ba "
            "(ban tafi ba); questions by intonation/shin/question words; "
            "copula ne/ce; possession na/ta link; TAM markers - completed "
            "na/ka/ya/mun, ongoing ina/kana/yana, future zan/zaka/zai, "
            "habitual na kan, subjunctive in/ka/ya; commands bare stem "
            "(zo!), polite don Allah, prohibition kada; relatives with da "
            "(mutumin da ya zo). \n\n"
            "PHRASE TABLES: greetings (sannu, sannu da safe/rana/dare, ina "
            "kwana/yini, lafiya lau, na gode, sai an jima, Allah ya kiyaye "
            "ka); market (nawa ne farashin, yayi tsada, ka rage mini, mun "
            "yi ciniki); travel (ina tashar mota, nawa ne kudin mota, tafi "
            "kai tsaye); health (jikina yana ciwo, ina da zazzabi, ina "
            "bukatar likita); time (karfe daya, yau Lahadi ne, watan "
            "Janairu). \n\n"
            "Study order for mastery: alphabet, phonology, nouns, verbs, "
            "adjectives, pronouns, numbers, greetings, grammar, themes "
            "11-20, tenses, Q&A, commands, descriptions, stories, idioms, "
            "registers, complex sentences, conversations - then this "
            "review, then teach it to someone else."
        ),
        "how_it_works": (
            "Use this record as the daily drill sheet: read the alphabet "
            "aloud, recite the TAM markers, run 20 random core words both "
            "directions, build five sentences from the grammar line, and "
            "hold one phrase-table exchange. When every section is fluent, "
            "teach the whole ladder to another learner - teaching is the "
            "final seal of mastery. Return to any record that hesitates; "
            "the ladder is circular, not a staircase."
        ),
        "key_points": [
            "Consolidated reference: alphabet, 200 core words, grammar, phrase tables.",
            "Daily drill sheet for the whole database.",
            "Study order restated: foundations to mastery.",
            "Teaching another is the final seal.",
        ],
        "requirements": [
            "Recite the alphabet, markers, and 200 words from memory.",
            "Teach the ladder to another learner.",
        ],
        "standards": [
            "All summaries derive strictly from records 1-33 of this database.",
        ],
        "citations": [CIT_NEWMAN, CIT_JAGGAR, CIT_ABRAHAM, CIT_ISO],
        "must_contain": ["200 CORE WORDS", "gida babba", "ban tafi ba", "mutumin da ya zo", "sai an jima"],
        "sig_lens": (
            "Through the Signature lens this review is the sworn seal upon "
            "the whole work: the alphabet counted, the two hundred words "
            "tallied, the grammar bound, the phrases tabled - the complete "
            "covenant of the Hausa language, closed and signed."
        ),
        "drill": {
            "core_words": [
                ("mutum", "person"), ("namiji", "man"), ("mace", "woman"),
                ("yaro", "boy"), ("yarinya", "girl"), ("uba", "father"),
                ("uwa", "mother"), ("dan uwa", "brother"), ("yar uwa", "sister"),
                ("kaka", "grandparent"), ("aboki", "friend"), ("gida", "house"),
                ("daki", "room"), ("madafa", "kitchen"), ("kofa", "door"),
                ("taga", "window"), ("kujera", "chair"), ("tebur", "table"),
                ("gado", "bed"), ("fitila", "lamp"), ("ruwa", "water"),
                ("abinci", "food"), ("tuwo", "tuwo"), ("shinkafa", "rice"),
                ("nama", "meat"), ("kifi", "fish"), ("kaza", "chicken"),
                ("kwai", "egg"), ("madara", "milk"), ("gishiri", "salt"),
                ("sukari", "sugar"), ("mangwaro", "mango"), ("ayaba", "banana"),
                ("lemu", "orange"), ("albasa", "onion"), ("tumatir", "tomato"),
                ("dankali", "potato"), ("mota", "car"), ("keke", "bicycle"),
                ("jirgin sama", "airplane"), ("hanya", "road"), ("kasuwa", "market"),
                ("shago", "shop"), ("makaranta", "school"), ("littafi", "book"),
                ("alkalami", "pen"), ("takarda", "paper"), ("asibiti", "hospital"),
                ("likita", "doctor"), ("magani", "medicine"), ("masallaci", "mosque"),
                ("gari", "town"), ("birni", "city"), ("kogi", "river"),
                ("daji", "bush"), ("itace", "tree"), ("fure", "flower"),
                ("rana", "sun/day"), ("dare", "night"), ("safe", "morning"),
                ("yamma", "afternoon"), ("wata", "moon/month"), ("tauraro", "star"),
                ("sama", "sky"), ("kasa", "land"), ("iska", "wind"),
                ("ruwan sama", "rain"), ("gajimare", "cloud"), ("sanyi", "cold"),
                ("zafi", "heat"), ("je", "go"), ("zo", "come"), ("tafi", "go (away)"),
                ("dawo", "return"), ("ci", "eat"), ("sha", "drink"),
                ("yi", "do/make"), ("gani", "see"), ("ji", "hear"),
                ("fada", "say"), ("tambaya", "ask"), ("amsa", "answer"),
                ("rubuta", "write"), ("karanta", "read"), ("koya", "learn"),
                ("koyar", "teach"), ("aiki", "work"), ("saya", "buy"),
                ("sayar", "sell"), ("bude", "open"), ("rufe", "close"),
                ("zauna", "sit/stay"), ("tashi", "get up"), ("kwana", "sleep"),
                ("farka", "wake up"), ("kawo", "bring"), ("biya", "pay"),
                ("ba", "give"), ("karba", "receive"), ("taimaka", "help"),
                ("so", "love/want"), ("ki", "refuse"), ("fara", "begin"),
                ("gama", "finish"), ("samu", "get"), ("rasa", "lose"),
                ("manta", "forget"), ("tuna", "remember"), ("babba", "big"),
                ("karami", "small"), ("dogo", "tall"), ("gajere", "short"),
                ("kyakkyawa", "beautiful"), ("mugu", "bad"), ("sabo", "new"),
                ("tsoho", "old"), ("baki", "black"), ("fari", "white"),
                ("ja", "red"), ("kore", "green"), ("dadi", "sweet"),
                ("daci", "bitter"), ("sauki", "easy"), ("wahala", "difficult"),
                ("nisa", "far"), ("kusa", "near"), ("tsada", "expensive"),
                ("rahusa", "cheap"), ("lafiya", "healthy"), ("mai kudi", "rich"),
                ("talaka", "poor"), ("ni", "I"), ("kai", "you (m)"),
                ("ke", "you (f)"), ("shi", "he"), ("ita", "she"), ("mu", "we"),
                ("ku", "you (pl)"), ("su", "they"), ("wannan", "this"),
                ("wancan", "that"), ("wa", "who"), ("me", "what"),
                ("ina", "where"), ("yaushe", "when"), ("ta yaya", "how"),
                ("me ya sa", "why"), ("nawa", "how many"), ("daya", "one"),
                ("biyu", "two"), ("uku", "three"), ("hudu", "four"),
                ("biyar", "five"), ("shida", "six"), ("bakwai", "seven"),
                ("takwas", "eight"), ("tara", "nine"), ("goma", "ten"),
                ("ashirin", "twenty"), ("dari", "hundred"), ("dubu", "thousand"),
                ("yau", "today"), ("jiya", "yesterday"), ("gobe", "tomorrow"),
                ("yanzu", "now"), ("kullum", "daily"), ("da safe", "in the morning"),
                ("da dare", "at night"), ("sosai", "very"), ("kadan", "a little"),
                ("da sauri", "quickly"), ("a hankali", "slowly"), ("tare", "together"),
                ("sannu", "hello"), ("na gode", "thank you"), ("don Allah", "please"),
                ("yi hakuri", "excuse me"), ("sannu da zuwa", "welcome"),
                ("sai an jima", "see you soon"), ("lafiya lau", "fine"),
                ("kwarai", "truly"), ("kuma", "also"), ("amma", "but"),
                ("saboda", "because"), ("idan", "if"), ("da", "and"),
                ("ko", "or"), ("sannan", "then"), ("in Allah ya so", "God willing"),
                ("alhamdulillah", "praise God"), ("to", "OK"), ("i", "yes"),
                ("a'a", "no"), ("girmama", "respect"), ("albarka", "blessing"),
                ("hira", "chat"), ("shawara", "advice"), ("tafiya", "journey"),
                ("aure", "marriage"), ("sana'a", "trade"),
            ],
            "grammar_rules": 10,
            "phrase_tables": 5,
        },
    }
)
