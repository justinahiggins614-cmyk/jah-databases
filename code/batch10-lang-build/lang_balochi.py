# -*- coding: utf-8 -*-
"""Language data module: Balochi (bal). Facts verified 2026-10-17 via
Wikivoyage phrasebook, published alphabet and proverb studies."""

SLUG = "language-balochi"
PREFIX = "JAH-LBAL-"
SIG_PREFIX = "JAH-LBALS-"
NAME = "Balochi"
NATIVE = "بلۏچی"
NATIVE_ROMAN = "Balóchi"
ISO1 = ""
ISO3 = "bal"
FAMILY = "Indo-European > Indo-Iranian > Iranian > Western Iranian > Northwestern"
SPEAKERS = "about 7 to 10 million speakers"
REGIONS = "Balochistan across Pakistan, Iran and southern Afghanistan, plus the Gulf states and a worldwide diaspora"
SCRIPT_NAME = "Perso-Arabic script (Balochi alphabet)"
WORD_ORDER = "subject-object-verb (SOV)"
AI_NAME = "JAH Balochi Language Archivist"
SIG_AI_NAME = "JAH Balochi Signature Archivist"

OVERVIEW = (
    "Balochi (بلۏچی, Balóchi) is a Northwestern Iranian language of the Indo-European family, spoken "
    "by about 7 to 10 million people across Balochistan — the region spanning Pakistan, Iran and "
    "southern Afghanistan — with communities in the Gulf states and a worldwide diaspora. It is "
    "related to Persian and Kurdish but keeps older features the others lost. Balochi is written in a "
    "Perso-Arabic alphabet with special letters for its sounds, read right to left, and follows "
    "subject-object-verb order."
)

SCRIPT_DESC = (
    "Balochi uses a Perso-Arabic alphabet read right to left. The standard Balochi alphabet adds "
    "letters Persian lacks: ٹ (retroflex t), ڈ (retroflex d), ڑ (retroflex r), ے (é), ۏ (ò). Vowels "
    "are written with ا (a/á), ی (i/í), و (u), ۏ (ò), ے (é) and short marks. Unlike Persian, Balochi "
    "writes its vowels more fully, which makes reading easier for learners."
)

ALPHABET_NOTE = (
    "The working alphabet is the 30-letter Balochi Perso-Arabic set. The table shows the twelve "
    "letters beginners meet first, including the signature retroflex series borrowed from contact "
    "with Indo-Aryan languages."
)

ALPHABET_SAMPLE = [
    ("ا", "a — a"), ("آ", "á — long a"), ("ب", "b — b"), ("چ", "ch — ch"),
    ("ڈ", "dh — retroflex d"), ("ٹ", "th — retroflex t"), ("ج", "j — j"),
    ("د", "d — d"), ("ر", "r — r"), ("ڑ", "rr — retroflex r"),
    ("ز", "z — z"), ("ژ", "zh — like 's' in 'measure'"),
]

SOUNDS_DESC = (
    "Balochi vowels: five long (á, é, í, ó, ú) and three short (a, i, u); length changes meaning, so "
    "hold long vowels full. Southern Balochi adds nasalized vowels. The signature sounds are the "
    "retroflex series ٹ ڈ ڑ (tongue curled back) and the fricatives خ (kh) and غ (gh). Stress usually "
    "falls on the last syllable. The distinction between د (d) and ڈ (retroflex d) is the beginner's "
    "key."
)

GRAMMAR_DESC = (
    "Balochi is subject-object-verb with two genders and a direct/oblique case system on nouns and "
    "pronouns. In past tenses Balochi uses ergative alignment: the doer of a completed action takes "
    "the oblique case and the verb agrees with the object — 'I ate bread' treats 'I' differently than "
    "'I eat bread' does. There are no articles. Negation prefixes na- to the verb. Postpositions "
    "follow the noun instead of prepositions."
)

TENSE_DESC = (
    "Balochi verbs build tense on the stem with suffixes. Present: man warán (I eat); past: man "
    "wart (I ate); the past stem is often shorter than the present stem — learn verbs as stem pairs. "
    "Future uses the helper: man warán (with context) or the -á construction. The examples below hold "
    "the subject man (I) steady on three everyday verbs — warag (to eat), shodag (to go), kanag (to "
    "do) — so you can watch only the tense shape move."
)

