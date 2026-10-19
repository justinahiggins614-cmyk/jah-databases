# -*- coding: utf-8 -*-
"""Language data module: Tatar (tat). Facts verified 2026-10-17 via
Omniglot phrases, Wikivoyage phrasebook, proverb studies."""

SLUG = "language-tatar"
PREFIX = "JAH-LTAT-"
SIG_PREFIX = "JAH-LTATS-"
NAME = "Tatar"
NATIVE = "татарча"
NATIVE_ROMAN = "tatarça"
ISO1 = "tt"
ISO3 = "tat"
FAMILY = "Turkic > Kipchak (Northwestern Turkic)"
SPEAKERS = "about 5 to 7 million speakers"
REGIONS = "Tatarstan in Russia, where it is co-official with Russian, plus Siberia, Central Asia and diaspora communities"
SCRIPT_NAME = "Cyrillic script (with 6 extra letters)"
WORD_ORDER = "subject-object-verb (SOV)"
AI_NAME = "JAH Tatar Language Archivist"
SIG_AI_NAME = "JAH Tatar Signature Archivist"

OVERVIEW = (
    "Tatar (татарча, tatarça) is a Kipchak Turkic language spoken by about 5 to 7 million people, most "
    "of them in Tatarstan, Russia, where it is co-official with Russian. Its closest relative is "
    "Bashkir. Tatar is written in a Cyrillic alphabet with six extra letters (ә, ө, ү, җ, ң, һ) and was "
    "earlier written in Arabic and Latin scripts. Like all Turkic languages it is agglutinative with "
    "vowel harmony and subject-object-verb word order, and it carries a deep proverb tradition."
)

SCRIPT_DESC = (
    "Tatar uses a Cyrillic alphabet of 39 letters: the 33 Russian letters plus Әә, Өө, Үү, Җҗ, Ңң, Һһ. "
    "The extra letters are: ә (like 'a' in 'cat'), ө (rounded 'e'), ү (rounded 'i'), җ ('j' as in "
    "'jump'), ң ('ng' as in 'sing'), һ (a soft breathy 'h'). Read left to right. Latin-script Tatar "
    "(tatarça with ä, ö, ü, ğ, ş, ç, ñ) is used online and in some publications; the records below show "
    "Cyrillic first with Latin transliteration."
)

ALPHABET_NOTE = (
    "The 39-letter Cyrillic alphabet is phonetic. The table shows the six extra letters plus six "
    "high-frequency letters with their sounds; ordinary Cyrillic letters match their Russian values."
)

ALPHABET_SAMPLE = [
    ("Әә", "like 'a' in 'cat'"), ("Өө", "rounded 'e'"), ("Үү", "rounded 'i'"),
    ("Җҗ", "'j' as in 'jump'"), ("Ңң", "'ng' as in 'sing'"), ("Һһ", "soft breathy 'h'"),
    ("Аа", "deep 'a'"), ("Ы", "like 'i' in 'bit' but deeper"), ("Е", "'ye'"),
    ("Ш", "'sh'"), ("Ч", "'ch'"), ("Ю", "'yu'"),
]

SOUNDS_DESC = (
    "Tatar has 9 vowels in harmony pairs: back (а, ы, о, у) and front (ә, э, ө, ү) plus и which is "
    "neutral. Suffix vowels harmonize with the root. The signature sounds are the uvular қ-like х "
    "(softer than Russian х) and the ң ('ng'). Tatar а is deeper and wider than Russian а; о, э, ө are "
    "short and crisp. Stress usually falls on the last syllable. The ә/а and ү/у pairs are the "
    "beginner's key distinction."
)

GRAMMAR_DESC = (
    "Tatar is subject-object-verb and agglutinative: suffixes stack onto unchanging roots in fixed "
    "order. Nouns take six cases; there is no grammatical gender and no articles. The verb root never "
    "changes — tense, person, negation and questions are suffixes: беләм = 'I know', белергә = 'to "
    "know', белмим = 'I do not know'. Vowel harmony chooses the suffix vowels."
)

TENSE_DESC = (
    "Tense is a suffix between the root and the person ending. Мин эшлим = 'I am working'; мин "
    "эшләдем = 'I worked'; мин эшләрмен = 'I will work'. Negation inserts -ма-/-мә- before the tense: "
    "мин эшләмим = 'I do not work'. The examples below hold the subject 'мин' (I) steady on three "
    "everyday verbs — эшләргә (to work), ашарга (to eat), барырга (to go) — so you can watch only the "
    "tense suffix move."
)

