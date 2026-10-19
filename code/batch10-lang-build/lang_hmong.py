# -*- coding: utf-8 -*-
"""Language data module: Hmong (hmn). Facts verified 2026-10-17 via
phrase references, UC Davis paj lug curriculum, Mong Leng dictionary."""

SLUG = "language-hmong"
PREFIX = "JAH-LHMN-"
SIG_PREFIX = "JAH-LHMNS-"
NAME = "Hmong"
NATIVE = "Hmoob"
NATIVE_ROMAN = "Hmoob"
ISO1 = ""
ISO3 = "hmn"
FAMILY = "Hmong-Mien > Hmongic > Western Hmongic"
SPEAKERS = "about 4 million speakers"
REGIONS = "Laos, Vietnam, Thailand, southern China and Myanmar; large diaspora in the United States, France and Australia"
SCRIPT_NAME = "RPA (Romanized Popular Alphabet)"
WORD_ORDER = "subject-verb-object (SVO)"
AI_NAME = "JAH Hmong Language Archivist"
SIG_AI_NAME = "JAH Hmong Signature Archivist"

OVERVIEW = (
    "Hmong (Hmoob) is a Hmong-Mien language spoken by about 4 million people across Laos, Vietnam, "
    "Thailand, southern China and Myanmar, with a large diaspora in the United States, France and "
    "Australia. Its two main dialects are White Hmong (Hmoob Dawb) and Green Hmong (Moob Ntsuab). "
    "Hmong is tonal with eight tones and is written in the RPA (Romanized Popular Alphabet), a Latin "
    "script created in the 1950s in which tone is marked by a final consonant letter. It is famous "
    "for its elaborate proverbs (paj lug) and paired poetic speech."
)

SCRIPT_DESC = (
    "Hmong is written in the RPA (Romanized Popular Alphabet), a Latin script developed in Laos in "
    "the 1950s. It uses the ordinary Latin letters with special digraphs: dl, hl, hm, hn, ml, nc, nd, "
    "nk, nq, nr, ny, pl, ts, tx, xy, plus the vowel digraphs aa, ee, oo. Tone is written with a final "
    "letter: b (high), j (high falling), v (rising), m (low creaky), s (low), g (falling breathy), d "
    "(low rising), and no letter (mid). There is also the Pahawh Hmong script, an indigenous writing "
    "system."
)

ALPHABET_NOTE = (
    "The RPA alphabet is phonetic once you learn the digraphs. The table shows the consonant clusters "
    "and tone letters that English readers must learn; single letters mostly match English."
)

ALPHABET_SAMPLE = [
    ("dl", "like 'tl'"), ("hl", "breathy 'l'"), ("hm", "voiceless 'm'"),
    ("nc", "'nts'"), ("tx", "aspirated 'ts'"), ("xy", "like 's' + 'y'"),
    ("b (final)", "high tone"), ("j (final)", "high falling tone"), ("v (final)", "rising tone"),
    ("m (final)", "low creaky tone"), ("s (final)", "low tone"), ("g (final)", "falling breathy tone"),
]

SOUNDS_DESC = (
    "Hmong has eight tones, and tone changes meaning: the same syllable with different tone letters "
    "is a different word. Vowels are pure and nasalized vowels (written with a following n, like 'ee' "
    "vs 'een') are common. Consonant clusters like ntx, npl and hm take practice — say the nasal "
    "first, then the release, in one smooth motion. White Hmong and Green Hmong differ mainly in "
    "pronunciation and some vocabulary; RPA writes both."
)

GRAMMAR_DESC = (
    "Hmong is subject-verb-object and isolating: words never change form. Tense and aspect come from "
    "helper words — tau (completed), yuav (future), tab tom (in progress), twb (already). There are no "
    "plurals, no articles, no conjugations. Classifiers count nouns: tus for people and animals, lub "
    "for round things, daim for flat things. Questions end with los, puas or nas depending on the "
    "question type. Negation uses tsis before the verb."
)

