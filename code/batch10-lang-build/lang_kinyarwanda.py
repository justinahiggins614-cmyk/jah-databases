# -*- coding: utf-8 -*-
"""Language data module: Kinyarwanda (kin). Facts verified 2026-10-17 via
phrase references, Omniglot-style numbers, Wits thesis proverb texts."""

SLUG = "language-kinyarwanda"
PREFIX = "JAH-LKIN-"
SIG_PREFIX = "JAH-LKINS-"
NAME = "Kinyarwanda"
NATIVE = "Ikinyarwanda"
NATIVE_ROMAN = "Ikinyarwanda"
ISO1 = "rw"
ISO3 = "kin"
FAMILY = "Niger-Congo > Atlantic-Congo > Benue-Congo > Bantoid > Bantu (Northeast Bantu, Rwanda-Rundi)"
SPEAKERS = "about 15 million first-language speakers"
REGIONS = "Rwanda, where it is the national language spoken by nearly the whole population, plus Burundi, eastern DR Congo, Uganda and Tanzania; a large global diaspora"
SCRIPT_NAME = "Latin script"
WORD_ORDER = "subject-verb-object (SVO)"
AI_NAME = "JAH Kinyarwanda Language Archivist"
SIG_AI_NAME = "JAH Kinyarwanda Signature Archivist"

OVERVIEW = (
    "Kinyarwanda (Ikinyarwanda) is a Bantu language of the Niger-Congo family, spoken as a first language "
    "by about 15 million people. It is the national language of Rwanda, spoken by nearly the entire "
    "population, and is closely related to Kirundi of Burundi. Kinyarwanda is a tonal, agglutinative "
    "language: words are built by stacking prefixes and suffixes onto roots, and nouns belong to about "
    "sixteen noun classes that control agreement across the whole sentence. It is written in the Latin "
    "script with a straightforward, nearly phonetic spelling."
)

SCRIPT_DESC = (
    "Kinyarwanda uses the Latin alphabet with no special letters: a b c d e f g h i j k l m n o p r s t "
    "u v w y z. Spelling is nearly phonetic — read what you see. The letter c is always pronounced 'ch' "
    "(icupa, bottle), g is always hard (genda, go), and j is soft (ijambo, word). There are no silent "
    "letters and no tone marks in everyday writing."
)

ALPHABET_NOTE = (
    "The working alphabet is the 24-letter Latin set used by Kinyarwanda. The table below shows the "
    "letters that surprise English readers; the rest sound as in English. Master these six and you can "
    "sound out almost any Kinyarwanda word."
)

ALPHABET_SAMPLE = [
    ("c", "ch as in 'church'"), ("g", "always hard, as in 'go'"), ("j", "soft, as in 'jump'"),
    ("r", "lightly rolled"), ("y", "as in 'yes'"), ("z", "as in 'zebra'"),
    ("a", "as in 'father'"), ("e", "as in 'bet'"), ("i", "ee as in 'see'"),
    ("o", "as in 'go'"), ("u", "oo as in 'moon'"), ("w", "as in 'water'"),
]

SOUNDS_DESC = (
    "Kinyarwanda has five vowels (a e i o u) and two tones, high and low, that can change meaning — "
    "context usually makes the meaning clear for beginners. Consonants are mostly as in English, with "
    "the key exceptions: c = 'ch', g always hard, j soft. The combinations bw, tw, rw and similar are "
    "single smooth sounds (Rwanda is pronounced with a quick 'rw'). Syllables are open — every syllable "
    "ends in a vowel — which gives the language its flowing rhythm."
)

GRAMMAR_DESC = (
    "Kinyarwanda is subject-verb-object, like English. Its engine is the noun-class system: every noun "
    "belongs to a class marked by a prefix (umu- for people singular, aba- for people plural, iki- for "
    "things, ibi- for things plural), and adjectives, verbs and pronouns all take matching prefixes. "
    "There are no articles. Negation is marked on the verb with si- or nti-. Tense is marked by infixes "
    "between the subject prefix and the verb root: nda- marks the present ('I am ...-ing')."
)

