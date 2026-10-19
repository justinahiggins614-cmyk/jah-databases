# -*- coding: utf-8 -*-
"""Language data module: Xhosa (xho). Facts verified 2026-10-17 via
phrasebooks, amaqhalo collections."""

SLUG = "language-xhosa"
PREFIX = "JAH-LXHO-"
SIG_PREFIX = "JAH-LXHOS-"
NAME = "Xhosa"
NATIVE = "isiXhosa"
NATIVE_ROMAN = "isiXhosa"
ISO1 = "xh"
ISO3 = "xho"
FAMILY = "Niger-Congo > Atlantic-Congo > Benue-Congo > Bantoid > Bantu (Nguni group)"
SPEAKERS = "about 19 to 20 million speakers (first and second language)"
REGIONS = "South Africa, where it is an official language, especially the Eastern Cape and Western Cape; also Zimbabwe and Lesotho"
SCRIPT_NAME = "Latin script"
WORD_ORDER = "subject-verb-object (SVO)"
AI_NAME = "JAH Xhosa Language Archivist"
SIG_AI_NAME = "JAH Xhosa Signature Archivist"

OVERVIEW = (
    "Xhosa (isiXhosa) is a Bantu language of the Nguni group, spoken by about 19 to 20 million people, "
    "most of them in South Africa where it is an official language. It is famous worldwide for its click "
    "consonants — three basic clicks written c, x and q — borrowed from long contact with Khoisan "
    "languages. Like its Nguni relatives, Xhosa runs on a noun-class system of about fifteen classes "
    "whose prefixes control agreement across the sentence. It is written in the Latin script."
)

SCRIPT_DESC = (
    "Xhosa uses the Latin alphabet with three extra click letters: c (the dental click, tongue behind "
    "the teeth, like a 'tsk' of annoyance), x (the lateral click, tongue on the side of the mouth, like "
    "urging a horse), and q (the alveolar click, tongue on the roof of the mouth, like a clock ticking). "
    "The digraphs hl (as in Welsh 'll'), dl, tsh, kh and ng also matter. Vowels are pure: a e i o u, "
    "pronounced as in Spanish."
)

ALPHABET_NOTE = (
    "The working alphabet is the Latin set plus the three click letters and the aspirated digraphs. "
    "The table shows the sounds that make Xhosa Xhosa; ordinary letters sound as in English, with g "
    "always hard."
)

ALPHABET_SAMPLE = [
    ("c", "dental click — 'tsk' behind the teeth"), ("x", "lateral click — urging a horse"),
    ("q", "alveolar click — clock ticking"), ("hl", "like Welsh 'll'"),
    ("kh", "aspirated k"), ("tsh", "like 'ch' in 'church'"),
    ("a", "as in 'hard'"), ("e", "as in 'red'"), ("i", "ee as in 'seen'"),
    ("o", "as in 'all'"), ("u", "oo as in 'moon'"), ("g", "always as in 'go'"),
]

SOUNDS_DESC = (
    "Xhosa vowels are short and pure: a (hard), e (red), i (seen), o (all), u (moon). The three clicks "
    "each combine with g, n and aspiration to make eighteen click sounds — start with the plain c, x, q "
    "and add the rest later. Tones are high and low and mark grammar as much as meaning: the same word "
    "can be a statement or a question depending on tone. The famous word 'Xhosa' itself begins with the "
    "lateral click."
)

GRAMMAR_DESC = (
    "Xhosa is subject-verb-object with a fifteen-class noun system: um- marks singular people (umntu, "
    "person), aba- plural people (abantu), in-/im- many things (inja, dog), izi- their plurals. "
    "Adjectives, verbs and pronouns all echo the class prefix. There are no articles. The verb carries "
    "subject, tense and object markers in one long word: ndiyabona = 'I see him/her' (ndi-ya-ba-on-a). "
    "Negation wraps the verb with a- ... -nga or uses the negative subject prefixes."
)