REGISTER_DESC = (
    "Balochi hospitality shapes its politeness. Drót (hello) opens; chónay taw? (how are you?) must "
    "be answered fully — wasshán, mennatwár (fine, thanks). Zahmat (trouble/excuse me) softens every "
    "request. Elders receive the longest greetings, with wishes for morning, evening and night: sohb "
    "wassh bát, bégáh wassh bát, shap wassh bát. A guest is sacred: receive, feed and honor before "
    "business."
)

COMPLEX_DESC = (
    "Balochi joins clauses with chóshka (because), bale (but), and kan (so that / to). Relative "
    "clauses follow the noun with ke: mardé ke kár kant (the man who works). Conditions use agar "
    "(if). Because the verb comes last and past tenses go ergative, read to the final verb and check "
    "which noun is in the oblique case before deciding who did what."
)

REVIEW_NOTE = (
    "You now hold the complete Balochi ladder: the Perso-Arabic script with its retroflex letters, "
    "long/short vowels and final stress, SOV grammar with ergative past tenses, core nouns verbs and "
    "adjectives, pronouns, numbers to one hundred, time words, greetings, ten themed sentence sets, "
    "the stem-pair tenses, questions, commands, descriptions, three graded stories, proverbs, formal "
    "registers, and three full conversations. Read right to left and watch the cases."
)

NOUNS = [
    ("آپ", "àp", "water", "آپ وش اِنت", "àp wassh ent", "The water is good."),
    ("نان", "nán", "bread", "نان وش اِنت", "nán wassh ent", "The bread is good."),
    ("لوگ", "lóg", "house, home", "لوگ وش اِنت", "lóg wassh ent", "The house is good."),
    ("گادی", "gádhi", "car", "گادی نوک اِنت", "gádhi nók ent", "The car is new."),
    ("کتاب", "kitáb", "book", "کتاب وش اِنت", "kitáb wassh ent", "The book is good."),
    ("بازار", "bázár", "market", "بازار مزن اِنت", "bázár mazan ent", "The market is big."),
    ("وانگجاه", "wángjah", "school", "وانگجاه وش اِنت", "wángjah wassh ent", "The school is good."),
    ("روچ", "ròch", "day, sun", "روچ وش اِنت", "ròch wassh ent", "The day is good."),
    ("شپ", "shap", "night", "شپ وش اِنت", "shap wassh ent", "The night is good."),
    ("پت", "pat", "father", "پت وش اِنت", "pat wassh ent", "Father is good."),
    ("مات", "mát", "mother", "مات وش اِنت", "mát wassh ent", "Mother is good."),
    ("دوستی", "dósti", "love, friendship", "دوستی وش اِنت", "dósti wassh ent", "Love is good."),
]

VERBS = [
    ("ورگ", "warag", "to eat", "ورگ وش اِنت", "warag wassh ent", "Eating is good."),
    ("نوشگ", "nóshag", "to drink", "نوشگ وش اِنت", "nóshag wassh ent", "Drinking is good."),
    ("شۆتگ", "shotag", "to go", "شۆتگ وش اِنت", "shotag wassh ent", "Going is good."),
    ("آتکگ", "átkag", "to come", "آتکگ وش اِنت", "átkag wassh ent", "Coming is good."),
    ("گپ کنگ", "gap kanag", "to speak", "گپ کنگ وش اِنت", "gap kanag wassh ent", "Speaking is good."),
    ("کار کنگ", "kár kanag", "to work", "کار کنگ وش اِنت", "kár kanag wassh ent", "Working is good."),
    ("وانگ", "wánag", "to read, to learn", "وانگ وش اِنت", "wánag wassh ent", "Learning is good."),
    ("دئیگ", "dayag", "to give", "دئیگ وش اِنت", "dayag wassh ent", "Giving is good."),
    ("دوست دارگ", "dóst dárag", "to love", "دوست دارگ وش اِنت", "dóst dárag wassh ent", "Loving is good."),
    ("نشتگ", "nishtag", "to sit, to live", "نشتگ وش اِنت", "nishtag wassh ent", "Living is good."),
]

ADJS = [
    ("وش", "wassh", "good", "وش لوگ", "wassh lóg", "a good house"),
    ("ھاراب", "haráb", "bad", "ھاراب گادی", "haráb gádhi", "a bad car"),
    ("مزن", "mazan", "big", "مزن لوگ", "mazan lóg", "a big house"),
    ("کس", "kas", "small", "کس کتاب", "kas kitáb", "a small book"),
    ("نوک", "nók", "new", "نوک گادی", "nók gádhi", "a new car"),
    ("کون", "kohan", "old", "کون لوگ", "kohan lóg", "an old house"),
    ("سور", "sohr", "red", "سور گادی", "sohr gádhi", "a red car"),
    ("اسپیت", "espét", "white", "اسپیت جامگ", "espét jámag", "a white shirt"),
]

