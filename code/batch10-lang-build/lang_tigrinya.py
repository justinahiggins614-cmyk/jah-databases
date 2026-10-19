# -*- coding: utf-8 -*-
"""Language data module: Tigrinya (ti/tir). Facts verified 2026-10-17 via
Omniglot numbers, Wikivoyage phrasebook, Harvard ELIAS lessons, published proverb collections."""

SLUG = "language-tigrinya"
PREFIX = "JAH-LTIR-"
SIG_PREFIX = "JAH-LTIRS-"
NAME = "Tigrinya"
NATIVE = "ትግርኛ"
NATIVE_ROMAN = "təgrəñña"
ISO1 = "ti"
ISO3 = "tir"
FAMILY = "Afro-Asiatic > Semitic > Ethio-Semitic (Northern branch)"
SPEAKERS = "about 9 to 10 million first-language speakers"
REGIONS = "Eritrea, where it is a working language, and the Tigray region of Ethiopia; large diaspora communities in the Middle East, Europe, North America and Australia"
SCRIPT_NAME = "Ge'ez (Ethiopic) script"
WORD_ORDER = "subject-object-verb (SOV)"
AI_NAME = "JAH Tigrinya Language Archivist"
SIG_AI_NAME = "JAH Tigrinya Signature Archivist"

OVERVIEW = (
    "Tigrinya (ትግርኛ, təgrəñña) is a Northern Ethio-Semitic language of the Afro-Asiatic family, "
    "spoken as a first language by about 9 to 10 million people. It is a working language of Eritrea "
    "and the first language of the vast majority of people in the Tigray region of Ethiopia, with large "
    "diaspora communities across the Middle East, Europe, North America and Australia. Tigrinya descends "
    "from the ancient Ge'ez language and shares its script. It is famous among linguists for its ejective "
    "consonants (p', t', ch', k'), its seven-vowel system, and verbs built on three-consonant roots that "
    "change shape by pattern, not just by ending."
)

SCRIPT_DESC = (
    "Tigrinya is written in the Ge'ez (Ethiopic) fidel script, read left to right. Each base consonant "
    "appears in seven vowel orders, so the full syllabary holds more than 200 fidel characters. There is "
    "no upper or lower case. Ge'ez also has its own numerals: ፩ (1), ፪ (2), ፫ (3), ፬ (4), ፭ (5), ፮ (6), "
    "፯ (7), ፰ (8), ፱ (9), ፲ (10), ፳ (20), ፻ (100). Punctuation includes ፡ (word space) and ። (full stop)."
)

ALPHABET_NOTE = (
    "The fidel are organized in rows: each row is one consonant across seven vowel orders "
    "(ä, u, i, a, e, ə, o). Learn one row at a time. The sample below shows the first-order "
    "(ä) form of twelve common rows; the full row multiplies each by seven."
)

ALPHABET_SAMPLE = [
    ("ሀ", "hä"), ("ለ", "lä"), ("ሐ", "ḥä"), ("መ", "mä"), ("ሠ", "śä"), ("ረ", "rä"),
    ("ሰ", "sä"), ("ቀ", "qä"), ("በ", "bä"), ("ተ", "tä"), ("ነ", "nä"), ("አ", "ʾä"),
]

SOUNDS_DESC = (
    "Tigrinya has seven vowels: ä (as in 'cat'), u, i, a (as in 'father'), e, ə (the neutral 'uh' sound), "
    "and o. Its signature sounds are the ejectives — consonants pronounced with a pop of air: ጰ (p'), "
    "ጠ (t'), ጨ (ch'), ቀ (k'). Learners must hear the difference between ተ (tä, plain t) and ጠ (t'ä, "
    "ejective t'), and between ሰ (sä, plain s) and ጸ (ts'ä, ejective ts). Stress usually falls on the "
    "last or second-to-last syllable."
)

GRAMMAR_DESC = (
    "Tigrinya is a subject-object-verb language: the verb comes last. Nouns have two genders "
    "(masculine and feminine) and verbs agree with their subject in gender and number. There are no "
    "articles; 'a house' is simply ቤት (bet). Negation wraps the verb: ኣይ- at the front and -ን at the "
    "end (ኣይፈልጥን, ayfelt'ən — 'I do not know'). Questions often end with a rising tone or the "
    "question particle -ዶ."
)

