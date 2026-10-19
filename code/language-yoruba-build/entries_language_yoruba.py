#!/usr/bin/env python3
"""Entries for the Yoruba to English databases (Manon's language project, 2026-10-17).

Verified 2026-10-17: RAW SWEEP over the full manifest PLUS every shard index
title in jah-databases-data-1: zero 'language-yoruba*' slugs. ID prefixes
JAH-LYOR- (public) and JAH-LYORS- (signature) verified free in the manifest
id_prefix values AND in every shard index (zero zgrep hits for 'JAH-LYOR'
across all index.jsonl.gz files). Pre-authoring whole-system dedupe-gate
check over all 68 planned titles (34 records + 34 Signature Edition titles):
zero collisions, zero refusals.

This build creates two NEW databases, 34 ladder-ordered records each:

  language-yoruba              - The Yoruba to English Database
                                (public-harvest: real, fact-checked Yoruba -
                                overview, the Latin writing system with tone
                                marks, phonology and the three tones, core
                                vocabulary with sentences, grammar essentials,
                                themed sentence sets, the aspect-marker verb
                                system, questions and answers, commands,
                                descriptions, stories, idioms and proverbs,
                                registers, complex sentences, conversations,
                                mastery reference; standard references
                                Abraham 1958, Bamgbose 1966, Awobuluyi 1978,
                                Rowlands 1969, ISO 639 yo/yor)
  language-yoruba-signature   - The Yoruba to English Signature Database
                                (his original Signature Language Method:
                                every letter a sworn mark, every tone a sealed
                                vow, every sentence a covenant of meaning;
                                src signature, titles suffixed
                                " (Signature Edition)", clearly labeled
                                Signature-made, never presented as authentic
                                public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record carries Yoruba content with English translation + example
sentences. Sentences are required in EVERY record - no vocabulary-list-only
records. Example sentences are constructed teaching examples in standard
Yoruba; documented linguistic facts (alphabet, tones, numbers, grammar
rules, proverbs) are fact-checked public-harvest.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_yoruba.py). Every demo prints its real computed
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

CIT_ABRAHAM = ("Abraham RC. Dictionary of Modern Yoruba. University of "
               "London Press; 1958.")
CIT_BAMGBOSE = ("Bamgbose A. A Grammar of Yoruba. Cambridge University "
                "Press; 1966.")
CIT_AWOBULUYI = ("Awobuluyi O. Essentials of Yoruba Grammar. Oxford "
                 "University Press; 1978.")
CIT_ROWLANDS = ("Rowlands EC. Teach Yourself Yoruba. English Universities "
                "Press; 1969.")
CIT_ISO = ("ISO 639: Yoruba is coded yo (ISO 639-1) and yor (ISO 639-3); "
           "standard Yoruba is based on the Oyo and Ibadan dialects.")

# The Yoruba alphabet (25 letters; gb is one letter, the digraph).
# (letter, sound note)
YORUBA_ALPHA = [
    ("a", "a as in father"), ("b", "b as in boy"), ("d", "d as in dog"),
    ("e", "e as in they (close e)"), ("ẹ", "open e, as in bet"),
    ("f", "f as in fan"), ("g", "g as in go"),
    ("gb", "labial-velar: g and b struck together"),
    ("h", "h as in hat"), ("i", "i as in machine"),
    ("j", "j as in joy"), ("k", "k as in kite"),
    ("l", "l as in love"), ("m", "m as in man"), ("n", "n as in name"),
    ("o", "o as in go (close o)"), ("ọ", "open o, as in law"),
    ("p", "p as in pen"), ("r", "tapped r"), ("s", "s as in sun"),
    ("ṣ", "sh as in ship"), ("t", "t as in top"), ("u", "u as in moon"),
    ("w", "w as in water"), ("y", "y as in yes"),
]
SPECIALS = ["ẹ", "ọ", "ṣ"]
VOWELS_ORAL = ["a", "e", "ẹ", "i", "o", "ọ", "u"]
VOWELS_NASAL = ["an", "ẹn", "in", "ọn", "un"]
MISSING_NATIVE = ["c", "q", "v", "x", "z"]
TONES = ["high", "mid", "low"]


def _alpha_lines():
    return "\n".join("  %s  - %s" % (ch, note) for ch, note in YORUBA_ALPHA)


ENTRIES = [
    {
        "key": "overview",
        "name": "Yoruba Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Yoruba (èdè Yorùbá, the language of the Yoruba people) is a "
            "Volta-Niger language of the Niger-Congo family, the great "
            "language family of sub-Saharan Africa. It carries ISO codes yo "
            "(ISO 639-1) and yor (ISO 639-3), and is one of the largest "
            "African languages by native speakers: about 46 million people "
            "speak it as a mother tongue, with total users higher when "
            "second-language speakers and the diaspora are counted. \n\n"
            "Where it is spoken. The heartland is southwestern Nigeria - "
            "Lagos (Èkó), Oyo (Ọ̀yọ́), Ogun, Ondo, Osun, Ekiti, Kwara - "
            "with large communities in the Republic of Benin and Togo, and "
            "a wide diaspora in Britain, the United States, and Canada. "
            "Yoruba heritage speech also lives on in the Americas: Lucumí "
            "in Cuba and the Yoruba of Candomblé in Brazil carry the "
            "language's tones across the Atlantic. \n\n"
            "Official status. Yoruba is one of Nigeria's three major "
            "national languages, alongside Hausa and Igbo, and a national "
            "language of Benin. \n\n"
            "Dialects. Standard Yoruba is based on the Oyo and Ibadan "
            "dialects - the speech of school, radio, and print. Other major "
            "dialects are Egba, Ijebu, Ondo, Ekiti, Ijesa, Ife, Akoko, Owo, "
            "Ikale, Ilaje, Awori, Yagba, and Igbomina; they are mutually "
            "intelligible with the standard with small adjustments. Close "
            "sister languages are Itsekiri and Igala. \n\n"
            "History in one breath. The Yoruba city-states - Ife, Oyo, "
            "Ijebu, Egba - built bronze, terracotta, and cavalry empires "
            "centuries before European contact; the Oyo Empire at its height "
            "ruled from the savanna to the coast; missionaries and scholars "
            "of the 1800s, chief among them Bishop Samuel Ajayi Crowther, "
            "gave the language its Latin orthography; and the 1960s "
            "grammarians fixed the standard taught in schools today. \n\n"
            "What makes Yoruba learnable. The script is Latin with a few "
            "extra marks, the word order is the familiar subject-verb-"
            "object, there is no grammatical gender and no noun cases - and "
            "verbs never conjugate: time and aspect ride on small markers "
            "like ń (is doing), ti (has done), and máa (will do). Learn the "
            "markers, learn the three tones, and the language opens like a "
            "door. \n\n"
            "First sentences in èdè Yorùbá:\n"
            "  Ẹ káàárọ̀! - Good morning!\n"
            "  Orúkọ mi ni Manon. - My name is Manon.\n"
            "  Mo nífẹ̀ẹ́ èdè Yorùbá. - I love the Yoruba language.\n"
            "  Mo ti bẹ̀rẹ̀ sí í kọ́ Yorùbá lónìí. - I have started learning "
            "Yoruba today."
        ),
        "how_it_works": (
            "This record is the map of the whole database. It fixes the "
            "identity of the language - name (èdè Yorùbá), codes (yo / yor), "
            "family (Niger-Congo, Volta-Niger), speaker scale (about 46 "
            "million native), territory (southwestern Nigeria, Benin, Togo, "
            "diaspora), official standing (national language in Nigeria and "
            "Benin), dialect landscape (Oyo/Ibadan standard; Egba, Ijebu, "
            "Ondo, Ekiti, Ijesa, Ife, Akoko, Owo, Ikale, Ilaje, Awori, "
            "Yagba, Igbomina), and the historical arc (Ife and Oyo "
            "city-states, Crowther's 19th-century orthography, the 1960s "
            "standard). Every later record hangs facts on this frame: the "
            "alphabet record spells the 25 letters, the phonology record "
            "sounds the three tones, the vocabulary records fill the "
            "word-hoard, and the grammar records assemble the engine. Work "
            "through the ladder in order and each record assumes only what "
            "earlier records taught."
        ),
        "key_points": [
            "Native name: èdè Yorùbá; ISO 639-1 yo, ISO 639-3 yor.",
            "Family: Niger-Congo, Volta-Niger branch.",
            "About 46 million native speakers; national language in Nigeria and Benin.",
            "Standard Yoruba is based on the Oyo and Ibadan dialects.",
            "Sister languages: Itsekiri and Igala; heritage speech in Cuba (Lucumí) and Brazil (Candomblé).",
            "SVO word order; verbs never conjugate - aspect markers ń, ti, máa carry time.",
            "Three tones - high, mid, low - are part of every word.",
        ],
        "requirements": [
            "No prior knowledge of any African language is assumed.",
            "Read the alphabet record before the phonology record; read the phonology record before the vocabulary records.",
        ],
        "standards": [
            "Speaker figures are rounded public estimates (Ethnologue-style reporting); the record states them as approximate.",
            "Dialect and history claims follow the standard references: Abraham 1958, Bamgbose 1966, Awobuluyi 1978.",
            "All example sentences are glossed word-for-word where the grammar is new.",
        ],
        "citations": [CIT_ABRAHAM, CIT_BAMGBOSE, CIT_AWOBULUYI, CIT_ISO],
        "must_contain": ["èdè Yorùbá", "yo", "yor", "Volta-Niger", "46 million", "Crowther"],
        "sig_lens": (
            "Through the Signature lens this overview is a census of a "
            "living nation of speakers: every headcount a sworn roll-call, "
            "every dialect a branch of one family tree, every city-state a "
            "seal on the covenant that this language will be carried whole "
            "into the archive."
        ),
        "drill": {
            "native_m": 46.0, "iso1": "yo", "iso3": "yor",
            "national_countries": 2,
            "dialects": ["Oyo", "Ibadan", "Egba", "Ijebu", "Ondo", "Ekiti",
                         "Ijesa", "Ife", "Akoko", "Owo", "Ikale", "Ilaje",
                         "Awori", "Yagba", "Igbomina"],
            "regions": ["Nigeria", "Benin", "Togo", "Britain",
                        "United States", "Canada"],
            "sisters": ["Itsekiri", "Igala"],
            "tones": TONES,
        },
    },
    {
        "key": "writing",
        "name": "The Yoruba Writing System",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Yoruba is written in a Latin alphabet of 25 letters, "
            "standardized in the 1800s and fixed in its modern form by the "
            "1960s grammarians. It runs left-to-right, is phonetic (one "
            "letter, one sound), and uses Arabic numerals 0-9 with "
            "English-style punctuation. \n\n"
            "The alphabet, letter by letter:\n"
            + _alpha_lines() + "\n\n"
            "The three dotted letters are the signature of written Yoruba: "
            "ẹ and ọ are the open vowels (ẹ as in bet, ọ as in law), and ṣ "
            "is the sh sound. The digraph gb counts as ONE letter - a "
            "labial-velar stop, g and b struck at the same instant, as in "
            "gbà (take/receive) and gbọ́ (hear). There is no c, q, v, x, or "
            "z in native Yoruba words; foreign words are respelled to fit "
            "the alphabet. \n\n"
            "Tone marks. High tone takes the acute (á), low tone the grave "
            "(à), and mid tone is left unmarked - so every written vowel "
            "carries its melody or its silence. Nasal vowels are written "
            "with a following n: an, ẹn, in, ọn, un (as in dán - to shine, "
            "as in fún (to give), with nasal u). A syllabic n "
            "stands alone as its own syllable and takes a tone mark: ń, ǹ. "
            "\n\n"
            "Read and write these first words:\n"
            "  ilé - house\n"
            "  omi - water\n"
            "  ọmọ - child\n"
            "  ẹja - fish\n"
            "  gbàdúrà - prayer\n"
            "  ṣe - to do"
        ),
        "how_it_works": (
            "The Yoruba alphabet works by direct sound-to-letter mapping: "
            "learn the 25 letters (24 single letters plus the digraph gb), "
            "learn the three dotted specials ẹ ọ ṣ, and you can read any "
            "Yoruba word aloud. Because the script is phonetic, spelling "
            "drills double as pronunciation drills. Tone marks appear in "
            "teaching texts, dictionaries, and this database; newspapers and "
            "schoolbooks often leave them off, and readers supply the tones "
            "from the word itself. Write the tone marks while you learn - "
            "they are the difference between one word and another."
        ),
        "key_points": [
            "Latin alphabet of 25 letters, written left-to-right, fully phonetic.",
            "Dotted specials: ẹ (open e), ọ (open o), ṣ (sh).",
            "gb is one letter: a labial-velar stop, g and b together.",
            "No c, q, v, x, z in native words; Arabic numerals 0-9.",
            "Tone marks: acute for high (á), grave for low (à), mid unmarked.",
            "Nasal vowels written with n: an, ẹn, in, ọn, un; syllabic ń/ǹ stands alone.",
        ],
        "requirements": [
            "Practice handwriting or typing ẹ, ọ, ṣ until they are automatic.",
            "Read the letter table aloud top to bottom before moving to the phonology record.",
        ],
        "standards": [
            "Letter inventory follows the standard Yoruba orthography (Abraham 1958; Awobuluyi 1978).",
            "Tone-marking conventions follow the teaching-text standard used in Yoruba grammars.",
        ],
        "citations": [CIT_ABRAHAM, CIT_AWOBULUYI, CIT_ISO],
        "must_contain": ["25 letters", "ẹ", "ọ", "ṣ", "gb", "left-to-right", "acute"],
        "sig_lens": (
            "Through the Signature lens the Yoruba alphabet is a sworn set "
            "of marks: each dotted letter a seal pressed into the page, gb "
            "a double vow struck as one, every tone mark a pitch sworn onto "
            "its vowel."
        ),
        "drill": {
            "letters": [ch for ch, _ in YORUBA_ALPHA],
            "specials": SPECIALS,
            "digraphs": ["gb"],
            "missing_native": MISSING_NATIVE,
            "vowels_oral": VOWELS_ORAL,
            "vowels_nasal": VOWELS_NASAL,
            "direction": "left-to-right",
            "test_words": ["ilé", "omi", "ọmọ", "ẹja", "gbàdúrà"],
        },
    },
    {
        "key": "phonology",
        "name": "Yoruba Pronunciation and Phonology",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Yoruba pronunciation rests on three pillars: seven oral vowels "
            "in open/close pairs, a consonant set with the labial-velar gb, "
            "and THREE tones - high, mid, and low - that can change a word's "
            "meaning. The rhythm is syllable-timed: every syllable gets its "
            "full weight, with no English-style stress squash. \n\n"
            "Vowels. Seven oral vowels: a, e, ẹ, i, o, ọ, u. The pairs "
            "e/ẹ and o/ọ are close/open partners - e as in they, ẹ as in "
            "bet; o as in go, ọ as in law. Five nasal vowels - an, ẹn, in, "
            "ọn, un - hum through the nose. Vowels do not come in "
            "short/long pairs; length is not contrastive. \n\n"
            "Consonants. Eighteen consonants, nearly all familiar to "
            "English ears, with two to master: gb (labial-velar, g and b "
            "together, as in gbọ́ - hear) and its voiceless partner kp, "
            "plus ṣ (sh) and the tapped r. There are NO consonant clusters "
            "and no closed syllables: every syllable is an open (C)V, or a "
            "syllabic nasal. \n\n"
            "Tone. High (marked á), mid (unmarked a), and low (marked à). "
            "Tone is part of the word, and grammar rides on it too. The "
            "classic trio every learner meets first:\n"
            "  igbá (high-high) - calabash\n"
            "  igba (mid-mid) - two hundred\n"
            "  ìgbà (low-low) - time, season, occasion\n"
            "Grammar rides on tone as well: ó lọ (he went) and o lọ (you "
            "went) differ by tone alone. \n\n"
            "Sound it out - ten spoken-example words:\n"
            "  ilé - house\n"
            "  ìlú - town\n"
            "  omi - water\n"
            "  ọmọ - child\n"
            "  obìnrin - woman\n"
            "  ọkùnrin - man\n"
            "  bàbá - father\n"
            "  ìyá - mother\n"
            "  ọjà - market\n"
            "  owó - money"
        ),
        "how_it_works": (
            "Yoruba phonology works as a three-way contract between vowel "
            "quality, consonant shape, and pitch. Vowel pairs e/ẹ and o/ọ "
            "split the mouth into close and open rooms; gb and kp fuse two "
            "places of articulation into one strike; and the three tones "
            "paint meaning onto every syllable. Because syllables are "
            "always open, words flow as clean vowel-ended beats - i-lé, "
            "ọ-mọ, o-bìn-rin. Train the ear on the igbá/igba/ìgbà trio "
            "until the three melodies feel like three different words, "
            "because they are. Tone deafness is the beginner's tax; every "
            "record after this one assumes the tones are heard."
        ),
        "key_points": [
            "Seven oral vowels (a e ẹ i o ọ u) plus five nasal vowels (an ẹn in ọn un).",
            "Eighteen consonants including labial-velar gb and kp; no clusters, no closed syllables.",
            "Three tones - high, mid, low - are lexical: igbá (calabash), igba (two hundred), ìgbà (time).",
            "Syllable-timed rhythm; syllables are open (C)V or syllabic nasal.",
            "Tone also carries grammar: ó lọ (he went) vs o lọ (you went).",
        ],
        "requirements": [
            "Say the igbá/igba/ìgbà trio aloud until the three tones are distinct.",
            "Read the ten example words aloud before starting the vocabulary records.",
        ],
        "standards": [
            "Vowel and consonant inventory follows Bamgbose 1966 and Awobuluyi 1978.",
            "Tone analysis follows the standard three-tone account of Yoruba.",
        ],
        "citations": [CIT_BAMGBOSE, CIT_AWOBULUYI, CIT_ROWLANDS],
        "must_contain": ["igbá", "igba", "ìgbà", "seven oral vowels", "labial-velar", "high, mid, and low"],
        "sig_lens": (
            "Through the Signature lens the three tones are three sworn "
            "pitches: high a lifted seal, mid a steady hand, low a deep "
            "vow - and the igbá trio proves one melody can carry three "
            "worlds."
        ),
        "drill": {
            "vowels_oral": VOWELS_ORAL,
            "vowels_nasal": VOWELS_NASAL,
            "consonants": 18,
            "tones": TONES,
            "specials": ["gb", "kp", "ṣ"],
            "tone_trio": [("igbá", "calabash", "high-high"),
                          ("igba", "two hundred", "mid-mid"),
                          ("ìgbà", "time, season", "low-low")],
            "example_words": ["ilé", "ìlú", "omi", "ọmọ", "obìnrin",
                              "ọkùnrin", "bàbá", "ìyá", "ọjà", "owó"],
        },
    },
]

ENTRIES += [
    {
        "key": "nouns",
        "name": "Core Yoruba Nouns I",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "compounded",
        "description": (
            "Twenty-five essential Yoruba nouns - people, places, and "
            "things - each with an example sentence and its English "
            "translation. Yoruba nouns have no gender, no cases, and no "
            "plural endings: one form serves singular and plural, and "
            "number is shown by context or by àwọn (those). Nouns stand "
            "bare where English needs a or the; definiteness comes from "
            "context or from demonstratives (covered in the pronouns "
            "record). \n\n"
            "People:\n"
            "  ọmọ - child. Ọmọ náà ń sáré. - The child is running.\n"
            "  obìnrin - woman. Obìnrin náà ń ta ẹja. - The woman is selling fish.\n"
            "  ọkùnrin - man. Ọkùnrin náà ń ṣiṣẹ́. - The man is working.\n"
            "  bàbá - father. Bàbá mi wà ní ilé. - My father is at home.\n"
            "  ìyá - mother. Ìyá mi ń se oúnjẹ. - My mother is cooking food.\n"
            "  ọ̀rẹ́ - friend. Ọ̀rẹ́ mi dé. - My friend has arrived.\n"
            "  olùkọ́ - teacher. Olùkọ́ náà ń kọ́ wa. - The teacher is teaching us.\n"
            "  akẹ́kọ̀ọ́ - student. Akẹ́kọ̀ọ́ náà ń kàwé. - The student is reading.\n"
            "Places:\n"
            "  ilé - house. Ilé wa tóbi. - Our house is big.\n"
            "  ilé-ìwé - school. Mo lọ sí ilé-ìwé. - I went to school.\n"
            "  ọjà - market. Ọjà kún fún ènìyàn. - The market is full of people.\n"
            "  ìlú - town. Ìlú wa lẹ́wà. - Our town is beautiful.\n"
            "  ọ̀nà - road. Ọ̀nà náà gùn. - The road is long.\n"
            "  ilẹ̀ - land, ground. Ilẹ̀ náà tútù. - The ground is wet.\n"
            "  ọ̀run - sky, heaven. Ẹyẹ ń fò lọ́run. - Birds fly in the sky.\n"
            "Things:\n"
            "  omi - water. Mu omi. - Drink water.\n"
            "  oúnjẹ - food. Oúnjẹ dùn. - The food is tasty.\n"
            "  ìwé - book. Ìwé náà wà lórí tábìlì. - The book is on the table.\n"
            "  owó - money. Mo ní owó. - I have money.\n"
            "  aṣọ - cloth. Aṣọ tuntun lẹ́wà. - New cloth is beautiful.\n"
            "  ọkọ̀ - vehicle. Ọkọ̀ náà dé. - The vehicle has arrived.\n"
            "  iná - fire, light. Iná ń jóná. - The fire is burning.\n"
            "  igi - tree. Igi náà ga. - The tree is tall.\n"
            "  ẹja - fish. Ẹja náà tutu. - The fish is fresh (cold).\n"
            "  ajá - dog. Ajá náà ń gbó. - The dog is barking."
        ),
        "how_it_works": (
            "Yoruba nouns work by position, not by endings. A noun is the "
            "subject when it stands before the verb (Ajá ń gbó - the dog is "
            "barking) and the object when it stands after it (Mo rí ajá - I "
            "saw a dog). One form covers singular and plural: ọmọ can be a "
            "child or children, and àwọn ọmọ (those children) pins it to "
            "plural when it matters. Adjectives follow the noun (ilé ńlá - "
            "big house), possessors follow the noun (ilé mi - my house), "
            "and the noun never changes shape for any of it. Learn the "
            "noun with its tone melody - ọmọ, ilé, ọjà - and the rest of "
            "the grammar arranges itself around it."
        ),
        "key_points": [
            "No gender, no cases, no plural endings on Yoruba nouns.",
            "One form serves singular and plural; àwọn marks plural when needed.",
            "No articles: nouns stand bare; definiteness comes from context.",
            "Adjectives and possessors follow the noun: ilé ńlá, ilé mi.",
            "Subject/object roles are shown by position (SVO), not by form.",
        ],
        "requirements": [
            "Say each noun with its tone melody until the tones are automatic.",
            "Build one sentence of your own for each of the 25 nouns.",
        ],
        "standards": [
            "Noun forms and tones follow Abraham 1958.",
            "Example sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_ABRAHAM, CIT_BAMGBOSE],
        "must_contain": ["Twenty-five", "àwọn", "no gender", "Ajá", "ajá"],
        "sig_lens": (
            "Through the Signature lens each noun is a sworn name: one "
            "unchanging mark for one thing, singular and plural in a "
            "single seal, position alone declaring its office in the "
            "sentence."
        ),
        "drill": {
            "nouns": ["ọmọ", "obìnrin", "ọkùnrin", "bàbá", "ìyá", "ọ̀rẹ́",
                      "olùkọ́", "akẹ́kọ̀ọ́", "ilé", "ilé-ìwé", "ọjà", "ìlú",
                      "ọ̀nà", "ilẹ̀", "ọ̀run", "omi", "oúnjẹ", "ìwé", "owó",
                      "aṣọ", "ọkọ̀", "iná", "igi", "ẹja", "ajá"],
            "groups": {"people": 8, "places": 7, "things": 10},
            "plural_marker": "àwọn",
        },
    },
    {
        "key": "verbs",
        "name": "Core Yoruba Verbs I",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "compounded",
        "description": (
            "Twenty-five essential Yoruba verbs, each with an example "
            "sentence and its English translation. Yoruba verbs NEVER "
            "conjugate: lọ is go, goes, went, and will go - the aspect "
            "markers ń, ti, and máa (covered in the tenses record) carry "
            "the time. Most verbs are one syllable, and many pair into "
            "serial chains: ó mú ìwé wá (he took-book came = he brought a "
            "book). \n\n"
            "Motion:\n"
            "  lọ - go. Mo lọ sí ọjà. - I went to the market.\n"
            "  wá - come. Wá síbí. - Come here.\n"
            "  rìn - walk. Wọ́n ń rìn lọ sí ilé-ìwé. - They are walking to school.\n"
            "  sáré - run. Ọmọ náà sáré. - The child ran.\n"
            "  dúró - stand, stop. Dúró níbẹ̀. - Stand there.\n"
            "  jókòó - sit. Jókòó lórí àga. - Sit on the chair.\n"
            "Body and daily life:\n"
            "  jẹ - eat. Mo fẹ́ jẹ ìrẹsì. - I want to eat rice.\n"
            "  mu - drink. Mu omi púpọ̀. - Drink plenty of water.\n"
            "  sùn - sleep. Ọmọ náà ń sùn. - The child is sleeping.\n"
            "  jí - wake. Jí ní òwúrọ̀. - Wake up in the morning.\n"
            "  wẹ̀ - bathe. Mo ti wẹ̀. - I have bathed.\n"
            "  ṣiṣẹ́ - work. Ó ń ṣiṣẹ́ ní ọ́fíìsì. - He is working at the office.\n"
            "Mind and speech:\n"
            "  rí - see. Mo rí i. - I saw it.\n"
            "  gbọ́ - hear, understand. Mo gbọ́ ohun tí o sọ. - I heard what you said.\n"
            "  sọ - say. Sọ fún mi. - Tell me.\n"
            "  mọ̀ - know. Mo mọ̀ ọ. - I know him.\n"
            "  fẹ́ - want, love. Mo nífẹ̀ẹ́ rẹ̀. - I love you.\n"
            "  béèrè - ask. Béèrè lọ́wọ́ olùkọ́. - Ask the teacher.\n"
            "  dáhùn - answer. Dáhùn ìbéèrè náà. - Answer the question.\n"
            "  kọ́ - teach. Ó ń kọ́ wa ní Yorùbá. - He is teaching us Yoruba.\n"
            "  kà - read, count. Mo ń kà ìwé. - I am reading a book.\n"
            "  kọ - write. Kọ orúkọ rẹ. - Write your name.\n"
            "Hands and exchange:\n"
            "  rà - buy. Mo rà aṣọ. - I bought cloth.\n"
            "  tà - sell. Ó ń tà ẹja. - She is selling fish.\n"
            "  fún - give. Fún mi ní omi. - Give me water."
        ),
        "how_it_works": (
            "Yoruba verbs work as bare roots: the verb never changes shape, "
            "and small markers before it set the time - ó lọ (he went), ó ń "
            "lọ (he is going), ó ti lọ (he has gone), ó máa lọ (he will "
            "go). Objects follow the verb directly (rà aṣọ - buy cloth), "
            "and verbs chain without any and: ó mú ìwé wá (he brought a "
            "book), ó lọ rà á (he went to buy it). Negation stands before "
            "the verb: kò lọ (he did not go). Learn the verb root with its "
            "tone - lọ, wá, jẹ, rí - and one marker at a time; the whole "
            "tense system in the tenses record is built from these roots."
        ),
        "key_points": [
            "Verbs never conjugate; aspect markers ń, ti, máa carry time.",
            "Most verbs are one syllable: lọ, wá, jẹ, rí, kọ.",
            "Objects follow the verb directly: rà aṣọ.",
            "Serial verb chains need no conjunction: ó mú ìwé wá.",
            "Negation stands before the verb: kò lọ.",
        ],
        "requirements": [
            "Drill each verb with the four markers: lọ, ń lọ, ti lọ, máa lọ.",
            "Chain two verbs in one sentence of your own.",
        ],
        "standards": [
            "Verb roots and tones follow Abraham 1958.",
            "Serial-verb analysis follows Bamgbose 1966.",
        ],
        "citations": [CIT_ABRAHAM, CIT_BAMGBOSE, CIT_AWOBULUYI],
        "must_contain": ["NEVER conjugate", "ó mú ìwé wá", "ń, ti, and máa", "Twenty-five"],
        "sig_lens": (
            "Through the Signature lens each verb is an unchanging seal of "
            "action: the root never bends, the markers are sworn riders "
            "that carry it through time, and chained verbs march as one "
            "covenant of doing."
        ),
        "drill": {
            "verbs": ["lọ", "wá", "rìn", "sáré", "dúró", "jókòó", "jẹ",
                      "mu", "sùn", "jí", "wẹ̀", "ṣiṣẹ́", "rí", "gbọ́", "sọ",
                      "mọ̀", "fẹ́", "béèrè", "dáhùn", "kọ́", "kà", "kọ",
                      "rà", "tà", "fún"],
            "markers": ["ń", "ti", "máa"],
            "serial_example": "ó mú ìwé wá",
        },
    },
    {
        "key": "adjectives",
        "name": "Yoruba Adjectives and Adverbs",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Twenty-five adjectives and fifteen adverbs with example "
            "sentences. Yoruba adjectives FOLLOW the noun and never change "
            "for gender or number: ilé ńlá (big house), ilé ńláńlá (very "
            "big houses - reduplication intensifies). Many adjectives are "
            "verbs in disguise - dùn (be tasty), ga (be tall), lẹ́wà (be "
            "beautiful) - and take the verbal markers: ó dùn (it is "
            "tasty). \n\n"
            "Adjectives (noun first, then the adjective):\n"
            "  ńlá - big. Ilé ńlá ni. - It is a big house.\n"
            "  kékeré - small. Ọmọ kékeré ń sùn. - The small child is sleeping.\n"
            "  gíga - tall, high. Igi gíga wà níbẹ̀. - A tall tree is there.\n"
            "  kúrú - short. Ọ̀nà kúrú ni. - It is a short road.\n"
            "  tuntun - new. Mo rà aṣọ tuntun. - I bought new cloth.\n"
            "  àtijọ́ - old (things). Ìwé àtijọ́ ni. - It is an old book.\n"
            "  pupa - red. Aṣọ pupa lẹ́wà. - Red cloth is beautiful.\n"
            "  funfun - white. Ilé funfun ga. - The white house is tall.\n"
            "  dúdú - black. Ajá dúdú ń gbó. - The black dog is barking.\n"
            "  dídùn - tasty, sweet. Oúnjẹ dídùn dùn. - Tasty food is sweet.\n"
            "  tútù - cold, fresh. Omi tútù dùn mu. - Cold water is good to drink.\n"
            "  gbígbẹ - dry. Aṣọ gbígbẹ yára gbẹ. - Dry cloth dries fast.\n"
            "  lẹ́wà - beautiful. Obìnrin lẹ́wà dé. - A beautiful woman arrived.\n"
            "  ọlọ́gbọ́n - wise. Ọmọ ọlọ́gbọ́n mọ̀ ìwé. - A wise child knows books.\n"
            "  òmùgọ̀ - foolish. Ìwà òmùgọ̀ ò dára. - Foolish behavior is not good.\n"
            "  ṣòro - difficult. Iṣẹ́ ṣòro wà. - Difficult work exists.\n"
            "  rọrùn - easy. Èdè Yorùbá rọrùn. - Yoruba is easy.\n"
            "  yára - fast. Ọkọ̀ yára dé. - The fast vehicle arrived.\n"
            "  lọ́ra - slow. Ìrìn lọ́ra sàn. - Slow walking is healthier.\n"
            "  púpọ̀ - many, much. Ènìyàn púpọ̀ wà ní ọjà. - Many people are at the market.\n"
            "  díẹ̀ - few, little. Omi díẹ̀ kù. - A little water remains.\n"
            "  gbogbo - all, every. Gbogbo ọmọ dé. - Every child arrived.\n"
            "  mímọ́ - clean, holy. Ilé mímọ́ dùn mí. - A clean house pleases me.\n"
            "  rere - good. Ìwà rere sàn. - Good character is better.\n"
            "  burúkú - bad. Ìwà burúkú ò dára. - Bad behavior is not good.\n"
            "Adverbs (manner, time, place - usually after the verb):\n"
            "  dáradára - well. Ó ṣiṣẹ́ dáradára. - He works well.\n"
            "  kíákíá - quickly. Wá kíákíá. - Come quickly.\n"
            "  díẹ̀díẹ̀ - slowly, little by little. Rìn díẹ̀díẹ̀. - Walk slowly.\n"
            "  lọ́jọ́júmọ́ - daily. Mo ń kàwé lọ́jọ́júmọ́. - I read daily.\n"
            "  lónìí - today. Mo máa lọ lónìí. - I will go today.\n"
            "  lánàá - yesterday. Ó dé lánàá. - He arrived yesterday.\n"
            "  lọ́la - tomorrow. A máa pàdé lọ́la. - We shall meet tomorrow.\n"
            "  níbí - here. Jókòó níbí. - Sit here.\n"
            "  níbẹ̀ - there. Dúró níbẹ̀. - Stand there.\n"
            "  púpọ̀ - very, much. Mo nífẹ̀ẹ́ rẹ̀ púpọ̀. - I love you very much.\n"
            "  gan - truly, indeed. Ó dára gan. - It is truly good.\n"
            "  pátápátá - completely. Ó parẹ́ pátápátá. - It is completely finished.\n"
            "  tẹ́lẹ̀ - already, before. Mo ti rí i tẹ́lẹ̀. - I have seen it before.\n"
            "  síbẹ̀síbẹ̀ - still. Ó ń sùn síbẹ̀síbẹ̀. - He is still sleeping.\n"
            "  lẹ́ẹ̀kan - once. Mo lọ lẹ́ẹ̀kan. - I went once.\n"
            "Intensification by reduplication: ńlá -> ńláńlá (very big), "
            "pupa -> pupa gidigidi (very red). Reduplication "
            "is the native intensifier: kékeré -> kékerékékeré (very tiny)."
        ),
        "how_it_works": (
            "Yoruba adjectives work by following: the adjective stands "
            "after its noun and agrees with nothing - ilé ńlá, ọmọ ńlá, "
            "ilé ńláńlá (very big, by reduplication). Because many "
            "adjectives are stative verbs, they can also stand alone as "
            "predicates with verbal markers: ó dùn (it is tasty), ó ti ga "
            "(it has grown tall). Adverbs work by placement after the verb "
            "or at the sentence edge: wá kíákíá (come quickly), mo máa lọ "
            "lọ́la (I will go tomorrow). Reduplication - repeating the word "
            "with tone changes - is the built-in intensifier and pluralizer "
            "of the language."
        ),
        "key_points": [
            "Adjectives follow the noun: ilé ńlá, aṣọ pupa.",
            "No agreement for gender or number, ever.",
            "Many adjectives are stative verbs: ó dùn (it is tasty).",
            "Reduplication intensifies: ńlá -> ńláńlá (very big).",
            "Adverbs follow the verb or sit at the sentence edge.",
        ],
        "requirements": [
            "Pair each of the 25 adjectives with a noun from the nouns record.",
            "Use five adverbs in sentences of your own.",
        ],
        "standards": [
            "Adjective forms and reduplication patterns follow Awobuluyi 1978.",
            "Example sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_AWOBULUYI, CIT_BAMGBOSE],
        "must_contain": ["ńláńlá", "dáradára", "kíákíá", "Twenty-five adjectives", "fifteen adverbs", "pupa"],
        "sig_lens": (
            "Through the Signature lens the adjective is a sworn quality "
            "sealed after its noun, and reduplication is the seal stamped "
            "twice - ńláńlá, the vow of bigness doubled."
        ),
        "drill": {
            "adjectives": ["ńlá", "kékeré", "gíga", "kúrú", "tuntun",
                           "àtijọ́", "pupa", "funfun", "dúdú", "dídùn",
                           "tútù", "gbígbẹ", "lẹ́wà", "ọlọ́gbọ́n", "òmùgọ̀",
                           "ṣòro", "rọrùn", "yára", "lọ́ra", "púpọ̀", "díẹ̀",
                           "gbogbo", "mímọ́", "rere", "burúkú"],
            "adverbs": ["dáradára", "kíákíá", "díẹ̀díẹ̀", "lọ́jọ́júmọ́",
                        "lónìí", "lánàá", "lọ́la", "níbí", "níbẹ̀", "púpọ̀",
                        "gan", "pátápátá", "tẹ́lẹ̀", "síbẹ̀síbẹ̀", "lẹ́ẹ̀kan"],
            "intensified": {"ńlá": "ńláńlá", "kékeré": "kékerékékeré"},
        },
    },
    {
        "key": "pronouns",
        "name": "Yoruba Pronouns",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The full Yoruba pronoun paradigms - personal, possessive, "
            "demonstrative, interrogative - with example sentences. Tones "
            "do heavy work here: mo (I) vs ó (he/she), rẹ (your) vs rẹ̀ "
            "(his/her). \n\n"
            "Personal pronouns (subject - before the verb):\n"
            "  mo - I. Mo lọ. - I went.\n"
            "  o - you (singular). O lọ. - You went.\n"
            "  ó - he, she, it. Ó lọ. - He went.\n"
            "  a - we. A lọ. - We went.\n"
            "  ẹ - you (plural). Ẹ lọ. - You (all) went.\n"
            "  wọ́n - they. Wọ́n lọ. - They went.\n"
            "Emphatic/independent forms: èmi (I), ìwọ (you sg), òun (he/she), "
            "àwa (we), ẹ̀yin (you pl), àwọn (they). Èmi ni mo lọ. - It was I "
            "who went. \n\n"
            "Possessive pronouns (after the noun):\n"
            "  mi - my. Ilé mi. - My house.\n"
            "  rẹ - your (sg). Ilé rẹ. - Your house.\n"
            "  rẹ̀ - his, her, its. Ilé rẹ̀. - His house.\n"
            "  wa - our. Ilé wa. - Our house.\n"
            "  yín - your (pl). Ilé yín. - Your (all) house.\n"
            "  wọn - their. Ilé wọn. - Their house.\n"
            "The possessive set also serves as object pronouns: Mo rí ẹ. - "
            "I saw you. Ó fẹ́ wa. - He loves us. \n\n"
            "Demonstratives (after the noun):\n"
            "  yìí - this. Ìwé yìí. - This book.\n"
            "  yẹn - that. Ìwé yẹn. - That book.\n"
            "  wọ̀nyí - these. Àwọn ìwé wọ̀nyí. - These books.\n"
            "  wọ̀nyẹn - those. Àwọn ìwé wọ̀nyẹn. - Those books.\n"
            "Demonstrative sentences: Èyí ni ìwé mi. - This is my book. Ìyẹn "
            "ni ilé wa. - That is our house. \n\n"
            "Interrogatives:\n"
            "  ta - who. Ta ni? - Who is it?\n"
            "  kí - what. Kí ni èyí? - What is this?\n"
            "  níbo - where. Níbo ni ìwé mi wà? - Where is my book?\n"
            "  ìgbà wo - when. Ìgbà wo ni o dé? - When did you arrive?\n"
            "  èéṣe - why. Èéṣe tí o kò wá? - Why did you not come?\n"
            "  báwo - how. Báwo ni? - How are you?\n"
            "  mélòó - how many. Mélòó ni owó náà? - How much is the money?\n"
            "  èwo - which. Èwo ni o fẹ́? - Which do you want?\n"
            "Reflexive with ara (body, self): ara mi (myself), ara rẹ "
            "(yourself), ara rẹ̀ (himself/herself). Ó pa ara rẹ̀. - He "
            "killed himself. Mo ṣe é fún ara mi. - I did it for myself. \n\n"
            "Indefinites: ẹnìkan (someone), gbogbo (everyone/all), kò sí "
            "ẹnìkan (no one). Ẹnìkan wà níbẹ̀. - Someone is there."
        ),
        "how_it_works": (
            "Yoruba pronouns work as tonal minimal sets: mo/o/ó differ by "
            "tone alone, and rẹ/rẹ̀ split your/his by a single pitch step. "
            "Subject pronouns lock before the verb (mo lọ), possessives "
            "lock after the noun (ilé mi), and the possessive set doubles "
            "as objects (mo rí ẹ). Emphatic forms (èmi, ìwọ, òun) step "
            "forward for focus: èmi ni - it was I. Demonstratives follow "
            "the noun they point at (ìwé yìí), and interrogatives open "
            "questions, often with the focus ni: ta ni? (who is it?), kí ni "
            "èyí? (what is this?). There is no he/she split - ó covers "
            "both, and context decides."
        ),
        "key_points": [
            "Subject: mo, o, ó, a, ẹ, wọ́n - tone distinguishes I/you/he.",
            "Possessive: mi, rẹ, rẹ̀, wa, yín, wọn - follows the noun.",
            "Possessives double as object pronouns: mo rí ẹ.",
            "Emphatic: èmi, ìwọ, òun, àwa, ẹ̀yin, àwọn.",
            "Demonstratives follow the noun: ìwé yìí, ìwé yẹn.",
            "No he/she distinction: ó covers both.",
        ],
        "requirements": [
            "Drill the six subjects with one verb: mo lọ, o lọ, ó lọ, a lọ, ẹ lọ, wọ́n lọ.",
            "Pair each possessive with three nouns.",
        ],
        "standards": [
            "Pronoun paradigms follow Bamgbose 1966 and Awobuluyi 1978.",
            "Example sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_BAMGBOSE, CIT_AWOBULUYI],
        "must_contain": ["Mo lọ", "Ilé mi.", "Ìwé yìí.", "Ta ni?", "ara mi"],
        "sig_lens": (
            "Through the Signature lens the pronouns are six sworn voices: "
            "mo the vow of self, ó the vow of the other, wọ́n the vow of "
            "the many - each sealed by its tone."
        ),
        "drill": {
            "subject": ["mo", "o", "ó", "a", "ẹ", "wọ́n"],
            "possessive": ["mi", "rẹ", "rẹ̀", "wa", "yín", "wọn"],
            "emphatic": ["èmi", "ìwọ", "òun", "àwa", "ẹ̀yin", "àwọn"],
            "demonstrative": ["yìí", "yẹn", "wọ̀nyí", "wọ̀nyẹn"],
            "interrogative": ["ta", "kí", "níbo", "ìgbà wo", "èéṣe",
                              "báwo", "mélòó", "èwo"],
        },
    },
]

ENTRIES += [
    {
        "key": "numbers",
        "name": "Yoruba Numbers and Time",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Yoruba numbers 1-100, ordinals, days, months, seasons, clock "
            "time, and dates - each with example sentences. The Yoruba "
            "number system is vigesimal (base 20) with subtraction: 45 is "
            "márùúndínlọ́gbọ̀n (five-less-than-thirty), 95 is "
            "márùúndínlọ́gọ́rùn-ún (five-less-than-a-hundred). \n\n"
            "1-10: ọ̀kan (1), méjì (2), mẹ́ta (3), mẹ́rin (4), márùún (5), "
            "mẹ́fà (6), méje (7), mẹ́jọ (8), mẹ́sàán (9), mẹ́wàá (10).\n"
            "11-20: mọ́kànlá (11), méjìlá (12), mẹ́tàlá (13), mẹ́rìnlá (14), "
            "ẹẹ́dógún (15), ẹẹ́rìndínlógún (16), ẹẹ́tàdínlógún (17), "
            "ẹẹ́jìdínlógún (18), ọ̀kàndínlógún (19), ogún (20).\n"
            "Tens: ọgbọ̀n (30), ogójì (40, 20x2), àádọ́ta (50, 20x3-10), "
            "ọgọ́ta (60, 20x3), àádọ́rin (70, 20x4-10), ọgọ́rin (80, 20x4), "
            "àádọ́rùn-ún (90, 20x5-10), ọgọ́rùn-ún (100, 20x5).\n"
            "Bigger: igba (200), irinwó (400), ẹgbẹ̀rún (1,000).\n"
            "Subtraction examples: 25 = márùúndínlọ́gbọ̀n (5-less-than-30); "
            "35 = márùúndínlógójì (5-less-than-40); 45 = "
            "márùúndínláàádọ́ta (5-less-than-50); 95 = "
            "márùúndínlọ́gọ́rùn-ún (5-less-than-100).\n"
            "Count with sentences:\n"
            "  Mo ní ìwé méjì. - I have two books.\n"
            "  Ọmọ mẹ́ta wà níbẹ̀. - Three children are there.\n"
            "  Owó ogún ni. - It is twenty (units of) money.\n"
            "  Mo ra ẹja mẹ́wàá. - I bought ten fish.\n"
            "Ordinals (first, second, third...): ẹ̀kínní (1st), ẹ̀kejì "
            "(2nd), ẹ̀kẹta (3rd), ẹ̀kẹrin (4th), ẹ̀kàrún-ún (5th), ẹ̀kẹfà "
            "(6th), ẹ̀keje (7th), ẹ̀kẹjọ (8th), ẹ̀kẹ̀sán-án (9th), ẹ̀kẹwàá "
            "(10th).\n"
            "  Èmi ni ẹ̀kínní. - I am the first.\n"
            "  Ìwé ẹ̀kejì dùn. - The second book is interesting.\n"
            "Days of the week:\n"
            "  Ọjọ́ Àìkú - Sunday. A máa lọ sí ìjọ ní Ọjọ́ Àìkú. - We go to church on Sunday.\n"
            "  Ọjọ́ Ajé - Monday. Iṣẹ́ bẹ̀rẹ̀ ní Ọjọ́ Ajé. - Work starts on Monday.\n"
            "  Ọjọ́ Ìṣẹ́gun - Tuesday. Mo máa wá ní Ọjọ́ Ìṣẹ́gun. - I will come on Tuesday.\n"
            "  Ọjọ́rú - Wednesday. Ọjà ń kún ní Ọjọ́rú. - The market fills on Wednesday.\n"
            "  Ọjọ́bọ̀ - Thursday. A pàdé ní Ọjọ́bọ̀. - We met on Thursday.\n"
            "  Ọjọ́ Ẹtì - Friday. Ẹtì ọjọ́ ìsimi ni. - Friday is a rest day.\n"
            "  Ọjọ́ Àbámẹ́ta - Saturday. A ń ṣe ayẹyẹ ní Ọjọ́ Àbámẹ́ta. - We celebrate on Saturday.\n"
            "Months: Ṣẹ́rẹ́ (January), Èrèlè (February), Ẹrẹ̀nà (March), "
            "Ìgbé (April), Ẹ̀bibi (May), Òkúdu (June), Agẹmọ (July), Ògún "
            "(August), Owewe (September), Ọ̀wàrà (October), Bélú (November), "
            "Ọ̀pẹ́ (December).\n"
            "  Mo bí ní oṣù Ẹrẹ̀nà. - I was born in the month of March.\n"
            "Seasons: ìgbà òjò (rainy season), ìgbà ẹ̀ẹ̀rùn (dry season).\n"
            "  Òjò ń rọ̀ ní ìgbà òjò. - Rain falls in the rainy season.\n"
            "Clock time with àgogo (clock): Àgogo méje - 7 o'clock; àgogo "
            "méjìlá - 12 o'clock. Note the traditional offset: the Yoruba "
            "day-count starts at 6, so àgogo méje on the Yoruba clock is 1 "
            "o'clock English time.\n"
            "  Àgogo mẹ́fà ni. - It is 6 o'clock.\n"
            "  Mo máa dé ní àgogo méje. - I will arrive at 7 o'clock.\n"
            "Dates: Ọjọ́ kẹwàá oṣù Ṣẹ́rẹ́ - the 10th of January.\n"
            "  Ọjọ́ ìbí mi ni ọjọ́ kẹẹ̀dógún oṣù Òkúdu. - My birthday is the 15th of June."
        ),
        "how_it_works": (
            "Yoruba numbers work as arithmetic in words: the base is 20 "
            "(ogún), tens multiply it (ogójì = 20x2 = 40, ọgọ́ta = 20x3 = "
            "60), and dín (less-than) subtracts from the next round number "
            "(márùúndínlọ́gbọ̀n = 5-less-than-30 = 25). Addition glues with "
            "lé (on top): mọ́kànlá = 1-on-10 = 11. Ordinals prefix ẹ̀k- to "
            "the cardinal: ẹ̀kínní, ẹ̀kejì. Time words anchor with ní (on/at): "
            "ní Ọjọ́ Ajé (on Monday), ní àgogo méje (at 7 o'clock), ní oṣù "
            "Ṣẹ́rẹ́ (in January). The traditional clock counts from 6, so "
            "convert by subtracting six when an elder gives you the hour."
        ),
        "key_points": [
            "Vigesimal system: base 20 (ogún); 40 = ogójì (20x2), 100 = ọgọ́rùn-ún (20x5).",
            "Subtraction with dín: 25 = márùúndínlọ́gbọ̀n (5-less-than-30).",
            "Ordinals prefix ẹ̀k-: ẹ̀kínní (first), ẹ̀kejì (second).",
            "Seven day-names: Ọjọ́ Àìkú through Ọjọ́ Àbámẹ́ta.",
            "Twelve month-names: Ṣẹ́rẹ́ through Ọ̀pẹ́.",
            "Traditional clock counts from 6: àgogo méje = 1 o'clock English time.",
        ],
        "requirements": [
            "Count aloud 1-20, then 20-100 by tens.",
            "Say today's day, month, and the time in Yoruba.",
        ],
        "standards": [
            "Number forms follow Abraham 1958 and the standard Yoruba number system.",
            "Day and month names follow standard Yoruba usage.",
        ],
        "citations": [CIT_ABRAHAM, CIT_ROWLANDS],
        "must_contain": ["ogún", "márùúndínlọ́gbọ̀n", "ẹ̀kínní", "Ọjọ́ Àìkú", "Ṣẹ́rẹ́", "àgogo"],
        "sig_lens": (
            "Through the Signature lens the numbers are sworn arithmetic: "
            "twenty the great seal, dín the sworn subtraction, every count "
            "a covenant of exact measure."
        ),
        "drill": {
            "one_to_ten": ["ọ̀kan", "méjì", "mẹ́ta", "mẹ́rin", "márùún",
                           "mẹ́fà", "méje", "mẹ́jọ", "mẹ́sàán", "mẹ́wàá"],
            "tens": {"20": "ogún", "30": "ọgbọ̀n", "40": "ogójì",
                     "50": "àádọ́ta", "60": "ọgọ́ta", "70": "àádọ́rin",
                     "80": "ọgọ́rin", "90": "àádọ́rùn-ún", "100": "ọgọ́rùn-ún"},
            "ordinals": ["ẹ̀kínní", "ẹ̀kejì", "ẹ̀kẹta", "ẹ̀kẹrin", "ẹ̀kàrún-ún"],
            "days": ["Ọjọ́ Àìkú", "Ọjọ́ Ajé", "Ọjọ́ Ìṣẹ́gun", "Ọjọ́rú",
                     "Ọjọ́bọ̀", "Ọjọ́ Ẹtì", "Ọjọ́ Àbámẹ́ta"],
            "months": ["Ṣẹ́rẹ́", "Èrèlè", "Ẹrẹ̀nà", "Ìgbé", "Ẹ̀bibi", "Òkúdu",
                       "Agẹmọ", "Ògún", "Owewe", "Ọ̀wàrà", "Bélú", "Ọ̀pẹ́"],
            "seasons": ["ìgbà òjò", "ìgbà ẹ̀ẹ̀rùn"],
        },
    },
    {
        "key": "greetings",
        "name": "Yoruba Greetings and Everyday Phrases",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Thirty-one greetings, farewells, and politeness phrases - the "
            "famous Yoruba greeting system, where you greet the time of "
            "day AND the activity: ẹ ku iṣẹ́ to one who works, ẹ ku òjò in "
            "the rain. Use the ẹ-forms with elders and strangers; the "
            "bare forms with friends and juniors. \n\n"
            "Time-of-day greetings:\n"
            "  Ẹ káàárọ̀. - Good morning. (respectful; káàárọ̀ to friends)\n"
            "  Ẹ káàsán. - Good afternoon. (káàsán to friends)\n"
            "  Ẹ káalẹ́. - Good evening. (káalẹ́ to friends)\n"
            "Welcome and meeting:\n"
            "  Káàbọ̀. - Welcome. (ẹ káàbọ̀ respectful)\n"
            "  Ẹ káàbọ̀ sí ilé wa. - Welcome to our home.\n"
            "  Ó dára láti pàdé ẹ. - Nice to meet you.\n"
            "  Báwo ni? - How are you?\n"
            "  Báwo ni ẹ ṣe wà? - How are you? (respectful)\n"
            "  Ṣe aláàfíà ni? - Is it peace? (are you well?)\n"
            "  Aláàfíà ni. - It is peace. (I am well.)\n"
            "Activity greetings (the ẹ ku system):\n"
            "  Ẹ ku iṣẹ́. - Well done. (to one working)\n"
            "  Ẹ ku ìtajà. - Happy trading. (to a trader)\n"
            "  Ẹ ku ìkẹ́kọ̀ọ́. - Happy studying. (to a student)\n"
            "  Ẹ ku ìrìnàjò. - Welcome from the journey.\n"
            "  Ẹ ku ìsimi. - Enjoy your rest.\n"
            "  Ẹ ku ayẹyẹ. - Enjoy the celebration.\n"
            "  Ẹ ku ọdún. - Happy festival.\n"
            "  Ẹ ku òjò. - Greetings in the rain.\n"
            "  Ẹ ku oòrùn. - Greetings in the sun.\n"
            "  Ẹ ku ìbànújẹ́. - Accept my sympathy.\n"
            "Thanks and politeness:\n"
            "  Ẹ ṣeun. - Thank you. (o ṣe to friends)\n"
            "  Ẹ ṣeun púpọ̀. - Thank you very much.\n"
            "  Jọ̀wọ́. - Please. (ẹ jọ̀wọ́ respectful)\n"
            "  Ẹ dákun. - Please, I beg you.\n"
            "  Má bínú. - Don't be angry; sorry. (ẹ má bínú respectful)\n"
            "  Kò sí ọ̀ràn. - No problem.\n"
            "  Ó dára. - It is good; fine.\n"
            "Farewells:\n"
            "  Ó dàbọ̀. - Goodbye.\n"
            "  Ó di ọ̀la. - Until tomorrow.\n"
            "  Ó di òwúrọ̀. - Until morning."
        ),
        "how_it_works": (
            "Yoruba greetings work as social radar: the time-of-day set "
            "(káàárọ̀, káàsán, káalẹ́) opens every encounter, and the ẹ ku "
            "set salutes whatever the person is DOING - working, trading, "
            "resting, traveling, even standing in the rain. The ẹ- prefix "
            "is the respect switch: ẹ káàárọ̀ to an elder, káàárọ̀ to a "
            "friend; using the bare form upward is the classic learner's "
            "insult, so default to ẹ- with anyone older or unknown. "
            "Greetings are never skipped - to pass an elder without "
            "greeting is to declare yourself a stranger."
        ),
        "key_points": [
            "Greet the time of day: káàárọ̀, káàsán, káalẹ́.",
            "Greet the activity: ẹ ku iṣẹ́, ẹ ku ìtajà, ẹ ku ìsimi.",
            "The ẹ- prefix is the respect switch; default to it with elders.",
            "Báwo ni? / Ṣe aláàfíà ni? open the health check.",
            "Never skip greeting an elder.",
        ],
        "requirements": [
            "Greet three people in Yoruba today using the right ẹ-forms.",
            "Use one ẹ ku greeting matched to someone's activity.",
        ],
        "standards": [
            "Greeting forms follow standard Yoruba usage (Rowlands 1969).",
            "Usage notes reflect documented Yoruba greeting etiquette.",
        ],
        "citations": [CIT_ROWLANDS, CIT_ABRAHAM],
        "must_contain": ["Ẹ káàárọ̀", "ẹ ku iṣẹ́", "Ẹ ṣeun", "Ó dàbọ̀", "Báwo ni"],
        "sig_lens": (
            "Through the Signature lens every greeting is a sworn "
            "recognition: káàárọ̀ seals the morning, ẹ ku iṣẹ́ seals the "
            "labor, and no elder passes unsealed."
        ),
        "drill": {
            "time_greetings": ["Ẹ káàárọ̀", "Ẹ káàsán", "Ẹ káalẹ́"],
            "welcome": ["Káàbọ̀", "Ẹ káàbọ̀ sí ilé wa", "Ó dára láti pàdé ẹ",
                        "Báwo ni?", "Báwo ni ẹ ṣe wà?", "Ṣe aláàfíà ni?",
                        "Aláàfíà ni"],
            "activity_greetings": ["Ẹ ku iṣẹ́", "Ẹ ku ìtajà", "Ẹ ku ìkẹ́kọ̀ọ́",
                                   "Ẹ ku ìrìnàjò", "Ẹ ku ìsimi", "Ẹ ku ayẹyẹ",
                                   "Ẹ ku ọdún", "Ẹ ku òjò", "Ẹ ku oòrùn",
                                   "Ẹ ku ìbànújẹ́"],
            "thanks": ["Ẹ ṣeun", "Ẹ ṣeun púpọ̀"],
            "please": ["Jọ̀wọ́", "Ẹ jọ̀wọ́", "Ẹ dákun", "Má bínú", "Kò sí ọ̀ràn", "Ó dára"],
            "farewells": ["Ó dàbọ̀", "Ó di ọ̀la", "Ó di òwúrọ̀"],
            "count": 31,
        },
    },
    {
        "key": "grammar",
        "name": "Yoruba Grammar Essentials",
        "group": "Grammar Essentials",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The ten load-bearing rules of Yoruba grammar, each with "
            "translated example sentences. \n\n"
            "1. Word order is SVO. Mo ra ìwé. - I bought a book. Ó ń ka ìwé. "
            "- He is reading a book.\n"
            "2. No grammatical gender. Ó covers he, she, it: Ó lọ. - "
            "He/she went. Ọmọ náà dé. - The child arrived.\n"
            "3. No noun cases, no articles. Ilé - house, a house, the house. "
            "Mo rí ilé. - I saw a house.\n"
            "4. Number by context or àwọn. Ọmọ dé. - A child / children "
            "arrived. Àwọn ọmọ dé. - The children arrived.\n"
            "5. Adjectives follow nouns. Ilé ńlá. - Big house. Aṣọ pupa. - "
            "Red cloth.\n"
            "6. Verbal negation with kò. Ó lọ. - He went. Kò lọ. - He did "
            "not go. Mi ò lọ. - I did not go. Wọ́n ò wá. - They did not come.\n"
            "7. Nominal negation with kì í ṣe. Ó jẹ́ olùkọ́. - He is a "
            "teacher. Kì í ṣe olùkọ́. - He is not a teacher.\n"
            "8. Yes/no questions with ṣé. Ṣé o ń bọ̀? - Are you coming? Ṣé "
            "ó ti jẹun? - Has he eaten?\n"
            "9. Focus with ni. Ìwé ni mo rà. - It was a book that I bought. "
            "Èmi ni mo lọ. - It was I who went.\n"
            "10. Copulas: jẹ́ (identity), wà (location). Ó jẹ́ ọ̀rẹ́ mi. - "
            "He is my friend. Ó wà ní ilé. - He is at home. Kì í ṣe ọ̀rẹ́ "
            "mi. - He is not my friend.\n"
            "Plus the engine room: aspect markers ń (progressive: ó ń lọ - "
            "he is going), ti (perfect: ó ti lọ - he has gone), máa/yóò "
            "(future: ó máa lọ - he will go); question words ta, kí, níbo, "
            "ìgbà wo, èéṣe, báwo; serial verbs ó mú ìwé wá (he brought a "
            "book); and the imperative Wá! (Come!), Jókòó! (Sit!)."
        ),
        "how_it_works": (
            "Yoruba grammar works as a fixed-stage play: the subject takes "
            "its mark before the verb, the verb never changes costume, the "
            "object follows, and small markers (ń, ti, máa, kò, ṣé, ni) "
            "light the scene for time, negation, questions, and focus. "
            "Because nouns carry no gender, case, or number endings, all "
            "the grammatical work moves to word order and particles - which "
            "is why the order is strict and the particles are small but "
            "mighty. Master these ten rules and every sentence in this "
            "database parses on sight."
        ),
        "key_points": [
            "SVO order, strict: Mo ra ìwé.",
            "No gender, no cases, no articles; àwọn marks plural.",
            "Adjectives follow nouns; possessives follow nouns.",
            "kò negates verbs; kì í ṣe negates nouns and adjectives.",
            "ṣé opens yes/no questions; ni marks focus; jẹ́/wà are the copulas.",
        ],
        "requirements": [
            "Parse ten sentences from earlier records into S-V-O.",
            "Negate five affirmative sentences with kò and five with kì í ṣe.",
        ],
        "standards": [
            "Rules follow Bamgbose 1966 and Awobuluyi 1978.",
            "Example sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_BAMGBOSE, CIT_AWOBULUYI],
        "must_contain": ["SVO", "Kò lọ.", "kì í ṣe", "Ṣé o ń bọ̀", "Ìwé ni mo rà"],
        "sig_lens": (
            "Through the Signature lens these ten rules are ten sworn laws: "
            "the order unbreakable, the markers unmoving, every sentence a "
            "covenant kept in SVO."
        ),
        "drill": {
            "rules": 10,
            "neg_verbal": "kò",
            "neg_nominal": "kì í ṣe",
            "question_particle": "ṣé",
            "focus_particle": "ni",
            "copulas": ["jẹ́", "wà"],
            "markers": ["ń", "ti", "máa"],
        },
    },
    {
        "key": "home",
        "name": "Home and Family Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the house and the family, in Yoruba with "
            "English translations. \n"
            "  1. Ilé wa tóbi. - Our house is big.\n"
            "  2. Yàrá mi wà lókè. - My room is upstairs.\n"
            "  3. Ìjókòó wà ní yàrá ìsimi. - The chair is in the sitting room.\n"
            "  4. Ibùsùn mi dùn. - My bed is comfortable.\n"
            "  5. Ilẹ̀kùn ṣí. - The door is open.\n"
            "  6. Fèrèsé ti. - The window is closed.\n"
            "  7. Ìwé wà lórí tábìlì. - The book is on the table.\n"
            "  8. Iná ń tàn ní yàrá. - The light is shining in the room.\n"
            "  9. Omi wà nínú ìgò. - Water is in the bottle.\n"
            "  10. Ìyá mi ń se oúnjẹ ní ilé ìdáná. - My mother is cooking in the kitchen.\n"
            "  11. Bàbá mi ń ka ìròyìn. - My father is reading the news.\n"
            "  12. Ẹ̀gbọ́n mi ń ṣiṣẹ́ ní Èkó. - My elder sibling works in Lagos.\n"
            "  13. Àbúrò mi ń kàwé. - My younger sibling is studying.\n"
            "  14. Ọmọ mi nífẹ̀ẹ́ ajá wa. - My child loves our dog.\n"
            "  15. Àwọn ọmọ ń ṣeré níta. - The children are playing outside.\n"
            "  16. Ìyá àgbà dé lánàá. - Grandmother arrived yesterday.\n"
            "  17. Bàbá àgbà ń sọ ìtàn. - Grandfather is telling stories.\n"
            "  18. Ẹbí wa púpọ̀. - Our extended family is large.\n"
            "  19. A jẹun papọ̀ ní alẹ́. - We eat together in the evening.\n"
            "  20. Ilé wa kún fún ayọ̀. - Our home is full of joy."
        ),
        "how_it_works": (
            "Home sentences work as location drills: wà (be at) plus ní "
            "(at/in) pins every person and thing to its place - yàrá mi wà "
            "lókè, ìwé wà lórí tábìlì. Family terms stack by seniority: "
            "ẹ̀gbọ́n (elder sibling) and àbúrò (younger sibling) replace "
            "brother/sister with the age order built in, and ìyá àgbà / "
            "bàbá àgbà (old mother/old father) are grandmother and "
            "grandfather. Possession is always noun-first: ilé wa, ọmọ mi, "
            "ajá wa."
        ),
        "key_points": [
            "wà + ní locates: ó wà ní ilé.",
            "ẹ̀gbọ́n (elder sibling), àbúrò (younger sibling) - age, not gender.",
            "ìyá àgbà = grandmother; bàbá àgbà = grandfather.",
            "Possession follows the noun: ilé wa, ọmọ mi.",
        ],
        "requirements": [
            "Describe your own home in five Yoruba sentences.",
            "Name five family members with the right seniority terms.",
        ],
        "standards": [
            "Kinship terms follow standard Yoruba usage (Abraham 1958).",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_ABRAHAM, CIT_ROWLANDS],
        "must_contain": ["Ẹ̀gbọ́n", "Àbúrò", "Ìyá àgbà", "Ilé wa tóbi", "20"],
        "sig_lens": (
            "Through the Signature lens the home is a sealed compound: "
            "every room a sworn chamber, every elder a living archive, "
            "every meal a covenant renewed at evening."
        ),
        "drill": {
            "sentences": 20,
            "rooms": ["yàrá", "ilé ìdáná", "yàrá ìsimi"],
            "kin": ["bàbá", "ìyá", "ẹ̀gbọ́n", "àbúrò", "ìyá àgbà", "bàbá àgbà", "ẹbí"],
        },
    },
    {
        "key": "food",
        "name": "Food and Cooking Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for meals, ingredients, cooking, and the "
            "restaurant, in Yoruba with English translations. \n"
            "  1. Oúnjẹ ti tán. - The food is ready.\n"
            "  2. Mo fẹ́ jẹ ìrẹsì. - I want to eat rice.\n"
            "  3. Ìyá ń se ọbẹ̀. - Mother is making soup.\n"
            "  4. Iyán dùn púpọ̀. - Pounded yam is very tasty.\n"
            "  5. Ẹja dídùn wà nínú ọbẹ̀. - Tasty fish is in the soup.\n"
            "  6. Mo nífẹ̀ẹ́ àkàrà. - I love bean cakes.\n"
            "  7. Ọkà gbóná dùn. - Hot pap is delicious.\n"
            "  8. Mu omi kí o tó jẹun. - Drink water before you eat.\n"
            "  9. Iyọ̀ pọ̀ jù nínú oúnjẹ yìí. - There is too much salt in this food.\n"
            "  10. Ata kò dùn mí. - Pepper does not agree with me.\n"
            "  11. Ẹran náà tutu. - The meat is fresh.\n"
            "  12. Èso wẹ̀ kí o tó jẹ ẹ́. - Wash the fruit before you eat it.\n"
            "  13. Mo ń gé àgbàdo. - I am cutting maize.\n"
            "  14. Dá omi sí iná. - Pour water on the fire.\n"
            "  15. Ó ń dín ẹja. - She is frying fish.\n"
            "  16. A máa jẹun ní àgogo méje. - We shall eat at 7 o'clock.\n"
            "  17. Mo ti yó. - I am satisfied.\n"
            "  18. Ẹ jọ̀wọ́, mo fẹ́ oúnjẹ. - Please, I want food.\n"
            "  19. Ẹló ni oúnjẹ náà? - How much is the food?\n"
            "  20. Ẹ ṣeun fún oúnjẹ. - Thank you for the meal."
        ),
        "how_it_works": (
            "Food sentences work as verb drills for the kitchen: se (cook/"
            "make), jẹ (eat), mu (drink), gé (cut), dá (pour), dín (fry) - "
            "each taking its object directly. Taste is dùn (be tasty): "
            "oúnjẹ dùn, iyán dùn púpọ̀. Ordering food runs on mo fẹ́ (I "
            "want) plus ẹ jọ̀wọ́ (please) and ẹló ni (how much is it) - the "
            "same three tools as the market record. Satiety is mo ti yó "
            "(I have become satisfied)."
        ),
        "key_points": [
            "Kitchen verbs: se, jẹ, mu, gé, dá, dín.",
            "dùn = be tasty: oúnjẹ dùn.",
            "Order with mo fẹ́ + ẹ jọ̀wọ́; price with ẹló ni.",
            "mo ti yó = I am satisfied.",
        ],
        "requirements": [
            "Order a full meal in Yoruba: greeting, request, price, thanks.",
            "Name ten Yoruba dishes with dùn in a sentence each.",
        ],
        "standards": [
            "Food vocabulary follows Abraham 1958.",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_ABRAHAM],
        "must_contain": ["Iyán", "àkàrà", "Dá omi", "Mo ti yó", "Ẹló ni"],
        "sig_lens": (
            "Through the Signature lens the kitchen is a sworn workshop: "
            "every dish a covenant of taste, iyán the sealed staple, dùn "
            "the vow the tongue keeps."
        ),
        "drill": {
            "sentences": 20,
            "dishes": ["ìrẹsì", "iyán", "àkàrà", "ọkà", "ọbẹ̀", "ẹja"],
            "kitchen_verbs": ["se", "jẹ", "mu", "gé", "dá", "dín"],
        },
    },
]

ENTRIES += [
    {
        "key": "travel",
        "name": "Travel and Directions Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for transport, directions, tickets, and "
            "lodging, in Yoruba with English translations. \n"
            "  1. Níbo ni ọ̀nà lọ sí ọjà? - Where is the road to the market?\n"
            "  2. Ọ̀nà yìí lọ sí Èkó. - This road goes to Lagos.\n"
            "  3. Ẹ tẹ̀síwájú, ẹ yí padà sí ọ̀tún. - Go straight, turn right.\n"
            "  4. Ẹ yí padà sí òsì ní ìkọ́lé. - Turn left at the junction.\n"
            "  5. Ọkọ̀ náà dé. - The vehicle has arrived.\n"
            "  6. Ọkọ̀ ń bọ̀. - The vehicle is coming.\n"
            "  7. Mo fẹ́ lọ sí Ìbàdàn. - I want to go to Ibadan.\n"
            "  8. Ẹló ni tikẹ́ẹ̀tì? - How much is the ticket?\n"
            "  9. Mo fẹ́ tikẹ́ẹ̀tì kan. - I want one ticket.\n"
            "  10. Ọkọ̀ náà kún. - The vehicle is full.\n"
            "  11. Jókòó níbẹ̀. - Sit there.\n"
            "  12. Dúró! Mo fẹ́ sọ̀kalẹ̀. - Stop! I want to get down.\n"
            "  13. Ìrìnàjò náà gùn. - The journey is long.\n"
            "  14. A dé ní àlàáfíà. - We arrived safely.\n"
            "  15. Níbo ni ilé ìtura wà? - Where is the hotel?\n"
            "  16. Mo fẹ́ yàrá kan fún òru kan. - I want a room for one night.\n"
            "  17. Yàrá náà lẹ́wà. - The room is beautiful.\n"
            "  18. Ẹló ni fún òru kan? - How much for one night?\n"
            "  19. Mo ti sanwó. - I have paid.\n"
            "  20. Ẹ ku ìrìnàjò! - Welcome from the journey!"
        ),
        "how_it_works": (
            "Travel sentences work as direction drills: níbo (where) opens, "
            "tẹ̀síwájú (go straight) / yí padà (turn) steer, and sí ọ̀tún / "
            "sí òsì (to the right / to the left) aim. Transport runs on ọkọ̀ "
            "(vehicle): dé (arrive), bọ̀ (come), kún (be full), sọ̀kalẹ̀ "
            "(alight). Lodging runs on ilé ìtura (hotel) with fún òru kan "
            "(for one night) and the price question ẹló ni. Arrival closes "
            "with the blessing a dé ní àlàáfíà (we arrived in peace)."
        ),
        "key_points": [
            "Directions: tẹ̀síwájú, yí padà sí ọ̀tún/òsì.",
            "Transport verbs: dé, bọ̀, kún, sọ̀kalẹ̀.",
            "Lodging: ilé ìtura, yàrá, fún òru kan, ẹló ni.",
            "Safe-arrival blessing: a dé ní àlàáfíà.",
        ],
        "requirements": [
            "Ask for and give directions to three places in Yoruba.",
            "Book a room and a ticket in a role-play.",
        ],
        "standards": [
            "Travel vocabulary follows standard Yoruba usage.",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_ROWLANDS, CIT_ABRAHAM],
        "must_contain": ["Níbo ni ọ̀nà", "yí padà sí ọ̀tún", "ilé ìtura", "A dé ní àlàáfíà"],
        "sig_lens": (
            "Through the Signature lens the journey is a sworn road: every "
            "turn sealed, every arrival a covenant kept in peace."
        ),
        "drill": {
            "sentences": 20,
            "direction_words": ["tẹ̀síwájú", "yí padà", "ọ̀tún", "òsì", "ìkọ́lé"],
            "transport_verbs": ["dé", "bọ̀", "kún", "sọ̀kalẹ̀"],
        },
    },
    {
        "key": "work",
        "name": "Work and School Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for jobs, the office, the classroom, and "
            "learning, in Yoruba with English translations. \n"
            "  1. Mo ń ṣiṣẹ́ ní ọ́fíìsì. - I work at the office.\n"
            "  2. Iṣẹ́ mi dùn mí. - I enjoy my work.\n"
            "  3. Ó jẹ́ olùkọ́. - He is a teacher.\n"
            "  4. Òun jẹ́ dókítà. - She is a doctor.\n"
            "  5. Mo ń kọ́ èdè Yorùbá. - I am learning Yoruba.\n"
            "  6. Akẹ́kọ̀ọ́ ń kàwé ní ilé-ìwé. - The student is reading at school.\n"
            "  7. Olùkọ́ ń kọ́ wa ní ìṣirò. - The teacher is teaching us mathematics.\n"
            "  8. Kọ́ mi ní èdè Gẹ̀ẹ́sì. - Teach me English.\n"
            "  9. Mo ti kọ́ ìwé náà. - I have learned the book.\n"
            "  10. Ẹ ku iṣẹ́! - Well done! (to one working)\n"
            "  11. Iṣẹ́ púpọ̀ wà lónìí. - There is much work today.\n"
            "  12. Mo máa parí iṣẹ́ náà lọ́la. - I will finish the work tomorrow.\n"
            "  13. Jọ̀wọ́ ràn mí lọ́wọ́. - Please help me.\n"
            "  14. Ẹ ṣeun fún ìrànlọ́wọ́. - Thank you for the help.\n"
            "  15. Ìpàdé wà ní àgogo mẹ́sàán. - The meeting is at 9 o'clock.\n"
            "  16. Mo pẹ́ díẹ̀. - I am a little late.\n"
            "  17. Má ṣe pẹ́! - Don't be late!\n"
            "  18. Ìdánwò náà rọrùn. - The examination is easy.\n"
            "  19. Mo kọjá ìdánwò náà. - I passed the examination.\n"
            "  20. Ẹ ku ìkẹ́kọ̀ọ́! - Happy studying!"
        ),
        "how_it_works": (
            "Work sentences run on ṣiṣẹ́ (work) and parí (finish); school "
            "sentences run on kọ́ (teach) and kọ́ ẹ̀kọ́/kàwé (learn/study). "
            "Professions take jẹ́: ó jẹ́ olùkọ́, òun jẹ́ dókítà. The office "
            "clock runs on ní àgogo (at o'clock) and pẹ́ (be late) with its "
            "imperative má ṣe pẹ́. Encouragement is the ẹ ku system again: "
            "ẹ ku iṣẹ́ to the worker, ẹ ku ìkẹ́kọ̀ọ́ to the student."
        ),
        "key_points": [
            "ṣiṣẹ́ (work), parí (finish); kọ́ (teach), kàwé (study).",
            "Professions with jẹ́: ó jẹ́ olùkọ́.",
            "Time: ní àgogo mẹ́sàán; pẹ́ (be late).",
            "Help: ràn lọ́wọ́; ìrànlọ́wọ́ (help, noun).",
        ],
        "requirements": [
            "State your job and workplace in Yoruba.",
            "Describe your school day in six sentences.",
        ],
        "standards": [
            "School and work vocabulary follows standard Yoruba usage.",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_ABRAHAM, CIT_ROWLANDS],
        "must_contain": ["Ó jẹ́ olùkọ́", "Mo ń kọ́ èdè Yorùbá", "ràn mí lọ́wọ́", "Ìdánwò"],
        "sig_lens": (
            "Through the Signature lens work is a sworn craft and study a "
            "sworn apprenticeship: every lesson a seal pressed into the "
            "mind."
        ),
        "drill": {
            "sentences": 20,
            "professions": ["olùkọ́", "dókítà", "akẹ́kọ̀ọ́"],
            "school_verbs": ["kọ́", "kàwé", "kọjá"],
        },
    },
    {
        "key": "health",
        "name": "Health and Body Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for body parts, symptoms, the doctor visit, "
            "and the pharmacy, in Yoruba with English translations. \n"
            "  1. Orí ń dun mi. - My head aches.\n"
            "  2. Inú ń run mi. - My stomach aches.\n"
            "  3. Ara mi ń gbóná. - My body is hot (I have a fever).\n"
            "  4. Mo ní ibà. - I have a fever.\n"
            "  5. Ikọ́ ń ṣe mi. - I have a cough.\n"
            "  6. Ojú mi ń dun mi. - My eyes hurt.\n"
            "  7. Ẹsẹ̀ mi wú. - My leg is swollen.\n"
            "  8. Mo rẹ̀ gan. - I am very tired.\n"
            "  9. Mo ṣàìsàn. - I am sick.\n"
            "  10. Lọ sí ilé-ìwòsàn. - Go to the hospital.\n"
            "  11. Dókítà wà? - Is the doctor in?\n"
            "  12. Dókítà, ara mi ò dáa. - Doctor, I am not well.\n"
            "  13. Níbo ni oògùn wà? - Where is the medicine?\n"
            "  14. Mu oògùn rẹ lọ́jọ́júmọ́. - Take your medicine daily.\n"
            "  15. Má ṣe jẹ oúnjẹ yìí. - Don't eat this food.\n"
            "  16. Sun dáradára. - Sleep well.\n"
            "  17. Mu omi púpọ̀. - Drink plenty of water.\n"
            "  18. Ọwọ́ mi mọ́. - My hands are clean.\n"
            "  19. Mo ti sàn. - I have recovered.\n"
            "  20. Ẹ ṣeun, dókítà. - Thank you, doctor."
        ),
        "how_it_works": (
            "Body sentences name the part first - orí (head), inú (belly), "
            "ojú (eye), ẹsẹ̀ (leg), ọwọ́ (hand) - then the symptom: ń dun "
            "mi (aches me), wú (swollen), gbóná (hot). Illness is ṣàìsàn "
            "(be sick) and ibà (fever); recovery is ti sàn (have become "
            "well). The clinic runs on ilé-ìwòsàn (hospital), dókítà "
            "(doctor), and oògùn (medicine) with the instruction mu oògùn "
            "rẹ (take your medicine). Prevention speaks in imperatives: mu "
            "omi púpọ̀, sun dáradára."
        ),
        "key_points": [
            "Body parts: orí, inú, ojú, etí, imú, ẹnu, ọwọ́, ẹsẹ̀.",
            "Pain: ń dun mi; swelling: wú; fever: ibà, gbóná.",
            "ṣàìsàn (be sick); mo ti sàn (I have recovered).",
            "Clinic: ilé-ìwòsàn, dókítà, oògùn.",
        ],
        "requirements": [
            "Describe three symptoms to a doctor in Yoruba.",
            "Give five health instructions using imperatives.",
        ],
        "standards": [
            "Body and health vocabulary follows Abraham 1958.",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_ABRAHAM],
        "must_contain": ["Orí ń dun mi", "ilé-ìwòsàn", "oògùn", "Mo ti sàn"],
        "sig_lens": (
            "Through the Signature lens the body is a sworn vessel: every "
            "ache a signal sealed in the flesh, every recovery a covenant "
            "renewed."
        ),
        "drill": {
            "sentences": 20,
            "body_parts": ["orí", "inú", "ojú", "etí", "imú", "ẹnu", "ọwọ́", "ẹsẹ̀"],
            "symptoms": ["dun", "wú", "gbóná", "ibà", "rẹ̀"],
        },
    },
    {
        "key": "emotions",
        "name": "Emotions and Feelings Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for happiness, sadness, anger, fear, love, "
            "and surprise - many built on inú (the inside, the heart), in "
            "Yoruba with English translations. \n"
            "  1. Inú mi dùn. - I am happy. (my inside is sweet)\n"
            "  2. Mo ní ayọ̀ púpọ̀. - I have great joy.\n"
            "  3. Ó ń rẹ́rìn-ín. - He is laughing.\n"
            "  4. Inú mi bàjẹ́. - I am sad. (my inside is spoiled)\n"
            "  5. Ó ń sunkún. - She is crying.\n"
            "  6. Mo ní ìbànújẹ́. - I am sorrowful.\n"
            "  7. Mo bínú. - I am angry.\n"
            "  8. Má bínú! - Don't be angry!\n"
            "  9. Inú rẹ dùn? - Are you happy?\n"
            "  10. Ẹ̀rù ń bà mí. - I am afraid. (fear catches me)\n"
            "  11. Má ṣe bẹ̀rù. - Don't be afraid.\n"
            "  12. Mo nífẹ̀ẹ́ rẹ̀. - I love you.\n"
            "  13. Ìfẹ́ dùn. - Love is sweet.\n"
            "  14. Ó yà mí lẹ́nu. - It surprised me.\n"
            "  15. Mo yà! - I am surprised!\n"
            "  16. Mo rẹ̀. - I am tired.\n"
            "  17. Mo ní ìrètí. - I have hope.\n"
            "  18. Mo ní ìgbàgbọ́. - I have faith.\n"
            "  19. Inú mi balẹ̀. - I am calm. (my inside is settled)\n"
            "  20. Ọkàn mi dákẹ́. - My heart is at peace."
        ),
        "how_it_works": (
            "Emotion sentences work through inú (the inside): dùn (sweet) "
            "for happy, bàjẹ́ (spoiled) for sad, balẹ̀ (settled) for calm - "
            "the heart as the seat of feeling. Fear is ẹ̀rù ń bà mí (fear "
            "catches me), with the imperative má ṣe bẹ̀rù. Love is nífẹ̀ẹ́ "
            "(have love for): mo nífẹ̀ẹ́ rẹ̀. Surprise is ó yà mí lẹ́nu (it "
            "opened my mouth). Anger is bínú (be angry) with the softener "
            "má bínú - the most-used apology in the language."
        ),
        "key_points": [
            "inú dùn (happy), inú bàjẹ́ (sad), inú balẹ̀ (calm).",
            "Fear: ẹ̀rù ń bà mí; courage: má ṣe bẹ̀rù.",
            "Love: mo nífẹ̀ẹ́ rẹ̀; surprise: ó yà mí lẹ́nu.",
            "má bínú = don't be angry / sorry.",
        ],
        "requirements": [
            "Express six emotions about your own day in Yoruba.",
            "Comfort a friend using má ṣe bẹ̀rù and inú rẹ yóò dùn.",
        ],
        "standards": [
            "Emotion idioms follow standard Yoruba usage (Abraham 1958).",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_ABRAHAM],
        "must_contain": ["Inú mi dùn", "Inú mi bàjẹ́", "Ẹ̀rù ń bà mí", "Mo nífẹ̀ẹ́ rẹ̀"],
        "sig_lens": (
            "Through the Signature lens the heart is a sealed chamber: inú "
            "dùn the vow of joy, inú bàjẹ́ the vow of grief, every feeling "
            "sworn in the inside."
        ),
        "drill": {
            "sentences": 20,
            "inu_forms": ["dùn", "bàjẹ́", "balẹ̀"],
            "emotions": ["ayọ̀", "ìbànújẹ́", "bínú", "ẹ̀rù", "ìfẹ́", "ìrètí"],
        },
    },
    {
        "key": "nature",
        "name": "Nature and Weather Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for animals, plants, seasons, and weather "
            "talk, in Yoruba with English translations. \n"
            "  1. Òjò ń rọ̀. - It is raining. (rain is falling)\n"
            "  2. Oòrùn ń ràn. - The sun is shining.\n"
            "  3. Afẹ́fẹ́ ń fẹ́. - The wind is blowing.\n"
            "  4. Ọ̀run ṣú. - The sky is dark.\n"
            "  5. Òṣùpá tàn. - The moon is bright.\n"
            "  6. Ìràwọ̀ púpọ̀ wà lọ́run. - Many stars are in the sky.\n"
            "  7. Òjò yóò rọ̀ lọ́la. - It will rain tomorrow.\n"
            "  8. Oòrùn mu lónìí. - The sun is strong today.\n"
            "  9. Òtútù ń ṣe. - It is cold.\n"
            "  10. Ẹ ku òjò! - Greetings in the rain!\n"
            "  11. Ajá mi nífẹ̀ẹ́ omi. - My dog loves water.\n"
            "  12. Ológbò ń lé eku. - The cat is chasing a rat.\n"
            "  13. Ẹyẹ ń kọrin. - The bird is singing.\n"
            "  14. Adìẹ púpọ̀ wà ní àgbo. - Many chickens are in the coop.\n"
            "  15. Ewúrẹ́ ń jẹ koríko. - The goat is eating grass.\n"
            "  16. Màlúù ń mu omi. - The cow is drinking water.\n"
            "  17. Igi ńlá wà ní àárín ọgbà. - A big tree is in the middle of the garden.\n"
            "  18. Òdòdó lẹ́wà. - The flower is beautiful.\n"
            "  19. Ẹ̀fọ́ yìí tutu. - These greens are fresh.\n"
            "  20. Ẹ ku oòrùn! - Greetings in the sun!"
        ),
        "how_it_works": (
            "Weather sentences work as nature verbs: rọ̀ (fall, of rain), "
            "ràn (shine, of sun), fẹ́ (blow, of wind), ṣú (be dark), tàn (be "
            "bright). Animals take everyday verbs: lé (chase), jẹ (eat), mu "
            "(drink), kọrin (sing). The garden is ọgbà, the flower òdòdó, "
            "greens ẹ̀fọ́. Weather greetings close the set: ẹ ku òjò in the "
            "rain, ẹ ku oòrùn in the sun - the ẹ ku system honoring even the "
            "sky."
        ),
        "key_points": [
            "Weather verbs: rọ̀ (rain falls), ràn (sun shines), fẹ́ (wind blows).",
            "ṣú (be dark), tàn (be bright) for sky, moon, stars.",
            "Animals: ajá, ológbò, ẹyẹ, adìẹ, ewúrẹ́, màlúù, eku.",
            "Garden: ọgbà; flower: òdòdó; greens: ẹ̀fọ́.",
        ],
        "requirements": [
            "Describe today's weather in four Yoruba sentences.",
            "Name ten animals with a verb each.",
        ],
        "standards": [
            "Nature vocabulary follows Abraham 1958.",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_ABRAHAM],
        "must_contain": ["Òjò ń rọ̀", "Oòrùn ń ràn", "Afẹ́fẹ́ ń fẹ́", "Òdòdó"],
        "sig_lens": (
            "Through the Signature lens the sky is a sworn canopy: òjò the "
            "sealed rain, oòrùn the sealed fire, every season a covenant "
            "the year keeps."
        ),
        "drill": {
            "sentences": 20,
            "weather_verbs": ["rọ̀", "ràn", "fẹ́", "ṣú", "tàn"],
            "animals": ["ajá", "ológbò", "ẹyẹ", "adìẹ", "ewúrẹ́", "màlúù", "eku"],
        },
    },
]

ENTRIES += [
    {
        "key": "shopping",
        "name": "Shopping and Money Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the market, prices, bargaining, and "
            "paying, in Yoruba with English translations. \n"
            "  1. Ẹló ni èyí? - How much is this?\n"
            "  2. Ẹló ni ẹja náà? - How much is the fish?\n"
            "  3. Ó wọ́n jù. - It is too expensive.\n"
            "  4. Ó lọ́wọ́lọ́wọ́. - It is cheap.\n"
            "  5. Ẹ dínkù. - Reduce the price.\n"
            "  6. Ẹ jọ̀wọ́, ẹ dínkù díẹ̀. - Please, reduce it a little.\n"
            "  7. Mo fẹ́ ra aṣọ. - I want to buy cloth.\n"
            "  8. Wọ́n ń tà ẹja ní ọjà. - They sell fish at the market.\n"
            "  9. Mo ní owó. - I have money.\n"
            "  10. Mi ò ní owó. - I don't have money.\n"
            "  11. Mo ti sanwó. - I have paid.\n"
            "  12. Ẹ mú ìyókù owó mi wá. - Bring my change.\n"
            "  13. Ìyókù owó náà kò pé. - The change is not complete.\n"
            "  14. Mo fẹ́ wo ẹ̀wù náà. - I want to look at the shirt.\n"
            "  15. Ẹ̀wù yìí tóbi jù. - This shirt is too big.\n"
            "  16. Ẹ̀wù yẹn kéré jù. - That shirt is too small.\n"
            "  17. Mo fẹ́ èyí. - I want this one.\n"
            "  18. Ẹ káàbọ̀ sí ọjà wa! - Welcome to our market!\n"
            "  19. Ọjà kún lónìí. - The market is crowded today.\n"
            "  20. Ẹ ṣeun, ẹ ku ìtajà! - Thank you, happy trading!"
        ),
        "how_it_works": (
            "Market sentences run on three tools: ẹló ni (how much is it) "
            "to price, ẹ dínkù (reduce it) to bargain, and mo ti sanwó (I "
            "have paid) to close. Judgments are wọ́n jù (too dear) and "
            "lọ́wọ́lọ́wọ́ (cheap). Fitting is tóbi jù / kéré jù (too big / "
            "too small). Money itself is owó, paying is sanwó, and the "
            "change is ìyókù owó. The trader's welcome is ẹ káàbọ̀ sí ọjà "
            "wa, and the parting blessing is ẹ ku ìtajà."
        ),
        "key_points": [
            "Price: ẹló ni; bargain: ẹ dínkù; pay: sanwó.",
            "Too dear: ó wọ́n jù; cheap: ó lọ́wọ́lọ́wọ́.",
            "Change: ìyókù owó; too big/small: tóbi jù / kéré jù.",
            "Trader's blessing: ẹ ku ìtajà.",
        ],
        "requirements": [
            "Bargain for three items in a market role-play.",
            "Price ten things in your room in Yoruba.",
        ],
        "standards": [
            "Market vocabulary follows standard Yoruba usage.",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_ROWLANDS, CIT_ABRAHAM],
        "must_contain": ["Ẹló ni èyí", "Ó wọ́n jù", "Ẹ dínkù", "ìyókù owó"],
        "sig_lens": (
            "Through the Signature lens the market is a sworn exchange: "
            "every price a vow, every bargain a covenant haggled in honor, "
            "every payment a seal."
        ),
        "drill": {
            "sentences": 20,
            "price_words": ["ẹló ni", "wọ́n jù", "lọ́wọ́lọ́wọ́", "dínkù", "sanwó", "ìyókù owó"],
        },
    },
    {
        "key": "friendship",
        "name": "Friendship and Social Life Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences for meeting people, invitations, and "
            "celebrations, in Yoruba with English translations. \n"
            "  1. Ẹ káàbọ̀, ọ̀rẹ́ mi! - Welcome, my friend!\n"
            "  2. Orúkọ mi ni Manon. - My name is Manon.\n"
            "  3. Kí ni orúkọ rẹ? - What is your name?\n"
            "  4. Ó dára láti pàdé ẹ. - Nice to meet you.\n"
            "  5. Níbo ni o ti wá? - Where are you from?\n"
            "  6. Mo ti Èkó wá. - I am from Lagos.\n"
            "  7. Jẹ́ ká lọ! - Let's go!\n"
            "  8. Jẹ́ ká jẹun papọ̀. - Let's eat together.\n"
            "  9. Mo pè ọ́ sí ayẹyẹ mi. - I invite you to my party.\n"
            "  10. Ayẹyẹ yóò wà ní ọ̀la. - The party will be tomorrow.\n"
            "  11. Ẹ ku ayẹyẹ! - Enjoy the celebration!\n"
            "  12. Ẹ ku ọdún! - Happy festival!\n"
            "  13. Ọjọ́ ìbí mi ni lónìí. - Today is my birthday.\n"
            "  14. Ẹ ku ọjọ́ ìbí! - Happy birthday!\n"
            "  15. Ẹ ṣeun fún ẹ̀bùn náà. - Thank you for the gift.\n"
            "  16. A máa pàdé lọ́la. - We shall meet tomorrow.\n"
            "  17. Má ṣe gbàgbé! - Don't forget!\n"
            "  18. Mo máa rántí ẹ. - I will remember you.\n"
            "  19. Ó dàbọ̀, ọ̀rẹ́ mi. - Goodbye, my friend.\n"
            "  20. Ó di ọ̀la! - Until tomorrow!"
        ),
        "how_it_works": (
            "Friendship sentences open with orúkọ (name): orúkọ mi ni X, "
            "kí ni orúkọ rẹ? Invitations run on mo pè ọ́ sí (I invite you "
            "to) and the hortative jẹ́ ká (let us): jẹ́ ká lọ, jẹ́ ká jẹun "
            "papọ̀. Celebrations take the ẹ ku blessings: ẹ ku ayẹyẹ, ẹ ku "
            "ọdún, ẹ ku ọjọ́ ìbí. Memory is rántí (remember) against gbàgbé "
            "(forget): mo máa rántí ẹ, má ṣe gbàgbé. Parting keeps ó dàbọ̀ "
            "and ó di ọ̀la."
        ),
        "key_points": [
            "Names: orúkọ mi ni X; kí ni orúkọ rẹ?",
            "Invitations: mo pè ọ́ sí; jẹ́ ká (let us).",
            "Celebration blessings: ẹ ku ayẹyẹ, ẹ ku ọdún, ẹ ku ọjọ́ ìbí.",
            "Memory: rántí vs gbàgbé.",
        ],
        "requirements": [
            "Introduce yourself and two friends in Yoruba.",
            "Invite someone to a celebration in five sentences.",
        ],
        "standards": [
            "Social vocabulary follows standard Yoruba usage.",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_ROWLANDS],
        "must_contain": ["Orúkọ mi ni", "Jẹ́ ká lọ", "Ẹ ku ọjọ́ ìbí", "rántí"],
        "sig_lens": (
            "Through the Signature lens friendship is a sworn bond: every "
            "invitation a seal, every celebration a covenant of joy kept "
            "together."
        ),
        "drill": {
            "sentences": 20,
            "social_words": ["orúkọ", "pè", "ayẹyẹ", "ọdún", "ẹ̀bùn", "rántí", "gbàgbé"],
        },
    },
    {
        "key": "technology",
        "name": "Technology and Communication Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences for the phone, internet, computer, and "
            "messaging, in Yoruba with English translations. \n"
            "  1. Mo ní fóònù. - I have a phone.\n"
            "  2. Fóònù mi ń dún. - My phone is ringing.\n"
            "  3. Ẹ dáhùn fóònù! - Answer the phone!\n"
            "  4. Kí ni nọ́mbà fóònù rẹ? - What is your phone number?\n"
            "  5. Fi ìránṣẹ́ ránṣẹ́ sí mi. - Send me a message.\n"
            "  6. Mo ti rán ìránṣẹ́. - I have sent the message.\n"
            "  7. Ṣí kọ̀mpútà. - Open the computer.\n"
            "  8. Kọ̀mpútà mi ń ṣiṣẹ́. - My computer is working.\n"
            "  9. Intánẹ́ẹ̀tì ń ṣiṣẹ́. - The internet is working.\n"
            "  10. Intánẹ́ẹ̀tì ò ń ṣiṣẹ́. - The internet is not working.\n"
            "  11. Mo ń lo intánẹ́ẹ̀tì. - I am using the internet.\n"
            "  12. Fọ́tò náà lẹ́wà. - The photo is beautiful.\n"
            "  13. Ẹ yà fọ́tò! - Take a photo!\n"
            "  14. Mo fẹ́ pè ẹ́. - I want to call you.\n"
            "  15. Ẹ máa pè mí lọ́la. - Call me tomorrow.\n"
            "  16. Bátìrì fóònù mi ti tán. - My phone battery is finished.\n"
            "  17. Ẹ so fóònù náà mọ́ iná. - Plug the phone in.\n"
            "  18. Ẹ pa á. - Turn it off.\n"
            "  19. Ẹ tan án. - Turn it on.\n"
            "  20. Ẹ ṣeun fún ìpè náà. - Thank you for the call."
        ),
        "how_it_works": (
            "Technology sentences borrow and bend: fóònù (phone), kọ̀mpútà "
            "(computer), intánẹ́ẹ̀tì (internet), fọ́tò (photo), tikẹ́ẹ̀tì "
            "(ticket) - English loans respelled to Yoruba sounds. Verbs "
            "stay native: dáhùn (answer), ránṣẹ́ (send a message), pè (call), "
            "ṣí (open), pa (turn off), tan (turn on). The machine obeys "
            "imperatives: ṣí kọ̀mpútà, ẹ pa á, ẹ tan án."
        ),
        "key_points": [
            "Loans respelled: fóònù, kọ̀mpútà, intánẹ́ẹ̀tì, fọ́tò.",
            "Native verbs: dáhùn, ránṣẹ́, pè, ṣí, pa, tan.",
            "Machine imperatives: ṣí kọ̀mpútà, ẹ pa á.",
        ],
        "requirements": [
            "Send a text message in Yoruba.",
            "Explain a phone problem in five sentences.",
        ],
        "standards": [
            "Technology loans follow current standard Yoruba usage.",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_ABRAHAM],
        "must_contain": ["fóònù", "kọ̀mpútà", "intánẹ́ẹ̀tì", "Fi ìránṣẹ́ ránṣẹ́"],
        "sig_lens": (
            "Through the Signature lens the machine is a sworn servant: "
            "every loanword a seal of the new age pressed into the old "
            "tongue, every command a covenant the device keeps."
        ),
        "drill": {
            "sentences": 20,
            "loans": ["fóònù", "kọ̀mpútà", "intánẹ́ẹ̀tì", "fọ́tò", "nọ́mbà"],
            "tech_verbs": ["dáhùn", "ránṣẹ́", "pè", "ṣí", "pa", "tan"],
        },
    },
    {
        "key": "tenses",
        "name": "Yoruba Verb Tenses in Sentences",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The Yoruba verb system is aspect, not tense: small markers "
            "before the unchanging verb root. Six patterns, six translated "
            "sentences each. \n\n"
            "Habitual / simple (bare verb - general truth or past by context):\n"
            "  1. Mo lọ sí ọjà lánàá. - I went to the market yesterday.\n"
            "  2. Ó jẹ ìrẹsì. - He ate rice.\n"
            "  3. Wọ́n dé ní òwúrọ̀. - They arrived in the morning.\n"
            "  4. Mo rí i. - I saw it.\n"
            "  5. Ó sùn. - He slept.\n"
            "  6. A pàdé ní ọjà. - We met at the market.\n"
            "Progressive ń (is doing):\n"
            "  1. Mo ń lọ sí ọjà. - I am going to the market.\n"
            "  2. Ó ń jẹ ìrẹsì. - He is eating rice.\n"
            "  3. Wọ́n ń dé. - They are arriving.\n"
            "  4. Ìyá ń se oúnjẹ. - Mother is cooking food.\n"
            "  5. Ọmọ náà ń sùn. - The child is sleeping.\n"
            "  6. A ń kọ́ Yorùbá. - We are learning Yoruba.\n"
            "Perfect ti (has done):\n"
            "  1. Mo ti lọ. - I have gone.\n"
            "  2. Ó ti jẹun. - He has eaten.\n"
            "  3. Wọ́n ti dé. - They have arrived.\n"
            "  4. Mo ti rí i. - I have seen it.\n"
            "  5. Ó ti sùn. - He has slept.\n"
            "  6. A ti kọ́ ẹ̀kọ́ náà. - We have learned the lesson.\n"
            "Future máa / yóò (will do):\n"
            "  1. Mo máa lọ lọ́la. - I will go tomorrow.\n"
            "  2. Ó máa jẹ ìrẹsì. - He will eat rice.\n"
            "  3. Wọ́n máa dé. - They will arrive.\n"
            "  4. Òjò yóò rọ̀. - It will rain.\n"
            "  5. A máa pàdé. - We shall meet.\n"
            "  6. Ẹ máa wá. - You will come.\n"
            "Subjunctive kí (should / let):\n"
            "  1. Kí ó lọ. - Let him go. / He should go.\n"
            "  2. Kí wọ́n wá. - Let them come.\n"
            "  3. Mo fẹ́ kí o dúró. - I want you to stop.\n"
            "  4. Kí á jẹun. - Let us eat.\n"
            "  5. Ó dára kí ó sùn. - It is good that he sleeps.\n"
            "  6. Kí ẹ máa bọ̀ lọ́la. - Come back tomorrow. (let you return)\n"
            "Negative kò / ò (did not / does not):\n"
            "  1. Kò lọ. - He did not go.\n"
            "  2. Mi ò rí i. - I did not see it.\n"
            "  3. Wọ́n ò dé. - They did not arrive.\n"
            "  4. Ó ò ń sùn. - He is not sleeping.\n"
            "  5. A ò ní owó. - We don't have money.\n"
            "  6. Ẹ ò gbọ́dọ̀ lọ. - You must not go."
        ),
        "how_it_works": (
            "Yoruba verbs work as root plus riders: the bare root covers "
            "habitual and past-by-context (mo lọ), ń rides for ongoing "
            "action (mo ń lọ), ti rides for completed action (mo ti lọ), "
            "máa/yóò ride for the future (mo máa lọ), kí rides for wishes "
            "and commands (kí ó lọ), and kò/ò rides for negation (kò lọ, mi "
            "ò lọ). Riders stack in a fixed order - kò before ń before the "
            "root: ó ò ń sùn. There is no conjugation table to memorize, "
            "only six riders to master."
        ),
        "key_points": [
            "Bare verb: habitual / past by context.",
            "ń = progressive; ti = perfect; máa/yóò = future.",
            "kí = subjunctive (let/should); kò/ò = negation.",
            "Riders stack in fixed order: ó ò ń sùn.",
            "No conjugation - only six markers.",
        ],
        "requirements": [
            "Conjugate one verb through all six patterns aloud.",
            "Write your yesterday, today, and tomorrow in the three aspects.",
        ],
        "standards": [
            "Aspect analysis follows Bamgbose 1966 and Awobuluyi 1978.",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_BAMGBOSE, CIT_AWOBULUYI],
        "must_contain": ["Mo ń lọ", "Mo ti lọ", "Mo máa lọ", "Kí ó lọ", "Kò lọ"],
        "sig_lens": (
            "Through the Signature lens the six markers are six sworn "
            "riders: ń the rider of now, ti the rider of done, máa the "
            "rider of tomorrow - the root unchanging beneath them all."
        ),
        "drill": {
            "patterns": ["bare", "ń", "ti", "máa/yóò", "kí", "kò/ò"],
            "per_pattern": 6,
            "root": "lọ",
        },
    },
    {
        "key": "qa",
        "name": "Yoruba Questions and Answers",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Twenty question-and-answer pairs covering who, what, where, "
            "when, why, and how - in Yoruba with English translations. \n"
            "  1. Q: Ta ni? A: Èmi ni. - Who is it? It is I.\n"
            "  2. Q: Kí ni èyí? A: Ìwé ni. - What is this? It is a book.\n"
            "  3. Q: Níbo ni ìwé mi wà? A: Ó wà lórí tábìlì. - Where is my book? It is on the table.\n"
            "  4. Q: Ìgbà wo ni o dé? A: Mo dé lánàá. - When did you arrive? I arrived yesterday.\n"
            "  5. Q: Èéṣe tí o kò wá? A: Mo ṣàìsàn. - Why did you not come? I was sick.\n"
            "  6. Q: Báwo ni? A: Aláàfíà ni. - How are you? I am well.\n"
            "  7. Q: Mélòó ni owó náà? A: Owó ogún ni. - How much is the money? It is twenty.\n"
            "  8. Q: Èwo ni o fẹ́? A: Mo fẹ́ èyí. - Which do you want? I want this one.\n"
            "  9. Q: Ṣé o ń bọ̀? A: Bẹ́ẹ̀ ni, mo ń bọ̀. - Are you coming? Yes, I am coming.\n"
            "  10. Q: Ṣé ó ti jẹun? A: Bẹ́ẹ̀ ni, ó ti jẹun. - Has he eaten? Yes, he has eaten.\n"
            "  11. Q: Ta ni bàbá rẹ? A: Bàbá mi ni olùkọ́. - Who is your father? My father is a teacher.\n"
            "  12. Q: Kí ni iṣẹ́ rẹ? A: Mo ń ṣiṣẹ́ ní ọ́fíìsì. - What is your work? I work at the office.\n"
            "  13. Q: Níbo ni o ń lọ? A: Mo ń lọ sí ọjà. - Where are you going? I am going to the market.\n"
            "  14. Q: Ìgbà wo ni a máa jẹun? A: A máa jẹun ní àgogo méje. - When shall we eat? We shall eat at 7.\n"
            "  15. Q: Èéṣe tí òjò fi ń rọ̀? A: Ìgbà òjò ni. - Why is it raining? It is the rainy season.\n"
            "  16. Q: Báwo ni o ṣe mọ̀? A: Olùkọ́ mi kọ́ mi. - How did you know? My teacher taught me.\n"
            "  17. Q: Mélòó ni ọmọ rẹ? A: Ọmọ mẹ́ta ni. - How many children do you have? Three children.\n"
            "  18. Q: Ṣé inú rẹ dùn? A: Bẹ́ẹ̀ ni, inú mi dùn. - Are you happy? Yes, I am happy.\n"
            "  19. Q: Kí ni orúkọ rẹ? A: Orúkọ mi ni Manon. - What is your name? My name is Manon.\n"
            "  20. Q: Níbo ni o ti wá? A: Mo ti Èkó wá. - Where are you from? I am from Lagos."
        ),
        "how_it_works": (
            "Yoruba questions work three ways: question words open "
            "information questions (ta, kí, níbo, ìgbà wo, èéṣe, báwo, "
            "mélòó, èwo), ṣé opens yes/no questions (ṣé o ń bọ̀?), and "
            "rising intonation alone can question in speech. Answers echo "
            "the focus with ni: ta ni? - èmi ni; kí ni èyí? - ìwé ni. Yes "
            "is bẹ́ẹ̀ ni, no is rárá. The question word usually "
            "stays where the answer would sit, with ni focusing it."
        ),
        "key_points": [
            "Question words: ta, kí, níbo, ìgbà wo, èéṣe, báwo, mélòó, èwo.",
            "ṣé opens yes/no questions; bẹ́ẹ̀ ni = yes.",
            "Answers echo with ni: ta ni? - èmi ni.",
            "Intonation alone can question in speech.",
        ],
        "requirements": [
            "Ask and answer all eight question-word types about your day.",
            "Hold a two-minute Q&A with a partner using only Yoruba.",
        ],
        "standards": [
            "Question formation follows Awobuluyi 1978.",
            "Pairs are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_AWOBULUYI, CIT_BAMGBOSE],
        "must_contain": ["Ṣé o ń bọ̀", "Bẹ́ẹ̀ ni", "Níbo ni", "Èéṣe"],
        "sig_lens": (
            "Through the Signature lens every question is a sworn inquiry "
            "and every answer a sealed testimony: ta ni? - èmi ni."
        ),
        "drill": {
            "pairs": 20,
            "qwords": ["ta", "kí", "níbo", "ìgbà wo", "èéṣe", "báwo", "mélòó", "èwo"],
            "yes": "bẹ́ẹ̀ ni",
            "yn_particle": "ṣé",
        },
    },
]

ENTRIES += [
    {
        "key": "commands",
        "name": "Yoruba Commands and Requests",
        "group": "Grammar in Action",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty imperatives and polite requests - formal (ẹ-forms) "
            "versus informal (bare forms) - in Yoruba with English "
            "translations. The bare verb commands; ẹ jọ̀wọ́ softens; má "
            "forbids. \n\n"
            "Direct commands (informal, to friends and juniors):\n"
            "  1. Wá! - Come!\n"
            "  2. Lọ! - Go!\n"
            "  3. Jókòó! - Sit down!\n"
            "  4. Dúró! - Stop! / Stand!\n"
            "  5. Sọ̀rọ̀! - Speak!\n"
            "  6. Dákẹ́! - Keep quiet!\n"
            "  7. Mu omi! - Drink water!\n"
            "  8. Jẹun! - Eat!\n"
            "  9. Ṣí ilẹ̀kùn! - Open the door!\n"
            "  10. Pa iná! - Turn off the light!\n"
            "Prohibitions with má:\n"
            "  11. Má lọ! - Don't go!\n"
            "  12. Má sọ̀rọ̀! - Don't speak!\n"
            "  13. Má bínú! - Don't be angry!\n"
            "  14. Má ṣe gbàgbé! - Don't forget!\n"
            "Polite requests (formal, with ẹ and jọ̀wọ́):\n"
            "  15. Ẹ jọ̀wọ́, ẹ jókòó. - Please, sit down.\n"
            "  16. Ẹ jọ̀wọ́, ẹ fún mi ní omi. - Please, give me water.\n"
            "  17. Ẹ dákun, ẹ ràn mí lọ́wọ́. - Please, help me.\n"
            "  18. Ẹ má bínú. - Don't be angry. (respectful)\n"
            "  19. Ẹ máa wá lọ́la. - Do come tomorrow. (respectful)\n"
            "  20. Ẹ ṣeun. - Thank you. (closes every request)"
        ),
        "how_it_works": (
            "Yoruba commands work by bareness: the verb alone is the "
            "command - wá, lọ, jókòó - with tone and a sharp voice doing "
            "the work of the exclamation mark. má before the verb forbids: "
            "má lọ, má bínú. Politeness is added, never subtracted: the "
            "plural/respectful ẹ- prefix lifts a command to a request (ẹ "
            "jókòó), jọ̀wọ́ and ẹ dákun soften it further, and ẹ ṣeun "
            "closes it. Use bare forms downward and to peers; use ẹ-forms "
            "upward - the direction of respect is never reversed."
        ),
        "key_points": [
            "Bare verb = command: wá!, lọ!, jókòó!",
            "má + verb = prohibition: má lọ, má bínú.",
            "ẹ- prefix + jọ̀wọ́/ẹ dákun = polite request.",
            "Respect flows upward: bare forms to juniors, ẹ-forms to elders.",
        ],
        "requirements": [
            "Give ten commands to a junior in Yoruba.",
            "Make five polite requests to an elder.",
        ],
        "standards": [
            "Imperative forms follow standard Yoruba usage.",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_AWOBULUYI, CIT_ROWLANDS],
        "must_contain": ["Wá!", "Má lọ!", "Ẹ jọ̀wọ́", "má bínú"],
        "sig_lens": (
            "Through the Signature lens the command is a sworn order and "
            "the polite request a sealed petition: wá the bare vow, ẹ "
            "jọ̀wọ́ the vow wrapped in honor."
        ),
        "drill": {
            "commands": 10,
            "prohibitions": 4,
            "polite": 6,
            "softeners": ["ẹ jọ̀wọ́", "ẹ dákun", "ẹ ṣeun"],
        },
    },
    {
        "key": "descriptions",
        "name": "Describing People and Places",
        "group": "Grammar in Action",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences describing people, places, and things in "
            "detail - the adjective and relative-clause workout - in Yoruba "
            "with English translations. \n"
            "  1. Ọmọdé lẹ́wà tí ń rẹ́rìn-ín dé. - A beautiful smiling child arrived.\n"
            "  2. Obìnrin gíga tí ó wọ aṣọ pupa wà níbẹ̀. - The tall woman wearing red cloth is there.\n"
            "  3. Ọkùnrin ọlọ́gbọ́n ń sọ̀rọ̀. - A wise man is speaking.\n"
            "  4. Bàbá mi jẹ́ ọkùnrin rere. - My father is a good man.\n"
            "  5. Ìyá mi ní ẹ̀rín dídùn. - My mother has a sweet smile.\n"
            "  6. Ọ̀rẹ́ mi ga, ó sì lẹ́wà. - My friend is tall and beautiful.\n"
            "  7. Olùkọ́ wa mọ̀ ìwé púpọ̀. - Our teacher knows many books.\n"
            "  8. Akẹ́kọ̀ọ́ kékeré ń kàwé dáradára. - The small student studies well.\n"
            "  9. Ilé ńlá funfun wà lórí òkè. - A big white house is on the hill.\n"
            "  10. Yàrá mi kékeré ṣùgbọ́n ó mọ́. - My room is small but clean.\n"
            "  11. Ọjà Èkó kún fún ènìyàn púpọ̀. - The Lagos market is full of many people.\n"
            "  12. Ìlú wa lẹ́wà, ọ̀nà rẹ̀ sì mọ́. - Our town is beautiful and its roads are clean.\n"
            "  13. Òkun ńlá dùn mí. - The great sea pleases me.\n"
            "  14. Igi gíga dúró ní ẹ̀bá ọ̀nà. - A tall tree stands by the roadside.\n"
            "  15. Òdòdó pupa ń tàn ní ọgbà. - Red flowers shine in the garden.\n"
            "  16. Ajá dúdú mi nífẹ̀ẹ́ mi púpọ̀. - My black dog loves me very much.\n"
            "  17. Ológbò funfun ń sùn lórí ibùsùn. - The white cat sleeps on the bed.\n"
            "  18. Oúnjẹ dídùn dùn lẹ́nu. - Tasty food is sweet in the mouth.\n"
            "  19. Omi tútù sàn fún ara. - Cold water is good for the body.\n"
            "  20. Ọjọ́ òní lẹ́wà gan. - Today is truly beautiful."
        ),
        "how_it_works": (
            "Descriptions work by stacking: noun, then adjectives, then a "
            "tí-clause (who/which) for the fine detail - obìnrin gíga tí ó "
            "wọ aṣọ pupa (the tall woman who wears red cloth). Contrast "
            "joins with ṣùgbọ́n (but) and addition with sì (and/also): yàrá "
            "mi kékeré ṣùgbọ́n ó mọ́; ó ga, ó sì lẹ́wà. Senses report with "
            "dùn (pleases): òkun ńlá dùn mí; ẹ̀rín dídùn (sweet smile) shows "
            "the adjective doubling as a noun's ornament."
        ),
        "key_points": [
            "Stack: noun + adjectives + tí-clause.",
            "ṣùgbọ́n (but), sì (and/also) join descriptions.",
            "dùn reports the senses: òkun dùn mí.",
            "Adjectives never agree; order carries the detail.",
        ],
        "requirements": [
            "Describe three people and three places in five sentences each.",
            "Use one tí-clause in every description.",
        ],
        "standards": [
            "Relative-clause formation follows Bamgbose 1966.",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_BAMGBOSE],
        "must_contain": ["tí ó wọ aṣọ pupa", "ṣùgbọ́n", "Òkun ńlá dùn mí"],
        "sig_lens": (
            "Through the Signature lens description is sworn portraiture: "
            "every adjective a seal of quality, every tí-clause a finer "
            "seal within."
        ),
        "drill": {
            "sentences": 20,
            "people": 8,
            "places": 7,
            "things": 5,
            "connectors": ["tí", "ṣùgbọ́n", "sì"],
        },
    },
    {
        "key": "story1",
        "name": "Story I: The Market Day",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence simple story in Yoruba - present and habitual "
            "forms - with line-by-line English translation. An original "
            "teaching story. \n"
            "  1. Ìyá mi lọ sí ọjà lọ́jọ́júmọ́. - My mother goes to the market daily.\n"
            "  2. Ó jí ní òwúrọ̀, ó sì wẹ̀. - She wakes in the morning and bathes.\n"
            "  3. Ó mú aṣọ lọ sí ọjà. - She takes cloth to the market.\n"
            "  4. Ọjà kún fún ènìyàn púpọ̀. - The market is full of many people.\n"
            "  5. Ó tà aṣọ, ó sì ra ẹja. - She sells cloth and buys fish.\n"
            "  6. Ọ̀rẹ́ rẹ̀ wá, wọ́n sì sọ̀rọ̀. - Her friend comes, and they chat.\n"
            "  7. Wọ́n rẹ́rìn-ín, inú wọn dùn. - They laugh; they are happy.\n"
            "  8. Oòrùn ń ràn, ṣùgbọ́n afẹ́fẹ́ ń fẹ́. - The sun shines, but the wind blows.\n"
            "  9. Ní alẹ́, ó padà sí ilé. - In the evening, she returns home.\n"
            "  10. A jẹun papọ̀, inú wa dùn. - We eat together; we are happy."
        ),
        "how_it_works": (
            "Story I works as the habitual-aspect showcase: bare verbs "
            "carry the daily round - lọ, jí, wẹ̀, mú, tà, ra, sọ̀rọ̀ - with "
            "lọ́jọ́júmọ́ (daily) setting the rhythm. Chaining with sì (and) "
            "moves the plot: ó jí, ó sì wẹ̀. Time words frame the day: ní "
            "òwúrọ̀, ní alẹ́. Every sentence uses only grammar from the "
            "foundations and vocabulary records - the story is the payoff "
            "for the ladder so far."
        ),
        "key_points": [
            "Bare verbs carry habitual action: ó lọ, ó tà, ó ra.",
            "sì chains events: ó jí, ó sì wẹ̀.",
            "Time frames: ní òwúrọ̀, ní alẹ́, lọ́jọ́júmọ́.",
            "Ten sentences, ten translations, zero new grammar.",
        ],
        "requirements": [
            "Retell the story aloud from memory.",
            "Write your own ten-sentence daily-round story.",
        ],
        "standards": [
            "Original teaching story in standard Yoruba.",
            "Uses only grammar taught in records 1-24.",
        ],
        "citations": [CIT_ROWLANDS],
        "must_contain": ["Ìyá mi lọ sí ọjà", "lọ́jọ́júmọ́", "A jẹun papọ̀"],
        "sig_lens": (
            "Through the Signature lens this market day is a sworn round: "
            "every dawn a seal broken open, every evening a seal closed, "
            "the day's covenant kept."
        ),
        "drill": {
            "sentences": 10,
            "verbs": ["lọ", "jí", "wẹ̀", "mú", "tà", "ra", "sọ̀rọ̀", "rẹ́rìn", "padà", "jẹ"],
            "time_words": ["lọ́jọ́júmọ́", "òwúrọ̀", "alẹ́"],
        },
    },
    {
        "key": "story2",
        "name": "Story II: The Lost Goat",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in Yoruba using past and perfect forms "
            "(ti, bare past) - with line-by-line English translation. An "
            "original teaching story. \n"
            "  1. Ní ọjọ́ kan, ewúrẹ́ bàbá mi sọnù. - One day, my father's goat got lost.\n"
            "  2. A wá a níbikíbi, a ò rí i. - We searched everywhere; we did not find it.\n"
            "  3. Bàbá mi bínú púpọ̀. - My father was very angry.\n"
            "  4. Ọmọ mi kékeré sọ pé: ẹ má bínú! - My small child said: don't be angry!\n"
            "  5. Ó lọ sí ẹ̀bá odò. - He went to the riverside.\n"
            "  6. Níbẹ̀ ni ó ti rí ewúrẹ́ náà. - There he found the goat.\n"
            "  7. Ewúrẹ́ náà ń jẹ koríko. - The goat was eating grass.\n"
            "  8. Ó mú u padà wá sí ilé. - He brought it back home.\n"
            "  9. Inú bàbá mi dùn púpọ̀. - My father was very happy.\n"
            "  10. Ó fún ọmọ náà ní ẹ̀bùn. - He gave the child a gift."
        ),
        "how_it_works": (
            "Story II works as the past-tense showcase: bare verbs set "
            "events in the past (sọnù, bínú, lọ), ti marks completion (ti "
            "rí - had found), and ń paints the background scene (ń jẹ "
            "koríko - was eating grass). Negation drives the middle: a ò rí "
            "i (we did not find it). Direct speech appears with pé (that): "
            "sọ pé: ẹ má bínú. The focus cleft níbẹ̀ ni ó ti rí (there it "
            "was that he found) spotlights the discovery."
        ),
        "key_points": [
            "Bare verbs narrate past events; ti marks completion.",
            "ń paints background action: ń jẹ koríko.",
            "Direct speech with pé: sọ pé.",
            "Focus cleft: níbẹ̀ ni ó ti rí.",
        ],
        "requirements": [
            "Retell the story in the present tense, then the future.",
            "Write a ten-sentence lost-and-found story of your own.",
        ],
        "standards": [
            "Original teaching story in standard Yoruba.",
            "Uses past and perfect forms from the tenses record.",
        ],
        "citations": [CIT_BAMGBOSE],
        "must_contain": ["ewúrẹ́", "sọnù", "Níbẹ̀ ni ó ti rí", "ẹ má bínú"],
        "sig_lens": (
            "Through the Signature lens the lost goat is a sworn parable: "
            "what is lost is sought, what is found is sealed home, the "
            "child's courage the covenant's hinge."
        ),
        "drill": {
            "sentences": 10,
            "past_verbs": ["sọnù", "bínú", "lọ", "rí", "mú", "padà", "fún"],
            "perfect": ["ti rí"],
            "background": ["ń jẹ koríko"],
        },
    },
    {
        "key": "story3",
        "name": "Story III: The Journey Tomorrow",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in Yoruba using future and conditional "
            "forms (máa, yóò, bí) - with line-by-line English translation. "
            "An original teaching story. \n"
            "  1. Lọ́la, mo máa lọ sí Ìbàdàn. - Tomorrow, I will go to Ibadan.\n"
            "  2. Mo máa jí ní àgogo márùún. - I will wake at 5 o'clock.\n"
            "  3. Bí òjò bá rọ̀, mo máa dúró. - If it rains, I will wait.\n"
            "  4. Bí oòrùn bá ràn, mo máa lọ. - If the sun shines, I will go.\n"
            "  5. Ọ̀rẹ́ mi yóò wá pẹ̀lú mi. - My friend will come with me.\n"
            "  6. A máa ra tikẹ́ẹ̀tì méjì. - We shall buy two tickets.\n"
            "  7. Ọkọ̀ yóò dé ní àgogo méje. - The vehicle will arrive at 7 o'clock.\n"
            "  8. A máa dé Ìbàdàn ní ọ̀sán. - We shall reach Ibadan in the afternoon.\n"
            "  9. Ẹ̀gbọ́n mi yóò pàdé wa níbẹ̀. - My elder sibling will meet us there.\n"
            "  10. Ayọ̀ yóò kún ọkàn wa. - Joy will fill our hearts."
        ),
        "how_it_works": (
            "Story III works as the future-and-conditional showcase: máa "
            "and yóò carry every plan (mo máa lọ, yóò dé), and bí ... bá "
            "frames the conditions (bí òjò bá rọ̀ - if rain falls). The "
            "bá after the subject is the conditional's hinge: bí oòrùn bá "
            "ràn. Time anchors stack: lọ́la, ní àgogo márùún, ní ọ̀sán. The "
            "story ends on the blessing-pattern: ayọ̀ yóò kún ọkàn wa."
        ),
        "key_points": [
            "máa / yóò mark the future: mo máa lọ, yóò dé.",
            "bí ... bá frames conditionals: bí òjò bá rọ̀.",
            "Time anchors: lọ́la, ní àgogo márùún, ní ọ̀sán.",
            "Blessing close: ayọ̀ yóò kún ọkàn wa.",
        ],
        "requirements": [
            "Plan your own tomorrow in ten future sentences.",
            "Add two bí-conditions to your plan.",
        ],
        "standards": [
            "Original teaching story in standard Yoruba.",
            "Uses future and conditional forms from the tenses record.",
        ],
        "citations": [CIT_AWOBULUYI],
        "must_contain": ["mo máa lọ sí Ìbàdàn", "Bí òjò bá rọ̀", "Ayọ̀ yóò kún"],
        "sig_lens": (
            "Through the Signature lens tomorrow is a sworn promise: máa "
            "the seal of intent, bí the seal of condition, every plan a "
            "covenant with the dawn."
        ),
        "drill": {
            "sentences": 10,
            "future_markers": ["máa", "yóò"],
            "conditionals": ["bí òjò bá rọ̀", "bí oòrùn bá ràn"],
        },
    },
]

ENTRIES += [
    {
        "key": "idioms",
        "name": "Yoruba Idioms and Proverbs",
        "group": "Stories and Idioms",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Twenty Yoruba proverbs (òwe) and idioms - literal translation, "
            "real meaning, and an example sentence each. Proverbs are the "
            "palm oil with which words are eaten: a Yoruba elder speaks in "
            "òwe. \n\n"
            "Proverbs:\n"
            "  1. Ká rìn ká pọ̀, yíye ní yẹ ni. (That we walk together "
            "befits dignity.) Unity is strength. Apẹẹrẹ: Ẹ jẹ́ ká rìn ká "
            "pọ̀, yíye ní yẹ ni. - Let us walk together; unity befits us.\n"
            "  2. Ọmọ tí a kò kọ́, yóò kọ́ ilé tí a kọ́. (A child we do not "
            "teach will sell the house we built.) Neglect in raising "
            "children destroys the family's work. Apẹẹrẹ: Kọ́ ọmọ rẹ; ọmọ "
            "tí a kò kọ́ yóò kọ́ ilé tí a kọ́. - Teach your child; an "
            "untaught child will sell the house you built.\n"
            "  3. Bí ọmọdé bá mọ ọwọ́ ẹ̀ wẹ̀, yóò bá àgbà jẹun. (If a child "
            "knows how to wash his hands, he will eat with elders.) Good "
            "conduct earns a place among the great. Apẹẹrẹ: Hùwà rere; bí "
            "ọmọdé bá mọ ọwọ́ ẹ̀ wẹ̀, yóò bá àgbà jẹun. - Behave well; a "
            "well-mannered child eats with elders.\n"
            "  4. Tí a bá fi ọwọ́ òtún bá ọmọ wí, a ó fi òsì fà á mọ́ra. "
            "(With the right hand we correct the child, with the left we "
            "draw him close.) Discipline must pair with love. Apẹẹrẹ: Bá ọmọ "
            "wí, ṣùgbọ́n fà á mọ́ra. - Correct the child, but draw him close.\n"
            "  5. Ẹni tó bá da omi síwájú, yóò tẹ̀lé e. (Whoever pours water "
            "ahead will step in it.) You reap what you sow. Apẹẹrẹ: Ṣe rere; "
            "ẹni tó bá da omi síwájú yóò tẹ̀lé e. - Do good; you reap what "
            "you sow.\n"
            "  6. Díẹ̀ díẹ̀ ni imú ẹlẹ́dẹ̀ fi ń wọ ọ̀gbà. (Little by little "
            "the pig's snout enters the garden.) Small compromises grow "
            "into ruin. Apẹẹrẹ: Má ṣe jẹ́ kí ìwà burúkú wọlé díẹ̀díẹ̀. - "
            "Don't let bad habits creep in little by little.\n"
            "  7. Ọwọ́ ọmọdé ò tó pẹpẹ, tàgbà ò wọ̀ keregbe. (A child's hand "
            "cannot reach the shelf; an elder's cannot enter the gourd.) "
            "Everyone has limits. Apẹẹrẹ: Mọ ààlà rẹ. - Know your limits.\n"
            "  8. Àgbà kì í wà lọ́jà kí orí ọmọ tuntun wọ. (An elder cannot "
            "be in the market and watch a newborn's head go wrong.) Elders "
            "must guide the young. Apẹẹrẹ: Àwọn àgbà gbọ́dọ̀ tọ́ ọmọ. - "
            "Elders must guide children.\n"
            "  9. Ilé tí a bá fi ìtọ̀ mọ́, ìrì ni yóò wọ̀ ọ́. (A house built "
            "with spit, dew will destroy it.) Shoddy foundations fail. "
            "Apẹẹrẹ: Fi ìpìlẹ̀ dídára mọ́ ilé rẹ. - Build your house on a "
            "solid foundation.\n"
            "  10. Bí ajá bá fẹ́ sọnù, kò ní gbọ́ fèrè ọlọ́dẹ. (If a dog will "
            "get lost, it will not hear the hunter's whistle.) Those bent "
            "on ruin ignore warnings. Apẹẹrẹ: Gbọ́ ìkìlọ̀. - Heed warnings.\n"
            "Idioms:\n"
            "  11. Inú mi dùn. (My inside is sweet.) I am happy. Apẹẹrẹ: "
            "Inú mi dùn láti rí ẹ. - I am happy to see you.\n"
            "  12. Inú mi bàjẹ́. (My inside is spoiled.) I am sad. Apẹẹrẹ: "
            "Inú mi bàjẹ́ nígbà tí mo gbọ́ ìròyìn náà. - I was sad when I "
            "heard the news.\n"
            "  13. Ó yà mí lẹ́nu. (It opened my mouth.) It surprised me. "
            "Apẹẹrẹ: Ìròyìn náà yà mí lẹ́nu. - The news surprised me.\n"
            "  14. Ẹ̀rù ń bà mí. (Fear catches me.) I am afraid. Apẹẹrẹ: "
            "Ẹ̀rù ń bà mí ní òkùnkùn. - I am afraid in the dark.\n"
            "  15. Ó pa mí lẹ́rìn-ín. (He killed me with laughter.) He is "
            "hilarious. Apẹẹrẹ: Ìtàn rẹ̀ pa mí lẹ́rìn-ín. - His story was "
            "hilarious.\n"
            "  16. Ó jẹ́ ọmọlúàbí. (He is a child of good character.) He is "
            "a person of integrity. Apẹẹrẹ: Jẹ́ ọmọlúàbí níbikíbi. - Be a "
            "person of integrity everywhere.\n"
            "  17. Ó ní ọkàn. (He has heart.) He is brave. Apẹẹrẹ: Ó ní "
            "ọkàn láti sọ òtítọ́. - He was brave enough to tell the truth.\n"
            "  18. Ó dùn mí. (It is sweet to me.) I like it. Apẹẹrẹ: Orin "
            "náà dùn mí. - I like the song.\n"
            "  19. Mo fẹ́ràn rẹ̀. (I hold you dear.) I like you. Apẹẹrẹ: Mo "
            "fẹ́ràn ìwé yìí. - I like this book.\n"
            "  20. Má ṣe dààmú. (Don't be troubled.) Don't worry. Apẹẹrẹ: Má "
            "ṣe dààmú, ohun gbogbo yóò dára. - Don't worry, everything will "
            "be fine."
        ),
        "how_it_works": (
            "Proverbs work as compressed law: òwe states the image (the "
            "pig's snout, the poured water, the two hands), and the hearer "
            "supplies the ruling. Elders deploy them to correct without "
            "confronting - the proverb carries the rebuke so the speaker "
            "need not. Idioms work as body-metaphors: inú (inside) for "
            "feeling, ẹnu (mouth) for surprise, ọkàn (heart) for courage. "
            "Learn ten proverbs and you can hold a conversation with any "
            "elder; learn the inú idioms and you can say anything you feel."
        ),
        "key_points": [
            "òwe (proverb): image states the law; hearer supplies the ruling.",
            "Elders correct through proverbs, not confrontation.",
            "Body idioms: inú (feeling), ẹnu (surprise), ọkàn (courage).",
            "ọmọlúàbí: the person of good character - the highest praise.",
        ],
        "requirements": [
            "Memorize five proverbs and use each once this week.",
            "Explain three idioms to a fellow learner.",
        ],
        "standards": [
            "Proverbs follow the documented Yoruba òwe corpus (Abraham 1958).",
            "Meanings follow standard Yoruba interpretation.",
        ],
        "citations": [CIT_ABRAHAM],
        "must_contain": ["Ká rìn ká pọ̀", "ọmọlúàbí", "Inú mi dùn", "Díẹ̀ díẹ̀ ni imú ẹlẹ́dẹ̀"],
        "sig_lens": (
            "Through the Signature lens the proverb is a sealed law and "
            "the idiom a sealed feeling: òwe the covenant of the elders, "
            "inú dùn the covenant of the heart."
        ),
        "drill": {
            "proverbs": 10,
            "idioms": 10,
            "body_words": ["inú", "ẹnu", "ọkàn"],
        },
    },
    {
        "key": "registers",
        "name": "Formal and Polite Registers",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen formal-versus-informal pairs for letters, business, "
            "and elders - in Yoruba with English translations. The ẹ-forms, "
            "jọ̀wọ́, ẹ dákun, and full titles mark the formal register. \n"
            "  1. káàárọ̀ -> Ẹ káàárọ̀. (Good morning -> Good morning, sir/ma.)\n"
            "  2. jọ̀wọ́ -> Ẹ jọ̀wọ́. (Please -> Please, sir/ma.)\n"
            "  3. Fún mi ní omi. -> Ẹ jọ̀wọ́, ẹ fún mi ní omi. (Give me water -> Please give me water.)\n"
            "  4. Wá! -> Ẹ wá. (Come! -> Do come.)\n"
            "  5. Jókòó! -> Ẹ jọ̀wọ́, ẹ jókòó. (Sit! -> Please sit down.)\n"
            "  6. Má bínú. -> Ẹ má bínú. (Don't be angry -> Please don't be angry.)\n"
            "  7. Ẹ ṣeun. -> Ẹ ṣeun púpọ̀. (Thanks -> Many thanks.)\n"
            "  8. Dákẹ́! -> Ẹ dákẹ́. (Be quiet! -> Please be quiet.)\n"
            "  9. Ẹló ni? -> Ẹ jọ̀wọ́, ẹló ni? (How much? -> Please, how much is it?)\n"
            "  10. Lọ! -> Ẹ máa lọ. (Go! -> Go well.)\n"
            "  11. Padà wá! -> Ẹ máa bọ̀. (Come back! -> Do return safely.)\n"
            "  12. Letter opening: Ọ̀rẹ́ mi, -> Ẹ̀yin ọ̀gá ọ̀wọ́n, (My friend, -> Esteemed sir,)\n"
            "  13. Letter body: Mo ń kọ̀wé yìí... -> Mo kọ lẹ́tà yìí pẹ̀lú ọ̀wọ̀ ńlá... (I am writing... -> I write this letter with great respect...)\n"
            "  14. Letter close: Ó dàbọ̀. -> Ẹ dákun, ẹ máa wà ní àlàáfíà. (Goodbye. -> Please, stay in peace.)\n"
            "  15. Request: Ràn mí lọ́wọ́. -> Ẹ dákun, ẹ ràn mí lọ́wọ́. (Help me. -> I beg you, help me.)"
        ),
        "how_it_works": (
            "Registers work as a respect ladder with three rungs: bare "
            "forms (peers and juniors), ẹ-forms (elders and strangers), and "
            "full titles plus ẹ dákun (formal letters and ceremony). The "
            "plural ẹ- is the workhorse - it lifts any command into a "
            "request. Letters open with ẹ̀yin ọ̀gá ọ̀wọ́n (esteemed sir) or "
            "ẹ̀yin màmá ọ̀wọ́n (esteemed ma), carry the body in ẹ-forms, "
            "and close with a peace blessing. In business, ẹ jọ̀wọ́ before "
            "every price question keeps the trader smiling."
        ),
        "key_points": [
            "Three rungs: bare (peers), ẹ-forms (elders), titles + ẹ dákun (ceremony).",
            "The plural ẹ- lifts commands into requests.",
            "Letters: ẹ̀yin ọ̀gá ọ̀wọ́n opens; peace blessing closes.",
            "Ẹ jọ̀wọ́ before price questions in business.",
        ],
        "requirements": [
            "Write a formal letter of request in Yoruba.",
            "Convert ten bare commands to ẹ-form requests.",
        ],
        "standards": [
            "Register distinctions follow standard Yoruba usage.",
            "Pairs are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_ROWLANDS],
        "must_contain": ["Ẹ̀yin ọ̀gá ọ̀wọ́n", "Ẹ dákun", "Ẹ máa lọ", "Fifteen"],
        "sig_lens": (
            "Through the Signature lens register is a sworn hierarchy of "
            "honor: the bare vow for equals, the ẹ-vow for elders, the "
            "titled vow for ceremony."
        ),
        "drill": {
            "pairs": 15,
            "rungs": ["bare", "ẹ-forms", "titles + ẹ dákun"],
            "openings": ["ẹ̀yin ọ̀gá ọ̀wọ́n", "ẹ̀yin màmá ọ̀wọ́n"],
        },
    },
    {
        "key": "complex",
        "name": "Compound and Complex Sentences",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen long sentences with clauses, connectors, and relative "
            "clauses - parsed and translated. \n"
            "  1. Ọmọ tí ó lọ sí ọjà náà ni ọ̀rẹ́ mi. [ọmọ (child) + tí ó lọ "
            "sí ọjà (who went to the market) + ni ọ̀rẹ́ mi (is my friend)] - "
            "The child who went to the market is my friend.\n"
            "  2. Ìwé tí mo rà lánàá dùn. [ìwé (book) + tí mo rà lánàá "
            "(which I bought yesterday) + dùn (is interesting)] - The book "
            "which I bought yesterday is interesting.\n"
            "  3. Mo lọ sí ọjà nítorí mo fẹ́ ra ẹja. [mo lọ sí ọjà (I went "
            "to the market) + nítorí (because) + mo fẹ́ ra ẹja (I want to "
            "buy fish)] - I went to the market because I want to buy fish.\n"
            "  4. Ó ń ṣiṣẹ́ dáradára ṣùgbọ́n owó rẹ̀ díẹ̀. [ó ń ṣiṣẹ́ "
            "dáradára (he works well) + ṣùgbọ́n (but) + owó rẹ̀ díẹ̀ (his "
            "pay is small)] - He works well but his pay is small.\n"
            "  5. Mo rí bàbá àti ìyá ní ọjà. [mo rí (I saw) + bàbá àti ìyá "
            "(father and mother) + ní ọjà (at the market)] - I saw father "
            "and mother at the market.\n"
            "  6. Ẹ mu omi tàbí ẹ mu ọtí? [ẹ mu omi (drink water) + tàbí (or) "
            "+ ẹ mu ọtí (drink beer)] - Will you drink water or beer?\n"
            "  7. Bí òjò bá rọ̀, a ò ní lọ. [bí òjò bá rọ̀ (if it rains) + a "
            "ò ní lọ (we will not go)] - If it rains, we will not go.\n"
            "  8. Nígbà tí mo dé, wọ́n ń jẹun. [nígbà tí mo dé (when I "
            "arrived) + wọ́n ń jẹun (they were eating)] - When I arrived, "
            "they were eating.\n"
            "  9. Mo wá kí n tó rí ẹ. [mo wá (I came) + kí (so that) + n tó "
            "rí ẹ (I might see you)] - I came so that I might see you.\n"
            "  10. Ó sọ pé òun máa wá lọ́la. [ó sọ (he said) + pé (that) + "
            "òun máa wá lọ́la (he will come tomorrow)] - He said that he "
            "will come tomorrow.\n"
            "  11. Ẹni tó bá ṣiṣẹ́ dáradára yóò rí èrè. [ẹni tó bá ṣiṣẹ́ "
            "dáradára (whoever works well) + yóò rí èrè (will see reward)] - "
            "Whoever works well will be rewarded.\n"
            "  12. Ilé tí a ń gbé ńlá, ṣùgbọ́n yàrá mi kékeré. [ilé tí a ń "
            "gbé ńlá (the house we live in is big) + ṣùgbọ́n (but) + yàrá mi "
            "kékeré (my room is small)] - The house we live in is big, but "
            "my room is small.\n"
            "  13. Kí á tó lọ, ẹ jẹ́ ká jẹun. [kí á tó lọ (before we go) + ẹ "
            "jẹ́ ká jẹun (let us eat)] - Before we go, let us eat.\n"
            "  14. Bó tilẹ̀ jẹ́ pé òjò ń rọ̀, a máa lọ. [bó tilẹ̀ jẹ́ pé "
            "(although) + òjò ń rọ̀ (it is raining) + a máa lọ (we will go)] "
            "- Although it is raining, we will go.\n"
            "  15. Ohun tí mo fẹ́ ni kí ẹ wá. [ohun tí mo fẹ́ (what I want) + "
            "ni (is) + kí ẹ wá (that you come)] - What I want is for you to "
            "come."
        ),
        "how_it_works": (
            "Complex sentences work by clause glue: tí builds relative "
            "clauses (ọmọ tí ó lọ - the child who went), nítorí gives "
            "reasons, ṣùgbọ́n contrasts, àti/tàbí join and choose, bí...bá "
            "conditions, nígbà tí times, kí purposes, pé reports speech. "
            "The head noun always comes first and tí follows it - the "
            "relative clause never leads. Stack two glues and the sentence "
            "grows: ó sọ pé [òun máa wá] nígbà tí [o bá pè é]."
        ),
        "key_points": [
            "tí = who/which/that (relative); head noun first.",
            "nítorí (because), ṣùgbọ́n (but), àti (and), tàbí (or).",
            "bí...bá (if), nígbà tí (when), kí (so that), pé (that).",
            "Glues stack: ó sọ pé òun máa wá nígbà tí o bá pè é.",
        ],
        "requirements": [
            "Combine ten simple sentence pairs with one glue each.",
            "Write a five-sentence paragraph using three different glues.",
        ],
        "standards": [
            "Clause formation follows Bamgbose 1966.",
            "Sentences are constructed teaching examples in standard Yoruba.",
        ],
        "citations": [CIT_BAMGBOSE, CIT_AWOBULUYI],
        "must_contain": ["Ọmọ tí ó lọ", "nítorí", "Bí òjò bá rọ̀", "bó tilẹ̀ jẹ́ pé"],
        "sig_lens": (
            "Through the Signature lens the complex sentence is a sworn "
            "edifice: tí the joint, nítorí the foundation, ṣùgbọ́n the "
            "buttress - every clause sealed to the next."
        ),
        "drill": {
            "sentences": 15,
            "glues": ["tí", "nítorí", "ṣùgbọ́n", "àti", "tàbí", "bí...bá", "nígbà tí", "kí", "pé"],
        },
    },
]

ENTRIES += [
    {
        "key": "conv_market",
        "name": "Conversation: At the Market",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue at the market - Yoruba with "
            "English - annotated with the grammar at work. An original "
            "teaching dialogue. \n"
            "  1. Oníṣòwò: Ẹ káàbọ̀ sí ọjà wa! (Welcome to our market!) "
            "[trader's welcome]\n"
            "  2. Oníbàárà: Ẹ káàsán. (Good afternoon.) [time greeting]\n"
            "  3. Oníbàárà: Ẹló ni ẹja yìí? (How much is this fish?) [ẹló ni prices]\n"
            "  4. Oníṣòwò: Owó márùún ni. (It is five [units].) [bare price]\n"
            "  5. Oníbàárà: Ó wọ́n jù! (Too expensive!) [bargaining opens]\n"
            "  6. Oníṣòwò: Ẹja tutu ni. (It is fresh fish.) [quality claim]\n"
            "  7. Oníbàárà: Ẹ jọ̀wọ́, ẹ dínkù díẹ̀. (Please reduce it a little.) [polite bargain]\n"
            "  8. Oníṣòwò: Ó dára. Owó mẹ́rin. (Fine. Four [units].) [counter-offer]\n"
            "  9. Oníbàárà: Mo fẹ́ méjì. (I want two.) [quantity]\n"
            "  10. Oníṣòwò: Ó dára gan. (Very good indeed.) [agreement]\n"
            "  11. Oníbàárà: Ẹló ni àkàrà? (How much is the bean cake?) [second item]\n"
            "  12. Oníṣòwò: Owó méjì ni. (Two [units].) [price]\n"
            "  13. Oníbàárà: Ẹ fun mi ní mẹ́ta. (Give me three.) [order]\n"
            "  14. Oníṣòwò: Gbogbo rẹ̀ ni owó mẹ́wàá. (All of it is ten [units].) [total]\n"
            "  15. Oníbàárà: Ẹ mú ìyókù owó mi wá. (Bring my change.) [payment]\n"
            "  16. Oníṣòwò: Ẹ wo, ìyókù náà. (Look, the change.) [change given]\n"
            "  17. Oníbàárà: Ẹ ṣeun púpọ̀. (Thank you very much.) [thanks]\n"
            "  18. Oníṣòwò: Kò sí ọ̀ràn. Ẹ máa bọ̀! (No problem. Come again!) [parting]\n"
            "  19. Oníbàárà: Ó dàbọ̀! (Goodbye!) [farewell]\n"
            "  20. Oníṣòwò: Ó di ọ̀la! (Until tomorrow!) [farewell answers]"
        ),
        "how_it_works": (
            "The market dialogue works as the bargaining script: welcome "
            "(ẹ káàbọ̀), price (ẹló ni), protest (ó wọ́n jù), softened demand "
            "(ẹ jọ̀wọ́, ẹ dínkù), counter-offer, quantity (mo fẹ́ méjì), "
            "total (gbogbo rẹ̀ ni...), change (ìyókù owó), thanks (ẹ ṣeun "
            "púpọ̀), parting (ẹ máa bọ̀ / ó dàbọ̀). Every line is a move in "
            "a game both players know; the annotations name each move so "
            "the learner can play either side."
        ),
        "key_points": [
            "Bargaining arc: ẹló ni -> ó wọ́n jù -> ẹ dínkù -> agreement.",
            "Politeness keeps the trader willing: ẹ jọ̀wọ́ throughout.",
            "Totals with gbogbo rẹ̀ ni; change with ìyókù owó.",
            "Parting pair: ẹ máa bọ̀ / ó dàbọ̀.",
        ],
        "requirements": [
            "Role-play both parts aloud with a partner.",
            "Swap in three new items and re-bargain.",
        ],
        "standards": [
            "Original teaching dialogue in standard Yoruba.",
            "Uses market vocabulary from the shopping record.",
        ],
        "citations": [CIT_ROWLANDS],
        "must_contain": ["Ẹló ni ẹja yìí", "Ó wọ́n jù", "ìyókù owó", "20"],
        "sig_lens": (
            "Through the Signature lens the market dialogue is a sworn "
            "negotiation: every price a vow tested, every agreement a seal "
            "struck in public."
        ),
        "drill": {
            "lines": 20,
            "moves": ["welcome", "price", "protest", "bargain", "counter",
                      "quantity", "total", "change", "thanks", "parting"],
            "speakers": ["Oníṣòwò", "Oníbàárà"],
        },
    },
    {
        "key": "conv_friend",
        "name": "Conversation: Meeting a Friend",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue meeting a friend - Yoruba "
            "with English - annotated. An original teaching dialogue. \n"
            "  1. Adé: Ẹ káàárọ̀, Wálé! (Good morning, Wale!) [greeting by name]\n"
            "  2. Wálé: Káàárọ̀, Adé! Báwo ni? (Morning, Ade! How are you?) [peer greeting]\n"
            "  3. Adé: Aláàfíà ni. Ìwọ náà? (I am well. And you?) [health answer]\n"
            "  4. Wálé: Aláàfíà ni. Ó ti pẹ́! (Well. It's been long!) [reunion]\n"
            "  5. Adé: Níbo ni o ti wá? (Where are you from? / Where have you been?) [catch-up]\n"
            "  6. Wálé: Mo ti Èkó wá. (I am from Lagos. / I've been in Lagos.) [origin]\n"
            "  7. Adé: Kí ni iṣẹ́ rẹ níbẹ̀? (What is your work there?) [inquiry]\n"
            "  8. Wálé: Mo ń ṣiṣẹ́ ní ilé-ìwé. (I work at a school.) [answer]\n"
            "  9. Adé: Ó dára gan! (That's truly good!) [approval]\n"
            "  10. Wálé: Báwo ni ẹbí rẹ? (How is your family?) [family inquiry]\n"
            "  11. Adé: Wọ́n wà dáradára. (They are all well.) [family answer]\n"
            "  12. Wálé: Ẹ ku iṣẹ́! (Well done on the work!) [praise]\n"
            "  13. Adé: Ẹ ṣeun. Jẹ́ ká jẹun papọ̀. (Thanks. Let's eat together.) [invitation]\n"
            "  14. Wálé: Ó dára! Níbo? (Good! Where?) [acceptance]\n"
            "  15. Adé: Ní ilé mi, ní alẹ́. (At my house, in the evening.) [plan]\n"
            "  16. Wálé: Mo máa wá. (I will come.) [promise]\n"
            "  17. Adé: Má ṣe gbàgbé! (Don't forget!) [reminder]\n"
            "  18. Wálé: Rárá, mo máa rántí. (No, I will remember.) [reassurance]\n"
            "  19. Adé: Ó dàbọ̀, ọ̀rẹ́ mi. (Goodbye, my friend.) [farewell]\n"
            "  20. Wálé: Ó di alẹ́! (Until evening!) [farewell answers]"
        ),
        "how_it_works": (
            "The reunion dialogue works as the social script: name "
            "greeting, báwo ni health check, ó ti pẹ́ reunion marker, "
            "origin and work inquiry, family inquiry (báwo ni ẹbí rẹ), "
            "praise (ẹ ku iṣẹ́), invitation (jẹ́ ká...), plan, promise (mo "
            "máa wá), reminder (má ṣe gbàgbé), and the paired farewell. The "
            "register slides from respectful ẹ-forms at the opening to peer "
            "bare forms between old friends - the dialogue teaches the "
            "slide."
        ),
        "key_points": [
            "Reunion marker: ó ti pẹ́ (it's been long).",
            "Family inquiry: báwo ni ẹbí rẹ?",
            "Invitation: jẹ́ ká jẹun papọ̀; promise: mo máa wá.",
            "Register slides ẹ-forms -> peer forms between friends.",
        ],
        "requirements": [
            "Role-play the reunion with a partner.",
            "Adapt it to your own town and work.",
        ],
        "standards": [
            "Original teaching dialogue in standard Yoruba.",
            "Uses greeting and social vocabulary from earlier records.",
        ],
        "citations": [CIT_ROWLANDS],
        "must_contain": ["Ó ti pẹ́", "Báwo ni ẹbí rẹ", "Jẹ́ ká jẹun papọ̀", "20"],
        "sig_lens": (
            "Through the Signature lens the reunion is a sworn renewal: ó "
            "ti pẹ́ the seal of absence broken, the shared meal the "
            "covenant restored."
        ),
        "drill": {
            "lines": 20,
            "moves": ["greeting", "health", "reunion", "catchup", "work",
                      "family", "praise", "invitation", "plan", "promise",
                      "reminder", "farewell"],
            "speakers": ["Adé", "Wálé"],
        },
    },
    {
        "key": "conv_problem",
        "name": "Conversation: Solving a Problem",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue solving a problem - Yoruba "
            "with English - annotated. An original teaching dialogue. \n"
            "  1. Ìyá: Kí ló dé? (What happened?) [problem opens]\n"
            "  2. Ọmọ: Fóònù mi sọnù. (My phone is lost.) [problem stated]\n"
            "  3. Ìyá: Níbo ni o ti rí i gbẹ̀yìn? (Where did you last see it?) [diagnosis]\n"
            "  4. Ọmọ: Nínú yàrá mi. (In my room.) [answer]\n"
            "  5. Ìyá: Ṣé o ti wá a dáradára? (Have you searched well?) [check]\n"
            "  6. Ọmọ: Bẹ́ẹ̀ ni, mo ti wá a. (Yes, I have searched.) [answer]\n"
            "  7. Ìyá: Má ṣe dààmú. (Don't worry.) [comfort]\n"
            "  8. Ìyá: Jẹ́ ká wá a papọ̀. (Let's search together.) [plan]\n"
            "  9. Ọmọ: Ó dára. (Good.) [agreement]\n"
            "  10. Ìyá: Wo abẹ́ ibùsùn. (Look under the bed.) [instruction]\n"
            "  11. Ọmọ: Kò sí níbẹ̀. (It is not there.) [report]\n"
            "  12. Ìyá: Wo inú àpótí. (Look in the box.) [instruction]\n"
            "  13. Ọmọ: Mo rí i! (I found it!) [discovery]\n"
            "  14. Ìyá: Níbo? (Where?) [question]\n"
            "  15. Ọmọ: Nínú àpótí ìwé. (In the book box.) [answer]\n"
            "  16. Ìyá: Ẹ ṣeun fún Ọlọ́run. (Thank God.) [relief]\n"
            "  17. Ọmọ: Ẹ ṣeun, ìyá. (Thank you, mother.) [thanks]\n"
            "  18. Ìyá: Má ṣe gbàgbé mọ́. (Don't forget again.) [lesson]\n"
            "  19. Ọmọ: Mo máa rántí. (I will remember.) [promise]\n"
            "  20. Ìyá: Ó dára. Jẹ́ ká jẹun. (Good. Let's eat.) [close]"
        ),
        "how_it_works": (
            "The problem dialogue works as the troubleshooting script: "
            "kí ló dé opens, the problem is stated plainly, níbo ... "
            "gbẹ̀yìn diagnoses, ṣé checks, má ṣe dààmú comforts, jẹ́ ká "
            "plans, imperatives direct the search (wo abẹ́ ibùsùn), kò sí "
            "níbẹ̀ reports, mo rí i! discovers, ẹ ṣeun fún Ọlọ́run relieves, "
            "and the lesson seals it: má ṣe gbàgbé mọ́. Every household "
            "problem in Yoruba follows this arc."
        ),
        "key_points": [
            "Open: kí ló dé?; diagnose: níbo ... gbẹ̀yìn?",
            "Comfort: má ṣe dààmú; plan: jẹ́ ká.",
            "Search imperatives: wo abẹ́ ibùsùn, wo inú àpótí.",
            "Close with lesson: má ṣe gbàgbé mọ́.",
        ],
        "requirements": [
            "Role-play the search with a partner.",
            "Adapt it to a different lost object.",
        ],
        "standards": [
            "Original teaching dialogue in standard Yoruba.",
            "Uses question and imperative forms from earlier records.",
        ],
        "citations": [CIT_AWOBULUYI],
        "must_contain": ["Kí ló dé", "Má ṣe dààmú", "Mo rí i!", "20"],
        "sig_lens": (
            "Through the Signature lens the search is a sworn recovery: "
            "what is lost is hunted, what is found is sealed with thanks, "
            "the lesson a covenant against the next loss."
        ),
        "drill": {
            "lines": 20,
            "moves": ["open", "state", "diagnose", "check", "comfort",
                      "plan", "instruct", "report", "discover", "relief",
                      "thanks", "lesson", "promise", "close"],
            "speakers": ["Ìyá", "Ọmọ"],
        },
    },
    {
        "key": "mastery",
        "name": "Yoruba Mastery Review and Full Reference",
        "group": "Mastery Reference",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The whole database in one teaching summary: the alphabet, 200 "
            "core words, the key grammar rules, and the phrase tables. \n\n"
            "Alphabet (25 letters): a b d e ẹ f g gb h i j k l m n o ọ p r "
            "s ṣ t u w y. Dotted: ẹ ọ ṣ. Digraph: gb. Tones: á (high), a "
            "(mid), à (low). \n\n"
            "200 core words:\n"
            "People (20): ọmọ, obìnrin, ọkùnrin, bàbá, ìyá, ẹ̀gbọ́n, àbúrò, "
            "ìyá àgbà, bàbá àgbà, ọ̀rẹ́, olùkọ́, akẹ́kọ̀ọ́, dókítà, oníṣòwò, "
            "àgbà, ọmọdé, ẹbí, ọkọ, aya, ènìyàn.\n"
            "Body (15): orí, ojú, etí, imú, ẹnu, ọwọ́, ẹsẹ̀, inú, ọkàn, "
            "ahọ́n, eyín, irun, awọ, ẹ̀jẹ̀, egungun.\n"
            "Home (15): ilé, yàrá, ilé ìdáná, yàrá ìsimi, ilẹ̀kùn, fèrèsé, "
            "tábìlì, àga, ibùsùn, iná, ìgò, àpótí, aṣọ, aṣọ ìbora, dígí.\n"
            "Food (20): oúnjẹ, omi, ìrẹsì, iyán, àkàrà, ọkà, èkó, ọbẹ̀, ẹja, "
            "ẹran, adìẹ, ẹyin, èso, àgbàdo, iyọ̀, ata, òróró, sùgà, ọtí, wàrà.\n"
            "Nature (20): oòrùn, òṣùpá, ìràwọ̀, ọ̀run, òjò, afẹ́fẹ́, igi, "
            "òdòdó, ewé, ẹ̀fọ́, koríko, òkè, òkun, odò, ilẹ̀, òkúta, iyanrìn, "
            "ìgbó, ọgbà, òwúrọ̀.\n"
            "Animals (15): ajá, ológbò, ẹyẹ, adìẹ, ewúrẹ́, màlúù, ẹṣin, eku, "
            "ẹja, ejò, òkété, kìnìún, ẹfọ̀n, agbọ́n, labalábá.\n"
            "Verbs (40): lọ, wá, jẹ, mu, sùn, jí, wẹ̀, rà, tà, ṣe, sọ, gbọ́, "
            "rí, fẹ́, mọ̀, ní, kọ́, kà, kọ, ṣiṣẹ́, rìn, sáré, dúró, jókòó, ṣí, "
            "ti, gé, dá, fún, gba, pè, béèrè, dáhùn, pàdé, rántí, gbàgbé, "
            "ṣubú, dìde, parí, bẹ̀rẹ̀.\n"
            "Adjectives (20): ńlá, kékeré, gíga, kúrú, tuntun, àtijọ́, pupa, "
            "funfun, dúdú, dídùn, tútù, lẹ́wà, ọlọ́gbọ́n, ṣòro, rọrùn, yára, "
            "lọ́ra, púpọ̀, díẹ̀, rere.\n"
            "Function words (20): mo, o, ó, a, ẹ, wọ́n, mi, rẹ, rẹ̀, wa, "
            "yín, wọn, yìí, yẹn, àti, ṣùgbọ́n, tàbí, nítorí, bí, pé.\n"
            "Time/number (15): òní, lánàá, lọ́la, òwúrọ̀, ọ̀sán, alẹ́, ọjọ́, "
            "òru, ọ̀sẹ̀, oṣù, ọdún, ìgbà, àgogo, mélòó, gbogbo.\n"
            "Key grammar (ten rules): 1) SVO: mo ra ìwé. 2) No gender, case, "
            "articles. 3) àwọn marks plural. 4) Adjectives follow nouns. 5) "
            "kò negates verbs; kì í ṣe negates nouns. 6) ṣé asks yes/no. 7) "
            "ni focuses: ìwé ni mo rà. 8) jẹ́ = identity, wà = location. 9) "
            "Markers: ń (progressive), ti (perfect), máa (future), kí "
            "(subjunctive). 10) tí builds relative clauses. \n\n"
            "Phrase tables:\n"
            "Greetings: Ẹ káàárọ̀ / Ẹ káàsán / Ẹ káalẹ́; Káàbọ̀; Báwo ni?; "
            "Ẹ ku iṣẹ́; Ẹ ṣeun; Ó dàbọ̀.\n"
            "Market: Ẹló ni?; Ó wọ́n jù; Ẹ dínkù; Mo ti sanwó; ìyókù owó.\n"
            "Travel: Níbo ni...?; Tẹ̀síwájú; Yí padà sí ọ̀tún/òsì; A dé ní "
            "àlàáfíà.\n"
            "Help: Ẹ jọ̀wọ́; Ẹ dákun; Ràn mí lọ́wọ́; Má ṣe dààmú.\n"
            "Feelings: Inú mi dùn; Inú mi bàjẹ́; Mo bínú; Mo nífẹ̀ẹ́ rẹ̀; "
            "Ẹ̀rù ń bà mí."
        ),
        "how_it_works": (
            "The mastery record works as the one-page covenant of the whole "
            "database: the 25 letters with their tones, the 200 words that "
            "carry 90 percent of daily speech, the ten rules that parse "
            "every sentence, and the five phrase tables that open every "
            "door. Learn this page cold and the other 33 records become "
            "reference depth behind it. The ladder is complete: foundations "
            "(records 1-3), core vocabulary (4-9), grammar essentials "
            "(10), everyday themes (11-20), grammar in action (21-24), "
            "stories and idioms (25-28), conversation and registers "
            "(29-33), and this mastery reference (34)."
        ),
        "key_points": [
            "25 letters, 3 tones, 200 core words, 10 grammar rules, 5 phrase tables.",
            "The 200 words carry most of daily speech.",
            "The ladder: foundations -> vocabulary -> grammar -> themes -> action -> stories -> conversation -> mastery.",
        ],
        "requirements": [
            "Recite the alphabet with tones from memory.",
            "Use 50 of the 200 words in sentences of your own.",
        ],
        "standards": [
            "Word list consolidates vocabulary from records 1-33.",
            "Reference follows the standard Yoruba orthography.",
        ],
        "citations": [CIT_ABRAHAM, CIT_BAMGBOSE, CIT_AWOBULUYI, CIT_ROWLANDS, CIT_ISO],
        "must_contain": ["200 core words", "25 letters", "mo ra ìwé", "Inú mi dùn", "àwọn marks plural"],
        "sig_lens": (
            "Through the Signature lens this reference is the sealed "
            "covenant of the whole ladder: every letter a mark, every word "
            "a vow, every rule a law - the language carried whole."
        ),
        "drill": {
            "letters": 25,
            "core_words": 200,
            "rules": 10,
            "phrase_tables": 5,
            "word_groups": {"people": 20, "body": 15, "home": 15,
                            "food": 20, "nature": 20, "animals": 15,
                            "verbs": 40, "adjectives": 20,
                            "function": 20, "time_number": 15},
        },
    },
]
