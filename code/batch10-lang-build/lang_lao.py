# -*- coding: utf-8 -*-
"""Language data module: Lao (lao). Facts verified 2026-10-17 via
phrase references, ling-app proverbs."""

SLUG = "language-lao"
PREFIX = "JAH-LLAO-"
SIG_PREFIX = "JAH-LLAOS-"
NAME = "Lao"
NATIVE = "ພາສາລາວ"
NATIVE_ROMAN = "phasa lao"
ISO1 = "lo"
ISO3 = "lao"
FAMILY = "Kra-Dai (Tai-Kadai) > Tai > Southwestern Tai"
SPEAKERS = "about 30 million speakers (including Isan in Thailand)"
REGIONS = "Laos, where it is the official language, and northeastern Thailand (Isan); diaspora communities in France, the United States and Australia"
SCRIPT_NAME = "Lao script"
WORD_ORDER = "subject-verb-object (SVO)"
AI_NAME = "JAH Lao Language Archivist"
SIG_AI_NAME = "JAH Lao Signature Archivist"

OVERVIEW = (
    "Lao (ພາສາລາວ, phasa lao) is a tonal Tai language of the Kra-Dai family, spoken by about 30 million "
    "people. It is the official language of Laos and, in its Isan variety, the home language of millions "
    "in northeastern Thailand. Lao is closely related to Thai but written in its own rounder, more "
    "cursive script. It has six tones, no verb conjugations, no plurals and no articles — grammar is "
    "carried by word order and small helper words, which makes the first steps surprisingly gentle."
)

SCRIPT_DESC = (
    "Lao is written in its own Brahmic-derived script, read left to right. It has 27 consonants and a "
    "rich set of vowel symbols that can sit before, after, above or below the consonant. There are no "
    "spaces between words — spaces mark phrases and sentences. Lao has its own digits: ໐ ໑ ໒ ໓ ໔ ໕ "
    "໖ ໗ ໘ ໙ (0-9). Compared with Thai script, Lao letters are rounder and several letters were "
    "simplified away."
)

ALPHABET_NOTE = (
    "The working set is 27 consonants in three tone classes (high, middle, low) plus vowels. The table "
    "shows twelve high-frequency consonants with their names and sounds; vowels are learned as symbols "
    "around these."
)

ALPHABET_SAMPLE = [
    ("ກ", "ko kai — k"), ("ຂ", "kho khai — kh"), ("ຄ", "kho khon — kh"),
    ("ງ", "ngo ngua — ng"), ("ຈ", "cho chua — ch"), ("ສ", "so sua — s"),
    ("ດ", "do dek — d"), ("ຕ", "to tao — t"), ("ນ", "no nu — n"),
    ("ມ", "mo ma — m"), ("ລ", "lo ling — l"), ("ຫ", "ho ha — h"),
]

SOUNDS_DESC = (
    "Lao has six tones in the Vientiane standard: mid, low, falling, high, rising, and low-rising. Tone "
    "is decided by the consonant class plus the vowel length and final sound — a fully regular system "
    "once learned. Vowels come in short/long pairs (a/aa, i/ii, u/uu) and length changes meaning. "
    "Final consonants are unreleased: kin (eat) ends with a stopped 'n'. Speak softly, keep tones "
    "level and distinct, and you will be understood."
)

GRAMMAR_DESC = (
    "Lao grammar is famously lean: verbs never conjugate, nouns never change for plural, and there are "
    "no articles. Time is shown with helper words — ຈະ (cha) for future, ແລ້ວ (laeo) for completed "
    "action. Questions end with ບໍ່ (bo). Negation puts ບໍ່ (bo) before the verb: ຂ້ອຍບໍ່ເຂົ້າໃຈ "
    "(khoi bo khao chai — I do not understand). Classifiers count nouns: ຄົນ (khon) for people."
)

TENSE_DESC = (
    "Lao has no tenses on the verb — time floats on helper words. ຂ້ອຍກິນ (khoi kin) = I eat; "
    "ຂ້ອຍຈະກິນ (khoi cha kin) = I will eat; ຂ້ອຍກິນແລ້ວ (khoi kin laeo) = I ate / have eaten. The "
    "examples below show the same three verbs — ກິນ (kin, eat), ໄປ (pai, go), ເຮັດວຽກ (het viak, "
    "work) — in present, future and completed frames so you can watch only the helpers move."
)