TENSE_DESC = (
    "Tigrinya verbs are built on consonantal roots that take different patterns for tense. The present "
    "tense adds the prefix ይ- (yə-) for 'he' forms and related prefixes for other persons; the past "
    "tense is marked by suffixes on the stem; the future is formed with a helper construction. Rather "
    "than memorizing tables first, learn the high-frequency sentences below as whole chunks — "
    "ትግርኛ ኣይፈልጥን (təgrəñña ayfelt'ən, 'I do not know Tigrinya') shows the negative past pattern in "
    "real use — then break the patterns apart."
)

REGISTER_DESC = (
    "Tigrinya marks respect through pronoun and verb choice. ከመይ ኣለኻ (kemay alekha) addresses a man, "
    "ከመይ ኣለኺ (kemay alekhi) a woman; the plural/formal ንስኻት (niskhat) form shows respect to elders and "
    "strangers. በጃኻ (bejakha, to a man) and በጃኺ (bejakhi, to a woman) both mean 'please'. Elders are "
    "greeted with the time-of-day formulas — ደሓንዶ (dehando, 'good morning' sense) — and answered with "
    "equal care. Using the wrong gender form is the classic beginner mistake; natives correct it kindly."
)

COMPLEX_DESC = (
    "Tigrinya joins ideas with small connector words and relative clauses built on the verb. The word "
    "እንተ (ənte, 'if/when') opens conditions; እዚ (əzi, 'this') and እቲ (əti, 'that') anchor descriptions; "
    "reason clauses use ስለምንታይ (səleməntay, 'why'). Because the verb comes last, long Tigrinya sentences "
    "stack all the background first and deliver the action at the end — read to the final verb before "
    "deciding what happened."
)

REVIEW_NOTE = (
    "You now hold the complete Tigrinya ladder: the Ge'ez script and its 200+ fidel, the ejective "
    "consonants and seven vowels, SOV grammar with gender agreement, core nouns verbs and adjectives, "
    "pronouns, numbers to one hundred, time words, greetings, ten themed sentence sets, verb tenses, "
    "questions, commands, descriptions, three graded stories, proverbs, formal registers, and three "
    "full conversations. Review by reading each record's sentences aloud; the script rewards the eye "
    "that has traced every fidel."
)

NOUNS = [
    ("ቤት", "bet", "house", "እዚ ቤት እዩ", "əzi bet iyu", "This is a house."),
    ("መኪና", "mekina", "car", "እዚ መኪና እዩ", "əzi mekina iyu", "This is a car."),
    ("እንጀራ", "ənjəra", "injera flatbread", "እዚ እንጀራ እዩ", "əzi ənjəra iyu", "This is injera."),
    ("ማይ", "may", "water", "እዚ ማይ እዩ", "əzi may iyu", "This is water."),
    ("ሰማይ", "semay", "sky", "እዚ ሰማይ እዩ", "əzi semay iyu", "This is the sky."),
    ("ጸሓይ", "ts'əhay", "sun", "እዚ ጸሓይ እዩ", "əzi ts'əhay iyu", "This is the sun."),
    ("ወርሒ", "werhi", "moon", "እዚ ወርሒ እዩ", "əzi werhi iyu", "This is the moon."),
    ("ኣቦ", "abo", "father", "እዚ ኣቦ እዩ", "əzi abo iyu", "This is a father."),
    ("ኣደ", "ade", "mother", "እዚ ኣደ እዩ", "əzi ade iyu", "This is a mother."),
    ("ሓወ", "haw", "brother", "እዚ ሓወ እዩ", "əzi haw iyu", "This is a brother."),
    ("ሓፍቲ", "hafti", "sister", "እዚ ሓፍቲ እዩ", "əzi hafti iyu", "This is a sister."),
    ("መጽሓፍ", "mets'haf", "book", "እዚ መጽሓፍ እዩ", "əzi mets'haf iyu", "This is a book."),
]