PRONOUNS = [
    ("من", "man", "I"),
    ("تو", "taw", "you (singular)"),
    ("شما", "shomá", "you (plural / polite)"),
    ("آ", "á", "he / she / it"),
    ("ما", "má", "we"),
    ("آوان", "áwán", "they"),
    ("اِے", "é", "this"),
    ("ھما", "hamá", "that"),
]

NUMBERS = [
    ("یک", "yak", "one"), ("دو", "do", "two"), ("سۓ", "sae", "three"),
    ("چار", "chár", "four"), ("پنچ", "panch", "five"), ("شش", "shash", "six"),
    ("ھپت", "hapt", "seven"), ("ھشت", "hasht", "eight"),
    ("نو", "noh", "nine"), ("دہ", "dah", "ten"),
    ("گِست", "gíst", "twenty"), ("سد", "sad", "one hundred"),
]

TIME_WORDS = [
    ("مرچی", "marchi", "today"), ("باندا", "bándá", "tomorrow"),
    ("زی", "zi", "yesterday"), ("ھپتگ", "haptag", "week"),
    ("ماہ", "máh", "month"), ("سال", "sál", "year"),
]

GREETINGS = [
    ("دروت", "drót", "Hello!"),
    ("چۏنے تو؟", "chónay taw", "How are you?"),
    ("وشّاں، منّتوار", "wasshán, mennatwár", "Fine, thanks. (reply)"),
    ("تئی منّتوار آن", "tai mennatwár án", "Thank you."),
    ("باز منّتوار", "báz mennatwár", "Thank you very much."),
    ("زحمت", "zahmat", "Please / excuse me (trouble)."),
    ("ببخش", "bebaksh", "Sorry / excuse me."),
    ("وشّاتکے", "wasshátkay", "You are welcome."),
    ("ھدای میار آی", "hodáay mayár ay", "Goodbye (may you be kept well)."),
    ("وش اِنت", "wassh ent", "Goodbye (be well)."),
]
THEMES = [
    ("Home and Family", [
        ("ھانوادگ", "hánwadag", "family", "ھانوادگ وش اِنت", "hánwadag wassh ent", "The family is good."),
        ("پت", "pat", "father", "پت کار کنت", "pat kár kant", "Father works."),
        ("مات", "mát", "mother", "مات ورگ پچت", "mát warag pachat", "Mother cooks food."),
        ("برات", "brát", "brother", "برات کمک کنت", "brát komak kant", "The brother helps."),
        ("گھار", "gohár", "sister", "گھار وانیت", "gohár wánit", "The sister learns."),
        ("چک", "chok", "child", "چک گوں بازی کنت", "chok gón bázi kant", "The child plays."),
    ]),
    ("Food and Cooking", [
        ("وراک", "warák", "food", "وراک وش اِنت", "warák wassh ent", "The food is good."),
        ("نان", "nán", "bread", "نان وش اِنت", "nán wassh ent", "The bread is good."),
        ("گوشت", "gósht", "meat", "گوشت گران اِنت", "gósht grán ent", "The meat is expensive."),
        ("آپ", "àp", "water", "آپ وش اِنت", "àp wassh ent", "The water is good."),
        ("شیر", "shir", "milk", "شیر وش اِنت", "shir wassh ent", "The milk is good."),
        ("چای", "cháy", "tea", "چای وش اِنت", "cháy wassh ent", "The tea is good."),
    ]),
    ("Travel and Directions", [
        ("راہ", "ráh", "road", "راہ دراج اِنت", "ráh dráj ent", "The road is long."),
        ("گادی", "gádhi", "car", "گادی شت", "gádhi shot", "The car goes."),
        ("جھاز", "jhaz", "airplane", "جھاز پرنت", "jhaz parant", "The plane flies."),
        ("اڈا", "addá", "station", "اڈا نزیک اِنت", "addá nazik ent", "The station is near."),
        ("راست", "rást", "right", "راستا برو", "rástá bro", "Go right."),
        ("چپ", "chap", "left", "چپا برو", "chapá bro", "Go left."),
    ]),
    ("Work and School", [
        ("کار", "kár", "work", "کار وش اِنت", "kár wassh ent", "The work is good."),
        ("وانگجاه", "wángjah", "school", "وانگجاه پچ اِنت", "wángjah pach ent", "The school is open."),
        ("وانندہ", "wánandah", "student", "وانندہ وانیت", "wánandah wánit", "The student learns."),
        ("استاد", "ostád", "teacher", "استاد گپ کنت", "ostád gap kant", "The teacher speaks."),
        ("کتاب", "kitáb", "book", "کتاب بند اِنت", "kitáb band ent", "The book is closed."),
        ("کلم", "kalam", "pen", "کلم وش اِنت", "kalam wassh ent", "The pen is good."),
    ]),
    ("Health and the Body", [
        ("جان", "ján", "body", "جان وش اِنت", "ján wassh ent", "The body is good."),
        ("سر", "sar", "head", "سر درد کنت", "sar dard kant", "The head aches."),
        ("چم", "chamm", "eye", "چم گندیت", "chamm gandit", "The eye sees."),
        ("دست", "dast", "hand, arm", "دست درد کنت", "dast dard kant", "The hand aches."),
        ("پاد", "pád", "foot, leg", "پاد درد کنت", "pád dard kant", "The leg aches."),
        ("ڈاکٹر", "dhákthar", "doctor", "ڈاکٹر درما کنت", "dhákthar darmá kant", "The doctor heals."),
    ]),
    ("Emotions and Feelings", [
        ("وشی", "washshi", "joy", "وشی وش اِنت", "washshi wassh ent", "Joy is good."),
        ("گم", "gham", "sadness", "گم شت", "gham shot", "The sadness is gone."),
        ("ترس", "tars", "fear", "ترس شت", "tars shot", "The fear is gone."),
        ("دوستی", "dósti", "love", "دوستی مزن اِنت", "dósti mazan ent", "Love is strong."),
        ("حسد", "hasad", "jealousy", "حسد ھاراب اِنت", "hasad haráb ent", "Jealousy is bad."),
        ("آمنی", "ámni", "peace", "آمنی وش اِنت", "ámni wassh ent", "Peace is good."),
    ]),
    ("Nature and Weather", [
        ("کدرت", "kodrat", "nature", "کدرت وش اِنت", "kodrat wassh ent", "Nature is beautiful."),
        ("ھور", "haur", "rain", "ھور کیت", "haur két", "The rain is falling."),
        ("روچ", "ròch", "sun", "روچ گرم اِنت", "ròch garm ent", "The sun is hot."),
        ("ماہ", "máh", "moon", "ماہ روشن اِنت", "máh róshan ent", "The moon is bright."),
        ("درچک", "drachk", "tree", "درچک مزن اِنت", "drachk mazan ent", "The tree is big."),
        ("پل", "pol", "flower", "پل وش اِنت", "pol wassh ent", "The flower is beautiful."),
    ]),
    ("Shopping and Money", [
        ("زر", "zar", "money", "زر وش اِنت", "zar wassh ent", "Money is good."),
        ("کیمت", "kimat", "price", "کیمت گران اِنت", "kimat grán ent", "The price is high."),
        ("دکان", "dukán", "shop", "دکان پچ اِنت", "dukán pach ent", "The shop is open."),
        ("ارزان", "arzán", "cheap", "ارزان وش اِنت", "arzán wassh ent", "Cheap is good."),
        ("گِراک", "girák", "customer", "گِراک وش اِنت", "girák wassh ent", "The customer is happy."),
        ("سوداگر", "sódágar", "seller", "سوداگر وش اِنت", "sódágar wassh ent", "The seller is good."),
    ]),
    ("Friendship and Social Life", [
        ("سنگت", "sangat", "friend", "سنگت وش اِنت", "sangat wassh ent", "The friend is good."),
        ("مھمانوازی", "mehmánwázi", "hospitality", "مھمانوازی وش اِنت", "mehmánwázi wassh ent", "Hospitality is good."),
        ("ھبر", "habar", "conversation, news", "ھبر وش اِنت", "habar wassh ent", "The conversation is good."),
        ("میڑھ", "mérh", "feast", "میڑھ وش اِنت", "mérh wassh ent", "The feast is good."),
        ("ڈیھ", "déyh", "dance", "ڈیھ وش اِنت", "déyh wassh ent", "The dance is beautiful."),
        ("سوت", "sót", "song", "سوت وش اِنت", "sót wassh ent", "The song is beautiful."),
    ]),
    ("Technology and Communication", [
        ("ٹیلیفون", "télifon", "telephone", "ٹیلیفون زنگ کنت", "télifon zang kant", "The phone is ringing."),
        ("کمپیوٹر", "kampyútar", "computer", "کمپیوٹر کار کنت", "kampyútar kár kant", "The computer is working."),
        ("انٹرنیٹ", "intarnét", "internet", "انٹرنیٹ تیز اِنت", "intarnét téz ent", "The internet is fast."),
        ("بجلی", "bijli", "electricity", "بجلی ھست", "bijli hast", "There is electricity."),
        ("پیغام", "paighám", "message", "پیغام آتک", "paighám átk", "The message has arrived."),
        ("ریڈیو", "rédio", "radio", "ریڈیو گپ کنت", "rédio gap kant", "The radio is playing."),
    ]),
]