REGISTER_DESC = (
    "Politeness in Lao is musical. Men end sentences with ຂ້ານ້ອຍ (khap) and women with ນ້ອຍ "
    "(noi) to soften everything they say. The nop gesture — palms together at the chest, higher for "
    "greater respect — accompanies greetings to elders and monks. ກະລຸນາ (karuna) marks formal "
    "requests. Never touch anyone's head, never point feet at people, and smile through small "
    "confusions — bo pen nyang (no problem) is a whole philosophy."
)

COMPLEX_DESC = (
    "Lao links ideas with ຍ້ອນວ່າ (nyon va, because), ແຕ່ (tae, but), and ເພື່ອ (pheua, in order to). "
    "Relative clauses follow the noun with ທີ່ (thi): ຄົນທີ່ເຮັດວຽກ (khon thi het viak — the person who "
    "works). Conditions use ຖ້າ (tha, if). Sentences chain short clauses with ແລ້ວ (laeo, then) — "
    "think in beads on a string, not in nested boxes."
)

REVIEW_NOTE = (
    "You now hold the complete Lao ladder: the round Lao script with its tone classes, six tones and "
    "vowel lengths, helper-word grammar with SVO order, core nouns verbs and adjectives, pronouns, "
    "numbers to one hundred, time words, greetings, ten themed sentence sets, the helper-word tenses, "
    "questions, commands, descriptions, three graded stories, proverbs, polite registers, and three "
    "full conversations. Keep the tones level and the smile ready."
)

NOUNS = [
    ("ນ້ຳ", "nam", "water", "ນ້ຳດີ", "nam di", "The water is good."),
    ("ເຂົ້າ", "khao", "rice, food", "ເຂົ້າດີ", "khao di", "The rice is good."),
    ("ເຮືອນ", "heuan", "house", "ເຮືອນໃຫຍ່", "heuan nyai", "The house is big."),
    ("ລົດ", "lot", "car", "ລົດໃໝ່", "lot mai", "The car is new."),
    ("ປຶ້ມ", "peum", "book", "ປຶ້ມດີ", "peum di", "The book is good."),
    ("ຕະຫຼາດ", "talaat", "market", "ຕະຫຼາດໃຫຍ່", "talaat nyai", "The market is big."),
    ("ໂຮງຮຽນ", "honghian", "school", "ໂຮງຮຽນດີ", "honghian di", "The school is good."),
    ("ພໍ່", "pho", "father", "ພໍ່ດີ", "pho di", "Father is good."),
    ("ແມ່", "mae", "mother", "ແມ່ດີ", "mae di", "Mother is good."),
    ("ໝາ", "ma", "dog", "ໝານ້ອຍ", "ma noi", "The dog is small."),
    ("ຮັກ", "hak", "love", "ຮັກດີ", "hak di", "Love is good."),
    ("ມື້", "meu", "day", "ມື້ນີ້ດີ", "meu ni di", "Today is good."),
]

VERBS = [
    ("ກິນ", "kin", "to eat", "ກິນດີ", "kin di", "Eating is good."),
    ("ດື່ມ", "deum", "to drink", "ດື່ມດີ", "deum di", "Drinking is good."),
    ("ໄປ", "pai", "to go", "ໄປດີ", "pai di", "Going is good."),
    ("ມາ", "ma", "to come", "ມາດີ", "ma di", "Coming is good."),
    ("ເວົ້າ", "vao", "to speak", "ເວົ້າດີ", "vao di", "Speaking is good."),
    ("ເຮັດວຽກ", "het viak", "to work", "ເຮັດວຽກດີ", "het viak di", "Working is good."),
    ("ຮຽນ", "hian", "to learn, to study", "ຮຽນດີ", "hian di", "Learning is good."),
    ("ໃຫ້", "hai", "to give", "ໃຫ້ດີ", "hai di", "Giving is good."),
    ("ຮັກ", "hak", "to love", "ຮັກດີ", "hak di", "Loving is good."),
    ("ຢູ່", "yu", "to live, to stay", "ຢູ່ດີ", "yu di", "Living is good."),
]

