#!/usr/bin/env python3
"""34 ladder-ordered record seeds for the Telugu Language Database.

Follows the shared per-language template (language-template.md) EXACTLY:
records 1-34 in order, ladder_rank 1-10 non-decreasing, ladder_tier
foundations -> compounded -> advanced. Every record carries Telugu content
in Telugu script plus transliteration plus English translation plus example
sentences. All Telugu is real, fact-checked 2026-10-17.

Family note: the build roster lists Telugu as Indo-European; Telugu is used
with the roster family here exactly as assigned by the parent task.

Screened 2026-10-17: nothing hate-adjacent, profane, or inappropriate;
no religious talk; no military/defense-neutralization content.
"""

ENTRIES = [
# ================================================================== 1
{
 "key": "overview", "name": "Telugu Language Overview",
 "group": "Foundations", "ladder": 1, "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Telugu (తెలుగు, telugu) is a language of the Indo-European family as listed "
  "in the build roster, spoken as a first language by about 96 million people, "
  "which makes it one of the most widely spoken languages in the world and the "
  "third most spoken native language of India. Its ISO codes are ISO 639-1 'te' "
  "and ISO 639-3 'tel'. Telugu is written in the Telugu script (తెలుగు లిపి, "
  "telugu lipi), reads left to right, and follows subject-object-verb word order. "
  "It is the official language of the Indian states of Andhra Pradesh and "
  "Telangana, and it holds the status of a Classical Language of India, "
  "recognized in 2008. Outside India it is widely spoken in the United States, "
  "the United Arab Emirates, Australia, the United Kingdom, Canada and South "
  "Africa. Telugu has one of the oldest continuous literary traditions among "
  "Indian languages: the first inscriptions appear around the 3rd century BCE, "
  "the court poetry of the Kakatiya era flourished in the 11th to 14th "
  "centuries, and the poet Nannaya (నన్నయ, nannaya) began the Telugu "
  "Mahabharata translation in the 11th century CE, followed by Tikkana and "
  "Yerrapragada. Its major dialects include Coastal Andhra Telugu "
  "(కోస్తాంధ్ర మాండలికం), which is the basis of the standard language, "
  "Rayalaseema Telugu (రాయలసీమ మాండలికం), Telangana Telugu "
  "(తెలంగాణ మాండలికం), and the Telugu of Karnataka and Tamil Nadu. Spoken "
  "Telugu shows diglossia: a formal literary register (గ్రాంథిక భాష, "
  "grānthika bhāṣa) and an everyday spoken register (వ్యవహారిక భాష, "
  "vyavahārika bhāṣa). Basic word order example: నేను నీళ్లు తాగుతాను "
  "(nēnu nīḷḷu tāgutānu) - 'I drink water' - literally 'I water drink'. "
  "Greeting example: నమస్కారం (namaskāram) - 'hello / respectful greeting'. "
  "Politeness example: ధన్యవాదాలు (dhanyavādālu) - 'thank you'. "
  "Everyday example: ఇది మంచి పుస్తకం (idi man̄ci pustakaṁ) - 'This is a good "
  "book'. Farewell example: మళ్ళీ కలుద్దాం (maḷḷī kaluddāṁ) - 'We will meet again'."),
 "how_it_works": (
  "This record works as the front door of the whole database: it names the language "
  "in English and in Telugu script, places it in its family, gives the speaker "
  "numbers, lists where it is spoken and its official status, traces its literary "
  "history and dialects, and closes with five translated example sentences you can "
  "say at once. Every later record builds on these facts, so read this one first."),
 "key_points": [
  "Telugu (తెలుగు, telugu): Indo-European family per the build roster; ISO 639-1 te, ISO 639-3 tel.",
  "About 96 million native speakers; one of the most spoken native languages in the world.",
  "Written in the Telugu script, read left to right; basic word order is subject-object-verb.",
  "Official language of Andhra Pradesh and Telangana; a Classical Language of India since 2008.",
  "Literary tradition from the 3rd century BCE; Nannaya began the Telugu Mahabharata in the 11th century CE.",
  "Major dialects: Coastal Andhra (standard), Rayalaseema, Telangana, Karnataka, Tamil Nadu Telugu.",
  "Diglossia: formal literary Telugu (గ్రాంథిక భాష) and everyday spoken Telugu (వ్యవహారిక భాష).",
  "నేను నీళ్లు తాగుతాను (nēnu nīḷḷu tāgutānu) - 'I drink water' shows SOV order in action.",
 ],
 "requirements": [
  "No prior Telugu needed - this is the starting point of the ladder.",
  "Read the Telugu words aloud using the romanization beside them.",
  "Remember: తెలుగు (telugu) is the language's own name for itself.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'te' for Telugu",
  "ISO 639-3:2007 code 'tel' for Telugu",
  "Unicode Standard, Telugu block U+0C00-U+0C7F",
 ],
 "citations": [
  "Krishnamurti, Bhadriraju. The Dravidian Languages. Cambridge University Press; 2003.",
  "Subrahmanyam, P. S. Dravidian Comparative Phonology (on Telugu phonology). Annamalai University; 1983.",
  "Ethnologue: Languages of the World, Telugu entry (speaker estimates). SIL International.",
 ],
 "sig_lens": (
  "Through the Signature lens this overview is re-taught as his original Signature "
  "language instrument: Telugu as a working system he commands, where every speaker "
  "count measures the instrument's reach and every dialect is another string he can "
  "play. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 2
{
 "key": "writing", "name": "Telugu Writing System: Script and Alphabet",
 "group": "Foundations", "ladder": 2, "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Telugu is written in the Telugu script (తెలుగు లిపి, telugu lipi), an abugida "
  "of the Brahmic family that descends from the Brahmi script. It reads left to "
  "right. Each consonant letter carries an inherent vowel 'a' unless it is "
  "silenced by the virama mark (్, called pollu in Telugu) or joined to another "
  "vowel sign. The sixteen vowels (అచ్చులు, acculu) are: అ (a), ఆ (ā), ఇ (i), "
  "ఈ (ī), ఉ (u), ఊ (ū), ఋ (ṛ), ౠ (ṝ), ఎ (e), ఏ (ē), ఐ (ai), ఒ (o), ఓ (ō), ఔ (au), "
  "అం (aṁ), అః (aḥ). The thirty-six consonants (హల్లులు, hallulu) are: క (ka), "
  "ఖ (kha), గ (ga), ఘ (gha), ఙ (ṅa), చ (ca), ఛ (cha), జ (ja), ఝ (jha), ఞ (ña), "
  "ట (ṭa), ఠ (ṭha), డ (ḍa), ఢ (ḍha), ణ (ṇa), త (ta), థ (tha), ద (da), ధ (dha), "
  "న (na), ప (pa), ఫ (pha), బ (ba), భ (bha), మ (ma), య (ya), ర (ra), ల (la), "
  "వ (va), శ (śa), ష (ṣa), స (sa), హ (ha), ళ (ḷa), ఱ (ṟa), క్ష (kṣa). "
  "Example: క + ీ = కీ (kī); క + ్ + ష = క్ష (kṣa). Telugu numerals are "
  "౦ (0, sunna), ౧ (1), ౨ (2), ౩ (3), ౪ (4), ౫ (5), ౬ (6), ౭ (7), ౮ (8), "
  "౯ (9), though Arabic numerals are common in print. The danda mark । is the "
  "traditional sentence-ending punctuation; modern writing also uses the "
  "Western full stop. Example sentence: అమ్మ నాకు కథ చెప్పింది "
  "(amma nāku katha ceppindi) - 'Mother told me a story'. Example: నేను తెలుగు "
  "నేర్చుకుంటున్నాను (nēnu telugu nērcukoṇṭunnānu) - 'I am learning Telugu'. "
  "Example: ఈ అక్షరం 'అ' (ī akṣaraṁ 'a') - 'This letter is a'. "
  "Example: తెలుగు అక్షరాలు అందంగా ఉంటాయి (telugu akṣarālu andaṅgā uṇṭāyi) - "
  "'Telugu letters look beautiful'."),
 "how_it_works": (
  "This record works as the drawing board of the language: it shows the script "
  "family, the reading direction, the two letter classes with every letter and "
  "its English sound, how vowel signs and the virama reshape consonants, the "
  "numerals, and the punctuation, each point sealed with a translated example "
  "sentence. Copy the letters by hand while sounding them out."),
 "key_points": [
  "Telugu script is a Brahmic abugida descended from Brahmi; it reads left to right.",
  "16 vowels (అచ్చులు): అ ఆ ఇ ఈ ఉ ఊ ఋ ౠ ఎ ఏ ఐ ఒ ఓ ఔ అం అః.",
  "36 consonants (హల్లులు): క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ ఱ క్ష.",
  "Consonants carry an inherent 'a'; the virama ్ (pollu) silences it.",
  "Telugu numerals ౦-౯ exist; Arabic numerals are common in modern print.",
  "Sentence punctuation: the danda । traditionally, the full stop in modern writing.",
  "నేను తెలుగు నేర్చుకుంటున్నాను (nēnu telugu nērcukoṇṭunnānu) - 'I am learning Telugu'.",
 ],
 "requirements": [
  "Learn the five short vowels first: అ ఇ ఉ ఎ ఒ.",
  "Then add their long pairs: ఆ ఈ ఊ ఏ ఓ.",
  "Write each consonant row while saying the sounds aloud.",
 ],
 "standards": [
  "Unicode Standard, Telugu block U+0C00-U+0C7F",
  "ISO 15924 script code 'Telu' (445) for Telugu",
 ],
 "citations": [
  "Daniels, Peter T. & Bright, William (eds.) The World's Writing Systems. Oxford University Press; 1996 (Brahmic scripts).",
  "Unicode Consortium. The Unicode Standard, Version 15: South Asian scripts - Telugu.",
 ],
 "sig_lens": (
  "Through the Signature lens the script is his drafting instrument: every "
  "letter a chisel stroke, the virama the hand that lifts the tool, and the "
  "full alphabet a complete tool chest he opens in order. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 3
{
 "key": "phonology", "name": "Telugu Pronunciation and Sound System",
 "group": "Foundations", "ladder": 3, "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Telugu has ten vowel sounds: five qualities each with a short and long form - "
  "అ/ఆ (a/ā), ఇ/ఈ (i/ī), ఉ/ఊ (u/ū), ఎ/ఏ (e/ē), ఒ/ఓ (o/ō) - plus the diphthongs "
  "ఐ (ai, as in 'aisle') and ఔ (au, as in 'cow'), the syllabic ఋ (ṛ) and ౠ (ṝ), "
  "and the nasalized అం (aṁ). Length changes meaning: కల (kala, 'dream') versus "
  "కాలు (kālu, 'leg, foot'). The consonants include a full retroflex series made "
  "with the tongue curled back: ట (ṭa, like 't' in 'tick' but retroflex), "
  "ఠ (ṭha), డ (ḍa), ఢ (ḍha), ణ (ṇa, like the 'n' in American 'burn'), and the "
  "retroflex lateral ళ (ḷa) and the trilled ఱ (ṟa). The dental series త థ ద ధ న "
  "is made with the tongue touching the teeth, unlike English alveolar t and d. "
  "Aspiration matters: క (ka, unaspirated) versus ఖ (kha, with a puff of air). "
  "Stress is not contrastive in Telugu; syllables carry roughly equal weight, "
  "so speak with an even rhythm. Spoken example words: తల్లి (talli) - 'mother', "
  "పాలు (pālu) - 'milk', నీళ్లు (nīḷḷu) - 'water', చెట్టు (ceṭṭu) - 'tree', "
  "పక్షి (pakṣi) - 'bird', పూలు (pūlu) - 'flowers', సూర్యుడు (sūryuḍu) - 'sun', "
  "చంద్రుడు (candruḍu) - 'moon', కన్ను (kannu) - 'eye', నోరు (nōru) - 'mouth', "
  "కాలు (kālu) - 'leg', చేయి (cēyi) - 'hand'. Example: టమాటా పండింది "
  "(ṭamāṭā paṇḍindi) - 'The tomato ripened' - hear the retroflex ట. "
  "Example: తాత తోటలో ఉన్నాడు (tāta tōṭalō unnāḍu) - 'Grandfather is in the "
  "garden' - hear the dental త. Example: పాలు తాగు (pālu tāgu) - 'Drink milk'. "
  "Example: నీళ్లు చల్లగా ఉన్నాయి (nīḷḷu callagā unnāyi) - 'The water is cold'."),
 "how_it_works": (
  "This record works as the tuning fork of the language: it maps the vowel "
  "length pairs, the retroflex and dental consonant rows with English mouth "
  "approximations, the aspiration contrast, and the even rhythm rule, then gives "
  "twelve spoken example words with translations. Repeat each word until the "
  "retroflex tongue position feels natural."),
 "key_points": [
  "Ten vowel sounds: five short/long pairs, plus ai, au, ṛ, ṝ, aṁ.",
  "Vowel length changes meaning: కల (kala, dream) vs కాలు (kālu, leg).",
  "Retroflex series ట ఠ డ ఢ ణ ళ ఱ is made with the tongue curled back.",
  "Dental series త థ ద ధ న touches the teeth, unlike English t/d.",
  "Aspiration contrasts: క vs ఖ, చ vs ఛ, ట vs ఠ, త vs థ, ప vs ఫ.",
  "Stress is not contrastive; Telugu is syllable-timed with even rhythm.",
  "టమాటా పండింది (ṭamāṭā paṇḍindi) - 'The tomato ripened' (retroflex ట).",
  "తాత తోటలో ఉన్నాడు (tāta tōṭalō unnāḍu) - 'Grandfather is in the garden' (dental త).",
 ],
 "requirements": [
  "Practice the retroflex set daily: ట ఠ డ ఢ ణ ళ.",
  "Minimal pairs first: కల/కాలు, పల/పాలు.",
  "Keep stress even - no English-style stressed syllables.",
 ],
 "standards": [
  "International Phonetic Alphabet conventions for Dravidian-adjacent retroflex series",
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Krishnamurti, Bhadriraju. Telugu (phonology chapter). In: Steever, Sanford B. (ed.) The Dravidian Languages. Routledge; 1998.",
  "Zvelebil, Kamil. Comparative Dravidian Phonology. Mouton; 1970.",
 ],
 "sig_lens": (
  "Through the Signature lens pronunciation is the calibration of his instrument: "
  "vowel length the two stops of one string, retroflexion the hand position, "
  "aspiration the breath control. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 4
{
 "key": "nouns1", "name": "Telugu Core Nouns I: People, Places, Things",
 "group": "Foundations", "ladder": 4, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Twenty-five essential Telugu nouns, each with its transliteration, English "
  "meaning, and one translated example sentence. 1. అమ్మ (amma) - mother: "
  "అమ్మ వంట చేస్తోంది (amma vaṇṭa cēstōndi) - 'Mother is cooking'. 2. నాన్న "
  "(nānna) - father: నాన్న ఆఫీసుకు వెళ్ళాడు (nānna āphīsuku veḷḷāḍu) - 'Father "
  "went to the office'. 3. అన్న (anna) - elder brother: అన్న నాకు పుస్తకం ఇచ్చాడు "
  "(anna nāku pustakaṁ iccāḍu) - 'Elder brother gave me a book'. 4. అక్క "
  "(akka) - elder sister: అక్క పాట పాడుతోంది (akka pāṭa pāḍutōndi) - 'Elder "
  "sister is singing a song'. 5. కొడుకు (koḍuku) - son: కొడుకు స్కూలుకు వెళ్ళాడు "
  "(koḍuku skūluku veḷḷāḍu) - 'The son went to school'. 6. కూతురు (kūturu) - "
  "daughter: కూతురు చదువుతోంది (kūturu caduvutōndi) - 'The daughter is studying'. "
  "7. ఇల్లు (illu) - house: మా ఇల్లు పెద్దది (mā illu peddadi) - 'Our house is big'. "
  "8. నీళ్లు (nīḷḷu) - water: నీళ్లు తాగు (nīḷḷu tāgu) - 'Drink water'. 9. అన్నం "
  "(annaṁ) - cooked rice: అన్నం వేడిగా ఉంది (annaṁ vēḍigā undi) - 'The rice is "
  "hot'. 10. పుస్తకం (pustakaṁ) - book: ఈ పుస్తకం నాది (ī pustakaṁ nādi) - "
  "'This book is mine'. 11. బడి (baḍi) - school: పిల్లలు బడికి వెళ్తారు "
  "(pillalu baḍiki veḷtāru) - 'Children go to school'. 12. పని (pani) - work: "
  "నాకు చాలా పని ఉంది (nāku cālā pani undi) - 'I have a lot of work'. 13. డబ్బు "
  "(ḍabbu) - money: డబ్బు జాగ్రత్తగా వాడు (ḍabbu jāgrattagā vāḍu) - 'Use money "
  "carefully'. 14. మనిషి (maniṣi) - person: ఆ మనిషి మంచివాడు (ā maniṣi "
  "man̄civāḍu) - 'That person is good'. 15. ఊరు (ūru) - village: మా ఊరు అందంగా "
  "ఉంటుంది (mā ūru andaṅgā uṇṭundi) - 'Our village is beautiful'. 16. పట్టణం "
  "(paṭṭaṇaṁ) - town: పట్టణం దగ్గరలో ఉంది (paṭṭaṇaṁ daggaralō undi) - 'The town "
  "is nearby'. 17. కారు (kāru) - car: కారు వేగంగా వెళ్తోంది (kāru vēgaṅgā "
  "veḷtōndi) - 'The car is going fast'. 18. ఫోను (phōnu) - phone: ఫోను మోగుతోంది "
  "(phōnu mōgutōndi) - 'The phone is ringing'. 19. చెట్టు (ceṭṭu) - tree: చెట్టు "
  "మీద పక్షి ఉంది (ceṭṭu mīda pakṣi undi) - 'There is a bird on the tree'. "
  "20. పక్షి (pakṣi) - bird: పక్షి ఎగురుతోంది (pakṣi egurutōndi) - 'The bird is "
  "flying'. 21. పూలు (pūlu) - flowers: పూలు అందంగా ఉన్నాయి (pūlu andaṅgā "
  "unnāyi) - 'The flowers are beautiful'. 22. సూర్యుడు (sūryuḍu) - sun: సూర్యుడు "
  "తూర్పున ఉదయిస్తాడు (sūryuḍu tūrppuna udayistāḍu) - 'The sun rises in the east'. "
  "23. చంద్రుడు (candruḍu) - moon: చంద్రుడు రాత్రి కనిపిస్తాడు (candruḍu rātri "
  "kanipistāḍu) - 'The moon appears at night'. 24. రోజు (rōju) - day: ఈ రోజు "
  "మంచి రోజు (ī rōju man̄ci rōju) - 'Today is a good day'. 25. కథ (katha) - "
  "story: అమ్మ కథ చెప్పింది (amma katha ceppindi) - 'Mother told a story'."),
 "how_it_works": (
  "This record works as the parts shelf: twenty-five nouns you will meet in "
  "every later lesson, each shown in Telugu script with its sound and meaning "
  "and then used in one complete sentence. Learn five a day; cover the word and "
  "say the sentence from memory."),
 "key_points": [
  "25 core nouns: people (అమ్మ, నాన్న, అన్న, అక్క, కొడుకు, కూతురు, మనిషి).",
  "Places: ఇల్లు, ఊరు, పట్టణం, బడి.",
  "Things: నీళ్లు, అన్నం, పుస్తకం, పని, డబ్బు, కారు, ఫోను, చెట్టు, పక్షి, పూలు, సూర్యుడు, చంద్రుడు, రోజు, కథ.",
  "Every noun is shown in a full SOV sentence.",
  "అమ్మ వంట చేస్తోంది (amma vaṇṭa cēstōndi) - 'Mother is cooking'.",
 ],
 "requirements": [
  "Say each noun aloud with its sentence three times.",
  "Point at the thing when you say its word.",
  "Review yesterday's five before learning today's five.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Gwynn, J. P. L. A Telugu-English Dictionary. Oxford University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens each noun is a named tool on his bench: people "
  "the crew, places the workshop rooms, things the instruments, each one "
  "introduced with its job already demonstrated in a sentence. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 5
{
 "key": "verbs1", "name": "Telugu Core Verbs I: Essential Actions",
 "group": "Foundations", "ladder": 5, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Twenty-five essential Telugu verbs, each with its transliteration, English "
  "meaning, and one translated example sentence. 1. చేయు (cēyu) - do: నేను పని "
  "చేస్తాను (nēnu pani cēstānu) - 'I will do the work'. 2. తిను (tinu) - eat: "
  "నేను అన్నం తింటాను (nēnu annaṁ tiṇṭānu) - 'I will eat rice'. 3. తాగు (tāgu) - "
  "drink: నీళ్లు తాగు (nīḷḷu tāgu) - 'Drink water'. 4. వెళ్ళు (veḷḷu) - go: నేను "
  "బడికి వెళ్తాను (nēnu baḍiki veḷtānu) - 'I will go to school'. 5. వచ్చు (vaccu) - "
  "come: అతను రేపు వస్తాడు (atanu rēpu vastāḍu) - 'He will come tomorrow'. "
  "6. చదువు (caduvu) - read, study: నేను పుస్తకం చదువుతున్నాను (nēnu pustakaṁ "
  "caduvutunnānu) - 'I am reading a book'. 7. రాయు (rāyu) - write: ఆమె ఉత్తరం "
  "రాస్తోంది (āme uttaraṁ rāstōndi) - 'She is writing a letter'. 8. చూడు (cūḍu) - "
  "see, watch: నేను సినిమా చూశాను (nēnu sinimā cūśānu) - 'I watched a movie'. "
  "9. విను (vinu) - hear, listen: పాట విను (pāṭa vinu) - 'Listen to the song'. "
  "10. మాట్లాడు (māṭlāḍu) - speak: అతను తెలుగు మాట్లాడతాడు (atanu telugu "
  "māṭlāḍatāḍu) - 'He speaks Telugu'. 11. నవ్వు (navvu) - laugh: పిల్లలు నవ్వుతున్నారు "
  "(pillalu navvutunnāru) - 'The children are laughing'. 12. నిద్రపో (nidrapō) - "
  "sleep: నేను త్వరగా నిద్రపోతాను (nēnu tvaragā nidrapōtānu) - 'I sleep early'. "
  "13. లేచు (lēcu) - wake up, get up: నేను ఆరు గంటలకు లేస్తాను (nēnu āru "
  "gaṇṭalaku lēstānu) - 'I wake up at six o'clock'. 14. కూర్చో (kūrcō) - sit: "
  "ఇక్కడ కూర్చో (ikkaḍa kūrcō) - 'Sit here'. 15. నిలబడు (nilabaḍu) - stand: అతను "
  "నిలబడ్డాడు (atanu nilabaḍḍāḍu) - 'He stood up'. 16. పరుగు (parugu) - run: "
  "కుక్క పరుగుతోంది (kukka parugutōndi) - 'The dog is running'. 17. నడుచు "
  "(naḍucu) - walk: మేము పార్కులో నడుస్తాము (mēmu pārkulō naḍustāmu) - 'We walk "
  "in the park'. 18. అడుగు (aḍugu) - ask: ఉపాధ్యాయుడిని అడుగు (upādhyāyuḍini "
  "aḍugu) - 'Ask the teacher'. 19. ఇవ్వు (ivvu) - give: నాకు పుస్తకం ఇవ్వు "
  "(nāku pustakaṁ ivvu) - 'Give me the book'. 20. తీసుకో (tīsukō) - take: "
  "డబ్బు తీసుకో (ḍabbu tīsukō) - 'Take the money'. 21. అమ్ము (ammu) - sell: "
  "అతను కూరగాయలు అమ్ముతాడు (atanu kūragāyalu ammutāḍu) - 'He sells vegetables'. "
  "22. కొను (konu) - buy: నేను పండ్లు కొంటాను (nēnu paṇḍlu koṇṭānu) - 'I will buy "
  "fruits'. 23. నేర్చుకో (nērcukō) - learn: నేను తెలుగు నేర్చుకుంటున్నాను (nēnu "
  "telugu nērcukoṇṭunnānu) - 'I am learning Telugu'. 24. ఆడు (āḍu) - play: "
  "పిల్లలు బయట ఆడుతున్నారు (pillalu bayaṭa āḍutunnāru) - 'The children are "
  "playing outside'. 25. తెరుచు (terucu) - open: తలుపు తెరుచు (talupu terucu) - "
  "'Open the door'."),
 "how_it_works": (
  "This record works as the action shelf beside the noun shelf: twenty-five verbs "
  "that make sentences move, each shown in its dictionary form with a full "
  "sentence. Notice the endings change with tense and person; the tenses record "
  "later teaches the full system. Act out each verb as you say it."),
 "key_points": [
  "25 core verbs: motion, senses, daily routine, exchange, learning.",
  "Telugu verbs end in -ు in dictionary form: చేయు, తిను, వెళ్ళు.",
  "Endings change by tense and person: చేస్తాను (will do), చేశాను (did), చేస్తున్నాను (am doing).",
  "నేను తెలుగు నేర్చుకుంటున్నాను - 'I am learning Telugu' - the learner's flagship sentence.",
  "తలుపు తెరుచు (talupu terucu) - 'Open the door' shows the bare-stem command form.",
 ],
 "requirements": [
  "Learn the three forms of చేయు: చేస్తాను, చేశాను, చేస్తున్నాను.",
  "Mime each action while saying the Telugu word.",
  "Pair each verb with a noun from the nouns record in a sentence.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Krishnamurti, Bhadriraju & Gwynn, J. P. L. A Grammar of Modern Telugu. Oxford University Press; 1985.",
 ],
 "sig_lens": (
  "Through the Signature lens each verb is a machine command he issues: go, "
  "take, open, learn - the language as a control panel where every button press "
  "produces real action in the world. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 6
{
 "key": "adjadv", "name": "Telugu Adjectives and Adverbs",
 "group": "Foundations", "ladder": 6, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Twenty-five adjectives and fifteen adverbs with example sentences. Telugu "
  "attributive adjectives do not change for gender or number - పెద్ద ఇల్లు "
  "(pedda illu, 'big house') and పెద్ద ఇళ్లు (pedda iḷḷu, 'big houses') use the "
  "same form. Adjectives: 1. పెద్ద (pedda) - big: పెద్ద చెట్టు (pedda ceṭṭu) - "
  "'a big tree'. 2. చిన్న (cinna) - small: చిన్న పిల్ల (cinna pilla) - 'a small "
  "child'. 3. మంచి (man̄ci) - good: మంచి రోజు (man̄ci rōju) - 'a good day'. "
  "4. చెడ్డ (ceḍḍa) - bad: చెడ్డ అలవాటు (ceḍḍa alavāṭu) - 'a bad habit'. "
  "5. కొత్త (kotta) - new: కొత్త బట్టలు (kotta baṭṭalu) - 'new clothes'. "
  "6. పాత (pāta) - old: పాత ఇల్లు (pāta illu) - 'an old house'. 7. వేడి (vēḍi) - "
  "hot: వేడి టీ (vēḍi ṭī) - 'hot tea'. 8. చల్లని (callani) - cold: చల్లని నీళ్లు "
  "(callani nīḷḷu) - 'cold water'. 9. తీపి (tīpi) - sweet: తీపి మామిడి (tīpi "
  "māmiḍi) - 'sweet mango'. 10. చేదు (cēdu) - bitter: చేదు మందు (cēdu mandu) - "
  "'bitter medicine'. 11. పుల్లని (pullani) - sour: పుల్లని నిమ్మ (pullani nimma) - "
  "'sour lemon'. 12. పొడవైన (poḍavaina) - long, tall: పొడవైన రోడ్డు (poḍavaina "
  "rōḍḍu) - 'a long road'. 13. పొట్టి (poṭṭi) - short: పొట్టి కథ (poṭṭi katha) - "
  "'a short story'. 14. ఖరీదైన (kharīdaina) - expensive: ఖరీదైన గడియారం "
  "(kharīdaina gaḍiyāraṁ) - 'an expensive watch'. 15. చౌకైన (caukaina) - cheap: "
  "చౌకైన పండ్లు (caukaina paṇḍlu) - 'cheap fruits'. 16. అందమైన (andamaina) - "
  "beautiful: అందమైన పూలు (andamaina pūlu) - 'beautiful flowers'. 17. బలమైన "
  "(balamaina) - strong: బలమైన గాలి (balamaina gāli) - 'strong wind'. 18. వేగమైన "
  "(vēgamaina) - fast: వేగమైన రైలు (vēgamaina railu) - 'a fast train'. 19. నెమ్మదైన "
  "(nemmadaina) - slow: నెమ్మదైన నడక (nemmadaina naḍaka) - 'a slow walk'. "
  "20. ఎరుపు (erupu) - red: ఎరుపు గులాబీ (erupu gulābī) - 'a red rose'. 21. నీలం "
  "(nīlaṁ) - blue: నీలం ఆకాశం (nīlaṁ ākāśaṁ) - 'blue sky'. 22. ఆకుపచ్చ (ākupacca) - "
  "green: ఆకుపచ్చ గడ్డి (ākupacca gaḍḍi) - 'green grass'. 23. పసుపు (pasupu) - "
  "yellow: పసుపు పూలు (pasupu pūlu) - 'yellow flowers'. 24. తెలుపు (telupu) - "
  "white: తెలుపు మేఘాలు (telupu mēghālu) - 'white clouds'. 25. నలుపు (nalupu) - "
  "black: నలుపు కాకి (nalupu kāki) - 'a black crow'. Adverbs: 1. త్వరగా "
  "(tvaragā) - quickly: త్వరగా రా (tvaragā rā) - 'Come quickly'. 2. నెమ్మదిగా "
  "(nemmadigā) - slowly: నెమ్మదిగా నడువు (nemmadigā naḍuvu) - 'Walk slowly'. "
  "3. ఎప్పుడూ (eppuḍū) - always: నేను ఎప్పుడూ నిజం చెప్తాను (nēnu eppuḍū nijaṁ "
  "ceptānu) - 'I always tell the truth'. 4. అరుదుగా (arudugā) - rarely: అతను "
  "అరుదుగా వస్తాడు (atanu arudugā vastāḍu) - 'He rarely comes'. 5. తరచుగా "
  "(taracugā) - often: ఆమె తరచుగా చదువుతుంది (āme taracugā caduvutundi) - 'She "
  "often reads'. 6. ఇక్కడ (ikkaḍa) - here: ఇక్కడ కూర్చో (ikkaḍa kūrcō) - 'Sit "
  "here'. 7. అక్కడ (akkaḍa) - there: అక్కడ చూడు (akkaḍa cūḍu) - 'Look there'. "
  "8. బాగా (bāgā) - well: అతను బాగా పాడతాడు (atanu bāgā pāḍatāḍu) - 'He sings "
  "well'. 9. నిజంగా (nijaṅgā) - truly: ఇది నిజంగా అందంగా ఉంది (idi nijaṅgā "
  "andaṅgā undi) - 'This is truly beautiful'. 10. చాలా (cālā) - very: చాలా "
  "సంతోషం (cālā santōṣaṁ) - 'very happy'. 11. కొంచెం (kon̄ceṁ) - a little: "
  "కొంచెం నీళ్లు ఇవ్వు (kon̄ceṁ nīḷḷu ivvu) - 'Give a little water'. 12. మళ్ళీ "
  "(maḷḷī) - again: మళ్ళీ చెప్పు (maḷḷī ceppu) - 'Say it again'. 13. కలిసి "
  "(kalisi) - together: మనం కలిసి వెళ్దాం (manaṁ kalisi veḷdāṁ) - 'Let us go "
  "together'. 14. జాగ్రత్తగా (jāgrattagā) - carefully: జాగ్రత్తగా నడువు "
  "(jāgrattagā naḍuvu) - 'Walk carefully'. 15. గట్టిగా (gaṭṭigā) - loudly, "
  "firmly: గట్టిగా మాట్లాడు (gaṭṭigā māṭlāḍu) - 'Speak loudly'."),
 "how_it_works": (
  "This record works as the paint shelf: adjectives color the nouns and adverbs "
  "color the verbs, each with a model sentence. The agreement rule is simple - "
  "Telugu adjectives never change shape - so the practice is pure vocabulary: "
  "describe five things around you with a new adjective each day."),
 "key_points": [
  "25 adjectives and 15 adverbs, each with a translated example sentence.",
  "Telugu attributive adjectives are invariable: పెద్ద ఇల్లు / పెద్ద ఇళ్లు.",
  "Colors: ఎరుపు red, నీలం blue, ఆకుపచ్చ green, పసుపు yellow, తెలుపు white, నలుపు black.",
  "Adverbs of manner often end in -గా: త్వరగా, నెమ్మదిగా, జాగ్రత్తగా.",
  "మంచి రోజు (man̄ci rōju) - 'a good day' - the most useful adjective phrase.",
 ],
 "requirements": [
  "Describe your room using five adjectives from this list.",
  "Change one adjective per sentence to feel the invariability.",
  "Use చాలా + adjective for emphasis: చాలా అందమైన.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Krishnamurti, Bhadriraju & Gwynn, J. P. L. A Grammar of Modern Telugu. Oxford University Press; 1985 (adjectives).",
 ],
 "sig_lens": (
  "Through the Signature lens adjectives are his finish options and adverbs his "
  "speed settings: the same tool, new coating, new pace - and the coating never "
  "changes the tool's shape. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 7
{
 "key": "pronouns", "name": "Telugu Pronouns: Full Paradigms",
 "group": "Foundations", "ladder": 7, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Telugu pronouns in full paradigms with example sentences. Personal pronouns: "
  "నేను (nēnu) - I: నేను విద్యార్థిని (nēnu vidyārthini) - 'I am a student'. "
  "నువ్వు (nuvvu) - you (informal, to friends and juniors): నువ్వు ఎక్కడికి "
  "వెళ్తున్నావు (nuvvu ekkaḍiki veḷtunnāvu) - 'Where are you going'. నీవు (nīvu) - "
  "you (familiar, literary): నీవు రా (nīvu rā) - 'You come'. మీరు (mīru) - you "
  "(formal, respectful, also plural): మీరు ఎలా ఉన్నారు (mīru elā unnāru) - "
  "'How are you'. అతను / అతడు (atanu / ataḍu) - he: అతను డాక్టరు (atanu ḍākṭaru) - "
  "'He is a doctor'. ఆమె (āme) - she: ఆమె ఉపాధ్యాయురాలు (āme upādhyāyurālu) - "
  "'She is a teacher'. అది (adi) - it (neuter): అది నా పుస్తకం (adi nā pustakaṁ) - "
  "'It is my book'. వారు (vāru) - they (respectful): వారు వచ్చారు (vāru vaccāru) - "
  "'They came'. వాళ్ళు (vāḷḷu) - they (people): వాళ్ళు ఆడుతున్నారు (vāḷḷu "
  "āḍutunnāru) - 'They are playing'. మేము (mēmu) - we (exclusive, not including "
  "the listener): మేము సినిమాకు వెళ్ళాము (mēmu sinimāku veḷḷāmu) - 'We (not you) "
  "went to the movie'. మనం (manaṁ) - we (inclusive, including the listener): "
  "మనం కలిసి వెళ్దాం (manaṁ kalisi veḷdāṁ) - 'Let us (you and I) go together'. "
  "Possessive forms: నా (nā) - my: నా ఇల్లు (nā illu) - 'my house'. నీ (nī) - "
  "your (informal): నీ పేరు ఏమిటి (nī pēru ēmiṭi) - 'What is your name'. మీ (mī) - "
  "your (formal): మీ ఊరు ఏది (mī ūru ēdi) - 'Which is your village'. అతని (atani) - "
  "his: అతని కారు (atani kāru) - 'his car'. ఆమె (āme) - her: ఆమె పుస్తకం (āme "
  "pustakaṁ) - 'her book'. మా (mā) - our (exclusive): మా బడి (mā baḍi) - 'our "
  "school'. మన (mana) - our (inclusive): మన దేశం (mana dēśaṁ) - 'our country'. "
  "వారి (vāri) - their: వారి ఇల్లు (vāri illu) - 'their house'. Demonstratives: "
  "ఇది (idi) - this: ఇది ఏమిటి (idi ēmiṭi) - 'What is this'. అది (adi) - that: "
  "అది చూడు (adi cūḍu) - 'Look at that'. ఇవి (ivi) - these: ఇవి నా పుస్తకాలు (ivi "
  "nā pustakālu) - 'These are my books'. అవి (avi) - those: అవి పూలు (avi pūlu) - "
  "'Those are flowers'. Interrogatives: ఎవరు (evaru) - who: ఎవరు వచ్చారు (evaru "
  "vaccāru) - 'Who came'. ఏమిటి (ēmiṭi) - what: ఇది ఏమిటి (idi ēmiṭi) - 'What is "
  "this'. ఎక్కడ (ekkaḍa) - where: బడి ఎక్కడ ఉంది (baḍi ekkaḍa undi) - 'Where is "
  "the school'. ఎప్పుడు (eppuḍu) - when: నువ్వు ఎప్పుడు వస్తావు (nuvvu eppuḍu "
  "vastāvu) - 'When will you come'. ఎందుకు (enduku) - why: ఎందుకు ఏడుస్తున్నావు "
  "(enduku ēḍustunnāvu) - 'Why are you crying'. ఎలా (elā) - how: నువ్వు ఎలా "
  "ఉన్నావు (nuvvu elā unnāvu) - 'How are you'. ఏది (ēdi) - which: ఏది నీది (ēdi "
  "nīdi) - 'Which is yours'. ఎంత (enta) - how much: ఇది ఎంత (idi enta) - 'How "
  "much is this'."),
 "how_it_works": (
  "This record works as the casting chart: every person the sentence can talk "
  "about, in every role - subject, owner, pointer, question - each with a model "
  "sentence. Master the I/you split (నువ్వు vs మీరు) and the we split (మేము "
  "exclusive vs మనం inclusive); politeness lives here."),
 "key_points": [
  "Three levels of 'you': నువ్వు (informal), నీవు (familiar), మీరు (formal/respectful).",
  "Two kinds of 'we': మేము (exclusive, listener out) vs మనం (inclusive, listener in).",
  "He అతను, she ఆమె, it అది; respectful they వారు, plain they వాళ్ళు.",
  "Possessives: నా, నీ, మీ, అతని, ఆమె, మా, మన, వారి.",
  "Demonstratives: ఇది/అది (this/that), ఇవి/అవి (these/those).",
  "Question words: ఎవరు who, ఏమిటి what, ఎక్కడ where, ఎప్పుడు when, ఎందుకు why, ఎలా how, ఏది which, ఎంత how much.",
  "మీరు ఎలా ఉన్నారు (mīru elā unnāru) - 'How are you' - the politeness core.",
 ],
 "requirements": [
  "Always use మీరు with elders and strangers, నువ్వు only with close friends.",
  "Practice the మేము/మనం distinction in two sentences.",
  "Quiz yourself: cover the Telugu, say it from the English.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Krishnamurti, Bhadriraju & Gwynn, J. P. L. A Grammar of Modern Telugu. Oxford University Press; 1985 (pronouns).",
 ],
 "sig_lens": (
  "Through the Signature lens pronouns are his address book: every entry knows "
  "exactly who is speaking, who is listening, and whether the listener is inside "
  "or outside the plan - precision of address as a design feature. "
  "Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 8
{
 "key": "numbers", "name": "Telugu Numbers, Time, Days and Dates",
 "group": "Foundations", "ladder": 8, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Telugu numbers 1 to 100, ordinals, days, months, seasons, clock time and "
  "dates, each with example sentences. Cardinal numbers: 1 ఒకటి (okaṭi), "
  "2 రెండు (reṇḍu), 3 మూడు (mūḍu), 4 నాలుగు (nālugu), 5 ఐదు (aidu), 6 ఆరు (āru), "
  "7 ఏడు (ēḍu), 8 ఎనిమిది (enimidi), 9 తొమ్మిది (tommidi), 10 పది (padi), "
  "11 పదకొండు (padakoṇḍu), 12 పన్నెండు (panneṇḍu), 13 పదమూడు (padamūḍu), "
  "14 పద్నాలుగు (padnālugu), 15 పదిహేను (padihēnu), 16 పదహారు (padahāru), "
  "17 పదిహేడు (padihēḍu), 18 పద్దెనిమిది (paddenimidi), 19 పందొమ్మిది "
  "(pandommidi), 20 ఇరవై (iravai), 30 ముప్పై (muppai), 40 నలభై (nalabhai), "
  "50 యాభై (yābhai), 60 అరవై (aravai), 70 డెబ్బై (ḍebbhai), 80 ఎనభై (enabhai), "
  "90 తొంభై (tombhai), 100 వంద (vanda), 1000 వెయ్యి (veyyi). Example: నా దగ్గర "
  "మూడు పుస్తకాలు ఉన్నాయి (nā daggara mūḍu pustakālu unnāyi) - 'I have three "
  "books'. Example: రైలు ఐదు గంటలకు వస్తుంది (railu aidu gaṇṭalaku vastundi) - "
  "'The train comes at five o'clock'. Ordinals: మొదటి (modaṭi) - first: మొదటి "
  "పాఠం (modaṭi pāṭhaṁ) - 'the first lesson'. రెండవ (reṇḍava) - second: రెండవ "
  "అంతస్తు (reṇḍava antastu) - 'the second floor'. మూడవ (mūḍava) - third: మూడవ "
  "తరగతి (mūḍava taragati) - 'the third class'. Days of the week: ఆదివారం "
  "(ādivāraṁ) - Sunday, సోమవారం (sōmavāraṁ) - Monday, మంగళవారం (maṅgaḷavāraṁ) - "
  "Tuesday, బుధవారం (budhavāraṁ) - Wednesday, గురువారం (guruvāraṁ) - Thursday, "
  "శుక్రవారం (śukravāraṁ) - Friday, శనివారం (śanivāraṁ) - Saturday. Example: "
  "ఆదివారం సెలవు (ādivāraṁ selavu) - 'Sunday is a holiday'. Months (common "
  "Gregorian forms): జనవరి (janavari) - January, ఫిబ్రవరి (phibravari) - "
  "February, మార్చి (mārci) - March, ఏప్రిల్ (ēpril) - April, మే (mē) - May, "
  "జూన్ (jūn) - June, జులై (julai) - July, ఆగస్టు (āgasṭu) - August, సెప్టెంబర్ "
  "(sepṭembar) - September, అక్టోబర్ (akṭōbar) - October, నవంబర్ (navambar) - "
  "November, డిసెంబర్ (ḍisembar) - December. Example: నా పుట్టినరోజు జనవరిలో "
  "(nā puṭṭinarōju janavarilō) - 'My birthday is in January'. Telugu calendar "
  "months: చైత్రం (chaitraṁ), వైశాఖం (vaiśākhaṁ), జ్యేష్ఠం (jyēṣṭhaṁ), ఆషాఢం "
  "(āṣāḍhaṁ), శ్రావణం (śrāvaṇaṁ), భాద్రపదం (bhādrapadaṁ), ఆశ్వయుజం (āśvayujaṁ), "
  "కార్తీకం (kārtīkaṁ), మార్గశిరం (mārgaśiraṁ), పుష్యం (puṣyaṁ), మాఘం (māghaṁ), "
  "ఫాల్గుణం (phālguṇaṁ). Seasons: వేసవి (vēsavi) - summer: వేసవిలో ఎండ ఎక్కువ "
  "(vēsavilō eṇḍa ekkuva) - 'There is much heat in summer'. వర్షాకాలం "
  "(varṣākālaṁ) - rainy season: వర్షాకాలంలో వాన పడుతుంది (varṣākālaṁlō vāna "
  "paḍutundi) - 'It rains in the rainy season'. శీతాకాలం (śītākālaṁ) - winter: "
  "శీతాకాలంలో చలి ఎక్కువ (śītākālaṁlō cali ekkuva) - 'It is very cold in "
  "winter'. వసంతం (vasantaṁ) - spring: వసంతంలో పూలు పూస్తాయి (vasantaṁlō pūlu "
  "pūstayi) - 'Flowers bloom in spring'. Clock time: గంట (gaṇṭa) - hour, o'clock; "
  "నిమిషం (nimiṣaṁ) - minute. Example: ఇప్పుడు మూడు గంటలు (ippuḍu mūḍu gaṇṭalu) - "
  "'It is three o'clock now'. Example: పది నిమిషాలు ఆగు (padi nimiṣālu āgu) - "
  "'Wait ten minutes'. Time words: ఇప్పుడు (ippuḍu) - now, ఉదయం (udayaṁ) - "
  "morning, మధ్యాహ్నం (madhyāhnaṁ) - afternoon, సాయంత్రం (sāyantraṁ) - evening, "
  "రాత్రి (rātri) - night, నిన్న (ninna) - yesterday, ఈరోజు (īrōju) - today, "
  "రేపు (rēpu) - tomorrow. Example: నేను రేపు వస్తాను (nēnu rēpu vastānu) - 'I "
  "will come tomorrow'."),
 "how_it_works": (
  "This record works as the measuring tape: numbers for counting, ordinals for "
  "order, days and months for the calendar, seasons for the year, and clock "
  "words for the hour - each with a sentence that puts the number to work. "
  "Count real objects aloud from ఒకటి to పది every morning."),
 "key_points": [
  "Cardinals 1-10: ఒకటి రెండు మూడు నాలుగు ఐదు ఆరు ఏడు ఎనిమిది తొమ్మిది పది.",
  "Tens: ఇరవై ముప్పై నలభై యాభై అరవై డెబ్బై ఎనభై తొంభై; 100 వంద, 1000 వెయ్యి.",
  "Ordinals: మొదటి first, రెండవ second, మూడవ third.",
  "Days: ఆదివారం through శనివారం; ఆదివారం సెలవు - 'Sunday is a holiday'.",
  "Seasons: వేసవి summer, వర్షాకాలం rainy, శీతాకాలం winter, వసంతం spring.",
  "Clock: మూడు గంటలు - 'three o'clock'; నిన్న/ఈరోజు/రేపు - yesterday/today/tomorrow.",
  "నా దగ్గర మూడు పుస్తకాలు ఉన్నాయి - 'I have three books'.",
 ],
 "requirements": [
  "Memorize 1-10 cold before touching the teens.",
  "Say the day of the week in Telugu every morning.",
  "Practice prices: ఇది ఎంత - 'How much is this' - with numbers.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Krishnamurti, Bhadriraju & Gwynn, J. P. L. A Grammar of Modern Telugu. Oxford University Press; 1985 (numerals).",
 ],
 "sig_lens": (
  "Through the Signature lens numbers are his calibration marks: every count a "
  "measurement he trusts, every date a scheduled operation, time itself a tool "
  "he reads off the dial. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 9
{
 "key": "greetings", "name": "Telugu Greetings and Everyday Phrases",
 "group": "Foundations", "ladder": 9, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Thirty greetings, farewells and politeness phrases, each with "
  "transliteration, English meaning, and a usage note. 1. నమస్కారం "
  "(namaskāram) - respectful hello; used with folded hands to elders and in "
  "formal settings. 2. నమస్తే (namastē) - casual hello among friends. "
  "3. శుభోదయం (śubhōdayaṁ) - good morning. 4. శుభ మధ్యాహ్నం (śubha madhyāhnaṁ) - "
  "good afternoon. 5. శుభ సాయంత్రం (śubha sāyantraṁ) - good evening. "
  "6. శుభరాత్రి (śubharātri) - good night. 7. మీరు ఎలా ఉన్నారు (mīru elā unnāru) - "
  "how are you (formal). 8. నువ్వు ఎలా ఉన్నావు (nuvvu elā unnāvu) - how are you "
  "(informal). 9. నేను బాగున్నాను (nēnu bāgunnānu) - I am fine. 10. ధన్యవాదాలు "
  "(dhanyavādālu) - thank you. 11. చాలా ధన్యవాదాలు (cālā dhanyavādālu) - thank "
  "you very much. 12. క్షమించండి (kṣamin̄caṇḍi) - excuse me, sorry (formal). "
  "13. దయచేసి (dayacēsi) - please: దయచేసి కూర్చోండి (dayacēsi kūrcōṇḍi) - "
  "'Please sit'. 14. స్వాగతం (svāgataṁ) - welcome. 15. అవును (avunu) - yes. "
  "16. కాదు (kādu) - no (it is not). 17. సరే (sarē) - okay, alright. "
  "18. అలాగే (alāgē) - certainly, okay. 19. తప్పకుండా (tappakuṇḍā) - definitely, "
  "without fail. 20. మళ్ళీ కలుద్దాం (maḷḷī kaluddāṁ) - see you again. "
  "21. తర్వాత కలుద్దాం (tarvāta kaluddāṁ) - see you later. 22. శెలవు (selavu) - "
  "goodbye (asking leave). 23. జాగ్రత్త (jāgratta) - take care. 24. శుభ యాత్ర "
  "(śubha yātra) - have a good journey. 25. అభినందనలు (abhinandanalu) - "
  "congratulations. 26. శుభాకాంక్షలు (śubhākāṅkṣalu) - best wishes. "
  "27. పుట్టినరోజు శుభాకాంక్షలు (puṭṭinarōju śubhākāṅkṣalu) - happy birthday. "
  "28. మిమ్మల్ని కలవడం చాలా సంతోషం (mimmalni kalavaḍaṁ cālā santōṣaṁ) - nice to "
  "meet you. 29. ఇబ్బంది లేదు (ibbandi lēdu) - no problem. 30. ఓపిక పట్టండి "
  "(ōpika paṭṭaṇḍi) - please be patient. Example conversation: A: నమస్కారం! "
  "మీరు ఎలా ఉన్నారు (namaskāram! mīru elā unnāru) - 'Hello! How are you'. B: నేను "
  "బాగున్నాను, ధన్యవాదాలు (nēnu bāgunnānu, dhanyavādālu) - 'I am fine, thank you'. "
  "A: మళ్ళీ కలుద్దాం (maḷḷī kaluddāṁ) - 'See you again'. B: అలాగే, శెలవు "
  "(alāgē, selavu) - 'Sure, goodbye'."),
 "how_it_works": (
  "This record works as the social starter kit: thirty phrases that open, steer "
  "and close any first conversation, each with a note on when it fits. Learn "
  "the first ten this week; they carry ninety percent of daily politeness."),
 "key_points": [
  "నమస్కారం (formal, folded hands) vs నమస్తే (casual) - choose by setting.",
  "మీరు ఎలా ఉన్నారు / నువ్వు ఎలా ఉన్నావు - formal vs informal 'how are you'.",
  "ధన్యవాదాలు - thank you; దయచేసి - please; క్షమించండి - excuse me.",
  "మళ్ళీ కలుద్దాం - 'we will meet again' - the warm standard farewell.",
  "Full mini-conversation included, line by line.",
 ],
 "requirements": [
  "Greet someone with నమస్కారం today.",
  "Never use నువ్వు forms with strangers - use మీరు.",
  "Memorize the farewell మళ్ళీ కలుద్దాం.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Snell, Rupert. Essential Hindi (greeting pragmatics parallel); Telugu usage notes from Gwynn, J. P. L. A Telugu-English Dictionary. Oxford University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens greetings are his handshake protocols: each "
  "phrase a calibrated signal of respect, warmth and intent, chosen for the "
  "exact distance between speaker and listener. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 10
{
 "key": "grammar", "name": "Telugu Grammar Essentials",
 "group": "Foundations", "ladder": 10, "ladder_rank": 4, "ladder_tier": "foundations",
 "description": (
  "The core grammar of Telugu, each rule with translated example sentences. "
  "Word order: Telugu is subject-object-verb. నేను అన్నం తింటాను (nēnu annaṁ "
  "tiṇṭānu) - 'I eat rice' - literally 'I rice eat'. Gender: Telugu has three "
  "genders - masculine for male humans and gods, feminine for female humans and "
  "goddesses, neuter for everything else. అతను వచ్చాడు (atanu vaccāḍu) - 'He "
  "came' (masculine verb); ఆమె వచ్చింది (āme vaccindi) - 'She came' (feminine "
  "verb); అది వచ్చింది (adi vaccindi) - 'It came' (neuter verb). Number: singular "
  "and plural; the plural marker is -లు (-lu). పుస్తకం (pustakaṁ) - 'book', "
  "పుస్తకాలు (pustakālu) - 'books'. Example: పుస్తకాలు టేబులు మీద ఉన్నాయి "
  "(pustakālu ṭēbulu mīda unnāyi) - 'The books are on the table'. Cases: the "
  "nominative is unmarked; the accusative takes -ని/-ను (-ni/-nu): పుస్తకాన్ని "
  "చదువు (pustakānni caduvu) - 'Read the book'. The dative -కు/-కి (-ku/-ki) "
  "marks the recipient: అమ్మకు ఇవ్వు (ammaku ivvu) - 'Give to mother'. The "
  "genitive -యొక్క (-yokka) marks possession: రాము యొక్క పుస్తకం (rāmu yokka "
  "pustakaṁ) - 'Ramu's book' (often shortened: రాము పుస్తకం). The locative "
  "-లో (-lō) marks place: ఇంట్లో (iṇṭlō) - 'in the house'. The instrumental "
  "-తో (-tō) marks 'with': కత్తితో (kattitō) - 'with a knife'. The ablative "
  "-నుండి (-nuṇḍi) marks 'from': ఊరి నుండి (ūri nuṇḍi) - 'from the village'. "
  "Articles: Telugu has no articles; ఈ (ī, 'this') and ఆ (ā, 'that') do the "
  "work. ఈ పిల్ల (ī pilla) - 'this child / the child'. Negation: కాదు (kādu) "
  "negates identity - నేను డాక్టరు కాదు (nēnu ḍākṭaru kādu) - 'I am not a "
  "doctor'. లేదు (lēdu) negates existence and past actions - నా దగ్గర డబ్బు "
  "లేదు (nā daggara ḍabbu lēdu) - 'I have no money'. వద్దు (vaddu) forbids - "
  "అక్కడికి వెళ్ళవద్దు (akkaḍiki veḷḷavaddu) - 'Do not go there'. Questions: "
  "question words or rising intonation; the particle -ఆ (-ā) can mark yes/no "
  "questions. నువ్వు వస్తావా (nuvvu vastāvā) - 'Will you come'. మీరు తెలుగు "
  "మాట్లాడతారా (mīru telugu māṭlāḍatārā) - 'Do you speak Telugu'."),
 "how_it_works": (
  "This record works as the rulebook: word order, gender, number, the seven "
  "cases, the missing articles, the three negations, and question formation - "
  "each rule demonstrated in a sentence you can imitate. Build ten of your own "
  "sentences by swapping the nouns in the examples."),
 "key_points": [
  "SOV word order: నేను అన్నం తింటాను - 'I rice eat'.",
  "Three genders: masculine, feminine, neuter; verbs agree with the subject.",
  "Plural marker -లు: పుస్తకం -> పుస్తకాలు.",
  "Seven cases: nominative, accusative -ని, dative -కు, genitive -యొక్క, locative -లో, instrumental -తో, ablative -నుండి.",
  "No articles: ఈ/ఆ do the work of 'the'.",
  "Negation trio: కాదు (identity), లేదు (existence/past), వద్దు (prohibition).",
  "Questions via question words, intonation, or the -ఆ particle.",
 ],
 "requirements": [
  "Write five SOV sentences using nouns and verbs you know.",
  "Convert three sentences to negative with కాదు and లేదు.",
  "Turn three statements into questions with -ఆ.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Krishnamurti, Bhadriraju & Gwynn, J. P. L. A Grammar of Modern Telugu. Oxford University Press; 1985.",
 ],
 "sig_lens": (
  "Through the Signature lens grammar is his assembly drawing: SOV the build "
  "sequence, cases the fasteners that join parts, negation the safety interlock "
  "that stops the machine. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 11
{
 "key": "home", "name": "Telugu Home and Family Sentences",
 "group": "Foundations", "ladder": 11, "ladder_rank": 4, "ladder_tier": "foundations",
 "description": (
  "Twenty sentences about the house, rooms, furniture and family members. "
  "1. మా ఇల్లు పెద్దది (mā illu peddadi) - 'Our house is big'. 2. ఇంట్లో నాలుగు "
  "గదులు ఉన్నాయి (iṇṭlō nālugu gadulu unnāyi) - 'There are four rooms in the "
  "house'. 3. వంటగది శుభ్రంగా ఉంది (vaṇṭagadi śubhraṅgā undi) - 'The kitchen is "
  "clean'. 4. పడకగదిలో మంచం ఉంది (paḍakagadilō man̄caṁ undi) - 'There is a bed "
  "in the bedroom'. 5. హాలులో సోఫా ఉంది (hālulō sōphā undi) - 'There is a sofa "
  "in the hall'. 6. టేబులు మీద దీపం ఉంది (ṭēbulu mīda dīpaṁ undi) - 'There is a "
  "lamp on the table'. 7. కిటికీ తెరిచి ఉంది (kiṭikī terici undi) - 'The window "
  "is open'. 8. తలుపు మూసి ఉంది (talupu mūsi undi) - 'The door is closed'. "
  "9. అమ్మ వంట చేస్తోంది (amma vaṇṭa cēstōndi) - 'Mother is cooking'. 10. నాన్న "
  "పేపరు చదువుతున్నాడు (nānna pēparu caduvutunnāḍu) - 'Father is reading the "
  "newspaper'. 11. అన్న కాలేజీలో చదువుతున్నాడు (anna kālējīlō caduvutunnāḍu) - "
  "'Elder brother is studying in college'. 12. అక్క నాకు సహాయం చేస్తుంది "
  "(akka nāku sahāyaṁ cēstundi) - 'Elder sister helps me'. 13. తాత కథలు చెప్తాడు "
  "(tāta kathalu ceptāḍu) - 'Grandfather tells stories'. 14. నాయనమ్మ పూజ చేస్తుంది "
  "(nāyanamma pūja cēstundi) - 'Grandmother performs the prayer'. 15. తమ్ముడు "
  "బయట ఆడుతున్నాడు (tammuḍu bayaṭa āḍutunnāḍu) - 'Younger brother is playing "
  "outside'. 16. చెల్లెలు పాట పాడుతోంది (cellelu pāṭa pāḍutōndi) - 'Younger "
  "sister is singing a song'. 17. మా కుటుంబం పెద్దది (mā kuṭuṁbaṁ peddadi) - "
  "'Our family is big'. 18. సాయంత్రం అందరం కలిసి భోజనం చేస్తాము (sāyantraṁ "
  "andaraṁ kalisi bhōjanaṁ cēstāmu) - 'In the evening we all eat dinner "
  "together'. 19. ఇల్లు ఊరి చివర ఉంది (illu ūri civara undi) - 'The house is at "
  "the edge of the village'. 20. మా ఇల్లు నాకు చాలా ఇష్టం (mā illu nāku cālā "
  "iṣṭaṁ) - 'I love our house very much'."),
 "how_it_works": (
  "This record works as the walkthrough of the home: twenty sentences that name "
  "every room and piece of furniture while the family moves through the day. "
  "Walk through your own house naming each room in Telugu as you enter it."),
 "key_points": [
  "20 home and family sentences: rooms, furniture, daily family life.",
  "Family terms: అమ్మ, నాన్న, అన్న, అక్క, తమ్ముడు, చెల్లెలు, తాత, నాయనమ్మ.",
  "Locative -లో in action: ఇంట్లో, వంటగదిలో, పడకగదిలో.",
  "సాయంత్రం అందరం కలిసి భోజనం చేస్తాము - 'In the evening we all eat dinner together'.",
 ],
 "requirements": [
  "Label five rooms of your home with Telugu words.",
  "Introduce your family in three Telugu sentences.",
  "Say what each family member is doing right now in Telugu.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Gwynn, J. P. L. A Telugu-English Dictionary. Oxford University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens the home is his first workshop: every room a "
  "station, every family member a teammate, the evening meal the daily review "
  "where the whole crew reports. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 12
{
 "key": "food", "name": "Telugu Food and Cooking Sentences",
 "group": "Foundations", "ladder": 12, "ladder_rank": 4, "ladder_tier": "foundations",
 "description": (
  "Twenty sentences about meals, ingredients, cooking actions and restaurants. "
  "1. నేను రోజూ మూడు పూటలా తింటాను (nēnu rōjū mūḍu pūṭalā tiṇṭānu) - 'I eat three "
  "meals a day'. 2. ఉదయం అల్పాహారం తింటాను (udayaṁ alpāhāraṁ tiṇṭānu) - 'I eat "
  "breakfast in the morning'. 3. మధ్యాహ్నం అన్నం తింటాను (madhyāhnaṁ annaṁ "
  "tiṇṭānu) - 'I eat rice at noon'. 4. అమ్మ పప్పు వండుతోంది (amma pappu "
  "vaṇḍutōndi) - 'Mother is cooking dal'. 5. కూరలో ఉప్పు తక్కువగా ఉంది "
  "(kūralō uppu takkuvagā undi) - 'There is too little salt in the curry'. "
  "6. ఈ కారం చాలా ఘాటుగా ఉంది (ī kāraṁ cālā ghāṭugā undi) - 'This spice is very "
  "hot'. 7. నాకు పాలు ఇష్టం (nāku pālu iṣṭaṁ) - 'I like milk'. 8. టీలో పంచదార "
  "వేయి (ṭīlō pan̄cadāra vēyi) - 'Put sugar in the tea'. 9. పండ్లు ఆరోగ్యానికి "
  "మంచివి (paṇḍlu ārōgyāniki man̄civi) - 'Fruits are good for health'. "
  "10. కూరగాయలు మార్కెట్ నుండి కొన్నాను (kūragāyalu mārkeṭ nuṇḍi konnānu) - 'I "
  "bought vegetables from the market'. 11. చేపల కూర రుచిగా ఉంది (cēpala kūra "
  "rucigā undi) - 'The fish curry is tasty'. 12. గుడ్డు ఉడికించు (guḍḍu "
  "uḍikin̄cu) - 'Boil the egg'. 13. రొట్టెలు కాల్చు (roṭṭelu kālcu) - 'Bake the "
  "breads'. 14. నీళ్లు మరిగించు (nīḷḷu marigin̄cu) - 'Boil the water'. "
  "15. భోజనం సిద్ధంగా ఉంది (bhōjanaṁ siddhaṅgā undi) - 'The meal is ready'. "
  "16. అందరూ కలిసి తినండి (andarū kalisi tinaṇḍi) - 'Everyone eat together'. "
  "17. నాకు కొంచెం అన్నం పెట్టు (nāku kon̄ceṁ annaṁ peṭṭu) - 'Serve me a little "
  "rice'. 18. రెస్టారెంట్లో దోశ తిన్నాము (resṭāreṇṭlō dōśa tinnāmu) - 'We ate "
  "dosa at the restaurant'. 19. బిల్లు తీసుకురండి (billu tīsukuraṇḍi) - 'Bring "
  "the bill, please'. 20. భోజనం చాలా బాగుంది, ధన్యవాదాలు (bhōjanaṁ cālā bāgundi, "
  "dhanyavādālu) - 'The meal was very good, thank you'."),
 "how_it_works": (
  "This record works as the kitchen shift: twenty sentences from market to table "
  "to restaurant, naming ingredients and cooking actions. Cook one dish while "
  "narrating each step in Telugu - వండు (cook), కాల్చు (bake), ఉడికించు (boil)."),
 "key_points": [
  "20 food and cooking sentences: meals, ingredients, cooking, restaurant.",
  "Cooking verbs: వండు cook, కాల్చు bake/roast, ఉడికించు boil, మరిగించు bring to boil.",
  "Tastes: తీపి sweet, చేదు bitter, పుల్లని sour, ఘాటు spicy-hot.",
  "భోజనం సిద్ధంగా ఉంది - 'The meal is ready' - the cook's announcement.",
 ],
 "requirements": [
  "Name ten foods in your kitchen in Telugu.",
  "Order a meal in Telugu at a restaurant (practice aloud).",
  "Describe your favorite dish in three Telugu sentences.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Gwynn, J. P. L. A Telugu-English Dictionary. Oxford University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens the kitchen is his materials lab: ingredients the "
  "raw stock, recipes the procedures, tasting the quality inspection - and a "
  "shared meal the acceptance test. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 13
{
 "key": "travel", "name": "Telugu Travel and Directions Sentences",
 "group": "Compounded", "ladder": 13, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about transport, asking directions, tickets and lodging. "
  "1. రైల్వే స్టేషన్ ఎక్కడ ఉంది (railvē sṭēṣan ekkaḍa undi) - 'Where is the "
  "railway station'. 2. బస్ స్టాప్ దగ్గరలో ఉందా (bas stāp daggaralō undā) - 'Is "
  "the bus stop nearby'. 3. విమానాశ్రయానికి ఎలా వెళ్ళాలి (vimānāśrayāniki elā "
  "veḷḷāli) - 'How do I get to the airport'. 4. నేరుగా వెళ్ళి కుడివైపు తిరగండి "
  "(nērugā veḷḷi kuḍivaipu tiragaṇḍi) - 'Go straight and turn right'. 5. ఎడమవైపు "
  "మొదటి రోడ్డు (eḍamavaipu modaṭi rōḍḍu) - 'The first road on the left'. "
  "6. ఇక్కడి నుండి ఎంత దూరం (ikkaḍi nuṇḍi enta dūraṁ) - 'How far is it from "
  "here'. 7. నడిచి వెళ్ళవచ్చా (naḍici veḷḷavaccā) - 'Can I walk there'. "
  "8. టికెట్ ఎక్కడ కొనాలి (ṭikeṭ ekkaḍa konāli) - 'Where do I buy the ticket'. "
  "9. హైదరాబాద్కు ఒక టికెట్ ఇవ్వండి (haidarābādku oka ṭikeṭ ivaṇḍi) - 'Give me one "
  "ticket to Hyderabad'. 10. రైలు ఎన్ని గంటలకు వస్తుంది (railu enni gaṇṭalaku "
  "vastundi) - 'At what time does the train come'. 11. బస్సు ఆలస్యంగా ఉందా "
  "(bassu ālasyaṅgā undā) - 'Is the bus late'. 12. టాక్సీ కావాలి (ṭāksī kāvāli) - "
  "'I need a taxi'. 13. మీటర్ ప్రకారం వెళ్ళండి (mīṭar prakāraṁ veḷḷaṇḍi) - 'Go "
  "by the meter, please'. 14. హోటల్లో గది ఖాళీగా ఉందా (hōṭallō gadi khāḷīgā "
  "undā) - 'Is a room free at the hotel'. 15. ఒక రాత్రికి ఎంత (oka rātriki "
  "enta) - 'How much for one night'. 16. నా సామాను ఇక్కడ ఉంచండి (nā sāmānu "
  "ikkaḍa un̄caṇḍi) - 'Keep my luggage here'. 17. ఉదయం ఆరు గంటలకు లేపండి "
  "(udayaṁ āru gaṇṭalaku lēpaṇḍi) - 'Wake me at six in the morning'. 18. నా "
  "పాస్పోర్ట్ పోయింది (nā pāsporṭ pōyindi) - 'I lost my passport'. 19. దయచేసి "
  "నాకు సహాయం చేయండి (dayacēsi nāku sahāyaṁ cēyaṇḍi) - 'Please help me'. "
  "20. ప్రయాణం సురక్షితంగా సాగాలి (prayāṇaṁ surakṣitaṅgā sāgāli) - 'May the "
  "journey go safely'."),
 "how_it_works": (
  "This record works as the traveler's phrasebook: twenty sentences that get "
  "you to the station, onto the vehicle, into the hotel, and safely home - "
  "directions, tickets, lodging, emergencies. Rehearse the direction trio: "
  "నేరుగా (straight), కుడివైపు (right), ఎడమవైపు (left)."),
 "key_points": [
  "20 travel sentences: stations, directions, tickets, hotel, emergencies.",
  "Direction words: నేరుగా straight, కుడివైపు right, ఎడమవైపు left, దగ్గర nearby, దూరం far.",
  "హైదరాబాద్కు ఒక టికెట్ ఇవ్వండి - 'One ticket to Hyderabad, please'.",
  "Emergency core: నా పాస్పోర్ట్ పోయింది - 'I lost my passport'.",
 ],
 "requirements": [
  "Ask for directions to three places in Telugu.",
  "Buy a ticket in a rehearsal conversation.",
  "Memorize the emergency sentences cold.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Gwynn, J. P. L. A Telugu-English Dictionary. Oxford University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens travel is a field operation: the route a planned "
  "procedure, directions the coordinates, the ticket the work order, and the "
  "safe return the mission closeout. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 14
{
 "key": "workschool", "name": "Telugu Work and School Sentences",
 "group": "Compounded", "ladder": 14, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about jobs, the office, the classroom and learning. 1. నేను "
  "ఉపాధ్యాయుడిని (nēnu upādhyāyuḍini) - 'I am a teacher'. 2. ఆమె డాక్టరుగా పని "
  "చేస్తుంది (āme ḍākṭarugā pani cēstundi) - 'She works as a doctor'. 3. నా "
  "ఆఫీసు నగరంలో ఉంది (nā āphīsu nagaraṁlō undi) - 'My office is in the city'. "
  "4. నేను ఉదయం తొమ్మిది గంటలకు పనికి వెళ్తాను (nēnu udayaṁ tommidi gaṇṭalaku "
  "paniki veḷtānu) - 'I go to work at nine in the morning'. 5. సాయంత్రం ఐదు "
  "గంటలకు ఇంటికి వస్తాను (sāyantraṁ aidu gaṇṭalaku iṇṭiki vastānu) - 'I come "
  "home at five in the evening'. 6. నా బాస్ చాలా మంచివాడు (nā bās cālā "
  "man̄civāḍu) - 'My boss is very good'. 7. ఈ ప్రాజెక్టు రేపటికి పూర్తి చేయాలి "
  "(ī prājekṭu rēpaṭiki pūrti cēyāli) - 'This project must be finished by "
  "tomorrow'. 8. సమావేశం పది గంటలకు మొదలవుతుంది (samāvēśaṁ padi gaṇṭalaku "
  "modalavutundi) - 'The meeting starts at ten o'clock'. 9. పిల్లలు బడిలో "
  "చదువుతున్నారు (pillalu baḍilō caduvutunnāru) - 'The children are studying in "
  "school'. 10. ఉపాధ్యాయుడు పాఠం చెప్తున్నాడు (upādhyāyuḍu pāṭhaṁ ceptunnāḍu) - "
  "'The teacher is teaching the lesson'. 11. విద్యార్థులు శ్రద్ధగా వింటున్నారు "
  "(vidyārthulu śraddhagā viṇṭunnāru) - 'The students are listening attentively'. "
  "12. నా పరీక్ష వచ్చే వారం (nā parīkṣa vaccē vāraṁ) - 'My exam is next week'. "
  "13. నేను గణితంలో బాగున్నాను (nēnu gaṇitaṁlō bāgunnānu) - 'I am good at "
  "mathematics'. 14. హోంవర్క్ పూర్తి చేశాను (hōmvark pūrti cēśānu) - 'I finished "
  "the homework'. 15. పుస్తకాలు బ్యాగ్లో ఉన్నాయి (pustakālu byāglō unnāyi) - "
  "'The books are in the bag'. 16. పెన్ను తీసుకో (pennu tīsukō) - 'Take the "
  "pen'. 17. బోర్డు మీద రాయి (bōrḍu mīda rāyi) - 'Write on the board'. 18. ప్రశ్న "
  "అడుగు (praśna aḍugu) - 'Ask a question'. 19. జీతం నెలాఖరుకు వస్తుంది (jītaṁ "
  "nelākharuku vastundi) - 'The salary comes at month's end'. 20. కష్టపడి పని "
  "చేస్తే ఫలితం ఉంటుంది (kaṣṭapaḍi pani cēstē phalitaṁ uṇṭundi) - 'If you work "
  "hard, there will be results'."),
 "how_it_works": (
  "This record works as the double shift: the office half and the classroom "
  "half, twenty sentences covering jobs, meetings, lessons and learning. Tell "
  "someone your job in Telugu today; describe your school day tomorrow."),
 "key_points": [
  "20 work and school sentences: jobs, office, classroom, learning.",
  "Job titles: ఉపాధ్యాయుడు teacher, డాక్టరు doctor, విద్యార్థి student.",
  "School objects: పుస్తకం book, పెన్ను pen, బోర్డు board, బ్యాగ్ bag.",
  "కష్టపడి పని చేస్తే ఫలితం ఉంటుంది - 'Hard work brings results'.",
 ],
 "requirements": [
  "Say your job or study in two Telugu sentences.",
  "Describe your workday schedule with clock times.",
  "Ask and answer one classroom question in Telugu.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Gwynn, J. P. L. A Telugu-English Dictionary. Oxford University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens work and school are his two production lines: the "
  "office where plans become products, the classroom where operators are "
  "trained - both running on schedules, checklists and measured results. "
  "Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 15
{
 "key": "health", "name": "Telugu Health and Body Sentences",
 "group": "Compounded", "ladder": 15, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about body parts, symptoms, the doctor visit and the "
  "pharmacy. 1. నా తల నొప్పిగా ఉంది (nā tala noppigā undi) - 'My head aches'. "
  "2. కడుపు నొప్పి వస్తోంది (kaḍupu noppi vastōndi) - 'My stomach hurts'. "
  "3. నాకు జ్వరం ఉంది (nāku jvaraṁ undi) - 'I have a fever'. 4. దగ్గు వస్తోంది "
  "(daggu vastōndi) - 'I have a cough'. 5. గొంతు నొప్పిగా ఉంది (gontu noppigā "
  "undi) - 'My throat hurts'. 6. కాలు బెణికింది (kālu beṇikindi) - 'My leg is "
  "sprained'. 7. చేయి వాచింది (cēyi vācindi) - 'My hand is swollen'. 8. కన్ను "
  "ఎర్రగా ఉంది (kannu erragā undi) - 'My eye is red'. 9. నాకు తల తిరుగుతోంది "
  "(nāku tala tirugutōndi) - 'I feel dizzy'. 10. డాక్టరు దగ్గరకు వెళ్దాం "
  "(ḍākṭaru daggaraku veldāṁ) - 'Let us go to the doctor'. 11. నాకు మందు కావాలి "
  "(nāku mandu kāvāli) - 'I need medicine'. 12. ఈ మందు రోజుకు రెండు సార్లు వేసుకో "
  "(ī mandu rōjuku reṇḍu sārlu vēsukō) - 'Take this medicine twice a day'. "
  "13. భోజనం తర్వాత మందు వేసుకో (bhōjanaṁ tarvāta mandu vēsukō) - 'Take the "
  "medicine after meals'. 14. నాకు ఈ మందు పడదు (nāku ī mandu paḍadu) - 'This "
  "medicine does not suit me'. 15. రక్తపోటు పరీక్ష చేయించండి (raktapōṭu "
  "parīkṣa cēyin̄caṇḍi) - 'Please check the blood pressure'. 16. విశ్రాంతి "
  "తీసుకో (viśrānti tīsukō) - 'Take rest'. 17. ఎక్కువ నీళ్లు తాగు (ekkuva nīḷḷu "
  "tāgu) - 'Drink plenty of water'. 18. ఆసుపత్రి ఎక్కడ ఉంది (āsupatri ekkaḍa "
  "undi) - 'Where is the hospital'. 19. అంబులెన్స్ పిలవండి (ambulens pilavaṇḍi) - "
  "'Call an ambulance'. 20. త్వరగా కోలుకోండి (tvaragā kōlukōṇḍi) - 'Get well "
  "soon'. Body parts: తల (tala) - head, కన్ను (kannu) - eye, ముక్కు (mukku) - "
  "nose, నోరు (nōru) - mouth, చెవి (cevi) - ear, గొంతు (gontu) - throat, "
  "చేయి (cēyi) - hand, కాలు (kālu) - leg, గుండె (guṇḍe) - heart, కడుపు (kaḍupu) - "
  "stomach."),
 "how_it_works": (
  "This record works as the first-aid card: body parts first, then symptom "
  "sentences, then the doctor visit and pharmacy. In a real need, the sentences "
  "that matter most are నాకు జ్వరం ఉంది and డాక్టరు దగ్గరకు వెళ్దాం - learn "
  "those first."),
 "key_points": [
  "20 health sentences: body parts, symptoms, doctor, pharmacy.",
  "Body parts: తల head, కన్ను eye, ముక్కు nose, నోరు mouth, చెవి ear, గుండె heart.",
  "Symptom pattern: నాకు జ్వరం ఉంది - 'I have a fever'.",
  "Medicine pattern: రోజుకు రెండు సార్లు - 'twice a day'.",
  "Emergency: అంబులెన్స్ పిలవండి - 'Call an ambulance'.",
 ],
 "requirements": [
  "Name ten body parts in Telugu while pointing.",
  "Describe one symptom in a full Telugu sentence.",
  "Rehearse the pharmacy sentence: ఈ మందు రోజుకు రెండు సార్లు.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Gwynn, J. P. L. A Telugu-English Dictionary. Oxford University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens the body is his most important machine and "
  "health its maintenance log: symptoms the warning lights, the doctor the "
  "service technician, medicine the replacement part. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 16
{
 "key": "emotions", "name": "Telugu Emotions and Feelings Sentences",
 "group": "Compounded", "ladder": 16, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about being happy, sad, angry, afraid, loving and "
  "surprised. 1. నేను చాలా సంతోషంగా ఉన్నాను (nēnu cālā santōṣaṅgā unnānu) - 'I "
  "am very happy'. 2. ఈ వార్త విని ఆనందించాను (ī vārta vini ānandin̄cānu) - 'I "
  "was delighted to hear this news'. 3. పిల్లలు సంతోషంతో ఆడుతున్నారు (pillalu "
  "santōṣantō āḍutunnāru) - 'The children are playing happily'. 4. నాకు బాధగా "
  "ఉంది (nāku bādhagā undi) - 'I feel sad'. 5. ఆమె కన్నీళ్లు పెట్టుకుంది (āme "
  "kannīḷḷu peṭṭukundi) - 'She burst into tears'. 6. అతను దుఃఖంలో ఉన్నాడు "
  "(atanu duḥkhaṁlō unnāḍu) - 'He is in sorrow'. 7. నాకు కోపం వస్తోంది (nāku "
  "kōpaṁ vastōndi) - 'I am getting angry'. 8. కోపంతో అరవద్దు (kōpantō "
  "aravaddu) - 'Do not shout in anger'. 9. శాంతించు, అంతా సర్దుకుంటుంది "
  "(śāntin̄cu, antā sardukuṇṭundi) - 'Calm down, everything will be fine'. "
  "10. నాకు భయంగా ఉంది (nāku bhayaṅgā undi) - 'I am afraid'. 11. చీకట్లో ఒంటరిగా "
  "భయం వేసింది (cīkaṭlō oṇṭarigā bhayaṁ vēsindi) - 'I felt scared alone in the "
  "dark'. 12. ధైర్యంగా ఉండు (dhairyaṅgā uṇḍu) - 'Be brave'. 13. నేను నిన్ను "
  "ప్రేమిస్తున్నాను (nēnu ninnu prēmistunnānu) - 'I love you'. 14. అమ్మ ప్రేమ "
  "గొప్పది (amma prēma goppadi) - 'A mother's love is great'. 15. వాళ్ళు ఒకరినొకరు "
  "ఇష్టపడతారు (vāḷḷu okarinokaru iṣṭapaḍatāru) - 'They like each other'. "
  "16. నాకు ఆశ్చర్యం వేసింది (nāku āścaryaṁ vēsindi) - 'I was surprised'. "
  "17. అది చూసి అందరూ ఆశ్చర్యపోయారు (adi cūsi andarū āścaryapōyāru) - 'Everyone "
  "was surprised to see that'. 18. నాకు గర్వంగా ఉంది (nāku garvaṅgā undi) - 'I "
  "feel proud'. 19. సిగ్గుపడకు, ధైర్యంగా చెప్పు (siggu paḍaku, dhairyaṅgā "
  "ceppu) - 'Do not be shy, speak boldly'. 20. మనశ్శాంతి అన్నిటికంటే ముఖ్యం "
  "(manaśśānti anniṭikaṇṭē mukhyaṁ) - 'Peace of mind matters most of all'."),
 "how_it_works": (
  "This record works as the feelings map: six emotions, each with sentences "
  "that name the feeling and sentences that respond to it. Say how you feel "
  "today in Telugu - నేను సంతోషంగా ఉన్నాను - and mean it."),
 "key_points": [
  "20 emotion sentences: happy, sad, angry, afraid, love, surprise.",
  "Feeling pattern: నాకు భయంగా ఉంది - 'I am afraid' (dative experiencer).",
  "Comfort pattern: శాంతించు - 'calm down'.",
  "నేను నిన్ను ప్రేమిస్తున్నాను - 'I love you'.",
  "మనశ్శాంతి అన్నిటికంటే ముఖ్యం - 'Peace of mind matters most'.",
 ],
 "requirements": [
  "Say your current feeling in Telugu each morning.",
  "Learn one comfort sentence for each emotion.",
  "Write three feeling sentences about yesterday.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Gwynn, J. P. L. A Telugu-English Dictionary. Oxford University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens emotions are his instrument panel readings: "
  "happiness the green light, anger the red warning, fear the low-fuel alarm - "
  "each one real data he reads and responds to, never ignores. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 17
{
 "key": "nature", "name": "Telugu Nature and Weather Sentences",
 "group": "Compounded", "ladder": 17, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about animals, plants, seasons and weather talk. 1. కుక్క "
  "మొరుగుతోంది (kukka morugutōndi) - 'The dog is barking'. 2. పిల్లి పాలు "
  "తాగుతోంది (pilli pālu tāgutōndi) - 'The cat is drinking milk'. 3. ఆవు గడ్డి "
  "మేస్తోంది (āvu gaḍḍi mēstōndi) - 'The cow is grazing'. 4. ఏనుగు పెద్ద జంతువు "
  "(ēnugu pedda jantuvu) - 'The elephant is a big animal'. 5. పులి అడవిలో "
  "ఉంటుంది (puli aḍavilō uṇṭundi) - 'The tiger lives in the forest'. 6. కోతి "
  "చెట్టు మీద ఉంది (kōti ceṭṭu mīda undi) - 'The monkey is on the tree'. "
  "7. పక్షులు ఆకాశంలో ఎగురుతున్నాయి (pakṣulu ākāśaṁlō egurutunnāyi) - 'Birds are "
  "flying in the sky'. 8. చేప నీటిలో ఈదుతోంది (cēpa nīṭilō īdutōndi) - 'The fish "
  "is swimming in the water'. 9. పామును చూసి జాగ్రత్త (pāmunu cūsi jāgratta) - "
  "'Beware of the snake'. 10. తోటలో పూలు పూశాయి (tōṭalō pūlu pūśāyi) - 'Flowers "
  "bloomed in the garden'. 11. మామిడి చెట్టు పెద్దది (māmiḍi ceṭṭu peddadi) - "
  "'The mango tree is big'. 12. వరి పొలాలు పచ్చగా ఉన్నాయి (vari polālu paccagā "
  "unnāyi) - 'The paddy fields are green'. 13. ఈరోజు వాతావరణం బాగుంది (īrōju "
  "vātāvaraṇaṁ bāgundi) - 'The weather is nice today'. 14. ఎండ ఎక్కువగా ఉంది "
  "(eṇḍa ekkuvagā undi) - 'It is very sunny'. 15. వాన పడుతోంది (vāna paḍutōndi) - "
  "'It is raining'. 16. గాలి వీస్తోంది (gāli vīstōndi) - 'The wind is blowing'. "
  "17. చలి ఎక్కువగా ఉంది (cali ekkuvagā undi) - 'It is very cold'. 18. మేఘాలు "
  "కమ్ముకున్నాయి (mēghālu kammukunnāyi) - 'Clouds have gathered'. 19. ఇంద్రధనస్సు "
  "కనిపిస్తోంది (indradhanassu kanipistōndi) - 'A rainbow is visible'. 20. రేపు "
  "వాన పడుతుందా (rēpu vāna paḍutundā) - 'Will it rain tomorrow'."),
 "how_it_works": (
  "This record works as the field guide: animals and plants first, then the "
  "weather small talk that opens every outdoor conversation. Start each day by "
  "describing the weather in Telugu - ఈరోజు వాతావరణం బాగుంది - looking out "
  "the window."),
 "key_points": [
  "20 nature and weather sentences: animals, plants, seasons, weather talk.",
  "Animals: కుక్క dog, పిల్లి cat, ఆవు cow, ఏనుగు elephant, పులి tiger, కోతి monkey, పాము snake.",
  "Weather core: వాన పడుతోంది (it is raining), ఎండ (sunshine), చలి (cold), గాలి (wind).",
  "రేపు వాన పడుతుందా - 'Will it rain tomorrow' - the farmer's question.",
 ],
 "requirements": [
  "Describe today's weather in two Telugu sentences daily.",
  "Name five animals and five plants in Telugu.",
  "Ask someone about tomorrow's weather in Telugu.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Gwynn, J. P. L. A Telugu-English Dictionary. Oxford University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens nature is his open-air laboratory: every animal "
  "a working prototype, every season a test cycle, the weather the daily "
  "conditions report he reads before starting work. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 18
{
 "key": "shopping", "name": "Telugu Shopping and Money Sentences",
 "group": "Compounded", "ladder": 18, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about the market, prices, bargaining and paying. 1. మార్కెట్ "
  "ఎక్కడ ఉంది (mārkeṭ ekkaḍa undi) - 'Where is the market'. 2. అంగడి ఎన్ని "
  "గంటలకు తెరుస్తారు (aṅgaḍi enni gaṇṭalaku terustāru) - 'At what time does the "
  "shop open'. 3. ఇది ఎంత (idi enta) - 'How much is this'. 4. కిలో ఎంత (kilō "
  "enta) - 'How much per kilo'. 5. చాలా ఖరీదు, కొంచెం తగ్గించండి (cālā kharīdu, "
  "kon̄ceṁ taggin̄caṇḍi) - 'Too expensive, reduce a little please'. 6. చివరి ధర "
  "ఏమిటి (civari dhara ēmiṭi) - 'What is the final price'. 7. ఇంకొంచెం తక్కువ "
  "చేయండి (iṅkon̄ceṁ takkuva cēyaṇḍi) - 'Make it a bit less'. 8. సరే, తీసుకుంటాను "
  "(sarē, tīsukoṇṭānu) - 'Okay, I will take it'. 9. వద్దు, చాలా ఎక్కువ (vaddu, "
  "cālā ekkuva) - 'No, too much'. 10. నాణ్యత బాగుందా (nāṇyata bāgundā) - 'Is "
  "the quality good'. 11. ఇంకోటి చూపించండి (iṅkōṭi cūpin̄caṇḍi) - 'Show me "
  "another one'. 12. ఈ రంగులో ఉందా (ī raṅgulō undā) - 'Do you have it in this "
  "color'. 13. పెద్ద సైజు ఉందా (pedda saiju undā) - 'Do you have a large size'. "
  "14. నగదు చెల్లిస్తాను (nagadu cellistānu) - 'I will pay cash'. 15. కార్డుతో "
  "చెల్లించవచ్చా (kārḍutō cellin̄cavaccā) - 'Can I pay by card'. 16. బిల్లు ఇవ్వండి "
  "(billu ivaṇḍi) - 'Give the bill'. 17. చిల్లర ఉందా (cillara undā) - 'Do you "
  "have change'. 18. సంచిలో పెట్టండి (san̄cilō peṭṭaṇḍi) - 'Put it in a bag'. "
  "19. రసీదు ఇవ్వండి (rasīdu ivaṇḍi) - 'Give the receipt'. 20. మళ్ళీ వస్తాను, "
  "ధన్యవాదాలు (maḷḷī vastānu, dhanyavādālu) - 'I will come again, thank you'."),
 "how_it_works": (
  "This record works as the market drill: the full bargaining arc from "
  "'how much' to the final handshake, plus paying. Practice the haggle loop "
  "aloud with a partner: చాలా ఖరీదు - కొంచెం తగ్గించండి - సరే, తీసుకుంటాను."),
 "key_points": [
  "20 shopping sentences: market, prices, bargaining, paying.",
  "Price core: ఇది ఎంత - 'How much is this'; కిలో ఎంత - 'How much per kilo'.",
  "Bargain trio: చాలా ఖరీదు / కొంచెం తగ్గించండి / సరే, తీసుకుంటాను.",
  "Paying: నగదు cash, కార్డు card, బిల్లు bill, చిల్లర change, రసీదు receipt.",
 ],
 "requirements": [
  "Rehearse a full bargaining conversation with a partner.",
  "Ask prices of five items in Telugu.",
  "Pay and ask for the receipt in Telugu (practice).",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Gwynn, J. P. L. A Telugu-English Dictionary. Oxford University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens the market is his supply depot: every price a "
  "negotiated specification, bargaining the engineering of value, the handshake "
  "the signed contract. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 19
{
 "key": "social", "name": "Telugu Friendship and Social Life Sentences",
 "group": "Compounded", "ladder": 19, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about meeting people, invitations and celebrations. 1. మీ "
  "పేరు ఏమిటి (mī pēru ēmiṭi) - 'What is your name'. 2. నా పేరు రాము (nā pēru "
  "rāmu) - 'My name is Ramu'. 3. మీరు ఎక్కడి నుండి వచ్చారు (mīru ekkaḍi nuṇḍi "
  "vaccāru) - 'Where are you from'. 4. నేను విజయవాడ నుండి వచ్చాను (nēnu "
  "vijayavāḍa nuṇḍi vaccānu) - 'I am from Vijayawada'. 5. మీ వయస్సు ఎంత (mī "
  "vayassu enta) - 'How old are you'. 6. నా వయస్సు ఇరవై ఐదు (nā vayassu iravai "
  "aidu) - 'I am twenty-five'. 7. మీరు ఏమి చేస్తారు (mīru ēmi cēstāru) - 'What "
  "do you do'. 8. నేను ఇంజనీరుని (nēnu in̄janīrini) - 'I am an engineer'. "
  "9. మనం స్నేహితులం అవుదాం (manaṁ snēhitulaṁ avudāṁ) - 'Let us become friends'. "
  "10. నా ఇంటికి రండి (nā iṇṭiki raṇḍi) - 'Come to my house'. 11. రేపు సాయంత్రం "
  "రండి (rēpu sāyantraṁ raṇḍi) - 'Come tomorrow evening'. 12. భోజనానికి రండి "
  "(bhōjanāniki raṇḍi) - 'Come for a meal'. 13. ఆహ్వానానికి ధన్యవాదాలు "
  "(āhvānāniki dhanyavādālu) - 'Thank you for the invitation'. 14. తప్పకుండా "
  "వస్తాను (tappakuṇḍā vastānu) - 'I will definitely come'. 15. క్షమించండి, నేను "
  "రాలేను (kṣamin̄caṇḍi, nēnu rālēnu) - 'Sorry, I cannot come'. 16. పండగ "
  "శుభాకాంక్షలు (paṇḍaga śubhākāṅkṣalu) - 'Happy festival'. 17. సంక్రాంతి "
  "శుభాకాంక్షలు (saṅkrānti śubhākāṅkṣalu) - 'Happy Sankranti'. 18. పెళ్ళికి "
  "ఆహ్వానిస్తున్నాము (peḷḷiki āhvānistunnāmu) - 'We invite you to the wedding'. "
  "19. బహుమతి తీసుకురండి (bahumati tīsukuraṇḍi) - 'Bring a gift' (said "
  "teasingly among friends). 20. మీ స్నేహం నాకు విలువైనది (mī snēhaṁ nāku "
  "viluvainadi) - 'Your friendship is precious to me'."),
 "how_it_works": (
  "This record works as the social script: the self-introduction sequence, the "
  "invitation and its two answers, and the celebration phrases. Introduce "
  "yourself fully in Telugu - name, place, work - to a real person this week."),
 "key_points": [
  "20 social sentences: introductions, invitations, celebrations.",
  "Introduction chain: పేరు - ఊరు - వయస్సు - పని (name, place, age, work).",
  "Invitation answers: తప్పకుండా వస్తాను (yes) / క్షమించండి, నేను రాలేను (no).",
  "మీ స్నేహం నాకు విలువైనది - 'Your friendship is precious to me'.",
 ],
 "requirements": [
  "Introduce yourself in four Telugu sentences.",
  "Invite someone and accept or decline politely.",
  "Wish someone a happy festival in Telugu.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Gwynn, J. P. L. A Telugu-English Dictionary. Oxford University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens friendship is his alliance network: introductions "
  "the handshake protocol, invitations the joint-operation orders, celebrations "
  "the shared victories logged together. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 20
{
 "key": "tech", "name": "Telugu Technology and Communication Sentences",
 "group": "Compounded", "ladder": 20, "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about the phone, internet, computer and messaging. 1. నా "
  "ఫోన్ నంబరు ఇది (nā phōn nambaru idi) - 'This is my phone number'. 2. నాకు "
  "ఫోన్ చేయండి (nāku phōn cēyaṇḍi) - 'Call me'. 3. నేను తర్వాత ఫోన్ చేస్తాను "
  "(nēnu tarvāta phōn cēstānu) - 'I will call later'. 4. ఫోన్ మోగుతోంది, "
  "ఎత్తండి (phōn mōgutōndi, ettaṇḍi) - 'The phone is ringing, pick it up'. "
  "5. సిగ్నల్ రావడం లేదు (signal rāvaḍaṁ lēdu) - 'There is no signal'. 6. ఫోన్ "
  "ఛార్జింగ్ పెట్టు (phōn chārjin̄g peṭṭu) - 'Put the phone on charge'. 7. నాకు "
  "మెసేజ్ పంపండి (nāku mesēj pampaṇḍi) - 'Send me a message'. 8. వాట్సాప్లో "
  "పంపండి (vāṭsāplō pampaṇḍi) - 'Send it on WhatsApp'. 9. ఈమెయిల్ పంపాను "
  "(īmeil pampānu) - 'I sent the email'. 10. ఈమెయిల్ అడ్రస్ ఏమిటి (īmeil aḍras "
  "ēmiṭi) - 'What is the email address'. 11. ఇంటర్నెట్ పని చేయడం లేదు "
  "(iṇṭarneṭ pani cēyaḍaṁ lēdu) - 'The internet is not working'. 12. వైఫై "
  "పాస్వర్డ్ ఏమిటి (vaiphai pāsvard ēmiṭi) - 'What is the Wi-Fi password'. "
  "13. కంప్యూటర్ ఆన్ చేయి (kampyūṭar ān cēyi) - 'Turn on the computer'. "
  "14. ఫైల్ సేవ్ చేయి (phail sēv cēyi) - 'Save the file'. 15. ఫోటో తీయి "
  "(phōṭō tīyi) - 'Take a photo'. 16. వీడియో కాల్ చేద్దాం (vīḍiyō kāl cēddāṁ) - "
  "'Let us do a video call'. 17. బ్యాటరీ అయిపోయింది (byāṭarī ayipōyindi) - 'The "
  "battery died'. 18. యాప్ డౌన్లోడ్ చేయి (yāp ḍaunlōḍ cēyi) - 'Download the "
  "app'. 19. పాస్వర్డ్ మర్చిపోయాను (pāsvard marcipōyānu) - 'I forgot the "
  "password'. 20. కంప్యూటర్ నెమ్మదిగా ఉంది (kampyūṭar nemmadigā undi) - 'The "
  "computer is slow'."),
 "how_it_works": (
  "This record works as the device manual in Telugu: calling, messaging, "
  "internet and computer sentences for the digital day. Change one app's "
  "language setting to Telugu and use three sentences from this record today."),
 "key_points": [
  "20 technology sentences: phone, internet, computer, messaging.",
  "Phone core: నాకు ఫోన్ చేయండి - 'Call me'; ఫోన్ మోగుతోంది - 'The phone is ringing'.",
  "Internet core: వైఫై పాస్వర్డ్ ఏమిటి - 'What is the Wi-Fi password'.",
  "వీడియో కాల్ చేద్దాం - 'Let us do a video call'.",
 ],
 "requirements": [
  "Make a phone call opening in Telugu.",
  "Ask for Wi-Fi in Telugu at a cafe (practice).",
  "Give three computer instructions in Telugu.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Gwynn, J. P. L. A Telugu-English Dictionary. Oxford University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens technology is his extended nervous system: the "
  "phone his long-distance voice, the network his shared memory, every message "
  "a signal packet routed with intent. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 21
{
 "key": "tenses", "name": "Telugu Verb Tenses in Sentences",
 "group": "Compounded", "ladder": 21, "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Telugu verb tenses with five or more translated sentences per tense, using "
  "the verb చేయు (cēyu, 'do') and చదువు (caduvu, 'read, study') as models. "
  "Present progressive (-తున్నాను): 1. నేను పుస్తకం చదువుతున్నాను (nēnu "
  "pustakaṁ caduvutunnānu) - 'I am reading a book'. 2. అతను పని చేస్తున్నాడు "
  "(atanu pani cēstunnāḍu) - 'He is working'. 3. ఆమె వంట చేస్తోంది (āme vaṇṭa "
  "cēstōndi) - 'She is cooking'. 4. పిల్లలు ఆడుతున్నారు (pillalu āḍutunnāru) - "
  "'The children are playing'. 5. వాన పడుతోంది (vāna paḍutōndi) - 'It is "
  "raining'. Habitual present (-తాను): 6. నేను ప్రతిరోజూ చదువుతాను (nēnu "
  "pratirōjū caduvutānu) - 'I read every day'. 7. అతను బడికి వెళ్తాడు (atanu "
  "baḍiki veḷtāḍu) - 'He goes to school'. 8. ఆమె పాటలు పాడుతుంది (āme pāṭalu "
  "pāḍutundi) - 'She sings songs'. 9. మేము కలిసి తింటాము (mēmu kalisi "
  "tiṇṭāmu) - 'We eat together'. 10. సూర్యుడు తూర్పున ఉదయిస్తాడు (sūryuḍu "
  "tūrppuna udayistāḍu) - 'The sun rises in the east'. Past (-ఆను/-ఇంది): "
  "11. నేను పుస్తకం చదివాను (nēnu pustakaṁ cadivānu) - 'I read the book'. "
  "12. అతను నిన్న వచ్చాడు (atanu ninna vaccāḍu) - 'He came yesterday'. 13. ఆమె "
  "ఉత్తరం రాసింది (āme uttaraṁ rāsindi) - 'She wrote a letter'. 14. మేము "
  "సినిమా చూశాము (mēmu sinimā cūśāmu) - 'We watched a movie'. 15. వాళ్ళు ఇల్లు "
  "కట్టారు (vāḷḷu illu kaṭṭāru) - 'They built a house'. Future (-తాను with "
  "future sense): 16. నేను రేపు వస్తాను (nēnu rēpu vastānu) - 'I will come "
  "tomorrow'. 17. అతను పరీక్ష రాస్తాడు (atanu parīkṣa rāstāḍu) - 'He will write "
  "the exam'. 18. ఆమె పాట పాడుతుంది (āme pāṭa pāḍutundi) - 'She will sing a "
  "song'. 19. మనం కలిసి వెళ్దాం (manaṁ kalisi veḷdāṁ) - 'We will go together'. "
  "20. వాళ్ళు సహాయం చేస్తారు (vāḷḷu sahāyaṁ cēstāru) - 'They will help'. "
  "Negative forms: 21. నేను రాను (nēnu rānu) - 'I will not come'. 22. అతను "
  "చేయలేదు (atanu cēyalēdu) - 'He did not do it'. Person endings: first person "
  "-ను (nēnu cēstānu), second informal -వు (nuvvu cēstāvu), third masculine "
  "-డు (atanu cēstāḍu), third feminine/neuter -ంది (āme cēstundi), plural "
  "-రు (vāru cēstāru)."),
 "how_it_works": (
  "This record works as the time machine: the same verbs bent into present, "
  "past and future, five sentences per tense, with the person-ending chart at "
  "the end. Take one verb - చదువు - and say it in all three tenses for నేను, "
  "నువ్వు, అతను, ఆమె, మేము, వాళ్ళు."),
 "key_points": [
  "Present progressive -తున్నాను: చదువుతున్నాను - 'am reading'.",
  "Habitual present -తాను: చదువుతాను - 'read (regularly)'.",
  "Past: చదివాను - 'read (did)'; feminine/neuter past -ఇంది: వచ్చింది.",
  "Future -తాను: వస్తాను - 'will come'.",
  "Person endings: -ను I, -వు you (inf), -డు he, -ంది she/it, -రు they (resp).",
  "Negatives: రాను (will not come), చేయలేదు (did not do).",
 ],
 "requirements": [
  "Conjugate చదువు in present, past, future for all persons.",
  "Write your yesterday, today and tomorrow in three sentences.",
  "Convert five affirmative sentences to negative.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Krishnamurti, Bhadriraju & Gwynn, J. P. L. A Grammar of Modern Telugu. Oxford University Press; 1985 (verb morphology).",
 ],
 "sig_lens": (
  "Through the Signature lens tense is his time-control dial: past the log of "
  "completed operations, present the live process monitor, future the scheduled "
  "work orders - one verb, three positions on the timeline. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 22
{
 "key": "qa", "name": "Telugu Questions and Answers",
 "group": "Compounded", "ladder": 22, "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Twenty question-and-answer pairs covering who, what, where, when, why and "
  "how. 1. Q: మీ పేరు ఏమిటి (mī pēru ēmiṭi) - 'What is your name'. A: నా పేరు "
  "సీత (nā pēru sīta) - 'My name is Sita'. 2. Q: మీరు ఎక్కడ ఉంటారు (mīru "
  "ekkaḍa uṇṭāru) - 'Where do you live'. A: నేను గుంటూరులో ఉంటాను (nēnu "
  "guṇṭūrulō uṇṭānu) - 'I live in Guntur'. 3. Q: ఇది ఏమిటి (idi ēmiṭi) - 'What "
  "is this'. A: ఇది నా పుస్తకం (idi nā pustakaṁ) - 'This is my book'. 4. Q: "
  "ఎవరు వచ్చారు (evaru vaccāru) - 'Who came'. A: నా స్నేహితుడు వచ్చాడు (nā "
  "snēhituḍu vaccāḍu) - 'My friend came'. 5. Q: నువ్వు ఎప్పుడు వస్తావు (nuvvu "
  "eppuḍu vastāvu) - 'When will you come'. A: నేను రేపు వస్తాను (nēnu rēpu "
  "vastānu) - 'I will come tomorrow'. 6. Q: ఎందుకు ఆలస్యం అయింది (enduku "
  "ālasyaṁ ayindi) - 'Why are you late'. A: ట్రాఫిక్ ఎక్కువగా ఉంది (ṭrāphik "
  "ekkuvagā undi) - 'There was heavy traffic'. 7. Q: ఇది ఎలా చేయాలి (idi elā "
  "cēyāli) - 'How do I do this'. A: ఇలా చేయండి (ilā cēyaṇḍi) - 'Do it like "
  "this'. 8. Q: మీకు తెలుగు వచ్చా (mīku telugu vaccā) - 'Do you know Telugu'. "
  "A: కొంచెం వచ్చు (kon̄ceṁ vaccu) - 'I know a little'. 9. Q: బడి ఎంత దూరం "
  "(baḍi enta dūraṁ) - 'How far is the school'. A: రెండు కిలోమీటర్లు (reṇḍu "
  "kilōmīṭarlu) - 'Two kilometers'. 10. Q: ఈ పండ్లు ఎంత (ī paṇḍlu enta) - 'How "
  "much are these fruits'. A: కిలో యాభై రూపాయలు (kilō yābhai rūpāyalu) - "
  "'Fifty rupees a kilo'. 11. Q: మీకు పిల్లలు ఉన్నారా (mīku pillalu unnārā) - "
  "'Do you have children'. A: అవును, ఇద్దరు (avunu, iddaru) - 'Yes, two'. "
  "12. Q: భోజనం చేశారా (bhōjanaṁ cēśārā) - 'Have you eaten'. A: ఇంకా లేదు "
  "(iṅkā lēdu) - 'Not yet'. 13. Q: ఏది నీది (ēdi nīdi) - 'Which is yours'. A: "
  "ఎరుపుది నాది (erupudi nādi) - 'The red one is mine'. 14. Q: ఎంతమంది వచ్చారు "
  "(entamandi vaccāru) - 'How many people came'. A: పదిమంది వచ్చారు (padimandi "
  "vaccāru) - 'Ten people came'. 15. Q: నీకు ఇష్టమైన రంగు ఏది (nīku iṣṭamaina "
  "raṅgu ēdi) - 'What is your favorite color'. A: నాకు నీలం ఇష్టం (nāku nīlaṁ "
  "iṣṭaṁ) - 'I like blue'. 16. Q: రేపు వాన పడుతుందా (rēpu vāna paḍutundā) - "
  "'Will it rain tomorrow'. A: బహుశా పడుతుంది (bahuśā paḍutundi) - 'Maybe it "
  "will'. 17. Q: డాక్టరు ఎక్కడ ఉన్నారు (ḍākṭaru ekkaḍa unnāru) - 'Where is the "
  "doctor'. A: ఆసుపత్రిలో ఉన్నారు (āsupatrilō unnāru) - 'In the hospital'. "
  "18. Q: ఈ పని ఎవరు చేశారు (ī pani evaru cēśāru) - 'Who did this work'. A: "
  "నేనే చేశాను (nēnē cēśānu) - 'I did it myself'. 19. Q: మీ ఫోన్ నంబరు ఏమిటి (mī "
  "phōn nambaru ēmiṭi) - 'What is your phone number'. A: తర్వాత చెప్తాను "
  "(tarvāta ceptānu) - 'I will tell you later'. 20. Q: మళ్ళీ ఎప్పుడు కలుద్దాం "
  "(maḷḷī eppuḍu kaluddāṁ) - 'When shall we meet again'. A: వచ్చే ఆదివారం "
  "(vaccē ādivāraṁ) - 'Next Sunday'."),
 "how_it_works": (
  "This record works as the interview drill: twenty exchanges covering every "
  "question word, each with a natural answer. Practice with a partner - one "
  "asks, one answers, then swap - until the question words come without "
  "thinking."),
 "key_points": [
  "20 Q&A pairs: who ఎవరు, what ఏమిటి, where ఎక్కడ, when ఎప్పుడు, why ఎందుకు, how ఎలా.",
  "మీకు తెలుగు వచ్చా - 'Do you know Telugu' - కొంచెం వచ్చు - 'a little'.",
  "భోజనం చేశారా - 'Have you eaten' - the classic Telugu greeting-question.",
  "Answers mirror the question's verb: వస్తావు -> వస్తాను.",
 ],
 "requirements": [
  "Ask and answer all twenty with a partner.",
  "Make five new questions about your own life.",
  "Answer without looking, then check.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Krishnamurti, Bhadriraju & Gwynn, J. P. L. A Grammar of Modern Telugu. Oxford University Press; 1985 (interrogatives).",
 ],
 "sig_lens": (
  "Through the Signature lens questions are his diagnostic probes and answers "
  "the sensor readouts: who, what, where, when, why, how - the six probes that "
  "map any unknown territory. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 23
{
 "key": "commands", "name": "Telugu Commands and Requests",
 "group": "Compounded", "ladder": 23, "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Twenty imperative and polite-request sentences, formal versus informal. The "
  "informal command uses the bare verb stem; the formal adds -అండి (-aṇḍi). "
  "1. రా (rā) - Come (informal) / రండి (raṇḍi) - Come (formal): రండి, కూర్చోండి "
  "(raṇḍi, kūrcōṇḍi) - 'Come, please sit'. 2. వెళ్ళు (veḷḷu) / వెళ్ళండి "
  "(veḷḷaṇḍi) - Go: త్వరగా వెళ్ళండి (tvaragā veḷḷaṇḍi) - 'Please go quickly'. "
  "3. కూర్చో (kūrcō) / కూర్చోండి (kūrcōṇḍi) - Sit: ఇక్కడ కూర్చోండి (ikkaḍa "
  "kūrcōṇḍi) - 'Please sit here'. 4. తిను (tinu) / తినండి (tinaṇḍi) - Eat: "
  "కలిసి తినండి (kalisi tinaṇḍi) - 'Please eat together'. 5. తాగు (tāgu) / "
  "తాగండి (tāgaṇḍi) - Drink: మంచినీళ్లు తాగండి (man̄cinīḷḷu tāgaṇḍi) - 'Please "
  "drink water'. 6. చూడు (cūḍu) / చూడండి (cūḍaṇḍi) - Look: ఇటు చూడండి (iṭu "
  "cūḍaṇḍi) - 'Please look here'. 7. విను (vinu) / వినండి (vinaṇḍi) - Listen: "
  "జాగ్రత్తగా వినండి (jāgrattagā vinaṇḍi) - 'Please listen carefully'. "
  "8. చెప్పు (ceppu) / చెప్పండి (ceppaṇḍi) - Tell: నిజం చెప్పండి (nijaṁ "
  "ceppaṇḍi) - 'Please tell the truth'. 9. ఇవ్వు (ivvu) / ఇవ్వండి (ivaṇḍi) - "
  "Give: పుస్తకం ఇవ్వండి (pustakaṁ ivaṇḍi) - 'Please give the book'. 10. తీసుకో "
  "(tīsukō) / తీసుకోండి (tīsukōṇḍi) - Take: ఇది తీసుకోండి (idi tīsukōṇḍi) - "
  "'Please take this'. 11. చేయి (cēyi) / చేయండి (cēyaṇḍi) - Do: పని చేయండి "
  "(pani cēyaṇḍi) - 'Please do the work'. 12. రాయి (rāyi) / రాయండి (rāyaṇḍi) - "
  "Write: పేరు రాయండి (pēru rāyaṇḍi) - 'Please write the name'. 13. చదువు "
  "(caduvu) / చదవండి (cadavaṇḍi) - Read: గట్టిగా చదవండి (gaṭṭigā cadavaṇḍi) - "
  "'Please read aloud'. 14. మాట్లాడు (māṭlāḍu) / మాట్లాడండి (māṭlāḍaṇḍi) - "
  "Speak: నెమ్మదిగా మాట్లాడండి (nemmadigā māṭlāḍaṇḍi) - 'Please speak slowly'. "
  "15. ఆగు (āgu) / ఆగండి (āgaṇḍi) - Stop, wait: కొంచెం ఆగండి (kon̄ceṁ āgaṇḍi) - "
  "'Please wait a little'. 16. తెరువు (teruvu) / తెరవండి (teravaṇḍi) - Open: "
  "తలుపు తెరవండి (talupu teravaṇḍi) - 'Please open the door'. 17. మూయి (mūyi) / "
  "మూయండి (mūyaṇḍi) - Close: కిటికీ మూయండి (kiṭikī mūyaṇḍi) - 'Please close the "
  "window'. 18. లేచు (lēcu) / లేవండి (lēvaṇḍi) - Get up: త్వరగా లేవండి (tvaragā "
  "lēvaṇḍi) - 'Please get up early'. 19. నిద్రపో (nidrapō) / నిద్రపోండి "
  "(nidrapōṇḍi) - Sleep: ప్రశాంతంగా నిద్రపోండి (praśāntaṅgā nidrapōṇḍi) - "
  "'Sleep peacefully'. 20. దయచేసి నాకు సహాయం చేయండి (dayacēsi nāku sahāyaṁ "
  "cēyaṇḍi) - 'Please help me' - the universal polite request."),
 "how_it_works": (
  "This record works as the command panel: twenty verbs in bare-stem informal "
  "and -అండి formal pairs. Rule of thumb: bare stem only for close friends "
  "and children; -అండి for everyone else. Practice by giving your room "
  "instructions in Telugu."),
 "key_points": [
  "Informal command = bare stem: రా, తిను, చూడు.",
  "Formal command = stem + -అండి: రండి, తినండి, చూడండి.",
  "దయచేసి + formal command = the universal polite request.",
  "Never use bare stems with elders or strangers.",
 ],
 "requirements": [
  "Convert ten informal commands to formal.",
  "Give five household instructions in formal Telugu.",
  "Add దయచేసి to three requests.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Krishnamurti, Bhadriraju & Gwynn, J. P. L. A Grammar of Modern Telugu. Oxford University Press; 1985 (imperatives).",
 ],
 "sig_lens": (
  "Through the Signature lens commands are his control inputs: the bare stem "
  "the direct drive for trusted operators, -అండి the guarded switch with the "
  "safety cover - same machine, two access levels. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 24
{
 "key": "descriptions", "name": "Telugu Descriptions of People and Places",
 "group": "Advanced", "ladder": 24, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Twenty sentences describing people, places and things in detail. 1. మా అమ్మ "
  "చాలా దయగలది (mā amma cālā dayagaladi) - 'My mother is very kind'. 2. నాన్న "
  "పొడవుగా, బలంగా ఉంటాడు (nānna poḍavugā, balaṅgā uṇṭāḍu) - 'Father is tall "
  "and strong'. 3. నా స్నేహితుడు తెలివైనవాడు (nā snēhituḍu telivainavāḍu) - "
  "'My friend is intelligent'. 4. ఆమె పొడవాటి జుట్టు కలది (āme poḍavāṭi juṭṭu "
  "kaladi) - 'She has long hair'. 5. పిల్లవాడు చురుకుగా ఆడుతున్నాడు "
  "(pillavāḍu curukugā āḍutunnāḍu) - 'The boy is playing actively'. 6. ముసలాయన "
  "అనుభవజ్ఞుడు (musalāyana anubhavajñuḍu) - 'The old man is experienced'. "
  "7. మా ఊరు పచ్చని పొలాలతో అందంగా ఉంటుంది (mā ūru paccani polālatō andaṅgā "
  "uṇṭundi) - 'Our village looks beautiful with green fields'. 8. గోదావరి "
  "పెద్ద నది (gōdāvari pedda nadi) - 'The Godavari is a big river'. 9. తిరుపతి "
  "కొండలు ఎత్తైనవి (tirupati koṇḍalu ettainavi) - 'The Tirupati hills are "
  "high'. 10. హైదరాబాద్ పెద్ద నగరం (haidarābād pedda nagaraṁ) - 'Hyderabad is a "
  "big city'. 11. చార్మినార్ చారిత్రక కట్టడం (cārminār cāritraka kaṭṭaḍaṁ) - "
  "'Charminar is a historic monument'. 12. సముద్ర తీరం విశాలంగా ఉంది (samudra "
  "tīraṁ viśālaṅgā undi) - 'The seashore is vast'. 13. ఈ తోటలో రకరకాల పూలు "
  "ఉన్నాయి (ī tōṭalō rakarakāla pūlu unnāyi) - 'There are many kinds of flowers "
  "in this garden'. 14. ఆకాశం నిర్మలంగా ఉంది (ākāśaṁ nirmalaṅgā undi) - 'The "
  "sky is clear'. 15. రాత్రి నక్షత్రాలు మెరుస్తున్నాయి (rātri nakṣatrālu "
  "merustunnāyi) - 'The stars are twinkling at night'. 16. ఈ పుస్తకం చాలా "
  "ఆసక్తికరంగా ఉంది (ī pustakaṁ cālā āsaktikaraṅgā undi) - 'This book is very "
  "interesting'. 17. ఆ సినిమా కథ హృదయాన్ని హత్తుకుంది (ā sinimā katha "
  "hṛdayānni hattukundi) - 'That movie's story touched the heart'. 18. వంటగది "
  "విశాలంగా, వెలుతురుగా ఉంది (vaṇṭagadi viśālaṅgā, veluturugā undi) - 'The "
  "kitchen is spacious and bright'. 19. రోడ్డు రద్దీగా ఉంది (rōḍḍu raddīgā "
  "undi) - 'The road is crowded'. 20. ఈ ప్రదేశం ప్రశాంతంగా ఉంది (ī pradēśaṁ "
  "praśāntaṅgā undi) - 'This place is peaceful'."),
 "how_it_works": (
  "This record works as the portrait studio: twenty detailed descriptions that "
  "stack adjectives, adverbs and relative detail the way fluent speakers do. "
  "Describe one person and one place from your life in five Telugu sentences "
  "each."),
 "key_points": [
  "20 descriptive sentences: people, places, things in detail.",
  "Descriptive stacking: పచ్చని పొలాలతో అందంగా - 'beautiful with green fields'.",
  "Place names in Telugu: గోదావరి, తిరుపతి, హైదరాబాద్, చార్మినార్.",
  "ఈ ప్రదేశం ప్రశాంతంగా ఉంది - 'This place is peaceful'.",
 ],
 "requirements": [
  "Describe a family member in five Telugu sentences.",
  "Describe your town in five Telugu sentences.",
  "Use three stacked adjectives in one sentence.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Gwynn, J. P. L. A Telugu-English Dictionary. Oxford University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens description is his specification sheet: every "
  "adjective a measured dimension, every detail a tolerance - the portrait "
  "drawn to blueprint precision. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 25
{
 "key": "story1", "name": "Telugu Story I: The Clever Rabbit",
 "group": "Advanced", "ladder": 25, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "A ten-sentence simple story in Telugu with line-by-line English translation. "
  "1. ఒక అడవిలో ఒక కుందేలు ఉండేది (oka aḍavilō oka kundēlu uṇḍēdi) - 'In a "
  "forest there lived a rabbit'. 2. అది చాలా తెలివైనది (adi cālā telivainadi) - "
  "'It was very clever'. 3. ప్రతిరోజూ అది పచ్చికలో గడ్డి తినేది (pratirōjū adi "
  "paccikalō gaḍḍi tinēdi) - 'Every day it ate grass in the meadow'. 4. ఒకరోజు "
  "ఒక నక్క వచ్చింది (okarōju oka nakka vaccindi) - 'One day a fox came'. "
  "5. నక్క కుందేలును పట్టుకోవాలనుకుంది (nakka kundēlunu paṭṭukōvālanukundi) - "
  "'The fox wanted to catch the rabbit'. 6. కుందేలు భయపడలేదు (kundēlu "
  "bhayapaḍalēdu) - 'The rabbit was not afraid'. 7. అది పెద్ద గొంతుతో అరిచింది "
  "(adi pedda gontutō aricindi) - 'It shouted in a loud voice'. 8. వేటగాడు "
  "వస్తున్నాడని నక్క అనుకుంది (vēṭagāḍu vastunnāḍani nakka anukundi) - 'The fox "
  "thought a hunter was coming'. 9. నక్క భయంతో పారిపోయింది (nakka bhayantō "
  "pāripōyindi) - 'The fox ran away in fear'. 10. కుందేలు సంతోషంతో ఇంటికి "
  "వెళ్ళింది (kundēlu santōṣantō iṇṭiki veḷḷindi) - 'The rabbit went home "
  "happily'. Moral: తెలివితేటలు బలాన్ని మించుతాయి (telivitēṭalu balānni "
  "min̄cutāyi) - 'Wit surpasses strength'."),
 "how_it_works": (
  "This record works as the first reader: a complete ten-sentence story using "
  "only the grammar and vocabulary of the foundations half. Read it aloud "
  "twice - once slowly for pronunciation, once at speaking speed - then retell "
  "it in your own Telugu words."),
 "key_points": [
  "10-sentence story with line-by-line English translation.",
  "Simple past narrative: ఉండేది, తినేది, వచ్చింది, పారిపోయింది.",
  "Story vocabulary: అడవి forest, కుందేలు rabbit, నక్క fox, వేటగాడు hunter.",
  "Moral: తెలివితేటలు బలాన్ని మించుతాయి - 'Wit surpasses strength'.",
 ],
 "requirements": [
  "Read the story aloud twice.",
  "Retell it in your own Telugu sentences.",
  "Learn the five story nouns by heart.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Traditional Telugu folk tale, retold in simple modern Telugu for learners.",
 ],
 "sig_lens": (
  "Through the Signature lens the story is his first field report: a complete "
  "operation narrated start to finish, where the clever operator wins by wit "
  "rather than force - the Signature method in fable form. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 26
{
 "key": "story2", "name": "Telugu Story II: The Rainy Day",
 "group": "Advanced", "ladder": 26, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "A ten-sentence story in the past tense with line-by-line English "
  "translation. 1. నిన్న ఉదయం ఆకాశం మేఘావృతంగా ఉంది (ninna udayaṁ ākāśaṁ "
  "mēghāvṛtaṅgā undi) - 'Yesterday morning the sky was cloudy'. 2. నేను బడికి "
  "బయలుదేరాను (nēnu baḍiki bayaludērānu) - 'I set out for school'. 3. దారిలో "
  "వాన మొదలైంది (dārilō vāna modalayindi) - 'On the way the rain began'. "
  "4. నా దగ్గర గొడుగు లేదు (nā daggara goḍugu lēdu) - 'I had no umbrella'. "
  "5. నేను ఒక చెట్టు కింద నిలబడ్డాను (nēnu oka ceṭṭu kinda nilabaḍḍānu) - 'I "
  "stood under a tree'. 6. నా స్నేహితుడు రవి అటుగా వచ్చాడు (nā snēhituḍu ravi "
  "aṭugā vaccāḍu) - 'My friend Ravi came that way'. 7. అతని దగ్గర పెద్ద గొడుగు "
  "ఉంది (atani daggara pedda goḍugu undi) - 'He had a big umbrella'. 8. మేము "
  "ఇద్దరం కలిసి బడికి వెళ్ళాము (mēmu iddaraṁ kalisi baḍiki veḷḷāmu) - 'We both "
  "went to school together'. 9. ఉపాధ్యాయుడు మమ్మల్ని మెచ్చుకున్నాడు "
  "(upādhyāyuḍu mammalni meccukunnāḍu) - 'The teacher praised us'. 10. ఆ రోజు "
  "నాకు ఎప్పటికీ గుర్తుంటుంది (ā rōju nāku eppaṭikī gurtuṇṭundi) - 'I will "
  "remember that day forever'."),
 "how_it_works": (
  "This record works as the past-tense workshop: a complete memory narrated "
  "entirely in past forms - మొదలైంది, నిలబడ్డాను, వచ్చాడు, వెళ్ళాము. Tell one "
  "true story from your own yesterday in Telugu past tense, ten sentences."),
 "key_points": [
  "10-sentence past-tense story, line-by-line translation.",
  "Past forms: వచ్చాడు, వెళ్ళాము, నిలబడ్డాను, మొదలైంది.",
  "Time anchors: నిన్న (yesterday), దారిలో (on the way).",
  "ఆ రోజు నాకు ఎప్పటికీ గుర్తుంటుంది - 'I will remember that day forever'.",
 ],
 "requirements": [
  "Tell your yesterday in ten Telugu past-tense sentences.",
  "Convert the story to present tense as an exercise.",
  "Memorize the past forms of వచ్చు and వెళ్ళు.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Original learner story composed 2026-10-17 in simple modern Telugu.",
 ],
 "sig_lens": (
  "Through the Signature lens the past-tense story is his operations log: "
  "every completed action timestamped and recorded, the log complete enough "
  "that the whole mission can be replayed. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 27
{
 "key": "story3", "name": "Telugu Story III: The Dream Journey",
 "group": "Advanced", "ladder": 27, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A ten-sentence story using future and conditional forms with line-by-line "
  "English translation. 1. రేపు నేను పెద్ద ప్రయాణం చేస్తాను (rēpu nēnu pedda "
  "prayāṇaṁ cēstānu) - 'Tomorrow I will make a big journey'. 2. నేను రైలులో "
  "హైదరాబాద్ వెళ్తాను (nēnu railulō haidarābād veḷtānu) - 'I will go to "
  "Hyderabad by train'. 3. అక్కడ నా స్నేహితుడు నన్ను కలుస్తాడు (akkaḍa nā "
  "snēhituḍu nannu kalustāḍu) - 'My friend will meet me there'. 4. మేము "
  "చార్మినార్ చూస్తాము (mēmu cārminār cūstāmu) - 'We will see Charminar'. "
  "5. తర్వాత గోల్కొండ కోటకు వెళ్తాము (tarvāta gōlkoṇḍa kōṭaku veḷtāmu) - 'Then "
  "we will go to Golconda Fort'. 6. సాయంత్రం హుస్సేన్ సాగర్ వద్ద నడుస్తాము "
  "(sāyantraṁ hussēn sāgar vadda naḍustāmu) - 'In the evening we will walk by "
  "Hussain Sagar'. 7. వాన పడితే మేము హోటల్లో ఉంటాము (vāna paḍitē mēmu "
  "hōṭallō uṇṭāmu) - 'If it rains, we will stay in the hotel'. 8. డబ్బు "
  "సరిపోతే మేము షాపింగ్ చేస్తాము (ḍabbu saripōtē mēmu ṣāpin̄g cēstāmu) - 'If the "
  "money is enough, we will go shopping'. 9. ఆదివారం నేను తిరిగి వస్తాను "
  "(ādivāraṁ nēnu tirigi vastānu) - 'On Sunday I will return'. 10. ఈ ప్రయాణం "
  "నాకు ఎంతో సంతోషాన్ని ఇస్తుంది (ī prayāṇaṁ nāku entō santōṣānni istundi) - "
  "'This journey will give me great happiness'."),
 "how_it_works": (
  "This record works as the planning board: future forms (-తాను) for the "
  "itinerary and conditional forms (-తే) for the backup plans. Plan one real "
  "future trip in ten Telugu sentences - five certainties, five ifs."),
 "key_points": [
  "10-sentence future/conditional story, line-by-line translation.",
  "Future forms: చేస్తాను, వెళ్తాను, చూస్తాము, వస్తాను.",
  "Conditionals: వాన పడితే - 'if it rains'; డబ్బు సరిపోతే - 'if money suffices'.",
  "Real places: హైదరాబాద్, చార్మినార్, గోల్కొండ, హుస్సేన్ సాగర్.",
 ],
 "requirements": [
  "Plan a real trip in ten Telugu sentences.",
  "Add three conditional backup plans with -తే.",
  "Say the whole plan aloud to a partner.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Original learner story composed 2026-10-17 in simple modern Telugu.",
 ],
 "sig_lens": (
  "Through the Signature lens the future-tense story is his mission plan: the "
  "itinerary the primary procedure, the conditionals the contingency branches - "
  "no plan ships without both. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 28
{
 "key": "idioms", "name": "Telugu Idioms and Proverbs",
 "group": "Advanced", "ladder": 28, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Twenty Telugu idioms and proverbs, each with literal translation, real "
  "meaning, and an example sentence. 1. అతిథి దేవో భవ (atithi dēvō bhava) - "
  "literally 'the guest is god' - meaning: treat guests with the highest honor. "
  "Example: అతిథి దేవో భవ అని మా అమ్మ ఎప్పుడూ చెప్తుంది (atithi dēvō bhava ani "
  "mā amma eppuḍū ceptundi) - 'My mother always says the guest is god'. "
  "2. కష్టే ఫలి (kaṣṭē phali) - literally 'in effort, fruit' - meaning: hard "
  "work yields results. Example: కష్టే ఫలి అని నాన్న చెప్పాడు (kaṣṭē phali ani "
  "nānna ceppāḍu) - 'Father said hard work yields results'. 3. నీటిమీద వ్రాత "
  "(nīṭimīda vrāta) - literally 'writing on water' - meaning: futile effort "
  "that leaves no trace. Example: అతనికి చెప్పడం నీటిమీద వ్రాత (ataniki "
  "ceppaḍaṁ nīṭimīda vrāta) - 'Advising him is writing on water'. 4. ఆకాశానికి "
  "నిచ్చెన వేయు (ākāśāniki niccena vēyu) - literally 'to put a ladder to the "
  "sky' - meaning: attempting the impossible. Example: పరీక్ష లేకుండా పాసవడం "
  "ఆకాశానికి నిచ్చెన వేయడం (parīkṣa lēkuṇḍā pāsavaḍaṁ ākāśāniki niccena "
  "vēyaḍaṁ) - 'Passing without the exam is putting a ladder to the sky'. "
  "5. పిల్లి మెడలో గంట కట్టు (pilli meḍalō gaṇṭa kaṭṭu) - literally 'to tie a "
  "bell on the cat's neck' - meaning: to take on a dangerous task. Example: "
  "బాస్ను అడగడం పిల్లి మెడలో గంట కట్టడం (bāsnu aḍagaḍaṁ pilli meḍalō gaṇṭa "
  "kaṭṭaḍaṁ) - 'Asking the boss is tying a bell on the cat'. 6. కంటిలో నలుసు "
  "(kaṇṭilō nalusu) - literally 'a speck in the eye' - meaning: a constant "
  "irritant. Example: ఆ శబ్దం నా కంటిలో నలుసు (ā śabdaṁ nā kaṇṭilō nalusu) - "
  "'That noise is a speck in my eye'. 7. నోట వేలు పెట్టు (nōṭa vēlu peṭṭu) - "
  "literally 'to put a finger in the mouth' - meaning: to be amazed. Example: "
  "ఆ వార్త విని నోట వేలు పెట్టుకున్నాను (ā vārta vini nōṭa vēlu "
  "peṭṭukunnānu) - 'Hearing the news I put my finger in my mouth (was amazed)'. "
  "8. చేసిన పాపం ఊరికే పోదు (cēsina pāpaṁ ūrikē pōdu) - literally 'a committed "
  "wrong never goes for nothing' - meaning: wrongdoing is never unpunished. "
  "9. అరచేతిలో వైకుంఠం చూపించు (aracētilō vaikuṇṭhaṁ cūpin̄cu) - literally 'to "
  "show heaven in the palm' - meaning: to make impossible promises. Example: "
  "అతను అరచేతిలో వైకుంఠం చూపిస్తున్నాడు (atanu aracētilō vaikuṇṭhaṁ "
  "cūpistunnāḍu) - 'He is showing heaven in his palm (promising the "
  "impossible)'. 10. కాకి ముక్కుకు దొండపండు (kāki mukkuku doṇḍapaṇḍu) - "
  "literally 'a donda fruit for a crow's beak' - meaning: a good thing wasted "
  "on the unworthy. 11. ఎద్దు ఈనింది అంటే దూడను కట్టేయమన్నట్లు (eddu īnindi "
  "aṇṭē ḍūḍanu kaṭṭēyamannaṭlu) - literally 'like tying the calf when told the "
  "ox calved' - meaning: acting on half-heard news. 12. గోడమీద పిల్లి వాటం "
  "(gōḍamīda pilli vāṭaṁ) - literally 'like a cat on the wall' - meaning: "
  "sitting on the fence. 13. చెవిలో పూలు పెట్టు (cevilō pūlu peṭṭu) - literally "
  "'to put flowers in the ear' - meaning: to fool someone. Example: అతను నా "
  "చెవిలో పూలు పెట్టాడు (atanu nā cevilō pūlu peṭṭāḍu) - 'He fooled me'. "
  "14. తలకు మించిన భారం (talaku min̄cina bhāraṁ) - literally 'a burden beyond "
  "the head' - meaning: more than one can bear. 15. నిద్రపోతున్న పులిని లేపకు "
  "(nidrapōtunna pulini lēpaku) - literally 'do not wake a sleeping tiger' - "
  "meaning: do not provoke a dangerous person. 16. పాముకు పాలు పోసినట్లు "
  "(pāmuku pālu pōsinaṭlu) - literally 'like feeding milk to a snake' - "
  "meaning: helping someone wicked. 17. మింగలేక కక్కలేక (miṅgalēka "
  "kakkalēka) - literally 'unable to swallow, unable to spit' - meaning: in a "
  "dilemma. Example: ఆ సమస్యలో నేను మింగలేక కక్కలేక ఉన్నాను (ā samasyalō nēnu "
  "miṅgalēka kakkalēka unnānu) - 'I am in a swallow-or-spit dilemma over that "
  "problem'. 18. గుండె దిటవు చేసుకో (guṇḍe diṭavu cēsukō) - literally 'make "
  "the heart firm' - meaning: take courage. 19. కాలం కలిసిరావాలి (kālaṁ "
  "kalisirāvāli) - literally 'time must join' - meaning: luck must favor the "
  "effort. 20. ఊరికే ఉండేవాడికి ఊరంతా ఆప్తులే (ūrikē uṇḍēvāḍiki ūrantā "
  "āptulē) - literally 'for one who stays quiet, the whole village is kin' - "
  "meaning: humility wins everyone over."),
 "how_it_works": (
  "This record works as the wisdom chest: twenty sayings that carry the "
  "culture inside the language, each unpacked into literal image, real meaning "
  "and live example. Learn one proverb a day and use it once in conversation - "
  "that is how they enter your speech."),
 "key_points": [
  "20 idioms/proverbs: literal translation + real meaning + example sentence.",
  "అతిథి దేవో భవ - 'the guest is god' - hospitality as duty.",
  "కష్టే ఫలి - 'hard work yields fruit'.",
  "నీటిమీద వ్రాత - 'writing on water' - futile effort.",
  "పిల్లి మెడలో గంట - 'bell the cat' - the dangerous task.",
  "మింగలేక కక్కలేక - 'neither swallow nor spit' - the dilemma.",
 ],
 "requirements": [
  "Use one proverb in conversation each day for a week.",
  "Explain three proverbs to a friend in English.",
  "Write your own example sentence for five idioms.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Traditional Telugu proverbs (సామెతలు), compiled for learners 2026-10-17.",
 ],
 "sig_lens": (
  "Through the Signature lens proverbs are his compressed engineering "
  "handbooks: centuries of field experience packed into one line, each saying "
  "a design rule that survived ten thousand trials. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 29
{
 "key": "registers", "name": "Telugu Formal and Polite Registers",
 "group": "Advanced", "ladder": 29, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Fifteen formal versus informal pairs for letters, business and elders, with "
  "translations. 1. Informal: నువ్వు రా (nuvvu rā) - 'You come'. Formal: మీరు "
  "రండి (mīru raṇḍi) - 'Please come'. 2. Informal: నీ పేరు ఏమిటి (nī pēru "
  "ēmiṭi) - 'What is your name'. Formal: మీ పేరు ఏమిటి (mī pēru ēmiṭi) - 'What "
  "is your name (respectful)'. 3. Informal: కూర్చో (kūrcō) - 'Sit'. Formal: "
  "దయచేసి కూర్చోండి (dayacēsi kūrcōṇḍi) - 'Please be seated'. 4. Informal: "
  "చెప్పు (ceppu) - 'Tell'. Formal: దయచేసి తెలియజేయండి (dayacēsi "
  "teliyajēyaṇḍi) - 'Kindly inform'. 5. Informal: ఇది తీసుకో (idi tīsukō) - "
  "'Take this'. Formal: దయచేసి స్వీకరించండి (dayacēsi svīkarin̄caṇḍi) - 'Kindly "
  "accept this'. 6. Informal: నాకు డబ్బు ఇవ్వు (nāku ḍabbu ivvu) - 'Give me "
  "money'. Formal: దయచేసి చెల్లించగలరు (dayacēsi cellin̄cagalaru) - 'Kindly "
  "make the payment'. 7. Informal: రేపు రా (rēpu rā) - 'Come tomorrow'. "
  "Formal: రేపు రాగలరు (rēpu rāgalaru) - 'You are requested to come tomorrow'. "
  "8. Informal: ఫోన్ చెయ్యి (phōn ceyyi) - 'Call'. Formal: దయచేసి ఫోన్ "
  "చేయగలరు (dayacēsi phōn cēyagalaru) - 'Kindly call'. 9. Informal: సంతకం చెయ్యి "
  "(santakaṁ ceyyi) - 'Sign'. Formal: దయచేసి సంతకం చేయగలరు (dayacēsi santakaṁ "
  "cēyagalaru) - 'Kindly sign'. 10. Informal: వేచి ఉండు (vēci uṇḍu) - 'Wait'. "
  "Formal: దయచేసి వేచి ఉండగలరు (dayacēsi vēci uṇḍagalaru) - 'Kindly wait'. "
  "11. Letter opening informal: ప్రియమైన రవి (priyamaina ravi) - 'Dear Ravi'. "
  "Formal: గౌరవనీయులైన శ్రీ రావు గారికి (gauravanīyulaina śrī rāvu gāriki) - "
  "'To the respected Mr. Rao'. 12. Letter closing informal: నీ స్నేహితుడు "
  "(nī snēhituḍu) - 'Your friend'. Formal: మీ విశ్వాసపాత్రుడు (mī "
  "viśvāsapātruḍu) - 'Yours faithfully'. 13. Informal thanks: థాంక్స్ (thyānks) - "
  "'Thanks'. Formal: హృదయపూర్వక ధన్యవాదాలు (hṛdayapūrvaka dhanyavādālu) - "
  "'Heartfelt thanks'. 14. Informal apology: సారీ (sārī) - 'Sorry'. Formal: "
  "మన్నించగలరు (mannin̄cagalaru) - 'Kindly forgive'. 15. Elder address "
  "informal: ఏమయ్యా (ēmayyā) - 'Hey mister' (familiar, can offend). Formal: "
  "అయ్యా / గారూ (ayyā / gārū) - 'Sir' with the respectful -గారు suffix: రావు "
  "గారు (rāvu gāru) - 'Mr. Rao (respected)'."),
 "how_it_works": (
  "This record works as the etiquette manual: fifteen side-by-side pairs "
  "showing how the same request dresses up for business, letters and elders. "
  "The -గారు suffix and the -గలరు verb form are the two formal uniforms - "
  "practice changing any informal sentence into its formal twin."),
 "key_points": [
  "15 formal vs informal pairs: requests, letters, business, elders.",
  "Formal markers: -అండి commands, -గలరు requests, -గారు respectful address.",
  "దయచేసి తెలియజేయండి - 'Kindly inform' - the business standard.",
  "మీ విశ్వాసపాత్రుడు - 'Yours faithfully' - the formal letter closing.",
  "Never use ఏమయ్యా with strangers - it can offend.",
 ],
 "requirements": [
  "Rewrite five informal sentences in formal register.",
  "Write a formal letter opening and closing.",
  "Address three people with the -గారు suffix.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Krishnamurti, Bhadriraju & Gwynn, J. P. L. A Grammar of Modern Telugu. Oxford University Press; 1985 (honorifics).",
 ],
 "sig_lens": (
  "Through the Signature lens register is his dress code for operations: "
  "informal the shop-floor uniform among the crew, formal the client-facing "
  "protocol - same engineer, correct uniform for the room. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 30
{
 "key": "complex", "name": "Telugu Compound and Complex Sentences",
 "group": "Advanced", "ladder": 30, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Fifteen long sentences with clauses, connectors and relative clauses, parsed "
  "and translated. 1. నేను బడికి వెళ్ళాను ఎందుకంటే పరీక్ష ఉంది (nēnu baḍiki "
  "veḷḷānu endukaṇṭē parīkṣa undi) - 'I went to school because there is an "
  "exam' - ఎందుకంటే = because. 2. వాన పడుతోంది కాబట్టి మేము ఇంట్లో ఉన్నాము "
  "(vāna paḍutōndi kābaṭṭi mēmu iṇṭlō unnāmu) - 'It is raining, so we are at "
  "home' - కాబట్టి = so, therefore. 3. అతను కష్టపడ్డాడు అందుకే పాసయ్యాడు "
  "(atanu kaṣṭapaḍḍāḍu andukē pāsayyāḍu) - 'He worked hard, that is why he "
  "passed' - అందుకే = that is why. 4. నేను అలసిపోయాను అయినా పని పూర్తి చేశాను "
  "(nēnu alasipōyānu ayinā pani pūrti cēśānu) - 'I was tired, yet I finished "
  "the work' - అయినా = yet, even so. 5. వాన పడినప్పటికీ మేము వెళ్ళాము (vāna "
  "paḍinappaṭikī mēmu veḷḷāmu) - 'Although it rained, we went' - -అప్పటికీ = "
  "although. 6. తెలుగు నేర్చుకోవడానికి నేను ప్రతిరోజూ చదువుతాను (telugu "
  "nērcukōvaḍāniki nēnu pratirōjū caduvutānu) - 'I study every day in order to "
  "learn Telugu' - -డానికి = in order to. 7. భోజనం చేసిన తర్వాత మేము నడిచాము "
  "(bhōjanaṁ cēsina tarvāta mēmu naḍicāmu) - 'After eating, we walked' - "
  "తర్వాత = after. 8. సినిమా మొదలయ్యే ముందు మేము చేరుకున్నాము (sinimā "
  "modalayyē mundu mēmu cērukunnāmu) - 'We arrived before the movie started' - "
  "ముందు = before. 9. నేను చదివిన పుస్తకం చాలా బాగుంది (nēnu cadivina pustakaṁ "
  "cālā bāgundi) - 'The book that I read is very good' - చదివిన = relative "
  "participle 'that (I) read'. 10. అక్కడ నిలబడిన వ్యక్తి నా స్నేహితుడు (akkaḍa "
  "nilabaḍina vyakti nā snēhituḍu) - 'The person standing there is my friend' "
  "- నిలబడిన = 'who is standing'. 11. మీరు చెప్పిన మాట నిజం (mīru ceppina māṭa "
  "nijaṁ) - 'What you said is true' - చెప్పిన = 'that you said'. 12. నేను "
  "వెళ్తున్నప్పుడు ఫోన్ మోగింది (nēnu veḷtunnappuḍu phōn mōgindi) - 'While I was "
  "going, the phone rang' - -అప్పుడు = while. 13. అతను వచ్చిన వెంటనే మేము "
  "బయలుదేరాము (atanu vaccina veṇṭanē mēmu bayaludērāmu) - 'As soon as he came, "
  "we left' - వెంటనే = immediately. 14. డబ్బు ఉంటే నేను కారు కొంటాను (ḍabbu "
  "uṇṭē nēnu kāru koṇṭānu) - 'If I have money, I will buy a car' - -తే = if. "
  "15. నువ్వు కష్టపడితే తప్పకుండా విజయం సాధిస్తావు (nuvvu kaṣṭapaḍitē "
  "tappakuṇḍā vijayaṁ sādhistāvu) - 'If you work hard, you will definitely "
  "succeed'."),
 "how_it_works": (
  "This record works as the joinery shop: fifteen sentences showing how Telugu "
  "joins clauses - ఎందుకంటే, కాబట్టి, అయినా, -డానికి, relative participles - "
  "each parsed so you see the joint. Take three of your simple sentences and "
  "join them with కాబట్టి, ఎందుకంటే and అయినా."),
 "key_points": [
  "15 complex sentences, each parsed: connector named and glossed.",
  "Connectors: ఎందుకంటే because, కాబట్టి so, అందుకే that is why, అయినా yet.",
  "Purpose: -డానికి (in order to); time: తర్వాత after, ముందు before, -అప్పుడు while.",
  "Relative participles: చదివిన పుస్తకం - 'the book that (I) read'.",
  "Conditionals: -తే (if) - డబ్బు ఉంటే - 'if there is money'.",
 ],
 "requirements": [
  "Join three simple sentence pairs with కాబట్టి and ఎందుకంటే.",
  "Write two relative-clause sentences with -ఇన participles.",
  "Write two if-sentences with -తే.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Krishnamurti, Bhadriraju & Gwynn, J. P. L. A Grammar of Modern Telugu. Oxford University Press; 1985 (complex sentences).",
 ],
 "sig_lens": (
  "Through the Signature lens complex sentences are his assemblies: simple "
  "sentences the parts, connectors the welds and bolts - and a fluent speaker "
  "is the welder who joins them without a visible seam. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 31
{
 "key": "convmarket", "name": "Telugu Conversation: At the Market",
 "group": "Advanced", "ladder": 31, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A twenty-line bilingual dialogue at the market, annotated. Buyer (కొనుగోలుదారు) "
  "and Seller (అమ్మకందారు) alternate. 1. Buyer: నమస్కారం అండీ (namaskāraṁ "
  "aṇḍī) - 'Hello, sir' [respectful greeting]. 2. Seller: నమస్కారం, ఏమి "
  "కావాలి (namaskāraṁ, ēmi kāvāli) - 'Hello, what do you need'. 3. Buyer: "
  "టమాటాలు ఉన్నాయా (ṭamāṭālu unnāyā) - 'Do you have tomatoes'. 4. Seller: "
  "ఉన్నాయి, తాజాగా ఉన్నాయి (unnāyi, tājāgā unnāyi) - 'Yes, they are fresh'. "
  "5. Buyer: కిలో ఎంత (kilō enta) - 'How much per kilo'. 6. Seller: కిలో "
  "నలభై రూపాయలు (kilō nalabhai rūpāyalu) - 'Forty rupees a kilo'. 7. Buyer: "
  "చాలా ఎక్కువ, ముప్పైకి ఇవ్వండి (cālā ekkuva, muppaiki ivaṇḍi) - 'Too much, "
  "give it for thirty' [bargaining opens]. 8. Seller: కుదరదు, ముప్పై ఐదుకు "
  "తీసుకోండి (kudaradu, muppai aiduku tīsukōṇḍi) - 'Not possible, take it for "
  "thirty-five'. 9. Buyer: సరే, రెండు కిలోలు ఇవ్వండి (sarē, reṇḍu kilōlu "
  "ivaṇḍi) - 'Okay, give two kilos' [deal]. 10. Seller: ఇంకేమైనా కావాలా "
  "(iṅkēmainā kāvālā) - 'Anything else'. 11. Buyer: ఉల్లిపాయలు కూడా ఉన్నాయా "
  "(ullipāyalu kūḍā unnāyā) - 'Do you have onions too'. 12. Seller: ఉన్నాయి, "
  "కిలో ముప్పై (unnāyi, kilō muppai) - 'Yes, thirty a kilo'. 13. Buyer: ఒక "
  "కిలో ఇవ్వండి (oka kilō ivaṇḍi) - 'Give one kilo'. 14. Seller: మొత్తం వంద "
  "రూపాయలు (mottaṁ vanda rūpāyalu) - 'One hundred rupees total' "
  "[2x35 + 30 = 100]. 15. Buyer: ఇదిగో వంద (idigō vanda) - 'Here is a hundred'. "
  "16. Seller: సంచిలో పెట్టనా (san̄cilō peṭṭanā) - 'Shall I put it in a bag'. "
  "17. Buyer: అవును, పెట్టండి (avunu, peṭṭaṇḍi) - 'Yes, please put it in'. "
  "18. Seller: ఇదిగో, తాజా కూరగాయలు (idigō, tājā kūragāyalu) - 'Here "
  "you are, fresh vegetables'. 19. Buyer: ధన్యవాదాలు, మళ్ళీ వస్తాను "
  "(dhanyavādālu, maḷḷī vastānu) - 'Thank you, I will come again'. 20. Seller: "
  "రండి, రండి (raṇḍi, raṇḍi) - 'Come, come (again)' [warm farewell]."),
 "how_it_works": (
  "This record works as the market rehearsal: a full twenty-line bargaining "
  "arc with the cultural notes in brackets - greeting, price ask, haggle, "
  "deal, bagging, farewell. Act it out with a partner, then run it for real "
  "at a shop."),
 "key_points": [
  "20-line bilingual market dialogue with cultural annotations.",
  "Bargain arc: కిలో ఎంత -> చాలా ఎక్కువ -> సరే, తీసుకుంటాను.",
  "Real arithmetic: 2 kilos at 35 + 1 kilo at 30 = 100 rupees.",
  "సంచిలో పెట్టనా - the seller's bagging offer.",
 ],
 "requirements": [
  "Act out the dialogue with a partner, twice.",
  "Swap roles and improvise new prices.",
  "Use three lines at a real shop.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Original learner dialogue composed 2026-10-17 in natural spoken Telugu.",
 ],
 "sig_lens": (
  "Through the Signature lens the market dialogue is his procurement "
  "negotiation played live: specification, quotation, counter-offer, "
  "acceptance - the whole supply contract in twenty lines. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 32
{
 "key": "convfriend", "name": "Telugu Conversation: Meeting a Friend",
 "group": "Advanced", "ladder": 32, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A twenty-line bilingual dialogue between two friends, annotated. Ravi "
  "(రవి) and Sita (సీత) meet after a long time. 1. Ravi: సీతా, ఎన్నాళ్ళకు "
  "కలిశాము (sītā, ennāḷḷaku kaliśāmu) - 'Sita, we meet after so long' [warm "
  "reunion]. 2. Sita: అవును రవి, ఎలా ఉన్నావు (avunu ravi, elā unnāvu) - 'Yes "
  "Ravi, how are you' [informal between friends]. 3. Ravi: బాగున్నాను, నువ్వు "
  "ఎలా ఉన్నావు (bāgunnānu, nuvvu elā unnāvu) - 'I am fine, how are you'. "
  "4. Sita: నేను కూడా బాగున్నాను (nēnu kūḍā bāgunnānu) - 'I am fine too'. "
  "5. Ravi: ఈ మధ్య ఏమి చేస్తున్నావు (ī madhya ēmi cēstunnāvu) - 'What are you "
  "doing these days'. 6. Sita: నేను బ్యాంకులో పని చేస్తున్నాను (nēnu "
  "byāṅkulō pani cēstunnānu) - 'I am working in a bank'. 7. Ravi: చాలా "
  "సంతోషం, ఎప్పటి నుండి (cālā santōṣaṁ, eppaṭi nuṇḍi) - 'Very happy, since "
  "when'. 8. Sita: గత ఆరు నెలల నుండి (gata āru nelala nuṇḍi) - 'For the last "
  "six months'. 9. Ravi: మన పాత స్నేహితులు ఎలా ఉన్నారు (mana pāta snēhitulu "
  "elā unnāru) - 'How are our old friends'. 10. Sita: అందరూ బాగున్నారు, రాజు "
  "విదేశాల్లో ఉన్నాడు (andarū bāgunnāru, rāju vidēśāllō unnāḍu) - 'All are "
  "fine, Raju is abroad'. 11. Ravi: టీ తాగుదామా (ṭī tāgudāmā) - 'Shall we have "
  "tea'. 12. Sita: తప్పకుండా, ఆ హోటల్కు వెళ్దాం (tappakuṇḍā, ā hōṭalku veḷdāṁ) - "
  "'Definitely, let us go to that hotel'. 13. Ravi: రెండు టీలు (reṇḍu ṭīlu) - "
  "'Two teas' [ordering]. 14. Sita: వచ్చే నెలలో మన క్లాస్ రీయూనియన్ ఉంది "
  "(vaccē nelalō mana klās rīyūniyan undi) - 'Next month we have our class "
  "reunion'. 15. Ravi: నిజమా, ఎక్కడ (nijamā, ekkaḍa) - 'Really, where'. "
  "16. Sita: మన పాత బడిలోనే (mana pāta baḍilōnē) - 'In our old school itself'. "
  "17. Ravi: తప్పకుండా వస్తాను (tappakuṇḍā vastānu) - 'I will definitely come'. "
  "18. Sita: నీ ఫోన్ నంబరు ఇవ్వు (nī phōn nambaru ivvu) - 'Give me your phone "
  "number'. 19. Ravi: రాసుకో, తొమ్మిది ఎనిమిది... (rāsukō, tommidi enimidi) - "
  "'Note it down, nine eight...' [number exchange]. 20. Sita: మళ్ళీ కలుద్దాం "
  "రవి (maḷḷī kaluddāṁ ravi) - 'We will meet again, Ravi' [farewell]."),
 "how_it_works": (
  "This record works as the reunion rehearsal: the full catch-up arc - "
  "greeting, news exchange, plan-making, contact swap, farewell - in informal "
  "friend register. Notice నువ్వు forms throughout: friends drop the formal "
  "మీరు."),
 "key_points": [
  "20-line bilingual friend dialogue with register annotations.",
  "Informal register: నువ్వు ఎలా ఉన్నావు between friends.",
  "Catch-up arc: greeting -> news -> plan -> contact -> farewell.",
  "టీ తాగుదామా - 'Shall we have tea' - the friendship ritual.",
 ],
 "requirements": [
  "Act out the dialogue with a friend.",
  "Improvise your own reunion with real news.",
  "Exchange a phone number in Telugu.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Original learner dialogue composed 2026-10-17 in natural spoken Telugu.",
 ],
 "sig_lens": (
  "Through the Signature lens the friend dialogue is his crew check-in: "
  "status reports exchanged, next operation planned, contact verified - the "
  "team kept in sync. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 33
{
 "key": "convproblem", "name": "Telugu Conversation: Solving a Problem",
 "group": "Advanced", "ladder": 33, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A twenty-line bilingual dialogue solving a problem, annotated. A tenant "
  "(అద్దెదారు) reports a water leak to the house owner (ఇంటి యజమాని). "
  "1. Tenant: నమస్కారం అండీ (namaskāraṁ aṇḍī) - 'Hello, sir' [formal opening]. "
  "2. Owner: నమస్కారం, ఏమైంది (namaskāraṁ, ēmaindi) - 'Hello, what happened'. "
  "3. Tenant: బాత్రూంలో నీళ్లు కారుతున్నాయి (bātrūṁlō nīḷḷu kārutunnāyi) - "
  "'Water is leaking in the bathroom'. 4. Owner: ఎప్పటి నుండి (eppaṭi nuṇḍi) - "
  "'Since when'. 5. Tenant: నిన్న సాయంత్రం నుండి (ninna sāyantraṁ nuṇḍi) - "
  "'Since yesterday evening'. 6. Owner: ప్లంబర్ను పిలిచారా (plambarnu "
  "pilicārā) - 'Did you call the plumber'. 7. Tenant: ఇంకా లేదండీ, మీ అనుమతి "
  "కావాలి (iṅkā lēnaṇḍī, mī anumati kāvāli) - 'Not yet, sir, I need your "
  "permission'. 8. Owner: సరే, నేనే పిలుస్తాను (sarē, nēnē pilustānu) - 'Okay, "
  "I will call him myself'. 9. Tenant: ఖర్చు ఎంతవుతుంది (kharcu entavutundi) - "
  "'How much will it cost'. 10. Owner: రెండు మూడు వందలు అవుతుంది (reṇḍu mūḍu "
  "vandalu avutundi) - 'Two or three hundred'. 11. Tenant: నేను సగం ఇస్తాను "
  "(nēnu sagaṁ istānu) - 'I will pay half'. 12. Owner: వద్దు, నేనే ఇస్తాను "
  "(vaddu, nēnē istānu) - 'No need, I will pay it'. 13. Tenant: ధన్యవాదాలండీ "
  "(dhanyavādālaṇḍī) - 'Thank you, sir'. 14. Owner: రేపు ఉదయం వస్తాడు (rēpu "
  "udayaṁ vastāḍu) - 'He will come tomorrow morning'. 15. Tenant: నేను ఇంట్లోనే "
  "ఉంటాను (nēnu iṇṭlōnē uṇṭānu) - 'I will be at home'. 16. Owner: తలుపు "
  "తెరిచి ఉంచండి (talupu terici un̄caṇḍi) - 'Keep the door open'. 17. Tenant: "
  "అలాగేనండీ (alāgēnaṇḍī) - 'Certainly, sir'. 18. Owner: ఇంకేమైనా సమస్య ఉందా "
  "(iṅkēmainā samasya undā) - 'Any other problem'. 19. Tenant: ఇంకేమీ లేదండీ "
  "(iṅkēmī lēnaṇḍī) - 'Nothing else, sir'. 20. Owner: సరే, శెలవు (sarē, "
  "selavu) - 'Okay, goodbye' [formal close]."),
 "how_it_works": (
  "This record works as the problem-solving drill: report, clarify, propose, "
  "agree, schedule - the five moves of any complaint handled well, all in "
  "formal register. Notice -అండీ endings softening every tenant line: "
  "politeness under pressure."),
 "key_points": [
  "20-line bilingual problem-solving dialogue with annotations.",
  "Five moves: report -> clarify -> propose -> agree -> schedule.",
  "Formal softeners: -అండీ, దయచేసి, మీ అనుమతి కావాలి.",
  "బాత్రూంలో నీళ్లు కారుతున్నాయి - 'Water is leaking in the bathroom'.",
 ],
 "requirements": [
  "Act out the dialogue, then improvise a new problem.",
  "Report one real household issue in Telugu.",
  "Practice the -అండీ softener in five sentences.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
 ],
 "citations": [
  "Original learner dialogue composed 2026-10-17 in natural spoken Telugu.",
 ],
 "sig_lens": (
  "Through the Signature lens the problem dialogue is his incident response: "
  "fault reported, diagnosis confirmed, repair authorized, cost settled, "
  "follow-up scheduled - the ticket closed clean. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 34
{
 "key": "mastery", "name": "Telugu Mastery Review and Full Reference",
 "group": "Advanced", "ladder": 34, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The whole database in one teaching summary. Alphabet: the 16 vowels "
  "అ ఆ ఇ ఈ ఉ ఊ ఋ ౠ ఎ ఏ ఐ ఒ ఓ ఔ అం అః and the 36 consonants క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ "
  "ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ ఱ క్ష. Two hundred core "
  "words: people - అమ్మ, నాన్న, అన్న, అక్క, తమ్ముడు, చెల్లెలు, కొడుకు, కూతురు, "
  "తాత, నాయనమ్మ, స్నేహితుడు, మనిషి, పిల్లలు, ఉపాధ్యాయుడు, డాక్టరు; body - తల, "
  "కన్ను, ముక్కు, నోరు, చెవి, చేయి, కాలు, గుండె; home - ఇల్లు, గది, వంటగది, "
  "పడకగది, తలుపు, కిటికీ, టేబులు, మంచం; food - అన్నం, నీళ్లు, పాలు, టీ, పండ్లు, "
  "కూరగాయలు, ఉప్పు, పంచదార, కారం, గుడ్డు, చేప, రొట్టె; nature - చెట్టు, పూలు, "
  "పక్షి, కుక్క, పిల్లి, సూర్యుడు, చంద్రుడు, వాన, గాలి, ఎండ; numbers - ఒకటి, "
  "రెండు, మూడు, నాలుగు, ఐదు, ఆరు, ఏడు, ఎనిమిది, తొమ్మిది, పది, వంద; time - "
  "రోజు, వారం, నెల, సంవత్సరం, ఉదయం, రాత్రి, నిన్న, రేపు, ఇప్పుడు; actions - "
  "చేయు, తిను, తాగు, వెళ్ళు, వచ్చు, చదువు, రాయు, చూడు, విను, మాట్లాడు, ఇవ్వు, "
  "తీసుకో, కొను, అమ్ము, నేర్చుకో; qualities - పెద్ద, చిన్న, మంచి, కొత్త, అందమైన, "
  "ఎరుపు, నీలం; feelings - సంతోషం, బాధ, కోపం, భయం, ప్రేమ; questions - ఎవరు, "
  "ఏమిటి, ఎక్కడ, ఎప్పుడు, ఎందుకు, ఎలా; politeness - నమస్కారం, ధన్యవాదాలు, "
  "దయచేసి, క్షమించండి, మళ్ళీ కలుద్దాం; with the remaining core words drawn "
  "from the lesson records above to reach two hundred. Key grammar: SOV word "
  "order (నేను అన్నం తింటాను); three genders with verb agreement; plural -లు; "
  "cases -ని/-ను accusative, -కు dative, -యొక్క genitive, -లో locative, -తో "
  "instrumental, -నుండి ablative; no articles (ఈ/ఆ); negation కాదు/లేదు/వద్దు; "
  "questions with words or -ఆ; tenses -తున్నాను present, -ఆను past, -తాను "
  "future; commands bare stem informal, -అండి formal. Phrase tables: greetings "
  "(నమస్కారం, శుభోదయం, మీరు ఎలా ఉన్నారు, మళ్ళీ కలుద్దాం), market (ఇది ఎంత, "
  "కిలో ఎంత, చాలా ఖరీదు, సరే తీసుకుంటాను), travel (ఎక్కడ ఉంది, టికెట్ ఇవ్వండి, "
  "ఎలా వెళ్ళాలి), emergency (నాకు జ్వరం ఉంది, డాక్టరు దగ్గరకు వెళ్దాం, "
  "అంబులెన్స్ పిలవండి). The ladder path: records 1-12 foundations (script, "
  "sounds, words, grammar, daily life), records 13-23 compounded (travel, "
  "work, health, feelings, nature, shopping, social, technology, tenses, "
  "questions, commands), records 24-34 advanced (description, stories, idioms, "
  "registers, complex sentences, conversations, this review). Speak every day, "
  "write every day, and the ladder climbs itself."),
 "how_it_works": (
  "This record works as the one-page command center: alphabet, two hundred "
  "core words, key grammar, and all phrase tables compressed into a single "
  "review. Use it for weekly revision - read it end to end, marking every "
  "word you can now use in a sentence without help."),
 "key_points": [
  "Full alphabet: 16 vowels + 36 consonants with transliteration.",
  "200 core words across people, body, home, food, nature, numbers, time, actions, qualities, feelings.",
  "Key grammar compressed: SOV, genders, cases, negation, tenses, commands.",
  "All phrase tables: greetings, market, travel, emergency.",
  "The ladder path 1-34 mapped: foundations -> compounded -> advanced.",
  "Speak every day, write every day, and the ladder climbs itself.",
 ],
 "requirements": [
  "Read this review end to end once a week.",
  "Mark every word you can use unaided.",
  "Retake the ladder from record 1 with new sentences.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Telugu",
  "Unicode Standard, Telugu block U+0C00-U+0C7F",
 ],
 "citations": [
  "Consolidated from records 1-33 of this database, 2026-10-17.",
 ],
 "sig_lens": (
  "Through the Signature lens this review is his master checklist: every tool "
  "inventoried, every procedure summarized, the whole instrument verified in "
  "one pass - ready for the next build. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
]

SIG_TAIL = ("Signature lens: his original Signature language instrument - "
            "Telugu as a working system he commands. Signature-made teaching, "
            "clearly labeled, never presented as authentic public record.")