REGISTER_DESC = (
    "Respect in Tatar is carried by the сез/син distinction: сез is polite and plural, син is intimate. "
    "Greet elders with исәнмесез (formal hello, answered the same); friends get сәлам. Рәхмәт thanks; "
    "зур рәхмәт thanks greatly. Зинһар softens requests ('please'). Address respected elders with "
    "абый (elder brother) or апа (elder sister). Take off shoes entering a home, accept tea, and never "
    "rush the greeting exchange."
)

COMPLEX_DESC = (
    "Tatar joins clauses with чөнки (because), әмма (but), and өчен (in order to). Relative clauses "
    "come before the noun as participles: эшләгән кеше (the person who worked). Conditions use әгәр "
    "(if) with the -са/-сә suffix. Proverbs love parallel structure — learn them and complex sentences "
    "come free."
)

REVIEW_NOTE = (
    "You now hold the complete Tatar ladder: the 39-letter Cyrillic script with ә ө ү җ ң һ, vowel "
    "harmony and final stress, agglutinative SOV grammar with six cases, core nouns verbs and "
    "adjectives, pronouns, numbers to one hundred, time words, greetings, ten themed sentence sets, "
    "the suffix tenses, questions, commands, descriptions, three graded stories, мәкаль proverbs, "
    "formal registers, and three full conversations. Read left to right and let the suffixes stack."
)

NOUNS = [
    ("су", "su", "water", "Су яхшы", "su yaxşı", "The water is good."),
    ("икмәк", "ikmäk", "bread", "Икмәк яхшы", "ikmäk yaxşı", "The bread is good."),
    ("өй", "öy", "house", "Өй зур", "öy zur", "The house is big."),
    ("машина", "mashina", "car", "Машина яңа", "mashina yaña", "The car is new."),
    ("китап", "kitap", "book", "Китап яхшы", "kitap yaxşı", "The book is good."),
    ("базар", "bazar", "market", "Базар зур", "bazar zur", "The market is big."),
    ("мәктәп", "mäktäp", "school", "Мәктәп яхшы", "mäktäp yaxşı", "The school is good."),
    ("көн", "kön", "day", "Көн яхшы", "kön yaxşı", "The day is good."),
    ("төн", "tön", "night", "Төн яхшы", "tön yaxşı", "The night is good."),
    ("әти", "äti", "father", "Әти яхшы", "äti yaxşı", "Father is good."),
    ("әни", "äni", "mother", "Әни яхшы", "äni yaxşı", "Mother is good."),
    ("мәхәббәт", "mäxäbbät", "love", "Мәхәббәт яхшы", "mäxäbbät yaxşı", "Love is good."),
]

VERBS = [
    ("ашарга", "asharga", "to eat", "Ашарга яхшы", "asharga yaxşı", "Eating is good."),
    ("эчәргә", "echärgä", "to drink", "Эчәргә яхшы", "echärgä yaxşı", "Drinking is good."),
    ("барырга", "barırga", "to go", "Барырга яхшы", "barırga yaxşı", "Going is good."),
    ("килергә", "kilergä", "to come", "Килергә яхшы", "kilergä yaxşı", "Coming is good."),
    ("сөйләшергә", "söyläşergä", "to speak", "Сөйләшергә яхшы", "söyläşergä yaxşı", "Speaking is good."),
    ("эшләргә", "eşlärgä", "to work", "Эшләргә яхшы", "eşlärgä yaxşı", "Working is good."),
    ("өйрәнергә", "öyränergä", "to learn", "Өйрәнергә яхшы", "öyränergä yaxşı", "Learning is good."),
    ("бирергә", "birergä", "to give", "Бирергә яхшы", "birergä yaxşı", "Giving is good."),
    ("яратырга", "yaratırga", "to love", "Яратырга яхшы", "yaratırga yaxşı", "Loving is good."),
    ("яшәргә", "yäşärgä", "to live", "Яшәргә яхшы", "yäşärgä yaxşı", "Living is good."),
]

ADJS = [
    ("яхшы", "yaxşı", "good", "яхшы өй", "yaxşı öy", "a good house"),
    ("начар", "naçar", "bad", "начар машина", "naçar mashina", "a bad car"),
    ("зур", "zur", "big", "зур өй", "zur öy", "a big house"),
    ("кечкенә", "keçkenä", "small", "кечкенә китап", "keçkenä kitap", "a small book"),
    ("яңа", "yaña", "new", "яңа машина", "yaña mashina", "a new car"),
    ("иске", "iske", "old", "иске өй", "iske öy", "an old house"),
    ("кызыл", "qızıl", "red", "кызыл машина", "qızıl mashina", "a red car"),
    ("ак", "aq", "white", "ак күлмәк", "aq külmäk", "a white shirt"),
]

