# -*- coding: utf-8 -*-
"""Language data module: Turkmen (tuk). Facts verified 2026-10-17 via
Wikibooks lessons, encyclopedia language article, comparative proverb study."""

SLUG = "language-turkmen"
PREFIX = "JAH-LTUK-"
SIG_PREFIX = "JAH-LTUKS-"
NAME = "Turkmen"
NATIVE = "Türkmençe"
NATIVE_ROMAN = "Türkmençe"
ISO1 = "tk"
ISO3 = "tuk"
FAMILY = "Turkic > Oghuz (Southwestern Turkic)"
SPEAKERS = "about 7 to 8 million speakers"
REGIONS = "Turkmenistan, where it is the official language, plus Iran, Afghanistan, Uzbekistan and Russia"
SCRIPT_NAME = "Latin script (official since 1993)"
WORD_ORDER = "subject-object-verb (SOV)"
AI_NAME = "JAH Turkmen Language Archivist"
SIG_AI_NAME = "JAH Turkmen Signature Archivist"

OVERVIEW = (
    "Turkmen (Türkmençe) is an Oghuz Turkic language spoken by about 7 to 8 million people, most of "
    "them in Turkmenistan where it is the official language, with large communities in Iran and "
    "Afghanistan. It is closely related to Turkish and Azerbaijani. Since 1993 it has been written in "
    "a Latin alphabet with distinctive letters (ä, ž, ň, ö, ü, ý, ş, ç). Like all Turkic languages it is "
    "agglutinative with vowel harmony and subject-object-verb word order."
)

SCRIPT_DESC = (
    "Turkmen uses a Latin alphabet of 30 letters, official since 1993: Aa Bb Çç Dd Ee Ää Ff Gg Hh Ii "
    "Jj Žž Kk Ll Mm Nn Ňň Oo Öö Pp Rr Ss Şş Tt Uu Üü Ww Yy Ýý Zz. The special letters are ä (like 'a' in "
    "'cat'), ž (like 's' in 'measure'), ň (like 'ng' in 'sing'), ö and ü (rounded front vowels), ý (like "
    "'y' in 'yes'), ş ('sh') and ç ('ch'). Before 1993 Turkmen was written in Cyrillic; the Arabic "
    "script is still used by Turkmen in Iran and Afghanistan."
)

ALPHABET_NOTE = (
    "The 30-letter Latin alphabet is phonetic: one letter, one sound. The table shows the letters that "
    "English readers must learn; the rest match English, with g always hard."
)

ALPHABET_SAMPLE = [
    ("Ää", "like 'a' in 'cat'"), ("Žž", "like 's' in 'measure'"), ("Ňň", "like 'ng' in 'sing'"),
    ("Öö", "rounded 'e'"), ("Üü", "rounded 'i'"), ("Ýý", "like 'y' in 'yes'"),
    ("Şş", "'sh'"), ("Çç", "'ch'"), ("Jj", "like 'j' in 'jump'"),
    ("Ww", "like English 'w'"), ("Yy", "like 'u' in 'put'"), ("Ee", "like 'e' in 'bed'"),
]

SOUNDS_DESC = (
    "Turkmen has 9 vowels in two harmony groups: back (a, y, o, u) and front (e, ä, ö, ü) plus i which "
    "is neutral. Suffixes change their vowels to match the root — this vowel harmony is the heartbeat "
    "of the language. The consonants ž and ň are the signature sounds. Stress usually falls on the "
    "last syllable. Long vowels (from lost consonants) can change meaning, so hold them full length."
)

GRAMMAR_DESC = (
    "Turkmen is subject-object-verb and agglutinative: suffixes stack onto unchanging roots in a fixed "
    "order. Nouns take six cases; there is no grammatical gender and no articles. The verb root never "
    "changes — tense, person, negation and questions are suffixes: bilýärin = 'I know', bilemok = 'to "
    "know', bilmeýärin = 'I do not know'. Questions add the particle -mi/-my."
)

TENSE_DESC = (
    "Tense is a suffix between the root and the person ending. Men işleýärin = 'I am working'; men "
    "işledim = 'I worked'; men işlärin = 'I will work'. Negation inserts -me-/-ma- before the tense: "
    "men işlemeýärin = 'I am not working'. The examples below hold the subject 'men' (I) steady on "
    "three everyday verbs — işlemek (to work), iýmek (to eat), gitmek (to go) — so you can watch only "
    "the tense suffix move."
)