TENSE_DESC = (
    "Tense lives in infixes after the subject marker. Ndiyahamba = 'I am going' (ndi-ya-hamb-a); "
    "ndihambile = 'I have gone'; ndizahamba = 'I will go'. The examples below hold the subject 'I' "
    "(ndi-) steady on three everyday verbs — ukuhamba (to go), ukutya (to eat), ukusebenza (to work) — "
    "so you can watch only the tense marker move."
)

REGISTER_DESC = (
    "Respect in Xhosa is audible. Molweni greets a group; molo greets one person informally. Elders "
    "receive camagu, a word of deep respect meaning 'I acknowledge you', and are addressed as tata "
    "(father/sir) or mama (mother/ma'am). The formal ndiyabulela (I thank) outranks casual enkosi with "
    "strangers. Speak softly, greet everyone present in turn, and let the elder speak first — language "
    "and manners are one thing."
)

COMPLEX_DESC = (
    "Xhosa joins clauses with kuba (because), kodwa (but), and ukuze (so that). Relative clauses follow "
    "the noun with an agreeing prefix: umntu osebenzayo (the person who works). Conditions use ukuba "
    "(if). The agreeing prefixes repeat the noun class everywhere, so long sentences stay anchored — "
    "track the prefixes and you always know who is doing what."
)

REVIEW_NOTE = (
    "You now hold the complete Xhosa ladder: the Latin script with its three clicks, pure vowels and "
    "tones, the noun-class engine with SVO order, core nouns verbs and adjectives, pronouns, numbers to "
    "one hundred, time words, greetings, ten themed sentence sets, the infix verb tenses, questions, "
    "commands, descriptions, three graded stories, amaqhalo proverbs, formal registers, and three full "
    "conversations. Click gently, speak the prefixes, and the language opens."
)

NOUNS = [
    ("amanzi", "amanzi", "water", "Amanzi mahle.", "amanzi mahle", "The water is good."),
    ("indoda", "indoda", "man", "Indoda ilungile.", "indoda ilungile", "The man is good."),
    ("umfazi", "umfazi", "woman", "Umfazi ulungile.", "umfazi ulungile", "The woman is good."),
    ("umntwana", "umntwana", "child", "Umntwana ulungile.", "umntwana ulungile", "The child is good."),
    ("indlu", "indlu", "house", "Indlu inkulu.", "indlu inkulu", "The house is big."),
    ("incwadi", "incwadi", "book", "Incwadi intle.", "incwadi intle", "The book is good."),
    ("imoto", "imoto", "car", "Imoto intle.", "imoto intle", "The car is good."),
    ("ukutya", "ukutya", "food", "Ukutya kumnandi.", "ukutya kumnandi", "The food is tasty."),
    ("isikolo", "isikolo", "school", "Isikolo sihle.", "isikolo sihle", "The school is good."),
    ("ivenkile", "ivenkile", "shop", "Ivenkile inkulu.", "ivenkile inkulu", "The shop is big."),
    ("uthando", "uthando", "love", "Uthando luhle.", "uthando luhle", "Love is good."),
    ("ilanga", "ilanga", "sun", "Ilanga liyashisa.", "ilanga liyashisa", "The sun is hot."),
]

VERBS = [
    ("ukuthanda", "ukuthanda", "to love", "Ukuthanda kuhle.", "ukuthanda kuhle", "Loving is good."),
    ("ukutya", "ukutya", "to eat", "Ukutya kuhle.", "ukutya kuhle", "Eating is good."),
    ("ukusela", "ukusela", "to drink", "Ukusela kuhle.", "ukusela kuhle", "Drinking is good."),
    ("ukuhamba", "ukuhamba", "to go", "Ukuhamba kuhle.", "ukuhamba kuhle", "Going is good."),
    ("ukuza", "ukuza", "to come", "Ukuza kuhle.", "ukuza kuhle", "Coming is good."),
    ("ukuthetha", "ukuthetha", "to speak", "Ukuthetha kuhle.", "ukuthetha kuhle", "Speaking is good."),
    ("ukusebenza", "ukusebenza", "to work", "Ukusebenza kuhle.", "ukusebenza kuhle", "Working is good."),
    ("ukufunda", "ukufunda", "to learn", "Ukufunda kuhle.", "ukufunda kuhle", "Learning is good."),
    ("ukunika", "ukunika", "to give", "Ukunika kuhle.", "ukunika kuhle", "Giving is good."),
    ("ukuphila", "ukuphila", "to live", "Ukuphila kuhle.", "ukuphila kuhle", "Living is good."),
]

