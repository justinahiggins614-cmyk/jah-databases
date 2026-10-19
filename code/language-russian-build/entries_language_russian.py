#!/usr/bin/env python3
"""Entries for the Russian to English databases (Manon language orders
#10-11, 2026-10-17, roster rank 8).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,410 databases)
PLUS every shard index title in jah-databases-data-1 (813 shard index
files) PLUS the main-repo data dir: zero 'language-russian*' slugs/names;
zero collisions on any of the 68 record titles (34 public + 34 Signature
Edition), checked with code/dedupe_gate.py BEFORE authoring. ID prefixes
JAH-LRUS- (public) and JAH-LRUSS- (signature) verified free: zero hits in
manifest id_prefix values and zero hits in all 813 shard index files.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-russian             - The Russian to English Database
                                 (public-harvest: real, fact-checked Russian
                                 language teaching - overview, Cyrillic
                                 writing system, phonology, core vocabulary
                                 with sentences, grammar essentials, themed
                                 sentence sets, tenses, dialogues, idioms,
                                 registers, and a mastery review; every
                                 record carries Russian content in Cyrillic
                                 + transliteration + English translation +
                                 example sentences; standard references
                                 Wade A Comprehensive Russian Grammar 3rd
                                 ed. 2011; Cubberley Russian: A Linguistic
                                 Introduction 2002; Comrie/Stone/Polinsky
                                 The Russian Language in the Twentieth
                                 Century 2nd ed. 1996; ISO 9:1995
                                 transliteration)
  language-russian-signature   - The Russian to English Signature Database
                                 (his original Signature Russian Method:
                                 every letter a sworn sign, every case a
                                 covenant of role, every verb a living
                                 action, the whole language taught as
                                 Signature science; src signature, titles
                                 suffixed " (Signature Edition)", never
                                 presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_russian.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before hand-off.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Russian Method: "
            "every letter a sworn sign, every case a covenant of role, "
            "every verb a living action, the whole language taught as "
            "Signature science. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT_WADE = ("Wade T. A Comprehensive Russian Grammar. 3rd ed. "
            "Wiley-Blackwell; 2011.")
CIT_CUBBERLEY = ("Cubberley P. Russian: A Linguistic Introduction. "
                 "Cambridge University Press; 2002.")
CIT_COMRIE = ("Comrie B, Stone G, Polinsky M. The Russian Language in the "
              "Twentieth Century. 2nd ed. Oxford: Clarendon Press; 1996.")
CIT_ISO9 = ("ISO 9:1995. Transliteration of Cyrillic characters into Latin "
            "characters - Slavic and non-Slavic languages.")
CIT_PED = ("Standard pedagogical sources for Russian vocabulary, usage, "
           "and phraseology.")
CIT_ALL = [CIT_WADE, CIT_CUBBERLEY, CIT_COMRIE, CIT_ISO9, CIT_PED]

ENTRIES = []


def _sent(items):
    """items: list of (russian, translit, english)."""
    return "\n".join(
        "%d. %s (%s - %s)" % (i + 1, ru, tr, en)
        for i, (ru, tr, en) in enumerate(items))


def _vocab(words):
    """words: list of (ru, tr, en, ex_ru, ex_tr, ex_en)."""
    return "\n".join(
        "%d. %s (%s) - %s. Example: %s (%s - %s)" % (i + 1, ru, tr, en,
                                                     ex_ru, ex_tr, ex_en)
        for i, (ru, tr, en, ex_ru, ex_tr, ex_en) in enumerate(words))


def _phrases(items):
    """items: list of (ru, tr, en, note)."""
    return "\n".join(
        "%d. %s (%s) - %s. Usage: %s" % (i + 1, ru, tr, en, note)
        for i, (ru, tr, en, note) in enumerate(items))


def _pairs(items):
    """items: list of (a_ru, a_tr, a_en, b_ru, b_tr, b_en, note)."""
    return "\n".join(
        "%d. %s (%s - %s)  |  %s (%s - %s). %s"
        % (i + 1, a_ru, a_tr, a_en, b_ru, b_tr, b_en, note)
        for i, (a_ru, a_tr, a_en, b_ru, b_tr, b_en, note) in enumerate(items))


def _dialogue(lines):
    """lines: list of (speaker, ru, tr, en)."""
    return "\n".join(
        "%d. %s: %s (%s - %s)" % (i + 1, sp, ru, tr, en)
        for i, (sp, ru, tr, en) in enumerate(lines))


# ---------------------------------------------------------------- record 1

FACTS_1 = {"letters": 33, "cases": 6, "genders": 3, "tenses": 3,
           "speakers_m": 147, "iso1": "ru", "iso3": "rus"}

ENTRIES.append({
    "key": "r01_overview",
    "name": "Russian Language Overview",
    "group": "Foundations",
    "ladder_rank": 1,
    "ladder_tier": "foundations",
    "description": (
        "Russian (русский язык, russkiy yazyk) is an East Slavic language of "
        "the Indo-European family, and the most widely spoken Slavic language "
        "in the world. It carries ISO 639-1 code ru and ISO 639-3 code rus. "
        "About 147 million people speak Russian as their native language, and "
        "about 260 million people speak it in total, making it the eighth "
        "most-spoken native language on earth. Russian is an official "
        "language in Russia, Belarus, Kazakhstan, and Kyrgyzstan, and one of "
        "the six official languages of the United Nations. It is widely "
        "spoken across Eastern Europe, the Caucasus, Central Asia, and the "
        "Baltic states. The standard language is based on the Moscow dialect "
        "of the Central dialect group; the two other traditional dialect "
        "groups are Northern and Southern. Russian is written in the Cyrillic "
        "alphabet of 33 letters, reads left to right, and is famous for its "
        "rich inflection: nouns change through six cases, verbs through "
        "person, number, tense, and aspect, and adjectives agree with nouns "
        "in gender, number, and case. Word order is flexible because the "
        "case endings, not the position, show who does what to whom.\n"
        "Key facts: native name русский (russkiy); family Indo-European, "
        "branch Balto-Slavic, group East Slavic; ISO 639-1 ru, ISO 639-3 rus; "
        "~147 million native speakers; official in Russia, Belarus, "
        "Kazakhstan, Kyrgyzstan; UN official language; script Cyrillic, 33 "
        "letters; dialects Northern, Southern, Central (Moscow standard)."
    ),
    "how_it_works": (
        "Russian works as a highly inflected language: the job of each word "
        "in a sentence is marked by its ending. A noun takes one of six case "
        "endings that say whether it is the subject, the owner, the receiver, "
        "the object, the instrument, or the place. Because the endings carry "
        "this information, word order is free and is used for emphasis rather "
        "than grammar: Мама любит папу and Папу любит мама both mean mother "
        "loves father, with different emphasis. Verbs come in aspect pairs - "
        "an imperfective form for ongoing or repeated action and a perfective "
        "form for completed action - which is how Russian expresses ideas "
        "that English handles with many tenses. Adjectives agree with their "
        "nouns in gender (masculine, feminine, neuter), number, and case, so "
        "an adjective and its noun always wear matching endings. There is no "
        "verb 'to be' in the present tense: Я студент (Ya student - I am a "
        "student) needs no word for 'am'; a dash often stands in its place in "
        "writing. Stress is free and mobile, and it can change meaning, so "
        "learners mark the stressed vowel in every new word."
    ),
    "key_points": [
        "Russian is East Slavic, Indo-European: ISO 639-1 ru, ISO 639-3 rus, native name русский (russkiy).",
        "About 147 million native speakers and about 260 million total speakers; official in Russia, Belarus, Kazakhstan, Kyrgyzstan, and at the United Nations.",
        "The standard language rests on the Moscow dialect of the Central group; Northern and Southern are the other traditional dialect groups.",
        "Cyrillic script, 33 letters, written left to right; the alphabet is taught letter by letter in record 2.",
        "Six noun cases mark each word's role, so word order is flexible and carries emphasis, not grammar.",
        "Verbs pair into imperfective (ongoing) and perfective (completed) aspects - the heart of the Russian verb system.",
        "Adjectives agree with nouns in gender, number, and case; there are three genders: masculine, feminine, neuter.",
        "No present-tense 'to be': Я студент (Ya student) means 'I am a student' with no verb at all.",
    ],
    "requirements": [
        "Learn the 33 Cyrillic letters before anything else - every later record assumes you can read them.",
        "Mark the stressed vowel in every new word; stress is free and can change meaning.",
        "Learn nouns together with their gender; gender controls every adjective and past-tense ending.",
        "Learn verbs as aspect pairs (imperfective/perfective), not as single words.",
    ],
    "standards": [
        "Language codes follow ISO 639-1 (ru) and ISO 639-3 (rus).",
        "Transliteration in this database follows the pedagogical Latin rendering aligned with ISO 9:1995 conventions.",
        "Grammatical description follows the standard reference grammars cited below.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method begins here: the language is a sworn "
        "system of signs, and this overview is its charter. Every letter "
        "will be a sworn sign, every case a covenant of role, every verb a "
        "living action. Learn the charter first - family, codes, speakers, "
        "script, cases, aspect - and every later lesson is simply the "
        "charter unfolding, sign by sign."
    ),
    "demo_key": "overview",
    "demo_data": FACTS_1,
})

# ---------------------------------------------------------------- record 2

LETTERS_2 = [
    ("А", "а", "a", "арбуз", "arbuz", "watermelon"),
    ("Б", "б", "b", "банан", "banan", "banana"),
    ("В", "в", "v", "вода", "voda", "water"),
    ("Г", "г", "g", "город", "gorod", "city"),
    ("Д", "д", "d", "дом", "dom", "house"),
    ("Е", "е", "ye/e", "еда", "yeda", "food"),
    ("Ё", "ё", "yo", "ёлка", "yolka", "fir tree"),
    ("Ж", "ж", "zh", "журнал", "zhurnal", "magazine"),
    ("З", "з", "z", "завод", "zavod", "factory"),
    ("И", "и", "i", "игра", "igra", "game"),
    ("Й", "й", "y", "йогурт", "yogurt", "yogurt"),
    ("К", "к", "k", "книга", "kniga", "book"),
    ("Л", "л", "l", "лампа", "lampa", "lamp"),
    ("М", "м", "m", "мама", "mama", "mama"),
    ("Н", "н", "n", "ночь", "noch", "night"),
    ("О", "о", "o", "окно", "okno", "window"),
    ("П", "п", "p", "папа", "papa", "papa"),
    ("Р", "р", "r", "рука", "ruka", "hand"),
    ("С", "с", "s", "стол", "stol", "table"),
    ("Т", "т", "t", "телефон", "telefon", "telephone"),
    ("У", "у", "u", "улица", "ulitsa", "street"),
    ("Ф", "ф", "f", "флаг", "flag", "flag"),
    ("Х", "х", "kh", "хлеб", "khleb", "bread"),
    ("Ц", "ц", "ts", "цветок", "tsvetok", "flower"),
    ("Ч", "ч", "ch", "часы", "chasy", "clock"),
    ("Ш", "ш", "sh", "школа", "shkola", "school"),
    ("Щ", "щ", "shch", "щука", "shchuka", "pike"),
    ("Ъ", "ъ", "hard sign", "объект", "obyekt", "object"),
    ("Ы", "ы", "y", "мы", "my", "we"),
    ("Ь", "ь", "soft sign", "день", "den", "day"),
    ("Э", "э", "e", "экран", "ekran", "screen"),
    ("Ю", "ю", "yu", "юг", "yug", "south"),
    ("Я", "я", "ya", "яблоко", "yabloko", "apple"),
]

ENTRIES.append({
    "key": "r02_alphabet",
    "name": "Russian Writing System - Cyrillic",
    "group": "Foundations",
    "ladder_rank": 1,
    "ladder_tier": "foundations",
    "description": (
        "Russian is written in the Cyrillic alphabet: 33 letters, read left "
        "to right, with upper and lower case like English. Ten letters are "
        "vowels (а, е, ё, и, о, у, ы, э, ю, я); twenty-one are consonants; "
        "two are signs - the hard sign ъ, which separates a prefix from a "
        "following iotated vowel, and the soft sign ь, which softens "
        "(palatalizes) the consonant before it. The letter ё is often "
        "printed as е, so learners read е as ё when the word demands it "
        "(e.g. ещё). Punctuation matches English in most uses, with « » "
        "guillemets for quotation marks and a dash where English would use "
        "the verb 'is'. Russian numerals use the same Arabic digits as "
        "English: 0 ноль (nol), 1 один (odin), 2 два (dva), 3 три (tri), "
        "4 четыре (chetyre), 5 пять (pyat), 6 шесть (shest), 7 семь (sem), "
        "8 восемь (vosem), 9 девять (devyat), 10 десять (desyat). "
        "The full alphabet with transliteration and an example word:\n" +
        "\n".join(
            "%d. %s %s (%s) - as in %s (%s - %s)" % (i + 1, U, L, tr, w, wtr, wen)
            for i, (U, L, tr, w, wtr, wen) in enumerate(LETTERS_2))
    ),
    "how_it_works": (
        "Cyrillic is a phonetic alphabet: each letter stands for a sound, "
        "and words are read as they are spelled far more reliably than in "
        "English. The five vowel letters а, о, у, э, ы mark hard consonants "
        "before them, while я, ё, ю, е, и mark soft ones - so the vowel "
        "letter tells you two things at once: the vowel sound and whether "
        "the preceding consonant is hard or soft. Й never starts a word and "
        "forms diphthongs (ай, ей, ой). The hard sign ъ appears only between "
        "a prefix and a root (объект, подъезд) and the soft sign ь softens "
        "the consonant it follows (день, любовь). Because spelling is "
        "regular, the fastest path to reading Russian is to learn the 33 "
        "letter-sound pairs cold, then read aloud slowly, sounding every "
        "letter until the pairs become automatic."
    ),
    "key_points": [
        "33 letters: 10 vowels, 21 consonants, hard sign ъ and soft sign ь; read left to right.",
        "Vowel letters do double duty: they name the vowel and mark the preceding consonant hard (а о у э ы) or soft (я ё ю е и).",
        "Ё is usually printed as е - read е as ё wherever the word requires it.",
        "The soft sign ь palatalizes the consonant before it; the hard sign ъ separates prefix from root.",
        "Spelling is highly phonetic: learn the 33 sound pairs and you can read any word aloud.",
        "Quotation marks are « »; a dash often replaces the verb 'is'; digits are the same Arabic numerals as English.",
    ],
    "requirements": [
        "Memorize all 33 letters with their transliterations before moving on.",
        "Practice the pairs that English lacks: ж (zh), ц (ts), ч (ch), ш (sh), щ (shch), х (kh), ы (y), р (rolled r).",
        "Read the example word for each letter aloud to anchor the sound.",
    ],
    "standards": [
        "Letter names and order follow the standard Russian alphabet sequence.",
        "Transliteration follows the pedagogical Latin rendering aligned with ISO 9:1995.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "In the Signature Russian Method each of the 33 letters is a sworn "
        "sign with a fixed sound-oath: learn the oath of each sign and no "
        "word can hide from you. The hard and soft signs are the two "
        "keepers of the gate - one divides, one softens - and the vowel "
        "letters are double-sworn, naming both the vowel and the hardness "
        "of the consonant before them."
    ),
    "demo_key": "alphabet",
    "demo_data": {"letters": [[U, L, tr] for U, L, tr, w, wtr, wen in LETTERS_2]},
})

# ---------------------------------------------------------------- record 3

PHON_3 = [
    ("вода", "vada", "water", "unstressed о sounds like а"),
    ("молоко", "malako", "milk", "unstressed о sounds like а"),
    ("хорошо", "kharasho", "well", "unstressed о sounds like а"),
    ("привет", "privet", "hello", "е after a consonant, like 'e' in met"),
    ("спасибо", "spasiba", "thank you", "unstressed о sounds like а"),
    ("тетрадь", "tetrad", "notebook", "soft дь at the end"),
    ("день", "den", "day", "soft нь at the end"),
    ("любовь", "lyubov", "love", "soft вь at the end"),
    ("город", "gorat", "city", "final д devoices to т; unstressed о sounds like а"),
    ("хлеб", "khlep", "bread", "final б devoices to п"),
    ("снег", "snek", "snow", "final г devoices to к"),
    ("нож", "nosh", "knife", "final ж devoices to ш"),
]

ENTRIES.append({
    "key": "r03_phonology",
    "name": "Russian Pronunciation and Phonology",
    "group": "Foundations",
    "ladder_rank": 2,
    "ladder_tier": "foundations",
    "description": (
        "Russian has 5 vowel sounds (а, о, у, э, ы, with и as the soft "
        "partner of ы) and a large consonant inventory in which almost "
        "every consonant comes in a hard and a soft (palatalized) pair: "
        "б/бь, в/вь, д/дь, з/зь, л/ль, м/мь, н/нь, п/пь, р/рь, с/сь, т/ть, "
        "ф/фь, plus the always-hard ж, ш, ц and the always-soft ч, щ, й. "
        "Stress is free - it can fall on any syllable - and mobile, so it "
        "must be learned with each word; misplaced stress is the fastest "
        "way to sound foreign. Unstressed vowels reduce: о sounds like а "
        "(аканье) and е sounds like и (иканье) before the stress, which is "
        "why молоко is pronounced 'malako'. Voiced consonants devoice at "
        "the end of a word: город sounds like 'gorat', хлеб like 'khlep'. "
        "Russian intonation uses melodic patterns (IK-1 through IK-7): "
        "IK-1 falls on the stressed word of a plain statement, IK-3 rises "
        "on the question word of a question without an interrogative word. "
        "Spoken examples with English approximations:\n" +
        "\n".join(
            "%d. %s (%s) - %s. Note: %s." % (i + 1, w, tr, en, note)
            for i, (w, tr, en, note) in enumerate(PHON_3))
    ),
    "how_it_works": (
        "Pronunciation works through three interacting systems. First, "
        "hardness: the vowel letter after a consonant tells you whether "
        "the consonant is hard or soft, and soft consonants are made with "
        "the middle of the tongue raised toward the palate. Second, stress "
        "and reduction: only the stressed vowel keeps its full sound; "
        "unstressed о weakens toward а and unstressed е toward и, so the "
        "spelling stays fixed while the pronunciation shifts with the "
        "stress. Third, voicing assimilation: consonant clusters agree in "
        "voicing, and word-final voiced consonants go voiceless. Together "
        "these rules mean you read the spelling, apply stress, reduce the "
        "unstressed vowels, devoice the endings, and you sound Russian."
    ),
    "key_points": [
        "Almost every consonant has a hard and a soft pair; ж, ш, ц are always hard, ч, щ, й always soft.",
        "Stress is free and mobile - learn it with every word; it drives vowel reduction.",
        "Unstressed о reduces toward а (аканье); unstressed е reduces toward и (иканье).",
        "Word-final voiced consonants devoice: д→т, б→п, г→к, ж→ш, з→с, в→ф.",
        "Intonation patterns IK-1 (statement fall) and IK-3 (question rise) carry sentence meaning.",
        "The rolled р is made with a tongue trill; ы is a hard 'i' with the tongue pulled back.",
    ],
    "requirements": [
        "Mark stress on every new word and practice the reduced pronunciations aloud.",
        "Drill the hard/soft consonant pairs until the tongue position is automatic.",
        "Practice final devoicing: read город, хлеб, снег, нож with voiceless endings.",
    ],
    "standards": [
        "Sound descriptions follow the standard phonological analysis in the cited grammars.",
        "Intonation constructions IK-1 through IK-7 follow the standard Russian intonology.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method treats every sound as a sworn tone: "
        "hard and soft are two oaths of the same consonant, stress is the "
        "crown placed on one vowel, and reduction is the court's bow to "
        "the crown - unstressed vowels soften their voice before it. "
        "Devoicing at the word's end is the final guard's salute."
    ),
    "demo_key": "phonology",
    "demo_data": {
        "reductions": [["moloko", 5, "malako"], ["khorosho", 7, "kharasho"],
                        ["voda", 3, "vada"], ["spasibo", 5, "spasiba"]],
        "devoicing": [["gorod", 1, "gorat"], ["khleb", 3, "khlep"],
                      ["sneg", 2, "snek"], ["nozh", 1, "nosh"]],
    },
})

# ---------------------------------------------------------------- record 4

NOUNS_4 = [
    ("человек", "chelovek", "person", "Этот человек - мой друг.", "Etot chelovek - moy drug.", "This person is my friend."),
    ("мужчина", "muzhchina", "man", "Мужчина стоит у окна.", "Muzhchina stoit u okna.", "The man is standing by the window."),
    ("женщина", "zhenshchina", "woman", "Женщина читает книгу.", "Zhenshchina chitayet knigu.", "The woman is reading a book."),
    ("ребёнок", "rebyonok", "child", "Ребёнок играет во дворе.", "Rebyonok igrayet vo dvore.", "The child is playing in the yard."),
    ("дом", "dom", "house", "Наш дом большой.", "Nash dom bolshoy.", "Our house is big."),
    ("город", "gorod", "city", "Это красивый город.", "Eto krasivyy gorod.", "This is a beautiful city."),
    ("улица", "ulitsa", "street", "Улица широкая и чистая.", "Ulitsa shirokaya i chistaya.", "The street is wide and clean."),
    ("школа", "shkola", "school", "Дети идут в школу.", "Deti idut v shkolu.", "The children are going to school."),
    ("книга", "kniga", "book", "Я читаю интересную книгу.", "Ya chitayu interesnuyu knigu.", "I am reading an interesting book."),
    ("стол", "stol", "table", "Книга лежит на столе.", "Kniga lezhit na stole.", "The book is lying on the table."),
    ("стул", "stul", "chair", "Стул стоит у стола.", "Stul stoit u stola.", "The chair is by the table."),
    ("окно", "akno", "window", "Открой окно, пожалуйста.", "Otkroy okno, pozhaluysta.", "Open the window, please."),
    ("дверь", "dver", "door", "Дверь закрыта.", "Dver zakryta.", "The door is closed."),
    ("хлеб", "khleb", "bread", "Купи свежий хлеб.", "Kupi svezhiy khleb.", "Buy fresh bread."),
    ("вода", "vada", "water", "Вода холодная.", "Voda kholodnaya.", "The water is cold."),
    ("молоко", "malako", "milk", "Ребёнок пьёт молоко.", "Rebyonok pyot malako.", "The child is drinking milk."),
    ("еда", "yeda", "food", "Еда вкусная.", "Yeda vkusnaya.", "The food is tasty."),
    ("машина", "mashina", "car", "Машина стоит у дома.", "Mashina stoit u doma.", "The car is by the house."),
    ("поезд", "poyezd", "train", "Поезд идёт быстро.", "Poyezd idyot bystro.", "The train goes fast."),
    ("самолёт", "samolyot", "airplane", "Самолёт летит высоко.", "Samolyot letit vysoko.", "The airplane flies high."),
    ("друг", "drug", "friend", "Мой друг живёт в Москве.", "Moy drug zhivyot v Moskve.", "My friend lives in Moscow."),
    ("семья", "semya", "family", "У меня большая семья.", "U menya bolshaya semya.", "I have a big family."),
    ("работа", "rabota", "work", "Работа начинается в девять.", "Rabota nachinayetsya v devyat.", "Work starts at nine."),
    ("время", "vremya", "time", "У меня нет времени.", "U menya net vremeni.", "I have no time."),
    ("деньги", "dengi", "money", "Деньги лежат на столе.", "Dengi lezhat na stole.", "The money is on the table."),
]

ENTRIES.append({
    "key": "r04_nouns",
    "name": "Russian Core Nouns I",
    "group": "Foundations",
    "ladder_rank": 2,
    "ladder_tier": "foundations",
    "description": (
        "Twenty-five essential Russian nouns - people, places, and things - "
        "each with its transliteration, English meaning, and one example "
        "sentence translated into English. Learn each noun with its gender: "
        "masculine nouns usually end in a consonant (дом, стол), feminine "
        "nouns usually end in -а or -я (книга, улица), neuter nouns usually "
        "end in -о or -е (окно). Gender controls every adjective and "
        "past-tense verb that goes with the noun, so never learn a noun "
        "without it.\n" + _vocab(NOUNS_4)
    ),
    "how_it_works": (
        "A Russian noun carries three permanent features: gender "
        "(masculine, feminine, neuter), number (singular, plural), and a "
        "declension pattern that generates its six case forms. The gender "
        "is usually readable from the ending: consonant means masculine, "
        "-а/-я means feminine, -о/-е means neuter, with a small set of "
        "exceptions to memorize (e.g. папа is masculine despite ending in "
        "-а). The noun's case ending then changes with its role in the "
        "sentence, while the gender stays fixed and dictates agreement. "
        "That is why the example sentences matter: each one shows the noun "
        "in a real case form, not just the dictionary nominative."
    ),
    "key_points": [
        "25 essential nouns: people (человек, мужчина, женщина, ребёнок, друг, семья), places (дом, город, улица, школа), things (книга, стол, стул, окно, дверь), food and drink (хлеб, вода, молоко, еда), transport (машина, поезд, самолёт), and abstracts (работа, время, деньги).",
        "Gender is usually visible in the ending: consonant = masculine, -а/-я = feminine, -о/-е = neuter.",
        "Always learn a noun with its gender - it controls adjective and verb agreement everywhere.",
        "Each example sentence shows the noun in a real case form, building case intuition from day one.",
    ],
    "requirements": [
        "Memorize all 25 nouns with gender and meaning.",
        "Read each example sentence aloud and identify the noun's case form.",
        "Practice plural forms: дом - дома, книга - книги, окно - окна.",
    ],
    "standards": [
        "Vocabulary selection follows frequency in standard pedagogical word lists.",
        "Gender and declension follow the standard reference grammars.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method swears each noun as a named thing "
        "with a fixed gender-oath: masculine things stand hard, feminine "
        "things end in open song, neuter things rest in balance. Learn the "
        "name and its oath together, and the noun will never betray you in "
        "a sentence."
    ),
    "demo_key": "vocab_quiz",
    "demo_data": {"words": [[ru, en] for ru, tr, en, eru, etr, een in NOUNS_4],
                  "quiz_kind": "nouns"},
})

# ---------------------------------------------------------------- record 5

VERBS_5 = [
    ("быть", "byt", "to be", "Я буду дома вечером.", "Ya budu doma vecherom.", "I will be home in the evening."),
    ("делать", "delat", "to do, to make", "Я делаю уроки.", "Ya delayu uroki.", "I am doing homework."),
    ("идти", "idti", "to go (on foot)", "Мы идём в школу.", "My idyom v shkolu.", "We are going to school."),
    ("ехать", "yekhat", "to go (by vehicle)", "Они едут в город.", "Oni yedut v gorod.", "They are going to the city."),
    ("говорить", "govorit", "to speak", "Я говорю по-русски.", "Ya govoryu po-russki.", "I speak Russian."),
    ("сказать", "skazat", "to say, to tell (perfective)", "Он скажет правду.", "On skazhet pravdu.", "He will tell the truth."),
    ("знать", "znat", "to know", "Я знаю ответ.", "Ya znayu otvet.", "I know the answer."),
    ("хотеть", "khotet", "to want", "Я хочу спать.", "Ya khochu spat.", "I want to sleep."),
    ("мочь", "moch", "to be able, can", "Я могу помочь.", "Ya mogu pomoch.", "I can help."),
    ("есть", "yest", "to eat", "Мы едим суп.", "My yedim sup.", "We are eating soup."),
    ("пить", "pit", "to drink", "Они пьют чай.", "Oni pyut chay.", "They are drinking tea."),
    ("спать", "spat", "to sleep", "Ребёнок спит.", "Rebyonok spit.", "The child is sleeping."),
    ("работать", "rabotat", "to work", "Отец работает в банке.", "Otets rabotayet v banke.", "Father works in a bank."),
    ("учиться", "uchitsya", "to study", "Я учусь в школе.", "Ya uchus v shkole.", "I study at school."),
    ("читать", "chitat", "to read", "Мама читает газету.", "Mama chitayet gazetu.", "Mother is reading a newspaper."),
    ("писать", "pisat", "to write", "Ученик пишет письмо.", "Uchenik pishet pismo.", "The pupil is writing a letter."),
    ("смотреть", "smotret", "to watch", "Мы смотрим фильм.", "My smotrim film.", "We are watching a movie."),
    ("слушать", "slushat", "to listen", "Я слушаю музыку.", "Ya slushayu muzyku.", "I am listening to music."),
    ("ждать", "zhdat", "to wait", "Я жду друга.", "Ya zhdu druga.", "I am waiting for a friend."),
    ("любить", "lyubit", "to love", "Я люблю свою семью.", "Ya lyublyu svoyu semyu.", "I love my family."),
    ("думать", "dumat", "to think", "Я думаю о тебе.", "Ya dumayu o tebe.", "I am thinking about you."),
    ("жить", "zhit", "to live", "Мы живём в деревне.", "My zhivyom v derevne.", "We live in a village."),
    ("покупать", "pokupat", "to buy", "Она покупает хлеб.", "Ona pokupayet khleb.", "She is buying bread."),
    ("давать", "davat", "to give", "Учитель даёт задание.", "Uchitel dayot zadaniye.", "The teacher is giving an assignment."),
    ("брать", "brat", "to take", "Я беру книгу.", "Ya beru knigu.", "I am taking a book."),
]

ENTRIES.append({
    "key": "r05_verbs",
    "name": "Russian Core Verbs I",
    "group": "Foundations",
    "ladder_rank": 2,
    "ladder_tier": "foundations",
    "description": (
        "Twenty-five essential Russian verbs, each with its transliteration, "
        "English meaning, and one example sentence translated into English. "
        "Russian verbs come in two conjugations: first-conjugation verbs "
        "(like делать, читать) take the endings -ю/-ешь/-ет/-ем/-ете/-ют, and "
        "second-conjugation verbs (like говорить, смотреть) take "
        "-ю/-ишь/-ит/-им/-ите/-ят. Motion verbs split into going on foot "
        "(идти) and going by vehicle (ехать). Aspect pairs - imperfective "
        "for ongoing action, perfective for completed action - are marked "
        "where they matter most (сказать is the perfective partner of "
        "говорить for single acts of telling).\n" + _vocab(VERBS_5)
    ),
    "how_it_works": (
        "A Russian verb is built from a stem plus endings. Drop the -ть "
        "from the infinitive to find the stem for most verbs: дела- gives "
        "я делаю, ты делаешь, он делает, мы делаем, вы делаете, они "
        "делают. Second-conjugation stems take -ишь/-ит: говор- gives я "
        "говорю, ты говоришь, он говорит, мы говорим, вы говорите, они "
        "говорят. The present tense covers both 'I do' and 'I am doing' - "
        "Russian has no separate continuous form. Reflexive verbs add -ся "
        "after consonants and -сь after vowels (учиться: я учусь, ты "
        "учишься). The example sentences show each verb in a real "
        "conjugated form, so the endings are learned in context, not as "
        "abstract tables."
    ),
    "key_points": [
        "25 essential verbs covering being, doing, motion, speech, knowledge, desire, senses, work, and daily life.",
        "Two conjugations: first (-ешь/-ет) and second (-ишь/-ит); the example sentences model both.",
        "Motion splits by means: идти on foot, ехать by vehicle - a core Russian distinction.",
        "The present tense covers both simple and continuous English meanings.",
        "Reflexive -ся/-сь marks actions turned back on the subject (учиться - to study).",
        "Verbs of saying, giving, and taking anchor everyday conversation.",
    ],
    "requirements": [
        "Memorize all 25 infinitives with meanings.",
        "Conjugate делать and говорить fully aloud until the endings are automatic.",
        "Learn идти vs ехать as a pair - never confuse foot and vehicle motion.",
    ],
    "standards": [
        "Conjugation classes follow the standard two-conjugation analysis in the cited grammars.",
        "Aspect pairing follows standard pedagogical presentation.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "In the Signature Russian Method every verb is a living action "
        "sworn to its conjugation: first-conjugation verbs march with "
        "open endings, second-conjugation verbs stand with closed ranks. "
        "Motion verbs swear a double oath - by foot and by wheel - and "
        "aspect is the verb's two faces, the ongoing and the completed."
    ),
    "demo_key": "conjugation",
    "demo_data": {
        "first": {"infinitive": "делать", "stem": "дела",
                  "endings": ["ю", "ешь", "ет", "ем", "ете", "ют"],
                  "forms": ["делаю", "делаешь", "делает", "делаем", "делаете", "делают"]},
        "second": {"infinitive": "говорить", "stem": "говор",
                   "endings": ["ю", "ишь", "ит", "им", "ите", "ят"],
                   "forms": ["говорю", "говоришь", "говорит", "говорим", "говорите", "говорят"]},
        "pronouns": ["я", "ты", "он", "мы", "вы", "они"],
    },
})

# ---------------------------------------------------------------- record 6

ADJ_6 = [
    ("большой", "bolshoy", "big", "Это большой дом.", "Eto bolshoy dom.", "This is a big house."),
    ("маленький", "malenkiy", "small", "У меня маленькая собака.", "U menya malenkaya sobaka.", "I have a small dog."),
    ("новый", "novyy", "new", "Я купил новый телефон.", "Ya kupil novyy telefon.", "I bought a new phone."),
    ("старый", "staryy", "old", "Это старый друг.", "Eto staryy drug.", "This is an old friend."),
    ("хороший", "khoroshiy", "good", "Хороший день!", "Khoroshiy den!", "A good day!"),
    ("плохой", "plokhoy", "bad", "Плохая погода.", "Plokhaya pogoda.", "Bad weather."),
    ("красивый", "krasivyy", "beautiful", "Какая красивая девушка!", "Kakaya krasivaya devushka!", "What a beautiful girl!"),
    ("быстрый", "bystryy", "fast", "Быстрый поезд.", "Bystryy poyezd.", "A fast train."),
    ("медленный", "medlennyy", "slow", "Медленный интернет.", "Medlennyy internet.", "Slow internet."),
    ("тёплый", "tyoplyy", "warm", "Тёплое молоко.", "Tyoploye moloko.", "Warm milk."),
    ("холодный", "kholodnyy", "cold", "Холодная зима.", "Kholodnaya zima.", "A cold winter."),
    ("высокий", "vysokiy", "tall, high", "Высокий мужчина.", "Vysokiy muzhchina.", "A tall man."),
    ("низкий", "nizkiy", "low, short", "Низкий стол.", "Nizkiy stol.", "A low table."),
    ("длинный", "dlinnyy", "long", "Длинная улица.", "Dlinnaya ulitsa.", "A long street."),
    ("короткий", "korotkiy", "short", "Короткий рассказ.", "Korotkiy rasskaz.", "A short story."),
    ("широкий", "shirokiy", "wide", "Широкая река.", "Shirokaya reka.", "A wide river."),
    ("узкий", "uzkiy", "narrow", "Узкий коридор.", "Uzkiy koridor.", "A narrow corridor."),
    ("светлый", "svetlyy", "light, bright", "Светлая комната.", "Svetlaya komnata.", "A bright room."),
    ("тёмный", "tyomnyy", "dark", "Тёмная ночь.", "Tyomnaya noch.", "A dark night."),
    ("сильный", "silnyy", "strong", "Сильный ветер.", "Silnyy veter.", "A strong wind."),
    ("слабый", "slabyy", "weak", "Слабый чай.", "Slabyy chay.", "Weak tea."),
    ("богатый", "bogatyy", "rich", "Богатый человек.", "Bogatyy chelovek.", "A rich person."),
    ("бедный", "bednyy", "poor", "Бедная семья.", "Bednaya semya.", "A poor family."),
    ("умный", "umnyy", "smart", "Умный ученик.", "Umnyy uchenik.", "A smart pupil."),
    ("глупый", "glupyy", "stupid", "Глупый вопрос.", "Glupyy vopros.", "A stupid question."),
]

ADV_6 = [
    ("быстро", "bystro", "quickly", "Он бегает быстро.", "On begayet bystro.", "He runs fast."),
    ("медленно", "medlenno", "slowly", "Говорите медленно, пожалуйста.", "Govorite medlenno, pozhaluysta.", "Speak slowly, please."),
    ("хорошо", "khorosho", "well", "Он хорошо говорит по-русски.", "On khorosho govorit po-russki.", "He speaks Russian well."),
    ("плохо", "plokho", "badly", "Я плохо сплю.", "Ya plokho splyu.", "I sleep badly."),
    ("очень", "ochen", "very", "Очень интересно!", "Ochen interesno!", "Very interesting!"),
    ("слишком", "slishkom", "too", "Слишком дорого.", "Slishkom dorogo.", "Too expensive."),
    ("всегда", "vsegda", "always", "Я всегда завтракаю дома.", "Ya vsegda zavtrakayu doma.", "I always have breakfast at home."),
    ("никогда", "nikogda", "never", "Я никогда не опаздываю.", "Ya nikogda ne opazdyvayu.", "I am never late."),
    ("часто", "chasto", "often", "Мы часто гуляем в парке.", "My chasto gulyayem v parke.", "We often walk in the park."),
    ("редко", "redko", "rarely", "Он редко звонит.", "On redko zvonit.", "He rarely calls."),
    ("сейчас", "seychas", "now", "Я сейчас занят.", "Ya seychas zanyat.", "I am busy now."),
    ("потом", "potom", "later", "Поговорим потом.", "Pogovorim potom.", "We will talk later."),
    ("здесь", "zdes", "here", "Здесь красиво.", "Zdes krasivo.", "It is beautiful here."),
    ("там", "tam", "there", "Там мой дом.", "Tam moy dom.", "My house is there."),
    ("дома", "doma", "at home", "Я буду дома вечером.", "Ya budu doma vecherom.", "I will be home in the evening."),
]

ENTRIES.append({
    "key": "r06_adjectives",
    "name": "Russian Adjectives and Adverbs",
    "group": "Foundations",
    "ladder_rank": 3,
    "ladder_tier": "foundations",
    "description": (
        "Twenty-five essential adjectives and fifteen essential adverbs, "
        "each with transliteration, meaning, and a translated example "
        "sentence. Russian adjectives agree with their noun in gender, "
        "number, and case: новый дом (masculine), новая книга (feminine), "
        "новое окно (neuter), новые дома (plural). Adverbs do not change: "
        "быстро stays быстро no matter what it describes. Many adverbs "
        "are built from adjectives (быстрый - быстро), and the neuter "
        "short form of an adjective often serves as an adverb of manner.\n"
        "Adjectives:\n" + _vocab(ADJ_6) +
        "\nAdverbs:\n" + _vocab(ADV_6)
    ),
    "how_it_works": (
        "An adjective takes the gender, number, and case of its noun by "
        "swapping its ending: hard-stem adjectives use -ый/-ой (masc), "
        "-ая (fem), -ое (neut), -ые (plural), so новый becomes новая, "
        "новое, новые. Soft-stem adjectives use -ий/-яя/-ее/-ие (синий, "
        "синяя, синее, синие). Adjectives also have short forms used as "
        "predicates - он счастлив (he is happy) - which agree only in "
        "gender and number. Adverbs are indeclinable: they never change "
        "form, they just sit before or after the verb they modify. The "
        "agreement system means that in the sentence Хорошая книга лежит "
        "на столе, the -ая on хорошая redundantly but reliably signals "
        "that книга is feminine nominative singular."
    ),
    "key_points": [
        "25 adjectives and 15 adverbs, each with a translated example sentence.",
        "Adjectives agree with nouns in gender, number, and case: новый/новая/новое/новые.",
        "Hard stems take -ый/-ая/-ое/-ые; soft stems take -ий/-яя/-ее/-ие.",
        "Adverbs never change form; many derive from adjectives (быстрый - быстро).",
        "Short-form adjectives serve as predicates: он счастлив, она счастлива.",
        "Agreement is redundant on purpose - it lets listeners catch the noun's features twice.",
    ],
    "requirements": [
        "Memorize all 40 words with meanings.",
        "Practice the four-form agreement drill: новый дом, новая книга, новое окно, новые книги.",
        "Learn which adverbs pair with which adjectives.",
    ],
    "standards": [
        "Adjective declension follows the standard hard/soft stem analysis in the cited grammars.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method dresses every adjective in the "
        "uniform of its noun: the noun's gender-oath dictates the "
        "adjective's ending, and the adjective marches in matching step. "
        "Adverbs are the free scouts - unchanging, unsworn to any noun, "
        "reporting only how the action was done."
    ),
    "demo_key": "agreement",
    "demo_data": {"hard": {"stem": "нов", "forms": ["новый", "новая", "новое", "новые"]},
                  "soft": {"stem": "син", "forms": ["синий", "синяя", "синее", "синие"]},
                  "genders": ["masculine", "feminine", "neuter", "plural"]},
})

# ---------------------------------------------------------------- record 7

PRON_7 = {
    "personal": [
        ("я", "ya", "I", "Я студент.", "Ya student.", "I am a student."),
        ("ты", "ty", "you (informal)", "Ты мой друг.", "Ty moy drug.", "You are my friend."),
        ("он", "on", "he", "Он врач.", "On vrach.", "He is a doctor."),
        ("она", "ona", "she", "Она учительница.", "Ona uchitelnitsa.", "She is a teacher."),
        ("оно", "ono", "it", "Оно большое.", "Ono bolshoye.", "It is big."),
        ("мы", "my", "we", "Мы дома.", "My doma.", "We are at home."),
        ("вы", "vy", "you (formal/plural)", "Вы правы.", "Vy pravy.", "You are right."),
        ("они", "oni", "they", "Они студенты.", "Oni studenty.", "They are students."),
    ],
    "possessive": [
        ("мой", "moy", "my (masc.)", "Мой брат.", "Moy brat.", "My brother."),
        ("моя", "moya", "my (fem.)", "Моя сестра.", "Moya sestra.", "My sister."),
        ("твой", "tvoy", "your (informal)", "Твой дом.", "Tvoy dom.", "Your house."),
        ("его", "yevo", "his", "Его книга.", "Yevo kniga.", "His book."),
        ("её", "yeyo", "her", "Её сумка.", "Yeyo sumka.", "Her bag."),
        ("наш", "nash", "our", "Наш город.", "Nash gorod.", "Our city."),
        ("ваш", "vash", "your (formal)", "Ваш паспорт.", "Vash pasport.", "Your passport."),
        ("их", "ikh", "their", "Их дети.", "Ikh deti.", "Their children."),
    ],
    "demonstrative": [
        ("этот", "etot", "this (masc.)", "Этот дом.", "Etot dom.", "This house."),
        ("эта", "eta", "this (fem.)", "Эта книга.", "Eta kniga.", "This book."),
        ("тот", "tot", "that (masc.)", "Тот человек.", "Tot chelovek.", "That person."),
        ("та", "ta", "that (fem.)", "Та улица.", "Ta ulitsa.", "That street."),
    ],
    "interrogative": [
        ("кто", "kto", "who", "Кто это?", "Kto eto?", "Who is this?"),
        ("что", "chto", "what", "Что это?", "Chto eto?", "What is this?"),
        ("какой", "kakoy", "which, what kind of", "Какой твой любимый фильм?", "Kakoy tvoy lyubimyy film?", "What is your favorite movie?"),
        ("чей", "chey", "whose", "Чья это сумка?", "Chya eto sumka?", "Whose bag is this?"),
        ("сколько", "skolko", "how many, how much", "Сколько стоит?", "Skolko stoit?", "How much is it?"),
    ],
}

ENTRIES.append({
    "key": "r07_pronouns",
    "name": "Russian Pronouns",
    "group": "Foundations",
    "ladder_rank": 3,
    "ladder_tier": "foundations",
    "description": (
        "The full Russian pronoun paradigms - personal, possessive, "
        "demonstrative, and interrogative - each with transliteration, "
        "meaning, and a translated example sentence. Note the two words "
        "for 'you': ты for friends, family, and children, вы for "
        "strangers, elders, and formal situations - using ты with a "
        "stranger is rude, and using вы with a close friend is cold. "
        "Possessives agree like adjectives (мой, моя, моё, мои); его, её, "
        "and их never change. Этот means 'this' (near), тот means 'that' "
        "(far).\nPersonal pronouns:\n" + _vocab(PRON_7["personal"]) +
        "\nPossessive pronouns:\n" + _vocab(PRON_7["possessive"]) +
        "\nDemonstrative pronouns:\n" + _vocab(PRON_7["demonstrative"]) +
        "\nInterrogative pronouns:\n" + _vocab(PRON_7["interrogative"])
    ),
    "how_it_works": (
        "Pronouns decline through the six cases just like nouns, and "
        "personal pronouns have famously irregular forms: я becomes меня "
        "in the genitive/accusative, мне in the dative, мной in the "
        "instrumental, обо мне in the prepositional. Ты follows the same "
        "pattern (тебя, тебе, тобой, о тебе). After prepositions, он/она/ "
        "оно/они gain an initial н: у него (at his place), с ней (with "
        "her), к ним (to them). Possessive pronouns decline exactly like "
        "adjectives, so мой behaves like новый. The interrogatives кто "
        "and что anchor all question formation: кто for people, что for "
        "things, with какой asking 'which kind' and чей asking 'whose'."
    ),
    "key_points": [
        "Two words for 'you': informal ты for friends and family, formal вы for strangers and elders.",
        "Personal pronouns decline irregularly: я - меня - мне - мной - обо мне.",
        "After prepositions он/она/они take an initial н: у него, с ней, к ним.",
        "Possessives agree like adjectives (мой/моя/моё/мои); его, её, их are indeclinable.",
        "Этот = this (near), тот = that (far); этот/эта/это agree in gender.",
        "Interrogatives: кто (who), что (what), какой (which), чей (whose), сколько (how much/many).",
    ],
    "requirements": [
        "Memorize the ты/вы distinction and use вы by default with strangers.",
        "Drill the я and ты case forms until automatic.",
        "Practice possessive agreement: мой брат, моя сестра, моё окно, мои книги.",
    ],
    "standards": [
        "Pronoun declension follows the standard paradigms in the cited grammars.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method names every person twice: once for "
        "the near circle (ты) and once for the far circle (вы) - the "
        "pronoun itself swears the distance of the relationship. The "
        "irregular hearts of я and ты are the oldest oaths in the "
        "language, and the н that appears after prepositions is the "
        "pronoun bowing before the preposition's authority."
    ),
    "demo_key": "paradigm",
    "demo_data": {
        "counts": {"personal": 8, "possessive": 8, "demonstrative": 4,
                   "interrogative": 5},
        "ya_cases": ["я", "меня", "мне", "меня", "мной", "обо мне"],
        "case_names": ["nominative", "genitive", "dative", "accusative",
                       "instrumental", "prepositional"],
    },
})

# ---------------------------------------------------------------- record 8

NUMS_8 = [
    ("1", "один", "odin", "Одна книга.", "Odna kniga.", "One book."),
    ("2", "два", "dva", "Два стола.", "Dva stola.", "Two tables."),
    ("3", "три", "tri", "Три окна.", "Tri okna.", "Three windows."),
    ("4", "четыре", "chetyre", "Четыре стула.", "Chetyre stula.", "Four chairs."),
    ("5", "пять", "pyat", "Пять книг.", "Pyat knig.", "Five books."),
    ("6", "шесть", "shest", "Шесть дней.", "Shest dney.", "Six days."),
    ("7", "семь", "sem", "Семь чашек.", "Sem chashek.", "Seven cups."),
    ("8", "восемь", "vosem", "Восемь человек.", "Vosem chelovek.", "Eight people."),
    ("9", "девять", "devyat", "Девять месяцев.", "Devyat mesyatsev.", "Nine months."),
    ("10", "десять", "desyat", "Десять рублей.", "Desyat rubley.", "Ten rubles."),
    ("11", "одиннадцать", "odinnadtsat", "Одиннадцать учеников.", "Odinnadtsat uchenikov.", "Eleven pupils."),
    ("12", "двенадцать", "dvenadtsat", "Двенадцать часов.", "Dvenadtsat chasov.", "Twelve hours."),
    ("13", "тринадцать", "trinadtsat", "Тринадцать лет.", "Trinadtsat let.", "Thirteen years."),
    ("14", "четырнадцать", "chetyrnadtsat", "Четырнадцать дней.", "Chetyrnadtsat dney.", "Fourteen days."),
    ("15", "пятнадцать", "pyatnadtsat", "Пятнадцать минут.", "Pyatnadtsat minut.", "Fifteen minutes."),
    ("16", "шестнадцать", "shestnadtsat", "Шестнадцать страниц.", "Shestnadtsat stranits.", "Sixteen pages."),
    ("17", "семнадцать", "semnadtsat", "Семнадцать слов.", "Semnadtsat slov.", "Seventeen words."),
    ("18", "восемнадцать", "vosemnadtsat", "Восемнадцать гостей.", "Vosemnadtsat gostey.", "Eighteen guests."),
    ("19", "девятнадцать", "devyatnadtsat", "Девятнадцать рублей.", "Devyatnadtsat rubley.", "Nineteen rubles."),
    ("20", "двадцать", "dvadtsat", "Двадцать человек.", "Dvadtsat chelovek.", "Twenty people."),
    ("30", "тридцать", "tridtsat", "Тридцать дней.", "Tridtsat dney.", "Thirty days."),
    ("40", "сорок", "sorok", "Сорок минут.", "Sorok minut.", "Forty minutes."),
    ("50", "пятьдесят", "pyatdesyat", "Пятьдесят копеек.", "Pyatdesyat kopeyek.", "Fifty kopecks."),
    ("60", "шестьдесят", "shestdesyat", "Шестьдесят секунд.", "Shestdesyat sekund.", "Sixty seconds."),
    ("70", "семьдесят", "semdesyat", "Семьдесят лет.", "Semdesyat let.", "Seventy years."),
    ("80", "восемьдесят", "vosemdesyat", "Восемьдесят страниц.", "Vosemdesyat stranits.", "Eighty pages."),
    ("90", "девяносто", "devyanosto", "Девяносто дней.", "Devyanosto dney.", "Ninety days."),
    ("100", "сто", "sto", "Сто рублей.", "Sto rubley.", "One hundred rubles."),
]

TIME_8 = [
    ("Который час?", "Kotoryy chas?", "What time is it?"),
    ("Сейчас три часа.", "Seychas tri chasa.", "It is three o'clock."),
    ("Сейчас половина четвёртого.", "Seychas polovina chetvyortogo.", "It is half past three."),
    ("Сейчас без четверти пять.", "Seychas bez chetverti pyat.", "It is a quarter to five."),
    ("Сейчас двадцать минут седьмого.", "Seychas dvadtsat minut sedmogo.", "It is twenty past six."),
    ("Сегодня семнадцатое октября.", "Sevodnya semnadtsoye oktyabrya.", "Today is October seventeenth."),
    ("Мой день рождения в мае.", "Moy den rozhdeniya v maye.", "My birthday is in May."),
    ("Урок в понедельник.", "Urok v ponedelnik.", "The lesson is on Monday."),
    ("Летом тепло.", "Letom teplo.", "It is warm in summer."),
    ("Зимой холодно.", "Zimoy kholodno.", "It is cold in winter."),
]

ENTRIES.append({
    "key": "r08_numbers",
    "name": "Russian Numbers and Time",
    "group": "Foundations",
    "ladder_rank": 3,
    "ladder_tier": "foundations",
    "description": (
        "Counting to one hundred in Russian, ordinals, the days of the "
        "week, the months, the seasons, clock time, and dates - each with "
        "transliteration and a translated example sentence. Cardinal "
        "numbers 1-100:\n" +
        "\n".join("%s. %s (%s) - %s (%s - %s)" % (d, w, tr, ex, ext, en)
                  for d, w, tr, ex, ext, en in NUMS_8) +
        "\nOrdinals: первый (pervyy - first), второй (vtoroy - second), "
        "третий (tretiy - third), четвёртый (chetvyortyy - fourth), пятый "
        "(pyatyy - fifth). Days of the week: понедельник (ponedelnik - "
        "Monday), вторник (vtornik - Tuesday), среда (sreda - Wednesday), "
        "четверг (chetverg - Thursday), пятница (pyatnitsa - Friday), "
        "суббота (subbota - Saturday), воскресенье (voskresenye - Sunday). "
        "Months: январь (yanvar), февраль (fevral), март (mart), апрель "
        "(aprel), май (may), июнь (iyun), июль (iyul), август (avgust), "
        "сентябрь (sentyabr), октябрь (oktyabr), ноябрь (noyabr), декабрь "
        "(dekabr). Seasons: весна (vesna - spring), лето (leto - summer), "
        "осень (osen - autumn), зима (zima - winter). Clock time and dates:\n"
        + _sent(TIME_8)
    ),
    "how_it_works": (
        "Russian numbers govern the noun that follows them: один takes "
        "the nominative singular (один стол), два/три/четыре take the "
        "genitive singular (два стола), and пять and above take the "
        "genitive plural (пять столов). Compound numbers follow the last "
        "digit: двадцать один стол, двадцать два стола, двадцать пять "
        "столов. Clock time counts differently by half: minutes past the "
        "hour use the cardinal number plus the ordinal genitive of the "
        "coming hour (двадцать минут седьмого - twenty minutes of the "
        "seventh, i.e. 6:20), and minutes to the hour use без plus the "
        "genitive (без четверти пять - 4:45). Dates put the ordinal in "
        "the neuter (семнадцатое) and the month in the genitive (октября). "
        "The week starts on Monday, and Russians write dates day-month-year."
    ),
    "key_points": [
        "Numbers 1-100 with the irregular anchors: сорок (40), девяносто (90), сто (100).",
        "The number controls the noun's case: 1 nominative singular, 2-4 genitive singular, 5+ genitive plural.",
        "Clock time: past the hour counts 'minutes of the coming hour' (двадцать минут седьмого = 6:20); to the hour uses без (без четверти пять = 4:45).",
        "Dates: neuter ordinal + genitive month (семнадцатое октября); week starts Monday.",
        "Ordinals decline like adjectives; months and weekdays are masculine except среда, пятница, суббота (feminine).",
    ],
    "requirements": [
        "Memorize 1-20 and the tens cold; compounds are regular after that.",
        "Drill the 1 / 2-4 / 5+ noun rule with real nouns.",
        "Practice telling time both ways: minutes past and minutes to.",
    ],
    "standards": [
        "Numeral-noun government follows the standard rules in the cited grammars.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method counts by covenant: one stands "
        "alone, two through four stand as a small company, five and above "
        "as a full host - and the noun bows to each in its proper case. "
        "Time itself is sworn in halves, and the coming hour lends its "
        "name to the minutes that approach it."
    ),
    "demo_key": "numbers",
    "demo_data": {
        "units": [["один", 1], ["два", 2], ["три", 3], ["четыре", 4],
                  ["пять", 5], ["шесть", 6], ["семь", 7], ["восемь", 8],
                  ["девять", 9], ["десять", 10]],
        "teens": [["одиннадцать", 11], ["двенадцать", 12], ["тринадцать", 13],
                  ["четырнадцать", 14], ["пятнадцать", 15], ["шестнадцать", 16],
                  ["семнадцать", 17], ["восемнадцать", 18], ["девятнадцать", 19]],
        "tens": [["двадцать", 20], ["тридцать", 30], ["сорок", 40],
                 ["пятьдесят", 50], ["шестьдесят", 60], ["семьдесят", 70],
                 ["восемьдесят", 80], ["девяносто", 90], ["сто", 100]],
    },
})

# ---------------------------------------------------------------- record 9

GREET_9 = [
    ("Здравствуйте!", "Zdravstvuyte!", "Hello! (formal)", "The default polite greeting to strangers and elders."),
    ("Привет!", "Privet!", "Hi! (informal)", "For friends, family, and people your age or younger."),
    ("Доброе утро!", "Dobroye utro!", "Good morning!", "Used until about noon."),
    ("Добрый день!", "Dobryy den!", "Good afternoon!", "Used from noon until evening."),
    ("Добрый вечер!", "Dobryy vecher!", "Good evening!", "Used in the evening."),
    ("Спокойной ночи!", "Spokoynoy nochi!", "Good night!", "Said when parting at night or before sleep."),
    ("До свидания!", "Do svidaniya!", "Goodbye! (formal)", "The standard polite farewell."),
    ("Пока!", "Poka!", "Bye! (informal)", "Casual farewell among friends."),
    ("Спасибо!", "Spasibo!", "Thank you!", "Works in every situation."),
    ("Большое спасибо!", "Bolshoye spasibo!", "Thank you very much!", "Stronger gratitude."),
    ("Пожалуйста!", "Pozhaluysta!", "Please! / You are welcome!", "Means both 'please' and 'you are welcome'."),
    ("Извините!", "Izvinite!", "Excuse me! (formal)", "To get attention or apologize politely."),
    ("Извини!", "Izvini!", "Sorry! (informal)", "Casual apology to friends."),
    ("Простите!", "Prostite!", "Forgive me!", "A stronger, more formal apology."),
    ("Рад знакомству!", "Rad znakomstvu!", "Nice to meet you!", "Said when introduced; women say 'Рада'."),
    ("Как дела?", "Kak dela?", "How are you?", "Informal; expects Хорошо! or Нормально."),
    ("Как ваши дела?", "Kak vashi dela?", "How are you? (formal)", "Polite version for elders and strangers."),
    ("Хорошо.", "Khorosho.", "Fine, well.", "The standard positive answer."),
    ("Нормально.", "Normalno.", "Okay, so-so.", "The honest neutral answer."),
    ("Добро пожаловать!", "Dobro pozhalovat!", "Welcome!", "Greeting an arriving guest."),
    ("Удачи!", "Udachi!", "Good luck!", "Before exams, trips, and ventures."),
    ("Поздравляю!", "Pozdravlyayu!", "Congratulations!", "For birthdays and achievements."),
    ("Приятного аппетита!", "Priyatnogo appetita!", "Enjoy your meal!", "Said before eating together."),
    ("Будьте здоровы!", "Budte zdorovy!", "Bless you! (after a sneeze)", "Also a drinking toast to health."),
    ("Всего хорошего!", "Vsego khoroshego!", "All the best!", "A warm parting wish."),
    ("До встречи!", "Do vstrechi!", "See you!", "When you expect to meet again."),
    ("До завтра!", "Do zavtra!", "See you tomorrow!", "Parting until the next day."),
    ("Как вас зовут?", "Kak vas zovut?", "What is your name? (formal)", "Literally 'how are you called'."),
    ("Меня зовут Анна.", "Menya zovut Anna.", "My name is Anna.", "Answer with your own name."),
    ("Откуда вы?", "Otkuda vy?", "Where are you from? (formal)", "The polite getting-to-know-you question."),
]

ENTRIES.append({
    "key": "r09_greetings",
    "name": "Russian Greetings and Everyday Phrases",
    "group": "Foundations",
    "ladder_rank": 3,
    "ladder_tier": "foundations",
    "description": (
        "Thirty greetings, farewells, and politeness phrases - the social "
        "survival kit of Russian - each with transliteration, English "
        "meaning, and a usage note. Russian politeness runs on the "
        "formal/informal split: default to the formal forms (Здравствуйте, "
        "Извините, вы) with anyone you do not know well, and switch to the "
        "informal forms (Привет, Извини, ты) only when invited or with "
        "clear peers.\n" + _phrases(GREET_9)
    ),
    "how_it_works": (
        "Russian greetings are time-anchored: утро in the morning, день "
        "in the afternoon, вечер in the evening, and ночи only when "
        "parting for sleep. Спасибо never needs a case ending and works "
        "everywhere; пожалуйста is the universal softener that turns any "
        "command into a polite request. Извините opens conversations with "
        "strangers ('excuse me, where is...'), while простите repairs a "
        "real offense. Small talk is thinner than in English - Как дела? "
        "expects a short honest answer, not a story - but hospitality "
        "phrases run deep: guests are greeted, fed, and seen off with "
        "fixed warm formulas."
    ),
    "key_points": [
        "30 greetings and politeness phrases with usage notes for formal vs informal situations.",
        "Default to formal (вы, Здравствуйте, Извините) with strangers; informal is earned, not assumed.",
        "Greetings follow the time of day: утро, день, вечер; Спокойной ночи only at parting/sleep.",
        "Пожалуйста means both 'please' and 'you are welcome' - the hardest-working word in the kit.",
        "Как дела? wants a short answer: Хорошо, Нормально, Плохо.",
    ],
    "requirements": [
        "Memorize all 30 phrases with their formality level.",
        "Practice the time-of-day greetings in order through a full day.",
        "Role-play meeting a stranger (formal) and meeting a friend (informal).",
    ],
    "standards": [
        "Phrase selection follows standard pedagogical phrasebooks and usage guides.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method treats every greeting as a sworn "
        "approach: the formal forms are the raised banner shown to "
        "strangers, the informal forms the lowered banner shown to kin. "
        "Time itself dictates the banner's words - morning, day, evening "
        "each have their sworn greeting."
    ),
    "demo_key": "phrases",
    "demo_data": {"count": 30,
                  "sample": [["Здравствуйте!", "Zdravstvuyte!", "Hello! (formal)"],
                             ["Привет!", "Privet!", "Hi! (informal)"],
                             ["Спасибо!", "Spasibo!", "Thank you!"]]},
})

# ---------------------------------------------------------------- record 10

GRAM_10 = [
    ("Слово порядок: подлежащее - сказуемое - дополнение.",
     "Slovo poryadok: podlezhashcheye - skazuyemoye - dopolneniye.",
     "Word order: subject - verb - object.",
     "Russian defaults to SVO, but any order is grammatical; order signals emphasis, not roles."),
    ("Существительные имеют три рода: мужской, женский, средний.",
     "Sushchestvitelnyye imeyut tri roda: muzhskoy, zhenskiy, sredniy.",
     "Nouns have three genders: masculine, feminine, neuter.",
     "Gender is usually read from the ending and controls all agreement."),
    ("Именительный падеж - кто? что? - подлежащее.",
     "Imenitelnyy padezh - kto? chto? - podlezhashcheye.",
     "Nominative case - who? what? - the subject. Example: Мама читает. (Mama chitayet. - Mother is reading.)",
     "The dictionary form of every noun; names the doer of the action."),
    ("Родительный падеж - кого? чего? - принадлежность и отсутствие.",
     "Roditelnyy padezh - kovo? chevo? - prinadlezhnost i otsutstviye.",
     "Genitive case - of whom? of what? - possession and absence. Example: Книга брата. (Kniga brata. - The brother's book.) У меня нет времени. (U menya net vremeni. - I have no time.)",
     "Also marks possession, absence with нет, and nouns after numbers 5 and above."),
    ("Дательный падеж - кому? чему? - адресат.",
     "Datelnyy padezh - komu? chemu? - adresat.",
     "Dative case - to whom? to what? - the recipient. Example: Я дал книгу другу. (Ya dal knigu drugu. - I gave the book to a friend.)",
     "Also used for age (мне двадцать лет) and liking (мне нравится)."),
    ("Винительный падеж - кого? что? - прямое дополнение.",
     "Vinitelnyy padezh - kovo? chto? - pryamoye dopolneniye.",
     "Accusative case - whom? what? - the direct object. Example: Я читаю книгу. (Ya chitayu knigu. - I am reading a book.)",
     "Inanimate masculine and neuter accusative matches the nominative form."),
    ("Творительный падеж - кем? чем? - инструмент и спутник.",
     "Tvoritelnyy padezh - kem? chem? - instrument i sputnik.",
     "Instrumental case - by whom? with what? - instrument and companion. Example: Я пишу ручкой. (Ya pishu ruchkoy. - I write with a pen.) Мы гуляем с другом. (My gulyayem s drugom. - We walk with a friend.)",
     "Also used for predicate nouns: он был учителем (he was a teacher)."),
    ("Предложный падеж - о ком? о чём? - место и тема.",
     "Predlozhnyy padezh - o kom? o chyom? - mesto i tema.",
     "Prepositional case - about whom? about what? - place and topic. Example: Я живу в городе. (Ya zhivu v gorode. - I live in a city.) Мы говорим о книге. (My govorim o knige. - We talk about the book.)",
     "Always used with a preposition: в, на, о, при."),
    ("Артиклей нет: книга значит и 'a book', и 'the book'.",
     "Artikley net: kniga znachit i 'a book', i 'the book'.",
     "There are no articles: книга means both 'a book' and 'the book'.",
     "Definiteness comes from context and word order, not from articles."),
    ("Отрицание: не перед глаголом, нет для отсутствия.",
     "Otritsaniye: ne pered glagolom, net dlya otsutstviya.",
     "Negation: не before the verb, нет for absence.",
     "Example: Я не знаю. (Ya ne znayu. - I do not know.) Здесь нет молока. (Zdes net moloka. - There is no milk here.)"),
    ("Вопросы: интонация, вопросительные слова, частица ли.",
     "Voprosy: intonatsiya, voprositelnyye slova, chastitsa li.",
     "Questions: intonation, question words, the particle ли.",
     "Example: Ты идёшь? (Ty idyosh? - Are you going?) Где ты живёшь? (Gde ty zhivyosh? - Where do you live?) Знаешь ли ты? (Znayesh li ty? - Do you know?)"),
    ("Число: единственное и множественное; plural endings -ы/-и, -а/-я.",
     "Chislo: yedinstvennoye i mnozhestvennoye.",
     "Number: singular and plural; plural endings -ы/-и, -а/-я.",
     "Example: стол - столы, книга - книги, окно - окна, дом - дома."),
]

ENTRIES.append({
    "key": "r10_grammar",
    "name": "Russian Grammar Essentials",
    "group": "Foundations",
    "ladder_rank": 3,
    "ladder_tier": "foundations",
    "description": (
        "The essential grammar of Russian in twelve rules, each with "
        "transliteration, English translation, and translated example "
        "sentences: word order, gender, number, the six cases, the absence "
        "of articles, negation, and question formation.\n" +
        "\n".join("%d. %s (%s - %s) %s" % (i + 1, ru, tr, en, note)
                  for i, (ru, tr, en, note) in enumerate(GRAM_10))
    ),
    "how_it_works": (
        "Russian grammar is a system of endings doing the work that word "
        "order and helper words do in English. The six cases are the core "
        "machine: nominative names the doer, genitive names the owner and "
        "marks absence, dative names the receiver, accusative names the "
        "object, instrumental names the tool or companion, prepositional "
        "names the place or topic - and each is triggered by its question "
        "word (кто/что, кого/чего, кому/чему, кого/что, кем/чем, о ком/о "
        "чём). Gender and number flow through agreement: adjectives and "
        "past-tense verbs copy the noun's features. Negation is a single "
        "не before the verb, and questions need no word-order change - "
        "intonation alone can turn Ты идёшь into Ты идёшь?. Master the "
        "case questions and the rest of the grammar becomes lookup, not "
        "mystery."
    ),
    "key_points": [
        "Default word order is SVO, but any order is grammatical - endings, not position, mark roles.",
        "Three genders and two numbers drive all agreement.",
        "Six cases, each with its question word: nominative (кто/что), genitive (кого/чего), dative (кому/чему), accusative (кого/что), instrumental (кем/чем), prepositional (о ком/о чём).",
        "No articles: definiteness lives in context and word order.",
        "Negation with не; нет declares absence and takes the genitive.",
        "Questions via intonation, question words, or the particle ли - no inversion needed.",
    ],
    "requirements": [
        "Memorize the six case names with their question words.",
        "Practice identifying the case of every noun in the earlier records' sentences.",
        "Drill не vs нет until the distinction is automatic.",
    ],
    "standards": [
        "Case analysis follows the standard six-case description in the cited grammars.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method swears the six cases as six "
        "covenants of role: the nominative names, the genitive owns and "
        "denies, the dative receives, the accusative suffers the action, "
        "the instrumental serves as tool and companion, the prepositional "
        "holds the place and the topic. Learn the six questions and you "
        "hold the keys to every sentence."
    ),
    "demo_key": "cases",
    "demo_data": {
        "declensions": {
            "дом": ["дом", "дома", "дому", "дом", "домом", "доме"],
            "книга": ["книга", "книги", "книге", "книгу", "книгой", "книге"],
            "окно": ["окно", "окна", "окну", "окно", "окном", "окне"],
        },
        "case_names": ["nominative", "genitive", "dative", "accusative",
                       "instrumental", "prepositional"],
        "genders": {"дом": "masculine", "книга": "feminine", "окно": "neuter"},
    },
})

# ---------------------------------------------------------------- record 11

SENT_11 = [
    ("Это наш дом.", "Eto nash dom.", "This is our house."),
    ("В доме пять комнат.", "V dome pyat komnat.", "The house has five rooms."),
    ("Гостиная большая и светлая.", "Gostinaya bolshaya i svetlaya.", "The living room is big and bright."),
    ("Кухня находится рядом со столовой.", "Kukhnya nakhoditsya ryadom so stolovoy.", "The kitchen is next to the dining room."),
    ("В спальне стоит удобная кровать.", "V spalne stoit udobnaya krovat.", "There is a comfortable bed in the bedroom."),
    ("Ванная комната чистая.", "Vannaya komnata chistaya.", "The bathroom is clean."),
    ("На столе стоит ваза с цветами.", "Na stole stoit vaza s tsvetami.", "There is a vase with flowers on the table."),
    ("Книги лежат на полке.", "Knigi lezhat na polke.", "The books are on the shelf."),
    ("Мой отец - инженер.", "Moy otets - inzhener.", "My father is an engineer."),
    ("Моя мама - врач.", "Moya mama - vrach.", "My mother is a doctor."),
    ("У меня есть брат и сестра.", "U menya yest brat i sestra.", "I have a brother and a sister."),
    ("Мой брат старше меня.", "Moy brat starshe menya.", "My brother is older than me."),
    ("Моя сестра младше меня.", "Moya sestra mladshe menya.", "My sister is younger than me."),
    ("Бабушка живёт в деревне.", "Babushka zhivyot v derevne.", "Grandmother lives in a village."),
    ("Дедушка любит рыбалку.", "Dedushka lyubit rybalku.", "Grandfather loves fishing."),
    ("Мы часто собираемся всей семьёй.", "My chasto sobirayemsya vsey semyoy.", "We often gather as a whole family."),
    ("Дети играют в саду.", "Deti igrayut v sadu.", "The children are playing in the garden."),
    ("Собака спит у двери.", "Sobaka spit u dveri.", "The dog is sleeping by the door."),
    ("Кошка сидит на окне.", "Koshka sidit na okne.", "The cat is sitting on the windowsill."),
    ("Мы любим наш уютный дом.", "My lyubim nash uyutnyy dom.", "We love our cozy home."),
]

ENTRIES.append({
    "key": "r11_home",
    "name": "Russian Home and Family Sentences",
    "group": "Compounded",
    "ladder_rank": 4,
    "ladder_tier": "compounded",
    "description": (
        "Twenty sentences about the house, its rooms and furniture, and "
        "family members - each in Russian with transliteration and English "
        "translation. These sentences put the foundations to work: "
        "prepositional case for location (в доме, на столе), instrumental "
        "for companionship (всей семьёй), and adjective agreement across "
        "genders.\n" + _sent(SENT_11)
    ),
    "how_it_works": (
        "Location sentences run on the prepositional case after в and на: "
        "в доме (in the house), на столе (on the table), на окне (on the "
        "windowsill). Family relations use the genitive of belonging and "
        "the у + genitive construction for possession: У меня есть брат "
        "(at me there is a brother - I have a brother). Comparisons of age "
        "use the comparative with чем or the genitive: старше меня (older "
        "than me). The dash in Мой отец - инженер replaces the missing "
        "present-tense 'is'. Read each sentence, find the case ending, and "
        "name the rule that put it there."
    ),
    "key_points": [
        "20 home and family sentences with full translations.",
        "Location lives in the prepositional case: в доме, на столе, в саду.",
        "Possession uses у + genitive: У меня есть брат.",
        "Age comparison: старше/ младше + genitive.",
        "The dash replaces present-tense 'is': Мой отец - инженер.",
    ],
    "requirements": [
        "Read all 20 sentences aloud; mark the case of each underlined noun.",
        "Describe your own home in 5 Russian sentences.",
        "Name all family members in Russian from memory.",
    ],
    "standards": [
        "Sentence patterns follow standard pedagogical models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method builds the house of the language "
        "first: rooms as sworn places, furniture as sworn tools, family as "
        "the sworn circle. Every sentence here is a brick - location, "
        "possession, kinship - laid in covenant order."
    ),
    "demo_key": "sentences",
    "demo_data": {"sentences": [list(s) for s in SENT_11], "topic": "home and family"},
})

# ---------------------------------------------------------------- record 12

SENT_12 = [
    ("На завтрак я ем кашу.", "Na zavtrak ya yem kashu.", "For breakfast I eat porridge."),
    ("Мама готовит вкусный суп.", "Mama gotovit vkusnyy sup.", "Mother is cooking tasty soup."),
    ("Мы обедаем в час дня.", "My obedayem v chas dnya.", "We have lunch at one o'clock."),
    ("На ужин будет рыба с овощами.", "Na uzhin budet ryba s ovoshchami.", "For dinner there will be fish with vegetables."),
    ("Хлеб свежий и тёплый.", "Khleb svezhiy i tyoplyy.", "The bread is fresh and warm."),
    ("Добавь соль по вкусу.", "Dobav sol po vkusu.", "Add salt to taste."),
    ("Я режу овощи ножом.", "Ya rezhu ovoshchi nozhom.", "I am cutting vegetables with a knife."),
    ("Вода уже кипит.", "Voda uzhe kipit.", "The water is already boiling."),
    ("Поставь чайник на плиту.", "Postav chaynik na plitu.", "Put the kettle on the stove."),
    ("Мы пьём чай с лимоном.", "My pyom chay s limonom.", "We drink tea with lemon."),
    ("Кофе слишком горячий.", "Kofe slishkom goryachiy.", "The coffee is too hot."),
    ("Я люблю яблочный сок.", "Ya lyublyu yablochnyy sok.", "I like apple juice."),
    ("В ресторане вкусное меню.", "V restorane vkusnoye menyu.", "The restaurant has a tasty menu."),
    ("Официант принёс счёт.", "Ofitsiant prinyos schyot.", "The waiter brought the bill."),
    ("Этот торт очень сладкий.", "Etot tort ochen sladkiy.", "This cake is very sweet."),
    ("Фрукты полезные для здоровья.", "Frukty poleznyye dlya zdorovya.", "Fruit is good for health."),
    ("Я не ем мясо.", "Ya ne yem myaso.", "I do not eat meat."),
    ("Приятного аппетита!", "Priyatnogo appetita!", "Enjoy your meal!"),
    ("Спасибо, было очень вкусно.", "Spasibo, bylo ochen vkusno.", "Thanks, it was very tasty."),
    ("Помой, пожалуйста, посуду.", "Pomoy, pozhaluysta, posudu.", "Wash the dishes, please."),
]

ENTRIES.append({
    "key": "r12_food",
    "name": "Russian Food and Cooking Sentences",
    "group": "Compounded",
    "ladder_rank": 4,
    "ladder_tier": "compounded",
    "description": (
        "Twenty sentences about meals, ingredients, cooking actions, and "
        "the restaurant - each in Russian with transliteration and English "
        "translation. Food sentences drill the accusative of the direct "
        "object (ем кашу, режу овощи), the instrumental of instrument "
        "(ножом, с лимоном), and polite imperatives (добавь, поставь, "
        "помой).\n" + _sent(SENT_12)
    ),
    "how_it_works": (
        "Cooking verbs take their ingredients in the accusative: готовить "
        "суп, резать овощи, пить чай. The tool or accompaniment goes to "
        "the instrumental: ножом (with a knife), с лимоном (with lemon), "
        "с овощами (with vegetables). Recipe instructions use the informal "
        "imperative (добавь, поставь) while requests soften with "
        "пожалуйста. Meals of the day are завтрак, обед, ужин, with the "
        "prepositions на + accusative for the meal as destination: на "
        "завтрак, на ужин. Restaurant service runs on fixed formulas: "
        "принёс счёт (brought the bill), приятного аппетита (enjoy your "
        "meal)."
    ),
    "key_points": [
        "20 food and cooking sentences with full translations.",
        "Ingredients take the accusative: готовлю суп, режу овощи.",
        "Tools and accompaniments take the instrumental: ножом, с лимоном.",
        "Recipe commands use the informal imperative; requests add пожалуйста.",
        "Meal formulas: на завтрак/обед/ужин; Приятного аппетита!",
    ],
    "requirements": [
        "Cook a simple dish narrating each step in Russian.",
        "Order a full meal in Russian: appetizer, main, drink, bill.",
        "List 10 foods with their accusative forms.",
    ],
    "standards": [
        "Sentence patterns follow standard pedagogical models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "In the Signature Russian Method the kitchen is a sworn "
        "workshop: ingredients take the accusative as the honored object "
        "of the action, tools take the instrumental as sworn helpers, and "
        "every recipe command is a direct oath from cook to helper."
    ),
    "demo_key": "sentences",
    "demo_data": {"sentences": [list(s) for s in SENT_12], "topic": "food and cooking"},
})

# ---------------------------------------------------------------- record 13

SENT_13 = [
    ("Я еду в аэропорт на такси.", "Ya yedu v aeroport na taksi.", "I am going to the airport by taxi."),
    ("Поезд отправляется в восемь утра.", "Poyezd otpravlyayetsya v vosem utra.", "The train leaves at eight in the morning."),
    ("Где здесь остановка автобуса?", "Gde zdes ostanovka avtobusa?", "Where is the bus stop here?"),
    ("Скажите, пожалуйста, как пройти к метро?", "Skazhite, pozhaluysta, kak proyti k metro?", "Tell me, please, how to get to the metro?"),
    ("Идите прямо, потом поверните направо.", "Idite pryamo, potom povernite napravo.", "Go straight, then turn right."),
    ("Музей находится недалеко отсюда.", "Muzey nakhoditsya nedaleko otsyuda.", "The museum is not far from here."),
    ("Сколько стоит билет до центра?", "Skolko stoit bilet do tsentra?", "How much is a ticket to the center?"),
    ("Два билета, пожалуйста.", "Dva bileta, pozhaluysta.", "Two tickets, please."),
    ("Мы летим самолётом в Сочи.", "My letim samolyotom v Sochi.", "We are flying to Sochi."),
    ("Полёт длится два часа.", "Polyot dlitsya dva chasa.", "The flight lasts two hours."),
    ("Я забронировал номер в гостинице.", "Ya zabroniroval nomer v gostinitse.", "I booked a room at the hotel."),
    ("У вас есть свободные места?", "U vas yest svobodnyye mesta?", "Do you have free seats?"),
    ("Мой рейс задержали на час.", "Moy reys zaderzhali na chas.", "My flight was delayed by an hour."),
    ("Где можно взять карту города?", "Gde mozhno vzyat kartu goroda?", "Where can I get a city map?"),
    ("Это далеко? Можно дойти пешком?", "Eto daleko? Mozhno doyti peshkom?", "Is it far? Can I walk there?"),
    ("Нет, это совсем рядом.", "Net, eto sovsem ryadom.", "No, it is quite close."),
    ("Вызовите, пожалуйста, такси.", "Vyzovite, pozhaluysta, taksi.", "Please call a taxi."),
    ("Отвезите меня в центр, пожалуйста.", "Otvezite menya v tsentr, pozhaluysta.", "Take me downtown, please."),
    ("Остановите здесь, пожалуйста.", "Ostanovite zdes, pozhaluysta.", "Stop here, please."),
    ("Спасибо за поездку!", "Spasibo za poyezdku!", "Thanks for the ride!"),
]

ENTRIES.append({
    "key": "r13_travel",
    "name": "Russian Travel and Directions Sentences",
    "group": "Compounded",
    "ladder_rank": 4,
    "ladder_tier": "compounded",
    "description": (
        "Twenty sentences about transport, asking directions, tickets, "
        "and lodging - each in Russian with transliteration and English "
        "translation. Travel sentences drill motion verbs (ехать, лететь, "
        "идти), the accusative of destination (в аэропорт, в Сочи, до "
        "центра), and formal imperatives for polite requests (скажите, "
        "вызовите, отвезите).\n" + _sent(SENT_13)
    ),
    "how_it_works": (
        "Destination takes в/на + accusative: в аэропорт, в Сочи, в центр; "
        "origin and 'from' take из/с + genitive. Motion by vehicle uses "
        "ехать/лететь/плыть while motion on foot uses идти/ходить - the "
        "means of motion is never left vague in Russian. Directions chain "
        "imperatives: идите, поверните, остановите. Transport by means "
        "takes the instrumental: на такси, самолётом, пешком (on foot, "
        "adverbial). Asking the way always opens with a softener - "
        "скажите, пожалуйста - and closings thank the helper: спасибо за "
        "поездку."
    ),
    "key_points": [
        "20 travel sentences with full translations.",
        "Destination: в/на + accusative; means of travel: instrumental (самолётом, на такси).",
        "Motion verbs split by means: идти on foot, ехать by vehicle, лететь by air.",
        "Direction-giving chains formal imperatives: идите, поверните.",
        "Polite travel requests always carry пожалуйста.",
    ],
    "requirements": [
        "Ask for and give directions to 3 places in Russian.",
        "Buy a ticket and book a room in a role-play.",
        "Describe your last trip in 5 sentences.",
    ],
    "standards": [
        "Sentence patterns follow standard pedagogical models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method treats every journey as a sworn "
        "passage: the destination takes the accusative as the oath's "
        "target, the vehicle takes the instrumental as the sworn steed, "
        "and direction-givers speak in the formal imperative - the "
        "command voice of the road."
    ),
    "demo_key": "sentences",
    "demo_data": {"sentences": [list(s) for s in SENT_13], "topic": "travel and directions"},
})

# ---------------------------------------------------------------- record 14

SENT_14 = [
    ("Я работаю в большой компании.", "Ya rabotayu v bolshoy kompanii.", "I work at a large company."),
    ("Мой офис находится в центре города.", "Moy ofis nakhoditsya v tsentre goroda.", "My office is in the city center."),
    ("Рабочий день начинается в девять.", "Rabochiy den nachinayetsya v devyat.", "The workday starts at nine."),
    ("У меня встреча в три часа.", "U menya vstrecha v tri chasa.", "I have a meeting at three."),
    ("Коллеги очень дружелюбные.", "Kollegi ochen druzhelyubnyye.", "The colleagues are very friendly."),
    ("Я получил повышение.", "Ya poluchil povysheniye.", "I got a promotion."),
    ("Зарплату платят вовремя.", "Zarplatu platyat vovremya.", "The salary is paid on time."),
    ("Мне нравится моя работа.", "Mne nravitsya moya rabota.", "I like my job."),
    ("Дети идут в школу утром.", "Deti idut v shkolu utrom.", "The children go to school in the morning."),
    ("Урок математики интересный.", "Urok matematiki interesnyy.", "The math lesson is interesting."),
    ("Учитель объясняет новое правило.", "Uchitel obyasnyayet novoye pravilo.", "The teacher is explaining a new rule."),
    ("Ученики пишут диктант.", "Ucheniki pishut diktant.", "The pupils are writing a dictation."),
    ("Я получил пятёрку по русскому.", "Ya poluchil pyatyorku po russkomu.", "I got an A in Russian."),
    ("Домашнее задание трудное.", "Domashneye zadaniye trudnoye.", "The homework is difficult."),
    ("Мы учим новые слова каждый день.", "My uchim novyye slova kazhdyy den.", "We learn new words every day."),
    ("Перемена длится десять минут.", "Peremena dlitsya desyat minut.", "The break lasts ten minutes."),
    ("В столовой вкусные обеды.", "V stolovoy vkusnyye obedy.", "The canteen has tasty lunches."),
    ("После школы я хожу на спорт.", "Posle shkoly ya khozhu na sport.", "After school I go to sports."),
    ("Экзамены будут в июне.", "Ekzameny budut v iyune.", "The exams will be in June."),
    ("Я хочу поступить в университет.", "Ya khochu postupit v universitet.", "I want to enter university."),
]

ENTRIES.append({
    "key": "r14_work",
    "name": "Russian Work and School Sentences",
    "group": "Compounded",
    "ladder_rank": 5,
    "ladder_tier": "compounded",
    "description": (
        "Twenty sentences about jobs, the office, the classroom, and "
        "learning - each in Russian with transliteration and English "
        "translation. Work sentences drill the prepositional of workplace "
        "(в компании, в офисе), the dative of liking (мне нравится), and "
        "school sentences drill subjects in the genitive (урок математики) "
        "and grades (пятёрка по русскому).\n" + _sent(SENT_14)
    ),
    "how_it_works": (
        "Workplace location uses в + prepositional: в компании, в офисе, "
        "в центре города. Liking is expressed impersonally with the "
        "dative: мне нравится (to me it is pleasing - I like it). School "
        "subjects attach in the genitive: урок математики, пятёрка по "
        "русскому (an A in Russian, with по + dative for the subject). "
        "Time expressions anchor the routine: в девять, в три часа, в "
        "июне, каждый день. The verb поступить (perfective) marks the "
        "single completed act of entering university, while учиться "
        "(imperfective) marks the ongoing studying."
    ),
    "key_points": [
        "20 work and school sentences with full translations.",
        "Workplace: в + prepositional (в офисе, в компании).",
        "Liking is dative-impersonal: мне нравится моя работа.",
        "School subjects: genitive (урок математики); grades: пятёрка по русскому.",
        "Aspect contrast: учиться (ongoing) vs поступить (single completed act).",
    ],
    "requirements": [
        "Describe your job or studies in 5 sentences.",
        "Role-play a meeting schedule and a parent-teacher talk.",
        "List 5 school subjects with their Russian names.",
    ],
    "standards": [
        "Sentence patterns follow standard pedagogical models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method swears the workplace and the "
        "classroom as two halls of duty: the office hall speaks in "
        "prepositional place-oaths, the school hall in genitive "
        "subject-oaths, and liking is sworn impersonally - the thing "
        "pleases me, I do not seize it."
    ),
    "demo_key": "sentences",
    "demo_data": {"sentences": [list(s) for s in SENT_14], "topic": "work and school"},
})

# ---------------------------------------------------------------- record 15

SENT_15 = [
    ("У меня болит голова.", "U menya bolit golova.", "My head aches."),
    ("У меня болит горло.", "U menya bolit gorlo.", "My throat hurts."),
    ("У меня высокая температура.", "U menya vysokaya temperatura.", "I have a high temperature."),
    ("Я чувствую себя плохо.", "Ya chuvstvuyu sebya plokho.", "I feel bad."),
    ("Мне нужен врач.", "Mne nuzhen vrach.", "I need a doctor."),
    ("Запишитесь на приём к терапевту.", "Zapishites na priyom k terapevtu.", "Make an appointment with a physician."),
    ("Что вас беспокоит?", "Chto vas bespokoit?", "What troubles you?"),
    ("У меня кашель и насморк.", "U menya kashel i nasmork.", "I have a cough and a runny nose."),
    ("Дышите глубже, пожалуйста.", "Dyshite glubzhe, pozhaluysta.", "Breathe deeply, please."),
    ("Вам нужно больше отдыхать.", "Vam nuzhno bolshe otdykhat.", "You need to rest more."),
    ("Принимайте это лекарство два раза в день.", "Prinimayte eto lekarstvo dva raza v den.", "Take this medicine twice a day."),
    ("Где ближайшая аптека?", "Gde blizhayshaya apteka?", "Where is the nearest pharmacy?"),
    ("У вас есть что-нибудь от головной боли?", "U vas yest chto-nibud ot golovnoy boli?", "Do you have anything for a headache?"),
    ("Мои глаза устали.", "Moi glaza ustali.", "My eyes are tired."),
    ("Рука болит после тренировки.", "Ruka bolit posle trenirovki.", "My arm hurts after training."),
    ("Сердце бьётся быстро.", "Serdtse byotsya bystro.", "The heart is beating fast."),
    ("Пейте больше воды.", "Peyte bolshe vody.", "Drink more water."),
    ("Ешьте больше овощей и фруктов.", "Yeshte bolshe ovoshchey i fruktov.", "Eat more vegetables and fruit."),
    ("Спорт полезен для здоровья.", "Sport polezen dlya zdorovya.", "Sport is good for health."),
    ("Выздоравливайте скорее!", "Vyzdoravlivayte skoreye!", "Get well soon!"),
]

ENTRIES.append({
    "key": "r15_health",
    "name": "Russian Health and Body Sentences",
    "group": "Compounded",
    "ladder_rank": 5,
    "ladder_tier": "compounded",
    "description": (
        "Twenty sentences about body parts, symptoms, the doctor visit, "
        "and the pharmacy - each in Russian with transliteration and "
        "English translation. Health sentences drill the у + genitive "
        "pain formula (у меня болит голова), the dative of need (мне "
        "нужен врач, вам нужно отдыхать), and formal medical imperatives "
        "(дышите, принимайте, запишитесь).\n" + _sent(SENT_15)
    ),
    "how_it_works": (
        "Pain is reported with the body part as the grammatical subject: "
        "у меня болит голова (at me the head aches) - the head does the "
        "aching, you are the location. Need is dative-impersonal: мне "
        "нужен врач, вам нужно отдыхать. Doctors speak in the formal "
        "imperative plural: дышите, принимайте. The pharmacy question "
        "uses от + genitive for the ailment: что-нибудь от головной боли "
        "(something for headache). Health vocabulary centers on "
        "болит/болят for pain, температура for fever, and лекарство for "
        "medicine."
    ),
    "key_points": [
        "20 health sentences with full translations.",
        "Pain formula: у меня болит + nominative body part (the part is the subject).",
        "Need is dative-impersonal: мне нужен врач; вам нужно отдыхать.",
        "Medical imperatives are formal plural: дышите, принимайте.",
        "Pharmacy: что-нибудь от + genitive (от головной боли).",
    ],
    "requirements": [
        "Describe 3 symptoms in Russian using the болит formula.",
        "Role-play a doctor visit: complaint, examination, prescription.",
        "Name 10 body parts from memory.",
    ],
    "standards": [
        "Sentence patterns follow standard pedagogical models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method treats the body as a sworn vessel: "
        "pain is reported by naming the suffering part as the speaker - "
        "the head itself declares its ache. Need is sworn impersonally, "
        "and the healer's commands arrive in the formal plural, the voice "
        "of sworn care."
    ),
    "demo_key": "sentences",
    "demo_data": {"sentences": [list(s) for s in SENT_15], "topic": "health and body"},
})

# ---------------------------------------------------------------- record 16

SENT_16 = [
    ("Я очень счастлив сегодня.", "Ya ochen schastliv sevodnya.", "I am very happy today."),
    ("Она рада видеть тебя.", "Ona rada videt tebya.", "She is glad to see you."),
    ("Мы смеёмся над шуткой.", "My smeyomsya nad shutkoy.", "We are laughing at the joke."),
    ("Это прекрасная новость!", "Eto prekrasnaya novost!", "This is wonderful news!"),
    ("Я грущу без тебя.", "Ya grushchu bez tebya.", "I am sad without you."),
    ("Он плачет от горя.", "On plachet ot gorya.", "He is crying from grief."),
    ("Мне одиноко вечером.", "Mne odinoko vecherom.", "I feel lonely in the evening."),
    ("Не расстраивайся, всё будет хорошо.", "Ne rasstraivaysya, vsyo budet khorosho.", "Do not be upset, everything will be fine."),
    ("Я злюсь, когда меня обманывают.", "Ya zlyus, kogda menya obmanyvayut.", "I get angry when I am deceived."),
    ("Он сердится на брата.", "On serditsya na brata.", "He is angry at his brother."),
    ("Успокойся, пожалуйста.", "Uspokoysya, pozhaluysta.", "Calm down, please."),
    ("Я боюсь темноты.", "Ya boyus temnoty.", "I am afraid of the dark."),
    ("Не бойся, я рядом.", "Ne boysya, ya ryadom.", "Do not be afraid, I am near."),
    ("Меня пугает гроза.", "Menya pugayet groza.", "Thunderstorms frighten me."),
    ("Я люблю тебя всем сердцем.", "Ya lyublyu tebya vsem serdtsem.", "I love you with all my heart."),
    ("Они любят друг друга.", "Oni lyubyat drug druga.", "They love each other."),
    ("Я удивлён твоим поступком.", "Ya udivlyon tvoim postupkom.", "I am surprised by your act."),
    ("Какая неожиданность!", "Kakaya neozhidannost!", "What a surprise!"),
    ("Мне стыдно за свои слова.", "Mne stydno za svoi slova.", "I am ashamed of my words."),
    ("Я горжусь своим сыном.", "Ya gorzhus svoim synom.", "I am proud of my son."),
]

ENTRIES.append({
    "key": "r16_emotions",
    "name": "Russian Emotions and Feelings Sentences",
    "group": "Compounded",
    "ladder_rank": 5,
    "ladder_tier": "compounded",
    "description": (
        "Twenty sentences about being happy, sad, angry, afraid, in love, "
        "and surprised - each in Russian with transliteration and English "
        "translation. Emotion sentences drill short-form adjectives "
        "(счастлив, рада, удивлён), reflexive emotion verbs (смеяться, "
        "злиться, бояться, гордиться), and the dative of feeling (мне "
        "одиноко, мне стыдно).\n" + _sent(SENT_16)
    ),
    "how_it_works": (
        "Feelings split into two grammatical strategies. Active emotions "
        "use reflexive verbs: смеяться (to laugh), злиться (to be angry), "
        "бояться (to fear), гордиться (to be proud) - the -ся turns the "
        "feeling back on the feeler. States use short-form adjectives or "
        "the dative-impersonal: я счастлив, она рада, мне одиноко, мне "
        "стыдно. Causes take от + genitive (плачет от горя) or the "
        "instrumental of the trigger (удивлён твоим поступком, горжусь "
        "сыном). Comforting runs on the negative imperative: не "
        "расстраивайся, не бойся, успокойся."
    ),
    "key_points": [
        "20 emotion sentences with full translations.",
        "Emotion verbs are reflexive: бояться, злиться, смеяться, гордиться.",
        "States use short adjectives (счастлив, рада) or dative-impersonal (мне одиноко).",
        "Causes: от + genitive (от горя) or instrumental (твоим поступком).",
        "Comforting: negative imperatives - не бойся, не расстраивайся.",
    ],
    "requirements": [
        "Describe your current mood in 3 Russian sentences.",
        "Conjugate бояться and гордиться in the present.",
        "Comfort a friend in Russian using two imperatives.",
    ],
    "standards": [
        "Sentence patterns follow standard pedagogical models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "In the Signature Russian Method feelings are sworn states of "
        "the heart: active passions turn inward with the reflexive oath "
        "-ся, quiet states are declared in short-form truth, and the "
        "dative carries what the heart cannot hold alone - мне одиноко, "
        "мне стыдно."
    ),
    "demo_key": "sentences",
    "demo_data": {"sentences": [list(s) for s in SENT_16], "topic": "emotions and feelings"},
})

# ---------------------------------------------------------------- record 17

SENT_17 = [
    ("Сегодня солнечная погода.", "Sevodnya solnechnaya pogoda.", "Today the weather is sunny."),
    ("На улице идёт дождь.", "Na ulitse idyot dozhd.", "It is raining outside."),
    ("Зимой идёт снег.", "Zimoy idyot sneg.", "It snows in winter."),
    ("Весной цветут деревья.", "Vesnoy tsvetut derevya.", "Trees bloom in spring."),
    ("Летом очень жарко.", "Letom ochen zharko.", "It is very hot in summer."),
    ("Осенью листья желтеют.", "Osenyu listya zhelteyut.", "Leaves turn yellow in autumn."),
    ("На небе нет облаков.", "Na nebe net oblakov.", "There are no clouds in the sky."),
    ("Дует сильный ветер.", "Duyet silnyy veter.", "A strong wind is blowing."),
    ("После дождя появилась радуга.", "Posle dozhdya poyavilas raduga.", "A rainbow appeared after the rain."),
    ("В лесу растут грибы и ягоды.", "V lesu rastut griby i yagody.", "Mushrooms and berries grow in the forest."),
    ("В реке плавают рыбы.", "V reke plavayut ryby.", "Fish swim in the river."),
    ("На лугу пасутся коровы.", "Na lugu pasutsya korovy.", "Cows are grazing in the meadow."),
    ("Птицы поют утром.", "Ptitsy poyut utrom.", "Birds sing in the morning."),
    ("Медведь спит зимой в берлоге.", "Medved spit zimoy v berloge.", "The bear sleeps in winter in its den."),
    ("Заяц быстро бегает.", "Zayats bystro begayet.", "The hare runs fast."),
    ("В саду растут розы.", "V sadu rastut rozy.", "Roses grow in the garden."),
    ("Горы покрыты снегом.", "Gory pokryty snegom.", "The mountains are covered with snow."),
    ("Море спокойное сегодня.", "More spokoynoye sevodnya.", "The sea is calm today."),
    ("Какая красивая природа!", "Kakaya krasivaya priroda!", "What beautiful nature!"),
    ("Возьми зонт, будет дождь.", "Vozmi zont, budet dozhd.", "Take an umbrella, it will rain."),
]

ENTRIES.append({
    "key": "r17_nature",
    "name": "Russian Nature and Weather Sentences",
    "group": "Compounded",
    "ladder_rank": 5,
    "ladder_tier": "compounded",
    "description": (
        "Twenty sentences about animals, plants, the seasons, and weather "
        "talk - each in Russian with transliteration and English "
        "translation. Nature sentences drill the instrumental of season "
        "(зимой, весной, летом, осенью), impersonal weather verbs (идёт "
        "дождь, дует ветер), and location in the prepositional (в лесу, "
        "в реке, на лугу).\n" + _sent(SENT_17)
    ),
    "how_it_works": (
        "Seasons become adverbs in the instrumental: зимой, весной, летом, "
        "осенью - literally 'with winter', used to mean 'in winter'. "
        "Weather is impersonal: идёт дождь (rain goes), идёт снег, дует "
        "ветер - no subject, just the phenomenon. Nature locations take "
        "в/на + prepositional: в лесу, в реке, на лугу, в саду, на небе. "
        "Small talk about weather is the universal Russian opener, and "
        "the forecast formula is simple: будет дождь, будет холодно. "
        "Animals act with vivid verbs: плавают, пасутся, поют, спит."
    ),
    "key_points": [
        "20 nature and weather sentences with full translations.",
        "Seasons as instrumental adverbs: зимой, весной, летом, осенью.",
        "Weather is impersonal: идёт дождь, идёт снег, дует ветер.",
        "Nature places: в/на + prepositional (в лесу, на лугу).",
        "Forecast formula: будет + weather word.",
    ],
    "requirements": [
        "Give today's weather and tomorrow's forecast in Russian.",
        "Describe each season in 2 sentences.",
        "Name 10 animals and where they live.",
    ],
    "standards": [
        "Sentence patterns follow standard pedagogical models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method reads nature as the great sworn "
        "cycle: seasons take the instrumental as the year's four sworn "
        "companions, weather speaks impersonally as the sky's own voice, "
        "and every creature is named in its rightful place."
    ),
    "demo_key": "sentences",
    "demo_data": {"sentences": [list(s) for s in SENT_17], "topic": "nature and weather"},
})


# ---------------------------------------------------------------- record 18

SENT_18 = [
    ("Я иду в магазин за продуктами.", "Ya idu v magazin za produktami.", "I am going to the store for groceries."),
    ("Сколько стоит это платье?", "Skolko stoit eto platye?", "How much is this dress?"),
    ("Это слишком дорого для меня.", "Eto slishkom dorogo dlya menya.", "This is too expensive for me."),
    ("У вас есть размер побольше?", "U vas yest razmer pobolshe?", "Do you have a larger size?"),
    ("Можно примерить?", "Mozhno primerit?", "May I try it on?"),
    ("Где примерочная?", "Gde primerochnaya?", "Where is the fitting room?"),
    ("Мне нравится, я беру.", "Mne nravitsya, ya beru.", "I like it, I will take it."),
    ("Вы принимаете карты?", "Vy prinimayete karty?", "Do you accept cards?"),
    ("Я заплачу наличными.", "Ya zaplachu nalichnymi.", "I will pay in cash."),
    ("Дайте, пожалуйста, чек.", "Dayte, pozhaluysta, chek.", "Please give me the receipt."),
    ("Цены здесь низкие.", "Tseny zdes nizkiye.", "Prices are low here."),
    ("На рынке можно торговаться.", "Na rynke mozhno torgovatsya.", "You can bargain at the market."),
    ("Скидка - пятьдесят процентов.", "Skidka - pyatdesyat protsentov.", "The discount is fifty percent."),
    ("Распродажа начинается в понедельник.", "Rasprodazha nachinayetsya v ponedelnik.", "The sale starts on Monday."),
    ("Я купил подарок для мамы.", "Ya kupil podarok dlya mamy.", "I bought a gift for mom."),
    ("Магазин открыт до десяти вечера.", "Magazin otkryt do desyati vechera.", "The store is open until ten in the evening."),
    ("Очередь очень длинная.", "Ochered ochen dlinnaya.", "The line is very long."),
    ("Касса находится справа.", "Kassa nakhoditsya sprava.", "The checkout is on the right."),
    ("Я забыл кошелёк дома.", "Ya zabyl koshelek doma.", "I forgot my wallet at home."),
    ("Вернусь завтра за покупками.", "Vernus zavtra za pokupkami.", "I will come back for shopping tomorrow."),
]

ENTRIES.append({
    "key": "r18_shopping",
    "name": "Russian Shopping and Money Sentences",
    "group": "Compounded",
    "ladder_rank": 6,
    "ladder_tier": "compounded",
    "description": (
        "Twenty sentences about the market, prices, bargaining, and "
        "paying - each in Russian with transliteration and English "
        "translation. Shopping sentences drill the price question "
        "(сколько стоит), the genitive of price, and polite buying "
        "formulas with пожалуйста.\n" + _sent(SENT_18)
    ),
    "how_it_works": (
        "Prices are asked with сколько стоит + nominative and answered "
        "with стоит + accusative-number: Сколько стоит хлеб? - Пятьдесят "
        "рублей. The purpose of a trip takes за + instrumental: за "
        "продуктами, за покупками. Trying on is примерить; the fitting "
        "room is примерочная. Bargaining lives at the рынок (market), not "
        "in fixed-price stores: можно торговаться. Payment splits into "
        "наличными (in cash, instrumental plural) and картой (by card, "
        "instrumental singular). The receipt is чек, the checkout is "
        "касса, the line is очередь."
    ),
    "key_points": [
        "20 shopping sentences with full translations.",
        "Price: сколько стоит? answered with the amount in the right case.",
        "Purpose of trip: за + instrumental (за продуктами).",
        "Bargaining belongs to the рынок; stores have fixed prices.",
        "Payment: наличными (cash) vs картой (card); always ask for the чек.",
    ],
    "requirements": [
        "Buy 3 items in a role-play: ask price, bargain, pay, take receipt.",
        "Convert 5 prices between rubles and your currency aloud.",
        "Describe what you bought last week in 5 sentences.",
    ],
    "standards": [
        "Sentence patterns follow standard pedagogical models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method swears the marketplace as the hall "
        "of honest exchange: the price is asked openly, the bargain is "
        "struck as a covenant between buyer and seller, and the чек is "
        "the sworn record that the covenant was kept."
    ),
    "demo_key": "sentences",
    "demo_data": {"sentences": [list(s) for s in SENT_18], "topic": "shopping and money"},
})

# ---------------------------------------------------------------- record 19

SENT_19 = [
    ("Мы познакомились в университете.", "My poznakomilis v universitete.", "We met at the university."),
    ("Он мой лучший друг.", "On moy luchshiy drug.", "He is my best friend."),
    ("Мы дружим с детства.", "My druzhim s detstva.", "We have been friends since childhood."),
    ("Давай встретимся в субботу.", "Davay vstretimsya v subbotu.", "Let us meet on Saturday."),
    ("Приходи ко мне в гости.", "Prikhodi ko mne v gosti.", "Come visit me."),
    ("Мы пригласили друзей на ужин.", "My priglasili druzey na uzhin.", "We invited friends for dinner."),
    ("Спасибо за приглашение.", "Spasibo za priglasheniye.", "Thanks for the invitation."),
    ("С днём рождения!", "S dnyom rozhdeniya!", "Happy birthday!"),
    ("Желаю счастья и здоровья.", "Zhelayu schastya i zdorovya.", "I wish you happiness and health."),
    ("Давай выпьем за дружбу.", "Davay vypyem za druzhbu.", "Let us drink to friendship."),
    ("Мы весело провели время.", "My veselo proveli vremya.", "We had a fun time."),
    ("Расскажи о себе.", "Rasskazhi o sebe.", "Tell me about yourself."),
    ("Чем ты увлекаешься?", "Chem ty uvlekayeshsya?", "What are your hobbies?"),
    ("Я люблю читать и гулять.", "Ya lyublyu chitat i gulyat.", "I like reading and walking."),
    ("У нас много общего.", "U nas mnogo obshchego.", "We have a lot in common."),
    ("Не пропадай, звони.", "Ne propaday, zvoni.", "Do not disappear, call."),
    ("Я всегда рад тебя видеть.", "Ya vsegda rad tebya videt.", "I am always glad to see you."),
    ("Ты настоящий друг.", "Ty nastoyashchiy drug.", "You are a true friend."),
    ("Друзья познаются в беде.", "Druzya poznayutsya v bede.", "Friends are known in trouble."),
    ("До скорой встречи!", "Do skoroy vstrechi!", "See you soon!"),
]

ENTRIES.append({
    "key": "r19_friendship",
    "name": "Russian Friendship and Social Life Sentences",
    "group": "Compounded",
    "ladder_rank": 6,
    "ladder_tier": "compounded",
    "description": (
        "Twenty sentences about meeting people, invitations, and "
        "celebrations - each in Russian with transliteration and English "
        "translation. Friendship sentences drill reflexive meeting verbs "
        "(познакомиться, встретиться, дружить), invitation formulas "
        "(приходи в гости, давай встретимся), and celebration wishes "
        "(с днём рождения, желаю счастья).\n" + _sent(SENT_19)
    ),
    "how_it_works": (
        "Meeting is reflexive: познакомиться (to get acquainted), "
        "встретиться (to meet up) - the -ся marks mutual action. "
        "Invitations use the informal imperative + в гости: приходи ко "
        "мне в гости. Suggestions use давай + future: давай встретимся, "
        "давай выпьем. Wishes take the accusative of the wish: желаю "
        "счастья и здоровья; the birthday formula is с + instrumental: с "
        "днём рождения. Friendship duration uses с + genitive: дружим с "
        "детства (since childhood). The proverb Друзья познаются в беде "
        "shows how fixed sayings carry cultural weight."
    ),
    "key_points": [
        "20 friendship sentences with full translations.",
        "Meeting verbs are reflexive: познакомиться, встретиться.",
        "Invitations: приходи в гости; suggestions: давай + future.",
        "Wishes: желаю + genitive; С днём рождения! with instrumental.",
        "Duration of friendship: с + genitive (с детства).",
    ],
    "requirements": [
        "Introduce yourself and make a friend in a role-play.",
        "Invite someone to dinner and accept/decline politely.",
        "Write 3 celebration wishes in Russian.",
    ],
    "standards": [
        "Sentence patterns follow standard pedagogical models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method swears friendship as a mutual "
        "covenant: the reflexive -ся binds both sides of every meeting, "
        "invitations are sworn in the imperative of welcome, and wishes "
        "are sworn in the genitive - the case of giving."
    ),
    "demo_key": "sentences",
    "demo_data": {"sentences": [list(s) for s in SENT_19], "topic": "friendship and social life"},
})

# ---------------------------------------------------------------- record 20

SENT_20 = [
    ("У меня новый телефон.", "U menya novyy telefon.", "I have a new phone."),
    ("Позвони мне вечером.", "Pozvoni mne vecherom.", "Call me in the evening."),
    ("Я не слышу тебя, перезвони.", "Ya ne slyshu tebya, perezvoni.", "I cannot hear you, call back."),
    ("Отправь мне сообщение.", "Otprav mne soobshcheniye.", "Send me a message."),
    ("Я получил твоё письмо.", "Ya poluchil tvoyo pismo.", "I received your letter."),
    ("Проверь электронную почту.", "Prover elektronnuyu pochtu.", "Check your email."),
    ("Мой компьютер не работает.", "Moy kompyuter ne rabotayet.", "My computer is not working."),
    ("Перезагрузи компьютер.", "Perezagruzi kompyuter.", "Restart the computer."),
    ("Подключись к интернету.", "Podklyuchis k internetu.", "Connect to the internet."),
    ("Какой у тебя пароль?", "Kakoy u tebya parol?", "What is your password?"),
    ("Я забыл пароль.", "Ya zabyl parol.", "I forgot the password."),
    ("Скачай это приложение.", "Skachay eto prilozheniye.", "Download this app."),
    ("Открой файл, пожалуйста.", "Otkroy fayl, pozhaluysta.", "Open the file, please."),
    ("Сохрани документ.", "Sokhrani dokument.", "Save the document."),
    ("Я ищу информацию в интернете.", "Ya ishchu informatsiyu v internete.", "I am searching for information online."),
    ("Этот сайт очень полезный.", "Etot sayt ochen poleznyy.", "This website is very useful."),
    ("Давай поговорим по видео.", "Davay pogovorim po video.", "Let us talk by video."),
    ("Камера не работает.", "Kamera ne rabotayet.", "The camera is not working."),
    ("Включи микрофон.", "Vklyuchi mikrofon.", "Turn on the microphone."),
    ("Выключи звук, пожалуйста.", "Vyklyuchi zvuk, pozhaluysta.", "Mute the sound, please."),
]

ENTRIES.append({
    "key": "r20_technology",
    "name": "Russian Technology and Communication Sentences",
    "group": "Compounded",
    "ladder_rank": 6,
    "ladder_tier": "compounded",
    "description": (
        "Twenty sentences about the phone, the internet, the computer, "
        "and messaging - each in Russian with transliteration and English "
        "translation. Technology sentences drill modern vocabulary "
        "(телефон, интернет, приложение, пароль), tech imperatives "
        "(позвони, перезагрузи, скачай, сохрани), and digital-life "
        "formulas.\n" + _sent(SENT_20)
    ),
    "how_it_works": (
        "Tech Russian borrows freely: телефон, компьютер, интернет, сайт, "
        "файл, пароль - all international words with Russian endings. "
        "Digital actions use perfective imperatives for single tasks: "
        "позвони, отправь, скачай, сохрани, перезагрузи. Connection is "
        "подключиться к + dative (к интернету); searching is искать в + "
        "prepositional (в интернете). Video calls run on по + dative: "
        "поговорим по видео. The phone itself is often just трубка in "
        "call formulas: возьми трубку (pick up), положи трубку (hang up)."
    ),
    "key_points": [
        "20 technology sentences with full translations.",
        "Core digital vocabulary: телефон, компьютер, интернет, приложение, пароль, файл.",
        "Tech tasks use perfective imperatives: позвони, скачай, сохрани.",
        "Connect: подключиться к + dative; search: искать в + prepositional.",
        "Video: поговорить по видео; mute: выключи звук.",
    ],
    "requirements": [
        "Give 5 tech instructions in Russian (turn on, connect, download, save, restart).",
        "Describe your phone and computer in 5 sentences.",
        "Role-play a call with bad connection.",
    ],
    "standards": [
        "Vocabulary follows current standard usage.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method wires the modern world into the "
        "ancient oath-system: borrowed words take Russian endings as "
        "sworn citizens, digital commands strike in the perfective - one "
        "oath, one completed act - and connection itself is sworn with к "
        "plus the dative, the case of joining."
    ),
    "demo_key": "sentences",
    "demo_data": {"sentences": [list(s) for s in SENT_20], "topic": "technology and communication"},
})

# ---------------------------------------------------------------- record 21

TENSE_21 = {
    "present": [
        ("Я читаю книгу.", "Ya chitayu knigu.", "I read / I am reading a book."),
        ("Ты пишешь письмо.", "Ty pishesh pismo.", "You write / are writing a letter."),
        ("Он работает в офисе.", "On rabotayet v ofise.", "He works / is working in an office."),
        ("Мы учим русский язык.", "My uchim russkiy yazyk.", "We learn / are learning Russian."),
        ("Они смотрят телевизор.", "Oni smotryat televizor.", "They watch / are watching TV."),
    ],
    "past": [
        ("Я читал вчера.", "Ya chital vchera.", "I read (masc.) yesterday."),
        ("Она написала письмо.", "Ona napisala pismo.", "She wrote (fem.) a letter."),
        ("Мы гуляли в парке.", "My gulyali v parke.", "We walked (pl.) in the park."),
        ("Они смотрели фильм.", "Oni smotreli film.", "They watched (pl.) a movie."),
        ("Дети играли во дворе.", "Deti igrali vo dvore.", "The children played (pl.) in the yard."),
    ],
    "future": [
        ("Я буду читать завтра.", "Ya budu chitat zavtra.", "I will read tomorrow."),
        ("Ты напишешь письмо.", "Ty napishesh pismo.", "You will write a letter."),
        ("Он будет работать.", "On budet rabotat.", "He will work."),
        ("Мы пойдём в кино.", "My poydyom v kino.", "We will go to the cinema."),
        ("Они приедут в пятницу.", "Oni priyedut v pyatnitsu.", "They will arrive on Friday."),
    ],
    "aspect_pairs": [
        ("читать", "прочитать", "to read"),
        ("писать", "написать", "to write"),
        ("делать", "сделать", "to do"),
        ("говорить", "сказать", "to speak / to say"),
        ("брать", "взять", "to take"),
    ],
}

ENTRIES.append({
    "key": "r21_tenses",
    "name": "Russian Verb Tenses in Sentences",
    "group": "Compounded",
    "ladder_rank": 6,
    "ladder_tier": "compounded",
    "description": (
        "The Russian verb system in sentences: present, past, and future, "
        "with five translated sentences per tense, plus the aspect pairs "
        "that are the true heart of Russian verbs. The present covers "
        "both 'I read' and 'I am reading'. The past agrees with the "
        "subject in gender and number (читал/читала/читало/читали). The "
        "future has two forms: imperfective буду + infinitive for ongoing "
        "future action, perfective single-word future (напишу, пойду) for "
        "completed future acts.\nPresent tense:\n" + _sent(TENSE_21["present"]) +
        "\nPast tense:\n" + _sent(TENSE_21["past"]) +
        "\nFuture tense:\n" + _sent(TENSE_21["future"]) +
        "\nAspect pairs (imperfective - perfective):\n" +
        "\n".join("%d. %s - %s (%s)" % (i + 1, imp, pf, en)
                  for i, (imp, pf, en) in enumerate(TENSE_21["aspect_pairs"]))
    ),
    "how_it_works": (
        "Russian has only three tenses but two aspects, and aspect does "
        "the work English spreads across many tenses. The imperfective "
        "describes ongoing, repeated, or general action: я читал means 'I "
        "was reading / I used to read'. The perfective describes a single "
        "completed act: я прочитал means 'I read it through'. In the past, "
        "the verb drops person endings and agrees like an adjective: "
        "masculine -л, feminine -ла, neuter -ло, plural -ли. In the future, "
        "imperfective verbs need the helper буду (буду читать), while "
        "perfective verbs conjugate directly in a future meaning "
        "(прочитаю - I will read through). Choosing aspect correctly is "
        "the single biggest leap from intermediate to fluent."
    ),
    "key_points": [
        "Three tenses, two aspects: aspect carries the meaning English spreads across many tenses.",
        "Present covers simple and continuous; past agrees in gender/number (-л/-ла/-ло/-ли).",
        "Future: imperfective буду + infinitive vs perfective single-word future (напишу).",
        "Imperfective = ongoing/repeated; perfective = single completed act.",
        "Five aspect pairs anchor the system: читать/прочитать, писать/написать, делать/сделать, говорить/сказать, брать/взять.",
    ],
    "requirements": [
        "Conjugate one verb in all three tenses aloud.",
        "Convert 5 imperfective sentences to perfective and explain the meaning change.",
        "Drill past-tense gender agreement with 10 subjects.",
    ],
    "standards": [
        "Tense and aspect analysis follows the standard description in the cited grammars.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method swears every verb two faces: the "
        "imperfective face that labors on without end, and the perfective "
        "face that strikes once and is done. Three tenses are the three "
        "fields of time, but aspect is the oath that decides what the "
        "action truly was."
    ),
    "demo_key": "tenses",
    "demo_data": {
        "past_endings": {"masculine": "л", "feminine": "ла", "neuter": "ло", "plural": "ли"},
        "stem": "чита",
        "aspect_pairs": [[a, b] for a, b, c in TENSE_21["aspect_pairs"]],
        "future_aux": ["буду", "будешь", "будет", "будем", "будете", "будут"],
    },
})

# ---------------------------------------------------------------- record 22

QA_22 = [
    ("Кто это?", "Kto eto?", "Who is this?", "Это мой друг Иван.", "Eto moy drug Ivan.", "This is my friend Ivan."),
    ("Что это?", "Chto eto?", "What is this?", "Это книга.", "Eto kniga.", "This is a book."),
    ("Где ты живёшь?", "Gde ty zhivyosh?", "Where do you live?", "Я живу в Москве.", "Ya zhivu v Moskve.", "I live in Moscow."),
    ("Куда ты идёшь?", "Kuda ty idyosh?", "Where are you going?", "Я иду в магазин.", "Ya idu v magazin.", "I am going to the store."),
    ("Когда начинается урок?", "Kogda nachinayetsya urok?", "When does the lesson start?", "Урок начинается в девять.", "Urok nachinayetsya v devyat.", "The lesson starts at nine."),
    ("Почему ты опоздал?", "Pochemu ty opozdal?", "Why are you late?", "Я опоздал, потому что была пробка.", "Ya opozdal, potomu chto byla probka.", "I am late because there was a traffic jam."),
    ("Как тебя зовут?", "Kak tebya zovut?", "What is your name?", "Меня зовут Анна.", "Menya zovut Anna.", "My name is Anna."),
    ("Сколько тебе лет?", "Skolko tebe let?", "How old are you?", "Мне двадцать лет.", "Mne dvadtsat let.", "I am twenty."),
    ("Какой твой любимый цвет?", "Kakoy tvoy lyubimyy tsvet?", "What is your favorite color?", "Мой любимый цвет - синий.", "Moy lyubimyy tsvet - siniy.", "My favorite color is blue."),
    ("Чей это портфель?", "Chey eto portfel?", "Whose briefcase is this?", "Это портфель учителя.", "Eto portfel uchitelya.", "This is the teacher's briefcase."),
    ("Сколько стоит хлеб?", "Skolko stoit khleb?", "How much is the bread?", "Хлеб стоит пятьдесят рублей.", "Khleb stoit pyatdesyat rubley.", "The bread costs fifty rubles."),
    ("Который час?", "Kotoryy chas?", "What time is it?", "Сейчас половина второго.", "Seychas polovina vtorogo.", "It is half past one."),
    ("Ты говоришь по-русски?", "Ty govorish po-russki?", "Do you speak Russian?", "Да, я говорю по-русски.", "Da, ya govoryu po-russki.", "Yes, I speak Russian."),
    ("Где находится вокзал?", "Gde nakhoditsya vokzal?", "Where is the station?", "Вокзал находится рядом с парком.", "Vokzal nakhoditsya ryadom s parkom.", "The station is next to the park."),
    ("Что ты делаешь вечером?", "Chto ty delayesh vecherom?", "What are you doing tonight?", "Вечером я читаю книгу.", "Vecherom ya chitayu knigu.", "Tonight I am reading a book."),
    ("Как пройти к музею?", "Kak proyti k muzeyu?", "How do I get to the museum?", "Идите прямо, потом налево.", "Idite pryamo, potom nalevo.", "Go straight, then left."),
    ("Ты любишь зиму?", "Ty lyubish zimu?", "Do you like winter?", "Да, я люблю зиму и снег.", "Da, ya lyublyu zimu i sneg.", "Yes, I like winter and snow."),
    ("Когда твой день рождения?", "Kogda tvoy den rozhdeniya?", "When is your birthday?", "Мой день рождения в мае.", "Moy den rozhdeniya v maye.", "My birthday is in May."),
    ("Почему ты учишь русский язык?", "Pochemu ty uchish russkiy yazyk?", "Why are you learning Russian?", "Я учу русский, потому что он мне нравится.", "Ya uchu russkiy, potomu chto on mne nravitsya.", "I am learning Russian because I like it."),
    ("Как дела на работе?", "Kak dela na rabote?", "How are things at work?", "Всё отлично, спасибо!", "Vsyo otlichno, spasibo!", "Everything is great, thanks!"),
]

ENTRIES.append({
    "key": "r22_qa",
    "name": "Russian Questions and Answers",
    "group": "Advanced",
    "ladder_rank": 7,
    "ladder_tier": "advanced",
    "description": (
        "Twenty question-and-answer pairs covering who, what, where, when, "
        "why, and how - each question in Russian with transliteration and "
        "translation, each answer the same. The pairs model the core "
        "question words: кто, что, где, куда, когда, почему, как, сколько, "
        "какой, чей, который.\n" +
        "\n".join("%d. Q: %s (%s - %s)  A: %s (%s - %s)" % (
            i + 1, q, qt, qe, a, at, ae)
            for i, (q, qt, qe, a, at, ae) in enumerate(QA_22))
    ),
    "how_it_works": (
        "Russian questions need no word-order change: Где ты живёшь? keeps "
        "subject-verb order and asks by intonation plus the question word. "
        "Кто asks about people; что asks about things. Где asks location "
        "(prepositional answer: в Москве), куда asks destination "
        "(accusative answer: в магазин), откуда asks origin. Почему takes "
        "потому что in the answer. Сколько governs the genitive plural "
        "in the answer: пятьдесят рублей, двадцать лет. Yes/no questions "
        "are answered by repeating the verb: Ты говоришь по-русски? - Да, "
        "говорю."
    ),
    "key_points": [
        "20 question/answer pairs covering all core question words.",
        "No inversion: word order stays SVO; intonation + question word asks the question.",
        "Кто for people, что for things; где location, куда destination, откуда origin.",
        "Почему answered with потому что; сколько answered with genitive plural.",
        "Yes/no answers repeat the verb: Да, говорю.",
    ],
    "requirements": [
        "Ask and answer all 20 pairs with a partner, swapping roles.",
        "Convert 5 statements into questions three ways: intonation, question word, ли.",
        "Interview someone in Russian using all question words.",
    ],
    "standards": [
        "Question formation follows the standard description in the cited grammars.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method treats every question as a sworn "
        "inquiry with its proper key: кто unlocks persons, что unlocks "
        "things, где unlocks places, когда unlocks times, почему unlocks "
        "reasons. The answer is the oath sworn back in matching form."
    ),
    "demo_key": "qa",
    "demo_data": {"pairs": [[q, a] for q, qt, qe, a, at, ae in QA_22],
                  "question_words": ["кто", "что", "где", "куда", "когда",
                                     "почему", "как", "сколько", "какой", "чей"]},
})

# ---------------------------------------------------------------- record 23

CMD_23 = [
    ("говорить", "govorit", "to speak", "Говори!", "Govori!", "Speak! (informal)", "Говорите!", "Govorite!", "Speak! (formal)"),
    ("идти", "idti", "to go", "Иди!", "Idi!", "Go! (informal)", "Идите!", "Idite!", "Go! (formal)"),
    ("садиться", "saditsya", "to sit down", "Садись!", "Sadis!", "Sit down! (informal)", "Садитесь!", "Sadites!", "Sit down! (formal)"),
    ("ждать", "zhdat", "to wait", "Подожди!", "Podozhdi!", "Wait! (informal)", "Подождите!", "Podozhdite!", "Wait! (formal)"),
    ("помогать", "pomogat", "to help", "Помоги!", "Pomogi!", "Help! (informal)", "Помогите!", "Pomogite!", "Help! (formal)"),
    ("давать", "davat", "to give", "Дай!", "Day!", "Give! (informal)", "Дайте!", "Dayte!", "Give! (formal)"),
    ("сказать", "skazat", "to say", "Скажи!", "Skazhi!", "Say! (informal)", "Скажите!", "Skazhite!", "Say! (formal)"),
    ("звонить", "zvonit", "to call", "Позвони!", "Pozvoni!", "Call! (informal)", "Позвоните!", "Pozvonite!", "Call! (formal)"),
    ("открывать", "otkryvat", "to open", "Открой!", "Otkroy!", "Open! (informal)", "Откройте!", "Otkroyte!", "Open! (formal)"),
    ("покупать", "pokupat", "to buy", "Купи!", "Kupi!", "Buy! (informal)", "Купите!", "Kupite!", "Buy! (formal)"),
    ("читать", "chitat", "to read", "Читай!", "Chitay!", "Read! (informal)", "Читайте!", "Chitayte!", "Read! (formal)"),
    ("писать", "pisat", "to write", "Пиши!", "Pishi!", "Write! (informal)", "Пишите!", "Pishite!", "Write! (formal)"),
    ("слушать", "slushat", "to listen", "Слушай!", "Slushay!", "Listen! (informal)", "Слушайте!", "Slushayte!", "Listen! (formal)"),
    ("смотреть", "smotret", "to look", "Смотри!", "Smotri!", "Look! (informal)", "Смотрите!", "Smotrite!", "Look! (formal)"),
    ("есть", "yest", "to eat", "Ешь!", "Yesh!", "Eat! (informal)", "Ешьте!", "Yeshte!", "Eat! (formal)"),
    ("пить", "pit", "to drink", "Пей!", "Pey!", "Drink! (informal)", "Пейте!", "Peyte!", "Drink! (formal)"),
    ("спать", "spat", "to sleep", "Спи!", "Spi!", "Sleep! (informal)", "Спите!", "Spite!", "Sleep! (formal)"),
    ("делать", "delat", "to do", "Делай!", "Delay!", "Do! (informal)", "Делайте!", "Delayte!", "Do! (formal)"),
    ("стоять", "stoyat", "to stand", "Стой!", "Stoy!", "Stand! (informal)", "Стойте!", "Stoyte!", "Stand! (formal)"),
    ("молчать", "molchat", "to be silent", "Молчи!", "Molchi!", "Be quiet! (informal)", "Молчите!", "Molchite!", "Be quiet! (formal)"),
]

ENTRIES.append({
    "key": "r23_commands",
    "name": "Russian Commands and Requests",
    "group": "Advanced",
    "ladder_rank": 7,
    "ladder_tier": "advanced",
    "description": (
        "Twenty imperative verbs in informal (ты) and formal (вы) forms - "
        "each with the infinitive, transliteration, meaning, and both "
        "command forms translated. The informal imperative addresses one "
        "friend; the formal addresses strangers, elders, or groups. Soft "
        "requests add пожалуйста; prohibitions use не + imperfective "
        "imperative (не говори - do not speak).\n" +
        "\n".join(
            "%d. %s (%s - %s): %s (%s - %s) / %s (%s - %s)" % (
                i + 1, inf, inftr, infen, ty, tytr, tyen, vy, vytr, vyen)
            for i, (inf, inftr, infen, ty, tytr, tyen, vy, vytr, vyen)
            in enumerate(CMD_23))
    ),
    "how_it_works": (
        "The imperative is built from the present-tense stem: verbs "
        "usually add -й after a vowel (читай, делай) or -и after a "
        "consonant (пиши, молчи, говори, смотри). The formal/plural "
        "simply adds -те: говори - говорите, иди - идите. A handful of "
        "verbs are irregular and must be memorized: дай/дайте, ешь/ешьте. "
        "Polite requests prefer softeners with пожалуйста, while true "
        "commands use the bare imperative. Negative commands use the "
        "imperfective: не кури (do not smoke)."
    ),
    "key_points": [
        "20 imperatives in ты and вы forms with translations.",
        "Informal imperative from the present stem: читай, говори, пиши.",
        "Formal/plural adds -те: говорите, идите, подождите.",
        "Irregulars to memorize: дай/дайте, ешь/ешьте.",
        "Soft requests add пожалуйста; prohibitions: не + imperfective.",
    ],
    "requirements": [
        "Give 10 commands to a friend (ты) and the same 10 formally (вы).",
        "Soften 5 commands into polite requests with пожалуйста.",
        "Memorize the irregular imperatives.",
    ],
    "standards": [
        "Imperative formation follows the standard description in the cited grammars.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "In the Signature Russian Method the imperative is the sworn "
        "command voice: to kin it speaks short and direct, to strangers "
        "it adds the -те of respect. Every command here is a covenant "
        "between speaker and doer - the verb itself swears the action."
    ),
    "demo_key": "imperative",
    "demo_data": {"pairs": [[ty, vy] for inf, inftr, infen, ty, tytr, tyen, vy, vytr, vyen in CMD_23]},
})

# ---------------------------------------------------------------- record 24

SENT_24 = [
    ("Моя бабушка - добрая пожилая женщина с тёплой улыбкой.", "Moya babushka - dobraya pozhilaya zhenshchina s tyoploy ulybkoy.", "My grandmother is a kind elderly woman with a warm smile."),
    ("У неё седые волосы и добрые голубые глаза.", "U neyo sedyye volosy i dobryye golubyye glaza.", "She has gray hair and kind blue eyes."),
    ("Наш дом - двухэтажный, с большим садом вокруг.", "Nash dom - dukhetazhnyy, s bolshim sadom vokrug.", "Our house has two floors, with a big garden around it."),
    ("В гостиной стоит старый диван и книжный шкаф.", "V gostinoy stoit staryy divan i knizhnyy shkaf.", "In the living room there is an old sofa and a bookcase."),
    ("Москва - огромный город с богатой историей.", "Moskva - ogromnyy gorod s bogatoy istoriyey.", "Moscow is a huge city with a rich history."),
    ("Красная площадь - самая известная площадь страны.", "Krasnaya ploshchad - samaya izvestnaya ploshchad strany.", "Red Square is the most famous square in the country."),
    ("Зимний лес тихий и загадочный.", "Zimniy les tikhiy i zagadochnyy.", "The winter forest is quiet and mysterious."),
    ("Снег блестит на солнце, как тысячи алмазов.", "Sneg blestit na solntse, kak tysyachi almazov.", "The snow glitters in the sun like thousands of diamonds."),
    ("Мой друг - высокий спортивный парень с чувством юмора.", "Moy drug - vysokiy sportivnyy paren s chuvstvom yumora.", "My friend is a tall athletic guy with a sense of humor."),
    ("Он всегда носит джинсы и красную куртку.", "On vsegda nosit dzhinsy i krasnuyu kurtku.", "He always wears jeans and a red jacket."),
    ("Эта книга - толстый роман с интересным сюжетом.", "Eta kniga - tolstyy roman s interesnym syuzhetom.", "This book is a thick novel with an interesting plot."),
    ("Её страницы пахнут типографской краской.", "Yeyo stranitsy pakhnut tipografskoy kraskoy.", "Its pages smell of printer's ink."),
    ("Наш кот - пушистый рыжий хитрец.", "Nash kot - pushistyy ryzhiy khitrets.", "Our cat is a fluffy ginger trickster."),
    ("Он любит спать на тёплой батарее.", "On lyubit spat na tyoploy batareye.", "He likes to sleep on the warm radiator."),
    ("Волга - самая длинная река Европы.", "Volga - samaya dlinnaya reka Yevropy.", "The Volga is the longest river in Europe."),
    ("Её берега покрыты зелёными лесами.", "Yeyo berega pokryty zelyonymi lesami.", "Its banks are covered with green forests."),
    ("Учительница - строгая, но справедливая женщина.", "Uchitelnitsa - strogaya, no spravedlivaya zhenshchina.", "The teacher is a strict but fair woman."),
    ("Её уроки всегда интересные и понятные.", "Yeyo uroki vsegda interesnyye i ponyatnyye.", "Her lessons are always interesting and clear."),
    ("Старый парк в центре города - моё любимое место.", "Staryy park v tsentre goroda - moyo lyubimoye mesto.", "The old park downtown is my favorite place."),
    ("Там тихо, зелено и пахнет цветами.", "Tam tikho, zeleno i pakhnet tsvetami.", "It is quiet and green there, and smells of flowers."),
]

ENTRIES.append({
    "key": "r24_descriptions",
    "name": "Russian Descriptions - People and Places",
    "group": "Advanced",
    "ladder_rank": 7,
    "ladder_tier": "advanced",
    "description": (
        "Twenty sentences describing people, places, and things in "
        "detail - each in Russian with transliteration and English "
        "translation. Description sentences drill stacked adjectives "
        "(добрая пожилая женщина), the instrumental of accompaniment "
        "(с тёплой улыбкой, с чувством юмора), superlatives (самая "
        "известная, самая длинная), and sensory verbs (пахнет, блестит).\n"
        + _sent(SENT_24)
    ),
    "how_it_works": (
        "Detailed description stacks adjectives before the noun, all in "
        "agreement: добрая пожилая женщина (kind elderly woman). "
        "Accompanying features take с + instrumental: с тёплой улыбкой, "
        "с богатой историей, с чувством юмора. Superlatives use самый + "
        "adjective: самая известная площадь, самая длинная река. Sensory "
        "description uses impersonal verbs: пахнет цветами (it smells of "
        "flowers), там тихо (it is quiet there). The dash construction X "
        "- Y (Волга - самая длинная река) is the workhorse of definition "
        "and description."
    ),
    "key_points": [
        "20 descriptive sentences with full translations.",
        "Stacked adjectives in agreement: добрая пожилая женщина.",
        "Accompaniment: с + instrumental (с тёплой улыбкой).",
        "Superlatives: самый + adjective (самая длинная река).",
        "Sensory impersonals: пахнет, там тихо; definition dash: X - Y.",
    ],
    "requirements": [
        "Describe 3 people and 3 places in 5 sentences each.",
        "Write a 10-sentence portrait of your hometown.",
        "Practice superlatives with 10 adjectives.",
    ],
    "standards": [
        "Sentence patterns follow standard pedagogical models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method paints in sworn colors: adjectives "
        "march in matching agreement before their noun, accompaniments "
        "are bound with the instrumental oath, and the superlative raises "
        "its subject above all others as the sworn finest."
    ),
    "demo_key": "sentences",
    "demo_data": {"sentences": [list(s) for s in SENT_24], "topic": "descriptions of people and places"},
})

# ---------------------------------------------------------------- record 25

STORY_25 = [
    ("Утром Анна просыпается рано.", "Utrom Anna prosypayetsya rano.", "In the morning Anna wakes up early."),
    ("Она умывается и завтракает.", "Ona umyvayetsya i zavtrakayet.", "She washes up and has breakfast."),
    ("Потом она идёт в школу.", "Potom ona idyot v shkolu.", "Then she goes to school."),
    ("В школе она учит русский язык.", "V shkole ona uchit russkiy yazyk.", "At school she studies Russian."),
    ("Учительница читает интересный рассказ.", "Uchitelnitsa chitayet interesnyy rasskaz.", "The teacher reads an interesting story."),
    ("Дети слушают внимательно.", "Deti slushayut vnimatelno.", "The children listen attentively."),
    ("После уроков Анна гуляет с подругой.", "Posle urokov Anna gulyayet s podrugoy.", "After lessons Anna walks with her friend."),
    ("Они разговаривают и смеются.", "Oni razgovarivayut i smeyutsya.", "They talk and laugh."),
    ("Вечером Анна делает уроки.", "Vecherom Anna delayet uroki.", "In the evening Anna does her homework."),
    ("Потом она ложится спать.", "Potom ona lozhitsya spat.", "Then she goes to bed."),
]

ENTRIES.append({
    "key": "r25_story1",
    "name": "Russian Story I - A Simple Story",
    "group": "Advanced",
    "ladder_rank": 8,
    "ladder_tier": "advanced",
    "description": (
        "A ten-sentence simple story in Russian, told in the present "
        "tense, with line-by-line English translation. Follow Anna "
        "through her day - morning, school, walk with a friend, evening - "
        "and see the present tense, reflexive verbs, and time words "
        "(утром, потом, вечером) working in a connected narrative.\n"
        + _sent(STORY_25)
    ),
    "how_it_works": (
        "A simple narrative chains present-tense verbs in time order: "
        "утром ... потом ... вечером. Reflexive verbs carry the daily "
        "routine: просыпается, умывается, ложится. Time words open the "
        "sentences and sequence the story without any conjunctions. "
        "Because the present tense covers habitual action, the whole "
        "story reads as 'what Anna does every day'. Read it aloud three "
        "times: first for meaning, second tracking every verb ending, "
        "third retelling it without looking."
    ),
    "key_points": [
        "10-sentence present-tense story with line-by-line translation.",
        "Narrative sequencing with time words: утром, потом, вечером.",
        "Daily-routine reflexive verbs: просыпается, умывается, ложится.",
        "Present tense as habitual: the story describes every day.",
    ],
    "requirements": [
        "Retell Anna's day from memory in Russian.",
        "Write your own 10-sentence day in the present tense.",
        "Identify every reflexive verb and its infinitive.",
    ],
    "standards": [
        "Narrative follows standard pedagogical story models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method tells the day as a sworn chain: "
        "each hour linked to the next by time-words, each routine act "
        "sealed with the reflexive oath. The present tense is the eternal "
        "day - always happening, always true."
    ),
    "demo_key": "story",
    "demo_data": {"lines": [list(s) for s in STORY_25], "tense": "present"},
})

# ---------------------------------------------------------------- record 26

STORY_26 = [
    ("Вчера был тёплый осенний день.", "Vchera byl tyoplyy osenniy den.", "Yesterday was a warm autumn day."),
    ("Иван пошёл в парк.", "Ivan poshyol v park.", "Ivan went to the park."),
    ("Он взял с собой книгу.", "On vzyal s soboy knigu.", "He took a book with him."),
    ("В парке он сел на скамейку.", "V parke on sel na skameyku.", "In the park he sat on a bench."),
    ("Он читал книгу два часа.", "On chital knigu dva chasa.", "He read the book for two hours."),
    ("Потом он встретил старого друга.", "Potom on vstretil starogo druga.", "Then he met an old friend."),
    ("Они долго разговаривали.", "Oni dolgo razgovarivali.", "They talked for a long time."),
    ("Друг рассказал интересную историю.", "Drug rasskazal interesnuyu istoriyu.", "The friend told an interesting story."),
    ("Вечером Иван вернулся домой.", "Vecherom Ivan vernulsya domoy.", "In the evening Ivan returned home."),
    ("Он был очень доволен днём.", "On byl ochen dovolen dnyom.", "He was very pleased with the day."),
]

ENTRIES.append({
    "key": "r26_story2",
    "name": "Russian Story II - A Story in the Past",
    "group": "Advanced",
    "ladder_rank": 8,
    "ladder_tier": "advanced",
    "description": (
        "A ten-sentence story using past-tense forms, with line-by-line "
        "English translation. Follow Ivan's autumn day in the park and "
        "watch aspect at work: imperfective читал for the two hours of "
        "reading, perfective встретил and рассказал for the single "
        "completed events.\n" + _sent(STORY_26)
    ),
    "how_it_works": (
        "Past-tense narrative shows aspect in its natural habitat. "
        "Ongoing background actions take the imperfective: читал (was "
        "reading), разговаривали (were talking). Single completed events "
        "take the perfective: пошёл (went), взял (took), встретил (met), "
        "рассказал (told), вернулся (returned). The past endings agree "
        "with the subject: Иван пошёл (masc.), книга - она взяла would be "
        "feminine. Time expressions anchor the past: вчера, два часа, "
        "вечером. Notice how the story needs no 'was -ing' helper - "
        "aspect alone carries it."
    ),
    "key_points": [
        "10-sentence past-tense story with line-by-line translation.",
        "Aspect in narrative: imperfective for background, perfective for events.",
        "Past endings agree with the subject: пошёл, взяла, разговаривали.",
        "Time anchors: вчера, два часа, потом, вечером.",
    ],
    "requirements": [
        "Retell Ivan's day from memory in the past tense.",
        "Mark every verb imperfective or perfective and explain why.",
        "Write your yesterday in 10 past-tense sentences.",
    ],
    "standards": [
        "Narrative follows standard pedagogical story models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method walks the past as a sworn road: "
        "imperfective verbs are the long stretches of the journey, "
        "perfective verbs the milestones struck once. The traveler's "
        "gender is sworn on every verb-ending, and time-words are the "
        "signposts."
    ),
    "demo_key": "story",
    "demo_data": {"lines": [list(s) for s in STORY_26], "tense": "past"},
})

# ---------------------------------------------------------------- record 27

STORY_27 = [
    ("Завтра будет солнечный день.", "Zavtra budet solnechnyy den.", "Tomorrow will be a sunny day."),
    ("Мы поедем на дачу.", "My poyedem na dachu.", "We will go to the country house."),
    ("Мама приготовит вкусный обед.", "Mama prigotovit vkusnyy obed.", "Mother will cook a tasty lunch."),
    ("Папа будет работать в саду.", "Papa budet rabotat v sadu.", "Father will work in the garden."),
    ("Дети будут играть на улице.", "Deti budut igrat na ulitse.", "The children will play outside."),
    ("Если будет дождь, мы останемся дома.", "Yesli budet dozhd, my ostanemsya doma.", "If it rains, we will stay home."),
    ("Тогда мы будем читать книги.", "Togda my budem chitat knigi.", "Then we will read books."),
    ("Я бы хотел поехать на речку.", "Ya by khotel poyekhat na rechku.", "I would like to go to the river."),
    ("Может быть, мы пойдём туда после обеда.", "Mozhet byt, my poydyom tuda posle obeda.", "Maybe we will go there after lunch."),
    ("Это будет прекрасный день.", "Eto budet prekrasnyy den.", "It will be a wonderful day."),
]

ENTRIES.append({
    "key": "r27_story3",
    "name": "Russian Story III - A Story of the Future",
    "group": "Advanced",
    "ladder_rank": 8,
    "ladder_tier": "advanced",
    "description": (
        "A ten-sentence story using future and conditional forms, with "
        "line-by-line English translation. Plan a family day at the "
        "country house and see both futures at work: perfective поедем, "
        "приготовит for single planned acts, imperfective будет работать, "
        "будем читать for ongoing plans - plus the conditional бы and the "
        "если-clause for possibilities.\n" + _sent(STORY_27)
    ),
    "how_it_works": (
        "Future plans split by aspect exactly like the past: single "
        "completed intentions take the perfective future (поедем, "
        "приготовит, останемся, пойдём), ongoing plans take буду + "
        "infinitive (будет работать, будем читать, будут играть). "
        "Conditions use если + future on both sides: если будет дождь, "
        "мы останемся дома. Wishes and polite possibilities use бы + "
        "past: я бы хотел (I would like). Может быть softens any plan "
        "into a possibility. The story shows that Russian future is not "
        "one form but a small system tuned by aspect and mood."
    ),
    "key_points": [
        "10-sentence future/conditional story with line-by-line translation.",
        "Perfective future for single acts: поедем, приготовит.",
        "Imperfective future (буду + infinitive) for ongoing plans.",
        "Conditions: если + future; wishes: бы + past (я бы хотел).",
        "Softening with может быть.",
    ],
    "requirements": [
        "Plan your tomorrow in 10 future-tense sentences.",
        "Convert 5 plans between perfective and imperfective futures.",
        "Write 3 conditional wishes with бы.",
    ],
    "standards": [
        "Narrative follows standard pedagogical story models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method reads the future as two sworn "
        "paths: the perfective path of single decisive acts, and the "
        "imperfective path of ongoing labor. Conditions are sworn "
        "if-oaths, and бы is the wish-oath that softens any claim."
    ),
    "demo_key": "story",
    "demo_data": {"lines": [list(s) for s in STORY_27], "tense": "future"},
})

# ---------------------------------------------------------------- record 28

IDIOMS_28 = [
    ("Без труда не выловишь и рыбку из пруда.", "Bez truda ne vylovish i rybku iz pruda.",
     "Without effort you will not pull even a fish from the pond.", "Nothing is achieved without effort.",
     "Чтобы выучить язык, надо заниматься каждый день: без труда не выловишь и рыбку из пруда.",
     "Chtoby vyuchit yazyk, nado zanimatsya kazhdyy den: bez truda ne vylovish i rybku iz pruda.",
     "To learn a language you must study every day: no effort, no fish."),
    ("Тише едешь - дальше будешь.", "Tishe yedesh - dalshe budesh.",
     "The quieter you go, the farther you get.", "Slow and steady wins the race.",
     "Не торопись: тише едешь - дальше будешь.",
     "Ne toropis: tishe yedesh - dalshe budesh.",
     "Do not hurry: slow and steady wins the race."),
    ("Не всё то золото, что блестит.", "Ne vsyo to zoloto, chto blestit.",
     "Not all that glitters is gold.", "Appearances deceive.",
     "Не верь рекламе: не всё то золото, что блестит.",
     "Ne ver reklame: ne vsyo to zoloto, chto blestit.",
     "Do not trust advertising: all that glitters is not gold."),
    ("Век живи - век учись.", "Vek zhivi - vek uchis.",
     "Live a century, learn a century.", "You never stop learning.",
     "Век живи - век учись, - говорит мой учитель.",
     "Vek zhivi - vek uchis, - govorit moy uchitel.",
     "Live and learn, says my teacher."),
    ("Дело мастера боится.", "Delo mastera boitsya.",
     "Work is afraid of the master.", "A skilled worker handles any job.",
     "Он всё чинит сам: дело мастера боится.",
     "On vsyo chinit sam: delo mastera boitsya.",
     "He fixes everything himself: work fears the master."),
    ("Лучше поздно, чем никогда.", "Luchshe pozdno, chem nikogda.",
     "Better late than never.", "Late action beats none.",
     "Он пришёл через час, но лучше поздно, чем никогда.",
     "On prishyol cherez chas, no luchshe pozdno, chem nikogda.",
     "He came an hour late, but better late than never."),
    ("Слово - не воробей, вылетит - не поймаешь.", "Slovo - ne vorobey, vyletit - ne poymayesh.",
     "A word is not a sparrow; once it flies out you will not catch it.", "Think before you speak.",
     "Думай, прежде чем говорить: слово - не воробей.",
     "Dumay, prezhde chem govorit: slovo - ne vorobey.",
     "Think before you speak: a word is not a sparrow."),
    ("Семь раз отмерь - один раз отрежь.", "Sem raz otmer - odin raz otrezh.",
     "Measure seven times, cut once.", "Plan carefully before acting.",
     "Семь раз отмерь - один раз отрежь, - советует мастер.",
     "Sem raz otmer - odin raz otrezh, - sovetuyet master.",
     "Measure seven times, cut once, advises the master."),
    ("Волков бояться - в лес не ходить.", "Volkov boyatsya - v les ne khodit.",
     "If you fear wolves, do not go to the forest.", "No risk, no reward.",
     "Волков бояться - в лес не ходить: начинай своё дело.",
     "Volkov boyatsya - v les ne khodit: nachinay svoyo delo.",
     "Nothing ventured, nothing gained: start your business."),
    ("Дарёному коню в зубы не смотрят.", "Daryonomu konyu v zuby ne smotryat.",
     "Do not look a gift horse in the mouth.", "Do not criticize gifts.",
     "Подарок скромный, но дарёному коню в зубы не смотрят.",
     "Podarok skromnyy, no daryonomu konyu v zuby ne smotryat.",
     "The gift is modest, but do not look a gift horse in the mouth."),
    ("Кашу маслом не испортишь.", "Kashu maslom ne isportish.",
     "You cannot spoil porridge with butter.", "You cannot have too much of a good thing.",
     "Добавь ещё сыра: кашу маслом не испортишь.",
     "Dobav yeshcho syra: kashu maslom ne isportish.",
     "Add more cheese: you cannot have too much of a good thing."),
    ("Не имей сто рублей, а имей сто друзей.", "Ne imey sto rubley, a imey sto druzey.",
     "Have not a hundred rubles, but a hundred friends.", "Friendship beats money.",
     "Не имей сто рублей, а имей сто друзей, - говорит пословица.",
     "Ne imey sto rubley, a imey sto druzey, - govorit poslovitsa.",
     "Have a hundred friends, not a hundred rubles, says the proverb."),
    ("Повторение - мать учения.", "Povtoreniye - mat ucheniya.",
     "Repetition is the mother of learning.", "Practice makes perfect.",
     "Повторение - мать учения: читай текст ещё раз.",
     "Povtoreniye - mat ucheniya: chitay tekst yeshcho raz.",
     "Repetition is the mother of learning: read the text again."),
    ("Утро вечера мудренее.", "Utro vechera mudreneye.",
     "Morning is wiser than evening.", "Sleep on a hard decision.",
     "Не решай сейчас: утро вечера мудренее.",
     "Ne reshay seychas: utro vechera mudreneye.",
     "Do not decide now: sleep on it."),
    ("Что написано пером, того не вырубишь топором.", "Chto napisano perom, togo ne vyrubish toporom.",
     "What is written with a pen cannot be cut out with an axe.", "Written words are permanent.",
     "Думай, что пишешь: что написано пером, того не вырубишь топором.",
     "Dumay, chto pishesh: chto napisano perom, togo ne vyrubish toporom.",
     "Think about what you write: the written word is permanent."),
    ("В гостях хорошо, а дома лучше.", "V gostyakh khorosho, a doma luchshe.",
     "Visiting is good, but home is better.", "There is no place like home.",
     "В гостях хорошо, а дома лучше, - вздохнул путешественник.",
     "V gostyakh khorosho, a doma luchshe, - vzdohnul puteshestvennik.",
     "East or west, home is best, sighed the traveler."),
    ("Яблоко от яблони недалеко падает.", "Yabloko ot yabloni nedaleko padayet.",
     "The apple does not fall far from the tree.", "Children resemble parents.",
     "Он такой же упрямый, как отец: яблоко от яблони недалеко падает.",
     "On takoy zhe upryamyy, kak otets: yabloko ot yabloni nedaleko padayet.",
     "He is as stubborn as his father: the apple does not fall far from the tree."),
    ("Куй железо, пока горячо.", "Kuy zhelezo, poka goryacho.",
     "Forge the iron while it is hot.", "Strike while the iron is hot.",
     "Куй железо, пока горячо: звони сейчас.",
     "Kuy zhelezo, poka goryacho: zvoni seychas.",
     "Strike while the iron is hot: call now."),
    ("Глаза боятся, а руки делают.", "Glaza boyatsya, a ruki delayut.",
     "The eyes fear, but the hands do.", "Start and the fear will pass.",
     "Глаза боятся, а руки делают: начинай работу.",
     "Glaza boyatsya, a ruki delayut: nachinay rabotu.",
     "The eyes fear but the hands do: start the work."),
    ("На безрыбье и рак рыба.", "Na bezrybye i rak ryba.",
     "Where there is no fish, even a crayfish is a fish.", "Make do with what you have.",
     "На безрыбье и рак рыба: бери, что есть.",
     "Na bezrybye i rak ryba: beri, chto yest.",
     "Beggars cannot be choosers: take what there is."),
]

ENTRIES.append({
    "key": "r28_idioms",
    "name": "Russian Idioms and Proverbs",
    "group": "Advanced",
    "ladder_rank": 8,
    "ladder_tier": "advanced",
    "description": (
        "Twenty Russian idioms and proverbs - each with transliteration, "
        "literal translation, real meaning, and an example sentence "
        "translated into English. Proverbs are the cultural bedrock of "
        "Russian speech: quoting one correctly marks you as an insider.\n" +
        "\n".join(
            "%d. %s (%s) Literal: %s Meaning: %s Example: %s (%s - %s)" % (
                i + 1, idm, idtr, lit, mean, ex, extr, exen)
            for i, (idm, idtr, lit, mean, ex, extr, exen) in enumerate(IDIOMS_28))
    ),
    "how_it_works": (
        "Russian proverbs work by fixed form: the wording never changes, "
        "and half-quoting one invites the listener to complete it. Many "
        "use parallel structure with a dash: Тише едешь - дальше будешь; "
        "Век живи - век учись. The grammar inside is often archaic or "
        "elliptical (Дело мастера боится), which is why proverbs are "
        "learned whole, not built. Using a proverb correctly requires "
        "matching its situation: Утро вечера мудренее for delayed "
        "decisions, Куй железо, пока горячо for urgent ones. The example "
        "sentences show each proverb in its natural habitat."
    ),
    "key_points": [
        "20 idioms and proverbs with literal translations, meanings, and example sentences.",
        "Proverbs have fixed wording - learn them whole, never rebuild them.",
        "Parallel dash structure is the classic proverb form.",
        "Match the proverb to its situation: delay vs urgency, effort vs luck.",
        "Quoting proverbs correctly marks cultural fluency.",
    ],
    "requirements": [
        "Memorize 10 proverbs with meanings.",
        "Use 3 proverbs correctly in conversation this week.",
        "Explain 5 proverbs' literal vs real meanings to a friend.",
    ],
    "standards": [
        "Proverb texts follow standard published collections.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method keeps proverbs as sworn sayings of "
        "the people: each is a covenant of wisdom sealed in fixed words, "
        "never to be rebuilt or broken. Speak one whole and true, and the "
        "language itself vouches for you."
    ),
    "demo_key": "idioms",
    "demo_data": {"idioms": [[idm, lit, mean] for idm, idtr, lit, mean, ex, extr, exen in IDIOMS_28]},
})

# ---------------------------------------------------------------- record 29

REG_29 = [
    ("Привет!", "Privet!", "Hi!", "Здравствуйте!", "Zdravstvuyte!", "Hello!", "Friends and peers vs strangers and elders."),
    ("Пока!", "Poka!", "Bye!", "До свидания!", "Do svidaniya!", "Goodbye!", "Casual parting vs polite parting."),
    ("Ты", "Ty", "you (informal)", "Вы", "Vy", "you (formal)", "One friend vs a stranger, elder, or group."),
    ("Спасибо!", "Spasibo!", "Thanks!", "Благодарю вас!", "Blagodaryu vas!", "Thank you!", "Everyday thanks vs formal gratitude."),
    ("Извини!", "Izvini!", "Sorry!", "Извините, пожалуйста!", "Izvinite, pozhaluysta!", "Excuse me!", "Casual apology vs polite apology."),
    ("Как дела?", "Kak dela?", "How are you?", "Как ваши дела?", "Kak vashi dela?", "How are you?", "Friends vs formal acquaintance."),
    ("Садись!", "Sadis!", "Sit down!", "Садитесь, пожалуйста!", "Sadites, pozhaluysta!", "Please sit down!", "Home vs office or ceremony."),
    ("Подожди!", "Podozhdi!", "Wait!", "Подождите, пожалуйста!", "Podozhdite, pozhaluysta!", "Please wait!", "Friends vs service situations."),
    ("Помоги мне!", "Pomogi mne!", "Help me!", "Не могли бы вы мне помочь?", "Ne mogli by vy mne pomoch?", "Could you help me?", "Direct ask vs softened formal request."),
    ("Дай мне!", "Day mne!", "Give me!", "Дайте мне, пожалуйста!", "Dayte mne, pozhaluysta!", "Give me, please!", "Family vs shops and offices."),
    ("Скажи!", "Skazhi!", "Tell me!", "Скажите, пожалуйста!", "Skazhite, pozhaluysta!", "Tell me, please!", "Friends vs strangers."),
    ("Позвони мне!", "Pozvoni mne!", "Call me!", "Позвоните мне, пожалуйста!", "Pozvonite mne, pozhaluysta!", "Please call me!", "Close contacts vs business."),
    ("Я не понимаю.", "Ya ne ponimayu.", "I do not understand.", "Простите, я не совсем понимаю.", "Prostite, ya ne sovsem ponimayu.", "Sorry, I do not quite understand.", "Blunt vs softened with strangers."),
    ("Где туалет?", "Gde tualet?", "Where is the bathroom?", "Подскажите, пожалуйста, где здесь туалет?", "Podskazhite, pozhaluysta, gde zdes tualet?", "Could you tell me where the bathroom is?", "Direct vs polite framing."),
    ("Сколько стоит?", "Skolko stoit?", "How much?", "Скажите, пожалуйста, сколько это стоит?", "Skazhite, pozhaluysta, skolko eto stoit?", "Could you tell me the price?", "Market vs formal shop."),
]

ENTRIES.append({
    "key": "r29_registers",
    "name": "Russian Formal and Polite Registers",
    "group": "Advanced",
    "ladder_rank": 9,
    "ladder_tier": "advanced",
    "description": (
        "Fifteen formal vs informal pairs for letters, business, and "
        "elders - each pair in Russian with transliteration, English "
        "translation, and a note on when to use which. The rule of thumb: "
        "informal (ты-forms, short commands) for friends and family; "
        "formal (вы-forms, пожалуйста, softened questions) for everyone "
        "else until invited closer.\n" + _pairs(REG_29)
    ),
    "how_it_works": (
        "Register in Russian is a system, not a feeling. Informal uses "
        "ты, short imperatives (садись, подожди), and direct questions. "
        "Formal uses вы, -те imperatives softened with пожалуйста "
        "(садитесь, пожалуйста), and indirect question frames: скажите, "
        "пожалуйста; не могли бы вы; подскажите, пожалуйста. Business "
        "letters open with Уважаемый/Уважаемая (Respected) and close "
        "with С уважением (With respect). Switching to ты is a social "
        "milestone - the elder or the host proposes it, never the junior "
        "uninvited. Using вы with a close friend creates cold distance; "
        "using ты with a stranger creates offense."
    ),
    "key_points": [
        "15 formal/informal pairs with usage notes.",
        "Informal: ты, short imperatives, direct questions - friends and family.",
        "Formal: вы, -те + пожалуйста, indirect frames - strangers, elders, business.",
        "Business letters: Уважаемый ... С уважением.",
        "The switch to ты is proposed by the elder/host, never taken uninvited.",
    ],
    "requirements": [
        "Rewrite 5 informal requests in formal register.",
        "Write a short formal letter and an informal note.",
        "Practice the softened frames: скажите, пожалуйста; не могли бы вы.",
    ],
    "standards": [
        "Register analysis follows standard sociolinguistic description.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method swears two banners of speech: the "
        "lowered banner of kin - short, direct, warm - and the raised "
        "banner of respect - softened, indirect, armored with пожалуйста. "
        "Raise the wrong banner and the covenant of conversation breaks."
    ),
    "demo_key": "register",
    "demo_data": {"pairs": [[a, b] for a, atr, ae, b, btr, be, n in REG_29]},
})

# ---------------------------------------------------------------- record 30

CX_30 = [
    ("Я остался дома, потому что шёл дождь.", "Ya ostalsya doma, potomu chto shyol dozhd.", "I stayed home because it was raining.", "потому что"),
    ("Книга, которую ты мне дал, очень интересная.", "Kniga, kotoruyu ty mne dal, ochen interesnaya.", "The book that you gave me is very interesting.", "которую"),
    ("Когда я пришёл, все уже ужинали.", "Kogda ya prishyol, vse uzhe uzhinali.", "When I arrived, everyone was already having dinner.", "когда"),
    ("Если будет хорошая погода, мы пойдём гулять.", "Yesli budet khoroshaya pogoda, my poydyom gulyat.", "If the weather is good, we will go for a walk.", "если"),
    ("Хотя было поздно, мы продолжали разговаривать.", "Khotya bylo pozdno, my prodolzhali razgovarivat.", "Although it was late, we kept talking.", "хотя"),
    ("Я учу русский язык, чтобы читать книги в оригинале.", "Ya uchu russkiy yazyk, chtoby chitat knigi v originale.", "I am learning Russian in order to read books in the original.", "чтобы"),
    ("Он так устал, что сразу лёг спать.", "On tak ustal, chto srazu lyog spat.", "He was so tired that he went straight to bed.", "что"),
    ("Я люблю чай, а мой брат предпочитает кофе.", "Ya lyublyu chay, a moy brat predpochitayet kofe.", "I love tea, while my brother prefers coffee.", "а"),
    ("Мы купили хлеб, молоко и сыр.", "My kupili khleb, moloko i syr.", "We bought bread, milk, and cheese.", "и"),
    ("Он не пришёл, но позвонил и извинился.", "On ne prishyol, no pozvonil i izvinilsya.", "He did not come, but he called and apologized.", "но"),
    ("Ты хочешь пойти в кино или остаться дома?", "Ty khochesh poyti v kino ili ostatsya doma?", "Do you want to go to the cinema or stay home?", "или"),
    ("Поэтому мы решили отложить поездку.", "Poetomu my reshili otlozhit poyezdku.", "That is why we decided to postpone the trip.", "поэтому"),
    ("Дом, в котором я живу, построили сто лет назад.", "Dom, v kotorom ya zhivu, postroili sto let nazad.", "The house I live in was built a hundred years ago.", "в котором"),
    ("Пока мама готовила ужин, дети делали уроки.", "Poka mama gotovila uzhin, deti delali uroki.", "While mother was cooking dinner, the children were doing homework.", "пока"),
    ("Чем больше ты читаешь, тем лучше говоришь.", "Chem bolshe ty chitayesh, tem luchshe govorish.", "The more you read, the better you speak.", "чем ... тем"),
]

ENTRIES.append({
    "key": "r30_complex",
    "name": "Russian Compound and Complex Sentences",
    "group": "Advanced",
    "ladder_rank": 9,
    "ladder_tier": "advanced",
    "description": (
        "Fifteen long sentences with clauses, connectors, and relative "
        "clauses - each parsed and translated. Master the connectors: "
        "потому что (because), который (which/who), когда (when), если "
        "(if), хотя (although), чтобы (in order to), что (that), а/и/но/или "
        "(and/but/or), поэтому (therefore), пока (while), чем...тем (the "
        "more...the).\n" +
        "\n".join("%d. %s (%s - %s) Connector: %s" % (i + 1, ru, tr, en, cx)
                  for i, (ru, tr, en, cx) in enumerate(CX_30))
    ),
    "how_it_works": (
        "Complex sentences join clauses with a comma before the "
        "connector: always write the comma. Который declines to match "
        "its role in the relative clause: которую (accusative feminine) "
        "in книгу, которую ты дал; в котором (prepositional) in дом, в "
        "котором я живу. Чтобы takes the past tense for purpose: чтобы "
        "читать (infinitive after same subject), чтобы ты понял (past "
        "after different subject). А contrasts mildly (я люблю чай, а "
        "брат - кофе) while но contrasts strongly. Чем...тем builds "
        "correlations: чем больше, тем лучше. Parse each sentence by "
        "finding the connector, splitting the clauses, and naming each "
        "clause's verb."
    ),
    "key_points": [
        "15 complex sentences, each parsed with its connector named.",
        "Comma always before the connector.",
        "Который declines by its role in the relative clause.",
        "Чтобы + past for purpose with a different subject.",
        "А for mild contrast, но for strong; чем...тем for correlations.",
    ],
    "requirements": [
        "Parse all 15 sentences: split clauses, name connectors.",
        "Combine 10 simple sentence pairs with the right connector.",
        "Write 5 complex sentences about your life.",
    ],
    "standards": [
        "Clause analysis follows the standard description in the cited grammars.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method builds sentences as sworn "
        "alliances of clauses: the comma is the treaty line, the "
        "connector the sworn bridge, and который the envoy who takes "
        "the case-oath of whatever role it serves in the foreign clause."
    ),
    "demo_key": "complex",
    "demo_data": {"sentences": [[ru, cx] for ru, tr, en, cx in CX_30]},
})

# ---------------------------------------------------------------- record 31

DLG_31 = [
    ("Покупатель", "Здравствуйте!", "Zdravstvuyte!", "Hello!"),
    ("Продавец", "Добрый день! Что желаете?", "Dobryy den! Chto zhelayete?", "Good day! What would you like?"),
    ("Покупатель", "У вас есть свежие яблоки?", "U vas yest svezhiye yabloki?", "Do you have fresh apples?"),
    ("Продавец", "Да, конечно. Вот, попробуйте.", "Da, konechno. Vot, poprobuyte.", "Yes, of course. Here, try one."),
    ("Покупатель", "Очень вкусные! Сколько стоят?", "Ochen vkusnyye! Skolko stoyat?", "Very tasty! How much are they?"),
    ("Продавец", "Сто рублей за килограмм.", "Sto rubley za kilogramm.", "One hundred rubles per kilo."),
    ("Покупатель", "Дороговато. А скидку сделаете?", "Dorogovato. A skidku sdelayete?", "A bit pricey. Will you give a discount?"),
    ("Продавец", "Хорошо, девяносто рублей, только для вас.", "Khorosho, devyanosto rubley, tolko dlya vas.", "Fine, ninety rubles, just for you."),
    ("Покупатель", "Дайте, пожалуйста, два килограмма.", "Dayte, pozhaluysta, dva kilogramma.", "Two kilos, please."),
    ("Продавец", "Вот, пожалуйста. Что-нибудь ещё?", "Vot, pozhaluysta. Chto-nibud yeshcho?", "Here you are. Anything else?"),
    ("Покупатель", "Да, ещё помидоры. Они свежие?", "Da, yeshcho pomidory. Oni svezhiye?", "Yes, tomatoes too. Are they fresh?"),
    ("Продавец", "Самые свежие! Только сегодня привезли.", "Samyye svezhiye! Tolko sevodnya privezli.", "The freshest! Just brought in today."),
    ("Покупатель", "Тогда возьму килограмм.", "Togda vozmu kilogramm.", "Then I will take a kilo."),
    ("Продавец", "Отлично. С вас двести семьдесят рублей.", "Otlichno. S vas dvesti semdesyat rubley.", "Great. That is two hundred seventy rubles."),
    ("Покупатель", "Вот триста. Сдачи не надо.", "Vot trista. Sdachi ne nado.", "Here is three hundred. Keep the change."),
    ("Продавец", "Спасибо большое! Приходите ещё!", "Spasibo bolshoye! Prikhodite yeshcho!", "Thank you very much! Come again!"),
    ("Покупатель", "Обязательно приду. До свидания!", "Obyazatelno pridu. Do svidaniya!", "I certainly will. Goodbye!"),
    ("Продавец", "До свидания! Хорошего дня!", "Do svidaniya! Khoroshego dnya!", "Goodbye! Have a good day!"),
    ("Покупатель", "И вам хорошего дня!", "I vam khoroshego dnya!", "Good day to you too!"),
    ("Продавец", "Спасибо!", "Spasibo!", "Thanks!"),
]

ENTRIES.append({
    "key": "r31_market",
    "name": "Russian Conversation - At the Market",
    "group": "Advanced",
    "ladder_rank": 9,
    "ladder_tier": "advanced",
    "description": (
        "A twenty-line bilingual dialogue at the market, annotated: a "
        "buyer greets the seller, tastes the apples, asks the price, "
        "bargains, buys two kilos of apples and a kilo of tomatoes, pays, "
        "and they part warmly. Watch the bargaining arc: дороговато "
        "(a bit pricey) invites the discount, and сдачи не надо (keep "
        "the change) closes with generosity.\n" + _dialogue(DLG_31)
    ),
    "how_it_works": (
        "Market dialogue runs on a fixed script: greeting, request, "
        "tasting, price question, bargaining, agreement, payment, "
        "farewell. The seller uses the formal вы throughout (желаете, "
        "сделаете); the buyer matches it. Попробуйте (try) is the "
        "perfective imperative of hospitality. Prices are quoted за "
        "килограмм (per kilo); the total is announced as с вас + amount. "
        "Bargaining is signaled indirectly - дороговато states the "
        "problem and lets the seller offer the solution. The dialogue "
        "alternates speakers cleanly, making it ideal for two-voice "
        "practice."
    ),
    "key_points": [
        "20-line market dialogue with full translations.",
        "The market script: greet, taste, ask price, bargain, pay, farewell.",
        "Formal вы throughout the transaction.",
        "Bargaining is indirect: дороговато invites the discount.",
        "Price formulas: за килограмм; с вас + total; сдачи не надо.",
    ],
    "requirements": [
        "Perform the dialogue with a partner, then swap roles.",
        "Improvise a market scene with different goods.",
        "Bargain in Russian for 3 items without switching language.",
    ],
    "standards": [
        "Dialogue follows standard pedagogical conversation models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method stages the market as the sworn "
        "exchange: buyer and seller meet under the formal banner, the "
        "taste is the oath of quality, the bargain the covenant of price, "
        "and the kept change the seal of goodwill."
    ),
    "demo_key": "dialogue",
    "demo_data": {"lines": [[sp, ru] for sp, ru, tr, en in DLG_31],
                  "speakers": ["Покупатель", "Продавец"]},
})

# ---------------------------------------------------------------- record 32

DLG_32 = [
    ("Анна", "Привет, Иван! Как дела?", "Privet, Ivan! Kak dela?", "Hi, Ivan! How are you?"),
    ("Иван", "Привет, Анна! Отлично! А у тебя?", "Privet, Anna! Otlichno! A u tebya?", "Hi, Anna! Great! And you?"),
    ("Анна", "Хорошо, спасибо. Давно не виделись!", "Khorosho, spasibo. Davno ne videlis!", "Fine, thanks. Long time no see!"),
    ("Иван", "Да, целую вечность! Как работа?", "Da, tseluyu vechnost! Kak rabota?", "Yes, ages! How is work?"),
    ("Анна", "Всё хорошо. А ты всё ещё учишься?", "Vsyo khorosho. A ty vsyo yeshcho uchishsya?", "All good. Are you still studying?"),
    ("Иван", "Да, заканчиваю университет в июне.", "Da, zakanchivayu universitet v iyune.", "Yes, finishing university in June."),
    ("Анна", "Поздравляю! Какие планы потом?", "Pozdravlyayu! Kakiye plany potom?", "Congratulations! What are your plans after?"),
    ("Иван", "Хочу найти работу по специальности.", "Khochu nayti rabotu po spetsialnosti.", "I want to find a job in my field."),
    ("Анна", "Уверена, у тебя получится.", "Uverena, u tebya poluchitsya.", "I am sure you will manage."),
    ("Иван", "Спасибо! А как твоя семья?", "Spasibo! A kak tvoya semya?", "Thanks! And how is your family?"),
    ("Анна", "Все здоровы. Мама передавала привет.", "Vse zdorovy. Mama peredavala privet.", "Everyone is well. Mom said hello."),
    ("Иван", "Передай ей большой привет от меня!", "Pereday yey bolshoy privet ot menya!", "Give her my warm regards!"),
    ("Анна", "Обязательно. Слушай, может, выпьем кофе?", "Obyazatelno. Slushay, mozhet, vypyem kofe?", "Of course. Listen, shall we have coffee?"),
    ("Иван", "С удовольствием! Тут рядом хорошее кафе.", "S udovolstviyem! Tut ryadom khorosheye kafe.", "With pleasure! There is a good cafe nearby."),
    ("Анна", "Отлично, пойдём!", "Otlichno, poydyom!", "Great, let us go!"),
    ("Иван", "Ты слышала новость про Петра?", "Ty slyshala novost pro Petra?", "Did you hear the news about Pyotr?"),
    ("Анна", "Нет, а что случилось?", "Net, a chto sluchilos?", "No, what happened?"),
    ("Иван", "Он женился в прошлом месяце!", "On zhenilsya v proshlom mesyatse!", "He got married last month!"),
    ("Анна", "Ничего себе! Надо его поздравить.", "Nichego sebe! Nado yego pozdravit.", "Wow! We must congratulate him."),
    ("Иван", "Давай позвоним ему сегодня вечером.", "Davay pozvonim yemu sevodnya vecherom.", "Let us call him tonight."),
]

ENTRIES.append({
    "key": "r32_friend",
    "name": "Russian Conversation - Meeting a Friend",
    "group": "Advanced",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "A twenty-line bilingual dialogue between old friends, annotated: "
        "Anna and Ivan meet, catch up on work and studies, exchange family "
        "news, decide on coffee, share gossip about Pyotr's wedding, and "
        "plan to call him. Notice the informal ты throughout, the "
        "catch-up question chain, and the decision arc from proposal "
        "(может, выпьем кофе?) to agreement.\n" + _dialogue(DLG_32)
    ),
    "how_it_works": (
        "Friend dialogue runs informal: привет, ты-forms, short "
        "questions. Catch-up follows a chain: greeting, health/work "
        "question, news exchange, family regards, new proposal. Передавала "
        "привет (said hello) is the standard regards formula; the answer "
        "is передай ей большой привет (give her my warm regards). "
        "Proposals use может + perfective future (может, выпьем кофе?) "
        "and agreement is с удовольствием. Gossip is introduced with ты "
        "слышала новость про... and reacted to with ничего себе. The "
        "dialogue closes with a joint plan: давай позвоним."
    ),
    "key_points": [
        "20-line friends dialogue with full translations.",
        "Informal register throughout: привет, ты-forms.",
        "Catch-up chain: greeting, work, studies, family, proposal.",
        "Regards formula: передавала привет - передай большой привет.",
        "Proposals: может + future; agreement: с удовольствием.",
    ],
    "requirements": [
        "Perform the dialogue, then improvise your own catch-up.",
        "Pass regards through a friend in Russian.",
        "Propose and accept 3 plans using может + future.",
    ],
    "standards": [
        "Dialogue follows standard pedagogical conversation models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method meets old friends under the "
        "lowered banner of kin: ты-forms, short questions, warm regards "
        "passed like sworn tokens between households. Every catch-up is "
        "a renewal of the friendship covenant."
    ),
    "demo_key": "dialogue",
    "demo_data": {"lines": [[sp, ru] for sp, ru, tr, en in DLG_32],
                  "speakers": ["Анна", "Иван"]},
})

# ---------------------------------------------------------------- record 33

DLG_33 = [
    ("Марина", "У меня проблема с компьютером.", "U menya problema s kompyuterom.", "I have a computer problem."),
    ("Олег", "Что случилось? Расскажи подробнее.", "Chto sluchilos? Rasskazhi podrobneye.", "What happened? Tell me in detail."),
    ("Марина", "Он не включается. Экран чёрный.", "On ne vklyuchayetsya. Ekran chyornyy.", "It will not turn on. The screen is black."),
    ("Олег", "Проверь, включён ли он в розетку.", "Prover, vklyuchyon li on v rozetku.", "Check whether it is plugged in."),
    ("Марина", "Да, кабель подключён.", "Da, kabel podklyuchyon.", "Yes, the cable is connected."),
    ("Олег", "А кнопка питания горит?", "A knopka pitaniya gorit?", "Is the power button lit?"),
    ("Марина", "Нет, ничего не горит.", "Net, nichego ne gorit.", "No, nothing is lit."),
    ("Олег", "Попробуй другую розетку.", "Poprobuy druguyu rozetku.", "Try a different outlet."),
    ("Марина", "Сейчас попробую... Тоже не работает.", "Seychas poprobuyu... Tozhe ne rabotayet.", "I will try now... It still does not work."),
    ("Олег", "Может, дело в блоке питания?", "Mozhet, delo v bloke pitaniya?", "Maybe the power supply is the issue?"),
    ("Марина", "Возможно. Что мне делать?", "Vozmozhno. Chto mne delat?", "Possibly. What should I do?"),
    ("Олег", "Отнеси его в сервис завтра утром.", "Otnesi yego v servis zavtra utrom.", "Take it to the repair shop tomorrow morning."),
    ("Марина", "А мои файлы? Они не пропадут?", "A moi fayly? Oni ne propadut?", "And my files? Will they be lost?"),
    ("Олег", "Скорее всего, нет. Диск, наверное, цел.", "Skoreye vsego, net. Disk, navernoye, tsel.", "Most likely not. The drive is probably fine."),
    ("Марина", "Надеюсь. Там важные документы.", "Nadeyus. Tam vazhnyye dokumenty.", "I hope so. There are important documents there."),
    ("Олег", "В следующий раз делай копии.", "V sleduyushchiy raz delay kopii.", "Next time make backups."),
    ("Марина", "Ты прав. Научусь на своих ошибках.", "Ty prav. Nauchus na svoikh oshibkakh.", "You are right. I will learn from my mistakes."),
    ("Олег", "Хочешь, я пойду с тобой в сервис?", "Khochesh, ya poydu s toboy v servis?", "Do you want me to go to the shop with you?"),
    ("Марина", "Было бы здорово! Спасибо за помощь.", "Bylo by zdorovo! Spasibo za pomoshch.", "That would be great! Thanks for the help."),
    ("Олег", "Всегда пожалуйста! Увидимся завтра.", "Vsegda pozhaluysta! Uvidimsya zavtra.", "Anytime! See you tomorrow."),
]

ENTRIES.append({
    "key": "r33_problem",
    "name": "Russian Conversation - Solving a Problem",
    "group": "Advanced",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "A twenty-line bilingual problem-solving dialogue, annotated: "
        "Marina's computer will not turn on, Oleg troubleshoots step by "
        "step (power cable, power button, different outlet, power supply "
        "hypothesis), they address the file-backup worry, and Oleg "
        "offers to go to the repair shop with her. A model of technical "
        "troubleshooting in Russian.\n" + _dialogue(DLG_33)
    ),
    "how_it_works": (
        "Troubleshooting dialogue follows the diagnostic ladder: symptom "
        "(не включается), simplest checks first (розетка, кнопка "
        "питания), then hypotheses (может, дело в блоке питания?). "
        "Instructions use the informal imperative (проверь, попробуй, "
        "отнеси); hypotheses soften with может, возможно, наверное, "
        "скорее всего. Worry is voiced as a question (они не пропадут?) "
        "and answered with reassurance. Advice for the future uses в "
        "следующий раз + imperative. Offers use хочешь + infinitive "
        "clause; gratitude closes the exchange."
    ),
    "key_points": [
        "20-line troubleshooting dialogue with full translations.",
        "Diagnostic ladder: symptom, simple checks, hypotheses.",
        "Instructions: informal imperatives; hypotheses: может/наверное.",
        "Worry voiced as question, answered with reassurance.",
        "Offers: хочешь + clause; future advice: в следующий раз.",
    ],
    "requirements": [
        "Troubleshoot a broken device in Russian with a partner.",
        "Explain 3 tech problems and their solutions.",
        "Give advice using в следующий раз + imperative.",
    ],
    "standards": [
        "Dialogue follows standard pedagogical conversation models.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method troubleshoots as a sworn inquiry: "
        "symptoms declared, simple oaths tested first, hypotheses sworn "
        "softly with может. The helper's imperatives are direct but "
        "kind, and the closing offer seals the covenant of aid."
    ),
    "demo_key": "dialogue",
    "demo_data": {"lines": [[sp, ru] for sp, ru, tr, en in DLG_33],
                  "speakers": ["Марина", "Олег"]},
})

# ---------------------------------------------------------------- record 34

WORDS_200 = [
    # pronouns and related (12)
    ("я", "I"), ("ты", "you (informal)"), ("он", "he"), ("она", "she"),
    ("оно", "it"), ("мы", "we"), ("вы", "you (formal)"), ("они", "they"),
    ("мой", "my"), ("твой", "your (informal)"), ("наш", "our"), ("их", "their"),
    # numbers (20)
    ("один", "one"), ("два", "two"), ("три", "three"), ("четыре", "four"),
    ("пять", "five"), ("шесть", "six"), ("семь", "seven"), ("восемь", "eight"),
    ("девять", "nine"), ("десять", "ten"), ("одиннадцать", "eleven"),
    ("двенадцать", "twelve"), ("двадцать", "twenty"), ("тридцать", "thirty"),
    ("сорок", "forty"), ("пятьдесят", "fifty"), ("сто", "one hundred"),
    ("тысяча", "one thousand"), ("первый", "first"), ("второй", "second"),
    # nouns (60)
    ("человек", "person"), ("мужчина", "man"), ("женщина", "woman"),
    ("ребёнок", "child"), ("друг", "friend"), ("семья", "family"),
    ("дом", "house"), ("город", "city"), ("улица", "street"), ("школа", "school"),
    ("книга", "book"), ("стол", "table"), ("стул", "chair"), ("окно", "window"),
    ("дверь", "door"), ("хлеб", "bread"), ("вода", "water"), ("молоко", "milk"),
    ("еда", "food"), ("машина", "car"), ("поезд", "train"), ("самолёт", "airplane"),
    ("работа", "work"), ("время", "time"), ("деньги", "money"), ("мама", "mama"),
    ("папа", "papa"), ("брат", "brother"), ("сестра", "sister"), ("сын", "son"),
    ("дочь", "daughter"), ("бабушка", "grandmother"), ("дедушка", "grandfather"),
    ("учитель", "teacher"), ("ученик", "pupil"), ("врач", "doctor"),
    ("магазин", "store"), ("рынок", "market"), ("ресторан", "restaurant"),
    ("гостиница", "hotel"), ("парк", "park"), ("лес", "forest"), ("река", "river"),
    ("море", "sea"), ("гора", "mountain"), ("солнце", "sun"), ("луна", "moon"),
    ("звезда", "star"), ("небо", "sky"), ("земля", "earth"), ("дерево", "tree"),
    ("цветок", "flower"), ("трава", "grass"), ("собака", "dog"), ("кошка", "cat"),
    ("птица", "bird"), ("рыба", "fish"), ("вопрос", "question"), ("ответ", "answer"),
    ("проблема", "problem"),
    # verbs (48)
    ("быть", "to be"), ("делать", "to do"), ("идти", "to go (on foot)"),
    ("ехать", "to go (by vehicle)"), ("говорить", "to speak"),
    ("сказать", "to say"), ("знать", "to know"), ("хотеть", "to want"),
    ("мочь", "to be able"), ("есть", "to eat"), ("пить", "to drink"),
    ("спать", "to sleep"), ("работать", "to work"), ("учиться", "to study"),
    ("читать", "to read"), ("писать", "to write"), ("смотреть", "to watch"),
    ("слушать", "to listen"), ("ждать", "to wait"), ("любить", "to love"),
    ("думать", "to think"), ("жить", "to live"), ("покупать", "to buy"),
    ("давать", "to give"), ("брать", "to take"), ("стоять", "to stand"),
    ("сидеть", "to sit"), ("лежать", "to lie"), ("открывать", "to open"),
    ("закрывать", "to close"), ("начинать", "to begin"), ("кончать", "to end"),
    ("помогать", "to help"), ("звонить", "to call"), ("встречать", "to meet"),
    ("спрашивать", "to ask"), ("отвечать", "to answer"),
    ("понимать", "to understand"), ("помнить", "to remember"),
    ("забывать", "to forget"), ("играть", "to play"), ("гулять", "to walk"),
    ("готовить", "to cook"), ("мыть", "to wash"), ("лететь", "to fly"),
    ("плыть", "to swim, to sail"), ("нести", "to carry"), ("вести", "to lead"),
    # adjectives (28)
    ("большой", "big"), ("маленький", "small"), ("новый", "new"),
    ("старый", "old"), ("хороший", "good"), ("плохой", "bad"),
    ("красивый", "beautiful"), ("быстрый", "fast"), ("медленный", "slow"),
    ("тёплый", "warm"), ("холодный", "cold"), ("высокий", "tall"),
    ("низкий", "low"), ("длинный", "long"), ("короткий", "short"),
    ("широкий", "wide"), ("узкий", "narrow"), ("светлый", "light"),
    ("тёмный", "dark"), ("сильный", "strong"), ("слабый", "weak"),
    ("богатый", "rich"), ("бедный", "poor"), ("умный", "smart"),
    ("глупый", "stupid"), ("молодой", "young"), ("добрый", "kind"),
    ("весёлый", "cheerful"),
    # adverbs and function words (32)
    ("быстро", "quickly"), ("медленно", "slowly"), ("хорошо", "well"),
    ("плохо", "badly"), ("очень", "very"), ("слишком", "too"),
    ("всегда", "always"), ("никогда", "never"), ("часто", "often"),
    ("редко", "rarely"), ("сейчас", "now"), ("потом", "later"),
    ("здесь", "here"), ("там", "there"), ("дома", "at home"),
    ("сегодня", "today"), ("вчера", "yesterday"), ("завтра", "tomorrow"),
    ("утром", "in the morning"), ("вечером", "in the evening"),
    ("ночью", "at night"), ("днём", "in the daytime"), ("где", "where"),
    ("куда", "where to"), ("когда", "when"), ("почему", "why"),
    ("как", "how"), ("сколько", "how much"), ("кто", "who"), ("что", "what"),
    ("да", "yes"), ("нет", "no"),
]

ENTRIES.append({
    "key": "r34_mastery",
    "name": "Russian Mastery Review and Full Reference",
    "group": "Advanced",
    "ladder_rank": 10,
    "ladder_tier": "advanced",
    "description": (
        "The whole database in one teaching summary: the alphabet, 200 "
        "core words, the key grammar, and all phrase tables. Use this "
        "record as the daily review sheet - read it end to end once a "
        "week and the entire course stays alive.\n\nALPHABET (33 "
        "letters): А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш "
        "Щ Ъ Ы Ь Э Ю Я.\n\n200 CORE WORDS:\n" +
        "\n".join("%d. %s - %s" % (i + 1, ru, en)
                  for i, (ru, en) in enumerate(WORDS_200)) +
        "\n\nKEY GRAMMAR: six cases (nominative кто/что, genitive "
        "кого/чего, dative кому/чему, accusative кого/что, instrumental "
        "кем/чем, prepositional о ком/о чём); three genders (masculine, "
        "feminine, neuter); two numbers; three tenses with two aspects "
        "(imperfective ongoing, perfective completed); two conjugations; "
        "adjectives agree in gender, number, case; no articles; negation "
        "with не; questions by intonation, question words, or ли.\n\n"
        "PHRASE TABLES: greetings - Здравствуйте/Привет, Доброе "
        "утро/Добрый день/Добрый вечер, До свидания/Пока, Спасибо, "
        "Пожалуйста, Извините; time - Который час? Сейчас три часа; "
        "travel - Где вокзал? Сколько стоит билет?; shopping - Сколько "
        "стоит? Дайте чек; health - У меня болит голова; Мне нужен врач; "
        "feelings - Я счастлив; Не бойся; problem-solving - Что "
        "случилось? Попробуй ещё раз."
    ),
    "how_it_works": (
        "Mastery review works by spaced retrieval: the 200 words are the "
        "highest-frequency core of the language, and re-reading them "
        "weekly keeps all 34 records active at once. Test yourself in "
        "three passes: Russian to English (recognition), English to "
        "Russian (recall), and sentence use (production) - five random "
        "words a day in new sentences. The grammar block is the "
        "compressed rule set: if a sentence puzzles you, find its rule "
        "here first. The phrase tables are the emergency kit - the "
        "sentences that solve real situations. A learner who owns these "
        "200 words and the grammar block can read simple texts, hold "
        "daily conversations, and learn everything else from context."
    ),
    "key_points": [
        "The full 33-letter alphabet in one line for daily recitation.",
        "200 core words: 12 pronouns, 20 numbers, 60 nouns, 48 verbs, 28 adjectives, 32 adverbs and function words.",
        "Compressed grammar: 6 cases, 3 genders, 3 tenses x 2 aspects, agreement rules.",
        "Emergency phrase tables for greetings, time, travel, shopping, health, feelings, problems.",
        "Review method: weekly full read + 5 random words in new sentences daily.",
    ],
    "requirements": [
        "Recite the alphabet from memory, forwards and backwards.",
        "Score 100% on the 200 words Russian-to-English, then English-to-Russian.",
        "Use 20 random core words in new sentences of your own.",
        "Re-read one earlier record per day for a month.",
    ],
    "standards": [
        "Word selection follows frequency in standard pedagogical word lists.",
    ],
    "citations": list(CIT_ALL),
    "sig_lens": (
        "The Signature Russian Method seals the course here: 200 sworn "
        "words, 33 sworn signs, six sworn cases - the whole charter on "
        "one page. Review it weekly and the oath renews itself; the "
        "language that was foreign becomes sworn kin."
    ),
    "demo_key": "mastery",
    "demo_data": {"words": [[ru, en] for ru, en in WORDS_200],
                  "categories": {"pronouns": 12, "numbers": 20, "nouns": 60,
                                 "verbs": 48, "adjectives": 28, "other": 32}},
})