REGISTER_DESC = (
    "Respect in Turkmen is carried by the siz/sen distinction: siz is polite and plural, sen is "
    "intimate. Greet elders with salam alaykum (answered wa alaykum salam); friends get selam. Sag "
    "boluň ('be healthy') thanks, blesses and farewells all at once — the most Turkmen word there is. "
    "Address respected elders as aga (elder brother) or eje (elder sister). Never rush a greeting; ask "
    "after health, family and work in turn."
)

COMPLEX_DESC = (
    "Turkmen joins clauses with sebäbi (because), ýöne (but), and üçin (in order to). Relative clauses "
    "come before the noun as participles: işleýän adam (the person who works). Conditions use eger "
    "(if) with the -sa/-se suffix. Because the verb always comes last, build the whole scene first and "
    "deliver the action at the end."
)

REVIEW_NOTE = (
    "You now hold the complete Turkmen ladder: the 30-letter Latin script with ä ž ň, vowel harmony "
    "and final stress, agglutinative SOV grammar with six cases, core nouns verbs and adjectives, "
    "pronouns, numbers to one hundred, time words, greetings, ten themed sentence sets, the suffix "
    "tenses, questions, commands, descriptions, three graded stories, nakyl proverbs, formal registers, "
    "and three full conversations. Let the suffixes stack and the vowels harmonize."
)

NOUNS = [
    ("suw", "suw", "water", "Suw gowy.", "suw gowy", "The water is good."),
    ("çörek", "çörek", "bread", "Çörek gowy.", "çörek gowy", "The bread is good."),
    ("öý", "öý", "house", "Öý uly.", "öý uly", "The house is big."),
    ("maşyn", "maşyn", "car", "Maşyn täze.", "maşyn täze", "The car is new."),
    ("kitap", "kitap", "book", "Kitap gowy.", "kitap gowy", "The book is good."),
    ("bazar", "bazar", "market", "Bazar uly.", "bazar uly", "The market is big."),
    ("mekdep", "mekdep", "school", "Mekdep gowy.", "mekdep gowy", "The school is good."),
    ("gün", "gün", "day, sun", "Gün gowy.", "gün gowy", "The day is good."),
    ("gije", "gije", "night", "Gije gowy.", "gije gowy", "The night is good."),
    ("ata", "ata", "father", "Ata gowy.", "ata gowy", "Father is good."),
    ("ene", "ene", "mother", "Ene gowy.", "ene gowy", "Mother is good."),
    ("söýgi", "söýgi", "love", "Söýgi gowy.", "söýgi gowy", "Love is good."),
]

VERBS = [
    ("iýmek", "iýmek", "to eat", "Iýmek gowy.", "iýmek gowy", "Eating is good."),
    ("içmek", "içmek", "to drink", "Içmek gowy.", "içmek gowy", "Drinking is good."),
    ("gitmek", "gitmek", "to go", "Gitmek gowy.", "gitmek gowy", "Going is good."),
    ("gelmek", "gelmek", "to come", "Gelmek gowy.", "gelmek gowy", "Coming is good."),
    ("geplemek", "geplemek", "to speak", "Geplemek gowy.", "geplemek gowy", "Speaking is good."),
    ("işlemek", "işlemek", "to work", "Işlemek gowy.", "işlemek gowy", "Working is good."),
    ("öwrenmek", "öwrenmek", "to learn", "Öwrenmek gowy.", "öwrenmek gowy", "Learning is good."),
    ("bermek", "bermek", "to give", "Bermek gowy.", "bermek gowy", "Giving is good."),
    ("söýmek", "söýmek", "to love", "Söýmek gowy.", "söýmek gowy", "Loving is good."),
    ("ýaşamak", "ýaşamak", "to live", "Ýaşamak gowy.", "ýaşamak gowy", "Living is good."),
]

ADJS = [
    ("gowy", "gowy", "good", "gowy öý", "gowy öý", "a good house"),
    ("erbet", "erbet", "bad", "erbet maşyn", "erbet maşyn", "a bad car"),
    ("uly", "uly", "big", "uly öý", "uly öý", "a big house"),
    ("kiçi", "kiçi", "small", "kiçi kitap", "kiçi kitap", "a small book"),
    ("täze", "täze", "new", "täze maşyn", "täze maşyn", "a new car"),
    ("köne", "köne", "old", "köne öý", "köne öý", "an old house"),
    ("gyzyl", "gyzyl", "red", "gyzyl maşyn", "gyzyl maşyn", "a red car"),
    ("ak", "ak", "white", "ak köýnek", "ak köýnek", "a white shirt"),
]

