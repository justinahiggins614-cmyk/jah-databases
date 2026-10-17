#!/usr/bin/env python3
"""Entries for The English to English Database (language-english)
and its Signature edition (language-english-signature).

34 ladder-ordered records per the shared per-language template:
1 overview, 2 writing system, 3 phonology, 4-6 core words,
7 pronouns, 8 numbers and time, 9 greetings, 10 grammar essentials,
11-20 themed sentence sets, 21 verb tenses, 22 questions and answers,
23 commands and requests, 24 descriptions, 25-27 stories, 28 idioms,
29 formal registers, 30 complex sentences, 31-33 conversations,
34 mastery review.

Public = real, fact-checked English pedagogy for non-native learners.
Signature = the same ladder through the Signature lens, clearly labeled.
"""

SIG_TAIL = ("Signature-generated interpretation, clearly labeled "
            "Signature-made and never presented as authentic public record.")

ENTRIES = [
# ------------------------------------------------------------------ 1
dict(key="overview", name="Language Overview: English", group="Foundations",
     ladder_rank=1, ladder_tier="foundations",
     description=(
         "English is the language you are learning, taught here in English "
         "itself so every lesson doubles as reading practice. Its native "
         "name is English, written the same in the Latin alphabet you will "
         "master in record 2. English belongs to the Indo-European family, "
         "on the Germanic branch, alongside German and Dutch. About 380 "
         "million people speak English as their first language, and more "
         "than 1.5 billion people use it in total, making it the most widely "
         "used language in the world for science, aviation, computing, and "
         "international business. It is an official language in 58 "
         "countries, including the United States, the United Kingdom, "
         "Canada, Australia, Ireland, New Zealand, Nigeria, India, and "
         "many more, and it is the working language of most international "
         "organizations. Major dialects include American, British, "
         "Australian, and Canadian English; they differ mostly in "
         "pronunciation, a few hundred words, and some spellings, and "
         "speakers of one dialect easily understand the others."),
     how_it_works=(
         "This database teaches English the way you would climb a ladder: "
         "each record builds on the last, from the alphabet (record 2) to "
         "full conversations (records 31 to 33) to a complete reference "
         "(record 34). Because the target language and the teaching "
         "language are both English, every explanation is itself a "
         "sentence to study. Read each record out loud when you can: "
         "English spelling and English sound follow regular patterns once "
         "you know them, and your mouth learns what your eyes practice. "
         "Example of the ladder in action: record 2 teaches the letter A; "
         "record 4 teaches the word apple; record 10 teaches the sentence "
         "'An apple is red'; record 21 teaches 'I ate an apple yesterday'; "
         "record 28 teaches the idiom 'the apple of my eye'. One small "
         "word, grown step by step into fluent English."),
     key_points=[
         "English is a Germanic language in the Indo-European family, ISO codes en (639-1) and eng (639-3).",
         "About 380 million native speakers; more than 1.5 billion total users worldwide.",
         "Official language in 58 countries and the working language of science, aviation, and computing.",
         "Written with the 26-letter Latin alphabet, read left to right.",
         "Major dialects (American, British, Australian, Canadian) are mutually intelligible.",
         "English has no tones and no grammatical gender for nouns; word order carries meaning.",
         "Every record in this database contains full example sentences, never vocabulary lists alone."],
     requirements=["No prior English needed; start at record 1.",
                   "A notebook for copying sentences by hand.",
                   "Reading each record aloud when possible."],
     standards=["ISO 639-1/639-3 language codes (en / eng).",
                "Speaker figures consistent with Ethnologue-style estimates; rounded, labeled approximate."],
     citations=["International Organization for Standardization. ISO 639 language codes.",
                "Council of Europe. Common European Framework of Reference for Languages: Companion Volume. 2020."],
     sig_lens=(
         "The Signature learner treats English as a workshop: each record a "
         "new tool on the bench, from the alphabet as the raw stock to "
         "idioms as the finished joinery. Nothing here is memorized and "
         "left on a shelf; every lesson is a working tool, picked up and "
         "used the same day, because a tool that never leaves the bench "
         "was never really owned. The ladder is the Signature way: one "
         "honest step, fully mastered, before the next."),
     demo_kind="ref", demo_data={
         "native_name": "English", "iso1": "en", "iso3": "eng",
         "family": "Indo-European", "branch": "Germanic",
         "native_speakers_m": 380, "total_users_m": 1500,
         "letters": 26, "official_countries": 58,
         "dialects": ["American", "British", "Canadian", "Australian"]}),
# ------------------------------------------------------------------ 2
dict(key="writing", name="The English Writing System", group="Foundations",
     ladder_rank=1, ladder_tier="foundations",
     description=(
         "English is written with the Latin alphabet: 26 letters, each with "
         "an uppercase (capital) form and a lowercase (small) form. The "
         "letters are A B C D E F G H I J K L M N O P Q R S T U V W X Y Z, "
         "and in lowercase a b c d e f g h i j k l m n o p q r s t u v w x "
         "y z. Text runs left to right and lines run top to bottom. "
         "Sentences begin with a capital letter and end with a period (.), "
         "a question mark (?), or an exclamation mark (!). The apostrophe "
         "(apostrophe) marks contractions like do not becoming don't and "
         "possession like the learner's book. The comma, colon, semicolon, "
         "and quotation marks organize longer writing. English uses the "
         "Arabic numerals 0 1 2 3 4 5 6 7 8 9. Because English borrows words "
         "from many languages, spelling must be learned word by word, but "
         "about 84 percent of English words follow regular spelling "
         "patterns."),
     how_it_works=(
         "Learn the letters in two groups: first the 5 vowels A E I O U, "
         "which name the main mouth-open sounds, then the 21 consonants. "
         "Practice writing each letter in both cases until your hand knows "
         "them. Read the sample sentence and point at each word as you "
         "say it: 'The quick brown fox jumps over the lazy dog.' This one "
         "sentence uses all 26 letters, which is why typists have practiced "
         "it for a hundred years. Notice the capital T at the start and "
         "the period at the end. Copy it five times. Then try: 'Pack my "
         "box with five dozen liquor jugs.' Same trick, all 26 letters. "
         "Capital letters also mark proper nouns: names of people (Maria), "
         "places (Paris), days (Monday), and months (January). Common nouns "
         "like dog and city stay lowercase."),
     key_points=[
         "26 letters, each with uppercase and lowercase forms.",
         "5 vowels (A E I O U) and 21 consonants.",
         "Write left to right; sentences start with a capital and end with . ? or !",
         "Apostrophes mark contractions (don't) and possession (learner's).",
         "Proper nouns take capitals: people, places, days, months.",
         "Numerals 0-9 are the Arabic digits.",
         "Most English spelling follows regular patterns; the rest is memorized word by word."],
     requirements=["Practice paper and a pen for letter formation.",
                   "Reading each sample sentence aloud."],
     standards=["Latin alphabet per Unicode Basic Latin block (U+0041-U+005A, U+0061-U+007A)."],
     citations=["Unicode Consortium. The Unicode Standard: Latin script blocks.",
                "Merriam-Webster. Guide to punctuation and style."],
     sig_lens=(
         "The Signature learner treats the alphabet as raw stock: 26 pieces "
         "of material, each one measured in two forms, capital and small. "
         "Before any building comes the inventory - know every piece by "
         "sight and by hand, the way a craftsperson knows every tool in "
         "the chest. The pangram sentence is the first project: one "
         "sentence that uses the whole stock, cut cleanly, no scrap left."),
     demo_kind="phonics", demo_data={
         "kind": "alphabet",
         "letters": list("abcdefghijklmnopqrstuvwxyz"),
         "vowels": ["a", "e", "i", "o", "u"],
         "pangram": "The quick brown fox jumps over the lazy dog"}),
# ------------------------------------------------------------------ 3
dict(key="phonology", name="English Pronunciation and Phonology", group="Foundations",
     ladder_rank=2, ladder_tier="foundations",
     description=(
         "English uses about 44 distinct sounds: 24 consonant sounds and 20 "
         "vowel sounds, all written with the 26 letters, which is why one "
         "letter can stand for several sounds. Consonants are made by "
         "blocking or narrowing the airflow: lips (p, b, m), teeth (th as "
         "in think and this), tongue ridge (t, d, n, s, z), and throat "
         "area (k, g). English pairs many sounds by voicing: the vocal "
         "cords buzz for b, d, g, v, z and stay still for p, t, k, f, s. "
         "Put your hand on your throat and feel the difference between "
         "'sip' and 'zip'. Vowels are open sounds: short vowels as in cat, "
         "bed, sit, hot, cup; long vowels as in see, blue, car; and "
         "diphthongs, two vowel sounds gliding together, as in my, now, "
         "and boy. Word stress matters: PHOtograph, phoTOgraphy, and "
         "photoGRAPHic stress different syllables. English is a stress-timed "
         "language: stressed syllables come at roughly even beats, and "
         "unstressed syllables shrink toward the weak 'uh' sound called "
         "schwa, as the a in about."),
     how_it_works=(
         "Start with the voicing pairs: say p then b, t then d, k then g, "
         "f then v, s then z, feeling your throat buzz on the second of "
         "each pair. Then practice the two th sounds: think (no buzz) and "
         "this (buzz), tongue tip lightly between the teeth. For vowels, "
         "stretch each short vowel: a as in cat, e as in bed, i as in sit, "
         "o as in hot, u as in cup. Then the long ones: ee as in see, oo "
         "as in blue, ar as in car. Then glide the diphthongs: my (ah-ee), "
         "now (ah-oo), boy (oh-ee). Finally, stress: say PHOtograph "
         "(stress first), phoTOgraphy (stress second), photoGRAPHic "
         "(stress third) - same root, three stress patterns, and the "
         "unstressed vowels shrink to schwa. Ten spoken examples to drill: "
         "ship (short i), sheep (long ee), full (short oo), fool (long oo), "
         "think (voiceless th), this (voiced th), light (long i), right "
         "(long i), about (schwa first syllable), banana (schwa first and "
         "last syllables)."),
     key_points=[
         "About 44 sounds: 24 consonants and 20 vowels, from 26 letters.",
         "Voicing pairs: p/b, t/d, k/g, f/v, s/s-z; feel the throat buzz.",
         "Two th sounds: think (voiceless) and this (voiced).",
         "Vowels: short (cat), long (see), and gliding diphthongs (my, now, boy).",
         "Word stress moves: PHOtograph, phoTOgraphy, photoGRAPHic.",
         "Unstressed syllables shrink to schwa, the 'uh' in about and banana.",
         "English is stress-timed: stressed beats fall at roughly even intervals."],
     requirements=["A mirror to watch lip and tongue positions.",
                   "Saying every example word aloud three times."],
     standards=["IPA transcription following the Handbook of the International Phonetic Association (1999)."],
     citations=["International Phonetic Association. Handbook of the International Phonetic Association. Cambridge University Press; 1999.",
                "Roach P. English Phonetics and Phonology. 4th ed. Cambridge University Press; 2009."],
     sig_lens=(
         "The Signature learner treats pronunciation as tuning an "
         "instrument: 44 strings, each tightened to its true pitch. The "
         "throat test for voicing is the tuner - no guessing, feel the "
         "buzz or its absence. Stress is the rhythm section: find the beat "
         "syllable and the rest of the word dances around it. Tune daily, "
         "and the instrument stays true."),
     demo_kind="phonics", demo_data={
         "kind": "phonemes",
         "consonants": 24, "vowels": 20,
         "voicing_pairs": [["p","b"],["t","d"],["k","g"],["f","v"],["s","z"],["th","thh"]],
         "drill_words": ["ship","sheep","full","fool","think","this","light","right","about","banana"],
         "stress_sets": ["PHOtograph","phoTOgraphy","photoGRAPHic"]}),
# ------------------------------------------------------------------ 4
dict(key="nouns1", name="Core Nouns I: People, Places, and Things", group="Foundations",
     ladder_rank=2, ladder_tier="foundations",
     description=(
         "Nouns name people, places, and things, and they are the anchors "
         "of every English sentence. English nouns do not change for "
         "gender: a table is simply a table. Most nouns form the plural by "
         "adding s (book to books) or es after s, sh, ch, x, or z sounds "
         "(box to boxes, church to churches). Some plurals are irregular "
         "and must be memorized: man to men, woman to women, child to "
         "children, foot to feet, tooth to teeth, mouse to mice. Countable "
         "nouns can take a number (three apples); uncountable nouns like "
         "water, rice, and information cannot, and use some or much "
         "instead. Proper nouns name one specific person, place, or thing "
         "and take a capital letter: Maria, Paris, Monday. Below are 25 "
         "essential nouns, each with a full example sentence to study and "
         "copy."),
     how_it_works=(
         "Study each noun with its sentence, then make the plural out loud: "
         "one book, two books; one box, two boxes; one child, two children. "
         "Notice which nouns are countable and which are not. Man: 'The man "
         "is reading a newspaper.' Woman: 'The woman is cooking dinner.' "
         "Child: 'The child is playing in the garden.' Friend: 'My friend "
         "lives near the school.' House: 'The house has a red door.' "
         "School: 'The school opens at eight o'clock.' City: 'The city is "
         "busy at night.' Book: 'The book is on the table.' Table: 'The "
         "table is made of wood.' Water: 'Drink some water every day.' "
         "Food: 'The food smells delicious.' Time: 'We have enough time.' "
         "Day: 'Today is a beautiful day.' Hand: 'Wash your hands before "
         "dinner.' Eye: 'She has brown eyes.' Dog: 'The dog is sleeping "
         "under the tree.' Cat: 'The cat drinks milk.' Tree: 'The tree "
         "gives us shade.' Car: 'The car needs fuel.' Money: 'Save your "
         "money for the trip.' Work: 'His work starts at nine.' Name: "
         "'What is your name?' Word: 'Say the word slowly.' Story: 'The "
         "story made us laugh.' Question: 'Ask your question now.' Answer: "
         "'The answer is forty-two.' Now cover the English side and recall "
         "each noun from its sentence alone."),
     key_points=[
         "Nouns name people, places, and things; no gender in English.",
         "Regular plurals add s or es; irregular plurals (men, children, feet) are memorized.",
         "Countable nouns take numbers; uncountable nouns (water, information) do not.",
         "Proper nouns take capitals: Maria, Paris, Monday.",
         "Every noun below comes with a full example sentence.",
         "Learn noun plus sentence together, not the word alone."],
     requirements=["Saying each plural aloud.",
                   "Copying five sentences by hand each day."],
     standards=["Plurals and countability per standard learner dictionaries (Merriam-Webster, Oxford)."],
     citations=["Merriam-Webster's Collegiate Dictionary. Plural formation entries.",
                "Swan M. Practical English Usage. 4th ed. Oxford University Press; 2016."],
     sig_lens=(
         "The Signature learner treats nouns as the foundation stones of "
         "the workshop: people, places, and things, each one a solid "
         "block. Lay 25 stones today - man, woman, child, friend, house - "
         "and tomorrow the walls of real sentences rise on them. A stone "
         "learned with its sentence is mortared in place; a stone learned "
         "alone rolls away."),
     demo_kind="vocab", demo_data={
         "words": [
             {"w":"man","s":"The man is reading a newspaper."},
             {"w":"woman","s":"The woman is cooking dinner."},
             {"w":"child","s":"The child is playing in the garden."},
             {"w":"friend","s":"My friend lives near the school."},
             {"w":"house","s":"The house has a red door."},
             {"w":"school","s":"The school opens at eight o'clock."},
             {"w":"city","s":"The city is busy at night."},
             {"w":"book","s":"The book is on the table."},
             {"w":"table","s":"The table is made of wood."},
             {"w":"water","s":"Drink some water every day."},
             {"w":"food","s":"The food smells delicious."},
             {"w":"time","s":"We have enough time."},
             {"w":"day","s":"Today is a beautiful day."},
             {"w":"hand","s":"Wash your hands before dinner."},
             {"w":"eye","s":"She has brown eyes."},
             {"w":"dog","s":"The dog is sleeping under the tree."},
             {"w":"cat","s":"The cat drinks milk."},
             {"w":"tree","s":"The tree gives us shade."},
             {"w":"car","s":"The car needs fuel."},
             {"w":"money","s":"Save your money for the trip."},
             {"w":"work","s":"His work starts at nine."},
             {"w":"name","s":"What is your name?"},
             {"w":"word","s":"Say the word slowly."},
             {"w":"story","s":"The story made us laugh."},
             {"w":"question","s":"Ask your question now."}]}),
# ------------------------------------------------------------------ 5
dict(key="verbs1", name="Core Verbs I: Essential Action Words", group="Foundations",
     ladder_rank=3, ladder_tier="foundations",
     description=(
         "Verbs are the engines of sentences: they say what happens. The "
         "base form (be, have, go) is the dictionary form; add s for he, "
         "she, and it in the present (she goes); add ing for ongoing action "
         "(I am going); add ed for most past actions (I walked). Irregular "
         "verbs change their shape and must be memorized: go to went to "
         "gone, eat to ate to eaten, see to saw to seen, do to did to "
         "done, have to had to had. The verb be is the most irregular of "
         "all: I am, you are, he is, we are, they are in the present; I "
         "was, you were, he was in the past. Auxiliary verbs (do, have, "
         "will, can, must) team up with main verbs to build questions, "
         "negatives, and tenses. Below are 25 essential verbs, each with a "
         "full example sentence."),
     how_it_works=(
         "Learn each verb in three shapes: base, past, and the ing form. "
         "Say them as a chant: go, went, going; eat, ate, eating; see, saw, "
         "seeing. Be: 'I am a learner.' (I am = present of be.) Have: 'I "
         "have two brothers.' Do: 'They do their homework.' Go: 'We go to "
         "school by bus.' Come: 'Come here, please.' Make: 'She makes bread "
         "every morning.' Take: 'Take your umbrella.' Give: 'Give me your "
         "hand.' Get: 'I get up at six.' Know: 'I know the answer.' Think: "
         "'I think it will rain.' See: 'I see a bird.' Look: 'Look at the "
         "sky.' Want: 'I want some tea.' Need: 'We need more time.' Like: "
         "'She likes music.' Love: 'They love their grandmother.' Eat: 'We "
         "eat dinner at seven.' Drink: 'Drink your milk.' Read: 'He reads "
         "every night.' Write: 'Write your name here.' Speak: 'She speaks "
         "three languages.' Say: 'Say it again.' Work: 'He works in a "
         "hospital.' Play: 'The children play football.' Help: 'Can you "
         "help me?' Now build the past: 'I went', 'she ate', 'they saw' - "
         "irregulars first, because regular ed verbs take care of "
         "themselves."),
     key_points=[
         "Verbs say what happens; learn base, past, and ing forms together.",
         "Third person present adds s: she goes, he eats.",
         "Irregular verbs change shape: go/went/gone, eat/ate/eaten.",
         "Be is fully irregular: am/is/are, was/were.",
         "Auxiliaries (do, have, will, can, must) build questions and negatives.",
         "Every verb below comes with a full example sentence."],
     requirements=["Chanting base-past-ing triples aloud.",
                   "Writing five new sentences with verbs from the list."],
     standards=["Verb paradigms per standard reference grammars (Swan; Cambridge Grammar)."],
     citations=["Swan M. Practical English Usage. 4th ed. Oxford University Press; 2016.",
                "Huddleston R, Pullum GK. The Cambridge Grammar of the English Language. 2002."],
     sig_lens=(
         "The Signature learner treats verbs as engines: nouns are the "
         "stones, verbs are what moves them. Twenty-five engines on the "
         "bench - be, have, go, make, take - and the irregulars are the "
         "high-performance models, each with its own custom shape. Learn "
         "the triple chant the way a mechanic learns an engine's sound: "
         "base, past, ing, until you hear it right without thinking."),
     demo_kind="vocab", demo_data={
         "words": [
             {"w":"be","s":"I am a learner.","alt":["am","is","are"]},
             {"w":"have","s":"I have two brothers."},
             {"w":"do","s":"They do their homework."},
             {"w":"go","s":"We go to school by bus."},
             {"w":"come","s":"Come here, please."},
             {"w":"make","s":"She makes bread every morning."},
             {"w":"take","s":"Take your umbrella."},
             {"w":"give","s":"Give me your hand."},
             {"w":"get","s":"I get up at six."},
             {"w":"know","s":"I know the answer."},
             {"w":"think","s":"I think it will rain."},
             {"w":"see","s":"I see a bird."},
             {"w":"look","s":"Look at the sky."},
             {"w":"want","s":"I want some tea."},
             {"w":"need","s":"We need more time."},
             {"w":"like","s":"She likes music."},
             {"w":"love","s":"They love their grandmother."},
             {"w":"eat","s":"We eat dinner at seven."},
             {"w":"drink","s":"Drink your milk."},
             {"w":"read","s":"He reads every night."},
             {"w":"write","s":"Write your name here."},
             {"w":"speak","s":"She speaks three languages."},
             {"w":"say","s":"Say it again."},
             {"w":"work","s":"He works in a hospital."},
             {"w":"help","s":"Can you help me?"}]}),
# ------------------------------------------------------------------ 6
dict(key="adjadv", name="Adjectives and Adverbs", group="Foundations",
     ladder_rank=3, ladder_tier="foundations",
     description=(
         "Adjectives describe nouns (a red car, a tall man) and adverbs "
         "describe verbs, adjectives, or other adverbs (drive carefully, "
         "very tall, quite slowly). English adjectives never change for "
         "gender or number: one red car, two red cars. Most adverbs are "
         "built by adding ly to an adjective: quick to quickly, careful to "
         "carefully, slow to slowly. Some adverbs are irregular: good "
         "becomes well (not goodly), fast stays fast, hard stays hard. "
         "Comparison: short adjectives add er and est (tall, taller, "
         "tallest); longer adjectives use more and most (beautiful, more "
         "beautiful, most beautiful); irregulars must be memorized: good, "
         "better, best; bad, worse, worst; far, farther, farthest. Adjective "
         "order in English follows a fixed habit: opinion, size, age, "
         "color, origin, material - 'a beautiful small old red Italian "
         "wooden box'. Below are 25 adjectives and 15 adverbs, each with a "
         "sentence."),
     how_it_works=(
         "Pair each adjective with a noun and each adverb with a verb, "
         "aloud: 'a big house', 'she sings beautifully'. Big: 'An elephant "
         "is big.' Small: 'A mouse is small.' Good: 'This is a good book.' "
         "Bad: 'Smoking is bad for you.' Happy: 'The children are happy.' "
         "Sad: 'She felt sad yesterday.' New: 'I bought a new phone.' Old: "
         "'My grandfather is old.' Young: 'The young man runs fast.' Long: "
         "'The river is long.' Short: 'Her hair is short.' High: 'The "
         "mountain is high.' Low: 'The price is low.' Hot: 'The soup is "
         "hot.' Cold: 'The water is cold.' Beautiful: 'The garden is "
         "beautiful.' Ugly: 'The old wall is ugly.' Rich: 'He is a rich "
         "man.' Poor: 'Help poor families.' Strong: 'He is strong.' Weak: "
         "'She felt weak after illness.' Easy: 'This lesson is easy.' "
         "Difficult: 'The exam was difficult.' Fast: 'A cheetah is fast.' "
         "Slow: 'The turtle is slow.' Clean: 'Keep your room clean.' "
         "Dirty: 'Wash your dirty hands.' Adverbs - Quickly: 'She ran "
         "quickly.' Slowly: 'Speak slowly, please.' Carefully: 'Drive "
         "carefully.' Loudly: 'They laughed loudly.' Quietly: 'Walk "
         "quietly.' Well: 'He plays well.' Badly: 'She slept badly.' "
         "Always: 'I always brush my teeth.' Never: 'He never lies.' "
         "Often: 'We often visit them.' Sometimes: 'It sometimes rains.' "
         "Very: 'It is very cold.' Too: 'The tea is too hot.' Really: 'I "
         "really like it.' Now compare: 'tall, taller, tallest' and "
         "'beautiful, more beautiful, most beautiful'."),
     key_points=[
         "Adjectives describe nouns; adverbs describe verbs, adjectives, or adverbs.",
         "English adjectives never change for gender or number.",
         "Most adverbs add ly: quickly, carefully; good becomes well.",
         "Comparisons: taller/tallest, more/most beautiful; good/better/best is irregular.",
         "Adjective order: opinion, size, age, color, origin, material.",
         "25 adjectives and 15 adverbs below, each with a sentence."],
     requirements=["Pairing each word with its partner (noun or verb) aloud.",
                   "Practicing the comparison triples."],
     standards=["Adjective ordering and adverb formation per standard reference grammars."],
     citations=["Swan M. Practical English Usage. 4th ed. Oxford University Press; 2016."],
     sig_lens=(
         "The Signature learner treats adjectives as paint and adverbs as "
         "the brushstroke: the noun is the wall, the adjective chooses "
         "the color, the adverb decides how the brush moves. Paint in the "
         "fixed order - opinion, size, age, color, origin, material - the "
         "way a craftsperson sands before staining. Forty new colors on "
         "the palette today; use every one in a sentence before sunset."),
     demo_kind="vocab", demo_data={
         "words": [
             {"w":"big","s":"An elephant is big."},
             {"w":"small","s":"A mouse is small."},
             {"w":"good","s":"This is a good book."},
             {"w":"happy","s":"The children are happy."},
             {"w":"new","s":"I bought a new phone."},
             {"w":"old","s":"My grandfather is old."},
             {"w":"long","s":"The river is long."},
             {"w":"hot","s":"The soup is hot."},
             {"w":"cold","s":"The water is cold."},
             {"w":"beautiful","s":"The garden is beautiful."},
             {"w":"strong","s":"He is strong."},
             {"w":"easy","s":"This lesson is easy."},
             {"w":"fast","s":"A cheetah is fast."},
             {"w":"clean","s":"Keep your room clean."},
             {"w":"quickly","s":"She ran quickly."},
             {"w":"slowly","s":"Speak slowly, please."},
             {"w":"carefully","s":"Drive carefully."},
             {"w":"quietly","s":"Walk quietly."},
             {"w":"well","s":"He plays well."},
             {"w":"always","s":"I always brush my teeth."},
             {"w":"never","s":"He never lies."},
             {"w":"often","s":"We often visit them."},
             {"w":"very","s":"It is very cold."},
             {"w":"really","s":"I really like it."}]}),
# ------------------------------------------------------------------ 7
dict(key="pronouns", name="Pronouns", group="Foundations",
     ladder_rank=4, ladder_tier="foundations",
     description=(
         "Pronouns stand in for nouns so sentences do not repeat the same "
         "name: 'Maria is here. She is my friend.' Personal pronouns: I, "
         "you, he, she, it, we, they. Object forms: me, you, him, her, it, "
         "us, them ('Give it to me'). Possessive adjectives: my, your, his, "
         "her, its, our, their ('This is my book'); possessive pronouns "
         "stand alone: mine, yours, his, hers, its, ours, theirs ('The book "
         "is mine'). Reflexive pronouns end in self/selves: myself, "
         "yourself, himself, herself, itself, ourselves, yourselves, "
         "themselves ('She taught herself'). Demonstratives point: this "
         "and these for near, that and those for far ('This apple is "
         "sweet; those apples are sour'). Interrogatives ask: who (people), "
         "what (things), which (choice), whose (ownership), whom (formal "
         "object). Indefinite pronouns generalize: someone, anyone, "
         "everyone, no one, something, nothing, everything."),
     how_it_works=(
         "Master the personal set first with the substitution drill: take "
         "'Maria is reading. Maria is happy.' and replace: 'Maria is "
         "reading. She is happy.' Then objects: 'I see Maria. I see her.' "
         "Possessives: 'This is my pen. The pen is mine.' Reflexives: 'He "
         "cut himself.' (himself = he, the same person). Demonstratives "
         "with pointing: hold a pen near - 'this pen'; point at a door far "
         "- 'that door'. Interrogatives in questions: 'Who is there?' "
         "'What is this?' 'Which one do you want?' 'Whose bag is this?' "
         "Indefinites in full sentences: 'Someone is knocking.' 'I need "
         "something to drink.' 'Everyone enjoyed the party.' 'Nothing is "
         "impossible.' Drill the full paradigm aloud: I-me-my-mine-myself; "
         "you-you-your-yours-yourself; he-him-his-his-himself; "
         "she-her-her-hers-herself; it-it-its-its-itself; "
         "we-us-our-ours-ourselves; they-them-their-theirs-themselves."),
     key_points=[
         "Personal pronouns: I, you, he, she, it, we, they.",
         "Objects: me, him, her, us, them ('Give it to me').",
         "Possessives: my book vs. the book is mine.",
         "Reflexives end in self/selves: myself, themselves.",
         "This/these = near; that/those = far.",
         "Who, what, which, whose ask; someone, everyone, nothing generalize.",
         "Drill the full I-me-my-mine-myself paradigm aloud."],
     requirements=["The substitution drill: noun to pronoun, aloud.",
                   "Pointing practice for this/that/these/those."],
     standards=["Pronoun paradigms per standard reference grammars."],
     citations=["Huddleston R, Pullum GK. The Cambridge Grammar of the English Language. 2002."],
     sig_lens=(
         "The Signature learner treats pronouns as quick-release fittings: "
         "the noun is the pipe, the pronoun the fitting that connects "
         "without re-cutting the pipe. I-me-my-mine-myself is one fitting "
         "in five sizes - learn the whole set and sentences connect fast, "
         "with no leaks and no repeated names dripping through the "
         "joints."),
     demo_kind="grammar", demo_data={
         "drills": [
             {"rule":"subject to object","from":"I see Maria.","to":"I see her."},
             {"rule":"possessive adjective","from":"This is my pen.","to":"The pen is mine."},
             {"rule":"reflexive","from":"He cut he.","to":"He cut himself."},
             {"rule":"demonstrative near","from":"pen (near)","to":"this pen"},
             {"rule":"demonstrative far","from":"door (far)","to":"that door"},
             {"rule":"who question","from":"___ is there?","to":"Who is there?"},
             {"rule":"what question","from":"___ is this?","to":"What is this?"},
             {"rule":"indefinite","from":"___ is knocking.","to":"Someone is knocking."}]}),
# ------------------------------------------------------------------ 8
dict(key="numbers", name="Numbers and Time", group="Foundations",
     ladder_rank=4, ladder_tier="foundations",
     description=(
         "Cardinal numbers count: one, two, three, up to ten, then eleven "
         "through nineteen, then the tens: twenty, thirty, forty, fifty, "
         "sixty, seventy, eighty, ninety. Combine them: twenty-one, "
         "thirty-five, ninety-nine, one hundred. Ordinal numbers order: "
         "first, second, third, fourth, fifth, then regular th: sixth, "
         "seventh, twentieth, hundredth. Days: Monday, Tuesday, Wednesday, "
         "Thursday, Friday, Saturday, Sunday. Months: January, February, "
         "March, April, May, June, July, August, September, October, "
         "November, December. Seasons: spring, summer, autumn (fall), "
         "winter. Clock time: 'It is three o'clock' for the hour; 'half "
         "past four' or 'four thirty' for 4:30; 'a quarter past five' for "
         "5:15; 'a quarter to six' for 5:45. Dates: 'May fifth' or 'the "
         "fifth of May', year 2026 spoken 'twenty twenty-six'."),
     how_it_works=(
         "Count aloud 1 to 20, then the tens to 100, then back down - "
         "speed builds memory. Learn the spelling traps: forty (not "
         "fourty), ninety, twelve, twenty. Ordinals: 'My birthday is on "
         "the third of June.' Days in order from Monday; months in order "
         "from January, spelling February carefully. Time drill: look at a "
         "clock and say it three ways - 'It is 4:30' as 'It is half past "
         "four' and 'It is four thirty'. Dates: 'Today is Saturday, "
         "October 17th, 2026.' Seasons with sentences: 'Spring brings "
         "flowers.' 'Summer is hot.' 'Autumn leaves fall.' 'Winter is "
         "cold.' Practice questions: 'What time is it?' 'It is ten "
         "fifteen.' 'What day is today?' 'It is Friday.' 'When is your "
         "birthday?' 'It is on May fifth.'"),
     key_points=[
         "Cardinals count (one, two); ordinals order (first, second).",
         "Spelling traps: forty, twelve, twenty, February.",
         "Days and months take capitals and go in fixed order.",
         "Clock: o'clock, half past, quarter past, quarter to.",
         "Dates: 'May fifth'; years: 'twenty twenty-six'.",
         "Every number and time phrase below has an example sentence."],
     requirements=["Counting aloud 1-100 and back.",
                   "Reading a real clock three ways."],
     standards=["Number words per standard learner dictionaries; date/time conventions per common usage."],
     citations=["Merriam-Webster. Number word entries.",
                "Associated Press Stylebook. Date and time conventions. 2024."],
     sig_lens=(
         "The Signature learner treats numbers as the measuring tape of "
         "the workshop: cardinals measure how many, ordinals mark the "
         "order of cuts, and the clock measures the day itself. A "
         "craftsperson who cannot read the tape cannot build to plan - so "
         "count it forward, count it back, read the clock three ways, "
         "until the numbers sit in the hand like a well-worn rule."),
     demo_kind="numbers", demo_data={
         "cardinals": ["one","two","three","four","five","six","seven","eight","nine","ten",
                       "eleven","twelve","thirteen","twenty","thirty","forty","fifty"],
         "ordinals": {"1":"first","2":"second","3":"third","4":"fourth","5":"fifth","20":"twentieth"},
         "days": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
         "times": [["4:00","four o'clock"],["4:30","half past four"],["5:15","a quarter past five"],["5:45","a quarter to six"]]}),
# ------------------------------------------------------------------ 9
dict(key="greetings", name="Greetings and Everyday Phrases", group="Foundations",
     ladder_rank=5, ladder_tier="foundations",
     description=(
         "Greetings open every conversation, and English has a greeting for "
         "every hour and every level of formality. Morning: 'Good "
         "morning.' Afternoon: 'Good afternoon.' Evening: 'Good evening.' "
         "Night is for leaving: 'Good night.' Anytime, casual: 'Hello.', "
         "'Hi.', 'Hey.' First meeting: 'Nice to meet you.' Polite reply: "
         "'Nice to meet you too.' Asking after someone: 'How are you?' - "
         "answer 'Fine, thanks. And you?' or 'Pretty good.' Leaving: "
         "'Goodbye.', 'Bye.', 'See you later.', 'Take care.' Politeness "
         "runs on five words: please, thank you, you're welcome, excuse "
         "me, I'm sorry. Requests soften with 'Could you...?' and 'Would "
         "you mind...?' Gratitude grows with 'Thank you very much.' and "
         "'I appreciate it.' Thirty phrases below, each with a usage note "
         "so you say the right one at the right moment."),
     how_it_works=(
         "Match the greeting to the hour: before noon 'Good morning', noon "
         "to evening 'Good afternoon', after dark 'Good evening', leaving "
         "at night 'Good night'. Practice the handshake pair: A: 'Hello, "
         "I'm Ana. Nice to meet you.' B: 'Nice to meet you too, Ana.' "
         "The 'How are you?' ritual: in English it is a greeting, not a "
         "medical exam - answer briefly and return it: 'Fine, thanks. And "
         "you?' Politeness in action: 'Excuse me, where is the station?' "
         "'Could you help me, please?' 'Thank you very much.' 'You're "
         "welcome.' Apology ladder: 'Excuse me' (getting attention or small "
         "bump), 'I'm sorry' (real mistake), 'I apologize' (formal). "
         "Learn these thirty as whole phrases - do not build them word by "
         "word at first; greetings are prefabricated parts, installed "
         "whole: Good morning. Good afternoon. Good evening. Good night. "
         "Hello. Hi. Hey. How are you? Fine, thanks. And you? Pretty good. "
         "Not bad. Nice to meet you. Nice to meet you too. Welcome. "
         "Goodbye. Bye. See you later. See you tomorrow. Take care. Have a "
         "nice day. Please. Thank you. Thank you very much. I appreciate "
         "it. You're welcome. No problem. Excuse me. I'm sorry. I "
         "apologize. Could you help me? Would you mind opening the window?"),
     key_points=[
         "Greetings follow the hour: morning, afternoon, evening; good night is for leaving.",
         "'How are you?' is a greeting; answer briefly and return it.",
         "Five politeness words: please, thank you, you're welcome, excuse me, I'm sorry.",
         "Excuse me = attention; I'm sorry = apology; I apologize = formal.",
         "Soften requests with 'Could you...?' and 'Would you mind...?'",
         "Learn greetings as whole prefabricated phrases.",
         "30 phrases below, each with a usage note."],
     requirements=["Practicing the handshake pair with a partner.",
                   "Using one new phrase in a real conversation each day."],
     standards=["Pragmatic usage per standard ESL references (Swan; Cambridge)."],
     citations=["Swan M. Practical English Usage. 4th ed. Oxford University Press; 2016."],
     sig_lens=(
         "The Signature learner treats greetings as the front door of the "
         "workshop: the first thing any visitor meets, so it must open "
         "smoothly every time. Thirty prefabricated doors, hung true - "
         "good morning for the early caller, excuse me for the crowded "
         "hallway, thank you very much for the helping hand. Install each "
         "one whole, test it in a real conversation, and the shop is open "
         "for business in any language."),
     demo_kind="phrases", demo_data={
         "pairs": [
             {"p":"Good morning","u":"before noon greeting"},
             {"p":"Good afternoon","u":"noon to evening greeting"},
             {"p":"Good evening","u":"after dark greeting"},
             {"p":"Good night","u":"leaving at night"},
             {"p":"Hello","u":"neutral anytime"},
             {"p":"Hi","u":"casual anytime"},
             {"p":"Nice to meet you","u":"first meeting"},
             {"p":"How are you?","u":"greeting ritual; answer briefly"},
             {"p":"Fine, thanks. And you?","u":"standard reply"},
             {"p":"Goodbye","u":"formal leaving"},
             {"p":"See you later","u":"casual leaving"},
             {"p":"Take care","u":"warm leaving"},
             {"p":"Please","u":"polite request word"},
             {"p":"Thank you","u":"gratitude"},
             {"p":"Thank you very much","u":"strong gratitude"},
             {"p":"You are welcome","u":"reply to thanks"},
             {"p":"Excuse me","u":"attention or small bump"},
             {"p":"I am sorry","u":"real apology"},
             {"p":"Could you help me?","u":"soft request"},
             {"p":"Have a nice day","u":"warm farewell"}]}),
# ------------------------------------------------------------------ 10
dict(key="grammar", name="Grammar Essentials", group="Foundations",
     ladder_rank=5, ladder_tier="foundations",
     description=(
         "Seven rules carry most of English grammar. Word order: Subject "
         "Verb Object - 'She reads books.' Time and place go at the end: "
         "'She reads books in the evening.' Number: singular vs plural, "
         "with the s/es/irregular rules from record 4. Articles: a/an for "
         "first mention ('I saw a dog'), the for known things ('The dog "
         "was big'), no article for plurals and uncountables in general "
         "('Dogs are loyal', 'Water is cold'). Negation: add not after "
         "auxiliaries - 'She does not read', 'I am not tired', 'They have "
         "not finished'. Questions: invert the auxiliary - 'Does she "
         "read?', 'Are you tired?', 'Have they finished?'; with no "
         "auxiliary, add do - 'Do you like tea?' Prepositions of place: in "
         "(inside), on (surface), at (point) - 'in the box', 'on the "
         "table', 'at the door'. There is / there are introduces new "
         "information: 'There is a cat.' 'There are two cats.' Each rule "
         "below comes with translated example sentences to copy and "
         "transform."),
     how_it_works=(
         "Take one base sentence and run it through all seven rules: base "
         "'She reads books.' Word order check: subject (she) verb (reads) "
         "object (books) - never 'She books reads.' Number: 'She reads a "
         "book.' vs 'She reads books.' Articles: 'I bought a car.' (first "
         "mention) then 'The car is red.' (now known). Negation: 'She does "
         "not read newspapers.' Question: 'Does she read newspapers?' "
         "Answer: 'Yes, she does.' / 'No, she doesn't.' Prepositions: "
         "'The book is in the bag.' 'The bag is on the chair.' 'She is at "
         "the door.' There is/are: 'There is a problem.' 'There are many "
         "problems.' Transform drills, each with the answer: 'He plays "
         "football.' to negative: 'He does not play football.' To "
         "question: 'Does he play football?' 'They are happy.' to "
         "negative: 'They are not happy.' To question: 'Are they happy?' "
         "'I have finished.' to negative: 'I have not finished.' To "
         "question: 'Have you finished?' Master these transforms and you "
         "can reshape any sentence on demand."),
     key_points=[
         "Word order: Subject Verb Object; time and place at the end.",
         "a/an = first mention; the = known; no article for general plurals.",
         "Negatives: add not after the auxiliary (does not, am not, have not).",
         "Questions: invert the auxiliary; add do when there is none.",
         "in = inside, on = surface, at = point.",
         "There is/there are introduces new information.",
         "Run one sentence through all seven transforms as a drill."],
     requirements=["Transform drills: sentence to negative to question, aloud.",
                   "Writing ten original sentences in SVO order."],
     standards=["Core grammar per Swan; Cambridge Grammar."],
     citations=["Swan M. Practical English Usage. 4th ed. Oxford University Press; 2016.",
                "Huddleston R, Pullum GK. The Cambridge Grammar of the English Language. 2002."],
     sig_lens=(
         "The Signature learner treats grammar as the frame of the "
         "workshop: seven steel rules, and every sentence hangs true on "
         "them. Subject-Verb-Object is the main beam - never cut it. "
         "Negation and questions are the hinges that let a sentence swing "
         "both ways. Build the frame once, square and level, and ten "
         "thousand sentences will hang on it without a wobble."),
     demo_kind="grammar", demo_data={
         "drills": [
             {"rule":"SVO order","from":"She books reads.","to":"She reads books."},
             {"rule":"article first mention","from":"I saw ___ dog.","to":"I saw a dog."},
             {"rule":"article known","from":"___ dog was big.","to":"The dog was big."},
             {"rule":"negation","from":"She reads newspapers.","to":"She does not read newspapers."},
             {"rule":"question","from":"She reads newspapers.","to":"Does she read newspapers?"},
             {"rule":"negation be","from":"They are happy.","to":"They are not happy."},
             {"rule":"question be","from":"They are happy.","to":"Are they happy?"},
             {"rule":"there is","from":"___ a problem.","to":"There is a problem."},
             {"rule":"preposition","from":"The book is ___ the bag.","to":"The book is in the bag."}]}),
# ------------------------------------------------------------------ 11
dict(key="home", name="Home and Family Sentences", group="Compounded",
     ladder_rank=6, ladder_tier="compounded",
     description=(
         "The home is the first world a learner can describe completely: "
         "rooms, furniture, and the people in them. Key rooms: kitchen, "
         "bedroom, bathroom, living room, dining room, garden, garage. Key "
         "furniture: table, chair, bed, sofa, lamp, shelf, cupboard, "
         "mirror. Family words: mother, father, parents, brother, sister, "
         "son, daughter, husband, wife, grandmother, grandfather, uncle, "
         "aunt, cousin, baby. Possession shows belonging: 'my mother's "
         "kitchen', 'their house'. Prepositions locate everything: 'in the "
         "kitchen', 'on the table', 'under the bed', 'behind the door', "
         "'next to the window'. Twenty sentences below walk through a "
         "whole house and the family inside it - read them in order and "
         "you have described a complete home."),
     how_it_works=(
         "Walk through your own home as you read: point at each thing and "
         "say its sentence. 'This is our house.' 'The living room is big "
         "and bright.' 'There is a sofa and two chairs in the living "
         "room.' 'The kitchen is next to the dining room.' 'My mother is "
         "cooking in the kitchen.' 'The bedroom has a large bed.' 'I sleep "
         "in my bedroom every night.' 'The bathroom is clean.' 'There is a "
         "mirror above the sink.' 'My father reads in the dining room.' "
         "'My sister does her homework at the table.' 'My brother plays in "
         "the garden.' 'Our grandmother lives with us.' 'The baby is "
         "sleeping in the small room.' 'The lamp is on the shelf.' 'The "
         "books are under the table.' 'Close the window, please.' 'Open "
         "the door for your aunt.' 'We eat dinner together at seven.' 'I "
         "love my family and my home.' Now describe YOUR home the same "
         "way, room by room, twenty sentences of your own."),
     key_points=[
         "Rooms: kitchen, bedroom, bathroom, living room, dining room, garden, garage.",
         "Family: parents, brother, sister, son, daughter, grandparents, uncle, aunt, cousin.",
         "Possession: my mother's kitchen, their house.",
         "Location prepositions: in, on, under, behind, next to.",
         "20 sentences below describe a complete home in order.",
         "Retell the set about your own home as the mastery drill."],
     requirements=["Walking through your real home, pointing and naming.",
                   "Writing 20 sentences about your own home and family."],
     standards=["Core domestic vocabulary per standard learner word lists."],
     citations=["Cambridge English. Vocabulary list guidance (CEFR A1-A2)."],
     sig_lens=(
         "The Signature learner treats the home as the first finished "
         "project: every room named, every beam and board - table, chair, "
         "lamp, shelf - set in its place, and the family named like the "
         "crew that raised it. Twenty sentences walk the whole house, "
         "foundation to roof. When you can describe your own home the "
         "same way, the first room of English is built."),
     demo_kind="sentences", demo_data={
         "sentences": [
             "This is our house.",
             "The living room is big and bright.",
             "There is a sofa and two chairs in the living room.",
             "The kitchen is next to the dining room.",
             "My mother is cooking in the kitchen.",
             "The bedroom has a large bed.",
             "I sleep in my bedroom every night.",
             "The bathroom is clean.",
             "There is a mirror above the sink.",
             "My father reads in the dining room.",
             "My sister does her homework at the table.",
             "My brother plays in the garden.",
             "Our grandmother lives with us.",
             "The baby is sleeping in the small room.",
             "The lamp is on the shelf.",
             "The books are under the table.",
             "Close the window, please.",
             "Open the door for your aunt.",
             "We eat dinner together at seven.",
             "I love my family and my home."]}),
# ------------------------------------------------------------------ 12
dict(key="food", name="Food and Cooking Sentences", group="Compounded",
     ladder_rank=6, ladder_tier="compounded",
     description=(
         "Food vocabulary is daily survival: meals (breakfast, lunch, "
         "dinner, snack), staples (bread, rice, eggs, milk, cheese, meat, "
         "fish, vegetables, fruit), flavors (sweet, sour, salty, spicy, "
         "bitter), and cooking actions (cut, chop, boil, fry, bake, grill, "
         "stir, mix, peel, taste). Countable vs uncountable matters at the "
         "table: 'an apple' but 'some rice'; 'a potato' but 'some soup'. "
         "Restaurant language is prefabricated: 'A table for two, please.' "
         "'Could I see the menu?' 'I would like the chicken.' 'The bill, "
         "please.' Quantities: 'a glass of water', 'a cup of tea', 'a "
         "piece of cake', 'a slice of bread'. Twenty sentences below cook "
         "a full day of meals and order a restaurant dinner."),
     how_it_works=(
         "Cook along with the sentences: name each action as you do it. "
         "'We eat breakfast at seven.' 'I like eggs and toast in the "
         "morning.' 'She drinks a glass of milk.' 'Cut the bread into "
         "slices.' 'Peel the potatoes first.' 'Boil the water for the "
         "rice.' 'Fry the eggs in a little oil.' 'Stir the soup slowly.' "
         "'The cake is baking in the oven.' 'Taste the sauce - is it too "
         "salty?' 'Lunch is usually rice and vegetables.' 'The apples are "
         "sweet this season.' 'I do not like spicy food.' 'Wash the fruit "
         "before you eat it.' 'Set the table, please.' 'A table for two, "
         "please.' 'Could I see the menu?' 'I would like the fish.' 'The "
         "food was delicious.' 'The bill, please.' Now cook one real meal "
         "narrating every step in English - that narration is the lesson."),
     key_points=[
         "Meals: breakfast, lunch, dinner, snack.",
         "Cooking verbs: cut, chop, boil, fry, bake, grill, stir, mix, peel, taste.",
         "Countable: an apple; uncountable: some rice, some soup.",
         "Quantities: a glass of, a cup of, a piece of, a slice of.",
         "Restaurant phrases are prefabricated: table for two, the menu, the bill.",
         "20 sentences below cook a full day and order dinner."],
     requirements=["Narrating one real cooking session in English.",
                   "Role-playing the restaurant scene with a partner."],
     standards=["Food vocabulary per standard learner word lists."],
     citations=["Cambridge English. Vocabulary list guidance (CEFR A1-A2)."],
     sig_lens=(
         "The Signature learner treats the kitchen as the second workshop: "
         "ten cooking verbs are ten tools - cut, chop, boil, fry, bake - "
         "and the meal is the project. Measure with a glass of and a piece "
         "of, season with sweet and salty, and serve the restaurant phrases "
         "like finished work to a customer: a table for two, the bill "
         "please. A meal cooked in English is a lesson you can taste."),
     demo_kind="sentences", demo_data={
         "sentences": [
             "We eat breakfast at seven.",
             "I like eggs and toast in the morning.",
             "She drinks a glass of milk.",
             "Cut the bread into slices.",
             "Peel the potatoes first.",
             "Boil the water for the rice.",
             "Fry the eggs in a little oil.",
             "Stir the soup slowly.",
             "The cake is baking in the oven.",
             "Taste the sauce - is it too salty?",
             "Lunch is usually rice and vegetables.",
             "The apples are sweet this season.",
             "I do not like spicy food.",
             "Wash the fruit before you eat it.",
             "Set the table, please.",
             "A table for two, please.",
             "Could I see the menu?",
             "I would like the fish.",
             "The food was delicious.",
             "The bill, please."]}),

]