TENSE_DESC = (
    "Tense lives inside the verb, between the subject marker and the root. Ndakora = 'I am working' "
    "(n-da-kor-a: I-present-work); nakoze = 'I worked'; nzakora = 'I will work'. Learn the three "
    "shapes of a handful of verbs — gukora (to work), kurya (to eat), kugenda (to go) — and the whole "
    "system opens. The examples below keep the subject 'I' (n-) so you can watch only the tense infix "
    "change."
)

REGISTER_DESC = (
    "Respect in Kinyarwanda is carried by pronouns and greetings. Muraho (hello, formal) opens any "
    "first meeting; bite is for friends. Mwaramutse (good morning) and mwiriwe (good afternoon/evening) "
    "show you know the time of day. The plural murakoze (thank you) is more respectful than the singular "
    "urakoze. Elders are addressed with titles and never rushed; a proper greeting exchange — muraho, "
    "amakuru, ni meza — is a small ceremony, not a transaction."
)

COMPLEX_DESC = (
    "Kinyarwanda links clauses with kuko (because), ariko (but), and kugira ngo (so that). Relative "
    "clauses follow the noun with a matching class prefix: umuntu ukora (the person who works). "
    "Conditions use niba (if). Because agreement prefixes repeat the noun class everywhere, long "
    "sentences stay clear — follow the prefixes and you always know which noun each verb belongs to."
)

REVIEW_NOTE = (
    "You now hold the complete Kinyarwanda ladder: the phonetic Latin script, five vowels and two "
    "tones, the noun-class engine with SVO order, core nouns verbs and adjectives, pronouns, numbers "
    "to one hundred, time words, greetings, ten themed sentence sets, the three-shape verb tenses, "
    "questions, commands, descriptions, three graded stories, imigani proverbs, formal registers, and "
    "three full conversations. Speak the prefixes aloud — they are the music of the language."
)

NOUNS = [
    ("amazi", "amazi", "water", "Amazi ni meza.", "amazi ni meza", "Water is good."),
    ("umugabo", "umugabo", "man", "Umugabo ni mwiza.", "umugabo ni mwiza", "The man is good."),
    ("umugore", "umugore", "woman", "Umugore ni mwiza.", "umugore ni mwiza", "The woman is good."),
    ("umwana", "umwana", "child", "Umwana ni mwiza.", "umwana ni mwiza", "The child is good."),
    ("inzu", "inzu", "house", "Inzu ni nziza.", "inzu ni nziza", "The house is good."),
    ("igitabo", "igitabo", "book", "Igitabo ni cyiza.", "igitabo ni cyiza", "The book is good."),
    ("imodoka", "imodoka", "car", "Imodoka ni nziza.", "imodoka ni nziza", "The car is good."),
    ("isoko", "isoko", "market", "Isoko ni rinini.", "isoko ni rinini", "The market is big."),
    ("ishuri", "ishuri", "school", "Ishuri ni ryiza.", "ishuri ni ryiza", "The school is good."),
    ("umuceri", "umuceri", "rice", "Umuceri ni mwiza.", "umuceri ni mwiza", "The rice is good."),
    ("inyama", "inyama", "meat", "Inyama ni nziza.", "inyama ni nziza", "The meat is good."),
    ("urukundo", "urukundo", "love", "Urukundo ni rwiza.", "urukundo ni rwiza", "Love is good."),
]