PRONOUNS = [
    ("мин", "min", "I"),
    ("син", "sin", "you (intimate)"),
    ("сез", "sez", "you (polite/plural)"),
    ("ул", "ul", "he / she / it"),
    ("без", "bez", "we"),
    ("алар", "alar", "they"),
    ("бу", "bu", "this"),
    ("теге", "tege", "that"),
]

NUMBERS = [
    ("бер", "ber", "one"), ("ике", "ike", "two"), ("өч", "öç", "three"),
    ("дүрт", "dürt", "four"), ("биш", "biş", "five"), ("алты", "altı", "six"),
    ("җиде", "cide", "seven"), ("сигез", "sigez", "eight"),
    ("тугыз", "tuğız", "nine"), ("ун", "un", "ten"),
    ("егерме", "egerme", "twenty"), ("йөз", "yöz", "one hundred"),
]

TIME_WORDS = [
    ("бүген", "bügen", "today"), ("иртәгә", "irtägä", "tomorrow"),
    ("кичә", "kiçä", "yesterday"), ("атна", "atna", "week"),
    ("ай", "ay", "month"), ("ел", "el", "year"),
]

GREETINGS = [
    ("Исәнмесез!", "isänmesez", "Hello! (formal)"),
    ("Исәнме!", "isänme", "Hello! (informal)"),
    ("Сәлам!", "sälam", "Hi!"),
    ("Хәлләрегез ничек?", "xälläregez niçek", "How are you? (polite)"),
    ("Яхшы, рәхмәт.", "yaxşı, räxmät", "Well, thanks. (reply)"),
    ("Рәхмәт.", "räxmät", "Thank you."),
    ("Зур рәхмәт.", "zur räxmät", "Thank you very much."),
    ("Зинһар.", "zinhar", "Please."),
    ("Гафу итегез.", "ğafu itegez", "Sorry / excuse me."),
    ("Сау булыгыз!", "sau bulığız", "Goodbye! (formal)"),
]
THEMES = [
    ("Home and Family", [
        ("гаилә", "ğailä", "family", "Гаилә яхшы", "ğailä yaxşı", "The family is good."),
        ("әти", "äti", "father", "Әти эшли", "äti eşli", "Father works."),
        ("әни", "äni", "mother", "Әни ашар пешерә", "äni aşar peşerä", "Mother cooks food."),
        ("абый", "abıy", "older brother", "Абый ярдәм итә", "abıy yärdäm itä", "The older brother helps."),
        ("апа", "apa", "older sister", "Апа өйрәнә", "apa öyränä", "The older sister learns."),
        ("эне", "ene", "younger brother", "Эне уйный", "ene uynıy", "The younger brother plays."),
    ]),
    ("Food and Cooking", [
        ("азык", "azıq", "food", "Азык тәмле", "azıq tämle", "The food is tasty."),
        ("икмәк", "ikmäk", "bread", "Икмәк тәмле", "ikmäk tämle", "The bread is tasty."),
        ("ит", "it", "meat", "Ит кыйммәт", "it qıymmät", "The meat is expensive."),
        ("су", "su", "water", "Су яхшы", "su yaxşı", "The water is good."),
        ("сөт", "söt", "milk", "Сөт яхшы", "söt yaxşı", "The milk is good."),
        ("чәй", "çäy", "tea", "Чәй яхшы", "çäy yaxşı", "The tea is good."),
    ]),
    ("Travel and Directions", [
        ("юл", "yul", "road", "Юл озын", "yul ozın", "The road is long."),
        ("машина", "mashina", "car", "Машина бара", "mashina bara", "The car goes."),
        ("очкыч", "oçqıç", "airplane", "Очкыч оча", "oçqıç oça", "The plane flies."),
        ("вокзал", "vokzal", "station", "Вокзал якын", "vokzal yaqın", "The station is near."),
        ("уң", "uñ", "right", "Уңга бар", "uñğa bar", "Go right."),
        ("сул", "sul", "left", "Сулга бар", "sulğa bar", "Go left."),
    ]),
    ("Work and School", [
        ("эш", "eş", "work", "Эш яхшы", "eş yaxşı", "The work is good."),
        ("мәктәп", "mäktäp", "school", "Мәктәп ачык", "mäktäp açıq", "The school is open."),
        ("укучы", "uquçı", "student", "Укучы өйрәнә", "uquçı öyränä", "The student learns."),
        ("укытучы", "uqıtuçı", "teacher", "Укытучы сөйли", "uqıtuçı söyli", "The teacher speaks."),
        ("китап", "kitap", "book", "Китап ябык", "kitap yabıq", "The book is closed."),
        ("каләм", "käläm", "pen", "Каләм яхшы", "käläm yaxşı", "The pen is good."),
    ]),
    ("Health and the Body", [
        ("тән", "tän", "body", "Тән яхшы", "tän yaxşı", "The body is good."),
        ("баш", "baş", "head", "Баш авырта", "baş awırta", "The head aches."),
        ("күз", "küz", "eye", "Күз күрә", "küz kürä", "The eye sees."),
        ("кул", "qul", "arm, hand", "Кул авырта", "qul awırta", "The arm aches."),
        ("аяк", "ayaq", "leg, foot", "Аяк авырта", "ayaq awırta", "The leg aches."),
        ("табиб", "tabib", "doctor", "Табиб дәвалый", "tabib däwalıy", "The doctor heals."),
    ]),
    ("Emotions and Feelings", [
        ("шатлык", "şatlıq", "joy", "Шатлык яхшы", "şatlıq yaxşı", "Joy is good."),
        ("кайгы", "qayğı", "sadness", "Кайгы үтте", "qayğı ütte", "The sadness is gone."),
        ("куркыныч", "qurqınıç", "fear", "Куркыныч үтте", "qurqınıç ütte", "The fear is gone."),
        ("мәхәббәт", "mäxäbbät", "love", "Мәхәббәт көчле", "mäxäbbät köçle", "Love is strong."),
        ("көнчелек", "könçelek", "jealousy", "Көнчелек начар", "könçelek naçar", "Jealousy is bad."),
        ("тынычлык", "tınıçlıq", "peace", "Тынычлык яхшы", "tınıçlıq yaxşı", "Peace is good."),
    ]),
    ("Nature and Weather", [
        ("табигать", "tabiğat", "nature", "Табигать матур", "tabiğat matur", "Nature is beautiful."),
        ("яңгыр", "yañğır", "rain", "Яңгыр ява", "yañğır yawa", "The rain is falling."),
        ("кояш", "qoyaş", "sun", "Кояш эссе", "qoyaş esse", "The sun is hot."),
        ("ай", "ay", "moon", "Ай якты", "ay yaqtı", "The moon is bright."),
        ("агач", "ağaç", "tree", "Агач зур", "ağaç zur", "The tree is big."),
        ("чәчәк", "çäçäk", "flower", "Чәчәк матур", "çäçäk matur", "The flower is beautiful."),
    ]),
    ("Shopping and Money", [
        ("акча", "aqça", "money", "Акча яхшы", "aqça yaxşı", "Money is good."),
        ("бәя", "bäyä", "price", "Бәя югары", "bäyä yuğarı", "The price is high."),
        ("кибет", "kibet", "shop", "Кибет ачык", "kibet açıq", "The shop is open."),
        ("арзан", "arzan", "cheap", "Арзан яхшы", "arzan yaxşı", "Cheap is good."),
        ("сатып алучы", "satıp aluçı", "customer", "Сатып алучы шат", "satıp aluçı şat", "The customer is happy."),
        ("сатучы", "satuçı", "seller", "Сатучы яхшы", "satuçı yaxşı", "The seller is good."),
    ]),
    ("Friendship and Social Life", [
        ("дус", "dus", "friend", "Дус яхшы", "dus yaxşı", "The friend is good."),
        ("кунакчыллык", "qunaqçıllıq", "hospitality", "Кунакчыллык яхшы", "qunaqçıllıq yaxşı", "Hospitality is good."),
        ("сөйләшү", "söyläşü", "conversation", "Сөйләшү яхшы", "söyläşü yaxşı", "The conversation is good."),
        ("сый", "sıy", "feast, treat", "Сый яхшы", "sıy yaxşı", "The feast is good."),
        ("бию", "biyü", "dance", "Бию матур", "biyü matur", "The dance is beautiful."),
        ("җыр", "cır", "song", "Җыр матур", "cır matur", "The song is beautiful."),
    ]),
    ("Technology and Communication", [
        ("телефон", "telefon", "telephone", "Телефон шалтырый", "telefon şaltırıy", "The phone is ringing."),
        ("компьютер", "kompyuter", "computer", "Компьютер эшли", "kompyuter eşli", "The computer is working."),
        ("интернет", "internet", "internet", "Интернет тиз", "internet tiz", "The internet is fast."),
        ("ут", "ut", "electricity, fire", "Ут бар", "ut bar", "There is electricity."),
        ("хат", "xat", "message, letter", "Хат килде", "xat kilde", "The message has arrived."),
        ("радио", "radio", "radio", "Радио уйный", "radio uynıy", "The radio is playing."),
    ]),
]

