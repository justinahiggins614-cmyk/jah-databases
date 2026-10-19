#!/usr/bin/env python3
"""Entries for the Javanese to English databases (Manon's language orders #10-12,
2026-10-17, roster rank 22).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,602 databases):
zero 'javanese' hits, zero id_prefix values containing 'LJAV'. ID prefixes
JAH-LJAV- (public) and JAH-LJAVS- (signature) verified free across manifest
id_prefix values AND all shard index IDs in jah-databases-data-1.
Pre-authoring whole-system dedupe-gate check over all 68 planned titles
(34 records + 34 Signature Edition titles): zero collisions, zero refusals.

This build creates two NEW databases, 34 ladder-ordered records each:

  language-javanese              - The Javanese to English Database
                                   (public-harvest: real, fact-checked
                                   Javanese (Basa Jawa) - overview, the
                                   Hanacaraka writing system, phonology,
                                   core vocabulary with sentences,
                                   grammar essentials, themed sentence
                                   sets, verb tense/aspect, questions and
                                   answers, commands, descriptions,
                                   stories, idioms, registers, complex
                                   sentences, conversations, mastery
                                   reference; every line in Javanese
                                   with romanization and English;
                                   standard references Robson & Wibisono
                                   2002, Errington 1988, Uhlenbeck 1978,
                                   Ogloblin 2005, ISO 639-3 jav)
  language-javanese-signature    - The Javanese to English Signature Database
                                   (his original Signature Language Method:
                                   the speech levels as sworn covenants of
                                   respect; src signature, titles suffixed
                                   " (Signature Edition)", clearly labeled
                                   Signature-made, never presented as
                                   authentic public record)

34 records each, ladder-ranked 1-34 (simple -> compounded -> most complex),
ladder_tier foundations (1-3) / compounded (4-20) / advanced (21-34); the
shard index is written in ladder order so pages present simple -> complex.

Every record carries Javanese content + romanization + English translation +
example sentences. Sentences are required in EVERY record - no
vocabulary-list-only records.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_javanese.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before writing.

Build-time cross-check: every entry declares 'must_contain' strings and the
build asserts each one appears verbatim in the record description, so entry
text and demo outputs can never drift apart.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "the speech levels are sworn covenants of respect, every word "
            "chooses its rank, every sentence keeps the peace. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_ROBSON = ("Robson S.O., Wibisono S. Javanese-English Dictionary. "
              "Periplus Editions; 2002.")
CIT_ERRINGTON = ("Errington J.J. Language in the World of Javanese. "
                 "Ohio University Center for International Studies; 1988.")
CIT_UHLENBECK = ("Uhlenbeck E.M. Studies in Javanese Morphology. "
                 "Martinus Nijhoff; 1978.")
CIT_OGLOBLIN = ("Ogloblin A.K. Javanese. In Adelaar K.A., Himmelmann N.P. "
                "(eds.), The Austronesian Languages of Asia and Madagascar. "
                "Routledge; 2005.")
CIT_ISO639 = ("ISO 639-3 code jav (Javanese); ISO 639-1 code jv.")
CIT_SPEAKERS = ("Speaker figures are best-available estimates, rounded, per "
                "the roster note: about 68 million native speakers.")


def _num_lines(items):
    """Numbered Javanese -> English sentence lines for descriptions."""
    out = []
    for i, (jv, en) in enumerate(items, 1):
        out.append("%d. %s - %s" % (i, jv, en))
    return "\n".join(out)


# ------------------------------------------------------------------ drills

OVERVIEW_SENTS = [
    ("Aku wong Jawa.", "I am Javanese."),
    ("Basa Jawa iku basa ibuku.", "Javanese is my mother tongue."),
]
NOUNS25 = [
    ("wong", "person"), ("bocah", "child"), ("lanang", "man"),
    ("wadon", "woman"), ("omah", "house"), ("lawang", "door"),
    ("jendhela", "window"), ("meja", "table"), ("kursi", "chair"),
    ("banyu", "water"), ("sego", "rice / a meal"), ("iwak", "fish / meat"),
    ("woh", "fruit"), ("wit", "tree"), ("kembang", "flower"),
    ("srengenge", "sun"), ("rembulan", "moon"), ("lintang", "star"),
    ("langit", "sky"), ("lemah", "earth / soil"), ("dalan", "road"),
    ("pasar", "market"), ("kutha", "city"), ("desa", "village"),
    ("negara", "country"),
]
VERBS25 = [
    ("mangan", "eat"), ("ngombe", "drink"), ("turu", "sleep"),
    ("tangi", "wake up"), ("mlaku", "walk"), ("mlayu", "run"),
    ("lungguh", "sit"), ("ngadeg", "stand"), ("omong", "speak"),
    ("takon", "ask"), ("maca", "read"), ("nulis", "write"),
    ("tuku", "buy"), ("adol", "sell"), ("gawe", "make"),
    ("adus", "bathe"), ("ngguyu", "laugh"), ("nangis", "cry"),
    ("lunga", "go"), ("teka", "come"), ("mulih", "go home"),
    ("kerja", "work"), ("sinau", "study"), ("dolan", "visit / play"),
    ("ndeleng", "see / watch"),
]
ADJ25 = [
    ("apik", "good"), ("ala", "bad"), ("gedhe", "big"), ("cilik", "small"),
    ("dawa", "long"), ("cendhak", "short"), ("dhuwur", "tall / high"),
    ("asor", "low"), ("anyar", "new"), ("lawas", "old (thing)"),
    ("enom", "young"), ("tuwa", "old (person)"), ("ayu", "beautiful"),
    ("pinter", "smart"), ("sugih", "rich"), ("mlarat", "poor"),
    ("panas", "hot"), ("adhem", "cold"), ("legi", "sweet"),
    ("pait", "bitter"), ("asin", "salty"), ("pedhes", "spicy"),
    ("abot", "heavy"), ("entheng", "light"), ("cepet", "fast"),
]
ADV15 = [
    ("banget", "very"), ("luwih", "more"), ("paling", "most"),
    ("wis", "already"), ("durung", "not yet"), ("lagi", "currently"),
    ("arep", "about to"), ("mesthi", "certainly"), ("mbokmenawa", "maybe"),
    ("saben", "every"), ("saiki", "now"), ("wingi", "yesterday"),
    ("sesuk", "tomorrow"), ("alon-alon", "slowly"), ("tenan", "really"),
]
NUMBERS = [
    (1, "siji", "setunggal"), (2, "loro", "kalih"), (3, "telu", "tiga"),
    (4, "papat", "sekawan"), (5, "lima", "gangsal"), (6, "enem", "enem"),
    (7, "pitu", "pitu"), (8, "wolu", "wolu"), (9, "sanga", "sanga"),
    (10, "sepuluh", "sedasa"), (11, "sewelas", "sewelas"),
    (12, "rolas", "rolas"), (20, "rong puluh", "kalih dasa"),
    (21, "selikur", "selikur"), (25, "selawe", "selawe"),
    (30, "telung puluh", "tigang dasa"), (50, "seket", "seket"),
    (60, "sewidak", "sewidak"), (100, "satus", "setunggal atus"),
    (1000, "sewu", "sewu"),
]
DAYS = ["Senen", "Selasa", "Rebo", "Kemis", "Jemuwah", "Setu", "Minggu"]
MONTHS_JV = ["Sura", "Sapar", "Mulud", "Bakdamulud", "Jumadilawal",
             "Jumadilakir", "Rejeb", "Ruwah", "Poso", "Sawal", "Selo",
             "Besar"]
GREET30 = [
    ("Sugeng enjing.", "Good morning."),
    ("Sugeng siang.", "Good midday."),
    ("Sugeng sonten.", "Good afternoon."),
    ("Sugeng dalu.", "Good evening / night."),
    ("Wilujeng rawuh.", "Welcome."),
    ("Matur nuwun.", "Thank you."),
    ("Nuwun sewu.", "Excuse me (asking permission)."),
    ("Nyuwun pangapunten.", "I ask forgiveness (sorry)."),
    ("Monggo.", "Please go ahead / please come in."),
    ("Sugeng tindak.", "Safe travels (farewell)."),
    ("Piye kabare?", "How are you?"),
    ("Apik-apik wae.", "Just fine."),
    ("Sampun nedha?", "Have you eaten?"),
    ("Ati-ati.", "Be careful."),
    ("Sugeng sare.", "Good night (sleep well)."),
    ("Sugeng ambal warsa.", "Happy birthday."),
    ("Sugeng riyadi.", "Happy Eid (Lebaran greeting)."),
    ("Wilujeng Natal.", "Merry Christmas."),
    ("Inggih.", "Yes (polite)."),
    ("Mboten.", "No (polite)."),
    ("Kula nuwun.", "I humbly ask permission (entering)."),
    ("Sugeng pinanggih.", "Nice to meet you."),
    ("Sugeng enjang tindak.", "Have a good morning trip."),
    ("Matur nuwun sanget.", "Thank you very much."),
    ("Sami-sami.", "You are welcome."),
    ("Pangapunten, kula kesah rumiyin.", "Excuse me, I will leave first."),
    ("Nganti ketemu maneh.", "Until we meet again."),
    ("Sugeng dalu, sugeng sare.", "Good evening, sleep well."),
    ("Wilujeng mangun.", "Welcome back / safe arrival."),
    ("Amit-amit.", "Far be it (warding off bad luck)."),
]

ENTRIES = [
    {
        "key": "overview",
        "name": "Javanese Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Javanese (Basa Jawa) is the Austronesian language of the "
            "Malayo-Polynesian branch spoken as a mother tongue by about "
            "68 million people, the largest native-speaker community of any "
            "Austronesian language. With second-language users the total "
            "passes 80 million. It is the first language of Central Java, "
            "East Java, and the Yogyakarta Special Region of Indonesia, "
            "with speaker communities in Banten, Cirebon, Lampung "
            "(transmigrants), and the historic diaspora of Suriname and "
            "New Caledonia.\n"
            "Indonesian is the national official language; Javanese is the "
            "language of home, market, ceremony, and literature across "
            "Java, used in regional schooling and local government. The "
            "prestige standard is the Central Javanese of Surakarta and "
            "Yogyakarta; other major dialects are Western Javanese "
            "(Banyumasan, Cirebon), Eastern Javanese (Surabaya, Malang), "
            "plus Tengger and Osing.\n"
            "Key facts a learner should hold from day one: (1) Javanese "
            "has speech levels - ngoko (informal), madya (middle), krama "
            "(polite), krama inggil (honorific) - and choosing the right "
            "level is choosing the right respect; (2) the language builds "
            "words with rich affixes (di-, ke-, -an, -ke, um-, -in-) around "
            "a root; (3) there is no grammatical gender, no case, and no "
            "verb conjugation for person - one verb form serves all "
            "subjects; (4) the basic sentence order is subject-verb-object, "
            "like English. Example: " +
            _num_lines(OVERVIEW_SENTS)
        ),
        "how_it_works": (
            "Javanese works as a root-and-affix system inside a "
            "respect-ranked vocabulary. The root carries the core idea - "
            "for example mangan (eat) - and affixes steer it: dipangan "
            "(eaten, passive), panganan (food, the thing eaten), mangan "
            "becik (eat well). Parallel to this, nearly every everyday "
            "word has a level twin: mangan (ngoko) vs dhahar (krama) for "
            "\"eat\", aku (ngoko) vs kula (krama) for \"I\". A speaker "
            "runs two gears at once - affixes for grammar, levels for "
            "respect. Learn the root families and the level pairs "
            "together and the whole language starts to unfold."
        ),
        "key_points": [
            "Javanese (Basa Jawa): Austronesian family, Malayo-Polynesian branch.",
            "About 68 million native speakers; over 80 million total - the largest Austronesian native community.",
            "First language of Central Java, East Java, Yogyakarta; diaspora in Suriname and New Caledonia.",
            "Indonesian is the national official language; Javanese rules home, market, ceremony, and literature.",
            "Prestige standard: Central Javanese (Surakarta/Yogyakarta); Western, Eastern, Tengger, Osing dialects.",
            "Speech levels ngoko/madya/krama/krama inggil: respect is built into word choice.",
            "Rich affix system (di-, ke-, -an, -ke, um-, -in-) around a stable root.",
            "No gender, no case, no person conjugation; subject-verb-object order.",
        ],
        "requirements": [
            "No prior knowledge of Javanese is assumed; the writing system record comes next.",
            "Accept that one idea has two or three words - the level, not the meaning, decides.",
            "Learn roots and affixes, not just whole words.",
        ],
        "standards": [
            "ISO 639-1 code jv; ISO 639-3 code jav.",
            "Romanization in this database follows modern Indonesian-based Javanese orthography.",
            "Speaker figures are best-available estimates, rounded, per the roster note.",
        ],
        "citations": [CIT_OGLOBLIN, CIT_ERRINGTON, CIT_ISO639, CIT_SPEAKERS],
        "sig_lens": (
            "The Signature read: Javanese is the Language of Sworn Respect "
            "- a system where every word bows or stands tall according to "
            "rank. The Signature Language Method learns Javanese the way "
            "Java teaches it: level first, word second, sentence last. "
            "Every letter a sworn mark of courtesy, every affix a family "
            "bond, every sentence a covenant of peace between speaker and "
            "listener."
        ),
        "drill": {
            "native_m": 68, "total_m": 84, "dialects": 6,
            "levels": 4, "scripts": 3,
        },
        "must_contain": ["68", "Austronesian", "Malayo-Polynesian", "Basa Jawa"],
    },
    {
        "key": "writing",
        "name": "The Javanese Writing System",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Javanese is written today mainly in the Latin alphabet with "
            "Indonesian-based spelling (dj became j, oe became u, tj "
            "became c after the 1972 spelling reform - so old \"Djogja\" "
            "is now \"Jogja\"). The traditional script is Aksara Jawa, "
            "the Hanacaraka abugida descended from the Kawi script of "
            "old Java, where each consonant letter carries an inherent "
            "vowel /a/.\n"
            "The 20 basic letters (aksara nglegena), in the famous "
            "Hanacaraka teaching order - itself a four-line poem telling "
            "how Aji Saka's two messengers quarreled and both died:\n"
            "ha na ca ra ka / da ta sa wa la / pa dha ja ya nya / ma ga "
            "ba tha nga.\n"
            "Vowels are written with sandhangan diacritics around the "
            "consonant; a pangkon kills the inherent vowel at a word's "
            "end. Murda letters serve as capitals, swara letters write "
            "standalone vowels, and pasangan conjuncts stack a second "
            "consonant under the first. A third script, Pegon "
            "(Arabic-based), was used for Islamic texts in the "
            "pesantren schools.\n"
            "Traditional digits: 0123456789 (0-9), written in Hanacaraka "
            "as ꧐ ꧑ ꧒ ꧓ ꧔ ꧕ ꧖ ꧗ ꧘ ꧙. Punctuation "
            "includes pada lingsa (comma-like) and pada lungsi (period-like). "
            "Example sentence: aku mangan sega (I eat rice), in Hanacaraka "
            "written with the ha-na-ca-ra-ka letters."
        ),
        "how_it_works": (
            "Reading Hanacaraka means reading consonant-vowel blocks, not "
            "letters. Train on the four facts that matter: (1) each "
            "aksara reads consonant + a (ha, na, ca...); (2) sandhangan "
            "marks change the vowel - wulu makes i, suku makes u, taling "
            "makes e, pepet makes the mid vowel; (3) a pangkon silences "
            "the final a so a word can end in a consonant; (4) the Latin "
            "spelling is phonetic enough to start speaking on day one - "
            "one letter, one sound, with dh/th as retroflex t/d and ny/ng "
            "as single sounds. Master the Latin layer first, then learn "
            "the 20 aksara through the Hanacaraka poem itself."
        ),
        "key_points": [
            "Latin script is the everyday standard, using Indonesian-based spelling.",
            "Aksara Jawa (Hanacaraka) is the traditional abugida: 20 basic letters, each consonant + inherent /a/.",
            "The Hanacaraka order is a poem: hana caraka, data sawala, padha jayanya, maga bathanga.",
            "Sandhangan diacritics change vowels; pangkon kills the final inherent vowel.",
            "Murda (capitals), swara (vowel letters), pasangan (conjuncts) complete the set.",
            "Pegon (Arabic-based) script served Islamic texts in pesantren schools.",
            "Traditional digits 0-9 in Hanacaraka; pada lingsa and pada lungsi punctuate.",
            "Direction is left to right in both Latin and Hanacaraka.",
        ],
        "requirements": [
            "Learn the Latin spelling layer before the traditional script.",
            "Memorize the 20 aksara through the four-line Hanacaraka poem.",
            "Practice ny, ng, dh, th as single sounds, not letter pairs.",
        ],
        "standards": [
            "Latin orthography follows the 1972 Indonesian spelling reform conventions.",
            "Hanacaraka letter order follows the traditional hana-caraka sequence.",
        ],
        "citations": [CIT_ROBSON, CIT_UHLENBECK, CIT_ISO639],
        "sig_lens": (
            "The Signature read: every aksara is a sworn mark - the "
            "Hanacaraka poem is a covenant story, two messengers who kept "
            "their duty unto death. The Signature Language Method treats "
            "each letter as a mark of honor: ha stands guard, na "
            "remembers, ca watches, and the line marches on. Learn the "
            "letters as the poem tells them and the script memorizes "
            "itself."
        ),
        "drill": {
            "aksara": 20, "murda": 8, "digits": 10,
            "poem_lines": 4, "scripts": 3,
            "aksara_order": ["ha", "na", "ca", "ra", "ka", "da", "ta",
                             "sa", "wa", "la", "pa", "dha", "ja", "ya",
                             "nya", "ma", "ga", "ba", "tha", "nga"],
        },
        "must_contain": ["Hanacaraka", "20", "sandhangan", "pangkon"],
    },
    {
        "key": "phonology",
        "name": "Javanese Pronunciation and Phonology",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Javanese has 6 vowels: /i u e o a/ plus the mid central "
            "pepet /e/ (written e, as in sego). In closed syllables the "
            "high vowels lower slightly, and a in an open final syllable "
            "rounds toward o - ana (there is) sounds like \"ono\", apa "
            "(what) like \"opo\". There is no lexical tone; stress falls "
            "on the penultimate syllable.\n"
            "The consonants pair voiced and voiceless: p/b, t/d, "
            "retroflex th/dh, palatal c/j, k/g, plus s, h, m, n, ny, ng, "
            "r, l, w, y. A word may not end in a voiced stop, so final "
            "b/d/g neutralize.\n"
            "Twelve spoken examples with English approximations:\n"
            "1. sego (seh-GAW) - rice / a meal; 2. banyu (BAHN-yoo) - "
            "water; 3. omah (AW-mah) - house; 4. mangan (MAH-ngahn) - "
            "eat; 5. turu (TOO-roo) - sleep; 6. mlaku (mlah-KOO) - walk; "
            "7. apik (AH-pik) - good; 8. gedhe (geh-DHEH) - big; 9. ayu "
            "(AH-yoo) - beautiful; 10. matur nuwun (mah-TOOR noo-WOON) - "
            "thank you; 11. sugeng enjing (soo-GENG EN-jing) - good "
            "morning; 12. piye (pee-YEH) - how. Note ana, the word for "
            "\"there is\", rounds its final a toward o in careful speech."
        ),
        "how_it_works": (
            "Pronunciation works through three habits: (1) keep the six "
            "vowels distinct - especially pepet e (sego) vs taling e "
            "(enjing); (2) round final-syllable a toward o (ana becomes "
            "\"ono\" in careful Central speech); (3) hit the retroflex "
            "th/dh with the tongue curled back - gedhe, dhahar. Stress the "
            "penultimate syllable and let questions rise at the end. "
            "Shadow the twelve example words aloud, recording yourself, "
            "until sego, banyu, and matur nuwun come out without thinking."
        ),
        "key_points": [
            "Six vowels /i u e o a/ plus pepet; pepet e is the mid central vowel.",
            "Final-syllable a rounds toward o: ana sounds like \"ono\".",
            "Consonant pairs p/b, t/d, retroflex th/dh, c/j, k/g; plus ny, ng.",
            "No voiced stop may end a word - final b/d/g neutralize.",
            "No lexical tone; stress is penultimate.",
            "dh/th are single retroflex sounds, ny/ng single sounds.",
            "Question intonation rises at the end of the sentence.",
            "12 example words with English approximations anchor the ear.",
        ],
        "requirements": [
            "Drill the six vowels in pairs, pepet vs taling first.",
            "Practice the a-to-o rounding in open final syllables.",
            "Curl the tongue for retroflex dh/th until gedhe sounds right.",
        ],
        "standards": [
            "Phoneme counts follow Ogloblin 2005: 6 vowels, 21 consonants.",
            "Approximations are teaching aids, not phonetic transcription.",
        ],
        "citations": [CIT_OGLOBLIN, CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the ear is the first sworn guard of the "
            "language. Six vowels stand like six sentries; the pepet "
            "holds the middle post that no other vowel may take. The "
            "Signature Language Method trains the tongue as a covenant "
            "drill - repeat, record, compare - until the sounds swear "
            "allegiance and never desert you."
        ),
        "drill": {
            "vowels": 6, "consonants": 21, "examples": 12,
            "pairs": [["p", "b"], ["t", "d"], ["th", "dh"], ["c", "j"],
                      ["k", "g"]],
        },
        "must_contain": ["pepet", "retroflex", "penultimate", "ana"],
    },
    {
        "key": "nouns1",
        "name": "Core Javanese Nouns I",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Twenty-five essential nouns - people, places, things - each "
            "with a full example sentence in Javanese and English. 25 nouns "
            "in 25 sentences:\n" +
            _num_lines([
                ("Wong iku apik.", "That person is good. (wong - person)"),
                ("Bocah-bocah padha dolan.", "The children are playing. (bocah - child)"),
                ("Lanang iku adhiku.", "That man is my younger sibling. (lanang - man)"),
                ("Wadon iku ibuku.", "That woman is my mother. (wadon - woman)"),
                ("Omahku gedhe.", "My house is big. (omah - house)"),
                ("Lawange ditutup.", "The door is closed. (lawang - door)"),
                ("Jendhelane dibukak.", "The window is opened. (jendhela - window)"),
                ("Meja iki resik.", "This table is clean. (meja - table)"),
                ("Kursine anyar.", "The chair is new. (kursi - chair)"),
                ("Banyune adhem.", "The water is cold. (banyu - water)"),
                ("Segone legi.", "The rice is sweet. (sego - rice/meal)"),
                ("Iwake seger.", "The fish is fresh. (iwak - fish/meat)"),
                ("Wohe legi banget.", "The fruit is very sweet. (woh - fruit)"),
                ("Wit iku dhuwur.", "That tree is tall. (wit - tree)"),
                ("Kembange ayu.", "The flower is beautiful. (kembang - flower)"),
                ("Srengengene panas.", "The sun is hot. (srengenge - sun)"),
                ("Rembulane padhang.", "The moon is bright. (rembulan - moon)"),
                ("Lintange akeh.", "The stars are many. (lintang - star)"),
                ("Langite biru.", "The sky is blue. (langit - sky)"),
                ("Lemahe subur.", "The soil is fertile. (lemah - earth/soil)"),
                ("Dalane rame.", "The road is busy. (dalan - road)"),
                ("Pasare adoh.", "The market is far. (pasar - market)"),
                ("Kuthane gedhe.", "The city is big. (kutha - city)"),
                ("Desaku ayem.", "My village is peaceful. (desa - village)"),
                ("Negara iki makmur.", "This country is prosperous. (negara - country)"),
            ])
        ),
        "how_it_works": (
            "Javanese nouns do not change for number, gender, or case - "
            "wong means person, people, the person, depending on context. "
            "Definiteness rides on the -e suffix (wonge, the person) or "
            "the demonstratives iki/iku/kae; plurality rides on "
            "reduplication (bocah-bocah, children) or words like akeh "
            "(many) and para (plural for people). Possession attaches "
            "-ku/-mu/-ne: omahku (my house), omahmu (your house), omahe "
            "(his/her house). Learn each noun with its -e definite form "
            "and one reduplicated plural and you own the noun system."
        ),
        "key_points": [
            "Nouns never inflect for number, gender, or case.",
            "-e marks definiteness: omah (a house) vs omahe (the house).",
            "Reduplication marks plurality: bocah-bocah (children).",
            "iki (this), iku (that), kae (that over there) point nouns out.",
            "-ku/-mu/-ne attach possession directly to the noun.",
            "25 essential nouns, each in a full translated sentence.",
            "Context, not endings, decides singular vs plural vs definite.",
        ],
        "requirements": [
            "Say each noun aloud with its -e definite form.",
            "Build the plural by reduplication for five of the nouns.",
            "Attach -ku, -mu, -ne to omah, meja, and banyu from memory.",
        ],
        "standards": [
            "Noun forms follow the Central Javanese standard (Surakarta/Yogyakarta).",
            "Glosses follow Robson & Wibisono 2002.",
        ],
        "citations": [CIT_ROBSON, CIT_UHLENBECK],
        "sig_lens": (
            "The Signature read: the noun is the sworn ground of the "
            "sentence - unchanging, unbent by number or rank. Omah stands "
            "whether one house or a hundred. The Signature Language "
            "Method plants nouns like foundation stones: learn the stone, "
            "then learn what can be built on it - the -e that points, "
            "the doubling that multiplies, the -ku that claims."
        ),
        "drill": {"nouns": [n for n, _ in NOUNS25]},
        "must_contain": ["wong", "Bocah-bocah", "Omahku", "25"],
    },
    {
        "key": "verbs1",
        "name": "Core Javanese Verbs I",
        "group": "Core Vocabulary",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty-five essential verbs - each with a full example "
            "sentence in Javanese and English. 25 verbs in 25 sentences. "
            "One verb form serves every subject; time comes from helper "
            "words (wis, lagi, arep), not from conjugation:\n" +
            _num_lines([
                ("Aku mangan sego.", "I eat rice. (mangan - eat)"),
                ("Dheweke ngombe banyu.", "He/she drinks water. (ngombe - drink)"),
                ("Bocah iku turu.", "That child sleeps. (turu - sleep)"),
                ("Aku tangi esuk.", "I wake up in the morning. (tangi - wake up)"),
                ("Kita mlaku-mlaku.", "We take a walk. (mlaku - walk)"),
                ("Jaran iku mlayu banter.", "That horse runs fast. (mlayu - run)"),
                ("Monggo lungguh.", "Please sit down. (lungguh - sit)"),
                ("Dheweke ngadeg ing ngarep.", "He/she stands in front. (ngadeg - stand)"),
                ("Aku omong Jawa.", "I speak Javanese. (omong - speak)"),
                ("Aku takon marang guru.", "I ask the teacher. (takon - ask)"),
                ("Dheweke maca buku.", "He/she reads a book. (maca - read)"),
                ("Aku nulis layang.", "I write a letter. (nulis - write)"),
                ("Ibuku tuku iwak.", "My mother buys fish. (tuku - buy)"),
                ("Bapak adol beras.", "Father sells rice. (adol - sell)"),
                ("Dheweke gawe omah.", "He/she builds a house. (gawe - make)"),
                ("Aku adus esuk.", "I bathe in the morning. (adus - bathe)"),
                ("Bocah-bocah padha ngguyu.", "The children laugh. (ngguyu - laugh)"),
                ("Adhiku nangis.", "My younger sibling cries. (nangis - cry)"),
                ("Aku lunga menyang pasar.", "I go to the market. (lunga - go)"),
                ("Tamu wis teka.", "The guest has arrived. (teka - come)"),
                ("Aku mulih sore.", "I go home in the afternoon. (mulih - go home)"),
                ("Bapak kerja ing kantor.", "Father works at the office. (kerja - work)"),
                ("Aku sinau basa Jawa.", "I study Javanese. (sinau - study)"),
                ("Aku dolan menyang omahe kanca.", "I visit my friend's house. (dolan - visit/play)"),
                ("Kita ndeleng wayang.", "We watch a shadow-puppet play. (ndeleng - see/watch)"),
            ])
        ),
        "how_it_works": (
            "The Javanese verb never changes for I, you, he, we, or they "
            "- mangan is eat for every subject. Instead, nasal prefixes "
            "(mangan from pangan, nulis from tulis) mark the active voice, "
            "di- marks the passive (dipangan, eaten), and time words do "
            "the tense work: wis mangan (already ate), lagi mangan "
            "(eating now), arep mangan (will eat). Learn the root, learn "
            "the three time words, and you can place any action in past, "
            "present, or future without a single conjugation table."
        ),
        "key_points": [
            "One verb form serves all subjects - no person conjugation.",
            "Nasal prefix marks active voice: tulis -> nulis.",
            "di- marks passive voice: dipangan (eaten).",
            "wis / lagi / arep place the verb in past / present / future.",
            "25 essential verbs, each in a full translated sentence.",
            "Roots stay stable; helpers and affixes do the grammar work.",
        ],
        "requirements": [
            "Pair each verb with wis, lagi, arep - no conjugation needed.",
            "Convert five active sentences to di- passive.",
            "Memorize the 25 verbs with their English meanings cold.",
        ],
        "standards": [
            "Verb forms follow the Central Javanese standard.",
            "Glosses follow Robson & Wibisono 2002.",
        ],
        "citations": [CIT_ROBSON, CIT_UHLENBECK],
        "sig_lens": (
            "The Signature read: the verb is the sworn action - one form, "
            "unyielding, serving every subject equally. Mangan does not "
            "bow to I or swell for they. The Signature Language Method "
            "teaches verbs as standing orders: learn the order once, then "
            "the three time-words march it into past, present, and "
            "future."
        ),
        "drill": {"verbs": [v for v, _ in VERBS25]},
        "must_contain": ["mangan", "wis", "arep", "25"],
    },
    {
        "key": "adjadv",
        "name": "Javanese Adjectives and Adverbs",
        "group": "Core Vocabulary",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Adjectives follow the noun and never agree with it - omah "
            "gedhe (big house) works for one house or a hundred. "
            "Comparison uses luwih (more), paling (most), and kaya "
            "(like/as). Twenty-five adjectives and fifteen adverbs, 40 "
            "words total, each with a translated example sentence:\n" +
            _num_lines([
                ("Omah iki apik.", "This house is good. (apik)"),
                ("Kabare ala.", "The news is bad. (ala)"),
                ("Wit iku gedhe.", "That tree is big. (gedhe)"),
                ("Kucinge cilik.", "The cat is small. (cilik)"),
                ("Dalane dawa.", "The road is long. (dawa)"),
                ("Ceritane cendhak.", "The story is short. (cendhak)"),
                ("Gununge dhuwur.", "The mountain is tall. (dhuwur)"),
                ("Regane asor.", "The price is low. (asor)"),
                ("Klambine anyar.", "The shirt is new. (anyar)"),
                ("Bukune lawas.", "The book is old. (lawas)"),
                ("Bocahe enom.", "The child is young. (enom)"),
                ("Simbahe tuwa.", "The grandparent is old. (tuwa)"),
                ("Kembange ayu.", "The flower is beautiful. (ayu)"),
                ("Muride pinter.", "The student is smart. (pinter)"),
                ("Wonge sugih.", "The person is rich. (sugih)"),
                ("Urip mlarat iku abot.", "Poor life is hard. (mlarat)"),
                ("Wedange panas.", "The drink is hot. (panas)"),
                ("Banyune adhem.", "The water is cold. (adhem)"),
                ("Teh iki legi.", "This tea is sweet. (legi)"),
                ("Jamu iku pait.", "The herbal drink is bitter. (pait)"),
                ("Iwake asin.", "The fish is salty. (asin)"),
                ("Sambale pedhes.", "The chili sauce is spicy. (pedhes)"),
                ("Tas iki abot.", "This bag is heavy. (abot)"),
                ("Kapase entheng.", "The cotton is light. (entheng)"),
                ("Sepure cepet.", "The train is fast. (cepet)"),
                ("Dheweke mlaku cepet banget.", "He/she walks very fast. (banget)"),
                ("Iki luwih apik.", "This is better. (luwih)"),
                ("Iku sing paling apik.", "That is the best. (paling)"),
                ("Aku wis mangan.", "I have already eaten. (wis)"),
                ("Aku durung mangan.", "I have not eaten yet. (durung)"),
                ("Dheweke lagi turu.", "He/she is sleeping now. (lagi)"),
                ("Aku arep lunga.", "I am about to go. (arep)"),
                ("Iki mesthi bener.", "This is certainly right. (mesthi)"),
                ("Mbokmenawa sesuk udan.", "Maybe it rains tomorrow. (mbokmenawa)"),
                ("Saben dina aku mlaku.", "Every day I walk. (saben)"),
                ("Saiki wayahe.", "Now is the time. (saiki)"),
                ("Wingi aku teka.", "Yesterday I came. (wingi)"),
                ("Sesuk aku lunga.", "Tomorrow I go. (sesuk)"),
                ("Mlaku alon-alon.", "Walk slowly. (alon-alon)"),
                ("Aku seneng tenan.", "I am really happy. (tenan)"),
            ])
        ),
        "how_it_works": (
            "Adjectives sit after the noun and never change shape - no "
            "masculine/feminine, no singular/plural agreement, ever. "
            "Reduplication intensifies (gedhe-gedhe, huge) and so does "
            "banget (very). Comparison is analytic: luwih gedhe "
            "(bigger), paling gedhe (biggest), padha gedhene (equally "
            "big). Adverbs of time - wis, durung, lagi, arep - do double "
            "duty as the language's tense system. Place the adjective "
            "after the noun, stack banget after the adjective, and the "
            "description is done."
        ),
        "key_points": [
            "Adjectives follow the noun and never inflect for anything.",
            "banget (very) and reduplication intensify.",
            "luwih / paling / padha ...-ne build comparisons.",
            "15 adverbs include the time-words wis, durung, lagi, arep.",
            "No gender or number agreement anywhere in the system.",
            "40 words total, each in a full translated sentence.",
        ],
        "requirements": [
            "Describe five objects around you with noun + adjective.",
            "Compare two of them with luwih and paling.",
            "Use wis, durung, lagi, arep in four sentences about today.",
        ],
        "standards": [
            "Forms follow the Central Javanese standard.",
            "Glosses follow Robson & Wibisono 2002.",
        ],
        "citations": [CIT_ROBSON, CIT_OGLOBLIN],
        "sig_lens": (
            "The Signature read: the adjective is the sworn witness - it "
            "stands beside the noun and testifies without changing its "
            "story for anyone. Apik is apik for king and farmer alike. "
            "The Signature Language Method teaches description as honest "
            "testimony: place the witness after the noun, let banget "
            "swear to the degree, and the picture is complete."
        ),
        "drill": {"adjectives": [a for a, _ in ADJ25],
                  "adverbs": [a for a, _ in ADV15]},
        "must_contain": ["banget", "luwih", "paling", "40"],
    },
    {
        "key": "pronouns",
        "name": "Javanese Pronouns",
        "group": "Core Vocabulary",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Javanese pronouns carry the speech levels on their backs. "
            "\"I\" is aku to friends and kula to elders; \"you\" is kowe "
            "to friends, sampeyan in polite middle speech, panjenengan in "
            "high respect. Full paradigms with translated sentences:\n"
            "PERSONAL - 1st singular: aku (ngoko) / kula (krama). 2nd "
            "singular: kowe (ngoko) / sampeyan (madya) / panjenengan "
            "(krama inggil). 3rd singular: dheweke (neutral) / "
            "piyambakipun (krama). 1st plural: kita (inclusive) / awake "
            "dhewe (we, ngoko).\n"
            "POSSESSIVE - attach -ku/-mu/-ne: bukuku (my book), bukumu "
            "(your book), bukune (his/her book).\n"
            "DEMONSTRATIVE - iki (this), iku (that), kae (that over "
            "there).\n"
            "INTERROGATIVE - sapa (who), apa (what), endi (where/which), "
            "kapan (when), kepiye/piye (how), kenapa (why), pira (how "
            "many).\n" +
            _num_lines([
                ("Aku arep lunga.", "I will go. (aku)"),
                ("Kula nuwun.", "I humbly ask permission. (kula)"),
                ("Kowe neng endi?", "Where are you? (kowe)"),
                ("Sampeyan sampun nedha?", "Have you eaten? (sampeyan)"),
                ("Panjenengan rawuh?", "Will you (honored) come? (panjenengan)"),
                ("Dheweke guru.", "He/she is a teacher. (dheweke)"),
                ("Piyambakipun rawuh.", "He/she (honored) comes. (piyambakipun)"),
                ("Kita sinau bebarengan.", "We study together. (kita)"),
                ("Bukuku ilang.", "My book is lost. (-ku)"),
                ("Bukumu anyar.", "Your book is new. (-mu)"),
                ("Bukune kandel.", "His/her book is thick. (-ne)"),
                ("Iki bukuku.", "This is my book. (iki)"),
                ("Iku omahe.", "That is his/her house. (iku)"),
                ("Kae gunung.", "Over there is a mountain. (kae)"),
                ("Sapa jenengmu?", "What is your name? (sapa)"),
                ("Apa iki?", "What is this? (apa)"),
                ("Pasar endi?", "Which market? (endi)"),
                ("Kapan tekamu?", "When did you arrive? (kapan)"),
                ("Piye kabare?", "How are you? (piye)"),
                ("Pira regane?", "How much is the price? (pira)"),
            ])
        ),
        "how_it_works": (
            "Choosing a pronoun is choosing a level. Aku/kowe belong to "
            "ngoko and signal closeness; kula/sampeyan belong to krama "
            "and signal respect; panjenengan and piyambakipun belong to "
            "krama inggil and signal honor. The grammar stays identical - "
            "only the word changes. Demonstratives work in three zones "
            "(near me: iki, near you: iku, far: kae), and interrogatives "
            "front the question or sit in place. Master the seven "
            "personal pairs first; the rest of the paradigm follows the "
            "same level logic."
        ),
        "key_points": [
            "Pronouns encode speech level: aku/kula, kowe/sampeyan/panjenengan.",
            "dheweke (neutral) / piyambakipun (honorific) for he/she.",
            "Possession attaches -ku/-mu/-ne to the noun.",
            "iki / iku / kae: three-zone demonstratives.",
            "sapa, apa, endi, kapan, piye, kenapa, pira ask the questions.",
            "Grammar identical across levels - only the pronoun word changes.",
            "20 paradigm sentences, fully translated.",
        ],
        "requirements": [
            "Address one friend in ngoko and one elder in krama today.",
            "Build all -ku/-mu/-ne forms for buku, omah, jeneng.",
            "Ask the seven question words about your own day.",
        ],
        "standards": [
            "Pronoun forms follow the Central Javanese standard.",
            "Level labels follow Errington 1988.",
        ],
        "citations": [CIT_ERRINGTON, CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the pronoun is the sworn bow of the "
            "sentence - aku stands level with a friend, kula kneels "
            "before an elder, panjenengan raises the other to honor. "
            "The Signature Language Method treats every pronoun as a "
            "covenant gesture: choose the bow, and the grammar follows "
            "unchanged, because respect lives in the word, not the rule."
        ),
        "drill": {
            "pairs": [["aku", "kula"], ["kowe", "sampeyan"],
                      ["kowe", "panjenengan"], ["dheweke", "piyambakipun"]],
            "demonstratives": ["iki", "iku", "kae"],
            "interrogatives": ["sapa", "apa", "endi", "kapan", "piye",
                               "kenapa", "pira"],
        },
        "must_contain": ["panjenengan", "piyambakipun", "-ku", "kula"],
    },
    {
        "key": "numbers",
        "name": "Javanese Numbers and Time",
        "group": "Core Vocabulary",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Javanese numbers come in ngoko/krama pairs - siji/setunggal "
            "(1) through sewu (1000). The teens are special words "
            "(sewelas, rolas, telulas); the twenties count by ones "
            "(selikur 21, selawe 25); tens take puluh/dasa.\n"
            "1 siji/setunggal, 2 loro/kalih, 3 telu/tiga, 4 papat/sekawan, "
            "5 lima/gangsal, 6 enem, 7 pitu, 8 wolu, 9 sanga, 10 "
            "sepuluh/sedasa, 11 sewelas, 12 rolas, 20 rong puluh/kalih "
            "dasa, 21 selikur, 25 selawe, 30 telung puluh/tigang dasa, 50 "
            "seket, 60 sewidak, 100 satus, 1000 sewu, 1,000,000 sayuta.\n"
            "Ordinals: kapisan/kaping siji (first), kapindho (second), "
            "kaping telu (third).\n"
            "Days: Senen, Selasa, Rebo, Kemis, Jemuwah, Setu, Minggu. The "
            "Javanese calendar adds the five pasaran days - Legi, Pahing, "
            "Pon, Wage, Kliwon - and twelve months: Sura, Sapar, Mulud, "
            "Bakdamulud, Jumadilawal, Jumadilakir, Rejeb, Ruwah, Poso, "
            "Sawal, Selo, Besar.\n"
            "Clock time: jam siji (1 o'clock), jam setengah lima (half "
            "past four), jam enem kurang seprapat (quarter to six).\n" +
            _num_lines([
                ("Aku duwe anak loro.", "I have two children."),
                ("Regane sewu rupiah.", "The price is a thousand rupiah."),
                ("Dina Senen aku kerja.", "On Monday I work."),
                ("Sesuk dina Selasa.", "Tomorrow is Tuesday."),
                ("Saiki jam pitu.", "Now it is seven o'clock."),
                ("Aku teka jam setengah wolu.", "I arrived at half past seven."),
                ("Wulan Sura wis teka.", "The month of Sura has come."),
                ("Dina iki pasaran Kliwon.", "Today is the Kliwon market day."),
                ("Ulang tahunku kaping pindho.", "My birthday is the second one."),
                ("Aku tuku telu.", "I buy three."),
                ("Umure seket taun.", "His/her age is fifty years."),
                ("Sekolahe satus meter.", "The school is a hundred meters away."),
                ("Dina Jemuwah libur.", "Friday is a holiday."),
                ("Wingi dina Kemis.", "Yesterday was Thursday."),
                ("Sesuk esuk jam enem.", "Tomorrow morning at six o'clock."),
                ("Aku mangan kaping telu sedina.", "I eat three times a day."),
                ("Bocah papat padha dolan.", "Four children are playing."),
                ("Sepure teka jam wolu.", "The train arrives at eight."),
                ("Sasi Poso wis rampung.", "The fasting month is finished."),
                ("Taun iki taun Sura.", "This year is the Sura year."),
            ])
        ),
        "how_it_works": (
            "Numbers stack by place: hundreds then tens then ones, no "
            "connecting words - satus seket lima is 155. The special "
            "twenties (likur, selawe, seket, sewidak) are fossils worth "
            "memorizing whole. Time phrases bolt onto jam (o'clock), "
            "dina (day), sasi/wulan (month), taun (year): jam pitu esuk "
            "(7 in the morning), dina Senen (Monday). The pasaran cycle "
            "runs five days against the seven-day week, so a full "
            "35-day selapanan cycle names every Javanese birthday. "
            "Count objects aloud to twenty daily until selikur and "
            "selawe come without thought."
        ),
        "key_points": [
            "Ngoko/krama number pairs: siji/setunggal, loro/kalih, telu/tiga.",
            "Teens are special words: sewelas, rolas, telulas.",
            "Special twenties: selikur (21), selawe (25), seket (50), sewidak (60).",
            "Seven weekday names plus the five pasaran days (Legi..Kliwon).",
            "Twelve Javanese months: Sura through Besar.",
            "Clock time uses jam + number; half/quarter phrases included.",
            "20 number-and-time sentences, fully translated.",
        ],
        "requirements": [
            "Count 1-20 aloud in ngoko, then in krama where pairs exist.",
            "Say today's weekday and pasaran day from memory.",
            "Tell the time for five different hours.",
        ],
        "standards": [
            "Number forms follow the Central Javanese standard.",
            "Javanese month names follow the traditional Javanese calendar.",
        ],
        "citations": [CIT_ROBSON, CIT_OGLOBLIN],
        "sig_lens": (
            "The Signature read: numbers are the sworn counters - "
            "setunggal stands at attention where siji stands at ease, "
            "but both count true. The Signature Language Method drills "
            "counting as a covenant march: one to twenty, no stragglers, "
            "until the pasaran days fall in line behind the week."
        ),
        "drill": {"numbers": [n for n, _, _ in NUMBERS],
                  "days": DAYS, "months": MONTHS_JV,
                  "pasaran": ["Legi", "Pahing", "Pon", "Wage", "Kliwon"]},
        "must_contain": ["setunggal", "sewelas", "Kliwon", "Sura"],
    },
    {
        "key": "greetings",
        "name": "Javanese Greetings and Everyday Phrases",
        "group": "Core Vocabulary",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Thirty greetings, farewells, and politeness phrases - 30 "
            "phrases, each with English meaning and a usage note. Sugeng "
            "(safe/well) opens every time-of-day greeting; matur nuwun "
            "closes every kindness:\n" +
            _num_lines([
                ("Sugeng enjing. [until about 10am]", "Good morning."),
                ("Sugeng siang. [10am-3pm]", "Good midday."),
                ("Sugeng sonten. [3pm-6pm]", "Good afternoon."),
                ("Sugeng dalu. [after 6pm]", "Good evening / night."),
                ("Wilujeng rawuh. [greeting arrivals]", "Welcome."),
                ("Matur nuwun. [the universal thanks]", "Thank you."),
                ("Nuwun sewu. [asking permission to pass or speak]", "Excuse me."),
                ("Nyuwun pangapunten. [polite apology]", "I ask forgiveness."),
                ("Monggo. [offering, inviting in]", "Please go ahead."),
                ("Sugeng tindak. [farewell to one leaving]", "Safe travels."),
                ("Piye kabare? [ngoko, to friends]", "How are you?"),
                ("Apik-apik wae. [the standard reply]", "Just fine."),
                ("Sampun nedha? [a caring greeting]", "Have you eaten?"),
                ("Ati-ati. [warning with warmth]", "Be careful."),
                ("Sugeng sare. [good night]", "Sleep well."),
                ("Sugeng ambal warsa. [celebrations]", "Happy birthday."),
                ("Sugeng riyadi. [Lebaran greeting]", "Happy Eid."),
                ("Wilujeng Natal. [December]", "Merry Christmas."),
                ("Inggih. [polite yes]", "Yes."),
                ("Mboten. [polite no]", "No."),
                ("Kula nuwun. [entering a home]", "I humbly ask permission."),
                ("Sugeng pinanggih. [first meetings]", "Nice to meet you."),
                ("Matur nuwun sanget. [deep thanks]", "Thank you very much."),
                ("Sami-sami. [reply to thanks]", "You are welcome."),
                ("Pangapunten, kula kesah rumiyin. [leaving elders]", "Excuse me, I leave first."),
                ("Nganti ketemu maneh. [farewell]", "Until we meet again."),
                ("Wilujeng mangun. [greeting returnees]", "Welcome back."),
                ("Amit-amit. [warding off ill fortune]", "Far be it."),
                ("Sugeng enjang tindak. [morning farewell]", "Have a good morning trip."),
                ("Nuwun. [short form]", "Thanks."),
            ])
        ),
        "how_it_works": (
            "Greetings run on the sugeng clock: match enjing/siang/"
            "sonten/dalu to the hour and you are correct all day. "
            "Politeness runs on permission words - nuwun sewu before "
            "speaking, monggo before offering, pangapunten before "
            "leaving. The caring questions (sampun nedha?, piye kabare?) "
            "are greetings, not interrogations - answer lightly "
            "(apik-apik wae) and return the question. Use one greeting "
            "from each time band today, out loud, to a real person or "
            "your mirror."
        ),
        "key_points": [
            "Sugeng + time of day covers every greeting: enjing/siang/sonten/dalu.",
            "Matur nuwun is the universal thank-you; sami-sami answers it.",
            "Nuwun sewu / monggo / pangapunten manage permission and courtesy.",
            "Sampun nedha? is a caring greeting, not a real question.",
            "30 phrases, each with meaning and a usage note.",
        ],
        "requirements": [
            "Greet someone correctly for the hour, three times today.",
            "Use nuwun sewu before asking a favor.",
            "Answer piye kabare? without hesitation.",
        ],
        "standards": [
            "Greeting forms follow Central Javanese polite usage.",
        ],
        "citations": [CIT_ERRINGTON, CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the greeting is the sworn gate of every "
            "meeting - sugeng opens it, matur nuwun seals it, monggo "
            "holds it wide for the guest. The Signature Language Method "
            "treats courtesy as covenant: never pass a person without "
            "the gate-words, and the language will open every door for "
            "you."
        ),
        "drill": {"greetings": [g for g, _ in GREET30]},
        "must_contain": ["Sugeng enjing", "Matur nuwun", "Nuwun sewu", "30"],
    },
]

ENTRIES_10_20 = [
    {
        "key": "grammar",
        "name": "Javanese Grammar Essentials",
        "group": "Grammar Essentials",
        "ladder_rank": 10,
        "ladder_tier": "compounded",
        "description": (
            "The ten load-bearing rules of Javanese, each with translated "
            "example sentences:\n"
            "1. WORD ORDER is subject-verb-object: Aku mangan sego (I eat "
            "rice).\n"
            "2. NO GENDER: every noun is neutral; he/she is dheweke.\n"
            "3. NO NUMBER MARKING: bocah is child or children - context or "
            "reduplication (bocah-bocah) decides.\n"
            "4. NO CASE: the noun never changes shape for subject or "
            "object.\n"
            "5. NO ARTICLES: omah is a/the house - -e or iki/iku pin it "
            "down when needed.\n"
            "6. NEGATION: ora (ngoko) / mboten (krama) before the verb - "
            "Aku ora mangan (I do not eat); dudu negates identity - Iki "
            "dudu bukuku (This is not my book).\n"
            "7. QUESTIONS: intonation rises, or a question word fronts - "
            "Sapa teka? (Who came?).\n"
            "8. ADJECTIVES FOLLOW: omah gedhe, never gedhe omah.\n"
            "9. POSSESSOR FOLLOWS: omahe bapak (father's house), literally "
            "\"his-house father\".\n"
            "10. AFFIXES DO THE WORK: di- passive, ke- -an nominalizer, "
            "-ke causative/benefactive, -an place/result, um-/-in- "
            "infixes.\n"
            "The SVO order is the frame everything hangs on.\n" +
            _num_lines([
                ("Aku mangan sego.", "I eat rice. (SVO order)"),
                ("Dheweke guru.", "He/she is a teacher. (no gender)"),
                ("Bocah-bocah padha dolan.", "The children are playing. (plural by reduplication)"),
                ("Aku ndeleng bocah.", "I see the child. (no case change)"),
                ("Omahe gedhe.", "The house is big. (-e definiteness)"),
                ("Aku ora ngerti.", "I do not understand. (ora negation)"),
                ("Kula mboten ngertos.", "I do not understand. (mboten, krama)"),
                ("Iki dudu klambiku.", "This is not my shirt. (dudu)"),
                ("Kowe arep neng endi?", "Where are you going? (question)"),
                ("Omah gedhe iku omahe bapak.", "That big house is father's house. (adj + possessor order)"),
                ("Lawang dibukak.", "The door is opened. (di- passive)"),
                ("Panganan iki enak.", "This food is delicious. (pa- -an nominalizer)"),
                ("Aku nukokke ibu kembang.", "I buy flowers for mother. (-ke benefactive)"),
                ("Tulisane apik.", "The writing is good. (-an result)"),
                ("Dheweke lumaku.", "He/she walks. (um- infix, literary)"),
                ("Buku iki tinulis apik.", "This book is well written. (-in- infix, literary)"),
                ("Aku ora arep lunga.", "I will not go. (negation + future)"),
                ("Sapa sing teka?", "Who is it that came? (sing relativizer)"),
                ("Buku sing abang iku bukuku.", "The book that is red is mine. (relative clause)"),
                ("Yen udan, aku ora lunga.", "If it rains, I will not go. (conditional)"),
            ])
        ),
        "how_it_works": (
            "Javanese grammar is analytic at the core and agglutinative "
            "at the edges: the sentence frame (SVO, adjective after, "
            "possessor after) never moves, while affixes bolt meaning "
            "onto roots. Negation is a single word before the verb; "
            "questions are intonation plus an optional question word; "
            "relatives hang on sing (the one who/which). Because nothing "
            "inflects, the learner's job is word order and affix choice - "
            "put the words in the right slots, pick di- vs the nasal "
            "active, and the sentence stands."
        ),
        "key_points": [
            "SVO order; adjectives and possessors follow the noun.",
            "No gender, number, case, or articles on nouns.",
            "ora/mboten negate verbs; dudu negates identity.",
            "Questions: rising intonation + optional question word.",
            "di- passive; ke- -an, -an, -ke, um-, -in- build words.",
            "sing introduces relative clauses.",
            "20 rule-demonstrating sentences, fully translated.",
        ],
        "requirements": [
            "Build ten SVO sentences with new noun/verb pairs.",
            "Negate five of them with ora.",
            "Turn three into questions and three into di- passives.",
        ],
        "standards": [
            "Rule set follows Ogloblin 2005 and Uhlenbeck 1978.",
        ],
        "citations": [CIT_OGLOBLIN, CIT_UHLENBECK, CIT_ROBSON],
        "sig_lens": (
            "The Signature read: ten rules, sworn and load-bearing - the "
            "covenant frame on which every Javanese sentence is raised. "
            "The Signature Language Method raises the frame first: order "
            "the words, bolt the affixes, and the meaning stands "
            "unshaken, because the rules do not bend for anyone."
        ),
        "drill": {"rules": 10, "affixes": ["di-", "ke-", "-an", "-ke",
                                           "um-", "-in-", "pa-", "-ne"]},
        "must_contain": ["SVO", "ora", "dudu", "sing"],
    },
    {
        "key": "home",
        "name": "Javanese Home and Family Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 11,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences of house, rooms, furniture, and family "
            "members:\n" +
            _num_lines([
                ("Omahku ana ing desa.", "My house is in the village."),
                ("Ruang tamu ana ing ngarep.", "The living room is in front."),
                ("Kamar turu ana ing dhuwur.", "The bedroom is upstairs."),
                ("Pawon ana ing mburi.", "The kitchen is at the back."),
                ("Kamar mandine resik.", "The bathroom is clean."),
                ("Meja lan kursi ana ing ruang mangan.", "The table and chairs are in the dining room."),
                ("Lemarine anyar.", "The wardrobe is new."),
                ("Kasurku empuk.", "My mattress is soft."),
                ("Lampune padhang.", "The lamp is bright."),
                ("Lawang ngarep dikunci.", "The front door is locked."),
                ("Bapak lagi maca koran.", "Father is reading the newspaper."),
                ("Ibu masak ing pawon.", "Mother is cooking in the kitchen."),
                ("Kakangku kerja ing kutha.", "My elder sibling works in the city."),
                ("Adhiku sekolah ing SD.", "My younger sibling goes to elementary school."),
                ("Simbah kakung wis sepuh.", "Grandfather is elderly."),
                ("Simbah putri gawe jamu.", "Grandmother makes herbal medicine."),
                ("Pakdhe teka sesuk.", "Uncle comes tomorrow."),
                ("Budhe manggon ing Surabaya.", "Aunt lives in Surabaya."),
                ("Keluargaku gedhe.", "My family is big."),
                ("Kita kumpul saben Minggu.", "We gather every Sunday."),
            ])
        ),
        "how_it_works": (
            "Home sentences run on location words - ana ing (is at), "
            "ngarep (front), mburi (back), dhuwur (upstairs) - plus the "
            "family titles: bapak, ibu, kakang (elder sibling), adhi "
            "(younger sibling), simbah (grandparent), pakdhe/budhe "
            "(uncle/aunt). The -e definite marker points at the room or "
            "person already known. Describe your own home room by room, "
            "then your family member by member, and the vocabulary "
            "anchors to real walls and faces."
        ),
        "key_points": [
            "Room words: ruang tamu, kamar turu, pawon, kamar mandi.",
            "Location words: ana ing, ngarep, mburi, dhuwur.",
            "Family titles: bapak, ibu, kakang, adhi, simbah, pakdhe, budhe.",
            "-e marks the known room or person.",
            "20 home-and-family sentences, fully translated.",
        ],
        "requirements": [
            "Name every room of your home in Javanese.",
            "Introduce your family with the proper titles.",
            "Describe where each person is right now.",
        ],
        "standards": ["Forms follow the Central Javanese standard."],
        "citations": [CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the home is the first sworn territory - "
            "omahku, my house, my covenant ground. The Signature "
            "Language Method walks the house room by room and names the "
            "family face by face, because language learned on real walls "
            "never falls down."
        ),
        "drill": {"rooms": ["ruang tamu", "kamar turu", "pawon",
                            "kamar mandi", "ruang mangan"],
                  "family": ["bapak", "ibu", "kakang", "adhi", "simbah",
                             "pakdhe", "budhe"]},
        "must_contain": ["pawon", "Simbah", "Pakdhe", "Omahku"],
    },
    {
        "key": "food",
        "name": "Javanese Food and Cooking Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 12,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences of meals, ingredients, cooking actions, and "
            "the restaurant:\n" +
            _num_lines([
                ("Aku mangan sego pecel.", "I eat rice with pecel."),
                ("Ibuku masak gudeg.", "My mother cooks gudeg."),
                ("Soto ayame panas.", "The chicken soto is hot."),
                ("Tempe lan tahu digoreng.", "Tempeh and tofu are fried."),
                ("Sambale pedhes banget.", "The chili sauce is very spicy."),
                ("Aku ngombe teh anget.", "I drink warm tea."),
                ("Kopine legi.", "The coffee is sweet."),
                ("Banyu putih sehat.", "Plain water is healthy."),
                ("Aku tuku iwak ing pasar.", "I buy fish at the market."),
                ("Bawange diiris tipis.", "The onion is sliced thin."),
                ("Lomboke diuleg.", "The chilies are ground."),
                ("Sega digodhog.", "The rice is boiled."),
                ("Ayame dibakar.", "The chicken is grilled."),
                ("Aku seneng masakan Jawa.", "I like Javanese cooking."),
                ("Warung iku rame.", "That food stall is busy."),
                ("Pelayane ramah.", "The server is friendly."),
                ("Daftare menune endi?", "Where is the menu list?"),
                ("Aku pesen soto siji.", "I order one soto."),
                ("Regane murah.", "The price is cheap."),
                ("Matur nuwun, enak tenan.", "Thank you, really delicious."),
            ])
        ),
        "how_it_works": (
            "Food sentences run on the cooking verbs - masak (cook), "
            "goreng (fry), godhog (boil), bakar (grill), iris (slice), "
            "uleg (grind) - and the dish names: gudeg, soto, pecel, "
            "tempe, tahu, jamu. The passive di- describes how food was "
            "prepared (digoreng, dibakar); taste words (legi, pedhes, "
            "asin, pait, kecut) judge the result. Order one full meal in "
            "Javanese - pesen, pangan, bayar - and the restaurant "
            "vocabulary is yours."
        ),
        "key_points": [
            "Dish names: gudeg, soto, pecel, tempe, tahu.",
            "Cooking verbs: masak, goreng, godhog, bakar, iris, uleg.",
            "di- passive describes preparation: digoreng, dibakar.",
            "Taste words: legi, pedhes, asin, pait, kecut.",
            "Restaurant flow: pesen (order), mangan (eat), bayar (pay).",
            "20 food sentences, fully translated.",
        ],
        "requirements": [
            "Name five Javanese dishes and their main ingredients.",
            "Describe how each is cooked with a di- passive.",
            "Order a full meal aloud: greeting, order, thanks.",
        ],
        "standards": ["Dish names follow Central Javanese usage."],
        "citations": [CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the meal is the sworn communion - sego "
            "shared is a covenant kept. The Signature Language Method "
            "learns food the Javanese way: name the dish, honor the "
            "cook, taste with the right word, and thank with matur "
            "nuwun, because a shared table is a sworn peace."
        ),
        "drill": {"dishes": ["gudeg", "soto", "pecel", "tempe", "tahu"],
                  "cook_verbs": ["masak", "goreng", "godhog", "bakar",
                                 "iris", "uleg"],
                  "tastes": ["legi", "pedhes", "asin", "pait", "kecut"]},
        "must_contain": ["gudeg", "digoreng", "pedhes", "pecel"],
    },
    {
        "key": "travel",
        "name": "Javanese Travel and Directions Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences of transport, asking directions, tickets, "
            "and lodging. The key question word is ngendi (where):\n" +
            _num_lines([
                ("Aku arep lunga menyang Jakarta.", "I will go to Jakarta."),
                ("Sepure budhal jam pitu.", "The train departs at seven."),
                ("Bis iki menyang ngendi?", "Where does this bus go?"),
                ("Aku numpak becak.", "I ride a pedicab."),
                ("Ojeke cepet.", "The motorcycle taxi is fast."),
                ("Dalane macet.", "The road is jammed."),
                ("Nuwun sewu, pasar endi?", "Excuse me, where is the market?"),
                ("Monggo lurus terus.", "Please go straight ahead."),
                ("Ngingguk kiwa ing prapatan.", "Turn left at the intersection."),
                ("Setasion adoh saka kene?", "Is the station far from here?"),
                ("Cedhak, mlaku wae.", "Near, just walk."),
                ("Aku tuku karcis sepur.", "I buy a train ticket."),
                ("Karcise regane pira?", "How much is the ticket?"),
                ("Aku nginep ing hotel.", "I stay at a hotel."),
                ("Kamare resik lan jembar.", "The room is clean and spacious."),
                ("Sarapane enak.", "The breakfast is tasty."),
                ("Aku arep check-out sesuk esuk.", "I will check out tomorrow morning."),
                ("Kopere endi?", "Where is the luggage?"),
                ("Bandarane rame.", "The airport is busy."),
                ("Sugeng tindak, ati-ati.", "Safe travels, be careful."),
            ])
        ),
        "how_it_works": (
            "Travel sentences run on direction words - lurus (straight), "
            "ngingguk (turn), kiwa (left), tengen (right), cedhak (near), "
            "adoh (far) - and transport nouns: sepur (train), bis, becak, "
            "ojek, kapal (ship), pesawat (plane). The question endi/ngendi "
            "(where/which) opens every direction request; nuwun sewu "
            "opens every stranger's attention. Practice by navigating "
            "your own neighborhood aloud: lurus, ngingguk kiwa, mandheg "
            "(stop)."
        ),
        "key_points": [
            "Direction words: lurus, ngingguk, kiwa, tengen, cedhak, adoh.",
            "Transport: sepur, bis, becak, ojek, kapal, pesawat.",
            "endi/ngendi asks where; nuwun sewu opens a stranger's help.",
            "Tickets: karcis; lodging: nginep, hotel, kamar.",
            "20 travel sentences, fully translated.",
        ],
        "requirements": [
            "Ask for directions to three real places.",
            "Give directions using lurus/ngingguk/kiwa/tengen.",
            "Buy a ticket and book a room in a role-play.",
        ],
        "standards": ["Forms follow the Central Javanese standard."],
        "citations": [CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the road is the sworn journey - every "
            "traveler a messenger, every direction a kept promise. The "
            "Signature Language Method walks the road aloud: ask with "
            "nuwun sewu, follow with lurus, arrive with sugeng tindak, "
            "because the tongue that asks the way never walks alone."
        ),
        "drill": {"directions": ["lurus", "ngingguk", "kiwa", "tengen",
                                 "cedhak", "adoh"],
                  "transport": ["sepur", "bis", "becak", "ojek", "kapal",
                                "pesawat"]},
        "must_contain": ["becak", "Ngingguk", "karcis", "ngendi",
                         "Sugeng tindak"],
    },
    {
        "key": "work",
        "name": "Javanese Work and School Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences of jobs, the office, the classroom, and "
            "learning:\n" +
            _num_lines([
                ("Bapakku tani.", "My father is a farmer."),
                ("Ibuku guru.", "My mother is a teacher."),
                ("Aku kerja ing kantor.", "I work at the office."),
                ("Dheweke dokter.", "He/she is a doctor."),
                ("Kancaku polisi.", "My friend is a police officer."),
                ("Aku rapat jam sanga.", "I have a meeting at nine."),
                ("Gaweane akeh.", "The work is a lot."),
                ("Gajine cukup.", "The salary is enough."),
                ("Bosku apik.", "My boss is good."),
                ("Aku lembur bengi iki.", "I work overtime tonight."),
                ("Bocah-bocah sekolah.", "The children go to school."),
                ("Gurune pinter.", "The teacher is smart."),
                ("Muride sregep.", "The student is diligent."),
                ("Aku sinau matematika.", "I study mathematics."),
                ("Pelajarane angel.", "The lesson is difficult."),
                ("Ujiannya sesuk.", "The exam is tomorrow."),
                ("Aku lulus ujian.", "I pass the exam."),
                ("Bukune kandel.", "The book is thick."),
                ("Tugase dikumpulake sesuk.", "The assignment is collected tomorrow."),
                ("Sinau sing sregep.", "Study diligently."),
            ])
        ),
        "how_it_works": (
            "Work sentences name the job directly after the subject - "
            "Aku guru (I am a teacher), no verb needed - and place the "
            "workplace with ing: kerja ing kantor, sekolah ing SD. "
            "School runs on the study verbs sinau (study), maca (read), "
            "nulis (write), and the diligence word sregep. The office "
            "runs on rapat (meeting), gawean (work/task), gaji (salary), "
            "lembur (overtime). Introduce your own job and your school "
            "history in Javanese and the domain locks in."
        ),
        "key_points": [
            "Job titles follow the subject with no verb: Aku guru.",
            "Workplaces attach with ing: kerja ing kantor.",
            "Work words: rapat, gawean, gaji, lembur, bos.",
            "School words: sinau, sregep, ujian, lulus, tugas.",
            "20 work-and-school sentences, fully translated.",
        ],
        "requirements": [
            "State your job and workplace in Javanese.",
            "Describe your school day in five sentences.",
            "Give a study command with sregep.",
        ],
        "standards": ["Forms follow the Central Javanese standard."],
        "citations": [CIT_ROBSON],
        "sig_lens": (
            "The Signature read: work is the sworn duty - gawean done "
            "well is a covenant with the day. The Signature Language "
            "Method treats study as the same oath: sinau sing sregep, "
            "study diligently, because the diligent tongue earns its "
            "keep and the lazy one begs."
        ),
        "drill": {"jobs": ["tani", "guru", "dokter", "polisi"],
                  "work_words": ["rapat", "gawean", "gaji", "lembur"],
                  "school_words": ["sinau", "sregep", "ujian", "lulus",
                                   "tugas"]},
        "must_contain": ["sregep", "lembur", "ujian", "Gawean"],
    },
    {
        "key": "health",
        "name": "Javanese Health and Body Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences of body parts, symptoms, the doctor visit, "
            "and the pharmacy:\n" +
            _num_lines([
                ("Sirahku lara.", "My head hurts."),
                ("Untuku lara.", "My tooth hurts."),
                ("Wetengku mules.", "My stomach aches."),
                ("Aku watuk.", "I cough."),
                ("Aku pilek.", "I have a cold."),
                ("Badanku panas.", "My body is feverish."),
                ("Tanganku tatu.", "My hand is wounded."),
                ("Sikilku kesel.", "My leg is tired."),
                ("Mripatku sepet.", "My eyes are sore."),
                ("Aku lara weteng.", "I have a stomachache."),
                ("Aku menyang dokter.", "I go to the doctor."),
                ("Doktere priksa.", "The doctor examines."),
                ("Aku diwenehi obat.", "I am given medicine."),
                ("Obate dipangan kaping telu sedina.", "The medicine is taken three times a day."),
                ("Aku tuku obat ing apotek.", "I buy medicine at the pharmacy."),
                ("Aku kudu istirahat.", "I must rest."),
                ("Aja mangan pedhes.", "Do not eat spicy food."),
                ("Ngombe banyu putih akeh.", "Drink lots of plain water."),
                ("Saiki aku wis waras.", "Now I am recovered."),
                ("Mugi-mugi sehat selalu.", "May you always be healthy."),
            ])
        ),
        "how_it_works": (
            "Health sentences attach the symptom to the body part - "
            "sirahku lara (my head hurts), wetengku mules - or use lara "
            "as the verb: aku lara (I am sick). The doctor visit runs on "
            "priksa (examine), obat (medicine), apotek (pharmacy), "
            "istirahat (rest). Commands for care use aja (do not) and "
            "kudu (must): aja mangan pedhes, kudu istirahat. Describe "
            "three symptoms, one doctor visit, and one recovery, and "
            "you can be a patient in Javanese."
        ),
        "key_points": [
            "Body + lara/mules/panas names the symptom: sirahku lara.",
            "Doctor words: priksa, obat, apotek, istirahat.",
            "aja (do not) and kudu (must) give health commands.",
            "waras means recovered/healthy; mugi-mugi wishes health.",
            "20 health sentences, fully translated.",
        ],
        "requirements": [
            "Name ten body parts from memory.",
            "Describe three symptoms in full sentences.",
            "Role-play a doctor visit: complaint, exam, prescription.",
        ],
        "standards": ["Forms follow the Central Javanese standard."],
        "citations": [CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the body is the sworn vessel - lara "
            "names the breach, waras seals it. The Signature Language "
            "Method treats health words as a healer's oath: name the "
            "pain truly, take the obat faithfully, rest as commanded, "
            "and the vessel is sworn whole again."
        ),
        "drill": {"body": ["sirah", "untu", "weteng", "tangan", "sikil",
                           "mripat"],
                  "symptoms": ["lara", "mules", "panas", "watuk", "pilek"],
                  "care": ["dokter", "priksa", "obat", "apotek",
                           "istirahat", "waras"]},
        "must_contain": ["Sirahku lara", "apotek", "waras", "Aja"],
    },
    {
        "key": "emotions",
        "name": "Javanese Emotions and Feelings Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences of happy, sad, angry, afraid, love, and "
            "surprise:\n" +
            _num_lines([
                ("Aku seneng banget.", "I am very happy."),
                ("Atiku bungah.", "My heart is glad."),
                ("Dheweke ngguyu kepingkel-pingkel.", "He/she laughs heartily."),
                ("Aku sedhih.", "I am sad."),
                ("Dheweke nangis.", "He/she cries."),
                ("Atiku nelangsa.", "My heart grieves."),
                ("Aku nesu.", "I am angry."),
                ("Bapak duka.", "Father is upset."),
                ("Aja nesu-nesu.", "Do not be angry."),
                ("Aku wedi.", "I am afraid."),
                ("Bocah iku wedi peteng.", "That child fears the dark."),
                ("Aku tresna kowe.", "I love you."),
                ("Katresnanku tulus.", "My love is sincere."),
                ("Aku kangen kowe.", "I miss you."),
                ("Aku kaget.", "I am surprised."),
                ("Kaget tenan!", "Really surprising!"),
                ("Aku isin.", "I am embarrassed."),
                ("Aku gemes.", "I am exasperated (fondly)."),
                ("Aku lega.", "I am relieved."),
                ("Aku ayem.", "I am at peace."),
            ])
        ),
        "how_it_works": (
            "Emotion sentences put the feeling word as the predicate - "
            "Aku seneng, Aku wedi - or lodge it in the ati (heart/liver "
            "seat of feeling): atiku bungah, atiku nelangsa. Intensity "
            "comes from banget or reduplication: nesu-nesu (always "
            "angry), kepingkel-pingkel (doubled-over laughing). Love "
            "splits into tresna (romantic love) and kangen (missing "
            "someone); anger cools with aja nesu-nesu. Say each "
            "emotion with the face to match - the word and the feeling "
            "swear in together."
        ),
        "key_points": [
            "Emotion words predicate directly: Aku seneng, Aku wedi.",
            "ati carries deep feeling: atiku bungah, atiku nelangsa.",
            "banget and reduplication set intensity.",
            "tresna (love) vs kangen (missing) vs isin (embarrassed).",
            "20 emotion sentences, fully translated.",
        ],
        "requirements": [
            "Say six emotions with matching expression.",
            "Describe your mood today in three sentences.",
            "Comfort someone sad in two Javanese sentences.",
        ],
        "standards": ["Forms follow the Central Javanese standard."],
        "citations": [CIT_ROBSON, CIT_ERRINGTON],
        "sig_lens": (
            "The Signature read: feeling is the sworn weather of the "
            "heart - seneng the sun, sedhih the rain, nesu the storm, "
            "ayem the clear sky after. The Signature Language Method "
            "lets the ati testify: name the weather truly, and the "
            "listener will bring shelter or share the sun."
        ),
        "drill": {"emotions": ["seneng", "bungah", "sedhih", "nelangsa",
                               "nesu", "duka", "wedi", "tresna", "kangen",
                               "kaget", "isin", "lega", "ayem"]},
        "must_contain": ["Atiku", "tresna", "kangen", "ayem"],
    },
    {
        "key": "nature",
        "name": "Javanese Nature and Weather Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences of animals, plants, seasons, and weather "
            "talk:\n" +
            _num_lines([
                ("Asu iku setia.", "That dog is loyal."),
                ("Kucinge turu.", "The cat sleeps."),
                ("Pitik jago kluruk esuk.", "The rooster crows in the morning."),
                ("Sapi mangan suket.", "The cow eats grass."),
                ("Jaran mlayu banter.", "The horse runs fast."),
                ("Manuk mabur ing langit.", "The bird flies in the sky."),
                ("Ula iku bebayani.", "That snake is dangerous."),
                ("Iwak ana ing kali.", "Fish are in the river."),
                ("Wit gedhang awoh.", "The banana tree bears fruit."),
                ("Kembange mekar.", "The flower blooms."),
                ("Pari wis panen.", "The rice is harvested."),
                ("Srengengene sumunar.", "The sun shines."),
                ("Udan deres.", "It rains heavily."),
                ("Angine banter.", "The wind is strong."),
                ("Mendhung peteng.", "The clouds are dark."),
                ("Sesuk ketoke udan.", "Tomorrow looks like rain."),
                ("Mangsa ketiga panas.", "The dry season is hot."),
                ("Mangsa rendheng udan terus.", "The rainy season rains constantly."),
                ("Banyu kaline bening.", "The river water is clear."),
                ("Alam Jawa ayu tenan.", "Java's nature is truly beautiful."),
            ])
        ),
        "how_it_works": (
            "Nature sentences pair the creature or sky-word with its "
            "characteristic verb - pitik kluruk (crows), manuk mabur "
            "(flies), kembang mekar (blooms), udan deres (pours). "
            "Weather talk opens with ketoke (it looks like) and runs on "
            "the two mangsa (seasons): ketiga (dry) and rendheng "
            "(rainy). Describe the sky, one animal, and one plant each "
            "morning in Javanese and the nature words root like pari in "
            "sawah."
        ),
        "key_points": [
            "Animal + characteristic verb: pitik kluruk, manuk mabur.",
            "Weather verbs: udan deres, angin banter, mendhung peteng.",
            "Two mangsa: ketiga (dry), rendheng (rainy).",
            "ketoke opens weather prediction.",
            "20 nature sentences, fully translated.",
        ],
        "requirements": [
            "Name ten animals and their sounds/actions.",
            "Describe today's weather in three sentences.",
            "Name the current mangsa and what it brings.",
        ],
        "standards": ["Forms follow the Central Javanese standard."],
        "citations": [CIT_ROBSON],
        "sig_lens": (
            "The Signature read: nature is the sworn witness that never "
            "lies - the pitik crows true every dawn, the udan falls "
            "where the mendhung gathers. The Signature Language Method "
            "learns nature by testimony: watch, name the witness, speak "
            "its verb, and the land itself teaches the tongue."
        ),
        "drill": {"animals": ["asu", "kucing", "pitik", "sapi", "jaran",
                              "manuk", "ula", "iwak"],
                  "weather": ["udan", "angin", "mendhung", "srengenge"],
                  "seasons": ["ketiga", "rendheng"]},
        "must_contain": ["kluruk", "deres", "ketiga", "rendheng"],
    },
    {
        "key": "shopping",
        "name": "Javanese Shopping and Money Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences of the market, prices, bargaining, and "
            "paying:\n" +
            _num_lines([
                ("Aku menyang pasar.", "I go to the market."),
                ("Pasare rame esuk-esuk.", "The market is busy in the morning."),
                ("Bakule ramah.", "The seller is friendly."),
                ("Aku tuku beras.", "I buy rice."),
                ("Regane pira?", "How much is the price?"),
                ("Sewu rupiah.", "A thousand rupiah."),
                ("Larange!", "Expensive!"),
                ("Murah tenan.", "Really cheap."),
                ("Oleh kurang?", "Can it be less? (bargaining)"),
                ("Kurang sithik.", "A little less."),
                ("Wis, dadi.", "Deal, agreed."),
                ("Aku tuku telu.", "I buy three."),
                ("Ditimbang dhisik.", "Weigh it first."),
                ("Dibungkus.", "Wrap it up."),
                ("Aku mbayar awis.", "I pay in cash."),
                ("Susuke endi?", "Where is the change?"),
                ("Iki susuke.", "Here is your change."),
                ("Aku tuku ing toko.", "I shop at the store."),
                ("Tukone nganggo kertu.", "Pay with a card."),
                ("Matur nuwun, bakule.", "Thank you, seller."),
            ])
        ),
        "how_it_works": (
            "Market sentences run on the bargaining arc: Regane pira? "
            "(how much?) -> Larange! (expensive!) -> Oleh kurang? (can "
            "it be less?) -> Wis, dadi (deal). The seller is bakul, the "
            "price rega, the change susuk. Quantity words (sithik - a "
            "little, akeh - a lot) tune the haggle; ditimbang (weighed) "
            "and dibungkus (wrapped) finish the sale. Bargain one real "
            "or imagined purchase through the full arc aloud and the "
            "market is yours."
        ),
        "key_points": [
            "Bargaining arc: pira? -> larang -> oleh kurang? -> dadi.",
            "bakul (seller), rega (price), susuk (change).",
            "sithik / akeh tune quantity; ditimbang / dibungkus finish.",
            "mbayar awis (cash) vs nganggo kertu (card).",
            "20 shopping sentences, fully translated.",
        ],
        "requirements": [
            "Bargain a full purchase through the arc aloud.",
            "Ask prices for five market goods.",
            "Pay, take change, and thank the seller.",
        ],
        "standards": ["Forms follow the Central Javanese standard."],
        "citations": [CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the market is the sworn exchange - rega "
            "named honestly, kurang asked boldly, dadi sealed fairly. "
            "The Signature Language Method haggles as covenant: never "
            "cheat the bakul, never shame the buyer, and every susuk "
            "returned keeps the peace of the pasar."
        ),
        "drill": {"market": ["bakul", "rega", "susuk", "pasar", "toko"],
                  "arc": ["Regane pira?", "Larange!", "Oleh kurang?",
                          "Wis, dadi."]},
        "must_contain": ["Oleh kurang", "Susuk", "Bakule", "dadi"],
    },
    {
        "key": "social",
        "name": "Javanese Friendship and Social Life Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences of meeting people, invitations, and "
            "celebrations. Guyub rukun (harmonious togetherness) and "
            "gotong royong (mutual cooperation) are the moral center:\n" +
            _num_lines([
                ("Sugeng pinanggih.", "Nice to meet you."),
                ("Jenengku Budi.", "My name is Budi."),
                ("Kowe saka ngendi?", "Where are you from?"),
                ("Aku saka Solo.", "I am from Solo."),
                ("Kita kanca lawas.", "We are old friends."),
                ("Ayo dolan menyang omahku.", "Come visit my house."),
                ("Monggo pinarak.", "Please come in and sit."),
                ("Aku ngundang kowe.", "I invite you."),
                ("Rawuha ing pestaku.", "Come to my party."),
                ("Sugeng ambal warsa!", "Happy birthday!"),
                ("Mugi-mugi panjang umur.", "May you have a long life."),
                ("Kita mangan bebarengan.", "We eat together."),
                ("Guyub rukun.", "Harmonious togetherness."),
                ("Gotong royong.", "Mutual cooperation."),
                ("Aku seneng ketemu kowe.", "I am glad to meet you."),
                ("Kanca iku penting.", "Friends are important."),
                ("Aja lali kabar-kabar.", "Do not forget to keep in touch."),
                ("Kita foto bebarengan.", "We take a photo together."),
                ("Nganti ketemu maneh.", "Until we meet again."),
                ("Sugeng tindak.", "Safe travels (farewell)."),
            ])
        ),
        "how_it_works": (
            "Social sentences run on the togetherness words - bebarengan "
            "(together), guyub rukun (harmonious unity), gotong royong "
            "(mutual help) - the moral center of Javanese social life. "
            "Invitations use ngundang and rawuh (come, polite); "
            "introductions use jenengku and saka ngendi. Celebrations "
            "bless with mugi-mugi (may...). Host one imagined guest "
            "from pinanggih to sugeng tindak - greeting, invitation, "
            "meal, farewell - and the social script is yours."
        ),
        "key_points": [
            "guyub rukun and gotong royong: the social moral center.",
            "ngundang / rawuh invite; jenengku / saka ngendi introduce.",
            "mugi-mugi opens blessings.",
            "Full guest script: pinanggih -> pinarak -> mangan -> tindak.",
            "20 social sentences, fully translated.",
        ],
        "requirements": [
            "Introduce yourself fully in Javanese.",
            "Invite a friend to a meal aloud.",
            "Bless someone with a mugi-mugi sentence.",
        ],
        "standards": ["Forms follow the Central Javanese standard."],
        "citations": [CIT_ERRINGTON, CIT_ROBSON],
        "sig_lens": (
            "The Signature read: friendship is the sworn circle - guyub "
            "rukun its unbroken ring, gotong royong its shared strength. "
            "The Signature Language Method enters the circle properly: "
            "greet with pinanggih, invite with rawuh, feast bebarengan, "
            "and part with tindak, because no one leaves the circle "
            "unblessed."
        ),
        "drill": {"social": ["guyub rukun", "gotong royong", "bebarengan",
                             "ngundang", "rawuh", "mugi-mugi"]},
        "must_contain": ["Guyub rukun", "Gotong royong", "pinanggih",
                         "Mugi-mugi"],
    },
    {
        "key": "tech",
        "name": "Javanese Technology and Communication Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences of phone, internet, computer, and "
            "messaging:\n" +
            _num_lines([
                ("Aku duwe HP anyar.", "I have a new phone."),
                ("Teleponku muni.", "My phone rings."),
                ("Aku nelpon ibuku.", "I call my mother."),
                ("Sinyale apik.", "The signal is good."),
                ("Baterene entek.", "The battery is dead."),
                ("Dicas dhisik.", "Charge it first."),
                ("Aku ngirim pesan.", "I send a message."),
                ("Wangsulana pesanku.", "Reply to my message."),
                ("Aku mbukak internet.", "I open the internet."),
                ("Situs iki apik.", "This site is good."),
                ("Aku golek informasi.", "I search for information."),
                ("Komputerku cepet.", "My computer is fast."),
                ("Aku ngetik layang.", "I type a letter."),
                ("Berkase dikirim.", "The file is sent."),
                ("Aku nonton video.", "I watch a video."),
                ("Fotone apik.", "The photo is good."),
                ("Aku motret kembang.", "I photograph a flower."),
                ("Aja lali disimpen.", "Do not forget to save it."),
                ("Sandi kudu rahasia.", "The password must stay secret."),
                ("Matur nuwun infone.", "Thanks for the info."),
            ])
        ),
        "how_it_works": (
            "Technology sentences borrow freely - HP, internet, komputer, "
            "video, foto - and Javanese verbs do the rest: nelpon (call), "
            "ngirim (send), mbukak (open), golek (search), ngetik (type), "
            "nonton (watch), motret (photograph), nyimpen (save). Commands "
            "protect the work: aja lali disimpen, dicas dhisik. Narrate "
            "your next hour with your phone in Javanese - muni, ngirim, "
            "nonton, nyimpen - and the modern words naturalize."
        ),
        "key_points": [
            "Borrowed tech nouns + Javanese verbs: nelpon, ngirim, mbukak.",
            "Phone words: muni, sinyal, batere, dicas.",
            "Internet words: situs, golek informasi, berkas, dikirim.",
            "aja lali disimpen guards the work.",
            "20 technology sentences, fully translated.",
        ],
        "requirements": [
            "Narrate one phone session in Javanese.",
            "Give three tech commands (charge, save, send).",
            "Explain a password rule in Javanese.",
        ],
        "standards": ["Borrowings follow common Javanese usage."],
        "citations": [CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the new tools are sworn messengers too "
            "- HP the swift runner, internet the far-seeing eye. The "
            "Signature Language Method puts Javanese verbs on borrowed "
            "nouns and sends them running: nelpon, ngirim, nyimpen, "
            "because the language that names the tool commands it."
        ),
        "drill": {"tech_verbs": ["nelpon", "ngirim", "mbukak", "golek",
                                 "ngetik", "nonton", "motret", "nyimpen"],
                  "tech_nouns": ["HP", "internet", "komputer", "video",
                                 "foto", "sinyal", "batere"]},
        "must_contain": ["nelpon", "disimpen", "Sinyal", "HP"],
    },
]

ENTRIES_21_34 = [
    {
        "key": "tenses",
        "name": "Javanese Verb Tenses in Sentences",
        "group": "Grammar in Action",
        "ladder_rank": 21,
        "ladder_tier": "advanced",
        "description": (
            "Javanese verbs do not conjugate - time rides on helper words. "
            "PAST: wis (already) - Aku wis mangan (I already ate). Lagi "
            "wae (just now) and mau mark recent past. PRESENT: lagi "
            "(right now) for ongoing action; bare verb for habit. FUTURE: "
            "arep (about to) and bakal (will). NOT YET: durung. EVER: "
            "tau (have ever). Six sentences per time frame, translated:\n"
            "PAST:\n" +
            _num_lines([
                ("Aku wis mangan.", "I have already eaten."),
                ("Dheweke wis teka wingi.", "He/she already came yesterday."),
                ("Aku lagi wae tangi.", "I just woke up."),
                ("Bocah iku mau nangis.", "That child was crying just now."),
                ("Kita wis sinau.", "We have studied."),
                ("Ibuku wis masak.", "My mother has cooked."),
            ]) + "\nPRESENT:\n" +
            _num_lines([
                ("Aku lagi mangan.", "I am eating (right now)."),
                ("Dheweke lagi turu.", "He/she is sleeping."),
                ("Aku mangan sego saben dina.", "I eat rice every day. (habit)"),
                ("Bocah-bocah padha dolan.", "The children are playing."),
                ("Aku kerja ing kantor.", "I work at the office. (habit)"),
                ("Srengengene lagi sumunar.", "The sun is shining now."),
            ]) + "\nFUTURE:\n" +
            _num_lines([
                ("Aku arep lunga.", "I am about to go."),
                ("Dheweke bakal teka sesuk.", "He/she will come tomorrow."),
                ("Kita arep mangan.", "We are about to eat."),
                ("Udan arep deres.", "It is about to rain heavily."),
                ("Aku bakal sinau bengi iki.", "I will study tonight."),
                ("Sesuk aku arep menyang pasar.", "Tomorrow I will go to the market."),
            ]) + "\nNOT YET / EVER:\n" +
            _num_lines([
                ("Aku durung mangan.", "I have not eaten yet."),
                ("Dheweke durung teka.", "He/she has not come yet."),
                ("Aku tau menyang Bali.", "I have been to Bali (ever)."),
                ("Kowe tau mangan gudeg?", "Have you ever eaten gudeg?"),
            ])
        ),
        "how_it_works": (
            "Think of the verb as a timeless engine and the helper word "
            "as the gear: wis shifts to completed past, lagi to ongoing "
            "present, arep/bakal to future, durung to not-yet, tau to "
            "ever-experienced. The verb itself never changes shape - "
            "mangan is mangan in every gear. Aspect shades refine it: "
            "lagi wae (just now), wis tau (have ever, completed "
            "experience), arep ... (intention). To master time, drill "
            "one verb through all six gears until the helpers feel like "
            "tenses."
        ),
        "key_points": [
            "No conjugation - helpers mark time: wis, lagi, arep, bakal, durung, tau.",
            "wis = completed past; lagi = ongoing; arep/bakal = future.",
            "durung = not yet; tau = ever-experienced.",
            "Bare verb = habitual present: Aku mangan saben dina.",
            "lagi wae / mau mark the immediate past.",
            "22 tense sentences, fully translated.",
        ],
        "requirements": [
            "Run five verbs through all six time gears.",
            "Narrate yesterday, today, and tomorrow in Javanese.",
            "Ask someone if they have ever (tau) done three things.",
        ],
        "standards": ["Usage follows Central Javanese standard."],
        "citations": [CIT_OGLOBLIN, CIT_UHLENBECK],
        "sig_lens": (
            "The Signature read: time is the sworn march - wis the "
            "vanguard done, lagi the column moving, arep the scouts "
            "ahead, durung the rear not yet arrived. The Signature "
            "Language Method marches every verb through the six gears "
            "until the tongue keeps time like a drum."
        ),
        "drill": {"past": 6, "present": 6, "future": 6, "extra": 4,
                  "helpers": ["wis", "lagi", "arep", "bakal", "durung",
                              "tau", "lagi wae", "mau"]},
        "must_contain": ["wis", "arep", "durung", "tau"],
    },
    {
        "key": "qa",
        "name": "Javanese Questions and Answers",
        "group": "Grammar in Action",
        "ladder_rank": 22,
        "ladder_tier": "advanced",
        "description": (
            "Twenty question-and-answer pairs covering who, what, where, "
            "when, why, and how - 20 pairs:\n" +
            _num_lines([
                ("Sapa jenengmu? - Jenengku Sari.", "What is your name? - My name is Sari. (who/what)"),
                ("Sapa sing teka? - Bapak sing teka.", "Who came? - Father came. (who)"),
                ("Apa iki? - Iki buku.", "What is this? - This is a book. (what)"),
                ("Kowe mangan apa? - Aku mangan sego.", "What are you eating? - I am eating rice. (what)"),
                ("Kowe neng endi? - Aku neng omah.", "Where are you? - I am at home. (where)"),
                ("Pasar endi? - Pasar Beringharjo.", "Which market? - Beringharjo Market. (which)"),
                ("Kapan tekamu? - Wingi sore.", "When did you arrive? - Yesterday afternoon. (when)"),
                ("Kapan lungamu? - Sesuk esuk.", "When will you go? - Tomorrow morning. (when)"),
                ("Kenapa kowe nangis? - Aku sedhih.", "Why are you crying? - I am sad. (why)"),
                ("Yagene ora teka? - Aku lara.", "Why did you not come? - I was sick. (why)"),
                ("Piye carane? - Gampang.", "How is it done? - Easy. (how)"),
                ("Piye kabare? - Apik-apik wae.", "How are you? - Just fine. (how)"),
                ("Pira regane? - Sewu rupiah.", "How much? - A thousand rupiah. (how many)"),
                ("Ana pira bocah? - Ana lima.", "How many children? - Five. (how many)"),
                ("Kowe wis mangan? - Wis.", "Have you eaten? - Already. (yes/no)"),
                ("Apa kowe arep lunga? - Iya, arep lunga.", "Will you go? - Yes, about to go. (yes/no)"),
                ("Iki bukumu? - Dudu, iki bukune.", "Is this your book? - No, it is his/hers. (yes/no)"),
                ("Kowe seneng? - Seneng banget.", "Are you happy? - Very happy. (yes/no)"),
                ("Sapa wae sing rawuh? - Kabeh kanca.", "Who all came? - All the friends. (who-all)"),
                ("Neng endi wae? - Neng pasar lan toko.", "Where all? - At the market and the store. (where-all)"),
            ])
        ),
        "how_it_works": (
            "Questions open with the question word - sapa, apa, endi, "
            "kapan, kenapa/yagene, piye, pira - and rise in intonation; "
            "answers drop the question word and keep the rest. Yes/no "
            "questions are statements with rising intonation: Kowe wis "
            "mangan? answered with wis, iya, or mboten. The wae suffix "
            "broadens: sapa wae (who all), neng endi wae (where all). "
            "Practice by interviewing yourself: ask all six question "
            "types about your day and answer every one."
        ),
        "key_points": [
            "Question words front the sentence: sapa, apa, endi, kapan, kenapa, piye, pira.",
            "Yes/no questions = statement + rising intonation.",
            "Answers drop the question word, keep the predicate.",
            "wae broadens: sapa wae (who all).",
            "yagene is the ngoko why; kenging menapa the krama why.",
            "20 Q&A pairs, fully translated.",
        ],
        "requirements": [
            "Ask and answer all six question types about today.",
            "Interview a friend (real or imagined) with ten questions.",
            "Answer five yes/no questions three ways: iya, wis, mboten.",
        ],
        "standards": ["Forms follow the Central Javanese standard."],
        "citations": [CIT_ROBSON, CIT_OGLOBLIN],
        "sig_lens": (
            "The Signature read: the question is the sworn summons - "
            "sapa calls the who, endi the where, kapan the when, and "
            "the answer must appear and testify. The Signature Language "
            "Method summons daily: six questions, six true answers, "
            "until asking feels like breathing."
        ),
        "drill": {"pairs": 20,
                  "qwords": ["sapa", "apa", "endi", "kapan", "kenapa",
                             "yagene", "piye", "pira"]},
        "must_contain": ["Sapa", "Kapan", "Pira", "20"],
    },
    {
        "key": "commands",
        "name": "Javanese Commands and Requests",
        "group": "Grammar in Action",
        "ladder_rank": 23,
        "ladder_tier": "advanced",
        "description": (
            "Twenty imperatives and polite requests - direct ngoko "
            "commands versus softened krama requests:\n" +
            _num_lines([
                ("Lungguh!", "Sit! (direct)"),
                ("Monggo lungguh.", "Please sit. (polite)"),
                ("Mangan!", "Eat! (direct)"),
                ("Monggo dhahar.", "Please eat. (krama polite)"),
                ("Tutup lawange!", "Close the door! (direct)"),
                ("Nuwun sewu, lawange ditutup.", "Excuse me, please close the door. (softened)"),
                ("Ayo lunga!", "Let us go! (inviting)"),
                ("Monggo tindak.", "Please go ahead. (polite)"),
                ("Ndeleng iki!", "Look at this! (direct)"),
                ("Coba dideleng.", "Try looking at it. (softened)"),
                ("Aja rame!", "Do not be noisy! (prohibition)"),
                ("Aja lali.", "Do not forget. (gentle prohibition)"),
                ("Tulung aku!", "Help me! (urgent)"),
                ("Nyuwun tulung.", "I ask for help. (polite request)"),
                ("Njaluk ngapura.", "I ask forgiveness. (request)"),
                ("Wenehana aku banyu.", "Give me water. (-a imperative)"),
                ("Maringana bukune.", "Hand over the book. (-a imperative)"),
                ("Dakjaluk tulung.", "I humbly ask help. (humble request)"),
                ("Sumangga.", "Please proceed (you first). (deferential)"),
                ("Aja kesusu.", "Do not rush. (gentle command)"),
            ])
        ),
        "how_it_works": (
            "Commands harden or soften by level. The bare verb is the "
            "direct order (Lungguh!); the -a/-ana suffix sharpens it "
            "(Wenehana!); aja forbids (Aja rame!). Politeness wraps the "
            "same order in monggo (please proceed), nuwun sewu (excuse "
            "me), coba (try), or the krama verb (dhahar for mangan). "
            "Requests humble the speaker: nyuwun tulung, dakjaluk. The "
            "rule: the closer the bond, the barer the verb; the greater "
            "the distance, the thicker the wrapping. Give five orders to "
            "a friend and five wrapped requests to an elder today."
        ),
        "key_points": [
            "Bare verb = direct command; -a/-ana sharpens it.",
            "aja forbids: Aja rame! Aja lali.",
            "monggo / nuwun sewu / coba soften any order.",
            "Krama verbs (dhahar) politely replace ngoko ones (mangan).",
            "nyuwun tulung / dakjaluk humble the request.",
            "20 command/request sentences, formal vs informal.",
        ],
        "requirements": [
            "Give five direct orders and five softened requests.",
            "Forbid three things with aja.",
            "Request help three ways: urgent, polite, humble.",
        ],
        "standards": ["Forms follow the Central Javanese standard."],
        "citations": [CIT_ERRINGTON, CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the command is the sworn order - bare "
            "to friends, wrapped in silk to elders, never shouted "
            "upward. The Signature Language Method drills command as "
            "covenant discipline: order down the rank with a bare verb, "
            "request up the rank with monggo, and the hierarchy holds."
        ),
        "drill": {"direct": 5, "softened": 5, "prohibitions": 4,
                  "requests": 6,
                  "softeners": ["monggo", "nuwun sewu", "coba", "nyuwun"]},
        "must_contain": ["Monggo", "Aja", "-a", "Nyuwun"],
    },
    {
        "key": "descriptions",
        "name": "Javanese Descriptions of People and Places",
        "group": "Grammar in Action",
        "ladder_rank": 24,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences describing people, places, and things in "
            "detail:\n" +
            _num_lines([
                ("Ibuku wong wadon sing ayu lan sabar.", "My mother is a beautiful and patient woman."),
                ("Bapakku dhuwur lan gagah.", "My father is tall and strong."),
                ("Kancaku rambute ireng lan dawa.", "My friend's hair is black and long."),
                ("Guruku pinter lan lucu.", "My teacher is smart and funny."),
                ("Bocah iku mripate biru.", "That child's eyes are blue."),
                ("Simbahku ramah banget.", "My grandparent is very kind."),
                ("Kutha Solo rame lan apik.", "Solo city is busy and nice."),
                ("Desaku ayem lan ijo.", "My village is peaceful and green."),
                ("Pantaine jembar lan resik.", "The beach is wide and clean."),
                ("Gununge dhuwur lan gagah.", "The mountain is tall and majestic."),
                ("Sawah ijo ombak-ombak.", "The rice fields wave green."),
                ("Omahku cilik nanging resik.", "My house is small but clean."),
                ("Kamar iki jembar lan padhang.", "This room is spacious and bright."),
                ("Bukune kandel lan abot.", "The book is thick and heavy."),
                ("Klambine abang lan anyar.", "The shirt is red and new."),
                ("Sego pecel iku enak lan murah.", "The pecel rice is tasty and cheap."),
                ("Wayang kulit iku seni sing adi.", "Shadow puppetry is a noble art."),
                ("Candi Borobudur gedhe lan nggumunake.", "Borobudur Temple is big and amazing."),
                ("Kraton Ngayogyakarta agung.", "The Yogyakarta Palace is grand."),
                ("Basa Jawa alus lan endah.", "Javanese is refined and beautiful."),
            ])
        ),
        "how_it_works": (
            "Descriptions stack adjectives after the noun with lan "
            "(and) or nanging (but): ayu lan sabar, cilik nanging resik. "
            "Body-part possession sharpens portraits - rambute ireng "
            "(his/her hair is black), mripate biru. The sing relative "
            "clause adds a whole portrait in one breath: wong wadon "
            "sing ayu lan sabar. Places take the same stacking: rame "
            "lan apik, jembar lan resik. Describe one person and one "
            "place with three stacked traits each, aloud, and the "
            "descriptive engine is running."
        ),
        "key_points": [
            "Stack traits with lan (and): ayu lan sabar.",
            "Contrast with nanging (but): cilik nanging resik.",
            "Body-part + -e sharpens portraits: rambute ireng.",
            "sing clauses pack full descriptions: wong sing ayu.",
            "20 descriptive sentences, fully translated.",
        ],
        "requirements": [
            "Describe three people with stacked traits.",
            "Describe two places in three sentences each.",
            "Use one sing relative clause per description.",
        ],
        "standards": ["Forms follow the Central Javanese standard."],
        "citations": [CIT_ROBSON],
        "sig_lens": (
            "The Signature read: description is the sworn portrait - "
            "each trait a brushstroke laid true, lan joining, nanging "
            "cutting light against shadow. The Signature Language "
            "Method paints portraits that testify: stack the traits, "
            "sharpen with the body-word, and the person stands "
            "recognizable in the sentence."
        ),
        "drill": {"stackers": ["lan", "nanging"], "relative": "sing",
                  "body_parts": ["rambut", "mripat", "kulit"]},
        "must_contain": ["lan sabar", "nanging", "sing ayu", "rambute"],
    },
    {
        "key": "story1",
        "name": "Javanese Story I: The Little Farmer",
        "group": "Stories and Idioms",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence simple story in Javanese, with line-by-line "
            "English translation:\n" +
            _num_lines([
                ("Ana bocah tani jenenge Bagus.", "There is a farmer boy named Bagus."),
                ("Saben esuk dheweke tangi gasik.", "Every morning he wakes up early."),
                ("Dheweke adus banjur sarapan.", "He bathes, then has breakfast."),
                ("Banjur dheweke menyang sawah.", "Then he goes to the rice field."),
                ("Ing sawah ana pari ijo.", "In the field there is green rice."),
                ("Bagus nyirami pari saben dina.", "Bagus waters the rice every day."),
                ("Kancane teka lan mbantu.", "His friend comes and helps."),
                ("Bebarengan padha nyambut gawe.", "Together they work."),
                ("Sore dheweke mulih kanthi bungah.", "In the afternoon he goes home happily."),
                ("Urip tani iku ayem.", "A farmer's life is peaceful."),
            ])
        ),
        "how_it_works": (
            "The story runs on sequence words - saben esuk (every "
            "morning), banjur (then), sore (in the afternoon) - and "
            "present-habit verbs: tangi, adus, nyirami. Ana opens the "
            "tale (there is/was); the final line lands the moral (urip "
            "tani iku ayem). Read each Javanese line aloud, cover the "
            "English, translate from memory, then uncover and check. "
            "Retell the whole story without looking: ten lines, in "
            "order, is the first storytelling victory."
        ),
        "key_points": [
            "Sequence words carry the plot: saben esuk, banjur, sore.",
            "ana opens a story; the last line lands the moral.",
            "Present-habit verbs narrate routine: tangi, nyirami.",
            "10 sentences, line-by-line English translation.",
            "Read-cover-translate-check is the study method.",
        ],
        "requirements": [
            "Retell the story in order without looking.",
            "Change the hero's name and retell it.",
            "Add two sentences of your own to the tale.",
        ],
        "standards": ["Story Javanese follows the Central standard."],
        "citations": [CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the story is the sworn chronicle - ten "
            "lines, each keeping its watch in order, from tangi gasik "
            "to mulih kanthi bungah. The Signature Language Method "
            "treats the first story as a first oath: retell it true, "
            "in order, and the tongue is sworn a storyteller."
        ),
        "drill": {"lines": 10, "sequence": ["saben esuk", "banjur",
                                            "sore"],
                  "hero": "Bagus"},
        "must_contain": ["Bagus", "banjur", "sawah", "ayem"],
    },
    {
        "key": "story2",
        "name": "Javanese Story II: The Lost Buffalo",
        "group": "Stories and Idioms",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the past tense, with line-by-line "
            "English translation. Wingi (yesterday) anchors the tale:\n" +
            _num_lines([
                ("Wingi sore kebone Pak Karta ilang.", "Yesterday afternoon Mr. Karta's buffalo was lost."),
                ("Pak Karta wis nggoleki tekan ngendi-endi.", "Mr. Karta had searched everywhere."),
                ("Dheweke takon marang tangga-tanggane.", "He asked his neighbors."),
                ("Ora ana sing weruh.", "No one had seen it."),
                ("Banjur dheweke menyang pinggir kali.", "Then he went to the riverbank."),
                ("Ing kana kebone lagi ngombe.", "There the buffalo was drinking."),
                ("Pak Karta bungah banget.", "Mr. Karta was very glad."),
                ("Dheweke nuntun kebone mulih.", "He led the buffalo home."),
                ("Tangga-tanggane padha ngguyu.", "The neighbors laughed."),
                ("Kebo iku wis ketemu.", "The buffalo was found."),
            ])
        ),
        "how_it_works": (
            "Past narration leans on wis (already/completed) and time "
            "anchors - wingi sore (yesterday afternoon) - while lagi "
            "marks what was ongoing when found (lagi ngombe). The "
            "search verbs - nggoleki (search for), takon (ask), ketemu "
            "(found/meet) - drive the plot; padha marks the group's "
            "shared action (padha ngguyu). Retell it as a completed "
            "past: every verb with wis where the action finished, and "
            "the story lands in yesterday where it belongs."
        ),
        "key_points": [
            "wis + time anchors narrate the completed past.",
            "lagi marks ongoing action inside past narration.",
            "Search verbs drive plot: nggoleki, takon, ketemu.",
            "padha marks shared group action.",
            "10 sentences, line-by-line English translation.",
        ],
        "requirements": [
            "Retell the story entirely in the past.",
            "Change the lost animal and retell it.",
            "Tell one true past event from your week.",
        ],
        "standards": ["Story Javanese follows the Central standard."],
        "citations": [CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the past tale is the sworn record - "
            "wingi sore fixed, wis sealing each finished deed, ketemu "
            "closing the search. The Signature Language Method keeps "
            "the record straight: anchor the time, seal with wis, and "
            "the past stands sworn and findable."
        ),
        "drill": {"lines": 10, "past_markers": ["wis", "wingi", "mau"],
                  "search_verbs": ["nggoleki", "takon", "ketemu"]},
        "must_contain": ["kebo", "nggoleki", "ketemu", "Wingi"],
    },
    {
        "key": "story3",
        "name": "Javanese Story III: The Voyage Tomorrow",
        "group": "Stories and Idioms",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in future and conditional forms, with "
            "line-by-line English translation:\n" +
            _num_lines([
                ("Sesuk Laras arep lunga menyang Semarang.", "Tomorrow Laras will go to Semarang."),
                ("Dheweke bakal numpak sepur esuk.", "She will take the morning train."),
                ("Yen udan, dheweke arep nggawa payung.", "If it rains, she will bring an umbrella."),
                ("Ibune bakal melu yen sehat.", "Her mother will join if she is well."),
                ("Padha arep tuku oleh-oleh.", "They will buy souvenirs."),
                ("Laras arep ketemu kanca lawase.", "Laras will meet her old friend."),
                ("Kancane bakal njemput ing setasion.", "Her friend will pick her up at the station."),
                ("Yen ora udan, padha arep mlaku-mlaku.", "If it does not rain, they will stroll."),
                ("Sore padha arep mulih.", "In the afternoon they will return."),
                ("Muga-muga selamet tekan omah.", "May they arrive home safely."),
            ])
        ),
        "how_it_works": (
            "Future narration runs on arep (about to) and bakal (will), "
            "with yen (if) opening every conditional branch: Yen udan "
            "... arep ... The plan verbs - lunga, numpak, tuku, ketemu, "
            "njemput, mulih - march in intention order; muga-muga "
            "closes with a blessing on the unmade future. Tell your "
            "own tomorrow the same way: sesuk + arep + plan, one yen "
            "branch for the weather, and a muga-muga to seal it."
        ),
        "key_points": [
            "arep / bakal narrate the future; yen opens conditionals.",
            "Plan verbs march in intention order.",
            "muga-muga blesses the unmade future.",
            "Yen ora udan shows the negative conditional.",
            "10 sentences, line-by-line English translation.",
        ],
        "requirements": [
            "Narrate your tomorrow in ten arep sentences.",
            "Add two yen branches (weather, health).",
            "Close with a muga-muga blessing.",
        ],
        "standards": ["Story Javanese follows the Central standard."],
        "citations": [CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the future tale is the sworn vow - "
            "arep the promise, yen the condition, muga-muga the seal. "
            "The Signature Language Method vows tomorrow aloud: plan "
            "the march, branch for the rain, bless the return, and the "
            "tongue learns to command the days ahead."
        ),
        "drill": {"lines": 10, "future_markers": ["arep", "bakal",
                                                  "sesuk"],
                  "conditionals": ["yen", "yen ora"]},
        "must_contain": ["arep", "bakal", "yen", "Muga-muga"],
    },
    {
        "key": "idioms",
        "name": "Javanese Idioms and Proverbs",
        "group": "Stories and Idioms",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "description": (
            "Twenty idioms and proverbs - literal translation, real "
            "meaning, and an example sentence. 20 idioms:\n" +
            _num_lines([
                ("Alon-alon waton kelakon. [Slow but sure gets it done.] Tegese: aja kesusu. Tuladha: Sinaua alon-alon waton kelakon.",
                 "Slowly but surely gets it done. Meaning: do not rush. Example: Study slowly but surely."),
                ("Becik ketitik ala ketara. [Good shows, bad shows.] Tegese: tumindak becik utawa ala mesthi ketok. Tuladha: Aja goroh, becik ketitik ala ketara.",
                 "Good and evil both show. Meaning: deeds always surface. Example: Do not lie; good and evil both show."),
                ("Kacang lali kulite. [The peanut forgets its shell.] Tegese: wong lali asale. Tuladha: Dheweke sugih banjur kacang lali kulite.",
                 "The peanut forgets its shell. Meaning: one who forgets their origins. Example: He got rich, then forgot his roots."),
                ("Kebo mulih kandhang. [The buffalo returns to its pen.] Tegese: bali menyang asal. Tuladha: Sawise suwe, dheweke kebo mulih kandhang.",
                 "The buffalo returns to its pen. Meaning: returning to one's origins. Example: After long, he returned home."),
                ("Gajah mati ninggal gading. [The elephant dies leaving ivory.] Tegese: wong becik ninggal jeneng apik. Tuladha: Simbah gajah mati ninggal gading.",
                 "The elephant dies leaving ivory. Meaning: the good leave a good name. Example: Grandfather left a good name."),
                ("Sapa nandur bakal ngundhuh. [Who plants will harvest.] Tegese: tumindak bali. Tuladha: Sing sabar, sapa nandur bakal ngundhuh.",
                 "Who plants will harvest. Meaning: deeds return. Example: Be patient; who plants will harvest."),
                ("Mangan ora mangan waton kumpul. [Eat or not, as long as together.] Tegese: guyub luwih penting. Tuladha: Mangan ora mangan waton kumpul.",
                 "Eat or not, so long as together. Meaning: togetherness matters most. Example: Eat or not, so long as together."),
                ("Urip iku mung mampir ngombe. [Life is just stopping to drink.] Tegese: urip mung sedhela. Tuladha: Elinga, urip iku mung mampir ngombe.",
                 "Life is only stopping for a drink. Meaning: life is brief. Example: Remember, life is brief."),
                ("Ana dina ana upa. [Where there is a day there is sustenance.] Tegese: rejeki mesthi ana. Tuladha: Aja kuwatir, ana dina ana upa.",
                 "Where there is a day there is sustenance. Meaning: provision always comes. Example: Do not worry; provision comes."),
                ("Sepi ing pamrih rame ing gawe. [Quiet in desire, busy in work.] Tegese: ikhlas nyambut gawe. Tuladha: Dadi pemimpin kudu sepi ing pamrih rame ing gawe.",
                 "Quiet in self-interest, busy in work. Meaning: selfless diligence. Example: A leader must be selfless and diligent."),
                ("Memayu hayuning bawana. [Beautify the world's beauty.] Tegese: njaga alam. Tuladha: Kita kudu memayu hayuning bawana.",
                 "Beautify the beauty of the world. Meaning: care for the world. Example: We must care for the world."),
                ("Sura dira jayaningrat lebur dening pangastuti. [Courage melts before virtue.] Tegese: kabecikan ngalahake kekuwatan. Tuladha: Sura dira jayaningrat lebur dening pangastuti.",
                 "Daring courage melts before virtue. Meaning: goodness defeats force. Example: Goodness defeats force."),
                ("Ojo dumeh. [Do not feel superior.] Tegese: aja sombong. Tuladha: Sugih ya sugih, ning ojo dumeh.",
                 "Do not feel mighty. Meaning: do not be arrogant. Example: Rich is fine, but do not feel superior."),
                ("Narima ing pandum. [Accept one's lot.] Tegese: nrima. Tuladha: Urip kudu narima ing pandum.",
                 "Accept what is apportioned. Meaning: contentment. Example: Life needs contentment."),
                ("Desa mawa cara negara mawa tata. [Each village its custom.] Tegese: ngajeni adat. Tuladha: Elinga, desa mawa cara negara mawa tata.",
                 "Each village its way, each land its order. Meaning: respect local custom. Example: Respect local custom."),
                ("Witing tresna jalaran saka kulina. [Love grows from familiarity.] Tegese: tresna tuwuh saka biasa. Tuladha: Witing tresna jalaran saka kulina.",
                 "Love grows from habit. Meaning: love grows from closeness. Example: Love grows from familiarity."),
                ("Kaya banyu mili. [Like flowing water.] Tegese: lancar. Tuladha: Rejekine kaya banyu mili.",
                 "Like flowing water. Meaning: smooth and continuous. Example: His fortune flows like water."),
                ("Adigang adigung adiguna. [Power, pride, prowess.] Tegese: sombong merga kuwasa. Tuladha: Aja adigang adigung adiguna.",
                 "Power, pride, and prowess. Meaning: arrogance from power. Example: Do not be arrogant with power."),
                ("Ngono ya ngono ning aja ngono. [Like that, but not like that.] Tegese: samubarang ana watese. Tuladha: Guyon ngono ya ngono ning aja ngono.",
                 "Like that yes, but not like that. Meaning: everything has limits. Example: Joke, but know the limits."),
                ("Cilik diukum gedhe dioyak. [Small punished, big chased.] Tegese: ora adil. Tuladha: Aturane cilik diukum gedhe dioyak.",
                 "The small are punished, the big are chased. Meaning: injustice. Example: The rules punish only the small."),
            ])
        ),
        "how_it_works": (
            "Idioms work as compressed philosophy - one image carrying "
            "a whole ethic: the peanut forgetting its shell warns "
            "against arrogance; the buffalo returning home blesses "
            "return. Proverbs open counsel (Elinga... - remember) and "
            "close arguments; dropping alon-alon waton kelakon into "
            "advice marks you as culturally fluent. Learn five by "
            "heart - the image, the meaning, one example - and use one "
            "per week in real counsel."
        ),
        "key_points": [
            "Idioms compress ethics into images: peanut, buffalo, elephant.",
            "Proverbs open counsel and close arguments.",
            "Using one correctly marks cultural fluency.",
            "20 idioms: literal translation + real meaning + example sentence.",
        ],
        "requirements": [
            "Memorize five idioms with image, meaning, and example.",
            "Use one idiom in real advice this week.",
            "Explain three idioms to someone else.",
        ],
        "standards": ["Idioms follow Central Javanese usage."],
        "citations": [CIT_ROBSON, CIT_ERRINGTON],
        "sig_lens": (
            "The Signature read: the proverb is the sworn law of the "
            "elders - alon-alon waton kelakon its patient statute, ojo "
            "dumeh its guard against pride. The Signature Language "
            "Method treats each idiom as inherited covenant: carry the "
            "image, keep the meaning, speak it in counsel, and the "
            "ancestors testify through your tongue."
        ),
        "drill": {"idioms": 20,
                  "images": ["kacang", "kebo", "gajah", "banyu", "pari"]},
        "must_contain": ["Alon-alon waton kelakon", "Ojo dumeh",
                         "kacang lali kulite", "20"],
    },
    {
        "key": "registers",
        "name": "Javanese Formal and Polite Registers",
        "group": "Conversation and Registers",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen formal-versus-informal pairs - the same meaning in "
            "ngoko (to friends) and krama (to elders, in letters, in "
            "business):\n" +
            _num_lines([
                ("Aku arep lunga. / Kula badhe tindak.", "I will go. (ngoko / krama)"),
                ("Kowe neng endi? / Sampeyan wonten pundi?", "Where are you? (ngoko / krama)"),
                ("Aku wis mangan. / Kula sampun nedha.", "I have eaten. (ngoko / krama)"),
                ("Jenengmu sapa? / Asma sampeyan sinten?", "What is your name? (ngoko / krama)"),
                ("Omahmu neng endi? / Griya sampeyan wonten pundi?", "Where is your house? (ngoko / krama)"),
                ("Aku ora ngerti. / Kula mboten mangertos.", "I do not understand. (ngoko / krama)"),
                ("Matur nuwun. / Matur nuwun.", "Thank you. (shared form)"),
                ("Nuwun sewu. / Nuwun sewu.", "Excuse me. (shared form)"),
                ("Aku njaluk ngapura. / Kula nyuwun pangapunten.", "I ask forgiveness. (ngoko / krama)"),
                ("Tulung aku. / Nyuwun tulung.", "Help me. (ngoko / krama)"),
                ("Kowe wis tuwa. / Sampeyan sampun sepuh.", "You are old. (ngoko / krama)"),
                ("Anakmu lanang apa wadon? / Putra sampeyan kakung menapa putri?", "Is your child a boy or girl? (ngoko / krama)"),
                ("Aku seneng. / Kula remen.", "I am happy. (ngoko / krama)"),
                ("Dheweke teka. / Piyambakipun rawuh.", "He/she comes. (ngoko / krama inggil)"),
                ("Piye kabare? / Kados pundi wartosipun?", "How are you? (ngoko / krama)"),
            ])
        ),
        "how_it_works": (
            "Register-switching replaces content words while the grammar "
            "holds still: aku->kula, kowe->sampeyan, mangan->nedha, "
            "arep->badhe, lunga->tindak, teka->rawuh, omah->griya, "
            "ngerti->mangertos. Krama inggil raises the other person "
            "further: dheweke->piyambakipun. The sentence frame never "
            "moves - only the words change rank. Practice by taking "
            "five ngoko sentences you own and promoting every word to "
            "krama; the frame will carry them."
        ),
        "key_points": [
            "Same grammar, different words: the frame never moves.",
            "Core swaps: aku/kula, kowe/sampeyan, mangan/nedha, lunga/tindak.",
            "Krama inggil honors the other: rawuh, piyambakipun, sepuh.",
            "Letters and business run in krama; elders get krama inggil.",
            "15 formal/informal pairs, fully translated.",
        ],
        "requirements": [
            "Promote five ngoko sentences to krama.",
            "Write a three-line polite letter opening.",
            "Address an elder in krama inggil for one minute.",
        ],
        "standards": ["Register forms follow Central Javanese usage."],
        "citations": [CIT_ERRINGTON, CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the register is the sworn uniform - "
            "ngoko the field dress of friends, krama the court dress "
            "of respect, krama inggil the ceremonial robe of honor. "
            "The Signature Language Method teaches the wardrobe: same "
            "body of grammar, changed garments of words, and the "
            "speaker always dressed for the rank of the room."
        ),
        "drill": {"pairs": 15,
                  "swaps": [["aku", "kula"], ["kowe", "sampeyan"],
                            ["mangan", "nedha"], ["lunga", "tindak"],
                            ["teka", "rawuh"], ["omah", "griya"],
                            ["ngerti", "mangertos"], ["dheweke",
                                                      "piyambakipun"]]},
        "must_contain": ["badhe tindak", "wonten pundi", "nedha",
                         "Piyambakipun"],
    },
    {
        "key": "complex",
        "name": "Javanese Compound and Complex Sentences",
        "group": "Conversation and Registers",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen long sentences with clauses, connectors, and "
            "relative clauses - parsed and translated:\n" +
            _num_lines([
                ("Aku tangi esuk, banjur adus, banjur sarapan. [sequence: banjur]", "I wake early, then bathe, then breakfast."),
                ("Dheweke lunga menyang pasar amarga ibune lara. [cause: amarga]", "He/she goes to the market because his/her mother is sick."),
                ("Yen udan, aku ora lunga. [condition: yen]", "If it rains, I will not go."),
                ("Senajan kesel, dheweke tetep kerja. [concession: senajan]", "Although tired, he/she keeps working."),
                ("Buku sing abang iku bukuku. [relative: sing]", "The book that is red is mine."),
                ("Wong sing teka wingi iku guruku. [relative: sing]", "The person who came yesterday is my teacher."),
                ("Aku tuku sego lan iwak ing pasar. [conjunction: lan]", "I buy rice and fish at the market."),
                ("Dheweke pinter nanging males. [contrast: nanging]", "He/she is smart but lazy."),
                ("Aku mangan nalika kanca teka. [time: nalika]", "I was eating when my friend arrived."),
                ("Sadurunge lunga, aku pamit. [time: sadurunge]", "Before leaving, I ask leave."),
                ("Sawise mangan, kita dolan. [time: sawise]", "After eating, we visit."),
                ("Supaya sehat, mangan sayur. [purpose: supaya]", "To be healthy, eat vegetables."),
                ("Aku sinau supaya lulus. [purpose: supaya]", "I study so that I pass."),
                ("Kebone ilang, mula dheweke nggoleki. [result: mula]", "The buffalo was lost, so he searched."),
                ("Aja rame, amarga bayi turu. [cause: amarga]", "Do not be noisy, because the baby sleeps."),
            ])
        ),
        "how_it_works": (
            "Complex sentences bolt clauses with connector words: lan "
            "(and), nanging (but), amarga (because), yen (if), senajan "
            "(although), nalika (when), sadurunge/sawise (before/after), "
            "supaya (so that), mula (so). The sing relative clause "
            "embeds a whole description inside a noun phrase: wong sing "
            "teka wingi. Build outward from a simple sentence: add one "
            "connector, then a second, checking that each clause still "
            "stands alone if lifted out."
        ),
        "key_points": [
            "Connectors: lan, nanging, amarga, yen, senajan, nalika, supaya, mula.",
            "sadurunge / sawise order events in time.",
            "sing embeds relative clauses in noun phrases.",
            "Each clause must stand alone if lifted out.",
            "15 complex sentences, parsed and translated.",
        ],
        "requirements": [
            "Join five sentence pairs with lan, nanging, amarga.",
            "Build three yen conditionals about tomorrow.",
            "Embed two sing relative clauses in descriptions.",
        ],
        "standards": ["Usage follows Central Javanese standard."],
        "citations": [CIT_OGLOBLIN, CIT_UHLENBECK],
        "sig_lens": (
            "The Signature read: the complex sentence is the sworn "
            "alliance - clauses bound by connector-oaths, each keeping "
            "its post: amarga gives the cause, yen the condition, sing "
            "the embedded witness. The Signature Language Method builds "
            "alliances clause by clause, testing each bond, until the "
            "sentence stands as one sworn formation."
        ),
        "drill": {"connectors": ["lan", "nanging", "amarga", "yen",
                                 "senajan", "nalika", "sadurunge",
                                 "sawise", "supaya", "mula", "banjur",
                                 "sing"]},
        "must_contain": ["amarga", "senajan", "supaya", "sing"],
    },
    {
        "key": "market",
        "name": "Javanese Conversation: At the Market",
        "group": "Conversation and Registers",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual market dialogue, annotated:\n" +
            _num_lines([
                ("[Buyer] Nuwun sewu, bakul. [opens with permission]", "Excuse me, seller."),
                ("[Seller] Monggo, badhe tumbas menapa? [polite offer]", "Please, what will you buy?"),
                ("[Buyer] Beras sekilo regane pira? [asks price]", "How much is a kilo of rice?"),
                ("[Seller] Sewelas ewu.", "Eleven thousand."),
                ("[Buyer] Larange! Oleh kurang? [bargains]", "Expensive! Can it be less?"),
                ("[Seller] Sepuluh ewu, wis murah. [counters]", "Ten thousand, already cheap."),
                ("[Buyer] Wis, dadi. [agrees]", "Deal."),
                ("[Seller] Badhe tumbas malih? [upsells politely]", "Will you buy more?"),
                ("[Buyer] Lombok seprapat. [adds item]", "A quarter (kilo) of chilies."),
                ("[Seller] Lomboke seger-seger. [praises goods]", "The chilies are fresh."),
                ("[Buyer] Ditimbang dhisik. [requests weighing]", "Weigh it first."),
                ("[Seller] Monggo, sampun. [completes]", "Here, done."),
                ("[Buyer] Dibungkus. [requests wrapping]", "Wrap it up."),
                ("[Seller] Sampun. Total rong puluh ewu. [totals]", "Done. Twenty thousand total."),
                ("[Buyer] Iki artane. [pays]", "Here is the money."),
                ("[Seller] Susuke sewu. [gives change]", "A thousand change."),
                ("[Buyer] Matur nuwun. [thanks]", "Thank you."),
                ("[Seller] Sami-sami. Mugi laris. [blesses]", "Welcome. May you prosper."),
                ("[Buyer] Sugeng tindak. [farewells]", "Safe travels."),
                ("[Seller] Sugeng tindak. [returns farewell]", "Safe travels."),
            ])
        ),
        "how_it_works": (
            "The market dialogue follows the full transaction arc: "
            "permission (nuwun sewu) -> offer (badhe tumbas menapa?) -> "
            "price (regane pira?) -> bargain (oleh kurang?) -> deal "
            "(wis, dadi) -> add-ons -> weigh/wrap -> total -> pay -> "
            "change (susuk) -> thanks -> mutual farewell. Krama verbs "
            "(tumbas for tuku, badhe for arep) keep it polite; the "
            "bargain stays in ngoko short-forms. Role-play both parts "
            "aloud, swapping roles, until the arc runs without the "
            "script."
        ),
        "key_points": [
            "Full arc: permission -> price -> bargain -> deal -> pay -> farewell.",
            "Krama tumbas/badh honor the seller; short forms bargain.",
            "susuk (change) closes the money; sami-sami closes thanks.",
            "20 annotated bilingual lines.",
        ],
        "requirements": [
            "Role-play buyer and seller, then swap.",
            "Bargain three different goods through the arc.",
            "Close with mugi laris like a real seller.",
        ],
        "standards": ["Market Javanese follows Central usage."],
        "citations": [CIT_ROBSON, CIT_ERRINGTON],
        "sig_lens": (
            "The Signature read: the market dialogue is the sworn "
            "treaty of trade - every line a clause, from nuwun sewu "
            "to sugeng tindak. The Signature Language Method signs the "
            "treaty aloud, both parties, until buyer and seller speak "
            "as one covenant of fair exchange."
        ),
        "drill": {"lines": 20, "arc": ["nuwun sewu", "regane pira?",
                                       "oleh kurang?", "wis, dadi",
                                       "susuk", "sami-sami"]},
        "must_contain": ["tumbas", "Susuk", "Wis, dadi", "Mugi laris"],
    },
    {
        "key": "friend",
        "name": "Javanese Conversation: Meeting a Friend",
        "group": "Conversation and Registers",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue of two friends meeting, "
            "annotated:\n" +
            _num_lines([
                ("[Andi] Eh, Budi! Piye kabare? [surprised greeting]", "Hey, Budi! How are you?"),
                ("[Budi] Apik-apik wae. Kowe dhewe? [returns question]", "Just fine. And you?"),
                ("[Andi] Apik. Suwene ora ketemu! [notes absence]", "Good. Long time no see!"),
                ("[Budi] Iya, wis rong taun. [agrees]", "Yes, two years already."),
                ("[Andi] Kowe saiki neng endi? [asks whereabouts]", "Where are you now?"),
                ("[Budi] Aku neng Jakarta, kerja. [answers]", "I am in Jakarta, working."),
                ("[Andi] Wah, hebat! [admires]", "Wow, great!"),
                ("[Budi] Kowe dhewe? [asks back]", "And you?"),
                ("[Andi] Aku isih neng Solo. [answers]", "I am still in Solo."),
                ("[Budi] Kapan mulih? [asks return]", "When did you return?"),
                ("[Andi] Wingi. Ayo ngopi! [invites]", "Yesterday. Let us get coffee!"),
                ("[Budi] Ayo! Neng endi? [accepts]", "Let us! Where?"),
                ("[Andi] Neng warung langganan. [suggests]", "At the usual stall."),
                ("[Budi] Wah, kangen tenan. [nostalgic]", "Wow, I really miss it."),
                ("[Andi] Ceritakna Jakarta! [requests stories]", "Tell me about Jakarta!"),
                ("[Budi] Macet, nanging rame. [describes]", "Jammed, but lively."),
                ("[Andi] Sesuk dolan menyang omahku ya. [invites home]", "Visit my house tomorrow."),
                ("[Budi] Mesthi! Aku kangen ibumu. [accepts warmly]", "Definitely! I miss your mother."),
                ("[Andi] Nganti ketemu sesuk. [farewells]", "Until tomorrow."),
                ("[Budi] Nganti ketemu! [returns]", "See you!"),
            ])
        ),
        "how_it_works": (
            "The friend dialogue runs the reunion arc: surprise (Eh!) -> "
            "greeting (piye kabare?) -> absence noted (suwene ora "
            "ketemu) -> whereabouts exchanged -> invitation (ayo ngopi) "
            "-> stories requested (ceritakna!) -> home invitation -> "
            "warm farewell. Ngoko flows throughout - bare verbs, short "
            "forms - because closeness permits it. Act it with a "
            "partner, trading Andi and Budi, and let the reunion energy "
            "carry the ngoko."
        ),
        "key_points": [
            "Reunion arc: surprise -> greeting -> absence -> news -> invite -> farewell.",
            "Ngoko throughout: closeness permits bare verbs.",
            "ayo invites; ceritakna requests stories.",
            "20 annotated bilingual lines.",
        ],
        "requirements": [
            "Act both roles, then swap with a partner.",
            "Improvise a reunion with your own news.",
            "Invite someone for coffee in Javanese today.",
        ],
        "standards": ["Dialogue Javanese follows Central usage."],
        "citations": [CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the reunion is the sworn renewal - "
            "suwene ora ketemu its opening oath, ayo ngopi its seal. "
            "The Signature Language Method renews the bond aloud: "
            "greet, marvel, invite, promise tomorrow, because friendship "
            "re-spoken is friendship re-sworn."
        ),
        "drill": {"lines": 20, "arc": ["Piye kabare?", "suwene ora ketemu",
                                       "ayo ngopi", "nganti ketemu"]},
        "must_contain": ["Piye kabare", "Suwene ora ketemu", "Ayo ngopi",
                         "Ceritakna"],
    },
    {
        "key": "problem",
        "name": "Javanese Conversation: Solving a Problem",
        "group": "Conversation and Registers",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue of neighbors solving a "
            "flooded road, annotated:\n" +
            _num_lines([
                ("[Pak RT] Nuwun sewu, ngumpul dhisik. [calls meeting]", "Excuse me, gather first."),
                ("[Warga] Ana apa, Pak? [asks issue]", "What is it, sir?"),
                ("[Pak RT] Dalan ngarep banjir. [states problem]", "The front road is flooded."),
                ("[Warga] Wah, banter tenan udane. [confirms]", "Wow, the rain is really heavy."),
                ("[Pak RT] Gotong royong sesuk esuk. [proposes]", "Mutual work tomorrow morning."),
                ("[Warga] Setuju! [agrees]", "Agreed!"),
                ("[Pak RT] Sapa nggawa cangkul? [assigns tools]", "Who brings hoes?"),
                ("[Warga] Aku nggawa cangkul. [volunteers]", "I bring a hoe."),
                ("[Warga] Aku nggawa arit. [volunteers]", "I bring a sickle."),
                ("[Pak RT] Ibu-ibu gawe teh. [assigns support]", "The mothers make tea."),
                ("[Warga] Siap! [confirms]", "Ready!"),
                ("[Pak RT] Jam pitu kumpul. [sets time]", "Gather at seven."),
                ("[Warga] Yen udan maneh piye? [raises risk]", "What if it rains again?"),
                ("[Pak RT] Tetep gotong royong. [resolves]", "We still work together."),
                ("[Warga] Gotong royong! [cheers]", "Mutual cooperation!"),
                ("[Pak RT] Matur nuwun kabeh. [thanks]", "Thank you all."),
                ("[Warga] Sami-sami, Pak. [answers]", "You are welcome, sir."),
                ("[Pak RT] Aja lali payung. [warns]", "Do not forget umbrellas."),
                ("[Warga] Siap! [confirms]", "Ready!"),
                ("[Pak RT] Bubaran, sugeng tindak. [dismisses]", "Dismissed, safe travels."),
            ])
        ),
        "how_it_works": (
            "The problem dialogue runs the gotong-royong arc: call "
            "(ngumpul) -> problem stated (banjir) -> proposal (gotong "
            "royong) -> agreement (setuju) -> roles assigned (sapa "
            "nggawa...?) -> volunteers -> time set (jam pitu) -> risk "
            "raised (yen...) -> resolved (tetep) -> thanks -> "
            "dismissal. Pak RT leads in firm krama-ngoko mix; warga "
            "answer short. Run it as a group drill, assigning Warga "
            "lines around the room, and feel how Javanese organizes "
            "collective action."
        ),
        "key_points": [
            "Gotong-royong arc: call -> problem -> proposal -> roles -> resolve.",
            "sapa nggawa...? assigns; Siap! confirms.",
            "yen raises the risk; tetep resolves it.",
            "The leader mixes firm and polite; members answer short.",
            "20 annotated bilingual lines.",
        ],
        "requirements": [
            "Run the drill with assigned roles.",
            "Propose gotong royong for a real small problem.",
            "Raise and resolve one yen risk aloud.",
        ],
        "standards": ["Dialogue Javanese follows Central usage."],
        "citations": [CIT_ERRINGTON, CIT_ROBSON],
        "sig_lens": (
            "The Signature read: the council is the sworn muster - "
            "banjir the alarm, gotong royong the battle plan, Siap! "
            "the oath of every warga. The Signature Language Method "
            "musters the tongue for collective duty: state the "
            "trouble, take a post, and hold it till bubaran."
        ),
        "drill": {"lines": 20, "arc": ["ngumpul", "banjir", "gotong royong",
                                       "setuju", "siap", "bubaran"]},
        "must_contain": ["gotong royong", "banjir", "Siap", "Bubaran"],
    },
    {
        "key": "mastery",
        "name": "Javanese Mastery Review and Full Reference",
        "group": "Mastery Reference",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "description": (
            "The whole database in one teaching summary. ALPHABET: Latin "
            "standard plus the 20 Hanacaraka aksara (ha na ca ra ka / da "
            "ta sa wa la / pa dha ja ya nya / ma ga ba tha nga), "
            "sandhangan vowel marks, pangkon, murda capitals, traditional "
            "digits 0-9.\n"
            "200 CORE WORDS (sample of the full set, grouped): people - "
            "wong, bocah, lanang, wadon, bapak, ibu, kakang, adhi, "
            "simbah, kanca; body - sirah, mripat, kuping, irung, cangkem, "
            "tangan, sikil, weteng; home - omah, lawang, jendhela, meja, "
            "kursi, pawon, kamar; nature - srengenge, rembulan, lintang, "
            "langit, lemah, banyu, geni, angin, udan, wit, kembang; food "
            "- sego, iwak, woh, sayur, teh, kopi, gudeg, soto, pecel, "
            "tempe; verbs - mangan, ngombe, turu, tangi, mlaku, mlayu, "
            "lungguh, ngadeg, omong, takon, maca, nulis, tuku, adol, "
            "gawe, teka, lunga, mulih, kerja, sinau; adjectives - apik, "
            "ala, gedhe, cilik, dawa, dhuwur, anyar, lawas, panas, adhem, "
            "legi, pedhes; numbers - siji, loro, telu, papat, lima, enem, "
            "pitu, wolu, sanga, sepuluh; time - esuk, awan, sore, bengi, "
            "dina, sasi, taun, saiki, wingi, sesuk; pronouns - aku, kowe, "
            "dheweke, kita, iki, iku, kae.\n"
            "KEY GRAMMAR: SVO order; no gender/number/case; adjectives "
            "and possessors follow; ora/mboten negate; questions rise; "
            "wis/lagi/arep/bakal/durung/tau mark time; di- passive; "
            "affixes -an/-ke/ke- -an/um-/-in- build words; sing makes "
            "relatives; levels ngoko/madya/krama/krama inggil rank every "
            "word.\n"
            "PHRASE TABLES: greetings - Sugeng enjing/siang/sonten/dalu, "
            "Matur nuwun, Nuwun sewu, Monggo, Sugeng tindak; questions - "
            "Sapa? Apa? Endi? Kapan? Kenapa? Piye? Pira?; commands - "
            "bare verb, -a, aja, monggo-softened; blessings - Mugi-mugi, "
            "Sugeng ambal warsa, Sugeng riyadi.\n"
            "THE LADDER BEHIND YOU: 34 records - 1 overview, 2 script, "
            "3 sounds, 4-6 core words, 7 pronouns, 8 numbers, 9 greetings, "
            "10 grammar, 11-20 themed sentences, 21 tenses, 22 questions, "
            "23 commands, 24 descriptions, 25-27 stories, 28 idioms, 29 "
            "registers, 30 complex sentences, 31-33 conversations, 34 "
            "this review. Example: Aku wis sinau basa Jawa, saiki aku "
            "bisa omong! (I have studied Javanese; now I can speak!)"
        ),
        "how_it_works": (
            "The review works as a self-test circuit: cover each section "
            "and reproduce it - the 20 aksara in order, the six vowels, "
            "the number pairs to twenty, the pronoun swaps, the ten "
            "grammar rules, one story retold, three idioms explained, "
            "one dialogue acted. Anything that sticks earns a check; "
            "anything that slips sends you back up the ladder to its "
            "record. Run the full circuit weekly until every section "
            "passes without the page."
        ),
        "key_points": [
            "Alphabet, 200 core words, key grammar, phrase tables in one record.",
            "Self-test circuit: cover, reproduce, check, revisit.",
            "The ladder map (1-34) shows exactly where to climb back.",
            "Weekly full-circuit review until it passes unaided.",
        ],
        "requirements": [
            "Reproduce the 20 aksara and six vowels from memory.",
            "Retell one story and act one dialogue unaided.",
            "Explain three idioms and five register swaps.",
        ],
        "standards": [
            "Reference forms follow the Central Javanese standard.",
            "Word counts: 200 core words grouped by domain.",
        ],
        "citations": [CIT_ROBSON, CIT_OGLOBLIN, CIT_ERRINGTON,
                      CIT_UHLENBECK, CIT_ISO639],
        "sig_lens": (
            "The Signature read: the review is the sworn muster of the "
            "whole campaign - every aksara present, every word "
            "accounted, every rule standing inspection. The Signature "
            "Language Method musters weekly: what stands earns its "
            "mark, what falls climbs the ladder again, until the "
            "entire language stands sworn and ready."
        ),
        "drill": {"core_words": 200, "aksara": 20, "rules": 10,
                  "records": 34, "sample_words": 60},
        "must_contain": ["200", "Hanacaraka", "SVO", "34"],
    },
]

ENTRIES = ENTRIES + ENTRIES_10_20 + ENTRIES_21_34
assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
assert [e["ladder_rank"] for e in ENTRIES] == list(range(1, 35)), "ladder ranks must be 1-34"
assert len({e["key"] for e in ENTRIES}) == 34, "entry keys must be unique"