VERBS = [
    ("gukunda", "gukunda", "to love", "Gukunda ni byiza.", "gukunda ni byiza", "Loving is good."),
    ("kurya", "kurya", "to eat", "Kurya ni byiza.", "kurya ni byiza", "Eating is good."),
    ("kunywa", "kunywa", "to drink", "Kunywa ni byiza.", "kunywa ni byiza", "Drinking is good."),
    ("kugenda", "kugenda", "to go", "Kugenda ni byiza.", "kugenda ni byiza", "Going is good."),
    ("kuza", "kuza", "to come", "Kuza ni byiza.", "kuza ni byiza", "Coming is good."),
    ("kuvuga", "kuvuga", "to speak", "Kuvuga ni byiza.", "kuvuga ni byiza", "Speaking is good."),
    ("gukora", "gukora", "to work", "Gukora ni byiza.", "gukora ni byiza", "Working is good."),
    ("kwiga", "kwiga", "to learn", "Kwiga ni byiza.", "kwiga ni byiza", "Learning is good."),
    ("kuguha", "kuguha", "to give", "Kuguha ni byiza.", "kuguha ni byiza", "Giving is good."),
    ("kubaho", "kubaho", "to live", "Kubaho ni byiza.", "kubaho ni byiza", "Living is good."),
]

ADJS = [
    ("mwiza", "mwiza", "good, beautiful", "umwana mwiza", "umwana mwiza", "a good child"),
    ("mubi", "mubi", "bad, ugly", "umwana mubi", "umwana mubi", "a bad child"),
    ("munini", "munini", "big", "inzu nini", "inzu nini", "a big house"),
    ("muto", "muto", "small", "inzu nto", "inzu nto", "a small house"),
    ("mushya", "mushya", "new", "igitabo gishya", "igitabo gishya", "a new book"),
    ("mukuru", "mukuru", "old, elder", "umugabo mukuru", "umugabo mukuru", "an old man"),
    ("mutuku", "mutuku", "red", "imodoka itukura", "imodoka itukura", "a red car"),
    ("mweru", "mweru", "white, clean", "ikanzu yera", "ikanzu yera", "a white shirt"),
]

PRONOUNS = [
    ("njye", "njye", "I"),
    ("wowe", "wowe", "you (singular)"),
    ("we", "we", "he / she"),
    ("twe", "twe", "we"),
    ("mwe", "mwe", "you (plural / formal)"),
    ("bo", "bo", "they"),
    ("uyu", "uyu", "this one"),
    ("uriya", "uriya", "that one"),
]

NUMBERS = [
    ("rimwe", "rimwe", "one"), ("kabiri", "kabiri", "two"), ("gatatu", "gatatu", "three"),
    ("kane", "kane", "four"), ("gatanu", "gatanu", "five"), ("gatandatu", "gatandatu", "six"),
    ("karindwi", "karindwi", "seven"), ("umunani", "umunani", "eight"),
    ("icyenda", "icyenda", "nine"), ("icumi", "icumi", "ten"),
    ("makumyabiri", "makumyabiri", "twenty"), ("ijana", "ijana", "one hundred"),
]

TIME_WORDS = [
    ("uyu munsi", "uyu munsi", "today"), ("ejo", "ejo", "tomorrow"),
    ("ejo bundi", "ejo bundi", "yesterday"), ("icyumweru", "icyumweru", "week"),
    ("ukwezi", "ukwezi", "month"), ("umwaka", "umwaka", "year"),
]

GREETINGS = [
    ("Muraho!", "muraho", "Hello! (formal)"),
    ("Bite?", "bite", "Hi! (informal)"),
    ("Amakuru?", "amakuru", "How are you?"),
    ("Ni meza.", "ni meza", "I am fine."),
    ("Mwaramutse?", "mwaramutse", "Good morning?"),
    ("Mwiriwe?", "mwiriwe", "Good afternoon / evening?"),
    ("Murakoze.", "murakoze", "Thank you."),
    ("Murakoze cyane.", "murakoze cyane", "Thank you very much."),
    ("Murabeho.", "murabeho", "Goodbye."),
    ("Nyabuneka.", "nyabuneka", "Please."),
]