VERBS = [
    ("ምብላዕ", "məbla'", "to eat", "ምብላዕ ጽብቕ እዩ", "məbla' tsəbbuq iyu", "Eating is good."),
    ("ምስታይ", "məstay", "to drink", "ምስታይ ጽብቕ እዩ", "məstay tsəbbuq iyu", "Drinking is good."),
    ("ምኻድ", "məkhad", "to go", "ምኻድ ጽብቕ እዩ", "məkhad tsəbbuq iyu", "Going is good."),
    ("ምምጻእ", "məmts'a'", "to come", "ምምጻእ ጽብቕ እዩ", "məmts'a' tsəbbuq iyu", "Coming is good."),
    ("ምዝራብ", "məzrab", "to speak", "ምዝራብ ጽብቕ እዩ", "məzrab tsəbbuq iyu", "Speaking is good."),
    ("ምስራሕ", "məsrah", "to work", "ምስራሕ ጽብቕ እዩ", "məsrah tsəbbuq iyu", "Working is good."),
    ("ምምሃር", "məmhar", "to learn", "ምምሃር ጽብቕ እዩ", "məmhar tsəbbuq iyu", "Learning is good."),
    ("ምፍቃር", "məfqar", "to love", "ምፍቃር ጽብቕ እዩ", "məfqar tsəbbuq iyu", "Loving is good."),
    ("ምህባብ", "məhbab", "to give", "ምህባብ ጽብቕ እዩ", "məhbab tsəbbuq iyu", "Giving is good."),
    ("ምንባር", "mənbar", "to live, to stay", "ምንባር ጽብቕ እዩ", "mənbar tsəbbuq iyu", "Living is good."),
]

ADJS = [
    ("ጽብቕ", "tsəbbuq", "good (masculine)", "ጽብቕ ሰብ", "tsəbbuq seb", "a good man"),
    ("ጽብቕቲ", "tsəbbuqti", "good (feminine)", "ጽብቕቲ ሰበይቲ", "tsəbbuqti sebeyti", "a good woman"),
    ("ሕማቕ", "həmaq", "bad", "ሕማቕ መኪና", "həmaq mekina", "a bad car"),
    ("ዓብዪ", "'abiy", "big", "ዓብዪ ቤት", "'abiy bet", "a big house"),
    ("ንእሽቱ", "nə'ushtu", "small", "ንእሽቱ መጽሓፍ", "nə'ushtu mets'haf", "a small book"),
    ("ሓድሽ", "haddəsh", "new", "ሓድሽ መኪና", "haddəsh mekina", "a new car"),
    ("ቀይሕ", "qeyh", "red", "ቀይሕ እንጀራ", "qeyh ənjəra", "red injera"),
    ("ጸሊም", "ts'elim", "black", "ጸሊም ሰማይ", "ts'elim semay", "a black sky"),
]

PRONOUNS = [
    ("ኣነ", "ane", "I"),
    ("ንስኻ", "nəsəkha", "you (masculine)"),
    ("ንስኺ", "nəsəkhi", "you (feminine)"),
    ("ንሱ", "nəsu", "he"),
    ("ንሳ", "nəsa", "she"),
    ("ንሕና", "nəhna", "we"),
    ("ንስኻት", "nəsəkhat", "you (plural / formal)"),
    ("ንሳቶም", "nəsatóm", "they (masculine)"),
]

NUMBERS = [
    ("ሓደ", "hade", "one"), ("ክልተ", "kelete", "two"), ("ሰለስተ", "seleste", "three"),
    ("ኣርባዕተ", "arba'ete", "four"), ("ሓሙሽት", "hamushte", "five"), ("ሽድሽተ", "shudushte", "six"),
    ("ሸውዓተ", "shewa'ate", "seven"), ("ሸሞንተ", "shemonte", "eight"),
    ("ትሽዓተ", "tishe'ate", "nine"), ("ዓሰርተ", "'äserte", "ten"),
    ("ዕስራ", "'äsra", "twenty"), ("ሚእቲ", "mi'äti", "one hundred"),
]