ADJS = [
    ("hle", "hle", "good, beautiful", "umntwana omhle", "umntwana omhle", "a good child"),
    ("bi", "bi", "bad, ugly", "umntwana ombi", "umntwana ombi", "a bad child"),
    ("khulu", "khulu", "big", "indlu enkulu", "indlu enkulu", "a big house"),
    ("ncinci", "ncinci", "small", "indlu encinci", "indlu encinci", "a small house"),
    ("tsha", "tsha", "new", "imoto entsha", "imoto entsha", "a new car"),
    ("dala", "dala", "old", "indlu endala", "indlu endala", "an old house"),
    ("bomvu", "bomvu", "red", "imoto ebomvu", "imoto ebomvu", "a red car"),
    ("mhlophe", "mhlophe", "white", "ihempe emhlophe", "ihempe emhlophe", "a white shirt"),
]

PRONOUNS = [
    ("mna", "mna", "I"),
    ("wena", "wena", "you (singular)"),
    ("yena", "yena", "he / she"),
    ("thina", "thina", "we"),
    ("nina", "nina", "you (plural)"),
    ("bona", "bona", "they"),
    ("lo", "lo", "this one"),
    ("lowaya", "lowaya", "that one"),
]

NUMBERS = [
    ("inye", "inye", "one"), ("zimbini", "zimbini", "two"), ("zintathu", "zintathu", "three"),
    ("ezine", "ezine", "four"), ("ezintlanu", "ezintlanu", "five"), ("isithandathu", "isithandathu", "six"),
    ("isixhenxe", "isixhenxe", "seven"), ("isibhozo", "isibhozo", "eight"),
    ("ithoba", "ithoba", "nine"), ("ishumi", "ishumi", "ten"),
    ("amashumi amabini", "amashumi amabini", "twenty"), ("ikhulu", "ikhulu", "one hundred"),
]

TIME_WORDS = [
    ("namhlanje", "namhlanje", "today"), ("ngomso", "ngomso", "tomorrow"),
    ("izolo", "izolo", "yesterday"), ("iveki", "iveki", "week"),
    ("inyanga", "inyanga", "month"), ("unyaka", "unyaka", "year"),
]

GREETINGS = [
    ("Molo!", "molo", "Hello! (to one person)"),
    ("Molweni!", "molweni", "Hello! (to a group)"),
    ("Unjani?", "unjani", "How are you?"),
    ("Ndiphilile.", "ndiphilile", "I am well."),
    ("Ndiphilile, enkosi.", "ndiphilile enkosi", "I am well, thank you."),
    ("Enkosi.", "enkosi", "Thank you."),
    ("Enkosi kakhulu.", "enkosi kakhulu", "Thank you very much."),
    ("Ndicela.", "ndicela", "Please."),
    ("Uxolo.", "uxolo", "Sorry / excuse me."),
    ("Sala kakuhle.", "sala kakuhle", "Goodbye (stay well)."),
]