THEMES = [
    ("Home and Family", [
        ("umuryango", "umuryango", "family", "Umuryango ni mwiza.", "umuryango ni mwiza", "The family is good."),
        ("data", "data", "father", "Data ni mwiza.", "data ni mwiza", "Father is good."),
        ("mama", "mama", "mother", "Mama ni mwiza.", "mama ni mwiza", "Mother is good."),
        ("umwana", "umwana", "child", "Umwana arakina.", "umwana arakina", "The child is playing."),
        ("mukuru", "mukuru", "elder sibling", "Mukuru arafasha.", "mukuru arafasha", "The elder sibling helps."),
        ("murumuna", "murumuna", "younger sibling", "Murumuna ariga.", "murumuna ariga", "The younger sibling is learning."),
    ]),
    ("Food and Cooking", [
        ("ibiryo", "ibiryo", "food", "Ibiryo ni byiza.", "ibiryo ni byiza", "The food is good."),
        ("umuceri", "umuceri", "rice", "Umuceri uraryoshye.", "umuceri uraryoshye", "The rice is tasty."),
        ("inyama", "inyama", "meat", "Inyama zihenze.", "inyama zihenze", "The meat is expensive."),
        ("amazi", "amazi", "water", "Amazi ni meza.", "amazi ni meza", "The water is good."),
        ("amata", "amata", "milk", "Amata ni meza.", "amata ni meza", "The milk is good."),
        ("isukari", "isukari", "sugar", "Isukari zirahenze.", "isukari zirahenze", "The sugar is expensive."),
    ]),
    ("Travel and Directions", [
        ("umuhanda", "umuhanda", "road", "Umuhanda ni muremure.", "umuhanda ni muremure", "The road is long."),
        ("imodoka", "imodoka", "car", "Imodoka iragenda.", "imodoka iragenda", "The car is going."),
        ("indege", "indege", "airplane", "Indege irahaguruka.", "indege irahaguruka", "The plane is taking off."),
        ("gare", "gare", "station", "Gare iri hafi.", "gare iri hafi", "The station is near."),
        ("iburyo", "iburyo", "right", "Genda iburyo.", "genda iburyo", "Go right."),
        ("ibumoso", "ibumoso", "left", "Genda ibumoso.", "genda ibumoso", "Go left."),
    ]),
    ("Work and School", [
        ("akazi", "akazi", "work, job", "Akazi ni keza.", "akazi ni keza", "The work is good."),
        ("ishuri", "ishuri", "school", "Ishuri rirafunguye.", "ishuri rirafunguye", "The school is open."),
        ("umunyeshuri", "umunyeshuri", "student", "Umunyeshuri ariga.", "umunyeshuri ariga", "The student is learning."),
        ("mwarimu", "mwarimu", "teacher", "Mwarimu aravuga.", "mwarimu aravuga", "The teacher is speaking."),
        ("igitabo", "igitabo", "book", "Igitabo kirafunze.", "igitabo kirafunze", "The book is closed."),
        ("ikaramu", "ikaramu", "pen", "Ikaramu ni nziza.", "ikaramu ni nziza", "The pen is good."),
    ]),
    ("Health and the Body", [
        ("umubiri", "umubiri", "body", "Umubiri ni mwiza.", "umubiri ni mwiza", "The body is good."),
        ("umutwe", "umutwe", "head", "Umutwe urababara.", "umutwe urababara", "The head aches."),
        ("ijisho", "ijisho", "eye", "Ijisho rirareba.", "ijisho rirareba", "The eye sees."),
        ("ukuboko", "ukuboko", "arm, hand", "Ukuboko kurababara.", "ukuboko kurababara", "The arm hurts."),
        ("ikirenge", "ikirenge", "leg, foot", "Ikirenge kirababara.", "ikirenge kirababara", "The leg hurts."),
        ("umuganga", "umuganga", "doctor", "Umuganga aravura.", "umuganga aravura", "The doctor heals."),
    ]),
    ("Emotions and Feelings", [
        ("ibyishimo", "ibyishimo", "joy", "Ibyishimo ni byiza.", "ibyishimo ni byiza", "Joy is good."),
        ("agahinda", "agahinda", "sadness", "Agahinda karashize.", "agahinda karashize", "The sadness is gone."),
        ("ubwoba", "ubwoba", "fear", "Ubwoba burashize.", "ubwoba burashize", "The fear is gone."),
        ("urukundo", "urukundo", "love", "Urukundo rurakomeye.", "urukundo rurakomeye", "Love is strong."),
        ("ishyari", "ishyari", "jealousy", "Ishyari ni ribi.", "ishyari ni ribi", "Jealousy is bad."),
        ("amahoro", "amahoro", "peace", "Amahoro ni meza.", "amahoro ni meza", "Peace is good."),
    ]),
    ("Nature and Weather", [
        ("kamere", "kamere", "nature", "Kamere ni nziza.", "kamere ni nziza", "Nature is beautiful."),
        ("imvura", "imvura", "rain", "Imvura iragwa.", "imvura iragwa", "The rain is falling."),
        ("izuba", "izuba", "sun", "Izuba rirashyushye.", "izuba rirashyushye", "The sun is hot."),
        ("ukwezi", "ukwezi", "moon", "Ukwezi kurabagirana.", "ukwezi kurabagirana", "The moon is bright."),
        ("igiti", "igiti", "tree", "Igiti ni kinini.", "igiti ni kinini", "The tree is big."),
        ("ururabo", "ururabo", "flower", "Ururabo ni rwiza.", "ururabo ni rwiza", "The flower is beautiful."),
    ]),
    ("Shopping and Money", [
        ("amafaranga", "amafaranga", "money", "Amafaranga ni meza.", "amafaranga ni meza", "Money is good."),
        ("igiciro", "igiciro", "price", "Igiciro kiri hejuru.", "igiciro kiri hejuru", "The price is high."),
        ("iduka", "iduka", "shop", "Iduka rirafunguye.", "iduka rirafunguye", "The shop is open."),
        ("gihendutse", "gihendutse", "cheap", "Gihendutse ni cyiza.", "gihendutse ni cyiza", "Cheap is good."),
        ("umuguzi", "umuguzi", "customer", "Umuguzi arishimye.", "umuguzi arishimye", "The customer is happy."),
        ("umucuruzi", "umucuruzi", "seller", "Umucuruzi ni mwiza.", "umucuruzi ni mwiza", "The seller is good."),
    ]),
    ("Friendship and Social Life", [
        ("inshuti", "inshuti", "friend", "Inshuti ni nziza.", "inshuti ni nziza", "The friend is good."),
        ("kwakira neza", "kwakira neza", "hospitality", "Kwakira neza ni cyiza.", "kwakira neza ni cyiza", "Hospitality is good."),
        ("ikiganiro", "ikiganiro", "conversation", "Ikiganiro ni cyiza.", "ikiganiro ni cyiza", "The conversation is good."),
        ("ibirori", "ibirori", "feast", "Ibirori ni byiza.", "ibirori ni byiza", "The feast is good."),
        ("imbyino", "imbyino", "dance", "Imbyino ni nziza.", "imbyino ni nziza", "The dance is beautiful."),
        ("indirimbo", "indirimbo", "song", "Indirimbo ni nziza.", "indirimbo ni nziza", "The song is beautiful."),
    ]),
    ("Technology and Communication", [
        ("telefone", "telefone", "telephone", "Telefone iravuga.", "telefone iravuga", "The phone is ringing."),
        ("mudasobwa", "mudasobwa", "computer", "Mudasobwa irakora.", "mudasobwa irakora", "The computer is working."),
        ("murandasi", "murandasi", "internet", "Murandasi irihuta.", "murandasi irihuta", "The internet is fast."),
        ("amashanyarazi", "amashanyarazi", "electricity", "Amashanyarazi arahari.", "amashanyarazi arahari", "There is electricity."),
        ("ubutumwa", "ubutumwa", "message", "Ubutumwa bwaraje.", "ubutumwa bwaraje", "The message has arrived."),
        ("radiyo", "radiyo", "radio", "Radiyo iravuga.", "radiyo iravuga", "The radio is playing."),
    ]),
]
QUESTIONS = [
    ("Witwa nde?", "witwa nde", "What is your name?"),
    ("Mama ari he?", "mama ari he", "Where is mother?"),
    ("Ni angahe?", "ni angahe", "How much is it?"),
    ("Kuki?", "kuki", "Why?"),
    ("Ryari?", "ryari", "When?"),
    ("Uyu ni nde?", "uyu ni nde", "Who is this?"),
    ("Ibiryo bimeze gute?", "ibiryo bimeze gute", "How is the food?"),
    ("Uva he?", "uva he", "Where are you from?"),
]