TIME_WORDS = [
    ("ሎሚ", "lomi", "today"), ("ጽባሕ", "tsəbah", "tomorrow"),
    ("ትማሊ", "təmali", "yesterday"), ("ሰሙን", "semun", "week"),
    ("ወርሒ", "werhi", "month"), ("ዓመት", "'amet", "year"),
]

GREETINGS = [
    ("ሰላም", "selam", "Hello!"),
    ("ከመይ ኣለኻ", "kemay alekha", "How are you? (to a man)"),
    ("ከመይ ኣለኺ", "kemay alekhi", "How are you? (to a woman)"),
    ("ደሓን ኣለኹ", "dehan aleku", "I am fine. (reply)"),
    ("የቐንየለይ", "yekenyelay", "Thank you."),
    ("ኣመሰጋን", "ameseghan", "Thank you. (variant)"),
    ("በጃኻ", "bejakha", "Please. (to a man)"),
    ("በጃኺ", "bejakhi", "Please. (to a woman)"),
    ("ይቕሬታ", "yəqreta", "Sorry / excuse me."),
    ("ደሓን ኹን", "dehan kun", "Goodbye (stay well)."),
]
THEMES = [
    ("Home and Family", [
        ("ስድራቤት", "sədrabet", "family", "ትምህርቲ ስድራቤት", "təmhirti sədrabet", "The educated family."),
        ("ኣቦ", "abo", "father", "ኣቦ ይሰርሕ", "abo yəserh", "Father works."),
        ("ኣደ", "ade", "mother", "ኣደ ትሰርሕ", "ade təserh", "Mother works."),
        ("ሓወ", "haw", "brother", "ሓወ ይምሃር", "haw yəmhar", "The brother learns."),
        ("ሓፍቲ", "hafti", "sister", "ሓፍቲ ትምሃር", "hafti təmhar", "The sister learns."),
        ("ቆልዓ", "qol'a", "child", "ቆልዓ ይጻወት", "qol'a yəts'awet", "The child plays."),
    ]),
    ("Food and Cooking", [
        ("ምግቢ", "məgbi", "food", "ምግቢ ጽብቕ እዩ", "məgbi tsəbbuq iyu", "The food is good."),
        ("እንጀራ", "ənjəra", "injera flatbread", "እንጀራ ጽብቕ እዩ", "ənjəra tsəbbuq iyu", "The injera is good."),
        ("ስጋ", "səga", "meat", "ስጋ ክቡር እዩ", "səga kəbur iyu", "The meat is expensive."),
        ("ማይ", "may", "water", "ማይ ጽብቕ እዩ", "may tsəbbuq iyu", "The water is good."),
        ("ሓሊብ", "halib", "milk", "ሓሊብ ጽብቕ እዩ", "halib tsəbbuq iyu", "The milk is good."),
        ("ሻሂ", "shahi", "tea", "ሻሂ ጽብቕ እዩ", "shahi tsəbbuq iyu", "The tea is good."),
    ]),
    ("Travel and Directions", [
        ("መንገዲ", "mengedi", "road", "መንገዲ ነዊሕ እዩ", "mengedi newih iyu", "The road is long."),
        ("መኪና", "mekina", "car", "መኪና ትኸይድ", "mekina təkhäyd", "The car goes."),
        ("ነፋሪት", "nefarit", "airplane", "ነፋሪት ትንፍር", "nefarit tənfər", "The plane flies."),
        ("ጣብያ", "t'abya", "station", "ጣብያ ቀሪብ እዩ", "t'abya qerib iyu", "The station is near."),
        ("የማን", "yeman", "right", "ናብ የማን", "nab yeman", "Go right."),
        ("ጸጋም", "ts'egam", "left", "ናብ ጸጋም", "nab ts'egam", "Go left."),
    ]),
    ("Work and School", [
        ("ስራሕ", "sərah", "work", "ስራሕ ጽብቕ እዩ", "sərah tsəbbuq iyu", "The work is good."),
        ("ቤት ትምህርቲ", "bet təmhərti", "school", "ቤት ትምህርቲ ክፍቲ እዩ", "bet təmhərti kəfti iyu", "The school is open."),
        ("ተማሃሪ", "temahari", "student", "ተማሃሪ ይምሃር", "temahari yəmhar", "The student learns."),
        ("መምህር", "memhər", "teacher", "መምህር ይዛረብ", "memhər yəzarab", "The teacher speaks."),
        ("መጽሓፍ", "mets'haf", "book", "መጽሓፍ ዕጹው እዩ", "mets'haf əts'uw iyu", "The book is closed."),
        ("እስክርቢቶ", "əskərbito", "pen", "እስክርቢቶ ጽብቕ እዩ", "əskərbito tsəbbuq iyu", "The pen is good."),
    ]),
    ("Health and the Body", [
        ("ሰውነት", "sewnet", "body", "ሰውነት ጽብቕ እዩ", "sewnet tsəbbuq iyu", "The body is good."),
        ("ርእሲ", "rə'si", "head", "ርእሲ ይሓምም", "rə'si yəhaməm", "The head aches."),
        ("ዐይኒ", "'ayni", "eye", "ዐይኒ ትርኢ", "ayni tər'i", "The eye sees."),
        ("ኢድ", "id", "hand, arm", "ኢድ ይሓምም", "id yəhaməm", "The hand aches."),
        ("እግሪ", "əgri", "foot, leg", "እግሪ ይሓምም", "əgri yəhaməm", "The leg aches."),
        ("ሓኪም", "hakim", "doctor", "ሓኪም ይሓዊ", "hakim yəhawwi", "The doctor heals."),
    ]),
    ("Emotions and Feelings", [
        ("ሓጎስ", "hagos", "joy", "ሓጎስ ጽብቕ እዩ", "hagos tsəbbuq iyu", "Joy is good."),
        ("ሓዘን", "hazan", "sadness", "ሓዘን ከይዱ", "hazan käydu", "The sadness is gone."),
        ("ፍርሒ", "fərhi", "fear", "ፍርሒ ከይዱ", "fərhi käydu", "The fear is gone."),
        ("ፍቕሪ", "fəqri", "love", "ፍቕሪ ሓያል እዩ", "fəqri hayal iyu", "Love is strong."),
        ("ቅንኢ", "qən'i", "jealousy", "ቅንኢ ሕማቕ እዩ", "qən'i həmaq iyu", "Jealousy is bad."),
        ("ሰላም", "selam", "peace", "ሰላም ጽብቕ እዩ", "selam tsəbbuq iyu", "Peace is good."),
    ]),
    ("Nature and Weather", [
        ("ተፈጥሮ", "tefet'ro", "nature", "ተፈጥሮ ጽብቕ እዩ", "tefet'ro tsəbbuq iyu", "Nature is beautiful."),
        ("ዝናብ", "zənab", "rain", "ዝናብ ይዝንብ", "zənab yəzənb", "The rain is falling."),
        ("ጸሓይ", "ts'ahay", "sun", "ጸሓይ ውዑይ እዩ", "ts'ahay wu'uy iyu", "The sun is hot."),
        ("ወርሒ", "werhi", "moon", "ወርሒ ብሩህ እዩ", "werhi bəruh iyu", "The moon is bright."),
        ("ኦም", "om", "tree", "ኦም ዓቢ እዩ", "om 'abi iyu", "The tree is big."),
        ("ዕንባባ", "'ənbaba", "flower", "ዕንባባ ጽብቕ እዩ", "'ənbaba tsəbbuq iyu", "The flower is beautiful."),
    ]),
    ("Shopping and Money", [
        ("ገንዘብ", "genzeb", "money", "ገንዘብ ጽብቕ እዩ", "genzeb tsəbbuq iyu", "Money is good."),
        ("ዋጋ", "waga", "price", "ዋጋ ልዑል እዩ", "waga lə'ul iyu", "The price is high."),
        ("ሱቕ", "suq", "shop, market", "ሱቕ ክፍቲ እዩ", "suq kəfti iyu", "The shop is open."),
        ("ርኺብ", "rəkhib", "cheap", "ርኺብ ጽብቕ እዩ", "rəkhib tsəbbuq iyu", "Cheap is good."),
        ("ገዛኢ", "geza'i", "customer", "ገዛኢ ሕጉስ እዩ", "geza'i həgus iyu", "The customer is happy."),
        ("ነጋዳይ", "negaday", "seller", "ነጋዳይ ጽብቕ እዩ", "negaday tsəbbuq iyu", "The seller is good."),
    ]),
    ("Friendship and Social Life", [
        ("መሓዛ", "mehaza", "friend", "መሓዛ ጽብቕ እዩ", "mehaza tsəbbuq iyu", "The friend is good."),
        ("እንግዳ ተቀባልነት", "əngəda teqebalənet", "hospitality", "እንግዳ ተቀባልነት ጽብቕ እዩ", "əngəda teqebalənet tsəbbuq iyu", "Hospitality is good."),
        ("ውይይት", "wəyəyət", "conversation", "ውይይት ጽብቕ እዩ", "wəyəyət tsəbbuq iyu", "The conversation is good."),
        ("ግብዣ", "gəbzha", "feast", "ግብዣ ጽብቕ እዩ", "gəbzha tsəbbuq iyu", "The feast is good."),
        ("ሳዕስዒት", "sa'sə'it", "dance", "ሳዕስዒት ጽብቕ እዩ", "sa'sə'it tsəbbuq iyu", "The dance is beautiful."),
        ("መዝሙር", "mezəmur", "song", "መዝሙር ጽብቕ እዩ", "mezəmur tsəbbuq iyu", "The song is beautiful."),
    ]),
    ("Technology and Communication", [
        ("ተሌፎን", "telefon", "telephone", "ተሌፎን ይደውል", "telefon yədewl", "The phone is ringing."),
        ("ኮምፒዩተር", "kompiyuter", "computer", "ኮምፒዩተር ይሰርሕ", "kompiyuter yəserh", "The computer is working."),
        ("ኢንተርነት", "internet", "internet", "ኢንተርነት ቀልጢፍ እዩ", "internet qelt'if iyu", "The internet is fast."),
        ("ኤሌክትሪክ", "elektrik", "electricity", "ኤሌክትሪክ ኣሎ", "elektrik allo", "There is electricity."),
        ("መልእኽቲ", "mel'əxti", "message", "መልእኽቲ መጺኡ", "mel'əxti mets'i'u", "The message has arrived."),
        ("ራድዮ", "radio", "radio", "ራድዮ ይዘምር", "radio yəzemər", "The radio is playing."),
    ]),
]