TENSE_DESC = (
    "Time floats on helper words around an unchanging verb. Kuv noj = 'I eat'; kuv yuav noj = 'I will "
    "eat'; kuv tau noj = 'I ate / have eaten'; kuv tab tom noj = 'I am eating'. The examples below "
    "hold the subject kuv (I) steady on three everyday verbs — noj (to eat), mus (to go), ua haujlwm "
    "(to work) — so you can watch only the helper words move."
)

REGISTER_DESC = (
    "Respect in Hmong is carried by kinship terms and careful speech. Elders are addressed by their "
    "relationship title, never by first name alone. Formal speech uses paired words and proverbs "
    "(paj lug); speaking plainly to an elder can sound blunt. Nyob zoo opens everything; ua tsaug "
    "thanks; thov softens requests. Speak gently, listen fully, and let elders finish — patience is "
    "the grammar of respect."
)

COMPLEX_DESC = (
    "Hmong links ideas with vim (because), tabsis (but), and thiaj (so that). Relative clauses follow "
    "the noun with uas: tus neeg uas ua haujlwm (the person who works). Conditions use yog (if). "
    "Hmong rhetoric loves parallelism — say a thing twice in paired words (paj lug style) and it "
    "lands twice as deep. Chain short clauses; the language breathes in couplets."
)

REVIEW_NOTE = (
    "You now hold the complete Hmong ladder: the RPA script with its digraphs and eight tone letters, "
    "tones and nasal vowels, isolating SVO grammar with helper words, core nouns verbs and adjectives, "
    "pronouns, numbers to one hundred, time words, greetings, ten themed sentence sets, the helper "
    "tenses, questions, commands, descriptions, three graded stories, paj lug proverbs, formal "
    "registers, and three full conversations. Mark every tone letter and the language sings."
)

NOUNS = [
    ("dej", "dej", "water", "Dej zoo.", "dej zoo", "The water is good."),
    ("mov", "mov", "rice, cooked food", "Mov zoo.", "mov zoo", "The rice is good."),
    ("tsev", "tsev", "house", "Tsev loj.", "tsev loj", "The house is big."),
    ("tsheb", "tsheb", "car", "Tsheb tshiab.", "tsheb tshiab", "The car is new."),
    ("phau ntawv", "phau ntawv", "book", "Phau ntawv zoo.", "phau ntawv zoo", "The book is good."),
    ("khw", "khw", "market", "Khw loj.", "khw loj", "The market is big."),
    ("tsev kawm ntawv", "tsev kawm ntawv", "school", "Tsev kawm ntawv zoo.", "tsev kawm ntawv zoo", "The school is good."),
    ("hnub", "hnub", "day, sun", "Hnub zoo.", "hnub zoo", "The day is good."),
    ("hmo", "hmo", "night", "Hmo zoo.", "hmo zoo", "The night is good."),
    ("txiv", "txiv", "father", "Txiv zoo.", "txiv zoo", "Father is good."),
    ("niam", "niam", "mother", "Niam zoo.", "niam zoo", "Mother is good."),
    ("kev hlub", "kev hlub", "love", "Kev hlub zoo.", "kev hlub zoo", "Love is good."),
]

VERBS = [
    ("noj", "noj", "to eat", "Noj zoo.", "noj zoo", "Eating is good."),
    ("haus", "haus", "to drink", "Haus zoo.", "haus zoo", "Drinking is good."),
    ("mus", "mus", "to go", "Mus zoo.", "mus zoo", "Going is good."),
    ("tuaj", "tuaj", "to come", "Tuaj zoo.", "tuaj zoo", "Coming is good."),
    ("hais", "hais", "to speak", "Hais zoo.", "hais zoo", "Speaking is good."),
    ("ua haujlwm", "ua haujlwm", "to work", "Ua haujlwm zoo.", "ua haujlwm zoo", "Working is good."),
    ("kawm", "kawm", "to learn", "Kawm zoo.", "kawm zoo", "Learning is good."),
    ("muab", "muab", "to give", "Muab zoo.", "muab zoo", "Giving is good."),
    ("hlub", "hlub", "to love", "Hlub zoo.", "hlub zoo", "Loving is good."),
    ("nyob", "nyob", "to live, to stay", "Nyob zoo.", "nyob zoo", "Living is good."),
]