COMMANDS = [
    ("Ngwino hano!", "ngwino hano", "Come here!"),
    ("Genda!", "genda", "Go!"),
    ("Icara hasi!", "icara hasi", "Sit down!"),
    ("Vuga buhoro!", "vuga buhoro", "Speak slowly!"),
    ("Mfasha!", "mfasha", "Help me!"),
    ("Tega amatwi!", "tega amatwi", "Listen!"),
    ("Reba!", "reba", "Look!"),
    ("Hagarara!", "hagarara", "Stop!"),
]

DESCRIBE = [
    ("Umugabo muremure, ni muremure.", "umugabo muremure ni muremure", "The tall man, he is tall."),
    ("Umugore mwiza, ni mwiza.", "umugore mwiza ni mwiza", "The beautiful woman, she is beautiful."),
    ("Inzu nini, ni nini.", "inzu nini ni nini", "The big house, it is big."),
    ("Imodoka itukura, ni itukura.", "imodoka itukura ni itukura", "The red car, it is red."),
    ("Umwana muto, ni muto.", "umwana muto ni muto", "The small child, he/she is small."),
    ("Igitabo gishya, ni gishya.", "igitabo gishya ni gishya", "The new book, it is new."),
    ("Izuba rishyushye, ririshyushye.", "izuba rishyushye ririshyushye", "The hot sun, it is hot."),
    ("Amazi akonje, arakonje.", "amazi akonje arakonje", "The cold water, it is cold."),
]
STORIES = [
    ("Story I: The Boy and the Lamb", [
        ("Hari umuhungu.", "hari umuhungu", "There was a boy."),
        ("Umuhungu afite intama.", "umuhungu afite intama", "The boy has a lamb."),
        ("Intama ni umweru.", "intama ni umweru", "The lamb is white."),
        ("Umuhungu akunda intama.", "umuhungu akunda intama", "The boy loves the lamb."),
        ("Umunsi umwe intama yazimiye.", "umunsi umwe intama yazimiye", "One day the lamb got lost."),
        ("Umuhungu yashakishije hose.", "umuhungu yashakishije hose", "The boy searched everywhere."),
        ("Amaherezo yayibonye.", "amaherezo yayibonye", "Finally he found it."),
        ("Yarishimye cyane.", "yarishimye cyane", "He was very happy."),
    ]),
    ("Story II: The Rainy Day", [
        ("Uyu munsi imvura iragwa.", "uyu munsi imvura iragwa", "Today the rain is falling."),
        ("Abana bari mu nzu.", "abana bari mu nzu", "The children stay in the house."),
        ("Mama arateka ibiryo.", "mama arateka ibiryo", "Mother is cooking food."),
        ("Ibiryo ni byiza.", "ibiryo ni byiza", "The food is good."),
        ("Data arasoma igitabo.", "data arasoma igitabo", "Father is reading a book."),
        ("Imvura imaze kugwa izuba ryavuye.", "imvura imaze kugwa izuba ryavuye", "After the rain the sun came out."),
        ("Abana basohotse.", "abana basohotse", "The children went outside."),
        ("Barakina mu rugo.", "barakina mu rugo", "They are playing in the yard."),
    ]),
    ("Story III: The Market Trip", [
        ("Ejo tuzajya ku isoko.", "ejo tuzajya ku isoko", "Tomorrow we go to the market."),
        ("Mama azagura umugati.", "mama azagura umugati", "Mother buys bread."),
        ("Data azagura inyama.", "data azagura inyama", "Father buys meat."),
        ("Umwana azagura ibombori.", "umwana azagura ibombori", "The child buys candy."),
        ("Umugati ni mwiza.", "umugati ni mwiza", "The bread is good."),
        ("Inyama zihenze.", "inyama zihenze", "The meat is expensive."),
        ("Twese tuzataha.", "twese tuzataha", "We all go home."),
        ("Twese tuzarya neza.", "twese tuzarya neza", "We all eat well."),
    ]),
]

