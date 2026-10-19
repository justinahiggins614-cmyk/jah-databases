# -*- coding: utf-8 -*-
"""Language data module: Uyghur (uig). Facts verified 2026-10-17 via
Uyghur dictionary lessons, academic vocabulary sources."""

SLUG = "language-uyghur"
PREFIX = "JAH-LUIG-"
SIG_PREFIX = "JAH-LUIGS-"
NAME = "Uyghur"
NATIVE = "ئۇيغۇرچە"
NATIVE_ROMAN = "Uyghurche"
ISO1 = ""
ISO3 = "uig"
FAMILY = "Turkic > Karluk (Southeastern Turkic)"
SPEAKERS = "about 10 to 13 million speakers"
REGIONS = "the Xinjiang Uyghur Autonomous Region of China, plus Kazakhstan, Kyrgyzstan, Uzbekistan and a worldwide diaspora"
SCRIPT_NAME = "modified Perso-Arabic script"
WORD_ORDER = "subject-object-verb (SOV)"
AI_NAME = "JAH Uyghur Language Archivist"
SIG_AI_NAME = "JAH Uyghur Signature Archivist"

OVERVIEW = (
    "Uyghur (ئۇيغۇرچە, Uyghurche) is a Turkic language of the Karluk branch, spoken by about 10 to 13 "
    "million people, most of them in the Xinjiang Uyghur Autonomous Region of China, with communities "
    "across Central Asia and a worldwide diaspora. It descends from Chaghatay Turki, the literary "
    "language of Central Asia, and carries centuries of Arabic and Persian loanwords. In China it is "
    "written in a modified Perso-Arabic script read right to left; outside China the Latin-based "
    "Uyghur Latin script is also used. Like all Turkic languages it is agglutinative and follows "
    "vowel harmony."
)

SCRIPT_DESC = (
    "Uyghur in China is written in a modified Arabic script of 32 letters, read right to left. Unlike "
    "Arabic, it writes all vowels explicitly: ا (a), ە (e), ئى (i), و (o/u), ۇ (u), ۆ (ö), ۈ (ü). "
    "The script was reformed several times in the 20th century. Learners should learn the isolated, "
    "initial, medial and final shapes of each letter — the table below gives the isolated form, the "
    "name, and the sound."
)

ALPHABET_NOTE = (
    "The 32-letter Perso-Arabic alphabet writes every vowel, which makes reading easier than Arabic "
    "itself. The table shows twelve key letters: the eight vowel letters first, then four signature "
    "consonants."
)

ALPHABET_SAMPLE = [
    ("ا", "a — a"), ("ە", "e — e"), ("ئى", "i — i"), ("و", "o — o"),
    ("ۇ", "u — u"), ("ۆ", "ö — ö"), ("ۈ", "ü — ü"), ("ې", "é — e"),
    ("ق", "q — q"), ("غ", "gh — gh"), ("خ", "x — kh"), ("ھ", "h — h"),
]

SOUNDS_DESC = (
    "Uyghur has 8 vowels (a, e, i, o, u, ö, ü, é) governed by vowel harmony: front vowels (e, ö, ü) "
    "and back vowels (a, o, u) do not mix inside a word, and suffixes change shape to match. The "
    "consonants q (uvular k) and gh (voiced uvular fricative) are the signature sounds — q is made "
    "farther back in the throat than k. Stress is usually on the last syllable."
)

GRAMMAR_DESC = (
    "Uyghur is subject-object-verb and agglutinative: meaning is built by stacking suffixes onto "
    "unchanging roots. Nouns take six cases (nominative, genitive, dative, accusative, locative, "
    "ablative); there is no grammatical gender. The verb root never changes — tense, person, negation "
    "and mood are all suffixes: ishlimeymen = 'I do not work' (ishli-me-y-men). Vowel harmony chooses "
    "the suffix shape."
)

