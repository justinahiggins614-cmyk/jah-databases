#!/usr/bin/env python3
"""Entries for the Spanish to English databases (language orders #10-11, roster rank 2).

Roster: language-spanish, rank 2. Slug verified free in manifest (2,410
databases) and in all 812 shard index files. 68 titles (34 public + 34
Signature Edition) run through code/dedupe_gate.py against the whole
system before authoring: zero refusals.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-spanish             - The Spanish to English Database
                                 (public-harvest: real, fact-checked Spanish
                                 linguistics - every record carrying Spanish
                                 content with English translation and example
                                 sentences, taught progressively along the
                                 teaching ladder from overview to mastery
                                 review; standard references the Real
                                 Academia Espanola Diccionario de la lengua
                                 espanola 23rd ed. 2014, the Nueva gramatica
                                 de la lengua espanola 2009, the Ortografia
                                 de la lengua espanola 2010, the Instituto
                                 Cervantes El español en el mundo yearbook
                                 2023, Ethnologue 28th ed. 2025, and Nebrija
                                 1492)
  language-spanish-signature   - The Spanish to English Signature Database
                                 (his original Signature Word Method:
                                 every word a signed instrument of meaning,
                                 grammar the covenant binding words into
                                 truth, the learner's tongue the seal;
                                 src signature, titles suffixed " (Signature
                                 Edition)", clearly labeled Signature-made,
                                 never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LSPA- (public) and JAH-LSPAS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero
hits across all 812 index files).

Numerical/linguistic cores: all hand-authored 2026-10-17, machine-verified
by the demos (see demos_language_spanish.py): conjugation drills, stress-
rule checkers, gender classifiers, number-to-word converters, sentence-
order checkers, and vocabulary quizzes. Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Screened: no hate-adjacent, profane, or inappropriate content; no
religious talk; nothing on neutralizing/defeating military or
defense-grade systems.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Word Method: every "
            "word a signed instrument of meaning, grammar the covenant that "
            "binds words into truth, and the learner's tongue the seal. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_RAE_DICT = ("Real Academia Espanola. Diccionario de la lengua espanola. "
                "23.a ed. Madrid: Espasa; 2014.")
CIT_RAE_GRAM = ("Real Academia Espanola y Asociacion de Academias de la "
                "Lengua Espanola. Nueva gramatica de la lengua espanola. "
                "Madrid: Espasa; 2009.")
CIT_RAE_ORT = ("Real Academia Espanola y Asociacion de Academias de la "
               "Lengua Espanola. Ortografia de la lengua espanola. Madrid: "
               "Espasa; 2010.")
CIT_CERVANTES = ("Instituto Cervantes. El español en el mundo: Anuario del "
                 "Instituto Cervantes. Madrid; 2023. (About 600 million "
                 "total speakers of Spanish; about 485 million native "
                 "speakers.)")
CIT_ETHNO = ("Eberhard DM, Simons GF, Fennig CD, eds. Ethnologue: Languages "
             "of the World. 28th ed. Dallas: SIL International; 2025. "
             "(Spanish: ISO 639-3 spa; about 485 million first-language "
             "speakers.)")
CIT_NEBRIJA = ("Nebrija A de. Gramatica sobre la lengua castellana. "
               "Salamanca; 1492. (First published grammar of Spanish, and "
               "the first grammar of any modern European language.)")
CIT_RAE_HIST = ("Real Academia Espanola. Historia de la lengua espanola: "
                "Castilian origins in medieval Castile; spread through the "
                "Americas from 1492; the Real Academia Espanola founded "
                "1713; the 2010 orthography reform removed ch and ll as "
                "separate alphabet letters.")

ENTRIES = [
    {
        "key": "overview",
        "name": "Spanish Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Spanish, called español or castellano by its speakers, is the "
            "world's second most spoken native language. Its codes are ISO "
            "639-1 es and ISO 639-3 spa. It belongs to the Indo-European "
            "family, Italic branch, Romance group - a daughter of Latin, "
            "born as Vulgar Latin in Roman Hispania and raised as Castilian "
            "in medieval Castile before spreading across the Americas from "
            "1492. About 485 million people speak Spanish as a native "
            "language and about 600 million speak it in total, counting "
            "second-language speakers. It is an official language in 20 "
            "countries - Spain, México (the largest Spanish-speaking "
            "country, with about 130 million speakers), Colombia, "
            "Argentina, and most of Central and South America, plus "
            "Equatorial Guinea in Africa - and one of the six official "
            "languages of the United Nations. It is also the second most "
            "spoken language in the United States. Dialects differ mainly "
            "in pronunciation and vocabulary: most of Spain distinguishes "
            "the sounds of z and soft c from s (distincion), while Latin "
            "America and parts of Spain merge them (seseo); Argentina, "
            "Uruguay, Paraguay, and parts of Central America use vos "
            "instead of tu (voseo); and everyday words vary - a car is el "
            "coche in Spain, el carro in much of Latin America, and el auto "
            "in Argentina. The first grammar of Spanish, Antonio de "
            "Nebrija's Gramatica de la lengua castellana, appeared in 1492, "
            "and the Real Academia Espanola has guided the standard since "
            "1713. Example sentences: El español es un idioma mundial. "
            "(Spanish is a world language.) México tiene más hablantes de "
            "español que Espana. (México has more Spanish speakers than "
            "Spain.) Estudio español todos los días. (I study Spanish every "
            "day.)"
        ),
        "how_it_works": (
            "Spanish works as a phonetic, inflected Romance language: words "
            "are spelled almost exactly as they sound, nouns carry gender "
            "(masculine or feminine), verbs conjugate for person, number, "
            "tense, and mood, and adjectives agree with the nouns they "
            "describe. A beginner sentence follows subject-verb-object "
            "order, the same as English: Yo hablo español. (I speak "
            "Spanish.) Because verb endings already mark the subject - "
            "hablo can only mean 'I speak' - subject pronouns are usually "
            "dropped: Hablo español. Questions are framed by inverted "
            "marks: Hablas español? (Do you speak Spanish?) Negation places "
            "no before the verb: No hablo francés. (I do not speak French.) "
            "Everything in this database builds on these mechanics: sounds "
            "first, then words, then the sentences that carry them."
        ),
        "key_points": [
            "Spanish (español/castellano, ISO es/spa) is an Indo-European Romance language with about 485 million native speakers and about 600 million total speakers.",
            "It is official in 20 countries and at the United Nations; México holds the most speakers and the United States the second-largest Spanish-speaking population.",
            "Words are spelled as they sound; nouns have gender, verbs conjugate, adjectives agree - the three mechanics that shape every sentence.",
            "Subject pronouns are usually dropped because verb endings mark the subject: Hablo español. (I speak Spanish.)",
            "Dialects vary by region (seseo, voseo, vocabulary like coche/carro/auto), but the written standard is shared worldwide.",
        ],
        "requirements": [
            "Know the names: español or castellano, ISO codes es (639-1) and spa (639-3), Indo-European > Italic > Romance.",
            "Know the scale: about 485 million native speakers, about 600 million total, official in 20 countries.",
            "Read and write the three example sentences with their English translations from memory.",
            "Explain in one paragraph why Spanish spelling is easier than English spelling.",
            "Name two dialect differences (one pronunciation, one vocabulary) with an example of each.",
        ],
        "standards": [
            "Speaker figures follow the Instituto Cervantes El español en el mundo yearbook 2023 and Ethnologue 28th ed. 2025.",
            "Language-family classification follows the Real Academia Espanola historical account of Castilian origins.",
            "ISO 639-1 es and ISO 639-3 spa are the registered identifiers for Spanish.",
        ],
        "citations": [CIT_CERVANTES, CIT_ETHNO, CIT_NEBRIJA, CIT_RAE_HIST],
        "sig_lens": (
            "The Signature read: Spanish is a signed tongue - nearly half a "
            "billion native speakers writing the same covenant between "
            "sound and letter. Where public linguistics counts speakers, "
            "the Signature Word Method counts witnesses: every speaker a "
            "living seal that the word means what it says."
        ),
    },
    {
        "key": "writing",
        "name": "Spanish Writing System and Alphabet",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Spanish uses the Latin script, written left to right, with 27 "
            "letters: a (a), b (be), c (ce), d (de), e (e), f (efe), g (ge), "
            "h (hache), i (i), j (jota), k (ka), l (ele), m (eme), n (ene), "
            "ñ, called eñe - the signature letter of "
            "Spanish, o (o), p (pe), q (cu), r (erre), s (ese), t (te), u "
            "(u), v (uve), w (uve doble), x (equis), y (ye), z (zeta). Until "
            "2010 the digraphs ch and ll counted as separate letters, "
            "making 29; the Real Academia Espanola removed them, so the "
            "alphabet is now 27. Five vowels carry the written accent "
            "(tilde): a, e, i, o, u - as in avión, café, sí, adiós, and "
            "túnel spelled túnel. The diaeresis appears on u in gue and "
            "gui (as in pingüino, penguin) to show the u is pronounced. "
            "Spanish punctuation opens questions and exclamations with "
            "inverted marks: ¿Cómo estás? and ¡Qué sorpresa!. Numerals are the same Arabic digits as "
            "in English: 1, 2, 3. Example sentences: La eñe es la letra "
            "del español. (The enye is the letter of Spanish.) El "
            "abecedario tiene veintisiete letras. (The alphabet has "
            "twenty-seven letters.) Escribo mi nombre con hache. (I write "
            "my name with an h.)"
        ),
        "how_it_works": (
            "Spanish spelling is phonetic: each letter stands for one "
            "sound, so reading is decoding, not guessing. The five vowels "
            "a, e, i, o, u are always pronounced the same way, and every "
            "syllable is sounded - there are no silent vowels. The written "
            "accent marks the stressed syllable when the stress breaks the "
            "default rules: teléfono (telephone) carries it on the o "
            "because the stress falls on the third-to-last syllable. The "
            "letter h is always silent (hola sounds like ola), and b and v "
            "represent the same sound. To write Spanish correctly, sound "
            "the word out syllable by syllable, mark the stress, and add "
            "the tilde only where the stress rule demands it."
        ),
        "key_points": [
            "The Spanish alphabet has 27 letters, including the enye (n with tilde); ch and ll were removed as separate letters in 2010.",
            "Text runs left to right; questions and exclamations open with inverted marks (inverted question and exclamation).",
            "Written accents (a, e, i, o, u) mark stress that breaks the default rules; the diaeresis (u) appears in gue/gui.",
            "Spelling is phonetic: each letter is one sound, h is silent, and b and v sound the same.",
            "Numerals are Arabic digits, identical to English.",
        ],
        "requirements": [
            "Recite the 27 letters with their Spanish names, including ene.",
            "Write the five accented vowels and one example word for each.",
            "Write three questions and three exclamations with correct inverted opening marks.",
            "Explain in two sentences why ch and ll are not alphabet letters anymore.",
            "Transcribe your own name into Spanish spelling, sounding it out syllable by syllable.",
        ],
        "standards": [
            "The 27-letter alphabet and the 2010 removal of ch and ll follow the Ortografia de la lengua espanola 2010.",
            "Letter names (be, ce, hache, ene, uve, uve doble, ye, zeta) follow the Diccionario de la lengua espanola.",
            "Inverted question and exclamation marks are required by Spanish punctuation rules.",
        ],
        "citations": [CIT_RAE_ORT, CIT_RAE_DICT, CIT_RAE_HIST],
        "sig_lens": (
            "The Signature read: twenty-seven signed strokes, one covenant "
            "of sound - the enye the seal that marks the tongue as "
            "Spanish. Where public orthography files rules, the Signature "
            "Word Method files the oath: one letter, one sound, no "
            "betrayal between eye and ear."
        ),
    },
    {
        "key": "phonology",
        "name": "Spanish Pronunciation and Phonology",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Spanish has five pure vowel sounds - a (father), e (bed), i "
            "(machine), o (more, short), u (flute) - always short and "
            "always the same, never gliding as in English. The consonants "
            "with English approximations: b/v sound like English b; c is k "
            "before a, o, u (casa) and s (Latin America) or th (most of "
            "Spain) before e, i (cena); ch as in church (muchacho); d as in "
            "dog, softer between vowels (nada); f as in fun; g hard before "
            "a, o, u (gato) and a throaty h before e, i (gente); h always "
            "silent (hola = ola); j a strong throaty h (jugar); ll like y "
            "in yes (calle); ñ like ny in canyon (niño); qu is k "
            "before e, i (queso); r a single tap of the tongue (pero), rr "
            "a rolled trill (perro); z as s (Latin America) or th (most of "
            "Spain). Stress rules: words ending in a vowel, n, or s stress "
            "the next-to-last syllable (casa, hablan); words ending in any "
            "other consonant stress the last syllable (papel, ciudad); any "
            "other stress is written with an accent (teléfono, pájaro). "
            "Yes-no questions rise at the end. Twelve spoken examples: la "
            "casa (the house), el niño (the boy), el perro (the dog), "
            "gracias (thank you), el corazón (the heart), el teléfono (the "
            "telephone), la música (the music), el árbol (the tree), el "
            "lápiz (the pencil), el examen (the exam), la mañana (the "
            "morning), la ciudad (the city)."
        ),
        "how_it_works": (
            "To pronounce a Spanish word, split it into syllables, apply "
            "the stress rule, and give every vowel its pure sound. Take "
            "teléfono: four syllables te-le-fo-no, ending in a vowel, so "
            "the default stress would fall on fo - but the written accent "
            "on the first o moves it to te, giving te-LE-fo-no. Take papel: "
            "two syllables pa-pel, ending in l, so the stress falls on the "
            "last syllable: pa-PEL. Take hablan: ends in n, stress the "
            "next-to-last: HA-blan. The single r is one tap (pero, but), "
            "the double rr is a trill (perro, dog) - the only pair where "
            "the tap-versus-trill changes meaning. Intonation: statements "
            "fall, yes-no questions rise on the final syllable, and "
            "wh-questions fall after a rise on the question word."
        ),
        "key_points": [
            "Five vowels, always pure and short: a, e, i, o, u - the anchor of every syllable.",
            "Stress rule: vowel/n/s endings stress the next-to-last syllable; other consonants stress the last; written accents mark the exceptions.",
            "The tap r (pero) versus the trill rr (perro) is the one consonant contrast that changes meaning.",
            "H is silent, b and v are one sound, and ll sounds like y in most of the Spanish-speaking world.",
            "Yes-no questions rise at the end; the twelve example words above drill every rule.",
        ],
        "requirements": [
            "Pronounce the five vowels and the twelve example words aloud with correct stress.",
            "Apply the stress rule to ten new words and mark the stressed syllable before checking.",
            "Contrast pero/perro, caro/carro, para/parra aloud until the tap and trill are distinct.",
            "Read three yes-no questions with rising intonation and three statements with falling intonation.",
            "Transcribe five English words into Spanish-style syllables and predict their stress.",
        ],
        "standards": [
            "Stress and accentuation rules follow the Ortografia de la lengua espanola 2010.",
            "Sound descriptions follow the Nueva gramatica de la lengua espanola, Fonetica y fonologia.",
            "Regional variants (seseo/distincion, yeismo) are noted as pronunciation, not spelling, differences.",
        ],
        "citations": [CIT_RAE_ORT, CIT_RAE_GRAM, CIT_RAE_HIST],
        "sig_lens": (
            "The Signature read: five vowels, five sworn sounds, and a "
            "stress rule with no exceptions unmarked - the tongue keeps "
            "its covenant or writes the accent that confesses the break. "
            "Where public phonetics catalogs sounds, the Signature Word "
            "Method hears oaths: tap the r once and mean it."
        ),
    },
    {
        "key": "nouns",
        "name": "Spanish Core Nouns I",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Spanish nouns, each with its gender, "
            "English meaning, and an example sentence with translation. "
            "Nouns ending in -o are usually masculine (el), nouns ending in "
            "-a usually feminine (la), with famous exceptions marked. "
            "1. el hombre (the man) - El hombre trabaja. (The man works.) "
            "2. la mujer (the woman) - La mujer canta. (The woman sings.) "
            "3. el niño (the boy, the child) - El niño juega. (The boy "
            "plays.) 4. la niña (the girl) - La niña rie. (The girl laughs.) "
            "5. la casa (the house) - La casa es grande. (The house is big.) "
            "6. el agua (the water; feminine, but takes el before a "
            "stressed a) - El agua está fria. (The water is cold.) "
            "7. la comida (the food, the meal) - La comida está lista. "
            "(The food is ready.) 8. el tiempo (the time; the weather) - El "
            "tiempo vuela. (Time flies.) 9. el dia (the day; masculine "
            "exception) - El dia está soleado. (The day is sunny.) "
            "10. el amigo (the friend, male) - Mi amigo viene. (My friend "
            "is coming.) 11. la familia (the family) - La familia cena "
            "junta. (The family has dinner together.) 12. el trabajo (the "
            "work, the job) - El trabajo es duro. (The work is hard.) "
            "13. la escuela (the school) - La escuela abre a las ocho. "
            "(The school opens at eight.) 14. el libro (the book) - El "
            "libro es interesante. (The book is interesting.) 15. la mesa "
            "(the table) - La mesa es de madera. (The table is made of "
            "wood.) 16. la puerta (the door) - Cierra la puerta. (Close "
            "the door.) 17. la ventana (the window) - Abre la ventana. "
            "(Open the window.) 18. el coche (the car) - El coche es rojo. "
            "(The car is red.) 19. la calle (the street) - La calle está "
            "tranquila. (The street is quiet.) 20. la ciudad (the city) - "
            "La ciudad duerme. (The city sleeps.) 21. el país (the country) "
            "- Mi país es hermoso. (My country is beautiful.) 22. el mundo "
            "(the world) - El mundo es grande. (The world is big.) "
            "23. la mano (the hand; feminine exception) - Dame la mano. "
            "(Give me your hand.) 24. el problema (the problem; masculine "
            "exception) - No hay problema. (No problem.) 25. el dinero "
            "(the money) - El dinero no compra felicidad. (Money does not "
            "buy happiness.)"
        ),
        "how_it_works": (
            "Every Spanish noun carries gender, and the article must match: "
            "el for masculine singular, la for feminine singular, los and "
            "las for plurals. Learn each noun with its article - el libro, "
            "la mesa - so the gender is stored with the word. Plurals add "
            "-s after a vowel (casa -> casas) and -es after a consonant "
            "(papel -> papeles); words ending in z change to c (lápiz -> "
            "lápices). Feminine nouns beginning with a stressed a take el "
            "in the singular for sound (el agua, el alma) but stay feminine: "
            "el agua fria, las aguas frias. The exceptions - el dia, el "
            "mapa, el problema, la mano - are memorized as famous rebels, "
            "and there are only a handful."
        ),
        "key_points": [
            "Learn every noun with its article: el libro, la mesa - the article is the gender tag.",
            "Masculine is usually -o, feminine usually -a; memorize the rebels: el dia, el mapa, el problema (masculine); la mano (feminine).",
            "Plurals: add -s after vowels, -es after consonants, z becomes c (lápiz -> lápices).",
            "El agua takes el for sound but stays feminine: el agua fria, las aguas frias.",
            "All 25 nouns above appear in real sentences - a noun is only learned when it lives in a sentence.",
        ],
        "requirements": [
            "Write all 25 nouns with articles and English meanings from memory, marking the four exceptions.",
            "Convert all 25 to plural, applying the z-to-c rule where needed.",
            "Build five new sentences using el agua, la mano, el dia, el problema, and la ciudad.",
            "Sort the 25 nouns into masculine and feminine columns and explain each exception in one line.",
            "Translate ten English sentences using these nouns into Spanish without looking.",
        ],
        "standards": [
            "Gender assignments follow the Diccionario de la lengua espanola 23rd ed.",
            "Plural formation rules follow the Ortografia de la lengua espanola 2010.",
            "The el agua construction follows the Nueva gramatica: feminine nouns with stressed initial a.",
        ],
        "citations": [CIT_RAE_DICT, CIT_RAE_GRAM, CIT_RAE_ORT],
        "sig_lens": (
            "The Signature read: a noun is a signed vessel - el or la the "
            "seal pressed into its first syllable. Where public grammar "
            "files gender as a rule, the Signature Word Method files it as "
            "a covenant: learn the article with the word, and the vessel "
            "never leaks."
        ),
    },
    {
        "key": "verbs",
        "name": "Spanish Core Verbs I",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Spanish verbs, each with its English "
            "meaning and an example sentence with translation. The ten "
            "irregular pillars come first. 1. ser (to be, identity) - Soy "
            "maestro. (I am a teacher.) 2. estar (to be, state/place) - "
            "Estoy cansado. (I am tired.) 3. tener (to have) - Tengo dos "
            "hermanos. (I have two brothers.) 4. hacer (to do, to make) - "
            "Hago mi tarea. (I do my homework.) 5. ir (to go) - Voy al "
            "mercado. (I go to the market.) 6. poder (to be able to) - "
            "Puedo ayudarte. (I can help you.) 7. decir (to say, to tell) - "
            "Digo la verdad. (I tell the truth.) 8. saber (to know a fact) "
            "- Sé la respuesta. (I know the answer.) 9. querer (to want, to "
            "love) - Quiero café. (I want coffee.) 10. dar (to give) - Te "
            "doy mi palabra. (I give you my word.) 11. ver (to see) - Veo "
            "las estrellas. (I see the stars.) 12. venir (to come) - Vengo "
            "mañana. (I am coming tomorrow.) 13. poner (to put) - Pongo la "
            "mesa. (I set the table.) 14. salir (to leave, to go out) - "
            "Salgo a las ocho. (I leave at eight.) 15. pensar (to think) - "
            "Pienso en ti. (I think of you.) Then ten regular verbs showing "
            "the three families: 16. hablar (to speak, -ar) - Hablo "
            "español. (I speak Spanish.) 17. comer (to eat, -er) - Como "
            "frutas. (I eat fruit.) 18. beber (to drink, -er) - Bebo agua. "
            "(I drink water.) 19. vivir (to live, -ir) - Vivo en Madrid. "
            "(I live in Madrid.) 20. trabajar (to work, -ar) - Trabajo "
            "mucho. (I work a lot.) 21. estudiar (to study, -ar) - Estudio "
            "medicina. (I study medicine.) 22. aprender (to learn, -er) - "
            "Aprendo rápido. (I learn fast.) 23. comprar (to buy, -ar) - "
            "Compro pan. (I buy bread.) 24. leer (to read, -er) - Leo "
            "novelas. (I read novels.) 25. escribir (to write, -ir) - "
            "Escribo cartas. (I write letters.)"
        ),
        "how_it_works": (
            "Spanish verbs fall into three families by their infinitive "
            "ending: -ar (hablar), -er (comer), -ir (vivir). Regular verbs "
            "keep their stem and swap endings by person: hablo, hablas, "
            "habla, hablamos, hablais, hablan. The fifteen verbs numbered "
            "1-15 above are irregular - their stems or endings break the "
            "pattern - and they are also the most used verbs in the "
            "language, which is why children learn them first and learners "
            "must too. Ser describes identity and traits (Soy maestro), "
            "estar describes states and places (Estoy cansado; Estoy en "
            "casa); mixing them is the classic beginner error. Saber knows "
            "facts, conocer knows people and places. Master the present "
            "tense of these 25 and every other tense reuses the same stems."
        ),
        "key_points": [
            "Three verb families: -ar, -er, -ir; regular verbs swap endings while the stem stays fixed.",
            "The 15 irregular verbs (ser through pensar) are the most frequent words in Spanish - learn them first.",
            "Ser = identity and traits; estar = states, conditions, and location.",
            "Saber knows facts; conocer knows people and places.",
            "Every verb above is shown in a real sentence - a verb is learned conjugated, never alone.",
        ],
        "requirements": [
            "Conjugate hablar, comer, and vivir in the full present tense from memory.",
            "Write the present tense of ser, estar, tener, ir, and poder without looking.",
            "Translate ten English sentences using these verbs, choosing ser or estar correctly each time.",
            "Explain the saber/conocer difference with two example sentences.",
            "Sort the 25 verbs into regular and irregular, naming each irregular verb's irregular form.",
        ],
        "standards": [
            "Conjugation paradigms follow the Nueva gramatica de la lengua espanola, Morfologia.",
            "The ser/estar distinction follows the Diccionario panhispanico de dudas usage guidance.",
            "Infinitive families (-ar, -er, -ir) follow the Real Academia Espanola classification.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: a verb is a signed action - its ending "
            "the seal of who acts and when. Where public grammar files "
            "conjugation tables, the Signature Word Method files fifteen "
            "irregular oaths: the pillars refuse the pattern because they "
            "carry the most weight."
        ),
    },
    {
        "key": "adjectives",
        "name": "Spanish Adjectives and Adverbs",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five adjectives with agreement examples, then fifteen "
            "adverbs. Adjectives match their noun in gender and number. "
            "1. bueno/buena (good) - Es un buen libro. / Es una buena "
            "idea. 2. malo/mala (bad) - Es un mal dia. / Es una mala "
            "noticia. 3. grande (big; gran before singular nouns) - Una "
            "casa grande. / Un gran hombre. 4. pequeño/pequeña (small) - Un "
            "perro pequeño. 5. nuevo/nueva (new) - Un coche nuevo. "
            "6. viejo/vieja (old) - Una casa vieja. 7. alto/alta (tall) - "
            "Un hombre alto. 8. bajo/baja (short) - Una mujer baja. "
            "9. largo/larga (long) - Un rio largo. 10. corto/corta (short) "
            "- Una historia corta. 11. feliz (happy; same both genders) - "
            "Estoy feliz. 12. triste (sad) - Está triste hoy. 13. bonito/"
            "bonita (pretty) - Una flor bonita. 14. feo/fea (ugly) - Un "
            "edificio feo. 15. rico/rica (rich; tasty) - Una comida rica. "
            "16. pobre (poor; same both genders) - Un país pobre. "
            "17. fácil (easy) - Un examen fácil. 18. difícil (difficult) - "
            "Una pregunta difícil. 19. rápido/rapida (fast) - Un coche "
            "rápido. 20. lento/lenta (slow) - Una tortuga lenta. "
            "21. caliente (hot; same both genders) - El café está caliente. "
            "22. frio/fria (cold) - La sopa está fria. 23. joven (young; "
            "same both genders) - Un maestro joven. 24. importante "
            "(important) - Una decision importante. 25. mejor (better, "
            "best) - Es el mejor dia. Fifteen adverbs (never change form): "
            "bien (well) - Canta bien. mal (badly) - Duerme mal. muy (very) "
            "- Es muy alto. poco (little) - Habla poco. mucho (a lot) - Te "
            "quiero mucho. siempre (always) - Siempre llega tarde. nunca "
            "(never) - Nunca miente. hoy (today) - Hoy llueve. ayer "
            "(yesterday) - Ayer vino. mañana (tomorrow) - Manana viajo. "
            "aquí (here) - Ven aquí. allí (there) - Está allí. ahora (now) "
            "- Hazlo ahora. después (afterwards) - Despues hablamos. "
            "también (also) - Yo también voy."
        ),
        "how_it_works": (
            "Adjectives agree with the noun they describe in gender and "
            "number: el libro bueno, la casa buena, los libros buenos, las "
            "casas buenas. Adjectives ending in -o change to -a for "
            "feminine; those ending in -e or a consonant usually stay the "
            "same (feliz, pobre, joven, importante). Plurals add -s or -es "
            "like nouns. Position matters: most adjectives follow the noun "
            "(una casa blanca), but bueno, malo, grande, and a few others "
            "can precede it and shorten - buen, mal, gran - with a "
            "figurative flavor: un gran hombre is a great man, un hombre "
            "grande is a big man. Adverbs never change: bien, mal, muy, "
            "siempre modify verbs, adjectives, or whole sentences. Many "
            "adverbs form with -mente (rapidamente), the Spanish -ly."
        ),
        "key_points": [
            "Adjectives agree in gender and number: bueno/buena/buenos/buenas; -e and consonant endings usually stay fixed.",
            "Most adjectives follow the noun; buen/mal/gran shorten and precede it (un gran hombre = a great man).",
            "Adverbs never change form: bien, mal, muy, siempre, nunca, hoy, ayer, mañana.",
            "The -mente ending builds adverbs from adjectives, like English -ly: rapida -> rapidamente.",
            "Every adjective and adverb above is shown working inside a real sentence.",
        ],
        "requirements": [
            "Write the four forms (masculine, feminine, masculine plural, feminine plural) of bueno, pequeño, alto, and rápido.",
            "Convert ten noun phrases to the opposite gender, fixing every adjective.",
            "Explain the gran/grande difference with two sentence pairs.",
            "Build five sentences using -mente adverbs you form yourself.",
            "Translate eight English sentences, placing each adjective correctly before or after the noun.",
        ],
        "standards": [
            "Agreement rules follow the Nueva gramatica de la lengua espanola, Sintaxis.",
            "Shortened forms (buen, mal, gran, primer, tercer) follow the Ortografia 2010.",
            "Adverb formation with -mente follows the Diccionario de la lengua espanola.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_ORT, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: the adjective signs itself to match its "
            "noun - gender and number the twin seals of agreement. Where "
            "public grammar files concordance tables, the Signature Word "
            "Method files a mirror oath: the description must wear the "
            "same seal as the thing described."
        ),
    },
    {
        "key": "pronouns",
        "name": "Spanish Pronouns",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The full Spanish pronoun paradigms with example sentences. "
            "Subject pronouns: yo (I) - Yo hablo. tú (you, informal) - Tú "
            "hablas. él (he) - Él habla. ella (she) - Ella habla. usted "
            "(you, formal) - Usted habla. nosotros/nosotras (we) - "
            "Nosotros hablamos. vosotros/vosotras (you all, informal, "
            "Spain) - Vosotros hablais. ellos (they, masculine/mixed) - "
            "Ellos hablan. ellas (they, feminine) - Ellas hablan. ustedes "
            "(you all, formal / universal in Latin America) - Ustedes "
            "hablan. Subject pronouns are usually dropped: Hablo español. "
            "Direct and indirect object pronouns: me (me) - Me ves. te "
            "(you) - Te veo. lo (him/it, masculine) - Lo compro. la (her/"
            "it, feminine) - La compro. le (to him/her/you) - Le escribo. "
            "nos (us) - Nos ayudas. os (you all, Spain) - Os veo. los "
            "(them, masculine) - Los invito. las (them, feminine) - Las "
            "invito. les (to them/you all) - Les hablo. Possessives: mi/mis "
            "(my) - Mi casa es tu casa. tu/tus (your, informal) - Tu libro. "
            "su/sus (his/her/your formal/their) - Su coche. nuestro/"
            "nuestra/nuestros/nuestras (our) - Nuestra familia. vuestro/"
            "vuestra (your all, Spain) - Vuestra clase. mio/mia (mine, "
            "after noun) - Es amigo mio. Demonstratives: este/esta (this) "
            "- Este libro es mio. ese/esa (that) - Esa silla es tuya. "
            "aquel/aquella (that over there) - Aquel edificio es viejo. "
            "estos/esos/aquellos for plurals. Interrogatives: qué (what) - "
            "¿Qué quieres? cuál (which) - ¿Cuál prefieres? quién (who) - "
            "¿Quién llama? dónde (where) - ¿Dónde vives? cuándo (when) - "
            "¿Cuándo vienes? por qué (why) - ¿Por qué lloras? cómo (how) - "
            "¿Cómo estás? cuánto (how much) - ¿Cuánto cuesta?"
        ),
        "how_it_works": (
            "Pronouns replace nouns, and Spanish pronouns do more work "
            "than English ones because they mark gender, formality, and "
            "case. The tu/usted split is the social engine: tu for friends, "
            "family, and children; usted for elders, officials, and "
            "strangers in formal settings; Latin America uses ustedes for "
            "all plurals while Spain keeps vosotros for informal groups. "
            "Object pronouns go before the conjugated verb (Me ves, Te "
            "quiero) but attach to the end of infinitives, gerunds, and "
            "affirmative commands (quiero verte, estoy viendote, dime). "
            "Possessives before the noun use the short forms (mi casa), "
            "after the noun the long forms (un amigo mio). Demonstratives "
            "mark three distances - este (near me), ese (near you), aquel "
            "(far from both) - a precision English lost."
        ),
        "key_points": [
            "Subject pronouns are usually dropped; the verb ending already says who acts.",
            "Tu is informal, usted is formal; ustedes covers all plurals in Latin America, vosotros the informal plural in Spain.",
            "Object pronouns precede the verb (Me ves) but attach to infinitives and affirmative commands (verte, dime).",
            "Este/ese/aquel mark three distances: near me, near you, far from both.",
            "Mi casa (short form before) versus un amigo mio (long form after) - position changes the form.",
        ],
        "requirements": [
            "Write the full subject, object, and possessive paradigms from memory.",
            "Convert five tu sentences to usted, fixing verbs and pronouns.",
            "Place object pronouns correctly in ten sentences (before verbs, attached to infinitives).",
            "Build three sentences each with este, ese, and aquel showing the distance logic.",
            "Translate eight English pronoun sentences, dropping subject pronouns where Spanish would.",
        ],
        "standards": [
            "Paradigms follow the Nueva gramatica de la lengua espanola, Morfologia.",
            "The tu/vos/usted distribution follows the Diccionario panhispanico de dudas.",
            "Object pronoun placement follows the Nueva gramatica, Sintaxis.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: the pronoun is the seal of the speaker - "
            "yo the sign of the self, usted the bow of respect. Where "
            "public grammar files paradigms, the Signature Word Method "
            "files relationships: every pronoun a signed measure of "
            "distance between souls."
        ),
    },
    {
        "key": "numbers",
        "name": "Spanish Numbers and Time",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Numbers 1 to 20: uno, dos, tres, cuatro, cinco, seis, siete, "
            "ocho, nueve, diez, once, doce, trece, catorce, quince, "
            "dieciseis, diecisiete, dieciocho, diecinueve, veinte. Tens: "
            "treinta, cuarenta, cincuenta, sesenta, setenta, ochenta, "
            "noventa, cien (ciento before other numbers: ciento uno). "
            "Compound numbers join with y: veintiuno (21, one word to 29), "
            "treinta y uno (31), cuarenta y dos (42), cincuenta y cinco "
            "(55), noventa y nueve (99). Hundreds: doscientos, "
            "trescientos, cuatrocientos, quinientos, seiscientos, "
            "setecientos, ochocientos, novecientos; mil (1,000), un millon "
            "(1,000,000). Ordinals: primero, segundo, tercero, cuarto, "
            "quinto, sexto, septimo, octavo, noveno, decimo - La primera "
            "vez. (The first time.) Days: lunes, martes, miércoles, "
            "jueves, viernes, sábado, domingo - Hoy es sábado. (Today is "
            "Saturday.) Months: enero, febrero, marzo, abril, mayo, junio, "
            "julio, agosto, septiembre, octubre, noviembre, diciembre - Mi "
            "cumpleanos es en octubre. Seasons: la primavera, el verano, "
            "el otoño, el invierno. Clock time: Es la una. (It is one "
            "o'clock.) Son las dos. (It is two.) Son las tres y cuarto. "
            "(3:15.) Son las cuatro y media. (4:30.) Son las cinco menos "
            "cuarto. (4:45.) Dates: Hoy es 17 de octubre de 2026. (Today "
            "is October 17, 2026.) Naci el 3 de mayo. (I was born May 3.) "
            "Example sentences: Tengo treinta años. (I am thirty years "
            "old.) La reunión es a las nueve y media. (The meeting is at "
            "9:30.) Hay cien estudiantes. (There are one hundred "
            "students.) El tren sale el lunes. (The train leaves Monday.)"
        ),
        "how_it_works": (
            "Spanish numbers build by pattern: 16-19 and 21-29 fuse into "
            "single words (dieciseis, veintidos), 31-99 join with y "
            "(treinta y uno), and hundreds agree in gender with the noun "
            "(doscientas casas). Uno shortens to un before masculine nouns "
            "(un libro) and becomes una before feminine (una mesa); in "
            "counting it stays uno. Time uses ser: Es la una for one "
            "o'clock (singular), Son las dos through Son las doce "
            "(plural). Minutes past the hour use y (Son las tres y diez), "
            "minutes to the hour use menos (Son las cuatro menos diez), "
            "with y cuarto, y media, menos cuarto as the landmarks. Dates "
            "run day-month-year with de: el 17 de octubre de 2026. Days and "
            "months are lowercase in Spanish."
        ),
        "key_points": [
            "1-15 are unique words; 16-29 fuse into one word; 31-99 join with y; cien becomes ciento before more numbers.",
            "Time: Es la una (singular) versus Son las dos (plural); y cuarto, y media, menos cuarto.",
            "Uno becomes un/una before nouns; hundreds agree in gender (doscientas casas).",
            "Dates run day-month-year: el 17 de octubre de 2026; days and months are lowercase.",
            "Ordinals primero through decimo; primero and tercero shorten to primer/tercer before masculine nouns.",
        ],
        "requirements": [
            "Count 1-100 aloud without hesitation, then write 21, 33, 47, 58, 76, 99 in words.",
            "Tell the time for 1:00, 2:15, 4:30, 6:45, 9:10, 11:50 in full Spanish sentences.",
            "Write the seven days, twelve months, and four seasons with correct spelling.",
            "Write five dates (including today) in the el 17 de octubre de 2026 form.",
            "Convert 200 casas, 300 libros, 500 euros to words with correct gender agreement.",
        ],
        "standards": [
            "Number words and the cien/ciento rule follow the Ortografia de la lengua espanola 2010.",
            "Ordinal shortening (primer, tercer) follows the Nueva gramatica.",
            "Time expressions follow standard usage in the Diccionario panhispanico de dudas.",
        ],
        "citations": [CIT_RAE_ORT, CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: numbers are the sworn measures - uno the "
            "first seal, cien the hundredth. Where public arithmetic "
            "counts, the Signature Word Method weighs: every number a "
            "signed quantity, every hour a covenant kept with the day."
        ),
    },
    {
        "key": "greetings",
        "name": "Spanish Greetings and Everyday Phrases",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Thirty greetings, farewells, and politeness phrases with "
            "usage notes. 1. Hola. (Hello.) - universal greeting. "
            "2. Buenos días. (Good morning.) - until midday. 3. Buenas "
            "tardes. (Good afternoon.) - midday to evening. 4. Buenas "
            "noches. (Good evening/night.) - evening greeting and bedtime "
            "farewell. 5. Adios. (Goodbye.) - final farewell. 6. Hasta "
            "luego. (See you later.) - casual. 7. Hasta mañana. (See you "
            "tomorrow.) 8. Hasta pronto. (See you soon.) 9. Nos vemos. "
            "(See you.) - very casual. 10. ¿Cómo estás? (How are you?, "
            "informal.) 11. ¿Cómo está usted? (How are you?, formal.) "
            "12. Bien, gracias. (Fine, thanks.) 13. Muy bien, ¿y tú? (Very "
            "well, and you?) 14. Mas o menos. (So-so.) 15. ¿Qué tal? "
            "(How is it going?) - casual. 16. Encantado./Encantada. "
            "(Delighted to meet you; masculine/feminine.) 17. Mucho gusto. "
            "(Nice to meet you.) 18. Por favor. (Please.) 19. Gracias. "
            "(Thank you.) 20. Muchas gracias. (Thank you very much.) "
            "21. De nada. (You are welcome.) 22. Con permiso. (Excuse me, "
            "to pass.) 23. Perdon. (Sorry/excuse me.) 24. Disculpe. "
            "(Excuse me, formal.) 25. Lo siento. (I am sorry.) - for real "
            "regret. 26. Bienvenido./Bienvenida. (Welcome.) 27. Salud! "
            "(Cheers!/Bless you after a sneeze.) 28. Feliz cumpleanos! "
            "(Happy birthday!) 29. Que tengas un buen dia. (Have a good "
            "day.) 30. Cuidate. (Take care.)"
        ),
        "how_it_works": (
            "Spanish greetings run on the clock and the relationship. "
            "Buenos días rules the morning, buenas tardes the afternoon, "
            "buenas noches the evening - and buenas noches doubles as the "
            "bedtime farewell. The handshake of formality: como estas and "
            "que tal for friends, como está usted for elders and officials. "
            "Politeness has three doors: con permiso to move past someone, "
            "perdon or disculpe to get attention or excuse a small fault, "
            "lo siento for genuine regret. Gracias takes muchas for "
            "emphasis, and de nada (it is nothing) answers it. Physical "
            "greeting varies by country - cheek kisses in Spain and much "
            "of Latin America, handshake in formal México - but the words "
            "above work everywhere."
        ),
        "key_points": [
            "Greetings follow the clock: buenos días, buenas tardes, buenas noches (also the bedtime farewell).",
            "Como estas (informal) versus Como está usted (formal) - the relationship sets the form.",
            "Con permiso (to pass), perdon/disculpe (excuse me), lo siento (true apology) - three different doors.",
            "De nada answers gracias; mucho gusto and encantado/a open introductions.",
            "All 30 phrases are universal Spanish - they work in every Spanish-speaking country.",
        ],
        "requirements": [
            "Greet for 8:00, 14:00, and 21:00 correctly, and say goodnight at bedtime.",
            "Hold a 10-line greeting exchange switching between informal and formal midway.",
            "Use con permiso, perdon, and lo siento each in a correct scenario sentence.",
            "Write five thank-you exchanges with gracias, muchas gracias, and de nada.",
            "Introduce yourself two ways (mucho gusto, encantado/a) with correct gender.",
        ],
        "standards": [
            "Greeting forms follow the Diccionario panhispanico de dudas usage notes.",
            "Formal/informal address follows the Nueva gramatica treatment of usted.",
            "Regional greeting customs are noted as custom, not grammar.",
        ],
        "citations": [CIT_RAE_DICT, CIT_RAE_GRAM],
        "sig_lens": (
            "The Signature read: a greeting is the first seal between two "
            "people - hola the open door, adiós the closed one with "
            "promise. Where public phrasebooks list words, the Signature "
            "Word Method teaches thresholds: every greeting a signed "
            "crossing from stranger to known."
        ),
    },
    {
        "key": "grammar",
        "name": "Spanish Grammar Essentials",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "The seven load-bearing rules of Spanish grammar, each with "
            "translated examples. Word order: subject-verb-object, as in "
            "English - María come manzanas. (María eats apples.) Adjectives "
            "usually follow nouns: una casa blanca. (a white house.) "
            "Gender: every noun is masculine or feminine - el libro (the "
            "book, masculine), la mesa (the table, feminine). Number: "
            "singular and plural - el niño / los niños, la flor / las "
            "flores. Articles: definite el/la/los/las (the), indefinite "
            "un/una/unos/unas (a, some) - Quiero un café. (I want a "
            "coffee.) Spanish uses definite articles more than English: Me "
            "gusta el café. (I like coffee.) Negation: no goes before the "
            "verb - No hablo francés. (I do not speak French.) Double "
            "negatives are required, not forbidden: No veo a nadie. (I "
            "see nobody - literally 'I do not see nobody.') Nunca, nadie, "
            "nada, ninguno follow the same pattern: Nunca llueve aquí. "
            "(It never rains here.) Questions: invert or just raise the "
            "voice - Hablas español? (Do you speak Spanish?) - and frame "
            "with inverted marks in writing. Question words lead: ¿Dónde "
            "vives? (Where do you live?) Agreement: articles, adjectives, "
            "and pronouns match their noun in gender and number - Las "
            "casas blancas son caras. (The white houses are expensive.)"
        ),
        "how_it_works": (
            "Spanish grammar is a system of agreements orbiting the noun. "
            "Pick the noun, and everything touching it - article, "
            "adjective, pronoun - takes its gender and number: el libro "
            "viejo, la mesa vieja, los libros viejos, las mesas viejas. "
            "The verb is the second orbit: its ending agrees with the "
            "subject in person and number, which is why the subject can be "
            "dropped. Negation is a single slot before the verb (no), and "
            "negative words stack after it without canceling (no veo "
            "nada). Questions need no helper verb: statement Habla español "
            "becomes question Hablas español? by intonation and the "
            "inverted marks. Build sentences inside-out: noun with its "
            "agreements, verb with its ending, then the modifiers."
        ),
        "key_points": [
            "Base order is subject-verb-object; adjectives usually follow the noun they describe.",
            "Everything agrees with the noun: article, adjective, and pronoun share its gender and number.",
            "No goes before the verb; negative words stack (No veo a nadie) instead of canceling.",
            "Questions need no helper verb - intonation plus inverted marks do the work.",
            "The definite article appears where English drops it: Me gusta el café (I like coffee).",
        ],
        "requirements": [
            "Diagram five sentences labeling subject, verb, object, and every agreement.",
            "Convert ten affirmative sentences to negative, using nadie, nada, and nunca correctly.",
            "Turn ten statements into questions two ways (intonation and question word).",
            "Fix five sentences with deliberate agreement errors, explaining each fix.",
            "Write ten original sentences using the definite article where English would drop it.",
        ],
        "standards": [
            "Agreement and word order follow the Nueva gramatica de la lengua espanola, Sintaxis.",
            "Negation patterns follow the Nueva gramatica treatment of negative concord.",
            "Article usage follows the Diccionario panhispanico de dudas.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: grammar is the covenant that binds words "
            "into truth - agreement the seal, word order the procession. "
            "Where public syntax draws trees, the Signature Word Method "
            "draws orbits: every word circling its noun, every verb "
            "answering its subject."
        ),
    },
    {
        "key": "home_family",
        "name": "Spanish Home and Family Sentences",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about house, rooms, furniture, and family "
            "members, each with English translation. 1. La casa es grande. "
            "(The house is big.) 2. Mi madre cocina en la cocina. (My "
            "mother cooks in the kitchen.) 3. El dormitorio tiene dos "
            "camas. (The bedroom has two beds.) 4. Mi padre lee el "
            "periodico en la sala. (My father reads the newspaper in the "
            "living room.) 5. Mi hermana mayor vive en Madrid. (My older "
            "sister lives in Madrid.) 6. Tenemos un perro y un gato. (We "
            "have a dog and a cat.) 7. La mesa del comedor es de madera. "
            "(The dining-room table is made of wood.) 8. Mi abuela cuenta "
            "historias. (My grandmother tells stories.) 9. El baño está al "
            "final del pasillo. (The bathroom is at the end of the "
            "hallway.) 10. Mi hermano menor juega en el jardin. (My "
            "younger brother plays in the garden.) 11. La cocina huele a "
            "pan fresco. (The kitchen smells of fresh bread.) 12. Los niños "
            "hacen la tarea en su cuarto. (The children do homework in "
            "their room.) 13. Mi tío nos visita los domingos. (My uncle "
            "visits us on Sundays.) 14. La ventana da al parque. (The "
            "window looks onto the park.) 15. Guardamos los libros en el "
            "estante. (We keep the books on the shelf.) 16. Mi prima "
            "estudia medicina. (My cousin, female, studies medicine.) "
            "17. El sofá es muy cómodo. (The sofá is very comfortable.) "
            "18. Cenamos juntos a las ocho. (We have dinner together at "
            "eight.) 19. Mi abuelo riega las plantas. (My grandfather "
            "waters the plants.) 20. Nuestra familia es muy unida. (Our "
            "family is very close.)"
        ),
        "how_it_works": (
            "Home sentences teach estar for location and condition (El "
            "baño está al final del pasillo; La cocina huele...) versus ser "
            "for identity and traits (La casa es grande; Nuestra familia "
            "es unida). Family vocabulary runs on gender pairs - padre/"
            "madre, hermano/hermana, abuelo/abuela, tío/tía, primo/prima - "
            "with mayor (older) and menor (younger) marking birth order. "
            "Possessives anchor the people: mi madre, tu cuarto, su casa, "
            "nuestra familia. Rooms take en or the verb estar with location "
            "phrases: en la cocina, en el jardin, al final del pasillo. "
            "Notice reflexive-free daily verbs (cocina, lee, juega) and the "
            "present tense carrying habitual meaning: Cenamos juntos means "
            "'we have dinner together' as a routine, not just tonight."
        ),
        "key_points": [
            "Ser for what the home and family are (es grande, es unida); estar for where things are (está al final).",
            "Family words come in gender pairs: padre/madre, hermano/hermana, abuelo/abuela, tío/tía, primo/prima.",
            "Mayor and menor mark older and younger siblings without new nouns.",
            "Possessives anchor people and rooms: mi madre, su cuarto, nuestra familia.",
            "The present tense carries habitual meaning: Cenamos juntos = we have dinner together (routinely).",
        ],
        "requirements": [
            "Label every ser/estar in the 20 sentences and justify each choice in one line.",
            "Draw your family tree in Spanish with all the relation words from this record.",
            "Write ten new sentences describing your own home using estar for locations.",
            "Convert five sentences to plural (mi hermano -> mis hermanos), fixing agreements.",
            "Describe your family routine in eight sentences modeled on sentences 18-20.",
        ],
        "standards": [
            "Family vocabulary follows the Diccionario de la lengua espanola.",
            "The ser/estar distribution follows the Nueva gramatica de la lengua espanola.",
            "Room and furniture terms follow standard usage in the Diccionario panhispanico de dudas.",
        ],
        "citations": [CIT_RAE_DICT, CIT_RAE_GRAM],
        "sig_lens": (
            "The Signature read: the home is the first sealed covenant - "
            "mi madre, mi casa, the words that need no translation because "
            "they are sworn in the blood. Where public vocabulary lists "
            "rooms, the Signature Word Method maps the hearth: every family "
            "word a seal pressed by childhood."
        ),
    },
    {
        "key": "food_cooking",
        "name": "Spanish Food and Cooking Sentences",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about meals, ingredients, cooking actions, "
            "and restaurants, each with English translation. 1. Desayuno "
            "café con leche y tostadas. (I have coffee with milk and "
            "toast for breakfast.) 2. El almuerzo es a las dos. (Lunch is "
            "at two.) 3. Me gusta la paella. (I like paella.) 4. La sopa "
            "está caliente. (The soup is hot.) 5. Corta las cebollas en "
            "cubos. (Cut the onions into cubes.) 6. Anade sal al gusto. "
            "(Add salt to taste.) 7. Hierve el agua primero. (Boil the "
            "water first.) 8. Frie los huevos en aceite de oliva. (Fry the "
            "eggs in olive oil.) 9. El pan está en el horno. (The bread is "
            "in the oven.) 10. ¿Qué hay de postre? (What is for dessert?) "
            "11. La cuenta, por favor. (The check, please.) 12. Una mesa "
            "para dos, por favor. (A table for two, please.) 13. El pescado "
            "está fresco hoy. (The fish is fresh today.) 14. No como "
            "carne. (I do not eat meat.) 15. ¿Tienen menú del día? (Do you "
            "have a daily special?) 16. El cocinero recomienda el guiso. "
            "(The cook recommends the stew.) 17. Lava las verduras. (Wash "
            "the vegetables.) 18. Mezcla bien los ingredientes. (Mix the "
            "ingredients well.) 19. El restaurante abre a las ocho. (The "
            "restaurant opens at eight.) 20. Deja propina si el servicio "
            "fue bueno. (Leave a tip if the service was good.)"
        ),
        "how_it_works": (
            "Food sentences run on gustar, the backward verb: Me gusta la "
            "paella puts the liked thing as the subject and the person as "
            "the indirect object - literally 'paella is pleasing to me.' "
            "Use me/te/le/nos/os/les + gusta/gustan, matching singular or "
            "plural of the thing liked. Cooking instructions use the "
            "affirmative tu command (corta, anade, hierve, frie, lava, "
            "mezcla) - the third-person singular present form. Restaurant "
            "Spanish is formulaic: Una mesa para dos, La cuenta por favor, "
            "menú del dia for the fixed-price lunch. Taste and state take "
            "estar (está caliente, está fresco, está listo) because they "
            "describe conditions, while identity takes ser (El almuerzo es "
            "a las dos)."
        ),
        "key_points": [
            "Gustar works backwards: Me gusta la paella - the thing liked is the subject.",
            "Recipe steps use the affirmative tu command: corta, anade, hierve, frie, mezcla.",
            "Restaurant formulas: Una mesa para dos, La cuenta por favor, menú del dia.",
            "Taste and condition take estar (está caliente); scheduled facts take ser (es a las dos).",
            "Meal names: el desayuno, el almuerzo, la cena - and merienda for the afternoon snack.",
        ],
        "requirements": [
            "Conjugate gustar with all six indirect objects for a singular and a plural food.",
            "Write a six-step recipe in tu commands using verbs from this record.",
            "Role-play ordering a full meal: table, order, special request, check.",
            "Label every ser/estar in the 20 sentences with one-line justifications.",
            "List ten foods you like and ten you dislike using me gusta/no me gusta correctly.",
        ],
        "standards": [
            "The gustar construction follows the Nueva gramatica de la lengua espanola.",
            "Command forms follow the Nueva gramatica, Morfologia.",
            "Food vocabulary follows the Diccionario de la lengua espanola.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: the table is a covenant of plenty - "
            "gustar the backward oath where the food is the subject and "
            "the eater the witness. Where public phrasebooks list dishes, "
            "the Signature Word Method sets the table: every meal a "
            "signed gathering, every recipe an oath kept in steps."
        ),
    },
    {
        "key": "travel",
        "name": "Spanish Travel and Directions Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about transport, asking directions, tickets, "
            "and lodging, each with English translation. 1. ¿Dónde está la "
            "estación de tren? (Where is the train station?) 2. Necesito "
            "dos billetes a Barcelona. (I need two tickets to Barcelona.) "
            "3. El avión sale a las seis. (The plane leaves at six.) "
            "4. El autobús llega tarde. (The bus is arriving late.) "
            "5. ¿A qué hora abre el hotel? (At what time does the hotel "
            "open?) 6. Tengo una reserva a nombre de García. (I have a "
            "reservation under García.) 7. La habitación tiene vista al "
            "mar. (The room has a sea view.) 8. ¿Cuánto cuesta el taxi al "
            "centro? (How much is the taxi to downtown?) 9. Gira a la "
            "derecha en la esquina. (Turn right at the corner.) 10. Sigue "
            "recto dos cuadras. (Go straight for two blocks.) 11. El museo "
            "está cerca de aquí. (The museum is near here.) 12. Perdi mi "
            "pasaporte. (I lost my passport.) 13. ¿Hablas inglés? (Do you "
            "speak English?) 14. La playa está a diez minutos. (The beach "
            "is ten minutes away.) 15. Alquilo un coche por tres días. (I "
            "am renting a car for three days.) 16. El tren de alta "
            "velocidad es rápido. (The high-speed train is fast.) 17. Mi "
            "vuelo tiene escala en Miami. (My flight has a layover in "
            "Miami.) 18. La maleta pesa veinte kilos. (The suitcase weighs "
            "twenty kilos.) 19. El guía habla tres idiomas. (The guide "
            "speaks three languages.) 20. Vuelvo el lunes por la mañana. "
            "(I return Monday morning.)"
        ),
        "how_it_works": (
            "Travel Spanish is built on question frames and direction "
            "verbs. ¿Dónde está...? locates anything; ¿Cuánto cuesta...? "
            "prices anything; A que hora...? times anything. Directions "
            "use the tu command: gira (turn), sigue (continue), cruza "
            "(cross), toma (take). Distance runs on estar + a + time or "
            "place: Está a diez minutos, Está cerca de aquí, Está lejos. "
            "Tickets and reservations use querer and necesitar: Quiero un "
            "billete, Necesito dos billetes, Tengo una reserva. "
            "Transport verbs: salir (to depart), llegar (to arrive), "
            "perder (to lose/miss - Perdi el tren means 'I missed the "
            "train'), alquilar (to rent). Por marks duration (por tres "
            "días), para marks destination (para Barcelona)."
        ),
        "key_points": [
            "Three question frames open every trip: ¿Dónde está...?, ¿Cuánto cuesta...?, ¿A qué hora...?",
            "Directions use tu commands: gira, sigue, cruza, toma; distance uses está a / está cerca de.",
            "Perder means both to lose and to miss: Perdi mi pasaporte, Perdi el tren.",
            "Por marks duration (por tres días); para marks destination (para Barcelona).",
            "Salir departs, llegar arrives; escala is a layover, and la maleta is the suitcase.",
        ],
        "requirements": [
            "Ask for directions to five places using ¿Dónde está? and follow with command-based answers.",
            "Buy tickets in a role-play: destination, quantity, time, price.",
            "Check into a hotel: reservation, room request, checkout time.",
            "Give walking directions with gira, sigue, cruza for a six-step route.",
            "Report three travel problems (lost passport, late bus, missed flight) in Spanish.",
        ],
        "standards": [
            "Question formation follows the Nueva gramatica de la lengua espanola, Sintaxis.",
            "Direction vocabulary follows the Diccionario de la lengua espanola.",
            "The por/para distinction follows the Nueva gramatica usage guidance.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: the road is a covenant of arrival - "
            "donde está the question that opens every map, sigue recto "
            "the oath of the straight path. Where public phrasebooks "
            "list stations, the Signature Word Method signs the journey: "
            "every ticket a sealed promise of return."
        ),
    },
    {
        "key": "work_school",
        "name": "Spanish Work and School Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about jobs, the office, the classroom, and "
            "learning, each with English translation. 1. Trabajo en una "
            "oficina. (I work in an office.) 2. Soy maestra de español. "
            "(I am a Spanish teacher, female.) 3. La reunión empieza a las "
            "nueve. (The meeting starts at nine.) 4. Tengo que entregar el "
            "informe hoy. (I have to turn in the report today.) 5. Mi jefe "
            "es muy justo. (My boss is very fair.) 6. Estudio ingeniería. "
            "(I study engineering.) 7. La clase de matemáticas es difícil. "
            "(Math class is hard.) 8. El examen es el viernes. (The exam "
            "is Friday.) 9. Aprendo vocabulario nuevo cada dia. (I learn "
            "new vocabulary every day.) 10. Mis compañeros son amables. "
            "(My coworkers/classmates are kind.) 11. El profesor explica "
            "bien. (The teacher explains well.) 12. Hago la tarea después "
            "de cenar. (I do homework after dinner.) 13. Busco trabajo de "
            "medio tiempo. (I am looking for part-time work.) 14. Mi "
            "horario es de ocho a cinco. (My schedule is eight to five.) "
            "15. La biblioteca cierra a las diez. (The library closes at "
            "ten.) 16. Presente mi proyecto ayer. (I presented my project "
            "yesterday.) 17. Me ascendieron el mes pasado. (I was promoted "
            "last month.) 18. Los estudiantes leen mucho. (The students "
            "read a lot.) 19. Escribo correos en español. (I write emails "
            "in Spanish.) 20. Me gusta mi trabajo. (I like my job.)"
        ),
        "how_it_works": (
            "Work and school sentences run on tener que + infinitive for "
            "obligation (Tengo que entregar), present tense for routine "
            "(Trabajo en una oficina), and preterite for completed events "
            "(Presente mi proyecto ayer). Job titles agree in gender: el "
            "maestro/la maestra, el jefe/la jefa, el estudiante/la "
            "estudiante (same form). De marks field and schedule: maestra "
            "de español, trabajo de medio tiempo, de ocho a cinco. "
            "Companero covers both coworker and classmate - context "
            "decides. The passive-like Me ascendieron ('they promoted me') "
            "shows how Spanish avoids the passive with a third-person "
            "plural. School verbs cluster: estudiar, aprender, leer, "
            "escribir, presentar, explicar."
        ),
        "key_points": [
            "Tener que + infinitive expresses obligation: Tengo que entregar el informe.",
            "Job titles agree in gender: maestro/maestra, jefe/jefa; estudiante works for both.",
            "De marks field and schedule: maestra de español, de ocho a cinco, trabajo de medio tiempo.",
            "Me ascendieron shows the Spanish they-passive replacing the English passive.",
            "Routine uses present, completed events use preterite: Trabajo aquí; Presente ayer.",
        ],
        "requirements": [
            "Write your job or studies in six sentences using ser, trabajar/estudiar, and tener que.",
            "Convert five present-routine sentences to preterite completed events.",
            "Build the gender pairs for ten job titles from this record.",
            "Role-play a job interview: greet, describe experience, ask two questions.",
            "Describe your school day hour by hour in eight sentences.",
        ],
        "standards": [
            "The tener que construction follows the Nueva gramatica de la lengua espanola.",
            "Job-title gender follows the Diccionario de la lengua espanola.",
            "Tense usage follows the Nueva gramatica treatment of present and preterite.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: work is the daily oath renewed - tengo "
            "que the seal of duty, aprendo the seal of growth. Where "
            "public vocabulary lists offices, the Signature Word Method "
            "files the craft: every trade a covenant, every lesson a "
            "signed step upward."
        ),
    },
    {
        "key": "health_body",
        "name": "Spanish Health and Body Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about body parts, symptoms, the doctor "
            "visit, and the pharmacy, each with English translation. "
            "1. Me duele la cabeza. (My head hurts - literally 'the head "
            "hurts me.') 2. Tengo fiebre. (I have a fever.) 3. El médico "
            "me recetó antibioticos. (The doctor prescribed antibiotics "
            "for me.) 4. La farmacia está en la esquina. (The pharmacy is "
            "on the corner.) 5. Me torcí el tobillo. (I twisted my ankle.) "
            "6. Necesito gafas nuevas. (I need new glasses.) 7. Duermo "
            "ocho horas. (I sleep eight hours.) 8. Como frutas todos los "
            "días. (I eat fruit every day.) 9. Hago ejercicio tres veces "
            "por semana. (I exercise three times a week.) 10. Me siento "
            "mareado. (I feel dizzy, masculine.) 11. Tengo tos y dolor de "
            "garganta. (I have a cough and a sore throat.) 12. La enfermera "
            "tomo mi presión. (The nurse took my blood pressure.) 13. "
            "Necesito una cita con el dentista. (I need an appointment "
            "with the dentist.) 14. Me lavo las manos antes de comer. (I "
            "wash my hands before eating.) 15. El corazón late rápido. "
            "(The heart beats fast.) 16. Respira profundo. (Breathe deeply "
            "- command.) 17. Tengo alergia al polen. (I am allergic to "
            "pollen.) 18. El hospital queda lejos. (The hospital is far.) "
            "19. Bebe mucha agua. (Drink lots of water - command.) 20. "
            "Descansa y te sentiras mejor. (Rest and you will feel "
            "better.)"
        ),
        "how_it_works": (
            "Body Spanish runs on three patterns. Pain uses doler "
            "backwards like gustar: Me duele la cabeza, Me duelen los "
            "pies - the body part is the subject. States use tener, not "
            "estar: Tengo fiebre, Tengo tos, Tengo alergia, Tengo treinta "
            "años - Spanish 'has' what English 'is.' Hygiene and daily "
            "care use reflexives: me lavo, se cepilla, nos vestimos - the "
            "action falls on the self. Body parts take the definite "
            "article, not possessives: Me duele la cabeza, never 'mi "
            "cabeza,' and Me lavo las manos, never 'mis manos.' Doctor "
            "verbs: recetar (prescribe), tomar la presión (take blood "
            "pressure), torcerse (twist), sentirse (feel). Health advice "
            "uses tu commands: descansa, bebe, respira."
        ),
        "key_points": [
            "Pain works backwards: Me duele la cabeza - the body part is the subject, like gustar.",
            "Spanish 'has' what English 'is': Tengo fiebre, Tengo tos, Tengo alergia.",
            "Reflexives handle self-care: me lavo, se cepilla, me siento.",
            "Body parts take the definite article: Me duele la cabeza, Me lavo las manos.",
            "Advice uses tu commands: Descansa, Bebe agua, Respira profundo.",
        ],
        "requirements": [
            "Conjugate doler for cabeza, pies, espalda, and muelas with correct me/te/le.",
            "Convert eight English 'I am...' health states to tener constructions.",
            "Write your morning routine with five reflexive verbs and definite articles.",
            "Role-play a doctor visit: symptoms, questions, prescription, advice.",
            "Label every reflexive verb in the 20 sentences and name its infinitive.",
        ],
        "standards": [
            "The doler construction follows the Nueva gramatica de la lengua espanola.",
            "Reflexive usage follows the Nueva gramatica treatment of reflexive verbs.",
            "Medical vocabulary follows the Diccionario de la lengua espanola.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: the body is the first sealed vessel - "
            "me duele the oath of pain spoken backwards, me lavo the "
            "daily renewal. Where public phrasebooks list symptoms, the "
            "Signature Word Method tends the vessel: every health word a "
            "signed care for the living seal."
        ),
    },
    {
        "key": "emotions",
        "name": "Spanish Emotions and Feelings Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about being happy, sad, angry, afraid, in "
            "love, and surprised, each with English translation. 1. Estoy "
            "feliz hoy. (I am happy today.) 2. Me siento triste por la "
            "noticia. (I feel sad about the news.) 3. Está enojado con su "
            "hermano. (He is angry with his brother.) 4. Tengo miedo de la "
            "oscuridad. (I am afraid of the dark - 'I have fear.') 5. La "
            "quiero mucho. (I love her very much.) 6. Me sorprendio la "
            "fiesta. (The party surprised me.) 7. Estoy orgulloso de ti. "
            "(I am proud of you, masculine speaker.) 8. Se puso nervioso "
            "antes del examen. (He got nervous before the exam.) 9. Estamos "
            "emocionados por el viaje. (We are excited about the trip.) "
            "10. Me siento solo a veces. (I feel lonely sometimes.) "
            "11. Ella está tranquila ahora. (She is calm now.) 12. Nos "
            "reimos toda la noche. (We laughed all night.) 13. Lloro de "
            "alegria. (She cried with joy.) 14. Estoy agradecido por tu "
            "ayuda. (I am grateful for your help.) 15. Tiene vergüenza de "
            "cantar. (He is embarrassed to sing - 'he has shame.') "
            "16. Me aburro en clase. (I get bored in class.) 17. Está "
            "celoso de su amigo. (He is jealous of his friend.) 18. Siento "
            "paz aquí. (I feel peace here.) 19. Me encanta esta cancion. "
            "(I love this song - encantar works like gustar.) 20. El bebe "
            "se rie. (The baby laughs.)"
        ),
        "how_it_works": (
            "Emotions take estar, not ser, because feelings are states: "
            "Estoy feliz, Está enojado, Ella está tranquila - with ser "
            "reserved for traits (Es feliz = he is a happy person). "
            "Reflexive verbs carry change and experience: sentirse (to "
            "feel), ponerse (to become: Se puso nervioso), reirse (to "
            "laugh), aburrirse (to get bored). Spanish 'has' several "
            "feelings English 'is': Tengo miedo, Tiene vergüenza. "
            "Gustar-family verbs (gustar, encantar, sorprender, doler) put "
            "the feeling's source as subject: Me encanta esta cancion, Me "
            "sorprendio la fiesta. De marks the cause: triste por la "
            "noticia, orgulloso de ti, celoso de su amigo. Adjectives of "
            "feeling agree with the speaker: orgulloso/orgullosa, "
            "agradecido/agradecida."
        ),
        "key_points": [
            "Feelings take estar (Estoy feliz); ser marks traits (Es feliz = a happy person).",
            "Reflexives carry emotional change: sentirse, ponerse nervioso, reirse, aburrirse.",
            "Spanish 'has' feelings: Tengo miedo, Tiene vergüenza.",
            "Encantar and sorprender work backwards like gustar: Me encanta esta cancion.",
            "Feeling adjectives agree with the speaker: orgulloso/orgullosa, agradecido/agradecida.",
        ],
        "requirements": [
            "Write twelve sentences pairing each emotion with estar and the correct adjective agreement.",
            "Conjugate sentirse, ponerse, and reirse in the present with all six subjects.",
            "Explain five ser/estar emotion pairs (es feliz vs está feliz) with translations.",
            "Build eight gustar-family emotion sentences with the source as subject.",
            "Describe your week emotionally in ten sentences using de/por for causes.",
        ],
        "standards": [
            "The ser/estar emotion distinction follows the Nueva gramatica de la lengua espanola.",
            "Reflexive emotion verbs follow the Nueva gramatica treatment of reflexives.",
            "Emotion vocabulary follows the Diccionario de la lengua espanola.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: feeling is the seal of the inner life - "
            "estoy feliz the sworn state of the hour, te quiero the "
            "deepest signature of all. Where public vocabulary lists "
            "moods, the Signature Word Method reads the heart's "
            "handwriting: every emotion a signed confession of the soul."
        ),
    },
    {
        "key": "nature_weather",
        "name": "Spanish Nature and Weather Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about animals, plants, seasons, and weather "
            "talk, each with English translation. 1. El perro ladra. (The "
            "dog barks.) 2. El gato duerme al sol. (The cat sleeps in the "
            "sun.) 3. Hace sol hoy. (It is sunny today - 'it makes sun.') "
            "4. Está lloviendo. (It is raining.) 5. Nieva en las montañas. "
            "(It snows in the mountains.) 6. Hace mucho calor. (It is very "
            "hot.) 7. Hace frio por la noche. (It is cold at night.) "
            "8. Hay mucho viento. (It is very windy - 'there is much "
            "wind.') 9. Las flores florecen en primavera. (The flowers "
            "bloom in spring.) 10. Los árboles pierden hojas en otoño. "
            "(The trees lose leaves in autumn.) 11. El rio corre rápido. "
            "(The river runs fast.) 12. La montaña es alta. (The mountain "
            "is tall.) 13. Veo pájaros en el cielo. (I see birds in the "
            "sky.) 14. Las estrellas brillan. (The stars shine.) 15. Hace "
            "buen tiempo. (The weather is nice.) 16. El pronóstico dice "
            "tormenta. (The forecast says storm.) 17. La playa tiene arena "
            "blanca. (The beach has white sand.) 18. El bosque es "
            "silencioso. (The forest is quiet.) 19. Sale el sol a las "
            "siete. (The sun rises at seven.) 20. La luna está llena. "
            "(The moon is full.)"
        ),
        "how_it_works": (
            "Weather Spanish runs on hacer, not estar: Hace sol, Hace "
            "calor, Hace frio, Hace viento, Hace buen/mal tiempo - 'it "
            "makes' the weather. Rain and snow are verbs: llueve (it "
            "rains), nieva (it snows), graniza (it hails), with the "
            "present progressive for right now: Está lloviendo. Nature "
            "nouns carry their gender: el rio, la montaña, el bosque, la "
            "playa, el cielo, la luna, el sol, la estrella, el árbol, la "
            "flor. Animals take onomatopoeic verbs: el perro ladra, el "
            "gato maulla, el pájaro canta, la vaca muge. Seasons use en: "
            "en primavera, en verano, en otoño, en invierno. Small talk "
            "about weather opens with Que tiempo hace? (What is the "
            "weather like?)"
        ),
        "key_points": [
            "Weather uses hacer: Hace sol, Hace calor, Hace frio, Hace buen tiempo.",
            "Rain and snow are verbs: llueve, nieva; Está lloviendo means right now.",
            "Nature nouns with gender: el rio, la montaña, el bosque, la playa, la luna.",
            "Animals have their own verbs: ladra, maulla, canta, muge.",
            "Seasons use en: en primavera, en verano, en otoño, en invierno.",
        ],
        "requirements": [
            "Describe today's weather in five sentences using hacer, llueve/nieva, and hay.",
            "Write the four seasons with three nature sentences each.",
            "List ten animals with their Spanish verbs of sound or motion.",
            "Convert five weather statements to questions a traveler would ask.",
            "Forecast tomorrow's weather in six sentences using the future tense.",
        ],
        "standards": [
            "Weather constructions follow the Nueva gramatica de la lengua espanola.",
            "Nature vocabulary follows the Diccionario de la lengua espanola.",
            "The hacer + weather-noun pattern follows standard usage in the Diccionario panhispanico de dudas.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: nature is the oldest signed document - "
            "hace sol the daily oath of the sky, la luna llena the "
            "monthly seal. Where public vocabulary lists clouds, the "
            "Signature Word Method reads the weather as covenant: every "
            "season a signed chapter, every dawn a renewed promise."
        ),
    },
    {
        "key": "shopping_money",
        "name": "Spanish Shopping and Money Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about the market, prices, bargaining, and "
            "paying, each with English translation. 1. ¿Cuánto cuesta? "
            "(How much does it cost?) 2. Es muy caro. (It is very "
            "expensive.) 3. ¿Tienen descuento? (Do you have a discount?) "
            "4. Pago con tarjeta. (I am paying by card.) 5. Aceptan "
            "efectivo? (Do you accept cash?) 6. ¿Puedo probármelo? (Can I "
            "try it on?) 7. Busco una talla mediana. (I am looking for a "
            "medium size.) 8. La tienda abre a las diez. (The store opens "
            "at ten.) 9. Cierra los domingos. (It closes on Sundays.) "
            "10. Hay una oferta especial. (There is a special offer.) "
            "11. Me llevo dos. (I will take two.) 12. Tienen en otro "
            "color? (Do you have it in another color?) 13. El mercado es "
            "barato. (The market is cheap.) 14. Regateo el precio. (I "
            "haggle over the price.) 15. Necesito un recibo. (I need a "
            "receipt.) 16. El cambio está mal. (The change is wrong.) "
            "17. Ahorro dinero cada mes. (I save money every month.) "
            "18. El banco está cerrado. (The bank is closed.) 19. Retiro "
            "dinero del cajero. (I withdraw money from the ATM.) 20. Gasto "
            "poco en ropa. (I spend little on clothes.)"
        ),
        "how_it_works": (
            "Shopping runs on costar backwards like gustar: ¿Cuánto cuesta? "
            "¿Cuánto cuestan? - the items are the subject. Price adjectives "
            "agree: caro/cara, barato/barata. Sizes: talla for clothes "
            "(pequeña, mediana, grande), número for shoes (calzo el 38). "
            "Trying on is reflexive: probarse - ¿Puedo probármelo? Me lo "
            "pruebo. Payment verbs: pagar (pago con tarjeta / en efectivo), "
            "cobrar (to charge), devolver (to return), ahorrar (to save), "
            "gastar (to spend), retirar (to withdraw). Markets expect "
            "regatear; fixed-price stores do not. Hay opens availability "
            "(Hay una oferta), tener asks for it (¿Tienen descuento?). "
            "Money nouns: el dinero, el precio, el cambio, el recibo, la "
            "factura, el cajero automatico."
        ),
        "key_points": [
            "Costar works backwards: ¿Cuánto cuesta? / ¿Cuánto cuestan? - the items are the subject.",
            "Talla for clothes, número for shoes; probarse is reflexive: ¿Puedo probármelo?",
            "Pago con tarjeta / en efectivo; cobrar charges, devolver returns, ahorrar saves.",
            "Hay announces availability; Tienen...? asks the seller directly.",
            "Regatear belongs to markets; fixed-price stores take the tag price.",
        ],
        "requirements": [
            "Conjugate costar for one item, three items, and ask prices for ten goods.",
            "Role-play a full purchase: greet, ask price, try on, bargain, pay, request receipt.",
            "Write eight sentences with pagar, cobrar, devolver, ahorrar, gastar, retirar.",
            "Convert five price statements between caro/barato with correct agreement.",
            "Describe your monthly budget in eight sentences using ahorro, gasto, and necesito.",
        ],
        "standards": [
            "The costar construction follows the Nueva gramatica de la lengua espanola.",
            "Commercial vocabulary follows the Diccionario de la lengua espanola.",
            "Reflexive probarse follows the Nueva gramatica treatment of reflexives.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: trade is the covenant of value - cuanto "
            "cuesta the honest question, el cambio exacto the kept "
            "promise. Where public phrasebooks list prices, the Signature "
            "Word Method weighs the exchange: every coin a signed token, "
            "every bargain an oath negotiated in good faith."
        ),
    },
    {
        "key": "friendship",
        "name": "Spanish Friendship and Social Life Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about meeting people, invitations, and "
            "celebrations, each with English translation. 1. Quieres ser "
            "mi amigo? (Do you want to be my friend?) 2. Te invito a mi "
            "fiesta. (I invite you to my party.) 3. Ven a cenar el sábado. "
            "(Come have dinner on Saturday - command.) 4. Felicitaciones "
            "por tu ascenso. (Congratulations on your promotion.) 5. Lo "
            "siento mucho. (I am very sorry.) 6. ¿Nos tomamos un café? "
            "(Shall we have a coffee?) 7. Te presento a mi amiga Ana. (Let "
            "me introduce my friend Ana to you.) 8. Nos conocimos en la "
            "escuela. (We met at school.) 9. Salimos todos los viernes. "
            "(We go out every Friday.) 10. Celebramos su cumpleanos. (We "
            "celebrate his/her birthday.) 11. Me alegro de verte. (I am "
            "glad to see you.) 12. Cuentame todo. (Tell me everything - "
            "command.) 13. Te extrano. (I miss you.) 14. Nos divertimos "
            "mucho. (We have a great time.) 15. Somos amigos desde niños. "
            "(We have been friends since childhood.) 16. Perdona mi "
            "tardanza. (Forgive my lateness.) 17. Te apoyo siempre. (I "
            "support you always.) 18. Brindemos por la amistad. (Let us "
            "toast to friendship.) 19. Nos vemos pronto. (See you soon.) "
            "20. Eres un buen amigo. (You are a good friend.)"
        ),
        "how_it_works": (
            "Friendship Spanish runs on reflexives and the subjunctive of "
            "invitation. Conocerse marks first meeting (Nos conocimos en "
            "la escuela), divertirse marks shared fun (Nos divertimos "
            "mucho), alegrarse marks gladness (Me alegro de verte). "
            "Invitations use the command or the vamos a form: Ven a cenar, "
            "Vamos a tomar un café, Te invito a mi fiesta. Extranar takes "
            "a direct object: Te extrano, Los extrano. Celebrations stack "
            "formulas: Felicitaciones, Feliz cumpleanos, Brindemos por... "
            "Somos amigos desde niños shows desde + time for 'since.' "
            "Apologies scale: perdona (casual), disculpa (neutral), lo "
            "siento (deep). The social verbs - invitar, presentar, "
            "celebrar, brindar, apoyar - all take direct objects of "
            "people."
        ),
        "key_points": [
            "Reflexives mark social life: conocerse (meet), divertirse (have fun), alegrarse (be glad).",
            "Invitations use commands or vamos a: Ven a cenar, Vamos a tomar un café.",
            "Extranar takes a direct object: Te extrano (I miss you).",
            "Apologies scale: perdona (casual), disculpa (neutral), lo siento (deep).",
            "Desde marks 'since': Somos amigos desde niños.",
        ],
        "requirements": [
            "Conjugate conocerse, divertirse, and alegrarse in the present with all subjects.",
            "Invite someone three ways (command, vamos a, te invito) to three different events.",
            "Write congratulations, apology, and toast sentences for five occasions.",
            "Role-play meeting a new friend: introduce, exchange facts, plan to meet.",
            "Describe your oldest friendship in eight sentences using desde and reflexive verbs.",
        ],
        "standards": [
            "Reflexive social verbs follow the Nueva gramatica de la lengua espanola.",
            "Invitation formulas follow standard usage in the Diccionario panhispanico de dudas.",
            "Social vocabulary follows the Diccionario de la lengua espanola.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: friendship is the voluntary covenant - "
            "te invito the open seal, te extrano the ache of distance. "
            "Where public phrasebooks list parties, the Signature Word "
            "Method signs the bond: every amigo a chosen witness, every "
            "brindis an oath raised in company."
        ),
    },
    {
        "key": "technology",
        "name": "Spanish Technology and Communication Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about the phone, the internet, the computer, "
            "and messaging, each with English translation. 1. Mi teléfono "
            "no enciende. (My phone will not turn on.) 2. ¿Tienes wifi? "
            "(Do you have wifi?) 3. La contrasena es secreta. (The "
            "password is secret.) 4. Te mando un mensaje. (I am sending "
            "you a message.) 5. Llamame más tarde. (Call me later - "
            "command.) 6. Mi computadora es rapida. (My computer is fast; "
            "el ordenador in Spain.) 7. Navego por internet. (I browse the "
            "internet.) 8. Busco en el buscador. (I search on the search "
            "engine.) 9. Descargue la aplicacion. (I downloaded the app.) "
            "10. La bateria está baja. (The battery is low.) 11. Carga el "
            "teléfono. (Charge the phone - command.) 12. Hago clic en el "
            "enlace. (I click the link.) 13. La pantalla está rota. (The "
            "screen is broken.) 14. Enviame el archivo por correo. (Send "
            "me the file by email - command.) 15. Hice una videollamada. "
            "(I made a video call.) 16. Sigue mi canal. (Follow my channel "
            "- command.) 17. Publico una foto. (He/she posted a photo.) "
            "18. El programa se actualizo. (The program updated itself.) "
            "19. Apaga la computadora. (Turn off the computer - command.) "
            "20. Guardo todo en la nube. (I save everything in the cloud.)"
        ),
        "how_it_works": (
            "Technology Spanish borrows and adapts: el wifi, el clic, el "
            "enlace, la nube, la aplicacion (la app), el archivo, la "
            "pantalla, la contrasena. Regional split: Latin America says "
            "la computadora, Spain says el ordenador. Device verbs: "
            "encender/apagar (turn on/off), cargar (charge), descargar "
            "(download), actualizar (update), publicar (post), navegar "
            "(browse), hacer clic (click). Messaging verbs: mandar, "
            "enviar, llamar, with attached pronouns in commands: llámame, "
            "envíame, dímelo. Reflexive se marks automatic action: El "
            "programa se actualizo, La pantalla se rompio. Por marks the "
            "channel: por correo, por mensaje, por videollamada. Tech "
            "troubleshooting runs on no + verb: No enciende, No carga, No "
            "funciona."
        ),
        "key_points": [
            "Core tech nouns: el teléfono, la computadora/el ordenador, la pantalla, la contrasena, la nube, el enlace.",
            "Device verbs: encender/apagar, cargar, descargar, actualizar, publicar, navegar.",
            "Commands attach pronouns: llámame, envíame, dímelo.",
            "Se marks automatic action: El programa se actualizo.",
            "Por marks the channel: por correo, por mensaje, por videollamada.",
        ],
        "requirements": [
            "Troubleshoot a broken phone in eight sentences using no + verb and se.",
            "Give five tech commands with correctly attached pronouns.",
            "Explain the computadora/ordenador split and use each in a sentence.",
            "Write instructions for sending a file: six steps with commands.",
            "Describe your daily tech routine in eight sentences with present-tense verbs.",
        ],
        "standards": [
            "Technology vocabulary follows the Diccionario de la lengua espanola, including americanismos.",
            "Command pronoun attachment follows the Nueva gramatica, Morfologia.",
            "Reflexive automatic-action se follows the Nueva gramatica treatment of reflexives.",
        ],
        "citations": [CIT_RAE_DICT, CIT_RAE_GRAM],
        "sig_lens": (
            "The Signature read: the device is the newest covenant - "
            "llámame the voice across distance, guardo en la nube the "
            "memory sealed in the sky. Where public manuals list buttons, "
            "the Signature Word Method signs the signal: every message a "
            "sealed letter, every call an oath that distance cannot break."
        ),
    },
    {
        "key": "verb_tenses",
        "name": "Spanish Verb Tenses in Sentences",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Five tenses, five translated sentences each. PRESENT "
            "(routine, now): 1. Hablo español todos los días. (I speak "
            "Spanish every day.) 2. Comes verduras. (You eat vegetables.) "
            "3. Vivimos en México. (We live in México.) 4. Trabajan mucho. "
            "(They work a lot.) 5. Estudias por la noche. (You study at "
            "night.) PRETERITE (finished past): 6. Ayer hablé con María. "
            "(Yesterday I spoke with María.) 7. Comimos paella. (We ate "
            "paella.) 8. Vivio en Espana. (He/she lived in Spain.) "
            "9. Trabajaron ayer. (They worked yesterday.) 10. Estudiaste "
            "hasta tarde. (You studied until late.) IMPERFECT (ongoing "
            "past, habits): 11. Hablaba con mi abuela. (I used to talk "
            "with my grandmother.) 12. Comiamos juntos. (We used to eat "
            "together.) 13. Vivia en el campo. (He/she lived in the "
            "countryside.) 14. Trabajaban poco. (They used to work "
            "little.) 15. Estudiaba medicina. (I was studying medicine.) "
            "FUTURE (will): 16. Hablare mañana. (I will speak tomorrow.) "
            "17. Comeras bien. (You will eat well.) 18. Viviremos aquí. "
            "(We will live here.) 19. Trabajaran duro. (They will work "
            "hard.) 20. Estudiaras mucho. (You will study a lot.) "
            "CONDITIONAL (would): 21. Hablaria más. (I would speak more.) "
            "22. Comerias menos. (You would eat less.) 23. Viviriamos "
            "felices. (We would live happily.) 24. Trabajarian mejor. "
            "(They would work better.) 25. Estudiarias ahora. (You would "
            "study now.)"
        ),
        "how_it_works": (
            "Spanish builds tenses on the infinitive stem. Present swaps "
            "endings: -o, -as, -a, -amos, -ais, -an for -ar verbs. "
            "Preterite marks finished action: hable, hablaste, hablo, "
            "hablamos, hablasteis, hablaron - note hablo (I spoke) versus "
            "hablo (I speak), context decides. Imperfect marks ongoing or "
            "habitual past: hablaba, hablabas, hablaba, hablabamos, "
            "hablabais, hablaban - the 'used to' tense. Future adds "
            "endings to the whole infinitive: hablare, hablaras, hablara, "
            "hablaremos, hablareis, hablaran - the accent marks every "
            "form. Conditional adds its own set to the infinitive: "
            "hablaria, hablarias, hablaria, hablariamos, hablariais, "
            "hablarian. Preterite versus imperfect is the great divide: "
            "finished (Ayer llovio) against background (Llovia cuando "
            "sali). Ir a + infinitive (Voy a hablar) also expresses the "
            "future in speech."
        ),
        "key_points": [
            "Present: stem + person endings; the tense of routine and now.",
            "Preterite: finished past (Ayer hable); imperfect: ongoing/habitual past (Hablaba cada dia).",
            "Future and conditional attach to the whole infinitive: hablare, hablaria.",
            "Hablo (present) versus hablo (preterite) - identical spelling, context decides.",
            "Voy a hablar is the spoken future; hablare is the formal one.",
        ],
        "requirements": [
            "Conjugate hablar, comer, vivir in present, preterite, imperfect, future, conditional.",
            "Write ten sentence pairs contrasting preterite (finished) and imperfect (background).",
            "Convert five present sentences to future two ways (hablare and voy a hablar).",
            "Explain the hablo/hablo ambiguity with two disambiguating sentences.",
            "Narrate yesterday in ten sentences mixing preterite events and imperfect background.",
        ],
        "standards": [
            "Tense paradigms follow the Nueva gramatica de la lengua espanola, Morfologia.",
            "The preterite/imperfect distinction follows the Nueva gramatica treatment of aspect.",
            "Future and conditional formation follows the Real Academia Espanola conjugation models.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: tense is the seal of time - hable the "
            "sworn past, hablare the promised future, hablaria the "
            "honorable maybe. Where public grammar files paradigms, the "
            "Signature Word Method files testimonies: every ending a "
            "signed witness to when the action stood."
        ),
    },
    {
        "key": "questions_answers",
        "name": "Spanish Questions and Answers",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty question-and-answer pairs covering who, what, where, "
            "when, why, and how. 1. ¿Dónde vives? - Vivo en Madrid. (Where "
            "do you live? - I live in Madrid.) 2. ¿Cómo estás? - Estoy "
            "bien, gracias. (How are you? - I am fine, thanks.) 3. ¿Qué "
            "hora es? - Son las tres. (What time is it? - It is three "
            "o'clock.) 4. ¿Cuándo vienes? - Vengo mañana. (When are you "
            "coming? - I am coming tomorrow.) 5. ¿Por qué lloras? - Porque "
            "estoy triste. (Why are you crying? - Because I am sad.) "
            "6. ¿Quién es ella? - Es mi hermana. (Who is she? - She is my "
            "sister.) 7. ¿Cuál prefieres? - Prefiero el rojo. (Which do you "
            "prefer? - I prefer the red one.) 8. ¿Cuánto cuesta? - Cuesta "
            "diez euros. (How much is it? - It is ten euros.) 9. ¿Cómo te "
            "llamas? - Me llamo Carlos. (What is your name? - My name is "
            "Carlos.) 10. ¿De dónde eres? - Soy de México. (Where are you "
            "from? - I am from México.) 11. ¿Qué quieres comer? - Quiero "
            "pizza. (What do you want to eat? - I want pizza.) 12. ¿Hablas "
            "español? - Sí, hablo español. (Do you speak Spanish? - Yes, "
            "I speak Spanish.) 13. ¿Dónde está el baño? - Está a la "
            "derecha. (Where is the bathroom? - It is on the right.) "
            "14. ¿Cuántos años tienes? - Tengo treinta años. (How old are "
            "you? - I am thirty.) 15. ¿A qué hora sales? - Salgo a las "
            "ocho. (At what time do you leave? - I leave at eight.) "
            "16. ¿Por qué estudias español? - Porque me encanta. (Why do "
            "you study Spanish? - Because I love it.) 17. ¿Qué día es hoy? "
            "- Hoy es sábado. (What day is today? - Today is Saturday.) "
            "18. ¿Vienes conmigo? - Sí, voy contigo. (Are you coming with "
            "me? - Yes, I am coming with you.) 19. ¿Cómo se dice 'house'? "
            "- Se dice 'casa'. (How do you say 'house'? - You say 'casa'.) "
            "20. ¿Qué haces? - Leo un libro. (What are you doing? - I am "
            "reading a book.)"
        ),
        "how_it_works": (
            "Question words carry written accents to separate them from "
            "their twin conjunctions: qué (what?) versus que (that), cómo "
            "(how?) versus como (like), dónde (where?) versus donde "
            "(where). Qué asks for definitions and identifications; cuál "
            "asks for a choice among options (¿Cuál prefieres? - which of "
            "these?). Por qué (two words) asks why; porque (one word) "
            "answers because. Cuánto agrees with its noun: cuánto dinero, "
            "cuánta gente, cuántos años. Yes-no questions need only "
            "intonation and the inverted marks: ¿Hablas español? Answers "
            "mirror the question's verb: ¿Dónde vives? - Vivo en Madrid. "
            "¿Cómo se dice...? is the learner's master key - it asks the "
            "language about itself."
        ),
        "key_points": [
            "Question words take written accents: qué, cómo, dónde, cuándo, cuál, quién, cuánto.",
            "Qué identifies; cuál chooses among options; por qué asks, porque answers.",
            "Cuánto agrees with its noun: cuánto dinero, cuánta gente, cuántos años.",
            "Yes-no questions need only intonation plus inverted marks - no helper verb.",
            "¿Cómo se dice...? is the master key: it asks the language about itself.",
        ],
        "requirements": [
            "Write twenty questions, one per question word, each with a full answer.",
            "Explain five que/cual choices with the identification-versus-selection rule.",
            "Convert ten statements to yes-no questions and answer them fully.",
            "Build a five-question interview using por que and answer with porque.",
            "Ask for ten English words in Spanish using Como se dice and record the answers.",
        ],
        "standards": [
            "Interrogative accentuation follows the Ortografia de la lengua espanola 2010.",
            "The que/cual distinction follows the Diccionario panhispanico de dudas.",
            "Question formation follows the Nueva gramatica de la lengua espanola, Sintaxis.",
        ],
        "citations": [CIT_RAE_ORT, CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: the question is the open seal - que the "
            "demand for truth, porque the sworn reason. Where public "
            "grammar files interrogatives, the Signature Word Method "
            "files inquests: every question a signed summons, every "
            "answer a testimony given."
        ),
    },
    {
        "key": "commands",
        "name": "Spanish Commands and Requests",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty imperative and polite-request sentences, formal versus "
            "informal. INFORMAL TU COMMANDS (to friends, family, "
            "children): 1. Habla más despacio. (Speak more slowly.) "
            "2. Come tus verduras. (Eat your vegetables.) 3. Ven aquí. "
            "(Come here - irregular.) 4. Dime la verdad. (Tell me the "
            "truth - irregular.) 5. Haz tu tarea. (Do your homework - "
            "irregular.) 6. Pon la mesa. (Set the table - irregular.) "
            "7. Sal temprano. (Leave early - irregular.) 8. Ten cuidado. "
            "(Be careful - irregular.) 9. Sé bueno. (Be good - irregular.) "
            "10. Ve a la cama. (Go to bed - irregular.) FORMAL USTED "
            "COMMANDS (to elders, officials, strangers): 11. Hable más "
            "despacio, por favor. (Speak more slowly, please.) 12. "
            "Sientese aquí. (Sit down here.) 13. Digame su nombre. (Tell "
            "me your name.) NOSOTROS (let us): 14. Comamos juntos. (Let us "
            "eat together.) 15. Vamos a la playa. (Let us go to the "
            "beach.) NEGATIVES: 16. No hables tan alto. (Do not speak so "
            "loudly.) 17. No comas eso. (Do not eat that.) POLITE "
            "REQUESTS: 18. ¿Puedes ayudarme? (Can you help me?) 19. Me pasas "
            "la sal, por favor? (Will you pass me the salt, please?) "
            "20. ¿Podría hablar con el gerente? (Could I speak with the "
            "manager? - formal.)"
        ),
        "how_it_works": (
            "The affirmative tu command is the third-person present form: "
            "habla, come, escribe - with eight famous irregulars: di "
            "(decir), haz (hacer), ve (ir), pon (poner), sal (salir), se "
            "(ser), ten (tener), ven (venir). Pronouns attach to the end: "
            "dime, siéntate, pásame. Negative commands switch to the "
            "subjunctive and put no first: No hables, No comas, No me "
            "digas. Usted commands are the subjunctive too, formal by "
            "nature: hable, coma, siéntese, dígame. Nosotros commands "
            "propose shared action: comamos, hablemos - though Vamos a + "
            "infinitive (Vamos a comer) is more common in speech. Polite "
            "requests soften with questions: Puedes...?, Podria...?, Me "
            "pasas...?, or the conditional: Me pasarias la sal? The "
            "command's sharpness is always cushioned by por favor."
        ),
        "key_points": [
            "Affirmative tu commands: habla, come, escribe - with eight irregulars: di, haz, ve, pon, sal, se, ten, ven.",
            "Pronouns attach to affirmative commands: dime, siéntate, pásame.",
            "Negative commands use no + subjunctive: No hables, No comas.",
            "Usted commands are subjunctive and formal: Hable, Sientese, Digame.",
            "Polite requests are questions: Puedes...?, Podria...?, Me pasas...?",
        ],
        "requirements": [
            "Write the eight irregular tu commands with their infinitives from memory.",
            "Convert ten affirmative commands to negative, switching to the subjunctive.",
            "Convert ten tu commands to usted, attaching pronouns correctly.",
            "Give five instructions with attached pronouns (dime, hazlo, siéntate).",
            "Make five polite requests two ways: question form and conditional form.",
        ],
        "standards": [
            "Command paradigms follow the Nueva gramatica de la lengua espanola, Morfologia.",
            "Pronoun attachment follows the Ortografia de la lengua espanola 2010.",
            "The eight irregular imperatives follow the Real Academia Espanola conjugation models.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_ORT, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: the command is the sealed order - habla "
            "the direct oath, no hables the sworn restraint. Where public "
            "grammar files moods, the Signature Word Method files "
            "authority: every imperative a signed directive, every por "
            "favor the seal of grace upon it."
        ),
    },
    {
        "key": "descriptions",
        "name": "Spanish Descriptions of People and Places",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences describing people, places, and things in "
            "detail, each with English translation. 1. Mi madre es alta y "
            "amable. (My mother is tall and kind.) 2. Madrid es una ciudad "
            "vibrante. (Madrid is a vibrant city.) 3. El libro es largo "
            "pero interesante. (The book is long but interesting.) 4. Su "
            "casa tiene un jardin hermoso. (His/her house has a beautiful "
            "garden.) 5. El profesor es paciente y sabio. (The teacher is "
            "patient and wise.) 6. La playa de Cancun tiene agua turquesa. "
            "(The beach at Cancun has turquoise water.) 7. Mi perro es "
            "pequeño y jugueton. (My dog is small and playful.) 8. La "
            "catedral es antigua e impresionante. (The cathedral is old "
            "and impressive.) 9. Ella tiene ojos verdes. (She has green "
            "eyes.) 10. El café está caliente y aromatico. (The coffee is "
            "hot and aromatic.) 11. Barcelona combina historia y "
            "modernidad. (Barcelona combines history and modernity.) "
            "12. Mi abuelo tiene manos fuertes. (My grandfather has strong "
            "hands.) 13. La novela tiene trescientas páginas. (The novel "
            "has three hundred pages.) 14. El parque está lleno de flores. "
            "(The park is full of flowers.) 15. Su voz es suave y clara. "
            "(His/her voice is soft and clear.) 16. El restaurante sirve "
            "comida deliciosa. (The restaurant serves delicious food.) "
            "17. La montaña se ve majestuosa. (The mountain looks "
            "majestic.) 18. Mi cuarto es pequeño pero acogedor. (My room "
            "is small but cozy.) 19. El niño lleva una camisa roja. (The "
            "boy is wearing a red shirt.) 20. La noche está estrellada y "
            "tranquila. (The night is starry and calm.)"
        ),
        "how_it_works": (
            "Descriptions stack three tools: ser for traits (es alta, es "
            "paciente), estar for states and appearances (está caliente, "
            "está estrellada, se ve majestuosa), and tener for features "
            "the body or object 'has' (tiene ojos verdes, tiene "
            "trescientas páginas). Adjectives follow the noun and agree: "
            "una ciudad vibrante, agua turquesa, manos fuertes. Pero joins "
            "contrasts (largo pero interesante, pequeño pero acogedor); y "
            "joins companions (alta y amable, suave y clara); e replaces y "
            "before i (antigua e impresionante). Llevar means 'to wear' "
            "(lleva una camisa roja). Numbers agree: trescientas páginas. "
            "The description sentence is the portrait: subject, ser/estar/"
            "tener, then the adjectives in agreeing procession."
        ),
        "key_points": [
            "Ser describes traits (es alta); estar describes states (está caliente); tener lists features (tiene ojos verdes).",
            "Adjectives follow the noun and agree: una ciudad vibrante, manos fuertes, trescientas páginas.",
            "Pero contrasts, y joins, e replaces y before i: antigua e impresionante.",
            "Llevar means to wear: El niño lleva una camisa roja.",
            "Se ve + adjective renders 'looks': La montaña se ve majestuosa.",
        ],
        "requirements": [
            "Describe three people, three places, and three things in four sentences each.",
            "Label every ser/estar/tener in the 20 sentences with justifications.",
            "Convert five descriptions to the opposite gender, fixing all agreements.",
            "Build five pero-contrast descriptions and five y-companion descriptions.",
            "Describe your hometown in ten sentences using all three description tools.",
        ],
        "standards": [
            "Description patterns follow the Nueva gramatica de la lengua espanola, Sintaxis.",
            "Adjective agreement follows the Nueva gramatica treatment of concordance.",
            "Descriptive vocabulary follows the Diccionario de la lengua espanola.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: description is the portrait sealed in "
            "words - es alta the sworn trait, está estrellada the "
            "witnessed state. Where public grammar files adjectives, the "
            "Signature Word Method paints in oaths: every detail a signed "
            "stroke, every portrait true to its subject."
        ),
    },
    {
        "key": "story1",
        "name": "Spanish Story I: A Simple Day",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the present tense - Un dia en la "
            "vida de Ana (A Day in the Life of Ana) - with line-by-line "
            "English translation. 1. Me llamo Ana y vivo en Sevilla. (My "
            "name is Ana and I live in Seville.) 2. Cada mañana me "
            "despierto a las siete. (Every morning I wake up at seven.) "
            "3. Desayuno tostadas con café. (I have toast with coffee for "
            "breakfast.) 4. Camino al trabajo por el parque. (I walk to "
            "work through the park.) 5. Trabajo en una libreria pequeña. "
            "(I work in a small bookstore.) 6. Al mediodía como con mis "
            "amigas. (At midday I eat with my friends, female.) 7. Por la "
            "tarde leo libros nuevos. (In the afternoon I read new books.) "
            "8. A las seis vuelvo a casa. (At six I return home.) 9. Ceno "
            "con mi familia y hablamos. (I have dinner with my family and "
            "we talk.) 10. Me acuesto a las once, feliz. (I go to bed at "
            "eleven, happy.)"
        ),
        "how_it_works": (
            "This story runs entirely in the present tense, the tense of "
            "routine: me despierto, desayuno, camino, trabajo, como, leo, "
            "vuelvo, ceno, hablamos, me acuesto. Reflexives mark the "
            "personal rituals: me llamo, me despierto, me acuesto - "
            "morning and night sealed by the self. Time expressions "
            "anchor each line: cada mañana, al mediodía, por la tarde, a "
            "las seis, a las once. Por marks the route (por el parque); "
            "con marks company (con mis amigas, con mi familia). The story "
            "arc is a day: waking, breakfast, journey, work, lunch, "
            "afternoon, return, dinner, sleep. Read it aloud three times: "
            "first for meaning, second for the verb endings, third for "
            "speed - then retell it as your own day."
        ),
        "key_points": [
            "The present tense carries routine: me despierto, trabajo, ceno - a day on repeat.",
            "Reflexives seal personal rituals: me llamo, me despierto, me acuesto.",
            "Time anchors: cada mañana, al mediodía, por la tarde, a las seis, a las once.",
            "Por marks the route (por el parque); con marks company (con mi familia).",
            "The arc is a day: waking, journey, work, return, sleep - retell it as your own.",
        ],
        "requirements": [
            "Read the story aloud and translate each line without looking.",
            "Retell the story as your own day, changing names, places, and times.",
            "Conjugate every verb in the story with all six subjects.",
            "Write a ten-sentence present-tense story about your yesterday-as-routine.",
            "Record yourself reading the story and mark every reflexive verb.",
        ],
        "standards": [
            "Narrative present follows the Nueva gramatica de la lengua espanola.",
            "Reflexive verbs follow the Nueva gramatica treatment of reflexives.",
            "Time expressions follow standard usage in the Diccionario panhispanico de dudas.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: the day is a covenant renewed each "
            "dawn - me despierto the morning seal, me acuesto the night's "
            "signature. Where public readers parse verbs, the Signature "
            "Word Method keeps the hours: every routine a sworn rhythm, "
            "every day a signed page."
        ),
    },
    {
        "key": "story2",
        "name": "Spanish Story II: Yesterday",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the past tenses - Ayer (Yesterday) - "
            "with line-by-line English translation. 1. Ayer fue un dia "
            "especial. (Yesterday was a special day.) 2. Me desperte "
            "temprano. (I woke up early.) 3. Desayune con mi abuela. (I "
            "had breakfast with my grandmother.) 4. Caminamos por el "
            "mercado. (We walked through the market.) 5. Compre flores "
            "amarillas. (I bought yellow flowers.) 6. Comimos paella en un "
            "restaurante. (We ate paella at a restaurant.) 7. Por la tarde "
            "visité a mis primos. (In the afternoon I visited my cousins.) "
            "8. Jugamos a las cartas. (We played cards.) 9. Volvi a casa "
            "al atardecer. (I returned home at sunset.) 10. Me dormi "
            "contenta. (I fell asleep content, feminine speaker.)"
        ),
        "how_it_works": (
            "This story mixes the two pasts: the preterite for finished "
            "events (fue, me desperte, desayune, caminamos, compre, "
            "comimos, visite, jugamos, volvi, me dormi) - every line a "
            "completed bead on the day's string. Time markers open the "
            "frames: ayer, por la tarde, al atardecer. Por marks passage "
            "through (por el mercado); en marks location (en un "
            "restaurante). The personal a appears before people: visite a "
            "mis primos. Contenta agrees with the feminine speaker - the "
            "storyteller signs her own gender into the final line. "
            "Contrast with Story I: same day-arc, but sealed in the past. "
            "Retell it changing the events, keeping the preterite spine."
        ),
        "key_points": [
            "The preterite seals finished events: fue, compre, comimos, volvi - beads on the day's string.",
            "Time frames: ayer, por la tarde, al atardecer - each line anchored.",
            "The personal a marks people as objects: visité a mis primos.",
            "Contenta signs the speaker's gender into the final line.",
            "Same day-arc as Story I, sealed in the past - compare the two spines.",
        ],
        "requirements": [
            "Conjugate every verb in the story in the preterite with all six subjects.",
            "Retell your own yesterday in ten preterite sentences.",
            "Explain the personal a in sentence 7 and add three more examples.",
            "Convert Story I's present-tense day into the preterite, line by line.",
            "Write ten new preterite sentences using ayer, anoche, and la semana pasada.",
        ],
        "standards": [
            "Preterite paradigms follow the Nueva gramatica de la lengua espanola, Morfologia.",
            "The personal a follows the Nueva gramatica treatment of direct objects.",
            "Narrative preterite follows the Nueva gramatica treatment of aspect.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: yesterday is the sealed archive - fue "
            "the sworn fact, compre the kept receipt. Where public "
            "readers note the preterite, the Signature Word Method files "
            "testimony: every finished action a signed record, every "
            "memory an oath the past cannot unsay."
        ),
    },
    {
        "key": "story3",
        "name": "Spanish Story III: Tomorrow",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the future and conditional - Manana "
            "(Tomorrow) - with line-by-line English translation. 1. Manana "
            "sera un gran dia. (Tomorrow will be a great day.) 2. Me "
            "despertare a las seis. (I will wake up at six.) 3. Viajare a "
            "Granada en tren. (I will travel to Granada by train.) "
            "4. Visitare la Alhambra. (I will visit the Alhambra.) "
            "5. Comere tapas famosas. (I will eat famous tapas.) 6. Por la "
            "tarde paseare por el Albaicin. (In the afternoon I will "
            "stroll through the Albaicin.) 7. Tomare muchas fotos. (I "
            "will take many photos.) 8. Cenare con viejos amigos. (I will "
            "have dinner with old friends.) 9. Volvere de noche, cansado "
            "pero feliz. (I will return at night, tired but happy.) "
            "10. Si tuviera más tiempo, me quedaria una semana. (If I had "
            "more time, I would stay a week.)"
        ),
        "how_it_works": (
            "The future attaches endings to the whole infinitive: sera, "
            "despertare, viajare, visitare, comere, paseare, tomare, "
            "cenare, volvere - every form accented, every promise sealed. "
            "En marks the vehicle (en tren); por marks passage (por el "
            "Albaicin); de noche marks the hour of return. The final "
            "sentence opens the conditional: si + imperfect subjunctive "
            "(tuviera) in the condition, conditional (me quedaria) in the "
            "result - the grammar of wishing. Cansado pero feliz shows "
            "the agreeing pair closing the day. Contrast the trilogy: "
            "Story I promises routine (present), Story II testifies "
            "(preterite), Story III vows (future). Retell it as your own "
            "tomorrow."
        ),
        "key_points": [
            "The future seals promises: sera, viajare, cenare - endings on the whole infinitive.",
            "En marks the vehicle (en tren); por marks passage (por el Albaicin).",
            "Si + imperfect subjunctive + conditional is the grammar of wishing: Si tuviera..., me quedaria.",
            "Cansado pero feliz: the agreeing pair that closes the day.",
            "The trilogy: Story I routine (present), Story II testimony (preterite), Story III vow (future).",
        ],
        "requirements": [
            "Conjugate the nine future verbs with all six subjects.",
            "Write your own tomorrow in ten future sentences.",
            "Build five si-clause wishes with imperfect subjunctive + conditional.",
            "Convert Story II's past day into the future, line by line.",
            "Explain the tuviera/me quedaria pairing with three new examples.",
        ],
        "standards": [
            "Future and conditional paradigms follow the Nueva gramatica de la lengua espanola, Morfologia.",
            "The si-clause construction follows the Nueva gramatica treatment of conditionals.",
            "Narrative future follows the Nueva gramatica treatment of tense.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: tomorrow is the unsealed covenant - "
            "viajare the vow, me quedaria the honorable wish. Where "
            "public readers conjugate the future, the Signature Word "
            "Method signs intentions: every will a promise witnessed, "
            "every would a dream given its proper seal."
        ),
    },
    {
        "key": "idioms",
        "name": "Spanish Idioms and Proverbs",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty idioms and proverbs, each with literal translation, "
            "real meaning, and an example sentence. 1. Estar en las nubes "
            "- lit. to be in the clouds; to be daydreaming. Deja de estar "
            "en las nubes y atiende. (Stop daydreaming and pay attention.) "
            "2. Tirar la casa por la ventana - lit. to throw the house "
            "out the window; to spare no expense. Para la boda tiraron la "
            "casa por la ventana. 3. Costar un ojo de la cara - lit. to "
            "cost an eye from the face; to cost an arm and a leg. El coche "
            "me costo un ojo de la cara. 4. Estar como una cabra - lit. "
            "to be like a goat; to be crazy. Estas como una cabra! "
            "5. Meter la pata - lit. to put the paw in; to put one's foot "
            "in it. Meti la pata en la reunión. 6. No tener pelos en la "
            "lengua - lit. to have no hairs on the tongue; to be blunt. "
            "Ella no tiene pelos en la lengua. 7. Ser pan comido - lit. to "
            "be eaten bread; to be a piece of cake. El examen fue pan "
            "comido. 8. Estar hasta las narices - lit. to be up to the "
            "nostrils; to be fed up. Estoy hasta las narices del trafico. "
            "9. Ponerse las pilas - lit. to put in the batteries; to get "
            "one's act together. Ponte las pilas o repites. 10. Hablar por "
            "los codos - lit. to talk through the elbows; to talk nonstop. "
            "Habla por los codos sin parar. 11. Tomar el pelo - lit. to "
            "take the hair; to tease, to pull one's leg. Me estas tomando "
            "el pelo! 12. Echar una mano - lit. to throw a hand; to lend "
            "a hand. Echame una mano con esto. 13. Estar hecho polvo - "
            "lit. to be made dust; to be exhausted. Estoy hecho polvo. "
            "14. Dar en el clavo - lit. to hit the nail on the head; "
            "exactly right. Diste en el clavo con tu respuesta. 15. No ver "
            "tres en un burro - lit. not to see three on a donkey; to be "
            "blind as a bat. Sin gafas no veo tres en un burro. 16. Ser la "
            "oveja negra - lit. to be the black sheep; the family "
            "outsider. Es la oveja negra de la familia. 17. Poner el grito "
            "en el cielo - lit. to put the shout in the sky; to complain "
            "loudly. Puso el grito en el cielo por la cuenta. 18. Tener "
            "la sarten por el mango - lit. to hold the pan by the handle; "
            "to call the shots. Ella tiene la sarten por el mango. "
            "19. Quedarse de piedra - lit. to stay like stone; to be "
            "stunned. Me quede de piedra con la noticia. 20. A caballo "
            "regalado no le mires el diente - lit. do not look at the "
            "tooth of a gifted horse; do not look a gift horse in the "
            "mouth (proverb). Acepta el regalo sin quejarte."
        ),
        "how_it_works": (
            "Idioms are frozen metaphors: the literal picture (goat, "
            "dust, batteries) carries a meaning no word-by-word "
            "translation reaches. Estar-idioms describe states (estar en "
            "las nubes, estar hecho polvo); tener-idioms describe "
            "control or lack (no tener pelos en la lengua, tener la "
            "sarten por el mango); ponerse-idioms describe change "
            "(ponerse las pilas). The proverb (refran) at the end shows "
            "the moral form: timeless, rhyming, and cited as wisdom, not "
            "opinion. Learn idioms in families - body idioms (ojo, pelo, "
            "narices, codos), animal idioms (cabra, burro, oveja) - and "
            "always with the example sentence, because the sentence is "
            "where the metaphor lives."
        ),
        "key_points": [
            "Idioms are frozen metaphors: translate the meaning, never the words.",
            "Estar-idioms describe states; tener-idioms describe control; ponerse-idioms describe change.",
            "Learn idioms in families: body parts, animals, food - the metaphor repeats.",
            "The refran (proverb) carries moral weight: A caballo regalado no le mires el diente.",
            "Every idiom above lives in an example sentence - that is where the metaphor breathes.",
        ],
        "requirements": [
            "Explain all 20 idioms' real meanings without looking at the list.",
            "Sort the 20 into estar, tener, ponerse, and other-verb families.",
            "Write ten new sentences using idioms in fitting situations.",
            "Match ten literal translations to their real meanings from memory.",
            "Collect five more refranes and gloss each literally and really.",
        ],
        "standards": [
            "Idiom glosses follow the Diccionario de la lengua espanola and the Diccionario panhispanico de dudas.",
            "Refranes follow the Real Academia Espanola paremiological collections.",
            "Usage notes follow the Nueva gramatica treatment of fixed expressions.",
        ],
        "citations": [CIT_RAE_DICT, CIT_RAE_GRAM],
        "sig_lens": (
            "The Signature read: the idiom is the people's sealed wisdom "
            "- pan comido the oath that difficulty is bread already "
            "eaten, la sarten por el mango the grip of command. Where "
            "public dictionaries file phrases, the Signature Word Method "
            "keeps the folk covenant: every refran a signed law of the "
            "street."
        ),
    },
    {
        "key": "registers",
        "name": "Spanish Formal and Polite Registers",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen formal-versus-informal pairs for letters, business, "
            "and elders, each with translation. 1. ¿Cómo estás? (How are "
            "you?, informal.) / ¿Cómo está usted? (How are you?, formal.) "
            "2. ¿Puedes ayudarme? (Can you help me?, informal.) / Podria "
            "ayudarme? (Could you help me?, formal.) 3. Gracias por tu "
            "ayuda. (Thanks for your help, informal.) / Gracias por su "
            "ayuda. (formal.) 4. Dime tu nombre. (Tell me your name, "
            "informal.) / Digame su nombre. (formal.) 5. Sientate aquí. "
            "(Sit here, informal.) / Sientese aquí. (formal.) 6. Tienes "
            "hora? (Do you have the time?, informal.) / ¿Tiene hora? "
            "(formal.) 7. Te llamo mañana. (I will call you tomorrow, "
            "informal.) / Le llamo mañana. (formal.) 8. Tu casa es bonita. "
            "(Your house is pretty, informal.) / Su casa es bonita. "
            "(formal.) 9. Perdona el retraso. (Sorry for the delay, "
            "informal.) / Disculpe el retraso. (formal.) 10. Hasta luego! "
            "(See you!, informal.) / Ha sido un placer. (It has been a "
            "pleasure., formal farewell.) 11. Querido Juan: (Dear Juan, "
            "informal letter.) / Estimado señor García: (Dear Mr. García, "
            "formal letter.) 12. Un abrazo, (Hugs - informal closing.) / "
            "Atentamente, (Sincerely - formal closing.) 13. ¿Qué quieres? "
            "(What do you want?, informal.) / ¿Qué desea? (What would you "
            "like?, formal.) 14. Ven conmigo. (Come with me, informal.) / "
            "Acompaneme, por favor. (Accompany me, please - formal.) "
            "15. Eres muy amable. (You are very kind, informal.) / Es "
            "usted muy amable. (formal.)"
        ),
        "how_it_works": (
            "Register is chosen before the first word: tu-forms for "
            "friends, family, children, and peers; usted-forms for elders, "
            "officials, clients, and strangers in formal settings. The "
            "switch changes verbs (puedes/podria, tienes/tiene, dime/"
            "dígame), pronouns (te/le, tu/su), and possessives (tu/su). "
            "Politeness softens further with the conditional (Podria...?, "
            "¿Qué desea?) and with por favor placed after the request. "
            "Letters open Querido/a for intimates and Estimado/a señor/a "
            "for formal address; they close Un abrazo or Saludos among "
            "friends and Atentamente or Cordialmente in business. Mixing "
            "registers mid-conversation signals either intimacy earned or "
            "respect lost - hold the line until invited across it."
        ),
        "key_points": [
            "Tu for friends, family, peers; usted for elders, officials, clients, formal strangers.",
            "The switch changes verbs, pronouns, and possessives: puedes/podria, te/le, tu/su.",
            "The conditional softens requests: ¿Podría ayudarme? ¿Qué desea?",
            "Letters: Querido/a (intimate) versus Estimado/a señor/a (formal); Un abrazo versus Atentamente.",
            "Hold the register until invited across - mixing mid-conversation sends a signal.",
        ],
        "requirements": [
            "Convert ten informal sentences to formal, changing verbs, pronouns, and possessives.",
            "Write a formal business letter: opening, three paragraphs, formal closing.",
            "Write an informal letter to a friend with matching intimate forms.",
            "Role-play a store: clerk formal, customer informal, then swap.",
            "List ten situations and assign tu or usted with one-line reasons.",
        ],
        "standards": [
            "The tu/usted distribution follows the Diccionario panhispanico de dudas.",
            "Letter formulas follow the Diccionario panhispanico de dudas usage notes.",
            "Polite conditional requests follow the Nueva gramatica de la lengua espanola.",
        ],
        "citations": [CIT_RAE_DICT, CIT_RAE_GRAM],
        "sig_lens": (
            "The Signature read: register is the seal of respect - usted "
            "the bow, tu the embrace, each sworn before the first word. "
            "Where public etiquette files rules, the Signature Word "
            "Method files reverence: every formal phrase a signed honor, "
            "every usted a covenant of courtesy."
        ),
    },
    {
        "key": "complex",
        "name": "Spanish Compound and Complex Sentences",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen long sentences with clauses, connectors, and "
            "relative clauses - parsed and translated. 1. Aunque llueve, "
            "salimos a caminar porque nos encanta la lluvia. (Although it "
            "rains, we go out walking because we love the rain. - "
            "concessive + causal.) 2. Cuando llegues, llámame para que "
            "sepa que estas bien. (When you arrive, call me so that I "
            "know you are fine. - temporal + purpose.) 3. El libro que me "
            "prestaste es el que más me ha gustado. (The book you lent me "
            "is the one I liked most. - relative clauses.) 4. Si estudias "
            "todos los días, aprobaras el examen sin problema. (If you "
            "study every day, you will pass the exam easily. - "
            "conditional.) 5. Trabaja tanto que no tiene tiempo para su "
            "familia. (He works so much that he has no time for his "
            "family. - consecutive.) 6. Mientras cocinaba, escuchaba "
            "música y pensaba en el viaje. (While I cooked, I listened to "
            "music and thought about the trip. - temporal, imperfect "
            "background.) 7. No solo habla español, sino que también "
            "habla portugués. (He not only speaks Spanish but also "
            "Portuguese. - correlative.) 8. Le dije que viniera temprano "
            "porque la reunión empieza a las ocho. (I told him to come "
            "early because the meeting starts at eight. - noun clause + "
            "causal.) 9. Por más que lo intenta, no consigue dormirse "
            "antes de medianoche. (However much he tries, he cannot fall "
            "asleep before midnight. - concessive.) 10. Despues de que "
            "terminemos, iremos a celebrar con los amigos. (After we "
            "finish, we will go celebrate with friends. - temporal.) "
            "11. Es importante que practiques cada dia para que progreses "
            "rápido. (It is important that you practice daily so you "
            "progress fast. - impersonal + purpose.) 12. La casa donde "
            "creci ya no existe, pero la recuerdo bien. (The house where "
            "I grew up no longer exists, but I remember it well. - "
            "relative + adversative.) 13. Como no tenia dinero, se quedo "
            "en casa todo el fin de semana. (Since he had no money, he "
            "stayed home all weekend. - causal.) 14. Habla tan despacio "
            "que todos entienden cada palabra. (He speaks so slowly that "
            "everyone understands every word. - consecutive.) 15. Ni "
            "estudia ni trabaja, aunque tiene dos titulos. (He neither "
            "studies nor works, although he has two degrees. - correlative "
            "negative + concessive.)"
        ),
        "how_it_works": (
            "Complex sentences join clauses with connectors that also "
            "choose the mood. Indicative connectors state facts: porque, "
            "cuando (habitual), mientras, pero, sino que. Subjunctive "
            "connectors mark purpose, concession, and unreality: para que "
            "(always subjunctive), aunque (subjunctive when conceded, "
            "indicative when factual), cuando (future reference), antes de "
            "que, sin que. Relative clauses use que (the book that), "
            "donde (the house where), lo que (what/that which). "
            "Consecutive tan/tanto...que and correlative no solo...sino "
            "frame paired ideas; ni...ni negates pairs. Parse inside-out: "
            "find the main verb, name each connector, check the mood it "
            "demands, and translate clause by clause."
        ),
        "key_points": [
            "Connectors choose the mood: para que always takes the subjunctive; porque takes the indicative.",
            "Aunque takes the subjunctive for conceded facts, the indicative for admitted facts.",
            "Relative clauses: que (that), donde (where), lo que (what/that which).",
            "Tan/tanto...que frames consequence; no solo...sino frames addition; ni...ni negates pairs.",
            "Parse inside-out: main verb, connector, mood check, clause-by-clause translation.",
        ],
        "requirements": [
            "Parse all 15 sentences: label each clause and name each connector's mood.",
            "Build five para que sentences and five porque sentences with correct moods.",
            "Write five aunque sentences - three conceded (subjunctive), two admitted (indicative).",
            "Combine ten simple-sentence pairs using relatives, consecutives, and correlatives.",
            "Translate five English complex sentences, choosing each connector and mood deliberately.",
        ],
        "standards": [
            "Connector-mood pairings follow the Nueva gramatica de la lengua espanola, Sintaxis.",
            "Subjunctive usage follows the Nueva gramatica treatment of mood.",
            "Relative clauses follow the Nueva gramatica treatment of subordination.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: the complex sentence is the covenant "
            "with many seals - cada que a clause sworn, cada para que a "
            "purpose sealed in the subjunctive. Where public syntax draws "
            "trees, the Signature Word Method raises cathedrals: every "
            "connector an arch, every clause a sworn stone."
        ),
    },
    {
        "key": "conv_market",
        "name": "Spanish Conversation: At the Market",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue at the market, annotated. "
            "María is the vendor; Carlos the customer. 1. María: ¡Buenos días! ¿Qué busca hoy? (Good morning! What are you looking for "
            "today? - greeting + question.) 2. Carlos: Buenos días. Busco "
            "tomates y aguacates. (Good morning. I am looking for tomatoes "
            "and avocados.) 3. María: Los tomates están a dos euros el "
            "kilo. (The tomatoes are two euros a kilo. - price with "
            "estar.) 4. Carlos: Están caros. ¿Me deja tres kilos por cinco euros? (They are expensive. Will you give me three kilos for "
            "five euros? - bargaining.) 5. María: Por cinco euros le doy "
            "dos kilos y medio. (For five euros I will give you two and a "
            "half kilos. - counteroffer.) 6. Carlos: Trato hecho. ¿Y los aguacates? (Deal. And the avocados?) 7. María: A uno cincuenta "
            "cada uno, bien maduros. (One fifty each, nice and ripe.) "
            "8. Carlos: Me llevo cuatro. ¿Están blandos? (I will take "
            "four. Are they soft? - ripeness check.) 9. María: Perfectos "
            "para hoy. Toquelos. (Perfect for today. Touch them. - "
            "command.) 10. Carlos: Tiene razon. Pongame también un manojo "
            "de cilantro. (You are right. Give me a bunch of cilantro "
            "too.) 11. María: Marchando. ¿Algo más? (Coming up. Anything "
            "else?) 12. Carlos: Eso es todo. ¿Cuánto es? (That is all. How "
            "much is it?) 13. María: Son ocho euros con cincuenta. (It is "
            "eight fifty. - plural because the total exceeds one.) "
            "14. Carlos: Pago con tarjeta. (I am paying by card.) "
            "15. María: Perfecto. Aquí tiene su cambio... digo, su "
            "recibo. (Perfect. Here is your change... I mean, your "
            "receipt. - self-correction, natural speech.) 16. Carlos: Gracias. ¿Vuelve mañana? (Thanks. Will you be back tomorrow? - "
            "relationship building.) 17. María: Todos los días, de ocho a "
            "dos. (Every day, eight to two.) 18. Carlos: Hasta mañana, "
            "pues. (See you tomorrow, then.) 19. María: ¡Que le vaya bien! "
            "(Take care! - lit. 'may it go well for you.') 20. Carlos: ¡Igualmente! (Likewise!)"
        ),
        "how_it_works": (
            "Market talk is bargaining inside politeness. Prices open "
            "with estar + a + price (Están a dos euros el kilo); the "
            "buyer counters with Me deja...? or Me lo deja en...?; the "
            "vendor answers with le doy. Quantities run on el kilo, medio "
            "kilo, un manojo, cada uno. Commands soften trade: Pongame, "
            "Toquelos - usted-forms keeping respect. Son for totals above "
            "one (Son ocho euros), Es for one. Natural speech includes "
            "self-correction (su cambio... digo, su recibo) and phatic "
            "closing (Que le vaya bien / Igualmente). The dialogue's "
            "arc: greeting, search, price, bargain, deal, add-ons, total, "
            "payment, farewell - the universal market script."
        ),
        "key_points": [
            "Prices: Están a dos euros el kilo; totals: Son ocho euros (plural) versus Es un euro.",
            "Bargaining pair: Me deja...? (buyer) / Le doy... (vendor).",
            "Quantities: el kilo, medio kilo, un manojo, cada uno.",
            "Usted-commands keep respect in trade: Pongame, Toquelos, Digame.",
            "The market arc: greeting, search, price, bargain, deal, add-ons, total, payment, farewell.",
        ],
        "requirements": [
            "Role-play the dialogue twice, swapping vendor and customer.",
            "Bargain for five new items using Me deja...? and counteroffers.",
            "Convert the dialogue's usted-forms to tu-forms and note what changes.",
            "Write a new 12-line market dialogue for fish instead of produce.",
            "Record the dialogue and mark every price, quantity, and command.",
        ],
        "standards": [
            "Commercial dialogue follows standard usage in the Diccionario panhispanico de dudas.",
            "Bargaining formulas follow the Diccionario de la lengua espanola.",
            "Command forms follow the Nueva gramatica de la lengua espanola, Morfologia.",
        ],
        "citations": [CIT_RAE_DICT, CIT_RAE_GRAM],
        "sig_lens": (
            "The Signature read: the market is the oldest covenant hall - "
            "trato hecho the spoken seal, que le vaya bien the blessing "
            "on the exchange. Where public dialogues rehearse prices, the "
            "Signature Word Method signs the trade: every bargain an oath "
            "in good faith, every handshake witnessed."
        ),
    },
    {
        "key": "conv_friend",
        "name": "Spanish Conversation: Meeting a Friend",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue between old friends, "
            "annotated. Ana and Luis meet by chance. 1. Ana: ¡Luis! ¡Cuánto tiempo! (Luis! Long time no see! - lit. 'how much time!') "
            "2. Luis: ¡Ana! ¡Qué sorpresa! ¿Cómo estás? (Ana! What a "
            "surprise! How are you?) 3. Ana: Muy bien, ¿y tú? ¿Sigues en Madrid? (Very well, and you? Are you still in Madrid?) "
            "4. Luis: Sí, sigo allí. ¿Y tu familia? (Yes, still there. And "
            "your family?) 5. Ana: Todos bien. Mi hijo ya tiene cinco "
            "años. (Everyone is fine. My son is already five.) 6. Luis: ¡No me digas! El tiempo vuela. (No way! Time flies. - lit. "
            "'do not tell me!') 7. Ana: ¿Y tú? ¿Sigues soltero? (And you? "
            "Still single? - teasing.) 8. Luis: Ya no. Me caso en junio. "
            "(Not anymore. I am getting married in June.) 9. Ana: ¡Felicidades! ¡Invítame, eh? (Congratulations! Invite me, "
            "okay?) 10. Luis: Claro que sí. Sera en la playa. (Of course. "
            "It will be at the beach.) 11. Ana: ¡Qué romántico! ¿Y el trabajo? (How romantic. And work?) 12. Luis: Bien, aunque "
            "con mucho estres. (Fine, though very stressful.) 13. Ana: Cuídate, ¿eh? La salud es primero. (Take care of yourself, "
            "okay? Health first.) 14. Luis: Tienes razón. Oye, ¿tomamos un café? (You are right. Hey, shall we grab a coffee?) 15. Ana: "
            "Me encantaria, pero tengo prisa. (I would love to, but I am "
            "in a hurry. - polite decline.) 16. Luis: Otro dia, entonces. "
            "Dame tu número. (Another day, then. Give me your number.) "
            "17. Ana: Apunta: seis uno dos... (Write it down: six one "
            "two... - dictating digits.) 18. Luis: Listo. Te llamo esta "
            "semana. (Got it. I will call you this week.) 19. Ana: Me "
            "alegro de verte, Luis. (I am so glad to see you, Luis.) "
            "20. Luis: ¡Igualmente, Ana! ¡No desaparezcas! (Likewise, Ana. "
            "Do not disappear on me!)"
        ),
        "how_it_works": (
            "Reunion talk runs on exclamation and update. Cuanto tiempo! "
            "opens; Que sorpresa! answers. Sigues...? asks what continues "
            "(Sigues en Madrid? Sigues soltero?); Ya no flips it (Ya no. "
            "Me caso en junio.). No me digas! marks delighted disbelief. "
            "The conditional softens the decline: Me encantaria, pero... "
            "Oye opens proposals (Oye, tomamos un café?); eh? seeks "
            "agreement (Invitame, eh? Cuidate, eh?). Phone numbers dictate "
            "digit by digit: seis uno dos. The arc: exclamation, mutual "
            "update, news, proposal, polite decline, contact exchange, "
            "warm farewell - the script of friendship resumed."
        ),
        "key_points": [
            "Openers: Cuanto tiempo! Que sorpresa! - exclamation carries the joy.",
            "Sigues...? asks what continues; Ya no flips the answer.",
            "Me encantaria, pero... is the polite decline formula.",
            "Oye proposes; eh? seeks agreement; No me digas! marks delighted disbelief.",
            "The reunión arc: exclamation, updates, news, proposal, contact, warm farewell.",
        ],
        "requirements": [
            "Role-play the dialogue, then improvise a reunión with your own news.",
            "Ask Sigues...? about five life facts and answer with Ya no or Todavia.",
            "Decline five invitations politely with Me encantaria, pero....",
            "Dictate three phone numbers digit by digit in Spanish.",
            "Write a 12-line reunión dialogue set at a wedding instead of the street.",
        ],
        "standards": [
            "Conversational formulas follow the Diccionario panhispanico de dudas.",
            "Social vocabulary follows the Diccionario de la lengua espanola.",
            "Conditional politeness follows the Nueva gramatica de la lengua espanola.",
        ],
        "citations": [CIT_RAE_DICT, CIT_RAE_GRAM],
        "sig_lens": (
            "The Signature read: reunión is the covenant renewed - cuanto "
            "tiempo the seal broken open, no desaparezcas the oath "
            "against distance. Where public dialogues rehearse small "
            "talk, the Signature Word Method signs the bond: every old "
            "friend a witness, every reunión a testimony kept."
        ),
    },
    {
        "key": "conv_problem",
        "name": "Spanish Conversation: Solving a Problem",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue solving a flat tire, "
            "annotated. Sofía has the problem; Diego helps. 1. Sofía: "
            "Diego, tenemos un problema. (Diego, we have a problem. - "
            "direct opening.) 2. Diego: ¿Qué pasa? (What is happening?) "
            "3. Sofía: Se pinchó una llanta. (A tire went flat. - se for "
            "the unplanned.) 4. Diego: Tranquila. ¿Dónde estamos? "
            "(Calm down. Where are we? - reassurance first.) 5. Sofía: En "
            "la carretera, a diez minutos del pueblo. (On the highway, ten "
            "minutes from town.) 6. Diego: ¿Tienes llanta de repuesto? (Do "
            "you have a spare tire?) 7. Sofía: Sí, pero no sé cambiarla. "
            "(Yes, but I do not know how to change it.) 8. Diego: Yo te "
            "ayudo. Saca el gato y la llave. (I will help you. Get out "
            "the jack and the wrench. - commands.) 9. Sofía: Aquí están. ¿Y ahora qué? (Here they are. Now what?) 10. Diego: Afloja "
            "las tuercas primero, sin quitarlas. (Loosen the lug nuts "
            "first, without removing them. - sequenced instruction.) "
            "11. Sofía: Listo. ¿Qué sigue? (Done. What is next?) 12. Diego: "
            "Levanta el coche con el gato. (Lift the car with the jack.) "
            "13. Sofía: Ya está arriba. ¿Quito las tuercas? (It is up. Do "
            "I remove the nuts?) 14. Diego: Sí, quítalas y saca la llanta. "
            "(Yes, remove them and take off the tire. - attached "
            "pronouns.) 15. Sofía: ¡Pesa mucho! (It is heavy!) 16. Diego: "
            "Pon la de repuesto y aprieta las tuercas. (Put on the spare "
            "and tighten the nuts.) 17. Sofía: ¡Hecho! ¿Bajo el coche? "
            "(Done! Do I lower the car?) 18. Diego: Baja el gato despacio "
            "y aprieta otra vez. (Lower the jack slowly and tighten "
            "again.) 19. Sofía: ¡Listo! Eres un genio. ¡Gracias! (Done! You "
            "are a genius. Thanks!) 20. Diego: De nada. Ahora maneja "
            "despacio hasta el taller. (You are welcome. Now drive slowly "
            "to the shop.)"
        ),
        "how_it_works": (
            "Problem-solving talk runs on se for the unplanned (Se "
            "pincho, Se rompio, Se me perdio), reassurance first "
            "(Tranquila), then sequenced tu commands: saca, afloja, "
            "levanta, quita, pon, aprieta, baja - each with attached "
            "pronouns where needed (quítalas). Check-ins punctuate the "
            "work: Y ahora que? Que sigue? Listo? The helper confirms "
            "and continues; the closing gives aftercare (maneja despacio "
            "hasta el taller). Sin + infinitive marks the constraint "
            "(sin quitarlas); primero/después sequence the steps. The "
            "arc: alarm, reassurance, diagnosis, tools, sequenced repair, "
            "verification, thanks, aftercare - the universal fix script."
        ),
        "key_points": [
            "Se marks the unplanned: Se pincho una llanta, Se rompio, Se me perdio.",
            "Reassurance opens: Tranquila. Then sequenced tu commands do the work.",
            "Check-ins punctuate: Y ahora que? Que sigue? Listo?",
            "Pronouns attach to affirmative commands: quítalas, ponla, aprieta.",
            "The fix arc: alarm, reassurance, diagnosis, tools, repair, verification, aftercare.",
        ],
        "requirements": [
            "Narrate three mishaps using se: a flat tire, a broken phone, a lost key.",
            "Give sequenced repair instructions for five problems with tu commands.",
            "Role-play helper and helped, swapping roles halfway.",
            "Convert the dialogue's commands to usted-forms for a formal roadside scene.",
            "Write a 12-line dialogue solving a dead phone battery instead.",
        ],
        "standards": [
            "The unplanned se follows the Nueva gramatica de la lengua espanola.",
            "Command sequences follow the Nueva gramatica, Morfologia.",
            "Problem vocabulary follows the Diccionario de la lengua espanola.",
        ],
        "citations": [CIT_RAE_GRAM, CIT_RAE_DICT],
        "sig_lens": (
            "The Signature read: the fix is the covenant of aid - tranquila "
            "the first seal of calm, de nada the last seal of grace. Where "
            "public dialogues rehearse repairs, the Signature Word Method "
            "signs the rescue: every helping hand a sworn oath, every "
            "problem a promise kept."
        ),
    },
    {
        "key": "mastery",
        "name": "Spanish Mastery Review and Full Reference",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The whole database in one teaching summary: the consolidated "
            "quick-reference. ALPHABET (27 letters): a b c d e f g h i j "
            "k l m n ene o p q r s t u v w x y z - with a e i o u accented "
            "and the diaeresis on u in gue/gui; inverted question and "
            "exclamation marks open their sentences. 200 CORE WORDS, "
            "grouped: People (20): hombre, mujer, niño, niña, madre, "
            "padre, hermano, hermana, abuelo, abuela, tío, tía, primo, "
            "prima, amigo, familia, hijo, esposo, bebe, gente. Home (20): "
            "casa, cocina, dormitorio, sala, baño, mesa, silla, cama, "
            "puerta, ventana, jardin, pared, techo, piso, espejo, "
            "almohada, manta, estante, pasillo, lámpara. Food (20): agua, "
            "pan, leche, café, arroz, huevo, carne, pescado, pollo, "
            "fruta, verdura, manzana, queso, azucar, sal, aceite, sopa, "
            "ensalada, postre, comida. Verbs (30): ser, estar, tener, "
            "hacer, ir, poder, decir, saber, querer, dar, ver, venir, "
            "poner, salir, pensar, hablar, comer, beber, vivir, trabajar, "
            "estudiar, aprender, comprar, leer, escribir, dormir, "
            "despertar, caminar, correr, nadar. Adjectives (20): bueno, malo, "
            "grande, pequeño, nuevo, viejo, alto, bajo, largo, corto, "
            "feliz, triste, bonito, rico, pobre, fácil, difícil, rápido, "
            "lento, importante. Adverbs (10): bien, mal, muy, poco, mucho, "
            "siempre, nunca, hoy, ayer, mañana. Pronouns (15): yo, tu, el, "
            "ella, usted, nosotros, ellos, ustedes, me, te, lo, la, le, "
            "nos, les. Numbers (15): uno, dos, tres, cuatro, cinco, seis, "
            "siete, ocho, nueve, diez, veinte, treinta, cincuenta, cien, "
            "mil. Time (15): dia, semana, mes, ano, hora, minuto, lunes, "
            "martes, miércoles, jueves, viernes, sábado, domingo, hoy, "
            "mañana. Nature (15): sol, luna, estrella, cielo, mar, rio, "
            "montaña, árbol, flor, perro, gato, pájaro, lluvia, nieve, "
            "viento. Question words (10): quien, cual, donde, como, "
            "cuanto, por que, este, ese, aquel, todo. Connectors (10): y, o, pero, porque, aunque, cuando, "
            "si, que, para, con. KEY GRAMMAR: subject-verb-object order; "
            "el/la/los/las and un/una; gender and number agreement on "
            "adjectives; no before the verb with stacked negatives (no "
            "veo a nadie); questions by intonation with inverted marks; "
            "ser for identity, estar for states and places; gustar "
            "backwards (me gusta); tu commands (habla) with eight "
            "irregulars (di, haz, ve, pon, sal, se, ten, ven); present, "
            "preterite, imperfect, future, conditional on the infinitive "
            "stem; para que always subjunctive. PHRASE TABLES: greetings "
            "(hola, buenos días, buenas tardes, buenas noches, adiós, "
            "hasta luego, gracias, por favor, de nada, perdon); travel "
            "(donde está, cuanto cuesta, a que hora, un billete, la "
            "cuenta); feelings (estoy feliz, tengo miedo, me encanta, lo "
            "siento). Study counsel: read one record daily in ladder "
            "order, speak every sentence aloud, write ten new sentences "
            "per record, and retest with the demos until each prints OK."
        ),
        "how_it_works": (
            "Mastery is the ladder walked twice: first for exposure, "
            "second for ownership. Use this record as the map: the "
            "alphabet for spelling, the 200 words for recognition, the "
            "grammar for construction, the phrase tables for survival. "
            "Test yourself in rounds: round one, translate the 200 words "
            "both directions; round two, conjugate the 30 verbs in five "
            "tenses; round three, rebuild the 15 complex sentences from "
            "their connectors; round four, perform the three dialogues "
            "from memory. The demos are the examiners: each prints real "
            "computed values - conjugations, stress placements, quiz "
            "scores - and every OK is a seal on that rung. When all 34 "
            "records read, all 68 demos pass, and the three stories retell "
            "in your own words, the ladder is climbed: you hold Spanish "
            "from its alphabet to its arguments."
        ),
        "key_points": [
            "The 200 core words above are the recognition floor - translate them both directions.",
            "The 30 verbs in five tenses are the engine - conjugate them until automatic.",
            "The phrase tables are survival Spanish: greetings, travel, feelings, on demand.",
            "The 15 complex sentences are the ceiling: rebuild each from its connector.",
            "Climb the ladder twice: once for exposure, once for ownership - then retell the three stories.",
        ],
        "requirements": [
            "Translate all 200 core words Spanish-to-English and back with 95 percent accuracy.",
            "Conjugate the 30 core verbs in present, preterite, imperfect, future, and conditional.",
            "Perform the three dialogues from memory with a partner.",
            "Rebuild the 15 complex sentences from their connectors alone.",
            "Retell all three stories in your own words, keeping each story's tense spine.",
        ],
        "standards": [
            "Word lists consolidate the Diccionario de la lengua espanola entries taught across records 1-33.",
            "Grammar summary consolidates the Nueva gramatica rules taught across records 1-33.",
            "Reference tables follow the Ortografia de la lengua espanola 2010.",
        ],
        "citations": [CIT_RAE_DICT, CIT_RAE_GRAM, CIT_RAE_ORT, CIT_CERVANTES],
        "sig_lens": (
            "The Signature read: mastery is the fully signed covenant - "
            "the alphabet the first seal, the argument the last. Where "
            "public courses issue certificates, the Signature Word "
            "Method issues fluency: every word witnessed, every tense "
            "sworn, the whole tongue sealed in the learner's keeping."
        ),
    },
]