PRONOUNS = [
    ("men", "men", "I"),
    ("sen", "sen", "you (intimate)"),
    ("siz", "siz", "you (polite/plural)"),
    ("ol", "ol", "he / she / it"),
    ("biz", "biz", "we"),
    ("olar", "olar", "they"),
    ("bu", "bu", "this"),
    ("şol", "şol", "that"),
]

NUMBERS = [
    ("bir", "bir", "one"), ("iki", "iki", "two"), ("üç", "üç", "three"),
    ("dört", "dört", "four"), ("bäş", "bäş", "five"), ("alty", "alty", "six"),
    ("ýedi", "ýedi", "seven"), ("sekiz", "sekiz", "eight"),
    ("dokuz", "dokuz", "nine"), ("on", "on", "ten"),
    ("ýigrimi", "ýigrimi", "twenty"), ("ýüz", "ýüz", "one hundred"),
]

TIME_WORDS = [
    ("bu gün", "bu gün", "today"), ("ertir", "ertir", "tomorrow"),
    ("düýn", "düýn", "yesterday"), ("hepde", "hepde", "week"),
    ("aý", "aý", "month"), ("ýyl", "ýyl", "year"),
]

GREETINGS = [
    ("Salam alaykum!", "salam alaykum", "Hello! (formal)"),
    ("Wa alaykum salam!", "wa alaykum salam", "And peace be upon you! (reply)"),
    ("Salam!", "salam", "Hello!"),
    ("Ýagdaýlaryňyz nähili?", "ýagdaýlaryňyz nähili", "How are you? (polite)"),
    ("Gowy, sag bol!", "gowy sag bol", "Fine, thanks! (reply)"),
    ("Sag boluň!", "sag boluň", "Thank you! / Be healthy!"),
    ("Köp sag boluň!", "köp sag boluň", "Thank you very much!"),
    ("Haýyş!", "haýyş", "Please!"),
    ("Bagyşlaň!", "bagyşlaň", "Sorry / excuse me!"),
    ("Hoş gal!", "hoş gal", "Goodbye (stay well)!"),
]
THEMES = [
    ("Home and Family", [
        ("maşgala", "maşgala", "family", "Maşgala gowy.", "maşgala gowy", "The family is good."),
        ("ata", "ata", "father", "Ata işleýär.", "ata işleýär", "Father works."),
        ("ene", "ene", "mother", "Ene nahar bişirýär.", "ene nahar bişirýär", "Mother cooks food."),
        ("aga", "aga", "older brother", "Aga kömek edýär.", "aga kömek edýär", "The older brother helps."),
        ("jigi", "jigi", "younger sibling", "Jigi okaýar.", "jigi okaýar", "The younger sibling studies."),
        ("dogan", "dogan", "sibling, relative", "Dogan oýnaýar.", "dogan oýnaýar", "The sibling plays."),
    ]),
    ("Food and Cooking", [
        ("nahar", "nahar", "food", "Nahar tagamly.", "nahar tagamly", "The food is tasty."),
        ("çörek", "çörek", "bread", "Çörek tagamly.", "çörek tagamly", "The bread is tasty."),
        ("et", "et", "meat", "Et gymmat.", "et gymmat", "The meat is expensive."),
        ("suw", "suw", "water", "Suw gowy.", "suw gowy", "The water is good."),
        ("süýt", "süýt", "milk", "Süýt gowy.", "süýt gowy", "The milk is good."),
        ("çaý", "çaý", "tea", "Çaý gowy.", "çaý gowy", "The tea is good."),
    ]),
    ("Travel and Directions", [
        ("ýol", "ýol", "road", "Ýol uzak.", "ýol uzak", "The road is long."),
        ("maşyn", "maşyn", "car", "Maşyn gidýär.", "maşyn gidýär", "The car goes."),
        ("uçar", "uçar", "airplane", "Uçar uçýar.", "uçar uçýar", "The plane flies."),
        ("durmuş", "durmuş", "station", "Durmuş ýakyn.", "durmuş ýakyn", "The station is near."),
        ("sag", "sag", "right", "Saga git.", "saga git", "Go right."),
        ("çep", "çep", "left", "Çepe git.", "çepe git", "Go left."),
    ]),
    ("Work and School", [
        ("iş", "iş", "work", "Iş gowy.", "iş gowy", "The work is good."),
        ("mekdep", "mekdep", "school", "Mekdep açyk.", "mekdep açyk", "The school is open."),
        ("okuwçy", "okuwçy", "student", "Okuwçy okaýar.", "okuwçy okaýar", "The student studies."),
        ("mugallym", "mugallym", "teacher", "Mugallym gepleýär.", "mugallym gepleýär", "The teacher speaks."),
        ("kitap", "kitap", "book", "Kitap ýapyk.", "kitap ýapyk", "The book is closed."),
        ("ruçka", "ruçka", "pen", "Ruçka gowy.", "ruçka gowy", "The pen is good."),
    ]),
    ("Health and the Body", [
        ("beden", "beden", "body", "Beden gowy.", "beden gowy", "The body is good."),
        ("kelle", "kelle", "head", "Kelle agyrýar.", "kelle agyrýar", "The head aches."),
        ("göz", "göz", "eye", "Göz görýär.", "göz görýär", "The eye sees."),
        ("gol", "gol", "arm, hand", "Gol agyrýar.", "gol agyrýar", "The arm aches."),
        ("aýak", "aýak", "leg, foot", "Aýak agyrýar.", "aýak agyrýar", "The leg aches."),
        ("lukman", "lukman", "doctor", "Lukman bejerýär.", "lukman bejerýär", "The doctor heals."),
    ]),
    ("Emotions and Feelings", [
        ("şatlyk", "şatlyk", "joy", "Şatlyk gowy.", "şatlyk gowy", "Joy is good."),
        ("gaýgy", "gaýgy", "sadness", "Gaýgy geçdi.", "gaýgy geçdi", "The sadness is gone."),
        ("gorky", "gorky", "fear", "Gorky geçdi.", "gorky geçdi", "The fear is gone."),
        ("söýgi", "söýgi", "love", "Söýgi güýçli.", "söýgi güýçli", "Love is strong."),
        ("göriplik", "göriplik", "jealousy", "Göriplik erbet.", "göriplik erbet", "Jealousy is bad."),
        ("parahatlyk", "parahatlyk", "peace", "Parahatlyk gowy.", "parahatlyk gowy", "Peace is good."),
    ]),
    ("Nature and Weather", [
        ("tebigat", "tebigat", "nature", "Tebigat owadan.", "tebigat owadan", "Nature is beautiful."),
        ("ýagyş", "ýagyş", "rain", "Ýagyş ýagýar.", "ýagyş ýagýar", "The rain is falling."),
        ("gün", "gün", "sun", "Gün yssy.", "gün yssy", "The sun is hot."),
        ("aý", "aý", "moon", "Aý ýagty.", "aý ýagty", "The moon is bright."),
        ("agaç", "agaç", "tree", "Agaç uly.", "agaç uly", "The tree is big."),
        ("gül", "gül", "flower", "Gül owadan.", "gül owadan", "The flower is beautiful."),
    ]),
    ("Shopping and Money", [
        ("pul", "pul", "money", "Pul gowy.", "pul gowy", "Money is good."),
        ("baha", "baha", "price", "Baha ýokary.", "baha ýokary", "The price is high."),
        ("dükan", "dükan", "shop", "Dükan açyk.", "dükan açyk", "The shop is open."),
        ("arzan", "arzan", "cheap", "Arzan gowy.", "arzan gowy", "Cheap is good."),
        ("müşderi", "müşderi", "customer", "Müşderi şat.", "müşderi şat", "The customer is happy."),
        ("satyjy", "satyjy", "seller", "Satyjy gowy.", "satyjy gowy", "The seller is good."),
    ]),
    ("Friendship and Social Life", [
        ("dost", "dost", "friend", "Dost gowy.", "dost gowy", "The friend is good."),
        ("myhmansöýerlik", "myhmansöýerlik", "hospitality", "Myhmansöýerlik gowy.", "myhmansöýerlik gowy", "Hospitality is good."),
        ("gürleşme", "gürleşme", "conversation", "Gürleşme gowy.", "gürleşme gowy", "The conversation is good."),
        ("toý", "toý", "feast, celebration", "Toý gowy.", "toý gowy", "The celebration is good."),
        ("tans", "tans", "dance", "Tans owadan.", "tans owadan", "The dance is beautiful."),
        ("aýdym", "aýdym", "song", "Aýdym owadan.", "aýdym owadan", "The song is beautiful."),
    ]),
    ("Technology and Communication", [
        ("telefon", "telefon", "telephone", "Telefon jyňňyrdaýar.", "telefon jyňňyrdaýar", "The phone is ringing."),
        ("kompýuter", "kompýuter", "computer", "Kompýuter işleýär.", "kompýuter işleýär", "The computer is working."),
        ("internet", "internet", "internet", "Internet çalt.", "internet çalt", "The internet is fast."),
        ("tok", "tok", "electricity", "Tok bar.", "tok bar", "There is electricity."),
        ("habar", "habar", "message, news", "Habar geldi.", "habar geldi", "The message has arrived."),
        ("radio", "radio", "radio", "Radio çalýar.", "radio çalýar", "The radio is playing."),
    ]),
]