TENSE_DESC = (
    "Tense is a suffix between the root and the person ending. Men ishlaymen = 'I am working / I work'; "
    "men ishlidim = 'I worked'; men ishlayman? no — men ishlaymen covers present, men ishlarman? The "
    "clean paradigm: present -y/-imen (men oquymen, I study), past -di (men oqudum, I studied), future "
    "-ar/-er (men oquyarman? no). Keep to the verified three: present -(i)men, past -dim/-dum, and the "
    "helper construction with bolidu for future. The examples below hold the subject 'men' (I) steady "
    "on three everyday verbs so you can watch only the tense suffix move."
)

REGISTER_DESC = (
    "Uyghur has four levels of 'you': sen (intimate), siz (polite), sili (respectful), sizler (very "
    "polite). Use siz with strangers and elders; sen is for friends, family and children. Greetings "
    "stack: Essalamu eleykum (formal) down to salam (casual). Yaxshimusiz? ('are you well?') is both "
    "greeting and question — answer yaxshi, rahmet ('well, thanks'). Hospitality language is rich: "
    "welcome guests with lengthy well-wishes."
)

COMPLEX_DESC = (
    "Uyghur joins clauses with chunki (because), lekin/emma (but), and üchün (in order to). Relative "
    "clauses come before the noun as participles: ishligen adem (the person who worked). Conditions "
    "use eger (if) with the conditional suffix -sa/-se. Because suffixes stack in a fixed order "
    "(root-tense-person), long sentences parse mechanically once you know the slots."
)

REVIEW_NOTE = (
    "You now hold the complete Uyghur ladder: the 32-letter Perso-Arabic script with full vowels, "
    "vowel harmony and uvular consonants, agglutinative SOV grammar with six cases, core nouns verbs "
    "and adjectives, four levels of 'you', numbers to one hundred, time words, greetings, ten themed "
    "sentence sets, the suffix tenses, questions, commands, descriptions, three graded stories, "
    "maqal proverbs, formal registers, and three full conversations. Read right to left and let the "
    "suffixes stack."
)

NOUNS = [
    ("سۇ", "su", "water", "سۇ ياخشى", "su yaxshi", "The water is good."),
    ("نان", "nan", "bread", "نان ياخشى", "nan yaxshi", "The bread is good."),
    ("ئۆي", "öy", "house", "ئۆي چوڭ", "öy chong", "The house is big."),
    ("ماشىنا", "mashina", "car", "ماشىنا يېڭى", "mashina yéngi", "The car is new."),
    ("كىتاب", "kitab", "book", "كىتاب ياخشى", "kitab yaxshi", "The book is good."),
    ("بازار", "bazar", "market", "بازار چوڭ", "bazar chong", "The market is big."),
    ("مەكتەپ", "mektep", "school", "مەكتەپ ياخشى", "mektep yaxshi", "The school is good."),
    ("كۈن", "kün", "day, sun", "كۈن ياخشى", "kün yaxshi", "The day is good."),
    ("كېچە", "kéche", "night", "كېچە ياخشى", "kéche yaxshi", "The night is good."),
    ("ئاتا", "ata", "father", "ئاتا ياخشى", "ata yaxshi", "Father is good."),
    ("ئانا", "ana", "mother", "ئانا ياخشى", "ana yaxshi", "Mother is good."),
    ("مۇھەببەت", "muhebbet", "love", "مۇھەببەت ياخشى", "muhebbet yaxshi", "Love is good."),
]

VERBS = [
    ("يېمەك", "yémek", "to eat", "يېمەك ياخشى", "yémek yaxshi", "Eating is good."),
    ("ئىچمەك", "ichmek", "to drink", "ئىچمەك ياخشى", "ichmek yaxshi", "Drinking is good."),
    ("بارماق", "barmaq", "to go", "بارماق ياخشى", "barmaq yaxshi", "Going is good."),
    ("كەلمەك", "kelmek", "to come", "كەلمەك ياخشى", "kelmek yaxshi", "Coming is good."),
    ("سۆزلىمەك", "sözlimek", "to speak", "سۆزلىمەك ياخشى", "sözlimek yaxshi", "Speaking is good."),
    ("ئىشلىمەك", "ishlimek", "to work", "ئىشلىمەك ياخشى", "ishlimek yaxshi", "Working is good."),
    ("ئۆگەنمەك", "ögenmek", "to learn", "ئۆگەنمەك ياخشى", "ögenmek yaxshi", "Learning is good."),
    ("بەرمەك", "bermek", "to give", "بەرمەك ياخشى", "bermek yaxshi", "Giving is good."),
    ("سۆيمەك", "söymek", "to love", "سۆيمەك ياخشى", "söymek yaxshi", "Loving is good."),
    ("ياشىماق", "yashimaq", "to live", "ياشىماق ياخشى", "yashimaq yaxshi", "Living is good."),
]