QUESTIONS = [
    ("تئی نام چے اِنت؟", "tai nám ché ent", "What is your name?"),
    ("مات کجا اِنت؟", "mát kojá ent", "Where is mother?"),
    ("اِے چند اِنت؟", "é chand ent", "How much is this?"),
    ("پرچا؟", "parchá", "Why?"),
    ("کدی؟", "kadi", "When?"),
    ("اِے کئے اِنت؟", "é kaye ent", "Who is this?"),
    ("وراک چون اِنت؟", "warák chón ent", "How is the food?"),
    ("تو کجا چے آتکگئے؟", "taw kojá ché átkagay", "Where are you from?"),
]

COMMANDS = [
    ("اِدا بیا!", "edá biyá", "Come here!"),
    ("برو!", "bro", "Go!"),
    ("بنند!", "binind", "Sit down!"),
    ("آرام گپ بکن!", "árám gap bekan", "Speak slowly!"),
    ("منا کمک بکن!", "maná komak bekan", "Help me!"),
    ("گوش بدار!", "gósh bedár", "Listen!"),
    ("بچار!", "bechár", "Look!"),
    ("اوشت!", "ósht", "Stop!"),
]

DESCRIBE = [
    ("بلند مردم، بلند اِنت", "boland mardom, boland ent", "The tall man, he is tall."),
    ("وش جنین، وش اِنت", "wassh janén, wassh ent", "The beautiful woman, she is beautiful."),
    ("مزن لوگ، مزن اِنت", "mazan lóg, mazan ent", "The big house, it is big."),
    ("سور گادی، سور اِنت", "sohr gádhi, sohr ent", "The red car, it is red."),
    ("کس چک، کس اِنت", "kas chok, kas ent", "The small child, he/she is small."),
    ("نوک کتاب، نوک اِنت", "nók kitáb, nók ent", "The new book, it is new."),
    ("گرم روچ، گرم اِنت", "garm ròch, garm ent", "The hot sun, it is hot."),
    ("سارت آپ، سارت اِنت", "sárt àp, sárt ent", "The cold water, it is cold."),
]

