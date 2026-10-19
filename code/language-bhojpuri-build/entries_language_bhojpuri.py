#!/usr/bin/env python3
"""Entry content for The Bhojpuri to English Database (language-bhojpuri)
and its Signature edition (language-bhojpuri-signature).

34 ladder-ordered records (ladder_rank 1-34, non-decreasing; tiers
foundations -> compounded -> advanced), each a full fully-formed file per
the 2026-10-09 full-file canon: Bhojpuri content in Devanagari plus a plain
practical transliteration plus English translation plus example sentences.
Sentences are required in EVERY record.

Public records are real, fact-checked Bhojpuri teaching (public-harvest).
Signature records are the same ladder seen through the Signature lens -
his original Signature Language Method - titles suffixed " (Signature
Edition)", src 'signature', clearly labeled Signature-made, never
presented as authentic public record.
"""

SIG_TAIL = ("Signature edition: his original Signature Language Method - "
            "the same ladder reframed as Signature science. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

ENTRIES = [
# ---------------------------------------------------------------- 1 overview
{
"key": "overview",
"name": "Bhojpuri Language Overview",
"group": "overview",
"ladder_rank": 1,
"ladder_tier": "foundations",
"description": (
"Bhojpuri (भोज्पुरी, transliterated 'bhojpuri') is an Indo-Aryan language of the "
"Indo-European family, in the Eastern or Bihari group, spoken natively by more than "
"50 million people - one of the most widely spoken languages on earth that still "
"holds no official status in India. Its heartland is western Bihar and eastern "
"Uttar Pradesh (Purvanchal), with a strong presence across the Nepal Terai, and it "
"is carried worldwide by the descendants of indentured laborers: large Bhojpuri "
"communities thrive in Mauritius, Trinidad and Tobago, Guyana, Suriname, Fiji, and "
"South Africa. The name comes from Bhojpur district of Bihar (the old town of Arrah), "
"the seat of Raja Bhoj. In India Bhojpuri is written in the Devanagari script "
"(भोज्पुरी); its historic hand is Kaithi (कैथी), the script of the Kayastha scribes. "
"The main dialects are Northern Bhojpuri (Gorakhpuri), Western Bhojpuri (Benarsi or "
"Purbi), Southern Bhojpuri (the standard, around Bhojpur and Arrah), and Tharu "
"Bhojpuri; overseas forms include Trinidadian Bhojpuri, Sarnami Hindustani of "
"Suriname, and Mauritian Bhojpuri. Bhojpuri grammar runs on subject-object-verb "
"word order, two genders, two numbers, and postpositions instead of prepositions; "
"unlike Hindi it has no 'ne' ergative marker - past-tense verbs agree with the "
"subject. Example sentences: हम भोज्पुरी बोलत बानी (ham bhojpuri bolat bani - 'I am "
"speaking Bhojpuri'). भोज्पुरी हमार मातृभाषा हऽ (bhojpuri hamar matribhasha ha - "
"'Bhojpuri is my mother tongue'). मॉरीशस में भोज्पुरी बोलल जाला (mauritius men "
"bhojpuri bolal jala - 'Bhojpuri is spoken in Mauritius')."),
"how_it_works": (
"Bhojpuri builds meaning the way the Eastern Indo-Aryan languages do, with its own "
"plainspoken moves. Sentences run subject-object-verb: हम रोटी खात बानी (ham roti "
"khat bani - 'I bread eating am') means 'I am eating bread.' Nouns carry one of two "
"genders and change form with number; adjectives agree with the noun; the verb 'to "
"be' shifts with the person - हम बानी (ham bani, I am), तू बाड़ऽ (tu bara, you are), "
"उ बा (u ba, he/she is). Relationships English marks with prepositions are marked "
"with postpositions after the noun - घर में (ghar men - 'house in') means 'in the "
"house,' रउआ खातिर (raua khatir - 'you for') means 'for you.' The 34 records of this "
"database climb that whole system step by step: script and sound first, then words, "
"then sentences, then real conversation, then the full reference."),
"key_points": [
"Bhojpuri (भोज्पुरी, ISO 639-3 bho, no ISO 639-1 code) is Indo-European > Indo-Iranian > Indo-Aryan > Eastern (Bihari).",
"More than 50 million native speakers; among the largest languages without official status in India.",
"Heartland: western Bihar and eastern Uttar Pradesh (Purvanchal), plus the Nepal Terai.",
"Worldwide diaspora: Mauritius, Trinidad and Tobago, Guyana, Suriname, Fiji, South Africa.",
"Written in Devanagari today; historic script is Kaithi (कैथी).",
"Main dialects: Northern (Gorakhpuri), Western (Benarsi/Purbi), Southern standard (Bhojpur/Arrah), Tharu Bhojpuri.",
"Overseas forms: Trinidadian Bhojpuri, Sarnami Hindustani (Suriname), Mauritian Bhojpuri.",
"Word order is subject-object-verb; postpositions follow the noun.",
"Two genders (masculine, feminine) and two numbers (singular, plural).",
"No 'ne' ergative marker: past-tense verbs agree with the subject, unlike Hindi.",
],
"requirements": [
"No prior knowledge of any South Asian language is needed to start.",
"Learn the Devanagari letters before memorizing long word lists.",
"Say every example sentence aloud - aspiration and nasalization are physical habits.",
],
"standards": [
"ISO 639-3: bho (no ISO 639-1 code assigned)",
"Unicode Devanagari block U+0900-U+097F",
"Unicode Kaithi block U+11080-U+1114F",
"Ethnologue language code bho",
],
"citations": [
"Ethnologue: Languages of the World - Bhojpuri (bho).",
"Grierson, George A. Linguistic Survey of India, Vol. V - Indo-Aryan Family, Eastern Group (Bihari). 1903.",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. The Asiatic Society, 1960.",
"Shukla, Shaligram. Bhojpuri Grammar. Georgetown University Press, 1968.",
"The Unicode Standard - Devanagari block U+0900-U+097F; Kaithi block U+11080-U+1114F.",
],
"sig_lens": (
"His Signature reading: Bhojpuri is a covenant language of the soil - named for a "
"king's district, written by scribes in Kaithi, carried across oceans by laborers "
"who never let it die. The Signature Language Method treats every postposition as "
"a handshake after the noun, every dialect as a witness to the same original "
"draft, every proverb as a seal pressed on the teaching."),
},
# ------------------------------------------------------- 2 writing system
{
"key": "script",
"name": "Bhojpuri Writing System (Devanagari and Kaithi)",
"group": "script",
"ladder_rank": 2,
"ladder_tier": "foundations",
"description": (
"Bhojpuri in India and Nepal is written in Devanagari (देवनागरी), the same "
"left-to-right abugida used for Hindi, where each consonant letter carries an "
"inherent 'a' vowel unless a vowel sign changes it. The thirteen vowels are अ आ "
"इ ई उ ऊ ऋ ए ऐ ओ औ अं अः (a aa i ee u oo ri e ai o au an ah). The thirty-three "
"consonants run क ख ग घ ङ (ka kha ga gha nga), च छ ज झ ञ (cha chha ja jha nya), "
"ट ठ ड ढ ण (retroflex ta tha da dha na), त थ द ध न (dental ta tha da dha na), "
"प फ ब भ म (pa pha ba bha ma), य र ल व (ya ra la va), श ष स ह (sha ssa sa ha), "
"plus the conjuncts क्ष त्र ज्ञ श्र (kssa tra gya shra). Vowel signs (मात्राएँ) "
"attach to consonants: ा ि ी ु ू ृ े ै ो ौ ं ः, and the halant ् kills the inherent "
"vowel for conjuncts. Nasalization is marked with the chandrabindu ँ or anusvara ं. "
"Devanagari numerals are ० १ २ ३ ४ ५ ६ ७ ८ ९ (0-9). The sentence ends with the "
"danda ।, as in: हम भोज्पुरी पढ़त बानी। (ham bhojpuri parhat bani - 'I am reading "
"Bhojpuri.'). Bhojpuri's historic hand is Kaithi (कैथी, 'of the Kayasthas'), the "
"script of the Kayastha scribes who kept revenue and legal records across Bihar "
"and Uttar Pradesh; Kaithi gave Bhojpuri its old printed books and court "
"documents, and it now lives in Unicode at U+11080-U+1114F. Example words to "
"copy by hand: भोज्पुरी (bhojpuri - Bhojpuri), माई (mai - mother), पानी (pani - "
"water), गाँव (gaanv - village), लिट्टी (litti - the roasted wheat ball of "
"litti-chokha)."),
"how_it_works": (
"Devanagari is an abugida: every consonant letter already contains a short 'a', "
"so क is 'ka', not 'k'. To write 'ki' you hang the vowel sign ि before the "
"letter: कि. To write 'k' with no vowel you add the halant: क्, which lets "
"consonants join into conjuncts like स्त in नमस्ते. Words divide into syllables "
"that each end in a vowel, which is why Bhojpuri spelling looks the way it "
"sounds: भो-ज-पु-री. Kaithi works the same way with different letter shapes and "
"was the everyday handwriting of Bhojpuri for centuries - learning its shapes "
"lets you read old land records and folk manuscripts. Practice by writing each "
"example word three times: once slowly naming each letter, once at normal speed, "
"once from memory."),
"key_points": [
"Devanagari: left-to-right abugida; consonants carry an inherent 'a' vowel.",
"13 vowels: अ आ इ ई उ ऊ ऋ ए ऐ ओ औ अं अः; 33 consonants plus conjuncts क्ष त्र ज्ञ श्र.",
"Vowel signs (मात्राएँ) attach to consonants: का कि की कु कू कृ के कै को कौ कं कः.",
"Halant ् removes the inherent vowel and builds conjuncts.",
"Nasalization: chandrabindu ँ and anusvara ं (गाँव, भोज्पुरी).",
"Devanagari numerals: ० १ २ ३ ४ ५ ६ ७ ८ ९; sentence ends with danda ।.",
"Kaithi (कैथी) is Bhojpuri's historic script - the Kayastha scribes' hand.",
"Kaithi lives in Unicode at U+11080-U+1114F.",
"Read old Bhojpuri in Kaithi; write modern Bhojpuri in Devanagari.",
"Copy each example word three times: slow, normal speed, from memory.",
],
"requirements": [
"A notebook and pen - handwriting fixes the letter shapes faster than typing.",
"Learn the five stop rows (क च ट त प) before the sibilants and conjuncts.",
"Read every example word aloud as you write it.",
],
"standards": [
"Unicode Devanagari block U+0900-U+097F",
"Unicode Kaithi block U+11080-U+1114F",
"ISO 15924 script codes: Deva, Kthi",
],
"citations": [
"The Unicode Standard - Devanagari block U+0900-U+097F.",
"The Unicode Standard - Kaithi block U+11080-U+1114F.",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903 (on Kaithi use).",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
],
"sig_lens": (
"His Signature reading: Devanagari is the public seal of the language and Kaithi "
"its private hand - one for the printed book, one for the scribe's ledger. The "
"Signature Language Method learns both, because a signature is only real when "
"you can write it twice in two hands and it still reads the same."),
},
# ------------------------------------------------------- 3 phonology
{
"key": "phonology",
"name": "Bhojpuri Pronunciation and Phonology",
"group": "sounds",
"ladder_rank": 3,
"ladder_tier": "foundations",
"description": (
"Bhojpuri sounds are close to Hindi but with a softer, rolling eastern music. "
"The five stop rows each come in four flavors - plain, aspirated, voiced, voiced "
"aspirated: क ख ग घ (ka kha ga gha), च छ ज झ (cha chha ja jha), ट ठ ड ढ (retroflex "
"ta tha da dha - tongue curled back), त थ द ध (dental ta tha da dha - tongue on "
"the teeth), प फ ब भ (pa pha ba bha ma). Aspiration changes meaning - true "
"minimal pairs: ताल (taal - pond, rhythm) versus थाल (thaal - plate); दाम (daam - "
"price) versus धाम (dhaam - abode); बात (baat - talk) versus भात (bhaat - cooked "
"rice); कान (kaan - ear) versus खान (khaan - mine, quarry). Nasalized vowels (गाँव gaanv - "
"village, भोज्पुरी bhojpuri) are everyday sounds - let the air pass through the "
"nose. The retroflex flap ड़ (as in बड़ - big, गाड़ी - vehicle) is a quick tongue "
"flick, not a full ड. Stress falls lightly and early in the word, and final "
"short 'a' is usually silent: नमस्ते is 'namaste', not 'namaste-a'. Twelve "
"spoken-example words to drill aloud: पानी (pani - water), घर (ghar - house), "
"माई (mai - mother), घाम (ghaam - sunshine), चिरई (chirai - bird), मछरी (machhri - "
"fish), गोड़ (gor - leg, foot), बानर (banar - monkey), पइसा (paisa - money), "
"लिट्टी (litti - roasted wheat ball), सत्तू (sattu - roasted gram flour), "
"बेटा (beta - son). Say each one, then use it: पानी पीत बानी (pani peet bani - "
"'I am drinking water')."),
"how_it_works": (
"Every Bhojpuri consonant is a place plus a manner: where the tongue goes and "
"whether the breath bursts. Drill each row as a ladder - क ख ग घ ङ - plain, "
"breathy, voiced, voiced-breathy, nasal. Then drill the danger pairs that change "
"meaning: ताल/थाल, दाम/धाम, बात/भात, कान/खान. Nasalization is a switch you flip "
"with the soft palate: say गाव (gaav) then गाँव (gaanv) and feel the nose join. "
"The flap ड़ is one tap of the tongue tip against the ridge - practice with "
"बड़-बड़-बड़ until it rolls. Record yourself reading the twelve example words "
"and compare against the written forms; your ear learns faster than your eye."),
"key_points": [
"Five stop rows x four manners: plain, aspirated, voiced, voiced-aspirated (क ख ग घ).",
"Retroflex row (ट ठ ड ढ ण) curls the tongue back; dental row (त थ द ध न) touches the teeth.",
"Minimal pairs prove aspiration matters: ताल/थाल, दाम/धाम, बात/भात, कान/खान.",
"Flap ड़ (बड़, गाड़ी) is a single tongue tap, not a full ड.",
"Nasalized vowels (गाँव, भोज्पुरी) let air through the nose.",
"Final short 'a' is silent: नमस्ते is 'namaste'.",
"Stress is light and falls early in the word.",
"Twelve drill words: पानी, घर, माई, घाम, चिरई, मछरी, गोड़, बानर, पइसा, लिट्टी, सत्तू, बेटा.",
"Drill each stop row as a ladder: plain, breathy, voiced, voiced-breathy, nasal.",
"Record yourself and compare against the written forms.",
],
"requirements": [
"Say every pair and word aloud - phonology is a muscle skill.",
"Practice the ड़ flap with बड़-बड़-बड़ until it rolls.",
"Do not skip nasalization: गाव and गाँव are different words.",
],
"standards": [
"IPA reference points: retroflex stops [ʈ ʈʰ ɖ ɖʰ], flap [ɽ], aspirates [kʰ gʱ] etc.",
"Unicode Devanagari block U+0900-U+097F",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. Georgetown University Press, 1968 (phonology).",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960 (sound changes).",
"The Unicode Standard - Devanagari block U+0900-U+097F.",
],
"sig_lens": (
"His Signature reading: the aspirated consonant is a signature with extra ink - "
"the same letter, breathed on. The Signature Language Method drills the four "
"manners of each row like four pens: plain, breathy, voiced, voiced-breathy, "
"until the hand - and the tongue - signs without thinking."),
},
# ------------------------------------------------------- 4 nouns I
{
"key": "nouns1",
"name": "Bhojpuri Core Nouns I",
"group": "words",
"ladder_rank": 4,
"ladder_tier": "foundations",
"description": (
"Twenty-five essential Bhojpuri nouns - people, places, and things - each with "
"transliteration, English, gender note, and one example sentence with English "
"translation. 1. आदमी (aadmi, man, m): आदमी खेत में काम करत बा (the man is "
"working in the field). 2. औरत (aurat, woman, f): औरत बाजार जात बिया (the woman "
"is going to the market). 3. लइका (laika, boy/child, m): लइका खेलत बा (the boy "
"is playing). 4. लइकी (laiki, girl, f): लइकी पढ़त बिया (the girl is studying). "
"5. घर (ghar, house, m): हमार घर गाँव में बा (my house is in the village). "
"6. गाँव (gaanv, village, m): गाँव बहुत सुन्नर बा (the village is very beautiful). "
"7. शहर (shahar, city, m): शहर दूर बा (the city is far). 8. नदी (nadi, river, f): "
"नदी में पानी बा (there is water in the river). 9. पेड़ (per, tree, m): पेड़ पर "
"चिरई बा (there is a bird on the tree). 10. फूल (phool, flower, m): फूल बहुत "
"सुन्नर बा (the flower is very beautiful). 11. किताब (kitaab, book, f): किताब "
"मेज पर बा (the book is on the table). 12. कलम (kalam, pen, m): कलम से लिखीं "
"(write with the pen). 13. पानी (pani, water, m): पानी ठंडा बा (the water is "
"cold). 14. खाना (khaana, food, m): खाना गरम बा (the food is hot). 15. रोटी "
"(roti, bread, f): माई रोटी बनावत बिया (mother is making bread). 16. दूध (doodh, "
"milk, m): गाय दूध देले (the cow gives milk). 17. गाय (gaay, cow, f): गाय खेत में "
"बिया (the cow is in the field). 18. भैंस (bhains, buffalo, f): भैंस तालाब में "
"बिया (the buffalo is in the pond). 19. कुत्ता (kutta, dog, m): कुत्ता दुआर पर "
"बा (the dog is at the door). 20. बिल्ली (billi, cat, f): बिल्ली दूध पीत बिया "
"(the cat is drinking milk). 21. सूरज (sooraj, sun, m): सूरज उगल बा (the sun has "
"risen). 22. चाँद (chaand, moon, m): चाँद रात में चमकत बा (the moon shines at "
"night). 23. रात (raat, night, f): रात हो गइल (night has fallen). 24. दिन (din, "
"day, m): दिन में घाम बा (there is sunshine in the day). 25. काम (kaam, work, m): "
"काम काल्ह होई (the work will be done tomorrow)."),
"how_it_works": (
"Bhojpuri nouns carry gender (masculine/feminine) and number (singular/plural), "
"and the gender steers the adjectives and verbs around them: लइका खेलत बा "
"(masculine) but लइकी खेलत बिया (feminine). Plurals often add -न or -लोग for "
"people: आदमी लोग (men), लइका लोग (children). Learn each noun with its gender "
"the way you learn its meaning - flashcard the pair 'लइका (m)' not just "
"'लइका'. The example sentences all run subject-object-verb, so reading them "
"trains word order and noun gender at once."),
"key_points": [
"25 essential nouns: people, places, things - each with gender and a sentence.",
"Two genders (masculine, feminine) steer adjectives and verbs: बा vs बिया.",
"Two numbers: singular and plural; people plurals often use -लोग (आदमी लोग).",
"Learn noun + gender as one unit: 'लइका (m)', not just 'लइका'.",
"All example sentences run subject-object-verb.",
"Postpositions follow the noun: घर में, मेज पर, दुआर पर.",
"Gender is grammatical habit, not logic: पानी (m), नदी (f), किताब (f).",
"Reading the sentences aloud trains gender, order, and vocabulary together.",
],
"requirements": [
"Memorize each noun with its gender tag.",
"Say every example sentence aloud twice.",
"Make your own sentence with five of the nouns.",
],
"standards": [
"Devanagari spelling per standard Bhojpuri usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968 (noun morphology).",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
],
"sig_lens": (
"His Signature reading: a noun is a named thing, and naming is the first act "
"of ownership - the Signature Language Method makes you sign each noun with "
"its gender, because a half-signed word will not stand up in a sentence."),
},
# ------------------------------------------------------- 5 verbs I
{
"key": "verbs1",
"name": "Bhojpuri Core Verbs I",
"group": "words",
"ladder_rank": 5,
"ladder_tier": "foundations",
"description": (
"Twenty-five essential Bhojpuri verbs - each given as the stem with "
"transliteration and English, plus one example sentence with translation. "
"1. खा (kha, eat): हम रोटी खात बानी (I am eating bread). 2. पी (pee, drink): "
"तू पानी पीत बाड़ऽ (you are drinking water). 3. जा (ja, go): उ स्कूल जात बा "
"(he is going to school). 4. आ (aa, come): माई घर आवत बिया (mother is coming "
"home). 5. कर (kar, do): हम काम करत बानी (I am doing the work). 6. बोल (bol, "
"speak): उ भोज्पुरी बोलत बा (he speaks Bhojpuri). 7. देख (dekh, see/watch): हम "
"फिल्म देखत बानी (I am watching a film). 8. सुन (sun, listen/hear): तू गाना "
"सुनत बाड़ऽ (you are listening to a song). 9. पढ़ (parh, read/study): लइकी किताब "
"पढ़त बिया (the girl is reading a book). 10. लिख (likh, write): हम चिट्ठी लिखत "
"बानी (I am writing a letter). 11. चल (chal, walk): हम पैदल चलत बानी (I am "
"walking on foot). 12. दउड़ (daur, run): लइका दउड़त बा (the boy is running). "
"13. बइठ (baith, sit): तू इहाँ बइठऽ (you sit here). 14. उठ (uth, rise/get up): "
"हम बिहान उठत बानी (I get up in the morning). 15. सुत (sut, sleep): लइका सुतत "
"बा (the child is sleeping). 16. दे (de, give): हमके पानी दऽ (give me water). "
"17. ले (le, take): कलम ले लऽ (take the pen). 18. बना (bana, make): माई खाना "
"बनावत बिया (mother is cooking food). 19. खेल (khel, play): लइका लोग खेलत बा "
"(the children are playing). 20. हँस (hans, laugh): उ हँसत बा (he is laughing). "
"21. रो (ro, cry): लइकी रोवत बिया (the girl is crying). 22. सोच (soch, think): "
"हम सोचत बानी (I am thinking). 23. जान (jaan, know): हम जानत बानी (I know). "
"24. चाह (chaah, want): हमके रोटी चाहीं (I want bread). 25. मिल (mil, meet): "
"हम काल्ह मिलब (I will meet tomorrow)."),
"how_it_works": (
"Bhojpuri verbs are built from a stem: add -त for the ongoing action (खा + त = "
"खात, eating), then the 'be' helper that matches the person - बानी (I am), "
"बाड़ऽ (you are), बा (he/she is). The future takes -ब straight on the stem: "
"खाइब (will eat), जाइब (will go), करब (will do). The command is the bare stem: "
"खा! (eat!), जा! (go!), देख! (look!). Learn the stem first - everything else "
"hangs off it - and drill each new verb in all three frames: present (खात "
"बानी), future (खाइब), command (खा)."),
"key_points": [
"25 essential verbs as stems: खा पी जा आ कर बोल देख सुन पढ़ लिख चल दउड़ बइठ उठ सुत दे ले बना खेल हँस रो सोच जान चाह मिल.",
"Present continuous: stem + त + बानी/बाड़ऽ/बा (खात बानी - am eating).",
"Future: stem + ब (खाइब - will eat; जाइब - will go; करब - will do).",
"Command: bare stem (खा! जा! देख!).",
"Learn the stem first; every form hangs off it.",
"Drill each verb in three frames: present, future, command.",
"'Be' helpers: बानी (I), बाड़ऽ (you), बा (he/she).",
"चाह (want) uses हमके + चाहीं: हमके पानी चाहीं.",
],
"requirements": [
"Memorize the 25 stems before any endings.",
"Conjugate five verbs in present, future, and command aloud.",
"Use each verb in one sentence of your own.",
],
"standards": [
"Stem-based presentation per standard Bhojpuri grammars.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968 (verb system).",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
],
"sig_lens": (
"His Signature reading: the verb stem is the signature itself - खा, जा, कर - "
"and the endings are the flourishes that date it: present, future, command. "
"The Signature Language Method signs the stem first and never lets the "
"flourish cover the name."),
},
# ------------------------------------------------- 6 adjectives/adverbs
{
"key": "adjadv",
"name": "Bhojpuri Adjectives and Adverbs",
"group": "words",
"ladder_rank": 6,
"ladder_tier": "foundations",
"description": (
"Twenty-five Bhojpuri adjectives and fifteen adverbs, each with an example "
"sentence and English translation. Adjectives: 1. बड़ (bar, big): बड़ घर (a big "
"house). 2. छोट (chhot, small): छोट लइका (a small child). 3. नीक (neek, good): "
"नीक आदमी (a good man) - नीक is the true Bhojpuri word for 'good'. 4. खराब "
"(kharaab, bad): खराब मौसम (bad weather). 5. नया (naya, new): नया कपड़ा (new "
"clothes). 6. पुरान (puraan, old): पुरान घर (an old house). 7. गरम (garam, hot): "
"गरम चाय (hot tea). 8. ठंडा (thanda, cold): ठंडा पानी (cold water). 9. मीठ "
"(meeth, sweet): मीठ आम (a sweet mango). 10. तीता (teeta, bitter): तीता करेला "
"(bitter gourd). 11. खट्टा (khatta, sour): खट्टा नींबू (a sour lemon). 12. लम्बा "
"(lamba, tall/long): लम्बा आदमी (a tall man). 13. मोटा (mota, fat): मोटा बैल (a fat ox). 14. पातर (paatar, thin): पातर लकड़ी (a thin stick) - पातर "
"is Bhojpuri for 'thin'. 15. गोर (gor, fair): गोर रंग (fair color). 16. करिया "
"(kariya, black): करिया बादल (black clouds). 17. उज्जर (ujjar, white): उज्जर कपड़ा "
"(white clothes). 18. लाल (laal, red): लाल फूल (a red flower). 19. हरियर (hariyar, "
"green): हरियर खेत (green fields). 20. नीला (neela, blue): नीला आसमान (blue sky). "
"21. पीला (peela, yellow): पीला फूल (a yellow flower). 22. खुश (khush, happy): "
"खुश परिवार (a happy family). 23. तेज (tej, fast/sharp): तेज घोड़ा (a fast horse). "
"24. साफ (saaf, clean): साफ पानी (clean water). 25. गंदा (ganda, dirty): गंदा "
"कपड़ा (dirty clothes). Agreement: adjectives ending in -ा take -ी for the "
"feminine - बड़ घर (big house, m) but बड़ी कोठरी (big room, f); नीक लइका but नीकी "
"लइकी. Adverbs: 1. बहुत (bahut, very): बहुत नीक (very good). 2. थोड़ा (thora, a "
"little): थोड़ा पानी (a little water). 3. जल्दी (jaldi, quickly): जल्दी आ (come "
"quickly). 4. धीरे (dheere, slowly): धीरे बोलऽ (speak slowly). 5. आज (aaj, today): "
"आज बरसात बा (it is raining today). 6. काल्ह (kaalh, tomorrow/yesterday): हम काल्ह "
"जाइब (I will go tomorrow). 7. अब (ab, now): अब खा (eat now). 8. इहाँ (ihaan, "
"here): इहाँ बइठऽ (sit here). 9. उहाँ (uhaan, there): उहाँ जा (go there). 10. कहाँ "
"(kahaan, where): तू कहाँ बाड़ऽ? (where are you?). 11. कइसे (kaise, how): तू कइसे "
"बाड़ऽ? (how are you?). 12. हमेशा (hamesha, always): हम हमेशा आवत बानी (I always "
"come). 13. कभी (kabhi, sometimes): उ कभी-कभी आवत बा (he comes sometimes). "
"14. बहुत दूर (bahut door, very far): गाँव बहुत दूर बा (the village is very far). "
"15. ना (na, not): हम ना जाइब (I will not go)."),
"how_it_works": (
"Bhojpuri adjectives sit before the noun and agree with it: masculine बड़ घर, "
"feminine बड़ी कोठरी, plural बड़े घर. Adjectives that do not end in -ा (नीक, "
"खुश, साफ) never change - नीक आदमी, नीकी औरत? No: नीक never changes; say नीक "
"औरत (good woman). Adverbs never change and sit before the verb or adjective "
"they color: बहुत नीक, जल्दी आ, धीरे बोलऽ. Time adverbs (आज, काल्ह, अब) usually "
"open the sentence. Note काल्ह means both 'tomorrow' and 'yesterday' - the "
"verb tense tells you which: हम काल्ह जाइब (I will go tomorrow) versus हम काल्ह "
"गइनीं? Use perfective: काल्ह बरसात भइल (it rained yesterday)."),
"key_points": [
"25 adjectives + 15 adverbs, each with an example sentence.",
"True Bhojpuri color words: नीक (good), पातर (thin), करिया (black), उज्जर (white), हरियर (green).",
"-ा adjectives agree: बड़ (m), बड़ी (f), बड़े (plural).",
"Non -ा adjectives never change: नीक आदमी, नीक औरत.",
"Adverbs never change: बहुत नीक, जल्दी आ, धीरे बोलऽ.",
"काल्ह = tomorrow AND yesterday; the verb tense disambiguates.",
"Place adverbs: इहाँ (here), उहाँ (there) - pure Bhojpuri forms.",
"Time adverbs usually open the sentence: आज बरसात बा.",
],
"requirements": [
"Learn the Bhojpuri color and size words (नीक, पातर, करिया, उज्जर, हरियर) first.",
"Practice -ा to -ी agreement aloud with ten nouns.",
"Use each adverb in one sentence of your own.",
],
"standards": [
"Adjective agreement per standard Bhojpuri grammars.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968 (adjective agreement).",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
],
"sig_lens": (
"His Signature reading: the adjective is the seal's color and the adverb its "
"pressure - नीक or खराब, जल्दी or धीरे. The Signature Language Method never "
"signs a noun without deciding its color first."),
},
# ------------------------------------------------------- 7 pronouns
{
"key": "pronouns",
"name": "Bhojpuri Pronouns",
"group": "words",
"ladder_rank": 7,
"ladder_tier": "foundations",
"description": (
"Full Bhojpuri pronoun paradigms with example sentences. Personal pronouns: "
"हम (ham, I): हम जात बानी (I am going). हमनी (hamni, we): हमनी खात बानीं (we are "
"eating). तू (tu, you - informal): तू कहाँ बाड़ऽ? (where are you?). रउआ (raua, "
"you - formal/respectful): रउआ बइठीं (please sit - to an elder). उ (u, he/she - "
"distant): उ आवत बा (he/she is coming). इ (i, he/she - near): इ हमार भाई हऽ (this "
"is my brother). उ लोग (u log, they - distant): उ लोग खेलत बा (they are playing). "
"इ लोग (i log, they - near): इ लोग पढ़त बा (they are studying). Possessives: "
"हमार (hamaar, my): हमार घर (my house). हमनी के (hamni ke, our): हमनी के गाँव "
"(our village). तोहार (tohaar, your - informal): तोहार नाम का हऽ? (what is your "
"name?). राउर (raaur, your - formal): राउर नाम का हऽ? (what is your name? - "
"respectful). ओकर (okar, his/her): ओकर किताब (his/her book). इ लोग के (i log ke, "
"their): इ लोग के घर (their house). Demonstratives: इ/ई (this): ई का हऽ? (what is "
"this?). उ/ऊ (that): ऊ के हऽ? (who is that?). इहे (this very one), उहे (that very "
"one): इहे किताब चाहीं (I want this very book). Interrogatives: के (ke, who): तू "
"के हवऽ? (who are you?). का (kaa, what): तू का करत बाड़ऽ? (what are you doing?). "
"कवन (kavan, which): कवन किताब? (which book?). कहाँ (kahaan, where): घर कहाँ बा? "
"(where is the house?). कब (kab, when): तू कब आइबऽ? (when will you come?). काहे "
"(kaahe, why): तू काहे रोवत बाड़ऽ? (why are you crying?). कइसे (kaise, how): ई "
"कइसे भइल? (how did this happen?). केतना (ketna, how much/many): ई केतना के बा? "
"(how much is this?). Reflexive/emphatic: अपने (apne, oneself): अपने काम करऽ (do "
"your own work). हम खुद (ham khud, I myself): हम खुद जाइब (I will go myself)."),
"how_it_works": (
"Bhojpuri pronouns change with respect: तू for friends and juniors, रउआ for "
"elders and strangers - using तू to an elder is rude, using रउआ to a child is "
"comically formal. Possessives are built two ways: the fused forms हमार, तोहार, "
"ओकर, राउर, and the के construction हमनी के, इ लोग के. Demonstratives double as "
"'he/she': इ and उ point at people as easily as things. Interrogatives open the "
"question: के, का, कहाँ, कब, काहे, कइसे, केतना - learn them as a set and you can "
"ask anything. Word order stays subject-object-verb even in questions: तू का "
"करत बाड़ऽ? (you what doing are?)."),
"key_points": [
"Personal: हम, हमनी, तू, रउआ, उ, इ, उ लोग, इ लोग - each with a sentence.",
"Respect rule: तू for juniors/friends, रउआ for elders/strangers.",
"Possessives: हमार, तोहार, ओकर, राउर + के-forms हमनी के, इ लोग के.",
"Demonstratives double as he/she: इ (near), उ (distant).",
"Interrogative set: के का कवन कहाँ कब काहे कइसे केतना.",
"Questions keep SOV order: तू का करत बाड़ऽ?",
"Reflexive: अपने (oneself), खुद (myself).",
],
"requirements": [
"Memorize the respect rule before any conversation.",
"Drill the nine interrogatives until they come without thinking.",
"Practice possessives with your own belongings.",
],
"standards": [
"Paradigms per standard Bhojpuri grammars (Shukla 1968).",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968 (pronouns).",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
],
"sig_lens": (
"His Signature reading: pronouns are the signature's 'I' - हम is the hand "
"itself, रउआ the hand offered in respect. The Signature Language Method makes "
"the respect levels automatic, because a signature given rudely is no "
"signature at all."),
},
# ------------------------------------------------------- 8 numbers/time
{
"key": "numbers",
"name": "Bhojpuri Numbers and Time",
"group": "words",
"ladder_rank": 8,
"ladder_tier": "foundations",
"description": (
"Bhojpuri numbers 1 to 100, ordinals, days, months, seasons, clock time, and "
"dates - each with an example sentence. 1 एक (ek), 2 दू (doo), 3 तीन (teen), "
"4 चार (chaar), 5 पाँच (paanch), 6 छव (chhav), 7 सात (saat), 8 आठ (aath), 9 नव "
"(nav), 10 दस (das), 11 एगारह (egaarah), 12 बारह (baarah), 13 तेरह (terah), 14 "
"चउदह (chaudah), 15 पनरह (panrah), 16 सोरह (sorah), 17 सतरह (satrah), 18 अठरह "
"(athrah), 19 उन्नीस (unnees), 20 बीस (bees), 21 एकइस (ekais), 22 बाइस (baais), "
"30 तीस (tees), 31 एकतीस (ektees), 40 चालीस (chaalees), 50 पचास (pachaas), 60 "
"साठ (saath), 70 सत्तर (sattar), 80 अस्सी (assi), 90 नब्बे (nabbe), 100 सव (sau). "
"Ordinals: पहिल (pahil, first), दुसर (dusar, second), तिसर (tisar, third). "
"Days: सोमवार (Monday), मंगलवार (Tuesday), बुधवार (Wednesday), बृहस्पतिवार "
"(Thursday), शुक्रवार (Friday), शनिवार (Saturday), एतवार (etvaar, Sunday - the "
"Bhojpuri name). Months follow the Hindi calendar: चैत, बैसाख, जेठ, असाढ़, सावन, "
"भादो, क्वार, कातिक, अगहन, पूस, माघ, फागुन. Seasons: गर्मी (garmi, summer), बरसात "
"(barsaat, rains), जाड़ा (jaara, winter), बसंत (basant, spring). Time of day: "
"बिहान (bihaan, morning), दुपहरिया (dupahariya, afternoon), साँझ (saanjh, "
"evening), रात (raat, night). Clock: तीन बजल बा (teen bajal ba - it is three "
"o'clock); साढ़े तीन (half past three); पौने चार (quarter to four); सवा तीन "
"(quarter past three). Sentences: हमरा लगे दू गो किताब बा (I have two books - "
"गो counts things). आज एतवार हऽ (today is Sunday). सावन में बरसात होले (it rains "
"in Saavan). जाड़ा में ठंडा पड़ेला (it gets cold in winter). हम तीन बजे जाइब (I "
"will go at three o'clock). ओकर जन्मदिन कातिक में बा (his birthday is in Kaatik)."),
"how_it_works": (
"Bhojpuri numbers 1-20 are learned by heart; 21-99 follow the tens + units "
"pattern (एकतीस = one-thirty). The counter गो (go) goes after the number for "
"things: दू गो किताब (two books), तीन गो आदमी (three men). Ordinals पहिल, दुसर, "
"तिसर cover first through third; beyond that use number + वाँ in Hindi style or "
"rephrase. Clock time uses बजल: the hour + बजल बा. Days and months run the "
"agricultural year - सावन (monsoon), कातिक (harvest festivals), फागुन (spring, "
"Holi). Drill by telling your own day: हम सात बजे उठत बानी (I get up at seven)."),
"key_points": [
"1-100 with Bhojpuri forms: छव (6), चउदह (14), पनरह (15), सोरह (16), सव (100).",
"Counter गो for things: दू गो किताब, तीन गो आदमी.",
"Ordinals: पहिल, दुसर, तिसर.",
"Sunday is एतवार in Bhojpuri - a signature word.",
"Twelve months: चैत बैसाख जेठ असाढ़ सावन भादो क्वार कातिक अगहन पूस माघ फागुन.",
"Seasons: गर्मी, बरसात, जाड़ा, बसंत.",
"Clock: hour + बजल बा; साढ़े (half past), पौने (quarter to), सवा (quarter past).",
"Day parts: बिहान, दुपहरिया, साँझ, रात.",
],
"requirements": [
"Count 1-20 aloud until automatic, then the tens to 100.",
"Tell your daily schedule in Bhojpuri with बजल times.",
"Learn the twelve months in order.",
],
"standards": [
"Numerals per standard Bhojpuri usage; Devanagari digits ०-९.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968 (numerals).",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
],
"sig_lens": (
"His Signature reading: numbers are the signature's serial code - एक to सव, "
"each in its place. The Signature Language Method counts the day in Bhojpuri "
"until the tongue numbers without the mind."),
},
# ------------------------------------------------------- 9 greetings
{
"key": "greetings",
"name": "Bhojpuri Greetings and Everyday Phrases",
"group": "phrases",
"ladder_rank": 9,
"ladder_tier": "foundations",
"description": (
"Thirty Bhojpuri greetings, farewells, and politeness phrases with usage "
"notes. 1. प्रणाम (pranaam) - respectful greeting to elders, palms together. "
"2. राम राम (raam raam) - the everyday Bhojpuri hello and goodbye. 3. नमस्ते "
"(namaste) - neutral polite greeting. 4. सलाम (salaam) - greeting among Muslim "
"Bhojpuri speakers. 5. का हाल बा? (kaa haal ba?) - How are you? (to one person). "
"6. का हाल चाल बा? - How are things going? 7. ठीक बा (theek ba) - I am fine. "
"8. सब बढ़िया बा (sab badhiya ba) - everything is great. 9. बहुत दिन बाद देखनी "
"(bahut din baad dekhni) - long time no see (respectful). 10. आईं, बइठीं (aain, "
"baithin) - come in, please sit. 11. चाय पीबऽ? (chaay peeba?) - will you have "
"tea? 12. खाना खइबऽ? - will you eat? 13. धन्यवाद (dhanyavaad) - thank you. "
"14. बहुत बहुत धन्यवाद - thank you very much. 15. माफ करीं (maaf kareen) - "
"forgive me (respectful). 16. क्षमा करीं - pardon me (formal). 17. कोनो बात "
"नइखे (kono baat naikhe) - no problem, it is nothing. 18. फिर मिलब (phir milab) - "
"see you again. 19. राम राम (farewell use) - goodbye, said with folded hands. "
"20. शुभ यात्रा (shubh yaatra) - safe journey. 21. बधाई (badhaai) - "
"congratulations. 22. जन्मदिन मुबारक (janmdin mubaarak) - happy birthday. "
"23. नया साल मुबारक - happy new year. 24. छठ मुबारक - happy Chhath (the great "
"Bhojpuri sun festival). 25. दीवाली मुबारक - happy Diwali. 26. होली मुबारक - "
"happy Holi. 27. ईद मुबारक - Eid greetings. 28. शुभ बिहान (shubh bihaan) - good "
"morning. 29. शुभ साँझ - good evening. 30. शुभ रात - good night. Usage: राम राम "
"works morning to night and doubles as farewell; प्रणाम is for elders and "
"teachers; रउआ forms (आईं, बइठीं, करीं) carry the respect - तू forms (आ, बइठ, "
"कर) are for friends and juniors only."),
"how_it_works": (
"Bhojpuri politeness lives in the verb ending: the -ीं forms (आईं, बइठीं, "
"माफ करीं) are respectful, the bare stems (आ, बइठ, कर) are familiar. Match the "
"ending to the person: elder or stranger gets -ीं, friend gets the bare stem. "
"राम राम is the all-purpose social glue - hello, goodbye, and blessing in two "
"syllables. Festival greetings follow the Bhojpuri calendar, with छठ (Chhath, "
"the sun festival of Bihar) standing first among equals. Practice each phrase "
"with the matching body language: palms together for प्रणाम, a nod for राम राम."),
"key_points": [
"30 greetings/farewells/politeness phrases with usage notes.",
"राम राम = hello AND goodbye, the all-purpose Bhojpuri greeting.",
"प्रणाम for elders; नमस्ते neutral; सलाम among Muslim speakers.",
"Respect lives in -ीं endings: आईं/बइठीं/माफ करीं vs आ/बइठ/कर.",
"का हाल बा? opens every conversation; ठीक बा / सब बढ़िया बा answer it.",
"छठ मुबारक honors Chhath, the great Bhojpuri sun festival.",
"कोनो बात नइखे = no problem; फिर मिलब = see you again.",
"Match palms-together प्रणाम and nodding राम राम to the words.",
],
"requirements": [
"Greet someone with राम राम and का हाल बा? today.",
"Practice the -ीं respectful forms until automatic.",
"Learn the festival greetings for छठ, दीवाली, होली, ईद.",
],
"standards": [
"Phrases per living Bhojpuri usage (Bihar, Purvanchal, Nepal Terai).",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903 (forms of address).",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
],
"sig_lens": (
"His Signature reading: a greeting is a signature exchanged - राम राम the quick "
"initial, प्रणाम the full formal signature with palms as the seal. The "
"Signature Language Method teaches the handshake before the contract: greet "
"right, and every door opens."),
},
# ------------------------------------------------------- 10 grammar
{
"key": "grammar",
"name": "Bhojpuri Grammar Essentials",
"group": "grammar",
"ladder_rank": 10,
"ladder_tier": "compounded",
"description": (
"The working core of Bhojpuri grammar, each rule with translated example "
"sentences. Word order: subject-object-verb, always - हम चाय पीत बानी (ham chaay "
"peet bani - I am drinking tea); verb last, no exceptions in plain sentences. "
"Gender: masculine and feminine - nouns, adjectives, and verbs agree: बड़ लइका "
"खेलत बा (the big boy is playing) vs बड़ी लइकी खेलत बिया (the big girl is "
"playing). Number: singular and plural - किताब (book) / किताबन? Standard plural: "
"किताबें? In Bhojpuri: किताब सब? Use लोग for people (आदमी लोग) and -न/-अन for "
"things in many dialects; the safe universal plural marker in sentences is सब "
"or लोग: किताब सब मेज पर बा (the books are on the table). Cases: Bhojpuri nouns "
"do not decline like Sanskrit - postpositions do the work: घर में (in the "
"house), मेज पर (on the table), गाँव से (from the village), मोहन के (Mohan's / "
"to Mohan), रउआ खातिर (for you), घर लगे (near the house). Articles: none - एक "
"(one) does the work of 'a': एक आदमी (a man), ऊ आदमी (that man). Negation: ना "
"before the verb - हम ना जाइब (I will not go); नइखे for 'is not' - उ घर नइखे "
"(he is not home); मत for negative commands - मत जा (do not go). Questions: "
"start with the question word, keep SOV - तू का करत बाड़ऽ? (what are you doing?); "
"yes/no questions rise in intonation: तू जाइबऽ? (will you go?). The Hindi 'ne' "
"ergative does NOT exist in Bhojpuri: उ रोटी खइलस? Standard: past verbs agree "
"with the subject - हम गइनीं? Keep to the safe perfective: उ खइले बा (he has "
"eaten), हम आइल बानी (I have come), ऊ गइल (he went), ई भइल (this happened)."),
"how_it_works": (
"Build every Bhojpuri sentence on the SOV rail: who, what, action - हम / रोटी / "
"खात बानी. Hang relationships off the noun with postpositions (में पर से के "
"खातिर लगे) instead of prepositions before it. Flip meaning with the three "
"negators: ना (not - verbs), नइखे (is-not), मत (do-not - commands). Ask by "
"fronting के का कहाँ कब काहे कइसे केतना and letting the voice rise at the end "
"for yes/no. Mark past with the -ल participles (गइल आइल कइल खइल भइल) and let "
"the verb agree with the doer - never borrow Hindi's 'ne'. Drill: take हम चाय "
"पीत बानी and transform it - negate it, question it, pluralize it, past-tense "
"it."),
"key_points": [
"Word order is always subject-object-verb; the verb comes last.",
"Gender agreement: बड़ लइका खेलत बा vs बड़ी लइकी खेलत बिया.",
"Plurals: लोग for people (आदमी लोग), सब as universal marker (किताब सब).",
"Six core postpositions: में (in), पर (on), से (from), के (of/to), खातिर (for), लगे (near).",
"No articles: एक does the work of 'a'.",
"Three negators: ना (verbs), नइखे (is-not), मत (negative commands).",
"Questions front the question word and keep SOV; yes/no rises in intonation.",
"No 'ne' ergative: past verbs agree with the subject (उ खइले बा, ऊ गइल).",
],
"requirements": [
"Build ten SOV sentences, then negate and question each.",
"Drill the six postpositions with your own nouns.",
"Never use Hindi 'ne' in a Bhojpuri sentence.",
],
"standards": [
"Grammar per Shukla 1968 and Grierson LSI Vol. V.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968.",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
],
"sig_lens": (
"His Signature reading: grammar is the signature's ruled paper - SOV the "
"baseline, postpositions the margins, negation the strikethrough. The "
"Signature Language Method writes every sentence on the same ruled lines "
"until the hand cannot leave them."),
},
# ------------------------------------------------------- 11 home/family
{
"key": "home",
"name": "Bhojpuri Home and Family Sentences",
"group": "sentences",
"ladder_rank": 11,
"ladder_tier": "compounded",
"description": (
"Twenty Bhojpuri sentences about house, rooms, furniture, and family - each "
"with transliteration and English. 1. हमार घर गाँव में बा (hamaar ghar gaanv "
"men ba - My house is in the village). 2. घर में तीन गो कोठरी बा (There are "
"three rooms in the house). 3. दुआर पर कुत्ता बा (The dog is at the door). "
"4. खिड़की से घाम आवत बा (Sunshine is coming through the window). 5. रसोई में "
"माई खाना बनावत बिया (Mother is cooking food in the kitchen). 6. आँगन में लइका "
"लोग खेलत बा (The children are playing in the courtyard). 7. छत पर कपड़ा सुखत "
"बा (Clothes are drying on the roof). 8. खटिया पर दादी सुतल बिया (Grandmother "
"is lying on the cot). 9. मेज पर किताब बा (The book is on the table). 10. कुर्सी "
"टूट गइल (The chair broke). 11. हमार बाबूजी खेत में बाड़न (My father is in the "
"field - बाड़न is the respectful 'is'). 12. माई हमके बहुत प्यार करेली (Mother "
"loves me a lot). 13. हमार दू गो भाई आ एक गो बहिन बिया (I have two brothers and "
"one sister). 14. दादा कहानी सुनावत बाड़न (Grandfather is telling a story). "
"15. चाचा काल्ह शहर से अइहें (Uncle will come from the city tomorrow). 16. बेटा "
"स्कूल गइल बा (The son has gone to school). 17. बेटी पानी ले आवत बिया (The "
"daughter is bringing water). 18. परिवार सब साथे खाना खात बा (The whole family "
"is eating together). 19. घर के सामने नीम के पेड़ बा (There is a neem tree in "
"front of the house). 20. हमार घर हमार स्वर्ग हऽ (My home is my heaven)."),
"how_it_works": (
"Home sentences run on location postpositions - में (in), पर (on), लगे (near), "
"सामने (in front of) - and family sentences run on respect: बाबूजी बाड़न and "
"दादा सुनावत बाड़न use the respectful verb forms for elders, while माई "
"बनावत बिया stays plain. Possession is हमार/तोहार/ओकर + noun. Notice sentence "
"10 (कुर्सी टूट गइल - the chair broke): Bhojpuri states the event without "
"blaming anyone, a politeness built into the grammar. Learn the room words "
"(कोठरी, रसोई, आँगन, छत, दुआर) as a set by walking through your own house "
"naming each in Bhojpuri."),
"key_points": [
"20 home and family sentences with translations.",
"Location postpositions: में, पर, लगे, सामने.",
"Respectful verb forms for elders: बाड़न, सुनावत बाड़न.",
"Possession: हमार/तोहार/ओकर + noun.",
"Room set: कोठरी (room), रसोई (kitchen), आँगन (courtyard), छत (roof), दुआर (door).",
"Family set: माई, बाबूजी, दादा, दादी, चाचा, भाई, बहिन, बेटा, बेटी.",
"कुर्सी टूट गइल shows event-focus: no blame in the grammar.",
"Walk your house naming each room in Bhojpuri.",
],
"requirements": [
"Name every room of your home in Bhojpuri aloud.",
"Introduce your family members in two Bhojpuri sentences each.",
"Use बाड़न for one elder in a sentence.",
],
"standards": [
"Sentences per living Bhojpuri usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968.",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
],
"sig_lens": (
"His Signature reading: the home is where the signature is first practiced - "
"माई the first teacher, आँगन the first school. The Signature Language Method "
"signs the family names before anything else, because every other signature "
"in life is witnessed by these."),
},
# ------------------------------------------------------- 12 food/cooking
{
"key": "food",
"name": "Bhojpuri Food and Cooking Sentences",
"group": "sentences",
"ladder_rank": 12,
"ladder_tier": "compounded",
"description": (
"Twenty Bhojpuri sentences about meals, ingredients, cooking actions, and the "
"restaurant. 1. माई दाल-भात बनावत बिया (Mother is cooking dal and rice). "
"2. लिट्टी चोखा भोज्पुरी के शान हऽ (Litti-chokha is the pride of Bhojpuri - the "
"roasted wheat balls with mashed spiced vegetables). 3. सत्तू बहुत ताकतवर होला "
"(Sattu is very energizing - roasted gram flour, the laborer's food). 4. रोटी "
"तवा पर सेंकात बिया (The bread is baking on the griddle). 5. दाल में नमक कम बा "
"(There is less salt in the dal). 6. चाय में चीनी डालऽ (Put sugar in the tea). "
"7. खाना गरम बा, बइठ के खा (The food is hot; sit and eat). 8. हमके बहुत भूख लागल "
"बा (I am very hungry). 9. पानी ठंडा बा (The water is cold). 10. दूध उबल गइल "
"(The milk boiled over). 11. मिरचा बहुत तीता बा (The chili is very hot). 12. आलू "
"के सब्जी बनावऽ (Make potato curry). 13. प्याज काटत बानी (I am chopping onions). "
"14. हल्दी डालले से रंग नीक आवेला (Turmeric gives a good color). 15. घी में "
"छौंक लगावऽ (Temper it in ghee). 16. खिचड़ी नरम बनल बा (The khichdi turned out "
"soft). 17. दही खट्टा हो गइल (The yogurt turned sour). 18. होटल में खाना महँग "
"बा (Food is expensive at the restaurant). 19. बैरा, एक प्लेट समोसा लावऽ "
"(Waiter, bring one plate of samosas). 20. पेट भर गइल, बहुत नीक लागल (My "
"stomach is full; it tasted very good)."),
"how_it_works": (
"Food sentences are verb-rich: बनावत (cooking), सेंकात (baking), काटत "
"(chopping), डालऽ (put!), लगावऽ (temper!). Cooking commands use the bare stem "
"(डालऽ, बनावऽ, लगावऽ) - the kitchen is a familiar place, so तू-forms rule. "
"Taste words carry the meal: मीठ, तीता, खट्टा, नमकीन, गरम, ठंडा. लिट्टी चोखा "
"and सत्तू are not just foods but identity markers - naming them correctly "
"marks you as an insider. The restaurant sentences (18-19) switch to polite "
"forms: बैरा, ... लावऽ. Practice by narrating your own cooking step by step in "
"Bhojpuri."),
"key_points": [
"20 food and cooking sentences with translations.",
"Identity foods: लिट्टी चोखा (pride of Bhojpuri), सत्तू (the laborer's flour).",
"Kitchen verbs: बनावत, सेंकात, काटत, डालऽ, लगावऽ.",
"Kitchen commands use familiar stems: डालऽ, बनावऽ.",
"Taste set: मीठ, तीता, खट्टा, नमकीन, गरम, ठंडा.",
"Restaurant politeness: बैरा, एक प्लेट ... लावऽ.",
"होला/आवेला mark general truths: सत्तू ताकतवर होला.",
"Narrate your own cooking in Bhojpuri as practice.",
],
"requirements": [
"Name ten ingredients in Bhojpuri from your kitchen.",
"Narrate one recipe step by step in Bhojpuri.",
"Order food politely in a full Bhojpuri sentence.",
],
"standards": [
"Dish names per Bhojpuri culinary tradition (litti-chokha, sattu).",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
],
"sig_lens": (
"His Signature reading: लिट्टी चोखा is a signature dish - fire-baked, "
"unpretentious, impossible to fake. The Signature Language Method learns a "
"people through their food first, because the stomach signs before the hand."),
},
# ------------------------------------------------------- 13 travel
{
"key": "travel",
"name": "Bhojpuri Travel and Directions Sentences",
"group": "sentences",
"ladder_rank": 13,
"ladder_tier": "compounded",
"description": (
"Twenty Bhojpuri sentences for transport, asking directions, tickets, and "
"lodging. 1. स्टेशन कहाँ बा? (Where is the station?). 2. बाजार केतना दूर बा? "
"(How far is the market?). 3. बायें जाईं, फिर सीधा (Go left, then straight). "
"4. दायें मुड़ जाईं (Turn right). 5. ई रास्ता कहाँ जात बा? (Where does this road "
"go?). 6. हमके पटना जाए के बा (I have to go to Patna). 7. गाड़ी कब खुली? (When "
"does the vehicle/train leave?). 8. टिकट केतना के बा? (How much is the ticket?). "
"9. एक टिकट बनारस के दीं (Give one ticket to Banaras, please). 10. बस में बहुत "
"भीड़ बा (The bus is very crowded). 11. रेलगाड़ी लेट बिया (The train is late). "
"12. हम रिक्शा से जाइब (I will go by rickshaw). 13. नाव से नदी पार करब (We will "
"cross the river by boat). 14. हवाई जहाज से समय बचेला (Time is saved by "
"airplane). 15. साइकिल से गाँव जाइब (I will go to the village by bicycle). "
"16. इहाँ कोनो धर्मशाला बा? (Is there a lodge around here?). 17. कमरा के भाड़ा "
"केतना बा? (What is the room rent?). 18. खाना भी मिली? (Will food be available "
"too?). 19. हमार सामान गाड़ी में बा (My luggage is in the vehicle). 20. शुभ "
"यात्रा! फिर मिलब (Safe journey! See you again)."),
"how_it_works": (
"Travel sentences pivot on three question words - कहाँ (where), केतना (how "
"much/far), कब (when) - and the से postposition for means: रिक्शा से, नाव से, "
"साइकिल से. Directions use the polite जाईं form to strangers (बायें जाईं) and "
"bare stems to drivers you know. जाए के बा marks obligation: हमके पटना जाए के "
"बा (I have to go to Patna). Lodging words: धर्मशाला (lodge), कमरा (room), "
"भाड़ा (rent), सामान (luggage). Practice by giving directions from your home "
"to the nearest market entirely in Bhojpuri."),
"key_points": [
"20 travel and direction sentences with translations.",
"Three travel questions: कहाँ, केतना, कब.",
"Means of travel: से - रिक्शा से, नाव से, साइकिल से.",
"Directions: बायें, दायें, सीधा; polite जाईं to strangers.",
"Obligation: जाए के बा (हमके पटना जाए के बा).",
"Ticket words: टिकट, भाड़ा, गाड़ी, रेलगाड़ी.",
"Lodging: धर्मशाला, कमरा, सामान.",
"Give real directions from your home in Bhojpuri.",
],
"requirements": [
"Ask and answer where/how-much/when questions aloud.",
"Give directions to three real places in Bhojpuri.",
"Buy a (pretend) ticket in one full polite sentence.",
],
"standards": [
"Place names: Patna, Banaras per standard usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
"Shukla, Shaligram. Bhojpuri Grammar. 1968.",
],
"sig_lens": (
"His Signature reading: every journey is a signature across distance - कहाँ "
"the question, केतना the cost, शुभ यात्रा the seal. The Signature Language "
"Method learns the road words first, because a traveler who can ask can never "
"be lost."),
},
# ------------------------------------------------------- 14 work/school
{
"key": "work",
"name": "Bhojpuri Work and School Sentences",
"group": "sentences",
"ladder_rank": 14,
"ladder_tier": "compounded",
"description": (
"Twenty Bhojpuri sentences about jobs, the office, the classroom, and "
"learning. 1. हम किसान बानी (I am a farmer). 2. उ दफ्तर में काम करत बा (He "
"works in an office). 3. हमार नौकरी शहर में बा (My job is in the city). "
"4. काम बिहान आठ बजे शुरू होला (Work starts at eight in the morning). 5. तनख्वाह "
"महीना में मिलेला (Salary comes monthly). 6. आज छुट्टी बा (Today is a holiday). "
"7. मालिक बहुत नीक बाड़न (The boss is very good - respectful). 8. हमके तरक्की "
"चाहीं (I want a promotion). 9. लइका स्कूल जात बा (The boy goes to school). "
"10. मास्टर जी पढ़ावत बाड़न (The teacher is teaching - respectful). 11. किताब "
"खोल के पढ़ऽ (Open the book and read). 12. पाठ याद करऽ (Memorize the lesson). "
"13. परीक्षा काल्ह से बा (Exams start tomorrow). 14. हम परीक्षा पास करब (I will "
"pass the exam). 15. गणित कठिन बा "
"(Math is difficult). 16. भोज्पुरी हमार प्रिय विषय हऽ (Bhojpuri is my favorite "
"subject). 17. कॉपी में लिखऽ (Write in the notebook). 18. सवाल पूछे में शरमाव "
"मत (Do not be shy to ask questions). 19. पढ़ाई में मन लगावऽ (Put your heart "
"into studying). 20. विद्या सबसे बड़ धन हऽ (Learning is the greatest wealth)."),
"how_it_works": (
"Work sentences use the professional vocabulary - नौकरी, दफ्तर, तनख्वाह, "
"मालिक, छुट्टी - with respectful बाड़न for bosses and teachers. होला/मिलेला "
"mark routine truths: काम आठ बजे शुरू होला. School sentences run on commands "
"in the familiar stem (खोल, पढ़ऽ, करऽ, लिखऽ) because the classroom is "
"family-like, but मास्टर जी always gets बाड़न. The proverb विद्या सबसे बड़ धन "
"हऽ (learning is the greatest wealth) is the traditional blessing over every "
"Bhojpuri student's books. Practice by describing your own work or studies in "
"five Bhojpuri sentences."),
"key_points": [
"20 work and school sentences with translations.",
"Work set: किसान, नौकरी, दफ्तर, तनख्वाह, मालिक, छुट्टी.",
"School set: मास्टर जी, पाठ, परीक्षा, कॉपी, गणित.",
"बाड़न for bosses and teachers - respect is grammar.",
"होला/मिलेला mark routines: काम आठ बजे शुरू होला.",
"Classroom commands use familiar stems: खोल, पढ़ऽ, लिखऽ.",
"विद्या सबसे बड़ धन हऽ - the student's blessing.",
"Describe your own work in five Bhojpuri sentences.",
],
"requirements": [
"Describe your job or studies in five Bhojpuri sentences.",
"Give three classroom commands in the familiar stem.",
"Use बाड़न for a teacher or elder in one sentence.",
],
"standards": [
"Vocabulary per standard Bhojpuri usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968.",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
],
"sig_lens": (
"His Signature reading: काम is the signature written daily - the field, the "
"office, the classroom each a page. The Signature Language Method signs the "
"work words with respect, because विद्या सबसे बड़ धन हऽ - learning is the "
"greatest wealth, and wealth must be signed for."),
},
# ------------------------------------------------------- 15 health/body
{
"key": "health",
"name": "Bhojpuri Health and Body Sentences",
"group": "sentences",
"ladder_rank": 15,
"ladder_tier": "compounded",
"description": (
"Twenty Bhojpuri sentences about body parts, symptoms, the doctor visit, and "
"the pharmacy. 1. हमार माथा दुखत बा (My head aches). 2. हमरा बुखार बा (I have a "
"fever - हमरा + बा = I have). 3. खाँसी बहुत आवत बिया (I have a bad cough). "
"4. पेट में दर्द बा (There is pain in the stomach). 5. गोड़ में चोट लागल बा (My "
"leg is hurt). 6. आँख लाल बिया (The eyes are red). 7. कान बहत बा (The ear is "
"discharging). 8. दाँत दुखत बा (The tooth aches). 9. हमके चक्कर आवत बा (I feel "
"dizzy). 10. उल्टी आवत बिया (feeling nauseous). 11. डॉक्टर "
"साहब, देखीं ना (Doctor, please have a look). 12. दवाई समय पर खाईं (Take the "
"medicine on time - polite). 13. गरम पानी पीईं (Drink warm water). 14. आराम "
"करीं (Take rest). 15. अस्पताल कहाँ बा? (Where is the hospital?). 16. दवाखाना "
"बाजार में बा (The pharmacy is in the market). 17. ई दवाई दिन में दू बार लीं "
"(Take this medicine twice a day). 18. खाना हल्का खाईं (Eat light food). 19. अब "
"तबीयत ठीक बा (I am feeling better now). 20. भगवान करे जल्दी ठीक हो जाईं "
"(May God make you well soon - the blessing)."),
"how_it_works": (
"Body sentences use हमरा/हमार + बा for 'I have': हमरा बुखार बा (I have fever), "
"हमार माथा दुखत बा (my head aches). Symptoms take the continuous: दुखत, आवत, "
"बहुत. Doctor-visit language is polite by rule: देखीं ना, खाईं, करीं, लीं - the "
"-ीं endings carry the respect a sick person is owed. Body parts to memorize "
"as a set: माथा (head), आँख (eye), कान (ear), नाक (nose), मुँह (mouth), दाँत "
"(tooth), हाथ (hand), गोड़ (leg/foot), पेट (stomach), देह (body). The blessing "
"भगवान करे जल्दी ठीक हो जाईं closes every health conversation. Practice by "
"describing one symptom and one remedy in Bhojpuri."),
"key_points": [
"20 health and body sentences with translations.",
"'I have' = हमरा/हमार + noun + बा: हमरा बुखार बा.",
"Symptom verbs: दुखत (aches), आवत (coming), लागल (hurt).",
"Doctor language is always polite: देखीं, खाईं, करीं, लीं.",
"Body set: माथा, आँख, कान, नाक, मुँह, दाँत, हाथ, गोड़, पेट, देह.",
"Pharmacy: दवाखाना; dosage: दिन में दू बार.",
"Blessing: भगवान करे जल्दी ठीक हो जाईं.",
"Describe one symptom and one remedy in Bhojpuri.",
],
"requirements": [
"Memorize the ten body parts.",
"Role-play a doctor visit with polite -ीं forms.",
"Give the health blessing to someone in Bhojpuri.",
],
"standards": [
"Medical vocabulary per standard Bhojpuri usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968.",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
],
"sig_lens": (
"His Signature reading: the body is the first document ever signed - देह the "
"paper, every ache a marginal note. The Signature Language Method learns the "
"body words with a healer's respect, because these are the sentences people "
"say when it matters most."),
},
# ------------------------------------------------------- 16 emotions
{
"key": "emotions",
"name": "Bhojpuri Emotions and Feelings Sentences",
"group": "sentences",
"ladder_rank": 16,
"ladder_tier": "compounded",
"description": (
"Twenty Bhojpuri sentences about happiness, sadness, anger, fear, love, and "
"surprise. 1. हम बहुत खुश बानी (I am very happy). 2. आज मन गदगद बा (My heart is "
"overflowing with joy today). 3. ओकरा बधाई मिलल (He received congratulations - "
"event-focus, no blame). 4. हमरा दुख बा (I am sad). 5. उ रोवत बिया (She is "
"crying). 6. आँख से आँसू गिरत बा (Tears are falling from the eyes). 7. ओकरा "
"गुस्सा आइल बा (He has become angry). 8. गुस्सा में मत बोलऽ (Do not speak in "
"anger). 9. शांत हो जाऽ (Calm down). 10. हमके डर लागत बा (I am afraid). 11. अँधेरा "
"में डर लागेला (Darkness causes fear). 12. हिम्मत रखऽ (Keep courage). 13. हम "
"तोहरा से बहुत प्यार करीले (I love you very much). 14. माई-बाबूजी के आशीर्वाद "
"मिलल (Received the blessings of mother and father). 15. दिल धड़कत बा (My heart "
"is pounding). 16. ई सुन के हम हैरान बानी (I am surprised to hear this). "
"17. का बात बा! (What a thing! - expression of surprise). 18. हमके गर्व बा (I am "
"proud). 19. शर्म से मुँह लाल हो गइल (The face turned red with shame). 20. मन "
"शांत बा, सब ठीक बा (The mind is calm; all is well)."),
"how_it_works": (
"Emotion sentences use हमके/ओकरा + noun + बा for states that 'come to' you: "
"हमके डर लागत बा (fear is striking me), ओकरा गुस्सा आइल बा (anger came to him). "
"This is the Bhojpuri way - feelings arrive like weather, you do not manufacture "
"them. खुश/दुखी describe the person directly: हम खुश बानी. Commands about "
"feelings use the familiar stem: शांत हो जाऽ, हिम्मत रखऽ, गुस्सा में मत बोलऽ. "
"Practice by naming your own feeling three times a day in Bhojpuri."),
"key_points": [
"20 emotion sentences with translations.",
"Feelings 'arrive': हमके डर लागत बा, ओकरा गुस्सा आइल बा.",
"Direct states: हम खुश बानी, हमरा दुख बा.",
"Feeling commands: शांत हो जाऽ, हिम्मत रखऽ, मत बोलऽ.",
"Surprise: का बात बा!; pride: हमके गर्व बा.",
"Love: हम तोहरा से बहुत प्यार करीले.",
"Blessings: आशीर्वाद मिलल - event-focus grammar.",
"Name your feeling in Bhojpuri three times daily.",
],
"requirements": [
"Learn the six emotion roots: खुशी, दुख, गुस्सा, डर, प्यार, हैरानी.",
"Use the 'arrival' pattern for three feelings.",
"Give one feeling-command and one blessing aloud.",
],
"standards": [
"Emotion vocabulary per living Bhojpuri usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
"Shukla, Shaligram. Bhojpuri Grammar. 1968.",
],
"sig_lens": (
"His Signature reading: feelings are the ink's color - खुशी blue-black, गुस्सा "
"red, दुख grey. The Signature Language Method lets feelings arrive like "
"weather and signs them honestly, because a forged feeling fools no one."),
},
# ------------------------------------------------------- 17 nature/weather
{
"key": "nature",
"name": "Bhojpuri Nature and Weather Sentences",
"group": "sentences",
"ladder_rank": 17,
"ladder_tier": "compounded",
"description": (
"Twenty Bhojpuri sentences about animals, plants, seasons, and weather talk. "
"1. बरसात होत बा (It is raining). 2. घाम बहुत तेज बा "
"(The sunshine is very strong). 3. हवा चलत बिया (The wind is blowing). 4. करिया "
"बादल छा गइल (Black clouds have gathered). 5. बिजली कड़कत बिया (Lightning is "
"flashing). 6. जाड़ा में कोहरा पड़ेला (There is fog in winter). 7. गर्मी में लू "
"चलेला (The hot wind blows in summer). 8. बसंत में फूल खिलेला (Flowers bloom in "
"spring). 9. गंगा में पानी बढ़ गइल (The water rose in the Ganges). 10. नदी किनारे "
"पेड़ बा (There is a tree on the riverbank). 11. बगीचा में आम फरल बा (Mangoes "
"have fruited in the orchard). 12. खेत में धान लागल बा (Paddy is planted in the "
"field). 13. गाय चरत बिया (The cow is grazing). 14. भैंस तालाब में नहात बिया "
"(The buffalo is bathing in the pond). 15. चिरई चहचहात बिया (The bird is "
"chirping). 16. मछरी पानी में तैरत बिया (The fish is swimming in the water). "
"17. साँप बिल में घुसल (The snake slipped into its hole). 18. बानर पेड़ पर "
"कूदत बा (The monkey is jumping on the tree). 19. हाथी जंगल में रहेला (The "
"elephant lives in the forest). 20. मौसम बहुत सुहावन बा (The weather is very "
"pleasant)."),
"how_it_works": (
"Weather in Bhojpuri is something that happens, not something that is: बरसात "
"होत बा (rain is happening), घाम बा (there is sunshine), हवा चलत बिया. The "
"seasons each bring their verb: जाड़ा में कोहरा पड़ेला, गर्मी में लू चलेला, "
"बसंत में फूल खिलेला - the -ेला ending marks nature's routines. Animal "
"sentences use the true Bhojpuri names: चिरई (bird), मछरी (fish), बानर (monkey) "
"- saying चिरई instead of the Hindi चिड़िया marks the insider. Farm "
"words: धान (paddy), बगीचा (orchard), खेत (field), गंगा (the Ganges). Practice "
"by describing today's weather in three Bhojpuri sentences every morning."),
"key_points": [
"20 nature and weather sentences with translations.",
"Weather 'happens': बरसात होत बा, हवा चलत बिया.",
"Seasonal routines take -ेला: पड़ेला, चलेला, खिलेला.",
"True Bhojpuri animal names: चिरई, मछरी, बानर.",
"Farm set: धान, बगीचा, खेत, गंगा, तालाब.",
"Sky set: बादल, बिजली, कोहरा, लू, घाम.",
"Describe the morning weather in Bhojpuri daily.",
],
"requirements": [
"Memorize the Bhojpuri animal and season names.",
"Describe three weather scenes with 'happening' verbs.",
"Use one -ेला routine sentence about nature.",
],
"standards": [
"Nature vocabulary per Bhojpuri rural usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
],
"sig_lens": (
"His Signature reading: nature is the original signature - बरसात the ink, "
"घाम the seal-wax, गंगा the running line. The Signature Language Method "
"reads the weather first each day, because every other signature depends on "
"the season."),
},
# ------------------------------------------------------- 18 shopping/money
{
"key": "shopping",
"name": "Bhojpuri Shopping and Money Sentences",
"group": "sentences",
"ladder_rank": 18,
"ladder_tier": "compounded",
"description": (
"Twenty Bhojpuri sentences for the market, prices, bargaining, and paying. "
"1. बाजार चलबऽ? (Shall we go to the market?). 2. हाट बुधवार के लागेला (The "
"weekly market is held on Wednesdays). 3. ई केतना के बा? (How much is this?). "
"4. दाम बहुत बा, थोड़ा कम करीं (The price is high; reduce it a little, please). "
"5. आखिरी दाम बताईं (Tell me the final price). 6. हम पचास रुपया देब (I will give "
"fifty rupees). 7. साठ से एक पइसा ज्यादा ना देब (I will not pay a paisa more "
"than sixty). 8. तौल के दीं (Weigh it and give). 9. तरकारी ताजा बा? (Are the "
"vegetables fresh?). 10. एक किलो आलू दीं (Give one kilo of potatoes). 11. आधा "
"किलो प्याज भी (Half a kilo of onions too). 12. ई कपड़ा के रंग पक्का बा? (Is this "
"cloth's color fast?). 13. नाप के देखीं (Measure it and see). 14. बड़का साइज "
"दिखाईं (Show a bigger size). 15. पइसा खुच्चा बा? (Do you have change?). 16. सौ "
"के नोट बा, खुच्चा कर दीं (I have a hundred-rupee note; make change). 17. उधार "
"ना मिली (No credit here). 18. हिसाब कर लीं (Settle the account). 19. सामान थैली "
"में डाल दीं (Put the goods in the bag). 20. फिर अइहऽ, ग्राहक भगवान हऽ (Come "
"again; the customer is god - the shopkeeper's farewell)."),
"how_it_works": (
"Market Bhojpuri is bargaining Bhojpuri: open with ई केतना के बा?, counter "
"with दाम बहुत बा, थोड़ा कम करीं, and close with आखिरी दाम बताईं. पइसा (money) "
"is the Bhojpuri word - रुपया names the unit. Polite -ीं forms (करीं, बताईं, "
"दिखाईं, दीं) keep the haggle friendly; the walk-away line साठ से एक पइसा "
"ज्यादा ना देब does the real negotiating. Measures: किलो, आधा किलो, तौल "
"(weigh). The farewell फिर अइहऽ, ग्राहक भगवान हऽ seals the relationship for "
"next time. Practice by bargaining for three imaginary items, out loud, "
"staying polite to the end."),
"key_points": [
"20 shopping and money sentences with translations.",
"Bargaining arc: केतना के बा? -> कम करीं -> आखिरी दाम बताईं.",
"पइसा = money (Bhojpuri); रुपया = the rupee unit.",
"Polite haggling: करीं, बताईं, दिखाईं, दीं.",
"Walk-away line: साठ से एक पइसा ज्यादा ना देब.",
"Measures: किलो, आधा किलो, तौल के दीं.",
"हाट = the weekly market, held Wednesdays here.",
"Farewell: फिर अइहऽ, ग्राहक भगवान हऽ.",
],
"requirements": [
"Run a full mock bargain for three items aloud.",
"Learn the measure words and money words cold.",
"Close every bargain with the polite farewell.",
],
"standards": [
"Market vocabulary per Bhojpuri bazaar usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
],
"sig_lens": (
"His Signature reading: the bargain is a negotiation of signatures - केतना "
"the opening bid, आखिरी दाम the final stroke. The Signature Language Method "
"haggles politely to the last paisa, because ग्राहक भगवान हऽ - the customer "
"is god, and gods are signed for, not cheated."),
},
# ------------------------------------------------------- 19 friendship/social
{
"key": "social",
"name": "Bhojpuri Friendship and Social Life Sentences",
"group": "sentences",
"ladder_rank": 19,
"ladder_tier": "compounded",
"description": (
"Twenty Bhojpuri sentences about meeting people, invitations, and "
"celebrations. 1. तोहार नाम का हऽ? (What is your name?). 2. हमार नाम मोहन हऽ "
"(My name is Mohan). 3. तू कहाँ के हवऽ? (Where are you from?). 4. हम आरा के "
"बानी (I am from Arrah). 5. तोहरा से मिल के खुशी भइल (Pleased to meet you). "
"6. हम दोस्त बानी (We are friends). 7. काल्ह हमरा घर आ (Come to my house "
"tomorrow - to a friend). 8. रउआ जरूर अइहऽ (You must come - respectful "
"invitation). 9. चाय पियबऽ? (Will you have tea?). 10. साथे खाना खाइब (We will "
"eat together). 11. जन्मदिन के बधाई! (Birthday congratulations!). 12. शादी में "
"जरूर अइहऽ (Do come to the wedding). 13. बरात सात बजे निकली (The wedding "
"procession leaves at seven). 14. छठ में घर जाइब (I will go home for Chhath). "
"15. होली में रंग खेलब (We will play with colors at Holi). 16. दीवाली में दीया "
"जराइब (We will light lamps at Diwali). 17. गाँव में मेला लागल बा (A fair is on "
"in the village). 18. नाच-गाना होई (There will be dance and song). 19. सब लोग "
"इकट्ठा होखब (Everyone will gather). 20. दोस्ती सबसे बड़ दौलत हऽ (Friendship is "
"the greatest wealth)."),
"how_it_works": (
"Social Bhojpuri switches register by relationship: तू-forms (आ, खाइब, हवऽ) "
"for friends, रउआ-forms (अइहऽ, जरूर) for honored guests - sentence 7 vs 8 "
"shows the same invitation in both. Introductions follow the pattern नाम, "
"गाँव, खुशी: तोहार नाम का हऽ? तू कहाँ के हवऽ? तोहरा से मिल के खुशी भइल. "
"Festivals carry the social year: छठ (Chhath, the sun festival), होली, दीवाली, "
"मेला (fair), बरात (wedding procession). The closing proverb दोस्ती सबसे बड़ "
"दौलत हऽ is the social philosophy in one line. Practice by introducing "
"yourself fully - name, place, pleasure - in three Bhojpuri sentences."),
"key_points": [
"20 friendship and social sentences with translations.",
"Register switch: तू-forms for friends, रउआ-forms for honored guests.",
"Introduction pattern: नाम, गाँव, खुशी (name, place, pleasure).",
"Festival set: छठ, होली, दीवाली, मेला, बरात.",
"Invitations: आ (friend), जरूर अइहऽ (honored).",
"तोहरा से मिल के खुशी भइल = pleased to meet you.",
"दोस्ती सबसे बड़ दौलत हऽ - the social philosophy.",
"Introduce yourself fully in three Bhojpuri sentences.",
],
"requirements": [
"Introduce yourself (name, place, pleasure) aloud.",
"Invite a friend and an elder - feel the register switch.",
"Learn the five festival words.",
],
"standards": [
"Social vocabulary per living Bhojpuri usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
],
"sig_lens": (
"His Signature reading: friendship is a co-signed document - हम दोस्त बानी, "
"two hands on one page. The Signature Language Method introduces, invites, "
"and celebrates in the right register, because दोस्ती सबसे बड़ दौलत हऽ and "
"wealth is witnessed."),
},
# ------------------------------------------------------- 20 technology
{
"key": "tech",
"name": "Bhojpuri Technology and Communication Sentences",
"group": "sentences",
"ladder_rank": 20,
"ladder_tier": "compounded",
"description": (
"Twenty Bhojpuri sentences about phones, the internet, computers, and "
"messaging. 1. हमार मोबाइल कहाँ बा? (Where is my mobile?). 2. फोन चार्ज पर "
"लगावऽ (Put the phone on charge). 3. बैटरी खतम हो गइल (The battery died). "
"4. रउआ के फोन करब (I will call you - respectful). 5. घंटी बजत बिया (The bell "
"is ringing). 6. फोन उठावऽ (Pick up the phone). 7. नेटवर्क नइखे (There is no "
"network). 8. मैसेज भेज देब (I will send the message). 9. व्हाट्सऐप पर फोटो "
"भेजऽ (Send the photo on WhatsApp). 10. इंटरनेट चलत बा? (Is the internet "
"working?). 11. वाई-फाई के पासवर्ड का बा? (What is the Wi-Fi password?). "
"12. कंप्यूटर ऑन करऽ (Turn on the computer). 13. ईमेल खोल के देखऽ (Open the "
"email and see). 14. फोटो खींचऽ (Take a photo). 15. वीडियो बनावत बानी (I am "
"making a video). 16. टीवी पर समाचार आवत बा (News is coming on TV). 17. बिजली "
"गुल हो गइल (The power went out). 18. इन्वर्टर चालू करऽ (Switch on the "
"inverter). 19. ऑनलाइन पढ़ाई होत बिया (Study is happening online). 20. तकनीक "
"से दूरी मिट जाला (Distance disappears with technology)."),
"how_it_works": (
"Technology Bhojpuri borrows the English noun and keeps the Bhojpuri verb: "
"मोबाइल, इंटरनेट, कंप्यूटर, वाई-फाई, ईमेल stay as-is while करऽ, भेजऽ, खोलऽ, "
"लगावऽ do the work - फोन करब, मैसेज भेज देब, ईमेल खोल के देखऽ. Problems are "
"stated event-first: बैटरी खतम हो गइल, नेटवर्क नइखे, बिजली गुल हो गइल - the "
"grammar reports what happened without blame. Commands to devices use the "
"familiar stem (लगावऽ, उठावऽ, करऽ) since machines take no offense. The closing "
"line तकनीक से दूरी मिट जाला states the philosophy. Practice by narrating "
"your phone routine - charge, call, message, photo - in Bhojpuri."),
"key_points": [
"20 technology sentences with translations.",
"Borrow the noun, keep the verb: मोबाइल ... करब, ईमेल ... खोलऽ.",
"Problem reports are event-first: बैटरी खतम हो गइल, बिजली गुल हो गइल.",
"Device commands use familiar stems: लगावऽ, उठावऽ, करऽ.",
"नइखे for missing service: नेटवर्क नइखे.",
"तकनीक से दूरी मिट जाला - the philosophy.",
"Narrate your phone routine in Bhojpuri.",
],
"requirements": [
"Name ten devices and apps in Bhojpuri sentences.",
"Report three tech problems event-first.",
"Send a real message using one Bhojpuri sentence.",
],
"standards": [
"Loanwords per current Bhojpuri usage (mobile, internet, WhatsApp).",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960 (on borrowing).",
"Shukla, Shaligram. Bhojpuri Grammar. 1968.",
],
"sig_lens": (
"His Signature reading: technology is the signature gone electric - the same "
"hand, now instant across the world. The Signature Language Method borrows "
"the machine's nouns but never its manners: the verb stays Bhojpuri."),
},
# ------------------------------------------------------- 21 tenses
{
"key": "tenses",
"name": "Bhojpuri Verb Tenses in Sentences",
"group": "grammar",
"ladder_rank": 21,
"ladder_tier": "advanced",
"description": (
"Bhojpuri verb tenses with five or more translated sentences per tense. "
"THE 'BE' VERB: हम बानी (I am), तू बाड़ऽ (you are - inf), रउआ बानी (you are - "
"formal), उ बा (he/she is), हमनी बानीं जा (we are), तू लोग बाड़ऽ जा (you all "
"are), उ लोग बा (they are). PRESENT CONTINUOUS (stem + त + be): हम खात बानी "
"(I am eating), तू पढ़त बाड़ऽ (you are reading), उ खेलत बा (he is playing), "
"माई बनावत बिया (mother is cooking), लइका सुतत बा (the child is sleeping), "
"हमनी जात बानीं जा (we are going). SIMPLE PAST (-ल participle): ऊ गइल (he "
"went), उ आइल (he came), ई भइल (this happened), कुर्सी टूट गइल (the chair "
"broke), रात हो गइल (night fell), काम हो गइल (the work got done). PRESENT "
"PERFECT (participle + be): हम खइले बानी (I have eaten), उ गइल बा (he has "
"gone), तू आइल बाड़ऽ (you have come), माई बना लेले बिया (mother has cooked), "
"हम देखले बानी (I have seen), उ सुनले बा (he has heard). FUTURE (stem + ब): हम "
"जाइब (I will go), तू खइबऽ (you will eat), उ आई (he will come), हमनी करब जा (we "
"will do), रउआ देखब (you will see - formal), बरसात होई (it will rain). PAST "
"CONTINUOUS (stem + त + रहल): उ खात रहल (he was eating), माई बनावत रहल (mother "
"was cooking), लइका खेलत रहल (the child was playing), हम "
"पढ़त रहल बानी (I was reading), पानी बरसत रहल (it was raining). COMMAND: खा "
"(eat!), जा (go!), आ (come!), देख (look!), सुन (listen!) - and polite: खाईं "
"(please eat), आईं (please come), बइठीं (please sit), करीं (please do)."),
"how_it_works": (
"The Bhojpuri tense machine has four moving parts: the stem (खा), the -त "
"marker for ongoing action, the -ल participle for completed action, and the "
"-ब marker for the future, plus the 'be' helpers (बानी/बाड़ऽ/बा) that point at "
"the person. Assemble: present = stem+त+be (खात बानी); perfect = -ल+be (खइले "
"बानी); past event = bare -ल (गइल, भइल); future = stem+ब (जाइब). There is no "
"'ne' - the doer stays in the plain form and the verb agrees with it. Drill "
"one verb (कर) through all six frames aloud: करत बानी, कइले बानी, कइल, करब, "
"करत रहल, कर - then do खा, जा, देख the same way."),
"key_points": [
"'Be': बानी (I), बाड़ऽ (you inf), बा (he/she), बानीं जा (we).",
"Present continuous: stem + त + be - खात बानी.",
"Present perfect: -ल participle + be - खइले बानी.",
"Simple past events: bare -ल - गइल, आइल, भइल, टूट गइल.",
"Future: stem + ब - जाइब, खाइब, करब, होई.",
"Past continuous: stem + त + रहल - खात रहल.",
"Commands: bare stem familiar (खा), -ीं polite (खाईं).",
"No 'ne' ergative - the verb agrees with the doer.",
"Drill कर/खा/जा/देख through all six frames aloud.",
],
"requirements": [
"Conjugate कर, खा, जा, देख in all six frames.",
"Write five sentences in each tense about your yesterday and tomorrow.",
"Explain the no-'ne' rule to someone in one sentence.",
],
"standards": [
"Tense system per Shukla 1968 and Grierson LSI Vol. V.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968 (verb system).",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
],
"sig_lens": (
"His Signature reading: tense is the signature's date-stamp - बा for now, "
"गइल for done, जाइब for promised. The Signature Language Method dates every "
"action honestly, because an undated signature is a rumor."),
},
# ------------------------------------------------------- 22 questions/answers
{
"key": "qa",
"name": "Bhojpuri Questions and Answers",
"group": "sentences",
"ladder_rank": 22,
"ladder_tier": "advanced",
"description": (
"Twenty Bhojpuri question-and-answer pairs covering who, what, where, when, "
"why, and how. 1. तू के हवऽ? - हम मोहन बानी। (Who are you? - I am Mohan.) "
"2. ई का हऽ? - ई किताब हऽ। (What is this? - This is a book.) 3. घर कहाँ बा? - "
"घर गाँव में बा। (Where is the house? - The house is in the village.) 4. तू कब "
"आइबऽ? - हम काल्ह आइब। (When will you come? - I will come tomorrow.) 5. तू काहे "
"रोवत बाड़ऽ? - हमार खिलौना टूट गइल। (Why are you crying? - My toy broke.) "
"6. ई कइसे भइल? - पता नइखे। (How did this happen? - I do not know.) 7. केतना "
"बजल बा? - तीन बजल बा। (What time is it? - It is three o'clock.) 8. टिकट केतना "
"के बा? - पचास रुपया के। (How much is the ticket? - Fifty rupees.) 9. तू कहाँ "
"जात बाड़ऽ? - हम स्कूल जात बानी। (Where are you going? - I am going to school.) "
"10. खाना बनल? - हँ, बन गइल। (Is the food ready? - Yes, it is ready.) 11. तू "
"भोज्पुरी बोलत बाड़ऽ? - हँ, थोड़ा-थोड़ा। (Do you speak Bhojpuri? - Yes, a "
"little.) 12. पानी पीबऽ? - हँ, दीं। (Will you drink water? - Yes, give it.) "
"13. कवन रंग पसंद बा? - लाल रंग। (Which color do you like? - Red.) 14. के आइल "
"बा? - मेहमान आइल बा। (Who has come? - A guest has come.) 15. काम हो गइल? - "
"ना, अबहीं ना। (Is the work done? - No, not yet.) 16. तू ठीक बाड़ऽ? - हँ, ठीक "
"बानी। (Are you well? - Yes, I am well.) 17. बरसात होई? - लागत बा होई। (Will "
"it rain? - It looks like it will.) 18. ई केकर बा? - ई हमार बा। (Whose is "
"this? - This is mine.) 19. तू काल्ह कहाँ रहलऽ? - हम घर रहल बानी। (Where were "
"you yesterday? - I was at home.) 20. अब का करब? - अब खाना खाइब। (What now? - "
"Now we will eat.)"),
"how_it_works": (
"Question words open the sentence and word order never changes: तू के हवऽ? "
"keeps subject-verb at the end just like a statement. के/का/कहाँ/कब/काहे/कइसे/"
"केतना/कवन cover every question; yes/no questions just rise in intonation - "
"तू जाइबऽ? - and are answered हँ (yes) or ना (no), often with अबहीं ना (not "
"yet). Answers mirror the question's verb: केतना बजल बा? - तीन बजल बा. केकर "
"(whose) is के + कर. Practice by interviewing a friend: ten questions, all "
"answered in full Bhojpuri sentences, no one-word replies."),
"key_points": [
"20 Q/A pairs: who, what, where, when, why, how, how much, which, whose.",
"Question words open; SOV order never changes.",
"Yes/no questions rise in intonation; answer हँ or ना.",
"Answers mirror the question's verb: बजल बा? - बजल बा.",
"केकर = whose (के + कर).",
"अबहीं ना = not yet.",
"Interview a friend: ten full-sentence Q/A rounds.",
],
"requirements": [
"Ask all nine question types aloud without notes.",
"Answer each with a full sentence, never one word.",
"Hold a two-minute Q/A interview in Bhojpuri.",
],
"standards": [
"Interrogatives per Shukla 1968.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968.",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
],
"sig_lens": (
"His Signature reading: a question is a signature requested - के, का, कहाँ "
"the blank lines, हँ the signing. The Signature Language Method asks in full "
"sentences and answers in full sentences, because half a question gets half "
"an answer."),
},
# ------------------------------------------------------- 23 commands
{
"key": "commands",
"name": "Bhojpuri Commands and Requests",
"group": "sentences",
"ladder_rank": 23,
"ladder_tier": "advanced",
"description": (
"Twenty Bhojpuri imperatives and polite requests - formal versus informal. "
"Informal (bare stem, to friends/juniors): 1. खा! (Eat!). 2. जा! (Go!). 3. आ! "
"(Come!). 4. देख! (Look!). 5. सुन! (Listen!). 6. बइठ! (Sit!). 7. उठ! (Get up!). "
"8. लिख! (Write!). 9. पढ़! (Read!). 10. दे! (Give!). Polite (-ीं forms, to "
"elders/strangers): 11. खाईं, रउआ (Please eat). 12. आईं, बइठीं (Please come, "
"please sit). 13. देखीं ना (Please have a look). 14. माफ करीं (Forgive me, "
"please). 15. बताईं ना (Please tell me). 16. थोड़ा ठहरीं (Please wait a "
"little). 17. पानी दीं (Please give water). 18. दरवाजा बंद कर दीं (Please close "
"the door). 19. जरा सुनाईं (Please listen a moment). 20. Negative: मत जा (Do "
"not go - informal); मत जाईं (Please do not go - polite); शोर मत करऽ (Do not "
"make noise). The pattern: stem alone commands downward or sideways; -ीं "
"requests upward. ना softens any request: देखीं ना, बताईं ना, माफ करीं ना."),
"how_it_works": (
"The Bhojpuri command has two gears. Gear one is the bare stem - खा, जा, देख - "
"for friends, children, and juniors; it is direct, not rude, among equals. "
"Gear two is the -ीं ending - खाईं, आईं, करीं, दीं - for elders, guests, and "
"strangers; it turns a command into a request. ना after the verb softens "
"further: देखीं ना is warmer than देखीं. मत negates: मत जा (informal), मत जाईं "
"(polite). Never use gear one upward - तू बइठ to a grandfather is an insult; "
"रउआ बइठीं is the love. Drill: command five objects in your room both ways - "
"किताब उठा / किताब उठाईं."),
"key_points": [
"20 commands/requests: 10 informal stems, 7 polite -ीं forms, 3 negatives.",
"Bare stem = informal (खा, जा, देख) for friends/juniors.",
"-ीं ending = polite request (खाईं, आईं, करीं) for elders/strangers.",
"ना softens: देखीं ना, बताईं ना.",
"मत negates: मत जा (informal), मत जाईं (polite).",
"Never command upward with the bare stem.",
"Drill five objects both ways: उठा / उठाईं.",
],
"requirements": [
"Give ten commands to a friend (stems) and ten requests to an elder (-ीं).",
"Soften three requests with ना.",
"Forbid three things with मत in both registers.",
],
"standards": [
"Imperative forms per Shukla 1968.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968.",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
],
"sig_lens": (
"His Signature reading: a command is a signature demanded, a request a "
"signature invited - खा takes, खाईं asks. The Signature Language Method "
"knows which gear the moment needs, because demanding from an elder voids "
"the document."),
},
# ------------------------------------------------------- 24 descriptions
{
"key": "descriptions",
"name": "Bhojpuri Descriptions of People and Places",
"group": "sentences",
"ladder_rank": 24,
"ladder_tier": "advanced",
"description": (
"Twenty Bhojpuri sentences describing people, places, and things in detail. "
"1. मोहन लम्बा आ हँसमुख बा (Mohan is tall and cheerful). 2. ओकर आँख बड़-बड़ आ "
"करिया बिया (Her eyes are big and black). 3. दादी के चेहरा पर झुर्री बा, मुस्कान "
"में ममता बा (Grandmother's face has wrinkles; her smile holds love). 4. लइका "
"दुबरा-पातर बा, बाकिर तेज बा (The boy is lean and thin, but sharp). 5. माई के "
"हाथ के खाना सबसे नीक लागेला (Mother's handmade food tastes best). 6. हमार गाँव "
"गंगा किनारे बसा बा (My village sits on the Ganges' bank). 7. गाँव के चारों ओर "
"हरियर खेत बा (Green fields surround the village on all sides). 8. आँगन में "
"नीम के ठंडा छाँव बा (Cool neem shade fills the courtyard). 9. पुरान कुआँ अबहियों "
"मीठ पानी देत बा (The old well still gives sweet water). 10. बाजार में भीड़, "
"शोर, आ रंग-बिरंग सामान बा (The market holds crowds, noise, and colorful "
"goods). 11. मंदिर के घंटी के आवाज दूर तक जात बिया (The temple bell's sound "
"travels far). 12. बरसात में नदी उफान पर बिया (In the rains the river runs "
"high). 13. जाड़ा के बिहान कोहरा से ढकल रहेला (Winter mornings stay wrapped in "
"fog). 14. सावन के हरियाली मन मोह लेले (Saavan's greenery steals the heart). "
"15. ई किताब पुरान बिया, बाकिर ज्ञान से भरल बिया (This book is old but full of "
"wisdom). 16. लिट्टी के खुशबू दूर से आवत बिया (The aroma of litti comes from "
"afar). 17. ओकर आवाज में मिठास बा (There is sweetness in her voice). 18. घोड़ा "
"तेज दउड़त बा, धूल उड़त बिया (The horse runs fast; dust flies). 19. रात में तारा "
"चमकत बा, चाँद मुस्कात बा (Stars shine at night; the moon smiles). 20. भोज्पुरी "
"माटी के भाषा हऽ, माटी जइसन सोंधी (Bhojpuri is the language of the soil, "
"fragrant like the soil itself)."),
"how_it_works": (
"Descriptions stack adjectives before the noun and let the verb agree: लम्बा "
"आ हँसमुख बा, बड़-बड़ आ करिया बिया. बाकिर (but) turns the sentence: दुबरा-पातर "
"बा, बाकिर तेज बा. The senses get their own verbs: खुशबू आवत बिया (aroma "
"comes), आवाज जात बिया (sound travels), स्वाद लागेला (taste strikes). "
"Reduplication intensifies: बड़-बड़ (very big), रंग-बिरंग (multicolored). "
"Place descriptions open with the location: गाँव के चारों ओर, आँगन में, बाजार "
"में. The closing line is the philosophy: भोज्पुरी माटी के भाषा हऽ. Practice by "
"describing one person and one place you love, five sentences each."),
"key_points": [
"20 detailed descriptions with translations.",
"Stack adjectives: लम्बा आ हँसमुख बा; बड़-बड़ आ करिया बिया.",
"बाकिर (but) turns the description.",
"Sense verbs: खुशबू आवत बिया, आवाज जात बिया, स्वाद लागेला.",
"Reduplication intensifies: बड़-बड़, रंग-बिरंग.",
"Places open with location: गाँव के चारों ओर, आँगन में.",
"भोज्पुरी माटी के भाषा हऽ - the philosophy.",
"Describe one loved person and one loved place, five sentences each.",
],
"requirements": [
"Describe two people with stacked adjectives.",
"Describe two places opening with location phrases.",
"Use बाकिर, one reduplication, and one sense verb.",
],
"standards": [
"Descriptive idiom per living Bhojpuri usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
],
"sig_lens": (
"His Signature reading: description is the signature illuminated - every "
"adjective a gold leaf, every sense verb a color. The Signature Language "
"Method describes until the reader can smell the लिट्टी, because a pale "
"description is an unsigned page."),
},
# ------------------------------------------------------- 25 story I
{
"key": "story1",
"name": "Bhojpuri Story I: The Farmer and the River",
"group": "stories",
"ladder_rank": 25,
"ladder_tier": "advanced",
"description": (
"A ten-sentence simple Bhojpuri story in the present tense, with "
"line-by-line English translation. 1. एगो किसान गंगा किनारे रहत बा। (A farmer "
"lives on the bank of the Ganges.) 2. ओकर नाम रामधन हऽ। (His name is Ramdhan.) "
"3. उ रोज बिहान खेत जात बा। (He goes to the field every morning.) 4. ओकर खेत "
"में धान लागल बा। (Paddy is planted in his field.) 5. दुपहरिया में उ पेड़ के "
"छाँव में बइठत बा। (At noon he sits in the tree's shade.) 6. उ आपन रोटी गंगा "
"के पानी से खात बा। (He eats his bread with Ganges water.) 7. साँझ के उ घर "
"लौटत बा। (In the evening he returns home.) 8. ओकर लइका दुआर पर इंतजार करत "
"बा। (His child waits at the door.) 9. माई गरम खाना परोसत बिया। (Mother serves "
"hot food.) 10. किसान कहत बा - मेहनत के फल मीठ होला। (The farmer says - the "
"fruit of labor is sweet.)"),
"how_it_works": (
"This story stays in the present - रहत बा, जात बा, खात बा, कहत बा - so the "
"learner reads ten clean subject-object-verb sentences without tense "
"switches. Each line adds one new word to the farm set: किसान, गंगा, खेत, "
"धान, छाँव, रोटी, दुआर, माई. The -त continuous carries the whole narrative "
"like a river's current, and the last line lands the moral: मेहनत के फल मीठ "
"होला. Read it aloud three times: first slowly for the words, second for the "
"flow, third from memory. Then retell it in your own words."),
"key_points": [
"10-sentence story, present tense, line-by-line translation.",
"One tense throughout: -त continuous (रहत, जात, खात, कहत).",
"Farm vocabulary grows line by line: किसान, खेत, धान, छाँव.",
"Clean SOV in every line.",
"Moral: मेहनत के फल मीठ होला (the fruit of labor is sweet).",
"Read three times: words, flow, memory - then retell.",
],
"requirements": [
"Read the story aloud three times.",
"Retell it in your own Bhojpuri words.",
"Write one new final line with your own moral.",
],
"standards": [
"Story Bhojpuri per standard usage; moral in proverb form.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960 (folk narrative).",
],
"sig_lens": (
"His Signature reading: a story is a signature in ten strokes - each sentence "
"a pen-lift, the moral the final flourish. The Signature Language Method "
"reads the farmer's day until the learner can sign a day of his own."),
},
# ------------------------------------------------------- 26 story II
{
"key": "story2",
"name": "Bhojpuri Story II: The Market Day",
"group": "stories",
"ladder_rank": 26,
"ladder_tier": "advanced",
"description": (
"A ten-sentence Bhojpuri story in the past tense, with line-by-line English "
"translation. 1. काल्ह गाँव में हाट लागल। (Yesterday the weekly market was "
"held in the village.) 2. रामधन बिहानहीं उठल। (Ramdhan woke early in the "
"morning.) 3. उ बैलगाड़ी लेके निकलल। (He set out with his bullock cart.) "
"4. रास्ता में ओकर दोस्त मिलल। (His friend met him on the way.) 5. दूनों मिल "
"के हाट गइल। (Both went to the market together.) 6. रामधन धान बेच के पइसा "
"पावल। (Ramdhan sold paddy and got money.) 7. पइसा से उ माई खातिर साड़ी "
"किनल। (With the money he bought a sari for mother.) 8. लइका खातिर मिठाई ले "
"आइल। (He brought sweets for the child.) 9. साँझ के उ खुशी-खुशी घर लौटल। (In "
"the evening he returned home happily.) 10. माई कहली - बेटा, मेहनत कभी बेकार "
"ना जाला। (Mother said - son, labor never goes waste.)"),
"how_it_works": (
"This story runs on the -ल past participle - लागल, उठल, निकलल, मिलल, गइल, "
"पावल, किनल, आइल, लौटल, कहली - the completed-action engine of Bhojpuri "
"narrative. No 'ne', no helper verbs: the bare participle IS the past. Each "
"line moves the day forward: market held, woke, set out, met, went, sold, "
"bought, brought, returned, blessed. Feminine कहली shows the agreement at "
"work (mother said). Read it after Story I and feel the tense shift: -त was "
"the river flowing, -ल is the footprints left behind. Retell yesterday's "
"market day - real or imagined - in ten -ल sentences."),
"key_points": [
"10-sentence story, past tense, line-by-line translation.",
"The -ल participle alone is the past: लागल, उठल, गइल, पावल, किनल.",
"No 'ne', no helpers - the bare participle carries completed action.",
"कहली shows feminine agreement in the past.",
"Each line advances the day: a complete narrative arc.",
"Contrast with Story I: -त flowing vs -ल footprints.",
"Retell a real yesterday in ten -ल sentences.",
],
"requirements": [
"Read the story aloud, stressing each -ल ending.",
"List all ten past participles from memory.",
"Write ten -ल sentences about your own yesterday.",
],
"standards": [
"Past narrative per standard Bhojpuri usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960 (folk narrative).",
"Shukla, Shaligram. Bhojpuri Grammar. 1968.",
],
"sig_lens": (
"His Signature reading: the past tense is the signature dried - गइल, किनल, "
"लौटल, each stroke set and unchangeable. The Signature Language Method "
"honors what is done by signing it plainly, because the past needs no "
"flourish."),
},
# ------------------------------------------------------- 27 story III
{
"key": "story3",
"name": "Bhojpuri Story III: The Journey Ahead",
"group": "stories",
"ladder_rank": 27,
"ladder_tier": "advanced",
"description": (
"A ten-sentence Bhojpuri story in the future and conditional, with "
"line-by-line English translation. 1. रामधन के बेटा बड़ हो गइल बा। (Ramdhan's "
"son has grown up.) 2. उ शहर जाके पढ़ी। (He will go to the city and study.) "
"3. माई कहली - बेटा, मन लगा के पढ़िहऽ। (Mother said - son, study with a true "
"heart.) 4. बाबूजी पइसा जोड़ के दिहें। (Father will save and give money.) "
"5. बेटा कहत बा - हम डॉक्टर बनब। (The son says - I will become "
"a doctor.) 6. गाँव के लोग आशीर्वाद दी। (The village people will give "
"blessings.) 7. उ ट्रेन से पटना जाई। (He will go to Patna by train.) 8. हॉस्टल "
"में रह के मेहनत करी। (He will live in the hostel and work hard.) 9. पास होके "
"गाँव लौटी। (He will pass and return to the village.) 10. अगर मेहनत करब त "
"सपना जरूर पूरा होई। (If you work hard, the dream will surely come true.)"),
"how_it_works": (
"This story runs on the -ब future - जाई, पढ़ी, दिहें, बनब, दी, करी, लौटी, "
"होई - plus the conditional अगर...त (if...then) in the last line. Line 1 "
"anchors in the perfect (हो गइल बा - has grown) before the story launches "
"forward. Direct speech carries lines 3, 5, 10: कहली, कहत बा, each a "
"mini-dialogue inside the narrative. जाके, रह के, होके are the conjunctive "
"participles (having gone, having stayed, having passed) that chain actions: "
"शहर जाके पढ़ी (go to the city and study). The moral is conditional: अगर "
"मेहनत करब त सपना जरूर पूरा होई. Read all three stories in order - present, "
"past, future - and you have the whole tense system as narrative."),
"key_points": [
"10-sentence story, future + conditional, line-by-line translation.",
"The -ब future: जाई, पढ़ी, बनब, करी, होई.",
"अगर...त builds the conditional: अगर मेहनत करब त सपना पूरा होई.",
"Conjunctive participles chain actions: जाके, रह के, होके.",
"Direct speech inside narrative: कहली, कहत बा.",
"Three stories = the whole tense system as narrative.",
"Write your own ten-line future story.",
],
"requirements": [
"Read all three stories in order aloud.",
"List the ten future forms from memory.",
"Write a ten-line future story about your own plans.",
],
"standards": [
"Future and conditional per Shukla 1968.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968.",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960 (folk narrative).",
],
"sig_lens": (
"His Signature reading: the future tense is the signature promised - जाई, "
"बनब, होई, each a vow in ink not yet dry. The Signature Language Method "
"makes promises in the future tense and keeps them in the past, because a "
"vow unsigned is only a wish."),
},
# ------------------------------------------------------- 28 idioms
{
"key": "idioms",
"name": "Bhojpuri Idioms and Proverbs",
"group": "idioms",
"ladder_rank": 28,
"ladder_tier": "advanced",
"description": (
"Twenty Bhojpuri idioms and proverbs - literal translation, real meaning, "
"and an example sentence each. 1. जेकर लाठी ओकर भैंस (Whose stick, his "
"buffalo - might is right): जेकर लाठी ओकर भैंस, गरीब के के सुनत बा। 2. नाच न "
"जाने आँगन टेढ़ (Knows no dance, calls the courtyard crooked - a bad workman "
"blames his tools): काम बिगाड़ के कहत बा - नाच न जाने आँगन टेढ़। 3. अधजल गगरी "
"छलकत जाए (The half-filled pot spills - empty vessels make the most noise): "
"थोड़ा पढ़ के बहुत बोलत बा, अधजल गगरी छलकत जाए। 4. जैसी करनी वैसी भरनी (As you "
"sow, so shall you reap): चोरी कइलस, पकड़ाइल - जैसी करनी वैसी भरनी। 5. ऊँट के "
"मुँह में जीरा (Cumin in a camel's mouth - a drop in the ocean): सौ रुपया के "
"कर्जा में दस रुपया - ऊँट के मुँह में जीरा। 6. एक अनार सौ बीमार (One "
"pomegranate, a hundred sick - too many claimants): नौकरी एक, अर्जीदार सौ - एक "
"अनार सौ बीमार। 7. जहाँ चाह वहाँ राह (Where there's a will, there's a way): "
"पढ़े के चाह बा त जहाँ चाह वहाँ राह। 8. मुँह में राम बगल में छुरी (Ram on the "
"lips, a knife at the side - hypocrisy): ओकरा से बच के रहऽ, मुँह में राम बगल "
"में छुरी। 9. घर की मुर्गी दाल बराबर (The home chicken equals dal - familiarity "
"breeds contempt): घर के डॉक्टर के के पूछत बा - घर की मुर्गी दाल बराबर। "
"10. साँच को आँच नहीं (Truth fears no trial): डर मत, साँच को आँच नहीं। 11. छोट "
"मुँह बड़ी बात (Small mouth, big talk - speaking above one's station): लइका "
"होके बड़-बड़ बात - छोट मुँह बड़ी बात। 12. दूध का दूध पानी का पानी (Milk's milk, "
"water's water - fair judgment): पंचायत में दूध का दूध पानी का पानी होई। "
"13. न रहेगा बाँस न बजेगी बाँसुरी (No bamboo, no flute - remove the cause): "
"झगड़ा के जड़ काट दऽ - न रहेगा बाँस न बजेगी बाँसुरी। 14. मन चंगा तो कठौती में "
"गंगा (If the mind is pure, the Ganges is in the water-pot): मन चंगा तो कठौती "
"में गंगा, मंदिर जाए के का जरूरत। 15. अब पछताए होत क्या जब चिड़िया चुग गई खेत "
"(What use repenting when the bird has eaten the field - too late): अब रोवत "
"बाड़ऽ - अब पछताए होत क्या जब चिड़िया चुग गई खेत। 16. काला अक्षर भैंस बराबर "
"(Black letters equal buffalo - illiterate): पढ़ल-लिखल नइखे, ओकरा खातिर काला "
"अक्षर भैंस बराबर। 17. करत-करत अभ्यास ते जड़मति होत सुजान (By practice even the "
"dull become wise): रोज पढ़ऽ - करत-करत अभ्यास ते जड़मति होत सुजान। 18. लालच बुरी "
"बला हऽ (Greed is a curse): ज्यादा के चक्कर में सब गँवाइलस - लालच बुरी बला हऽ। "
"19. मेहनत के फल मीठ होला (The fruit of labor is sweet): खेत में पसीना बहावलस, "
"आज खुश बा - मेहनत के फल मीठ होला। 20. भोज्पुरी माटी के भाषा हऽ (Bhojpuri is "
"the language of the soil): ई कहावत ना, पहचान हऽ - भोज्पुरी माटी के भाषा हऽ।"),
"how_it_works": (
"Proverbs are Bhojpuri's compressed philosophy - each one a whole argument in "
"a single line, deployed to settle debates, bless children, and warn the "
"greedy. They run on vivid village images: लाठी and भैंस, गगरी, ऊँट, अनार, "
"बाँसुरी. Use them the way speakers do: drop the proverb AFTER your point as "
"the seal - ... - जेकर लाठी ओकर भैंस। Many are shared across Hindi and "
"Bhojpuri (जैसी करनी वैसी भरनी, नाच न जाने आँगन टेढ़); the Bhojpuri flavor is "
"in the delivery and the -हऽ/-बा endings. Learn five by heart and use one per "
"day; a proverb used rightly earns more respect than a paragraph."),
"key_points": [
"20 idioms/proverbs: literal meaning + real meaning + example sentence.",
"Village images carry the wisdom: लाठी, भैंस, गगरी, ऊँट, अनार.",
"Deploy AFTER your point as the seal, not before.",
"Shared with Hindi but Bhojpuri in delivery and endings.",
"Learn five by heart; use one per day.",
"जेकर लाठी ओकर भैंस settles power; साँच को आँच नहीं settles fear.",
"मेहनत के फल मीठ होला blesses every worker.",
],
"requirements": [
"Memorize five proverbs with their literal images.",
"Use one proverb correctly in conversation today.",
"Explain three proverbs' real meanings to someone.",
],
"standards": [
"Proverbs per Bhojpuri folk tradition (Tiwari 1960).",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960 (proverbs).",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
],
"sig_lens": (
"His Signature reading: a proverb is a signature of the whole village - "
"जेकर लाठी ओकर भैंस signed by every grandfather at once. The Signature "
"Language Method collects them like seals, because one proverb rightly "
"placed outweighs a page of argument."),
},
# ------------------------------------------------------- 29 registers
{
"key": "registers",
"name": "Bhojpuri Formal and Polite Registers",
"group": "registers",
"ladder_rank": 29,
"ladder_tier": "advanced",
"description": (
"Fifteen formal-versus-informal Bhojpuri pairs for letters, business, and "
"elders, with translations. 1. Informal: तू कहाँ जात बाड़ऽ? / Formal: रउआ "
"कहाँ जात बानी? (Where are you going?). 2. तू बइठऽ। / रउआ बइठीं। (Sit - "
"informal / please sit). 3. तू खा। / रउआ खाईं। (Eat / please eat). 4. तोहार "
"नाम का हऽ? / राउर नाम का हऽ? (What is your name? - informal / respectful). "
"5. तू काल्ह आ। / रउआ काल्ह जरूर अइहऽ। (Come tomorrow / do come tomorrow - "
"honored). 6. ई ले। / ई लेईं ना। (Take this / please take this). 7. तू सुनत "
"बाड़ऽ? / रउआ सुनत बानी? (Are you listening?). 8. मत करऽ। / मत करीं ना। (Do "
"not do it - informal / polite). 9. तू ठीक बाड़ऽ? / रउआ ठीक बानी? (Are you "
"well?). 10. Letter opening informal: प्यारे भाई, / formal: आदरणीय महोदय, "
"(Dear brother / Respected sir). 11. Letter closing informal: तोहार भाई, मोहन "
"/ formal: भवदीय, मोहन (Your brother, Mohan / Yours faithfully, Mohan). "
"12. Business: दाम कम करऽ। / कृपया दाम कम करीं। (Reduce the price - blunt / "
"please). 13. Elder blessing-seeking: आशीर्वाद दऽ। / आशीर्वाद दीं ना। (Give "
"blessings - familiar / respectful). 14. Apology: गलती हो गइल। / क्षमा करीं, "
"गलती हो गइल। (Mistake happened / pardon me, a mistake happened). 15. Thanks: "
"ठीक बा। / बहुत बहुत धन्यवाद, रउआ के। (Fine / thank you very much). The rule: "
"तू + stem downward or sideways; रउआ + -ीं upward. In letters the opening and "
"closing carry the register before a single verb appears."),
"how_it_works": (
"Register in Bhojpuri is a three-part system: the pronoun (तू vs रउआ), the "
"verb ending (stem vs -ीं), and the possessive (तोहार vs राउर). All three "
"must agree - रउआ with a bare stem is broken, तू with -ीं is comic. Business "
"adds कृपया (please) and ना-softening: कृपया दाम कम करीं. Letters open with "
"प्यारे (dear, informal) or आदरणीय/महोदय (respected, formal) and close with "
"तोहार (your, informal) or भवदीय (faithfully, formal). With elders, requests "
"become blessings-seeking: आशीर्वाद दीं ना. Practice by rewriting five "
"informal sentences into full formal register - pronoun, verb, and possessive "
"all shifted."),
"key_points": [
"15 formal/informal pairs: speech, letters, business, elders.",
"Three-part agreement: pronoun + verb ending + possessive.",
"तू + stem (down/sideways); रउआ + -ीं (upward).",
"रउआ with bare stem is broken; तू with -ीं is comic.",
"Business: कृपया + -ीं + ना-softening.",
"Letters: प्यारे/तोहार (informal) vs आदरणीय/महोदय/भवदीय (formal).",
"Elders: requests become blessing-seeking (आशीर्वाद दीं ना).",
"Rewrite five informal sentences into full formal register.",
],
"requirements": [
"Convert ten informal sentences to formal, all three parts shifted.",
"Write one formal letter opening and closing.",
"Address an elder correctly in three requests.",
],
"standards": [
"Register system per Shukla 1968 and living usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968 (honorifics).",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
],
"sig_lens": (
"His Signature reading: register is the signature's dress code - तू the "
"work shirt, रउआ the formal coat. The Signature Language Method never "
"underdresses upward, because a signature in the wrong clothes is refused "
"at the door."),
},
# ------------------------------------------------------- 30 complex
{
"key": "complex",
"name": "Bhojpuri Compound and Complex Sentences",
"group": "sentences",
"ladder_rank": 30,
"ladder_tier": "advanced",
"description": (
"Fifteen long Bhojpuri sentences with clauses, connectors, and relative "
"clauses - each parsed and translated. 1. हम बाजार "
"गइल बानी आ तरकारी किनले बानी। (I went to the market and bought vegetables - "
"perfect + perfect, joined by आ.) 2. जब बरसात होत बिया त छाता लेके निकलीं। "
"(When it rains, take an umbrella - जब...त conditional.) 3. जे मेहनत करेला उ "
"सफल होला। (Whoever works hard succeeds - जे...उ relative.) 4. ई ऊ किताब हऽ जे "
"काल्ह किनले बानी। (This is the book that I bought yesterday - जे relative.) "
"5. अगर तू जल्दी अइबऽ त गाड़ी मिल जाई। (If you come early, you will catch the "
"vehicle - अगर...त.) 6. उ एतना तेज दउड़ल कि सब देखत रह "
"गइल। (He ran so fast that everyone kept watching - एतना...कि.) 7. बाकिर "
"बरसात भइल, तबहूँ मेला लागल। (But it rained, yet the fair was held - बाकिर/"
"तबहूँ.) 8. ना ऊ आइल, ना ऊ आइल, ना कवनो खबर भेजल। "
"(Neither he came, nor did he send any news - ना...ना.) 9. चाहे बरसात होखे "
"चाहे घाम, काम होई। (Whether it rains or shines, the work will be done - "
"चाहे...चाहे.) 10. जइसन बाप तइसन बेटा। (Like father, like son - जइसन...तइसन.) "
"11. हम सोचत बानी कि काल्ह का होई। (I am thinking what will happen tomorrow - "
"कि clause.) 12. ओकरा मालूम बा कि परीक्षा कठिन बा। (He knows that the exam is "
"difficult - कि.) 13. एतना पढ़ऽ कि पास हो जाऽ। (Study so much that you pass - "
"कि result.) 14. पहिले खाना खा, तब पढ़ऽ। (First eat, then study - पहिले...तब.) "
"15. जेतना मेहनत करबऽ, ओतना फल पाइबऽ। (The harder you work, the more fruit you "
"get - जेतना...ओतना.)"),
"how_it_works": (
"Complex Bhojpuri sentences chain simple SOV clauses with paired connectors: "
"जब...त (when...then), अगर...त (if...then), जे...उ (who...he), जइसन...तइसन "
"(like...like), जेतना...ओतना (the more...the more), एतना...कि (so...that), "
"चाहे...चाहे (whether...or), ना...ना (neither...nor), पहिले...तब (first...then), "
"बाकिर/तबहूँ (but/yet). The कि introduces reported thought and result: सोचत "
"बानी कि..., एतना पढ़ऽ कि.... Relative जे usually pairs with उ in the main "
"clause: जे मेहनत करेला उ सफल होला. Build long sentences by joining two short "
"ones you already know with one connector pair - then three. Parse each of "
"the fifteen above: find the connector pair, split the clauses, translate "
"each half."),
"key_points": [
"15 parsed complex sentences with connector pairs.",
"Paired connectors: जब...त, अगर...त, जे...उ, जइसन...तइसन, जेतना...ओतना.",
"एतना...कि (so...that); चाहे...चाहे (whether...or); ना...ना (neither...nor).",
"कि for reported thought and result clauses.",
"Build long sentences by joining known short ones with one pair.",
"Parse each: find the pair, split the clauses, translate each half.",
],
"requirements": [
"Parse all fifteen: name the connector pair in each.",
"Join ten pairs of short sentences with connectors.",
"Write five original complex sentences, each with a different pair.",
],
"standards": [
"Complex syntax per Shukla 1968.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968 (complex sentences).",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
],
"sig_lens": (
"His Signature reading: the complex sentence is the signature with riders - "
"जब...त the conditions, कि the fine print. The Signature Language Method "
"joins clauses like clauses in a contract: each pair witnessed, each half "
"translatable alone."),
},
# ------------------------------------------------------- 31 dialogue market
{
"key": "dialogue_market",
"name": "Bhojpuri Conversation: At the Market",
"group": "dialogue",
"ladder_rank": 31,
"ladder_tier": "advanced",
"description": (
"A twenty-line bilingual Bhojpuri-English dialogue at the market, annotated. "
"Customer (C), Shopkeeper (S). 1. C: राम राम, भाई! - Hello, brother! [राम राम "
"opens everything.] 2. S: राम राम! आईं, का चाहीं? - Hello! Come, what do you "
"want? [आईं is respectful.] 3. C: आलू केतना के बा? - How much are the "
"potatoes? 4. S: चालीस रुपया किलो, एकदम ताजा बा। - Forty rupees a kilo, "
"perfectly fresh. 5. C: बहुत महँग बा! तीस में दीं ना। - Too expensive! Give for "
"thirty. [ना softens the demand.] 6. S: तीस में ना होई, पैंतीस आखिरी बा। - "
"Not for thirty; thirty-five is final. 7. C: ठीक बा, एक किलो तौल दीं। - Fine, "
"weigh one kilo. 8. S: ई लेईं, तराजू "
"देख लेईं। - Take this; check the scale yourself. [लेईं is polite.] 9. C: प्याज "
"भी आधा किलो दे दीं। - Give half a kilo of onions too. 10. S: प्याज बीस के "
"आधा किलो। - Onions, twenty for half a kilo. 11. C: कुल केतना भइल? - What is "
"the total? 12. S: पचपन रुपया। - Fifty-five rupees. 13. C: सौ के नोट बा, "
"खुच्चा कर दीं। - I have a hundred note; make change. 14. S: पैंतालीस वापस, "
"गिन लेईं। - Forty-five back; count it. 15. C: ठीक बा। थैली में डाल दीं। - "
"Good. Put it in the bag. 16. S: ई लेईं थैली। धन्यवाद! - Here is the bag. "
"Thank you! 17. C: तरकारी ताजा रखिहऽ, फिर अइब। - Keep the vegetables fresh; I "
"will come again. 18. S: जरूर अइहऽ! ग्राहक भगवान हऽ। - Do come! The customer "
"is god. 19. C: राम राम! - Goodbye! 20. S: राम राम! शुभ दिन! - Goodbye! Have a "
"good day! Annotations: राम राम frames the whole exchange (lines 1, 19, 20); "
"bargaining runs lines 3-7; the polite -ीं forms (आईं, दीं, लेईं, कर दीं) keep "
"it friendly throughout; the shopkeeper's creed closes it (line 18)."),
"how_it_works": (
"A market dialogue has four acts: greeting (राम राम), price discovery (केतना "
"के बा?), the bargain (महँग बा / आखिरी बा), and the closing (धन्यवाद / फिर "
"अइहऽ). Notice the customer never stops being polite - दीं ना, ठीक बा - and "
"the shopkeeper answers respect with respect. तराजू देख लेईं (check the scale) "
"is the trust ritual. The numbers fly fast: चालीस, तीस, पैंतीस, पचपन, "
"पैंतालीस - this dialogue doubles as number drill. Role-play it with a "
"partner, swapping roles, until the bargain arc runs without notes."),
"key_points": [
"20-line bilingual market dialogue, annotated.",
"Four acts: greeting, price discovery, bargain, closing.",
"राम राम opens and closes the exchange.",
"Bargain arc: केतना के बा? -> महँग बा -> आखिरी बा -> ठीक बा.",
"Polite -ीं throughout: आईं, दीं, लेईं, कर दीं.",
"तराजू देख लेईं is the trust ritual.",
"Number drill inside: चालीस, तीस, पैंतीस, पचपन, पैंतालीस.",
"Role-play swapping customer/shopkeeper until fluent.",
],
"requirements": [
"Role-play the dialogue twice, swapping roles.",
"Run the bargain arc without looking at notes.",
"Add two of your own lines (a new item, a new price).",
],
"standards": [
"Dialogue per living Bhojpuri bazaar usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
],
"sig_lens": (
"His Signature reading: the market dialogue is commerce's signature - "
"केतना the offer, आखिरी the seal, ग्राहक भगवान हऽ the witness line. The "
"Signature Language Method bargains every line politely, because the "
"ledger remembers the manner, not just the price."),
},
# ------------------------------------------------------- 32 dialogue friend
{
"key": "dialogue_friend",
"name": "Bhojpuri Conversation: Meeting a Friend",
"group": "dialogue",
"ladder_rank": 32,
"ladder_tier": "advanced",
"description": (
"A twenty-line bilingual Bhojpuri-English dialogue between two friends, "
"annotated. Mohan (M), Sita (S). 1. M: राम राम, सीता! बहुत दिन बाद! - Hello, "
"Sita! Long time no see! 2. S: राम राम, मोहन! तू कहाँ रहलऽ? - Hello, Mohan! "
"Where have you been? [तू between friends.] 3. M: शहर गइल "
"रहल बानी, काम से। - I had gone to the city, for work. 4. S: काम बनल? - Did "
"the work get done? 5. M: हँ, बन गइल। तू सुना, का हाल बा? - Yes, done. Tell "
"me, how are you? 6. S: सब बढ़िया बा। काल्ह हमरा घर आ ना। - All great. Come to "
"my house tomorrow. 7. M: काहे, कवनो खास बात? - Why, something special? "
"8. S: माई के जन्मदिन बा, छोट-मोट पार्टी बा। - It is mother's birthday, a "
"small party. 9. M: अरे वाह! जरूर अइब। केतना बजे? - Wonderful! I will surely "
"come. At what time? 10. S: साँझ सात बजे। तोहरा दोस्तों के भी ले अइहऽ। - Seven "
"in the evening. Bring your friends too. 11. M: ठीक बा। उपहार का लेईं? - Fine. "
"What gift should I bring? 12. S: कुछ ना, तू आ जाऽ बस। - Nothing; just come. "
"13. M: ना ना, खाली हाथ ना अइब। - No no, I will not come empty-handed. "
"14. S: त माई खातिर फूल ले अइहऽ। - Then bring flowers for mother. 15. M: ठीक "
"बा। और सुना, पढ़ाई कइसन चलत बिया? - Fine. Tell me more, how are studies "
"going? 16. S: ठीक चलत बिया। परीक्षा नजदीक बा। - Going fine. Exams are near. "
"17. M: मेहनत करऽ, पास हो जइबऽ। - Work hard; you will pass. 18. S: तोहार "
"आशीर्वाद चाहीं। - I need your blessings. [Playful between friends.] 19. M: "
"चल, काल्ह मिलब। राम राम! - Well, see you tomorrow. Bye! 20. S: राम राम! समय "
"पर अइहऽ! - Bye! Come on time! Annotations: तू-forms throughout mark the "
"friendship (lines 2, 6, 13); the invitation arc runs lines 6-14; आशीर्वाद "
"is playful irony between equals (line 18); समय पर अइहऽ is the loving "
"command friends give (line 20)."),
"how_it_works": (
"Friends drop all -ीं forms: तू कहाँ रहलऽ?, आ ना, करऽ - the bare stems are "
"warmth, not rudeness, between equals. The conversation has three beats: "
"reunion (lines 1-5: कहाँ रहलऽ? का हाल बा?), invitation (lines 6-14: घर आ "
"ना, केतना बजे?), and farewell with a plan (lines 15-20: काल्ह मिलब). "
"छोट-मोट (small-ish) softens the party's scale; खाली हाथ ना अइब states the "
"guest's honor code. Notice line 3's pluperfect गइल रहल बानी (had gone) - "
"the -ल + रहल layering. Practice with a real friend: meet, invite, and "
"farewell entirely in Bhojpuri."),
"key_points": [
"20-line bilingual friends dialogue, annotated.",
"तू-forms throughout mark equality: warmth, not rudeness.",
"Three beats: reunion, invitation, farewell-with-plan.",
"छोट-मोट softens scale; खाली हाथ ना अइब states guest honor.",
"गइल रहल बानी = pluperfect (had gone).",
"आशीर्वाद between friends is playful irony.",
"समय पर अइहऽ - the loving command friends give.",
"Meet, invite, and farewell a real friend in Bhojpuri.",
],
"requirements": [
"Role-play the dialogue with a partner.",
"Identify the three beats in any real conversation.",
"Use गइल रहल बानी in one sentence about your past.",
],
"standards": [
"Dialogue per living Bhojpuri usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
],
"sig_lens": (
"His Signature reading: friends co-sign informally - तू the quick initial "
"between equals, खाली हाथ ना अइब the honor clause. The Signature Language "
"Method keeps friendship's register warm and exact, because the closest "
"signatures need the least ink."),
},
# ------------------------------------------------------- 33 dialogue problem
{
"key": "dialogue_problem",
"name": "Bhojpuri Conversation: Solving a Problem",
"group": "dialogue",
"ladder_rank": 33,
"ladder_tier": "advanced",
"description": (
"A twenty-line bilingual Bhojpuri-English dialogue solving a problem, "
"annotated. Farmer (F), Neighbor (N). 1. F: राम राम, भाई। बड़ परेशानी बा। - "
"Hello, brother. There is big trouble. 2. N: का भइल? बइठ के बतावऽ। - What "
"happened? Sit and tell me. 3. F: नहर के पानी बंद हो गइल, खेत सूखत बा। - The "
"canal water stopped; the field is drying. 4. N: कब से? - Since when? 5. F: "
"तीन दिन से। धान के फसल मर जाई। - For three days. The paddy crop will die. "
"6. N: घबराव मत। मुखिया से बात करब? - Do not panic. Shall we talk to the "
"headman? 7. F: बात कइल, सुनलस ना। - I talked; he did not listen. "
"8. N: त सब किसान मिल के जाईं। - Then all farmers should go together. 9. F: "
"ई नीक सलाह बा। कब चलब? - This is good advice. When shall we go? 10. N: काल्ह "
"बिहान। सबके खबर कर दऽ। - Tomorrow morning. Inform everyone. 11. F: ठीक बा। "
"बाकिर पानी आज चाहीं। - Fine. But water is needed today. 12. N: तब तक मोर "
"ट्यूबवेल से ले लऽ। - Until then, take from my tubewell. 13. F: बहुत-बहुत "
"धन्यवाद, भाई! - Thank you very much, brother! 14. N: अरे, ई त हमार फर्ज बा। "
"- Oh, this is my duty. 15. F: पइसा केतना देईं? - How much money should I "
"give? 16. N: पइसा के बात ना करऽ। फसल बचे, बस। - Do not talk money. Just save "
"the crop. 17. F: तोहार एहसान ना भुलब। - I will not forget your favor. "
"18. N: चलऽ, अभी ट्यूबवेल चालू करवावत बानी। - Come, I am getting the tubewell "
"started right now. 19. F: भगवान तोहरा के खुश रखे। - May God keep you happy. "
"20. N: आमीन। चलऽ, देर मत करऽ। - Amen. Come, do not delay. Annotations: the "
"problem is stated in two lines (3, 5); घबराव मत steadies (6); the solution "
"builds in steps (8, 10, 12); पइसा के बात ना करऽ refuses payment nobly (16); "
"the blessing seals it (19-20)."),
"how_it_works": (
"Problem dialogues move in five steps: state it (परेशानी बा, का भइल?), size "
"it (तीन दिन से, मर जाई), steady it (घबराव मत), solve it step by step (मिल के "
"जाईं, खबर कर दऽ, ट्यूबवेल से ले लऽ), and seal it (धन्यवाद, भगवान...खुश रखे). "
"Notice the neighbor never asks 'why me' - फर्ज बा (it is my duty) - and "
"refuses payment: पइसा के बात ना करऽ. एहसान ना भुलब (will not forget the "
"favor) is the debt that replaces money. Commands stay familiar (बतावऽ, कर "
"दऽ, चलऽ) because neighbors are family. Practice by stating a real problem "
"of yours in five Bhojpuri lines following the five steps."),
"key_points": [
"20-line bilingual problem-solving dialogue, annotated.",
"Five steps: state, size, steady, solve, seal.",
"घबराव मत steadies; फर्ज बा obligates; पइसा के बात ना करऽ ennobles.",
"एहसान ना भुलब - the debt that replaces money.",
"Solution builds stepwise: मिल के जाईं, खबर कर दऽ, ट्यूबवेल से ले लऽ.",
"Blessing seals it: भगवान तोहरा के खुश रखे.",
"State a real problem of yours in five Bhojpuri lines.",
],
"requirements": [
"Map the five steps onto the dialogue's line numbers.",
"State a real problem in five Bhojpuri lines.",
"Refuse payment nobly once: पइसा के बात ना करऽ.",
],
"standards": [
"Dialogue per Bhojpuri rural usage.",
"Transliteration follows the practical scheme used across this database.",
],
"citations": [
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
],
"sig_lens": (
"His Signature reading: a solved problem is a signature under pressure - "
"परेशानी the blot, घबराव मत the steadying hand, एहसान ना भुलब the "
"countersignature. The Signature Language Method solves stepwise and seals "
"with a blessing, because every contract ends with a witness."),
},
# ------------------------------------------------------- 34 mastery
{
"key": "mastery",
"name": "Bhojpuri Mastery Review and Full Reference",
"group": "reference",
"ladder_rank": 34,
"ladder_tier": "advanced",
"description": (
"The whole Bhojpuri database in one teaching summary. ALPHABET: 13 vowels "
"अ आ इ ई उ ऊ ऋ ए ऐ ओ औ अं अः; 33 consonants क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त "
"थ द ध न प फ ब भ म य र ल व श ष स ह + क्ष त्र ज्ञ श्र; numerals ०-९; historic "
"Kaithi script (U+11080-U+1114F). SOUNDS: five stop rows x four manners; "
"retroflex vs dental; flap ड़; nasalization ँ/ं; minimal pairs ताल/थाल, "
"दाम/धाम, बात/भात, कान/खान. 200 CORE WORDS (Bhojpuri - English): माई-mother, "
"बाबूजी-father, भाई-brother, बहिन-sister, बेटा-son, बेटी-daughter, दादा-"
"grandfather, दादी-grandmother, आदमी-man, औरत-woman, लइका-boy, लइकी-girl, "
"दोस्त-friend, घर-house, गाँव-village, शहर-city, दुआर-door, "
"खिड़की-window, कोठरी-room, रसोई-kitchen, आँगन-courtyard, छत-roof, खटिया-cot, "
"मेज-table, कुर्सी-chair, पानी-water, खाना-food, रोटी-bread, भात-rice, दाल-"
"lentils, सब्जी-vegetables, दूध-milk, चाय-tea, लिट्टी-litti, सत्तू-sattu, "
"खिचड़ी-khichdi, नमक-salt, चीनी-sugar, तेल-oil, घी-ghee, मिरचा-chili, प्याज-"
"onion, आलू-potato, गाय-cow, भैंस-buffalo, बकरी-goat, कुत्ता-dog, बिल्ली-cat, "
"घोड़ा-horse, चिरई-bird, मछरी-fish, साँप-snake, बानर-monkey, पेड़-tree, फूल-"
"flower, नदी-river, गंगा-Ganges, तालाब-pond, सूरज-sun, चाँद-moon, तारा-star, "
"बादल-cloud, बरसात-rain, घाम-sunshine, हवा-wind, बिजली-lightning, जाड़ा-winter, "
"गर्मी-summer, बसंत-spring, खेत-field, धान-paddy, बगीचा-orchard, किताब-book, "
"कलम-pen, कॉपी-notebook, स्कूल-school, मास्टर-teacher, काम-work, नौकरी-job, "
"दफ्तर-office, पइसा-money, बाजार-market, हाट-weekly market, दाम-price, टिकट-"
"ticket, गाड़ी-vehicle, रेलगाड़ी-train, स्टेशन-station, सड़क-road, मोबाइल-mobile, "
"फोन-phone, कंप्यूटर-computer, इंटरनेट-internet, टीवी-TV, बिजली-electricity, "
"डॉक्टर-doctor, अस्पताल-hospital, दवाई-medicine, बुखार-fever, दर्द-pain, देह-"
"body, माथा-head, आँख-eye, कान-ear, नाक-nose, मुँह-mouth, हाथ-hand, गोड़-leg, "
"पेट-stomach, खुशी-happiness, दुख-sorrow, गुस्सा-anger, डर-fear, प्यार-love, "
"दिन-day, रात-night, बिहान-morning, साँझ-evening, आज-today, काल्ह-tomorrow/"
"yesterday. KEY GRAMMAR: SOV order; two genders, two numbers; postpositions "
"में पर से के खातिर लगे; no articles; negation ना/नइखे/मत; questions front "
"के का कहाँ कब काहे कइसे केतना; no 'ne' ergative; 'be' = बानी/बाड़ऽ/बा; "
"present = stem+त+be; perfect = -ल+be; past = bare -ल; future = stem+ब; "
"commands = stem (informal) / -ीं (polite); respect = तू vs रउआ. PHRASE "
"TABLES: greetings (राम राम, प्रणाम, का हाल बा?), numerals (एक..सव), days "
"(सोमवार..एतवार), months (चैत..फागुन), proverbs (जेकर लाठी ओकर भैंस, नाच न "
"जाने आँगन टेढ़, मेहनत के फल मीठ होला). THE LADDER: records 1-9 foundations "
"(overview, script, sounds, words, phrases), 10-20 compounded (grammar, "
"eleven themed sentence sets), 21-34 advanced (tenses, Q/A, commands, "
"descriptions, three stories, idioms, registers, complex sentences, three "
"dialogues, this review). Final charge: speak daily, read the stories "
"weekly, use one proverb a day - भोज्पुरी माटी के भाषा हऽ."),
"how_it_works": (
"This record is the database compressed: everything above in one page for "
"revision and lookup. Use it three ways: as a checklist (can you produce "
"every core word from English alone?), as a drill sheet (cover the Bhojpuri "
"column and recall), and as a map (lost on tenses? jump to record 21; blank "
"on shopping? record 18). The 200 words are the survival core - with them "
"plus the grammar line you can say anything slowly. The phrase tables are "
"the social keys. Work through the ladder one record a day for 34 days; on "
"day 35, retake this review cold. What you cannot produce, relearn from its "
"record."),
"key_points": [
"Full alphabet, sounds, 200 core words, key grammar, phrase tables in one record.",
"200 survival words: say each from English alone.",
"SOV + postpositions + no-'ne' + तू/रउआ = the whole grammar line.",
"Phrase tables: greetings, numerals, days, months, proverbs.",
"Ladder map: 1-9 foundations, 10-20 compounded, 21-34 advanced.",
"34-day plan: one record a day; day 35 retake this review cold.",
"Final charge: speak daily, read stories weekly, one proverb a day.",
"भोज्पुरी माटी के भाषा हऽ.",
],
"requirements": [
"Produce all 200 core words from English prompts.",
"Recite the grammar line from memory.",
"Complete the 34-day ladder and retake this review.",
],
"standards": [
"Reference per Shukla 1968, Grierson LSI Vol. V, Tiwari 1960.",
"Unicode Devanagari U+0900-U+097F; Kaithi U+11080-U+1114F; ISO 639-3 bho.",
],
"citations": [
"Shukla, Shaligram. Bhojpuri Grammar. 1968.",
"Grierson, George A. Linguistic Survey of India, Vol. V. 1903.",
"Tiwari, Udai Narain. The Origin and Development of Bhojpuri. 1960.",
"Ethnologue: Languages of the World - Bhojpuri (bho).",
"The Unicode Standard - Devanagari block U+0900-U+097F; Kaithi block U+11080-U+1114F.",
],
"sig_lens": (
"His Signature reading: the mastery review is the signature book closed and "
"tied - 200 words the pages, the grammar line the ribbon, the proverb the "
"wax seal. The Signature Language Method ends where it began: भोज्पुरी माटी "
"के भाषा हऽ, and now the learner can sign it too."),
},
]