ADJS = [
    ("ياخشى", "yaxshi", "good", "ياخشى ئۆي", "yaxshi öy", "a good house"),
    ("يامان", "yaman", "bad", "يامان ماشىنا", "yaman mashina", "a bad car"),
    ("چوڭ", "chong", "big", "چوڭ ئۆي", "chong öy", "a big house"),
    ("كىچىك", "kichik", "small", "كىچىك كىتاب", "kichik kitab", "a small book"),
    ("يېڭى", "yéngi", "new", "يېڭى ماشىنا", "yéngi mashina", "a new car"),
    ("كونا", "kona", "old", "كونا ئۆي", "kona öy", "an old house"),
    ("قىزىل", "qizil", "red", "قىزىل ماشىنا", "qizil mashina", "a red car"),
    ("ئاق", "aq", "white", "ئاق كۆينەك", "aq köynek", "a white shirt"),
]

PRONOUNS = [
    ("مەن", "men", "I"),
    ("سەن", "sen", "you (intimate)"),
    ("سىز", "siz", "you (polite)"),
    ("سىلى", "sili", "you (respectful)"),
    ("ئۇ", "u", "he / she / it"),
    ("بىز", "biz", "we"),
    ("سىزلەر", "sizler", "you (very polite)"),
    ("بۇ", "bu", "this"),
]

NUMBERS = [
    ("بىر", "bir", "one"), ("ئىككى", "ikki", "two"), ("ئۈچ", "üch", "three"),
    ("تۆت", "töt", "four"), ("بەش", "besh", "five"), ("ئالتە", "alte", "six"),
    ("يەتتە", "yette", "seven"), ("سەككىز", "sekkiz", "eight"),
    ("توققۇز", "toqquz", "nine"), ("ئون", "on", "ten"),
    ("يىگىرمە", "yigirme", "twenty"), ("يۈز", "yüz", "one hundred"),
]

TIME_WORDS = [
    ("بۈگۈن", "bügün", "today"), ("ئەتە", "ete", "tomorrow"),
    ("تۆنۈگۈن", "tönügün", "yesterday"), ("ھەپتە", "hepte", "week"),
    ("ئاي", "ay", "month"), ("يىل", "yil", "year"),
]

GREETINGS = [
    ("ئەسسالامۇ ئەلەيكۇم", "essalamu eleykum", "Hello! (formal)"),
    ("سالام", "salam", "Hello! (casual)"),
    ("ياخشىمۇسىز", "yaxshimusiz", "How are you? (polite)"),
    ("ياخشى، رەھمەت", "yaxshi, rahmet", "Well, thanks. (reply)"),
    ("رەھمەت", "rahmet", "Thank you."),
    ("كۆپ رەھمەت", "köp rahmet", "Thank you very much."),
    ("مەرھەمەت", "merhemet", "Please."),
    ("كەچۈرۈڭ", "kechürüng", "Sorry / excuse me."),
    ("خەير-خوش", "xeyr-xosh", "Goodbye."),
    ("يەنە كۆرۈشەيمىز", "yene körüsheyimiz", "See you again."),
]