THEMES = [
    ("Home and Family", [
        ("usapho", "usapho", "family", "Usapho luhle.", "usapho luhle", "The family is good."),
        ("utata", "utata", "father", "Utata ulungile.", "utata ulungile", "Father is good."),
        ("umama", "umama", "mother", "Umama ulungile.", "umama ulungile", "Mother is good."),
        ("umzalwana", "umzalwana", "sibling", "Umzalwana uyanceda.", "umzalwana uyanceda", "The sibling helps."),
        ("utatomkhulu", "utatomkhulu", "grandfather", "Utatomkhulu uhloniphekile.", "utatomkhulu uhloniphekile", "Grandfather is respected."),
        ("umakhulu", "umakhulu", "grandmother", "Umakhulu uhloniphekile.", "umakhulu uhloniphekile", "Grandmother is respected."),
    ]),
    ("Food and Cooking", [
        ("ukutya", "ukutya", "food", "Ukutya kumnandi.", "ukutya kumnandi", "The food is tasty."),
        ("isonka", "isonka", "bread", "Isonka simnandi.", "isonka simnandi", "The bread is tasty."),
        ("inyama", "inyama", "meat", "Inyama ibiza.", "inyama ibiza", "The meat is expensive."),
        ("amanzi", "amanzi", "water", "Amanzi mahle.", "amanzi mahle", "The water is good."),
        ("ubisi", "ubisi", "milk", "Ubisi luhle.", "ubisi luhle", "The milk is good."),
        ("iswekile", "iswekile", "sugar", "Iswekile ibiza.", "iswekile ibiza", "The sugar is expensive."),
    ]),
    ("Travel and Directions", [
        ("indlela", "indlela", "road, path", "Indlela inde.", "indlela inde", "The road is long."),
        ("imoto", "imoto", "car", "Imoto iyahamba.", "imoto iyahamba", "The car is going."),
        ("inqwelomoya", "inqwelomoya", "airplane", "Inqwelomoya iyaphapha.", "inqwelomoya iyaphapha", "The plane is flying."),
        ("isikhululo", "isikhululo", "station", "Isikhululo sikufuphi.", "isikhululo sikufuphi", "The station is near."),
        ("ekunene", "ekunene", "right", "Hamba ekunene.", "hamba ekunene", "Go right."),
        ("ekhohlo", "ekhohlo", "left", "Hamba ekhohlo.", "hamba ekhohlo", "Go left."),
    ]),
    ("Work and School", [
        ("umsebenzi", "umsebenzi", "work, job", "Umsebenzi ulungile.", "umsebenzi ulungile", "The work is good."),
        ("isikolo", "isikolo", "school", "Isikolo sivuliwe.", "isikolo sivuliwe", "The school is open."),
        ("umfundi", "umfundi", "student", "Umfundi uyafunda.", "umfundi uyafunda", "The student is learning."),
        ("utitshala", "utitshala", "teacher", "Utitshala uyathetha.", "utitshala uyathetha", "The teacher is speaking."),
        ("incwadi", "incwadi", "book", "Incwadi ivaliwe.", "incwadi ivaliwe", "The book is closed."),
        ("usiba", "usiba", "pen", "Usiba luhle.", "usiba luhle", "The pen is good."),
    ]),
    ("Health and the Body", [
        ("umzimba", "umzimba", "body", "Umzimba ulungile.", "umzimba ulungile", "The body is good."),
        ("intloko", "intloko", "head", "Intloko iyaphatha.", "intloko iyaphatha", "The head aches."),
        ("iliso", "iliso", "eye", "Iliso liyabona.", "iliso liyabona", "The eye sees."),
        ("ingalo", "ingalo", "arm", "Ingalo iyaphatha.", "ingalo iyaphatha", "The arm aches."),
        ("umlenze", "umlenze", "leg", "Umlenze uyaphatha.", "umlenze uyaphatha", "The leg aches."),
        ("ugqirha", "ugqirha", "doctor", "Ugqirha uyaphilisa.", "ugqirha uyaphilisa", "The doctor heals."),
    ]),
    ("Emotions and Feelings", [
        ("uvuyo", "uvuyo", "joy", "Uvuyo luhle.", "uvuyo luhle", "Joy is good."),
        ("usizi", "usizi", "sadness", "Usizi luhambile.", "usizi luhambile", "The sadness is gone."),
        ("uloyiko", "uloyiko", "fear", "Uloyiko luhambile.", "uloyiko luhambile", "The fear is gone."),
        ("uthando", "uthando", "love", "Uthando lunamandla.", "uthando lunamandla", "Love is strong."),
        ("ukona", "ukona", "jealousy", "Ukona kubi.", "ukona kubi", "Jealousy is bad."),
        ("uxolo", "uxolo", "peace", "Uxolo luhle.", "uxolo luhle", "Peace is good."),
    ]),
    ("Nature and Weather", [
        ("indalo", "indalo", "nature", "Indalo intle.", "indalo intle", "Nature is beautiful."),
        ("imvula", "imvula", "rain", "Imvula iyanetha.", "imvula iyanetha", "The rain is falling."),
        ("ilanga", "ilanga", "sun", "Ilanga liyashisa.", "ilanga liyashisa", "The sun is hot."),
        ("inyanga", "inyanga", "moon", "Inyanga iyakhanya.", "inyanga iyakhanya", "The moon is shining."),
        ("umthi", "umthi", "tree", "Umthi mkhulu.", "umthi mkhulu", "The tree is big."),
        ("intyatyambo", "intyatyambo", "flower", "Intyatyambo intle.", "intyatyambo intle", "The flower is beautiful."),
    ]),
    ("Shopping and Money", [
        ("imali", "imali", "money", "Imali intle.", "imali intle", "Money is good."),
        ("ixabiso", "ixabiso", "price", "Ixabiso liphezulu.", "ixabiso liphezulu", "The price is high."),
        ("ivenkile", "ivenkile", "shop", "Ivenkile ivuliwe.", "ivenkile ivuliwe", "The shop is open."),
        ("isaphulelo", "isaphulelo", "discount", "Isaphulelo sihle.", "isaphulelo sihle", "The discount is good."),
        ("umthengi", "umthengi", "customer", "Umthengi uyonwabile.", "umthengi uyonwabile", "The customer is happy."),
        ("umthengisi", "umthengisi", "seller", "Umthengisi ulungile.", "umthengisi ulungile", "The seller is good."),
    ]),
    ("Friendship and Social Life", [
        ("umhlobo", "umhlobo", "friend", "Umhlobo ulungile.", "umhlobo ulungile", "The friend is good."),
        ("ubuntu", "ubuntu", "humanity, compassion", "Ubuntu luhle.", "ubuntu luhle", "Ubuntu is good."),
        ("incoko", "incoko", "conversation", "Incoko intle.", "incoko intle", "The conversation is good."),
        ("isidlo", "isidlo", "meal, feast", "Isidlo simnandi.", "isidlo simnandi", "The meal is tasty."),
        ("umdaniso", "umdaniso", "dance", "Umdaniso muhle.", "umdaniso muhle", "The dance is beautiful."),
        ("ingoma", "ingoma", "song", "Ingoma intle.", "ingoma intle", "The song is beautiful."),
    ]),
    ("Technology and Communication", [
        ("ifowuni", "ifowuni", "telephone", "Ifowuni iyakhala.", "ifowuni iyakhala", "The phone is ringing."),
        ("ikhompyutha", "ikhompyutha", "computer", "Ikhompyutha iyasebenza.", "ikhompyutha iyasebenza", "The computer is working."),
        ("i-intanethi", "i-intanethi", "internet", "I-intanethi iyakhawuleza.", "i-intanethi iyakhawuleza", "The internet is fast."),
        ("umbane", "umbane", "electricity", "Umbane ukhona.", "umbane ukhona", "There is electricity."),
        ("umyalezo", "umyalezo", "message", "Umyalezo ufikile.", "umyalezo ufikile", "The message has arrived."),
        ("irediyo", "irediyo", "radio", "Irediyo iyadlala.", "irediyo iyadlala", "The radio is playing."),
    ]),
]

