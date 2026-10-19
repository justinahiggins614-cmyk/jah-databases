#!/usr/bin/env python3
"""Language data: Quechua (Runa Simi) - Southern Quechua variety.

Dedupe gate: 'quechua' zero hits across the full manifest; 'JAH-LQUE-' /
'JAH-LQUES-' zero hits in all shard index files of jah-databases-data-1
(checked BEFORE authoring). ID prefixes JAH-LQUE- (public) and JAH-LQUES-
(signature) verified free: zero hits in manifest id_prefix values (exact
and substring) and zero hits in shard record IDs.

Fact-check notes (2026-10-17): about 9 million speakers across the
Quechuan family (most-spoken Indigenous language family of the Americas);
official in Peru and Bolivia; 28-letter official alphabet (Peru),
including ch, ll, enye, q, and ejective/aspirated series; SOV word
order; agglutinative with suffix chains; 3 vowel phonemes (a, i, u);
evidential suffixes; inclusive/exclusive we; no grammatical gender;
ISO 639-1 qu, 639-3 que (macrolanguage).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

LANG = {
    "slug": "language-quechua",
    "name": "Quechua",
    "prefix": "JAH-LQUE-",
    "sig_prefix": "JAH-LQUES-",
    "tagline": ("Learn Quechua from the ground up: the language overview, the "
                "28-letter Latin alphabet, pronunciation and phonology, core "
                "vocabulary with sentences, grammar essentials, and themed "
                "sentence sets for daily life - every record carrying Quechua "
                "plus romanization plus English translation plus example "
                "sentences, taught progressively along the ladder."),
    "sig_phrase": "every word a thread in the Andean weave",
    "sig_method": ("His original Signature Quechua Method: every word a "
                   "thread in the Andean weave, every verb a living deed of "
                   "the mountain people, every proverb a memory of the high "
                   "valleys. The whole language taught as Signature science."),
    "search_ph": "Search Quechua words, verbs, phrases, grammar, dialogues...",
    "chat_ph": "Ask about Quechua...",
    "greet": ("I am the JAH Quechua Language Archivist. Ask me about Quechua - "
              "from the 28-letter alphabet and sounds through core words, "
              "grammar, and everyday sentences to stories, idioms, and "
              "conversations."),
    "role": ("Quechua language archivist - teaching Quechua from the 28-letter "
             "alphabet and sounds through core vocabulary, grammar, and "
             "everyday sentences to stories, idioms, registers, and "
             "conversations; teaching progressively along the ladder from "
             "foundations through compounded to advanced; answers from many "
             "angles - definition, example, pronunciation, usage, grammar, "
             "culture - using only archive data from this system"),
    "facts": [
        ("Alphabet", "28 letters - the official Quechua alphabet (Peru), including ch, ll, enye, q, and ejective/aspirated series"),
        ("Script", "Latin"),
        ("Word order", "Subject-Object-Verb (SOV)"),
        ("Speakers", "about 9 million across the Quechuan family"),
        ("Family", "Quechuan"),
        ("Region", "Andes: Peru, Bolivia, Ecuador, Colombia, Argentina, Chile - official in Peru and Bolivia"),
        ("Sounds", "3 vowel phonemes (a, i, u); ejective and aspirated consonants"),
        ("Grammar", "agglutinative - suffix chains; evidential markers; no grammatical gender"),
        ("ISO 639-1 / 639-3", "qu / que (macrolanguage)"),
    ],
    "check": {"letters": 28, "speakers_m": 9.0, "speakers_lo": 7.0,
              "speakers_hi": 11.0, "iso": "que", "word_order": "SOV",
              "family": "Quechuan", "script_line": "the Latin script"},
    "alphabet_note": ("The official Quechua alphabet has 28 letters. The "
                      "ejective series (p', t', k', q', ch') is pronounced "
                      "with a sharp pop; the aspirated series (ph, th, kh, "
                      "qh, chh) with a puff of air."),
    "alphabet": [
        ["a", "ah", "mama", "mother"],
        ["ch", "ch", "chaki", "foot"],
        ["chh", "ch + breath", "chhuru", "shell"],
        ["ch'", "ch + pop", "ch'isi", "evening"],
        ["h", "h", "hamuy", "to come"],
        ["i", "ee", "inti", "sun"],
        ["k", "k", "killa", "moon"],
        ["kh", "k + breath", "khuyay", "to love"],
        ["k'", "k + pop", "k'uchi", "pig"],
        ["l", "l", "llaqta", "town"],
        ["ll", "ly", "llank'ay", "to work"],
        ["m", "m", "mama", "mother"],
        ["n", "n", "nina", "fire"],
        ["ny", "ny", "nyuqa", "I"],
        ["p", "p", "pukyu", "spring"],
        ["ph", "p + breath", "phuyu", "cloud"],
        ["p'", "p + pop", "p'unchay", "day"],
        ["q", "deep k", "qullqi", "money"],
        ["qh", "q + breath", "qhapaq", "mighty"],
        ["q'", "q + pop", "q'illu", "yellow"],
        ["r", "flap", "riy", "to go"],
        ["s", "s", "sara", "corn"],
        ["t", "t", "tata", "father"],
        ["th", "t + breath", "thanta", "rag"],
        ["t'", "t + pop", "t'anta", "bread"],
        ["u", "oo", "urqu", "mountain"],
        ["w", "w", "wasi", "house"],
        ["y", "y", "yaku", "water"],
    ],
    "phonology_note": ("Quechua has only three vowel sounds; i and u open "
                       "toward e and o next to the uvular q. The ejectives "
                       "and aspirates are the signature sounds - practice "
                       "them slowly."),
    "phonology": [
        ["a", "ah as in father", "wasi (house)"],
        ["i", "ee as in machine; eh near q", "inti (sun)"],
        ["u", "oo as in moon; oh near q", "tuta (night)"],
        ["p'", "p with a sharp pop", "p'unchay (day)"],
        ["t'", "t with a sharp pop", "t'anta (bread)"],
        ["k'", "k with a sharp pop", "k'uchi (pig)"],
        ["q'", "deep q with a pop", "q'illu (yellow)"],
        ["ph", "p with a puff of air", "phuyu (cloud)"],
        ["q", "k made deep in the throat", "qullqi (money)"],
        ["ny", "ny as in canyon", "nyuqa (I)"],
        ["ll", "ly as in million", "llank'ay (work)"],
        ["stress", "almost always on the next-to-last syllable", "wasi (house)"],
    ],
    "nouns": [
        ["runa", "runa", "person"],
        ["qhari", "qhari", "man"],
        ["warmi", "warmi", "woman"],
        ["irqi", "irqi", "child"],
        ["wasi", "wasi", "house"],
        ["yaku", "yaku", "water"],
        ["mikhuna", "mikhuna", "food"],
        ["allqu", "allqu", "dog"],
        ["misi", "misi", "cat"],
        ["p'unchay", "p'unchay", "day"],
        ["tuta", "tuta", "night"],
        ["qillqa", "qillqa", "book, writing"],
    ],
    "verbs": [
        ["mikhuy", "mikhuy", "to eat"],
        ["upyay", "upyay", "to drink"],
        ["punyuy", "punyuy", "to sleep"],
        ["riy", "riy", "to go"],
        ["hamuy", "hamuy", "to come"],
        ["rimay", "rimay", "to speak"],
        ["qhaway", "qhaway", "to look"],
        ["ruway", "ruway", "to do, to make"],
        ["llank'ay", "llank'ay", "to work"],
        ["yachay", "yachay", "to learn, to know"],
        ["munay", "munay", "to want, to love"],
        ["rantiy", "rantiy", "to buy"],
    ],
    "adjectives": [
        ["allin", "allin", "good"],
        ["hatun", "hatun", "big"],
        ["uchuy", "uchuy", "small"],
        ["sumaq", "sumaq", "beautiful"],
        ["musuq", "musuq", "new"],
        ["machu", "machu", "old"],
        ["q'uñi", "q'uñi", "warm"],
        ["chiri", "chiri", "cold"],
        ["misk'i", "misk'i", "sweet"],
        ["sinchi", "sinchi", "strong"],
    ],
    "adverbs": [
        ["kunan", "kunan", "now"],
        ["qayna", "qayna", "yesterday"],
        ["paqarin", "paqarin", "tomorrow"],
        ["kaypi", "kaypi", "here"],
        ["chaypi", "chaypi", "there"],
        ["ancha", "ancha", "very"],
    ],
    "pronouns": [
        ["nyuqa", "nyuqa", "I"],
        ["qan", "qan", "you (singular)"],
        ["pay", "pay", "he, she"],
        ["nyuqanchik", "nyuqanchik", "we (including you)"],
        ["nyuqayku", "nyuqayku", "we (excluding you)"],
        ["qankuna", "qankuna", "you (plural)"],
        ["paykuna", "paykuna", "they"],
        ["kay", "kay", "this"],
    ],
    "numbers": [
        ["huk", "huk", "one"],
        ["iskay", "iskay", "two"],
        ["kimsa", "kimsa", "three"],
        ["tawa", "tawa", "four"],
        ["pichqa", "pichqa", "five"],
        ["suqta", "suqta", "six"],
        ["qanchis", "qanchis", "seven"],
        ["pusaq", "pusaq", "eight"],
        ["isqun", "isqun", "nine"],
        ["chunka", "chunka", "ten"],
    ],
    "time": [
        ["kunan", "kunan", "now"],
        ["kunan p'unchay", "kunan p'unchay", "today"],
        ["paqarin", "paqarin", "tomorrow"],
        ["qayna p'unchay", "qayna p'unchay", "yesterday"],
        ["tutamanta", "tutamanta", "morning"],
        ["ch'isi", "ch'isi", "evening"],
    ],
    "greetings": [
        ["Allillanchu.", "Allillanchu.", "Hello - are you well?"],
        ["Allinllam.", "Allinllam.", "I am well."],
        ["Napaykullayki.", "Napaykullayki.", "Greetings to you."],
        ["Allin p'unchay.", "Allin p'unchay.", "Good day."],
        ["Sumaq tuta.", "Sumaq tuta.", "Good night."],
        ["Anay.", "Anay.", "Thank you."],
        ["Allin hamuy.", "Allin hamuy.", "Welcome."],
        ["Tupananchikkama.", "Tupananchikkama.", "Until we meet again."],
    ],
    "grammar_rules": [
        ("Subject-Object-Verb order",
         "The verb comes last: Nyuqa tantata mikhuni (I bread eat = I eat bread). Time and place phrases come early in the sentence."),
        ("Agglutination - suffix chains",
         "Meaning builds by stacking suffixes: wasi (house), wasi-pi (in the house), wasi-yki-pi (in your house), wasi-yki-pi-chu (is it in your house?)."),
        ("Three vowels",
         "Quechua has only a, i, u. Next to the uvular q, i opens toward e and u toward o: qillqa sounds like qellqa."),
        ("Evidential suffixes",
         "Speakers mark how they know things: -mi for witnessed (Rirqami, he went - I saw it), -si for reported (Rirqasi, they say he went), -cha for doubt."),
        ("Inclusive and exclusive we",
         "nyuqanchik is we including you; nyuqayku is we excluding you - a distinction English cannot make."),
        ("Verb person endings",
         "-ni (I), -nki (you), -n (he/she), -nchik (we incl), -yku (we excl), -nkichik (you pl), -nku (they): mikhuni, mikhunki, mikhun."),
        ("Questions with -chu",
         "Add -chu to the questioned word: Allillanchu? (Are you well?), Maypin? becomes Maypinchu? in careful speech."),
        ("No grammatical gender",
         "pay means he, she, or it by context; nouns never change for gender - one less thing to memorize."),
    ],
    "themes": [
        ("At Home and with Family", [
            ["Nyuqa wasipi kachkani.", "Nyuqa wasipi kachkani.", "I am at home."],
            ["Wasiyki hatunmi.", "Wasiyki hatunmi.", "Your house is big."],
            ["Anay, tatay.", "Anay, tatay.", "Thank you, father."],
            ["Mamayta munani.", "Mamayta munani.", "I love my mother."],
            ["Mikhurqani.", "Mikhurqani.", "I ate."],
            ["Paykuna tiyachkanku wasipi.", "Paykuna tiyachkanku wasipi.", "They are sitting in the house."],
        ]),
        ("Food and Cooking", [
            ["Mikhusunchik!", "Mikhusunchik!", "Let us eat!"],
            ["Mikhuna sumaqmi.", "Mikhuna sumaqmi.", "The food is delicious."],
            ["Tantata munani.", "Tantata munani.", "I want bread."],
            ["Yakuta upyay.", "Yakuta upyay.", "Drink water."],
            ["Mamay yanukuchkan.", "Mamay yanukuchkan.", "Mother is cooking."],
            ["Saksasqani.", "Saksasqani.", "I am full."],
        ]),
        ("Travel and Directions", [
            ["Llaqtaman rishani.", "Llaqtaman rishani.", "I am going to town."],
            ["Maypi nyan?", "Maypi nyan?", "Where is the road?"],
            ["Karullachu?", "Karullachu?", "Is it still far?"],
            ["Panyaman riy.", "Panyaman riy.", "Go to the right."],
            ["Kaypin samana.", "Kaypin samana.", "Here is the resting place."],
            ["Hayk'an qullqi?", "Hayk'an qullqi?", "How much money?"],
        ]),
        ("Work and School", [
            ["Oficinapi llank'ani.", "Oficinapi llank'ani.", "I work in an office."],
            ["Yachachkanku yachaywasipi.", "Yachachkanku yachaywasipi.", "They are studying at school."],
            ["Yachachiq allinmi.", "Yachachiq allinmi.", "The teacher is good."],
            ["Imapin llank'anki?", "Imapin llank'anki?", "Where do you work?"],
            ["Kunan llank'anayman rishani.", "Kunan llank'anayman rishani.", "Now I am going to my work."],
            ["Tukurqunnan.", "Tukurqunnan.", "It is finished."],
        ]),
        ("Health and the Body", [
            ["Umay nanan.", "Umay nanan.", "My head hurts."],
            ["Hampiqman rishani.", "Hampiqman rishani.", "I am going to the doctor."],
            ["Unqusqani.", "Unqusqani.", "I am sick."],
            ["Hampita upyay.", "Hampita upyay.", "Drink the medicine."],
            ["Kunanqa allinnyan kachkani.", "Kunanqa allinnyan kachkani.", "Now I am better."],
            ["Samay.", "Samay.", "Rest."],
        ]),
        ("Emotions and Feelings", [
            ["Kusisqani.", "Kusisqani.", "I am happy."],
            ["Llakisqani.", "Llakisqani.", "I am sad."],
            ["Phinyasqani.", "Phinyasqani.", "I am angry."],
            ["Manchasqani.", "Manchasqani.", "I am afraid."],
            ["Munakuyki.", "Munakuyki.", "I love you."],
            ["Asichkani.", "Asichkani.", "I am laughing."],
        ]),
        ("Nature and Weather", [
            ["Kunan p'unchayqa ruphaymi.", "Kunan p'unchayqa ruphaymi.", "Today it is hot."],
            ["Parachkan.", "Parachkan.", "It is raining."],
            ["Wayraqa sinchimi.", "Wayraqa sinchimi.", "The wind is strong."],
            ["Killaqa sumaqmi.", "Killaqa sumaqmi.", "The moon is beautiful."],
            ["Ch'askakuna achkhami.", "Ch'askakuna achkhami.", "There are many stars."],
            ["Yakuqa chirimi.", "Yakuqa chirimi.", "The water is cold."],
        ]),
        ("Shopping and Money", [
            ["Hayk'an kay?", "Hayk'an kay?", "How much is this?"],
            ["Ancha chaniyuq.", "Ancha chaniyuq.", "It is too expensive."],
            ["Chaninta pisiyachiy.", "Chaninta pisiyachiy.", "Lower its price."],
            ["Kayta rantisaq.", "Kayta rantisaq.", "I will buy this."],
            ["Kutichiy kanchu?", "Kutichiy kanchu?", "Is there change?"],
            ["Qhatu karuchu?", "Qhatu karuchu?", "Is the market far?"],
        ]),
        ("Friendship and Social Life", [
            ["Payqa masiy.", "Payqa masiy.", "He is my friend."],
            ["Kuska purisunchik.", "Kuska purisunchik.", "Let us walk together."],
            ["Wasiyman hamuy.", "Wasiyman hamuy.", "Come to my house."],
            ["Paqarin raymita ruwasunchik.", "Paqarin raymita ruwasunchik.", "Tomorrow we will hold a feast."],
            ["Takisunchik.", "Takisunchik.", "Let us sing."],
            ["Kusisunchik llapanchik.", "Kusisunchik llapanchik.", "Let us all rejoice."],
        ]),
        ("Technology and Communication", [
            ["Paqarin qamta waqyasaq.", "Paqarin qamta waqyasaq.", "Tomorrow I will call you."],
            ["Kaypiqa mana senyal kanchu.", "Kaypiqa mana senyal kanchu.", "There is no signal here."],
            ["Qillqamuy.", "Qillqamuy.", "Text me."],
            ["Internetpi rikurqani.", "Internetpi rikurqani.", "I saw it on the internet."],
            ["Kunanqa internetpi kachkani.", "Kunanqa internetpi kachkani.", "Now I am on the internet."],
            ["Celularniykita cargay.", "Celularniykita cargay.", "Charge your cellphone."],
        ]),
    ],
    "tenses": [
        ["Qayna p'unchay mikhurqani.", "Qayna p'unchay mikhurqani.", "I ate yesterday."],
        ["Kunan mikhuchkani.", "Kunan mikhuchkani.", "I am eating now."],
        ["Paqarin mikhusaq.", "Paqarin mikhusaq.", "I will eat tomorrow."],
        ["Pay llaqtaman rirqa.", "Pay llaqtaman rirqa.", "He went to town."],
        ["Pay llaqtaman richkan.", "Pay llaqtaman richkan.", "He is going to town."],
        ["Pay paqarin llaqtaman rinqa.", "Pay paqarin llaqtaman rinqa.", "He will go to town tomorrow."],
    ],
    "questions": [
        ["Imataq sutiyki? - Sutiyqa Mariami.", "Imataq sutiyki? - Sutiyqa Mariami.", "What is your name? - My name is Maria."],
        ["Maymantataq kanki? - Qusqumantan kani.", "Maymantataq kanki? - Qusqumantan kani.", "Where are you from? - I am from Cusco."],
        ["Hayk'a watayuq kanki? - Iskay chunka watayuq kani.", "Hayk'a watayuq kanki? - Iskay chunka watayuq kani.", "How old are you? - I am twenty."],
        ["Hayk'aq pachachu? - Kimsa pacham.", "Hayk'aq pachachu? - Kimsa pacham.", "What time is it? - It is three o'clock."],
        ["Maymanmi rishanki? - Llaqtamanmi rishani.", "Maymanmi rishanki? - Llaqtamanmi rishani.", "Where are you going? - I am going to town."],
        ["Cafetacha munankichu? - Ari, munani.", "Cafetacha munankichu? - Ari, munani.", "Do you want coffee? - Yes, I want some."],
    ],
    "commands": [
        ["Kayman hamuy.", "Kayman hamuy.", "Come here."],
        ["Tiyaykuy.", "Tiyaykuy.", "Sit down."],
        ["Mikhuy.", "Mikhuy.", "Eat."],
        ["Yakuta upyay.", "Yakuta upyay.", "Drink the water."],
        ["Samay.", "Samay.", "Rest."],
        ["Wasiykiman kutiy.", "Wasiykiman kutiy.", "Go home."],
    ],
    "descriptions": [
        ["Payqa sumaqmi.", "Payqa sumaqmi.", "She is beautiful."],
        ["Wasiyki hatunmi.", "Wasiyki hatunmi.", "Your house is tall."],
        ["Allquqa uchuymi.", "Allquqa uchuymi.", "The dog is small."],
        ["Juanqa allin runami.", "Juanqa allin runami.", "Juan is a good person."],
        ["Sach'akunaqa achkha raphiyuqmi.", "Sach'akunaqa achkha raphiyuqmi.", "The trees have many leaves."],
        ["Chakrakuna hatunmi.", "Chakrakuna hatunmi.", "The fields are wide."],
    ],
    "stories": [
        ("Irqiwan Allquwan", [
            ["Huk irqi karqa.", "Huk irqi karqa.", "There was a child."],
            ["Yuraq allqun karqa.", "Yuraq allqun karqa.", "He had a white dog."],
            ["Sapa p'unchay chakrapi pukllarqanku.", "Sapa p'unchay chakrapi pukllarqanku.", "Every day they played in the field."],
            ["Huk p'unchay allqu chinkarqa.", "Huk p'unchay allqu chinkarqa.", "One day the dog got lost."],
            ["Irqiqa kusikurqa allqunta tarispa.", "Irqiqa kusikurqa allqunta tarispa.", "The child was happy finding his dog."],
        ]),
        ("Chakramayu", [
            ["Pabluqa chakramayun.", "Pabluqa chakramayun.", "Pablo is a farmer."],
            ["Tutamanta chakraman rin.", "Tutamanta chakraman rin.", "He goes to the field in the morning."],
            ["Saratatan tarpun.", "Saratatan tarpun.", "He plants corn."],
            ["Paray timpuqa paran.", "Paray timpuqa paran.", "In the rainy season it rains."],
            ["Achkha mikhunata pallan.", "Achkha mikhunata pallan.", "He gathers much food."],
        ]),
        ("Musuq Yachaywasi", [
            ["Llaqtaqpi musuq yachaywasin kan.", "Llaqtaqpi musuq yachaywasin kan.", "There is a new school in our town."],
            ["Yachaqkuna kusisqan kanku.", "Yachaqkuna kusisqan kanku.", "The students are happy."],
            ["Musuq yachachiq allinmi.", "Musuq yachachiq allinmi.", "The new teacher is good."],
            ["Runasimita kastillanotapas yachachkanku.", "Runasimita kastillanotapas yachachkanku.", "They are learning Quechua and Spanish too."],
            ["Llaqtaqa qhipa p'unchayta suyachkan.", "Llaqtaqa qhipa p'unchayta suyachkan.", "The town awaits the future."],
        ]),
    ],
    "idioms": [
        ["Ama sua, ama llulla, ama qilla.", "Ama sua, ama llulla, ama qilla.", "Do not steal, do not lie, do not be lazy - the ancient moral code."],
        ["Llank'aq makiqa mana yarqanchu.", "Llank'aq makiqa mana yarqanchu.", "The working hand never goes hungry."],
        ["Yachayqa qullqimanta aswan chaniyuqmi.", "Yachayqa qullqimanta aswan chaniyuqmi.", "Knowledge is worth more than money."],
        ["Allin simiqa allin sunqumanta paqarimun.", "Allin simiqa allin sunqumanta paqarimun.", "Good words grow from a good heart."],
        ["Uchuy yakuqa hatun mayuman tukun.", "Uchuy yakuqa hatun mayuman tukun.", "A small stream becomes a great river."],
        ["Sapa tuta qhipanpiqa p'unchaymi hamun.", "Sapa tuta qhipanpiqa p'unchaymi hamun.", "After every night, day comes."],
        ["Runamasiykiwan allinta kawsay.", "Runamasiykiwan allinta kawsay.", "Live well with your fellow people."],
        ["Kallpawan llamk'aspaqa tukuy ima atipanchikmi.", "Kallpawan llamk'aspaqa tukuy ima atipanchikmi.", "Working with strength, we can do everything."],
    ],
    "registers": [
        ["Allillanchu, taytay.", "(respectful) Allillanchu, taytay.", "Hello, sir."],
        ["Imaynallan kashanki?", "(polite) Imaynallan kashanki?", "How are you?"],
        ["Ama hina kaychu, manyakuyki.", "(formal request) Ama hina kaychu, manyakuyki.", "Please, I ask you."],
        ["Pampachaway.", "Pampachaway.", "(formal) Forgive me."],
        ["Anaykullayki.", "Anaykullayki.", "Thank you kindly."],
        ["Tupananchikkama, wawqey.", "(warm) Tupananchikkama, wawqey.", "Until we meet again, my brother."],
    ],
    "compound": [
        ["Mikhuyta munani, ichaqa saksasqanyan kani.", "Mikhuyta munani, ichaqa saksasqanyan kani.", "I want to eat, but I am already full."],
        ["Llaqtaman rishani, imaraykuchus rantisaq mikhunata.", "Llaqtaman rishani, imaraykuchus rantisaq mikhunata.", "I am going to town because I will buy food."],
        ["Paraptinqa wasipi qhipakusaq.", "Paraptinqa wasipi qhipakusaq.", "If it rains, I will stay home."],
        ["Pay hamuqtin kusikurqaniku.", "Pay hamuqtin kusikurqaniku.", "When he came, we were happy."],
        ["Sumaqta takin, sumaqta tusun.", "Sumaqta takin, sumaqta tusun.", "She sings beautifully, she dances beautifully."],
        ["Saykusqaywanpas llank'achkaniraqmi.", "Saykusqaywanpas llank'achkaniraqmi.", "Although I am tired, I am still working."],
    ],
    "conversations": [
        ("Qhatupi", [
            ["Maria", "Allillanchu, qhatuq runa.", "Allillanchu, qhatuq runa.", "Hello, market seller."],
            ["Juana", "Allillanmi. Imatataq munanki?", "Allillanmi. Imatataq munanki?", "I am well. What do you want?"],
            ["Maria", "Hayk'an huk kilu tumatitaq?", "Hayk'an huk kilu tumatitaq?", "How much is a kilo of tomatoes?"],
            ["Juana", "Iskay chunka sulistaq kilun.", "Iskay chunka sulistaq kilun.", "Twenty soles a kilo."],
            ["Maria", "Ancha chaniyuq. Chunka pichqayuqchu?", "Ancha chaniyuq. Chunka pichqayuqchu?", "Too expensive. Fifteen?"],
            ["Juana", "Ari, chunka pichqapi. Anay!", "Ari, chunka pichqapi. Anay!", "Yes, for fifteen. Thanks!"],
        ]),
        ("Masiwan Tupay", [
            ["Ana", "Juan! Unay watamanta!", "Juan! Unay watamanta!", "Juan! It has been years!"],
            ["Juan", "Ana! Imaynallan kashanki?", "Ana! Imaynallan kashanki?", "Ana! How are you?"],
            ["Ana", "Allinllan. Maymantaq rishanki?", "Allinllan. Maymantaq rishanki?", "Well. Where are you going?"],
            ["Juan", "Yachaywasimanmi rishani. Qanri?", "Yachaywasimanmi rishani. Qanri?", "I am going to school. And you?"],
            ["Ana", "Llaqtamanmi rishani. Tupananchikkama!", "Llaqtamanmi rishani. Tupananchikkama!", "I am going to town. Until we meet!"],
            ["Juan", "Ari! Allinta puriy!", "Ari! Allinta puriy!", "Yes! Walk well!"],
        ]),
        ("Sasachakuyta Allichay", [
            ["Pedro", "Celularniyqa sasachakuyniyuqmi.", "Celularniyqa sasachakuyniyuqmi.", "My phone has a problem."],
            ["Rosa", "Ima sasachakuy?", "Ima sasachakuy?", "What problem?"],
            ["Pedro", "Mana senyalniyuqchu.", "Mana senyalniyuqchu.", "It has no signal."],
            ["Rosa", "Musuqmanta hap'iy.", "Musuqmanta hap'iy.", "Turn it on anew."],
            ["Pedro", "Musuqmanta hap'irqani, ichaqa manan kanchu.", "Musuqmanta hap'irqani, ichaqa manan kanchu.", "I restarted it, but there is still none."],
            ["Rosa", "Paqarin allichiqman risunchik.", "Paqarin allichiqman risunchik.", "Tomorrow let us go to the repairer."],
        ]),
    ],
    "citations": [
        "Parker GJ. Ayacucho Quechua Grammar and Dictionary. The Hague: Mouton; 1969.",
        "Cerron-Palomino R. Linguistica quechua. Cusco: CBC; 1987.",
        "Soto Ruiz C. Quechua: Manual de Ensenanza. Lima: IEP; 1976.",
        "ISO 639-1:2002 qu; ISO 639-3:2007 que (macrolanguage).",
    ],
}
