#!/usr/bin/env python3
"""34 ladder-ordered record seeds for The Gujarati to English Database.

Follows the shared per-language template (language-template.md) EXACTLY:
records 1-34 in order, ladder_rank 1-10 non-decreasing, ladder_tier
foundations -> compounded -> advanced. Every record carries Gujarati content
in the Gujarati script plus transliteration plus English translation plus
example sentences. All Gujarati is real, fact-checked 2026-10-17
(ISO 639-1 gu / ISO 639-3 guj; Unicode Gujarati block U+0A80-U+0AFF).

Screened 2026-10-17: nothing hate-adjacent, profane, or inappropriate;
no religious talk; no military/defense-neutralization content. No website
references. No Facebook.
"""

ENTRIES = [
# ================================================================== 1
{
 "key": "overview", "name": "Gujarati Language Overview",
 "group": "Foundations", "ladder": 1, "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Gujarati (ગુજરાતી, gujarātī) is an Indo-Aryan language of the Indo-European family, "
  "whose own name for itself is ગુજરાતી. About 62 million people speak it as a first "
  "language and roughly 70 million use it in total, making it one of the most-spoken "
  "languages of India and the world. Its ISO codes are ISO 639-1 'gu' and ISO 639-3 'guj'. "
  "Gujarati is written in the Gujarati script (ગુજરાતી લિપિ), reads left to right, and "
  "follows subject-object-verb word order. It is the official language of the Indian state "
  "of Gujarat and of the union territories of Dadra and Nagar Haveli and Daman and Diu, and "
  "it is a scheduled language of the Constitution of India. Large Gujarati-speaking "
  "communities live in the United Kingdom, the United States, Canada, Kenya, Tanzania, "
  "Uganda, South Africa, Pakistan, Fiji, Mauritius, Australia and New Zealand. The language "
  "descends from Shauraseni Prakrit through Gurjara Apabhramsha; the 12th-century scholar "
  "Hemachandra's grammar documents its early form, and its literature runs from Jain monks "
  "through Narsinh Mehta (15th century) and Premanand Bhatt to the modern era. Its closest "
  "large relatives are Hindi, Marathi and Punjabi. Five sentences you can say at once: "
  "હું ગુજરાતી બોલું છું (huṁ gujarātī boluṁ chuṁ) - 'I speak Gujarati'; કેમ છો? (kem cho?) - "
  "'How are you?'; આભાર (ābhār) - 'Thank you'; મારું નામ મીરા છે (māruṁ nām mīrā che) - "
  "'My name is Mira'; આવજો (āvjo) - 'Goodbye - come again'."),
 "how_it_works": (
  "This record works as the front door of the whole database: it names the language in "
  "English and in the Gujarati script, places it in its language family, gives the speaker "
  "numbers, lists where it is spoken and its official status, traces its history, and closes "
  "with five translated example sentences you can say at once. Every later record builds on "
  "these facts, so read this one first."),
 "key_points": [
  "Gujarati (ગુજરાતી, gujarātī): Indo-European > Indo-Iranian > Indo-Aryan; ISO 639-1 gu, ISO 639-3 guj.",
  "About 62 million native speakers; about 70 million total speakers.",
  "Written in the Gujarati script, read left to right; basic word order is subject-object-verb.",
  "Official language of Gujarat state and of Dadra and Nagar Haveli and Daman and Diu; a scheduled language of India.",
  "Descends from Shauraseni Prakrit through Gurjara Apabhramsha; documented by Hemachandra in the 12th century.",
  "Major literary figures: Jain scholars, Narsinh Mehta, Premanand Bhatt, Dayaram.",
  "Large diaspora communities in the UK, USA, Canada, East Africa, South Africa, Pakistan, Fiji and Mauritius.",
  "હું ગુજરાતી બોલું છું (huṁ gujarātī boluṁ chuṁ) - 'I speak Gujarati' shows SOV order in action.",
 ],
 "requirements": [
  "No prior Gujarati needed - this is the starting point of the ladder.",
  "Read the Gujarati words aloud using the romanization beside them.",
  "Remember: ગુજરાતી (gujarātī) is the language's own name for itself.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'gu' for Gujarati",
  "ISO 639-3:2007 code 'guj' for Gujarati",
  "Unicode Standard, Gujarati block U+0A80-U+0AFF",
 ],
 "citations": [
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003.",
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
  "Masica, Colin P. The Indo-Aryan Languages. Cambridge University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens this overview is re-taught as his original Signature "
  "language instrument: Gujarati as a working system he commands, where every speaker "
  "count measures the instrument's reach and every dialect is another string he can "
  "play. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 2
{
 "key": "writing", "name": "Gujarati Writing System: The Gujarati Script",
 "group": "Foundations", "ladder": 2, "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Gujarati is written in the Gujarati script (ગુજરાતી લિપિ, gujarātī lipi), an abugida "
  "derived from Devanagari but with its own letterforms and with no headline stroke "
  "(shirorekha) across the top of words, which gives written Gujarati its open, rounded "
  "look. It reads left to right. Every consonant carries an inherent 'a' vowel unless "
  "marked otherwise. The 13 independent vowels are: અ (a), આ (ā), ઇ (i), ઈ (ī), ઉ (u), "
  "ઊ (ū), ઋ (ṛ, rare), એ (e), ઐ (ai), ઓ (o), ઔ (au), અં (aṁ), અઃ (aḥ). The 34 consonants "
  "are: ક (ka), ખ (kha), ગ (ga), ઘ (gha), ઙ (ṅa), ચ (ca), છ (cha), જ (ja), ઝ (jha), ઞ "
  "(ña), ટ (ṭa), ઠ (ṭha), ડ (ḍa), ઢ (ḍha), ણ (ṇa), ત (ta), થ (tha), દ (da), ધ (dha), ન "
  "(na), પ (pa), ફ (pha), બ (ba), ભ (bha), મ (ma), ય (ya), ર (ra), લ (la), વ (va), ળ "
  "(ḷa - the retroflex 'l', a signature Gujarati sound), શ (śa), ષ (ṣa), સ (sa), હ (ha). "
  "Vowel signs (matras) attach to consonants - ા િ ી ુ ૂ ૃ ે ૈ ો ૌ ં ઃ - for example ક + "
  "ી = કી (kī). Special marks: anusvara ં (nasalizes, as in હં huṁ), visarga ઃ (a breathy "
  "h, as in દુઃખ duḥkha 'sorrow'), chandrabindu ઁ (nasal vowel, as in ચાંદ cā̃d 'moon'). "
  "Conjuncts join consonants: ક્ષ (kṣa), જ્ઞ (jña), ત્ર (tra), શ્ર (śra). The danda । ends "
  "a sentence in traditional writing; modern Gujarati often uses the period instead. "
  "Gujarati digits are ૦ ૧ ૨ ૩ ૪ ૫ ૬ ૭ ૮ ૯ (0-9). Example words: નમસ્તે (namaste) - "
  "'hello'; પાણી (pāṇī) - 'water'; પુસ્તક (pustak) - 'book'; ઘર (ghar) - 'house'; શાળા "
  "(śāḷā) - 'school'. Full sentence: હું ગુજરાતી લખું છું (huṁ gujarātī lakhuṁ chuṁ) - "
  "'I write Gujarati'."),
 "how_it_works": (
  "This record teaches the script the way it is used: the vowel list and the consonant "
  "list with romanization, the vowel-sign system that turns ક into કા કિ કી કુ, the special "
  "marks, conjuncts, the sentence-ending danda, and the digits - each with a translated "
  "example word. Trace each letter, say its sound, then read the five example words aloud. "
  "Notice the missing headline: unlike Devanagari, Gujarati letters stand free."),
 "key_points": [
  "The Gujarati script is an abugida derived from Devanagari, with no headline stroke.",
  "13 independent vowels: અ આ ઇ ઈ ઉ ઊ ઋ એ ઐ ઓ ઔ અં અઃ.",
  "34 consonants including ળ (ḷa), the retroflex l that marks Gujarati.",
  "Vowel signs (matras) attach to consonants: ક → કા, કિ, કી, કુ, કૂ, કે, કૈ, કો, કૌ.",
  "Anusvara ં, visarga ઃ and chandrabindu ઁ modify sounds.",
  "Conjuncts: ક્ષ (kṣa), જ્ઞ (jña), ત્ર (tra), શ્ર (śra).",
  "The danda । ends sentences in traditional text; digits are ૦૧૨૩૪૫૬૭૮૯.",
  "હું ગુજરાતી લખું છું (huṁ gujarātī lakhuṁ chuṁ) - 'I write Gujarati'.",
 ],
 "requirements": [
  "Say each letter's romanized sound aloud as you read it.",
  "Practice writing: vowels first, then the five consonant groups, then ળ શ ષ સ હ.",
  "Remember that ક is 'ka', not 'k' - the vowel sign removes or changes the 'a'.",
 ],
 "standards": [
  "Unicode Standard, Gujarati block U+0A80-U+0AFF",
  "ISO 15919:2001 transliteration of Indic scripts",
 ],
 "citations": [
  "Daniels, Peter T. & Bright, William (eds.) The World's Writing Systems. Oxford University Press; 1996. Gujarati chapter.",
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Script chapter.",
 ],
 "sig_lens": (
  "Through the Signature lens the script becomes his original Signature writing "
  "instrument: each letter a struck key with no headline to fence it in, each matra a "
  "modifier on the key, the danda the full stop of a finished Signature line. "
  "Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 3
{
 "key": "phonology", "name": "Gujarati Pronunciation and Phonology",
 "group": "Foundations", "ladder": 3, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Gujarati has 8 vowel phonemes: અ (a, like 'u' in 'but'), આ (ā, like 'a' in 'father'), "
  "ઇ/ઈ (i/ī, like 'i' in 'bit' and 'ee' in 'beet'), ઉ/ઊ (u/ū, like 'oo' in 'put' and "
  "'boot'), એ (e, like 'a' in 'late'), ઓ (o, like 'o' in 'note'); the diphthongs ઐ (ai) "
  "and ઔ (au) also occur, and ઋ (ṛ) survives in learned words. Vowels can be nasalized "
  "(ચાંદ cā̃d 'moon'). The consonant system keeps the classic five articulation rows: "
  "velar ક ખ ગ ઘ ઙ; palatal ચ છ જ ઝ ઞ; retroflex ટ ઠ ડ ઢ ણ; dental ત થ દ ધ ન; labial પ ફ "
  "બ ભ મ - plus ય ર લ વ, the Gujarati special ળ (ḷa, a retroflex 'l' made with the tongue "
  "curled back - no English equivalent), the sibilants શ ષ સ, and હ. Aspirated pairs "
  "matter: ક (ka) vs ખ (kha), ગ (ga) vs ઘ (gha), ચ (ca) vs છ (cha). Stress usually falls "
  "on the first syllable; questions rise in intonation at the end. Spoken examples: "
  "પાણી (pāṇī) - 'water'; ઘર (ghar) - 'house'; છોકરો (chokro) - 'boy'; છોકરી (chokrī) - "
  "'girl'; બાળક (bāḷak) - 'child' (hear the ળ); રોટલી (roṭlī) - 'bread'; દૂધ (dūdh) - "
  "'milk'; સૂરજ (sūraj) - 'sun'; ચાંદ (cā̃d) - 'moon' (nasal ā); ફૂલ (phūl) - 'flower'; "
  "ઝાડ (jhāḍ) - 'tree'; કૂતરો (kūtro) - 'dog'. Full sentence: સૂરજ પૂર્વમાં ઊગે છે (sūraj "
  "pūrvamā̃ ūge che) - 'The sun rises in the east'."),
 "how_it_works": (
  "This record trains your ear and mouth: the vowel chart with English approximations, "
  "the five consonant rows with aspirated pairs, the special Gujarati sounds (ળ, nasal "
  "vowels), stress and question intonation, and twelve spoken example words with "
  "translations. Say each word slowly, then at normal speed, then inside the full "
  "sentence."),
 "key_points": [
  "8 vowel phonemes: a, ā, i, ī, u, ū, e, o; plus diphthongs ai, au and nasalized vowels.",
  "Five consonant rows: velar, palatal, retroflex, dental, labial - each with aspirated pairs.",
  "ળ (ḷa) is the signature Gujarati sound: a retroflex 'l' with the tongue curled back.",
  "ખ vs ક, ઘ vs ગ, છ vs ચ: aspiration changes meaning - practice the pairs.",
  "Stress falls on the first syllable; questions rise in intonation.",
  "ચાંદ (cā̃d) shows a nasalized vowel; બાળક (bāḷak) shows ળ in action.",
  "પાણી (pāṇī) - 'water'; ઘર (ghar) - 'house'; સૂરજ (sūraj) - 'sun'.",
  "સૂરજ પૂર્વમાં ઊગે છે (sūraj pūrvamā̃ ūge che) - 'The sun rises in the east'.",
 ],
 "requirements": [
  "Practice the aspirated pairs aloud: ક/ખ, ગ/ઘ, ચ/છ, ટ/ઠ, ત/થ, પ/ફ.",
  "Curl the tongue back for ળ - say બાળક (bāḷak) ten times.",
  "Read the twelve example words into the full sentence at the end.",
 ],
 "standards": [
  "IPA transcription conventions for Indo-Aryan languages",
  "ISO 15919:2001 transliteration of Indic scripts",
 ],
 "citations": [
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003. Phonology section.",
  "Pandit, Prabodh B. Historical Phonology of Gujarati Vowels. (Gujarati phonology studies).",
 ],
 "sig_lens": (
  "Through the Signature lens pronunciation is his original Signature voice training: "
  "each aspirated pair a breath-control drill, the ળ a tongue-placement instrument "
  "setting, nasal vowels a resonance control. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 4
{
 "key": "nouns1", "name": "Core Gujarati Nouns I",
 "group": "Foundations", "ladder": 4, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Twenty-five essential Gujarati nouns - people, places and things - each with its "
  "gender (m = masculine, f = feminine, n = neuter; Gujarati keeps all three, unlike Hindi) "
  "and one full example sentence with translation: 1. માણસ (māṇas, m) - person: આ માણસ "
  "મારો મિત્ર છે (ā māṇas māro mitra che) - 'This man is my friend'. 2. સ્ત્રી (strī, f) - "
  "woman: તે સ્ત્રી શિક્ષક છે (te strī śikṣak che) - 'That woman is a teacher'. 3. છોકરો "
  "(chokro, m) - boy: છોકરો રમે છે (chokro rame che) - 'The boy is playing'. 4. છોકરી "
  "(chokrī, f) - girl: છોકરી હસે છે (chokrī hase che) - 'The girl is laughing'. 5. બાળક "
  "(bāḷak, n) - child: બાળક સૂએ છે (bāḷak sūe che) - 'The child is sleeping'. 6. ઘર (ghar, "
  "n) - house: મારું ઘર મોટું છે (māruṁ ghar moṭuṁ che) - 'My house is big'. 7. પાણી (pāṇī, "
  "n) - water: પાણી ઠંડું છે (pāṇī ṭhaṇḍuṁ che) - 'The water is cold'. 8. ખોરાક (khorāk, m) - "
  "food: ખોરાક તૈયાર છે (khorāk taiyār che) - 'The food is ready'. 9. રોટલી (roṭlī, f) - "
  "bread: રોટલી ગરમ છે (roṭlī garam che) - 'The bread is hot'. 10. શાક (śāk, n) - vegetable "
  "curry: શાક સ્વાદિષ્ટ છે (śāk svādiṣṭ che) - 'The curry is tasty'. 11. દૂધ (dūdh, n) - milk: "
  "દૂધ સફેદ છે (dūdh saphed che) - 'Milk is white'. 12. ચા (cā, f) - tea: ચા મીઠી છે (cā "
  "mīṭhī che) - 'The tea is sweet'. 13. પુસ્તક (pustak, n) - book: આ પુસ્તક નવું છે (ā "
  "pustak navuṁ che) - 'This book is new'. 14. કલમ (kalam, f) - pen: કલમ ટેબલ પર છે "
  "(kalam ṭebal par che) - 'The pen is on the table'. 15. શાળા (śāḷā, f) - school: શાળા "
  "નજીક છે (śāḷā najīk che) - 'The school is near'. 16. શિક્ષક (śikṣak, m) - teacher: "
  "શિક્ષક દયાળુ છે (śikṣak dayāḷu che) - 'The teacher is kind'. 17. ડૉક્ટર (ḍŏkṭar, m/f) - "
  "doctor: ડૉક્ટર આવ્યા છે (ḍŏkṭar āvyā che) - 'The doctor has come'. 18. બજાર (bajār, n) - "
  "market: બજાર દૂર છે (bajār dūr che) - 'The market is far'. 19. રસ્તો (rasto, m) - road: "
  "રસ્તો લાંબો છે (rasto lāṁbo che) - 'The road is long'. 20. ગાડી (gāḍī, f) - car: ગાડી "
  "ઝડપી છે (gāḍī jhaḍpī che) - 'The car is fast'. 21. ફોન (phon, m) - phone: ફોન વાગે છે "
  "(phon vāge che) - 'The phone is ringing'. 22. પૈસા (paisā, m pl) - money: પૈસા જરૂરી "
  "છે (paisā jarūrī che) - 'Money is necessary'. 23. સમય (samay, m) - time: સમય કિંમતી છે "
  "(samay kiṁmatī che) - 'Time is precious'. 24. દિવસ (divas, m) - day: આજનો દિવસ સારો છે "
  "(ājno divas sāro che) - 'Today is a good day'. 25. રાત (rāt, f) - night: રાત શાંત છે "
  "(rāt śāṁt che) - 'The night is quiet'."),
 "how_it_works": (
  "This record builds your first working vocabulary: 25 nouns covering people, food, home, "
  "school, travel and time. Each entry gives the Gujarati word, its romanization, its "
  "English meaning, its gender, and one full sentence showing it in use. Learn the gender "
  "with the word - it controls adjective and verb endings later. Cover the English column "
  "and test yourself both ways."),
 "key_points": [
  "25 essential nouns, each with gender, romanization, and a full translated sentence.",
  "Gujarati keeps three genders: masculine (છોકરો), feminine (છોકરી), neuter (બાળક).",
  "માણસ (māṇas) - person; ઘર (ghar) - house; પાણી (pāṇī) - water.",
  "પુસ્તક (pustak) - book; શાળા (śāḷā) - school; શિક્ષક (śikṣak) - teacher.",
  "બજાર (bajār) - market; રસ્તો (rasto) - road; ગાડી (gāḍī) - car.",
  "પૈસા (paisā) - money; સમય (samay) - time; દિવસ (divas) - day; રાત (rāt) - night.",
  "આ માણસ મારો મિત્ર છે (ā māṇas māro mitra che) - 'This man is my friend'.",
  "મારું ઘર મોટું છે (māruṁ ghar moṭuṁ che) - 'My house is big'.",
 ],
 "requirements": [
  "Memorize each noun WITH its gender - say 'છોકરો masculine' as one unit.",
  "Say every example sentence aloud, then say it again from the English alone.",
  "Write each noun once in the Gujarati script from memory.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Indic scripts",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Vocabulary sections.",
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens these nouns are his original Signature naming instruments: "
  "each word a label he stamps onto the world, gender a sorting key in his system, every "
  "sentence a first Signature line spoken in Gujarati. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 5
{
 "key": "verbs1", "name": "Core Gujarati Verbs I",
 "group": "Foundations", "ladder": 5, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Twenty-five essential Gujarati verbs, each in dictionary form (-વું) with one full "
  "present-tense example sentence with translation. Gujarati present tense: stem + "
  "ું/ે/ે/ીએ/ો/ે + છું/છે/છે/છીએ/છો/છે. 1. કરવું (karvuṁ) - to do: હું કામ કરું છું (huṁ kām "
  "karuṁ chuṁ) - 'I do work'. 2. હોવું (hovuṁ) - to be: તે ખુશ છે (te khuś che) - 'He is "
  "happy'. 3. જવું (javuṁ) - to go: હું શાળાએ જાઉં છું (huṁ śāḷāe jāuṁ chuṁ) - 'I go to "
  "school'. 4. આવવું (āvvū) - to come: તે અહીં આવે છે (te ahī̃ āve che) - 'He comes here'. "
  "5. ખાવું (khāvuṁ) - to eat: અમે ભાત ખાઈએ છીએ (ame bhāt khāīe chīe) - 'We eat rice'. 6. "
  "પીવું (pīvuṁ) - to drink: હું પાણી પીઉં છું (huṁ pāṇī pīuṁ chuṁ) - 'I drink water'. 7. "
  "બોલવું (bolvuṁ) - to speak: તે ગુજરાતી બોલે છે (te gujarātī bole che) - 'She speaks "
  "Gujarati'. 8. વાંચવું (vā̃cvuṁ) - to read: હું પુસ્તક વાંચું છું (huṁ pustak vā̃cuṁ chuṁ) - "
  "'I read a book'. 9. લખવું (lakhvuṁ) - to write: તે પત્ર લખે છે (te patra lakhe che) - "
  "'He writes a letter'. 10. જોવું (jovuṁ) - to see: હું તને જોઉં છું (huṁ tane jouṁ chuṁ) - "
  "'I see you'. 11. સાંભળવું (sā̃bhaḷvuṁ) - to listen: તે ગીત સાંભળે છે (te gīt sā̃bhaḷe "
  "che) - 'She listens to a song'. 12. સૂવું (sūvuṁ) - to sleep: બાળક સૂએ છે (bāḷak sūe "
  "che) - 'The child sleeps'. 13. ઊઠવું (ūṭhvuṁ) - to get up: હું વહેલો ઊઠું છું (huṁ vahelo "
  "ūṭhuṁ chuṁ) - 'I get up early'. 14. બેસવું (besvuṁ) - to sit: તે ખુરશી પર બેસે છે (te "
  "khurśī par bese che) - 'He sits on the chair'. 15. ચાલવું (cālvuṁ) - to walk: અમે બગીચામાં "
  "ચાલીએ છીએ (ame bagīcāmā̃ cālīe chīe) - 'We walk in the garden'. 16. દોડવું (doḍvuṁ) - to "
  "run: છોકરો ઝડપથી દોડે છે (chokro jhaḍapthī doḍe che) - 'The boy runs fast'. 17. આપવું "
  "(āpvuṁ) - to give: તે મને પુસ્તક આપે છે (te mane pustak āpe che) - 'He gives me a book'. "
  "18. લેવું (levuṁ) - to take: હું કલમ લઉં છું (huṁ kalam lauṁ chuṁ) - 'I take the pen'. 19. "
  "ખરીદવું (kharīdvuṁ) - to buy: તે શાક ખરીદે છે (te śāk kharīde che) - 'She buys vegetables'. "
  "20. વેચવું (vecvuṁ) - to sell: તે ફળ વેચે છે (te phaḷ vece che) - 'He sells fruit'. 21. "
  "બનાવવું (banāvuṁ) - to make: તે ચા બનાવે છે (te cā banāve che) - 'She makes tea'. 22. "
  "શીખવું (śīkhvuṁ) - to learn: હું ગુજરાતી શીખું છું (huṁ gujarātī śīkhuṁ chuṁ) - 'I learn "
  "Gujarati'. 23. શીખવવું (śīkhavvuṁ) - to teach: શિક્ષક "
  "ગણિત શીખવે છે (śikṣak gaṇit śīkhave che) - 'The teacher teaches math'. 24. સમજવું "
  "(samajvuṁ) - to understand: હું સમજું છું (huṁ samjuṁ chuṁ) - 'I understand'. 25. કામ "
  "કરવું (kām karvuṁ) - to work: તે ઑફિસમાં કામ કરે છે (te ŏphisamā̃ kām kare che) - 'He "
  "works in an office'."),
 "how_it_works": (
  "This record gives you the engine of every sentence: 25 verbs in dictionary form with a "
  "present-tense example each. Gujarati dictionary forms end in -વું; the present tense "
  "adds person endings plus છું/છે/છો/છીએ. Learn the pattern from કરવું: હું કરું છું, તું "
  "કરે છે, તે કરે છે, અમે કરીએ છીએ, તમે કરો છો, તેઓ કરે છે - then swap in any new stem."),
 "key_points": [
  "25 essential verbs in -વું dictionary form, each with a full present-tense sentence.",
  "Present pattern: stem + ું/ે/ી/ીએ/ો + છું/છે/છીએ/છો: હું કરું છું, તે કરે છે.",
  "કરવું (karvuṁ) - to do; હોવું (hovuṁ) - to be; જવું (javuṁ) - to go; આવવું (āvvū) - to come.",
  "ખાવું (khāvuṁ) - to eat; પીવું (pīvuṁ) - to drink; બોલવું (bolvuṁ) - to speak.",
  "વાંચવું (vā̃cvuṁ) - to read; લખવું (lakhvuṁ) - to write; જોવું (jovuṁ) - to see.",
  "આપવું (āpvuṁ) - to give; લેવું (levuṁ) - to take; ખરીદવું (kharīdvuṁ) - to buy.",
  "શીખવું (śīkhvuṁ) - to learn; શીખવવું (śīkhavvuṁ) - to teach; સમજવું (samajvuṁ) - to understand.",
  "હું પાણી પીઉં છું (huṁ pāṇī pīuṁ chuṁ) - 'I drink water'.",
 ],
 "requirements": [
  "Conjugate કરવું fully aloud before learning any other verb.",
  "Say each example sentence, then replace હું with તમે and re-say it.",
  "Write the five most-used verbs - કરવું, હોવું, જવું, ખાવું, બોલવું - from memory.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Indic scripts",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Verb chapters.",
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003. Morphology section.",
 ],
 "sig_lens": (
  "Through the Signature lens these verbs are his original Signature action instruments: "
  "twenty-five engines of doing, each stem a lever he pulls, each ending a gear that "
  "fits the speaker. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 6
{
 "key": "adjadv", "name": "Gujarati Adjectives and Adverbs",
 "group": "Foundations", "ladder": 6, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Gujarati adjectives agree with the noun: -ો (masculine), -ી (feminine), -ું (neuter) - "
  "સારો છોકરો (sāro chokro, 'good boy'), સારી છોકરી (sārī chokrī, 'good girl'), સારું બાળક "
  "(sāruṁ bāḷak, 'good child'). Twenty-five adjectives with sentences: 1. સારો (sāro) - "
  "good: તે સારો માણસ છે (te sāro māṇas che) - 'He is a good man'. 2. ખરાબ (kharāb) - bad: "
  "આ ખરાબ સમાચાર છે (ā kharāb samācār che) - 'This is bad news'. 3. મોટો (moṭo) - big: ઘર "
  "મોટું છે (ghar moṭuṁ che) - 'The house is big'. 4. નાનો (nāno) - small: આ નાનું ગામ છે "
  "(ā nānuṁ gām che) - 'This is a small village'. 5. નવો (navo) - new: મારી પાસે નવી ગાડી "
  "છે (mārī pāse navī gāḍī che) - 'I have a new car'. 6. જૂનો (jūno) - old: આ જૂનું મકાન "
  "છે (ā jūnuṁ makān che) - 'This is an old building'. 7. લાંબો (lāṁbo) - long/tall: રસ્તો "
  "લાંબો છે (rasto lāṁbo che) - 'The road is long'. 8. ટૂંકો (ṭūṁko) - short: દિવસ ટૂંકો છે "
  "(divas ṭūṁko che) - 'The day is short'. 9. ગરમ (garam) - hot: ચા ગરમ છે (cā garam che) - "
  "'The tea is hot'. 10. ઠંડો (ṭhaṇḍo) - cold: પાણી ઠંડું છે (pāṇī ṭhaṇḍuṁ che) - 'The water "
  "is cold'. 11. મીઠો (mīṭho) - sweet: કેરી મીઠી છે (kerī mīṭhī che) - 'The mango is sweet'. "
  "12. ખાટો (khāṭo) - sour: લીંબુ ખાટું છે (līṁbu khāṭuṁ che) - 'The lemon is sour'. 13. "
  "તીખો (tīkho) - spicy: શાક તીખું છે (śāk tīkhuṁ che) - 'The curry is spicy'. 14. સુંદર "
  "(sundar) - beautiful: બગીચો સુંદર છે (bagīco sundar che) - 'The garden is beautiful'. "
  "15. ઝડપી (jhaḍpī) - fast: ટ્રેન ઝડપી છે (ṭren jhaḍpī che) - 'The train is fast'. 16. ધીમો "
  "(dhīmo) - slow: કાચબો ધીમો છે (kācbo dhīmo che) - 'The tortoise is slow'. 17. ખુશ (khuś) - "
  "happy: હું ખુશ છું (huṁ khuś chuṁ) - 'I am happy'. 18. દુઃખી (duḥkhī) - sad: તે દુઃખી છે "
  "(te duḥkhī che) - 'She is sad'. 19. ભૂખ્યો (bhūkhyo) - hungry: હું ભૂખ્યો છું (huṁ "
  "bhūkhyo chuṁ) - 'I am hungry' (masculine speaker). 20. તરસ્યો (tarasyo) - thirsty: તે "
  "તરસી છે (te tarsī che) - 'She is thirsty'. 21. થાકેલો (thākelo) - tired: હું થાકેલો છું "
  "(huṁ thākelo chuṁ) - 'I am tired'. 22. સ્વચ્છ (svacch) - clean: ઓરડો સ્વચ્છ છે (orḍo "
  "svacch che) - 'The room is clean'. 23. ગંદો (gando) - dirty: કપડાં ગંદાં છે (kapḍā̃ "
  "gandā̃ che) - 'The clothes are dirty'. 24. ધનવાન (dhanvān) - rich: તે ધનવાન વેપારી છે "
  "(te dhanvān vepārī che) - 'He is a rich merchant'. 25. ગરીબ (garīb) - poor: તે ગરીબ "
  "ખેડૂત છે (te garīb kheḍūt che) - 'He is a poor farmer'. Fifteen adverbs with sentences: "
  "ખૂબ (khūb) - very: તે ખૂબ સારો છે (te khūb sāro che) - 'He is very good'; ધીમે ધીમે "
  "(dhīme dhīme) - slowly: ધીમે ધીમે ચાલો (dhīme dhīme cālo) - 'Walk slowly'; ઝડપથી (jhaḍapthī) "
  "- quickly: ઝડપથી આવો (jhaḍapthī āvo) - 'Come quickly'; હંમેશા (hameśā) - always: તે "
  "હંમેશા સમયસર આવે છે (te hameśā samaysar āve che) - 'He always comes on time'; ક્યારેક "
  "(kyārek) - sometimes: હું ક્યારેક ત્યાં જાઉં છું (huṁ kyārek tyā̃ jāuṁ chuṁ) - 'I sometimes "
  "go there'; ક્યારેય નહીં (kyārey nahī̃) - never: હું ક્યારેય નહીં ભૂલું (huṁ kyārey nahī̃ "
  "bhūluṁ) - 'I will never forget'; આજે (āje) - today: આજે વરસાદ છે (āje varsād che) - "
  "'It is raining today'; કાલે (kāle) - tomorrow/yesterday: હું કાલે આવીશ (huṁ kāle āvīś) - "
  "'I will come tomorrow'; અહીં (ahī̃) - here: અહીં બેસો (ahī̃ beso) - 'Sit here'; ત્યાં "
  "(tyā̃) - there: ત્યાં જાઓ (tyā̃ jāo) - 'Go there'; અંદર (andar) - inside: અંદર આવો (andar "
  "āvo) - 'Come inside'; બહાર (bahār) - outside: બહાર જાઓ (bahār jāo) - 'Go outside'; ઉપર "
  "(upar) - up: ઉપર જુઓ (upar juo) - 'Look up'; નીચે (nīce) - down: નીચે બેસો (nīce beso) - "
  "'Sit down'; સાથે (sāthe) - together: અમે સાથે જઈશું (ame sāthe jaīśuṁ) - 'We will go "
  "together'."),
 "how_it_works": (
  "This record teaches description: adjectives that change endings with gender (-ો/-ી/-ું) "
  "and adverbs that never change. Practice each adjective in all three genders - સારો "
  "છોકરો, સારી છોકરી, સારું બાળક - until the pattern is automatic. Then add adverbs to "
  "your verb sentences: હું ઝડપથી દોડું છું (huṁ jhaḍapthī doḍuṁ chuṁ) - 'I run fast'."),
 "key_points": [
  "Adjectives agree in gender: -ો masculine, -ી feminine, -ું neuter.",
  "સારો છોકરો (sāro chokro), સારી છોકરી (sārī chokrī), સારું બાળક (sāruṁ bāḷak).",
  "Some adjectives never change: ખરાબ, ગરમ, ખુશ, ગરીબ.",
  "Adverbs never change form: ખૂબ, હંમેશા, ઝડપથી, ધીમે ધીમે.",
  "મોટો/નાનો, નવો/જૂનો, ગરમ/ઠંડો, ઝડપી/ધીમો are core opposites.",
  "કાલે (kāle) means both 'tomorrow' and 'yesterday' - context decides.",
  "તે ખૂબ સારો છે (te khūb sāro che) - 'He is very good'.",
  "અમે સાથે જઈશું (ame sāthe jaīśuṁ) - 'We will go together'.",
 ],
 "requirements": [
  "Drill every -ો adjective in all three genders aloud.",
  "Add one adverb to five verb sentences you already know.",
  "Describe three people and three things around you using new adjectives.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Indic scripts",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Adjective and adverb chapters.",
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens adjectives and adverbs are his original Signature coloring "
  "instruments: the -ો/-ી/-ું endings three brushes for three genders, adverbs the "
  "pressure on each stroke. Signature-made teaching, clearly labeled, never presented as "
  "an outside authority's text."),
},
# ================================================================== 7
{
 "key": "pronouns", "name": "Gujarati Pronouns",
 "group": "Foundations", "ladder": 7, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Gujarati pronouns with full paradigms and sentences. Personal pronouns - હું (huṁ) I: "
  "હું વિદ્યાર્થી છું (huṁ vidyārthī chuṁ) - 'I am a student'; તું (tuṁ) you (informal, close): "
  "તું ક્યાં જાય છે? (tuṁ kyā̃ jāy che?) - 'Where are you going?'; તમે (tame) you (formal/plural): "
  "તમે કેમ છો? (tame kem cho?) - 'How are you?'; તે (te) he/she (informal): તે ડૉક્ટર છે (te "
  "ḍŏkṭar che) - 'He/she is a doctor'; તેઓ (teo) they (formal/respectful): તેઓ શિક્ષકો છે "
  "(teo śikṣako che) - 'They are teachers'; અમે (ame) we: અમે મિત્રો છીએ (ame mitro chīe) - "
  "'We are friends'; આપણે (āpaṇe) we (inclusive, includes listener): આપણે જઈએ (āpaṇe jaīe) - "
  "'Let us go'. Ergative forms for past transitive: મેં (mẽ) I (did): મેં ખાધું (mẽ khādhuṁ) - "
  "'I ate'; તેણે (teṇe) he/she (did): તેણે લખ્યું (teṇe lakhyuṁ) - 'He/she wrote'. Possessives "
  "agree in gender: મારો/મારી/મારું (māro/mārī/māruṁ) my: મારો ભાઈ (māro bhāī) - 'my brother', "
  "મારી બહેન (mārī bahen) - 'my sister', મારું ઘર (māruṁ ghar) - 'my house'; તારો/તારી/તારું "
  "(tāro/tārī/tāruṁ) your (informal): તારું નામ શું છે? (tāruṁ nām śuṁ che?) - 'What is your "
  "name?'; તમારો/તમારી/તમારું (tamāro/tamārī/tamāruṁ) your (formal): તમારું કામ સારું છે "
  "(tamāruṁ kām sāruṁ che) - 'Your work is good'; તેનો/તેની/તેનું (teno/tenī/tenuṁ) his/her: "
  "તેનું પુસ્તક (tenuṁ pustak) - 'his/her book'; અમારો (amāro) our: અમારો દેશ (amāro deś) - "
  "'our country'; આપણો (āpaṇo) our (inclusive): આપણું ગામ (āpaṇuṁ gām) - 'our village'. "
  "Demonstratives: આ (ā) this: આ મારી કલમ છે (ā mārī kalam che) - 'This is my pen'; તે (te) "
  "that: તે દૂર છે (te dūr che) - 'That is far'; ઓ (o) that (far/yonder, literary): ઓ પહાડ "
  "ઊંચો છે (o pahāḍ ū̃co che) - 'That mountain is tall'. Interrogatives: કોણ (koṇ) who: કોણ "
  "આવ્યું? (koṇ āvyuṁ?) - 'Who came?'; શું (śuṁ) what: આ શું છે? (ā śuṁ che?) - 'What is this?'; "
  "કયો/કઈ/કયું (kayo/kaī/kayuṁ) which: કયું પુસ્તક? (kayuṁ pustak?) - 'Which book?'; કેટલું "
  "(keṭluṁ) how much: કેટલું દૂર? (keṭluṁ dūr?) - 'How far?'. Reflexive: પોતે (pote) self: "
  "તે પોતે આવ્યો (te pote āvyo) - 'He came himself'."),
 "how_it_works": (
  "This record maps every person-word: who is speaking, who is spoken to (તું for friends, "
  "તમે for respect), possession that changes with gender, pointing words (આ/તે), and "
  "question words. Drill: point at things and say આ... છે / તે... છે; then ask કોણ/શું/ક્યાં "
  "about each. Master અમે vs આપણે - one excludes the listener, one includes them."),
 "key_points": [
  "તું is informal (close friends, children); તમે is formal and plural - default to તમે.",
  "Possessives agree: મારો ભાઈ (m), મારી બહેન (f), મારું ઘર (n).",
  "અમે (we, exclusive) vs આપણે (we, inclusive of the listener).",
  "Past transitive uses ergative: મેં ખાધું (mẽ khādhuṁ) - 'I ate'.",
  "આ (this) / તે (that) / ઓ (that yonder); કોણ (who), શું (what), કયું (which).",
  "તમારું નામ શું છે? (tamāruṁ nām śuṁ che?) - 'What is your name?'",
  "આપણે જઈએ (āpaṇe jaīe) - 'Let us go' (includes the listener).",
  "તે પોતે આવ્યો (te pote āvyo) - 'He came himself'.",
 ],
 "requirements": [
  "Address everyone as તમે until invited to use તું.",
  "Practice possessives in all three genders with five nouns.",
  "Make ten આ/તે sentences about objects in the room.",
 ],
 "standards": [
  "ISO 15919:2001 transliteration of Indic scripts",
 ],
 "citations": [
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003. Pronoun section.",
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Pronoun chapters.",
 ],
 "sig_lens": (
  "Through the Signature lens pronouns are his original Signature pointing instruments: "
  "તું/તમે a respect dial he turns, possessives gender-gears, આ/તે twin pointers, the "
  "ergative મેં a past-action stamp. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 8
{
 "key": "numbers", "name": "Gujarati Numbers and Time",
 "group": "Foundations", "ladder": 8, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Numbers 1-10: એક (ek) 1, બે (be) 2, ત્રણ (traṇ) 3, ચાર (cār) 4, પાંચ (pā̃c) 5, છ (cha) 6, "
  "સાત (sāt) 7, આઠ (āṭh) 8, નવ (nav) 9, દસ (das) 10. 11-20: અગિયાર (agiyār) 11, બાર (bār) 12, "
  "તેર (ter) 13, ચૌદ (caud) 14, પંદર (pandar) 15, સોળ (soḷ) 16, સત્તર (sattar) 17, અઢાર "
  "(aḍhār) 18, ઓગણીસ (ogṇīs) 19, વીસ (vīs) 20. Tens: ત્રીસ (trīs) 30, ચાળીસ (cāḷīs) 40, પચાસ "
  "(pacās) 50, સાઠ (sāṭh) 60, સિત્તેર (sitter) 70, એંસી (ẽsī) 80, નેવું (nevuṁ) 90, સો (so) "
  "100, હજાર (hajār) 1000, લાખ (lākh) 100,000, કરોડ (karoḍ) 10,000,000. Digits in script: "
  "૦૧૨૩૪૫૬૭૮૯. Ordinals: પહેલો (pahelo) first, બીજો (bījo) second, ત્રીજો (trījo) third, "
  "ચોથો (cotho) fourth, પાંચમો (pā̃cmo) fifth. Sentences: મારી પાસે બે પુસ્તકો છે (mārī pāse "
  "be pustako che) - 'I have two books'; તે ત્રીજા માળે રહે છે (te trījā māḷe rahe che) - "
  "'He lives on the third floor'. Days: સોમવાર (somvār) Monday, મંગળવાર (maṅgaḷvār) Tuesday, "
  "બુધવાર (budhvār) Wednesday, ગુરુવાર (guruvār) Thursday, શુક્રવાર (śukravār) Friday, શનિવાર "
  "(śanivār) Saturday, રવિવાર (ravivār) Sunday. Months: જાન્યુઆરી (jānyuārī) January, "
  "ફેબ્રુઆરી (phebruārī) February, માર્ચ (mārca) March, એપ્રિલ (epril) April, મે (me) May, જૂન "
  "(jūn) June, જુલાઈ (julāī) July, ઑગસ્ટ (ŏgasṭa) August, સપ્ટેમ્બર (sapṭembar) September, "
  "ઑક્ટોબર (ŏkṭobar) October, નવેમ્બર (navembar) November, ડિસેમ્બર (ḍisembar) December; "
  "traditional Gujarati (Vikram Samvat) months include કારતક, માગશર, પોષ, મહા, ફાગણ, ચૈત્ર, "
  "વૈશાખ, જેઠ, અષાઢ, શ્રાવણ, ભાદરવો, આસો. Seasons: ઉનાળો (uṇāḷo) summer, ચોમાસું (comāsuṁ) "
  "monsoon, શિયાળો (śiyāḷo) winter, વસંત (vasant) spring. Clock time: વાગ્યો/વાગ્યા (vāgyo/"
  "vāgyā) o’clock: એક વાગ્યો (ek vāgyo) - 'one o’clock', ત્રણ વાગ્યા (traṇ vāgyā) - 'three "
  "o’clock'; minutes: પાંચ વાગીને દસ મિનિટ (pā̃c vāgīne das miniṭ) - 'ten minutes past five'; "
  "સવા (savā) quarter past, અડધો (aḍdho) half: સવા ત્રણ (savā traṇ) - 'quarter past three', "
  "સાડા ચાર (sāḍā cār) - 'half past four'. Dates: આજે સોમવાર છે (āje somvār che) - 'Today is "
  "Monday'; મારો જન્મદિવસ પાંચમી જૂને છે (māro janmadivas pā̃cmī jūne che) - 'My birthday is "
  "on June fifth'; કાલે રવિવાર છે (kāle ravivār che) - 'Tomorrow is Sunday'; ગઈકાલે વરસાદ "
  "હતો (gaīkāle varsād hato) - 'It rained yesterday'."),
 "how_it_works": (
  "This record makes you fluent in counting and clock-reading: 1-100 with the Indian "
  "lakh/crore system, ordinals, the seven days, twelve months plus the traditional Gujarati "
  "calendar months, four seasons, and clock time with સવા/સાડા. Count objects around you "
  "to વીસ, then say the time every hour until the pattern sticks."),
 "key_points": [
  "એક બે ત્રણ ચાર પાંચ છ સાત આઠ નવ દસ - 1 to 10; વીસ ત્રીસ ચાળીસ પચાસ - 20/30/40/50.",
  "Indian system: હજાર (1,000), લાખ (100,000), કરોડ (10,000,000).",
  "Ordinals: પહેલો, બીજો, ત્રીજો, ચોથો, પાંચમો.",
  "Days: સોમવાર, મંગળવાર, બુધવાર, ગુરુવાર, શુક્રવાર, શનિવાર, રવિવાર.",
  "Clock: વાગ્યો/વાગ્યા; સવા = quarter past, સાડા = half past.",
  "ત્રણ વાગ્યા (traṇ vāgyā) - 'three o’clock'; સવા ત્રણ - 'quarter past three'.",
  "મારી પાસે બે પુસ્તકો છે (mārī pāse be pustako che) - 'I have two books'.",
  "કાલે means 'tomorrow' or 'yesterday' - ગઈકાલે pins it to yesterday.",
 ],
 "requirements": [
  "Count 1-20 forward and backward without looking.",
  "Say today's day, date and the current time in Gujarati.",
  "Learn the lakh/crore groupings - they run Indian money and news.",
 ],
 "standards": [
  "Unicode Standard, Gujarati block U+0A80-U+0AFF (digits ૦-૯)",
  "Vikram Samvat traditional calendar month names",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Numbers and time chapters.",
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens numbers and time are his original Signature measuring "
  "instruments: the lakh/crore scale his counting engine, સવા/સાડા his clock gears, the "
  "seven days a weekly Signature cycle. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 9
{
 "key": "greetings", "name": "Gujarati Greetings and Everyday Phrases",
 "group": "Foundations", "ladder": 9, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Thirty greetings, farewells and politeness phrases with usage notes. 1. નમસ્તે (namaste) "
  "- 'Hello / greetings' - universal, palms together. 2. કેમ છો? (kem cho?) - 'How are you?' "
  "(formal) - the standard Gujarati greeting-question. 3. કેમ છે? (kem che?) - 'How are you?' "
  "(informal, to friends). 4. મજામાં? (majāmā̃?) - 'Doing well?' - casual. 5. સારું છે (sāruṁ "
  "che) - 'All good' - the standard reply. 6. બસ, મજામાં (bas, majāmā̃) - 'Just fine' - casual "
  "reply. 7. આવો, આવો (āvo, āvo) - 'Come in, come in' - welcoming a guest. 8. બેસો (beso) - "
  "'Please sit' - offering a seat. 9. ચા પીશો? (cā pīśo?) - 'Will you have tea?' - the "
  "Gujarati welcome ritual. 10. આવજો (āvjo) - 'Goodbye (come again)' - warm farewell. 11. "
  "ફરી મળીશું (pharī maḷīśuṁ) - 'We will meet again'. 12. શુભ સવાર (śubh savār) - 'Good "
  "morning'. 13. શુભ સાંજ (śubh sā̃j) - 'Good evening'. 14. શુભ રાત્રિ (śubh rātri) - 'Good "
  "night'. 15. આભાર (ābhār) - 'Thank you'. 16. ખૂબ ખૂબ આભાર (khūb khūb ābhār) - 'Thank you "
  "very much'. 17. માફ કરજો (māph karjo) - 'Please forgive me / excuse me' - polite apology. "
  "18. માફ કરશો (māph karśo) - 'Excuse me' - getting attention politely. 19. કૃપા કરીને "
  "(kṛpā karīne) - 'Please / kindly'. 20. મહેરબાની કરીને (maherbānī karīne) - 'Please (do me "
  "the kindness)'. 21. વાંધો નહીં (vā̃dho nahī̃) - 'No problem / never mind'. 22. ભલે (bhale) - "
  "'Okay / fine / may it be so' - agreement. 23. સારું (sāruṁ) - 'Okay / good'. 24. હા (hā) - "
  "'Yes'. 25. ના (nā) - 'No'. 26. ખરેખર? (kharekhar?) - 'Really?' - surprise. 27. અરે વાહ! "
  "(are vāh!) - 'Oh wow!' - delight. 28. શાબાશ! (śābāś!) - 'Well done! / Bravo!' - praise. "
  "29. અભિનંદન (abhinandan) - 'Congratulations'. 30. શુભેચ્છા (śubhecchā) - 'Best wishes'. "
  "Usage: start every meeting with નમસ્તે + કેમ છો?, answer સારું છે, offer ચા before business, "
  "close with આવજો. Use માફ કરજો for real apologies and માફ કરશો to get attention."),
 "how_it_works": (
  "This record is your social survival kit: the thirty phrases that open doors in Gujarat. "
  "Each carries a usage note - when to say it, to whom, and what it signals. Practice them "
  "as a chain: greeting, small talk, offer, thanks, farewell. Say the whole chain aloud "
  "until it flows like one breath."),
 "key_points": [
  "નમસ્તે (namaste) + કેમ છો? (kem cho?) opens every polite meeting.",
  "કેમ છો? is formal; કેમ છે? is for close friends.",
  "ચા પીશો? (cā pīśo?) - offering tea is the Gujarati welcome ritual.",
  "આવજો (āvjo) - 'come again' - is the warm standard farewell.",
  "માફ કરજો = apology; માફ કરશો = 'excuse me' to get attention.",
  "આભાર (ābhār) - thank you; ખૂબ ખૂબ આભાર - thank you very much.",
  "ભલે (bhale) - the all-purpose 'okay / agreed'.",
  "શાબાશ! (śābāś!) praises; અભિનંદન congratulates; શુભેચ્છા wishes well.",
 ],
 "requirements": [
  "Greet someone with the full chain: નમસ્તે, કેમ છો?, સારું છે.",
  "Practice the tea offer: ચા પીશો? - with a welcoming gesture.",
  "Close every practice conversation with આવજો.",
 ],
 "standards": [
  "Standard Gujarati polite-register conventions",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Conversation sections.",
 ],
 "sig_lens": (
  "Through the Signature lens these phrases are his original Signature social instruments: "
  "કેમ છો? a handshake in sound, ચા પીશો? a welcome ritual he performs, આવજો a door left "
  "open. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 10
{
 "key": "grammar", "name": "Gujarati Grammar Essentials",
 "group": "Foundations", "ladder": 10, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The essential rules with a translated example for each. 1. Word order is SOV: હું પાણી "
  "પીઉં છું (huṁ pāṇī pīuṁ chuṁ) - 'I drink water' (I water drink). 2. Three genders: છોકરો "
  "રમે છે (chokro rame che) - 'The boy plays' (m); છોકરી રમે છે (chokrī rame che) - 'The girl "
  "plays' (f); બાળક રમે છે (bāḷak rame che) - 'The child plays' (n). 3. Number: છોકરો/છોકરાઓ "
  "(chokro/chokrāo) - 'boy/boys'; છોકરી/છોકરીઓ (chokrī/chokrīo) - 'girl/girls'. 4. No articles: "
  "પુસ્તક (pustak) means 'book', 'a book' or 'the book' - context decides. 5. Postpositions "
  "replace prepositions and follow the noun: માં (mā̃) in - ઘરમાં (gharmā̃) - 'in the house'; "
  "પર (par) on - ટેબલ પર (ṭebal par) - 'on the table'; થી (thī) from - ગામથી (gāmthī) - 'from "
  "the village'; ને (ne) to - તેને આપો (tene āpo) - 'give to him'; નો/ની/નું (no/nī/nuṁ) of - "
  "મારું પુસ્તક (māruṁ pustak) - 'my book'; સાથે (sāthe) with - મારી સાથે આવો (mārī sāthe "
  "āvo) - 'come with me'. 6. Negation with નથી/નહીં: હું નથી જતો (huṁ nathī jato) - 'I am not "
  "going' (m speaker); તે નથી આવતી (te nathī āvatī) - 'She is not coming'; હું નહીં જાઉં (huṁ "
  "nahī̃ jāuṁ) - 'I will not go'. 7. Questions: intonation or question words - તું ક્યાં જાય "
  "છે? (tuṁ kyā̃ jāy che?) - 'Where are you going?'; શું તે આવે છે? (śuṁ te āve che?) - 'Is "
  "he coming?'. 8. Ergative past for transitive verbs: મેં પત્ર લખ્યો (mẽ patra lakhyo) - 'I "
  "wrote the letter' (verb agrees with પત્ર, masculine); તેણે ચા પીધી (teṇe cā pīdhī) - 'She "
  "drank tea' (verb agrees with ચા, feminine). 9. Adjectives agree: નવો ફોન (navo phon) - "
  "'new phone' (m); નવી ગાડી (navī gāḍī) - 'new car' (f); નવું ઘર (navuṁ ghar) - 'new house' "
  "(n). 10. Polite imperative: બેસો (beso) - 'please sit'; informal: બેસ (bes) - 'sit'."),
 "how_it_works": (
  "This record is the rulebook every later record obeys: ten rules, each with a sentence "
  "that proves it. Read a rule, say its sentence, then build two of your own by swapping "
  "nouns from record 4. The ergative past (rule 8) is the one that surprises learners - "
  "practice મેં/તેણે sentences until the verb-agreement flip feels natural."),
 "key_points": [
  "SOV word order: હું પાણી પીઉં છું - 'I water drink'.",
  "Three genders (m/f/n); adjectives and verbs agree with them.",
  "No articles: પુસ્તક = 'book / a book / the book'.",
  "Postpositions follow nouns: ઘરમાં (in the house), ટેબલ પર (on the table), ગામથી (from the village).",
  "Negation: નથી for present, નહીં for future/imperative.",
  "Questions use intonation or શું/કોણ/ક્યાં/ક્યારે/કેમ.",
  "Past transitive is ergative: મેં પત્ર લખ્યો - the verb agrees with the object.",
  "Polite command adds -ો: બેસ (sit) vs બેસો (please sit).",
 ],
 "requirements": [
  "Build ten SOV sentences by combining records 4 and 5.",
  "Convert five present sentences to negative with નથી.",
  "Write three ergative past sentences: મેં..., તેણે..., અમે....",
 ],
 "standards": [
  "Standard Gujarati grammatical description (Cardona & Suthar 2003)",
 ],
 "citations": [
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003. Syntax section.",
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Grammar chapters.",
 ],
 "sig_lens": (
  "Through the Signature lens grammar is his original Signature rule engine: SOV the "
  "assembly order, three genders the sorting bins, postpositions the connectors, the "
  "ergative past a gear that flips agreement. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 11
{
 "key": "home", "name": "Home and Family Sentences",
 "group": "Compounded", "ladder": 11, "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about house, rooms, furniture and family. 1. આ મારું ઘર છે (ā māruṁ "
  "ghar che) - 'This is my house'. 2. ઘરમાં ચાર ઓરડા છે (gharmā̃ cār orḍā che) - 'There are "
  "four rooms in the house'. 3. રસોડું મોટું છે (rasoḍuṁ moṭuṁ che) - 'The kitchen is big'. "
  "4. બેઠકખંડમાં સોફો છે (beṭhakakhaṇḍamā̃ sopho che) - 'There is a sofa in the living room'. "
  "5. મારો ઓરડો ઉપર છે (māro orḍo upar che) - 'My room is upstairs'. 6. ટેબલ પર પુસ્તક છે "
  "(ṭebal par pustak che) - 'There is a book on the table'. 7. ખુરશી બારી પાસે છે (khurśī "
  "bārī pāse che) - 'The chair is near the window'. 8. પિતા ઑફિસે ગયા છે (pitā ŏphise gayā "
  "che) - 'Father has gone to the office'. 9. માતા રસોડામાં રાંધે છે (mātā rasoḍāmā̃ rā̃dhe "
  "che) - 'Mother is cooking in the kitchen'. 10. મારો ભાઈ શાળાએ જાય છે (māro bhāī śāḷāe "
  "jāy che) - 'My brother goes to school'. 11. મારી બહેન કૉલેજમાં ભણે છે (mārī bahen kŏlej "
  "mā̃ bhaṇe che) - 'My sister studies in college'. 12. દાદા બગીચામાં બેઠા છે (dādā bagīcāmā̃ "
  "beṭhā che) - 'Grandfather is sitting in the garden'. 13. દાદી વાર્તા કહે છે (dādī vārtā "
  "kahe che) - 'Grandmother tells stories'. 14. અમે સાથે જમીએ છીએ (ame sāthe jamīe chīe) - "
  "'We eat together'. 15. ઘર સાફ રાખો (ghar sāph rākho) - 'Keep the house clean'. 16. લાઇટ "
  "બંધ કરો (lāiṭ bandh karo) - 'Turn off the light'. 17. બારણું ખોલો (bāraṇuṁ kholo) - 'Open "
  "the door'. 18. બારી બંધ કરો (bārī bandh karo) - 'Close the window'. 19. મારો પરિવાર મોટો "
  "છે (māro parivār moṭo che) - 'My family is big'. 20. અમે ઘરે ખુશ છીએ (ame ghare khuś "
  "chīe) - 'We are happy at home'."),
 "how_it_works": (
  "This record moves you from words to home life: twenty sentences that name every room, "
  "key furniture, and every family member in action. Walk through your own home saying "
  "each sentence - point at the રસોડું, the બારી, the સોફો. Family words (પિતા, માતા, ભાઈ, "
  "બહેન, દાદા, દાદી) double as the respect vocabulary for elders everywhere."),
 "key_points": [
  "ઘર (ghar) - house; ઓરડો (orḍo) - room; રસોડું (rasoḍuṁ) - kitchen; બેઠકખંડ - living room.",
  "પિતા/માતા - father/mother; ભાઈ/બહેન - brother/sister; દાદા/દાદી - grandfather/grandmother.",
  "ટેબલ પર (on the table), બારી પાસે (near the window), ઘરમાં (in the house).",
  "ઘર સાફ રાખો - 'Keep the house clean'; લાઇટ બંધ કરો - 'Turn off the light'.",
  "અમે સાથે જમીએ છીએ (ame sāthe jamīe chīe) - 'We eat together'.",
  "મારો પરિવાર મોટો છે (māro parivār moṭo che) - 'My family is big'.",
 ],
 "requirements": [
  "Walk through your home naming each room in Gujarati.",
  "Introduce your family members with one sentence each.",
  "Give the four household commands (15-18) aloud as orders.",
 ],
 "standards": [
  "Standard Gujarati household vocabulary",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens home sentences are his original Signature household "
  "instruments: each room a chamber of his system, each family word a respect setting, "
  "every command a switch he flips. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 12
{
 "key": "food", "name": "Food and Cooking Sentences",
 "group": "Compounded", "ladder": 12, "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about meals, ingredients, cooking and restaurants. 1. મને ભૂખ લાગી છે "
  "(mane bhūkh lāgī che) - 'I am hungry'. 2. જમવાનું તૈયાર છે (jamvānuṁ taiyār che) - 'The "
  "meal is ready'. 3. આજે શું બનાવ્યું? (āje śuṁ banāvyuṁ?) - 'What did you cook today?' 4. "
  "રોટલી અને શાક ખૂબ સ્વાદિષ્ટ છે (roṭlī ane śāk khūb svādiṣṭ che) - 'The bread and curry are "
  "very tasty'. 5. મને તીખું નથી ભાવતું (mane tīkhuṁ nathī bhāvtuṁ) - 'I do not like spicy "
  "food'. 6. થોડું મીઠું આપો (thoḍuṁ mīṭhuṁ āpo) - 'Give me a little salt'. 7. ચામાં ખાંડ નાખો "
  "(cāmā̃ khā̃ḍ nākho) - 'Put sugar in the tea'. 8. દૂધ ઉકાળો (dūdh ukāḷo) - 'Boil the milk'. "
  "9. શાક સમારો (śāk samāro) - 'Chop the vegetables'. 10. ભાત રાંધો (bhāt rā̃dho) - 'Cook the "
  "rice'. 11. હું શાકાહારી છું (huṁ śākāhārī chuṁ) - 'I am vegetarian'. 12. મને દાળ ભાત ભાવે "
  "છે (mane dāḷ bhāt bhāve che) - 'I like lentils and rice'. 13. ખીચડી હળવી હોય છે (khīchḍī "
  "haḷvī hoy che) - 'Khichdi is light (easy to digest)'. 14. જમ્યા પછી ફળ ખાઓ (jamyā pachī "
  "phaḷ khāo) - 'Eat fruit after the meal'. 15. પાણી પીઓ (pāṇī pīo) - 'Drink water'. 16. "
  "રેસ્ટોરન્ટમાં ટેબલ બુક કરો (resṭoranṭamā̃ ṭebal buk karo) - 'Book a table in the restaurant'. "
  "17. મેનુ બતાવો (menu batāvo) - 'Show me the menu'. 18. બિલ લાવો (bil lāvo) - 'Bring the "
  "bill'. 19. જમવાનું ખૂબ સરસ હતું (jamvānuṁ khūb saras hatuṁ) - 'The meal was very nice'. 20. "
  "આવજો, ફરી આવજો (āvjo, pharī āvjo) - 'Goodbye, come again - leaving the table'."),
 "how_it_works": (
  "This record feeds you: twenty sentences from hunger to bill-paying, covering Gujarat's "
  "vegetarian table (રોટલી, શાક, દાળ, ભાત, ખીચડી), cooking verbs (રાંધવું, સમારવું, ઉકાળવું), "
  "and restaurant phrases. Cook one meal narrating each step in Gujarati - થોડું મીઠું "
  "નાખો - and the verbs will stick to your hands."),
 "key_points": [
  "મને ભૂખ લાગી છે - 'I am hungry'; જમવાનું તૈયાર છે - 'The meal is ready'.",
  "રોટલી, શાક, દાળ, ભાત, ખીચડી - the core Gujarati vegetarian meal.",
  "રાંધવું (to cook), સમારવું (to chop), ઉકાળવું (to boil).",
  "હું શાકાહારી છું - 'I am vegetarian'.",
  "મેનુ બતાવો - 'Show the menu'; બિલ લાવો - 'Bring the bill'.",
  "જમવાનું ખૂબ સરસ હતું - 'The meal was very nice'.",
 ],
 "requirements": [
  "Narrate cooking one full meal in Gujarati, step by step.",
  "Order a full meal in a restaurant role-play: table, menu, bill.",
  "Say whether five foods are મીઠું/ખાટું/તીખું.",
 ],
 "standards": [
  "Standard Gujarati food vocabulary",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens food sentences are his original Signature kitchen "
  "instruments: each ingredient a material, each cooking verb a process step, the "
  "restaurant phrases his service protocol. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 13
{
 "key": "travel", "name": "Travel and Directions Sentences",
 "group": "Compounded", "ladder": 13, "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about transport, directions, tickets and lodging. 1. સ્ટેશન ક્યાં છે? "
  "(sṭeśan kyā̃ che?) - 'Where is the station?' 2. બસ સ્ટેન્ડ કેટલું દૂર છે? (bas sṭenḍ "
  "keṭluṁ dūr che?) - 'How far is the bus stand?' 3. જમણી બાજુ વળો (jamṇī bāju vaḷo) - 'Turn "
  "right'. 4. ડાબી બાજુ વળો (ḍābī bāju vaḷo) - 'Turn left'. 5. સીધા જાઓ (sīdhā jāo) - 'Go "
  "straight'. 6. અહીંથી કેટલો સમય લાગશે? (ahī̃thī keṭlo samay lāgśe?) - 'How long will it "
  "take from here?' 7. ટિકિટ કેટલાની છે? (ṭikiṭ keṭlānī che?) - 'How much is the ticket?' 8. "
  "એક ટિકિટ આપો (ek ṭikiṭ āpo) - 'Give me one ticket'. 9. ટ્રેન ક્યારે આવશે? (ṭren kyāre "
  "āvśe?) - 'When will the train come?' 10. બસ મોડી છે (bas moḍī che) - 'The bus is late'. "
  "11. રિક્ષા મળશે? (rikṣā maḷśe?) - 'Will I get a rickshaw?' 12. ભાડું કેટલું? (bhāḍuṁ "
  "keṭluṁ?) - 'What is the fare?' 13. મીટર પર ચલાવો (mīṭar par calāvo) - 'Go by the meter'. "
  "14. અહીં ઊભા રાખો (ahī̃ ūbhā rākho) - 'Stop here'. 15. હોટલ ક્યાં છે? (hoṭal kyā̃ che?) - "
  "'Where is the hotel?' 16. એક રૂમ જોઈએ છે (ek rūm joīe che) - 'I need a room'. 17. એક "
  "રાતનું ભાડું કેટલું? (ek rātnuṁ bhāḍuṁ keṭluṁ?) - 'What is the charge for one night?' 18. "
  "સવારે ચા મળશે? (savāre cā maḷśe?) - 'Will tea be available in the morning?' 19. મારો "
  "સામાન ઉપર લઈ જાઓ (māro sāmān upar laī jāo) - 'Take my luggage upstairs'. 20. મુસાફરી "
  "સુખદ રહો (musāpharī sukhad raho) - 'Have a pleasant journey'."),
 "how_it_works": (
  "This record is your Gujarati road kit: asking where things are, giving and getting "
  "directions, buying tickets, bargaining with rickshaws, and checking into hotels. "
  "Practice as pairs - one asks સ્ટેશન ક્યાં છે?, the other answers with જમણી/ડાબી/સીધા. "
  "The rickshaw lines (11-14) are survival Gujarati in any Gujarat city."),
 "key_points": [
  "સ્ટેશન ક્યાં છે? - 'Where is the station?' - the most useful travel question.",
  "જમણી (right), ડાબી (left), સીધા (straight) - the direction trio.",
  "ટિકિટ કેટલાની છે? - 'How much is the ticket?'",
  "રિક્ષા મળશે? / ભાડું કેટલું? / મીટર પર ચલાવો - rickshaw survival.",
  "એક રૂમ જોઈએ છે - 'I need a room'.",
  "મુસાફરી સુખદ રહો - 'Have a pleasant journey'.",
 ],
 "requirements": [
  "Give directions to three real places using જમણી/ડાબી/સીધા.",
  "Role-play a full rickshaw ride: hail, bargain, direct, stop, pay.",
  "Book a hotel room start to finish in Gujarati.",
 ],
 "standards": [
  "Standard Gujarati travel vocabulary",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Travel sections.",
 ],
 "sig_lens": (
  "Through the Signature lens travel sentences are his original Signature navigation "
  "instruments: directions a compass, tickets a boarding pass, the rickshaw bargain a "
  "negotiation engine. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 14
{
 "key": "workschool", "name": "Work and School Sentences",
 "group": "Compounded", "ladder": 14, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about jobs, office, classroom and learning. 1. તમે શું કામ કરો છો? "
  "(tame śuṁ kām karo cho?) - 'What work do you do?' 2. હું શિક્ષક છું (huṁ śikṣak chuṁ) - "
  "'I am a teacher'. 3. તે ડૉક્ટર છે (te ḍŏkṭar che) - 'She is a doctor'. 4. હું ઑફિસમાં કામ "
  "કરું છું (huṁ ŏphisamā̃ kām karuṁ chuṁ) - 'I work in an office'. 5. મારી નોકરી સારી છે "
  "(mārī nokrī sārī che) - 'My job is good'. 6. મીટિંગ દસ વાગ્યે છે (mīṭiṁg das vāgye che) - "
  "'The meeting is at ten o’clock'. 7. રિપોર્ટ તૈયાર કરો (riporṭ taiyār karo) - 'Prepare the "
  "report'. 8. ઈમેલ મોકલો (īmel moklo) - 'Send the email'. 9. બોસ સાથે વાત કરો (bos sāthe "
  "vāt karo) - 'Talk to the boss'. 10. રજા જોઈએ છે (rajā joīe che) - 'I need leave'. 11. શાળા "
  "સવારે શરૂ થાય છે (śāḷā savāre śarū thāy che) - 'School starts in the morning'. 12. વર્ગમાં "
  "શાંતિથી બેસો (vargamā̃ śāṁtithī beso) - 'Sit quietly in class'. 13. પુસ્તક ખોલો (pustak "
  "kholo) - 'Open the book'. 14. પાઠ વાંચો (pāṭh vā̃co) - 'Read the lesson'. 15. પ્રશ્ન પૂછો "
  "(praśna pūcho) - 'Ask a question'. 16. જવાબ લખો (javāb lakho) - 'Write the answer'. 17. "
  "ગૃહકાર્ય કરો (gṛhakārya karo) - 'Do the homework'. 18. પરીક્ષા આવતા અઠવાડિયે છે (parīkṣā "
  "āvatā aṭhavāḍiye che) - 'The exam is next week'. 19. મહેનત કરો, સફળ થશો (mahenat karo, "
  "saphaḷ thaśo) - 'Work hard, you will succeed'. 20. શીખવાનું ક્યારેય બંધ ન કરો (śīkhvānuṁ "
  "kyārey bandh na karo) - 'Never stop learning'."),
 "how_it_works": (
  "This record covers the two daily worlds: office and classroom. Ten sentences each, "
  "mixing statements, requests and commands. Notice how workplace Gujarati stays in the "
  "polite તમે/કરો register. Practice by narrating your own workday - હું ઑફિસમાં કામ કરું "
  "છું - then give the classroom commands to an imaginary class."),
 "key_points": [
  "તમે શું કામ કરો છો? - 'What work do you do?'",
  "મીટિંગ દસ વાગ્યે છે - 'The meeting is at ten'.",
  "રિપોર્ટ તૈયાર કરો / ઈમેલ મોકલો - office commands in polite register.",
  "શાળા સવારે શરૂ થાય છે - 'School starts in the morning'.",
  "પુસ્તક ખોલો / પાઠ વાંચો / જવાબ લખો - classroom commands.",
  "મહેનત કરો, સફળ થશો - 'Work hard, you will succeed'.",
 ],
 "requirements": [
  "Narrate your workday in six Gujarati sentences.",
  "Give all ten classroom commands as a teacher would.",
  "Ask and answer તમે શું કામ કરો છો? for five professions.",
 ],
 "standards": [
  "Standard Gujarati workplace and school vocabulary",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens work and school sentences are his original Signature "
  "productivity instruments: office phrases his command protocols, classroom commands "
  "his training drills. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 15
{
 "key": "health", "name": "Health and Body Sentences",
 "group": "Compounded", "ladder": 15, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about body parts, symptoms, doctor visits and pharmacy. Body: માથું "
  "(māthuṁ) - head: મારું માથું દુઃખે છે (māruṁ māthuṁ duḥkhe che) - 'My head aches'. 2. આંખ "
  "(ā̃kh, f) - eye: મારી આંખો લાલ છે (mārī ā̃kho lāl che) - 'My eyes are red'. 3. કાન (kān, "
  "m) - ear: કાનમાં દુઃખે છે (kānmā̃ duḥkhe che) - 'My ear hurts'. 4. નાક (nāk, n) - nose: "
  "નાક બંધ છે (nāk bandh che) - 'My nose is blocked'. 5. મોં (mõ, n) - mouth: મોં ખોલો (mõ "
  "kholo) - 'Open your mouth'. 6. દાંત (dā̃t, m) - tooth: દાંત દુઃખે છે (dā̃t duḥkhe che) - "
  "'My tooth aches'. 7. ગળું (gaḷuṁ, n) - throat: ગળામાં ખારાશ છે (gaḷāmā̃ khārāś che) - 'My "
  "throat is sore'. 8. હાથ (hāth, m) - hand: હાથ ધુઓ (hāth dhuo) - 'Wash your hands'. 9. પગ "
  "(pag, m) - leg/foot: પગ મચકોડાયો છે (pag mackoḍāyo che) - 'My ankle is sprained'. 10. પેટ "
  "(peṭ, n) - stomach: પેટમાં દુઃખે છે (peṭmā̃ duḥkhe che) - 'My stomach hurts'. Symptoms: 11. "
  "મને તાવ છે (mane tāv che) - 'I have a fever'. 12. મને શરદી થઈ છે (mane śardī thaī che) - "
  "'I have a cold'. 13. મને ઉધરસ આવે છે (mane udhras āve che) - 'I have a cough'. 14. મને "
  "ચક્કર આવે છે (mane cakkar āve che) - 'I feel dizzy'. 15. મને નબળાઈ લાગે છે (mane nabḷāī "
  "lāge che) - 'I feel weak'. Doctor: 16. ડૉક્ટરને બતાવો (ḍŏkṭarne batāvo) - 'See a doctor'. "
  "17. દવા સમયસર લો (davā samaysar lo) - 'Take the medicine on time'. 18. આરામ કરો (ārām "
  "karo) - 'Rest'. 19. ગરમ પાણી પીઓ (garam pāṇī pīo) - 'Drink warm water'. Pharmacy: 20. "
  "મને તાવની દવા આપો (mane tāvnī davā āpo) - 'Give me medicine for fever'."),
 "how_it_works": (
  "This record teaches the body and how to report trouble: ten body-part sentences with "
  "the દુઃખે છે ('aches') pattern, five symptom reports with the મને... છે pattern, and "
  "five doctor/pharmacy lines. The pattern મને X છે covers almost every symptom - swap in "
  "તાવ, શરદી, ઉધરસ. Practice by pointing at body parts and naming them, then reporting "
  "three imaginary symptoms."),
 "key_points": [
  "દુઃખે છે = 'aches/hurts': માથું દુઃખે છે, દાંત દુઃખે છે.",
  "મને... છે = 'I have...': મને તાવ છે, મને શરદી થઈ છે.",
  "માથું, આંખ, કાન, નાક, મોં, દાંત, ગળું, હાથ, પગ, પેટ - ten body parts.",
  "ડૉક્ટરને બતાવો - 'See a doctor'; દવા સમયસર લો - 'Take medicine on time'.",
  "મને તાવની દવા આપો - 'Give me medicine for fever' (pharmacy).",
  "આરામ કરો - 'Rest'; ગરમ પાણી પીઓ - 'Drink warm water'.",
 ],
 "requirements": [
  "Name ten body parts pointing at yourself.",
  "Report five symptoms using મને... છે.",
  "Role-play a full doctor visit: greeting, symptoms, advice, pharmacy.",
 ],
 "standards": [
  "Standard Gujarati health vocabulary",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens health sentences are his original Signature body instruments: "
  "દુઃખે છે a diagnostic signal, મને... છે a status report, the doctor's lines his repair "
  "protocol. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 16
{
 "key": "emotions", "name": "Emotions and Feelings Sentences",
 "group": "Compounded", "ladder": 16, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about feelings - happy, sad, angry, afraid, love, surprise. 1. હું ખૂબ "
  "ખુશ છું (huṁ khūb khuś chuṁ) - 'I am very happy'. 2. આજે મારો દિવસ સારો છે (āje māro "
  "divas sāro che) - 'Today is a good day for me'. 3. તે હસી રહી છે (te hasī rahī che) - "
  "'She is laughing'. 4. સમાચાર સાંભળીને આનંદ થયો (samācār sā̃bhaḷīne ānand thayo) - 'Hearing "
  "the news made me glad'. 5. હું દુઃખી છું (huṁ duḥkhī chuṁ) - 'I am sad'. 6. તે રડે છે (te "
  "raḍe che) - 'He is crying'. 7. મારું દિલ ભારે છે (māruṁ dil bhāre che) - 'My heart feels "
  "heavy'. 8. ચિંતા ન કરો (cintā na karo) - 'Do not worry'. 9. મને ગુસ્સો આવે છે (mane gusso "
  "āve che) - 'I feel angry'. 10. શાંત થાઓ (śāṁt thāo) - 'Calm down'. 11. મને બીક લાગે છે "
  "(mane bīk lāge che) - 'I feel afraid'. 12. અંધારાથી ડર લાગે છે (ãdhārāthī ḍar lāge che) - "
  "'The darkness frightens me'. 13. હિંમત રાખો (hiṁmat rākho) - 'Be brave'. 14. હું તને પ્રેમ "
  "કરું છું (huṁ tane prem karuṁ chuṁ) - 'I love you'. 15. મારો પરિવાર મને વહાલો છે (māro "
  "parivār mane vahālo che) - 'My family is dear to me'. 16. મને નવાઈ લાગી (mane navāī "
  "lāgī) - 'I was surprised'. 17. ખરેખર? મને વિશ્વાસ નથી થતો (kharekhar? mane viśvās nathī "
  "thato) - 'Really? I cannot believe it'. 18. મને શરમ આવે છે (mane śaram āve che) - 'I feel "
  "embarrassed'. 19. મને ગર્વ છે (mane garva che) - 'I feel proud'. 20. બધું સારું થશે (badhuṁ "
  "sāruṁ thaśe) - 'Everything will be all right'."),
 "how_it_works": (
  "This record gives feelings a voice: twenty sentences across joy, sorrow, anger, fear, "
  "love and surprise. Notice the patterns: હું X છું for states, મને X આવે/લાગે છે for "
  "feelings that 'come to' you. Say each one with the matching face - emotion words stick "
  "when the body joins in."),
 "key_points": [
  "હું ખુશ છું - 'I am happy'; હું દુઃખી છું - 'I am sad'.",
  "Feelings use મને... આવે/લાગે છે: મને ગુસ્સો આવે છે, મને બીક લાગે છે.",
  "હું તને પ્રેમ કરું છું - 'I love you'.",
  "ચિંતા ન કરો - 'Do not worry'; શાંત થાઓ - 'Calm down'; હિંમત રાખો - 'Be brave'.",
  "મને નવાઈ લાગી - 'I was surprised'; મને ગર્વ છે - 'I feel proud'.",
  "બધું સારું થશે - 'Everything will be all right'.",
 ],
 "requirements": [
  "Say each sentence with a matching facial expression.",
  "Describe your current mood in three Gujarati sentences.",
  "Comfort a friend: use ચિંતા ન કરો, હિંમત રાખો, બધું સારું થશે.",
 ],
 "standards": [
  "Standard Gujarati emotion vocabulary",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens emotion sentences are his original Signature feeling "
  "instruments: each sentence a dial for an inner state, મને... આવે છે feelings arriving "
  "like weather. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 17
{
 "key": "nature", "name": "Nature and Weather Sentences",
 "group": "Compounded", "ladder": 17, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about animals, plants, seasons and weather talk. 1. આજે હવામાન સારું "
  "છે (āje havāmān sāruṁ che) - 'The weather is nice today'. 2. વરસાદ પડે છે (varsād paḍe "
  "che) - 'It is raining'. 3. તડકો નીકળ્યો છે (taḍko nīkaḷyo che) - 'The sun has come out'. "
  "4. ખૂબ ગરમી છે (khūb garmī che) - 'It is very hot'. 5. ઠંડી વાય છે (ṭhaṇḍī vāy che) - 'A "
  "cold wind is blowing'. 6. ચોમાસું આવી ગયું (comāsuṁ āvī gayuṁ) - 'The monsoon has arrived'. "
  "7. શિયાળામાં ધુમ્મસ હોય છે (śiyāḷāmā̃ dhummas hoy che) - 'There is fog in winter'. 8. "
  "વસંતમાં ફૂલો ખીલે છે (vasantamā̃ phūlo khīle che) - 'Flowers bloom in spring'. 9. ઝાડ પર "
  "પક્ષીઓ બેઠાં છે (jhāḍ par pakṣīo beṭhā̃ che) - 'Birds are sitting on the tree'. 10. કૂતરો "
  "ભસે છે (kūtro bhase che) - 'The dog is barking'. 11. બિલાડી દૂધ પીએ છે (bilāḍī dūdh pīe "
  "che) - 'The cat drinks milk'. 12. ગાય ઘાસ ખાય છે (gāy ghās khāy che) - 'The cow eats grass'. "
  "13. હાથી મોટું પ્રાણી છે (hāthī moṭuṁ prāṇī che) - 'The elephant is a big animal'. 14. "
  "વાઘ જંગલમાં રહે છે (vāgh jaṅgalmā̃ rahe che) - 'The tiger lives in the forest'. 15. માછલી "
  "પાણીમાં તરે છે (māchlī pāṇīmā̃ tare che) - 'The fish swims in water'. 16. નદી વહે છે (nadī "
  "vahe che) - 'The river flows'. 17. પહાડ ઊંચો છે (pahāḍ ū̃co che) - 'The mountain is tall'. "
  "18. સમુદ્ર વિશાળ છે (samudra viśāḷ che) - 'The ocean is vast'. 19. ચાંદ ચમકે છે (cā̃d "
  "camke che) - 'The moon is shining'. 20. તારા ટમટમે છે (tārā ṭamṭame che) - 'The stars are "
  "twinkling'."),
 "how_it_works": (
  "This record takes you outside: weather talk (the universal small talk), the monsoon "
  "cycle that shapes Gujarat's year, animals in action, and land, water and sky. Look out "
  "a window and describe what you see - આજે હવામાન... - then name five animals doing five "
  "things."),
 "key_points": [
  "વરસાદ પડે છે - 'It is raining'; તડકો નીકળ્યો છે - 'The sun is out'.",
  "ચોમાસું (monsoon), શિયાળો (winter), ઉનાળો (summer), વસંત (spring).",
  "કૂતરો, બિલાડી, ગાય, હાથી, વાઘ, માછલી, પક્ષી - seven animals.",
  "ઝાડ (tree), ફૂલ (flower), નદી (river), પહાડ (mountain), સમુદ્ર (ocean).",
  "ચાંદ ચમકે છે - 'The moon is shining'; તારા ટમટમે છે - 'The stars twinkle'.",
  "આજે હવામાન સારું છે - 'The weather is nice today'.",
 ],
 "requirements": [
  "Describe today's weather in three sentences.",
  "Name five animals and what each does.",
  "Describe a landscape: mountain, river, trees, sky.",
 ],
 "standards": [
  "Standard Gujarati nature vocabulary",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens nature sentences are his original Signature landscape "
  "instruments: weather his atmosphere dial, animals his living exhibits, the monsoon his "
  "annual cycle. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 18
{
 "key": "shopping", "name": "Shopping and Money Sentences",
 "group": "Compounded", "ladder": 18, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about market, prices, bargaining and paying. 1. આ કેટલાનું છે? (ā "
  "keṭlānuṁ che?) - 'How much is this?' 2. આ બહુ મોંઘું છે (ā bahu moṅghuṁ che) - 'This is too "
  "expensive'. 3. થોડું ઓછું કરો (thoḍuṁ ochuṁ karo) - 'Reduce the price a little'. 4. છેલ્લો "
  "ભાવ બોલો (chello bhāv bolo) - 'Tell me your final price'. 5. સો રૂપિયામાં આપશો? (so "
  "rūpiyāmā̃ āpśo?) - 'Will you give it for a hundred rupees?' 6. બરાબર, પેક કરો (barābar, "
  "pek karo) - 'Okay, pack it'. 7. બીજું બતાવો (bījuṁ batāvo) - 'Show me another'. 8. આનો રંગ "
  "બીજો છે? (āno raṅg bījo che?) - 'Is there another color of this?' 9. મોટી સાઇઝ છે? (moṭī "
  "sāijh che?) - 'Is there a larger size?' 10. આ તાજું છે? (ā tājuṁ che?) - 'Is this fresh?' "
  "11. એક કિલો બટાટા આપો (ek kilo baṭāṭā āpo) - 'Give me one kilo of potatoes'. 12. અડધો કિલો "
  "ડુંગળી (aḍdho kilo ḍuṅgaḷī) - 'Half a kilo of onions'. 13. છૂટા પૈસા છે? (chūṭā paisā che?) "
  "- 'Do you have change?' 14. કાર્ડ ચાલશે? (kārḍ cālśe?) - 'Will you accept a card?' 15. "
  "રોકડા આપું છું (rokḍā āpuṁ chuṁ) - 'I am paying cash'. 16. બિલ આપો (bil āpo) - 'Give me "
  "the bill'. 17. થેલીમાં નાખો (thelīmā̃ nākho) - 'Put it in the bag'. 18. કાલે નવો માલ આવશે "
  "(kāle navo māl āvśe) - 'New stock will come tomorrow'. 19. દુકાન ક્યારે બંધ થાય છે? (dukān "
  "kyāre bandh thāy che?) - 'When does the shop close?' 20. ખરીદી મજા આવી (kharīdī majā "
  "āvī) - 'Shopping was fun'."),
 "how_it_works": (
  "This record makes you a market negotiator: asking prices, calling things expensive, "
  "bargaining down, closing the deal, and paying. Practice the bargaining chain - આ "
  "કેટલાનું છે? → બહુ મોંઘું છે → થોડું ઓછું કરો → બરાબર, પેક કરો - until you can run it "
  "without thinking. The vegetable lines (11-12) work in any Gujarat market."),
 "key_points": [
  "આ કેટલાનું છે? - 'How much is this?' - the market opener.",
  "બહુ મોંઘું છે → થોડું ઓછું કરો → છેલ્લો ભાવ બોલો - the bargaining chain.",
  "સો રૂપિયામાં આપશો? - 'Will you give it for a hundred rupees?'",
  "છૂટા પૈસા છે? - 'Do you have change?'; કાર્ડ ચાલશે? - 'Card accepted?'",
  "એક કિલો બટાટા / અડધો કિલો ડુંગળી - market weights.",
  "ખરીદી મજા આવી - 'Shopping was fun'.",
 ],
 "requirements": [
  "Run the full bargaining chain on three imaginary items.",
  "Buy vegetables: name five items with weights.",
  "Pay three ways: રોકડા, કાર્ડ, and ask for છૂટા.",
 ],
 "standards": [
  "Standard Gujarati market vocabulary; Indian rupee denominations",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Market sections.",
 ],
 "sig_lens": (
  "Through the Signature lens shopping sentences are his original Signature trade "
  "instruments: the price question his opening move, bargaining his negotiation engine, "
  "પેક કરો his closing stamp. Signature-made teaching, clearly labeled, never presented "
  "as an outside authority's text."),
},
# ================================================================== 19
{
 "key": "social", "name": "Friendship and Social Life Sentences",
 "group": "Compounded", "ladder": 19, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about meeting people, invitations and celebrations. 1. તમને મળીને "
  "આનંદ થયો (tamne maḷīne ānand thayo) - 'Nice to meet you'. 2. તમે ક્યાં રહો છો? (tame kyā̃ "
  "raho cho?) - 'Where do you live?' 3. હું અમદાવાદમાં રહું છું (huṁ amadāvādmā̃ rahuṁ chuṁ) - "
  "'I live in Ahmedabad'. 4. તમારો ફોન નંબર શું છે? (tamāro phon nambar śuṁ che?) - 'What is "
  "your phone number?' 5. આપણે મિત્રો બનીએ (āpaṇe mitro banīe) - 'Let us become friends'. 6. "
  "કાલે મારે ઘરે આવો (kāle māre ghare āvo) - 'Come to my home tomorrow'. 7. જમવા માટે આમંત્રણ "
  "છે (jamvā māṭe āmantraṇ che) - 'You are invited for a meal'. 8. જરૂર આવજો (jarūr āvjo) - "
  "'Do come'. 9. તમારો જન્મદિવસ ક્યારે છે? (tamāro janmadivas kyāre che?) - 'When is your "
  "birthday?' 10. જન્મદિવસની શુભેચ્છા (janmadivasnī śubhecchā) - 'Happy birthday'. 11. ભેટ "
  "સ્વીકારો (bheṭ svīkāro) - 'Please accept the gift'. 12. લગ્નમાં આવજો (lagnamā̃ āvjo) - "
  "'Come to the wedding'. 13. અભિનંદન! (abhinandan!) - 'Congratulations!' 14. તહેવારની "
  "શુભેચ્છા (tahevārnī śubhecchā) - 'Festival greetings'. 15. દિવાળી મુબારક (divāḷī mubārak) - "
  "'Happy Diwali'. 16. સાથે ફોટો પડાવીએ (sāthe phoṭo paḍāvīe) - 'Let us take a photo together'. "
  "17. સંપર્કમાં રહેજો (samparkamā̃ rahejo) - 'Stay in touch'. 18. ફરી ક્યારે મળીશું? (pharī "
  "kyāre maḷīśuṁ?) - 'When will we meet again?' 19. તમારી સાથે વાત કરીને મજા આવી (tamārī "
  "sāthe vāt karīne majā āvī) - 'I enjoyed talking with you'. 20. આવજો, સંભાળજો (āvjo, "
  "sambhāḷjo) - 'Goodbye, take care'."),
 "how_it_works": (
  "This record teaches friendship: first meetings, invitations, celebrations and warm "
  "goodbyes. Gujarati social life runs on invitations - કાલે મારે ઘરે આવો - and festival "
  "greetings. Practice the meeting chain (1-5), the invitation chain (6-8), and the "
  "celebration lines (10-15) as three separate drills."),
 "key_points": [
  "તમને મળીને આનંદ થયો - 'Nice to meet you'.",
  "કાલે મારે ઘરે આવો - 'Come to my home tomorrow' - the invitation.",
  "જન્મદિવસની શુભેચ્છા - 'Happy birthday'; લગ્નમાં આવજો - 'Come to the wedding'.",
  "દિવાળી મુબારક - 'Happy Diwali'; તહેવારની શુભેચ્છા - 'Festival greetings'.",
  "સંપર્કમાં રહેજો - 'Stay in touch'.",
  "તમારી સાથે વાત કરીને મજા આવી - 'I enjoyed talking with you'.",
 ],
 "requirements": [
  "Introduce yourself to an imaginary stranger: five sentences.",
  "Invite someone home, to a meal, and to a wedding.",
  "Give festival greetings for three occasions.",
 ],
 "standards": [
  "Standard Gujarati social conventions",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens social sentences are his original Signature friendship "
  "instruments: the greeting a bridge, the invitation an open door, festival wishes his "
  "celebration protocol. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 20
{
 "key": "tech", "name": "Technology and Communication Sentences",
 "group": "Compounded", "ladder": 20, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences about phone, internet, computer and messaging. 1. મારો ફોન ક્યાં છે? "
  "(māro phon kyā̃ che?) - 'Where is my phone?' 2. ફોન વાગે છે (phon vāge che) - 'The phone "
  "is ringing'. 3. ફોન ઉપાડો (phon upāḍo) - 'Pick up the phone'. 4. હેલો, કોણ બોલે છે? "
  "(helo, koṇ bole che?) - 'Hello, who is speaking?' 5. લાઇન કપાઈ ગઈ (lāin kapāī gaī) - "
  "'The line got disconnected'. 6. ફરી ફોન કરજો (pharī phon karjo) - 'Please call again'. "
  "7. મેસેજ મોકલો (mesej moklo) - 'Send a message'. 8. મને મેસેજ મળ્યો (mane mesej maḷyo) - "
  "'I got the message'. 9. ઈન્ટરનેટ ચાલે છે? (inṭarneṭ cāle che?) - 'Is the internet working?' "
  "10. વાઇફાઇ પાસવર્ડ શું છે? (vāiphāi pāsvarḍ śuṁ che?) - 'What is the WiFi password?' 11. "
  "કમ્પ્યુટર ચાલુ કરો (kampyuṭar cālu karo) - 'Turn on the computer'. 12. કમ્પ્યુટર બંધ કરો "
  "(kampyuṭar bandh karo) - 'Turn off the computer'. 13. ફાઇલ સેવ કરો (phāil sev karo) - "
  "'Save the file'. 14. ફોટો મોકલો (phoṭo moklo) - 'Send the photo'. 15. વીડિયો કૉલ કરીએ "
  "(vīḍiyo kŏl karīe) - 'Let us make a video call'. 16. બેટરી ઓછી છે (beṭarī ochī che) - "
  "'The battery is low'. 17. ચાર્જર આપો (cārjar āpo) - 'Give me the charger'. 18. સ્ક્રીન "
  "તૂટી ગઈ (skrīn ṭūṭī gaī) - 'The screen broke'. 19. એપ ડાઉનલોડ કરો (ep ḍāunlōḍ karo) - "
  "'Download the app'. 20. ઑનલાઇન મળીશું (ŏnlāin maḷīśuṁ) - 'We will meet online'."),
 "how_it_works": (
  "This record wires you up: phone calls, messaging, internet and computer basics in "
  "everyday Gujarati. Much tech vocabulary is borrowed (ફોન, ઈન્ટરનેટ, કમ્પ્યુટર, એપ) with "
  "Gujarati verbs doing the work - ચાલુ કરો, બંધ કરો, મોકલો. Practice by narrating your "
  "phone use: ફોન ઉપાડો, મેસેજ મોકલો, ફોટો મોકલો."),
 "key_points": [
  "હેલો, કોણ બોલે છે? - 'Hello, who is speaking?'",
  "લાઇન કપાઈ ગઈ - 'The line got disconnected'; ફરી ફોન કરજો - 'Call again'.",
  "વાઇફાઇ પાસવર્ડ શું છે? - 'What is the WiFi password?'",
  "કમ્પ્યુટર ચાલુ કરો / બંધ કરો - 'Turn on/off the computer'.",
  "બેટરી ઓછી છે - 'The battery is low'; ચાર્જર આપો - 'Give the charger'.",
  "ઑનલાઇન મળીશું - 'We will meet online'.",
 ],
 "requirements": [
  "Narrate answering a phone call start to finish.",
  "Troubleshoot: internet down, battery low, screen broken.",
  "Send an imaginary message and photo, narrating each tap.",
 ],
 "standards": [
  "Contemporary Gujarati technology vocabulary",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens technology sentences are his original Signature "
  "communication instruments: the phone his voice line, the message his dispatch, the "
  "computer his engine room. Signature-made teaching, clearly labeled, never presented "
  "as an outside authority's text."),
},
# ================================================================== 21
{
 "key": "tenses", "name": "Gujarati Verb Tenses in Sentences",
 "group": "Advanced", "ladder": 21, "ladder_rank": 7, "ladder_tier": "advanced",
 "description": (
  "The full verb system in sentences. PRESENT (stem + endings + છું/છે): હું રોટલી ખાઉં છું "
  "(huṁ roṭlī khāuṁ chuṁ) - 'I eat bread'; તું પાણી પીએ છે (tuṁ pāṇī pīe che) - 'You drink "
  "water'; તે શાળાએ જાય છે (te śāḷāe jāy che) - 'He goes to school'; અમે ગુજરાતી શીખીએ છીએ "
  "(ame gujarātī śīkhīe chīe) - 'We learn Gujarati'; તમે ક્યાં રહો છો? (tame kyā̃ raho cho?) "
  "- 'Where do you live?'; તેઓ કામ કરે છે (teo kām kare che) - 'They work'. PAST: "
  "intransitive - હું ગયો/ગઈ (huṁ gayo/gaī) - 'I went' (m/f); તે આવી (te āvī) - 'She came'; "
  "અમે રમ્યા (ame ramyā) - 'We played'. Transitive past is ergative (ને-forms + object "
  "agreement): મેં પત્ર લખ્યો (mẽ patra lakhyo) - 'I wrote the letter'; તેણે ચા પીધી (teṇe cā "
  "pīdhī) - 'She drank tea'; અમે ઘર બનાવ્યું (ame ghar banāvyuṁ) - 'We built the house'; તેઓએ "
  "ગીત ગાયું (teoae gīt gāyuṁ) - 'They sang a song'. FUTURE: હું જઈશ (huṁ jaīś) - 'I will go'; "
  "તું આવીશ (tuṁ āvīś) - 'You will come'; તે કરશે (te karśe) - 'He will do'; અમે મળીશું (ame "
  "maḷīśuṁ) - 'We will meet'; તમે લખશો (tame lakhśo) - 'You will write'; તેઓ રમશે (teo ramśe) "
  "- 'They will play'. PROGRESSIVE: હું વાંચી રહ્યો છું (huṁ vā̃cī rahyo chuṁ) - 'I am reading "
  "(right now)'; તે રાંધી રહી છે (te rā̃dhī rahī che) - 'She is cooking (right now)'. PERFECT: "
  "હું ખાઈ ચૂક્યો છું (huṁ khāī cūkyo chuṁ) - 'I have eaten'; તે આવી ચૂકી છે (te āvī cūkī che) - "
  "'She has arrived'. CONDITIONAL: જો વરસાદ પડે તો હું નહીં જાઉં (jo varsād paḍe to huṁ nahī̃ "
  "jāuṁ) - 'If it rains, I will not go'; તે આવત તો મજા આવત (te āvat to majā āvat) - 'If he "
  "had come, it would have been fun'."),
 "how_it_works": (
  "This record is the tense engine room: present, past (with the ergative flip for "
  "transitive verbs), future, progressive, perfect and conditional - each with full "
  "sentences. Take one verb (લખવું) and run it through every tense aloud: હું લખું છું, મેં "
  "લખ્યું, હું લખીશ. The ergative past is the summit - practice until મેં/તેણે feels "
  "automatic."),
 "key_points": [
  "Present: હું ખાઉં છું, તું ખાય છે, તે ખાય છે, અમે ખાઈએ છીએ, તમે ખાઓ છો, તેઓ ખાય છે.",
  "Past intransitive agrees with subject: હું ગયો (m) / ગઈ (f).",
  "Past transitive is ergative: મેં પત્ર લખ્યો - verb agrees with the object.",
  "Future: હું જઈશ, તે કરશે, અમે મળીશું, તમે લખશો.",
  "Progressive: વાંચી રહ્યો છું - 'am reading right now'.",
  "Perfect: ખાઈ ચૂક્યો છું - 'have eaten'.",
  "Conditional: જો... તો... - 'if... then...'.",
  "મેં પત્ર લખ્યો (mẽ patra lakhyo) - 'I wrote the letter'.",
 ],
 "requirements": [
  "Conjugate લખવું, જવું, કરવું through present, past and future.",
  "Convert ten present sentences to past (watch the ergative flip).",
  "Make five જો... તો... conditional sentences.",
 ],
 "standards": [
  "Standard Gujarati verb morphology (Cardona & Suthar 2003)",
 ],
 "citations": [
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003. Verb section.",
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Tense chapters.",
 ],
 "sig_lens": (
  "Through the Signature lens tenses are his original Signature time instruments: present "
  "his live feed, the ergative past his completed-action stamp, future his forward gear, "
  "the conditional his what-if engine. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 22
{
 "key": "qa", "name": "Gujarati Questions and Answers",
 "group": "Advanced", "ladder": 22, "ladder_rank": 7, "ladder_tier": "advanced",
 "description": (
  "Twenty question-and-answer pairs covering who, what, where, when, why and how. 1. Q: "
  "તમારું નામ શું છે? (tamāruṁ nām śuṁ che?) - 'What is your name?' A: મારું નામ રવિ છે (māruṁ "
  "nām ravi che) - 'My name is Ravi'. 2. Q: તમે ક્યાં રહો છો? (tame kyā̃ raho cho?) - 'Where do "
  "you live?' A: હું સુરતમાં રહું છું (huṁ suratmā̃ rahuṁ chuṁ) - 'I live in Surat'. 3. Q: તું "
  "ક્યારે આવીશ? (tuṁ kyāre āvīś?) - 'When will you come?' A: હું કાલે આવીશ (huṁ kāle āvīś) - "
  "'I will come tomorrow'. 4. Q: આ શું છે? (ā śuṁ che?) - 'What is this?' A: આ મારી ચોપડી છે "
  "(ā mārī copḍī che) - 'This is my book'. 5. Q: કોણ આવ્યું? (koṇ āvyuṁ?) - 'Who came?' A: "
  "મારો મિત્ર આવ્યો (māro mitra āvyo) - 'My friend came'. 6. Q: તું કેમ રડે છે? (tuṁ kem raḍe "
  "che?) - 'Why are you crying?' A: હું દુઃખી છું (huṁ duḥkhī chuṁ) - 'I am sad'. 7. Q: આ કેવી "
  "રીતે બનાવ્યું? (ā kevī rīte banāvyuṁ?) - 'How did you make this?' A: મહેનતથી બનાવ્યું "
  "(mahenatthī banāvyuṁ) - 'I made it with effort'. 8. Q: તને ગુજરાતી આવડે છે? (tane gujarātī "
  "āvaḍe che?) - 'Do you know Gujarati?' A: હા, થોડું થોડું આવડે છે (hā, thoḍuṁ thoḍuṁ āvaḍe "
  "che) - 'Yes, a little'. 9. Q: કેટલા વાગ્યા? (keṭlā vāgyā?) - 'What time is it?' A: ચાર "
  "વાગ્યા (cār vāgyā) - 'It is four o’clock'. 10. Q: ટ્રેન ક્યારે જશે? (ṭren kyāre jaśe?) - "
  "'When will the train leave?' A: છ વાગ્યે જશે (cha vāgye jaśe) - 'It will leave at six'. "
  "11. Q: તું શું કરે છે? (tuṁ śuṁ kare che?) - 'What are you doing?' A: હું વાંચું છું (huṁ "
  "vā̃cuṁ chuṁ) - 'I am reading'. 12. Q: શું તું આવીશ? (śuṁ tuṁ āvīś?) - 'Will you come?' A: "
  "હા, જરૂર આવીશ (hā, jarūr āvīś) - 'Yes, I will certainly come'. 13. Q: કોની સાથે જઈશ? "
  "(konī sāthe jaīś?) - 'With whom will you go?' A: મારા ભાઈ સાથે (mārā bhāī sāthe) - 'With "
  "my brother'. 14. Q: ક્યાંથી આવો છો? (kyā̃thī āvo cho?) - 'Where are you coming from?' A: "
  "બજારથી આવું છું (bajārthī āvuṁ chuṁ) - 'I am coming from the market'. 15. Q: શા માટે મોડું "
  "થયું? (śā māṭe moḍuṁ thayuṁ?) - 'Why are you late?' A: બસ મોડી હતી (bas moḍī hatī) - 'The "
  "bus was late'. 16. Q: તને શું ભાવે છે? (tane śuṁ bhāve che?) - 'What do you like?' A: મને "
  "કેરી ભાવે છે (mane kerī bhāve che) - 'I like mangoes'. 17. Q: કેટલું દૂર છે? (keṭluṁ dūr "
  "che?) - 'How far is it?' A: બે કિલોમીટર દૂર છે (be kilomīṭar dūr che) - 'It is two "
  "kilometers away'. 18. Q: આ કોનું છે? (ā konuṁ che?) - 'Whose is this?' A: આ મારું છે (ā "
  "māruṁ che) - 'This is mine'. 19. Q: તું કેમ છો? (tuṁ kem cho?) - 'How are you?' A: હું "
  "મજામાં છું (huṁ majāmā̃ chuṁ) - 'I am fine'. 20. Q: ફરી ક્યારે મળીશું? (pharī kyāre "
  "maḷīśuṁ?) - 'When will we meet again?' A: આવતા રવિવારે (āvatā ravivāre) - 'Next Sunday'."),
 "how_it_works": (
  "This record drills the conversation loop: ask, answer, ask back. Twenty pairs cover "
  "every question word - શું, કોણ, ક્યાં, ક્યારે, કેમ, કેવી રીતે, કેટલું, કોનું. Practice with "
  "a partner: one reads the Q, the other answers without looking, then swap. Answer in "
  "full sentences - મારું નામ રવિ છે, not just રવિ."),
 "key_points": [
  "શું (what), કોણ (who), ક્યાં (where), ક્યારે (when), કેમ/શા માટે (why), કેવી રીતે (how).",
  "કેટલું (how much/far), કોનું (whose), કોની સાથે (with whom).",
  "તને ગુજરાતી આવડે છે? - 'Do you know Gujarati?' - આવડવું = to know how.",
  "Answer in full sentences: હા, જરૂર આવીશ - not just હા.",
  "કેટલા વાગ્યા? - 'What time is it?'",
  "ફરી ક્યારે મળીશું? - 'When will we meet again?'",
 ],
 "requirements": [
  "Ask and answer all twenty with a partner, then solo.",
  "Interview an imaginary person: name, home, work, likes.",
  "Answer every question with a full sentence, never one word.",
 ],
 "standards": [
  "Standard Gujarati interrogative constructions",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Question chapters.",
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens questions and answers are his original Signature dialogue "
  "instruments: each question word a probe, each full-sentence answer a completed "
  "circuit. Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 23
{
 "key": "commands", "name": "Gujarati Commands and Requests",
 "group": "Advanced", "ladder": 23, "ladder_rank": 7, "ladder_tier": "advanced",
 "description": (
  "Twenty imperatives and polite requests, informal vs formal. Informal (તું, close): 1. બેસ "
  "(bes) - 'Sit'. 2. ઊભો થા (ūbho thā) - 'Stand up' (to a male). 3. અહીં આવ (ahī̃ āv) - 'Come "
  "here'. 4. જા (jā) - 'Go'. 5. ખા (khā) - 'Eat'. Formal/polite (તમે): 6. બેસો (beso) - "
  "'Please sit'. 7. અંદર આવો (andar āvo) - 'Please come in'. 8. બહાર જાઓ (bahār jāo) - "
  "'Please go outside'. 9. ધીમે બોલો (dhīme bolo) - 'Please speak slowly'. 10. ફરી બોલો "
  "(pharī bolo) - 'Please say it again'. Polite requests with કરજો/આપજો: 11. મદદ કરજો (madad "
  "karjo) - 'Please help'. 12. પાણી આપજો (pāṇī āpjo) - 'Please give water'. 13. રાહ જોજો "
  "(rāh jojo) - 'Please wait'. 14. માફ કરજો (māph karjo) - 'Please forgive me'. 15. જરા "
  "ઊભા રહેજો (jarā ūbhā rahejo) - 'Please hold on a moment'. Negative commands: 16. અહીં ન "
  "બેસ (ahī̃ na bes) - 'Do not sit here' (informal). 17. ઘોંઘાટ ન કરો (ghoṅghāṭ na karo) - "
  "'Do not make noise' (formal). 18. મોડું ન કરશો (moḍuṁ na karśo) - 'Please do not be late'. "
  "Suggestions (ીએ): 19. ચાલો, જઈએ (cālo, jaīe) - 'Come on, let us go'. 20. આપણે ચા પીએ "
  "(āpaṇe cā pīe) - 'Let us have tea'. Rule: stem alone is informal (બેસ), stem + ો is "
  "formal (બેસો), stem + જો is a soft request (બેસજો)."),
 "how_it_works": (
  "This record teaches command power with manners: three levels - blunt informal (બેસ), "
  "polite formal (બેસો), soft request (બેસજો) - plus negatives and group suggestions. "
  "Gujarati politeness lives in these endings. Drill: give the same order at all three "
  "levels - જા / જાઓ / જજો - and feel the temperature change."),
 "key_points": [
  "બેસ (informal) / બેસો (formal) / બેસજો (soft request) - three command levels.",
  "Default to the -ો form with anyone you do not know well.",
  "Negatives: ન/નહીં before the verb - ઘોંઘાટ ન કરો.",
  "Suggestions use -ીએ: ચાલો, જઈએ - 'Come on, let us go'.",
  "મદદ કરજો - 'Please help'; પાણી આપજો - 'Please give water'.",
  "માફ કરજો - 'Please forgive me'.",
 ],
 "requirements": [
  "Give five orders at all three politeness levels.",
  "Issue five negative commands, formal and informal.",
  "Make five group suggestions with -ીએ.",
 ],
 "standards": [
  "Standard Gujarati imperative morphology",
 ],
 "citations": [
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003. Imperative section.",
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens commands are his original Signature control instruments: "
  "the bare stem a direct switch, -ો a polite relay, -જો a soft request dial, negatives "
  "the off switch. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 24
{
 "key": "descriptions", "name": "Describing People and Places in Gujarati",
 "group": "Advanced", "ladder": 24, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Twenty detailed descriptive sentences. 1. મારો મિત્ર ઊંચો અને પાતળો છે (māro mitra ū̃co "
  "ane pātaḷo che) - 'My friend is tall and slim'. 2. તેની આંખો કાળી છે (tenī ā̃kho kāḷī "
  "che) - 'Her eyes are black'. 3. તેના વાળ લાંબા છે (tenā vāḷ lā̃bā che) - 'His hair is "
  "long'. 4. દાદીનો ચહેરો પ્રેમાળ છે (dādīno cahero premāḷ che) - 'Grandmother has a loving face"
  "'. 5. બાળક ગોળમટોળ છે (bāḷak goḷamṭoḷ che) - 'The baby is chubby'. 6. શિક્ષક કડક "
  "પણ ન્યાયી છે (śikṣak kaḍak paṇ nyāyī che) - 'The teacher is strict but fair'. 7. તે હંમેશા "
  "હસતો રહે છે (te hameśā hasto rahe che) - 'He is always smiling'. 8. અમદાવાદ મોટું શહેર છે "
  "(amadāvād moṭuṁ śaher che) - 'Ahmedabad is a big city'. 9. સાબરમતી નદી શહેરમાંથી વહે છે "
  "(sābarmatī nadī śahermā̃thī vahe che) - 'The Sabarmati river flows through the city'. 10. "
  "મારું ગામ નાનું પણ સુંદર છે (māruṁ gām nānuṁ paṇ sundar che) - 'My village is small but "
  "beautiful'. 11. ઘરની આસપાસ લીલાં ઝાડ છે (gharnī āspās līlā̃ jhāḍ che) - 'There are green "
  "trees around the house'. 12. બગીચામાં રંગબેરંગી ફૂલો છે (bagīcāmā̃ raṅgaberangī phūlo che) "
  "- 'There are colorful flowers in the garden'. 13. બજારમાં ભીડ છે (bajārmā̃ bhīḍ che) - "
  "'The market is crowded'. 14. રસ્તો પહોળો અને સાફ છે (rasto pahoḷo ane sāph che) - 'The "
  "road is wide and clean'. 15. મંદિર જૂનું અને ભવ્ય છે (mandir jūnuṁ ane bhavya che) - 'The "
  "temple is old and grand'. 16. તળાવનું પાણી ચોખ્ખું છે (taḷāvnuṁ pāṇī cokhkhuṁ che) - 'The "
  "lake water is clear'. 17. સાંજનું આકાશ લાલ છે (sā̃jnuṁ ākāś lāl che) - 'The evening sky is "
  "red'. 18. વરસાદ પછી હવા તાજી છે (varsād pachī havā tajī che) - 'The air is fresh after "
  "rain'. 19. આ પુસ્તક જાડું પણ રસપ્રદ છે (ā pustak jāḍuṁ paṇ rasprad che) - 'This book is "
  "thick but interesting'. 20. મારો દિવસ લાંબો પણ આનંદદાયક હતો (māro divas lāṁbo paṇ "
  "ānandadāyak hato) - 'My day was long but joyful'."),
 "how_it_works": (
  "This record teaches rich description: people (build, face, nature), places (city, "
  "village, market, temple, lake), and things - each sentence stacking two adjectives or "
  "a contrast with પણ ('but'). Describe three people you know and three places you love, "
  "using the પણ-contrast at least twice."),
 "key_points": [
  "Stack adjectives: ઊંચો અને પાતળો - 'tall and slim'.",
  "પણ ('but') builds contrast: નાનું પણ સુંદર - 'small but beautiful'.",
  "People: build, eyes, hair, face, nature (હસતો, કડક, ન્યાયી).",
  "Places: અમદાવાદ, સાબરમતી નદી, ગામ, બજાર, મંદિર, તળાવ.",
  "મારું ગામ નાનું પણ સુંદર છે - 'My village is small but beautiful'.",
  "વરસાદ પછી હવા તાજી છે - 'The air is fresh after rain'.",
 ],
 "requirements": [
  "Describe three people with two adjectives each.",
  "Describe three places with a પણ-contrast each.",
  "Describe today's sky, air and light in three sentences.",
 ],
 "standards": [
  "Standard Gujarati descriptive constructions",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens descriptions are his original Signature portrait instruments: "
  "adjectives his palette, પણ his contrast brush, each sentence a finished miniature. "
  "Signature-made teaching, clearly labeled, never presented as an outside authority's "
  "text."),
},
# ================================================================== 25
{
 "key": "story1", "name": "Gujarati Story I: A Day at the Lake",
 "group": "Advanced", "ladder": 25, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "A ten-sentence simple story in Gujarati, each line with English translation. 1. રવિવારે "
  "સવારે હું તળાવે જાઉં છું (ravivāre savāre huṁ taḷāve jāuṁ chuṁ) - 'On Sunday morning I go "
  "to the lake'. 2. તળાવનું પાણી ચોખ્ખું અને શાંત છે (taḷāvnuṁ pāṇī cokhkhuṁ ane śāṁt che) - "
  "'The lake water is clear and calm'. 3. કિનારે લીલું ઘાસ છે (kināre līluṁ ghās che) - "
  "'There is green grass on the bank'. 4. પક્ષીઓ પાણીમાં તરે છે (pakṣīo pāṇīmā̃ tare che) - "
  "'Birds swim in the water'. 5. હું ઝાડ નીચે બેસું છું (huṁ jhāḍ nīce besuṁ chuṁ) - 'I sit "
  "under a tree'. 6. મારો મિત્ર પણ આવે છે (māro mitra paṇ āve che) - 'My friend comes too'. "
  "7. અમે સાથે વાતો કરીએ છીએ (ame sāthe vāto karīe chīe) - 'We chat together'. 8. પછી અમે "
  "નાસ્તો કરીએ છીએ (pachī ame nāsto karīe chīe) - 'Then we have breakfast'. 9. સૂરજ ઊંચે "
  "ચડે છે (sūraj ū̃ce caḍe che) - 'The sun climbs high'. 10. અમે ખુશ થઈને ઘરે જઈએ છીએ (ame "
  "khuś thaīne ghare jaīe chīe) - 'We go home happily'."),
 "how_it_works": (
  "This record is your first full Gujarati story: ten simple present-tense sentences that "
  "flow as one morning. Read it aloud three times - first slowly for pronunciation, then "
  "for meaning, then at story speed. Then retell it without looking, changing one detail "
  "(the day, the friend, the food)."),
 "key_points": [
  "Ten sentences, one flowing morning - all in the simple present.",
  "તળાવ (lake), કિનારો (bank), ઘાસ (grass) - lakeside vocabulary.",
  "પછી (then) links events in sequence.",
  "થઈને (having become) - અમે ખુશ થઈને જઈએ છીએ - 'we go happily'.",
  "રવિવારે સવારે - 'on Sunday morning' - time phrases open stories.",
  "Retell it changing one detail to make it yours.",
 ],
 "requirements": [
  "Read the story aloud three times at increasing speed.",
  "Retell it from memory with one changed detail.",
  "Write two new sentences continuing the story.",
 ],
 "standards": [
  "Standard Gujarati narrative present tense",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Reading sections.",
 ],
 "sig_lens": (
  "Through the Signature lens this story is his original Signature narrative instrument: "
  "ten sentences one morning, each a frame in his film, પછી his cut between scenes. "
  "Signature-made teaching, clearly labeled, never presented as an outside authority's "
  "text."),
},
# ================================================================== 26
{
 "key": "story2", "name": "Gujarati Story II: The Lost Wallet",
 "group": "Advanced", "ladder": 26, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "A ten-sentence story in the past tense, each line with English translation. 1. ગઈકાલે "
  "સાંજે હું બજાર ગયો (gaīkāle sā̃je huṁ bajār gayo; male speaker) - 'Yesterday evening I went to the market' "
  "2. મેં શાક અને ફળ ખરીદ્યાં (mẽ śāk ane phaḷ kharīdyā̃) - 'I bought "
  "vegetables and fruit'. 3. ઘરે આવીને મેં ખિસ્સામાં હાથ નાખ્યો (ghare āvīne mẽ khissāmā̃ "
  "hāth nākhyo) - 'Coming home, I put my hand in my pocket'. 4. મારું પાકીટ નહોતું! (māruṁ "
  "pākīṭ nahotuṁ!) - 'My wallet was not there!' 5. હું ગભરાયો (huṁ gabharāyo) - 'I panicked'. "
  "6. હું તરત બજાર પાછો ગયો (huṁ tarat bajār pācho gayo) - 'I went straight back to the "
  "market'. 7. દુકાનદારે પાકીટ સાચવી રાખ્યું હતું (dukāndāre pākīṭ sācvī rākhyuṁ hatuṁ) - 'The "
  "shopkeeper had kept the wallet safe'. 8. મેં તેનો ખૂબ આભાર માન્યો (mẽ teno khūb ābhār "
  "mānyo) - 'I thanked him warmly'. 9. તેણે કહ્યું, 'પ્રામાણિકતા જ સાચી દોલત છે' (teṇe kahyuṁ, "
  "'prāmāṇiktā ja sācī dolat che') - 'He said, Honesty is the true wealth'. 10. હું ખુશ "
  "થઈને ઘરે પાછો આવ્યો (huṁ khuś thaīne ghare pācho āvyo) - 'I came back home happily'."),
 "how_it_works": (
  "This record runs the past tense through a real story: intransitive past (ગયો, ગભરાયો), "
  "ergative transitive past (મેં ખરીદ્યાં), past perfect (રાખ્યું હતું), and quoted speech. "
  "Read it, then retell it in the present tense - ગઈકાલે becomes આજે, ગયો becomes જાઉં છું - "
  "to feel the tense shift."),
 "key_points": [
  "Intransitive past: હું ગયો (I went), હું ગભરાયો (I panicked).",
  "Ergative past: મેં ખરીદ્યાં (I bought) - verb agrees with the object.",
  "Past perfect: રાખ્યું હતું - 'had kept'.",
  "Quoted speech: તેણે કહ્યું, '...' - 'He said, ...'.",
  "નહોતું - 'was not there' - past negative.",
  "Retell the story in the present tense as a drill.",
 ],
 "requirements": [
  "Read the story aloud, marking every ergative verb.",
  "Retell it in the present tense.",
  "Write a two-line ending of your own in the past tense.",
 ],
 "standards": [
  "Standard Gujarati past-tense narration",
 ],
 "citations": [
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens this past-tense story is his original Signature memory "
  "instrument: each past verb a recorded frame, the ergative flip his editing cut, quoted "
  "speech his playback. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 27
{
 "key": "story3", "name": "Gujarati Story III: Tomorrow's Journey",
 "group": "Advanced", "ladder": 27, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A ten-sentence story in the future and conditional, each line with English translation. "
  "1. કાલે સવારે અમે સફરે જઈશું (kāle savāre ame saphare jaīśuṁ) - 'Tomorrow morning we will "
  "go on a journey'. 2. અમે ટ્રેનમાં બેસીશું (ame ṭrenmā̃ besīśuṁ) - 'We will sit in the train'. "
  "3. બારીમાંથી ખેતરો દેખાશે (bārīmā̃thī khetaro dekhāśe) - 'Fields will be visible from the "
  "window'. 4. બપોરે અમે નવા શહેરે પહોંચીશું (bapore ame navā śahere pahocīśuṁ) - 'At noon we "
  "will reach the new city'. 5. પહેલાં અમે હોટલમાં રૂમ લઈશું (pahelā̃ ame hoṭalmā̃ rūm laīśuṁ) "
  "- 'First we will take a room in the hotel'. 6. પછી અમે બજાર ફરીશું (pachī ame bajār "
  "pharīśuṁ) - 'Then we will roam the market'. 7. સાંજે અમે નદી કિનારે બેસીશું (sā̃je ame "
  "nadī kināre besīśuṁ) - 'In the evening we will sit by the river'. 8. જો વરસાદ પડશે તો અમે "
  "હોટલમાં જ રોકાઈશું (jo varsād paḍśe to ame hoṭalmā̃ ja rokāīśuṁ) - 'If it rains, we will "
  "stay right in the hotel'. 9. બીજા દિવસે અમે પાછા આવીશું (bījā divase ame pāchā āvīśuṁ) - "
  "'The next day we will come back'. 10. આ સફર યાદગાર રહેશે (ā saphar yādgār raheśe) - "
  "'This journey will be memorable'."),
 "how_it_works": (
  "This record drives the future tense through a journey: -ીશ/-શે/-શું endings, the "
  "જો... તો... conditional for plans with a backup, and time markers (કાલે, બપોરે, સાંજે, "
  "બીજા દિવસે). Plan your own real or imaginary trip in ten future-tense sentences - "
  "કાલે હું... જઈશ - and the endings will lock in."),
 "key_points": [
  "Future endings: હું જઈશ, તે કરશે, અમે જઈશું, તમે કરશો.",
  "જો વરસાદ પડશે તો... - 'If it rains, then...' - the conditional plan.",
  "Time markers order the story: કાલે, બપોરે, સાંજે, બીજા દિવસે.",
  "પહેલાં... પછી... - 'first... then...' - sequence words.",
  "બારીમાંથી ખેતરો દેખાશે - passive-like 'will be visible'.",
  "Plan your own ten-sentence future trip.",
 ],
 "requirements": [
  "Conjugate જવું fully in the future tense aloud.",
  "Write a ten-sentence future plan for your own trip.",
  "Add one જો... તો... backup plan to your story.",
 ],
 "standards": [
  "Standard Gujarati future and conditional",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Future chapter.",
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens this future story is his original Signature planning "
  "instrument: each -ીશ a forward gear, the conditional his contingency engine, the "
  "journey his roadmap. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 28
{
 "key": "idioms", "name": "Gujarati Idioms and Proverbs",
 "group": "Advanced", "ladder": 28, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Twenty Gujarati idioms and proverbs - literal translation, real meaning, and an example "
  "sentence each. 1. જેવું વાવો તેવું લણો (jevuṁ vāvo tevuṁ laṇo) - lit. 'As you sow, so you "
  "reap' - meaning: actions have consequences. Ex: મહેનત કર, જેવું વાવીશ તેવું લણીશ (mahenat "
  "kar, jevuṁ vāviś tevuṁ laṇiś) - 'Work hard; as you sow, so you shall reap'. 2. દૂરના ઢોલ "
  "વાગે મીઠા (dūrnā ḍhol vāge mīṭhā) - lit. 'Distant drums sound sweet' - meaning: things look "
  "better from far away. Ex: પરદેશનાં વખાણ ન કર, દૂરના ઢોલ વાગે મીઠા (pardeśnā̃ vakhāṇ na "
  "kar, dūrnā ḍhol vāge mīṭhā) - 'Do not praise foreign lands; distant drums sound sweet'. 3. "
  "હાથીના દાંત ખાવાના જુદા ને બતાવવાના જુદા (hāthīnā dā̃t khāvānā judā ne batāvvānā judā) - "
  "lit. 'An elephant's eating teeth differ from its showing teeth' - meaning: hypocrisy, "
  "saying one thing and doing another. 4. નાચ ન જાણે આંગણ વાંકું (nāc na jāṇe āṅgaṇ vā̃kuṁ) "
  "- lit. 'One who cannot dance blames the courtyard' - meaning: blaming tools for one's own "
  "failure. 5. જ્યાં ચાહ ત્યાં રાહ (jyā̃ cāh tyā̃ rāh) - lit. 'Where there is desire, there is "
  "a path' - meaning: where there is a will, there is a way. 6. ખાલી ચણો વાગે ઘણો (khālī "
  "caṇo vāge ghaṇo) - lit. 'An empty pot makes much noise' - meaning: empty people boast "
  "most. 7. ઊંટના મોંમાં જીરું (ū̃ṭnā mõmā̃ jīruṁ) - lit. 'Cumin in a camel's mouth' - "
  "meaning: far too little for the need. 8. ધીરજનાં ફળ મીઠાં (dhīrajnā̃ phaḷ mīṭhā̃) - lit. "
  "'Patience bears sweet fruit' - meaning: patience is rewarded. 9. મોંઘું રડે એક વાર, સસ્તું "
  "રડે વારંવાર (moṅghuṁ raḍe ek vār, sastuṁ raḍe vāraṁvār) - lit. 'The expensive cries once, "
  "the cheap cries again and again' - meaning: buy quality once rather than cheap twice. 10. "
  "કર ભલા તો હો ભલા (kar bhalā to ho bhalā) - lit. 'Do good, and good will happen' - meaning: "
  "goodness returns to the giver. 11. લોભે લક્ષણ જાય (lobhe lakṣaṇ jāy) - lit. 'Greed ruins "
  "character' - meaning: greed destroys virtue. 12. દૂધનું દૂધ ને પાણીનું પાણી (dūdhnuṁ dūdh "
  "ne pāṇīnuṁ pāṇī) - lit. 'Milk's milk and water's water' - meaning: fair judgment "
  "separating right from wrong. 13. જે ગરજે છે તે વરસતા નથી (je garje che te varastā nathī) "
  "- lit. 'Those who thunder do not rain' - meaning: big talkers rarely act. 14. ચોરની "
  "દાઢીમાં તણખલું (cornī dāḍhīmā̃ taṇkhluṁ) - lit. 'A straw in the thief's beard' - meaning: "
  "a guilty conscience shows. 15. મહેનતનું ફળ મીઠું (mahenatnuṁ phaḷ mīṭhuṁ) - lit. 'Hard "
  "work's fruit is sweet' - meaning: effort pays. 16. ટીપે ટીપે સરોવર ભરાય (ṭīpe ṭīpe sarovar "
  "bharāy) - lit. 'Drop by drop the lake fills' - meaning: small efforts accumulate. 17. "
  "વહેતા પાણીમાં હાથ ધોવા (vahetā pāṇīmā̃ hāth dhovā) - lit. 'To wash hands in flowing water' "
  "- meaning: to seize an opportunity. 18. આંધળામાં કાણો રાજા (ā̃dhaḷāmā̃ kāṇo rājā) - lit. "
  "'Among the blind, the one-eyed is king' - meaning: modest skill shines among the "
  "unskilled. 19. દીવા તળે અંધારું (dīvā taḷe ãdhāruṁ) - lit. 'Darkness beneath the lamp' - "
  "meaning: faults nearest home go unseen. 20. ઘર ફૂટે ઘર જાય (ghar phūṭe ghar jāy) - lit. "
  "'A divided house falls' - meaning: disunity destroys from within."),
 "how_it_works": (
  "This record teaches you to speak like a native: twenty proverbs with their literal "
  "image, their real meaning, and a sentence showing use. Learn five at a time - say the "
  "Gujarati, picture the literal scene (an elephant's two sets of teeth!), then use it in "
  "the example sentence. Proverbs are the spice; sprinkle, do not pour."),
 "key_points": [
  "જેવું વાવો તેવું લણો - 'As you sow, so shall you reap'.",
  "દૂરના ઢોલ વાગે મીઠા - 'Distant drums sound sweet' (grass is greener).",
  "હાથીના દાંત... - the hypocrisy proverb with its vivid image.",
  "ઊંટના મોંમાં જીરું - 'a drop in the ocean'.",
  "ટીપે ટીપે સરોવર ભરાય - 'drop by drop the lake fills'.",
  "દીવા તળે અંધારું - 'darkness beneath the lamp'.",
  "Learn five at a time: Gujarati, literal picture, real meaning, example.",
  "મહેનતનું ફળ મીઠું - 'Hard work's fruit is sweet'.",
 ],
 "requirements": [
  "Learn five proverbs fully: say, picture, use.",
  "Use three proverbs in real conversation this week.",
  "Explain one proverb's literal image to someone else.",
 ],
 "standards": [
  "Documented Gujarati proverbial usage",
 ],
 "citations": [
  "Gujarati proverb collections (standard published કહેવતો compilations).",
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens proverbs are his original Signature wisdom instruments: "
  "each a compressed life-lesson, the literal image its casing, the meaning its payload. "
  "Signature-made teaching, clearly labeled, never presented as an outside authority's "
  "text."),
},
# ================================================================== 29
{
 "key": "register", "name": "Formal and Polite Registers in Gujarati",
 "group": "Advanced", "ladder": 29, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Fifteen formal vs informal pairs for letters, business and elders, with translations. "
  "1. Informal: તું ક્યાં જાય છે? (tuṁ kyā̃ jāy che?) - 'Where are you going?' / Formal: તમે "
  "ક્યાં જાઓ છો? (tame kyā̃ jāo cho?) - 'Where are you going?' 2. Informal: તારું નામ શું? "
  "(tāruṁ nām śuṁ?) - 'What's your name?' / Formal: તમારું નામ શું છે? (tamāruṁ nām śuṁ che?) "
  "- 'What is your name?' 3. Informal: બેસ (bes) - 'Sit' / Formal: બિરાજો / બેસો (birājo / "
  "beso) - 'Please be seated'. 4. Informal: પાણી આપ (pāṇī āp) - 'Give water' / Formal: પાણી "
  "આપશો? (pāṇī āpśo?) - 'Would you give some water?' 5. Informal: મને ખબર નથી (mane khabar "
  "nathī) - 'I don't know' / Formal: મને જાણ નથી (mane jāṇ nathī) - 'I do not know'. 6. "
  "Informal: જા (jā) - 'Go' / Formal: પધારો (padhāro) - 'Please come in / proceed' (honorific). "
  "7. Informal: શું થયું? (śuṁ thayuṁ?) - 'What happened?' / Formal: શું થયું છે? (śuṁ thayuṁ "
  "che?) - 'What has happened?' 8. Business letter opening (formal): પ્રતિ, માનનીય સાહેબ "
  "(prati, mānnīy sāheb) - 'To: Respected Sir' / Informal note: હેલો રવિ (helo ravi) - 'Hello "
  "Ravi'. 9. Formal closing: આપનો વિશ્વાસુ (āpno viśvāsu) - 'Yours faithfully' / Informal: "
  "તારો મિત્ર (tāro mitra) - 'Your friend'. 10. Formal request: મહેરબાની કરીને જણાવશો "
  "(maherbānī karīne jaṇāvśo) - 'Kindly inform' / Informal: કહેજે (kaheje) - 'Tell me'. 11. "
  "To elders: તમે કેમ છો? (tame kem cho?) - 'How are you?' (never તું to elders) / To friends: "
  "તું કેમ છે? (tuṁ kem che?) - 'How are you?' 12. Formal apology: ક્ષમા કરશો (kṣamā karśo) - "
  "'Please forgive me' / Informal: સોરી (sorī) - 'Sorry'. 13. Formal thanks: આપનો ખૂબ ખૂબ "
  "આભાર (āpno khūb khūb ābhār) - 'Thank you very much' / Informal: થેન્ક્સ (thenks) - "
  "'Thanks'. 14. Business: મીટિંગ ક્યારે રાખીશું? (mīṭiṁg kyāre rākhīśuṁ?) - 'When shall we "
  "hold the meeting?' / Casual: ક્યારે મળીએ? (kyāre maḷīe?) - 'When do we meet?' 15. Formal "
  "farewell: ફરી મળવાની આશા રાખું છું (pharī maḷvānī āśā rākhuṁ chuṁ) - 'I hope we meet again' "
  "/ Informal: ચલ, આવજે (cal, āvje) - 'Bye, see you'. Rule: તમે + -ો verbs + આપ/મહેરબાની = "
  "formal; તું + bare stem = intimate only."),
 "how_it_works": (
  "This record is your register switchboard: fifteen pairs showing the same meaning at "
  "informal and formal voltage. The rule is simple - તમે with -ો endings for respect, તું "
  "with bare stems only for the closest circle. Practice flipping each pair both ways, "
  "then write a three-line formal request and a three-line friendly note."),
 "key_points": [
  "તમે + -ો = formal; તું + bare stem = intimate (friends, children only).",
  "Never use તું with elders or strangers.",
  "પધારો (padhāro) - the honorific 'please come/proceed'.",
  "Formal letter: પ્રતિ, માનનીય સાહેબ ... આપનો વિશ્વાસુ.",
  "મહેરબાની કરીને / કૃપા કરીને soften any formal request.",
  "ક્ષમા કરશો - formal apology; માફ કરજો - standard polite.",
  "તમારું નામ શું છે? vs તારું નામ શું? - feel the distance change.",
 ],
 "requirements": [
  "Convert five informal sentences to formal register.",
  "Write a three-line formal request (leave, meeting, information).",
  "Address an imaginary elder for two minutes using only તમે.",
 ],
 "standards": [
  "Standard Gujarati polite-register conventions",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Register sections.",
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003.",
 ],
 "sig_lens": (
  "Through the Signature lens register is his original Signature voltage control: તમે/-ો "
  "high respect current, તું/bare stem intimate low current, પધારો the honorific surge. "
  "Signature-made teaching, clearly labeled, never presented as an outside authority's "
  "text."),
},
# ================================================================== 30
{
 "key": "complex", "name": "Compound and Complex Sentences in Gujarati",
 "group": "Advanced", "ladder": 30, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Fifteen long sentences with clauses and connectors, parsed and translated. 1. હું બજાર "
  "ગયો અને શાક ખરીદ્યું (huṁ bajār gayo ane śāk kharīdyuṁ) - 'I went to the market and bought "
  "vegetables' [અને = and]. 2. તે થાકેલો હતો પણ તેણે કામ પૂરું કર્યું (te thākelo hato paṇ "
  "teṇe kām pūruṁ karyuṁ) - 'He was tired, but he finished the work' [પણ = but]. 3. જો તું "
  "મહેનત કરીશ તો સફળ થઈશ (jo tuṁ mahenat karīś to saphaḷ thaīś) - 'If you work hard, you will "
  "succeed' [જો... તો... = if... then...]. 4. જે છોકરો ત્યાં ઊભો છે તે મારો ભાઈ છે (je chokro "
  "tyā̃ ūbho che te māro bhāī che) - 'The boy who is standing there is my brother' [જે... "
  "તે... = who...]. 5. મેં જે પુસ્તક ખરીદ્યું તે ખૂબ સારું છે (mẽ je pustak kharīdyuṁ te khūb "
  "sāruṁ che) - 'The book that I bought is very good' [relative clause]. 6. જ્યારે હું નાનો "
  "હતો ત્યારે અમે ગામમાં રહેતા (jyāre huṁ nāno hato tyāre ame gāmmā̃ rahetā) - 'When I was "
  "small, we lived in the village' [જ્યારે... ત્યારે... = when... then...]. 7. કારણ કે વરસાદ "
  "પડતો હતો, અમે ઘરે રોકાયા (kāraṇ ke varsād paḍto hato, ame ghare rokāyā) - 'Because it was "
  "raining, we stayed home' [કારણ કે = because]. 8. તે એટલો ઝડપથી દોડ્યો કે બધા જોતા રહી "
  "ગયા (te eṭlo jhaḍapthī doḍyo ke badhā jotā rahī gayā) - 'He ran so fast that everyone kept "
  "watching' [એટલો... કે... = so... that...]. 9. તું આવે કે ન આવે, હું જઈશ (tuṁ āve ke na "
  "āve, huṁ jaīś) - 'Whether you come or not, I will go' [કે = or/whether]. 10. પહેલાં હાથ "
  "ધુઓ પછી જમો (pahelā̃ hāth dhuo pachī jamo) - 'First wash your hands, then eat' [પહેલાં... "
  "પછી... = first... then...]. 11. જેમ જેમ સમય જાય છે તેમ તેમ શીખું છું (jem jem samay jāy "
  "che tem tem śīkhuṁ chuṁ) - 'As time passes, I keep learning' [જેમ... તેમ... = as... so...]. "
  "12. તે માત્ર શિક્ષક નથી, માર્ગદર્શક પણ છે (te mātra śikṣak nathī, mārgadarśak paṇ che) - "
  "'He is not just a teacher, but also a guide' [માત્ર... પણ... = not only... but also...]. "
  "13. ભલે વરસાદ પડે, કાર્યક્રમ થશે (bhale varsād paḍe, kāryakram thaśe) - 'Even if it rains, "
  "the program will happen' [ભલે = even if]. 14. હું એટલા માટે આવ્યો કે તને મળું (huṁ eṭlā "
  "māṭe āvyo ke tane maḷuṁ) - 'I came so that I could meet you' [એટલા માટે... કે... = so "
  "that]. 15. જે થવાનું હતું તે થયું, હવે આગળ વધો (je thavānuṁ hatuṁ te thayuṁ, have āgaḷ "
  "vadho) - 'What had to happen happened; now move forward' [acceptance + command]."),
 "how_it_works": (
  "This record builds skyscraper sentences: fifteen complex builds with the connector "
  "bracketed and parsed - અને, પણ, જો... તો, જે... તે, જ્યારે... ત્યારે, કારણ કે, એટલો... કે, "
  "જેમ... તેમ. Take each one apart (find the two clauses, name the connector), then "
  "rebuild it with your own nouns. Master જે... તે... and જો... તો... and you can say "
  "almost anything."),
 "key_points": [
  "અને (and), પણ (but), કે (that/or), કારણ કે (because).",
  "જો... તો... (if... then...); જ્યારે... ત્યારે... (when... then...).",
  "જે... તે... (who/which... that...) - the relative clause frame.",
  "એટલો... કે... (so... that...); જેમ... તેમ... (as... so...).",
  "ભલે (even if); એટલા માટે... કે... (so that).",
  "જે છોકરો ત્યાં ઊભો છે તે મારો ભાઈ છે - 'The boy who stands there is my brother'.",
 ],
 "requirements": [
  "Parse all fifteen: name both clauses and the connector.",
  "Rebuild five with your own nouns and verbs.",
  "Write three જે... તે... and three જો... તો... sentences.",
 ],
 "standards": [
  "Standard Gujarati complex-sentence constructions",
 ],
 "citations": [
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003. Syntax section.",
 ],
 "sig_lens": (
  "Through the Signature lens complex sentences are his original Signature architecture "
  "instruments: connectors his joints and beams, relative clauses his extensions, each "
  "fifteen-sentence set a finished structure. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 31
{
 "key": "dialogue1", "name": "Conversation in Gujarati: At the Market",
 "group": "Advanced", "ladder": 31, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A twenty-line bilingual market dialogue (buyer = ખરીદનાર, seller = વેચનાર), annotated. "
  "1. ખરીદનાર: નમસ્તે! શાક તાજું છે? (namaste! śāk tājuṁ che?) - 'Hello! Are the vegetables "
  "fresh?' [greeting + freshness check]. 2. વેચનાર: નમસ્તે! એકદમ તાજું, સવારે જ આવ્યું "
  "(namaste! ekdam tājuṁ, savāre ja āvyuṁ) - 'Hello! Completely fresh, arrived this morning' "
  "[reassurance]. 3. ખરીદનાર: ટામેટા કેટલાના? (ṭāmeṭā keṭlānā?) - 'How much are the tomatoes?' "
  "[price ask]. 4. વેચનાર: ચાળીસ રૂપિયા કિલો (cāḷīs rūpiyā kilo) - 'Forty rupees a kilo' "
  "[quote]. 5. ખરીદનાર: બહુ મોંઘું! ત્રીસમાં આપો (bahu moṅghuṁ! trīsmā̃ āpo) - 'Too expensive! "
  "Give it for thirty' [bargain]. 6. વેચનાર: ત્રીસમાં નહીં થાય, પાંત્રીસ છેલ્લા (trīsmā̃ nahī̃ "
  "thāy, pā̃trīs chellā) - 'Not for thirty; thirty-five is final' [counter]. 7. ખરીદનાર: "
  "બરાબર, એક કિલો આપો (barābar, ek kilo āpo) - 'Okay, give one kilo' [deal]. 8. વેચનાર: બીજું "
  "કંઈ જોઈએ? (bījuṁ kaī̃ joīe?) - 'Do you need anything else?' [upsell]. 9. ખરીદનાર: અડધો "
  "કિલો ડુંગળી અને લીંબુ (aḍdho kilo ḍuṅgaḷī ane līṁbu) - 'Half a kilo of onions and lemons' "
  "[add]. 10. વેચનાર: લીંબુ મફત, ડુંગળી પંદર રૂપિયા (līṁbu maphat, ḍuṅgaḷī pandar rūpiyā) - 'Lemons "
  "free, onions fifteen rupees' [goodwill]. 11. ખરીદનાર: વાહ! આભાર (vāh! ābhār) - 'Wow! Thanks' "
  "[thanks]. 12. વેચનાર: કુલ પચાસ રૂપિયા (kul pacās rūpiyā) - 'Fifty rupees total' [35 + 15] 13. ખરીદનાર: આ રહ્યા પચાસ રૂપિયા (ā rahyā pacās "
  "rūpiyā) - 'Here are fifty rupees' [pay]. 14. વેચનાર: થેલીમાં નાખી દઉં? (thelīmā̃ nākhī "
  "dauṁ?) - 'Shall I put it in the bag?' [service]. 15. ખરીદનાર: હા, મહેરબાની (hā, maherbānī) "
  "- 'Yes, please' [accept]. 16. વેચનાર: કાલે નવો માલ આવશે (kāle navo māl āvśe) - 'New stock "
  "comes tomorrow' [invite back]. 17. ખરીદનાર: જરૂર આવીશ (jarūr āvīś) - 'I will surely come' "
  "[promise]. 18. વેચનાર: આવજો! (āvjo!) - 'Goodbye - come again!' [farewell]. 19. ખરીદનાર: "
  "આવજો! (āvjo!) - 'Goodbye!' [farewell]. 20. વેચનાર: ફરી પધારજો! (pharī padhārjo!) - 'Do visit again!' [warm close]"),
 "how_it_works": (
  "This record is a complete market transaction as a play: twenty lines from greeting to "
  "goodbye, each annotated with its move (price ask, bargain, counter, deal). Act it out "
  "with a partner - then swap roles. The bargaining chain in lines 3-7 is the engine; "
  "master it and every Gujarat market opens to you."),
 "key_points": [
  "ટામેટા કેટલાના? - 'How much are the tomatoes?' - price ask.",
  "બહુ મોંઘું! ત્રીસમાં આપો - 'Too expensive! Give it for thirty' - bargain.",
  "પાંત્રીસ છેલ્લા - 'Thirty-five is final' - counter.",
  "બરાબર, એક કિલો આપો - 'Okay, give one kilo' - deal.",
  "લીંબુ મફત - 'Lemons free' - goodwill gesture.",
  "Act it out, then swap buyer/seller roles.",
 ],
 "requirements": [
  "Perform the dialogue with a partner, both roles.",
  "Improvise the same chain for three new items.",
  "Bargain in a real or role-played shop this week.",
 ],
 "standards": [
  "Standard Gujarati market discourse",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens this market dialogue is his original Signature trade "
  "performance: twenty lines one transaction, each move a gear in his negotiation engine. "
  "Signature-made teaching, clearly labeled, never presented as an outside authority's "
  "text."),
},
# ================================================================== 32
{
 "key": "dialogue2", "name": "Conversation in Gujarati: Meeting a Friend",
 "group": "Advanced", "ladder": 32, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A twenty-line bilingual dialogue between two friends (રવિ and સીતા), annotated. 1. "
  "રવિ: અરે સીતા! કેમ છો? (are sītā! kem cho?) - 'Hey Sita! How are you?' [warm greeting]. "
  "2. સીતા: રવિ! મજામાં! તું કેમ છે? (ravi! majāmā̃! tuṁ kem che?) - 'Ravi! Doing well! How "
  "are you?' [return greeting]. 3. રવિ: બસ, મજામાં. ઘણા દિવસે મળ્યા (bas, majāmā̃. ghaṇā "
  "divase maḷyā) - 'Just fine. We meet after many days' [catch-up]. 4. સીતા: હા! શું ચાલે "
  "છે? (hā! śuṁ cāle che?) - 'Yes! What is going on?' [news ask]. 5. રવિ: નવી નોકરી મળી "
  "(navī nokrī maḷī) - 'I got a new job' [news]. 6. સીતા: અરે વાહ! અભિનંદન! (are vāh! "
  "abhinandan!) - 'Oh wow! Congratulations!' [celebrate]. 7. રવિ: આભાર! ચા પીશે? (ābhār! cā "
  "pīśe?) - 'Thanks! Will you have tea?' [offer]. 8. સીતા: હા, જરૂર (hā, jarūr) - 'Yes, "
  "surely' [accept]. 9. રવિ: તો ચાલ, સામેની હોટલમાં જઈએ (to cāl, sāmenī hoṭalmā̃ jaīe) - "
  "'Then come, let us go to the hotel across' [plan]. 10. સીતા: તારું કામ કેવું ચાલે છે? "
  "(tāruṁ kām kevuṁ cāle che?) - 'How is your work going?' [interest]. 11. રવિ: ખૂબ સરસ, "
  "પણ કામ વધારે છે (khūb saras, paṇ kām vadhāre che) - 'Very good, but there is lots of work' "
  "[honest]. 12. સીતા: મહેનતનું ફળ મીઠું (mahenatnuṁ phaḷ mīṭhuṁ) - 'The fruit of hard work is sweet"
  "' [proverb comfort]. 13. રવિ: સાચું કહ્યું! તારો અભ્યાસ કેમ ચાલે? (sācuṁ kahyuṁ! "
  "tāro abhyās kem cāle?) - 'Well said! How are your studies?' [return interest]. 14. સીતા: "
  "પરીક્ષા નજીક છે, તૈયારી ચાલે છે (parīkṣā najīk che, taiyārī cāle che) - 'Exams are near, "
  "preparation is on' [news]. 15. રવિ: શુભેચ્છા! તું જરૂર પાસ થઈશ (śubhecchā! tuṁ jarūr pās "
  "thaīś) - 'Best wishes! You will surely pass' [encourage]. 16. સીતા: આભાર! મળીને આનંદ "
  "થયો (ābhār! maḷīne ānand thayo) - 'Thanks! Nice meeting you' [warmth]. 17. રવિ: મને પણ! "
  "સંપર્કમાં રહેજે (mane paṇ! samparkamā̃ raheje) - 'Me too! Stay in touch' [close]. 18. "
  "સીતા: જરૂર! આવતા રવિવારે મળીએ (jarūr! āvatā ravivāre maḷīe) - 'Surely! Let us meet next "
  "Sunday' [plan]. 19. રવિ: નક્કી! આવજે (nakkī! āvje) - 'Done! Bye' [agree]. 20. સીતા: આવજે! "
  "(āvje!) - 'Bye!' [farewell]."),
 "how_it_works": (
  "This record is friendship in action: twenty lines from surprise meeting to next plan, "
  "with friends using the intimate તું register. Notice the rhythm - greeting, news, "
  "celebration, offer, mutual interest, encouragement, plan, farewell. Perform it, then "
  "improvise your own reunion with different news."),
 "key_points": [
  "ઘણા દિવસે મળ્યા - 'We meet after many days' - reunion opener.",
  "Friends use તું; અરે વાહ! અભિનંદન! celebrates news.",
  "મહેનતનું ફળ મીઠું - proverb as encouragement.",
  "શુભેચ્છા! તું જરૂર પાસ થઈશ - 'Best wishes, you will pass'.",
  "સંપર્કમાં રહેજે - 'Stay in touch'; આવતા રવિવારે મળીએ - plan next.",
  "The rhythm: greet, news, celebrate, offer, interest, encourage, plan, farewell.",
 ],
 "requirements": [
  "Perform the dialogue with a partner, both roles.",
  "Improvise a reunion with your own news.",
  "Use તું naturally with a close friend in role-play.",
 ],
 "standards": [
  "Standard Gujarati friendly discourse",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens this reunion is his original Signature friendship "
  "instrument: twenty lines one bond renewed, the તું register his intimacy setting, the "
  "proverb his encouragement engine. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 33
{
 "key": "dialogue3", "name": "Conversation in Gujarati: Solving a Problem",
 "group": "Advanced", "ladder": 33, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A twenty-line bilingual problem-solving dialogue (અનિલ and મીરા - a missed bus and a "
  "plan B), annotated. 1. અનિલ: અરે! બસ ચૂકી ગઈ! (are! bas cūkī gaī!) - 'Oh no! I missed the "
  "bus!' [problem]. 2. મીરા: શાંત થા, શું થયું? (śāṁt thā, śuṁ thayuṁ?) - 'Calm down, what "
  "happened?' [calm + ask]. 3. અનિલ: છેલ્લી બસ નીકળી ગઈ, હવે શું કરું? (chellī bas nīkaḷī "
  "gaī, have śuṁ karuṁ?) - 'The last bus left; what do I do now?' [explain]. 4. મીરા: "
  "ચિંતા ન કર, ઉપાય છે (cintā na kar, upāy che) - 'Do not worry, there is a solution' "
  "[reassure]. 5. અનિલ: કયો ઉપાય? (kayo upāy?) - 'Which solution?' [ask]. 6. મીરા: રિક્ષા "
  "કરીએ? (rikṣā karīe?) - 'Shall we take a rickshaw?' [suggest 1]. 7. અનિલ: રિક્ષાવાળો બહુ "
  "પૈસા માંગશે (rikṣāvāḷo bahu paisā mā̃gśe) - 'The rickshaw driver will ask for a lot' "
  "[object]. 8. મીરા: તો મારા ભાઈને ફોન કરું? (to mārā bhāīne phon karuṁ?) - 'Then shall I "
  "call my brother?' [suggest 2]. 9. અનિલ: તે કેટલે દૂર છે? (te keṭle dūr che?) - 'How far is "
  "he?' [check]. 10. મીરા: દસ મિનિટમાં આવી જશે (das miniṭmā̃ āvī jaśe) - 'He will come in ten "
  "minutes' [answer]. 11. અનિલ: એ તો સરસ! (e to saras!) - 'That is great!' [accept]. 12. "
  "મીરા: ઊભો રહે, ફોન કરું છું (ūbho rahe, phon karuṁ chuṁ) - 'Wait here, I am calling' "
  "[act]. 13. અનિલ: તારો ખૂબ આભાર (tāro khūb ābhār) - 'Thank you so much' [thanks]. 14. મીરા: "
  "એમાં શું? મિત્રો કામના જ હોય (emā̃ śuṁ? mitro kāmnā ja hoy) - 'What of it? Friends are "
  "for helping' [warmth]. 15. અનિલ: હવે પછી વહેલો નીકળીશ (have pachī vahelo nīkaḷīś) - 'From "
  "now on I will leave early' [lesson]. 16. મીરા: બરાબર! ભાઈ આવી ગયો (barābar! bhāī āvī "
  "gayo) - 'Right! Brother has arrived' [resolve]. 17. અનિલ: નમસ્તે ભાઈ! (namaste bhāī!) - "
  "'Hello, brother!' [greet]. 18. મીરા: ચાલો, બેસીએ (cālo, besīe) - 'Come, let us sit' "
  "[move]. 19. અનિલ: આજે તું ન હોત તો... (āje tuṁ na hot to...) - 'If you had not been here "
  "today...' [gratitude]. 20. મીરા: બસ હવે! ઘરે જઈએ (bas have! ghare jaīe) - 'Enough now! "
  "Let us go home' [close]."),
 "how_it_works": (
  "This record teaches problem-solving talk: state the problem, calm down, propose "
  "options, object, counter-propose, check facts, accept, act, thank, and learn the "
  "lesson. The frame - શું થયું? → ઉપાય છે → તો...? → બરાબર! - works for any crisis. "
  "Perform it, then invent your own problem (lost keys, flat tire) and solve it the "
  "same way."),
 "key_points": [
  "શાંત થા, શું થયું? - 'Calm down, what happened?' - crisis opener.",
  "ચિંતા ન કર, ઉપાય છે - 'Do not worry, there is a solution'.",
  "રિક્ષા કરીએ? / મારા ભાઈને ફોન કરું? - proposing options with -ીએ/-ું.",
  "હવે પછી વહેલો નીકળીશ - 'From now on I will leave early' - the lesson.",
  "એમાં શું? મિત્રો કામના જ હોય - 'Friends are for helping'.",
  "The frame: problem → calm → options → check → act → thanks → lesson.",
 ],
 "requirements": [
  "Perform the dialogue, then swap roles.",
  "Invent a new problem and solve it with the same frame.",
  "Propose three options for a real problem using -ીએ.",
 ],
 "standards": [
  "Standard Gujarati problem-solving discourse",
 ],
 "citations": [
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995.",
 ],
 "sig_lens": (
  "Through the Signature lens this crisis dialogue is his original Signature repair "
  "instrument: the problem a fault report, options his troubleshooting tree, the "
  "resolution his fix verified. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 34
{
 "key": "mastery", "name": "Gujarati Mastery Review and Full Reference",
 "group": "Advanced", "ladder": 34, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The whole database in one teaching summary. ALPHABET: vowels અ આ ઇ ઈ ઉ ઊ ઋ એ ઐ ઓ ઔ અં "
  "અઃ; consonants ક ખ ગ ઘ ઙ ચ છ જ ઝ ઞ ટ ઠ ડ ઢ ણ ત થ દ ધ ન પ ફ બ ભ મ ય ર લ વ ળ શ ષ સ હ; "
  "digits ૦૧૨૩૪૫૬૭૮૯; danda ।. 200 CORE WORDS (sampled across the database): people - માણસ, "
  "સ્ત્રી, છોકરો, છોકરી, બાળક, મિત્ર, પિતા, માતા, ભાઈ, બહેન, દાદા, દાદી, શિક્ષક, ડૉક્ટર, "
  "દુકાનદાર; home - ઘર, ઓરડો, રસોડું, બેઠકખંડ, ટેબલ, ખુરશી, બારી, બારણું, પથારી, બગીચો; food - "
  "ખોરાક, રોટલી, શાક, દાળ, ભાત, ખીચડી, દૂધ, ચા, પાણી, કેરી, મીઠું, ખાંડ; verbs - કરવું, હોવું, "
  "જવું, આવવું, ખાવું, પીવું, બોલવું, વાંચવું, લખવું, જોવું, સૂવું, ઊઠવું, બેસવું, ચાલવું, "
  "દોડવું, આપવું, લેવું, ખરીદવું, બનાવવું, શીખવું, સમજવું; adjectives - સારો, ખરાબ, મોટો, "
  "નાનો, નવો, જૂનો, ગરમ, ઠંડો, મીઠો, સુંદર, ઝડપી, ખુશ; pronouns - હું, તું, તમે, તે, તેઓ, "
  "અમે, આપણે, આ, તે, કોણ, શું, મારો, તારો; numbers - એક, બે, ત્રણ, ચાર, પાંચ, દસ, વીસ, સો, "
  "હજાર, લાખ; time - દિવસ, રાત, સવાર, સાંજ, આજે, કાલે, સોમવાર, રવિવાર; nature - સૂરજ, ચાંદ, "
  "તારો, ઝાડ, ફૂલ, નદી, પહાડ, સમુદ્ર, વરસાદ, પક્ષી, કૂતરો, બિલાડી; body - માથું, આંખ, હાથ, "
  "પગ, પેટ; phrases - નમસ્તે, કેમ છો, આભાર, આવજો, માફ કરજો, કૃપા કરીને. KEY GRAMMAR: SOV "
  "order (હું પાણી પીઉં છું); three genders -ો/-ી/-ું; postpositions માં/પર/થી/ને/નો/સાથે; no "
  "articles; negation નથી/નહીં; questions with શું/કોણ/ક્યાં/ક્યારે/કેમ; ergative past મેં "
  "પત્ર લખ્યો; future હું જઈશ; commands બેસ/બેસો/બેસજો; formal તમે vs intimate તું. PHRASE "
  "TABLES: greetings (નમસ્તે, કેમ છો, આવજો), market (કેટલાનું, મોંઘું, પેક કરો), travel "
  "(ક્યાં, જમણી, ટિકિટ), health (દુઃખે છે, તાવ), emotions (ખુશ, ગુસ્સો, પ્રેમ). PROVERBS: "
  "જેવું વાવો તેવું લણો; દૂરના ઢોલ વાગે મીઠા; ટીપે ટીપે સરોવર ભરાય. FINAL CHECK: say કેમ છો?, "
  "introduce yourself, buy vegetables, give directions, tell the lake story - if all five "
  "flow, the ladder is climbed."),
 "how_it_works": (
  "This record is graduation: the alphabet, 200 core words, the grammar rules, the phrase "
  "tables and the proverbs - the entire database compressed to one page. Use it as your "
  "daily review sheet: read a section, close your eyes, reproduce it. The final check at "
  "the end is your exam - five tasks, all from earlier records."),
 "key_points": [
  "Full alphabet: 13 vowels, 34 consonants, digits ૦-૯, danda ।.",
  "200 core words across people, home, food, verbs, adjectives, pronouns, numbers, time, nature, body, phrases.",
  "Grammar in one breath: SOV, 3 genders, postpositions, નથી/નહીં, ergative past, future -ીશ.",
  "Commands: બેસ/બેસો/બેસજો; register: તમે formal, તું intimate.",
  "Phrase tables: greetings, market, travel, health, emotions.",
  "Proverbs: જેવું વાવો તેવું લણો; દૂરના ઢોલ વાગે મીઠા; ટીપે ટીપે સરોવર ભરાય.",
  "Final check: greet, introduce, shop, direct, tell the story.",
  "The ladder is climbed: foundations (1-10), compounded (11-20), advanced (21-34).",
 ],
 "requirements": [
  "Reproduce the alphabet from memory, then check.",
  "Say all 200 core words in Gujarati from the English list.",
  "Pass the final check: five tasks, no notes.",
 ],
 "standards": [
  "Consolidated Gujarati reference (all prior records)",
  "ISO 639-1:2002 'gu'; ISO 639-3:2007 'guj'; Unicode U+0A80-U+0AFF",
 ],
 "citations": [
  "Cardona, George & Suthar, Babu. Gujarati. In: Cardona, George & Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003.",
  "Dwyer, Rachel. Teach Yourself Gujarati. Hodder & Stoughton; 1995. Complete course.",
  "Masica, Colin P. The Indo-Aryan Languages. Cambridge University Press; 1991.",
 ],
 "sig_lens": (
  "Through the Signature lens this mastery record is his original Signature graduation: "
  "the whole Gujarati instrument laid out on one bench, every word a tool he now owns, "
  "the learner become the speaker. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
]

SIG_TAIL = ("Signature Note: this Signature Edition re-teaches the lesson through "
            "his original Signature method - the same real Gujarati, framed as his own "
            "language instrument. Signature-made, clearly labeled, never presented "
            "as an outside authority's text.")

assert len(ENTRIES) == 34, "template requires exactly 34 records"
assert [e["ladder"] for e in ENTRIES] == list(range(1, 35)), "ladder must be 1-34 in order"
_r = [e["ladder_rank"] for e in ENTRIES]
assert _r == sorted(_r), "ladder_rank must be non-decreasing"
assert all(1 <= x <= 10 for x in _r), "ladder_rank must be 1-10"
_t = [e["ladder_tier"] for e in ENTRIES]
assert _t == ["foundations"] * 10 + ["compounded"] * 10 + ["advanced"] * 14