QUESTIONS = [
    ("ሽመይ ዝብሃል?", "shimay zəbhal", "What is your name?"),
    ("ኣደ ኣበይ ኣላ?", "ade abäy alla", "Where is mother?"),
    ("ክንደይ ይኸውን?", "kəndäy yəkhäwn", "How much does it cost?"),
    ("ስለምንታይ?", "sələmentay", "Why?"),
    ("መዓስ?", "me'as", "When?"),
    ("እዚ መን እዩ?", "əzi men iyu", "Who is this?"),
    ("ምግቢ ከመይ እዩ?", "məgbi kemäy iyu", "How is the food?"),
    ("ካበይ መጺእኻ?", "kabäy mets'i'əkha", "Where are you from? (to a man)"),
]

COMMANDS = [
    ("ናብዚ ና!", "nabzi na", "Come here!"),
    ("ኪድ!", "kid", "Go!"),
    ("ተቀመጥ!", "teqemet'", "Sit down!"),
    ("ቀስ ብል ተዛረብ!", "qes bəl təzarab", "Speak slowly!"),
    ("ሓግዘኒ!", "hagzeni", "Help me!"),
    ("ስማዕ!", "səma'", "Listen!"),
    ("ርኣይ!", "rə'ay", "Look!"),
    ("ኣቁም!", "aqum", "Stop!"),
]