ADJS = [
    ("zoo", "zoo", "good", "tsev zoo", "tsev zoo", "a good house"),
    ("phem", "phem", "bad", "tsheb phem", "tsheb phem", "a bad car"),
    ("loj", "loj", "big", "tsev loj", "tsev loj", "a big house"),
    ("me", "me", "small", "phau ntawv me", "phau ntawv me", "a small book"),
    ("tshiab", "tshiab", "new", "tsheb tshiab", "tsheb tshiab", "a new car"),
    ("qub", "qub", "old", "tsev qub", "tsev qub", "an old house"),
    ("liab", "liab", "red", "tsheb liab", "tsheb liab", "a red car"),
    ("dawb", "dawb", "white", "tsho dawb", "tsho dawb", "a white shirt"),
]

PRONOUNS = [
    ("kuv", "kuv", "I"),
    ("koj", "koj", "you (singular)"),
    ("nws", "nws", "he / she"),
    ("peb", "peb", "we (exclusive)"),
    ("neb", "neb", "you (plural)"),
    ("lawv", "lawv", "they"),
    ("qhov no", "qhov no", "this"),
    ("qhov ntawd", "qhov ntawd", "that"),
]

NUMBERS = [
    ("ib", "ib", "one"), ("ob", "ob", "two"), ("peb", "peb", "three"),
    ("plaub", "plaub", "four"), ("tsib", "tsib", "five"), ("rau", "rau", "six"),
    ("xya", "xya", "seven"), ("yim", "yim", "eight"),
    ("cuaj", "cuaj", "nine"), ("kaum", "kaum", "ten"),
    ("nees nkaum", "nees nkaum", "twenty"), ("pua", "pua", "one hundred"),
]

TIME_WORDS = [
    ("hnub no", "hnub no", "today"), ("tagkis", "tagkis", "tomorrow"),
    ("nag", "nag", "yesterday"), ("lim tiam", "lim tiam", "week"),
    ("hli", "hli", "month"), ("xyoo", "xyoo", "year"),
]

