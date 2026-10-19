#!/usr/bin/env python3
"""Entries for the Indonesian to English databases (Manon's language project, 2026-10-17).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,750 databases) PLUS
every shard index title in jah-databases-data-1: zero 'language-indonesian*'
slugs; ID prefixes JAH-LIND- (public) and JAH-LINDS- (signature) verified
free in the manifest id_prefix values AND in every shard index (zero zgrep
hits for 'JAH-LIND' across all index.jsonl.gz files). Pre-authoring
whole-system dedupe-gate check over all 68 planned titles (34 records + 34
Signature Edition titles): zero collisions, zero refusals.

This build creates two NEW databases, 34 ladder-ordered records each:

  language-indonesian           - The Indonesian to English Database
                                    (public-harvest: real, fact-checked
                                    Indonesian - overview, the Latin writing
                                    system, phonology, core vocabulary with
                                    sentences, grammar essentials, themed
                                    sentence sets, verb tenses and aspect,
                                    questions and answers, commands,
                                    descriptions, stories, idioms and
                                    proverbs, registers, complex sentences,
                                    conversations, mastery reference;
                                    standard references Sneddon 1996, 2010,
                                    Alwi et al. 2003, Echols & Shadily 1989,
                                    ISO 639 id/ind)
  language-indonesian-signature - The Indonesian to English Signature
                                    Database
                                    (his original Signature Language Method:
                                    every letter a sworn mark, every affix a
                                    sealed vow, every sentence a covenant of
                                    meaning; src signature, titles suffixed
                                    " (Signature Edition)", clearly labeled
                                    Signature-made, never presented as
                                    authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record carries Indonesian content with English translation + example
sentences. Sentences are required in EVERY record - no vocabulary-list-only
records.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_indonesian.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and ends
with the OK marker; the build machine-executes all 68 demos before writing.

Build-time cross-check: every entry declares 'must_contain' strings and the
build asserts each one appears verbatim in the record description, so entry
text and demo outputs can never drift apart.

No website references. Screened per canon.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every letter a sworn mark, every affix a sealed vow, every "
            "sentence a covenant of meaning. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_SNEDDON_G = ("Sneddon JN. Indonesian: A Comprehensive Grammar. 2nd ed. "
                 "Routledge; 2010.")
CIT_SNEDDON_R = ("Sneddon JN. Indonesian Reference Grammar. Allen & Unwin; "
                 "1996.")
CIT_ALWI = ("Alwi H, Dardjowidjojo S, Lapoliwa H, Moeliono AM. Tata Bahasa "
            "Baku Bahasa Indonesia. 3rd ed. Balai Pustaka; 2003.")
CIT_ECHOLS = ("Echols JM, Shadily H. Kamus Indonesia-Inggris: An Indonesian-"
              "English Dictionary. 3rd ed. Cornell University Press; 1989.")
CIT_ISO = ("ISO 639: Indonesian is coded id (ISO 639-1) and ind (ISO 639-3); "
           "the EYD spelling system was adopted in 1972, revised as EBI in "
           "2015.")
CIT_ASEAN = ("The Association of Southeast Asian Nations uses Indonesian as "
             "a working language alongside English.")

# The 26-letter Indonesian alphabet (Latin/Rumi script, EYD/EBI spelling).
# (letter, English approximation). All letters are pronounced; spelling is
# nearly phonetic.
ALPHABET = [
    ("a", "a as in father"), ("b", "b as in boy"), ("c", "ch as in church"),
    ("d", "d as in dog"), ("e", "e as in bed OR the schwa uh in about"),
    ("f", "f as in fan"), ("g", "hard g as in go, never soft"),
    ("h", "h as in hat"), ("i", "i as in machine"), ("j", "j as in jump"),
    ("k", "k as in kite"), ("l", "l as in love"), ("m", "m as in man"),
    ("n", "n as in name"), ("o", "o as in go"), ("p", "p as in pen"),
    ("q", "q as in Quran, mostly in Arabic loans"), ("r", "trilled r"),
    ("s", "s as in sun"), ("t", "t as in top"), ("u", "u as in moon"),
    ("v", "v as in van, mostly in loans"), ("w", "w as in water"),
    ("x", "x as in box, mostly in loans"), ("y", "y as in yes"),
    ("z", "z as in zebra"),
]
VOWELS = ["a", "e", "i", "o", "u"]
DIGRAPHS = ["kh", "ng", "ny", "sy"]
DIPHTHONGS = ["ai", "au", "oi"]


def _alpha_lines():
    return "\n".join("  %s  - %s" % (ch, note) for ch, note in ALPHABET)


ENTRIES = [
    {
        "key": "overview",
        "name": "Indonesian Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Indonesian (Bahasa Indonesia, literally the language of "
            "Indonesia) is the Austronesian language of the Malayo-"
            "Polynesian branch and the Malayic group that unites the "
            "Indonesian archipelago. It carries ISO codes id (ISO 639-1) "
            "and ind (ISO 639-3). About 43 million people speak it as a "
            "mother tongue, and more than 200 million speak it in total "
            "when the hundreds of millions who use it as a second language "
            "across the islands are counted, making it one of the most "
            "spoken languages on earth. \n\n"
            "Where it is spoken. The homeland is the Republic of Indonesia "
            "- Java, Sumatra, Kalimantan, Sulawesi, Bali, Nusa Tenggara, "
            "Maluku, and Papua - a nation of more than 17,000 islands and "
            "over 700 living regional languages. Indonesian is also used in "
            "East Timor, in Malaysian and Singaporean border trade, and by "
            "diaspora communities in the Netherlands, Australia, and "
            "beyond. \n\n"
            "Official status. Indonesian is the sole official and national "
            "language of Indonesia, fixed by the 1945 constitution, and a "
            "working language of ASEAN. \n\n"
            "How it was born. On 28 October 1928 the Youth Pledge (Sumpah "
            "Pemuda) proclaimed one motherland, one nation, and one "
            "language - Bahasa Indonesia. It grew from Riau Malay, the "
            "trade Malay of the straits, deliberately chosen because it "
            "belonged to no single dominant ethnic group, and was "
            "standardized after independence in 1945. \n\n"
            "Dialects and registers. Standard Indonesian is the language of "
            "school, news, and government. Daily speech runs on regional "
            "varieties - Jakarta Indonesian, Javanese-flavored Indonesian, "
            "Medan, Makassar, and Papuan varieties - and on hundreds of "
            "local languages such as Javanese, Sundanese, and Balinese "
            "spoken at home. Formal Indonesian (Bahasa Indonesia baku) and "
            "colloquial Indonesian are two ends of one living spectrum. \n\n"
            "What makes Indonesian learnable. The alphabet is the familiar "
            "26-letter Latin script and spelling is nearly phonetic; word "
            "order is the familiar subject-verb-object; there are no verb "
            "conjugations, no noun genders, and no cases - tense rides on "
            "small time words like sudah (already), sedang (in progress), "
            "and akan (will). Learn the affixes, learn the time words, and "
            "the language opens like a door. \n\n"
            "First sentences in Bahasa Indonesia:\n"
            "  Halo! - Hello!\n"
            "  Nama saya Manon. - My name is Manon.\n"
            "  Saya suka Bahasa Indonesia. - I like the Indonesian language.\n"
            "  Saya mulai belajar Bahasa Indonesia hari ini. - I started "
            "learning Indonesian today."
        ),
        "how_it_works": (
            "This record is the map of the whole database. It fixes the "
            "identity of the language - name (Bahasa Indonesia), codes "
            "(id / ind), family (Austronesian, Malayo-Polynesian, "
            "Malayic), speaker scale (about 43 million native, more than "
            "200 million total), territory (the Indonesian archipelago "
            "plus East Timor and the diaspora), official standing "
            "(Indonesia, ASEAN working language), the birth story (Youth "
            "Pledge 1928, Riau Malay base, standardized 1945), and the "
            "register spectrum (baku formal standard through colloquial "
            "daily varieties). Every later record hangs facts on this "
            "frame: the alphabet record spells the 26 letters, the "
            "phonology record sounds the vowels and digraphs, the "
            "vocabulary records fill the word-hoard, and the grammar "
            "records assemble the affix engine. Work through the ladder in "
            "order and each record assumes only what earlier records "
            "taught."
        ),
        "key_points": [
            "Native name: Bahasa Indonesia; ISO 639-1 id, ISO 639-3 ind.",
            "Family: Austronesian, Malayo-Polynesian branch, Malayic group.",
            "About 43 million native speakers; more than 200 million total with second-language users.",
            "Sole official language of Indonesia (1945 constitution); ASEAN working language.",
            "Born 28 October 1928 in the Youth Pledge; standardized from Riau Malay after 1945.",
            "Standard baku Indonesian for school and news; lively colloquial varieties for daily life.",
            "SVO word order; tense carried by time words (sudah, sedang, akan); no conjugations, genders, or cases.",
        ],
        "requirements": [
            "No prior knowledge of any Austronesian language is assumed.",
            "Read the alphabet record before the phonology record; read the phonology record before the vocabulary records.",
        ],
        "standards": [
            "Speaker figures are rounded public estimates; the record states them as approximate.",
            "Family and history claims follow the standard references: Sneddon 1996, 2010; Alwi et al. 2003.",
            "All example sentences are glossed word-for-word where the grammar is new.",
        ],
        "citations": [CIT_SNEDDON_R, CIT_ALWI, CIT_ISO, CIT_ASEAN],
        "must_contain": ["Bahasa Indonesia", "id", "ind", "Austronesian", "Riau Malay", "43 million"],
        "sig_lens": (
            "Through the Signature lens this overview is a census of an "
            "archipelago of speakers: every headcount a sworn roll-call, "
            "every island a seal on the covenant that these 17,000 islands "
            "speak with one national voice, carried whole into the archive."
        ),
        "drill": {
            "native_m": 43.0, "total_m": 210.0, "islands": 17000,
            "regional_langs": 700, "iso1": "id", "iso3": "ind",
            "pledge_year": 1928, "indep_year": 1945, "eyd_year": 1972,
            "regions": ["Java", "Sumatra", "Kalimantan", "Sulawesi", "Bali",
                        "Nusa Tenggara", "Maluku", "Papua"],
            "registers": ["baku", "colloquial Jakarta", "Medan", "Makassar",
                          "Papuan", "Javanese-flavored"],
        },
    },
    {
        "key": "writing",
        "name": "The Indonesian Writing System",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Indonesian is written in the Latin alphabet - the Rumi script - "
            "with 26 letters, exactly the English A to Z, and the spelling "
            "is nearly phonetic: words are pronounced as they are written. "
            "The modern spelling system (EYD, Ejaan Yang Disempurnakan, "
            "adopted 1972 and revised as EBI, Ejaan Bahasa Indonesia, in "
            "2015) fixed the rules still used today. \n\n"
            "The alphabet, letter by letter:\n" + _alpha_lines() + "\n\n"
            "The five vowels. a, e, i, o, u. The letter e has two sounds: "
            "the clear e as in bed (enak = delicious) and the schwa uh as "
            "in about (emas = gold, pronounced uh-mas). \n\n"
            "Digraphs - two letters, one sound. Indonesian has four: kh "
            "(throaty, like Scottish loch, in khusus = special), ng (the "
            "sing sound, in bunga = flower), ny (like the Spanish n with a "
            "tilde, as in canyon, in minyak = oil), and sy (sh as in ship, "
            "in syarat = condition). \n\n"
            "Diphthongs. Three vowel glides: ai (pantai = beach), au (laut "
            "= sea), oi (amboi, an exclamation). \n\n"
            "Direction and punctuation. Indonesian runs left to right, uses "
            "the same punctuation as English (period, comma, question "
            "mark), and capitalizes sentence starts and proper names the "
            "same way. Numerals are the ordinary Arabic digits 0-9. \n\n"
            "Hyphens do real work. Reduplication - the plural and "
            "emphasis engine - is written with a hyphen: buku-buku "
            "(books), anak-anak (children), besar-besar (very big). \n\n"
            "The older scripts. Before Latin, Malay was written for "
            "centuries in Jawi, an Arabic-based script still seen on "
            "signs, coins, and religious texts in Malaysia and Brunei; "
            "the Pegon variant served Javanese Islamic scholarship. "
            "Knowing they exist explains the many Arabic loanwords in the "
            "vocabulary records. \n\n"
            "First written sentences:\n"
            "  Saya membaca buku. - I read a book.\n"
            "  Anak-anak bermain di pantai. - The children play at the "
            "beach.\n"
            "  Minyak dan bunga ada di meja. - The oil and the flowers are "
            "on the table."
        ),
        "how_it_works": (
            "This record teaches the 26 letters as a sound map, not a "
            "memorization list. Each letter is paired with an English "
            "approximation so an English reader can sound out any word on "
            "first sight. The four digraphs (kh, ng, ny, sy) and three "
            "diphthongs (ai, au, oi) are the only letter combinations that "
            "break the one-letter-one-sound rule, so they get their own "
            "drills. The hyphen rule for reduplication is introduced here "
            "because the plural system of record 10 depends on it, and the "
            "Jawi note gives the historical key to the Arabic loanwords in "
            "the vocabulary records."
        ),
        "key_points": [
            "26-letter Latin (Rumi) alphabet; spelling is nearly phonetic.",
            "Modern spelling: EYD 1972, revised as EBI 2015.",
            "Five vowels a, e, i, o, u; e has two sounds (bed-e and schwa).",
            "Four digraphs: kh (loch), ng (sing), ny (canyon), sy (ship).",
            "Three diphthongs: ai, au, oi.",
            "Left to right; same punctuation and digits as English.",
            "Reduplication written with a hyphen: buku-buku.",
            "Jawi (Arabic-based) was the historic script of Malay.",
        ],
        "requirements": [
            "Read the overview record first for the language's identity and codes.",
            "Practice sounding out each digraph aloud before the phonology record.",
        ],
        "standards": [
            "Letter names and sounds follow EBI (Ejaan Bahasa Indonesia) 2015.",
            "Loan letters q, v, x appear almost only in foreign and Arabic-origin words.",
        ],
        "citations": [CIT_SNEDDON_R, CIT_ALWI, CIT_ISO],
        "must_contain": ["Rumi", "EYD", "Digraphs", "buku-buku", "Jawi", "26"],
        "sig_lens": (
            "Through the Signature lens each letter is a sworn mark on the "
            "page: twenty-six seals of the covenant, four digraphs where "
            "two marks speak with one voice, and the hyphen a binding "
            "cord that doubles a word into a multitude."
        ),
        "drill": {
            "letters": [c for c, _ in ALPHABET],
            "vowels": VOWELS, "digraphs": DIGRAPHS, "diphthongs": DIPHTHONGS,
            "direction": "left-to-right", "loan_letters": ["q", "v", "x"],
            "eyd": 1972, "ebi": 2015, "redupe_example": "buku-buku",
        },
    },
    {
        "key": "pronunciation",
        "name": "Indonesian Pronunciation and Phonology",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Indonesian pronunciation is famously regular: learn the letter "
            "sounds once and you can read the whole language aloud. There "
            "are no tones - pitch never changes a word's meaning - and "
            "stress falls on the penultimate (second-to-last) syllable in "
            "the great majority of words. \n\n"
            "The vowels. a is always the father-a (pagi = morning). i is "
            "the machine-i but shorter (ini = this). u is the moon-u "
            "(untuk = for). o is the go-o (orang = person). e is the one "
            "vowel with two faces: the bed-e in enak (delicious) and "
            "dengan (with), and the schwa uh in emas (gold) and beras "
            "(rice). \n\n"
            "The consonants to watch. c is always ch as in church "
            "(cinta = love) - never the soft s of English. g is always "
            "hard as in go (guru = teacher) - never the soft g of giant. "
            "j is j as in jump (jalan = road). r is trilled, rolled on the "
            "tongue (rumah = house). h is pronounced everywhere it is "
            "written (hati = heart), never silent. Final k is a stopped "
            "glottal catch, not released (anak = child). \n\n"
            "The digraphs in the mouth. ng is the sing sound and can start "
            "a syllable (nganga = to gape). ny is the canyon sound (nyanyi "
            "= to sing). sy is sh (syarat = condition). kh is the throaty "
            "loch sound (khas = special). \n\n"
            "Stress and rhythm. Stress the penultimate syllable: BAhasa, "
            "inDOnesia, maKAnan. Schwa e never takes stress, so the accent "
            "slides one syllable earlier in words like BAras (rice) and "
            "tUlis (write). Rhythm is syllable-timed - every syllable gets "
            "roughly equal time, unlike English. \n\n"
            "Ten spoken examples with English:\n"
            "  selamat (suh-LA-mat) - safe / greeting word\n"
            "  pagi (PA-gi) - morning\n"
            "  terima kasih (tuh-REE-ma KA-sih) - thank you\n"
            "  cinta (CHEEN-ta) - love\n"
            "  nyanyi (NYA-nyi) - to sing\n"
            "  bunga (BOO-nga) - flower\n"
            "  guru (GOO-roo) - teacher\n"
            "  enak (eh-NAK) - delicious\n"
            "  emas (uh-MAS) - gold\n"
            "  rumah (ROO-mah) - house\n"
            "  jalan (JA-lan) - road\n"
            "  makan (MA-kan) - to eat"
        ),
        "how_it_works": (
            "This record converts the alphabet into muscle memory. Each "
            "tricky sound is anchored to an English anchor word, and the "
            "penultimate-stress rule plus the schwa-never-stressed "
            "exception give a complete stress algorithm in two rules. The "
            "twelve spoken examples are chosen to exercise every digraph, "
            "both e sounds, the trilled r, and the stopped final k, so "
            "saying them aloud completes the whole sound inventory. No "
            "tones means English speakers can trust their intonation "
            "habits for statements and questions."
        ),
        "key_points": [
            "No tones; stress on the penultimate syllable.",
            "Spelling is nearly phonetic - read as written.",
            "c is always ch, g always hard, r trilled, final k stopped.",
            "e has two sounds: bed-e and schwa; schwa never takes stress.",
            "Rhythm is syllable-timed, unlike English.",
        ],
        "requirements": [
            "Master the writing-system record's digraphs first.",
            "Say every example word aloud; Indonesian is learned in the mouth.",
        ],
        "standards": [
            "Pronunciation described per standard baku Indonesian (Sneddon 2010).",
            "Colloquial Jakarta speech may soften some sounds; the record teaches the standard.",
        ],
        "citations": [CIT_SNEDDON_R, CIT_SNEDDON_G],
        "must_contain": ["penultimate", "no tones", "trilled", "schwa", "syllable-timed"],
        "sig_lens": (
            "Through the Signature lens every sound is a sealed vow: the "
            "trilled r a drum-roll of allegiance, the penultimate stress "
            "a drumbeat that never misses, and the schwa the quiet breath "
            "between the sworn syllables."
        ),
        "drill": {
            "vowel_count": 5, "two_face_vowel": "e",
            "tricky": ["c", "g", "j", "r", "h", "k-final"],
            "digraph_sounds": {"kh": "loch", "ng": "sing", "ny": "canyon",
                               "sy": "ship"},
            "stress_rule": "penultimate", "tones": 0,
            "examples": ["selamat", "pagi", "terima kasih", "cinta",
                         "nyanyi", "bunga", "guru", "enak", "emas",
                         "rumah", "jalan", "makan"],
        },
    },
    {
        "key": "nouns",
        "name": "Core Nouns I - 25 Essential Nouns",
        "group": "Core Vocabulary",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five nouns that carry daily life. Indonesian nouns "
            "never change for gender, case, or number - one form does all "
            "the work, and plurals come from reduplication (record 10). "
            "Each noun below comes with one full sentence, translated. \n\n"
            "  orang - person. Orang itu guru saya. - That person is my "
            "teacher.\n"
            "  anak - child. Anak saya suka membaca. - My child likes to "
            "read.\n"
            "  ibu - mother. Ibu memasak nasi. - Mother cooks rice.\n"
            "  ayah - father. Ayah bekerja di kantor. - Father works at the "
            "office.\n"
            "  rumah - house. Rumah kami besar. - Our house is big.\n"
            "  air - water. Air ini dingin. - This water is cold.\n"
            "  makanan - food. Makanan ini enak. - This food is delicious.\n"
            "  buku - book. Buku itu tebal. - That book is thick.\n"
            "  mobil - car. Mobil ayah berwarna merah. - Father's car is "
            "red.\n"
            "  sekolah - school. Sekolah dimulai jam tujuh. - School starts "
            "at seven o'clock.\n"
            "  pasar - market. Pasar buka setiap hari. - The market opens "
            "every day.\n"
            "  kota - city. Kota Jakarta sangat besar. - The city of "
            "Jakarta is very big.\n"
            "  negara - country. Indonesia adalah negara kepulauan. - "
            "Indonesia is an archipelago country.\n"
            "  hari - day. Hari ini hari Senin. - Today is Monday.\n"
            "  waktu - time. Waktu adalah uang. - Time is money.\n"
            "  tangan - hand. Tangan saya bersih. - My hands are clean.\n"
            "  mata - eye. Mata adik berwarna cokelat. - Little sibling's "
            "eyes are brown.\n"
            "  kepala - head. Kepala saya pusing. - My head is dizzy.\n"
            "  uang - money. Uang itu di dompet. - The money is in the "
            "wallet.\n"
            "  teman - friend. Teman saya baik hati. - My friend is kind.\n"
            "  jalan - road. Jalan ini panjang. - This road is long.\n"
            "  pintu - door. Pintu itu terbuka. - That door is open.\n"
            "  meja - table. Buku ada di meja. - The book is on the table.\n"
            "  kursi - chair. Kursi ini nyaman. - This chair is "
            "comfortable.\n"
            "  telepon - telephone. Telepon saya berdering. - My telephone "
            "is ringing."
        ),
        "how_it_works": (
            "Each noun is presented in its single invariant form with a "
            "sentence that places it in a real situation, so the learner "
            "absorbs word order and the noun-adjective pattern (rumah "
            "besar, big house) without a grammar lecture. Possession "
            "appears naturally in forms like anak saya (my child) and "
            "mobil ayah (father's car), pre-teaching the owner-after-noun "
            "rule of record 10. Every sentence is short enough to memorize "
            "whole."
        ),
        "key_points": [
            "25 essential nouns, each with a translated sentence.",
            "Indonesian nouns have one form: no gender, no case, no plural endings.",
            "Adjectives follow nouns: rumah besar (big house).",
            "Possession: owner after the noun (anak saya, mobil ayah).",
        ],
        "requirements": [
            "Know the alphabet sounds from the writing-system record.",
            "Say each sentence aloud; memorize at least ten whole.",
        ],
        "standards": [
            "Word glosses follow Echols & Shadily 1989.",
            "All sentences use standard baku word order.",
        ],
        "citations": [CIT_ECHOLS, CIT_SNEDDON_R],
        "must_contain": ["orang", "rumah", "makanan", "never change for gender", "reduplication"],
        "sig_lens": (
            "Through the Signature lens each noun is a sworn landmark: the "
            "house, the road, the market - twenty-five stones laid as the "
            "foundation course of the covenant vocabulary."
        ),
        "drill": {
            "nouns": ["orang", "anak", "ibu", "ayah", "rumah", "air",
                      "makanan", "buku", "mobil", "sekolah", "pasar",
                      "kota", "negara", "hari", "waktu", "tangan", "mata",
                      "kepala", "uang", "teman", "jalan", "pintu", "meja",
                      "kursi", "telepon"],
            "forms_per_noun": 1, "genders": 0, "cases": 0,
        },
    },
    {
        "key": "verbs",
        "name": "Core Verbs I - 25 Essential Verbs",
        "group": "Core Vocabulary",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five verbs that move daily life. Indonesian verbs never "
            "conjugate - makan is eat, eats, ate, and will eat depending on "
            "the time words around it. Most action verbs wear the me- "
            "prefix (membaca, menulis); the base form sits inside. Each "
            "verb below comes with one full sentence, translated. \n\n"
            "  makan - to eat. Saya makan nasi setiap hari. - I eat rice "
            "every day.\n"
            "  minum - to drink. Dia minum teh panas. - She drinks hot tea.\n"
            "  pergi - to go. Kami pergi ke pasar. - We go to the market.\n"
            "  datang - to come. Teman saya datang sore ini. - My friend "
            "comes this afternoon.\n"
            "  melihat - to see. Saya melihat burung di pohon. - I see a "
            "bird in the tree.\n"
            "  mendengar - to hear. Anak itu mendengar musik. - That child "
            "hears music.\n"
            "  berbicara - to speak. Ibu berbicara dengan guru. - Mother "
            "speaks with the teacher.\n"
            "  membaca - to read. Adik membaca buku cerita. - Little "
            "sibling reads a storybook.\n"
            "  menulis - to write. Saya menulis surat. - I write a letter.\n"
            "  belajar - to study. Mereka belajar Bahasa Indonesia. - They "
            "study Indonesian.\n"
            "  bekerja - to work. Ayah bekerja di bank. - Father works at "
            "a bank.\n"
            "  tidur - to sleep. Bayi itu tidur nyenyak. - The baby sleeps "
            "soundly.\n"
            "  bangun - to wake up. Saya bangun jam lima. - I wake up at "
            "five o'clock.\n"
            "  duduk - to sit. Silakan duduk. - Please sit down.\n"
            "  berdiri - to stand. Murid-murid berdiri. - The students "
            "stand up.\n"
            "  berjalan - to walk. Kami berjalan ke sekolah. - We walk to "
            "school.\n"
            "  berlari - to run. Anak-anak berlari di lapangan. - The "
            "children run in the field.\n"
            "  membeli - to buy. Ibu membeli sayur di pasar. - Mother buys "
            "vegetables at the market.\n"
            "  menjual - to sell. Dia menjual buah. - He sells fruit.\n"
            "  membuka - to open. Tolong buka pintu. - Please open the door.\n"
            "  menutup - to close. Dia menutup jendela. - She closes the "
            "window.\n"
            "  memberi - to give. Guru memberi PR. - The teacher gives "
            "homework.\n"
            "  mengambil - to take. Saya mengambil buku dari meja. - I "
            "take the book from the table.\n"
            "  tahu - to know. Saya tahu jawabannya. - I know the answer.\n"
            "  suka - to like. Saya suka kopi. - I like coffee."
        ),
        "how_it_works": (
            "The me- prefix is introduced as the engine of action verbs: "
            "strip it and the root appears (membaca -> baca, menulis -> "
            "tulis, membeli -> beli). Stative verbs like tahu and suka "
            "take no prefix, a pattern the learner meets here before the "
            "full affix system of record 10. Because verbs never "
            "conjugate, every sentence is a reusable template: swap the "
            "subject and the sentence still works."
        ),
        "key_points": [
            "25 essential verbs, each with a translated sentence.",
            "Verbs never conjugate; time words carry tense.",
            "The me- prefix marks most action verbs; the root hides inside.",
            "Stative verbs (tahu, suka) take no prefix.",
        ],
        "requirements": [
            "Know the noun record's basic word order.",
            "Practice stripping me- to find each verb root.",
        ],
        "standards": [
            "Verb forms follow standard baku affixation (Alwi et al. 2003).",
            "Colloquial speech may drop prefixes; the record teaches full forms.",
        ],
        "citations": [CIT_ALWI, CIT_SNEDDON_G],
        "must_contain": ["never conjugate", "me-", "membaca", "menulis", "tahu"],
        "sig_lens": (
            "Through the Signature lens each verb is a sworn deed: the "
            "prefix me- a seal pressed onto the root, turning a bare word "
            "into an action that moves through the sentence like a "
            "covenant kept."
        ),
        "drill": {
            "verbs": ["makan", "minum", "pergi", "datang", "melihat",
                      "mendengar", "berbicara", "membaca", "menulis",
                      "belajar", "bekerja", "tidur", "bangun", "duduk",
                      "berdiri", "berjalan", "berlari", "membeli",
                      "menjual", "membuka", "menutup", "memberi",
                      "mengambil", "tahu", "suka"],
            "conjugations": 0, "me_prefix_verbs": 10,
        },
    },
    {
        "key": "adjectives",
        "name": "Adjectives and Adverbs - 25 Plus 15",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five adjectives and fifteen adverbs. Adjectives follow "
            "the noun (rumah besar = big house) and never agree with "
            "anything - no gender, no number, no case endings. Adverbs "
            "usually sit before the adjective or verb they modify. Each "
            "word comes with a translated sentence. \n\n"
            "Adjectives:\n"
            "  besar - big. Rumah itu besar. - That house is big.\n"
            "  kecil - small. Kucing itu kecil. - That cat is small.\n"
            "  baik - good. Dia orang baik. - He is a good person.\n"
            "  buruk - bad. Cuaca hari ini buruk. - Today's weather is bad.\n"
            "  baru - new. Sepatu saya baru. - My shoes are new.\n"
            "  lama - old, long (time). Film itu lama. - That film is long.\n"
            "  cepat - fast. Mobil itu cepat. - That car is fast.\n"
            "  lambat - slow. Kura-kura berjalan lambat. - The turtle walks "
            "slowly.\n"
            "  panas - hot. Kopi ini panas. - This coffee is hot.\n"
            "  dingin - cold. Air itu dingin. - That water is cold.\n"
            "  mahal - expensive. Baju ini mahal. - This shirt is expensive.\n"
            "  murah - cheap. Buah di pasar murah. - Fruit at the market is "
            "cheap.\n"
            "  panjang - long. Rambutnya panjang. - Her hair is long.\n"
            "  pendek - short. Cerita ini pendek. - This story is short.\n"
            "  tinggi - tall, high. Gedung itu tinggi. - That building is "
            "tall.\n"
            "  rendah - low. Harga beras rendah. - Rice prices are low.\n"
            "  senang - happy. Saya senang bertemu Anda. - I am happy to "
            "meet you.\n"
            "  sedih - sad. Dia sedih karena hujan. - She is sad because "
            "of the rain.\n"
            "  mudah - easy. Soal ini mudah. - This problem is easy.\n"
            "  sulit - difficult. Ujian itu sulit. - That exam is "
            "difficult.\n"
            "  cantik - beautiful. Bunga itu cantik. - That flower is "
            "beautiful.\n"
            "  kuat - strong. Petinju itu kuat. - That boxer is strong.\n"
            "  pintar - smart. Anak itu pintar. - That child is smart.\n"
            "  bersih - clean. Kamar ini bersih. - This room is clean.\n"
            "  kotor - dirty. Sepatu saya kotor. - My shoes are dirty.\n\n"
            "Adverbs:\n"
            "  sangat - very. Dia sangat baik. - She is very kind.\n"
            "  terlalu - too. Kopi ini terlalu panas. - This coffee is too "
            "hot.\n"
            "  cukup - enough, quite. Uang saya cukup. - My money is "
            "enough.\n"
            "  hampir - almost. Saya hampir selesai. - I am almost done.\n"
            "  selalu - always. Dia selalu tepat waktu. - He is always on "
            "time.\n"
            "  kadang-kadang - sometimes. Kami kadang-kadang pergi ke "
            "pantai. - We sometimes go to the beach.\n"
            "  jarang - rarely. Saya jarang menonton TV. - I rarely watch "
            "TV.\n"
            "  tidak pernah - never. Dia tidak pernah terlambat. - She is "
            "never late.\n"
            "  sudah - already. Saya sudah makan. - I have already eaten.\n"
            "  belum - not yet. Dia belum datang. - He has not come yet.\n"
            "  sekarang - now. Saya sibuk sekarang. - I am busy now.\n"
            "  segera - soon. Dokter akan datang segera. - The doctor will "
            "come soon.\n"
            "  perlahan - slowly. Berjalanlah perlahan. - Walk slowly.\n"
            "  benar-benar - really. Film itu benar-benar bagus. - That "
            "film is really good.\n"
            "  mungkin - maybe. Mungkin dia sakit. - Maybe she is sick."
        ),
        "how_it_works": (
            "The noun-adjective order is drilled through every example: "
            "the adjective always trails its noun, the opposite of "
            "English, so the pattern becomes reflex. Degree is handled "
            "with the adverbs sangat (very), terlalu (too), and paling "
            "(most) rather than with word endings, which the examples "
            "demonstrate in place. Sudah and belum double as time adverbs, "
            "pre-teaching the tense system of record 21."
        ),
        "key_points": [
            "25 adjectives + 15 adverbs, each with a translated sentence.",
            "Adjectives follow nouns and never agree: rumah besar.",
            "Degree uses sangat, terlalu, paling - no comparative endings.",
            "Sudah (already) and belum (not yet) are adverbs that carry tense.",
        ],
        "requirements": [
            "Know the noun record's word order.",
            "Drill noun + adjective pairs until the order feels natural.",
        ],
        "standards": [
            "All forms are standard baku; colloquial banget (very) is noted but not taught as standard.",
        ],
        "citations": [CIT_SNEDDON_R, CIT_ECHOLS],
        "must_contain": ["follow the noun", "rumah besar", "sangat", "never agree", "belum"],
        "sig_lens": (
            "Through the Signature lens each adjective is a sworn quality "
            "stamped onto its noun: the word walks behind its master, "
            "never changing its shape, loyal to one form in every "
            "sentence."
        ),
        "drill": {
            "adjectives": 25, "adverbs": 15,
            "order": "noun-adjective", "agreement_forms": 0,
            "degree_words": ["sangat", "terlalu", "paling", "cukup"],
        },
    },
    {
        "key": "pronouns",
        "name": "Pronouns - Full Paradigms",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The complete pronoun system: personal, possessive, "
            "demonstrative, and interrogative. Indonesian pronouns never "
            "change for case - saya is I, me, and my depending on position. "
            "The two great choices are formality (saya vs aku) and the "
            "inclusive-exclusive we (kita vs kami). \n\n"
            "Personal pronouns:\n"
            "  saya - I (formal/polite). Saya pergi ke kantor. - I go to "
            "the office.\n"
            "  aku - I (informal, intimate). Aku sayang kamu. - I love you.\n"
            "  kamu - you (informal). Kamu sudah makan? - Have you eaten?\n"
            "  Anda - you (formal, respectful). Anda mau minum apa? - What "
            "would you like to drink?\n"
            "  dia - he/she (neutral). Dia guru saya. - She is my teacher.\n"
            "  ia - he/she (formal written). Ia menulis laporan. - He wrote "
            "the report.\n"
            "  beliau - he/she (highly respectful). Beliau presiden "
            "pertama. - He was the first president.\n"
            "  kami - we (exclusive: not you). Kami pergi tanpa kamu. - We "
            "go without you.\n"
            "  kita - we (inclusive: you too). Kita belajar bersama. - We "
            "learn together.\n"
            "  mereka - they. Mereka tinggal di Surabaya. - They live in "
            "Surabaya.\n\n"
            "Possessives - two styles. Full: buku saya (my book), rumah "
            "kamu (your house), mobil dia (his car). Suffixed (informal, "
            "attached): bukuku (my book), rumahmu (your house), mobilnya "
            "(his/her car). \n"
            "  Bukuku ada di meja. - My book is on the table.\n"
            "  Rumahmu besar sekali. - Your house is very big.\n"
            "  Mobilnya baru. - His car is new.\n\n"
            "Demonstratives:\n"
            "  ini - this. Buku ini mahal. - This book is expensive.\n"
            "  itu - that. Rumah itu jauh. - That house is far.\n"
            "  sini - here. Duduk sini. - Sit here.\n"
            "  situ - there (near you). Taruh situ. - Put it there.\n"
            "  sana - there (far). Dia tinggal di sana. - He lives over "
            "there.\n\n"
            "Interrogatives:\n"
            "  apa - what. Apa ini? - What is this?\n"
            "  siapa - who. Siapa nama kamu? - What is your name?\n"
            "  di mana - where. Di mana toilet? - Where is the toilet?\n"
            "  kapan - when. Kapan kamu datang? - When will you come?\n"
            "  mengapa / kenapa - why. Mengapa kamu sedih? - Why are you "
            "sad?\n"
            "  bagaimana - how. Bagaimana kabarmu? - How are you?\n"
            "  berapa - how much/many. Berapa harganya? - How much is it?\n"
            "  yang mana - which. Yang mana bukumu? - Which one is your "
            "book?"
        ),
        "how_it_works": (
            "The formality ladder saya/aku and kamu/Anda is taught as a "
            "social compass: formal upward and outward, informal inward "
            "and among friends. The kami/kita distinction is drilled with "
            "minimal pairs so the inclusive-exclusive line becomes "
            "automatic. Possessives are shown in both full and suffixed "
            "styles because real speech mixes them constantly. The eight "
            "interrogatives are the question engine for record 22."
        ),
        "key_points": [
            "10 personal pronouns; no case changes - position does the work.",
            "Saya/aku and kamu/Anda: formality is a social compass.",
            "Kami (exclusive we) vs kita (inclusive we) - English has no such line.",
            "Possessives: full (buku saya) or suffixed (bukuku, rumahmu, mobilnya).",
            "Demonstratives: ini/itu, sini/situ/sana - a three-way distance scale.",
            "8 interrogatives form the whole question engine.",
        ],
        "requirements": [
            "Know basic sentence order from the noun and verb records.",
            "Practice the kami/kita minimal pairs aloud.",
        ],
        "standards": [
            "Pronoun usage follows standard baku norms; beliau and Anda marked as respectful.",
        ],
        "citations": [CIT_SNEDDON_R, CIT_ALWI],
        "must_contain": ["kami", "kita", "beliau", "bukuku", "rumahmu", "mobilnya", "di mana"],
        "sig_lens": (
            "Through the Signature lens each pronoun is a sworn name of "
            "relationship: saya the seal of the self, kami and kita two "
            "different covenants of togetherness, and -ku, -mu, -nya "
            "small clasps that lock a thing to its owner."
        ),
        "drill": {
            "personal": ["saya", "aku", "kamu", "Anda", "dia", "ia",
                         "beliau", "kami", "kita", "mereka"],
            "possessive_suffixes": ["-ku", "-mu", "-nya"],
            "demonstratives": ["ini", "itu", "sini", "situ", "sana"],
            "interrogatives": ["apa", "siapa", "di mana", "kapan",
                               "mengapa", "bagaimana", "berapa",
                               "yang mana"],
            "case_forms": 1,
        },
    },
    {
        "key": "numbers",
        "name": "Numbers and Time - 1 to 100 and Beyond",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The complete number engine, the calendar, and clock time. "
            "Indonesian numbers are beautifully regular: learn 1-10 and "
            "the words for ten, hundred, thousand, and million, and you "
            "can build any number. \n\n"
            "One to ten: satu, dua, tiga, empat, lima, enam, tujuh, "
            "delapan, sembilan, sepuluh. \n"
            "Eleven to nineteen add -belas: sebelas (11), dua belas (12), "
            "tiga belas (13), empat belas (14), lima belas (15), enam "
            "belas (16), tujuh belas (17), delapan belas (18), sembilan "
            "belas (19). \n"
            "Tens add puluh: dua puluh (20), tiga puluh (30), lima puluh "
            "lima (55), sembilan puluh sembilan (99). \n"
            "Hundreds, thousands, millions: seratus (100), dua ratus "
            "(200), seribu (1000), dua ribu (2000), satu juta (1,000,000), "
            "satu miliar (1,000,000,000). Note the special se- forms: "
            "sebelas, seratus, seribu - never satu belas. \n"
            "  Saya punya dua puluh lima buku. - I have twenty-five books.\n"
            "  Harganya seratus ribu rupiah. - The price is one hundred "
            "thousand rupiah.\n\n"
            "Ordinals add ke-: pertama (first), kedua (second), ketiga "
            "(third), kesepuluh (tenth), keseratus (hundredth). \n"
            "  Ini pertama kalinya saya ke Bali. - This is my first time "
            "in Bali.\n\n"
            "Days of the week: Senin (Monday), Selasa (Tuesday), Rabu "
            "(Wednesday), Kamis (Thursday), Jumat (Friday), Sabtu "
            "(Saturday), Minggu (Sunday). \n"
            "Months: Januari, Februari, Maret, April, Mei, Juni, Juli, "
            "Agustus, September, Oktober, November, Desember. \n"
            "  Hari ini hari Senin. - Today is Monday.\n"
            "  Ulang tahun saya bulan Mei. - My birthday is in May.\n\n"
            "Clock time: jam + number. jam tujuh (7 o'clock), jam setengah "
            "delapan (half past seven - literally half to eight), jam "
            "tujuh lewat lima belas (7:15), jam tujuh kurang lima (five "
            "to seven). \n"
            "Parts of day: pagi (morning), siang (midday), sore "
            "(afternoon), malam (night). \n"
            "  Sekarang jam delapan pagi. - It is now eight in the "
            "morning.\n"
            "  Kereta berangkat jam setengah enam sore. - The train leaves "
            "at half past five in the afternoon.\n\n"
            "Dates: tanggal + day + month + year. \n"
            "  Hari ini tanggal tujuh belas Oktober dua ribu dua puluh "
            "enam. - Today is 17 October 2026."
        ),
        "how_it_works": (
            "The number system is taught as a construction kit: ten roots "
            "plus the builders -belas, puluh, ratus, ribu, juta, miliar. "
            "The se- special forms (sebelas, seratus, seribu) are flagged "
            "as the only irregularity in the whole system. Clock time is "
            "taught through the half-to-the-next-hour logic (setengah "
            "delapan = 7:30), the one genuinely foreign concept for "
            "English speakers, drilled with examples until it clicks."
        ),
        "key_points": [
            "1-10 roots plus -belas, puluh, ratus, ribu, juta, miliar build every number.",
            "Only irregularity: se- forms - sebelas, seratus, seribu.",
            "Ordinals: ke- + number (pertama, kedua); pertama is the special first.",
            "Days Senin-Minggu; months mirror English names.",
            "Time: jam + number; setengah delapan means 7:30 (half to eight).",
        ],
        "requirements": [
            "Count 1-20 aloud until automatic.",
            "Practice the setengah logic with a clock face.",
        ],
        "standards": [
            "Number words follow EBI spelling; rupiah amounts in standard commercial form.",
        ],
        "citations": [CIT_SNEDDON_R, CIT_ECHOLS],
        "must_contain": ["sebelas", "seratus", "setengah", "pertama", "Senin"],
        "sig_lens": (
            "Through the Signature lens numbers are sworn measures: ten "
            "roots like ten commandments, each larger unit a seal upon "
            "the last, and the clock a covenant wheel turning the day "
            "into named hours."
        ),
        "drill": {
            "roots": ["satu", "dua", "tiga", "empat", "lima", "enam",
                      "tujuh", "delapan", "sembilan", "sepuluh"],
            "builders": ["belas", "puluh", "ratus", "ribu", "juta",
                         "miliar"],
            "specials": ["sebelas", "seratus", "seribu"],
            "days": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu",
                     "Minggu"],
            "months": 12, "dayparts": ["pagi", "siang", "sore", "malam"],
            "test_number": 2026, "test_reading": "dua ribu dua puluh enam",
        },
    },
    {
        "key": "greetings",
        "name": "Greetings and Everyday Phrases - 30 Phrases",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Thirty phrases for the whole social day, each with English "
            "and a usage note. Indonesian greetings track the sun - "
            "selamat follows the time of day - and politeness is built "
            "from small softeners. \n\n"
            "  Selamat pagi! - Good morning! (until ~10am)\n"
            "  Selamat siang! - Good midday! (~10am-3pm)\n"
            "  Selamat sore! - Good afternoon! (~3pm-6pm)\n"
            "  Selamat malam! - Good evening/night! (after ~6pm)\n"
            "  Halo! / Hai! - Hello! / Hi! (casual, any time)\n"
            "  Apa kabar? - How are you? (literally: what is the news?)\n"
            "  Kabar baik. - Good news / I'm fine. (the standard reply)\n"
            "  Terima kasih. - Thank you.\n"
            "  Terima kasih banyak. - Thank you very much.\n"
            "  Sama-sama. - You're welcome. (also: likewise)\n"
            "  Maaf. - Sorry. / Excuse me. (apology)\n"
            "  Permisi. - Excuse me. (getting attention, passing by)\n"
            "  Tolong. - Please / help. (request softener)\n"
            "  Silakan. - Please (do go ahead). (offering, inviting in)\n"
            "  Sampai jumpa. - See you. (general farewell)\n"
            "  Sampai nanti. - See you later.\n"
            "  Selamat jalan! - Have a safe trip! (said TO the one "
            "leaving)\n"
            "  Selamat tinggal! - Goodbye! (said BY the one leaving)\n"
            "  Selamat datang! - Welcome!\n"
            "  Senang bertemu dengan Anda. - Nice to meet you. (formal)\n"
            "  Sudah makan? - Have you eaten? (warm greeting showing "
            "care)\n"
            "  Mau ke mana? - Where are you off to? (friendly small "
            "talk)\n"
            "  Dari mana? - Where are you from? / Where have you been?\n"
            "  Hati-hati! - Be careful!\n"
            "  Selamat tidur! - Good night! (at bedtime)\n"
            "  Mimpi indah! - Sweet dreams!\n"
            "  Selamat ulang tahun! - Happy birthday!\n"
            "  Selamat! - Congratulations!\n"
            "  Ayo! - Let's go! / Come on!\n"
            "  Mari! - Let's. (formal invitation to act together)"
        ),
        "how_it_works": (
            "Greetings are organized by the day's arc - morning to night - "
            "so the selamat system teaches itself as a timeline. The "
            "jalan/tinggal pair is the classic learner trap (who says "
            "which), so it is drilled as a mirror: the stayer says jalan "
            "to the goer, the goer says tinggal to the stayer. Sudah "
            "makan? reveals the food-centered warmth of Indonesian "
            "sociability, a cultural key, not just a phrase."
        ),
        "key_points": [
            "30 greetings, farewells, and politeness phrases with usage notes.",
            "Selamat greetings follow the sun: pagi, siang, sore, malam.",
            "Selamat jalan (to the leaver) vs selamat tinggal (from the leaver).",
            "Maaf = apology; permisi = excuse me (attention/passing).",
            "Sudah makan? is care disguised as a question.",
        ],
        "requirements": [
            "Practice the four selamat greetings against the clock.",
            "Use each phrase aloud in a full mini-dialogue.",
        ],
        "standards": [
            "All phrases are standard usage nationwide; regional variants noted where common.",
        ],
        "citations": [CIT_ECHOLS, CIT_SNEDDON_R],
        "must_contain": ["Selamat pagi", "Apa kabar", "Sama-sama", "Selamat jalan", "Sudah makan"],
        "sig_lens": (
            "Through the Signature lens each greeting is a sworn courtesy: "
            "selamat a blessing sealed upon the hour, terima kasih a "
            "debt of gratitude spoken aloud, and sampai jumpa a promise "
            "that the covenant of meeting will renew."
        ),
        "drill": {
            "phrases": 30,
            "selamat_hours": {"pagi": "5-10", "siang": "10-15",
                              "sore": "15-18", "malam": "18-5"},
            "farewell_pair": ["selamat jalan", "selamat tinggal"],
            "politeness": ["maaf", "permisi", "tolong", "silakan"],
        },
    },
    {
        "key": "grammar",
        "name": "Grammar Essentials - Ten Load-Bearing Rules",
        "group": "Grammar Essentials",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Ten rules that hold up the whole language. Indonesian grammar "
            "is famously lean - no conjugations, no genders, no cases - "
            "and these ten rules are nearly all a learner needs. Each "
            "rule comes with translated examples. \n\n"
            "Rule 1 - Word order is SVO. Saya makan nasi. - I eat rice. "
            "Dia membaca buku. - She reads a book.\n\n"
            "Rule 2 - Verbs never conjugate; time words carry tense. Saya "
            "makan (I eat), saya sudah makan (I have eaten), saya sedang "
            "makan (I am eating), saya akan makan (I will eat).\n\n"
            "Rule 3 - Negation: tidak for verbs and adjectives, bukan for "
            "nouns, jangan for prohibitions. Saya tidak tahu (I don't "
            "know). Ini bukan buku saya (This is not my book). Jangan "
            "pergi! (Don't go!)\n\n"
            "Rule 4 - Questions by intonation, apakah, -kah, or question "
            "words. Kamu sudah makan? (Have you eaten?) Apakah kamu sudah "
            "makan? (formal). Benarkah itu? (Is that true?)\n\n"
            "Rule 5 - Adjectives follow nouns. rumah besar (big house), "
            "mobil merah (red car). No agreement, ever.\n\n"
            "Rule 6 - Plurals by reduplication. buku-buku (books), "
            "anak-anak (children). Context often makes it unnecessary: "
            "dua buku (two books) needs no reduplication.\n\n"
            "Rule 7 - Classifiers count things: seorang guru (a teacher), "
            "seekor kucing (a cat), sebuah rumah (a house), dua lembar "
            "kertas (two sheets of paper).\n\n"
            "Rule 8 - Affixes build words: me- makes verbs (membaca), ber- "
            "makes intransitives (berlari), di- makes passives (dibaca), "
            "ter- marks accident or superlative (terjatuh = fell "
            "accidentally, terbesar = biggest), pe- makes doers (penulis = "
            "writer), -kan and -i extend verbs, -an makes nouns (makanan = "
            "food).\n\n"
            "Rule 9 - Possession: owner after the noun. buku saya (my "
            "book), rumah ibu (mother's house), or suffixed: bukuku, "
            "rumahmu, bukunya.\n\n"
            "Rule 10 - Prepositions of place: di (at/in), ke (to), dari "
            "(from). Saya di rumah (I am at home). Dia pergi ke pasar (He "
            "goes to the market). Surat dari ibu (A letter from mother)."
        ),
        "how_it_works": (
            "The ten rules are ordered by load-bearing weight: word order "
            "and the no-conjugation principle first, because every later "
            "record assumes them. Each rule is stated in one line, then "
            "proved with two or three minimal sentences that differ by "
            "exactly one element, so the rule's effect is visible. The "
            "affix rule is a preview map for the deeper affix drills in "
            "record 21; the classifier rule previews record 18's market "
            "counting."
        ),
        "key_points": [
            "SVO order; verbs never conjugate.",
            "Time words (sudah, sedang, akan) carry tense.",
            "Tidak (verbs/adjectives), bukan (nouns), jangan (prohibitions).",
            "Adjectives follow nouns; no agreement.",
            "Plurals by reduplication; classifiers count (orang, ekor, buah).",
            "Core affixes: me-, ber-, di-, ter-, pe-, ke-, -kan, -i, -an.",
            "Possession: owner after noun; place: di, ke, dari.",
        ],
        "requirements": [
            "All vocabulary records 4-9 should feel familiar first.",
            "Build five original sentences per rule before moving on.",
        ],
        "standards": [
            "Rules describe standard baku Indonesian (Sneddon 2010; Alwi et al. 2003).",
        ],
        "citations": [CIT_SNEDDON_G, CIT_ALWI],
        "must_contain": ["SVO", "tidak", "bukan", "jangan", "reduplication", "seorang"],
        "sig_lens": (
            "Through the Signature lens these ten rules are the ten "
            "pillars of the covenant house: each one sworn and load-"
            "bearing, and the affixes the carved joints where roots lock "
            "into meaning."
        ),
        "drill": {
            "rules": 10, "word_order": "SVO", "conjugations": 0,
            "negators": ["tidak", "bukan", "jangan"],
            "classifiers": ["orang", "ekor", "buah", "lembar",
                            "batang", "helai"],
            "affixes": ["me-", "ber-", "di-", "ter-", "pe-", "ke-",
                        "-kan", "-i", "-an"],
            "place_preps": ["di", "ke", "dari"],
        },
    },
    {
        "key": "home",
        "name": "Home and Family - 20 Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the house and the people in it. Family "
            "words carry deep respect: bapak and ibu double as respectful "
            "address for any older man or woman. \n\n"
            "  Ini rumah saya. - This is my house.\n"
            "  Ruang tamu ada di depan. - The living room is at the front.\n"
            "  Dapur terletak di belakang. - The kitchen is at the back.\n"
            "  Kamar tidur saya di lantai dua. - My bedroom is on the "
            "second floor.\n"
            "  Kamar mandi ada di samping dapur. - The bathroom is next to "
            "the kitchen.\n"
            "  Meja dan kursi ada di ruang makan. - The table and chairs "
            "are in the dining room.\n"
            "  Ayah membaca koran di teras. - Father reads the newspaper "
            "on the terrace.\n"
            "  Ibu memasak di dapur. - Mother cooks in the kitchen.\n"
            "  Kakak saya bekerja di Jakarta. - My older sibling works in "
            "Jakarta.\n"
            "  Adik saya masih sekolah. - My younger sibling is still in "
            "school.\n"
            "  Kakek dan nenek tinggal di desa. - Grandfather and "
            "grandmother live in the village.\n"
            "  Paman saya datang berkunjung kemarin. - My uncle came to "
            "visit yesterday.\n"
            "  Bibi membuat kue yang enak. - Aunt makes delicious cakes.\n"
            "  Sepupu saya tinggal di Surabaya. - My cousin lives in "
            "Surabaya.\n"
            "  Kami makan malam bersama setiap hari. - We have dinner "
            "together every day.\n"
            "  Lampu ruang tamu sudah menyala. - The living room light is "
            "already on.\n"
            "  Jendela kamar saya menghadap ke taman. - My bedroom window "
            "faces the garden.\n"
            "  Halaman rumah kami luas. - Our house yard is spacious.\n"
            "  Kunci rumah ada di saku saya. - The house key is in my "
            "pocket.\n"
            "  Selamat datang di rumah kami! - Welcome to our home!"
        ),
        "how_it_works": (
            "Family vocabulary is taught with the address system built in: "
            "kakak/adik (older/younger sibling, gender-neutral), bapak/ibu "
            "(father/mother and respectful address), kakek/nenek, "
            "paman/bibi - so learners address people correctly from day "
            "one. House sentences use the di/ke/dari prepositions of "
            "record 10 in their natural habitat, and room names "
            "(ruang tamu, kamar tidur, kamar mandi, dapur) become a "
            "memory palace for the whole theme."
        ),
        "key_points": [
            "20 home-and-family sentences, every one translated.",
            "Kakak/adik are gender-neutral; bapak/ibu double as respectful address.",
            "Room vocabulary anchors prepositions of place.",
        ],
        "requirements": [
            "Know di/ke/dari from the grammar record.",
            "Label the rooms of your own home in Indonesian.",
        ],
        "standards": [
            "Kinship terms follow standard Indonesian usage nationwide.",
        ],
        "citations": [CIT_ECHOLS, CIT_SNEDDON_R],
        "must_contain": ["ruang tamu", "Kakak", "Adik", "Kakek", "dapur"],
        "sig_lens": (
            "Through the Signature lens the house is a sworn sanctuary "
            "and the family its sealed circle: each kinship word a vow of "
            "belonging, each room a chamber of the covenant kept daily."
        ),
        "drill": {
            "sentences": 20,
            "kinship": ["ayah", "ibu", "kakak", "adik", "kakek", "nenek",
                        "paman", "bibi", "sepupu"],
            "rooms": ["ruang tamu", "dapur", "kamar tidur", "kamar mandi",
                      "ruang makan", "teras", "halaman"],
        },
    },
    {
        "key": "food",
        "name": "Food and Cooking - 20 Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for meals, ingredients, cooking, and the "
            "restaurant. Indonesian food language is rich: nasi is cooked "
            "rice (and by extension, a meal), beras is uncooked rice, and "
            "padi is rice in the field. \n\n"
            "  Saya sarapan jam enam pagi. - I have breakfast at six in the "
            "morning.\n"
            "  Nasi goreng adalah makanan favorit saya. - Fried rice is my "
            "favorite food.\n"
            "  Ibu memasak rendang untuk makan malam. - Mother cooks "
            "rendang for dinner.\n"
            "  Ayam goreng ini sangat renyah. - This fried chicken is very "
            "crispy.\n"
            "  Tolong tambahkan garam sedikit. - Please add a little salt.\n"
            "  Sambal ini terlalu pedas untuk saya. - This chili sauce is "
            "too spicy for me.\n"
            "  Saya suka sate ayam dengan bumbu kacang. - I like chicken "
            "satay with peanut sauce.\n"
            "  Kita makan siang di warung dekat kantor. - We have lunch at "
            "the food stall near the office.\n"
            "  Pelayan, minta menu tolong. - Waiter, the menu please.\n"
            "  Saya pesan gado-gado dan es teh. - I'll order gado-gado and "
            "iced tea.\n"
            "  Berapa harga satu porsi bakso? - How much is one bowl of "
            "meatball soup?\n"
            "  Makanannya sudah datang. - The food has arrived.\n"
            "  Rasanya enak sekali! - It tastes so delicious!\n"
            "  Saya sudah kenyang, terima kasih. - I'm full, thank you.\n"
            "  Cuci tangan sebelum makan. - Wash your hands before eating.\n"
            "  Potong bawang dan cabai kecil-kecil. - Chop the shallots and "
            "chilies finely.\n"
            "  Rebus air sampai mendidih. - Boil the water until it boils.\n"
            "  Goreng tempe sampai kecokelatan. - Fry the tempeh until "
            "golden brown.\n"
            "  Buah mangga ini manis dan segar. - This mango is sweet and "
            "fresh.\n"
            "  Selamat menikmati hidangan Anda! - Enjoy your meal!"
        ),
        "how_it_works": (
            "The rice trilogy (padi/beras/nasi) opens the record because "
            "it is the single most useful cultural key in Indonesian "
            "food language. Cooking verbs (memasak, menggoreng, merebus, "
            "memotong) demonstrate the me- prefix on kitchen roots, "
            "reinforcing record 5. Restaurant sentences form a complete "
            "ordering script - menu, order, price, arrival, compliment - "
            "that works verbatim in any warung or restaurant."
        ),
        "key_points": [
            "20 food-and-cooking sentences, every one translated.",
            "Padi (field), beras (raw), nasi (cooked) - the rice trilogy.",
            "Warung = small food stall; the heart of everyday eating.",
            "Complete restaurant script from menu to compliment.",
        ],
        "requirements": [
            "Know me- verbs from the verb record.",
            "Cook one Indonesian dish following an Indonesian-language recipe.",
        ],
        "standards": [
            "Dish names (rendang, sate, gado-gado, bakso) are standard national dishes.",
        ],
        "citations": [CIT_ECHOLS, CIT_SNEDDON_R],
        "must_contain": ["nasi", "beras", "warung", "Sambal", "rendang"],
        "sig_lens": (
            "Through the Signature lens the meal is a sworn communion: "
            "rice the seal of sustenance, the shared table a covenant "
            "renewed three times daily, and selamat menikmati the "
            "blessing that opens it."
        ),
        "drill": {
            "sentences": 20,
            "rice_words": ["padi", "beras", "nasi"],
            "dishes": ["nasi goreng", "rendang", "sate ayam", "gado-gado",
                       "bakso", "ayam goreng"],
            "cooking_verbs": ["memasak", "menggoreng", "merebus",
                              "memotong", "mencuci"],
        },
    },
    {
        "key": "travel",
        "name": "Travel and Directions - 20 Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for transport, asking directions, tickets, "
            "and lodging. Direction words pair with di/ke/dari, and "
            "polite questions open every request. \n\n"
            "  Permisi, di mana stasiun kereta? - Excuse me, where is the "
            "train station?\n"
            "  Stasiun ada di sebelah kanan jalan ini. - The station is on "
            "the right side of this road.\n"
            "  Belok kiri di lampu merah. - Turn left at the traffic "
            "light.\n"
            "  Lurus terus sampai pertigaan. - Go straight until the "
            "T-junction.\n"
            "  Apakah jauh dari sini? - Is it far from here?\n"
            "  Berapa lama perjalanan ke bandara? - How long is the trip "
            "to the airport?\n"
            "  Saya mau beli tiket ke Yogyakarta. - I want to buy a ticket "
            "to Yogyakarta.\n"
            "  Kereta berangkat jam delapan pagi. - The train departs at "
            "eight in the morning.\n"
            "  Berapa harga tiket pulang-pergi? - How much is a round-trip "
            "ticket?\n"
            "  Bis ini berhenti di terminal. - This bus stops at the "
            "terminal.\n"
            "  Tolong antar saya ke hotel ini. - Please take me to this "
            "hotel.\n"
            "  Berapa ongkos ke Malioboro? - What is the fare to "
            "Malioboro?\n"
            "  Kamar untuk dua malam, tolong. - A room for two nights, "
            "please.\n"
            "  Apakah ada kamar kosong? - Is there a vacant room?\n"
            "  Kamar mandi ada di dalam, kan? - The bathroom is inside, "
            "right?\n"
            "  Jam berapa check-out? - What time is check-out?\n"
            "  Saya tersesat, bisa bantu? - I'm lost, can you help?\n"
            "  Di mana saya bisa naik ojek? - Where can I catch a "
            "motorcycle taxi?\n"
            "  Peta ini sangat membantu. - This map is very helpful.\n"
            "  Selamat jalan, sampai jumpa lagi! - Have a safe trip, see "
            "you again!"
        ),
        "how_it_works": (
            "Direction sentences are built on the kanan/kiri/lurus/dekat/"
            "jauh compass plus di/ke/dari, so every direction is a small "
            "grammar drill in disguise. The ticket and hotel sentences "
            "form two more complete real-world scripts. Ojek (motorcycle "
            "taxi) and terminal anchor the record in how Indonesia actually "
            "moves, and the tersesat (lost) sentence is the emergency key "
            "every traveler memorizes first."
        ),
        "key_points": [
            "20 travel sentences, every one translated.",
            "Direction compass: kanan, kiri, lurus, dekat, jauh.",
            "Complete scripts for tickets, taxis, and hotel check-in.",
            "Ojek and terminal: how Indonesia actually moves.",
        ],
        "requirements": [
            "Know di/ke/dari and question words from earlier records.",
            "Draw a map and give directions across it in Indonesian.",
        ],
        "standards": [
            "Transport terms are standard nationwide usage.",
        ],
        "citations": [CIT_ECHOLS, CIT_SNEDDON_R],
        "must_contain": ["ojek", "terminal", "Belok kiri", "pulang-pergi", "tersesat"],
        "sig_lens": (
            "Through the Signature lens the road is a sworn path: every "
            "direction a vow of guidance, every ticket a sealed passage, "
            "and selamat jalan the blessing that sends the traveler "
            "forth."
        ),
        "drill": {
            "sentences": 20,
            "compass": ["kanan", "kiri", "lurus", "depan", "belakang",
                        "dekat", "jauh"],
            "transport": ["kereta", "bis", "ojek", "taksi", "kapal",
                          "pesawat"],
            "scripts": ["directions", "ticket", "hotel"],
        },
    },
    {
        "key": "work",
        "name": "Work and School - 20 Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for jobs, the office, the classroom, and "
            "learning. Work words show the pe- doer prefix (pekerja = "
            "worker) in its natural home. \n\n"
            "  Saya bekerja sebagai guru. - I work as a teacher.\n"
            "  Kantor saya buka jam delapan. - My office opens at eight "
            "o'clock.\n"
            "  Rapat dimulai jam sembilan pagi. - The meeting starts at "
            "nine in the morning.\n"
            "  Tolong kirim email ini segera. - Please send this email "
            "right away.\n"
            "  Bos saya sedang rapat dengan klien. - My boss is in a "
            "meeting with a client.\n"
            "  Gaji dibayar setiap akhir bulan. - Salary is paid every end "
            "of the month.\n"
            "  Saya lembur sampai jam tujuh malam. - I work overtime until "
            "seven at night.\n"
            "  Rekan kerja saya sangat membantu. - My coworker is very "
            "helpful.\n"
            "  Anak-anak belajar matematika di sekolah. - The children "
            "study mathematics at school.\n"
            "  Guru menjelaskan pelajaran dengan jelas. - The teacher "
            "explains the lesson clearly.\n"
            "  Murid-murid mengerjakan PR di kelas. - The students do "
            "homework in class.\n"
            "  Ujian akan diadakan minggu depan. - The exam will be held "
            "next week.\n"
            "  Nilai saya bagus semester ini. - My grades are good this "
            "semester.\n"
            "  Perpustakaan buka sampai jam sembilan. - The library is open "
            "until nine o'clock.\n"
            "  Saya pinjam tiga buku dari perpustakaan. - I borrow three "
            "books from the library.\n"
            "  Pelajaran Bahasa Indonesia sangat menarik. - The Indonesian "
            "lesson is very interesting.\n"
            "  Jangan menyontek saat ujian! - Don't cheat during the exam!\n"
            "  Wisuda akan diadakan bulan Juni. - Graduation will be held "
            "in June.\n"
            "  Saya ingin menjadi dokter. - I want to become a doctor.\n"
            "  Semoga sukses dalam pekerjaan Anda! - Good luck in your "
            "work!"
        ),
        "how_it_works": (
            "Office sentences demonstrate passive di- in real "
            "administrative language (dibayar, diadakan), pre-teaching "
            "record 21's passive. School sentences reuse the ber- and "
            "me- verbs of record 5 (belajar, mengerjakan, menjelaskan) "
            "in academic contexts. The pe- doer nouns (pekerja, pelajar "
            "would-be) appear naturally, and jangan gives the "
            "prohibition pattern of record 23 an early foothold."
        ),
        "key_points": [
            "20 work-and-school sentences, every one translated.",
            "Passive di- appears in office language: dibayar, diadakan.",
            "Jangan + verb is the prohibition pattern.",
        ],
        "requirements": [
            "Know me-/ber-/di- prefixes from the grammar record.",
            "Describe your own job or school day in ten sentences.",
        ],
        "standards": [
            "Workplace and academic terms are standard baku Indonesian.",
        ],
        "citations": [CIT_SNEDDON_G, CIT_ECHOLS],
        "must_contain": ["pekerja", "rapat", "ujian", "perpustakaan", "lembur"],
        "sig_lens": (
            "Through the Signature lens work is a sworn craft and school "
            "a sealed apprenticeship: every lesson a vow taken, every "
            "deadline a covenant honored, every graduation a seal "
            "bestowed."
        ),
        "drill": {
            "sentences": 20,
            "workplaces": ["kantor", "sekolah", "perpustakaan", "bank",
                           "rumah sakit"],
            "passives": ["dibayar", "diadakan"],
            "doer_prefix": "pe-",
        },
    },
    {
        "key": "health",
        "name": "Health and Body - 20 Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for body parts, symptoms, the doctor visit, "
            "and the pharmacy. This is the record to memorize whole - it "
            "is the one you hope never to need. \n\n"
            "  Kepala saya sakit. - My head hurts.\n"
            "  Perut saya mual sejak pagi. - My stomach has been nauseous "
            "since morning.\n"
            "  Saya demam dan batuk. - I have a fever and a cough.\n"
            "  Tenggorokan saya sakit saat menelan. - My throat hurts when "
            "I swallow.\n"
            "  Kaki saya terkilir kemarin. - My foot got sprained "
            "yesterday.\n"
            "  Tangan saya terluka karena pisau. - My hand is cut from a "
            "knife.\n"
            "  Saya alergi terhadap kacang. - I am allergic to peanuts.\n"
            "  Tekanan darah saya tinggi. - My blood pressure is high.\n"
            "  Saya perlu ke dokter. - I need to see a doctor.\n"
            "  Di mana rumah sakit terdekat? - Where is the nearest "
            "hospital?\n"
            "  Tolong panggil ambulans! - Please call an ambulance!\n"
            "  Sudah berapa lama sakitnya? - How long have you been sick?\n"
            "  Minum obat ini tiga kali sehari. - Take this medicine three "
            "times a day.\n"
            "  Obat ini diminum sesudah makan. - This medicine is taken "
            "after meals.\n"
            "  Apakah ada efek samping? - Are there side effects?\n"
            "  Saya butuh istirahat yang cukup. - I need enough rest.\n"
            "  Luka harus dibersihkan setiap hari. - The wound must be "
            "cleaned every day.\n"
            "  Jantung berdebar kencang. - The heart is pounding fast.\n"
            "  Saya merasa lebih baik sekarang. - I feel better now.\n"
            "  Semoga lekas sembuh! - Get well soon!"
        ),
        "how_it_works": (
            "Body-part sentences use the X saya sakit frame, the fastest "
            "pain-reporting template in the language: swap any body part "
            "into the X slot. Doctor-visit sentences are a complete "
            "consultation script - symptom, duration question, "
            "prescription, dosage, side effects - in the polite formal "
            "register (Anda implied). Ter- accident forms (terkilir, "
            "terluka) show the accidental prefix of record 10 in urgent "
            "real use."
        ),
        "key_points": [
            "20 health sentences, every one translated - memorize whole.",
            "The X saya sakit frame reports any pain instantly.",
            "Complete doctor-visit and pharmacy scripts.",
            "Ter- marks accidents: terkilir, terluka.",
        ],
        "requirements": [
            "Memorize the emergency sentences first: doctor, hospital, ambulance.",
            "Practice the consultation script as a dialogue.",
        ],
        "standards": [
            "Medical terms are standard Indonesian; this record is language study, not medical advice.",
        ],
        "citations": [CIT_ECHOLS, CIT_SNEDDON_R],
        "must_contain": ["rumah sakit", "ambulans", "terkilir", "efek samping", "lekas sembuh"],
        "sig_lens": (
            "Through the Signature lens the body is a sworn vessel: every "
            "ache a signal honored, every remedy a covenant of care, and "
            "lekas sembuh the spoken seal of healing wished upon another."
        ),
        "drill": {
            "sentences": 20,
            "body_parts": ["kepala", "perut", "tenggorokan", "kaki",
                           "tangan", "jantung", "mata"],
            "symptoms": ["sakit", "demam", "batuk", "mual", "alergi"],
            "emergency": ["dokter", "rumah sakit", "ambulans", "apotek"],
        },
    },
    {
        "key": "emotions",
        "name": "Emotions and Feelings - 20 Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the inner life: happy, sad, angry, "
            "afraid, love, surprise. Indonesian feelings often live in "
            "the hati (heart/liver) - senang hati, sakit hati. \n\n"
            "  Saya sangat bahagia hari ini. - I am very happy today.\n"
            "  Hati saya senang mendengar kabar itu. - My heart is glad to "
            "hear that news.\n"
            "  Dia tertawa terbahak-bahak. - He laughed out loud.\n"
            "  Saya sedih karena dia pergi. - I am sad because he left.\n"
            "  Air matanya menetes. - Her tears fell.\n"
            "  Hati saya hancur mendengarnya. - My heart broke hearing it.\n"
            "  Dia marah besar kepada adiknya. - He is furious at his "
            "younger sibling.\n"
            "  Jangan marah, sabar dulu. - Don't be angry, be patient "
            "first.\n"
            "  Saya takut gelap. - I am afraid of the dark.\n"
            "  Anak itu ketakutan saat petir. - That child was frightened "
            "during the thunder.\n"
            "  Aku cinta kamu. - I love you.\n"
            "  Mereka saling menyayangi. - They love each other.\n"
            "  Saya kaget mendengar teriakan itu. - I was startled hearing "
            "that scream.\n"
            "  Betapa terkejutnya saya! - How surprised I was!\n"
            "  Saya bangga padamu. - I am proud of you.\n"
            "  Dia malu berbicara di depan umum. - She is shy speaking in "
            "public.\n"
            "  Saya cemas menunggu hasilnya. - I am anxious waiting for "
            "the result.\n"
            "  Tenanglah, semuanya akan baik-baik saja. - Calm down, "
            "everything will be fine.\n"
            "  Perasaan saya campur aduk. - My feelings are mixed.\n"
            "  Terima kasih atas perhatian Anda. - Thank you for your "
            "kindness."
        ),
        "how_it_works": (
            "The hati (heart) idiom field is the emotional core of the "
            "record: Indonesian maps feeling onto the heart the way "
            "English maps it onto the heart too, but with its own "
            "compounds (sakit hati = heartache, literally sick liver). "
            "Reciprocal saling- (saling menyayangi) and the ter- "
            "accidental-involuntary forms (terkejut, ketakutan) extend "
            "the affix map. The -lah softener in tenanglah and jangan "
            "marah preview the command record's politeness system."
        ),
        "key_points": [
            "20 emotion sentences, every one translated.",
            "Feelings live in the hati: senang hati, sakit hati.",
            "Saling- marks reciprocity: saling menyayangi.",
            "Ter- marks involuntary feeling: terkejut, ketakutan.",
        ],
        "requirements": [
            "Know ter- and -lah from the grammar record.",
            "Keep an Indonesian feelings journal for one week.",
        ],
        "standards": [
            "Emotion vocabulary is standard; hati compounds are everyday idiom.",
        ],
        "citations": [CIT_ECHOLS, CIT_SNEDDON_R],
        "must_contain": ["hati", "saling", "terkejut", "Aku cinta kamu", "sabar"],
        "sig_lens": (
            "Through the Signature lens every feeling is a sworn weather "
            "of the heart: joy a bright seal, grief a heavy one, and "
            "love the deepest covenant the language can speak."
        ),
        "drill": {
            "sentences": 20,
            "emotions": ["bahagia", "senang", "sedih", "marah", "takut",
                         "cinta", "kaget", "bangga", "malu", "cemas",
                         "tenang"],
            "hati_compounds": ["senang hati", "sakit hati"],
            "reciprocal": "saling-",
        },
    },
    {
        "key": "nature",
        "name": "Nature and Weather - 20 Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for animals, plants, and the tropical sky. "
            "Indonesia has two seasons - musim hujan (rainy) and musim "
            "kemarau (dry) - and weather talk runs on them. \n\n"
            "  Hari ini cuaca cerah. - Today the weather is clear.\n"
            "  Langit mendung, mungkin akan hujan. - The sky is cloudy, it "
            "might rain.\n"
            "  Hujan turun dengan deras. - The rain falls heavily.\n"
            "  Musim hujan tiba bulan November. - The rainy season arrives "
            "in November.\n"
            "  Kemarau tahun ini sangat panjang. - This year's dry season "
            "is very long.\n"
            "  Pelangi muncul setelah hujan. - A rainbow appears after the "
            "rain.\n"
            "  Matahari terbit jam enam pagi. - The sun rises at six in "
            "the morning.\n"
            "  Angin bertiup kencang malam ini. - The wind blows hard "
            "tonight.\n"
            "  Kucing itu tidur di bawah pohon. - That cat sleeps under "
            "the tree.\n"
            "  Anjing menggonggong pada tamu. - The dog barks at the "
            "guest.\n"
            "  Burung berkicau di pagi hari. - Birds chirp in the morning.\n"
            "  Gajah adalah hewan terbesar di kebun binatang. - The "
            "elephant is the biggest animal at the zoo.\n"
            "  Harimau Sumatra hampir punah. - The Sumatran tiger is "
            "nearly extinct.\n"
            "  Orangutan hidup di hutan Kalimantan. - Orangutans live in "
            "the forests of Kalimantan.\n"
            "  Pohon kelapa tumbuh di tepi pantai. - Coconut trees grow at "
            "the beach's edge.\n"
            "  Bunga mawar mekar di taman. - Roses bloom in the garden.\n"
            "  Sawah menghijau setelah hujan. - The rice fields turn green "
            "after rain.\n"
            "  Gunung itu tertutup kabut. - That mountain is covered in "
            "mist.\n"
            "  Laut tenang pagi ini. - The sea is calm this morning.\n"
            "  Alam Indonesia sangat indah. - Indonesia's nature is very "
            "beautiful."
        ),
        "how_it_works": (
            "The two-season system (musim hujan / musim kemarau) replaces "
            "the four-season vocabulary English speakers expect - the "
            "record teaches the tropical frame directly. Animal sentences "
            "show ber- verbs of characteristic behavior (berkicau, "
            "menggonggong as me- form), and the ter- stative forms "
            "(tertutup, terbit) extend the accidental-result pattern. "
            "Endemic animals (harimau Sumatra, orangutan) root the "
            "vocabulary in the real archipelago."
        ),
        "key_points": [
            "20 nature-and-weather sentences, every one translated.",
            "Two seasons: musim hujan (rainy) and musim kemarau (dry).",
            "Ter- marks results: tertutup (covered), terbit (risen).",
            "Endemic wildlife anchors the vocabulary: orangutan, harimau Sumatra.",
        ],
        "requirements": [
            "Know ter- from the grammar record.",
            "Describe today's weather in five Indonesian sentences.",
        ],
        "standards": [
            "Season and wildlife terms are standard; conservation status stated generally.",
        ],
        "citations": [CIT_ECHOLS, CIT_SNEDDON_R],
        "must_contain": ["musim hujan", "musim kemarau", "Orangutan", "Pelangi", "Sawah"],
        "sig_lens": (
            "Through the Signature lens nature is the great sworn temple: "
            "the rain a covenant renewed each season, each endemic "
            "creature a living seal found nowhere else on earth."
        ),
        "drill": {
            "sentences": 20,
            "seasons": ["musim hujan", "musim kemarau"],
            "animals": ["kucing", "anjing", "burung", "gajah",
                        "harimau Sumatra", "orangutan"],
            "plants": ["pohon kelapa", "bunga mawar", "sawah"],
        },
    },
    {
        "key": "shopping",
        "name": "Shopping and Money - 20 Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the market, prices, bargaining, and "
            "paying. Bargaining (tawar-menawar) is expected in traditional "
            "markets - these sentences are the whole negotiation. \n\n"
            "  Berapa harga mangga ini? - How much are these mangoes?\n"
            "  Harganya dua puluh ribu per kilo. - The price is twenty "
            "thousand per kilo.\n"
            "  Mahal sekali! Bisa kurang? - So expensive! Can it be less?\n"
            "  Saya tawar lima belas ribu. - I bid fifteen thousand.\n"
            "  Tidak bisa, Bu. Sudah harga pas. - It can't, Ma'am. That's "
            "already the fixed price.\n"
            "  Ya sudah, saya beli dua kilo. - Alright, I'll buy two "
            "kilos.\n"
            "  Ada diskon untuk pembelian banyak? - Is there a discount "
            "for buying a lot?\n"
            "  Kembalinya lima ribu rupiah. - The change is five thousand "
            "rupiah.\n"
            "  Bisa bayar dengan kartu? - Can I pay by card?\n"
            "  Kami terima tunai dan transfer. - We accept cash and "
            "transfer.\n"
            "  Toko ini buka sampai jam sembilan malam. - This shop is "
            "open until nine at night.\n"
            "  Di mana kasir? - Where is the cashier?\n"
            "  Minta kantong plastik, tolong. - A plastic bag, please.\n"
            "  Baju ini ada ukuran yang lebih besar? - Does this shirt "
            "come in a bigger size?\n"
            "  Boleh dicoba dulu? - May I try it on first?\n"
            "  Warnanya cocok untuk Anda. - The color suits you.\n"
            "  Saya hanya lihat-lihat saja. - I'm just browsing.\n"
            "  Kuitansinya tolong. - The receipt, please.\n"
            "  Belanja di pasar tradisional lebih murah. - Shopping at the "
            "traditional market is cheaper.\n"
            "  Terima kasih sudah berbelanja! - Thank you for shopping!"
        ),
        "how_it_works": (
            "The bargaining sequence (harga -> mahal sekali -> tawar -> "
            "harga pas -> deal) is a complete negotiation script in five "
            "lines - the most economically useful paragraph in the "
            "database. Classifiers from record 10 do their market work "
            "here (per kilo, dua kilo). Harga pas (fixed price) vs "
            "negotiable price is the key cultural distinction, and the "
            "browsing sentence (hanya lihat-lihat) uses reduplication "
            "for casualness."
        ),
        "key_points": [
            "20 shopping sentences, every one translated.",
            "Complete bargaining script: ask, react, bid, fix, buy.",
            "Harga pas = fixed price; tawar-menawar = bargaining.",
            "Rupiah is the currency; ribu = thousand in prices.",
        ],
        "requirements": [
            "Know numbers and classifiers from records 8 and 10.",
            "Role-play a full market negotiation with a partner.",
        ],
        "standards": [
            "Market language is standard nationwide; prices are examples only.",
        ],
        "citations": [CIT_ECHOLS, CIT_SNEDDON_R],
        "must_contain": ["tawar", "harga pas", "rupiah", "Kembalinya", "lihat-lihat"],
        "sig_lens": (
            "Through the Signature lens the market is a sworn exchange: "
            "every price a proposal, every bid a counter-vow, and the "
            "handshake of deal a small covenant sealed in rupiah."
        ),
        "drill": {
            "sentences": 20,
            "bargain_script": ["Berapa harga", "Mahal sekali", "Saya tawar",
                               "harga pas", "saya beli"],
            "currency": "rupiah", "thousand": "ribu",
            "payment": ["tunai", "kartu", "transfer"],
        },
    },
    {
        "key": "friendship",
        "name": "Friendship and Social Life - 20 Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences for meeting people, invitations, and "
            "celebrations. Indonesian friendship runs on warmth and food - "
            "invitations are rarely refused lightly. \n\n"
            "  Senang berkenalan denganmu! - Nice to meet you!\n"
            "  Sudah lama tidak bertemu! - Long time no see!\n"
            "  Apa kabar keluargamu? - How is your family?\n"
            "  Mari mampir ke rumah saya. - Come visit my house.\n"
            "  Ayo makan bersama besok. - Let's eat together tomorrow.\n"
            "  Kamu diundang ke pesta ulang tahunku. - You're invited to "
            "my birthday party.\n"
            "  Pestanya mulai jam tujuh malam. - The party starts at seven "
            "at night.\n"
            "  Bawa apa ya ke sana? - What should I bring there?\n"
            "  Tidak usah bawa apa-apa. - No need to bring anything.\n"
            "  Kami bersahabat sejak kecil. - We've been close friends "
            "since childhood.\n"
            "  Dia teman baik saya. - He is my good friend.\n"
            "  Kita selalu saling membantu. - We always help each other.\n"
            "  Selamat atas kelulusanmu! - Congratulations on your "
            "graduation!\n"
            "  Selamat menempuh hidup baru! - Congratulations on the new "
            "life! (wedding wish)\n"
            "  Turut berduka cita. - My condolences.\n"
            "  Semoga cepat sembuh ya. - Hope you get well soon.\n"
            "  Jaga dirimu baik-baik. - Take good care of yourself.\n"
            "  Sampai ketemu lagi! - Until we meet again!\n"
            "  Persahabatan kita tak akan putus. - Our friendship will "
            "never break.\n"
            "  Terima kasih atas persahabatanmu. - Thank you for your "
            "friendship."
        ),
        "how_it_works": (
            "Social sentences are organized by the friendship arc - "
            "meeting, inviting, celebrating, comforting, parting - so "
            "each maps to a real social moment. The ber- reciprocal and "
            "saling- forms (bersahabat, saling membantu) show friendship "
            "as mutual action in the grammar itself. Ceremonial phrases "
            "(selamat menempuh hidup baru, turut berduka cita) are "
            "taught as fixed formulas, because getting them word-perfect "
            "matters socially."
        ),
        "key_points": [
            "20 friendship sentences, every one translated.",
            "Full social arc: meeting, inviting, celebrating, comforting, parting.",
            "Bersahabat and saling membantu: friendship as mutual grammar.",
            "Ceremonial phrases are fixed formulas - learn them word-perfect.",
        ],
        "requirements": [
            "Know saling- and ber- from earlier records.",
            "Write invitations to three different events.",
        ],
        "standards": [
            "Social formulas are standard nationwide usage.",
        ],
        "citations": [CIT_ECHOLS, CIT_SNEDDON_R],
        "must_contain": ["bersahabat", "saling membantu", "Turut berduka cita", "mampir", "diundang"],
        "sig_lens": (
            "Through the Signature lens friendship is a sworn alliance: "
            "every invitation a vow extended, every shared meal a seal "
            "renewed, and the promise tak akan putus the covenant's "
            "keeping."
        ),
        "drill": {
            "sentences": 20,
            "arc": ["meeting", "inviting", "celebrating", "comforting",
                    "parting"],
            "ceremonial": ["Selamat menempuh hidup baru",
                           "Turut berduka cita"],
            "mutual": ["bersahabat", "saling membantu"],
        },
    },
    {
        "key": "technology",
        "name": "Technology and Communication - 20 Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences for phones, the internet, computers, and "
            "messaging. Indonesian tech language freely borrows and "
            "Indonesianizes: mengunduh (to download), mengunggah (to "
            "upload), tetikus (mouse). \n\n"
            "  Ponsel saya kehabisan baterai. - My phone ran out of "
            "battery.\n"
            "  Tolong isi ulang pulsa saya. - Please top up my credit.\n"
            "  Sinyalnya lemah di sini. - The signal is weak here.\n"
            "  Saya kirim pesan lewat WhatsApp. - I send messages via "
            "WhatsApp.\n"
            "  Foto ini diunggah kemarin. - This photo was uploaded "
            "yesterday.\n"
            "  Unduh aplikasinya dulu. - Download the app first.\n"
            "  Kata sandi saya tidak berfungsi. - My password doesn't work.\n"
            "  Klik tautan di bawah ini. - Click the link below.\n"
            "  Komputer saya lemot sekali. - My computer is so slow.\n"
            "  Tetikusnya rusak, perlu diganti. - The mouse is broken, it "
            "needs replacing.\n"
            "  Simpan berkasnya di awan. - Save the file in the cloud.\n"
            "  Internet di kantor sangat cepat. - The internet at the "
            "office is very fast.\n"
            "  Saya sedang rapat daring. - I am in an online meeting.\n"
            "  Nyalakan kameranya, tolong. - Please turn on the camera.\n"
            "  Suaranya terputus-putus. - The audio keeps cutting out.\n"
            "  Kirim surelnya sebelum jam lima. - Send the email before "
            "five o'clock.\n"
            "  Balas pesannya segera ya. - Reply to the message soon, "
            "okay.\n"
            "  Nomor telepon saya kosong delapan satu dua... - My phone "
            "number is 0812...\n"
            "  Ikuti akun media sosial kami. - Follow our social media "
            "account.\n"
            "  Teknologi memudahkan hidup kita. - Technology makes our "
            "lives easier."
        ),
        "how_it_works": (
            "Tech vocabulary demonstrates Indonesian word-formation at "
            "full power: mengunduh and mengunggah are me- verbs built on "
            "Indonesian roots for download/upload, while surel (surat "
            "elektronik) is a native acronym for email. Passive di- "
            "appears in digital contexts (diunggah, diganti), and "
            "reduplication marks repetition (terputus-putus). Loanwords "
            "(internet, komputer, aplikasi) show the open borrowing "
            "habit; native coinages show the purist counter-current."
        ),
        "key_points": [
            "20 technology sentences, every one translated.",
            "Native coinages: mengunduh, mengunggah, tetikus, surel, daring.",
            "Open borrowing alongside purist coinage - both are standard.",
            "Passive di- and reduplication in digital contexts.",
        ],
        "requirements": [
            "Know me-/di- affixes and reduplication from earlier records.",
            "Change your phone's language to Indonesian for one day.",
        ],
        "standards": [
            "Terms follow standard Indonesian tech usage; brand names are incidental examples.",
        ],
        "citations": [CIT_ECHOLS, CIT_SNEDDON_R],
        "must_contain": ["mengunduh", "tetikus", "surel", "daring", "Kata sandi"],
        "sig_lens": (
            "Through the Signature lens technology is the covenant's new "
            "scriptorium: every upload a seal sent skyward, every password "
            "a secret vow, and the network the threads binding the "
            "archipelago's voices."
        ),
        "drill": {
            "sentences": 20,
            "native_coinages": ["mengunduh", "mengunggah", "tetikus",
                               "surel", "daring"],
            "loans": ["internet", "komputer", "aplikasi", "baterai"],
            "devices": ["ponsel", "komputer", "tetikus"],
        },
    },
    {
        "key": "tenses",
        "name": "Verb Tenses in Sentences - Past, Present, Future",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Indonesian has no tense endings: time words and aspect "
            "markers do the work. This record gives five or more "
            "translated sentences per tense, plus the passive and the "
            "key aspects. \n\n"
            "Present - habitual and general truth, no marker:\n"
            "  Saya makan nasi setiap hari. - I eat rice every day.\n"
            "  Dia bekerja di bank. - She works at a bank.\n"
            "  Matahari terbit dari timur. - The sun rises in the east.\n"
            "  Anak-anak suka bermain. - Children like to play.\n"
            "  Air mengalir ke bawah. - Water flows downward.\n\n"
            "Past - sudah / telah (already, completed):\n"
            "  Saya sudah makan. - I have eaten / I ate.\n"
            "  Dia telah pergi ke Surabaya. - He has gone to Surabaya.\n"
            "  Kami sudah menonton film itu. - We already watched that "
            "film.\n"
            "  Mereka sudah tiba kemarin. - They arrived yesterday.\n"
            "  Saya sudah belajar tiga jam. - I have studied for three "
            "hours.\n\n"
            "Progressive - sedang (in progress right now):\n"
            "  Saya sedang makan. - I am eating.\n"
            "  Dia sedang membaca buku. - She is reading a book.\n"
            "  Mereka sedang bermain bola. - They are playing ball.\n"
            "  Ibu sedang memasak di dapur. - Mother is cooking in the "
            "kitchen.\n"
            "  Kami sedang belajar Bahasa Indonesia. - We are learning "
            "Indonesian.\n\n"
            "Future - akan / mau (will, want-to):\n"
            "  Saya akan pergi besok. - I will go tomorrow.\n"
            "  Dia mau menjadi dokter. - He wants to become a doctor.\n"
            "  Kami akan membangun rumah baru. - We will build a new house.\n"
            "  Hujan akan turun sore ini. - It will rain this afternoon.\n"
            "  Mereka mau pindah ke Jakarta. - They want to move to "
            "Jakarta.\n\n"
            "Passive - di- (the action receives):\n"
            "  Buku itu dibaca anak saya. - That book is read by my child.\n"
            "  Surat sudah dikirim. - The letter has been sent.\n"
            "  Rumah itu dijual murah. - That house is sold cheaply.\n"
            "  Pintu ditutup jam sepuluh. - The door is closed at ten.\n"
            "  Nasi goreng dimasak ibu. - The fried rice is cooked by "
            "mother."
        ),
        "how_it_works": (
            "Each tense is a minimal frame: bare verb for present, sudah/"
            "telah for completed past, sedang for ongoing, akan/mau for "
            "future, di- for passive. The sentences are parallel by "
            "design - the same verbs recur across tenses (makan appears "
            "in present, past, progressive) so the marker's effect is "
            "isolated and visible. Mau doubles as want and near-future, "
            "a nuance the examples make plain."
        ),
        "key_points": [
            "No tense endings: markers do all the work.",
            "Present: bare verb. Past: sudah/telah. Progressive: sedang.",
            "Future: akan (neutral) / mau (want, near future).",
            "Passive: di- prefix; agent optional.",
            "Parallel verbs across tenses isolate each marker's effect.",
        ],
        "requirements": [
            "All vocabulary records should be comfortable first.",
            "Convert ten present sentences into past, progressive, and future.",
        ],
        "standards": [
            "Tense/aspect description follows Sneddon 2010.",
        ],
        "citations": [CIT_SNEDDON_G, CIT_ALWI],
        "must_contain": ["sudah", "sedang", "akan", "dibaca", "no tense endings"],
        "sig_lens": (
            "Through the Signature lens time is the covenant's ledger: "
            "sudah the seal of what is done, sedang the vow in progress, "
            "akan the promise sworn forward, and di- the mark that the "
            "deed was received."
        ),
        "drill": {
            "tenses": {"present": 5, "past": 5, "progressive": 5,
                       "future": 5, "passive": 5},
            "markers": {"present": None, "past": ["sudah", "telah"],
                        "progressive": ["sedang"],
                        "future": ["akan", "mau"], "passive": ["di-"]},
            "parallel_verb": "makan",
        },
    },
    {
        "key": "qa",
        "name": "Questions and Answers - 20 Pairs",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Twenty question-and-answer pairs covering who, what, where, "
            "when, why, and how. Questions rise in intonation; answers "
            "are complete sentences. \n\n"
            "  Siapa nama Anda? - Nama saya Budi. (What is your name? - "
            "My name is Budi.)\n"
            "  Apa ini? - Ini buku. (What is this? - This is a book.)\n"
            "  Di mana kamu tinggal? - Saya tinggal di Bandung. (Where do "
            "you live? - I live in Bandung.)\n"
            "  Kapan kereta berangkat? - Jam delapan pagi. (When does the "
            "train leave? - At eight in the morning.)\n"
            "  Mengapa kamu terlambat? - Karena macet. (Why are you late? "
            "- Because of traffic.)\n"
            "  Bagaimana cara ke pasar? - Belok kiri, lalu lurus. (How do "
            "I get to the market? - Turn left, then go straight.)\n"
            "  Berapa harganya? - Lima puluh ribu. (How much is it? - "
            "Fifty thousand.)\n"
            "  Yang mana milikmu? - Yang biru. (Which is yours? - The blue "
            "one.)\n"
            "  Apakah kamu sudah makan? - Sudah. (Have you eaten? - "
            "Already.)\n"
            "  Bisakah kamu membantu saya? - Tentu, dengan senang hati. "
            "(Can you help me? - Of course, gladly.)\n"
            "  Jam berapa sekarang? - Jam tiga sore. (What time is it? - "
            "Three in the afternoon.)\n"
            "  Dari mana asalmu? - Saya dari Medan. (Where are you from? "
            "- I'm from Medan.)\n"
            "  Mau ke mana? - Mau ke toko buku. (Where are you off to? - "
            "To the bookstore.)\n"
            "  Sudah berapa lama di sini? - Dua tahun. (How long have you "
            "been here? - Two years.)\n"
            "  Kenapa tidak datang kemarin? - Saya sakit. (Why didn't you "
            "come yesterday? - I was sick.)\n"
            "  Apa pekerjaanmu? - Saya guru. (What is your job? - I'm a "
            "teacher.)\n"
            "  Siapa yang menelepon? - Ibu saya. (Who called? - My "
            "mother.)\n"
            "  Bagaimana kabarmu? - Baik, terima kasih. (How are you? - "
            "Fine, thank you.)\n"
            "  Apa kamu suka kopi? - Suka sekali! (Do you like coffee? - "
            "Very much!)\n"
            "  Ke mana kita pergi besok? - Ke pantai! (Where are we going "
            "tomorrow? - To the beach!)"
        ),
        "how_it_works": (
            "Each pair is a complete conversational turn: the question "
            "models the interrogative word in place, the answer models a "
            "full-sentence reply (not just the fragment), so learners "
            "absorb both asking and answering. The eight interrogatives "
            "of record 7 all appear, plus the yes-no apakah and the "
            "ability bisakah. Short answers (Sudah., Tentu.) show the "
            "natural ellipsis of real speech."
        ),
        "key_points": [
            "20 Q&A pairs; every question word from record 7 in action.",
            "Answers are full sentences - learn to answer, not just ask.",
            "Apakah for yes-no; bisakah for ability/permission.",
            "Natural short answers: Sudah., Tentu.",
        ],
        "requirements": [
            "Master the eight interrogatives of the pronoun record.",
            "Practice each pair as a spoken dialogue.",
        ],
        "standards": [
            "All pairs are standard conversational Indonesian.",
        ],
        "citations": [CIT_SNEDDON_R, CIT_ECHOLS],
        "must_contain": ["Siapa", "Mengapa", "Bisakah", "Berapa harganya", "Sudah."],
        "sig_lens": (
            "Through the Signature lens every question is a sworn "
            "inquiry and every answer a testimony: the interrogatives "
            "the keys that unlock, the full-sentence replies the seals "
            "that confirm."
        ),
        "drill": {
            "pairs": 20,
            "question_words": ["siapa", "apa", "di mana", "kapan",
                               "mengapa", "bagaimana", "berapa",
                               "yang mana"],
            "yes_no": ["apakah", "bisakah"],
            "full_sentence_answers": True,
        },
    },
    {
        "key": "commands",
        "name": "Commands and Requests - 20 Sentences",
        "group": "Grammar in Action",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty imperatives and polite requests, formal and informal. "
            "Indonesian softens commands with -lah, tolong, and silakan; "
            "bare imperatives are for urgency or intimacy only. \n\n"
            "Polite requests (formal - to strangers, elders, officials):\n"
            "  Tolong buka pintunya. - Please open the door.\n"
            "  Silakan duduk, Pak. - Please sit down, Sir.\n"
            "  Mohon tunggu sebentar. - Please wait a moment.\n"
            "  Tolong kirimkan berkasnya besok. - Please send the file "
            "tomorrow.\n"
            "  Silakan masuk. - Please come in.\n\n"
            "Everyday commands (neutral - friends, family, colleagues):\n"
            "  Duduklah. - Sit down. (-lah softens)\n"
            "  Makanlah dulu. - Eat first.\n"
            "  Tutup pintunya. - Close the door.\n"
            "  Buka jendelanya. - Open the window.\n"
            "  Cepatlah sedikit! - Hurry up a bit!\n"
            "  Lihat ini! - Look at this!\n"
            "  Dengarkan saya! - Listen to me!\n"
            "  Coba lagi! - Try again!\n"
            "  Ayo pergi! - Let's go!\n"
            "  Berhenti! - Stop!\n\n"
            "Prohibitions (jangan = don't):\n"
            "  Jangan pergi! - Don't go!\n"
            "  Jangan berisik! - Don't be noisy!\n"
            "  Jangan lupa bawa payung. - Don't forget to bring an "
            "umbrella.\n"
            "  Jangan khawatir. - Don't worry.\n"
            "  Dilarang merokok. - No smoking. (formal sign)"
        ),
        "how_it_works": (
            "The three politeness tiers are taught as separate toolkits: "
            "tolong/silakan/mohon for formal requests, -lah and bare "
            "verbs for everyday commands, jangan for prohibitions, and "
            "dilarang for official bans. The -lah suffix is the key "
            "discovery - the same verb with and without it shifts from "
            "order to invitation (duduk vs duduklah). Ayo + verb builds "
            "the let's-do pattern, completing the command family."
        ),
        "key_points": [
            "20 commands and requests, formal and informal.",
            "Three tiers: tolong/silakan (formal), -lah/bare (everyday), jangan (don't).",
            "-Lah softens: duduk (sit!) vs duduklah (do sit down).",
            "Dilarang = officially prohibited (signs).",
        ],
        "requirements": [
            "Know -lah and jangan from the grammar record.",
            "Give five commands to your room in Indonesian.",
        ],
        "standards": [
            "Command forms are standard; mohon is formal written/official.",
        ],
        "citations": [CIT_SNEDDON_G, CIT_ALWI],
        "must_contain": ["-lah", "tolong", "silakan", "jangan", "Dilarang"],
        "sig_lens": (
            "Through the Signature lens a command is a sworn directive: "
            "tolong the velvet seal of courtesy, -lah the softening wax, "
            "and jangan the red line no vow may cross."
        ),
        "drill": {
            "sentences": 20,
            "tiers": {"formal": ["tolong", "silakan", "mohon"],
                      "everyday": ["-lah", "bare verb", "ayo"],
                      "prohibition": ["jangan", "dilarang"]},
            "softener": "-lah",
        },
    },
    {
        "key": "descriptions",
        "name": "Descriptions - 20 Sentences on People and Places",
        "group": "Grammar in Action",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences describing people, places, and things in "
            "detail. Description stacks adjectives after nouns and links "
            "clauses with yang (who/which). \n\n"
            "  Ibu saya orang yang sabar dan penyayang. - My mother is a "
            "patient and loving person.\n"
            "  Tetangga kami tinggi dan berkacamata. - Our neighbor is "
            "tall and wears glasses.\n"
            "  Anak kecil itu berambut keriting. - That small child has "
            "curly hair.\n"
            "  Guru baru itu pintar dan lucu. - The new teacher is smart "
            "and funny.\n"
            "  Nenek memasak dengan tangan yang cekatan. - Grandmother "
            "cooks with skillful hands.\n"
            "  Sopir itu ramah kepada semua penumpang. - That driver is "
            "friendly to all passengers.\n"
            "  Rumah kami bercat putih dengan pagar hijau. - Our house is "
            "painted white with a green fence.\n"
            "  Kebun di belakang penuh bunga warna-warni. - The garden at "
            "the back is full of colorful flowers.\n"
            "  Pantai itu berpasir putih dan berair jernih. - That beach "
            "has white sand and clear water.\n"
            "  Kota tua itu sepi dan bersejarah. - That old town is quiet "
            "and historic.\n"
            "  Pasar pagi ramai dan berwarna. - The morning market is busy "
            "and colorful.\n"
            "  Gunung itu tinggi menjulang ke awan. - That mountain towers "
            "high into the clouds.\n"
            "  Sungai mengalir tenang di antara sawah. - The river flows "
            "calmly between rice fields.\n"
            "  Kamar hotelnya bersih dan nyaman. - His hotel room is clean "
            "and comfortable.\n"
            "  Jalanan kota macet pada jam sibuk. - The city streets are "
            "jammed at rush hour.\n"
            "  Langit malam bertabur bintang. - The night sky is studded "
            "with stars.\n"
            "  Kue ini manis dan lembut di lidah. - This cake is sweet and "
            "soft on the tongue.\n"
            "  Bajunya batik bermotif indah. - Her dress is batik with a "
            "beautiful pattern.\n"
            "  Suaranya merdu dan menenangkan. - Her voice is melodious "
            "and calming.\n"
            "  Pemandangan dari sini luar biasa. - The view from here is "
            "extraordinary."
        ),
        "how_it_works": (
            "Description is taught as noun + stacked adjectives + yang-"
            "clauses: the yang relative (orang yang sabar) is the "
            "workhorse that lets one noun carry a whole portrait. Ber- "
            "possession forms (berkacamata, berpasir, bermotif) pack "
            "has-a-X into a single word, a compact elegance the examples "
            "drill repeatedly. Place descriptions layer prepositional "
            "phrases (di antara sawah, dari sini) onto the adjective "
            "stacks."
        ),
        "key_points": [
            "20 descriptive sentences, every one translated.",
            "Yang-clauses carry portraits: orang yang sabar.",
            "Ber- packs possession: berkacamata, berpasir putih.",
            "Adjective stacks trail the noun: bunga warna-warni.",
        ],
        "requirements": [
            "Master yang and ber- from the grammar record.",
            "Describe three people and three places from memory.",
        ],
        "standards": [
            "Descriptive forms are standard literary and spoken Indonesian.",
        ],
        "citations": [CIT_SNEDDON_G, CIT_ECHOLS],
        "must_contain": ["yang sabar", "berkacamata", "warna-warni", "batik", "bertabur"],
        "sig_lens": (
            "Through the Signature lens description is sworn portraiture: "
            "each adjective a brushstroke sealed upon the noun, each "
            "yang-clause a frame that holds the likeness true."
        ),
        "drill": {
            "sentences": 20,
            "people": 6, "places": 10, "things": 4,
            "yang_clauses": 5, "ber_forms": ["berkacamata", "berpasir",
                                             "bermotif", "bertabur"],
        },
    },
    {
        "key": "story1",
        "name": "Story I - A Simple Ten-Sentence Story",
        "group": "Stories and Idioms",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence simple story in Indonesian, with line-by-line "
            "English translation. Present tense, everyday words, one "
            "clear arc. \n\n"
            "  1. Setiap pagi, Budi bangun jam lima. - Every morning, Budi "
            "wakes up at five o'clock.\n"
            "  2. Dia mencuci muka dan sarapan nasi goreng. - He washes "
            "his face and eats fried rice for breakfast.\n"
            "  3. Setelah itu, dia berjalan ke sekolah. - After that, he "
            "walks to school.\n"
            "  4. Di sekolah, dia bertemu teman-temannya. - At school, he "
            "meets his friends.\n"
            "  5. Mereka belajar matematika dan Bahasa Indonesia. - They "
            "study mathematics and Indonesian.\n"
            "  6. Saat istirahat, mereka bermain bola di lapangan. - "
            "During break, they play ball in the field.\n"
            "  7. Siang hari, Budi pulang dan makan siang. - At midday, "
            "Budi goes home and has lunch.\n"
            "  8. Sore hari, dia membantu ibu di kebun. - In the "
            "afternoon, he helps mother in the garden.\n"
            "  9. Malam hari, dia mengerjakan PR dan membaca buku. - At "
            "night, he does homework and reads a book.\n"
            "  10. Kemudian dia tidur dengan nyenyak. - Then he sleeps "
            "soundly."
        ),
        "how_it_works": (
            "The story is a day-arc: morning to night, ten beats, each "
            "sentence one new verb in the present-habitual frame, so the "
            "narrative teaches time-of-day words (pagi, siang, sore, "
            "malam) as its skeleton. Every sentence reuses only "
            "vocabulary from records 4-20 - no new words - proving the "
            "learner already owns the language of a whole day. Read it "
            "aloud straight through; it is the first fluency test."
        ),
        "key_points": [
            "10-sentence story, line-by-line English translation.",
            "Present-habitual tense; a full day arc morning to night.",
            "Zero new vocabulary - only words from earlier records.",
            "First fluency test: read aloud straight through.",
        ],
        "requirements": [
            "All vocabulary and tense records should be familiar.",
            "Retell the story from memory in Indonesian.",
        ],
        "standards": [
            "Narrative uses standard storybook Indonesian.",
        ],
        "citations": [CIT_SNEDDON_R],
        "must_contain": ["Setiap pagi", "teman-temannya", "mengerjakan PR", "nyenyak"],
        "sig_lens": (
            "Through the Signature lens this day is a sworn cycle: ten "
            "beats like ten seals pressed in order, from the morning "
            "vow of waking to the night's covenant of rest."
        ),
        "drill": {
            "sentences": 10, "tense": "present-habitual",
            "dayparts": ["pagi", "siang", "sore", "malam"],
            "new_words": 0,
        },
    },
    {
        "key": "story2",
        "name": "Story II - A Ten-Sentence Story in the Past",
        "group": "Stories and Idioms",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the past tense, with line-by-line "
            "English translation. Sudah and telah carry the completed "
            "action; time anchors order the events. \n\n"
            "  1. Tahun lalu, keluarga kami pergi ke Bali. - Last year, "
            "our family went to Bali.\n"
            "  2. Kami telah merencanakan perjalanan itu selama tiga "
            "bulan. - We had planned that trip for three months.\n"
            "  3. Pesawat lepas landas jam tujuh pagi. - The plane took "
            "off at seven in the morning.\n"
            "  4. Setibanya di sana, kami langsung ke pantai. - Upon "
            "arriving there, we went straight to the beach.\n"
            "  5. Anak-anak sudah berenang sebelum makan siang. - The "
            "children had already swum before lunch.\n"
            "  6. Kami makan ikan bakar di tepi laut. - We ate grilled "
            "fish by the sea.\n"
            "  7. Sore harinya, kami menonton matahari terbenam. - That "
            "afternoon, we watched the sunset.\n"
            "  8. Ibu membeli oleh-oleh untuk nenek. - Mother bought "
            "souvenirs for grandmother.\n"
            "  9. Kami pulang dengan hati gembira. - We returned home with "
            "glad hearts.\n"
            "  10. Perjalanan itu tak akan kami lupakan. - We will never "
            "forget that trip."
        ),
        "how_it_works": (
            "Past narration is taught as a chain of completed seals: "
            "sudah/telah mark what is finished, time words (tahun lalu, "
            "setibanya, sore harinya) order the chain, and the final "
            "sentence reaches into the future (tak akan lupakan) to "
            "close the arc. Oleh-oleh (souvenirs) is the cultural word "
            "every traveler learns, and the ter- form terbenam shows the "
            "prefix in its stative glory."
        ),
        "key_points": [
            "10-sentence past-tense story, line-by-line translation.",
            "Sudah/telah seal completed actions; time words order events.",
            "Oleh-oleh: the traveler's cultural keyword.",
        ],
        "requirements": [
            "Master the past markers of the tense record.",
            "Retell a real past trip in ten Indonesian sentences.",
        ],
        "standards": [
            "Narrative uses standard storybook Indonesian.",
        ],
        "citations": [CIT_SNEDDON_G],
        "must_contain": ["Tahun lalu", "telah merencanakan", "oleh-oleh", "matahari terbenam", "tak akan"],
        "sig_lens": (
            "Through the Signature lens the past is a sealed archive: "
            "each sudah a wax stamp on a finished deed, the whole journey "
            "a covenant of memory the family carries home."
        ),
        "drill": {
            "sentences": 10, "tense": "past",
            "markers": ["sudah", "telah", "tahun lalu", "setibanya"],
            "cultural_words": ["oleh-oleh"],
        },
    },
    {
        "key": "story3",
        "name": "Story III - A Ten-Sentence Story in the Future",
        "group": "Stories and Idioms",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the future and conditional, with "
            "line-by-line English translation. Akan and mau carry the "
            "forward arc; kalau opens the what-if branch. \n\n"
            "  1. Tahun depan, saya akan lulus sekolah. - Next year, I "
            "will graduate from school.\n"
            "  2. Saya mau kuliah di Universitas Indonesia. - I want to "
            "study at the University of Indonesia.\n"
            "  3. Saya akan belajar dengan giat setiap hari. - I will "
            "study diligently every day.\n"
            "  4. Kalau lulus ujian, saya akan merayakannya. - If I pass "
            "the exam, I will celebrate it.\n"
            "  5. Ibu dan ayah akan sangat bangga. - Mother and father "
            "will be very proud.\n"
            "  6. Saya akan mencari pekerjaan yang baik. - I will look for "
            "a good job.\n"
            "  7. Kalau mendapat gaji pertama, saya akan menabung. - When "
            "I get my first salary, I will save.\n"
            "  8. Saya mau membeli rumah untuk orang tua. - I want to buy "
            "a house for my parents.\n"
            "  9. Semua mimpi itu akan terwujud dengan kerja keras. - All "
            "those dreams will come true with hard work.\n"
            "  10. Masa depan ada di tangan kita. - The future is in our "
            "hands."
        ),
        "how_it_works": (
            "Future narration pairs akan (neutral future) with mau (willed "
            "future) so the learner feels the modal difference in "
            "context, not in a rule list. Kalau-clauses build the "
            "conditional branch (kalau lulus... akan merayakannya), the "
            "simplest if-then engine in the language. The closing maxim "
            "(masa depan ada di tangan kita) is a real Indonesian "
            "saying-pattern, landing the story on a cultural note."
        ),
        "key_points": [
            "10-sentence future story, line-by-line translation.",
            "Akan (neutral) vs mau (willed) futures in living contrast.",
            "Kalau-clauses: the simplest conditional engine.",
        ],
        "requirements": [
            "Master akan/mau from the tense record.",
            "Write your own ten-sentence future in Indonesian.",
        ],
        "standards": [
            "Narrative uses standard storybook Indonesian.",
        ],
        "citations": [CIT_SNEDDON_G],
        "must_contain": ["Tahun depan", "akan lulus", "Kalau lulus", "menabung", "Masa depan"],
        "sig_lens": (
            "Through the Signature lens the future is a covenant sworn "
            "forward: each akan a promise stamped on tomorrow, each "
            "kalau a branch of possibility, and the closing maxim the "
            "seal upon the dream."
        ),
        "drill": {
            "sentences": 10, "tense": "future-conditional",
            "markers": ["akan", "mau", "kalau", "tahun depan"],
            "conditionals": 2,
        },
    },
    {
        "key": "idioms",
        "name": "Idioms and Proverbs - 20 Sayings",
        "group": "Stories and Idioms",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Twenty Indonesian idioms and proverbs (peribahasa): literal "
            "translation, real meaning, and an example sentence each. "
            "Peribahasa are quoted constantly in speech and writing - "
            "knowing them is fluency. \n\n"
            "  Bagai pinang dibelah dua. - Like a betel nut split in two. "
            "= Identical twins. Mereka bagai pinang dibelah dua. - They "
            "are like two peas in a pod.\n"
            "  Air beriak tanda tak dalam. - Rippling water is a sign it "
            "is not deep. = Big talkers know little. Air beriak tanda tak "
            "dalam, jangan percaya semua katanya. - Rippling water runs "
            "shallow; don't believe everything he says.\n"
            "  Besar pasak daripada tiang. - The peg is bigger than the "
            "post. = Living beyond one's means. Belanja begitu, besar "
            "pasak daripada tiang. - Shopping like that, you're living "
            "beyond your means.\n"
            "  Sambil menyelam minum air. - While diving, drink water. = "
            "Kill two birds with one stone. Dia sambil menyelam minum "
            "air. - He's killing two birds with one stone.\n"
            "  Tong kosong nyaring bunyinya. - The empty barrel sounds the "
            "loudest. = Empty vessels make most noise. Tong kosong nyaring "
            "bunyinya, katanya. - Empty barrels make the most noise, they "
            "say.\n"
            "  Seperti katak dalam tempurung. - Like a frog under a "
            "coconut shell. = Narrow-minded, sheltered. Jangan seperti "
            "katak dalam tempurung. - Don't be a frog under a shell.\n"
            "  Ada udang di balik batu. - There's a shrimp behind the "
            "rock. = A hidden agenda. Pujiannya? Ada udang di balik batu. "
            "- His praise? There's a shrimp behind the rock.\n"
            "  Mulutmu harimaumu. - Your mouth is your tiger. = Watch your "
            "words. Hati-hati, mulutmu harimaumu. - Careful, your mouth "
            "is your tiger.\n"
            "  Tak kenal maka tak sayang. - Not knowing means not loving. "
            "= Get to know me first. Tak kenal maka tak sayang, mari "
            "berkenalan. - You can't love what you don't know; let's get "
            "acquainted.\n"
            "  Sedikit-sedikit lama-lama menjadi bukit. - Little by little, "
            "over time, becomes a hill. = Small efforts accumulate. "
            "Menabung sedikit-sedikit lama-lama menjadi bukit. - Save "
            "little by little and it becomes a hill.\n"
            "  Di mana bumi dipijak, di situ langit dijunjung. - Wherever "
            "the earth is stepped on, there the sky is upheld. = Respect "
            "local customs. Di mana bumi dipijak, di situ langit "
            "dijunjung. - When in Rome, do as the Romans do.\n"
            "  Bagai aur dengan tebing. - Like bamboo and the riverbank. = "
            "Mutually supportive. Mereka bagai aur dengan tebing. - They "
            "support each other like bamboo and riverbank.\n"
            "  Nasi sudah menjadi bubur. - The rice has become porridge. = "
            "No use crying over spilled milk. Nasi sudah menjadi bubur, "
            "terima saja. - What's done is done; accept it.\n"
            "  Kambing hitam. - Black goat. = Scapegoat. Dia dijadikan "
            "kambing hitam. - He was made the scapegoat.\n"
            "  Lidah tak bertulang. - The tongue has no bone. = Careless, "
            "hurtful speech. Lidah tak bertulang, ucapannya menyakitkan. "
            "- The tongue has no bone; his words hurt.\n"
            "  Masuk telinga kanan keluar telinga kiri. - In the right "
            "ear, out the left. = In one ear and out the other. "
            "Nasihatku masuk telinga kanan keluar telinga kiri. - My "
            "advice went in one ear and out the other.\n"
            "  Bagai kacang lupa kulitnya. - Like a peanut forgetting its "
            "shell. = Ungrateful, forgetting one's roots. Jangan bagai "
            "kacang lupa kulitnya. - Don't be a peanut forgetting its "
            "shell.\n"
            "  Jauh di mata dekat di hati. - Far from the eyes, near to "
            "the heart. = Absence makes the heart grow fonder. Meski jauh "
            "di mata, dia dekat di hati. - Though far from sight, she's "
            "close to the heart.\n"
            "  Sepandai-pandai tupai melompat, akhirnya jatuh juga. - "
            "However clever the squirrel's leap, it falls in the end. = "
            "Everyone slips eventually. Sepandai-pandai tupai melompat, "
            "akhirnya jatuh juga. - Even the cleverest slip in the end.\n"
            "  Rajin pangkal pandai. - Diligence is the root of "
            "cleverness. = Practice makes perfect. Rajin pangkal pandai, "
            "teruslah belajar. - Diligence is the root of skill; keep "
            "studying."
        ),
        "how_it_works": (
            "Each peribahasa is unpacked in three layers - the literal "
            "image, the real meaning, and a living example - because the "
            "literal image is the memory hook and the example is the "
            "usage license. Nature images dominate (water, bamboo, frog, "
            "tiger), revealing the agrarian imagination behind the "
            "language. The record is the cultural summit of the database: "
            "quoting these correctly marks the speaker as truly fluent."
        ),
        "key_points": [
            "20 peribahasa: literal image + real meaning + example sentence.",
            "Nature imagery dominates: water, bamboo, frog, tiger, rice.",
            "Quoting peribahasa correctly is a fluency marker.",
        ],
        "requirements": [
            "All earlier records should be comfortable.",
            "Use five peribahasa in real conversation this week.",
        ],
        "standards": [
            "Peribahasa are standard, widely-quoted sayings; glosses follow standard usage.",
        ],
        "citations": [CIT_ECHOLS, CIT_ALWI],
        "must_contain": ["peribahasa", "pinang dibelah dua", "kambing hitam", "Mulutmu harimaumu", "Rajin pangkal pandai"],
        "sig_lens": (
            "Through the Signature lens each proverb is a sworn maxim of "
            "the elders: the literal image a painted seal, the hidden "
            "meaning the covenant inside, passed hand to hand across "
            "generations."
        ),
        "drill": {
            "sayings": 20,
            "layers": ["literal", "meaning", "example"],
            "nature_images": ["pinang", "air", "katak", "harimau", "nasi",
                              "aur", "tupai", "kambing"],
        },
    },
    {
        "key": "registers",
        "name": "Formal and Polite Registers - 15 Pairs",
        "group": "Conversation and Registers",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen formal-vs-informal pairs for letters, business, and "
            "elders. Formal Indonesian (baku) uses saya/Anda, full "
            "affixes, and ceremonial openers; colloquial speech uses "
            "aku/kamu and clipped forms. \n\n"
            "  Formal: Dengan hormat, saya mengajukan lamaran ini. / "
            "Informal: Gue mau ngelamar kerja nih. (I am applying for "
            "this job.)\n"
            "  Formal: Apakah Bapak berkenan hadir? / Informal: Bapak bisa "
            "datang nggak? (Can you attend, Sir?)\n"
            "  Formal: Terima kasih atas perhatian Bapak/Ibu. / Informal: "
            "Makasih banyak ya. (Thank you for your attention.)\n"
            "  Formal: Mohon maaf atas ketidaknyamanan ini. / Informal: "
            "Maaf ya, nggak enak nih. (Sorry for this inconvenience.)\n"
            "  Formal: Saya ingin menyampaikan pendapat. / Informal: Gue "
            "mau ngomong nih. (I want to give my opinion.)\n"
            "  Formal: Bagaimana kabar Anda? / Informal: Apa kabar lo? "
            "(How are you?)\n"
            "  Formal: Silakan menunggu di ruang tamu. / Informal: "
            "Tunggu di sini aja. (Please wait in the living room.)\n"
            "  Formal: Kami akan segera menindaklanjuti. / Informal: "
            "Nanti gue urus. (We will follow up soon.)\n"
            "  Formal: Hormat saya, Budi Santoso. / Informal: Salam, Budi. "
            "(Respectfully, Budi Santoso. / Cheers, Budi.)\n"
            "  Formal: Dimohon kehadirannya tepat waktu. / Informal: "
            "Datang on time ya. (Please arrive on time.)\n"
            "  Formal: Saya tidak dapat menghadiri acara tersebut. / "
            "Informal: Gue nggak bisa datang. (I can't attend the event.)\n"
            "  Formal: Atas kerja sama yang baik, kami ucapkan terima "
            "kasih. / Informal: Makasih kerja samanya ya. (Thanks for the "
            "good cooperation.)\n"
            "  Formal: Berapa biaya administrasinya? / Informal: "
            "Administrasinya berapa? (What is the admin fee?)\n"
            "  Formal: Saya permisi terlebih dahulu. / Informal: Gue cabut "
            "dulu ya. (I'll take my leave now.)\n"
            "  Formal: Semoga Bapak/Ibu sehat selalu. / Informal: Sehat-"
            "sehat ya. (Wishing you good health.)"
        ),
        "how_it_works": (
            "Each pair is the same message in two social keys, so the "
            "learner sees exactly which elements shift: pronouns "
            "(saya/aku, Anda/kamu-lo), negation (tidak/nggak), prefixes "
            "kept or clipped (menyampaikan/ngomong), and ceremonial "
            "frames (Dengan hormat / Hormat saya). Jakarta colloquial "
            "(gue/lo, nggak) is shown as what it is - the capital's "
            "street register, not standard - so learners recognize it "
            "without writing it in a job letter."
        ),
        "key_points": [
            "15 formal/informal pairs, every message in two keys.",
            "Formal: saya/Anda, full affixes, Dengan hormat/Hormat saya frames.",
            "Colloquial Jakarta (gue/lo, nggak) is for recognition, not for letters.",
            "Wrong register is a social error, not a grammar error.",
        ],
        "requirements": [
            "Master pronouns and affixes from earlier records.",
            "Rewrite five informal sentences into formal Indonesian.",
        ],
        "standards": [
            "Formal forms are standard baku; colloquial forms labeled as Jakarta street register.",
        ],
        "citations": [CIT_SNEDDON_R, CIT_ALWI],
        "must_contain": ["Dengan hormat", "Hormat saya", "gue", "nggak", "baku"],
        "sig_lens": (
            "Through the Signature lens register is the covenant's "
            "dress code: formal the sealed robe of ceremony, informal "
            "the working clothes of kinship, each sworn appropriate to "
            "its hour."
        ),
        "drill": {
            "pairs": 15,
            "formal_markers": ["Dengan hormat", "Hormat saya", "Mohon",
                               "Dimohon"],
            "colloquial_markers": ["gue", "lo", "nggak"],
            "pronoun_shift": ["saya/aku", "Anda/kamu"],
        },
    },
    {
        "key": "complex",
        "name": "Compound and Complex Sentences - 15 Parsed",
        "group": "Conversation and Registers",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen long sentences with clauses, connectors, and "
            "relative clauses - each parsed and translated. The "
            "connectors are the mortar of advanced Indonesian. \n\n"
            "  Saya pergi ke pasar karena ibu meminta tolong. - I went to "
            "the market because mother asked for help. [karena = "
            "because]\n"
            "  Dia pintar tetapi malas belajar. - He is smart but lazy "
            "about studying. [tetapi = but]\n"
            "  Walaupun hujan, mereka tetap bermain bola. - Although it "
            "rained, they kept playing ball. [walaupun = although]\n"
            "  Dia belajar giat sehingga lulus dengan nilai bagus. - She "
            "studied hard so she passed with good grades. [sehingga = so "
            "that]\n"
            "  Buku yang saya baca sangat menarik. - The book that I read "
            "is very interesting. [yang = who/which]\n"
            "  Orang yang berdiri di sana adalah guru saya. - The person "
            "standing there is my teacher. [yang + verb]\n"
            "  Ketika saya tiba, rapat sudah dimulai. - When I arrived, "
            "the meeting had started. [ketika = when]\n"
            "  Jika kamu rajin, kamu akan berhasil. - If you are diligent, "
            "you will succeed. [jika = if]\n"
            "  Supaya sehat, makanlah sayur setiap hari. - To stay "
            "healthy, eat vegetables every day. [supaya = in order to]\n"
            "  Sambil menunggu, dia membaca koran. - While waiting, he "
            "read the newspaper. [sambil = while]\n"
            "  Sebelum pergi, kunci semua pintu. - Before leaving, lock "
            "all the doors. [sebelum = before]\n"
            "  Setelah makan, kami berjalan-jalan. - After eating, we took "
            "a stroll. [sesudah/setelah = after]\n"
            "  Dia tidak datang maupun menelepon. - He neither came nor "
            "called. [maupun = nor]\n"
            "  Semakin banyak latihan, semakin baik hasilnya. - The more "
            "practice, the better the result. [semakin...semakin = the "
            "more...the more]\n"
            "  Bukan hanya pintar, dia juga rajin. - Not only smart, she "
            "is also diligent. [bukan hanya...juga = not only...but also]"
        ),
        "how_it_works": (
            "Each sentence is glossed with its connector in brackets, "
            "turning fifteen sentences into a connector dictionary with "
            "living examples. Yang-relatives get two patterns (yang + "
            "verb, yang + saya + verb) because the relative clause is "
            "the single most-used complex structure. Correlative pairs "
            "(semakin...semakin, bukan hanya...juga) close the record as "
            "the most advanced frames, each decomposable into its two "
            "halves."
        ),
        "key_points": [
            "15 complex sentences, each parsed with its connector glossed.",
            "Core connectors: karena, tetapi, walaupun, sehingga, yang, ketika, jika.",
            "Yang-relatives: the most-used complex structure.",
            "Correlatives: semakin...semakin, bukan hanya...juga.",
        ],
        "requirements": [
            "All grammar records must be solid first.",
            "Combine ten simple sentence pairs using these connectors.",
        ],
        "standards": [
            "Connector usage follows standard written and spoken Indonesian.",
        ],
        "citations": [CIT_SNEDDON_G, CIT_ALWI],
        "must_contain": ["karena", "walaupun", "sehingga", "semakin", "yang saya baca"],
        "sig_lens": (
            "Through the Signature lens connectors are the covenant's "
            "mortar: karena the seal of reason, yang the clasp binding "
            "clause to noun, and semakin...semakin the rising vow that "
            "lifts both halves together."
        ),
        "drill": {
            "sentences": 15,
            "connectors": ["karena", "tetapi", "walaupun", "sehingga",
                           "yang", "ketika", "jika", "supaya",
                           "sambil", "sebelum", "setelah", "maupun",
                           "semakin", "bukan hanya"],
            "relative_patterns": 2,
        },
    },
    {
        "key": "convo_market",
        "name": "Conversation - At the Market (20 Lines)",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue at a traditional market, "
            "annotated. Buyer (Pembeli) and seller (Penjual) bargain over "
            "mangoes. \n\n"
            "  Penjual: Selamat pagi, Bu! Mau cari apa? - Good morning, "
            "Ma'am! What are you looking for? [greeting + offer]\n"
            "  Pembeli: Pagi, Pak. Mangga ini berapa sekilo? - Morning. "
            "How much are these mangoes per kilo? [price ask]\n"
            "  Penjual: Dua puluh lima ribu, Bu. Manis-manis! - Twenty-"
            "five thousand, Ma'am. Sweet ones! [price + pitch]\n"
            "  Pembeli: Wah, mahal sekali. Dua puluh ribu ya? - Wow, so "
            "expensive. Twenty thousand, okay? [react + bid]\n"
            "  Penjual: Belum bisa, Bu. Modalnya sudah dua puluh dua. - "
            "Can't yet, Ma'am. My cost is already twenty-two. [refuse + "
            "reason]\n"
            "  Pembeli: Ya sudah, dua puluh dua ribu. Saya ambil dua kilo. "
            "- Alright, twenty-two thousand. I'll take two kilos. "
            "[accept + quantity]\n"
            "  Penjual: Baik, Bu. Dipilih yang bagus-bagus ya. - Good, "
            "Ma'am. Pick the nice ones. [agree + invite to choose]\n"
            "  Pembeli: Yang ini dan yang ini. Total berapa? - These ones. "
            "What's the total? [choose + total]\n"
            "  Penjual: Empat puluh empat ribu, Bu. - Forty-four thousand, "
            "Ma'am. [total]\n"
            "  Pembeli: Ini lima puluh ribu. Kembali enam ribu ya? - Here's "
            "fifty thousand. Six thousand change, right? [pay + confirm]\n"
            "  Penjual: Betul, Bu. Ini kembaliannya. - Correct, Ma'am. "
            "Here's the change. [confirm + hand over]\n"
            "  Pembeli: Minta kantongnya dua ya, Pak. - Two bags please, "
            "Sir. [bag request]\n"
            "  Penjual: Silakan, Bu. Sudah dibungkus. - Here you go, "
            "Ma'am. Already wrapped. [serve]\n"
            "  Pembeli: Besok mangga masih ada? - Will there still be "
            "mangoes tomorrow? [return question]\n"
            "  Penjual: Ada, Bu. Datang pagi-pagi ya. - Yes, Ma'am. Come "
            "early. [promise + tip]\n"
            "  Pembeli: Baik, terima kasih banyak, Pak! - Good, thank you "
            "very much, Sir! [thanks]\n"
            "  Penjual: Sama-sama, Bu. Laris manis! - You're welcome, "
            "Ma'am. May they sell sweet! [blessing]\n"
            "  Pembeli: Hahaha, itu doa untuk Bapak. - Hahaha, that's a "
            "blessing for you. [joke]\n"
            "  Penjual: Sampai jumpa besok, Bu! - See you tomorrow, Ma'am! "
            "[farewell]\n"
            "  Pembeli: Sampai jumpa! - See you! [farewell]"
        ),
        "how_it_works": (
            "The dialogue is a complete market transaction with the "
            "bargaining beats numbered by their function in brackets: "
            "greet, ask, pitch, bid, refuse, accept, choose, total, pay, "
            "serve, bless, part. Pak/Bu address runs through every line, "
            "drilling respectful address as reflex. The laris manis "
            "blessing is the cultural gem - the seller's traditional "
            "good-luck wish - and the buyer's laugh shows the warmth "
            "that closes Indonesian deals."
        ),
        "key_points": [
            "20-line bilingual market dialogue, every line annotated.",
            "Complete transaction: greet to farewell.",
            "Pak/Bu respectful address on nearly every line.",
            "Laris manis: the seller's traditional blessing.",
        ],
        "requirements": [
            "Know the bargaining script of the shopping record.",
            "Act out both roles with a partner.",
        ],
        "standards": [
            "Dialogue uses natural market Indonesian nationwide.",
        ],
        "citations": [CIT_ECHOLS],
        "must_contain": ["Laris manis", "kembaliannya", "Modalnya", "pagi-pagi", "Sampai jumpa besok"],
        "sig_lens": (
            "Through the Signature lens the market dialogue is a sworn "
            "exchange ritual: each bid a proposal sealed in speech, the "
            "agreed price a covenant struck, and laris manis the blessing "
            "that witnesses it."
        ),
        "drill": {
            "lines": 20, "speakers": ["Penjual", "Pembeli"],
            "beats": ["greet", "ask", "pitch", "bid", "refuse", "accept",
                      "choose", "total", "pay", "serve", "bless", "part"],
            "address": ["Pak", "Bu"],
        },
    },
    {
        "key": "convo_friend",
        "name": "Conversation - Meeting a Friend (20 Lines)",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue between old friends meeting "
            "again, annotated. Rina and Dimas catch up after two years. \n\n"
            "  Rina: Dimas! Ya ampun, lama tidak bertemu! - Dimas! Oh my, "
            "long time no see! [surprised greeting]\n"
            "  Dimas: Rina! Apa kabar? Kamu kurusan ya? - Rina! How are "
            "you? You've gotten slimmer, huh? [greeting + remark]\n"
            "  Rina: Kabar baik! Iya, lagi diet nih. Kamu sendiri? - Good "
            "news! Yes, on a diet. And you? [answer + return]\n"
            "  Dimas: Baik juga. Masih di Jakarta? - Fine too. Still in "
            "Jakarta? [catch-up question]\n"
            "  Rina: Masih. Kamu katanya pindah ke Bandung? - Still. I "
            "heard you moved to Bandung? [confirm rumor]\n"
            "  Dimas: Iya, sudah setahun. Kerja di sana. - Yes, a year "
            "now. Working there. [confirm + detail]\n"
            "  Rina: Wah, enak ya Bandung. Dingin. - Wow, Bandung is nice. "
            "Cool air. [react]\n"
            "  Dimas: Enak, tapi macet juga sekarang. - Nice, but traffic "
            "jams too now. [qualify]\n"
            "  Rina: Hahaha, sama saja di mana-mana. - Hahaha, same "
            "everywhere. [laugh + generalize]\n"
            "  Dimas: Eh, kamu sudah nikah belum? - Hey, are you married "
            "yet? [personal question]\n"
            "  Rina: Belum! Masih betah sendiri. - Not yet! Still happily "
            "single. [deflect with humor]\n"
            "  Dimas: Sama dong. Bebas! - Same here. Free! [bond]\n"
            "  Rina: Ngomong-ngomong, mau kopi? - By the way, want "
            "coffee? [pivot + invite]\n"
            "  Dimas: Boleh! Yang di pojok itu enak. - Sure! The one on "
            "the corner is good. [accept + suggest]\n"
            "  Rina: Ayo. Sambil ngobrol. - Let's go. While chatting. "
            "[lead]\n"
            "  Dimas: Kamu masih suka baca novel? - Do you still like "
            "reading novels? [shared memory]\n"
            "  Rina: Masih! Terakhir baca yang tentang sejarah. - Still! "
            "Last read one about history. [answer]\n"
            "  Dimas: Pinjam dong nanti. - Lend it to me later. [request]\n"
            "  Rina: Boleh. Nanti aku kabari. - Sure. I'll let you know. "
            "[promise]\n"
            "  Dimas: Janji ya! Sampai ketemu lagi! - Promise! Until we "
            "meet again! [seal + farewell]"
        ),
        "how_it_works": (
            "The dialogue runs on colloquial warmth - nih, dong, ya "
            "particles, clipped questions - showing the informal key of "
            "record 29 in living use between equals. Each line's bracket "
            "names its conversational job (greet, deflect, bond, pivot), "
            "teaching dialogue as a sequence of moves. Sudah nikah belum "
            "is the famously Indonesian personal question, and the "
            "humorous deflection models the graceful answer."
        ),
        "key_points": [
            "20-line bilingual friend dialogue, every line annotated.",
            "Colloquial particles in action: nih, dong, ya.",
            "Dialogue as moves: greet, catch up, bond, pivot, seal.",
            "Sudah nikah belum: the classic personal question, gracefully deflected.",
        ],
        "requirements": [
            "Know informal register markers from the register record.",
            "Perform the dialogue, then improvise a reunion of your own.",
        ],
        "standards": [
            "Colloquial forms are natural spoken Indonesian between friends.",
        ],
        "citations": [CIT_ECHOLS],
        "must_contain": ["lama tidak bertemu", "sudah nikah belum", "Ngomong-ngomong", "Janji ya", "kurusan"],
        "sig_lens": (
            "Through the Signature lens reunion is a covenant renewed: "
            "the old names spoken aloud like seals re-pressed, the "
            "shared laughter a witness, and janji ya the vow that the "
            "friendship holds."
        ),
        "drill": {
            "lines": 20, "speakers": ["Rina", "Dimas"],
            "particles": ["nih", "dong", "ya"],
            "moves": ["greet", "catch-up", "bond", "pivot", "seal"],
        },
    },
    {
        "key": "convo_problem",
        "name": "Conversation - Solving a Problem (20 Lines)",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue solving a problem, "
            "annotated. A tenant (Penghuni) reports a leak to the building "
            "manager (Pengelola), and they fix it together. \n\n"
            "  Penghuni: Permisi, Pak. Ada masalah di kamar saya. - "
            "Excuse me, Sir. There's a problem in my room. [polite open]\n"
            "  Pengelola: Ada apa, Bu? Silakan duduk dulu. - What is it, "
            "Ma'am? Please sit down first. [invite + calm]\n"
            "  Penghuni: Atap kamar mandi bocor sejak kemarin. - The "
            "bathroom ceiling has leaked since yesterday. [state problem]\n"
            "  Pengelola: Wah, sudah lama ya. Airnya banyak? - Oh, since "
            "yesterday. Is there a lot of water? [assess]\n"
            "  Penghuni: Lumayan. Ember sampai penuh semalam. - Quite a "
            "bit. The bucket filled overnight. [quantify]\n"
            "  Pengelola: Baik, saya catat dulu. Kamar nomor berapa? - "
            "Okay, let me note it. Which room number? [record]\n"
            "  Penghuni: Kamar 204, lantai dua. - Room 204, second floor. "
            "[identify]\n"
            "  Pengelola: Tukang akan datang jam dua siang ini. - The "
            "repairman will come at two this afternoon. [promise action]\n"
            "  Penghuni: Apakah saya harus ada di kamar? - Must I be in "
            "the room? [clarify]\n"
            "  Pengelola: Tidak perlu, Bu. Kami punya kunci cadangan. - "
            "No need, Ma'am. We have a spare key. [reassure]\n"
            "  Penghuni: Kalau begitu saya titip kamar ya, Pak. - Then "
            "I'll entrust the room to you, Sir. [entrust]\n"
            "  Pengelola: Tentu. Semua aman. - Of course. All safe. "
            "[guarantee]\n"
            "  Penghuni: Berapa biayanya? - What is the cost? [ask cost]\n"
            "  Pengelola: Gratis, Bu. Itu tanggung jawab pengelola. - "
            "Free, Ma'am. That's management's responsibility. [waive]\n"
            "  Penghuni: Wah, terima kasih banyak! - Wow, thank you so "
            "much! [gratitude]\n"
            "  Pengelola: Sama-sama. Itu sudah tugas kami. - You're "
            "welcome. That's our duty. [duty]\n"
            "  Penghuni: Nanti saya cek lagi sore ini. - I'll check again "
            "this afternoon. [follow-up]\n"
            "  Pengelola: Silakan. Hubungi saya kalau masih bocor. - "
            "Please do. Contact me if it still leaks. [contingency]\n"
            "  Penghuni: Baik, Pak. Permisi dulu. - Good, Sir. Excuse me "
            "then. [close politely]\n"
            "  Pengelola: Mari, Bu. Semoga cepat beres! - Go ahead, Ma'am. "
            "Hope it's fixed soon! [bless the fix]"
        ),
        "how_it_works": (
            "The dialogue is a problem-solving template: open politely, "
            "state, assess, quantify, record, promise, clarify, entrust, "
            "cost, gratitude, follow-up, contingency, close. Formal "
            "register (Pak/Bu, silakan, permisi) runs throughout because "
            "problem-solving with officials demands the formal key. Titip "
            "(entrust) is the cultural keyword - leaving one's room in "
            "another's care - and the cost waiver shows the "
            "responsibility norm."
        ),
        "key_points": [
            "20-line bilingual problem-solving dialogue, annotated.",
            "Complete template: open, state, assess, promise, follow up, close.",
            "Formal register throughout - problems need the formal key.",
            "Titip: the cultural keyword of entrusting.",
        ],
        "requirements": [
            "Master formal register from the register record.",
            "Role-play reporting three different problems.",
        ],
        "standards": [
            "Dialogue uses standard formal spoken Indonesian.",
        ],
        "citations": [CIT_ECHOLS],
        "must_contain": ["bocor", "Tukang", "titip", "tanggung jawab", "cepat beres"],
        "sig_lens": (
            "Through the Signature lens problem-solving is a covenant of "
            "care: the complaint a sworn testimony, the promised repair "
            "a vow undertaken, and cepat beres the blessing that seals "
            "the work."
        ),
        "drill": {
            "lines": 20, "speakers": ["Penghuni", "Pengelola"],
            "template": ["open", "state", "assess", "promise", "clarify",
                         "cost", "follow-up", "close"],
            "register": "formal",
        },
    },
    {
        "key": "mastery",
        "name": "Mastery Review - The Whole Database in One Reference",
        "group": "Mastery Reference",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The consolidated quick-reference: the alphabet, 200 core "
            "words, the key grammar, and all phrase tables - the whole "
            "database in one teaching summary. \n\n"
            "The alphabet in one line: a b c d e f g h i j k l m n o p q "
            "r s t u v w x y z - 26 letters, 5 vowels (a e i o u), 4 "
            "digraphs (kh ng ny sy), 3 diphthongs (ai au oi), penultimate "
            "stress, no tones. \n\n"
            "200 core words, grouped: People - orang, anak, ibu, ayah, "
            "kakak, adik, teman, guru, dokter, tetangga; Body - kepala, "
            "mata, tangan, kaki, hati, perut; Home - rumah, pintu, jendela, "
            "meja, kursi, dapur, kamar; Food - nasi, air, kopi, teh, buah, "
            "sayur, daging, ikan, garam, gula; Nature - pohon, bunga, "
            "laut, gunung, sungai, hujan, matahari, langit; Animals - "
            "kucing, anjing, burung, ikan, ayam; Time - hari, minggu, "
            "bulan, tahun, pagi, siang, sore, malam, sekarang, kemarin, "
            "besok; Numbers - satu, dua, tiga, empat, lima, enam, tujuh, "
            "delapan, sembilan, sepuluh, seratus, seribu; Action - makan, "
            "minum, pergi, datang, melihat, membaca, menulis, belajar, "
            "bekerja, tidur, bangun, duduk, membeli, menjual, membuka, "
            "memberi; Quality - besar, kecil, baik, buruk, baru, panas, "
            "dingin, mahal, murah, cepat, senang, sedih; Little words - "
            "saya, kamu, dia, kami, kita, mereka, ini, itu, apa, siapa, di, "
            "ke, dari, dan, atau, tidak, bukan, sudah, sedang, akan, "
            "sangat, yang. \n\n"
            "Key grammar in one breath: SVO order; verbs never conjugate; "
            "time words sudah/sedang/akan carry tense; tidak/bukan/jangan "
            "negate; adjectives follow nouns with no agreement; plurals "
            "by reduplication (buku-buku); classifiers count (seorang, "
            "seekor, sebuah); affixes me-/ber-/di-/ter-/pe-/-kan/-i/-an "
            "build words; possession is owner-after-noun (buku saya) or "
            "suffixed (-ku/-mu/-nya); questions use intonation, apakah, "
            "-kah, or question words. \n\n"
            "Phrase tables: the four selamat greetings (pagi/siang/sore/"
            "malam); thanks (terima kasih / sama-sama); apology (maaf / "
            "permisi); farewell (sampai jumpa; selamat jalan to the "
            "leaver, selamat tinggal from the leaver); bargaining "
            "(berapa harganya? / mahal sekali! / saya tawar... / harga "
            "pas); directions (belok kiri/kanan, lurus, dekat/jauh); "
            "emergency (tolong! / panggil ambulans! / di mana rumah "
            "sakit?). \n\n"
            "The ladder you climbed: Foundations (overview, writing, "
            "pronunciation) -> Core Vocabulary (nouns, verbs, adjectives, "
            "pronouns, numbers, greetings) -> Grammar Essentials (ten "
            "rules) -> Everyday Themes (home, food, travel, work, "
            "health, emotions, nature, shopping, friendship, technology) "
            "-> Grammar in Action (tenses, Q&A, commands, descriptions) "
            "-> Stories and Idioms (three stories, peribahasa) -> "
            "Conversation and Registers (formal pairs, complex sentences, "
            "three dialogues) -> this Mastery Reference. \n\n"
            "Final sentences:\n"
            "  Saya sudah belajar Bahasa Indonesia. - I have studied "
            "Indonesian.\n"
            "  Saya sedang berbicara Bahasa Indonesia. - I am speaking "
            "Indonesian.\n"
            "  Saya akan terus belajar. - I will keep learning.\n"
            "  Terima kasih, dan sampai jumpa! - Thank you, and goodbye!"
        ),
        "how_it_works": (
            "The mastery record is the database compressed to one page: "
            "every earlier record contributes its densest line, so the "
            "page works as a daily review sheet and a final exam "
            "checklist. The 200-word core list is the active vocabulary "
            "target - own these and the themed sentences of records "
            "11-20 become readable. The ladder recap names every rung "
            "climbed, turning the whole database into a visible "
            "achievement."
        ),
        "key_points": [
            "The whole database in one reference: alphabet, 200 words, grammar, phrases.",
            "200 core words grouped by theme - the active vocabulary target.",
            "Grammar in one breath: the ten rules compressed.",
            "Phrase tables: greetings, thanks, bargaining, directions, emergency.",
        ],
        "requirements": [
            "This record is the capstone; all 33 before it are its prerequisites.",
            "Review this page weekly until every line is instant.",
        ],
        "standards": [
            "All summaries restate earlier records; no new claims introduced.",
        ],
        "citations": [CIT_SNEDDON_R, CIT_ECHOLS],
        "must_contain": ["200 core words", "buku-buku", "SVO", "sampai jumpa", "akan terus belajar"],
        "sig_lens": (
            "Through the Signature lens this reference is the covenant's "
            "charter: the whole journey sealed onto one page, every rung "
            "of the ladder a vow kept, and the learner's name written at "
            "the bottom in the language itself."
        ),
        "drill": {
            "core_words": 200, "groups": 12,
            "grammar_lines": 10, "phrase_tables": 7,
            "records_referenced": 33,
        },
    },
]