DESCRIBE = [
    ("ነዊሕ ሰብኣይ, ነዊሕ እዩ.", "newih seb'ay, newih iyu", "The tall man, he is tall."),
    ("ጽብቕቲ ሰበይቲ, ጽብቕቲ እያ.", "tsəbəqti sebäyti, tsəbəqti iya", "The beautiful woman, she is beautiful."),
    ("ዓቢ ቤት, ዓቢ እዩ.", "'abi bet, 'abi iyu", "The big house, it is big."),
    ("ቀይሕ መኪና, ቀይሕ እዩ.", "qeyəh mekina, qeyəh iyu", "The red car, it is red."),
    ("ንእሽተይ ቆልዓ, ንእሽተይ እዩ.", "nə'əshtëy qol'a, nə'əshtëy iyu", "The small child, he/she is small."),
    ("ሓዲሽ መጽሓፍ, ሓዲሽ እዩ.", "hadish mets'haf, hadish iyu", "The new book, it is new."),
    ("ውዑይ ጸሓይ, ውዑይ እዩ.", "wu'uy ts'ahay, wu'uy iyu", "The hot sun, it is hot."),
    ("ቀዛፊ ማይ, ቀዛፊ እዩ.", "qezzafi may, qezzafi iyu", "The cold water, it is cold."),
]
STORIES = [
    ("Story I: The Boy and the Lamb", [
        ("ሓደ ቆልዓ ነይሩ።", "hade qol'a näyru", "There was a boy."),
        (" እቲ ቆልዓ ሓደ በግዒ ኣለዎ።", "əti qol'a hade beg'i aläwo", "The boy has a lamb."),
        ("እቲ በግዒ ጻዕዳ እዩ።", "əti beg'i ts'a'da iyu", "The lamb is white."),
        ("እቲ ቆልዓ ነቲ በግዒ ይፈትዎ።", "əti qol'a neti beg'i yəfetwo", "The boy loves the lamb."),
        ("ሓደ መዓልቲ እቲ በግዒ ጠፊኡ።", "hade me'alti əti beg'i t'efi'u", "One day the lamb got lost."),
        ("እቲ ቆልዓ ኩሉ ቦታ ደልዮ።", "əti qol'a kulu bota dälyo", "The boy searched everywhere."),
        ("ኣብ መወዳእታ ረኺብዎ።", "ab meweda'əta rekhəbwo", "Finally he found it."),
        ("ብጣዕሚ ሕጉስ ኮይኑ።", "bət'a'mi həgus koynu", "He was very happy."),
    ]),
    ("Story II: The Rainy Day", [
        ("ሎሚ ዝናብ ይዝንብ።", "lomi zənab yəzənb", "Today the rain is falling."),
        ("ህጻናት ኣብ ቤት ይኹኑ።", "həts'anat ab bet yəkhunu", "The children stay in the house."),
        ("ኣደ ምግቢ ትሰርሕ።", "ade məgbi təserh", "Mother is cooking food."),
        ("ምግቢ ጽብቕ እዩ።", "məgbi tsəbbuq iyu", "The food is good."),
        ("ኣቦ መጽሓፍ ይነብብ።", "abo mets'haf yənebəb", "Father is reading a book."),
        ("ድሕሪ ዝናብ ጸሓይ ወጺኣ።", "dəhri zənab ts'ahay wets'i'a", "After the rain the sun came out."),
        ("ህጻናት ናብ ደገ ወጺኦም።", "həts'anat nab degä wets'i'om", "The children went outside."),
        ("ኣብ ዕርዲ ይጻወቱ።", "ab ə'rdi yəts'awetu", "They are playing in the yard."),
    ]),
    ("Story III: The Market Trip", [
        ("ጽባሕ ናብ ሱቕ ንኸይድ።", "tsəbah nab suq nəkhaid", "Tomorrow we go to the market."),
        ("ኣደ እንጀራ ትገዝእ።", "ade ənjəra təgezə'", "Mother buys injera."),
        ("ኣቦ ስጋ ይገዝእ።", "abo səga yəgezə'", "Father buys meat."),
        ("ቆልዓ ከረሜላ ይገዝእ።", "qol'a keremela yəgezə'", "The child buys candy."),
        ("እንጀራ ጽብቕ እዩ።", "ənjəra tsəbbuq iyu", "The injera is good."),
        ("ስጋ ክቡር እዩ።", "səga kəbur iyu", "The meat is expensive."),
        ("ኩልና ናብ ገዛ ንኸይድ።", "kulna nab geza nəkhaid", "We all go home."),
        ("ኩልና ጽብቕ ንበልዕ።", "kulna tsəbbuq nəbelə'", "We all eat well."),
    ]),
]