GREETINGS = [
    ("Nyob zoo!", "nyob zoo", "Hello!"),
    ("Nyob zoo!", "nyob zoo", "Goodbye! (same word)"),
    ("Koj nyob li cas?", "koj nyob li cas", "How are you?"),
    ("Kuv nyob zoo.", "kuv nyob zoo", "I am well. (reply)"),
    ("Ua tsaug.", "ua tsaug", "Thank you."),
    ("Ua tsaug ntau.", "ua tsaug ntau", "Thank you very much."),
    ("Thov.", "thov", "Please."),
    ("Thov txim.", "thov txim", "Sorry / excuse me."),
    ("Tsis ua li cas.", "tsis ua li cas", "You are welcome / no problem."),
    ("Sib ntsib dua.", "sib ntsib dua", "See you again."),
]
THEMES = [
    ("Home and Family", [
        ("tsev neeg", "tsev neeg", "family", "Tsev neeg zoo.", "tsev neeg zoo", "The family is good."),
        ("txiv", "txiv", "father", "Txiv ua haujlwm.", "txiv ua haujlwm", "Father works."),
        ("niam", "niam", "mother", "Niam ua mov.", "niam ua mov", "Mother cooks food."),
        ("tij", "tij", "older brother", "Tij pab.", "tij pab", "The older brother helps."),
        ("muam", "muam", "sister", "Muam kawm.", "muam kawm", "The sister learns."),
        ("kwv", "kwv", "younger brother", "Kwv ua si.", "kwv ua si", "The younger brother plays."),
    ]),
    ("Food and Cooking", [
        ("zaub mov", "zaub mov", "food", "Zaub mov qab.", "zaub mov qab", "The food is delicious."),
        ("mov", "mov", "rice", "Mov qab.", "mov qab", "The rice is delicious."),
        ("nqaij", "nqaij", "meat", "Nqaij kim.", "nqaij kim", "The meat is expensive."),
        ("dej", "dej", "water", "Dej zoo.", "dej zoo", "The water is good."),
        ("mis", "mis", "milk", "Mis zoo.", "mis zoo", "The milk is good."),
        ("tshuaj yej", "tshuaj yej", "tea", "Tshuaj yej zoo.", "tshuaj yej zoo", "The tea is good."),
    ]),
    ("Travel and Directions", [
        ("kev", "kev", "road", "Kev deb.", "kev deb", "The road is long."),
        ("tsheb", "tsheb", "car", "Tsheb mus.", "tsheb mus", "The car goes."),
        ("dav hlau", "dav hlau", "airplane", "Dav hlau ya.", "dav hlau ya", "The plane flies."),
        ("chaw nres tsheb", "chaw nres tsheb", "station", "Chaw nres tsheb nyob ze.", "chaw nres tsheb nyob ze", "The station is near."),
        ("sab xis", "sab xis", "right", "Mus sab xis.", "mus sab xis", "Go right."),
        ("sab laug", "sab laug", "left", "Mus sab laug.", "mus sab laug", "Go left."),
    ]),
    ("Work and School", [
        ("haujlwm", "haujlwm", "work", "Haujlwm zoo.", "haujlwm zoo", "The work is good."),
        ("tsev kawm ntawv", "tsev kawm ntawv", "school", "Tsev kawm ntawv qhib.", "tsev kawm ntawv qhib", "The school is open."),
        ("tub kawm", "tub kawm", "student", "Tub kawm kawm.", "tub kawm kawm", "The student learns."),
        ("xib hwb", "xib hwb", "teacher", "Xib hwb hais.", "xib hwb hais", "The teacher speaks."),
        ("phau ntawv", "phau ntawv", "book", "Phau ntawv kaw.", "phau ntawv kaw", "The book is closed."),
        ("cwj mem", "cwj mem", "pen", "Cwj mem zoo.", "cwj mem zoo", "The pen is good."),
    ]),
    ("Health and the Body", [
        ("cev", "cev", "body", "Cev zoo.", "cev zoo", "The body is good."),
        ("taub hau", "taub hau", "head", "Taub hau mob.", "taub hau mob", "The head aches."),
        ("qhov muag", "qhov muag", "eye", "Qhov muag pom.", "qhov muag pom", "The eye sees."),
        ("npab", "npab", "arm", "Npab mob.", "npab mob", "The arm aches."),
        ("ceg", "ceg", "leg", "Ceg mob.", "ceg mob", "The leg aches."),
        ("kws kho mob", "kws kho mob", "doctor", "Kws kho mob kho.", "kws kho mob kho", "The doctor heals."),
    ]),
    ("Emotions and Feelings", [
        ("kev zoo siab", "kev zoo siab", "joy", "Kev zoo siab zoo.", "kev zoo siab zoo", "Joy is good."),
        ("kev tu siab", "kev tu siab", "sadness", "Kev tu siab dhau.", "kev tu siab dhau", "The sadness is gone."),
        ("kev ntshai", "kev ntshai", "fear", "Kev ntshai dhau.", "kev ntshai dhau", "The fear is gone."),
        ("kev hlub", "kev hlub", "love", "Kev hlub loj.", "kev hlub loj", "Love is strong."),
        ("kev khib", "kev khib", "jealousy", "Kev khib phem.", "kev khib phem", "Jealousy is bad."),
        ("kev sib haum", "kev sib haum", "peace", "Kev sib haum zoo.", "kev sib haum zoo", "Peace is good."),
    ]),
    ("Nature and Weather", [
        ("ntuj", "ntuj", "nature, sky", "Ntuj zoo.", "ntuj zoo", "Nature is beautiful."),
        ("nag", "nag", "rain", "Nag los.", "nag los", "The rain is falling."),
        ("hnub", "hnub", "sun", "Hnub kub.", "hnub kub", "The sun is hot."),
        ("hli", "hli", "moon", "Hli ci.", "hli ci", "The moon is bright."),
        ("ntoo", "ntoo", "tree", "Ntoo loj.", "ntoo loj", "The tree is big."),
        ("paj", "paj", "flower", "Paj zoo.", "paj zoo", "The flower is beautiful."),
    ]),
    ("Shopping and Money", [
        ("nyiaj", "nyiaj", "money", "Nyiaj zoo.", "nyiaj zoo", "Money is good."),
        ("nqi", "nqi", "price", "Nqi kim.", "nqi kim", "The price is high."),
        ("khw", "khw", "shop, market", "Khw qhib.", "khw qhib", "The shop is open."),
        ("pheej yig", "pheej yig", "cheap", "Pheej yig zoo.", "pheej yig zoo", "Cheap is good."),
        ("tus yuav", "tus yuav", "customer", "Tus yuav zoo siab.", "tus yuav zoo siab", "The customer is happy."),
        ("tus muag", "tus muag", "seller", "Tus muag zoo.", "tus muag zoo", "The seller is good."),
    ]),
    ("Friendship and Social Life", [
        ("phooj ywg", "phooj ywg", "friend", "Phooj ywg zoo.", "phooj ywg zoo", "The friend is good."),
        ("kev tos txais", "kev tos txais", "hospitality", "Kev tos txais zoo.", "kev tos txais zoo", "Hospitality is good."),
        ("kev sib tham", "kev sib tham", "conversation", "Kev sib tham zoo.", "kev sib tham zoo", "The conversation is good."),
        ("noj haus", "noj haus", "feast", "Noj haus zoo.", "noj haus zoo", "The feast is good."),
        ("kev seev cev", "kev seev cev", "dance", "Kev seev cev zoo.", "kev seev cev zoo", "The dance is beautiful."),
        ("zaj nkauj", "zaj nkauj", "song", "Zaj nkauj zoo.", "zaj nkauj zoo", "The song is beautiful."),
    ]),
    ("Technology and Communication", [
        ("xov tooj", "xov tooj", "telephone", "Xov tooj nrov.", "xov tooj nrov", "The phone is ringing."),
        ("khoos phis tawj", "khoos phis tawj", "computer", "Khoos phis tawj ua haujlwm.", "khoos phis tawj ua haujlwm", "The computer is working."),
        ("is taws nem", "is taws nem", "internet", "Is taws nem ceev.", "is taws nem ceev", "The internet is fast."),
        ("hluav taws xob", "hluav taws xob", "electricity", "Muaj hluav taws xob.", "muaj hluav taws xob", "There is electricity."),
        ("lus", "lus", "message", "Lus tuaj.", "lus tuaj", "The message has arrived."),
        ("xov xwm", "xov xwm", "radio", "Xov xwm hais.", "xov xwm hais", "The radio is playing."),
    ]),
]

