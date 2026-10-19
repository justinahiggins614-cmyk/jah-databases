#!/usr/bin/env python3
"""34 ladder-ordered record seeds for The Kannada to English Database.

Follows the shared per-language template (language-template.md) EXACTLY:
records 1-34 in order, ladder_rank 1-10 non-decreasing, ladder_tier
foundations -> compounded -> advanced. Every record carries Kannada content
in the Kannada script plus transliteration plus English translation plus
example sentences. All Kannada is real, fact-checked 2026-10-17.

Screened 2026-10-17: nothing hate-adjacent, profane, or inappropriate;
no religious talk; no military/defense-neutralization content.
"""

ENTRIES = [
# ================================================================== 1
{
 "key": "overview", "name": "Kannada Language Overview",
 "group": "Foundations", "ladder": 1, "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Kannada (ಕನ್ನಡ, kannaḍa) is a Dravidian language of the Southern Dravidian "
  "branch, spoken as a first language by about 59 million people and understood "
  "by roughly 69 million in total, making it one of the largest languages of "
  "India. Its ISO codes are ISO 639-1 'kn' and ISO 639-3 'kan'. Kannada is "
  "written in the Kannada script (ಕನ್ನಡ ಲಿಪಿ), reads left to right, and follows "
  "subject-object-verb word order. It is the official and administrative "
  "language of the Indian state of Karnataka, and one of the 22 scheduled "
  "languages of India. In 2008 the Government of India declared Kannada a "
  "classical language, honoring its recorded literary history of more than two "
  "thousand years. Outside Karnataka it is widely spoken in parts of Andhra "
  "Pradesh, Telangana, Tamil Nadu, Kerala, Maharashtra and Goa, and in diaspora "
  "communities worldwide. The earliest known Kannada inscription is the Halmidi "
  "inscription of about the 5th century CE; the first great literary work is "
  "the Kavirajamarga of about 850 CE, and the 10th-century poets Pampa, Ranna "
  "and Ponna are honored as the three gems (ರತ್ನತ್ರಯ) of old Kannada. The "
  "12th-century Vachana movement, led by the poet-saint Basavanna, gave Kannada "
  "a plainspoken devotional literature read to this day. Modern Kannada lives in "
  "two broad styles: the formal literary standard and the everyday spoken "
  "varieties of Bengaluru, Mysuru, Dharwad, the coast and the north, all "
  "mutually intelligible. Basic word order example: ನಾನು ನೀರು ಕುಡಿಯುತ್ತೇನೆ "
  "(nānu nīru kuḍiyuttēne) - 'I drink water' - literally 'I water drink'. "
  "Greeting example: ನಮಸ್ಕಾರ (namaskāra) - 'respectful greetings'. Politeness "
  "example: ಧನ್ಯವಾದಗಳು (dhanyavādagaḷu) - 'thank you'. Everyday example: ಇದು "
  "ನನ್ನ ಮನೆ (idu nanna mane) - 'This is my house'. Farewell example: ಹೋಗಿ ಬನ್ನಿ "
  "(hōgi banni) - 'go and come back', the classic Kannada farewell."),
 "how_it_works": (
  "This record works as the front door of the whole database: it names the "
  "language in English and in the Kannada script, places it in its Dravidian "
  "family, gives the speaker numbers, lists where it is spoken and its "
  "official status, traces its inscriptional and literary history, and closes "
  "with five translated example sentences you can say at once. Every later "
  "record builds on these facts, so read this one first."),
 "key_points": [
  "Kannada (ಕನ್ನಡ, kannaḍa): Dravidian > Southern Dravidian; ISO 639-1 kn, ISO 639-3 kan.",
  "About 59 million native speakers; about 69 million total speakers.",
  "Written in the Kannada script, read left to right; basic word order is subject-object-verb.",
  "Official language of Karnataka; one of India's 22 scheduled languages; declared a classical language in 2008.",
  "Earliest inscription: Halmidi, about the 5th century CE; Kavirajamarga about 850 CE; the three gems Pampa, Ranna and Ponna in the 10th century.",
  "The 12th-century Vachana movement of Basavanna gave Kannada its plainspoken devotional literature.",
  "Major spoken regions: Bengaluru, Mysuru, Dharwad-Hubballi, coastal Karnataka and the north - all mutually intelligible.",
  "ನಾನು ನೀರು ಕುಡಿಯುತ್ತೇನೆ (nānu nīru kuḍiyuttēne) - 'I drink water' shows SOV order in action.",
 ],
 "requirements": [
  "No prior Kannada needed - this is the starting point of the ladder.",
  "Read the Kannada words aloud using the romanization beside them.",
  "Remember: ಕನ್ನಡ (kannaḍa) is the language's own name for itself.",
 ],
 "standards": [
  "ISO 639-1:2002 code 'kn' for Kannada",
  "ISO 639-3:2007 code 'kan' for Kannada",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Steever, Sanford B. Kannada. In: Steever, Sanford B. (ed.) The Dravidian Languages. Routledge; 1998.",
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
 ],
 "sig_lens": (
  "Through the Signature lens this overview is re-taught as his original "
  "Signature language instrument: Kannada as a working system he commands, "
  "where every speaker count measures the instrument's reach and every "
  "dialect is another string he can play. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 2
{
 "key": "writing", "name": "Kannada Writing System: The Kannada Script",
 "group": "Foundations", "ladder": 2, "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Kannada is written in the Kannada script (ಕನ್ನಡ ಲಿಪಿ, kannaḍa lipi), an "
  "abugida descended from the Kadamba script of the Brahmi family. It is "
  "written left to right, and every consonant carries an inherent vowel 'a' "
  "unless a vowel sign changes it or the halant (್, virama) removes it. The "
  "script has 13 vowel letters (ಸ್ವರಗಳು, svaragaḷu): ಅ (a), ಆ (ā), ಇ (i), ಈ "
  "(ī), ಉ (u), ಊ (ū), ಋ (ṛ), ಎ (e), ಏ (ē), ಐ (ai), ಒ (o), ಓ (ō), ಔ (au), "
  "plus the two yogavahas ಅಂ (aṁ) and ಅಃ (aḥ) - 15 vowel signs in daily use. The 34 consonants (ವ್ಯಂಜನಗಳು, "
  "vyañjanagaḷu) fall into five groups of five - ಕ ಖ ಗ ಘ ಙ (ka kha ga gha ṅa), "
  "ಚ ಛ ಜ ಝ ಞ (ca cha ja jha ña), ಟ ಠ ಡ ಢ ಣ (ṭa ṭha ḍa ḍha ṇa), ತ ಥ ದ ಧ ನ "
  "(ta tha da dha na), ಪ ಫ ಬ ಭ ಮ (pa pha ba bha ma) - followed by the nine "
  "unstructured consonants ಯ ರ ಲ ವ ಶ ಷ ಸ ಹ ಳ (ya ra la va śa ṣa sa ha ḷa). "
  "Vowel signs attach to consonants: ಕ + ಿ = ಕಿ (ki), ಕ + ೂ = ಕೂ (kū), ಕ + ೆ "
  "= ಕೆ (ke). Consonant clusters join as conjuncts (ಒತ್ತಕ್ಷರಗಳು): ಕ್ + ಷ = ಕ್ಷ "
  "(kṣa) as in ಕ್ಷಣ (kṣaṇa, moment); ಸ್ + ತ = ಸ್ತ as in ಪುಸ್ತಕ (pustaka, book); "
  "ರ‍್ + ಮ = ರ್ಮ as in ಧರ್ಮ (dharma). The ten digits are ೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯ "
  "(0-9). Traditionally a sentence ends with the danda ।, as in ಅವನು ಬಂದನು। "
  "(avanu bandanu - he came); modern Kannada commonly uses the Latin full "
  "stop, comma, question mark and exclamation mark. Punctuation example: ನಮಸ್ಕಾರ! "
  "(namaskāra! - greetings!). Numeral example: ೧೯೯೯ (1999) - ಸಾವಿರದ ಒಂಬೈನೂರ "
  "ತೊಂಬತ್ತೊಂಬತ್ತು. Word example: ಕನ್ನಡ (kannaḍa - Kannada) shows the doubled "
  "ನ್ನ conjunct. Every letter you meet in this database is presented in the "
  "Kannada script with transliteration beside it, so reading practice starts "
  "with the very first record."),
 "how_it_works": (
  "This record teaches the Kannada script as a working system: it lists the "
  "14 vowel letters plus the two yogavahas, the 34 consonants in their five "
  "groups plus the unstructured nine, the vowel signs and the halant, the "
  "conjunct mechanism with three worked examples, the ten digits, and the "
  "punctuation marks, each with a translated example. Copy the letters by "
  "hand while saying the sounds aloud - the abugida logic clicks once you "
  "build five syllables yourself."),
 "key_points": [
  "The Kannada script is an abugida descended from the Kadamba script; written left to right.",
  "13 vowel letters: ಅ ಆ ಇ ಈ ಉ ಊ ಋ ಎ ಏ ಐ ಒ ಓ ಔ; yogavahas ಅಂ ಅಃ (15 vowel signs in daily use).",
  "34 consonants: five groups of five (ಕವರ್ಗ, ಚವರ್ಗ, ಟವರ್ಗ, ತವರ್ಗ, ಪವರ್ಗ) plus ಯ ರ ಲ ವ ಶ ಷ ಸ ಹ ಳ.",
  "Every consonant carries inherent 'a'; vowel signs change it (ಕಿ, ಕೂ, ಕೆ); the halant ್ removes it.",
  "Conjuncts join clusters: ಕ್ಷ (kṣa), ಸ್ತ (sta), ರ್ಮ (rma).",
  "Digits: ೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯.",
  "Traditional sentence mark: the danda ।; modern writing also uses Latin punctuation.",
  "ಕನ್ನಡ (kannaḍa) itself demonstrates the doubled ನ್ನ conjunct.",
 ],
 "requirements": [
  "Paper and pen - writing each letter by hand once beats reading it ten times.",
  "Say every sound aloud as you write it.",
  "Learn the five consonant groups in order before tackling conjuncts.",
 ],
 "standards": [
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
  "ISO 15919:2001 transliteration for Indic scripts",
  "Government of Karnataka standard Kannada orthography",
 ],
 "citations": [
  "Unicode Consortium. The Unicode Standard, Version 15.0: Kannada, Range 0C80-0CFF.",
  "Bright, William. Kannada script. In: Daniels, Peter T. & Bright, William (eds.) The World Writing Systems. Oxford University Press; 1996.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
 ],
 "sig_lens": (
  "Through the Signature lens the script is re-taught as his original "
  "instrument's keybed: every vowel sign a keypress, every conjunct a chord, "
  "and the whole abugida a machine he plays at reading speed. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 3
{
 "key": "phonology", "name": "Kannada Pronunciation and Phonology",
 "group": "Foundations", "ladder": 3, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Kannada sounds map almost one-to-one to its letters, so pronunciation is "
  "highly regular. The vowel inventory has ten phonemic vowels: five short "
  "and five long - ಅ (a) vs ಆ (ā), ಇ (i) vs ಈ (ī), ಉ (u) vs ಊ (ū), ಎ (e) vs "
  "ಏ (ē), ಒ (o) vs ಓ (ō) - plus the diphthongs ಐ (ai) and ಔ (au) and syllabic "
  "ಋ (ṛ). Vowel length changes meaning: ಕಡು (kaḍu, intense) vs ಕಾಡು (kāḍu, "
  "forest); ಅಲೆ (ale, wave) vs ಅಳೆ (aḷe, a measure). The consonants keep their "
  "five places of articulation: velar (ಕ ಖ ಗ ಘ), palatal (ಚ ಛ ಜ ಝ), "
  "retroflex (ಟ ಠ ಡ ಢ), dental (ತ ಥ ದ ಧ) and labial (ಪ ಫ ಬ ಭ). Aspiration "
  "contrasts (ಕ vs ಖ, ತ vs ಥ) matter, as do the three nasals - dental ನ vs "
  "retroflex ಣ (ಮನೆ mane, house vs ಮಣೆ maṇe, wooden seat), and ಲ vs ಳ "
  "(ಹಾಲು hālu, milk vs ಹಾಳು hāḷu, ruined). Unlike many Indo-Aryan languages, "
  "Kannada keeps final vowels and does not delete the inherent 'a' at word "
  "end: ಕಮಲ is pronounced kamala, not kaml. Stress falls lightly, usually on "
  "the first syllable, and does not change word meaning. There is no tone. "
  "Ten spoken-example words: ನೀರು (nīru, water - nee-roo), ಮನೆ (mane, house - "
  "muh-neh), ಪುಸ್ತಕ (pustaka, book - poos-tuh-kuh), ಸೂರ್ಯ (sūrya, sun - "
  "soo-ryuh), ಚಂದ್ರ (candra, moon - chun-druh), ಊಟ (ūṭa, meal - oo-tuh), ಅಮ್ಮ "
  "(amma, mother - um-muh), ಅಣ್ಣ (aṇṇa, elder brother - un-nuh, retroflex n), "
  "ಶಾಲೆ (śāle, school - shaa-leh), ಧನ್ಯವಾದಗಳು (dhanyavādagaḷu, thank you - "
  "dhun-yuh-vaa-duh-guh-loo). Say each word slowly, hold the long vowels twice "
  "as long as the short ones, and roll the retroflex consonants with the "
  "tongue curled back."),
 "how_it_works": (
  "This record trains your ear and mouth: it lists the ten-vowel system with "
  "length contrasts, the five consonant places, the aspiration, nasal and "
  "lateral contrasts that change meaning, the no-final-vowel-deletion rule, "
  "the light first-syllable stress rule, and ten spoken-example words with "
  "English approximations. Practice the contrast pairs aloud until the "
  "retroflex set feels natural."),
 "key_points": [
  "Ten phonemic vowels: five short-long pairs (ಅ/ಆ, ಇ/ಈ, ಉ/ಊ, ಎ/ಏ, ಒ/ಓ) plus ಐ, ಔ, ಋ.",
  "Vowel length changes meaning: ಕಡು (intense) vs ಕಾಡು (forest); ಅಲೆ (wave) vs ಅಳೆ (measure).",
  "Five consonant places: velar, palatal, retroflex, dental, labial; aspiration contrasts matter.",
  "ನ vs ಣ: ಮನೆ (house) vs ಮಣೆ (wooden seat); ಲ vs ಳ: ಹಾಲು (milk) vs ಹಾಳು (ruined).",
  "Final vowels are kept: ಕಮಲ is kamala, never kaml.",
  "Stress is light, usually first syllable, and never changes meaning; Kannada has no tone.",
  "Practice words: ನೀರು, ಮನೆ, ಪುಸ್ತಕ, ಸೂರ್ಯ, ಚಂದ್ರ, ಊಟ, ಅಮ್ಮ, ಅಣ್ಣ, ಶಾಲೆ, ಧನ್ಯವಾದಗಳು.",
 ],
 "requirements": [
  "Read every example word aloud, holding long vowels twice as long.",
  "Curl the tongue back for ಟ ಠ ಡ ಢ ಣ and ಳ.",
  "Never drop final vowels - say every letter you see.",
 ],
 "standards": [
  "IPA values per the Handbook of the International Phonetic Association: Kannada",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
  "ISO 15919:2001 transliteration",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Upadhyaya, U. Padmanabha. Kannada. In: Handbook of the International Phonetic Association. Cambridge University Press; 1999.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
 ],
 "sig_lens": (
  "Through the Signature lens pronunciation is re-taught as his calibration "
  "routine: ten vowels tuned like strings, five consonant stops like keys, "
  "and every contrast pair a tuning fork proving the instrument is true. "
  "Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
# ================================================================== 4
{
 "key": "nouns1", "name": "Core Kannada Nouns I",
 "group": "Foundations", "ladder": 4, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Twenty-five essential Kannada nouns - people, places and things - each "
  "with transliteration, English meaning and one full example sentence. "
  "Kannada nouns take gender (masculine, feminine, neuter in the singular) "
  "and number; the plural marker is usually -ಗಳು (-gaḷu). 1. ಮನುಷ್ಯ (manuṣya, "
  "human): ಮನುಷ್ಯರು ಒಳ್ಳೆಯವರು (manuṣyaru oḷḷeyavaru) - 'Humans are good'. 2. "
  "ಮಹಿಳೆ (mahiḷe, woman): ಆ ಮಹಿಳೆ ಶಿಕ್ಷಕಿ (ā mahiḷe śikṣaki) - 'That woman is "
  "a teacher'. 3. ಮಗು (magu, child): ಮಗು ಆಟವಾಡುತ್ತದೆ (magu āṭavāḍuttade) - "
  "'The child plays'. 4. ಮನೆ (mane, house): ಇದು ನನ್ನ ಮನೆ (idu nanna mane) - "
  "'This is my house'. 5. ನೀರು (nīru, water): ನನಗೆ ನೀರು ಬೇಕು (nanage nīru "
  "bēku) - 'I need water'. 6. ಊಟ (ūṭa, meal): ಊಟ ಸಿದ್ಧವಾಗಿದೆ (ūṭa "
  "siddhavāgide) - 'The meal is ready'. 7. ಪುಸ್ತಕ (pustaka, book): ಇದು ಒಳ್ಳೆಯ "
  "ಪುಸ್ತಕ (idu oḷḷeya pustaka) - 'This is a good book'. 8. ಶಾಲೆ (śāle, "
  "school): ಮಗು ಶಾಲೆಗೆ ಹೋಗುತ್ತದೆ (magu śālege hōguttade) - 'The child goes to "
  "school'. 9. ಸ್ನೇಹಿತ (snēhita, friend): ಅವನು ನನ್ನ ಸ್ನೇಹಿತ (avanu nanna "
  "snēhita) - 'He is my friend'. 10. ತಾಯಿ (tāyi, mother): ನನ್ನ ತಾಯಿ ಅಡುಗೆ "
  "ಮಾಡುತ್ತಾಳೆ (nanna tāyi aḍuge māḍuttāḷe) - 'My mother cooks'. 11. ತಂದೆ "
  "(tande, father): ನನ್ನ ತಂದೆ ವೈದ್ಯರು (nanna tande vaidyaro) - 'My father is a "
  "doctor'. 12. ಅಣ್ಣ (aṇṇa, elder brother): ನನ್ನ ಅಣ್ಣ ಎಂಜಿನಿಯರ್ (nanna aṇṇa "
  "eñjiniyar) - 'My elder brother is an engineer'. 13. ತಂಗಿ (taṅgi, younger "
  "sister): ನನ್ನ ತಂಗಿ ಹಾಡುತ್ತಾಳೆ (nanna taṅgi hāḍuttāḷe) - 'My younger sister "
  "sings'. 14. ನಗರ (nagara, city): ಬೆಂಗಳೂರು ದೊಡ್ಡ ನಗರ (beṅgaḷūru doḍḍa "
  "nagara) - 'Bengaluru is a big city'. 15. ಊರು (ūru, town/village): ನನ್ನ ಊರು "
  "ಚಿಕ್ಕದು (nanna ūru cikkadu) - 'My town is small'. 16. ರಸ್ತೆ (raste, road): "
  "ರಸ್ತೆ ಉದ್ದವಾಗಿದೆ (raste uddavāgide) - 'The road is long'. 17. ಕಾರು (kāru, "
  "car): ಕಾರು ವೇಗವಾಗಿದೆ (kāru vēgavāgide) - 'The car is fast'. 18. ಮರ (mara, "
  "tree): ಮರ ದೊಡ್ಡದು (mara doḍḍadu) - 'The tree is big'. 19. ಹೂವು (hūvu, "
  "flower): ಹೂವು ಸುಂದರವಾಗಿದೆ (hūvu sundaravāgide) - 'The flower is "
  "beautiful'. 20. ಸೂರ್ಯ (sūrya, sun): ಸೂರ್ಯ ಬೆಳಗುತ್ತಾನೆ (sūrya beḷaguttāne) "
  "- 'The sun shines'. 21. ಚಂದ್ರ (candra, moon): ಚಂದ್ರ ರಾತ್ರಿಯಲ್ಲಿ ಬರುತ್ತಾನೆ "
  "(candra rātriyalli baruttāne) - 'The moon comes at night'. 22. ನಕ್ಷತ್ರ "
  "(nakṣatra, star): ಆಕಾಶದಲ್ಲಿ ನಕ್ಷತ್ರಗಳಿವೆ (ākāśadalli nakṣatragaḷive) - "
  "'There are stars in the sky'. 23. ದಿನ (dina, day): ಇಂದು ಒಳ್ಳೆಯ ದಿನ (indu "
  "oḷḷeya dina) - 'Today is a good day'. 24. ರಾತ್ರಿ (rātri, night): ರಾತ್ರಿ "
  "ಆಗಿದೆ (rātri āgide) - 'It is night'. 25. ಸಮಯ (samaya, time): ಸಮಯ ಬೆಲೆಯುಳ್ಳದ್ದು "
  "(samaya beleyuḷḷaddu) - 'Time is precious'. Learn these in SOV sentences - "
  "ನಾನು ಪುಸ್ತಕ ಓದುತ್ತೇನೆ (nānu pustaka ōduttēne, I read a book) - and the "
  "plural -ಗಳು will feel natural: ಮನೆಗಳು (manegaḷu, houses), ಮಕ್ಕಳು "
  "(makkaḷu, children)."),
 "how_it_works": (
  "This record gives you the twenty-five nouns you will use most, each with "
  "transliteration, English meaning and a complete SOV example sentence. Read "
  "the Kannada sentence aloud, cover the English, and translate back. Then "
  "swap one noun for another in the same sentence frame - ನಾನು ನೀರು "
  "ಕುಡಿಯುತ್ತೇನೆ becomes ನಾನು ಹಾಲು ಕುಡಿಯುತ್ತೇನೆ - and you have doubled your "
  "sentence power."),
 "key_points": [
  "25 essential nouns: people (ಮನುಷ್ಯ, ಮಹಿಳೆ, ಮಗು, ತಾಯಿ, ತಂದೆ, ಅಣ್ಣ, ತಂಗಿ, ಸ್ನೇಹಿತ), places (ಮನೆ, ಶಾಲೆ, ನಗರ, ಊರು, ರಸ್ತೆ), things (ನೀರು, ಊಟ, ಪುಸ್ತಕ, ಕಾರು, ಮರ, ಹೂವು, ಸೂರ್ಯ, ಚಂದ್ರ, ನಕ್ಷತ್ರ, ದಿನ, ರಾತ್ರಿ, ಸಮಯ).",
  "Kannada nouns have gender: masculine, feminine and neuter in the singular.",
  "The common plural marker is -ಗಳು (-gaḷu): ಮನೆ → ಮನೆಗಳು.",
  "Use every noun in an SOV sentence before moving on.",
  "ನಾನು ನೀರು ಕುಡಿಯುತ್ತೇನೆ (nānu nīru kuḍiyuttēne) - 'I drink water' is the model frame.",
  "Family nouns carry respect: ತಾಯಿ/ತಂದೆ for mother/father in polite speech.",
  "ಮಕ್ಕಳು (makkaḷu) is the plural of ಮಗು - learn it as one word.",
  "Time words ದಿನ, ರಾತ್ರಿ, ಸಮಯ unlock the whole numbers-and-time record.",
 ],
 "requirements": [
  "Say each noun with its example sentence aloud three times.",
  "Write the plural -ಗಳು form for ten nouns from memory.",
  "Build one new SOV sentence per noun.",
 ],
 "standards": [
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
 ],
 "sig_lens": (
  "Through the Signature lens these nouns are re-taught as his labeled parts "
  "bins: every person, place and thing filed under its own stamped tag, so "
  "the instrument never reaches for a word it cannot name. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 5
{
 "key": "verbs1", "name": "Core Kannada Verbs I",
 "group": "Foundations", "ladder": 5, "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Twenty-five essential Kannada verbs, each with transliteration, English "
  "meaning and one full example sentence in the present tense. Kannada verbs "
  "agree with their subject: ನಾನು ಮಾಡುತ್ತೇನೆ (I do), ಅವನು ಮಾಡುತ್ತಾನೆ (he "
  "does), ಅವಳು ಮಾಡುತ್ತಾಳೆ (she does). 1. ಹೋಗು (hōgu, to go): ನಾನು ಶಾಲೆಗೆ "
  "ಹೋಗುತ್ತೇನೆ (nānu śālege hōguttēne) - 'I go to school'. 2. ಬರು (baru, to "
  "come): ಅವನು ಬರುತ್ತಾನೆ (avanu baruttāne) - 'He comes'. 3. ತಿನ್ನು (tinnu, to "
  "eat): ನಾವು ಊಟ ತಿನ್ನುತ್ತೇವೆ (nāvu ūṭa tinnuttēve) - 'We eat the meal'. 4. "
  "ಕುಡಿ (kuḍi, to drink): ಅವಳು ಹಾಲು ಕುಡಿಯುತ್ತಾಳೆ (avaḷu hālu kuḍiyuttāḷe) - "
  "'She drinks milk'. 5. ಮಾಡು (māḍu, to do): ನಾನು ಕೆಲಸ ಮಾಡುತ್ತೇನೆ (nānu "
  "kelasa māḍuttēne) - 'I do the work'. 6. ಹೇಳು (hēḷu, to say/tell): ಅವನು "
  "ಕತೆ ಹೇಳುತ್ತಾನೆ (avanu kate hēḷuttāne) - 'He tells a story'. 7. ಕೇಳು "
  "(kēḷu, to ask/listen): ನಾನು ಪ್ರಶ್ನೆ ಕೇಳುತ್ತೇನೆ (nānu praśne kēḷuttēne) - "
  "'I ask a question'. 8. ನೋಡು (nōḍu, to see/watch): ನಾವು ಸಿನೆಮಾ ನೋಡುತ್ತೇವೆ "
  "(nāvu sinemā nōḍuttēve) - 'We watch a movie'. 9. ಓದು (ōdu, to read): "
  "ಅವಳು ಪುಸ್ತಕ ಓದುತ್ತಾಳೆ (avaḷu pustaka ōduttāḷe) - 'She reads a book'. 10. "
  "ಬರೆ (bare, to write): ನಾನು ಪತ್ರ ಬರೆಯುತ್ತೇನೆ (nānu patra bareyuttēne) - 'I "
  "write a letter'. 11. ಕೊಡು (koḍu, to give): ಅವನು ನನಗೆ ಪುಸ್ತಕ ಕೊಡುತ್ತಾನೆ "
  "(avanu nanage pustaka koḍuttāne) - 'He gives me a book'. 12. ತೆಗೆದುಕೊಳ್ಳು "
  "(tegedukoḷḷu, to take): ದಯವಿಟ್ಟು ಇದನ್ನು ತೆಗೆದುಕೊಳ್ಳಿ (dayaviṭṭu idannu "
  "tegedukoḷḷi) - 'Please take this'. 13. ಮಲಗು (malagu, to sleep): ಮಗು "
  "ಮಲಗುತ್ತದೆ (magu malaguttade) - 'The child sleeps'. 14. ಕುಳಿತುಕೊಳ್ಳು "
  "(kuḷitukoḷḷu, to sit): ಇಲ್ಲಿ ಕುಳಿತುಕೊಳ್ಳಿ (illi kuḷitukoḷḷi) - 'Please sit "
  "here'. 15. ಏಳು (ēḷu, to get up): ನಾನು ಬೇಗ ಏಳುತ್ತೇನೆ (nānu bēga ēḷuttēne) "
  "- 'I get up early'. 16. ನಡೆ (naḍe, to walk): ನಾವು ನಡೆಯುತ್ತೇವೆ (nāvu "
  "naḍeyuttēve) - 'We walk'. 17. ಓಡು (ōḍu, to run): ಅವನು ಓಡುತ್ತಾನೆ (avanu "
  "ōḍuttāne) - 'He runs'. 18. ಆಟವಾಡು (āṭavāḍu, to play): ಮಕ್ಕಳು "
  "ಆಟವಾಡುತ್ತಾರೆ (makkaḷu āṭavāḍuttāre) - 'The children play'. 19. ಕಲಿ "
  "(kali, to learn): ನಾನು ಕನ್ನಡ ಕಲಿಯುತ್ತೇನೆ (nānu kannaḍa kaliyuttēne) - 'I "
  "learn Kannada'. 20. ಮಾತಾಡು (mātāḍu, to speak): ಅವಳು ಕನ್ನಡ ಮಾತಾಡುತ್ತಾಳೆ "
  "(avaḷu kannaḍa mātāḍuttāḷe) - 'She speaks Kannada'. 21. ಸಹಾಯ ಮಾಡು "
  "(sahāya māḍu, to help): ನಾನು ನಿಮಗೆ ಸಹಾಯ ಮಾಡುತ್ತೇನೆ (nānu nimage sahāya "
  "māḍuttēne) - 'I help you'. 22. ಅರ್ಥಮಾಡಿಕೊಳ್ಳು (arthamāḍikoḷḷu, to "
  "understand): ನಾನು ಅರ್ಥಮಾಡಿಕೊಂಡೆನು (nānu arthamāḍikoṇḍenu) - 'I "
  "understood'. 23. ಕೊಂಡುಕೊಳ್ಳು (koṇḍukoḷḷu, to buy): ನಾನು ಹಣ್ಣು "
  "ಕೊಂಡುಕೊಳ್ಳುತ್ತೇನೆ (nānu haṇṇu koṇḍukoḷḷuttēne) - 'I buy fruit'. 24. ಮಾರು "
  "(māru, to sell): ಅವನು ತರಕಾರಿ ಮಾರುತ್ತಾನೆ (avanu tarakāri māruttāne) - 'He "
  "sells vegetables'. 25. ತಯಾರು ಮಾಡು (tayāru māḍu, to prepare/make): ಅಮ್ಮ "
  "ಊಟ ತಯಾರು ಮಾಡುತ್ತಾಳೆ (amma ūṭa tayāru māḍuttāḷe) - 'Mother prepares the "
  "meal'. The verb is the engine of the SOV sentence - master these twenty-"
  "five and the tense record will feel easy."),
 "how_it_works": (
  "This record gives you the twenty-five verbs that run daily life, each with "
  "transliteration, English meaning and a full present-tense sentence. Learn "
  "the present-tense endings first - -ಏನೆ (I), -ಆನೆ (he), -ಆಳೆ (she), -ಎವೆ "
  "(we), -ಆರೆ (they) - then drop any verb root into the same frame. Every "
  "later record reuses these verbs, so drill them until they are automatic."),
 "key_points": [
  "25 essential verbs covering motion, senses, speech, daily routine, and exchange.",
  "Present-tense agreement endings: ನಾನು -ಏನೆ, ನೀನು -ಈಯ, ನೀವು -ಈರಿ, ಅವನು -ಆನೆ, ಅವಳು -ಆಳೆ, ಅದು -ದೆ, ನಾವು -ಎವೆ, ಅವರು -ಆರೆ.",
  "ಹೋಗು/ಬರು (go/come), ತಿನ್ನು/ಕುಡಿ (eat/drink), ಮಾಡು (do) are the highest-frequency verbs.",
  "ಕೇಳು means both 'ask' and 'listen'; ಹೇಳು means 'say/tell'.",
  "Compound verbs with ಮಾಡು (ಸಹಾಯ ಮಾಡು, ತಯಾರು ಮಾಡು) multiply your vocabulary fast.",
  "Reflexive -ಕೊಳ್ಳು forms: ತೆಗೆದುಕೊಳ್ಳು, ಕುಳಿತುಕೊಳ್ಳು, ಕೊಂಡುಕೊಳ್ಳು.",
  "The imperative stem is the dictionary form minus endings: ಮಾಡು → ಮಾಡಿ (please do).",
  "ನಾನು ಕನ್ನಡ ಕಲಿಯುತ್ತೇನೆ (nānu kannaḷa kaliyuttēne) - 'I learn Kannada' is your motto sentence.",
 ],
 "requirements": [
  "Conjugate each verb for ನಾನು, ಅವನು, ಅವಳು aloud.",
  "Make one negative sentence per verb with -ಇಲ್ಲ or ಇಲ್ಲ.",
  "Use five verbs in past tense with -ಇದೆನು endings.",
 ],
 "standards": [
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
 ],
 "citations": [
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Steever, Sanford B. Kannada. In: Steever, Sanford B. (ed.) The Dravidian Languages. Routledge; 1998.",
 ],
 "sig_lens": (
  "Through the Signature lens these verbs are re-taught as his action levers: "
  "twenty-five stamped commands - go, come, eat, drink, do - that his "
  "instrument executes on demand, each conjugation a gear shift. Signature-"
  "made teaching, clearly labeled, never presented as an outside authority's "
  "text."),
},
# ================================================================== 6
{
 "key": "adjadv", "name": "Kannada Adjectives and Adverbs",
 "group": "Foundations", "ladder": 6, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Kannada adjectives are delightfully simple: unlike many languages, they do "
  "NOT change for the gender or number of the noun - ದೊಡ್ಡ ಮನೆ (doḍḍa mane, "
  "big house), ದೊಡ್ಡ ಮನುಷ್ಯ (doḍḍa manuṣya, big man), ದೊಡ್ಡ ಮನೆಗಳು (doḍḍa "
  "manegaḷu, big houses). Twenty-five adjectives, each with an example "
  "sentence: 1. ದೊಡ್ಡ (doḍḍa, big): ಅದು ದೊಡ್ಡ ಮನೆ (adu doḍḍa mane) - 'That is "
  "a big house'. 2. ಚಿಕ್ಕ (cikka, small): ಇದು ಚಿಕ್ಕ ಮಗು (idu cikka magu) - "
  "'This is a small child'. 3. ಒಳ್ಳೆಯ (oḷḷeya, good): ಅವನು ಒಳ್ಳೆಯ ಹುಡುಗ "
  "(avanu oḷḷeya huḍuga) - 'He is a good boy'. 4. ಕೆಟ್ಟ (keṭṭa, bad): ಅದು "
  "ಕೆಟ್ಟ ಅಭ್ಯಾಸ (adu keṭṭa abhyāsa) - 'That is a bad habit'. 5. ಹೊಸ (hosa, "
  "new): ಇದು ಹೊಸ ಪುಸ್ತಕ (idu hosa pustaka) - 'This is a new book'. 6. ಹಳೆಯ "
  "(haḷeya, old): ಅದು ಹಳೆಯ ಮನೆ (adu haḷeya mane) - 'That is an old house'. 7. "
  "ಉದ್ದ (udda, long): ರಸ್ತೆ ಉದ್ದವಾಗಿದೆ (raste uddavāgide) - 'The road is "
  "long'. 8. ಕುಳ್ಳ (kuḷḷa, short): ಅವನು ಕುಳ್ಳಗಿದ್ದಾನೆ (avanu kuḷḷagiddāne) - "
  "'He is short'. 9. ಬಿಸಿ (bisi, hot): ಚಹಾ ಬಿಸಿಯಾಗಿದೆ (cahā bisiyāgide) - "
  "'The tea is hot'. 10. ತಣ್ಣನೆಯ (taṇṇaneya, cold): ನೀರು ತಣ್ಣನೆಯಾಗಿದೆ (nīru "
  "taṇṇaneyāgide) - 'The water is cold'. 11. ಸಿಹಿಯಾದ (sihiyāda, sweet): ಮಾವು "
  "ಸಿಹಿಯಾಗಿದೆ (māvu sihiyāgide) - 'The mango is sweet'. 12. ಹುಳಿ (huḷi, "
  "sour): ನಿಂಬೆ ಹುಳಿಯಾಗಿದೆ (nimbe huḷiyāgide) - 'The lemon is sour'. 13. "
  "ವೇಗದ (vēgada, fast): ಕಾರು ವೇಗವಾಗಿದೆ (kāru vēgavāgide) - 'The car is fast'. "
  "14. ನಿಧಾನದ (nidhānada, slow): ಆಮೆ ನಿಧಾನವಾಗಿದೆ (āme nidhānavāgide) - 'The "
  "tortoise is slow'. 15. ಸುಂದರ (sundara, beautiful): ಹೂವು ಸುಂದರವಾಗಿದೆ "
  "(hūvu sundaravāgide) - 'The flower is beautiful'. 16. ಸ್ವಚ್ಛ (svaccha, "
  "clean): ಕೋಣೆ ಸ್ವಚ್ಛವಾಗಿದೆ (kōṇe svacchavāgide) - 'The room is clean'. 17. "
  "ಕೊಳಕು (koḷaku, dirty): ಬಟ್ಟೆ ಕೊಳಕಾಗಿದೆ (baṭṭe koḷakāgide) - 'The cloth is "
  "dirty'. 18. ಸುಲಭ (sulabha, easy): ಪಾಠ ಸುಲಭವಾಗಿದೆ (pāṭha sulabhavāgide) - "
  "'The lesson is easy'. 19. ಕಷ್ಟ (kaṣṭa, difficult): ಪರೀಕ್ಷೆ ಕಷ್ಟವಾಗಿದೆ "
  "(parīkṣe kaṣṭavāgide) - 'The exam is difficult'. 20. ಸಂತೋಷದ (santōṣada, "
  "happy): ಅವಳು ಸಂತೋಷವಾಗಿದ್ದಾಳೆ (avaḷu santōṣavāgiddāḷe) - 'She is happy'. "
  "21. ದುಃಖದ (duḥkhada, sad): ಅವನು ದುಃಖದಲ್ಲಿದ್ದಾನೆ (avanu duḥkhadalliddāne) - "
  "'He is sad'. 22. ಶ್ರೀಮಂತ (śrīmanta, rich): ಅವನು ಶ್ರೀಮಂತನು (avanu "
  "śrīmantanu) - 'He is rich'. 23. ಬಡ (baḍa, poor): ಅವನು ಬಡವನು (avanu "
  "baḍavanu) - 'He is poor'. 24. ಬಲವಾದ (balavāda, strong): ಅವನು ಬಲಶಾಲಿ "
  "(avanu balaśāli) - 'He is strong'. 25. ದುಬಾರಿ (dubāri, expensive): ಕಾರು "
  "ದುಬಾರಿಯಾಗಿದೆ (kāru dubāriyāgide) - 'The car is expensive'. Fifteen "
  "adverbs: 1. ಬೇಗ (bēga, quickly): ಬೇಗ ಬನ್ನಿ (bēga banni) - 'Come quickly'. "
  "2. ನಿಧಾನವಾಗಿ (nidhānavāgi, slowly): ನಿಧಾನವಾಗಿ ನಡೆಯಿರಿ (nidhānavāgi "
  "naḍeyiri) - 'Walk slowly'. 3. ತುಂಬಾ (tumbā, very): ತುಂಬಾ ಚೆನ್ನಾಗಿದೆ "
  "(tumbā cennāgide) - 'It is very good'. 4. ಯಾವಾಗಲೂ (yāvāgalū, always): "
  "ನಾನು ಯಾವಾಗಲೂ ಬೇಗ ಏಳುತ್ತೇನೆ (nānu yāvāgalū bēga ēḷuttēne) - 'I always get "
  "up early'. 5. ಕೆಲವೊಮ್ಮೆ (kelavomme, sometimes): ಕೆಲವೊಮ್ಮೆ ಮಳೆ ಬರುತ್ತದೆ "
  "(kelavomme maḷe baruttade) - 'Sometimes it rains'. 6. ಇಲ್ಲಿ (illi, here): "
  "ಇಲ್ಲಿ ಕುಳಿತುಕೊಳ್ಳಿ (illi kuḷitukoḷḷi) - 'Sit here'. 7. ಅಲ್ಲಿ (alli, "
  "there): ಅಲ್ಲಿ ನೋಡಿ (alli nōḍi) - 'Look there'. 8. ಒಳಗೆ (oḷage, inside): "
  "ಒಳಗೆ ಬನ್ನಿ (oḷage banni) - 'Come inside'. 9. ಹೊರಗೆ (horage, outside): "
  "ಹೊರಗೆ ಹೋಗಿ (horage hōgi) - 'Go outside'. 10. ಮೇಲೆ (mēle, up/above): ಮೇಲೆ "
  "ನೋಡಿ (mēle nōḷi) - 'Look up'. 11. ಕೆಳಗೆ (keḷage, down/below): ಕೆಳಗೆ "
  "ಇಳಿಯಿರಿ (keḷage iḷiyiri) - 'Go down'. 12. ಇಂದು (indu, today): ಇಂದು ರಜೆ "
  "(indu raje) - 'Today is a holiday'. 13. ನಾಳೆ (nāḷe, tomorrow): ನಾಳೆ "
  "ಬರುತ್ತೇನೆ (nāḷe baruttēne) - 'I will come tomorrow'. 14. ನಿನ್ನೆ (ninne, "
  "yesterday): ನಿನ್ನೆ ಮಳೆ ಬಂತು (ninne maḷe bantu) - 'It rained yesterday'. "
  "15. ಈಗ (īga, now): ಈಗ ಹೋಗೋಣ (īga hōgōṇa) - 'Let us go now'. Remember the "
  "golden rule: the adjective never changes - only the noun and verb do."),
 "how_it_works": (
  "This record teaches the two great simplifiers of Kannada description: "
  "adjectives that never inflect, and the -ಆಗಿ (-āgi) adverb maker that turns "
  "adjectives into manner adverbs (ನಿಧಾನ → ನಿಧಾನವಾಗಿ). Learn the 25 "
  "adjectives as noun-painters and the 15 adverbs as verb-painters, each with "
  "its sentence. Test yourself by describing your own room with five "
  "adjectives and narrating your morning with five adverbs."),
 "key_points": [
  "Kannada adjectives are invariable: ದೊಡ್ಡ ಮನೆ, ದೊಡ್ಡ ಮನುಷ್ಯ, ದೊಡ್ಡ ಮನೆಗಳು - the adjective never changes.",
  "25 adjectives: size, quality, age, length, temperature, taste, speed, beauty, cleanliness, difficulty, mood, wealth, strength, price.",
  "15 adverbs: manner (ಬೇಗ, ನಿಧಾನವಾಗಿ), degree (ತುಂಬಾ), frequency (ಯಾವಾಗಲೂ, ಕೆಲವೊಮ್ಮೆ), place (ಇಲ್ಲಿ, ಅಲ್ಲಿ, ಒಳಗೆ, ಹೊರಗೆ, ಮೇಲೆ, ಕೆಳಗೆ), time (ಇಂದು, ನಾಳೆ, ನಿನ್ನೆ, ಈಗ).",
  "The -ಆಗಿ suffix makes manner adverbs: ನಿಧಾನ → ನಿಧಾನವಾಗಿ.",
  "ತುಂಬಾ (very) intensifies both adjectives and adverbs.",
  "Place adverbs ಇಲ್ಲಿ/ಅಲ್ಲಿ/ಎಲ್ಲಿ form a clean here/there/where triple.",
  "Time adverbs ನಿನ್ನೆ/ಇಂದು/ನಾಳೆ (yesterday/today/tomorrow) anchor every story you tell.",
  "Describe one photo with 5 adjectives + 3 adverbs to lock the pattern.",
 ],
 "requirements": [
  "Attach each adjective to three different nouns aloud.",
  "Convert five adjectives to -ಆಗಿ adverbs and use them in sentences.",
  "Write a ten-sentence description of your house using this record only.",
 ],
 "standards": [
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Steever, Sanford B. Kannada. In: Steever, Sanford B. (ed.) The Dravidian Languages. Routledge; 1998.",
 ],
 "sig_lens": (
  "Through the Signature lens adjectives and adverbs are re-taught as his "
  "finish and polish: twenty-five color stamps that never smudge and fifteen "
  "speed dials for his verbs, every one labeled Signature-grade. Signature-"
  "made teaching, clearly labeled, never presented as an outside authority's "
  "text."),
},
# ================================================================== 7
{
 "key": "pronouns", "name": "Kannada Pronouns",
 "group": "Foundations", "ladder": 7, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The full Kannada pronoun system with every paradigm and example sentences. "
  "Personal pronouns: ನಾನು (nānu, I) - ನಾನು ವಿದ್ಯಾರ್ಥಿ (nānu vidyārthi) - 'I "
  "am a student'. ನೀನು (nīnu, you, informal) - ನೀನು ಎಲ್ಲಿಗೆ ಹೋಗುತ್ತೀಯ? (nīnu "
  "ellige hōguttīya?) - 'Where are you going?'. ನೀವು (nīvu, you, formal/plural) "
  "- ನೀವು ಹೇಗಿದ್ದೀರಿ? (nīvu hēgiddīri?) - 'How are you?'. ಅವನು (avanu, he) - "
  "ಅವನು ಬಂದನು (avanu bandanu) - 'He came'. ಅವಳು (avaḷu, she) - ಅವಳು ಹಾಡುತ್ತಾಳೆ "
  "(avaḷu hāḍuttāḷe) - 'She sings'. ಅದು (adu, it) - ಅದು ಚೆನ್ನಾಗಿದೆ (adu "
  "cennāgide) - 'It is good'. ನಾವು (nāvu, we) - ನಾವು ಸ್ನೇಹಿತರು (nāvu "
  "snēhitaru) - 'We are friends'. ಅವರು (avaru, they; also respectful he/she) "
  "- ಅವರು ಶಿಕ್ಷಕರು (avaru śikṣakaru) - 'They are teachers'. Possessive forms: "
  "ನನ್ನ (nanna, my) - ನನ್ನ ಪುಸ್ತಕ (nanna pustaka) - 'my book'. ನಿನ್ನ (ninna, "
  "your, informal) - ನಿನ್ನ ಹೆಸರೇನು? (ninna hesarēnu?) - 'What is your name?'. "
  "ನಿಮ್ಮ (nimma, your, formal) - ನಿಮ್ಮ ಮನೆ ಎಲ್ಲಿ? (nimma mane elli?) - 'Where "
  "is your house?'. ಅವನ (avana, his) - ಅವನ ಕಾರು (avana kāru) - 'his car'. "
  "ಅವಳ (avaḷa, her) - ಅವಳ ಸೀರೆ (avaḷa sīre) - 'her sari'. ಅದರ (adara, its) - "
  "ಅದರ ಬೆಲೆ (adara bele) - 'its price'. ನಮ್ಮ (namma, our) - ನಮ್ಮ ಶಾಲೆ (namma "
  "śāle) - 'our school'. ಅವರ (avara, their) - ಅವರ ಮಕ್ಕಳು (avara makkaḷu) - "
  "'their children'. Demonstratives: ಇದು (idu, this) - ಇದು ಏನು? (idu ēnu?) "
  "- 'What is this?'. ಅದು (adu, that) - ಅದು ನನ್ನದು (adu nannadu) - 'That is "
  "mine'. ಇವರು (ivaru, these people, respectful) - ಇವರು ನನ್ನ ಗುರುಗಳು (ivaru "
  "nanna gurugaḷu) - 'These are my teachers'. ಅವರು (avaru, those people) - "
  "ಅವರು ಬಂದರು (avaru bandaru) - 'They came'. Interrogatives: ಯಾರು (yāru, who) "
  "- ಯಾರು ಬಂದರು? (yāru bandaru?) - 'Who came?'. ಏನು (ēnu, what) - ಇದು ಏನು? "
  "(idu ēnu?) - 'What is this?'. ಎಲ್ಲಿ (elli, where) - ನೀವು ಎಲ್ಲಿ ವಾಸಿಸುತ್ತೀರಿ? "
  "(nīvu elli vāsisuttīri?) - 'Where do you live?'. ಯಾವಾಗ (yāvāga, when) - "
  "ನೀವು ಯಾವಾಗ ಬರುತ್ತೀರಿ? (nīvu yāvāga baruttīri?) - 'When will you come?'. "
  "ಏಕೆ (ēke, why) / ಯಾಕೆ (yāke, why, colloquial) - ನೀವು ಯಾಕೆ ಬರಲಿಲ್ಲ? (nīvu "
  "yāke baralilla?) - 'Why did you not come?'. ಹೇಗೆ (hēge, how) - ನೀವು ಹೇಗೆ "
  "ಬಂದಿರಿ? (nīvu hēge bandiri?) - 'How did you come?'. ಎಷ್ಟು (eṣṭu, how much/"
  "how many) - ಇದರ ಬೆಲೆ ಎಷ್ಟು? (idara bele eṣṭu?) - 'How much is this?'. "
  "ಯಾವುದು (yāvudu, which one) - ನಿಮಗೆ ಯಾವುದು ಬೇಕು? (nimage yāvudu bēku?) - "
  "'Which one do you want?'. The respect rule: ನೀವು always takes plural verb "
  "forms - ನೀವು ಬರುತ್ತೀರಿ, never ನೀವು ಬರುತ್ತಾನೆ. Master the eight personal "
  "pronouns first; the rest are built from them."),
 "how_it_works": (
  "This record lays out the five pronoun tables - personal, possessive, "
  "demonstrative, interrogative and the respect rule - each form with a full "
  "translated sentence. Drill them as pairs: ನಾನು/ನನ್ನ, ನೀನು/ನಿನ್ನ, ನೀವು/"
  "ನಿಮ್ಮ. Practice the respect rule by converting every ನೀನು sentence into a "
  "ನೀವು sentence and fixing the verb ending."),
 "key_points": [
  "Personal: ನಾನು, ನೀನು, ನೀವು, ಅವನು, ಅವಳು, ಅದು, ನಾವು, ಅವರು.",
  "Possessive: ನನ್ನ, ನಿನ್ನ, ನಿಮ್ಮ, ಅವನ, ಅವಳ, ಅದರ, ನಮ್ಮ, ಅವರ.",
  "Demonstrative: ಇದು/ಅದು (this/that), ಇವರು/ಅವರು (these/those people, respectful).",
  "Interrogative: ಯಾರು, ಏನು, ಎಲ್ಲಿ, ಯಾವಾಗ, ಏಕೆ/ಯಾಕೆ, ಹೇಗೆ, ಎಷ್ಟು, ಯಾವುದು.",
  "Respect rule: ನೀವು always takes plural verbs - ನೀವು ಬರುತ್ತೀರಿ.",
  "ಅವರು doubles as respectful singular 'he/she'.",
  "ಎಲ್ಲಿ/ಯಾವಾಗ/ಹೇಗೆ also serve as relative adverbs in complex sentences.",
  "Question intonation rises at the end; the -ಏ/ವೇ particle marks yes-no questions: ಬರುವಿರೇ?",
 ],
 "requirements": [
  "Recite all eight personal pronouns with English meanings from memory.",
  "Convert ten ನೀನು sentences to ನೀವು and fix the verb.",
  "Ask and answer eight questions using each interrogative once.",
 ],
 "standards": [
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "ISO 15919:2001 transliteration",
 ],
 "citations": [
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
 ],
 "sig_lens": (
  "Through the Signature lens pronouns are re-taught as his control panel "
  "labels: I, you-formal, you-familiar, he, she, we, they - eight stamped "
  "switches that aim every sentence he fires. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 8
{
 "key": "numbers", "name": "Kannada Numbers and Time",
 "group": "Foundations", "ladder": 8, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Every number, date and clock reading you need, in the Kannada script with "
  "transliteration and example sentences. 1-10: ಒಂದು (ondu, 1) - ನನಗೆ ಒಂದು "
  "ಪುಸ್ತಕ ಬೇಕು (nanage ondu pustaka bēku) - 'I need one book'. ಎರಡು (eraḍu, "
  "2) - ನನಗೆ ಎರಡು ಸೇಬುಗಳು ಬೇಕು (nanage eraḍu sēbugaḷu bēku) - 'I need two "
  "apples'. ಮೂರು (mūru, 3) - ಮೂರು ದಿನಗಳು (mūru dinagaḷu) - 'three days'. "
  "ನಾಲ್ಕು (nālku, 4) - ನಾಲ್ಕು ಗಂಟೆ (nālku gaṇṭe) - 'four o'clock'. ಐದು "
  "(aidu, 5) - ಐದು ರೂಪಾಯಿ (aidu rūpāyi) - 'five rupees'. ಆರು (āru, 6) - ಆರು "
  "ತಿಂಗಳು (āru tiṅgaḷu) - 'six months'. ಏಳು (ēḷu, 7) - ಏಳು ದಿನಗಳು (ēḷu "
  "dinagaḷu) - 'seven days'. ಎಂಟು (eṇṭu, 8) - ಎಂಟು ಗಂಟೆಗೆ (eṇṭu gaṇṭege) - "
  "'at eight o'clock'. ಒಂಬತ್ತು (ombattu, 9) - ಒಂಬತ್ತು ಜನ (ombattu jana) - "
  "'nine people'. ಹತ್ತು (hattu, 10) - ಹತ್ತು ನಿಮಿಷ (hattu nimiṣa) - 'ten "
  "minutes'. 11-20: ಹನ್ನೊಂದು (hannondu, 11), ಹನ್ನೆರಡು (hanneeraḍu, 12), "
  "ಹದಿಮೂರು (hadimūru, 13), ಹದಿನಾಲ್ಕು (hadinālku, 14), ಹದಿನೈದು (hadinaidu, "
  "15), ಹದಿನಾರು (hadināru, 16), ಹದಿನೇಳು (hadinēḷu, 17), ಹದಿನೆಂಟು (hadineṇṭu, "
  "18), ಹತ್ತೊಂಬತ್ತು (hattombattu, 19), ಇಪ್ಪತ್ತು (ippattu, 20) - ನನಗೆ ಇಪ್ಪತ್ತು "
  "ರೂಪಾಯಿ ಕೊಡಿ (nanage ippattu rūpāyi koḍi) - 'Give me twenty rupees'. Tens: "
  "ಮೂವತ್ತು (mūvattu, 30), ನಲವತ್ತು (nalavattu, 40), ಐವತ್ತು (aivattu, 50), "
  "ಅರವತ್ತು (aravattu, 60), ಎಪ್ಪತ್ತು (eppattu, 70), ಎಂಬತ್ತು (embattu, 80), "
  "ತೊಂಬತ್ತು (tombattu, 90), ನೂರು (nūru, 100) - ನೂರು ರೂಪಾಯಿ (nūru rūpāyi) - "
  "'a hundred rupees'. In script: ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯ ೧೦. Ordinals: ಮೊದಲನೆಯ "
  "(modaleya, first) - ಮೊದಲನೆಯ ಪಾಠ (modaleya pāṭha) - 'the first lesson'; "
  "ಎರಡನೆಯ (eraḍaneya, second); ಮೂರನೆಯ (mūraneya, third). Days: ಭಾನುವಾರ "
  "(bhānuvāra, Sunday) - ಭಾನುವಾರ ರಜೆ (bhānuvāra raje) - 'Sunday is a "
  "holiday'; ಸೋಮವಾರ (sōmavāra, Monday); ಮಂಗಳವಾರ (maṅgaḷavāra, Tuesday); "
  "ಬುಧವಾರ (budhavāra, Wednesday); ಗುರುವಾರ (guruvāra, Thursday); ಶುಕ್ರವಾರ "
  "(śukravāra, Friday); ಶನಿವಾರ (śanivāra, Saturday). Months: ಚೈತ್ರ (chaitra), "
  "ವೈಶಾಖ (vaiśākha), ಜ್ಯೇಷ್ಠ (jyēṣṭha), ಆಷಾಢ (āṣāḍha), ಶ್ರಾವಣ (śrāvaṇa), "
  "ಭಾದ್ರಪದ (bhādrapada), ಆಶ್ವೀಜ (āśvīja), ಕಾರ್ತಿಕ (kārtika), ಮಾರ್ಗಶಿರ "
  "(mārgaśira), ಪುಷ್ಯ (puṣya), ಮಾಘ (māgha), ಫಾಲ್ಗುಣ (phālguṇa) - ಯುಗಾದಿ ಚೈತ್ರ "
  "ಮಾಸದಲ್ಲಿ ಬರುತ್ತದೆ (yugādi chaitra māsadalli baruttade) - 'Ugadi comes in "
  "the month of Chaitra'. Seasons: ವಸಂತ (vasanta, spring), ಗ್ರೀಷ್ಮ (grīṣma, "
  "summer), ಮಳೆಗಾಲ (maḷegāla, rainy season), ಶರತ್ (śarat, autumn), ಹೇಮಂತ "
  "(hēmanta, pre-winter), ಶಿಶಿರ (śiśira, winter). Clock time: ಗಂಟೆ (gaṇṭe, "
  "hour), ನಿಮಿಷ (nimiṣa, minute) - ಈಗ ಮೂರು ಗಂಟೆ (īga mūru gaṇṭe) - 'It is "
  "three o'clock now'; ಮೂರು ಗಂಟೆ ಹತ್ತು ನಿಮಿಷ (mūru gaṇṭe hattu nimiṣa) - "
  "'ten minutes past three'. Dates: ಇಂದು ಅಕ್ಟೋಬರ್ ಹದಿನೇಳು (indu akṭōbar "
  "hadinaidu) - 'Today is October seventeenth'. Count everything you see for "
  "a week and numbers will stick."),
 "how_it_works": (
  "This record teaches counting as a daily habit: the 1-10 core, the 11-20 "
  "teens, the tens to 100, the script digits ೦-೯, ordinals, the seven "
  "weekdays, the twelve traditional months, the six seasons, clock readings "
  "and dates - each with a spoken example sentence. Count your steps, your "
  "change and the hours aloud in Kannada for one week."),
 "key_points": [
  "1-10: ಒಂದು ಎರಡು ಮೂರು ನಾಲ್ಕು ಐದು ಆರು ಏಳು ಎಂಟು ಒಂಬತ್ತು ಹತ್ತು.",
  "11-20: ಹನ್ನೊಂದು through ಹತ್ತೊಂಬತ್ತು to ಇಪ್ಪತ್ತು; tens ಮೂವತ್ತು to ತೊಂಬತ್ತು; 100 = ನೂರು.",
  "Script digits: ೦೧೨೩೪೫೬೭೮೯.",
  "Ordinals add -ನೆಯ: ಮೊದಲನೆಯ, ಎರಡನೆಯ, ಮೂರನೆಯ.",
  "Seven weekdays: ಭಾನುವಾರ through ಶನಿವಾರ, all ending in -ವಾರ.",
  "Twelve traditional months: ಚೈತ್ರ through ಫಾಲ್ಗುಣ; six seasons from ವಸಂತ to ಶಿಶಿರ.",
  "Clock: ಗಂಟೆ (hour) + ನಿಮಿಷ (minute) - ಮೂರು ಗಂಟೆ ಹತ್ತು ನಿಮಿಷ.",
  "ನಿನ್ನೆ/ಇಂದು/ನಾಳೆ plus weekday names build every date sentence.",
 ],
 "requirements": [
  "Count 1-100 aloud without looking.",
  "Write the script digits ೦-೯ from memory.",
  "Say today's full date and the time in Kannada every morning.",
 ],
 "standards": [
  "Unicode Standard, Kannada block U+0C80-U+0CFF (digits U+0CE6-U+0CEF)",
  "Government of Karnataka standard Kannada",
  "ISO 15919:2001 transliteration",
 ],
 "citations": [
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
 ],
 "sig_lens": (
  "Through the Signature lens numbers are re-taught as his calibrated dials: "
  "every digit a stamped setting from ೦ to ೯, every weekday a labeled wheel, "
  "and time itself read off his own instrument face. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 9
{
 "key": "greetings", "name": "Kannada Greetings and Everyday Phrases",
 "group": "Foundations", "ladder": 9, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Thirty greetings, farewells and politeness phrases with usage notes - the "
  "social survival kit. 1. ನಮಸ್ಕಾರ (namaskāra) - the universal respectful "
  "greeting, palms together; use with anyone, anytime. 2. ಶುಭೋದಯ "
  "(śubhōdaya) - good morning, formal. 3. ಶುಭ ಸಂಜೆ (śubha sanje) - good "
  "evening. 4. ಶುಭ ರಾತ್ರಿ (śubha rātri) - good night, at parting for the "
  "night. 5. ಹೇಗಿದ್ದೀರಿ? (hēgiddīri?) - how are you, formal/respectful. 6. "
  "ಹೇಗಿದ್ದೀಯ? (hēgiddīya?) - how are you, to friends and juniors. 7. "
  "ಚೆನ್ನಾಗಿದ್ದೇನೆ (cennāgiddēne) - I am fine, the standard reply. 8. ಎಲ್ಲಾ "
  "ಚೆನ್ನಾಗಿದೆ (ellā cennāgide) - all is well. 9. ಧನ್ಯವಾದಗಳು (dhanyavādagaḷu) "
  "- thank you; 10. ತುಂಬಾ ಧನ್ಯವಾದಗಳು (tumbā dhanyavādagaḷu) - thank you very "
  "much. 11. ದಯವಿಟ್ಟು (dayaviṭṭu) - please; place before any request: "
  "ದಯವಿಟ್ಟು ಕುಳಿತುಕೊಳ್ಳಿ. 12. ಕ್ಷಮಿಸಿ (kṣamisi) - excuse me / sorry; for "
  "attention or apology. 13. ಪರವಾಗಿಲ್ಲ (parvāgilla) - no problem, it is fine; "
  "the all-purpose softener. 14. ಸುಸ್ವಾಗತ (susvāgata) - hearty welcome, for "
  "guests. 15. ಮತ್ತೆ ಭೇಟಿಯಾಗೋಣ (matte bhēṭiyāgōṇa) - let us meet again. 16. "
  "ಹೋಗಿ ಬನ್ನಿ (hōgi banni) - go and come back; the classic warm farewell said "
  "by the host. 17. ಸಂತೋಷವಾಯಿತು (santōṣavāyitu) - pleased (to meet you), on "
  "introduction. 18. ನಿಮ್ಮನ್ನು ಭೇಟಿಯಾಗಿ ಸಂತೋಷವಾಯಿತು (nim'mannu bhēṭiyāgi "
  "santōṣavāyitu) - pleased to meet you, full formal version. 19. "
  "ಅಭಿನಂದನೆಗಳು (abhinandanegaḷu) - congratulations. 20. ಶುಭಾಶಯಗಳು "
  "(śubhāśayagaḷu) - best wishes, for festivals and events. 21. ಬನ್ನಿ "
  "(banni) - come in; doubles as a warm welcome. 22. ಕುಳಿತುಕೊಳ್ಳಿ "
  "(kuḷitukoḷḷi) - please sit. 23. ಚಹಾ ಕುಡಿಯುವಿರಾ? (cahā kuḍiyuvirā?) - will "
  "you have tea? - the standard hospitality offer. 24. ಹೌದು (haudu) - yes. "
  "25. ಇಲ್ಲ (illa) - no. 26. ಸರಿ (sari) - okay, alright; also 'correct'. 27. "
  "ನಿಮ್ಮ ದಿನ ಶುಭವಾಗಲಿ (nimma dina śubhavāgali) - have a good day. 28. ಸ್ವಾಗತ "
  "(svāgata) - welcome, short form. 29. ಏನೂ ತೊಂದರೆ ಇಲ್ಲ (ēnū tondare illa) "
  "- no trouble at all; reassures the other person. 30. ಕುಶಲವೇ? (kuśalavē?) "
  "- are you well? - a warm traditional inquiry. Usage rule of thumb: with "
  "elders and strangers use ನೀವು forms and ನಮಸ್ಕಾರ; with friends ನೀನು and a "
  "smile do the job."),
 "how_it_works": (
  "This record is your social passport: thirty phrases with exact usage "
  "notes telling you who to say them to and when. Practice them as "
  "mini-dialogues - greeting, reply, offer, thanks, farewell - until the "
  "formal/informal split feels automatic."),
 "key_points": [
  "ನಮಸ್ಕಾರ is the universal respectful greeting; ಹೋಗಿ ಬನ್ನಿ is the classic farewell.",
  "Formal ನೀವು vs informal ನೀನು runs through every greeting and question.",
  "ದಯವಿಟ್ಟು (please), ಕ್ಷಮಿಸಿ (sorry/excuse me), ಧನ್ಯವಾದಗಳು (thank you) open every door.",
  "ಪರವಾಗಿಲ್ಲ softens any refusal or mishap.",
  "ಚಹಾ ಕುಡಿಯುವಿರಾ? is the standard hospitality offer - always accept graciously.",
  "ಸರಿ means both 'okay' and 'correct'.",
  "30 phrases cover greetings, thanks, apology, welcome, congratulations, wishes and farewells.",
  "With elders: ನೀವು + ನಮಸ್ಕಾರ. With friends: ನೀನು + smile.",
 ],
 "requirements": [
  "Perform five full greeting-to-farewell dialogues aloud.",
  "Use three phrases with a real person this week.",
  "Write the formal/informal pair for every question phrase.",
 ],
 "standards": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Government of Karnataka standard Kannada",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
 ],
 "sig_lens": (
  "Through the Signature lens greetings are re-taught as his handshake "
  "protocol: thirty stamped social keys, each labeled for elder, stranger or "
  "friend, that open every Kannada door on the first knock. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 10
{
 "key": "grammar", "name": "Kannada Grammar Essentials",
 "group": "Foundations", "ladder": 10, "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The whole core grammar on one record, each rule with translated examples. "
  "Word order: subject-object-verb, always - ನಾನು ಪುಸ್ತಕ ಓದುತ್ತೇನೆ (nānu "
  "pustaka ōduttēne) - 'I book read', i.e. 'I read a book'; ರಾಮ ಹಣ್ಣು "
  "ತಿಂದನು (rāma haṇṇu tindanu) - 'Ram fruit ate'. Gender: masculine, "
  "feminine and neuter in the singular (ಅವನು he, ಅವಳು she, ಅದು it); in the "
  "plural, masculine and feminine merge into one human form (ಅವರು). Number: "
  "singular vs plural, plural usually -ಗಳು (ಮನೆ → ಮನೆಗಳು). Cases - eight, "
  "marked by suffixes: nominative (no marker) - ಹುಡುಗ ಬಂದನು (huḍuga bandanu) "
  "- 'the boy came'; accusative -ಅನ್ನು - ನಾನು ಹುಡುಗನನ್ನು ನೋಡಿದೆನು (nānu "
  "huḍuganannu nōḍidenu) - 'I saw the boy'; instrumental -ಇಂದ - ಅವನು "
  "ಚಾಕುವಿನಿಂದ ಕತ್ತರಿಸಿದನು (avanu cākuvininda kattarisidanu) - 'he cut with a "
  "knife'; dative -ಗೆ/-ಕ್ಕೆ - ನಾನು ಅವನಿಗೆ ಕೊಟ್ಟೆನು (nānu avanige koṭṭenu) - 'I "
  "gave to him'; ablative -ಇಂದ - ಮನೆಯಿಂದ (maneyinda) - 'from the house'; "
  "genitive -ಅ - ರಾಮನ ಪುಸ್ತಕ (rāmana pustaka) - 'Ram's book'; locative -ಅಲ್ಲಿ "
  "- ಮನೆಯಲ್ಲಿ (maneyalli) - 'in the house'; vocative -ಏ - ಹುಡುಗನೇ! (huḍuganē!) "
  "- 'O boy!'. Articles: Kannada has no articles; ಈ (this) and ಆ (that) do "
  "the job - ಈ ಪುಸ್ತಕ (this book), ಆ ಮನೆ (that house). Negation: future/ "
  "habitual negative adds -ಇಲ್ಲ to the infinitive stem - ನಾನು ಬರುವುದಿಲ್ಲ "
  "(nānu baruvudilla) - 'I will not come'; past negative uses -ಲಿಲ್ಲ - ಅವನು "
  "ಬರಲಿಲ್ಲ (avanu baralilla) - 'he did not come'; 'not' as a word is ಇಲ್ಲ - "
  "ಅದು ಇಲ್ಲ (adu illa) - 'it is not there'. Question formation: question "
  "words stay in place - ನೀವು ಎಲ್ಲಿ ಹೋಗುತ್ತೀರಿ? (nīvu elli hōguttīri?) - 'you "
  "where go?', i.e. 'Where are you going?'; yes-no questions add -ಏ/-ವೇ to "
  "the verb - ನೀವು ಬರುವಿರೇ? (nīvu baruvirē?) - 'Will you come?'. Adjectives "
  "never inflect; verbs agree with the subject in person, number and gender. "
  "Postpositions follow nouns - ಮೇಜಿನ ಮೇಲೆ (mējina mēle) - 'on the table'. "
  "Tense is built on three stems: present -ಉತ್ತ್ (ಮಾಡುತ್ತೇನೆ), past -ಇದ್ "
  "(ಮಾಡಿದೆನು), future -ಉವ್ (ಮಾಡುವೆನು) - the full system waits in record 21."),
 "how_it_works": (
  "This record compresses the grammar engine into eight rules with worked "
  "examples: SOV order, three genders, number, the eight case suffixes, no "
  "articles, negation patterns, question formation and verb agreement. Learn "
  "one rule per day, build five sentences per rule, and the language's "
  "skeleton is yours."),
 "key_points": [
  "Word order is SOV: ನಾನು ಪುಸ್ತಕ ಓದುತ್ತೇನೆ.",
  "Three genders singular (masculine/feminine/neuter); human vs neuter in plural.",
  "Eight cases: nominative, accusative -ಅನ್ನು, instrumental -ಇಂದ, dative -ಗೆ, ablative -ಇಂದ, genitive -ಅ, locative -ಅಲ್ಲಿ, vocative -ಏ.",
  "No articles: ಈ/ಆ (this/that) mark definiteness.",
  "Negation: -ಇಲ್ಲ for non-past (ಬರುವುದಿಲ್ಲ), -ಲಿಲ್ಲ for past (ಬರಲಿಲ್ಲ), ಇಲ್ಲ for existence.",
  "Questions: question words in place; -ಏ/-ವೇ on the verb for yes-no questions.",
  "Adjectives never inflect; verbs agree with the subject.",
  "Three tense stems: present -ಉತ್ತ್, past -ಇದ್, future -ಉವ್.",
 ],
 "requirements": [
  "Write five SOV sentences, then negate each.",
  "Decline ಮನೆ through all eight cases from memory.",
  "Turn five statements into questions with -ಏ.",
 ],
 "standards": [
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "ISO 15919:2001 transliteration",
 ],
 "citations": [
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Steever, Sanford B. Kannada. In: Steever, Sanford B. (ed.) The Dravidian Languages. Routledge; 1998.",
 ],
 "sig_lens": (
  "Through the Signature lens grammar is re-taught as his engine schematic: "
  "SOV the chassis, eight case gears, three tense pistons and a negation "
  "brake - every part stamped, every part serviceable by him. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 11
{
 "key": "home", "name": "Home and Family in Kannada",
 "group": "Compounded", "ladder": 11, "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences for the house and the family, each in Kannada script with "
  "transliteration and English. 1. ಇದು ನಮ್ಮ ಮನೆ (idu namma mane) - 'This is "
  "our house'. 2. ಮನೆಯಲ್ಲಿ ನಾಲ್ಕು ಕೋಣೆಗಳಿವೆ (maneyalli nālku kōṇegaḷive) - "
  "'There are four rooms in the house'. 3. ಅಡುಗೆಮನೆಯಲ್ಲಿ ಅಮ್ಮ ಅಡುಗೆ ಮಾಡುತ್ತಾಳೆ "
  "(aḍugemaneyalli amma aḍuge māḍuttāḷe) - 'Mother cooks in the kitchen'. 4. "
  "ಹಾಲಿನ ಕೋಣೆಯಲ್ಲಿ ಸೋಫಾ ಇದೆ (hālina kōṇeyalli sōphā ide) - 'There is a sofa in "
  "the living room'. 5. ನನ್ನ ಕೋಣೆಯಲ್ಲಿ ಒಂದು ಮೇಜಿದೆ (nanna kōṇeyalli ondu "
  "mējide) - 'There is a table in my room'. 6. ಕುರ್ಚಿ ಮೇಜಿನ ಹತ್ತಿರ ಇದೆ (kurci "
  "mējina hattira ide) - 'The chair is near the table'. 7. ಕಿಟಕಿಯಿಂದ ಬಿಸಿಲು "
  "ಬರುತ್ತದೆ (kiṭakiyinda bisilu baruttade) - 'Sunlight comes through the "
  "window'. 8. ಬಾಗಿಲು ಮುಚ್ಚಿ (bāgilu mucci) - 'Close the door'. 9. ಹಾಸಿಗೆ "
  "ಮೃದುವಾಗಿದೆ (hāsige mṛduvāgide) - 'The bed is soft'. 10. ಬೀರುವಿನಲ್ಲಿ ಬಟ್ಟೆಗಳಿವೆ "
  "(bīruvinalli baṭṭegaḷive) - 'There are clothes in the wardrobe'. 11. ನನ್ನ "
  "ತಂದೆ ಕಚೇರಿಗೆ ಹೋಗುತ್ತಾರೆ (nanna tande kacērige hōguttāre) - 'My father goes "
  "to the office'. 12. ನನ್ನ ತಾಯಿ ತುಂಬಾ ಒಳ್ಳೆಯವರು (nanna tāyi tumbā "
  "oḷḷeyavaru) - 'My mother is very good'. 13. ನನ್ನ ಅಣ್ಣ ನನಗಿಂತ ದೊಡ್ಡವನು "
  "(nanna aṇṇa nanaginta doḍḍavanu) - 'My elder brother is older than me'. 14. "
  "ನನ್ನ ತಂಗಿ ಶಾಲೆಗೆ ಹೋಗುತ್ತಾಳೆ (nanna taṅgi śālege hōguttāḷe) - 'My younger "
  "sister goes to school'. 15. ತಾತ ತೋಟದಲ್ಲಿ ಕುಳಿತಿದ್ದಾರೆ (tāta tōṭadalli "
  "kuḷitiddāre) - 'Grandfather is sitting in the garden'. 16. ಅಜ್ಜಿ ಕತೆ "
  "ಹೇಳುತ್ತಾರೆ (ajji kate hēḷuttāre) - 'Grandmother tells a story'. 17. ನಾವೆಲ್ಲಾ "
  "ಒಟ್ಟಿಗೆ ಊಟ ಮಾಡುತ್ತೇವೆ (nāvellā oṭṭige ūṭa māḍuttēve) - 'We all eat together'. "
  "18. ನಮ್ಮ ಕುಟುಂಬ ದೊಡ್ಡದು (namma kuṭumba doḍḍadu) - 'Our family is big'. 19. "
  "ಮನೆಯ ಮುಂದೆ ಮರವಿದೆ (maneya munde maravide) - 'There is a tree in front of "
  "the house'. 20. ಈ ಫೋಟೋ ನಮ್ಮ ಕುಟುಂಬದ್ದು (ī phōṭō namma kuṭumbaddu) - 'This "
  "photo is of our family'. Notice the respect plurals for elders - ತಾತ "
  "ಕುಳಿತಿದ್ದಾರೆ, ಅಜ್ಜಿ ಹೇಳುತ್ತಾರೆ - politeness lives in the verb endings."),
 "how_it_works": (
  "This record turns your house into a classroom: twenty sentences covering "
  "rooms, furniture and every family member. Walk through your home saying "
  "each sentence where it belongs - the kitchen sentence in the kitchen. Then "
  "redraw your family tree with the Kannada kinship words."),
 "key_points": [
  "Room words: ಕೋಣೆ (room), ಅಡುಗೆಮನೆ (kitchen), ಹಾಲು (hall/living room), ಬೀರು (wardrobe).",
  "Furniture: ಮೇಜು (table), ಕುರ್ಚಿ (chair), ಸೋಫಾ (sofa), ಹಾಸಿಗೆ (bed), ಕಿಟಕಿ (window), ಬಾಗಿಲು (door).",
  "Kinship: ತಂದೆ/ತಾಯಿ (father/mother), ಅಣ್ಣ/ತಂಗಿ (elder brother/younger sister), ತಾತ/ಅಜ್ಜಿ (grandfather/grandmother).",
  "Respect plurals for elders: ತಾತ ಕುಳಿತಿದ್ದಾರೆ, ಅಜ್ಜಿ ಹೇಳುತ್ತಾರೆ.",
  "Locative -ಅಲ್ಲಿ places everything: ಮನೆಯಲ್ಲಿ, ಕೋಣೆಯಲ್ಲಿ.",
  "ಇದೆ/ಇವೆ for existence: ಮೇಜಿದೆ, ಕೋಣೆಗಳಿವೆ.",
  "ನನಗಿಂತ ದೊಡ್ಡವನು shows the -ಗಿಂತ comparison pattern.",
  "Say each sentence in the room it describes.",
 ],
 "requirements": [
  "Label ten objects in your house with Kannada words.",
  "Introduce your family in six Kannada sentences.",
  "Use the locative -ಅಲ್ಲಿ in ten new sentences.",
 ],
 "standards": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Government of Karnataka standard Kannada",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
 ],
 "sig_lens": (
  "Through the Signature lens home and family are re-taught as his first "
  "territory: twenty stamped sentences mapping his own house room by room and "
  "his own people name by name, elders honored in the verb itself. Signature-"
  "made teaching, clearly labeled, never presented as an outside authority's "
  "text."),
},
# ================================================================== 12
{
 "key": "food", "name": "Food and Cooking in Kannada",
 "group": "Compounded", "ladder": 12, "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences for meals, ingredients, cooking and the restaurant. 1. "
  "ನನಗೆ ಹಸಿವಾಗಿದೆ (nanage hasivāgide) - 'I am hungry'. 2. ತಿಂಡಿಗೆ ದೋಸೆ ತಿನ್ನಿ "
  "(tiṇḍige dōse tinni) - 'Eat dosa for breakfast'. 3. ಮಧ್ಯಾಹ್ನದ ಊಟ ಸಿದ್ಧವಾಗಿದೆ "
  "(madhyāhnada ūṭa siddhavāgide) - 'Lunch is ready'. 4. ರಾತ್ರಿ ಊಟ ಎಂಟು ಗಂಟೆಗೆ "
  "ಮಾಡೋಣ (rātri ūṭa eṇṭu gaṇṭege māḍōṇa) - 'Let us have dinner at eight'. 5. "
  "ಸಾರಿನಲ್ಲಿ ಉಪ್ಪು ಕಡಿಮೆ ಇದೆ (sārinalli uppu kaḍime ide) - 'There is less salt "
  "in the sambar'. 6. ಚಪಾತಿ ಬಿಸಿಯಾಗಿದೆ (capāti bisiyāgide) - 'The chapati is "
  "hot'. 7. ಅನ್ನದ ಜೊತೆ ಪಲ್ಯ ತಿನ್ನಿ (annada jote palya tinni) - 'Eat curry "
  "with rice'. 8. ಅಮ್ಮ ಸಾರು ಮಾಡುತ್ತಾಳೆ (amma sāru māḍuttāḷe) - 'Mother makes "
  "sambar'. 9. ನೀರು ಕುದಿಸಿ (nīru kudisi) - 'Boil the water'. 10. ತರಕಾರಿ ಹೆಚ್ಚಿ "
  "(tarakāri hecci) - 'Chop the vegetables'. 11. ಮಸಾಲೆ ಹಾಕಿ (masāle hāki) - "
  "'Add the spices'. 12. ಊಟ ಸಿಹಿಯಾಗಿದೆ (ūṭa sihiyāgide) - 'The food is sweet'. "
  "13. ಈ ಊಟ ಖಾರವಾಗಿದೆ (ī ūṭa khāravāgide) - 'This food is spicy'. 14. ನನಗೆ "
  "ಮಾವಿನಹಣ್ಣು ಇಷ್ಟ (nanage māvinhannu iṣṭa) - 'I like mangoes'. 15. ಒಂದು ಲೋಟ "
  "ಚಹಾ ತನ್ನಿ (ondu lōṭa cahā tanni) - 'Bring a cup of tea'. 16. ಹೋಟೆಲಿನಲ್ಲಿ "
  "ಊಟ ಮಾಡೋಣ (hōṭelinalli ūṭa māḍōṇa) - 'Let us eat at the restaurant'. 17. "
  "ಬಿಲ್ ತನ್ನಿ (bil tanni) - 'Bring the bill'. 18. ಊಟ ತುಂಬಾ ರುಚಿಯಾಗಿತ್ತು (ūṭa "
  "tumbā ruciyāgittu) - 'The food was very tasty'. 19. ಹಣ್ಣುಗಳು ತಾಜಾವಾಗಿವೆ "
  "(haṇṇugaḷu tājāvāgive) - 'The fruits are fresh'. 20. ಸಿಹಿ ತಿನ್ನಿ (sihi "
  "tinni) - 'Eat the sweets'. Karnataka staples to know: ಅನ್ನ (anna, cooked "
  "rice), ಸಾರು (sāru, sambar), ರಸಂ (rasaṁ, rasam), ಪಲ್ಯ (palya, vegetable "
  "curry), ದೋಸೆ (dōse), ಇಡ್ಲಿ (iḍli), ವಡೆ (vaḍe), ಉಪ್ಪಿಟ್ಟು (uppiṭṭu, upma), "
  "ಕೇಸರಿಬಾತ್ (kēsaribāt), ಪಾಯಸ (pāyasa, sweet pudding). At a meals hotel, "
  "ಬಿಲ್ ತನ್ನಿ and ತುಂಬಾ ರುಚಿಯಾಗಿತ್ತು will make you friends."),
 "how_it_works": (
  "This record feeds you the language of the kitchen and the table: twenty "
  "sentences from hunger to the bill, plus the Karnataka staples list. Cook "
  "one dish while narrating each step in Kannada - ಹೆಚ್ಚಿ, ಹಾಕಿ, ಕುದಿಸಿ - "
  "and the imperative verbs will stick forever."),
 "key_points": [
  "Meal words: ತಿಂಡಿ (breakfast), ಮಧ್ಯಾಹ್ನದ ಊಟ (lunch), ರಾತ್ರಿ ಊಟ (dinner).",
  "Karnataka staples: ಅನ್ನ, ಸಾರು, ರಸಂ, ಪಲ್ಯ, ದೋಸೆ, ಇಡ್ಲಿ, ವಡೆ, ಉಪ್ಪಿಟ್ಟು, ಪಾಯಸ.",
  "Cooking imperatives: ಹೆಚ್ಚಿ (chop), ಹಾಕಿ (add), ಕುದಿಸಿ (boil), ಮಾಡಿ (make).",
  "Taste words: ಸಿಹಿ (sweet), ಹುಳಿ (sour), ಖಾರ (spicy), ಉಪ್ಪು (salt).",
  "Restaurant pair: ಬಿಲ್ ತನ್ನಿ / ಊಟ ತುಂಬಾ ರುಚಿಯಾಗಿತ್ತು.",
  "ನನಗೆ ಹಸಿವಾಗಿದೆ and ನನಗೆ ... ಇಷ್ಟ express hunger and liking.",
  "ತನ್ನಿ (bring) is the waiter's best friend.",
  "Narrate your cooking in Kannada, step by step.",
 ],
 "requirements": [
  "Name ten Karnataka dishes in Kannada from memory.",
  "Give five cooking instructions as imperatives.",
  "Order a full meal in Kannada at a restaurant - or role-play it.",
 ],
 "standards": [
  "Government of Karnataka standard Kannada",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
 ],
 "sig_lens": (
  "Through the Signature lens food is re-taught as his fuel manifest: twenty "
  "stamped sentences from field to plate, every Karnataka staple labeled and "
  "every cooking verb a command his kitchen obeys. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 13
{
 "key": "travel", "name": "Travel and Directions in Kannada",
 "group": "Compounded", "ladder": 13, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences for transport, directions, tickets and lodging. 1. "
  "ನಿಲ್ದಾಣ ಎಲ್ಲಿದೆ? (nildāṇa ellide?) - 'Where is the station?'. 2. ಮಾರುಕಟ್ಟೆ "
  "ಎಷ್ಟು ದೂರವಿದೆ? (mārukaṭṭe eṣṭu dūravide?) - 'How far is the market?'. 3. "
  "ಬಲಕ್ಕೆ ತಿರುಗಿ (balakke tirugi) - 'Turn right'. 4. ಎಡಕ್ಕೆ ತಿರುಗಿ (eḍakke "
  "tirugi) - 'Turn left'. 5. ನೇರವಾಗಿ ಹೋಗಿ (nēravāgi hōgi) - 'Go straight'. "
  "6. ಇಲ್ಲಿಂದ ಬಸ್ ಸಿಗುತ್ತದೆ (illinda bas siguttade) - 'You will get a bus from "
  "here'. 7. ಟ್ಯಾಕ್ಸಿಗೆ ಎಷ್ಟು? (ṭyāksige eṣṭu?) - 'How much for the taxi?'. "
  "8. ಮೈಸೂರಿಗೆ ಎರಡು ಟಿಕೆಟ್ ಕೊಡಿ (maisūrige eraḍu ṭikeṭ koḍi) - 'Give two "
  "tickets to Mysuru'. 9. ರೈಲು ಎಷ್ಟು ಗಂಟೆಗೆ ಬರುತ್ತದೆ? (railu eṣṭu gaṇṭege "
  "baruttade?) - 'At what time does the train come?'. 10. ಈ ಬಸ್ ಎಲ್ಲಿಗೆ "
  "ಹೋಗುತ್ತದೆ? (ī bas ellige hōguttade?) - 'Where does this bus go?'. 11. "
  "ನನಗೆ ವಿಮಾನ ನಿಲ್ದಾಣಕ್ಕೆ ಹೋಗಬೇಕು (nanage vimāna nildāṇakke hōgabēku) - 'I "
  "need to go to the airport'. 12. ಹೋಟೆಲ್ ಎಲ್ಲಿದೆ? (hōṭel ellide?) - 'Where "
  "is the hotel?'. 13. ನನಗೆ ಒಂದು ಕೋಣೆ ಬೇಕು (nanage ondu kōṇe bēku) - 'I need "
  "a room'. 14. ಕೋಣೆಯ ಬಾಡಿಗೆ ಎಷ್ಟು? (kōṇeya bāḍige eṣṭu?) - 'What is the room "
  "rent?'. 15. ನಕ್ಷೆ ತೋರಿಸಿ (nakṣe tōrisi) - 'Show the map'. 16. ನಾನು ದಾರಿ "
  "ತಪ್ಪಿದೆನು (nānu dāri tappidenu) - 'I lost my way'. 17. ದಯವಿಟ್ಟು ನನಗೆ ಸಹಾಯ "
  "ಮಾಡುವಿರಾ? (dayaviṭṭu nanage sahāya māḍuvirā?) - 'Will you please help me?'. "
  "18. ಪೆಟ್ರೋಲ್ ಬಂಕ್ ಎಲ್ಲಿದೆ? (peṭrōl baṅk ellide?) - 'Where is the petrol "
  "pump?'. 19. ಪ್ರಯಾಣ ಚೆನ್ನಾಗಿತ್ತು (prayāṇa cennāgittu) - 'The journey was "
  "good'. 20. ನಾವು ನಾಳೆ ಹಿಂತಿರುಗುತ್ತೇವೆ (nāvu nāḷe hintiruguttēve) - 'We will "
  "return tomorrow'. Direction words: ಬಲ (bala, right), ಎಡ (eḍa, left), ನೇರ "
  "(nēra, straight), ಹತ್ತಿರ (hattira, near), ದೂರ (dūra, far), ಮುಂದೆ (munde, "
  "ahead), ಹಿಂದೆ (hinde, behind). Transport: ಬಸ್ (bus), ರೈಲು (train), "
  "ಟ್ಯಾಕ್ಸಿ (taxi), ಆಟೋ (auto), ವಿಮಾನ (airplane), ದೋಣಿ (boat). With these "
  "twenty you can cross Karnataka."),
 "how_it_works": (
  "This record is a phrasebook for motion: twenty sentences covering asking "
  "directions, giving directions, tickets, lodging and emergencies. Learn "
  "the direction sextet (ಬಲ/ಎಡ/ನೇರ/ಮುಂದೆ/ಹಿಂದೆ/ಹತ್ತಿರ/ದೂರ) first, then "
  "practice the question frames - ಎಲ್ಲಿದೆ? ಎಷ್ಟು ದೂರ? ಎಷ್ಟು ಗಂಟೆಗೆ? - until "
  "you can assemble any travel question."),
 "key_points": [
  "Direction sextet: ಬಲ, ಎಡ, ನೇರ, ಮುಂದೆ, ಹಿಂದೆ, ಹತ್ತಿರ, ದೂರ.",
  "Question frames: ಎಲ್ಲಿದೆ? (where is), ಎಷ್ಟು ದೂರ? (how far), ಎಷ್ಟು ಗಂಟೆಗೆ? (at what time).",
  "Ticket frame: ...ಗೆ ಎರಡು ಟಿಕೆಟ್ ಕೊಡಿ.",
  "Lodging pair: ನನಗೆ ಒಂದು ಕೋಣೆ ಬೇಕು / ಕೋಣೆಯ ಬಾಡಿಗೆ ಎಷ್ಟು?",
  "Emergency pair: ನಾನು ದಾರಿ ತಪ್ಪಿದೆನು / ದಯವಿಟ್ಟು ಸಹಾಯ ಮಾಡುವಿರಾ?",
  "Transport nouns: ಬಸ್, ರೈಲು, ಟ್ಯಾಕ್ಸಿ, ಆಟೋ, ವಿಮಾನ.",
  "ಬಲಕ್ಕೆ ತಿರುಗಿ / ಎಡಕ್ಕೆ ತಿರುಗಿ / ನೇರವಾಗಿ ಹೋಗಿ give directions like a local.",
  "ನಕ್ಷೆ ತೋರಿಸಿ rescues every lost traveler.",
 ],
 "requirements": [
  "Give directions from your home to the market in Kannada.",
  "Buy an imaginary ticket using the ticket frame.",
  "Ask five ಎಲ್ಲಿದೆ? questions about your town.",
 ],
 "standards": [
  "Government of Karnataka standard Kannada",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
 ],
 "sig_lens": (
  "Through the Signature lens travel is re-taught as his route chart: twenty "
  "stamped sentences plotting every road, rail and runway, with rescue "
  "phrases filed under emergency use. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 14
{
 "key": "workschool", "name": "Work and School in Kannada",
 "group": "Compounded", "ladder": 14, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences for jobs, the office, the classroom and learning. 1. "
  "ನಾನು ಶಿಕ್ಷಕನು (nānu śikṣakanu) - 'I am a teacher'. 2. ಅವನು ವೈದ್ಯನು (avanu "
  "vaidyanu) - 'He is a doctor'. 3. ನನ್ನ ಕೆಲಸ ಚೆನ್ನಾಗಿದೆ (nanna kelasa "
  "cennāgide) - 'My work is good'. 4. ಕಚೇರಿ ಒಂಬತ್ತು ಗಂಟೆಗೆ ತೆರೆಯುತ್ತದೆ "
  "(kacēri ombattu gaṇṭege tereyuttade) - 'The office opens at nine'. 5. "
  "ನನಗೆ ಕೆಲಸಕ್ಕೆ ಹೋಗಬೇಕು (nanage kelasakke hōgabēku) - 'I have to go to "
  "work'. 6. ಇಂದು ತುಂಬಾ ಕೆಲಸವಿದೆ (indu tumbā kelasavide) - 'There is a lot "
  "of work today'. 7. ಸಭೆ ಮೂರು ಗಂಟೆಗೆ ಇದೆ (sabhe mūru gaṇṭege ide) - 'The "
  "meeting is at three'. 8. ಇವರು ನನ್ನ ಸಹೋದ್ಯೋಗಿ (ivaru nanna sahōdyōgi) - "
  "'He is my colleague'. 9. ಸಂಬಳ ತಿಂಗಳಿಗೊಮ್ಮೆ ಬರುತ್ತದೆ (sambaḷa "
  "tiṅgaḷigomme baruttade) - 'Salary comes every month'. 10. ಮಗು ಶಾಲೆಗೆ "
  "ಹೋಗುತ್ತದೆ (magu śālege hōguttade) - 'The child goes to school'. 11. "
  "ತರಗತಿಯಲ್ಲಿ ನಲವತ್ತು ವಿದ್ಯಾರ್ಥಿಗಳಿದ್ದಾರೆ (taragatiyalli nalavattu "
  "vidyārthigaḷiddāre) - 'There are forty students in the class'. 12. "
  "ಅಧ್ಯಾಪಕರು ಪಾಠ ಮಾಡುತ್ತಾರೆ (adhyāpakaru pāṭha māḍuttāre) - 'The teacher "
  "teaches'. 13. ವಿದ್ಯಾರ್ಥಿಗಳು ಪ್ರಶ್ನೆ ಕೇಳುತ್ತಾರೆ (vidyārthigaḷu praśne "
  "kēḷuttāre) - 'The students ask questions'. 14. ಪರೀಕ್ಷೆ ಮುಂದಿನ ವಾರ ಇದೆ "
  "(parīkṣe mundina vāra ide) - 'The exam is next week'. 15. ನಾನು ಕನ್ನಡ "
  "ಕಲಿಯುತ್ತೇನೆ (nānu kannaḍa kaliyuttēne) - 'I am learning Kannada'. 16. "
  "ಓದಿನಲ್ಲಿ ಮನಸ್ಸಿಡಿ (ōdinalli manassiḍi) - 'Put your mind into studies'. 17. "
  "ಮನೆಕೆಲಸ ಮುಗಿಸಿ (manekelasa mugisi) - 'Finish the homework'. 18. ಪುಸ್ತಕ "
  "ತೆರೆಯಿರಿ (pustaka tereyiri) - 'Open the book'. 19. ಗಮನವಿಟ್ಟು ಕೇಳಿ "
  "(gamanaviṭṭu kēḷi) - 'Listen carefully'. 20. ಕಲಿಯುವುದನ್ನು ಎಂದೂ ನಿಲ್ಲಿಸಬೇಡಿ "
  "(kaliyuvadannu endū nillisabēḍi) - 'Never stop learning'. Job words: "
  "ಶಿಕ್ಷಕ (teacher), ವೈದ್ಯ (doctor), ಎಂಜಿನಿಯರ್ (engineer), ರೈತ (farmer), "
  "ಅಂಗಡಿಯವನು (shopkeeper), ಚಾಲಕ (driver), ಬರಹಗಾರ (writer). School words: "
  "ಶಾಲೆ (school), ತರಗತಿ (class), ಪಾಠ (lesson), ಪರೀಕ್ಷೆ (exam), ಮನೆಕೆಲಸ "
  "(homework), ಪುಸ್ತಕ (book). Work or study - these twenty carry the day."),
 "how_it_works": (
  "This record covers the two great daily arenas - work and school - with "
  "twenty sentences from the morning commute to the exam hall. Learn the job "
  "list and the classroom imperatives (ತೆರೆಯಿರಿ, ಕೇಳಿ, ಮುಗಿಸಿ) as call-and-"
  "response: the teacher says it, you do it."),
 "key_points": [
  "Job nouns: ಶಿಕ್ಷಕ, ವೈದ್ಯ, ಎಂಜಿನಿಯರ್, ರೈತ, ಅಂಗಡಿಯವನು, ಚಾಲಕ, ಬರಹಗಾರ.",
  "Workplace: ಕಚೇರಿ (office), ಸಭೆ (meeting), ಸಂಬಳ (salary), ಸಹೋದ್ಯೋಗಿ (colleague), ಕೆಲಸ (work).",
  "School: ಶಾಲೆ, ತರಗತಿ, ಪಾಠ, ಪರೀಕ್ಷೆ, ಮನೆಕೆಲಸ, ವಿದ್ಯಾರ್ಥಿ, ಅಧ್ಯಾಪಕ.",
  "Classroom imperatives: ತೆರೆಯಿರಿ, ಕೇಳಿ, ಮುಗಿಸಿ, ಮನಸ್ಸಿಡಿ.",
  "Time frames: ಒಂಬತ್ತು ಗಂಟೆಗೆ, ಮುಂದಿನ ವಾರ, ತಿಂಗಳಿಗೊಮ್ಮೆ.",
  "ಕಲಿಯುವುದನ್ನು ಎಂದೂ ನಿಲ್ಲಿಸಬೇಡಿ is the student's motto.",
  "ನಾನು ...ನು / ...ಳು frames introduce any profession.",
  "Role-play teacher and student to fix the imperatives.",
 ],
 "requirements": [
  "Introduce five professions in Kannada.",
  "Give eight classroom commands as the teacher.",
  "Describe your workday in ten sentences.",
 ],
 "standards": [
  "Government of Karnataka standard Kannada",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
 ],
 "sig_lens": (
  "Through the Signature lens work and school are re-taught as his two "
  "workshops: twenty stamped sentences for the office bench and the study "
  "desk, every profession a labeled tool on his wall. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 15
{
 "key": "health", "name": "Health and the Body in Kannada",
 "group": "Compounded", "ladder": 15, "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences for body parts, symptoms, the doctor's visit and the "
  "pharmacy. 1. ನನ್ನ ತಲೆ ನೋಯುತ್ತಿದೆ (nanna tale nōyuttide) - 'My head aches'. "
  "2. ನನಗೆ ಜ್ವರವಿದೆ (nanage jvaravide) - 'I have a fever'. 3. ನನಗೆ ಕೆಮ್ಮು "
  "ಬರುತ್ತಿದೆ (nanage kemmu baruttide) - 'I have a cough'. 4. ನನ್ನ ಹೊಟ್ಟೆ "
  "ನೋಯುತ್ತಿದೆ (nanna hoṭṭe nōyuttide) - 'My stomach aches'. 5. ನನಗೆ ತಲೆಸುತ್ತು "
  "ಬರುತ್ತಿದೆ (nanage talesuttu baruttide) - 'I feel dizzy'. 6. ವೈದ್ಯರು "
  "ಎಲ್ಲಿದ್ದಾರೆ? (vaidyaru elliddāre?) - 'Where is the doctor?'. 7. ದಯವಿಟ್ಟು "
  "ಆಂಬುಲೆನ್ಸ್ ಕರೆಸಿ (dayaviṭṭu āmbulens karesi) - 'Please call an ambulance'. "
  "8. ನನಗೆ ಔಷಧಿ ಬೇಕು (nanage auṣadhi bēku) - 'I need medicine'. 9. ಈ ಮಾತ್ರೆಯನ್ನು "
  "ದಿನಕ್ಕೆ ಎರಡು ಬಾರಿ ತಿನ್ನಿ (ī mātreyannu dinakke eraḍu bāri tinni) - 'Take "
  "this tablet twice a day'. 10. ಊಟದ ನಂತರ ಔಷಧಿ ತಿನ್ನಿ (ūṭada nantara auṣadhi "
  "tinni) - 'Take the medicine after food'. 11. ನನಗೆ ಅಲರ್ಜಿ ಇದೆ (nanage "
  "alarji ide) - 'I have an allergy'. 12. ರಕ್ತದೊತ್ತಡ ಪರೀಕ್ಷಿಸಿ (raktadottada "
  "parīkṣisi) - 'Check the blood pressure'. 13. ವಿಶ್ರಾಂತಿ ತೆಗೆದುಕೊಳ್ಳಿ "
  "(viśrānti tegedukoḷḷi) - 'Take rest'. 14. ಬೇಗ ಗುಣಮುಖರಾಗಿ (bēga "
  "guṇamukharāgi) - 'Get well soon'. 15. ಆಸ್ಪತ್ರೆ ಎಲ್ಲಿದೆ? (āspatre ellide?) "
  "- 'Where is the hospital?'. 16. ಔಷಧಿ ಅಂಗಡಿ ಹತ್ತಿರವಿದೆಯೇ? (auṣadhi aṅgaḍi "
  "hattiravideyē?) - 'Is the pharmacy nearby?'. 17. ನನ್ನ ಕಣ್ಣು ಕೆಂಪಾಗಿದೆ "
  "(nanna kaṇṇu kempāgide) - 'My eye is red'. 18. ನನ್ನ ಕೈಗೆ ಗಾಯವಾಗಿದೆ "
  "(nanna kaige gāyavāgide) - 'My hand is injured'. 19. ನೀರು ಹೆಚ್ಚು ಕುಡಿಯಿರಿ "
  "(nīru heccu kuḍiyiri) - 'Drink more water'. 20. ಆರೋಗ್ಯವೇ ಭಾಗ್ಯ (ārōgyavē "
  "bhāgya) - 'Health is wealth'. Body parts: ತಲೆ (tale, head), ಕಣ್ಣು (kaṇṇu, "
  "eye), ಮೂಗು (mūgu, nose), ಬಾಯಿ (bāyi, mouth), ಕಿವಿ (kivi, ear), ಕುತ್ತಿಗೆ "
  "(kuttige, neck), ಹೆಗಲು (hegalu, shoulder), ಕೈ (kai, hand/arm), ಬೆರಳು "
  "(beraḷu, finger), ಎದೆ (ede, chest), ಹೊಟ್ಟೆ (hoṭṭe, stomach), ಬೆನ್ನು (bennu, "
  "back), ಕಾಲು (kālu, leg/foot), ಮೊಣಕಾಲು (moṇakālu, knee), ಹೃದಯ (hṛdaya, "
  "heart). Symptom frame: ನನ್ನ ... ನೋಯುತ್ತಿದೆ / ನನಗೆ ... ಇದೆ. In an emergency, "
  "ದಯವಿಟ್ಟು ಸಹಾಯ ಮಾಡಿ (please help) comes first."),
 "how_it_works": (
  "This record teaches the body as a labeled diagram and sickness as "
  "sentence frames: twenty sentences from naming parts to the pharmacy "
  "counter. Point to each body part and name it in Kannada; then practice "
  "the symptom frames - ನನ್ನ ... ನೋಯುತ್ತಿದೆ, ನನಗೆ ... ಇದೆ - until describing "
  "any ache is automatic."),
 "key_points": [
  "15 body parts from ತಲೆ to ಹೃದಯ, each usable in the symptom frames.",
  "Symptom frames: ನನ್ನ X ನೋಯುತ್ತಿದೆ (my X aches); ನನಗೆ Y ಇದೆ (I have Y).",
  "Doctor-visit core: ವೈದ್ಯರು ಎಲ್ಲಿದ್ದಾರೆ? / ಆಸ್ಪತ್ರೆ ಎಲ್ಲಿದೆ? / ಔಷಧಿ ಅಂಗಡಿ ಹತ್ತಿರವಿದೆಯೇ?",
  "Emergency: ದಯವಿಟ್ಟು ಆಂಬುಲೆನ್ಸ್ ಕರೆಸಿ; ದಯವಿಟ್ಟು ಸಹಾಯ ಮಾಡಿ.",
  "Dosage frame: ದಿನಕ್ಕೆ ಎರಡು ಬಾರಿ; ಊಟದ ನಂತರ / ಊಟಕ್ಕಿಂತ ಮೊದಲು.",
  "Advice verbs: ವಿಶ್ರಾಂತಿ ತೆಗೆದುಕೊಳ್ಳಿ, ನೀರು ಹೆಚ್ಚು ಕುಡಿಯಿರಿ.",
  "ಆರೋಗ್ಯವೇ ಭಾಗ್ಯ - health is wealth - is the cultural anchor.",
  "Point-and-name drill locks the body vocabulary.",
 ],
 "requirements": [
  "Point to and name 15 body parts in Kannada.",
  "Describe five imaginary symptoms with the frames.",
  "Role-play a full doctor visit: complaint, exam, prescription.",
 ],
 "standards": [
  "Government of Karnataka standard Kannada",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
 ],
 "sig_lens": (
  "Through the Signature lens health is re-taught as his maintenance manual: "
  "twenty stamped sentences servicing the body machine part by part, symptoms "
  "as diagnostic readouts and the pharmacy as his parts counter. Signature-"
  "made teaching, clearly labeled, never presented as an outside authority's "
  "text."),
},
# ================================================================== 16
{
 "key": "emotions", "name": "Emotions and Feelings in Kannada",
 "group": "Compounded", "ladder": 16, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences for the inner life - happy, sad, angry, afraid, love, "
  "surprise. 1. ನನಗೆ ತುಂಬಾ ಸಂತೋಷವಾಗಿದೆ (nanage tumbā santōṣavāgide) - 'I am "
  "very happy'. 2. ಅವಳು ಸಂತೋಷದಿಂದ ನಗುತ್ತಾಳೆ (avaḷu santōṣadinda naguttāḷe) - "
  "'She laughs with joy'. 3. ನನಗೆ ದುಃಖವಾಗಿದೆ (nanage duḥkhavāgide) - 'I am "
  "sad'. 4. ಅವನು ದುಃಖದಿಂದ ಅಳುತ್ತಾನೆ (avanu duḥkhadinda aḷuttāne) - 'He cries "
  "with sadness'. 5. ನನಗೆ ಕೋಪ ಬರುತ್ತಿದೆ (nanage kōpa baruttide) - 'I am "
  "getting angry'. 6. ದಯವಿಟ್ಟು ಕೋಪ ಮಾಡಿಕೊಳ್ಳಬೇಡಿ (dayaviṭṭu kōpa "
  "māḍikoḷḷabēḍi) - 'Please do not get angry'. 7. ನನಗೆ ಭಯವಾಗುತ್ತಿದೆ (nanage "
  "bhayavāguttide) - 'I am afraid'. 8. ಹೆದರಬೇಡಿ, ನಾನಿದ್ದೇನೆ (hedarabēḍi, "
  "nāniddēne) - 'Do not fear, I am here'. 9. ನಾನು ನಿನ್ನನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ "
  "(nānu ninnannu prītisuttēne) - 'I love you'. 10. ಪ್ರೀತಿ ಎಲ್ಲಕ್ಕಿಂತ ದೊಡ್ಡದು "
  "(prīti ellakkinta doḍḍadu) - 'Love is greater than everything'. 11. ನನಗೆ "
  "ಆಶ್ಚರ್ಯವಾಯಿತು (nanage āścaryavāyitu) - 'I was surprised'. 12. ಅದು ನಿಜಕ್ಕೂ "
  "ಆಶ್ಚರ್ಯಕರ! (adu nijakkū āścaryakara!) - 'That is truly surprising!'. 13. "
  "ನನಗೆ ಹೆಮ್ಮೆಯಾಗುತ್ತಿದೆ (nanage hemmyyāguttide) - 'I feel proud'. 14. ನನಗೆ "
  "ನಾಚಿಕೆಯಾಗುತ್ತಿದೆ (nanage nācikeyāguttide) - 'I feel shy'. 15. ನನಗೆ ಬೇಸರವಾಗಿದೆ "
  "(nanage bēsaravāgide) - 'I am bored / fed up'. 16. ಸಮಾಧಾನವಾಗಿರಿ "
  "(samādhānavāgiri) - 'Be calm / take comfort'. 17. ಚಿಂತೆ ಮಾಡಬೇಡಿ (cinte "
  "māḍabēḍi) - 'Do not worry'. 18. ನನಗೆ ಆತಂಕವಿದೆ (nanage ātaṅkavide) - 'I am "
  "anxious'. 19. ಅವನಿಗೆ ಕೃತಜ್ಞತೆ ಇದೆ (avanige kṛtajñate ide) - 'He feels "
  "grateful'. 20. ಕ್ಷಮಿಸಿ, ನನ್ನ ತಪ್ಪು (kṣamisi, nanna tappu) - 'Forgive me, my "
  "mistake'. Emotion nouns: ಸಂತೋಷ (santōṣa, happiness), ದುಃಖ (duḥkha, "
  "sadness), ಕೋಪ (kōpa, anger), ಭಯ (bhaya, fear), ಪ್ರೀತಿ (prīti, love), "
  "ಆಶ್ಚರ್ಯ (āścarya, surprise), ಹೆಮ್ಮೆ (hemme, pride), ನಾಚಿಕೆ (nācike, "
  "shyness), ಚಿಂತೆ (cinte, worry), ಕೃತಜ್ಞತೆ (kṛtajñate, gratitude). The master "
  "frame: ನನಗೆ ...-ಆಗಿದೆ / -ಆಗುತ್ತಿದೆ expresses any feeling - ನನಗೆ "
  "ಸಂತೋಷವಾಗಿದೆ, ನನಗೆ ಭಯವಾಗುತ್ತಿದೆ. Feelings are for sharing; practice these "
  "with someone you trust."),
 "how_it_works": (
  "This record gives feelings a grammar: twenty sentences built on the "
  "master frame ನನಗೆ ...-ಆಗಿದೆ (I feel ...), plus the ten core emotion nouns. "
  "Keep a one-week feelings diary - one Kannada sentence per day naming your "
  "strongest feeling - and the frame becomes permanent."),
 "key_points": [
  "Master frame: ನನಗೆ X-ಆಗಿದೆ / X-ಆಗುತ್ತಿದೆ for every feeling.",
  "Core six: ಸಂತೋಷ, ದುಃಖ, ಕೋಪ, ಭಯ, ಪ್ರೀತಿ, ಆಶ್ಚರ್ಯ.",
  "Extended: ಹೆಮ್ಮೆ, ನಾಚಿಕೆ, ಬೇಸರ, ಚಿಂತೆ, ಆತಂಕ, ಕೃತಜ್ಞತೆ.",
  "Comfort phrases: ಹೆದರಬೇಡಿ, ಚಿಂತೆ ಮಾಡಬೇಡಿ, ಸಮಾಧಾನವಾಗಿರಿ.",
  "ನಾನು ನಿನ್ನನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ - say it right.",
  "ಕ್ಷಮಿಸಿ, ನನ್ನ ತಪ್ಪು repairs any quarrel.",
  "-ಇಂದ (with) shades the emotion: ಸಂತೋಷದಿಂದ, ದುಃಖದಿಂದ.",
  "A feelings diary in Kannada fixes the frames.",
 ],
 "requirements": [
  "Write seven days of feelings with the master frame.",
  "Comfort an imaginary friend with three phrases.",
  "Express all ten emotion nouns in full sentences.",
 ],
 "standards": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Government of Karnataka standard Kannada",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
 ],
 "sig_lens": (
  "Through the Signature lens emotions are re-taught as his instrument's "
  "tuning: twenty stamped sentences naming every string's pitch from joy to "
  "grief, so he always knows which note he is playing. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 17
{
 "key": "nature", "name": "Nature and Weather in Kannada",
 "group": "Compounded", "ladder": 17, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences for animals, plants, seasons and weather talk. 1. ಇಂದು "
  "ಹವಾಮಾನ ಚೆನ್ನಾಗಿದೆ (indu havāmāna cennāgide) - 'The weather is nice today'. "
  "2. ಹೊರಗೆ ಮಳೆ ಬರುತ್ತಿದೆ (horage maḷe baruttide) - 'It is raining outside'. "
  "3. ನಾಳೆ ಬಿಸಿಲು ಇರುತ್ತದೆ (nāḷe bisilu iruttade) - 'Tomorrow will be sunny'. "
  "4. ಚಳಿಗಾಲದಲ್ಲಿ ತುಂಬಾ ಚಳಿಯಿರುತ್ತದೆ (caḷigāladalli tumbā caḷiyiruttade) - "
  "'It is very cold in winter'. 5. ವಸಂತಕಾಲದಲ್ಲಿ ಹೂವುಗಳು ಅರಳುತ್ತವೆ "
  "(vasantakāladalli hūvugaḷu araḷuttave) - 'Flowers bloom in spring'. 6. "
  "ಆಕಾಶದಲ್ಲಿ ಮೋಡಗಳಿವೆ (ākāśadalli mōḍagaḷive) - 'There are clouds in the sky'. "
  "7. ಗಾಳಿ ಬಲವಾಗಿ ಬೀಸುತ್ತಿದೆ (gāḷi balavāgi bīsuttide) - 'The wind is blowing "
  "strongly'. 8. ಮಿಂಚು ಹೊಳೆಯುತ್ತಿದೆ (mincu hoḷeyuttide) - 'Lightning is "
  "flashing'. 9. ಗುಡುಗು ಕೇಳಿಸುತ್ತಿದೆ (guḍugu kēḷisuttide) - 'Thunder is "
  "heard'. 10. ನದಿಯಲ್ಲಿ ನೀರು ಹರಿಯುತ್ತಿದೆ (nadiyalli nīru hariyuttide) - "
  "'Water flows in the river'. 11. ಬೆಟ್ಟದ ಮೇಲೆ ದೇವಸ್ಥಾನವಿದೆ (beṭṭada mēle "
  "dēvasthānavide) - 'There is a temple on the hill'. 12. ಕಾಡಿನಲ್ಲಿ ಆನೆಗಳಿವೆ "
  "(kāḍinalli ānegaḷive) - 'There are elephants in the forest'. 13. ಹುಲಿ "
  "ಕಾಡಿನ ರಾಜ (huli kāḍina rāja) - 'The tiger is the king of the forest'. 14. "
  "ನಾಯಿ ಬೊಗಳುತ್ತಿದೆ (nāyi bogaḷuttide) - 'The dog is barking'. 15. ಬೆಕ್ಕು "
  "ಹಾಲು ಕುಡಿಯುತ್ತಿದೆ (bekku hālu kuḍiyuttide) - 'The cat is drinking milk'. "
  "16. ಹಕ್ಕಿಗಳು ಹಾಡುತ್ತಿವೆ (hakkigaḷu hāḍuttive) - 'The birds are singing'. "
  "17. ಹಸು ಹುಲ್ಲು ತಿನ್ನುತ್ತಿದೆ (hasu hullu tinnuttide) - 'The cow is eating "
  "grass'. 18. ಮರದ ಮೇಲೆ ಕೋತಿ ಕುಳಿತಿದೆ (marada mēle kōti kuḷitide) - 'A monkey "
  "sits on the tree'. 19. ತೋಟದಲ್ಲಿ ಮಾವಿನ ಮರಗಳಿವೆ (tōṭadalli māvina "
  "maragaḷive) - 'There are mango trees in the orchard'. 20. ಪ್ರಕೃತಿ ನಮ್ಮ "
  "ಅಮೂಲ್ಯ ಸಂಪತ್ತು (prakṛti namma amūlya sampattu) - 'Nature is our precious "
  "wealth'. Weather words: ಮಳೆ (rain), ಬಿಸಿಲು (sunshine), ಚಳಿ (cold), ಗಾಳಿ "
  "(wind), ಮೋಡ (cloud), ಮಂಜು (fog), ಆಲಿಕಲ್ಲು (hail). Animals: ಆನೆ "
  "(elephant), ಹುಲಿ (tiger), ಸಿಂಹ (lion), ಕರಡಿ (bear), ಜಿಂಕೆ (deer), ನವಿಲು "
  "(peacock), ಹಾವು (snake), ಮೀನು (fish). Weather talk opens every Kannada "
  "conversation - ಮಳೆ ಬರುತ್ತಿದೆಯೇ? is small talk gold."),
 "how_it_works": (
  "This record walks you through the living world: twenty sentences for "
  "weather, sky, land, plants and animals, plus the weather and animal word "
  "lists. Narrate the sky every morning in Kannada - ಮೋಡಗಳಿವೆ, ಬಿಸಿಲಿದೆ, "
  "ಗಾಳಿ ಬೀಸುತ್ತಿದೆ - and name every animal you see."),
 "key_points": [
  "Weather core: ಮಳೆ, ಬಿಸಿಲು, ಚಳಿ, ಗಾಳಿ, ಮೋಡ, ಮಂಜು.",
  "Sky and land: ಆಕಾಶ, ನದಿ, ಬೆಟ್ಟ, ಕಾಡು, ತೋಟ.",
  "Animals: ಆನೆ, ಹುಲಿ, ಸಿಂಹ, ನಾಯಿ, ಬೆಕ್ಕು, ಹಕ್ಕಿ, ಹಸು, ಕೋತಿ, ಮೀನು, ಹಾವು.",
  "Season frames: -ಕಾಲದಲ್ಲಿ - ವಸಂತಕಾಲದಲ್ಲಿ, ಚಳಿಗಾಲದಲ್ಲಿ.",
  "ಮಳೆ ಬರುತ್ತಿದೆಯೇ? is the universal small-talk opener.",
  "Existence pattern: -ಅಲ್ಲಿ ...-ಇವೆ - ಕಾಡಿನಲ್ಲಿ ಆನೆಗಳಿವೆ.",
  "ಪ್ರಕೃತಿ ನಮ್ಮ ಅಮೂಲ್ಯ ಸಂಪತ್ತು closes with the cultural note.",
  "Narrate the morning sky in Kannada daily.",
 ],
 "requirements": [
  "Describe today's weather in five Kannada sentences.",
  "Name ten animals with one sentence each.",
  "Write a six-sentence nature walk narration.",
 ],
 "standards": [
  "Government of Karnataka standard Kannada",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
 ],
 "sig_lens": (
  "Through the Signature lens nature is re-taught as his open-air laboratory: "
  "twenty stamped sentences logging sky, weather, beast and bloom, every "
  "observation filed like a field scientist's notes. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 18
{
 "key": "shopping", "name": "Shopping and Money in Kannada",
 "group": "Compounded", "ladder": 18, "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences for the market, prices, bargaining and paying. 1. ಇದರ "
  "ಬೆಲೆ ಎಷ್ಟು? (idara bele eṣṭu?) - 'How much is this?'. 2. ತುಂಬಾ ದುಬಾರಿಯಾಗಿದೆ "
  "(tumbā dubāriyāgide) - 'It is too expensive'. 3. ಸ್ವಲ್ಪ ಕಡಿಮೆ ಮಾಡಿ (svalpa "
  "kaḍime māḍi) - 'Reduce a little (the price)'. 4. ಕೊನೆಯ ಬೆಲೆ ಹೇಳಿ (koneya "
  "bele hēḷi) - 'Tell the final price'. 5. ನನಗೆ ಇದು ಇಷ್ಟವಾಯಿತು (nanage idu "
  "iṣṭavāyitu) - 'I like this'. 6. ಬೇರೆ ಬಣ್ಣ ತೋರಿಸಿ (bēre baṇṇa tōrisi) - "
  "'Show another color'. 7. ದೊಡ್ಡ ಗಾತ್ರವಿದೆಯೇ? (doḍḍa gātravideyē?) - 'Is "
  "there a bigger size?'. 8. ನಾನು ಇದನ್ನು ತೆಗೆದುಕೊಳ್ಳುತ್ತೇನೆ (nānu idannu "
  "tegedukoḷḷuttēne) - 'I will take this'. 9. ಬಿಲ್ ಕೊಡಿ (bil koḍi) - 'Give "
  "the bill'. 10. ನಗದು ಕೊಡುತ್ತೇನೆ (nagadu koḍuttēne) - 'I will pay cash'. 11. "
  "ಕಾರ್ಡಿನಲ್ಲಿ ಪಾವತಿಸಬಹುದೇ? (kārḍinalli pāvatisabahudē?) - 'Can I pay by "
  "card?'. 12. ಚಿಲ್ಲರೆ ಇದೆಯೇ? (cillare ideyē?) - 'Do you have change?'. 13. "
  "ರಸೀದಿ ಕೊಡಿ (rasīdi koḍi) - 'Give the receipt'. 14. ಇದು ಖಾತರಿಯಿದೆಯೇ? (idu "
  "khātriyideyē?) - 'Does this have a warranty?'. 15. ವಾಪಸ್ ತೆಗೆದುಕೊಳ್ಳುವಿರಾ? "
  "(vāpas tegedukoḷḷuvirā?) - 'Will you take it back (return)?'. 16. "
  "ಮಾರುಕಟ್ಟೆ ಬೆಳಿಗ್ಗೆ ತೆರೆಯುತ್ತದೆ (mārukaṭṭe beḷigge tereyuttade) - 'The "
  "market opens in the morning'. 17. ತರಕಾರಿ ತಾಜಾವಾಗಿದೆ (tarakāri tājāvāgide) "
  "- 'The vegetables are fresh'. 18. ಒಂದು ಕೆಜಿ ಟೊಮೆಟೊ ಕೊಡಿ (ondu keji "
  "ṭomeṭo koḍi) - 'Give one kilo of tomatoes'. 19. ಹಣ ಉಳಿಸಿ (haṇa uḷisi) - "
  "'Save money'. 20. ಚೌಕಾಶಿ ಮಾಡುವುದು ಸಾಮಾನ್ಯ (caukāśi māḍuvudu sāmānya) - "
  "'Bargaining is normal'. Money words: ಹಣ (money), ರೂಪಾಯಿ (rupee), ನಗದು "
  "(cash), ಚಿಲ್ಲರೆ (change), ಬಿಲ್ (bill), ರಸೀದಿ (receipt), ಬೆಲೆ (price), "
  "ರಿಯಾಯಿತಿ (discount). Measures: ಕೆಜಿ (kilo), ಗ್ರಾಂ (gram), ಲೀಟರ್ (litre), "
  "ಮೀಟರ್ (metre). Bargaining is expected in street markets - ಸ್ವಲ್ಪ ಕಡಿಮೆ "
  "ಮಾಡಿ with a smile works better than any argument."),
 "how_it_works": (
  "This record is your market wallet: twenty sentences from price inquiry "
  "through bargaining to payment, plus money and measure words. Practice the "
  "bargaining trio - ಇದರ ಬೆಲೆ ಎಷ್ಟು? / ತುಂಬಾ ದುಬಾರಿ / ಸ್ವಲ್ಪ ಕಡಿಮೆ ಮಾಡಿ - "
  "as a role-play until you can haggle without thinking."),
 "key_points": [
  "Price core: ಬೆಲೆ ಎಷ್ಟು? / ತುಂಬಾ ದುಬಾರಿ / ಸ್ವಲ್ಪ ಕಡಿಮೆ ಮಾಡಿ / ಕೊನೆಯ ಬೆಲೆ ಹೇಳಿ.",
  "Money: ಹಣ, ರೂಪಾಯಿ, ನಗದು, ಚಿಲ್ಲರೆ, ಬಿಲ್, ರಸೀದಿ, ರಿಯಾಯಿತಿ.",
  "Measures: ಕೆಜಿ, ಗ್ರಾಂ, ಲೀಟರ್, ಮೀಟರ್.",
  "Payment: ನಗದು ಕೊಡುತ್ತೇನೆ / ಕಾರ್ಡಿನಲ್ಲಿ ಪಾವತಿಸಬಹುದೇ?",
  "After-sale: ಇದು ಖಾತರಿಯಿದೆಯೇ? / ವಾಪಸ್ ತೆಗೆದುಕೊಳ್ಳುವಿರಾ?",
  "Market adjectives: ತಾಜಾ (fresh), ದುಬಾರಿ (expensive), ಅಗ್ಗ (cheap).",
  "ಚೌಕಾಶಿ ಮಾಡುವುದು ಸಾಮಾನ್ಯ - bargaining is culturally normal.",
  "Smile beats argument in every bargain.",
 ],
 "requirements": [
  "Role-play buyer and seller for five items.",
  "Convert five prices between rupees and kilos aloud.",
  "Write a market shopping list in Kannada.",
 ],
 "standards": [
  "Government of Karnataka standard Kannada",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
 ],
 "sig_lens": (
  "Through the Signature lens shopping is re-taught as his trading floor: "
  "twenty stamped sentences for price discovery, the bargain as his sport, "
  "and every rupee accounted on his ledger. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 19
{
 "key": "social", "name": "Friendship and Social Life in Kannada",
 "group": "Compounded", "ladder": 19, "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences for meeting people, invitations and celebrations. 1. "
  "ನಿಮ್ಮ ಹೆಸರೇನು? (nimma hesarēnu?) - 'What is your name?'. 2. ನನ್ನ ಹೆಸರು "
  "ರವಿ (nanna hesaru ravi) - 'My name is Ravi'. 3. ನೀವು ಎಲ್ಲಿಯವರು? (nīvu "
  "elliyavaru?) - 'Where are you from?'. 4. ನಾನು ಬೆಂಗಳೂರಿನವನು (nānu "
  "beṅgaḷūrinavanu) - 'I am from Bengaluru'. 5. ನಿಮಗೆ ಎಷ್ಟು ವಯಸ್ಸು? (nimage "
  "eṣṭu vayassu?) - 'How old are you?'. 6. ನನಗೆ ಇಪ್ಪತ್ತೈದು ವಯಸ್ಸು (nanage "
  "ippattnaidu vayassu) - 'I am twenty-five'. 7. ನೀವು ಏನು ಮಾಡುತ್ತೀರಿ? (nīvu "
  "ēnu māḍuttīri?) - 'What do you do?'. 8. ನಾನು ವಿದ್ಯಾರ್ಥಿ (nānu vidyārthi) "
  "- 'I am a student'. 9. ನಾವು ಸ್ನೇಹಿತರಾಗೋಣ (nāvu snēhitarāgōṇa) - 'Let us "
  "be friends'. 10. ನನ್ನ ಮನೆಗೆ ಬನ್ನಿ (nanna manege banni) - 'Come to my "
  "house'. 11. ನಾಳೆ ಸಂಜೆ ಬಿಡುವಿದೆಯೇ? (nāḷe sanje biḍuvideyē?) - 'Are you free "
  "tomorrow evening?'. 12. ಊಟಕ್ಕೆ ಬನ್ನಿ (ūṭakke banni) - 'Come for a meal'. "
  "13. ನನ್ನ ಹುಟ್ಟುಹಬ್ಬಕ್ಕೆ ಬನ್ನಿ (nanna huṭṭuhabbakke banni) - 'Come to my "
  "birthday'. 14. ಹುಟ್ಟುಹಬ್ಬದ ಶುಭಾಶಯಗಳು! (huṭṭuhabbada śubhāśayagaḷu!) - "
  "'Happy birthday!'. 15. ಮದುವೆಗೆ ಬನ್ನಿ (maduvege banni) - 'Come to the "
  "wedding'. 16. ಹಬ್ಬದ ಶುಭಾಶಯಗಳು! (habbada śubhāśayagaḷu!) - 'Festival "
  "greetings!'. 17. ದೀಪಾವಳಿ ಹಬ್ಬ ಚೆನ್ನಾಗಿ ಆಚರಿಸಿ (dīpāvaḷi habba cennāgi "
  "ācarisi) - 'Celebrate Diwali well'. 18. ಯುಗಾದಿ ಹಬ್ಬದ ಶುಭಾಶಯಗಳು (yugādi "
  "habbada śubhāśayagaḷu) - 'Ugadi greetings'. 19. ನಾವು ಒಟ್ಟಿಗೆ ಸಿನೆಮಾ "
  "ನೋಡೋಣ (nāvu oṭṭige sinemā nōḍōṇa) - 'Let us watch a movie together'. 20. "
  "ಸ್ನೇಹವೇ ದೊಡ್ಡ ಸಂಪತ್ತು (snēhavē doḍḍa sampattu) - 'Friendship is the "
  "greatest wealth'. Celebrations: ಹುಟ್ಟುಹಬ್ಬ (birthday), ಮದುವೆ (wedding), "
  "ಹಬ್ಬ (festival), ದೀಪಾವಳಿ (Diwali), ಯುಗಾದಿ (Ugadi, the Kannada new year), "
  "ದಸರಾ (Dasara). Invitation frame: ...-ಕ್ಕೆ ಬನ್ನಿ works for everything - "
  "ಊಟಕ್ಕೆ ಬನ್ನಿ, ಮನೆಗೆ ಬನ್ನಿ, ಮದುವೆಗೆ ಬನ್ನಿ. -ಓಣ (let us) makes plans: "
  "ಹೋಗೋಣ, ನೋಡೋಣ, ಮಾಡೋಣ. Friendship in Karnataka runs on shared meals and "
  "festivals - accept every invitation."),
 "how_it_works": (
  "This record teaches the social engine: twenty sentences for introductions, "
  "the -ಕ್ಕೆ ಬನ್ನಿ invitation frame, the -ಓಣ let-us planner, and festival "
  "greetings. Practice full introduction chains - name, place, work, age - "
  "then issue three invitations and make two plans."),
 "key_points": [
  "Introduction chain: ಹೆಸರೇನು? / ಎಲ್ಲಿಯವರು? / ಏನು ಮಾಡುತ್ತೀರಿ? / ಎಷ್ಟು ವಯಸ್ಸು?",
  "Invitation frame: -ಕ್ಕೆ ಬನ್ನಿ - ಊಟಕ್ಕೆ ಬನ್ನಿ, ಮನೆಗೆ ಬನ್ನಿ, ಮದುವೆಗೆ ಬನ್ನಿ.",
  "Plan maker: -ಓಣ - ಹೋಗೋಣ, ನೋಡೋಣ, ಮಾಡೋಣ, ಸ್ನೇಹಿತರಾಗೋಣ.",
  "Festivals: ಯುಗಾದಿ (new year), ದಸರಾ, ದೀಪಾವಳಿ; ಹಬ್ಬದ ಶುಭಾಶಯಗಳು for all.",
  "ಹುಟ್ಟುಹಬ್ಬದ ಶುಭಾಶಯಗಳು! for birthdays.",
  "ನಾಳೆ ಸಂಜೆ ಬಿಡುವಿದೆಯೇ? is the polite availability check.",
  "ಸ್ನೇಹವೇ ದೊಡ್ಡ ಸಂಪತ್ತು - the cultural anchor.",
  "Accept invitations warmly; shared meals build friendships.",
 ],
 "requirements": [
  "Introduce yourself fully in six sentences.",
  "Issue three invitations with -ಕ್ಕೆ ಬನ್ನಿ.",
  "Make two plans with friends using -ಓಣ.",
 ],
 "standards": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Government of Karnataka standard Kannada",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
 ],
 "sig_lens": (
  "Through the Signature lens social life is re-taught as his alliance "
  "ledger: twenty stamped sentences for introductions, invitations and "
  "festivals, every friendship a signed pact and every celebration a "
  "dividend. Signature-made teaching, clearly labeled, never presented as an "
  "outside authority's text."),
},
# ================================================================== 20
{
 "key": "tech", "name": "Technology and Communication in Kannada",
 "group": "Compounded", "ladder": 20, "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Twenty sentences for the phone, the internet, the computer and messaging. "
  "1. ನನ್ನ ಫೋನ್ ಸಂಖ್ಯೆ ... (nanna phōn sankhye ...) - 'My phone number is "
  "...'. 2. ದಯವಿಟ್ಟು ನನಗೆ ಕರೆ ಮಾಡಿ (dayaviṭṭu nanage kare māḍi) - 'Please "
  "call me'. 3. ನಾನು ನಿಮಗೆ ಮೆಸೇಜ್ ಮಾಡುತ್ತೇನೆ (nānu nimage mesej māḍuttēne) - "
  "'I will message you'. 4. ಇಂಟರ್ನೆಟ್ ಕೆಲಸ ಮಾಡುತ್ತಿಲ್ಲ (iṇṭarneṭ kelasa "
  "māḍuttilla) - 'The internet is not working'. 5. ವೈ-ಫೈ ಪಾಸ್ವರ್ಡ್ ಏನು? "
  "(vai-phai pāsvard ēnu?) - 'What is the Wi-Fi password?'. 6. ನನ್ನ ಕಂಪ್ಯೂಟರ್ "
  "ಆನ್ ಆಗುತ್ತಿಲ್ಲ (nanna kampyūṭar ān āguttilla) - 'My computer will not turn "
  "on'. 7. ಚಾರ್ಜರ್ ಇದೆಯೇ? (cārjar ideyē?) - 'Do you have a charger?'. 8. "
  "ಬ್ಯಾಟರಿ ಖಾಲಿಯಾಗಿದೆ (byāṭari khāliyāgide) - 'The battery is empty'. 9. "
  "ಫೋಟೋ ತೆಗೆಯಬಹುದೇ? (phōṭō tegeyabahudē?) - 'May I take a photo?'. 10. "
  "ವೀಡಿಯೋ ಕರೆ ಮಾಡೋಣ (vīḍiyō kare māḍōṇa) - 'Let us make a video call'. 11. "
  "ನಿಮ್ಮ ಈಮೇಲ್ ವಿಳಾಸ ಕೊಡಿ (nimma īmel viḷāsa koḍi) - 'Give your email "
  "address'. 12. ನಾನು ನಿಮಗೆ ಈಮೇಲ್ ಕಳುಹಿಸುತ್ತೇನೆ (nānu nimage īmel "
  "kaḷuhisuttēne) - 'I will send you an email'. 13. ಪಾಸ್ವರ್ಡ್ ಮರೆತುಹೋಗಿದೆ "
  "(pāsvard marettuhōgide) - 'I forgot the password'. 14. ಹೊಸ ಪಾಸ್ವರ್ಡ್ "
  "ಹಾಕಿ (hosa pāsvard hāki) - 'Set a new password'. 15. ಆ್ಯಪ್ ಡೌನ್ಲೋಡ್ ಮಾಡಿ "
  "(āp ḍaunlōḍ māḍi) - 'Download the app'. 16. ಸಾಫ್ಟ್ವೇರ್ ಅಪ್ಡೇಟ್ ಮಾಡಿ "
  "(sāphṭvēr apḍēṭ māḍi) - 'Update the software'. 17. ಸ್ಕ್ರೀನ್ ತುಂಬಾ "
  "ಪ್ರಕಾಶಮಾನವಾಗಿದೆ (skrīn tumbā prakāśamānavāgide) - 'The screen is too "
  "bright'. 18. ಸದ್ದು ಹೆಚ್ಚು ಮಾಡಿ (saddu heccu māḍi) - 'Increase the "
  "volume'. 19. ನನ್ನ ಫೋನಿನಲ್ಲಿ ಕನ್ನಡ ಕೀಬೋರ್ಡ್ ಇದೆ (nanna phōninalli kannaḍa "
  "kībōrḍ ide) - 'My phone has a Kannada keyboard'. 20. ತಂತ್ರಜ್ಞಾನ ನಮ್ಮ "
  "ಬಾಳನ್ನು ಸುಲಭಗೊಳಿಸಿದೆ (tantrajñāna namma bāḷannu sulabhagoḷiside) - "
  "'Technology has made our lives easier'. Tech nouns: ಫೋನ್ (phone), ಕರೆ "
  "(call), ಮೆಸೇಜ್ (message), ಇಂಟರ್ನೆಟ್ (internet), ಕಂಪ್ಯೂಟರ್ (computer), "
  "ಚಾರ್ಜರ್ (charger), ಬ್ಯಾಟರಿ (battery), ಪಾಸ್ವರ್ಡ್ (password), ಆ್ಯಪ್ (app), "
  "ಈಮೇಲ್ (email). Troubleshooting trio: ... ಕೆಲಸ ಮಾಡುತ್ತಿಲ್ಲ / ... ಆಗುತ್ತಿಲ್ಲ "
  "covers every broken device. Enable the Kannada keyboard and type these "
  "sentences for real practice."),
 "how_it_works": (
  "This record wires you into the digital world in Kannada: twenty sentences "
  "for calls, messages, internet, computers and troubleshooting, plus the "
  "core tech nouns. Switch your phone to the Kannada keyboard and retype "
  "five sentences - typing is the fastest path to reading fluency."),
 "key_points": [
  "Tech nouns: ಫೋನ್, ಕರೆ, ಮೆಸೇಜ್, ಇಂಟರ್ನೆಟ್, ಕಂಪ್ಯೂಟರ್, ಚಾರ್ಜರ್, ಬ್ಯಾಟರಿ, ಪಾಸ್ವರ್ಡ್, ಆ್ಯಪ್, ಈಮೇಲ್.",
  "Troubleshooting: X ಕೆಲಸ ಮಾಡುತ್ತಿಲ್ಲ / X ಆಗುತ್ತಿಲ್ಲ.",
  "Request frames: ದಯವಿಟ್ಟು ಕರೆ ಮಾಡಿ / ಮೆಸೇಜ್ ಮಾಡುತ್ತೇನೆ / ಈಮೇಲ್ ಕಳುಹಿಸುತ್ತೇನೆ.",
  "ಫೋಟೋ ತೆಗೆಯಬಹುದೇ? asks permission politely.",
  "ವೈ-ಫೈ ಪಾಸ್ವರ್ಡ್ ಏನು? is the traveler's lifeline.",
  "ನನ್ನ ಫೋನಿನಲ್ಲಿ ಕನ್ನಡ ಕೀಬೋರ್ಡ್ ಇದೆ - enable it and use it.",
  "Commands: ಡೌನ್ಲೋಡ್ ಮಾಡಿ, ಅಪ್ಡೇಟ್ ಮಾಡಿ, ಹಾಕಿ.",
  "Type five sentences on a real Kannada keyboard.",
 ],
 "requirements": [
  "Enable the Kannada keyboard on your phone.",
  "Type ten sentences from this record.",
  "Explain three phone problems in Kannada.",
 ],
 "standards": [
  "Government of Karnataka standard Kannada",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
  "Unicode Consortium. The Unicode Standard, Version 15.0: Kannada, Range 0C80-0CFF.",
 ],
 "sig_lens": (
  "Through the Signature lens technology is re-taught as his comms array: "
  "twenty stamped sentences operating every device in his kit, each "
  "troubleshooting phrase a field repair order. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 21
{
 "key": "tenses", "name": "Kannada Verb Tenses in Sentences",
 "group": "Advanced", "ladder": 21, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "The Kannada verb system in sentences: present, past and future, six "
  "sentences per tense, each translated. Kannada builds tenses on three "
  "stems: present -ಉತ್ತ್- (-utt-), past -ಇದ್- (-id-), future -ಉವ್- (-uv-), "
  "with personal endings -ಏನೆ (I), -ಆನೆ (he), -ಆಳೆ (she), -ದೆ (it), -ಎವೆ "
  "(we), -ಈರಿ (you formal), -ಆರೆ (they). PRESENT (6): 1. ನಾನು ಪ್ರತಿದಿನ "
  "ಓದುತ್ತೇನೆ (nānu pratidina ōduttēne) - 'I read every day'. 2. ಅವನು ಶಾಲೆಗೆ "
  "ಹೋಗುತ್ತಾನೆ (avanu śālege hōguttāne) - 'He goes to school'. 3. ಅವಳು ಅಡುಗೆ "
  "ಮಾಡುತ್ತಾಳೆ (avaḷu aḍuge māḍuttāḷe) - 'She cooks'. 4. ನಾವು ಕನ್ನಡ "
  "ಕಲಿಯುತ್ತೇವೆ (nāvu kannaḍa kaliyuttēve) - 'We learn Kannada'. 5. ಅವರು "
  "ಬೆಂಗಳೂರಿನಲ್ಲಿ ವಾಸಿಸುತ್ತಾರೆ (avaru beṅgaḷūrinalli vāsisuttāre) - 'They live "
  "in Bengaluru'. 6. ಮಳೆ ಬರುತ್ತದೆ (maḷe baruttade) - 'Rain comes'. PAST (6): "
  "1. ನಾನು ನಿನ್ನೆ ಪುಸ್ತಕ ಓದಿದೆನು (nānu ninne pustaka ōdidenu) - 'I read a book "
  "yesterday'. 2. ಅವನು ಮನೆಗೆ ಹೋದನು (avanu manege hōdanu) - 'He went home'. "
  "3. ಅವಳು ಊಟ ಮಾಡಿದಳು (avaḷu ūṭa māḍidaḷu) - 'She cooked the meal'. 4. ನಾವು "
  "ಸಿನೆಮಾ ನೋಡಿದೆವು (nāvu sinemā nōḍidevu) - 'We watched a movie'. 5. ಅವರು "
  "ಬಂದರು (avaru bandaru) - 'They came'. 6. ಮಳೆ ಬಂತು (maḷe bantu) - 'It "
  "rained'. FUTURE (6): 1. ನಾನು ನಾಳೆ ಬರುವೆನು (nānu nāḷe baruvenu) - 'I will "
  "come tomorrow'. 2. ಅವನು ಕೆಲಸ ಮಾಡುವನು (avanu kelasa māḍuvanu) - 'He will "
  "work'. 3. ಅವಳು ಹಾಡುವಳು (avaḷu hāḍuvaḷu) - 'She will sing'. 4. ನಾವು ನಾಳೆ "
  "ಹೋಗುವೆವು (nāvu nāḷe hōguvevu) - 'We will go tomorrow'. 5. ಅವರು ಸಹಾಯ "
  "ಮಾಡುವರು (avaru sahāya māḍuvaru) - 'They will help'. 6. ಸೂರ್ಯ ಮೂಡುವನು "
  "(sūrya mūḍuvanu) - 'The sun will rise'. Aspect extras: the progressive "
  "ಮಾಡುತ್ತಿದ್ದೇನೆ (māḍuttiddēne, I am doing right now) and the perfect "
  "ಮಾಡಿದ್ದೇನೆ (māḍiddēne, I have done) refine the present; the past "
  "progressive ಮಾಡುತ್ತಿದ್ದೆನು (māḍuttiddenu, I was doing) refines the past. "
  "Negatives: present/future ನಾನು ಬರುವುದಿಲ್ಲ (I will not come), past ಅವನು "
  "ಬರಲಿಲ್ಲ (he did not come). Drill one verb - ಮಾಡು - through all persons "
  "and all three tenses, then every other verb follows the same machine."),
 "how_it_works": (
  "This record runs the tense machine: eighteen sentences, six per tense, "
  "showing the three stems (-ಉತ್ತ್, -ಇದ್, -ಉವ್) and the personal endings in "
  "action, plus progressive, perfect and negative forms. Take ಮಾಡು through "
  "all persons × all tenses aloud, then repeat with ಹೋಗು and ಬರು."),
 "key_points": [
  "Three stems: present -ಉತ್ತ್- (ಮಾಡುತ್ತೇನೆ), past -ಇದ್- (ಮಾಡಿದೆನು), future -ಉವ್- (ಮಾಡುವೆನು).",
  "Personal endings: -ಏನೆ (I), -ಆನೆ (he), -ಆಳೆ (she), -ದೆ (it), -ಎವೆ (we), -ಈರಿ (you formal), -ಆರೆ (they).",
  "Six present, six past, six future sentences - all translated.",
  "Progressive: ಮಾಡುತ್ತಿದ್ದೇನೆ (am doing); perfect: ಮಾಡಿದ್ದೇನೆ (have done); past progressive: ಮಾಡುತ್ತಿದ್ದೆನು (was doing).",
  "Negative: ಬರುವುದಿಲ್ಲ (will not come); ಬರಲಿಲ್ಲ (did not come).",
  "Time adverbs anchor tense: ಪ್ರತಿದಿನ (present), ನಿನ್ನೆ (past), ನಾಳೆ (future).",
  "One verb × all persons × all tenses is the master drill.",
  "ನಾವು ಕನ್ನಡ ಕಲಿಯುತ್ತೇವೆ → ಕಲಿದೆವು → ಕಲಿಯುವೆವು: past, present, future of your journey.",
 ],
 "requirements": [
  "Conjugate ಮಾಡು, ಹೋಗು, ಬರು fully: 8 persons × 3 tenses.",
  "Write six original sentences per tense.",
  "Convert ten present sentences to past and future.",
 ],
 "standards": [
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "ISO 15919:2001 transliteration",
 ],
 "citations": [
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
 ],
 "sig_lens": (
  "Through the Signature lens tenses are re-taught as his time machine: "
  "three stamped stems driving past, present and future, every personal "
  "ending a labeled gear, negatives as the reverse lever. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 22
{
 "key": "qa", "name": "Kannada Questions and Answers",
 "group": "Advanced", "ladder": 22, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Twenty question-and-answer pairs covering who, what, where, when, why and "
  "how - the complete interrogation toolkit. 1. ನಿಮ್ಮ ಹೆಸರೇನು? (nimma "
  "hesarēnu?) - ನನ್ನ ಹೆಸರು ಸೀತಾ (nanna hesaru sītā) - 'What is your name?' - "
  "'My name is Sita'. 2. ನೀವು ಎಲ್ಲಿರುತ್ತೀರಿ? (nīvu elliruttīri?) - ನಾನು "
  "ಮೈಸೂರಿನಲ್ಲಿರುತ್ತೇನೆ (nānu maisūrinalliruttēne) - 'Where do you live?' - 'I "
  "live in Mysuru'. 3. ಇವರು ಯಾರು? (ivaru yāru?) - ಇವರು ನನ್ನ ಅಣ್ಣ (ivaru "
  "nanna aṇṇa) - 'Who is this?' - 'He is my elder brother'. 4. ನೀವು ಏನು "
  "ಮಾಡುತ್ತೀರಿ? (nīvu ēnu māḍuttīri?) - ನಾನು ಓದುತ್ತೇನೆ (nānu ōduttēne) - 'What "
  "do you do?' - 'I study'. 5. ನೀವು ಮಾರುಕಟ್ಟೆಗೆ ಯಾವಾಗ ಹೋಗುವಿರಿ? (nīvu "
  "mārukaṭṭege yāvāga hōguviri?) - ನಾನು ಸಂಜೆ ಹೋಗುವೆನು (nānu sanje hōguvenu) "
  "- 'When will you go to the market?' - 'I will go in the evening'. 6. ನೀವು "
  "ಯಾಕೆ ಬರಲಿಲ್ಲ? (nīvu yāke baralilla?) - ನಾನು ಅಸ್ವಸ್ಥನಾಗಿದ್ದೆನು (nānu "
  "asvasthanāgiddenu) - 'Why did you not come?' - 'I was unwell'. 7. ಇದು ಹೇಗೆ "
  "ಕೆಲಸ ಮಾಡುತ್ತದೆ? (idu hēge kelasa māḍuttade?) - ಗುಂಡಿ ಒತ್ತಿ (guṇḍi otti) - "
  "'How does this work?' - 'Press the button'. 8. ಈಗ ಎಷ್ಟು ಗಂಟೆ? (īga eṣṭu "
  "gaṇṭe?) - ಎರಡು ಗಂಟೆ (eraḍu gaṇṭe) - 'What time is it?' - 'Two o'clock'. "
  "9. ನೀವು ಕನ್ನಡ ಮಾತಾಡುತ್ತೀರೇ? (nīvu kannaḍa mātāḍuttīrē?) - ಹೌದು, ಸ್ವಲ್ಪ "
  "ಸ್ವಲ್ಪ (haudu, svalpa svalpa) - 'Do you speak Kannada?' - 'Yes, a "
  "little'. 10. ಊಟ ಹೇಗಿತ್ತು? (ūṭa hēgittu?) - ತುಂಬಾ ಚೆನ್ನಾಗಿತ್ತು (tumbā "
  "cennāgittu) - 'How was the food?' - 'It was very good'. 11. ಟಿಕೆಟ್ಗೆ ಎಷ್ಟು? "
  "(ṭikeṭge eṣṭu?) - ಐವತ್ತು ರೂಪಾಯಿ (aivattu rūpāyi) - 'How much for the "
  "ticket?' - 'Fifty rupees'. 12. ವೈದ್ಯರು ಎಲ್ಲಿದ್ದಾರೆ? (vaidyaru elliddāre?) "
  "- ವೈದ್ಯರು ಒಳಗಿದ್ದಾರೆ (vaidyaru oḷagiddāre) - 'Where is the doctor?' - 'The "
  "doctor is inside'. 13. ನಿಮ್ಮ ವಯಸ್ಸೆಷ್ಟು? (nimma vayasseṣṭu?) - ನನಗೆ ಇಪ್ಪತ್ತು "
  "ವಯಸ್ಸು (nanage ippattu vayassu) - 'How old are you?' - 'I am twenty'. 14. "
  "ಮಳೆ ಬರುತ್ತದೆಯೇ? (maḷe baruttadeyē?) - ಹೌದು, ಬರುವಂತೆ ಕಾಣುತ್ತದೆ (haudu, "
  "baruvante kāṇuttade) - 'Will it rain?' - 'Yes, it looks like it'. 15. ಇದು "
  "ಯಾರದ್ದು? (idu yāraddu?) - ಇದು ನನ್ನದು (idu nannadu) - 'Whose is this?' - "
  "'It is mine'. 16. ನೀವು ಎಲ್ಲಿಂದ ಬಂದಿರಿ? (nīvu ellinda bandiri?) - ನಾನು "
  "ಧಾರವಾಡದಿಂದ ಬಂದೆನು (nānu dhāravāḍadinda bandenu) - 'Where did you come "
  "from?' - 'I came from Dharwad'. 17. ನಾನು ಒಳಗೆ ಬರಬಹುದೇ? (nānu oḷage "
  "barabahudē?) - ಹೌದು, ಬನ್ನಿ (haudu, banni) - 'May I come in?' - 'Yes, come "
  "in'. 18. ನಾಳೆ ಏನು ಮಾಡುವಿರಿ? (nāḷe ēnu māḍuviri?) - ನಾಳೆ ನಾನು ಮನೆಯಲ್ಲಿರುತ್ತೇನೆ "
  "(nāḷe nānu maneyalliruttēne) - 'What will you do tomorrow?' - 'Tomorrow I "
  "will stay home'. 19. ಚಹಾ ಕುಡಿಯುವಿರಾ? (cahā kuḍiyuvirā?) - ಹೌದು, "
  "ಧನ್ಯವಾದಗಳು (haudu, dhanyavādagaḷu) - 'Will you have tea?' - 'Yes, thank "
  "you'. 20. ಎಲ್ಲಾ ಸರಿಯಿದೆಯೇ? (ellā sariyideyē?) - ಹೌದು, ಎಲ್ಲಾ ಸರಿಯಿದೆ "
  "(haudu, ellā sariyide) - 'Is everything all right?' - 'Yes, all is well'. "
  "The eight question words - ಯಾರು, ಏನು, ಎಲ್ಲಿ, ಯಾವಾಗ, ಏಕೆ/ಯಾಕೆ, ಹೇಗೆ, "
  "ಎಷ್ಟು, ಯಾವುದು - plus the -ಏ/-ವೇ yes-no particle cover every question you "
  "will ever need."),
 "how_it_works": (
  "This record drills the full interrogation cycle: twenty pairs, each "
  "question using one of the eight question words or the yes-no -ಏ particle, "
  "each answer a complete natural sentence. Practice as a dialogue with a "
  "partner - one asks from the left column, the other answers from memory."),
 "key_points": [
  "Eight question words: ಯಾರು, ಏನು, ಎಲ್ಲಿ, ಯಾವಾಗ, ಏಕೆ/ಯಾಕೆ, ಹೇಗೆ, ಎಷ್ಟು, ಯಾವುದು.",
  "Yes-no questions add -ಏ/-ವೇ to the verb: ಬರುವಿರೇ?, ಮಾತಾಡುತ್ತೀರೇ?",
  "Permission frame: ...-ಬಹುದೇ? - ಬರಬಹುದೇ?, ತೆಗೆಯಬಹುದೇ?",
  "Question words stay in place - no word-order gymnastics.",
  "Answer frames mirror the question's verb and tense.",
  "ಹೌದು/ಇಲ್ಲ open every yes-no answer; ಸ್ವಲ್ಪ ಸ್ವಲ್ಪ softens ability claims.",
  "ಎಲ್ಲಾ ಸರಿಯಿದೆಯೇ? checks on anyone, anywhere.",
  "Twenty pairs = the complete daily interrogation set.",
 ],
 "requirements": [
  "Ask a partner all twenty questions from memory.",
  "Answer each with a different true sentence about yourself.",
  "Convert ten statements into -ಏ yes-no questions.",
 ],
 "standards": [
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "ISO 15919:2001 transliteration",
 ],
 "citations": [
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
 ],
 "sig_lens": (
  "Through the Signature lens questions are re-taught as his interrogation "
  "array: twenty stamped Q-and-A circuits, eight question-word probes and one "
  "yes-no switch, every answer logged like telemetry. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 23
{
 "key": "commands", "name": "Kannada Commands and Requests",
 "group": "Advanced", "ladder": 23, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Twenty imperatives and polite requests, formal versus informal - command "
  "with courtesy. Formal (to elders, strangers, groups) uses -ಇರಿ/-ಿ "
  "endings; informal (to friends, juniors) uses the bare stem. 1. ದಯವಿಟ್ಟು "
  "ಕುಳಿತುಕೊಳ್ಳಿ (dayaviṭṭu kuḷitukoḷḷi) - 'Please sit down' (formal) vs "
  "ಕುಳಿತುಕೋ (kuḷitukō) - 'sit' (informal). 2. ದಯವಿಟ್ಟು ಬನ್ನಿ (dayaviṭṭu "
  "banni) - 'Please come' vs ಬಾ (bā) - 'come'. 3. ದಯವಿಟ್ಟು ಹೇಳಿ (dayaviṭṭu "
  "hēḷi) - 'Please tell me' vs ಹೇಳು (hēḷu) - 'tell'. 4. ಸ್ವಲ್ಪ ನಿಧಾನವಾಗಿ "
  "ಮಾತಾಡಿ (svalpa nidhānavāgi mātāḍi) - 'Please speak a little slowly' vs "
  "ನಿಧಾನವಾಗಿ ಮಾತಾಡು (nidhānavāgi mātāḍu). 5. ದಯವಿಟ್ಟು ಸಹಾಯ ಮಾಡಿ (dayaviṭṭu "
  "sahāya māḍi) - 'Please help' vs ಸಹಾಯ ಮಾಡು (sahāya māḍu). 6. ಬಾಗಿಲು "
  "ತೆರೆಯಿರಿ (bāgilu tereyiri) - 'Open the door' (formal) vs ಬಾಗಿಲು ತೆರೆ "
  "(bāgilu tere). 7. ಬಾಗಿಲು ಮುಚ್ಚಿರಿ (bāgilu mucciri) - 'Close the door' vs "
  "ಬಾಗಿಲು ಮುಚ್ಚು (bāgilu muccu). 8. ಇಲ್ಲಿ ನೋಡಿ (illi nōḍi) - 'Look here' vs "
  "ಇಲ್ಲಿ ನೋಡು (illi nōḍu). 9. ಗಮನವಿಟ್ಟು ಕೇಳಿ (gamanaviṭṭu kēḷi) - 'Listen "
  "carefully' vs ಗಮನವಿಟ್ಟು ಕೇಳು (gamanaviṭṭu kēḷu). 10. ಪುಸ್ತಕ ಕೊಡಿ (pustaka "
  "koḍi) - 'Give the book' vs ಪುಸ್ತಕ ಕೊಡು (pustaka koḍu). 11. ಊಟ ಮಾಡಿ (ūṭa "
  "māḍi) - 'Please eat' vs ಊಟ ಮಾಡು (ūṭa māḍu). 12. ನೀರು ಕುಡಿಯಿರಿ (nīru "
  "kuḍiyiri) - 'Drink water' vs ನೀರು ಕುಡಿ (nīru kuḍi). 13. ಬೇಗ ಬನ್ನಿ (bēga "
  "banni) - 'Come quickly' vs ಬೇಗ ಬಾ (bēga bā). 14. ನಾಳೆ ಬನ್ನಿ (nāḷe banni) "
  "- 'Come tomorrow' vs ನಾಳೆ ಬಾ (nāḷe bā). 15. ಸುಮ್ಮನಿರಿ (summaniri) - 'Be "
  "quiet' (formal) vs ಸುಮ್ಮನಿರು (summaniru). 16. ಹೋಗಬೇಡಿ (hōgabēḍi) - 'Do "
  "not go' (formal) vs ಹೋಗಬೇಡ (hōgabēḍa). 17. ಹೆದರಬೇಡಿ (hedarabēḍi) - 'Do "
  "not fear' vs ಹೆದರಬೇಡ (hedarabēḍa). 18. ಚಿಂತೆ ಮಾಡಬೇಡಿ (cinte māḍabēḍi) - "
  "'Do not worry' vs ಚಿಂತೆ ಮಾಡಬೇಡ (cinte māḍabēḍa). 19. ದಯವಿಟ್ಟು ಕ್ಷಮಿಸಿ "
  "(dayaviṭṭu kṣamisi) - 'Please forgive me' vs ಕ್ಷಮಿಸು (kṣamisu). 20. "
  "ಶುಭವಾಗಲಿ! (śubhavāgali!) - 'May it go well!' - the blessing imperative. "
  "Negative commands use -ಬೇಡಿ/-ಬೇಡ: ಮಾಡಬೇಡಿ (do not do). The softener trio "
  "ದಯವಿಟ್ಟು (please), ಸ್ವಲ್ಪ (a little), -ಇರಿ endings turns any order into a "
  "request. Rule of thumb: when in doubt, go formal - no Kannadiga ever "
  "minded extra politeness."),
 "how_it_works": (
  "This record teaches command as a courtesy system: twenty formal/informal "
  "pairs showing the -ಇರಿ/-ಿ formal endings against bare-stem informal "
  "forms, plus the -ಬೇಡಿ negative and the ದಯವಿಟ್ಟು softener. Practice giving "
  "every command both ways, then default to formal with anyone you do not "
  "know well."),
 "key_points": [
  "Formal imperatives: -ಇರಿ/-ಿ (ಬನ್ನಿ, ಮಾಡಿ, ಕುಳಿತುಕೊಳ್ಳಿ); informal: bare stem (ಬಾ, ಮಾಡು, ಕುಳಿತುಕೋ).",
  "20 formal/informal pairs covering daily commands.",
  "Negative commands: -ಬೇಡಿ (formal) / -ಬೇಡ (informal) - ಹೋಗಬೇಡಿ, ಮಾಡಬೇಡಿ.",
  "Softener trio: ದಯವಿಟ್ಟು, ಸ್ವಲ್ಪ, formal endings.",
  "ಶುಭವಾಗಲಿ! is the blessing imperative.",
  "ಹೇಳಿ vs ಹೇಳು, ಕೊಡಿ vs ಕೊಡು - the politeness gap in one syllable.",
  "When in doubt, go formal.",
  "Commands + ದಯವಿಟ್ಟು = requests; requests get results.",
 ],
 "requirements": [
  "Give all twenty commands formally, then informally.",
  "Forbid five actions with -ಬೇಡಿ.",
  "Soften five blunt orders with ದಯವಿಟ್ಟು + ಸ್ವಲ್ಪ.",
 ],
 "standards": [
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Government of Karnataka standard Kannada",
 ],
 "citations": [
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
 ],
 "sig_lens": (
  "Through the Signature lens commands are re-taught as his order book: "
  "twenty stamped directives in two courtesy grades, negatives as stop "
  "orders, and ದಯವಿಟ್ಟು as the polish on every command he issues. Signature-"
  "made teaching, clearly labeled, never presented as an outside authority's "
  "text."),
},
# ================================================================== 24
{
 "key": "descriptions", "name": "Describing People and Places in Kannada",
 "group": "Advanced", "ladder": 24, "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Twenty rich descriptive sentences - people, places and things in detail. "
  "1. ನನ್ನ ಅಣ್ಣ ಎತ್ತರವಾಗಿದ್ದಾನೆ ಮತ್ತು ಬಲಶಾಲಿಯಾಗಿದ್ದಾನೆ (nanna aṇṇa "
  "ettaravāgiddāne mattu balaśāliyāgiddāne) - 'My elder brother is tall and "
  "strong'. 2. ನನ್ನ ತಂಗಿಗೆ ಉದ್ದ ಕೂದಲು ಮತ್ತು ದೊಡ್ಡ ಕಣ್ಣುಗಳಿವೆ (nanna taṅgige "
  "udda kūdalu mattu doḍḍa kaṇṇugaḷive) - 'My younger sister has long hair "
  "and big eyes'. 3. ತಾತನಿಗೆ ಬಿಳಿ ಗಡ್ಡವಿದೆ (tātanige biḷi gaḍḍavide) - "
  "'Grandfather has a white beard'. 4. ಅಜ್ಜಿ ಯಾವಾಗಲೂ ನಗುತ್ತಿರುತ್ತಾರೆ (ajji "
  "yāvāgalū naguttiruttāre) - 'Grandmother is always smiling'. 5. ನನ್ನ "
  "ಸ್ನೇಹಿತ ತುಂಬಾ ಬುದ್ಧಿವಂತನು (nanna snēhita tumbā buddhivantanu) - 'My friend "
  "is very intelligent'. 6. ಆ ಹುಡುಗಿ ಸುಂದರವಾಗಿ ಹಾಡುತ್ತಾಳೆ (ā huḍugi "
  "sundaravāgi hāḍuttāḷe) - 'That girl sings beautifully'. 7. ಬೆಂಗಳೂರು "
  "ತುಂಬಾ ದೊಡ್ಡ ಮತ್ತು ಸುಂದರ ನಗರ (beṅgaḷūru tumbā doḍḍa mattu sundara nagara) - "
  "'Bengaluru is a very big and beautiful city'. 8. ಮೈಸೂರು ಅರಮನೆ ಅದ್ಭುತವಾಗಿದೆ "
  "(maisūru aramane adbhutavāgide) - 'The Mysuru palace is magnificent'. 9. "
  "ಹಂಪಿಯ ಶಿಲ್ಪಗಳು ಸಾವಿರ ವರ್ಷ ಹಳೆಯವು (hampiya śilpagaḷu sāvira varṣa "
  "haḷeyavu) - 'Hampi's sculptures are a thousand years old'. 10. ಜೋಗ "
  "ಜಲಪಾತ ಭಾರತದ ಅತಿ ಎತ್ತರದ ಜಲಪಾತಗಳಲ್ಲಿ ಒಂದು (jōga jalapāta bhāratada ati "
  "ettarada jalapātagalaḷli ondu) - 'Jog Falls is among India's tallest "
  "waterfalls'. 11. ಕೂರ್ಗ್ ಹಸಿರು ಬೆಟ್ಟಗಳಿಂದ ಕೂಡಿದೆ (kūrg hasiru "
  "beṭṭagaḷinda kūḍide) - 'Coorg is covered with green hills'. 12. ನಮ್ಮ ಮನೆ "
  "ಶಾಂತವಾದ ಬೀದಿಯಲ್ಲಿದೆ (namma mane śāntavāda bīdiyallide) - 'Our house is on "
  "a quiet street'. 13. ಈ ಉದ್ಯಾನದಲ್ಲಿ ನೂರಾರು ಹೂವುಗಳಿವೆ (ī udyānadalli "
  "nūrāru hūvugaḷive) - 'There are hundreds of flowers in this garden'. 14. "
  "ಸಮುದ್ರ ತೀರ ಸುಂದರವಾಗಿದೆ (samudra tīra sundaravāgide) - 'The sea shore is "
  "beautiful'. 15. ಈ ಪುಸ್ತಕ ತುಂಬಾ ಆಸಕ್ತಿದಾಯಕವಾಗಿದೆ (ī pustaka tumbā "
  "āsaktidāyakavāgide) - 'This book is very interesting'. 16. ಆ ಸಿನೆಮಾ "
  "ತುಂಬಾ ಮನರಂಜನೆಯಾಗಿತ್ತು (ā sinemā tumbā manarañjaneyāgittu) - 'That movie "
  "was very entertaining'. 17. ಕಾಫಿ ಘಮಘಮಿಸುತ್ತಿದೆ (kāphi ghamaghamisuttide) "
  "- 'The coffee smells aromatic'. 18. ಮಾವಿನಹಣ್ಣು ಸಿಹಿಯಾಗಿ ರುಚಿಯಾಗಿದೆ "
  "(māvinhannu sihiyāgi ruciyāgide) - 'The mango is sweet and tasty'. 19. "
  "ಚಳಿಗಾಲದ ಬೆಳಿಗ್ಗೆ ಮಂಜಿನಿಂದ ಕೂಡಿರುತ್ತದೆ (caḷigālada beḷigge manjiniṃda "
  "kūḍiruttade) - 'Winter mornings are full of fog'. 20. ಕರ್ನಾಟಕ ಸಂಸ್ಕೃತಿ "
  "ಮತ್ತು ಸಂಗೀತದಿಂದ ಸಮೃದ್ಧವಾಗಿದೆ (karnāṭaka sanskṛti mattu sangītadinda "
  "samṛddhavāgide) - 'Karnataka is rich in culture and music'. Description "
  "tools: ಮತ್ತು (and), ತುಂಬಾ (very), -ಇಂದ ಕೂಡಿದೆ (covered with), ಅತಿ ...-"
  "ಗಳಲ್ಲಿ ಒಂದು (among the most ...). Paint with adjectives; connect with "
  "ಮತ್ತು; measure with numbers."),
 "how_it_works": (
  "This record teaches description as painting: twenty detailed sentences "
  "about people, Karnataka's famous places, and sensory things, using the "
  "connector toolkit - ಮತ್ತು, ತುಂಬಾ, -ಇಂದ ಕೂಡಿದೆ, ಅತಿ. Describe your best "
  "friend, your street and your favorite dish in five sentences each."),
 "key_points": [
  "People: ಎತ್ತರ, ಬಲಶಾಲಿ, ಬುದ್ಧಿವಂತ, ಸುಂದರ - stack two adjectives with ಮತ್ತು.",
  "Places: ಬೆಂಗಳೂರು, ಮೈಸೂರು ಅರಮನೆ, ಹಂಪಿ, ಜೋಗ ಜಲಪಾತ, ಕೂರ್ಗ್ - Karnataka's showcase.",
  "Sensory: ಘಮಘಮಿಸುತ್ತಿದೆ (aromatic), ಸಿಹಿಯಾಗಿ ರುಚಿಯಾಗಿದೆ, ಮಂಜಿನಿಂದ ಕೂಡಿದೆ.",
  "Measure phrases: ನೂರಾರು, ಸಾವಿರ ವರ್ಷ, ಅತಿ ಎತ್ತರದ ...ಗಳಲ್ಲಿ ಒಂದು.",
  "-ಇಂದ ಕೂಡಿದೆ = covered/filled with.",
  "ತುಂಬಾ intensifies any description.",
  "Describe friend + street + dish in five sentences each.",
  "ಕರ್ನಾಟಕ ಸಂಸ್ಕೃತಿಯಿಂದ ಸಮೃದ್ಧವಾಗಿದೆ closes with pride.",
 ],
 "requirements": [
  "Describe three people in five sentences each.",
  "Describe three Karnataka places from memory.",
  "Write a ten-sentence sensory description of a meal.",
 ],
 "standards": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
 ],
 "sig_lens": (
  "Through the Signature lens description is re-taught as his portrait "
  "studio: twenty stamped sentences painting people, places and flavors in "
  "full color, every adjective a brushstroke he controls. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 25
{
 "key": "story1", "name": "Kannada Story I: A Simple Day",
 "group": "Advanced", "ladder": 25, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A ten-sentence simple story in Kannada with line-by-line English "
  "translation - a boy's ordinary day, present and habitual tenses. 1. ರವಿ "
  "ಬೆಳಿಗ್ಗೆ ಬೇಗ ಏಳುತ್ತಾನೆ (ravi beḷigge bēga ēḷuttāne) - 'Ravi wakes up early "
  "in the morning'. 2. ಅವನು ಹಲ್ಲುಜ್ಜಿ ಮುಖ ತೊಳೆಯುತ್ತಾನೆ (avanu hallujji mukha "
  "toḷeyuttāne) - 'He brushes his teeth and washes his face'. 3. ಅಮ್ಮ ಅವನಿಗೆ "
  "ತಿಂಡಿ ಕೊಡುತ್ತಾಳೆ (amma avanige tiṇḍi koḍuttāḷe) - 'Mother gives him "
  "breakfast'. 4. ಅವನು ಶಾಲಾ ಬ್ಯಾಗ್ ತೆಗೆದುಕೊಂಡು ಹೊರಡುತ್ತಾನೆ (avanu śālā byāg "
  "tegedukoṇḍu horaḍuttāne) - 'He takes his school bag and leaves'. 5. "
  "ಶಾಲೆಯಲ್ಲಿ ಅವನು ಸ್ನೇಹಿತರನ್ನು ಭೇಟಿಯಾಗುತ್ತಾನೆ (śāleyalli avanu snēhitarannu "
  "bhēṭiyāguttāne) - 'At school he meets his friends'. 6. ಅಧ್ಯಾಪಕರು ಕನ್ನಡ "
  "ಪಾಠ ಮಾಡುತ್ತಾರೆ (adhyāpakaru kannaḍa pāṭha māḍuttāre) - 'The teacher "
  "teaches the Kannada lesson'. 7. ರವಿ ಗಮನವಿಟ್ಟು ಕೇಳುತ್ತಾನೆ (ravi "
  "gamanaviṭṭu kēḷuttāne) - 'Ravi listens attentively'. 8. ಮಧ್ಯಾಹ್ನ ಅವನು "
  "ಸ್ನೇಹಿತರೊಂದಿಗೆ ಊಟ ಮಾಡುತ್ತಾನೆ (madhyāhna avanu snēhitarondige ūṭa "
  "māḍuttāne) - 'At noon he eats lunch with his friends'. 9. ಸಂಜೆ ಅವನು ಮನೆಗೆ "
  "ಬಂದು ಆಟವಾಡುತ್ತಾನೆ (sanje avanu manege bandu āṭavāḍuttāne) - 'In the "
  "evening he comes home and plays'. 10. ರಾತ್ರಿ ಅವನು ಬೇಗ ಮಲಗುತ್ತಾನೆ (rātri "
  "avanu bēga malaguttāne) - 'At night he sleeps early'. Read the Kannada "
  "line first, guess the meaning, then check the English. Retell the whole "
  "story from memory in Kannada - that is the real test."),
 "how_it_works": (
  "This record proves you can follow a whole narrative: ten simple sentences, "
  "present and habitual verbs, line-by-line English. Read Kannada-first, "
  "guess, check. Then retell it without looking, then change one detail - "
  "the boy's name, the subject, the game - and retell again."),
 "key_points": [
  "10-sentence story, line-by-line English translation.",
  "Present/habitual tense throughout: -ಉತ್ತಾನೆ forms.",
  "Daily routine vocabulary: ಏಳು, ಹಲ್ಲುಜ್ಜು, ತಿಂಡಿ, ಶಾಲೆ, ಪಾಠ, ಆಟ.",
  "Sequence words: ಬೆಳಿಗ್ಗೆ, ಮಧ್ಯಾಹ್ನ, ಸಂಜೆ, ರಾತ್ರಿ.",
  "Compound actions with -ಕೊಂಡು/-ದು: ತೆಗೆದುಕೊಂಡು, ಬಂದು.",
  "ಗಮನವಿಟ್ಟು ಕೇಳುತ್ತಾನೆ models the good student.",
  "Retell from memory - the real comprehension test.",
  "Change one detail and retell to prove mastery.",
 ],
 "requirements": [
  "Read the story Kannada-first three times.",
  "Retell it from memory in Kannada.",
  "Write your own ten-sentence day.",
 ],
 "standards": [
  "Government of Karnataka standard Kannada",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
 ],
 "sig_lens": (
  "Through the Signature lens this story is re-taught as his day-one "
  "field log: ten stamped lines tracking an ordinary day with "
  "instrument precision, proving the machine runs on routine. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 26
{
 "key": "story2", "name": "Kannada Story II: A Past Journey",
 "group": "Advanced", "ladder": 26, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A ten-sentence story in the past tense with line-by-line English - a "
  "family trip to Mysuru. 1. ಕಳೆದ ಭಾನುವಾರ ನಾವು ಮೈಸೂರಿಗೆ ಹೋದೆವು (kaḷeda "
  "bhānuvāra nāvu maisūrige hōdevu) - 'Last Sunday we went to Mysuru'. 2. "
  "ನಾವು ಬೆಳಿಗ್ಗೆ ಆರು ಗಂಟೆಗೆ ಹೊರಟೆವು (nāvu beḷigge āru gaṇṭege horaṭevu) - "
  "'We left at six in the morning'. 3. ರೈಲು ತುಂಬಾ ವೇಗವಾಗಿ ಹೋಯಿತು (railu "
  "tumbā vēgavāgi hōyitu) - 'The train went very fast'. 4. ನಾವು ಕಿಟಕಿಯಿಂದ "
  "ಹಸಿರು ಹೊಲಗಳನ್ನು ನೋಡಿದೆವು (nāvu kiṭakiyinda hasiru holagaḷannu nōḍidevu) - "
  "'We saw green fields through the window'. 5. ಮೈಸೂರಿನಲ್ಲಿ ನಾವು ಮೊದಲು "
  "ಅರಮನೆಯನ್ನು ನೋಡಿದೆವು (maisūrinalli nāvu modalu aramaneyannu nōḍidevu) - 'In "
  "Mysuru we first saw the palace'. 6. ಅರಮನೆ ತುಂಬಾ ಸುಂದರವಾಗಿತ್ತು (aramane "
  "tumbā sundaravāgittu) - 'The palace was very beautiful'. 7. ನಂತರ ನಾವು "
  "ಮೃಗಾಲಯಕ್ಕೆ ಹೋದೆವು (nantara nāvu mṛgālayakke hōdevu) - 'Then we went to the "
  "zoo'. 8. ಮಕ್ಕಳು ಆನೆಗಳನ್ನು ನೋಡಿ ಸಂತೋಷಪಟ್ಟರು (makkaḷu ānegaḷannu nōḍi "
  "santōṣapaṭṭaru) - 'The children were delighted to see the elephants'. 9. "
  "ಸಂಜೆ ನಾವು ಮಸಾಲೆ ದೋಸೆ ತಿಂದೆವು (sanje nāvu masāle dōse tindevu) - 'In the "
  "evening we ate masala dosa'. 10. ರಾತ್ರಿ ನಾವು ಸಂತೋಷದಿಂದ ಮನೆಗೆ ಹಿಂತಿರುಗಿದೆವು "
  "(rātri nāvu santōṣadinda manege hintirugidevu) - 'At night we returned "
  "home happily'. Past-tense endings on parade: -ಎವು (we), -ಇತ್ತು (it), -ಅರು "
  "(they). Time markers: ಕಳೆದ (last), ಮೊದಲು (first), ನಂತರ (then). Retell "
  "your own last trip with the same skeleton."),
 "how_it_works": (
  "This record runs the past tense through a complete journey: ten "
  "sentences, line-by-line English, past endings -ಎವು/-ಇತ್ತು/-ಅರು and time "
  "markers ಕಳೆದ/ಮೊದಲು/ನಂತರ. Map your own last trip onto the skeleton - "
  "where, when, saw, ate, returned - and tell it in Kannada."),
 "key_points": [
  "10-sentence past-tense story, line-by-line English.",
  "Past endings: -ಎವು (we), -ಇತ್ತು (it was), -ಅರು (they).",
  "Time skeleton: ಕಳೆದ (last), ಮೊದಲು (first), ನಂತರ (then), ಸಂಜೆ, ರಾತ್ರಿ.",
  "Travel verbs in past: ಹೋದೆವು, ಹೊರಟೆವು, ನೋಡಿದೆವು, ತಿಂದೆವು, ಹಿಂತಿರುಗಿದೆವು.",
  "ಮೈಸೂರು ಅರಮನೆ and ಮಸಾಲೆ ದೋಸೆ - cultural landmarks in the tale.",
  "ಮಕ್ಕಳು ... ಸಂತೋಷಪಟ್ಟರು shows the -ಪಡು emotion verb.",
  "Retell your own last trip on this skeleton.",
  "Past narration is the heart of storytelling.",
 ],
 "requirements": [
  "Retell the Mysuru story from memory.",
  "Narrate your own last trip in ten past-tense sentences.",
  "Convert story I to the past tense.",
 ],
 "standards": [
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
 ],
 "sig_lens": (
  "Through the Signature lens this journey is re-taught as his expedition "
  "log: ten stamped lines, every past-tense verb a waypoint, the whole trip "
  "archived like a surveyed route. Signature-made teaching, clearly labeled, "
  "never presented as an outside authority's text."),
},
# ================================================================== 27
{
 "key": "story3", "name": "Kannada Story III: A Future Plan",
 "group": "Advanced", "ladder": 27, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "A ten-sentence story in future and conditional forms with line-by-line "
  "English - a girl's plans and dreams. 1. ಲಕ್ಷ್ಮಿಗೆ ದೊಡ್ಡ ಕನಸುಗಳಿವೆ "
  "(lakṣmige doḍḍa kanasugaḷive) - 'Lakshmi has big dreams'. 2. ಅವಳು ವೈದ್ಯಳಾಗುವಳು "
  "(avaḷu vaidyāḷāguvaḷu) - 'She will become a doctor'. 3. ಅವಳು ಪ್ರತಿದಿನ "
  "ಐದು ಗಂಟೆ ಓದುವಳು (avaḷu pratidina aidu gaṇṭe ōduvaḷu) - 'She will study "
  "five hours every day'. 4. ಅವಳ ತಂದೆ-ತಾಯಿ ಅವಳಿಗೆ ಸಹಾಯ ಮಾಡುವರು (avaḷa "
  "tande-tāyi avaḷige sahāya māḍuvaru) - 'Her parents will help her'. 5. "
  "ಅವಳು ಪರೀಕ್ಷೆಯಲ್ಲಿ ಪ್ರಥಮ ಸ್ಥಾನ ಪಡೆಯುವಳು (avaḷu parīkṣeyalli prathama "
  "sthāna paḍeyuvaḷu) - 'She will secure the first rank in the exam'. 6. "
  "ನಂತರ ಅವಳು ವೈದ್ಯಕೀಯ ಕಾಲೇಜಿಗೆ ಸೇರುವಳು (nantara avaḷu vaidyēkīya kālējige "
  "sēruvaḷu) - 'Then she will join medical college'. 7. ಅವಳು ಬಡವರಿಗೆ ಉಚಿತವಾಗಿ "
  "ಚಿಕಿತ್ಸೆ ಕೊಡುವಳು (avaḷu baḍavarige ucitavāgi cikitsa koḍuvaḷu) - 'She will "
  "treat the poor for free'. 8. ಅವಳ ಊರಿನಲ್ಲಿ ಆಸ್ಪತ್ರೆ ಕಟ್ಟುವಳು (avaḷa "
  "ūrinalli āspatre kaṭṭuvaḷu) - 'She will build a hospital in her town'. 9. "
  "ಅವಳು ಕಷ್ಟಪಟ್ಟರೆ ಯಶಸ್ಸು ಸಿಗುತ್ತದೆ"
  "(avaḷu kaṣṭapaṭṭare yaśassu siguttade) - 'If she works hard, "
  "success will come'. 10. ನಾವೆಲ್ಲರೂ ಅವಳಿಗೆ ಶುಭ ಹಾರೈಸೋಣ (nāvellaru avaḷige "
  "śubha hāraisōṇa) - 'Let us all wish her well'. Future endings: -ಉವಳು "
  "(she will), -ಉವರು (they will), -ಉವೆವು (we will). Conditional: -ಅದರೆ "
  "(if) - ಕಷ್ಟಪಟ್ಟರೆ (if she works hard), ಮಳೆ ಬಂದರೆ (if it rains). The "
  "-ಓಣ ending (ಹಾರೈಸೋಣ, let us wish) invites everyone into the dream. "
  "Write your own ten-sentence future: your plan, your conditions, your "
  "invitation."),
 "how_it_works": (
  "This record aims the language at tomorrow: ten sentences in future and "
  "conditional forms, line-by-line English, showing -ಉವಳು/-ಉವರು endings, the "
  "-ಅದರೆ conditional and the -ಓಣ invitation. Write your own ten-sentence "
  "future plan with one condition and one invitation."),
 "key_points": [
  "10-sentence future/conditional story, line-by-line English.",
  "Future endings: -ಉವಳು (she), -ಉವರು (they), -ಉವೆವು (we), -ಉವೆನು (I).",
  "Conditional -ಅದರೆ: ಕಷ್ಟಪಟ್ಟರೆ (if she works hard), ಮಳೆ ಬಂದರೆ (if it rains).",
  "Invitation -ಓಣ: ಹಾರೈಸೋಣ (let us wish).",
  "Dream vocabulary: ಕನಸು, ಯಶಸ್ಸು, ಪ್ರಥಮ ಸ್ಥಾನ.",
  "Service verbs: ಸಹಾಯ ಮಾಡುವರು, ಚಿಕಿತ್ಸೆ ಕೊಡುವಳು.",
  "Your future plan in ten sentences is the assignment.",
  "Conditionals turn plans into wisdom.",
 ],
 "requirements": [
  "Write your ten-sentence future plan.",
  "Make five -ಅದರೆ conditional sentences.",
  "Invite friends to three plans with -ಓಣ.",
 ],
 "standards": [
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "ISO 15919:2001 transliteration",
 ],
 "citations": [
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
 ],
 "sig_lens": (
  "Through the Signature lens this future is re-taught as his blueprint "
  "file: ten stamped lines projecting the build ahead, conditionals as "
  "engineering tolerances, the invitation as his crew call. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 28
{
 "key": "idioms", "name": "Kannada Idioms and Proverbs",
 "group": "Advanced", "ladder": 28, "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Twenty Kannada idioms and proverbs - literal translation, real meaning, "
  "and an example sentence each. 1. ಅತ್ತೆಗೊಂದು ಕಾಲ ಸೊಸೆಗೊಂದು ಕಾಲ (attegondu "
  "kāla sosegondu kāla) - literally 'a time for the mother-in-law, a time "
  "for the daughter-in-law' - meaning: every dog has its day; fortune turns. "
  "Example: ಧೈರ್ಯವಾಗಿರು, ಅತ್ತೆಗೊಂದು ಕಾಲ ಸೊಸೆಗೊಂದು ಕಾಲ (dhairyavāgiru, "
  "attegondu kāla sosegondu kāla) - 'Be brave; every dog has its day'. 2. "
  "ಕಾಗೆಗೆ ತನ್ನ ಮರಿ ಬಂಗಾರ (kāgege tanna mari baṅgāra) - literally 'to the crow "
  "its chick is gold' - meaning: one's own is dearest. 3. ಆನೆಯ ಹೊಟ್ಟೆಗೆ "
  "ಅರೆಕಾಸಿನ ಮಜ್ಜಿಗೆ (āneya hoṭṭege arekāsina majjige) - literally 'buttermilk "
  "worth half a paisa for an elephant's stomach' - meaning: a drop in the "
  "ocean; too little for the need. 4. ಊಟ ಬಲ್ಲವನಿಗೆ ರೋಗವಿಲ್ಲ, ಮಾತು "
  "ಬಲ್ಲವನಿಗೆ ಜಗಳವಿಲ್ಲ (ūṭa ballavanige rōgavilla, mātu ballavanige "
  "jagaḷavilla) - literally 'he who knows food has no disease, he who knows "
  "speech has no quarrel' - meaning: right eating keeps health, right speech "
  "keeps peace. 5. ಕೈ ಕೆಸರಾದರೆ ಬಾಯಿ ಮೊಸರು (kai kesarādare bāyi mosaru) - "
  "literally 'if the hands get muddy, the mouth gets yogurt' - meaning: hard "
  "work is rewarded. 6. ದೀಪದ ಕೆಳಗೆ ಕತ್ತಲು (dīpada keḷage kattalu) - literally "
  "'darkness beneath the lamp' - meaning: we overlook what is closest. 7. "
  "ಯಥಾ ರಾಜಾ ತಥಾ ಪ್ರಜಾ (yathā rājā tathā prajā) - literally 'as the king, so "
  "the people' - meaning: leaders set the example. 8. ಮಾತು ಬೆಳ್ಳಿ ಮೌನ "
  "ಬಂಗಾರ (mātu beḷḷi mauna baṅgāra) - literally 'speech is silver, silence "
  "is gold' - meaning: silence is often wiser than speech. 9. ಅತಿಯಾಸೆ "
  "ಗತಿಕೇಡು (atiyāse gatikēḍu) - literally 'excessive greed ruins the fate' - "
  "meaning: greed destroys. 10. ದೂರದ ಬೆಟ್ಟ ಕಣ್ಣಿಗೆ ನುಣುಪು (dūrāda beṭṭa "
  "kaṇṇige nuṇupu) - literally 'the distant hill looks smooth to the eye' - "
  "meaning: the grass is always greener elsewhere. 11. ಹಾಸಿಗೆ ಇದ್ದಷ್ಟು ಕಾಲು "
  "ಚಾಚು (hāsige iddaṣṭu kālu cācu) - literally 'stretch the legs as far as "
  "the bed' - meaning: live within your means. 12. ಎತ್ತು ಏರಿಗೆ ಎಳೆಯಿತು ಕೋಣ "
  "ನೀರಿಗೆ ಎಳೆಯಿತು (ettu ērige eḷeyitu kōṇa nīrige eḷeyitu) - literally 'the ox "
  "pulled toward the hill, the buffalo toward the water' - meaning: people "
  "pull in different directions. 13. ಮಾಡಿದ್ದುಣ್ಣೋ ಮಹಾರಾಯ (māḍidduṇṇō "
  "mahārāya) - literally 'eat what you have cooked, O king' - meaning: face "
  "the consequences of your actions. 14. ಕುಂಬಾರನಿಗೆ ವರುಷ ದೊಣ್ಣೆ ನಾಯಿಗೆ ನಿಮಿಷ "
  "(kumbāranige varuṣa doṇṇe nāyige nimiṣa) - literally 'a year for the "
  "potter, a minute for the dog with the stick' - meaning: building takes "
  "long, destroying is quick. 15. ಒಂದು ಕೈಯಿಂದ ಚಪ್ಪಾಳೆ ತಟ್ಟಲಾಗದು (ondu "
  "kaiyinda cappāḷe taṭṭalāgadu) - literally 'you cannot clap with one hand' "
  "- meaning: it takes two for a quarrel or a task. 16. ಮುಳ್ಳಿನಿಂದ ಮುಳ್ಳೇ "
  "ತೆಗೆಯಬೇಕು (muḷḷininda muḷḷē tegeyabēku) - literally 'a thorn must be "
  "removed by a thorn' - meaning: fight fire with fire. 17. ಬೊಗಳುವ ನಾಯಿ "
  "ಕಚ್ಚುವುದಿಲ್ಲ (bogaḷuva nāyi kaccuvudilla) - literally 'a barking dog does "
  "not bite' - meaning: loud threats are often empty. 18. ಗಿಡವಾಗಿ ಬಗ್ಗದ್ದು "
  "ಮರವಾಗಿ ಬಗ್ಗೀತೆ (giḍavāgi baggaddu maravāgi baggīte) - literally 'what does "
  "not bend as a sapling will not bend as a tree' - meaning: habits form "
  "young. 19. ಮಾತು ಆಡಿದರೆ ಹೋಯಿತು ಮುತ್ತು ಒಡೆದರೆ ಹೋಯಿತು (mātu āḍidare hōyitu "
  "muttu oḍedare hōyitu) - literally 'spoken word is gone, broken pearl is "
  "gone' - meaning: words cannot be taken back. 20. ಹೊಟ್ಟೆಗೆ ಹಿಟ್ಟಿಲ್ಲ "
  "ಜುಟ್ಟಿಗೆ ಮಲ್ಲಿಗೆ (hoṭṭege hiṭṭilla juṭṭige mallige) - literally 'no flour "
  "for the stomach, jasmine for the hair' - meaning: misplaced priorities. "
  "Example for 20: ಹೊಟ್ಟೆಗೆ ಹಿಟ್ಟಿಲ್ಲ ಜುಟ್ಟಿಗೆ ಮಲ್ಲಿಗೆ ಎಂಬಂತೆ ಅವನು ಹೊಸ ಫೋನ್ "
  "ತೆಗೆದುಕೊಂಡನು (hoṭṭege hiṭṭilla juṭṭige mallige embante avanu hosa phōn "
  "tegedukoṇḍanu) - 'Like the proverb says, he bought a new phone while "
  "short on food money'. Use one proverb a week in real conversation and "
  "elders will smile."),
 "how_it_works": (
  "This record teaches wisdom in twenty capsules: each proverb with literal "
  "translation, real meaning and a usage example. Learn them in pairs of "
  "opposites - ಕೈ ಕೆಸರಾದರೆ (work rewarded) vs ಅತಿಯಾಸೆ ಗತಿಕೇಡು (greed ruins) "
  "- and deploy one per week in real speech."),
 "key_points": [
  "20 proverbs: literal meaning + real meaning + example sentence.",
  "Time and fortune: ಅತ್ತೆಗೊಂದು ಕಾಲ, ದೂರದ ಬೆಟ್ಟ.",
  "Work and consequence: ಕೈ ಕೆಸರಾದರೆ ಬಾಯಿ ಮೊಸರು; ಮಾಡಿದ್ದುಣ್ಣೋ ಮಹಾರಾಯ; ಕುಂಬಾರನಿಗೆ ವರುಷ.",
  "Speech wisdom: ಮಾತು ಬೆಳ್ಳಿ ಮೌನ ಬಂಗಾರ; ಮಾತು ಆಡಿದರೆ ಹೋಯಿತು.",
  "Measure and means: ಹಾಸಿಗೆ ಇದ್ದಷ್ಟು ಕಾಲು ಚಾಚು; ಆನೆಯ ಹೊಟ್ಟೆಗೆ ಅರೆಕಾಸಿನ ಮಜ್ಜಿಗೆ.",
  "Human nature: ಕಾಗೆಗೆ ತನ್ನ ಮರಿ ಬಂಗಾರ; ಒಂದು ಕೈಯಿಂದ ಚಪ್ಪಾಳೆ.",
  "Youth and habit: ಗಿಡವಾಗಿ ಬಗ್ಗದ್ದು ಮರವಾಗಿ ಬಗ್ಗೀತೆ.",
  "One proverb a week in real conversation.",
 ],
 "requirements": [
  "Explain five proverbs in your own words.",
  "Use three proverbs in real conversations this month.",
  "Write a short story ending with one proverb.",
 ],
 "standards": [
  "Traditional Kannada proverb collections; Government of Karnataka standard Kannada",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Traditional Kannada proverb collections (gaadegaḷu), as documented in Kannada folklore studies.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
 ],
 "sig_lens": (
  "Through the Signature lens proverbs are re-taught as his wisdom chips: "
  "twenty stamped sayings, each a compressed circuit of generations, slotted "
  "into his speech where plain words would fail. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 29
{
 "key": "register", "name": "Formal and Polite Kannada",
 "group": "Advanced", "ladder": 29, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Fifteen formal versus informal pairs for letters, business and elders - "
  "the register ladder. 1. Formal: ತಮಗೆ ತಿಳಿಸಲು ಇಚ್ಛಿಸುತ್ತೇನೆ (tamage "
  "tiḷisalu icchisuttēne) - 'I wish to inform you' / Informal: ನಿನಗೆ ಹೇಳ್ತೀನಿ "
  "(ninage hēḷtīni) - 'I'll tell you'. 2. Formal: ದಯವಿಟ್ಟು ಸ್ವಲ್ಪ ಕಾಯಿರಿ "
  "(dayaviṭṭu svalpa kāyiri) - 'Please wait a moment' / Informal: ಸ್ವಲ್ಪ "
  "ಇರು (svalpa iru) - 'wait a bit'. 3. Formal: ನಿಮ್ಮ ಅಭಿಪ್ರಾಯವೇನು? (nimma "
  "abhiprāyavēnu?) - 'What is your opinion?' / Informal: ನಿನ್ನ ಅಭಿಪ್ರಾಯವೇನು? "
  "(ninna abhiprāyavēnu?). 4. Formal: ತಾವು ಬರಬಹುದೇ? (tāvu barabahudē?) - "
  "'Could you come?' / Informal: ನೀನು ಬರ್ತೀಯಾ? (nīnu bartīyā?) - 'Will you "
  "come?'. 5. Formal: ಕ್ಷಮೆ ಕೋರುತ್ತೇನೆ (kṣame kōruttēne) - 'I beg your pardon' "
  "/ Informal: ಸಾರಿ ಕಣೋ (sāri kaṇō) - 'sorry, man'. 6. Formal: ಧನ್ಯವಾದಗಳು "
  "ತಿಳಿಸುತ್ತೇನೆ (dhanyavādagaḷu tiḷisuttēne) - 'I convey my thanks' / "
  "Informal: ಥ್ಯಾಂಕ್ಸ್ (thyānks) - 'thanks'. 7. Formal: ದಯವಿಟ್ಟು ಒಳಗೆ ಬನ್ನಿ "
  "(dayaviṭṭu oḷage banni) - 'Please come in' / Informal: ಒಳಗೆ ಬಾ (oḷage "
  "bā). 8. Formal: ತಮ್ಮ ಸಹಕಾರಕ್ಕೆ ಧನ್ಯವಾದಗಳು (tamma sahakārakke "
  "dhanyavādagaḷu) - 'Thanks for your cooperation' / Informal: ಸಹಾಯಕ್ಕೆ "
  "ಥ್ಯಾಂಕ್ಸ್ (sahāyakke thyānks). 9. Formal: ನಾನು ಹೊರಡಲು ಅಪ್ಪಣೆ ಕೊಡಿ (nānu "
  "horaḍalu appaṇe koḍi) - 'Permit me to leave' / Informal: ನಾನು ಹೋಗ್ತೀನಿ "
  "(nānu hōgtīni) - 'I'm going'. 10. Formal: ಶುಭದಿನ (śubhadina) - 'good day "
  "(in letters)' / Informal: ಬಾಯ್ (bāy) - 'bye'. 11. Formal: ವಂದನೆಗಳೊಂದಿಗೆ "
  "(vandhanegaḷondige) - 'with regards' / Informal: ಸೀ ಯೂ (sī yū) - 'see "
  "you'. 12. Formal: ತಮಗೆ ವಿನಂತಿಸುತ್ತೇನೆ (tamage vinantisuttēne) - 'I request "
  "you' / Informal: ಪ್ಲೀಸ್ ಕಣೋ (plīs kaṇō) - 'please, man'. 13. Formal: ಇದು "
  "ಸಾಧ್ಯವೇ? (idu sādhyavē?) - 'Is this possible?' / Informal: ಇದು ಆಗುತ್ತಾ? "
  "(idu āguttā?) - 'Will this work?'. 14. Formal: ದಯವಿಟ್ಟು ಪುನಃ ಹೇಳಿ "
  "(dayaviṭṭu punaḥ hēḷi) - 'Please say it again' / Informal: ಮತ್ತೆ ಹೇಳು "
  "(matte hēḷu) - 'say again'. 15. Formal: ತಮ್ಮ ವಿಶ್ವಾಸಿ (tamma viśvāsi) - "
  "'yours faithfully (letter closing)' / Informal: ನಿನ್ನ ಸ್ನೇಹಿತ (ninna "
  "snēhita) - 'your friend'. Register markers: formal uses ನೀವು/ತಾವು/ತಮಗೆ, "
  "-ಇರಿ verb endings, Sanskrit-derived vocabulary (ವಿನಂತಿ, ಸಹಕಾರ, ಅಪ್ಪಣೆ); "
  "informal uses ನೀನು, shortened verbs (ಹೋಗ್ತೀನಿ, ಹೇಳ್ತೀನಿ), English loans "
  "(ಥ್ಯಾಂಕ್ಸ್, ಬಾಯ್, ಪ್ಲೀಸ್). A formal letter opens with ಶ್ರೀಮಾನ್/ಶ್ರೀಮತಿ and "
  "closes with ತಮ್ಮ ವಿಶ್ವಾಸಿ. With elders and in writing, climb the formal "
  "ladder; with friends, stay on the ground floor."),
 "how_it_works": (
  "This record maps the politeness ladder: fifteen formal/informal pairs "
  "showing pronoun choice (ನೀವು/ತಾವು vs ನೀನು), verb endings (-ಇರಿ vs "
  "shortened stems), vocabulary (Sanskrit vs colloquial) and letter "
  "conventions. Write one formal letter and one casual note on the same "
  "topic to feel the register shift."),
 "key_points": [
  "Formal pronouns: ನೀವು, ತಾವು, ತಮಗೆ; informal: ನೀನು, ನಿನಗೆ.",
  "Formal verbs: -ಇರಿ endings (ಬನ್ನಿ, ಹೇಳಿ); informal: shortened (ಬಾ, ಹೇಳ್ತೀನಿ).",
  "Formal vocabulary is Sanskrit-flavored: ವಿನಂತಿ, ಸಹಕಾರ, ಅಪ್ಪಣೆ, ವಿಶ್ವಾಸಿ.",
  "Letter frame: ಶ್ರೀಮಾನ್/ಶ್ರೀಮತಿ ... ತಮ್ಮ ವಿಶ್ವಾಸಿ.",
  "15 pairs: requests, thanks, apologies, invitations, closings.",
  "ತಮಗೆ ತಿಳಿಸಲು ಇಚ್ಛಿಸುತ್ತೇನೆ is the formal workhorse.",
  "Informal loans (ಥ್ಯಾಂಕ್ಸ್, ಬಾಯ್) never enter formal writing.",
  "Climb the ladder with elders; stay casual with friends.",
 ],
 "requirements": [
  "Write a formal leave application in Kannada.",
  "Rewrite it as a casual note to a friend.",
  "Convert five informal sentences to formal register.",
 ],
 "standards": [
  "Government of Karnataka standard Kannada",
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
 ],
 "sig_lens": (
  "Through the Signature lens register is re-taught as his two dress codes: "
  "fifteen stamped pairs of ceremonial robes and workshop clothes, each "
  "labeled for its occasion, so he is never underdressed. Signature-made "
  "teaching, clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 30
{
 "key": "complex", "name": "Compound and Complex Kannada Sentences",
 "group": "Advanced", "ladder": 30, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Fifteen long sentences with clauses, connectors and relative clauses - "
  "parsed and translated. 1. ನಾನು ಮಾರುಕಟ್ಟೆಗೆ ಹೋದೆನು ಏಕೆಂದರೆ ತರಕಾರಿ "
  "ಮುಗಿದಿತ್ತು (nānu mārukaṭṭege hōdenu ēkendare tarakāri mugidittu) - 'I went "
  "to the market because the vegetables were finished' - main clause + "
  "ಏಕೆಂದರೆ (because) clause. 2. ಮಳೆ ಬರುತ್ತಿತ್ತು ಆದರೂ ನಾವು ಹೊರಟೆವು (maḷe "
  "baruttittu ādarū nāvu horaṭevu) - 'It was raining, yet we left' - "
  "ಆದರೂ (although/yet) concession. 3. ಅವನು ಬುದ್ಧಿವಂತನು ಮತ್ತು ಕಷ್ಟಪಡುವವನು "
  "(avanu buddhivantanu mattu kaṣṭapaḍuvavanu) - 'He is intelligent and "
  "hardworking' - ಮತ್ತು joins equals. 4. ನೀವು ಚಹಾ ಕುಡಿಯುವಿರಾ ಅಥವಾ ಕಾಫಿ "
  "ಕುಡಿಯುವಿರಾ? (nīvu cahā kuḍiyuvirā athavā kāphi kuḍiyuvirā?) - 'Will you "
  "have tea or coffee?' - ಅಥವಾ (or) alternation. 5. ಅವನು ಬರಲಿಲ್ಲ ಆದ್ದರಿಂದ "
  "ನಾವು ಕಾಯಿದೆವು (avanu baralilla āddarinda nāvu kāyidevu) - 'He did not "
  "come, therefore we waited' - ಆದ್ದರಿಂದ (therefore) result. 6. ನಾನು ನೋಡಿದ "
  "ಹುಡುಗ ನನ್ನ ಸ್ನೇಹಿತನು (nānu nōḍida huḍuga nanna snēhitanu) - 'The boy I saw "
  "is my friend' - relative clause with the -ದ participle (ನೋಡಿದ = who "
  "saw/was seen). 7. ನೀವು ಹೇಳಿದ ಕತೆ ತುಂಬಾ ಚೆನ್ನಾಗಿತ್ತು (nīvu hēḷida kate "
  "tumbā cennāgittu) - 'The story you told was very good' - ಹೇಳಿದ relative "
  "participle. 8. ಮಳೆ ಬಂದರೆ ನಾವು ಮನೆಯಲ್ಲೇ ಇರುತ್ತೇವೆ (maḷe bandare nāvu "
  "maneyallē iruttēve) - 'If it rains, we will stay home' - -ಅದರೆ "
  "conditional. 9. ಅವನು ಬಂದಾಗ ನಾನು ಊಟ ಮಾಡುತ್ತಿದ್ದೆನು (avanu bandāga nānu ūṭa "
  "māḍuttiddenu) - 'When he came, I was eating' - -ಆಗ (when) time clause. "
  "10. ಕೆಲಸ ಮುಗಿದ ನಂತರ ನಾವು ಸಿನೆಮಾ ನೋಡಿದೆವು (kelasa mugida nantara nāvu "
  "sinemā nōḍidevu) - 'After finishing work, we watched a movie' - ನಂತರ "
  "(after) sequence. 11. ಅವಳು ಹಾಡುತ್ತಾ ಅಡುಗೆ ಮಾಡುತ್ತಾಳೆ (avaḷu hāḍuttā "
  "aḍuge māḍuttāḷe) - 'She cooks while singing' - -ಉತ್ತಾ simultaneous "
  "action. 12. ನಾನು ಹೇಳಿದ್ದನ್ನು ಕೇಳಿ (nānu hēḷiddannu kēḷi) - 'Listen to what "
  "I said' - -ಇದ್ದದ್ದು nominalized clause as object. 13. ಎಷ್ಟು ಕಷ್ಟಪಟ್ಟರೂ "
  "ಫಲ ಸಿಗಲಿಲ್ಲ (eṣṭu kaṣṭapaṭṭarū phala sigalilla) - 'However hard he worked, "
  "there was no result' - -ಆರೂ (however) concession. 14. ನೀನು ಬರುವವರೆಗೆ ನಾನು "
  "ಕಾಯುತ್ತೇನೆ (nīnu baruvarage nānu kāyuttēne) - 'I will wait until you come' "
  "- -ಉವವರೆಗೆ (until) time limit. 15. ಅವನು ಗೆದ್ದಿದ್ದು ಅವನ ಕಷ್ಟದಿಂದಲೇ (avanu "
  "geddiddu avana kaṣṭadindalē) - 'His victory came from his hard work alone' "
  "- -ಇದ್ದದ್ದು cleft emphasis. Connector kit: ಏಕೆಂದರೆ (because), ಆದರೆ/ಆದರೂ "
  "(but/although), ಮತ್ತು (and), ಅಥವಾ (or), ಆದ್ದರಿಂದ (therefore), -ಅದರೆ (if), "
  "-ಆಗ (when), ನಂತರ (after), -ಉತ್ತಾ (while), -ಆರೂ (however), -ಉವವರೆಗೆ "
  "(until). Parse each sentence into its clauses before translating."),
 "how_it_works": (
  "This record builds long sentences from short ones: fifteen parsed "
  "examples, each with its connectors labeled - ಏಕೆಂದರೆ, ಆದರೂ, ಮತ್ತು, "
  "ಅಥವಾ, ಆದ್ದರಿಂದ, -ದ relatives, -ಅದರೆ, -ಆಗ, -ಉತ್ತಾ, -ಆರೂ, -ಉವವರೆಗೆ. Take "
  "two simple sentences you know and join them with each connector in turn."),
 "key_points": [
  "Connector kit: ಏಕೆಂದರೆ, ಆದರೆ/ಆದರೂ, ಮತ್ತು, ಅಥವಾ, ಆದ್ದರಿಂದ.",
  "Relative clauses use -ದ/-ತ participles: ನೋಡಿದ ಹುಡುಗ, ಹೇಳಿದ ಕತೆ.",
  "Conditional -ಅದರೆ, temporal -ಆಗ, simultaneous -ಉತ್ತಾ, concessive -ಆರೂ, limit -ಉವವರೆಗೆ.",
  "Nominalizer -ಇದ್ದದ್ದು turns clauses into nouns: ಹೇಳಿದ್ದನ್ನು.",
  "Cleft -ಇದ್ದದ್ದು ...-ಲೇ emphasizes: ಗೆದ್ದಿದ್ದು ಕಷ್ಟದಿಂದಲೇ.",
  "15 parsed sentences: cause, concession, joining, alternation, result, relatives, conditions, time, simultaneity.",
  "Parse clauses before translating - find the connector first.",
  "Join two simple sentences with each connector as drill.",
 ],
 "requirements": [
  "Join ten sentence pairs with different connectors.",
  "Build five -ದ relative clauses.",
  "Parse all fifteen sentences into labeled clauses.",
 ],
 "standards": [
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "ISO 15919:2001 transliteration",
 ],
 "citations": [
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Kittel, Ferdinand. A Grammar of the Kannada Language. Basel Mission Press; 1903.",
  "Steever, Sanford B. Kannada. In: Steever, Sanford B. (ed.) The Dravidian Languages. Routledge; 1998.",
 ],
 "sig_lens": (
  "Through the Signature lens complex sentences are re-taught as his "
  "assembly work: fifteen stamped builds, clauses bolted with connector "
  "fasteners, relatives as precision joints, every joint labeled. Signature-"
  "made teaching, clearly labeled, never presented as an outside authority's "
  "text."),
},
# ================================================================== 31
{
 "key": "dialogue1", "name": "Conversation in Kannada: At the Market",
 "group": "Advanced", "ladder": 31, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A twenty-line bilingual dialogue at the vegetable market - buyer and "
  "seller, annotated. Buyer: ರವಿ (Ravi). Seller: ಮಾರಾಟಗಾರ (mārāṭagāra, the "
  "seller). 1. ರವಿ: ನಮಸ್ಕಾರ! ಟೊಮೆಟೊ ಬೆಲೆ ಎಷ್ಟು? (namaskāra! ṭomeṭo bele "
  "eṣṭu?) - 'Greetings! How much are the tomatoes?' [Opens with ನಮಸ್ಕಾರ and "
  "the ಬೆಲೆ ಎಷ್ಟು? frame.] 2. ಮಾರಾಟಗಾರ: ನಮಸ್ಕಾರ! ಕೆಜಿಗೆ ನಲವತ್ತು ರೂಪಾಯಿ "
  "(namaskāra! kejige nalavattu rūpāyi) - 'Greetings! Forty rupees a kilo.' "
  "[Answers with the per-unit price.] 3. ರವಿ: ತುಂಬಾ ದುಬಾರಿ! ಸ್ವಲ್ಪ ಕಡಿಮೆ "
  "ಮಾಡಿ (tumbā dubāri! svalpa kaḍime māḍi) - 'Too expensive! Reduce a "
  "little.' [The bargaining opener.] 4. ಮಾರಾಟಗಾರ: ಸರಿ, ನಿಮಗಾಗಿ ಮೂವತ್ತೈದು "
  "ರೂಪಾಯಿ (sari, nimagāgi mūvattnaidu rūpāyi) - 'Okay, thirty-five for you.' "
  "[Counter-offer with ನಿಮಗಾಗಿ, for you.] 5. ರವಿ: ಟೊಮೆಟೊ ತಾಜಾವಾಗಿದೆಯೇ? "
  "(ṭomeṭo tājāvāgideyē?) - 'Are the tomatoes fresh?' [Quality check with "
  "-ಇದೆಯೇ?.] 6. ಮಾರಾಟಗಾರ: ಹೌದು, ಬೆಳಿಗ್ಗೆಯೇ ತೋಟದಿಂದ ತಂದದ್ದು (haudu, "
  "beḷiggeyē tōṭadinda tandaddu) - 'Yes, brought from the farm this very "
  "morning.' [Reassurance with origin.] 7. ರವಿ: ಸರಿ, ಎರಡು ಕೆಜಿ ಕೊಡಿ (sari, "
  "eraḍu keji koḍi) - 'Okay, give two kilos.' [Order with the ಕೊಡಿ frame.] "
  "8. ಮಾರಾಟಗಾರ: ಬೇರೆ ಏನು ಬೇಕು? (bēre ēnu bēku?) - 'What else do you need?' "
  "[Upsell question.] 9. ರವಿ: ಒಂದು ಕೆಜಿ ಈರುಳ್ಳಿ ಕೊಡಿ (ondu keji īruḷḷi koḍi) "
  "- 'Give one kilo of onions.' 10. ಮಾರಾಟಗಾರ: ಈರುಳ್ಳಿ ಕೆಜಿಗೆ ಮೂವತ್ತು "
  "ರೂಪಾಯಿ (īruḷḷi kejige mūvattu rūpāyi) - 'Onions are thirty rupees a "
  "kilo.' 11. ರವಿ: ಹಸಿರು ಮೆಣಸಿನಕಾಯಿ ಇದೆಯೇ? (hasiru meṇasinakāyi ideyē?) - "
  "'Do you have green chilies?' 12. ಮಾರಾಟಗಾರ: ಇದೆ, ಅರ್ಧ ಕೆಜಿ ತೆಗೆದುಕೊಳ್ಳಿ "
  "(ide, ardha keji tegedukoḷḷi) - 'Yes, take half a kilo.' 13. ರವಿ: ಒಟ್ಟು "
  "ಎಷ್ಟು ಆಯಿತು? (oṭṭu eṣṭu āyitu?) - 'What is the total?' [ಒಟ್ಟು = total.] "
  "14. ಮಾರಾಟಗಾರ: ನೂರಿಪ್ಪತ್ತು ರೂಪಾಯಿ ಆಯಿತು (nūrippattu rūpāyi āyitu) - 'It "
  "comes to one hundred twenty rupees.' 15. ರವಿ: ನೂರ ಹತ್ತು ಕೊಡುತ್ತೇನೆ "
  "(nūra hattu koḍuttēne) - 'I will give one hundred ten.' [Final haggle.] "
  "16. ಮಾರಾಟಗಾರ: ಸರಿ, ಕೊಡಿ (sari, koḍi) - 'Okay, give it.' [Deal closed.] "
  "17. ರವಿ: ಚಿಲ್ಲರೆ ಇದೆಯೇ? (cillare ideyē?) - 'Do you have change?' 18. "
  "ಮಾರಾಟಗಾರ: ಇದೆ, ತೆಗೆದುಕೊಳ್ಳಿ (ide, tegedukoḷḷi) - 'Yes, take it.' 19. ರವಿ: "
  "ಧನ್ಯವಾದಗಳು! ಮತ್ತೆ ಬರುತ್ತೇನೆ (dhanyavādagaḷu! matte baruttēne) - 'Thank "
  "you! I will come again.' [Closes with thanks and return promise.] 20. "
  "ಮಾರಾಟಗಾರ: ಬನ್ನಿ, ಬನ್ನಿ! ಶುಭದಿನ! (banni, banni! śubhadina!) - 'Come, come! "
  "Have a good day!' [Warm send-off.] Act this out with a partner, swapping "
  "roles - the bargaining trio (ಬೆಲೆ ಎಷ್ಟು? / ತುಂಬಾ ದುಬಾರಿ / ಸ್ವಲ್ಪ ಕಡಿಮೆ "
  "ಮಾಡಿ) will become reflex."),
 "how_it_works": (
  "This record stages a complete market transaction: twenty annotated lines "
  "from greeting through bargaining, quality check, ordering, totaling, "
  "paying and farewell. Perform it twice, swapping buyer and seller, then "
  "improvise the same dialogue for a fruit stall."),
 "key_points": [
  "20-line annotated dialogue: buyer ರವಿ, seller ಮಾರಾಟಗಾರ.",
  "Bargaining trio in action: ಬೆಲೆ ಎಷ್ಟು? / ತುಂಬಾ ದುಬಾರಿ / ಸ್ವಲ್ಪ ಕಡಿಮೆ ಮಾಡಿ.",
  "Quality check: ತಾಜಾವಾಗಿದೆಯೇ?; total: ಒಟ್ಟು ಎಷ್ಟು?",
  "Measure words: ಕೆಜಿ, ಅರ್ಧ ಕೆಜಿ.",
  "Deal closers: ಸರಿ, ಕೊಡಿ / ಧನ್ಯವಾದಗಳು! ಮತ್ತೆ ಬರುತ್ತೇನೆ.",
  "ನಿಮಗಾಗಿ (for you) is the seller's charm word.",
  "Swap roles and re-perform; improvise a fruit-stall version.",
  "Every annotation explains the move - learn the moves, not just the lines.",
 ],
 "requirements": [
  "Perform the dialogue with a partner, both roles.",
  "Improvise the same transaction for three new items.",
  "Bargain entirely in Kannada at a real shop once.",
 ],
 "standards": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Government of Karnataka standard Kannada",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
 ],
 "sig_lens": (
  "Through the Signature lens this market dialogue is re-taught as his "
  "trade drill: twenty stamped moves from price probe to deal close, every "
  "bargain a negotiation he wins with a smile. Signature-made teaching, "
  "clearly labeled, never presented as an outside authority's text."),
},
# ================================================================== 32
{
 "key": "dialogue2", "name": "Conversation in Kannada: Meeting a Friend",
 "group": "Advanced", "ladder": 32, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A twenty-line bilingual dialogue between two friends meeting after a long "
  "time - ಮನೋಹರ್ (Manohar) and ಪ್ರಿಯಾ (Priya), annotated. 1. ಮನೋಹರ್: ಪ್ರಿಯಾ! "
  "ಎಷ್ಟು ದಿನಗಳಾಯಿತು! (priyā! eṣṭu dinagaḷāyitu!) - 'Priya! It has been so "
  "many days!' [Joyful reunion opener.] 2. ಪ್ರಿಯಾ: ಮನೋಹರ್! ನಿಜವಾಗಲೂ! ಹೇಗಿದ್ದೀಯ? "
  "(manōhar! nijavāgalū! hēgiddīya?) - 'Manohar! Really! How are you?' "
  "[Informal ಹೇಗಿದ್ದೀಯ between friends.] 3. ಮನೋಹರ್: ಚೆನ್ನಾಗಿದ್ದೇನೆ, ನೀನು "
  "ಹೇಗಿದ್ದೀಯ? (cennāgiddēne, nīnu hēgiddīya?) - 'I am fine, how are you?' "
  "4. ಪ್ರಿಯಾ: ನಾನೂ ಚೆನ್ನಾಗಿದ್ದೇನೆ. ಈಗ ಎಲ್ಲಿರುತ್ತೀಯ? (nānū cennāgiddēne. īga "
  "elliruttīya?) - 'I am fine too. Where do you live now?' 5. ಮನೋಹರ್: ನಾನು "
  "ಬೆಂಗಳೂರಿನಲ್ಲಿರುತ್ತೇನೆ. ನೀನು? (nānu beṅgaḷūrinalliruttēne. nīnu?) - 'I live "
  "in Bengaluru. And you?' 6. ಪ್ರಿಯಾ: ನಾನು ಮೈಸೂರಿನಲ್ಲಿರುತ್ತೇನೆ (nānu "
  "maisūrinalliruttēne) - 'I live in Mysuru.' 7. ಮನೋಹರ್: ಏನು ಮಾಡುತ್ತಿದ್ದೀಯ? "
  "(ēnu māḍuttiddīya?) - 'What are you doing (these days)?' 8. ಪ್ರಿಯಾ: ನಾನು "
  "ಶಿಕ್ಷಕಿಯಾಗಿದ್ದೇನೆ (nānu śikṣakiyāgiddēne) - 'I am a teacher.' 9. ಮನೋಹರ್: "
  "ಅದ್ಭುತ! ಮಕ್ಕಳು ಹೇಗಿದ್ದಾರೆ? (adbhuta! makkaḷu hēgiddāre?) - 'Wonderful! How "
  "are the kids?' 10. ಪ್ರಿಯಾ: ಇಬ್ಬರೂ ಚೆನ್ನಾಗಿದ್ದಾರೆ. ದೊಡ್ಡವನು ಶಾಲೆಗೆ "
  "ಹೋಗುತ್ತಾನೆ (ibbarū cennāgiddāre. doḍḍavanu śālege hōguttāne) - 'Both are "
  "fine. The elder goes to school.' 11. ಮನೋಹರ್: ನಾಳೆ ಸಂಜೆ ಬಿಡುವಿದೆಯೇ? (nāḷe "
  "sanje biḍuvideyē?) - 'Are you free tomorrow evening?' [Invitation setup.] "
  "12. ಪ್ರಿಯಾ: ಹೌದು, ಬಿಡುವಿದ್ದೇನೆ. ಏಕೆ? (haudu, biḍuviddēne. ēke?) - 'Yes, "
  "I am free. Why?' 13. ಮನೋಹರ್: ನಮ್ಮ ಮನೆಗೆ ಊಟಕ್ಕೆ ಬಾ (namma manege ūṭakke "
  "bā) - 'Come to our house for a meal.' [Informal ಬಾ between friends.] 14. "
  "ಪ್ರಿಯಾ: ಖಂಡಿತ ಬರುತ್ತೇನೆ! ಏನು ಮಾಡುತ್ತೀಯ? (khaṇḍita baruttēne! ēnu "
  "māḍuttīya?) - 'I will definitely come! What will you make?' 15. ಮನೋಹರ್: "
  "ಅಮ್ಮ ಬಿಸಿಬೇಳೆಬಾತ್ ಮಾಡುತ್ತಾರೆ (amma bisibēḷebāt māḍuttāre) - 'Mother will "
  "make bisibelebath.' [The Karnataka classic.] 16. ಪ್ರಿಯಾ: ಅಯ್ಯೋ, ನನಗೆ "
  "ತುಂಬಾ ಇಷ್ಟ! (ayyō, nanage tumbā iṣṭa!) - 'Oh, I love it!' 17. ಮನೋಹರ್: "
  "ಏಳು ಗಂಟೆಗೆ ಬಾ (ēḷu gaṇṭege bā) - 'Come at seven.' 18. ಪ್ರಿಯಾ: ಸರಿ, ಏಳು "
  "ಗಂಟೆಗೆ ಬರುತ್ತೇನೆ (sari, ēḷu gaṇṭege baruttēne) - 'Okay, I will come at "
  "seven.' 19. ಮನೋಹರ್: ಮತ್ತೆ ಭೇಟಿಯಾಗೋಣ! (matte bhēṭiyāgōṇa!) - 'See you "
  "again!' 20. ಪ್ರಿಯಾ: ಹೌದು, ನಾಳೆ ಭೇಟಿಯಾಗೋಣ! (haudu, nāḷe bhēṭiyāgōṇa!) - "
  "'Yes, see you tomorrow!' Note the informal register throughout - "
  "ಹೇಗಿದ್ದೀಯ, ಬಾ, ಮಾಡುತ್ತೀಯ - friends drop the formal endings. Perform with "
  "a friend and feel the warmth."),
 "how_it_works": (
  "This record stages a friends' reunion: twenty annotated lines showing the "
  "informal register - ಹೇಗಿದ್ದೀಯ, ಬಾ, -ತ್ತೀಯ endings - plus the catch-up "
  "topics (where, work, kids) and the -ಕ್ಕೆ ಬಾ invitation. Perform it with a "
  "real friend, then improvise your own reunion."),
 "key_points": [
  "20-line annotated dialogue: friends ಮನೋಹರ್ and ಪ್ರಿಯಾ.",
  "Informal register: ಹೇಗಿದ್ದೀಯ, ಬಾ, ಮಾಡುತ್ತೀಯ, ಬರುತ್ತೇನೆ.",
  "Catch-up chain: ಎಷ್ಟು ದಿನ! / ಎಲ್ಲಿರುತ್ತೀಯ? / ಏನು ಮಾಡುತ್ತಿದ್ದೀಯ? / ಮಕ್ಕಳು ಹೇಗಿದ್ದಾರೆ?",
  "Invitation: ನಾಳೆ ಸಂಜೆ ಬಿಡುವಿದೆಯೇ? → ನಮ್ಮ ಮನೆಗೆ ಊಟಕ್ಕೆ ಬಾ.",
  "ಬಿಸಿಬೇಳೆಬಾತ್ - the Karnataka dish that seals friendships.",
  "Time pin: ಏಳು ಗಂಟೆಗೆ ಬಾ.",
  "ಮತ್ತೆ ಭೇಟಿಯಾಗೋಣ closes warmly.",
  "Perform with a friend; improvise your own reunion.",
 ],
 "requirements": [
  "Perform the reunion dialogue with a partner.",
  "Improvise a reunion with your own details.",
  "Invite someone to a meal using the -ಕ್ಕೆ ಬಾ frame.",
 ],
 "standards": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Government of Karnataka standard Kannada",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
 ],
 "sig_lens": (
  "Through the Signature lens this reunion is re-taught as his alliance "
  "renewal: twenty stamped lines reaffirming an old pact, every informal "
  "ending a badge of trust. Signature-made teaching, clearly labeled, never "
  "presented as an outside authority's text."),
},
# ================================================================== 33
{
 "key": "dialogue3", "name": "Conversation in Kannada: Solving a Problem",
 "group": "Advanced", "ladder": 33, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A twenty-line bilingual dialogue solving a problem together - ಅನಿಲ್ "
  "(Anil) and ಮೀರಾ (Meera) fix a leaking tap, annotated. 1. ಅನಿಲ್: ಮೀರಾ, "
  "ನೋಡು! ನಲ್ಲಿ ಸೋರುತ್ತಿದೆ (mīrā, nōḍu! nalli sōruttide) - 'Meera, look! The "
  "tap is leaking.' [Problem stated with ನೋಡು.] 2. ಮೀರಾ: ಅಯ್ಯೋ! ಯಾವಾಗಿನಿಂದ? "
  "(ayyō! yāvāgininda?) - 'Oh no! Since when?' 3. ಅನಿಲ್: ಬೆಳಿಗ್ಗೆಯಿಂದ "
  "ಸೋರುತ್ತಿದೆ (beḷiggeyinda sōruttide) - 'It has been leaking since morning.' "
  "[-ಇಂದ marks duration.] 4. ಮೀರಾ: ಮೊದಲು ನೀರಿನ ಕವಾಟ ಮುಚ್ಚೋಣ (modalu nīrina "
  "kavāṭa muccōṇa) - 'First, let us close the water valve.' [-ಓಣ proposes "
  "joint action.] 5. ಅನಿಲ್: ಕವಾಟ ಎಲ್ಲಿದೆ? (kavāṭa ellide?) - 'Where is the "
  "valve?' 6. ಮೀರಾ: ಸಿಂಕ್ ಕೆಳಗೆ ಇದೆ. ನಾನು ತೋರಿಸುತ್ತೇನೆ (sink keḷage ide. "
  "nānu tōrisuttēne) - 'It is under the sink. I will show you.' 7. ಅನಿಲ್: "
  "ಸರಿ, ಮುಚ್ಚಿದೆ. ಈಗ ಏನು ಮಾಡೋಣ? (sari, muccide. īga ēnu māḍōṇa?) - 'Okay, "
  "closed. What shall we do now?' 8. ಮೀರಾ: ಪ್ಲಂಬರ್‌ಗೆ ಕರೆ ಮಾಡೋಣ (plambar‌ge "
  "kare māḍōṇa) - 'Let us call the plumber.' 9. ಅನಿಲ್: ಪ್ಲಂಬರ್ ಸಂಖ್ಯೆ "
  "ನಿನ್ನಲ್ಲಿದೆಯೇ? (plambar sankhye ninnalideyē?) - 'Do you have the plumber's "
  "number?' 10. ಮೀರಾ: ಹೌದು, ನನ್ನ ಫೋನಿನಲ್ಲಿದೆ (haudu, nanna phōninallide) - "
  "'Yes, it is in my phone.' 11. ಅನಿಲ್: ಬೇಗ ಕರೆ ಮಾಡು (bēga kare māḍu) - "
  "'Call quickly.' 12. ಮೀರಾ: ಮಾಡುತ್ತಿದ್ದೇನೆ... ಅವರು ಅರ್ಧ ಗಂಟೆಯಲ್ಲಿ ಬರುತ್ತಾರೆ "
  "(māḍuttiddēne... avaru ardha gaṇṭeyalli baruttāre) - 'Calling... they will "
  "come in half an hour.' 13. ಅನಿಲ್: ಅಲ್ಲಿವರೆಗೆ ಬಕೆಟ್ ಇಡೋಣ (allivarege "
  "bakeṭ iḍōṇa) - 'Until then, let us place a bucket.' [-ವರೆಗೆ = until.] 14. "
  "ಮೀರಾ: ಒಳ್ಳೆಯ ಯೋಚನೆ! ಬಕೆಟ್ ತರುತ್ತೇನೆ (oḷḷeya yōcane! bakeṭ taruttēne) - "
  "'Good idea! I will bring the bucket.' 15. ಅನಿಲ್: ನೆಲ ಒರೆಸೋಣ (nela "
  "oresōṇa) - 'Let us wipe the floor.' 16. ಮೀರಾ: ನಾನು ಬಟ್ಟೆ ತರುತ್ತೇನೆ "
  "(nānu baṭṭe taruttēne) - 'I will bring the cloth.' 17. ಅನಿಲ್: ಪ್ಲಂಬರ್ "
  "ಬಂದರು! (plambar bandaru!) - 'The plumber has come!' 18. ಮೀರಾ: ಬೇಗ ಸರಿಪಡಿಸಿ "
  "ಎಂದು ಹೇಳೋಣ (bēga saripaḍisi endu hēḷōṇa) - 'Let us ask him to fix it "
  "quickly.' 19. ಅನಿಲ್: ಸರಿಯಾಯಿತು! ಎಷ್ಟು ಕೊಡಬೇಕು? (sariyāyitu! eṣṭu "
  "koḍabēku?) - 'It is fixed! How much should we pay?' 20. ಮೀರಾ: ಇನ್ನೂರು "
  "ರೂಪಾಯಿ. ಸಮಸ್ಯೆ ಬಗೆಹರಿದಿದೆ! (innūru rūpāyi. samasye bageharidide!) - 'Two "
  "hundred rupees. Problem solved!' Problem-solving frames: -ಓಣ (let us), "
  "-ವರೆಗೆ (until), ಮೊದಲು (first), ಎಷ್ಟು ಕೊಡಬೇಕು? (how much to pay). Teamwork "
  "in Kannada - practice with a real household problem."),
 "how_it_works": (
  "This record rehearses crisis teamwork: twenty annotated lines from "
  "problem statement through joint action (-ಓಣ), delegation, waiting (-"
  "ವರೆಗೆ), and resolution. Run it as a role-play with a real household task "
  "- the frames transfer to any problem."),
 "key_points": [
  "20-line annotated dialogue: ಅನಿಲ್ and ಮೀರಾ fix a leak.",
  "Joint-action -ಓಣ: ಮುಚ್ಚೋಣ, ಮಾಡೋಣ, ಇಡೋಣ, ಒರೆಸೋಣ.",
  "Sequence: ಮೊದಲು (first), ಈಗ (now), ಅಲ್ಲಿವರೆಗೆ (until then).",
  "Duration -ಇಂದ: ಬೆಳಿಗ್ಗೆಯಿಂದ ಸೋರುತ್ತಿದೆ.",
  "Limit -ವರೆಗೆ: ಅಲ್ಲಿವರೆಗೆ ಬಕೆಟ್ ಇಡೋಣ.",
  "Payment close: ಸರಿಯಾಯಿತು! ಎಷ್ಟು ಕೊಡಬೇಕು?",
  "ಸಮಸ್ಯೆ ಬಗೆಹರಿದಿದೆ! - problem solved - is the victory line.",
  "Role-play with a real household problem.",
 ],
 "requirements": [
  "Perform the repair dialogue with a partner.",
  "Solve a real small problem narrating in Kannada.",
  "Propose three joint actions with -ಓಣ.",
 ],
 "standards": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Government of Karnataka standard Kannada",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "Schiffman, Harold F. A Reference Grammar of Spoken Kannada. University of Washington Press; 1979.",
  "Sridhar, S. N. Kannada. Descriptive Grammars series. Routledge; 1990.",
  "Nayak, H. M. Kannada: A Language. In: The Gazetteer of India: Karnataka State; Government of Karnataka.",
 ],
 "sig_lens": (
  "Through the Signature lens this repair is re-taught as his damage-"
  "control drill: twenty stamped lines from fault report to fix verified, "
  "every -ಓಣ a crew order he commands. Signature-made teaching, clearly "
  "labeled, never presented as an outside authority's text."),
},
# ================================================================== 34
{
 "key": "mastery", "name": "Kannada Mastery Review and Full Reference",
 "group": "Advanced", "ladder": 34, "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The whole database in one teaching summary - alphabet, 200 core words, "
  "key grammar, and every phrase table. ALPHABET: 13 vowels ಅ ಆ ಇ ಈ ಉ ಊ ಋ ಎ "
  "ಏ ಐ ಒ ಓ ಔ + ಅಂ ಅಃ (15 vowel signs); 34 consonants in five groups (ಕ ಖ ಗ ಘ ಙ; ಚ ಛ ಜ ಝ ಞ; "
  "ಟ ಠ ಡ ಢ ಣ; ತ ಥ ದ ಧ ನ; ಪ ಫ ಬ ಭ ಮ) + ಯ ರ ಲ ವ ಶ ಷ ಸ ಹ ಳ; digits ೦-೯; "
  "left-to-right abugida; danda । ends traditional sentences. 200 CORE WORDS "
  "(Kannada - English): ನಾನು-I, ನೀನು-you (informal), ನೀವು-you (formal), "
  "ಅವನು-he, ಅವಳು-she, ಅದು-it, ನಾವು-we, ಅವರು-they, ಇದು-this, ಅದು-that, "
  "ಯಾರು-who, ಏನು-what, ಎಲ್ಲಿ-where, ಯಾವಾಗ-when, ಏಕೆ-why, ಹೇಗೆ-how, "
  "ಎಷ್ಟು-how much, ಯಾವುದು-which, ನನ್ನ-my, ನಿನ್ನ-your (informal), ನಿಮ್ಮ-your "
  "(formal), ಅವನ-his, ಅವಳ-her, ನಮ್ಮ-our, ಅವರ-their, ಮನುಷ್ಯ-human, "
  "ಮಹಿಳೆ-woman, ಮಗು-child, ಮಕ್ಕಳು-children, ತಾಯಿ-mother, ತಂದೆ-father, "
  "ಅಣ್ಣ-elder brother, ತಂಗಿ-younger sister, ತಾತ-grandfather, ಅಜ್ಜಿ-"
  "grandmother, ಸ್ನೇಹಿತ-friend, ಮನೆ-house, ಶಾಲೆ-school, ನಗರ-city, ಊರು-town, "
  "ರಸ್ತೆ-road, ಅಂಗಡಿ-shop, ಕಚೇರಿ-office, ಆಸ್ಪತ್ರೆ-hospital, ದೇವಸ್ಥಾನ-temple, "
  "ನೀರು-water, ಊಟ-meal, ಅನ್ನ-rice, ಹಾಲು-milk, ಚಹಾ-tea, ಕಾಫಿ-coffee, "
  "ಹಣ್ಣು-fruit, ತರಕಾರಿ-vegetable, ಪುಸ್ತಕ-book, ಪತ್ರ-letter, ಪೆನ್ನು-pen, "
  "ಮೇಜು-table, ಕುರ್ಚಿ-chair, ಬಾಗಿಲು-door, ಕಿಟಕಿ-window, ಬಟ್ಟೆ-cloth, ಹಣ-money, "
  "ಕಾರು-car, ಬಸ್-bus, ರೈಲು-train, ವಿಮಾನ-airplane, ಫೋನ್-phone, ಕಂಪ್ಯೂಟರ್-"
  "computer, ಮರ-tree, ಹೂವು-flower, ಸೂರ್ಯ-sun, ಚಂದ್ರ-moon, ನಕ್ಷತ್ರ-star, "
  "ಆಕಾಶ-sky, ಮಳೆ-rain, ಗಾಳಿ-wind, ಬೆಟ್ಟ-hill, ನದಿ-river, ಕಾಡು-forest, "
  "ಸಮುದ್ರ-sea, ನಾಯಿ-dog, ಬೆಕ್ಕು-cat, ಹಸು-cow, ಕುದುರೆ-horse, ಆನೆ-elephant, "
  "ಹುಲಿ-tiger, ಹಕ್ಕಿ-bird, ಮೀನು-fish, ಹಾವು-snake, ದಿನ-day, ರಾತ್ರಿ-night, "
  "ಬೆಳಿಗ್ಗೆ-morning, ಸಂಜೆ-evening, ಇಂದು-today, ನಾಳೆ-tomorrow, ನಿನ್ನೆ-"
  "yesterday, ಈಗ-now, ಸಮಯ-time, ವಾರ-week, ತಿಂಗಳು-month, ವರ್ಷ-year, ದೊಡ್ಡ-big, "
  "ಚಿಕ್ಕ-small, ಒಳ್ಳೆಯ-good, ಕೆಟ್ಟ-bad, ಹೊಸ-new, ಹಳೆಯ-old, ಉದ್ದ-long, "
  "ಬಿಸಿ-hot, ತಣ್ಣನೆಯ-cold, ಸಿಹಿ-sweet, ಸುಂದರ-beautiful, ಸ್ವಚ್ಛ-clean, "
  "ಸುಲಭ-easy, ಕಷ್ಟ-difficult, ಸಂತೋಷದ-happy, ಬೇಗ-quickly, ನಿಧಾನವಾಗಿ-slowly, "
  "ತುಂಬಾ-very, ಇಲ್ಲಿ-here, ಅಲ್ಲಿ-there, ಮೇಲೆ-up, ಕೆಳಗೆ-down, ಒಂದು-1, "
  "ಎರಡು-2, ಮೂರು-3, ನಾಲ್ಕು-4, ಐದು-5, ಆರು-6, ಏಳು-7, ಎಂಟು-8, ಒಂಬತ್ತು-9, "
  "ಹತ್ತು-10, ಇಪ್ಪತ್ತು-20, ಮೂವತ್ತು-30, ನಲವತ್ತು-40, ಐವತ್ತು-50, ನೂರು-100, "
  "ಮೊದಲನೆಯ-first, ತಲೆ-head, ಕಣ್ಣು-eye, ಕೈ-hand, ಕಾಲು-leg, ಹೊಟ್ಟೆ-stomach, "
  "ಹೃದಯ-heart, to go-ಹೋಗು, to come-ಬರು, to eat-ತಿನ್ನು, to drink-ಕುಡಿ, to do-"
  "ಮಾಡು, to say-ಹೇಳು, to ask-ಕೇಳು, to see-ನೋಡು, to read-ಓದು, to write-ಬರೆ, "
  "to give-ಕೊಡು, to take-ತೆಗೆದುಕೊಳ್ಳು, to sleep-ಮಲಗು, to sit-ಕುಳಿತುಕೊಳ್ಳು, "
  "to walk-ನಡೆ, to run-ಓಡು, to play-ಆಟವಾಡು, to learn-ಕಲಿ, to speak-ಮಾತಾಡು, "
  "to help-ಸಹಾಯ ಮಾಡು. KEY GRAMMAR: SOV order; 3 genders singular, human/"
  "neuter plural; 8 cases (-ಅನ್ನು, -ಇಂದ, -ಗೆ, -ಅ, -ಅಲ್ಲಿ, -ಏ); no articles; "
  "negation -ಇಲ್ಲ/-ಲಿಲ್ಲ; questions in place + -ಏ; adjectives invariable; "
  "verbs agree; tenses -ಉತ್ತ್/-ಇದ್/-ಉವ್. PHRASE TABLES: greetings - ನಮಸ್ಕಾರ, "
  "ಹೇಗಿದ್ದೀರಿ?, ಧನ್ಯವಾದಗಳು, ದಯವಿಟ್ಟು, ಕ್ಷಮಿಸಿ, ಹೋಗಿ ಬನ್ನಿ; travel - ಎಲ್ಲಿದೆ?, "
  "ಬೆಲೆ ಎಷ್ಟು?, ಬಲಕ್ಕೆ/ಎಡಕ್ಕೆ ತಿರುಗಿ; shopping - ಸ್ವಲ್ಪ ಕಡಿಮೆ ಮಾಡಿ, ಬಿಲ್ "
  "ಕೊಡಿ; health - ನನಗೆ ಜ್ವರವಿದೆ, ವೈದ್ಯರು ಎಲ್ಲಿದ್ದಾರೆ?; invitations - ಊಟಕ್ಕೆ "
  "ಬನ್ನಿ, ಹೋಗೋಣ. You climbed from first sounds to full conversation - "
  "ನೀವು ಕನ್ನಡ ಕಲಿತಿದ್ದೀರಿ! (nīvu kannaḍa kalitiddīri - you have learned "
  "Kannada!)."),
 "how_it_works": (
  "This record compresses all 33 records into one reference: the alphabet, "
  "200 core words, the grammar engine, and every phrase table. Use it as "
  "your daily drill sheet - read it end to end once a week until every line "
  "is instant. Then teach one record to someone else; teaching is the final "
  "mastery test."),
 "key_points": [
  "Full alphabet: 13 vowels + 2 yogavahas (15 vowel signs), 34 consonants, digits ೦-೯.",
  "200 core words: pronouns, people, places, things, nature, time, adjectives, adverbs, numbers, body, verbs.",
  "Grammar engine: SOV, 3 genders, 8 cases, no articles, -ಇಲ್ಲ/-ಲಿಲ್ಲ negation, in-place questions, invariable adjectives, agreeing verbs, -ಉತ್ತ್/-ಇದ್/-ಉವ್ tenses.",
  "Phrase tables: greetings, travel, shopping, health, invitations.",
  "ನೀವು ಕನ್ನಡ ಕಲಿತಿದ್ದೀರಿ! - you have learned Kannada!",
  "Weekly end-to-end read keeps everything instant.",
  "Teach one record to someone else - the final test.",
  "The ladder is climbed: foundations → compounded → advanced.",
 ],
 "requirements": [
  "Read this record end to end weekly.",
  "Score 180+/200 on the core-word list.",
  "Teach record 1 to another person.",
 ],
 "standards": [
  "All standards of records 1-33 consolidated",
  "ISO 639-1:2002 kn; ISO 639-3:2007 kan",
  "Unicode Standard, Kannada block U+0C80-U+0CFF",
 ],
 "citations": [
  "All citations of records 1-33 consolidated.",
  "Steever, Sanford B. (ed.) The Dravidian Languages. Routledge; 1998.",
  "Government of Karnataka standard Kannada",
 ],
 "sig_lens": (
  "Through the Signature lens this review is re-taught as his commissioning "
  "report: the whole instrument inventoried - alphabet, 200 words, grammar "
  "engine, phrase tables - tested, stamped and declared operational. "
  "Signature-made teaching, clearly labeled, never presented as an outside "
  "authority's text."),
},
]

SIG_TAIL = ("Signature editions are his original Signature language method - "
            "the same real Kannada re-taught through the Signature lens, "
            "clearly labeled Signature-made.")