IDIOMS = [
    ("ከብዲ ኣሎኒ ዝበለ ዓሣ ኣይትበልዕ", "kebdi aloni zəbäle 'asa aytəbelə'", "Do not eat the fish that says 'eat my liver'", "Beware of flatterers who offer too much."),
    ("ዝተኸድነ ዓወት ኣይኸውንን", "zətäkhädne 'awet ayəkhäwnn", "What is covered does not become victory", "Hidden things cannot win."),
    ("ድር ቢትራይ በይኑ", "dər bitray bäynu", "Between the spider and the fly", "A delicate, dangerous balance."),
    ("ፍርያት ጽንሒ ኣይትርእይ", "fəryat ts'ənhi aytərə'y", "Do not show the fruit before it ripens", "Do not boast before the result."),
]

CONVOS = [
    ("At the Market", [
        ("A", "ሰላም!", "selam", "Hello!"),
        ("B", "ሰላም! እንታይ ትደሊ?", "selam əntay tədeli", "Hello! What do you want?"),
        ("A", "ክንደይ ይኸውን?", "kəndäy yəkhäwn", "How much does it cost?"),
        ("B", "ዓሰርተ ብር።", "'äserte bər", "Ten birr."),
        ("A", "ክቡር እዩ።", "kəbur iyu", "Expensive."),
        ("B", "ርኺብ እገብሮ።", "rəkhib əgebro", "I will make it cheap."),
        ("A", "የቐንየለይ, እወስዶ።", "yekenyelay, əwesədo", "Thank you, I will take it."),
        ("B", "ደሓን ኹን!", "dehan kun", "Goodbye!"),
    ]),
    ("Meeting a Friend", [
        ("A", "ሰላም, ከመይ ኣለኻ?", "selam, kemay alekha", "Hi, how are you?"),
        ("B", "ደሓን ኣለኹ, የቐንየለይ። ንስኻ?", "dehan aleku, yekenyelay. nəsəkha", "I am fine, thanks. And you?"),
        ("A", "ኣነውን ደሓን ኣለኹ።", "anäwn dehan aleku", "I am fine too."),
        ("B", "ሽመይ ዝብሃል?", "shimay zəbhal", "What is your name?"),
        ("A", "ሽመይ ዳዊት እዩ።", "shimay dawit iyu", "My name is Dawit."),
        ("B", "ሕጉስ ምትእኽኻብ።", "həgus məttə'əkhkhab", "Nice to meet you."),
        ("A", "ኣነውን ሕጉስ።", "anäwn həgus", "Nice to meet you too."),
        ("B", "ክንደይ ክንራኸብ!", "kəndäy kənrakhab", "Until we meet again!"),
    ]),
    ("Solving a Problem", [
        ("A", "ጸገም ኣሎ።", "ts'egem allo", "There is a problem."),
        ("B", "እንታይ ጸገም?", "əntay ts'egem", "What problem?"),
        ("A", "መኪና ተሰቢራ።", "mekina tesebira", "The car broke down."),
        ("B", "ኣይትሽገር።", "aytshəger", "Do not worry."),
        ("A", "ሓግዘኒ!", "hagzeni", "Help me!"),
        ("B", "እሕግዘካ።", "əhəgezkha", "I will help you."),
        ("A", "ብጣዕሚ የቐንየለይ!", "bət'a'mi yekenyelay", "Thank you very much!"),
        ("B", "እንኳዕ ደሓን መጻእኻ።", "ənkwa' dehan mets'a'əkha", "You are welcome."),
    ]),
]

CITATIONS = [
    "Omniglot. Useful phrases in Tigrinya — numbers 1-10, basic phrases.",
    "Wikivoyage contributors. Tigrinya phrasebook.",
    "Buckley J. Tigrinya proverbs and riddles (studies of Eritrean oral tradition).",
    "Kane T. Tigrinya-English Dictionary. Dunwoody Press; 2000.",
    "ISO 639-1:2002 language code ti; ISO 639-3:2007 language code tir.",
    "Standard pedagogical sources for Tigrinya vocabulary, usage, and phraseology.",
]
