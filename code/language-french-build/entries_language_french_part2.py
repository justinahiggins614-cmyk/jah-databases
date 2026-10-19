#!/usr/bin/env python3
"""Entries part 2 (records 10, 11-34) for The French Language Database (language-french).

Compounded records 10-23 (ranks 6-9) and advanced records 24-34 (ranks 9-10).
Same canon as part 1: full sentences everywhere, French + English.
"""

ENTRIES_2 = [
    {
        "key": "grammar",
        "name": "French Grammar Essentials",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The skeleton of French in seven rules, each with translated "
            "examples. 1) Word order is subject-verb-object: Le chat mange "
            "la souris. (The cat eats the mouse.) Adverbs of time often move "
            "to the front: Hier, je suis alle au marche. (Yesterday, I went "
            "to the market.) 2) Gender: every noun is masculine or feminine, "
            "and articles and adjectives follow: le petit garcon / la petite "
            "fille. (the little boy / the little girl.) 3) Number: plurals "
            "add silent -s, heard on the article and adjectives: les petits "
            "garcons. (the little boys.) 4) Articles: definite le/la/les "
            "(the), indefinite un/une/des (a/some), partitive du/de la/des "
            "for uncountables - Je bois du cafe. (I drink coffee.) Je mange "
            "de la soupe. (I eat soup.) After negation, du/de la/des become "
            "de: Je ne bois pas de cafe. (I do not drink coffee.) 5) "
            "Negation wraps the verb: ne + verb + pas - Je ne parle pas "
            "anglais. (I do not speak English.) With compound tenses the "
            "block wraps the auxiliary: Je n'ai pas fini. (I have not "
            "finished.) Common negatives: ne...jamais (never), ne...plus "
            "(no longer), ne...rien (nothing), ne...personne (nobody) - Je "
            "ne vois personne. (I see nobody.) 6) Questions form three ways: "
            "rising intonation (Tu viens? - Are you coming?), est-ce que "
            "(Est-ce que tu viens? - Are you coming?), and inversion "
            "(Viens-tu? - Are you coming?) - inversion is formal and drops "
            "with je in speech. 7) Adjective position: most follow the noun "
            "(une maison blanche - a white house), BANGS adjectives precede "
            "(un grand homme - a great man), and some change meaning with "
            "position (un pauvre homme = unfortunate; un homme pauvre = "
            "broke). Possession uses de, never an apostrophe-s: le livre de "
            "Marie (Marie's book), never *le livre d'Marie."
        ),
        "how_it_works": (
            "French grammar works as a wrapping system: negation wraps the "
            "verb (ne...pas), object pronouns huddle before the verb "
            "(Je le lui donne), and adjectives orbit their noun in fixed "
            "positions. The partitive article is the English some made "
            "mandatory - French will not let you say bare coffee or bare "
            "soup; it demands du cafe, de la soupe. Gender is the gravity "
            "of the system: get the article right and the adjectives fall "
            "into line automatically. Questions escalate in formality from "
            "intonation (friends) through est-ce que (neutral) to inversion "
            "(writing and formal speech). The whole skeleton fits on one "
            "page, and every later record hangs flesh on these seven bones."
        ),
        "key_points": [
            "SVO word order; time adverbs may front the sentence.",
            "Gender + number agreement drives articles and adjectives.",
            "Definite/indefinite/partitive articles; partitives become de after negation.",
            "Negation wraps the verb: ne...pas, ne...jamais, ne...plus, ne...rien, ne...personne.",
            "Three question forms: intonation, est-ce que, inversion - in rising formality.",
            "Adjective position: default after noun; BANGS before; some change meaning with position.",
        ],
        "requirements": [
            "Word order, gender, number, articles, negation, question formation - each rule with translated example sentences.",
            "Partitive articles and the de-after-negation rule stated.",
            "At least 14 translated example sentences across the rules.",
        ],
        "standards": [
            "Rules follow Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Terminology follows Price, A Comprehensive French Grammar 7th ed.",
        ],
        "citations": [
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Price G. A Comprehensive French Grammar. 7th ed. Wiley-Blackwell; 2007.",
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
        ],
        "sig_lens": (
            "The Signature read: grammar is the frame of the press - seven "
            "iron rules holding the dies in alignment. The Signature "
            "Language Method squares the frame first, because no seal "
            "presses true in a crooked frame."
        ),
    },
    {
        "key": "home",
        "name": "French Sentences: Home and Family",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the house and the family: 1. J'habite dans "
            "une grande maison. (I live in a big house.) 2. Le salon est "
            "lumineux. (The living room is bright.) 3. La cuisine est a cote "
            "de la salle a manger. (The kitchen is next to the dining room.) "
            "4. Ma chambre est en haut. (My bedroom is upstairs.) 5. La salle "
            "de bain a une douche. (The bathroom has a shower.) 6. Le canape "
            "est confortable. (The sofa is comfortable.) 7. La table est en "
            "bois. (The table is wooden.) 8. Les rideaux sont bleus. (The "
            "curtains are blue.) 9. Mon pere regarde la television. (My "
            "father watches television.) 10. Ma mere prepare le repas. (My "
            "mother prepares the meal.) 11. Mon frere joue dans le jardin. "
            "(My brother plays in the garden.) 12. Ma soeur lit un livre. "
            "(My sister reads a book.) 13. Mes grands-parents habitent a la "
            "campagne. (My grandparents live in the countryside.) 14. Mon "
            "oncle et ma tante viennent dimanche. (My uncle and aunt come on "
            "Sunday.) 15. Mes cousins sont en vacances. (My cousins are on "
            "vacation.) 16. Le chien dort sous la table. (The dog sleeps "
            "under the table.) 17. Le chat est sur le lit. (The cat is on "
            "the bed.) 18. Nous mangeons ensemble le soir. (We eat together "
            "in the evening.) 19. La cle est sur l'etagere. (The key is on "
            "the shelf.) 20. Ferme la porte, s'il te plait. (Close the door, "
            "please.)"
        ),
        "how_it_works": (
            "Home sentences work as the learner's first territory: the "
            "vocabulary of rooms and relatives is used daily, so it sticks "
            "fast. Notice the prepositions of place - dans (in), sur (on), "
            "sous (under), a cote de (next to), en haut (upstairs) - each "
            "one a small machine for locating things. Family words carry "
            "possessives (mon, ma, mes) that agree with the noun, not the "
            "owner: mon pere, ma mere, mes parents. Possessive + family "
            "member is the fastest drill for possessive agreement in the "
            "whole language."
        ),
        "key_points": [
            "Rooms: le salon, la cuisine, la salle a manger, la chambre, la salle de bain.",
            "Family: le pere, la mere, le frere, la soeur, les grands-parents, l'oncle, la tante, les cousins.",
            "Place prepositions: dans, sur, sous, a cote de, en haut.",
            "Possessives agree with the noun: mon pere, ma mere, mes parents.",
            "Furniture and objects recycle gender practice: le canape, la table, les rideaux.",
        ],
        "requirements": [
            "20 sentences covering house, rooms, furniture, and family members, each translated.",
            "Place prepositions and possessive agreement demonstrated.",
        ],
        "standards": [
            "Vocabulary follows the Academie francaise dictionary, 9th edition.",
            "Sentence patterns follow Price 7th ed.",
        ],
        "citations": [
            "Academie francaise. Dictionnaire de l'Academie francaise, 9e edition. In progress.",
            "Price G. A Comprehensive French Grammar. 7th ed. Wiley-Blackwell; 2007.",
        ],
        "sig_lens": (
            "The Signature read: the home is the first workshop - every "
            "room a station of the press, every relative a fellow sealer. "
            "The Signature Language Method stamps the home first, because "
            "the hand learns fastest where it lives."
        ),
    },
    {
        "key": "food",
        "name": "French Sentences: Food and Cooking",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for meals, ingredients, cooking, and the "
            "restaurant: 1. Je prends le petit dejeuner a sept heures. (I "
            "have breakfast at seven.) 2. Le dejeuner est a midi. (Lunch is "
            "at noon.) 3. Nous dinons a huit heures. (We have dinner at "
            "eight.) 4. J'aime le pain frais. (I like fresh bread.) 5. Le "
            "fromage francais est celebre. (French cheese is famous.) 6. "
            "Elle coupe les legumes. (She cuts the vegetables.) 7. Il fait "
            "bouillir l'eau. (He boils the water.) 8. Ajoute du sel, s'il te "
            "plait. (Add salt, please.) 9. La soupe est trop chaude. (The "
            "soup is too hot.) 10. Ce gateau est delicieux. (This cake is "
            "delicious.) 11. Je bois un verre de vin rouge. (I drink a glass "
            "of red wine.) 12. Tu veux du cafe ou du the? (Do you want "
            "coffee or tea?) 13. L'addition, s'il vous plait. (The bill, "
            "please.) 14. Le serveur apporte le menu. (The waiter brings the "
            "menu.) 15. Je voudrais le plat du jour. (I would like the dish "
            "of the day.) 16. La viande est bien cuite. (The meat is well "
            "done.) 17. Le poisson est frais. (The fish is fresh.) 18. Avez-"
            "vous une table pour deux? (Do you have a table for two?) 19. "
            "C'etait excellent, merci. (That was excellent, thank you.) 20. "
            "Bon appetit! (Enjoy your meal!)"
        ),
        "how_it_works": (
            "Food sentences work as the partitive-article gym: du pain, de "
            "la soupe, des legumes - uncountables demand their article and "
            "the gym builds the reflex. Restaurant French runs on the "
            "conditional of politeness: Je voudrais (I would like) opens "
            "every order, never the blunt Je veux. Cooking verbs (couper, "
            "faire bouillir, ajouter, melanger) are regular first-group "
            "verbs, so the kitchen doubles as conjugation practice. Meal "
            "names anchor the day: petit dejeuner, dejeuner, diner - and the "
            "French dinner at eight explains why restaurants fill late."
        ),
        "key_points": [
            "Meals: le petit dejeuner, le dejeuner, le diner; dinner is late, around eight.",
            "Partitive drill: du pain, de la soupe, des legumes.",
            "Restaurant politeness: Je voudrais, L'addition s'il vous plait.",
            "Cooking verbs are regular -er verbs: couper, ajouter, melanger.",
            "Taste adjectives: delicieux, frais, bien cuit, trop chaud.",
        ],
        "requirements": [
            "20 sentences covering meals, ingredients, cooking actions, and restaurant, each translated.",
            "Partitive articles and politeness conditional demonstrated.",
        ],
        "standards": [
            "Vocabulary follows the Academie francaise dictionary, 9th edition.",
            "Usage follows Battye, Hintze, and Rowlett.",
        ],
        "citations": [
            "Academie francaise. Dictionnaire de l'Academie francaise, 9e edition. In progress.",
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
        ],
        "sig_lens": (
            "The Signature read: the kitchen is the proofing room - every "
            "dish a test strike of the day's seal. The Signature Language "
            "Method tastes every sentence before serving it, because a "
            "sealer who will not taste will not trust the press."
        ),
    },
    {
        "key": "travel",
        "name": "French Sentences: Travel and Directions",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for transport, directions, tickets, and "
            "lodging: 1. Ou est la gare, s'il vous plait? (Where is the "
            "train station, please?) 2. Prenez la premiere rue a droite. "
            "(Take the first street on the right.) 3. Allez tout droit. (Go "
            "straight ahead.) 4. C'est loin d'ici? (Is it far from here?) 5. "
            "Le train part a neuf heures. (The train leaves at nine.) 6. "
            "Mon vol est retarde. (My flight is delayed.) 7. Je voudrais un "
            "billet aller-retour. (I would like a round-trip ticket.) 8. "
            "Quel quai pour Lyon? (Which platform for Lyon?) 9. Le bus "
            "s'arrete ici. (The bus stops here.) 10. Ou puis-je louer une "
            "voiture? (Where can I rent a car?) 11. J'ai reserve une chambre "
            "pour deux nuits. (I reserved a room for two nights.) 12. La "
            "chambre est au deuxieme etage. (The room is on the second "
            "floor.) 13. Le petit dejeuner est-il compris? (Is breakfast "
            "included?) 14. A quelle heure est le check-out? (What time is "
            "check-out?) 15. Pouvez-vous appeler un taxi? (Can you call a "
            "taxi?) 16. Combien coute le trajet? (How much is the ride?) 17. "
            "Je cherche un hotel pas cher. (I am looking for a cheap hotel.) "
            "18. La plage est a dix minutes a pied. (The beach is ten "
            "minutes on foot.) 19. Nous visitons le musee demain. (We visit "
            "the museum tomorrow.) 20. Bon voyage! (Have a good trip!)"
        ),
        "how_it_works": (
            "Travel sentences work as the imperative gym: Prenez, Allez, "
            "Tournez - directions run on commands, and the vous form keeps "
            "them polite to strangers. Transport verbs split by auxiliary: "
            "aller takes etre (je suis alle), while most others take avoir. "
            "Prepositions of movement are precise: a Paris (to Paris), en "
            "France (to France, feminine countries), au Japon (masculine), "
            "aux Etats-Unis (plural). Hotel French recycles the politeness "
            "conditional (Je voudrais, Pouvez-vous) and numbers (deuxieme "
            "etage, deux nuits). Learn the direction trio - a droite, a "
            "gauche, tout droit - and any city becomes navigable."
        ),
        "key_points": [
            "Directions run on the polite imperative: Prenez, Allez, Tournez.",
            "Direction trio: a droite, a gauche, tout droit.",
            "Country prepositions: a Paris, en France, au Japon, aux Etats-Unis.",
            "Tickets and lodging: un billet aller-retour, une chambre pour deux nuits.",
            "Aller takes etre as auxiliary: je suis alle.",
        ],
        "requirements": [
            "20 sentences covering transport, directions, tickets, and lodging, each translated.",
            "Imperative directions and country prepositions demonstrated.",
        ],
        "standards": [
            "Preposition rules follow Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Transport vocabulary follows the OIF 2022 report usage.",
        ],
        "citations": [
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Organisation internationale de la Francophonie. La langue francaise dans le monde 2022. Gallimard; 2022.",
        ],
        "sig_lens": (
            "The Signature read: the road is the long bed of the press and "
            "every direction a registration mark - a droite, a gauche, tout "
            "droit keep the sheet aligned. The Signature Language Method "
            "walks the learner through a real station until the marks read "
            "themselves."
        ),
    },
    {
        "key": "work",
        "name": "French Sentences: Work and School",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for jobs, the office, the classroom, and "
            "learning: 1. Je suis ingenieur. (I am an engineer - no article "
            "for professions.) 2. Elle est medecin. (She is a doctor.) 3. "
            "Il travaille dans une banque. (He works in a bank.) 4. Nous "
            "avons une reunion a dix heures. (We have a meeting at ten.) 5. "
            "Envoyez-moi le rapport, s'il vous plait. (Send me the report, "
            "please.) 6. Le patron est en voyage. (The boss is traveling.) 7. "
            "Je cherche un emploi. (I am looking for a job.) 8. Quel est "
            "votre metier? (What is your job?) 9. Je commence a neuf heures. "
            "(I start at nine.) 10. La pause dejeuner dure une heure. (The "
            "lunch break lasts an hour.) 11. Les eleves ecoutent le "
            "professeur. (The pupils listen to the teacher.) 12. J'apprends "
            "le francais depuis un an. (I have been learning French for a "
            "year.) 13. Le cours commence a huit heures et demie. (The class "
            "starts at eight thirty.) 14. Ouvrez vos livres page dix. (Open "
            "your books to page ten.) 15. Ecrivez la reponse au tableau. "
            "(Write the answer on the board.) 16. J'ai un examen demain. (I "
            "have an exam tomorrow.) 17. Elle a reussi son bac. (She passed "
            "her baccalaureat.) 18. L'universite est en centre-ville. (The "
            "university is downtown.) 19. Mon collegue m'aide beaucoup. (My "
            "colleague helps me a lot.) 20. Bon travail! (Good work!)"
        ),
        "how_it_works": (
            "Work sentences work on the no-article profession rule: Je suis "
            "ingenieur, never *Je suis un ingenieur - the article appears "
            "only with a qualifier (C'est un bon ingenieur). School French "
            "runs on classroom imperatives (Ouvrez, Ecrivez, Repetez) and "
            "the depuis construction for ongoing time: J'apprends depuis un "
            "an uses the present tense where English uses the perfect. "
            "Office politeness stacks the conditional and the imperative "
            "softened by s'il vous plait: Envoyez-moi le rapport, s'il vous "
            "plait. The bac (baccalaureat) is the national exam at the end "
            "of French secondary school - reussir son bac is a life "
            "milestone."
        ),
        "key_points": [
            "Professions take no article: Je suis ingenieur.",
            "Depuis + present for ongoing time: J'apprends depuis un an.",
            "Classroom imperatives: Ouvrez, Ecrivez, Repetez.",
            "Office politeness: conditional + s'il vous plait.",
            "Le bac is the national secondary-school exam.",
        ],
        "requirements": [
            "20 sentences covering jobs, office, classroom, and learning, each translated.",
            "No-article profession rule and depuis construction demonstrated.",
        ],
        "standards": [
            "Grammar follows Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Institutional terms follow the Academie francaise dictionary.",
        ],
        "citations": [
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Academie francaise. Dictionnaire de l'Academie francaise, 9e edition. In progress.",
        ],
        "sig_lens": (
            "The Signature read: the office is the day-shift of the press "
            "and the classroom the night-shift - one stamps the world's "
            "business, the other stamps the next sealers. The Signature "
            "Language Method apprentices the learner at both benches."
        ),
    },
    {
        "key": "health",
        "name": "French Sentences: Health and the Body",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for body parts, symptoms, the doctor, and the "
            "pharmacy: 1. J'ai mal a la tete. (I have a headache - "
            "literally, I have pain at the head.) 2. J'ai mal au dos. (My "
            "back hurts.) 3. J'ai mal au ventre. (My stomach hurts.) 4. Je "
            "me suis foule la cheville. (I sprained my ankle.) 5. Elle s'est "
            "casse le bras. (She broke her arm.) 6. J'ai de la fievre. (I "
            "have a fever.) 7. Je suis enrhume. (I have a cold.) 8. Je tousse "
            "beaucoup. (I cough a lot.) 9. J'ai besoin d'un medecin. (I need "
            "a doctor.) 10. Appelez une ambulance! (Call an ambulance!) 11. "
            "Ou est la pharmacie la plus proche? (Where is the nearest "
            "pharmacy?) 12. Avez-vous quelque chose contre la douleur? (Do "
            "you have something for pain?) 13. Prenez ce medicament deux "
            "fois par jour. (Take this medicine twice a day.) 14. Le docteur "
            "m'a donne une ordonnance. (The doctor gave me a prescription.) "
            "15. Je suis allergique aux arachides. (I am allergic to "
            "peanuts.) 16. Mon fils a la grippe. (My son has the flu.) 17. "
            "Respirez profondement. (Breathe deeply.) 18. Ouvrez la bouche. "
            "(Open your mouth.) 19. Ca va mieux aujourd'hui. (It is better "
            "today.) 20. Reposez-vous bien. (Rest well.)"
        ),
        "how_it_works": (
            "Health sentences work on the avoir mal a construction: French "
            "says I have pain at the head, never *my head hurts with "
            "possessives - body parts take the definite article (Je me suis "
            "foule la cheville, not *ma cheville) because the reflexive "
            "pronoun already says whose. Reflexive verbs dominate the "
            "symptom list: se fouler, se casser, se reposer. Pharmacy French "
            "is polite-request French (Avez-vous quelque chose contre...?), "
            "and dosage runs on fois par jour. The green cross marks the "
            "pharmacie, which in France handles minor ailments directly - "
            "the pharmacist is a first-line clinician."
        ),
        "key_points": [
            "Pain: J'ai mal a la tete / au dos / au ventre.",
            "Body parts take the definite article with reflexives: Je me suis foule la cheville.",
            "Reflexive verbs dominate symptoms: se casser, se fouler, se reposer.",
            "Pharmacy requests: Avez-vous quelque chose contre...?",
            "Dosage: deux fois par jour; the green cross marks the pharmacie.",
        ],
        "requirements": [
            "20 sentences covering body parts, symptoms, doctor visit, and pharmacy, each translated.",
            "Avoir mal a and definite-article body parts demonstrated.",
        ],
        "standards": [
            "Constructions follow Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Medical vocabulary follows the Academie francaise dictionary.",
        ],
        "citations": [
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Academie francaise. Dictionnaire de l'Academie francaise, 9e edition. In progress.",
        ],
        "sig_lens": (
            "The Signature read: the body is the sealer's own press - when "
            "it jams, the whole shop stops. The Signature Language Method "
            "teaches the pain-words first, because a sealer must be able to "
            "call for help in any shop on earth."
        ),
    },
    {
        "key": "emotions",
        "name": "French Sentences: Emotions and Feelings",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for happy, sad, angry, afraid, love, and "
            "surprise: 1. Je suis tres heureux aujourd'hui. (I am very happy "
            "today.) 2. Elle est ravie de te voir. (She is delighted to see "
            "you.) 3. Nous sommes fiers de toi. (We are proud of you.) 4. "
            "Il est triste depuis hier. (He has been sad since yesterday.) 5. "
            "Elle pleure de joie. (She cries with joy.) 6. J'ai le cafard. "
            "(I feel blue - literally, I have the cockroach.) 7. Tu me "
            "manques. (I miss you - literally, you are missing to me.) 8. "
            "Il est en colere. (He is angry.) 9. Ne te fache pas! (Do not get "
            "angry!) 10. Ca m'enerve. (That annoys me.) 11. J'ai peur du "
            "noir. (I am afraid of the dark.) 12. N'aie pas peur. (Do not be "
            "afraid.) 13. Je t'aime. (I love you.) 14. Ils s'aiment beaucoup. "
            "(They love each other very much.) 15. Mon coeur bat vite. (My "
            "heart beats fast.) 16. Quelle surprise! (What a surprise!) 17. "
            "Je n'en reviens pas! (I cannot get over it!) 18. C'est "
            "incroyable! (It is incredible!) 19. Je suis soulage. (I am "
            "relieved.) 20. Tout va bien se passer. (Everything will be "
            "fine.)"
        ),
        "how_it_works": (
            "Emotion sentences work on French's famous inversions: Tu me "
            "manques means I miss you - the grammar runs backward from "
            "English, with the missed person as the subject. Avoir carries "
            "many feelings where English uses to be: avoir peur (to be "
            "afraid), avoir honte (to be ashamed), avoir le cafard (to feel "
            "blue). Etre carries the states: etre heureux, etre triste, "
            "etre en colere. Reflexives color relationships: s'aimer, se "
            "facher, se disputer. The subjunctive often follows emotion "
            "verbs (Je suis content que tu viennes), which makes this set "
            "the emotional doorway to the subjunctive mood."
        ),
        "key_points": [
            "Tu me manques = I miss you (grammar runs backward from English).",
            "Avoir carries feelings: avoir peur, avoir honte, avoir le cafard.",
            "Etre carries states: etre heureux, etre triste, etre en colere.",
            "Reflexives for relationships: s'aimer, se facher, se disputer.",
            "Emotion verbs open the door to the subjunctive.",
        ],
        "requirements": [
            "20 sentences covering happy, sad, angry, afraid, love, surprise, each translated.",
            "Tu me manques inversion and avoir-vs-etre emotion split demonstrated.",
        ],
        "standards": [
            "Constructions follow Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Idioms follow the Academie francaise dictionary.",
        ],
        "citations": [
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
        ],
        "sig_lens": (
            "The Signature read: feelings are the ink of the seal - "
            "invisible until pressed, indelible once stamped. The "
            "Signature Language Method presses the heart-words deep, "
            "because a seal without ink is only an impression."
        ),
    },
    {
        "key": "nature",
        "name": "French Sentences: Nature and Weather",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for animals, plants, seasons, and weather "
            "talk: 1. Le chien aboie. (The dog barks.) 2. Le chat dort au "
            "soleil. (The cat sleeps in the sun.) 3. Les oiseaux chantent le "
            "matin. (The birds sing in the morning.) 4. Il y a un ecureuil "
            "dans l'arbre. (There is a squirrel in the tree.) 5. Les fleurs "
            "poussent au printemps. (Flowers grow in spring.) 6. Les feuilles "
            "tombent en automne. (Leaves fall in autumn.) 7. Quel temps fait-"
            "il? (What is the weather like?) 8. Il fait beau aujourd'hui. "
            "(The weather is nice today.) 9. Il pleut des cordes. (It is "
            "pouring - literally, it rains ropes.) 10. Il neige en hiver. "
            "(It snows in winter.) 11. Il fait un froid de canard. (It is "
            "bitterly cold - literally, a duck cold.) 12. Le ciel est "
            "nuageux. (The sky is cloudy.) 13. Il y a du vent. (It is windy.) "
            "14. L'orage approche. (The storm approaches.) 15. Il fait trente "
            "degres. (It is thirty degrees.) 16. Le soleil se couche a huit "
            "heures. (The sun sets at eight.) 17. La riviere est gelee. (The "
            "river is frozen.) 18. Nous nous promenons dans la foret. (We "
            "walk in the forest.) 19. La montagne est couverte de neige. "
            "(The mountain is covered with snow.) 20. Demain, il fera beau. "
            "(Tomorrow the weather will be nice.)"
        ),
        "how_it_works": (
            "Weather sentences work on the il fait construction: French "
            "describes weather with faire (to make/do) - Il fait beau, Il "
            "fait chaud, Il fait un froid de canard - where English uses to "
            "be. Impersonal verbs run the sky: il pleut, il neige, il gele. "
            "Animal sounds use specific verbs (aboyer, miauler, chanter), "
            "and nature vocabulary recycles gender practice across the "
            "seasons (le printemps but la saison). Weather small talk is the "
            "universal French icebreaker - Quel temps fait-il? opens more "
            "conversations than any other question."
        ),
        "key_points": [
            "Weather uses il fait: Il fait beau, Il fait chaud, Il fait froid.",
            "Impersonal sky verbs: il pleut, il neige, il gele.",
            "Idioms: Il pleut des cordes (pouring), un froid de canard (bitter cold).",
            "Animal verbs: aboyer, miauler, chanter.",
            "Quel temps fait-il? is the universal icebreaker.",
        ],
        "requirements": [
            "20 sentences covering animals, plants, seasons, and weather talk, each translated.",
            "Il fait construction and impersonal weather verbs demonstrated.",
        ],
        "standards": [
            "Constructions follow Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Idioms follow the Academie francaise dictionary.",
        ],
        "citations": [
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Price G. A Comprehensive French Grammar. 7th ed. Wiley-Blackwell; 2007.",
        ],
        "sig_lens": (
            "The Signature read: the sky is the great unsealed page - the "
            "weather writes on it daily and every French speaker reads the "
            "script aloud. The Signature Language Method reads the sky "
            "first, because the press runs best in fair weather."
        ),
    },
    {
        "key": "shopping",
        "name": "French Sentences: Shopping and Money",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the market, prices, bargaining, and "
            "paying: 1. Combien coute ce fromage? (How much is this cheese?) "
            "2. C'est trop cher. (It is too expensive.) 3. Avez-vous quelque "
            "chose de moins cher? (Do you have something cheaper?) 4. Je "
            "cherche une taille medium. (I am looking for a medium size.) 5. "
            "Puis-je essayer ceci? (Can I try this on?) 6. La cabine "
            "d'essayage est la-bas. (The fitting room is over there.) 7. "
            "C'est la bonne taille. (It is the right size.) 8. Je vais "
            "prendre celui-ci. (I will take this one.) 9. Faites-vous des "
            "reductions? (Do you give discounts?) 10. C'est mon dernier "
            "prix. (This is my last price.) 11. Je paie en especes. (I pay "
            "cash.) 12. Acceptez-vous la carte bancaire? (Do you accept bank "
            "cards?) 13. Le marche est ouvert le dimanche. (The market is "
            "open on Sunday.) 14. Les fruits sont frais ce matin. (The fruit "
            "is fresh this morning.) 15. Un kilo de pommes, s'il vous plait. "
            "(A kilo of apples, please.) 16. Ca fait combien en tout? (How "
            "much is that altogether?) 17. Voila vingt euros. (Here are "
            "twenty euros.) 18. Gardez la monnaie. (Keep the change.) 19. "
            "Avez-vous un sac? (Do you have a bag?) 20. Merci, bonne "
            "journee! (Thank you, have a good day!)"
        ),
        "how_it_works": (
            "Shopping sentences work as the numbers gym in the wild: prices "
            "force fast decoding of soixante-dix-neuf euros and "
            "quatre-vingt-quinze centimes under pressure. Bargaining runs on "
            "polite conditionals (Je vous propose... - I propose to you) "
            "and the ritual C'est trop cher. Demonstratives do the pointing: "
            "celui-ci (this one) versus celui-la (that one). Payment "
            "vocabulary is modern and practical: en especes, par carte "
            "bancaire, sans contact (contactless). The market sentence Un "
            "kilo de pommes drills the de of quantity - always de, never des, "
            "after expressions of amount."
        ),
        "key_points": [
            "Prices drill number decoding under pressure: soixante-dix-neuf euros.",
            "Bargaining ritual: C'est trop cher / C'est mon dernier prix.",
            "Demonstratives for pointing: celui-ci vs celui-la.",
            "Payment: en especes, par carte bancaire, sans contact.",
            "Quantity takes de: un kilo de pommes, beaucoup de monde.",
        ],
        "requirements": [
            "20 sentences covering market, prices, bargaining, and paying, each translated.",
            "Bargaining phrases and quantity-de demonstrated.",
        ],
        "standards": [
            "Usage follows Battye, Hintze, and Rowlett.",
            "Grammar follows Price 7th ed.",
        ],
        "citations": [
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
            "Price G. A Comprehensive French Grammar. 7th ed. Wiley-Blackwell; 2007.",
        ],
        "sig_lens": (
            "The Signature read: the market is the public counter of the "
            "press - every price a small seal struck between buyer and "
            "seller. The Signature Language Method haggles aloud until the "
            "numbers strike themselves."
        ),
    },
    {
        "key": "friendship",
        "name": "French Sentences: Friendship and Social Life",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for meeting people, invitations, and "
            "celebrations: 1. Enchante de faire votre connaissance. (Nice to "
            "meet you.) 2. Je te presente mon ami Paul. (Let me introduce my "
            "friend Paul.) 3. Tu viens d'ou? (Where are you from?) 4. Je "
            "viens du Canada. (I come from Canada.) 5. Qu'est-ce que tu fais "
            "dans la vie? (What do you do in life?) 6. Tu veux prendre un "
            "cafe? (Do you want to grab a coffee?) 7. Avec plaisir! (With "
            "pleasure!) 8. Je t'invite a diner samedi. (I invite you to "
            "dinner Saturday.) 9. La fete commence a huit heures. (The party "
            "starts at eight.) 10. Apporte quelque chose a boire. (Bring "
            "something to drink.) 11. Joyeux anniversaire! (Happy birthday!) "
            "12. Quel age as-tu? (How old are you?) 13. J'ai trente ans. (I "
            "am thirty.) 14. Felicitations pour ton mariage! (Congratulations "
            "on your wedding!) 15. On se voit bientot? (Shall we see each "
            "other soon?) 16. Passe le bonjour a ta famille. (Say hello to "
            "your family for me.) 17. C'etait une super soiree. (That was a "
            "great evening.) 18. Merci pour l'invitation. (Thanks for the "
            "invitation.) 19. On reste en contact. (Let us stay in touch.) "
            "20. A la prochaine! (Until next time!)"
        ),
        "how_it_works": (
            "Friendship sentences work on the tu fast-track: friends switch "
            "to tu almost immediately, and invitations run on the informal "
            "register (Tu veux prendre un cafe?). Introductions follow the "
            "script - Je te presente X / Enchante - and the cheek-kiss count "
            "(two in Paris, three or four elsewhere) seals the meeting. "
            "Celebrations recycle the wish formulas: Joyeux anniversaire, "
            "Felicitations, Bonne annee. The reflexive se voir (to see each "
            "other) and the pronoun on (On se voit bientot?) make plans "
            "without committing a subject - the social softener of French "
            "planning."
        ),
        "key_points": [
            "Friends switch to tu fast; invitations run informal.",
            "Introduction script: Je te presente X / Enchante.",
            "Celebration formulas: Joyeux anniversaire, Felicitations, Bonne annee.",
            "On se voit bientot? - the soft way to make plans.",
            "Passe le bonjour a... - pass greetings along.",
        ],
        "requirements": [
            "20 sentences covering meeting people, invitations, and celebrations, each translated.",
            "Tu register and introduction script demonstrated.",
        ],
        "standards": [
            "Pragmatics follow Battye, Hintze, and Rowlett.",
            "Usage follows Fagyal, Kibbee, and Jenkins.",
        ],
        "citations": [
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
            "Fagyal Z, Kibbee D, Jenkins F. French: A Linguistic Introduction. Cambridge; 2006.",
        ],
        "sig_lens": (
            "The Signature read: friendship is the co-signed page - two "
            "seals pressed side by side, neither over the other. The "
            "Signature Language Method introduces the learner around until "
            "the page fills with fellow signers."
        ),
    },
    {
        "key": "technology",
        "name": "French Sentences: Technology and Communication",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences for the phone, the internet, the computer, and "
            "messaging: 1. Mon telephone est decharge. (My phone is dead.) 2. "
            "Ou est le chargeur? (Where is the charger?) 3. Le wifi ne marche "
            "pas. (The wifi does not work.) 4. Quel est le mot de passe? "
            "(What is the password?) 5. Je t'envoie un message. (I send you a "
            "message.) 6. Reponds a mon texto. (Answer my text.) 7. Je suis "
            "en ligne. (I am online.) 8. La connexion est lente. (The "
            "connection is slow.) 9. Mon ordinateur a plante. (My computer "
            "crashed.) 10. Redemarre l'appareil. (Restart the device.) 11. "
            "J'ai recu ton email. (I received your email.) 12. Envoie-moi la "
            "photo. (Send me the photo.) 13. On s'appelle ce soir? (Shall we "
            "call each other tonight?) 14. Je te rappelle dans cinq minutes. "
            "(I will call you back in five minutes.) 15. Le reseau est "
            "sature. (The network is congested.) 16. Telecharge l'application. "
            "(Download the app.) 17. Mets a jour le logiciel. (Update the "
            "software.) 18. La batterie est faible. (The battery is low.) 19. "
            "Partage ta localisation. (Share your location.) 20. A plus tard "
            "en ligne! (See you later online!)"
        ),
        "how_it_works": (
            "Technology sentences work as the loanword frontier: le wifi, le "
            "smartphone, le bug, le cloud - English loans flood in, but the "
            "Academie counters with courriel (email), mot de passe, and "
            "telechargement. Quebec goes further, officializing clavardage "
            "(chat) and pourriel (spam). Texting runs on abbreviations: "
            "slt (salut), bjr (bonjour), mdr (mort de rire - lol), a+ (a "
            "plus). The verbs are regular and practical: envoyer, recevoir, "
            "telecharger, redemarrer, mettre a jour. Tech French is the "
            "fastest-changing corner of the language - and the most fun to "
            "watch."
        ),
        "key_points": [
            "Loanwords flood in: le wifi, le smartphone, le bug; Academie counters with courriel.",
            "Quebec officializes clavardage (chat) and pourriel (spam).",
            "Texting abbreviations: slt, bjr, mdr, a+.",
            "Regular tech verbs: envoyer, recevoir, telecharger, redemarrer.",
            "Allo? opens every phone call in French.",
        ],
        "requirements": [
            "20 sentences covering phone, internet, computer, and messaging, each translated.",
            "Loanword vs Academie terms and texting abbreviations noted.",
        ],
        "standards": [
            "Terminology follows the Academie francaise dictionary, 9th edition.",
            "Quebec usage follows the OIF 2022 report.",
        ],
        "citations": [
            "Academie francaise. Dictionnaire de l'Academie francaise, 9e edition. In progress.",
            "Organisation internationale de la Francophonie. La langue francaise dans le monde 2022. Gallimard; 2022.",
        ],
        "sig_lens": (
            "The Signature read: the network is the new paper - the seal "
            "now travels at light speed, but the hand that presses it is "
            "still human. The Signature Language Method signs every message "
            "as if it were wax, because the medium never excuses a sloppy "
            "seal."
        ),
    },
    {
        "key": "tenses",
        "name": "French Verb Tenses in Sentences",
        "group": "Compounded",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "The French tense system in sentences, five or more per tense. "
            "Present (habits, current states): Je parle francais. (I speak "
            "French.) Tu habites a Paris. (You live in Paris.) Il pleut. (It "
            "rains.) Nous mangeons ensemble. (We eat together.) Vous "
            "comprenez vite. (You understand quickly.) Ils jouent au foot. "
            "(They play soccer.) Passe compose (completed past, with avoir "
            "or etre): J'ai mange une pomme. (I ate an apple.) Tu as fini? "
            "(Did you finish?) Il est alle a l'ecole. (He went to school.) "
            "Elle est nee en 1990. (She was born in 1990.) Nous avons vu un "
            "film. (We saw a film.) Vous etes partis tot. (You left early.) "
            "Imparfait (ongoing past, habits, background): Je jouais dehors. "
            "(I used to play outside.) Tu etais fatigue. (You were tired.) "
            "Il faisait beau. (The weather was nice.) Nous habitions a "
            "Lyon. (We lived in Lyon.) Vous lisiez beaucoup. (You read a "
            "lot.) Futur proche (near future, aller + infinitive): Je vais "
            "partir. (I am going to leave.) Tu vas reussir. (You are going "
            "to succeed.) Il va pleuvoir. (It is going to rain.) Nous allons "
            "manger. (We are going to eat.) Vous allez aimer. (You are going "
            "to like it.) Futur simple (later future, will): Je partirai "
            "demain. (I will leave tomorrow.) Tu reussiras. (You will "
            "succeed.) Il pleuvra. (It will rain.) Nous mangerons a huit "
            "heures. (We will eat at eight.) Vous aimerez ce film. (You will "
            "like this film.) Conditionnel (would, polite requests, "
            "hypotheses): Je voudrais un cafe. (I would like a coffee.) Tu "
            "pourrais m'aider? (Could you help me?) Il viendrait demain. (He "
            "would come tomorrow.) Nous aimerions voyager. (We would like to "
            "travel.) Si j'avais le temps, je viendrais. (If I had time, I "
            "would come.) Subjonctif (after doubt, emotion, necessity): Il "
            "faut que tu viennes. (You must come.) Je veux qu'il parte. (I "
            "want him to leave.) Bien qu'il soit tard... (Although it is "
            "late...) J'ai peur qu'elle soit malade. (I am afraid she is "
            "sick.) Il est possible qu'ils viennent. (They may come.) Plus-"
            "que-parfait (past before past): J'avais deja mange. (I had "
            "already eaten.) Tu etais parti. (You had left.) Imperatif "
            "(commands): Parle! (Speak!) Parlons! (Let us speak!) Parlez! "
            "(Speak! formal/plural.)"
        ),
        "how_it_works": (
            "French tenses work as a time machine with two engines: simple "
            "tenses (one word: je parlerai) and compound tenses (auxiliary + "
            "participle: j'ai parle). The auxiliary is avoir for most verbs "
            "and etre for 17 movement/state verbs remembered by the house of "
            "etre (aller, venir, arriver, partir, entrer, sortir, monter, "
            "descendre, naitre, mourir, rester, tomber, retourner, passer, "
            "devenir, revenir) plus all reflexives - and with etre the "
            "participle agrees (Elle est allee). The great past-tense "
            "choice is passe compose (what happened) versus imparfait (what "
            "was happening): Il a plu quand je sortais (It rained when I was "
            "going out). The subjunctive is triggered, not chosen - learn "
            "the triggers (il faut que, je veux que, bien que, avoir peur "
            "que) and the mood follows."
        ),
        "key_points": [
            "Simple vs compound tenses: je parlerai vs j'ai parle.",
            "Avoir for most verbs; etre for the 17 house-of-etre verbs and all reflexives, with participle agreement.",
            "Passe compose = what happened; imparfait = what was happening.",
            "Futur proche (aller + infinitive) for near future; futur simple for later future.",
            "Subjonctif is triggered by set phrases: il faut que, je veux que, bien que.",
        ],
        "requirements": [
            "Present, passe compose, imparfait, futur proche, futur simple, conditionnel, subjonctif, plus-que-parfait, imperatif - 5+ translated sentences each.",
            "Avoir/etre auxiliary rule and house of etre stated.",
            "Passe compose vs imparfait distinction with example.",
        ],
        "standards": [
            "Tense system follows Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Tables follow Price, A Comprehensive French Grammar 7th ed.",
        ],
        "citations": [
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Price G. A Comprehensive French Grammar. 7th ed. Wiley-Blackwell; 2007.",
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
        ],
        "sig_lens": (
            "The Signature read: tenses are the time-dies of the press - "
            "past, present, and future struck from the same verb-blank. "
            "The Signature Language Method machines the auxiliary pair "
            "first, because every compound strike needs its hammer."
        ),
    },
    {
        "key": "qa",
        "name": "French Questions and Answers",
        "group": "Compounded",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Twenty question-and-answer pairs covering who, what, where, "
            "when, why, and how: 1. Qui est-ce? - C'est mon frere. (Who is "
            "it? - It is my brother.) 2. Qu'est-ce que c'est? - C'est un "
            "cadeau. (What is it? - It is a gift.) 3. Ou habites-tu? - "
            "J'habite a Marseille. (Where do you live? - I live in "
            "Marseille.) 4. Quand pars-tu? - Je pars demain. (When do you "
            "leave? - I leave tomorrow.) 5. Pourquoi pleures-tu? - Parce que "
            "je suis triste. (Why are you crying? - Because I am sad.) 6. "
            "Comment vas-tu? - Tres bien, merci. (How are you? - Very well, "
            "thanks.) 7. Combien coute ce livre? - Dix euros. (How much is "
            "this book? - Ten euros.) 8. Quelle est ta couleur preferee? - "
            "Le bleu. (What is your favorite color? - Blue.) 9. Quel age as-"
            "tu? - J'ai vingt ans. (How old are you? - I am twenty.) 10. "
            "Parles-tu anglais? - Oui, un peu. (Do you speak English? - "
            "Yes, a little.) 11. Est-ce que tu viens? - Oui, j'arrive. (Are "
            "you coming? - Yes, I am coming.) 12. As-tu des freres? - Oui, "
            "un frere et une soeur. (Do you have siblings? - Yes, a brother "
            "and a sister.) 13. Ou sont les toilettes? - Au fond du couloir. "
            "(Where is the restroom? - At the end of the hall.) 14. Quelle "
            "heure est-il? - Il est trois heures. (What time is it? - It is "
            "three o'clock.) 15. Tu as faim? - Oui, tres faim. (Are you "
            "hungry? - Yes, very hungry.) 16. Qu'est-ce que tu fais ce "
            "week-end? - Je visite ma famille. (What are you doing this "
            "weekend? - I visit my family.) 17. Pourquoi pas? - Pourquoi "
            "pas! (Why not? - Why not!) 18. C'est loin? - Non, a cinq "
            "minutes. (Is it far? - No, five minutes.) 19. Tu comprends? - "
            "Oui, parfaitement. (Do you understand? - Yes, perfectly.) 20. "
            "On y va? - Allons-y! (Shall we go? - Let us go!)"
        ),
        "how_it_works": (
            "French questions work in three gears of formality. Gear one is "
            "intonation - say the statement with rising pitch: Tu viens? "
            "Gear two is est-ce que, the universal question maker: Est-ce "
            "que tu viens? Gear three is inversion, the formal written "
            "gear: Viens-tu? The question words stay simple: qui (who), que "
            "(what - Qu'est-ce que tu fais?), ou (where), quand (when), "
            "pourquoi (why - always answered by parce que), comment (how), "
            "combien (how much/many), quel (which). Answers recycle the "
            "question's verb: - Tu viens? - Oui, je viens. Short answers "
            "with si contradict a negative question: - Tu ne viens pas? - "
            "Si, je viens! (Yes I am!)"
        ),
        "key_points": [
            "Three question gears: intonation, est-ce que, inversion - rising formality.",
            "Question words: qui, que, ou, quand, pourquoi, comment, combien, quel.",
            "Pourquoi is answered by parce que.",
            "Si contradicts a negative question: - Tu ne viens pas? - Si!",
            "Answers recycle the question's verb.",
        ],
        "requirements": [
            "20 question/answer pairs covering who/what/where/when/why/how, each translated.",
            "Three question formations and the si rule demonstrated.",
        ],
        "standards": [
            "Question formation follows Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Usage follows Battye, Hintze, and Rowlett.",
        ],
        "citations": [
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
        ],
        "sig_lens": (
            "The Signature read: a question is the blank side of the seal - "
            "the press asks, the answer strikes. The Signature Language "
            "Method teaches all three gears, because a sealer asks politely "
            "upward and plainly among equals."
        ),
    },
    {
        "key": "commands",
        "name": "French Commands and Requests",
        "group": "Compounded",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Twenty imperatives and polite requests, informal versus "
            "formal: 1. Viens ici! (Come here! - tu) 2. Venez par ici, s'il "
            "vous plait. (Come this way, please. - vous) 3. Assieds-toi. "
            "(Sit down. - tu) 4. Asseyez-vous. (Sit down. - vous) 5. Parle "
            "plus fort. (Speak louder. - tu) 6. Parlez plus lentement, s'il "
            "vous plait. (Speak more slowly, please. - vous) 7. Mange ta "
            "soupe. (Eat your soup. - tu) 8. Prenez votre temps. (Take your "
            "time. - vous) 9. Ne t'inquiete pas. (Do not worry. - tu) 10. "
            "Ne vous inquietez pas. (Do not worry. - vous) 11. Fais attention! "
            "(Be careful! - tu) 12. Faites attention en traversant. (Be "
            "careful crossing. - vous) 13. Donne-moi ton numero. (Give me "
            "your number. - tu) 14. Pourriez-vous m'aider? (Could you help "
            "me? - formal request) 15. Voudriez-vous un cafe? (Would you "
            "like a coffee? - formal offer) 16. Aide-moi, s'il te plait. "
            "(Help me, please. - tu) 17. Excuse-moi une minute. (Excuse me a "
            "minute. - tu) 18. Ecoute-moi bien. (Listen to me carefully. - "
            "tu) 19. Allons-y! (Let us go! - nous) 20. Restons calmes. (Let "
            "us stay calm. - nous) The imperative has three forms: tu "
            "(Parle!), nous (Parlons!), vous (Parlez!). First-group verbs "
            "drop the -s in the tu form: Parle! not *Parles! Object pronouns "
            "attach with hyphens after affirmative commands (Donne-moi, "
            "Assieds-toi) but go before the verb in negatives (Ne t'assieds "
            "pas). Requests soften with the conditional: Pourriez-vous, "
            "Voudriez-vous, Auriez-vous l'amabilite de..."
        ),
        "how_it_works": (
            "French commands work as the verb stripped of its subject: the "
            "pronoun disappears and the ending does the talking. Politeness "
            "is a dial, not a switch: bare imperative for family and "
            "urgency (Viens!), imperative + s'il vous plait for neutral "
            "politeness (Venez, s'il vous plait), conditional for formal "
            "requests (Pourriez-vous m'aider?). The nous form (Allons-y!) "
            "is the let's of French, proposing joint action. Reflexive "
            "commands keep the pronoun but move it after: Assieds-toi, "
            "Levez-vous. Master the three forms and the politeness dial, "
            "and you can direct, invite, and request in any setting."
        ),
        "key_points": [
            "Three imperative forms: tu (Parle!), nous (Parlons!), vous (Parlez!).",
            "First-group verbs drop -s in tu form: Parle!",
            "Pronouns attach after affirmative commands (Donne-moi), before in negatives (Ne me donne pas).",
            "Politeness dial: bare imperative < + s'il vous plait < conditional (Pourriez-vous).",
            "Nous form = let's: Allons-y!",
        ],
        "requirements": [
            "20 imperative/polite-request sentences, formal vs informal, each translated.",
            "The -s drop rule and pronoun placement rules stated.",
            "Politeness dial explained.",
        ],
        "standards": [
            "Imperative formation follows Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Pragmatics follow Battye, Hintze, and Rowlett.",
        ],
        "citations": [
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Price G. A Comprehensive French Grammar. 7th ed. Wiley-Blackwell; 2007.",
        ],
        "sig_lens": (
            "The Signature read: the command is the press-handle - one firm "
            "pull and the die strikes. The Signature Language Method teaches "
            "the handle's three grips and the politeness dial, because a "
            "sealer commands the press but requests of people."
        ),
    },
    {
        "key": "descriptions",
        "name": "French Descriptions of People and Places",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences describing people, places, and things in "
            "detail: 1. Marie a les cheveux longs et bruns. (Marie has long "
            "brown hair.) 2. Paul est grand avec des yeux bleus. (Paul is "
            "tall with blue eyes.) 3. Ma grand-mere a quatre-vingts ans et "
            "le sourire facile. (My grandmother is eighty and smiles "
            "easily.) 4. Le bebe a de petites mains douces. (The baby has "
            "tiny soft hands.) 5. C'est un homme d'une cinquantaine "
            "d'annees, barbu. (He is a man in his fifties, bearded.) 6. Elle "
            "porte une robe rouge elegante. (She wears an elegant red dress.) "
            "7. Paris est une ville magnifique au bord de la Seine. (Paris "
            "is a magnificent city on the Seine.) 8. La tour Eiffel mesure "
            "trois cent trente metres. (The Eiffel Tower is 330 meters "
            "tall.) 9. Le vieux quartier a des rues etroites et pavees. "
            "(The old quarter has narrow cobbled streets.) 10. La plage de "
            "sable fin s'etend sur deux kilometres. (The fine-sand beach "
            "stretches two kilometers.) 11. C'est un petit village calme "
            "entoure de vignes. (It is a small quiet village surrounded by "
            "vineyards.) 12. La maison en pierre a un toit d'ardoise. (The "
            "stone house has a slate roof.) 13. Le jardin est plein de "
            "fleurs colorees. (The garden is full of colorful flowers.) 14. "
            "Le fromage a une odeur forte mais un gout doux. (The cheese has "
            "a strong smell but a mild taste.) 15. Ce vin rouge a des aromes "
            "de fruits noirs. (This red wine has black-fruit aromas.) 16. La "
            "musique douce remplit la salle. (Soft music fills the hall.) 17. "
            "C'est une journee ensoleillee et fraiche. (It is a sunny, cool "
            "day.) 18. Le ciel d'un bleu profond annonce l'orage. (The deep-"
            "blue sky announces the storm.) 19. Son rire joyeux eclaire la "
            "piece. (Her joyful laugh lights up the room.) 20. Voila un "
            "endroit parfait pour pique-niquer. (Here is a perfect spot for "
            "a picnic.)"
        ),
        "how_it_works": (
            "Descriptions work as adjective stacking in the right slots: "
            "opinion and BANGS adjectives before the noun (une magnifique "
            "ville, un petit village), color, shape, and origin after "
            "(une robe rouge elegante, des rues etroites et pavees). "
            "Measurements use avoir + number (La tour mesure 330 metres; "
            "Marie a 80 ans becomes Elle a quatre-vingts ans). The present "
            "participle paints ongoing states (entoure de vignes, annonce "
            "l'orage). Sensory verbs - sentir, avoir l'air, sembler - carry "
            "the impressions: une odeur forte, un gout doux, des aromes de "
            "fruits noirs. Rich description is where agreement practice "
            "pays off visibly: every adjective must match, and the matches "
            "are the beauty of the sentence."
        ),
        "key_points": [
            "Adjective stacking: opinion/BANGS before, color/shape/origin after.",
            "Measurements with avoir/mesurer: 330 metres, 80 ans.",
            "Present participles paint states: entoure de, annonce.",
            "Sensory vocabulary: odeur, gout, aromes, eclaire.",
            "Every adjective must agree - description is agreement practice made visible.",
        ],
        "requirements": [
            "20 sentences describing people, places, and things in detail, each translated.",
            "Adjective slot order and measurement constructions demonstrated.",
        ],
        "standards": [
            "Description patterns follow Price 7th ed.",
            "Vocabulary follows the Academie francaise dictionary.",
        ],
        "citations": [
            "Price G. A Comprehensive French Grammar. 7th ed. Wiley-Blackwell; 2007.",
            "Academie francaise. Dictionnaire de l'Academie francaise, 9e edition. In progress.",
        ],
        "sig_lens": (
            "The Signature read: description is the engraving on the seal - "
            "fine lines cut after the blank is cast, and every line must be "
            "true. The Signature Language Method engraves slowly, because "
            "the engraving is what the eye remembers."
        ),
    },
    {
        "key": "story1",
        "name": "French Story I: A Simple Day",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence simple story in French, present tense, with "
            "line-by-line English translation. 1. Je m'appelle Lucas et "
            "j'habite a Bordeaux. (My name is Lucas and I live in "
            "Bordeaux.) 2. Chaque matin, je me leve a sept heures. (Every "
            "morning, I get up at seven.) 3. Je prends une douche et je "
            "m'habille vite. (I take a shower and get dressed quickly.) 4. "
            "Je mange du pain avec de la confiture. (I eat bread with jam.) "
            "5. Je bois un grand cafe au lait. (I drink a large cafe au "
            "lait.) 6. Je vais au travail en velo. (I go to work by bike.) "
            "7. Mon bureau est pres de la riviere. (My office is near the "
            "river.) 8. A midi, je dejeune avec mes collegues. (At noon, I "
            "have lunch with my colleagues.) 9. Le soir, je lis ou je "
            "regarde un film. (In the evening, I read or watch a film.) 10. "
            "Je me couche a onze heures. (I go to bed at eleven.) The story "
            "uses only present tense and first-group verbs plus the "
            "reflexives se lever, s'habiller, se coucher - the complete "
            "daily routine in ten lines, ready to personalize by swapping "
            "the city, the times, and the habits."
        ),
        "how_it_works": (
            "Simple stories work as the learner's first narrative machine: "
            "present tense, chronological order, one verb per line, and the "
            "reflexive routine verbs (se lever, se laver, s'habiller, se "
            "coucher) carrying the day from morning to night. Time markers "
            "open each line - Chaque matin, A midi, Le soir - training the "
            "fronted-adverb habit. The story is a template, not a text: swap "
            "Bordeaux for your city, sept heures for your hour, velo for "
            "your transport, and it becomes your day in French. Retell it "
            "about a friend (Il s'appelle... Il se leve...) and the third "
            "person arrives for free."
        ),
        "key_points": [
            "Present tense only; one verb per line; chronological order.",
            "Reflexive routine verbs carry the day: se lever, s'habiller, se coucher.",
            "Time markers front each line: Chaque matin, A midi, Le soir.",
            "The story is a template: swap city, times, habits to personalize.",
            "Retell in third person for free il/elle practice.",
        ],
        "requirements": [
            "10-sentence simple story in French with line-by-line English translation.",
            "Present tense throughout; daily-routine vocabulary.",
        ],
        "standards": [
            "Narrative patterns follow Battye, Hintze, and Rowlett.",
            "Grammar follows Price 7th ed.",
        ],
        "citations": [
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
            "Price G. A Comprehensive French Grammar. 7th ed. Wiley-Blackwell; 2007.",
        ],
        "sig_lens": (
            "The Signature read: the simple story is the first full sheet "
            "off the press - ten clean strikes in a row, morning to night. "
            "The Signature Language Method runs the sheet daily until the "
            "press runs itself."
        ),
    },
    {
        "key": "story2",
        "name": "French Story II: A Past Adventure",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the past, with line-by-line English "
            "translation, mixing passe compose and imparfait. 1. L'ete "
            "dernier, nous sommes alles en Bretagne. (Last summer, we went "
            "to Brittany.) 2. Il faisait beau quand nous sommes arrives. "
            "(The weather was nice when we arrived.) 3. Nous avons loue une "
            "petite maison pres de la mer. (We rented a small house near the "
            "sea.) 4. Chaque jour, nous marchions sur la plage. (Every day, "
            "we walked on the beach.) 5. Un matin, nous avons vu des "
            "dauphins. (One morning, we saw dolphins.) 6. Les enfants "
            "jouaient dans les vagues. (The children played in the waves.) "
            "7. Nous avons mange des crepes au marche. (We ate crepes at the "
            "market.) 8. Le soir, le ciel etait rose et orange. (In the "
            "evening, the sky was pink and orange.) 9. Nous avons pris "
            "beaucoup de photos. (We took many photos.) 10. C'etait les "
            "meilleures vacances de notre vie. (It was the best vacation of "
            "our lives.) Notice the dance: imparfait paints the background "
            "(il faisait beau, nous marchions, le ciel etait), passe "
            "compose strikes the events (nous sommes arrives, nous avons "
            "vu, nous avons mange)."
        ),
        "how_it_works": (
            "Past stories work on the two-tense dance: the imparfait is the "
            "stage - weather, habits, ongoing scenes - and the passe "
            "compose is the actor walking across it. Learners narrate by "
            "alternating: set the scene in imparfait (Il faisait beau), "
            "strike the event in passe compose (nous avons vu des "
            "dauphins). Etre-verbs of movement (nous sommes alles) carry "
            "the journey, and the participle agrees with the subject "
            "(allees for an all-female nous). Time markers sort the tenses "
            "automatically: chaque jour and pendant que pull imparfait; un "
            "matin, soudain, and tout a coup pull passe compose. Tell any "
            "past event with this rhythm and it sounds native."
        ),
        "key_points": [
            "Imparfait = background/stage; passe compose = events/actors.",
            "Time markers sort tenses: chaque jour -> imparfait; soudain -> passe compose.",
            "Etre-verbs carry journeys, with participle agreement (nous sommes allees).",
            "C'etait closes a story; C'est opens the present.",
            "Any past event told in this rhythm sounds native.",
        ],
        "requirements": [
            "10-sentence story using past tenses with line-by-line English translation.",
            "Both passe compose and imparfait used and their roles explained.",
        ],
        "standards": [
            "Tense usage follows Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Narrative patterns follow Battye, Hintze, and Rowlett.",
        ],
        "citations": [
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
        ],
        "sig_lens": (
            "The Signature read: the past story is the archive copy - the "
            "imparfait the paper, the passe compose the ink. The Signature "
            "Language Method files every memory in both, because a record "
            "needs its paper and its ink."
        ),
    },
    {
        "key": "story3",
        "name": "French Story III: Plans for Tomorrow",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in the future and conditional, with "
            "line-by-line English translation. 1. L'annee prochaine, je "
            "demenagerai a Montreal. (Next year, I will move to Montreal.) "
            "2. Je trouverai un appartement pres du metro. (I will find an "
            "apartment near the metro.) 3. Je vais apprendre l'anglais "
            "canadien. (I am going to learn Canadian English.) 4. Nous "
            "visiterons le Vieux-Port en ete. (We will visit the Old Port in "
            "summer.) 5. Tu viendras me voir, j'espere. (You will come see "
            "me, I hope.) 6. S'il fait beau, nous ferons du velo. (If the "
            "weather is nice, we will bike.) 7. J'aimerais aussi voir "
            "Quebec en hiver. (I would also like to see Quebec City in "
            "winter.) 8. On mangera de la poutine ensemble. (We will eat "
            "poutine together.) 9. Ce sera une grande aventure. (It will be "
            "a great adventure.) 10. Je te raconterai tout a mon retour. (I "
            "will tell you everything when I return.) The futur simple "
            "carries the plan (je demenagerai), the futur proche carries "
            "the near intention (je vais apprendre), the conditional "
            "carries the wish (j'aimerais), and si + present carries the "
            "condition (S'il fait beau, nous ferons)."
        ),
        "how_it_works": (
            "Future stories work on the three-track system: futur proche "
            "(aller + infinitive) for what is already decided, futur simple "
            "for what is planned or predicted, conditional for what is "
            "wished or hypothetical. The si clause runs on present tense "
            "even for future meaning - S'il fait beau, nous ferons - never "
            "*Si il fera beau. Hopes ride on esperer + future (j'espere que "
            "tu viendras) while wishes ride on the conditional (j'aimerais). "
            "Plans told this way sound confident and French: near intentions "
            "in proche, firm plans in simple, dreams in conditional."
        ),
        "key_points": [
            "Futur proche = decided; futur simple = planned/predicted; conditional = wished/hypothetical.",
            "Si clauses use present tense for future meaning: S'il fait beau, nous ferons.",
            "J'espere que + future; J'aimerais + infinitive.",
            "Irregular future stems: ser-, aur-, ir-, fer-, pourr-, devr-.",
            "Plans in three tracks sound confident and French.",
        ],
        "requirements": [
            "10-sentence story using future/conditional forms with line-by-line English translation.",
            "All three future tracks and the si-clause rule demonstrated.",
        ],
        "standards": [
            "Future/conditional usage follows Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Tables follow Price 7th ed.",
        ],
        "citations": [
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Price G. A Comprehensive French Grammar. 7th ed. Wiley-Blackwell; 2007.",
        ],
        "sig_lens": (
            "The Signature read: the future story is the proof pulled "
            "before the run - the plan inked before the press rolls. The "
            "Signature Language Method proofs every plan in three tracks, "
            "because a sealer who cannot state tomorrow cannot stamp today."
        ),
    },
    {
        "key": "idioms",
        "name": "French Idioms and Proverbs",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Twenty idioms and proverbs, each with literal translation, "
            "real meaning, and an example sentence. 1. Avoir le cafard - "
            "lit. to have the cockroach - to feel blue. Depuis son depart, "
            "j'ai le cafard. (Since he left, I feel blue.) 2. Poser un lapin "
            "- lit. to put down a rabbit - to stand someone up. Elle m'a "
            "pose un lapin hier soir. (She stood me up last night.) 3. "
            "Donner sa langue au chat - lit. to give one's tongue to the "
            "cat - to give up guessing. Je donne ma langue au chat! (I give "
            "up!) 4. Avoir un poil dans la main - lit. to have a hair in "
            "the hand - to be lazy. Il a un poil dans la main, celui-la. "
            "(He is lazy, that one.) 5. Couter les yeux de la tete - lit. "
            "to cost the eyes of the head - to cost a fortune. Ce voyage "
            "coute les yeux de la tete. (This trip costs a fortune.) 6. Etre "
            "dans la lune - lit. to be in the moon - to be daydreaming. Tu "
            "es dans la lune aujourd'hui. (You are daydreaming today.) 7. "
            "Faire la grasse matinee - lit. to do the fat morning - to "
            "sleep in. Dimanche, je fais la grasse matinee. (On Sunday, I "
            "sleep in.) 8. Avoir la peche - lit. to have the peach - to "
            "feel great, full of energy. Depuis ce matin, j'ai la peche. "
            "(Since this morning, I feel great.) 9. Tomber dans les pommes "
            "- lit. to fall in the apples - to faint. Elle est tombee dans "
            "les pommes. (She fainted.) 10. Mettre son grain de sel - lit. "
            "to put in one's grain of salt - to put in one's two cents. Il "
            "met toujours son grain de sel. (He always puts in his two "
            "cents.) 11. Faire d'une pierre deux coups - lit. to make two "
            "hits with one stone - to kill two birds with one stone. En "
            "allant au marche, je fais d'une pierre deux coups. (Going to "
            "the market, I kill two birds with one stone.) 12. Avoir "
            "d'autres chats a fouetter - lit. to have other cats to whip - "
            "to have other fish to fry. Desole, j'ai d'autres chats a "
            "fouetter. (Sorry, I have other fish to fry.) 13. Etre sur son "
            "trente-et-un - lit. to be on one's thirty-one - to be dressed "
            "to the nines. Pour le mariage, il etait sur son trente-et-un. "
            "(For the wedding, he was dressed to the nines.) 14. Raconter "
            "des salades - lit. to tell salads - to tell tall tales. Arrete "
            "de raconter des salades! (Stop telling tall tales!) 15. Avoir "
            "le coeur sur la main - lit. to have the heart on the hand - "
            "to be generous, warm-hearted. Elle a le coeur sur la main. "
            "(She is warm-hearted.) 16. Il pleut des cordes - lit. it rains "
            "ropes - it is pouring. Prends un parapluie, il pleut des "
            "cordes. (Take an umbrella, it is pouring.) 17. Un froid de "
            "canard - lit. a duck cold - bitter cold. Il fait un froid de "
            "canard ce matin. (It is bitterly cold this morning.) 18. Casser "
            "les pieds - lit. to break the feet - to annoy someone. Tu me "
            "casses les pieds! (You annoy me!) 19. Prendre ses jambes a son "
            "cou - lit. to take one's legs to one's neck - to run away "
            "fast. En voyant le chien, il a pris ses jambes a son cou. "
            "(Seeing the dog, he ran away fast.) 20. Petit a petit, l'oiseau "
            "fait son nid - lit. little by little, the bird builds its nest "
            " - proverb: slow and steady wins. Petit a petit, l'oiseau fait "
            "son nid: continue tes efforts. (Little by little: keep up your "
            "efforts.)"
        ),
        "how_it_works": (
            "Idioms work as the cultural encryption of French: the literal "
            "words mislead and only the shared meaning unlocks the "
            "sentence. Learn them in literal-meaning-example triples and "
            "the triple becomes one memorized chunk - never translate them "
            "word by word in conversation. Many carry body parts (les yeux "
            "de la tete, le coeur sur la main, casser les pieds) or animals "
            "(le cafard, le lapin, le chat, les chats, le canard), which "
            "gives the memory a hook. Proverbs (Petit a petit...) deliver "
            "the folk wisdom in ready-made rhythm. Drop one correct idiom "
            "into conversation and native speakers instantly upgrade their "
            "estimate of your French."
        ),
        "key_points": [
            "Learn idioms as literal-meaning-example triples, never word-by-word translations.",
            "Body-part and animal images give memory hooks: cafard, lapin, chat, canard.",
            "Avoir and etre carry most idioms: avoir le cafard, etre dans la lune.",
            "Proverbs deliver folk wisdom in rhythm: Petit a petit, l'oiseau fait son nid.",
            "One correct idiom upgrades a native speaker's estimate of your French.",
        ],
        "requirements": [
            "20 idioms/proverbs, each with literal translation, real meaning, and an example sentence.",
            "Triple format (literal/meaning/example) consistent throughout.",
        ],
        "standards": [
            "Idioms follow the Academie francaise dictionary, 9th edition.",
            "Selection follows Battye, Hintze, and Rowlett on idiomatic French.",
        ],
        "citations": [
            "Academie francaise. Dictionnaire de l'Academie francaise, 9e edition. In progress.",
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
        ],
        "sig_lens": (
            "The Signature read: idioms are the secret marks cut into the "
            "seal - invisible to outsiders, instant recognition among "
            "sealers. The Signature Language Method cuts one secret mark a "
            "day until the learner's seal carries the guild signs."
        ),
    },
    {
        "key": "registers",
        "name": "French Formal and Polite Registers",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen formal versus informal pairs for letters, business, "
            "and elders, each with translation. 1. Formal: Pourriez-vous "
            "m'indiquer le chemin? (Could you show me the way?) / Informal: "
            "Tu peux me montrer le chemin? (Can you show me the way?) 2. "
            "Formal: Je vous prie de m'excuser. (I beg your pardon.) / "
            "Informal: Excuse-moi. (Sorry.) 3. Formal: Voudriez-vous vous "
            "asseoir? (Would you like to sit?) / Informal: Assieds-toi. (Sit "
            "down.) 4. Formal: Auriez-vous l'amabilite de fermer la porte? "
            "(Would you be so kind as to close the door?) / Informal: Tu "
            "peux fermer la porte? (Can you close the door?) 5. Formal: Je "
            "vous remercie de votre aide. (I thank you for your help.) / "
            "Informal: Merci pour ton aide. (Thanks for your help.) 6. "
            "Formal: Veuillez agreer, Madame, l'expression de mes sentiments "
            "distingues. (Yours respectfully - letter closing.) / Informal: "
            "Bisous! (Kisses! - letter closing to friends.) 7. Formal: Cher "
            "Monsieur le Directeur, (Dear Director,) / Informal: Salut Marc, "
            "(Hi Marc,) 8. Formal: Je me permets de vous contacter au sujet "
            "de... (I take the liberty of contacting you about...) / "
            "Informal: Je t'ecris pour... (I am writing about...) 9. Formal: "
            "Dans l'attente de votre reponse... (Awaiting your reply...) / "
            "Informal: Reponds-moi vite! (Answer me quick!) 10. Formal: "
            "N'hesitez pas a me contacter. (Do not hesitate to contact me.) "
            "/ Informal: Appelle-moi si tu veux. (Call me if you want.) 11. "
            "Formal: Je vous souhaite une excellente journee. (I wish you an "
            "excellent day.) / Informal: Bonne journee! (Have a good day!) "
            "12. Formal: Excusez-moi de vous deranger. (Sorry to disturb "
            "you.) / Informal: Desole de te deranger. (Sorry to bother "
            "you.) 13. Formal: Serait-il possible de reporter notre rendez-"
            "vous? (Would it be possible to postpone our meeting?) / "
            "Informal: On peut remettre ca a demain? (Can we push this to "
            "tomorrow?) 14. Formal: Je vous prie d'agreer mes salutations "
            "les meilleures. (Best regards.) / Informal: A plus! (See you!) "
            "15. Formal: Madame, Monsieur, bonjour. (Hello - formal "
            "address.) / Informal: Salut tout le monde! (Hi everyone!) The "
            "formal register runs on vous, the conditional (pourriez, "
            "voudriez, auriez), and ritual formulas; the informal runs on "
            "tu, the present, and short forms. Letters open with Cher/Chere "
            "+ title and close with the veuillez agreer formula - never "
            "translate English closings word for word."
        ),
        "how_it_works": (
            "Registers work as the two floors of French: the formal floor "
            "(vous, conditional, ritual formulas) for strangers, elders, "
            "business, and writing; the informal floor (tu, present, short "
            "forms) for friends, family, and children. The conditional is "
            "the politeness engine - Pourriez-vous, Voudriez-vous, "
            "Serait-il possible - softening every request one degree. "
            "Business letters are the most ritualized: the opening names "
            "the title (Cher Monsieur le Directeur), the closing performs "
            "the veuillez agreer bow, and between them the sentences stay "
            "short and conditional. Climb to the formal floor by default "
            "with anyone older or unknown; descend to tu only when invited "
            "- or when they start it first."
        ),
        "key_points": [
            "Two floors: formal (vous, conditional, ritual) vs informal (tu, present, short).",
            "The conditional is the politeness engine: Pourriez-vous, Voudriez-vous.",
            "Letter ritual: Cher + title opening; veuillez agreer closing.",
            "Default to vous with elders and strangers; switch to tu when invited.",
            "Never translate English letter closings word for word.",
        ],
        "requirements": [
            "15 formal vs informal pairs (letters, business, elders), each with translations.",
            "The veuillez agreer closing formula given in full.",
            "Tu/vous switching rule stated.",
        ],
        "standards": [
            "Epistolary formulas follow Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Pragmatics follow Battye, Hintze, and Rowlett.",
        ],
        "citations": [
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
        ],
        "sig_lens": (
            "The Signature read: register is the pressure setting of the "
            "press - full pressure for the formal floor, light touch for "
            "friends. The Signature Language Method calibrates the dial "
            "daily, because the wrong pressure ruins the impression."
        ),
    },
    {
        "key": "complex",
        "name": "French Compound and Complex Sentences",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen long sentences with clauses, connectors, and relative "
            "clauses - each parsed and translated. 1. L'homme qui parle au "
            "telephone est mon voisin. [qui = who; relative clause as "
            "subject] (The man who is on the phone is my neighbor.) 2. Le "
            "livre que tu m'as prete est passionnant. [que = that/which; "
            "relative clause as object] (The book you lent me is "
            "fascinating.) 3. La maison dont je reve est au bord de la mer. "
            "[dont = of which; replaces de + noun] (The house I dream of is "
            "by the sea.) 4. C'est la ville ou je suis ne. [ou = where; "
            "relative of place] (This is the city where I was born.) 5. Je "
            "reste a la maison parce qu'il pleut. [parce que = because; "
            "cause] (I stay home because it rains.) 6. Bien qu'il soit "
            "tard, nous continuons. [bien que + subjunctive = although; "
            "concession] (Although it is late, we continue.) 7. Puisqu'il "
            "fait beau, sortons! [puisque = since, given that; known cause] "
            "(Since the weather is nice, let us go out!) 8. Il est parti "
            "sans dire au revoir. [sans + infinitive = without; manner] (He "
            "left without saying goodbye.) 9. Elle travaille pour payer ses "
            "etudes. [pour + infinitive = in order to; purpose] (She works "
            "to pay for her studies.) 10. Si tu viens, je serai content. "
            "[si + present -> future; condition] (If you come, I will be "
            "happy.) 11. Quand il est arrive, nous dinions. [quand + passe "
            "compose vs imparfait; background event] (When he arrived, we "
            "were dining.) 12. Je pense qu'il a raison, mais je n'en suis "
            "pas sur. [que-clause + mais; opinion with reservation] (I "
            "think he is right, but I am not sure.) 13. Non seulement il "
            "parle francais, mais il ecrit aussi des poemes. [non seulement"
            "... mais; paired connectors] (Not only does he speak French, "
            "he also writes poems.) 14. Cependant, les resultats restent "
            "incertains. [cependant = however; formal contrast] (However, "
            "the results remain uncertain.) 15. En outre, nous devons "
            "prevenir les invites. [en outre = furthermore; addition] "
            "(Furthermore, we must notify the guests.) Master qui/que/dont/"
            "ou and the big connectors (parce que, bien que, puisque, si, "
            "quand, cependant, en outre, donc, alors, neanmoins), and any "
            "French sentence comes apart cleanly."
        ),
        "how_it_works": (
            "Complex sentences work as clause trains: the main clause is "
            "the engine, relative clauses (qui, que, dont, ou, ce qui, ce "
            "que) are the passenger cars, and connectors are the couplings. "
            "Dont is the workhorse students fear most - it replaces de + "
            "noun (parler de -> dont je parle; rever de -> dont je reve; "
            "avoir besoin de -> dont j'ai besoin). Bien que, quoique, and "
            "pour que demand the subjunctive; parce que, puisque, and quand "
            "take the indicative. Punctuation rule: a comma separates the "
            "subordinate clause when it comes first (Bien qu'il soit tard, "
            "nous continuons), but not always when it follows. Parse any "
            "sentence by finding the verbs first - each verb heads a clause "
            "- then attaching each clause to its connector."
        ),
        "key_points": [
            "Relative pronouns: qui (subject), que (object), dont (de + noun), ou (place).",
            "Dont replaces de + noun: dont je reve, dont j'ai besoin.",
            "Bien que / pour que -> subjunctive; parce que / puisque -> indicative.",
            "Connectors: parce que, bien que, puisque, si, quand, cependant, en outre, donc, neanmoins.",
            "Parse by verbs: each verb heads a clause; connectors are the couplings.",
        ],
        "requirements": [
            "15 long sentences with clauses, connectors, relative clauses - each parsed and translated.",
            "Dont rule and subjunctive-trigger connectors stated.",
        ],
        "standards": [
            "Clause analysis follows Grevisse and Goosse, Le Bon Usage 16th ed.",
            "Connector inventory follows Price 7th ed.",
        ],
        "citations": [
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Price G. A Comprehensive French Grammar. 7th ed. Wiley-Blackwell; 2007.",
        ],
        "sig_lens": (
            "The Signature read: the complex sentence is the multi-die "
            "strike - several seals pressed in one pull, each clause a die, "
            "each connector a coupling. The Signature Language Method "
            "assembles the train car by car until the whole consist rolls."
        ),
    },
    {
        "key": "dialogue-market",
        "name": "French Conversation: At the Market",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue at an open-air market, "
            "annotated. 1. Cliente: Bonjour Monsieur! [greeting - mandatory "
            "in shops] (Hello!) 2. Marchand: Bonjour Madame, qu'est-ce qu'il "
            "vous faut aujourd'hui? [polite service question] (Hello, what "
            "do you need today?) 3. Cliente: Je voudrais un kilo de pommes, "
            "s'il vous plait. [conditional of politeness + quantity de] (I "
            "would like a kilo of apples, please.) 4. Marchand: Voila. Et "
            "avec ceci? [upsell formula] (Here you go. Anything else?) 5. "
            "Cliente: Ces tomates sont a combien? [price question] (How "
            "much are these tomatoes?) 6. Marchand: Trois euros le kilo. "
            "[price per unit] (Three euros a kilo.) 7. Cliente: C'est un peu "
            "cher. Vous pouvez faire un prix? [bargaining] (That is a bit "
            "expensive. Can you do a price?) 8. Marchand: Pour vous, deux "
            "cinquante. [concession] (For you, two fifty.) 9. Cliente: "
            "D'accord, mettez-m'en un kilo. [agreement + en for of-them] "
            "(Agreed, give me a kilo of them.) 10. Marchand: Voila. Autre "
            "chose? [checking] (Here. Anything else?) 11. Cliente: Oui, une "
            "baguette bien cuite. [preference stated] (Yes, a well-baked "
            "baguette.) 12. Marchand: La voila, encore chaude. [presenting] "
            "(Here it is, still warm.) 13. Cliente: Ca fait combien en tout? "
            "[total] (How much altogether?) 14. Marchand: Ca fait huit euros "
            "vingt. [total stated] (That is eight twenty.) 15. Cliente: Voila "
            "dix euros. [paying] (Here are ten euros.) 16. Marchand: Et "
            "voila un euro quatre-vingts de monnaie. [change with 80s "
            "number] (And here is one eighty change.) 17. Cliente: Merci "
            "beaucoup! [thanks] (Thank you very much!) 18. Marchand: Merci a "
            "vous, bonne journee! [reciprocal thanks + parting wish] (Thank "
            "you, have a good day!) 19. Cliente: Bonne journee! [parting] "
            "(Have a good day!) 20. Marchand: A la semaine prochaine! "
            "[regular-customer close] (See you next week!) The dialogue "
            "drills the market script end to end: greeting, polite request, "
            "price check, bargaining, agreement, total, payment, change, "
            "thanks, parting."
        ),
        "how_it_works": (
            "Market dialogues work as ritual scripts: the roles are fixed "
            "(cliente/marchand), the moves are ordered (greet -> request -> "
            "price -> bargain -> agree -> pay -> thank -> part), and the "
            "formulas slot in. Numbers do the heavy lifting at the till: "
            "huit euros vingt, un euro quatre-vingts - change-making is "
            "mental arithmetic in French. En replaces the repeated noun "
            "(mettez-m'en = give me of-them), and voila presents everything. "
            "Rehearse the script with a partner, swapping the products and "
            "prices, until the moves run without thinking - then the real "
            "market is just a change of cast."
        ),
        "key_points": [
            "Market script order: greet -> request -> price -> bargain -> agree -> pay -> thank -> part.",
            "Bargaining pair: C'est un peu cher / Pour vous, deux cinquante.",
            "En replaces repeated nouns: mettez-m'en un kilo.",
            "Change-making drills 70/80/90 numbers: un euro quatre-vingts.",
            "Rehearse swapping products and prices until automatic.",
        ],
        "requirements": [
            "20-line bilingual dialogue (French + English), annotated with bracket notes.",
            "Full market script from greeting to parting.",
        ],
        "standards": [
            "Dialogue pragmatics follow Battye, Hintze, and Rowlett.",
            "Formulas follow the Academie francaise dictionary.",
        ],
        "citations": [
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
            "Academie francaise. Dictionnaire de l'Academie francaise, 9e edition. In progress.",
        ],
        "sig_lens": (
            "The Signature read: the market dialogue is the rehearsal "
            "strike - the full run practiced on scrap before the real "
            "sheet. The Signature Language Method rehearses every script "
            "until the hand strikes true on the real paper."
        ),
    },
    {
        "key": "dialogue-friend",
        "name": "French Conversation: Meeting a Friend",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue between friends, annotated. "
            "1. Lea: Salut Marc! Ca va? [informal greeting] (Hi Marc! How "
            "are you?) 2. Marc: Salut Lea! Ca va super, et toi? [reciprocal] "
            "(Hi Lea! Great, and you?) 3. Lea: Pas mal. Tu as passe un bon "
            "week-end? [small talk] (Not bad. Did you have a good weekend?) "
            "4. Marc: Genial! Je suis alle a la mer. [passe compose, etre] "
            "(Great! I went to the seaside.) 5. Lea: La chance! Il faisait "
            "beau? [imparfait for weather] (Lucky! Was the weather nice?) 6. "
            "Marc: Oui, un temps magnifique. Et toi, quoi de neuf? [returning "
            "the question] (Yes, magnificent weather. And you, what is new?) "
            "7. Lea: Pas grand-chose. Je bosse beaucoup en ce moment. "
            "[bosser = slang for travailler] (Not much. I work a lot right "
            "now.) 8. Marc: Tu veux prendre un cafe? [invitation] (Want to "
            "grab a coffee?) 9. Lea: Avec plaisir! On va ou? [accepting] "
            "(With pleasure! Where to?) 10. Marc: Au petit bistrot de la "
            "place? [suggestion] (To the little bistro on the square?) 11. "
            "Lea: Bonne idee. Tu viens souvent ici? [agreement + question] "
            "(Good idea. Do you come here often?) 12. Marc: Oui, le serveur "
            "me connait. [habit] (Yes, the waiter knows me.) 13. Lea: Deux "
            "cafes, s'il vous plait. [ordering for two] (Two coffees, "
            "please.) 14. Serveur: Tout de suite. [service reply] (Right "
            "away.) 15. Lea: Alors, raconte! [prompting stories] (So, tell "
            "me!) 16. Marc: Tu ne devineras jamais... [teasing] (You will "
            "never guess...) 17. Lea: Arrete, dis-moi! [playful pressure] "
            "(Stop it, tell me!) 18. Marc: J'ai rencontre une vieille amie "
            "d'ecole. [the news] (I met an old school friend.) 19. Lea: "
            "C'est genial! On se revoit bientot? [reaction + plan] (That is "
            "great! Shall we meet again soon?) 20. Marc: Oui, je t'appelle "
            "cette semaine. A plus! [promise + informal goodbye] (Yes, I "
            "will call you this week. See you!) The dialogue runs on tu, "
            "slang (bosser, genial), and the passe compose/imparfait dance "
            "of storytelling."
        ),
        "how_it_works": (
            "Friend dialogues work on the informal engine: tu everywhere, "
            "slang seasoning (bosser, genial, pas mal), short questions, "
            "and the storytelling alternation of passe compose events with "
            "imparfait background. Small talk follows the weather-weekend-"
            "news circuit before the real topic lands. Invitations are "
            "casual (Tu veux prendre un cafe?) and accepted with Avec "
            "plaisir! The dialogue is the payoff of the whole database: "
            "greetings, questions, tenses, and idioms all firing in one "
            "natural exchange. Shadow it - repeat each line aloud right "
            "after reading - and the rhythm transfers to your own speech."
        ),
        "key_points": [
            "Informal engine: tu, slang (bosser, genial), short questions.",
            "Small-talk circuit: weather -> weekend -> news -> real topic.",
            "Storytelling alternates passe compose events with imparfait background.",
            "Invitations: Tu veux prendre un cafe? / Avec plaisir!",
            "Shadow the dialogue aloud to transfer the rhythm.",
        ],
        "requirements": [
            "20-line bilingual dialogue (French + English), annotated.",
            "Informal register with slang and storytelling tenses.",
        ],
        "standards": [
            "Dialogue pragmatics follow Battye, Hintze, and Rowlett.",
            "Slang usage follows Fagyal, Kibbee, and Jenkins.",
        ],
        "citations": [
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
            "Fagyal Z, Kibbee D, Jenkins F. French: A Linguistic Introduction. Cambridge; 2006.",
        ],
        "sig_lens": (
            "The Signature read: the friend dialogue is the seal pressed "
            "among equals - no ceremony, full force, the truest "
            "impression. The Signature Language Method practices the "
            "informal press most, because friends are the daily work."
        ),
    },
    {
        "key": "dialogue-problem",
        "name": "French Conversation: Solving a Problem",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue solving a lost-luggage "
            "problem, annotated. 1. Voyageur: Excusez-moi, j'ai un probleme. "
            "[formal opening] (Excuse me, I have a problem.) 2. Agent: Je "
            "vous ecoute. Qu'est-ce qui se passe? [service listening] (I am "
            "listening. What is happening?) 3. Voyageur: Ma valise n'est pas "
            "arrivee. [stating the problem, passe compose] (My suitcase did "
            "not arrive.) 4. Agent: Quel etait votre vol? [gathering facts] "
            "(What was your flight?) 5. Voyageur: Le vol AF 342 de New York. "
            "[details] (Flight AF 342 from New York.) 6. Agent: Avez-vous "
            "votre ticket de bagage? [procedure] (Do you have your baggage "
            "ticket?) 7. Voyageur: Oui, le voila. [complying] (Yes, here it "
            "is.) 8. Agent: Je verifie dans le systeme. Un moment, s'il "
            "vous plait. [process] (I check the system. One moment, "
            "please.) 9. Voyageur: Pensez-vous qu'on va la retrouver? "
            "[worried question] (Do you think we will find it?) 10. Agent: "
            "Ne vous inquietez pas, ca arrive souvent. [reassurance] (Do "
            "not worry, it happens often.) 11. Voyageur: Que dois-je faire "
            "maintenant? [asking next steps] (What should I do now?) 12. "
            "Agent: Remplissez ce formulaire, s'il vous plait. [instruction] "
            "(Fill in this form, please.) 13. Voyageur: C'est fait. Et "
            "ensuite? [confirming + next] (Done. And then?) 14. Agent: Nous "
            "vous appellerons des qu'on la trouve. [promise] (We will call "
            "you as soon as we find it.) 15. Voyageur: Combien de temps ca "
            "prend en general? [timeline] (How long does it usually take?) "
            "16. Agent: En general vingt-quatre heures. [answer] (Usually "
            "twenty-four hours.) 17. Voyageur: Et mes affaires urgentes? "
            "[escalation] (And my urgent belongings?) 18. Agent: Gardez les "
            "factures, on vous remboursera. [solution] (Keep the receipts, "
            "we will reimburse you.) 19. Voyageur: Merci beaucoup pour votre "
            "aide. [thanks] (Thank you very much for your help.) 20. Agent: "
            "De rien, bon sejour a Paris! [close with wish] (You are "
            "welcome, enjoy your stay in Paris!) The dialogue runs the "
            "problem script: state, detail, procedure, worry, next steps, "
            "timeline, escalation, solution, thanks."
        ),
        "how_it_works": (
            "Problem dialogues work as the formal-register stress test: "
            "vous throughout, conditional softeners (Pensez-vous que...? "
            "Que dois-je faire?), and the service script of listen -> "
            "gather -> process -> reassure -> instruct -> promise. Key "
            "moves: state the problem in one passe compose sentence (Ma "
            "valise n'est pas arrivee), ask the next step (Que dois-je "
            "faire?), ask the timeline (Combien de temps?), escalate "
            "politely (Et mes affaires urgentes?). The agent's reassurance "
            "formulas (Ne vous inquietez pas, Un moment s'il vous plait) "
            "are worth memorizing whole. Run this script mentally before "
            "any service counter and the French comes out under pressure."
        ),
        "key_points": [
            "Problem script: state -> detail -> procedure -> worry -> next steps -> timeline -> solution -> thanks.",
            "State the problem in one passe compose sentence.",
            "Key questions: Que dois-je faire? Combien de temps?",
            "Reassurance formulas worth memorizing whole.",
            "Vous and conditionals throughout the formal stress test.",
        ],
        "requirements": [
            "20-line bilingual dialogue (French + English), annotated.",
            "Full problem-resolution script in formal register.",
        ],
        "standards": [
            "Dialogue pragmatics follow Battye, Hintze, and Rowlett.",
            "Service formulas follow Price 7th ed.",
        ],
        "citations": [
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
            "Price G. A Comprehensive French Grammar. 7th ed. Wiley-Blackwell; 2007.",
        ],
        "sig_lens": (
            "The Signature read: the problem dialogue is the press under "
            "load - the true test of every seal is pressure. The Signature "
            "Language Method drills the formal script until it holds at "
            "full pressure, because trouble never waits for rehearsal."
        ),
    },
    {
        "key": "mastery",
        "name": "French Mastery Review and Full Reference",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The whole database in one teaching summary. Alphabet: 26 "
            "letters (a-z) with French names; 5 diacritics (acute, grave, "
            "circumflex, diaeresis, cedilla); guillemets << >> for quotes. "
            "Sounds: 12 oral vowels, 4 nasal vowels (an, in, on, un), final "
            "stress, liaison, elision. Two hundred core words, grouped: "
            "people (homme, femme, enfant, ami, pere, mere, frere, soeur, grand-pere, grand-mere, "
            "famille, monde), home (maison, appartement, chambre, cuisine, "
            "salon, porte, fenetre, table, chaise, lit, jardin, garage), food (pain, eau, "
            "lait, fromage, viande, poisson, fruit, legume, cafe, vin, sucre, sel), "
            "time (jour, nuit, matin, soir, semaine, mois, annee, heure, "
            "temps, aujourd'hui, hier, demain), nature (soleil, lune, ciel, terre, mer, "
            "arbre, fleur, oiseau, chien, chat, riviere, montagne), body (tete, yeux, main, "
            "pied, coeur, dos, bras, jambe, bouche, oreille, nez, doigt), verbs (etre, "
            "avoir, faire, aller, dire, pouvoir, vouloir, savoir, venir, "
            "prendre, voir, donner, parler, manger, boire, dormir, "
            "travailler, aimer, penser, mettre, rester, devenir, connaitre, ecouter), adjectives (grand, petit, "
            "bon, mauvais, beau, nouveau, vieux, jeune, long, court, chaud, "
            "froid, rapide, lent, fort, heureux, triste, facile, difficile, "
            "premier, riche, pauvre), adverbs and function words (bien, mal, vite, souvent, "
            "toujours, jamais, tres, trop, ici, la, oui, non, merci, s'il "
            "vous plait, pardon, deja, encore, aussi, seulement), question words (qui, que, ou, quand, "
            "pourquoi, comment, combien, quel, lequel, laquelle), pronouns (je, tu, il, elle, "
            "nous, vous, ils, le, la, les, lui, leur, mon, ton, son, ce, "
            "cette), numbers (un, deux, trois, quatre, cinq, six, sept, huit, neuf, dix, "
            "onze, douze, treize, quatorze, quinze, seize, dix-sept, dix-huit, dix-neuf, vingt, "
            "trente, quarante, cinquante, soixante, cent, mille), "
            "connectors (et, ou, mais, "
            "parce que, quand, si, comme, donc, alors, cependant). Key "
            "grammar: SVO order; two genders; silent plural -s; partitive "
            "du/de la/des; ne...pas negation; three question forms; "
            "adjectives agree and mostly follow; BANGS precede; etre/avoir "
            "auxiliaries; passe compose vs imparfait; futur proche vs futur "
            "simple; subjunctive triggers (il faut que, je veux que, bien "
            "que). Phrase tables: greetings (Bonjour, Bonsoir, Salut, Au "
            "revoir, Merci, S'il vous plait), survival (Ou est...?, Combien "
            "coute...?, Je voudrais..., L'addition s'il vous plait, Au "
            "secours!), time (Quelle heure est-il? Il est midi/minuit), "
            "feelings (J'ai faim/soif/peur/froid/chaud). Study path: read "
            "records 1-10 in order, drill one themed set daily (11-20), "
            "conjugate aloud (21), run the Q&A and commands (22-23), tell "
            "the three stories from memory (25-27), deploy one idiom a day "
            "(28), rehearse the dialogues with a partner (31-33). At 34 "
            "records the learner holds the complete ladder: foundations "
            "stamped, compounded riveted, advanced engraved."
        ),
        "how_it_works": (
            "The mastery review works as the single-page control panel: "
            "everything the database teaches, compressed to the essentials "
            "a learner can scan in ten minutes and drill for a year. The "
            "200 core words cover about 80 percent of everyday conversation "
            "by frequency - they are the highest-leverage list in the "
            "language. The grammar panel is the seven-rule skeleton plus "
            "the tense triggers; the phrase tables are the survival kit. "
            "Use it as a pre-flight checklist before any trip, any exam, "
            "any conversation: scan the panel, spot the weak rivet, drill "
            "that record. The ladder is climbed one record at a time, but "
            "the view from the top is this page."
        ),
        "key_points": [
            "200 core words cover ~80 percent of everyday conversation.",
            "Alphabet, sounds, grammar, and phrase tables on one page.",
            "Study path: 1-10 in order, one themed set daily, conjugate aloud, stories from memory.",
            "Phrase tables: greetings, survival, time, feelings.",
            "Use as a pre-flight checklist: scan, spot the weak rivet, drill that record.",
        ],
        "requirements": [
            "Consolidated quick-reference: alphabet, 200 core words, key grammar, all phrase tables.",
            "Study path through the 34 records stated.",
            "Every word group translated or glossed.",
        ],
        "standards": [
            "Word selection follows Battye, Hintze, and Rowlett frequency guidance.",
            "Reference follows Grevisse and Goosse, Le Bon Usage 16th ed.",
        ],
        "citations": [
            "Battye A, Hintze M-A, Rowlett P. The French Language Today. 2nd ed. Routledge; 2000.",
            "Grevisse M, Goosse A. Le Bon Usage: Grammaire francaise. 16th ed. De Boeck; 2016.",
            "Organisation internationale de la Francophonie. La langue francaise dans le monde 2022. Gallimard; 2022.",
        ],
        "sig_lens": (
            "The Signature read: the mastery page is the finished seal, "
            "held up to the light - every line of the ladder visible in "
            "one impression. The Signature Language Method ends where it "
            "began: stamp the sound, seal the word, sign the sentence."
        ),
    },
]

# build.py combines ENTRIES_1 + ENTRIES_2 into ENTRIES.