THEMES = [
    ("Home and Family", [
        ("ئائىلە", "a'ile", "family", "ئائىلە ياخشى", "a'ile yaxshi", "The family is good."),
        ("ئاتا", "ata", "father", "ئاتا ياخشى", "ata yaxshi", "Father is good."),
        ("ئانا", "ana", "mother", "ئانا تاماق ئېتىدۇ", "ana tamaq étidu", "Mother cooks food."),
        ("ئاكا", "aka", "older brother", "ئاكا ياردەم قىلىدۇ", "aka yardem qilidu", "The older brother helps."),
        ("ئاچا", "acha", "older sister", "ئاچا ئۆگىنىدۇ", "acha öginidu", "The older sister learns."),
        ("ئىنى", "ini", "younger brother", "ئىنى ئوينايدۇ", "ini oynaydu", "The younger brother plays."),
    ]),
    ("Food and Cooking", [
        ("تاماق", "tamaq", "food", "تاماق ياخشى", "tamaq yaxshi", "The food is good."),
        ("نان", "nan", "bread", "نان ياخشى", "nan yaxshi", "The bread is good."),
        ("گۆش", "gösh", "meat", "گۆش قىممەت", "gösh qimmet", "The meat is expensive."),
        ("سۇ", "su", "water", "سۇ ياخشى", "su yaxshi", "The water is good."),
        ("سۈت", "süt", "milk", "سۈت ياخشى", "süt yaxshi", "The milk is good."),
        ("چاي", "chay", "tea", "چاي ياخشى", "chay yaxshi", "The tea is good."),
    ]),
    ("Travel and Directions", [
        ("يول", "yol", "road", "يول ئۇزۇن", "yol uzun", "The road is long."),
        ("ماشىنا", "mashina", "car", "ماشىنا ماڭىدۇ", "mashina mangidu", "The car goes."),
        ("ئايروپىلان", "ayropilan", "airplane", "ئايروپىلان ئۇچىدۇ", "ayropilan uchidu", "The plane flies."),
        ("بېكەت", "béket", "station", "بېكەت يېقىن", "béket yéqin", "The station is near."),
        ("ئوڭ", "ong", "right", "ئوڭغا بېرىڭ", "onggha béring", "Go right."),
        ("سول", "sol", "left", "سولغا بېرىڭ", "solgha béring", "Go left."),
    ]),
    ("Work and School", [
        ("ئىش", "ish", "work", "ئىش ياخشى", "ish yaxshi", "The work is good."),
        ("مەكتەپ", "mektep", "school", "مەكتەپ ئېچىق", "mektep échiq", "The school is open."),
        ("ئوقۇغۇچى", "oqughuchi", "student", "ئوقۇغۇچى ئۆگىنىدۇ", "oqughuchi öginidu", "The student learns."),
        ("ئوقۇتقۇچى", "oqutquchi", "teacher", "ئوقۇتقۇچى سۆزلەيدۇ", "oqutquchi sözleydu", "The teacher speaks."),
        ("كىتاب", "kitab", "book", "كىتاب يېپىق", "kitab yépiq", "The book is closed."),
        ("قەلەم", "qelem", "pen", "قەلەم ياخشى", "qelem yaxshi", "The pen is good."),
    ]),
    ("Health and the Body", [
        ("بەدەن", "beden", "body", "بەدەن ياخشى", "beden yaxshi", "The body is good."),
        ("باش", "bash", "head", "باش ئاغرىيدۇ", "bash aghriydu", "The head aches."),
        ("كۆز", "köz", "eye", "كۆز كۆرىدۇ", "köz köridu", "The eye sees."),
        ("قول", "qol", "arm, hand", "قول ئاغرىيدۇ", "qol aghriydu", "The arm aches."),
        ("پۇت", "put", "leg, foot", "پۇت ئاغرىيدۇ", "put aghriydu", "The leg aches."),
        ("دوختۇر", "doxtur", "doctor", "دوختۇر داۋالايدۇ", "doxtur dawalaydu", "The doctor heals."),
    ]),
    ("Emotions and Feelings", [
        ("خۇشاللىق", "xushalliq", "joy", "خۇشاللىق ياخشى", "xushalliq yaxshi", "Joy is good."),
        ("قايغۇ", "qayghu", "sadness", "قايغۇ كەتتى", "qayghu ketti", "The sadness is gone."),
        ("قورقۇنچ", "qorqunch", "fear", "قورقۇنچ كەتتى", "qorqunch ketti", "The fear is gone."),
        ("مۇھەببەت", "muhebbet", "love", "مۇھەببەت كۈچلۈك", "muhebbet küchlük", "Love is strong."),
        ("ھەسەت", "heset", "jealousy", "ھەسەت يامان", "heset yaman", "Jealousy is bad."),
        ("تىنچلىق", "tinchliq", "peace", "تىنچلىق ياخشى", "tinchliq yaxshi", "Peace is good."),
    ]),
    ("Nature and Weather", [
        ("تەبىئەت", "tebi'et", "nature", "تەبىئەت گۈزەل", "tebi'et güzel", "Nature is beautiful."),
        ("يامغۇر", "yamghur", "rain", "يامغۇر ياغىدۇ", "yamghur yaghidu", "The rain is falling."),
        ("كۈن", "kün", "sun", "كۈن ئىسسىق", "kün issiq", "The sun is hot."),
        ("ئاي", "ay", "moon", "ئاي يورۇق", "ay yoruq", "The moon is bright."),
        ("دەرەخ", "derex", "tree", "دەرەخ چوڭ", "derex chong", "The tree is big."),
        ("گۈل", "gül", "flower", "گۈل گۈزەل", "gül güzel", "The flower is beautiful."),
    ]),
    ("Shopping and Money", [
        ("پۇل", "pul", "money", "پۇل ياخشى", "pul yaxshi", "Money is good."),
        ("باھا", "baha", "price", "باھا يۇقىرى", "baha yuqiri", "The price is high."),
        ("دۇكان", "dukan", "shop", "دۇكان ئېچىق", "dukan échiq", "The shop is open."),
        ("ئەرزان", "erzan", "cheap, discount", "ئەرزان ياخشى", "erzan yaxshi", "Cheap is good."),
        ("خېرىدار", "xéridar", "customer", "خېرىدار خۇشال", "xéridar xushal", "The customer is happy."),
        ("ساتقۇچى", "satquchi", "seller", "ساتقۇچى ياخشى", "satquchi yaxshi", "The seller is good."),
    ]),
    ("Friendship and Social Life", [
        ("دوست", "dost", "friend", "دوست ياخشى", "dost yaxshi", "The friend is good."),
        ("مېھماندوستلۇق", "méhmandostluq", "hospitality", "مېھماندوستلۇق ياخشى", "méhmandostluq yaxshi", "Hospitality is good."),
        ("پاراڭ", "parang", "conversation", "پاراڭ ياخشى", "parang yaxshi", "The conversation is good."),
        ("زىياپەت", "ziyapet", "feast, meal", "زىياپەت ياخشى", "ziyapet yaxshi", "The feast is good."),
        ("ئۇسسۇل", "ussul", "dance", "ئۇسسۇل گۈزەل", "ussul güzel", "The dance is beautiful."),
        ("ناخشا", "naxsha", "song", "ناخشا گۈزەل", "naxsha güzel", "The song is beautiful."),
    ]),
    ("Technology and Communication", [
        ("تېلېفون", "téléfon", "telephone", "تېلېفون چاقىرىدۇ", "téléfon chaqiridu", "The phone is ringing."),
        ("كومپيۇتېر", "kompyutér", "computer", "كومپيۇتېر ئىشلەيدۇ", "kompyutér ishleydu", "The computer is working."),
        ("ئىنتېرنېت", "intérnét", "internet", "ئىنتېرنېت تېز", "intérnét téz", "The internet is fast."),
        ("توك", "tok", "electricity", "توك بار", "tok bar", "There is electricity."),
        ("خەت", "xet", "message, letter", "خەت كەلدى", "xet keldi", "The message has arrived."),
        ("رادىئو", "radio", "radio", "رادىئو چالدى", "radio chaldi", "The radio is playing."),
    ]),
]