QUESTIONS = [
    ("Siziň adyňyz näme?", "siziň adyňyz näme", "What is your name?"),
    ("Ejeň nirede?", "ejeň nirede", "Where is mother?"),
    ("Bu näçe?", "bu näçe", "How much is this?"),
    ("Näme üçin?", "näme üçin", "Why?"),
    ("Haçan?", "haçan", "When?"),
    ("Bu kim?", "bu kim", "Who is this?"),
    ("Nahar nähili?", "nahar nähili", "How is the food?"),
    ("Siz nireden?", "siz nireden", "Where are you from?"),
]

COMMANDS = [
    ("Bäri gel!", "bäri gel", "Come here!"),
    ("Git!", "git", "Go!"),
    ("Otur!", "otur", "Sit down!"),
    ("Haýal geple!", "haýal geple", "Speak slowly!"),
    ("Maňa kömek et!", "maňa kömek et", "Help me!"),
    ("Diňle!", "diňle", "Listen!"),
    ("Seret!", "seret", "Look!"),
    ("Dur!", "dur", "Stop!"),
]

DESCRIBE = [
    ("Beýik adam, beýik.", "beýik adam beýik", "The tall man, he is tall."),
    ("Owadan aýal, owadan.", "owadan aýal owadan", "The beautiful woman, she is beautiful."),
    ("Uly öý, uly.", "uly öý uly", "The big house, it is big."),
    ("Gyzyl maşyn, gyzyl.", "gyzyl maşyn gyzyl", "The red car, it is red."),
    ("Kiçi çaga, kiçi.", "kiçi çaga kiçi", "The small child, he/she is small."),
    ("Täze kitap, täze.", "täze kitap täze", "The new book, it is new."),
    ("Yssy gün, yssy.", "yssy gün yssy", "The hot sun, it is hot."),
    ("Sowuk suw, sowuk.", "sowuk suw sowuk", "The cold water, it is cold."),
]

