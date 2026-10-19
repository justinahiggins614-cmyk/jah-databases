#!/usr/bin/env python3
"""34 ladder-ordered record seeds for the Marathi Language Database.

Follows the shared per-language template (language-template.md) EXACTLY:
records 1-34 in order, ladder_rank 1-10 non-decreasing, ladder_tier
foundations -> compounded -> advanced. Every record carries Marathi content
in Devanagari plus transliteration plus English translation plus example
sentences. All Marathi is real, fact-checked 2026-10-17 (Marathi, मराठी,
Indo-European > Indo-Iranian > Indo-Aryan, ISO 639-1 mr, ISO 639-3 mar).

Verified 2026-10-17: RAW SWEEP of the full manifest (2,410 databases) PLUS
every shard index title in jah-databases-data-1 (825 index files): zero
'language-marathi*' slugs/names; zero 'marathi language' title collisions.
ID prefixes JAH-LMAR- (public) and JAH-LMARS- (signature) verified free in
manifest id_prefix values and in every shard index file (zero hits).

Screened 2026-10-17: nothing hate-adjacent, profane, or inappropriate;
no religious talk; no military/defense content.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature language instrument: "
            "Marathi re-taught as a working system he commands, every speaker "
            "count a measure of the instrument's reach, every dialect another "
            "string he can play, every rule a control he operates. Clearly "
            "labeled Signature-made, never presented as an outside authority's "
            "text.")

CIT_DW = ("Dhongde, R. V. & Wali, Kashi. Marathi. John Benjamins; 2009 "
          "(London Oriental and African Language Library).")
CIT_MASICA = ("Masica, Colin P. The Indo-Aryan Languages. Cambridge "
              "University Press; 1991.")
CIT_MOLES = ("Molesworth, J. T. A Dictionary, Marathi and English. 2nd ed. "
             "Bombay Education Society; 1857.")
CIT_ISO = ("ISO 639-1:2002 code 'mr' for Marathi; ISO 639-3:2007 code 'mar' "
           "for Marathi.")
CIT_UNI = ("The Unicode Standard, Devanagari block U+0900-U+097F.")

ENTRIES = [
# ================================================================== 1
{
 "key": "overview", "name": "Marathi Language Overview",
 "group": "Foundations", "ladder": 1, "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Marathi (मराठी, marāṭhī) is an Indo-Aryan language of the Indo-European family, "
  "spoken as a first language by about 99 million people, making it one of the most "
  "spoken languages in the world. Its ISO codes are ISO 639-1 'mr' and ISO 639-3 'mar'. "
  "Marathi is written in the Devanagari script (देवनागरी), read left to right, and "
  "follows subject-object-verb word order. It is the official language of the Indian "
  "state of Maharashtra and a co-official language of Goa, and it is listed in the "
  "Eighth Schedule of the Indian Constitution. Outside Maharashtra it is widely spoken "
  "in Goa, parts of Karnataka, Madhya Pradesh, Gujarat, Andhra Pradesh, Telangana and "
  "Tamil Nadu, and by diaspora communities including the Bene Israel of Israel. Marathi "
  "descends from Maharashtri Prakrit through Apabhramsha, is attested in inscriptions "
  "from around the 10th century, and its literature begins with Mukundaraja's "
  "Vivekasindhu (c. 1188 CE) and flowers in Sant Dnyaneshwar's Dnyaneshwari (1290 CE). "
  "Its major dialects include Varhadi (वऱ्हाडी) of Vidarbha, Malvani (मालवणी) of the "
  "Konkan coast, and Ahirani (अहिराणी) of Khandesh. Example: मी मराठी बोलतो "
  "(mī marāṭhī bolto) - 'I speak Marathi'. Greeting example: नमस्कार (namaskār) - "
  "'greetings'. Politeness example: धन्यवाद (dhanyavād) - 'thank you'. Everyday "
  "example: हे पुस्तक चांगले आहे (he pustak cāṅgle āhe) - 'This book is good'. "
  "Farewell example: पुन्हा भेटू (punhā bheṭū) - 'See you again'."),
 "how_it_works": (
  "This record works as the front door of the whole database: it names the language "
  "in English and in Devanagari, places it in its language family, gives the speaker "
  "numbers, lists where it is spoken and its official status, traces its history and "
  "dialects, and closes with five translated example sentences you can say at once. "
  "Every later record builds on these facts, so read this one first."),
 "key_points": [
  "Marathi (मराठी, marāṭhī): Indo-European > Indo-Iranian > Indo-Aryan; ISO 639-1 mr, ISO 639-3 mar.",
  "About 99 million native speakers; total speakers above 100 million including second-language users.",
  "Written in Devanagari, read left to right; basic word order is subject-object-verb.",
  "Official language of Maharashtra and co-official in Goa; Eighth Schedule language.",
  "Descends from Maharashtri Prakrit; literature from the 12th-13th century (Vivekasindhu, Dnyaneshwari).",
  "Major dialects: Varhadi, Malvani, Ahirani; standard based on the Pune-Mumbai region.",
  "मी मराठी बोलतो (mī marāṭhī bolto) - 'I speak Marathi' shows SOV order in action.",
 ],
 "requirements": [
  "No prior Marathi needed - this is the starting point of the ladder.",
  "Read the Devanagari words aloud using the romanization beside them.",
  "Remember: मराठी (marāṭhī) is the language's own name for itself.",
 ],
 "standards": [CIT_ISO, CIT_UNI],
 "citations": [CIT_DW, CIT_MASICA],
 "sig_lens": (
  "Through the Signature lens this overview is re-taught as his original Signature "
  "language instrument: Marathi as a working system he commands, where the 99 million "
  "speakers measure the instrument's reach and every dialect is another string he can "
  "play. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 2
{
 "key": "writing", "name": "Marathi Writing System: Devanagari and Modi",
 "group": "Foundations", "ladder": 2, "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Marathi is written in Devanagari (देवनागरी, devanāgarī), an abugida script read "
  "left to right. Every consonant carries an inherent 'a' vowel unless marked "
  "otherwise. The 13 vowels are: अ (a), आ (ā), इ (i), ई (ī), उ (u), ऊ (ū), ऋ (ṛ), "
  "ए (e), ऐ (ai), ओ (o), औ (au), अं (aṁ), अः (aḥ). The 34 consonants are: क (ka), "
  "ख (kha), ग (ga), घ (gha), ङ (ṅa), च (ca), छ (cha), ज (ja), झ (jha), ञ (ña), ट "
  "(ṭa), ठ (ṭha), ड (ḍa), ढ (ḍha), ण (ṇa), त (ta), थ (tha), द (da), ध (dha), न "
  "(na), प (pa), फ (pha), ब (ba), भ (bha), म (ma), य (ya), र (ra), ल (la), व (va), "
  "श (śa), ष (ṣa), स (sa), ह (ha), ळ (ḷa). The letter ळ is the Marathi retroflex "
  "lateral flap, as in काळ (kāḷ) - 'time, era' and बाळ (bāḷ) - 'child'. Vowel signs "
  "(matras) attach to consonants: ा ि ी ु ू ृ े ै ो ौ ं ः - for example क + ी = की "
  "(kī). Special marks: anusvara ं (nasalizes, as in मां mā̃), visarga ः (a breathy "
  "h, as in दुःख duḥkha - 'sorrow'), chandrabindu ँ (nasal vowel, as in चाँद cā̃d - "
  "'moon'). Conjuncts join consonants: क्ष (kṣa), त्र (tra), ज्ञ (jña). Marathi "
  "writes the half-ra (reph) in its distinctive eyelash form, as in आर्या (āryā). "
  "Punctuation: the danda । ends a sentence and the double danda ॥ ends a verse. "
  "Devanagari digits are ० १ २ ३ ४ ५ ६ ७ ८ ९ (0-9). Historically Marathi was also "
  "written in the Modi script (मोडी), used for administration and literature until "
  "the 1950s, when Balbodh Devanagari became the standard. Example words: नमस्कार "
  "(namaskār) - 'greetings'; पाणी (pāṇī) - 'water'; पुस्तक (pustak) - 'book'; घर "
  "(ghar) - 'house'; शाळा (śāḷā) - 'school'. Full sentence: मी मराठी वाचतो "
  "(mī marāṭhī vācto) - 'I read Marathi'."),
 "how_it_works": (
  "This record teaches the script the way it is used: the vowel list and the "
  "consonant list with romanization, the vowel signs that reshape consonants, the "
  "special marks and conjuncts, the Marathi-specific ळ and eyelash reph, sentence "
  "punctuation, the digits, and the historical Modi script. Read each letter aloud "
  "with its romanization until the shapes feel familiar, then read the example words "
  "and the full sentence."),
 "key_points": [
  "Devanagari is an abugida read left to right; consonants carry an inherent 'a'.",
  "13 vowels: अ आ इ ई उ ऊ ऋ ए ऐ ओ औ अं अः; 34 consonants including Marathi ळ (ḷa).",
  "Vowel signs reshape consonants: क + ी = की (kī); anusvara ं, visarga ः, chandrabindu ँ.",
  "Conjuncts क्ष त्र ज्ञ; Marathi uses the distinctive eyelash form of half-ra.",
  "Danda । ends a sentence; digits ०-९; the Modi script (मोडी) served Marathi until the 1950s.",
  "मी मराठी वाचतो (mī marāṭhī vācto) - 'I read Marathi'.",
 ],
 "requirements": [
  "Practice writing each letter while saying its romanized sound.",
  "Learn ळ (ḷa) and the eyelash reph as the two most Marathi-specific shapes.",
  "Remember the Modi script as history; write daily Marathi in Devanagari.",
 ],
 "standards": [CIT_UNI, CIT_ISO],
 "citations": [CIT_DW, CIT_MASICA],
 "sig_lens": (
  "Through the Signature lens the script is his instrument panel: 13 vowel keys and "
  "34 consonant keys, the ळ key that Hindi lacks, the eyelash reph as his signature "
  "stroke. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 3
{
 "key": "phonology", "name": "Marathi Sounds and Pronunciation",
 "group": "Foundations", "ladder": 3, "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Marathi pronunciation is highly regular: words sound the way they are spelled. "
  "The vowel अ is pronounced as a central 'uh' (schwa) in many positions, so कमळ "
  "(kamaḷ) sounds like 'kuh-mul'. Retroflex consonants ट ठ ड ढ ण are made with the "
  "tongue curled back, unlike English t/d. The letter ळ (ḷa) is a retroflex lateral "
  "flap unique to Marathi among major Devanagari languages: काळ (kāḷ) - 'time'. "
  "Aspiration matters: क (ka) vs ख (kha), त (ta) vs थ (tha) are different sounds. "
  "Stress falls lightly, usually on the first heavy syllable, and Marathi has no "
  "tones. The inherent 'a' is dropped at word ends (schwa deletion), so राम "
  "(rām) is pronounced 'raam' not 'raa-ma'. Nasalization (ं/ँ) colors the vowel: "
  "मां (mā̃). Spoken examples: 1. पाणी (pāṇī) - 'water'; 2. घर (ghar) - 'house'; "
  "3. शाळा (śāḷā) - 'school'; 4. मुलगा (mulgā) - 'boy'; 5. मुलगी (mulgī) - 'girl'; "
  "6. पुस्तक (pustak) - 'book'; 7. झाड (jhāḍ) - 'tree'; 8. फूल (phūl) - 'flower'; "
  "9. रस्ता (rastā) - 'road'; 10. बाजार (bājār) - 'market'; 11. चहा (cahā) - 'tea'; "
  "12. भात (bhāt) - 'rice'; 13. आई (āī) - 'mother'; 14. वडील (vaḍīl) - 'father'. "
  "Say each word slowly, then at normal speed, and compare with the romanization."),
 "how_it_works": (
  "This record maps the Marathi sound system onto sounds you already know: the "
  "schwa 'a', the curled-tongue retroflexes, the Marathi-only ळ, aspiration pairs, "
  "schwa deletion at word ends, and nasalization. The 14 spoken examples give your "
  "mouth the full workout; repeat each three times, slowly then at speed."),
 "key_points": [
  "Pronunciation is regular: spell it, say it - with schwa deletion at word ends.",
  "Retroflexes ट ठ ड ढ ण use a curled tongue; aspiration pairs (क/ख, त/थ) are distinct.",
  "ळ (ḷa) is the Marathi-only retroflex lateral flap: काळ (kāḷ) - 'time'.",
  "Light stress, no tones; nasalization (ं/ँ) colors vowels: मां (mā̃).",
  "14 spoken examples cover everyday words: पाणी (water), घर (house), शाळा (school).",
 ],
 "requirements": [
  "Say every example word aloud three times: slow, slower, normal speed.",
  "Curl the tongue for retroflexes; feel the difference between त and ट.",
  "Record yourself and compare with the romanization until they match.",
 ],
 "standards": [CIT_UNI, "Schwa-deletion and retroflex articulation per standard Marathi phonology (Dhongde & Wali 2009, ch. 2)."],
 "citations": [CIT_DW, CIT_MASICA],
 "sig_lens": (
  "Through the Signature lens the sound system is his tuning protocol: regular "
  "spelling, curled-tongue retroflexes, the ळ string no neighbor instrument has. "
  "Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 4
{
 "key": "nouns", "name": "Marathi Core Nouns I: People, Places, Things",
 "group": "Foundations", "ladder": 4, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Twenty-five essential Marathi nouns with English meanings and one example "
  "sentence each, translated. Marathi nouns have three genders - masculine, "
  "feminine, neuter - which control adjective and verb agreement. 1. माणूस "
  "(māṇūs) - 'person': तो चांगला माणूस आहे (to cāṅglā māṇūs āhe) - 'He is a good "
  "person'. 2. आई (āī) - 'mother': माझी आई स्वयंपाक करते (mājhī āī svayampāk "
  "karte) - 'My mother cooks'. 3. वडील (vaḍīl) - 'father': माझे वडील शेतकरी आहेत "
  "(mājhe vaḍīl śetkarī āhet) - 'My father is a farmer'. 4. मुलगा (mulgā) - 'boy': "
  "मुलगा खेळतो (mulgā kheḷto) - 'The boy plays'. 5. मुलगी (mulgī) - 'girl': मुलगी "
  "गाते (mulgī gāte) - 'The girl sings'. 6. मित्र (mitra) - 'friend': तो माझा "
  "मित्र आहे (to mājhā mitra āhe) - 'He is my friend'. 7. घर (ghar) - 'house': "
  "माझे घर मोठे आहे (mājhe ghar moṭhe āhe) - 'My house is big'. 8. शाळा (śāḷā) - "
  "'school': मुलं शाळेत जातात (mulã śāḷet jātāt) - 'The children go to school'. "
  "9. पुस्तक (pustak) - 'book': हे पुस्तक माझे आहे (he pustak mājhe āhe) - 'This "
  "book is mine'. 10. पाणी (pāṇī) - 'water': मला पाणी हवे आहे (malā pāṇī have "
  "āhe) - 'I want water'. 11. जेवण (jevaṇ) - 'meal/food': जेवण तयार आहे (jevaṇ "
  "tayār āhe) - 'The meal is ready'. 12. बाजार (bājār) - 'market': आम्ही बाजारात "
  "जातो (āmhī bājārāt jāto) - 'We go to the market'. 13. रस्ता (rastā) - 'road': "
  "हा रस्ता लांब आहे (hā rastā lāmb āhe) - 'This road is long'. 14. गाव (gāv) - "
  "'village': माझे गाव सुंदर आहे (mājhe gāv sundar āhe) - 'My village is "
  "beautiful'. 15. शहर (śahar) - 'city': पुणे एक मोठे शहर आहे (puṇe ek moṭhe "
  "śahar āhe) - 'Pune is a big city'. 16. झाड (jhāḍ) - 'tree': झाडाखाली सावली आहे "
  "(jhāḍākhālī sāvlī āhe) - 'There is shade under the tree'. 17. फूल (phūl) - "
  "'flower': हे फूल लाल आहे (he phūl lāl āhe) - 'This flower is red'. 18. प्राणी "
  "(prāṇī) - 'animal': कुत्रा एक प्राणी आहे (kutrā ek prāṇī āhe) - 'A dog is an "
  "animal'. 19. वेळ (veḷ) - 'time': आता वेळ झाली (ātā veḷ jhālī) - 'It is time "
  "now'. 20. दिवस (divas) - 'day': आज छान दिवस आहे (āj chān divas āhe) - 'Today "
  "is a nice day'. 21. काम (kām) - 'work': माझे काम महत्त्वाचे आहे (mājhe kām "
  "mahattvāce āhe) - 'My work is important'. 22. पैसा (paisā) - 'money': माझ्याकडे "
  "पैसे नाहीत (mājhyākaḍe paise nāhīt) - 'I have no money'. 23. नाव (nāv) - "
  "'name': तुझे नाव काय आहे (tujhe nāv kāy āhe) - 'What is your name'. 24. प्रश्न "
  "(praśna) - 'question': मला एक प्रश्न आहे (malā ek praśna āhe) - 'I have a "
  "question'. 25. उत्तर (uttar) - 'answer': उत्तर बरोबर आहे (uttar barobar āhe) - "
  "'The answer is correct'. Learn each noun with its gender, since adjectives and "
  "verbs agree with it."),
 "how_it_works": (
  "This record builds your noun foundation: 25 high-frequency nouns spanning "
  "people, places, and things, each shown in a real sentence so you learn the "
  "noun inside living Marathi. Note the gender of each noun - masculine (मुलगा), "
  "feminine (मुलगी), neuter (घर) - because adjectives and verbs change to match "
  "it. Say each sentence aloud; the noun is the anchor, the sentence is the "
  "neighborhood."),
 "key_points": [
  "25 essential nouns: people (माणूस, आई, वडील), places (घर, शाळा, बाजार), things (पुस्तक, पाणी, वेळ).",
  "Marathi nouns have three genders: masculine, feminine, neuter - learn the gender with the word.",
  "Gender controls agreement: चांगला मुलगा (masc), चांगली मुलगी (fem), चांगले घर (neut).",
  "माझे घर मोठे आहे (mājhe ghar moṭhe āhe) - 'My house is big'.",
  "मला पाणी हवे आहे (malā pāṇī have āhe) - 'I want water' - the dative experiencer pattern.",
 ],
 "requirements": [
  "Memorize each noun with its gender; flashcards help.",
  "Say all 25 example sentences aloud twice.",
  "Use each noun in one sentence of your own.",
 ],
 "standards": ["Three-gender noun system per standard Marathi grammar (Dhongde & Wali 2009, ch. 4)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens these 25 nouns are his foundation stones: people, "
  "places, things - each carrying its gender like a serial number he reads at a "
  "glance. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 5
{
 "key": "verbs", "name": "Marathi Core Verbs I: Action Words",
 "group": "Foundations", "ladder": 5, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Twenty-five essential Marathi verbs with English meanings and one example "
  "sentence each, translated. Marathi infinitives end in -णे (-ṇe). 1. जाणे "
  "(jāṇe) - 'to go': मी शाळेत जातो (mī śāḷet jāto) - 'I go to school'. 2. येणे "
  "(yeṇe) - 'to come': तो उद्या येईल (to udyā yeīl) - 'He will come tomorrow'. "
  "3. करणे (karaṇe) - 'to do': मी काम करतो (mī kām karto) - 'I do the work'. "
  "4. खाणे (khāṇe) - 'to eat': आम्ही भात खातो (āmhī bhāt khāto) - 'We eat rice'. "
  "5. पिणे (piṇe) - 'to drink': ती चहा पिते (tī cahā pite) - 'She drinks tea'. "
  "6. बोलणे (bolaṇe) - 'to speak': तो मराठी बोलतो (to marāṭhī bolto) - 'He speaks "
  "Marathi'. 7. वाचणे (vācaṇe) - 'to read': मी पुस्तक वाचतो (mī pustak vācto) - "
  "'I read a book'. 8. लिहिणे (lihiṇe) - 'to write': ती पत्र लिहिते (tī patra "
  "lihite) - 'She writes a letter'. 9. पाहणे (pāhaṇe) - 'to see/watch': आम्ही "
  "चित्रपट पाहतो (āmhī citrapaṭ pāhto) - 'We watch a movie'. 10. ऐकणे (aikaṇe) - "
  "'to listen': मी गाणे ऐकतो (mī gāṇe aikto) - 'I listen to a song'. 11. देणे "
  "(deṇe) - 'to give': मला पुस्तक दे (malā pustak de) - 'Give me the book'. 12. "
  "घेणे (gheṇe) - 'to take': तो पैसे घेतो (to paise gheto) - 'He takes the money'. "
  "13. बसणे (basaṇe) - 'to sit': ती खुर्चीवर बसते (tī khurcīvar baste) - 'She sits "
  "on the chair'. 14. उभे राहणे (ubhe rāhaṇe) - 'to stand': तो दारात उभा राहतो "
  "(to dārāt ubhā rāhto) - 'He stands at the door'. 15. झोपणे (jhopaṇe) - 'to "
  "sleep': बाळ झोपते (bāḷ jhopte) - 'The baby sleeps'. 16. उठणे (uṭhaṇe) - 'to "
  "wake/get up': मी सकाळी उठतो (mī sakāḷī uṭhto) - 'I wake up in the morning'. "
  "17. चालणे (cālaṇe) - 'to walk': आम्ही बागेत चालतो (āmhī bāget cālto) - 'We walk "
  "in the garden'. 18. धावणे (dhāvaṇe) - 'to run': मुलगा वेगाने धावतो (mulgā "
  "vegāne dhāvto) - 'The boy runs fast'. 19. हसणे (hasaṇe) - 'to laugh': ती "
  "मोठ्याने हसते (tī moṭhyāne haste) - 'She laughs loudly'. 20. रडणे (raḍaṇe) - "
  "'to cry': बाळ रडते (bāḷ raḍte) - 'The baby cries'. 21. शिकणे (śikaṇe) - 'to "
  "learn': मी मराठी शिकतो (mī marāṭhī śikto) - 'I learn Marathi'. 22. शिकवणे "
  "(śikavaṇe) - 'to teach': शिक्षक शिकवतात (śikṣak śikavtāt) - 'The teacher "
  "teaches'. 23. खेळणे (kheḷaṇe) - 'to play': मुलं मैदानात खेळतात (mulã maidānāt "
  "kheḷtāt) - 'The children play in the field'. 24. काम करणे (kām karaṇe) - 'to "
  "work': तो कार्यालयात काम करतो (to kāryālayāt kām karto) - 'He works in the "
  "office'. 25. प्रेम करणे (prem karaṇe) - 'to love': मी माझ्या कुटुंबावर प्रेम "
  "करतो (mī mājhyā kuṭumbāvar prem karto) - 'I love my family'. Present-tense "
  "endings change with gender: -तो (masc), -ते (fem), -तं (neut)."),
 "how_it_works": (
  "This record builds your verb foundation: 25 high-frequency verbs, each in a "
  "real sentence showing the verb alive in context. Marathi infinitives end in "
  "-णे; the present tense adds gendered endings (-तो masculine, -ते feminine, "
  "-तं neuter). Learn each verb's meaning and its sentence; the endings pattern "
  "will start repeating in your ear after a dozen verbs."),
 "key_points": [
  "25 essential verbs; infinitives end in -णे: जाणे (to go), करणे (to do), खाणे (to eat).",
  "Present endings agree with gender: जातो (masc), जाते (fem), जातं (neut).",
  "मी मराठी शिकतो (mī marāṭhī śikto) - 'I learn Marathi'.",
  "आम्ही भात खातो (āmhī bhāt khāto) - 'We eat rice'.",
  "Verbs of giving/taking (देणे, घेणे) take dative recipients: मला पुस्तक दे.",
 ],
 "requirements": [
  "Memorize each verb's infinitive and its example sentence.",
  "Conjugate जाणे and करणे in present tense for all three genders.",
  "Say all 25 sentences aloud twice.",
 ],
 "standards": ["Infinitive in -णे and present-tense gender agreement per standard Marathi grammar (Dhongde & Wali 2009, ch. 6)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens these 25 verbs are his control levers: go, come, "
  "do, eat, speak, learn - each lever moving the world one gendered ending at a "
  "time. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 6
{
 "key": "adjectives", "name": "Marathi Adjectives and Adverbs",
 "group": "Foundations", "ladder": 6, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Twenty-five Marathi adjectives and fifteen adverbs with example sentences. "
  "Marathi adjectives agree in gender and number with the noun they describe: "
  "-ा (masculine), -ी (feminine), -े/-ं (neuter). 1. चांगला (cāṅglā) - 'good': "
  "चांगला मुलगा (cāṅglā mulgā) - 'good boy'; चांगली मुलगी (cāṅglī mulgī) - 'good "
  "girl'; चांगले घर (cāṅgle ghar) - 'good house'. 2. मोठा (moṭhā) - 'big': मोठे "
  "शहर (moṭhe śahar) - 'big city'. 3. लहान (lahān) - 'small': लहान घर (lahān "
  "ghar) - 'small house'. 4. नवीन (navīn) - 'new': नवीन पुस्तक (navīn pustak) - "
  "'new book'. 5. जुना (junā) - 'old': जुनी इमारत (junī imārat) - 'old building'. "
  "6. सुंदर (sundar) - 'beautiful': सुंदर फूल (sundar phūl) - 'beautiful flower'. "
  "7. वाईट (vāīṭ) - 'bad': वाईट बातमी (vāīṭ bātmī) - 'bad news'. 8. लांब (lāmb) - "
  "'long': लांब रस्ता (lāmb rastā) - 'long road'. 9. आखूड (ākhūḍ) - 'short': आखूड "
  "कथा (ākhūḍ kathā) - 'short story'. 10. उंच (uñc) - 'tall/high': उंच झाड (uñc "
  "jhāḍ) - 'tall tree'. 11. खोल (khol) - 'deep': खोल विहीर (khol vihīr) - 'deep "
  "well'. 12. गरम (garam) - 'hot': गरम चहा (garam cahā) - 'hot tea'. 13. थंड (thaṇḍ) "
  "- 'cold': थंड पाणी (thaṇḍ pāṇī) - 'cold water'. 14. गोड (goḍ) - 'sweet': गोड "
  "आंबा (goḍ āmbā) - 'sweet mango'. 15. आंबट (āmbaṭ) - 'sour': आंबट लिंबू (āmbaṭ "
  "limbū) - 'sour lemon'. 16. तिखट (tikhaṭ) - 'spicy': तिखट भाजी (tikhaṭ bhājī) - "
  "'spicy vegetable dish'. 17. श्रीमंत (śrīmanta) - 'rich': श्रीमंत माणूस (śrīmanta "
  "māṇūs) - 'rich person'. 18. गरीब (garīb) - 'poor': गरीब शेतकरी (garīb śetkarī) "
  "- 'poor farmer'. 19. आनंदी (ānandī) - 'happy': आनंदी कुटुंब (ānandī kuṭumba) - "
  "'happy family'. 20. दुःखी (duḥkhī) - 'sad': दुःखी चेहरा (duḥkhī cehrā) - 'sad "
  "face'. 21. हुशार (huśār) - 'clever': हुशार विद्यार्थी (huśār vidyārthī) - "
  "'clever student'. 22. आळशी (āḷaśī) - 'lazy': आळशी मुलगा (āḷaśī mulgā) - 'lazy "
  "boy'. 23. स्वच्छ (svaccha) - 'clean': स्वच्छ खोली (svaccha kholī) - 'clean "
  "room'. 24. घाणेरडा (ghāṇeraḍā) - 'dirty': घाणेरडा रस्ता (ghāṇeraḍā rastā) - "
  "'dirty road'. 25. महत्त्वाचा (mahattvācā) - 'important': महत्त्वाचे काम "
  "(mahattvāce kām) - 'important work'. Adverbs: 1. वेगाने (vegāne) - 'quickly': "
  "तो वेगाने धावतो (to vegāne dhāvto) - 'He runs quickly'. 2. हळू (haḷū) - "
  "'slowly': ती हळू चालते (tī haḷū cālte) - 'She walks slowly'. 3. नेहमी (nehmī) - "
  "'always': मी नेहमी सत्य बोलतो (mī nehmī satya bolto) - 'I always speak the "
  "truth'. 4. कधीही (kadhīhī) - 'never': तो कधीही खोटे बोलत नाही (to kadhīhī "
  "khoṭe bolat nāhī) - 'He never lies'. 5. आज (āj) - 'today': आज पाऊस पडतो (āj "
  "pāūs paḍto) - 'It rains today'. 6. उद्या (udyā) - 'tomorrow': उद्या सुट्टी आहे "
  "(udyā suṭṭī āhe) - 'Tomorrow is a holiday'. 7. काल (kāl) - 'yesterday': काल मी "
  "बाजारात गेलो (kāl mī bājārāt gelo) - 'Yesterday I went to the market'. 8. इथे "
  "(ithe) - 'here': इथे बसा (ithe basā) - 'Sit here'. 9. तिथे (tithe) - 'there': "
  "तिथे जा (tithe jā) - 'Go there'. 10. खूप (khūp) - 'very/much': खूप छान (khūp "
  "chān) - 'very nice'. 11. थोडे (thoḍe) - 'a little': थोडे पाणी दे (thoḍe pāṇī "
  "de) - 'Give a little water'. 12. एकत्र (ekatra) - 'together': आम्ही एकत्र "
  "जातो (āmhī ekatra jāto) - 'We go together'. 13. एकटे (ekaṭe) - 'alone': तो "
  "एकटा राहतो (to ekaṭā rāhto) - 'He lives alone'. 14. पुन्हा (punhā) - 'again': "
  "पुन्हा प्रयत्न कर (punhā prayatna kar) - 'Try again'. 15. नक्की (nakkī) - "
  "'surely': मी नक्की येईन (mī nakkī yeīn) - 'I will surely come'. Adverbs do not "
  "change form; adjectives agree with their noun."),
 "how_it_works": (
  "This record teaches description: 25 adjectives that bend to match their noun's "
  "gender and number, plus 15 adverbs that stay fixed while coloring the verb. "
  "Watch the same adjective wear three endings - चांगला/चांगली/चांगले - and the "
  "adverbs sit before the verb like वेगाने. Practice by describing five things "
  "around you with gender-matched adjectives."),
 "key_points": [
  "25 adjectives + 15 adverbs, each with a translated example sentence.",
  "Adjectives agree in gender/number: चांगला मुलगा / चांगली मुलगी / चांगले घर.",
  "Adverbs are invariable: वेगाने धावतो (runs quickly), हळू चालते (walks slowly).",
  "काल/आज/उद्या (yesterday/today/tomorrow) anchor time; इथे/तिथे anchor place.",
  "खूप (khūp) intensifies: खूप छान - 'very nice'.",
 ],
 "requirements": [
  "Describe 10 objects around you with gender-matched adjectives.",
  "Use each of the 15 adverbs in a sentence of your own.",
  "Say all example sentences aloud.",
 ],
 "standards": ["Adjective agreement in gender and number per standard Marathi grammar (Dhongde & Wali 2009, ch. 5)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens adjectives are his paint and adverbs his brush "
  "speed: the paint changes shade for every noun it touches, the brush speed "
  "never changes. Signature-made teaching, clearly labeled, never presented as "
  "an outside authority's text."),
},
# ================================================================== 7
{
 "key": "pronouns", "name": "Marathi Pronouns: Full Paradigms",
 "group": "Foundations", "ladder": 7, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Marathi personal, possessive, demonstrative, and interrogative pronouns with "
  "full paradigms and example sentences. Personal pronouns: मी (mī) - 'I': मी "
  "जातो (mī jāto) - 'I go'. तू (tū) - 'you (informal)': तू ये (tū ye) - 'You "
  "come'. तुम्ही (tumhī) - 'you (formal/plural)': तुम्ही बसा (tumhī basā) - 'Please "
  "sit'. तो (to) - 'he': तो खेळतो (to kheḷto) - 'He plays'. ती (tī) - 'she': ती "
  "गाते (tī gāte) - 'She sings'. ते (te) - 'it/they': ते झाड आहे (te jhāḍ āhe) - "
  "'It is a tree'; ते येतात (te yetāt) - 'They come'. आम्ही (āmhī) - 'we "
  "(exclusive)': आम्ही जातो (āmhī jāto) - 'We go'. आपण (āpaṇ) - 'we (inclusive) "
  "/ polite you': आपण जाऊया (āpaṇ jāūyā) - 'Let us go'. Oblique forms before "
  "postpositions: मला (malā) - 'to me': मला भूक लागली (malā bhūk lāglī) - 'I am "
  "hungry'. तुला (tulā) - 'to you': तुला काय हवे (tulā kāy have) - 'What do you "
  "want'. त्याला (tyālā) - 'to him': त्याला विचारा (tyālā vicārā) - 'Ask him'. "
  "Possessives agree with the owned noun's gender: माझा/माझी/माझे (mājhā/mājhī/"
  "mājhe) - 'my': माझा भाऊ (mājhā bhāū) - 'my brother'; माझी बहीण (mājhī bahīṇ) - "
  "'my sister'; माझे घर (mājhe ghar) - 'my house'. तुझा/तुझी/तुझे (tujhā/tujhī/"
  "tujhe) - 'your (informal)': तुझी शाळा (tujhī śāḷā) - 'your school'. तुमचा/तुमची/"
  "तुमचे (tumcā/tumcī/tumce) - 'your (formal)': तुमचे नाव (tumce nāv) - 'your "
  "name'. त्याचा/त्याची/त्याचे (tyācā/tyācī/tyāce) - 'his': त्याचे पुस्तक (tyāce "
  "pustak) - 'his book'. तिचा/तिची/तिचे (ticā/ticī/tice) - 'her': तिची मैत्रीण "
  "(ticī maitrīṇ) - 'her friend'. आमचा/आमची/आमचे (āmcā/āmcī/āmce) - 'our': आमचे "
  "गाव (āmce gāv) - 'our village'. Demonstratives: हा/ही/हे (hā/hī/he) - 'this': "
  "हा मुलगा (hā mulgā) - 'this boy'. तो/ती/ते (to/tī/te) - 'that': तो रस्ता (to "
  "rastā) - 'that road'. Interrogatives: कोण (koṇ) - 'who': तो कोण आहे (to koṇ "
  "āhe) - 'Who is he'. काय (kāy) - 'what': हे काय आहे (he kāy āhe) - 'What is "
  "this'. कुठे (kuṭhe) - 'where': तू कुठे जातोस (tū kuṭhe jātos) - 'Where are you "
  "going'. कधी (kadhī) - 'when': तू कधी येशील (tū kadhī yeśīl) - 'When will you "
  "come'. का (kā) - 'why': तू का रडतोस (tū kā raḍtos) - 'Why are you crying'. कसा/"
  "कशी/कसे (kasā/kaśī/kase) - 'how': तू कसा आहेस (tū kasā āhes) - 'How are you'. "
  "किती (kitī) - 'how many': किती पैसे (kitī paise) - 'How much money'."),
 "how_it_works": (
  "This record is the pronoun switchboard: personal pronouns for who acts, "
  "oblique forms (मला, तुला) for who receives, possessives that agree with the "
  "owned thing's gender, demonstratives for pointing, and interrogatives for "
  "asking. Master आपण vs आम्ही (inclusive vs exclusive 'we') - it changes the "
  "meaning of every invitation you make."),
 "key_points": [
  "Personal: मी, तू, तुम्ही, तो/ती/ते, आम्ही, आपण - with oblique मला, तुला, त्याला.",
  "आपण (inclusive we) vs आम्ही (exclusive we): आपण जाऊया - 'Let us (you and I) go'.",
  "Possessives agree with the owned noun: माझा भाऊ / माझी बहीण / माझे घर.",
  "Demonstratives: हा/ही/हे (this), तो/ती/ते (that); interrogatives: कोण, काय, कुठे, कधी, का, कसा, किती.",
  "मला भूक लागली (malā bhūk lāglī) - 'I am hungry' - the dative experiencer pattern.",
 ],
 "requirements": [
  "Conjugate the pronoun table from memory: I, you, he/she/it, we, they.",
  "Write three sentences each with माझा/माझी/माझे.",
  "Ask and answer five questions using each interrogative once.",
 ],
 "standards": ["Inclusive/exclusive first-person plural and oblique case forms per standard Marathi grammar (Dhongde & Wali 2009, ch. 4)."],
 "citations": [CIT_DW, CIT_MASICA],
 "sig_lens": (
  "Through the Signature lens pronouns are his cast list: who speaks, who is "
  "spoken to, who owns what - and the inclusive आपण that pulls the listener "
  "onto his stage. Signature-made teaching, clearly labeled, never presented as "
  "an outside authority's text."),
},
# ================================================================== 8
{
 "key": "numbers", "name": "Marathi Numbers, Time, and Dates",
 "group": "Foundations", "ladder": 8, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Marathi numbers 1 to 100, ordinals, days, months, seasons, clock time, and "
  "dates, each with example sentences. Cardinal numbers: 1 एक (ek), 2 दोन (don), "
  "3 तीन (tīn), 4 चार (cār), 5 पाच (pāc), 6 सहा (sahā), 7 सात (sāt), 8 आठ (āṭh), "
  "9 नऊ (naū), 10 दहा (dahā), 11 अकरा (akrā), 12 बारा (bārā), 13 तेरा (terā), 14 "
  "चौदा (caudā), 15 पंधरा (pandharā), 16 सोळा (soḷā), 17 सतरा (satarā), 18 अठरा "
  "(aṭharā), 19 एकोणवीस (ekoṇavīs), 20 वीस (vīs), 21 एकवीस (ekvīs), 30 तीस (tīs), "
  "40 चाळीस (cāḷīs), 50 पन्नास (pannās), 60 साठ (sāṭh), 70 सत्तर (sattar), 80 ऐंशी "
  "(aĩśī), 90 नव्वद (navvad), 100 शंभर (śambhar), 1000 हजार (hajār). Example: "
  "माझ्याकडे पाच पुस्तके आहेत (mājhyākaḍe pāc pustake āhet) - 'I have five books'. "
  "Ordinals: पहिला (pahilā) - 'first': पहिला दिवस (pahilā divas) - 'the first day'; "
  "दुसरा (dusrā) - 'second'; तिसरा (tisrā) - 'third'. Days of the week: सोमवार "
  "(somvār) - 'Monday', मंगळवार (maṅgaḷvār) - 'Tuesday', बुधवार (budhvār) - "
  "'Wednesday', गुरुवार (guruvār) - 'Thursday', शुक्रवार (śukravār) - 'Friday', "
  "शनिवार (śanivār) - 'Saturday', रविवार (ravivār) - 'Sunday'. Example: आज सोमवार "
  "आहे (āj somvār āhe) - 'Today is Monday'. Months (Gregorian): जानेवारी "
  "(jānevārī), फेब्रुवारी (phebrūvārī), मार्च (mārca), एप्रिल (epril), मे (me), जून "
  "(jūn), जुलै (julai), ऑगस्ट (ŏgasṭa), सप्टेंबर (sapṭembar), ऑक्टोबर (ŏkṭobar), "
  "नोव्हेंबर (novhembar), डिसेंबर (ḍisembar). Traditional months: चैत्र (caitra), "
  "वैशाख (vaiśākh), ज्येष्ठ (jyeṣṭha), आषाढ (āṣāḍh), श्रावण (śrāvaṇ), भाद्रपद "
  "(bhādrapad), आश्विन (āśvin), कार्तिक (kārtik), मार्गशीर्ष (mārgaśīrṣa), पौष "
  "(pauṣa), माघ (māgh), फाल्गुन (phālgun). Seasons: उन्हाळा (unhāḷā) - 'summer', "
  "पावसाळा (pāvsāḷā) - 'monsoon', हिवाळा (hivāḷā) - 'winter'. Example: पावसाळ्यात "
  "पाऊस पडतो (pāvsāḷyāt pāūs paḍto) - 'It rains in the monsoon'. Clock time: किती "
  "वाजले (kitī vājle) - 'What time is it'; तीन वाजले (tīn vājle) - 'It is three "
  "o'clock'; साडेतीन (sāḍetīn) - 'half past three'; पावणेचार (pāvaṇecār) - "
  "'quarter to four'; सव्वाचार (savvācār) - 'quarter past four'. Example: मी "
  "सकाळी सात वाजता उठतो (mī sakāḷī sāt vājtā uṭhto) - 'I wake up at seven in the "
  "morning'. Dates: १५ ऑगस्ट (15 ŏgasṭa) - '15th August'; माझा वाढदिवस पाच जूनला "
  "आहे (mājhā vāḍhadivas pāc jūnlā āhe) - 'My birthday is on the fifth of June'."),
 "how_it_works": (
  "This record makes you numerate in Marathi: the 1-100 sequence with its "
  "nineteen 'ekoṇa' teens pattern, ordinals, the seven weekdays, both month "
  "systems, the three Marathi seasons, and clock time with साडे/पावणे/सव्वा. "
  "Count aloud 1-20 daily; ask किती वाजले every hour until the clock answers in "
  "Marathi by itself."),
 "key_points": [
  "1-100 with the ekoṇa- pattern (एकोणवीस = 19); 100 शंभर, 1000 हजार.",
  "Ordinals: पहिला, दुसरा, तिसरा; days: सोमवार through रविवार.",
  "Three seasons: उन्हाळा (summer), पावसाळा (monsoon), हिवाळा (winter).",
  "Clock: साडेतीन (3:30), पावणेचार (3:45), सव्वाचार (4:15); किती वाजले - 'What time is it'.",
  "मी सकाळी सात वाजता उठतो - 'I wake up at seven in the morning'.",
 ],
 "requirements": [
  "Count 1-100 aloud without stopping; then count backwards 20-1.",
  "Say the time in Marathi every hour for one day.",
  "Write your birthday and today's date in Marathi.",
 ],
 "standards": ["Devanagari digits ०-९ per the Unicode Standard, Devanagari block U+0900-U+097F."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens numbers are his measuring tape: एक to शंभर, the "
  "three seasons, the clock that answers किती वाजले - every count a calibration "
  "of his instrument. Signature-made teaching, clearly labeled, never presented "
  "as an outside authority's text."),
},
# ================================================================== 9
{
 "key": "greetings", "name": "Marathi Greetings and Everyday Phrases",
 "group": "Foundations", "ladder": 9, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Thirty Marathi greetings, farewells, and politeness phrases with English "
  "meanings and usage notes. 1. नमस्कार (namaskār) - 'greetings/hello' - the "
  "universal respectful greeting. 2. राम राम (rām rām) - 'hello' - warm rural "
  "greeting. 3. सुप्रभात (suprabhāt) - 'good morning'. 4. शुभ दुपार (śubh dupār) "
  "- 'good afternoon'. 5. शुभ संध्याकाळ (śubh sandhyākāḷ) - 'good evening'. 6. "
  "शुभ रात्री (śubh rātrī) - 'good night'. 7. कसे आहात (kase āhāt) - 'How are "
  "you (formal)'. 8. कसा आहेस (kasā āhes) - 'How are you (informal, to a male)'. "
  "9. कशी आहेस (kaśī āhes) - 'How are you (informal, to a female)'. 10. मी ठीक "
  "आहे (mī ṭhīk āhe) - 'I am fine'. 11. धन्यवाद (dhanyavād) - 'thank you'. 12. "
  "खूप खूप आभार (khūp khūp ābhār) - 'many thanks'. 13. माफ करा (māph karā) - "
  "'sorry/excuse me (formal)'. 14. क्षमा करा (kṣamā karā) - 'forgive me'. 15. "
  "कृपया (kṛpayā) - 'please'. 16. हो (ho) - 'yes'. 17. नाही (nāhī) - 'no'. 18. "
  "चालेल (cālel) - 'okay/fine, it will do'. 19. ठीक आहे (ṭhīk āhe) - 'okay'. 20. "
  "पुन्हा भेटू (punhā bheṭū) - 'see you again'. 21. निरोप (nirop) - 'farewell'. "
  "22. शुभेच्छा (śubhecchā) - 'best wishes'. 23. अभिनंदन (abhinandan) - "
  "'congratulations'. 24. स्वागत आहे (svāgat āhe) - 'welcome'. 25. या, बसा (yā, "
  "basā) - 'come, sit (formal welcome)'. 26. काळजी घ्या (kāḷjī ghyā) - 'take "
  "care'. 27. देव तुमचे भले करो (dev tumce bhale karo) - 'God bless you (formal "
  "blessing)'. 28. काही हरकत नाही (kāhī harkat nāhī) - 'no problem'. 29. मला माफ "
  "करा (malā māph karā) - 'forgive me'. 30. भेटून आनंद झाला (bheṭūn ānand jhālā) "
  "- 'pleased to meet you'. Use तुम्ही forms (कसे आहात, माफ करा) with elders and "
  "strangers; तू forms (कसा आहेस) with friends and juniors."),
 "how_it_works": (
  "This record is your social survival kit: the phrases that open doors, smooth "
  "mistakes, and close conversations warmly. The formality rule is simple - "
  "तुम्ही/तुमचा for respect, तू/तुझा for closeness. Practice each phrase as a "
  "mini-scene: greet, thank, apologize, and say goodbye to an imaginary elder, "
  "then to an imaginary friend."),
 "key_points": [
  "30 greetings/farewells/politeness phrases with usage notes.",
  "नमस्कार is the universal respectful greeting; राम राम is the warm rural hello.",
  "Formality: कसे आहात/माफ करा (formal) vs कसा आहेस (informal).",
  "भेटून आनंद झाला (bheṭūn ānand jhālā) - 'pleased to meet you'.",
  "काही हरकत नाही - 'no problem'; काळजी घ्या - 'take care'.",
 ],
 "requirements": [
  "Role-play greeting an elder, then a friend, using the right forms.",
  "Say all 30 phrases aloud with the right warmth.",
  "Write a three-line greeting exchange of your own.",
 ],
 "standards": ["Levels of address (तू/तुम्ही) per standard Marathi sociolinguistics (Dhongde & Wali 2009, ch. 1)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens greetings are his handshakes: नमस्कार opens every "
  "door, माफ करा repairs every stumble, पुन्हा भेटू promises the next meeting. "
  "Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 10
{
 "key": "grammar", "name": "Marathi Grammar Essentials",
 "group": "Foundations", "ladder": 10, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The essential grammar of Marathi, each rule with translated example sentences. "
  "Word order: subject-object-verb. मी भात खातो (mī bhāt khāto) - 'I eat rice' - "
  "literally 'I rice eat'. Gender: three genders - masculine, feminine, neuter. "
  "मुलगा (mulgā, masc) - 'boy'; मुलगी (mulgī, fem) - 'girl'; घर (ghar, neut) - "
  "'house'. Number: singular and plural. मुलगा/मुलं (mulgā/mulã) - 'boy/boys'; "
  "मुलगी/मुली (mulgī/mulī) - 'girl/girls'. Cases: Marathi uses postpositions on an "
  "oblique stem. Dative/accusative ला (lā): मला पुस्तक दे (malā pustak de) - 'Give "
  "me the book'. Ergative ने (ne) in perfective transitives: मी पुस्तक वाचले (mī "
  "pustak vācle) - 'I read the book'. Instrumental ने (ne): चमच्याने खा (camcyāne "
  "khā) - 'Eat with a spoon'. Genitive चा/ची/चे (cā/cī/ce) agreeing with the owned "
  "noun: माझा भाऊ (mājhā bhāū) - 'my brother'; माझी बहीण (mājhī bahīṇ) - 'my "
  "sister'; माझे घर (mājhe ghar) - 'my house'. Locative त (ta): घरात (gharāt) - "
  "'in the house'; शाळेत (śāḷet) - 'in/at school'. Ablative कडून/पासून (kaḍūn/"
  "pāsūn): माझ्याकडून (mājhyākaḍūn) - 'from me'. Dative साठी (sāṭhī) - 'for': "
  "तुझ्यासाठी (tujhyāsāṭhī) - 'for you'. Comitative बरोबर (barobar) - 'with': "
  "माझ्याबरोबर (mājhyābarobar) - 'with me'. Articles: Marathi has no articles; "
  "एक (ek) - 'one' marks indefiniteness. एक मुलगा (ek mulgā) - 'a boy'. Negation: "
  "नाही (nāhī) after the verb. मी जात नाही (mī jāt nāhī) - 'I do not go'; तो आला "
  "नाही (to ālā nāhī) - 'He did not come'. नको (nako) for 'do not want/need': मला "
  "नको (malā nako) - 'I do not want it'. Questions: question words stay in place; "
  "rising intonation or का (kā) at the end. तू येशील का (tū yeśīl kā) - 'Will you "
  "come'. Ergativity: in the perfective, the subject of a transitive verb takes "
  "ने and the verb agrees with the object. मी आंबा खाल्ला (mī āmbā khāllā) - 'I "
  "ate the mango (masc)'; मी कैरी खाल्ली (mī kairī khāllī) - 'I ate the raw mango "
  "(fem)'. Adjective agreement: मोठा/मोठी/मोठे with masculine/feminine/neuter "
  "nouns."),
 "how_it_works": (
  "This record is the grammar engine room: SOV order, three genders, two numbers, "
  "the postposition case system, no articles, नाही negation, in-place questions, "
  "and the famous ergative ने. Build one sentence per rule, then combine two "
  "rules per sentence, until the engine runs on its own."),
 "key_points": [
  "SOV word order: मी भात खातो - 'I rice eat' = 'I eat rice'.",
  "Three genders, two numbers; postpositions (ला, ने, चा/ची/चे, त, कडून, साठी) mark cases.",
  "Split ergativity: perfective transitives take ने, verb agrees with the object.",
  "Negation with नाही after the verb: मी जात नाही - 'I do not go'.",
  "No articles; एक marks indefiniteness; questions use in-place question words.",
 ],
 "requirements": [
  "Build five SOV sentences of your own and translate them.",
  "Write the ने ergative sentence for three objects of different genders.",
  "Negate five present-tense sentences with नाही.",
 ],
 "standards": ["SOV order, three-gender agreement, and split ergativity per standard Marathi grammar (Dhongde & Wali 2009, ch. 3-6)."],
 "citations": [CIT_DW, CIT_MASICA],
 "sig_lens": (
  "Through the Signature lens grammar is his machine code: SOV the instruction "
  "order, three genders the data types, ने the perfective flag, नाही the NOT "
  "gate. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 11
{
 "key": "home", "name": "Marathi Home and Family Sentences",
 "group": "Compounded", "ladder": 11, "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Twenty Marathi sentences about the house, rooms, furniture, and family "
  "members, each translated. 1. हे माझे घर आहे (he mājhe ghar āhe) - 'This is my "
  "house'. 2. घरात चार खोल्या आहेत (gharāt cār kholyā āhet) - 'There are four "
  "rooms in the house'. 3. स्वयंपाकघरात आई जेवण बनवते (svayampākgharāt āī jevaṇ "
  "banavte) - 'Mother cooks food in the kitchen'. 4. दिवाणखान्यात सोफा आहे "
  "(divāṇkhānyāt sophā āhe) - 'There is a sofa in the living room'. 5. माझ्या "
  "खोलीत एक टेबल आहे (mājhyā kholīt ek ṭebal āhe) - 'There is a table in my room'. "
  "6. खुर्ची टेबलाजवळ आहे (khurcī ṭeblājaval āhe) - 'The chair is near the table'. "
  "7. पलंगावर स्वच्छ चादर आहे (palaṅgāvar svaccha cādar āhe) - 'There is a clean "
  "sheet on the bed'. 8. कपाटात कपडे ठेवले आहेत (kapāṭāt kapaḍe ṭhevle āhet) - "
  "'Clothes are kept in the cupboard'. 9. खिडकीतून वारा येतो (khiḍkītūn vārā "
  "yeto) - 'Wind comes through the window'. 10. दार उघडे आहे (dār ughaḍe āhe) - "
  "'The door is open'. 11. माझे कुटुंब मोठे आहे (mājhe kuṭumba moṭhe āhe) - 'My "
  "family is big'. 12. आजी गोष्ट सांगते (ājī goṣṭa sāṅgte) - 'Grandmother tells a "
  "story'. 13. आजोबा बागेत बसतात (ājobā bāget bastāt) - 'Grandfather sits in the "
  "garden'. 14. माझा भाऊ डॉक्टर आहे (mājhā bhāū ḍŏkṭar āhe) - 'My brother is a "
  "doctor'. 15. माझी बहीण शिक्षिका आहे (mājhī bahīṇ śikṣikā āhe) - 'My sister is "
  "a teacher'. 16. काका उद्या येणार आहेत (kākā udyā yeṇār āhet) - 'Uncle will "
  "come tomorrow'. 17. आत्या मुलांना भेटायला आली (ātyā mulānnā bheṭāylā ālī) - "
  "'Aunt came to meet the children'. 18. आम्ही सगळे एकत्र जेवतो (āmhī sagaḷe "
  "ekatra jevto) - 'We all eat together'. 19. घरासमोर झाड आहे (gharāsamor jhāḍ "
  "āhe) - 'There is a tree in front of the house'. 20. माझे घर मला खूप आवडते "
  "(mājhe ghar malā khūp āvaḍte) - 'I like my house very much'."),
 "how_it_works": (
  "This record furnishes your Marathi house: rooms, furniture, and the family "
  "who lives in it. Notice the locative -त/-ात endings (घरात, खोलीत, बागेत) "
  "placing everything in space, and family titles (आजी, आजोबा, काका, आत्या) "
  "that English needs phrases to express. Walk through your own home naming "
  "each room and person in Marathi."),
 "key_points": [
  "20 sentences: rooms (खोली), furniture (टेबल, खुर्ची, पलंग, कपाट), family (आजी, आजोबा, काका, आत्या).",
  "Locative endings place things: घरात (in the house), बागेत (in the garden), घरासमोर (in front of the house).",
  "Kinship precision: काका (father's brother), आत्या (father's sister).",
  "आम्ही सगळे एकत्र जेवतो - 'We all eat together'.",
 ],
 "requirements": [
  "Label every room and piece of furniture in your home in Marathi.",
  "Introduce your family members in Marathi sentences.",
  "Say all 20 sentences aloud.",
 ],
 "standards": ["Locative case in -त/-ात per standard Marathi grammar (Dhongde & Wali 2009, ch. 4)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens the home is his first territory mapped in "
  "Marathi: every room a labeled zone, every relative a titled officer of the "
  "household. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 12
{
 "key": "food", "name": "Marathi Food and Cooking Sentences",
 "group": "Compounded", "ladder": 12, "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Twenty Marathi sentences about meals, ingredients, cooking actions, and "
  "restaurants, each translated. 1. आज जेवणात काय आहे (āj jevaṇāt kāy āhe) - "
  "'What is for the meal today'. 2. आई वरण-भात बनवते (āī varaṇ-bhāt banavte) - "
  "'Mother makes dal-rice'. 3. पोळी गरम आहे (poḷī garam āhe) - 'The flatbread "
  "is hot'. 4. भाकरी ज्वारीची आहे (bhākrī jvārīcī āhe) - 'The bhakri is made of "
  "sorghum'. 5. भाजीत मीठ कमी आहे (bhājīt mīṭh kamī āhe) - 'There is less salt "
  "in the vegetable dish'. 6. आमटी तिखट झाली (āmṭī tikhaṭ jhālī) - 'The amti "
  "turned out spicy'. 7. मला भात आवडतो (malā bhāt āvaḍto) - 'I like rice'. 8. "
  "चहात साखर घाल (cahāt sākhar ghāl) - 'Put sugar in the tea'. 9. पाणी थंड आहे "
  "(pāṇī thaṇḍ āhe) - 'The water is cold'. 10. फळे ताजी आहेत (phaḷe tājī āhet) - "
  "'The fruits are fresh'. 11. आंबा गोड आहे (āmbā goḍ āhe) - 'The mango is "
  "sweet'. 12. कांदा चिर (kāndā cir) - 'Chop the onion'. 13. तेल तापव (tel tāpav) "
  "- 'Heat the oil'. 14. डाळ शिजली का (ḍāḷ śijlī kā) - 'Is the dal cooked'. 15. "
  "जेवण तयार आहे (jevaṇ tayār āhe) - 'The meal is ready'. 16. ये, जेवायला बस (ye, "
  "jevāylā bas) - 'Come, sit down to eat'. 17. आणखी पोळी घेशील का (āṇakhī poḷī "
  "gheśīl kā) - 'Will you take another flatbread'. 18. हॉटेलात जेवण छान होते "
  "(hŏṭelāt jevaṇ chān hote) - 'The food at the restaurant was nice'. 19. बिल "
  "आणा (bil āṇā) - 'Bring the bill'. 20. जेवण खूप चवदार होते (jevaṇ khūp cavdār "
  "hote) - 'The meal was very tasty'."),
 "how_it_works": (
  "This record feeds you in Marathi: the staple foods (वरण-भात, पोळी, भाकरी, "
  "आमटी), cooking verbs in the imperative (चिर, तापव, घाल), and restaurant "
  "language (बिल आणा). Taste vocabulary is precise - गोड, आंबट, तिखट - so "
  "describe every meal you eat for a week using these words."),
 "key_points": [
  "20 sentences: staples (वरण-भात, पोळी, भाकरी, आमटी), cooking verbs, restaurant phrases.",
  "Imperative cooking verbs: चिर (chop), तापव (heat), घाल (put).",
  "Taste words: गोड (sweet), आंबट (sour), तिखट (spicy), चवदार (tasty).",
  "बिल आणा (bil āṇā) - 'Bring the bill' - the key restaurant sentence.",
 ],
 "requirements": [
  "Name ten foods in your kitchen in Marathi.",
  "Give three cooking instructions in Marathi imperatives.",
  "Order a full imaginary meal in Marathi.",
 ],
 "standards": ["Imperative verb forms per standard Marathi grammar (Dhongde & Wali 2009, ch. 6)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens the kitchen is his laboratory of taste: staple "
  "formulas, imperative commands, and the precise vocabulary of flavor - every "
  "meal a repeatable experiment. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 13
{
 "key": "travel", "name": "Marathi Travel and Directions Sentences",
 "group": "Compounded", "ladder": 13, "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Twenty Marathi sentences about transport, asking directions, tickets, and "
  "lodging, each translated. 1. रेल्वे स्टेशन कुठे आहे (relve sṭeśan kuṭhe āhe) "
  "- 'Where is the railway station'. 2. बस स्टॉप जवळ आहे का (bas sṭŏp javaḷ "
  "āhe kā) - 'Is the bus stop nearby'. 3. पुण्याला जाणारी बस कधी आहे (puṇyālā "
  "jāṇārī bas kadhī āhe) - 'When is the bus going to Pune'. 4. तिकीट कितीला आहे "
  "(ṭikīṭ kitīlā āhe) - 'How much is the ticket'. 5. दोन तिकिटे द्या (don "
  "ṭikiṭe dyā) - 'Give two tickets'. 6. गाडी किती वाजता सुटते (gāḍī kitī vājtā "
  "suṭte) - 'At what time does the train leave'. 7. ही गाडी मुंबईला जाते का (hī "
  "gāḍī mumbaīlā jāte kā) - 'Does this train go to Mumbai'. 8. उजवीकडे वळा "
  "(ujvīkaḍe vaḷā) - 'Turn right'. 9. डावीकडे जा (ḍāvīkaḍe jā) - 'Go left'. 10. "
  "सरळ जा (saraḷ jā) - 'Go straight'. 11. किती दूर आहे (kitī dūr āhe) - 'How far "
  "is it'. 12. चालत जाता येईल का (cālat jātā yeīl kā) - 'Can one go walking'. "
  "13. रिक्षाने किती पैसे होतील (rikṣāne kitī paise hotīl) - 'How much will it "
  "cost by rickshaw'. 14. मीटरने चला (mīṭarne calā) - 'Go by the meter'. 15. "
  "हॉटेल कुठे आहे (hŏṭel kuṭhe āhe) - 'Where is the hotel'. 16. खोली उपलब्ध आहे "
  "का (kholī upalabdha āhe kā) - 'Is a room available'. 17. एका रात्रीचे भाडे "
  "किती (ekā rātrīce bhāḍe kitī) - 'What is the rent for one night'. 18. माझे "
  "सामान वर न्या (mājhe sāmān var nyā) - 'Take my luggage upstairs'. 19. सकाळी "
  "सहा वाजता उठवा (sakāḷī sahā vājtā uṭhavā) - 'Wake me at six in the morning'. "
  "20. प्रवास सुखाचा झाला (pravās sukhācā jhālā) - 'The journey was pleasant'."),
 "how_it_works": (
  "This record moves you through Maharashtra in Marathi: stations, buses, "
  "tickets, directions (उजवीकडे, डावीकडे, सरळ), fares, and hotel rooms. The "
  "question pattern कुठे आहे and कितीला आहे unlocks every journey; practice by "
  "planning a real trip and speaking every step in Marathi."),
 "key_points": [
  "20 sentences: stations, tickets, directions, fares, hotel rooms.",
  "Direction words: उजवीकडे (right), डावीकडे (left), सरळ (straight).",
  "Key questions: कुठे आहे (where is), कितीला आहे (how much), कधी आहे (when).",
  "मीटरने चला - 'Go by the meter' - the traveler's shield.",
 ],
 "requirements": [
  "Ask for directions to three real places in Marathi.",
  "Buy an imaginary ticket with full Marathi dialogue.",
  "Book an imaginary hotel room in Marathi.",
 ],
 "standards": ["Interrogative constructions per standard Marathi grammar (Dhongde & Wali 2009, ch. 7)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens travel is his field operation: stations secured, "
  "fares negotiated, directions decoded - every journey a mission brief in "
  "Marathi. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 14
{
 "key": "work", "name": "Marathi Work and School Sentences",
 "group": "Compounded", "ladder": 14, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty Marathi sentences about jobs, the office, the classroom, and learning, "
  "each translated. 1. तू काय काम करतोस (tū kāy kām kartos) - 'What work do you "
  "do'. 2. मी शिक्षक आहे (mī śikṣak āhe) - 'I am a teacher'. 3. ती बँकेत काम "
  "करते (tī bænket kām karte) - 'She works in a bank'. 4. कार्यालय सकाळी नऊ "
  "वाजता उघडते (kāryālay sakāḷī naū vājtā ughaḍte) - 'The office opens at nine in "
  "the morning'. 5. माझी शिफ्ट संध्याकाळी संपते (mājhī śiphṭa sandhyākāḷī sampte) "
  "- 'My shift ends in the evening'. 6. बॉसने मला बोलावले (bŏsne malā bolāvle) - "
  "'The boss called me'. 7. अहवाल उद्या द्या (ahvāl udyā dyā) - 'Give the report "
  "tomorrow'. 8. मीटिंग दहा वाजता आहे (mīṭiṅg dahā vājtā āhe) - 'The meeting is at "
  "ten'. 9. पगार महिन्याच्या शेवटी मिळतो (pagār mahinyācyā śevṭī miḷto) - 'Salary "
  "comes at month end'. 10. सुट्टीसाठी अर्ज करा (suṭṭīsāṭhī arja karā) - 'Apply "
  "for leave'. 11. शाळा सकाळी सात वाजता भरते (śāḷā sakāḷī sāt vājtā bharte) - "
  "'School starts at seven in the morning'. 12. वर्गात चाळीस विद्यार्थी आहेत "
  "(vargāt cāḷīs vidyārthī āhet) - 'There are forty students in the class'. 13. "
  "शिक्षक धडा शिकवतात (śikṣak dhaḍā śikavtāt) - 'The teacher teaches the lesson'. "
  "14. मुलं अभ्यास करतात (mulã abhyās kartāt) - 'The children study'. 15. "
  "परीक्षा पुढच्या महिन्यात आहे (parīkṣā puḍhcyā mahinyāt āhe) - 'The exam is "
  "next month'. 16. गृहपाठ पूर्ण कर (gṛhapāṭh pūrṇa kar) - 'Complete the "
  "homework'. 17. पुस्तक उघडा (pustak ughaḍā) - 'Open the book'. 18. प्रश्न विचारा "
  "(praśna vicārā) - 'Ask a question'. 19. मला गणित आवडते (malā gaṇit āvaḍte) - "
  "'I like mathematics'. 20. शिकणे कधीही थांबत नाही (śikaṇe kadhīhī thāmbat "
  "nāhī) - 'Learning never stops'."),
 "how_it_works": (
  "This record puts Marathi to work: office vocabulary (कार्यालय, अहवाल, मीटिंग, "
  "पगार), classroom vocabulary (वर्ग, धडा, परीक्षा, गृहपाठ), and the verbs "
  "that run both. Notice काम करणे for work and अभ्यास करणे for study. Describe "
  "your own job and school day in Marathi sentences."),
 "key_points": [
  "20 sentences: office (कार्यालय, अहवाल, पगार), classroom (वर्ग, धडा, परीक्षा).",
  "काम करणे (to work) vs अभ्यास करणे (to study) - the two engines of the day.",
  "Time discipline: सकाळी नऊ वाजता, महिन्याच्या शेवटी, पुढच्या महिन्यात.",
  "शिकणे कधीही थांबत नाही - 'Learning never stops'.",
 ],
 "requirements": [
  "Describe your job or studies in five Marathi sentences.",
  "Write a leave application sentence in Marathi.",
  "Say all 20 sentences aloud.",
 ],
 "standards": ["Formal register verb forms per standard Marathi usage (Dhongde & Wali 2009, ch. 6)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens work and school are his two workshops: the "
  "office runs on reports and meetings, the classroom on lessons and exams - "
  "both fueled by शिकणे. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 15
{
 "key": "health", "name": "Marathi Health and Body Sentences",
 "group": "Compounded", "ladder": 15, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty Marathi sentences about body parts, symptoms, the doctor visit, and "
  "the pharmacy, each translated. 1. माझे डोके दुखते (mājhe ḍoke dukhte) - 'My "
  "head aches'. 2. मला ताप आला आहे (malā tāp ālā āhe) - 'I have a fever'. 3. "
  "माझा घसा दुखतो (mājhā ghasā dukhto) - 'My throat hurts'. 4. मला सर्दी झाली "
  "आहे (malā sardī jhālī āhe) - 'I have a cold'. 5. खोकला थांबत नाही (khoklā "
  "thāmbat nāhī) - 'The cough will not stop'. 6. माझ्या पोटात दुखते (mājhyā "
  "poṭāt dukhte) - 'My stomach hurts'. 7. हाताला जखम झाली (hātāla jakham jhālī) "
  "- 'The hand got wounded'. 8. पाय मुरगळला (pāy murgaḷlā) - 'The foot is "
  "sprained'. 9. डोळे लाल झाले आहेत (ḍoḷe lāl jhāle āhet) - 'The eyes have turned "
  "red'. 10. मला चक्कर येते (malā cakkar yete) - 'I feel dizzy'. 11. डॉक्टरकडे "
  "जा (ḍŏkṭarkaḍe jā) - 'Go to the doctor'. 12. दवाखाना कुठे आहे (davākhānā "
  "kuṭhe āhe) - 'Where is the clinic'. 13. मला औषध हवे आहे (malā auṣadh have "
  "āhe) - 'I need medicine'. 14. हे औषध दिवसातून तीन वेळा घ्या (he auṣadh "
  "divsātūn tīn veḷā ghyā) - 'Take this medicine three times a day'. 15. जेवणानंतर "
  "गोळी घ्या (jevaṇāntar goḷī ghyā) - 'Take the pill after meals'. 16. आराम करा "
  "(ārām karā) - 'Take rest'. 17. पाणी जास्त प्या (pāṇī jāst pyā) - 'Drink more "
  "water'. 18. औषध दुकान कुठे आहे (auṣadh dukān kuṭhe āhe) - 'Where is the "
  "pharmacy'. 19. मला ॲलर्जी आहे (malā ælarjī āhe) - 'I have an allergy'. 20. "
  "आता बरे वाटते (ātā bare vāṭte) - 'I feel better now'."),
 "how_it_works": (
  "This record teaches the language of the body and its care: body parts (डोके, "
  "घसा, पोट, हात, पाय, डोळे), symptom patterns (मला ताप आला, माझे डोके दुखते), "
  "and doctor-pharmacy dialogue. The dative experiencer (मला) is the key "
  "pattern - symptoms happen TO you. Practice describing three imaginary "
  "ailments in full Marathi."),
 "key_points": [
  "20 sentences: body parts, symptoms, doctor visit, pharmacy.",
  "Symptom pattern: मला ताप आला (I have a fever), माझे डोके दुखते (my head aches).",
  "Doctor instructions: हे औषध दिवसातून तीन वेळा घ्या - 'Take this medicine three times a day'.",
  "औषध दुकान कुठे आहे - 'Where is the pharmacy'.",
 ],
 "requirements": [
  "Name 15 body parts in Marathi from memory.",
  "Describe two symptoms and ask for medicine in Marathi.",
  "Say all 20 sentences aloud.",
 ],
 "standards": ["Dative experiencer constructions per standard Marathi grammar (Dhongde & Wali 2009, ch. 7)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens the body is his most critical machine: every "
  "part named, every symptom reported in the dative, every dosage a precise "
  "instruction. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 16
{
 "key": "emotions", "name": "Marathi Emotions and Feelings Sentences",
 "group": "Compounded", "ladder": 16, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty Marathi sentences about happiness, sadness, anger, fear, love, and "
  "surprise, each translated. 1. मी खूप आनंदी आहे (mī khūp ānandī āhe) - 'I am "
  "very happy'. 2. बातमी ऐकून आनंद झाला (bātmī aikūn ānand jhālā) - 'Hearing the "
  "news made me happy'. 3. ती दुःखी दिसते (tī duḥkhī diste) - 'She looks sad'. "
  "4. मला वाईट वाटले (malā vāīṭ vāṭle) - 'I felt bad'. 5. तो रागावला (to rāgāvlā) "
  "- 'He got angry'. 6. रागावर नियंत्रण ठेव (rāgāvar niyantraṇ ṭhev) - 'Control "
  "your anger'. 7. मला भीती वाटते (malā bhītī vāṭte) - 'I feel afraid'. 8. अंधारात "
  "भीती वाटली (andhārāt bhītī vāṭlī) - 'I felt scared in the dark'. 9. मी माझ्या "
  "कुटुंबावर प्रेम करतो (mī mājhyā kuṭumbāvar prem karto) - 'I love my family'. "
  "10. प्रेम ही सुंदर भावना आहे (prem hī sundar bhāvnā āhe) - 'Love is a "
  "beautiful feeling'. 11. मला आश्चर्य वाटले (malā āścarya vāṭle) - 'I was "
  "surprised'. 12. हे ऐकून धक्का बसला (he aikūn dhakkā baslā) - 'Hearing this "
  "gave me a shock'. 13. मी उत्साहित आहे (mī utsāhit āhe) - 'I am excited'. 14. "
  "तिला अभिमान वाटतो (tilā abhimān vāṭto) - 'She feels proud'. 15. मला लाज वाटली "
  "(malā lāj vāṭlī) - 'I felt shy'. 16. तो निराश झाला (to nirāś jhālā) - 'He "
  "became disappointed'. 17. आशा सोडू नको (āśā soḍū nako) - 'Do not lose hope'. "
  "18. मला कंटाळा आला (malā kaṇṭāḷā ālā) - 'I got bored'. 19. शांत राहा (śānta "
  "rāhā) - 'Stay calm'. 20. भावना व्यक्त करणे महत्त्वाचे आहे (bhāvnā vyakta "
  "karaṇe mahattvāce āhe) - 'Expressing feelings is important'."),
 "how_it_works": (
  "This record gives feelings their Marathi voice: the वाटणे (to feel) "
  "construction that carries most emotions - मला भीती वाटते, मला आश्चर्य "
  "वाटले - plus the core emotion nouns (आनंद, दुःख, राग, भीती, प्रेम). Say "
  "each sentence with the feeling it names; emotion vocabulary sticks when "
  "the face matches the word."),
 "key_points": [
  "20 sentences across happy, sad, angry, afraid, love, surprise.",
  "वाटणे construction: मला भीती वाटते (I feel afraid), मला आश्चर्य वाटले (I was surprised).",
  "Core nouns: आनंद (joy), दुःख (sorrow), राग (anger), भीती (fear), प्रेम (love).",
  "आशा सोडू नको - 'Do not lose hope'; शांत राहा - 'Stay calm'.",
 ],
 "requirements": [
  "Express six emotions about your own day in Marathi.",
  "Use the वाटणे pattern with five different feelings.",
  "Say all 20 sentences aloud with feeling.",
 ],
 "standards": ["Experiencer predicates with वाटणे per standard Marathi grammar (Dhongde & Wali 2009, ch. 7)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens emotions are his inner weather system: आनंद "
  "sunshine, राग thunder, प्रेम the climate itself - every state reported "
  "through वाटणे. Signature-made teaching, clearly labeled, never presented as "
  "an outside authority's text."),
},
# ================================================================== 17
{
 "key": "nature", "name": "Marathi Nature and Weather Sentences",
 "group": "Compounded", "ladder": 17, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Twenty Marathi sentences about animals, plants, seasons, and weather talk, "
  "each translated. 1. आज हवामान छान आहे (āj havāmān chān āhe) - 'The weather "
  "is nice today'. 2. पाऊस पडतोय (pāūs paḍtoy) - 'It is raining'. 3. ऊन कडक आहे "
  "(ūn kaḍak āhe) - 'The sun is harsh'. 4. वारा वाहतोय (vārā vāhtoy) - 'The "
  "wind is blowing'. 5. आकाशात ढग आहेत (ākāśāt ḍhag āhet) - 'There are clouds in "
  "the sky'. 6. हिवाळ्यात थंडी पडते (hivāḷyāt thaṇḍī paḍte) - 'It gets cold in "
  "winter'. 7. उन्हाळ्यात आंबे येतात (unhāḷyāt āmbe yetāt) - 'Mangoes come in "
  "summer'. 8. झाडावर पक्षी बसले आहेत (jhāḍāvar pakṣī basle āhet) - 'Birds are "
  "sitting on the tree'. 9. मोर सुंदर दिसतो (mor sundar disto) - 'The peacock "
  "looks beautiful'. 10. वाघ जंगलात राहतो (vāgh jaṅglāt rāhto) - 'The tiger "
  "lives in the forest'. 11. हत्ती मोठा प्राणी आहे (hattī moṭhā prāṇī āhe) - "
  "'The elephant is a big animal'. 12. गाय दूध देते (gāy dūdh dete) - 'The cow "
  "gives milk'. 13. कुत्रा भुंकतो (kutrā bhuṅkto) - 'The dog barks'. 14. मांजर "
  "दूध पिते (māñjar dūdh pite) - 'The cat drinks milk'. 15. फुलं फुलली आहेत "
  "(phulã phullī āhet) - 'The flowers have bloomed'. 16. बागेत गुलाब आहेत "
  "(bāget gulāb āhet) - 'There are roses in the garden'. 17. नदीत पाणी भरपूर आहे "
  "(nadīt pāṇī bharpūr āhe) - 'There is plenty of water in the river'. 18. डोंगर "
  "उंच आहे (ḍoṅgar uñc āhe) - 'The mountain is high'. 19. समुद्र निळा दिसतो "
  "(samudra niḷā disto) - 'The sea looks blue'. 20. निसर्गाचे रक्षण करा "
  "(nisargāce rakṣaṇ karā) - 'Protect nature'."),
 "how_it_works": (
  "This record takes you outside in Marathi: weather verbs (पाऊस पडतो, वारा "
  "वाहतो), the three seasons in action, animals of field and forest, and plants "
  "in bloom. Weather is the universal small talk - master आज हवामान छान आहे and "
  "you can open a conversation with anyone, anywhere in Maharashtra."),
 "key_points": [
  "20 sentences: weather, seasons, animals, plants.",
  "Weather verbs: पाऊस पडतो (it rains), वारा वाहतो (wind blows), थंडी पडते (it gets cold).",
  "Animals: वाघ (tiger), हत्ती (elephant), मोर (peacock), गाय (cow).",
  "निसर्गाचे रक्षण करा - 'Protect nature'.",
 ],
 "requirements": [
  "Describe today's weather in three Marathi sentences.",
  "Name ten animals and five plants in Marathi.",
  "Say all 20 sentences aloud.",
 ],
 "standards": ["Impersonal weather constructions per standard Marathi usage (Dhongde & Wali 2009)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens nature is his open-air laboratory: weather "
  "readings, animal specimens, blooming data points - every sentence a field "
  "note. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 18
{
 "key": "shopping", "name": "Marathi Shopping and Money Sentences",
 "group": "Compounded", "ladder": 18, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Twenty Marathi sentences about the market, prices, bargaining, and paying, "
  "each translated. 1. हे कितीला आहे (he kitīlā āhe) - 'How much is this'. 2. "
  "भाव जास्त आहे (bhāv jāst āhe) - 'The price is too high'. 3. थोडे कमी करा "
  "(thoḍe kamī karā) - 'Reduce it a little'. 4. शेवटचा भाव सांगा (śevṭacā bhāv "
  "sāṅgā) - 'Tell me the final price'. 5. हे मला घ्यायचे आहे (he malā ghyāyce "
  "āhe) - 'I want to buy this'. 6. दुसरा रंग दाखवा (dusrā raṅg dākhavā) - 'Show "
  "me another color'. 7. मोठा आकार आहे का (moṭhā ākār āhe kā) - 'Is there a "
  "bigger size'. 8. भाजी ताजी आहे का (bhājī tājī āhe kā) - 'Are the vegetables "
  "fresh'. 9. एक किलो टोमॅटो द्या (ek kilo ṭomæṭo dyā) - 'Give one kilo of "
  "tomatoes'. 10. अर्धा किलो साखर घ्या (ardhā kilo sākhar ghyā) - 'Take half a "
  "kilo of sugar'. 11. सूट आहे का (sūṭ āhe kā) - 'Is there a discount'. 12. "
  "पैसे सुटे आहेत का (paise suṭe āhet kā) - 'Do you have change'. 13. कार्डने "
  "पैसे देऊ शकतो का (kārḍne paise deū śakto kā) - 'Can I pay by card'. 14. रोख "
  "पैसे द्या (rokh paise dyā) - 'Pay in cash'. 15. पावती द्या (pāvtī dyā) - 'Give "
  "the receipt'. 16. पिशवी द्या (piśvī dyā) - 'Give a bag'. 17. उद्या परत येईन "
  "(udyā parat yeīn) - 'I will come again tomorrow'. 18. दुकान कधी बंद होते "
  "(dukān kadhī band hote) - 'When does the shop close'. 19. बाजार स्वस्त आहे "
  "(bājār svast āhe) - 'The market is cheap'. 20. खरेदी छान झाली (kharedī chān "
  "jhālī) - 'The shopping went well'."),
 "how_it_works": (
  "This record makes you a Marathi bargainer: the price question (कितीला), the "
  "bargaining moves (थोडे कमी करा, शेवटचा भाव सांगा), quantities (किलो, अर्धा), "
  "and payment (रोख, कार्डने, पावती). Role-play buyer and seller until the "
  "whole transaction flows without thinking."),
 "key_points": [
  "20 sentences: prices, bargaining, quantities, payment.",
  "Bargaining sequence: कितीला आहे - भाव जास्त आहे - थोडे कमी करा - शेवटचा भाव सांगा.",
  "Quantities: एक किलो, अर्धा किलो; payment: रोख (cash), कार्डने (by card), पावती (receipt).",
  "पैसे सुटे आहेत का - 'Do you have change'.",
 ],
 "requirements": [
  "Role-play a full market purchase in Marathi.",
  "Bargain a price down in three Marathi moves.",
  "Say all 20 sentences aloud.",
 ],
 "standards": ["Commercial transaction vocabulary per standard Marathi usage (Molesworth 1857)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens the market is his trading floor: every price a "
  "negotiation, every discount a victory, every receipt a closed deal. "
  "Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 19
{
 "key": "friendship", "name": "Marathi Friendship and Social Life Sentences",
 "group": "Compounded", "ladder": 19, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Twenty Marathi sentences about meeting people, invitations, and celebrations, "
  "each translated. 1. हा माझा मित्र आहे (hā mājhā mitra āhe) - 'This is my "
  "friend'. 2. आमची मैत्री जुनी आहे (āmcī maitrī junī āhe) - 'Our friendship is "
  "old'. 3. तुझ्याशी बोलून छान वाटले (tujhyāśī bolūn chān vāṭle) - 'It was nice "
  "talking to you'. 4. उद्या घरी ये (udyā gharī ye) - 'Come home tomorrow'. 5. "
  "चहा घेशील का (cahā gheśīl kā) - 'Will you have tea'. 6. जेवायला ये (jevāylā "
  "ye) - 'Come for a meal'. 7. वाढदिवसाच्या शुभेच्छा (vāḍhadivasācyā śubhecchā) "
  "- 'Happy birthday'. 8. लग्नाला नक्की ये (lagnālā nakkī ye) - 'Do come to the "
  "wedding'. 9. दिवाळीच्या शुभेच्छा (divāḷīcyā śubhecchā) - 'Happy Diwali'. 10. "
  "गणपती बाप्पा मोरया (gaṇpatī bāppā moryā) - 'Hail Lord Ganesha' - the "
  "Ganesh-festival cheer. 11. सणाला घरी या (saṇālā gharī yā) - 'Come home for "
  "the festival'. 12. आपण भेटूया (āpaṇ bheṭūyā) - 'Let us meet'. 13. फोन कर "
  "(phon kar) - 'Call me'. 14. मेसेज कर (mesej kar) - 'Send a message'. 15. "
  "तुझी आठवण येते (tujhī āṭhvaṇ yete) - 'I miss you'. 16. मित्रांसोबत वेळ छान "
  "जातो (mitrānsobat veḷ chān jāto) - 'Time passes nicely with friends'. 17. "
  "पार्टी कधी आहे (pārṭī kadhī āhe) - 'When is the party'. 18. मी नक्की येईन "
  "(mī nakkī yeīn) - 'I will definitely come'. 19. खूप मजा आली (khūp majā ālī) "
  "- 'Had a lot of fun'. 20. मैत्री हेच खरे धन आहे (maitrī hec khare dhan āhe) "
  "- 'Friendship itself is the true wealth'."),
 "how_it_works": (
  "This record opens your social life in Marathi: introductions, invitations "
  "(ये, जेवायला ये), festival wishes (वाढदिवसाच्या शुभेच्छा, दिवाळीच्या "
  "शुभेच्छा), and the warmth of मैत्री. Marathi hospitality is direct - "
  "चहा घेशील का is never just about tea. Invite three real people to three "
  "real things in Marathi this week."),
 "key_points": [
  "20 sentences: introductions, invitations, festival wishes, friendship.",
  "Invitations: ये (come), जेवायला ये (come for a meal), चहा घेशील का (will you have tea).",
  "Festival cheers: गणपती बाप्पा मोरया; wishes: वाढदिवसाच्या शुभेच्छा.",
  "तुझी आठवण येते - 'I miss you' - literally 'your memory comes'.",
 ],
 "requirements": [
  "Introduce a friend in Marathi.",
  "Invite someone to tea and to a meal in Marathi.",
  "Say all 20 sentences aloud warmly.",
 ],
 "standards": ["Festival and social formulae per standard Marathi usage (Dhongde & Wali 2009, ch. 1)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens friendship is his alliance network: introductions "
  "as handshakes, invitations as summits, festivals as grand assemblies - "
  "मैत्री the true wealth. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 20
{
 "key": "tech", "name": "Marathi Technology and Communication Sentences",
 "group": "Compounded", "ladder": 20, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Twenty Marathi sentences about the phone, internet, computer, and messaging, "
  "each translated. 1. माझा फोन कुठे आहे (mājhā phon kuṭhe āhe) - 'Where is my "
  "phone'. 2. फोन वाजतोय (phon vājtoy) - 'The phone is ringing'. 3. फोन उचल "
  "(phon ucal) - 'Pick up the phone'. 4. मला फोन कर (malā phon kar) - 'Call "
  "me'. 5. नेटवर्क नाहीये (neṭvark nāhīye) - 'There is no network'. 6. बॅटरी "
  "संपली (bæṭarī samplī) - 'The battery died'. 7. चार्जर आहे का (cārjar āhe kā) "
  "- 'Do you have a charger'. 8. इंटरनेट चालते का (iṇṭarneṭ cālte kā) - 'Is the "
  "internet working'. 9. वायफाय पासवर्ड काय आहे (vāyphāy pāsvard kāy āhe) - "
  "'What is the wifi password'. 10. मेसेज पाठव (mesej pāṭhav) - 'Send a message'. "
  "11. ईमेल लिहिला का (īmel lihilā kā) - 'Did you write the email'. 12. फोटो "
  "पाठव (phoṭo pāṭhav) - 'Send the photo'. 13. व्हिडिओ कॉल करूया (vhiḍio kŏl "
  "karūyā) - 'Let us do a video call'. 14. संगणक चालू कर (saṅgaṇak cālū kar) - "
  "'Turn on the computer'. 15. फाईल सेव्ह कर (phāīl sevh kar) - 'Save the file'. "
  "16. प्रिंट काढ (priṇṭ kāḍh) - 'Take a printout'. 17. ॲप डाउनलोड कर (æp "
  "ḍāunloḍ kar) - 'Download the app'. 18. पासवर्ड बदल (pāsvard badal) - 'Change "
  "the password'. 19. स्क्रीनवर बघ (skrīnavar bagh) - 'Look at the screen'. 20. "
  "तंत्रज्ञानाने जग जवळ आले (tantradnyānāne jag javaḷ āle) - 'Technology has "
  "brought the world closer'."),
 "how_it_works": (
  "This record wires you into the digital world in Marathi: phones, networks, "
  "messages, computers - with the Marathi verbs that run them (कर, पाठव, उचल, "
  "बदल). Technology words are mostly English loans written in Devanagari - "
  "फोन, इंटरनेट, ईमेल - so the skill is in the verbs around them. Narrate your "
  "next hour of phone use entirely in Marathi."),
 "key_points": [
  "20 sentences: phone, internet, computer, messaging.",
  "Tech nouns are English loans in Devanagari: फोन, इंटरनेट, ईमेल, पासवर्ड.",
  "Command verbs: उचल (pick up), पाठव (send), कर (do), बदल (change).",
  "वायफाय पासवर्ड काय आहे - the modern traveler's first question.",
 ],
 "requirements": [
  "Narrate your phone use for one hour in Marathi.",
  "Send a real message using three sentences from this record.",
  "Say all 20 sentences aloud.",
 ],
 "standards": ["Loanword adaptation in Devanagari per standard Marathi orthography (Dhongde & Wali 2009, ch. 2)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens technology is his extended nervous system: every "
  "device a sense organ, every message a nerve impulse - all commanded in "
  "Marathi. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 21
{
 "key": "tenses", "name": "Marathi Verb Tenses in Sentences",
 "group": "Advanced", "ladder": 21, "ladder_rank": 7, "ladder_tier": "advanced",
 "description": (
  "Marathi verb tenses with five or more translated sentences per tense. "
  "PRESENT (habitual, -तो/-ते/-तं): 1. मी रोज शाळेत जातो (mī roj śāḷet jāto) - "
  "'I go to school daily'. 2. ती गाणे गाते (tī gāṇe gāte) - 'She sings a song'. "
  "3. ते झाड वाढते (te jhāḍ vāḍhte) - 'The tree grows'. 4. आम्ही मराठी शिकतो "
  "(āmhī marāṭhī śikto) - 'We learn Marathi'. 5. पक्षी आकाशात उडतात (pakṣī "
  "ākāśāt uḍtāt) - 'Birds fly in the sky'. 6. सूर्य पूर्वेला उगवतो (sūrya "
  "pūrvelā ugavto) - 'The sun rises in the east'. PRESENT CONTINUOUS (राहिला "
  "with -त): 1. मी जेवत आहे (mī jevat āhe) - 'I am eating'. 2. ती अभ्यास करत "
  "आहे (tī abhyās karat āhe) - 'She is studying'. 3. ते खेळत आहेत (te kheḷat "
  "āhet) - 'They are playing'. 4. पाऊस पडत आहे (pāūs paḍat āhe) - 'It is "
  "raining'. 5. मी तुला बघत आहे (mī tulā baghat āhe) - 'I am looking at you'. "
  "PAST (simple, -ल-): 1. मी काल बाजारात गेलो (mī kāl bājārāt gelo) - 'I went "
  "to the market yesterday'. 2. तिने पत्र लिहिले (tine patra lihile) - 'She "
  "wrote a letter'. 3. त्याने आंबा खाल्ला (tyāne āmbā khāllā) - 'He ate the "
  "mango'. 4. आम्ही चित्रपट पाहिला (āmhī citrapaṭ pāhilā) - 'We watched the "
  "movie'. 5. पाऊस पडला (pāūs paḍlā) - 'It rained'. 6. ती आली नाही (tī ālī "
  "nāhī) - 'She did not come'. FUTURE (-ईल/-शील/-णार): 1. मी उद्या येईन (mī "
  "udyā yeīn) - 'I will come tomorrow'. 2. तू जाशील का (tū jāśīl kā) - 'Will "
  "you go'. 3. तो पुस्तक वाचेल (to pustak vācel) - 'He will read the book'. 4. "
  "आम्ही जाऊ (āmhī jāū) - 'We shall go'. 5. पाऊस पडेल (pāūs paḍel) - 'It will "
  "rain'. 6. ती गाणार आहे (tī gāṇār āhe) - 'She is going to sing'. IMPERATIVE: "
  "1. ये (ye) - 'Come (informal)'. 2. बसा (basā) - 'Sit (formal)'. 3. पुस्तक वाच "
  "(pustak vāc) - 'Read the book'. 4. शांत राहा (śānta rāhā) - 'Stay calm "
  "(formal)'. 5. प्रयत्न कर (prayatna kar) - 'Try'. SUBJUNCTIVE/OPTATIVE (-ावा/"
  "-ू): 1. आपण जाऊया (āpaṇ jāūyā) - 'Let us go'. 2. देव करो (dev karo) - 'May "
  "God grant'. 3. तो यावा (to yāvā) - 'He should come'."),
 "how_it_works": (
  "This record is the time machine: present, present continuous, past, future, "
  "imperative, and optative - each with its endings and its sentence family. "
  "Watch how the verb agrees with gender in the present (जातो/जाते/जातं) and "
  "with the object in the ergative past (खाल्ला/खाल्ली). Tell one day of your "
  "life three times: what you do, what you did, what you will do."),
 "key_points": [
  "Present -तो/-ते/-तं; continuous -त आहे; past -ल-; future -ईल/-णार; imperative; optative -ावा.",
  "मी रोज शाळेत जातो - 'I go to school daily'; मी काल बाजारात गेलो - 'I went yesterday'.",
  "Ergative past: त्याने आंबा खाल्ला - verb agrees with the object.",
  "मी उद्या येईन - 'I will come tomorrow'; आपण जाऊया - 'Let us go'.",
 ],
 "requirements": [
  "Tell your yesterday, today, and tomorrow in Marathi.",
  "Conjugate जाणे fully: present, past, future, imperative.",
  "Say all sentences aloud.",
 ],
 "standards": ["Tense-aspect-mood system per standard Marathi grammar (Dhongde & Wali 2009, ch. 6)."],
 "citations": [CIT_DW, CIT_MASICA],
 "sig_lens": (
  "Through the Signature lens tenses are his time controls: -तो for the "
  "eternal present, -ल- for the recorded past, -ईल for the projected future - "
  "every ending a dial he turns. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 22
{
 "key": "qa", "name": "Marathi Questions and Answers",
 "group": "Advanced", "ladder": 22, "ladder_rank": 7, "ladder_tier": "advanced",
 "description": (
  "Twenty Marathi question-and-answer pairs covering who, what, where, when, "
  "why, and how. 1. Q: तुझे नाव काय आहे (tujhe nāv kāy āhe) - 'What is your "
  "name'. A: माझे नाव राहुल आहे (mājhe nāv rāhul āhe) - 'My name is Rahul'. 2. "
  "Q: तू कुठे राहतोस (tū kuṭhe rāhtos) - 'Where do you live'. A: मी पुण्यात "
  "राहतो (mī puṇyāt rāhto) - 'I live in Pune'. 3. Q: तू काय करतोस (tū kāy "
  "kartos) - 'What do you do'. A: मी विद्यार्थी आहे (mī vidyārthī āhe) - 'I am "
  "a student'. 4. Q: तू कधी येशील (tū kadhī yeśīl) - 'When will you come'. A: "
  "मी उद्या येईन (mī udyā yeīn) - 'I will come tomorrow'. 5. Q: तू का हसतोस "
  "(tū kā hastos) - 'Why are you laughing'. A: गोष्ट गंमतीशीर आहे (goṣṭa "
  "gammatīśīr āhe) - 'The story is funny'. 6. Q: तू कसा आहेस (tū kasā āhes) - "
  "'How are you'. A: मी ठीक आहे (mī ṭhīk āhe) - 'I am fine'. 7. Q: कोण आले "
  "(koṇ āle) - 'Who came'. A: माझा मित्र आला (mājhā mitra ālā) - 'My friend "
  "came'. 8. Q: हे काय आहे (he kāy āhe) - 'What is this'. A: हे पुस्तक आहे (he "
  "pustak āhe) - 'This is a book'. 9. Q: किती वाजले (kitī vājle) - 'What time "
  "is it'. A: पाच वाजले (pāc vājle) - 'It is five'. 10. Q: किती पैसे (kitī "
  "paise) - 'How much money'. A: शंभर रुपये (śambhar rupaye) - 'Hundred rupees'. "
  "11. Q: तू मराठी बोलतोस का (tū marāṭhī boltos kā) - 'Do you speak Marathi'. "
  "A: हो, थोडे बोलतो (ho, thoḍe bolto) - 'Yes, I speak a little'. 12. Q: शाळा "
  "कुठे आहे (śāḷā kuṭhe āhe) - 'Where is the school'. A: शाळा जवळ आहे (śāḷā "
  "javaḷ āhe) - 'The school is nearby'. 13. Q: जेवण तयार आहे का (jevaṇ tayār "
  "āhe kā) - 'Is the meal ready'. A: हो, तयार आहे (ho, tayār āhe) - 'Yes, it is "
  "ready'. 14. Q: तुला चहा आवडतो का (tulā cahā āvaḍto kā) - 'Do you like tea'. "
  "A: हो, खूप आवडतो (ho, khūp āvaḍto) - 'Yes, I like it very much'. 15. Q: "
  "तुझा वाढदिवस कधी आहे (tujhā vāḍhadivas kadhī āhe) - 'When is your birthday'. "
  "A: माझा वाढदिवस जूनमध्ये आहे (mājhā vāḍhadivas jūnmadhye āhe) - 'My birthday "
  "is in June'. 16. Q: तू काल कुठे होतास (tū kāl kuṭhe hotās) - 'Where were you "
  "yesterday'. A: मी घरी होतो (mī gharī hoto) - 'I was at home'. 17. Q: हे "
  "पुस्तक कोणाचे आहे (he pustak koṇāce āhe) - 'Whose book is this'. A: हे माझे "
  "आहे (he mājhe āhe) - 'It is mine'. 18. Q: तू कसे येशील (tū kase yeśīl) - "
  "'How will you come'. A: मी बसने येईन (mī basne yeīn) - 'I will come by bus'. "
  "19. Q: तुला भूक लागली का (tulā bhūk lāglī kā) - 'Are you hungry'. A: हो, खूप "
  "भूक लागली (ho, khūp bhūk lāglī) - 'Yes, very hungry'. 20. Q: आपण भेटूया का "
  "(āpaṇ bheṭūyā kā) - 'Shall we meet'. A: हो, नक्की भेटूया (ho, nakkī "
  "bheṭūyā) - 'Yes, let us definitely meet'."),
 "how_it_works": (
  "This record is conversation boot camp: twenty real exchanges covering every "
  "question word - कोण, काय, कुठे, कधी, का, कसा, किती - plus yes/no questions "
  "with का. Notice answers mirror the question's verb. Practice with a partner: "
  "one asks, one answers, then swap - until the pairs fire automatically."),
 "key_points": [
  "20 Q/A pairs covering who, what, where, when, why, how, how much.",
  "Question words stay in place: तू कुठे राहतोस - 'Where do you live'.",
  "Yes/no questions add का: तू मराठी बोलतोस का - 'Do you speak Marathi'.",
  "Answers mirror the question verb: कधी येशील / उद्या येईन.",
 ],
 "requirements": [
  "Answer all 20 questions about yourself in Marathi.",
  "Ask a partner five questions and answer five.",
  "Say all 40 lines aloud.",
 ],
 "standards": ["Interrogative syntax per standard Marathi grammar (Dhongde & Wali 2009, ch. 7)."],
 "citations": [CIT_DW, CIT_MASICA],
 "sig_lens": (
  "Through the Signature lens questions are his sonar pings and answers the "
  "echoes: every कोण, काय, कुठे a pulse sent out, every answer the world "
  "answering back. Signature-made teaching, clearly labeled, never presented "
  "as an outside authority's text."),
},
# ================================================================== 23
{
 "key": "commands", "name": "Marathi Commands and Requests",
 "group": "Advanced", "ladder": 23, "ladder_rank": 7, "ladder_tier": "advanced",
 "description": (
  "Twenty Marathi imperative and polite-request sentences, formal versus "
  "informal. Informal (तू): 1. ये (ye) - 'Come'. 2. जा (jā) - 'Go'. 3. बस (bas) "
  "- 'Sit'. 4. खा (khā) - 'Eat'. 5. पी (pī) - 'Drink'. 6. बघ (bagh) - 'Look'. "
  "7. ऐक (aik) - 'Listen'. 8. बोल (bol) - 'Speak'. 9. लिहि (lihi) - 'Write'. "
  "10. थांब (thāmb) - 'Stop'. Formal/plural (तुम्ही): 11. या (yā) - 'Come "
  "(formal)'. 12. बसा (basā) - 'Sit (formal)'. 13. सांगा (sāṅgā) - 'Tell "
  "(formal)'. 14. द्या (dyā) - 'Give (formal)'. 15. घ्या (ghyā) - 'Take "
  "(formal)'. 16. कृपया शांत बसा (kṛpayā śānta basā) - 'Please sit quietly'. "
  "17. मला मदत करा (malā madat karā) - 'Help me'. 18. दरवाजा बंद करा (darvājā "
  "band karā) - 'Close the door'. 19. थोडे थांबा (thoḍe thāmbā) - 'Wait a "
  "little'. 20. नक्की या (nakkī yā) - 'Do come'. Polite softeners: कृपया "
  "(kṛpayā) - 'please' before any command; जरा (jarā) - 'a little/just' to "
  "soften: जरा बघा (jarā baghā) - 'Just have a look'. Negative commands use "
  "नको/नका: जाऊ नको (jāū nako) - 'Do not go (informal)'; काळजी करू नका (kāḷjī "
  "karū nakā) - 'Do not worry (formal)'. The formal imperative usually adds -ा "
  "to the stem: ये/या, बस/बसा, दे/द्या."),
 "how_it_works": (
  "This record teaches command and courtesy: the bare stem for तू, the -ा "
  "form for तुम्ही, कृपया and जरा as softeners, and नको/नका for prohibitions. "
  "The rule of thumb: command friends with the stem, command the world with "
  "-ा. Practice by giving your room ten orders, then rephrasing each politely."),
 "key_points": [
  "20 imperatives: informal stem (ये, जा, बस) vs formal -ा form (या, बसा, द्या).",
  "Softeners: कृपया (please), जरा (just/a little): जरा बघा.",
  "Prohibitions: नको (informal), नका (formal): जाऊ नको / काळजी करू नका.",
  "मला मदत करा - 'Help me' - the most useful formal request.",
 ],
 "requirements": [
  "Give ten commands to a friend (informal) and ten to an elder (formal).",
  "Soften five commands with कृपया and जरा.",
  "Say all 20 sentences aloud.",
 ],
 "standards": ["Imperative and prohibitive forms per standard Marathi grammar (Dhongde & Wali 2009, ch. 6)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens commands are his orders of the day: the bare "
  "stem for the inner circle, the -ा form for the parade ground, कृपया the "
  "diplomat's seal. Signature-made teaching, clearly labeled, never presented "
  "as an outside authority's text."),
},
# ================================================================== 24
{
 "key": "descriptions", "name": "Marathi Descriptions of People and Places",
 "group": "Advanced", "ladder": 24, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Twenty Marathi sentences describing people, places, and things in detail, "
  "each translated. 1. माझा मित्र उंच आणि हुशार आहे (mājhā mitra uñc āṇi huśār "
  "āhe) - 'My friend is tall and clever'. 2. तिचे डोळे काळे आहेत (tice ḍoḷe "
  "kāḷe āhet) - 'Her eyes are black'. 3. त्याचे केस पांढरे झाले आहेत (tyāce "
  "kes pāndhare jhāle āhet) - 'His hair has turned white'. 4. आजी दयाळू आहे "
  "(ājī dayāḷū āhe) - 'Grandmother is kind'. 5. लहान मुलगी गोड हसते (lahān "
  "mulgī goḍ haste) - 'The little girl smiles sweetly'. 6. पुणे हे शिक्षणाचे "
  "शहर आहे (puṇe he śikṣaṇāce śahar āhe) - 'Pune is a city of education'. 7. "
  "मुंबई समुद्रकिनारी वसलेले मोठे शहर आहे (mumbaī samudrakinārī vaslele moṭhe "
  "śahar āhe) - 'Mumbai is a big city situated on the seashore'. 8. माझे गाव "
  "हिरवेगार आहे (mājhe gāv hirvegār āhe) - 'My village is lush green'. 9. "
  "सह्याद्रीचे डोंगर उंच आहेत (sahyādrīce ḍoṅgar uñc āhet) - 'The Sahyadri "
  "mountains are high'. 10. कोकणचा समुद्रकिनारा सुंदर आहे (kokaṇcā "
  "samudrakinārā sundar āhe) - 'The Konkan coastline is beautiful'. 11. हे घर "
  "जुने पण मजबूत आहे (he ghar june paṇ majbūt āhe) - 'This house is old but "
  "strong'. 12. खोली स्वच्छ आणि हवेशीर आहे (kholī svaccha āṇi haveśīr āhe) - "
  "'The room is clean and airy'. 13. बाजार गजबजलेला आहे (bājār gajbajlelā "
  "āhe) - 'The market is bustling'. 14. रस्ता रुंद आणि स्वच्छ आहे (rastā rund "
  "āṇi svaccha āhe) - 'The road is wide and clean'. 15. आंब्याचा वास गोड आहे "
  "(āmbyācā vās goḍ āhe) - 'The mango smells sweet'. 16. चहा गरम आणि गोड आहे "
  "(cahā garam āṇi goḍ āhe) - 'The tea is hot and sweet'. 17. पावसाळ्यात धबधबा "
  "प्रचंड दिसतो (pāvsāḷyāt dhabdhabā pracaṇḍa disto) - 'The waterfall looks "
  "mighty in the monsoon'. 18. सकाळची हवा ताजी असते (sakāḷcī havā tājī aste) - "
  "'The morning air is fresh'. 19. रात्रीचे आकाश ताऱ्यांनी भरलेले असते "
  "(rātrīce ākāś tāryānnī bharlele aste) - 'The night sky is full of stars'. "
  "20. महाराष्ट्र हा संतांची भूमी आहे (mahārāṣṭra hā santāñcī bhūmī āhe) - "
  "'Maharashtra is the land of saints'."),
 "how_it_works": (
  "This record paints in Marathi: people described feature by feature, places "
  "described in sweeping sentences, with adjectives agreeing at every step "
  "(उंच/हुशार, काळे डोळे, हिरवेगार गाव). The pattern is noun + adjectives + "
  "आहे/असते. Describe five people and five places you know, each in two full "
  "Marathi sentences."),
 "key_points": [
  "20 detailed descriptive sentences: people, places, things.",
  "Agreement everywhere: तिचे डोळे काळे आहेत (her eyes are black).",
  "Place pride: पुणे हे शिक्षणाचे शहर आहे; महाराष्ट्र हा संतांची भूमी आहे.",
  "Sensory detail: वास (smell), दिसतो (looks), हवा (air).",
 ],
 "requirements": [
  "Describe three people and three places in two sentences each.",
  "Use five senses words in Marathi descriptions.",
  "Say all 20 sentences aloud.",
 ],
 "standards": ["Attributive and predicative adjective agreement per standard Marathi grammar (Dhongde & Wali 2009, ch. 5)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens description is his portrait studio: every "
  "person a study, every place a landscape, every adjective a brushstroke "
  "matched to its noun. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 25
{
 "key": "story1", "name": "Marathi Short Story I: A Simple Day",
 "group": "Advanced", "ladder": 25, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "A ten-sentence simple Marathi story, line by line with English translation. "
  "Title: एक साधा दिवस (ek sādhā divas) - 'A Simple Day'. 1. सकाळी रवी लवकर "
  "उठतो (sakāḷī ravī lavkar uṭhto) - 'In the morning Ravi wakes up early'. 2. "
  "तो आंघोळ करतो आणि नाश्ता करतो (to āṅghoḷ karto āṇi nāśtā karto) - 'He bathes "
  "and eats breakfast'. 3. नाश्त्यात तो पोहे खातो (nāśtyāt to pohe khāto) - "
  "'For breakfast he eats poha'. 4. मग तो शाळेत जातो (mag to śāḷet jāto) - "
  "'Then he goes to school'. 5. शाळेत तो मित्रांना भेटतो (śāḷet to mitrānnā "
  "bheṭto) - 'At school he meets his friends'. 6. दुपारी ते मैदानात खेळतात "
  "(dupārī te maidānāt kheḷtāt) - 'In the afternoon they play in the field'. "
  "7. संध्याकाळी तो घरी परततो (sandhyākāḷī to gharī partato) - 'In the evening "
  "he returns home'. 8. घरी आई त्याच्यासाठी जेवण बनवते (gharī āī tyācyāsāṭhī "
  "jevaṇ banavte) - 'At home mother cooks dinner for him'. 9. जेवणानंतर तो "
  "अभ्यास करतो (jevaṇāntar to abhyās karto) - 'After dinner he studies'. 10. "
  "रात्री तो लवकर झोपतो (rātrī to lavkar jhopto) - 'At night he sleeps early'. "
  "The story uses only present-tense verbs and everyday vocabulary from "
  "records 4-20; every word has appeared before."),
 "how_it_works": (
  "This record proves you can read a whole story: ten simple sentences, "
  "present tense only, built entirely from words you already know. Read the "
  "Marathi line first and guess the meaning before checking the English. Then "
  "retell Ravi's day in your own Marathi words - that retelling is the real "
  "test."),
 "key_points": [
  "10-sentence story, present tense, everyday vocabulary - line-by-line translation.",
  "Title: एक साधा दिवस (ek sādhā divas) - 'A Simple Day'.",
  "Time adverbs carry the story: सकाळी, दुपारी, संध्याकाळी, रात्री.",
  "Every word appeared in records 4-20 - nothing new, only new combinations.",
 ],
 "requirements": [
  "Read the story aloud three times without the English.",
  "Retell Ravi's day in your own Marathi sentences.",
  "Write your own ten-sentence day story.",
 ],
 "standards": ["Narrative present tense per standard Marathi usage (Dhongde & Wali 2009, ch. 6)."],
 "citations": [CIT_DW, CIT_MASICA],
 "sig_lens": (
  "Through the Signature lens this story is his first broadcast: one ordinary "
  "day, ten clean sentences, zero unknown words - proof the instrument plays. "
  "Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 26
{
 "key": "story2", "name": "Marathi Short Story II: The Journey (Past Tense)",
 "group": "Advanced", "ladder": 26, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "A ten-sentence Marathi story in the past tense, line by line with English "
  "translation. Title: प्रवास (pravās) - 'The Journey'. 1. गेल्या वर्षी आम्ही "
  "कोकणात गेलो (gelyā varṣī āmhī kokaṇāt gelo) - 'Last year we went to the "
  "Konkan'. 2. आम्ही सकाळी लवकर निघालो (āmhī sakāḷī lavkar nighālo) - 'We left "
  "early in the morning'. 3. रस्ता हिरवा आणि सुंदर होता (rastā hirvā āṇi "
  "sundar hotā) - 'The road was green and beautiful'. 4. वाटेत आम्ही आंबे "
  "खाल्ले (vāṭet āmhī āmbe khālle) - 'On the way we ate mangoes'. 5. दुपारी "
  "आम्ही समुद्रकिनारी पोहोचलो (dupārī āmhī samudrakinārī pohochlo) - 'In the "
  "afternoon we reached the beach'. 6. लाटा मोठ्या होत्या (lāṭā moṭhyā hotyā) "
  "- 'The waves were big'. 7. मुलं पाण्यात खेळली (mulã pāṇyāt kheḷlī) - 'The "
  "children played in the water'. 8. संध्याकाळी आम्ही मासे खाल्ले (sandhyākāḷī "
  "āmhī māse khālle) - 'In the evening we ate fish'. 9. रात्री आम्ही गाणी "
  "गायली (rātrī āmhī gāṇī gāylī) - 'At night we sang songs'. 10. तो प्रवास आम्ही "
  "कधीही विसरणार नाही (to pravās āmhī kadhīhī visraṇār nāhī) - 'We will never "
  "forget that journey'. The story shows the ergative past (आम्ही आंबे खाल्ले - "
  "verb agrees with आंबे) and past of असणे (होता/होती/होते)."),
 "how_it_works": (
  "This record moves your storytelling into the past: the -ल- past endings, "
  "the ergative agreement (खाल्ले with आंबे, खाल्ली with गाणी), and होता/होती/"
  "होते for 'was'. Compare each sentence with its present-tense twin from "
  "Story I. Then narrate a real trip you took, entirely in the past tense."),
 "key_points": [
  "10-sentence past-tense story with line-by-line translation.",
  "Title: प्रवास (pravās) - 'The Journey'.",
  "Ergative past in action: आम्ही आंबे खाल्ले (verb agrees with mangoes).",
  "Past of 'to be': होता (masc), होती (fem), होते (neut/pl).",
 ],
 "requirements": [
  "Narrate a real past trip in ten Marathi sentences.",
  "Convert five Story I sentences into the past tense.",
  "Say all sentences aloud.",
 ],
 "standards": ["Past tense and ergative agreement per standard Marathi grammar (Dhongde & Wali 2009, ch. 6)."],
 "citations": [CIT_DW, CIT_MASICA],
 "sig_lens": (
  "Through the Signature lens this story is his logbook: the journey "
  "recorded, every verb stamped in the past, the ergative flag flying over "
  "each transitive line. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 27
{
 "key": "story3", "name": "Marathi Short Story III: The Promise (Future Tense)",
 "group": "Advanced", "ladder": 27, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A ten-sentence Marathi story in the future tense, line by line with English "
  "translation. Title: वचन (vacan) - 'The Promise'. 1. उद्या मी नवीन शाळेत "
  "जाईन (udyā mī navīn śāḷet jāīn) - 'Tomorrow I will go to the new school'. 2. "
  "मी लवकर उठेन आणि तयार होईन (mī lavkar uṭhen āṇi tayār hoīn) - 'I will wake "
  "up early and get ready'. 3. आई मला डबा देईल (āī malā ḍabā deīl) - 'Mother "
  "will give me the lunchbox'. 4. मी नव्या मित्रांना भेटेन (mī navyā mitrānnā "
  "bheṭen) - 'I will meet new friends'. 5. शिक्षक मला धडा शिकवतील (śikṣak malā "
  "dhaḍā śikavtīl) - 'The teachers will teach me the lesson'. 6. मी मन लावून "
  "अभ्यास करीन (mī man lāvūn abhyās karīn) - 'I will study with full attention'. "
  "7. परीक्षेत मी चांगले गुण मिळवीन (parīkṣet mī cāṅgle guṇ miḷvīn) - 'In the "
  "exam I will score good marks'. 8. आई-वडिलांना अभिमान वाटेल (āī-vaḍilānnā "
  "abhimān vāṭel) - 'My parents will feel proud'. 9. मी मोठा होऊन डॉक्टर होईन "
  "(mī moṭhā hoūn ḍŏkṭar hoīn) - 'Growing up, I will become a doctor'. 10. हे "
  "माझे वचन आहे (he mājhe vacan āhe) - 'This is my promise'. The story uses the "
  "future endings -ईन (first person), -ईल (third singular), -तील (third "
  "plural/respectful)."),
 "how_it_works": (
  "This record aims your Marathi at tomorrow: the future endings -ईन, -शील, "
  "-ईल, -ऊ, -तील in a story of promises. Notice how the future carries resolve "
  "- मी करीन is a vow, not just a prediction. Make five promises about your "
  "own future in Marathi, each with a different future ending."),
 "key_points": [
  "10-sentence future-tense story with line-by-line translation.",
  "Title: वचन (vacan) - 'The Promise'.",
  "Future endings: -ईन (I will), -शील (you will), -ईल (he/she will), -तील (they will).",
  "मी मन लावून अभ्यास करीन - 'I will study with full attention'.",
 ],
 "requirements": [
  "Make five promises about your future in Marathi.",
  "Convert five Story I sentences into the future tense.",
  "Say all sentences aloud.",
 ],
 "standards": ["Future tense morphology per standard Marathi grammar (Dhongde & Wali 2009, ch. 6)."],
 "citations": [CIT_DW, CIT_MASICA],
 "sig_lens": (
  "Through the Signature lens this story is his charter: ten vows in the "
  "future tense, every -ईन a signature on tomorrow. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 28
{
 "key": "idioms", "name": "Marathi Idioms and Proverbs",
 "group": "Advanced", "ladder": 28, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Twenty Marathi idioms and proverbs with literal translation, real meaning, "
  "and an example sentence each. 1. अति तेथे माती (ati tethe mātī) - literal: "
  "'where there is excess, there is dust' - meaning: excess ruins everything. "
  "Ex: अति खाणे आरोग्याला वाईट, अति तेथे माती (ati khāṇe ārogyālā vāīṭ, ati "
  "tethe mātī) - 'Overeating is bad for health - excess ruins everything'. 2. "
  "नाचता येईना अंगण वाकडे (nāctā yeīnā āṅgaṇ vākḍe) - literal: 'cannot dance, "
  "says the courtyard is crooked' - meaning: blaming others for one's own "
  "failure. Ex: परीक्षेत नापास झाला आणि शिक्षकांना दोष देतो, नाचता येईना अंगण "
  "वाकडे - 'He failed and blames the teachers - a bad workman blames his "
  "tools'. 3. हातची काकणाला आरसा कशाला (hātacī kākaṇālā ārsā kaśālā) - literal: "
  "'why a mirror for the bracelet on your own wrist' - meaning: what is "
  "obvious needs no proof. 4. थेंबे थेंबे तळे साचे (thembeth thebe taḷe sāce) - "
  "literal: 'drop by drop the lake fills' - meaning: small efforts accumulate. "
  "5. जसा देश तसा वेश (jasā deś tasā veś) - literal: 'as the country, so the "
  "dress' - meaning: when in Rome, do as the Romans do. 6. दाम करी काम (dām "
  "karī kām) - literal: 'money does the work' - meaning: money gets things "
  "done. 7. एका हाताने टाळी वाजत नाही (ekā hātāne ṭāḷī vājat nāhī) - literal: "
  "'one hand cannot clap' - meaning: it takes two for a quarrel. 8. रिकामे "
  "भांडे जास्त वाजते (rikāme bhāṇḍe jāst vājte) - literal: 'an empty vessel "
  "makes more noise' - meaning: empty minds boast most. 9. जिभेवर साखर (jibhevar "
  "sākhar) - literal: 'sugar on the tongue' - meaning: sweet speech. Ex: "
  "त्याच्या जिभेवर साखर आहे (tyācyā jibhevar sākhar āhe) - 'He speaks sweetly'. "
  "10. डोळे वटारणे (ḍoḷe vaṭārṇe) - literal: 'to widen the eyes' - meaning: to "
  "glare angrily. 11. हातभार लावणे (hātbhār lāvṇe) - literal: 'to lend a hand's "
  "weight' - meaning: to help. Ex: कामात हातभार लाव (kāmāt hātbhār lāv) - "
  "'Lend a hand with the work'. 12. पाठ थोपटणे (pāṭh thopaṭṇe) - literal: 'to "
  "pat the back' - meaning: to encourage/praise. 13. तोंडावर येणे (toṇḍāvar "
  "yeṇe) - literal: 'to come on the mouth' - meaning: to be about to say. 14. "
  "कान भरणे (kān bharṇe) - literal: 'to fill the ears' - meaning: to poison "
  "someone's mind against another. 15. पाणी पाजणे (pāṇī pājṇe) - literal: 'to "
  "make someone drink water' - meaning: to defeat soundly. 16. डोक्यावर घेणे "
  "(ḍokyāvar gheṇe) - literal: 'to take on the head' - meaning: to take "
  "responsibility. 17. हृदय पिळवटणे (hṛday piḷvaṭṇe) - literal: 'to wring the "
  "heart' - meaning: to grieve deeply. 18. शिंगावर घेणे (śiṅgāvar gheṇe) - "
  "literal: 'to take on the horns' - meaning: to confront boldly. 19. गळा काढणे "
  "(gaḷā kāḍhṇe) - literal: 'to take out the throat' - meaning: to shout "
  "loudly. 20. वेळ मारून नेणे (veḷ mārūn neṇe) - literal: 'to kill time and "
  "take it away' - meaning: to procrastinate."),
 "how_it_works": (
  "This record teaches you to speak like a native: idioms are the shortcut to "
  "sounding Marathi. Each entry gives the literal image, the real meaning, and "
  "a sentence showing it alive. Learn five a week; drop one into real "
  "conversation and watch faces light up - that is the idiom working."),
 "key_points": [
  "20 idioms/proverbs: literal image + real meaning + example sentence.",
  "अति तेथे माती - 'excess ruins everything'; थेंबे थेंबे तळे साचे - 'small efforts accumulate'.",
  "नाचता येईना अंगण वाकडे - 'a bad workman blames his tools'.",
  "Body idioms: जिभेवर साखर (sweet speech), डोळे वटारणे (glare), हातभार लावणे (help).",
 ],
 "requirements": [
  "Use five idioms in real conversation this week.",
  "Explain three idioms' literal vs real meanings to a friend.",
  "Say all example sentences aloud.",
 ],
 "standards": ["Idiomatic usage per standard Marathi (Molesworth 1857; Dhongde & Wali 2009)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens idioms are his code phrases: अति तेथे माती the "
  "warning flag, थेंबे थेंबे तळे साचे the compounding law - compressed wisdom "
  "he deploys in one line. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 29
{
 "key": "registers", "name": "Marathi Formal and Polite Registers",
 "group": "Advanced", "ladder": 29, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Fifteen formal-versus-informal Marathi pairs for letters, business, and "
  "elders, each translated. 1. Informal: तू कसा आहेस (tū kasā āhes) - 'How are "
  "you'. Formal: तुम्ही कसे आहात (tumhī kase āhāt) - 'How are you (respectful)'. "
  "2. Informal: ये (ye) - 'Come'. Formal: कृपया या (kṛpayā yā) - 'Please come'. "
  "3. Informal: बस (bas) - 'Sit'. Formal: कृपया बसा (kṛpayā basā) - 'Please be "
  "seated'. 4. Informal: दे (de) - 'Give'. Formal: कृपया द्या (kṛpayā dyā) - "
  "'Please give'. 5. Informal: सांग (sāṅg) - 'Tell'. Formal: सांगावे (sāṅgāve) "
  "- 'Kindly inform' - letter style. 6. Informal: कर (kar) - 'Do'. Formal: "
  "करावे (karāve) - 'Kindly do' - official style. 7. Informal: माफ कर (māph "
  "kar) - 'Forgive'. Formal: क्षमा करावी (kṣamā karāvī) - 'Kindly forgive' - "
  "written apology. 8. Informal: धन्यवाद (dhanyavād) - 'Thanks'. Formal: मनःपूर्वक "
  "आभार (manaḥpūrvak ābhār) - 'Heartfelt gratitude' - formal letter. 9. "
  "Informal: भेटू (bheṭū) - 'See you'. Formal: भेटण्याची संधी द्यावी "
  "(bheṭaṇyācī sandhī dyāvī) - 'Kindly grant an appointment' - business. 10. "
  "Informal: फोन कर (phon kar) - 'Call'. Formal: संपर्क साधावा (sampark "
  "sādhāvā) - 'Kindly contact' - official. 11. Informal: पैसे दे (paise de) - "
  "'Give money'. Formal: रक्कम अदा करावी (rakkam adā karāvī) - 'Kindly remit "
  "the amount' - business. 12. Informal: लवकर ये (lavkar ye) - 'Come soon'. "
  "Formal: लवकर यावे ही विनंती (lavkar yāve hī vinantī) - 'You are requested "
  "to come soon' - invitation. 13. Informal: काळजी घे (kāḷjī ghe) - 'Take care'. "
  "Formal: काळजी घ्यावी ही विनंती (kāḷjī ghyāvī hī vinantī) - 'You are "
  "requested to take care' - elder. 14. Informal: ऐक (aik) - 'Listen'. Formal: "
  "लक्ष द्यावे (lakṣa dyāve) - 'Kindly pay attention' - meeting. 15. Informal: "
  "थांब (thāmb) - 'Stop'. Formal: थांबावे ही विनंती (thāmbāve hī vinantī) - "
  "'You are requested to stop' - official notice. The -ावे form is the "
  "signature of written formal Marathi."),
 "how_it_works": (
  "This record teaches the two Marathis: the spoken one for friends and the "
  "-ावे one for letters, offices, and elders. The formal register adds distance "
  "and respect through तुम्ही, कृपया, and the -ावे verb form. Write one formal "
  "letter (an application, an apology) and one informal note to feel the gear "
  "shift."),
 "key_points": [
  "15 formal/informal pairs: letters, business, elders.",
  "The -ावे form (सांगावे, करावे) is the signature of written formal Marathi.",
  "तू vs तुम्ही; कृपया as the spoken softener; ही विनंती as the written closer.",
  "मनःपूर्वक आभार - 'heartfelt gratitude' for formal thanks.",
 ],
 "requirements": [
  "Write a formal leave application in Marathi.",
  "Convert five informal sentences to formal register.",
  "Say all 30 lines aloud, feeling the tone shift.",
 ],
 "standards": ["Honorific and formal verb morphology per standard Marathi usage (Dhongde & Wali 2009, ch. 6)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens register is his dress code: the stem for the "
  "inner circle, -ावे for the court - every -ावे a bow, every कृपया a handshake. "
  "Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 30
{
 "key": "complex", "name": "Marathi Compound and Complex Sentences",
 "group": "Advanced", "ladder": 30, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Fifteen long Marathi sentences with clauses, connectors, and relative "
  "clauses - parsed and translated. 1. मी बाजारात गेलो आणि भाजी आणली (mī "
  "bājārāt gelo āṇi bhājī āṇlī) - 'I went to the market and brought vegetables' "
  "- two clauses joined by आणि (and). 2. पाऊस पडत होता म्हणून आम्ही घरी "
  "थांबलो (pāūs paḍat hotā mhaṇūn āmhī gharī thāmblo) - 'It was raining, so we "
  "stayed home' - म्हणून (so/therefore). 3. जरी तो थकला होता तरी त्याने काम "
  "पूर्ण केले (jarī to thaklā hotā tarī tyāne kām pūrṇa kele) - 'Although he "
  "was tired, he completed the work' - जरी...तरी (although...yet). 4. जो मुलगा "
  "अभ्यास करतो तो यशस्वी होतो (jo mulgā abhyās karto to yaśasvī hoto) - 'The "
  "boy who studies succeeds' - जो...तो relative clause. 5. जी मुलगी गाते ती "
  "माझी बहीण आहे (jī mulgī gāte tī mājhī bahīṇ āhe) - 'The girl who sings is my "
  "sister' - feminine relative. 6. जे पुस्तक तू वाचतोस ते माझे आहे (je pustak "
  "tū vāctos te mājhe āhe) - 'The book that you are reading is mine' - neuter "
  "relative. 7. मी जेव्हा घरी पोहोचलो तेव्हा आई वाट बघत होती (mī jevhā gharī "
  "pohochlo tevhā āī vāṭ baghat hotī) - 'When I reached home, mother was "
  "waiting' - जेव्हा...तेव्हा (when...then). 8. जर पाऊस पडला तर सामना रद्द होईल "
  "(jar pāūs paḍlā tar sāmnā radda hoīl) - 'If it rains, the match will be "
  "cancelled' - जर...तर (if...then). 9. तो इतका वेगाने धावला की सगळे थक्क झाले "
  "(to itkā vegāne dhāvlā kī sagaḷe thakka jhāle) - 'He ran so fast that "
  "everyone was amazed' - की result clause. 10. मला माहीत आहे की तू येशील "
  "(malā māhīt āhe kī tū yeśīl) - 'I know that you will come' - की complement. "
  "11. काम संपल्यावर आम्ही घरी जाऊ (kām samplyāvar āmhī gharī jāū) - 'After "
  "the work ends, we will go home' - -ल्यावर (after doing). 12. जेवण करून तो "
  "बाहेर गेला (jevaṇ karūn to bāher gelā) - 'Having eaten, he went out' - -ून "
  "conjunctive participle. 13. ती गात गात चालली (tī gāt gāt cāllī) - 'She walked "
  "along singing' - repeated participle for ongoing action. 14. माझ्याकडे वेळ "
  "असता तर मी आलो असतो (mājhyākaḍe veḷ astā tar mī ālo asto) - 'If I had time, "
  "I would have come' - conditional perfect. 15. शिकल्याशिवाय यश मिळत नाही "
  "(śikalyāśivāy yaś miḷat nāhī) - 'Without learning, success does not come' - "
  "-ल्याशिवाय (without doing)."),
 "how_it_works": (
  "This record builds long sentences from short ones: आणि joins, म्हणून "
  "explains, जरी...तरी concedes, जो...तो relativizes, जर...तर conditions, की "
  "reports, and the participles (-ून, -ल्यावर, -ल्याशिवाय) pack whole clauses "
  "into single words. Take three simple sentences and join them five different "
  "ways - that is the whole skill."),
 "key_points": [
  "15 parsed complex sentences: coordination, subordination, relativization.",
  "Connectors: आणि, म्हणून, जरी...तरी, जेव्हा...तेव्हा, जर...तर, की.",
  "Relative जो...तो agrees in gender: जो मुलगा, जी मुलगी, जे पुस्तक.",
  "Participles: -ून (having done), -ल्यावर (after), -ल्याशिवाय (without).",
 ],
 "requirements": [
  "Join five pairs of simple sentences with five different connectors.",
  "Write three जो...तो relative sentences, one per gender.",
  "Say all 15 sentences aloud slowly.",
 ],
 "standards": ["Complex sentence syntax per standard Marathi grammar (Dhongde & Wali 2009, ch. 8)."],
 "citations": [CIT_DW, CIT_MASICA],
 "sig_lens": (
  "Through the Signature lens complex sentences are his engineering drawings: "
  "आणि the welds, जो...तो the load-bearing joints, participles the compact "
  "fasteners - every clause carrying weight. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 31
{
 "key": "conv_market", "name": "Marathi Conversation: At the Market",
 "group": "Advanced", "ladder": 31, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A twenty-line bilingual Marathi-English dialogue at the market, annotated. "
  "Speakers: ग्राहक (grāhak) - 'customer' (G), विक्रेता (vikretā) - 'seller' (V). "
  "1. G: नमस्कार, टोमॅटो कसे दिले (namaskār, ṭomæṭo kase dile) - 'Hello, how "
  "much are the tomatoes' - [कसे दिले = how did you give = what is the rate]. "
  "2. V: नमस्कार, चाळीस रुपये किलो (namaskār, cāḷīs rupaye kilo) - 'Hello, "
  "forty rupees a kilo'. 3. G: भाव जास्त आहे, तीसला द्या (bhāv jāst āhe, "
  "tīslā dyā) - 'The price is high, give for thirty' - [bargaining opens]. 4. "
  "V: तीसला नाही जमणार, पस्तीसला घ्या (tīslā nāhī jamṇār, pastīslā ghyā) - "
  "'Thirty will not work, take for thirty-five'. 5. G: ठीक आहे, एक किलो द्या "
  "(ṭhīk āhe, ek kilo dyā) - 'Okay, give one kilo'. 6. V: आणखी काही (āṇakhī "
  "kāhī) - 'Anything else'. 7. G: कांदे कसे (kānde kase) - 'How much are the "
  "onions'. 8. V: वीस रुपये किलो, ताजे आहेत (vīs rupaye kilo, tāje āhet) - "
  "'Twenty a kilo, they are fresh'. 9. G: अर्धा किलो कांदे द्या (ardhā kilo "
  "kānde dyā) - 'Give half a kilo of onions'. 10. V: हे घ्या, एकूण पंचावन्न "
  "रुपये (he ghyā, ekūṇ pancāvanna rupaye) - 'Take these, fifty-five rupees "
  "total'. 11. G: शंभरची नोट आहे, सुटे आहेत का (śambharcī noṭ āhe, suṭe āhet "
  "kā) - 'I have a hundred note, do you have change' - [payment]. 12. V: हो, "
  "आहेत (ho, āhet) - 'Yes, I do'. 13. G: पिशवी द्या (piśvī dyā) - 'Give a bag'. "
  "14. V: ही घ्या पिशवी (hī ghyā piśvī) - 'Take the bag'. 15. G: धन्यवाद (dhanyavād) "
  "- 'Thank you'. 16. V: परत या (parat yā) - 'Come again'. 17. G: उद्या भाजी "
  "ताजी असेल का (udyā bhājī tājī asel kā) - 'Will the vegetables be fresh "
  "tomorrow'. 18. V: रोज ताजी भाजी येते (roj tājī bhājī yete) - 'Fresh "
  "vegetables come daily'. 19. G: मग उद्या नक्की येईन (mag udyā nakkī yeīn) - "
  "'Then I will definitely come tomorrow'. 20. V: वाट बघतो (vāṭ baghto) - 'I "
  "will wait' - [warm close]. The dialogue shows the full market arc: greeting, "
  "price ask, bargain, deal, add-on, total, payment, bag, thanks, return promise."),
 "how_it_works": (
  "This record is a rehearsed market visit: read both roles aloud, then play "
  "the customer while a partner plays the seller. The annotations decode the "
  "idioms (कसे दिले, नाही जमणार) that textbooks skip. When you can bargain to "
  "पस्तीसला without pausing, the market is yours."),
 "key_points": [
  "20-line bilingual market dialogue with annotations.",
  "Bargaining arc: कसे दिले - भाव जास्त आहे - तीसला द्या - पस्तीसला घ्या.",
  "Payment and close: सुटे आहेत का - परत या - वाट बघतो.",
  "नाही जमणार - 'it will not work' - the seller's key refusal phrase.",
 ],
 "requirements": [
  "Role-play both parts aloud twice.",
  "Bargain a new item using the same arc.",
  "Memorize the six bargaining phrases.",
 ],
 "standards": ["Commercial dialogue per standard Marathi usage (Molesworth 1857)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens the market dialogue is his trade negotiation "
  "drill: price asked, value tested, deal closed - every line a move on the "
  "board. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 32
{
 "key": "conv_friend", "name": "Marathi Conversation: Meeting a Friend",
 "group": "Advanced", "ladder": 32, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A twenty-line bilingual Marathi-English dialogue meeting a friend, annotated. "
  "Speakers: अमित (Amit, A), प्रिया (Priya, P). 1. A: अरे प्रिया, कशी आहेस "
  "(are priyā, kaśī āhes) - 'Hey Priya, how are you' - [अरे = warm informal "
  "hey]. 2. P: मी छान आहे, तू कसा आहेस (mī chān āhe, tū kasā āhes) - 'I am "
  "great, how are you'. 3. A: मी पण ठीक आहे, खूप दिवसांनी भेटलो (mī paṇ ṭhīk "
  "āhe, khūp divsānnī bheṭlo) - 'I am fine too, meeting after many days'. 4. "
  "P: हो ना, काय चाललंय (ho nā, kāy cāllay) - 'Yes, what is going on' - [काय "
  "चाललंय = what is up]. 5. A: अभ्यास चालू आहे, परीक्षा जवळ आली (abhyās cālū "
  "āhe, parīkṣā javaḷ ālī) - 'Studies are on, exams are near'. 6. P: माझी पण "
  "तयारी चालू आहे (mājhī paṇ tayārī cālū āhe) - 'My preparation is also on'. "
  "7. A: चहा घेशील का (cahā gheśīl kā) - 'Will you have tea' - [the "
  "hospitality move]. 8. P: हो, चालेल (ho, cālel) - 'Yes, fine'. 9. A: चल, "
  "टपरीवर जाऊया (cal, ṭaparīvar jāūyā) - 'Come, let us go to the tea stall'. "
  "10. P: चालेल, मला कटिंग हवी (cālel, malā kaṭiṅg havī) - 'Okay, I want a "
  "cutting' - [कटिंग = Mumbai half-glass tea]. 11. A: दोन कटिंग द्या (don "
  "kaṭiṅg dyā) - 'Give two cuttings' - [ordering]. 12. P: आठवतंय का, शाळेतले "
  "दिवस (āṭhvatay kā, śāḷetle divas) - 'Do you remember the school days'. 13. "
  "A: कसे विसरेन, खूप मजा यायची (kase visren, khūp majā yāycī) - 'How could I "
  "forget, it was so much fun'. 14. P: शिक्षक अजूनही तेच आहेत (śikṣak ajūnhī "
  "tec āhet) - 'The teachers are still the same'. 15. A: उद्या भेटूया का (udyā "
  "bheṭūyā kā) - 'Shall we meet tomorrow'. 16. P: हो, संध्याकाळी चालेल (ho, "
  "sandhyākāḷī cālel) - 'Yes, evening works'. 17. A: मग ठरलं (mag ṭharlã) - "
  "'Then it is decided'. 18. P: फोन करशील ना (phon karśīl nā) - 'You will call, "
  "right'. 19. A: नक्की करेन (nakkī karen) - 'I definitely will'. 20. P: चल, "
  "बाय (cal, bāy) - 'Okay, bye' - [warm close]. The dialogue shows informal "
  "तू register, nostalgia, hospitality, and plan-making between friends."),
 "how_it_works": (
  "This record is friendship in the informal register: अरे, काय चाललंय, कटिंग "
  "चहा - the Marathi of real friends. Notice how invitations and plans are made "
  "(जाऊया, भेटूया का, ठरलं). Meet a real friend and run this conversation for "
  "real - the dialogue is a script until you live it."),
 "key_points": [
  "20-line bilingual friend dialogue with annotations.",
  "Informal register: अरे, काय चाललंय, तू forms throughout.",
  "Hospitality: चहा घेशील का; plan-making: जाऊया, भेटूया का, ठरलं.",
  "कटिंग (kaṭiṅg) - the Mumbai half-glass tea, a cultural password.",
 ],
 "requirements": [
  "Run this conversation with a real friend.",
  "Make three real plans using जाऊया/भेटूया.",
  "Say all 20 lines aloud with warmth.",
 ],
 "standards": ["Informal register and discourse markers per standard Marathi usage (Dhongde & Wali 2009, ch. 1)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens this dialogue is his reunion protocol: the warm "
  "अरे, the shared past, the tea, the plan - friendship maintained in twenty "
  "lines. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 33
{
 "key": "conv_problem", "name": "Marathi Conversation: Solving a Problem",
 "group": "Advanced", "ladder": 33, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A twenty-line bilingual Marathi-English dialogue solving a problem, "
  "annotated. Speakers: व्यवस्थापक (vyavasthāpak) - 'manager' (M), कर्मचारी "
  "(karmacārī) - 'employee' (E). 1. M: काय झाले, सांगा (kāy jhāle, sāṅgā) - "
  "'What happened, tell me' - [problem opening]. 2. E: सर्व्हर बंद पडला आहे "
  "(sarvhar band paḍlā āhe) - 'The server is down'. 3. M: कधीपासून (kadhīpāsūn) "
  "- 'Since when'. 4. E: सकाळी नऊ वाजल्यापासून (sakāḷī naū vājlyāpāsūn) - "
  "'Since nine in the morning'. 5. M: ग्राहकांना कळवले का (grāhakānnā "
  "kaḷavle kā) - 'Did you inform the customers'. 6. E: हो, मेसेज पाठवला (ho, "
  "mesej pāṭhavlā) - 'Yes, I sent a message'. 7. M: तंत्रज्ञाला बोलावले का "
  "(tantradnyālā bolāvle kā) - 'Did you call the technician'. 8. E: हो, तो "
  "वाटेत आहे (ho, to vāṭet āhe) - 'Yes, he is on the way'. 9. M: ठीक आहे, "
  "बॅकअप चालू करा (ṭhīk āhe, bækap cālū karā) - 'Okay, start the backup' - "
  "[action]. 10. E: बॅकअप तयार आहे (bækap tayār āhe) - 'The backup is ready'. "
  "11. M: किती वेळ लागेल (kitī veḷ lāgel) - 'How long will it take'. 12. E: "
  "अंदाजे एक तास (andāje ek tās) - 'About one hour'. 13. M: ग्राहकांना वेळ "
  "सांगा (grāhakānnā veḷ sāṅgā) - 'Tell the customers the time'. 14. E: हो, "
  "लगेच सांगतो (ho, lagec sāṅgto) - 'Yes, I will tell them right away'. 15. "
  "M: काळजी करू नका (kāḷjī karū nakā) - 'Do not worry' - [reassurance]. 16. E: "
  "धन्यवाद सर (dhanyavād sar) - 'Thank you, sir'. 17. M: पुढे अशी चूक होऊ नये "
  "(puḍhe aśī cūk hoū naye) - 'Such a mistake should not happen again' - "
  "[prevention]. 18. E: नक्की काळजी घेईन (nakkī kāḷjī gheīn) - 'I will surely "
  "take care'. 19. M: चांगले, कामाला लागा (cāṅgle, kāmālā lāgā) - 'Good, get "
  "to work'. 20. E: हो सर (ho sar) - 'Yes sir' - [respectful close]. The "
  "dialogue shows the problem-solving arc: report, timeline, containment, "
  "action, estimate, communication, reassurance, prevention."),
 "how_it_works": (
  "This record runs a crisis in formal Marathi: the manager's diagnostic "
  "questions (काय झाले, कधीपासून, किती वेळ लागेल), the employee's status "
  "reports, and the action orders (चालू करा, सांगा). The arc - report, contain, "
  "act, prevent - works for any problem. Rehearse it, then use it for a real "
  "small problem in Marathi."),
 "key_points": [
  "20-line bilingual problem-solving dialogue with annotations.",
  "Diagnostic questions: काय झाले, कधीपासून, किती वेळ लागेल.",
  "Action arc: report, contain (बॅकअप चालू करा), communicate, prevent.",
  "पुढे अशी चूक होऊ नये - 'Such a mistake should not happen again'.",
 ],
 "requirements": [
  "Role-play both parts aloud.",
  "Solve a real small problem narrating in Marathi.",
  "Memorize the five diagnostic questions.",
 ],
 "standards": ["Formal workplace register per standard Marathi usage (Dhongde & Wali 2009, ch. 1)."],
 "citations": [CIT_DW, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens this dialogue is his incident response playbook: "
  "diagnose, contain, communicate, prevent - every crisis handled in formal "
  "Marathi. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 34
{
 "key": "mastery", "name": "Marathi Mastery Review and Full Reference",
 "group": "Advanced", "ladder": 34, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The whole Marathi database in one teaching summary: alphabet, 200 core "
  "words, key grammar, and all phrase tables. ALPHABET: 13 vowels (अ आ इ ई उ "
  "ऊ ऋ ए ऐ ओ औ अं अः), 34 consonants (क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न "
  "प फ ब भ म य र ल व श ष स ह ळ), digits ०-९, danda । - plus the historical "
  "Modi script (मोडी). SOUNDS: schwa 'a', retroflexes, Marathi ळ, aspiration "
  "pairs, schwa deletion, nasalization. CORE WORDS (200): nouns - माणूस, आई, "
  "वडील, मुलगा, मुलगी, मित्र, घर, शाळा, पुस्तक, पाणी, जेवण, बाजार, रस्ता, गाव, "
  "शहर, झाड, फूल, प्राणी, वेळ, दिवस, काम, पैसा, नाव, प्रश्न, उत्तर; verbs - "
  "जाणे, येणे, करणे, खाणे, पिणे, बोलणे, वाचणे, लिहिणे, पाहणे, ऐकणे, देणे, घेणे, "
  "बसणे, उभे राहणे, झोपणे, उठणे, चालणे, धावणे, हसणे, रडणे, शिकणे, शिकवणे, "
  "खेळणे, काम करणे, प्रेम करणे; adjectives - चांगला, मोठा, लहान, नवीन, जुना, "
  "सुंदर, वाईट, लांब, आखूड, उंच, खोल, गरम, थंड, गोड, आंबट, तिखट, श्रीमंत, गरीब, "
  "आनंदी, दुःखी, हुशार, आळशी, स्वच्छ, घाणेरडा, महत्त्वाचा; adverbs - वेगाने, "
  "हळू, नेहमी, कधीही, आज, उद्या, काल, इथे, तिथे, खूप, थोडे, एकत्र, एकटे, पुन्हा, "
  "नक्की; pronouns - मी, तू, तुम्ही, तो, ती, ते, आम्ही, आपण, माझा, तुझा, तुमचा, "
  "त्याचा; numbers - एक, दोन, तीन, चार, पाच, सहा, सात, आठ, नऊ, दहा, वीस, तीस, "
  "शंभर, हजार; greetings - नमस्कार, धन्यवाद, माफ करा, कृपया, हो, नाही, ठीक आहे; "
  "plus body, food, emotion, nature, and tech words from the domain records. "
  "GRAMMAR: SOV order; three genders; two numbers; postpositions ला/ने/चा-ची-चे/"
  "त/कडून/साठी/बरोबर; no articles; नाही negation; in-place questions; split "
  "ergativity with ने; present -तो/-ते/-तं, past -ल-, future -ईल/-णार, imperative, "
  "optative -ावा; जो...तो relatives; participles -ून/-ल्यावर/-ल्याशिवाय. PHRASE "
  "TABLES: greetings (नमस्कार through भेटून आनंद झाला), market bargaining "
  "(कितीला आहे through शेवटचा भाव सांगा), travel (कुठे आहे, कितीला आहे, मीटरने "
  "चला), health (मला ताप आला आहे, औषध दुकान कुठे आहे), 20 idioms (अति तेथे "
  "माती, थेंबे थेंबे तळे साचे), 15 register pairs (ये/कृपया या, कर/करावे). "
  "STORIES: एक साधा दिवस (present), प्रवास (past), वचन (future). DIALOGUES: "
  "market, friend, problem-solving. You now hold the complete ladder: "
  "foundations (records 1-10), compounded (11-20), advanced (21-34)."),
 "how_it_works": (
  "This record is the whole database compressed: use it as your daily "
  "drill sheet and your exam. Cover the English column and produce the "
  "Marathi; cover the Marathi and produce the English. When you can recite the "
  "alphabet, the 200 words, and the grammar rules from memory, the ladder is "
  "climbed - then start again from record 1, because mastery is a circle."),
 "key_points": [
  "Full reference: alphabet, 200 core words, grammar, phrase tables, idioms, stories, dialogues.",
  "13 vowels, 34 consonants, digits ०-९; SOV; three genders; split ergativity.",
  "200 core words across nouns, verbs, adjectives, adverbs, pronouns, numbers, greetings.",
  "Ladder complete: foundations 1-10, compounded 11-20, advanced 21-34.",
 ],
 "requirements": [
  "Recite the alphabet and 200 words from memory.",
  "Write the grammar rules from memory, then check.",
  "Retake the whole database: one record per day for 34 days.",
 ],
 "standards": [CIT_ISO, CIT_UNI, "Full grammar per Dhongde & Wali 2009; lexicon per Molesworth 1857."],
 "citations": [CIT_DW, CIT_MASICA, CIT_MOLES],
 "sig_lens": (
  "Through the Signature lens this review is his instrument certification: "
  "every key tested, every string tuned, the full Marathi system under his "
  "command. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
]