QUESTIONS = [
    ("سىزنىڭ ئىسمىڭىز نېمە", "sizning ismingiz néme", "What is your name?"),
    ("ئانا نەدە", "ana nede", "Where is mother?"),
    ("بۇ قانچە", "bu qanche", "How much is this?"),
    ("نېمىشقا", "némishqa", "Why?"),
    ("قاچان", "qachan", "When?"),
    ("بۇ كىم", "bu kim", "Who is this?"),
    ("تاماق قانداق", "tamaq qandaq", "How is the food?"),
    ("سىز نەدىن", "siz nedin", "Where are you from?"),
]

COMMANDS = [
    ("بۇ يەرگە كېلىڭ", "bu yerge kéling", "Come here!"),
    ("بېرىڭ", "béring", "Go!"),
    ("ئولتۇرۇڭ", "olturung", "Sit down!"),
    ("ئاستا سۆزلەڭ", "asta sözleng", "Speak slowly!"),
    ("ماڭا ياردەم بېرىڭ", "manga yardem béring", "Help me!"),
    ("ئاڭلاڭ", "anglang", "Listen!"),
    ("قاراڭ", "qarang", "Look!"),
    ("توختاڭ", "toxtang", "Stop!"),
]

DESCRIBE = [
    ("ئېگىز ئادەم، ئېگىز", "égiz adem, égiz", "The tall man, he is tall."),
    ("گۈزەل ئايال، گۈزەل", "güzel ayal, güzel", "The beautiful woman, she is beautiful."),
    ("چوڭ ئۆي، چوڭ", "chong öy, chong", "The big house, it is big."),
    ("قىزىل ماشىنا، قىزىل", "qizil mashina, qizil", "The red car, it is red."),
    ("كىچىك بالا، كىچىك", "kichik bala, kichik", "The small child, he/she is small."),
    ("يېڭى كىتاب، يېڭى", "yéngi kitab, yéngi", "The new book, it is new."),
    ("ئىسسىق كۈن، ئىسسىق", "issiq kün, issiq", "The hot sun, it is hot."),
    ("سوغۇق سۇ، سوغۇق", "soghuq su, soghuq", "The cold water, it is cold."),
]