ADJS = [
    ("ດີ", "di", "good", "ເຮືອນດີ", "heuan di", "a good house"),
    ("ບໍ່ດີ", "bo di", "bad", "ລົດບໍ່ດີ", "lot bo di", "a bad car"),
    ("ໃຫຍ່", "nyai", "big", "ເຮືອນໃຫຍ່", "heuan nyai", "a big house"),
    ("ນ້ອຍ", "noi", "small", "ໝານ້ອຍ", "ma noi", "a small dog"),
    ("ໃໝ່", "mai", "new", "ລົດໃໝ່", "lot mai", "a new car"),
    ("ເກົ່າ", "kao", "old", "ເຮືອນເກົ່າ", "heuan kao", "an old house"),
    ("ແດງ", "daeng", "red", "ລົດແດງ", "lot daeng", "a red car"),
    ("ຂາວ", "khao", "white", "ເສື້ອຂາວ", "seua khao", "a white shirt"),
]

PRONOUNS = [
    ("ຂ້ອຍ", "khoi", "I"),
    ("ເຈົ້າ", "chao", "you (singular)"),
    ("ລາວ", "lao", "he / she"),
    ("ພວກເຮົາ", "phuak hao", "we"),
    ("ພວກເຈົ້າ", "phuak chao", "you (plural)"),
    ("ພວກເຂົາ", "phuak khao", "they"),
    ("ນີ້", "ni", "this"),
    ("ນັ້ນ", "nan", "that"),
]

NUMBERS = [
    ("ນຶ່ງ", "neung", "one"), ("ສອງ", "song", "two"), ("ສາມ", "sam", "three"),
    ("ສີ່", "si", "four"), ("ຫ້າ", "ha", "five"), ("ຫົກ", "hok", "six"),
    ("ເຈັດ", "jet", "seven"), ("ແປດ", "paet", "eight"),
    ("ເກົ້າ", "kao", "nine"), ("ສິບ", "sip", "ten"),
    ("ຊາວ", "sao", "twenty"), ("ຮ້ອຍ", "loi", "one hundred"),
]

TIME_WORDS = [
    ("ມື້ນີ້", "meu ni", "today"), ("ມື້ອື່ນ", "meu eun", "tomorrow"),
    ("ມື້ວານນີ້", "meu van ni", "yesterday"), ("ອາທິດ", "athit", "week"),
    ("ເດືອນ", "deuan", "month"), ("ປີ", "pi", "year"),
]

GREETINGS = [
    ("ສະບາຍດີ", "sabaidee", "Hello! / Goodbye!"),
    ("ສະບາຍດີບໍ", "sabaidee bo", "How are you?"),
    ("ສະບາຍດີ", "sabaidee", "I am well. (reply)"),
    ("ຂອບໃຈ", "khop jai", "Thank you."),
    ("ຂອບໃຈຫຼາຍໆ", "khop jai lai lai", "Thank you very much."),
    ("ກະລຸນາ", "karuna", "Please (formal)."),
    ("ຂໍໂທດ", "kho thot", "Sorry / excuse me."),
    ("ບໍ່ເປັນຫຍັງ", "bo pen nyang", "No problem / you are welcome."),
    ("ລາກອນ", "la gon", "Goodbye (stay well)."),
    ("ພົບກັນໃໝ່", "phop kan mai", "See you again."),
]