QUESTIONS = [
    ("Ngubani igama lakho?", "ngubani igama lakho", "What is your name?"),
    ("Uphi umama?", "uphi umama", "Where is mother?"),
    ("Yimalini le?", "yimalini le", "How much is this?"),
    ("Kutheni?", "kutheni", "Why?"),
    ("Nini?", "nini", "When?"),
    ("Ngubani lo?", "ngubani lo", "Who is this?"),
    ("Kunjani ukutya?", "kunjani ukutya", "How is the food?"),
    ("Uvelaphi?", "uvelaphi", "Where are you from?"),
]

COMMANDS = [
    ("Yiza apha!", "yiza apha", "Come here!"),
    ("Hamba!", "hamba", "Go!"),
    ("Hlala phantsi!", "hlala phantsi", "Sit down!"),
    ("Thetha kancinci!", "thetha kancinci", "Speak a little!"),
    ("Ndincede!", "ndincede", "Help me!"),
    ("Mamela!", "mamela", "Listen!"),
    ("Jonga!", "jonga", "Look!"),
    ("Misa!", "misa", "Stop!"),
]

DESCRIBE = [
    ("Indoda ende, inde.", "indoda ende inde", "The tall man, he is tall."),
    ("Umfazi omhle, omhle.", "umfazi omhle omhle", "The beautiful woman, she is beautiful."),
    ("Indlu enkulu, inkulu.", "indlu enkulu inkulu", "The big house, it is big."),
    ("Imoto ebomvu, ibomvu.", "imoto ebomvu ibomvu", "The red car, it is red."),
    ("Umntwana omncinci, umncinci.", "umntwana omncinci umncinci", "The small child, he/she is small."),
    ("Incwadi entsha, intsha.", "incwadi entsha intsha", "The new book, it is new."),
    ("Ilanga elishisayo, liyashisa.", "ilanga elishisayo liyashisa", "The hot sun, it is hot."),
    ("Amanzi abandayo, abandayo.", "amanzi abandayo abandayo", "The cold water, it is cold."),
]