QUESTIONS = [
    ("Koj hu li cas?", "koj hu li cas", "What is your name?"),
    ("Niam nyob qhov twg?", "niam nyob qhov twg", "Where is mother?"),
    ("Nqi li cas?", "nqi li cas", "How much is this?"),
    ("Vim li cas?", "vim li cas", "Why?"),
    ("Thaum twg?", "thaum twg", "When?"),
    ("Leej twg no?", "leej twg no", "Who is this?"),
    ("Zaub mov li cas?", "zaub mov li cas", "How is the food?"),
    ("Koj tuaj qhov twg?", "koj tuaj qhov twg", "Where are you from?"),
]

COMMANDS = [
    ("Tuaj ntawm no!", "tuaj ntawm no", "Come here!"),
    ("Mus!", "mus", "Go!"),
    ("Zaum!", "zaum", "Sit down!"),
    ("Hais maj mam!", "hais maj mam", "Speak slowly!"),
    ("Pab kuv!", "pab kuv", "Help me!"),
    ("Mloog!", "mloog", "Listen!"),
    ("Saib!", "saib", "Look!"),
    ("Nres!", "nres", "Stop!"),
]

DESCRIBE = [
    ("Tus txiv neej siab, siab.", "tus txiv neej siab siab", "The tall man, he is tall."),
    ("Tus poj niam zoo nkauj, zoo nkauj.", "tus poj niam zoo nkauj zoo nkauj", "The beautiful woman, she is beautiful."),
    ("Lub tsev loj, loj.", "lub tsev loj loj", "The big house, it is big."),
    ("Lub tsheb liab, liab.", "lub tsheb liab liab", "The red car, it is red."),
    ("Tus me nyuam me, me.", "tus me nyuam me me", "The small child, he/she is small."),
    ("Phau ntawv tshiab, tshiab.", "phau ntawv tshiab tshiab", "The new book, it is new."),
    ("Hnub kub, kub.", "hnub kub kub", "The hot sun, it is hot."),
    ("Dej txias, txias.", "dej txias txias", "The cold water, it is cold."),
]