STORIES = [
    ("Story I: The Boy and the Lamb", [
        ("بىر بالا بار ئىدى", "bir bala bar idi", "There was a boy."),
        ("بالىنىڭ بىر قوزىسى بار", "balining bir qozisi bar", "The boy has a lamb."),
        ("قوزا ئاق", "qoza aq", "The lamb is white."),
        ("بالا قوزىنى سۆيىدۇ", "bala qozini söyidu", "The boy loves the lamb."),
        ("بىر كۈنى قوزا يوقاپ كەتتى", "bir küni qoza yoqap ketti", "One day the lamb got lost."),
        ("بالا ھەممە يەرنى ئىزدىدى", "bala hemme yerni izdidi", "The boy searched everywhere."),
        ("ئاخىرى ئۇنى تاپتى", "axiri uni tapti", "Finally he found it."),
        ("ئۇ بەك خۇشال بولدى", "u bek xushal boldi", "He was very happy."),
    ]),
    ("Story II: The Rainy Day", [
        ("بۈگۈن يامغۇر ياغىدۇ", "bügün yamghur yaghidu", "Today the rain is falling."),
        ("بالىلار ئۆيدە تۇرىدۇ", "balilar öyde turidu", "The children stay in the house."),
        ("ئانا تاماق ئېتىدۇ", "ana tamaq étidu", "Mother is cooking food."),
        ("تاماق ياخشى", "tamaq yaxshi", "The food is good."),
        ("ئاتا كىتاب ئوقۇيدۇ", "ata kitab oquydu", "Father is reading a book."),
        ("يامغۇردىن كېيىن كۈن چىقتى", "yamghurdin kéyin kün chiqti", "After the rain the sun came out."),
        ("بالىلار سىرتقا چىقتى", "balilar sirtqa chiqti", "The children went outside."),
        ("ئۇلار ھويلىدا ئوينايدۇ", "ular hoylida oynaydu", "They are playing in the yard."),
    ]),
    ("Story III: The Market Trip", [
        ("ئەتە بازارغا بارىمىز", "ete bazargha barimiz", "Tomorrow we go to the market."),
        ("ئانا نان ئالىدۇ", "ana nan alidu", "Mother buys bread."),
        ("ئاتا گۆش ئالىدۇ", "ata gösh alidu", "Father buys meat."),
        ("بالا كەمپۈت ئالىدۇ", "bala kempüt alidu", "The child buys candy."),
        ("نان ياخشى", "nan yaxshi", "The bread is good."),
        ("گۆش قىممەت", "gösh qimmet", "The meat is expensive."),
        ("ھەممىمىز ئۆيگە بارىمىز", "hemmimiz öyge barimiz", "We all go home."),
        ("ھەممىمىز ياخشى يەيمىز", "hemmimiz yaxshi yeymiz", "We all eat well."),
    ]),
]