IDIOMS = [
    ("Nta we uta akanyaga atagahambuye", "nta we uta akanyaga atagahambuye", "No one loses the young cow without having lost the calf's rope", "Loss is always paid twice over."),
    ("Utumviye se na nyina yumvira ijeri", "utumviye se na nyina yumvira ijeri", "Who does not listen to father and mother listens to the abyss", "Obedience saves; stubbornness falls."),
    ("Agahinda k'umugabo kamenywa n'undi", "agahinda k'umugabo kamenywa n'undi", "A man's pain is known by another", "Shared sorrow is understood."),
    ("Utaribwa n'umugabo arayirwa", "utaribwa n'umugabo arayirwa", "Who is not fought by a man is protected", "The protected need no battle."),
]

CONVOS = [
    ("At the Market", [
        ("A", "Muraho!", "muraho", "Hello!"),
        ("B", "Muraho! Ukeneye iki?", "muraho ukeneye iki", "Hello! What do you need?"),
        ("A", "Ni angahe?", "ni angahe", "How much is it?"),
        ("B", "Ni igihumbi.", "ni igihumbi", "It is one thousand."),
        ("A", "Irahenze.", "irahenze", "Expensive."),
        ("B", "Nzayigabanya.", "nzayigabanya", "I will lower it."),
        ("A", "Murakoze, nzayigura.", "murakoze nzayigura", "Thanks, I will buy it."),
        ("B", "Murabeho!", "murabeho", "Goodbye!"),
    ]),
    ("Meeting a Friend", [
        ("A", "Muraho, amakuru?", "muraho amakuru", "Hi, how are you?"),
        ("B", "Ni meza, murakoze. Nawe?", "ni meza murakoze nawe", "I am well, thanks. And you?"),
        ("A", "Nanjye ni meza.", "nanjye ni meza", "I am well too."),
        ("B", "Witwa nde?", "witwa nde", "What is your name?"),
        ("A", "Nitwa Jean.", "nitwa jean", "My name is Jean."),
        ("B", "Nishimiye kukumenya.", "nishimiye kukumenya", "Nice to meet you."),
        ("A", "Nanjye nishimye.", "nanjye nishimye", "Nice to meet you too."),
        ("B", "Tuzabonana!", "tuzabonana", "See you again!"),
    ]),
    ("Solving a Problem", [
        ("A", "Hari ikibazo.", "hari ikibazo", "There is a problem."),
        ("B", "Ni ikihe kibazo?", "ni ikihe kibazo", "What problem?"),
        ("A", "Imodoka yapfuye.", "imodoka yapfuye", "The car broke down."),
        ("B", "Witinya.", "witinya", "Do not worry."),
        ("A", "Mfasha!", "mfasha", "Help me!"),
        ("B", "Nzagufasha.", "nzagufasha", "I will help you."),
        ("A", "Murakoze cyane!", "murakoze cyane", "Thank you very much!"),
        ("B", "Nta cyo.", "nta cyo", "You are welcome."),
    ]),
]

CITATIONS = [
    "Omniglot. Useful phrases in Kinyarwanda.",
    "Wikivoyage contributors. Kinyarwanda phrasebook.",
    "Scholarly collections of Kinyarwanda proverbs (imigani): 'Nta we uta akanyaga atagahambuye', 'Utumviye se na nyina yumvira ijeri'.",
    "Jerrold's Kinyarwanda Online Dictionary (kimundi.com).",
    "ISO 639-1:2002 language code rw; ISO 639-3:2007 language code kin.",
    "Standard pedagogical sources for Kinyarwanda vocabulary, usage, and phraseology.",
]