QUESTIONS = [
    ("Исемегез ничек?", "isemegez niçek", "What is your name? (polite)"),
    ("Әниегез кайда?", "äniegez qayda", "Where is mother?"),
    ("Бу ничә тора?", "bu niçä tora", "How much does this cost?"),
    ("Ни өчен?", "ni öçen", "Why?"),
    ("Кайчан?", "qayçan", "When?"),
    ("Бу кем?", "bu kem", "Who is this?"),
    ("Ашар ничек?", "aşar niçek", "How is the food?"),
    ("Сез кайдан?", "sez qaydan", "Where are you from?"),
]

COMMANDS = [
    ("Монда кил!", "monda kil", "Come here!"),
    ("Бар!", "bar", "Go!"),
    ("Утыр!", "utır", "Sit down!"),
    ("Әкрен сөйлә!", "äkren söylä", "Speak slowly!"),
    ("Миңа ярдәм ит!", "miña yärdäm it", "Help me!"),
    ("Тыңла!", "tıñla", "Listen!"),
    ("Кара!", "qara", "Look!"),
    ("Тукта!", "tuqta", "Stop!"),
]

DESCRIBE = [
    ("Озын ир, озын.", "ozın ir, ozın", "The tall man, he is tall."),
    ("Матур хатын, матур.", "matur xatın, matur", "The beautiful woman, she is beautiful."),
    ("Зур өй, зур.", "zur öy, zur", "The big house, it is big."),
    ("Кызыл машина, кызыл.", "qızıl mashina, qızıl", "The red car, it is red."),
    ("Кечкенә бала, кечкенә.", "keçkenä bala, keçkenä", "The small child, he/she is small."),
    ("Яңа китап, яңа.", "yaña kitap, yaña", "The new book, it is new."),
    ("Эссе кояш, эссе.", "esse qoyaş, esse", "The hot sun, it is hot."),
    ("Салкын су, салкын.", "salqın su, salqın", "The cold water, it is cold."),
]

