#!/usr/bin/env python3
"""Entries for the German Language databases (language project 2026-10-17, batch 2, roster rank 11).

Roster: language-german (rank 11) / language-german-signature (rank 12).
Slug verified free in manifest and in the db/ tree (zero language-german* hits).
ID prefixes JAH-LDEU- (public) and JAH-LDEUS- (signature) verified zero hits
in the manifest id_prefix values; shard-index scan for JAH-LDEU confirmed
zero hits before use. 68 titles (34 public + 34 Signature Edition) run through
code/dedupe_gate.py against the whole system before authoring: zero refusals.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-german             - The German Language Database
                                (public-harvest: real, fact-checked German
                                linguistics - every record carrying German
                                content with English translation and example
                                sentences, taught progressively along the
                                teaching ladder from overview to mastery
                                review; standard references the Duden, the
                                Rat fuer deutsche Rechtschreibung, the
                                Grimm Deutsches Woerterbuch, Ethnologue 28th
                                ed. 2025, the Goethe-Institut, and Hammer's
                                German Grammar and Usage 6th ed. 2017)
  language-german-signature   - The German Language Signature Database
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

Numerical/linguistic cores: all hand-authored 2026-10-17, machine-verified
by the demos (see demos_language_german.py): speaker-count math, alphabet
counts, gender/plural drills, conjugation checkers, number-to-word
converters, case-table audits, sentence-count verifiers, and quiz checkers.
Every demo prints its real computed values, asserts tight bounds (never
float exact-equality), and ends with the OK marker; the build
machine-executes all 68 demos.

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

CIT_ETHNO = ("Eberhard DM, Simons GF, Fennig CD, eds. Ethnologue: Languages "
             "of the World. 28th ed. Dallas: SIL International; 2025. "
             "(German: ISO 639-3 deu; about 95.2 million first-language "
             "speakers, about 135 million total speakers.)")
CIT_DUDEN = ("Dudenredaktion. Duden: Die deutsche Rechtschreibung. 28. Aufl. "
             "Berlin: Dudenverlag; 2020. (The standard reference dictionary "
             "and orthography guide for German, founded by Konrad Duden "
             "1880.)")
CIT_RAT = ("Rat fuer deutsche Rechtschreibung. (The Council for German "
           "Orthography, the official body regulating Standard German "
           "spelling since the 1996 orthography reform.)")
CIT_GRIMM = ("Grimm J, Grimm W. Deutsches Woerterbuch. Leipzig: Hirzel; "
             "1854-1961. (The monumental historical dictionary of German "
             "by the Brothers Grimm.)")
CIT_GOETHE = ("Goethe-Institut. (The German cultural institute promoting "
              "German language teaching worldwide; publisher of the "
              "standardized Deutsch-Test fuer Zuwanderer and Goethe-Zertifikat "
              "examinations.)")
CIT_HAMMER = ("Durrell M. Hammer's German Grammar and Usage. 6th ed. "
              "London: Routledge; 2017.")
CIT_CEFR = ("Council of Europe. Common European Framework of Reference for "
            "Languages: Learning, teaching, assessment. (German courses "
            "worldwide are graded A1 through C2.)")

ENTRIES = [
    {
        "key": "overview",
        "name": "German Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "German, called Deutsch by its speakers, is the most widely "
            "spoken native language in the European Union. Its codes are "
            "ISO 639-1 de and ISO 639-3 deu. It belongs to the Indo-European "
            "family, Germanic branch, West Germanic group - a sister of "
            "English and Dutch, descended from the High German consonant "
            "shift that changed p to pf, t to ss or z, and k to ch "
            "(compare English water with German Wasser, apple with Apfel). "
            "About 95.2 million people speak German as a native language "
            "and about 135 million speak it in total, counting "
            "second-language speakers. It is an official language in "
            "Germany (about 83 million inhabitants), Austria, Switzerland, "
            "Liechtenstein, Luxembourg, and the German-speaking community "
            "of Belgium, and one of the 24 official languages of the "
            "European Union. Dialects run from Low German in the north "
            "through Middle German to Upper German (including Bavarian and "
            "Alemannic) in the south, but everyone learns the shared "
            "standard, Standarddeutsch or Hochdeutsch, in school. National "
            "varieties exist: Swiss Standard German drops the letter sharp "
            "s and uses Helvetisms like Velo for bicycle; Austrian Standard "
            "German has its own vocabulary like Erdapfel for potato. The "
            "first German dictionary of note, the Brothers Grimm Deutsches "
            "Woerterbuch, began in 1854; Konrad Duden published the first "
            "unified spelling dictionary in 1880; and the 1996 orthography "
            "reform standardized spelling across the German-speaking "
            "countries. Example sentences: Deutsch ist die meistgesprochene "
            "Muttersprache in der EU. (German is the most widely spoken "
            "native language in the EU.) Deutschland, Oesterreich und die "
            "Schweiz sprechen Deutsch. (Germany, Austria, and Switzerland "
            "speak German.) Ich lerne Deutsch jeden Tag. (I study German "
            "every day.)"
        ),
        "how_it_works": (
            "German works as an inflected Germanic language: nouns carry "
            "gender (masculine, feminine, neuter) and decline through four "
            "cases, verbs conjugate for person and tense, and the "
            "characteristic sentence rule is verb-second in main clauses "
            "with the verb pushed to the end in subordinate clauses. A "
            "beginner sentence looks like English: Ich lerne Deutsch. (I "
            "learn German.) German compounds freely: Haustuerschluessel is "
            "Haus plus Tuer plus Schluessel - house door key - which is "
            "why German words can grow so long. Nouns are always "
            "capitalized, a memory aid the learner should use from day "
            "one. Questions flip the verb to the front: Lernst du Deutsch? "
            "(Are you learning German?) Negation uses nicht or kein: Ich "
            "lerne kein Franzoesisch. (I am learning no French.) "
            "Everything in this database builds on these mechanics: the "
            "overview first, then the script, then the sounds, then the "
            "words, then the sentences that carry them."
        ),
        "key_points": [
            "German (Deutsch, ISO de/deu) is an Indo-European West Germanic language with about 95.2 million native speakers and about 135 million total speakers.",
            "It is official in Germany, Austria, Switzerland, Liechtenstein, Luxembourg, and Belgium's German-speaking community, and is the EU's most spoken native language.",
            "The High German consonant shift separates German from English: English water, German Wasser; English apple, German Apfel.",
            "Nouns have three genders and four cases; main clauses put the conjugated verb second; subordinate clauses push it to the end.",
            "Dialects vary north to south (Low, Middle, Upper German), but Standarddeutsch (Hochdeutsch) is shared; Swiss and Austrian standard varieties have their own words and spellings.",
        ],
        "requirements": [
            "Know the names: Deutsch, ISO codes de (639-1) and deu (639-3), Indo-European > Germanic > West Germanic.",
            "Know the scale: about 95.2 million native speakers, about 135 million total, official in six countries.",
            "Read and write the three example sentences with their English translations from memory.",
            "Explain the High German consonant shift with two English-German word pairs.",
            "Name the three noun genders and the four cases, and explain verb-second order in one sentence.",
        ],
        "standards": [
            "Speaker figures follow Ethnologue 28th ed. 2025.",
            "Language-family classification follows the standard Germanic subgrouping used by the Duden.",
            "ISO 639-1 de and ISO 639-3 deu are the registered identifiers for German.",
        ],
        "citations": [CIT_ETHNO, CIT_DUDEN, CIT_GOETHE],
        "sig_lens": (
            "The Signature read: German is a forge-tongue - a language that "
            "stamps every noun with a capital letter like a seal on steel, "
            "and welds words into compounds the way a smith welds parts. "
            "Where public linguistics counts ninety-five million speakers, "
            "the Signature Word Method counts ninety-five million "
            "witnesses that meaning is engineered, not guessed."
        ),
    },
    {
        "key": "writing",
        "name": "German Writing System and Alphabet",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "German is written left to right in the Latin script. The "
            "alphabet has the 26 standard letters A B C D E F G H I J K L "
            "M N O P Q R S T U V W X Y Z, plus the three umlaut letters Ae "
            "Oe Ue and the sharp s, the Eszett. Transliteration: Ae = ae, "
            "Oe = oe, Ue = ue, Eszett = ss. The umlauts can always be "
            "written as ae, oe, ue when the dots are unavailable - Maedchen "
            "for Maedchen is correct spelling in crosswords, telegrams, "
            "and URLs. The sharp s only ever appears lowercase; in "
            "all-caps writing it becomes SS (STRASSE for Strasse). "
            "Switzerland and Liechtenstein do not use the sharp s at all: "
            "Swiss German writes Strasse, never Strasse with the sharp s. "
            "Nouns are ALWAYS capitalized: der Hund, die Katze, das Haus - "
            "this rule alone makes German text easier to scan. "
            "Punctuation matches English closely: period, comma, question "
            "mark, exclamation mark. German quotation marks are "
            "Anfuehrungszeichen, low opening and high closing: Er sagte: "
            "Guten Tag. Numerals use Arabic digits: 0 1 2 3 4 5 6 7 8 9. "
            "The decimal comma replaces the English decimal point: 3,14 is "
            "three point one four; the thousands separator is a dot or a "
            "space: 1.000 or 1 000 is one thousand. Example sentences: Das "
            "Deutsche hat 26 Buchstaben plus Ae, Oe, Ue und Eszett. (German "
            "has 26 letters plus ae, oe, ue and sharp s.) Alle Nomen werden "
            "grossgeschrieben. (All nouns are capitalized.) In der Schweiz "
            "gibt es kein Eszett. (In Switzerland there is no sharp s.)"
        ),
        "how_it_works": (
            "The German writing system works almost phonetically: once the "
            "learner knows the sound of each letter and letter pair, most "
            "words can be read aloud correctly. Each of the 30 letters maps "
            "to a predictable sound, with the famous exception that "
            "vowels come in short-long pairs and the umlauts are distinct "
            "letters that sort as a, o, u in dictionaries but change "
            "meaning: schon (already) versus schoen (beautiful) differ only "
            "in the two dots. The Eszett is not a fancy B - it is a sharp "
            "s, and the rule is simple: after a long vowel or diphthong it "
            "is written with the sharp s (Strasse, gross), after a short "
            "vowel with double s (Wasser, Klasse). In Switzerland the sharp "
            "s is always double s. Because nouns are capitalized, a German "
            "sentence shows its skeleton at a glance: nouns stand tall, "
            "verbs hold the frame."
        ),
        "key_points": [
            "30 letters: the 26 Latin letters plus Ae, Oe, Ue and the sharp s Eszett; Swiss German drops the sharp s and writes ss.",
            "Umlauts can be written ae, oe, ue when dots are unavailable; the sharp s becomes SS in all-caps.",
            "All nouns are capitalized, always - der Hund, die Katze, das Haus.",
            "Numerals are Arabic; the decimal mark is a comma (3,14) and the thousands separator a dot (1.000).",
            "German quotation marks are low-high Anfuehrungszeichen: Er sagte: Guten Tag.",
        ],
        "requirements": [
            "Recite the 26 letters plus the four special letters with their English transliterations.",
            "Write each special letter three ways: with dots, as ae/oe/ue/ss, and in all-caps.",
            "Capitalize the nouns in five English sentences translated into German.",
            "Convert the numbers 3.5 and 2,000 into German notation.",
            "Explain in one sentence why Switzerland writes Strasse with double s.",
        ],
        "standards": [
            "Spelling follows the Duden 28th ed. 2020 and the Council for German Orthography.",
            "The 1996 orthography reform rules govern sharp-s versus double-s usage.",
            "Swiss spelling conventions follow the Swiss standard that omits the sharp s.",
        ],
        "citations": [CIT_DUDEN, CIT_RAT],
        "sig_lens": (
            "The Signature read: the German alphabet is a set of thirty "
            "stamps in the Signature forge - twenty-six common, four "
            "special. The capital letter on every noun is the Signature "
            "seal made public: importance marked at a glance, nothing "
            "hidden, everything labeled."
        ),
    },
    {
        "key": "pronunciation",
        "name": "German Pronunciation and Phonology",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "German pronunciation is regular: letters sound the way they "
            "look, far more than English. The vowel system has short and "
            "long pairs: a as in Vater (father), e as in Bett (bed) or "
            "long as in Beet (flower bed), i as in bitte (please) or long "
            "as in Liebe (love), o as in Gott (God) or long as in Brot "
            "(bread), u as in Mutter (mother) or long as in gut (good). "
            "The umlauts: Ae as in Maedchen (girl, like English bed), Oe "
            "as in Schoen (beautiful, lips rounded saying eh), Ue as in "
            "Tuer (door, lips rounded saying ee). The letter pair ie is "
            "always long i: Liebe, nie (never). The diphthongs: ei sounds "
            "like English my: mein (my), nein (no); au sounds like English "
            "house: Haus (house), Baum (tree); eu and Aeu sound like "
            "English boy: heute (today), Haeuser (houses). The consonants: "
            "w always sounds like English v: Wasser (water); v sounds like "
            "f: Vater (father); z sounds like ts: Zeit (time), Zug (train); "
            "j sounds like English y: ja (yes); sch is sh: Schule (school); "
            "st and sp at the start of a syllable are sht and shp: Stadt "
            "(city), sprechen (to speak). The ch has two sounds: soft like "
            "a hissed h after front vowels - ich (I), Maedchen - and hard "
            "like clearing the throat after back vowels - ach (oh), Buch "
            "(book). The r is usually rolled in the throat (uvular), not "
            "the tongue tip. Word stress falls on the first syllable of "
            "native words: WA-sser, MU-tter, SCHU-le; loanwords often "
            "stress the end: Ho-TEL, compu-TER. Spoken examples: Haus "
            "(house), Baum (tree), Schule (school), Bruder (brother), "
            "Wasser (water), Maedchen (girl), Sprache (language), ich (I), "
            "ach (oh), Zug (train), Zeit (time), Brot (bread), gross "
            "(big), klein (small), Danke (thank you), bitte (please)."
        ),
        "how_it_works": (
            "German phonology works as a near one-to-one mapping between "
            "letters and sounds, so reading aloud is a mechanical skill "
            "the learner can trust. The engine of the system is the "
            "short-long vowel pair: double the consonant after a vowel "
            "and the vowel is short (Bett), single consonant or an h and "
            "the vowel is long (Beet, gehen). The umlauts are front-rounded "
            "vowels - the learner rounds the lips and says the base vowel. "
            "The ch rule is positional, not random: front vowel before it "
            "(i, e, Ae, Oe, Ue, ie) gives the soft sound, back vowel "
            "(a, o, u, au) gives the throat sound. Final devoicing means "
            "b, d, g at the end of a syllable sound like p, t, k: Hund "
            "sounds like hunt, Tag like tak. Stress is weight-based: "
            "native words hammer the first syllable, which is why German "
            "sounds so rhythmic to English ears."
        ),
        "key_points": [
            "Vowels come in short-long pairs; double consonant means short vowel (Bett), single means long (Beet).",
            "The umlauts Ae Oe Ue are distinct letters that change meaning: schon (already) vs schoen (beautiful).",
            "Letter pairs: ie is long i; ei sounds like my; eu/Aeu like boy; au like house.",
            "W sounds like v, v like f, z like ts, j like y; st/sp at syllable start are sht/shp.",
            "The ch is soft after front vowels (ich) and throaty after back vowels (ach); final b, d, g devoice to p, t, k.",
            "Stress falls on the first syllable of native words; loanwords often stress the last.",
        ],
        "requirements": [
            "Pronounce the eight basic vowels plus the three umlauts and explain the short-long rule.",
            "Read aloud the 16 spoken example words and give each English translation.",
            "Explain the two ch sounds with two words each and state the positional rule.",
            "Transcribe w, v, z, j, sch, st, sp into their English sound equivalents.",
            "Mark the stressed syllable in Wasser, Mutter, Schule, Hotel, Computer.",
        ],
        "standards": [
            "Sound descriptions follow standard Hochdeutsch as codified in the Duden pronunciation dictionary.",
            "The ch allophone rule follows standard German phonology (palatal after front vowels, velar after back vowels).",
            "Final devoicing is a documented rule of Standard German phonology.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: German pronunciation is honest machinery - "
            "what you see is what you say, a covenant between letter and "
            "sound that English broke long ago. The Signature ear trusts "
            "the first syllable like a struck bell: the word announces "
            "itself before it explains itself."
        ),
    },
    {
        "key": "nouns1",
        "name": "Core German Nouns I: People, Places, Things",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential German nouns with gender, plural, and an "
            "example sentence each. 1. der Mann, die Maenner (man, men): "
            "Der Mann liest. (The man is reading.) 2. die Frau, die Frauen "
            "(woman, women): Die Frau arbeitet. (The woman is working.) 3. "
            "das Kind, die Kinder (child, children): Das Kind spielt. (The "
            "child is playing.) 4. der Vater, die Vaeter (father, fathers): "
            "Der Vater kocht. (The father is cooking.) 5. die Mutter, die "
            "Muetter (mother, mothers): Die Mutter lacht. (The mother is "
            "laughing.) 6. der Bruder, die Brueder (brother, brothers): "
            "Der Bruder hilft. (The brother is helping.) 7. die Schwester, "
            "die Schwestern (sister, sisters): Die Schwester singt. (The "
            "sister is singing.) 8. der Freund, die Freunde (friend, "
            "friends): Der Freund kommt. (The friend is coming.) 9. das "
            "Haus, die Haeuser (house, houses): Das Haus ist gross. (The "
            "house is big.) 10. die Wohnung, die Wohnungen (apartment, "
            "apartments): Die Wohnung ist hell. (The apartment is bright.) "
            "11. das Zimmer, die Zimmer (room, rooms): Das Zimmer ist "
            "klein. (The room is small.) 12. die Tuer, die Tueren (door, "
            "doors): Die Tuer ist offen. (The door is open.) 13. der Tisch, "
            "die Tische (table, tables): Der Tisch ist rund. (The table is "
            "round.) 14. der Stuhl, die Stuehle (chair, chairs): Der Stuhl "
            "ist bequem. (The chair is comfortable.) 15. das Bett, die "
            "Betten (bed, beds): Das Bett ist weich. (The bed is soft.) "
            "16. die Kueche, die Kuechen (kitchen, kitchens): Die Kueche "
            "ist sauber. (The kitchen is clean.) 17. das Essen, die Essen "
            "(meal, meals): Das Essen schmeckt. (The meal tastes good.) 18. "
            "das Wasser, die Waesser (water, waters): Das Wasser ist kalt. "
            "(The water is cold.) 19. der Kaffee, die Kaffees (coffee, "
            "coffees): Der Kaffee ist heiss. (The coffee is hot.) 20. die "
            "Stadt, die Staedte (city, cities): Die Stadt ist alt. (The "
            "city is old.) 21. das Dorf, die Doerfer (village, villages): "
            "Das Dorf ist ruhig. (The village is quiet.) 22. die Strasse, "
            "die Strassen (street, streets): Die Strasse ist lang. (The "
            "street is long.) 23. der Hund, die Hunde (dog, dogs): Der Hund "
            "bellt. (The dog is barking.) 24. die Katze, die Katzen (cat, "
            "cats): Die Katze schlaeft. (The cat is sleeping.) 25. das "
            "Auto, die Autos (car, cars): Das Auto ist schnell. (The car is "
            "fast.) Gender patterns to memorize: most nouns ending in -ung, "
            "-heit, -keit, -schaft, -tät, -tion, -ik are feminine; most "
            "ending in -chen, -lein are neuter; days, months, seasons, and "
            "most ending in -er are masculine. But gender must be learned "
            "with each noun: always learn der, die, or das together with "
            "the word."
        ),
        "how_it_works": (
            "German nouns work as gendered, capitalized building blocks: "
            "every noun carries one of three genders - der (masculine), "
            "die (feminine), das (neuter) - and the gender controls which "
            "article and adjective endings the noun takes in all four "
            "cases. The plural system has five main patterns: add -e (der "
            "Tisch, die Tische), add -en (die Frau, die Frauen), add -er "
            "with umlaut (das Haus, die Haeuser), add -s for loanwords (das "
            "Auto, die Autos), or change nothing (das Zimmer, die Zimmer). "
            "About half of all masculine and neuter nouns add -e; most "
            "feminine nouns add -en; -er plurals take umlaut on a, o, u. "
            "There is no single rule that predicts every plural, which is "
            "why the learner memorizes the plural with the noun: Wort, "
            "plural Woerter. Suffixes give strong hints - -ung, -heit, "
            "-keit, -schaft are always feminine; -chen and -lein always "
            "neuter - and the learner exploits every hint."
        ),
        "key_points": [
            "Every German noun has a gender (der/die/das) that must be learned with the word; gender drives articles and adjective endings.",
            "Nouns are always capitalized: der Hund, die Katze, das Haus.",
            "Five plural patterns: -e, -en, -er with umlaut, -s for loanwords, or no change.",
            "Suffix hints: -ung, -heit, -keit, -schaft, -tion are feminine; -chen, -lein are neuter; days, months, seasons are masculine.",
            "This record's 25 nouns cover people (8), home (8), food and drink (3), places (3), animals (2), and transport (1).",
        ],
        "requirements": [
            "Recite all 25 nouns with correct gender, plural, and English meaning.",
            "Write the 25 example sentences in German from the English translations.",
            "Sort the 25 nouns by plural pattern and count how many use each pattern.",
            "Apply the suffix rules to predict the gender of five new nouns ending in -ung, -chen, -heit, -schaft, -tion.",
            "Explain why gender must be memorized with the noun, in two sentences.",
        ],
        "standards": [
            "Gender and plural forms follow the Duden standard.",
            "Suffix-based gender rules follow the standard German grammar descriptions.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: a German noun is a signed ingot - gender "
            "the stamp, plural the edge, capitalization the hallmark. The "
            "learner who learns der, die, das with every word is signing "
            "each ingot as it enters the vault; the learner who skips "
            "gender is stacking unmarked metal."
        ),
    },
    {
        "key": "verbs1",
        "name": "Core German Verbs I: The 25 Essential Verbs",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential German verbs with an example sentence "
            "each. 1. sein (to be): Ich bin muede. (I am tired.) 2. haben "
            "(to have): Ich habe Zeit. (I have time.) 3. werden (to "
            "become): Ich werde Arzt. (I am becoming a doctor.) 4. koennen "
            "(can, to be able): Ich kann schwimmen. (I can swim.) 5. muessen "
            "(must, to have to): Ich muss gehen. (I must go.) 6. wollen (to "
            "want): Ich will Wasser. (I want water.) 7. sollen (should, to "
            "be supposed to): Ich soll arbeiten. (I am supposed to work.) "
            "8. duerfen (may, to be allowed): Ich darf bleiben. (I may "
            "stay.) 9. machen (to make, to do): Ich mache Hausaufgaben. (I "
            "do homework.) 10. gehen (to go): Ich gehe nach Hause. (I go "
            "home.) 11. kommen (to come): Ich komme spaeter. (I am coming "
            "later.) 12. sehen (to see): Ich sehe den Film. (I see the "
            "movie.) 13. sprechen (to speak): Ich spreche Deutsch. (I speak "
            "German.) 14. lernen (to learn): Ich lerne jeden Tag. (I learn "
            "every day.) 15. lesen (to read): Ich lese ein Buch. (I read a "
            "book.) 16. schreiben (to write): Ich schreibe einen Brief. (I "
            "write a letter.) 17. essen (to eat): Ich esse Brot. (I eat "
            "bread.) 18. trinken (to drink): Ich trinke Tee. (I drink tea.) "
            "19. schlafen (to sleep): Ich schlafe gut. (I sleep well.) 20. "
            "arbeiten (to work): Ich arbeite im Buero. (I work in the "
            "office.) 21. spielen (to play): Ich spiele Fussball. (I play "
            "soccer.) 22. fragen (to ask): Ich frage den Lehrer. (I ask "
            "the teacher.) 23. antworten (to answer): Ich antworte schnell. "
            "(I answer quickly.) 24. kaufen (to buy): Ich kaufe Brot. (I "
            "buy bread.) 25. verkaufen (to sell): Ich verkaufe das Auto. "
            "(I sell the car.) Present-tense endings for regular verbs: "
            "ich mache, du machst, er macht, wir machen, ihr macht, sie "
            "machen - the stem plus -e, -st, -t, -en, -t, -en. The three "
            "irregular giants - sein (bin, bist, ist, sind, seid, sind), "
            "haben (habe, hast, hat, haben, habt, haben), werden (werde, "
            "wirst, wird, werden, werdet, werden) - are memorized whole. "
            "The six modal verbs (koennen, muessen, wollen, sollen, "
            "duerfen, moegen) push the main verb to the end in its "
            "infinitive: Ich kann schwimmen."
        ),
        "how_it_works": (
            "German verbs work as stem-plus-ending machines: strip -en from "
            "the infinitive to find the stem (mach- from machen), then bolt "
            "on the personal endings -e, -st, -t, -en, -t, -en. The system "
            "has two irregularities the learner meets immediately: stem "
            "vowel changes in strong verbs (sprechen becomes du sprichst, "
            "er spricht; lesen becomes du liest; sehen becomes du siehst) "
            "and the three fully irregular giants sein, haben, werden that "
            "must be memorized as complete tables. Modal verbs are "
            "sentence architects: they take second position and send the "
            "dependent infinitive to the very end - Ich muss heute lange "
            "arbeiten. Separable verbs split the same way: anrufen (to "
            "call) becomes Ich rufe dich an. Conjugation is the skeleton "
            "key of German: once the endings are automatic, every new verb "
            "is just a new stem."
        ),
        "key_points": [
            "Regular present endings: -e, -st, -t, -en, -t, -en on the verb stem.",
            "Sein, haben, werden are fully irregular and memorized whole.",
            "Strong verbs change their stem vowel in du and er/sie/es: sprechen to sprichst/spricht.",
            "The six modal verbs (koennen, muessen, wollen, sollen, duerfen, moegen) send the main verb to the end as an infinitive.",
            "Separable verbs split: the prefix goes to the end - Ich rufe dich an (from anrufen).",
        ],
        "requirements": [
            "Conjugate machen, lernen, and spielen fully in the present tense.",
            "Conjugate sein, haben, and werden fully in the present tense from memory.",
            "Translate the 25 example sentences both directions.",
            "Build five modal-verb sentences with the infinitive correctly at the end.",
            "Explain the stem-vowel change rule with sprechen, lesen, and sehen.",
        ],
        "standards": [
            "Conjugation tables follow the Duden standard grammar.",
            "Modal verb inventory follows the standard six-verb classification.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: a German verb is a signed engine - the "
            "stem the block, the ending the piston, the modal the "
            "transmission that throws the infinitive to the rear. Sein, "
            "haben, werden are the three master engines every apprentice "
            "memorizes before touching any other machine."
        ),
    },
]

ENTRIES += [
    {
        "key": "adjectives",
        "name": "German Adjectives and Adverbs",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five adjectives and fifteen adverbs with example "
            "sentences. Adjectives: 1. gut (good): Das Essen ist gut. (The "
            "food is good.) 2. schlecht (bad): Das Wetter ist schlecht. "
            "(The weather is bad.) 3. gross (big): Das Haus ist gross. "
            "(The house is big.) 4. klein (small): Die Katze ist klein. "
            "(The cat is small.) 5. neu (new): Das Auto ist neu. (The car "
            "is new.) 6. alt (old): Der Mann ist alt. (The man is old.) 7. "
            "jung (young): Das Kind ist jung. (The child is young.) 8. "
            "schoen (beautiful): Die Blume ist schoen. (The flower is "
            "beautiful.) 9. haesslich (ugly): Das Gebaeude ist haesslich. "
            "(The building is ugly.) 10. schnell (fast): Der Zug ist "
            "schnell. (The train is fast.) 11. langsam (slow): Die "
            "Schnecke ist langsam. (The snail is slow.) 12. warm (warm): "
            "Die Suppe ist warm. (The soup is warm.) 13. kalt (cold): Das "
            "Wasser ist kalt. (The water is cold.) 14. heiss (hot): Der Tee "
            "ist heiss. (The tea is hot.) 15. hell (bright): Das Zimmer ist "
            "hell. (The room is bright.) 16. dunkel (dark): Die Nacht ist "
            "dunkel. (The night is dark.) 17. teuer (expensive): Das Hotel "
            "ist teuer. (The hotel is expensive.) 18. billig (cheap): Das "
            "Brot ist billig. (The bread is cheap.) 19. lang (long): Die "
            "Strasse ist lang. (The street is long.) 20. kurz (short): Der "
            "Film ist kurz. (The movie is short.) 21. breit (wide): Der "
            "Fluss ist breit. (The river is wide.) 22. hoch (high): Der "
            "Berg ist hoch. (The mountain is high.) 23. tief (deep): Der "
            "See ist tief. (The lake is deep.) 24. stark (strong): Der Mann "
            "ist stark. (The man is strong.) 25. schwach (weak): Das Signal "
            "ist schwach. (The signal is weak.) Adverbs: 1. sehr (very): "
            "Es ist sehr kalt. (It is very cold.) 2. viel (a lot): Er "
            "arbeitet viel. (He works a lot.) 3. wenig (little): Sie isst "
            "wenig. (She eats little.) 4. oft (often): Ich komme oft. (I "
            "come often.) 5. selten (rarely): Wir sehen uns selten. (We "
            "rarely see each other.) 6. immer (always): Er ist immer "
            "puenktlich. (He is always on time.) 7. nie (never): Ich rauche "
            "nie. (I never smoke.) 8. bald (soon): Wir sehen uns bald. (We "
            "will see each other soon.) 9. gern (gladly, liking): Ich trinke "
            "gern Tee. (I like drinking tea.) 10. heute (today): Heute ist "
            "Montag. (Today is Monday.) 11. morgen (tomorrow): Morgen komme "
            "ich. (Tomorrow I am coming.) 12. hier (here): Ich bin hier. "
            "(I am here.) 13. dort (there): Er ist dort. (He is there.) 14. "
            "draussen (outside): Die Kinder sind draussen. (The children "
            "are outside.) 15. drinnen (inside): Wir bleiben drinnen. (We "
            "stay inside.) Agreement rules: predicative adjectives take "
            "NO ending - Der Hund ist gross. Attributive adjectives "
            "inflect: ein grosser Hund (a big dog), der grosse Hund (the "
            "big dog), grosse Hunde (big dogs). Adverbs never inflect."
        ),
        "how_it_works": (
            "German adjectives work in two modes. Predicative mode - after "
            "sein, werden, bleiben - takes no ending at all: Der Kaffee "
            "ist heiss. Attributive mode - directly before the noun - "
            "inflects according to three declension tables (strong, weak, "
            "mixed), which is why learners meet adjective endings as a "
            "table to memorize, not a feeling to acquire. The good news: "
            "the endings are few and repetitive (-e, -en, -er, -es, -em), "
            "and the article usually already shows the case and gender, so "
            "the adjective just echoes it: der grosse Hund, einem grossen "
            "Hund. Adverbs are the simple sibling: they never change form, "
            "they just modify verbs, adjectives, or whole sentences, and "
            "the learner can use gern (gladly) to express liking where "
            "English needs a verb: Ich trinke gern Tee."
        ),
        "key_points": [
            "Predicative adjectives take no ending: Der Kaffee ist heiss.",
            "Attributive adjectives inflect: ein grosser Hund, der grosse Hund, grosse Hunde.",
            "Only five endings cycle through the tables: -e, -en, -er, -es, -em.",
            "Adverbs never inflect: sehr, oft, gern, heute, hier.",
            "The adverb gern expresses liking: Ich trinke gern Tee (I like drinking tea).",
        ],
        "requirements": [
            "Translate all 25 adjective and 15 adverb sentences both directions.",
            "Convert five predicative sentences into attributive form with correct endings.",
            "List the three adjective declension types and when each applies.",
            "Write five original sentences using gern, sehr, oft, nie, and bald.",
            "Explain why attributive adjectives need endings but predicative ones do not.",
        ],
        "standards": [
            "Adjective declension tables follow the Duden standard grammar.",
            "Example vocabulary follows standard Hochdeutsch usage.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: the German adjective is a signed label - "
            "blank on the shelf (predicative), stamped to the crate when "
            "it ships with the noun (attributive). The five endings are "
            "five stamps; the master stamper never grabs the wrong one "
            "because the article already told him which."
        ),
    },
    {
        "key": "pronouns",
        "name": "German Pronouns: Full Paradigms",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Personal pronouns, nominative: ich (I), du (you, informal "
            "singular), er (he), sie (she), es (it), wir (we), ihr (you, "
            "informal plural), sie (they), Sie (you, formal - always "
            "capitalized). Accusative: mich (me), dich (you), ihn (him), "
            "sie (her), es (it), uns (us), euch (you), sie (them), Sie "
            "(you formal). Dative: mir (to me), dir (to you), ihm (to him), "
            "ihr (to her), ihm (to it), uns (to us), euch (to you), ihnen "
            "(to them), Ihnen (to you formal). Example sentences: Ich sehe "
            "dich. (I see you.) Er hilft mir. (He helps me.) Sie gibt ihm "
            "das Buch. (She gives him the book.) Wir danken Ihnen. (We "
            "thank you, formal.) Possessive stems: mein (my), dein (your "
            "informal), sein (his/its), ihr (her/their), unser (our), euer "
            "(your informal plural), Ihr (your formal). They take adjective "
            "endings: mein Hund (my dog), meine Katze (my cat), mein Haus "
            "(my house), meine Freunde (my friends). Example: Das ist mein "
            "Bruder. (That is my brother.) Das ist deine Schwester. (That "
            "is your sister.) Demonstratives: dieser (this), diese (this "
            "feminine/plural), dieses (this neuter), jener (that). Example: "
            "Dieser Mann ist nett. (This man is nice.) Diese Frau ist "
            "nett. (This woman is nice.) Interrogatives: wer (who, "
            "nominative), wen (whom, accusative), wem (to whom, dative), "
            "wessen (whose, genitive), was (what). Example: Wer kommt? (Who "
            "is coming?) Wen siehst du? (Whom do you see?) Wem gehoert das "
            "Buch? (Whose is the book - to whom does the book belong?) "
            "Welcher, welche, welches (which): Welcher Film laeuft? (Which "
            "movie is playing?) Reflexive pronouns: mich, dich, sich, uns, "
            "euch, sich - Er waescht sich. (He washes himself.)"
        ),
        "how_it_works": (
            "German pronouns work as case-marked pointers: the same person "
            "changes form depending on the job in the sentence - ich sees, "
            "mich is seen, mir is given to. The dative is the indirect "
            "object case and appears constantly: helfen (to help), danken "
            "(to thank), gefallen (to please), and gehören (to belong to) "
            "all take the dative - Ich helfe dir, not dich. The "
            "formal-informal split is social machinery: du for friends, "
            "family, children, and peers; Sie for strangers, customers, "
            "and anyone owed respect; ihr addresses groups informally. "
            "Possessives behave exactly like adjectives with endings, so "
            "mein, dein, sein are one memorized stem each plus the "
            "adjective table. The interrogatives decline like the "
            "articles they replace: wer, wen, wem, wessen mirrors der, "
            "den, dem, des."
        ),
        "key_points": [
            "Nine personal pronouns: ich, du, er/sie/es, wir, ihr, sie, Sie - each with nominative, accusative, and dative forms.",
            "The dative marks the indirect object; verbs like helfen, danken, gefallen, gehoeren take the dative.",
            "Du is informal singular, ihr informal plural, Sie formal and always capitalized.",
            "Possessive stems (mein, dein, sein, ihr, unser, euer, Ihr) take adjective endings.",
            "Interrogatives decline: wer, wen, wem, wessen; welcher, welche, welches for which.",
            "Reflexive pronouns: mich, dich, sich, uns, euch, sich - Er waescht sich.",
        ],
        "requirements": [
            "Write the full personal pronoun table (nom/acc/dat) from memory.",
            "Translate ten sentences using dative verbs (helfen, danken, gefallen).",
            "Convert five du sentences to Sie and five Sie sentences to du.",
            "Decline mein Hund through all four cases in singular and plural.",
            "Ask and answer six questions using wer, was, wen, wem, wessen, welcher.",
        ],
        "standards": [
            "Pronoun paradigms follow the Duden standard grammar.",
            "The du/Sie distinction follows standard German sociolinguistic usage.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: German pronouns are signed pointers - "
            "each one stamped with its case so the sentence can never "
            "lose track of who acts and who receives. Du and Sie are the "
            "two seals of the social contract: one for the inner circle, "
            "one for the honored stranger."
        ),
    },
    {
        "key": "numbers",
        "name": "German Numbers, Time, and Dates",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Numbers 1 to 20: eins (1), zwei (2), drei (3), vier (4), fuenf "
            "(5), sechs (6), sieben (7), acht (8), neun (9), zehn (10), elf "
            "(11), zwoelf (12), dreizehn (13), vierzehn (14), fuenfzehn "
            "(15), sechzehn (16), siebzehn (17), achtzehn (18), neunzehn "
            "(19), zwanzig (20). Note the spelling drops: sechzehn not "
            "sechszehn, siebzehn not siebenzehn. Tens: zwanzig (20), "
            "dreissig (30 - note the ss, not z), vierzig (40), fuenfzig "
            "(50), sechzig (60), siebzig (70), achtzig (80), neunzig (90), "
            "hundert (100). Compound numbers put the ones first: "
            "einundzwanzig (21, literally one-and-twenty), zweiundzwanzig "
            "(22), fuenfunddreissig (35), neunundneunzig (99). Ordinals: "
            "der erste (1st), der zweite (2nd), der dritte (3rd), der vierte "
            "(4th), then -te to 19 and -ste after: der zwanzigste (20th). "
            "Days: Montag (Monday), Dienstag (Tuesday), Mittwoch "
            "(Wednesday, literally mid-week), Donnerstag (Thursday), "
            "Freitag (Friday), Samstag or Sonnabend (Saturday), Sonntag "
            "(Sunday). Months: Januar, Februar, Maerz, April, Mai, Juni, "
            "Juli, August, September, Oktober, November, Dezember. Seasons: "
            "der Fruehling (spring), der Sommer (summer), der Herbst "
            "(autumn), der Winter (winter). Clock time: Germans say halb "
            "drei for 2:30 (half to three, not half past two), viertel "
            "nach zwei for 2:15, viertel vor drei for 2:45, fuenf vor halb "
            "drei for 2:25. Official time uses the 24-hour clock: 14:30 is "
            "vierzehn Uhr dreissig. Example sentences: Es ist halb drei. "
            "(It is 2:30.) Heute ist Montag, der siebzehnte Oktober. (Today "
            "is Monday, October 17th.) Der Zug faehrt um acht Uhr. (The "
            "train leaves at eight o'clock.) Ich habe am dritten Mai "
            "Geburtstag. (My birthday is on May 3rd.) Ein Kilo kostet zwei "
            "Euro fuenfzig. (A kilo costs two euros fifty.)"
        ),
        "how_it_works": (
            "German numbers work as a ones-first construction set: from 21 "
            "up, the unit is spoken before the ten, joined by und - "
            "einundzwanzig, literally one-and-twenty - a direct inheritance "
            "from the old Germanic counting that English abandoned. The "
            "irregulars are few and fixed: elf, zwoelf, sechzehn, siebzehn, "
            "dreissig. Ordinals are adjectives: add -te up to 19, -ste "
            "from 20 on, and decline them like any attributive adjective - "
            "der erste Mai, am dritten Mai. Time-telling is the famous "
            "trap: halb drei means half an hour TOWARD three (2:30), and "
            "viertel vor/nach anchor to the coming or past hour. Dates are "
            "spoken day-month-year: der siebzehnte Oktober 2026. Money "
            "reads like the clock: zwei Euro fuenfzig. Once the learner "
            "internalizes ones-first and halb-means-toward, the whole "
            "system clicks."
        ),
        "key_points": [
            "1-20 memorized whole; note sechzehn, siebzehn, dreissig as the irregular spellings.",
            "From 21, ones come first: einundzwanzig, fuenfunddreissig, neunundneunzig.",
            "Ordinals: erste, zweite, dritte, then -te to 19, -ste from 20; they decline as adjectives.",
            "Seven days (Montag-Sonntag), twelve months, four seasons - all masculine except die Woche-related nouns.",
            "Halb drei is 2:30 (half toward three); official time uses the 24-hour clock.",
            "Dates are day-month-year: der siebzehnte Oktober; money reads like time: zwei Euro fuenfzig.",
        ],
        "requirements": [
            "Count 1-100 aloud in German without hesitation.",
            "Write the numbers 21, 35, 47, 68, 99 as German words.",
            "Give the ordinals 1st-10th and 20th with correct endings.",
            "Tell the time for 2:15, 2:30, 2:45, 8:05, 14:30 in German.",
            "Write five dates and five prices in German.",
        ],
        "standards": [
            "Number words follow Duden standard spelling (sechzehn, siebzehn, dreissig).",
            "Time expressions follow standard German usage including halb/viertel conventions.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: German numbers are signed measures - the "
            "ones march first like a vanguard, the tens follow like the "
            "main column. Halb drei is the Signature clock: it does not "
            "tell where you are, it tells where you are GOING."
        ),
    },
    {
        "key": "greetings",
        "name": "German Greetings and Everyday Phrases",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Thirty greetings, farewells, and politeness phrases with "
            "usage notes. 1. Guten Morgen! (Good morning! - until about "
            "11.) 2. Guten Tag! (Good day! - the standard daytime greeting.) "
            "3. Guten Abend! (Good evening! - after about 18:00.) 4. Gute "
            "Nacht! (Good night! - only when parting for sleep.) 5. Hallo! "
            "(Hello! - universal, informal to neutral.) 6. Hi! (Hi! - very "
            "informal, young.) 7. Servus! (Hello/bye! - Bavaria and "
            "Austria.) 8. Gruess Gott! (Hello! - southern Germany and "
            "Austria, traditional.) 9. Moin! (Hello! - northern Germany, "
            "any time of day.) 10. Willkommen! (Welcome!) 11. Tschuess! "
            "(Bye! - informal standard.) 12. Tschau! / Ciao! (Bye! - casual, "
            "borrowed.) 13. Auf Wiedersehen! (Goodbye! - formal, until we "
            "meet again.) 14. Bis spaeter! (See you later!) 15. Bis bald! "
            "(See you soon!) 16. Bis morgen! (See you tomorrow!) 17. Mach's "
            "gut! (Take care! - informal.) 18. Schoenen Tag noch! (Have a "
            "nice day! - when parting.) 19. Schoenes Wochenende! (Have a "
            "nice weekend!) 20. Wie geht es Ihnen? (How are you? - formal.) "
            "21. Wie geht's? (How is it going? - informal.) 22. Wie geht es "
            "dir? (How are you? - informal singular.) 23. Mir geht es gut, "
            "danke. (I am well, thanks.) 24. Und Ihnen? / Und dir? (And "
            "you? - formal/informal.) 25. Freut mich! (Nice to meet you!) "
            "26. Danke! / Dankeschoen! (Thanks! / Thank you very much!) 27. "
            "Bitte! (Please! / You are welcome! - also used when handing "
            "something over.) 28. Entschuldigung! (Excuse me! / Sorry! - "
            "for getting attention or small faults.) 29. Es tut mir leid. "
            "(I am sorry. - for real faults.) 30. Kein Problem! (No "
            "problem!) Usage: greet shop staff with Guten Tag on entry; "
            "answer Wie geht's with Gut, danke, never a life story; say "
            "Prost or Zum Wohl when clinking glasses; say Gesundheit after "
            "a sneeze."
        ),
        "how_it_works": (
            "German greetings work as time- and region-coded rituals: the "
            "day is sliced into Morgen, Tag, Abend, and Nacht, each with "
            "its own Guten, and the regions stamp their own hello - Moin "
            "in the north, Servus and Gruess Gott in the south - so the "
            "traveler reads the greeting like a license plate. The "
            "formality engine runs underneath: Guten Tag and Auf "
            "Wiedersehen are neutral-formal; Hallo and Tschuess are "
            "informal-neutral; Hi, Servus, and Mach's gut are inner "
            "circle. Wie geht es Ihnen versus Wie geht's is the du/Sie "
            "choice in question form. Bitte is the hardest-working word "
            "in German - please, you're welcome, here you are, pardon - "
            "and Entschuldigung is the social oil for bumping, asking, "
            "and interrupting. The learner who greets on entry, thanks on "
            "exit, and answers Wie geht's with Gut, danke is already "
            "functioning in German society."
        ),
        "key_points": [
            "Time-coded greetings: Guten Morgen, Guten Tag, Guten Abend, Gute Nacht (only for parting to sleep).",
            "Regional greetings: Moin (north), Servus and Gruess Gott (south/Austria).",
            "Formality ladder: Auf Wiedersehen (formal) - Tschuess (neutral) - Mach's gut (informal).",
            "Wie geht es Ihnen (formal) vs Wie geht's / Wie geht es dir (informal).",
            "Bitte does four jobs: please, you're welcome, here you are, pardon.",
            "Answer Wie geht's with Gut, danke - never a life story; say Gesundheit after sneezes, Prost when toasting.",
        ],
        "requirements": [
            "Recite all 30 phrases with translations and say when each is used.",
            "Role-play: greet a shopkeeper at 9:00, 14:00, 20:00, and when leaving for the night.",
            "Convert five formal phrases to their informal equivalents and back.",
            "Write a three-line dialogue: greeting, how-are-you, farewell.",
            "Explain the four jobs of bitte with one example each.",
        ],
        "standards": [
            "Greeting usage follows standard German sociolinguistic conventions.",
            "Regional greetings follow documented northern and southern usage.",
        ],
        "citations": [CIT_GOETHE, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: every German greeting is a signed "
            "handshake - time-stamped (Morgen, Tag, Abend), region-stamped "
            "(Moin, Servus), and respect-stamped (Ihnen, dir). The "
            "Signature traveler reads the stamp before extending the hand."
        ),
    },
    {
        "key": "grammar",
        "name": "German Grammar Essentials",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Word order: German main clauses are verb-second (V2) - the "
            "conjugated verb is always the second element: Ich lerne heute "
            "Deutsch. Heute lerne ich Deutsch. (Today I am learning "
            "German.) In yes/no questions the verb moves to first "
            "position: Lernst du Deutsch? (Are you learning German?) In "
            "subordinate clauses the conjugated verb goes last: Ich weiss, "
            "dass du Deutsch lernst. (I know that you are learning German.) "
            "Gender: three genders - der Mann (masculine), die Frau "
            "(feminine), das Kind (neuter). Every noun is learned with its "
            "article. Number: singular and plural - der Hund, die Hunde. "
            "Cases: nominative (subject: Der Mann liest.), accusative "
            "(direct object: Ich sehe den Mann.), dative (indirect object: "
            "Ich gebe dem Mann das Buch. - I give the man the book.), "
            "genitive (possession: Das ist das Auto des Mannes. - That is "
            "the man's car.) Articles: definite der/die/das, die (plural); "
            "indefinite ein (masculine/neuter), eine (feminine); negative "
            "kein/keine. Example: Ein Mann liest ein Buch. (A man reads a "
            "book.) Der Mann liest das Buch. (The man reads the book.) "
            "Negation: nicht negates verbs and adjectives - Ich lerne "
            "nicht. (I am not learning.) Das ist nicht gut. (That is not "
            "good.); kein negates nouns with indefinite or no article - "
            "Ich habe kein Geld. (I have no money.) Er ist kein Lehrer. "
            "(He is not a teacher.) Question formation: W-questions start "
            "with the question word in first position, verb second - Was "
            "machst du? (What are you doing?) Wo wohnst du? (Where do you "
            "live?) Warum lernst du Deutsch? (Why are you learning "
            "German?) - and yes/no questions invert verb and subject: "
            "Kommst du mit? (Are you coming along?) Separable verbs: the "
            "prefix detaches in main clauses - anrufen becomes Ich rufe "
            "dich morgen an. (I will call you tomorrow.)"
        ),
        "how_it_works": (
            "German grammar works as a case-and-position machine. The four "
            "cases label every noun phrase with its job: nominative acts, "
            "accusative is acted upon, dative receives, genitive owns. The "
            "articles carry most of the case marking - den, dem, des are "
            "the accusative, dative, and genitive of der - which is why "
            "learners drill article tables before anything else. Position "
            "is the second engine: the conjugated verb anchors second "
            "place in statements, first place in yes/no questions, and "
            "last place after subordinating conjunctions like dass, weil, "
            "wenn, and ob. Negation is a fork: nicht for verbs and "
            "adjectives, kein for nouns. Separable verbs are the "
            "signature move of German syntax - the prefix flies to the "
            "end, bracketing the sentence: Ich stehe um sieben Uhr auf. "
            "Master V2, the four cases, nicht/kein, and separable verbs, "
            "and the grammar of German is fundamentally unlocked."
        ),
        "key_points": [
            "Verb-second in main clauses; verb-first in yes/no questions; verb-last in subordinate clauses.",
            "Four cases label noun jobs: nominative (subject), accusative (direct object), dative (indirect object), genitive (possession).",
            "Articles carry case marking: der/den/dem/des for masculine.",
            "Nicht negates verbs and adjectives; kein negates nouns.",
            "W-questions: question word first, verb second - Was machst du?",
            "Separable verbs split the prefix to the end: Ich rufe dich an.",
        ],
        "requirements": [
            "Draw the masculine article table across all four cases from memory.",
            "Transform five statements into yes/no questions and five into W-questions.",
            "Mark the case of every noun phrase in five sentences.",
            "Write five nicht and five kein negations.",
            "Rewrite five subordinate clauses with the verb correctly at the end.",
        ],
        "standards": [
            "Case and word-order rules follow the Duden standard grammar.",
            "Article paradigms follow standard Hochdeutsch declension.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: German grammar is a signed machine shop - "
            "four cases are four workstations, verb-second the conveyor "
            "that never misplaces the engine, separable verbs the "
            "two-handed press that stamps the sentence at both ends. The "
            "Signature grammarian does not memorize rules; he learns the "
            "floor plan."
        ),
    },
]

ENTRIES += [
    {
        "key": "home",
        "name": "Home and Family Sentences",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about house, rooms, furniture, and family. "
            "1. Wir wohnen in einem grossen Haus. (We live in a big "
            "house.) 2. Die Kueche ist neben dem Wohnzimmer. (The kitchen "
            "is next to the living room.) 3. Mein Zimmer ist oben. (My "
            "room is upstairs.) 4. Das Badezimmer hat eine Dusche. (The "
            "bathroom has a shower.) 5. Der Tisch steht in der Mitte. (The "
            "table stands in the middle.) 6. Die Stuehle sind um den Tisch. "
            "(The chairs are around the table.) 7. Das Bett ist sehr "
            "bequem. (The bed is very comfortable.) 8. Der Schrank ist "
            "voll. (The wardrobe is full.) 9. Das Fenster ist offen. (The "
            "window is open.) 10. Die Lampe steht auf dem Schreibtisch. "
            "(The lamp stands on the desk.) 11. Meine Familie ist gross. "
            "(My family is big.) 12. Mein Vater arbeitet als Ingenieur. "
            "(My father works as an engineer.) 13. Meine Mutter ist "
            "Lehrerin. (My mother is a teacher.) 14. Ich habe zwei Brueder "
            "und eine Schwester. (I have two brothers and one sister.) 15. "
            "Mein Grossvater erzaehlt Geschichten. (My grandfather tells "
            "stories.) 16. Meine Grossmutter backt Kuchen. (My grandmother "
            "bakes cake.) 17. Unser Hund schlaeft im Flur. (Our dog sleeps "
            "in the hallway.) 18. Die Katze sitzt auf dem Sofa. (The cat "
            "sits on the sofa.) 19. Wir essen zusammen im Esszimmer. (We "
            "eat together in the dining room.) 20. Zu Hause fuehle ich mich "
            "wohl. (At home I feel comfortable.)"
        ),
        "how_it_works": (
            "Home-and-family sentences work as the learner's first "
            "compounded territory: rooms take prepositions with the "
            "dative for location (in der Kueche, auf dem Tisch, neben dem "
            "Wohnzimmer), family members introduce possessives (mein "
            "Vater, meine Mutter, unser Hund), and everyday verbs - wohnen, "
            "stehen, sitzen, liegen, haengen - describe position the way "
            "English uses is. The dative of location is the quiet engine "
            "of this domain: in, an, auf, hinter, neben, unter, ueber, vor, "
            "zwischen plus dative answer wo (where), plus accusative "
            "answer wohin (where to). Family vocabulary compounds "
            "naturally: Grossvater, Grossmutter, and the learner sees the "
            "German compounding instinct in action."
        ),
        "key_points": [
            "Location prepositions take the dative: in der Kueche, auf dem Tisch, neben dem Wohnzimmer.",
            "Position verbs: stehen (standing), sitzen (sitting), liegen (lying), haengen (hanging).",
            "Family possessives: mein Vater, meine Mutter, unser Hund, meine Grosseltern.",
            "Wo (where) takes dative; wohin (where to) takes accusative.",
            "Twenty sentences covering rooms, furniture, family members, and pets.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions from memory.",
            "Describe your own home in ten German sentences using location prepositions.",
            "List eight family members with possessives and an example sentence each.",
            "Explain the wo/wohin distinction with two sentence pairs.",
            "Conjugate stehen, sitzen, liegen in the present tense.",
        ],
        "standards": [
            "Preposition-case government follows the Duden standard grammar.",
            "Family vocabulary follows standard Hochdeutsch usage.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: the home sentences are the signed "
            "foundation course - every room a chamber of the vault, every "
            "family member a witness. The dative of location is the "
            "Signature anchor: where a thing RESTS is stamped in the "
            "dative, where it MOVES in the accusative."
        ),
    },
    {
        "key": "food",
        "name": "Food and Cooking Sentences",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about meals, ingredients, cooking, and "
            "restaurants. 1. Das Fruehstueck ist die wichtigste Mahlzeit. "
            "(Breakfast is the most important meal.) 2. Ich esse gern Brot "
            "mit Kaese. (I like eating bread with cheese.) 3. Zum "
            "Mittagessen gibt es Suppe. (For lunch there is soup.) 4. Wir "
            "kochen heute Abendessen. (We are cooking dinner today.) 5. Die "
            "Kartoffeln sind noch nicht gar. (The potatoes are not done "
            "yet.) 6. Schneide die Zwiebeln klein. (Cut the onions small.) "
            "7. Das Wasser kocht schon. (The water is already boiling.) 8. "
            "Ich brate das Fleisch in der Pfanne. (I fry the meat in the "
            "pan.) 9. Der Kuchen backt im Ofen. (The cake is baking in the "
            "oven.) 10. Schmeckt es dir? (Does it taste good to you?) 11. "
            "Ja, es schmeckt sehr gut. (Yes, it tastes very good.) 12. Das "
            "Rezept braucht drei Eier. (The recipe needs three eggs.) 13. "
            "Ich kaufe frisches Gemuese auf dem Markt. (I buy fresh "
            "vegetables at the market.) 14. Die Aepfel sind reif. (The "
            "apples are ripe.) 15. Moechtest du einen Kaffee? (Would you "
            "like a coffee?) 16. Die Rechnung, bitte. (The check, please.) "
            "17. Das Restaurant ist sehr beliebt. (The restaurant is very "
            "popular.) 18. Ich haette gern die Speisekarte. (I would like "
            "the menu.) 19. Ist dieser Tisch frei? (Is this table free?) "
            "20. Guten Appetit! (Enjoy your meal!)"
        ),
        "how_it_works": (
            "Food sentences work as the learner's kitchen laboratory for "
            "the accusative: ingredients are direct objects - Ich schneide "
            "die Zwiebeln, Ich brate das Fleisch - so every recipe is "
            "accusative drill disguised as dinner. The dative appears in "
            "taste judgments: Schmeckt es dir? (the eater is the dative "
            "receiver of the taste). Restaurant German runs on the "
            "Konjunktiv II politeness engine: Ich haette gern (I would "
            "gladly have), Moechtest du (would you like), and the magic "
            "word bitte. Measurements stay simple: ein Kilo, drei Eier, "
            "zwei Euro fuenfzig. Guten Appetit is said by everyone at the "
            "table before eating - it is not optional in German culture."
        ),
        "key_points": [
            "Cooking verbs take the accusative: Ich schneide die Zwiebeln, Ich brate das Fleisch.",
            "Taste judgments use the dative: Schmeckt es dir?",
            "Restaurant politeness runs on haette gern and Moechtest du.",
            "Measurements: ein Kilo, drei Eier, zwei Euro fuenfzig.",
            "Guten Appetit is said by all before eating; Die Rechnung, bitte asks for the check.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Write a five-step recipe in German using imperative or present-tense verbs.",
            "Order a full three-course meal in German: greeting, drinks, starter, main, dessert, check.",
            "Explain why the eater is dative in Schmeckt es dir.",
            "List ten ingredients with gender and plural.",
        ],
        "standards": [
            "Culinary and restaurant vocabulary follows standard Hochdeutsch usage.",
            "Politeness forms follow standard German service conventions.",
        ],
        "citations": [CIT_DUDEN, CIT_GOETHE],
        "sig_lens": (
            "The Signature read: the kitchen is the signed laboratory - "
            "every ingredient an accusative test subject, every taste a "
            "dative verdict. Ich haette gern is the Signature request: "
            "politeness forged in the conditional, never demanded, always "
            "earned."
        ),
    },
    {
        "key": "travel",
        "name": "Travel and Directions Sentences",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about transport, directions, tickets, and "
            "lodging. 1. Wo ist der Bahnhof? (Where is the train station?) "
            "2. Gehen Sie geradeaus. (Go straight ahead.) 3. Biegen Sie "
            "links ab. (Turn left.) 4. Biegen Sie rechts ab. (Turn right.) "
            "5. Die Bank ist gegenueber der Post. (The bank is across from "
            "the post office.) 6. Ist es weit von hier? (Is it far from "
            "here?) 7. Nein, es ist ganz in der Naehe. (No, it is quite "
            "nearby.) 8. Eine Fahrkarte nach Berlin, bitte. (One ticket to "
            "Berlin, please.) 9. Wann faehrt der naechste Zug? (When does "
            "the next train leave?) 10. Der Zug hat Verspaetung. (The "
            "train is delayed.) 11. Von welchem Gleis faehrt er ab? (From "
            "which platform does it depart?) 12. Ich brauche ein Taxi zum "
            "Flughafen. (I need a taxi to the airport.) 13. Wie viel kostet "
            "die Fahrt? (How much is the ride?) 14. Halten Sie bitte hier. "
            "(Please stop here.) 15. Haben Sie ein Zimmer frei? (Do you "
            "have a room available?) 16. Das Zimmer kostet achtzig Euro "
            "pro Nacht. (The room costs eighty euros per night.) 17. Ist "
            "das Fruehstueck inklusive? (Is breakfast included?) 18. Wo kann "
            "ich ein Auto mieten? (Where can I rent a car?) 19. Ich habe "
            "mich verfahren. (I took a wrong turn - I am lost driving.) "
            "20. Koennen Sie mir das auf dem Stadtplan zeigen? (Can you "
            "show me that on the city map?)"
        ),
        "how_it_works": (
            "Travel sentences work as the learner's survival kit, built on "
            "three engines: direction prepositions with the dative of "
            "location (gegenueber der Post, in der Naehe, von hier), "
            "separable verbs of motion (abfahren, abbiegen, ankommen, "
            "umsteigen), and the formal Sie imperative for asking "
            "strangers (Gehen Sie, Biegen Sie, Halten Sie). Tickets and "
            "times run on the accusative of extent: eine Fahrkarte nach "
            "Berlin, achtzig Euro pro Nacht. The two motion verbs divide "
            "the work: fahren for vehicles, gehen for feet - Ich gehe zum "
            "Bahnhof, Ich fahre nach Berlin. Reflexive verbs appear in "
            "travel trouble: sich verfahren (to take a wrong turn), sich "
            "verspaeten (to be delayed). The traveler who can ask Wo ist, "
            "understand links/rechts/geradeaus, and buy a Fahrkarte can "
            "move through any German city."
        ),
        "key_points": [
            "Direction engine: Wo ist, Gehen Sie geradeaus, Biegen Sie links/rechts ab.",
            "Location prepositions take the dative: gegenueber der Post, in der Naehe.",
            "Separable motion verbs: abfahren, abbiegen, ankommen, umsteigen.",
            "Fahren is for vehicles, gehen is for feet.",
            "Ticket and price language: Eine Fahrkarte nach Berlin, bitte; achtzig Euro pro Nacht.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Give walking directions from a station to a hotel in six German sentences.",
            "Buy a train ticket and ask about platform and delays in a role-play.",
            "Conjugate abfahren and ankommen in the present tense.",
            "Explain the gehen/fahren distinction with three sentence pairs.",
        ],
        "standards": [
            "Transport vocabulary follows standard Hochdeutsch usage.",
            "Formal imperatives follow standard Sie-address conventions.",
        ],
        "citations": [CIT_DUDEN, CIT_GOETHE],
        "sig_lens": (
            "The Signature read: travel German is the signed compass - "
            "every direction a stamped instruction, every ticket a sealed "
            "contract of motion. Links, rechts, geradeaus: three stamps, "
            "and the Signature traveler never needs a fourth."
        ),
    },
    {
        "key": "work",
        "name": "Work and School Sentences",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about jobs, the office, the classroom, and "
            "learning. 1. Ich arbeite als Softwareentwickler. (I work as "
            "a software developer.) 2. Mein Buero ist im dritten Stock. "
            "(My office is on the third floor.) 3. Die Besprechung beginnt "
            "um neun Uhr. (The meeting starts at nine o'clock.) 4. Ich "
            "habe viel zu tun. (I have a lot to do.) 5. Der Chef ist heute "
            "nicht da. (The boss is not here today.) 6. Koennen wir das "
            "morgen besprechen? (Can we discuss that tomorrow?) 7. Ich "
            "schicke Ihnen die E-Mail. (I will send you the email.) 8. Der "
            "Computer funktioniert nicht. (The computer is not working.) 9. "
            "Ich brauche Hilfe bei diesem Projekt. (I need help with this "
            "project.) 10. Die Deadline ist am Freitag. (The deadline is "
            "on Friday.) 11. Ich gehe zur Schule. (I go to school.) 12. "
            "Der Unterricht faengt um acht an. (Class starts at eight.) 13. "
            "Die Lehrerin erklaert die Grammatik. (The teacher explains the "
            "grammar.) 14. Wir schreiben einen Test. (We are writing a "
            "test.) 15. Hast du die Hausaufgaben gemacht? (Did you do the "
            "homework?) 16. Ich lerne fuer die Pruefung. (I am studying "
            "for the exam.) 17. Die Pruefung war schwer. (The exam was "
            "hard.) 18. Ich habe eine gute Note bekommen. (I got a good "
            "grade.) 19. In Deutschland sind Noten von eins bis sechs. (In "
            "Germany grades run from one to six.) 20. Nach der Schule "
            "spiele ich Fussball. (After school I play soccer.)"
        ),
        "how_it_works": (
            "Work-and-school sentences work as the domain of formal "
            "address and scheduled time: colleagues are Sie until invited "
            "to du, meetings begin um neun Uhr, and the German grading "
            "scale runs backwards from English - eins is the best grade, "
            "sechs is failure. The verbs of this domain are "
            "communication verbs (besprechen, erklaeren, schicken) and "
            "obligation verbs (muessen, sollen), often in the passive "
            "voice of office life: Die E-Mail wurde geschickt. Time "
            "prepositions do heavy lifting: um for clock time (um neun "
            "Uhr), am for days (am Freitag), im for months (im Mai). "
            "School vocabulary reveals the system: die Grundschule, das "
            "Gymnasium, die Universitaet, der Abschluss. The learner who "
            "can schedule, report, and ask for help in this register is "
            "employable in German."
        ),
        "key_points": [
            "Workplace runs on Sie; school runs on the um/am/im time system.",
            "German grades run 1 (best) to 6 (fail) - the reverse of the American instinct.",
            "Time prepositions: um neun Uhr, am Freitag, im Mai.",
            "Key verbs: besprechen, erklaeren, schicken, muessen, sollen.",
            "Twenty sentences covering jobs, office life, classroom, and exams.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Schedule a meeting in German: propose a time, confirm, and postpone.",
            "Explain the German grading scale in three German sentences.",
            "Write a short work email in German with greeting and closing.",
            "List ten school subjects in German with articles.",
        ],
        "standards": [
            "Professional and academic vocabulary follows standard Hochdeutsch usage.",
            "The 1-to-6 grading scale is the official German school grading system.",
        ],
        "citations": [CIT_DUDEN, CIT_GOETHE],
        "sig_lens": (
            "The Signature read: work German is the signed ledger - every "
            "meeting stamped with um, every deadline sealed with am, every "
            "grade a number from the honest scale where one is the crown "
            "and six is the void. The Signature worker signs the ledger "
            "daily and never fudges the figures."
        ),
    },
    {
        "key": "health",
        "name": "Health and Body Sentences",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about body parts, symptoms, the doctor visit, "
            "and the pharmacy. 1. Mein Kopf tut weh. (My head hurts.) 2. "
            "Ich habe Halsschmerzen. (I have a sore throat.) 3. Mein "
            "Ruecken schmerzt. (My back aches.) 4. Mir ist schlecht. (I "
            "feel sick - to me it is bad.) 5. Ich habe Fieber. (I have a "
            "fever.) 6. Ich bin erklaetet. (I have a cold.) 7. Mein Hals "
            "ist entzuendet. (My throat is inflamed.) 8. Ich brauche einen "
            "Arzt. (I need a doctor.) 9. Wo ist das naechste Krankenhaus? "
            "(Where is the nearest hospital?) 10. Ich habe einen Termin um "
            "zehn Uhr. (I have an appointment at ten o'clock.) 11. Was fehlt "
            "Ihnen? (What is wrong with you? - formal.) 12. Seit wann haben "
            "Sie die Schmerzen? (Since when have you had the pain?) 13. "
            "Zeigen Sie mir, wo es wehtut. (Show me where it hurts.) 14. "
            "Atmen Sie tief ein. (Breathe in deeply.) 15. Sie brauchen "
            "Ruhe. (You need rest.) 16. Nehmen Sie diese Tabletten zweimal "
            "taeglich. (Take these pills twice daily.) 17. Haben Sie etwas "
            "gegen Kopfschmerzen? (Do you have something for headaches?) 18. "
            "Brauche ich ein Rezept? (Do I need a prescription?) 19. Mir "
            "geht es schon besser. (I am already feeling better.) 20. Gute "
            "Besserung! (Get well soon!)"
        ),
        "how_it_works": (
            "Health sentences work as the learner's dative-experience "
            "laboratory: pain and feeling are expressed as things "
            "happening TO the person - Mir ist schlecht, Mein Kopf tut "
            "weh, Mir geht es besser - so the sufferer is the dative "
            "experiencer, not the nominative actor. Body parts are mostly "
            "straightforward compounds: der Kopf, das Auge, die Nase, der "
            "Mund, der Hals, die Schulter, der Arm, die Hand, der Finger, "
            "der Ruecken, das Bein, der Fuss. Symptoms compound too: "
            "Kopfschmerzen, Halsschmerzen, Rueckenschmerzen - literally "
            "head-pains. The doctor's questions run on seit (since when) "
            "and wo (where), and instructions use the Sie imperative: "
            "Nehmen Sie, Atmen Sie, Zeigen Sie. The pharmacy counter runs "
            "on Haben Sie etwas gegen plus the symptom. Gute Besserung is "
            "the universal get-well wish."
        ),
        "key_points": [
            "Pain and feeling take the dative experiencer: Mir ist schlecht, Mein Kopf tut weh.",
            "Symptom compounds: Kopfschmerzen, Halsschmerzen, Rueckenschmerzen.",
            "Doctor questions: Was fehlt Ihnen? Seit wann? Wo tut es weh?",
            "Doctor instructions use the Sie imperative: Nehmen Sie, Atmen Sie.",
            "Pharmacy: Haben Sie etwas gegen Kopfschmerzen? Brauche ich ein Rezept?",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Name 15 body parts with articles from memory.",
            "Describe three symptoms to a doctor in German using seit and wo.",
            "Give three doctor instructions using the Sie imperative.",
            "Explain the dative-experiencer pattern with three examples.",
        ],
        "standards": [
            "Medical vocabulary follows standard Hochdeutsch usage.",
            "Symptom descriptions follow standard German patient-doctor conventions.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: health German is the signed infirmary - "
            "pain reported as weather passing over the dative soul, the "
            "doctor reading the signs like an instrument panel. Mir ist "
            "schlecht is the honest report: the Signature patient states "
            "what IS, never what he wishes."
        ),
    },
    {
        "key": "emotions",
        "name": "Emotions and Feelings Sentences",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences: happy, sad, angry, afraid, love, surprise. "
            "1. Ich bin gluecklich. (I am happy.) 2. Sie freut sich sehr. "
            "(She is very pleased.) 3. Wir sind froh, dich zu sehen. (We "
            "are glad to see you.) 4. Das macht mich froh. (That makes me "
            "happy.) 5. Ich bin traurig. (I am sad.) 6. Er weint. (He is "
            "crying.) 7. Das tut mir leid. (I am sorry about that.) 8. Ich "
            "vermisses dich. (I miss you.) 9. Ich bin wuetend. (I am "
            "furious.) 10. Sie aergerte sich ueber ihn. (She was annoyed "
            "with him.) 11. Beruhige dich! (Calm down!) 12. Das regt mich "
            "auf. (That upsets me.) 13. Ich habe Angst. (I am afraid.) 14. "
            "Ich fuerchte mich vor Spinnen. (I am afraid of spiders.) 15. "
            "Keine Angst! (Do not be afraid!) 16. Ich liebe dich. (I love "
            "you.) 17. Sie haben sich verliebt. (They fell in love.) 18. "
            "Ich bin ueberrascht. (I am surprised.) 19. Das ist eine "
            "Ueberraschung! (That is a surprise!) 20. Ich bin stolz auf "
            "dich. (I am proud of you.)"
        ),
        "how_it_works": (
            "Emotion sentences work as the reflexive-verb showcase: "
            "German feelings often happen to the self reflexively - sich "
            "freuen (to be glad), sich aergern (to be annoyed), sich "
            "verlieben (to fall in love), sich fuerchten (to be afraid) - "
            "so the emotion is something the subject does to itself. "
            "Prepositions carry the emotional direction: stolz AUF "
            "(proud of), Angst VOR (fear of), wuetend AUF (angry at), "
            "sich freuen UEBER (glad about) versus sich freuen AUF "
            "(looking forward to) - the ueber/auf split is the famous "
            "trap. Adjective states use sein: Ich bin gluecklich, Ich bin "
            "traurig, Ich bin muede. Causation uses machen plus "
            "accusative: Das macht mich gluecklich. The learner who "
            "masters the reflexive emotion verbs and their prepositions "
            "sounds German from the inside out."
        ),
        "key_points": [
            "Emotion verbs are often reflexive: sich freuen, sich aergern, sich verlieben, sich fuerchten.",
            "Prepositions carry direction: stolz auf, Angst vor, wuetend auf.",
            "Sich freuen ueber (glad about now) vs sich freuen auf (looking forward to later).",
            "States use sein + adjective: Ich bin gluecklich, Ich bin traurig.",
            "Causation: Das macht mich gluecklich (accusative).",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Conjugate sich freuen in the present tense fully.",
            "Write six sentences using stolz auf, Angst vor, wuetend auf, freuen ueber/auf.",
            "Describe your current mood in five German sentences.",
            "Explain the ueber/auf split in sich freuen with two examples.",
        ],
        "standards": [
            "Emotion vocabulary and reflexive usage follow standard Hochdeutsch.",
            "Prepositional government of emotion verbs follows the Duden standard.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: German emotion is signed weather - the "
            "self both sky and storm, reflexive verbs the barometer. Sich "
            "freuen auf versus ueber is the Signature distinction: joy "
            "aimed at the future wears a different stamp than joy resting "
            "on the present."
        ),
    },
    {
        "key": "nature",
        "name": "Nature and Weather Sentences",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about animals, plants, seasons, and weather "
            "talk. 1. Wie ist das Wetter heute? (How is the weather "
            "today?) 2. Es ist sonnig. (It is sunny.) 3. Es regnet. (It is "
            "raining.) 4. Es schneit. (It is snowing.) 5. Es ist bewoelkt. "
            "(It is cloudy.) 6. Es ist windig. (It is windy.) 7. Es "
            "gewittert. (There is a thunderstorm.) 8. Die Sonne scheint. "
            "(The sun is shining.) 9. Der Himmel ist blau. (The sky is "
            "blue.) 10. Es ist zehn Grad. (It is ten degrees.) 11. Im "
            "Fruehling bluehen die Blumen. (In spring the flowers bloom.) "
            "12. Im Sommer ist es heiss. (In summer it is hot.) 13. Im "
            "Herbst fallen die Blaetter. (In autumn the leaves fall.) 14. "
            "Im Winter ist es kalt. (In winter it is cold.) 15. Der Hund "
            "rennt durch den Wald. (The dog runs through the forest.) 16. "
            "Die Voegel singen. (The birds are singing.) 17. Die Bienen "
            "sammeln Honig. (The bees collect honey.) 18. Der Fluss fliesst "
            "ins Meer. (The river flows into the sea.) 19. Die Berge sind "
            "mit Schnee bedeckt. (The mountains are covered with snow.) 20. "
            "Morgen wird es besser. (Tomorrow it will be better.)"
        ),
        "how_it_works": (
            "Weather sentences work as the impersonal-es laboratory: German "
            "weather happens to nobody - Es regnet, Es schneit, Es ist kalt "
            "- the dummy subject es holds the verb's place while nature "
            "acts. Temperature is counted in Grad (Celsius, always): Es "
            "ist zehn Grad, Es sind minus fuenf Grad. Seasons take im plus "
            "dative: im Fruehling, im Sommer, im Herbst, im Winter. "
            "Animal and plant vocabulary compounds transparently: der "
            "Regenwald (rain forest), die Sonnenblume (sunflower), der "
            "Marienkaefer (ladybug, literally Mary-beetle). Weather talk "
            "is Germany's universal small talk - Wie ist das Wetter "
            "opens more conversations than any other sentence, and "
            "answering with the forecast marks the speaker as an insider."
        ),
        "key_points": [
            "Weather uses impersonal es: Es regnet, Es schneit, Es ist kalt.",
            "Temperatures are in Celsius: Es ist zehn Grad.",
            "Seasons take im + dative: im Fruehling, im Sommer, im Herbst, im Winter.",
            "Nature compounds transparently: Regenwald, Sonnenblume, Marienkaefer.",
            "Weather talk is the universal German small-talk opener.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Give a three-day weather forecast in German.",
            "Name ten animals and ten plants with articles.",
            "Describe each season in three German sentences.",
            "Explain the impersonal es with five weather verbs.",
        ],
        "standards": [
            "Weather and nature vocabulary follows standard Hochdeutsch usage.",
            "Temperature is given in degrees Celsius per German convention.",
        ],
        "citations": [CIT_DUDEN, CIT_GOETHE],
        "sig_lens": (
            "The Signature read: German weather is the signed sky - "
            "impersonal, honest, stamped es because no one owns the rain. "
            "The Signature forecaster reads the clouds like a ledger: "
            "what falls is recorded, what shines is celebrated, nothing "
            "is argued with."
        ),
    },
    {
        "key": "shopping",
        "name": "Shopping and Money Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about the market, prices, bargaining, and "
            "paying. 1. Wo ist der naechste Supermarkt? (Where is the "
            "nearest supermarket?) 2. Der Markt ist jeden Samstag. (The "
            "market is every Saturday.) 3. Wie viel kostet das? (How much "
            "does that cost?) 4. Das kostet drei Euro fuenfzig. (That "
            "costs three euros fifty.) 5. Das ist zu teuer. (That is too "
            "expensive.) 6. Haben Sie etwas Billigeres? (Do you have "
            "something cheaper?) 7. Ich schaue mich nur um. (I am just "
            "looking around.) 8. Kann ich das anprobieren? (Can I try this "
            "on?) 9. Haben Sie eine groessere Groesse? (Do you have a "
            "larger size?) 10. Das passt mir gut. (That fits me well.) 11. "
            "Das steht Ihnen sehr gut. (That suits you very well.) 12. Ich "
            "nehme es. (I will take it.) 13. Kann ich mit Karte zahlen? "
            "(Can I pay by card?) 14. Bar oder mit Karte? (Cash or card?) "
            "15. Die Kasse ist dort drueben. (The checkout is over there.) "
            "16. Ich brauche eine Tuete. (I need a bag.) 17. Haben Sie den "
            "Kassenbon? (Do you have the receipt?) 18. Das ist ein "
            "Schnaeppchen. (That is a bargain.) 19. Im Sonderangebot "
            "kostet es die Haelfte. (On sale it costs half.) 20. Viel Spass "
            "beim Einkaufen! (Have fun shopping!)"
        ),
        "how_it_works": (
            "Shopping sentences work as the comparative-adjective "
            "marketplace: prices are negotiated in comparatives - "
            "billiger, groesser, kleiner - and declined as attributive "
            "adjectives (etwas Billigeres, eine groessere Groesse). Money "
            "speaks in Euro and Cent: drei Euro fuenfzig, with the coin "
            "called Cent and the bill called Schein. The fitting room "
            "runs on two verbs: passen (to fit, dative - Das passt mir) "
            "and stehen (to suit, dative - Das steht Ihnen). Payment is "
            "bar (cash) or mit Karte (by card); the receipt is the "
            "Kassenbon. Bargaining is rare in German shops but normal at "
            "flea markets: Geht es auch billiger? The shopper who can ask "
            "Wie viel kostet das, decline a polite Kein Interesse, and "
            "pay mit Karte is fully equipped."
        ),
        "key_points": [
            "Price language: Wie viel kostet das? Das kostet drei Euro fuenfzig.",
            "Comparatives drive bargaining: billiger, groesser, etwas Billigeres.",
            "Passen (to fit) and stehen (to suit) take the dative: Das passt mir.",
            "Payment: bar (cash) or mit Karte (by card); the receipt is the Kassenbon.",
            "Fitting room: Kann ich das anprobieren? Haben Sie eine groessere Groesse?",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Role-play buying clothes: greeting, trying on, size change, paying.",
            "Form comparatives of ten adjectives and use five in shopping sentences.",
            "Explain passen vs stehen with two sentence pairs.",
            "Write prices for eight items in German words.",
        ],
        "standards": [
            "Commercial vocabulary follows standard Hochdeutsch usage.",
            "Currency is the euro per German convention.",
        ],
        "citations": [CIT_DUDEN, CIT_GOETHE],
        "sig_lens": (
            "The Signature read: the market is the signed exchange - "
            "every price a stamped figure, every bargain a re-stamping. "
            "Wie viel kostet das is the Signature question: asked plainly, "
            "answered honestly, sealed with the Kassenbon."
        ),
    },
    {
        "key": "friendship",
        "name": "Friendship and Social Life Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about meeting people, invitations, and "
            "celebrations. 1. Freut mich, dich kennenzulernen. (Nice to "
            "meet you.) 2. Woher kommst du? (Where are you from?) 3. Ich "
            "komme aus den USA. (I come from the USA.) 4. Wie lange bist du "
            "schon hier? (How long have you been here?) 5. Was machst du "
            "beruflich? (What do you do for work?) 6. Hast du Lust auf "
            "einen Kaffee? (Do you feel like a coffee?) 7. Kommst du mit "
            "ins Kino? (Are you coming to the cinema with us?) 8. Ich lade "
            "dich zum Essen ein. (I invite you to dinner.) 9. Wann passt es "
            "dir? (When suits you?) 10. Am Samstag passt es mir gut. (On "
            "Saturday suits me well.) 11. Wir treffen uns um acht. (We "
            "meet at eight.) 12. Bring bitte nichts mit. (Please bring "
            "nothing.) 13. Herzlichen Glueckwunsch zum Geburtstag! (Happy "
            "birthday!) 14. Alles Gute! (All the best!) 15. Prost! Auf dein "
            "Wohl! (Cheers! To your health!) 16. Das war ein schoener "
            "Abend. (That was a lovely evening.) 17. Danke fuer die "
            "Einladung. (Thanks for the invitation.) 18. Wir sollten uns "
            "bald wieder treffen. (We should meet again soon.) 19. Ruf mich "
            "an! (Call me!) 20. Bis zum naechsten Mal! (Until next time!)"
        ),
        "how_it_works": (
            "Friendship sentences work as the du-territory of German: "
            "friends are du from the first real conversation, and the "
            "invitation verbs - einladen, mitkommen, sich treffen - are "
            "separable and social. The preposition zu governs the dative "
            "of invitation: zum Essen, zum Geburtstag, ins Kino (in plus "
            "accusative of motion). Celebrations have fixed formulas: "
            "Herzlichen Glueckwunsch zum Geburtstag, Frohe Weihnachten, "
            "Frohes neues Jahr, Viel Glueck bei der Pruefung. Small talk "
            "runs on Woher kommst du, Was machst du beruflich, and Wie "
            "lange bist du schon hier - the three questions that open "
            "every German acquaintance. The guest rule: never arrive "
            "empty-handed unless told Bring bitte nichts mit, and even "
            "then flowers or wine are safe."
        ),
        "key_points": [
            "Friends are du; invitations use einladen, mitkommen, sich treffen.",
            "Invitation prepositions: zum Essen, zum Geburtstag, ins Kino.",
            "Celebration formulas: Herzlichen Glueckwunsch, Alles Gute, Prost, Viel Glueck.",
            "The three acquaintance questions: Woher kommst du? Was machst du beruflich? Wie lange bist du schon hier?",
            "Guest rule: bring flowers or wine unless told otherwise.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Introduce yourself to a new acquaintance in six German sentences.",
            "Invite a friend to dinner, propose a time, and accept - as a dialogue.",
            "Write birthday, Christmas, and New Year wishes in German.",
            "Explain when du replaces Sie in three sentences.",
        ],
        "standards": [
            "Social formulas follow standard German conventions.",
            "Invitation and celebration vocabulary follows standard Hochdeutsch.",
        ],
        "citations": [CIT_GOETHE, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: friendship German is the signed circle - "
            "du the inner seal, the invitation the stamped summons, Prost "
            "the raised seal of the evening. The Signature friend never "
            "arrives empty-handed and never leaves without Bis zum "
            "naechsten Mal."
        ),
    },
    {
        "key": "technology",
        "name": "Technology and Communication Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty sentences about phone, internet, computer, and "
            "messaging. 1. Mein Handy ist leer. (My phone is dead - empty "
            "of battery.) 2. Wo ist mein Ladekabel? (Where is my charging "
            "cable?) 3. Hast du WLAN? (Do you have Wi-Fi?) 4. Wie ist das "
            "Passwort? (What is the password?) 5. Das Internet ist sehr "
            "langsam. (The internet is very slow.) 6. Ich schicke dir eine "
            "Nachricht. (I am sending you a message.) 7. Ruf mich spaeter "
            "an. (Call me later.) 8. Ich bin gerade nicht erreichbar. (I "
            "cannot be reached right now.) 9. Sprich bitte lauter. (Please "
            "speak louder.) 10. Die Verbindung ist schlecht. (The "
            "connection is bad.) 11. Mein Computer startet nicht. (My "
            "computer will not start.) 12. Der Bildschirm ist schwarz. (The "
            "screen is black.) 13. Ich habe die Datei gespeichert. (I saved "
            "the file.) 14. Kannst du mir den Link schicken? (Can you send "
            "me the link?) 15. Ich lade das Foto hoch. (I am uploading the "
            "photo.) 16. Das Programm ist abgestuerzt. (The program "
            "crashed.) 17. Starte den Computer neu. (Restart the computer.) "
            "18. Ich suche im Internet nach Informationen. (I am searching "
            "the internet for information.) 19. Meine E-Mail-Adresse hat "
            "sich geaendert. (My email address has changed.) 20. Schreib "
            "mir bitte zurueck. (Please write back to me.)"
        ),
        "how_it_works": (
            "Technology sentences work as the loanword frontier of German: "
            "the nouns are largely English imports naturalized with German "
            "genders - das Handy (mobile phone), das WLAN, der Computer, "
            "die E-Mail, der Link, das Passwort - while the verbs stay "
            "German and separable: anrufen, zurueckschreiben, hochladen, "
            "herunterladen, neustarten. Note das Handy is a false friend: "
            "it means mobile phone, never handy. Compound nouns name the "
            "hardware: das Ladekabel, der Bildschirm, die Tastatur, die "
            "Maus. Commands in tech support are informal imperatives: "
            "Starte neu, Sprich lauter, Schreib zurueck. The perfect tense "
            "reports what happened: Das Programm ist abgestuerzt, Ich habe "
            "die Datei gespeichert. The tech user who knows anrufen, "
            "schicken, speichern, hochladen, and neustarten can survive "
            "any German help desk."
        ),
        "key_points": [
            "Tech nouns are English loans with German genders: das Handy, der Computer, die E-Mail.",
            "Das Handy means mobile phone - a false friend, never handy.",
            "Tech verbs are German and separable: anrufen, hochladen, zurueckschreiben, neustarten.",
            "Hardware compounds: Ladekabel, Bildschirm, Tastatur.",
            "Tech support runs on informal imperatives and the perfect tense.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Explain a phone problem to a support agent in six German sentences.",
            "List twelve tech nouns with genders and plurals.",
            "Conjugate anrufen, hochladen, and zurueckschreiben in the present tense.",
            "Write instructions for restarting a computer in four German imperatives.",
        ],
        "standards": [
            "Technology vocabulary follows current standard German usage.",
            "Loanword genders follow Duden standard assignments.",
        ],
        "citations": [CIT_DUDEN, CIT_GOETHE],
        "sig_lens": (
            "The Signature read: tech German is the signed workbench - "
            "English parts, German tools, every loanword re-stamped with a "
            "gender on arrival. Das Handy is the Signature lesson in false "
            "friends: the label lies, the stamp tells the truth."
        ),
    },
]

ENTRIES += [
    {
        "key": "tenses",
        "name": "German Verb Tenses in Sentences",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "The six German tenses, six translated sentences each. "
            "PRAESENS (present - also used for scheduled future): 1. Ich "
            "lerne Deutsch. (I am learning German.) 2. Er arbeitet in "
            "Berlin. (He works in Berlin.) 3. Wir essen um zwoelf Uhr. (We "
            "eat at twelve o'clock.) 4. Sie spricht drei Sprachen. (She "
            "speaks three languages.) 5. Morgen regnet es. (Tomorrow it "
            "will rain.) 6. Der Zug faehrt um acht. (The train leaves at "
            "eight.) PRAETERITUM (simple past - written narrative, "
            "especially northern Germany): 1. Ich lernte Deutsch. (I "
            "learned German.) 2. Er arbeitete in Berlin. (He worked in "
            "Berlin.) 3. Wir assen um zwoelf Uhr. (We ate at twelve.) 4. "
            "Sie sprach drei Sprachen. (She spoke three languages.) 5. Es "
            "regnete den ganzen Tag. (It rained all day.) 6. Der Zug fuhr "
            "puenktlich. (The train left on time.) PERFEKT (conversational "
            "past - haben/sein plus past participle): 1. Ich habe Deutsch "
            "gelernt. (I learned German.) 2. Er hat in Berlin gearbeitet. "
            "(He worked in Berlin.) 3. Wir haben um zwoelf Uhr gegessen. "
            "(We ate at twelve.) 4. Sie hat drei Sprachen gesprochen. (She "
            "spoke three languages.) 5. Es hat den ganzen Tag geregnet. "
            "(It rained all day.) 6. Der Zug ist puenktlich abgefahren. "
            "(The train departed on time.) PLUSQUAMPERFEKT (past perfect - "
            "had done): 1. Ich hatte Deutsch gelernt. (I had learned "
            "German.) 2. Er hatte in Berlin gearbeitet. (He had worked in "
            "Berlin.) 3. Wir hatten schon gegessen. (We had already eaten.) "
            "4. Sie hatte drei Sprachen gesprochen. (She had spoken three "
            "languages.) 5. Es hatte den ganzen Tag geregnet. (It had "
            "rained all day.) 6. Der Zug war schon abgefahren. (The train "
            "had already departed.) FUTUR I (future - werden plus "
            "infinitive): 1. Ich werde Deutsch lernen. (I will learn "
            "German.) 2. Er wird in Berlin arbeiten. (He will work in "
            "Berlin.) 3. Wir werden um zwoelf Uhr essen. (We will eat at "
            "twelve.) 4. Sie wird drei Sprachen sprechen. (She will speak "
            "three languages.) 5. Es wird morgen regnen. (It will rain "
            "tomorrow.) 6. Der Zug wird um acht fahren. (The train will "
            "leave at eight.) FUTUR II (future perfect - will have done): "
            "1. Ich werde Deutsch gelernt haben. (I will have learned "
            "German.) 2. Er wird in Berlin gearbeitet haben. (He will have "
            "worked in Berlin.) 3. Wir werden schon gegessen haben. (We "
            "will have already eaten.) 4. Sie wird drei Sprachen gesprochen "
            "haben. (She will have spoken three languages.) 5. Es wird den "
            "ganzen Tag geregnet haben. (It will have rained all day.) 6. "
            "Der Zug wird puenktlich abgefahren sein. (The train will have "
            "departed on time.) Participle rules: weak verbs take ge- plus "
            "-t (gelernt, gearbeitet); strong verbs take ge- plus -en with "
            "vowel change (gesprochen, gegessen, gefahren); verbs of motion "
            "and change of state use sein (gegangen, geblieben, geworden); "
            "verbs with inseparable prefixes skip ge- (besucht, verkauft)."
        ),
        "how_it_works": (
            "German tenses work as a six-gear transmission built from three "
            "auxiliaries. The Praesens is the workhorse - present action "
            "and scheduled future both, since Morgen regnet es needs no "
            "future marking. The past splits by register: Praeteritum for "
            "writing and storytelling (strong verbs show their vowel "
            "music: sprechen/sprach/gesprochen), Perfekt for speaking "
            "(haben or sein plus the participle at the end). The "
            "Plusquamperfekt reaches one step further back with hatte/war. "
            "Futur I is werden plus infinitive at the end; Futur II stacks "
            "werden plus participle plus haben/sein. The auxiliary choice "
            "is the key decision: sein for motion and change of state "
            "(gehen, kommen, bleiben, werden, sterben), haben for "
            "everything else. Participles follow the ge- rule with the "
            "inseparable-prefix exception. Six gears, three auxiliaries, "
            "one rule set - the whole past and future of German."
        ),
        "key_points": [
            "Six tenses: Praesens, Praeteritum, Perfekt, Plusquamperfekt, Futur I, Futur II.",
            "Praesens covers present and scheduled future; Praeteritum is written past, Perfekt spoken past.",
            "Sein for motion and change of state; haben for everything else.",
            "Participles: ge- + -t for weak verbs, ge- + -en with vowel change for strong verbs; inseparable prefixes skip ge-.",
            "In Perfekt and Plusquamperfekt the participle goes to the end; in Futur the infinitive goes to the end.",
        ],
        "requirements": [
            "Conjugate sprechen, gehen, and arbeiten in all six tenses.",
            "Convert six Praesens sentences into Perfekt and six into Praeteritum.",
            "Explain the haben/sein choice with four verb pairs.",
            "Form past participles of twelve verbs, six weak and six strong.",
            "Write two sentences in each of the six tenses about your week.",
        ],
        "standards": [
            "Tense formation follows the Duden standard grammar.",
            "Auxiliary selection follows the standard motion/change-of-state rule.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: German tenses are six signed gears - "
            "present the drive gear, past the two reverse gears (one for "
            "the page, one for the mouth), future the overdrive. Haben "
            "and sein are the two master keys; the Signature driver never "
            "forces the wrong key into the ignition."
        ),
    },
    {
        "key": "qa",
        "name": "German Questions and Answers",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Twenty question-and-answer pairs covering who, what, where, "
            "when, why, and how. 1. Wer ist das? - Das ist mein Bruder. "
            "(Who is that? - That is my brother.) 2. Was ist das? - Das "
            "ist ein Apfel. (What is that? - That is an apple.) 3. Wo "
            "wohnst du? - Ich wohne in Muenchen. (Where do you live? - I "
            "live in Munich.) 4. Wohin gehst du? - Ich gehe zur Arbeit. "
            "(Where are you going? - I am going to work.) 5. Woher kommst "
            "du? - Ich komme aus Hamburg. (Where are you from? - I come "
            "from Hamburg.) 6. Wann beginnt der Film? - Um zwanzig Uhr. "
            "(When does the movie start? - At eight pm.) 7. Warum lernst "
            "du Deutsch? - Weil ich in Deutschland arbeiten will. (Why are "
            "you learning German? - Because I want to work in Germany.) 8. "
            "Wie heisst du? - Ich heisse Anna. (What is your name? - My "
            "name is Anna.) 9. Wie alt bist du? - Ich bin dreissig Jahre "
            "alt. (How old are you? - I am thirty years old.) 10. Wie viel "
            "kostet das? - Fuenf Euro. (How much does that cost? - Five "
            "euros.) 11. Wie viele Sprachen sprichst du? - Drei. (How many "
            "languages do you speak? - Three.) 12. Welcher Tag ist heute? "
            "- Heute ist Montag. (Which day is today? - Today is Monday.) "
            "13. Welche Farbe magst du? - Blau. (Which color do you like? "
            "- Blue.) 14. Wem gehoert das Buch? - Mir. (Whose book is "
            "that? - Mine.) 15. Wen hast du eingeladen? - Meine Freunde. "
            "(Whom did you invite? - My friends.) 16. Wie geht es dir? - "
            "Gut, danke. (How are you? - Well, thanks.) 17. Was machst du "
            "beruflich? - Ich bin Lehrer. (What do you do for work? - I am "
            "a teacher.) 18. Wie lange bleibst du? - Zwei Wochen. (How "
            "long are you staying? - Two weeks.) 19. Wie oft trainierst "
            "du? - Dreimal pro Woche. (How often do you train? - Three "
            "times per week.) 20. Warum nicht? - Warum nicht! (Why not? - "
            "Why not!)"
        ),
        "how_it_works": (
            "German questions work on two tracks. W-questions put the "
            "interrogative first and the verb second: Wer, Was, Wo, Wohin, "
            "Woher, Wann, Warum, Wie, Wie viel, Wie viele, Welcher - the "
            "question word is always position one, the verb always "
            "position two. Yes/no questions invert: the verb takes first "
            "position and the voice rises - Kommst du mit? The answers "
            "follow the case logic: wer asks nominative, wen accusative, "
            "wem dative, wessen genitive. Wie viel asks uncountable "
            "amount (Wie viel kostet das?), Wie viele asks countable "
            "number (Wie viele Sprachen?). Welcher declines like the "
            "definite article it replaces. Warum is answered with weil "
            "plus verb-final word order - the question-answer pair "
            "teaches subordinate clauses for free."
        ),
        "key_points": [
            "W-questions: question word first, verb second - Was machst du?",
            "Yes/no questions: verb first, rising intonation - Kommst du mit?",
            "Wer/wen/wem/wessen mirror the four cases.",
            "Wie viel (how much, uncountable) vs Wie viele (how many, countable).",
            "Welcher declines like the definite article; warum is answered with weil + verb-final.",
        ],
        "requirements": [
            "Ask and answer all 20 pairs from memory both directions.",
            "Write six new W-questions, one per interrogative family.",
            "Convert six statements into yes/no questions.",
            "Explain wie viel vs wie viele with three examples each.",
            "Decline welcher through masculine, feminine, neuter, plural.",
        ],
        "standards": [
            "Interrogative usage follows the Duden standard grammar.",
            "Question formation follows standard German word-order rules.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: German questions are signed probes - "
            "each W-word a calibrated instrument, wer for persons, was "
            "for things, wo/wohin/woher for the three directions of "
            "space. The Signature inquirer never asks vaguely; the stamp "
            "on the question determines the shape of the answer."
        ),
    },
    {
        "key": "commands",
        "name": "German Commands and Requests",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Twenty imperative and polite-request sentences, formal versus "
            "informal. Informal singular (du): 1. Komm her! (Come here!) "
            "2. Iss dein Gemuese! (Eat your vegetables!) 3. Sprich "
            "langsamer! (Speak more slowly!) 4. Warte einen Moment! (Wait "
            "a moment!) 5. Sei ruhig! (Be quiet! - sein is irregular.) "
            "Informal plural (ihr): 6. Kommt her! (Come here, you all!) 7. "
            "Esst euer Gemuese! (Eat your vegetables, you all!) Formal "
            "(Sie): 8. Kommen Sie bitte her! (Please come here!) 9. "
            "Sprechen Sie bitte langsamer! (Please speak more slowly!) 10. "
            "Nehmen Sie Platz! (Take a seat!) Polite requests with "
            "Konjunktiv II: 11. Koennten Sie mir helfen? (Could you help "
            "me?) 12. Wuerden Sie bitte warten? (Would you please wait?) "
            "13. Haettest du einen Moment Zeit? (Would you have a moment? "
            "- informal.) 14. Wuerdest du mir das geben? (Would you give "
            "me that? - informal.) Softened with modal particles: 15. "
            "Mach doch das Fenster zu! (Do close the window! - doch "
            "softens.) 16. Komm mal her! (Come here a moment! - mal "
            "softens.) Suggestions with wir: 17. Gehen wir spazieren! "
            "(Let us go for a walk!) 18. Fangen wir an! (Let us begin!) "
            "Negative commands: 19. Mach das nicht! (Do not do that!) 20. "
            "Vergiss das bitte nicht! (Please do not forget that!) "
            "Formation: du-imperative is the verb stem - komm from "
            "kommen, iss from essen (stem vowel change kept), sprich from "
            "sprechen; ihr-imperative is the ihr present form - kommt, "
            "esst; Sie-imperative is the infinitive plus Sie - Kommen Sie, "
            "Sprechen Sie; wir-suggestion is Gehen wir."
        ),
        "how_it_works": (
            "German imperatives work as a four-address system: du for one "
            "friend (stem only, no ending, no pronoun - Komm!), ihr for "
            "several friends (the ihr present form - Kommt!), Sie for "
            "formal address (infinitive plus Sie - Kommen Sie!), and wir "
            "for suggestions (Gehen wir!). The du form drops the -en and "
            "usually the -e: komm, mach, warte; stem-changing verbs keep "
            "their change (iss, sprich, lies) but lose any umlaut (fahren "
            "becomes fahr, not faehr). Sein is the famous irregular: Sei "
            "ruhig! True politeness, however, rarely uses the bare "
            "imperative with strangers - it wraps the request in "
            "Konjunktiv II (Koennten Sie, Wuerden Sie) and the word bitte, "
            "or softens with modal particles: doch, mal, denn. The "
            "learner's rule: command friends, request strangers."
        ),
        "key_points": [
            "Four imperatives: du (Komm!), ihr (Kommt!), Sie (Kommen Sie!), wir (Gehen wir!).",
            "Du-imperative is the bare stem; stem-changing verbs keep the change but lose umlaut.",
            "Sein is irregular: Sei ruhig!",
            "Polite requests use Konjunktiv II: Koennten Sie, Wuerden Sie, plus bitte.",
            "Modal particles soften commands: Mach doch, Komm mal her.",
        ],
        "requirements": [
            "Form du, ihr, and Sie imperatives for ten verbs from memory.",
            "Convert five bare commands into polite Konjunktiv II requests.",
            "Explain the stem-vowel rule with iss, sprich, lies, fahr.",
            "Write three suggestions with Gehen wir / Fangen wir an.",
            "Soften five commands with doch or mal.",
        ],
        "standards": [
            "Imperative formation follows the Duden standard grammar.",
            "Politeness conventions follow standard German address usage.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: the German imperative is the signed "
            "order - four stamps for four ranks, du for the comrade, Sie "
            "for the honored. But the Signature commander knows the "
            "deeper art: true authority requests with Koennten Sie and "
            "softens with doch, because the willing hand outworks the "
            "commanded one."
        ),
    },
    {
        "key": "descriptions",
        "name": "German Descriptions: People and Places",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Twenty sentences describing people, places, and things in "
            "detail. 1. Meine Schwester hat lange blonde Haare und blaue "
            "Augen. (My sister has long blond hair and blue eyes.) 2. Er "
            "ist gross, schlank und sehr sportlich. (He is tall, slim, and "
            "very athletic.) 3. Die alte Dame traegt einen eleganten Hut. "
            "(The old lady wears an elegant hat.) 4. Der kleine Junge "
            "lacht laut. (The little boy laughs loudly.) 5. Sie hat ein "
            "freundliches Laecheln. (She has a friendly smile.) 6. Sein "
            "Bart ist grau und kurz. (His beard is gray and short.) 7. "
            "Berlin ist eine aufregende Stadt mit vielen Museen. (Berlin "
            "is an exciting city with many museums.) 8. Das Brandenburger "
            "Tor ist das Wahrzeichen Berlins. (The Brandenburg Gate is "
            "Berlin's landmark.) 9. Muenchen liegt im Sueden Deutschlands. "
            "(Munich lies in the south of Germany.) 10. Die Alpen sind im "
            "Winter wunderschoen. (The Alps are wonderful in winter.) 11. "
            "Der Rhein fliesst durch mehrere Laender. (The Rhine flows "
            "through several countries.) 12. Das Schloss steht auf einem "
            "Huegel. (The castle stands on a hill.) 13. Die Altstadt hat "
            "enge Gassen und alte Haeuser. (The old town has narrow alleys "
            "and old houses.) 14. Mein Zimmer ist gemuetlich und hell. (My "
            "room is cozy and bright.) 15. Der Garten ist voller bunter "
            "Blumen. (The garden is full of colorful flowers.) 16. Das "
            "neue Auto ist rot und sehr schnell. (The new car is red and "
            "very fast.) 17. Die Suppe schmeckt wuerzig und heiss. (The "
            "soup tastes spicy and hot.) 18. Der Kaffee duftet stark. (The "
            "coffee smells strong.) 19. Die Musik klingt froehlich. (The "
            "music sounds cheerful.) 20. Die Nacht war still und sternklar. "
            "(The night was quiet and starry.)"
        ),
        "how_it_works": (
            "Description sentences work as the attributive-adjective "
            "workshop: adjectives before nouns must carry their endings - "
            "eine aufregende Stadt, einen eleganten Hut, enge Gassen - "
            "while predicative adjectives stay bare - Er ist gross, Die "
            "Nacht war still. The senses divide the labor in German: "
            "schmecken for taste, duften or riechen for smell, klingen for "
            "sound, sich anfuehlen for touch, aussehen for appearance. "
            "Possession in descriptions uses haben plus accusative (Sie "
            "hat blaue Augen) or the genitive (das Wahrzeichen Berlins). "
            "Location descriptions lean on liegen, stehen, and sich "
            "befinden with dative prepositions. Color, size, and character "
            "adjectives stack naturally before the noun - lange blonde "
            "Haare - and the learner practices the ending tables with "
            "every description."
        ),
        "key_points": [
            "Attributive adjectives inflect: eine aufregende Stadt, einen eleganten Hut.",
            "Sense verbs: schmecken (taste), duften/riechen (smell), klingen (sound), aussehen (look).",
            "Possession: Sie hat blaue Augen; das Wahrzeichen Berlins (genitive).",
            "Location: liegen, stehen, sich befinden with dative prepositions.",
            "Adjectives stack before the noun: lange blonde Haare.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Describe a family member in eight German sentences.",
            "Describe your city in eight German sentences.",
            "Write five sentences using the sense verbs correctly.",
            "Explain attributive vs predicative adjectives with four pairs.",
        ],
        "standards": [
            "Descriptive vocabulary follows standard Hochdeutsch usage.",
            "Adjective declension follows the Duden standard grammar.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: description is the signed portrait - "
            "each adjective a brushstroke stamped with its ending, each "
            "sense verb a window opened to the world. The Signature "
            "painter never leaves an attributive adjective unstamped; "
            "the ending is the signature in the corner of the canvas."
        ),
    },
    {
        "key": "story1",
        "name": "German Story I: A Day in Berlin",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence simple story in German with line-by-line "
            "English translation. 1. Anna wohnt in Berlin. (Anna lives in "
            "Berlin.) 2. Jeden Morgen steht sie um sieben Uhr auf. (Every "
            "morning she gets up at seven o'clock.) 3. Sie fruehstueckt mit "
            "ihrer Familie. (She has breakfast with her family.) 4. Um acht "
            "Uhr geht sie zur Arbeit. (At eight o'clock she goes to work.) "
            "5. Sie arbeitet in einem grossen Buero. (She works in a big "
            "office.) 6. Mittags isst sie mit Kollegen in der Kantine. (At "
            "lunchtime she eats with colleagues in the cafeteria.) 7. Am "
            "Nachmittag hat sie eine Besprechung. (In the afternoon she "
            "has a meeting.) 8. Um sechs Uhr faehrt sie nach Hause. (At six "
            "o'clock she drives home.) 9. Abends kocht sie mit ihrem Mann. "
            "(In the evening she cooks with her husband.) 10. Um zehn Uhr "
            "geht sie ins Bett. (At ten o'clock she goes to bed.)"
        ),
        "how_it_works": (
            "This story works as the learner's first connected German "
            "text: ten sentences, all present tense, all verb-second, "
            "time expressions in first position driving inversion (Jeden "
            "Morgen steht sie auf). The separable verb aufstehen shows "
            "its split across the sentence - steht sie um sieben Uhr auf. "
            "The dative of accompaniment appears naturally: mit ihrer "
            "Familie, mit Kollegen, mit ihrem Mann. Time vocabulary "
            "compounds: morgens, mittags, nachmittags, abends, and the "
            "clock phrases um sieben Uhr. The learner reads it aloud "
            "three times - first for sound, second for meaning, third "
            "for the verb positions - and the story becomes a template "
            "for describing any day."
        ),
        "key_points": [
            "Ten sentences, all present tense, all verb-second - the template of a German day.",
            "Time-first position triggers inversion: Jeden Morgen steht sie auf.",
            "Separable verb aufstehen splits across the sentence.",
            "Dative of accompaniment: mit ihrer Familie, mit ihrem Mann.",
            "Time words: morgens, mittags, nachmittags, abends; um sieben Uhr.",
        ],
        "requirements": [
            "Read the story aloud and translate each line without looking.",
            "Write your own ten-sentence day in German following the template.",
            "Mark the verb position in each of the ten sentences.",
            "Conjugate aufstehen fully in the present tense.",
            "Explain inversion after time expressions with three examples.",
        ],
        "standards": [
            "Narrative follows standard Hochdeutsch usage.",
            "Word order follows standard verb-second rules.",
        ],
        "citations": [CIT_DUDEN, CIT_GOETHE],
        "sig_lens": (
            "The Signature read: Anna's day is the signed routine - ten "
            "stamps from seven in the morning to ten at night, each hour "
            "a station on the conveyor. The Signature day is engineered "
            "the same way: wake, work, return, rest, every verb in its "
            "second position, nothing out of order."
        ),
    },
    {
        "key": "story2",
        "name": "German Story II: The Lost Key (Past Tense)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story using past tenses, with line-by-line "
            "English translation. 1. Gestern verlor Max seinen Schluessel. "
            "(Yesterday Max lost his key.) 2. Er suchte ueberall in der "
            "Wohnung. (He searched everywhere in the apartment.) 3. Er "
            "schaute unter das Bett und hinter den Schrank. (He looked "
            "under the bed and behind the wardrobe.) 4. Ploetzlich "
            "erinnerte er sich an den Park. (Suddenly he remembered the "
            "park.) 5. Er war am Nachmittag dort spazieren gegangen. (He "
            "had gone for a walk there in the afternoon.) 6. Schnell lief "
            "er zum Park zurueck. (He quickly ran back to the park.) 7. Auf "
            "der Bank lag der Schluessel. (On the bench lay the key.) 8. "
            "Max freute sich sehr. (Max was very glad.) 9. Er hatte ihn "
            "beim Lesen verloren. (He had lost it while reading.) 10. "
            "Seitdem traegt er ihn immer am Halsband. (Since then he "
            "always wears it on a lanyard.)"
        ),
        "how_it_works": (
            "This story works as the past-tense engine room: the "
            "Praeteritum carries the narrative (verlor, suchte, schaute, "
            "erinnerte, lief, lag, freute), the Plusquamperfekt reaches "
            "further back (war gegangen, hatte verloren), and the "
            "Praesens closes the story in the present (traegt). Strong "
            "verbs show their vowel changes: verlieren/verlor/verloren, "
            "laufen/lief/gelaufen, liegen/lag/gelegen. The separable verb "
            "zuruecklaufen splits in the past: lief er zum Park zurueck. "
            "Reflexive verbs appear in narrative: sich erinnern, sich "
            "freuen. Time markers sequence the story: gestern, ploetzlich, "
            "am Nachmittag, seitdem. The learner who can retell this "
            "story controls the German past."
        ),
        "key_points": [
            "Praeteritum carries written narrative: verlor, suchte, lief, lag.",
            "Plusquamperfekt reaches further back: war gegangen, hatte verloren.",
            "Strong-verb vowel changes: verlieren/verlor/verloren, laufen/lief/gelaufen.",
            "Separable verbs split in the past: lief er zum Park zurueck.",
            "Time markers sequence narrative: gestern, ploetzlich, seitdem.",
        ],
        "requirements": [
            "Retell the story in German without looking at the text.",
            "Identify the tense of every verb in the ten sentences.",
            "Convert the story from Praeteritum to Perfekt.",
            "Conjugate verlieren, laufen, liegen in Praeteritum.",
            "Write your own ten-sentence past-tense story.",
        ],
        "standards": [
            "Past-tense forms follow the Duden standard grammar.",
            "Narrative tense usage follows standard German conventions.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: the lost key is the signed parable of "
            "the past - what is lost in the present is found by walking "
            "the Plusquamperfekt backward. The Signature investigator "
            "reconstructs: war gegangen, hatte verloren, and the key "
            "appears on the bench of memory."
        ),
    },
    {
        "key": "story3",
        "name": "German Story III: The Dream Journey (Future and Conditional)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story using future and conditional forms, "
            "with line-by-line English translation. 1. Naechstes Jahr wird "
            "Lena eine grosse Reise machen. (Next year Lena will take a "
            "big trip.) 2. Sie wird drei Laender besuchen. (She will visit "
            "three countries.) 3. Zuerst wird sie nach Italien fliegen. "
            "(First she will fly to Italy.) 4. Dort wird sie die "
            "Kunststaedte sehen. (There she will see the art cities.) 5. "
            "Dann wird sie weiter nach Spanien fahren. (Then she will "
            "travel on to Spain.) 6. Sie wird am Meer entspannen. (She "
            "will relax by the sea.) 7. Wenn sie genug Geld haette, wuerde "
            "sie auch nach Japan fliegen. (If she had enough money, she "
            "would also fly to Japan.) 8. Sie wuerde den Berg Fuji "
            "besteigen. (She would climb Mount Fuji.) 9. Aber zuerst wird "
            "sie fleissig sparen. (But first she will save diligently.) 10. "
            "In einem Jahr wird sie am Strand sitzen und laecheln. (In a "
            "year she will sit on the beach and smile.)"
        ),
        "how_it_works": (
            "This story works as the future-conditional duet: Futur I "
            "with werden plus infinitive paints the certain plan (wird "
            "machen, wird besuchen, wird fliegen), while Konjunktiv II "
            "with wuerde plus infinitive paints the dream (wuerde fliegen, "
            "wuerde besteigen). The wenn-clause with haette triggers the "
            "conditional main clause - the classic German if-then machine: "
            "Wenn sie genug Geld haette, wuerde sie fliegen. Time adverbs "
            "sequence the future: naechstes Jahr, zuerst, dann, in einem "
            "Jahr. The story teaches the learner's most useful "
            "distinction: werden for what will happen, wuerde for what "
            "would happen. The final sentence lands the story in the "
            "future perfect of imagination: she WILL sit on the beach."
        ),
        "key_points": [
            "Futur I: werden + infinitive - wird machen, wird besuchen, wird fliegen.",
            "Konjunktiv II: wuerde + infinitive - wuerde fliegen, wuerde besteigen.",
            "Wenn with Konjunktiv II triggers the conditional: Wenn sie Geld haette, wuerde sie fliegen.",
            "Werden is for what will happen; wuerde is for what would happen.",
            "Future sequencing: naechstes Jahr, zuerst, dann, in einem Jahr.",
        ],
        "requirements": [
            "Retell the story in German without looking.",
            "Convert five Futur I sentences into Konjunktiv II conditionals.",
            "Build three wenn/wuerde sentence pairs of your own.",
            "Conjugate werden in Futur I fully.",
            "Write a ten-sentence story about your own dream trip.",
        ],
        "standards": [
            "Future and conditional forms follow the Duden standard grammar.",
            "Konjunktiv II usage follows standard German conventions.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: Lena's journey is the signed blueprint - "
            "wird for the committed steel, wuerde for the dreamed "
            "addition. The Signature builder draws in wuerde and builds "
            "in wird; the dream is the draft, the future the "
            "construction."
        ),
    },
    {
        "key": "idioms",
        "name": "German Idioms and Proverbs",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty idioms and proverbs with literal translation, real "
            "meaning, and an example sentence. 1. Aller Anfang ist schwer. "
            "(All beginning is hard. - Every beginning is difficult.) "
            "Example: Aller Anfang ist schwer, aber du schaffst das. 2. "
            "Uebung macht den Meister. (Practice makes the master. - "
            "Practice makes perfect.) Example: Uebe jeden Tag: Uebung "
            "macht den Meister. 3. Morgenstund hat Gold im Mund. (Morning "
            "hour has gold in its mouth. - The early bird gets the worm.) "
            "Example: Steh frueh auf: Morgenstund hat Gold im Mund. 4. Der "
            "Apfel faellt nicht weit vom Stamm. (The apple does not fall "
            "far from the trunk. - Children resemble parents.) Example: Er "
            "ist Ingenieur wie sein Vater: Der Apfel faellt nicht weit vom "
            "Stamm. 5. Viele Koeche verderben den Brei. (Many cooks spoil "
            "the porridge. - Too many cooks spoil the broth.) Example: "
            "Lasst nur zwei entscheiden: Viele Koeche verderben den Brei. "
            "6. Reden ist Silber, Schweigen ist Gold. (Talking is silver, "
            "silence is gold. - Speech is silver, silence is golden.) "
            "Example: Manchmal gilt: Reden ist Silber, Schweigen ist Gold. "
            "7. Wo ein Wille ist, ist auch ein Weg. (Where there is a "
            "will, there is a way.) Example: Gib nicht auf: Wo ein Wille "
            "ist, ist auch ein Weg. 8. Luegen haben kurze Beine. (Lies "
            "have short legs. - Lies are quickly exposed.) Example: Sag "
            "die Wahrheit: Luegen haben kurze Beine. 9. Kleider machen "
            "Leute. (Clothes make people. - Clothes make the man.) "
            "Example: Zieh dich gut an: Kleider machen Leute. 10. Wer "
            "rastet, der rostet. (Who rests, rusts. - Use it or lose it.) "
            "Example: Bleib aktiv: Wer rastet, der rostet. 11. In der Ruhe "
            "liegt die Kraft. (In calm lies strength. - Strength lies in "
            "calm.) Example: Atme tief: In der Ruhe liegt die Kraft. 12. "
            "Aus den Augen, aus dem Sinn. (Out of the eyes, out of the "
            "mind. - Out of sight, out of mind.) Example: Schreib ihr: Aus "
            "den Augen, aus dem Sinn. 13. Geteiltes Leid ist halbes Leid. "
            "(Shared sorrow is half sorrow. - Shared sorrow is halved.) "
            "Example: Erzaehl mir alles: Geteiltes Leid ist halbes Leid. "
            "14. Stille Wasser sind tief. (Still waters are deep.) Example: "
            "Unterschaetze ihn nicht: Stille Wasser sind tief. 15. Da liegt "
            "der Hund begraben. (There lies the dog buried. - That is the "
            "crux of the matter.) Example: Hoer gut zu: Da liegt der Hund "
            "begraben. 16. Alles hat ein Ende, nur die Wurst hat zwei. "
            "(Everything has an end, only the sausage has two. - All good "
            "things come to an end, said humorously.) Example: Die Party "
            "ist vorbei: Alles hat ein Ende, nur die Wurst hat zwei. 17. "
            "Man soll den Tag nicht vor dem Abend loben. (One should not "
            "praise the day before the evening. - Do not count your "
            "chickens.) Example: Warte ab: Man soll den Tag nicht vor dem "
            "Abend loben. 18. Wie du mir, so ich dir. (As you to me, so I "
            "to you. - Tit for tat.) Example: Hilf mir, dann helfe ich "
            "dir: Wie du mir, so ich dir. 19. Der fruehe Vogel faengt den "
            "Wurm. (The early bird catches the worm.) Example: Sei "
            "puenktlich: Der fruehe Vogel faengt den Wurm. 20. Arbeit "
            "adelt. (Work ennobles.) Example: Jede Arbeit zaehlt: Arbeit "
            "adelt."
        ),
        "how_it_works": (
            "German idioms work as the culture's compressed wisdom: each "
            "Sprichwort packs a life rule into a rhyming, rhythmic "
            "sentence that native speakers deploy like punctuation. The "
            "grammar inside is often archaic or playful - Man soll den "
            "Tag nicht vor dem Abend loben uses the impersonal man; Wer "
            "rastet, der rostet is a relative-clause proverb; Alles hat "
            "ein Ende, nur die Wurst hat zwei is pure humor. Learners "
            "should never translate idioms word-for-word into English "
            "conversation - Da liegt der Hund begraben will baffle an "
            "English speaker - but recognizing the twenty core proverbs "
            "unlocks newspapers, speeches, and everyday talk. The example "
            "sentences show each idiom in its natural habitat: advice, "
            "warning, or joke."
        ),
        "key_points": [
            "Sprichwoerter are compressed cultural wisdom, often rhyming and rhythmic.",
            "Never translate idioms literally into English: Da liegt der Hund begraben baffles.",
            "Core proverbs: Aller Anfang ist schwer, Uebung macht den Meister, Morgenstund hat Gold im Mund.",
            "Humor idioms: Alles hat ein Ende, nur die Wurst hat zwei.",
            "Recognizing the 20 core proverbs unlocks newspapers, speeches, and everyday talk.",
        ],
        "requirements": [
            "Recite all 20 idioms with literal translation and real meaning.",
            "Use five idioms correctly in original German sentences.",
            "Explain three idioms to an English speaker without translating literally.",
            "Identify the grammar quirk in Wer rastet, der rostet and Man soll den Tag nicht vor dem Abend loben.",
            "Write a short advice paragraph using three proverbs.",
        ],
        "standards": [
            "Proverbs are documented standard German Sprichwoerter.",
            "Meanings follow standard German idiom dictionaries.",
        ],
        "citations": [CIT_DUDEN, CIT_GRIMM],
        "sig_lens": (
            "The Signature read: proverbs are the signed ingots of the "
            "folk - each one assayed by centuries, stamped with rhyme so "
            "it cannot be counterfeited. Uebung macht den Meister is the "
            "Signature motto itself: the master is not born, he is "
            "practiced into being."
        ),
    },
    {
        "key": "registers",
        "name": "German Formal and Polite Registers",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen formal-versus-informal pairs with translations. 1. "
            "Formal: Wie geht es Ihnen? - Informal: Wie geht's? (How are "
            "you?) 2. Formal: Koennten Sie mir bitte helfen? - Informal: "
            "Kannst du mir helfen? (Could you help me?) 3. Formal: Ich "
            "haette gern einen Tisch fuer zwei. - Informal: Ich haette "
            "gern einen Tisch fuer zwei. (I would like a table for two - "
            "the phrase is polite in both; the Sie/du around it changes.) "
            "4. Formal: Wuerden Sie bitte Platz nehmen? - Informal: Setz "
            "dich bitte. (Please take a seat.) 5. Formal: Darf ich Sie "
            "etwas fragen? - Informal: Darf ich dich etwas fragen? (May I "
            "ask you something?) 6. Formal: Vielen Dank fuer Ihre Hilfe. - "
            "Informal: Danke fuer deine Hilfe. (Thank you for your help.) "
            "7. Formal: Entschuldigen Sie bitte die Stoerung. - Informal: "
            "Entschuldige die Stoerung. (Sorry for the disturbance.) 8. "
            "Formal: Ich wuensche Ihnen einen schoenen Tag. - Informal: "
            "Ich wuensche dir einen schoenen Tag. (Have a nice day.) 9. "
            "Formal: Koennten Sie das bitte wiederholen? - Informal: "
            "Kannst du das bitte wiederholen? (Could you repeat that?) 10. "
            "Formal: Es war mir ein Vergnuegen. - Informal: Hat Spass "
            "gemacht. (It was a pleasure. / That was fun.) 11. Formal "
            "letter opening: Sehr geehrte Frau Mueller, - Informal: Liebe "
            "Anna, (Dear Ms. Mueller, / Dear Anna,) 12. Formal letter "
            "closing: Mit freundlichen Gruessen - Informal: Viele Gruesse "
            "or Liebe Gruesse (Kind regards / Best wishes) 13. Formal: "
            "Ich freue mich auf Ihre Antwort. - Informal: Ich freue mich "
            "auf deine Antwort. (I look forward to your reply.) 14. "
            "Formal: Gestatten Sie, dass ich mich vorstelle? - Informal: "
            "Ich bin der Max. (May I introduce myself? / I am Max.) 15. "
            "Formal: Wuerden Sie mir bitte folgen? - Informal: Kommst du "
            "bitte mit? (Would you follow me, please? / Are you coming "
            "with me?) Register rules: strangers, customers, officials, "
            "and elders get Sie; friends, family, children, fellow "
            "students, and colleagues under about 30 get du. In doubt, "
            "use Sie - being too formal is forgiven, being too informal "
            "is not. Business letters never use du unless invited."
        ),
        "how_it_works": (
            "German registers work as a two-gear social transmission: Sie "
            "is the formal gear - capitalized pronoun, third-person "
            "plural verb forms (Kommen Sie, Haben Sie), Konjunktiv II "
            "requests (Koennten Sie) - and du is the informal gear - "
            "second-person forms (Kommst du, Hast du), direct imperatives. "
            "The shift between gears is itself a ritual: someone offers "
            "das Du an (offers the informal you), often with Wollen wir "
            "uns duzen? The letter formulas are fixed machinery: Sehr "
            "geehrte Damen und Herren opens the unknown formal letter; "
            "Mit freundlichen Gruessen closes it; Liebe Anna opens the "
            "friendly one. Email has relaxed the rules slightly - Viele "
            "Gruesse now passes in business - but the Sie/du line has not "
            "moved. The learner's survival rule: default to Sie with "
            "anyone over 30, any official, any customer; accept du "
            "gracefully when offered."
        ),
        "key_points": [
            "Sie: capitalized, third-person plural verbs, Konjunktiv II requests - the formal gear.",
            "Du: second-person verbs, direct imperatives - the informal gear for friends, family, peers.",
            "The shift is a ritual: Wollen wir uns duzen? (Shall we use du?)",
            "Letter machinery: Sehr geehrte Frau Mueller / Mit freundlichen Gruessen vs Liebe Anna / Viele Gruesse.",
            "In doubt, use Sie: too formal is forgiven, too informal is not.",
        ],
        "requirements": [
            "Convert all 15 pairs both directions from memory.",
            "Write a formal business email and an informal note to a friend.",
            "Explain the duzen ritual in three German sentences.",
            "List five situations demanding Sie and five allowing du.",
            "Role-play offering du to a colleague and accepting.",
        ],
        "standards": [
            "Address conventions follow standard German sociolinguistic usage.",
            "Business letter formulas follow standard German correspondence conventions.",
        ],
        "citations": [CIT_GOETHE, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: Sie and du are the two seals of German "
            "society - the great seal for the honored stranger, the "
            "private seal for the trusted friend. The Signature diplomat "
            "never breaks a seal early: Sie until invited, du ever after."
        ),
    },
    {
        "key": "complex",
        "name": "German Compound and Complex Sentences",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen long sentences with clauses, connectors, and relative "
            "clauses - parsed and translated. 1. Ich bleibe zu Hause, weil "
            "ich krank bin. (I am staying home because I am sick. - weil "
            "sends bin to the end.) 2. Er sagt, dass er morgen kommt. (He "
            "says that he is coming tomorrow. - dass clause, verb last.) "
            "3. Obwohl es regnet, gehen wir spazieren. (Although it is "
            "raining, we are going for a walk. - obwohl clause first, "
            "then inversion.) 4. Wenn ich Zeit habe, rufe ich dich an. (If "
            "I have time, I will call you. - wenn clause first, verb "
            "second in main clause.) 5. Die Frau, die dort steht, ist "
            "meine Lehrerin. (The woman who is standing there is my "
            "teacher. - relative clause with die, verb last.) 6. Das Buch, "
            "das du mir gegeben hast, ist spannend. (The book that you "
            "gave me is exciting. - relative clause in the middle.) 7. Ich "
            "weiss nicht, ob er kommt. (I do not know whether he is "
            "coming. - ob question clause.) 8. Je mehr du uebst, desto "
            "besser wirst du. (The more you practice, the better you get. "
            "- je/desto correlative.) 9. Er arbeitet, waehrend sie kocht. "
            "(He works while she cooks. - waehrend clause.) 10. Nachdem er "
            "gegessen hatte, ging er spazieren. (After he had eaten, he "
            "went for a walk. - nachdem with Plusquamperfekt.) 11. Bevor "
            "du gehst, ruf mich an. (Before you go, call me. - bevor "
            "clause first.) 12. Damit du es weisst: Der Zug faehrt um "
            "acht. (So that you know: the train leaves at eight. - damit "
            "purpose clause.) 13. Er ist so muede, dass er sofort "
            "einschlaeft. (He is so tired that he falls asleep immediately. "
            "- so/dass result clause.) 14. Anstatt zu arbeiten, spielte er "
            "Computerspiele. (Instead of working, he played computer "
            "games. - anstatt zu infinitive clause.) 15. Ohne ein Wort zu "
            "sagen, verliess er den Raum. (Without saying a word, he left "
            "the room. - ohne zu infinitive clause.)"
        ),
        "how_it_works": (
            "Complex German sentences work as verb-bracketing machines: "
            "subordinating conjunctions - weil, dass, obwohl, wenn, als, "
            "ob, waehrend, nachdem, bevor, damit, sodass - open a clause "
            "and the conjugated verb must close it at the very end, no "
            "matter how long the clause grows. This is why German "
            "sentences can feel like suspension bridges: the verb is the "
            "far tower. Relative pronouns (der, die, das, den, dem, "
            "dessen) agree in gender and number with their antecedent and "
            "take their case from their job inside the relative clause. "
            "Infinitive clauses with zu, um zu, anstatt zu, ohne zu keep "
            "the zu-infinitive at the end. The je/desto correlative is "
            "the elegant exception that inverts both clauses. The "
            "learner's drill: find the conjunction, hold the verb, and "
            "wait for the end."
        ),
        "key_points": [
            "Subordinating conjunctions send the conjugated verb to the end: weil, dass, obwohl, wenn, ob, waehrend, nachdem, bevor, damit.",
            "Main clause after a fronted subordinate clause inverts: Obwohl es regnet, gehen wir spazieren.",
            "Relative pronouns agree with the antecedent in gender/number, take case from their clause job.",
            "Infinitive clauses: zu, um zu, anstatt zu, ohne zu - infinitive at the end.",
            "Je/desto correlative: Je mehr du uebst, desto besser wirst du.",
        ],
        "requirements": [
            "Parse all 15 sentences: mark conjunction, clause boundaries, and verb positions.",
            "Join ten simple sentence pairs with weil, dass, obwohl, wenn, and als.",
            "Build five relative clauses with der/die/das in different cases.",
            "Write three je/desto sentences and three um zu purpose sentences.",
            "Explain verb-bracketing to a beginner in four sentences.",
        ],
        "standards": [
            "Subordinate clause word order follows the Duden standard grammar.",
            "Relative pronoun usage follows standard Hochdeutsch declension.",
        ],
        "citations": [CIT_DUDEN, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: the complex German sentence is a signed "
            "suspension bridge - the conjunction opens the span, the verb "
            "anchors the far tower, and everything hangs between. The "
            "Signature engineer never drops the far tower: hold the verb, "
            "wait for the end, and the bridge holds."
        ),
    },
]

ENTRIES += [
    {
        "key": "dialogue-market",
        "name": "German Conversation: At the Market",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue at a farmers market, "
            "annotated. 1. Verkaeufer: Guten Morgen! Was darf es sein? "
            "(Good morning! What may it be? - standard market greeting.) "
            "2. Kundin: Guten Morgen! Ich haette gern ein Kilo Aepfel. "
            "(Good morning! I would like a kilo of apples.) 3. Verkaeufer: "
            "Sehr gern. Diese hier sind besonders suess. (Gladly. These "
            "here are especially sweet.) 4. Kundin: Wie viel kosten sie? "
            "(How much are they?) 5. Verkaeufer: Zwei Euro fuenfzig das "
            "Kilo. (Two euros fifty per kilo.) 6. Kundin: Das ist guenstig. "
            "Geben Sie mir bitte auch ein halbes Kilo Birnen. (That is "
            "cheap. Please give me half a kilo of pears too.) 7. "
            "Verkaeufer: Die Birnen sind heute im Angebot. (The pears are "
            "on sale today.) 8. Kundin: Wunderbar. Haben Sie auch frische "
            "Kraeuter? (Wonderful. Do you also have fresh herbs?) 9. "
            "Verkaeufer: Ja, Petersilie, Schnittlauch und Basilikum. (Yes, "
            "parsley, chives, and basil.) 10. Kundin: Dann nehme ich einen "
            "Bund Petersilie. (Then I will take a bunch of parsley.) 11. "
            "Verkaeufer: Sonst noch etwas? (Anything else?) 12. Kundin: "
            "Nein, das ist alles. Was macht das zusammen? (No, that is "
            "all. What does that come to altogether?) 13. Verkaeufer: Das "
            "macht sechs Euro zwanzig. (That comes to six euros twenty.) "
            "14. Kundin: Kann ich mit Karte zahlen? (Can I pay by card?) "
            "15. Verkaeufer: Ja, natuerlich. (Yes, of course.) 16. Kundin: "
            "[bezahlt] Stimmt so. (Keep the change. - literally: it is "
            "right so.) 17. Verkaeufer: Vielen Dank! Auf Wiedersehen! "
            "(Thank you very much! Goodbye!) 18. Kundin: Danke, Ihnen auch "
            "einen schoenen Tag! (Thanks, have a nice day too!) 19. "
            "Verkaeufer: [zur naechsten Kundin] Der Naechste, bitte! (Next, "
            "please!) 20. Kundin: [geht] Die Aepfel duften herrlich. (The "
            "apples smell wonderful.)"
        ),
        "how_it_works": (
            "This dialogue works as the complete market transaction in "
            "twenty lines: greeting (Was darf es sein?), request with "
            "haette gern, price negotiation (Wie viel kosten sie?), "
            "add-ons (Sonst noch etwas?), totaling (Was macht das "
            "zusammen?), payment (mit Karte), change etiquette (Stimmt "
            "so), and farewell. The grammar on display: the polite "
            "Konjunktiv II of commerce (Ich haette gern), accusative "
            "quantities (ein Kilo Aepfel, einen Bund Petersilie), the "
            "demonstrative diese hier, and the impersonal was macht das. "
            "Cultural notes: market sellers expect a greeting first; "
            "Stimmt so rounds up the payment as a tip; produce is weighed "
            "and priced per Kilo or per Stueck. The learner performs this "
            "dialogue aloud with a partner, swapping roles, until the "
            "market German is automatic."
        ),
        "key_points": [
            "Market opening: Was darf es sein? - the standard seller greeting.",
            "Requests run on Ich haette gern + accusative quantities: ein Kilo Aepfel.",
            "Totals: Was macht das zusammen? Das macht sechs Euro zwanzig.",
            "Stimmt so means keep the change; produce is priced per Kilo or Stueck.",
            "Twenty lines cover the full transaction: greeting to farewell.",
        ],
        "requirements": [
            "Perform the dialogue aloud with a partner, swapping roles.",
            "Translate all 20 lines both directions from memory.",
            "Buy three different items at a market stall in a role-play.",
            "Explain Stimmt so and Sonst noch etwas in two sentences each.",
            "Write a six-line market dialogue of your own.",
        ],
        "standards": [
            "Market vocabulary and formulas follow standard German usage.",
            "Politeness forms follow standard Sie-address conventions.",
        ],
        "citations": [CIT_DUDEN, CIT_GOETHE],
        "sig_lens": (
            "The Signature read: the market dialogue is the signed "
            "transaction - greeting the opening seal, haette gern the "
            "stamped request, Stimmt so the generous final seal. The "
            "Signature buyer greets first, asks plainly, and tips with "
            "the rounding."
        ),
    },
    {
        "key": "dialogue-friend",
        "name": "German Conversation: Meeting a Friend",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue between friends, annotated. "
            "1. Jonas: Hey, Lena! Lange nicht gesehen! (Hey, Lena! Long "
            "time no see!) 2. Lena: Jonas! Wie geht's? (Jonas! How are "
            "you?) 3. Jonas: Gut, danke! Und dir? (Good, thanks! And you?) "
            "4. Lena: Mir geht's super. Ich habe einen neuen Job. (I am "
            "great. I have a new job.) 5. Jonas: Echt? Erzaehl! (Really? "
            "Tell me!) 6. Lena: Ich arbeite jetzt in einer Buchhandlung. "
            "(I work in a bookstore now.) 7. Jonas: Cool! Das passt zu "
            "dir. (Cool! That suits you.) 8. Lena: Ja, ich liebe Buecher. "
            "Was machst du so? (Yes, I love books. What are you up to?) 9. "
            "Jonas: Ich studiere noch und jobbe nebenbei. (I am still "
            "studying and working on the side.) 10. Lena: Hast du Lust, am "
            "Samstag einen Kaffee zu trinken? (Do you feel like having a "
            "coffee on Saturday?) 11. Jonas: Sehr gern! Wann und wo? (Very "
            "gladly! When and where?) 12. Lena: Um drei im Cafe am Markt. "
            "(At three at the cafe on the market square.) 13. Jonas: "
            "Perfekt, ich bin da. (Perfect, I will be there.) 14. Lena: "
            "Bringst du deine Gitarre mit? (Are you bringing your guitar?) "
            "15. Jonas: Klar! Dann spielen wir etwas. (Of course! Then we "
            "will play something.) 16. Lena: Ich freue mich schon. (I am "
            "already looking forward to it.) 17. Jonas: Ich mich auch. Bis "
            "Samstag! (Me too. See you Saturday!) 18. Lena: Bis dann! "
            "Gruess deine Schwester von mir! (See you then! Say hi to your "
            "sister for me!) 19. Jonas: Mach ich! Tschuess! (Will do! "
            "Bye!) 20. Lena: Tschuess! (Bye!)"
        ),
        "how_it_works": (
            "This dialogue works as the du-register in full flight: "
            "informal greetings (Hey, Wie geht's), interjections (Echt? "
            "Cool! Klar!), separable verbs of social life (sich treffen "
            "is implied, mitbringen appears as mit), and the invitation "
            "machinery (Hast du Lust, Wann und wo, Bis Samstag). The "
            "grammar on display: present tense for the near future (ich "
            "bin da), the accusative of time (am Samstag), modal verbs of "
            "willingness (Willst du mitkommen is implied in the "
            "invitation), and reflexive sich freuen with auf for looking "
            "forward. Cultural notes: Lange nicht gesehen is the reunion "
            "formula; Gruess deine Schwester von mir sends regards through "
            "the friend; Mach ich is the casual promise. The learner "
            "performs it until the du-music sounds natural."
        ),
        "key_points": [
            "Friend register: Hey, Wie geht's, Echt?, Cool!, Klar!, Mach ich!",
            "Reunion formula: Lange nicht gesehen!",
            "Invitation machinery: Hast du Lust, Wann und wo, Bis Samstag.",
            "Sich freuen auf for looking forward; Gruess X von mir sends regards.",
            "Present tense covers the near future: ich bin da.",
        ],
        "requirements": [
            "Perform the dialogue aloud with a partner, swapping roles.",
            "Translate all 20 lines both directions.",
            "Plan a weekend with a friend in an eight-line dialogue.",
            "Explain three interjections (Echt?, Klar!, Mach ich!) in context.",
            "Write a reunion dialogue using Lange nicht gesehen.",
        ],
        "standards": [
            "Informal dialogue follows standard German du-register conventions.",
            "Youth and casual expressions follow current standard usage.",
        ],
        "citations": [CIT_GOETHE, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: the friend dialogue is the signed circle "
            "unbroken - du the inner seal, Lange nicht gesehen the "
            "re-stamping, Bis Samstag the dated promise. The Signature "
            "friend keeps promises the way Mach ich keeps them: short, "
            "certain, kept."
        ),
    },
    {
        "key": "dialogue-problem",
        "name": "German Conversation: Solving a Problem",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue solving a problem, "
            "annotated. 1. Herr Weber: Guten Tag, womit kann ich Ihnen "
            "helfen? (Good day, how can I help you? - formal service "
            "opening.) 2. Frau Klein: Guten Tag. Mein Internet "
            "funktioniert nicht mehr. (Good day. My internet no longer "
            "works.) 3. Herr Weber: Seit wann besteht das Problem? (Since "
            "when has the problem existed?) 4. Frau Klein: Seit gestern "
            "Abend. (Since yesterday evening.) 5. Herr Weber: Haben Sie "
            "den Router schon neu gestartet? (Have you already restarted "
            "the router?) 6. Frau Klein: Ja, zweimal. Es hat nichts "
            "gebracht. (Yes, twice. It did not help.) 7. Herr Weber: "
            "Leuchtet die Lampe am Router? (Is the light on the router "
            "on?) 8. Frau Klein: Nein, sie blinkt rot. (No, it is blinking "
            "red.) 9. Herr Weber: Das deutet auf eine Stoerung hin. Ich "
            "pruefe die Leitung. (That points to an outage. I will check "
            "the line.) 10. Frau Klein: Wie lange wird das dauern? (How "
            "long will that take?) 11. Herr Weber: Einen Moment, bitte. "
            "[prueft] Es gibt eine Stoerung in Ihrer Strasse. (One moment, "
            "please. There is an outage on your street.) 12. Frau Klein: "
            "Ach so. Wann wird es behoben? (I see. When will it be fixed?) "
            "13. Herr Weber: Der Techniker kommt heute Nachmittag. (The "
            "technician is coming this afternoon.) 14. Frau Klein: Muss "
            "ich zu Hause sein? (Do I have to be home?) 15. Herr Weber: "
            "Nein, die Stoerung liegt ausserhalb. (No, the fault is "
            "outside.) 16. Frau Klein: Gut. Bekomme ich eine "
            "Gutschrift? (Good. Will I get a credit?) 17. Herr Weber: Ja, "
            "fuer den Ausfall schreiben wir Ihnen zwei Tage gut. (Yes, we "
            "will credit you two days for the outage.) 18. Frau Klein: "
            "Vielen Dank fuer Ihre Hilfe. (Thank you very much for your "
            "help.) 19. Herr Weber: Gern geschehen. Auf Wiederhoeren! "
            "(You are welcome. Goodbye on the phone!) 20. Frau Klein: "
            "Wiederhoeren! (Goodbye!)"
        ),
        "how_it_works": (
            "This dialogue works as the formal problem-solving register: "
            "Sie throughout, Konjunktiv II politeness (womit kann ich "
            "Ihnen helfen), the diagnostic question chain (Seit wann? "
            "Haben Sie schon? Leuchtet die Lampe?), and the passive voice "
            "of resolutions (Es wird behoben, wird gutgeschrieben). The "
            "grammar on display: seit plus dative for duration, the "
            "Perfekt for completed troubleshooting (hat nichts gebracht), "
            "and the future passive for the fix. Cultural notes: German "
            "service expects the problem stated first, troubleshooting "
            "steps already tried, and precise answers; Auf Wiederhoeren "
            "is the telephone goodbye; Gutschrift is the standard "
            "compensation word. The learner who can run this dialogue can "
            "handle any German hotline."
        ),
        "key_points": [
            "Service opening: Womit kann ich Ihnen helfen? - formal throughout.",
            "Diagnostic chain: Seit wann? Haben Sie schon? Leuchtet die Lampe?",
            "Seit + dative for duration: Seit gestern Abend.",
            "Resolutions use future passive: Es wird behoben; credit is Gutschrift.",
            "Telephone goodbye is Auf Wiederhoeren, not Auf Wiedersehen.",
        ],
        "requirements": [
            "Perform the dialogue aloud, swapping roles.",
            "Translate all 20 lines both directions.",
            "Report a different problem (heating, water, phone) in six lines.",
            "Explain seit + dative with three examples.",
            "Write a complaint email requesting a Gutschrift.",
        ],
        "standards": [
            "Service dialogue follows standard German formal conventions.",
            "Technical vocabulary follows standard Hochdeutsch usage.",
        ],
        "citations": [CIT_DUDEN, CIT_GOETHE],
        "sig_lens": (
            "The Signature read: the problem dialogue is the signed "
            "troubleshooting protocol - symptom first, history second, "
            "diagnosis third, resolution sealed with the Gutschrift. The "
            "Signature technician never guesses: Seit wann, schon "
            "probiert, Lampe pruefen - the three stamps before the "
            "verdict."
        ),
    },
    {
        "key": "mastery",
        "name": "German Mastery Review and Full Reference",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The whole database in one teaching summary. ALPHABET: 26 "
            "letters A-Z plus Ae, Oe, Ue and the sharp s (30 total); "
            "Swiss German writes ss instead of the sharp s; all nouns "
            "capitalized. SOUNDS: short-long vowel pairs; ie is long i; "
            "ei like my, eu like boy, au like house; w like v, v like f, "
            "z like ts, j like y; ch soft after front vowels (ich), throaty "
            "after back vowels (ach); stress on the first syllable. CORE "
            "WORDS (200): people - Mann, Frau, Kind, Vater, Mutter, "
            "Bruder, Schwester, Freund, Familie, Baby; home - Haus, "
            "Wohnung, Zimmer, Kueche, Bad, Tisch, Stuhl, Bett, Tuer, "
            "Fenster; food - Brot, Wasser, Milch, Kaffee, Tee, Apfel, "
            "Kartoffel, Fleisch, Fisch, Kaese; body - Kopf, Auge, Nase, "
            "Mund, Hand, Fuss, Herz, Ruecken, Arm, Bein; nature - Baum, "
            "Blume, Sonne, Mond, Stern, Wasser, Berg, Fluss, Wald, Tier; "
            "time - Tag, Nacht, Morgen, Abend, Woche, Monat, Jahr, Stunde, "
            "Minute, Zeit; verbs - sein, haben, werden, koennen, muessen, "
            "wollen, machen, gehen, kommen, sehen, sprechen, lernen, lesen, "
            "schreiben, essen, trinken, schlafen, arbeiten, spielen, "
            "fragen, kaufen, verkaufen, helfen, danken, wohnen, stehen, "
            "sitzen, liegen, geben, nehmen; adjectives - gut, schlecht, "
            "gross, klein, neu, alt, jung, schoen, schnell, langsam, warm, "
            "kalt, heiss, hell, dunkel, teuer, billig, lang, kurz, hoch, "
            "tief, stark, schwach, wichtig, richtig; adverbs and function "
            "words - sehr, viel, wenig, oft, immer, nie, heute, morgen, "
            "hier, dort, auch, nur, schon, noch, gern, bitte, danke, ja, "
            "nein, nicht, kein, und, oder, aber, weil, dass, wenn, als, "
            "mit, ohne, fuer, zu, nach, von, aus, in, an, auf, "
            "ueber, vor, hinter, neben, zwischen; pronouns - ich, "
            "du, er, sie, es, wir, ihr, sie, Sie, mich, dich, ihn, uns, "
            "mir, dir, ihm, mein, dein, sein, ihr, unser, "
            "dieser, wer, was, wo, wann, warum, wie; numbers "
            "- eins, zwei, drei, vier, fuenf, sechs, sieben, acht, neun, "
            "zehn, elf, zwoelf, zwanzig, hundert. GRAMMAR CORE: verb-second in main clauses, verb-first "
            "in yes/no questions, verb-last in subordinate clauses; three "
            "genders (der/die/das), four cases (nominative, accusative, "
            "dative, genitive); present endings -e/-st/-t/-en/-t/-en; "
            "Perfekt with haben/sein; modal verbs send the infinitive to "
            "the end; separable verbs split; nicht negates verbs, kein "
            "negates nouns; du informal, Sie formal. PHRASE TABLES: "
            "greetings - Guten Morgen/Tag/Abend, Hallo, Tschuess, Auf "
            "Wiedersehen; politeness - bitte, danke, Entschuldigung, Es "
            "tut mir leid; restaurant - Die Rechnung bitte, Guten Appetit, "
            "Ich haette gern; travel - Wo ist, Eine Fahrkarte nach, Wie "
            "viel kostet das; emergency - Hilfe, Ich brauche einen Arzt, "
            "Rufen Sie einen Krankenwagen. The ladder path: overview (1), "
            "script (2), sounds (3), words (4-9), grammar engine (10), "
            "life domains (11-20), tense mastery (21), interaction (22-24), "
            "stories (25-27), culture (28-29), complex syntax (30), "
            "dialogues (31-33), this review (34)."
        ),
        "how_it_works": (
            "This review works as the database's capstone and quick-"
            "reference: the alphabet in one line, the sound rules in one "
            "paragraph, 200 core words organized by domain, the grammar "
            "engine in one block, and the survival phrases in tables. The "
            "200 words are the learner's working vocabulary - with them "
            "plus the grammar core, the learner can build thousands of "
            "correct sentences, since German compounds and conjugates "
            "freely from these roots. The ladder path at the end maps the "
            "whole journey from record 1 to record 34, so the learner can "
            "revisit any rung. The review is also the self-test: cover "
            "the English, read the German, and any gap sends the learner "
            "back to that record. Mastery is not memorizing this page - "
            "it is being able to rebuild it from memory."
        ),
        "key_points": [
            "30 letters, regular sounds, capitalized nouns - the script in three facts.",
            "200 core words by domain: people, home, food, body, nature, time, verbs, adjectives, function words, pronouns, numbers.",
            "Grammar engine: V2/V1/V-last, 3 genders, 4 cases, -e/-st/-t/-en/-t/-en, haben/sein Perfekt, modals to the end.",
            "Survival phrase tables: greetings, politeness, restaurant, travel, emergency.",
            "The ladder path maps records 1-34 for review and self-testing.",
        ],
        "requirements": [
            "Recite the 200 core words with articles and English meanings.",
            "Write the grammar core from memory: word order, cases, endings, negation, address.",
            "Hold a five-minute conversation using only the phrase tables.",
            "Retell all three stories from memory.",
            "Use ten idioms correctly in a written paragraph.",
        ],
        "standards": [
            "Reference content consolidates the Duden-standard material of records 1-33.",
            "Core word selection follows standard frequency lists for German learners.",
        ],
        "citations": [CIT_DUDEN, CIT_ETHNO, CIT_GOETHE, CIT_HAMMER],
        "sig_lens": (
            "The Signature read: the mastery review is the signed vault "
            "inventory - thirty letters, two hundred words, one grammar "
            "engine, counted and stamped. The Signature master does not "
            "carry the vault on his back; he carries the inventory in his "
            "head and rebuilds the vault anywhere."
        ),
    },
]