STORIES = [
    ("Story I: The Boy and the Goat", [
        ("Muaj ib tug tub.", "muaj ib tug tub", "There was a boy."),
        ("Tus tub muaj ib tug tshis.", "tus tub muaj ib tug tshis", "The boy has a goat."),
        ("Tus tshis dawb.", "tus tshis dawb", "The goat is white."),
        ("Tus tub hlub tus tshis.", "tus tub hlub tus tshis", "The boy loves the goat."),
        ("Ib hnub tus tshis ploj.", "ib hnub tus tshis ploj", "One day the goat got lost."),
        ("Tus tub nrhiav txhua qhov.", "tus tub nrhiav txhua qhov", "The boy searched everywhere."),
        ("Thaum kawg nws nrhiav tau.", "thaum kawg nws nrhiav tau", "Finally he found it."),
        ("Nws zoo siab heev.", "nws zoo siab heev", "He was very happy."),
    ]),
    ("Story II: The Rainy Day", [
        ("Hnub no nag los.", "hnub no nag los", "Today the rain is falling."),
        ("Cov me nyuam nyob hauv tsev.", "cov me nyuam nyob hauv tsev", "The children stay in the house."),
        ("Niam ua zaub mov.", "niam ua zaub mov", "Mother is cooking food."),
        ("Zaub mov qab.", "zaub mov qab", "The food is delicious."),
        ("Txiv nyeem ntawv.", "txiv nyeem ntawv", "Father is reading a book."),
        ("Nag dhau hnub tuaj.", "nag dhau hnub tuaj", "After the rain the sun came out."),
        ("Cov me nyuam tawm mus.", "cov me nyuam tawm mus", "The children went outside."),
        ("Lawv ua si hauv vaj.", "lawv ua si hauv vaj", "They are playing in the yard."),
    ]),
    ("Story III: The Market Trip", [
        ("Tagkis peb mus khw.", "tagkis peb mus khw", "Tomorrow we go to the market."),
        ("Niam yuav mov.", "niam yuav mov", "Mother buys rice."),
        ("Txiv yuav nqaij.", "txiv yuav nqaij", "Father buys meat."),
        ("Me nyuam yuav khoom qab zib.", "me nyuam yuav khoom qab zib", "The child buys candy."),
        ("Mov qab.", "mov qab", "The rice is delicious."),
        ("Nqaij kim.", "nqaij kim", "The meat is expensive."),
        ("Peb sawv daws mus tsev.", "peb sawv daws mus tsev", "We all go home."),
        ("Peb sawv daws noj zoo.", "peb sawv daws noj zoo", "We all eat well."),
    ]),
]