STORIES = [
    ("Story I: The Boy and the Lamb", [
        ("Bir oglan bar eken.", "bir oglan bar eken", "There was a boy."),
        ("Oglanyň bir guzysy bar.", "oglanyň bir guzysy bar", "The boy has a lamb."),
        ("Guzy ak.", "guzy ak", "The lamb is white."),
        ("Oglan guzyny söýýär.", "oglan guzyny söýýär", "The boy loves the lamb."),
        ("Bir gün guzy ýitdi.", "bir gün guzy ýitdi", "One day the lamb got lost."),
        ("Oglan hemme ýeri gözledi.", "oglan hemme ýeri gözledi", "The boy searched everywhere."),
        ("Ahyrynda ony tapdy.", "ahyrynda ony tapdy", "Finally he found it."),
        ("Ol örän şat boldy.", "ol örän şat boldy", "He was very happy."),
    ]),
    ("Story II: The Rainy Day", [
        ("Bu gün ýagyş ýagýar.", "bu gün ýagyş ýagýar", "Today the rain is falling."),
        ("Çagalar öýde galýar.", "çagalar öýde galýar", "The children stay in the house."),
        ("Ene nahar bişirýär.", "ene nahar bişirýär", "Mother is cooking food."),
        ("Nahar tagamly.", "nahar tagamly", "The food is tasty."),
        ("Ata kitap okaýar.", "ata kitap okaýar", "Father is reading a book."),
        ("Ýagyşdan soň gün çykdy.", "ýagyşdan soň gün çykdy", "After the rain the sun came out."),
        ("Çagalar daşary çykdy.", "çagalar daşary çykdy", "The children went outside."),
        ("Olar howlyda oýnaýar.", "olar howlyda oýnaýar", "They are playing in the yard."),
    ]),
    ("Story III: The Market Trip", [
        ("Ertir bazara gidýäris.", "ertir bazara gidýäris", "Tomorrow we go to the market."),
        ("Ene çörek satyn alýar.", "ene çörek satyn alýar", "Mother buys bread."),
        ("Ata et satyn alýar.", "ata et satyn alýar", "Father buys meat."),
        ("Çaga süýji satyn alýar.", "çaga süýji satyn alýar", "The child buys candy."),
        ("Çörek tagamly.", "çörek tagamly", "The bread is tasty."),
        ("Et gymmat.", "et gymmat", "The meat is expensive."),
        ("Hemmemiz öýe gidýäris.", "hemmemiz öýe gidýäris", "We all go home."),
        ("Hemmemiz gowy iýýäris.", "hemmemiz gowy iýýäris", "We all eat well."),
    ]),
]

