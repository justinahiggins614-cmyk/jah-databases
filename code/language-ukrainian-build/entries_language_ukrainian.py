#!/usr/bin/env python3
"""Entries for the Ukrainian to English databases (Manon's language project, 2026-10-17).

Verified 2026-10-17: RAW SWEEP over the full manifest PLUS every shard index
title in jah-databases-data-1: zero 'language-ukrainian*' slugs. ID prefixes
JAH-LUKR- (public) and JAH-LUKRS- (signature) verified free in the manifest
id_prefix values AND in every shard index (zero hits for 'JAH-LUKR' across
all index.jsonl.gz files). Pre-authoring whole-system dedupe-gate check over
all 68 planned titles (34 records + 34 Signature Edition titles): zero
collisions, zero refusals.

This build creates two NEW databases, 34 ladder-ordered records each:

  language-ukrainian              - The Ukrainian to English Database
                                    (public-harvest: real, fact-checked
                                    Ukrainian - overview, the Cyrillic
                                    alphabet, phonology and free stress, core
                                    vocabulary with sentences, the seven
                                    cases and grammar essentials, themed
                                    sentence sets, verb aspect and tenses,
                                    questions and answers, commands,
                                    descriptions, stories, idioms and
                                    proverbs, registers, complex sentences,
                                    conversations, mastery reference; every
                                    line in Ukrainian with English
                                    translation; standard references
                                    Shevelov 1979, Pugh and Press 1999,
                                    ISO 639 uk/ukr)
  language-ukrainian-signature    - The Ukrainian to English Signature Database
                                    (his original Signature Language Method:
                                    every Cyrillic letter a sworn mark,
                                    every case a sealed vow, every sentence a
                                    covenant of meaning; src signature,
                                    titles suffixed " (Signature Edition)",
                                    clearly labeled Signature-made, never
                                    presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record carries Ukrainian content with English translation + example
sentences. Sentences are required in EVERY record - no vocabulary-list-only
records. Example sentences are Signature-generated teaching constructions
built from the documented grammar and attested vocabulary; the linguistic
facts (alphabet, grammar rules, core vocabulary, idioms) are public-harvest
and fact-checked.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_ukrainian.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with the
OK marker; the build machine-executes all 68 demos before writing.

Build-time cross-check: every entry declares 'must_contain' strings and the
build asserts each one appears verbatim in the record description, so entry
text and demo outputs can never drift apart.

No website references. Screened per canon.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every Cyrillic letter a sworn mark, every case a sealed vow, "
            "every sentence a covenant of meaning. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_SHEVELOV = ("Shevelov GY. A Historical Phonology of the Ukrainian "
                "Language. Harvard Ukrainian Research Institute; 1979.")
CIT_PUGH = ("Pugh SM, Press I. Ukrainian: A Comprehensive Grammar. "
            "Routledge; 1999.")
CIT_BILODID = ("Bilodid IK, ed. Suchasna ukrainska literaturna mova "
               "(Modern Ukrainian Literary Language). Naukova Dumka; 1969.")
CIT_ISO = ("ISO 639: Ukrainian is coded uk (ISO 639-1) and ukr "
           "(ISO 639-3); the modern 33-letter alphabet was restored with "
           "the letter g (ge) in 1990.")

# The Ukrainian Cyrillic alphabet: (letter, transliteration, sound note).
# The four iotated letters ye yi yu ya are the signature marks of the script.
UKR_ALPHA = [
    ("А", "a", "a as in father"), ("Б", "b", "b as in boy"),
    ("В", "v", "v as in van"), ("Г", "h", "voiced h, as in ahead"),
    ("Ґ", "g", "hard g as in go"), ("Д", "d", "d as in dog"),
    ("Е", "e", "e as in bed"), ("Є", "ye", "ye as in yes"),
    ("Ж", "zh", "zh as in measure"), ("З", "z", "z as in zebra"),
    ("И", "y", "short i, as in bit"), ("І", "i", "ee as in machine"),
    ("Ї", "yi", "yee as in yield"), ("Й", "y", "y as in boy"),
    ("К", "k", "k as in kite"), ("Л", "l", "l as in love"),
    ("М", "m", "m as in man"), ("Н", "n", "n as in name"),
    ("О", "o", "o as in more"), ("П", "p", "p as in pen"),
    ("Р", "r", "rolled r"), ("С", "s", "s as in sun"),
    ("Т", "t", "t as in top"), ("У", "u", "oo as in moon"),
    ("Ф", "f", "f as in fan"), ("Х", "kh", "ch as in loch"),
    ("Ц", "ts", "ts as in cats"), ("Ч", "ch", "ch as in church"),
    ("Ш", "sh", "sh as in ship"), ("Щ", "shch", "sh + ch together"),
    ("Ь", "ʹ", "soft sign, softens the consonant"),
    ("Ю", "yu", "yoo as in you"), ("Я", "ya", "ya as in yard"),
]
IOTATED = ["Є", "Ї", "Ю", "Я"]
VOWEL_LETTERS = ["А", "Е", "Є", "И", "І", "Ї", "О", "У", "Ю", "Я"]


def _alpha_lines():
    return "\n".join(
        "  %s  %s  - %s" % (ch, tr, note) for ch, tr, note in UKR_ALPHA)


ENTRIES = [
    {
        "key": "overview",
        "name": "Ukrainian Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Ukrainian (українська мова, ukrainska mova) is the East Slavic "
            "language of the Indo-European family, spoken by the Ukrainian "
            "people and the state language of Ukraine. It carries ISO codes "
            "uk (ISO 639-1) and ukr (ISO 639-3). About 40 million people "
            "speak it as a mother tongue, and total speakers are near 50 "
            "million when second-language users are counted. \n\n"
            "Where it is spoken. The heartland is Ukraine itself - from "
            "Kyiv on the Dnipro to Lviv in the west, Odesa on the Black "
            "Sea, and Kharkiv in the east. Large Ukrainian-speaking "
            "diasporas live in Canada (over a million people of Ukrainian "
            "descent), the United States, Poland, Romania, Moldova, "
            "Kazakhstan, Brazil, and Argentina, and Ukrainian is recognized "
            "as a minority language in nine European states. \n\n"
            "Official status. Ukrainian is the sole official language of "
            "Ukraine under its constitution. It is a recognized minority "
            "language in Bosnia and Herzegovina, Croatia, Czechia, Hungary, "
            "Moldova, Poland, Romania, Serbia, and Slovakia. \n\n"
            "Dialects. Three dialect groups are recognized: Northern "
            "(Polissian), Southeastern (Middle Dnieprian, the basis of the "
            "standard literary language), and Southwestern (Galician, "
            "Transcarpathian, Bukovinian, Podillian, Volhynian). Speakers "
            "of all three understand the literary standard with ease. \n\n"
            "History in one breath. Ukrainian grew from the Old East Slavic "
            "of Kyivan Rus; the first literary monuments appear in the "
            "twelfth century; Taras Shevchenko's Kobzar (1840) fixed the "
            "modern literary language; the 1876 Ems Ukaz tried to ban "
            "Ukrainian print; the letter ґ was restored to the alphabet in "
            "1990; and Ukrainian became the state language of independent "
            "Ukraine in 1991. \n\n"
            "What makes Ukrainian learnable. The alphabet is phonetic "
            "Cyrillic - what you see is what you say. Word order is the "
            "familiar subject-verb-object. There are no articles. Learn the "
            "seven noun cases, the two verb conjugations, and the "
            "perfective-imperfective aspect pair, and the language opens "
            "like a door. \n\n"
            "First sentences in українська мова:\n"
            "  Привіт! - Hello!\n"
            "  Мене звати Манон. - My name is Manon.\n"
            "  Я люблю українську мову. - I love the Ukrainian language.\n"
            "  Я почав вивчати українську сьогодні. - I started learning Ukrainian today."
        ),
        "how_it_works": (
            "This record is the map of the whole database. It fixes the "
            "identity of the language - name (українська мова), codes (uk / "
            "ukr), family (Indo-European, Balto-Slavic, Slavic, East "
            "Slavic), speaker scale (about 40 million native, near 50 "
            "million total), territory (Ukraine and the world diaspora, "
            "strongest in Canada, the USA, Poland, and Romania), official "
            "standing (state language of Ukraine; recognized minority "
            "language in nine European states), dialect landscape "
            "(Northern, Southeastern standard, Southwestern), and the "
            "historical arc (Kyivan Rus, Shevchenko 1840, Ems Ukaz 1876, "
            "ґ restored 1990, state language 1991). Every later record "
            "hangs facts on this frame: the alphabet record spells the 33 "
            "Cyrillic letters, the phonology record sounds the six vowels "
            "and free stress, the vocabulary records fill the word-hoard, "
            "and the grammar records assemble the engine. Work through the "
            "ladder in order and each record assumes only what earlier "
            "records taught."
        ),
        "key_points": [
            "Native name: українська мова; ISO 639-1 uk, ISO 639-3 ukr.",
            "Family: Indo-European, Balto-Slavic, Slavic, East Slavic.",
            "About 40 million native speakers; near 50 million total with second-language users.",
            "Sole official language of Ukraine; recognized minority language in nine European states.",
            "Three dialect groups: Northern (Polissian), Southeastern (standard), Southwestern.",
            "Kyivan Rus roots; Shevchenko 1840; Ems Ukaz 1876; letter ґ restored 1990; state language 1991.",
            "SVO word order; no articles; seven noun cases; perfective-imperfective verb aspect.",
        ],
        "requirements": [
            "No prior knowledge of any Slavic language is assumed.",
            "Read the alphabet record before the phonology record; read the phonology record before the vocabulary records.",
        ],
        "standards": [
            "Speaker figures are rounded public estimates (Ethnologue-style reporting); the record states them as approximate.",
            "Dialect and history claims follow the standard references: Shevelov 1979, Pugh and Press 1999.",
            "All example sentences are Signature-generated teaching constructions built from documented grammar and attested vocabulary; linguistic facts are public-harvest and fact-checked.",
        ],
        "citations": [CIT_SHEVELOV, CIT_PUGH, CIT_ISO],
        "must_contain": ["українська мова", "uk", "ukr", "East Slavic", "Kyiv", "40 million"],
        "sig_lens": (
            "Through the Signature lens this overview is a census of a "
            "living nation of speakers: every headcount a sworn roll-call, "
            "every dialect a branch of one family tree, every century of "
            "history a seal on the covenant that this language will be "
            "carried whole into the archive."
        ),
        "drill": {
            "native_m": 40.0, "total_m": 50.0, "official_countries": 1,
            "iso1": "uk", "iso3": "ukr",
            "dialects": ["Northern (Polissian)", "Southeastern (Middle Dnieprian)",
                         "Southwestern (Galician)", "Southwestern (Transcarpathian)",
                         "Southwestern (Bukovynian)"],
            "regions": ["Ukraine", "Canada", "United States", "Poland",
                        "Romania", "Moldova", "Kazakhstan", "Brazil", "Argentina"],
            "recognized": 9,
        },
    },
    {
        "key": "writing",
        "name": "The Ukrainian Writing System",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Ukrainian is written in a 33-letter Cyrillic alphabet, used "
            "left-to-right, and it is phonetic: what you see is what you "
            "say. Numerals are the ordinary Arabic digits 0-9, and "
            "punctuation follows European conventions. \n\n"
            "The Ukrainian alphabet, letter by letter:\n"
            + _alpha_lines() + "\n\n"
            "The four iotated letters are the signature of written "
            "Ukrainian: Є (ye), Ї (yi), Ю (yu), Я (ya) each carry a "
            "built-in y-glide, so яма (pit) starts with the sound ya. Ї is "
            "found almost nowhere else in the Slavic world. Ґ (ge) is the "
            "hard g of go, kept distinct from Г (he), the voiced h of "
            "ahead; the letter ґ was restored to the alphabet in 1990 "
            "after decades of absence. Ь (soft sign) has no sound of its "
            "own - it softens the consonant before it, as in день (day). "
            "The apostrophe ’ (as in м’ясо, meat, or ім’я, name) keeps a "
            "consonant hard before an iotated vowel. \n\n"
            "Ten letters are vowel letters: А Е Є И І Ї О У Ю Я. There is "
            "no q, w, or x in native Ukrainian words; foreign words are "
            "adapted, so the Latin w becomes в. Upper and lower case "
            "mirror each other: Аа Бб Вв Гг Ґґ. \n\n"
            "Read and write these first words:\n"
            "  україна - Ukraine\n"
            "  мова - language\n"
            "  ґрунт - soil, ground\n"
            "  їжак - hedgehog\n"
            "  ім’я - name\n"
            "  щастя - happiness\n"
            "  день - day\n"
            "  вода - water"
        ),
        "how_it_works": (
            "The alphabet works by direct sound-to-letter mapping: learn "
            "the 33 letters and you can read any Ukrainian word aloud. "
            "The iotated letters Є Ї Ю Я do double duty - they spell both "
            "a y-glide and their vowel, and after a consonant they soften "
            "it. The soft sign Ь softens without adding a vowel; the "
            "apostrophe ’ blocks softening where the hard sound must stay. "
            "Г is always the voiced h (голова, head), Ґ is always hard g "
            "(ґанок, porch). Because spelling is phonetic, writing drills "
            "double as pronunciation drills: copy the table, read it "
            "aloud, and the letters become reflexes."
        ),
        "key_points": [
            "33-letter Cyrillic alphabet, left-to-right, fully phonetic.",
            "Iotated signatures: Є (ye), Ї (yi), Ю (yu), Я (ya).",
            "Г = voiced h, Ґ = hard g (restored 1990); Ь softens, ’ blocks softening.",
            "Ten vowel letters: А Е Є И І Ї О У Ю Я.",
            "Arabic numerals 0-9; European punctuation; no q, w, x in native words.",
        ],
        "requirements": [
            "Practice writing the iotated letters Є Ї Ю Я until they are automatic.",
            "Read the letter table aloud top to bottom before moving to the phonology record.",
        ],
        "standards": [
            "Letter inventory follows the modern 33-letter standard (ґ restored 1990) as described in Pugh and Press 1999.",
            "All example words are Signature-generated teaching choices from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID, CIT_ISO],
        "must_contain": ["33-letter", "Є", "Ї", "Ґ", "Ь", "left-to-right", "ім’я"],
        "sig_lens": (
            "Through the Signature lens the Cyrillic alphabet is a sworn "
            "set of marks: each iotated letter a seal pressed into the "
            "page with its y-glide, ґ the restored vow of the hard g, the "
            "soft sign a whispered covenant that softens without "
            "speaking."
        ),
        "drill": {
            "letters": [ch for ch, _, _ in UKR_ALPHA],
            "vowel_letters": VOWEL_LETTERS,
            "iotated": IOTATED,
            "specials": ["Ґ", "Є", "Ї"],
            "direction": "left-to-right",
            "test_words": ["україна", "мова", "ґрунт", "їжак", "ім’я",
                           "щастя", "день", "вода"],
        },
    },
    {
        "key": "phonology",
        "name": "Ukrainian Pronunciation and Stress",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Ukrainian has six vowel phonemes: а [a], е [ɛ], и [ɪ] (as in "
            "bit), і [i] (as in machine), о [ɔ], у [u]. The letter Е is "
            "always the open е [ɛ] of bed, never the closed e of they; the "
            "letter И is the relaxed и [ɪ], one of the sounds foreigners "
            "must train. Consonants come in hard-soft pairs before the "
            "iotated vowels: ніс (nose) softens its н, while нас (us) keeps "
            "it hard. \n\n"
            "Ukrainian has no tones - pitch never changes a word's meaning. "
            "Instead it has free, mobile stress: the stressed syllable can "
            "fall anywhere in the word, and it is not marked in ordinary "
            "writing. Stress can change meaning, so learners mark it "
            "themselves while studying:\n"
            "  замок (castle) - замок (lock)\n"
            "  мука (flour) - мука (torment)\n"
            "  плачу (I cry) - плачу (I pay)\n\n"
            "Sound changes to know. Voicing assimilation: a consonant takes "
            "the voicing of the next one, as in просьба [прɔзьба] (request) "
            "and легко [лɛгко] (easily). Second palatalization: г к х become "
            "з ц с before the vowel і in noun endings - нога becomes нозі "
            "(on the leg), рука becomes руці (on the hand), муха becomes "
            "мусі (on the fly). Verbs soften д to дж and т to ч in the "
            "first person: ходити (to walk) gives ходжу (I walk), писати "
            "(to write) gives пишу (I write). \n\n"
            "Ten spoken-example words with translations:\n"
            "  хліб - bread\n  вода - water\n  сонце - sun\n  книга - book\n"
            "  вікно - window\n  дерево - tree\n  птах - bird\n"
            "  молоко - milk\n  земля - earth\n  небо - sky\n"
            "  мова - language\n  щастя - happiness\n"
            "  Україна - Ukraine\n  дякую - thank you"
        ),
        "how_it_works": (
            "Ukrainian pronunciation works from the six vowels outward: "
            "fix а е и і о у in the ear first, keeping Е open and И "
            "relaxed. Then learn the hard-soft contrast - the same "
            "consonant is hard before а о у and soft before і and the "
            "iotated letters. Stress is memorized with each word, the way "
            "English speakers memorize it; the minimal pairs замок/замок "
            "and мука/мука prove why. The sound changes are automatic once "
            "the endings are known: add the dative-locative і to a stem in "
            "г к х and it palatalizes by itself; conjugate a verb in д or "
            "т to the first person and it softens by itself. No pitch "
            "patterns to learn - say each word with one clear stressed "
            "syllable and the rest unstressed."
        ),
        "key_points": [
            "Six vowel phonemes: а е и і о у; Е is open [ɛ], И is relaxed [ɪ].",
            "No tones; stress is free and mobile and can change meaning (замок/замок, мука/мука).",
            "Consonants palatalize before і and the iotated letters.",
            "Second palatalization: г→з, к→ц, х→с before і (нога→нозі, рука→руці, муха→мусі).",
            "д→дж and т→ч in first-person verb forms (ходити→ходжу, писати→пишу).",
            "Voicing assimilation: просьба, легко.",
        ],
        "requirements": [
            "Drill the six vowels in pairs (а-о, е-и, і-и) until Е and И are distinct.",
            "Mark stress in every new word for the first month of study.",
        ],
        "standards": [
            "Phoneme inventory follows the standard account in Shevelov 1979 and Pugh and Press 1999.",
            "Example words are Signature-generated teaching choices from attested vocabulary.",
        ],
        "citations": [CIT_SHEVELOV, CIT_PUGH],
        "must_contain": ["six vowel", "замок", "мука", "нозі", "ходжу", "free", "stress"],
        "sig_lens": (
            "Through the Signature lens the six vowels are six sworn notes "
            "and stress is the seal-stamp that chooses the meaning: move "
            "the stamp and the word becomes another word entirely."
        ),
        "drill": {
            "vowel_phonemes": ["a", "ɛ", "ɪ", "i", "ɔ", "u"],
            "vowel_pairs": 15,
            "consonant_phonemes": 22,
            "stress_pairs": [
                ["замок", "замок", "castle", "lock"],
                ["мука", "мука", "flour", "torment"],
                ["плачу", "плачу", "I cry", "I pay"],
            ],
            "palatalize": [["нога", "нозі"], ["рука", "руці"], ["муха", "мусі"]],
            "soften_verbs": [["ходити", "ходжу"], ["писати", "пишу"]],
            "example_words": [
                ["хліб", "bread"], ["вода", "water"], ["сонце", "sun"],
                ["книга", "book"], ["вікно", "window"], ["дерево", "tree"],
                ["птах", "bird"], ["молоко", "milk"], ["земля", "earth"],
                ["небо", "sky"], ["мова", "language"], ["щастя", "happiness"],
                ["Україна", "Ukraine"], ["дякую", "thank you"],
            ],
        },
    },
    {
        "key": "nouns",
        "name": "Core Nouns I: 25 Essential Nouns",
        "group": "Core Vocabulary",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Ukrainian nouns have three genders - masculine, feminine, "
            "neuter - and the gender is usually read straight off the "
            "ending: consonant endings are masculine, -а/-я feminine, "
            "-о/-е neuter. Plurals add -и/-і or, for neuters, change the "
            "ending to -а: вікно becomes вікна. \n\n"
            "25 essential nouns, each with gender and an example sentence:\n"
            "  1. чоловік (m) - man. Чоловік читає газету. - The man is reading the newspaper.\n"
            "  2. жінка (f) - woman. Жінка співає пісню. - The woman is singing a song.\n"
            "  3. дитина (f) - child. Дитина грається у дворі. - The child is playing in the yard.\n"
            "  4. дім (m) - house, home. Наш дім великий. - Our house is big.\n"
            "  5. вода (f) - water. Вода холодна. - The water is cold.\n"
            "  6. хліб (m) - bread. Хліб свіжий. - The bread is fresh.\n"
            "  7. книга (f) - book. Це цікава книга. - This is an interesting book.\n"
            "  8. стіл (m) - table. Книга лежить на столі. - The book is lying on the table.\n"
            "  9. вікно (n) - window. Вікно відчинене. - The window is open.\n"
            "  10. двері (pl) - door. Двері зачинені. - The door is closed.\n"
            "  11. сонце (n) - sun. Сонце світить яскраво. - The sun is shining brightly.\n"
            "  12. місяць (m) - moon, month. Місяць повний. - The moon is full.\n"
            "  13. день (m) - day. День довгий. - The day is long.\n"
            "  14. ніч (f) - night. Ніч тиха. - The night is quiet.\n"
            "  15. рік (m) - year. Рік минув швидко. - The year passed quickly.\n"
            "  16. час (m) - time. Час летить. - Time flies.\n"
            "  17. рука (f) - hand, arm. Рука болить. - My hand hurts.\n"
            "  18. око (n) - eye. Око бачить далеко. - The eye sees far.\n"
            "  19. слово (n) - word. Це важливе слово. - This is an important word.\n"
            "  20. мова (f) - language. Українська мова гарна. - The Ukrainian language is beautiful.\n"
            "  21. друг (m) - friend. Мій друг прийшов. - My friend came.\n"
            "  22. робота (f) - work, job. Робота цікава. - The work is interesting.\n"
            "  23. школа (f) - school. Школа поруч. - The school is nearby.\n"
            "  24. місто (n) - city. Місто велике. - The city is big.\n"
            "  25. країна (f) - country. Україна - моя країна. - Ukraine is my country.\n\n"
            "Plural patterns to memorize:\n"
            "  книжка -> книжки (book -> books)\n"
            "  стіл -> столи (table -> tables)\n"
            "  вікно -> вікна (window -> windows)\n"
            "  море -> моря (sea -> seas)"
        ),
        "how_it_works": (
            "A Ukrainian noun works as a three-part package: stem + gender "
            "+ case ending. Learn the noun with its gender from the start "
            "(чоловік is masculine, жінка feminine, вікно neuter), because "
            "every adjective and pronoun that touches it must agree. The "
            "nominative singular - the dictionary form - is the anchor; "
            "plurals branch from it by the four patterns above. Each "
            "sentence above shows the noun doing real work in the "
            "nominative: subject of бути (to be) or an action verb. Once "
            "these 25 are solid, the grammar-essentials record will bend "
            "them through all seven cases."
        ),
        "key_points": [
            "Three genders: masculine (consonant), feminine (-а/-я), neuter (-о/-е).",
            "25 nouns learned with gender, English gloss, and a translated sentence.",
            "Plural patterns: -и/-і for masc/fem, -а/-я for neuter.",
            "Adjectives and pronouns must agree with noun gender.",
        ],
        "requirements": [
            "Memorize each noun together with its gender - never the word alone.",
            "Say every example sentence aloud; the nominative form must be automatic.",
        ],
        "standards": [
            "Gender and plural assignments follow Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["three genders", "чоловік", "вікно", "книжка", "feminine"],
        "sig_lens": (
            "Through the Signature lens each noun is a sworn vessel with "
            "its gender sealed at birth: masculine, feminine, or neuter, "
            "and every adjective that touches it must bow to the seal."
        ),
        "drill": {
            "nouns": [
                ["чоловік", "man", "m"], ["жінка", "woman", "f"],
                ["дитина", "child", "f"], ["дім", "house", "m"],
                ["вода", "water", "f"], ["хліб", "bread", "m"],
                ["книга", "book", "f"], ["стіл", "table", "m"],
                ["вікно", "window", "n"], ["двері", "door", "pl"],
                ["сонце", "sun", "n"], ["місяць", "moon", "m"],
                ["день", "day", "m"], ["ніч", "night", "f"],
                ["рік", "year", "m"], ["час", "time", "m"],
                ["рука", "hand", "f"], ["око", "eye", "n"],
                ["слово", "word", "n"], ["мова", "language", "f"],
                ["друг", "friend", "m"], ["робота", "work", "f"],
                ["школа", "school", "f"], ["місто", "city", "n"],
                ["країна", "country", "f"],
            ],
            "plurals": [["книжка", "книжки"], ["стіл", "столи"],
                         ["вікно", "вікна"], ["море", "моря"]],
            "sentences": 25,
            "genders": ["m", "f", "n"],
        },
    },
    {
        "key": "verbs",
        "name": "Core Verbs I: 25 Essential Verbs",
        "group": "Core Vocabulary",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Ukrainian verbs come in two conjugations: the first (писати - "
            "пишу, пишеш, пише) and the second (говорити - говорю, "
            "говориш, говорить). The dictionary form is the infinitive in "
            "-ти. Verbs also come in aspect pairs - imperfective for "
            "ongoing action, perfective for completed action: писати / "
            "написати (to write), читати / прочитати (to read). \n\n"
            "25 essential verbs, infinitive + English + example sentence:\n"
            "  1. бути - to be. Я студент. - I am a student.\n"
            "  2. мати - to have. Я маю книгу. - I have a book.\n"
            "  3. робити - to do, make. Я роблю уроки. - I am doing my homework.\n"
            "  4. говорити - to speak. Вона говорить українською. - She speaks Ukrainian.\n"
            "  5. казати - to say, tell. Він каже правду. - He tells the truth.\n"
            "  6. читати - to read. Я читаю книгу. - I am reading a book.\n"
            "  7. писати - to write. Вона пише листа. - She is writing a letter.\n"
            "  8. їсти - to eat. Ми їмо суп. - We are eating soup.\n"
            "  9. пити - to drink. Я п’ю воду. - I am drinking water.\n"
            "  10. спати - to sleep. Дитина спить. - The child is sleeping.\n"
            "  11. йти - to go (on foot). Я йду додому. - I am going home.\n"
            "  12. їхати - to go (by vehicle). Ми їдемо до Києва. - We are going to Kyiv.\n"
            "  13. прийти - to come, arrive. Він прийшов учора. - He came yesterday.\n"
            "  14. знати - to know. Я знаю відповідь. - I know the answer.\n"
            "  15. думати - to think. Я думаю про тебе. - I am thinking about you.\n"
            "  16. любити - to love. Я люблю маму. - I love my mother.\n"
            "  17. хотіти - to want. Я хочу чаю. - I want some tea.\n"
            "  18. могти - to be able. Я можу допомогти. - I can help.\n"
            "  19. бачити - to see. Я бачу сонце. - I see the sun.\n"
            "  20. чути - to hear. Я чую музику. - I hear music.\n"
            "  21. давати - to give. Він дає мені книгу. - He is giving me a book.\n"
            "  22. брати - to take. Я беру олівець. - I am taking a pencil.\n"
            "  23. працювати - to work. Я працюю в школі. - I work at a school.\n"
            "  24. вчитися - to study, learn. Я вчуся добре. - I study well.\n"
            "  25. жити - to live. Ми живемо в Україні. - We live in Ukraine.\n\n"
            "Two conjugations at a glance (present tense):\n"
            "  I conjugation: писати - пишу, пишеш, пише, пишемо, пишете, пишуть\n"
            "  II conjugation: говорити - говорю, говориш, говорить, говоримо, говорите, говорять"
        ),
        "how_it_works": (
            "A Ukrainian verb works as stem + theme vowel + personal "
            "ending. The theme vowel decides the conjugation: -а-/-е- "
            "verbs take the first conjugation endings (-у/-ю, -еш, -е, "
            "-емо, -ете, -уть/-ють), -и- verbs take the second (-у/-ю, -иш, "
            "-ить, -имо, -ите, -ать/-ять). Aspect is the second axis: the "
            "imperfective (писати) paints the action as ongoing or "
            "repeated, the perfective (написати) presents it as a "
            "completed whole, usually with a prefix. The sentences above "
            "use present-tense imperfective forms - the natural starting "
            "point; the tenses record will run the full system."
        ),
        "key_points": [
            "Infinitive in -ти is the dictionary form.",
            "Two conjugations: I (писати - пишеш) and II (говорити - говориш).",
            "Aspect pairs: imperfective (ongoing) vs perfective (completed), often prefix-formed.",
            "25 verbs learned as infinitive + English + translated sentence.",
        ],
        "requirements": [
            "Memorize each verb with its conjugation class and its aspect partner where given.",
            "Conjugate писати and говорити aloud through all six persons daily.",
        ],
        "standards": [
            "Conjugation classes and aspect pairs follow Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["two conjugations", "писати", "говорити", "aspect", "infinitive"],
        "sig_lens": (
            "Through the Signature lens each verb is a sworn engine with "
            "two gears: the imperfective gear that turns without end and "
            "the perfective gear that locks the work complete."
        ),
        "drill": {
            "verbs": [
                ["бути", "to be", "irr"], ["мати", "to have", "I"],
                ["робити", "to do, make", "II"], ["говорити", "to speak", "II"],
                ["казати", "to say, tell", "I"], ["читати", "to read", "I"],
                ["писати", "to write", "I"], ["їсти", "to eat", "irr"],
                ["пити", "to drink", "irr"], ["спати", "to sleep", "II"],
                ["йти", "to go (on foot)", "irr"], ["їхати", "to go (by vehicle)", "I"],
                ["прийти", "to come, arrive", "irr"], ["знати", "to know", "I"],
                ["думати", "to think", "I"], ["любити", "to love", "II"],
                ["хотіти", "to want", "irr"], ["могти", "to be able", "I"],
                ["бачити", "to see", "II"], ["чути", "to hear", "irr"],
                ["давати", "to give", "I"], ["брати", "to take", "I"],
                ["працювати", "to work", "irr"], ["вчитися", "to study", "II"],
                ["жити", "to live", "I"],
            ],
            "conjugations": ["I", "II"],
            "aspect_pairs": [["писати", "написати"], ["читати", "прочитати"],
                             ["робити", "зробити"], ["говорити", "сказати"]],
            "sentences": 25,
        },
    },
    {
        "key": "adjectives",
        "name": "Adjectives and Adverbs",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Ukrainian adjectives agree with their noun in gender, number, "
            "and case: великий дім (big house, masc), велика книга (big "
            "book, fem), велике вікно (big window, neut), великі будинки "
            "(big houses, pl). The masculine dictionary ending is usually "
            "-ий or -ій. Adverbs are mostly built from adjectives: швидко "
            "(quickly) from швидкий (quick). \n\n"
            "25 adjectives with example sentences:\n"
            "  1. великий - big. Великий дім стоїть на горі. - The big house stands on the hill.\n"
            "  2. малий - small. Малий хлопець біжить. - The small boy is running.\n"
            "  3. новий - new. Це нова школа. - This is a new school.\n"
            "  4. старий - old. Старий міст красивий. - The old bridge is beautiful.\n"
            "  5. добрий - good, kind. Добра людина допомагає. - A good person helps.\n"
            "  6. поганий - bad. Погана погода сьогодні. - The weather is bad today.\n"
            "  7. гарний - beautiful, nice. Гарна квітка цвіте. - A beautiful flower is blooming.\n"
            "  8. довгий - long. Довга дорога веде до міста. - A long road leads to the city.\n"
            "  9. короткий - short. Короткий день минув. - The short day has passed.\n"
            "  10. високий - tall, high. Високе дерево росте тут. - A tall tree grows here.\n"
            "  11. низький - low, short. Низький паркан біля дому. - A low fence is by the house.\n"
            "  12. широкий - wide. Широка річка тече. - A wide river is flowing.\n"
            "  13. вузький - narrow. Вузька вулиця темна. - The narrow street is dark.\n"
            "  14. теплий - warm. Тепле молоко смачне. - Warm milk is tasty.\n"
            "  15. холодний - cold. Холодна вода освіжає. - Cold water refreshes.\n"
            "  16. швидкий - fast. Швидкий поїзд їде. - A fast train is going.\n"
            "  17. повільний - slow. Повільна хода втомлює. - A slow walk is tiring.\n"
            "  18. легкий - light, easy. Легке завдання зроблене. - The easy task is done.\n"
            "  19. важкий - heavy, hard. Важка сумка на столі. - The heavy bag is on the table.\n"
            "  20. молодий - young. Молода вчителька усміхається. - The young teacher is smiling.\n"
            "  21. щасливий - happy. Щаслива дитина грається. - The happy child is playing.\n"
            "  22. сумний - sad. Сумна пісня звучить. - A sad song is playing.\n"
            "  23. червоний - red. Червоне яблуко стигле. - The red apple is ripe.\n"
            "  24. синій - blue. Синє небо чисте. - The blue sky is clear.\n"
            "  25. зелений - green. Зелена трава м’яка. - The green grass is soft.\n\n"
            "15 adverbs with example sentences:\n"
            "  1. швидко - quickly. Він біжить швидко. - He runs quickly.\n"
            "  2. повільно - slowly. Вона говорить повільно. - She speaks slowly.\n"
            "  3. добре - well. Ти співаєш добре. - You sing well.\n"
            "  4. погано - badly. Він пише погано. - He writes badly.\n"
            "  5. дуже - very. Дуже гарний день! - A very nice day!\n"
            "  6. завжди - always. Я завжди рано встаю. - I always get up early.\n"
            "  7. ніколи - never. Я ніколи не спізнююсь. - I am never late.\n"
            "  8. часто - often. Ми часто гуляємо. - We often take walks.\n"
            "  9. рідко - rarely. Він рідко телефонує. - He rarely calls.\n"
            "  10. тут - here. Книга тут. - The book is here.\n"
            "  11. там - there. Дім там. - The house is there.\n"
            "  12. сьогодні - today. Сьогодні тепло. - It is warm today.\n"
            "  13. учора - yesterday. Учора був дощ. - It rained yesterday.\n"
            "  14. завтра - tomorrow. Завтра буде сонце. - It will be sunny tomorrow.\n"
            "  15. разом - together. Ми працюємо разом. - We work together."
        ),
        "how_it_works": (
            "An adjective works as a mirror of its noun: take the stem "
            "(велик-, нов-), then attach the ending that matches the "
            "noun's gender, number, and case - -ий for masculine "
            "nominative, -а/-я for feminine, -е/-є for neuter, -і for "
            "plural. Soft stems (синій, ending in -ій) take the soft "
            "series -я, -є, -і. Adverbs stand outside this system: they "
            "never change, and most are built by swapping the adjective's "
            "-ий for -о (швидкий -> швидко). The sentences above always "
            "pair each adjective with a noun whose gender forces the "
            "right ending, training the agreement reflex."
        ),
        "key_points": [
            "Adjectives agree with nouns in gender, number, and case.",
            "Masculine -ий/-ій, feminine -а/-я, neuter -е/-є, plural -і.",
            "Adverbs do not change; most derive from adjectives (швидкий -> швидко).",
            "25 adjectives + 15 adverbs, each with a translated sentence.",
        ],
        "requirements": [
            "Decline великий through masculine, feminine, neuter, and plural nominative aloud.",
            "Build the adverb from each new adjective you learn.",
        ],
        "standards": [
            "Agreement rules follow Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["agree", "великий", "швидко", "-ий", "adverbs"],
        "sig_lens": (
            "Through the Signature lens each adjective is a sworn mirror: "
            "hold it to a noun and it takes the noun's own face - its "
            "gender, its number, its case."
        ),
        "drill": {
            "adjectives": 25,
            "adverbs": 15,
            "endings": {"m": ["-ий", "-ій"], "f": ["-а", "-я"],
                        "n": ["-е", "-є"], "pl": ["-і"]},
            "pairs": [["швидкий", "швидко"], ["повільний", "повільно"],
                      ["добрий", "добре"], ["теплий", "тепло"]],
            "sentences": 40,
        },
    },
    {
        "key": "pronouns",
        "name": "Pronouns: Personal, Possessive, Demonstrative, Interrogative",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Ukrainian pronouns decline through the seven cases, so each "
            "pronoun is really a small table. Learn the nominative first, "
            "then the accusative and genitive forms that appear in the "
            "sentences below. \n\n"
            "Personal pronouns (nominative -> accusative/genitive):\n"
            "  я (мене) - I (me). Я бачу тебе. - I see you.\n"
            "  ти (тебе) - you singular informal (you). Ти знаєш мене. - You know me.\n"
            "  він (його) - he (him). Він любить її. - He loves her.\n"
            "  вона (її) - she (her). Вона кличе його. - She is calling him.\n"
            "  воно (його) - it (it). Воно лежить тут. - It is lying here.\n"
            "  ми (нас) - we (us). Ми чекаємо на вас. - We are waiting for you.\n"
            "  ви (вас) - you plural/formal (you). Ви читаєте нас? - Are you reading us?\n"
            "  вони (їх) - they (them). Вони бачать нас. - They see us.\n\n"
            "The formal you is ви with a capital Ви in writing: Ви говорите "
            "українською? - Do you (formal) speak Ukrainian? The informal ти "
            "is for friends, family, and children. \n\n"
            "Possessive pronouns (my, your, his/her, our, their):\n"
            "  мій / моя / моє / мої - my. Моя книга тут. - My book is here.\n"
            "  твій / твоя / твоє / твої - your (informal). Твій дім великий. - Your house is big.\n"
            "  його / її - his / her (indeclinable). Його брат прийшов. - His brother came.\n"
            "  наш / наша / наше / наші - our. Наша школа нова. - Our school is new.\n"
            "  ваш / ваша / ваше / ваші - your (formal/plural). Ваше ім’я? - Your name?\n"
            "  їхній / їхня / їхнє / їхні - their. Їхній син студент. - Their son is a student.\n\n"
            "Demonstrative pronouns:\n"
            "  цей / ця / це / ці - this. Ця квітка гарна. - This flower is beautiful.\n"
            "  той / та / те / ті - that. Той дім старий. - That house is old.\n\n"
            "Interrogative pronouns:\n"
            "  хто - who. Хто це? - Who is this?\n"
            "  що - what. Що це? - What is this?\n"
            "  який / яка / яке - which, what kind. Яка це книга? - What kind of book is this?\n"
            "  чий / чия / чиє - whose. Чия це сумка? - Whose bag is this?\n"
            "  скільки - how many. Скільки тобі років? - How old are you?"
        ),
        "how_it_works": (
            "A pronoun works as a stand-in that carries case: я becomes "
            "мене in the accusative and genitive, ти becomes тебе, він "
            "becomes його - the sentence Я бачу тебе (I see you) proves "
            "both forms at once. Possessives behave like adjectives and "
            "agree with the possessed noun (мій брат but моя сестра). "
            "Demonstratives point near (цей) or far (той) and agree the "
            "same way. Interrogatives open questions and decline too: "
            "кого (whom), чого (of what). The ти/ви split runs through "
            "the whole language - verbs, commands, and possessives all "
            "shift with it."
        ),
        "key_points": [
            "Eight personal pronouns; accusative/genitive forms differ (я->мене, ти->тебе, він->його).",
            "ти is informal singular; ви is plural and formal singular.",
            "Possessives agree with the possessed noun (мій/моя/моє/мої); його/її are indeclinable.",
            "цей (this) vs той (that); interrogatives хто, що, який, чий, скільки.",
        ],
        "requirements": [
            "Recite the personal pronouns with their accusative forms until automatic.",
            "Practice the ти/ви switch: address one friend as ти, one elder as ви.",
        ],
        "standards": [
            "Pronoun paradigms follow Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["мене", "тебе", "ти", "ви", "цей", "хто"],
        "sig_lens": (
            "Through the Signature lens each pronoun is a sworn mask the "
            "speaker wears: я for the self, ти for the friend, Ви for the "
            "elder - and the mask changes its face with every case."
        ),
        "drill": {
            "personal": [["я", "мене"], ["ти", "тебе"], ["він", "його"],
                         ["вона", "її"], ["воно", "його"], ["ми", "нас"],
                         ["ви", "вас"], ["вони", "їх"]],
            "possessive_sets": 6,
            "demonstratives": [["цей", "ця", "це", "ці"], ["той", "та", "те", "ті"]],
            "interrogatives": ["хто", "що", "який", "чий", "скільки"],
            "sentences": 21,
        },
    },
    {
        "key": "numbers",
        "name": "Numbers and Time",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Ukrainian numbers agree in gender with what they count: один "
            "(one, masc), одна (fem), одне (neut); два (two, masc/neut), "
            "дві (fem). They also decline through the cases. \n\n"
            "Cardinal numbers 1-20:\n"
            "  1 один/одна/одне, 2 два/дві, 3 три, 4 чотири, 5 п’ять,\n"
            "  6 шість, 7 сім, 8 вісім, 9 дев’ять, 10 десять,\n"
            "  11 одинадцять, 12 дванадцять, 13 тринадцять, 14 чотирнадцять,\n"
            "  15 п’ятнадцять, 16 шістнадцять, 17 сімнадцять, 18 вісімнадцять,\n"
            "  19 дев’ятнадцять, 20 двадцять\n\n"
            "Tens and hundreds: 30 тридцять, 40 сорок, 50 п’ятдесят, "
            "60 шістдесят, 70 сімдесят, 80 вісімдесят, 90 дев’яносто, "
            "100 сто, 1000 тисяча, 1 000 000 мільйон. \n\n"
            "Ordinals: перший (first), другий (second), третій (third), "
            "четвертий, п’ятий, шостий, сьомий, восьмий, дев’ятий, "
            "десятий. \n\n"
            "Days of the week: понеділок (Monday), вівторок (Tuesday), "
            "середа (Wednesday), четвер (Thursday), п’ятниця (Friday), "
            "субота (Saturday), неділя (Sunday). \n\n"
            "Months: січень (January), лютий (February), березень "
            "(March), квітень (April), травень (May), червень (June), "
            "липень (July), серпень (August), вересень (September), "
            "жовтень (October), листопад (November), грудень (December). "
            "Seasons: весна (spring), літо (summer), осінь (autumn), зима "
            "(winter). \n\n"
            "Clock time: година (hour), хвилина (minute). Третя година - "
            "three o'clock. Пів на четверту - half past three (half to "
            "the fourth). Чверть на четверту - quarter past three. \n\n"
            "Example sentences:\n"
            "  У мене два брати. - I have two brothers.\n"
            "  Сьогодні понеділок. - Today is Monday.\n"
            "  Мій день народження у травні. - My birthday is in May.\n"
            "  Зараз третя година. - It is three o'clock now.\n"
            "  Вона прийде о пів на п’яту. - She will come at half past four.\n"
            "  У році дванадцять місяців. - There are twelve months in a year."
        ),
        "how_it_works": (
            "A Ukrainian number works as a counter with manners: 1 agrees "
            "fully (один брат, одна сестра, одне вікно), 2 splits by "
            "gender (два брати, дві сестри), 3 and 4 take the genitive "
            "singular (три брати), and 5 and above take the genitive "
            "plural (п’ять братів). Ordinals behave exactly like "
            "adjectives. Days and months are ordinary nouns with their "
            "own genders - понеділок is masculine, середа feminine. "
            "Clock time counts the coming hour: пів на четверту literally "
            "means half toward the fourth, i.e. 3:30."
        ),
        "key_points": [
            "один/одна/одне, два/дві: numbers agree in gender.",
            "Case government: 2-4 + genitive singular, 5+ + genitive plural.",
            "Ordinals decline like adjectives (перший, другий, третій).",
            "Seven days, twelve months, four seasons; clock counts the coming hour.",
        ],
        "requirements": [
            "Count 1-20 aloud daily until the teens are automatic.",
            "Say the current time in Ukrainian every time you check the clock.",
        ],
        "standards": [
            "Numeral forms and government follow Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["один", "одна", "два", "дві", "понеділок", "година"],
        "sig_lens": (
            "Through the Signature lens each number is a sworn counter "
            "that bows to what it counts: one brother is один, one sister "
            "is одна, and the counter changes its own face to honor them."
        ),
        "drill": {
            "cardinals_1_20": 20,
            "tens": ["тридцять", "сорок", "п’ятдесят", "шістдесят",
                     "сімдесят", "вісімдесят", "дев’яносто", "сто"],
            "gendered": [["один", "одна", "одне"], ["два", "дві"]],
            "ordinals": ["перший", "другий", "третій", "четвертий", "п’ятий"],
            "days": ["понеділок", "вівторок", "середа", "четвер",
                     "п’ятниця", "субота", "неділя"],
            "months": ["січень", "лютий", "березень", "квітень", "травень",
                       "червень", "липень", "серпень", "вересень",
                       "жовтень", "листопад", "грудень"],
            "seasons": ["весна", "літо", "осінь", "зима"],
            "sentences": 6,
        },
    },
    {
        "key": "greetings",
        "name": "Greetings and Everyday Phrases",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Ukrainian greetings change with the time of day and with the "
            "ти/ви line between informal and formal speech. \n\n"
            "30 greetings, farewells, and politeness phrases:\n"
            "  1. Привіт! - Hi! (informal)\n"
            "  2. Доброго ранку! - Good morning!\n"
            "  3. Добрий день! - Good day! (midday hello, works formally)\n"
            "  4. Добрий вечір! - Good evening!\n"
            "  5. На добраніч! - Good night! (before sleep)\n"
            "  6. Як справи? - How are things?\n"
            "  7. Як ти? - How are you? (informal)\n"
            "  8. Як ви? - How are you? (formal)\n"
            "  9. Добре, дякую. - Fine, thank you.\n"
            "  10. Дуже добре! - Very well!\n"
            "  11. Так собі. - So-so.\n"
            "  12. Дякую! - Thank you!\n"
            "  13. Дуже дякую! - Thank you very much!\n"
            "  14. Будь ласка! - Please! / You're welcome!\n"
            "  15. Прошу! - Here you are! / Please come in!\n"
            "  16. Вибачте! - Excuse me! / Sorry! (formal)\n"
            "  17. Вибач! - Sorry! (informal)\n"
            "  18. Перепрошую! - Excuse me! (getting attention)\n"
            "  19. Нічого страшного. - No problem. / It's nothing.\n"
            "  20. До побачення! - Goodbye! (formal)\n"
            "  21. Бувай! - Bye! (informal singular)\n"
            "  22. Бувайте! - Bye! (informal plural / formal)\n"
            "  23. До зустрічі! - See you! / Until we meet!\n"
            "  24. Щасливо! - Good luck! / Take care!\n"
            "  25. Ласкаво просимо! - Welcome!\n"
            "  26. Радий познайомитися! - Nice to meet you! (man speaking)\n"
            "  27. Рада познайомитися! - Nice to meet you! (woman speaking)\n"
            "  28. Смачного! - Enjoy your meal!\n"
            "  29. На здоров’я! - Cheers! / Bless you! (after a sneeze)\n"
            "  30. Вітаю! - Congratulations! / Greetings!\n\n"
            "Usage notes. Добрий день doubles as the standard polite hello "
            "at any hour of the working day - shopkeepers say it to every "
            "customer. Смачного is said to people who are eating, even "
            "strangers. На здоров’я answers both a toast and a sneeze. "
            "Men say радий, women say рада - the greeting itself agrees "
            "with the speaker's gender. Привіт and бувай stay on the "
            "informal side of the line; with elders and strangers, use "
            "добрий день and до побачення."
        ),
        "how_it_works": (
            "A greeting works as a social key: the right phrase opens the "
            "right door. Time-of-day greetings (доброго ранку, добрий "
            "день, добрий вечір) track the clock; register greetings "
            "(привіт vs добрий день, бувай vs до побачення) track the "
            "relationship. Будь ласка is the universal lubricant - please, "
            "you're welcome, here you go, after you. Learn the set as "
            "whole phrases first, then notice the grammar inside: доброго "
            "ранку is the genitive case (of a good morning), на добраніч "
            "is a prepositional phrase (for the good night)."
        ),
        "key_points": [
            "Greetings track time of day (доброго ранку / добрий день / добрий вечір) and register (ти vs ви).",
            "Будь ласка = please / you're welcome / here you go.",
            "Смачного to people eating; на здоров’я for toasts and sneezes.",
            "Радий (man) / рада (woman): the greeting agrees with the speaker.",
            "30 phrases with English and usage notes.",
        ],
        "requirements": [
            "Greet someone in Ukrainian every day for a week, matching the time of day.",
            "Practice the formal set (добрий день, до побачення) separately from the informal set.",
        ],
        "standards": [
            "Phrases are standard literary Ukrainian per Pugh and Press 1999.",
            "Usage notes are Signature-generated teaching guidance.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["Привіт", "Добрий день", "Будь ласка", "Смачного", "до побачення"],
        "sig_lens": (
            "Through the Signature lens each greeting is a sworn key cut "
            "for its door: the morning key, the evening key, the friend's "
            "key, the elder's key - and the wrong key never turns."
        ),
        "drill": {
            "phrases": 30,
            "time_of_day": ["Доброго ранку", "Добрий день", "Добрий вечір", "На добраніч"],
            "formal": ["Добрий день", "До побачення", "Вибачте", "Перепрошую"],
            "informal": ["Привіт", "Бувай", "Вибач"],
            "gendered": [["Радий", "m"], ["Рада", "f"]],
        },
    },
    {
        "key": "grammar",
        "name": "Grammar Essentials: The Ten Load-Bearing Rules",
        "group": "Grammar Essentials",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Ten rules carry the whole weight of Ukrainian grammar. Learn "
            "these and every sentence in this database becomes readable. \n\n"
            "  Rule 1 - Word order is subject-verb-object, but flexible. "
            "Я читаю книгу. - I am reading a book. Книгу читаю я. - It is I who am reading the book (emphasis on the subject).\n"
            "  Rule 2 - Three genders: masculine, feminine, neuter. "
            "Дім (m), книга (f), вікно (n). Adjectives and past-tense verbs agree: він читав, вона читала, воно читало.\n"
            "  Rule 3 - Seven cases bend every noun. Називний (nominative): "
            "хто? що? - книга. Родовий (genitive): кого? чого? - книги. "
            "Давальний (dative): кому? чому? - книзі. Знахідний "
            "(accusative): кого? що? - книгу. Орудний (instrumental): ким? "
            "чим? - книгою. Місцевий (locative): на кому? на чому? - на "
            "книзі. Кличний (vocative): - книго! (O book!)\n"
            "  Rule 4 - No articles. Книга means the book or a book - "
            "context decides: Я бачу книгу. - I see the book / a book.\n"
            "  Rule 5 - Negation is не before the verb, and double "
            "negation is required: Я не знаю. - I do not know. Я нічого "
            "не знаю. - I know nothing (literally: I nothing do not know). "
            "Немає means there is not: Немає часу. - There is no time.\n"
            "  Rule 6 - Questions use intonation, the particle чи, or a "
            "question word. Ти читаєш? - Are you reading? Чи ти читаєш? - "
            "Do you read? Що ти читаєш? - What are you reading?\n"
            "  Rule 7 - Adjectives agree with nouns in gender, number, "
            "case: новий дім, нова книга, нове вікно, нові будинки.\n"
            "  Rule 8 - Verbs conjugate for person and number; past tense "
            "agrees in gender and number: я писав (man) / я писала "
            "(woman) / ми писали (we).\n"
            "  Rule 9 - Aspect: imperfective for ongoing or repeated "
            "action, perfective for completed: я читав книгу (I was "
            "reading) vs я прочитав книгу (I have read / finished the book).\n"
            "  Rule 10 - The vocative addresses people directly: друже! "
            "(friend!), мамо! (mom!), пане! (sir!). Олено, де ти? - Olena, where are you?"
        ),
        "how_it_works": (
            "These ten rules work as the operating system of the language. "
            "Rules 1-4 build the noun phrase (order, gender, case, no "
            "articles); rules 5-6 build negation and questions; rules 7-8 "
            "wire agreement between adjectives, verbs, and nouns; rule 9 "
            "adds the aspect axis to every verb; rule 10 opens direct "
            "address. Every themed sentence set in this database is "
            "generated by these rules: pick a noun, bend it to its case, "
            "agree the adjective, conjugate the verb, choose the aspect. "
            "The later records (tenses, questions, commands, complex "
            "sentences) are these same ten rules running at higher speed."
        ),
        "key_points": [
            "SVO word order, flexible for emphasis.",
            "Three genders; adjectives and past verbs agree.",
            "Seven cases: nominative, genitive, dative, accusative, instrumental, locative, vocative.",
            "No articles; double negation required; questions by intonation, чи, or question words.",
            "Aspect: imperfective (ongoing) vs perfective (completed).",
            "Vocative for direct address: друже!, мамо!, пане!",
        ],
        "requirements": [
            "Decline книга through all seven cases aloud before moving on.",
            "Write five negations with double negation (ніхто не, нічого не).",
        ],
        "standards": [
            "Case system and rules follow Pugh and Press 1999 and Bilodid 1969.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID, CIT_SHEVELOV],
        "must_contain": ["Seven cases", "Кличний", "Немає", "чи", "друже"],
        "sig_lens": (
            "Through the Signature lens these ten rules are the ten sworn "
            "pillars of the temple: gender the first, case the sevenfold "
            "arch, aspect the twin torches that light every verb."
        ),
        "drill": {
            "rules": 10,
            "cases": ["називний", "родовий", "давальний", "знахідний",
                      "орудний", "місцевий", "кличний"],
            "case_forms": ["книга", "книги", "книзі", "книгу", "книгою",
                           "книзі", "книго"],
            "genders": ["m", "f", "n"],
            "aspects": ["imperfective", "perfective"],
        },
    },
    {
        "key": "home",
        "name": "Home and Family Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "20 sentences about the house, its rooms, its furniture, and "
            "the family inside it:\n"
            "  1. Це наш дім. - This is our house.\n"
            "  2. У домі чотири кімнати. - There are four rooms in the house.\n"
            "  3. Кухня велика і світла. - The kitchen is big and bright.\n"
            "  4. Мама готує обід на кухні. - Mom is cooking lunch in the kitchen.\n"
            "  5. Вітальня затишна. - The living room is cozy.\n"
            "  6. Тато читає газету у вітальні. - Dad is reading the newspaper in the living room.\n"
            "  7. Спальня на другому поверсі. - The bedroom is on the second floor.\n"
            "  8. Ліжко біля вікна. - The bed is by the window.\n"
            "  9. У ванній кімнаті тепло. - It is warm in the bathroom.\n"
            "  10. Стіл стоїть посеред кімнати. - The table stands in the middle of the room.\n"
            "  11. На столі лежить книга. - A book is lying on the table.\n"
            "  12. Стілець біля столу. - The chair is by the table.\n"
            "  13. У нас велика сім’я. - We have a big family.\n"
            "  14. Мій брат старший за мене. - My brother is older than me.\n"
            "  15. Моя сестра вчиться в університеті. - My sister studies at the university.\n"
            "  16. Дідусь розповідає казки. - Grandfather tells fairy tales.\n"
            "  17. Бабуся пече пироги. - Grandmother bakes pies.\n"
            "  18. Наш кіт спить на дивані. - Our cat is sleeping on the sofa.\n"
            "  19. Собака гавкає у дворі. - The dog is barking in the yard.\n"
            "  20. Увечері вся сім’я збирається разом. - In the evening the whole family gathers together."
        ),
        "how_it_works": (
            "These sentences work as a walk through the house: each room "
            "is named in the locative case (на кухні, у вітальні, на "
            "другому поверсі), each family member in the nominative as "
            "the actor. The prepositions у/в (in) and на (on) govern the "
            "locative for location - a pattern that repeats in every "
            "record of this database. Possessives (наш, мій, моя) agree "
            "with their nouns, drilling the adjective agreement rule in "
            "real rooms."
        ),
        "key_points": [
            "Rooms: кухня, вітальня, спальня, ванна кімната.",
            "Location uses у/в + locative: на кухні, у вітальні.",
            "Family: мама, тато, брат, сестра, дідусь, бабуся.",
            "20 sentences, each in Ukrainian with English translation.",
        ],
        "requirements": [
            "Describe your own home aloud using these sentence frames.",
            "Name five family members with possessives (мій брат, моя сестра).",
        ],
        "standards": [
            "Vocabulary is standard literary Ukrainian per Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["кухні", "вітальні", "Дідусь", "Бабуся", "сім’я"],
        "sig_lens": (
            "Through the Signature lens the house is a sworn hall with "
            "seven doors: each room a chamber of meaning, each family "
            "member a keeper of its covenant."
        ),
        "drill": {
            "sentences": [
                ["Це наш дім.", "This is our house."],
                ["У домі чотири кімнати.", "There are four rooms in the house."],
                ["Кухня велика і світла.", "The kitchen is big and bright."],
                ["Мама готує обід на кухні.", "Mom is cooking lunch in the kitchen."],
                ["Вітальня затишна.", "The living room is cozy."],
                ["Тато читає газету у вітальні.", "Dad is reading the newspaper in the living room."],
                ["Спальня на другому поверсі.", "The bedroom is on the second floor."],
                ["Ліжко біля вікна.", "The bed is by the window."],
                ["У ванній кімнаті тепло.", "It is warm in the bathroom."],
                ["Стіл стоїть посеред кімнати.", "The table stands in the middle of the room."],
                ["На столі лежить книга.", "A book is lying on the table."],
                ["Стілець біля столу.", "The chair is by the table."],
                ["У нас велика сім’я.", "We have a big family."],
                ["Мій брат старший за мене.", "My brother is older than me."],
                ["Моя сестра вчиться в університеті.", "My sister studies at the university."],
                ["Дідусь розповідає казки.", "Grandfather tells fairy tales."],
                ["Бабуся пече пироги.", "Grandmother bakes pies."],
                ["Наш кіт спить на дивані.", "Our cat is sleeping on the sofa."],
                ["Собака гавкає у дворі.", "The dog is barking in the yard."],
                ["Увечері вся сім’я збирається разом.", "In the evening the whole family gathers together."],
            ],
            "rooms": ["кухня", "вітальня", "спальня", "ванна кімната"],
        },
    },
    {
        "key": "food",
        "name": "Food and Cooking Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences about meals, ingredients, cooking, and the "
            "restaurant:\n"
            "  1. Сніданок о восьмій ранку. - Breakfast is at eight in the morning.\n"
            "  2. Я їм кашу з молоком. - I am eating porridge with milk.\n"
            "  3. Хліб свіжий і теплий. - The bread is fresh and warm.\n"
            "  4. Мама варить борщ. - Mom is cooking borscht.\n"
            "  5. Борщ червоний від буряка. - Borscht is red from the beetroot.\n"
            "  6. Додай сметани, будь ласка. - Add some sour cream, please.\n"
            "  7. Вареники з картоплею - моя улюблена страва. - Varenyky with potatoes is my favorite dish.\n"
            "  8. Бабуся ліпить вареники. - Grandmother is making varenyky.\n"
            "  9. Сало з часником дуже смачне. - Salo with garlic is very tasty.\n"
            "  10. Наріж овочі для салату. - Chop the vegetables for the salad.\n"
            "  11. Суп кипить на плиті. - The soup is boiling on the stove.\n"
            "  12. Посоли суп трохи. - Salt the soup a little.\n"
            "  13. Обід готовий! - Lunch is ready!\n"
            "  14. Смачного всім! - Enjoy your meal, everyone!\n"
            "  15. Я хочу ще чаю. - I want some more tea.\n"
            "  16. Кава гаряча. - The coffee is hot.\n"
            "  17. У ресторані смачна кухня. - The restaurant has tasty food.\n"
            "  18. Офіціанте, принесіть меню! - Waiter, bring the menu!\n"
            "  19. Рахунок, будь ласка. - The bill, please.\n"
            "  20. Вечеря була чудова. - Dinner was wonderful."
        ),
        "how_it_works": (
            "These sentences work as a meal from morning to night: the "
            "imperatives (додай, наріж, посоли) drill the command forms "
            "that the commands record will systematize; the instrumental "
            "case appears in its natural habitat (з молоком, з картоплею, "
            "з часником - with milk, with potatoes, with garlic). The "
            "national dishes - борщ, вареники, сало - are named with "
            "their real recipes' vocabulary, so the food set doubles as a "
            "culture set."
        ),
        "key_points": [
            "Meals: сніданок, обід, вечеря; national dishes борщ, вареники, сало.",
            "Instrumental case for accompaniment: з молоком, з часником.",
            "Imperatives in the kitchen: додай, наріж, посоли.",
            "Restaurant frames: принесіть меню, рахунок будь ласка.",
            "20 sentences, each in Ukrainian with English translation.",
        ],
        "requirements": [
            "Cook one dish while narrating the steps in Ukrainian.",
            "Order a full meal aloud: menu, dish, bill.",
        ],
        "standards": [
            "Vocabulary is standard literary Ukrainian per Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["борщ", "вареники", "Сало", "Смачного", "Рахунок"],
        "sig_lens": (
            "Through the Signature lens the table is a sworn altar: "
            "борщ the red covenant, вареники the folded vows, сало the "
            "sealed promise of the harvest."
        ),
        "drill": {
            "sentences": [
                ["Сніданок о восьмій ранку.", "Breakfast is at eight in the morning."],
                ["Я їм кашу з молоком.", "I am eating porridge with milk."],
                ["Хліб свіжий і теплий.", "The bread is fresh and warm."],
                ["Мама варить борщ.", "Mom is cooking borscht."],
                ["Борщ червоний від буряка.", "Borscht is red from the beetroot."],
                ["Додай сметани, будь ласка.", "Add some sour cream, please."],
                ["Вареники з картоплею - моя улюблена страва.", "Varenyky with potatoes is my favorite dish."],
                ["Бабуся ліпить вареники.", "Grandmother is making varenyky."],
                ["Сало з часником дуже смачне.", "Salo with garlic is very tasty."],
                ["Наріж овочі для салату.", "Chop the vegetables for the salad."],
                ["Суп кипить на плиті.", "The soup is boiling on the stove."],
                ["Посоли суп трохи.", "Salt the soup a little."],
                ["Обід готовий!", "Lunch is ready!"],
                ["Смачного всім!", "Enjoy your meal, everyone!"],
                ["Я хочу ще чаю.", "I want some more tea."],
                ["Кава гаряча.", "The coffee is hot."],
                ["У ресторані смачна кухня.", "The restaurant has tasty food."],
                ["Офіціанте, принесіть меню!", "Waiter, bring the menu!"],
                ["Рахунок, будь ласка.", "The bill, please."],
                ["Вечеря була чудова.", "Dinner was wonderful."],
            ],
            "dishes": ["борщ", "вареники", "сало"],
        },
    },
    {
        "key": "travel",
        "name": "Travel and Directions Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences about transport, asking directions, tickets, and "
            "lodging:\n"
            "  1. Я їду до Києва. - I am going to Kyiv.\n"
            "  2. Поїзд відправляється о десятій. - The train departs at ten.\n"
            "  3. Де вокзал? - Where is the train station?\n"
            "  4. Як дістатися до центру? - How do I get to the center?\n"
            "  5. Ідіть прямо, потім наліво. - Go straight, then left.\n"
            "  6. Це далеко звідси? - Is it far from here?\n"
            "  7. Ні, це поруч, п’ять хвилин пішки. - No, it is nearby, five minutes on foot.\n"
            "  8. Де зупинка автобуса? - Where is the bus stop?\n"
            "  9. Який автобус їде до музею? - Which bus goes to the museum?\n"
            "  10. Два квитки до Львова, будь ласка. - Two tickets to Lviv, please.\n"
            "  11. Скільки коштує квиток? - How much is the ticket?\n"
            "  12. Літак прилітає вчасно. - The plane is arriving on time.\n"
            "  13. Мій рейс затримується. - My flight is delayed.\n"
            "  14. Де мій багаж? - Where is my luggage?\n"
            "  15. Готель біля моря. - The hotel is by the sea.\n"
            "  16. У вас є вільні номери? - Do you have free rooms?\n"
            "  17. Мені потрібен номер на двох. - I need a double room.\n"
            "  18. Сніданок включено? - Is breakfast included?\n"
            "  19. Таксі! Відвезіть мене в аеропорт. - Taxi! Take me to the airport.\n"
            "  20. Дякую, подорож була чудова! - Thank you, the trip was wonderful!"
        ),
        "how_it_works": (
            "These sentences work as a complete journey: departure (поїзд "
            "відправляється), navigation (як дістатися, ідіть прямо), "
            "tickets (два квитки), flight (рейс затримується), and lodging "
            "(вільні номери). Motion verbs split by vehicle - йти/їхати, "
            "прийти/приїхати - and the questions drill the interrogative "
            "set (де, як, який, скільки) in the situations where "
            "travelers actually need them. Prepositions до (to) and в/у "
            "(into) govern the genitive and accusative of destination."
        ),
        "key_points": [
            "Motion verbs: йти (on foot) vs їхати (by vehicle).",
            "Directions: прямо, наліво, направо, поруч, далеко.",
            "Travel questions: де, як дістатися, скільки коштує.",
            "Tickets and hotel frames: два квитки, вільні номери, сніданок включено.",
            "20 sentences, each in Ukrainian with English translation.",
        ],
        "requirements": [
            "Give directions from your home to the nearest station aloud.",
            "Buy a ticket and book a room in a role-play.",
        ],
        "standards": [
            "Vocabulary is standard literary Ukrainian per Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["вокзал", "квитки", "Готель", "прямо", "наліво"],
        "sig_lens": (
            "Through the Signature lens the journey is a sworn road: "
            "every direction a sealed instruction, every ticket a "
            "covenant of arrival."
        ),
        "drill": {
            "sentences": [
                ["Я їду до Києва.", "I am going to Kyiv."],
                ["Поїзд відправляється о десятій.", "The train departs at ten."],
                ["Де вокзал?", "Where is the train station?"],
                ["Як дістатися до центру?", "How do I get to the center?"],
                ["Ідіть прямо, потім наліво.", "Go straight, then left."],
                ["Це далеко звідси?", "Is it far from here?"],
                ["Ні, це поруч, п’ять хвилин пішки.", "No, it is nearby, five minutes on foot."],
                ["Де зупинка автобуса?", "Where is the bus stop?"],
                ["Який автобус їде до музею?", "Which bus goes to the museum?"],
                ["Два квитки до Львова, будь ласка.", "Two tickets to Lviv, please."],
                ["Скільки коштує квиток?", "How much is the ticket?"],
                ["Літак прилітає вчасно.", "The plane is arriving on time."],
                ["Мій рейс затримується.", "My flight is delayed."],
                ["Де мій багаж?", "Where is my luggage?"],
                ["Готель біля моря.", "The hotel is by the sea."],
                ["У вас є вільні номери?", "Do you have free rooms?"],
                ["Мені потрібен номер на двох.", "I need a double room."],
                ["Сніданок включено?", "Is breakfast included?"],
                ["Таксі! Відвезіть мене в аеропорт.", "Taxi! Take me to the airport."],
                ["Дякую, подорож була чудова!", "Thank you, the trip was wonderful!"],
            ],
            "directions": ["прямо", "наліво", "далеко", "поруч"],
        },
    },
    {
        "key": "work",
        "name": "Work and School Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences about jobs, the office, the classroom, and learning:\n"
            "  1. Я працюю інженером. - I work as an engineer.\n"
            "  2. Вона лікар у поліклініці. - She is a doctor at the clinic.\n"
            "  3. Мій офіс у центрі міста. - My office is in the city center.\n"
            "  4. Робочий день починається о дев’ятій. - The workday starts at nine.\n"
            "  5. У мене важлива зустріч. - I have an important meeting.\n"
            "  6. Надішли мені листа, будь ласка. - Send me the letter, please.\n"
            "  7. Ми обговоримо це завтра. - We will discuss it tomorrow.\n"
            "  8. Діти йдуть до школи. - The children are going to school.\n"
            "  9. Урок починається за п’ять хвилин. - The lesson starts in five minutes.\n"
            "  10. Вчитель пояснює правило. - The teacher is explaining the rule.\n"
            "  11. Учні уважно слухають. - The pupils are listening attentively.\n"
            "  12. Відкрий підручник на десятій сторінці. - Open the textbook to page ten.\n"
            "  13. Напиши вправу в зошиті. - Write the exercise in the notebook.\n"
            "  14. Я отримав гарну оцінку. - I got a good grade.\n"
            "  15. Вона вчиться в університеті. - She studies at the university.\n"
            "  16. Лекція цікава. - The lecture is interesting.\n"
            "  17. Студенти складають іспит. - The students are taking an exam.\n"
            "  18. Я вивчаю українську мову. - I am studying the Ukrainian language.\n"
            "  19. Знання - сила. - Knowledge is power.\n"
            "  20. Праця зробила з мавпи людину. - Labor made a human out of the ape. (common saying)"
        ),
        "how_it_works": (
            "These sentences work as a day split in two: the office half "
            "drills professional vocabulary (зустріч, лист, обговоримо - "
            "the future tense appearing naturally), and the school half "
            "drills classroom imperatives (відкрий, напиши) and learning "
            "verbs (вчитися, вивчати, пояснювати). Instrumental of "
            "profession (працюю інженером - I work as an engineer) shows "
            "the case doing its most idiomatic work. The closing proverbs "
            "prove the vocabulary has entered the culture."
        ),
        "key_points": [
            "Professions in the instrumental: працюю інженером, вона лікар.",
            "Office: зустріч, лист, офіс; school: урок, підручник, зошит, оцінка.",
            "Classroom imperatives: відкрий, напиши.",
            "Learning verbs: вчитися, вивчати, пояснювати.",
            "20 sentences, each in Ukrainian with English translation.",
        ],
        "requirements": [
            "Describe your job or studies in five Ukrainian sentences.",
            "Give three classroom commands aloud.",
        ],
        "standards": [
            "Vocabulary is standard literary Ukrainian per Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["інженером", "підручник", "іспит", "Знання", "оцінку"],
        "sig_lens": (
            "Through the Signature lens work and study are twin sworn "
            "forges: the office hammers the day's iron, the classroom "
            "tempers tomorrow's steel."
        ),
        "drill": {
            "sentences": [
                ["Я працюю інженером.", "I work as an engineer."],
                ["Вона лікар у поліклініці.", "She is a doctor at the clinic."],
                ["Мій офіс у центрі міста.", "My office is in the city center."],
                ["Робочий день починається о дев’ятій.", "The workday starts at nine."],
                ["У мене важлива зустріч.", "I have an important meeting."],
                ["Надішли мені листа, будь ласка.", "Send me the letter, please."],
                ["Ми обговоримо це завтра.", "We will discuss it tomorrow."],
                ["Діти йдуть до школи.", "The children are going to school."],
                ["Урок починається за п’ять хвилин.", "The lesson starts in five minutes."],
                ["Вчитель пояснює правило.", "The teacher is explaining the rule."],
                ["Учні уважно слухають.", "The pupils are listening attentively."],
                ["Відкрий підручник на десятій сторінці.", "Open the textbook to page ten."],
                ["Напиши вправу в зошиті.", "Write the exercise in the notebook."],
                ["Я отримав гарну оцінку.", "I got a good grade."],
                ["Вона вчиться в університеті.", "She studies at the university."],
                ["Лекція цікава.", "The lecture is interesting."],
                ["Студенти складають іспит.", "The students are taking an exam."],
                ["Я вивчаю українську мову.", "I am studying the Ukrainian language."],
                ["Знання - сила.", "Knowledge is power."],
                ["Праця зробила з мавпи людину.", "Labor made a human out of the ape."],
            ],
            "professions": ["інженер", "лікар", "вчитель", "студент"],
        },
    },
    {
        "key": "health",
        "name": "Health and Body Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences about body parts, symptoms, the doctor visit, "
            "and the pharmacy:\n"
            "  1. У мене болить голова. - My head hurts.\n"
            "  2. У нього болить горло. - His throat hurts.\n"
            "  3. Мої очі втомилися. - My eyes are tired.\n"
            "  4. Я відчуваю слабкість. - I feel weakness.\n"
            "  5. У мене температура. - I have a temperature.\n"
            "  6. Мене нудить. - I feel nauseous.\n"
            "  7. У мене болить живіт. - My stomach hurts.\n"
            "  8. Я застудився. - I caught a cold. (man speaking)\n"
            "  9. Вона захворіла на грип. - She got the flu.\n"
            "  10. Треба викликати лікаря. - We need to call a doctor.\n"
            "  11. Лікар оглянув пацієнта. - The doctor examined the patient.\n"
            "  12. Де болить? Покажіть. - Where does it hurt? Show me.\n"
            "  13. Відкрий рота і скажи ааа. - Open your mouth and say ahh.\n"
            "  14. Вам потрібен спокій. - You need rest.\n"
            "  15. Приймайте ліки двічі на день. - Take the medicine twice a day.\n"
            "  16. Де найближча аптека? - Where is the nearest pharmacy?\n"
            "  17. Дайте щось від головного болю. - Give me something for a headache.\n"
            "  18. Рука вже не болить. - The arm does not hurt anymore.\n"
            "  19. Бережіть здоров’я! - Take care of your health!\n"
            "  20. Я одужую. - I am recovering."
        ),
        "how_it_works": (
            "These sentences work as a clinic visit in order: symptoms "
            "(болить голова, температура), diagnosis (застудився, грип), "
            "examination (лікар оглянув, покажіть), prescription "
            "(приймайте ліки), and pharmacy (аптека, від головного болю). "
            "The impersonal construction у мене болить (at me it hurts) "
            "is the idiomatic Ukrainian way to report pain - the body "
            "part, not the person, is the grammatical subject of the "
            "feeling. Imperatives to the patient (покажіть, приймайте) "
            "drill the formal command forms."
        ),
        "key_points": [
            "Pain is impersonal: у мене болить голова (at me the head hurts).",
            "Body: голова, горло, очі, живіт, рука; illness: застуда, грип, температура.",
            "Doctor frames: викликайте лікаря, приймайте ліки.",
            "Pharmacy: аптека, щось від головного болю.",
            "20 sentences, each in Ukrainian with English translation.",
        ],
        "requirements": [
            "Name ten body parts while pointing to them.",
            "Role-play a doctor visit: symptoms, examination, prescription.",
        ],
        "standards": [
            "Vocabulary is standard literary Ukrainian per Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["болить голова", "аптека", "лікаря", "одужую", "температура"],
        "sig_lens": (
            "Through the Signature lens the body is a sworn temple and "
            "every symptom a messenger: the doctor reads the messages, "
            "the medicine seals the covenant of healing."
        ),
        "drill": {
            "sentences": [
                ["У мене болить голова.", "My head hurts."],
                ["У нього болить горло.", "His throat hurts."],
                ["Мої очі втомилися.", "My eyes are tired."],
                ["Я відчуваю слабкість.", "I feel weakness."],
                ["У мене температура.", "I have a temperature."],
                ["Мене нудить.", "I feel nauseous."],
                ["У мене болить живіт.", "My stomach hurts."],
                ["Я застудився.", "I caught a cold."],
                ["Вона захворіла на грип.", "She got the flu."],
                ["Треба викликати лікаря.", "We need to call a doctor."],
                ["Лікар оглянув пацієнта.", "The doctor examined the patient."],
                ["Де болить? Покажіть.", "Where does it hurt? Show me."],
                ["Відкрий рота і скажи ааа.", "Open your mouth and say ahh."],
                ["Вам потрібен спокій.", "You need rest."],
                ["Приймайте ліки двічі на день.", "Take the medicine twice a day."],
                ["Де найближча аптека?", "Where is the nearest pharmacy?"],
                ["Дайте щось від головного болю.", "Give me something for a headache."],
                ["Рука вже не болить.", "The arm does not hurt anymore."],
                ["Бережіть здоров’я!", "Take care of your health!"],
                ["Я одужую.", "I am recovering."],
            ],
            "body_parts": ["голова", "горло", "очі", "живіт", "рука", "рот"],
        },
    },
    {
        "key": "emotions",
        "name": "Emotions and Feelings Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences about being happy, sad, angry, afraid, in love, "
            "and surprised:\n"
            "  1. Я щасливий! - I am happy! (man speaking)\n"
            "  2. Вона щаслива сьогодні. - She is happy today.\n"
            "  3. Ми раді тебе бачити. - We are glad to see you.\n"
            "  4. Це чудова новина! - This is wonderful news!\n"
            "  5. Я сумую за домом. - I miss home.\n"
            "  6. Він сумний через дощ. - He is sad because of the rain.\n"
            "  7. Не плач, усе буде добре. - Don't cry, everything will be fine.\n"
            "  8. Я сердитий на нього. - I am angry at him. (man speaking)\n"
            "  9. Вона розлючена! - She is furious!\n"
            "  10. Заспокойся, будь ласка. - Calm down, please.\n"
            "  11. Я боюся темряви. - I am afraid of the dark.\n"
            "  12. Не бійся, я поруч. - Don't be afraid, I am nearby.\n"
            "  13. Я кохаю тебе. - I love you (romantic).\n"
            "  14. Я люблю свою сім’ю. - I love my family.\n"
            "  15. Вони одружилися влітку. - They got married in the summer.\n"
            "  16. Я здивований! - I am surprised! (man speaking)\n"
            "  17. Яка несподіванка! - What a surprise!\n"
            "  18. Мені соромно. - I am ashamed.\n"
            "  19. Я пишаюся тобою. - I am proud of you.\n"
            "  20. Спокій - це сила. - Calmness is strength."
        ),
        "how_it_works": (
            "These sentences work as the emotional spectrum: joy "
            "(щасливий, раді), sorrow (сумую, сумний, не плач), anger "
            "(сердитий, розлючена, заспокойся), fear (боюся, не бійся), "
            "love (кохаю for romance, люблю for family and things), "
            "surprise (здивований, несподіванка), shame and pride "
            "(соромно, пишаюся). Short adjectives (раді, соромно) and "
            "impersonal constructions (мені соромно) show the two "
            "Ukrainian ways of stating feelings - as a property of the "
            "person or as a state that has come over them."
        ),
        "key_points": [
            "кохати = romantic love; любити = love for family, things, ideas.",
            "Emotions as adjectives (щасливий) or impersonal states (мені соромно).",
            "Comfort frames: не плач, заспокойся, не бійся.",
            "20 sentences, each in Ukrainian with English translation.",
        ],
        "requirements": [
            "Say how you feel right now in Ukrainian, then say the opposite.",
            "Comfort a friend aloud: не плач, усе буде добре.",
        ],
        "standards": [
            "Vocabulary is standard literary Ukrainian per Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["щасливий", "кохаю", "боюся", "пишаюся", "сумую"],
        "sig_lens": (
            "Through the Signature lens every feeling is a sworn weather "
            "of the soul: joy the sunrise, sorrow the rain, anger the "
            "thunder, love the deep river that never dries."
        ),
        "drill": {
            "sentences": [
                ["Я щасливий!", "I am happy!"],
                ["Вона щаслива сьогодні.", "She is happy today."],
                ["Ми раді тебе бачити.", "We are glad to see you."],
                ["Це чудова новина!", "This is wonderful news!"],
                ["Я сумую за домом.", "I miss home."],
                ["Він сумний через дощ.", "He is sad because of the rain."],
                ["Не плач, усе буде добре.", "Don't cry, everything will be fine."],
                ["Я сердитий на нього.", "I am angry at him."],
                ["Вона розлючена!", "She is furious!"],
                ["Заспокойся, будь ласка.", "Calm down, please."],
                ["Я боюся темряви.", "I am afraid of the dark."],
                ["Не бійся, я поруч.", "Don't be afraid, I am nearby."],
                ["Я кохаю тебе.", "I love you (romantic)."],
                ["Я люблю свою сім’ю.", "I love my family."],
                ["Вони одружилися влітку.", "They got married in the summer."],
                ["Я здивований!", "I am surprised!"],
                ["Яка несподіванка!", "What a surprise!"],
                ["Мені соромно.", "I am ashamed."],
                ["Я пишаюся тобою.", "I am proud of you."],
                ["Спокій - це сила.", "Calmness is strength."],
            ],
            "spectrum": ["happy", "sad", "angry", "afraid", "love", "surprise"],
        },
    },
    {
        "key": "nature",
        "name": "Nature and Weather Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences about animals, plants, the seasons, and weather talk:\n"
            "  1. Сонце світить яскраво. - The sun is shining brightly.\n"
            "  2. Сьогодні хмарно. - It is cloudy today.\n"
            "  3. Іде дощ. - It is raining.\n"
            "  4. Вчора був сильний вітер. - Yesterday there was a strong wind.\n"
            "  5. Узимку падає сніг. - In winter snow falls.\n"
            "  6. Навесні цвітуть сади. - In spring the orchards bloom.\n"
            "  7. Влітку спекотно. - In summer it is hot.\n"
            "  8. Восени жовтіє листя. - In autumn the leaves turn yellow.\n"
            "  9. Яка гарна погода! - What beautiful weather!\n"
            "  10. Завтра буде мороз. - Tomorrow there will be frost.\n"
            "  11. Дуб - могутнє дерево. - The oak is a mighty tree.\n"
            "  12. Квіти пахнуть чудово. - The flowers smell wonderful.\n"
            "  13. Трава зелена після дощу. - The grass is green after the rain.\n"
            "  14. Птах співає на гілці. - A bird is singing on the branch.\n"
            "  15. Кіт ловить мишу. - The cat is catching a mouse.\n"
            "  16. Собака охороняє дім. - The dog is guarding the house.\n"
            "  17. Кінь пасеться на лузі. - The horse is grazing in the meadow.\n"
            "  18. У річці плаває риба. - Fish are swimming in the river.\n"
            "  19. Вовк виє в лісі. - A wolf is howling in the forest.\n"
            "  20. Бережімо природу! - Let's protect nature!"
        ),
        "how_it_works": (
            "These sentences work as a year in the Ukrainian landscape: "
            "weather verbs are impersonal (іде дощ, спекотно, хмарно - it "
            "rains, it is hot, it is cloudy), seasons take the locative "
            "(узимку, навесні, влітку, восени), and animals act in the "
            "nominative as full subjects. The impersonal weather pattern "
            "is one of Ukrainian's most idiomatic structures - there is "
            "no it, the sky simply does things. Nature vocabulary "
            "doubles as poetry vocabulary: дуб, калина, верба are the "
            "trees of a thousand Ukrainian songs."
        ),
        "key_points": [
            "Weather is impersonal: іде дощ, спекотно, хмарно.",
            "Seasons in the locative: узимку, навесні, влітку, восени.",
            "Animals: птах, кіт, собака, кінь, риба, вовк.",
            "Plants: дуб, квіти, трава; nature call: бережімо природу.",
            "20 sentences, each in Ukrainian with English translation.",
        ],
        "requirements": [
            "Describe today's weather in three Ukrainian sentences.",
            "Name five animals and five plants aloud.",
        ],
        "standards": [
            "Vocabulary is standard literary Ukrainian per Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["Іде дощ", "Влітку", "Восени", "Вовк", "природу"],
        "sig_lens": (
            "Through the Signature lens nature is the oldest sworn book: "
            "the oak its spine, the seasons its chapters, the wolf's howl "
            "its marginal note."
        ),
        "drill": {
            "sentences": [
                ["Сонце світить яскраво.", "The sun is shining brightly."],
                ["Сьогодні хмарно.", "It is cloudy today."],
                ["Іде дощ.", "It is raining."],
                ["Вчора був сильний вітер.", "Yesterday there was a strong wind."],
                ["Узимку падає сніг.", "In winter snow falls."],
                ["Навесні цвітуть сади.", "In spring the orchards bloom."],
                ["Влітку спекотно.", "In summer it is hot."],
                ["Восени жовтіє листя.", "In autumn the leaves turn yellow."],
                ["Яка гарна погода!", "What beautiful weather!"],
                ["Завтра буде мороз.", "Tomorrow there will be frost."],
                ["Дуб - могутнє дерево.", "The oak is a mighty tree."],
                ["Квіти пахнуть чудово.", "The flowers smell wonderful."],
                ["Трава зелена після дощу.", "The grass is green after the rain."],
                ["Птах співає на гілці.", "A bird is singing on the branch."],
                ["Кіт ловить мишу.", "The cat is catching a mouse."],
                ["Собака охороняє дім.", "The dog is guarding the house."],
                ["Кінь пасеться на лузі.", "The horse is grazing in the meadow."],
                ["У річці плаває риба.", "Fish are swimming in the river."],
                ["Вовк виє в лісі.", "A wolf is howling in the forest."],
                ["Бережімо природу!", "Let's protect nature!"],
            ],
            "seasons_locative": ["узимку", "навесні", "влітку", "восени"],
        },
    },
    {
        "key": "shopping",
        "name": "Shopping and Money Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences about the market, prices, bargaining, and paying:\n"
            "  1. Де тут базар? - Where is the market here?\n"
            "  2. Магазин відчинено до восьмої. - The shop is open until eight.\n"
            "  3. Скільки коштує кілограм яблук? - How much is a kilo of apples?\n"
            "  4. Це коштує сто гривень. - This costs one hundred hryvnias.\n"
            "  5. Дорого! Зробіть знижку. - Expensive! Give a discount.\n"
            "  6. Дешевше не буде. - It won't be cheaper.\n"
            "  7. Я беру два кілограми. - I'll take two kilos.\n"
            "  8. Дайте мені свіжого хліба. - Give me some fresh bread.\n"
            "  9. У вас є здача? - Do you have change?\n"
            "  10. Можна карткою? - Can I pay by card?\n"
            "  11. Так, термінал працює. - Yes, the terminal works.\n"
            "  12. Чек, будь ласка. - The receipt, please.\n"
            "  13. Я шукаю подарунок. - I am looking for a gift.\n"
            "  14. Покажіть мені цю сорочку. - Show me this shirt.\n"
            "  15. Чи є більший розмір? - Is there a bigger size?\n"
            "  16. Примірочна там. - The fitting room is there.\n"
            "  17. Мені пасує? - Does it suit me?\n"
            "  18. Дуже гарно! - Very nice!\n"
            "  19. Я купую це. - I'll buy this.\n"
            "  20. Дякую за покупку! - Thank you for your purchase!"
        ),
        "how_it_works": (
            "These sentences work as a full market run: finding the shop "
            "(де базар), asking prices (скільки коштує), bargaining "
            "(дорого, зробіть знижку), choosing goods (я беру, покажіть), "
            "and paying (можна карткою, чек). The currency is the "
            "hryvnia (гривня), divided into 100 kopiykas (копійки). "
            "Genitive of quantity appears everywhere - кілограм яблук, "
            "сто гривень - drilling the case of amounts. The bargaining "
            "pair дорого/дешевше is the whole economy of the bazaar in "
            "two words."
        ),
        "key_points": [
            "Currency: гривня (hryvnia), копійка (kopiyka).",
            "Price questions: скільки коштує; bargaining: дорого, зробіть знижку.",
            "Genitive of quantity: кілограм яблук, сто гривень.",
            "Payment: можна карткою, чек будь ласка; clothes: розмір, примірочна.",
            "20 sentences, each in Ukrainian with English translation.",
        ],
        "requirements": [
            "Role-play a market scene: greet, ask prices, bargain, pay.",
            "Convert five prices into Ukrainian aloud.",
        ],
        "standards": [
            "Vocabulary is standard literary Ukrainian per Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["гривень", "Скільки коштує", "знижку", "Чек", "базар"],
        "sig_lens": (
            "Through the Signature lens the market is a sworn exchange: "
            "every price a proposed covenant, every bargain a "
            "negotiation of vows, every receipt the sealed record."
        ),
        "drill": {
            "sentences": [
                ["Де тут базар?", "Where is the market here?"],
                ["Магазин відчинено до восьмої.", "The shop is open until eight."],
                ["Скільки коштує кілограм яблук?", "How much is a kilo of apples?"],
                ["Це коштує сто гривень.", "This costs one hundred hryvnias."],
                ["Дорого! Зробіть знижку.", "Expensive! Give a discount."],
                ["Дешевше не буде.", "It won't be cheaper."],
                ["Я беру два кілограми.", "I'll take two kilos."],
                ["Дайте мені свіжого хліба.", "Give me some fresh bread."],
                ["У вас є здача?", "Do you have change?"],
                ["Можна карткою?", "Can I pay by card?"],
                ["Так, термінал працює.", "Yes, the terminal works."],
                ["Чек, будь ласка.", "The receipt, please."],
                ["Я шукаю подарунок.", "I am looking for a gift."],
                ["Покажіть мені цю сорочку.", "Show me this shirt."],
                ["Чи є більший розмір?", "Is there a bigger size?"],
                ["Примірочна там.", "The fitting room is there."],
                ["Мені пасує?", "Does it suit me?"],
                ["Дуже гарно!", "Very nice!"],
                ["Я купую це.", "I'll buy this."],
                ["Дякую за покупку!", "Thank you for your purchase!"],
            ],
            "currency": ["гривня", "копійка"],
        },
    },
    {
        "key": "friendship",
        "name": "Friendship and Social Life Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences about meeting people, invitations, and celebrations:\n"
            "  1. Давай познайомимося! - Let's get acquainted!\n"
            "  2. Мене звати Олена. А тебе? - My name is Olena. And yours?\n"
            "  3. Дуже приємно! - Very nice to meet you!\n"
            "  4. Звідки ти? - Where are you from? (informal)\n"
            "  5. Я з Канади. - I am from Canada.\n"
            "  6. Скільки тобі років? - How old are you? (informal)\n"
            "  7. Мені двадцять п’ять. - I am twenty-five.\n"
            "  8. Ходімо гуляти! - Let's go for a walk!\n"
            "  9. Запрошую тебе на день народження! - I invite you to my birthday!\n"
            "  10. Коли свято? - When is the celebration?\n"
            "  11. У суботу о шостій. - On Saturday at six.\n"
            "  12. Я прийду з другом. - I'll come with a friend.\n"
            "  13. Що тобі подарувати? - What should I give you as a gift?\n"
            "  14. Найкращий подарунок - твоя присутність. - The best gift is your presence.\n"
            "  15. Вітаю з днем народження! - Happy birthday!\n"
            "  16. Бажаю щастя і здоров’я! - I wish you happiness and health!\n"
            "  17. За твоє здоров’я! - To your health! (toast)\n"
            "  18. Дякую, що прийшов! - Thank you for coming! (to a man)\n"
            "  19. Ми друзі назавжди. - We are friends forever.\n"
            "  20. До скорої зустрічі! - See you soon!"
        ),
        "how_it_works": (
            "These sentences work as a friendship from first hello to "
            "lifelong bond: introduction (давай познайомимося), small "
            "talk (звідки ти, скільки років), invitation (запрошую, "
            "ходімо), celebration (вітаю, бажаю, за твоє здоров’я), and "
            "farewell (до скорої зустрічі). Age uses the dative of the "
            "person - мені двадцять п’ять, literally to me it is "
            "twenty-five - one of Ukrainian's signature impersonal "
            "patterns. Toasts and wishes (бажаю, вітаю) run in the "
            "accusative of the thing wished."
        ),
        "key_points": [
            "Introductions: давай познайомимося, мене звати, дуже приємно.",
            "Age in the dative: мені двадцять п’ять.",
            "Invitations: запрошую, ходімо гуляти, я прийду з другом.",
            "Celebrations: вітаю з днем народження, бажаю щастя, за твоє здоров’я.",
            "20 sentences, each in Ukrainian with English translation.",
        ],
        "requirements": [
            "Introduce yourself fully: name, origin, age, in Ukrainian.",
            "Give a birthday toast aloud.",
        ],
        "standards": [
            "Vocabulary is standard literary Ukrainian per Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["познайомимося", "двадцять п’ять", "Вітаю", "друзі", "Запрошую"],
        "sig_lens": (
            "Through the Signature lens friendship is a sworn bond "
            "sealed twice: once at the first hello, once at every toast "
            "after."
        ),
        "drill": {
            "sentences": [
                ["Давай познайомимося!", "Let's get acquainted!"],
                ["Мене звати Олена. А тебе?", "My name is Olena. And yours?"],
                ["Дуже приємно!", "Very nice to meet you!"],
                ["Звідки ти?", "Where are you from?"],
                ["Я з Канади.", "I am from Canada."],
                ["Скільки тобі років?", "How old are you?"],
                ["Мені двадцять п’ять.", "I am twenty-five."],
                ["Ходімо гуляти!", "Let's go for a walk!"],
                ["Запрошую тебе на день народження!", "I invite you to my birthday!"],
                ["Коли свято?", "When is the celebration?"],
                ["У суботу о шостій.", "On Saturday at six."],
                ["Я прийду з другом.", "I'll come with a friend."],
                ["Що тобі подарувати?", "What should I give you as a gift?"],
                ["Найкращий подарунок - твоя присутність.", "The best gift is your presence."],
                ["Вітаю з днем народження!", "Happy birthday!"],
                ["Бажаю щастя і здоров’я!", "I wish you happiness and health!"],
                ["За твоє здоров’я!", "To your health!"],
                ["Дякую, що прийшов!", "Thank you for coming!"],
                ["Ми друзі назавжди.", "We are friends forever."],
                ["До скорої зустрічі!", "See you soon!"],
            ],
            "stages": ["introduction", "small talk", "invitation", "celebration", "farewell"],
        },
    },
    {
        "key": "technology",
        "name": "Technology and Communication Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences about the phone, the internet, the computer, and messaging:\n"
            "  1. Де мій телефон? - Where is my phone?\n"
            "  2. Телефон розрядився. - The phone ran out of battery.\n"
            "  3. Постав на зарядку. - Put it on the charger.\n"
            "  4. Я тобі телефоную. - I am calling you.\n"
            "  5. Алло! Хто це? - Hello! Who is this? (on the phone)\n"
            "  6. Зачекай хвилину. - Wait a minute.\n"
            "  7. Зв’язок поганий. - The connection is bad.\n"
            "  8. Надішли мені повідомлення. - Send me a message.\n"
            "  9. Я надіслав тобі фото. - I sent you a photo.\n"
            "  10. Відкрий це посилання. - Open this link.\n"
            "  11. Інтернет не працює. - The internet is not working.\n"
            "  12. Який пароль від вайфаю? - What is the Wi-Fi password?\n"
            "  13. Увімкни комп’ютер. - Turn on the computer.\n"
            "  14. Екран завис. - The screen froze.\n"
            "  15. Перезавантаж його. - Restart it.\n"
            "  16. Збережи файл. - Save the file.\n"
            "  17. Я шукаю це в інтернеті. - I am looking this up on the internet.\n"
            "  18. Завантаж цю програму. - Download this app.\n"
            "  19. Мій електронний лист уже надіслано. - My email has already been sent.\n"
            "  20. Технології змінюють світ. - Technology is changing the world."
        ),
        "how_it_works": (
            "These sentences work as a day with devices: power (телефон "
            "розрядився, постав на зарядку), calls (я телефоную, алло), "
            "messages (надішли повідомлення, я надіслав фото), network "
            "(інтернет не працює, пароль від вайфаю), and computer "
            "(увімкни, завис, перезавантаж, збережи файл). Imperatives "
            "dominate - technology is commanded, not described - drilling "
            "the command forms in their most modern habitat. Loanwords "
            "(вайфай, файл, сайт) show how Ukrainian absorbs the digital "
            "age while keeping its own grammar."
        ),
        "key_points": [
            "Devices: телефон, комп’ютер, екран; network: інтернет, вайфай, зв’язок.",
            "Actions: телефонувати, надіслати, завантажити, зберегти, перезавантажіти.",
            "Tech imperatives: увімкни, відкрий, збережи, перезавантаж.",
            "Loanwords keep Ukrainian grammar: вайфаю (genitive), фото (indeclinable).",
            "20 sentences, each in Ukrainian with English translation.",
        ],
        "requirements": [
            "Give five tech commands to your phone aloud in Ukrainian.",
            "Describe a frozen screen and its fix in three sentences.",
        ],
        "standards": [
            "Vocabulary is standard literary Ukrainian per Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["телефон", "інтернет", "комп’ютер", "повідомлення", "вайфаю"],
        "sig_lens": (
            "Through the Signature lens technology is the newest sworn "
            "tool: the phone a covenant of voices across distance, the "
            "file a sealed letter that never fades."
        ),
        "drill": {
            "sentences": [
                ["Де мій телефон?", "Where is my phone?"],
                ["Телефон розрядився.", "The phone ran out of battery."],
                ["Постав на зарядку.", "Put it on the charger."],
                ["Я тобі телефоную.", "I am calling you."],
                ["Алло! Хто це?", "Hello! Who is this?"],
                ["Зачекай хвилину.", "Wait a minute."],
                ["Зв’язок поганий.", "The connection is bad."],
                ["Надішли мені повідомлення.", "Send me a message."],
                ["Я надіслав тобі фото.", "I sent you a photo."],
                ["Відкрий це посилання.", "Open this link."],
                ["Інтернет не працює.", "The internet is not working."],
                ["Який пароль від вайфаю?", "What is the Wi-Fi password?"],
                ["Увімкни комп’ютер.", "Turn on the computer."],
                ["Екран завис.", "The screen froze."],
                ["Перезавантаж його.", "Restart it."],
                ["Збережи файл.", "Save the file."],
                ["Я шукаю це в інтернеті.", "I am looking this up on the internet."],
                ["Завантаж цю програму.", "Download this app."],
                ["Мій електронний лист уже надіслано.", "My email has already been sent."],
                ["Технології змінюють світ.", "Technology is changing the world."],
            ],
            "devices": ["телефон", "комп’ютер", "екран"],
        },
    },
    {
        "key": "tenses",
        "name": "Verb Tenses in Sentences: Present, Past, Future",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Ukrainian verbs run on two axes at once: tense (present, "
            "past, future) and aspect (imperfective, perfective). Only "
            "imperfective verbs have a present tense; the past is built "
            "with -в/-ла/-ло/-ли endings that agree in gender and number; "
            "the future is synthetic (писатиму) or analytic (буду писати) "
            "for the imperfective, and simple perfective (напишу) for the "
            "completed future. \n\n"
            "Present tense (imperfective only) - 6 sentences:\n"
            "  Я читаю книгу. - I am reading a book.\n"
            "  Ти пишеш листа. - You are writing a letter.\n"
            "  Він говорить українською. - He speaks Ukrainian.\n"
            "  Ми їмо обід. - We are eating lunch.\n"
            "  Ви працюєте добре. - You work well.\n"
            "  Вони живуть у Києві. - They live in Kyiv.\n\n"
            "Past tense (-в masc, -ла fem, -ло neut, -ли pl) - 6 sentences:\n"
            "  Я читав книгу вчора. - I read (was reading) the book yesterday. (man)\n"
            "  Вона писала листа. - She wrote (was writing) the letter.\n"
            "  Вікно було відчинене. - The window was open.\n"
            "  Ми їли обід разом. - We ate (were eating) lunch together.\n"
            "  Ви працювали вчора? - Did you work yesterday?\n"
            "  Вони жили у Львові. - They lived in Lviv.\n\n"
            "Future tense (synthetic, analytic, perfective) - 7 sentences:\n"
            "  Я читатиму книгу завтра. - I will be reading the book tomorrow. (synthetic)\n"
            "  Ти будеш писати листа. - You will be writing the letter. (analytic)\n"
            "  Він говоритиме українською. - He will speak Ukrainian. (synthetic)\n"
            "  Ми будемо їсти обід. - We will eat lunch. (analytic)\n"
            "  Я прочитаю книгу завтра. - I will read (finish) the book tomorrow. (perfective)\n"
            "  Вона напише листа. - She will write (complete) the letter. (perfective)\n"
            "  Ми зробимо це разом. - We will do it together. (perfective)\n\n"
            "Aspect in action - the same verb, two views:\n"
            "  Я писав листа дві години. - I was writing the letter for two hours. (process)\n"
            "  Я написав листа за годину. - I wrote the letter in an hour. (completed)"
        ),
        "how_it_works": (
            "The tense system works as a grid. Present: take the "
            "imperfective stem and add the conjugation endings (-у/-ю, "
            "-еш/-иш, -е/-ить, -емо/-имо, -ете/-ите, -уть/-ять). Past: "
            "drop the infinitive -ти, add -в (masc), -ла (fem), -ло "
            "(neut), -ли (plural) - the verb now agrees like an "
            "adjective. Future imperfective: either fuse -му/-меш/-ме "
            "endings onto the infinitive (читатиму) or pair буду with "
            "the infinitive (буду читати). Future perfective: conjugate "
            "the perfective stem as if it were present (напишу, "
            "прочитаєш) - the completion is baked into the stem. Aspect "
            "chooses the lens: писав watches the writing happen, написав "
            "announces it done."
        ),
        "key_points": [
            "Present tense exists only for imperfective verbs.",
            "Past: -в/-ла/-ло/-ли, agreeing in gender and number.",
            "Future: synthetic (читатиму), analytic (буду читати), perfective (прочитаю).",
            "Aspect pairs: писати/написати, читати/прочитати, робити/зробити.",
            "19 sentences: 6 present, 6 past, 7 future, each translated.",
        ],
        "requirements": [
            "Conjugate читати in present, past (all genders), and both futures aloud.",
            "Convert five present sentences into the past and the perfective future.",
        ],
        "standards": [
            "Tense and aspect system follows Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["читатиму", "буду писати", "напише", "-ла", "imperfective"],
        "sig_lens": (
            "Through the Signature lens tense is the sworn river of time "
            "and aspect its two banks: the imperfective bank where the "
            "work flows on, the perfective bank where it comes to rest."
        ),
        "drill": {
            "present": [
                ["Я читаю книгу.", "I am reading a book."],
                ["Ти пишеш листа.", "You are writing a letter."],
                ["Він говорить українською.", "He speaks Ukrainian."],
                ["Ми їмо обід.", "We are eating lunch."],
                ["Ви працюєте добре.", "You work well."],
                ["Вони живуть у Києві.", "They live in Kyiv."],
            ],
            "past": [
                ["Я читав книгу вчора.", "I read the book yesterday."],
                ["Вона писала листа.", "She was writing the letter."],
                ["Вікно було відчинене.", "The window was open."],
                ["Ми їли обід разом.", "We were eating lunch together."],
                ["Ви працювали вчора?", "Did you work yesterday?"],
                ["Вони жили у Львові.", "They lived in Lviv."],
            ],
            "future": [
                ["Я читатиму книгу завтра.", "I will be reading the book tomorrow."],
                ["Ти будеш писати листа.", "You will be writing the letter."],
                ["Він говоритиме українською.", "He will speak Ukrainian."],
                ["Ми будемо їсти обід.", "We will eat lunch."],
                ["Я прочитаю книгу завтра.", "I will finish the book tomorrow."],
                ["Вона напише листа.", "She will complete the letter."],
                ["Ми зробимо це разом.", "We will do it together."],
            ],
            "aspect_pairs": [["писати", "написати"], ["читати", "прочитати"],
                             ["робити", "зробити"]],
        },
    },
    {
        "key": "qa",
        "name": "Questions and Answers",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "20 question-and-answer pairs covering who, what, where, when, "
            "why, and how:\n"
            "  1. Хто це? - Who is this? / Це мій друг. - This is my friend.\n"
            "  2. Що це? - What is this? / Це книга. - This is a book.\n"
            "  3. Де ти живеш? - Where do you live? / Я живу в Києві. - I live in Kyiv.\n"
            "  4. Куди ти йдеш? - Where are you going (to)? / Я йду додому. - I am going home.\n"
            "  5. Звідки ти? - Where are you from? / Я з України. - I am from Ukraine.\n"
            "  6. Коли ти прийдеш? - When will you come? / Я прийду завтра. - I will come tomorrow.\n"
            "  7. Чому ти сумуєш? - Why are you sad? / Бо йде дощ. - Because it is raining.\n"
            "  8. Як тебе звати? - What is your name? / Мене звати Олена. - My name is Olena.\n"
            "  9. Як справи? - How are things? / Добре, дякую! - Fine, thank you!\n"
            "  10. Скільки це коштує? - How much does this cost? / Сто гривень. - One hundred hryvnias.\n"
            "  11. Яка це книга? - What kind of book is this? / Цікава книга. - An interesting book.\n"
            "  12. Чий це телефон? - Whose phone is this? / Це мій телефон. - This is my phone.\n"
            "  13. Ти говориш українською? - Do you speak Ukrainian? / Так, трохи. - Yes, a little.\n"
            "  14. Ви розумієте мене? - Do you understand me? / Так, розумію. - Yes, I understand.\n"
            "  15. Що ти робиш? - What are you doing? / Я читаю. - I am reading.\n"
            "  16. Де ти був учора? - Where were you yesterday? / Я був удома. - I was at home.\n"
            "  17. Коли ти народився? - When were you born? / Я народився у 2000 році. - I was born in 2000.\n"
            "  18. Чому ти спізнився? - Why were you late? / Бо була затор. - Because there was a traffic jam.\n"
            "  19. Як дістатися до музею? - How do I get to the museum? / Ідіть прямо. - Go straight.\n"
            "  20. Що нового? - What's new? / Нічого нового. - Nothing new."
        ),
        "how_it_works": (
            "Questions work three ways in Ukrainian. Intonation alone "
            "turns a statement into a yes-no question (Ти говориш "
            "українською?). The particle чи marks it explicitly (Чи ти "
            "говориш?). Question words open information questions, and "
            "each word has its own territory: хто asks for people, що "
            "for things, де for place, куди for destination, звідки for "
            "origin, коли for time, чому for reason, як for manner and "
            "identity, скільки for quantity, який for kind, чий for "
            "ownership. Answers mirror the question's verb and case - "
            "the drill of this record is to hear the question word and "
            "fire back the matching frame."
        ),
        "key_points": [
            "Three question strategies: intonation, чи, question words.",
            "хто/що (who/what), де/куди/звідки (where/to/from), коли (when), чому (why), як (how).",
            "скільки (how many), який (which kind), чий (whose).",
            "Answers mirror the question's verb and case.",
            "20 Q&A pairs, each translated.",
        ],
        "requirements": [
            "Ask and answer all 20 pairs aloud with a partner or to yourself.",
            "Convert five statements into questions three ways (intonation, чи, question word).",
        ],
        "standards": [
            "Question formation follows Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["Хто", "Що", "Де", "Коли", "Чому", "Як", "чи"],
        "sig_lens": (
            "Through the Signature lens every question is a sworn key "
            "and every answer the door it opens: хто opens the person, "
            "де opens the place, чому opens the reason."
        ),
        "drill": {
            "pairs": [
                ["Хто це?", "Це мій друг."], ["Що це?", "Це книга."],
                ["Де ти живеш?", "Я живу в Києві."], ["Куди ти йдеш?", "Я йду додому."],
                ["Звідки ти?", "Я з України."], ["Коли ти прийдеш?", "Я прийду завтра."],
                ["Чому ти сумуєш?", "Бо йде дощ."], ["Як тебе звати?", "Мене звати Олена."],
                ["Як справи?", "Добре, дякую!"], ["Скільки це коштує?", "Сто гривень."],
                ["Яка це книга?", "Цікава книга."], ["Чий це телефон?", "Це мій телефон."],
                ["Ти говориш українською?", "Так, трохи."],
                ["Ви розумієте мене?", "Так, розумію."],
                ["Що ти робиш?", "Я читаю."],
                ["Де ти був учора?", "Я був удома."],
                ["Коли ти народився?", "Я народився у 2000 році."],
                ["Чому ти спізнився?", "Бо був затор."],
                ["Як дістатися до музею?", "Ідіть прямо."],
                ["Що нового?", "Нічого нового."],
            ],
            "question_words": ["хто", "що", "де", "куди", "звідки", "коли",
                               "чому", "як", "скільки", "який", "чий"],
        },
    },
    {
        "key": "commands",
        "name": "Commands and Requests",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Ukrainian commands come in informal (ти) and formal/plural "
            "(ви) forms: читай (read! informal) vs читайте (read! formal). "
            "The informal imperative usually ends in a bare stem or -й; "
            "the formal adds -те. \n\n"
            "20 imperatives and polite requests, informal vs formal:\n"
            "  1. Читай! / Читайте! - Read! / Сідай! / Сідайте! - Sit down!\n"
            "  2. Пиши! / Пишіть! - Write! / Слухай! / Слухайте! - Listen!\n"
            "  3. Іди! / Ідіть! - Go! / Приходь! / Приходьте! - Come!\n"
            "  4. Дай! / Дайте! - Give! / Візьми! / Візьміть! - Take!\n"
            "  5. Скажи! / Скажіть! - Say! / Покажи! / Покажіть! - Show!\n"
            "  6. Зроби! / Зробіть! - Do it! / Допоможи! / Допоможіть! - Help!\n"
            "  7. Зачекай! / Зачекайте! - Wait! / Почекай! / Почекайте! - Wait a bit!\n"
            "  8. Відкрий! / Відкрийте! - Open! / Зачини! / Зачиніть! - Close!\n"
            "  9. Увімкни! / Увімкніть! - Turn on! / Вимкни! / Вимкніть! - Turn off!\n"
            "  10. Їж! / Їжте! - Eat! / Пий! / Пийте! - Drink!\n"
            "  11. Не хвилюйся! / Не хвилюйтеся! - Don't worry!\n"
            "  12. Будь ласка, сядь. / Будь ласка, сядьте. - Please sit down.\n"
            "  13. Дай мені, будь ласка. / Дайте мені, будь ласка. - Give me, please.\n"
            "  14. Вибач! / Вибачте! - Sorry! / Дякую! - Thank you!\n"
            "  15. Говори повільніше. / Говоріть повільніше. - Speak more slowly.\n"
            "  16. Повтори, будь ласка. / Повторіть, будь ласка. - Repeat, please.\n"
            "  17. Напиши мені. / Напишіть мені. - Write to me.\n"
            "  18. Подзвони ввечері. / Подзвоніть ввечері. - Call in the evening.\n"
            "  19. Бережи себе! / Бережіть себе! - Take care of yourself!\n"
            "  20. Щасти тобі! / Щасти вам! - Good luck to you!"
        ),
        "how_it_works": (
            "The imperative works by stripping the verb to its stem and "
            "adding the command ending: second-conjugation verbs take -и "
            "(говори -> говори), first-conjugation verbs take the bare "
            "stem (читай, пиши), and the formal/plural adds -те to either "
            "(читайте, говоріть). Negation (не хвилюйся) softens or "
            "prohibits; будь ласка turns any command into a polite "
            "request. Reflexive commands keep their -ся (сідай, "
            "бережися). The drill is always the pair: learn читай and "
            "читайте as one unit, never one without the other."
        ),
        "key_points": [
            "Informal imperative: bare stem or -й/-и (читай, говори).",
            "Formal/plural: add -те (читайте, говоріть).",
            "Negation with не; politeness with будь ласка.",
            "Reflexives keep -ся: сідай, бережи себе.",
            "20 command pairs, informal vs formal, each translated.",
        ],
        "requirements": [
            "Give ten commands to a friend (ти) and the same ten formally (ви).",
            "Soften five commands with будь ласка.",
        ],
        "standards": [
            "Imperative formation follows Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["Читай", "Читайте", "будь ласка", "Не хвилюйся", "imperatives"],
        "sig_lens": (
            "Through the Signature lens a command is a sworn arrow: "
            "читай flies to one friend, читайте to the honored elder - "
            "same arrow, different bow."
        ),
        "drill": {
            "pairs": [
                ["Читай!", "Читайте!"], ["Пиши!", "Пишіть!"],
                ["Іди!", "Ідіть!"], ["Дай!", "Дайте!"],
                ["Скажи!", "Скажіть!"], ["Зроби!", "Зробіть!"],
                ["Зачекай!", "Зачекайте!"], ["Відкрий!", "Відкрийте!"],
                ["Увімкни!", "Увімкніть!"], ["Їж!", "Їжте!"],
            ],
            "softened": 5,
            "reflexive": ["Сідай!", "Бережи себе!"],
        },
    },
    {
        "key": "descriptions",
        "name": "Descriptions: People and Places",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "20 sentences describing people, places, and things in detail:\n"
            "  1. Мій друг високий і спортивний. - My friend is tall and athletic.\n"
            "  2. У неї довге чорне волосся. - She has long black hair.\n"
            "  3. Його очі сині, як небо. - His eyes are blue like the sky.\n"
            "  4. Вона носить червону сукню. - She is wearing a red dress.\n"
            "  5. Дідусь мудрий і добрий. - Grandfather is wise and kind.\n"
            "  6. Маленька дівчинка усміхається. - The little girl is smiling.\n"
            "  7. Київ - велике і старовинне місто. - Kyiv is a big and ancient city.\n"
            "  8. Дніпро - широка і могутня ріка. - The Dnipro is a wide and mighty river.\n"
            "  9. Львів славиться кавою і архітектурою. - Lviv is famous for coffee and architecture.\n"
            "  10. Карпати вкриті густим лісом. - The Carpathians are covered with dense forest.\n"
            "  11. Море спокійне і тепле. - The sea is calm and warm.\n"
            "  12. Наш дім стоїть на тихій вулиці. - Our house stands on a quiet street.\n"
            "  13. Кімната світла, з великим вікном. - The room is bright, with a big window.\n"
            "  14. Старий дуб росте біля хати. - An old oak grows by the house.\n"
            "  15. Квіти у саду яскраві і пахучі. - The flowers in the garden are bright and fragrant.\n"
            "  16. Ця книга товста і цікава. - This book is thick and interesting.\n"
            "  17. Стіл дерев’яний, стільці зручні. - The table is wooden, the chairs comfortable.\n"
            "  18. Ніч тиха, зорі яскраві. - The night is quiet, the stars bright.\n"
            "  19. Ранок туманний, але гарний. - The morning is foggy but beautiful.\n"
            "  20. Україна - прекрасна країна. - Ukraine is a beautiful country."
        ),
        "how_it_works": (
            "Descriptions work by stacking agreeing adjectives onto nouns: "
            "each adjective takes the noun's gender, number, and case "
            "(високий друг, довге волосся, сині очі, червону сукню). "
            "Comparisons use як (like) with the nominative. Instrumental "
            "of material and covering appears naturally (вкриті лісом, "
            "стіл дерев’яний). The descriptive sentence is the adjective "
            "agreement rule from the grammar record running at full "
            "speed - every sentence here is a drill disguised as a "
            "picture."
        ),
        "key_points": [
            "Stack agreeing adjectives: високий друг, довге чорне волосся.",
            "Comparisons with як: сині, як небо.",
            "Instrumental of material/covering: вкриті лісом.",
            "Place descriptions: Київ, Дніпро, Львів, Карпати, море.",
            "20 sentences, each in Ukrainian with English translation.",
        ],
        "requirements": [
            "Describe three people and three places aloud in full sentences.",
            "Use як in two comparisons of your own.",
        ],
        "standards": [
            "Vocabulary is standard literary Ukrainian per Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["Дніпро", "Карпати", "як небо", "дерев’яний", "прекрасна"],
        "sig_lens": (
            "Through the Signature lens a description is a sworn portrait: "
            "each adjective a brushstroke, each agreement a true line, "
            "until the person or place stands living on the page."
        ),
        "drill": {
            "sentences": [
                ["Мій друг високий і спортивний.", "My friend is tall and athletic."],
                ["У неї довге чорне волосся.", "She has long black hair."],
                ["Його очі сині, як небо.", "His eyes are blue like the sky."],
                ["Вона носить червону сукню.", "She is wearing a red dress."],
                ["Дідусь мудрий і добрий.", "Grandfather is wise and kind."],
                ["Маленька дівчинка усміхається.", "The little girl is smiling."],
                ["Київ - велике і старовинне місто.", "Kyiv is a big and ancient city."],
                ["Дніпро - широка і могутня ріка.", "The Dnipro is a wide and mighty river."],
                ["Львів славиться кавою і архітектурою.", "Lviv is famous for coffee and architecture."],
                ["Карпати вкриті густим лісом.", "The Carpathians are covered with dense forest."],
                ["Море спокійне і тепле.", "The sea is calm and warm."],
                ["Наш дім стоїть на тихій вулиці.", "Our house stands on a quiet street."],
                ["Кімната світла, з великим вікном.", "The room is bright, with a big window."],
                ["Старий дуб росте біля хати.", "An old oak grows by the house."],
                ["Квіти у саду яскраві і пахучі.", "The flowers in the garden are bright and fragrant."],
                ["Ця книга товста і цікава.", "This book is thick and interesting."],
                ["Стіл дерев’яний, стільці зручні.", "The table is wooden, the chairs comfortable."],
                ["Ніч тиха, зорі яскраві.", "The night is quiet, the stars bright."],
                ["Ранок туманний, але гарний.", "The morning is foggy but beautiful."],
                ["Україна - прекрасна країна.", "Ukraine is a beautiful country."],
            ],
            "comparisons": 1,
        },
    },
    {
        "key": "story1",
        "name": "Story I: A Day in the Village",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A 10-sentence simple story in Ukrainian, present tense, with "
            "line-by-line English translation:\n"
            "  1. Ранок у селі тихий і світлий. - The morning in the village is quiet and bright.\n"
            "  2. Сонце сходить над полем. - The sun is rising over the field.\n"
            "  3. Півень співає на подвір’ї. - The rooster is singing in the yard.\n"
            "  4. Бабуся доїть корову. - Grandmother is milking the cow.\n"
            "  5. Дідусь годує курей. - Grandfather is feeding the hens.\n"
            "  6. Діти біжать до школи. - The children are running to school.\n"
            "  7. Мама пече хліб у печі. - Mom is baking bread in the oven.\n"
            "  8. Запах свіжого хліба наповнює хату. - The smell of fresh bread fills the house.\n"
            "  9. Собака лежить на сонці. - The dog is lying in the sun.\n"
            "  10. Усі щасливі в цьому домі. - Everyone is happy in this house."
        ),
        "how_it_works": (
            "This story works as a present-tense panorama: every verb is "
            "imperfective present (сходить, співає, доїть, годує, біжать, "
            "пече, наповнює, лежить), painting actions in progress. Nouns "
            "stay in the nominative as actors, with the locative marking "
            "place (у селі, на подвір’ї, у печі, на сонці). Read it aloud "
            "three times: first for the sounds, second translating each "
            "line, third without looking at the English."
        ),
        "key_points": [
            "10 sentences, present-tense imperfective verbs throughout.",
            "Village vocabulary: півень, корова, кури, піч, подвір’я.",
            "Locative of place: у селі, на подвір’ї, у печі.",
            "Line-by-line English translation.",
        ],
        "requirements": [
            "Read the story aloud until it flows without hesitation.",
            "Retell the story in your own Ukrainian words.",
        ],
        "standards": [
            "Grammar follows Pugh and Press 1999; the story is a Signature-generated teaching text.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["селі", "Півень", "Бабуся", "Дідусь", "щасливі"],
        "sig_lens": (
            "Through the Signature lens this village morning is a sworn "
            "fresco: ten panels, each verb a living figure, the bread's "
            "smell the gold leaf that binds them."
        ),
        "drill": {
            "lines": [
                ["Ранок у селі тихий і світлий.", "The morning in the village is quiet and bright."],
                ["Сонце сходить над полем.", "The sun is rising over the field."],
                ["Півень співає на подвір’ї.", "The rooster is singing in the yard."],
                ["Бабуся доїть корову.", "Grandmother is milking the cow."],
                ["Дідусь годує курей.", "Grandfather is feeding the hens."],
                ["Діти біжать до школи.", "The children are running to school."],
                ["Мама пече хліб у печі.", "Mom is baking bread in the oven."],
                ["Запах свіжого хліба наповнює хату.", "The smell of fresh bread fills the house."],
                ["Собака лежить на сонці.", "The dog is lying in the sun."],
                ["Усі щасливі в цьому домі.", "Everyone is happy in this house."],
            ],
            "tense": "present",
        },
    },
    {
        "key": "story2",
        "name": "Story II: The Trip to Kyiv",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A 10-sentence story in the past tense, with line-by-line "
            "English translation:\n"
            "  1. Минулого літа ми поїхали до Києва. - Last summer we went to Kyiv.\n"
            "  2. Поїзд прибув рано-вранці. - The train arrived early in the morning.\n"
            "  3. Ми побачили золоті куполи церков. - We saw the golden domes of the churches.\n"
            "  4. Дніпро виблискував на сонці. - The Dnipro was sparkling in the sun.\n"
            "  5. Ми гуляли Хрещатиком цілий день. - We walked Khreshchatyk all day.\n"
            "  6. У музеї ми дізналися багато нового. - At the museum we learned a lot of new things.\n"
            "  7. Ввечері ми їли вареники в ресторані. - In the evening we ate varenyky at a restaurant.\n"
            "  8. Дощ почався, але ми не змокли. - The rain started, but we did not get wet.\n"
            "  9. Ми купили сувеніри для друзів. - We bought souvenirs for our friends.\n"
            "  10. Подорож запам’яталася назавжди. - The trip was remembered forever."
        ),
        "how_it_works": (
            "This story works as a past-tense journey: verbs agree in "
            "gender and number with their subjects (поїзд прибув - "
            "masculine, ми поїхали - plural, подорож запам’яталася - "
            "feminine reflexive). Perfective verbs (поїхали, прибув, "
            "побачили, купили) mark completed events; imperfective verbs "
            "(виблискував, гуляли, їли) paint the ongoing background. "
            "The time frame минулого літа opens in the genitive - "
            "Ukrainian's way of saying last."
        ),
        "key_points": [
            "10 sentences, past-tense verbs agreeing in gender and number.",
            "Perfective events vs imperfective background.",
            "Time expressions: минулого літа, рано-вранці, цілий день, ввечері.",
            "Kyiv sights: золоті куполи, Дніпро, Хрещатик.",
            "Line-by-line English translation.",
        ],
        "requirements": [
            "Underline every past-tense verb and name its gender/number.",
            "Retell a trip of your own in the past tense.",
        ],
        "standards": [
            "Grammar follows Pugh and Press 1999; the story is a Signature-generated teaching text.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["поїхали", "прибув", "Хрещатиком", "вареники", "запам’яталася"],
        "sig_lens": (
            "Through the Signature lens this journey is a sworn road "
            "behind the traveler: each completed verb a milestone passed, "
            "each golden dome a seal on the memory."
        ),
        "drill": {
            "lines": [
                ["Минулого літа ми поїхали до Києва.", "Last summer we went to Kyiv."],
                ["Поїзд прибув рано-вранці.", "The train arrived early in the morning."],
                ["Ми побачили золоті куполи церков.", "We saw the golden domes of the churches."],
                ["Дніпро виблискував на сонці.", "The Dnipro was sparkling in the sun."],
                ["Ми гуляли Хрещатиком цілий день.", "We walked Khreshchatyk all day."],
                ["У музеї ми дізналися багато нового.", "At the museum we learned a lot of new things."],
                ["Ввечері ми їли вареники в ресторані.", "In the evening we ate varenyky at a restaurant."],
                ["Дощ почався, але ми не змокли.", "The rain started, but we did not get wet."],
                ["Ми купили сувеніри для друзів.", "We bought souvenirs for our friends."],
                ["Подорож запам’яталася назавжди.", "The trip was remembered forever."],
            ],
            "tense": "past",
        },
    },
    {
        "key": "story3",
        "name": "Story III: The Dream of Tomorrow",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A 10-sentence story using future and conditional forms, with "
            "line-by-line English translation:\n"
            "  1. Завтра я прокинуся рано. - Tomorrow I will wake up early.\n"
            "  2. Сонце зійде, і день буде чудовим. - The sun will rise, and the day will be wonderful.\n"
            "  3. Я напишу листа другові. - I will write (complete) a letter to my friend.\n"
            "  4. Ми зустрінемося біля річки. - We will meet by the river.\n"
            "  5. Я будуватиму плани на літо. - I will be making plans for the summer.\n"
            "  6. Якщо буде дощ, ми залишимося вдома. - If it rains, we will stay home.\n"
            "  7. Я хотів би подорожувати світом. - I would like to travel the world.\n"
            "  8. Мрії збуваються, якщо працювати. - Dreams come true if you work.\n"
            "  9. Ми побудуємо новий дім. - We will build a new house.\n"
            "  10. Майбутнє належить тим, хто вірить. - The future belongs to those who believe."
        ),
        "how_it_works": (
            "This story works as a future-tense vision: perfective "
            "futures (прокинуся, зійде, напишу, зустрінемося, побудуємо) "
            "promise completed actions; the synthetic imperfective "
            "future (будуватиму) stretches an ongoing plan across the "
            "summer. The conditional (хотів би - would like) opens the "
            "world of wishes, and якщо (if) builds the conditional "
            "frame. Note the reflexive futures (зустрінемося - we will "
            "meet each other) keeping their -ся into tomorrow."
        ),
        "key_points": [
            "10 sentences: perfective futures, synthetic imperfective future, conditional.",
            "хотів би = would like; якщо = if.",
            "Reflexive futures keep -ся: зустрінемося.",
            "Line-by-line English translation.",
        ],
        "requirements": [
            "Write five sentences about your own tomorrow in the future tense.",
            "Convert three of them into wishes with би.",
        ],
        "standards": [
            "Grammar follows Pugh and Press 1999; the story is a Signature-generated teaching text.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["прокинуся", "будуватиму", "хотів би", "якщо", "Майбутнє"],
        "sig_lens": (
            "Through the Signature lens tomorrow is a sworn page not "
            "yet written: each future verb a promise sealed, each "
            "conditional a door left open for the dream."
        ),
        "drill": {
            "lines": [
                ["Завтра я прокинуся рано.", "Tomorrow I will wake up early."],
                ["Сонце зійде, і день буде чудовим.", "The sun will rise, and the day will be wonderful."],
                ["Я напишу листа другові.", "I will write a letter to my friend."],
                ["Ми зустрінемося біля річки.", "We will meet by the river."],
                ["Я будуватиму плани на літо.", "I will be making plans for the summer."],
                ["Якщо буде дощ, ми залишимося вдома.", "If it rains, we will stay home."],
                ["Я хотів би подорожувати світом.", "I would like to travel the world."],
                ["Мрії збуваються, якщо працювати.", "Dreams come true if you work."],
                ["Ми побудуємо новий дім.", "We will build a new house."],
                ["Майбутнє належить тим, хто вірить.", "The future belongs to those who believe."],
            ],
            "tense": "future",
        },
    },
    {
        "key": "idioms",
        "name": "Idioms and Proverbs",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "20 Ukrainian idioms and proverbs - each with literal "
            "translation, real meaning, and an example sentence:\n"
            "  1. Без труда нема плода. - Lit: Without labor there is no fruit. Means: No pain, no gain. Ex: Вчися щодня - без труда нема плода. - Study daily - no pain, no gain.\n"
            "  2. Вода камінь точить. - Lit: Water wears away stone. Means: Persistence wins. Ex: Він вчив мову рік - вода камінь точить. - He studied the language for a year - persistence wins.\n"
            "  3. Не все те золото, що блищить. - Lit: Not all that glitters is gold. Means: Appearances deceive. Ex: Не вір рекламі - не все те золото, що блищить. - Don't trust the ad - appearances deceive.\n"
            "  4. Сім раз відміряй, один раз відріж. - Lit: Measure seven times, cut once. Means: Think before you act. Ex: Сім раз відміряй, один раз відріж - не поспішай. - Think before you act - don't rush.\n"
            "  5. Під лежачий камінь вода не тече. - Lit: Water does not flow under a lying stone. Means: Nothing comes to those who wait passively. Ex: Шукай роботу сам - під лежачий камінь вода не тече. - Look for work yourself - nothing comes to drifters.\n"
            "  6. Слово - не горобець: вилетить - не спіймаєш. - Lit: A word is not a sparrow: once out, you won't catch it. Means: Think before you speak. Ex: Думай, що кажеш: слово - не горобець. - Think about what you say: words can't be unsaid.\n"
            "  7. Хто рано встає, тому Бог дає. - Lit: God gives to him who rises early. Means: The early bird catches the worm. Ex: Вставай рано - хто рано встає, тому Бог дає. - Get up early - the early bird catches the worm.\n"
            "  8. Яблуко від яблуні недалеко падає. - Lit: The apple falls not far from the apple tree. Means: Children resemble parents. Ex: Він такий же впертий, як батько - яблуко від яблуні недалеко падає. - He is as stubborn as his father - like father, like son.\n"
            "  9. За двома зайцями поженешся - жодного не спіймаєш. - Lit: Chase two hares, catch neither. Means: Don't split your focus. Ex: Роби одну справу - за двома зайцями не женися. - Do one thing at a time - don't chase two hares.\n"
            "  10. Клин клином вибивають. - Lit: A wedge is driven out with a wedge. Means: Fight fire with fire. Ex: На грубість відповідай твердо - клин клином вибивають. - Answer rudeness firmly - fight fire with fire.\n"
            "  11. Брати бика за роги. - Lit: To take the bull by the horns. Means: To face a problem boldly. Ex: Бери бика за роги і починай! - Take the bull by the horns and start!\n"
            "  12. Як риба у воді. - Lit: Like a fish in water. Means: Completely at ease. Ex: Він почувається тут як риба у воді. - He feels completely at ease here.\n"
            "  13. Біла ворона. - Lit: A white crow. Means: An odd one out. Ex: Вона біла ворона в цій компанії. - She is the odd one out in this company.\n"
            "  14. Вішати локшину на вуха. - Lit: To hang noodles on someone's ears. Means: To pull someone's leg, to deceive. Ex: Не вір йому - він вішає локшину на вуха. - Don't believe him - he's pulling your leg.\n"
            "  15. Каша в голові. - Lit: Porridge in the head. Means: A muddle, confusion. Ex: Після іспиту в мене каша в голові. - After the exam my head is a muddle.\n"
            "  16. Собаку з’їсти на чомусь. - Lit: To have eaten a dog on something. Means: To be an expert. Ex: Він собаку з’їв на комп’ютерах. - He is an expert on computers.\n"
            "  17. Терпіння і труд все перетруть. - Lit: Patience and labor grind everything down. Means: Perseverance overcomes all. Ex: Вчи мову щодня - терпіння і труд все перетруть. - Study the language daily - perseverance overcomes all.\n"
            "  18. Дареному коневі зубів не дивляться. - Lit: Don't look at a gift horse's teeth. Means: Don't criticize gifts. Ex: Бери подарунок і дякуй - дареному коневі зубів не дивляться. - Take the gift and say thanks - don't look a gift horse in the mouth.\n"
            "  19. Золота середина. - Lit: The golden middle. Means: The happy medium, moderation. Ex: У всьому шукай золоту середину. - In everything seek the golden mean.\n"
            "  20. Мова - душа народу. - Lit: Language is the soul of the people. Means: A people's language is its essence. Ex: Бережімо мову - мова - душа народу. - Let's cherish the language - language is the soul of the people."
        ),
        "how_it_works": (
            "Idioms work as compressed culture: each one packs a whole "
            "situation into a vivid image - water wearing stone, noodles "
            "on ears, porridge in the head. Learn them as unbreakable "
            "units first (the words never change order), then unpack the "
            "literal image, then the real meaning. The example sentence "
            "shows the idiom doing its natural work at the end of a "
            "thought, which is where Ukrainians deploy them - as the "
            "punchline of advice."
        ),
        "key_points": [
            "20 idioms and proverbs: literal translation + real meaning + example sentence.",
            "Core images: water and stone, the sparrow-word, the white crow, noodles on ears.",
            "Learn as fixed units; deploy as the punchline of advice.",
        ],
        "requirements": [
            "Use five idioms in your own sentences this week.",
            "Explain three idioms' literal images to someone else.",
        ],
        "standards": [
            "Idioms are attested Ukrainian proverbs and sayings per the standard phraseological dictionaries.",
            "Example sentences are Signature-generated teaching constructions.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["Вода камінь точить", "горобець", "Біла ворона", "локшину", "душа народу"],
        "sig_lens": (
            "Through the Signature lens each proverb is a sworn coin of "
            "the people: worn smooth by a million hands, its image "
            "stamped too deep to fade."
        ),
        "drill": {
            "idioms": [
                ["Без труда нема плода.", "Without labor there is no fruit.", "No pain, no gain."],
                ["Вода камінь точить.", "Water wears away stone.", "Persistence wins."],
                ["Не все те золото, що блищить.", "Not all that glitters is gold.", "Appearances deceive."],
                ["Сім раз відміряй, один раз відріж.", "Measure seven times, cut once.", "Think before you act."],
                ["Під лежачий камінь вода не тече.", "Water does not flow under a lying stone.", "Nothing comes to drifters."],
                ["Слово - не горобець: вилетить - не спіймаєш.", "A word is not a sparrow.", "Think before you speak."],
                ["Хто рано встає, тому Бог дає.", "God gives to early risers.", "The early bird catches the worm."],
                ["Яблуко від яблуні недалеко падає.", "The apple falls near the tree.", "Like father, like son."],
                ["За двома зайцями поженешся - жодного не спіймаєш.", "Chase two hares, catch neither.", "Don't split focus."],
                ["Клин клином вибивають.", "Drive out a wedge with a wedge.", "Fight fire with fire."],
                ["Брати бика за роги.", "Take the bull by the horns.", "Face problems boldly."],
                ["Як риба у воді.", "Like a fish in water.", "Completely at ease."],
                ["Біла ворона.", "A white crow.", "An odd one out."],
                ["Вішати локшину на вуха.", "Hang noodles on ears.", "To deceive, pull one's leg."],
                ["Каша в голові.", "Porridge in the head.", "Confusion, a muddle."],
                ["Собаку з’їсти на чомусь.", "To have eaten a dog on it.", "To be an expert."],
                ["Терпіння і труд все перетруть.", "Patience and labor grind all.", "Perseverance overcomes all."],
                ["Дареному коневі зубів не дивляться.", "Don't check a gift horse's teeth.", "Don't criticize gifts."],
                ["Золота середина.", "The golden middle.", "Moderation, the happy medium."],
                ["Мова - душа народу.", "Language is the soul of the people.", "Language is a people's essence."],
            ],
        },
    },
    {
        "key": "registers",
        "name": "Formal and Polite Registers",
        "group": "Conversation and Registers",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "15 formal vs informal pairs for letters, business, and elders:\n"
            "  1. informal: Привіт, як справи? - Hi, how are things? / formal: Добрий день! Як ваші справи? - Good day! How are you?\n"
            "  2. informal: Дай мені це. - Give me this. / formal: Будьте ласкаві, дайте мені це. - Please be so kind as to give me this.\n"
            "  3. informal: Ти знаєш? - Do you know? / formal: Чи відомо вам? - Is it known to you?\n"
            "  4. informal: Приходь завтра. - Come tomorrow. / formal: Прошу завітати завтра. - I ask you to visit tomorrow.\n"
            "  5. informal: Напиши мені. - Write to me. / formal: Прошу написати мені. - I request that you write to me.\n"
            "  6. informal: Дякую! - Thanks! / formal: Щиро дякую за допомогу. - I sincerely thank you for the help.\n"
            "  7. informal: Вибач! - Sorry! / formal: Прошу вибачення. - I ask your forgiveness.\n"
            "  8. informal: Бувай! - Bye! / formal: До побачення! - Goodbye!\n"
            "  9. informal: Що ти хочеш? - What do you want? / formal: Чим можу вам допомогти? - How may I help you?\n"
            "  10. informal: Чекай тут. - Wait here. / formal: Зачекайте, будь ласка, тут. - Please wait here.\n"
            "  11. letter opening informal: Привіт, друже! - Hi, friend! / formal: Шановний пане Петренку! - Dear Mr. Petrenko!\n"
            "  12. letter closing informal: Твій Олексій. - Yours, Oleksii. / formal: З повагою, Олексій Петренко. - Respectfully, Oleksii Petrenko.\n"
            "  13. informal: Подзвони мені. - Call me. / formal: Прошу зателефонувати мені. - Please call me.\n"
            "  14. informal: Покажи це. - Show this. / formal: Чи могли б ви це показати? - Could you show this?\n"
            "  15. informal: Іди сюди. - Come here. / formal: Прошу підійти сюди. - Please come here."
        ),
        "how_it_works": (
            "Register works as a three-gear shift. Gear one is the "
            "pronoun: ти commands and plain verbs for friends, Ви forms "
            "for elders and strangers. Gear two is the vocabulary: "
            "прошу, будьте ласкаві, шановний, з повагою replace the "
            "bare imperatives. Gear three is the formula: letters open "
            "with шановний пане/пані + surname in the vocative "
            "(Петренку!) and close with з повагою + full name. Business "
            "Ukrainian runs almost entirely in the formal gear - learn "
            "the 15 formal frames cold and you can write any business "
            "letter."
        ),
        "key_points": [
            "Three gears: ти/Ви pronouns, polite vocabulary, fixed formulas.",
            "Formal requests: прошу + infinitive; будьте ласкаві.",
            "Letter opening: Шановний пане Петренку! closing: З повагою, ...",
            "15 informal/formal pairs with translations.",
        ],
        "requirements": [
            "Write a formal request letter using прошу three times.",
            "Address an elder aloud entirely in the formal gear.",
        ],
        "standards": [
            "Register conventions follow standard business Ukrainian per Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["Шановний", "З повагою", "Будьте ласкаві", "Прошу", "Ви"],
        "sig_lens": (
            "Through the Signature lens register is the sworn wardrobe "
            "of speech: the friend's shirt, the business suit, the "
            "elder's ceremonial robe - and the speaker dresses for the "
            "occasion."
        ),
        "drill": {
            "pairs": [
                ["Привіт, як справи?", "Добрий день! Як ваші справи?"],
                ["Дай мені це.", "Будьте ласкаві, дайте мені це."],
                ["Ти знаєш?", "Чи відомо вам?"],
                ["Приходь завтра.", "Прошу завітати завтра."],
                ["Напиши мені.", "Прошу написати мені."],
                ["Дякую!", "Щиро дякую за допомогу."],
                ["Вибач!", "Прошу вибачення."],
                ["Бувай!", "До побачення!"],
                ["Що ти хочеш?", "Чим можу вам допомогти?"],
                ["Чекай тут.", "Зачекайте, будь ласка, тут."],
                ["Привіт, друже!", "Шановний пане Петренку!"],
                ["Твій Олексій.", "З повагою, Олексій Петренко."],
                ["Подзвони мені.", "Прошу зателефонувати мені."],
                ["Покажи це.", "Чи могли б ви це показати?"],
                ["Іди сюди.", "Прошу підійти сюди."],
            ],
        },
    },
    {
        "key": "complex",
        "name": "Compound and Complex Sentences",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "15 long sentences with clauses, connectors, and relative "
            "clauses - parsed and translated:\n"
            "  1. Я знаю, що ти хочеш сказати. - I know what you want to say. (що = that/what)\n"
            "  2. Книга, яку я читаю, дуже цікава. - The book that I am reading is very interesting. (яку = which, accusative)\n"
            "  3. Чоловік, який стоїть біля вікна, мій брат. - The man who is standing by the window is my brother. (який = who)\n"
            "  4. Ми підемо гуляти, якщо не буде дощу. - We will go for a walk if it does not rain. (якщо = if)\n"
            "  5. Коли я прийшов, усі вже спали. - When I arrived, everyone was already asleep. (коли = when)\n"
            "  6. Вона не прийшла, бо захворіла. - She did not come because she got sick. (бо = because)\n"
            "  7. Я вчу українську, тому що хочу читати Шевченка. - I am learning Ukrainian because I want to read Shevchenko. (тому що = because)\n"
            "  8. Хоча був дощ, ми пішли в похід. - Although it was raining, we went hiking. (хоча = although)\n"
            "  9. Щоб вивчити мову, треба практикуватися щодня. - In order to learn a language, one must practice daily. (щоб = in order to)\n"
            "  10. Дім, де я народився, стоїть на горі. - The house where I was born stands on the hill. (де = where)\n"
            "  11. Скажи мені, коли ти будеш вільний. - Tell me when you will be free.\n"
            "  12. Я не знаю, чи він прийде. - I do not know whether he will come. (чи = whether)\n"
            "  13. Вона така втомлена, що заснула одразу. - She was so tired that she fell asleep at once. (така... що = so... that)\n"
            "  14. Чим більше вчишся, тим більше знаєш. - The more you study, the more you know. (чим... тим = the... the)\n"
            "  15. Ні дощ, ні вітер не зупинили нас. - Neither rain nor wind stopped us. (ні... ні = neither... nor)"
        ),
        "how_it_works": (
            "Complex sentences work by chaining clauses with connectors, "
            "and Ukrainian connectors are precise tools: що introduces "
            "reported content (я знаю, що...), який/яка/яке relativize "
            "with full case agreement (книга, яку я читаю - яку is "
            "accusative because the book is the object of reading), "
            "якщо/коли/бо/тому що/хоча build adverbial clauses, щоб "
            "marks purpose, чи marks embedded yes-no questions. Commas "
            "are the road signs: Ukrainian puts a comma before every "
            "subordinate clause without exception. Master the 15 "
            "connectors and any two simple sentences can become one "
            "complex one."
        ),
        "key_points": [
            "Connectors: що, який, якщо, коли, бо, тому що, хоча, щоб, де, чи.",
            "Relative який agrees in gender/number/case with its antecedent's role.",
            "Correlatives: така... що, чим... тим, ні... ні.",
            "A comma stands before every subordinate clause.",
            "15 parsed sentences with translations.",
        ],
        "requirements": [
            "Join ten pairs of simple sentences with a connector and a comma.",
            "Parse three sentences: name the connector and the clause type.",
        ],
        "standards": [
            "Connector use follows Pugh and Press 1999.",
            "Example sentences are Signature-generated teaching constructions from attested vocabulary.",
        ],
        "citations": [CIT_PUGH, CIT_BILODID],
        "must_contain": ["який", "тому що", "хоча", "щоб", "relative clauses"],
        "sig_lens": (
            "Through the Signature lens connectors are sworn bridges: "
            "що the bridge of knowing, який the bridge of belonging, "
            "бо the bridge of reason - and every comma a toll paid to "
            "clarity."
        ),
        "drill": {
            "sentences": [
                ["Я знаю, що ти хочеш сказати.", "I know what you want to say."],
                ["Книга, яку я читаю, дуже цікава.", "The book that I am reading is very interesting."],
                ["Чоловік, який стоїть біля вікна, мій брат.", "The man who is standing by the window is my brother."],
                ["Ми підемо гуляти, якщо не буде дощу.", "We will go for a walk if it does not rain."],
                ["Коли я прийшов, усі вже спали.", "When I arrived, everyone was already asleep."],
                ["Вона не прийшла, бо захворіла.", "She did not come because she got sick."],
                ["Я вчу українську, тому що хочу читати Шевченка.", "I am learning Ukrainian because I want to read Shevchenko."],
                ["Хоча був дощ, ми пішли в похід.", "Although it was raining, we went hiking."],
                ["Щоб вивчити мову, треба практикуватися щодня.", "In order to learn a language, one must practice daily."],
                ["Дім, де я народився, стоїть на горі.", "The house where I was born stands on the hill."],
                ["Скажи мені, коли ти будеш вільний.", "Tell me when you will be free."],
                ["Я не знаю, чи він прийде.", "I do not know whether he will come."],
                ["Вона така втомлена, що заснула одразу.", "She was so tired that she fell asleep at once."],
                ["Чим більше вчишся, тим більше знаєш.", "The more you study, the more you know."],
                ["Ні дощ, ні вітер не зупинили нас.", "Neither rain nor wind stopped us."],
            ],
            "connectors": ["що", "який", "якщо", "коли", "бо", "тому що",
                           "хоча", "щоб", "де", "чи"],
        },
    },
    {
        "key": "conv_market",
        "name": "Conversation: At the Market",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A 20-line bilingual dialogue at the bazaar, annotated:\n"
            "  Продавець (Seller): Добрий день! Що бажаєте? - Good day! What would you like?\n"
            "  Покупець (Buyer): Добрий день! Скільки коштують помідори? - Good day! How much are the tomatoes?\n"
            "  Продавець: П’ятдесят гривень за кілограм. - Fifty hryvnias a kilo.\n"
            "  Покупець: Ой, дорого! А огірки? - Oh, expensive! And the cucumbers?\n"
            "  Продавець: Огірки дешевші - тридцять. - The cucumbers are cheaper - thirty.\n"
            "  Покупець: Дайте кілограм огірків і пів кіло помідорів. - Give me a kilo of cucumbers and half a kilo of tomatoes.\n"
            "  Продавець: Будь ласка! Щось іще? - Here you are! Anything else?\n"
            "  Покупець: Так, мені потрібен кріп і петрушка. - Yes, I need dill and parsley.\n"
            "  Продавець: Свіжа зелень, сьогодні зірвана. - Fresh greens, picked today.\n"
            "  Покупець: Чудово! Скільки з мене? - Wonderful! How much do I owe?\n"
            "  Продавець: Сто десять гривень. - One hundred ten hryvnias.\n"
            "  Покупець: Зробіть знижку, будь ласка! - Give a discount, please!\n"
            "  Продавець: Добре, сто гривень. Ви постійний покупець. - Fine, one hundred. You are a regular customer.\n"
            "  Покупець: Дякую! Можна карткою? - Thank you! Can I pay by card?\n"
            "  Продавець: Так, прикладіть картку. - Yes, tap your card.\n"
            "  Покупець: Готово! Дякую! - Done! Thank you!\n"
            "  Продавець: Дякую за покупку! Приходьте ще! - Thank you for the purchase! Come again!\n"
            "  Покупець: Обов’язково! До побачення! - Definitely! Goodbye!\n"
            "  Продавець: До побачення! Гарного дня! - Goodbye! Have a nice day!\n"
            "  [Примітка: покупець торгується ввічливо - знижка дається постійним покупцям.] - [Note: the buyer bargains politely - regulars get the discount.]"
        ),
        "how_it_works": (
            "This dialogue works as a complete market transaction in 20 "
            "moves: greeting, price inquiry, reaction, bargaining, "
            "order, add-ons, total, discount request, payment, farewell. "
            "The genitive of quantity runs through it (кілограм огірків, "
            "пів кіло помідорів, сто десять гривень). The seller's "
            "register stays formal (бажаєте, прикладіть), the buyer's "
            "polite but direct. Play both parts aloud - the dialogue is "
            "a script, and fluency is rehearsal."
        ),
        "key_points": [
            "20 lines: full transaction from greeting to farewell.",
            "Genitive of quantity: кілограм огірків, сто гривень.",
            "Bargaining frame: дорого, зробіть знижку; regulars get the price cut.",
            "Payment: можна карткою, прикладіть картку.",
            "Annotated with speaker roles and a cultural note.",
        ],
        "requirements": [
            "Perform the dialogue aloud, playing both roles.",
            "Improvise a second version with different goods.",
        ],
        "standards": [
            "Dialogue is a Signature-generated teaching text in standard literary Ukrainian.",
        ],
        "citations": [CIT_PUGH],
        "must_contain": ["Продавець", "Покупець", "гривень", "знижку", "карткою"],
        "sig_lens": (
            "Through the Signature lens this market dialogue is a sworn "
            "dance of twenty steps: question and answer, price and "
            "counter-price, until both partners bow at до побачення."
        ),
        "drill": {
            "lines": [
                ["Продавець", "Добрий день! Що бажаєте?", "Good day! What would you like?"],
                ["Покупець", "Добрий день! Скільки коштують помідори?", "Good day! How much are the tomatoes?"],
                ["Продавець", "П’ятдесят гривень за кілограм.", "Fifty hryvnias a kilo."],
                ["Покупець", "Ой, дорого! А огірки?", "Oh, expensive! And the cucumbers?"],
                ["Продавець", "Огірки дешевші - тридцять.", "The cucumbers are cheaper - thirty."],
                ["Покупець", "Дайте кілограм огірків і пів кіло помідорів.", "Give me a kilo of cucumbers and half a kilo of tomatoes."],
                ["Продавець", "Будь ласка! Щось іще?", "Here you are! Anything else?"],
                ["Покупець", "Так, мені потрібен кріп і петрушка.", "Yes, I need dill and parsley."],
                ["Продавець", "Свіжа зелень, сьогодні зірвана.", "Fresh greens, picked today."],
                ["Покупець", "Чудово! Скільки з мене?", "Wonderful! How much do I owe?"],
                ["Продавець", "Сто десять гривень.", "One hundred ten hryvnias."],
                ["Покупець", "Зробіть знижку, будь ласка!", "Give a discount, please!"],
                ["Продавець", "Добре, сто гривень. Ви постійний покупець.", "Fine, one hundred. You are a regular customer."],
                ["Покупець", "Дякую! Можна карткою?", "Thank you! Can I pay by card?"],
                ["Продавець", "Так, прикладіть картку.", "Yes, tap your card."],
                ["Покупець", "Готово! Дякую!", "Done! Thank you!"],
                ["Продавець", "Дякую за покупку! Приходьте ще!", "Thank you for the purchase! Come again!"],
                ["Покупець", "Обов’язково! До побачення!", "Definitely! Goodbye!"],
                ["Продавець", "До побачення! Гарного дня!", "Goodbye! Have a nice day!"],
                ["Примітка", "Покупець торгується ввічливо.", "The buyer bargains politely."],
            ],
        },
    },
    {
        "key": "conv_friend",
        "name": "Conversation: Meeting a Friend",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A 20-line bilingual dialogue between friends, annotated:\n"
            "  Олена: Привіт, Тарасе! Скільки років, скільки зим! - Hi, Taras! Long time no see! (lit: how many summers, how many winters)\n"
            "  Тарас: Олено! Яка зустріч! Як ти? - Olena! What a meeting! How are you?\n"
            "  Олена: Чудово! А ти як? - Wonderful! And you?\n"
            "  Тарас: Не скаржуся. Де ти була? - Can't complain. Where have you been?\n"
            "  Олена: Я їздила до Львова. - I went to Lviv.\n"
            "  Тарас: О, Львів! І як тобі? - Oh, Lviv! How did you like it?\n"
            "  Олена: Неймовірно! Кава, старі вулиці... - Amazing! Coffee, old streets...\n"
            "  Тарас: А я був у Карпатах. - And I was in the Carpathians.\n"
            "  Олена: Правда? Розповідай! - Really? Tell me!\n"
            "  Тарас: Ми ходили в гори три дні. - We hiked in the mountains for three days.\n"
            "  Олена: Вау! А погода була гарна? - Wow! Was the weather nice?\n"
            "  Тарас: Перший день - дощ, потім сонце. - First day rain, then sun.\n"
            "  Олена: Слухай, ходімо на каву! - Listen, let's go for coffee!\n"
            "  Тарас: Давай! Тут поруч гарна кав’ярня. - Let's! There's a nice cafe nearby.\n"
            "  Олена: Розкажеш усе детально. - You'll tell me everything in detail.\n"
            "  Тарас: Обіцяю! А ти розкажеш про Львів. - I promise! And you'll tell me about Lviv.\n"
            "  Олена: Домовилися! - Agreed!\n"
            "  Тарас: До речі, як твоя сестра? - By the way, how is your sister?\n"
            "  Олена: Добре! Вона вийшла заміж. - Fine! She got married.\n"
            "  Тарас: Вітаю! Передай вітання! - Congratulations! Give her my regards!\n"
            "  [Примітка: друзі говорять на ти; скільки років, скільки зим - сталий вираз.] - [Note: friends use ти; the greeting is a fixed idiom.]"
        ),
        "how_it_works": (
            "This dialogue works as a reunion in 20 moves: the idiomatic "
            "greeting (скільки років, скільки зим), catching up (де ти "
            "була, як тобі), parallel travel stories, the invitation "
            "(ходімо на каву), the promise exchange, and family news. "
            "Friends speak ти throughout - the whole dialogue is a drill "
            "in the informal register. Past-tense verbs (їздила, був, "
            "ходили) agree with their speakers' genders, proving the "
            "agreement rule in living speech."
        ),
        "key_points": [
            "20 lines: reunion, travel stories, invitation, family news.",
            "Informal ти register throughout.",
            "Fixed idiom: скільки років, скільки зим (long time no see).",
            "Past-tense gender agreement in dialogue: їздила (she), був (he).",
            "Annotated with speaker roles and a cultural note.",
        ],
        "requirements": [
            "Perform the dialogue with a partner, then swap roles.",
            "Tell your own travel story in five lines of dialogue.",
        ],
        "standards": [
            "Dialogue is a Signature-generated teaching text in standard literary Ukrainian.",
        ],
        "citations": [CIT_PUGH],
        "must_contain": ["Олена", "Тарас", "скільки зим", "кав’ярня", "Домовилися"],
        "sig_lens": (
            "Through the Signature lens this reunion is a sworn "
            "rekindling: two roads that parted, twenty lines that join "
            "them again over coffee."
        ),
        "drill": {
            "lines": [
                ["Олена", "Привіт, Тарасе! Скільки років, скільки зим!", "Hi, Taras! Long time no see!"],
                ["Тарас", "Олено! Яка зустріч! Як ти?", "Olena! What a meeting! How are you?"],
                ["Олена", "Чудово! А ти як?", "Wonderful! And you?"],
                ["Тарас", "Не скаржуся. Де ти була?", "Can't complain. Where have you been?"],
                ["Олена", "Я їздила до Львова.", "I went to Lviv."],
                ["Тарас", "О, Львів! І як тобі?", "Oh, Lviv! How did you like it?"],
                ["Олена", "Неймовірно! Кава, старі вулиці...", "Amazing! Coffee, old streets..."],
                ["Тарас", "А я був у Карпатах.", "And I was in the Carpathians."],
                ["Олена", "Правда? Розповідай!", "Really? Tell me!"],
                ["Тарас", "Ми ходили в гори три дні.", "We hiked in the mountains for three days."],
                ["Олена", "Вау! А погода була гарна?", "Wow! Was the weather nice?"],
                ["Тарас", "Перший день - дощ, потім сонце.", "First day rain, then sun."],
                ["Олена", "Слухай, ходімо на каву!", "Listen, let's go for coffee!"],
                ["Тарас", "Давай! Тут поруч гарна кав’ярня.", "Let's! There's a nice cafe nearby."],
                ["Олена", "Розкажеш усе детально.", "You'll tell me everything in detail."],
                ["Тарас", "Обіцяю! А ти розкажеш про Львів.", "I promise! And you'll tell me about Lviv."],
                ["Олена", "Домовилися!", "Agreed!"],
                ["Тарас", "До речі, як твоя сестра?", "By the way, how is your sister?"],
                ["Олена", "Добре! Вона вийшла заміж.", "Fine! She got married."],
                ["Тарас", "Вітаю! Передай вітання!", "Congratulations! Give her my regards!"],
            ],
        },
    },
    {
        "key": "conv_problem",
        "name": "Conversation: Solving a Problem",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A 20-line bilingual dialogue solving a lost-wallet problem, annotated:\n"
            "  Марічка: Ой! Я загубила гаманець! - Oh! I lost my wallet!\n"
            "  Петро: Спокійно! Де ти його бачила востаннє? - Calmly! Where did you last see it?\n"
            "  Марічка: У кафе, на столі. - At the cafe, on the table.\n"
            "  Петро: Ходімо туди зараз! - Let's go there right now!\n"
            "  Марічка: А якщо його вже немає? - And if it's already gone?\n"
            "  Петро: Тоді запитаємо офіціанта. - Then we'll ask the waiter.\n"
            "  Офіціант: Добрий день! Чим допомогти? - Good day! How can I help?\n"
            "  Марічка: Я загубила тут гаманець. Ви не бачили? - I lost my wallet here. Haven't you seen it?\n"
            "  Офіціант: Який він? Опишіть, будь ласка. - What does it look like? Please describe it.\n"
            "  Марічка: Чорний, шкіряний, з блискавкою. - Black, leather, with a zipper.\n"
            "  Офіціант: Хвилинку... Так! Ось він! - One moment... Yes! Here it is!\n"
            "  Марічка: Ура! Дякую вам велике! - Hurray! Thank you so much!\n"
            "  Петро: Перевір, чи все на місці. - Check whether everything is in place.\n"
            "  Марічка: Гроші є, картки є. Усе добре! - The money is there, the cards are there. All good!\n"
            "  Офіціант: Радий допомогти! - Glad to help!\n"
            "  Марічка: Ви врятували мій день! - You saved my day!\n"
            "  Петро: Бачиш? Усе вирішилося! - See? Everything worked out!\n"
            "  Марічка: Тепер я буду обережніша. - Now I will be more careful. (woman speaking)\n"
            "  Петро: І я тобі нагадаю. - And I'll remind you.\n"
            "  Марічка: Домовилися! Дякую! - Agreed! Thank you!\n"
            "  [Примітка: проблема вирішується крок за кроком - заспокоїти, згадати, повернутися, запитати, перевірити.] - [Note: the problem is solved step by step - calm, recall, return, ask, verify.]"
        ),
        "how_it_works": (
            "This dialogue works as a problem-solving protocol in 20 "
            "moves: panic, calming, recall, return, contingency (а якщо), "
            "asking for help, describing the lost object, recovery, "
            "verification, gratitude, resolution. The register shifts "
            "with the addressee - ти between friends, ви to the waiter. "
            "The description sequence (чорний, шкіряний, з блискавкою) "
            "drills adjective stacking under pressure. Learn the five "
            "steps of the note and any lost-object crisis in Ukraine is "
            "solvable."
        ),
        "key_points": [
            "20 lines: panic to resolution in five steps.",
            "Register shift: ти with friends, ви with the waiter.",
            "Object description: чорний, шкіряний, з блискавкою.",
            "Contingency frame: а якщо...? тоді...",
            "Annotated with speaker roles and a problem-solving note.",
        ],
        "requirements": [
            "Perform the dialogue, then improvise a lost-keys version.",
            "Describe three of your belongings as if reporting them lost.",
        ],
        "standards": [
            "Dialogue is a Signature-generated teaching text in standard literary Ukrainian.",
        ],
        "citations": [CIT_PUGH],
        "must_contain": ["гаманець", "Офіціант", "блискавкою", "вирішилося", "обережніша"],
        "sig_lens": (
            "Through the Signature lens this crisis is a sworn trial: "
            "panic the first seal, calm the second, and the recovered "
            "wallet the third - the covenant that nothing truly lost "
            "stays lost."
        ),
        "drill": {
            "lines": [
                ["Марічка", "Ой! Я загубила гаманець!", "Oh! I lost my wallet!"],
                ["Петро", "Спокійно! Де ти його бачила востаннє?", "Calmly! Where did you last see it?"],
                ["Марічка", "У кафе, на столі.", "At the cafe, on the table."],
                ["Петро", "Ходімо туди зараз!", "Let's go there right now!"],
                ["Марічка", "А якщо його вже немає?", "And if it's already gone?"],
                ["Петро", "Тоді запитаємо офіціанта.", "Then we'll ask the waiter."],
                ["Офіціант", "Добрий день! Чим допомогти?", "Good day! How can I help?"],
                ["Марічка", "Я загубила тут гаманець. Ви не бачили?", "I lost my wallet here. Haven't you seen it?"],
                ["Офіціант", "Який він? Опишіть, будь ласка.", "What does it look like? Please describe it."],
                ["Марічка", "Чорний, шкіряний, з блискавкою.", "Black, leather, with a zipper."],
                ["Офіціант", "Хвилинку... Так! Ось він!", "One moment... Yes! Here it is!"],
                ["Марічка", "Ура! Дякую вам велике!", "Hurray! Thank you so much!"],
                ["Петро", "Перевір, чи все на місці.", "Check whether everything is in place."],
                ["Марічка", "Гроші є, картки є. Усе добре!", "The money is there, the cards are there. All good!"],
                ["Офіціант", "Радий допомогти!", "Glad to help!"],
                ["Марічка", "Ви врятували мій день!", "You saved my day!"],
                ["Петро", "Бачиш? Усе вирішилося!", "See? Everything worked out!"],
                ["Марічка", "Тепер я буду обережніша.", "Now I will be more careful."],
                ["Петро", "І я тобі нагадаю.", "And I'll remind you."],
                ["Марічка", "Домовилися! Дякую!", "Agreed! Thank you!"],
            ],
        },
    },
    {
        "key": "mastery",
        "name": "Mastery Review and Full Reference",
        "group": "Mastery Reference",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The whole database in one teaching summary: the alphabet, "
            "200 core words, the key grammar, and every phrase table. \n\n"
            "Alphabet (33 letters): А Б В Г Ґ Д Е Є Ж З И І Ї Й К Л М Н "
            "О П Р С Т У Ф Х Ц Ч Ш Щ Ь Ю Я. Vowel letters: А Е Є И І Ї О "
            "У Ю Я. Six vowel phonemes: а е и і о у. Stress is free and "
            "mobile. \n\n"
            "Seven cases: називний (nominative), родовий (genitive), "
            "давальний (dative), знахідний (accusative), орудний "
            "(instrumental), місцевий (locative), кличний (vocative). "
            "Three genders: masculine, feminine, neuter. Two verb "
            "conjugations: I (писати - пишеш), II (говорити - говориш). "
            "Aspect: imperfective (ongoing) vs perfective (completed). "
            "No articles. Double negation required. Questions by "
            "intonation, чи, or question words. \n\n"
            "200 core words (Ukrainian - English), the working vocabulary "
            "of this entire database:\n"
            "  я-I, ти-you(inf), він-he, вона-she, воно-it, ми-we, ви-you(form), вони-they,\n"
            "  мій-my, твій-your, його-his, її-her, наш-our, ваш-your(form), їхній-their,\n"
            "  цей-this, той-that, хто-who, що-what, де-where, коли-when, чому-why, як-how,\n"
            "  один-one, два-two, три-three, чотири-four, п’ять-five, десять-ten, сто-hundred,\n"
            "  чоловік-man, жінка-woman, дитина-child, друг-friend, мама-mom, тато-dad,\n"
            "  дім-house, кімната-room, стіл-table, вікно-window, двері-door, книга-book,\n"
            "  вода-water, хліб-bread, молоко-milk, м’ясо-meat, суп-soup, борщ-borscht,\n"
            "  сонце-sun, місяць-moon, день-day, ніч-night, рік-year, час-time,\n"
            "  рука-hand, голова-head, око-eye, серце-heart, нога-leg,\n"
            "  великий-big, малий-small, новий-new, старий-old, добрий-good, поганий-bad,\n"
            "  гарний-beautiful, довгий-long, високий-tall, теплий-warm, холодний-cold,\n"
            "  червоний-red, синій-blue, зелений-green, чорний-black, білий-white,\n"
            "  бути-to be, мати-to have, робити-to do, говорити-to speak, читати-to read,\n"
            "  писати-to write, їсти-to eat, пити-to drink, спати-to sleep, йти-to go,\n"
            "  їхати-to ride, знати-to know, думати-to think, любити-to love, хотіти-to want,\n"
            "  бачити-to see, чути-to hear, давати-to give, брати-to take, жити-to live,\n"
            "  працювати-to work, вчитися-to study, могти-can,\n"
            "  швидко-quickly, добре-well, дуже-very, завжди-always, ніколи-never,\n"
            "  тут-here, там-there, сьогодні-today, учора-yesterday, завтра-tomorrow,\n"
            "  привіт-hi, дякую-thank you, будь ласка-please, до побачення-goodbye,\n"
            "  так-yes, ні-no, не-not, і-and, але-but, бо-because, якщо-if,\n"
            "  школа-school, робота-work, місто-city, країна-country, вулиця-street,\n"
            "  гроші-money, ціна-price, магазин-shop, ринок-market,\n"
            "  весна-spring, літо-summer, осінь-autumn, зима-winter,\n"
            "  понеділок-Monday, вівторок-Tuesday, середа-Wednesday, четвер-Thursday,\n"
            "  п’ятниця-Friday, субота-Saturday, неділя-Sunday,\n"
            "  січень-January, лютий-February, березень-March, квітень-April, травень-May,\n"
            "  червень-June, липень-July, серпень-August, вересень-September,\n"
            "  жовтень-October, листопад-November, грудень-December,\n"
            "  телефон-phone, комп’ютер-computer, інтернет-internet,\n"
            "  щастя-happiness, любов-love, здоров’я-health, мова-language, слово-word,\n"
            "  Україна-Ukraine, Київ-Kyiv, Львів-Lviv, Дніпро-Dnipro.\n\n"
            "Phrase tables: greetings (доброго ранку, добрий день, добрий "
            "вечір, привіт, до побачення), politeness (дякую, будь "
            "ласка, вибачте, смачного), travel (де вокзал, скільки "
            "коштує, два квитки), shopping (дорого, зробіть знижку, чек), "
            "health (болить голова, викличте лікаря, аптека). \n\n"
            "Grammar at a glance: книга/книги/книзі/книгу/книгою/книзі/"
            "книго; читаю/читаєш/читає; читав/читала/читало/читали; "
            "читатиму/буду читати/прочитаю; читай/читайте; я знаю, що...; "
            "книга, яку читаю; якщо...; хоча...; щоб... \n\n"
            "You have climbed the ladder: foundations (the language, its "
            "letters, its sounds), core vocabulary (nouns, verbs, "
            "describers, pointers, counters, greetings), grammar "
            "essentials (the ten rules), everyday themes (ten worlds of "
            "sentences), grammar in action (tenses, questions, commands, "
            "descriptions), stories and idioms (three tales, twenty "
            "proverbs), conversation and registers (three dialogues, "
            "formal speech, complex sentences) - and this summit, the "
            "whole language in one page."
        ),
        "how_it_works": (
            "This record works as the summit and the map at once: "
            "everything taught across the 33 earlier records is "
            "compressed into recallable form - the alphabet in one "
            "line, the cases in one line, the conjugations in one line, "
            "the 200 words in one list, the phrases in one table. Use it "
            "three ways: as a placement test (read it cold - what you "
            "recognize is what you have learned), as a daily drill "
            "(one section per day, cycling), and as a launchpad (any "
            "word or rule you have forgotten points back to its record). "
            "The database is now a circle: the end teaches the "
            "beginning."
        ),
        "key_points": [
            "Full alphabet, six vowels, free stress, in one line.",
            "Seven cases, three genders, two conjugations, aspect - one line each.",
            "200 core words: the working vocabulary of the whole database.",
            "Phrase tables: greetings, politeness, travel, shopping, health.",
            "Grammar at a glance: full paradigms in miniature.",
        ],
        "requirements": [
            "Read the 200 words aloud weekly until all are instant.",
            "Use this page as the index: any forgotten rule sends you back to its record.",
        ],
        "standards": [
            "Reference content is consolidated from the 33 earlier records of this database.",
            "Word list is a Signature-generated selection from attested vocabulary.",
        ],
        "citations": [CIT_SHEVELOV, CIT_PUGH, CIT_BILODID, CIT_ISO],
        "must_contain": ["200 core words", "Seven cases", "33 letters", "Aspect", "ladder"],
        "sig_lens": (
            "Through the Signature lens this summit is the sworn seal "
            "on the whole ascent: thirty-three records the mountain, "
            "this page the flag planted at the top - and the view from "
            "it is the entire language."
        ),
        "drill": {
            "words": [
                ["я", "I"], ["ти", "you (inf)"], ["він", "he"], ["вона", "she"],
                ["воно", "it"], ["ми", "we"], ["ви", "you (form)"], ["вони", "they"],
                ["мій", "my"], ["твій", "your"], ["його", "his"], ["її", "her"],
                ["наш", "our"], ["ваш", "your (form)"], ["їхній", "their"],
                ["цей", "this"], ["той", "that"], ["хто", "who"], ["що", "what"],
                ["де", "where"], ["коли", "when"], ["чому", "why"], ["як", "how"],
                ["один", "one"], ["два", "two"], ["три", "three"], ["чотири", "four"],
                ["п’ять", "five"], ["десять", "ten"], ["сто", "hundred"],
                ["скільки", "how many"], ["який", "which"],
                ["чоловік", "man"], ["жінка", "woman"], ["дитина", "child"],
                ["друг", "friend"], ["мама", "mom"], ["тато", "dad"],
                ["брат", "brother"], ["сестра", "sister"], ["дідусь", "grandfather"],
                ["бабуся", "grandmother"], ["сім’я", "family"],
                ["дім", "house"], ["кімната", "room"], ["стіл", "table"],
                ["вікно", "window"], ["двері", "door"], ["книга", "book"],
                ["вода", "water"], ["хліб", "bread"], ["молоко", "milk"],
                ["м’ясо", "meat"], ["суп", "soup"], ["борщ", "borscht"],
                ["каша", "porridge"], ["чай", "tea"], ["кава", "coffee"],
                ["яблуко", "apple"], ["сонце", "sun"], ["місяць", "moon"],
                ["день", "day"], ["ніч", "night"], ["рік", "year"], ["час", "time"],
                ["тиждень", "week"], ["рука", "hand"], ["голова", "head"],
                ["око", "eye"], ["серце", "heart"], ["нога", "leg"],
                ["великий", "big"], ["малий", "small"], ["новий", "new"],
                ["старий", "old"], ["добрий", "good"], ["поганий", "bad"],
                ["гарний", "beautiful"], ["довгий", "long"], ["високий", "tall"],
                ["теплий", "warm"], ["холодний", "cold"], ["швидкий", "fast"],
                ["червоний", "red"], ["синій", "blue"], ["зелений", "green"],
                ["чорний", "black"], ["білий", "white"], ["жовтий", "yellow"],
                ["бути", "to be"], ["мати", "to have"], ["робити", "to do"],
                ["говорити", "to speak"], ["читати", "to read"], ["писати", "to write"],
                ["їсти", "to eat"], ["пити", "to drink"], ["спати", "to sleep"],
                ["йти", "to go"], ["їхати", "to ride"], ["прийти", "to come"],
                ["знати", "to know"], ["думати", "to think"], ["любити", "to love"],
                ["хотіти", "to want"], ["бачити", "to see"], ["чути", "to hear"],
                ["давати", "to give"], ["брати", "to take"], ["жити", "to live"],
                ["працювати", "to work"], ["вчитися", "to study"], ["могти", "can"],
                ["швидко", "quickly"], ["добре", "well"], ["дуже", "very"],
                ["завжди", "always"], ["ніколи", "never"], ["часто", "often"],
                ["тут", "here"], ["там", "there"], ["сьогодні", "today"],
                ["учора", "yesterday"], ["завтра", "tomorrow"], ["тепер", "now"],
                ["привіт", "hi"], ["дякую", "thank you"], ["будь ласка", "please"],
                ["до побачення", "goodbye"], ["вибачте", "sorry"],
                ["так", "yes"], ["ні", "no"], ["не", "not"], ["і", "and"],
                ["але", "but"], ["бо", "because"], ["якщо", "if"],
                ["школа", "school"], ["робота", "work"], ["місто", "city"],
                ["країна", "country"], ["вулиця", "street"], ["село", "village"],
                ["гроші", "money"], ["ціна", "price"], ["магазин", "shop"],
                ["ринок", "market"], ["квиток", "ticket"],
                ["весна", "spring"], ["літо", "summer"], ["осінь", "autumn"],
                ["зима", "winter"], ["погода", "weather"], ["дощ", "rain"],
                ["сніг", "snow"], ["вітер", "wind"],
                ["понеділок", "Monday"], ["вівторок", "Tuesday"], ["середа", "Wednesday"],
                ["четвер", "Thursday"], ["п’ятниця", "Friday"], ["субота", "Saturday"],
                ["неділя", "Sunday"],
                ["січень", "January"], ["лютий", "February"], ["березень", "March"],
                ["квітень", "April"], ["травень", "May"], ["червень", "June"],
                ["липень", "July"], ["серпень", "August"], ["вересень", "September"],
                ["жовтень", "October"], ["листопад", "November"], ["грудень", "December"],
                ["телефон", "phone"], ["комп’ютер", "computer"], ["інтернет", "internet"],
                ["фото", "photo"], ["лист", "letter"],
                ["щастя", "happiness"], ["любов", "love"], ["здоров’я", "health"],
                ["мова", "language"], ["слово", "word"], ["народ", "people"],
                ["Україна", "Ukraine"], ["Київ", "Kyiv"], ["Львів", "Lviv"],
                ["Дніпро", "Dnipro"], ["світ", "world"],
                ["квітка", "flower"], ["дерево", "tree"], ["птах", "bird"],
                ["риба", "fish"], ["кіт", "cat"], ["собака", "dog"],
                ["гора", "mountain"], ["річка", "river"], ["озеро", "lake"],
            ],
            "cases": 7,
            "letters": 33,
        },
    },
]