STORIES = [
    ("Story I: The Boy and the Goat", [
        ("Kwakukho inkwenkwe.", "kwakukho inkwenkwe", "There was a boy."),
        ("Inkwenkwe inebhokwe.", "inkwenkwe inebhokwe", "The boy has a goat."),
        ("Ibhokwe imhlophe.", "ibhokwe imhlophe", "The goat is white."),
        ("Inkwenkwe iyayithanda ibhokwe.", "inkwenkwe iyayithanda ibhokwe", "The boy loves the goat."),
        ("Ngenye imini ibhokwe yalahleka.", "ngenye imini ibhokwe yalahleka", "One day the goat got lost."),
        ("Inkwenkwe yakhangela yonke indawo.", "inkwenkwe yakhangela yonke indawo", "The boy searched everywhere."),
        ("Ekugqibeleni wayifumana.", "ekugqibeleni wayifumana", "Finally he found it."),
        ("Wavuya kakhulu.", "wavuya kakhulu", "He was very happy."),
    ]),
    ("Story II: The Rainy Day", [
        ("Namhlanje imvula iyanetha.", "namhlanje imvula iyanetha", "Today the rain is falling."),
        ("Abantwana bahlala endlwini.", "abantwana bahlala endlwini", "The children stay in the house."),
        ("Umama upheka ukutya.", "umama upheka ukutya", "Mother is cooking food."),
        ("Ukutya kumnandi.", "ukutya kumnandi", "The food is tasty."),
        ("Utata ufunda incwadi.", "utata ufunda incwadi", "Father is reading a book."),
        ("Emva kwemvula ilanga liphumile.", "emva kwemvula ilanga liphumile", "After the rain the sun came out."),
        ("Abantwana baphumela ngaphandle.", "abantwana baphumela ngaphandle", "The children went outside."),
        ("Badlala egadini.", "badlala egadini", "They are playing in the garden."),
    ]),
    ("Story III: The Market Trip", [
        ("Ngomso siya evenkileni.", "ngomso siya evenkileni", "Tomorrow we go to the shop."),
        ("Umama uthenga isonka.", "umama uthenga isonka", "Mother buys bread."),
        ("Utata uthenga inyama.", "utata uthenga inyama", "Father buys meat."),
        ("Umntwana uthenga iilekese.", "umntwana uthenga iilekese", "The child buys sweets."),
        ("Isonka simnandi.", "isonka simnandi", "The bread is tasty."),
        ("Inyama ibiza.", "inyama ibiza", "The meat is expensive."),
        ("Sihamba sonke ekhaya.", "sihamba sonke ekhaya", "We all go home."),
        ("Sitya sonke simnandi.", "sitya sonke simnandi", "We all eat tastily."),
    ]),
]