THEMES = [
    ("Home and Family", [
        ("ຄອບຄົວ", "khop khua", "family", "ຄອບຄົວດີ", "khop khua di", "The family is good."),
        ("ພໍ່", "pho", "father", "ພໍ່ເຮັດວຽກ", "pho het viak", "Father works."),
        ("ແມ່", "mae", "mother", "ແມ່ແຕ່ງອາຫານ", "mae taeng ahan", "Mother cooks food."),
        ("ອ້າຍ", "ai", "older brother", "ອ້າຍຊ່ວຍເຫຼືອ", "ai chuai leua", "The older brother helps."),
        ("ເອື້ອຍ", "euy", "older sister", "ເອື້ອຍຮຽນ", "euy hian", "The older sister studies."),
        ("ນ້ອງ", "nong", "younger sibling", "ນ້ອງຫຼິ້ນ", "nong lin", "The younger sibling plays."),
    ]),
    ("Food and Cooking", [
        ("ອາຫານ", "ahan", "food", "ອາຫານແຊບ", "ahan saep", "The food is delicious."),
        ("ເຂົ້າ", "khao", "rice", "ເຂົ້າແຊບ", "khao saep", "The rice is delicious."),
        ("ຊີ້ນ", "sin", "meat", "ຊີ້ນແພງ", "sin phaeng", "The meat is expensive."),
        ("ນ້ຳ", "nam", "water", "ນ້ຳດີ", "nam di", "The water is good."),
        ("ນົມ", "nom", "milk", "ນົມດີ", "nom di", "The milk is good."),
        ("ນ້ຳຕານ", "nam tan", "sugar", "ນ້ຳຕານແພງ", "nam tan phaeng", "The sugar is expensive."),
    ]),
    ("Travel and Directions", [
        ("ທາງ", "thang", "road", "ທາງຍາວ", "thang nyao", "The road is long."),
        ("ລົດ", "lot", "car", "ລົດໄປ", "lot pai", "The car goes."),
        ("ຍົນ", "nyon", "airplane", "ຍົນບິນ", "nyon bin", "The plane flies."),
        ("ສະຖານີ", "sathani", "station", "ສະຖານີໃກ້", "sathani khai", "The station is near."),
        ("ຂວາ", "khua", "right", "ໄປຂວາ", "pai khua", "Go right."),
        ("ຊ້າຍ", "sai", "left", "ໄປຊ້າຍ", "pai sai", "Go left."),
    ]),
    ("Work and School", [
        ("ວຽກ", "viak", "work", "ວຽກດີ", "viak di", "The work is good."),
        ("ໂຮງຮຽນ", "honghian", "school", "ໂຮງຮຽນເປີດ", "honghian poet", "The school is open."),
        ("ນັກຮຽນ", "nak hian", "student", "ນັກຮຽນຮຽນ", "nak hian hian", "The student studies."),
        ("ຄູ", "khu", "teacher", "ຄູເວົ້າ", "khu vao", "The teacher speaks."),
        ("ປຶ້ມ", "peum", "book", "ປຶ້ມປິດ", "peum pit", "The book is closed."),
        ("ປາກກາ", "pak ka", "pen", "ປາກກາດີ", "pak ka di", "The pen is good."),
    ]),
    ("Health and the Body", [
        ("ຮ່າງກາຍ", "hang kai", "body", "ຮ່າງກາຍດີ", "hang kai di", "The body is good."),
        ("ຫົວ", "hua", "head", "ຫົວເຈັບ", "hua jep", "The head aches."),
        ("ຕາ", "ta", "eye", "ຕາເຫັນ", "ta hen", "The eye sees."),
        ("ແຂນ", "khaen", "arm", "ແຂນເຈັບ", "khaen jep", "The arm aches."),
        ("ຂາ", "kha", "leg", "ຂາເຈັບ", "kha jep", "The leg aches."),
        ("ໝໍ", "mo", "doctor", "ໝໍປິ່ນປົວ", "mo pin pua", "The doctor heals."),
    ]),
    ("Emotions and Feelings", [
        ("ຄວາມສຸກ", "khuam suk", "joy", "ຄວາມສຸກດີ", "khuam suk di", "Joy is good."),
        ("ຄວາມເສົ້າ", "khuam sao", "sadness", "ຄວາມເສົ້າຫາຍ", "khuam sao hai", "The sadness is gone."),
        ("ຄວາມຢ້ານ", "khuam yan", "fear", "ຄວາມຢ້ານຫາຍ", "khuam yan hai", "The fear is gone."),
        ("ຄວາມຮັກ", "khuam hak", "love", "ຄວາມຮັກແຂງແຮງ", "khuam hak khaeng haeng", "Love is strong."),
        ("ຄວາມອິດສາ", "khuam it sa", "jealousy", "ຄວາມອິດສາບໍ່ດີ", "khuam it sa bo di", "Jealousy is bad."),
        ("ຄວາມສະຫງົບ", "khuam sa ngop", "peace", "ຄວາມສະຫງົບດີ", "khuam sa ngop di", "Peace is good."),
    ]),
    ("Nature and Weather", [
        ("ທຳມະຊາດ", "tham ma sat", "nature", "ທຳມະຊາດງາມ", "tham ma sat ngam", "Nature is beautiful."),
        ("ຝົນ", "fon", "rain", "ຝົນຕົກ", "fon tok", "The rain is falling."),
        ("ແສງຕາເວັນ", "saeng ta ven", "sun", "ແສງຕາເວັນຮ້ອນ", "saeng ta ven hon", "The sun is hot."),
        ("ເດືອນ", "duean", "moon", "ເດືອນສະຫວ່າງ", "duean sa wang", "The moon is bright."),
        ("ຕົ້ນໄມ້", "ton mai", "tree", "ຕົ້ນໄມ້ໃຫຍ່", "ton mai nyai", "The tree is big."),
        ("ດອກໄມ້", "dok mai", "flower", "ດອກໄມ້ງາມ", "dok mai ngam", "The flower is beautiful."),
    ]),
    ("Shopping and Money", [
        ("ເງິນ", "ngoen", "money", "ເງິນດີ", "ngoen di", "Money is good."),
        ("ລາຄາ", "la kha", "price", "ລາຄາແພງ", "la kha phaeng", "The price is high."),
        ("ຮ້ານ", "han", "shop", "ຮ້ານເປີດ", "han poet", "The shop is open."),
        ("ຖືກ", "thuk", "cheap", "ຖືກດີ", "thuk di", "Cheap is good."),
        ("ລູກຄ້າ", "luk kha", "customer", "ລູກຄ້າດີໃຈ", "luk kha di jai", "The customer is happy."),
        ("ພໍ່ຄ້າ", "pho kha", "seller", "ພໍ່ຄ້າດີ", "pho kha di", "The seller is good."),
    ]),
    ("Friendship and Social Life", [
        ("ໝູ່", "mu", "friend", "ໝູ່ດີ", "mu di", "The friend is good."),
        ("ການຕ້ອນຮັບ", "kan ton hap", "hospitality", "ການຕ້ອນຮັບດີ", "kan ton hap di", "Hospitality is good."),
        ("ການສົນທະນາ", "kan son tha na", "conversation", "ການສົນທະນາດີ", "kan son tha na di", "The conversation is good."),
        ("ງານລ້ຽງ", "ngan liang", "feast", "ງານລ້ຽງດີ", "ngan liang di", "The feast is good."),
        ("ການເຕັ້ນ", "kan ten", "dance", "ການເຕັ້ນງາມ", "kan ten ngam", "The dance is beautiful."),
        ("ເພງ", "pheng", "song", "ເພງງາມ", "pheng ngam", "The song is beautiful."),
    ]),
    ("Technology and Communication", [
        ("ໂທລະສັບ", "tho la sap", "telephone", "ໂທລະສັບດັງ", "tho la sap dang", "The phone is ringing."),
        ("ຄອມພິວເຕີ", "khom phiu toe", "computer", "ຄອມພິວເຕີເຮັດວຽກ", "khom phiu toe het viak", "The computer is working."),
        ("ອິນເຕີເນັດ", "in toe net", "internet", "ອິນເຕີເນັດໄວ", "in toe net vai", "The internet is fast."),
        ("ໄຟຟ້າ", "fai fa", "electricity", "ມີໄຟຟ້າ", "mi fai fa", "There is electricity."),
        ("ຂໍ້ຄວາມ", "kho khuam", "message", "ຂໍ້ຄວາມມາ", "kho khuam ma", "The message has arrived."),
        ("ວິທະຍຸ", "vi tha nyu", "radio", "ວິທະຍຸຫຼິ້ນ", "vi tha nyu lin", "The radio is playing."),
    ]),
]
QUESTIONS = [
    ("ຊື່ເຈົ້າແມ່ນຫຍັງ?", "seu jao maen nyang", "What is your name?"),
    ("ແມ່ຢູ່ໃສ?", "mae yu sai", "Where is mother?"),
    ("ອັນນີ້ເທົ່າໃດ?", "an ni thao dai", "How much is this?"),
    ("ເປັນຫຍັງ?", "pen nyang", "Why?"),
    ("ເມື່ອໃດ?", "muea dai", "When?"),
    ("ໃຜນີ?", "phai ni", "Who is this?"),
    ("ອາຫານເປັນແນວໃດ?", "a han pen naeo dai", "How is the food?"),
    ("ເຈົ້າມາຈາກໃສ?", "jao ma jak sai", "Where are you from?"),
]

