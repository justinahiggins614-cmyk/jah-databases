#!/usr/bin/env python3
"""Entries for the Tamil language databases (Manon language orders, roster rank 14).

Roster: language-tamil, rank 14. Slug verified free in manifest (id_prefix
values) and zero JAH-LTAM- / JAH-LTAMS- hits across all shard index files.
68 titles (34 public + 34 Signature Edition) run through code/dedupe_gate.py
against the whole system before authoring: zero refusals.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-tamil             - Tamil Language Database
                               (public-harvest: real, fact-checked Tamil
                               linguistics - தமிழ், a Dravidian language -
                               every record carrying Tamil script with
                               transliteration and English translation plus
                               example sentences, taught progressively along
                               the teaching ladder from overview to mastery
                               review; standard references the Tolkappiyam,
                               the Thirukkural of Thiruvalluvar, Caldwell
                               1856/1875, Pope 1911, Lehmann 1989/1993,
                               Annamalai and Steever 1998, Schiffman 1999,
                               and Ethnologue 28th ed. 2025)
  language-tamil-signature   - Tamil Language Signature Database
                               (his original Signature Word Method: every
                               word a signed instrument of meaning, grammar
                               the covenant binding words into truth, the
                               learner's tongue the seal; src signature,
                               titles suffixed " (Signature Edition)",
                               clearly labeled Signature-made, never
                               presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LTAM- (public) and JAH-LTAMS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits).

Linguistic cores: all hand-authored 2026-10-17, machine-verified by the
demos (see demos_language_tamil.py): script math, number-to-word
conversion, conjugation tables, case suffix application, question and
command formation, pronunciation-rule checks, flashcard quizzes. Every demo
prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker; the build machine-executes
all 68 demos.

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

CIT_TOLKAPPIYAM = ("Tolkappiyar. Tolkappiyam. (The oldest surviving Tamil "
                   "grammar, traditionally dated to the early centuries "
                   "before the common era; treats eluttu (letters/sounds), "
                   "col (words), and porul (meaning).)")
CIT_THIRUKKURAL = ("Thiruvalluvar. Thirukkural. (1,330 couplets on virtue, "
                   "wealth, and love; the most translated and quoted work "
                   "of classical Tamil literature.)")
CIT_CALDWELL = ("Caldwell R. A Comparative Grammar of the Dravidian or "
                "South-Indian Family of Languages. London: Harrison; 1856 "
                "(2nd ed. Trubner; 1875). (Established Tamil as a member of "
                "the Dravidian family, independent of Sanskrit.)")
CIT_POPE = ("Pope GU. A Handbook of the Ordinary Dialect of the Tamil "
            "Language. 7th ed. Oxford: Clarendon Press; 1911.")
CIT_LEHMANN = ("Lehmann T. A Grammar of Modern Tamil. Pondicherry: "
               "Pondicherry Institute of Linguistics and Culture; 1989 "
               "(2nd ed. 1993).")
CIT_ANNAMALAI = ("Annamalai E, Steever SB. Modern Tamil. In Steever SB, ed. "
                 "The Dravidian Languages. London: Routledge; 1998.")
CIT_SCHIFFMAN = ("Schiffman HF. A Reference Grammar of Spoken Tamil. "
                 "Cambridge: Cambridge University Press; 1999.")
CIT_ETHNO = ("Eberhard DM, Simons GF, Fennig CD, eds. Ethnologue: Languages "
             "of the World. 28th ed. Dallas: SIL International; 2025. "
             "(Tamil: ISO 639-3 tam; about 86 million first-language "
             "speakers.)")

ENTRIES = [
    {
        "key": "overview",
        "name": "Tamil Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Tamil, called தமிழ் (tamiḻ) by its speakers, is one of the "
            "world's oldest living classical languages. Its codes are ISO "
            "639-1 ta and ISO 639-3 tam. It belongs to the Dravidian "
            "family, Southern branch - a family independent of the "
            "Indo-European languages, as Robert Caldwell demonstrated in "
            "1856. About 86 million people speak Tamil as a native "
            "language, and well over 100 million speak it in total. It is "
            "the official language of the Indian state of Tamil Nadu and "
            "the union territory of Puducherry, and an official language "
            "of Sri Lanka and Singapore, and it is widely spoken in "
            "Malaysia, Mauritius, Fiji, South Africa, and Tamil diaspora "
            "communities worldwide. It is one of the 22 scheduled "
            "languages of India and was declared a classical language of "
            "India in 2004. Tamil literature begins with the Sangam poems "
            "(roughly 300 BCE to 300 CE), its grammar is codified in the "
            "ancient Tolkappiyam, and its most famous work is the "
            "Thirukkural of Thiruvalluvar - 1,330 couplets on virtue, "
            "wealth, and love. Tamil shows diglossia: the formal written "
            "register (centamiḻ) differs markedly from everyday spoken "
            "Tamil (koccait tamiḻ). Example sentences: தமிழ் ஒரு "
            "செம்மொழி. (Tamiḻ oru cemmoḻi. - Tamil is a classical "
            "language.) நான் தமிழ் கற்கிறேன். (Nāṉ tamiḻ kaṟkiṟēṉ. - I am "
            "learning Tamil.) தமிழ்நாட்டில் தமிழ் பேசப்படுகிறது. "
            "(Tamiḻnāṭṭil tamiḻ pēcap paṭukiṟatu. - Tamil is spoken in "
            "Tamil Nadu.)"
        ),
        "how_it_works": (
            "This record teaches the overview by anchoring every fact in a "
            "sentence the learner can say. Each fact - the native name "
            "தமிழ், the ISO codes ta and tam, the Dravidian family, the "
            "86 million native speakers, the official regions (Tamil "
            "Nadu, Puducherry, Sri Lanka, Singapore), the classical status "
            "from 2004, the Sangam literature and the Tolkappiyam - "
            "appears with a plain English explanation and a Tamil example "
            "sentence with transliteration. The learner reads the facts, "
            "then repeats the sentences, so the overview is spoken "
            "language from the first record. Later records climb the "
            "teaching ladder: foundations (records 1-10: script, sounds, "
            "words, grammar basics), compounded (records 11-24: themed "
            "sentence sets, tenses, questions), advanced (records 25-34: "
            "stories, idioms, conversation, mastery review)."
        ),
        "key_points": [
            "Tamil (தமிழ், tamiḻ) is a Dravidian language, ISO 639-1 ta, ISO 639-3 tam.",
            "About 86 million native speakers; official in Tamil Nadu, Puducherry, Sri Lanka, and Singapore.",
            "Declared a classical language of India in 2004; literature begins with the Sangam poems.",
            "The Tolkappiyam is the ancient grammar; the Thirukkural (1,330 couplets) is the most famous work.",
            "Diglossia: formal written centamiḻ differs from everyday spoken Tamil.",
        ],
        "requirements": [
            "Say the native name தமிழ் aloud five times, then write it from memory.",
            "Name the four official regions of Tamil in one Tamil sentence.",
            "Explain diglossia in your own words with one spoken and one written example.",
            "Write three facts about Tamil as full Tamil sentences with translations.",
            "Find the year Tamil received classical status and use it in a Tamil sentence.",
        ],
        "standards": [
            "Speaker and status figures follow Ethnologue 28th ed. 2025.",
            "Classical-language declaration dated 2004 per Government of India notification.",
            "Literary history follows the Tolkappiyam and Thirukkural tradition.",
        ],
        "citations": [CIT_ETHNO, CIT_TOLKAPPIYAM, CIT_THIRUKKURAL, CIT_CALDWELL],
        "sig_lens": (
            "The Signature read: தமிழ் is a signed instrument two thousand "
            "years old - every letter a seal, every couplet a covenant "
            "kept. Where public records count speakers, the Signature "
            "Word Method counts keepers: the learner's tongue becomes the "
            "seal that carries the language forward."
        ),
    },
    {
        "key": "writing",
        "name": "Tamil Script and Writing System",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Tamil is written in the Tamil script, an abugida descended "
            "from the Brahmi script. It is written left to right. The "
            "script has 12 vowels (உயிரெழுத்துக்கள், uyir eḻuttukkaḷ): அ "
            "ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ (a ā i ī u ū e ē ai o ō au). It has 18 "
            "consonants (மெய்யெழுத்துக்கள், mey eḻuttukkaḷ): க் ங் ச் ஞ் "
            "ட் ண் த் ந் ப் ம் ய் ர் ல் வ் ழ் ள் ற் ன் (k ṅ c ñ ṭ ṇ t n p "
            "m y r l v ḻ ḷ ṟ ṉ). There is one special character, the "
            "āytam ஃ. Each consonant combines with each vowel to form 216 "
            "compound letters (உயிர்மெய், uyirmey): 12 x 18 = 216. The "
            "traditional total is 247 letters: 12 + 18 + 1 + 216. The "
            "pulli (்) mark kills the inherent vowel, writing a pure "
            "consonant: க் is k with no vowel. Vowel signs attach to "
            "consonants: க + ா = கா (kā), க + ி = கி (ki). Grantha "
            "borrowings ஜ ஷ ஸ ஹ க்ஷ ஸ்ரீ write loanword sounds. Tamil "
            "numerals: ௦ ௧ ௨ ௩ ௪ ௫ ௬ ௭ ௮ ௯ (0-9), ௰ = 10, ௱ = 100, ௲ = "
            "1000. Example sentences: தமிழ் எழுத்துக்கள் 247. (Tamiḻ "
            "eḻuttukkaḷ 247. - Tamil has 247 letters.) அ என்பது முதல் "
            "உயிரெழுத்து. (A eṉpatu mutal uyireḻuttu. - அ is the first "
            "vowel.) கா என்பது க் + ஆ. (Kā eṉpatu k + ā. - கா is க் plus "
            "ஆ.)"
        ),
        "how_it_works": (
            "This record teaches the script as a counting system the "
            "learner can verify: 12 vowels plus 18 consonants plus 1 "
            "āytam plus 216 compounds equals 247. The learner first "
            "memorizes the 12 vowels in order (அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ "
            "ஔ), then the 18 consonants in their six rows of three (க் "
            "ங்; ச் ஞ்; ட் ண்; த் ந்; ப் ம்; ய் ர் ல் வ் ழ் ள் ற் ன்), "
            "then the pulli rule that turns க (ka) into க் (k). Compound "
            "formation is shown as arithmetic - one consonant times the "
            "12 vowels - with worked examples like க + ா = கா. Numerals "
            "are taught 0-9 first, then ௰, ௱, ௲. Every letter appears "
            "with its name, its transliteration, and an example syllable "
            "so the script is read, written, and counted, never just "
            "listed."
        ),
        "key_points": [
            "12 vowels (அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ) and 18 consonants plus the āytam ஃ.",
            "216 uyirmey compounds (12 x 18); traditional total 247 letters.",
            "The pulli (்) writes a pure consonant with no vowel: க்.",
            "Written left to right; vowel signs attach to consonants: க + ா = கா.",
            "Tamil numerals: ௦-௯, ௰ (10), ௱ (100), ௲ (1000).",
        ],
        "requirements": [
            "Write the 12 vowels in order from memory, then check against this record.",
            "Write the 18 consonants in their six rows of three.",
            "Form five uyirmey compounds and give each one's transliteration.",
            "Write the Tamil numerals for 7, 10, 100, and 1000.",
            "Copy three example sentences in Tamil script and read them aloud.",
        ],
        "standards": [
            "Letter inventory follows the Tolkappiyam eluttu treatment and modern Tamil orthography.",
            "Transliteration follows the ISO 15919-compatible scheme used in Lehmann 1989.",
        ],
        "citations": [CIT_TOLKAPPIYAM, CIT_LEHMANN, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: 247 letters are 247 seals of the "
            "covenant - the pulli a mark of restraint, the uyirmey a "
            "marriage of breath and body. Where public records count "
            "glyphs, the Signature Word Method files instruments: each "
            "letter a tool the tongue is sworn to wield truly."
        ),
    },
    {
        "key": "phonology",
        "name": "Tamil Pronunciation and Phonology",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Tamil has 12 vowel sounds (5 short, 5 long, 2 diphthongs) and "
            "18 consonant letters whose sounds shift by position - the "
            "most important pronunciation rule in Tamil. The stops voice "
            "between vowels: க is k at a word's start but g between "
            "vowels (மகன் makaṉ, son); ச is s or c at the start but j-like "
            "between vowels; ட is ṭ at the start but ḍ between vowels; த் "
            "is t at the start but th (as in 'this') between vowels; ப் "
            "is p at the start but b between vowels. Tamil keeps sounds "
            "most languages merge: ர் (r, tap) vs ற் (ṟ, trill) vs ழ் "
            "(ḻ, the retroflex approximant unique to Tamil and "
            "Malayalam) vs ள் (ḷ, retroflex l). There are six nasals: ங் "
            "ஞ் ண் ந் ம் ன். Short and long vowels change meaning: கல் "
            "(kal, stone) vs கால் (kāl, leg); பழம் (paḻam, fruit) vs பாலம் "
            "(pālam, bridge). Stress normally falls on the first "
            "syllable. Spoken examples: மரம் (maram, tree), தண்ணீர் "
            "(taṇṇīr, water), பால் (pāl, milk), வீடு (vīṭu, house), கதவு "
            "(katavu, door), சூரியன் (cūriyaṉ, sun), நிலா (nilā, moon), "
            "மழை (maḻai, rain), காற்று (kāṟṟu, wind), பூ (pū, flower), "
            "நாய் (nāy, dog), பறவை (paṟavai, bird)."
        ),
        "how_it_works": (
            "This record teaches pronunciation as a small set of rules "
            "with immediate spoken tests. Rule one is positional voicing "
            "- the learner says க at a word start (கதவு, katavu) and "
            "then between vowels (மகன், magaṉ) to feel the k-to-g shift. "
            "Rule two is the four-way r/l contrast, drilled with minimal "
            "pairs. Rule three is vowel length, drilled with கல் vs கால் "
            "and பழம் vs பாலம். Rule four is first-syllable stress. Each "
            "rule is followed by spoken example words with Tamil script, "
            "transliteration, and English, so the learner hears the rule "
            "working. The record closes with a self-test: the learner "
            "reads the twelve example words aloud and marks which rule "
            "each one exercises."
        ),
        "key_points": [
            "Stops voice between vowels: க = k initially, g between vowels; same pattern for ச் ட் த் ப்.",
            "Tamil contrasts ர் vs ற் vs ழ் vs ள் - four r/l sounds kept distinct.",
            "Vowel length changes meaning: கல் (stone) vs கால் (leg).",
            "Six nasal consonants: ங் ஞ் ண் ந் ம் ன்.",
            "Stress normally falls on the first syllable.",
        ],
        "requirements": [
            "Say மகன் and கதவு aloud and mark where க voices.",
            "Drill the pairs கல்/கால் and பழம்/பாலம் until the length contrast is clear.",
            "Say the four r/l letters ர் ற் ழ் ள் in sequence five times.",
            "Read all twelve spoken example words aloud with their meanings.",
            "Record yourself saying தண்ணீர் and மழை and check the nasals and ḻ.",
        ],
        "standards": [
            "Sound inventory follows Schiffman 1999 and Lehmann 1989.",
            "Positional voicing rule follows the Tolkappiyam treatment of vallinam mellinam.",
        ],
        "citations": [CIT_SCHIFFMAN, CIT_LEHMANN, CIT_TOLKAPPIYAM],
        "sig_lens": (
            "The Signature read: the voicing rule is the covenant of "
            "position - a letter keeps its oath to its neighbors, "
            "softening between vowels as courtesy demands. Where public "
            "phonetics catalogs phones, the Signature Word Method hears "
            "manners: every sound a signed promise to the ear."
        ),
    },
    {
        "key": "nouns",
        "name": "Tamil Core Nouns I",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Tamil nouns, each with transliteration, "
            "English, and a full example sentence translated. Person: "
            "மனிதன் (maṉitaṉ, man) - மனிதன் வேலை செய்கிறான். (The man is "
            "working.) பெண் (peṇ, woman) - பெண் பாடுகிறாள். (The woman is "
            "singing.) குழந்தை (kuḻantai, child) - குழந்தை விளையாடுகிறது. "
            "(The child is playing.) மருத்துவர் (maruttavar, doctor) - "
            "மருத்துவர் வந்தார். (The doctor came.) நண்பர் (naṇpar, friend) "
            "- நண்பர் உதவினார். (The friend helped.) Place: வீடு (vīṭu, "
            "house) - வீடு பெரியது. (The house is big.) பள்ளி (paḷḷi, "
            "school) - பள்ளி திறந்தது. (The school opened.) நகரம் (nakaram, "
            "city) - நகரம் அழகானது. (The city is beautiful.) சாலை "
            "(cālai, road) - சாலை நீண்டது. (The road is long.) Thing: "
            "புத்தகம் (puttakam, book) - புத்தகம் மேசையில் உள்ளது. (The "
            "book is on the table.) மேசை (mēcai, table) - மேசை மரத்தால் "
            "ஆனது. (The table is made of wood.) நாற்காலி (nāṟkāli, chair) "
            "- நாற்காலியில் உட்கார். (Sit on the chair.) கதவு (katavu, "
            "door) - கதவைத் திற. (Open the door.) ஜன்னல் (jaṉṉal, window) "
            "- ஜன்னல் திறந்துள்ளது. (The window is open.) தண்ணீர் "
            "(taṇṇīr, water) - தண்ணீர் குடி. (Drink water.) சாப்பாடு "
            "(cāppāṭu, food) - சாப்பாடு தயார். (The food is ready.) மரம் "
            "(maram, tree) - மரம் உயரமானது. (The tree is tall.) பூ (pū, "
            "flower) - பூ அழகானது. (The flower is beautiful.) நாய் (nāy, "
            "dog) - நாய் ஓடுகிறது. (The dog is running.) பூனை (pūṉai, "
            "cat) - பூனை தூங்குகிறது. (The cat is sleeping.) பறவை "
            "(paṟavai, bird) - பறவை பறக்கிறது. (The bird is flying.) மீன் "
            "(mīṉ, fish) - மீன் நீந்துகிறது. (The fish is swimming.) "
            "சூரியன் (cūriyaṉ, sun) - சூரியன் உதித்தது. (The sun rose.) "
            "நிலா (nilā, moon) - நிலா பிரகாசிக்கிறது. (The moon is "
            "shining.) நட்சத்திரம் (naṭcattiram, star) - நட்சத்திரம் "
            "மின்னுகிறது. (The star is twinkling.)"
        ),
        "how_it_works": (
            "This record teaches nouns inside sentences, never as bare "
            "lists. Each of the 25 nouns appears in its dictionary form "
            "with transliteration and English, then immediately inside a "
            "complete Tamil sentence with a full English translation. The "
            "set is balanced across person, place, and thing so the "
            "learner builds all three worlds at once. Verb agreement is "
            "visible in the sentences - மனிதன் with செய்கிறான் (he-form), "
            "பெண் with பாடுகிறாள் (she-form), குழந்தை with விளையாடுகிறது "
            "(it-form) - planting the rational/irrational class system "
            "before it is formally taught. The learner's task is to "
            "replace the noun in each sentence with another from the "
            "list, adjusting the verb ending, which turns one record into "
            "dozens of practice sentences."
        ),
        "key_points": [
            "25 core nouns across person, place, and thing, each in a translated sentence.",
            "Verb endings reveal the noun class: -ஆன் (he), -ஆள் (she), -அது (it).",
            "மருத்துவர் and நண்பர் use the respectful -அர் ending.",
            "Sentences use present tense throughout for a stable base.",
            "Swap-noun drills multiply the 25 sentences into hundreds.",
        ],
        "requirements": [
            "Memorize all 25 nouns with their transliterations.",
            "Rewrite five sentences swapping in different nouns with correct verb endings.",
            "Sort the 25 nouns into person, place, and thing columns.",
            "Say each noun aloud and write it in Tamil script.",
            "Build three new sentences using one person, one place, and one thing noun.",
        ],
        "standards": [
            "Vocabulary follows standard modern Tamil usage per Lehmann 1989.",
            "Verb agreement forms follow Schiffman 1999.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: naming is the first signature - to say "
            "மரம் is to sign the tree into the learner's world. Where "
            "public lists file labels, the Signature Word Method files "
            "witnesses: each noun a thing the tongue has sworn to know."
        ),
    },
    {
        "key": "verbs",
        "name": "Tamil Core Verbs I",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Tamil verbs, given as roots with "
            "transliteration, English, and a full present-tense example "
            "sentence translated. சாப்பிடு (cāppiṭu, eat) - நான் சாப்பாடு "
            "சாப்பிடுகிறேன். (I am eating food.) குடி (kuṭi, drink) - நான் "
            "தண்ணீர் குடிக்கிறேன். (I am drinking water.) போ (pō, go) - "
            "நான் பள்ளிக்குப் போகிறேன். (I am going to school.) வா (vā, "
            "come) - நீ இங்கே வா. (You come here.) இரு (iru, be/stay) - "
            "நான் வீட்டில் இருக்கிறேன். (I am at home.) செய் (cey, do) - "
            "நான் வேலை செய்கிறேன். (I am doing work.) பார் (pār, see) - "
            "நான் படம் பார்க்கிறேன். (I am watching a movie.) கேள் (kēḷ, "
            "listen/ask) - நான் பாட்டு கேட்கிறேன். (I am listening to a "
            "song.) பேசு (pēcu, speak) - நான் தமிழ் பேசுகிறேன். (I am "
            "speaking Tamil.) படி (paṭi, read/study) - நான் புத்தகம் "
            "படிக்கிறேன். (I am reading a book.) எழுது (eḻutu, write) - "
            "நான் கடிதம் எழுதுகிறேன். (I am writing a letter.) ஓடு (ōṭu, "
            "run) - அவன் ஓடுகிறான். (He is running.) நட (naṭa, walk) - "
            "நான் நடக்கிறேன். (I am walking.) உட்கார் (uṭkār, sit) - நீ "
            "உட்கார். (You sit.) நில் (nil, stand) - அவன் நிற்கிறான். (He "
            "is standing.) தூங்கு (tūṅku, sleep) - குழந்தை தூங்குகிறது. "
            "(The child is sleeping.) எழு (eḻu, wake/get up) - நான் "
            "காலையில் எழுகிறேன். (I wake up in the morning.) கொடு (koṭu, "
            "give) - எனக்குப் புத்தகம் கொடு. (Give me the book.) எடு "
            "(eṭu, take) - பையை எடு. (Take the bag.) வாங்கு (vāṅku, buy) "
            "- நான் பழம் வாங்குகிறேன். (I am buying fruit.) வில் (vil, "
            "sell) - அவன் காய்கறி விற்கிறான். (He is selling vegetables.) "
            "கற்றுக்கொள் (kaṟṟukkoḷ, learn) - நான் தமிழ் "
            "கற்றுக்கொள்கிறேன். (I am learning Tamil.) சமை (camai, cook) "
            "- அம்மா சமைக்கிறார். (Mother is cooking.) விளையாடு "
            "(viḷaiyāṭu, play) - குழந்தைகள் விளையாடுகிறார்கள். (The "
            "children are playing.) வேலை செய் (vēlai cey, work) - நான் "
            "அலுவலகத்தில் வேலை செய்கிறேன். (I work in an office.)"
        ),
        "how_it_works": (
            "This record teaches verbs as roots that grow endings. Each "
            "verb is shown first as its root (சாப்பிடு, போ, வா), then "
            "inside a present-tense sentence where the learner can see "
            "the -கிற்- present marker and the person ending: "
            "சாப்பிடுகிறேன் (I eat), போகிறான் (he goes), சமைக்கிறார் "
            "(she/respectful cooks). All sentences use நான் (I) or a "
            "third person so the pattern stays visible. The learner's "
            "drill is conjugation by substitution: take போகிறேன் and "
            "rebuild it as போகிறான், போகிறாள், போகிறார்கள், watching "
            "only the ending change. Commands appear too (வா, உட்கார், "
            "கொடு) because the bare root is the informal imperative - "
            "the first verb form every learner actually needs."
        ),
        "key_points": [
            "25 core verbs as roots, each in a translated present-tense sentence.",
            "Present tense marker is -கிற்-: சாப்பிடுகிறேன், போகிறான்.",
            "Person endings: -ஏன் (I), -ஆன் (he), -ஆள் (she), -ஆர்கள் (they).",
            "The bare root doubles as the informal command: வா (come!), கொடு (give!).",
            "Substitution drills turn 25 sentences into full conjugation practice.",
        ],
        "requirements": [
            "Memorize all 25 verb roots with meanings.",
            "Conjugate சாப்பிடு, போ, and வா in the present for I, he, she, and they.",
            "Convert five நான் sentences to அவன் sentences with correct endings.",
            "Give the informal command form of ten verbs.",
            "Write five new sentences using verbs from this record.",
        ],
        "standards": [
            "Verb roots and present-tense formation follow Lehmann 1989.",
            "Spoken forms cross-checked with Schiffman 1999.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: the verb root is the unsigned instrument "
            "- the ending is the signature that binds it to a person. "
            "Where public grammar tables file forms, the Signature Word "
            "Method files oaths: செய்கிறேன் is the tongue signing its "
            "name to the doing."
        ),
    },
    {
        "key": "adjectives",
        "name": "Tamil Adjectives and Adverbs",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five Tamil adjectives and fifteen adverbs, each with "
            "transliteration, English, and a translated example sentence. "
            "Tamil adjectives come before the noun and do not change for "
            "gender or number. Adjectives: பெரிய (periya, big) - பெரிய "
            "வீடு. (big house.) சிறிய (ciṟiya, small) - சிறிய பூனை. "
            "(small cat.) நல்ல (nalla, good) - நல்ல நண்பன். (good friend.) "
            "கெட்ட (keṭṭa, bad) - கெட்ட பழக்கம். (bad habit.) புதிய "
            "(putiya, new) - புதிய புத்தகம். (new book.) பழைய (paḻaiya, "
            "old) - பழைய வீடு. (old house.) அழகான (aḻakāṉa, beautiful) - "
            "அழகான பூ. (beautiful flower.) வேகமான (vēkamāṉa, fast) - "
            "வேகமான கார். (fast car.) மெதுவான (metuvāṉa, slow) - மெதுவான "
            "நடை. (slow walk.) சூடான (cūṭāṉa, hot) - சூடான காபி. (hot "
            "coffee.) குளிர்ந்த (kuḷirta, cold) - குளிர்ந்த நீர். (cold "
            "water.) இனிப்பான (iṉippāṉa, sweet) - இனிப்பான மாம்பழம். "
            "(sweet mango.) கசப்பான (kacappāṉa, bitter) - கசப்பான மருந்து. "
            "(bitter medicine.) உயரமான (uyaramāṉa, tall) - உயரமான மரம். "
            "(tall tree.) குட்டையான (kuṭṭaiyāṉa, short) - குட்டையான பையன். "
            "(short boy.) நீண்ட (nīṇṭa, long) - நீண்ட சாலை. (long road.) "
            "குறுகிய (kuṟukiya, narrow) - குறுகிய தெரு. (narrow street.) "
            "அகலமான (akalamāṉa, wide) - அகலமான ஆறு. (wide river.) "
            "மெல்லிய (melliya, thin) - மெல்லிய தாள். (thin paper.) தடித்த "
            "(taṭitta, thick) - தடித்த புத்தகம். (thick book.) சுத்தமான "
            "(cuttamāṉa, clean) - சுத்தமான அறை. (clean room.) அழுக்கான "
            "(aḻukkāṉa, dirty) - அழுக்கான சட்டை. (dirty shirt.) எளிய "
            "(eḷiya, easy) - எளிய பாடம். (easy lesson.) கடினமான "
            "(kaṭiṉamāṉa, difficult) - கடினமான தேர்வு. (difficult exam.) "
            "முக்கியமான (mukkiyamāṉa, important) - முக்கியமான செய்தி. "
            "(important news.) Adverbs: வேகமாக (vēkamāka, quickly) - அவன் "
            "வேகமாக ஓடினான். (He ran quickly.) மெதுவாக (metuvāka, slowly) "
            "- மெதுவாகப் பேசு. (Speak slowly.) நன்றாக (naṉṟāka, well) - "
            "அவள் நன்றாகப் பாடினாள். (She sang well.) மோசமாக (mōcamāka, "
            "badly) - அவன் மோசமாக எழுதினான். (He wrote badly.) எப்போதும் "
            "(eppōtum, always) - நான் எப்போதும் சிரிப்பேன். (I always "
            "smile.) ஒருபோதும் (orupōtum, never) - நான் ஒருபோதும் "
            "பொய் சொல்லமாட்டேன். (I never lie.) அடிக்கடி (aṭikkaṭi, "
            "often) - அவள் அடிக்கடி வருவாள். (She comes often.) சில "
            "நேரங்களில் (cila nēraṅkaḷil, sometimes) - சில நேரங்களில் "
            "மழை பெய்யும். (Sometimes it rains.) இன்று (iṉṟu, today) - "
            "இன்று வெயில். (Today is sunny.) நேற்று (nēṟṟu, yesterday) - "
            "நேற்று மழை பெய்தது. (Yesterday it rained.) நாளை (nāḷai, "
            "tomorrow) - நாளை வருவேன். (I will come tomorrow.) இங்கே "
            "(iṅkē, here) - இங்கே வா. (Come here.) அங்கே (aṅkē, there) - "
            "அங்கே போ. (Go there.) மிகவும் (mikavum, very) - இது மிகவும் "
            "நல்லது. (This is very good.) மீண்டும் (mīṇṭum, again) - "
            "மீண்டும் சொல். (Say it again.)"
        ),
        "how_it_works": (
            "This record teaches the two describer words by their "
            "positions. Adjectives stand before the noun and never "
            "change: பெரிய வீடு, பெரிய வீடுகள் - the adjective is the "
            "same for one house or many, for a man or a woman. Many "
            "Tamil adjectives end in -ஆன (அழகான, வேகமான) or are simple "
            "roots (நல்ல, பெரிய). Adverbs modify the verb and often end "
            "in -ஆக: வேகமான (fast) becomes வேகமாக (quickly). The "
            "record's drill is transformation - turn each adjective into "
            "its adverb and use it in a verb sentence - which teaches "
            "the -ஆன to -ஆக pattern as a living rule. Time and place "
            "adverbs (இன்று, நேற்று, நாளை, இங்கே, அங்கே) are drilled as "
            "sentence starters, the natural Tamil position for setting "
            "the scene."
        ),
        "key_points": [
            "25 adjectives + 15 adverbs, each in a translated sentence.",
            "Adjectives precede the noun and never inflect: பெரிய வீடு, பெரிய வீடுகள்.",
            "Adjective -ஆன becomes adverb -ஆக: வேகமான to வேகமாக.",
            "Time/place adverbs open the sentence: நேற்று மழை பெய்தது.",
            "மிகவும் (very) intensifies any adjective or adverb.",
        ],
        "requirements": [
            "Memorize all 25 adjectives and 15 adverbs.",
            "Convert ten -ஆன adjectives to -ஆக adverbs in sentences.",
            "Describe five objects using two adjectives each.",
            "Write five sentences using time adverbs as openers.",
            "Transform five adjective phrases into full sentences.",
        ],
        "standards": [
            "Adjective and adverb forms follow Lehmann 1989.",
            "Usage examples follow standard modern written Tamil.",
        ],
        "citations": [CIT_LEHMANN, CIT_ANNAMALAI],
        "sig_lens": (
            "The Signature read: the adjective is the witness called to "
            "describe, the adverb the witness called to testify how. "
            "Where public lists file modifiers, the Signature Word "
            "Method files testimony: அழகான பூ is the tongue swearing the "
            "flower beautiful."
        ),
    },
    {
        "key": "pronouns",
        "name": "Tamil Pronouns",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The full Tamil pronoun system - personal, possessive, "
            "demonstrative, and interrogative - with paradigms and "
            "example sentences. Personal: நான் (nāṉ, I) - நான் மாணவன். "
            "(I am a student.) நீ (nī, you, informal) - நீ வா. (You "
            "come.) நீங்கள் (nīṅkaḷ, you, formal/plural) - நீங்கள் "
            "வாருங்கள். (Please come.) அவன் (avaṉ, he) - அவன் நல்லவன். "
            "(He is good.) அவள் (avaḷ, she) - அவள் பாடுகிறாள். (She is "
            "singing.) அது (atu, it) - அது பெரியது. (It is big.) அவர் "
            "(avar, he/she respectful) - அவர் வந்தார். (He/she came - "
            "respectful.) நாங்கள் (nāṅkaḷ, we exclusive) - நாங்கள் "
            "போகிறோம். (We are going - not including you.) நாம் (nām, we "
            "inclusive) - நாம் போகலாம். (Let us go - including you.) "
            "அவர்கள் (avarkaḷ, they) - அவர்கள் வந்தார்கள். (They came.) "
            "Possessive: என்/எனது (eṉ/eṉatu, my) - என் புத்தகம். (my "
            "book.) உன்/உங்கள் (uṉ/uṅkaḷ, your) - உங்கள் வீடு. (your "
            "house.) அவனுடைய/அவளுடைய (avaṉuṭaiya/avaḷuṭaiya, his/her) - "
            "அவளுடைய பேனா. (her pen.) எங்கள்/நமது (eṅkaḷ/namatu, our) - "
            "நமது நாடு. (our country.) Demonstrative: இவன் (ivaṉ, this "
            "he) - இவன் என் நண்பன். (This is my friend - male.) இவள் "
            "(ivaḷ, this she) - இவள் என் தங்கை. (This is my sister.) இது "
            "(itu, this) - இது என்ன? (What is this?) அவன் (avaṉ, that he) "
            "- அவன் யார்? (Who is he?) அவள் (avaḷ, that she) - அவள் "
            "ஆசிரியை. (She is a teacher.) அது (atu, that) - அது பழையது. "
            "(That is old.) Interrogative: யார் (yār, who) - யார் "
            "வந்தது? (Who came?) என்ன (eṉṉa, what) - என்ன வேண்டும்? (What "
            "do you want?) எங்கே (eṅkē, where) - எங்கே போகிறாய்? (Where "
            "are you going?) எப்போது (eppōtu, when) - எப்போது வருவாய்? "
            "(When will you come?) ஏன் (ēṉ, why) - ஏன் அழுகிறாய்? (Why "
            "are you crying?) எப்படி (eppaṭi, how) - எப்படி இருக்கிறாய்? "
            "(How are you?) எது (etu, which) - எது உன்னுடையது? (Which is "
            "yours?) எவ்வளவு (evvaḷavu, how much) - எவ்வளவு ஆகும்? (How "
            "much will it be?)"
        ),
        "how_it_works": (
            "This record teaches pronouns as a politeness machine. The "
            "core lesson is the three levels of 'you': நீ for close "
            "friends and children, நீங்கள் for elders, strangers, and "
            "plural - and using the wrong one is the fastest way to "
            "sound rude. The record then teaches the inclusive/exclusive "
            "'we' distinction (நாம் includes the listener, நாங்கள் does "
            "not), which English lacks entirely. Demonstratives pair "
            "இ- (near) with அ- (far) across all three noun classes, and "
            "interrogatives all begin with எ-, a pattern the learner can "
            "lean on. Possessives attach as prefixes (என் புத்தகம்) or "
            "with -உடைய (அவனுடைய). The drill is role-play: the learner "
            "addresses a friend, then an elder, then a group, converting "
            "நீ sentences to நீங்கள் sentences and watching verbs shift "
            "to the respectful -ஈர்கள்/-ஆர்கள் endings."
        ),
        "key_points": [
            "Three levels of you: நீ (informal), நீங்கள் (formal/plural).",
            "We splits inclusive நாம் and exclusive நாங்கள்.",
            "அவர் is the respectful he/she; verb takes -ஆர்.",
            "Demonstratives pair இ- (near) with அ- (far): இது/அது.",
            "All question words begin with எ-: யார், என்ன, எங்கே, ஏன், எப்படி.",
        ],
        "requirements": [
            "Memorize the personal pronoun paradigm with English meanings.",
            "Convert five நீ sentences to நீங்கள் form with correct verb endings.",
            "Write three sentences each with நாம் and நாங்கள் showing the difference.",
            "Ask and answer eight questions using the interrogative pronouns.",
            "Introduce two people using இவன்/இவள்/இது correctly.",
        ],
        "standards": [
            "Pronoun paradigms follow Lehmann 1989 and Schiffman 1999.",
            "Politeness levels follow standard Tamil sociolinguistic usage.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN, CIT_ANNAMALAI],
        "sig_lens": (
            "The Signature read: pronouns are the signatures of "
            "relationship - நீ the seal of closeness, நீங்கள் the seal "
            "of honor. Where public tables file persons, the Signature "
            "Word Method files bonds: every pronoun a signed measure of "
            "distance between two souls."
        ),
    },
    {
        "key": "numbers",
        "name": "Tamil Numbers and Time",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Tamil numbers 1-100, ordinals, days, months, seasons, clock "
            "time, and dates - each with example sentences. Numbers: 1 "
            "ஒன்று (oṉṟu), 2 இரண்டு (iraṇṭu), 3 மூன்று (mūṉṟu), 4 நான்கு "
            "(nāṉku), 5 ஐந்து (aintu), 6 ஆறு (āṟu), 7 ஏழு (ēḻu), 8 எட்டு "
            "(eṭṭu), 9 ஒன்பது (oṉpatu), 10 பத்து (pattu), 11 பதினொன்று, "
            "12 பன்னிரண்டு, 13 பதின்மூன்று, 14 பதினான்கு, 15 பதினைந்து, "
            "16 பதினாறு, 17 பதினேழு, 18 பதினெட்டு, 19 பத்தொன்பது, 20 "
            "இருபது, 21 இருபத்தொன்று, 30 முப்பது, 40 நாற்பது, 50 ஐம்பது, "
            "60 அறுபது, 70 எழுபது, 80 எண்பது, 90 தொண்ணூறு, 100 நூறு. "
            "Compounding rule: 22 இருபத்திரண்டு, 35 முப்பத்தைந்து, 47 "
            "நாற்பத்தேழு, 58 ஐம்பத்தெட்டு, 69 அறுபத்தொன்பது, 76 "
            "எழுபத்தாறு, 84 எண்பத்துநான்கு, 93 தொண்ணூற்றுமூன்று. "
            "Ordinals: முதல் (first), இரண்டாவது (second), மூன்றாவது "
            "(third). Days: ஞாயிறு (Sunday), திங்கள் (Monday), செவ்வாய் "
            "(Tuesday), புதன் (Wednesday), வியாழன் (Thursday), வெள்ளி "
            "(Friday), சனி (Saturday). Months (Tamil calendar): சித்திரை, "
            "வைகாசி, ஆனி, ஆடி, ஆவணி, புரட்டாசி, ஐப்பசி, கார்த்திகை, "
            "மார்கழி, தை, மாசி, பங்குனி. Seasons: இளவேனில் (spring), "
            "முதுவேனில் (summer), கார் (monsoon), கூதிர் (autumn), முன்பனி "
            "and பின்பனி (winter). Clock time uses மணி: ஒரு மணி (1 "
            "o'clock), இரண்டு மணி (2 o'clock), அரை மணி (half hour), கால் "
            "மணி (quarter hour). Example sentences: எனக்கு இரண்டு "
            "புத்தகங்கள் உள்ளன. (I have two books.) இன்று திங்கள். "
            "(Today is Monday.) மணி மூன்று. (It is three o'clock.) "
            "நாளை என் பிறந்தநாள். (Tomorrow is my birthday.) இது முதல் "
            "பாடம். (This is the first lesson.)"
        ),
        "how_it_works": (
            "This record teaches numbers as a building system, not a "
            "memorization list. The learner masters 1-10 cold, then "
            "learns the compounding rule: the tens word sheds its final "
            "து for த்து and takes the unit (இருபது to இருபத்து + ஒன்று "
            "= இருபத்தொன்று), with the memorized exceptions 11 "
            "பதினொன்று and 12 பன்னிரண்டு. Once the rule clicks, the "
            "learner can build any number to 99 and reach 100 நூறு. Days "
            "of the week are learned as a chant in order from ஞாயிறு; "
            "the twelve Tamil months are learned as a year-wheel from "
            "சித்திரை; the six seasons pair with them. Clock time is "
            "taught as number + மணி with அரை and கால் for halves and "
            "quarters. Every section ends with a doing task - telling "
            "today's date, your age, the time - so numbers become speech "
            "immediately."
        ),
        "key_points": [
            "1-10 memorized; 21-99 built by the து to த்து compounding rule.",
            "Exceptions: 11 பதினொன்று, 12 பன்னிரண்டு, 19 பத்தொன்பது.",
            "Ordinals add -ஆவது: இரண்டாவது, மூன்றாவது; first is முதல்.",
            "Seven days from ஞாயிறு; twelve Tamil months from சித்திரை; six seasons.",
            "Time is number + மணி; அரை = half, கால் = quarter.",
        ],
        "requirements": [
            "Count 1-20 aloud in Tamil without looking.",
            "Build the numbers 25, 47, 68, 83, and 96 using the compounding rule.",
            "Say today's day, date, and time fully in Tamil.",
            "Recite the seven days and twelve months in order.",
            "Write your age and phone number in Tamil words.",
        ],
        "standards": [
            "Numeral forms follow standard modern Tamil per Lehmann 1989.",
            "Tamil calendar months follow the traditional solar calendar order.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: numbers are the seals of measure - ஒன்று "
            "the first signature on the world. Where public lists file "
            "digits, the Signature Word Method files reckonings: every "
            "count a covenant that what is numbered is known."
        ),
    },
    {
        "key": "greetings",
        "name": "Tamil Greetings and Everyday Phrases",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Thirty Tamil greetings, farewells, and politeness phrases "
            "with transliteration, English, and usage notes. வணக்கம் "
            "(vaṇakkam, hello - the universal greeting, palms together) - "
            "use anytime. காலை வணக்கம் (morning greeting), மாலை வணக்கம் "
            "(evening greeting), இரவு வணக்கம் (night greeting). நன்றி "
            "(naṉṟi, thank you). மிக்க நன்றி (many thanks). தயவு செய்து "
            "(tayavu ceytu, please). மன்னிக்கவும் (maṉṉikkavum, excuse "
            "me/sorry). பரவாயில்லை (paravāyillai, it is okay/no problem). "
            "சரி (cari, okay). ஆமாம் (āmām, yes). இல்லை (illai, no). "
            "வருக வருக (varuka varuka, welcome). உள்ளே வாருங்கள் (come "
            "in - respectful). உட்காருங்கள் (please sit). சாப்பிட்டீர்களா? "
            "(have you eaten? - the warm Tamil welcome question). காபி "
            "சாப்பிடுங்கள் (have some coffee). நலமா? (nalamā, are you "
            "well?). நல்லா இருக்கேன் (I am fine). எப்படி இருக்கீங்க? (how "
            "are you - respectful). உங்களைச் சந்தித்ததில் மகிழ்ச்சி (nice "
            "to meet you). போய் வருகிறேன் (pōy varukiṟēṉ, goodbye - "
            "literally I go and will come). மீண்டும் சந்திப்போம் (see you "
            "again). கவனமாகப் போங்கள் (go carefully/take care). நல்ல நாள் "
            "(have a good day). வாழ்த்துக்கள் (vāḻttukkaḷ, "
            "congratulations). பிறந்தநாள் வாழ்த்துக்கள் (happy birthday). "
            "புத்தாண்டு வாழ்த்துக்கள் (happy new year). தயவுசெய்து "
            "உதவுங்கள் (please help me). கொஞ்சம் பொறுங்கள் (please wait a "
            "moment). Example exchanges: வணக்கம்! நலமா? - நல்லா "
            "இருக்கேன், நீங்க? (Hello! Are you well? - I am fine, and "
            "you?)"
        ),
        "how_it_works": (
            "This record teaches greetings as social choreography. "
            "வணக்கம் is first - the one word that opens every door - "
            "with the note that palms pressed together carry the "
            "meaning. Then come the day-part greetings, then the "
            "gratitude and apology set (நன்றி, மன்னிக்கவும், "
            "பரவாயில்லை), then hospitality phrases - because in Tamil "
            "culture the guest is offered food and drink first, so "
            "சாப்பிட்டீர்களா and காபி சாப்பிடுங்கள் are taught as "
            "greetings, not just sentences. Farewells center on போய் "
            "வருகிறேன், whose literal 'I go and will come' teaches the "
            "Tamil reluctance to say a final goodbye. Each phrase "
            "carries a usage note - who to, when - and the drill is "
            "paired role-play: one learner greets, the other answers, "
            "through morning, meeting, hospitality, and farewell scenes."
        ),
        "key_points": [
            "வணக்கம் is the universal greeting, said with palms together.",
            "சாப்பிட்டீர்களா (have you eaten?) is a genuine Tamil welcome.",
            "போய் வருகிறேன் means I go and will come - goodbye without finality.",
            "Hospitality phrases (come in, sit, have coffee) are greeting rituals.",
            "நீங்கள்-forms keep every polite phrase respectful.",
        ],
        "requirements": [
            "Greet three people with வணக்கம் and palms together today.",
            "Role-play a full meeting: greeting, how-are-you, welcome, farewell.",
            "Use சாப்பிட்டீர்களா with a guest and note their reaction.",
            "Write five mini-dialogues using phrases from this record.",
            "Say the farewell set (போய் வருகிறேன், மீண்டும் சந்திப்போம்) from memory.",
        ],
        "standards": [
            "Phrases follow standard polite Tamil usage per Schiffman 1999.",
            "Usage notes reflect documented Tamil hospitality conventions.",
        ],
        "citations": [CIT_SCHIFFMAN, CIT_ANNAMALAI],
        "sig_lens": (
            "The Signature read: வணக்கம் is the bow of the tongue - the "
            "first signature exchanged between strangers. Where public "
            "phrasebooks file hellos, the Signature Word Method files "
            "covenants of welcome: every greeting a seal that the other "
            "is honored."
        ),
    },
    {
        "key": "grammar",
        "name": "Tamil Grammar Essentials",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "The core machinery of Tamil grammar, each rule with "
            "translated example sentences. Word order is subject-object-"
            "verb: நான் புத்தகம் படிக்கிறேன். (I book read - I am reading "
            "a book.) Tamil is agglutinative: suffixes stack on roots - "
            "வீடுகளில் (in the houses) = வீடு + கள் + இல். Nouns divide "
            "into rational (உயர்திணை: humans, gods) and irrational "
            "(அஃறிணை: animals, things): rational masculine takes -அன் "
            "(மனிதன்), rational feminine -அள் (பெண் becomes பெண்கள் "
            "plural), irrational takes -அது (மரம்...அது). Cases attach as "
            "suffixes to the oblique stem: accusative -ஐ (புத்தகத்தை - "
            "the book [object]), dative -க்கு (அவனுக்கு - to him), "
            "instrumental -ஆல் (கத்தியால் - with a knife), sociative "
            "-ஓடு/-உடன் (அவனோடு - with him), locative -இல் (வீட்டில் - in "
            "the house), ablative -இலிருந்து (வீட்டிலிருந்து - from the "
            "house), genitive -இன்/-உடைய (வீட்டின் - of the house). "
            "Plural is -கள்: புத்தகங்கள் (books). There are no articles; "
            "ஒரு (a) and அந்த (that/the) do the work: ஒரு புத்தகம் (a "
            "book), அந்த புத்தகம் (the book). Negation: இல்லை (not/is "
            "not) - அது இல்லை. (It is not there.); verb negation with "
            "-ஆ- - செய்யாதே (do not do); future negative -மாட்ட்- - "
            "வரமாட்டேன் (I will not come). Questions form with -ஆ (நீ "
            "வருகிறாயா? - Are you coming?), with எ- words (எங்கே "
            "போகிறாய்?), or with ஆம்/இல்லை answers. Adjectives precede "
            "nouns and never inflect. Example sentences: அவன் பள்ளிக்குப் "
            "போகிறான். (He is going to school - dative -க்கு.) நான் "
            "கத்தியால் வெட்டினேன். (I cut with a knife - instrumental.) "
            "புத்தகம் மேசையில் உள்ளது. (The book is on the table - "
            "locative.)"
        ),
        "how_it_works": (
            "This record teaches grammar as eight machines, each "
            "demonstrated on the same small vocabulary so the machinery "
            "stays visible. Machine one: SOV order, shown by scrambling "
            "an English sentence into Tamil order. Machine two: "
            "agglutination, shown by building வீடுகளில் suffix by "
            "suffix. Machine three: the rational/irrational split, shown "
            "through verb endings (-அன், -அள், -அது). Machines four and "
            "five: the seven case suffixes and the -கள் plural, each "
            "applied to வீடு and புத்தகம். Machine six: ஒரு and அந்த "
            "standing in for articles. Machine seven: the three negations "
            "(இல்லை, -ஆ-, -மாட்ட்-). Machine eight: the three question "
            "forms. The learner's drill is transformation chains: take "
            "நான் புத்தகம் படிக்கிறேன் and negate it, question it, "
            "pluralize the book, and move it to the table - one sentence "
            "exercising every machine."
        ),
        "key_points": [
            "Word order is SOV: நான் புத்தகம் படிக்கிறேன்.",
            "Suffixes stack: வீடு + கள் + இல் = வீடுகளில்.",
            "Rational vs irrational noun classes drive verb agreement.",
            "Seven working cases: -ஐ, -க்கு, -ஆல், -ஓடு, -இல், -இலிருந்து, -இன்.",
            "Negation: இல்லை, -ஆ-, -மாட்ட்-; questions: -ஆ, எ- words.",
        ],
        "requirements": [
            "Build வீடுகளிலிருந்து suffix by suffix and gloss each piece.",
            "Apply all seven cases to புத்தகம் with translations.",
            "Negate five affirmative sentences three ways each.",
            "Turn five statements into questions using each question form.",
            "Write ten SOV sentences and mark subject, object, verb.",
        ],
        "standards": [
            "Case system follows the Tolkappiyam col treatment as analyzed in Lehmann 1989.",
            "Rational/irrational classes follow Caldwell 1856 and Annamalai/Steever 1998.",
        ],
        "citations": [CIT_TOLKAPPIYAM, CIT_LEHMANN, CIT_CALDWELL, CIT_ANNAMALAI],
        "sig_lens": (
            "The Signature read: grammar is the covenant binding words "
            "into truth - the suffix the seal, the word order the "
            "procession. Where public grammars file rules, the Signature "
            "Word Method files the oath of structure: every sentence a "
            "signed and witnessed instrument."
        ),
    },
    {
        "key": "home_family",
        "name": "Tamil Home and Family Sentences",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Tamil sentences about house, rooms, furniture, and "
            "family members, each with transliteration and English. 1. "
            "என் வீடு பெரியது. (Eṉ vīṭu periyatu. - My house is big.) 2. "
            "வீட்டில் நான்கு அறைகள் உள்ளன. (Vīṭṭil nāṉku aṟaikaḷ uḷḷaṉa. "
            "- There are four rooms in the house.) 3. சமையலறை சுத்தமாக "
            "உள்ளது. (Camaiyalaṟai cuttamāka uḷḷatu. - The kitchen is "
            "clean.) 4. படுக்கையறையில் கட்டில் உள்ளது. (Paṭukkaiyaṟaiyil "
            "kaṭṭil uḷḷatu. - There is a bed in the bedroom.) 5. மேசை "
            "ஜன்னல் அருகில் உள்ளது. (Mēcai jaṉṉal arukil uḷḷatu. - The "
            "table is near the window.) 6. நாற்காலியில் உட்காருங்கள். "
            "(Nāṟkāliyil uṭkāruṅkaḷ. - Please sit on the chair.) 7. கதவைத் "
            "திறவுங்கள். (Katavait tiṟavuṅkaḷ. - Please open the door.) "
            "8. விளக்கை அணைத்துவிடு. (Viḷakkai aṇaittuviṭu. - Switch off "
            "the light.) 9. என் அப்பா ஆசிரியர். (Eṉ appā āciriyar. - My "
            "father is a teacher.) 10. என் அம்மா சமைக்கிறார். (Eṉ ammā "
            "camaikkiṟār. - My mother is cooking.) 11. எனக்கு ஒரு அண்ணன் "
            "உள்ளான். (Eṉakku oru aṇṇaṉ uḷḷāṉ. - I have an elder brother.) "
            "12. என் தங்கை பள்ளியில் படிக்கிறாள். (Eṉ taṅkai paḷḷiyil "
            "paṭikkiṟāḷ. - My younger sister studies at school.) 13. தாத்தா "
            "தோட்டத்தில் இருக்கிறார். (Tāttā tōṭṭattil irukkiṟār. - "
            "Grandfather is in the garden.) 14. பாட்டி கதை சொல்கிறார். "
            "(Pāṭṭi katai colkiṟār. - Grandmother is telling a story.) "
            "15. என் மாமா நேற்று வந்தார். (Eṉ māmā nēṟṟu vantār. - My "
            "uncle came yesterday.) 16. அத்தை பலகாரம் கொடுத்தார். (Attai "
            "palakāram koṭuttār. - Aunt gave sweets.) 17. எங்கள் குடும்பம் "
            "பெரியது. (Eṅkaḷ kuṭumpam periyatu. - Our family is big.) 18. "
            "வீட்டு வேலைகளைப் பகிர்ந்து செய்வோம். (Vīṭṭu vēlaikaḷaip "
            "pakirntu ceyvōm. - We share the housework.) 19. முற்றத்தில் "
            "பூக்கள் பூத்துள்ளன. (Muṟṟattil pūkkaḷ pūttuḷḷaṉa. - Flowers "
            "have bloomed in the courtyard.) 20. வீடு எனக்கு மிகவும் "
            "பிடிக்கும். (Vīṭu eṉakku mikavum piṭikkum. - I like home "
            "very much.)"
        ),
        "how_it_works": (
            "This record teaches the home as a walk-through: the learner "
            "enters the வீடு, counts the அறைகள், visits the சமையலறை and "
            "படுக்கையறை, notes the furniture with locative -இல் "
            "sentences, then meets the family - அப்பா, அம்மா, அண்ணன், "
            "தங்கை, தாத்தா, பாட்டி, மாமா, அத்தை - each introduced in a "
            "doing sentence. Kinship terms carry Tamil's precision: "
            "அண்ணன் is elder brother specifically, தங்கை younger sister "
            "specifically - the record notes this so the learner feels "
            "the system. Locative and dative cases recur naturally "
            "(வீட்டில், எனக்கு), and the respectful -ஆர் ending appears "
            "on elders. The drill is a home tour: the learner describes "
            "their own house room by room and introduces their own "
            "family, replacing each sentence's nouns."
        ),
        "key_points": [
            "20 home and family sentences, each with transliteration and English.",
            "Kinship terms mark age and gender precisely: அண்ணன் vs தங்கை.",
            "Locative -இல் places everything: வீட்டில், அறையில்.",
            "Elders take respectful -ஆர்: தாத்தா இருக்கிறார்.",
            "உள்ளது/உள்ளன express existence: there is / there are.",
        ],
        "requirements": [
            "Describe your own home room by room in eight Tamil sentences.",
            "Introduce your family members using precise kinship terms.",
            "Rewrite five sentences changing singular rooms to plural.",
            "Practice the respectful -ஆர் endings for three elders.",
            "Give a spoken tour of your house using only Tamil.",
        ],
        "standards": [
            "Kinship vocabulary follows standard Tamil usage per Schiffman 1999.",
            "Locative and existential constructions follow Lehmann 1989.",
        ],
        "citations": [CIT_SCHIFFMAN, CIT_LEHMANN],
        "sig_lens": (
            "The Signature read: the home is the first archive - every "
            "room a shelf, every elder a living record. Where public "
            "lessons file vocabulary, the Signature Word Method files "
            "belonging: வீடு the seal of shelter, குடும்பம் the seal of "
            "kin."
        ),
    },
    {
        "key": "food_cooking",
        "name": "Tamil Food and Cooking Sentences",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Tamil sentences about meals, ingredients, cooking "
            "actions, and restaurants. 1. காலை உணவு தயார். (Kālai uṇavu "
            "tayār. - Breakfast is ready.) 2. சாதம் சூடாக உள்ளது. "
            "(Cātam cūṭāka uḷḷatu. - The rice is hot.) 3. சாம்பார் மிகவும் "
            "சுவையாக உள்ளது. (Cāmpār mikavum cuvaiyāka uḷḷatu. - The "
            "sambar is very tasty.) 4. இட்லி மென்மையாக உள்ளது. (Iṭli "
            "meṉmaiyāka uḷḷatu. - The idli is soft.) 5. தோசை மொறுமொறுப்பாக "
            "உள்ளது. (Tōcai moṟumoṟuppāka uḷḷatu. - The dosa is crispy.) "
            "6. அம்மா காய்கறி நறுக்குகிறார். (Ammā kāykaṟi naṟukkukiṟār. - "
            "Mother is chopping vegetables.) 7. குக்கரில் பருப்பு "
            "வேகிறது. (Kukkaril paruppu vēkiṟatu. - Lentils are cooking "
            "in the cooker.) 8. எண்ணெயில் கடுகு தாளி. (Eṇṇeyil kaṭuku "
            "tāḷi. - Temper mustard in oil.) 9. உப்பு கொஞ்சம் போடு. "
            "(Uppu koñcam pōṭu. - Add a little salt.) 10. மிளகாய் அதிகம் "
            "வேண்டாம். (Miḷakāy atikam vēṇṭām. - Do not add too much "
            "chili.) 11. பால் காய்ச்சு. (Pāl kāyccu. - Boil the milk.) 12. "
            "காபி ஆறிவிட்டது. (Kāpi āṟiviṭṭatu. - The coffee has cooled.) "
            "13. மதிய உணவு என்ன? (Matiya uṇavu eṉṉa? - What is for lunch?) "
            "14. இரவு சாப்பாடு எட்டு மணிக்கு. (Iravu cāppāṭu eṭṭu "
            "maṇikku. - Dinner is at eight o'clock.) 15. பழங்கள் "
            "மேசையில் உள்ளன. (Paḻaṅkaḷēcaiyil uḷḷaṉa. - The fruits are on "
            "the table.) 16. தண்ணீர் குடியுங்கள். (Taṇṇīr kuṭiyuṅkaḷ. - "
            "Please drink water.) 17. உணவகத்தில் சாப்பிடலாம். (Uṇavakattil "
            "cāppiṭalām. - We can eat at the restaurant.) 18. மெனு கொண்டு "
            "வாருங்கள். (Meṉu koṇṭu vāruṅkaḷ. - Please bring the menu.) "
            "19. கணக்கு எவ்வளவு? (Kaṇakku evvaḷavu? - How much is the "
            "bill?) 20. உணவு அருமையாக இருந்தது. (Uṇavu arumaiyāka "
            "iruntatu. - The food was excellent.)"
        ),
        "how_it_works": (
            "This record teaches food through the day's three meals and "
            "the kitchen's actions. Breakfast opens with இட்லி, தோசை, "
            "and காபி - the foods a Tamil learner will actually meet. "
            "Cooking verbs arrive as commands the learner can use at the "
            "stove: நறுக்கு (chop), வேகு (cook/boil), தாளி (temper), "
            "போடு (add), காய்ச்சு (boil milk). Taste adjectives (சுவையான, "
            "மென்மையான, மொறுமொறுப்பான) describe the results. The "
            "restaurant scene teaches the service script: asking for the "
            "menu, asking the bill. Measurement words (கொஞ்சம், அதிகம்) "
            "teach quantity control. The drill is a cooking show: the "
            "learner narrates making one dish step by step in Tamil, "
            "then role-plays ordering it at a restaurant."
        ),
        "key_points": [
            "20 food and cooking sentences with transliteration and English.",
            "Kitchen commands: நறுக்கு, தாளி, போடு, காய்ச்சு.",
            "Three meals: காலை உணவு, மதிய உணவு, இரவு சாப்பாடு.",
            "Restaurant script: menu request, bill question.",
            "கொஞ்சம் (a little) and அதிகம் (too much) control quantity.",
        ],
        "requirements": [
            "Narrate cooking one Tamil dish in six steps, all in Tamil.",
            "Role-play ordering food at a restaurant with a partner.",
            "Describe five foods using taste adjectives.",
            "Convert five commands from informal to respectful -உங்கள் form.",
            "Write your day's three meals in Tamil sentences.",
        ],
        "standards": [
            "Food vocabulary follows standard Tamil usage.",
            "Cooking verbs follow Lehmann 1989 verb classes.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: cooking is the daily alchemy - fire the "
            "witness, the hand the signer. Where public lessons file "
            "recipes, the Signature Word Method files transformation: "
            "சமை the seal by which raw becomes ready."
        ),
    },
    {
        "key": "travel",
        "name": "Tamil Travel and Directions Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Tamil sentences about transport, asking directions, "
            "tickets, and lodging. 1. ரயில் நிலையம் எங்கே? (Rayil "
            "nilaiyam eṅkē? - Where is the railway station?) 2. பேருந்து "
            "நிறுத்தம் அங்கே. (Pēruntu niṟuttam aṅkē. - The bus stop is "
            "there.) 3. நேராகப் போங்கள். (Nērākap pōṅkaḷ. - Go straight.) "
            "4. இடது பக்கம் திரும்புங்கள். (Iṭatu pakkam tirumpuṅkaḷ. - "
            "Turn left.) 5. வலது பக்கம் திரும்புங்கள். (Valatu pakkam "
            "tirumpuṅkaḷ. - Turn right.) 6. அருகில் தான். (Arukil tāṉ. - "
            "It is nearby.) 7. தூரம் அதிகம். (Tūram atikam. - It is far.) "
            "8. டிக்கெட் எங்கே வாங்குவது? (Ṭikkeṭ eṅkē vāṅkuvatu? - Where "
            "do I buy a ticket?) 9. சென்னைக்கு ஒரு டிக்கெட். (Ceṉṉaikku "
            "oru ṭikkeṭ. - One ticket to Chennai.) 10. ரயில் எத்தனை "
            "மணிக்கு? (Rayil ettaṉai maṇikku? - At what time is the "
            "train?) 11. பேருந்து தாமதமாக வருகிறது. (Pēruntu tāmatamāka "
            "varukiṟatu. - The bus is coming late.) 12. ஆட்டோ எவ்வளவு? "
            "(Āṭṭō evvaḷavu? - How much for the auto?) 13. மீட்டர் "
            "போடுங்கள். (Mīṭṭar pōṭuṅkaḷ. - Please turn on the meter.) 14. "
            "இங்கே நிறுத்துங்கள். (Iṅkē niṟuttuṅkaḷ. - Please stop here.) "
            "15. விமான நிலையம் எவ்வளவு தூரம்? (Vimāṉa nilaiyam evvaḷavu "
            "tūram? - How far is the airport?) 16. ஹோட்டலில் அறை உள்ளதா? "
            "(Hōṭṭalil aṟai uḷḷatā? - Is there a room in the hotel?) 17. "
            "ஒரு நாளைக்கு எவ்வளவு? (Oru nāḷaikku evvaḷavu? - How much per "
            "day?) 18. காலை உணவு சேர்த்தா? (Kālai uṇavu cērttā? - Is "
            "breakfast included?) 19. என் பை எங்கே? (Eṉ pai eṅkē? - Where "
            "is my bag?) 20. உதவிக்கு நன்றி. (Utavikku naṉṟi. - Thanks "
            "for the help.)"
        ),
        "how_it_works": (
            "This record teaches travel as a survival script in four "
            "scenes. Scene one: directions - the question எங்கே plus "
            "the three answers every traveler needs (நேராக, இடது, "
            "வலது). Scene two: tickets - the dative -க்கு marks "
            "destination (சென்னைக்கு), and எத்தனை மணிக்கு asks the "
            "time. Scene three: the auto-rickshaw negotiation - "
            "எவ்வளவு and மீட்டர் போடுங்கள், the two sentences that save "
            "every traveler's wallet. Scene four: the hotel - room, "
            "price per day, breakfast included. Direction words pair "
            "with பக்கம் (side), distance with அருகில் and தூரம். The "
            "drill is a journey: the learner plans a trip from home to "
            "station to hotel entirely in Tamil, asking and answering "
            "every question in the record."
        ),
        "key_points": [
            "20 travel sentences covering transport, directions, tickets, lodging.",
            "Dative -க்கு marks destination: சென்னைக்கு.",
            "நேராக, இடது பக்கம், வலது பக்கம் give all directions.",
            "எவ்வளவு and மீட்டர் போடுங்கள் handle fares.",
            "Hotel script: room, daily price, breakfast included.",
        ],
        "requirements": [
            "Plan a full trip in Tamil: home to station to hotel.",
            "Give directions from your house to the nearest shop.",
            "Role-play buying a train ticket with destination and time.",
            "Negotiate an auto fare using எவ்வளவு.",
            "Book a hotel room asking price and breakfast.",
        ],
        "standards": [
            "Transport vocabulary follows standard modern Tamil.",
            "Direction constructions follow Lehmann 1989.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: the road is the unsealed page - every "
            "journey a sentence the feet write. Where public lessons "
            "file phrases, the Signature Word Method files passage: "
            "எங்கே the seal of the seeker, நேராக the seal of the true "
            "path."
        ),
    },
    {
        "key": "work_school",
        "name": "Tamil Work and School Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Tamil sentences about jobs, office, classroom, and "
            "learning. 1. நான் ஆசிரியர். (Nāṉ āciriyar. - I am a teacher.) "
            "2. அவர் அலுவலகத்தில் வேலை செய்கிறார். (Avar aluvalakattil "
            "vēlai ceykiṟār. - He works in an office.) 3. என் வேலை "
            "எனக்குப் பிடிக்கும். (Eṉ vēla eṉakkup piṭikkum. - I like my "
            "job.) 4. இன்று அறிக்கை கொடுக்க வேண்டும். (Iṉṟu aṟikkai "
            "koṭukka vēṇṭum. - I must submit the report today.) 5. என் "
            "முதலாளி மிகவும் நல்லவர். (Eṉ mutalāḷi mikavum nallavar. - My "
            "boss is very good.) 6. நான் பொறியியல் படிக்கிறேன். (Nāṉ "
            "poṟiyiyal paṭikkiṟēṉ. - I am studying engineering.) 7. கணித "
            "வகுப்பு கடினமானது. (Kaṇita vakuppu kaṭiṉamāṉatu. - Math class "
            "is difficult.) 8. தேர்வு வெள்ளிக்கிழமை. (Tērvu "
            "veḷḷikkiḻamai. - The exam is on Friday.) 9. நான் தினமும் "
            "புதிய சொற்கள் கற்கிறேன். (Nāṉ tiṉamum putiya coṟkaḷ "
            "kaṟkiṟēṉ. - I learn new words every day.) 10. என் "
            "வகுப்புத் தோழர்கள் அன்பானவர்கள். (Eṉ vakupput tōḻarkaḷ "
            "aṉpāṉavarkaḷ. - My classmates are kind.) 11. ஆசிரியர் "
            "நன்றாக விளக்குகிறார். (Āciriyar naṉṟāka viḷakkukiṟār. - The "
            "teacher explains well.) 12. இரவு உணவுக்குப் பிறகு வீட்டுப் "
            "பாடம் செய்கிறேன். (Iravu uṇavukkup piṟaku vīṭṭup pāṭam "
            "ceykiṟēṉ. - I do homework after dinner.) 13. பகுதிநேர வேலை "
            "தேடுகிறேன். (Pakutinēra vēlai tēṭukiṟēṉ. - I am looking for "
            "part-time work.) 14. என் நேரம் காலை எட்டு முதல் மாலை ஐந்து "
            "வரை. (Eṉ nēram kālai eṭṭu mutal mālai aintu varai. - My hours "
            "are eight in the morning to five in the evening.) 15. "
            "நூலகம் பத்து மணிக்கு மூடும். (Nūlakam pattu maṇikku mūṭum. - "
            "The library closes at ten.) 16. நேற்று என் திட்டத்தை "
            "வழங்கினேன். (Nēṟṟu eṉ tiṭṭattai vaḻaṅkiṉēṉ. - I presented my "
            "project yesterday.) 17. கடந்த மாதம் எனக்குப் பதவி உயர்வு "
            "கிடைத்தது. (Kaṭanta mātam eṉakkup patavi uyarvu kiṭaittatu. - "
            "I got a promotion last month.) 18. மாணவர்கள் நிறையப் "
            "படிக்கிறார்கள். (Māṇavarkaḷ niṟaiyap paṭikkiṟārkaḷ. - The "
            "students study a lot.) 19. நான் தமிழில் மின்னஞ்சல் "
            "எழுதுகிறேன். (Nāṉ tamiḻil miṉṉañcal eḻutukiṟēṉ. - I write "
            "emails in Tamil.) 20. எனக்கு என் வேலை பிடிக்கும். (Eṉakku eṉ "
            "vēlai piṭikkum. - I like my job.)"
        ),
        "how_it_works": (
            "This record teaches work and school through obligation, "
            "routine, and achievement. Obligation runs on வேண்டும் "
            "(must): அறிக்கை கொடுக்க வேண்டும். Routine runs on present "
            "tense: வேலை செய்கிறேன், படிக்கிறேன். Completed events run on "
            "past tense: வழங்கினேன், கிடைத்தது. Job titles show Tamil's "
            "respectful forms (ஆசிரியர், முதலாளி with -அர்). Time spans "
            "use முதல்...வரை (from...to). The promotion sentence shows "
            "the dative experiencer pattern (எனக்கு...கிடைத்தது - to me "
            "it was obtained), a core Tamil construction. The drill is a "
            "workday: the learner narrates their own job or studies "
            "morning to evening, then converts the routine to yesterday's "
            "completed events."
        ),
        "key_points": [
            "20 work and school sentences with transliteration and English.",
            "வேண்டும் expresses obligation: கொடுக்க வேண்டும்.",
            "முதல்...வரை marks time spans: எட்டு முதல் ஐந்து வரை.",
            "Dative experiencer: எனக்குப் பிடிக்கும், எனக்குக் கிடைத்தது.",
            "Routine in present, completed events in past.",
        ],
        "requirements": [
            "Narrate your workday or school day in eight Tamil sentences.",
            "Convert your routine sentences to yesterday's past-tense events.",
            "Write five obligation sentences with வேண்டும்.",
            "Describe your job or studies using a time span.",
            "Role-play telling a friend about a promotion.",
        ],
        "standards": [
            "Verb forms follow Lehmann 1989.",
            "Dative experiencer constructions follow Schiffman 1999.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: work is the daily oath renewed - வேண்டும் "
            "the seal of duty, கற்கிறேன் the seal of growth. Where public "
            "vocabulary lists offices, the Signature Word Method files "
            "the craft: every trade a covenant, every lesson a signed "
            "step upward."
        ),
    },
    {
        "key": "health_body",
        "name": "Tamil Health and Body Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Tamil sentences about body parts, symptoms, doctor "
            "visits, and the pharmacy. 1. எனக்குத் தலை வலிக்கிறது. "
            "(Eṉakkut talai valikkiṟatu. - I have a headache - literally "
            "to me the head aches.) 2. என் கண் சிவந்துள்ளது. (Eṉ kaṇ "
            "civant uḷḷatu. - My eye is red.) 3. மூக்கு ஒழுகுகிறது. "
            "(Mūkku oḻukukiṟatu. - My nose is running.) 4. தொண்டை "
            "வலிக்கிறது. (Toṇṭai valikkiṟatu. - My throat hurts.) 5. "
            "எனக்குக் காய்ச்சல் உள்ளது. (Eṉakkuk kāyccal uḷḷatu. - I have "
            "a fever.) 6. இருமல் வருகிறது. (Irumal varukiṟatu. - I have a "
            "cough.) 7. வயிறு வலிக்கிறது. (Vayiṟu valikkiṟatu. - My "
            "stomach hurts.) 8. கால் வீங்கியுள்ளது. (Kāl vīṅkiy uḷḷatu. - "
            "My leg is swollen.) 9. கை எரிகிறது. (Kai erikiṟatu. - My "
            "hand is burning.) 10. மருத்துவரைப் பார்க்க வேண்டும். "
            "(Maruttuvaraip pārkka vēṇṭum. - I need to see a doctor.) 11. "
            "மருத்துவமனை எங்கே? (Maruttuvamaṉai eṅkē? - Where is the "
            "hospital?) 12. மருந்துக் கடை அருகில் உள்ளதா? (Maruntuk kaṭai "
            "arukil uḷḷatā? - Is there a pharmacy nearby?) 13. இந்த "
            "மருந்தை எப்படி எடுப்பது? (Inta maruntai eppaṭi eṭuppatu? - "
            "How do I take this medicine?) 14. உணவுக்குப் பிறகு இரண்டு "
            "மாத்திரை. (Uṇavukkup piṟaku iraṇṭu māttirai. - Two tablets "
            "after food.) 15. தண்ணீர் நிறையக் குடியுங்கள். (Taṇṇīr "
            "niṟaiyak kuṭiyuṅkaḷ. - Drink plenty of water.) 16. ஓய்வு "
            "எடுங்கள். (Ōyvu eṭuṅkaḷ. - Take rest.) 17. உடற்பயிற்சி "
            "செய்யுங்கள். (Uṭaṟpayiṟci ceyyuṅkaḷ. - Do exercise.) 18. என் "
            "இதயம் வேகமாகத் துடிக்கிறது. (Eṉ itayam vēkamākat tuṭikkiṟatu. "
            "- My heart is beating fast.) 19. நான் நன்றாகத் தூங்கினேன். "
            "(Nāṉ naṉṟākat tūṅkiṉēṉ. - I slept well.) 20. இப்போது நன்றாக "
            "உணர்கிறேன். (Ippōtu naṉṟāka uṇarkiṟēṉ. - I feel better now.)"
        ),
        "how_it_works": (
            "This record teaches the body through the dative experiencer "
            "- the construction Tamil uses for feelings and symptoms: "
            "எனக்குத் தலை வலிக்கிறது (to me the head aches), not 'my head "
            "aches'. The learner practices this pattern across ten body "
            "parts so it becomes reflex. The doctor-visit script follows: "
            "asking for the hospital, the pharmacy, dosage instructions - "
            "the sentences a traveler or patient actually needs. "
            "Prescription language (உணவுக்குப் பிறகு, இரண்டு மாத்திரை) "
            "is taught as fixed frames. Health advice closes the record "
            "(drink water, rest, exercise). The drill is a clinic "
            "role-play: one learner is the patient describing symptoms "
            "with எனக்கு, the other is the doctor giving instructions "
            "with respectful commands."
        ),
        "key_points": [
            "20 health and body sentences with transliteration and English.",
            "Symptoms use the dative experiencer: எனக்குத் தலை வலிக்கிறது.",
            "Clinic script: hospital, pharmacy, dosage questions.",
            "Dosage frames: உணவுக்குப் பிறகு + number + மாத்திரை.",
            "Advice uses respectful commands: குடியுங்கள், எடுங்கள்.",
        ],
        "requirements": [
            "Describe three symptoms using the எனக்கு pattern.",
            "Role-play a full doctor visit in Tamil.",
            "Ask for dosage instructions for two medicines.",
            "Name ten body parts in Tamil from memory.",
            "Give health advice to a friend in five sentences.",
        ],
        "standards": [
            "Dative experiencer constructions follow Schiffman 1999.",
            "Medical vocabulary follows standard Tamil usage.",
        ],
        "citations": [CIT_SCHIFFMAN, CIT_LEHMANN],
        "sig_lens": (
            "The Signature read: the body is the first instrument - its "
            "aches the signals it signs. Where public lessons file "
            "symptoms, the Signature Word Method files testimony: "
            "எனக்கு வலிக்கிறது the tongue witnessing truly what the "
            "body reports."
        ),
    },
    {
        "key": "emotions",
        "name": "Tamil Emotions and Feelings Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Tamil sentences about happiness, sadness, anger, "
            "fear, love, and surprise. 1. நான் மிகவும் மகிழ்ச்சியாக "
            "உள்ளேன். (Nāṉ mikavum makiḻcciyāka uḷḷēṉ. - I am very "
            "happy.) 2. செய்தி கேட்டு சிரித்தேன். (Ceyti kēṭṭu "
            "cirittēṉ. - I laughed hearing the news.) 3. எனக்கு வருத்தமாக "
            "உள்ளது. (Eṉakku varuttamāka uḷḷatu. - I feel sad.) 4. அவள் "
            "அழுதாள். (Avaḷ aḻutāḷ. - She cried.) 5. எனக்குக் கோபம் "
            "வருகிறது. (Eṉakkuk kōpam varukiṟatu. - I am getting angry - "
            "literally anger comes to me.) 6. அவன் கத்தினான். (Avaṉ "
            "kattiṉāṉ. - He shouted.) 7. எனக்குப் பயமாக உள்ளது. "
            "(Eṉakkup payamāka uḷḷatu. - I am afraid.) 8. இருட்டில் "
            "தனியாகப் பயந்தேன். (Iruṭṭil taṉiyākap payantēṉ. - I was "
            "scared alone in the dark.) 9. நான் உன்னை நேசிக்கிறேன். "
            "(Nāṉ uṉṉai nēcikkiṟēṉ. - I love you.) 10. அவர்கள் ஒருவரை "
            "ஒருவர் நேசிக்கிறார்கள். (Avarkaḷ oruvarai oruvar "
            "nēcikkiṟārkaḷ. - They love each other.) 11. எனக்கு "
            "ஆச்சரியமாக உள்ளது. (Eṉakku āccariyamāka uḷḷatu. - I am "
            "surprised.) 12. அதைக் கேட்டு வியந்தேன். (Ataik kēṭṭu "
            "viyantēṉ. - I was amazed hearing it.) 13. நான் பெருமைப்படு"
            "கிறேன். (Nāṉ perumaippaṭukiṟēṉ. - I am proud.) 14. எனக்கு "
            "நம்பிக்கை உள்ளது. (Eṉakku nampikkai uḷḷatu. - I have hope.) "
            "15. மனம் அமைதியாக உள்ளது. (Maṉam amaitiyāka uḷḷatu. - My "
            "mind is calm.) 16. நான் பதற்றமாக உள்ளேன். (Nāṉ pataṟṟamāka "
            "uḷḷēṉ. - I am nervous.) 17. அவளுக்குப் பொறாமை. (Avaḷukkup "
            "poṟāmai. - She is jealous.) 18. எனக்கு நன்றி உணர்வு உள்ளது. "
            "(Eṉakku naṉṟi uṇarvu uḷḷatu. - I feel grateful.) 19. நாம் "
            "சேர்ந்து மகிழ்வோம். (Nām cērntu makiḻvōm. - Let us rejoice "
            "together.) 20. உணர்வுகளைப் பகிர்ந்து கொள். (Uṇarvukaḷaip "
            "pakirntu koḷ. - Share your feelings.)"
        ),
        "how_it_works": (
            "This record teaches emotions through Tamil's two great "
            "patterns. Pattern one is the dative experiencer - feelings "
            "happen TO you: எனக்குக் கோபம் வருகிறது (anger comes to "
            "me), எனக்குப் பயமாக உள்ளது (to me it is fearful). Pattern "
            "two is the -ஆக உள்ளேன் frame: மகிழ்ச்சியாக உள்ளேன், "
            "பதற்றமாக உள்ளேன். The record moves through the six basic "
            "emotions - joy, sadness, anger, fear, love, surprise - then "
            "adds pride, hope, calm, nervousness, jealousy, gratitude. "
            "நேசி (love) is taught with the accusative -ஐ it requires "
            "(உன்னை நேசிக்கிறேன்). The drill is emotional storytelling: "
            "the learner narrates their week naming one feeling per day "
            "in Tamil, using both patterns."
        ),
        "key_points": [
            "20 emotion sentences with transliteration and English.",
            "Feelings use the dative experiencer: எனக்குக் கோபம் வருகிறது.",
            "The -ஆக உள்ளேன் frame states feelings: மகிழ்ச்சியாக உள்ளேன்.",
            "நேசி takes the accusative: உன்னை நேசிக்கிறேன்.",
            "Covers joy, sadness, anger, fear, love, surprise, and more.",
        ],
        "requirements": [
            "Narrate your week naming one feeling per day in Tamil.",
            "Convert five நான்-feeling sentences to எனக்கு-feeling sentences.",
            "Write a short love note in Tamil using நேசி.",
            "Describe a surprising event with ஆச்சரியம் and வியப்பு.",
            "Comfort a sad friend in five Tamil sentences.",
        ],
        "standards": [
            "Emotion constructions follow Schiffman 1999.",
            "Dative experiencer usage follows Lehmann 1989.",
        ],
        "citations": [CIT_SCHIFFMAN, CIT_LEHMANN],
        "sig_lens": (
            "The Signature read: feelings are the unsigned letters of "
            "the heart - the tongue signs them into the world. Where "
            "public lessons file adjectives, the Signature Word Method "
            "files confessions: மகிழ்ச்சியாக உள்ளேன் the seal of joy "
            "truly witnessed."
        ),
    },
    {
        "key": "nature_weather",
        "name": "Tamil Nature and Weather Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Tamil sentences about animals, plants, seasons, and "
            "weather talk. 1. இன்று வெயில் அதிகம். (Iṉṟu veyil atikam. - "
            "Today is very sunny.) 2. நேற்று மழை பெய்தது. (Nēṟṟu maḻai "
            "peytatu. - Yesterday it rained.) 3. நாளை மழை வரும். (Nāḷai "
            "maḻai varum. - It will rain tomorrow.) 4. காற்று வீசுகிறது. "
            "(Kāṟṟu vīcukiṟatu. - The wind is blowing.) 5. வானம் மேகமூட்டமாக "
            "உள்ளது. (Vāṉam mēkamūṭṭamāka uḷḷatu. - The sky is cloudy.) "
            "6. இடி இடிக்கிறது. (Iṭi iṭikkiṟatu. - It is thundering.) 7. "
            "மின்னல் மின்னுகிறது. (Miṉṉal miṉṉukiṟatu. - Lightning is "
            "flashing.) 8. குளிர் காலம் வந்துவிட்டது. (Kuḷir kālam "
            "vantuviṭṭatu. - Winter has come.) 9. கோடையில் வெப்பம் அதிகம். "
            "(Kōṭaiyil veppam atikam. - It is very hot in summer.) 10. "
            "மரங்கள் பசுமையாக உள்ளன. (Maraṅkaḷ pacumaiyāka uḷḷaṉa. - The "
            "trees are green.) 11. பூக்கள் மணம் வீசுகின்றன. (Pūkkaḷ "
            "maṇam vīcukiṉṟaṉa. - The flowers are fragrant.) 12. ஆற்றில் "
            "நீர் ஓடுகிறது. (Āṟṟil nīr ōṭukiṟatu. - Water flows in the "
            "river.) 13. கடல் அலைகள் பெரியவை. (Kaṭal alaikaḷ periyavai. "
            "- The sea waves are big.) 14. மலை உயரமானது. (Malai "
            "uyaramāṉatu. - The mountain is tall.) 15. காட்டில் யானை "
            "உள்ளது. (Kāṭṭil yāṉai uḷḷatu. - There is an elephant in the "
            "forest.) 16. குரங்கு மரத்தில் தாவுகிறது. (Kuraṅku marattil "
            "tāvukiṟatu. - The monkey is jumping in the tree.) 17. மயில் "
            "அழகாக ஆடுகிறது. (Mayil aḻakāka āṭukiṟatu. - The peacock "
            "dances beautifully.) 18. பசு பால் கொடுக்கிறது. (Pacu pāl "
            "koṭukkiṟatu. - The cow gives milk.) 19. நாய் குரைக்கிறது. "
            "(Nāy kuraikkiṟatu. - The dog is barking.) 20. இயற்கை மிகவும் "
            "அழகானது. (Iyaṟkai mikavum aḻakāṉatu. - Nature is very "
            "beautiful.)"
        ),
        "how_it_works": (
            "This record teaches nature through weather talk - the "
            "universal small talk that opens conversations in every "
            "language. Tamil weather verbs are taught as a set: மழை "
            "பெய்கிறது (it rains), காற்று வீசுகிறது (wind blows), இடி "
            "இடிக்கிறது (it thunders) - each a complete sentence with no "
            "subject needed, like English 'it is raining'. The seasons "
            "from the numbers record return in sentences (கோடை, குளிர் "
            "காலம்). Plants and landscape follow (மரம், பூ, ஆறு, கடல், "
            "மலை), then animals with their characteristic verbs: "
            "யானை, குரங்கு தாவுகிறது, மயில் ஆடுகிறது, பசு பால் "
            "கொடுக்கிறது, நாய் குரைக்கிறது. The drill is a nature walk: "
            "the learner describes what they see outside, in season, in "
            "Tamil - weather first, then plants, then animals."
        ),
        "key_points": [
            "20 nature and weather sentences with transliteration and English.",
            "Weather verbs need no subject: மழை பெய்கிறது.",
            "Seasons return in sentences: கோடை, குளிர் காலம்.",
            "Animals pair with characteristic verbs: மயில் ஆடுகிறது.",
            "Weather talk is taught as conversation openers.",
        ],
        "requirements": [
            "Describe today's weather in five Tamil sentences.",
            "Take a nature walk and name ten things in Tamil.",
            "Write a four-season paragraph in Tamil.",
            "Pair eight animals with their characteristic verbs.",
            "Start three conversations with weather observations.",
        ],
        "standards": [
            "Nature vocabulary follows standard Tamil usage.",
            "Weather constructions follow Schiffman 1999.",
        ],
        "citations": [CIT_SCHIFFMAN, CIT_LEHMANN],
        "sig_lens": (
            "The Signature read: nature is the original archive - older "
            "than any script, signed in every leaf. Where public lessons "
            "file weather words, the Signature Word Method files "
            "witness: மழை பெய்கிறது the sky signing its own sentence."
        ),
    },
    {
        "key": "shopping_money",
        "name": "Tamil Shopping and Money Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Tamil sentences about markets, prices, bargaining, "
            "and paying. 1. சந்தை எங்கே? (Cantai eṅkē? - Where is the "
            "market?) 2. கடை எத்தனை மணிக்குத் திறக்கும்? (Kaṭai ettaṉai "
            "maṇikkut tiṟakkum? - At what time does the shop open?) 3. "
            "இது எவ்வளவு? (Itu evvaḷavu? - How much is this?) 4. அது "
            "மிகவும் விலை அதிகம். (Atu mikavum vilai atikam. - That is "
            "too expensive.) 5. கொஞ்சம் குறையுங்கள். (Koñcam kuṟaiyuṅkaḷ. "
            "- Please reduce a little - bargaining.) 6. கடைசி விலை "
            "என்ன? (Kaṭaici vilai eṉṉa? - What is the final price?) 7. "
            "இரண்டு கிலோ தக்காளி கொடுங்கள். (Iraṇṭu kilō takkāḷi "
            "koṭuṅkaḷ. - Please give two kilos of tomatoes.) 8. புதியது "
            "உள்ளதா? (Putiyatu uḷḷatā? - Is there a fresh one?) 9. வேறு "
            "நிறம் காட்டுங்கள். (Vēṟu niṟam kāṭṭuṅkaḷ. - Please show "
            "another color.) 10. பெரிய அளவு வேண்டும். (Periya aḷavu "
            "vēṇṭum. - I need a large size.) 11. இதைப் பார்க்கலாமா? "
            "(Itaip pārkkalāmā? - May I see this?) 12. பில் கொடுங்கள். "
            "(Pil koṭuṅkaḷ. - Please give the bill.) 13. பணம் ரொக்கமாகக் "
            "கொடுக்கிறேன். (Paṇam rokkamākak koṭukkiṟēṉ. - I will pay in "
            "cash.) 14. அட்டையில் செலுத்தலாமா? (Aṭṭaiyil celuttalāmā? - "
            "Can I pay by card?) 15. மீதிப் பணம் கொடுங்கள். (Mītip paṇam "
            "koṭuṅkaḷ. - Please give the change.) 16. ரசீது வேண்டும். "
            "(Racītu vēṇṭum. - I need a receipt.) 17. தள்ளுபடி உள்ளதா? "
            "(Taḷḷupaṭi uḷḷatā? - Is there a discount?) 18. நாளை மீண்டும் "
            "வருவேன். (Nāḷai mīṇṭum varuvēṉ. - I will come again "
            "tomorrow.) 19. உங்கள் கடை மிகவும் நல்லது. (Uṅkaḷ kaṭai "
            "mikavum nallatu. - Your shop is very good.) 20. நன்றி, "
            "வணக்கம். (Naṉṟi, vaṇakkam. - Thank you, goodbye.)"
        ),
        "how_it_works": (
            "This record teaches shopping as a negotiation in five "
            "moves: find (சந்தை எங்கே), ask (இது எவ்வளவு), bargain "
            "(கொஞ்சம் குறையுங்கள், கடைசி விலை என்ன), specify (இரண்டு "
            "கிலோ, வேறு நிறம், பெரிய அளவு), and pay (ரொக்கம், அட்டை, "
            "மீதிப் பணம், ரசீது). Bargaining language is taught as "
            "polite ritual - கொஞ்சம் குறையுங்கள் keeps the respectful "
            "form even while haggling. Quantity words (கிலோ, அளவு) and "
            "quality checks (புதியது உள்ளதா, இதைப் பார்க்கலாமா) make the "
            "learner a competent buyer. The drill is a market day: the "
            "learner role-plays buyer and seller through three "
            "purchases, bargaining each one down politely."
        ),
        "key_points": [
            "20 shopping sentences covering market, price, bargaining, payment.",
            "Bargaining stays polite: கொஞ்சம் குறையுங்கள், கடைசி விலை என்ன.",
            "Quantities: கிலோ for weight, அளவு for size.",
            "Payment options: ரொக்கம் (cash), அட்டை (card), மீதிப் பணம் (change).",
            "தள்ளுபடி (discount) and ரசீது (receipt) complete the purchase.",
        ],
        "requirements": [
            "Role-play buying vegetables with bargaining in Tamil.",
            "Ask prices for five items using எவ்வளவு.",
            "Buy clothing specifying size and color in Tamil.",
            "Pay by cash and by card, asking for change and receipt.",
            "Write a shopping list with quantities in Tamil.",
        ],
        "standards": [
            "Market vocabulary follows standard modern Tamil.",
            "Polite request forms follow Schiffman 1999.",
        ],
        "citations": [CIT_SCHIFFMAN, CIT_LEHMANN],
        "sig_lens": (
            "The Signature read: trade is the covenant of value - every "
            "price a proposed seal, every bargain a negotiation of "
            "truth. Where public lessons file shopping phrases, the "
            "Signature Word Method files fair dealing: கடைசி விலை the "
            "final signature on the exchange."
        ),
    },
    {
        "key": "friendship_social",
        "name": "Tamil Friendship and Social Life Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Tamil sentences about meeting people, invitations, "
            "and celebrations. 1. உங்களைச் சந்தித்ததில் மகிழ்ச்சி. "
            "(Uṅkaḷaic cantittatil makiḻcci. - Nice to meet you.) 2. "
            "நாம் நண்பர்களாக இருப்போம். (Nām naṇparkaḷāka iruppōm. - Let "
            "us be friends.) 3. என் வீட்டுக்கு வாருங்கள். (Eṉ vīṭṭukku "
            "vāruṅkaḷ. - Please come to my house.) 4. நாளை மாலை "
            "சந்திக்கலாமா? (Nāḷai mālai cantikkalāmā? - Shall we meet "
            "tomorrow evening?) 5. காபி குடிக்கலாம். (Kāpi kuṭikkalām. - "
            "Let us have coffee.) 6. சினிமாவுக்குப் போகலாமா? (Ciṉimāvukkup "
            "pōkalāmā? - Shall we go to a movie?) 7. உங்கள் குடும்பம் "
            "எப்படி? (Uṅkaḷ kuṭumpam eppaṭi? - How is your family?) 8. "
            "நீண்ட நாட்களாகப் பார்க்கவில்லை. (Nīṇṭa nāṭkaḷākap "
            "pārkkavillai. - Long time no see.) 9. உங்களை நினைத்தேன். "
            "(Uṅkaḷai niṉaittēṉ. - I thought of you.) 10. பிறந்தநாள் "
            "வாழ்த்துக்கள். (Piṟantanāḷ vāḻttukkaḷ. - Happy birthday.) 11. "
            "பரிசு உங்களுக்கு. (Paricu uṅkaḷukku. - This gift is for you.) "
            "12. விருந்துக்கு வாருங்கள். (Viruntukku vāruṅkaḷ. - Please "
            "come to the feast/party.) 13. சாப்பிட்டுவிட்டுப் போங்கள். "
            "(Cāppiṭṭuviṭṭup pōṅkaḷ. - Please eat and then go - the Tamil "
            "insistence on feeding guests.) 14. மீண்டும் வாருங்கள். "
            "(Mīṇṭum vāruṅkaḷ. - Please come again.) 15. உங்கள் உதவிக்கு "
            "நன்றி. (Uṅkaḷ utavikku naṉṟi. - Thanks for your help.) 16. "
            "நான் உங்களோடு இருக்கிறேன். (Nāṉ uṅkaḷōṭu irukkiṟēṉ. - I am "
            "with you.) 17. கவலைப்படாதீர்கள். (Kavalaippaṭātīrkaḷ. - Do "
            "not worry.) 18. எல்லாம் சரியாகும். (Ellām cariyākum. - "
            "Everything will be fine.) 19. நண்பர்கள் என்றும் உடனிருப்போம். "
            "(Naṇparkaḷ eṉṟum uṭaṉiruppōm. - We friends will always stand "
            "together.) 20. பிரிவு கடினமானது. (Pirivu kaṭiṉamāṉatu. - "
            "Parting is hard.)"
        ),
        "how_it_works": (
            "This record teaches friendship as invitation and loyalty. "
            "Meeting phrases open it (சந்தித்ததில் மகிழ்ச்சி, நீண்ட "
            "நாட்களாகப் பார்க்கவில்லை), then come the invitations that "
            "build Tamil social life - வீட்டுக்கு வாருங்கள், காபி "
            "குடிக்கலாம், சினிமாவுக்குப் போகலாமா - all using the "
            "suggestive -லாம் form (let us / shall we). Celebrations "
            "follow: birthdays, gifts, feasts, with சாப்பிட்டுவிட்டுப் "
            "போங்கள் teaching the Tamil rule that no guest leaves "
            "unfed. Comfort phrases close it (கவலைப்படாதீர்கள், எல்லாம் "
            "சரியாகும்). The drill is social: the learner invites a "
            "real friend to coffee in Tamil, hosts a small gathering "
            "with Tamil invitations, and writes a birthday wish."
        ),
        "key_points": [
            "20 friendship sentences with transliteration and English.",
            "The -லாம் form makes suggestions: போகலாமா, குடிக்கலாம்.",
            "சாப்பிட்டுவிட்டுப் போங்கள்: no guest leaves unfed.",
            "நீண்ட நாட்களாகப் பார்க்கவில்லை is long-time-no-see.",
            "Comfort phrases: கவலைப்படாதீர்கள், எல்லாம் சரியாகும்.",
        ],
        "requirements": [
            "Invite a friend to coffee using the -லாம் form.",
            "Write birthday wishes for three people in Tamil.",
            "Role-play hosting a guest: welcome, feed, farewell.",
            "Comfort a worried friend in five Tamil sentences.",
            "Reconnect with an old friend using நீண்ட நாட்களாக.",
        ],
        "standards": [
            "Social phrases follow standard Tamil usage per Schiffman 1999.",
            "The -லாம் suggestive follows Lehmann 1989.",
        ],
        "citations": [CIT_SCHIFFMAN, CIT_LEHMANN],
        "sig_lens": (
            "The Signature read: friendship is the covenant of presence "
            "- நாம் the seal that includes, உடனிருப்போம் the oath to "
            "stand together. Where public lessons file social phrases, "
            "the Signature Word Method files loyalty: every invitation "
            "a signed promise of welcome."
        ),
    },
    {
        "key": "technology",
        "name": "Tamil Technology and Communication Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Tamil sentences about phones, internet, computers, "
            "and messaging. 1. என் கைபேசி எங்கே? (Eṉ kaipēci eṅkē? - "
            "Where is my phone?) 2. தொலைபேசியில் பேசலாமா? (Tolaipēciyil "
            "pēcalāmā? - Can we talk on the phone?) 3. என்னை அழையுங்கள். "
            "(Eṉṉai aḻaiyuṅkaḷ. - Please call me.) 4. சமிக்ஞை இல்லை. "
            "(Camikñai illai. - There is no signal.) 5. மின்கலம் "
            "தீர்ந்துவிட்டது. (Miṉkalam tīrntuviṭṭatu. - The battery is "
            "dead.) 6. குறுஞ்செய்தி அனுப்பினேன். (Kuṟuñceyti aṉuppiṉēṉ. - "
            "I sent a text message.) 7. மின்னஞ்சல் பார்த்தீர்களா? "
            "(Miṉṉañcal pārttīrkaḷā? - Did you check the email?) 8. "
            "இணையம் வேகமாக உள்ளது. (Iṇaiyam vēkamāka uḷḷatu. - The "
            "internet is fast.) 9. கடவுச்சொல் மறந்துவிட்டேன். "
            "(Kaṭavuccol maṟantuviṭṭēṉ. - I forgot the password.) 10. "
            "கணினியை இயக்குங்கள். (Kaṇiṉiyai iyakkuṅkaḷ. - Please turn on "
            "the computer.) 11. திரை உறைந்துவிட்டது. (Tirai "
            "uṟaintuviṭṭatu. - The screen is frozen.) 12. கோப்பைச் "
            "சேமியுங்கள். (Kōppaic cēmiyuṅkaḷ. - Please save the file.) 13. "
            "புகைப்படம் எடுக்கலாமா? (Pukaippaṭam eṭukkalāmā? - May I take "
            "a photo?) 14. காணொளி அழைப்பு செய்வோம். (Kāṇoḷi aḻaippu "
            "ceyvōm. - Let us make a video call.) 15. செயலி பதிவிறக்கு. "
            "(Ceyali pativiṟakku. - Download the app.) 16. மென்பொருள் "
            "புதுப்பிக்கப்பட்டது. (Meṉporuḷ putuppikkappaṭṭatu. - The "
            "software was updated.) 17. அச்சுப்பொறி வேலை செய்யவில்லை. "
            "(Accuppoṟi vēlai ceyyavillai. - The printer is not working.) "
            "18. இணைப்பைத் துண்டியுங்கள். (Iṇaippait tuṇṭiyuṅkaḷ. - Please "
            "disconnect.) 19. மீண்டும் தொடங்குங்கள். (Mīṇṭum "
            "toṭaṅkuṅkaḷ. - Please restart.) 20. தொழில்நுட்பம் வாழ்க்கையை "
            "எளிதாக்குகிறது. (Toḻilnuṭpam vāḻkkaiyai eḷitākkiṟatu. - "
            "Technology makes life easier.)"
        ),
        "how_it_works": (
            "This record teaches technology through Tamil's own coined "
            "words - கைபேசி (hand-phone), மின்னஞ்சல் (lightning-mail for "
            "email), கணினி (computer), இணையம் (internet) - showing the "
            "learner that Tamil builds its own vocabulary rather than "
            "only borrowing. Problem sentences form the troubleshooting "
            "script every user needs: no signal, dead battery, frozen "
            "screen, forgotten password, printer not working - each with "
            "its fix command (இயக்குங்கள், சேமியுங்கள், துண்டியுங்கள், "
            "தொடங்குங்கள்). Communication verbs (அழை, அனுப்பு, பேசு) "
            "recur in tech contexts. The drill is a help desk: one "
            "learner reports a tech problem in Tamil, the other gives "
            "the fix commands, entirely in Tamil."
        ),
        "key_points": [
            "20 technology sentences with transliteration and English.",
            "Tamil coins its own tech words: கைபேசி, மின்னஞ்சல், கணினி, இணையம்.",
            "Troubleshooting script: problem sentence + fix command.",
            "Fix commands: இயக்குங்கள், சேமியுங்கள், துண்டியுங்கள், தொடங்குங்கள்.",
            "Communication verbs recur: அழை, அனுப்பு, பேசு.",
        ],
        "requirements": [
            "Report three tech problems and their fixes in Tamil.",
            "Role-play a help desk call entirely in Tamil.",
            "Write instructions for downloading an app in five steps.",
            "Ask a friend for a video call using காணொளி அழைப்பு.",
            "List ten Tamil tech words with their literal meanings.",
        ],
        "standards": [
            "Technical vocabulary follows standard Tamil computing usage.",
            "Command forms follow Lehmann 1989.",
        ],
        "citations": [CIT_LEHMANN, CIT_ANNAMALAI],
        "sig_lens": (
            "The Signature read: the coined word is the signature of a "
            "living tongue - மின்னஞ்சல் proof the language signs new "
            "things rather than borrowing names. Where public lessons "
            "file tech terms, the Signature Word Method files invention: "
            "every new word a fresh seal on the world."
        ),
    },
    {
        "key": "verb_tenses",
        "name": "Tamil Verb Tenses in Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Tamil verb tenses - present, past, future, and negatives - "
            "with five or more translated sentences per tense. Tamil "
            "marks tense between the root and the person ending: present "
            "-கிற்-, past -த்-/-ந்த்-/-ன்-, future -வ்-/-ப்-. Present "
            "(-கிற்-): 1. நான் தமிழ் கற்கிறேன். (I am learning Tamil.) 2. "
            "அவன் பள்ளிக்குப் போகிறான். (He goes to school.) 3. அவள் "
            "பாட்டுப் பாடுகிறாள். (She is singing a song.) 4. நாங்கள் "
            "சாப்பிடுகிறோம். (We are eating.) 5. மழை பெய்கிறது. (It is "
            "raining.) 6. நீங்கள் எங்கே இருக்கிறீர்கள்? (Where are you?) "
            "Past: 1. நான் நேற்று வந்தேன். (I came yesterday.) 2. அவன் "
            "சாப்பிட்டான். (He ate.) 3. அவள் படித்தாள். (She studied.) 4. "
            "நாங்கள் பார்த்தோம். (We saw.) 5. மழை பெய்தது. (It rained.) "
            "6. நீங்கள் சொன்னீர்கள். (You said.) Future: 1. நான் நாளை "
            "வருவேன். (I will come tomorrow.) 2. அவன் போவான். (He will "
            "go.) 3. அவள் பாடுவாள். (She will sing.) 4. நாங்கள் "
            "செய்வோம். (We will do.) 5. மழை வரும். (It will rain.) 6. "
            "நீங்கள் வருவீர்கள். (You will come.) Negatives: present "
            "negative uses -ஆ-/-இல்லை: நான் வரவில்லை. (I am not coming.) "
            "Future negative uses -மாட்ட்-: நான் வரமாட்டேன். (I will not "
            "come.) Prohibition uses -ஆதே: போகாதே. (Do not go.) The "
            "person endings stay constant across tenses: -ஏன் (I), -ஆய் "
            "(you inf), -ஆன் (he), -ஆள் (she), -அது (it), -ஓம் (we), "
            "-ஈர்கள் (you formal), -ஆர்கள் (they)."
        ),
        "how_it_works": (
            "This record teaches tense as a sandwich: root + tense "
            "marker + person ending. The learner holds the person "
            "endings constant (they already know -ஏன், -ஆன், -ஆள் from "
            "the verbs record) and swaps only the middle: வா + கிற் + "
            "ஏன் = வருகிறேன், வா + ந்த் + ஏன் = வந்தேன், வா + வ் + ஏன் = "
            "வருவேன். Four model verbs are conjugated fully across all "
            "three tenses - வா (come), போ (go), செய் (do), சாப்பிடு "
            "(eat) - so the learner sees both regular patterns and the "
            "small irregularities (வா takes -ந்த்- in the past, not "
            "-த்-). Negatives are taught as three separate tools for "
            "three jobs: -வில்லை for past/present denial, -மாட்ட்- for "
            "future refusal, -ஆதே for commands. The drill is tense "
            "shifting: take any present sentence and move it to "
            "yesterday and tomorrow."
        ),
        "key_points": [
            "Tense markers: present -கிற்-, past -த்-/-ந்த்-/-ன்-, future -வ்-.",
            "Person endings are constant across tenses: -ஏன், -ஆன், -ஆள், -அது.",
            "வா is irregular in the past: வந்தேன், not வாதேன்.",
            "Negatives: -வில்லை (denial), -மாட்ட்- (future refusal), -ஆதே (prohibition).",
            "Four model verbs conjugated fully: வா, போ, செய், சாப்பிடு.",
        ],
        "requirements": [
            "Conjugate வா, போ, செய், சாப்பிடு in all three tenses for I, he, she.",
            "Shift ten present sentences to past and future.",
            "Negate five sentences with each of the three negative tools.",
            "Narrate yesterday, today, and tomorrow in six sentences each.",
            "Explain the வந்தேன் irregularity in your own words.",
        ],
        "standards": [
            "Tense formation follows Lehmann 1989 verb classes.",
            "Past-tense allomorphs follow the Tolkappiyam analysis.",
        ],
        "citations": [CIT_LEHMANN, CIT_TOLKAPPIYAM, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: tense is the seal of time - the middle "
            "syllable signing when the deed was done. Where public "
            "tables file forms, the Signature Word Method files "
            "testimony: வந்தேன் the tongue swearing I came, வருவேன் "
            "swearing I shall."
        ),
    },
    {
        "key": "questions_answers",
        "name": "Tamil Questions and Answers",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Tamil question-and-answer pairs covering who, what, "
            "where, when, why, and how. 1. உங்கள் பெயர் என்ன? - என் பெயர் "
            "ராஜா. (What is your name? - My name is Raja.) 2. நீங்கள் "
            "எங்கிருந்து வருகிறீர்கள்? - நான் சென்னையிலிருந்து "
            "வருகிறேன். (Where are you from? - I am from Chennai.) 3. "
            "உங்களுக்கு எத்தனை வயது? - எனக்கு இருபத்தைந்து வயது. (How "
            "old are you? - I am 25.) 4. நீங்கள் என்ன செய்கிறீர்கள்? - "
            "நான் ஆசிரியர். (What do you do? - I am a teacher.) 5. இது "
            "என்ன? - இது புத்தகம். (What is this? - This is a book.) 6. "
            "யார் வந்தது? - என் நண்பர் வந்தார். (Who came? - My friend "
            "came.) 7. எங்கே போகிறீர்கள்? - கடைக்குப் போகிறேன். (Where "
            "are you going? - I am going to the shop.) 8. எப்போது "
            "வருவீர்கள்? - நாளை வருவேன். (When will you come? - I will "
            "come tomorrow.) 9. ஏன் தாமதம்? - பேருந்து தாமதமானது. (Why "
            "late? - The bus was late.) 10. எப்படி இருக்கிறீர்கள்? - "
            "நன்றாக இருக்கிறேன். (How are you? - I am well.) 11. நீங்கள் "
            "தமிழ் பேசுவீர்களா? - ஆம், கொஞ்சம் பேசுவேன். (Do you speak "
            "Tamil? - Yes, I speak a little.) 12. இது உங்களுடையதா? - "
            "ஆம், என்னுடையது. (Is this yours? - Yes, it is mine.) 13. "
            "சாப்பிட்டீர்களா? - ஆம், சாப்பிட்டேன். (Have you eaten? - "
            "Yes, I have eaten.) 14. எது நல்லது? - இது நல்லது. (Which is "
            "good? - This is good.) 15. எவ்வளவு தூரம்? - ஐந்து கிலோமீட்டர். "
            "(How far? - Five kilometers.) 16. யாரோடு வந்தீர்கள்? - என் "
            "மனைவியோடு வந்தேன். (With whom did you come? - I came with "
            "my wife.) 17. என்ன வேண்டும்? - தண்ணீர் வேண்டும். (What do "
            "you want? - I want water.) 18. எத்தனை பேர்? - நான்கு பேர். "
            "(How many people? - Four people.) 19. எந்தப் புத்தகம்? - "
            "சிவப்புப் புத்தகம். (Which book? - The red book.) 20. "
            "புரிகிறதா? - ஆம், புரிகிறது. (Do you understand? - Yes, I "
            "understand.)"
        ),
        "how_it_works": (
            "This record teaches questions in three families. Family "
            "one: எ- question words (யார், என்ன, எங்கே, எப்போது, ஏன், "
            "எப்படி, எது, எவ்வளவு, எத்தனை, எந்த) - each paired with the "
            "answer shape it expects. Family two: yes/no questions "
            "formed by adding -ஆ to the verb (பேசுவீர்களா, "
            "உங்களுடையதா), answered with ஆம் or இல்லை. Family three: "
            "tag-like confirmations (புரிகிறதா). The record moves from "
            "identity (name, origin, age, work) to location and time to "
            "choice and quantity - the order a real conversation "
            "follows. Each answer models the full-sentence reply Tamil "
            "prefers. The drill is an interview: the learner asks a "
            "partner all twenty questions and answers them back, then "
            "conducts the same interview with a stranger's patience."
        ),
        "key_points": [
            "20 question-answer pairs across who/what/where/when/why/how.",
            "எ- words ask open questions; -ஆ makes yes/no questions.",
            "Answers model full Tamil sentences, not fragments.",
            "எத்தனை asks how many; எவ்வளவு asks how much/how far.",
            "யாரோடு (with whom) shows case stacking on question words.",
        ],
        "requirements": [
            "Interview a partner with all twenty questions.",
            "Answer each question about yourself in full sentences.",
            "Convert five எ- questions to -ஆ yes/no questions.",
            "Ask for directions using three different எ- words.",
            "Write a self-introduction answering the first five questions.",
        ],
        "standards": [
            "Question formation follows Lehmann 1989.",
            "Interrogative paradigms follow Schiffman 1999.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: the question is the open seal - எ the "
            "mark of the seeker, -ஆ the knock on the door. Where public "
            "lists file interrogatives, the Signature Word Method files "
            "the quest: every question a signed admission that there is "
            "more to know."
        ),
    },
    {
        "key": "commands_requests",
        "name": "Tamil Commands and Requests",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Tamil imperatives and polite requests, formal versus "
            "informal. Informal (to friends, children): 1. வா. (Vā. - "
            "Come.) 2. போ. (Pō. - Go.) 3. உட்கார். (Uṭkār. - Sit.) 4. "
            "சாப்பிடு. (Cāppiṭu. - Eat.) 5. குடி. (Kuṭi. - Drink.) 6. "
            "பார். (Pār. - Look.) 7. சொல். (Col. - Say/tell.) 8. எழுது. "
            "(Eḻutu. - Write.) 9. நில். (Nil. - Stand/stop.) 10. கொடு. "
            "(Koṭu. - Give.) Formal/respectful (to elders, strangers): "
            "11. வாருங்கள். (Vāruṅkaḷ. - Please come.) 12. போங்கள். "
            "(Pōṅkaḷ. - Please go.) 13. உட்காருங்கள். (Uṭkāruṅkaḷ. - "
            "Please sit.) 14. சாப்பிடுங்கள். (Cāppiṭuṅkaḷ. - Please eat.) "
            "15. சொல்லுங்கள். (Colluṅkaḷ. - Please tell.) 16. "
            "தயவுசெய்து காத்திருங்கள். (Tayavuceytu kāttiruṅkaḷ. - Please "
            "wait.) 17. மெதுவாகப் பேசுங்கள். (Metuvākap pēcuṅkaḷ. - "
            "Please speak slowly.) 18. மீண்டும் சொல்லுங்கள். (Mīṇṭum "
            "colluṅkaḷ. - Please say it again.) 19. உதவி செய்யுங்கள். "
            "(Utavi ceyyuṅkaḷ. - Please help.) 20. மன்னித்துவிடுங்கள். "
            "(Maṉṉittuviṭuṅkaḷ. - Please forgive.) Prohibitions: informal "
            "போகாதே (do not go), formal போகாதீர்கள் (please do not go). "
            "The informal command is the bare root; the formal adds "
            "-உங்கள்; தயவுசெய்து softens any request."
        ),
        "how_it_works": (
            "This record teaches the command ladder: bare root for "
            "intimates (வா, போ, கொடு), -உங்கள் for respect (வாருங்கள், "
            "போங்கள்), தயவுசெய்து + -உங்கள் for formal requests, and "
            "-ஆதே/-ஆதீர்கள் for prohibitions. The learner first masters "
            "the ten informal roots - they are also the dictionary "
            "forms, so this doubles as verb-root review - then learns "
            "the single transformation to formal. The critical social "
            "rule is drilled hard: using வா to an elder is rude; using "
            "வாருங்கள் to a close friend is cold. Requests for service "
            "(wait, speak slowly, say again, help, forgive) are taught "
            "as the traveler's toolkit. The drill is role reversal: the "
            "learner commands a friend, then requests the same things "
            "from an elder, feeling the register shift."
        ),
        "key_points": [
            "20 imperatives: 10 informal roots, 10 formal -உங்கள் forms.",
            "Informal command = bare verb root: வா, போ, கொடு.",
            "Formal adds -உங்கள்: வாருங்கள், போங்கள்.",
            "தயவுசெய்து softens requests; -ஆதே/-ஆதீர்கள் prohibit.",
            "Wrong register is rude or cold - the social rule matters.",
        ],
        "requirements": [
            "Give ten informal commands to a friend in role-play.",
            "Convert them all to formal requests for an elder.",
            "Prohibit five actions in both informal and formal.",
            "Ask for help, slower speech, and repetition politely.",
            "Write classroom commands a teacher would use.",
        ],
        "standards": [
            "Imperative formation follows Lehmann 1989.",
            "Politeness registers follow Schiffman 1999.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: the command is the seal of authority - "
            "வா the order of equals, வாருங்கள் the honor of distance. "
            "Where public tables file moods, the Signature Word Method "
            "files the weight of words: every imperative a signed "
            "measure of the bond between speaker and hearer."
        ),
    },
    {
        "key": "descriptions",
        "name": "Tamil Descriptions of People and Places",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Tamil sentences describing people, places, and "
            "things in detail. 1. என் நண்பர் உயரமானவர், சிரித்த முகம் "
            "உடையவர். (Eṉ naṇpar uyaramāṉavar, ciritta mukam uṭaiyavar. - "
            "My friend is tall and has a smiling face.) 2. அவள் நீண்ட "
            "முடி உடையவள். (Avaḷ nīṇṭa muṭi uṭaiyavaḷ. - She has long "
            "hair.) 3. தாத்தாவுக்கு வெள்ளை தாடி உள்ளது. (Tāttāvukku "
            "veḷḷai tāṭi uḷḷatu. - Grandfather has a white beard.) 4. "
            "குழந்தை சுறுசுறுப்பானது. (Kuḻantai cuṟucuṟuppāṉatu. - The "
            "child is lively.) 5. ஆசிரியர் கண்டிப்பானவர் ஆனால் அன்பானவர். "
            "(Āciriyar kaṇṭippāṉavar āṉāl aṉpāṉavar. - The teacher is "
            "strict but kind.) 6. சென்னை பெரிய நகரம். (Ceṉṉai periya "
            "nakaram. - Chennai is a big city.) 7. மதுரை பழமையான நகரம். "
            "(Maturai paḻamaiyāṉa nakaram. - Madurai is an ancient city.) "
            "8. கோவில் கோபுரம் மிக உயரமானது. (Kōvil kōpuram mika "
            "uyaramāṉatu. - The temple tower is very tall.) 9. கடற்கரை "
            "அழகானது, மணல் மென்மையானது. (Kaṭaṟkarai aḻakāṉatu, maṇal "
            "meṉmaiyāṉatu. - The beach is beautiful, the sand is soft.) "
            "10. என் வீடு சிறியது ஆனால் வசதியானது. (Eṉ vīṭu ciṟiyatu "
            "āṉāl vacatiyāṉatu. - My house is small but comfortable.) 11. "
            "தோட்டத்தில் வண்ணப் பூக்கள் உள்ளன. (Tōṭṭattil vaṇṇap pūkkaḷ "
            "uḷḷaṉa. - There are colorful flowers in the garden.) 12. "
            "அந்தப் புத்தகம் தடித்தது, சுவாரஸ்யமானது. (Antap puttakam "
            "taṭittatu, cuvārasyamāṉatu. - That book is thick and "
            "interesting.) 13. காபி சூடாகவும் இனிப்பாகவும் உள்ளது. (Kāpi "
            "cūṭākavum iṉippākavum uḷḷatu. - The coffee is hot and sweet.) "
            "14. இந்தச் சாலை நீண்டது, அகலமானது. (Intac cālai nīṇṭatu, "
            "akalamāṉatu. - This road is long and wide.) 15. மலை பசுமையாக "
            "மூடப்பட்டுள்ளது. (Malai pacumaiyāka mūṭappaṭṭuḷḷatu. - The "
            "mountain is covered in green.) 16. அறை வெளிச்சமாகவும் "
            "காற்றோட்டமாகவும் உள்ளது. (Aṟai veḷiccamākavum "
            "kāṟṟōṭṭamākavum uḷḷatu. - The room is bright and airy.) 17. "
            "அவன் குரல் இனிமையானது. (Avaṉ kural iṉimaiyāṉatu. - His voice "
            "is sweet.) 18. அவள் சிரிப்பு அழகானது. (Avaḷ cirippu "
            "aḻakāṉatu. - Her laugh is beautiful.) 19. இரவு வானம் "
            "நட்சத்திரங்களால் நிறைந்துள்ளது. (Iravu vāṉam "
            "naṭcattiraṅkaḷāl niṟaintuḷḷatu. - The night sky is full of "
            "stars.) 20. தமிழ்நாடு இயற்கை அழகு நிறைந்தது. (Tamiḻnāṭu "
            "iyaṟkai aḻaku niṟaintatu. - Tamil Nadu is full of natural "
            "beauty.)"
        ),
        "how_it_works": (
            "This record teaches description as layering: one adjective "
            "per sentence becomes two, then a contrast with ஆனால் "
            "(but), then a possession with உடையவர்/உள்ளது (having). The "
            "learner describes people first - height, hair, face, "
            "character - using -அவர்/-அவள் nominalized adjectives "
            "(உயரமானவர், அன்பானவர்), which Tamil prefers over bare "
            "adjectives for people. Places follow: cities, temple "
            "towers, beaches, houses - with paired adjectives joined by "
            "-உம் (சூடாகவும் இனிப்பாகவும்). Sensory description closes "
            "it: voice, laugh, night sky. The drill is portraiture: the "
            "learner describes three people and three places they know, "
            "each in three layered sentences."
        ),
        "key_points": [
            "20 descriptive sentences with transliteration and English.",
            "People take nominalized adjectives: உயரமானவர், அன்பானவர்.",
            "உடையவர்/உள்ளது expresses having: முடி உடையவள்.",
            "-உம் pairs qualities: சூடாகவும் இனிப்பாகவும்.",
            "ஆனால் contrasts: சிறியது ஆனால் வசதியானது.",
        ],
        "requirements": [
            "Describe three people you know in three sentences each.",
            "Describe three places in three layered sentences each.",
            "Convert five bare adjectives to -அவர்/-அவள் forms.",
            "Write paired-quality sentences with -உம்.",
            "Describe your hometown's beauty in a paragraph.",
        ],
        "standards": [
            "Nominalized adjectives follow Lehmann 1989.",
            "Descriptive constructions follow Schiffman 1999.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: description is the portrait the tongue "
            "paints - each adjective a brushstroke, each sentence a "
            "signed likeness. Where public lessons file modifiers, the "
            "Signature Word Method files portraits: அழகானது the seal "
            "that beauty was truly seen."
        ),
    },
    {
        "key": "story1",
        "name": "Tamil Story: A Simple Day",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence simple Tamil story in the present tense, "
            "with line-by-line English translation. Title: ஒரு எளிய நாள் "
            "(Oru eḷiya nāḷ - A Simple Day). 1. காலையில் சூரியன் "
            "உதிக்கிறது. (Kālaiyil cūriyaṉ utikkiṟatu. - In the morning "
            "the sun rises.) 2. ராஜா கண் விழிக்கிறான். (Rājā kaṇ "
            "viḻikkiṟāṉ. - Raja opens his eyes.) 3. அவன் பல் துலக்குகிறான். "
            "(Avaṉ pal tulakkukiṟāṉ. - He brushes his teeth.) 4. அம்மா "
            "இட்லி சுடுகிறார். (Ammā iṭli cuṭukiṟār. - Mother is steaming "
            "idlis.) 5. ராஜா சாப்பிட்டுப் பள்ளிக்குப் போகிறான். (Rājā "
            "cāppiṭṭup paḷḷikkup pōkiṟāṉ. - Raja eats and goes to school.) "
            "6. வகுப்பில் ஆசிரியர் பாடம் நடத்துகிறார். (Vakuppi "
            "āciriyar pāṭam naṭattukiṟār. - In class the teacher teaches "
            "the lesson.) 7. மதியம் நண்பர்களோடு விளையாடுகிறான். (Matiyam "
            "naṇparkaḷōṭu viḷaiyāṭukiṟāṉ. - At noon he plays with "
            "friends.) 8. மாலையில் வீடு திரும்புகிறான். (Mālaiyil vīṭu "
            "tirumpukiṟāṉ. - In the evening he returns home.) 9. இரவு "
            "அப்பாவோடு கதை பேசுகிறான். (Iravu appāvōṭu katai pēckiṟāṉ. - At night he chats with father.) 10. படுக்கையில் நன்றாகத் தூங்குகிறான். "
            "(Paṭukkaiyil naṉṟākat tūṅkukiṟāṉ. - In bed he sleeps well.) "
            "The story uses only present tense and the vocabulary of "
            "records 1-20, so the learner reads fluently. Time words "
            "open each sentence (காலையில், மதியம், மாலையில், இரவு), "
            "teaching narrative sequencing. The -ஓடு sociative appears "
            "twice (நண்பர்களோடு, அப்பாவோடு). The learner retells the "
            "story from memory, then rewrites it about their own day."
        ),
        "how_it_works": (
            "This record teaches reading through a story the learner "
            "can already understand - every word comes from earlier "
            "records, so the challenge is flow, not vocabulary. The ten "
            "sentences follow one character through one day, each "
            "opened by a time word, which teaches Tamil narrative "
            "rhythm: time first, then action. The learner reads the "
            "Tamil line, covers the translation, and says the English - "
            "then reverses. Two grammar points are planted for later "
            "harvest: the sociative -ஓடு in sentences 7 and 9, and the "
            "serial verb in sentence 5 (சாப்பிட்டுப் போகிறான் - eats "
            "and goes). The drill is retelling: first with the book "
            "open, then closed, then as one's own day."
        ),
        "key_points": [
            "10-sentence story, present tense only, line-by-line translation.",
            "Time words open sentences: காலையில், மதியம், மாலையில், இரவு.",
            "All vocabulary drawn from earlier records - fluent reading.",
            "Sociative -ஓடு appears naturally twice.",
            "Serial verb சாப்பிட்டுப் போகிறான் planted for later.",
        ],
        "requirements": [
            "Read the story aloud three times, then retell it closed-book.",
            "Cover the English and translate each line from Tamil.",
            "Rewrite the story about your own day keeping the time words.",
            "Find the two -ஓடு sentences and explain the suffix.",
            "Write a second ten-sentence day story with a new character.",
        ],
        "standards": [
            "Narrative forms follow standard written Tamil per Lehmann 1989.",
            "Vocabulary controlled to records 1-20 of this database.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: a day is the smallest complete "
            "instrument - dawn to sleep, a signed circle. Where public "
            "readers file graded texts, the Signature Word Method files "
            "a life: ஒரு எளிய நாள் the seal that the ordinary is worth "
            "telling truly."
        ),
    },
    {
        "key": "story2",
        "name": "Tamil Story: A Journey in the Past",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence Tamil story in the past tense, with "
            "line-by-line English translation. Title: கடந்த காலப் "
            "பயணம் (Kaṭanta kālap payaṇam - A Journey in the Past). 1. "
            "கடந்த வாரம் நாங்கள் மதுரைக்குப் போனோம். (Kaṭanta vāram "
            "nāṅkaḷ maturaikkup pōṉōm. - Last week we went to Madurai.) "
            "2. அதிகாலையில் ரயிலில் ஏறினோம். (Atikālaiyil rayilil "
            "ēṟiṉōm. - We boarded the train at dawn.) 3. ஜன்னல் வழியாகப் "
            "பசுமையான வயல்களைப் பார்த்தோம். (Jaṉṉal vaḻiyākap pacumaiyāṉa "
            "vayalkaḷaip pārttōm. - Through the window we saw green "
            "fields.) 4. மதுரையில் மீனாட்சி கோவிலைக் கண்டோம். "
            "(Maturaiyil mīnāṭci kōvilaik kaṇṭōm. - In Madurai we saw "
            "the Meenakshi temple.) 5. கோபுரம் வானத்தைத் தொட்டது. "
            "(Kōpuram vāṉattait toṭṭatu. - The tower touched the sky.) 6. "
            "கோவில் குளத்தில் மீன்கள் நீந்தின. (Kōvil kuḷattil mīṉkaḷ "
            "nīntina. - Fish swam in the temple tank.) 7. மதியம் "
            "சாப்பாட்டுக் கடையில் சாப்பிட்டோம். (Matiyam cāppāṭṭuk "
            "kaṭaiyil cāppiṭṭōm. - At noon we ate at a meals shop.) 8. "
            "மாலையில் பூங்காவில் நடந்தோம். (Mālaiyil pūṅkāvil naṭantōm. - In the evening we walked in the park.) 9. நண்பர்கள் புகைப்படம் எடுத்தார்கள். "
            "(Naṇparkaḷ pukaippaṭam eṭuttārkaḷ. - Friends took photos.) "
            "10. இரவு மகிழ்ச்சியோடு வீடு திரும்பினோம். (Iravu "
            "makiḻcciyōṭu vīṭu tirumpiṉōm. - At night we returned home "
            "happily.) The story exercises past-tense forms across "
            "person and number: போனோம் (we went), ஏறினோம், பார்த்தோம், "
            "கண்டோம், சாப்பிட்டோம், நடந்தோம், திரும்பினோம், plus "
            "third-person தொட்டது, நீந்தின, எடுத்தார்கள். "
            "Postpositions appear naturally: வழியாக (through), -ஓடு "
            "(with). The learner retells the journey, then narrates "
            "their own last trip."
        ),
        "how_it_works": (
            "This record teaches the past tense inside a journey worth "
            "remembering. The ten sentences move dawn to night like the "
            "first story, but every verb is past: the learner feels the "
            "-ன்-/-த்-/-த்த்- past markers working across seven different "
            "verbs. Third-person forms interrupt the we-narration "
            "(தொட்டது, நீந்தின, எடுத்தார்கள்), teaching agreement "
            "shifts. Postpositions வழியாக and -ஓடு extend the learner's "
            "connective tissue. Place names (மதுரை, மீனாட்சி கோவில்) "
            "root the story in real Tamil geography. The drill is "
            "memory: the learner narrates their own most recent trip in "
            "ten past-tense Tamil sentences, then answers questions "
            "about the story's details."
        ),
        "key_points": [
            "10-sentence past-tense story with line-by-line translation.",
            "Past markers across seven verbs: போனோம், பார்த்தோம், நடந்தோம்.",
            "Agreement shifts: we-forms vs தொட்டது vs எடுத்தார்கள்.",
            "Postpositions வழியாக and -ஓடு in natural use.",
            "Set in real Madurai - geography with grammar.",
        ],
        "requirements": [
            "Narrate your last trip in ten past-tense Tamil sentences.",
            "List every past-tense verb in the story with its root.",
            "Answer ten detail questions about the story in Tamil.",
            "Convert the story's we-forms to I-forms.",
            "Write a second journey story to a different city.",
        ],
        "standards": [
            "Past-tense formation follows Lehmann 1989.",
            "Place references use standard Tamil names.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: memory is the archive the heart keeps - "
            "every past-tense verb a record sealed and shelved. Where "
            "public readers file narratives, the Signature Word Method "
            "files witness: போனோம் the tongue swearing we went, truly."
        ),
    },
    {
        "key": "story3",
        "name": "Tamil Story: Dreams of Tomorrow",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence Tamil story in the future tense with "
            "conditional touches, line-by-line English translation. "
            "Title: நாளைய கனவுகள் (Nāḷaiya kaṉavukaḷ - Dreams of "
            "Tomorrow). 1. நாளை என் வாழ்வில் புதிய நாள் பிறக்கும். "
            "(Nāḷai eṉ vāḻvil putiya nāḷ piṟakkum. - Tomorrow a new day "
            "will dawn in my life.) 2. நான் அதிகாலையில் எழுவேன். (Nāṉ "
            "atikālaiyil eḻuvēṉ. - I will wake at dawn.) 3. தமிழ் நன்றாகப் "
            "பேசுவேன். (Tamiḻ naṉṟākap pēcuvēṉ. - I will speak Tamil well.) 4. நண்பர்களைச் "
            "சந்தித்து மகிழ்வேன். (Naṇparkaḷaic cantittu makiḻvēṉ. - I "
            "will meet friends and rejoice.) 5. கடினமாக உழைத்தால் வெற்றி "
            "கிடைக்கும். (Kaṭiṉamāka uḻaittāl veṟṟi kiṭaikkum. - If one "
            "works hard, success will come.) 6. நல்லது செய்தால் நல்லது "
            "நடக்கும். (Nallatu ceytāl nallatu naṭakkum. - If you do "
            "good, good will happen.) 7. நான் புதிய ஊர்களுக்குப் "
            "பயணிப்பேன். (Nāṉ putiya ūrkaḷukkup payaṇippēṉ. - I will "
            "travel to new towns.) 8. உலகைப் பார்த்துக் கற்றுக்கொள்வேன். "
            "(Ulakaip pārttuk kaṟṟukkoḷvēṉ. - I will see the world and learn.) 9. என் "
            "குடும்பத்தை மகிழ்விப்பேன். (Eṉ kuṭumpattai makiḻvippēṉ. - I "
            "will make my family happy.) 10. கனவுகள் நனவாகும் என்று "
            "நம்புகிறேன். (Kaṉavukaḷ naṉavākum eṉṟu nampukiṟēṉ. - I "
            "believe dreams will come true.) Future markers -வ்-/-ப்- "
            "run through the story (எழுவேன், பேசுவேன், மகிழ்வேன், "
            "பயணிப்பேன்), with the conditional -ஆல் in sentences 5-6 "
            "(உழைத்தால், செய்தால்) and the quotative என்று in sentence "
            "10. The learner writes their own ten-sentence future."
        ),
        "how_it_works": (
            "This record teaches the future as intention and the "
            "conditional as wisdom. The future -வ்- marker is drilled "
            "across six verbs, then the conditional -ஆல் arrives inside "
            "two proverb-like truths (உழைத்தால் வெற்றி கிடைக்கும்), "
            "which is how Tamil actually teaches conditionals - inside "
            "sayings. The quotative என்று in the final sentence "
            "(நனவாகும் என்று நம்புகிறேன்) introduces reported thought, "
            "the bridge to complex sentences. The story's arc - dawn, "
            "effort, travel, family, belief - gives the learner an "
            "emotional template. The drill is vision: the learner "
            "writes their own ten-sentence future, including two "
            "-ஆல் conditionals and one என்று belief."
        ),
        "key_points": [
            "10-sentence future-tense story with line-by-line translation.",
            "Future -வ்- across six verbs: எழுவேன், பேசுவேன், மகிழ்வேன்.",
            "Conditional -ஆல் taught inside proverb-like truths.",
            "Quotative என்று introduces reported thought.",
            "Learner writes their own ten-sentence future.",
        ],
        "requirements": [
            "Write your own ten-sentence future in Tamil.",
            "Include two -ஆல் conditionals and one என்று belief.",
            "Convert the story to past tense as if it already happened.",
            "Explain the conditional formation in your own words.",
            "Memorize sentences 5-6 as sayings and use them.",
        ],
        "standards": [
            "Future and conditional formation follow Lehmann 1989.",
            "Quotative constructions follow Schiffman 1999.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN],
        "sig_lens": (
            "The Signature read: the future is the unsigned page - "
            "every -வேன் a signature promised in advance. Where public "
            "readers file tenses, the Signature Word Method files vows: "
            "செய்வேன் the tongue signing what it has not yet done."
        ),
    },
    {
        "key": "idioms",
        "name": "Tamil Idioms and Proverbs",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty Tamil idioms and proverbs, each with literal "
            "translation, real meaning, and an example sentence. 1. "
            "கற்றது கைமண் அளவு, கல்லாதது உலகளவு. (Kaṟṟatu kaimaṇ aḷavu, "
            "kallātatu ulakaḷavu. - Lit: What is learned is a handful of "
            "sand, what is unlearned is the world. Meaning: knowledge is "
            "endless; stay humble.) Ex: பட்டம் பெற்றாலும் கற்க "
            "வேண்டும். (Even with a degree, one must keep learning.) 2. "
            "முயற்சி திருவினையாக்கும். (Muyaṟci tiruviṉaiyākkum. - Lit: "
            "Effort makes fortune. Meaning: hard work brings success.) "
            "Ex: தினமும் பயிற்சி செய், முயற்சி திருவினையாக்கும். 3. சிறு "
            "துளி பெரு வெள்ளம். (Ciṟu tuḷi peru veḷḷam. - Lit: Small drops "
            "make a great flood. Meaning: small efforts accumulate.) Ex: "
            "சிறு சேமிப்பு பெரும் செல்வம். 4. ஆத்திரக்காரனுக்கு புத்தி "
            "மட்டு. (Āttirakkāraṉukku putti maṭṭu. - Lit: The angry man "
            "has limited sense. Meaning: anger clouds judgment.) Ex: "
            "கோபத்தில் முடிவு எடுக்காதே. 5. காக்கைக்குத் தன் குஞ்சு பொன் "
            "குஞ்சு. (Kākaikkut taṉ kuñcu poṉ kuñcu. - Lit: To the crow "
            "its chick is golden. Meaning: every parent cherishes their "
            "child.) 6. ஆழம் தெரியாமல் காலை விடாதே. (Āḻam teriyāmal "
            "kālai viṭātē. - Lit: Do not step in without knowing the "
            "depth. Meaning: investigate before acting.) 7. எலி "
            "வளையானாலும் தனி வளை வேண்டும். (Eli vaḷaiyāṉālum taṉi vaḷai "
            "vēṇṭum. - Lit: Even a rat-hole should be one's own. "
            "Meaning: independence matters more than luxury.) 8. வினை "
            "விதைத்தவன் வினை அறுப்பான். (Viṉai vitaittavaṉ viṉai "
            "aṟuppāṉ. - Lit: Who sows deeds reaps deeds. Meaning: you "
            "reap what you sow.) 9. அகத்தின் அழகு முகத்தில் தெரியும். "
            "(Akattiṉ aḻaku mukattil teriyum. - Lit: The beauty within "
            "shows on the face. Meaning: character shows.) 10. செய்வன "
            "திருந்தச் செய். (Ceyvaṉa tiruntac cey. - Lit: Whatever you "
            "do, do it well. Meaning: take pride in work - from "
            "Auvaiyar.) 11. யாதும் ஊரே யாவரும் கேளிர். (Yātum ūrē "
            "yāvarum kēḷir. - Lit: Every town is my town, all are my "
            "kin. Meaning: universal kinship - Kaniyan Pungundranar, "
            "Purananuru.) 12. பிறப்பொக்கும் எல்லா உயிர்க்கும். "
            "(Piṟappokkum ellā uyirkkum. - Lit: All beings are equal by "
            "birth. Meaning: equality - Thirukkural 972.) 13. கற்க கசடற "
            "கற்பவை. (Kaṟka kacaṭaṟa kaṟpavai. - Lit: Learn flawlessly "
            "what is to be learned. Meaning: study with precision - "
            "Thirukkural 391.) 14. இனிய உளவாக இன்னாத கூறல். (Iṉiya "
            "uḷavāka iṉṉāta kūṟal. - Lit: Speaking harsh words when sweet "
            "ones exist. Meaning: choose kind speech - Thirukkural 100.) "
            "15. அறிவுடையார் எல்லாம் உடையார். (Aṟivuṭaiyār ellām "
            "uṭaiyār. - Lit: The wise possess everything. Meaning: "
            "wisdom is true wealth - Thirukkural 430.) 16. தீதும் நன்றும் "
            "பிறர் தர வாரா. (Tītum naṉṟum piṟar tara vārā. - Lit: Good "
            "and bad do not come from others. Meaning: take "
            "responsibility - Purananuru.) 17. ஆனைக்கும் அடி சறுக்கும். "
            "(Āṉaikkum aṭi caṟukkum. - Lit: Even the elephant's foot "
            "slips. Meaning: anyone can err.) 18. மலை போல் வரும் துன்பம் "
            "பனி போல் நீங்கும். (Malai pōl varum tuṉpam paṉi pōl "
            "nīṅkum. - Lit: Trouble coming like a mountain leaves like "
            "mist. Meaning: troubles pass.) 19. தேனொழுகப் பேசிக் "
            "கொல்லுவார். (Tēṉoḻukap pēcik kolluvār. - Lit: They speak "
            "dripping honey and kill. Meaning: beware flatterers.) 20. "
            "நூல் போலச் சேலை, தாய் போலப் பிள்ளை. (Nūl pōlac cēlai, tāy "
            "pōlap piḷḷai. - Lit: As the thread, so the cloth; as the "
            "mother, so the child. Meaning: character is inherited.)"
        ),
        "how_it_works": (
            "This record teaches proverbs as compressed philosophy - "
            "each one a whole lesson in a single line. The learner "
            "first reads the literal translation to feel the image "
            "(small drops, golden chicks, rat-holes), then the real "
            "meaning to get the wisdom, then an example sentence showing "
            "it in use. Four come from the Thirukkural and two from "
            "Purananuru, connecting the learner to classical Tamil "
            "directly; the rest are folk sayings every Tamil speaker "
            "knows. The drill is application: the learner matches ten "
            "life situations to the right proverb, then uses three "
            "proverbs in real conversation during the week."
        ),
        "key_points": [
            "20 idioms/proverbs: literal translation + meaning + example.",
            "Four from the Thirukkural (391, 100, 430, 972), two from Purananuru.",
            "Images carry the wisdom: drops, floods, golden chicks.",
            "யாதும் ஊரே யாவரும் கேளிர் teaches universal kinship.",
            "Proverbs are used in real speech, not just studied.",
        ],
        "requirements": [
            "Memorize ten proverbs with their meanings.",
            "Match ten situations to the right proverb.",
            "Use three proverbs in conversation this week.",
            "Explain two Thirukkural couplets in your own words.",
            "Write an example sentence for five folk proverbs.",
        ],
        "standards": [
            "Thirukkural citations follow the standard 1330-couplet numbering.",
            "Purananuru attributions follow the classical anthology.",
        ],
        "citations": [CIT_THIRUKKURAL, CIT_TOLKAPPIYAM],
        "sig_lens": (
            "The Signature read: the proverb is the sealed verdict of "
            "generations - a whole court of ancestors signing one line. "
            "Where public lists file sayings, the Signature Word Method "
            "files inheritance: கற்க கசடற the seal of the learned, kept "
            "two thousand years."
        ),
    },
    {
        "key": "registers",
        "name": "Tamil Formal and Polite Registers",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen formal versus informal Tamil pairs for letters, "
            "business, and elders, with translations. 1. Informal: நீ வா. "
            "/ Formal: நீங்கள் வாருங்கள். (You come. / Please come.) 2. "
            "Informal: உன் பெயர் என்ன? / Formal: உங்கள் பெயர் என்ன? "
            "(What is your name?) 3. Informal: சாப்பிட்டியா? / Formal: "
            "சாப்பிட்டீர்களா? (Have you eaten?) 4. Informal: எங்கே "
            "போறே? / Formal: எங்கே போகிறீர்கள்? (Where are you going? - "
            "spoken போறே vs written போகிறீர்கள்.) 5. Informal: இதைக் "
            "கொடு. / Formal: இதைக் கொடுங்கள். (Give this.) 6. Informal: "
            "நீ சொல்றது சரி. / Formal: நீங்கள் சொல்வது சரி. (What you say "
            "is right.) 7. Informal letter open: அன்புள்ள ராஜா, / Formal "
            "letter open: மதிப்பிற்குரிய ஐயா, (Dear Raja, / Respected "
            "sir,) 8. Informal close: உன் நண்பன், / Formal close: "
            "தங்கள் உண்மையுள்ள, (Your friend, / Yours faithfully,) 9. "
            "Informal: பணம் கொடு. / Formal business: பணம் செலுத்துமாறு "
            "கேட்டுக்கொள்கிறேன். (Give the money. / I request you to "
            "remit the payment.) 10. Informal: நாளைக்கு வா. / Formal: "
            "நாளை வருமாறு அன்புடன் அழைக்கிறேன். (Come tomorrow. / I "
            "cordially invite you to come tomorrow.) 11. Informal: "
            "அவன் வந்தான். / Formal: அவர் வந்தார். (He came. / He came - "
            "respectful.) 12. Informal: சரி, போலாம். / Formal: சரி, "
            "போகலாம். (Okay, let us go - spoken vs written.) 13. "
            "Informal: என்ன வேணும்? / Formal: உங்களுக்கு என்ன வேண்டும்? "
            "(What do you want?) 14. Informal: இரு. / Formal elder: "
            "இருங்கள். (Wait/stay.) 15. Informal thanks: நன்றி டா. / "
            "Formal thanks: மிக்க நன்றி. (Thanks, buddy. / Thank you very "
            "much.) The formal register uses நீங்கள், -ஈர்கள்/-ஆர்கள் "
            "verb endings, and full written forms; the informal uses நீ, "
            "short endings, and spoken contractions like போறே for "
            "போகிறேன்."
        ),
        "how_it_works": (
            "This record teaches register as a social instrument with "
            "three strings: pronoun (நீ vs நீங்கள்), verb ending "
            "(-ஆய் vs -ஈர்கள், -அன் vs -ஆர்), and fullness (spoken "
            "போறே vs written போகிறேன்). Each pair shows the same "
            "meaning in both registers so the learner feels exactly "
            "what changes. Business Tamil gets its own frames: "
            "செலுத்துமாறு கேட்டுக்கொள்கிறேன் (I request remittance) and "
            "அன்புடன் அழைக்கிறேன் (I cordially invite) - the fixed "
            "formulas of formal letters. Letter openings and closings "
            "are taught as templates. The drill is code-switching: the "
            "learner takes five informal sentences and rewrites them "
            "for a business letter, then takes five formal ones and "
            "makes them friendly."
        ),
        "key_points": [
            "15 formal/informal pairs with translations.",
            "Three register strings: pronoun, verb ending, fullness.",
            "Business frames: கேட்டுக்கொள்கிறேன், அன்புடன் அழைக்கிறேன்.",
            "Letter templates: மதிப்பிற்குரிய ஐயா to தங்கள் உண்மையுள்ள.",
            "அவர்/வந்தார் honors the third person too.",
        ],
        "requirements": [
            "Rewrite five informal sentences in formal register.",
            "Rewrite five formal sentences as friendly informal.",
            "Write a formal invitation letter in Tamil.",
            "Write an informal note to a friend in Tamil.",
            "Address an elder correctly in a three-sentence speech.",
        ],
        "standards": [
            "Register distinctions follow Schiffman 1999 diglossia analysis.",
            "Business formulas follow standard Tamil official usage.",
        ],
        "citations": [CIT_SCHIFFMAN, CIT_LEHMANN],
        "sig_lens": (
            "The Signature read: register is the seal of honor - நீங்கள் "
            "the bow, நீ the embrace. Where public grammar files "
            "levels, the Signature Word Method files reverence: every "
            "formal ending a signed acknowledgment of the other's worth."
        ),
    },
    {
        "key": "complex_sentences",
        "name": "Tamil Compound and Complex Sentences",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen long Tamil sentences with clauses, connectors, and "
            "relative clauses - parsed and translated. 1. நான் பள்ளிக்குப் "
            "போனேன், ஏனென்றால் தேர்வு இருந்தது. (I went to school "
            "because there was an exam - ஏனென்றால் = because.) 2. மழை "
            "பெய்தாலும் நாங்கள் விளையாடினோம். (Even though it rained, we "
            "played - -ஆலும் = even though.) 3. அவன் வந்த பிறகு நாங்கள் "
            "சாப்பிட்டோம். (After he came, we ate - பிறகு = after.) 4. "
            "நான் சொன்னதை அவன் கேட்கவில்லை. (He did not listen to what I "
            "said - சொன்னதை = what was said, relative participle + -அதை.) "
            "5. படித்த பையன் வெற்றி பெற்றான். (The boy who studied "
            "succeeded - படித்த = who studied, relative participle.) 6. "
            "நான் வாங்கிய புத்தகம் நல்லது. (The book I bought is good - "
            "வாங்கிய = which I bought.) 7. அவள் பாடும்போது நான் "
            "கேட்டேன். (While she sang, I listened - -உம்போது = while.) "
            "8. வீட்டுக்குப் போவதற்கு முன் கடைக்குப் போனேன். (Before "
            "going home, I went to the shop - -வதற்கு முன் = before.) 9. "
            "அவன் வரும்வரை நான் காத்திருந்தேன். (Until he came, I waited "
            "- -உம்வரை = until.) 10. பணம் இருந்தால் பயணிப்பேன். (If I "
            "have money, I will travel - -ஆல் = if.) 11. நீ வந்தாலும் "
            "வராவிட்டாலும் நான் போவேன். (Whether you come or not, I will "
            "go - -ஆலும்...-ஆவிட்டாலும் = whether...or.) 12. அவர் சொன்னார், "
            "நாளை வருவேன் என்று. (He said that he will come tomorrow - "
            "என்று = that, quotative.) 13. எனக்குத் தெரியும், அவள் "
            "நல்லவள் என்று. (I know that she is good.) 14. மழை பெய்ததால் "
            "போட்டி நிறுத்தப்பட்டது. (Because it rained, the match was "
            "stopped - -அதால் = because.) 15. நான் சமைத்த உணவை எல்லோரும் "
            "பாராட்டினார்கள். (Everyone praised the food I cooked - "
            "சமைத்த = which I cooked.) Connectors: ஏனென்றால் (because), "
            "ஆனால் (but), மற்றும் (and), அதனால் (therefore), -ஆல் (if), "
            "-ஆலும் (even though), -உம்போது (while), -உம்வரை (until), "
            "என்று (that/saying)."
        ),
        "how_it_works": (
            "This record teaches the two great Tamil clause machines. "
            "Machine one is the relative participle: the verb sheds its "
            "tense-person ending and becomes an adjective - படித்த "
            "(who studied), வாங்கிய (which I bought), சமைத்த (which I "
            "cooked) - placed before the noun, no 'who/which' word "
            "needed. Machine two is the verbal participle and "
            "conditional suffixes: -ஆல் (if), -ஆலும் (even though), "
            "-உம்போது (while), -உம்வரை (until), -அதால் (because), "
            "என்று (that). Each sentence is parsed into clauses with "
            "the connector named and glossed, so the learner sees the "
            "joints. The drill is combining: the learner takes pairs of "
            "simple sentences from earlier records and joins them with "
            "each connector, then breaks complex sentences back apart."
        ),
        "key_points": [
            "15 complex sentences, parsed with connectors named.",
            "Relative participles replace who/which: படித்த பையன்.",
            "Conditional suffixes: -ஆல், -ஆலும், -உம்போது, -உம்வரை, -அதால்.",
            "என்று reports speech and thought: வருவேன் என்று.",
            "Combining and breaking drills build clause control.",
        ],
        "requirements": [
            "Join ten simple-sentence pairs with different connectors.",
            "Break five complex sentences into their clauses.",
            "Write five relative-participle descriptions of people you know.",
            "Report three things people said using என்று.",
            "Write a paragraph using at least four connectors.",
        ],
        "standards": [
            "Relative participles follow the Tolkappiyam col analysis.",
            "Clause structure follows Lehmann 1989 and Annamalai/Steever 1998.",
        ],
        "citations": [CIT_TOLKAPPIYAM, CIT_LEHMANN, CIT_ANNAMALAI],
        "sig_lens": (
            "The Signature read: the complex sentence is the covenant "
            "in full - clauses the witnesses, connectors the seals "
            "binding them. Where public syntax files trees, the "
            "Signature Word Method files the oath entire: every என்று "
            "a signed record of what was said."
        ),
    },
    {
        "key": "conv_market",
        "name": "Tamil Conversation: At the Market",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual Tamil dialogue at the market, "
            "annotated. Speakers: வாடிக்கையாளர் (customer, C) and "
            "வியாபாரி (shopkeeper, S). 1. C: வணக்கம்! (Hello!) 2. S: "
            "வணக்கம்! என்ன வேண்டும்? (Hello! What do you need?) 3. C: "
            "தக்காளி உள்ளதா? (Do you have tomatoes?) 4. S: உள்ளது, புதியது. "
            "எவ்வளவு வேண்டும்? (Yes, fresh. How much do you want?) 5. C: "
            "ஒரு கிலோ எவ்வளவு? (How much for one kilo?) 6. S: ஒரு கிலோ "
            "அறுபது ரூபாய். (Sixty rupees a kilo.) 7. C: அதிகம்! ஐம்பது "
            "ரூபாய்க்குக் கொடுங்கள். (Too much! Give it for fifty.) 8. S: "
            "முடியாது, ஐம்பத்தைந்து கடைசி. (Cannot; fifty-five is final.) "
            "9. C: சரி, ஒரு கிலோ கொடுங்கள். (Okay, give one kilo.) 10. "
            "S: வேறு என்ன வேண்டும்? (What else do you need?) 11. C: "
            "வெங்காயம் இரண்டு கிலோ. (Two kilos of onions.) 12. S: "
            "வெங்காயம் நாற்பது ரூபாய் கிலோ. (Onions are forty rupees a "
            "kilo.) 13. C: புதியதா? (Are they fresh?) 14. S: இன்று காலை "
            "வந்தது. (Arrived this morning.) 15. C: சரி, இரண்டு கிலோ "
            "போடுங்கள். (Okay, pack two kilos.) 16. S: மொத்தம் நூற்று "
            "முப்பத்தைந்து ரூபாய். (Total one hundred thirty-five "
            "rupees.) 17. C: இந்தாருங்கள், நூற்று ஐம்பது. (Here, one "
            "fifty.) 18. S: மீதி பதினைந்து ரூபாய். (Fifteen rupees "
            "change.) 19. C: நன்றி! நாளை வருவேன். (Thanks! I will come "
            "tomorrow.) 20. S: மீண்டும் வாருங்கள், வணக்கம்! (Come again, "
            "goodbye!) Annotations: lines 3-4 show உள்ளதா (is there?) as "
            "the stock question; lines 7-8 show polite bargaining "
            "கொடுங்கள் vs firm முடியாது; line 13 shows the freshness "
            "check புதியதா; lines 16-18 show the payment exchange with "
            "மொத்தம் (total) and மீதி (change); the dialogue opens and "
            "closes with வணக்கம்."
        ),
        "how_it_works": (
            "This record teaches the market as a complete transaction "
            "script. The learner plays both parts, feeling the rhythm: "
            "greeting, need, stock check, price ask, bargain, agreement, "
            "second item, freshness check, packing, total, payment, "
            "change, thanks, farewell. Each line is glossed so the "
            "learner knows why it is said, not just what it means - "
            "line 7's கொடுங்கள் is the polite push, line 8's முடியாது "
            "the polite wall. Numbers appear as real prices (அறுபது, "
            "ஐம்பத்தைந்து, நூற்று முப்பத்தைந்து), drilling the "
            "compounding rule under pressure. The drill is performance: "
            "pairs act the dialogue, then improvise it with new items "
            "and prices, then run it with a real shopkeeper's patience."
        ),
        "key_points": [
            "20-line market dialogue, Tamil + English, annotated.",
            "Transaction arc: greet, stock, price, bargain, pay, farewell.",
            "உள்ளதா asks stock; புதியதா checks freshness.",
            "Real prices drill number compounding: 55, 135, 150.",
            "மொத்தம் (total) and மீதி (change) close the sale.",
        ],
        "requirements": [
            "Perform the dialogue with a partner, both roles.",
            "Improvise the same dialogue with three new items.",
            "Bargain down two prices using கொடுங்கள் politely.",
            "Compute three totals in Tamil from item prices.",
            "Run the dialogue from memory without the book.",
        ],
        "standards": [
            "Market language follows standard Tamil commercial usage.",
            "Prices use standard Tamil number compounding.",
        ],
        "citations": [CIT_SCHIFFMAN, CIT_LEHMANN],
        "sig_lens": (
            "The Signature read: the market is the daily court of value "
            "- every price proposed, every bargain a signed negotiation. "
            "Where public dialogues file scripts, the Signature Word "
            "Method files the exchange itself: மொத்தம் the final seal, "
            "மீதி the honest remainder."
        ),
    },
    {
        "key": "conv_friend",
        "name": "Tamil Conversation: Meeting a Friend",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual Tamil dialogue meeting a friend, "
            "annotated. Speakers: ராஜா (R) and மீனா (M). 1. R: மீனா! நீண்ட "
            "நாட்களாகப் பார்க்கவில்லை! (Meena! Long time no see!) 2. M: "
            "ராஜா! எப்படி இருக்கே? (Raja! How are you? - informal "
            "between friends.) 3. R: நல்லா இருக்கேன். நீ? (I am good. "
            "You?) 4. M: நானும் நல்லா இருக்கேன். வேலை எப்படி? (I am good "
            "too. How is work?) 5. R: வேலை நல்லா போகுது. உன் படிப்பு? "
            "(Work is going well. Your studies?) 6. M: படிப்பு முடியப் "
            "போகுது. தேர்வு அடுத்த மாதம். (Studies are nearly done. Exam "
            "next month.) 7. R: வாழ்த்துக்கள்! நல்லா எழுது. "
            "(Congratulations! Write well.) 8. M: நன்றி! சனிக்கிழமை "
            "ஃப்ரீயா? (Thanks! Are you free Saturday?) 9. R: ஃப்ரீ தான். "
            "என்ன திட்டம்? (Free. What is the plan?) 10. M: சினிமாவுக்குப் "
            "போகலாமா? (Shall we go to a movie?) 11. R: போகலாம்! எந்தப் "
            "படம்? (Let us go! Which movie?) 12. M: புதிய படம் வந்துள்ளது. "
            "நல்லா இருக்காம். (A new movie came. They say it is good.) "
            "13. R: சரி, எத்தனை மணிக்கு? (Okay, at what time?) 14. M: "
            "மாலை ஆறு மணி காட்சி. (The six o'clock evening show.) 15. R: "
            "டிக்கெட் நான் வாங்குகிறேன். (I will buy the tickets.) 16. M: "
            "இல்லை இல்லை, பகிர்ந்து கொள்வோம். (No no, we will share.) "
            "17. R: சரி சரி. எங்கே சந்திப்போம்? (Okay okay. Where shall "
            "we meet?) 18. M: தியேட்டர் வாசலில் ஐந்தரைக்கு. (At the "
            "theater entrance at five-thirty.) 19. R: சரி, சனிக்கிழமை "
            "பார்ப்போம்! (Okay, see you Saturday!) 20. M: பார்ப்போம்! "
            "போய் வா! (See you! Go well - friend's farewell.) "
            "Annotations: lines 2-3 show informal -ஏ endings between "
            "friends (இருக்கே vs formal இருக்கிறீர்கள்); line 8 shows "
            "planning with ஃப்ரீயா; lines 10-11 show -லாம் suggestions; "
            "line 12 shows hearsay -ஆம்; lines 15-16 show Tamil "
            "gift-politeness (refusing to let the friend pay all); line "
            "20 shows போய் வா, the friend's warm farewell."
        ),
        "how_it_works": (
            "This record teaches friendship register - the informal "
            "Tamil friends actually speak, with spoken contractions "
            "(இருக்கே, போகுது, ஃப்ரீயா) alongside their written forms. "
            "The learner hears how friends plan: the -லாம் suggestion, "
            "the time-place pinning (ஐந்தரைக்கு, வாசலில்), the "
            "ticket-politeness dance. Hearsay -ஆம் (நல்லா இருக்காம்) "
            "arrives naturally. The dialogue models the full social "
            "arc: reunion joy, life updates, congratulations, planning, "
            "negotiating cost, fixing time and place, warm farewell. "
            "The drill is real planning: the learner uses the dialogue's "
            "frames to make actual plans with a real friend in Tamil."
        ),
        "key_points": [
            "20-line friend dialogue with informal spoken forms glossed.",
            "Friend register: இருக்கே, போகுது vs formal இருக்கிறீர்கள்.",
            "Planning frames: -லாம், time + -க்கு, place + -இல்.",
            "Hearsay -ஆம்: நல்லா இருக்காம்.",
            "போய் வா is the friend's farewell.",
        ],
        "requirements": [
            "Perform the dialogue with a friend, both roles.",
            "Make real weekend plans with someone using these frames.",
            "Convert five lines to formal register.",
            "Explain three spoken contractions and their written forms.",
            "Write a reunion dialogue with your own old friend.",
        ],
        "standards": [
            "Spoken forms follow Schiffman 1999 spoken Tamil.",
            "Register contrasts follow Annamalai/Steever 1998.",
        ],
        "citations": [CIT_SCHIFFMAN, CIT_ANNAMALAI],
        "sig_lens": (
            "The Signature read: friendship speaks the unsealed tongue - "
            "இருக்கே the signature of trust, needing no formal wax. "
            "Where public dialogues file scripts, the Signature Word "
            "Method files the bond: போய் வா the warmest seal, sending "
            "the friend off well."
        ),
    },
    {
        "key": "conv_problem",
        "name": "Tamil Conversation: Solving a Problem",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual Tamil dialogue solving a problem, "
            "annotated. Speakers: மாணவர் (student, St) and ஆசிரியர் "
            "(teacher, T). Problem: a lost bag. 1. St: ஐயா, வணக்கம். "
            "(Sir, hello - respectful address.) 2. T: வணக்கம். என்ன "
            "ஆயிற்று? (Hello. What happened?) 3. St: என் பை "
            "காணவில்லை. (My bag is missing.) 4. T: எங்கே வைத்தாய்? "
            "(Where did you keep it?) 5. St: வகுப்பறையில் வைத்தேன் என்று "
            "நினைக்கிறேன். (I think I kept it in the classroom.) 6. T: "
            "எப்போது கடைசியாகப் பார்த்தாய்? (When did you last see it?) "
            "7. St: மதிய உணவுக்கு முன் பார்த்தேன். (I saw it before "
            "lunch.) 8. T: கவலைப்படாதே. சேர்ந்து தேடுவோம். (Do not "
            "worry. We will search together.) 9. St: நன்றி ஐயா. (Thank "
            "you, sir.) 10. T: வா, வகுப்பறைக்குப் போவோம். (Come, let us "
            "go to the classroom.) 11. St: இதோ, மேசைக்கு அடியில் "
            "உள்ளது! (Here, it is under the desk!) 12. T: நல்லது! "
            "எல்லாம் உள்ளதா என்று பார். (Good! Check if everything is "
            "there.) 13. St: புத்தகங்கள் உள்ளன, பேனா இல்லை. (Books are "
            "there, the pen is missing.) 14. T: நண்பர்களிடம் கேட்டுப் "
            "பார். (Ask your friends.) 15. St: சரி ஐயா, கேட்கிறேன். "
            "(Okay sir, I will ask.) 16. T: அடுத்த முறை பையை மறக்காதே. "
            "(Next time do not forget the bag.) 17. St: மறக்கமாட்டேன் "
            "ஐயா. (I will not forget, sir.) 18. T: சரி, வகுப்புக்குப் "
            "போ. (Okay, go to class.) 19. St: மிக்க நன்றி ஐயா! (Thank "
            "you very much, sir!) 20. T: பரவாயில்லை. போய் வா. (No "
            "problem. Go well.) Annotations: lines 1-2 show the problem "
            "report frame (என்ன ஆயிற்று); lines 4-7 show information "
            "gathering with past tense; line 8 shows comfort + joint "
            "action (சேர்ந்து தேடுவோம்); lines 11-13 show discovery and "
            "inventory; lines 14-17 show advice with prohibition "
            "(மறக்காதே) and promise (மறக்கமாட்டேன்); the student uses "
            "respectful ஐயா throughout while the teacher uses informal "
            "-ஆய் with the student."
        ),
        "how_it_works": (
            "This record teaches problem-solving as a five-act "
            "conversation: report (என் பை காணவில்லை), investigate "
            "(எங்கே, எப்போது), comfort and team up (கவலைப்படாதே, "
            "சேர்ந்து தேடுவோம்), discover and verify (இதோ, பார்), advise "
            "and close (மறக்காதே, பரவாயில்லை). The register asymmetry is "
            "the lesson's heart: the student says ஐயா and formal forms "
            "upward, the teacher says -ஆய் forms downward - Tamil "
            "hierarchy made audible. Past tense carries the "
            "investigation (வைத்தாய், பார்த்தேன்); future promise closes "
            "it (மறக்கமாட்டேன்). The drill is crisis role-play: pairs "
            "invent a lost item, a missed bus, a wrong turn, and solve "
            "it in Tamil through all five acts."
        ),
        "key_points": [
            "20-line problem-solving dialogue, annotated act by act.",
            "Five acts: report, investigate, comfort, discover, advise.",
            "Register asymmetry: ஐயா upward, -ஆய் downward.",
            "Past tense investigates; future promise closes.",
            "மறக்காதே (do not forget) vs மறக்கமாட்டேன் (I will not forget).",
        ],
        "requirements": [
            "Role-play solving a lost-item problem in Tamil.",
            "Invent two new problems and solve each in five acts.",
            "Practice the upward/downward register asymmetry.",
            "Report a real problem to someone using என்ன ஆயிற்று frame.",
            "Write advice with -ஆதே and promises with -மாட்டேன்.",
        ],
        "standards": [
            "Register asymmetry follows Schiffman 1999.",
            "Narrative past forms follow Lehmann 1989.",
        ],
        "citations": [CIT_SCHIFFMAN, CIT_LEHMANN],
        "sig_lens": (
            "The Signature read: trouble is the unsealed test - "
            "கவலைப்படாதே the seal of comfort, சேர்ந்து தேடுவோம் the "
            "covenant of help. Where public dialogues file scripts, the "
            "Signature Word Method files rescue: every solved problem a "
            "signed testimony that no one is left alone."
        ),
    },
    {
        "key": "mastery",
        "name": "Tamil Mastery Review and Full Reference",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The whole Tamil Language Database in one teaching summary: "
            "alphabet, 200 core words, key grammar, and all phrase "
            "tables. THE SCRIPT: 12 vowels அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ; 18 "
            "consonants க் ங் ச் ஞ் ட் ண் த் ந் ப் ம் ய் ர் ல் வ் ழ் ள் "
            "ற் ன்; āytam ஃ; 216 uyirmey; total 247; pulli ்; numerals "
            "௦-௯, ௰=10, ௱=100, ௲=1000. 200 CORE WORDS (sampled across the "
            "database): nouns - மனிதன், பெண், குழந்தை, வீடு, பள்ளி, "
            "புத்தகம், தண்ணீர், மரம், நாய், சூரியன், நிலா, கடல், மலை, "
            "நகரம், சாலை, நண்பர், அப்பா, அம்மா, கடை, உணவு; verbs - "
            "சாப்பிடு, குடி, போ, வா, இரு, செய், பார், கேள், பேசு, படி, "
            "எழுது, ஓடு, நட, கொடு, எடு, வாங்கு, கற்றுக்கொள், சமை, "
            "விளையாடு, தூங்கு; adjectives - பெரிய, சிறிய, நல்ல, புதிய, "
            "அழகான, வேகமான, சூடான, இனிப்பான, உயரமான, முக்கியமான; and "
            "the full sets from records 4-6, 8-9. KEY GRAMMAR: SOV order; "
            "agglutinative suffix stacking; rational vs irrational noun "
            "classes; cases -ஐ -க்கு -ஆல் -ஓடு -இல் -இலிருந்து -இன்; plural "
            "-கள்; tenses -கிற்- -த்- -வ்-; person endings -ஏன் -ஆன் -ஆள் "
            "-அது -ஓம் -ஈர்கள் -ஆர்கள்; negation இல்லை/-ஆ-/-மாட்ட்-; "
            "questions -ஆ and எ- words; relative participles; "
            "connectors ஏனென்றால் ஆனால் -ஆல் என்று. PHRASE TABLES: "
            "greetings (வணக்கம், நன்றி, போய் வருகிறேன்), travel (எங்கே, "
            "எவ்வளவு, நேராக), market (உள்ளதா, கொஞ்சம் குறையுங்கள், "
            "மொத்தம்), health (எனக்கு வலிக்கிறது, மருந்து), emotions "
            "(மகிழ்ச்சியாக உள்ளேன்), time (மணி, இன்று, நாளை). THE "
            "LADDER PATH: records 1-10 foundations (script, sounds, "
            "words, grammar), 11-24 compounded (themed sentences, "
            "tenses, questions, commands), 25-34 advanced (stories, "
            "idioms, registers, complex sentences, conversations). "
            "FINAL DRILL: read all three stories aloud; hold all three "
            "market/friend/problem conversations; write 200 words from "
            "memory; narrate your day in past, present, and future."
        ),
        "how_it_works": (
            "This record is the database folded into one page - the "
            "learner's desert-island sheet. It compresses the script to "
            "its counting skeleton (12+18+1+216=247), the vocabulary to "
            "200 core words organized by class, the grammar to its "
            "machines (order, stacking, classes, cases, tenses, "
            "negation, questions, participles, connectors), and the "
            "phrases to their tables by situation. Each compressed item "
            "points back to its full record by name, so the summary is "
            "also an index. The final drill is a graduation exam the "
            "learner gives themselves: three stories read aloud, three "
            "conversations held, 200 words written from memory, one day "
            "narrated in three tenses. Passing it means the ladder is "
            "climbed."
        ),
        "key_points": [
            "Consolidated reference: script, 200 words, grammar, phrase tables.",
            "Script skeleton: 12 + 18 + 1 + 216 = 247.",
            "Grammar machines: SOV, stacking, classes, cases, tenses, negation, questions.",
            "Phrase tables by situation: greetings, travel, market, health, emotions, time.",
            "Self-graduation drill: stories, conversations, 200 words, three tenses.",
        ],
        "requirements": [
            "Write the full script inventory from memory and verify.",
            "Write 200 core Tamil words from memory with meanings.",
            "Recite the case suffixes and tense markers cold.",
            "Hold all three conversations without the book.",
            "Narrate your day in past, present, and future Tamil.",
        ],
        "standards": [
            "Summary verified against all 33 preceding records.",
            "Forms follow Lehmann 1989 and Schiffman 1999 throughout.",
        ],
        "citations": [CIT_LEHMANN, CIT_SCHIFFMAN, CIT_TOLKAPPIYAM, CIT_THIRUKKURAL],
        "sig_lens": (
            "The Signature read: the summary is the seal upon the whole "
            "- 34 records folded into one signed page. Where public "
            "reviews file cheat sheets, the Signature Word Method files "
            "the graduation: the learner's tongue now the seal-bearer of "
            "தமிழ் itself."
        ),
    },
]
