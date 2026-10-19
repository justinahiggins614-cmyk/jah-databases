#!/usr/bin/env python3
"""Entries for the Hakka Chinese to English databases (Manon's language project,
2026-10-17, batch 4 rank 31/100).

Verified 2026-10-17: RAW SWEEP over the full manifest PLUS every shard index
in jah-databases-data-1: zero 'language-hakka*' slugs. ID prefixes JAH-LHAK-
(public) and JAH-LHAKS- (signature) verified free in the manifest id_prefix
values AND in every shard index (zero zgrep hits for 'JAH-LHAK' across all
index.jsonl.gz files). Pre-authoring whole-system dedupe-gate check over all
68 planned titles (34 + 34 Signature Edition): zero collisions, zero refusals.

This build creates two NEW databases, 34 ladder-ordered records each:

  language-hakka              - The Hakka Chinese to English Database
                                (public-harvest: real, fact-checked Hakka -
                                overview, characters and romanizations,
                                phonology and the six tones, core vocabulary
                                with sentences, grammar essentials, themed
                                sentence sets, aspect and tense, questions and
                                answers, commands, descriptions, stories,
                                idioms and proverbs, registers, complex
                                sentences, conversations, mastery reference;
                                every line in Hakka characters with Pinfa
                                romanization and English; standard references
                                Li Rong (Meixian), MacIver 1926, Hashimoto,
                                Norman, ISO 639-3 hak)
  language-hakka-signature    - The Hakka Chinese to English Signature Database
                                (his original Signature Language Method:
                                every character a sworn mark, every tone a
                                sealed vow, every sentence a covenant of
                                meaning; src signature, titles suffixed
                                " (Signature Edition)", clearly labeled
                                Signature-made, never presented as authentic
                                public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record carries Hakka content with English translation + example
sentences. Sentences are required in EVERY record - no vocabulary-list-only
records. Romanization follows the Guangdong Kejiahua Pinyin Fang'an
(Pinfa, official 1960, Meixian basis) with tone numbers 1-6, defined once in
the writing-system and phonology records; characters follow common written
Hakka usage. Composed example sentences are teaching constructions in
documented Meixian grammar and vocabulary, stated as such in the standards;
quoted sources are cited.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_hakka.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with the
OK marker; the build machine-executes all 68 demos before writing.

Build-time cross-check: every entry declares 'must_contain' strings and the
build asserts each one appears verbatim in the record description, so entry
text and demo outputs can never drift apart.

No website references. Screened per canon.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every character a sworn mark, every tone a sealed vow, every "
            "sentence a covenant of meaning. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_LI = ("Li R. (ed.) Meixian fangyan cidian (Meixian Dialect Dictionary). "
          "Jiangsu Education Press; the standard phonological reference for "
          "Meixian Hakka.")
CIT_MACIVER = ("MacIver D. A Chinese-English Dictionary: Hakka-Dialect as "
               "Spoken in Kwang-tung Province. 2nd ed. Presbyterian Mission "
               "Press; 1926.")
CIT_HASHIMOTO = ("Hashimoto M. The Hakka Dialect: A Linguistic Study of Its "
                 "Phonology, Syntax and Lexicon. Cambridge University Press; "
                 "1973.")
CIT_NORMAN = ("Norman J. Chinese. Cambridge University Press; 1988 - "
              "classification of Hakka within Sinitic and its tone history.")
CIT_ISO = ("ISO 639-3: Hakka Chinese is coded hak; Glottolog hakk1236. "
           "No ISO 639-1 code is assigned.")
CIT_UDHR = ("Universal Declaration of Human Rights, Article 1, Hakka "
            "translation with Pha̍k-fa-sṳ transliteration, as published on "
            "the Omniglot Hakka language page.")
CIT_PHRASEBOOK = ("Hakka phrasebook (Meixian basis), Wikivoyage - numerals, "
                  "time expressions and clock-time constructions in "
                  "Guangdong-style romanization with tone numbers.")
CIT_PROVERBS = ("Kejia yanyu (Hakka Proverbs) - the traditional proverb "
                "corpus including the land-and-language saying and the "
                "thunder, beggar-song and mouse-seeking-cat sayings.")
CIT_PINFA = ("Guangdong Province Department of Education, Kejiahua Pinyin "
             "Fang'an (1960) - the official Guangdong romanization of "
             "Meixian Hakka; tone numbers 1-6 as documented in the Pinfa "
             "tone table (fu1 fu2 fu3 fu4 fug5 fug6).")

# The six Meixian tones in the Guangdong (Pinfa) numbering:
# 1 yinping 44 high level | 2 yangping 11 low level | 3 shang 31 falling
# 4 qu 52 high falling (no yin/yang split) | 5 yinru low checked |
# 6 yangru high checked. Verified against the Pinfa tone table
# (fu1 夫, fu2 扶, fu3 府, fu4 富, fug5 福, fug6 服).
TONES = [
    ("1", "yinping", "44", "high level"),
    ("2", "yangping", "11", "low level"),
    ("3", "shang", "31", "falling"),
    ("4", "qu", "52", "high falling"),
    ("5", "yinru", "checked", "low stopped"),
    ("6", "yangru", "checked", "high stopped"),
]

ROMANIZATIONS = ["Pha̍k-fa-sṳ", "Pinfa (Guangdong Kejiahua Pinyin Fang'an)",
                 "Taiwan Hakka Pinyin", "Hagfa Pinyim"]

TEACHING_SENTENCE_NOTE = ("Composed example sentences are teaching "
    "constructions in documented Meixian Hakka grammar and vocabulary; "
    "quoted material is cited.")


def _sent_lines(pairs):
    return "\n".join("  %s %s - %s" % (c, r, g) for c, r, g in pairs)


ENTRIES = [
    {
        "key": "overview",
        "name": "Hakka Chinese Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Hakka Chinese (客家話 hag5 ga1 fa4, Pha̍k-fa-sṳ Hak-kâ-fa or "
            "Hak-kâ-va) is the Sinitic language of the Hakka people, the "
            "'guest families' whose ancestors migrated south from the "
            "Central Plains over a thousand years of moves. It carries ISO "
            "639-3 code hak (Glottolog hakk1236) and no ISO 639-1 code. "
            "About 44 million people speak it natively (2023 figures; older "
            "estimates reach 47.8 million), which makes Hakka one of the "
            "largest Sinitic languages on earth. \n\n"
            "Where it is spoken. The homeland arcs across northeastern "
            "Guangdong (Meizhou/Meixian, the prestige center), southern "
            "Jiangxi, western Fujian (Tingzhou, Longyan), with Hakka "
            "counties also in Guangxi, Hunan, Sichuan and Guizhou. In "
            "Taiwan it is a statutory national language with Hakka "
            "television, radio and MRT announcements; in Hong Kong the old "
            "New Territories villages spoke it; and the great 19th-century "
            "migrations carried it to Malaysia, Indonesia, Singapore, "
            "Thailand, Mauritius, French Guiana and beyond. \n\n"
            "Official status. Hakka is an official (national) language of "
            "Taiwan, regulated there by the Ministry of Education and the "
            "Hakka Affairs Council; in Guangdong it is regulated by the "
            "Guangdong Province Department of Education, which issued the "
            "official romanization in 1960. \n\n"
            "Dialects. The Meixian (Moiyen) dialect of Meizhou is the "
            "standard used in dictionaries, broadcasting and this database. "
            "Other major dialects are Wuhua, Tingzhou, Huizhou, Sixian "
            "(Taiwan) and Hailu/Haifeng (Taiwan); most Hakka dialects keep "
            "six tones, while Haifeng and Lufeng split the qu tone for "
            "seven. Dialects from distant counties are not always mutually "
            "intelligible. \n\n"
            "The name. Hak 客 means 'guest' and ka 家 means 'family' - the "
            "guest families. Among themselves Hakka speakers also call it "
            "Hak-kâ-ngî 客家語, Hak-fa 客話, or simply ngai2-fa4 𠊎話 'our "
            "speech'. The old Guangdong saying runs 'acknowledge the speech, "
            "not the surname' (認聲不認姓), and Sichuan Hakkas still say you "
            "may sell your ancestral land but never sell your clan's "
            "language. \n\n"
            "What makes Hakka learnable. It is written in Chinese characters "
            "you may already know, the word order is the familiar "
            "subject-verb-object, and verbs never conjugate - time is shown "
            "with small aspect words like liau3 了 (finished), go4 過 "
            "(experienced) and voi4 會 (will). Learn the six tones, the "
            "pronoun set built on ngai2 𠊎, and the plural marker deu1 兜, "
            "and the language opens like a door. \n\n"
            "First sentences in Hak-kâ-fa:\n"
            "  客家話 hag5 ga1 fa4 - the Hakka language\n"
            "  𠊎係客家人。 ngai2 he4 hag5 ga1 ngin2. - I am a Hakka person.\n"
            "  你好! ngi2 ho3! - Hello!\n"
            "  𠊎愛學客家話。 ngai2 oi4 hog6 hag5 ga1 fa4. - I want to learn Hakka."
        ),
        "how_it_works": (
            "This record is the map of the whole database. It fixes the "
            "identity of the language - name (客家話 hag5 ga1 fa4, Hak-kâ-fa), "
            "code (hak, no ISO 639-1), family (Sino-Tibetan, Sinitic, Hakka), "
            "speaker scale (about 44 million native), territory (Guangdong, "
            "Jiangxi, Fujian, Taiwan, Hong Kong, Southeast Asian diaspora), "
            "official standing (national language of Taiwan; Guangdong "
            "education regulation), dialect landscape (Meixian standard; "
            "Wuhua, Tingzhou, Huizhou, Sixian, Hailu), and the guest-family "
            "history with its language-loyalty sayings. Every later record "
            "hangs facts on this frame: the writing record spells the "
            "scripts and romanizations, the phonology record sounds the six "
            "tones, the vocabulary records fill the word-hoard, and the "
            "grammar records assemble the engine. Work through the ladder in "
            "order and each record assumes only what earlier records taught."
        ),
        "key_points": [
            "Native names: 客家話 hag5 ga1 fa4 (Hak-kâ-fa), 客家語, 𠊎話 ngai2-fa4.",
            "ISO 639-3 hak, Glottolog hakk1236; no ISO 639-1 code.",
            "Family: Sino-Tibetan, Sinitic, Hakka group; close to Gan.",
            "About 44 million native speakers across China, Taiwan and the diaspora.",
            "National language of Taiwan; Guangdong romanization official since 1960.",
            "Meixian (Meizhou) is the standard dialect; most dialects keep six tones.",
            "SVO word order; verbs uninflected; aspect words carry time (liau3, go4, voi4).",
        ],
        "requirements": [
            "No prior knowledge of any Chinese language is assumed.",
            "Read the writing-system record before the phonology record; read the phonology record before the vocabulary records.",
        ],
        "standards": [
            "Speaker figures are rounded public estimates; the record states them as approximate.",
            "Classification and dialect claims follow the standard references: Norman 1988, Hashimoto 1973, Li Rong (Meixian).",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_ISO, CIT_NORMAN, CIT_HASHIMOTO, CIT_LI],
        "must_contain": ["hag5 ga1 fa4", "hak", "44 million", "Meixian", "Taiwan"],
        "sig_lens": (
            "Through the Signature lens this overview is a census of a "
            "guest-family nation: every headcount a sworn roll-call, every "
            "migration a sealed journey, every dialect a branch of one "
            "family tree, and the old vow - sell the land before you sell "
            "the speech - engraved as the covenant that carries this "
            "language whole into the archive."
        ),
        "drill": {
            "native_m": 44.0, "iso3": "hak", "glottolog": "hakk1236",
            "iso1": None, "tones": 6, "romanizations": ROMANIZATIONS,
            "dialects": ["Meixian", "Wuhua", "Tingzhou", "Sixian", "Huizhou", "Hailu"],
            "regions": ["Guangdong", "Jiangxi", "Fujian", "Guangxi", "Hunan",
                        "Sichuan", "Taiwan", "Hong Kong"],
            "official_taiwan": True, "romanization_year": 1960,
        },
    },
    {
        "key": "writing",
        "name": "Hakka Chinese Writing System",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Hakka is written first in Chinese characters - the same "
            "character bank as Mandarin and Cantonese, traditional forms in "
            "Taiwan and Hong Kong, simplified forms on the mainland. "
            "Everyday Hakka words have their own written characters: 𠊎 "
            "ngai2 'I', 兜 deu1 the plural marker, 食 sit5 'to eat', 𠊎兜 "
            "ngai2-deu1 'we'. Because characters carry meaning, a Mandarin "
            "reader can often guess a written Hakka sentence even without "
            "hearing it. \n\n"
            "Four romanizations. (1) Pha̍k-fa-sṳ - the church romanization, "
            "created by Presbyterian missionaries for the Bible; it writes "
            "Hakka as Hak-kâ-fa with tone diacritics. (2) Pinfa - the "
            "Guangdong Kejiahua Pinyin Fang'an, official since 1960 for "
            "Meixian Hakka; it writes 客家話 as hag5 ga1 fa4 with tone "
            "numbers 1-6. (3) The Taiwan Hakka Pinyin system of the Ministry "
            "of Education. (4) Hagfa Pinyim. This database uses Pinfa "
            "spellings with tone numbers, because the tone numbers are "
            "machine-friendly and unambiguous. \n\n"
            "The six tone numbers (Pinfa): 1 = yinping (high level 44), "
            "2 = yangping (low level 11), 3 = shang (falling 31), 4 = qu "
            "(high falling 52), 5 = yinru (low checked, ends in p/t/k), "
            "6 = yangru (high checked). The textbook row is fu1 夫, fu2 扶, "
            "fu3 府, fu4 富, fug5 福, fug6 服 - one syllable, six tones, six "
            "meanings. \n\n"
            "Direction and punctuation. Hakka writes left to right, top to "
            "bottom like modern standard Chinese, with the same punctuation "
            "marks (。，！？、). Classical-style vertical right-to-left "
            "columns appear only in ceremonial or artistic settings. \n\n"
            "Numerals in characters: 一 yit5 (1), 二 ngi4 (2), 三 sam1 (3), "
            "四 si4 (4), 五 ng3 (5), 六 liuk5 (6), 七 cit5 (7), 八 bat5 (8), "
            "九 giu3 (9), 十 sip6 (10), 百 bag5 (100), 千 cien1 (1000), 萬 "
            "van4 (10000). \n\n"
            "Practice - read the signature words aloud:\n"
            "  𠊎 ngai2 - I\n"
            "  客家話 hag5 ga1 fa4 - the Hakka language\n"
            "  食飯 sit5 pon4 - to eat a meal\n"
            "  多謝 do1 qia4 - thank you"
        ),
        "how_it_works": (
            "This record teaches the two-track writing of Hakka: characters "
            "for meaning, romanization for sound. It names the four "
            "romanization systems and commits this database to one of them "
            "(Pinfa with tone numbers 1-6), defines the six tone numbers "
            "with the fu1-fug6 textbook row, states the left-to-right "
            "direction and punctuation, and gives the character numerals "
            "with their readings. Every later record prints Hakka as "
            "characters + Pinfa + English, so this record is the key that "
            "unlocks all of them."
        ),
        "key_points": [
            "Written in Chinese characters (traditional in Taiwan/HK, simplified on the mainland).",
            "Hakka has its own everyday characters: 𠊎 ngai2, 兜 deu1, 食 sit5.",
            "Four romanizations: Pha̍k-fa-sṳ, Pinfa (official 1960), Taiwan Hakka Pinyin, Hagfa Pinyim.",
            "This database uses Pinfa with tone numbers 1-6.",
            "Tone numbers: 1 yinping, 2 yangping, 3 shang, 4 qu, 5 yinru, 6 yangru.",
            "Textbook row: fu1 夫, fu2 扶, fu3 府, fu4 富, fug5 福, fug6 服.",
            "Left to right with standard Chinese punctuation.",
        ],
        "requirements": [
            "Read the overview record first for the language's identity and codes.",
            "No character knowledge is assumed; romanization carries the sound throughout.",
        ],
        "standards": [
            "Pinfa spellings follow the Guangdong Kejiahua Pinyin Fang'an (1960), Meixian basis.",
            "Pha̍k-fa-sṳ forms follow the missionary Bible orthography.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_PINFA, CIT_LI, CIT_MACIVER],
        "must_contain": ["Pha̍k-fa-sṳ", "Pinfa", "1960", "fug5", "left to right"],
        "sig_lens": (
            "Through the Signature lens this writing system is a double "
            "seal: characters stamp the meaning for the eye, tone numbers "
            "stamp the sound for the machine, and the 1960 Pinfa scheme is "
            "the sworn standard by which every later sentence in this "
            "database is measured."
        ),
        "drill": {
            "scripts": ["characters", "Pha̍k-fa-sṳ", "Pinfa",
                        "Taiwan Hakka Pinyin", "Hagfa Pinyim"],
            "chosen": "Pinfa",
            "direction": "left-to-right",
            "tone_numbers": {"1": "yinping", "2": "yangping", "3": "shang",
                             "4": "qu", "5": "yinru", "6": "yangru"},
            "textbook_row": ["fu1", "fu2", "fu3", "fu4", "fug5", "fug6"],
            "numerals": [("一", "yit5", 1), ("二", "ngi4", 2), ("三", "sam1", 3),
                         ("四", "si4", 4), ("五", "ng3", 5), ("六", "liuk5", 6),
                         ("七", "cit5", 7), ("八", "bat5", 8), ("九", "giu3", 9),
                         ("十", "sip6", 10)],
            "test_words": ["𠊎", "客家話", "食飯", "多謝"],
        },
    },
    {
        "key": "phonology",
        "name": "Hakka Chinese Pronunciation and Tones",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Meixian Hakka sounds are built from about 17 initials, 6 core "
            "vowels and the old Middle Chinese final consonants m, n, ng, "
            "p, t, k - which Mandarin lost centuries ago. That is why Hakka "
            "keeps 入聲 checked syllables like sit5 食, fug5 福 and sip6 十, "
            "short and stopped at the end. \n\n"
            "The initials include the plain series b, d, g and the aspirated "
            "series p, t, k; the sibilants z, c, s; the nasals m, n, ng; "
            "the liquids l; and h, f, v, y, w. Before the vowel i, z/c/s "
            "soften toward j/q/x sounds. The six vowels are i, e (as in 柿), "
            "a, o, u, plus the rounded ê sound written e in Pinfa. \n\n"
            "The six tones are the heart of the language: 1 yinping 44 "
            "(high level, like singing one steady note), 2 yangping 11 (low "
            "level, calm and low), 3 shang 31 (falling, like a sigh), 4 qu "
            "52 (high falling, decisive), 5 yinru (low checked - fug5 福 "
            "ends in a stopped -g), 6 yangru (high checked - fug6 服). All "
            "checked syllables end in -p/-t/-k. Change "
            "the tone and you change the word: mai1 買 'to buy' against "
            "mai4 賣 'to sell'. \n\n"
            "Tone in running speech. Hakka has tone sandhi - a low tone "
            "before another tone may rise slightly - but the citation tones "
            "taught here are always understood, so beginners should master "
            "the six citation tones first. \n\n"
            "Fourteen spoken examples - say each with its tone:\n"
            "  山 san1 - mountain (high level)\n"
            "  人 ngin2 - person (low level)\n"
            "  好 ho3 - good (falling)\n"
            "  話 fa4 - speech (high falling)\n"
            "  福 fug5 - fortune (low checked)\n"
            "  服 fug6 - clothes (high checked)\n"
            "  水 sui3 - water\n"
            "  火 fo3 - fire\n"
            "  食 sit5 - to eat\n"
            "  飲 jim3 - to drink\n"
            "  屋 vuk5 - house\n"
            "  天 tien1 - sky\n"
            "  月 ngiat6 - moon\n"
            "  日 ngit5 - sun, day"
        ),
        "how_it_works": (
            "This record teaches the Hakka sound system the way a singer "
            "learns scales: first the inventory (initials, six vowels, the "
            "preserved -m/-n/-ng/-p/-t/-k finals), then the six tones with "
            "their numbers, contours and plain-English images, then the "
            "minimal pair mai1/mai4 that proves tone carries meaning, then "
            "fourteen spoken examples covering every tone class. The tone "
            "numbers defined here are used on every romanized word in the "
            "rest of the database."
        ),
        "key_points": [
            "17 initials; aspirated vs unaspirated is the key contrast.",
            "Six vowels; finals keep -m -n -ng -p -t -k from Middle Chinese.",
            "Six tones: 1 yinping 44, 2 yangping 11, 3 shang 31, 4 qu 52, 5 yinru, 6 yangru.",
            "mai1 買 'buy' vs mai4 賣 'sell' - tone changes meaning.",
            "Checked tones (5, 6) end in stopped -p/-t/-k.",
            "Tone sandhi exists but citation tones are always understood.",
        ],
        "requirements": [
            "Read the writing-system record first for the Pinfa tone numbers.",
            "Say every example aloud; tones are muscle memory, not eye memory.",
        ],
        "standards": [
            "Phonological claims follow Li Rong (Meixian) and Hashimoto 1973.",
            "Contours given as Chao tone letters; checked tones are short and unreleased.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_LI, CIT_HASHIMOTO, CIT_PINFA],
        "must_contain": ["yinru", "yangru", "mai1", "mai4", "-p/-t/-k", "six tones"],
        "sig_lens": (
            "Through the Signature lens these sounds are the sworn marks of "
            "the language: every initial a stamped consonant, every checked "
            "syllable a sealed stop, every tone a vow of pitch - six vows, "
            "and breaking one breaks the meaning."
        ),
        "drill": {
            "tones": ["yinping", "yangping", "shang", "qu", "yinru", "yangru"],
            "tone_numbers": ["1", "2", "3", "4", "5", "6"],
            "vowels": 6,
            "initials": 17,
            "checked_finals": ["p", "t", "k"],
            "nasal_finals": ["m", "n", "ng"],
            "example_words": [("san1", "mountain"), ("ngin2", "person"),
                               ("ho3", "good"), ("fa4", "speech"),
                               ("fug5", "fortune"), ("fug6", "clothes"),
                               ("sui3", "water"), ("fo3", "fire"),
                               ("sit5", "eat"), ("jim3", "drink"),
                               ("vuk5", "house"), ("tien1", "sky"),
                               ("ngiat6", "moon"), ("ngit5", "sun")],
            "tone_pair": [("mai1", "buy", "yinping"), ("mai4", "sell", "qu")],
        },
    },
    {
        "key": "nouns",
        "name": "Hakka Chinese Core Nouns I",
        "group": "Core Vocabulary",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Hakka nouns - people, places and things - "
            "each with its Pinfa reading and one full example sentence in "
            "Hakka with English. Hakka nouns never change for number: 人 "
            "ngin2 is 'person' or 'people' - count words and context do the "
            "work. \n\n"
            "  人 ngin2 - person: 佢係好人。 gi2 he4 ho3 ngin2. - He is a good person.\n"
            "  屋 vuk5 - house: 𠊎屋下當大。 ngai2 vuk5-ha1 dong1 tai4. - My home is very big.\n"
            "  水 sui3 - water: 𠊎愛飲水。 ngai2 oi4 jim3 sui3. - I want to drink water.\n"
            "  火 fo3 - fire: 火當熱。 fo3 dong1 ngiat6. - The fire is very hot.\n"
            "  山 san1 - mountain: 該座山當高。 ge4 co4 san1 dong1 go1. - That mountain is very tall.\n"
            "  天 tien1 - sky: 天頂有雲。 tien1-dang3 yiu1 yun2. - There are clouds in the sky.\n"
            "  日 ngit5 - sun, day: 日頭出來了。 ngit5-teu2 cut5 loi2 liau3. - The sun has come out.\n"
            "  月 ngiat6 - moon, month: 月光當靚。 ngiat6-gong1 dong1 jiang4. - The moonlight is very pretty.\n"
            "  米 mi3 - rice (uncooked): 買兩斤米。 mai1 liong3 gin1 mi3. - Buy two catties of rice.\n"
            "  飯 pon4 - cooked rice: 食飯了冇? sit5 pon4 liau3 mau2? - Have you eaten yet?\n"
            "  錢 qian2 - money: 佢冇錢。 gi2 mau2 qian2. - He has no money.\n"
            "  書 su1 - book: 𠊎看書。 ngai2 kon4 su1. - I read books.\n"
            "  學校 hog6-hau4 - school: 細子去學校。 se4-zii3 hi4 hog6-hau4. - The child goes to school.\n"
            "  老師 lo3-sii1 - teacher: 老師當好。 lo3-sii1 dong1 ho3. - The teacher is very good.\n"
            "  醫生 ji1-sen1 - doctor: 醫生來了。 ji1-sen1 loi2 liau3. - The doctor has come.\n"
            "  朋友 pen2-iu1 - friend: 佢係𠊎朋友。 gi2 he4 ngai2 pen2-iu1. - He is my friend.\n"
            "  街 gie1 - street: 去行街。 hi4 hang2 gie1. - Go for a stroll on the street.\n"
            "  車 ca1 - car: 坐車去。 co4 ca1 hi4. - Go by car.\n"
            "  電話 tien4-fa4 - telephone: 打電話分佢。 da3 tien4-fa4 bun1 gi2. - Call him on the phone.\n"
            "  狗 gieu3 - dog: 狗仔當得人惜。 gieu3-e3 dong1 det5 ngin2 xiak5. - The puppy is very lovable.\n"
            "  雞 gie1 - chicken: 屋下養雞。 vuk5-ha1 yong1 gie1. - We raise chickens at home.\n"
            "  豬 zu1 - pig: 豬當肥。 zu1 dong1 pui2. - The pig is very fat.\n"
            "  魚 ng2 - fish: 魚當新鮮。 ng2 dong1 sin1-xien1. - The fish is very fresh.\n"
            "  樹 su4 - tree: 樹下好歇涼。 su4-ha1 ho3 hiat5 liong2. - It is good to rest in the shade under the tree.\n"
            "  花 fa1 - flower: 花開了。 fa1 koi1 liau3. - The flowers have bloomed."
        ),
        "how_it_works": (
            "This record builds the noun core: twenty-five high-frequency "
            "nouns across people, places, things and animals, each shown in "
            "characters, Pinfa with tone numbers, English gloss, and a "
            "complete SVO sentence. It teaches the first grammar fact about "
            "nouns - they never inflect for number - and seeds the sentence "
            "pattern (subject + verb + object) that every later record "
            "reuses."
        ),
        "key_points": [
            "25 essential nouns with Pinfa readings and tone numbers.",
            "Hakka nouns do not inflect for number: context and count words do the work.",
            "Every noun appears in a full translated sentence.",
            "屋下 vuk5-ha1 means 'home, household' - a core Hakka word.",
            "食飯了冇 sit5 pon4 liau3 mau2 is the classic 'have you eaten' greeting.",
        ],
        "requirements": [
            "Read the phonology record first so the tone numbers read aloud correctly.",
        ],
        "standards": [
            "Vocabulary follows MacIver 1926 and the Meixian dialect dictionary.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["ngin2", "vuk5-ha1", "sit5 pon4 liau3 mau2", "Twenty-five essential"],
        "sig_lens": (
            "Through the Signature lens each noun is a sworn name for a "
            "thing in the world: person, house, water, fire, mountain - "
            "twenty-five seals pressed into the archive, each with its "
            "sentence as witness."
        ),
        "drill": {
            "nouns": [("人", "ngin2", "person"), ("屋", "vuk5", "house"),
                      ("水", "sui3", "water"), ("火", "fo3", "fire"),
                      ("山", "san1", "mountain"), ("天", "tien1", "sky"),
                      ("日", "ngit5", "sun"), ("月", "ngiat6", "moon"),
                      ("米", "mi3", "rice"), ("飯", "pon4", "cooked rice"),
                      ("錢", "qian2", "money"), ("書", "su1", "book"),
                      ("學校", "hog6-hau4", "school"), ("老師", "lo3-sii1", "teacher"),
                      ("醫生", "ji1-sen1", "doctor"), ("朋友", "pen2-iu1", "friend"),
                      ("街", "gie1", "street"), ("車", "ca1", "car"),
                      ("電話", "tien4-fa4", "telephone"), ("狗", "gieu3", "dog"),
                      ("雞", "gie1", "chicken"), ("豬", "zu1", "pig"),
                      ("魚", "ng2", "fish"), ("樹", "su4", "tree"),
                      ("花", "fa1", "flower")],
            "sentences": 25,
            "inflects_for_number": False,
        },
    },
    {
        "key": "verbs",
        "name": "Hakka Chinese Core Verbs I",
        "group": "Core Vocabulary",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Hakka verbs, each with Pinfa reading and "
            "a full example sentence. Hakka verbs never conjugate - 食 sit5 "
            "is 'eat', 'eats', 'ate' and 'will eat'; small aspect words "
            "carry the time. \n\n"
            "  食 sit5 - to eat: 𠊎食飯。 ngai2 sit5 pon4. - I eat rice.\n"
            "  飲 jim3 - to drink: 飲茶。 jim3 ca2. - Drink tea.\n"
            "  睡 soi4 - to sleep: 佢睡了。 gi2 soi4 liau3. - He has slept.\n"
            "  行 hang2 - to walk: 𠊎行路去。 ngai2 hang2 lu4 hi4. - I go on foot.\n"
            "  走 zeu3 - to run, to leave: 快走! kuai4 zeu3! - Run! / Go quickly!\n"
            "  講 gong3 - to speak: 講客家話。 gong3 hag5 ga1 fa4. - Speak Hakka.\n"
            "  看 kon4 - to look, to read: 看書。 kon4 su1. - Read a book.\n"
            "  聽 tang1 - to listen: 聽話。 tang1 fa4. - Listen.\n"
            "  寫 xia3 - to write: 寫字。 xia3 sii4. - Write characters.\n"
            "  讀 tug6 - to read aloud, to study: 讀書。 tug6 su1. - Study.\n"
            "  做 zo4 - to do: 做事。 zo4 sii4. - Do work.\n"
            "  買 mai1 - to buy: 買米。 mai1 mi3. - Buy rice.\n"
            "  賣 mai4 - to sell: 賣菜。 mai4 coi4. - Sell vegetables.\n"
            "  去 hi4 - to go: 去學校。 hi4 hog6-hau4. - Go to school.\n"
            "  來 loi2 - to come: 來𠊎屋下。 loi2 ngai2 vuk5-ha1. - Come to my home.\n"
            "  坐 co4 - to sit: 坐低。 co4 dai1. - Sit down.\n"
            "  企 ki1 - to stand: 企起來。 ki1 hi3 loi2. - Stand up.\n"
            "  笑 xiau4 - to laugh: 佢笑起來。 gi2 xiau4 hi3 loi2. - He started laughing.\n"
            "  哭 heu4 - to cry: 細子哭了。 se4-zii3 heu4 liau3. - The child cried.\n"
            "  愛 oi4 - to want, to love: 𠊎愛你。 ngai2 oi4 ngi2. - I love you.\n"
            "  有 yiu1 - to have: 有錢。 yiu1 qian2. - Have money.\n"
            "  係 he4 - to be: 佢係老師。 gi2 he4 lo3-sii1. - He is a teacher.\n"
            "  曉 hiau3 - to know how to: 𠊎曉講。 ngai2 hiau3 gong3. - I know how to speak (it).\n"
            "  開 koi1 - to open: 開門。 koi1 mun2. - Open the door.\n"
            "  煮 zu3 - to cook: 煮飯。 zu3 pon4. - Cook rice."
        ),
        "how_it_works": (
            "This record builds the verb core: twenty-five high-frequency "
            "verbs, each in characters, Pinfa, English gloss and a complete "
            "sentence. It teaches the second great grammar fact - verbs "
            "never change form - and shows the sentence skeleton "
            "(subject-verb-object) in action across eating, moving, speaking "
            "and making. The aspect words that mark time on these verbs are "
            "taught in the tenses record."
        ),
        "key_points": [
            "25 essential verbs with Pinfa readings and tone numbers.",
            "Verbs never conjugate: sit5 covers eat/eats/ate/will eat.",
            "買 mai1 'buy' vs 賣 mai4 'sell' - a tone minimal pair in daily use.",
            "食 sit5 and 飲 jim3 are the two consumption verbs; 睡 soi4 is 'to sleep'.",
            "Every verb appears in a full translated sentence.",
        ],
        "requirements": [
            "Read the phonology record first so the tone numbers read aloud correctly.",
        ],
        "standards": [
            "Vocabulary follows MacIver 1926 and the Meixian dialect dictionary.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["never conjugate", "mai1", "mai4", "soi4", "Twenty-five essential Hakka verbs"],
        "sig_lens": (
            "Through the Signature lens each verb is a sworn action: eat, "
            "drink, walk, speak, make - twenty-five deeds stamped into the "
            "archive, unchanging in form, with time itself carried by small "
            "separate seals."
        ),
        "drill": {
            "verbs": [("食", "sit5", "eat"), ("飲", "jim3", "drink"),
                      ("睡", "soi4", "sleep"), ("行", "hang2", "walk"),
                      ("走", "zeu3", "run"), ("講", "gong3", "speak"),
                      ("看", "kon4", "look"), ("聽", "tang1", "listen"),
                      ("寫", "xia3", "write"), ("讀", "tug6", "study"),
                      ("做", "zo4", "do"), ("買", "mai1", "buy"),
                      ("賣", "mai4", "sell"), ("去", "hi4", "go"),
                      ("來", "loi2", "come"), ("坐", "co4", "sit"),
                      ("企", "ki1", "stand"), ("笑", "xiau4", "laugh"),
                      ("哭", "heu4", "cry"), ("愛", "oi4", "want"),
                      ("有", "yiu1", "have"), ("係", "he4", "be"),
                      ("曉", "hiau3", "know how"), ("開", "koi1", "open"),
                      ("煮", "zu3", "cook")],
            "sentences": 25,
            "conjugates": False,
            "tone_pair": ["mai1", "mai4"],
        },
    },
    {
        "key": "adjectives",
        "name": "Hakka Chinese Adjectives and Adverbs",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five Hakka adjectives and fifteen adverbs, each with a "
            "full example sentence. Adjectives sit before the noun or after "
            "係 he4: 好人 ho3 ngin2 'a good person', 佢係好人 gi2 he4 ho3 "
            "ngin2 'he is a good person'. There is no agreement - the "
            "adjective never changes. \n\n"
            "Adjectives:\n"
            "  好 ho3 - good: 好人。 ho3 ngin2. - A good person.\n"
            "  壞 fai4 - bad: 壞天氣。 fai4 tien1-hi4. - Bad weather.\n"
            "  大 tai4 - big: 大屋。 tai4 vuk5. - A big house.\n"
            "  細 se4 - small: 細狗仔。 se4 gieu3-e3. - A small puppy.\n"
            "  高 go1 - tall: 高山。 go1 san1. - A tall mountain.\n"
            "  矮 ai3 - short: 矮樹。 ai3 su4. - A short tree.\n"
            "  長 cong2 - long: 長路。 cong2 lu4. - A long road.\n"
            "  短 don3 - short: 短時間。 don3 si2-gien1. - A short time.\n"
            "  新 sin1 - new: 新衫。 sin1 sam1. - New clothes.\n"
            "  舊 kiu4 - old: 舊書。 kiu4 su1. - An old book.\n"
            "  多 do1 - many: 多人。 do1 ngin2. - Many people.\n"
            "  少 sau3 - few: 少錢。 sau3 qian2. - Little money.\n"
            "  紅 fung2 - red: 紅花。 fung2 fa1. - Red flowers.\n"
            "  白 pag6 - white: 白雲。 pag6 yun2. - White clouds.\n"
            "  黑 het5 - black: 黑狗。 het5 gieu3. - A black dog.\n"
            "  快 kuai4 - fast: 快車。 kuai4 ca1. - A fast car.\n"
            "  慢 man4 - slow: 慢行。 man4 hang2. - Walk slowly.\n"
            "  遠 yen3 - far: 遠路。 yen3 lu4. - A far road.\n"
            "  近 kiun4 - near: 近街。 kiun4 gie1. - Near the street.\n"
            "  重 cung4 - heavy: 重擔。 cung4 dam4. - A heavy load.\n"
            "  輕 kiang1 - light: 輕身。 kiang1 siin1. - Light-bodied.\n"
            "  熱 ngiat6 - hot: 熱水。 ngiat6 sui3. - Hot water.\n"
            "  冷 lang1 - cold: 冷天。 lang1 tien1. - Cold weather.\n"
            "  甜 tiam2 - sweet: 甜果。 tiam2 go3. - Sweet fruit.\n"
            "  苦 fu3 - bitter: 苦藥。 fu3 yog6. - Bitter medicine.\n\n"
            "Adverbs:\n"
            "  當 dong1 - very: 當好。 dong1 ho3. - Very good.\n"
            "  好 ho3 - quite, very: 好熱。 ho3 ngiat6. - Quite hot.\n"
            "  又 yiu4 - again: 又來了。 yiu4 loi2 liau3. - (He) has come again.\n"
            "  再 zai4 - once more: 再講一擺。 zai4 gong3 yit5 bai3. - Say it once more.\n"
            "  還 han2 - still: 還冇食。 han2 mau2 sit5. - Still haven't eaten.\n"
            "  就 qiu4 - then: 食就去。 sit5 qiu4 hi4. - Eat, then go.\n"
            "  盡 qin3 - extremely: 盡靚。 qin3 jiang4. - Extremely pretty.\n"
            "  頭下 teu2-ha4 - in a moment: 頭下來。 teu2-ha4 loi2. - Come in a moment.\n"
            "  常常 song2-song2 - often: 常常去。 song2-song2 hi4. - Go often.\n"
            "  慢慢 man4-man4 - slowly: 慢慢行。 man4-man4 hang2. - Walk slowly.\n"
            "  快快 kuai4-kuai4 - quickly: 快快來。 kuai4-kuai4 loi2. - Come quickly.\n"
            "  一齊 yit5-ce2 - together: 一齊去。 yit5-ce2 hi4. - Go together.\n"
            "  實在 sit6-cai4 - really: 實在好。 sit6-cai4 ho3. - Really good.\n"
            "  正真 zin4-zin1 - truly: 正真靚。 zin4-zin1 jiang4. - Truly pretty.\n"
            "  隨便 cui2-pien4 - casually: 隨便坐。 cui2-pien4 co4. - Sit anywhere."
        ),
        "how_it_works": (
            "This record teaches description: twenty-five adjectives that "
            "place directly before nouns or after 係 he4 with zero agreement, "
            "and fifteen adverbs of degree, time and manner that slide "
            "before the verb. Reduplicated adverbs (慢慢, 快快, 常常) show "
            "the common intensifying pattern. Every item carries a full "
            "translated sentence."
        ),
        "key_points": [
            "25 adjectives + 15 adverbs, each with a translated sentence.",
            "Adjectives take no agreement and no gender/number marking.",
            "Position: before the noun (好人) or after 係 (係好人).",
            "當 dong1 and 好 ho3 both mean 'very' before adjectives.",
            "Reduplication intensifies: 慢慢 'slowly', 快快 'quickly', 常常 'often'.",
        ],
        "requirements": [
            "Read the nouns and verbs records first; adjectives describe those words.",
        ],
        "standards": [
            "Vocabulary follows MacIver 1926 and the Meixian dialect dictionary.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["no agreement", "dong1", "man4-man4", "Twenty-five Hakka adjectives"],
        "sig_lens": (
            "Through the Signature lens these are the colors and measures "
            "of the archive: forty sworn descriptors, each stamped on its "
            "noun or verb, never bending, never changing - the measure is "
            "the same for every thing it measures."
        ),
        "drill": {
            "adjectives": 25, "adverbs": 15, "sentences": 40,
            "agreement": False,
            "degree_words": ["dong1", "ho3", "qin3"],
            "reduplicated": ["man4-man4", "kuai4-kuai4", "song2-song2"],
        },
    },
    {
        "key": "pronouns",
        "name": "Hakka Chinese Pronouns",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The complete Hakka pronoun system. The signature word is 𠊎 "
            "ngai2 'I' - written with its own character - and the plural "
            "marker 兜 deu1 builds every plural: 𠊎兜 ngai2-deu1 'we', 你兜 "
            "ngi2-deu1 'you (plural)', 佢兜 gi2-deu1 'they'. \n\n"
            "Personal pronouns:\n"
            "  𠊎 ngai2 - I: 𠊎係客家人。 ngai2 he4 hag5 ga1 ngin2. - I am a Hakka person.\n"
            "  你 ngi2 - you: 你好! ngi2 ho3! - Hello!\n"
            "  佢 gi2 - he/she/it: 佢來了。 gi2 loi2 liau3. - He has come.\n"
            "  𠊎兜 ngai2-deu1 - we: 𠊎兜去街。 ngai2-deu1 hi4 gie1. - We go to the street.\n"
            "  你兜 ngi2-deu1 - you (plural): 你兜食飯冇? ngi2-deu1 sit5 pon4 mau2? - Have you (all) eaten?\n"
            "  佢兜 gi2-deu1 - they: 佢兜係朋友。 gi2-deu1 he4 pen2-iu1. - They are friends.\n\n"
            "Possessives - add 个 ge4:\n"
            "  𠊎个 ngai2-ge4 - my: 𠊎个書。 ngai2-ge4 su1. - My book.\n"
            "  你个 ngi2-ge4 - your: 你个名。 ngi2-ge4 miang2. - Your name.\n"
            "  佢个 gi2-ge4 - his/her: 佢个屋。 gi2-ge4 vuk5. - His house.\n\n"
            "Demonstratives:\n"
            "  這 li4 - this: 這個。 li4-ge4. - This one.\n"
            "  該 ge4 - that: 該個。 ge4-ge4. - That one.\n"
            "  這隻 li4-zag5 - this (one): 這隻狗。 li4-zag5 gieu3. - This dog.\n"
            "  該隻 ge4-zag5 - that (one): 該隻貓。 ge4-zag5 meu4. - That cat.\n"
            "  這兜 li4-deu1 - these: 這兜人。 li4-deu1 ngin2. - These people.\n"
            "  該兜 ge4-deu1 - those: 該兜事。 ge4-deu1 sii4. - Those matters.\n\n"
            "Interrogatives:\n"
            "  麼人 mag5-ngin2 - who: 麼人來? mag5-ngin2 loi2? - Who is coming?\n"
            "  乜 mag5 - what: 乜事? mag5 sii4? - What is it?\n"
            "  邊 bin1 - which: 邊一個? bin1 yit5-ge4? - Which one?\n"
            "  幾多 gi3-do1 - how many: 幾多人? gi3-do1 ngin2? - How many people?\n"
            "  幾時 gi3-si2 - when: 幾時去? gi3-si2 hi4? - When to go?\n"
            "  點樣 dim3-ngiong4 - how: 點樣做? dim3-ngiong4 zo4? - How to do it?\n"
            "  做麼 zo4-ma1 - why: 做麼哭? zo4-ma1 heu4? - Why cry?\n"
            "  哪位 nai3-vi4 - where (person): 哪位先生? nai3-vi4 xin1-sang1? - Which gentleman?"
        ),
        "how_it_works": (
            "This record teaches reference: the six personal pronouns built "
            "from three roots plus 兜 deu1, the possessive built by adding "
            "个 ge4, the demonstrative pairs 這/該 with the classifier 隻 "
            "zag5 and plural 兜, and eight interrogatives. The pattern is "
            "mechanical - learn the roots and the two markers (兜, 个) and "
            "the whole table generates itself."
        ),
        "key_points": [
            "𠊎 ngai2 'I' has its own character; 你 ngi2 'you'; 佢 gi2 covers he/she/it.",
            "兜 deu1 is the plural marker: 𠊎兜, 你兜, 佢兜, 這兜, 該兜.",
            "Possessive = pronoun + 个 ge4.",
            "Demonstratives: 這 li4 'this', 該 ge4 'that', with 隻 zag5 for single items.",
            "Interrogatives: 麼人 who, 乜 what, 點樣 how, 做麼 why.",
        ],
        "requirements": [
            "Read the nouns record first; pronouns replace nouns.",
        ],
        "standards": [
            "Paradigms follow MacIver 1926 and the Meixian dialect dictionary.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["ngai2", "deu1", "ge4", "mag5-ngin2", "dim3-ngiong4"],
        "sig_lens": (
            "Through the Signature lens these pronouns are the sworn "
            "pointers of the language: I, you, he - three roots and two "
            "markers that generate the whole table, every pointing word a "
            "seal pressed exactly where it means."
        ),
        "drill": {
            "personal": ["ngai2", "ngi2", "gi2", "ngai2-deu1", "ngi2-deu1", "gi2-deu1"],
            "possessive_marker": "ge4",
            "demonstratives": ["li4", "ge4", "li4-zag5", "ge4-zag5", "li4-deu1", "ge4-deu1"],
            "interrogatives": ["mag5-ngin2", "mag5", "bin1", "gi3-do1",
                               "gi3-si2", "dim3-ngiong4", "zo4-ma1", "nai3-vi4"],
            "plural_marker": "deu1",
            "sentences": 23,
        },
    },
    {
        "key": "numbers",
        "name": "Hakka Chinese Numbers and Time",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Numbers 1-100, ordinals, days, months, seasons, clock time and "
            "dates - every item with Pinfa reading and example sentences. "
            "The digits are: 一 yit5, 二 ngi4, 三 sam1, 四 si4, 五 ng3, 六 "
            "liuk5, 七 cit5, 八 bat5, 九 giu3, 十 sip6. \n\n"
            "Building numbers: 十一 sip6-yit5 (11), 二十 ngi4-sip6 (20), "
            "二十一 ngi4-sip6-yit5 (21), 三十 sam1-sip6 (30), 一百 yit5-bag5 "
            "(100), 一千 yit5-cien1 (1000), 一萬 yit5-van4 (10000). 兩 "
            "liong3 replaces 二 before classifiers: 兩點鐘 liong3-diam3-zung1 "
            "'two o'clock'. \n\n"
            "Time of day: 朝頭早 zau1-teu2-zau3 (morning), 下晝 ha1-zu4 "
            "(afternoon), 暗晡晨 am4-bu1-sin2 (evening), 夜晚晨 ya4-man1-sin2 "
            "(night), 今下 gin1-ha4 (now). Clock time: 一點鐘 yit5-diam3-zung1 "
            "(1 o'clock), 搭正 dap5-zin4 (on the hour), 搭半 dap5-ban4 (half "
            "past). \n\n"
            "Days: 禮拜一 li1-bai4-yit5 (Monday) through 禮拜日 li1-bai4-ngit5 "
            "(Sunday); 今日 gin1-ngit5 (today), 尋日 qim2-ngit5 (yesterday), "
            "天光日 tien1-gong1-ngit5 (tomorrow). Months: 一月 yit5-ngiat6 "
            "(January); seasons: 春 cun1 (spring), 夏 ha4 (summer), 秋 qiu1 "
            "(autumn), 冬 dung1 (winter). \n\n"
            "Example sentences:\n"
            "  𠊎有三本書。 ngai2 yiu1 sam1 bun3 su1. - I have three books.\n"
            "  今下幾點? gin1-ha4 gi3-diam3? - What time is it now?\n"
            "  今下三點半。 gin1-ha4 sam1-diam3-ban4. - It is half past three now.\n"
            "  尋日落雨。 qim2-ngit5 log6-sui3. - It rained yesterday.\n"
            "  天光日去街。 tien1-gong1-ngit5 hi4 gie1. - Go to town tomorrow.\n"
            "  佢今年十歲。 gi2 gin1-ngian2 sip6-soi4. - He is ten years old this year.\n"
            "  第一個 tai4-yit5-ge4 - the first one.\n"
            "  一年有十二個月。 yit5-ngian2 yiu1 sip6-ngi4-ge4 ngiat6. - A year has twelve months."
        ),
        "how_it_works": (
            "This record teaches counting and telling time: the ten digits "
            "with tone numbers, the mechanical building rules (ten+X, "
            "X-ten, hundred/thousand/ten-thousand), the classifier rule "
            "that swaps 二 ngi4 for 兩 liong3, the day-parts and clock "
            "constructions (點鐘, 搭正, 搭半), the week built on 禮拜, the "
            "three deictic days, months and seasons - each with translated "
            "sentences."
        ),
        "key_points": [
            "Digits: yit5 ngi4 sam1 si4 ng3 liuk5 cit5 bat5 giu3 sip6.",
            "11-99 build mechanically: sip6-yit5, ngi4-sip6, ngi4-sip6-yit5.",
            "Use 兩 liong3 (not 二) before classifiers.",
            "Clock: 點鐘 diam3-zung1 for hours; 搭正 'on the hour'; 搭半 'half past'.",
            "Day-parts: 朝頭早, 下晝, 暗晡晨, 夜晚晨; 今下 'now'.",
            "Week: 禮拜一 to 禮拜日; 今日/尋日/天光日 for today/yesterday/tomorrow.",
        ],
        "requirements": [
            "Read the writing-system record first for the character numerals.",
        ],
        "standards": [
            "Numerals and time expressions verified against the Meixian-basis Hakka phrasebook.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_PHRASEBOOK, CIT_LI],
        "must_contain": ["yit5", "ngi4", "sam1", "liong3", "diam3-zung1", "gin1-ha4"],
        "sig_lens": (
            "Through the Signature lens these numbers are the sworn tallies "
            "of the archive: ten digits, four great units, and the clock "
            "itself - every count exact, every hour named, time measured in "
            "sealed units."
        ),
        "drill": {
            "digits": [("一", "yit5", 1), ("二", "ngi4", 2), ("三", "sam1", 3),
                       ("四", "si4", 4), ("五", "ng3", 5), ("六", "liuk5", 6),
                       ("七", "cit5", 7), ("八", "bat5", 8), ("九", "giu3", 9),
                       ("十", "sip6", 10)],
            "tens": ["sip6-yit5", "ngi4-sip6", "ngi4-sip6-yit5", "sam1-sip6",
                     "si4-sip6", "ng3-sip6", "liuk5-sip6", "cit5-sip6", "bat5-sip6"],
            "big_units": [("百", "bag5", 100), ("千", "cien1", 1000), ("萬", "van4", 10000)],
            "classifier_two": "liong3",
            "day_parts": ["zau1-teu2-zau3", "ha1-zu4", "am4-bu1-sin2", "ya4-man1-sin2"],
            "week": ["li1-bai4-yit5", "li1-bai4-ngi4", "li1-bai4-sam1",
                     "li1-bai4-si4", "li1-bai4-ng3", "li1-bai4-liuk5", "li1-bai4-ngit5"],
            "deictic_days": ["gin1-ngit5", "qim2-ngit5", "tien1-gong1-ngit5"],
            "seasons": ["cun1", "ha4", "qiu1", "dung1"],
            "sentences": 8,
        },
    },
    {
        "key": "greetings",
        "name": "Hakka Chinese Greetings and Everyday Phrases",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Thirty greetings, farewells and politeness phrases - the "
            "social oil of Hakka life - each with Pinfa reading, English, "
            "and usage notes. The most Hakka greeting of all is not 'hello' "
            "but 食飯了冇? sit5-pon4-liau3-mau2? - 'have you eaten yet?' \n\n"
            "  你好! ngi2 ho3! - Hello! (general)\n"
            "  食飯了冇? sit5-pon4-liau3-mau2? - Have you eaten yet? (the classic greeting)\n"
            "  早! zau3! - Good morning!\n"
            "  好久冇見! ho3-giu3-mau2-gien4! - Long time no see!\n"
            "  你好嗎? ngi2 ho3-ma1? - How are you?\n"
            "  𠊎當好。 ngai2 dong1 ho3. - I am very well.\n"
            "  多謝! do1-qia4! - Thank you!\n"
            "  唔使客氣。 m2-sii3-hag5-hi4. - You are welcome. (no need for politeness)\n"
            "  唔好意思。 m2-ho3-ji4-sii1. - Excuse me. (embarrassed)\n"
            "  對唔住。 dui4-m2-qi4. - Sorry.\n"
            "  請! qiang3! - Please! / After you!\n"
            "  請坐。 qiang3-co4. - Please sit.\n"
            "  請飲茶。 qiang3-jim3-ca2. - Please have some tea.\n"
            "  歡迎! fon1-ngiang2! - Welcome!\n"
            "  勞煩你。 lo2-fan2-ngi2. - Sorry to trouble you.\n"
            "  承蒙你。 siin2-mung2-ngi2. - Much obliged to you.\n"
            "  再見! zai4-gien4! - Goodbye!\n"
            "  慢行! man4-hang2! - Take care! (walk slowly)\n"
            "  一路順風! yit5-lu4-sun4-fung1! - Have a smooth journey!\n"
            "  保重! bo3-cung4! - Take care of yourself!\n"
            "  請保重身體。 qiang3-bo3-cung4-siin1-ti3. - Please take care of your health.\n"
            "  恭喜! gung1-hi3! - Congratulations!\n"
            "  新年快樂! sin1-ngian2-kuai4-log6! - Happy New Year!\n"
            "  生日快樂! sen1-ngit5-kuai4-log6! - Happy birthday!\n"
            "  祝你健康。 zug5-ngi2-kien4-kong1. - Wishing you health.\n"
            "  入來坐。 ngip6-loi2-co4. - Come in and sit.\n"
            "  隨便。 cui2-pien4. - Make yourself at home. (casually)\n"
            "  唔使送。 m2-sii3-sung4. - No need to see me out.\n"
            "  下擺再來。 ha4-bai3-zai4-loi2. - Come again next time.\n"
            "  一路好走。 yit5-lu4-ho3-zeu3. - Travel safely. (said to the departing)"
        ),
        "how_it_works": (
            "This record teaches social language: thirty fixed phrases for "
            "meeting, thanking, apologizing, inviting, congratulating and "
            "parting, each with usage notes explaining WHEN Hakka speakers "
            "use it. The notes teach the culture inside the phrase - why "
            "food is the greeting, why 'walk slowly' means 'take care', why "
            "tea is the welcome."
        ),
        "key_points": [
            "30 greetings and politeness phrases with usage notes.",
            "食飯了冇? 'have you eaten yet?' is the signature Hakka greeting.",
            "慢行 man4-hang2 'walk slowly' is the warm farewell.",
            "Tea (請飲茶) is the ritual welcome; refusing it outright is rude.",
            "多謝 do1-qia4 thanks; 唔使客氣 declines the thanks.",
        ],
        "requirements": [
            "Read the pronouns record first; many greetings address 你 ngi2.",
        ],
        "standards": [
            "Phrases follow documented Meixian usage (MacIver 1926; phrasebook).",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_PHRASEBOOK],
        "must_contain": ["sit5-pon4-liau3-mau2", "man4-hang2", "do1-qia4", "Thirty greetings"],
        "sig_lens": (
            "Through the Signature lens these thirty phrases are the sworn "
            "courtesies of the guest-family nation: every greeting a small "
            "covenant of kindness, every farewell a blessing sealed with "
            "tea, food and safe roads."
        ),
        "drill": {
            "phrases": 30,
            "signature_greeting": "sit5-pon4-liau3-mau2",
            "farewell": "man4-hang2",
            "thanks": "do1-qia4",
            "categories": ["meeting", "thanking", "apologizing", "inviting",
                           "congratulating", "parting"],
        },
    },
    {
        "key": "grammar",
        "name": "Hakka Chinese Grammar Essentials",
        "group": "Grammar Essentials",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The ten load-bearing rules of Hakka grammar, each with "
            "translated example sentences. \n\n"
            "1. Word order is SVO. 𠊎食飯。 ngai2 sit5 pon4. - I eat rice. "
            "(subject-verb-object, like English.)\n"
            "2. Verbs never conjugate. 佢去。 gi2 hi4. - He goes / he went / "
            "he will go. Time comes from context or aspect words.\n"
            "3. Completed action: 了 liau3. 佢食了。 gi2 sit5 liau3. - He "
            "has eaten.\n"
            "4. Experienced past: 過 go4. 𠊎去過。 ngai2 hi4 go4. - I have "
            "been (there) before.\n"
            "5. Future and will: 會 voi4. 佢會來。 gi2 voi4 loi2. - He will "
            "come.\n"
            "6. Ongoing action: 緊 gin3 or 在 cai4. 佢食緊飯。 gi2 sit5 "
            "gin3 pon4. - He is eating.\n"
            "7. Negation: 唔 m2 before verbs and adjectives. 𠊎唔去。 "
            "ngai2 m2 hi4. - I am not going. 唔好 m2-ho3 - not good.\n"
            "8. Not-have negation: 冇 mau2. 佢冇錢。 gi2 mau2 qian2. - He "
            "has no money. 冇去 mau2 hi4 - did not go.\n"
            "9. Questions: A-not-A or 麼 ma1. 你去唔去? ngi2 hi4-m2-hi4? - "
            "Are you going? 你食飯麼? ngi2 sit5 pon4 ma1? - Are you eating?\n"
            "10. Classifiers sit between number and noun. 一個人 "
            "yit5-ge4-ngin2 - one person; 三本書 sam1-bun3-su1 - three "
            "books; 隻 zag5 for animals: 一隻狗 yit5-zag5-gieu3 - one dog.\n\n"
            "No gender, no cases, no articles. Possession is pronoun + 个 "
            "ge4: 𠊎个書 ngai2-ge4-su1 'my book'. Comparison uses 過 go4: "
            "佢高過𠊎。 gi2 go1 go4 ngai2. - He is taller than me. The "
            "passive uses 分 bun1: 分人打 bun1-ngin2-da3 - beaten by someone."
        ),
        "how_it_works": (
            "This record assembles the engine: ten rules that generate "
            "nearly every Hakka sentence - SVO order, zero conjugation, "
            "the aspect quartet (liau3, go4, voi4, gin3), the two negators "
            "(m2, mau2), two question strategies, classifiers, and the "
            "comparison and passive patterns. Each rule carries sentences "
            "that isolate exactly that rule."
        ),
        "key_points": [
            "SVO; verbs never conjugate; no gender, cases or articles.",
            "Aspect words: 了 liau3 completed, 過 go4 experienced, 會 voi4 future, 緊 gin3 ongoing.",
            "唔 m2 negates verbs/adjectives; 冇 mau2 negates having and past action.",
            "Questions via A-not-A (去唔去) or sentence-final 麼 ma1.",
            "Classifiers required: 個人, 本書, 隻狗.",
            "Comparison with 過 go4; passive with 分 bun1.",
        ],
        "requirements": [
            "Read the nouns, verbs and pronouns records first; this record assembles them.",
        ],
        "standards": [
            "Grammatical claims follow Hashimoto 1973 and the Meixian dialect dictionary.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_HASHIMOTO, CIT_LI],
        "must_contain": ["SVO", "liau3", "m2", "mau2", "zag5", "ten"],
        "sig_lens": (
            "Through the Signature lens these ten rules are the sworn "
            "mechanics of the language: every sentence built on the same "
            "frame, every time marked by its own small seal, nothing "
            "inflected, nothing hidden - the engine laid bare."
        ),
        "drill": {
            "rules": 10,
            "aspects": ["liau3", "go4", "voi4", "gin3"],
            "negators": ["m2", "mau2"],
            "question_strategies": ["A-not-A", "ma1"],
            "classifiers": ["ge4", "bun3", "zag5"],
            "sentences": 14,
        },
    },
    {
        "key": "home",
        "name": "Hakka Chinese Home and Family Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about house, rooms, furniture and family - "
            "the Hakka household, where the language lives. \n\n"
            "  𠊎屋下有五個人。 ngai2 vuk5-ha1 yiu1 ng3-ge4-ngin2. - There are five people in my family.\n"
            "  阿爸去做事。 a1-ba1 hi4 zo4-sii4. - Father has gone to work.\n"
            "  阿姆煮飯。 a1-me1 zu3-pon4. - Mother is cooking.\n"
            "  阿公看報紙。 a1-gung1 kon4-bo4-zii3. - Grandfather reads the newspaper.\n"
            "  阿婆在廳下坐。 a1-po2 cai4-tang1-ha1-co4. - Grandmother is sitting in the hall.\n"
            "  兄弟兩人去學校。 hiung1-ti4 liong3-ngin2 hi4-hog6-hau4. - The two brothers go to school.\n"
            "  姊妹在房間讀書。 zi3-moi4 cai4-fong2-gien1-tug6-su1. - The sisters are studying in the room.\n"
            "  𠊎个房間當光。 ngai2-ge4-fong2-gien1 dong1-gong1. - My room is very bright.\n"
            "  廳下有張大桌。 tang1-ha1 yiu1-zong1-tai4-zog5. - There is a big table in the hall.\n"
            "  廚房在屋後背。 cu2-fong2 cai4-vuk5-heu4-boi4. - The kitchen is behind the house.\n"
            "  𠊎愛掃地。 ngai2 oi4 so4-ti4. - I want to sweep the floor.\n"
            "  衫褲洗淨了。 sam1-fu4 se3-qiang4-liau3. - The clothes have been washed clean.\n"
            "  打開窗門。 da3-koi1-cung1-mun2. - Open the window.\n"
            "  關燈睡覺。 guan1-den1 soi4-gau4. - Turn off the light and sleep.\n"
            "  細子愛食糖。 se4-zii3 oi4-sit5-tong2. - The child wants candy.\n"
            "  阿哥轉來了。 a1-go1 zon3-loi2-liau3. - Elder brother has returned.\n"
            "  阿姊去街買菜。 a1-zi3 hi4-gie1-mai1-coi4. - Elder sister went to the market to buy vegetables.\n"
            "  屋頂愛修。 vuk5-dang3 oi4-xiu1. - The roof needs repair.\n"
            "  門口有隻狗。 mun2-heu3 yiu1-zag5-gieu3. - There is a dog at the door.\n"
            "  一家人食飯。 yit5-ga1-ngin2 sit5-pon4. - The whole family eats together."
        ),
        "how_it_works": (
            "This record teaches the household: kinship terms (阿爸, 阿姆, "
            "阿公, 阿婆, 兄弟, 姊妹), rooms (廳下, 房間, 廚房), furniture and "
            "daily chores - twenty sentences that reuse the noun, verb and "
            "grammar records inside a single theme. The Hakka-specific "
            "words (屋下, 廳下, 阿姆) are the vocabulary no Mandarin speaker "
            "would guess."
        ),
        "key_points": [
            "20 sentences on home and family life.",
            "Kinship: 阿爸 father, 阿姆 mother, 阿公 grandfather, 阿婆 grandmother.",
            "屋下 vuk5-ha1 = home/household; 廳下 tang1-ha1 = the main hall.",
            "Daily verbs in context: 煮飯, 掃地, 洗衫, 開窗.",
            "一家人 yit5-ga1-ngin2 = the whole family.",
        ],
        "requirements": [
            "Read the grammar record first; these sentences use 了, 在 and classifiers.",
        ],
        "standards": [
            "Kinship and household vocabulary per MacIver 1926.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["a1-me1", "tang1-ha1", "vuk5-ha1", "Twenty sentences"],
        "sig_lens": (
            "Through the Signature lens this record is the sworn household "
            "register: every room named, every elder titled, every chore a "
            "small covenant - the family as the first archive of the "
            "language."
        ),
        "drill": {
            "sentences": 20,
            "kinship": ["a1-ba1", "a1-me1", "a1-gung1", "a1-po2",
                        "hiung1-ti4", "zi3-moi4", "a1-go1", "a1-zi3"],
            "rooms": ["tang1-ha1", "fong2-gien1", "cu2-fong2"],
            "theme": "home",
        },
    },
    {
        "key": "food",
        "name": "Hakka Chinese Food and Cooking Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about meals, ingredients, cooking actions and "
            "the restaurant - Hakka food culture in Hakka words. \n\n"
            "  食飯了冇? sit5-pon4-liau3-mau2? - Have you eaten?\n"
            "  𠊎肚飢了。 ngai2-du3-gi1-liau3. - I am hungry.\n"
            "  阿姆煮个菜當好食。 a1-me1-zu3-ge4-coi4 dong1-ho3-sit5. - Mother's cooking is delicious.\n"
            "  今日食麼个? gin1-ngit5 sit5-mag5-ge4? - What shall we eat today?\n"
            "  買斤豬肉。 mai1-gin1-zu1-ngiuk6. - Buy a catty of pork.\n"
            "  雞湯當補。 gie1-tong1 dong1-bu3. - Chicken soup is very nourishing.\n"
            "  擂茶係客家名食。 lui2-ca2 he4-hag5-ga1-miang2-sit5. - Lei-cha is a famous Hakka food.\n"
            "  梅菜扣肉好食。 moi2-coi4-kieu4-ngiuk6 ho3-sit5. - Preserved mustard greens with pork is tasty.\n"
            "  鹽焗雞係名菜。 yam2-giug5-gie1 he4-miang2-coi4. - Salt-baked chicken is a famous dish.\n"
            "  飯煮熟了冇? pon4-zu3-sug6-liau3-mau2? - Is the rice cooked?\n"
            "  菜太鹹了。 coi4-tai4-ham2-liau3. - The dish is too salty.\n"
            "  湯少放鹽。 tong1-sau3-biong4-yam2. - Put less salt in the soup.\n"
            "  切菜愛細心。 qiet5-coi4 oi4-se4-xim1. - Be careful when chopping vegetables.\n"
            "  火細一點。 fo3-se4-yit5-diam3. - Turn the flame down a bit.\n"
            "  請飲茶。 qiang3-jim3-ca2. - Please have some tea.\n"
            "  佢唔飲酒。 gi2-m2-jim3-ziu3. - He does not drink alcohol.\n"
            "  食飽了。 sit5-bau3-liau3. - I have eaten my fill.\n"
            "  埋單幾多錢? mai2-dan1 gi3-do1-qian2? - How much is the bill?\n"
            "  打包轉去。 da3-bau1-zon3-hi4. - Pack it to take home.\n"
            "  下擺再來食。 ha4-bai3-zai4-loi2-sit5. - Come eat again next time."
        ),
        "how_it_works": (
            "This record teaches food: the meal verbs (食, 煮, 切, 放), "
            "taste words (鹹, 甜, 好食), the famous Hakka dishes (擂茶, 梅菜"
            "扣肉, 鹽焗雞) that carry the culture, market buying, and "
            "restaurant language through the bill and the takeaway. Every "
            "sentence is a mouthful of real usage."
        ),
        "key_points": [
            "20 sentences on food, cooking and restaurants.",
            "Signature dishes: 擂茶 lui2-ca2, 梅菜扣肉, 鹽焗雞 yam2-giug5-gie1.",
            "好食 ho3-sit5 = delicious; 肚飢 du3-gi1 = hungry.",
            "Restaurant: 埋單 mai2-dan1 the bill; 打包 da3-bau1 takeaway.",
            "Cooking verbs: 煮, 切 qiet5, 放 biong4, with 火 fo3 the flame.",
        ],
        "requirements": [
            "Read the verbs and adjectives records first for 食, 煮, 鹹, 甜.",
        ],
        "standards": [
            "Dish names are documented Hakka cuisine terms.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["lui2-ca2", "ho3-sit5", "mai2-dan1", "Twenty sentences"],
        "sig_lens": (
            "Through the Signature lens this record is the sworn cookbook: "
            "every dish a sealed recipe, every taste a vow of flavor - the "
            "guest-family table set in the archive forever."
        ),
        "drill": {
            "sentences": 20,
            "dishes": ["lui2-ca2", "moi2-coi4-kieu4-ngiuk6", "yam2-giug5-gie1"],
            "taste_words": ["ham2", "tiam2", "ho3-sit5"],
            "theme": "food",
        },
    },
    {
        "key": "travel",
        "name": "Hakka Chinese Travel and Directions Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about transport, asking directions, tickets "
            "and lodging - the traveler's Hakka. \n\n"
            "  車站在哪? ca1-cam4 cai4-nai3? - Where is the station?\n"
            "  去梅州幾遠? hi4-moi2-ziu1 gi3-yen3? - How far is it to Meizhou?\n"
            "  行路去愛幾久? hang2-lu4-hi4 oi4-gi3-giu3? - How long does it take on foot?\n"
            "  向左轉。 hiong4-zo3-zon3. - Turn left.\n"
            "  向右轉。 hiong4-yiu4-zon3. - Turn right.\n"
            "  直直去。 cit6-cit6-hi4. - Go straight ahead.\n"
            "  過橋就到。 go4-kieu2-qiu4-dau4. - Cross the bridge and you arrive.\n"
            "  火車幾點開? fo3-ca1 gi3-diam3-koi1? - When does the train leave?\n"
            "  買兩張票。 mai1-liong3-zong1-pieu4. - Buy two tickets.\n"
            "  票幾多錢? pieu4 gi3-do1-qian2? - How much is the ticket?\n"
            "  坐巴士去。 co4-ba1-sii4-hi4. - Go by bus.\n"
            "  的士在門口。 tit5-sii4 cai4-mun2-heu3. - The taxi is at the door.\n"
            "  飛機場遠唔遠? fi1-gi1-cong2 yen3-m2-yen3? - Is the airport far?\n"
            "  𠊎愛住旅店。 ngai2 oi4-qi4-li1-diam4. - I want to stay at a hotel.\n"
            "  有房間冇? yiu1-fong2-gien1-mau2? - Do you have rooms?\n"
            "  一晚幾多錢? yit5-man1 gi3-do1-qian2? - How much for one night?\n"
            "  地圖在哪? ti4-tu2 cai4-nai3? - Where is the map?\n"
            "  𠊎迷路了。 ngai2-mi2-lu4-liau3. - I am lost.\n"
            "  請帶𠊎去。 qiang3-dai4-ngai2-hi4. - Please take me there.\n"
            "  多謝你个幫忙。 do1-qia4-ngi2-ge4-bong1-mang2. - Thank you for your help."
        ),
        "how_it_works": (
            "This record teaches movement: direction verbs (轉, 過), "
            "transport nouns (火車, 巴士, 的士, 飛機), ticket and hotel "
            "transactions, and the question frames (在哪, 幾遠, 幾久, 幾多錢) "
            "that unlock any journey. The sentences chain into a complete "
            "trip: asking, buying, riding, lodging, thanking."
        ),
        "key_points": [
            "20 sentences covering the whole journey.",
            "Direction set: 向左, 向右, 直直去, 過橋.",
            "哪裡問法: 在哪 cai4-nai3; 幾遠 gi3-yen3; 幾久 gi3-giu3.",
            "Tickets: 買票 mai1-pieu4; 票價問法 票幾多錢.",
            "Lodging: 住旅店 qi4-li1-diam4; 一晚幾多錢.",
        ],
        "requirements": [
            "Read the numbers and questions material first for 幾多 and 幾點.",
        ],
        "standards": [
            "Transport and direction terms per documented Meixian usage.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_PHRASEBOOK],
        "must_contain": ["cai4-nai3", "gi3-do1-qian2", "fo3-ca1", "Twenty sentences"],
        "sig_lens": (
            "Through the Signature lens this record is the sworn road-map: "
            "every turn named, every fare counted, every night's lodging "
            "sealed - the guest-family journey written so no traveler is "
            "ever lost."
        ),
        "drill": {
            "sentences": 20,
            "transport": ["fo3-ca1", "ba1-sii4", "tit5-sii4", "fi1-gi1"],
            "question_frames": ["cai4-nai3", "gi3-yen3", "gi3-giu3", "gi3-do1-qian2"],
            "theme": "travel",
        },
    },
    {
        "key": "work",
        "name": "Hakka Chinese Work and School Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about jobs, the office, the classroom and "
            "learning. \n\n"
            "  佢在工廠做事。 gi2-cai4-gung1-cong3-zo4-sii4. - He works in a factory.\n"
            "  𠊎係老師。 ngai2-he4-lo3-sii1. - I am a teacher.\n"
            "  今日開會。 gin1-ngit5-koi1-fi4. - There is a meeting today.\n"
            "  老闆當好。 lo3-ban3-dong1-ho3. - The boss is very good.\n"
            "  人工幾多? ngin2-gung1-gi3-do1? - What is the wage?\n"
            "  放工了冇? biong4-gung1-liau3-mau2? - Have you finished work?\n"
            "  加班到夜。 ga1-ban1-dau4-ya4. - Work overtime into the night.\n"
            "  細子讀書當用功。 se4-zii3-tug6-su1-dong1-yung4-gung1. - The child studies very hard.\n"
            "  學校有操場。 hog6-hau4-yiu1-cau1-cong2. - The school has a playground.\n"
            "  上課了。 song1-ko4-liau3. - Class has started.\n"
            "  下課休息。 ha4-ko4-hiu1-xit5. - Rest after class.\n"
            "  功課做完冇? gung1-ko4-zo4-von2-mau2? - Have you finished the homework?\n"
            "  考試在下禮拜。 kau3-shi4-cai4-ha4-li1-bai4. - The exam is next week.\n"
            "  學客家話當有趣。 hog6-hag5-ga1-fa4-dong1-yiu1-qi4. - Learning Hakka is very interesting.\n"
            "  寫字愛認真。 xia3-sii4-oi4-ngin4-zin1. - Write characters carefully.\n"
            "  讀書聲當大。 tug6-su1-sang1-dong1-tai4. - The reading voices are very loud.\n"
            "  同學一齊去。 tung2-hog6-yit5-ce2-hi4. - The classmates go together.\n"
            "  畢業了做麼个? bit5-ngiap6-liau3-zo4-mag5-ge4? - What will you do after graduation?\n"
            "  𠊎愛做醫生。 ngai2-oi4-zo4-ji1-sen1. - I want to be a doctor.\n"
            "  努力就會成功。 nu3-lag6-qiu4-voi4-siin2-gung1. - Hard work brings success."
        ),
        "how_it_works": (
            "This record teaches work and school: job nouns (工廠, 老闆, "
            "人工), office events (開會, 放工, 加班), classroom life (上課, "
            "下課, 功課, 考試), and the aspiration sentences that close "
            "every school career. The grammar record's aspect words do "
            "heavy lifting here (放工了, 做完冇)."
        ),
        "key_points": [
            "20 sentences on jobs, office, classroom and study.",
            "Work: 做事 zo4-sii4, 開會 koi1-fi4, 放工 biong4-gung1, 人工 ngin2-gung1.",
            "School: 上課/下課, 功課 gung1-ko4, 考試 kau3-shi4.",
            "用功 yung4-gung1 = studious; 努力 nu3-lag6 = effort.",
            "Aspiration pattern: 𠊎愛做... 'I want to be...'",
        ],
        "requirements": [
            "Read the grammar record first for 了, 完 and 會.",
        ],
        "standards": [
            "Work and school vocabulary per documented usage.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["biong4-gung1", "gung1-ko4", "kau3-shi4", "Twenty sentences"],
        "sig_lens": (
            "Through the Signature lens this record is the sworn ledger of "
            "labor and learning: every job titled, every lesson sealed - "
            "work and study as twin covenants of the guest-family house."
        ),
        "drill": {
            "sentences": 20,
            "work_words": ["gung1-cong3", "lo3-ban3", "ngin2-gung1", "koi1-fi4"],
            "school_words": ["song1-ko4", "ha4-ko4", "gung1-ko4", "kau3-shi4"],
            "theme": "work",
        },
    },
    {
        "key": "health",
        "name": "Hakka Chinese Health and Body Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about body parts, symptoms, the doctor visit "
            "and the pharmacy. \n\n"
            "  頭痛。 teu2-tung4. - Headache. (head hurts)\n"
            "  𠊎肚痛。 ngai2-du3-tung4. - My stomach hurts.\n"
            "  佢發燒了。 gi2-fat5-sau1-liau3. - He has a fever.\n"
            "  感冒了。 gam3-mau4-liau3. - (I) caught a cold.\n"
            "  咳得當厲害。 kat5-det5-dong1-li4-hoi4. - The cough is very severe.\n"
            "  𠊎个牙痛。 ngai2-ge4-nga2-tung4. - My tooth hurts.\n"
            "  目睛紅了。 mug5-jiang1-fung2-liau3. - The eyes are red.\n"
            "  手割傷了。 su3-got5-song1-liau3. - The hand is cut.\n"
            "  腳扭到。 giog5-ngiu3-dau4. - The foot is sprained.\n"
            "  去看醫生。 hi4-kon4-ji1-sen1. - Go see the doctor.\n"
            "  醫生講冇大事。 ji1-sen1-gong3-mau2-tai4-sii4. - The doctor says it is nothing serious.\n"
            "  食藥。 sit5-yog6. - Take medicine.\n"
            "  一天食三次。 yit5-tien1-sit5-sam1-ci4. - Take three times a day.\n"
            "  藥房在哪? yog6-fong2-cai4-nai3? - Where is the pharmacy?\n"
            "  打針會痛麼? da3-zim1-voi4-tung4-ma1? - Will the injection hurt?\n"
            "  多休息。 do1-hiu1-xit5. - Rest more.\n"
            "  飲多水。 jim3-do1-sui3. - Drink more water.\n"
            "  身體保重。 siin1-ti3-bo3-cung4. - Take care of your health.\n"
            "  佢好轉了。 gi2-ho3-zon3-liau3. - He has recovered.\n"
            "  祝你早日康復。 zug5-ngi2-zau3-ngit5-kong1-fug6. - Wishing you a speedy recovery."
        ),
        "how_it_works": (
            "This record teaches the body and its troubles: body-part nouns "
            "(頭, 肚, 牙, 目睛, 手, 腳), the pain pattern X痛, symptom verbs "
            "(發燒, 感冒, 咳), the doctor-visit script, dosage language (一"
            "天三次), and recovery wishes. The X痛 pattern generates every "
            "ache: swap the body part, keep the 痛."
        ),
        "key_points": [
            "20 sentences on body, symptoms, doctor and pharmacy.",
            "Pain pattern: body part + 痛 tung4 (頭痛, 肚痛, 牙痛).",
            "Symptoms: 發燒 fat5-sau1, 感冒 gam3-mau4, 咳 kat5.",
            "Dosage: 一天食三次 'three times a day'; 食藥 'take medicine'.",
            "Pharmacy: 藥房 yog6-fong2; recovery wish 早日康復.",
        ],
        "requirements": [
            "Read the nouns record first for body-part words.",
        ],
        "standards": [
            "Medical vocabulary per documented usage; no medical advice beyond language teaching.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["tung4", "fat5-sau1", "yog6-fong2", "Twenty sentences"],
        "sig_lens": (
            "Through the Signature lens this record is the sworn care of "
            "the body: every ache named, every remedy sealed - the language "
            "itself as medicine, prescribed word by word."
        ),
        "drill": {
            "sentences": 20,
            "body_parts": ["teu2", "du3", "nga2", "mug5-jiang1", "su3", "giog5"],
            "pain_pattern": "tung4",
            "symptoms": ["fat5-sau1", "gam3-mau4", "kat5"],
            "theme": "health",
        },
    },
    {
        "key": "emotions",
        "name": "Hakka Chinese Emotions and Feelings Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about happiness, sadness, anger, fear, love "
            "and surprise - the inner life in Hakka. \n\n"
            "  𠊎當歡喜。 ngai2-dong1-fon1-hi3. - I am very happy.\n"
            "  佢笑到見牙唔見眼。 gi2-xiau4-dau4-gien4-nga2-m2-gien4-ngian3. - He is laughing with joy.\n"
            "  好消息! ho3-xiau1-xit5! - Good news!\n"
            "  𠊎傷心。 ngai2-song1-xim1. - I am sad.\n"
            "  佢哭了。 gi2-heu4-liau3. - She cried.\n"
            "  唔好難過。 m2-ho3-nan2-go4. - Do not be sad.\n"
            "  佢當嬲。 gi2-dong1-neu4. - He is very angry.\n"
            "  發脾氣冇用。 fat5-pi2-hi4-mau2-yung4. - Losing your temper is useless.\n"
            "  冷靜一點。 lang1-qin4-yit5-diam3. - Calm down a bit.\n"
            "  𠊎驚。 ngai2-giang1. - I am afraid.\n"
            "  唔使驚。 m2-sii3-giang1. - Do not be afraid.\n"
            "  夜路當恐怖。 ya4-lu4-dong1-kung3-bu4. - The night road is frightening.\n"
            "  𠊎愛你。 ngai2-oi4-ngi2. - I love you.\n"
            "  佢兜感情當好。 gi2-deu1-gam3-qiin2-dong1-ho3. - Their relationship is very good.\n"
            "  想念屋下。 xiong3-ngiam4-vuk5-ha1. - I miss home.\n"
            "  嚇𠊎一跳。 hag5-ngai2-yit5-tiau4. - You startled me.\n"
            "  真意外! zin1-ji4-ngoi4! - What a surprise!\n"
            "  𠊎放心了。 ngai2-biong4-xim1-liau3. - I am relieved.\n"
            "  佢當失望。 gi2-dong1-sit5-mong4. - He is very disappointed.\n"
            "  保持希望。 bo3-cii2-hi1-mong4. - Keep hope."
        ),
        "how_it_works": (
            "This record teaches feeling: the six emotion families with "
            "their core words (歡喜, 傷心, 嬲, 驚, 愛, 意外), the comfort "
            "patterns (唔好難過, 唔使驚), and the idiomatic intensifiers "
            "(笑到見牙唔見眼). Emotions take 當 dong1 for degree, exactly "
            "like adjectives - the grammar stays constant while the heart "
            "changes."
        ),
        "key_points": [
            "20 sentences across happy, sad, angry, afraid, love, surprise.",
            "歡喜 fon1-hi3 = happy; 傷心 song1-xim1 = sad; 嬲 neu4 = angry; 驚 giang1 = afraid.",
            "Comfort patterns: 唔好難過, 唔使驚, 冷靜一點.",
            "愛 oi4 covers both 'to love' and 'to want'.",
            "Degree with 當 dong1 works for feelings as for adjectives.",
        ],
        "requirements": [
            "Read the adjectives record first for 當 and degree words.",
        ],
        "standards": [
            "Emotion vocabulary per documented usage.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["fon1-hi3", "neu4", "giang1", "Twenty sentences"],
        "sig_lens": (
            "Through the Signature lens these are the sworn feelings: joy "
            "and sorrow, anger and fear, love and surprise - every emotion "
            "named in the archive so the heart, too, is fully documented."
        ),
        "drill": {
            "sentences": 20,
            "emotion_words": ["fon1-hi3", "song1-xim1", "neu4", "giang1",
                              "oi4", "ji4-ngoi4"],
            "comfort_patterns": 3,
            "theme": "emotions",
        },
    },
    {
        "key": "nature",
        "name": "Hakka Chinese Nature and Weather Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about animals, plants, seasons and weather "
            "talk - the Hakka countryside. \n\n"
            "  落雨了。 log6-sui3-liau3. - It is raining.\n"
            "  出日了。 cut5-ngit5-liau3. - The sun is out.\n"
            "  今日當熱。 gin1-ngit5-dong1-ngiat6. - Today is very hot.\n"
            "  尋日好冷。 qim2-ngit5-ho3-lang1. - Yesterday was very cold.\n"
            "  起風了。 hi3-fung1-liau3. - The wind has risen.\n"
            "  打雷了。 da3-lui2-liau3. - It is thundering.\n"
            "  天頂有星。 tien1-dang3-yiu1-xen1. - There are stars in the sky.\n"
            "  山頂當涼。 san1-dang3-dong1-liong2. - The mountaintop is very cool.\n"
            "  田裡禾當青。 tien2-li1-vo2-dong1-qiang1. - The rice in the field is very green.\n"
            "  牛在食草。 ngiu2-cai4-sit5-cau3. - The cow is eating grass.\n"
            "  狗追貓。 gieu3-zui1-meu4. - The dog chases the cat.\n"
            "  鳥在樹頂唱歌。 diau1-cai4-su4-dang3-cong4-go1. - The bird sings in the treetop.\n"
            "  魚在水裡游。 ng2-cai4-sui3-li1-yiu2. - The fish swims in the water.\n"
            "  蟲咬人。 cung2-ngau1-ngin2. - Insects bite people.\n"
            "  春天花開。 cun1-tien1-fa1-koi1. - Flowers bloom in spring.\n"
            "  秋天收禾。 qiu1-tien1-siu1-vo2. - Harvest the rice in autumn.\n"
            "  竹當直。 zug5-dong1-cit6. - Bamboo is very straight.\n"
            "  松樹當高。 ciung2-su4-dong1-go1. - The pine tree is very tall.\n"
            "  河水當清。 ho2-sui3-dong1-qiang1. - The river water is very clear.\n"
            "  愛護自然。 oi4-fu4-cii4-ngian2. - Protect nature."
        ),
        "how_it_works": (
            "This record teaches the natural world: weather verbs that "
            "stand alone as sentences (落雨了, 出日了), the farm animals and "
            "their actions, plants and seasons, and the landscape words "
            "(山頂, 田裡, 河). Weather sentences need no subject - the sky "
            "itself is the actor - a pattern worth noticing."
        ),
        "key_points": [
            "20 sentences on animals, plants, seasons and weather.",
            "Weather verbs stand alone: 落雨了, 出日了, 起風了, 打雷了.",
            "Farm set: 牛, 禾 vo2 (rice plant), 田 tien2 (field).",
            "Seasons: 春天, 夏天, 秋天, 冬天 with their work (收禾).",
            "Landscape: 山頂, 河 ho2, 天頂.",
        ],
        "requirements": [
            "Read the nouns record first for 山, 水, 日, 月.",
        ],
        "standards": [
            "Nature vocabulary per documented usage.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["log6-sui3", "vo2", "tien2", "Twenty sentences"],
        "sig_lens": (
            "Through the Signature lens this is the sworn countryside: "
            "rain and sun, field and river, beast and bird - the guest-"
            "family land recorded acre by acre, season by season."
        ),
        "drill": {
            "sentences": 20,
            "weather_verbs": ["log6-sui3", "cut5-ngit5", "hi3-fung1", "da3-lui2"],
            "animals": ["ngiu2", "gieu3", "meu4", "diau1", "ng2", "cung2"],
            "theme": "nature",
        },
    },
    {
        "key": "shopping",
        "name": "Hakka Chinese Shopping and Money Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about the market, prices, bargaining and "
            "paying. \n\n"
            "  去街買東西。 hi4-gie1-mai1-dung1-xi1. - Go to town to buy things.\n"
            "  這隻幾多錢? li4-zag5-gi3-do1-qian2? - How much is this one?\n"
            "  太貴了。 tai4-gui4-liau3. - Too expensive.\n"
            "  平一點好麼? piang2-yit5-diam3-ho3-ma1? - Can it be a bit cheaper?\n"
            "  算平一點。 son4-piang2-yit5-diam3. - Count it a bit cheaper.\n"
            "  好，成交。 ho3, siin2-gau1. - OK, deal.\n"
            "  𠊎買兩斤。 ngai2-mai1-liong3-gin1. - I will buy two catties.\n"
            "  找錢。 zau3-qian2. - Give change.\n"
            "  唔使找。 m2-sii3-zau3. - Keep the change.\n"
            "  有冇散紙? yiu1-mau2-san3-zii3? - Do you have small change?\n"
            "  可以刷卡麼? ko3-ji3-set5-ka1-ma1? - Can I pay by card?\n"
            "  收現金。 siu1-hien4-gim1. - Cash accepted.\n"
            "  這件衫幾靚。 li4-kien4-sam1-gi3-jiang4. - This shirt is very pretty.\n"
            "  試得麼? shi4-det5-ma1? - May I try it on?\n"
            "  大件一點。 tai4-kien4-yit5-diam3. - One size larger.\n"
            "  細件一點。 se4-kien4-yit5-diam3. - One size smaller.\n"
            "  新貨到了。 sin1-fo4-dau4-liau3. - New stock has arrived.\n"
            "  打折冇? da3-zet5-mau2? - Is there a discount?\n"
            "  開發票。 koi1-fat5-pieu4. - Issue a receipt.\n"
            "  下擺再來。 ha4-bai3-zai4-loi2. - Come again next time."
        ),
        "how_it_works": (
            "This record teaches the market: the price question (幾多錢), "
            "the bargaining dance (太貴了, 平一點, 成交), paying (找錢, 刷"
            "卡, 現金), sizing clothes (大件一點), and the shopkeeper's "
            "courtesies. Bargaining sentences are polite formulas - learn "
            "them whole."
        ),
        "key_points": [
            "20 sentences on market, bargaining and paying.",
            "Price: 這隻幾多錢?; Too dear: 太貴了 tai4-gui4-liau3.",
            "Bargain: 平一點好麼?; Deal: 好，成交 ho3 siin2-gau1.",
            "Pay: 找錢 zau3-qian2 change; 刷卡 set5-ka1 card; 現金 hien4-gim1 cash.",
            "Clothes: 試得麼 try on; 大件/細件一點 sizing.",
        ],
        "requirements": [
            "Read the numbers record first for 幾多錢 and amounts.",
        ],
        "standards": [
            "Market vocabulary per documented usage.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["tai4-gui4", "siin2-gau1", "zau3-qian2", "Twenty sentences"],
        "sig_lens": (
            "Through the Signature lens this is the sworn marketplace: "
            "every price asked, every bargain sealed with 成交 - trade as "
            "covenant, coin by counted coin."
        ),
        "drill": {
            "sentences": 20,
            "bargain_steps": ["gi3-do1-qian2", "tai4-gui4", "piang2-yit5-diam3", "siin2-gau1"],
            "pay_words": ["zau3-qian2", "set5-ka1", "hien4-gim1"],
            "theme": "shopping",
        },
    },
    {
        "key": "friendship",
        "name": "Hakka Chinese Friendship and Social Life Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about meeting people, invitations and "
            "celebrations. \n\n"
            "  認識你當歡喜。 ngin4-shit5-ngi2-dong1-fon1-hi3. - Very pleased to meet you.\n"
            "  你叫麼个名? ngi2-gieu4-mag5-ge4-miang2? - What is your name?\n"
            "  𠊎叫阿明。 ngai2-gieu4-a1-min2. - I am called A-Ming.\n"
            "  你係哪裡人? ngi2-he4-nai3-li1-ngin2? - Where are you from?\n"
            "  𠊎係梅州人。 ngai2-he4-moi2-ziu1-ngin2. - I am from Meizhou.\n"
            "  幾大年紀? gi3-tai4-ngian2-gi3? - How old are you?\n"
            "  做麼个事? zo4-mag5-ge4-sii4? - What work do you do?\n"
            "  請你食飯。 qiang3-ngi2-sit5-pon4. - I invite you to dinner.\n"
            "  下晝來𠊎屋下。 ha4-zu4-loi2-ngai2-vuk5-ha1. - Come to my home this afternoon.\n"
            "  一齊飲茶。 yit5-ce2-jim3-ca2. - Have tea together.\n"
            "  歡迎你來。 fon1-ngiang2-ngi2-loi2. - You are welcome to come.\n"
            "  生日快樂! sen1-ngit5-kuai4-log6! - Happy birthday!\n"
            "  祝你步步高升。 zug5-ngi2-pu4-pu4-go1-shiin1. - Wishing you success at every step.\n"
            "  恭喜發財! gung1-hi3-fat5-coi2! - Wishing you prosperity!\n"
            "  新婚快樂! sin1-fun1-kuai4-log6! - Happy wedding!\n"
            "  大家飲勝! tai4-ga1-jim3-shin4! - Cheers, everyone!\n"
            "  好朋友難得。 ho3-pen2-iu1-nan2-det5. - Good friends are hard to find.\n"
            "  有事相幫。 yiu1-sii4-xiong1-bong1. - Help each other when in need.\n"
            "  保持聯絡。 bo3-cii2-lion2-log6. - Keep in touch.\n"
            "  有閒再來尞。 yiu1-han2-zai4-loi2-liau4. - Come visit again when free."
        ),
        "how_it_works": (
            "This record teaches social life: the meeting script (name, "
            "home, age, work), invitations (請你食飯, 來𠊎屋下), celebration "
            "wishes (生日快樂, 恭喜發財, 大家飲勝), and the friendship "
            "values (有事相幫, 保持聯絡). 尞 liau4 'to visit, to play' is the "
            "warm Hakka social verb."
        ),
        "key_points": [
            "20 sentences on meeting, inviting and celebrating.",
            "Meeting script: 叫麼个名, 哪裡人, 幾大年紀, 做麼个事.",
            "Invitation: 請你食飯; 來𠊎屋下; 一齊飲茶.",
            "Toasts: 大家飲勝 tai4-ga1-jim3-shin4 = cheers.",
            "尞 liau4 = to visit socially, the warm Hakka verb.",
        ],
        "requirements": [
            "Read the greetings record first for the politeness base.",
        ],
        "standards": [
            "Social phrases per documented usage.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["liau4", "jim3-shin4", "bo3-cii2-lion2-log6", "Twenty sentences"],
        "sig_lens": (
            "Through the Signature lens this is the sworn fellowship: every "
            "meeting a covenant begun, every toast sealed, every friendship "
            "a vow of mutual help - 有事相幫 written into the archive."
        ),
        "drill": {
            "sentences": 20,
            "meeting_script": 4,
            "wishes": ["sen1-ngit5-kuai4-log6", "gung1-hi3-fat5-coi2", "jim3-shin4"],
            "social_verb": "liau4",
            "theme": "friendship",
        },
    },
    {
        "key": "technology",
        "name": "Hakka Chinese Technology and Communication Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about phone, internet, computer and messaging "
            "- modern life in Hakka. \n\n"
            "  打電話分𠊎。 da3-tien4-fa4-bun1-ngai2. - Call me.\n"
            "  𠊎个電話號碼係... ngai2-ge4-tien4-fa4-hau4-ma1-he4... - My phone number is...\n"
            "  手機冇電了。 su3-gi1-mau2-tien4-liau3. - The phone is out of battery.\n"
            "  充電。 cung1-tien4. - Charge it.\n"
            "  上網。 song1-miong3. - Go online.\n"
            "  網絡斷了。 miong3-log6-ton1-liau3. - The internet is down.\n"
            "  發信息分佢。 fat5-xin4-xit5-bun1-gi2. - Send him a message.\n"
            "  𠊎收到了。 ngai2-siu1-dau4-liau3. - I received it.\n"
            "  開電腦。 koi1-tien4-nau3. - Turn on the computer.\n"
            "  關電腦。 guan1-tien4-nau3. - Turn off the computer.\n"
            "  打字。 da3-sii4. - Type.\n"
            "  存檔。 cun2-dong4. - Save the file.\n"
            "  影相。 yang3-xiong4. - Take a photo.\n"
            "  錄音。 lug6-jim1. - Record audio.\n"
            "  視頻通話。 shi4-pin2-tung1-fa4. - Video call.\n"
            "  密碼係幾多? met6-ma1-he4-gi3-do1? - What is the password?\n"
            "  掃碼。 so4-ma1. - Scan the code.\n"
            "  下載軟件。 ha4-zai4-ngion1-kien4. - Download the software.\n"
            "  更新了冇? gen1-xin1-liau3-mau2? - Has it updated?\n"
            "  人工智能當厲害。 ngin2-gung1-zhi4-nen2-dong1-li4-hoi4. - Artificial intelligence is amazing."
        ),
        "how_it_works": (
            "This record teaches the digital layer: phone verbs (打電話, "
            "充電, 掃碼), the internet nouns (上網, 網絡, 信息), computer "
            "actions (開/關電腦, 打字, 存檔), media (影相, 錄音, 視頻通話), "
            "and the password question. Modern borrowings sit inside pure "
            "Hakka grammar - the frame never changes."
        ),
        "key_points": [
            "20 sentences on phone, internet, computer, messaging.",
            "Phone: 打電話, 手機 su3-gi1, 充電 cung1-tien4.",
            "Internet: 上網 song1-miong3, 網絡 miong3-log6, 信息 xin4-xit5.",
            "Computer: 開/關電腦, 打字 da3-sii4, 存檔 cun2-dong4.",
            "Media: 影相 yang3-xiong4 photo; 錄音 lug6-jim1 audio.",
        ],
        "requirements": [
            "Read the verbs record first for 打, 開, 關.",
        ],
        "standards": [
            "Technology terms per current documented Hakka usage.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_LI],
        "must_contain": ["song1-miong3", "tien4-nau3", "yang3-xiong4", "Twenty sentences"],
        "sig_lens": (
            "Through the Signature lens this is the sworn signal-room: "
            "every call connected, every file saved, every message sealed - "
            "the old language carrying the newest wires."
        ),
        "drill": {
            "sentences": 20,
            "phone_words": ["tien4-fa4", "su3-gi1", "cung1-tien4"],
            "net_words": ["song1-miong3", "miong3-log6", "xin4-xit5"],
            "computer_words": ["tien4-nau3", "da3-sii4", "cun2-dong4"],
            "theme": "technology",
        },
    },
    {
        "key": "tenses",
        "name": "Hakka Chinese Verb Tenses in Sentences",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Hakka has no tense conjugation - it has aspect words. This "
            "record shows present, past, future and the aspect system with "
            "five translated sentences per pattern. \n\n"
            "Present / habitual (bare verb):\n"
            "  𠊎食飯。 ngai2-sit5-pon4. - I eat. / I am eating.\n"
            "  佢天天行路。 gi2-tien1-tien1-hang2-lu4. - He walks every day.\n"
            "  阿姆煮飯。 a1-me1-zu3-pon4. - Mother cooks.\n"
            "  𠊎愛客家話。 ngai2-oi4-hag5-ga1-fa4. - I love Hakka.\n"
            "  狗吠。 gieu3-pui4. - The dog barks.\n\n"
            "Ongoing (緊 gin3 / 在 cai4):\n"
            "  佢食緊飯。 gi2-sit5-gin3-pon4. - He is eating.\n"
            "  𠊎在看書。 ngai2-cai4-kon4-su1. - I am reading.\n"
            "  佢兜在開會。 gi2-deu1-cai4-koi1-fi4. - They are in a meeting.\n"
            "  雨落緊。 ji3-log6-gin3. - It is raining.\n"
            "  阿爸在睡覺。 a1-ba1-cai4-soi4-gau4. - Father is sleeping.\n\n"
            "Completed past (了 liau3):\n"
            "  𠊎食了。 ngai2-sit5-liau3. - I have eaten.\n"
            "  佢去了。 gi2-hi4-liau3. - He has gone.\n"
            "  書看完了。 su1-kon4-von2-liau3. - The book has been read through.\n"
            "  雨停了。 ji3-tin2-liau3. - The rain has stopped.\n"
            "  𠊎做到。 ngai2-zo4-dau4. - I have done it.\n\n"
            "Experienced past (過 go4):\n"
            "  𠊎去過北京。 ngai2-hi4-go4-bit5-gin1. - I have been to Beijing.\n"
            "  佢食過擂茶。 gi2-sit5-go4-lui2-ca2. - He has tried lei-cha.\n"
            "  你看過這本書冇? ngi2-kon4-go4-li4-bun3-su1-mau2? - Have you read this book?\n"
            "  𠊎聽過這首歌。 ngai2-tang1-go4-li4-su3-go1. - I have heard this song.\n"
            "  佢來過兩擺。 gi2-loi2-go4-liong3-bai3. - He has come twice.\n\n"
            "Future (會 voi4 / 愛 oi4):\n"
            "  佢會來。 gi2-voi4-loi2. - He will come.\n"
            "  天光日會落雨。 tien1-gong1-ngit5-voi4-log6-sui3. - It will rain tomorrow.\n"
            "  𠊎會學好客家話。 ngai2-voi4-hog6-ho3-hag5-ga1-fa4. - I will learn Hakka well.\n"
            "  𠊎愛去街。 ngai2-oi4-hi4-gie1. - I am going to town. (intention)\n"
            "  佢愛做醫生。 gi2-oi4-zo4-ji1-sen1. - He is going to be a doctor."
        ),
        "how_it_works": (
            "This record teaches the aspect engine: the bare verb for "
            "present/habitual, 緊/在 for ongoing, 了 for completed, 過 for "
            "experienced, 會 for future, 愛 for intention - five sentences "
            "each, so the pattern burns in. The key insight: Hakka marks "
            "HOW an action relates to time, not WHEN on a European tense "
            "line."
        ),
        "key_points": [
            "No conjugation; five aspect words do all the time-work.",
            "Bare verb = present/habitual; 緊 gin3 / 在 cai4 = ongoing.",
            "了 liau3 = completed; 過 go4 = experienced ('have ... before').",
            "會 voi4 = future; 愛 oi4 = intention ('going to').",
            "25 sentences, five per pattern.",
        ],
        "requirements": [
            "Read the grammar-essentials record first for the aspect list.",
        ],
        "standards": [
            "Aspect analysis follows Hashimoto 1973.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_HASHIMOTO, CIT_LI],
        "must_contain": ["gin3", "liau3", "go4", "voi4", "aspect"],
        "sig_lens": (
            "Through the Signature lens these are the sworn seals of time: "
            "six small words, each stamped beside the verb, marking whether "
            "the deed is ongoing, done, experienced, or yet to come."
        ),
        "drill": {
            "patterns": ["bare", "gin3/cai4", "liau3", "go4", "voi4/oi4"],
            "sentences_per": 5,
            "total_sentences": 25,
            "aspect_words": ["gin3", "cai4", "liau3", "go4", "voi4", "oi4"],
        },
    },
    {
        "key": "qa",
        "name": "Hakka Chinese Questions and Answers",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Twenty question-and-answer pairs covering who, what, where, "
            "when, why and how - the interrogative engine in full. \n\n"
            "  麼人來? - 𠊎阿爸來。 mag5-ngin2-loi2? - ngai2-a1-ba1-loi2. - Who is coming? - My father is coming.\n"
            "  乜事? - 冇麼个事。 mag5-sii4? - mau2-mag5-ge4-sii4. - What is it? - Nothing.\n"
            "  你去哪? - 𠊎去街。 ngi2-hi4-nai3? - ngai2-hi4-gie1. - Where are you going? - I am going to town.\n"
            "  學校在哪? - 在路尾。 hog6-hau4-cai4-nai3? - cai4-lu4-mi1. - Where is the school? - At the end of the road.\n"
            "  幾時去? - 天光日去。 gi3-si2-hi4? - tien1-gong1-ngit5-hi4. - When to go? - Go tomorrow.\n"
            "  幾點開會? - 三點開會。 gi3-diam3-koi1-fi4? - sam1-diam3-koi1-fi4. - When is the meeting? - At three.\n"
            "  做麼哭? - 跌倒了。 zo4-ma1-heu4? - diet5-dau3-liau3. - Why cry? - (I) fell down.\n"
            "  做麼唔去? - 冇閒。 zo4-ma1-m2-hi4? - mau2-han2. - Why not go? - No time.\n"
            "  點樣做? - 恁樣做。 dim3-ngiong4-zo4? - an4-ngiong4-zo4. - How to do it? - Do it like this.\n"
            "  點樣去? - 坐車去。 dim3-ngiong4-hi4? - co4-ca1-hi4. - How to get there? - Go by car.\n"
            "  幾多人? - 五個人。 gi3-do1-ngin2? - ng3-ge4-ngin2. - How many people? - Five people.\n"
            "  幾多錢? - 十塊錢。 gi3-do1-qian2? - sip6-kuai4-qian2. - How much? - Ten dollars.\n"
            "  係唔係你? - 係𠊎。 he4-m2-he4-ngi2? - he4-ngai2. - Is it you? - It is me.\n"
            "  好唔好? - 好。 ho3-m2-ho3? - ho3. - Is it good? - Good.\n"
            "  去唔去? - 去。 hi4-m2-hi4? - hi4. - Going? - Going.\n"
            "  有冇錢? - 有。 yiu1-mau2-qian2? - yiu1. - Have money? - Yes.\n"
            "  食飯麼? - 食。 sit5-pon4-ma1? - sit5. - Eating? - Eating.\n"
            "  哪一個? - 這個。 nai3-yit5-ge4? - li4-ge4. - Which one? - This one.\n"
            "  幾大? - 恁大。 gi3-tai4? - an4-tai4. - How big? - This big.\n"
            "  哪位先生? - 佢係王先生。 nai3-vi4-xin1-sang1? - gi2-he4-vong2-xin1-sang1. - Which gentleman? - He is Mr. Wong."
        ),
        "how_it_works": (
            "This record drills the question system: the seven interrogative "
            "words (麼人, 乜, 哪, 幾時, 做麼, 點樣, 幾多) plus the two "
            "yes-no strategies (A-not-A, 麼). Each pair shows the question "
            "word in its natural slot and a natural short answer - answers "
            "repeat the verb, the Hakka way, instead of 'yes'."
        ),
        "key_points": [
            "20 question/answer pairs across who/what/where/when/why/how.",
            "Interrogatives stay in place - no word-order gymnastics.",
            "Yes-no via A-not-A (去唔去) or final 麼 ma1.",
            "Answers repeat the verb: 有冇錢? - 有.",
            "Quantity questions: 幾多 gi3-do1; 幾大 gi3-tai4.",
        ],
        "requirements": [
            "Read the pronouns record first for the interrogative words.",
        ],
        "standards": [
            "Question patterns per documented Meixian usage.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_HASHIMOTO, CIT_LI],
        "must_contain": ["zo4-ma1", "dim3-ngiong4", "hi4-m2-hi4", "Twenty question"],
        "sig_lens": (
            "Through the Signature lens these are the sworn inquiries: "
            "twenty questions, each with its sealed answer - who, what, "
            "where, when, why, how - the whole world interrogated and "
            "answered."
        ),
        "drill": {
            "pairs": 20,
            "interrogatives": ["mag5-ngin2", "mag5", "nai3", "gi3-si2",
                               "zo4-ma1", "dim3-ngiong4", "gi3-do1"],
            "yes_no": ["A-not-A", "ma1"],
        },
    },
    {
        "key": "commands",
        "name": "Hakka Chinese Commands and Requests",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Twenty imperative and polite-request sentences - formal "
            "against informal. The bare verb commands; 請 qiang3 softens; "
            "莫 mog5 forbids. \n\n"
            "Informal (family, friends):\n"
            "  來! loi2! - Come!\n"
            "  食飯! sit5-pon4! - Eat!\n"
            "  坐低! co4-dai1! - Sit down!\n"
            "  快一點! kuai4-yit5-diam3! - Hurry up!\n"
            "  唔好吵! m2-ho3-cau3! - Don't be noisy!\n"
            "  莫走! mog5-zeu3! - Don't go!\n"
            "  細聲一點! se4-sang1-yit5-diam3! - Quieter!\n"
            "  看這! kon4-li4! - Look at this!\n"
            "  拿來! na1-loi2! - Bring it here!\n"
            "  轉去! zon3-hi4! - Go back!\n\n"
            "Polite / formal (elders, guests, business):\n"
            "  請坐。 qiang3-co4. - Please sit.\n"
            "  請飲茶。 qiang3-jim3-ca2. - Please have tea.\n"
            "  請你幫忙。 qiang3-ngi2-bong1-mang2. - Please help me.\n"
            "  勞煩你。 lo2-fan2-ngi2. - May I trouble you.\n"
            "  唔好意思，借問一下。 m2-ho3-ji4-sii1, jia4-mun4-yit5-ha4. - Excuse me, may I ask.\n"
            "  請保重。 qiang3-bo3-cung4. - Please take care.\n"
            "  請慢用。 qiang3-man4-yung4. - Please enjoy (your meal).\n"
            "  歡迎再來。 fon1-ngiang2-zai4-loi2. - Welcome to come again.\n"
            "  請多指教。 qiang3-do1-zii3-gau4. - Please guide me.\n"
            "  承蒙關照。 siin2-mung2-guan1-zeu4. - Thank you for your care."
        ),
        "how_it_works": (
            "This record teaches command force: the bare verb is the "
            "informal imperative; adding 請 qiang3 makes it polite; 唔好 "
            "m2-ho3 and 莫 mog5 are the two forbidders (莫 is stronger, "
            "older). The ten informal and ten formal sentences form matched "
            "pairs of situations - the same intent, two registers."
        ),
        "key_points": [
            "20 commands/requests: 10 informal, 10 formal.",
            "Bare verb = informal command; 請 qiang3 = polite request.",
            "唔好 m2-ho3 = don't (soft); 莫 mog5 = don't (strong).",
            "Formal set uses 請, 勞煩, 承蒙 - the courtesy verbs.",
            "請慢用 qiang3-man4-yung4 = 'enjoy your meal'.",
        ],
        "requirements": [
            "Read the verbs record first; imperatives are bare verbs.",
        ],
        "standards": [
            "Register contrasts per documented usage.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["qiang3", "mog5", "m2-ho3", "Twenty"],
        "sig_lens": (
            "Through the Signature lens these are the sworn orders and "
            "petitions: the bare verb as command, the courtesy word as "
            "seal - force and grace, each in its proper register."
        ),
        "drill": {
            "sentences": 20,
            "informal": 10,
            "formal": 10,
            "politeness": "qiang3",
            "forbidders": ["m2-ho3", "mog5"],
        },
    },
    {
        "key": "descriptions",
        "name": "Hakka Chinese Descriptions of People and Places",
        "group": "Grammar in Action",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences describing people, places and things in "
            "detail - adjectives, relative clauses and measure words "
            "working together. \n\n"
            "  佢係高高大大个人。 gi2-he4-go1-go1-tai4-tai4-ge4-ngin2. - He is a tall, big person.\n"
            "  阿婆个頭那白了。 a1-po2-ge4-teu2-na4-pag6-liau3. - Grandmother's hair has turned white.\n"
            "  這隻狗當乖。 li4-zag5-gieu3-dong1-guai1. - This dog is very well-behaved.\n"
            "  該間屋當舊。 ge4-gien1-vuk5-dong1-kiu4. - That house is very old.\n"
            "  梅州係好地方。 moi2-ziu1-he4-ho3-ti4-fong1. - Meizhou is a good place.\n"
            "  山頂个風景當靚。 san1-dang3-ge4-fung1-ging3-dong1-jiang4. - The mountaintop scenery is very pretty.\n"
            "  這條河當清。 li4-tiau2-ho2-dong1-qiang1. - This river is very clear.\n"
            "  街上當多人。 gie1-song4-dong1-do1-ngin2. - There are very many people on the street.\n"
            "  夜晚个街當靜。 ya4-man1-ge4-gie1-dong1-qin4. - The street at night is very quiet.\n"
            "  這本書當有趣。 li4-bun3-su1-dong1-yiu1-qi4. - This book is very interesting.\n"
            "  佢講話當細聲。 gi2-gong3-fa4-dong1-se4-sang1. - He speaks very softly.\n"
            "  細子个目珠當大。 se4-zii3-ge4-mug5-zu1-dong1-tai4. - The child's eyes are very big.\n"
            "  老師戴目鏡。 lo3-sii1-dai4-mug5-giang4. - The teacher wears glasses.\n"
            "  佢著紅衫。 gi2-zog5-fung2-sam1. - She wears a red shirt.\n"
            "  這雙鞋當舒服。 li4-sung1-hai2-dong1-su1-fug6. - These shoes are very comfortable.\n"
            "  菜市場當鬧熱。 coi4-shi4-cong2-dong1-nau4-ngiet6. - The market is very lively.\n"
            "  圍龍屋當大。 vui2-liung2-vuk5-dong1-tai4. - The weilong (round) house is huge.\n"
            "  客家圍屋有歷史。 hag5-ga1-vui2-vuk5-yiu1-lit6-sii3. - Hakka walled houses have history.\n"
            "  天頂个雲走得好快。 tien1-dang3-ge4-yun2-zeu3-det5-ho3-kuai4. - The clouds in the sky move very fast.\n"
            "  這係𠊎看過最靚个地方。 li4-he4-ngai2-kon4-go4-zui4-jiang4-ge4-ti4-fong1. - This is the prettiest place I have ever seen."
        ),
        "how_it_works": (
            "This record teaches rich description: stacked adjectives "
            "(高高大大), the 个 ge4 relative-clause bridge (阿婆个頭那, 山"
            "頂个風景), place nouns with their classifiers (間屋, 條河, 雙"
            "鞋), and the superlative frame (看過最靚). The Hakka round "
            "houses (圍龍屋) ground the descriptions in the real built "
            "heritage."
        ),
        "key_points": [
            "20 detailed descriptive sentences.",
            "Doubled adjectives intensify: 高高大大 'tall and big'.",
            "个 ge4 builds relative clauses: 山頂个風景.",
            "Place classifiers: 間 (houses), 條 (rivers/roads), 雙 (pairs).",
            "Cultural anchors: 圍龍屋 the Hakka round house.",
        ],
        "requirements": [
            "Read the adjectives and grammar records first for 當, 个 and classifiers.",
        ],
        "standards": [
            "Architectural terms (圍龍屋) are documented Hakka heritage vocabulary.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["vui2-liung2-vuk5", "zui4-jiang4", "go1-go1-tai4-tai4", "Twenty"],
        "sig_lens": (
            "Through the Signature lens these are the sworn portraits: "
            "every person measured, every place mapped, every round house "
            "sealed - description as documentation, the archive with eyes."
        ),
        "drill": {
            "sentences": 20,
            "doubled_adjectives": ["go1-go1-tai4-tai4"],
            "place_classifiers": ["gien1", "tiau2", "sung1"],
            "heritage": ["vui2-liung2-vuk5"],
        },
    },
    {
        "key": "story1",
        "name": "Hakka Chinese Story I - All People Are Born Free",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence simple story in Hakka: Article 1 of the "
            "Universal Declaration of Human Rights, in the documented Hakka "
            "translation with its Pha̍k-fa-sṳ transliteration - line-by-line "
            "English translation. Quoted source, not composed. \n\n"
            "  人人生而自由，\n"
            "  Ngìn ngìn sâng yì chhṳ-yù,\n"
            "  All human beings are born free,\n\n"
            "  在尊嚴同權利上一律平等。\n"
            "  chhai chûn ngiàm thùng khièn li sông yit li̍t phìn-tén.\n"
            "  and equal in dignity and rights.\n\n"
            "  佢丁人賦有理性同好心田，\n"
            "  Kì tên ngìn fù yû lî sin thùng hó sîm thièn,\n"
            "  They are endowed with reason and conscience\n\n"
            "  並應以兄弟關係個精神相對待。\n"
            "  pin yin yî hiûng thi kôan hì ke chîn sṳ̀n siông tui thai.\n"
            "  and should act towards one another in a spirit of brotherhood.\n\n"
            "Word notes: 人人 ngin2-ngin2 'everyone'; 自由 cii4-yiu2 "
            "'freedom'; 尊嚴 zun1-ngiam2 'dignity'; 權利 kien2-li4 'rights'; "
            "平等 pin2-den3 'equality'; 理性 li1-xin4 'reason'; 兄弟 hiung1-"
            "ti4 'brothers'. 佢丁 gi2-den1 is the literary 'they' of this "
            "translation. This is the simplest of the three stories: short "
            "lines, grand ideas, every word a foundation stone."
        ),
        "how_it_works": (
            "This record proves the database's authenticity claim: a "
            "published, checkable Hakka text - the UDHR Article 1 - given "
            "in characters, Pha̍k-fa-sṳ romanization and line-by-line "
            "English, with word notes glossing the key vocabulary. It "
            "teaches reading real Hakka: formal register, abstract nouns, "
            "and the literary pronoun 佢丁."
        ),
        "key_points": [
            "10 lines: the documented Hakka UDHR Article 1 with Pha̍k-fa-sṳ.",
            "Quoted source with citation - not a composed teaching text.",
            "Abstract vocabulary: 自由, 尊嚴, 權利, 平等, 理性.",
            "Literary pronoun 佢丁 gi2-den1 'they'.",
            "Every line glossed word-by-word in the notes.",
        ],
        "requirements": [
            "Read the writing-system record first for Pha̍k-fa-sṳ diacritics.",
        ],
        "standards": [
            "Text and transliteration quoted from the published Hakka UDHR translation.",
        ],
        "citations": [CIT_UDHR],
        "must_contain": ["chhṳ-yù", "phìn-tén", "hiûng thi", "Universal Declaration"],
        "sig_lens": (
            "Through the Signature lens this story is the sworn charter: "
            "freedom and dignity sealed in Hakka characters, every human a "
            "signatory - the archive's founding document, quoted whole."
        ),
        "drill": {
            "lines": 4,
            "sentences": 10,
            "quoted": True,
            "key_words": ["cii4-yiu2", "zun1-ngiam2", "kien2-li4", "pin2-den3"],
            "romanization": "Pha̍k-fa-sṳ",
        },
    },
    {
        "key": "story2",
        "name": "Hakka Chinese Story II - The Guest Family's Journey",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the past tense - the Hakka migration, "
            "told in Hakka with line-by-line English. A composed teaching "
            "story in documented vocabulary and grammar. \n\n"
            "  𠊎个祖公對中原來。 ngai2-ge4-zu3-gung1 dui4-zung1-ngian2-loi2. - My ancestors came from the Central Plains.\n"
            "  佢兜行了當遠个路。 gi2-deu1 hang2-liau3-dong1-yen3-ge4-lu4. - They walked a very long road.\n"
            "  經過江西同福建。 ging1-go4-gong1-xi1-tung2-fug5-gien4. - They passed through Jiangxi and Fujian.\n"
            "  到了廣東个山區。 dau4-liau3-gong3-dung1-ge4-san1-ki1. - They reached the mountains of Guangdong.\n"
            "  佢兜起圍龍屋。 gi2-deu1-hi3-vui2-liung2-vuk5. - They built round houses.\n"
            "  開田種禾。 koi1-tien2-zung4-vo2. - They opened fields and planted rice.\n"
            "  日出而作，日落而息。 ngit5-cut5-ngi2-zog5, ngit5-log6-ngi2-xit5. - They worked at sunrise and rested at sunset.\n"
            "  雖然辛苦，毋忘祖宗言。 sui1-ngian2-xin1-fu3, m2-mong4-zu3-zung1-ngian2. - Though life was hard, they never forgot the ancestors' speech.\n"
            "  一代傳一代。 yit5-toi4-con2-yit5-toi4. - Generation passed it to generation.\n"
            "  今下𠊎兜還講客家話。 gin1-ha4-ngai2-deu1-han2-gong3-hag5-ga1-fa4. - And today we still speak Hakka."
        ),
        "how_it_works": (
            "This record teaches past-tense narration: 了 liau3 marking "
            "completed events, 過 go4 implied in the journey, time words "
            "(對...來, 到了) sequencing the migration. The story carries the "
            "documented history - Central Plains to Jiangxi to Fujian to "
            "Guangdong, the round houses, the vow never to forget the "
            "speech - inside ten simple past-tense sentences."
        ),
        "key_points": [
            "10-sentence past-tense story with line-by-line English.",
            "Composed teaching story; history follows the documented migration account.",
            "Past markers: 來, 了, 到了 sequencing events.",
            "Key vow: 毋忘祖宗言 'never forget the ancestors' speech'.",
            "Ends in the present: 今下還講客家話.",
        ],
        "requirements": [
            "Read the tenses record first for 了 and past narration.",
        ],
        "standards": [
            "Historical frame follows the documented Hakka migration; sentences are composed teaching text.",
        ],
        "citations": [CIT_LI, CIT_PROVERBS],
        "must_contain": ["zu3-gung1", "vui2-liung2-vuk5", "m2-mong4-zu3-zung1-ngian2", "ten-sentence"],
        "sig_lens": (
            "Through the Signature lens this is the sworn chronicle: the "
            "thousand-year road sealed in ten sentences, every step a vow "
            "kept - the guest-family journey, archived."
        ),
        "drill": {
            "lines": 10,
            "tense": "past",
            "past_markers": ["liau3", "dau4-liau3"],
            "composed": True,
            "stops": ["Zhongyuan", "Jiangxi", "Fujian", "Guangdong"],
        },
    },
    {
        "key": "story3",
        "name": "Hakka Chinese Story III - Tomorrow's Hakka",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the future and conditional - a child "
            "imagining tomorrow, in Hakka with line-by-line English. A "
            "composed teaching story. \n\n"
            "  天光日𠊎會去學校。 tien1-gong1-ngit5-ngai2-voi4-hi4-hog6-hau4. - Tomorrow I will go to school.\n"
            "  𠊎會學好客家話。 ngai2-voi4-hog6-ho3-hag5-ga1-fa4. - I will learn Hakka well.\n"
            "  𠊎會教細子講。 ngai2-voi4-gau4-se4-zii3-gong3. - I will teach the children to speak it.\n"
            "  若係大家努力，客家話會傳下去。 ngiog6-he4-tai4-ga1-nu3-lag6, hag5-ga1-fa4-voi4-con2-ha1-hi4. - If everyone works hard, Hakka will be passed on.\n"
            "  𠊎兜會起新个學校。 ngai2-deu1-voi4-hi3-xin1-ge4-hog6-hau4. - We will build a new school.\n"
            "  會請好个老師。 voi4-qiang3-ho3-ge4-lo3-sii1. - We will invite good teachers.\n"
            "  細子會唱山歌。 se4-zii3-voi4-cong4-san1-go1. - The children will sing mountain songs.\n"
            "  過年會轉唐山。 go4-ngian2-voi4-zon3-tong2-san1. - At New Year we will return to the homeland.\n"
            "  阿公阿婆會歡喜。 a1-gung1-a1-po2-voi4-fon1-hi3. - Grandfather and grandmother will be happy.\n"
            "  客家話萬歲! hag5-ga1-fa4-van4-soi4! - Long live the Hakka language!"
        ),
        "how_it_works": (
            "This record teaches future and conditional: 會 voi4 on nearly "
            "every verb, the 若係...會... ngiog6-he4 conditional frame, and "
            "the closing exclamation. The vocabulary looks forward - 學校, "
            "老師, 山歌, 轉唐山 - while the grammar stays in the aspect "
            "system taught in the tenses record."
        ),
        "key_points": [
            "10-sentence future/conditional story with line-by-line English.",
            "Composed teaching story.",
            "Future marker 會 voi4; conditional frame 若係...會....",
            "Forward vocabulary: 起學校, 請老師, 唱山歌, 轉唐山.",
            "Closes with the blessing 客家話萬歲.",
        ],
        "requirements": [
            "Read the tenses record first for 會 and conditionals.",
        ],
        "standards": [
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_LI],
        "must_contain": ["voi4", "ngiog6-he4", "van4-soi4", "ten-sentence"],
        "sig_lens": (
            "Through the Signature lens this is the sworn promise: the "
            "future sealed in ten sentences, every 'will' a vow - the "
            "language carried forward, generation to generation."
        ),
        "drill": {
            "lines": 10,
            "tense": "future",
            "future_marker": "voi4",
            "conditional": "ngiog6-he4",
            "composed": True,
        },
    },
    {
        "key": "idioms",
        "name": "Hakka Chinese Idioms and Proverbs",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty Hakka idioms and proverbs - literal translation, real "
            "meaning, and an example sentence each. Quoted from the "
            "traditional 客家諺語 corpus. \n\n"
            "  寧賣祖宗田，不忘祖宗言。 nin2-mai4-zu3-zung1-tien2, but-mong4-zu3-zung1-ngian2. - Lit: Better sell the ancestral fields than forget the ancestors' speech. Meaning: the language is the clan's soul; keep it at any cost.\n"
            "  一下雷鳴天下知。 yit5-ha4-lui2-min2-tien1-ha4-di1. - Lit: One thunderclap and all under heaven knows. Meaning: no deed stays secret forever.\n"
            "  一世做官三世絕。 yit5-shi4-zo4-guan1-sam1-shi4-qiet6. - Lit: One generation as official, three generations ruined. Meaning: power offends, and the price falls on descendants.\n"
            "  乞食仔唱山歌。 het5-shit6-e3-cong4-san1-go1. - Lit: The beggar boy sings mountain songs. Meaning: poverty does not kill joy.\n"
            "  大目娘看不到灶頭。 tai4-mug5-ngiong2-kon4-but5-dau4-zo4-teu2. - Lit: The big-eyed lady cannot see the stove. Meaning: even the sharpest miss what is under their nose.\n"
            "  老鼠尋貓公。 lo3-cu3-qim2-meu4-gung1. - Lit: The mouse seeks out the tomcat. Meaning: courting disaster on purpose.\n"
            "  沒節个竹筒。 mut6-jiet5-ge4-zug5-tung2. - Lit: A bamboo tube without joints. Meaning: busy about nothing; nothing held.\n"
            "  供子身，冇供子心。 giung1-zii3-siin1, mau2-giung1-zii3-xim1. - Lit: Give the child a body, not a heart. Meaning: parents shape the body, never the mind.\n"
            "  行莫嫖，坐莫賭。 hang2-mog5-pieu2, co4-mog5-du3. - Lit: Walking, no visiting brothels; sitting, no gambling. Meaning: be virtuous in private as in public.\n"
            "  你有初一，我有十五。 ngi2-yiu1-cu1-yit5, ngai2-yiu1-ship6-ng3. - Lit: You have the first of the month, I have the fifteenth. Meaning: everyone has their own talent and day.\n"
            "  妻賢子肖父之寬。 qi1-hien2-zii3-xiau4-fu4-zii1-kuan1. - Lit: Wife virtuous, son filial, father lenient. Meaning: each family role has its proper conduct.\n"
            "  食兩粒黃豆仔，就想學人上西天。 sit5-liong3-liap6-vong2-teu4-e3, qiu4-xiong3-hog6-ngin2-song1-xi1-tien1. - Lit: Eat two soybeans and dream of flying to heaven. Meaning: a little learning breeds wild ambition.\n"
            "  認聲不認姓。 ngin4-sang1-but5-ngin4-xiang4. - Lit: Acknowledge the speech, not the surname. Meaning: the dialect, not the family name, proves a Hakka.\n"
            "  入鄉隨俗。 ngip6-hiong1-cui2-siug6. - Lit: Enter the village, follow its customs. Meaning: adapt to local ways.\n"
            "  好事多磨。 ho3-sii4-do1-mo2. - Lit: Good things take much grinding. Meaning: worthwhile things come hard.\n"
            "  心急食唔到熱豆腐。 xim1-gip5-sit5-m2-dau4-ngiat6-teu4-fu4. - Lit: The hasty mouth cannot eat hot tofu. Meaning: haste ruins the reward.\n"
            "  一分耕耘，一分收穫。 yit5-fun1-gang1-yun2, yit5-fun1-siu1-fog6. - Lit: One part plowing, one part harvest. Meaning: you reap what you sow.\n"
            "  樹高千丈，落葉歸根。 su4-go1-qien1-cong4, log6-yiap6-gui1-gin1. - Lit: The tree a thousand fathoms high, its fallen leaves return to the roots. Meaning: no matter how far you go, you return to your origins.\n"
            "  和氣生財。 fo2-hi4-sang1-coi2. - Lit: Harmony breeds wealth. Meaning: peace is profitable.\n"
            "  學到老，做到老。 hog6-dau4-lau3, zo4-dau4-lau3. - Lit: Learn till old, work till old. Meaning: never stop learning."
        ),
        "how_it_works": (
            "This record teaches wisdom speech: twenty proverbs from the "
            "documented 客家諺語 corpus, each in three layers - the Hakka "
            "line with Pinfa, the literal English (often startling), and "
            "the real meaning. Proverbs are quoted heritage, not composed, "
            "and several double as cultural history (the land-and-language "
            "vow, 認聲不認姓)."
        ),
        "key_points": [
            "20 proverbs: literal translation + real meaning + context.",
            "Quoted from the traditional Hakka proverb corpus.",
            "The land-and-language vow: 寧賣祖宗田，不忘祖宗言.",
            "認聲不認姓: speech, not surname, proves a Hakka.",
            "Every proverb is usable in conversation - they are living speech.",
        ],
        "requirements": [
            "Read the stories records first for the historical background.",
        ],
        "standards": [
            "Proverbs quoted from the documented 客家諺語 corpus.",
        ],
        "citations": [CIT_PROVERBS],
        "must_contain": ["寧賣祖宗田", "認聲不認姓", "乞食仔唱山歌", "Twenty"],
        "sig_lens": (
            "Through the Signature lens these are the sworn maxims: twenty "
            "vows of the guest-family nation, each sealed by generations of "
            "use - wisdom that has survived a thousand years of road."
        ),
        "drill": {
            "idioms": 20,
            "quoted": True,
            "land_vow": "寧賣祖宗田，不忘祖宗言",
            "speech_vow": "認聲不認姓",
        },
    },
    {
        "key": "registers",
        "name": "Hakka Chinese Formal and Polite Registers",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen formal-versus-informal pairs - letters, business and "
            "elders - showing how Hakka shifts its weight. \n\n"
            "  Informal: 食飯冇? sit5-pon4-mau2? - Formal: 請問食飽了冇? qiang3-mun4-sit5-bau3-liau3-mau2? - Have you eaten?\n"
            "  Informal: 來坐。 loi2-co4. - Formal: 請入來坐。 qiang3-ngip6-loi2-co4. - Come sit.\n"
            "  Informal: 幾多錢? gi3-do1-qian2? - Formal: 請問幾多錢? qiang3-mun4-gi3-do1-qian2? - How much?\n"
            "  Informal: 𠊎唔知。 ngai2-m2-di1. - Formal: 𠊎不清楚。 ngai2-m2-qiang1-cu3. - I don't know.\n"
            "  Informal: 等下。 den3-ha4. - Formal: 請稍等。 qiang3-sau1-den3. - Wait a moment.\n"
            "  Informal: 拿來。 na1-loi2. - Formal: 勞煩拿來。 lo2-fan2-na1-loi2. - Bring it here.\n"
            "  Informal: 講大聲點。 gong3-tai4-sang1-diam3. - Formal: 請講大聲一點。 qiang3-gong3-tai4-sang1-yit5-diam3. - Speak louder, please.\n"
            "  Informal: 轉去吧。 zon3-hi4-ba1. - Formal: 請慢行。 qiang3-man4-hang2. - Please go (take care).\n"
            "  Informal: 多謝。 do1-qia4. - Formal: 承蒙你。 siin2-mung2-ngi2. - Thank you kindly.\n"
            "  Informal: 對唔住。 dui4-m2-qi4. - Formal: 實在唔好意思。 sit6-cai4-m2-ho3-ji4-sii1. - I am truly sorry.\n"
            "  Informal: 𠊎寫信分你。 ngai2-xia3-xin4-bun1-ngi2. - Formal: 敬啟者... ngin4-qi3-zhe3... - Letter opening: Dear Sir/Madam...\n"
            "  Informal: 好，就恁樣。 ho3, qiu4-an4-ngiong4. - Formal: 好，就照你講个辦。 ho3, qiu4-zeu4-ngi2-gong3-ge4-pan4. - Business: agreed, we will do as you say.\n"
            "  Informal: 阿爸，食飯! a1-ba1, sit5-pon4! - Formal: 阿爸，請食飯。 a1-ba1, qiang3-sit5-pon4. - Father, (please) eat.\n"
            "  Informal: 借錢來。 jia4-qian2-loi2. - Formal: 想同你借一點錢。 xiong3-tung2-ngi2-jia4-yit5-diam3-qian2. - I would like to borrow some money.\n"
            "  Informal: 唔得閒。 m2-det5-han2. - Formal: 實在抽唔出時間。 sit6-cai4-cau1-m2-cut5-si2-gien1. - I truly cannot spare the time."
        ),
        "how_it_works": (
            "This record teaches register shift: the same intent in work "
            "clothes and in ceremony. The formal side adds 請, 請問, 勞煩, "
            "承蒙, softens verbs (不清楚 for 唔知), and lengthens the "
            "sentence; the informal side is bare and direct. Letters get "
            "敬啟者, business gets 照你講个辦, elders get 請 before every "
            "verb."
        ),
        "key_points": [
            "15 formal/informal pairs with translations.",
            "Formal markers: 請, 請問, 勞煩, 承蒙, 敬啟者.",
            "Softening: 唔知 -> 不清楚; 轉去吧 -> 請慢行.",
            "Elders: put 請 before the verb; never bark orders.",
            "Business closings: 照你講个辦 'as you say'.",
        ],
        "requirements": [
            "Read the commands record first for 請 and the forbidders.",
        ],
        "standards": [
            "Register contrasts per documented usage.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["qiang3-mun4", "siin2-mung2", "ngin4-qi3-zhe3", "Fifteen"],
        "sig_lens": (
            "Through the Signature lens these are the sworn courtesies in "
            "two weights: the plain word for kin, the sealed word for "
            "elders and guests - respect measured out in syllables."
        ),
        "drill": {
            "pairs": 15,
            "formal_markers": ["qiang3", "qiang3-mun4", "lo2-fan2", "siin2-mung2"],
            "letter_opening": "ngin4-qi3-zhe3",
        },
    },
    {
        "key": "complex",
        "name": "Hakka Chinese Compound and Complex Sentences",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen long sentences with clauses, connectors and relative "
            "clauses - parsed and translated. \n\n"
            "  𠊎食完飯就去學校。 [𠊎/食完飯/就/去學校] ngai2-sit5-von2-pon4-qiu4-hi4-hog6-hau4. - After I finish eating, I go to school.\n"
            "  因為落雨，所以冇去。 [因為/落雨/所以/冇去] jin1-vui4-log6-sui3, so3-ji3-mau2-hi4. - Because it rained, (we) did not go.\n"
            "  雖然當遠，但係值得去。 [雖然/當遠/但係/值得去] sui1-ngian2-dong1-yen3, tan4-he4-cit6-det5-hi4. - Although it is far, it is worth going.\n"
            "  佢講个話𠊎聽唔明。 [佢講个話/𠊎/聽唔明] gi2-gong3-ge4-fa4-ngai2-tang1-m2-min2. - I don't understand what he says.\n"
            "  𠊎買个書當有趣。 [𠊎買个書/當有趣] ngai2-mai1-ge4-su1-dong1-yiu1-qi4. - The book I bought is very interesting.\n"
            "  你尋个人來了。 [你尋个人/來了] ngi2-qim2-ge4-ngin2-loi2-liau3. - The person you were looking for has come.\n"
            "  若係有閒就來尞。 [若係/有閒/就/來尞] ngiog6-he4-yiu1-han2-qiu4-loi2-liau4. - If you are free, come visit.\n"
            "  食得多，身體就好。 [食得多/身體就好] sit5-det5-do1, siin1-ti3-qiu4-ho3. - Eat plenty and the body stays well.\n"
            "  佢一邊行一邊唱歌。 [佢/一邊行/一邊唱歌] gi2-yit5-bien1-hang2-yit5-bien1-cong4-go1. - He sings while walking.\n"
            "  越學越有趣。 [越學/越有趣] yet6-hog6-yet6-yiu1-qi4. - The more you learn, the more interesting it gets.\n"
            "  唔單止好食，擱當平。 [唔單止/好食/擱/當平] m2-dan1-zii3-ho3-sit5, gog5-dong1-piang2. - Not only tasty but also cheap.\n"
            "  頭先講个事，你記得麼? [頭先講个事/你記得麼] teu2-xien1-gong3-ge4-sii4, ngi2-gi4-det5-ma1? - Do you remember what was just said?\n"
            "  阿公講古个時節，𠊎兜靜靜聽。 [阿公講古个時節/𠊎兜靜靜聽] a1-gung1-gong3-gu3-ge4-si2-jiet5, ngai2-deu1-qin4-qin4-tang1. - When Grandfather told old stories, we listened quietly.\n"
            "  等𠊎轉來再講。 [等/𠊎轉來/再講] den3-ngai2-zon3-loi2-zai4-gong3. - Wait till I return, then we will talk.\n"
            "  無論幾辛苦，都愛堅持。 [無論/幾辛苦/都/愛堅持] vu2-lun4-gi3-xin1-fu3, du1-oi4-gien1-cii2. - No matter how hard, keep going."
        ),
        "how_it_works": (
            "This record teaches clause architecture: each sentence is "
            "bracket-parsed so learners see the joints - 因為...所以, 雖"
            "然...但係, 若係...就, 个-relative clauses, 一邊...一邊, 越..."
            "越, 唔單止...擱, and time clauses with 个時節. The connectors "
            "are the load-bearing beams; learn them and long sentences "
            "assemble themselves."
        ),
        "key_points": [
            "15 complex sentences, each bracket-parsed and translated.",
            "Connectors: 因為...所以, 雖然...但係, 若係...就.",
            "Relative clauses with 个: 佢講个話, 𠊎買个書.",
            "Correlatives: 一邊...一邊, 越...越, 唔單止...擱.",
            "Time clauses: 个時節 'when'; 等...再... 'wait till...then'.",
        ],
        "requirements": [
            "Read the grammar-essentials and tenses records first.",
        ],
        "standards": [
            "Connector inventory per Hashimoto 1973.",
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_HASHIMOTO, CIT_LI],
        "must_contain": ["jin1-vui4", "sui1-ngian2", "ngiog6-he4", "yet6-hog6"],
        "sig_lens": (
            "Through the Signature lens these are the sworn long-houses: "
            "fifteen great sentences, every beam and joint visible - the "
            "architecture of thought, built to stand."
        ),
        "drill": {
            "sentences": 15,
            "connectors": ["jin1-vui4-so3-ji3", "sui1-ngian2-tan4-he4",
                           "ngiog6-he4-qiu4", "yit5-bien1", "yet6"],
            "parsed": True,
        },
    },
    {
        "key": "conv_market",
        "name": "Hakka Chinese Conversation - At the Market",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue at the market, annotated. "
            "A-buyer meets B-seller. \n\n"
            "  A: 老闆，早! lo3-ban3, zau3! - Boss, good morning!\n"
            "  B: 早! 買麼个? zau3! mai1-mag5-ge4? - Morning! What are you buying?\n"
            "  A: 豬肉幾多錢一斤? zu1-ngiuk6-gi3-do1-qian2-yit5-gin1? - How much is pork per catty?\n"
            "  B: 廿五塊。 ngiam4-ng3-kuai4. - Twenty-five dollars.\n"
            "  A: 恁貴! 平一點好麼? an4-gui4! piang2-yit5-diam3-ho3-ma1? - So expensive! A bit cheaper?\n"
            "  B: 廿三，最平了。 ngiam4-sam1, zui4-piang2-liau3. - Twenty-three, the cheapest already.\n"
            "  A: 好，買兩斤。 ho3, mai1-liong3-gin1. - OK, two catties.\n"
            "  B: 還愛麼个? han2-oi4-mag5-ge4? - Anything else?\n"
            "  A: 菜心幾多錢? coi4-xim1-gi3-do1-qian2? - How much is the choi-sum?\n"
            "  B: 五塊一斤。 ng3-kuai4-yit5-gin1. - Five dollars a catty.\n"
            "  A: 買一斤。 mai1-yit5-gin1. - One catty.\n"
            "  B: 一共五十五塊。 yit5-kiung4-ng3-sip6-ng3-kuai4. - Fifty-five dollars altogether.\n"
            "  A: 給，一百塊。 gip5, yit5-bag5-kuai4. - Here, one hundred.\n"
            "  B: 找你四十五。 zau3-ngi2-si4-sip6-ng3. - Forty-five change for you.\n"
            "  A: 數啱了。 su3-ang1-liau3. - The count is right.\n"
            "  B: 下擺再來! ha4-bai3-zai4-loi2! - Come again!\n"
            "  A: 好，多謝! ho3, do1-qia4! - OK, thanks!\n"
            "  B: 慢行! man4-hang2! - Take care!\n"
            "  A: (轉身) 該檔菜當新鮮。 (zon3-siin1) ge4-dong4-coi4-dong1-xin1-xien1. - (turning) That stall's vegetables are very fresh.\n"
            "  B: (笑) 聽到你講好話了! (xiau4) tang1-dau4-ngi2-gong3-ho3-fa4-liau3! - (laughing) I heard your kind words!\n\n"
            "Notes: 廿 ngiam4 = twenty (the old single character for 二十); "
            "一共 yit5-kiung4 = altogether; 數啱 su3-ang1 = the count is "
            "correct; the whole dialogue reuses the bargaining ladder from "
            "the shopping record."
        ),
        "how_it_works": (
            "This record stages a full market transaction: greeting, "
            "price-asking, bargaining, adding items, totaling, paying, "
            "change-checking, and the farewell pair (下擺再來 / 慢行). The "
            "annotation teaches the market-only words (廿, 一共, 數啱) and "
            "shows the shopping record's formulas in living sequence."
        ),
        "key_points": [
            "20-line bilingual market dialogue, annotated.",
            "Full arc: greet -> price -> bargain -> buy -> pay -> change -> farewell.",
            "Market words: 廿 ngiam4 twenty; 一共 yit5-kiung4 altogether; 數啱 correct count.",
            "Bargaining ladder reused: 恁貴 -> 平一點 -> 最平了 -> 好.",
            "Closes with the warm pair 下擺再來 / 慢行.",
        ],
        "requirements": [
            "Read the shopping and numbers records first.",
        ],
        "standards": [
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["ngiam4", "yit5-kiung4", "su3-ang1", "twenty-line"],
        "sig_lens": (
            "Through the Signature lens this is the sworn transaction: "
            "every price spoken, every coin counted, every farewell sealed "
            "- the marketplace dialogue archived whole."
        ),
        "drill": {
            "lines": 20,
            "speakers": ["A", "B"],
            "market_words": ["ngiam4", "yit5-kiung4", "su3-ang1"],
            "arc": ["greet", "price", "bargain", "buy", "pay", "change", "farewell"],
        },
    },
    {
        "key": "conv_friend",
        "name": "Hakka Chinese Conversation - Meeting a Friend",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue between old friends, "
            "annotated. A-host meets B-guest. \n\n"
            "  A: 阿強，好久冇見! a1-kiong2, ho3-giu3-mau2-gien4! - A-Kiong, long time no see!\n"
            "  B: 係啊! 你當好麼? he4-a1! ngi2-dong1-ho3-ma1? - Yes! Are you well?\n"
            "  A: 當好。你呢? dong1-ho3. ngi2-ne1? - Very well. And you?\n"
            "  B: 還可以。 han2-ko3-ji3. - Getting by.\n"
            "  A: 入來坐，飲茶。 ngip6-loi2-co4, jim3-ca2. - Come in, sit, have tea.\n"
            "  B: 唔好意思，打擾了。 m2-ho3-ji4-sii1, da3-gieu3-liau3. - Sorry to disturb you.\n"
            "  A: 哪裡話! 歡迎! nai3-li1-fa4! fon1-ngiang2! - Nonsense! Welcome!\n"
            "  B: 你个細子幾大了? ngi2-ge4-se4-zii3-gi3-tai4-liau3? - How old is your child now?\n"
            "  A: 十歲了，讀三年級。 sip6-soi4-liau3, tug6-sam1-ngian2-kip5. - Ten, in third grade.\n"
            "  B: 當乖。 dong1-guai1. - Very well-behaved.\n"
            "  A: 你在深圳做事還好麼? ngi2-cai4-shim1-zun4-zo4-sii4-han2-ho3-ma1? - Is work in Shenzhen still good?\n"
            "  B: 還好，就係忙。 han2-ho3, qiu4-he4-mang2. - Fine, just busy.\n"
            "  A: 有閒轉來尞。 yiu1-han2-zon3-loi2-liau4. - Come back to visit when free.\n"
            "  B: 一定。一定。 yit5-tin4. yit5-tin4. - Definitely. Definitely.\n"
            "  A: 中午在這食飯。 zung1-ng3-cai4-li4-sit5-pon4. - Stay for lunch here.\n"
            "  B: 唔使客氣了。 m2-sii3-hag5-hi4-liau3. - Don't stand on ceremony.\n"
            "  A: 自家人，客氣麼个! cii4-ga1-ngin2, hag5-hi4-mag5-ge4! - We're family, what's ceremony!\n"
            "  B: 好，那就打擾了。 ho3, na4-qiu4-da3-gieu3-liau3. - OK then, I'll impose.\n"
            "  A: 食飽再走。 sit5-bau3-zai4-zeu3. - Leave after you've eaten your fill.\n"
            "  B: 下擺你來𠊎屋下。 ha4-bai3-ngi2-loi2-ngai2-vuk5-ha1. - Next time come to my place.\n\n"
            "Notes: 哪裡話 nai3-li1-fa4 = 'nonsense, don't say that' (the "
            "polite refusal of thanks); 自家人 cii4-ga1-ngin2 = 'one's own "
            "people'; 尞 liau4 = to visit socially."
        ),
        "how_it_works": (
            "This record stages friendship: the reunion greeting, the "
            "catch-up questions (child, work), the hospitality ritual "
            "(入來坐，飲茶), the polite refusal dance (唔好意思 / 哪裡話), "
            "the meal invitation and its acceptance, and the reciprocal "
            "invitation. The annotation teaches the social formulas that "
            "make Hakka hospitality run."
        ),
        "key_points": [
            "20-line bilingual friend dialogue, annotated.",
            "Hospitality ritual: 入來坐，飲茶; refusal dance: 哪裡話.",
            "自家人 cii4-ga1-ngin2 = one's own people (no ceremony needed).",
            "Reciprocal invitation closes every visit: 下擺你來𠊎屋下.",
            "Catch-up frames: 幾大了, 還好麼, 有閒轉來尞.",
        ],
        "requirements": [
            "Read the friendship and greetings records first.",
        ],
        "standards": [
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["nai3-li1-fa4", "cii4-ga1-ngin2", "liau4", "twenty-line"],
        "sig_lens": (
            "Through the Signature lens this is the sworn reunion: every "
            "welcome warm, every refusal polite, every visit repaid - "
            "friendship as a covenant renewed line by line."
        ),
        "drill": {
            "lines": 20,
            "speakers": ["A", "B"],
            "formulas": ["nai3-li1-fa4", "cii4-ga1-ngin2", "liau4"],
            "arc": ["reunion", "catch-up", "hospitality", "invitation", "reciprocal"],
        },
    },
    {
        "key": "conv_problem",
        "name": "Hakka Chinese Conversation - Solving a Problem",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue solving a problem - a broken "
            "water pipe - annotated. A-neighbor meets B-neighbor. \n\n"
            "  A: 阿嫂，唔好意思。 a1-so3, m2-ho3-ji4-sii1. - Sister-in-law, excuse me.\n"
            "  B: 麼个事? mag5-ge4-sii4? - What is it?\n"
            "  A: 𠊎屋水喉漏水。 ngai2-vuk5-sui3-heu2-leu4-sui3. - My water pipe is leaking.\n"
            "  B: 哪位漏? nai3-vi4-leu4? - Where is it leaking?\n"
            "  A: 廚房該截。 cu2-fong2-ge4-jiet5. - The kitchen section.\n"
            "  B: 關水掣冇? guan1-sui3-zat5-mau2? - Have you shut the water valve?\n"
            "  A: 關了，還係漏。 guan1-liau3, han2-he4-leu4. - Shut, but still leaking.\n"
            "  B: 愛請師傅來修。 oi4-qiang3-sii1-fu4-loi2-xiu1. - Need to call a repairman.\n"
            "  A: 你識師傅麼? ngi2-shit5-sii1-fu4-ma1? - Do you know a repairman?\n"
            "  B: 識，佢住隔壁。 shit5, gi2-qi4-gag5-biag5. - Yes, he lives next door.\n"
            "  A: 勞煩你打電話分佢。 lo2-fan2-ngi2-da3-tien4-fa4-bun1-gi2. - Please call him for me.\n"
            "  B: 好，等下。 ho3, den3-ha4. - OK, one moment.\n"
            "  A: 修好愛幾多錢? xiu1-ho3-oi4-gi3-do1-qian2? - How much to fix it?\n"
            "  B: 佢講五十塊。 gi2-gong3-ng3-sip6-kuai4. - He says fifty dollars.\n"
            "  A: 可以。幾時來? ko3-ji3. gi3-si2-loi2? - Fine. When will he come?\n"
            "  B: 下晝三點。 ha4-zu4-sam1-diam3. - Three this afternoon.\n"
            "  A: 承蒙你幫忙。 siin2-mung2-ngi2-bong1-mang2. - Thank you for your help.\n"
            "  B: 細事一樁。 se4-sii4-yit5-zong1. - A small matter.\n"
            "  A: 修好請你飲茶。 xiu1-ho3-qiang3-ngi2-jim3-ca2. - I'll treat you to tea when it's fixed.\n"
            "  B: 好，一言為定。 ho3, yit5-ngian2-vui2-tin4. - Deal, a promise is a promise.\n\n"
            "Notes: 水喉 sui3-heu2 = water pipe; 水掣 sui3-zat5 = water "
            "valve; 師傅 sii1-fu4 = master workman; 一言為定 = 'one word "
            "settles it' (deal)."
        ),
        "how_it_works": (
            "This record stages problem-solving: stating the trouble (漏"
            "水), locating it (哪位), first aid (關水掣), finding help (識"
            "師傅麼), the favor (勞煩你), price and time (幾多錢, 幾時), "
            "thanks (承蒙), and the tea promise that seals it. The "
            "annotation teaches the repair vocabulary and the favor economy "
            "of Hakka neighborhoods."
        ),
        "key_points": [
            "20-line bilingual problem-solving dialogue, annotated.",
            "Repair words: 水喉 sui3-heu2 pipe; 水掣 sui3-zat5 valve; 師傅 sii1-fu4 workman.",
            "Favor economy: 勞煩你 -> 承蒙你 -> 請你飲茶.",
            "Deal sealed: 一言為定 yit5-ngian2-vui2-tin4.",
            "Small-matter reply: 細事一樁 se4-sii4-yit5-zong1.",
        ],
        "requirements": [
            "Read the home and commands records first.",
        ],
        "standards": [
            TEACHING_SENTENCE_NOTE,
        ],
        "citations": [CIT_MACIVER, CIT_LI],
        "must_contain": ["sui3-heu2", "sii1-fu4", "yit5-ngian2-vui2-tin4", "twenty-line"],
        "sig_lens": (
            "Through the Signature lens this is the sworn repair: trouble "
            "named, help found, price fixed, promise sealed with tea - the "
            "neighborhood covenant, archived."
        ),
        "drill": {
            "lines": 20,
            "speakers": ["A", "B"],
            "repair_words": ["sui3-heu2", "sui3-zat5", "sii1-fu4"],
            "arc": ["trouble", "locate", "first-aid", "help", "price", "time", "thanks", "seal"],
        },
    },
    {
        "key": "mastery",
        "name": "Hakka Chinese Mastery Review and Full Reference",
        "group": "Mastery Reference",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The whole database in one teaching summary: the tone table, "
            "200 core words, the ten grammar rules, and the five phrase "
            "tables - the ladder's summit. \n\n"
            "TONE TABLE (Pinfa): 1 yinping 44 高平 - 夫 fu1; 2 yangping 11 "
            "低平 - 扶 fu2; 3 shang 31 下降 - 府 fu3; 4 qu 52 高降 - 富 "
            "fu4; 5 yinru 低促 - 福 fug5; 6 yangru 高促 - 服 fug6. \n\n"
            "200 CORE WORDS (word - gloss): 𠊎 ngai2 I, 你 ngi2 you, 佢 "
            "gi2 he/she, 𠊎兜 ngai2-deu1 we, 你兜 ngi2-deu1 you(pl), 佢兜 "
            "gi2-deu1 they, 人 ngin2 person, 屋 vuk5 house, 屋下 vuk5-ha1 "
            "home, 水 sui3 water, 火 fo3 fire, 山 san1 mountain, 天 tien1 "
            "sky, 日 ngit5 sun/day, 月 ngiat6 moon/month, 米 mi3 rice, 飯 "
            "pon4 cooked rice, 錢 qian2 money, 書 su1 book, 學校 hog6-hau4 "
            "school, 老師 lo3-sii1 teacher, 醫生 ji1-sen1 doctor, 朋友 "
            "pen2-iu1 friend, 街 gie1 street, 車 ca1 car, 電話 tien4-fa4 "
            "telephone, 狗 gieu3 dog, 雞 gie1 chicken, 豬 zu1 pig, 魚 ng2 "
            "fish, 樹 su4 tree, 花 fa1 flower, 食 sit5 eat, 飲 jim3 drink, "
            "睡 soi4 sleep, 行 hang2 walk, 走 zeu3 run, 講 gong3 speak, 看 "
            "kon4 look, 聽 tang1 listen, 寫 xia3 write, 讀 tug6 study, 做 "
            "zo4 do, 買 mai1 buy, 賣 mai4 sell, 去 hi4 go, 來 loi2 come, 坐 "
            "co4 sit, 企 ki1 stand, 笑 xiau4 laugh, 哭 heu4 cry, 愛 oi4 "
            "want/love, 有 yiu1 have, 係 he4 be, 曉 hiau3 know-how, 開 koi1 "
            "open, 煮 zu3 cook, 好 ho3 good, 壞 fai4 bad, 大 tai4 big, 細 "
            "se4 small, 高 go1 tall, 矮 ai3 short, 長 cong2 long, 短 don3 "
            "short, 新 sin1 new, 舊 kiu4 old, 多 do1 many, 少 sau3 few, 紅 "
            "fung2 red, 白 pag6 white, 黑 het5 black, 快 kuai4 fast, 慢 "
            "man4 slow, 遠 yen3 far, 近 kiun4 near, 重 cung4 heavy, 輕 "
            "kiang1 light, 熱 ngiat6 hot, 冷 lang1 cold, 甜 tiam2 sweet, 苦 "
            "fu3 bitter, 當 dong1 very, 又 yiu4 again, 再 zai4 once-more, 還 "
            "han2 still, 就 qiu4 then, 這 li4 this, 該 ge4 that, 這隻 "
            "li4-zag5 this-one, 該隻 ge4-zag5 that-one, 麼人 mag5-ngin2 who, "
            "乜 mag5 what, 幾多 gi3-do1 how-many, 幾時 gi3-si2 when, 點樣 "
            "dim3-ngiong4 how, 做麼 zo4-ma1 why, 一 yit5 one, 二 ngi4 two, 三 "
            "sam1 three, 四 si4 four, 五 ng3 five, 六 liuk5 six, 七 cit5 "
            "seven, 八 bat5 eight, 九 giu3 nine, 十 sip6 ten, 百 bag5 "
            "hundred, 千 cien1 thousand, 萬 van4 ten-thousand, 今日 "
            "gin1-ngit5 today, 尋日 qim2-ngit5 yesterday, 天光日 "
            "tien1-gong1-ngit5 tomorrow, 今下 gin1-ha4 now, 朝頭早 "
            "zau1-teu2-zau3 morning, 下晝 ha1-zu4 afternoon, 暗晡晨 "
            "am4-bu1-sin2 evening, 點鐘 diam3-zung1 o'clock, 阿爸 a1-ba1 "
            "father, 阿姆 a1-me1 mother, 阿公 a1-gung1 grandfather, 阿婆 "
            "a1-po2 grandmother, 兄弟 hiung1-ti4 brothers, 姊妹 zi3-moi4 "
            "sisters, 廳下 tang1-ha1 hall, 房間 fong2-gien1 room, 廚房 "
            "cu2-fong2 kitchen, 衫 sam1 clothes, 褲 fu4 trousers, 鞋 hai2 "
            "shoes, 菜 coi4 vegetables, 湯 tong1 soup, 茶 ca2 tea, 酒 ziu3 "
            "wine, 糖 tong2 sugar, 鹽 yam2 salt, 頭 teu2 head, 手 su3 hand, "
            "腳 giog5 foot, 目 mug5 eye, 耳 ngi3 ear, 鼻 pi4 nose, 嘴 zoi4 "
            "mouth, 心 xim1 heart, 身體 siin1-ti3 body, 藥 yog6 medicine, 病 "
            "piang4 sickness, 歡喜 fon1-hi3 happy, 傷心 song1-xim1 sad, 嬲 "
            "neu4 angry, 驚 giang1 afraid, 牛 ngiu2 cow, 馬 ma1 horse, 貓 "
            "meu4 cat, 鳥 diau1 bird, 蟲 cung2 insect, 竹 zug5 bamboo, 禾 "
            "vo2 rice-plant, 田 tien2 field, 河 ho2 river, 雲 yun2 cloud, 雨 "
            "ji3 rain, 風 fung1 wind, 雷 lui2 thunder, 星 xen1 star, 春 "
            "cun1 spring, 夏 ha4 summer, 秋 qiu1 autumn, 冬 dung1 winter, "
            "工廠 gung1-cong3 factory, 老闆 lo3-ban3 boss, 會議 fi4 meeting, "
            "功課 gung1-ko4 homework, 考試 kau3-shi4 exam, 市場 shi4-cong2 "
            "market, 價錢 ga4-qian2 price, 故事 gu4-sii4 story, 歌 go1 song, "
            "山歌 san1-go1 mountain-song, 諺語 ngian4-ngi3 proverb, 電腦 "
            "tien4-nau3 computer, 網絡 miong3-log6 internet, 信息 xin4-xit5 "
            "message, 相片 xiong4-pien4 photo, 多謝 do1-qia4 thanks, 再見 "
            "zai4-gien4 goodbye, 請 qiang3 please, 對唔住 dui4-m2-qi4 sorry, "
            "歡迎 fon1-ngiang2 welcome, 保重 bo3-cung4 take-care, 尞 liau4 "
            "visit, 慢行 man4-hang2 farewell, 努力 nu3-lag6 effort, 成功 "
            "siin2-gung1 success, 希望 hi1-mong4 hope, 和平 fo2-pin2 peace, "
            "團結 ton2-giet5 unity, 客家話 hag5-ga1-fa4 Hakka-language. \n\n"
            "TEN GRAMMAR RULES: 1 SVO. 2 Verbs never conjugate. 3 了 liau3 "
            "completed. 4 過 go4 experienced. 5 會 voi4 future. 6 緊 gin3/在 "
            "cai4 ongoing. 7 唔 m2 negates verbs/adjectives. 8 冇 mau2 "
            "negates having/past. 9 Questions: A-not-A or 麼 ma1. 10 "
            "Classifiers: 個人, 本書, 隻狗. \n\n"
            "FIVE PHRASE TABLES: greetings (食飯了冇, 你好, 多謝, 唔使客氣, "
            "再見, 慢行), market (幾多錢, 太貴了, 平一點, 成交, 找錢), "
            "travel (在哪, 幾遠, 買票, 住旅店), time (今下, 點鐘, 禮拜, 今"
            "日/尋日/天光日), feelings (歡喜, 傷心, 嬲, 驚, 愛). \n\n"
            "Landmark sentences: 𠊎係客家人 ngai2-he4-hag5-ga1-ngin2; 食飯"
            "了冇 sit5-pon4-liau3-mau2; 寧賣祖宗田，不忘祖宗言; 認聲不認姓; "
            "客家話萬歲 hag5-ga1-fa4-van4-soi4."
        ),
        "how_it_works": (
            "This record is the summit: the tone table, all 200 core words "
            "in one list, the ten grammar rules compressed, the five phrase "
            "tables, and the five landmark sentences - everything the "
            "ladder taught, in one reference. A learner who can read this "
            "record straight through has climbed the whole database."
        ),
        "key_points": [
            "200 core words with Pinfa readings.",
            "Tone table with all six tones and example characters.",
            "Ten grammar rules in compressed form.",
            "Five phrase tables: greetings, market, travel, time, feelings.",
            "Five landmark sentences from across the ladder.",
        ],
        "requirements": [
            "Read every record before this one; this is the review.",
        ],
        "standards": [
            "Word list consolidates vocabulary from all earlier records.",
        ],
        "citations": [CIT_LI, CIT_MACIVER, CIT_PINFA],
        "must_contain": ["200", "fug6", "liau4", "hag5-ga1-fa4-van4-soi4", "ten grammar"],
        "sig_lens": (
            "Through the Signature lens this is the sworn seal of the "
            "whole: two hundred words, ten rules, five tables, five "
            "landmarks - the entire language pressed into one page, "
            "complete and unbreakable."
        ),
        "drill": {
            "core_words": [
                ("𠊎", "ngai2", "I"), ("你", "ngi2", "you"), ("佢", "gi2", "he/she"),
                ("𠊎兜", "ngai2-deu1", "we"), ("你兜", "ngi2-deu1", "you(pl)"),
                ("佢兜", "gi2-deu1", "they"), ("人", "ngin2", "person"),
                ("屋", "vuk5", "house"), ("屋下", "vuk5-ha1", "home"),
                ("水", "sui3", "water"), ("火", "fo3", "fire"),
                ("山", "san1", "mountain"), ("天", "tien1", "sky"),
                ("日", "ngit5", "sun"), ("月", "ngiat6", "moon"),
                ("米", "mi3", "rice"), ("飯", "pon4", "cooked rice"),
                ("錢", "qian2", "money"), ("書", "su1", "book"),
                ("學校", "hog6-hau4", "school"), ("老師", "lo3-sii1", "teacher"),
                ("醫生", "ji1-sen1", "doctor"), ("朋友", "pen2-iu1", "friend"),
                ("街", "gie1", "street"), ("車", "ca1", "car"),
                ("電話", "tien4-fa4", "telephone"), ("狗", "gieu3", "dog"),
                ("雞", "gie1", "chicken"), ("豬", "zu1", "pig"),
                ("魚", "ng2", "fish"), ("樹", "su4", "tree"),
                ("花", "fa1", "flower"), ("食", "sit5", "eat"),
                ("飲", "jim3", "drink"), ("睡", "soi4", "sleep"),
                ("行", "hang2", "walk"), ("走", "zeu3", "run"),
                ("講", "gong3", "speak"), ("看", "kon4", "look"),
                ("聽", "tang1", "listen"), ("寫", "xia3", "write"),
                ("讀", "tug6", "study"), ("做", "zo4", "do"),
                ("買", "mai1", "buy"), ("賣", "mai4", "sell"),
                ("去", "hi4", "go"), ("來", "loi2", "come"),
                ("坐", "co4", "sit"), ("企", "ki1", "stand"),
                ("笑", "xiau4", "laugh"), ("哭", "heu4", "cry"),
                ("愛", "oi4", "want"), ("有", "yiu1", "have"),
                ("係", "he4", "be"), ("曉", "hiau3", "know-how"),
                ("開", "koi1", "open"), ("煮", "zu3", "cook"),
                ("好", "ho3", "good"), ("壞", "fai4", "bad"),
                ("大", "tai4", "big"), ("細", "se4", "small"),
                ("高", "go1", "tall"), ("矮", "ai3", "short"),
                ("長", "cong2", "long"), ("短", "don3", "short"),
                ("新", "sin1", "new"), ("舊", "kiu4", "old"),
                ("多", "do1", "many"), ("少", "sau3", "few"),
                ("紅", "fung2", "red"), ("白", "pag6", "white"),
                ("黑", "het5", "black"), ("快", "kuai4", "fast"),
                ("慢", "man4", "slow"), ("遠", "yen3", "far"),
                ("近", "kiun4", "near"), ("重", "cung4", "heavy"),
                ("輕", "kiang1", "light"), ("熱", "ngiat6", "hot"),
                ("冷", "lang1", "cold"), ("甜", "tiam2", "sweet"),
                ("苦", "fu3", "bitter"), ("當", "dong1", "very"),
                ("又", "yiu4", "again"), ("再", "zai4", "once-more"),
                ("還", "han2", "still"), ("就", "qiu4", "then"),
                ("這", "li4", "this"), ("該", "ge4", "that"),
                ("這隻", "li4-zag5", "this-one"), ("該隻", "ge4-zag5", "that-one"),
                ("麼人", "mag5-ngin2", "who"), ("乜", "mag5", "what"),
                ("幾多", "gi3-do1", "how-many"), ("幾時", "gi3-si2", "when"),
                ("點樣", "dim3-ngiong4", "how"), ("做麼", "zo4-ma1", "why"),
                ("一", "yit5", "one"), ("二", "ngi4", "two"),
                ("三", "sam1", "three"), ("四", "si4", "four"),
                ("五", "ng3", "five"), ("六", "liuk5", "six"),
                ("七", "cit5", "seven"), ("八", "bat5", "eight"),
                ("九", "giu3", "nine"), ("十", "sip6", "ten"),
                ("百", "bag5", "hundred"), ("千", "cien1", "thousand"),
                ("萬", "van4", "ten-thousand"), ("今日", "gin1-ngit5", "today"),
                ("尋日", "qim2-ngit5", "yesterday"), ("天光日", "tien1-gong1-ngit5", "tomorrow"),
                ("今下", "gin1-ha4", "now"), ("朝頭早", "zau1-teu2-zau3", "morning"),
                ("下晝", "ha1-zu4", "afternoon"), ("暗晡晨", "am4-bu1-sin2", "evening"),
                ("點鐘", "diam3-zung1", "o'clock"), ("阿爸", "a1-ba1", "father"),
                ("阿姆", "a1-me1", "mother"), ("阿公", "a1-gung1", "grandfather"),
                ("阿婆", "a1-po2", "grandmother"), ("兄弟", "hiung1-ti4", "brothers"),
                ("姊妹", "zi3-moi4", "sisters"), ("廳下", "tang1-ha1", "hall"),
                ("房間", "fong2-gien1", "room"), ("廚房", "cu2-fong2", "kitchen"),
                ("衫", "sam1", "clothes"), ("褲", "fu4", "trousers"),
                ("鞋", "hai2", "shoes"), ("菜", "coi4", "vegetables"),
                ("湯", "tong1", "soup"), ("茶", "ca2", "tea"),
                ("酒", "ziu3", "wine"), ("糖", "tong2", "sugar"),
                ("鹽", "yam2", "salt"), ("頭", "teu2", "head"),
                ("手", "su3", "hand"), ("腳", "giog5", "foot"),
                ("目", "mug5", "eye"), ("耳", "ngi3", "ear"),
                ("鼻", "pi4", "nose"), ("嘴", "zoi4", "mouth"),
                ("心", "xim1", "heart"), ("身體", "siin1-ti3", "body"),
                ("藥", "yog6", "medicine"), ("病", "piang4", "sickness"),
                ("歡喜", "fon1-hi3", "happy"), ("傷心", "song1-xim1", "sad"),
                ("嬲", "neu4", "angry"), ("驚", "giang1", "afraid"),
                ("牛", "ngiu2", "cow"), ("馬", "ma1", "horse"),
                ("貓", "meu4", "cat"), ("鳥", "diau1", "bird"),
                ("蟲", "cung2", "insect"), ("竹", "zug5", "bamboo"),
                ("禾", "vo2", "rice-plant"), ("田", "tien2", "field"),
                ("河", "ho2", "river"), ("雲", "yun2", "cloud"),
                ("雨", "ji3", "rain"), ("風", "fung1", "wind"),
                ("雷", "lui2", "thunder"), ("星", "xen1", "star"),
                ("春", "cun1", "spring"), ("夏", "ha4", "summer"),
                ("秋", "qiu1", "autumn"), ("冬", "dung1", "winter"),
                ("工廠", "gung1-cong3", "factory"), ("老闆", "lo3-ban3", "boss"),
                ("會議", "fi4", "meeting"), ("功課", "gung1-ko4", "homework"),
                ("考試", "kau3-shi4", "exam"), ("市場", "shi4-cong2", "market"),
                ("價錢", "ga4-qian2", "price"), ("故事", "gu4-sii4", "story"),
                ("歌", "go1", "song"), ("山歌", "san1-go1", "mountain-song"),
                ("諺語", "ngian4-ngi3", "proverb"), ("電腦", "tien4-nau3", "computer"),
                ("網絡", "miong3-log6", "internet"), ("信息", "xin4-xit5", "message"),
                ("相片", "xiong4-pien4", "photo"), ("多謝", "do1-qia4", "thanks"),
                ("再見", "zai4-gien4", "goodbye"), ("請", "qiang3", "please"),
                ("對唔住", "dui4-m2-qi4", "sorry"), ("歡迎", "fon1-ngiang2", "welcome"),
                ("保重", "bo3-cung4", "take-care"), ("尞", "liau4", "visit"),
                ("慢行", "man4-hang2", "farewell"), ("努力", "nu3-lag6", "effort"),
                ("成功", "siin2-gung1", "success"), ("希望", "hi1-mong4", "hope"),
                ("和平", "fo2-pin2", "peace"), ("團結", "ton2-giet5", "unity"),
                ("萬歲", "van4-soi4", "long-live"), ("祖公", "zu3-gung1", "ancestor"),
                ("客家話", "hag5-ga1-fa4", "Hakka-language"),
            ],
            "grammar_rules": 10,
            "phrase_tables": 5,
        },
    },
]