COMMANDS = [
    ("ມານີ່ມາ!", "ma ni ma", "Come here!"),
    ("ໄປ!", "pai", "Go!"),
    ("ນັ່ງ!", "nang", "Sit down!"),
    ("ເວົ້າຊ້າໆ!", "vao sa sa", "Speak slowly!"),
    ("ຊ່ວຍຂ້ອຍ!", "suai khoi", "Help me!"),
    ("ຟັງ!", "fang", "Listen!"),
    ("ເບິ່ງ!", "boeng", "Look!"),
    ("ຢຸດ!", "yut", "Stop!"),
]

DESCRIBE = [
    ("ຜູ້ຊາຍສູງ, ສູງ.", "phu sai sung sung", "The tall man, he is tall."),
    ("ຜູ້ຍິງງາມ, ງາມ.", "phu nying ngam ngam", "The beautiful woman, she is beautiful."),
    ("ເຮືອນໃຫຍ່, ໃຫຍ່.", "huean nyai nyai", "The big house, it is big."),
    ("ລົດແດງ, ແດງ.", "lot daeng daeng", "The red car, it is red."),
    ("ເດັກນ້ອຍ, ນ້ອຍ.", "dek noi noi", "The small child, he/she is small."),
    ("ປຶ້ມໃໝ່, ໃໝ່.", "puem mai mai", "The new book, it is new."),
    ("ແສງຕາເວັນຮ້ອນ, ຮ້ອນ.", "saeng ta ven hon hon", "The hot sun, it is hot."),
    ("ນ້ຳເຢັນ, ເຢັນ.", "nam yen yen", "The cold water, it is cold."),
]
STORIES = [
    ("Story I: The Boy and the Goat", [
        ("ມີເດັກຊາຍຄົນໜຶ່ງ.", "mi dek sai khon nueng", "There was a boy."),
        ("ເດັກຊາຍມີແບ້ໂຕໜຶ່ງ.", "dek sai mi bae to nueng", "The boy has a goat."),
        ("ແບ້ສີຂາວ.", "bae si khao", "The goat is white."),
        ("ເດັກຊາຍຮັກແບ້.", "dek sai hak bae", "The boy loves the goat."),
        ("ມື້ໜຶ່ງແບ້ຫາຍ.", "mue nueng bae hai", "One day the goat got lost."),
        ("ເດັກຊາຍຊອກຫາທຸກບ່ອນ.", "dek sai sok ha thuk bon", "The boy searched everywhere."),
        ("ສຸດທ້າຍລາວພົບ.", "sut thai lao phop", "Finally he found it."),
        ("ລາວດີໃຈຫຼາຍ.", "lao di jai lai", "He was very happy."),
    ]),
    ("Story II: The Rainy Day", [
        ("ມື້ນີ້ຝົນຕົກ.", "mue ni fon tok", "Today the rain is falling."),
        ("ເດັກໆຢູ່ເຮືອນ.", "dek dek yu huean", "The children stay in the house."),
        ("ແມ່ແຕ່ງອາຫານ.", "mae taeng a han", "Mother is cooking food."),
        ("ອາຫານແຊບ.", "a han saep", "The food is delicious."),
        ("ພໍ່ອ່ານປຶ້ມ.", "pho an puem", "Father is reading a book."),
        ("ຝົນຢຸດແສງຕາເວັນອອກ.", "fon yut saeng ta ven ok", "After the rain the sun came out."),
        ("ເດັກໆອອກໄປ.", "dek dek ok pai", "The children went outside."),
        ("ເຂົາເຈົ້າຫຼິ້ນຢູ່ເດີ່ນ.", "khao jao lin yu doen", "They are playing in the yard."),
    ]),
    ("Story III: The Market Trip", [
        ("ມື້ອື່ນໄປຕະຫຼາດ.", "mue uen pai ta lat", "Tomorrow we go to the market."),
        ("ແມ່ຊື້ເຂົ້າ.", "mae seu khao", "Mother buys rice."),
        ("ພໍ່ຊື້ຊີ້ນ.", "pho seu sin", "Father buys meat."),
        ("ເດັກຊື້ເຂົ້າໜົມ.", "dek seu khao nom", "The child buys candy."),
        ("ເຂົ້າແຊບ.", "khao saep", "The rice is delicious."),
        ("ຊີ້ນແພງ.", "sin phaeng", "The meat is expensive."),
        ("ພວກເຮົາກັບບ້ານ.", "phuak hao kap ban", "We all go home."),
        ("ພວກເຮົາກິນເຂົ້າແຊບ.", "phuak hao kin khao saep", "We all eat well."),
    ]),
]