STORIES = [
    ("Story I: The Boy and the Lamb", [
        ("Бер малай бар иде.", "ber malay bar ide", "There was a boy."),
        ("Малайның бер бәрәне бар.", "malaynıñ ber bäräne bar", "The boy has a lamb."),
        ("Бәрән ак.", "bärän aq", "The lamb is white."),
        ("Малай бәрәнне ярата.", "malay bäränne yarata", "The boy loves the lamb."),
        ("Бер көнне бәрән югалды.", "ber könne bärän yuğaldı", "One day the lamb got lost."),
        ("Малай һәр җирне эзләде.", "malay här cirne ezläde", "The boy searched everywhere."),
        ("Ахырда аны тапты.", "axırda anı taptı", "Finally he found it."),
        ("Ул бик шат булды.", "ul bik şat buldı", "He was very happy."),
    ]),
    ("Story II: The Rainy Day", [
        ("Бүген яңгыр ява.", "bügen yañğır yawa", "Today the rain is falling."),
        ("Балалар өйдә утыра.", "balalar öydä utıra", "The children stay in the house."),
        ("Әни ашар пешерә.", "äni aşar peşerä", "Mother is cooking food."),
        ("Ашар тәмле.", "aşar tämle", "The food is tasty."),
        ("Әти китап укый.", "äti kitap uqıy", "Father is reading a book."),
        ("Яңгырдан соң кояш чыкты.", "yañğırdan soñ qoyaş çıqtı", "After the rain the sun came out."),
        ("Балалар урамга чыкты.", "balalar uramğa çıqtı", "The children went outside."),
        ("Алар ишегалдында уйный.", "alar işeğaldında uynıy", "They are playing in the yard."),
    ]),
    ("Story III: The Market Trip", [
        ("Иртәгә базарга барабыз.", "irtägä bazarğa barabız", "Tomorrow we go to the market."),
        ("Әни икмәк ала.", "äni ikmäk ala", "Mother buys bread."),
        ("Әти ит ала.", "äti it ala", "Father buys meat."),
        ("Бала кәнфит ала.", "bala känfit ala", "The child buys candy."),
        ("Икмәк тәмле.", "ikmäk tämle", "The bread is tasty."),
        ("Ит кыйммәт.", "it qıymmät", "The meat is expensive."),
        ("Без барыбыз да өйгә барабыз.", "bez barıbız da öygä barabız", "We all go home."),
        ("Без барыбыз да яхшы ашыйбыз.", "bez barıbız da yaxşı aşıybız", "We all eat well."),
    ]),
]

