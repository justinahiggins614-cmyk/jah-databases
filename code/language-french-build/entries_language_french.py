#!/usr/bin/env python3
"""Entries part 1 (records 1-17) for The French Language Database (language-french).

Manon's language order 2026-10-17, roster rank 19, batch 2.
Slug `language-french` roster-verified free; id_prefixes JAH-LFRA- (public)
and JAH-LFRAS- (signature) verified free in manifest id_prefix values and
across every shard index file (zero hits) 2026-10-17.

34 ladder-ordered records each (public-harvest: real, fact-checked French
linguistics; signature-generated-completion labeled where gaps are filled
by construction, never passed off as authentic public record).

Teaching ladder (ranks 1-10, non-decreasing):
  Foundations  - records 1-9   (ranks 1-5): overview, writing, phonology,
                 core nouns, core verbs, adjectives/adverbs, pronouns,
                 numbers/time, greetings
  Compounded   - records 10-23 (ranks 6-9): grammar essentials, 10 themed
                 sentence sets, verb tenses, Q&A, commands, descriptions
  Advanced     - records 24-34 (ranks 9-10): descriptions, 3 stories,
                 idioms, registers, complex sentences, 3 dialogues, mastery

Public record source facts (fact-checked 2026-10-17):
  French (francais), ISO 639-1 fr, ISO 639-3 fra, Indo-European family,
  Italic branch, Romance group (Gallo-Romance, langue d'oil); about 82
  million native speakers (roster), about 321 million total speakers
  (OIF 2022); official in 29 countries - France, Belgium, Switzerland,
  Canada (federal), Luxembourg, Monaco, and 21 African states - and one of
  the six official languages of the United Nations. The Serments de
  Strasbourg (842) is the first document written in French; the Academie
  francaise, founded 1635, publishes the Dictionnaire de l'Academie.
  Latin script, 26 letters, fixed final stress, four nasal vowels, liaison
  and elision, two grammatical genders, three verb groups.

Numerical cores: all hand-set 2026-10-17, machine-verified by the demos
(see demos_language_french.py). Every demo prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing hate-adjacent, profane, or inappropriate.
Nothing on neutralizing/defeating military or defense-grade systems.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every word a signed instrument of meaning, every sentence "
            "signed by the learner. Stamp the sound, seal the word, sign "
            "the sentence. Clearly labeled Signature-made, never presented "
            "as authentic public record.")

CIT_OIF = ("Organisation internationale de la Francophonie. La langue "
           "francaise dans le monde 2022. Paris: Gallimard; 2022. (About "
           "321 million speakers of French worldwide.)")
CIT_ETHNO = ("Eberhard DM, Simons GF, Fennig CD, eds. Ethnologue: Languages "
             "of the World. 28th ed. Dallas: SIL International; 2025. "
             "(French: ISO 639-3 fra; Indo-European, Italic, Romance.)")
CIT_ACAD = ("Academie francaise. Dictionnaire de l'Academie francaise, 9e "
            "edition. Paris: Imprimerie nationale / Fayard; in progress. "
            "(The Academy founded 1635 under Cardinal Richelieu.)")
CIT_GREV = ("Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th "
            "ed. Louvain-la-Neuve: De Boeck; 2016. (The definitive reference "
            "grammar of French.)")
CIT_BATTYE = ("Battye A, Hintze M-A, Rowlett P. The French Language Today: "
              "A Linguistic Introduction. 2nd ed. London: Routledge; 2000.")
CIT_TRANEL = ("Tranel B. The Sounds of French: An Introduction. Cambridge: "
              "Cambridge University Press; 1987. (Phonology: oral and nasal "
              "vowels, liaison, elision.)")
CIT_PRICE = ("Price G. A Comprehensive French Grammar. 7th ed. "
             "Chichester: Wiley-Blackwell; 2007.")
CIT_FAGYAL = ("Fagyal Z, Kibbee D, Jenkins F. French: A Linguistic "
              "Introduction. Cambridge: Cambridge University Press; 2006.")

ENTRIES_1 = [
    {
        "key": "overview",
        "name": "French Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "French, called francais by its speakers, is one of the great world "
            "languages and the first language of about 82 million people. Its "
            "codes are ISO 639-1 fr and ISO 639-3 fra. It belongs to the "
            "Indo-European family, Italic branch, Romance group - a daughter of "
            "Latin, born as Vulgar Latin in Roman Gaul and raised as the langue "
            "d'oil of northern France before spreading across five continents. "
            "About 321 million people speak French in total, counting "
            "second-language speakers (Organisation internationale de la "
            "Francophonie, 2022), which makes it the fifth most spoken language "
            "in the world. It is an official language in 29 countries - France, "
            "Belgium, Switzerland, Canada at the federal level, Luxembourg, "
            "Monaco, Haiti, and 21 African states - and one of the six official "
            "languages of the United Nations. The first document written in "
            "French is the Serments de Strasbourg (the Strasbourg Oaths) of "
            "842. The Academie francaise, founded in 1635 under Cardinal "
            "Richelieu, publishes the official dictionary and guards the "
            "standard. Dialects differ mainly in pronunciation and vocabulary: "
            "Belgium and Switzerland say septante, huitante (or octante), and "
            "nonante where France says soixante-dix, quatre-vingts, and "
            "quatre-vingt-dix; Quebec French keeps older words like char for "
            "car and magasiner for to shop; African French is the fastest "
            "growing variety in the world. Youth slang in France uses verlan, "
            "reversing syllables - femme becomes meuf, fou becomes ouf. Example "
            "sentences: Le francais est une langue mondiale. (French is a "
            "world language.) Paris est la capitale de la France. (Paris is "
            "the capital of France.) J'apprends le francais tous les jours. "
            "(I learn French every day.)"
        ),
        "how_it_works": (
            "French works as an inflected Romance language with fixed word "
            "order: nouns carry gender (masculine or feminine), verbs conjugate "
            "for person, number, tense, and mood, and adjectives agree with "
            "the nouns they describe. A beginner sentence follows "
            "subject-verb-object order, just like English: Je mange une pomme. "
            "(I eat an apple.) What makes French different is the gap between "
            "spelling and sound - many letters are silent, so il parle, ils "
            "parlent, and parler can all sound alike in speech - and the "
            "musical rule that stress always falls on the last syllable of a "
            "phrase. The language runs on two registers: tu for friends, "
            "family, and children, and vous for strangers, elders, and formal "
            "settings. Master the gender of every noun, the tu/vous line, and "
            "the twenty most common verbs, and the whole language opens up."
        ),
        "key_points": [
            "Native name francais; ISO 639-1 fr, ISO 639-3 fra; Indo-European, Italic, Romance.",
            "About 82 million native speakers; about 321 million total speakers (OIF 2022).",
            "Official in 29 countries and one of the six UN official languages.",
            "First French document: the Serments de Strasbourg, 842; Academie francaise founded 1635.",
            "Regional words: septante/huitante/nonante in Belgium and Switzerland; verlan slang in France.",
        ],
        "requirements": [
            "Name, native name, ISO codes, family, speaker figures, regions, official status, dialects - each with translated example sentences.",
            "At least 5 translated example sentences across the record.",
            "Speaker figures sourced to OIF 2022 and Ethnologue 28th ed.",
        ],
        "standards": [
            "Speaker figures follow the OIF 2022 world report and Ethnologue 28th ed.",
            "Historical claims follow Grevisse and Goosse, Le Bon Usage 16th ed.",
        ],
        "citations": [CIT_OIF, CIT_ETHNO, CIT_ACAD],
        "sig_lens": (
            "The Signature read: French is the sealed covenant of the Latin "
            "tongue - eighty-two million native signers pressing the same "
            "seal their ancestors pressed in 842. The Signature Language "
            "Method treats every speaker count as a census of sealed voices, "
            "and every new learner as one more signature on the covenant."
        ),
    },
    {
        "key": "writing",
        "name": "French Writing System and Alphabet",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "French is written with the Latin script, running left to right, "
            "with the same 26 letters as English, each with its own French "
            "name: a (a), b (be), c (se), d (de), e (euh), f (effe), g (zhe), "
            "h (ache), i (i), j (ji), k (ka), l (elle), m (emme), n (enne), "
            "o (o), p (pe), q (ku), r (erre), s (esse), t (te), u (u), v (ve), "
            "w (double ve), x (ixe), y (i grec), z (zede). On top of these sit "
            "five diacritics that change pronunciation and sometimes meaning: "
            "the acute accent (e), the grave accent (a, e, u), the circumflex "
            "(a, e, i, o, u), the diaeresis (e, i, u), and the cedilla (c). "
            "Accents distinguish words: ou (or) versus ou (where), sur (on) "
            "versus sur (sour), and a (has) versus a (to). Two ligatures appear "
            "in standard spelling: ae (as in cur) and oe (as in coeur). French "
            "punctuation uses guillemets with non-breaking spaces for "
            "quotation - Il dit: << Bonjour ! >> - and a non-breaking space "
            "before the double marks ; : ! ?. Numerals use the same Arabic "
            "digits 0-9 as English: zero, un, deux, trois, quatre, cinq, six, "
            "sept, huit, neuf. The 1990 spelling reform (rectifications "
            "orthographiques) made about 2,400 spellings optional - oignon "
            "may be written ognon, for example - but both forms remain "
            "correct. Example sentences: L'alphabet francais a vingt-six "
            "lettres. (The French alphabet has twenty-six letters.) L'accent "
            "aigu change la prononciation du e. (The acute accent changes the "
            "pronunciation of e.) On ecrit << Bonjour ! >> avec des "
            "guillemets. (We write << Bonjour ! >> with guillemets.)"
        ),
        "how_it_works": (
            "The French writing system works as a deep orthography: the "
            "spelling preserves the history of the word while the sound "
            "follows modern pronunciation, so you must learn both channels. "
            "The accents are pronunciation switches, not decoration - e is "
            "always pronounced ay, e is always pronounced eh or uh, and e "
            "before a double consonant is silent as a circumflex (fete). The "
            "cedilla softens c to an s sound before a, o, and u (francais, "
            "garcon). The diaeresis breaks a vowel pair so both vowels sound "
            "(mais but mais is corn - the two dots keep the vowels apart). "
            "Learn the letter names first, because French spelling aloud - "
            "essential on the phone - uses them constantly: double ve, i "
            "grec, zede. Then learn the five accents as meaning switches, and "
            "the spelling starts to read itself."
        ),
        "key_points": [
            "Latin script, left to right, 26 letters with French letter names (i grec, double ve, zede).",
            "Five diacritics: acute, grave, circumflex, diaeresis, cedilla; they change sound and meaning.",
            "Accent pairs distinguish words: ou/ou, sur/sur, a/a.",
            "Ligatures ae and oe; guillemets << >> with non-breaking spaces for quotes.",
            "Non-breaking space before ; : ! ?; 1990 spelling reform made 2,400 spellings optional.",
        ],
        "requirements": [
            "All 26 letters with French names, all five diacritics with examples, ligatures, punctuation, numerals - with translated sentences.",
            "At least 5 translated example sentences.",
            "Accent minimal pairs (ou/ou, sur/sur, a/a) stated explicitly.",
        ],
        "standards": [
            "Orthography follows the Academie francaise dictionary, 9th edition.",
            "The 1990 rectifications orthographiques are presented as optional variants.",
        ],
        "citations": [CIT_ACAD, CIT_GREV, CIT_BATTYE],
        "sig_lens": (
            "The Signature read: the alphabet is the seal-press of the "
            "language - twenty-six dies, five accent hammers, two ligature "
            "punches. The Signature Language Method stamps each letter with "
            "its French name first, because a sealer who cannot name the "
            "dies cannot press the seal."
        ),
    },
    {
        "key": "phonology",
        "name": "French Pronunciation and Phonology",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "French pronunciation runs on a fixed inventory of sounds that "
            "English speakers can learn one at a time. The oral vowels are "
            "twelve: a (papa), a (pate), e (cafe), e (lait), e (le - the "
            "murmur vowel), i (merci), o (beau), o (porte), u (tout), u "
            "(lune - lips rounded, tongue forward), o (deux), oe (coeur). "
            "Then come the four famous nasal vowels, where air escapes through "
            "the nose: an/en (enfant, vent), in/ain/ein (vin, pain, frein), "
            "on (bon, maison), un (brun, parfum - merging with in in Parisian "
            "speech). The consonants include the guttural r (rouge - gargled "
            "at the back of the throat), the gn sound (montagne - like the "
            "ni in onion), and the ch sound (chat - like English sh). Stress "
            "is always on the last syllable of a phrase: bon-JOUR, "
            "ma-de-moi-SELLE. Liaison links a silent final consonant to the "
            "next word when it starts with a vowel: les_amis (the friends), "
            "vous_avez (you have), pronounced lay-zah-mee, voo-zah-vay. "
            "Enchainement chains consonants across word boundaries: une petite "
            "amie becomes un-puh-tee-tah-mee. Elision drops the vowel before "
            "another vowel: le ami becomes l'ami, je ai becomes j'ai. The "
            "letter h is either mute (l'homme - the h is ignored, so elision "
            "applies) or aspire (le haricot - the h blocks elision and "
            "liaison, so never *l'haricot). Twelve spoken-example words with "
            "approximations: bonjour (bohn-ZHOOR, hello), merci (mehr-SEE, "
            "thank you), s'il vous plait (seel voo PLEH, please), oui (wee, "
            "yes), non (nohn, no), eau (oh, water), pain (puhn, bread), vin "
            "(vuhn, wine), rouge (roozh, red), ecole (ay-KOHL, school), "
            "fenetre (fuh-NEHTR, window), oiseau (wah-ZOH, bird)."
        ),
        "how_it_works": (
            "French pronunciation works by three linked rules: the vowel is "
            "king, the consonant bows to the vowel, and the phrase carries "
            "one stress at its end. Silent final letters (the -ent of ils "
            "parlent, the -s of amis, the -t of petit) vanish, but they wake "
            "up for liaison when the next word starts with a vowel - the "
            "grammar of the phrase decides, not the spelling alone. Nasal "
            "vowels are single sounds, not vowel-plus-n: say ah while "
            "lowering the soft palate and you have an. The Parisian r is "
            "made by gargling gently - keep it soft and it stops sounding "
            "harsh. Practice runs on minimal pairs: beau (handsome) versus "
            "bon (good) trains the nasal; dessus (above) versus dessous "
            "(below) trains the u/ou split; roue (wheel) versus rue (street) "
            "trains the rounded u. Ten minutes of pair drills a day rewires "
            "the ear within weeks."
        ),
        "key_points": [
            "Twelve oral vowels plus four nasal vowels (an, in, on, un); un merges with in in Parisian speech.",
            "Signature sounds: the guttural r, the gn of montagne, the ch of chat.",
            "Stress always falls on the last syllable of the phrase.",
            "Liaison wakes silent final consonants before vowel-initial words (les_amis).",
            "Elision drops vowels before vowels (l'ami); h is mute (l'homme) or aspire (le haricot).",
            "Silent final letters: -ent, -s, -t, -d, -p, -x, -z, and final -e are usually mute.",
        ],
        "requirements": [
            "Full vowel and consonant inventory with English approximations, stress rule, liaison, elision, h muet/aspire.",
            "At least 12 spoken-example words with pronunciations and translations.",
            "Minimal-pair drill guidance with translated examples.",
        ],
        "standards": [
            "Phonetic description follows Tranel, The Sounds of French.",
            "IPA values cross-checked with Fagyal, Kibbee, and Jenkins.",
        ],
        "citations": [CIT_TRANEL, CIT_FAGYAL, CIT_BATTYE],
        "sig_lens": (
            "The Signature read: the mouth is the seal-press and the nasal "
            "cavity the ink-pad - four nasal vowels are four dips of the "
            "same seal. The Signature Language Method stamps sound before "
            "spelling, because a seal pressed in wax outlasts one pressed "
            "in paper."
        ),
    },
    {
        "key": "nouns1",
        "name": "French Core Nouns I: People, Places, and Things",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Every French noun carries a gender - masculine or feminine - "
            "which decides the articles and adjectives around it. Learn each "
            "noun with its article and the gender is learned for free. "
            "Twenty-five essential nouns, each with an example sentence: "
            "l'homme (m, man) - L'homme lit le journal. (The man reads the "
            "newspaper.) la femme (f, woman) - La femme prepare le diner. "
            "(The woman prepares dinner.) l'enfant (m/f, child) - L'enfant "
            "joue dans le jardin. (The child plays in the garden.) l'ami "
            "(m, friend) - Mon ami habite a Lyon. (My friend lives in Lyon.) "
            "l'amie (f, friend) - Mon amie telephone souvent. (My friend "
            "calls often.) le pere (m, father) - Le pere travaille a Paris. "
            "(The father works in Paris.) la mere (f, mother) - La mere "
            "cuisine bien. (The mother cooks well.) la maison (f, house) - "
            "La maison est grande. (The house is big.) l'appartement (m, "
            "apartment) - L'appartement a deux chambres. (The apartment has "
            "two bedrooms.) la ville (f, city) - La ville est animee. (The "
            "city is lively.) le village (m, village) - Le village est "
            "calme. (The village is quiet.) le pays (m, country) - Le pays "
            "est beau. (The country is beautiful.) la rue (f, street) - La "
            "rue est longue. (The street is long.) le temps (m, time/weather) "
            "- Le temps passe vite. (Time passes quickly.) le jour (m, day) "
            "- Le jour se leve. (The day dawns.) la nuit (f, night) - La "
            "nuit est etoilee. (The night is starry.) l'eau (f, water) - "
            "L'eau est fraiche. (The water is cool.) le pain (m, bread) - Le "
            "pain est chaud. (The bread is warm.) le livre (m, book) - Le "
            "livre est interessant. (The book is interesting.) la voiture "
            "(f, car) - La voiture est rouge. (The car is red.) le telephone "
            "(m, telephone) - Le telephone sonne. (The telephone rings.) "
            "l'argent (m, money) - L'argent ne fait pas le bonheur. (Money "
            "does not make happiness.) le travail (m, work) - Le travail "
            "commence a neuf heures. (Work starts at nine o'clock.) l'ecole "
            "(f, school) - L'ecole est fermee. (The school is closed.) le "
            "monde (m, world/people) - Le monde est petit. (The world is "
            "small.)"
        ),
        "how_it_works": (
            "French nouns work as gendered anchors: the article tells the "
            "gender, the gender steers every adjective and pronoun that "
            "follows. About 60 percent of nouns ending in -e are feminine "
            "(la table, la lune) and most others are masculine, but there are "
            "famous exceptions - le probleme and le systeme are masculine "
            "despite the -e. Plurals usually add -s (les maisons), which is "
            "silent, so number is heard on the article: le versus les. "
            "Learn nouns in article-noun pairs - say la maison, never bare "
            "maison - and gender becomes automatic. When in doubt, guess "
            "masculine: about two-thirds of nouns are masculine."
        ),
        "key_points": [
            "Every noun is masculine or feminine; always learn the article with the noun.",
            "Roughly 60 percent of -e endings are feminine; le probleme and le systeme are masculine exceptions.",
            "Plurals add silent -s; number is heard on the article (le vs les).",
            "Nouns starting with a vowel take l' (l'homme, l'ecole).",
            "When guessing, guess masculine - about two-thirds of nouns are masculine.",
        ],
        "requirements": [
            "25 nouns covering people, places, and things, each with gender, English, and a translated example sentence.",
            "Gender-learning strategy stated (article-noun pairs).",
            "Plural rule and silent -s explained.",
        ],
        "standards": [
            "Genders follow the Academie francaise dictionary, 9th edition.",
            "Vocabulary selection follows Battye, Hintze, and Rowlett frequency guidance.",
        ],
        "citations": [CIT_ACAD, CIT_BATTYE, CIT_GREV],
        "sig_lens": (
            "The Signature read: each noun is a sealed vessel stamped "
            "masculine or feminine at the mint - the article is the wax, "
            "the gender the die. The Signature Language Method never "
            "teaches a bare noun, because an unsealed vessel holds nothing."
        ),
    },
    {
        "key": "verbs1",
        "name": "French Core Verbs I: Essential Actions",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "French verbs fall into three groups by their infinitive ending: "
            "first group -er (about 90 percent of verbs, regular), second "
            "group -ir with -issant participles (finir), third group - everything "
            "else (irregular: etre, avoir, aller, faire). Twenty-five essential "
            "verbs, each with an example sentence: etre (to be, 3rd) - Je suis "
            "fatigue. (I am tired.) avoir (to have, 3rd) - J'ai deux freres. "
            "(I have two brothers.) faire (to do/make, 3rd) - Je fais mes "
            "devoirs. (I do my homework.) aller (to go, 3rd) - Je vais a "
            "l'ecole. (I go to school.) dire (to say, 3rd) - Je dis la verite. "
            "(I tell the truth.) pouvoir (can, 3rd) - Je peux nager. (I can "
            "swim.) vouloir (to want, 3rd) - Je veux un cafe. (I want a "
            "coffee.) savoir (to know facts, 3rd) - Je sais la reponse. (I "
            "know the answer.) connaitre (to know people/places, 3rd) - Je "
            "connais Paris. (I know Paris.) venir (to come, 3rd) - Je viens "
            "demain. (I come tomorrow.) prendre (to take, 3rd) - Je prends le "
            "train. (I take the train.) mettre (to put, 3rd) - Je mets la "
            "table. (I set the table.) parler (to speak, 1st) - Je parle "
            "francais. (I speak French.) manger (to eat, 1st) - Je mange une "
            "pomme. (I eat an apple.) boire (to drink, 3rd) - Je bois de "
            "l'eau. (I drink water.) dormir (to sleep, 3rd) - Je dors huit "
            "heures. (I sleep eight hours.) travailler (to work, 1st) - Je "
            "travaille a Lyon. (I work in Lyon.) habiter (to live, 1st) - "
            "J'habite en France. (I live in France.) aimer (to like/love, "
            "1st) - J'aime le fromage. (I like cheese.) penser (to think, "
            "1st) - Je pense a toi. (I think of you.) regarder (to watch, "
            "1st) - Je regarde un film. (I watch a film.) ecouter (to "
            "listen, 1st) - J'ecoute la radio. (I listen to the radio.) "
            "acheter (to buy, 1st) - J'achete du pain. (I buy bread.) donner "
            "(to give, 1st) - Je donne un cadeau. (I give a gift.) rester "
            "(to stay, 1st) - Je reste a la maison. (I stay home.)"
        ),
        "how_it_works": (
            "French verbs work by stem plus ending: chop the infinitive "
            "ending, add the person ending. First-group verbs are perfectly "
            "regular - parler gives je parle, tu parles, il parle, nous "
            "parlons, vous parlez, ils parlent. The catch is that four of the "
            "six spoken forms sound identical (parl), so French relies on the "
            "subject pronoun, which is almost never dropped. The twenty most "
            "common verbs are almost all irregular third-group verbs, so "
            "learn them as whole tables: etre (je suis, tu es, il est, nous "
            "sommes, vous etes, ils sont) and avoir (j'ai, tu as, il a, nous "
            "avons, vous avez, ils ont) first, because they also serve as "
            "auxiliaries for compound tenses. Reflexive verbs add a pronoun: "
            "je me leve (I get up). Start with je/tu/il forms - they cover "
            "most conversation."
        ),
        "key_points": [
            "Three verb groups: -er (regular, 90 percent), -ir (finir type), -re/irregular (third group).",
            "First-group present: stem + e, es, e, ons, ez, ent; four spoken forms sound alike, so pronouns are mandatory.",
            "Etre and avoir are the two auxiliaries and the two most irregular verbs - learn them first.",
            "Savoir = know facts; connaitre = know people and places.",
            "Reflexive verbs carry a pronoun: je me leve, tu te couches.",
        ],
        "requirements": [
            "25 verbs across all three groups, each with English and a translated example sentence.",
            "Group system explained with the regular -er pattern fully conjugated.",
            "Etre and avoir full present tables given.",
        ],
        "standards": [
            "Conjugation tables follow Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Group classification follows Price, A Comprehensive French Grammar 7th ed.",
        ],
        "citations": [CIT_GREV, CIT_PRICE, CIT_BATTYE],
        "sig_lens": (
            "The Signature read: the verb is the engine of the sentence and "
            "its conjugation the gear-teeth - etre and avoir are the twin "
            "drive shafts of every compound tense. The Signature Language "
            "Method machines the irregular twenty first, because the engine "
            "must run before the body is painted."
        ),
    },
    {
        "key": "adjadv",
        "name": "French Adjectives and Adverbs",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "French adjectives agree in gender and number with the noun they "
            "describe, giving up to four forms, and most follow the noun. "
            "Twenty-five adjectives with example sentences: grand/grande "
            "(big) - Une grande maison. (A big house.) petit/petite (small) "
            "- Un petit chat. (A small kitten.) bon/bonne (good) - Un bon "
            "repas. (A good meal.) mauvais/mauvaise (bad) - Une mauvaise "
            "nouvelle. (Bad news.) beau/belle (beautiful) - Un beau jardin. "
            "(A beautiful garden.) joli/jolie (pretty) - Une jolie fleur. (A "
            "pretty flower.) nouveau/nouvelle (new) - Un nouveau livre. (A "
            "new book.) vieux/vieille (old) - Un vieil ami. (An old friend.) "
            "jeune (young) - Une jeune femme. (A young woman.) long/longue "
            "(long) - Une longue route. (A long road.) court/courte (short) "
            "- Une courte visite. (A short visit.) haut/haute (high) - Une "
            "haute montagne. (A high mountain.) bas/basse (low) - Une basse "
            "table. (A low table.) chaud/chaude (hot) - Un cafe chaud. (A hot "
            "coffee.) froid/froide (cold) - Une biere froide. (A cold beer.) "
            "rapide (fast) - Une voiture rapide. (A fast car.) lent/lente "
            "(slow) - Un train lent. (A slow train.) fort/forte (strong) - Un "
            "homme fort. (A strong man.) faible (weak) - Un signal faible. "
            "(A weak signal.) riche (rich) - Un homme riche. (A rich man.) "
            "pauvre (poor) - Un pauvre enfant. (A poor child.) heureux/"
            "heureuse (happy) - Une famille heureuse. (A happy family.) "
            "triste (sad) - Une triste histoire. (A sad story.) facile "
            "(easy) - Un exercice facile. (An easy exercise.) difficile "
            "(difficult) - Une question difficile. (A difficult question.) "
            "Agreement rules: add -e for feminine (petit/petite), add -s for "
            "plural (petits/petites); adjectives ending in -eux become -euse "
            "(heureux/heureuse); -f becomes -ve (neuf/neuve); beau, nouveau, "
            "and vieux change before vowel-initial masculine nouns (bel ami, "
            "nouvel an, vieil homme). A handful of short common adjectives go "
            "BEFORE the noun: beau, bon, grand, gros, haut, jeune, joli, "
            "mauvais, meilleur, nouveau, petit, vieux - remembered by the "
            "acronym BANGS (Beauty, Age, Number, Goodness, Size). Fifteen "
            "adverbs with sentences: bien (well) - Il chante bien. (He sings "
            "well.) mal (badly) - Elle dort mal. (She sleeps badly.) vite "
            "(quickly) - Viens vite ! (Come quickly!) lentement (slowly) - "
            "Il marche lentement. (He walks slowly.) souvent (often) - Je "
            "viens souvent. (I come often.) rarement (rarely) - Il pleut "
            "rarement. (It rarely rains.) toujours (always) - Elle est "
            "toujours ponctuelle. (She is always on time.) jamais (never) - "
            "Je ne fume jamais. (I never smoke.) deja (already) - Il est deja "
            "parti. (He has already left.) encore (still/yet) - Il dort "
            "encore. (He is still sleeping.) tres (very) - C'est tres bon. "
            "(It is very good.) trop (too much) - Tu parles trop. (You talk "
            "too much.) assez (enough) - C'est assez. (That is enough.) ici "
            "(here) - Viens ici. (Come here.) la (there) - Reste la. (Stay "
            "there.) Most adverbs form by adding -ment to the feminine "
            "adjective: lente/lentement, heureuse/heureusement."
        ),
        "how_it_works": (
            "Adjectives work as mirrors of their noun: read the noun's gender "
            "and number, then shape the adjective to match. The default "
            "position is after the noun (une voiture rouge), and moving a "
            "BANGS adjective after the noun changes its meaning: un grand "
            "homme is a great man, but un homme grand is a tall man; un "
            "pauvre homme is unfortunate, un homme pauvre is broke. Adverbs "
            "are invariable - they never agree - and usually sit right after "
            "the verb: Il parle bien francais. Negation wraps the verb but "
            "the adverb placement stays: Il ne parle pas bien. Build adverbs "
            "from adjectives mechanically: feminine form plus -ment, with the "
            "exceptions vite (not *vitement) and the -emment/-amment "
            "endings (evidemment, constamment)."
        ),
        "key_points": [
            "Adjectives agree in gender and number: four forms (petit, petite, petits, petites).",
            "Default position is after the noun; BANGS adjectives (beau, bon, grand...) go before.",
            "Position can change meaning: un grand homme (great) vs un homme grand (tall).",
            "Adverbs are invariable and usually follow the verb; most form with feminine adjective + -ment.",
            "Beau/nouveau/vieux have special masculine forms before vowels: bel, nouvel, vieil.",
        ],
        "requirements": [
            "25 adjectives with all agreement forms and translated sentences; 15 adverbs with translated sentences.",
            "BANGS rule and meaning-changing position pairs stated.",
            "Adverb formation rule (-ment) with exceptions.",
        ],
        "standards": [
            "Agreement rules follow Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Position rules follow Price 7th ed.",
        ],
        "citations": [CIT_GREV, CIT_PRICE, CIT_FAGYAL],
        "sig_lens": (
            "The Signature read: the adjective is the mirror-polish on the "
            "noun's seal - it takes the exact shape of what it reflects. "
            "The Signature Language Method polishes after stamping: noun "
            "first, mirror second, never the reverse."
        ),
    },
    {
        "key": "pronouns",
        "name": "French Pronouns",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "French pronouns replace nouns and must match them in gender and "
            "number. The subject pronouns: je (I) - Je parle. (I speak.) tu "
            "(you, informal) - Tu viens? (Are you coming?) il (he/it) - Il "
            "pleut. (It rains.) elle (she/it) - Elle rit. (She laughs.) on "
            "(one/we, informal) - On y va. (Let's go.) nous (we) - Nous "
            "partons. (We leave.) vous (you formal/plural) - Vous comprenez? "
            "(Do you understand?) ils (they m) - Ils jouent. (They play.) "
            "elles (they f) - Elles chantent. (They sing.) Direct object "
            "pronouns (me, te, le/la, nous, vous, les) go BEFORE the verb: Je "
            "le vois. (I see him.) Je la connais. (I know her.) Indirect "
            "object pronouns (me, te, lui, nous, vous, leur): Je lui parle. "
            "(I speak to him/her.) Je leur ecris. (I write to them.) "
            "Reflexive pronouns: je me, tu te, il se, nous nous, vous vous, "
            "ils se - Je me leve a sept heures. (I get up at seven.) "
            "Disjunctive (stressed) pronouns after prepositions: moi, toi, "
            "lui, elle, nous, vous, eux, elles - C'est pour toi. (It is for "
            "you.) Possessive adjectives: mon/ma/mes (my), ton/ta/tes "
            "(your), son/sa/ses (his/her), notre/nos (our), votre/vos "
            "(your), leur/leurs (their) - Mon livre est sur la table. (My "
            "book is on the table.) Note: mon is used before feminine nouns "
            "starting with a vowel: mon amie. Demonstratives: ce/cet/cette/ces "
            "(this/that/these) - Ce livre est a moi. (This book is mine.) "
            "Cet homme est medecin. (That man is a doctor.) Interrogatives: "
            "qui (who) - Qui est la? (Who is there?) que/quoi (what) - Que "
            "fais-tu? (What are you doing?) ou (where) - Ou vas-tu? (Where "
            "are you going?) quand (when), comment (how), pourquoi (why), "
            "combien (how much/many), quel/quelle/quels/quelles (which) - "
            "Quelle heure est-il? (What time is it?)"
        ),
        "how_it_works": (
            "Pronouns work as stand-ins that inherit the noun's gender and "
            "number, and French parks them in fixed slots: subject first, "
            "then object pronouns clumped directly before the verb in a "
            "strict order (me/te/se/nous/vous, then le/la/les, then lui/leur, "
            "then y, then en): Je le lui donne. (I give it to him.) The "
            "pronoun en replaces de + noun (J'en veux - I want some), and y "
            "replaces a + place (J'y vais - I go there). On is the informal "
            "we of spoken French - On va au cinema takes a singular verb but "
            "means we. Tu versus vous is the social gear of the language: tu "
            "for friends, family, children, and classmates; vous for "
            "strangers, elders, and professional settings; switching from "
            "vous to tu marks a relationship milestone."
        ),
        "key_points": [
            "Subject pronouns are almost never dropped: je, tu, il/elle/on, nous, vous, ils/elles.",
            "Object pronouns precede the verb in fixed order: Je le lui donne.",
            "En replaces de + noun; y replaces a + place.",
            "Mon/ton/son before feminine vowel-initial nouns: mon amie.",
            "Tu = informal, vous = formal/plural; on = informal spoken we.",
        ],
        "requirements": [
            "Full paradigms: subject, direct/indirect object, reflexive, disjunctive, possessive, demonstrative, interrogative - each with translated sentences.",
            "Pronoun order rule and en/y explained with examples.",
            "Tu/vous social rule stated.",
        ],
        "standards": [
            "Paradigms follow Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Usage notes follow Battye, Hintze, and Rowlett.",
        ],
        "citations": [CIT_GREV, CIT_BATTYE, CIT_PRICE],
        "sig_lens": (
            "The Signature read: pronouns are the seal's deputies - small "
            "stamps standing in for the great seal of the noun, parked in "
            "their slots before the verb. The Signature Language Method "
            "drills the parking order until the hand moves on its own."
        ),
    },
    {
        "key": "numbers",
        "name": "French Numbers and Time",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "French numbers 1-16 have unique names: un, deux, trois, quatre, "
            "cinq, six, sept, huit, neuf, dix, onze, douze, treize, quatorze, "
            "quinze, seize. Then 17-19 build on ten: dix-sept, dix-huit, "
            "dix-neuf. The tens: vingt (20), trente (30), quarante (40), "
            "cinquante (50), soixante (60). Seventy is sixty-ten: "
            "soixante-dix (70), soixante et onze (71), soixante-douze (72). "
            "Eighty is four-twenties: quatre-vingts (80), quatre-vingt-un "
            "(81), quatre-vingt-dix (90), quatre-vingt-dix-neuf (99). Then "
            "cent (100), mille (1,000), million, milliard. Belgium and "
            "Switzerland simplify with septante, huitante/octante, nonante. "
            "Ordinals: premier/premiere (1st), deuxieme, troisieme - Le "
            "premier jour. (The first day.) Days: lundi, mardi, mercredi, "
            "jeudi, vendredi, samedi, dimanche - Je travaille lundi. (I work "
            "on Monday.) Months: janvier, fevrier, mars, avril, mai, juin, "
            "juillet, aout, septembre, octobre, novembre, decembre - Mon "
            "anniversaire est en mai. (My birthday is in May.) Seasons: le "
            "printemps, l'ete, l'automne, l'hiver - L'ete est chaud. (Summer "
            "is hot.) Clock time: Il est une heure. (It is one o'clock.) Il "
            "est trois heures et demie. (It is half past three.) Il est huit "
            "heures moins le quart. (It is quarter to eight.) Il est midi. "
            "(It is noon.) Il est minuit. (It is midnight.) Dates: le 17 "
            "octobre 2026, le premier mai - Nous sommes le lundi 20 octobre. "
            "(Today is Monday, October 20.) Quel age as-tu? J'ai trente ans. "
            "(How old are you? I am thirty.)"
        ),
        "how_it_works": (
            "French numbers work as a base-20 fossil inside a base-10 "
            "system: the Celtic vigesimal habit survived in quatre-vingts "
            "(four-twenties) and soixante-dix (sixty-ten). Build any number "
            "by stacking: tens + ones with hyphens (vingt-deux), except "
            "with et for the ones ending in 1 up to 60 (vingt et un, "
            "trente et un) - but not after 80 (quatre-vingt-un, no et). "
            "Quatre-vingts takes an -s only when it is exactly 80 with "
            "nothing after it. Cent and vingt take -s only when multiplied "
            "and final: quatre-vingts, deux cents, but deux cent cinquante. "
            "Time reads the clock face in words: hours + et quart/et demie/"
            "moins le quart, or the 24-hour railway style (quinze heures "
            "trente = 3:30 PM). Dates put the day before the month, and the "
            "year is spoken in hundreds: mil neuf cent quatre-vingt-dix."
        ),
        "key_points": [
            "1-16 unique; 70 = soixante-dix, 80 = quatre-vingts, 90 = quatre-vingt-dix.",
            "Use et for -et-un up to 60; no et after 80; -s rules for vingt and cent.",
            "Belgium/Switzerland: septante, huitante/octante, nonante.",
            "Time: et quart, et demie, moins le quart; midi = noon, minuit = midnight.",
            "Dates: day before month (le 17 octobre); age uses avoir (J'ai trente ans).",
        ],
        "requirements": [
            "1-100 with the 70/80/90 constructions, ordinals, days, months, seasons, clock time, dates - each with translated example sentences.",
            "The -s rules for quatre-vingts and cents stated.",
            "Belgian/Swiss variants noted.",
        ],
        "standards": [
            "Number formation follows Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Regional variants follow the OIF 2022 report.",
        ],
        "citations": [CIT_GREV, CIT_OIF, CIT_PRICE],
        "sig_lens": (
            "The Signature read: the numbers are the measuring dies of the "
            "seal-press - base ten for the world, base twenty for the "
            "ancestors, both striking true. The Signature Language Method "
            "counts to one hundred aloud daily until the dies seat "
            "themselves."
        ),
    },
    {
        "key": "greetings",
        "name": "French Greetings and Everyday Phrases",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "Thirty greetings, farewells, and politeness phrases with usage "
            "notes: Bonjour (Hello/Good day - the universal daytime greeting, "
            "say it everywhere you enter). Bonsoir (Good evening - after "
            "about 6 PM). Salut (Hi/Bye - informal, friends only). Au revoir "
            "(Goodbye). A bientot "
            "(See you soon). A demain (See you tomorrow). A tout a l'heure "
            "(See you later today). Bonne journee (Have a good day - said "
            "when parting). Bonne soiree (Have a good evening). Bonne nuit "
            "(Good night - only at bedtime). Merci (Thank you). Merci "
            "beaucoup (Thank you very much). De rien (You are welcome - "
            "informal). Je vous en prie (You are welcome - formal). Je t'en "
            "prie (You are welcome - informal). S'il vous plait (Please - "
            "formal). S'il te plait (Please - informal). Pardon (Sorry/Excuse "
            "me - bumping into someone). Excusez-moi (Excuse me - formal, "
            "getting attention). Desole/Desolee (Sorry - apologizing). "
            "Enchante/Enchantee (Nice to meet you - said when introduced). "
            "Comment allez-vous? (How are you? - formal.) Comment ca va? "
            "(How is it going? - informal.) Ca va? (How are you? - very "
            "informal.) Bienvenue "
            "(Welcome). Felicitations (Congratulations). Bonne chance (Good "
            "luck). Bon courage (a uniquely French wish: strength for a hard "
            "task). Bon appetit (Enjoy your meal - said before eating). Joyeux "
            "anniversaire (Happy "
            "birthday). Always greet shopkeepers with Bonjour on entering - "
            "skipping it is the fastest way to seem rude in France."
        ),
        "how_it_works": (
            "French greetings work as social keys: the right key opens the "
            "door, the wrong one leaves it shut. Bonjour is not optional - "
            "it is the toll you pay on entering any shop, office, or "
            "elevator, and Bonsoir replaces it after about six in the "
            "evening. La bise - the cheek kiss, two to four depending on "
            "the region - greets friends and family; a handshake covers "
            "everyone else. The tu/vous line runs through every phrase: "
            "S'il vous plait to strangers, S'il te plait to friends. Bon "
            "courage has no English equivalent and marks you as an insider "
            "the first time you use it correctly. Farewells mirror the "
            "formality: Au revoir for strangers, Salut or A plus for "
            "friends."
        ),
        "key_points": [
            "Bonjour is mandatory on entering shops and offices; Bonsoir after ~6 PM.",
            "Salut/Coucou are friends-only; Au revoir/A bientot for parting.",
            "Politeness runs on tu/vous: S'il vous plait vs S'il te plait.",
            "La bise (cheek kiss) for friends and family; handshake otherwise.",
            "Bon courage is the untranslatable French wish for hard tasks.",
        ],
        "requirements": [
            "30 greetings/farewells/politeness phrases, each with English and a usage note.",
            "The mandatory-Bonjour rule and la bise explained.",
            "Tu/vous split across the phrases.",
        ],
        "standards": [
            "Usage notes follow Battye, Hintze, and Rowlett on French sociolinguistics.",
            "Pragmatics cross-checked with Fagyal, Kibbee, and Jenkins.",
        ],
        "citations": [CIT_BATTYE, CIT_FAGYAL, CIT_OIF],
        "sig_lens": (
            "The Signature read: a greeting is the first press of the seal "
            "on a new page - Bonjour opens the ledger, Au revoir closes it. "
            "The Signature Language Method greets every room aloud, because "
            "a sealer who will not say Bonjour will not be trusted with the "
            "press."
        ),
    },
]