IDIOMS = [
    ("Umntu ngumntu ngabantu", "umntu ngumntu ngabantu", "A person is a person through other people", "Our humanity comes from our relationships — the spirit of ubuntu."),
    ("Akukho mvula ingayeki ukunqena", "akukho mvula ingayeki ukunqena", "There is no rain that does not stop", "Hard times always pass."),
    ("Ukuqala kuxolelwa, ukuphinda akubikho", "ukuqala kuxolelwa ukuphinda akubikho", "Starting is forgiven, repeating is not", "Learn from the first mistake; do not repeat it."),
    ("Amaxesha onke ayalunga", "amaxesha onke ayalunga", "All seasons are good", "Patience and resilience in every circumstance."),
    ("Intloko ayinciphi ngokubaleka", "intloko ayinciphi ngokubaleka", "The head does not shrink by running away", "Face challenges directly instead of avoiding them."),
    ("Inyembezi kayilibali", "inyembezi kayilibali", "Tears do not lie", "Genuine emotion tells the truth."),
]

CONVOS = [
    ("At the Market", [
        ("A", "Molo!", "molo", "Hello!"),
        ("B", "Molo! Ufuna ntoni?", "molo ufuna ntoni", "Hello! What do you want?"),
        ("A", "Yimalini le?", "yimalini le", "How much is this?"),
        ("B", "Lishumi.", "lishumi", "Ten."),
        ("A", "Kuyabiza.", "kuyabiza", "Expensive."),
        ("B", "Ndingayithoba.", "ndingayithoba", "I can lower it."),
        ("A", "Enkosi, ndiyayithatha.", "enkosi ndiyayithatha", "Thanks, I will take it."),
        ("B", "Hamba kakuhle!", "hamba kakuhle", "Goodbye!"),
    ]),
    ("Meeting a Friend", [
        ("A", "Molo, unjani?", "molo unjani", "Hi, how are you?"),
        ("B", "Ndiphilile, enkosi. Wena unjani?", "ndiphilile enkosi wena unjani", "I am fine, thanks. And you?"),
        ("A", "Nam ndiphilile.", "nam ndiphilile", "I am fine too."),
        ("B", "Ungubani igama lakho?", "ungubani igama lakho", "What is your name?"),
        ("A", "Igama lam nguSipho.", "igama lam nguSipho", "My name is Sipho."),
        ("B", "Kuhle ukukwazi.", "kuhle ukukwazi", "Nice to meet you."),
        ("A", "Nam kuhle.", "nam kuhle", "Nice to meet you too."),
        ("B", "Sizobonana!", "sizobonana", "See you again!"),
    ]),
    ("Solving a Problem", [
        ("A", "Kukho ingxaki.", "kukho ingxaki", "There is a problem."),
        ("B", "Yintoni ingxaki?", "yintoni ingxaki", "What problem?"),
        ("A", "Imoto yonakele.", "imoto yonakele", "The car broke down."),
        ("B", "Musa ukukhathazeka.", "musa ukukhathazeka", "Do not worry."),
        ("A", "Ndincede!", "ndincede", "Help me!"),
        ("B", "Ndizakunceda.", "ndizakunceda", "I will help you."),
        ("A", "Enkosi kakhulu!", "enkosi kakhulu", "Thank you very much!"),
        ("B", "Wamkelekile.", "wamkelekile", "You are welcome."),
    ]),
]

CITATIONS = [
    "Omniglot. Useful phrases in Xhosa.",
    "Wikivoyage contributors. Xhosa phrasebook.",
    "Scholarly collections of Xhosa proverbs (amaqhalo): 'Umntu ngumntu ngabantu', 'Akukho mvula ingayeki ukunqena', 'Amaxesha onke ayalunga'.",
    "Pahl H.W. The Xhosa Proverb (studies of Xhosa oral literature).",
    "ISO 639-1:2002 language code xh; ISO 639-3:2007 language code xho.",
    "Standard pedagogical sources for Xhosa vocabulary, usage, and phraseology.",
]
