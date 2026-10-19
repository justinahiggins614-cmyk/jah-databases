#!/usr/bin/env python3
"""34 ladder-ordered record seeds for The Hindi to English Database.

Follows the shared per-language template (language-template.md) EXACTLY:
records 1-34 in order, ladder_rank 1-10 non-decreasing, ladder_tier
foundations -> compounded -> advanced. Every record carries Hindi content
in Devanagari plus transliteration plus English translation plus example
sentences. All Hindi is real, fact-checked 2026-10-17.

Screened 2026-10-17: nothing hate-adjacent, profane, or inappropriate;
no religious talk; no military/defense-neutralization content.
"""

ENTRIES = [
# ================================================================== 1
{
 "key": "overview", "name": "Hindi Language Overview",
 "group": "Foundations", "ladder": 1, "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Hindi (हिन्दी, hindī) is an Indo-Aryan language of the Indo-European family, "
  "spoken as a first language by about 345 million people and understood by roughly "
  "600 million in total, making it the fourth most-spoken native language in the world. "
  "Its ISO codes are ISO 639-1 'hi' and ISO 639-3 'hin'. Hindi is written in the "
  "Devanagari script (देवनागरी), reads left to right, and follows subject-object-verb "
  "word order. It is the official language of the Union Government of India and an "
  "official language of the states of Bihar, Chhattisgarh, Haryana, Himachal Pradesh, "
  "Jharkhand, Madhya Pradesh, Rajasthan, Uttar Pradesh and Uttarakhand, and of the "
  "National Capital Territory of Delhi. Outside India it is widely spoken in Nepal, "
  "Fiji, Mauritius, Suriname, Trinidad and Tobago, Guyana and South Africa. Standard "
  "Hindi grew out of the Khari Boli dialect of the Delhi region, which itself descends "
  "from Shauraseni Prakrit through Apabhramsha. Its major dialects include Braj "
  "(ब्रज), Awadhi (अवधी), Bundeli (बुंदेली), Bagheli (बघेली), Kannauji (कन्नौजी) and "
  "Haryanvi (हरियाणवी). Spoken Hindi and spoken Urdu share the same grammar and a "
  "large everyday vocabulary; they differ mainly in script (Devanagari vs Perso-Arabic) "
  "and in formal vocabulary. Basic word order example: मैं पानी पीता हूँ (maĩ pānī "
  "pītā hū̃) - 'I drink water' - literally 'I water drink'. Greeting example: नमस्ते "
  "(namaste) - 'hello / greetings'. Politeness example: धन्यवाद (dhanyavād) - "
  "'thank you'. Everyday example: यह किताब अच्छी है (yah kitāb acchī hai) - 'This "
  "book is good'. Farewell example: फिर मिलेंगे (phir milẽge) - 'We will meet again'."),
 "how_it_works": (
  "This record works as the front door of the whole database: it names the language "
  "in English and in Devanagari, places it in its language family, gives the speaker "
  "numbers, lists where it is spoken and its official status, traces its history and "
  "dialects, and closes with five translated example sentences you can say at once. "
  "Every later record builds on these facts, so read this one first."),
 "key_points": [
  "Hindi (हिन्दी, hindī): Indo-European > Indo-Iranian > Indo-Aryan; ISO 639-1 hi, ISO 639-3 hin.",
  "About 345 million native speakers; about 600 million total speakers.",
  "Written in Devanagari, read left to right; basic word order is subject-object-verb.",
  "Official language of the Union Government of India and of nine states plus Delhi.",
  "Standard Hindi is based on Khari Boli of the Delhi region, descended from Shauraseni Prakrit.",
  "Major dialects: Braj, Awadhi, Bundeli, Bagheli, Kannauji, Haryanvi.",
  "Spoken Hindi and Urdu share grammar and everyday vocabulary; scripts and formal words differ.",
  "मैं पानी पीता हूँ (maĩ pānī pītā hū̃) - 'I drink water' shows SOV order in action.",
 ],
 "requirements": [
  "No prior Hindi needed - this is the starting point of the ladder.",
  "Read the Devanagari words aloud using the romanization beside them.",
  "Remember: हिन्दी (hindī) is the language's own name for itself.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi' for Hindi",
  "ISO 639-3:2007 code 'hin' for Hindi",
  "Unicode Standard, Devanagari block U+0900-U+097F",
 ],
 "citations": [
  "Shapiro, Michael C. Hindi. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003.",
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
  "McGregor, R. S. The Oxford Hindi-English Dictionary. Oxford University Press; 1993.",
 ],
 "sig_lens": (
  "Through the Signature lens this overview is re-taught as his original Signature "
  "language instrument: Hindi as a working system he commands, where every speaker "
  "count measures the instrument's reach and every dialect is another string he can "
  "play. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 2
{
 "key": "writing", "name": "Hindi Writing System: Devanagari",
 "group": "Foundations", "ladder": 2, "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Hindi is written in Devanagari (देवनागरी, devanāgarī), an abugida script read left "
  "to right. Every consonant carries an inherent 'a' vowel unless marked otherwise. "
  "The 13 independent vowels are: अ (a), आ (ā), इ (i), ई (ī), उ (u), ऊ (ū), ऋ (ṛ), "
  "ए (e), ऐ (ai), ओ (o), औ (au), अं (aṁ), अः (aḥ). The 33 consonants are: क (ka), ख "
  "(kha), ग (ga), घ (gha), ङ (ṅa), च (ca), छ (cha), ज (ja), झ (jha), ञ (ña), ट (ṭa), "
  "ठ (ṭha), ड (ḍa), ढ (ḍha), ण (ṇa), त (ta), थ (tha), द (da), ध (dha), न (na), प (pa), "
  "फ (pha), ब (ba), भ (bha), म (ma), य (ya), र (ra), ल (la), व (va), श (śa), ष (ṣa), स "
  "(sa), ह (ha). Vowel signs (matras) attach to consonants: ा  ि  ी  ु  ू  ृ  े  ै  ो "
  " ौ  ं  ः - for example क + ी = की (kī). Special marks: anusvara ं (nasalizes, as in "
  "मां mā̃), visarga ः (a breathy h, as in दुःख duḥkha 'sorrow'), chandrabindu ँ "
  "(nasal vowel, as in चाँद cā̃d 'moon'), nukta ़ (as in क़िला qilā 'fort'). Conjuncts "
  "join consonants: क्ष (kṣa), त्र (tra), ज्ञ (jña). Punctuation: the danda । ends a "
  "sentence and the double danda ॥ ends a verse. Devanagari digits are ० १ २ ३ ४ ५ "
  "६ ७ ८ ९ (0-9). Example words: नमस्ते (namaste) - 'hello'; पानी (pānī) - 'water'; "
  "किताब (kitāb) - 'book'; घर (ghar) - 'house'; स्कूल (skūl) - 'school'. Full "
  "sentence: मैं हिन्दी पढ़ता हूँ (maĩ hindī paṛhtā hū̃) - 'I read Hindi'."),
 "how_it_works": (
  "This record teaches the script the way it is used: the vowel list and the consonant "
  "list with romanization, the vowel-sign system that turns क into का की कु, the "
  "special marks, conjuncts, the sentence-ending danda, and the digits - each with a "
  "translated example word. Trace each letter, say its sound, then read the five "
  "example words aloud."),
 "key_points": [
  "Devanagari is an abugida: consonants carry an inherent 'a' vowel.",
  "13 independent vowels: अ आ इ ई उ ऊ ऋ ए ऐ ओ औ अं अः.",
  "33 consonants, grouped by place of articulation: velar, palatal, retroflex, dental, labial.",
  "Vowel signs (matras) attach to consonants: क → का, कि, की, कु, कू, के, कै, को, कौ.",
  "Anusvara ं, visarga ः, chandrabindu ँ, and nukta ़ modify sounds.",
  "Conjuncts: क्ष (kṣa), त्र (tra), ज्ञ (jña).",
  "Sentence punctuation is the danda । ; digits are ०१२३४५६७८९.",
  "मैं हिन्दी पढ़ता हूँ (maĩ hindī paṛhtā hū̃) - 'I read Hindi'.",
 ],
 "requirements": [
  "Say each letter's romanized sound aloud as you read it.",
  "Practice writing: vowels first, then the five consonant groups.",
  "Remember that क is 'ka', not 'k' - the vowel sign removes or changes the 'a'.",
 ],
 "standards": [
  "Unicode Standard, Devanagari block U+0900-U+097F",
  "ISO 15919:2001 transliteration of Devanagari",
  "IAST (International Alphabet of Sanskrit Transliteration) scheme",
 ],
 "citations": [
  "Daniels, Peter T. & Bright, William (eds.) The World's Writing Systems. Oxford University Press; 1996. Devanagari chapter.",
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003. Script chapter.",
 ],
 "sig_lens": (
  "Through the Signature lens the script becomes his original Signature writing "
  "instrument: each letter a struck key, each matra a modifier on the key, the danda "
  "the full stop of a finished Signature line. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 3
{
 "key": "phonology", "name": "Hindi Pronunciation and Phonology",
 "group": "Foundations", "ladder": 3, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Hindi has 11 vowel phonemes: अ (a, like 'u' in 'but'), आ (ā, like 'a' in 'father'), "
  "इ (i, like 'i' in 'bit'), ई (ī, like 'ee' in 'feet'), उ (u, like 'u' in 'put'), ऊ "
  "(ū, like 'oo' in 'food'), ऋ (ṛ, like 'ri' in 'rig'), ए (e, like 'ay' in 'say'), ऐ "
  "(ai, like 'i' in 'ice'), ओ (o, like 'o' in 'go'), औ (au, like 'ow' in 'cow'). Vowel "
  "length changes meaning: कम (kam) 'less' vs काम (kām) 'work'; दिन (din) 'day' vs दीन "
  "(dīn) 'poor'; कुल (kul) 'family' vs कूल (kūl) 'cool, riverbank'. Consonants come in "
  "aspirated/unaspirated and voiced/voiceless sets: क (k, unaspirated, like 'sk' in "
  "'skill') vs ख (kh, aspirated, k plus a puff of air); ग (g) vs घ (gh, g plus breath). "
  "Hindi contrasts dental and retroflex sounds: त (ta, tongue on teeth) vs ट (ṭa, "
  "tongue curled back); द (da) vs ड (ḍa); न (na) vs ण (ṇa). Nasalized vowels (written "
  "with ँ or ं) change meaning: है (hai) 'is' vs हैं (haĩ) 'are (honorific)'. The "
  "written short 'a' is usually silent at the end of words (schwa deletion): राम is "
  "pronounced 'rām', not 'rāma'; नमस्ते is 'namaste', not 'namasate'. Stress falls "
  "naturally on long vowels and heavy syllables. Spoken examples with English "
  "approximations: टमाटर (ṭamāṭar) 'tomato' - say 'tuh-MAH-tuhr' with curled-tongue t; "
  "धन्यवाद (dhanyavād) 'thank you' - 'dhun-yuh-VAAD'; चाय (cāy) 'tea' - 'chaa-ee'; "
  "पानी (pānī) 'water' - 'paa-nee'; किताब (kitāb) 'book' - 'kih-TAAB'; दोस्त (dost) "
  "'friend' - 'dost'; बाज़ार (bāzār) 'market' - 'baa-ZAAR'; अच्छा (acchā) 'good' - "
  "'uch-CHHAA'; घर (ghar) 'house' - 'ghar' with breathy gh; स्कूल (skūl) 'school' - "
  "'skool'; नमस्ते (namaste) 'hello' - 'nuh-muh-STAY'."),
 "how_it_works": (
  "This record trains your ear and mouth: the 11 vowels with English approximations, "
  "the length contrasts that change meaning, the aspiration and retroflex contrasts "
  "with tongue-placement notes, nasalization, and schwa deletion - then 11 spoken "
  "example words, each with a say-it-like-this guide and a translation. Read each "
  "example aloud three times."),
 "key_points": [
  "11 vowel phonemes; vowel length is meaningful: कम 'less' vs काम 'work'.",
  "Aspiration contrast: क (k) vs ख (kh); ग (g) vs घ (gh).",
  "Dental vs retroflex contrast: त vs ट, द vs ड, न vs ण.",
  "Nasalized vowels change meaning: है 'is' vs हैं 'are (honorific)'.",
  "Final short 'a' is silent: राम is 'rām', नमस्ते is 'namaste'.",
  "Stress lands on long vowels and heavy syllables.",
  "धन्यवाद (dhanyavād) - 'thank you'; चाय (cāy) - 'tea'; घर (ghar) - 'house'.",
 ],
 "requirements": [
  "Practice minimal pairs aloud: कम/काम, दिन/दीन, कुल/कूल.",
  "Curl the tongue back for ट ठ ड ढ ण; keep it on the teeth for त थ द ध न.",
  "Add a puff of air for ख घ छ झ ठ ढ थ ध फ भ.",
 ],
 "standards": [
  "IPA transcription conventions for Indo-Aryan phonology",
  "ISO 15919:2001 transliteration of Devanagari",
 ],
 "citations": [
  "Ohala, Manjari. Hindi. In: Handbook of the International Phonetic Association. Cambridge University Press; 1999.",
  "Shapiro, Michael C. Hindi. In: Cardona & Jain (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens pronunciation becomes his original Signature sound "
  "instrument: every aspiration a breath he controls, every retroflex a tongue "
  "position he commands, every minimal pair a precision drill of the Signature "
  "method. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 4
{
 "key": "nouns1", "name": "Hindi Core Nouns I: People, Places, Things",
 "group": "Foundations", "ladder": 4, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "25 essential Hindi nouns - Devanagari, romanization, English, and one translated "
  "example sentence each. 1. आदमी (ādmī) 'man': वह आदमी मेरा दोस्त है (vah ādmī merā "
  "dost hai) - 'That man is my friend'. 2. औरत (aurat) 'woman': वह औरत डॉक्टर है (vah "
  "aurat ḍākṭar hai) - 'That woman is a doctor'. 3. बच्चा (baccā) 'child': बच्चा खेल "
  "रहा है (baccā khel rahā hai) - 'The child is playing'. 4. घर (ghar) 'house': मेरा "
  "घर बड़ा है (merā ghar baṛā hai) - 'My house is big'. 5. पानी (pānī) 'water': मुझे "
  "पानी चाहिए (mujhe pānī cāhie) - 'I need water'. 6. खाना (khānā) 'food': खाना गरम "
  "है (khānā garam hai) - 'The food is hot'. 7. किताब (kitāb) 'book': यह किताब मेरी "
  "है (yah kitāb merī hai) - 'This book is mine'. 8. स्कूल (skūl) 'school': बच्चा स्कूल "
  "जाता है (baccā skūl jātā hai) - 'The child goes to school'. 9. दोस्त (dost) "
  "'friend': वह मेरा दोस्त है (vah merā dost hai) - 'He is my friend'. 10. माँ (mā̃) "
  "'mother': मेरी माँ खाना बनाती है (merī mā̃ khānā banātī hai) - 'My mother cooks "
  "food'. 11. पिता (pitā) 'father': मेरे पिता काम करते हैं (mere pitā kām karte haĩ) "
  "- 'My father works'. 12. भाई (bhāī) 'brother': मेरा भाई दिल्ली में है (merā bhāī "
  "dillī mẽ hai) - 'My brother is in Delhi'. 13. बहन (bahan) 'sister': मेरी बहन पढ़ती "
  "है (merī bahan paṛhtī hai) - 'My sister studies'. 14. शहर (śahar) 'city': यह शहर "
  "बहुत बड़ा है (yah śahar bahut baṛā hai) - 'This city is very big'. 15. गाँव (gā̃v) "
  "'village': मेरा गाँव छोटा है (merā gā̃v choṭā hai) - 'My village is small'. 16. "
  "सड़क (saṛak) 'road': सड़क लंबी है (saṛak lambī hai) - 'The road is long'. 17. गाड़ी "
  "(gāṛī) 'car/vehicle': गाड़ी तेज़ चलती है (gāṛī tez caltī hai) - 'The car moves "
  "fast'. 18. पेड़ (peṛ) 'tree': पेड़ हरा है (peṛ harā hai) - 'The tree is green'. 19. "
  "फूल (phūl) 'flower': फूल सुंदर है (phūl sundar hai) - 'The flower is beautiful'. 20. "
  "सूरज (sūraj) 'sun': सूरज चमक रहा है (sūraj camak rahā hai) - 'The sun is shining'. "
  "21. चाँद (cā̃d) 'moon': चाँद रात में दिखता है (cā̃d rāt mẽ dikhtā hai) - 'The moon "
  "appears at night'. 22. तारा (tārā) 'star': आसमान में तारे हैं (āsmān mẽ tāre "
  "haĩ) - 'There are stars in the sky'. 23. दिन (din) 'day': आज अच्छा दिन है (āj "
  "acchā din hai) - 'Today is a good day'. 24. रात (rāt) 'night': रात ठंडी है (rāt "
  "ṭhaṇḍī hai) - 'The night is cold'. 25. समय (samay) 'time': समय बहुत कीमती है (samay "
  "bahut kīmtī hai) - 'Time is very precious'. Note: Hindi nouns have gender - "
  "आदमी, घर, पेड़ are masculine; औरत, किताब, सड़क are feminine - and adjectives "
  "agree with them (बड़ा घर, बड़ी सड़क)."),
 "how_it_works": (
  "Each of the 25 nouns is presented in four parts - Devanagari, romanization, "
  "English meaning, and a full translated sentence - so you learn the word inside a "
  "real sentence, not alone. The closing note introduces noun gender, which the "
  "grammar record explains fully. Say each sentence aloud, then cover the English "
  "and translate back."),
 "key_points": [
  "25 core nouns across people, places, things, and nature.",
  "Every noun: Devanagari + romanization + English + translated sentence.",
  "People: आदमी, औरत, बच्चा, दोस्त, माँ, पिता, भाई, बहन.",
  "Places: घर, स्कूल, शहर, गाँव, सड़क. Things: पानी, खाना, किताब, गाड़ी.",
  "Nature: पेड़, फूल, सूरज, चाँद, तारा, दिन, रात, समय.",
  "Hindi nouns have masculine/feminine gender; adjectives agree with it.",
  "मेरा घर बड़ा है (merā ghar baṛā hai) - 'My house is big'.",
 ],
 "requirements": [
  "Read each sentence aloud using the romanization.",
  "Memorize the 25 nouns before moving to verbs.",
  "Notice which nouns take बड़ा and which take बड़ी - that is gender at work.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
  "Unicode Standard, Devanagari block U+0900-U+097F",
 ],
 "citations": [
  "McGregor, R. S. The Oxford Hindi-English Dictionary. Oxford University Press; 1993.",
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens these 25 nouns are his original Signature naming "
  "instrument: the first words he gives things, each one a label struck in the "
  "Signature system and drilled until it answers on call. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 5
{
 "key": "verbs1", "name": "Hindi Core Verbs I: Essential Actions",
 "group": "Foundations", "ladder": 5, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "25 essential Hindi verbs - Devanagari, romanization, English, and one translated "
  "example sentence each. Hindi verb stems take endings for tense and agreement; the "
  "sentences below show the everyday present forms. 1. जाना (jānā) 'to go': मैं स्कूल "
  "जाता हूँ (maĩ skūl jātā hū̃) - 'I go to school'. 2. आना (ānā) 'to come': वह कल "
  "आएगा (vah kal āegā) - 'He will come tomorrow'. 3. खाना (khānā) 'to eat': मैं खाना "
  "खाता हूँ (maĩ khānā khātā hū̃) - 'I eat food'. 4. पीना (pīnā) 'to drink': वह चाय "
  "पीता है (vah cāy pītā hai) - 'He drinks tea'. 5. करना (karnā) 'to do': मैं काम करता "
  "हूँ (maĩ kām kartā hū̃) - 'I do work'. 6. बोलना (bolnā) 'to speak': वह हिन्दी बोलता "
  "है (vah hindī boltā hai) - 'He speaks Hindi'. 7. पढ़ना (paṛhnā) 'to read/study': "
  "मैं किताब पढ़ता हूँ (maĩ kitāb paṛhtā hū̃) - 'I read a book'. 8. लिखना (likhnā) "
  "'to write': वह पत्र लिखती है (vah patra likhtī hai) - 'She writes a letter'. 9. "
  "देखना (dekhnā) 'to see/watch': मैं फिल्म देखता हूँ (maĩ philm dekhtā hū̃) - 'I "
  "watch a film'. 10. सुनना (sunnā) 'to listen': वह गाना सुनती है (vah gānā suntī "
  "hai) - 'She listens to a song'. 11. सोना (sonā) 'to sleep': बच्चा सोता है (baccā "
  "sotā hai) - 'The child sleeps'. 12. उठना (uṭhnā) 'to wake up/get up': मैं सुबह "
  "उठता हूँ (maĩ subah uṭhtā hū̃) - 'I wake up in the morning'. 13. बैठना (baiṭhnā) "
  "'to sit': वह कुर्सी पर बैठता है (vah kursī par baiṭhtā hai) - 'He sits on the "
  "chair'. 14. चलना (calnā) 'to walk/move': हम पार्क में चलते हैं (ham pārk mẽ calte "
  "haĩ) - 'We walk in the park'. 15. दौड़ना (dauṛnā) 'to run': लड़का तेज़ दौड़ता है "
  "(laṛkā tez dauṛtā hai) - 'The boy runs fast'. 16. देना (denā) 'to give': वह मुझे "
  "किताब देता है (vah mujhe kitāb detā hai) - 'He gives me a book'. 17. लेना (lenā) "
  "'to take': मैं पैसे लेता हूँ (maĩ paise letā hū̃) - 'I take the money'. 18. "
  "खरीदना (kharīdnā) 'to buy': वह सब्ज़ी खरीदती है (vah sabzī kharīdtī hai) - 'She "
  "buys vegetables'. 19. बेचना (becnā) 'to sell': दुकानदार फल बेचता है (dukāndār phal "
  "bectā hai) - 'The shopkeeper sells fruit'. 20. बनाना (banānā) 'to make': माँ खाना "
  "बनाती है (mā̃ khānā banātī hai) - 'Mother makes food'. 21. खेलना (khelnā) 'to "
  "play': बच्चे खेलते हैं (bacce khelte haĩ) - 'The children play'. 22. हँसना "
  "(hãsnā) 'to laugh': वह ज़ोर से हँसता है (vah zor se hãstā hai) - 'He laughs "
  "loudly'. 23. रोना (ronā) 'to cry': बच्चा रोता है (baccā rotā hai) - 'The child "
  "cries'. 24. समझना (samajhnā) 'to understand': मैं समझता हूँ (maĩ samajhtā hū̃) "
  "- 'I understand'. 25. मदद करना (madad karnā) 'to help': वह मेरी मदद करता है (vah "
  "merī madad kartā hai) - 'He helps me'. Note the pattern: the stem (जा, खा, कर) "
  "takes -ता/-ती + है/हूँ/हैं for the habitual present, agreeing with the subject's "
  "gender and number."),
 "how_it_works": (
  "Each verb appears with its dictionary form (the -ना infinitive), its English "
  "meaning, and a translated sentence showing it in the everyday present tense. The "
  "closing note reveals the stem + ending pattern that all 25 share. Learn the "
  "stems now; the tenses record will build every other form on them."),
 "key_points": [
  "25 core verbs, each with Devanagari + romanization + English + sentence.",
  "Dictionary form ends in -ना: जाना, खाना, करना, बोलना, पढ़ना.",
  "Habitual present pattern: stem + ता/ती + है/हूँ/हैं (मैं जाता हूँ, वह जाती है).",
  "Endings agree with the subject's gender and number.",
  "Compound verbs like मदद करना ('to help') use करना as the helper.",
  "मैं समझता हूँ (maĩ samajhtā hū̃) - 'I understand'.",
 ],
 "requirements": [
  "Learn each verb's stem by dropping -ना.",
  "Say every sentence aloud; swap मैं for वह and change the ending.",
  "Master these 25 stems - the tense system is built on them.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
  "IAST transliteration for verb stems",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003. Verb chapters.",
  "Shapiro, Michael C. Hindi. In: Cardona & Jain (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens these 25 verbs are his original Signature action "
  "instrument: the stems are the handles, the endings the gears, and every sentence "
  "a machine he starts with his own hand. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 6
{
 "key": "adjadv", "name": "Hindi Adjectives and Adverbs",
 "group": "Foundations", "ladder": 6, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "25 adjectives and 15 adverbs with translated example sentences, plus the agreement "
  "rule. Adjectives ending in -ा (ā) inflect: बड़ा (baṛā) 'big' becomes बड़ी (baṛī) "
  "before feminine nouns and बड़े (baṛe) before masculine plurals; other adjectives "
  "like खुश (khuś) 'happy' never change. ADJECTIVES: 1. बड़ा (baṛā) 'big': बड़ा घर "
  "(baṛā ghar) - 'big house'; बड़ी किताब (baṛī kitāb) - 'big book'. 2. छोटा (choṭā) "
  "'small': छोटा बच्चा (choṭā baccā) - 'small child'. 3. अच्छा (acchā) 'good': अच्छा "
  "लड़का (acchā laṛkā) - 'good boy'; अच्छी लड़की (acchī laṛkī) - 'good girl'. 4. बुरा "
  "(burā) 'bad': बुरा दिन (burā din) - 'bad day'. 5. नया (nayā) 'new': नयी गाड़ी "
  "(nayī gāṛī) - 'new car'. 6. पुराना (purānā) 'old': पुराना घर (purānā ghar) - 'old "
  "house'. 7. लंबा (lambā) 'long/tall': लंबी सड़क (lambī saṛak) - 'long road'. 8. "
  "गर्म (garm) 'hot': गर्म चाय (garm cāy) - 'hot tea'. 9. ठंडा (ṭhaṇḍā) 'cold': ठंडा "
  "पानी (ṭhaṇḍā pānī) - 'cold water'. 10. मीठा (mīṭhā) 'sweet': मीठा आम (mīṭhā ām) "
  "- 'sweet mango'. 11. खट्टा (khaṭṭā) 'sour': खट्टा नींबू (khaṭṭā nīmbū) - 'sour "
  "lemon'. 12. तेज़ (tez) 'fast': तेज़ गाड़ी (tez gāṛī) - 'fast car'. 13. धीमा (dhīmā) "
  "'slow': धीमा काम (dhīmā kām) - 'slow work'. 14. सुंदर (sundar) 'beautiful': सुंदर "
  "फूल (sundar phūl) - 'beautiful flower'. 15. साफ़ (sāf) 'clean': साफ़ कपड़े (sāf "
  "kapaṛe) - 'clean clothes'. 16. गंदा (gandā) 'dirty': गंदे हाथ (gande hāth) - "
  "'dirty hands'. 17. आसान (āsān) 'easy': आसान सवाल (āsān savāl) - 'easy question'. "
  "18. मुश्किल (muśkil) 'difficult': मुश्किल काम (muśkil kām) - 'difficult work'. 19. "
  "खुश (khuś) 'happy': खुश बच्चा (khuś baccā) - 'happy child'; खुश लड़की (khuś "
  "laṛkī) - 'happy girl' (no change). 20. दुखी (dukhī) 'sad': दुखी आदमी (dukhī ādmī) "
  "- 'sad man'. 21. अमीर (amīr) 'rich': अमीर लोग (amīr log) - 'rich people'. 22. "
  "गरीब (garīb) 'poor': गरीब किसान (garīb kisān) - 'poor farmer'. 23. मजबूत (majbūt) "
  "'strong': मजबूत पेड़ (majbūt peṛ) - 'strong tree'. 24. कमजोर (kamzor) 'weak': "
  "कमजोर दीवार (kamzor dīvār) - 'weak wall'. 25. महँगा (mahãgā) 'expensive': महँगी "
  "घड़ी (mahãgī ghaṛī) - 'expensive watch'. ADVERBS (never inflect): 1. बहुत (bahut) "
  "'very': वह बहुत अच्छा है (vah bahut acchā hai) - 'He is very good'. 2. जल्दी "
  "(jaldī) 'quickly': जल्दी आओ (jaldī āo) - 'Come quickly'. 3. धीरे (dhīre) "
  "'slowly': धीरे बोलो (dhīre bolo) - 'Speak slowly'. 4. हमेशा (hameśā) 'always': वह "
  "हमेशा सच बोलता है (vah hameśā sac boltā hai) - 'He always speaks the truth'. 5. "
  "कभी (kabhī) 'sometimes': मैं कभी-कभी जाता हूँ (maĩ kabhī-kabhī jātā hū̃) - 'I go "
  "sometimes'. 6. कभी नहीं (kabhī nahī̃) 'never': वह कभी नहीं आता (vah kabhī nahī̃ "
  "ātā) - 'He never comes'. 7. यहाँ (yahā̃) 'here': यहाँ बैठो (yahā̃ baiṭho) - 'Sit "
  "here'. 8. वहाँ (vahā̃) 'there': वह वहाँ रहता है (vah vahā̃ rahtā hai) - 'He lives "
  "there'. 9. अंदर (andar) 'inside': अंदर आओ (andar āo) - 'Come inside'. 10. बाहर "
  "(bāhar) 'outside': बाहर जाओ (bāhar jāo) - 'Go outside'. 11. ऊपर (ūpar) "
  "'up/above': ऊपर देखो (ūpar dekho) - 'Look up'. 12. नीचे (nīce) 'down/below': नीचे "
  "उतरो (nīce utro) - 'Go down'. 13. आज (āj) 'today': आज छुट्टी है (āj chuṭṭī hai) - "
  "'Today is a holiday'. 14. कल (kal) 'tomorrow/yesterday': मैं कल आऊँगा (maĩ kal "
  "āū̃gā) - 'I will come tomorrow'. 15. अब (ab) 'now': अब चलो (ab calo) - 'Let's go "
  "now'."),
 "how_it_works": (
  "Adjectives come first with the agreement rule stated up front and demonstrated in "
  "every -ा adjective pair (बड़ा घर / बड़ी किताब); adverbs follow with the note that "
  "they never change. Each item carries Devanagari, romanization, English, and a "
  "translated sentence. Practice by describing five things around you."),
 "key_points": [
  "25 adjectives + 15 adverbs, each with a translated example sentence.",
  "Adjectives in -ा inflect: बड़ा/बड़ी/बड़े; others like खुश never change.",
  "Adjectives come BEFORE the noun: अच्छा लड़का, बड़ी किताब.",
  "Adverbs never inflect: बहुत, जल्दी, धीरे, हमेशा, कभी.",
  "कल means both 'tomorrow' and 'yesterday' - context decides.",
  "वह बहुत अच्छा है (vah bahut acchā hai) - 'He is very good'.",
 ],
 "requirements": [
  "Learn the -ा agreement pattern: masculine बड़ा, feminine बड़ी, plural बड़े.",
  "Describe ten objects around you with an adjective + noun.",
  "Use each adverb in one spoken sentence.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
  "IAST transliteration for inflected forms",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003. Adjective chapter.",
  "McGregor, R. S. The Oxford Hindi-English Dictionary. Oxford University Press; 1993.",
 ],
 "sig_lens": (
  "Through the Signature lens adjectives and adverbs are his original Signature "
  "coloring instrument: the -ा ending a dial he turns for gender and number, the "
  "adverbs fixed brushes that never change shape. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 7
{
 "key": "pronouns", "name": "Hindi Pronouns: Full Paradigms",
 "group": "Foundations", "ladder": 7, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Personal, possessive, demonstrative, and interrogative pronouns with full paradigms "
  "and translated example sentences. PERSONAL: मैं (maĩ) 'I': मैं जाता हूँ (maĩ "
  "jātā hū̃) - 'I go'. तुम (tum) 'you (informal/intimate)': तुम कहाँ हो (tum kahā̃ ho) "
  "- 'Where are you'. आप (āp) 'you (formal/respectful)': आप कैसे हैं (āp kaise haĩ) "
  "- 'How are you (formal)'. वह (vah) 'he/she/that': वह आता है (vah ātā hai) - 'He "
  "comes'. यह (yah) 'this (he/she)': यह मेरी बहन है (yah merī bahan hai) - 'She is my "
  "sister'. हम (ham) 'we': हम खेलते हैं (ham khelte haĩ) - 'We play'. वे (ve) "
  "'they': वे पढ़ते हैं (ve paṛhte haĩ) - 'They study'. Oblique forms before "
  "postpositions: मुझ (mujh) 'me', तुझ (tujh) 'you (inf)', उस (us) 'him/her', इस (is) "
  "'this', हम (ham) 'us', उन (un) 'them' - e.g. मुझको दो (mujhko do) - 'Give me'. "
  "POSSESSIVE (agree like -ा adjectives): मेरा/मेरी/मेरे (merā/merī/mere) 'my': मेरा घर "
  "(merā ghar) - 'my house'; मेरी किताब (merī kitāb) - 'my book'. तुम्हारा (tumhārā) "
  "'your (inf)'; आपका (āpkā) 'your (formal)'; उसका (uskā) 'his/her'; इसका (iskā) "
  "'its/this one's'; हमारा (hamārā) 'our': हमारा देश (hamārā deś) - 'our country'; "
  "उनका (unkā) 'their': उनका काम (unkā kām) - 'their work'. DEMONSTRATIVE: यह (yah) "
  "'this': यह अच्छा है (yah acchā hai) - 'This is good'. वह (vah) 'that': वह बुरा है "
  "(vah burā hai) - 'That is bad'. ये (ye) 'these': ये फूल हैं (ye phūl haĩ) - 'These "
  "are flowers'. वे (ve) 'those': वे पेड़ हैं (ve peṛ haĩ) - 'Those are trees'. "
  "INTERROGATIVE: कौन (kaun) 'who': वह कौन है (vah kaun hai) - 'Who is he'. क्या (kyā) "
  "'what': यह क्या है (yah kyā hai) - 'What is this'. कहाँ (kahā̃) 'where': तुम कहाँ "
  "हो (tum kahā̃ ho) - 'Where are you'. कब (kab) 'when': वह कब आएगा (vah kab āegā) - "
  "'When will he come'. क्यों (kyõ) 'why': तुम क्यों रोते हो (tum kyõ rote ho) - "
  "'Why do you cry'. कैसे (kaise) 'how': आप कैसे हैं (āp kaise haĩ) - 'How are you'. "
  "कितना (kitnā) 'how much/many': यह कितने का है (yah kitne kā hai) - 'How much is "
  "this'. कौन-सा (kaun-sā) 'which': कौन-सी किताब (kaun-sī kitāb) - 'which book'. Rule "
  "of respect: आप takes plural verb forms (आप जाते हैं), तुम takes its own form (तुम "
  "जाते हो), and तू (tū, very intimate) exists but learners should use तुम/आप."),
 "how_it_works": (
  "Pronouns are taught as four tables - personal, possessive, demonstrative, "
  "interrogative - each cell with Devanagari, romanization, English, and a translated "
  "sentence. The respect rule (आप vs तुम) is stated plainly. Drill by replacing nouns "
  "in earlier sentences with pronouns."),
 "key_points": [
  "Three levels of 'you': तू (very intimate), तुम (informal), आप (formal/respectful).",
  "आप always takes plural verb forms: आप जाते हैं.",
  "Possessives agree like -ा adjectives: मेरा घर, मेरी किताब, मेरे दोस्त.",
  "Oblique forms before postpositions: मुझको, उसको, इनको.",
  "यह/ये = this/these (near); वह/वे = that/those (far).",
  "Question words: कौन, क्या, कहाँ, कब, क्यों, कैसे, कितना.",
  "आप कैसे हैं (āp kaise haĩ) - 'How are you (formal)'.",
 ],
 "requirements": [
  "Use आप with elders and strangers; तुम with friends and juniors.",
  "Drill possessives with ten of your own belongings.",
  "Memorize the question words - they unlock every conversation.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
  "IAST transliteration for paradigm tables",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003. Pronoun chapters.",
  "Shapiro, Michael C. Hindi. In: Cardona & Jain (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens pronouns are his original Signature pointing "
  "instrument: मैं the self he speaks from, आप the respect he extends, कौन the "
  "question he aims - each one a finger pointing in the Signature system. "
  "Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 8
{
 "key": "numbers", "name": "Hindi Numbers, Time, Days, and Dates",
 "group": "Foundations", "ladder": 8, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Numbers 1-100, ordinals, days, months, seasons, clock time, and dates - each with "
  "example sentences. NUMBERS 1-10: एक (ek) 1, दो (do) 2, तीन (tīn) 3, चार (cār) 4, "
  "पाँच (pā̃c) 5, छह (chah) 6, सात (sāt) 7, आठ (āṭh) 8, नौ (nau) 9, दस (das) 10. "
  "11-20: ग्यारह (gyārah) 11, बारह (bārah) 12, तेरह (terah) 13, चौदह (caudah) 14, "
  "पंद्रह (pandrah) 15, सोलह (solah) 16, सत्रह (satrah) 17, अठारह (aṭhārah) 18, "
  "उन्नीस (unnīs) 19, बीस (bīs) 20. Tens: तीस (tīs) 30, चालीस (cālīs) 40, पचास "
  "(pacās) 50, साठ (sāṭh) 60, सत्तर (sattar) 70, अस्सी (assī) 80, नब्बे (nabbe) 90, "
  "सौ (sau) 100. Note: 21-29, 31-39 etc. have unique forms (इक्कीस ikkīs 21, बाईस "
  "bāīs 22...); learn them as words, not formulas. Example: मेरे पास तीन किताबें हैं "
  "(mere pās tīn kitābẽ haĩ) - 'I have three books'. ORDINALS: पहला (pehlā) "
  "'first', दूसरा (dūsrā) 'second', तीसरा (tīsrā) 'third': यह पहला पाठ है (yah pehlā "
  "pāṭh hai) - 'This is the first lesson'. DAYS: सोमवार (somvār) Monday, मंगलवार "
  "(maṅgalvār) Tuesday, बुधवार (budhvār) Wednesday, गुरुवार (guruvār) Thursday, "
  "शुक्रवार (śukravār) Friday, शनिवार (śanivār) Saturday, रविवार (ravivār) Sunday: आज "
  "सोमवार है (āj somvār hai) - 'Today is Monday'. MONTHS: जनवरी (janvarī), फ़रवरी "
  "(farvarī), मार्च (mārc), अप्रैल (aprail), मई (maī), जून (jūn), जुलाई (julāī), अगस्त "
  "(agast), सितंबर (sitambar), अक्टूबर (akṭūbar), नवंबर (navambar), दिसंबर (disambar): "
  "मेरा जन्मदिन जून में है (merā janmadin jūn mẽ hai) - 'My birthday is in June'. "
  "SEASONS: वसंत (vasant) spring, ग्रीष्म (grīṣma) summer, वर्षा (varṣā) monsoon, शरद "
  "(śarad) autumn, हेमंत (hemant) pre-winter, शिशिर (śiśir) winter: वर्षा में बारिश "
  "होती है (varṣā mẽ bāriś hotī hai) - 'It rains in the monsoon'. CLOCK TIME: बजा "
  "(bajā) 'o'clock': एक बजा (ek bajā) 'one o'clock'; सवा (savā) 'quarter past': सवा "
  "दो (savā do) 'quarter past two'; साढ़े (sāṛhe) 'half past': साढ़े तीन (sāṛhe tīn) "
  "'half past three'; पौने (paune) 'quarter to': पौने चार (paune cār) 'quarter to "
  "four'. अब तीन बजे हैं (ab tīn baje haĩ) - 'It is three o'clock now'. DATES: 15 "
  "अगस्त (15 agast) '15th August': स्वतंत्रता दिवस 15 अगस्त को है (svatantratā divas "
  "15 agast ko hai) - 'Independence Day is on 15th August'. Year example: सन् 2026 "
  "(san 2026) 'the year 2026'."),
 "how_it_works": (
  "Numbers are given in learnable blocks (1-10, 11-20, tens) with the warning that "
  "21-99 are individual words to memorize; ordinals, days, months, seasons, clock "
  "time, and dates follow, each with translated sentences. Count aloud 1-20 daily "
  "until it is automatic."),
 "key_points": [
  "1-20 and the tens are the core: एक दो तीन... बीस, तीस, चालीस... सौ.",
  "21-99 have unique forms (इक्कीस 21, बाईस 22) - learn as words.",
  "Ordinals: पहला, दूसरा, तीसरा.",
  "Days: सोमवार to रविवार; months: जनवरी to दिसंबर.",
  "Six seasons: वसंत, ग्रीष्म, वर्षा, शरद, हेमंत, शिशिर.",
  "Time: सवा (quarter past), साढ़े (half past), पौने (quarter to).",
  "अब तीन बजे हैं (ab tīn baje haĩ) - 'It is three o'clock now'.",
 ],
 "requirements": [
  "Count 1-20 aloud every day for a week.",
  "Say today's day, date, and time in Hindi each morning.",
  "Learn the six season names - they structure the Indian year.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
  "Devanagari digits U+0966-U+096F",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003. Number chapter.",
  "McGregor, R. S. The Oxford Hindi-English Dictionary. Oxford University Press; 1993.",
 ],
 "sig_lens": (
  "Through the Signature lens numbers are his original Signature counting "
  "instrument: एक the first mark, सौ the hundred-mark, the clock words the gears "
  "that tell his day - every number a notch he cuts himself. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 9
{
 "key": "greetings", "name": "Hindi Greetings and Everyday Phrases",
 "group": "Foundations", "ladder": 9, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "30 greetings, farewells, and politeness phrases - Hindi, romanization, English, "
  "and usage notes. 1. नमस्ते (namaste) 'hello/greetings' - the universal greeting, "
  "palms together. 2. नमस्कार (namaskār) 'greetings' - slightly more formal. 3. शुभ "
  "प्रभात (śubh prabhāt) 'good morning'. 4. शुभ संध्या (śubh sandhyā) 'good evening'. "
  "5. शुभ रात्रि (śubh rātri) 'good night'. 6. आप कैसे हैं (āp kaise haĩ) 'how are "
  "you (formal)'. 7. तुम कैसे हो (tum kaise ho) 'how are you (informal)'. 8. मैं ठीक "
  "हूँ (maĩ ṭhīk hū̃) 'I am fine'. 9. सब ठीक है (sab ṭhīk hai) 'all is well'. 10. "
  "धन्यवाद (dhanyavād) 'thank you'. 11. शुक्रिया (śukriyā) 'thanks'. 12. बहुत-बहुत "
  "धन्यवाद (bahut-bahut dhanyavād) 'thank you very much'. 13. कृपया (kṛpayā) "
  "'please'. 14. माफ़ कीजिए (māf kījie) 'excuse me / forgive me (formal)'. 15. माफ़ "
  "करना (māf karnā) 'excuse me (informal)'. 16. कोई बात नहीं (koī bāt nahī̃) 'no "
  "problem / you are welcome'. 17. आपका स्वागत है (āpkā svāgat hai) 'you are "
  "welcome (formal)'. 18. फिर मिलेंगे (phir milẽge) 'we will meet again'. 19. अलविदा "
  "(alvidā) 'farewell'. 20. बहुत खुशी हुई (bahut khuśī huī) 'very pleased to meet "
  "you'. 21. आपसे मिलकर खुशी हुई (āpse milkar khuśī huī) 'pleased to meet you'. 22. "
  "बधाई हो (badhāī ho) 'congratulations'. 23. शुभकामनाएँ (śubhkāmnāẽ) 'best "
  "wishes'. 24. आइए (āie) 'please come in'. 25. बैठिए (baiṭhie) 'please sit'. 26. "
  "चाय पिएँगे (cāy piyẽge) 'will you have tea' - the classic offer of hospitality. "
  "27. जी हाँ (jī hā̃) 'yes (respectful)'. 28. जी नहीं (jī nahī̃) 'no (respectful)'. "
  "29. ठीक है (ṭhīk hai) 'okay / all right'. 30. आपका दिन शुभ हो (āpkā din śubh ho) "
  "'have a good day'. Usage rule: add जी (jī) after names for respect - हाँ जी, "
  "राम जी. Use the -इए forms (आइए, बैठिए, कीजिए) with anyone you would call आप."),
 "how_it_works": (
  "Each phrase comes with its pronunciation, English meaning, and a usage note "
  "telling you exactly when to say it. Learn 1-10 first (survival set), then 11-20 "
  "(politeness set), then 21-30 (warmth set). Practice by greeting someone in Hindi "
  "tomorrow."),
 "key_points": [
  "नमस्ते is the universal greeting; नमस्कार is more formal.",
  "जी adds respect: हाँ जी, राम जी.",
  "-इए verb forms (आइए, बैठिए) match आप-level politeness.",
  "चाय पिएँगे - offering tea is the classic Hindi hospitality move.",
  "कोई बात नहीं covers both 'no problem' and 'you are welcome'.",
  "फिर मिलेंगे (phir milẽge) - 'we will meet again' - the warm farewell.",
 ],
 "requirements": [
  "Memorize phrases 1-10 cold - they cover daily survival.",
  "Use जी with every name for one full day.",
  "Offer someone tea with चाय पिएँगे this week.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens greetings are his original Signature opening "
  "instrument: नमस्ते the door he opens, जी the respect he stamps on a name, चाय "
  "पिएँगे the hospitality he extends - every phrase a handshake of the Signature "
  "method. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 10
{
 "key": "grammar", "name": "Hindi Grammar Essentials",
 "group": "Foundations", "ladder": 10, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The core grammar rules, each with translated example sentences. WORD ORDER is "
  "subject-object-verb: मैं किताब पढ़ता हूँ (maĩ kitāb paṛhtā hū̃) - 'I read a book' "
  "(literally 'I book read'). Questions keep SOV too: तुम क्या खाते हो (tum kyā khāte "
  "ho) - 'What do you eat'. GENDER: every noun is masculine or feminine. Masculine: "
  "लड़का (laṛkā) 'boy', घर (ghar) 'house', पेड़ (peṛ) 'tree'. Feminine: लड़की (laṛkī) "
  "'girl', किताब (kitāb) 'book', सड़क (saṛak) 'road'. Adjectives and verbs agree: "
  "अच्छा लड़का (acchā laṛkā) 'good boy' vs अच्छी लड़की (acchī laṛkī) 'good girl'. "
  "NUMBER: singular/plural - लड़का/लड़के (laṛkā/laṛke) 'boy/boys', लड़की/लड़कियाँ "
  "(laṛkī/laṛkiyā̃) 'girl/girls'. POSTPOSITIONS (Hindi uses postpositions, not "
  "prepositions): ने (ne) marks the doer in perfective past: राम ने खाना खाया (rām ne "
  "khānā khāyā) - 'Ram ate food'. को (ko) marks the object/recipient: मुझको दो "
  "(mujhko do) - 'Give me'; राम को बुलाओ (rām ko bulāo) - 'Call Ram'. से (se) 'from / "
  "with / by': दिल्ली से (dillī se) - 'from Delhi'; चम्मच से (cammac se) - 'with a "
  "spoon'. में (mẽ) 'in': घर में (ghar mẽ) - 'in the house'. पर (par) 'on': मेज़ पर "
  "(mez par) - 'on the table'. का/की/के (kā/kī/ke) 'of', agreeing with the following "
  "noun: राम का घर (rām kā ghar) - 'Ram's house'; सीता की किताब (sītā kī kitāb) - "
  "'Sita's book'. ARTICLES: Hindi has no 'the'; एक (ek) 'one' works like 'a': एक "
  "लड़का (ek laṛkā) - 'a boy'. NEGATION: नहीं (nahī̃) 'not': मैं नहीं जाता (maĩ "
  "nahī̃ jātā) - 'I do not go'. न (na) with commands: मत जाओ (mat jāo) - 'don't go'. "
  "QUESTIONS: क्या (kyā) at the start makes a yes/no question: क्या तुम आओगे (kyā "
  "tum āoge) - 'Will you come'; question words ask directly: वह कहाँ है (vah kahā̃ "
  "hai) - 'Where is he'; rising intonation alone can ask: तुम जाते हो (tum jāte ho) "
  "- 'Are you going'. है/हैं/हूँ (hai/haĩ/hū̃) 'is/are/am' anchor the present: मैं "
  "खुश हूँ (maĩ khuś hū̃) - 'I am happy'; वे खुश हैं (ve khuś haĩ) - 'They are "
  "happy'."),
 "how_it_works": (
  "Seven grammar stations - word order, gender, number, postpositions, articles, "
  "negation, questions - each stated as a rule and proved with translated sentences. "
  "Work them in order and make one sentence of your own per station."),
 "key_points": [
  "SOV word order: मैं किताब पढ़ता हूँ - 'I read a book'.",
  "Every noun is masculine or feminine; adjectives and verbs agree.",
  "Postpositions follow the noun: ने, को, से, में, पर, का/की/के.",
  "No 'the'; एक works as 'a'.",
  "नहीं negates statements; मत negates commands.",
  "क्या starts yes/no questions; question words ask directly.",
  "राम ने खाना खाया (rām ne khānā khāyā) - 'Ram ate food' shows ने in action.",
 ],
 "requirements": [
  "Write five SOV sentences of your own.",
  "Drill का/की/के with ten possessions.",
  "Say every example sentence aloud twice.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
  "IAST transliteration for grammatical examples",
 ],
 "citations": [
  "Shapiro, Michael C. Hindi. In: Cardona & Jain (eds.) The Indo-Aryan Languages. Routledge; 2003.",
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens grammar is his original Signature machine shop: SOV "
  "the assembly order, gender the two molds, postpositions the fasteners that bolt "
  "meaning together, ने the stamp of the doer - every rule a tool he owns. "
  "Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 11
{
 "key": "home", "name": "Hindi Sentences: Home and Family",
 "group": "Compounded", "ladder": 11, "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "20 sentences about the house, rooms, furniture, and family members - Hindi, "
  "romanization, and English. 1. यह मेरा घर है (yah merā ghar hai) - 'This is my "
  "house'. 2. घर में चार कमरे हैं (ghar mẽ cār kamre haĩ) - 'There are four rooms in "
  "the house'. 3. रसोई में माँ खाना बनाती है (rasoī mẽ mā̃ khānā banātī hai) - "
  "'Mother cooks food in the kitchen'. 4. बैठक में सोफ़ा है (baiṭhak mẽ sofā hai) - "
  "'There is a sofa in the living room'. 5. मेरे कमरे में एक मेज़ है (mere kamre mẽ "
  "ek mez hai) - 'There is a table in my room'. 6. कुर्सी मेज़ के पास है (kursī mez "
  "ke pās hai) - 'The chair is near the table'. 7. खिड़की से धूप आती है (khiṛkī se "
  "dhūp ātī hai) - 'Sunlight comes through the window'. 8. दरवाज़ा बंद करो (darvāzā "
  "band karo) - 'Close the door'. 9. बिस्तर नरम है (bistar naram hai) - 'The bed is "
  "soft'. 10. अलमारी में कपड़े हैं (almārī mẽ kapaṛe haĩ) - 'There are clothes in "
  "the wardrobe'. 11. मेरे पिता दफ़्तर जाते हैं (mere pitā daftar jāte haĩ) - 'My "
  "father goes to the office'. 12. मेरी माँ बहुत अच्छी है (merī mā̃ bahut acchī hai) "
  "- 'My mother is very good'. 13. मेरा भाई मुझसे बड़ा है (merā bhāī mujhse baṛā "
  "hai) - 'My brother is older than me'. 14. मेरी बहन स्कूल जाती है (merī bahan skūl "
  "jātī hai) - 'My sister goes to school'. 15. दादा बगीचे में बैठते हैं (dādā bagīce "
  "mẽ baiṭhte haĩ) - 'Grandfather sits in the garden'. 16. दादी कहानी सुनाती है "
  "(dādī kahānī sunātī hai) - 'Grandmother tells a story'. 17. हम सब साथ खाना खाते "
  "हैं (ham sab sāth khānā khāte haĩ) - 'We all eat food together'. 18. मेरा परिवार "
  "बड़ा है (merā parivār baṛā hai) - 'My family is big'. 19. घर के सामने पेड़ है (ghar "
  "ke sāmne peṛ hai) - 'There is a tree in front of the house'. 20. यह तस्वीर मेरे "
  "परिवार की है (yah tasvīr mere parivār kī hai) - 'This photo is of my family'. "
  "Family words to keep: दादा (dādā) paternal grandfather, दादी (dādī) paternal "
  "grandmother, नाना (nānā) maternal grandfather, नानी (nānī) maternal grandmother, "
  "चाचा (cācā) paternal uncle, मामा (māmā) maternal uncle."),
 "how_it_works": (
  "Twenty full sentences walk you through a Hindi home - rooms, furniture, daily "
  "actions, and the family members in it - each with romanization and translation. "
  "Read them in order as a tour of the house, then describe your own home in five "
  "Hindi sentences."),
 "key_points": [
  "20 home-and-family sentences with full translations.",
  "Room words: कमरा (room), रसोई (kitchen), बैठक (living room), बगीचा (garden).",
  "Furniture words: मेज़, कुर्सी, सोफ़ा, बिस्तर, अलमारी, खिड़की, दरवाज़ा.",
  "Family words: माँ, पिता, भाई, बहन, दादा, दादी, नाना, नानी, चाचा, मामा.",
  "में = in, पर = on, के सामने = in front of, के पास = near.",
  "हम सब साथ खाना खाते हैं - 'We all eat food together'.",
 ],
 "requirements": [
  "Say all 20 sentences aloud.",
  "Describe your own home in five Hindi sentences.",
  "Name every family member in Hindi from memory.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens the home set is his original Signature household "
  "instrument: every room a chamber of the Signature house, every family word a "
  "name he calls across it. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 12
{
 "key": "food", "name": "Hindi Sentences: Food and Cooking",
 "group": "Compounded", "ladder": 12, "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "20 sentences about meals, ingredients, cooking actions, and restaurants. 1. मुझे "
  "भूख लगी है (mujhe bhūkh lagī hai) - 'I am hungry'. 2. नाश्ते में पराठा खाओ "
  "(nāśte mẽ parāṭhā khāo) - 'Eat paratha for breakfast'. 3. दोपहर का खाना तैयार है "
  "(dopahar kā khānā taiyār hai) - 'Lunch is ready'. 4. रात का खाना आठ बजे खाएँगे "
  "(rāt kā khānā āṭh baje khāẽge) - 'We will eat dinner at eight'. 5. दाल में नमक "
  "कम है (dāl mẽ namak kam hai) - 'There is less salt in the lentils'. 6. रोटी गरम "
  "है (roṭī garam hai) - 'The bread is hot'. 7. चावल के साथ सब्ज़ी खाओ (cāval ke "
  "sāth sabzī khāo) - 'Eat vegetables with rice'. 8. माँ दाल बनाती है (mā̃ dāl "
  "banātī hai) - 'Mother makes lentils'. 9. पानी उबालो (pānī ubālo) - 'Boil the "
  "water'. 10. सब्ज़ी काटो (sabzī kāṭo) - 'Cut the vegetables'. 11. मसाले डालो "
  "(masāle ḍālo) - 'Add the spices'. 12. खाना मीठा है (khānā mīṭhā hai) - 'The food "
  "is sweet'. 13. यह खाना तीखा है (yah khānā tīkhā hai) - 'This food is spicy'. 14. "
  "मुझे आम पसंद है (mujhe ām pasand hai) - 'I like mangoes'. 15. एक कप चाय लाओ (ek "
  "kap cāy lāo) - 'Bring a cup of tea'. 16. रेस्टोरेंट में खाना खाएँगे (resṭorẽṭ "
  "mẽ khānā khāẽge) - 'We will eat at the restaurant'. 17. बिल लाइए (bil lāie) - "
  "'Bring the bill (please)'. 18. खाना बहुत स्वादिष्ट था (khānā bahut svādiṣṭ thā) "
  "- 'The food was very tasty'. 19. फल ताज़े हैं (phal tāze haĩ) - 'The fruits are "
  "fresh'. 20. मिठाई खाओ (miṭhāī khāo) - 'Eat the sweets'. Food words to keep: रोटी "
  "(roṭī) flatbread, दाल (dāl) lentils, चावल (cāval) rice, सब्ज़ी (sabzī) vegetables, "
  "मसाला (masālā) spice, नमक (namak) salt, चीनी (cīnī) sugar, तेल (tel) oil, दूध "
  "(dūdh) milk, अंडा (aṇḍā) egg."),
 "how_it_works": (
  "Twenty sentences cover the full food day - hunger, the three meals, cooking "
  "verbs, tastes, and the restaurant - each translated. Cook one dish while naming "
  "every action in Hindi."),
 "key_points": [
  "20 food-and-cooking sentences with full translations.",
  "Meal words: नाश्ता (breakfast), दोपहर का खाना (lunch), रात का खाना (dinner).",
  "Cooking verbs: बनाना (make), उबालना (boil), काटना (cut), डालना (add/put).",
  "Taste words: मीठा (sweet), तीखा (spicy), खट्टा (sour), नमकीन (salty).",
  "Staple foods: रोटी, दाल, चावल, सब्ज़ी, मसाला.",
  "खाना बहुत स्वादिष्ट था - 'The food was very tasty'.",
 ],
 "requirements": [
  "Name ten foods in Hindi from memory.",
  "Give three cooking commands aloud: काटो, डालो, उबालो.",
  "Order a full meal in Hindi at your next restaurant visit.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "McGregor, R. S. The Oxford Hindi-English Dictionary. Oxford University Press; 1993.",
 ],
 "sig_lens": (
  "Through the Signature lens the food set is his original Signature kitchen "
  "instrument: every spice a Signature measure, every cooking verb a motion of his "
  "hand, the restaurant sentence a table he sets himself. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 13
{
 "key": "travel", "name": "Hindi Sentences: Travel and Directions",
 "group": "Compounded", "ladder": 13, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "20 sentences about transport, asking directions, tickets, and lodging. 1. "
  "स्टेशन कहाँ है (sṭeśan kahā̃ hai) - 'Where is the station'. 2. बाज़ार कितनी दूर है "
  "(bāzār kitnī dūr hai) - 'How far is the market'. 3. दाएँ मुड़ो (dāẽ muṛo) - "
  "'Turn right'. 4. बाएँ मुड़ो (bāẽ muṛo) - 'Turn left'. 5. सीधे जाओ (sīdhē jāo) - "
  "'Go straight'. 6. यहाँ से बस मिलेगी (yahā̃ se bas milegī) - 'You will get a bus "
  "from here'. 7. टैक्सी कितने की है (ṭaiksī kitne kī hai) - 'How much is the taxi'. "
  "8. दिल्ली का टिकट दो (dillī kā ṭikaṭ do) - 'Give two tickets to Delhi' - note: दो "
  "also means 'two'; context decides. 9. ट्रेन कितने बजे आएगी (ṭren kitne baje "
  "āegī) - 'At what time will the train come'. 10. यह बस कहाँ जाती है (yah bas "
  "kahā̃ jātī hai) - 'Where does this bus go'. 11. मुझे हवाई अड्डा जाना है (mujhe "
  "havāī aḍḍā jānā hai) - 'I have to go to the airport'. 12. होटल कहाँ है (hoṭal "
  "kahā̃ hai) - 'Where is the hotel'. 13. एक कमरा चाहिए (ek kamrā cāhie) - 'I need "
  "a room'. 14. कमरे का किराया कितना है (kamre kā kirāyā kitnā hai) - 'What is the "
  "room rent'. 15. नक्शा दिखाइए (nakśā dikhāie) - 'Show the map (please)'. 16. मैं "
  "रास्ता भूल गया (maĩ rāstā bhūl gayā) - 'I lost my way'. 17. क्या आप मेरी मदद "
  "करेंगे (kyā āp merī madad karẽge) - 'Will you help me'. 18. पेट्रोल पंप कहाँ है "
  "(peṭrol pamp kahā̃ hai) - 'Where is the petrol pump'. 19. यात्रा अच्छी रही "
  "(yātrā acchī rahī) - 'The journey was good'. 20. हम कल वापस जाएँगे (ham kal "
  "vāpas jāẽge) - 'We will go back tomorrow'. Direction words: दाएँ (dāẽ) right, "
  "बाएँ (bāẽ) left, सीधे (sīdhē) straight, पास (pās) near, दूर (dūr) far, सामने "
  "(sāmne) in front, पीछे (pīche) behind."),
 "how_it_works": (
  "Twenty travel sentences form a complete journey - asking the way, taking "
  "transport, buying tickets, finding a room, and coming home - each translated. "
  "Rehearse them before any trip; they are the survival kit."),
 "key_points": [
  "20 travel-and-direction sentences with full translations.",
  "Direction core: दाएँ, बाएँ, सीधे, पास, दूर, सामने, पीछे.",
  "कहाँ है ('where is') unlocks every location question.",
  "कितने की है / कितना है asks any price.",
  "मैं रास्ता भूल गया - 'I lost my way' - the traveler's rescue line.",
  "हम कल वापस जाएँगे - 'We will go back tomorrow'.",
 ],
 "requirements": [
  "Memorize the seven direction words cold.",
  "Practice the full station-to-hotel sequence aloud.",
  "Ask for directions in Hindi on your next outing.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens the travel set is his original Signature road "
  "instrument: every direction a turn he calls, every ticket a passage he claims, "
  "the journey a line he draws himself. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 14
{
 "key": "workschool", "name": "Hindi Sentences: Work and School",
 "group": "Compounded", "ladder": 14, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "20 sentences about jobs, the office, the classroom, and learning. 1. मैं शिक्षक "
  "हूँ (maĩ śikṣak hū̃) - 'I am a teacher'. 2. वह डॉक्टर है (vah ḍākṭar hai) - 'He "
  "is a doctor'. 3. मेरा काम अच्छा है (merā kām acchā hai) - 'My work is good'. 4. "
  "दफ़्तर नौ बजे खुलता है (daftar nau baje khultā hai) - 'The office opens at nine'. "
  "5. मुझे काम पर जाना है (mujhe kām par jānā hai) - 'I have to go to work'. 6. आज "
  "बहुत काम है (āj bahut kām hai) - 'There is a lot of work today'. 7. बैठक तीन बजे "
  "है (baiṭhak tīn baje hai) - 'The meeting is at three'. 8. यह मेरा सहकर्मी है (yah "
  "merā sahakarmī hai) - 'He is my colleague'. 9. वेतन महीने में मिलता है (vetan "
  "mahīne mẽ miltā hai) - 'Salary comes every month'. 10. बच्चा स्कूल जाता है "
  "(baccā skūl jātā hai) - 'The child goes to school'. 11. कक्षा में चालीस छात्र हैं "
  "(kakṣā mẽ cālīs chātra haĩ) - 'There are forty students in the class'. 12. "
  "अध्यापक पढ़ाते हैं (adhyāpak paṛhāte haĩ) - 'The teacher teaches'. 13. छात्र "
  "सवाल पूछते हैं (chātra savāl pūchte haĩ) - 'The students ask questions'. 14. "
  "परीक्षा अगले हफ़्ते है (parīkṣā agle hafte hai) - 'The exam is next week'. 15. "
  "मैं हिन्दी सीखता हूँ (maĩ hindī sīkhtā hū̃) - 'I am learning Hindi'. 16. पढ़ाई "
  "में मन लगाओ (paṛhāī mẽ man lagāo) - 'Put your mind into studies'. 17. गृहकार्य "
  "पूरा करो (gṛhakārya pūrā karo) - 'Complete the homework'. 18. किताब खोलो (kitāb "
  "kholo) - 'Open the book'. 19. ध्यान से सुनो (dhyān se suno) - 'Listen carefully'. "
  "20. सीखना कभी बंद मत करो (sīkhnā kabhī band mat karo) - 'Never stop learning'. "
  "Work words: नौकरी (naukarī) job, दफ़्तर (daftar) office, बैठक (baiṭhak) meeting, "
  "वेतन (vetan) salary, सहकर्मी (sahakarmī) colleague. School words: कक्षा (kakṣā) "
  "class, छात्र (chātra) student, अध्यापक (adhyāpak) teacher, परीक्षा (parīkṣā) exam, "
  "पढ़ाई (paṛhāī) studies."),
 "how_it_works": (
  "Twenty sentences split between the office and the classroom - jobs, meetings, "
  "salary, lessons, exams - each translated. Use the classroom half to run your own "
  "study session in Hindi."),
 "key_points": [
  "20 work-and-school sentences with full translations.",
  "Office words: नौकरी, दफ़्तर, बैठक, वेतन, सहकर्मी.",
  "School words: कक्षा, छात्र, अध्यापक, परीक्षा, पढ़ाई, गृहकार्य.",
  "मैं हिन्दी सीखता हूँ - 'I am learning Hindi'.",
  "सीखना कभी बंद मत करो - 'Never stop learning'.",
 ],
 "requirements": [
  "Say your own job in Hindi: मैं ___ हूँ.",
  "Give the five classroom commands aloud.",
  "Write your week's schedule using the day names.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens the work set is his original Signature craft "
  "instrument: the office his workshop, the classroom his training ground, every "
  "lesson a Signature operation he runs himself. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 15
{
 "key": "health", "name": "Hindi Sentences: Health and the Body",
 "group": "Compounded", "ladder": 15, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "20 sentences about body parts, symptoms, the doctor visit, and the pharmacy. 1. "
  "मेरा सिर दुख रहा है (merā sir dukh rahā hai) - 'My head is aching'. 2. मुझे "
  "बुखार है (mujhe bukhār hai) - 'I have a fever'. 3. मेरा गला खराब है (merā galā "
  "kharāb hai) - 'My throat is sore'. 4. मुझे खाँसी है (mujhe khā̃sī hai) - 'I have "
  "a cough'. 5. मेरा पेट दुखता है (merā peṭ dukhtā hai) - 'My stomach hurts'. 6. "
  "मेरी आँखें लाल हैं (merī ā̃khẽ lāl haĩ) - 'My eyes are red'. 7. मेरा हाथ कट गया "
  "(merā hāth kaṭ gayā) - 'My hand got cut'. 8. मेरे पैर में दर्द है (mere pair mẽ "
  "dard hai) - 'There is pain in my leg'. 9. डॉक्टर को दिखाओ (ḍākṭar ko dikhāo) - "
  "'Show it to the doctor'. 10. अस्पताल कहाँ है (aspatāl kahā̃ hai) - 'Where is the "
  "hospital'. 11. डॉक्टर ने दवा दी (ḍākṭar ne davā dī) - 'The doctor gave medicine'. "
  "12. दवा समय पर लो (davā samay par lo) - 'Take the medicine on time'. 13. आराम करो "
  "(ārām karo) - 'Take rest'. 14. ज़्यादा पानी पियो (zyādā pānī piyo) - 'Drink more "
  "water'. 15. अब तबीयत कैसी है (ab tabīyat kaisī hai) - 'How is your health now'. "
  "16. मैं ठीक हो रहा हूँ (maĩ ṭhīk ho rahā hū̃) - 'I am getting better'. 17. दवा "
  "की दुकान कहाँ है (davā kī dukān kahā̃ hai) - 'Where is the pharmacy'. 18. यह दवा "
  "दिन में दो बार लो (yah davā din mẽ do bār lo) - 'Take this medicine twice a day'. "
  "19. सेहत का ख्याल रखो (sehat kā khyāl rakho) - 'Take care of your health'. 20. "
  "रोज़ व्यायाम करो (roz vyāyām karo) - 'Exercise daily'. Body words: सिर (sir) "
  "head, आँख (ā̃kh) eye, नाक (nāk) nose, मुँह (mũh) mouth, गला (galā) throat, हाथ "
  "(hāth) hand, पैर (pair) leg/foot, पेट (peṭ) stomach, दिल (dil) heart, हड्डी "
  "(haḍḍī) bone."),
 "how_it_works": (
  "Twenty sentences form a complete health episode - naming the body, describing "
  "symptoms, visiting the doctor, taking medicine, recovering - each translated. "
  "Point to each body part and name it in Hindi as you read."),
 "key_points": [
  "20 health-and-body sentences with full translations.",
  "Body words: सिर, आँख, नाक, मुँह, गला, हाथ, पैर, पेट, दिल.",
  "Symptom pattern: मुझे ___ है (मुझे बुखार है - 'I have a fever').",
  "Doctor words: डॉक्टर, अस्पताल, दवा, दवा की दुकान.",
  "दवा समय पर लो - 'Take the medicine on time'.",
  "सेहत का ख्याल रखो - 'Take care of your health'.",
 ],
 "requirements": [
  "Point to and name ten body parts in Hindi.",
  "Memorize the symptom pattern मुझे ___ है.",
  "Know अस्पताल कहाँ है cold - it is the emergency line.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "McGregor, R. S. The Oxford Hindi-English Dictionary. Oxford University Press; 1993.",
 ],
 "sig_lens": (
  "Through the Signature lens the health set is his original Signature body "
  "instrument: every part named, every symptom reported, every recovery a system "
  "he maintains himself. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 16
{
 "key": "emotions", "name": "Hindi Sentences: Emotions and Feelings",
 "group": "Compounded", "ladder": 16, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "20 sentences about happiness, sadness, anger, fear, love, and surprise. 1. मैं "
  "बहुत खुश हूँ (maĩ bahut khuś hū̃) - 'I am very happy'. 2. आज मेरा मन प्रसन्न है "
  "(āj merā man prasann hai) - 'My heart is cheerful today'. 3. वह हँस रही है (vah "
  "hãs rahī hai) - 'She is laughing'. 4. अच्छी खबर सुनकर खुशी हुई (acchī khabar "
  "sunkar khuśī huī) - 'I felt happy hearing the good news'. 5. मैं दुखी हूँ (maĩ "
  "dukhī hū̃) - 'I am sad'. 6. वह रो रहा है (vah ro rahā hai) - 'He is crying'. 7. "
  "मुझे आपकी याद आती है (mujhe āpkī yād ātī hai) - 'I miss you'. 8. दिल टूट गया (dil "
  "ṭūṭ gayā) - 'The heart broke'. 9. मुझे गुस्सा आ रहा है (mujhe gussā ā rahā hai) "
  "- 'I am getting angry'. 10. शांत हो जाओ (śānt ho jāo) - 'Calm down'. 11. मुझे "
  "डर लग रहा है (mujhe ḍar lag rahā hai) - 'I am feeling scared'. 12. अँधेरे से मत "
  "डरो (ãdhēre se mat ḍaro) - 'Do not fear the darkness'. 13. मैं तुमसे प्यार करता "
  "हूँ (maĩ tumse pyār kartā hū̃) - 'I love you'. 14. प्यार सबसे बड़ी ताकत है (pyār "
  "sabse baṛī tākat hai) - 'Love is the greatest strength'. 15. मुझे आश्चर्य हुआ "
  "(mujhe āścarya huā) - 'I was surprised'. 16. यह तो कमाल है (yah to kamāl hai) - "
  "'This is amazing'. 17. मुझे गर्व है (mujhe garv hai) - 'I am proud'. 18. चिंता मत "
  "करो (cintā mat karo) - 'Do not worry'. 19. सब ठीक हो जाएगा (sab ṭhīk ho jāegā) - "
  "'Everything will be all right'. 20. मुस्कुराओ, जीवन सुंदर है (muskurāo, jīvan "
  "sundar hai) - 'Smile, life is beautiful'. Emotion words: खुशी (khuśī) happiness, "
  "दुख (dukh) sorrow, गुस्सा (gussā) anger, डर (ḍar) fear, प्यार (pyār) love, "
  "आश्चर्य (āścarya) surprise, गर्व (garv) pride, चिंता (cintā) worry, उम्मीद "
  "(ummīd) hope, शांति (śānti) peace."),
 "how_it_works": (
  "Twenty sentences carry the six core emotions - each one felt, named, and "
  "translated - so you learn to say what you feel in Hindi. Read each with the "
  "feeling in your voice."),
 "key_points": [
  "20 emotion sentences with full translations.",
  "Emotion words: खुशी, दुख, गुस्सा, डर, प्यार, आश्चर्य, गर्व, चिंता.",
  "Feeling pattern: मुझे ___ है / मुझे ___ लग रहा है.",
  "मैं तुमसे प्यार करता हूँ - 'I love you'.",
  "सब ठीक हो जाएगा - 'Everything will be all right'.",
 ],
 "requirements": [
  "Say each emotion sentence with real feeling.",
  "Name the ten emotion words from memory.",
  "Tell someone how you feel in Hindi today.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "McGregor, R. S. The Oxford Hindi-English Dictionary. Oxford University Press; 1993.",
 ],
 "sig_lens": (
  "Through the Signature lens the emotion set is his original Signature heart "
  "instrument: every feeling named in his own system, every comfort a line he "
  "writes himself. Signature-made teaching, clearly labeled, never presented as "
  "an outside authority's text."),
},
# ================================================================== 17
{
 "key": "nature", "name": "Hindi Sentences: Nature and Weather",
 "group": "Compounded", "ladder": 17, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "20 sentences about animals, plants, seasons, and weather talk. 1. कुत्ता भौंक रहा "
  "है (kuttā bhaũk rahā hai) - 'The dog is barking'. 2. बिल्ली दूध पीती है (billī "
  "dūdh pītī hai) - 'The cat drinks milk'. 3. गाय घास खाती है (gāy ghās khātī hai) - "
  "'The cow eats grass'. 4. हाथी बहुत बड़ा जानवर है (hāthī bahut baṛā jānvar hai) - "
  "'The elephant is a very big animal'. 5. चिड़िया पेड़ पर बैठी है (ciṛiyā peṛ par "
  "baiṭhī hai) - 'The bird is sitting on the tree'. 6. मछली पानी में तैरती है "
  "(machlī pānī mẽ tairtī hai) - 'The fish swims in water'. 7. बगीचे में फूल खिले "
  "हैं (bagīce mẽ phūl khile haĩ) - 'Flowers have bloomed in the garden'. 8. पेड़ "
  "की छाँव ठंडी है (peṛ kī chā̃v ṭhaṇḍī hai) - 'The tree's shade is cool'. 9. आज मौसम "
  "अच्छा है (āj mausam acchā hai) - 'The weather is nice today'. 10. बहुत गर्मी है "
  "(bahut garmī hai) - 'It is very hot'. 11. सर्दी बढ़ रही है (sardī baṛh rahī hai) "
  "- 'The cold is increasing'. 12. बारिश हो रही है (bāriś ho rahī hai) - 'It is "
  "raining'. 13. बादल छाए हैं (bādal chāe haĩ) - 'Clouds have gathered'. 14. हवा "
  "तेज़ चल रही है (havā tez cal rahī hai) - 'The wind is blowing fast'. 15. आसमान "
  "नीला है (āsmān nīlā hai) - 'The sky is blue'. 16. इंद्रधनुष दिख रहा है (indradhanuṣ "
  "dikh rahā hai) - 'A rainbow is visible'. 17. कल धूप निकलेगी (kal dhūp niklegī) "
  "- 'The sun will come out tomorrow'. 18. नदी में पानी बह रहा है (nadī mẽ pānī bah "
  "rahā hai) - 'Water is flowing in the river'. 19. पहाड़ बहुत ऊँचे हैं (pahāṛ bahut "
  "ū̃ce haĩ) - 'The mountains are very high'. 20. प्रकृति सुंदर है (prakṛti sundar "
  "hai) - 'Nature is beautiful'. Nature words: जानवर (jānvar) animal, पेड़ (peṛ) "
  "tree, फूल (phūl) flower, नदी (nadī) river, पहाड़ (pahāṛ) mountain, बादल (bādal) "
  "cloud, बारिश (bāriś) rain, हवा (havā) wind, धूप (dhūp) sunshine."),
 "how_it_works": (
  "Twenty sentences walk through the living world - animals, plants, sky, and "
  "weather - each translated. Step outside and describe what you see in Hindi."),
 "key_points": [
  "20 nature-and-weather sentences with full translations.",
  "Animal words: कुत्ता, बिल्ली, गाय, हाथी, चिड़िया, मछली.",
  "Weather core: बारिश हो रही है - 'It is raining'; बहुत गर्मी है - 'It is very hot'.",
  "Sky words: आसमान, बादल, धूप, इंद्रधनुष.",
  "प्रकृति सुंदर है - 'Nature is beautiful'.",
 ],
 "requirements": [
  "Describe today's weather in three Hindi sentences.",
  "Name ten animals in Hindi from memory.",
  "Take a walk and name five natural things aloud.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "McGregor, R. S. The Oxford Hindi-English Dictionary. Oxford University Press; 1993.",
 ],
 "sig_lens": (
  "Through the Signature lens the nature set is his original Signature world "
  "instrument: every animal named, every weather called, the whole outdoors "
  "brought into his system. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 18
{
 "key": "shopping", "name": "Hindi Sentences: Shopping and Money",
 "group": "Compounded", "ladder": 18, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "20 sentences about the market, prices, bargaining, and paying. 1. बाज़ार कहाँ है "
  "(bāzār kahā̃ hai) - 'Where is the market'. 2. यह कितने का है (yah kitne kā hai) - "
  "'How much is this'. 3. बहुत महँगा है (bahut mahãgā hai) - 'It is very expensive'. "
  "4. कुछ कम कीजिए (kuch kam kījie) - 'Reduce the price a little (please)'. 5. आखिरी "
  "दाम बताइए (ākhirī dām batāie) - 'Tell me the final price'. 6. ठीक है, दे दीजिए "
  "(ṭhīk hai, de dījie) - 'Okay, give it'. 7. क्या आपके पास छोटा नोट है (kyā āpke "
  "pās choṭā noṭ hai) - 'Do you have a smaller note'. 8. मैं नकद दूँगा (maĩ nakad "
  "dū̃gā) - 'I will pay cash'. 9. क्या कार्ड चलता है (kyā kārḍ caltā hai) - 'Do you "
  "accept cards'. 10. रसीद दीजिए (rasīd dījie) - 'Give the receipt (please)'. 11. "
  "सब्ज़ी ताज़ी है (sabzī tāzī hai) - 'The vegetables are fresh'. 12. एक किलो टमाटर "
  "दो (ek kilo ṭamāṭar do) - 'Give one kilo of tomatoes'. 13. आधा किलो आलू चाहिए "
  "(ādhā kilo ālū cāhie) - 'I need half a kilo of potatoes'. 14. फल मीठे हैं (phal "
  "mīṭhe haĩ) - 'The fruits are sweet'. 15. यह कपड़ा अच्छा है (yah kapaṛā acchā "
  "hai) - 'This cloth is good'. 16. बड़ा साइज़ दिखाइए (baṛā sāiz dikhāie) - 'Show a "
  "bigger size (please)'. 17. छूट मिलेगी (chūṭ milegī) - 'Will I get a discount'. 18. "
  "दुकान कब बंद होती है (dukān kab band hotī hai) - 'When does the shop close'. 19. "
  "मैं कल फिर आऊँगा (maĩ kal phir āū̃gā) - 'I will come again tomorrow'. 20. "
  "खरीदारी अच्छी रही (kharīdārī acchī rahī) - 'The shopping went well'. Money words: "
  "पैसा (paisā) money, रुपया (rupayā) rupee, दाम (dām) price, छूट (chūṭ) discount, "
  "नकद (nakad) cash, रसीद (rasīd) receipt, किराया (kirāyā) rent/fare."),
 "how_it_works": (
  "Twenty sentences run a full market trip - finding the market, asking prices, "
  "bargaining, choosing, paying - each translated. Bargaining lines 4-6 are the "
  "ones to rehearse most."),
 "key_points": [
  "20 shopping-and-money sentences with full translations.",
  "Price core: यह कितने का है - 'How much is this'.",
  "Bargaining: कुछ कम कीजिए; आखिरी दाम बताइए.",
  "Paying: मैं नकद दूँगा; क्या कार्ड चलता है; रसीद दीजिए.",
  "Money words: पैसा, रुपया, दाम, छूट, नकद, रसीद.",
  "खरीदारी अच्छी रही - 'The shopping went well'.",
 ],
 "requirements": [
  "Rehearse the bargaining sequence aloud three times.",
  "Buy one thing using only Hindi this week.",
  "Memorize the money words cold.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "McGregor, R. S. The Oxford Hindi-English Dictionary. Oxford University Press; 1993.",
 ],
 "sig_lens": (
  "Through the Signature lens the shopping set is his original Signature market "
  "instrument: every price asked, every bargain struck, every payment a deal he "
  "closes himself. Signature-made teaching, clearly labeled, never presented as "
  "an outside authority's text."),
},
# ================================================================== 19
{
 "key": "social", "name": "Hindi Sentences: Friendship and Social Life",
 "group": "Compounded", "ladder": 19, "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "20 sentences about meeting people, invitations, and celebrations. 1. आपसे मिलकर "
  "खुशी हुई (āpse milkar khuśī huī) - 'Pleased to meet you'. 2. मेरा नाम राम है (merā "
  "nām rām hai) - 'My name is Ram'. 3. आपका नाम क्या है (āpkā nām kyā hai) - 'What "
  "is your name'. 4. आप कहाँ रहते हैं (āp kahā̃ rahte haĩ) - 'Where do you live'. 5. "
  "मैं दिल्ली में रहता हूँ (maĩ dillī mẽ rahtā hū̃) - 'I live in Delhi'. 6. आप क्या "
  "काम करते हैं (āp kyā kām karte haĩ) - 'What work do you do'. 7. क्या हम दोस्त बन "
  "सकते हैं (kyā ham dost ban sakte haĩ) - 'Can we become friends'. 8. मेरा नंबर ले "
  "लीजिए (merā nambar le lījie) - 'Please take my number'. 9. कल मेरे घर आइए (kal "
  "mere ghar āie) - 'Please come to my house tomorrow'. 10. चाय पिएँगे (cāy piyẽge) "
  "- 'Will you have tea'. 11. जन्मदिन की बधाई (janmadin kī badhāī) - 'Happy "
  "birthday'. 12. शादी में आइएगा (śādī mẽ āiegā) - 'Please come to the wedding'. "
  "13. त्योहार की शुभकामनाएँ (tyohār kī śubhkāmnāẽ) - 'Festival greetings'. 14. "
  "साथ में खाना खाएँगे (sāth mẽ khānā khāẽge) - 'We will eat together'. 15. बहुत "
  "मज़ा आया (bahut mazā āyā) - 'I had a lot of fun'. 16. फिर कब मिलेंगे (phir kab "
  "milẽge) - 'When will we meet again'. 17. संपर्क में रहिएगा (sampark mẽ rahiegā) "
  "- 'Stay in touch'. 18. आपकी मदद के लिए धन्यवाद (āpkī madad ke lie dhanyavād) - "
  "'Thanks for your help'. 19. आप बहुत अच्छे हैं (āp bahut acche haĩ) - 'You are "
  "very kind'. 20. दोस्ती ज़िंदाबाद (dostī zindābād) - 'Long live friendship'. "
  "Social words: दोस्त (dost) friend, मेहमान (mehmān) guest, निमंत्रण (nimantraṇ) "
  "invitation, बधाई (badhāī) congratulations, त्योहार (tyohār) festival, शादी "
  "(śādī) wedding, जन्मदिन (janmadin) birthday, मुलाकात (mulākāt) meeting."),
 "how_it_works": (
  "Twenty sentences carry you from first introduction to lasting friendship - "
  "names, invitations, celebrations, goodbyes - each translated. Introduce "
  "yourself in Hindi to someone this week."),
 "key_points": [
  "20 friendship-and-social-life sentences with full translations.",
  "Introduction core: मेरा नाम ___ है; आपसे मिलकर खुशी हुई.",
  "Invitation core: कल मेरे घर आइए; चाय पिएँगे.",
  "Celebration words: बधाई, शुभकामनाएँ, जन्मदिन, शादी, त्योहार.",
  "संपर्क में रहिएगा - 'Stay in touch'.",
  "दोस्ती ज़िंदाबाद - 'Long live friendship'.",
 ],
 "requirements": [
  "Introduce yourself fully in Hindi: name, home, work.",
  "Invite someone somewhere using कल मेरे घर आइए pattern.",
  "Wish someone on their next birthday in Hindi.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens the social set is his original Signature friendship "
  "instrument: every introduction a door he opens, every invitation a table he "
  "sets, every celebration a Signature gathering. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 20
{
 "key": "tech", "name": "Hindi Sentences: Technology and Communication",
 "group": "Compounded", "ladder": 20, "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "20 sentences about the phone, internet, computer, and messaging. 1. मेरा फ़ोन "
  "कहाँ है (merā fon kahā̃ hai) - 'Where is my phone'. 2. फ़ोन की बैटरी खत्म हो गई "
  "(fon kī baiṭrī khatm ho gaī) - 'The phone battery died'. 3. चार्जर दीजिए (cārjar "
  "dījie) - 'Give the charger (please)'. 4. मुझे फ़ोन कीजिए (mujhe fon kījie) - "
  "'Call me'. 5. नेटवर्क नहीं आ रहा (neṭvark nahī̃ ā rahā) - 'There is no network'. "
  "6. इंटरनेट धीमा है (iṇṭarneṭ dhīmā hai) - 'The internet is slow'. 7. वाई-फ़ाई का "
  "पासवर्ड क्या है (vāī-fāī kā pāsvard kyā hai) - 'What is the Wi-Fi password'. 8. "
  "मुझे संदेश भेजो (mujhe sandeś bhejo) - 'Send me a message'. 9. मैंने ईमेल भेजा "
  "(maĩne īmel bhejā) - 'I sent an email'. 10. तस्वीर भेजो (tasvīr bhejo) - 'Send "
  "the photo'. 11. वीडियो कॉल करो (vīḍiyo kŏl karo) - 'Make a video call'. 12. "
  "कंप्यूटर चालू करो (kampyūṭar cālū karo) - 'Turn on the computer'. 13. कंप्यूटर बंद "
  "करो (kampyūṭar band karo) - 'Turn off the computer'. 14. फ़ाइल खोलो (fāil kholo) "
  "- 'Open the file'. 15. यह ऐप बहुत अच्छा है (yah aip bahut acchā hai) - 'This app "
  "is very good'. 16. सॉफ़्टवेयर अपडेट करो (sŏfṭveyar apḍeṭ karo) - 'Update the "
  "software'. 17. पासवर्ड भूल गया (pāsvard bhūl gayā) - 'I forgot the password'. 18. "
  "ऑनलाइन पढ़ाई करो (ŏnlāin paṛhāī karo) - 'Study online'. 19. खबर देखो (khabar "
  "dekho) - 'Watch the news'. 20. तकनीक जीवन आसान बनाती है (taknīk jīvan āsān "
  "banātī hai) - 'Technology makes life easy'. Tech words: फ़ोन (fon) phone, "
  "संदेश (sandeś) message, ईमेल (īmel) email, इंटरनेट (iṇṭarneṭ) internet, कंप्यूटर "
  "(kampyūṭar) computer, ऐप (aip) app, पासवर्ड (pāsvard) password, बैटरी (baiṭrī) "
  "battery, चार्जर (cārjar) charger, स्क्रीन (skrīn) screen."),
 "how_it_works": (
  "Twenty sentences cover modern digital life - calls, messages, internet, "
  "computers - each translated. Change your phone's language to Hindi for a day "
  "and use these lines."),
 "key_points": [
  "20 technology-and-communication sentences with full translations.",
  "Phone core: मुझे फ़ोन कीजिए - 'Call me'; मुझे संदेश भेजो - 'Send me a message'.",
  "Internet core: वाई-फ़ाई का पासवर्ड क्या है.",
  "Computer commands: चालू करो, बंद करो, फ़ाइल खोलो.",
  "तकनीक जीवन आसान बनाती है - 'Technology makes life easy'.",
 ],
 "requirements": [
  "Send one full message in Hindi this week.",
  "Learn the ten tech words cold.",
  "Give the computer commands aloud while doing them.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "McGregor, R. S. The Oxford Hindi-English Dictionary. Oxford University Press; 1993.",
 ],
 "sig_lens": (
  "Through the Signature lens the tech set is his original Signature signal "
  "instrument: every call a line he opens, every message a packet he sends, the "
  "whole digital world addressed in his system. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 21
{
 "key": "tenses", "name": "Hindi Verb Tenses in Sentences",
 "group": "Advanced", "ladder": 21, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Present, past, and future - with aspect notes - five or more translated "
  "sentences per tense. PRESENT HABITUAL (stem + ता/ती + है): 1. मैं पढ़ता हूँ "
  "(maĩ paṛhtā hū̃) - 'I read (habitually)'. 2. वह खेलती है (vah kheltī hai) - "
  "'She plays'. 3. हम काम करते हैं (ham kām karte haĩ) - 'We work'. 4. तुम कहाँ "
  "जाते हो (tum kahā̃ jāte ho) - 'Where do you go'. 5. बच्चे दूध पीते हैं (bacce "
  "dūdh pīte haĩ) - 'Children drink milk'. PRESENT PROGRESSIVE (रहा/रही + है): 6. "
  "मैं पढ़ रहा हूँ (maĩ paṛh rahā hū̃) - 'I am reading (right now)'. 7. वह खाना बना "
  "रही है (vah khānā banā rahī hai) - 'She is cooking food'. 8. बारिश हो रही है "
  "(bāriś ho rahī hai) - 'It is raining'. PAST SIMPLE (stem + या/यी/ये + था): 9. "
  "मैं गया (maĩ gayā) - 'I went'. 10. वह आई (vah āī) - 'She came'. 11. राम ने खाना "
  "खाया (rām ne khānā khāyā) - 'Ram ate food' - ने marks the doer. 12. हमने फिल्म "
  "देखी (hamne philm dekhī) - 'We watched a film'. 13. कल बहुत गर्मी थी (kal bahut "
  "garmī thī) - 'It was very hot yesterday'. PAST PROGRESSIVE: 14. मैं पढ़ रहा था "
  "(maĩ paṛh rahā thā) - 'I was reading'. PRESENT PERFECT (चुका): 15. मैं खा चुका "
  "हूँ (maĩ khā cukā hū̃) - 'I have eaten (finished eating)'. FUTURE (stem + गा/गी/गे): "
  "16. मैं जाऊँगा (maĩ jāū̃gā) - 'I will go'. 17. वह आएगी (vah āegī) - 'She will "
  "come'. 18. हम खेलेंगे (ham khelẽge) - 'We will play'. 19. तुम क्या करोगे (tum "
  "kyā karoge) - 'What will you do'. 20. कल छुट्टी होगी (kal chuṭṭī hogī) - "
  "'Tomorrow will be a holiday'. Aspect summary: ता = habit ('I read'), रहा = "
  "right-now ('I am reading'), चुका = completed ('I have finished reading'), गा = "
  "future ('I will read')."),
 "how_it_works": (
  "The tense system is taught as four aspects - habitual, progressive, completed, "
  "future - each with its formula and five translated sentences. Convert each "
  "sentence through all four aspects aloud: मैं पढ़ता हूँ → मैं पढ़ रहा हूँ → मैं "
  "पढ़ चुका हूँ → मैं पढूँगा."),
 "key_points": [
  "Habitual present: stem + ता/ती + है (मैं पढ़ता हूँ).",
  "Progressive: रहा/रही + है (मैं पढ़ रहा हूँ).",
  "Perfective past uses ने for transitive verbs (राम ने खाया).",
  "Completed: चुका + है (मैं खा चुका हूँ).",
  "Future: गा/गी/गे (मैं जाऊँगा, वह आएगी, हम खेलेंगे).",
  "20 tense sentences, each with full translation.",
 ],
 "requirements": [
  "Conjugate जाना, खाना, करना through all four aspects.",
  "Say each of the 20 sentences in all tenses.",
  "Watch for ने in every perfective transitive sentence.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
  "IAST transliteration for verb paradigms",
 ],
 "citations": [
  "Shapiro, Michael C. Hindi. In: Cardona & Jain (eds.) The Indo-Aryan Languages. Routledge; 2003.",
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens tenses are his original Signature time instrument: "
  "ता the habit he keeps, रहा the moment he holds, चुका the work he finishes, गा "
  "the future he claims - time itself conjugated in his system. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 22
{
 "key": "qa", "name": "Hindi Questions and Answers",
 "group": "Advanced", "ladder": 22, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "20 question/answer pairs covering who, what, where, when, why, and how - Hindi, "
  "romanization, English. 1. Q: आपका नाम क्या है (āpkā nām kyā hai) - 'What is your "
  "name'. A: मेरा नाम सीता है (merā nām sītā hai) - 'My name is Sita'. 2. Q: आप कहाँ "
  "रहते हैं (āp kahā̃ rahte haĩ) - 'Where do you live'. A: मैं जयपुर में रहता हूँ "
  "(maĩ jaypur mẽ rahtā hū̃) - 'I live in Jaipur'. 3. Q: यह कौन है (yah kaun hai) "
  "- 'Who is this'. A: यह मेरा भाई है (yah merā bhāī hai) - 'This is my brother'. "
  "4. Q: तुम क्या करते हो (tum kyā karte ho) - 'What do you do'. A: मैं पढ़ता हूँ "
  "(maĩ paṛhtā hū̃) - 'I study'. 5. Q: बाज़ार कब जाओगे (bāzār kab jāoge) - 'When "
  "will you go to the market'. A: मैं शाम को जाऊँगा (maĩ śām ko jāū̃gā) - 'I will go "
  "in the evening'. 6. Q: तुम क्यों नहीं आए (tum kyõ nahī̃ āe) - 'Why did you not "
  "come'. A: मैं बीमार था (maĩ bīmār thā) - 'I was ill'. 7. Q: यह कैसे काम करता है "
  "(yah kaise kām kartā hai) - 'How does this work'. A: बटन दबाओ (baṭan dabāo) - "
  "'Press the button'. 8. Q: कितने बजे हैं (kitne baje haĩ) - 'What time is it'. A: "
  "दो बजे हैं (do baje haĩ) - 'It is two o'clock'. 9. Q: क्या तुम हिन्दी बोलते हो "
  "(kyā tum hindī bolte ho) - 'Do you speak Hindi'. A: हाँ, थोड़ी-थोड़ी (hā̃, "
  "thoṛī-thoṛī) - 'Yes, a little'. 10. Q: खाना कैसा था (khānā kaisā thā) - 'How was "
  "the food'. A: बहुत अच्छा था (bahut acchā thā) - 'It was very good'. 11. Q: टिकट "
  "कितने का है (ṭikaṭ kitne kā hai) - 'How much is the ticket'. A: पचास रुपये का है "
  "(pacās rupaye kā hai) - 'It is fifty rupees'. 12. Q: डॉक्टर कहाँ है (ḍākṭar "
  "kahā̃ hai) - 'Where is the doctor'. A: डॉक्टर अंदर है (ḍākṭar andar hai) - 'The "
  "doctor is inside'. 13. Q: तुम्हारी उम्र क्या है (tumhārī umra kyā hai) - 'What "
  "is your age'. A: मेरी उम्र बीस साल है (merī umra bīs sāl hai) - 'I am twenty "
  "years old'. 14. Q: क्या बारिश होगी (kyā bāriś hogī) - 'Will it rain'. A: हाँ, "
  "लगता है (hā̃, lagtā hai) - 'Yes, it seems so'. 15. Q: यह किसका है (yah kiskā hai) "
  "- 'Whose is this'. A: यह मेरा है (yah merā hai) - 'It is mine'. 16. Q: तुम कहाँ "
  "से हो (tum kahā̃ se ho) - 'Where are you from'. A: मैं आगरा से हूँ (maĩ āgrā se "
  "hū̃) - 'I am from Agra'. 17. Q: क्या मैं अंदर आ सकता हूँ (kyā maĩ andar ā saktā "
  "hū̃) - 'May I come in'. A: हाँ, आइए (hā̃, āie) - 'Yes, please come in'. 18. Q: "
  "कल क्या करोगे (kal kyā karoge) - 'What will you do tomorrow'. A: कल मैं घर पर "
  "रहूँगा (kal maĩ ghar par rahū̃gā) - 'Tomorrow I will stay home'. 19. Q: चाय लोगे "
  "(cāy loge) - 'Will you have tea'. A: हाँ, धन्यवाद (hā̃, dhanyavād) - 'Yes, thank "
  "you'. 20. Q: सब ठीक है (sab ṭhīk hai) - 'Is everything fine'. A: हाँ, सब ठीक है "
  "(hā̃, sab ṭhīk hai) - 'Yes, everything is fine'."),
 "how_it_works": (
  "Twenty complete exchanges - question and answer, both translated - covering "
  "every question word. Practice with a partner: one asks, one answers, then "
  "switch. Then make your own answers true for you."),
 "key_points": [
  "20 full Q/A pairs, each side translated.",
  "कौन (who), क्या (what), कहाँ (where), कब (when), क्यों (why), कैसे (how).",
  "क्या at the start makes yes/no questions.",
  "कितने का है asks price; कितने बजे हैं asks time.",
  "मेरा नाम सीता है - 'My name is Sita' - the model introduction answer.",
 ],
 "requirements": [
  "Practice all 20 pairs with a partner, switching roles.",
  "Answer each question truthfully about yourself.",
  "Ask five real questions in Hindi this week.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens questions are his original Signature inquiry "
  "instrument: every कौन a target he names, every क्यों a depth he sounds, every "
  "answer a Signature fact he files. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 23
{
 "key": "commands", "name": "Hindi Commands and Polite Requests",
 "group": "Advanced", "ladder": 23, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "20 imperative and polite-request sentences, formal vs informal. Informal (तुम) "
  "commands use the bare stem + ओ: आओ (āo) 'come', जाओ (jāo) 'go', खाओ (khāo) "
  "'eat', पियो (piyo) 'drink', बोलो (bolo) 'speak', बैठो (baiṭho) 'sit', देखो (dekho) "
  "'look', सुनो (suno) 'listen'. Formal (आप) requests use -इए: आइए (āie) 'please "
  "come', जाइए (jāie) 'please go', खाइए (khāie) 'please eat', पीजिए (pījie) 'please "
  "drink', बोलिए (bolie) 'please speak', बैठिए (baiṭhie) 'please sit', देखिए (dekhie) "
  "'please look', सुनिए (sunie) 'please listen'. THE 20: 1. आओ (āo) - 'Come "
  "(informal)'. 2. आइए (āie) - 'Please come in (formal)'. 3. बैठो (baiṭho) - 'Sit "
  "(informal)'. 4. बैठिए (baiṭhie) - 'Please sit (formal)'. 5. पानी पियो (pānī piyo) "
  "- 'Drink water (informal)'. 6. चाय पीजिए (cāy pījie) - 'Please have tea "
  "(formal)'. 7. धीरे बोलो (dhīre bolo) - 'Speak slowly (informal)'. 8. कृपया धीरे "
  "बोलिए (kṛpayā dhīre bolie) - 'Please speak slowly (formal)'. 9. दरवाज़ा खोलो "
  "(darvāzā kholo) - 'Open the door (informal)'. 10. कृपया दरवाज़ा बंद कीजिए "
  "(kṛpayā darvāzā band kījie) - 'Please close the door (formal)'. 11. मुझे किताब दो "
  "(mujhe kitāb do) - 'Give me the book (informal)'. 12. कृपया मेरी मदद कीजिए "
  "(kṛpayā merī madad kījie) - 'Please help me (formal)'. 13. जल्दी आओ (jaldī āo) - "
  "'Come quickly (informal)'. 14. ज़रा रुकिए (zarā rukie) - 'Please wait a moment "
  "(formal)'. 15. मत जाओ (mat jāo) - 'Do not go (informal)'. 16. मत जाइए (mat jāie) "
  "- 'Please do not go (formal)'. 17. चिंता मत करो (cintā mat karo) - 'Do not worry "
  "(informal)'. 18. आराम कीजिए (ārām kījie) - 'Please rest (formal)'. 19. खाना खाओ "
  "(khānā khāo) - 'Eat your food (informal, caring)'. 20. शुभ यात्रा (śubh yātrā) - "
  "'Have a good journey'. Rule: match the command form to the person - ओ-forms for "
  "तुम-people (friends, juniors, children), -इए-forms for आप-people (elders, "
  "strangers, officials). Adding कृपया ('please') or ज़रा ('a little') softens any "
  "request."),
 "how_it_works": (
  "The two command systems are taught side by side - informal ओ-forms and formal "
  "-इए-forms - in ten matched pairs, each translated, plus the softeners कृपया and "
  "ज़रा. Practice each pair on the right person."),
 "key_points": [
  "20 commands/requests in matched informal/formal pairs.",
  "Informal: stem + ओ (आओ, जाओ, खाओ, बोलो).",
  "Formal: stem + इए (आइए, जाइए, खाइए, बोलिए).",
  "मत + command = prohibition: मत जाओ, मत जाइए.",
  "कृपया and ज़रा soften any request.",
  "Match the form to the person: ओ for तुम-people, इए for आप-people.",
 ],
 "requirements": [
  "Drill all ten pairs aloud, feeling the politeness shift.",
  "Use only -इए forms with elders for one full day.",
  "Soften three requests with कृपया today.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
  "IAST transliteration for imperative paradigms",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003. Imperative chapter.",
  "Shapiro, Michael C. Hindi. In: Cardona & Jain (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens commands are his original Signature order "
  "instrument: the ओ-form the direct command he gives, the -इए-form the respect "
  "he wraps it in, कृपया the polish on the Signature order. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 24
{
 "key": "descriptions", "name": "Hindi Descriptions: People and Places",
 "group": "Advanced", "ladder": 24, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "20 sentences describing people, places, and things in detail. 1. मेरी माँ लंबी "
  "और सुंदर है (merī mā̃ lambī aur sundar hai) - 'My mother is tall and beautiful'. "
  "2. उसका चेहरा गोल है (uskā cehrā gol hai) - 'His face is round'. 3. उसकी आँखें "
  "काली हैं (uskī ā̃khẽ kālī haĩ) - 'Her eyes are black'. 4. उसके बाल लंबे हैं "
  "(uske bāl lambe haĩ) - 'His hair is long'. 5. वह नीली कमीज़ पहनता है (vah nīlī "
  "kamīz pahantā hai) - 'He wears a blue shirt'. 6. बच्चा छोटा और प्यारा है (baccā "
  "choṭā aur pyārā hai) - 'The child is small and lovely'. 7. दादा के बाल सफ़ेद हैं "
  "(dādā ke bāl safed haĩ) - 'Grandfather's hair is white'. 8. वह हमेशा मुस्कुराती "
  "है (vah hameśā muskurātī hai) - 'She always smiles'. 9. दिल्ली बड़ा शहर है "
  "(dillī baṛā śahar hai) - 'Delhi is a big city'. 10. आगरा में ताजमहल है (āgrā mẽ "
  "tājmahal hai) - 'The Taj Mahal is in Agra'. 11. जयपुर गुलाबी शहर है (jaypur "
  "gulābī śahar hai) - 'Jaipur is the pink city'. 12. गंगा लंबी नदी है (gaṅgā lambī "
  "nadī hai) - 'The Ganga is a long river'. 13. हिमालय ऊँचा पहाड़ है (himālaya ū̃cā "
  "pahāṛ hai) - 'The Himalaya is a high mountain'. 14. मेरा गाँव हरा-भरा है (merā "
  "gā̃v harā-bharā hai) - 'My village is lush green'. 15. यह घर पुराना पर मज़बूत है "
  "(yah ghar purānā par mazbūt hai) - 'This house is old but strong'. 16. बाज़ार "
  "भीड़भाड़ वाला है (bāzār bhīṛbhāṛ vālā hai) - 'The market is crowded'. 17. कमरा "
  "साफ़ और हवादार है (kamrā sāf aur havādār hai) - 'The room is clean and airy'. "
  "18. फूल लाल, पीले और सफ़ेद हैं (phūl lāl, pīle aur safed haĩ) - 'The flowers are "
  "red, yellow and white'. 19. आसमान साफ़ नीला है (āsmān sāf nīlā hai) - 'The sky is "
  "clear blue'. 20. यह जगह शांत और सुंदर है (yah jagah śānt aur sundar hai) - "
  "'This place is peaceful and beautiful'. Description tools: colors - लाल (lāl) "
  "red, नीला (nīlā) blue, हरा (harā) green, पीला (pīlā) yellow, काला (kālā) black, "
  "सफ़ेद (safed) white, गुलाबी (gulābī) pink; sizes - बड़ा/छोटा, लंबा/छोटा, ऊँचा "
  "(ū̃cā) high, गहरा (gahrā) deep; connectors - और (and), पर/लेकिन (but)."),
 "how_it_works": (
  "Twenty descriptive sentences - eight on people, twelve on places and things - "
  "each translated, with a color/size/connector toolkit at the end. Describe five "
  "people and five places around you in Hindi."),
 "key_points": [
  "20 detailed descriptive sentences with full translations.",
  "People toolkit: चेहरा, आँखें, बाल + colors + लंबा/छोटा.",
  "Place toolkit: शहर, नदी, पहाड़, गाँव + बड़ा/पुराना/सुंदर.",
  "Color words: लाल, नीला, हरा, पीला, काला, सफ़ेद, गुलाबी.",
  "और joins; पर/लेकिन contrasts: पुराना पर मज़बूत.",
  "यह जगह शांत और सुंदर है - 'This place is peaceful and beautiful'.",
 ],
 "requirements": [
  "Describe three people you know in Hindi.",
  "Describe your town in five Hindi sentences.",
  "Learn the seven color words cold.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "McGregor, R. S. The Oxford Hindi-English Dictionary. Oxford University Press; 1993.",
 ],
 "sig_lens": (
  "Through the Signature lens descriptions are his original Signature portrait "
  "instrument: every face drawn, every place mapped, every color a Signature "
  "shade he mixes himself. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 25
{
 "key": "story1", "name": "Hindi Story I: A Simple Story",
 "group": "Advanced", "ladder": 25, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A 10-sentence simple story in Hindi, line-by-line English translation. एक लड़का "
  "था (ek laṛkā thā) - 'There was a boy'. उसका नाम मोहन था (uskā nām mohan thā) - "
  "'His name was Mohan'. वह गाँव में रहता था (vah gā̃v mẽ rahtā thā) - 'He lived in "
  "a village'. उसका एक कुत्ता था (uskā ek kuttā thā) - 'He had a dog'. उसके कुत्ते "
  "का नाम मोती था (uske kutte kā nām motī thā) - 'His dog's name was Moti'. हर सुबह "
  "मोहन और मोती सैर पर जाते थे (har subah mohan aur motī sair par jāte the) - 'Every "
  "morning Mohan and Moti went for a walk'. एक दिन नदी किनारे एक चिड़िया मिली (ek "
  "din nadī kināre ek ciṛiyā milī) - 'One day they met a bird by the river'. चिड़िया "
  "घायल थी (ciṛiyā ghāyal thī) - 'The bird was hurt'. मोहन ने चिड़िया की देखभाल की "
  "(mohan ne ciṛiyā kī dekhbhāl kī) - 'Mohan took care of the bird'. दस दिन में "
  "चिड़िया ठीक हो गई और मोहन बहुत खुश हुआ (das din mẽ ciṛiyā ṭhīk ho gaī aur mohan "
  "bahut khuś huā) - 'In ten days the bird recovered and Mohan was very happy'. "
  "Story notes: था/थी/थे (thā/thī/the) is the past of है; ने marks the doer (मोहन "
  "ने); हर सुबह = 'every morning'. Retell the whole story aloud without looking."),
 "how_it_works": (
  "The story is read line by line - Hindi, romanization, translation - then the "
  "grammar notes decode the past-tense machinery inside it. Read each line aloud, "
  "then retell the whole story from memory."),
 "key_points": [
  "10-sentence story with line-by-line translation.",
  "था/थी/थे = past of है (was/were).",
  "ने marks the doer in past transitive sentences (मोहन ने).",
  "हर सुबह = 'every morning'; time phrases anchor stories.",
  "Retell the story aloud without looking - the mastery test.",
 ],
 "requirements": [
  "Read each line aloud three times.",
  "Retell the full story from memory.",
  "Change the characters and retell it as your own.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens this story is his original Signature tale: a boy, "
  "a dog, and a kindness, told in his own system's past tense - narrative as a "
  "Signature instrument. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 26
{
 "key": "story2", "name": "Hindi Story II: A Story in the Past Tense",
 "group": "Advanced", "ladder": 26, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A 10-sentence story using past-tense forms, line-by-line English translation. "
  "पिछले साल मैं जयपुर गया (pichle sāl maĩ jaypur gayā) - 'Last year I went to "
  "Jaipur'. मेरे साथ मेरा दोस्त था (mere sāth merā dost thā) - 'My friend was with "
  "me'. हमने सुबह की ट्रेन पकड़ी (hamne subah kī ṭren pakṛī) - 'We caught the "
  "morning train'. ट्रेन पाँच घंटे में पहुँची (ṭren pā̃c ghaṇṭe mẽ pahũcī) - 'The "
  "train arrived in five hours'. हमने होटल में कमरा लिया (hamne hoṭal mẽ kamrā "
  "liyā) - 'We took a room in the hotel'. दोपहर में हमने किला देखा (dopahar mẽ "
  "hamne qilā dekhā) - 'In the afternoon we saw the fort'. किला बहुत पुराना था "
  "(qilā bahut purānā thā) - 'The fort was very old'. शाम को हमने बाज़ार में "
  "खरीदारी की (śām ko hamne bāzār mẽ kharīdārī kī) - 'In the evening we shopped in "
  "the market'. रात को हमने दाल-बाटी खाई (rāt ko hamne dāl-bāṭī khāī) - 'At night we "
  "ate dal-baati'. अगले दिन हम घर वापस आए और यात्रा बहुत अच्छी रही (agle din ham "
  "ghar vāpas āe aur yātrā bahut acchī rahī) - 'The next day we came back home and "
  "the journey was very good'. Story notes: गया/गई/गए = 'went'; पकड़ी/देखी/खाई show "
  "feminine agreement with feminine objects (ट्रेन, फिल्म-like nouns); हम ने marks "
  "'we' as doers; time phrases (पिछले साल, सुबह, दोपहर में, शाम को, रात को, अगले "
  "दिन) sequence the story."),
 "how_it_works": (
  "A travel story told entirely in the past - line-by-line translation - with "
  "notes decoding the past forms and agreement inside it. Tell your own last trip "
  "in Hindi using the same time-phrase skeleton."),
 "key_points": [
  "10-sentence past-tense story with line-by-line translation.",
  "गया/गई/गए = 'went'; past verbs agree with the subject/object.",
  "हम ने marks 'we' as the doer of completed actions.",
  "Time phrases sequence stories: पिछले साल, सुबह, दोपहर में, शाम को, रात को.",
  "यात्रा बहुत अच्छी रही - 'The journey was very good'.",
 ],
 "requirements": [
  "Tell your own last trip in Hindi with six time phrases.",
  "Convert five present sentences into the past.",
  "Retell this story from memory.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
  "IAST transliteration for past paradigms",
 ],
 "citations": [
  "Shapiro, Michael C. Hindi. In: Cardona & Jain (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens this past-tense story is his original Signature "
  "journey record: every completed action stamped, every time phrase a notch on "
  "his timeline. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 27
{
 "key": "story3", "name": "Hindi Story III: A Story in Future and Conditional",
 "group": "Advanced", "ladder": 27, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A 10-sentence story using future and conditional forms, line-by-line English "
  "translation. अगले महीने मैं नया काम शुरू करूँगा (agle mahīne maĩ nayā kām śurū "
  "karū̃gā) - 'Next month I will start a new job'. मैं रोज़ सुबह जल्दी उठूँगा (maĩ "
  "roz subah jaldī uṭhū̃gā) - 'I will wake up early every morning'. अगर मेहनत "
  "करूँगा तो सफल होऊँगा (agar mehnat karū̃gā to saphal hoū̃gā) - 'If I work hard, "
  "I will succeed'. मैं हिन्दी में बात करूँगा (maĩ hindī mẽ bāt karū̃gā) - 'I will "
  "speak in Hindi'. मेरे दोस्त मेरी मदद करेंगे (mere dost merī madad karẽge) - 'My "
  "friends will help me'. हम सब मिलकर काम करेंगे (ham sab milkar kām karẽge) - "
  "'We will all work together'. अगर बारिश होगी तो हम घर पर रहेंगे (agar bāriś "
  "hogī to ham ghar par rahẽge) - 'If it rains, we will stay home'. साल के अंत तक "
  "मैं बहुत कुछ सीख लूँगा (sāl ke ant tak maĩ bahut kuch sīkh lū̃gā) - 'By year's "
  "end I will have learned a lot'. मेरा परिवार मुझ पर गर्व करेगा (merā parivār "
  "mujh par garv karegā) - 'My family will be proud of me'. भविष्य उज्ज्वल होगा "
  "(bhaviṣya ujjval hogā) - 'The future will be bright'. Story notes: गा/गी/गे "
  "marks the future (करूँगा, करेंगे, होगा); अगर...तो (agar...to) builds the "
  "conditional 'if...then'; ऊँगा/ऊँगी are first-person future forms (जाऊँगा, "
  "करूँगा). Write your own five future plans in Hindi."),
 "how_it_works": (
  "A plans-for-the-future story - line-by-line translation - with notes decoding "
  "the future endings and the अगर...तो conditional frame. Close by writing your "
  "own five future plans in Hindi."),
 "key_points": [
  "10-sentence future/conditional story with line-by-line translation.",
  "गा/गी/गे = future marker (जाऊँगा, आएगी, करेंगे).",
  "अगर...तो = 'if...then' conditional frame.",
  "First-person future: जाऊँगा, करूँगा, सीखूँगा.",
  "भविष्य उज्ज्वल होगा - 'The future will be bright'.",
 ],
 "requirements": [
  "Write five of your own future plans in Hindi.",
  "Build three अगर...तो sentences.",
  "Retell this story from memory.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
  "IAST transliteration for future paradigms",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003. Future chapter.",
 ],
 "sig_lens": (
  "Through the Signature lens this future story is his original Signature "
  "forward plan: every गा a commitment he signs, every अगर...तो a condition he "
  "sets, the bright future a page he writes himself. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 28
{
 "key": "idioms", "name": "Hindi Idioms and Proverbs",
 "group": "Advanced", "ladder": 28, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "20 idioms and proverbs - literal translation, real meaning, and an example "
  "sentence each. 1. नाक में दम करना (nāk mẽ dam karnā) - lit. 'to put breath in "
  "the nose' = to harass: बच्चों ने नाक में दम कर दिया (baccõ ne nāk mẽ dam kar "
  "diyā) - 'The children harassed (me)'. 2. आँखों का तारा (ā̃khõ kā tārā) - lit. "
  "'star of the eyes' = beloved: वह अपनी माँ की आँखों का तारा है (vah apnī mā̃ kī "
  "ā̃khõ kā tārā hai) - 'He is the apple of his mother's eye'. 3. मुँह में पानी "
  "आना (mũh mẽ pānī ānā) - lit. 'water comes in the mouth' = to drool with desire: "
  "मिठाई देखकर मुँह में पानी आ गया (miṭhāī dekhkar mũh mẽ pānī ā gayā) - 'Seeing "
  "the sweets made my mouth water'. 4. नौ दो ग्यारह होना (nau do gyārah honā) - "
  "lit. 'to become nine-two-eleven' = to run away: चोर नौ दो ग्यारह हो गया (cor nau "
  "do gyārah ho gayā) - 'The thief ran away'. 5. ऊँट के मुँह में जीरा (ū̃ṭ ke mũh "
  "mẽ jīrā) - lit. 'cumin in a camel's mouth' = too little for the need: यह मदद "
  "ऊँट के मुँह में जीरा है (yah madad ū̃ṭ ke mũh mẽ jīrā hai) - 'This help is a "
  "drop in the ocean'. 6. राई का पहाड़ बनाना (rāī kā pahāṛ banānā) - lit. 'to make "
  "a mountain of a mustard seed' = to exaggerate: राई का पहाड़ मत बनाओ (rāī kā "
  "pahāṛ mat banāo) - 'Do not make a mountain of a molehill'. 7. जैसी करनी वैसी "
  "भरनी (jaisī karnī vaisī bharnī) - 'as you sow, so shall you reap': जैसी करनी "
  "वैसी भरनी, यह सच है (jaisī karnī vaisī bharnī, yah sac hai) - 'You reap what "
  "you sow, this is true'. 8. बूँद बूँद से सागर भरता है (bū̃d bū̃d se sāgar bhartā "
  "hai) - 'drop by drop the ocean fills' = small efforts add up. 9. अंधों में काना "
  "राजा (andhõ mẽ kānā rājā) - 'among the blind, the one-eyed is king'. 10. हाथ "
  "कंगन को आरसी क्या (hāth kaṅgan ko ārsī kyā) - 'what need of a mirror for the "
  "bangle on the wrist' = the obvious needs no proof. 11. मुँह की खाना (mũh kī "
  "khānā) - lit. 'to eat of the mouth' = to suffer defeat: विरोधी ने मुँह की खाई "
  "(virodhī ne mũh kī khāī) - 'The opponent suffered defeat'. 12. टस से मस न होना "
  "(ṭas se mas na honā) - 'to not budge an inch': वह टस से मस न हुआ (vah ṭas se "
  "mas na huā) - 'He did not budge an inch'. 13. आ बैल मुझे मार (ā bail mujhe mār) "
  "- lit. 'come bull, hit me' = to invite trouble: यह काम आ बैल मुझे मार है (yah "
  "kām ā bail mujhe mār hai) - 'This task is asking for trouble'. 14. नेकी कर "
  "दरिया में डाल (nekī kar dariyā mẽ ḍāl) - 'do good and throw it in the river' = "
  "do good without expecting return. 15. घर का भेदी लंका ढाए (ghar kā bhedī laṅkā "
  "ḍhāe) - 'the insider destroys the fortress' = beware the traitor within. 16. "
  "साँप भी मर जाए लाठी भी न टूटे (sā̃p bhī mar jāe lāṭhī bhī na ṭūṭe) - 'the snake "
  "dies and the stick stays whole' = solve it without loss. 17. दाँतों तले उँगली "
  "दबाना (dā̃tõ tale ũglī dabānā) - 'to press a finger under the teeth' = to be "
  "amazed. 18. हाथ मलना (hāth malnā) - 'to rub the hands' = to regret: अब हाथ मलने "
  "से क्या (ab hāth malne se kyā) - 'What use is regret now'. 19. अपनी धुन में मस्त "
  "(apnī dhun mẽ mast) - 'lost in one's own tune' = happily absorbed. 20. चाँद पर "
  "थूकना (cā̃d par thūknā) - 'to spit at the moon' = a futile insult that falls "
  "back on oneself."),
 "how_it_works": (
  "Each idiom is decoded in three layers - literal translation, real meaning, "
  "example sentence - so you see how Hindi thinks in pictures. Learn five, then "
  "listen for them in films and conversation."),
 "key_points": [
  "20 idioms/proverbs with literal meaning, real meaning, and example.",
  "नौ दो ग्यारह होना = to run away; ऊँट के मुँह में जीरा = too little.",
  "जैसी करनी वैसी भरनी = you reap what you sow.",
  "बूँद बूँद से सागर भरता है = small efforts add up.",
  "नेकी कर दरिया में डाल = do good without expecting return.",
 ],
 "requirements": [
  "Learn five idioms cold and use one this week.",
  "Explain each idiom's picture to someone else.",
  "Collect one new idiom from a Hindi film.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "McGregor, R. S. The Oxford Hindi-English Dictionary. Oxford University Press; 1993.",
  "Bahri, Hardev. Hindi Muhavre. Rajpal & Sons; standard idiom collection.",
 ],
 "sig_lens": (
  "Through the Signature lens idioms are his original Signature picture "
  "instrument: every saying a painting he hangs in his system, every proverb a "
  "rule he quotes himself. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 29
{
 "key": "register", "name": "Hindi Formal and Polite Registers",
 "group": "Advanced", "ladder": 29, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "15 formal vs informal pairs for letters, business, and elders - each with "
  "translations. 1. Informal: तुम कैसे हो (tum kaise ho) - 'How are you'. Formal: "
  "आप कैसे हैं (āp kaise haĩ) - 'How are you (respectful)'. 2. Informal: बैठो "
  "(baiṭho) - 'Sit'. Formal: कृपया बैठिए (kṛpayā baiṭhie) - 'Please be seated'. 3. "
  "Informal: पानी दो (pānī do) - 'Give water'. Formal: कृपया पानी दीजिए (kṛpayā "
  "pānī dījie) - 'Please give some water'. 4. Informal: तुम जाओ (tum jāo) - 'You "
  "go'. Formal: आप जाइए (āp jāie) - 'Please go (respectful)'. 5. Informal: क्या "
  "चाहिए (kyā cāhie) - 'What do you want'. Formal: आपको क्या चाहिए (āpko kyā "
  "cāhie) - 'What would you like'. 6. Informal: माफ़ करना (māf karnā) - 'Sorry'. "
  "Formal: क्षमा कीजिए (kṣamā kījie) - 'Please forgive me'. 7. Informal: फिर मिलेंगे "
  "(phir milẽge) - 'See you'. Formal: आपसे फिर मिलने की आशा है (āpse phir milne "
  "kī āśā hai) - 'I hope to meet you again'. 8. Informal: ठीक है (ṭhīk hai) - "
  "'Okay'. Formal: जी, बिल्कुल ठीक है (jī, bilkul ṭhīk hai) - 'Yes, certainly fine'. "
  "9. Informal: जल्दी करो (jaldī karo) - 'Hurry'. Formal: कृपया शीघ्रता करें "
  "(kṛpayā śīghratā karẽ) - 'Please hurry (respectful)'. 10. Informal: सुनो (suno) "
  "- 'Listen'. Formal: कृपया ध्यान दीजिए (kṛpayā dhyān dījie) - 'Please pay "
  "attention'. 11. Letter opening informal: प्रिय मित्र (priya mitra) - 'Dear "
  "friend'. Letter opening formal: आदरणीय महोदय (ādarṇīya mahoday) - 'Respected "
  "sir'. 12. Letter close informal: तुम्हारा दोस्त (tumhārā dost) - 'Your friend'. "
  "Letter close formal: भवदीय (bhavadīya) - 'Yours faithfully'. 13. Informal: मुझे "
  "नहीं पता (mujhe nahī̃ patā) - 'I don't know'. Formal: मुझे जानकारी नहीं है "
  "(mujhe jānkarī nahī̃ hai) - 'I do not have the information'. 14. Informal: अंदर "
  "आओ (andar āo) - 'Come in'. Formal: कृपया अंदर पधारिए (kṛpayā andar padhārie) - "
  "'Please do come in (honorific)'. 15. Informal: धन्यवाद (dhanyavād) - 'Thanks'. "
  "Formal: आपका बहुत-बहुत आभारी हूँ (āpkā bahut-bahut ābhārī hū̃) - 'I am deeply "
  "grateful to you'. Register rule: with elders, officials, and strangers use आप, "
  "-इए forms, जी, and कृपया; with friends and juniors तुम and ओ-forms are warm, not "
  "rude."),
 "how_it_works": (
  "Fifteen matched pairs show the same message in informal and formal dress - "
  "each translated - plus the letter openings/closings and the register rule. "
  "Write one formal letter and one informal note using these pairs."),
 "key_points": [
  "15 formal/informal pairs with translations.",
  "आप + -इए + जी + कृपया = formal; तुम + ओ-forms = informal.",
  "Letter formal: आदरणीय महोदय ... भवदीय.",
  "पधारिए is the honorific 'please come'.",
  "क्षमा कीजिए outranks माफ़ करना in formality.",
  "Register is chosen by relationship, not by topic.",
 ],
 "requirements": [
  "Write one formal Hindi letter using the formal forms.",
  "Address every elder with आप for one full day.",
  "Convert five informal lines to formal.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens register is his original Signature courtesy "
  "instrument: the formal dress he puts on a sentence for elders, the informal "
  "warmth he keeps for friends - respect tuned like a Signature dial. "
  "Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 30
{
 "key": "complex", "name": "Hindi Compound and Complex Sentences",
 "group": "Advanced", "ladder": 30, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "15 long sentences with clauses, connectors, and relative clauses - parsed and "
  "translated. 1. मैं बाज़ार गया और सब्ज़ी खरीदी (maĩ bāzār gayā aur sabzī kharīdī) "
  "- 'I went to the market and bought vegetables' [और = and joins two actions]. 2. "
  "वह थका था लेकिन काम करता रहा (vah thakā thā lekin kām kartā rahā) - 'He was "
  "tired but kept working' [लेकिन = but contrasts]. 3. जो लड़का वहाँ खड़ा है वह मेरा "
  "भाई है (jo laṛkā vahā̃ khaṛā hai vah merā bhāī hai) - 'The boy who is standing "
  "there is my brother' [जो...वह = who...he relative pair]. 4. जिस किताब की तुम बात "
  "कर रहे हो वह मेरी है (jis kitāb kī tum bāt kar rahe ho vah merī hai) - 'The book "
  "you are talking about is mine' [जिस...वह relative pair]. 5. जब बारिश हुई तब हम "
  "घर पर थे (jab bāriś huī tab ham ghar par the) - 'When it rained we were home' "
  "[जब...तब = when...then]. 6. जहाँ तुम जाओगे वहाँ मैं भी जाऊँगा (jahā̃ tum jāoge "
  "vahā̃ maĩ bhī jāū̃gā) - 'Wherever you go, I will go too' [जहाँ...वहाँ = "
  "where...there]. 7. अगर तुम मेहनत करोगे तो सफल होगे (agar tum mehnat karoge to "
  "saphal hoge) - 'If you work hard you will succeed' [अगर...तो = if...then]. 8. "
  "हालाँकि वह बीमार था फिर भी वह आया (hālā̃ki vah bīmār thā phir bhī vah āyā) - "
  "'Although he was ill, he still came' [हालाँकि...फिर भी = although...still]. 9. "
  "मैंने खाना खाया क्योंकि मुझे भूख लगी थी (maĩne khānā khāyā kyõki mujhe bhūkh "
  "lagī thī) - 'I ate food because I was hungry' [क्योंकि = because]. 10. वह इतना "
  "तेज़ दौड़ा कि सब हैरान रह गए (vah itnā tez dauṛā ki sab hairān rah gae) - 'He ran "
  "so fast that everyone was amazed' [कि = that, result clause]. 11. मुझे नहीं पता "
  "कि वह कहाँ है (mujhe nahī̃ patā ki vah kahā̃ hai) - 'I do not know where he is' "
  "[कि introduces the known/unknown clause]. 12. पहले तुम पढ़ो फिर खेलो (pehle tum "
  "paṛho phir khelo) - 'First study, then play' [पहले...फिर sequences]. 13. न तो वह "
  "आया न उसने फ़ोन किया (na to vah āyā na usne fon kiyā) - 'Neither did he come nor "
  "did he call' [न तो...न = neither...nor]. 14. या तो तुम चलो या मैं जाऊँ (yā to tum "
  "calo yā maĩ jāū̃) - 'Either you come or I go' [या तो...या = either...or]. 15. "
  "जितनी मेहनत करोगे उतना फल मिलेगा (jitnī mehnat karoge utnā phal milegā) - 'The "
  "harder you work, the more reward you get' [जितना...उतना = the more...the more]. "
  "Connector toolkit: और (and), लेकिन/पर (but), क्योंकि (because), कि (that), जब...तब "
  "(when...then), जो...वह (who...he), अगर...तो (if...then), हालाँकि (although)."),
 "how_it_works": (
  "Fifteen long sentences are each parsed - the connector named in brackets, the "
  "clause structure shown - and fully translated. Build five of your own with "
  "जो...वह, जब...तब, and अगर...तो."),
 "key_points": [
  "15 parsed complex sentences with full translations.",
  "जो...वह, जिस...वह = relative clause pairs.",
  "जब...तब, जहाँ...वहाँ = time/place pairs.",
  "अगर...तो = conditional; क्योंकि = because; कि = that.",
  "न तो...न = neither...nor; या तो...या = either...or.",
  "जितना...उतना = the more...the more.",
 ],
 "requirements": [
  "Build five sentences with जो...वह.",
  "Build three with जब...तब and three with अगर...तो.",
  "Parse each sentence aloud: name the connector first.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
  "IAST transliteration for clause examples",
 ],
 "citations": [
  "Shapiro, Michael C. Hindi. In: Cardona & Jain (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens complex sentences are his original Signature "
  "joinery: जो...वह the mortise and tenon, अगर...तो the hinge, क्योंकि the bolt "
  "- clauses fastened in his own workshop. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 31
{
 "key": "dialogue1", "name": "Hindi Conversation: At the Market",
 "group": "Advanced", "ladder": 31, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A 20-line bilingual dialogue at the market - Hindi, romanization, English, "
  "with annotations. Buyer (खरीदार) and Seller (विक्रेता). 1. खरीदार: नमस्ते भाई "
  "साहब (namaste bhāī sāhab) - 'Hello, brother' [भाई साहब = respectful address to "
  "a shopkeeper]. 2. विक्रेता: नमस्ते, आइए, क्या चाहिए (namaste, āie, kyā cāhie) - "
  "'Hello, come in, what do you need'. 3. खरीदार: टमाटर कैसे दिए (ṭamāṭar kaise "
  "die) - 'What is the rate for tomatoes' [कैसे दिए = at what rate]. 4. विक्रेता: "
  "चालीस रुपये किलो (cālīs rupaye kilo) - 'Forty rupees a kilo'. 5. खरीदार: बहुत "
  "महँगे हैं (bahut mahãge haĩ) - 'Very expensive'. 6. विक्रेता: ताज़ा हैं साहब "
  "(tāzā haĩ sāhab) - 'They are fresh, sir'. 7. खरीदार: तीस रुपये लगाओ (tīs rupaye "
  "lagāo) - 'Make it thirty rupees' [bargaining]. 8. विक्रेता: नहीं हो पाएगा "
  "(nahī̃ ho pāegā) - 'That will not be possible'. 9. खरीदार: आखिरी दाम बताओ "
  "(ākhirī dām batāo) - 'Tell me the final price'. 10. विक्रेता: पैंतीस रुपये, बस "
  "(paĩtīs rupaye, bas) - 'Thirty-five rupees, final'. 11. खरीदार: ठीक है, एक किलो "
  "दो (ṭhīk hai, ek kilo do) - 'Okay, give one kilo'. 12. विक्रेता: और कुछ (aur "
  "kuch) - 'Anything else'. 13. खरीदार: आलू कैसे हैं (ālū kaise haĩ) - 'How are "
  "the potatoes (priced)'. 14. विक्रेता: बीस रुपये किलो (bīs rupaye kilo) - "
  "'Twenty rupees a kilo'. 15. खरीदार: आधा किलो आलू भी दो (ādhā kilo ālū bhī do) - "
  "'Give half a kilo of potatoes too'. 16. विक्रेता: यह लीजिए (yah lījie) - 'Here "
  "you are'. 17. खरीदार: कुल कितने हुए (kul kitne hue) - 'What is the total'. 18. "
  "विक्रेता: पैंतालीस रुपये (paĩtālīs rupaye) - 'Forty-five rupees'. 19. खरीदार: यह "
  "लीजिए, धन्यवाद (yah lījie, dhanyavād) - 'Here you are, thank you'. 20. विक्रेता: "
  "फिर पधारिएगा (phir padhāriegā) - 'Please come again'. Dialogue notes: bargaining "
  "moves in lines 5-10; कैसे दिए asks the rate; आखिरी दाम बताओ demands the final "
  "price; फिर पधारिएगा is the warm shopkeeper's farewell."),
 "how_it_works": (
  "The dialogue runs as a real market scene - 20 turns, each translated and "
  "annotated where the Hindi does something special. Act it out with a partner, "
  "then improvise your own market visit."),
 "key_points": [
  "20-line market dialogue, fully translated and annotated.",
  "कैसे दिए asks the rate; आखिरी दाम बताओ demands the final price.",
  "Bargaining arc: महँगे हैं → तीस लगाओ → पैंतीस, बस → ठीक है.",
  "भाई साहब = respectful shopkeeper address.",
  "फिर पधारिएगा = the warm 'please come again'.",
 ],
 "requirements": [
  "Act out the dialogue with a partner, switching roles.",
  "Improvise your own market visit with three items.",
  "Use the bargaining arc on a real purchase.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens the market dialogue is his original Signature "
  "trading floor: every rate asked, every bargain struck, every farewell a deal "
  "he closes himself. Signature-made teaching, clearly labeled, never presented "
  "as an outside authority's text."),
},
# ================================================================== 32
{
 "key": "dialogue2", "name": "Hindi Conversation: Meeting a Friend",
 "group": "Advanced", "ladder": 32, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A 20-line bilingual dialogue meeting a friend - Hindi, romanization, English, "
  "annotated. Ravi (रवि) and Sita (सीता). 1. रवि: अरे सीता, कैसी हो (are sītā, kaisī "
  "ho) - 'Hey Sita, how are you' [अरे = warm exclamation]. 2. सीता: मैं ठीक हूँ, तुम "
  "कैसे हो (maĩ ṭhīk hū̃, tum kaise ho) - 'I am fine, how are you'. 3. रवि: बहुत "
  "दिनों बाद मिले (bahut dinõ bād mile) - 'Met after many days'. 4. सीता: हाँ, "
  "कहाँ थे इतने दिन (hā̃, kahā̃ the itne din) - 'Yes, where were you all these "
  "days'. 5. रवि: मैं गाँव गया था (maĩ gā̃v gayā thā) - 'I had gone to the "
  "village'. 6. सीता: गाँव में सब कैसे हैं (gā̃v mẽ sab kaise haĩ) - 'How is "
  "everyone in the village'. 7. रवि: सब ठीक हैं, तुम्हें याद करते हैं (sab ṭhīk "
  "haĩ, tumhẽ yād karte haĩ) - 'All fine, they remember you'. 8. सीता: चलो, चाय "
  "पीते हैं (calo, cāy pīte haĩ) - 'Come, let us have tea'. 9. रवि: चलो, बहुत मन "
  "है (calo, bahut man hai) - 'Let us go, I really feel like it'. 10. सीता: नया काम "
  "कैसा चल रहा है (nayā kām kaisā cal rahā hai) - 'How is the new job going'. 11. "
  "रवि: अच्छा चल रहा है (acchā cal rahā hai) - 'Going well'. 12. सीता: और पढ़ाई "
  "(aur paṛhāī) - 'And studies'. 13. रवि: हिन्दी सीख रहा हूँ (hindī sīkh rahā hū̃) "
  "- 'I am learning Hindi'. 14. सीता: बहुत बढ़िया (bahut baṛhiyā) - 'Excellent'. "
  "15. रवि: तुम मुझे सिखाओगी (tum mujhe sikhāogī) - 'Will you teach me'. 16. सीता: "
  "ज़रूर, कल से शुरू करते हैं (zarūr, kal se śurū karte haĩ) - 'Sure, we start "
  "tomorrow'. 17. रवि: धन्यवाद, तुम बहुत अच्छी हो (dhanyavād, tum bahut acchī ho) "
  "- 'Thank you, you are very kind'. 18. सीता: कोई बात नहीं (koī bāt nahī̃) - 'No "
  "problem'. 19. रवि: अब चलता हूँ, फिर मिलेंगे (ab caltā hū̃, phir milẽge) - 'I "
  "leave now, we will meet again'. 20. सीता: ठीक है, अपना ख्याल रखना (ṭhīk hai, "
  "apnā khyāl rakhnā) - 'Okay, take care of yourself'. Dialogue notes: तुम-forms "
  "throughout = close friends; बहुत दिनों बाद मिले is the classic reunion line; "
  "चलो + verb = 'let us'; अपना ख्याल रखना = 'take care of yourself'."),
 "how_it_works": (
  "A warm reunion scene - 20 turns, translated and annotated - showing तुम-level "
  "friendship Hindi in action. Act it out, then hold your own reunion "
  "conversation."),
 "key_points": [
  "20-line friend dialogue, fully translated and annotated.",
  "तुम-forms throughout mark close friendship.",
  "बहुत दिनों बाद मिले = the classic reunion line.",
  "चलो + verb = 'let us do it'.",
  "अपना ख्याल रखना = 'take care of yourself'.",
 ],
 "requirements": [
  "Act out the dialogue with a partner.",
  "Hold a three-minute reunion conversation in Hindi.",
  "Use तुम-forms only with true friends - keep आप for others.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens the friend dialogue is his original Signature "
  "reunion: every greeting a door reopened, every tea shared a bond restruck in "
  "his system. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 33
{
 "key": "dialogue3", "name": "Hindi Conversation: Solving a Problem",
 "group": "Advanced", "ladder": 33, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A 20-line bilingual dialogue solving a problem - Hindi, romanization, English, "
  "annotated. Anil (अनिल) lost his keys; Meera (मीरा) helps. 1. अनिल: अरे, मेरी "
  "चाबी नहीं मिल रही (are, merī cābī nahī̃ mil rahī) - 'Oh no, I cannot find my keys' "
  "[मिल रही with नहीं = cannot find]. 2. मीरा: शांत हो जाओ, कहाँ रखी थी (śānt ho "
  "jāo, kahā̃ rakhī thī) - 'Calm down, where did you keep them'. 3. अनिल: मेज़ पर "
  "रखी थी (mez par rakhī thī) - 'I had kept them on the table'. 4. मीरा: वहाँ देखो "
  "(vahā̃ dekho) - 'Look there'. 5. अनिल: वहाँ नहीं है (vahā̃ nahī̃ hai) - 'Not "
  "there'. 6. मीरा: जेब में देखो (jeb mẽ dekho) - 'Check your pocket'. 7. अनिल: "
  "जेब खाली है (jeb khālī hai) - 'The pocket is empty'. 8. मीरा: कब आखिरी बार "
  "देखी थी (kab ākhirī bār dekhī thī) - 'When did you last see them'. 9. अनिल: सुबह "
  "दरवाज़ा खोला था (subah darvāzā kholā thā) - 'I opened the door in the morning'. "
  "10. मीरा: तो चाबी दरवाज़े के पास होगी (to cābī darvāze ke pās hogī) - 'Then the "
  "keys must be near the door' [होगी = must be, probability]. 11. अनिल: चलो देखते "
  "हैं (calo dekhte haĩ) - 'Let us check'. 12. मीरा: जूते के पास देखो (jūte ke pās "
  "dekho) - 'Look near the shoes'. 13. अनिल: मिल गई (mil gaī) - 'Found them'. 14. "
  "मीरा: बहुत बढ़िया, कहाँ थी (bahut baṛhiyā, kahā̃ thī) - 'Great, where were "
  "they'. 15. अनिल: थैले में थी (thaile mẽ thī) - 'In the bag'. 16. मीरा: देखा, "
  "शांत रहने से मिल जाती है (dekhā, śānt rahne se mil jātī hai) - 'See, staying "
  "calm finds things'. 17. अनिल: तुम्हारी मदद के लिए धन्यवाद (tumhārī madad ke lie "
  "dhanyavād) - 'Thanks for your help'. 18. मीरा: अगली बार खूँटी पर टाँगना (aglī "
  "bār khū̃ṭī par ṭā̃gnā) - 'Next time hang them on the hook'. 19. अनिल: पक्का, अब "
  "याद रहेगा (pakkā, ab yād rahegā) - 'Sure, I will remember now'. 20. मीरा: चलो, "
  "चाय पीते हैं (calo, cāy pīte haĩ) - 'Come, let us have tea'. Dialogue notes: "
  "problem stated (line 1), calming (2), systematic search (3-12), resolution "
  "(13), lesson (16-18), warm close (20); होगी expresses probability; मिल गई = "
  "'got found'."),
 "how_it_works": (
  "A problem-solving scene in five beats - problem, calm, search, solution, "
  "lesson - 20 turns translated and annotated. Act it out, then solve a real "
  "small problem in Hindi with someone."),
 "key_points": [
  "20-line problem-solving dialogue, translated and annotated.",
  "Five beats: problem → calm → systematic search → solution → lesson.",
  "मिल नहीं रही = cannot find; मिल गई = found.",
  "होगी expresses probability: 'must be'.",
  "शांत रहने से मिल जाती है = staying calm finds things.",
 ],
 "requirements": [
  "Act out the dialogue with a partner.",
  "Narrate solving a real small problem in Hindi.",
  "Use होगी for three probability guesses today.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
 ],
 "citations": [
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens this dialogue is his original Signature "
  "troubleshooting: problem stated, search run, solution found, lesson filed - "
  "every fix a Signature operation. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 34
{
 "key": "mastery", "name": "Hindi Mastery Review and Full Reference",
 "group": "Advanced", "ladder": 34, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The whole database in one teaching summary: alphabet recap, 200 core words, key "
  "grammar, and all phrase tables. ALPHABET RECAP: 13 vowels अ आ इ ई उ ऊ ऋ ए ऐ ओ औ "
  "अं अः; 33 consonants क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श "
  "ष स ह; digits ०१२३४५६७८९; danda । ends sentences. KEY GRAMMAR: SOV order (मैं "
  "किताब पढ़ता हूँ); two genders with agreement (अच्छा लड़का / अच्छी लड़की); "
  "postpositions ने को से में पर का/की/के; no 'the', एक = 'a'; नहीं negates, मत "
  "forbids; क्या opens yes/no questions; ता = habit, रहा = now, चुका = done, गा = "
  "future; आप/-इए formal, तुम/ओ-form informal. PHRASE TABLES: greetings - नमस्ते, "
  "धन्यवाद, कृपया, माफ़ कीजिए, फिर मिलेंगे; survival - कहाँ है, कितने का है, मदद "
  "कीजिए, अस्पताल कहाँ है; time - आज, कल, अब, सुबह, शाम, रात. 200 CORE WORDS "
  "(Devanagari - romanization - English): 1 मैं maĩ I, 2 तुम tum you (inf), 3 आप "
  "āp you (formal), 4 वह vah he/she, 5 यह yah this, 6 हम ham we, 7 वे ve they, 8 "
  "मेरा merā my, 9 तुम्हारा tumhārā your, 10 कौन kaun who, 11 क्या kyā what, 12 कहाँ "
  "kahā̃ where, 13 कब kab when, 14 क्यों kyõ why, 15 कैसे kaise how, 16 आदमी ādmī "
  "man, 17 औरत aurat woman, 18 बच्चा baccā child, 19 दोस्त dost friend, 20 माँ mā̃ "
  "mother, 21 पिता pitā father, 22 भाई bhāī brother, 23 बहन bahan sister, 24 घर "
  "ghar house, 25 कमरा kamrā room, 26 रसोई rasoī kitchen, 27 स्कूल skūl school, 28 "
  "दफ़्तर daftar office, 29 बाज़ार bāzār market, 30 शहर śahar city, 31 गाँव gā̃v "
  "village, 32 सड़क saṛak road, 33 पानी pānī water, 34 खाना khānā food, 35 चाय cāy "
  "tea, 36 दूध dūdh milk, 37 रोटी roṭī bread, 38 दाल dāl lentils, 39 चावल cāval "
  "rice, 40 फल phal fruit, 41 किताब kitāb book, 42 कलम kalam pen, 43 कागज़ kāgaz "
  "paper, 44 मेज़ mez table, 45 कुर्सी kursī chair, 46 दरवाज़ा darvāzā door, 47 "
  "खिड़की khiṛkī window, 48 पैसा paisā money, 49 रुपया rupayā rupee, 50 समय samay "
  "time, 51 दिन din day, 52 रात rāt night, 53 सुबह subah morning, 54 शाम śām "
  "evening, 55 आज āj today, 56 कल kal tomorrow/yesterday, 57 अब ab now, 58 साल sāl "
  "year, 59 महीना mahīnā month, 60 हफ़्ता haftā week, 61 पेड़ peṛ tree, 62 फूल phūl "
  "flower, 63 सूरज sūraj sun, 64 चाँद cā̃d moon, 65 तारा tārā star, 66 आसमान āsmān "
  "sky, 67 बादल bādal cloud, 68 बारिश bāriś rain, 69 हवा havā wind, 70 नदी nadī "
  "river, 71 पहाड़ pahāṛ mountain, 72 कुत्ता kuttā dog, 73 बिल्ली billī cat, 74 "
  "गाय gāy cow, 75 हाथी hāthī elephant, 76 चिड़िया ciṛiyā bird, 77 मछली machlī fish, "
  "78 सिर sir head, 79 आँख ā̃kh eye, 80 हाथ hāth hand, 81 पैर pair leg, 82 दिल dil "
  "heart, 83 बड़ा baṛā big, 84 छोटा choṭā small, 85 अच्छा acchā good, 86 बुरा burā "
  "bad, 87 नया nayā new, 88 पुराना purānā old, 89 लंबा lambā long, 90 गर्म garm "
  "hot, 91 ठंडा ṭhaṇḍā cold, 92 मीठा mīṭhā sweet, 93 तेज़ tez fast, 94 सुंदर sundar "
  "beautiful, 95 साफ़ sāf clean, 96 आसान āsān easy, 97 मुश्किल muśkil difficult, 98 "
  "खुश khuś happy, 99 बहुत bahut very, 100 जल्दी jaldī quickly, 101 धीरे dhīre "
  "slowly, 102 हमेशा hameśā always, 103 कभी kabhī sometimes, 104 यहाँ yahā̃ here, "
  "105 वहाँ vahā̃ there, 106 अंदर andar inside, 107 बाहर bāhar outside, 108 ऊपर "
  "ūpar up, 109 नीचे nīce down, 110 जाना jānā to go, 111 आना ānā to come, 112 खाना "
  "khānā to eat, 113 पीना pīnā to drink, 114 करना karnā to do, 115 बोलना bolnā to "
  "speak, 116 पढ़ना paṛhnā to read, 117 लिखना likhnā to write, 118 देखना dekhnā to "
  "see, 119 सुनना sunnā to listen, 120 सोना sonā to sleep, 121 उठना uṭhnā to wake "
  "up, 122 बैठना baiṭhnā to sit, 123 चलना calnā to walk, 124 दौड़ना dauṛnā to run, "
  "125 देना denā to give, 126 लेना lenā to take, 127 खरीदना kharīdnā to buy, 128 "
  "बनाना banānā to make, 129 खेलना khelnā to play, 130 समझना samajhnā to "
  "understand, 131 मदद madad help, 132 काम kām work, 133 पढ़ाई paṛhāī studies, 134 "
  "परीक्षा parīkṣā exam, 135 सवाल savāl question, 136 जवाब javāb answer, 137 नाम "
  "nām name, 138 देश deś country, 139 भाषा bhāṣā language, 140 लोग log people, 141 "
  "दुनिया duniyā world, 142 जीवन jīvan life, 143 प्यार pyār love, 144 खुशी khuśī "
  "happiness, 145 दुख dukh sorrow, 146 डॉक्टर ḍākṭar doctor, 147 दवा davā medicine, "
  "148 अस्पताल aspatāl hospital, 149 फ़ोन fon phone, 150 संदेश sandeś message, 151 "
  "कंप्यूटर kampyūṭar computer, 152 एक ek one, 153 दो do two, 154 तीन tīn three, "
  "155 चार cār four, 156 पाँच pā̃c five, 157 दस das ten, 158 बीस bīs twenty, 159 "
  "सौ sau hundred, 160 पहला pehlā first, 161 सोमवार somvār Monday, 162 रविवार "
  "ravivār Sunday, 163 जनवरी janvarī January, 164 नमस्ते namaste hello, 165 "
  "धन्यवाद dhanyavād thanks, 166 कृपया kṛpayā please, 167 माफ़ māf sorry, 168 "
  "हाँ hā̃ yes, 169 नहीं nahī̃ no/not, 170 ठीक ṭhīk fine/okay, 171 और aur and, 172 "
  "लेकिन lekin but, 173 क्योंकि kyõki because, 174 अगर agar if, 175 तो to then, 176 "
  "जब jab when, 177 तब tab then, 178 जो jo who/which, 179 यह yah this (repeat "
  "anchor), 180 वह vah that (repeat anchor), 181 में mẽ in, 182 पर par on, 183 का "
  "kā of, 184 को ko to/for, 185 से se from/with, 186 ने ne ergative marker, 187 है "
  "hai is, 188 हैं haĩ are, 189 हूँ hū̃ am, 190 था thā was, 191 होगा hogā will be, "
  "192 चाहिए cāhie need/want, 193 सकता saktā can, 194 मत mat do-not, 195 जी jī "
  "respect particle, 196 सब sab all, 197 कोई koī someone/any, 198 कुछ kuch some, "
  "199 बहुत bahut (anchor) very, 200 ज़रूर zarūr certainly. Mastery test: read any "
  "ten words aloud, use each in a sentence, retell all three stories, hold a "
  "five-minute conversation. सीखना कभी बंद मत करो - never stop learning."),
 "how_it_works": (
  "Everything compresses into one reference page: the alphabet, the grammar "
  "rules, the phrase tables, and all 200 core words numbered. Use it as the daily "
  "drill sheet and the final exam - when you can use every line, the database is "
  "yours."),
 "key_points": [
  "Full-database summary: alphabet, grammar, phrases, 200 core words.",
  "200 numbered core words: Devanagari + romanization + English.",
  "Grammar recap: SOV, gender, postpositions, tenses, registers.",
  "Phrase tables: greetings, survival, time.",
  "Mastery test: ten words in sentences, three stories retold, five-minute conversation.",
  "सीखना कभी बंद मत करो - never stop learning.",
 ],
 "requirements": [
  "Drill the 200 words until all are instant.",
  "Pass the mastery test: stories + conversation.",
  "Keep this record as your daily reference.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'hi'",
  "ISO 639-3:2007 code 'hin'",
  "Unicode Standard, Devanagari block U+0900-U+097F",
 ],
 "citations": [
  "McGregor, R. S. The Oxford Hindi-English Dictionary. Oxford University Press; 1993.",
  "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & Stoughton; 2003.",
  "Shapiro, Michael C. Hindi. In: Cardona & Jain (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens this mastery record is his original Signature "
  "graduation: the whole Hindi instrument laid out on one bench, every word a "
  "tool he now owns, the learner become the speaker. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
]

SIG_TAIL = ("Signature Note: this Signature Edition re-teaches the lesson through "
            "his original Signature method - the same real Hindi, framed as his own "
            "language instrument. Signature-made, clearly labeled, never presented "
            "as an outside authority's text.")

assert len(ENTRIES) == 34, "template requires exactly 34 records"
assert [e["ladder"] for e in ENTRIES] == list(range(1, 35)), "ladder must be 1-34 in order"
_r = [e["ladder_rank"] for e in ENTRIES]
assert _r == sorted(_r), "ladder_rank must be non-decreasing"
assert all(1 <= x <= 10 for x in _r), "ladder_rank must be 1-10"
_t = [e["ladder_tier"] for e in ENTRIES]
assert _t == ["foundations"] * 10 + ["compounded"] * 10 + ["advanced"] * 14