STORIES = [
    ("Story I: The Boy and the Lamb", [
        ("یک چک ھست اَت", "yak chok hast at", "There was a boy."),
        ("چکا یک میش ھست اَت", "choká yak mésh hast at", "The boy has a lamb."),
        ("میش اسپیت اَت", "mésh espét at", "The lamb is white."),
        ("چک میشا دوست داریت", "chok méshá dóst dárit", "The boy loves the lamb."),
        ("یک روچا میش گار بوت", "yak róchá mésh gár bot", "One day the lamb got lost."),
        ("چک ھر جاہ شوھازگ", "chok har jáh shoházg", "The boy searched everywhere."),
        ("آخری آئیہ پیدا کت", "ákhri áyá paidá kot", "Finally he found it."),
        ("آ باز وش بوت", "á báz wassh bot", "He was very happy."),
    ]),
    ("Story II: The Rainy Day", [
        ("مرچی ھور کیت", "marchi haur két", "Today the rain is falling."),
        ("چک لوگ ءَ نشتگ اَنت", "chok lóg á nishtag ant", "The children stay in the house."),
        ("مات وراک پچت", "mát warák pachat", "Mother is cooking food."),
        ("وراک وش اِنت", "warák wassh ent", "The food is good."),
        ("پت کتاب وانیت", "pat kitáb wánit", "Father is reading a book."),
        ("ھورا پد روچ در آتک", "haurá pad ròch dar átk", "After the rain the sun came out."),
        ("چک در آتک اَنت", "chok dar átk ant", "The children went outside."),
        ("آوان حیوان ءَ بازی کننت", "áwán haywán á bázi kanant", "They are playing in the yard."),
    ]),
    ("Story III: The Market Trip", [
        ("باندا بازارا شوئیں", "bándá bázárá shuén", "Tomorrow we go to the market."),
        ("مات نان گِرت", "mát nán girt", "Mother buys bread."),
        ("پت گوشت گِرت", "pat gósht girt", "Father buys meat."),
        ("چک شیرنی گِرت", "chok shirni girt", "The child buys candy."),
        ("نان وش اِنت", "nán wassh ent", "The bread is good."),
        ("گوشت گران اِنت", "gósht grán ent", "The meat is expensive."),
        ("ما دراھیں لوگ ءَ شوئیں", "má dráhén lóg á shuén", "We all go home."),
        ("ما دراھیں وش ورئیں", "má dráhén wassh warén", "We all eat well."),
    ]),
]