IDIOMS = [
    ("Ua ruam thiaj txawj zov tsev, tsab ntse thiaj tau ua qhev", "ua ruam thiaj txawj zov tsev, tsab ntse thiaj tau ua qhev", "Act unintelligent to have time to build your home; act smart and you work like a slave", "Humility protects; showing off enslaves."),
    ("Suab neeg nrov dua suab xob, lus phem ntsim dua kua txob", "suab neeg nrov dua suab xob, lus phem ntsim dua kua txob", "People's voices are louder than thunder; hurtful words are hotter than chilies", "Words wound deeper than storms."),
    ("Tsis noj ces yuav tshaib plab, tsis yuav kwv yuav tij ces yuav poob dab", "tsis noj ces yuav tshaib plab, tsis yuav kwv yuav tij ces yuav poob dab", "If you do not eat you will hunger; if you reject kin you will lose the ancestors", "Honor food and family alike."),
    ("Kaum leej tsom, tsis cuag yus qhov muag pom", "kaum leej tsom, tsis cuag yus qhov muag pom", "Ten people watching cannot match your own eyes seeing", "See for yourself; believe your own eyes."),
]

CONVOS = [
    ("At the Market", [
        ("A", "Nyob zoo!", "nyob zoo", "Hello!"),
        ("B", "Nyob zoo! Yuav dab tsi?", "nyob zoo yuav dab tsi", "Hello! What are you buying?"),
        ("A", "Nqi li cas?", "nqi li cas", "How much is this?"),
        ("B", "Kaum txhiab.", "kaum txhiab", "Ten thousand."),
        ("A", "Kim.", "kim", "Expensive."),
        ("B", "Pheej yig tau.", "pheej yig tau", "It can be cheaper."),
        ("A", "Ua tsaug, kuv yuav.", "ua tsaug kuv yuav", "Thanks, I will buy."),
        ("B", "Nyob zoo!", "nyob zoo", "Goodbye!"),
    ]),
    ("Meeting a Friend", [
        ("A", "Nyob zoo, koj nyob li cas?", "nyob zoo koj nyob li cas", "Hi, how are you?"),
        ("B", "Kuv nyob zoo, ua tsaug. Koj ne?", "kuv nyob zoo ua tsaug koj ne", "I am well, thanks. And you?"),
        ("A", "Kuv nyob zoo thiab.", "kuv nyob zoo thiab", "I am well too."),
        ("B", "Koj hu li cas?", "koj hu li cas", "What is your name?"),
        ("A", "Kuv hu Maiv.", "kuv hu maiv", "My name is Mai."),
        ("B", "Zoo siab ntsib koj.", "zoo siab ntsib koj", "Nice to meet you."),
        ("A", "Kuv zoo siab thiab.", "kuv zoo siab thiab", "Nice to meet you too."),
        ("B", "Sib ntsib dua!", "sib ntsib dua", "See you again!"),
    ]),
    ("Solving a Problem", [
        ("A", "Muaj teeb meem.", "muaj teeb meem", "There is a problem."),
        ("B", "Teeb meem dab tsi?", "teeb meem dab tsi", "What problem?"),
        ("A", "Tsheb tawg.", "tsheb tawg", "The car broke down."),
        ("B", "Tsis txhob txhawj.", "tsis txhob txhawj", "Do not worry."),
        ("A", "Pab kuv!", "pab kuv", "Help me!"),
        ("B", "Kuv yuav pab.", "kuv yuav pab", "I will help."),
        ("A", "Ua tsaug ntau!", "ua tsaug ntau", "Thank you very much!"),
        ("B", "Tsis ua li cas.", "tsis ua li cas", "You are welcome."),
    ]),
]

CITATIONS = [
    "UC Davis Hmong History and Cultural Studies Model Curriculum. Hmong Worldview through Oral Traditions: paj lug examples.",
    "Johnson M. Mong Leng - English Dictionary, revised.",
    "Heimbach E. White Hmong - English Dictionary. Cornell Southeast Asia Program; 1979.",
    "ISO 639-3:2007 language code hmn.",
    "Standard pedagogical sources for Hmong (RPA) vocabulary, tones, usage, and phraseology.",
]