IDIOMS = [
    ("ເມື່ອນ້ຳຂຶ້ນ ປາກິນມົດ ເມື່ອນ້ຳລົດ ມົດກິນປາ", "muea nam khuen pa kin mot muea nam lot mot kin pa", "When the water rises the fish eat the ants; when the water falls the ants eat the fish", "Fortunes reverse — be humble in good times."),
    ("ຊ້າງຕາຍທັງໂຕ ເອົາໃບບົວປິດບໍ່ມິດ", "sang tai thang to ao bai bua pit bo mit", "A dead elephant cannot be hidden with a lotus leaf", "Big truths cannot be covered up."),
    ("ເຫັນຊ້າງຂີ້ ຢ່າຂີ້ຕາມຊ້າງ", "hen sang khi ya khi tam sang", "Seeing the elephant defecate, do not defecate after the elephant", "Do not copy others beyond your capacity."),
    ("ນ້ຳເຊາະດິນພັງ ນ້ຳແຫ້ງປາຕາຍ", "nam sao din phang nam haeng pa tai", "Eroding water breaks the bank; dry water kills the fish", "Actions have unavoidable consequences."),
]
CONVOS = [
    ("At the Market", [
        ("A", "ສະບາຍດີ!", "sa bai di", "Hello!"),
        ("B", "ສະບາຍດີ! ຢາກໄດ້ຫຍັງ?", "sa bai di yak dai nyang", "Hello! What do you want?"),
        ("A", "ອັນນີ້ເທົ່າໃດ?", "an ni thao dai", "How much is this?"),
        ("B", "ສິບພັນ.", "sip phan", "Ten thousand."),
        ("A", "ແພງ.", "phaeng", "Expensive."),
        ("B", "ຫຼຸດໄດ້.", "lut dai", "It can be less."),
        ("A", "ຂອບໃຈ, ເອົາ.", "khop jai ao", "Thank you, I will take it."),
        ("B", "ສະບາຍດີ!", "sa bai di", "Goodbye!"),
    ]),
    ("Meeting a Friend", [
        ("A", "ສະບາຍດີ, ສະບາຍດີບໍ?", "sa bai di sa bai di bo", "Hi, how are you?"),
        ("B", "ສະບາຍດີ, ຂອບໃຈ. ເຈົ້າເດ?", "sa bai di khop jai jao de", "I am well, thanks. And you?"),
        ("A", "ຂ້ອຍກໍ່ສະບາຍດີ.", "khoi ko sa bai di", "I am well too."),
        ("B", "ຊື່ເຈົ້າແມ່ນຫຍັງ?", "seu jao maen nyang", "What is your name?"),
        ("A", "ຂ້ອຍຊື່ຄຳ.", "khoi seu kham", "My name is Kham."),
        ("B", "ຍິນດີທີ່ໄດ້ຮູ້ຈັກ.", "nyin di thi dai hu jak", "Nice to meet you."),
        ("A", "ຂ້ອຍກໍ່ຍິນດີ.", "khoi ko nyin di", "Nice to meet you too."),
        ("B", "ພົບກັນໃໝ່!", "phop kan mai", "See you again!"),
    ]),
    ("Solving a Problem", [
        ("A", "ມີບັນຫາ.", "mi ban ha", "There is a problem."),
        ("B", "ບັນຫາຫຍັງ?", "ban ha nyang", "What problem?"),
        ("A", "ລົດເສຍ.", "lot sia", "The car broke down."),
        ("B", "ຢ່າກັງວົນ.", "ya kang von", "Do not worry."),
        ("A", "ຊ່ວຍຂ້ອຍ!", "suai khoi", "Help me!"),
        ("B", "ຂ້ອຍຈະຊ່ວຍ.", "khoi ja suai", "I will help."),
        ("A", "ຂອບໃຈຫຼາຍໆ!", "khop jai lai lai", "Thank you very much!"),
        ("B", "ບໍ່ເປັນຫຍັງ.", "bo pen nyang", "You are welcome."),
    ]),
]

CITATIONS = [
    "Omniglot. Useful phrases in Lao.",
    "Wikivoyage contributors. Lao phrasebook.",
    "Proverb studies of Lao oral tradition: 'ເມື່ອນ້ຳຂຶ້ນ ປາກິນມົດ ເມື່ອນ້ຳລົດ ມົດກິນປາ', 'ຊ້າງຕາຍທັງໂຕ ເອົາໃບບົວປິດບໍ່ມິດ'.",
    "Reinhorn M. Dictionnaire Laotien-Français. CNRS; 1970.",
    "ISO 639-1:2002 language code lo; ISO 639-3:2007 language code lao.",
    "Standard pedagogical sources for Lao vocabulary, tones, usage, and phraseology.",
]