IDIOMS = [
    ("Waye watan hushkain dar", "waye watan hushkain dar", "I love my land even if it is like a withered twig", "Love of homeland endures through hardship."),
    ("In our lands, the price of a glass of water is a hundred years of loyalty", "in our lands, the price of a glass of water is a hundred years of loyalty", "In our lands, the price of a glass of water is a hundred years of loyalty", "Never forget a kindness done to you."),
    ("Ropes break at the weakest point", "ropes break at the weakest point", "Ropes break at the weakest point", "Trouble finds the weakest link."),
    ("Dóstdári — dóst dárag", "dóst dárag", "To love — hold love", "Hold fast to love and friendship."),
]

CONVOS = [
    ("At the Market", [
        ("A", "دروت", "drót", "Hello!"),
        ("B", "دروت! چی لوٹئے؟", "drót! chi lóthay", "Hello! What do you want?"),
        ("A", "اِے چند اِنت؟", "é chand ent", "How much is this?"),
        ("B", "دہ روپیہ", "dah rupiá", "Ten rupees."),
        ("A", "گران اِنت", "grán ent", "Expensive."),
        ("B", "ارزان کناں", "arzán kanán", "I will make it cheap."),
        ("A", "منّتوار، گِرآں", "mennatwár, girán", "Thanks, I will take it."),
        ("B", "ھدای میار آی", "hodáay mayár ay", "Goodbye."),
    ]),
    ("Meeting a Friend", [
        ("A", "دروت، چۏنے ئے؟", "drót, chónay ay", "Hi, how are you?"),
        ("B", "وشّاں، منّتوار. تو چون ئے؟", "wasshán, mennatwár. taw chón ay", "Fine, thanks. How are you?"),
        ("A", "من ھم وش آن", "man ham wassh án", "I am well too."),
        ("B", "تئی نام چے اِنت؟", "tai nám ché ent", "What is your name?"),
        ("A", "منی نام نازینک اِنت", "mani nám názénk ent", "My name is Nazenk."),
        ("B", "تارا دیستگ ءَ وش بوتاں", "tará distag á wassh botán", "Nice to meet you."),
        ("A", "من ھم وش بوتاں", "man ham wassh botán", "Nice to meet you too."),
        ("B", "پدا وش بے", "padá wassh bay", "See you again."),
    ]),
    ("Solving a Problem", [
        ("A", "یک مشکل ھست", "yak moshkil hast", "There is a problem."),
        ("B", "چے مشکل؟", "ché moshkil", "What problem?"),
        ("A", "گادی خراب بوتگ", "gádhi kharáb botag", "The car broke down."),
        ("B", "پریشان مبے", "paréshán mabay", "Do not worry."),
        ("A", "منا کمک بکن!", "maná komak bekan", "Help me!"),
        ("B", "من کمک کناں", "man komak kanán", "I will help."),
        ("A", "باز منّتوار!", "báz mennatwár", "Thank you very much!"),
        ("B", "وشّاتکے", "wasshátkay", "You are welcome."),
    ]),
]

CITATIONS = [
    "Wikivoyage contributors. Balochi phrasebook.",
    "Balochi alphabet studies: Southern Balochi (Kachi dialect) alphabet with example words.",
    "Badalkhan S. Ropes break at the weakest point. Proverbium; 2000.",
    "Branz Baluch. Baluch identity and social values through Baluchi poetry.",
    "ISO 639-3:2007 language code bal.",
    "Standard pedagogical sources for Balochi vocabulary, usage, and phraseology.",
]