IDIOMS = [
    ("Akyl bile ynsap bolsa, daşda däl içdedir", "akyl bile ynsap bolsa daşda däl içdedir", "If there is wisdom with conscience, it is not outside but inside", "Wisdom and conscience live within oneself."),
    ("Boljak oglan ýaşlykdan bellidir", "boljak oglan ýaşlykdan bellidir", "The boy who will become a man is known from youth", "Character shows early."),
    ("Adam boljak bolsaň, bigänelikde däl, märekede ulal", "adam boljak bolsaň bigänelikde däl märekede ulal", "To become a person, grow not in solitude but among people", "People grow through community."),
    ("Saglyk baýlykdan gymmat", "saglyk baýlykdan gymmat", "Health is dearer than wealth", "Health outweighs riches."),
]

CONVOS = [
    ("At the Market", [
        ("A", "Salam!", "salam", "Hello!"),
        ("B", "Salam! Näme gerek?", "salam näme gerek", "Hello! What do you need?"),
        ("A", "Bu näçe?", "bu näçe", "How much is this?"),
        ("B", "On manat.", "on manat", "Ten manat."),
        ("A", "Gymmat.", "gymmat", "Expensive."),
        ("B", "Arzan ederin.", "arzan ederin", "I will make it cheap."),
        ("A", "Sag boluň, alýaryn.", "sag boluň alýaryn", "Thanks, I will take it."),
        ("B", "Hoş gal!", "hoş gal", "Goodbye!"),
    ]),
    ("Meeting a Friend", [
        ("A", "Salam, nähili?", "salam nähili", "Hi, how are you?"),
        ("B", "Gowy, sag bol! Sen nähili?", "gowy sag bol sen nähili", "Fine, thanks! How are you?"),
        ("A", "Men hem gowy.", "men hem gowy", "I am fine too."),
        ("B", "Seniň adyň näme?", "seniň adyň näme", "What is your name?"),
        ("A", "Meniň adym Serdar.", "meniň adym serdar", "My name is Serdar."),
        ("B", "Tanyşanyma şat.", "tanyşanyma şat", "Nice to meet you."),
        ("A", "Men hem şat.", "men hem şat", "Nice to meet you too."),
        ("B", "Ýene görüşeris!", "ýene görüşeris", "See you again!"),
    ]),
    ("Solving a Problem", [
        ("A", "Mesele bar.", "mesele bar", "There is a problem."),
        ("B", "Nähili mesele?", "nähili mesele", "What kind of problem?"),
        ("A", "Maşyn döwüldi.", "maşyn döwüldi", "The car broke down."),
        ("B", "Gaýgy etme.", "gaýgy etme", "Do not worry."),
        ("A", "Maňa kömek et!", "maňa kömek et", "Help me!"),
        ("B", "Men kömek ederin.", "men kömek ederin", "I will help."),
        ("A", "Köp sag boluň!", "köp sag boluň", "Thank you very much!"),
        ("B", "Arzymaýar.", "arzymaýar", "You are welcome."),
    ]),
]

CITATIONS = [
    "Wikibooks contributors. Turkmen/Lesson One: Siziň adyňyz näme? Wikibooks.",
    "Encyclopedia article: Turkmen language — vocabulary, numbers, colors, basic expressions.",
    "International Journal of Pedagogics. Comparative analysis of Uzbek and Turkmen proverbs. 2026.",
    "ISO 639-1:2002 language code tk; ISO 639-3:2007 language code tuk.",
    "Standard pedagogical sources for Turkmen vocabulary, usage, and phraseology.",
]