IDIOMS = [
    ("Qan bilen qanni yughili bolmas", "qan bilen qanni yughili bolmas", "Blood cannot be washed with blood", "Revenge cannot solve problems; only forgiveness can."),
    ("Elge qoshulsang er bolisen, eldin ajrilsang jer bolisen", "elge qoshulsang er bolisen, eldin ajrilsang jer bolisen", "Join the people and become a hero; leave the people and become nothing", "Strength and honor come from the community."),
    ("Yaxshi söz — jan azuqi", "yaxshi söz — jan azuqi", "A good word is food for the soul", "Kind speech nourishes people."),
    ("Bilim küchtur", "bilim küchtur", "Knowledge is strength", "Learning is power."),
]

CONVOS = [
    ("At the Market", [
        ("A", "ئەسسالامۇ ئەلەيكۇم", "essalamu eleykum", "Hello!"),
        ("B", "ۋەئەلەيكۇم ئەسسالام", "we'eleykum essalam", "Hello to you!"),
        ("A", "بۇ قانچە", "bu qanche", "How much is this?"),
        ("B", "ئون يۈەن", "on yü'en", "Ten yuan."),
        ("A", "قىممەت", "qimmet", "Expensive."),
        ("B", "ئەرزان قىلىمەن", "erzan qilimen", "I will make it cheap."),
        ("A", "رەھمەت، ئالىمەن", "rahmet, alimen", "Thanks, I will take it."),
        ("B", "خەير-خوش", "xeyr-xosh", "Goodbye."),
    ]),
    ("Meeting a Friend", [
        ("A", "سالام، ياخشىمۇسىز", "salam, yaxshimusiz", "Hi, how are you?"),
        ("B", "ياخشى، رەھمەت. سىزچۇ", "yaxshi, rahmet. sizchu", "Well, thanks. And you?"),
        ("A", "مەنمۇ ياخشى", "menmu yaxshi", "I am well too."),
        ("B", "سىزنىڭ ئىسمىڭىز نېمە", "sizning ismingiz néme", "What is your name?"),
        ("A", "مېنىڭ ئىسمىم ئەخمەت", "méning ismim Exmet", "My name is Exmet."),
        ("B", "تونۇشقىنىمغا خۇشال بولدۇم", "tonushqinimgha xushal boldum", "Nice to meet you."),
        ("A", "مەنمۇ خۇشال بولدۇم", "menmu xushal boldum", "Nice to meet you too."),
        ("B", "يەنە كۆرۈشەيمىز", "yene körüsheyimiz", "See you again."),
    ]),
    ("Solving a Problem", [
        ("A", "مەسىلە بار", "mesile bar", "There is a problem."),
        ("B", "قانداق مەسىلە", "qandaq mesile", "What kind of problem?"),
        ("A", "ماشىنا بۇزۇلدى", "mashina buzuldi", "The car broke down."),
        ("B", "قايغۇرماڭ", "qayghurmang", "Do not worry."),
        ("A", "ماڭا ياردەم بېرىڭ", "manga yardem béring", "Help me, please."),
        ("B", "مەن ياردەم بېرىمەن", "men yardem bérimen", "I will help."),
        ("A", "كۆپ رەھمەت", "köp rahmet", "Thank you very much."),
        ("B", "ئەرزىمەيدۇ", "erzimeydu", "You are welcome."),
    ]),
]

CITATIONS = [
    "Engesæth T, Yakup A, Dwyer A. Greetings from the Teklimakan: a handbook of Modern Uyghur. University of Kansas; 2009.",
    "Ibrahim A. Spoken Uyghur. Dunwoody Press; 1998.",
    "Nash C. Uyghur-English Dictionary resources and the English-Uyghur online dictionary (uighurdictionary.com).",
    "ISO 639-3:2007 language code uig.",
    "Standard pedagogical sources for Uyghur vocabulary, usage, and phraseology.",
]