IDIOMS = [
    ("Дөреслек утта да янмый, суда да батмый", "döreslek utta da yanmıy, suda da batmıy", "Truth does not burn in fire, nor drown in water", "Truth survives everything."),
    ("Ай яктыртканда, йолдыз күренми", "ay yaqtırtqanda, yoldız kürenmi", "When the moon shines, the stars are not seen", "A great light outshines lesser ones."),
    ("Бала баласы балдан татлы", "bala balası baldan tatlı", "A grandchild is sweeter than honey", "Grandchildren are the sweetest joy."),
    ("Көчең белән мактанма, акылың белән мактан", "köçeñ belän maqtanma, aqılıñ belän maqtan", "Do not boast of strength, boast of mind", "Wisdom outranks force."),
    ("Саулык җеп түгел, өзелсә бәйләп булмый", "saulıq cep tügel, özelsä bäyläp bulmıy", "Health is not a thread; if it breaks you cannot tie it", "Guard your health — it cannot be mended like cloth."),
]

CONVOS = [
    ("At the Market", [
        ("A", "Исәнмесез!", "isänmesez", "Hello!"),
        ("B", "Исәнмесез! Нәрсә кирәк?", "isänmesez närsä kiräk", "Hello! What do you need?"),
        ("A", "Бу ничә тора?", "bu niçä tora", "How much does this cost?"),
        ("B", "Ун сум.", "un sum", "Ten som."),
        ("A", "Кыйммәт.", "qıymmät", "Expensive."),
        ("B", "Арзанрак итәм.", "arzanraq itäm", "I will make it cheaper."),
        ("A", "Рәхмәт, алам.", "räxmät, alam", "Thanks, I will take it."),
        ("B", "Сау булыгыз!", "sau bulığız", "Goodbye!"),
    ]),
    ("Meeting a Friend", [
        ("A", "Сәлам, хәлләр ничек?", "sälam, xällär niçek", "Hi, how are things?"),
        ("B", "Яхшы, рәхмәт! Син ничек?", "yaxşı, räxmät! sin niçek", "Well, thanks! How are you?"),
        ("A", "Мин дә яхшы.", "min dä yaxşı", "I am well too."),
        ("B", "Исемең ничек?", "isemeñ niçek", "What is your name?"),
        ("A", "Минем исемем Алсу.", "minem isemem Alsu", "My name is Alsu."),
        ("B", "Танышуыма шатмын.", "tanışuıma şatmın", "Nice to meet you."),
        ("A", "Мин дә шатмын.", "min dä şatmın", "Nice to meet you too."),
        ("B", "Күрешкәнгә кадәр!", "küreşkängä kadar", "Until we meet again!"),
    ]),
    ("Solving a Problem", [
        ("A", "Проблема бар.", "problema bar", "There is a problem."),
        ("B", "Нинди проблема?", "nindi problema", "What kind of problem?"),
        ("A", "Машина ватылды.", "mashina watıldı", "The car broke down."),
        ("B", "Борчылма.", "borçılma", "Do not worry."),
        ("A", "Миңа ярдәм ит!", "miña yärdäm it", "Help me!"),
        ("B", "Мин ярдәм итәм.", "min yärdäm itäm", "I will help."),
        ("A", "Зур рәхмәт!", "zur räxmät", "Thank you very much!"),
        ("B", "Бернәрсә дә түгел.", "bernärsә dä tügel", "It is nothing."),
    ]),
]

CITATIONS = [
    "Omniglot. Useful phrases in Tatar (tatarça / татарча).",
    "Wikivoyage contributors. Tatar phrasebook.",
    "European Proceedings. Representation of proverbs with zoonyms in Tatar linguistic view of the world. 2020.",
    "Revista San Gregorio. Linguistic means of expression in proverbs of Tatar, Russian, Turkish. 2017.",
    "ISO 639-1:2002 language code tt; ISO 639-3:2007 language code tat.",
    "Standard pedagogical sources for Tatar vocabulary, usage, and phraseology.",
]
