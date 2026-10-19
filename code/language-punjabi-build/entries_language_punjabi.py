#!/usr/bin/env python3
"""Entry content for The Punjabi to English Database (language-punjabi)
and its Signature edition (language-punjabi-signature).

34 ladder-ordered records (ladder_rank 1-10, non-decreasing; tiers
foundations -> compounded -> advanced), each a full fully-formed file per
the 2026-10-09 full-file canon: Punjabi content in Gurmukhi plus a plain
practical transliteration plus English translation plus example sentences.
Sentences are required in EVERY record.

Public records are real, fact-checked Punjabi teaching (public-harvest).
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
"name": "Punjabi Language Overview",
"group": "overview",
"ladder_rank": 1,
"ladder_tier": "foundations",
"description": (
"Punjabi (ਪੰਜਾਬੀ, transliterated 'panjabi') is an Indo-Aryan language of the "
"Indo-European family, spoken natively by about 125 million people, which makes "
"it one of the ten most-spoken native languages in the world. It is the official "
"language of the Indian state of Punjab and a major provincial language of "
"Pakistan's Punjab province, and it is carried worldwide by one of the largest "
"diasporas on earth - millions of speakers in Canada, the United Kingdom, the "
"United States, and Australia. In India Punjabi is written in the Gurmukhi script "
"(ਗੁਰਮੁਖੀ, 'gurmukhi'), developed from the Landa scripts and standardized by Guru "
"Angad in the 16th century; in Pakistan it is most often written in Shahmukhi, a "
"Perso-Arabic script. The standard literary dialect is Majhi, spoken around "
"Amritsar and Lahore, with major regional dialects including Malwai, Doabi, "
"Pothohari, and Multani. Punjabi is a tonal language - one of the few Indo-Aryan "
"languages with lexical tone - and its grammar runs on subject-object-verb word "
"order, two genders, postpositions instead of prepositions, and an ergative "
"pattern in the completed past."),
"how_it_works": (
"Punjabi builds meaning the way most Indo-Aryan languages do, but with its own "
"signature moves. Sentences run subject-object-verb: ਮੈਂ ਰੋਟੀ ਖਾਂਦਾ ਹਾਂ (main roti "
"khaanda haan - 'I bread eat am') means 'I am eating bread.' Nouns carry one of two "
"genders and change form with number; adjectives agree with the noun they describe; "
"verbs agree with the subject in the present but with the object in the completed "
"past (the ergative pattern); relationships that English marks with prepositions "
"(in, on, to) are marked with postpositions that follow the noun - ਘਰ ਵਿੱਚ (ghar "
"vich - 'house in') means 'in the house.' Pitch does word-level work: the same "
"syllable spoken with a high-falling tone versus a low-rising tone can be a "
"different word. The 34 records of this database climb that whole system step by "
"step: script and sound first, then words, then sentences, then real conversation, "
"then the full reference."),
"key_points": [
"Punjabi (ਪੰਜਾਬੀ, ISO 639-1 pa, ISO 639-3 pan) is Indo-European > Indo-Iranian > Indo-Aryan.",
"About 125 million native speakers: top-ten native language worldwide.",
"Official language of Indian Punjab; major provincial language of Pakistan's Punjab.",
"Two scripts: Gurmukhi in India (ਗੁਰਮੁਖੀ), Shahmukhi (Perso-Arabic) in Pakistan.",
"Standard dialect is Majhi; regional dialects include Malwai, Doabi, Pothohari, Multani.",
"Lexically tonal: three tones - high-falling, level, low-rising.",
"Word order is subject-object-verb; postpositions follow the noun.",
"Two genders (masculine, feminine) and two numbers (singular, plural).",
"Ergative pattern: in the completed past the verb agrees with the object, not the subject.",
"No articles: ਇੱਕ (ikk) means 'one' and does the work of 'a'.",
],
"requirements": [
"No prior knowledge of any South Asian language is needed to start.",
"Learn the Gurmukhi letters before memorizing long word lists.",
"Say every example sentence aloud - tone and aspiration are physical habits.",
],
"standards": [
"ISO 639-1: pa",
"ISO 639-3: pan",
"Unicode Gurmukhi block U+0A00-U+0A7F",
"Ethnologue language code pan",
],
"citations": [
"Ethnologue: Languages of the World - Punjabi (pan).",
"Shackle, Christopher. 'Punjabi.' In The Indo-Aryan Languages, edited by George Cardona and Dhanesh Jain, Routledge, 2003.",
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar. Routledge Descriptive Grammars, 1993.",
"The Unicode Standard - Gurmukhi block U+0A00-U+0A7F.",
],
"sig_lens": (
"His Signature reading: Punjabi is a covenant language - tonal where other "
"Indo-Aryan tongues are flat, ergative where they are straight, carrying two "
"scripts like two seals on one oath. The Signature Language Method treats every "
"tone as a signature stroke, every postposition as a handshake after the noun, "
"every dialect as a witness to the same original draft."),
},
# ------------------------------------------------------- 2 writing system
{
"key": "script",
"name": "Punjabi Writing System (Gurmukhi)",
"group": "script",
"ladder_rank": 1,
"ladder_tier": "foundations",
"description": (
"Punjabi in India is written in Gurmukhi (ਗੁਰਮੁਖੀ, 'from the mouth of the Guru'), "
"a left-to-right abugida where each consonant letter carries an inherent 'a' vowel "
"unless a vowel sign changes it. The alphabet is called the painti akhar - the "
"thirty-five letters. The traditional order begins with the three base letters "
"ਉ (ura), ਅ (aira), ੳ (iri), which carry vowel signs when a word starts with a "
"vowel, then ਸ (sassa) and ਹ (haha), then the five rows of stops: ਕ ਖ ਗ ਘ ਙ "
"(kakka, khakha, gagga, ghagga, nganga - k kh g gh ng), ਚ ਛ ਜ ਝ ਞ (chacha, chhachha, "
"jajja, jhajja, nyanya - ch chh j jh ny), ਟ ਠ ਡ ਢ ਣ (tainka, thatha, dadda, dhadha, "
"nana - retroflex t th d dh n), ਤ ਥ ਦ ਧ ਨ (tatta, thutha, dadda, dhudda, nanna - "
"dental t th d dh n), ਪ ਫ ਬ ਭ ਮ (pappa, phupha, babba, bhabha, mamma - p ph b bh m), "
"then ਯ ਰ ਲ ਵ (yaya, rarra, lalla, vava - y r l v), and finally ੜ (rarha - the "
"flapped retroflex rh). The ten vowels are ਅ ਆ ਇ ਈ ਉ ਊ ਏ ਐ ਓ ਔ (a aa i ee u oo e "
"ai o au). Vowel signs (lagaan matraan) attach to consonants: ਾ (aa), ਿ (i), ੀ "
"(ee), ੁ (u), ੂ (oo), ੇ (e), ੈ (ai), ੋ (o), ੌ (au), plus the nasalization marks "
"bindi (ਂ) and tippi (ੰ), the doubling mark addak (ੱ), and the vowel-killer halant "
"(੍). Perso-Arabic loan sounds add five dotted letters: ਖ਼ ਗ਼ ਜ਼ ਫ਼ ਲ਼ (kha gha za "
"fa lla). Punctuation uses the danda । (single) and double danda ॥ at sentence and "
"verse ends. Gurmukhi numerals are ੦ ੧ ੨ ੩ ੪ ੫ ੬ ੭ ੮ ੯ (0-9). Example: ਪੰਜਾਬੀ "
"reads 'panjabi' - ਪ (pa) + ਨ੍ (n, killed vowel) + ਜਾ (jaa) + ਬੀ (bee)."
),
"how_it_works": (
"Gurmukhi spells sound, not English letters, so read it as a sound map. A bare "
"consonant like ਕ is 'ka', not 'k' - add the sign ਿ and ਕੀ becomes 'kee'; add ੁ "
"and ਕੁ is 'ku'. The addak ੱ doubles the next consonant: ਪੱਕਾ (pakkaa, 'ripe, "
"certain') has a doubled k. Words never start with a bare vowel sign - the base "
"letters ਉ ਅ ੳ hold it: ਆਦਮੀ (aadmi, 'man') starts with ਅ + ਾ. The bindi and "
"tippi nasalize: ਹਾਂ (haan, 'yes') carries the bindi. Learn the five stop rows by "
"row - each row runs unaspirated, aspirated, voiced, voiced-aspirated, nasal - and "
"the whole script unlocks at once."
),
"key_points": [
"Gurmukhi is a left-to-right abugida: consonants carry an inherent 'a' vowel.",
"The painti akhar: 35 letters in a fixed traditional order starting with ਉ ਅ ੳ.",
"Five stop rows: velar (ਕ ਵਰਗ), palatal (ਚ ਵਰਗ), retroflex (ਟ ਵਰਗ), dental (ਤ ਵਰਗ), labial (ਪ ਵਰਗ).",
"Ten vowels: ਅ ਆ ਇ ਈ ਉ ਊ ਏ ਐ ਓ ਔ (a aa i ee u oo e ai o au).",
"Vowel signs (lagaan matraan) attach to consonants; base letters ਉ ਅ ੳ hold word-initial vowels.",
"Addak (ੱ) doubles the following consonant; bindi/tippi nasalize; halant (੍) kills the vowel.",
"Five dotted letters for Perso-Arabic loans: ਖ਼ ਗ਼ ਜ਼ ਫ਼ ਲ਼.",
"Danda । ends sentences; double danda ॥ ends verses.",
"Gurmukhi digits: ੦੧੨੩੪੫੬੭੮੯.",
"Example: ਪੰਜਾਬੀ = pa + n + jaa + bee = 'panjabi'.",
],
"requirements": [
"Practice writing each of the 35 letters by hand in the traditional order.",
"Drill the five stop rows aloud: k kh g gh ng, ch chh j jh ny, and so on.",
"Read the vowel signs on ਕ first (ਕਾ ਕਿ ਕੀ ਕੁ ਕੂ ਕੇ ਕੈ ਕੋ ਕੌ) before touching real words.",
],
"standards": [
"Unicode Gurmukhi block U+0A00-U+0A7F",
"ISO 15924 script code Guru",
"Traditional painti akhar ordering",
],
"citations": [
"The Unicode Standard - Gurmukhi block U+0A00-U+0A7F.",
"Shackle, Christopher. 'Punjabi.' In The Indo-Aryan Languages, Routledge, 2003.",
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: the painti akhar is a thirty-five-seal covenant - five "
"rows of five stops like five fingers of a hand, each row running plain, "
"breathed, voiced, voiced-and-breathed, nasal. The Signature Language Method "
"teaches the script as an armory: learn the rows and you hold every word the "
"language can make."),
},
# ------------------------------------------------------- 3 phonology
{
"key": "phonology",
"name": "Punjabi Pronunciation and Phonology",
"group": "sounds",
"ladder_rank": 2,
"ladder_tier": "foundations",
"description": (
"Punjabi sounds run on three pillars: vowels, consonants, and tone. The ten "
"vowels are ਅ (a, like 'u' in 'but'), ਆ (aa, like 'a' in 'father'), ਇ (i, like 'i' "
"in 'bit'), ਈ (ee, like 'ee' in 'feet'), ਉ (u, like 'u' in 'put'), ਊ (oo, like "
"'oo' in 'boot'), ਏ (e, like 'ay' in 'say'), ਐ (ai, like 'ai' in 'buy'), ਓ (o, "
"like 'o' in 'go'), ਔ (au, like 'ow' in 'cow'). Consonants include the five stop "
"rows with aspiration contrasts - ਕ (k) versus ਖ (kh, with a puff of air), ਚ (ch) "
"versus ਛ (chh) - plus retroflex ਟ ਠ ਡ ਢ ਣ (t th d dh n with the tongue curled "
"back), dental ਤ ਥ ਦ ਧ ਨ (t th d dh n with the tongue on the teeth), nasals, and "
"the flapped retroflex ੜ (rh). Punjabi is one of the few Indo-Aryan languages "
"with lexical tone: three tones - level, high-falling, and low-rising. The tones "
"come from history: old voiced aspirates (ਘ ਝ ਢ ਧ ਭ) lost their voicing and left "
"their breath behind as pitch. So ਘਰ (ghar, 'house') is spoken with a low-rising "
"tone on the first syllable, ਝੰਡਾ (jhanda, 'flag') the same, while ਕੋੜਾ (kora, "
"'whip') keeps a level tone and ਘੋੜਾ (ghora, 'horse') takes the low-rising tone "
"that marks it as different from ਕੋੜਾ. Stress generally falls on the last heavy "
"syllable. Twelve spoken examples: ਘਰ (ghar, house), ਪਾਣੀ (paani, water), ਕਿਤਾਬ "
"(kitaab, book), ਰੋਟੀ (roti, bread), ਚਾਹ (chaa, tea), ਦੋਸਤ (dost, friend), ਸਕੂਲ "
"(school, school), ਬੱਚਾ (baccha, child), ਸੂਰਜ (sooraj, sun), ਚੰਨ (chann, moon), "
"ਢੋਲ (dhol, drum), ਝੰਡਾ (jhanda, flag)."
),
"how_it_works": (
"Tone is the make-or-break habit. Say ਕੋੜਾ (kora, 'whip') flat and level; now say "
"ਘੋੜਾ (ghora, 'horse') starting low and rising on the first syllable - that rise "
"is the ghost of the old voiced 'gh'. Aspiration is the second habit: hold your "
"palm before your mouth - ਖ (kh), ਛ (chh), ਠ (th), ਥ (th), ਫ (ph) should puff air, "
"while ਕ ਚ ਟ ਤ ਪ should not. Retroflexes curl the tongue back to the hard palate; "
"dentals touch the teeth. Vowel length matters: ਇ (i, short) versus ਈ (ee, long) "
"can change a word. Drill the twelve example words above daily until the tones "
"come without thinking."
),
"key_points": [
"Ten vowels: five short-long pairs (a/aa, i/ee, u/oo) plus e, ai, o, au.",
"Aspiration contrast: k/kh, ch/chh, t/th, p/ph - puff of air versus none.",
"Retroflex row (ਟ ਵਰਗ) curls the tongue back; dental row (ਤ ਵਰਗ) touches the teeth.",
"Three lexical tones: level, high-falling, low-rising - rare in Indo-Aryan.",
"Tones descend from lost voiced aspirates (ਘ ਝ ਢ ਧ ਭ): ਘੋੜਾ (ghora, horse) vs ਕੋੜਾ (kora, whip).",
"Stress falls on the last heavy syllable.",
"Flapped retroflex ੜ (rh) is its own sound, not r + h.",
"Nasalization (bindi/tippi) changes meaning: ਹਾਂ (haan, yes) needs it.",
],
"requirements": [
"Practice the palm test for aspiration: kh chh th ph must move air.",
"Drill the tone pair ਕੋੜਾ/ਘੋੜਾ (kora/ghora) until the pitch difference is automatic.",
"Record yourself reading the twelve example words and compare with a native speaker.",
],
"standards": [
"IPA reference: Punjabi vowels /ə aː ɪ iː ʊ uː eː ɛː oː ɔː/",
"Three-tone analysis per Shackle 2003",
],
"citations": [
"Shackle, Christopher. 'Punjabi.' In The Indo-Aryan Languages, Routledge, 2003.",
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
"Gill, Harjit Singh and Gleason, Henry A. A Reference Grammar of Punjabi, 1969.",
],
"sig_lens": (
"His Signature reading: tone is the signature stroke of Punjabi - the breath of "
"the old voiced consonants, kept as pitch after the voicing died. The Signature "
"Language Method drills tone as oath-taking: flat for the level, falling for the "
"high, rising for the low, until the hand of the voice signs each word without "
"thinking."),
},
# ------------------------------------------------------- 4 core nouns I
{
"key": "nouns1",
"name": "Punjabi Core Nouns I",
"group": "words",
"ladder_rank": 2,
"ladder_tier": "foundations",
"description": (
"Twenty-five essential Punjabi nouns - person, place, and thing - each with its "
"gender (m = masculine, f = feminine), transliteration, English meaning, and one "
"example sentence with translation. Gender matters: it drives adjective and verb "
"agreement everywhere in the language. 1. ਪਾਣੀ (paani, m) water - ਮੈਂ ਪਾਣੀ ਪੀਂਦਾ "
"ਹਾਂ। (main paani peenda haan.) I drink water. 2. ਕਿਤਾਬ (kitaab, f) book - ਇਹ "
"ਮੇਰੀ ਕਿਤਾਬ ਹੈ। (eh meri kitaab hai.) This is my book. 3. ਘਰ (ghar, m) house - "
"ਮੇਰਾ ਘਰ ਵੱਡਾ ਹੈ। (mera ghar vadda hai.) My house is big. 4. ਸਕੂਲ (school, m) "
"school - ਬੱਚਾ ਸਕੂਲ ਜਾਂਦਾ ਹੈ। (baccha school jaanda hai.) The child goes to school. "
"5. ਰੋਟੀ (roti, f) bread - ਮਾਂ ਰੋਟੀ ਬਣਾਉਂਦੀ ਹੈ। (maan roti banaundi hai.) Mother "
"makes bread. 6. ਚਾਹ (chaa, f) tea - ਚਾਹ ਗਰਮ ਹੈ। (chaa garam hai.) The tea is hot. "
"7. ਦੋਸਤ (dost, m) friend - ਉਹ ਮੇਰਾ ਦੋਸਤ ਹੈ। (oh mera dost hai.) He is my friend. "
"8. ਮਾਂ (maan, f) mother - ਮਾਂ ਖੁਸ਼ ਹੈ। (maan khush hai.) Mother is happy. 9. ਪਿਉ "
"(pio, m) father - ਪਿਉ ਕੰਮ ਕਰਦਾ ਹੈ। (pio kamm karda hai.) Father works. 10. ਬੱਚਾ "
"(baccha, m) child - ਬੱਚਾ ਖੇਡਦਾ ਹੈ। (baccha khed da hai.) The child plays. 11. "
"ਗੱਡੀ (gaddi, f) car - ਗੱਡੀ ਤੇਜ਼ ਹੈ। (gaddi tez hai.) The car is fast. 12. ਰਸਤਾ "
"(rastaa, m) road - ਇਹ ਰਸਤਾ ਲੰਬਾ ਹੈ। (eh rastaa lamba hai.) This road is long. 13. "
"ਦੁਕਾਨ (dukaan, f) shop - ਦੁਕਾਨ ਬੰਦ ਹੈ। (dukaan band hai.) The shop is closed. 14. "
"ਬਾਜ਼ਾਰ (bazaar, m) market - ਬਾਜ਼ਾਰ ਭਰਿਆ ਹੈ। (bazaar bhariya hai.) The market is "
"crowded. 15. ਕੰਮ (kamm, m) work - ਕੰਮ ਮੁਸ਼ਕਲ ਹੈ। (kamm mushkal hai.) The work is "
"difficult. 16. ਖਾਣਾ (khaana, m) food/meal - ਖਾਣਾ ਤਿਆਰ ਹੈ। (khaana tiyaar hai.) "
"The food is ready. 17. ਦੁੱਧ (duddh, m) milk - ਦੁੱਧ ਠੰਡਾ ਹੈ। (duddh thanda hai.) "
"The milk is cold. 18. ਸਬਜ਼ੀ (sabzi, f) vegetable - ਸਬਜ਼ੀ ਤਾਜ਼ੀ ਹੈ। (sabzi taazi "
"hai.) The vegetable is fresh. 19. ਫਲ (phal, m) fruit - ਫਲ ਮਿੱਠਾ ਹੈ। (phal mittha "
"hai.) The fruit is sweet. 20. ਦਿਨ (din, m) day - ਅੱਜ ਚੰਗਾ ਦਿਨ ਹੈ। (ajj changa din "
"hai.) Today is a good day. 21. ਰਾਤ (raat, f) night - ਰਾਤ ਕਾਲੀ ਹੈ। (raat kaali "
"hai.) The night is dark. 22. ਸੂਰਜ (sooraj, m) sun - ਸੂਰਜ ਚਮਕਦਾ ਹੈ। (sooraj "
"chamakda hai.) The sun shines. 23. ਪੰਛੀ (panchhi, m) bird - ਪੰਛੀ ਉੱਡਦਾ ਹੈ। "
"(panchhi udda hai.) The bird flies. 24. ਕੁੱਤਾ (kutta, m) dog - ਕੁੱਤਾ ਭੌਂਕਦਾ ਹੈ। "
"(kutta bhaunkda hai.) The dog barks. 25. ਬਿੱਲੀ (billi, f) cat - ਬਿੱਲੀ ਸੌਂਦੀ ਹੈ। "
"(billi saundi hai.) The cat sleeps."
),
"how_it_works": (
"Every Punjabi noun has a gender, and the gender is not decoration - adjectives "
"and verbs bend to match it. ਮੇਰਾ ਘਰ (mera ghar, 'my house') uses ਮੇਰਾ because "
"ਘਰ is masculine; ਮੇਰੀ ਕਿਤਾਬ (meri kitaab, 'my book') uses ਮੇਰੀ because ਕਿਤਾਬ is "
"feminine. Feminine nouns often end in -ੀ (-ee): ਰੋਟੀ, ਚਾਹ, ਗੱਡੀ, ਬਿੱਲੀ. Learn "
"each noun with its gender the way you learn its meaning - say 'ਪਾਣੀ, masculine, "
"water' as one unit. The example sentences show the most common sentence frame in "
"the language: subject + description + ਹੈ (hai, 'is')."
),
"key_points": [
"25 essential nouns with gender, transliteration, meaning, and a translated sentence each.",
"Gender is grammatical: masculine or feminine, and it controls adjective and verb agreement.",
"Feminine nouns often end in -ੀ (-ee): roti, chaa, gaddi, billi.",
"ਮੇਰਾ (mera) goes with masculine nouns; ਮੇਰੀ (meri) with feminine nouns.",
"The frame 'X ਹੈ' (X hai) means 'X is' - the commonest sentence in the language.",
],
"requirements": [
"Memorize each noun together with its gender - never the word alone.",
"Say each example sentence aloud and swap in a different noun.",
],
"standards": [
"Gender classification per Bhatia 1993",
"Transliteration: plain practical romanization used across this database",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
"Gill, Harjit Singh and Gleason, Henry A. A Reference Grammar of Punjabi, 1969.",
],
"sig_lens": (
"His Signature reading: twenty-five foundation stones, each stamped with its "
"gender like a maker's mark. The Signature Language Method lays nouns first "
"because everything else in Punjabi - adjectives, verbs, pronouns - swears "
"allegiance to the noun's gender."),
},
# ------------------------------------------------------- 5 core verbs I
{
"key": "verbs1",
"name": "Punjabi Core Verbs I",
"group": "words",
"ladder_rank": 2,
"ladder_tier": "foundations",
"description": (
"Twenty-five essential Punjabi verbs in their dictionary form (the -ਣਾ/-ਨਾ "
"infinitive), each with transliteration, English meaning, and one example "
"sentence with translation. 1. ਕਰਨਾ (karna) to do - ਮੈਂ ਕੰਮ ਕਰਦਾ ਹਾਂ। (main kamm "
"karda haan.) I do the work. 2. ਜਾਣਾ (jaana) to go - ਉਹ ਸਕੂਲ ਜਾਂਦਾ ਹੈ। (oh school "
"jaanda hai.) He goes to school. 3. ਆਉਣਾ (aauna) to come - ਤੁਸੀਂ ਕਦੋਂ ਆਉਂਦੇ ਹੋ? "
"(tusin kadon aaunde ho?) When do you come? 4. ਖਾਣਾ (khaana) to eat - ਅਸੀਂ ਰੋਟੀ "
"ਖਾਂਦੇ ਹਾਂ। (asin roti khaande haan.) We eat bread. 5. ਪੀਣਾ (peena) to drink - ਮੈਂ "
"ਚਾਹ ਪੀਂਦੀ ਹਾਂ। (main chaa peendi haan.) I drink tea. (female speaker) 6. ਪੜ੍ਹਨਾ "
"(parhna) to read, to study - ਬੱਚਾ ਕਿਤਾਬ ਪੜ੍ਹਦਾ ਹੈ। (baccha kitaab parhda hai.) "
"The child reads a book. 7. ਲਿਖਣਾ (likhna) to write - ਉਹ ਚਿੱਠੀ ਲਿਖਦੀ ਹੈ। (oh "
"chitthi likhdi hai.) She writes a letter. 8. ਬੋਲਣਾ (bolna) to speak - ਕੀ ਤੁਸੀਂ "
"ਪੰਜਾਬੀ ਬੋਲਦੇ ਹੋ? (ki tusin panjaabi bolde ho?) Do you speak Punjabi? 9. ਸੁਣਨਾ "
"(sunna) to listen, to hear - ਮੈਂ ਗਾਣਾ ਸੁਣਦਾ ਹਾਂ। (main gaana sunda haan.) I "
"listen to a song. 10. ਦੇਖਣਾ (dekhna) to see, to watch - ਅਸੀਂ ਫਿਲਮ ਦੇਖਦੇ ਹਾਂ। "
"(asin film dekhde haan.) We watch a film. 11. ਲੈਣਾ (laina) to take - ਮੈਂ ਕਿਤਾਬ "
"ਲੈਂਦਾ ਹਾਂ। (main kitaab lainda haan.) I take the book. 12. ਦੇਣਾ (dena) to give - "
"ਉਹ ਮੈਨੂੰ ਪੈਸੇ ਦਿੰਦਾ ਹੈ। (oh mainun paise dinda hai.) He gives me money. 13. "
"ਬਣਾਉਣਾ (banauna) to make - ਮਾਂ ਖਾਣਾ ਬਣਾਉਂਦੀ ਹੈ। (maan khaana banaundi hai.) Mother "
"makes food. 14. ਬੈਠਣਾ (baithna) to sit - ਤੁਸੀਂ ਇੱਥੇ ਬੈਠੋ। (tusin itthe baitho.) "
"Please sit here. 15. ਉੱਠਣਾ (utthna) to get up - ਮੈਂ ਸਵੇਰੇ ਉੱਠਦਾ ਹਾਂ। (main savere "
"utthda haan.) I get up in the morning. 16. ਸੌਣਾ (sauna) to sleep - ਬੱਚਾ ਸੌਂਦਾ "
"ਹੈ। (baccha saunda hai.) The child sleeps. 17. ਚੱਲਣਾ (challna) to walk, to move - "
"ਅਸੀਂ ਪੈਦਲ ਚੱਲਦੇ ਹਾਂ। (asin paidal challde haan.) We walk on foot. 18. ਦੌੜਨਾ "
"(daurna) to run - ਮੁੰਡਾ ਤੇਜ਼ ਦੌੜਦਾ ਹੈ। (munda tez daurda hai.) The boy runs fast. "
"19. ਖਰੀਦਣਾ (khareedna) to buy - ਮੈਂ ਸਬਜ਼ੀ ਖਰੀਦਦਾ ਹਾਂ। (main sabzi khareedda "
"haan.) I buy vegetables. 20. ਵੇਚਣਾ (vechna) to sell - ਉਹ ਫਲ ਵੇਚਦਾ ਹੈ। (oh phal "
"vechda hai.) He sells fruit. 21. ਖੇਡਣਾ (khedna) to play - ਬੱਚੇ ਖੇਡਦੇ ਹਨ। (bacche "
"khedde han.) The children play. 22. ਸਿੱਖਣਾ (sikhna) to learn - ਮੈਂ ਪੰਜਾਬੀ "
"ਸਿੱਖਦਾ ਹਾਂ। (main panjaabi sikhda haan.) I learn Punjabi. 23. ਸਿਖਾਉਣਾ (sikhauna) "
"to teach - ਅਧਿਆਪਕ ਪੜ੍ਹਾਉਂਦਾ ਹੈ। (adhiaapak parhaunda hai.) The teacher teaches. "
"24. ਮਦਦ ਕਰਨਾ (madad karna) to help - ਕੀ ਮੈਂ ਤੁਹਾਡੀ ਮਦਦ ਕਰਾਂ? (ki main tuhadi madad "
"karaan?) May I help you? 25. ਪਿਆਰ ਕਰਨਾ (pyaar karna) to love - ਮੈਂ ਆਪਣੇ ਪਰਿਵਾਰ "
"ਨੂੰ ਪਿਆਰ ਕਰਦਾ ਹਾਂ। (main aapne parivaar nun pyaar karda haan.) I love my family."
),
"how_it_works": (
"Punjabi verbs are cited in the infinitive ending in -ਣਾ (-naa): ਕਰਨਾ (karna, 'to "
"do'). Drop the -ਣਾ to get the stem (ਕਰ, kar), then add endings for tense, person, "
"gender, and number. The present habitual adds -ਦਾ/-ਦੀ/-ਦੇ (-da/-dee/-de): ਮੈਂ "
"ਕਰਦਾ ਹਾਂ (main karda haan, 'I do' - male speaker), ਮੈਂ ਕਰਦੀ ਹਾਂ (main kardi haan, "
"'I do' - female speaker), ਉਹ ਕਰਦੇ ਹਨ (oh karde han, 'they do'). The auxiliary "
"ਹਾਂ/ਹੈ/ਹੋ/ਹਨ (haan/hai/ho/han) marks person: ਹਾਂ (haan) for ਮੈਂ, ਹੈ (hai) for "
"ਉਹ, ਹੋ (ho) for ਤੁਸੀਂ, ਹਨ (han) for plural ਉਹ. Compound verbs like ਮਦਦ ਕਰਨਾ "
"(madad karna, 'to help') pair a noun with ਕਰਨਾ - learn them as units."
),
"key_points": [
"25 essential verbs in the -ਣਾ infinitive, each with a translated sentence.",
"Stem = infinitive minus -ਣਾ: ਕਰਨਾ gives the stem ਕਰ (kar).",
"Present habitual endings: -ਦਾ (masculine singular), -ਦੀ (feminine singular), -ਦੇ (plural).",
"Auxiliaries mark person: ਹਾਂ (I), ਹੈ (he/she), ਹੋ (you formal), ਹਨ (they).",
"Female speakers use -ਦੀ forms: ਮੈਂ ਕਰਦੀ ਹਾਂ (main kardi haan).",
"Compound verbs pair a noun with ਕਰਨਾ: ਮਦਦ ਕਰਨਾ (to help), ਪਿਆਰ ਕਰਨਾ (to love).",
],
"requirements": [
"Memorize each verb in its infinitive and say its stem aloud.",
"Conjugate ਕਰਨਾ, ਜਾਣਾ, and ਖਾਣਾ in the present for all six persons.",
],
"standards": [
"Verb classification per Bhatia 1993",
"Infinitive citation form -ਣਾ",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
"Gill, Harjit Singh and Gleason, Henry A. A Reference Grammar of Punjabi, 1969.",
],
"sig_lens": (
"His Signature reading: twenty-five engine verbs - the moving parts of the "
"language. The Signature Language Method treats the stem as the engine block "
"and the endings as the gears: swap the gear and the same engine drives a man, "
"a woman, or a crowd."),
},
# ------------------------------------------------------- 6 adjectives/adverbs
{
"key": "adjadv",
"name": "Punjabi Adjectives and Adverbs",
"group": "words",
"ladder_rank": 3,
"ladder_tier": "foundations",
"description": (
"Twenty-five adjectives and fifteen adverbs, each with a translated example "
"sentence, plus the agreement rule that governs them all. Adjectives agree with "
"the noun in gender and number: ਵੱਡਾ (vadda, big - masculine) becomes ਵੱਡੀ "
"(vaddi) before a feminine noun and ਵੱਡੇ (vadde) before a plural. Adjectives: 1. "
"ਵੱਡਾ/ਵੱਡੀ (vadda/vaddi) big - ਇਹ ਵੱਡਾ ਘਰ ਹੈ। (eh vadda ghar hai.) This is a big "
"house. 2. ਛੋਟਾ/ਛੋਟੀ (chhota/chhoti) small - ਇਹ ਛੋਟੀ ਕਿਤਾਬ ਹੈ। (eh chhoti kitaab "
"hai.) This is a small book. 3. ਨਵਾਂ/ਨਵੀਂ (navaan/naveen) new - ਮੇਰੀ ਗੱਡੀ ਨਵੀਂ "
"ਹੈ। (meri gaddi naveen hai.) My car is new. 4. ਪੁਰਾਣਾ/ਪੁਰਾਣੀ (puraana/puraani) "
"old - ਇਹ ਪੁਰਾਣਾ ਰਸਤਾ ਹੈ। (eh puraana rastaa hai.) This is an old road. 5. ਅੱਛਾ/"
"ਅੱਛੀ (acchha/acchhi) good - ਉਹ ਅੱਛਾ ਮੁੰਡਾ ਹੈ। (oh acchha munda hai.) He is a good "
"boy. 6. ਬੁਰਾ/ਬੁਰੀ (bura/buri) bad - ਇਹ ਬੁਰੀ ਖ਼ਬਰ ਹੈ। (eh buri khabar hai.) This "
"is bad news. 7. ਗਰਮ (garam) hot - ਚਾਹ ਗਰਮ ਹੈ। (chaa garam hai.) The tea is hot. "
"8. ਠੰਡਾ/ਠੰਡੀ (thanda/thandi) cold - ਪਾਣੀ ਠੰਡਾ ਹੈ। (paani thanda hai.) The water "
"is cold. 9. ਮਿੱਠਾ/ਮਿੱਠੀ (mittha/mitthi) sweet - ਇਹ ਮਿੱਠਾ ਫਲ ਹੈ। (eh mittha phal "
"hai.) This is a sweet fruit. 10. ਕੌੜਾ/ਕੌੜੀ (kaura/kauri) bitter - ਇਹ ਦਵਾਈ ਕੌੜੀ "
"ਹੈ। (eh davaai kauri hai.) This medicine is bitter. 11. ਸੁੰਦਰ (sundar) beautiful "
"- ਉਹ ਸੁੰਦਰ ਕੁੜੀ ਹੈ। (oh sundar kurhi hai.) She is a beautiful girl. 12. ਲੰਬਾ/"
"ਲੰਬੀ (lamba/lambi) long, tall - ਉਹ ਲੰਬਾ ਆਦਮੀ ਹੈ। (oh lamba aadmi hai.) He is a "
"tall man. 13. ਖੁਸ਼ (khush) happy - ਮੈਂ ਅੱਜ ਖੁਸ਼ ਹਾਂ। (main ajj khush haan.) I am "
"happy today. 14. ਉਦਾਸ (udaas) sad - ਉਹ ਉਦਾਸ ਹੈ। (oh udaas hai.) He is sad. 15. "
"ਤੇਜ਼ (tez) fast - ਇਹ ਤੇਜ਼ ਗੱਡੀ ਹੈ। (eh tez gaddi hai.) This is a fast car. 16. "
"ਹੌਲੀ (hauli) slow - ਕੱਛੂ ਹੌਲੀ ਹੈ। (kachhoo hauli hai.) The tortoise is slow. 17. "
"ਸਾਫ਼ (saaf) clean - ਕਮਰਾ ਸਾਫ਼ ਹੈ। (kamraa saaf hai.) The room is clean. 18. ਗੰਦਾ/"
"ਗੰਦੀ (ganda/gandi) dirty - ਇਹ ਗੰਦੀ ਗਲੀ ਹੈ। (eh gandi gali hai.) This is a dirty "
"street. 19. ਅਮੀਰ (ameer) rich - ਉਹ ਅਮੀਰ ਆਦਮੀ ਹੈ। (oh ameer aadmi hai.) He is a "
"rich man. 20. ਗਰੀਬ (gareeb) poor - ਉਹ ਗਰੀਬ ਪਰਿਵਾਰ ਹੈ। (oh gareeb parivaar hai.) "
"That is a poor family. 21. ਮੁਸ਼ਕਲ (mushkal) difficult - ਇਹ ਕੰਮ ਮੁਸ਼ਕਲ ਹੈ। (eh "
"kamm mushkal hai.) This work is difficult. 22. ਆਸਾਨ (aasaan) easy - ਇਹ ਸਵਾਲ "
"ਆਸਾਨ ਹੈ। (eh savaal aasaan hai.) This question is easy. 23. ਸੱਚਾ/ਸੱਚੀ "
"(sachcha/sachchi) true - ਇਹ ਸੱਚੀ ਗੱਲ ਹੈ। (eh sachchi gall hai.) This is a true "
"thing. 24. ਝੂਠਾ/ਝੂਠੀ (jhootha/jhoothi) false - ਇਹ ਝੂਠੀ ਖ਼ਬਰ ਹੈ। (eh jhoothi "
"khabar hai.) This is false news. 25. ਤਿਆਰ (tiyaar) ready - ਖਾਣਾ ਤਿਆਰ ਹੈ। "
"(khaana tiyaar hai.) The food is ready. Adverbs (they never change form): 1. "
"ਬਹੁਤ (bahut) very - ਉਹ ਬਹੁਤ ਖੁਸ਼ ਹੈ। (oh bahut khush hai.) He is very happy. 2. "
"ਜਲਦੀ (jaldi) quickly - ਜਲਦੀ ਆਓ। (jaldi aao.) Come quickly. 3. ਹੌਲੀ ਹੌਲੀ (hauli "
"hauli) slowly - ਹੌਲੀ ਹੌਲੀ ਬੋਲੋ। (hauli hauli bolo.) Speak slowly. 4. ਅੱਜ (ajj) "
"today - ਮੈਂ ਅੱਜ ਆਵਾਂਗਾ। (main ajj aavaangaa.) I will come today. 5. ਕੱਲ੍ਹ "
"(kallh) tomorrow/yesterday - ਉਹ ਕੱਲ੍ਹ ਆਇਆ ਸੀ। (oh kallh aayaa see.) He came "
"yesterday. 6. ਹੁਣ (hun) now - ਹੁਣ ਚੱਲੀਏ। (hun challiye.) Let us go now. 7. ਫਿਰ "
"(phir) again, then - ਫਿਰ ਮਿਲਾਂਗੇ। (phir milaange.) We will meet again. 8. ਹਮੇਸ਼ਾ "
"(hamesha) always - ਉਹ ਹਮੇਸ਼ਾ ਸੱਚ ਬੋਲਦਾ ਹੈ। (oh hamesha sach bolda hai.) He always "
"speaks the truth. 9. ਕਦੇ (kade) sometimes - ਮੈਂ ਕਦੇ ਕਦੇ ਜਾਂਦਾ ਹਾਂ। (main kade "
"kade jaanda haan.) I go sometimes. 10. ਕਦੇ ਨਹੀਂ (kade nahin) never - ਮੈਂ ਕਦੇ "
"ਨਹੀਂ ਜਾਂਦਾ। (main kade nahin jaanda.) I never go. 11. ਇੱਥੇ (itthe) here - ਇੱਥੇ "
"ਬੈਠੋ। (itthe baitho.) Sit here. 12. ਉੱਥੇ (utthe) there - ਉੱਥੇ ਜਾਓ। (utthe jaao.) "
"Go there. 13. ਬਾਹਰ (baahar) outside - ਬਾਹਰ ਮੀਂਹ ਪੈ ਰਿਹਾ ਹੈ। (baahar meenh pai "
"rihaa hai.) It is raining outside. 14. ਅੰਦਰ (andar) inside - ਅੰਦਰ ਆਓ। (andar "
"aao.) Come inside. 15. ਸ਼ਾਇਦ (shaayad) maybe - ਸ਼ਾਇਦ ਉਹ ਆਵੇ। (shaayad oh aave.) "
"Maybe he will come. Agreement rule: adjectives ending in -ਾ (-aa) change to -ੀ "
"(-ee) for feminine singular and -ੇ (-e) for masculine plural: ਵੱਡਾ ਮੁੰਡਾ (vadda "
"munda, big boy), ਵੱਡੀ ਕੁੜੀ (vaddi kurhi, big girl), ਵੱਡੇ ਮੁੰਡੇ (vadde munde, big "
"boys). Adjectives not ending in -ਾ (ਗਰਮ, ਖੁਸ਼, ਤੇਜ਼, ਸਾਫ਼) never change."
),
"how_it_works": (
"Adjectives are chameleons and adverbs are stones. An -ਾ adjective takes three "
"shapes: ਵੱਡਾ (vadda) for masculine singular, ਵੱਡੀ (vaddi) for feminine singular, "
"ਵੱਡੇ (vadde) for masculine plural - the feminine plural usually matches the "
"feminine singular. Check the noun's gender first, then dress the adjective to "
"match: masculine ਘਰ (ghar) takes ਵੱਡਾ ਘਰ, feminine ਕਿਤਾਬ (kitaab) takes ਵੱਡੀ "
"ਕਿਤਾਬ. Adjectives that do not end in -ਾ - ਗਰਮ (garam), ਖੁਸ਼ (khush), ਤੇਜ਼ (tez) - "
"keep one shape forever. Adverbs never agree with anything: ਬਹੁਤ (bahut), ਜਲਦੀ "
"(jaldi), ਹੁਣ (hun) stay identical before any verb or adjective. Place the "
"adjective before the noun and the adverb before the word it sharpens."
),
"key_points": [
"25 adjectives + 15 adverbs, each with a translated example sentence.",
"Adjectives ending in -ਾ agree: -ਾ masculine singular, -ੀ feminine, -ੇ masculine plural.",
"ਵੱਡਾ ਮੁੰਡਾ (vadda munda), ਵੱਡੀ ਕੁੜੀ (vaddi kurhi), ਵੱਡੇ ਮੁੰਡੇ (vadde munde).",
"Adjectives not ending in -ਾ (garam, khush, tez, saaf) never change form.",
"Adverbs never change form and sit before the word they modify.",
"ਕੱਲ੍ਹ (kallh) means both yesterday and tomorrow - tense tells you which.",
],
"requirements": [
"Sort every new adjective into 'changes' (-ਾ ending) or 'never changes'.",
"Build ten noun phrases and check each adjective against the noun's gender.",
],
"standards": [
"Adjective agreement classes per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
"Gill, Harjit Singh and Gleason, Henry A. A Reference Grammar of Punjabi, 1969.",
],
"sig_lens": (
"His Signature reading: adjectives are the oath-takers of the noun phrase - "
"they swear the noun's gender and number before they are allowed to stand "
"beside it. The Signature Language Method drills the three shapes (ਵੱਡਾ/ਵੱਡੀ/"
"ਵੱਡੇ) as three seals: stamp the wrong one and the sentence is unsigned."),
},
# ------------------------------------------------------- 7 pronouns
{
"key": "pronouns",
"name": "Punjabi Pronouns",
"group": "words",
"ladder_rank": 3,
"ladder_tier": "foundations",
"description": (
"The full Punjabi pronoun system - personal, possessive, demonstrative, and "
"interrogative - with example sentences. Personal pronouns: ਮੈਂ (main, I) - ਮੈਂ "
"ਪੰਜਾਬੀ ਸਿੱਖਦਾ ਹਾਂ। (main panjaabi sikhda haan.) I learn Punjabi. ਤੂੰ (tun, you "
"- informal, singular, intimate) - ਤੂੰ ਕਿੱਥੇ ਜਾਂਦਾ ਹੈਂ? (tun kitthe jaanda hain?) "
"Where are you going? ਤੁਸੀਂ (tusin, you - formal or plural) - ਤੁਸੀਂ ਕਿਵੇਂ ਹੋ? "
"(tusin kiven ho?) How are you? ਉਹ (oh, he/she - near or far) - ਉਹ ਮੇਰਾ ਦੋਸਤ ਹੈ। "
"(oh mera dost hai.) He is my friend. ਅਸੀਂ (asin, we) - ਅਸੀਂ ਸਕੂਲ ਜਾਂਦੇ ਹਾਂ। (asin "
"school jaande haan.) We go to school. ਉਹ (oh, they) - ਉਹ ਖੇਡਦੇ ਹਨ। (oh khedde "
"han.) They play. Oblique forms (used before postpositions): ਮੈਨੂੰ/ਮੈਂ (mainun, "
"to me) - ਉਹ ਮੈਨੂੰ ਮਿਲਿਆ। (oh mainun miliyaa.) He met me. ਤੈਨੂੰ (tainun, to you "
"informal) - ਮੈਂ ਤੈਨੂੰ ਦੇਖਿਆ। (main tainun dekhiyaa.) I saw you. ਤੁਹਾਨੂੰ (tuhaanun, "
"to you formal) - ਮੈਂ ਤੁਹਾਨੂੰ ਦੱਸਾਂਗਾ। (main tuhaanun dassaangaa.) I will tell you. "
"ਉਸਨੂੰ (usnun, to him/her) - ਮੈਂ ਉਸਨੂੰ ਜਾਣਦਾ ਹਾਂ। (main usnun jaanda haan.) I know "
"him. ਸਾਨੂੰ (saanun, to us) - ਸਾਨੂੰ ਭੁੱਖ ਲੱਗੀ ਹੈ। (saanun bhukkh laggi hai.) We "
"are hungry. (literally 'to us hunger is attached') ਉਹਨਾਂ ਨੂੰ (uhnaan nun, to "
"them) - ਮੈਂ ਉਹਨਾਂ ਨੂੰ ਬੁਲਾਵਾਂਗਾ। (main uhnaan nun bulaavaangaa.) I will call "
"them. Possessive pronouns: ਮੇਰਾ/ਮੇਰੀ (mera/meri, my) - ਇਹ ਮੇਰੀ ਕਿਤਾਬ ਹੈ। (eh "
"meri kitaab hai.) This is my book. ਤੇਰਾ/ਤੇਰੀ (tera/teri, your - informal) - ਇਹ "
"ਤੇਰਾ ਘਰ ਹੈ। (eh tera ghar hai.) This is your house. ਤੁਹਾਡਾ/ਤੁਹਾਡੀ (tuhada/tuhadi, "
"your - formal) - ਤੁਹਾਡਾ ਨਾਂ ਕੀ ਹੈ? (tuhada naan ki hai?) What is your name? "
"ਉਸਦਾ/ਉਸਦੀ (usda/usdi, his/her) - ਇਹ ਉਸਦੀ ਗੱਡੀ ਹੈ। (eh usdi gaddi hai.) This is "
"her car. ਸਾਡਾ/ਸਾਡੀ (saada/saadi, our) - ਇਹ ਸਾਡਾ ਸਕੂਲ ਹੈ। (eh saada school hai.) "
"This is our school. ਉਹਨਾਂ ਦਾ (uhnaan da, their) - ਇਹ ਉਹਨਾਂ ਦਾ ਬਾਗ਼ ਹੈ। (eh uhnaan "
"da baagh hai.) This is their garden. Demonstratives: ਇਹ (eh, this/these) - ਇਹ "
"ਕੀ ਹੈ? (eh ki hai?) What is this? ਉਹ (oh, that/those) - ਉਹ ਕੌਣ ਹੈ? (oh kaun hai?) "
"Who is that? Interrogatives: ਕੌਣ (kaun, who) - ਕੌਣ ਆਇਆ? (kaun aayaa?) Who came? "
"ਕੀ (ki, what) - ਤੁਸੀਂ ਕੀ ਕਰਦੇ ਹੋ? (tusin ki karde ho?) What do you do? ਕਿਹੜਾ "
"(kihra, which) - ਕਿਹੜੀ ਕਿਤਾਬ? (kihri kitaab?) Which book? ਕਿੰਨਾ (kinna, how "
"much/many) - ਇਹ ਕਿੰਨੇ ਦਾ ਹੈ? (eh kinne da hai?) How much is this? Note: ਤੂੰ "
"(tun) is intimate - use ਤੁਸੀਂ (tusin) with strangers and elders; using ਤੂੰ with "
"an elder is rude."
),
"how_it_works": (
"Pronouns change shape with their job. ਮੈਂ (main, 'I') becomes ਮੈਨੂੰ (mainun) "
"when it receives the action: ਮੈਂ ਦੇਖਦਾ ਹਾਂ (main dekhda haan, 'I see') but ਉਹ "
"ਮੈਨੂੰ ਦੇਖਦਾ ਹੈ (oh mainun dekhda hai, 'he sees me'). The ergative ਨੇ (ne) "
"attaches to the oblique: ਮੈਂ ਨੇ (main ne, 'by me') in ਮੈਂ ਨੇ ਕਿਤਾਬ ਪੜ੍ਹੀ (main ne "
"kitaab parhi, 'I read the book'). Possessives agree like adjectives: ਮੇਰਾ ਘਰ "
"(mera ghar, masculine), ਮੇਰੀ ਕਿਤਾਬ (meri kitaab, feminine), ਮੇਰੇ ਦੋਸਤ (mere "
"dost, plural/oblique). The respect ladder runs ਤੂੰ (tun, intimate) < ਤੁਸੀਂ "
"(tusin, formal) - climb it with age and strangers, never down with elders. "
"Demonstratives double as third-person pronouns: ਉਹ (oh) is both 'that' and "
"'he/she/they' - context decides."
),
"key_points": [
"Full paradigms: personal, oblique, possessive, demonstrative, interrogative.",
"ਤੂੰ (tun) is intimate; ਤੁਸੀਂ (tusin) is formal/plural - never ਤੂੰ with elders.",
"Oblique forms before postpositions: ਮੈਨੂੰ (mainun), ਤੁਹਾਨੂੰ (tuhaanun), ਉਸਨੂੰ (usnun).",
"Ergative ਨੇ (ne) attaches to the oblique: ਮੈਂ ਨੇ ਕਿਤਾਬ ਪੜ੍ਹੀ (I read the book).",
"Possessives agree like adjectives: ਮੇਰਾ/ਮੇਰੀ/ਮੇਰੇ (mera/meri/mere).",
"ਉਹ (oh) covers he, she, it, they, that, those - context decides.",
"ਸਾਨੂੰ ਭੁੱਖ ਲੱਗੀ ਹੈ (saanun bhukkh laggi hai): 'to us hunger is attached' = we are hungry.",
],
"requirements": [
"Drill the respect ladder: practice every sentence in both ਤੂੰ and ਤੁਸੀਂ forms.",
"Learn each pronoun with its oblique form as a pair: ਮੈਂ/ਮੈਨੂੰ, ਤੁਸੀਂ/ਤੁਹਾਨੂੰ.",
],
"standards": [
"Pronoun paradigms per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
"Gill, Harjit Singh and Gleason, Henry A. A Reference Grammar of Punjabi, 1969.",
],
"sig_lens": (
"His Signature reading: pronouns are the identity seals of the sentence - ਮੈਂ "
"the self-seal, ਤੁਸੀਂ the respect-seal, ਉਹ the witness-seal. The Signature "
"Language Method teaches the oblique pairs as two sides of one coin: flip from "
"actor to receiver and the seal changes shape but never breaks."),
},
# ------------------------------------------------------- 8 numbers and time
{
"key": "numbers",
"name": "Punjabi Numbers and Time",
"group": "words",
"ladder_rank": 3,
"ladder_tier": "foundations",
"description": (
"Counting, telling time, and dating in Punjabi - every form with an example "
"sentence. Cardinals 1-10: ਇੱਕ (ikk, 1) - ਮੇਰੇ ਕੋਲ ਇੱਕ ਕਿਤਾਬ ਹੈ। (mere kol ikk "
"kitaab hai.) I have one book. ਦੋ (do, 2) - ਮੇਰੇ ਦੋ ਭਰਾ ਹਨ। (mere do bharaa han.) "
"I have two brothers. ਤਿੰਨ (tinn, 3) - ਤਿੰਨ ਦਿਨ ਹੋ ਗਏ। (tinn din ho gaye.) Three "
"days have passed. ਚਾਰ (chaar, 4) - ਚਾਰ ਵਜੇ ਮਿਲੋ। (chaar vaje milo.) Meet at four "
"o'clock. ਪੰਜ (panj, 5) - ਪੰਜ ਮਿੰਟ ਰੁਕੋ। (panj mint ruko.) Wait five minutes. ਛੇ "
"(chhe, 6) - ਛੇ ਮਹੀਨੇ ਲੱਗਣਗੇ। (chhe maheene laggan ge.) It will take six months. "
"ਸੱਤ (satt, 7) - ਹਫ਼ਤੇ ਵਿੱਚ ਸੱਤ ਦਿਨ ਹਨ। (hafte vich satt din han.) There are seven "
"days in a week. ਅੱਠ (atth, 8) - ਅੱਠ ਵਜੇ ਸਕੂਲ ਲੱਗਦਾ ਹੈ। (atth vaje school lagda "
"hai.) School starts at eight. ਨੌਂ (naun, 9) - ਨੌਂ ਬੱਚੇ ਖੇਡਦੇ ਹਨ। (naun bacche "
"khedde han.) Nine children are playing. ਦਸ (das, 10) - ਮੇਰੇ ਕੋਲ ਦਸ ਰੁਪਏ ਹਨ। "
"(mere kol das rupaye han.) I have ten rupees. Tens: ਵੀਹ (veeh, 20), ਤੀਹ (teeh, "
"30), ਚਾਲੀ (chaali, 40), ਪੰਜਾਹ (panjaah, 50), ਸੱਠ (satth, 60), ਸੱਤਰ (sattar, 70), "
"ਅੱਸੀ (assi, 80), ਨੱਬੇ (nabbe, 90), ਸੌ (sau, 100) - ਸੌ ਰੁਪਏ ਦਿਓ। (sau rupaye dio.) "
"Give a hundred rupees. ਹਜ਼ਾਰ (hazaar, 1000), ਲੱਖ (lakkh, 100,000). Ordinals: "
"ਪਹਿਲਾ (pahilaa, first), ਦੂਜਾ (doojaa, second), ਤੀਜਾ (teejaa, third) - ਉਹ ਪਹਿਲੇ "
"ਨੰਬਰ ਤੇ ਆਇਆ। (oh pahile number te aayaa.) He came first. Days: ਸੋਮਵਾਰ (somvaar, "
"Monday), ਮੰਗਲਵਾਰ (mangalvaar, Tuesday), ਬੁੱਧਵਾਰ (buddhvaar, Wednesday), ਵੀਰਵਾਰ "
"(veervaar, Thursday), ਸ਼ੁੱਕਰਵਾਰ (shukkarvaar, Friday), ਸ਼ਨੀਵਾਰ (shanivaar, "
"Saturday), ਐਤਵਾਰ (aitvaar, Sunday) - ਅੱਜ ਸੋਮਵਾਰ ਹੈ। (ajj somvaar hai.) Today is "
"Monday. Months: ਜਨਵਰੀ (janvari), ਫਰਵਰੀ (farvari), ਮਾਰਚ (maarch), ਅਪ੍ਰੈਲ (aprail), "
"ਮਈ (mai), ਜੂਨ (joon), ਜੁਲਾਈ (julaai), ਅਗਸਤ (agasat), ਸਤੰਬਰ (satambar), ਅਕਤੂਬਰ "
"(aktoobar), ਨਵੰਬਰ (navambar), ਦਸੰਬਰ (dasambar) - ਮੇਰਾ ਜਨਮਦਿਨ ਜੂਨ ਵਿੱਚ ਹੈ। (mera "
"janamdin joon vich hai.) My birthday is in June. Seasons: ਬਸੰਤ (basant, spring), "
"ਗਰਮੀ (garmi, summer), ਪੱਤਝੜ (pattjharh, autumn), ਸਰਦੀ (sardi, winter), ਬਰਸਾਤ "
"(barsaat, rainy season) - ਸਰਦੀ ਵਿੱਚ ਠੰਡ ਹੁੰਦੀ ਹੈ। (sardi vich thand hundi hai.) "
"It is cold in winter. Clock time: ਵਜੇ (vaje, o'clock) - ਤਿੰਨ ਵਜੇ (tinn vaje, 3 "
"o'clock); ਮਿੰਟ (mint, minute) - ਦਸ ਮਿੰਟ (das mint, ten minutes); ਘੰਟਾ (ghanta, "
"hour) - ਦੋ ਘੰਟੇ (do ghante, two hours); ਸਵੇਰ (saver, morning), ਦੁਪਹਿਰ (dupahir, "
"midday), ਸ਼ਾਮ (shaam, evening), ਰਾਤ (raat, night) - ਮੈਂ ਸਵੇਰੇ ਛੇ ਵਜੇ ਉੱਠਦਾ ਹਾਂ। "
"(main savere chhe vaje utthda haan.) I get up at six in the morning."
),
"how_it_works": (
"Numbers 1-10 and the tens are the bricks; teens and the numbers between tens "
"are built from them (ਇਕੀਹ ikkeeh 21, ਬੱਤੀ battee 32 - each with its own fused "
"form, learned as vocabulary). For time, put the number before ਵਜੇ (vaje): ਤਿੰਨ "
"ਵਜੇ (tinn vaje) is '3 o'clock'. Days of the week mostly end in -ਵਾਰ (-vaar) and "
"months match English with Punjabi spelling. Dates run day-month-year in speech: "
"ਪੰਜ ਜਨਵਰੀ (panj januari, '5 January'). ਕੀ ਵਜੇ ਹਨ? (ki vaje han?) asks 'what time "
"is it?' - answer with the number + ਵਜੇ. ਲੱਖ (lakkh, 100,000) is the South Asian "
"hundred-thousand - prices and populations count in lakhs, not hundred-thousands."
),
"key_points": [
"1-10: ikk, do, tinn, chaar, panj, chhe, satt, atth, naun, das - each with a sentence.",
"Tens: veeh, teeh, chaali, panjaah, satth, sattar, assi, nabbe, sau (100); hazaar (1000), lakkh (100,000).",
"Ordinals: pahilaa (first), doojaa (second), teejaa (third).",
"Seven days ending in -ਵਾਰ (-vaar); twelve months matching English.",
"Five seasons including ਬਰਸਾਤ (barsaat, the rainy season).",
"Time: number + ਵਜੇ (vaje) for o'clock; ਸਵੇਰ/ਦੁਪਹਿਰ/ਸ਼ਾਮ/ਰਾਤ for parts of day.",
"ਕੀ ਵਜੇ ਹਨ? (ki vaje han?) = what time is it?",
],
"requirements": [
"Count aloud 1-20, then by tens to 100, every day for a week.",
"Say today's full date in Punjabi every morning.",
],
"standards": [
"Number forms per Bhatia 1993",
"Gurmukhi digits ੦-੯",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: numbers are the measure-seals - ਇੱਕ to ਸੌ, each a notch "
"on the Signature measuring rod, with ਲੱਖ (lakkh) as the great South Asian "
"hundred-thousand seal. The Signature Language Method counts time as well as "
"things: ਵਜੇ stamps the hour, -ਵਾਰ stamps the week, and the speaker stamps the "
"day by speaking it."),
},
# ------------------------------------------------------- 9 greetings
{
"key": "greetings",
"name": "Punjabi Greetings and Everyday Phrases",
"group": "words",
"ladder_rank": 3,
"ladder_tier": "foundations",
"description": (
"Thirty greetings, farewells, and politeness phrases with usage notes. 1. ਸਤਿ "
"ਸ੍ਰੀ ਅਕਾਲ (sat sri akaal) - the universal Sikh/Punjabi greeting, hello - use "
"anytime, with anyone. 2. ਸਤਿ ਸ੍ਰੀ ਵਾਹਿਗੁਰੂ (sat sri vaahiguru) - a warmer, more "
"reverent greeting. 3. ਆਦਾਬ (aadaab) - the traditional Muslim Punjabi greeting. "
"4. ਨਮਸਤੇ (namaste) - respectful greeting, common with elders. 5. ਸਲਾਮ (salaam) "
"- short Muslim greeting. 6. ਕੀ ਹਾਲ ਹੈ? (ki haal hai?) - How are you? (informal) "
"7. ਤੁਸੀਂ ਕਿਵੇਂ ਹੋ? (tusin kiven ho?) - How are you? (formal) 8. ਸਭ ਠੀਕ ਹੈ? (sabh "
"theek hai?) - Is everything fine? 9. ਮੈਂ ਠੀਕ ਹਾਂ। (main theek haan.) - I am fine. "
"10. ਬਹੁਤ ਵਧੀਆ! (bahut vadheeyaa!) - Excellent! 11. ਧੰਨਵਾਦ (dhannvaad) - Thank "
"you. 12. ਬਹੁਤ ਬਹੁਤ ਧੰਨਵਾਦ (bahut bahut dhannvaad) - Thank you very much. 13. "
"ਮਾਫ਼ ਕਰੋ (maaf karo) - Sorry / excuse me (formal). 14. ਮਾਫ਼ ਕਰੀਂ (maaf kareen) - "
"Sorry (informal). 15. ਕੋਈ ਗੱਲ ਨਹੀਂ (koi gall nahin) - No problem / it is "
"nothing. 16. ਕਿਰਪਾ ਕਰਕੇ (kirpaa karke) - Please. 17. ਜੀ ਆਇਆਂ ਨੂੰ (ji aayaan "
"nun) - Welcome (formal, warm). 18. ਅਲਵਿਦਾ (alvida) - Goodbye (Muslim usage). 19. "
"ਰੱਬ ਰਾਖਾ (rabb raakha) - Goodbye, 'God keep you'. 20. ਫਿਰ ਮਿਲਾਂਗੇ (phir "
"milaange) - We will meet again. 21. ਚੰਗਾ, ਫਿਰ ਮਿਲਦੇ ਹਾਂ (changa, phir milde "
"haan) - OK, see you later. 22. ਸ਼ੁਭ ਸਵੇਰ (shubh saver) - Good morning. 23. ਸ਼ੁਭ "
"ਦੁਪਹਿਰ (shubh dupahir) - Good afternoon. 24. ਸ਼ੁਭ ਸ਼ਾਮ (shubh shaam) - Good "
"evening. 25. ਸ਼ੁਭ ਰਾਤਰੀ (shubh raatri) - Good night. 26. ਵਧਾਈ ਹੋਵੇ (vadhaai "
"hove) - Congratulations. 27. ਜਨਮਦਿਨ ਮੁਬਾਰਕ (janamdin mubaarak) - Happy "
"birthday. 28. ਖੁਸ਼ ਰਹੋ (khush raho) - Stay happy (elder's blessing). 29. ਜੁਗ ਜੁਗ "
"ਜੀਓ (jug jug jeeo) - Live long (elder's blessing to a child). 30. ਰੱਬ ਮੇਹਰ ਕਰੇ "
"(rabb mehar kare) - May God be kind (blessing). Usage notes: open with ਸਤਿ ਸ੍ਰੀ "
"ਅਕਾਲ among Sikhs and most Punjabis in India; ਆਦਾਬ/ਸਲਾਮ among Muslim Punjabis. "
"Always use ਜੀ (ji) after a name or 'yes' for respect: ਹਾਂ ਜੀ (haan ji, 'yes, "
"respected'). Blessings flow downward - elders bless, juniors receive."
),
"how_it_works": (
"Greetings are chosen by community and respect, not by the clock. ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ "
"(sat sri akaal) works morning, noon, and night - Punjabi does not require "
"time-based greetings the way English does, though ਸ਼ੁਭ ਸਵੇਰ (shubh saver) "
"exists for formal settings. Stack respect with ਜੀ (ji): ਹਾਂ ਜੀ (haan ji) for "
"'yes' to an elder, ਨਹੀਂ ਜੀ (nahin ji) for 'no'. Apology scales the same way: "
"ਮਾਫ਼ ਕਰੋ (maaf karo) to strangers, ਮਾਫ਼ ਕਰੀਂ (maaf kareen) to friends. Leave-"
"taking is a promise, not an end: ਫਿਰ ਮਿਲਾਂਗੇ (phir milaange, 'we will meet "
"again') keeps the door open."
),
"key_points": [
"30 greetings, farewells, and politeness phrases with usage notes.",
"ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ (sat sri akaal): the universal greeting; ਆਦਾਬ/ਸਲਾਮ: Muslim usage.",
"ਜੀ (ji) is the respect particle: ਹਾਂ ਜੀ, ਤੁਹਾਡਾ ਨਾਂ ਜੀ.",
"Apology and requests scale formal/informal: ਮਾਫ਼ ਕਰੋ vs ਮਾਫ਼ ਕਰੀਂ.",
"Farewells promise return: ਫਿਰ ਮਿਲਾਂਗੇ (we will meet again).",
"Blessings flow downward: ਖੁਸ਼ ਰਹੋ, ਜੁਗ ਜੁਗ ਜੀਓ from elders.",
],
"requirements": [
"Greet someone with ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ today and answer ਕੀ ਹਾਲ ਹੈ? with ਮੈਂ ਠੀਕ ਹਾਂ।.",
"Practice the ਜੀ (ji) habit: add it to every yes, no, and name for a week.",
],
"standards": [
"Sociolinguistic norms per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: every greeting is a seal exchanged - ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ the "
"open seal of the community, ਜੀ the respect-seal stamped after names, blessings "
"the elder's seal pressed on the younger. The Signature Language Method teaches "
"phrases as handshakes: offer the right seal to the right person and the door "
"opens."),
},
# ------------------------------------------------------- 10 grammar essentials
{
"key": "grammar",
"name": "Punjabi Grammar Essentials",
"group": "grammar",
"ladder_rank": 4,
"ladder_tier": "compounded",
"description": (
"The working core of Punjabi grammar - word order, gender, number, cases, "
"negation, and questions - each rule with translated example sentences. Word "
"order: subject-object-verb. ਮੁੰਡਾ ਰੋਟੀ ਖਾਂਦਾ ਹੈ। (munda roti khaanda hai.) The "
"boy eats bread. (literally 'boy bread eats') Gender: every noun is masculine "
"or feminine; adjectives and verbs agree. ਵੱਡਾ ਘਰ (vadda ghar, big house - "
"masculine), ਵੱਡੀ ਕਿਤਾਬ (vaddi kitaab, big book - feminine). Number: singular "
"and plural; masculine -ਾ nouns take -ੇ in the plural: ਮੁੰਡਾ/ਮੁੰਡੇ (munda/munde, "
"boy/boys); feminine -ੀ nouns usually stay -ੀ: ਕੁੜੀ/ਕੁੜੀਆਂ (kurhi/kurhiyaan, "
"girl/girls). Cases and postpositions: Punjabi has a direct case and an oblique "
"case, and relations are marked by postpositions after the noun. ਨੂੰ (nun, to/for "
"- dative/accusative): ਮੈਂ ਉਸਨੂੰ ਦੇਖਿਆ। (main usnun dekhiyaa.) I saw him. ਨੇ (ne, "
"ergative - marks the doer in the completed past): ਉਸਨੇ ਕਿਤਾਬ ਪੜ੍ਹੀ। (usne "
"kitaab parhi.) He/she read the book. ਵਿੱਚ (vich, in): ਘਰ ਵਿੱਚ (ghar vich, in "
"the house). ਉੱਤੇ (utte, on): ਮੇਜ਼ ਉੱਤੇ (mez utte, on the table). ਤੋਂ (ton, from): "
"ਘਰੋਂ? no - ਘਰ ਤੋਂ (ghar ton, from the house). ਨਾਲ (naal, with): ਮੇਰੇ ਨਾਲ ਆਓ। "
"(mere naal aao.) Come with me. ਲਈ (lai, for): ਤੁਹਾਡੇ ਲਈ (tuhade lai, for you). "
"ਦਾ/ਦੀ/ਦੇ (da/di/de, of - agrees like an adjective): ਮੇਰਾ ਦੋਸਤ (mera dost, my "
"friend), ਮੇਰੀ ਕਿਤਾਬ (meri kitaab, my book). Articles: none - ਇੱਕ (ikk) does the "
"work of 'a': ਇੱਕ ਮੁੰਡਾ (ikk munda, a boy). Negation: ਨਹੀਂ (nahin) follows the "
"verb: ਮੈਂ ਨਹੀਂ ਜਾਂਦਾ। (main nahin jaanda.) I do not go. ਨਾ (na) goes before the "
"verb for prohibitions: ਨਾ ਜਾਓ। (na jaao.) Do not go. Questions: ਕੀ (ki) at the "
"start for yes/no questions - ਕੀ ਤੁਸੀਂ ਪੰਜਾਬੀ ਬੋਲਦੇ ਹੋ? (ki tusin panjaabi bolde "
"ho?) Do you speak Punjabi? - or question words: ਕੌਣ (kaun, who), ਕੀ (ki, what), "
"ਕਿੱਥੇ (kitthe, where), ਕਦੋਂ (kadon, when), ਕਿਉਂ (kion, why), ਕਿਵੇਂ (kiven, how), "
"ਕਿੰਨਾ (kinna, how much). ਤੁਸੀਂ ਕਿੱਥੇ ਰਹਿੰਦੇ ਹੋ? (tusin kitthe rahinde ho?) Where "
"do you live? The ergative rule: in the completed past (ਮੈਂ ਨੇ ਕੀਤਾ), the verb "
"agrees with the OBJECT: ਉਸਨੇ ਰੋਟੀ ਖਾਧੀ। (usne roti khaadhi.) He ate the bread. "
"(roti is feminine, so ਖਾਧੀ is feminine.) But ਉਸਨੇ ਪਾਣੀ ਪੀਤਾ। (usne paani peetaa.) "
"He drank the water. (paani is masculine, so ਪੀਤਾ.)"
),
"how_it_works": (
"Build a Punjabi sentence in four moves. One: pick the word order - subject, "
"object, verb, always: ਮੈਂ (I) ਚਾਹ (tea) ਪੀਂਦਾ ਹਾਂ (drink). Two: check every "
"noun's gender and dress the adjectives to match. Three: choose the case tool - "
"no marker for the plain subject, ਨੂੰ for the receiver, ਨੇ for the doer of a "
"completed past action, and ਵਿੱਚ/ਉੱਤੇ/ਤੋਂ/ਨਾਲ/ਲਈ for place and relation. Four: "
"negate by putting ਨਹੀਂ after the verb, question by fronting ਕੀ or a question "
"word. The ergative flip is the one surprise: ਮੈਂ ਰੋਟੀ ਖਾਂਦਾ ਹਾਂ (present - verb "
"matches ਮੈਂ) but ਮੈਂ ਨੇ ਰੋਟੀ ਖਾਧੀ (completed past - verb matches ਰੋਟੀ). Drill "
"that pair until the flip feels natural."
),
"key_points": [
"Word order is subject-object-verb, always.",
"Two genders, two numbers; adjectives and verbs agree with the noun.",
"Direct and oblique cases; postpositions (not prepositions) mark relations.",
"ਨੂੰ (to/for), ਨੇ (ergative doer), ਵਿੱਚ (in), ਉੱਤੇ (on), ਤੋਂ (from), ਨਾਲ (with), ਲਈ (for), ਦਾ/ਦੀ/ਦੇ (of).",
"No articles: ਇੱਕ (ikk) does the work of 'a'.",
"Negation: ਨਹੀਂ after the verb; ਨਾ before the verb for commands.",
"Questions: front ਕੀ for yes/no; ਕੌਣ/ਕੀ/ਕਿੱਥੇ/ਕਦੋਂ/ਕਿਉਂ/ਕਿਵੇਂ/ਕਿੰਨਾ for content.",
"Ergative rule: in the completed past the verb agrees with the object.",
],
"requirements": [
"Write ten SOV sentences and mark subject, object, and verb in each.",
"Convert five present sentences to the completed past and apply the ergative flip.",
],
"standards": [
"Grammatical analysis per Bhatia 1993 and Gill & Gleason 1969",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
"Gill, Harjit Singh and Gleason, Henry A. A Reference Grammar of Punjabi, 1969.",
"Shackle, Christopher. 'Punjabi.' In The Indo-Aryan Languages, Routledge, 2003.",
],
"sig_lens": (
"His Signature reading: grammar is the signing protocol - SOV the fixed seal "
"order, postpositions the handshake after the noun, the ergative flip the "
"counter-signature where the object signs back. The Signature Language Method "
"teaches each rule as a clause of one covenant: learn the protocol and every "
"sentence you make is legally binding in Punjabi."),
},
# ------------------------------------------------------- 11 home and family
{
"key": "home",
"name": "Punjabi Home and Family Sentences",
"group": "sentences",
"ladder_rank": 4,
"ladder_tier": "compounded",
"description": (
"Twenty sentences for house, rooms, furniture, and family members. 1. ਇਹ ਮੇਰਾ "
"ਘਰ ਹੈ। (eh mera ghar hai.) This is my house. 2. ਸਾਡਾ ਘਰ ਵੱਡਾ ਹੈ। (saada ghar "
"vadda hai.) Our house is big. 3. ਰਸੋਈ ਵਿੱਚ ਮਾਂ ਖਾਣਾ ਬਣਾਉਂਦੀ ਹੈ। (rasoi vich maan "
"khaana banaundi hai.) Mother cooks food in the kitchen. 4. ਮੇਰਾ ਕਮਰਾ ਉੱਪਰ ਹੈ। "
"(mera kamraa uppar hai.) My room is upstairs. 5. ਬੈਠਕ ਵਿੱਚ ਸੋਫ਼ਾ ਹੈ। (baithak "
"vich sofa hai.) There is a sofa in the living room. 6. ਮੇਜ਼ ਉੱਤੇ ਕਿਤਾਬਾਂ ਹਨ। "
"(mez utte kitaabaan han.) There are books on the table. 7. ਕੁਰਸੀ ਟੁੱਟ ਗਈ ਹੈ। "
"(kursi tutt gayi hai.) The chair is broken. 8. ਖਿੜਕੀ ਖੋਲ੍ਹ ਦਿਓ। (khirhki kholh "
"dio.) Please open the window. 9. ਦਰਵਾਜ਼ਾ ਬੰਦ ਕਰ ਦਿਓ। (darvaazaa band kar dio.) "
"Please close the door. 10. ਬੱਤੀ ਜਗਾ ਦਿਓ। (batti jagaa dio.) Please turn on the "
"light. 11. ਮੇਰੇ ਪਿਉ ਦਾ ਨਾਂ ਹਰਪ੍ਰੀਤ ਹੈ। (mere pio da naan Harpreet hai.) My "
"father's name is Harpreet. 12. ਮੇਰੀ ਮਾਂ ਅਧਿਆਪਕ ਹੈ। (meri maan adhiaapak hai.) "
"My mother is a teacher. 13. ਮੇਰਾ ਭਰਾ ਡਾਕਟਰ ਹੈ। (mera bharaa daaktar hai.) My "
"brother is a doctor. 14. ਮੇਰੀ ਭੈਣ ਸਕੂਲ ਜਾਂਦੀ ਹੈ। (meri bhain school jaandi hai.) "
"My sister goes to school. 15. ਮੇਰੇ ਦਾਦਾ ਜੀ ਬਹੁਤ ਸਿਆਣੇ ਹਨ। (mere daadaa ji bahut "
"siyaane han.) My grandfather is very wise. 16. ਮੇਰੀ ਦਾਦੀ ਕਹਾਣੀਆਂ ਸੁਣਾਉਂਦੀ ਹੈ। "
"(meri daadi kahaaniyaan sunaundi hai.) My grandmother tells stories. 17. ਸਾਡੇ "
"ਘਰ ਪੰਜ ਜੀਅ ਹਨ। (saade ghar panj jee han.) There are five people in our house. "
"18. ਮੇਰਾ ਪੁੱਤਰ ਤਿੰਨ ਸਾਲ ਦਾ ਹੈ। (mera puttar tinn saal da hai.) My son is three "
"years old. 19. ਮੇਰੀ ਧੀ ਬਹੁਤ ਪਿਆਰੀ ਹੈ। (meri dhee bahut pyaari hai.) My daughter "
"is very lovely. 20. ਅਸੀਂ ਸਾਰੇ ਇਕੱਠੇ ਰਹਿੰਦੇ ਹਾਂ। (asin saare ikatthe rahinde "
"haan.) We all live together."
),
"how_it_works": (
"Home sentences run on two frames: 'X ਹੈ' for describing ('the kitchen is big') "
"and 'X ਵਿੱਚ Y ਹੈ' for locating ('in the kitchen there is Y'). Family "
"introductions use the ਦਾ/ਦੀ/ਦੇ (of) chain: ਮੇਰੇ ਪਿਉ ਦਾ ਨਾਂ (mere pio da naan, "
"'my father's name'). Respect rides on ਜੀ (ji): ਦਾਦਾ ਜੀ (daadaa ji, 'respected "
"grandfather'). Ages use ਸਾਲ ਦਾ (saal da, 'years old'): ਤਿੰਨ ਸਾਲ ਦਾ (tinn saal "
"da). Requests in the home use the polite imperative ਦਿਓ (dio, 'please give/do'): "
"ਖਿੜਕੀ ਖੋਲ੍ਹ ਦਿਓ (khirhki kholh dio, 'please open the window')."
),
"key_points": [
"20 sentences: house, rooms, furniture, family members.",
"Locating frame: X ਵਿੱਚ Y ਹੈ (in X there is Y).",
"Family chain with ਦਾ/ਦੀ/ਦੇ: ਮੇਰੇ ਪਿਉ ਦਾ ਨਾਂ.",
"ਜੀ (ji) marks respect: ਦਾਦਾ ਜੀ, ਦਾਦੀ ਜੀ.",
"Age: number + ਸਾਲ ਦਾ (saal da).",
"Polite home requests use ਦਿਓ (dio).",
],
"requirements": [
"Describe your own home in five Punjabi sentences using ਵਿੱਚ.",
"Introduce three family members with the ਦਾ/ਦੀ/ਦੇ chain.",
],
"standards": [
"Sentence frames per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: the home is the first archive - every room a field, "
"every elder a record, the family chain a lineage of seals. The Signature "
"Language Method files the household first because a language learned at the "
"hearth is never lost to the street."),
},
# ------------------------------------------------------- 12 food and cooking
{
"key": "food",
"name": "Punjabi Food and Cooking Sentences",
"group": "sentences",
"ladder_rank": 4,
"ladder_tier": "compounded",
"description": (
"Twenty sentences for meals, ingredients, cooking actions, and restaurants. 1. "
"ਮੈਨੂੰ ਭੁੱਖ ਲੱਗੀ ਹੈ। (mainun bhukkh laggi hai.) I am hungry. 2. ਖਾਣਾ ਤਿਆਰ ਹੈ। "
"(khaana tiyaar hai.) The food is ready. 3. ਅੱਜ ਦਾਲ ਰੋਟੀ ਬਣੀ ਹੈ। (ajj daal roti "
"bani hai.) Today dal and roti are made. 4. ਮਾਂ ਸਾਗ ਬਣਾਉਂਦੀ ਹੈ। (maan saag "
"banaundi hai.) Mother makes saag. 5. ਰੋਟੀ ਤਵੇ ਉੱਤੇ ਸੇਕੋ। (roti tave utte seko.) "
"Cook the roti on the griddle. 6. ਚਾਹ ਵਿੱਚ ਖੰਡ ਪਾਓ। (chaa vich khand paao.) Put "
"sugar in the tea. 7. ਸਬਜ਼ੀ ਵਿੱਚ ਨਮਕ ਘੱਟ ਹੈ। (sabzi vich namak ghatt hai.) There "
"is less salt in the vegetable. 8. ਦੁੱਧ ਉਬਾਲ ਲਓ। (duddh ubaal lao.) Boil the "
"milk. 9. ਚੌਲ ਧੋ ਕੇ ਪਕਾਓ। (chaul dho ke pakaao.) Wash the rice and cook it. 10. "
"ਮੈਨੂੰ ਤਿੱਖਾ ਖਾਣਾ ਪਸੰਦ ਹੈ। (mainun tikkhaa khaana pasand hai.) I like spicy food. "
"11. ਇਹ ਮਿੱਠਾ ਬਹੁਤ ਸਵਾਦ ਹੈ। (eh mitthaa bahut svaad hai.) This sweet is very "
"tasty. 12. ਪਾਣੀ ਦਾ ਗਲਾਸ ਦਿਓ। (paani da glaas dio.) Please give a glass of water. "
"13. ਹੋਰ ਰੋਟੀ ਲਓਗੇ? (hor roti laoge?) Will you take more bread? 14. ਬਸ, ਮੇਰਾ ਢਿੱਡ "
"ਭਰ ਗਿਆ। (bas, mera dhidd bhar gayaa.) Enough, my stomach is full. 15. ਖਾਣਾ ਬਹੁਤ "
"ਸਵਾਦ ਬਣਿਆ ਹੈ। (khaana bahut svaad baniyaa hai.) The food turned out very tasty. "
"16. ਅਸੀਂ ਢਾਬੇ ਤੇ ਖਾਣਾ ਖਾਧਾ। (asin dhaabe te khaana khaadhaa.) We ate at a roadside "
"eatery. 17. ਬਿੱਲ ਕਿੰਨਾ ਹੋਇਆ? (bill kinna hoyaa?) How much is the bill? 18. "
"ਮੈਨੂੰ ਸ਼ਾਕਾਹਾਰੀ ਖਾਣਾ ਚਾਹੀਦਾ ਹੈ। (mainun shaakaahaari khaana chaheeda hai.) I "
"need vegetarian food. 19. ਲੱਸੀ ਠੰਡੀ ਕਰਕੇ ਦਿਓ। (lassi thandi karke dio.) Please "
"give the lassi chilled. 20. ਰੱਬ ਦਾ ਸ਼ੁਕਰ ਹੈ, ਖਾਣਾ ਮਿਲ ਗਿਆ। (rabb da shukar hai, "
"khaana mil gayaa.) Thank God, we got food."
),
"how_it_works": (
"Food talk is built from three verb families: ਬਣਾਉਣਾ (banauna, to make/cook), "
"ਪਕਾਉਣਾ (pakauna, to cook), and ਖਾਣਾ/ਪੀਣਾ (to eat/to drink). Hunger is expressed "
"with ਲੱਗਣਾ (lagna, 'to attach'): ਮੈਨੂੰ ਭੁੱਖ ਲੱਗੀ ਹੈ (mainun bhukkh laggi hai, "
"'to me hunger is attached'). Taste judgments use ਸਵਾਦ (svaad, taste): ਬਹੁਤ ਸਵਾਦ "
"(bahut svaad, very tasty). At a restaurant or ਢਾਬਾ (dhaabaa, roadside eatery), "
"order with ਦਿਓ (dio, please give) and ask the price with ਕਿੰਨਾ (kinna, how "
"much). Dietary needs use ਚਾਹੀਦਾ ਹੈ (chaheeda hai, 'is needed'): ਮੈਨੂੰ ਸ਼ਾਕਾਹਾਰੀ "
"ਖਾਣਾ ਚਾਹੀਦਾ ਹੈ."
),
"key_points": [
"20 sentences: meals, ingredients, cooking actions, restaurant.",
"Hunger frame: ਮੈਨੂੰ ਭੁੱਖ ਲੱਗੀ ਹੈ (to me hunger is attached).",
"Cooking verbs: ਬਣਾਉਣਾ (make), ਪਕਾਉਣਾ (cook), ਸੇਕਣਾ (roast on griddle), ਉਬਾਲਣਾ (boil).",
"Taste word: ਸਵਾਦ (svaad) - ਬਹੁਤ ਸਵਾਦ (very tasty).",
"Ordering frame: X ਦਿਓ (please give X); price: ਬਿੱਲ ਕਿੰਨਾ ਹੋਇਆ?",
"Dietary needs: ਮੈਨੂੰ X ਚਾਹੀਦਾ ਹੈ (I need X).",
],
"requirements": [
"Name five dishes and say who makes them in your house.",
"Role-play ordering a full meal: greeting, order, bill question.",
],
"standards": [
"Sentence frames per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: the kitchen is the laboratory where the language proves "
"itself daily - ਸਵਾਦ the verdict, the ਢਿੱਡ the witness. The Signature Language "
"Method seasons every lesson like a dish: hunger first (the need), then the "
"ingredients (words), then the cooking (grammar), then the tasting (speaking)."),
},
# ------------------------------------------------------- 13 travel and directions
{
"key": "travel",
"name": "Punjabi Travel and Directions Sentences",
"group": "sentences",
"ladder_rank": 5,
"ladder_tier": "compounded",
"description": (
"Twenty sentences for transport, asking directions, tickets, and lodging. 1. "
"ਰੇਲਵੇ ਸਟੇਸ਼ਨ ਕਿੱਥੇ ਹੈ? (relve station kitthe hai?) Where is the railway station? "
"2. ਬੱਸ ਅੱਡਾ ਕਿੰਨੀ ਦੂਰ ਹੈ? (bass addaa kinni door hai?) How far is the bus stand? "
"3. ਸਿੱਧਾ ਜਾਓ, ਫਿਰ ਖੱਬੇ ਮੁੜੋ। (siddhaa jaao, phir khabbe murho.) Go straight, "
"then turn left. 4. ਸੱਜੇ ਮੁੜੋ, ਉੱਥੇ ਮੰਦਰ ਹੈ। (sajje murho, utthe mandar hai.) "
"Turn right, the temple is there. 5. ਇਹ ਰਸਤਾ ਕਿੱਥੇ ਜਾਂਦਾ ਹੈ? (eh rastaa kitthe "
"jaanda hai?) Where does this road go? 6. ਟੈਕਸੀ ਮਿਲੇਗੀ? (taiksi milegi?) Will I "
"get a taxi? 7. ਕਿਰਾਇਆ ਕਿੰਨਾ ਹੋਵੇਗਾ? (kiraayaa kinna hovegaa?) How much will the "
"fare be? 8. ਮੈਨੂੰ ਹਵਾਈ ਅੱਡੇ ਜਾਣਾ ਹੈ। (mainun havaai adde jaanaa hai.) I need to "
"go to the airport. 9. ਗੱਡੀ ਕਿੰਨੇ ਵਜੇ ਆਵੇਗੀ? (gaddi kinne vaje aavegi?) At what "
"time will the train come? 10. ਇੱਕ ਟਿਕਟ ਦਿਓ, ਅੰਮ੍ਰਿਤਸਰ ਤੱਕ। (ikk tikat dio, "
"Amritsar takk.) One ticket, to Amritsar. 11. ਇਹ ਸੀਟ ਖਾਲੀ ਹੈ? (eh seat khaali "
"hai?) Is this seat free? 12. ਬੱਸ ਕਦੋਂ ਚੱਲੇਗੀ? (bass kadon challegi?) When will "
"the bus leave? 13. ਮੈਂ ਰਸਤਾ ਭੁੱਲ ਗਿਆ ਹਾਂ। (main rastaa bhull gayaa haan.) I am "
"lost. (male speaker) 14. ਕੀ ਤੁਸੀਂ ਮੇਰੀ ਮਦਦ ਕਰ ਸਕਦੇ ਹੋ? (ki tusin meri madad kar "
"sakde ho?) Can you help me? 15. ਨਕਸ਼ੇ ਵਿੱਚ ਦੇਖੋ। (nakshe vich dekho.) Look at "
"the map. 16. ਹੋਟਲ ਕਿੰਨੀ ਦੂਰ ਹੈ? (hotal kinni door hai?) How far is the hotel? "
"17. ਇੱਕ ਕਮਰਾ ਚਾਹੀਦਾ ਹੈ, ਦੋ ਦਿਨਾਂ ਲਈ। (ikk kamraa chaheeda hai, do dinaan lai.) "
"I need a room for two days. 18. ਕਿਰਾਇਆ ਇੱਕ ਰਾਤ ਦਾ ਕਿੰਨਾ ਹੈ? (kiraayaa ikk raat "
"da kinna hai?) What is the rent for one night? 19. ਸਵੇਰੇ ਨਾਸ਼ਤਾ ਮਿਲੇਗਾ? (savere "
"naashtaa milegaa?) Will breakfast be available in the morning? 20. ਸਫ਼ਰ "
"ਸੁਰੱਖਿਅਤ ਰਹੇ! (safar surakkhiat rahe!) Have a safe journey!"
),
"how_it_works": (
"Direction sentences pivot on three words: ਸਿੱਧਾ (siddhaa, straight), ਸੱਜੇ "
"(sajje, to the right), ਖੱਬੇ (khabbe, to the left) - with ਮੁੜੋ (murho, turn) "
"after them. Distance questions use ਕਿੰਨੀ ਦੂਰ (kinni door, 'how far'). Tickets "
"and rooms are requested with the ਦਿਓ/ਚਾਹੀਦਾ ਹੈ frames from earlier records: "
"ਇੱਕ ਟਿਕਟ ਦਿਓ (ikk tikat dio), ਇੱਕ ਕਮਰਾ ਚਾਹੀਦਾ ਹੈ (ikk kamraa chaheeda hai). "
"Destinations take ਤੱਕ (takk, 'up to, as far as'): ਅੰਮ੍ਰਿਤਸਰ ਤੱਕ (Amritsar takk). "
"Being lost is ਰਸਤਾ ਭੁੱਲਣਾ (rastaa bhullnaa, 'to forget the road') - ਮੈਂ ਰਸਤਾ "
"ਭੁੱਲ ਗਿਆ ਹਾਂ (male) / ਭੁੱਲ ਗਈ ਹਾਂ (female). Help is asked with ਸਕਣਾ (saknaa, "
"'can'): ਕੀ ਤੁਸੀਂ ਮਦਦ ਕਰ ਸਕਦੇ ਹੋ? Always close travel talk with ਸਫ਼ਰ ਸੁਰੱਖਿਅਤ "
"ਰਹੇ (safe journey)."
),
"key_points": [
"20 sentences: transport, directions, tickets, lodging.",
"Direction trio: ਸਿੱਧਾ (straight), ਸੱਜੇ (right), ਖੱਬੇ (left) + ਮੁੜੋ (turn).",
"ਕਿੰਨੀ ਦੂਰ (kinni door) asks how far; ਤੱਕ (takk) marks the destination.",
"Tickets and rooms: ਦਿਓ (please give) and ਚਾਹੀਦਾ ਹੈ (is needed).",
"Lost = ਰਸਤਾ ਭੁੱਲਣਾ: ਮੈਂ ਰਸਤਾ ਭੁੱਲ ਗਿਆ/ਗਈ ਹਾਂ।",
"Can-you-help frame: ਕੀ ਤੁਸੀਂ X ਕਰ ਸਕਦੇ ਹੋ?",
],
"requirements": [
"Give directions from your home to the nearest market using ਸਿੱਧਾ/ਸੱਜੇ/ਖੱਬੇ.",
"Buy a ticket and book a room in a role-play, using ਤੱਕ and ਚਾਹੀਦਾ ਹੈ.",
],
"standards": [
"Sentence frames per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: the road is the testing ground of every seal - ਸਿੱਧਾ "
"the straight oath, ਤੱਕ the destination stamped on the ticket. The Signature "
"Language Method walks the learner out the door: a language that cannot buy a "
"ticket and find a bed is a map with no roads."),
},
# ------------------------------------------------------- 14 work and school
{
"key": "work",
"name": "Punjabi Work and School Sentences",
"group": "sentences",
"ladder_rank": 5,
"ladder_tier": "compounded",
"description": (
"Twenty sentences for jobs, the office, the classroom, and learning. 1. ਤੁਸੀਂ "
"ਕੀ ਕੰਮ ਕਰਦੇ ਹੋ? (tusin ki kamm karde ho?) What work do you do? 2. ਮੈਂ ਦਫ਼ਤਰ "
"ਵਿੱਚ ਕੰਮ ਕਰਦਾ ਹਾਂ। (main daftar vich kamm karda haan.) I work in an office. 3. "
"ਮੇਰੀ ਨੌਕਰੀ ਨਵੀਂ ਹੈ। (meri naukri naveen hai.) My job is new. 4. ਤਨਖ਼ਾਹ ਕਦੋਂ "
"ਮਿਲੇਗੀ? (tankhaah kadon milegi?) When will the salary come? 5. ਅੱਜ ਮੀਟਿੰਗ ਦਸ "
"ਵਜੇ ਹੈ। (ajj meeting das vaje hai.) The meeting is at ten today. 6. ਮੈਨੂੰ ਛੁੱਟੀ "
"ਚਾਹੀਦੀ ਹੈ। (mainun chhutti chaheedi hai.) I need leave. 7. ਬੌਸ ਨੇ ਬੁਲਾਇਆ ਹੈ। "
"(boss ne bulaayaa hai.) The boss has called. 8. ਇਹ ਰਿਪੋਰਟ ਕੱਲ੍ਹ ਤੱਕ ਦੇ ਦਿਓ। "
"(eh riport kallh takk de dio.) Please submit this report by tomorrow. 9. ਮੈਂ "
"ਸਕੂਲ ਵਿੱਚ ਪੜ੍ਹਦਾ ਹਾਂ। (main school vich parhda haan.) I study in school. 10. "
"ਮੇਰਾ ਮਨਪਸੰਦ ਵਿਸ਼ਾ ਗਣਿਤ ਹੈ। (mera manpasand vishaa ganit hai.) My favorite "
"subject is mathematics. 11. ਅਧਿਆਪਕ ਬਹੁਤ ਚੰਗਾ ਪੜ੍ਹਾਉਂਦਾ ਹੈ। (adhiaapak bahut "
"changa parhaunda hai.) The teacher teaches very well. 12. ਹੋਮਵਰਕ ਪੂਰਾ ਕਰ ਲਿਆ? "
"(homework pooraa kar liyaa?) Did you finish the homework? 13. ਕਿਤਾਬ ਦਾ ਪੰਨਾ "
"ਖੋਲ੍ਹੋ। (kitaab da pannaa kholho.) Open the book's page. 14. ਸਵਾਲ ਪੁੱਛੋ, ਡਰੋ "
"ਨਾ। (savaal puchho, daro na.) Ask questions, do not be afraid. 15. ਇਮਤਿਹਾਨ "
"ਅਗਲੇ ਹਫ਼ਤੇ ਹੈ। (imtihaan agle hafte hai.) The exam is next week. 16. ਮੈਂ ਪਹਿਲੇ "
"ਨੰਬਰ ਤੇ ਆਇਆ। (main pahile number te aayaa.) I came first. 17. ਸਿੱਖਣਾ ਕਦੇ ਨਹੀਂ "
"ਰੁਕਦਾ। (sikhnaa kade nahin rukdaa.) Learning never stops. 18. ਮਿਹਨਤ ਦਾ ਫਲ "
"ਮਿੱਠਾ ਹੁੰਦਾ ਹੈ। (mehnat da phal mittha hunda hai.) The fruit of hard work is "
"sweet. 19. ਦਫ਼ਤਰ ਕਦੋਂ ਬੰਦ ਹੁੰਦਾ ਹੈ? (daftar kadon band hunda hai?) When does "
"the office close? 20. ਕੱਲ੍ਹ ਫਿਰ ਮਿਲਦੇ ਹਾਂ। (kallh phir milde haan.) See you "
"tomorrow."
),
"how_it_works": (
"Work and school share the ਕੰਮ/ਪੜ੍ਹਾਈ vocabulary and the deadline frame: X "
"ਤੱਕ (takk, 'by X'). Orders at work use the polite imperative: ਦੇ ਦਿਓ (de dio, "
"'please submit/give'). Classroom language runs on ਖੋਲ੍ਹੋ (kholho, 'open'), "
"ਪੁੱਛੋ (puchho, 'ask'), and the encouragement ਡਰੋ ਨਾ (daro na, 'do not fear'). "
"Results use ਆਉਣਾ (aauna, 'to come'): ਪਹਿਲੇ ਨੰਬਰ ਤੇ ਆਉਣਾ (to come first). The "
"proverb ਮਿਹਨਤ ਦਾ ਫਲ ਮਿੱਠਾ ਹੁੰਦਾ ਹੈ seals the record - hard work's fruit is "
"sweet - and it doubles as a usable idiom in any workplace."
),
"key_points": [
"20 sentences: jobs, office, classroom, learning.",
"Deadline frame: X ਤੱਕ (by X) - ਕੱਲ੍ਹ ਤੱਕ ਦੇ ਦਿਓ.",
"Workplace imperative: ਦੇ ਦਿਓ (please submit).",
"Classroom verbs: ਖੋਲ੍ਹੋ (open), ਪੁੱਛੋ (ask), ਡਰੋ ਨਾ (do not fear).",
"Coming first = ਪਹਿਲੇ ਨੰਬਰ ਤੇ ਆਉਣਾ.",
"Proverb seal: ਮਿਹਨਤ ਦਾ ਫਲ ਮਿੱਠਾ ਹੁੰਦਾ ਹੈ.",
],
"requirements": [
"Describe your job or studies in five sentences.",
"Give three classroom instructions using the polite imperative.",
],
"standards": [
"Sentence frames per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: work is the oath in action and school the oath in "
"training - ਮਿਹਨਤ the signature, ਫਲ the seal. The Signature Language Method "
"files this record under 'the proving ground': speak it where money and marks "
"are on the line."),
},
# ------------------------------------------------------- 15 health and body
{
"key": "health",
"name": "Punjabi Health and Body Sentences",
"group": "sentences",
"ladder_rank": 5,
"ladder_tier": "compounded",
"description": (
"Twenty sentences for body parts, symptoms, the doctor visit, and the pharmacy. "
"1. ਮੇਰਾ ਸਿਰ ਦੁੱਖਦਾ ਹੈ। (mera sir dukkhda hai.) My head hurts. 2. ਮੈਨੂੰ ਬੁਖ਼ਾਰ "
"ਹੈ। (mainun bukhaar hai.) I have a fever. 3. ਮੇਰਾ ਗਲਾ ਖ਼ਰਾਬ ਹੈ। (mera galaa "
"kharaab hai.) My throat is bad. 4. ਮੈਨੂੰ ਜ਼ੁਕਾਮ ਲੱਗਿਆ ਹੈ। (mainun zukaam "
"laggiyaa hai.) I have a cold. 5. ਮੇਰੇ ਪੇਟ ਵਿੱਚ ਦਰਦ ਹੈ। (mere pet vich darad "
"hai.) I have pain in my stomach. 6. ਮੇਰੀ ਅੱਖ ਲਾਲ ਹੈ। (meri akkh laal hai.) My "
"eye is red. 7. ਮੇਰਾ ਦੰਦ ਦੁੱਖਦਾ ਹੈ। (mera dand dukkhda hai.) My tooth aches. 8. "
"ਮੈਨੂੰ ਚੱਕਰ ਆ ਰਹੇ ਹਨ। (mainun chakkar aa rahe han.) I feel dizzy. 9. ਡਾਕਟਰ ਨੂੰ "
"ਦਿਖਾਓ। (daaktar nun dikhaao.) Show it to a doctor. 10. ਹਸਪਤਾਲ ਕਿੱਥੇ ਹੈ? "
"(haspataal kitthe hai?) Where is the hospital? 11. ਡਾਕਟਰ ਸਾਹਿਬ, ਮੈਨੂੰ ਬਚਾਓ। "
"(daaktar saahib, mainun bachaao.) Doctor, help me. 12. ਦਵਾਈ ਕਦੋਂ ਲੈਣੀ ਹੈ? "
"(davaai kadon laini hai?) When should the medicine be taken? 13. ਖਾਣੇ ਤੋਂ ਬਾਅਦ "
"ਇੱਕ ਗੋਲੀ ਲਓ। (khaane ton baad ikk goli lao.) Take one pill after meals. 14. "
"ਪਾਣੀ ਜ਼ਿਆਦਾ ਪੀਓ। (paani ziyaadaa peeo.) Drink more water. 15. ਆਰਾਮ ਕਰੋ। (aaraam "
"karo.) Take rest. 16. ਇਹ ਦਵਾਈ ਕੌੜੀ ਹੈ ਪਰ ਅਸਰਦਾਰ ਹੈ। (eh davaai kauri hai par "
"asardaar hai.) This medicine is bitter but effective. 17. ਮੈਨੂੰ ਐਲਰਜੀ ਹੈ। "
"(mainun allergy hai.) I have an allergy. 18. ਦਵਾਖ਼ਾਨਾ ਕਦੋਂ ਖੁੱਲ੍ਹਦਾ ਹੈ? "
"(davaakhaanaa kadon khullhda hai?) When does the pharmacy open? 19. ਪੱਟੀ ਬਦਲ "
"ਦਿਓ। (patti badal dio.) Please change the bandage. 20. ਹੁਣ ਮੈਂ ਠੀਕ ਹਾਂ, ਰੱਬ ਦਾ "
"ਸ਼ੁਕਰ ਹੈ। (hun main theek haan, rabb da shukar hai.) Now I am fine, thank God."
),
"how_it_works": (
"Symptoms are reported with three frames: X ਦੁੱਖਦਾ ਹੈ (X dukkhda hai, 'X aches') "
"for localized pain, ਮੈਨੂੰ X ਹੈ (mainun X hai, 'to me there is X') for conditions "
"like fever and cold, and X ਵਿੱਚ ਦਰਦ ਹੈ for pain inside something. Body parts "
"to know: ਸਿਰ (sir, head), ਅੱਖ (akkh, eye), ਨੱਕ (nakk, nose), ਕੰਨ (kann, ear), "
"ਮੂੰਹ (munh, mouth), ਦੰਦ (dand, tooth), ਗਲਾ (galaa, throat), ਹੱਥ (hath, hand), "
"ਪੈਰ (pair, foot), ਪੇਟ (pet, stomach), ਦਿਲ (dil, heart), ਹੱਡੀ (haddi, bone). "
"Doctors give orders with the imperative: ਲਓ (lao, take), ਪੀਓ (peeo, drink), "
"ਕਰੋ (karo, do). Dosage uses ਤੋਂ ਬਾਅਦ/ਤੋਂ ਪਹਿਲਾਂ (after/before): ਖਾਣੇ ਤੋਂ ਬਾਅਦ "
"(after meals). Address the doctor as ਡਾਕਟਰ ਸਾਹਿਬ (daaktar saahib)."
),
"key_points": [
"20 sentences: body parts, symptoms, doctor visit, pharmacy.",
"Pain frames: X ਦੁੱਖਦਾ ਹੈ (aches); ਮੈਨੂੰ X ਹੈ (I have X); X ਵਿੱਚ ਦਰਦ ਹੈ.",
"Twelve core body parts from ਸਿਰ (head) to ਹੱਡੀ (bone).",
"Doctor's orders: ਲਓ (take), ਪੀਓ (drink), ਆਰਾਮ ਕਰੋ (rest).",
"Dosage timing: ਖਾਣੇ ਤੋਂ ਬਾਅਦ (after meals), ਖਾਣੇ ਤੋਂ ਪਹਿਲਾਂ (before meals).",
"Respect address: ਡਾਕਟਰ ਸਾਹਿਬ.",
],
"requirements": [
"Point to ten body parts and name each in Punjabi.",
"Describe three symptoms using the three pain frames.",
],
"standards": [
"Sentence frames per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: the body is the first instrument and health its tuning "
"- ਦਰਦ the alarm seal, ਆਰਾਮ the repair seal. The Signature Language Method "
"teaches health talk as emergency protocol: when the body files a complaint, "
"the tongue must already know the forms."),
},
# ------------------------------------------------------- 16 emotions
{
"key": "emotions",
"name": "Punjabi Emotions and Feelings Sentences",
"group": "sentences",
"ladder_rank": 5,
"ladder_tier": "compounded",
"description": (
"Twenty sentences for happy, sad, angry, afraid, love, and surprise. 1. ਮੈਂ "
"ਬਹੁਤ ਖੁਸ਼ ਹਾਂ। (main bahut khush haan.) I am very happy. 2. ਅੱਜ ਮੇਰਾ ਦਿਲ ਬਾਗ਼ "
"ਬਾਗ਼ ਹੋ ਗਿਆ। (ajj mera dil baagh baagh ho gayaa.) Today my heart is overjoyed. "
"(idiom: heart became a garden) 3. ਉਹ ਖੁਸ਼ੀ ਨਾਲ ਨੱਚ ਰਹੀ ਹੈ। (oh khushi naal "
"nach rahi hai.) She is dancing with joy. 4. ਮੈਨੂੰ ਉਦਾਸੀ ਹੈ। (mainun udaasi "
"hai.) I feel sad. 5. ਉਹ ਰੋ ਰਿਹਾ ਹੈ। (oh ro rihaa hai.) He is crying. 6. ਮੇਰਾ "
"ਦਿਲ ਟੁੱਟ ਗਿਆ। (mera dil tutt gayaa.) My heart is broken. 7. ਮੈਨੂੰ ਗੁੱਸਾ ਆ "
"ਰਿਹਾ ਹੈ। (mainun gussaa aa rihaa hai.) I am getting angry. 8. ਸ਼ਾਂਤ ਹੋ ਜਾਓ। "
"(shaant ho jaao.) Calm down. 9. ਉਹ ਗੁੱਸੇ ਵਿੱਚ ਚਲਾ ਗਿਆ। (oh gusse vich chalaa "
"gayaa.) He left in anger. 10. ਮੈਨੂੰ ਡਰ ਲੱਗਦਾ ਹੈ। (mainun dar lagdaa hai.) I "
"feel afraid. 11. ਡਰੋ ਨਾ, ਮੈਂ ਤੁਹਾਡੇ ਨਾਲ ਹਾਂ। (daro na, main tuhade naal haan.) "
"Do not be afraid, I am with you. 12. ਹਨੇਰੇ ਤੋਂ ਡਰ ਲੱਗਦਾ ਹੈ। (hanere ton dar "
"lagdaa hai.) Darkness is frightening. 13. ਮੈਂ ਤੁਹਾਨੂੰ ਪਿਆਰ ਕਰਦਾ ਹਾਂ। (main "
"tuhaanun pyaar karda haan.) I love you. (male speaker) 14. ਮਾਂ ਦਾ ਪਿਆਰ ਸਭ ਤੋਂ "
"ਵੱਡਾ ਹੈ। (maan da pyaar sabh ton vaddaa hai.) A mother's love is the greatest. "
"15. ਉਹ ਆਪਣੇ ਦੇਸ਼ ਨੂੰ ਪਿਆਰ ਕਰਦਾ ਹੈ। (oh aapne desh nun pyaar karda hai.) He loves "
"his country. 16. ਮੈਂ ਹੈਰਾਨ ਹਾਂ! (main hairaan haan!) I am surprised! 17. ਇਹ "
"ਸੁਣ ਕੇ ਮੈਂ ਦੰਗ ਰਹਿ ਗਿਆ। (eh sun ke main dang reh gayaa.) Hearing this, I was "
"stunned. 18. ਕੀ ਗੱਲ ਹੈ, ਤੁਸੀਂ ਪਰੇਸ਼ਾਨ ਲੱਗਦੇ ਹੋ? (ki gall hai, tusin pareshaan "
"lagde ho?) What is the matter, you look worried? 19. ਹੌਸਲਾ ਰੱਖੋ, ਸਭ ਠੀਕ "
"ਹੋਵੇਗਾ। (hauslaa rakkho, sabh theek hovegaa.) Keep courage, all will be well. "
"20. ਖੁਸ਼ੀ ਵੰਡਣ ਨਾਲ ਵਧਦੀ ਹੈ। (khushi vanddan naal vadhdii hai.) Happiness grows "
"by sharing."
),
"how_it_works": (
"Feelings use the 'to me' frame more than English does: ਮੈਨੂੰ ਡਰ ਲੱਗਦਾ ਹੈ "
"(mainun dar lagdaa hai, 'to me fear attaches') for 'I am afraid', ਮੈਨੂੰ ਗੁੱਸਾ "
"ਆ ਰਿਹਾ ਹੈ ('to me anger is coming') for 'I am getting angry'. The heart (ਦਿਲ, "
"dil) carries the big metaphors: ਦਿਲ ਟੁੱਟਣਾ (heart breaking), ਦਿਲ ਬਾਗ਼ ਬਾਗ਼ "
"ਹੋਣਾ (heart becoming a garden = overjoyed). Comfort someone with ਹੌਸਲਾ ਰੱਖੋ "
"(hauslaa rakkho, 'keep courage') and ਡਰੋ ਨਾ (daro na, 'do not fear'). Love is "
"ਪਿਆਰ ਕਰਨਾ with ਨੂੰ marking the beloved: ਤੁਹਾਨੂੰ ਪਿਆਰ ਕਰਦਾ ਹਾਂ. Surprise is "
"ਹੈਰਾਨ ਹੋਣਾ (hairaan honaa) or the stronger ਦੰਗ ਰਹਿ ਜਾਣਾ (to be left stunned)."
),
"key_points": [
"20 sentences across happy, sad, angry, afraid, love, surprise.",
"Feeling frame: ਮੈਨੂੰ X ਲੱਗਦਾ/ਆ ਰਿਹਾ ਹੈ (to me X attaches/comes).",
"ਦਿਲ (heart) metaphors: ਟੁੱਟਣਾ (break), ਬਾਗ਼ ਬਾਗ਼ ਹੋਣਾ (overjoyed).",
"Comfort phrases: ਹੌਸਲਾ ਰੱਖੋ, ਡਰੋ ਨਾ, ਸਭ ਠੀਕ ਹੋਵੇਗਾ।",
"Love: ਪਿਆਰ ਕਰਨਾ + ਨੂੰ for the beloved.",
"Surprise scale: ਹੈਰਾਨ (surprised) to ਦੰਗ (stunned).",
],
"requirements": [
"Say how you feel today in Punjabi, then comfort a friend in three sentences.",
"Learn the six ਦਿਲ idioms by acting each one.",
],
"standards": [
"Sentence frames per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: emotions are the ink of the signature - ਖੁਸ਼ੀ the "
"bright seal, ਹੌਸਲਾ the steady one. The Signature Language Method teaches "
"feelings as weather the speaker reports honestly: the 'to me' frame makes "
"every emotion a dispatch from the heart's own station."),
},
# ------------------------------------------------------- 17 nature and weather
{
"key": "nature",
"name": "Punjabi Nature and Weather Sentences",
"group": "sentences",
"ladder_rank": 6,
"ladder_tier": "compounded",
"description": (
"Twenty sentences for animals, plants, seasons, and weather talk. 1. ਅੱਜ ਮੌਸਮ "
"ਬਹੁਤ ਚੰਗਾ ਹੈ। (ajj mausam bahut changa hai.) The weather is very good today. 2. "
"ਬਾਹਰ ਮੀਂਹ ਪੈ ਰਿਹਾ ਹੈ। (baahar meenh pai rihaa hai.) It is raining outside. 3. "
"ਸਰਦੀ ਵਿੱਚ ਬਰਫ਼ ਪੈਂਦੀ ਹੈ। (sardi vich baraf paindi hai.) It snows in winter. 4. "
"ਗਰਮੀ ਵਿੱਚ ਲੂ ਚੱਲਦੀ ਹੈ। (garmi vich loo challdi hai.) Hot winds blow in summer. "
"5. ਅੱਜ ਧੁੱਪ ਖਿੜੀ ਹੈ। (ajj dhupp khirhi hai.) It is sunny today. 6. ਅਸਮਾਨ ਵਿੱਚ "
"ਬੱਦਲ ਹਨ। (asmaan vich baddal han.) There are clouds in the sky. 7. ਹਵਾ ਤੇਜ਼ "
"ਚੱਲ ਰਹੀ ਹੈ। (havaa tez chall rahi hai.) The wind is blowing fast. 8. ਕੱਲ੍ਹ "
"ਤੂਫ਼ਾਨ ਆਇਆ ਸੀ। (kallh toofaan aayaa see.) A storm came yesterday. 9. ਬਾਗ਼ ਵਿੱਚ "
"ਫੁੱਲ ਖਿੜੇ ਹਨ। (baagh vich phull khirhe han.) Flowers are blooming in the garden. "
"10. ਇਹ ਦਰੱਖਤ ਬਹੁਤ ਪੁਰਾਣਾ ਹੈ। (eh darakht bahut puraanaa hai.) This tree is very "
"old. 11. ਅੰਬ ਦਾ ਮੌਸਮ ਆ ਗਿਆ। (amb da mausam aa gayaa.) Mango season has come. "
"12. ਖੇਤਾਂ ਵਿੱਚ ਫ਼ਸਲ ਪੱਕ ਗਈ ਹੈ। (khetaan vich fasal pakk gayi hai.) The crop has "
"ripened in the fields. 13. ਚਿੜੀ ਦਰੱਖਤ ਉੱਤੇ ਬੈਠੀ ਹੈ। (chirhi darakht utte baithi "
"hai.) A sparrow sits on the tree. 14. ਮੋਰ ਬਹੁਤ ਸੁੰਦਰ ਪੰਛੀ ਹੈ। (mor bahut "
"sundar panchhi hai.) The peacock is a very beautiful bird. 15. ਗਾਂ ਦੁੱਧ ਦਿੰਦੀ "
"ਹੈ। (gaan duddh dindi hai.) The cow gives milk. 16. ਮੱਝ ਪਾਣੀ ਵਿੱਚ ਨਹਾਉਂਦੀ ਹੈ। "
"(majjh paani vich nahaundi hai.) The buffalo bathes in the water. 17. ਸ਼ੇਰ "
"ਜੰਗਲ ਦਾ ਰਾਜਾ ਹੈ। (sher jangal da raajaa hai.) The lion is the king of the "
"jungle. 18. ਸੱਪ ਤੋਂ ਬਚ ਕੇ ਰਹੋ। (sapp ton bach ke raho.) Stay safe from snakes. "
"19. ਤਿਤਲੀ ਫੁੱਲਾਂ ਉੱਤੇ ਉੱਡਦੀ ਹੈ। (titli phullaan utte uddi hai.) The butterfly "
"flies over the flowers. 20. ਕੁਦਰਤ ਦੀ ਰੱਖਿਆ ਕਰੋ। (kudrat di rakkhiyaa karo.) "
"Protect nature."
),
"how_it_works": (
"Weather verbs are special: rain 'falls' (ਮੀਂਹ ਪੈਣਾ, meenh painaa), snow 'falls' "
"(ਬਰਫ਼ ਪੈਣਾ), wind 'walks' (ਹਵਾ ਚੱਲਣਾ), sun 'blooms' (ਧੁੱਪ ਖਿੜਨਾ). Learn the "
"verb with the weather noun as one unit - never translate word by word. Seasons "
"drive the farming sentences: ਫ਼ਸਲ ਪੱਕਣਾ (crop ripening), ਅੰਬ ਦਾ ਮੌਸਮ (mango "
"season). Animals take the respect of their role: ਗਾਂ (cow) gives, ਸ਼ੇਰ (lion) "
"rules, ਸੱਪ (snake) warns. The closing line ਕੁਦਰਤ ਦੀ ਰੱਖਿਆ ਕਰੋ doubles as a "
"public-service sentence you will actually see on signs."
),
"key_points": [
"20 sentences: animals, plants, seasons, weather talk.",
"Weather verbs: ਮੀਂਹ ਪੈਣਾ (rain falls), ਹਵਾ ਚੱਲਣਾ (wind walks), ਧੁੱਪ ਖਿੜਨਾ (sun blooms).",
"Seasons in action: ਫ਼ਸਲ ਪੱਕਣਾ, ਅੰਬ ਦਾ ਮੌਸਮ.",
"Farm animals: ਗਾਂ (cow), ਮੱਝ (buffalo); wild: ਸ਼ੇਰ (lion), ਸੱਪ (snake), ਮੋਰ (peacock).",
"Small creatures: ਚਿੜੀ (sparrow), ਤਿਤਲੀ (butterfly).",
"Plants: ਦਰੱਖਤ (tree), ਫੁੱਲ (flower), ਫ਼ਸਲ (crop).",
],
"requirements": [
"Describe today's weather in three full sentences.",
"Name ten animals and say one true sentence about each.",
],
"standards": [
"Sentence frames per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: nature is the original archive - every season a volume, "
"every crop a record filed by the sun. The Signature Language Method reads "
"weather as dispatches: ਮੀਂਹ ਪੈ ਰਿਹਾ ਹੈ is not grammar practice, it is a field "
"report from the sky."),
},
# ------------------------------------------------------- 18 shopping and money
{
"key": "shopping",
"name": "Punjabi Shopping and Money Sentences",
"group": "sentences",
"ladder_rank": 6,
"ladder_tier": "compounded",
"description": (
"Twenty sentences for the market, prices, bargaining, and paying. 1. ਇਹ ਕਿੰਨੇ "
"ਦਾ ਹੈ? (eh kinne da hai?) How much is this? 2. ਬਹੁਤ ਮਹਿੰਗਾ ਹੈ, ਥੋੜ੍ਹਾ ਘੱਟ ਕਰੋ। "
"(bahut mahingaa hai, thorhaa ghatt karo.) It is very expensive, reduce it a "
"little. 3. ਆਖ਼ਰੀ ਭਾਅ ਦੱਸੋ। (aakhri bhaa dasso.) Tell me the final price. 4. "
"ਮੈਂ ਸਬਜ਼ੀ ਲੈਣ ਬਾਜ਼ਾਰ ਗਿਆ। (main sabzi lain bazaar gayaa.) I went to the market "
"to buy vegetables. 5. ਟਮਾਟਰ ਕਿਲੋ ਦੇ ਹਿਸਾਬ ਨਾਲ ਹਨ? (tamaatar kilo de hisaab "
"naal han?) Are the tomatoes priced per kilo? 6. ਅੱਧਾ ਕਿਲੋ ਆਲੂ ਦਿਓ। (addhaa kilo "
"aaloo dio.) Give half a kilo of potatoes. 7. ਤਾਜ਼ਾ ਮਾਲ ਦਿਖਾਓ। (taazaa maal "
"dikhaao.) Show me fresh stock. 8. ਇਹ ਕੱਪੜਾ ਕਿਸ ਭਾਅ ਹੈ? (eh kaprhaa kis bhaa "
"hai?) What is the price of this cloth? 9. ਕੋਈ ਸਸਤਾ ਵਿਕਲਪ ਹੈ? (koi sastaa "
"vikalap hai?) Is there a cheaper option? 10. ਦੁਕਾਨਦਾਰ ਇਮਾਨਦਾਰ ਹੈ। (dukaandaar "
"imaandaar hai.) The shopkeeper is honest. 11. ਪੈਸੇ ਗਿਣ ਲਓ। (paise gin lao.) "
"Count the money. 12. ਖੁੱਲ੍ਹੇ ਪੈਸੇ ਹਨ? (khullhe paise han?) Do you have change? "
"13. ਮੈਂ ਨਕਦ ਦੇਵਾਂਗਾ। (main nakad devaangaa.) I will pay cash. 14. ਕਾਰਡ ਚੱਲੇਗਾ? "
"(card challegaa?) Will a card work? 15. ਬਿੱਲ ਬਣਾ ਦਿਓ। (bill banaa dio.) Please "
"make the bill. 16. ਰਸੀਦ ਦੇ ਦਿਓ। (raseed de dio.) Please give the receipt. 17. "
"ਇਹ ਵਸਤੂ ਵਾਪਸ ਹੋ ਸਕਦੀ ਹੈ? (eh vastoo vaapas ho sakdi hai?) Can this item be "
"returned? 18. ਗਾਰੰਟੀ ਕਿੰਨੇ ਸਾਲ ਦੀ ਹੈ? (guarantee kinne saal di hai?) How many "
"years is the guarantee? 19. ਸੌਦਾ ਪੱਕਾ! (saudaa pakkaa!) Deal done! 20. ਅਗਲੀ "
"ਵਾਰ ਫਿਰ ਆਵਾਂਗਾ। (agli vaar phir aavaangaa.) I will come again next time."
),
"how_it_works": (
"Bargaining is a ritual with fixed moves. Open with ਇਹ ਕਿੰਨੇ ਦਾ ਹੈ? (how much "
"is this?), counter with ਬਹੁਤ ਮਹਿੰਗਾ ਹੈ (too expensive), demand ਆਖ਼ਰੀ ਭਾਅ "
"(the final price), and seal with ਸੌਦਾ ਪੱਕਾ (deal done). Quantities use the "
"weight words: ਕਿਲੋ (kilo), ਅੱਧਾ ਕਿਲੋ (half kilo), ਗ੍ਰਾਮ (gram). Paying runs on "
"ਨਕਦ (nakad, cash) versus ਕਾਰਡ (card); ask ਖੁੱਲ੍ਹੇ ਪੈਸੇ ਹਨ? before handing big "
"notes. The receipt is ਰਸੀਦ (raseed) and the return question is ਵਾਪਸ ਹੋ ਸਕਦੀ "
"ਹੈ? Every market sentence keeps the SOV order even in a hurry: ਪੈਸੇ ਗਿਣ ਲਓ "
"('money count take')."
),
"key_points": [
"20 sentences: market, prices, bargaining, paying.",
"Bargaining script: ਕਿੰਨੇ ਦਾ? -> ਬਹੁਤ ਮਹਿੰਗਾ -> ਆਖ਼ਰੀ ਭਾਅ -> ਸੌਦਾ ਪੱਕਾ!",
"Weights: ਕਿਲੋ, ਅੱਧਾ ਕਿਲੋ, ਗ੍ਰਾਮ.",
"Payment: ਨਕਦ (cash), ਕਾਰਡ (card); ਖੁੱਲ੍ਹੇ ਪੈਸੇ (change).",
"After-sale: ਰਸੀਦ (receipt), ਵਾਪਸ (return), ਗਾਰੰਟੀ (guarantee).",
"Price question: ਇਹ ਕਿੰਨੇ ਦਾ ਹੈ? / ਕਿਸ ਭਾਅ ਹੈ?",
],
"requirements": [
"Bargain for three items in a role-play without breaking the script.",
"Buy vegetables by weight using ਕਿਲੋ and ਅੱਧਾ ਕਿਲੋ correctly.",
],
"standards": [
"Sentence frames per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: the bazaar is the exchange where every seal is tested "
"- ਭਾਅ the asking seal, ਸੌਦਾ ਪੱਕਾ the closing seal. The Signature Language "
"Method haggles on purpose: bargaining forces the tongue to move fast, and a "
"fast tongue is a fluent one."),
},
# ------------------------------------------------------- 19 friendship
{
"key": "social",
"name": "Punjabi Friendship and Social Life Sentences",
"group": "sentences",
"ladder_rank": 6,
"ladder_tier": "compounded",
"description": (
"Twenty sentences for meeting people, invitations, and celebrations. 1. "
"ਤੁਹਾਡਾ ਨਾਂ ਕੀ ਹੈ? (tuhada naan ki hai?) What is your name? 2. ਮੇਰਾ ਨਾਂ ਸਿਮਰਨ "
"ਹੈ। (mera naan Simran hai.) My name is Simran. 3. ਤੁਸੀਂ ਕਿੱਥੋਂ ਹੋ? (tusin "
"kitthon ho?) Where are you from? 4. ਮੈਂ ਪੰਜਾਬ ਤੋਂ ਹਾਂ। (main Panjaab ton haan.) "
"I am from Punjab. 5. ਤੁਹਾਨੂੰ ਮਿਲ ਕੇ ਖੁਸ਼ੀ ਹੋਈ। (tuhaanun mil ke khushi hoi.) "
"Pleased to meet you. 6. ਇਹ ਮੇਰਾ ਦੋਸਤ ਗੁਰਪ੍ਰੀਤ ਹੈ। (eh mera dost Gurpreet hai.) "
"This is my friend Gurpreet. 7. ਅਸੀਂ ਪੁਰਾਣੇ ਦੋਸਤ ਹਾਂ। (asin puraane dost haan.) "
"We are old friends. 8. ਚਾਹ ਪੀਓਗੇ? (chaa peeoge?) Will you have tea? 9. ਮੇਰੇ "
"ਘਰ ਆਓ, ਖਾਣਾ ਖਾਵਾਂਗੇ। (mere ghar aao, khaana khaavaange.) Come to my house, we "
"will eat. 10. ਕੱਲ੍ਹ ਪਾਰਟੀ ਹੈ, ਜ਼ਰੂਰ ਆਉਣਾ। (kallh party hai, zaroor aaunaa.) "
"There is a party tomorrow, do come. 11. ਵਿਆਹ ਵਿੱਚ ਜ਼ਰੂਰ ਆਇਓ। (viaah vich "
"zaroor aaio.) Do come to the wedding. 12. ਵਧਾਈ ਹੋਵੇ! (vadhaai hove!) "
"Congratulations! 13. ਤੁਹਾਡੀ ਸਫ਼ਲਤਾ ਤੇ ਮਾਣ ਹੈ। (tuhadi safaltaa te maan hai.) "
"Proud of your success. 14. ਦੋਸਤੀ ਸਭ ਤੋਂ ਵੱਡੀ ਦੌਲਤ ਹੈ। (dosti sabh ton vaddi "
"daulat hai.) Friendship is the greatest wealth. 15. ਮੁਸੀਬਤ ਵਿੱਚ ਦੋਸਤ ਕੰਮ "
"ਆਉਂਦਾ ਹੈ। (museebat vich dost kamm aaundaa hai.) A friend helps in trouble. 16. "
"ਅਸੀਂ ਇਕੱਠੇ ਫਿਲਮ ਦੇਖੀ। (asin ikatthe film dekhi.) We watched a film together. "
"17. ਚਲੋ, ਸੈਰ ਕਰ ਆਈਏ। (chalo, sair kar aaie.) Come, let us go for a walk. 18. "
"ਤੁਹਾਡਾ ਪਰਿਵਾਰ ਕਿਵੇਂ ਹੈ? (tuhada parivaar kiven hai?) How is your family? 19. "
"ਸਭ ਨੂੰ ਮੇਰਾ ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਕਹਿਣਾ। (sabh nun mera sat sri akaal kahinaa.) Give my "
"greetings to everyone. 20. ਦੋਸਤੋ, ਰੱਬ ਰਾਖਾ! (dosto, rabb raakha!) Friends, "
"goodbye!"
),
"how_it_works": (
"Social Punjabi opens with the name-and-place exchange: ਨਾਂ ਕੀ ਹੈ? / ਕਿੱਥੋਂ "
"ਹੋ? Then comes the pleasure formula ਤੁਹਾਨੂੰ ਮਿਲ ਕੇ ਖੁਸ਼ੀ ਹੋਈ ('meeting you, "
"happiness happened'). Invitations use the future or the imperative with "
"ਜ਼ਰੂਰ (zaroor, 'definitely'): ਜ਼ਰੂਰ ਆਉਣਾ (do come). Hospitality is tea first: "
"ਚਾਹ ਪੀਓਗੇ? is the standard welcome, asked before any business. Celebrations "
"run on ਵਧਾਈ ਹੋਵੇ and blessings; partings pass greetings along: ਸਭ ਨੂੰ ਮੇਰਾ "
"ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਕਹਿਣਾ. Friendship proverbs - ਦੋਸਤੀ ਸਭ ਤੋਂ ਵੱਡੀ ਦੌਲਤ ਹੈ - are "
"usable in toasts and speeches."
),
"key_points": [
"20 sentences: meeting people, invitations, celebrations.",
"Introduction trio: ਨਾਂ ਕੀ ਹੈ? / ਕਿੱਥੋਂ ਹੋ? / ਮਿਲ ਕੇ ਖੁਸ਼ੀ ਹੋਈ।",
"Invitation strengthener: ਜ਼ਰੂਰ ਆਉਣਾ (do come).",
"Hospitality rule: offer ਚਾਹ first - ਚਾਹ ਪੀਓਗੇ?",
"Parting courtesy: pass greetings to the family left behind.",
"Friendship proverbs double as toasts.",
],
"requirements": [
"Introduce yourself and two friends in full Punjabi.",
"Invite someone to a wedding and to tea, using ਜ਼ਰੂਰ correctly.",
],
"standards": [
"Sentence frames per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: friendship is the witness system - every ਦੋਸਤ a "
"co-signer, every ਵਧਾਈ a seal of honor. The Signature Language Method treats "
"social talk as the notary office of the language: names recorded, invitations "
"issued, blessings stamped."),
},
# ------------------------------------------------------- 20 technology
{
"key": "tech",
"name": "Punjabi Technology and Communication Sentences",
"group": "sentences",
"ladder_rank": 6,
"ladder_tier": "compounded",
"description": (
"Twenty sentences for phone, internet, computer, and messaging. 1. ਮੇਰਾ ਫ਼ੋਨ "
"ਕਿੱਥੇ ਹੈ? (mera phone kitthe hai?) Where is my phone? 2. ਫ਼ੋਨ ਦੀ ਬੈਟਰੀ ਖ਼ਤਮ "
"ਹੋ ਗਈ। (phone di battery khatam ho gayi.) The phone battery died. 3. ਚਾਰਜਰ "
"ਲਗਾ ਦਿਓ। (charger lagaa dio.) Please plug in the charger. 4. ਮੈਨੂੰ ਫ਼ੋਨ ਕਰੋ। "
"(mainun phone karo.) Call me. 5. ਉਸਦਾ ਨੰਬਰ ਬੰਦ ਆ ਰਿਹਾ ਹੈ। (usda number band aa "
"rihaa hai.) His number is switched off. 6. ਨੈੱਟ ਨਹੀਂ ਚੱਲ ਰਿਹਾ। (net nahin "
"chall rihaa.) The internet is not working. 7. ਵਾਈ-ਫਾਈ ਦਾ ਪਾਸਵਰਡ ਦੱਸੋ। "
"(wifi da password dasso.) Tell me the wifi password. 8. ਮੈਂ ਤੁਹਾਨੂੰ ਸੁਨੇਹਾ "
"ਭੇਜਾਂਗਾ। (main tuhaanun sunehaa bhejaangaa.) I will send you a message. 9. "
"ਵਟਸਐਪ ਤੇ ਫੋਟੋ ਭੇਜੋ। (whatsapp te photo bhejo.) Send the photo on WhatsApp. 10. "
"ਈਮੇਲ ਚੈੱਕ ਕਰ ਲਓ। (email check kar lao.) Check the email. 11. ਕੰਪਿਊਟਰ ਚਾਲੂ "
"ਕਰੋ। (computer chaaloo karo.) Turn on the computer. 12. ਫ਼ਾਈਲ ਡਾਊਨਲੋਡ ਹੋ ਰਹੀ "
"ਹੈ। (file download ho rahi hai.) The file is downloading. 13. ਪਾਸਵਰਡ ਭੁੱਲ "
"ਗਿਆ ਹਾਂ। (password bhull gayaa haan.) I forgot the password. 14. ਸਕਰੀਨ ਬਹੁਤ "
"ਚਮਕਦਾਰ ਹੈ। (screen bahut chamakdaar hai.) The screen is very bright. 15. "
"ਐਪ ਅੱਪਡੇਟ ਕਰੋ। (app update karo.) Update the app. 16. ਵੀਡੀਓ ਕਾਲ ਕਰੀਏ? (video "
"call kariye?) Shall we video call? 17. ਆਵਾਜ਼ ਸਾਫ਼ ਨਹੀਂ ਆ ਰਹੀ। (aavaaz saaf "
"nahin aa rahi.) The voice is not clear. 18. ਮੈਂ ਆਨਲਾਈਨ ਪੜ੍ਹਦਾ ਹਾਂ। (main "
"online parhda haan.) I study online. 19. ਇਹ ਖ਼ਬਰ ਸੱਚੀ ਹੈ ਜਾਂ ਝੂਠੀ? (eh khabar "
"sachchi hai jaan jhoothi?) Is this news true or false? 20. ਫ਼ੋਨ ਥੋੜ੍ਹਾ ਦੂਰ "
"ਰੱਖੋ, ਅੱਖਾਂ ਖ਼ਰਾਬ ਹੁੰਦੀਆਂ ਹਨ। (phone thorhaa door rakkho, akkhaan kharaab "
"hundiyaan han.) Keep the phone a little away, eyes get spoiled."
),
"how_it_works": (
"Technology Punjabi borrows the English noun and Punjabi-fies the verb: ਫ਼ੋਨ "
"ਕਰਨਾ (to phone), ਡਾਊਨਲੋਡ ਹੋਣਾ (to download), ਅੱਪਡੇਟ ਕਰਨਾ (to update), ਚੈੱਕ "
"ਕਰਨਾ (to check). ਚੱਲਣਾ (challnaa, 'to walk/move') does the work of 'working': "
"ਨੈੱਟ ਨਹੀਂ ਚੱਲ ਰਿਹਾ (the net is not walking = not working). ਹੋਣਾ (honaa, 'to "
"become') marks state changes: ਬੈਟਰੀ ਖ਼ਤਮ ਹੋ ਗਈ (battery finished-became). "
"Troubleshooting follows the pattern 'X ਨਹੀਂ ਚੱਲ ਰਿਹਾ / ਆ ਰਿਹਾ' - name the "
"thing, negate the motion. The closing health note is real advice Punjabi "
"parents give: ਫ਼ੋਨ ਥੋੜ੍ਹਾ ਦੂਰ ਰੱਖੋ."
),
"key_points": [
"20 sentences: phone, internet, computer, messaging.",
"Borrowed nouns + Punjabi verbs: ਫ਼ੋਨ ਕਰਨਾ, ਡਾਊਨਲੋਡ ਹੋਣਾ, ਅੱਪਡੇਟ ਕਰਨਾ.",
"ਚੱਲਣਾ = working (ਨੈੱਟ ਨਹੀਂ ਚੱਲ ਰਿਹਾ).",
"ਹੋਣਾ marks state change: ਬੈਟਰੀ ਖ਼ਤਮ ਹੋ ਗਈ।",
"Troubleshooting frame: X ਨਹੀਂ ਚੱਲ/ਆ ਰਿਹਾ।",
"Media literacy line: ਇਹ ਖ਼ਬਰ ਸੱਚੀ ਹੈ ਜਾਂ ਝੂਠੀ?",
],
"requirements": [
"Explain a phone problem and its fix in four sentences.",
"Give five instructions for using a new app.",
],
"standards": [
"Sentence frames per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: technology is the new post - the message still needs a "
"seal, only now the seal is a password and the courier is the net. The "
"Signature Language Method files tech talk under 'the fast oath': same "
"grammar, new instruments, zero confusion."),
},
# ------------------------------------------------------- 21 verb tenses
{
"key": "tenses",
"name": "Punjabi Verb Tenses in Sentences",
"group": "grammar",
"ladder_rank": 7,
"ladder_tier": "advanced",
"description": (
"The Punjabi tense system in sentences - present, past, and future, five or "
"more translated sentences per tense, built on the verb ਖਾਣਾ (khaanaa, to eat). "
"Present habitual (-ਦਾ/-ਦੀ/-ਦੇ + ਹੈ-family): 1. ਮੈਂ ਰੋਟੀ ਖਾਂਦਾ ਹਾਂ। (main roti "
"khaanda haan.) I eat bread. (male) 2. ਮੈਂ ਰੋਟੀ ਖਾਂਦੀ ਹਾਂ। (main roti khaandi "
"haan.) I eat bread. (female) 3. ਤੁਸੀਂ ਚਾਹ ਪੀਂਦੇ ਹੋ। (tusin chaa peende ho.) "
"You drink tea. 4. ਉਹ ਸਕੂਲ ਜਾਂਦਾ ਹੈ। (oh school jaanda hai.) He goes to school. "
"5. ਅਸੀਂ ਪੰਜਾਬੀ ਬੋਲਦੇ ਹਾਂ। (asin panjaabi bolde haan.) We speak Punjabi. 6. ਉਹ "
"ਖੇਡਦੇ ਹਨ। (oh khedde han.) They play. Present continuous (stem + ਰਿਹਾ/ਰਹੀ/ਰਹੇ + "
"ਹੈ-family): 7. ਮੈਂ ਖਾਣਾ ਖਾ ਰਿਹਾ ਹਾਂ। (main khaana khaa rihaa haan.) I am eating "
"food. 8. ਉਹ ਗਾਣਾ ਗਾ ਰਹੀ ਹੈ। (oh gaanaa gaa rahi hai.) She is singing a song. 9. "
"ਬੱਚੇ ਬਾਹਰ ਖੇਡ ਰਹੇ ਹਨ। (bacche baahar khed rahe han.) The children are playing "
"outside. Past simple - completed action (-ਇਆ/-ਈ/-ਏ, ergative ਨੇ with transitive "
"verbs): 10. ਮੈਂ ਨੇ ਰੋਟੀ ਖਾਧੀ। (main ne roti khaadhi.) I ate the bread. 11. ਉਸਨੇ "
"ਚਾਹ ਪੀਤੀ। (usne chaa peeti.) He/she drank the tea. 12. ਅਸੀਂ ਫਿਲਮ ਦੇਖੀ। (asin "
"film dekhi.) We watched the film. 13. ਉਹ ਸਕੂਲ ਗਿਆ। (oh school gayaa.) He went "
"to school. (intransitive - no ਨੇ) 14. ਬੱਚਾ ਸੌਂ ਗਿਆ। (baccha saun gayaa.) The "
"child fell asleep. Past continuous (ਰਿਹਾ ਸੀ-family): 15. ਮੈਂ ਪੜ੍ਹ ਰਿਹਾ ਸੀ। "
"(main parh rihaa see.) I was studying. 16. ਉਹ ਖਾਣਾ ਬਣਾ ਰਹੀ ਸੀ। (oh khaana "
"banaa rahi see.) She was cooking food. Future (-ਾਂਗਾ/-ੇਗਾ/-ੇਗੀ/-ਾਂਗੇ): 17. ਮੈਂ "
"ਕੱਲ੍ਹ ਆਵਾਂਗਾ। (main kallh aavaangaa.) I will come tomorrow. (male) 18. ਮੈਂ "
"ਕੱਲ੍ਹ ਆਵਾਂਗੀ। (main kallh aavaangi.) I will come tomorrow. (female) 19. ਉਹ "
"ਪੰਜਾਬੀ ਸਿੱਖੇਗਾ। (oh panjaabi sikkhegaa.) He will learn Punjabi. 20. ਅਸੀਂ "
"ਮਿਲਾਂਗੇ। (asin milaange.) We will meet. 21. ਤੁਸੀਂ ਜ਼ਰੂਰ ਆਓਗੇ। (tusin zaroor "
"aaoge.) You will definitely come. Imperative mood: 22. ਖਾਣਾ ਖਾਓ। (khaana "
"khaao.) Eat the food. (formal/plural) 23. ਇੱਥੇ ਬੈਠ। (itthe baith.) Sit here. "
"(informal) The system: present uses -ਦਾ endings with ਹੈ/ਹਾਂ/ਹੋ/ਹਨ; completed "
"past uses -ਇਆ endings with ਨੇ on transitive subjects and agreement with the "
"object; future uses -ਾਂਗਾ endings with no auxiliary; continuous uses ਰਿਹਾ with "
"ਹੈ (now) or ਸੀ (then)."
),
"how_it_works": (
"Build any tense in three steps: take the stem (ਖਾ from ਖਾਣਾ), pick the tense "
"marker, add the person/gender/number ending. Present habitual: stem + ਦਾ/ਦੀ/ਦੇ "
"+ ਹੈ-family (ਖਾਂਦਾ ਹਾਂ). Present continuous: stem + ਰਿਹਾ/ਰਹੀ/ਰਹੇ + ਹੈ-family "
"(ਖਾ ਰਿਹਾ ਹਾਂ) - use it for 'right now'. Completed past: stem + ਇਆ/ਈ/ਏ, and if "
"the verb takes an object, mark the subject with ਨੇ and make the verb agree "
"with the OBJECT (ਮੈਂ ਨੇ ਰੋਟੀ ਖਾਧੀ - ਖਾਧੀ is feminine because ਰੋਟੀ is). "
"Intransitive past needs no ਨੇ (ਉਹ ਗਿਆ). Future: stem + ਾਂਗਾ/ੇਗਾ/ੇਗੀ/ਾਂਗੇ, no "
"auxiliary (ਆਵਾਂਗਾ). Past continuous swaps ਹੈ for ਸੀ (ਰਿਹਾ ਸੀ). Drill one verb "
"through all six persons in each tense before moving to the next verb."
),
"key_points": [
"Present habitual: -ਦਾ/-ਦੀ/-ਦੇ + ਹੈ/ਹਾਂ/ਹੋ/ਹਨ.",
"Present continuous: stem + ਰਿਹਾ/ਰਹੀ/ਰਹੇ + ਹੈ-family (right now).",
"Completed past: -ਇਆ/-ਈ/-ਏ; transitive subjects take ਨੇ; verb agrees with the OBJECT.",
"Intransitive past takes no ਨੇ: ਉਹ ਗਿਆ।",
"Past continuous: ਰਿਹਾ/ਰਹੀ/ਰਹੇ + ਸੀ-family.",
"Future: -ਾਂਗਾ/-ੇਗਾ/-ੇਗੀ/-ਾਂਗੇ, no auxiliary.",
"Imperative: stem + ਓ (formal), bare stem (informal).",
],
"requirements": [
"Conjugate ਖਾਣਾ, ਜਾਣਾ, ਕਰਨਾ in all six persons across present, past, and future.",
"Convert ten present sentences to completed past with the ergative flip.",
],
"standards": [
"Tense-aspect analysis per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
"Gill, Harjit Singh and Gleason, Henry A. A Reference Grammar of Punjabi, 1969.",
],
"sig_lens": (
"His Signature reading: tense is the time-seal on the verb - ਹਾਂ stamps now, "
"ਸੀ stamps then, -ਾਂਗਾ stamps tomorrow, ਨੇ counter-signs the completed deed. "
"The Signature Language Method teaches the ergative flip as the honest clause: "
"when the act is finished, the object signs the verb, not the actor."),
},
# ------------------------------------------------------- 22 questions and answers
{
"key": "qa",
"name": "Punjabi Questions and Answers",
"group": "grammar",
"ladder_rank": 7,
"ladder_tier": "advanced",
"description": (
"Twenty question-and-answer pairs covering who, what, where, when, why, and "
"how. 1. ਤੁਹਾਡਾ ਨਾਂ ਕੀ ਹੈ? - ਮੇਰਾ ਨਾਂ ਸਿਮਰਨ ਹੈ। (tuhada naan ki hai? - mera naan "
"Simran hai.) What is your name? - My name is Simran. 2. ਤੁਸੀਂ ਕਿੱਥੇ ਰਹਿੰਦੇ ਹੋ? "
"- ਮੈਂ ਲੁਧਿਆਣੇ ਵਿੱਚ ਰਹਿੰਦਾ ਹਾਂ। (tusin kitthe rahinde ho? - main Ludhiane vich "
"rahinda haan.) Where do you live? - I live in Ludhiana. 3. ਤੁਸੀਂ ਕੀ ਕਰਦੇ ਹੋ? - "
"ਮੈਂ ਪੜ੍ਹਦਾ ਹਾਂ। (tusin ki karde ho? - main parhda haan.) What do you do? - I "
"study. 4. ਇਹ ਕੌਣ ਹੈ? - ਇਹ ਮੇਰਾ ਭਰਾ ਹੈ। (eh kaun hai? - eh mera bharaa hai.) "
"Who is this? - This is my brother. 5. ਤੁਸੀਂ ਕਦੋਂ ਆਓਗੇ? - ਮੈਂ ਕੱਲ੍ਹ ਆਵਾਂਗਾ। "
"(tusin kadon aaoge? - main kallh aavaangaa.) When will you come? - I will come "
"tomorrow. 6. ਤੁਸੀਂ ਕਿਉਂ ਨਹੀਂ ਆਏ? - ਮੈਂ ਬਿਮਾਰ ਸੀ। (tusin kion nahin aaye? - main "
"bimaar see.) Why did you not come? - I was ill. 7. ਇਹ ਕਿਵੇਂ ਬਣਿਆ? - ਮਾਂ ਨੇ "
"ਬਣਾਇਆ। (eh kiven baniyaa? - maan ne banaayaa.) How was this made? - Mother "
"made it. 8. ਕੀ ਤੁਸੀਂ ਪੰਜਾਬੀ ਬੋਲਦੇ ਹੋ? - ਹਾਂ ਜੀ, ਥੋੜ੍ਹੀ ਥੋੜ੍ਹੀ। (ki tusin panjaabi "
"bolde ho? - haan ji, thorhi thorhi.) Do you speak Punjabi? - Yes, a little. 9. "
"ਕੀ ਖਾਣਾ ਤਿਆਰ ਹੈ? - ਹਾਂ, ਆਓ ਖਾਈਏ। (ki khaana tiyaar hai? - haan, aao khaaie.) "
"Is the food ready? - Yes, come, let us eat. 10. ਇਹ ਕਿੰਨੇ ਦਾ ਹੈ? - ਸੌ ਰੁਪਏ ਦਾ। "
"(eh kinne da hai? - sau rupaye da.) How much is this? - A hundred rupees. 11. "
"ਕਿੰਨੇ ਵਜੇ ਹਨ? - ਤਿੰਨ ਵਜੇ ਹਨ। (kinne vaje han? - tinn vaje han.) What time is it? "
"- It is three o'clock. 12. ਤੁਹਾਡੀ ਉਮਰ ਕਿੰਨੀ ਹੈ? - ਮੈਂ ਵੀਹ ਸਾਲ ਦਾ ਹਾਂ। (tuhadi "
"umar kinni hai? - main veeh saal da haan.) How old are you? - I am twenty years "
"old. 13. ਕੀ ਮੈਂ ਅੰਦਰ ਆ ਸਕਦਾ ਹਾਂ? - ਹਾਂ ਜੀ, ਆਓ। (ki main andar aa sakdaa haan? - "
"haan ji, aao.) May I come in? - Yes, please come. 14. ਰੇਲਵੇ ਸਟੇਸ਼ਨ ਕਿੱਥੇ ਹੈ? - "
"ਸਿੱਧਾ ਜਾਓ, ਸੱਜੇ ਪਾਸੇ ਹੈ। (relve station kitthe hai? - siddhaa jaao, sajje paase "
"hai.) Where is the railway station? - Go straight, it is on the right. 15. "
"ਤੁਹਾਨੂੰ ਕੀ ਚਾਹੀਦਾ ਹੈ? - ਮੈਨੂੰ ਪਾਣੀ ਚਾਹੀਦਾ ਹੈ। (tuhaanun ki chaheeda hai? - "
"mainun paani chaheeda hai.) What do you need? - I need water. 16. ਕਿਹੜੀ ਕਿਤਾਬ "
"ਚੰਗੀ ਹੈ? - ਇਹ ਵਾਲੀ। (kihri kitaab changi hai? - eh vaali.) Which book is good? "
"- This one. 17. ਤੁਸੀਂ ਕਿੱਥੋਂ ਆਏ ਹੋ? - ਮੈਂ ਦਿੱਲੀ ਤੋਂ ਆਇਆ ਹਾਂ। (tusin kitthon aaye "
"ho? - main Dilli ton aayaa haan.) Where have you come from? - I have come from "
"Delhi. 18. ਕੀ ਹਾਲ ਹੈ? - ਬਹੁਤ ਵਧੀਆ, ਤੁਸੀਂ ਸੁਣਾਓ। (ki haal hai? - bahut vadheeyaa, "
"tusin sunaao.) How are you? - Very well, you tell. 19. ਮੌਸਮ ਕਿਵੇਂ ਹੈ? - ਬਹੁਤ "
"ਸੋਹਣਾ ਹੈ। (mausam kiven hai? - bahut sohnaa hai.) How is the weather? - Very "
"nice. 20. ਕੀ ਤੁਸੀਂ ਮੇਰੀ ਮਦਦ ਕਰੋਗੇ? - ਜ਼ਰੂਰ, ਦੱਸੋ ਕੀ ਕਰਨਾ ਹੈ। (ki tusin meri madad "
"karoge? - zaroor, dasso ki karnaa hai.) Will you help me? - Of course, tell me "
"what to do."
),
"how_it_works": (
"Two question engines: front ਕੀ (ki) for yes/no questions answered with ਹਾਂ/ਨਹੀਂ, "
"and the content words for everything else - ਕੌਣ (who), ਕੀ (what), ਕਿੱਥੇ "
"(where), ਕਦੋਂ (when), ਕਿਉਂ (why), ਕਿਵੇਂ (how), ਕਿੰਨਾ (how much/many), ਕਿਹੜਾ "
"(which). Answers mirror the question's verb: ਕਦੋਂ ਆਓਗੇ? (when will you come?) "
"is answered ਆਵਾਂਗਾ (I will come) - same future, first person. Permission uses "
"ਸਕਣਾ (saknaa, 'can'): ਕੀ ਮੈਂ ਆ ਸਕਦਾ ਹਾਂ? Offers use the future: ਚਾਹ ਪੀਓਗੇ? "
"The return question ਤੁਸੀਂ ਸੁਣਾਓ ('you tell') keeps conversations alive - learn "
"it as a reflex."
),
"key_points": [
"20 Q/A pairs across who/what/where/when/why/how.",
"ਕੀ fronts yes/no questions; ਹਾਂ/ਨਹੀਂ answer them.",
"Content words: ਕੌਣ, ਕੀ, ਕਿੱਥੇ, ਕਦੋਂ, ਕਿਉਂ, ਕਿਵੇਂ, ਕਿੰਨਾ, ਕਿਹੜਾ.",
"Answers mirror the question's tense and person.",
"Permission frame: ਕੀ ਮੈਂ X ਸਕਦਾ ਹਾਂ?",
"Conversation keeper: ਤੁਸੀਂ ਸੁਣਾਓ (you tell).",
],
"requirements": [
"Ask and answer all twenty pairs with a partner, swapping roles.",
"Interview someone for five minutes using only the content words.",
],
"standards": [
"Interrogative syntax per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: questions are summons and answers are testimony - ਕੀ "
"the summons seal, ਹਾਂ ਜੀ the sworn reply. The Signature Language Method "
"drills Q/A as courtroom call-and-response until the mirror reflex (matching "
"tense, matching person) is automatic."),
},
# ------------------------------------------------------- 23 commands and requests
{
"key": "commands",
"name": "Punjabi Commands and Requests",
"group": "grammar",
"ladder_rank": 8,
"ladder_tier": "advanced",
"description": (
"Twenty imperatives and polite requests, formal versus informal. Formal/plural "
"(safe default - the -ਓ ending): 1. ਇੱਥੇ ਆਓ। (itthe aao.) Come here. 2. ਬੈਠੋ, "
"ਚਾਹ ਪੀਓ। (baitho, chaa peeo.) Sit, have tea. 3. ਕਿਤਾਬ ਖੋਲ੍ਹੋ। (kitaab kholho.) "
"Open the book. 4. ਧਿਆਨ ਨਾਲ ਸੁਣੋ। (dhiaan naal suno.) Listen carefully. 5. "
"ਦਰਵਾਜ਼ਾ ਬੰਦ ਕਰੋ। (darvaazaa band karo.) Close the door. 6. ਜਲਦੀ ਆਓ। (jaldi "
"aao.) Come quickly. 7. ਮੇਰੀ ਮਦਦ ਕਰੋ। (meri madad karo.) Help me. 8. ਇਹ ਕੰਮ "
"ਕੱਲ੍ਹ ਤੱਕ ਕਰ ਦਿਓ। (eh kamm kallh takk kar dio.) Please do this work by tomorrow. "
"9. ਕਿਰਪਾ ਕਰਕੇ ਥੋੜ੍ਹਾ ਰੁਕੋ। (kirpaa karke thorhaa ruko.) Please wait a little. "
"10. ਸ਼ਾਂਤ ਰਹੋ। (shaant raho.) Stay calm. Informal singular (friends, children "
"- the bare stem): 11. ਇੱਥੇ ਆ। (itthe aa.) Come here. 12. ਬੈਠ, ਗੱਲ ਸੁਣ। "
"(baith, gall sun.) Sit, listen. 13. ਖਾਣਾ ਖਾ। (khaana khaa.) Eat the food. 14. "
"ਜਲਦੀ ਕਰ। (jaldi kar.) Hurry up. 15. ਮੈਨੂੰ ਦੇ। (mainun de.) Give me. (intimate) "
"Polite requests (softeners that make commands gentle): 16. ਕੀ ਤੁਸੀਂ ਖਿੜਕੀ "
"ਖੋਲ੍ਹ ਸਕਦੇ ਹੋ? (ki tusin khirhki kholh sakde ho?) Could you open the window? 17. "
"ਮੈਨੂੰ ਇੱਕ ਗਲਾਸ ਪਾਣੀ ਦੇ ਦਿਓ। (mainun ikk glaas paani de dio.) Please give me a "
"glass of water. 18. ਜੇ ਹੋ ਸਕੇ ਤਾਂ ਕੱਲ੍ਹ ਆ ਜਾਓ। (je ho sake taan kallh aa jaao.) "
"If possible, come tomorrow. 19. ਮਾਫ਼ ਕਰਨਾ, ਥੋੜ੍ਹਾ ਪਾਸੇ ਹੋ ਜਾਓ। (maaf karnaa, "
"thorhaa paase ho jaao.) Excuse me, please move aside a little. 20. ਰੱਬ ਤੁਹਾਡਾ "
"ਭਲਾ ਕਰੇ, ਬਹੁਤ ਮਦਦ ਕੀਤੀ। (rabb tuhada bhalaa kare, bahut madad keeti.) God bless "
"you, you helped a lot. (thanks after a request)"
),
"how_it_works": (
"The imperative has two gears: the bare stem for intimates (ਆ, ਖਾ, ਕਰ) and the "
"-ਓ ending for everyone else (ਆਓ, ਖਾਓ, ਕਰੋ). When in doubt, use -ਓ - it is never "
"rude. Soften any command with ਕਿਰਪਾ ਕਰਕੇ (please) in front or ਦਿਓ (please "
"give/do) at the end: ਕਰੋ (do it) becomes ਕਰ ਦਿਓ (please do it). The gentlest "
"requests are questions with ਸਕਣਾ (can): ਕੀ ਤੁਸੀਂ ਖੋਲ੍ਹ ਸਕਦੇ ਹੋ? Conditions "
"soften further: ਜੇ ਹੋ ਸਕੇ ਤਾਂ (if possible). Prohibitions use ਨਾ or ਮਤ before "
"the stem: ਨਾ ਜਾਓ (do not go), ਮਤ ਰੋ (do not cry - informal). Never use the bare "
"stem with elders or strangers - that gear is for friends and children only."
),
"key_points": [
"20 imperatives and polite requests, formal vs informal.",
"Two gears: bare stem (intimate: ਆ, ਖਾ) vs -ਓ ending (formal/plural: ਆਓ, ਖਾਓ).",
"Default to -ਓ with strangers and elders - never rude.",
"Softeners: ਕਿਰਪਾ ਕਰਕੇ (front), ਦਿਓ (end), ਸਕਣਾ-questions, ਜੇ ਹੋ ਸਕੇ ਤਾਂ.",
"Prohibitions: ਨਾ/ਮਤ + stem (ਨਾ ਜਾਓ, ਮਤ ਰੋ).",
"Thanks after help: ਰੱਬ ਤੁਹਾਡਾ ਭਲਾ ਕਰੇ।",
],
"requirements": [
"Give ten orders in both gears and feel the respect difference.",
"Make five requests three ways: blunt, softened, question-form.",
],
"standards": [
"Imperative morphology per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: the imperative is the order-seal - bare stem the "
"commander's seal for intimates, -ਓ the officer's seal for the ranks. The "
"Signature Language Method teaches softeners as the wax on the seal: ਕਿਰਪਾ "
"ਕਰਕੇ and ਦਿਓ keep every order from cracking."),
},
# ------------------------------------------------------- 24 descriptions
{
"key": "descriptions",
"name": "Punjabi Descriptions of People and Places",
"group": "sentences",
"ladder_rank": 8,
"ladder_tier": "advanced",
"description": (
"Twenty sentences describing people, places, and things in detail. 1. ਮੇਰਾ "
"ਦੋਸਤ ਲੰਬਾ, ਗੋਰਾ, ਅਤੇ ਹੱਸਮੁੱਖ ਹੈ। (mera dost lamba, goraa, ate hassmukh hai.) "
"My friend is tall, fair, and cheerful. 2. ਉਸਦੀਆਂ ਅੱਖਾਂ ਕਾਲੀਆਂ ਅਤੇ ਵੱਡੀਆਂ ਹਨ। "
"(usdiyaan akkhaan kaaliyaan ate vaddiyaan han.) Her eyes are black and large. "
"3. ਬਜ਼ੁਰਗ ਆਦਮੀ ਦੀ ਦਾੜ੍ਹੀ ਚਿੱਟੀ ਹੈ। (bazurg aadmi di daarhi chitti hai.) The old "
"man's beard is white. 4. ਕੁੜੀ ਨੇ ਲਾਲ ਸੂਟ ਪਾਇਆ ਹੋਇਆ ਹੈ। (kurhi ne laal suit "
"paayaa hoyaa hai.) The girl is wearing a red suit. 5. ਉਹ ਹਮੇਸ਼ਾ ਮੁਸਕਰਾਉਂਦਾ ਹੈ। "
"(oh hameshaa muskaraaundaa hai.) He always smiles. 6. ਮੇਰੀ ਦਾਦੀ ਦੀ ਆਵਾਜ਼ ਬਹੁਤ "
"ਮਿੱਠੀ ਹੈ। (meri daadi di aavaaz bahut mitthi hai.) My grandmother's voice is "
"very sweet. 7. ਅੰਮ੍ਰਿਤਸਰ ਇੱਕ ਪਵਿੱਤਰ ਅਤੇ ਸੁੰਦਰ ਸ਼ਹਿਰ ਹੈ। (Amritsar ikk pavittar "
"ate sundar shehar hai.) Amritsar is a holy and beautiful city. 8. ਸੁਨਹਿਰੀ "
"ਮੰਦਰ ਸਰੋਵਰ ਦੇ ਵਿਚਕਾਰ ਹੈ। (Sunahiri Mandar sarovar de vichkaar hai.) The Golden "
"Temple is in the middle of the holy pool. 9. ਪਿੰਡ ਹਰਾ ਭਰਾ ਅਤੇ ਸ਼ਾਂਤ ਹੈ। (pind "
"haraa bharaa ate shaant hai.) The village is green and peaceful. 10. ਖੇਤਾਂ "
"ਵਿੱਚ ਪੀਲੀ ਸਰਸੋਂ ਖਿੜੀ ਹੈ। (khetaan vich peeli sarson khirhi hai.) Yellow mustard "
"blooms in the fields. 11. ਸ਼ਹਿਰ ਦੀਆਂ ਗਲੀਆਂ ਭਰੀਆਂ ਹੋਈਆਂ ਹਨ। (shehar diy aan "
"galiyaan bhariyaan hoiyaan han.) The city streets are crowded. 12. ਇਹ ਇਮਾਰਤ "
"ਬਹੁਤ ਉੱਚੀ ਹੈ। (eh imaarat bahut ucchi hai.) This building is very tall. 13. "
"ਕਮਰਾ ਸਾਫ਼ ਸੁਥਰਾ ਅਤੇ ਹਵਾਦਾਰ ਹੈ। (kamraa saaf suthraa ate havaadaar hai.) The "
"room is clean and airy. 14. ਬਾਗ਼ ਵਿੱਚ ਰੰਗ ਬਰੰਗੇ ਫੁੱਲ ਹਨ। (baagh vich rang "
"barange phull han.) There are colorful flowers in the garden. 15. ਦਰਿਆ ਦਾ "
"ਪਾਣੀ ਸਾਫ਼ ਅਤੇ ਠੰਡਾ ਹੈ। (dariyaa da paani saaf ate thandaa hai.) The river water "
"is clean and cold. 16. ਪਹਾੜਾਂ ਉੱਤੇ ਬਰਫ਼ ਜਮੀ ਹੋਈ ਹੈ। (pahaarhaan utte baraf "
"jami hoi hai.) Snow lies frozen on the mountains. 17. ਸੂਰਜ ਡੁੱਬ ਰਿਹਾ ਹੈ, "
"ਅਸਮਾਨ ਲਾਲ ਹੈ। (sooraj dubb rihaa hai, asmaan laal hai.) The sun is setting, "
"the sky is red. 18. ਇਹ ਪੁਰਾਣੀ ਹਵੇਲੀ ਸੌ ਸਾਲ ਪੁਰਾਣੀ ਹੈ। (eh puraani haveli sau "
"saal puraani hai.) This old mansion is a hundred years old. 19. ਬਾਜ਼ਾਰ ਵਿੱਚ "
"ਰੌਣਕ ਲੱਗੀ ਹੋਈ ਹੈ। (bazaar vich raunak laggi hoi hai.) The market is lively. "
"20. ਪੰਜਾਬ ਧਰਤੀ ਸੋਨੇ ਵਰਗੀ ਹੈ। (Panjaab dharti sone vargi hai.) Punjab's land is "
"like gold."
),
"how_it_works": (
"Descriptions stack adjectives with ਅਤੇ (ate, 'and'): ਲੰਬਾ, ਗੋਰਾ, ਅਤੇ ਹੱਸਮੁੱਖ "
"(tall, fair, and cheerful) - commas between, ਅਤੇ before the last. Wearing is "
"ਪਾਉਣਾ (paaunaa) in the perfect: ਸੂਟ ਪਾਇਆ ਹੋਇਆ ਹੈ (suit paayaa hoyaa hai, 'has "
"worn'). States that resulted from earlier actions use ਹੋਇਆ/ਹੋਈ (hoyaa/hoi, "
"'become'): ਬਰਫ਼ ਜਮੀ ਹੋਈ ਹੈ (snow has become frozen = lies frozen). Comparisons "
"use ਵਰਗਾ/ਵਰਗੀ (vargaa/vargi, 'like'): ਸੋਨੇ ਵਰਗੀ (like gold). Place descriptions "
"locate first, then paint: ਸਰੋਵਰ ਦੇ ਵਿਚਕਾਰ (in the middle of the pool), ਖੇਤਾਂ "
"ਵਿੱਚ (in the fields). The final line - ਪੰਜਾਬ ਧਰਤੀ ਸੋਨੇ ਵਰਗੀ ਹੈ - is a "
"well-known praise of Punjab's land, usable as a toast."
),
"key_points": [
"20 detailed descriptive sentences.",
"Adjective stacking: X, Y, ਅਤੇ Z.",
"Wearing: ਪਾਇਆ/ਪਾਈ ਹੋਇਆ/ਹੋਈ ਹੈ.",
"Result states: ਹੋਇਆ/ਹੋਈ ਹੈ (has become).",
"Comparison: ਵਰਗਾ/ਵਰਗੀ (like).",
"Locate then paint: place phrase first, colors second.",
],
"requirements": [
"Describe one person and one place in five sentences each.",
"Use ਹੋਇਆ/ਹੋਈ in three descriptions of states.",
],
"standards": [
"Descriptive syntax per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: description is the portrait seal - every adjective a "
"brushstroke, ਅਤੇ the frame, ਵਰਗਾ the likeness sworn true. The Signature "
"Language Method paints in order: locate the subject, stack the colors, stamp "
"the likeness with ਹੋਇਆ."),
},
# ------------------------------------------------------- 25 story I
{
"key": "story1",
"name": "Punjabi Short Story I",
"group": "stories",
"ladder_rank": 8,
"ladder_tier": "advanced",
"description": (
"A ten-sentence simple story in Punjabi - 'A Morning in the Village' - with "
"line-by-line English translation. Simple present and everyday vocabulary. "
"1. ਸਿਮਰਨ ਸਵੇਰੇ ਛੇ ਵਜੇ ਉੱਠਦੀ ਹੈ। (Simran savere chhe vaje utthdi hai.) Simran "
"gets up at six in the morning. 2. ਉਹ ਹੱਥ ਮੂੰਹ ਧੋਂਦੀ ਹੈ। (oh hath munh dhondi "
"hai.) She washes her hands and face. 3. ਮਾਂ ਰਸੋਈ ਵਿੱਚ ਪਰੌਂਠੇ ਬਣਾਉਂਦੀ ਹੈ। (maan "
"rasoi vich paraunthe banaundi hai.) Mother makes parathas in the kitchen. 4. "
"ਸਿਮਰਨ ਦੁੱਧ ਪੀਂਦੀ ਹੈ। (Simran duddh peendi hai.) Simran drinks milk. 5. ਉਹ "
"ਸਕੂਲ ਦਾ ਬਸਤਾ ਚੁੱਕਦੀ ਹੈ। (oh school da bastaa chukkdi hai.) She picks up her "
"school bag. 6. ਉਹ ਆਪਣੀ ਸਹੇਲੀ ਨਾਲ ਸਕੂਲ ਜਾਂਦੀ ਹੈ। (oh aapni saheli naal school "
"jaandi hai.) She goes to school with her friend. 7. ਰਸਤੇ ਵਿੱਚ ਉਹ ਪੰਛੀਆਂ ਨੂੰ "
"ਦੇਖਦੀ ਹੈ। (raste vich oh panchhiyaan nun dekhdi hai.) On the way she watches "
"the birds. 8. ਸਕੂਲ ਵਿੱਚ ਅਧਿਆਪਕ ਪੜ੍ਹਾਉਂਦਾ ਹੈ। (school vich adhiaapak parhaundaa "
"hai.) In school the teacher teaches. 9. ਸਿਮਰਨ ਧਿਆਨ ਨਾਲ ਸੁਣਦੀ ਹੈ। (Simran "
"dhiaan naal sundi hai.) Simran listens carefully. 10. ਸ਼ਾਮ ਨੂੰ ਉਹ ਹੱਸਦੀ ਹੋਈ "
"ਘਰ ਆਉਂਦੀ ਹੈ। (shaam nun oh hassdi hoi ghar aaundi hai.) In the evening she "
"comes home smiling."
),
"how_it_works": (
"This is the whole foundations ladder inside one story: SOV order, -ਦੀ "
"feminine present endings (ਉੱਠਦੀ, ਧੋਂਦੀ, ਬਣਾਉਂਦੀ), postpositions (ਰਸੋਈ ਵਿੱਚ, "
"ਰਸਤੇ ਵਿੱਚ, ਸਹੇਲੀ ਨਾਲ), time words (ਸਵੇਰੇ, ਸ਼ਾਮ ਨੂੰ), and the ਹੈ auxiliary. "
"Read it three ways: first for meaning with the translations, second aloud "
"shadowing the rhythm, third with the translations covered, retelling each "
"line in English from the Punjabi. Every verb is feminine singular present - "
"change the hero to a boy and re-conjugate: ਉੱਠਦਾ, ਧੋਂਦਾ, ਬਣਾਉਂਦਾ."
),
"key_points": [
"10-sentence story, line-by-line English translation.",
"All verbs in feminine singular present (-ਦੀ): one tense, fully drilled.",
"SOV order, postpositions, and time words in natural use.",
"Retelling drill: cover the English, rebuild it from the Punjabi.",
"Gender-flip drill: rewrite with a male hero (-ਦਾ endings).",
],
"requirements": [
"Retell the whole story in English from the Punjabi alone.",
"Rewrite the story with a male hero, fixing every verb.",
],
"standards": [
"Narrative present per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: the first story is the maiden voyage - one heroine, "
"one morning, one tense, signed clean. The Signature Language Method launches "
"small boats before ships: master one tense in ten sentences and the ocean of "
"the language stops looking wide."),
},
# ------------------------------------------------------- 26 story II
{
"key": "story2",
"name": "Punjabi Short Story II",
"group": "stories",
"ladder_rank": 9,
"ladder_tier": "advanced",
"description": (
"A ten-sentence story in the past tense - 'A Day at the Fair' - with "
"line-by-line English translation. 1. ਕੱਲ੍ਹ ਅਸੀਂ ਮੇਲੇ ਵਿੱਚ ਗਏ। (kallh asin "
"mele vich gaye.) Yesterday we went to the fair. 2. ਮੇਲਾ ਬਹੁਤ ਵੱਡਾ ਸੀ। (melaa "
"bahut vaddaa see.) The fair was very big. 3. ਉੱਥੇ ਬਹੁਤ ਸਾਰੇ ਲੋਕ ਆਏ ਹੋਏ ਸਨ। "
"(utthe bahut saare lok aaye hoye san.) Many people had come there. 4. ਮੈਂ ਨੇ "
"ਝੂਲੇ ਲਏ। (main ne jhoole laye.) I took rides on the swings. 5. ਮੇਰੇ ਭਰਾ ਨੇ "
"ਮਠਿਆਈ ਖਾਧੀ। (mere bharaa ne mithiaai khaadhi.) My brother ate sweets. (note: "
"ਖਾਧੀ feminine, agreeing with ਮਠਿਆਈ) 6. ਅਸੀਂ ਖਿਡੌਣੇ ਖਰੀਦੇ। (asin khidaune "
"khareede.) We bought toys. 7. ਢੋਲ ਵੱਜਿਆ ਅਤੇ ਲੋਕ ਨੱਚੇ। (dhol vajjiyaa ate lok "
"nacche.) The drum played and people danced. 8. ਸੂਰਜ ਡੁੱਬ ਗਿਆ। (sooraj dubb "
"gayaa.) The sun set. 9. ਅਸੀਂ ਖੁਸ਼ੀ ਖੁਸ਼ੀ ਘਰ ਆਏ। (asin khushi khushi ghar aaye.) "
"We came home happily. 10. ਇਹ ਦਿਨ ਮੈਨੂੰ ਹਮੇਸ਼ਾ ਯਾਦ ਰਹੇਗਾ। (eh din mainun "
"hameshaa yaad rahegaa.) I will always remember this day."
),
"how_it_works": (
"The past-tense engine room: ਗਏ/ਆਏ/ਲਏ/ਖਰੀਦੇ (went/came/took/bought) show the "
"-ਏ past endings, ਸੀ/ਸਨ (was/were) sets the scene, and ਲਏ/ਖਾਧੀ/ਖਰੀਦੇ show the "
"ergative agreement - ਮੈਂ ਨੇ ਝੂਲੇ ਲਏ (ਲਏ plural, agreeing with ਝੂਲੇ), ਮੇਰੇ ਭਰਾ "
"ਨੇ ਮਠਿਆਈ ਖਾਧੀ (ਖਾਧੀ feminine, agreeing with ਮਠਿਆਈ). ਆਏ ਹੋਏ ਸਨ is the past "
"perfect ('had come'). The final line jumps to the future (ਯਾਦ ਰਹੇਗਾ) - stories "
"are allowed to land in any tense. Retell it watching every verb: who agrees "
"with whom, and why."
),
"key_points": [
"10-sentence past-tense story, line-by-line translation.",
"Ergative agreement drilled live: ਲਏ (plural), ਖਾਧੀ (feminine), ਖਰੀਦੇ (plural).",
"ਸੀ/ਸਨ sets the scene; ਆਏ ਹੋਏ ਸਨ is the past perfect.",
"Intransitive past needs no ਨੇ: ਅਸੀਂ ਗਏ।",
"Final line lands in the future - tenses can mix at the close.",
],
"requirements": [
"Mark every verb and write what it agrees with.",
"Retell the fair day as if it happens tomorrow (future tense).",
],
"standards": [
"Past-tense narrative per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: the past is the sealed archive - ਨੇ the witness "
"stamp, the object the co-signer. The Signature Language Method reads Story "
"II as an audit: every completed action filed, every verb signed by the "
"object it acted upon."),
},
# ------------------------------------------------------- 27 story III
{
"key": "story3",
"name": "Punjabi Short Story III",
"group": "stories",
"ladder_rank": 9,
"ladder_tier": "advanced",
"description": (
"A ten-sentence story in the future and conditional - 'The School We Will "
"Build' - with line-by-line English translation. 1. ਸਾਡੇ ਪਿੰਡ ਵਿੱਚ ਸਕੂਲ ਨਹੀਂ "
"ਹੈ। (saade pind vich school nahin hai.) There is no school in our village. 2. "
"ਬੱਚੇ ਦੂਰ ਪੜ੍ਹਨ ਜਾਂਦੇ ਹਨ। (bacche door parhan jaande han.) The children go far "
"to study. 3. ਅਸੀਂ ਇੱਕ ਸਕੂਲ ਬਣਾਵਾਂਗੇ। (asin ikk school banaavaange.) We will "
"build a school. 4. ਸਾਰੇ ਪਿੰਡ ਵਾਲੇ ਮਦਦ ਕਰਨਗੇ। (saare pind vaale madad karange.) "
"All the villagers will help. 5. ਜੇ ਪੈਸੇ ਇਕੱਠੇ ਹੋ ਗਏ ਤਾਂ ਕੰਮ ਸ਼ੁਰੂ ਹੋਵੇਗਾ। (je "
"paise ikatthe ho gaye taan kamm shuru hovegaa.) If the money is collected, "
"the work will begin. 6. ਮੈਂ ਅਧਿਆਪਕ ਬਣਾਂਗੀ। (main adhiaapak banaangi.) I will "
"become a teacher. (female speaker) 7. ਬੱਚੇ ਖੁਸ਼ੀ ਨਾਲ ਪੜ੍ਹਨਗੇ। (bacche khushi "
"naal parhange.) The children will study happily. 8. ਸਕੂਲ ਵਿੱਚ ਇੱਕ ਵੱਡੀ "
"ਲਾਇਬ੍ਰੇਰੀ ਹੋਵੇਗੀ। (school vich ikk vaddi library hovegi.) There will be a big "
"library in the school. 9. ਜੇ ਤੁਸੀਂ ਆਓਗੇ ਤਾਂ ਅਸੀਂ ਜ਼ਰੂਰ ਜਿੱਤਾਂਗੇ। (je tusin "
"aaoge taan asin zaroor jittaange.) If you come, we will surely win. 10. ਸਾਡਾ "
"ਸੁਪਨਾ ਇੱਕ ਦਿਨ ਸੱਚ ਹੋਵੇਗਾ। (saadaa supnaa ikk din sachch hovegaa.) Our dream "
"will come true one day."
),
"how_it_works": (
"The future toolkit: -ਾਂਗਾ/-ਾਂਗੇ/-ੇਗਾ/-ੇਗੀ endings with no auxiliary - "
"ਬਣਾਵਾਂਗੇ (we will build), ਕਰਨਗੇ (they will help), ਹੋਵੇਗਾ (it will be). The "
"conditional runs on ਜੇ...ਤਾਂ (je...taan, 'if...then'): ਜੇ ਪੈਸੇ ਇਕੱਠੇ ਹੋ ਗਏ "
"ਤਾਂ ਕੰਮ ਸ਼ੁਰੂ ਹੋਵੇਗਾ - note the 'if' clause uses the completed form (ਹੋ ਗਏ) "
"for a future condition, the classic Punjabi conditional shape. ਹੋਵੇਗਾ/ਹੋਵੇਗੀ "
"is the future of ਹੋਣਾ (to be/become) - the workhorse of plans: ਸਕੂਲ ਹੋਵੇਗਾ, "
"ਲਾਇਬ੍ਰੇਰੀ ਹੋਵੇਗੀ. Dreams close with ਸੱਚ ਹੋਣਾ (to come true). Write your own "
"plan-story with five future verbs and one ਜੇ...ਤਾਂ condition."
),
"key_points": [
"10-sentence future/conditional story, line-by-line translation.",
"Future endings: -ਾਂਗਾ/-ਾਂਗੀ/-ੇਗਾ/-ੇਗੀ/-ਾਂਗੇ - no auxiliary.",
"Conditional shape: ਜੇ...ਤਾਂ with completed form in the if-clause.",
"ਹੋਵੇਗਾ/ਹੋਵੇਗੀ: the future of being - the engine of plans.",
"ਸੱਚ ਹੋਣਾ (to come true) closes dream-statements.",
],
"requirements": [
"Write a ten-sentence plan for your own future using five future verbs.",
"Build three ਜੇ...ਤਾਂ conditions about real plans.",
],
"standards": [
"Future and conditional per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: the future is the unsigned draft - -ਾਂਗਾ the pen "
"raised, ਜੇ...ਤਾਂ the clause awaiting its condition. The Signature Language "
"Method files plans as drafts: speak the future firmly and the hand learns "
"to sign what the mouth promises."),
},
# ------------------------------------------------------- 28 idioms and proverbs
{
"key": "idioms",
"name": "Punjabi Idioms and Proverbs",
"group": "sayings",
"ladder_rank": 9,
"ladder_tier": "advanced",
"description": (
"Twenty Punjabi idioms and proverbs - literal translation, real meaning, and "
"an example sentence each. 1. ਜਿਹਾ ਦੇਸ ਤਿਹਾ ਭੇਸ (jihaa des tihaa bhes) - "
"literal: 'as the country, so the dress'; meaning: when in Rome, do as the "
"Romans do. Example: ਨਵੇਂ ਸ਼ਹਿਰ ਵਿੱਚ ਜਿਹਾ ਦੇਸ ਤਿਹਾ ਭੇਸ ਅਪਣਾਓ। (Adopt the local "
"ways in a new city.) 2. ਨੱਚ ਨਾ ਜਾਣੇ ਵਿਹੜਾ ਟੇਢਾ (nach na jaane vihraa tedhaa) - "
"literal: 'cannot dance, says the courtyard is crooked'; meaning: blaming your "
"tools for your own failure. Example: ਹਾਰ ਕੇ ਉਹ ਵਿਹੜਾ ਟੇਢਾ ਕਹਿ ਰਿਹਾ ਹੈ। 3. "
"ਮੂੰਹ ਵਿੱਚ ਰਾਮ ਰਾਮ, ਬਗਲ ਵਿੱਚ ਛੁਰੀ (munh vich raam raam, bagal vich chhuri) - "
"literal: 'Ram Ram on the lips, a knife under the arm'; meaning: hypocrisy. "
"Example: ਉਸਦੇ ਮੂੰਹ ਵਿੱਚ ਰਾਮ ਰਾਮ, ਬਗਲ ਵਿੱਚ ਛੁਰੀ ਹੈ। 4. ਜਿੱਥੇ ਚਾਹ ਉੱਥੇ ਰਾਹ "
"(jitthe chaah utthe raah) - literal: 'where there is desire, there is a road'; "
"meaning: where there is a will, there is a way. Example: ਜਿੱਥੇ ਚਾਹ ਉੱਥੇ ਰਾਹ, "
"ਮਿਹਨਤ ਕਰੋ। 5. ਹੱਥ ਕੰਗਣ ਨੂੰ ਆਰਸੀ ਕੀ (hath kanggan nun aarsi ki) - literal: 'what "
"need of a mirror for the bangle on the wrist'; meaning: the obvious needs no "
"proof. Example: ਉਸਦੀ ਇਮਾਨਦਾਰੀ ਸਭ ਜਾਣਦੇ ਹਨ, ਹੱਥ ਕੰਗਣ ਨੂੰ ਆਰਸੀ ਕੀ। 6. ਦੂਰੋਂ ਢੋਲ "
"ਸੁਹਾਵਣੇ (dooron dhol suhaavne) - literal: 'drums sound sweet from afar'; "
"meaning: the grass is always greener. Example: ਵਿਦੇਸ਼ ਦੇ ਸੁਪਨੇ ਦੂਰੋਂ ਢੋਲ "
"ਸੁਹਾਵਣੇ ਹਨ। 7. ਨੌਂ ਨਕਦ ਨਾ ਤੇਰਾਂ ਉਧਾਰ (naun nakad na teraan udhaar) - literal: "
"'nine in cash, not thirteen on credit'; meaning: a bird in the hand is worth "
"two in the bush. Example: ਨੌਕਰੀ ਲੈ ਲਓ, ਨੌਂ ਨਕਦ ਨਾ ਤੇਰਾਂ ਉਧਾਰ। 8. ਜੋ ਗਰਜਦੇ ਹਨ "
"ਉਹ ਵਰਸਦੇ ਨਹੀਂ (jo garajde han oh varasde nahin) - literal: 'those who thunder "
"do not rain'; meaning: barking dogs seldom bite. Example: ਉਹ ਸਿਰਫ਼ ਗਰਜਦਾ ਹੈ, "
"ਵਰਸਦਾ ਨਹੀਂ। 9. ਬੂੰਦ ਬੂੰਦ ਨਾਲ ਤਲਾਬ ਭਰਦਾ ਹੈ (boond boond naal talaab bhardaa "
"hai) - literal: 'drop by drop the pond fills'; meaning: little by little, "
"great things grow. Example: ਰੋਜ਼ ਥੋੜ੍ਹਾ ਬਚਾਓ, ਬੂੰਦ ਬੂੰਦ ਨਾਲ ਤਲਾਬ ਭਰਦਾ ਹੈ। 10. "
"ਲੋਹਾ ਲੋਹੇ ਨੂੰ ਕੱਟਦਾ ਹੈ (lohaa lohe nun kattdaa hai) - literal: 'iron cuts "
"iron'; meaning: fight fire with fire. Example: ਸਖ਼ਤ ਮੁਕਾਬਲੇ ਵਿੱਚ ਲੋਹਾ ਲੋਹੇ "
"ਨੂੰ ਕੱਟਦਾ ਹੈ। 11. ਸੱਚ ਕੌੜਾ ਹੁੰਦਾ ਹੈ (sachch kauraa hundaa hai) - literal: "
"'truth is bitter'; meaning: the truth hurts. Example: ਸੱਚ ਕੌੜਾ ਹੁੰਦਾ ਹੈ, ਪਰ "
"ਕਹਿਣਾ ਚਾਹੀਦਾ ਹੈ। 12. ਵਕਤ ਸਭ ਤੋਂ ਵੱਡਾ ਉਸਤਾਦ ਹੈ (vakat sabh ton vaddaa ustaad "
"hai) - literal: 'time is the greatest teacher'; meaning: experience teaches "
"all. Example: ਵਕਤ ਸਭ ਤੋਂ ਵੱਡਾ ਉਸਤਾਦ ਹੈ, ਸਬਰ ਕਰੋ। 13. ਮਿਹਨਤ ਦਾ ਫਲ ਮਿੱਠਾ ਹੁੰਦਾ "
"ਹੈ (mehnat da phal mitthaa hundaa hai) - literal: 'the fruit of hard work is "
"sweet'; meaning: effort pays. Example: ਮਿਹਨਤ ਕਰੋ, ਮਿਹਨਤ ਦਾ ਫਲ ਮਿੱਠਾ ਹੁੰਦਾ ਹੈ। "
"14. ਅੱਖੋਂ ਓਹਲੇ ਪਹਾੜ ਓਹਲੇ (akkhon ohle pahaarh ohle) - literal: 'hidden from the "
"eye, hidden behind the mountain'; meaning: out of sight, out of mind. Example: "
"ਦੂਰ ਜਾ ਕੇ ਉਹ ਅੱਖੋਂ ਓਹਲੇ ਪਹਾੜ ਓਹਲੇ ਹੋ ਗਿਆ। 15. ਜਾਨ ਹੈ ਤਾਂ ਜਹਾਨ ਹੈ (jaan hai taan "
"jahaan hai) - literal: 'if there is life, there is the world'; meaning: "
"health is wealth. Example: ਸਿਹਤ ਦਾ ਖ਼ਿਆਲ ਰੱਖੋ, ਜਾਨ ਹੈ ਤਾਂ ਜਹਾਨ ਹੈ। 16. ਕਰ "
"ਭਲਾ ਹੋ ਭਲਾ (kar bhalaa ho bhalaa) - literal: 'do good, get good'; meaning: "
"kindness returns. Example: ਕਰ ਭਲਾ ਹੋ ਭਲਾ, ਮਦਦ ਕਰਦੇ ਰਹੋ। 17. ਖੁਦਾ ਮਿਹਰਬਾਨ ਤੇ "
"ਗਧਾ ਪਹਿਲਵਾਨ (khudaa meharbaan te gadhaa pehalvaan) - literal: 'when God is "
"kind, the donkey becomes a wrestler'; meaning: fortune can lift anyone. "
"Example: ਕਿਸਮਤ ਨੇ ਸਾਥ ਦਿੱਤਾ, ਖੁਦਾ ਮਿਹਰਬਾਨ ਤੇ ਗਧਾ ਪਹਿਲਵਾਨ। 18. ਧੀਰਜ ਦਾ ਫਲ "
"ਮਿੱਠਾ (dheeraj da phal mitthaa) - literal: 'the fruit of patience is sweet'; "
"meaning: patience pays. Example: ਧੀਰਜ ਰੱਖੋ, ਧੀਰਜ ਦਾ ਫਲ ਮਿੱਠਾ। 19. ਮੂੰਹੋਂ "
"ਨਿਕਲੀ ਗੱਲ ਤੀਰ ਵਾਂਗ (munhon nikli gall teer vaang) - literal: 'a word from the "
"mouth is like an arrow'; meaning: spoken words cannot be taken back. Example: "
"ਸੋਚ ਕੇ ਬੋਲੋ, ਮੂੰਹੋਂ ਨਿਕਲੀ ਗੱਲ ਤੀਰ ਵਾਂਗ ਹੁੰਦੀ ਹੈ। 20. ਇਕਤਾ ਵਿੱਚ ਬਲ ਹੈ (ektaa "
"vich bal hai) - literal: 'in unity there "
"is strength'; meaning: united we stand. Example: ਇਕਤਾ ਵਿੱਚ ਬਲ ਹੈ, ਮਿਲ ਕੇ ਕੰਮ "
"ਕਰੋ।"
),
"how_it_works": (
"Proverbs are complete sentences you quote whole - never translate them word "
"by word into English and expect them to land. Deploy them as closers: make "
"your point in plain speech, then seal it with the proverb - 'ਮਿਹਨਤ ਕਰੋ, "
"ਮਿਹਨਤ ਦਾ ਫਲ ਮਿੱਠਾ ਹੁੰਦਾ ਹੈ।' Many come in rhyming pairs (ਜਿਹਾ ਦੇਸ ਤਿਹਾ ਭੇਸ, "
"ਕਰ ਭਲਾ ਹੋ ਭਲਾ) - the rhyme is the memory hook. Some carry gentle mockery "
"(ਨੱਚ ਨਾ ਜਾਣੇ ਵਿਹੜਾ ਟੇਢਾ, ਖੁਦਾ ਮਿਹਰਬਾਨ ਤੇ ਗਧਾ ਪਹਿਲਵਾਨ) - use them on "
"situations, never to wound a person. One proverb per conversation is plenty; "
"two is a speech."
),
"key_points": [
"20 idioms/proverbs: literal translation + real meaning + example sentence.",
"Use proverbs as closers: plain point first, proverb as the seal.",
"Rhyming pairs (ਜਿਹਾ ਦੇਸ ਤਿਹਾ ਭੇਸ) are memory hooks.",
"Mocking proverbs target situations, never people.",
"One proverb per conversation; two is a speech.",
],
"requirements": [
"Use five proverbs in real conversation this week.",
"Explain three proverbs to someone in English without translating word by word.",
],
"standards": [
"Proverb collection: standard Punjabi sayings, public tradition",
],
"citations": [
"Standard Punjabi proverb tradition (public oral literature).",
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: proverbs are the sealed verdicts of generations - "
"each a case closed, each rhyme a wax stamp. The Signature Language Method "
"treats them as precedent law: quote the precedent, win the point, and let "
"the ancestors argue for you."),
},
# ------------------------------------------------------- 29 formal registers
{
"key": "registers",
"name": "Punjabi Formal and Polite Registers",
"group": "sayings",
"ladder_rank": 9,
"ladder_tier": "advanced",
"description": (
"Fifteen formal-versus-informal pairs for letters, business, and elders, with "
"translations. 1. Informal: ਤੂੰ ਕਿੱਥੇ ਹੈਂ? (tun kitthe hain?) Where are you? / "
"Formal: ਤੁਸੀਂ ਕਿੱਥੇ ਹੋ? (tusin kitthe ho?) Where are you? 2. Informal: ਮੈਨੂੰ ਦੇ। "
"(mainun de.) Give me. / Formal: ਮੈਨੂੰ ਦੇ ਦਿਓ। (mainun de dio.) Please give me. "
"3. Informal: ਚੁੱਪ ਕਰ। (chupp kar.) Be quiet. / Formal: ਕਿਰਪਾ ਕਰਕੇ ਸ਼ਾਂਤ ਰਹੋ। "
"(kirpaa karke shaant raho.) Please stay quiet. 4. Informal: ਤੇਰਾ ਨਾਂ ਕੀ ਹੈ? "
"(tera naan ki hai?) What is your name? / Formal: ਤੁਹਾਡਾ ਨਾਂ ਕੀ ਹੈ? (tuhada naan "
"ki hai?) What is your name? 5. Informal: ਤੂੰ ਆਵੇਂਗਾ? (tun aavengaa?) Will you "
"come? / Formal: ਕੀ ਤੁਸੀਂ ਆਓਗੇ? (ki tusin aaoge?) Will you come? 6. Informal "
"letter opening: ਪਿਆਰੇ ਮੋਹਨ, (pyaare Mohan,) Dear Mohan, / Formal letter "
"opening: ਸਤਿਕਾਰਯੋਗ ਮਹੋਦਯ, (satikaaryog mahoday,) Respected Sir, 7. Informal "
"closing: ਤੇਰਾ ਦੋਸਤ, (tera dost,) Your friend, / Formal closing: ਆਪ ਦਾ "
"ਵਿਸ਼ਵਾਸਪਾਤਰ, (aap da vishvaaspaatar,) Yours faithfully, 8. Informal request: "
"ਪੈਸੇ ਦੇ। (paise de.) Give the money. / Formal request: ਪੈਸੇ ਦੇਣ ਦੀ ਕਿਰਪਾ ਕਰੋ। "
"(paise den di kirpaa karo.) Kindly give the money. 9. Informal thanks: "
"ਸ਼ੁਕਰੀਆ। (shukriyaa.) Thanks. / Formal thanks: ਬਹੁਤ ਬਹੁਤ ਧੰਨਵਾਦ। (bahut bahut "
"dhannvaad.) Thank you very much. 10. Informal refusal: ਨਹੀਂ ਚਾਹੀਦਾ। (nahin "
"chaheeda.) Do not want it. / Formal refusal: ਮਾਫ਼ ਕਰਨਾ, ਇਸ ਵੇਲੇ ਸੰਭਵ ਨਹੀਂ ਹੈ। "
"(maaf karnaa, is vele sambhav nahin hai.) Excuse me, it is not possible at "
"this time. 11. Informal to elder (WRONG): ਤੂੰ ਬੈਠ। / Correct formal: ਤੁਸੀਂ "
"ਬੈਠੋ ਜੀ। (tusin baitho ji.) Please sit. 12. Business: ਮਾਲ ਭੇਜ ਦਿਓ। (maal bhej "
"dio.) Send the goods. (polite) / Softer business: ਮਾਲ ਭੇਜਣ ਦੀ ਕਿਰਪਾਲਤਾ ਕਰਨੀ। "
"(maal bhejan di kirpaaltaa karni.) Kindly arrange to send the goods. 13. "
"Informal apology: ਗ਼ਲਤੀ ਹੋ ਗਈ। (ghalti ho gayi.) My mistake. / Formal apology: "
"ਮੈਨੂੰ ਮਾਫ਼ ਕਰ ਦਿਓ, ਗ਼ਲਤੀ ਹੋ ਗਈ। (mainun maaf kar dio, ghalti ho gayi.) Please "
"forgive me, a mistake happened. 14. Informal phone: ਹੈਲੋ, ਕੌਣ? (hello, kaun?) "
"Hello, who is it? / Formal phone: ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਜੀ, ਮੈਂ ਸਿਮਰਨ ਬੋਲ ਰਹੀ ਹਾਂ। "
"(sat sri akaal ji, main Simran bol rahi haan.) Greetings, this is Simran "
"speaking. 15. Informal blessing: ਖੁਸ਼ ਰਹਿ। (khush reh.) Stay happy. / Formal "
"elder's blessing: ਖੁਸ਼ ਰਹੋ, ਜੁਗ ਜੁਗ ਜੀਓ। (khush raho, jug jug jeeo.) Stay "
"happy, live long."
),
"how_it_works": (
"The register ladder has three rungs: ਤੂੰ (intimate - family, close friends, "
"children, God), ਤੁਸੀਂ (formal - everyone else), and the written formal of "
"letters (ਸਤਿਕਾਰਯੋਗ, ਵਿਸ਼ਵਾਸਪਾਤਰ). Climb with age, rank, and strangers; the "
"only safe error is too formal, never too casual. Letters open with "
"ਸਤਿਕਾਰਯੋਗ (respected) and close with ਆਪ ਦਾ ਵਿਸ਼ਵਾਸਪਾਤਰ (yours faithfully). "
"Business softens commands into requests: ਭੇਜ ਦਿਓ (send please) or the "
"noun-form ਕਿਰਪਾਲਤਾ ਕਰਨੀ (kindly arrange). Refusals never say a flat ਨਹੀਂ to "
"superiors - wrap them: ਮਾਫ਼ ਕਰਨਾ, ... ਸੰਭਵ ਨਹੀਂ ਹੈ. On the phone, name "
"yourself with ਬੋਲ ਰਿਹਾ/ਰਹੀ ਹਾਂ ('I am speaking')."
),
"key_points": [
"15 formal/informal pairs: speech, letters, business, elders.",
"Three rungs: ਤੂੰ (intimate), ਤੁਸੀਂ (formal), written formal.",
"Safe error is too formal - never too casual with elders.",
"Letter frame: ਸਤਿਕਾਰਯੋਗ opening, ਆਪ ਦਾ ਵਿਸ਼ਵਾਸਪਾਤਰ closing.",
"Business softener: ਕਿਰਪਾਲਤਾ ਕਰਨੀ; refusals wrapped in ਮਾਫ਼ ਕਰਨਾ.",
"Phone self-naming: ਮੈਂ X ਬੋਲ ਰਿਹਾ/ਰਹੀ ਹਾਂ।",
],
"requirements": [
"Write a formal letter and an informal note on the same topic.",
"Role-play a business call using only the formal rung.",
],
"standards": [
"Sociolinguistic register analysis per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: register is the seal-rank system - ਤੂੰ the family "
"seal, ਤੁਸੀਂ the public seal, ਸਤਿਕਾਰਯੋਗ the court seal. The Signature Language "
"Method teaches the ladder as protocol: stamp every person with the seal "
"their rank deserves and no door stays closed."),
},
# ------------------------------------------------------- 30 complex sentences
{
"key": "complex",
"name": "Punjabi Compound and Complex Sentences",
"group": "grammar",
"ladder_rank": 10,
"ladder_tier": "advanced",
"description": (
"Fifteen long sentences with clauses, connectors, and relative clauses - each "
"parsed and translated. 1. ਮੈਂ ਸਕੂਲ ਗਿਆ ਕਿਉਂਕਿ ਮੈਨੂੰ ਪੜ੍ਹਨਾ ਸੀ। (main school "
"gayaa kionki mainun parhnaa see.) I went to school because I had to study. "
"[main clause + ਕਿਉਂਕਿ reason clause] 2. ਜਦੋਂ ਮੀਂਹ ਪਿਆ ਤਾਂ ਅਸੀਂ ਅੰਦਰ ਆ ਗਏ। "
"(jadon meenh piyaa taan asin andar aa gaye.) When it rained, we came inside. "
"[ਜਦੋਂ...ਤਾਂ when-clause] 3. ਉਹ ਮੁੰਡਾ ਜੋ ਬਾਹਰ ਖੜ੍ਹਾ ਹੈ ਮੇਰਾ ਦੋਸਤ ਹੈ। (oh munda "
"jo baahar kharhaa hai mera dost hai.) The boy who is standing outside is my "
"friend. [ਜੋ relative clause] 4. ਜਿਹੜੀ ਕਿਤਾਬ ਤੁਸੀਂ ਦਿੱਤੀ ਸੀ ਉਹ ਬਹੁਤ ਚੰਗੀ ਹੈ। "
"(jihri kitaab tusin ditti see oh bahut changi hai.) The book which you gave is "
"very good. [ਜਿਹੜੀ relative clause] 5. ਮੈਂ ਚਾਹੁੰਦਾ ਹਾਂ ਕਿ ਤੁਸੀਂ ਆਓ। (main "
"chaahundaa haan ki tusin aao.) I want you to come. [ਕਿ that-clause] 6. ਉਸਨੇ "
"ਕਿਹਾ ਕਿ ਉਹ ਕੱਲ੍ਹ ਆਵੇਗਾ। (usne kihaa ki oh kallh aavegaa.) He said that he will "
"come tomorrow. [reported speech with ਕਿ] 7. ਜੇ ਤੁਸੀਂ ਮਿਹਨਤ ਕਰੋਗੇ ਤਾਂ ਸਫ਼ਲ "
"ਹੋਵੋਗੇ। (je tusin mehnat karoge taan safal hovoge.) If you work hard, you will "
"succeed. [ਜੇ...ਤਾਂ condition] 8. ਭਾਵੇਂ ਮੀਂਹ ਪੈ ਰਿਹਾ ਸੀ, ਅਸੀਂ ਖੇਡਦੇ ਰਹੇ। "
"(bhaaven meenh pai rihaa see, asin khedde rahe.) Although it was raining, we "
"kept playing. [ਭਾਵੇਂ concession] 9. ਉਹ ਇੰਨਾ ਥੱਕਿਆ ਹੋਇਆ ਸੀ ਕਿ ਸੌਂ ਗਿਆ। (oh "
"innaa thakkiyaa hoyaa see ki saun gayaa.) He was so tired that he fell asleep. "
"[ਇੰਨਾ...ਕਿ result] 10. ਪਹਿਲਾਂ ਖਾਣਾ ਖਾਓ, ਫਿਰ ਬਾਹਰ ਜਾਓ। (pahilaan khaana khaao, "
"phir baahar jaao.) First eat food, then go outside. [ਪਹਿਲਾਂ...ਫਿਰ sequence] "
"11. ਨਾ ਉਹ ਆਇਆ, ਨਾ ਉਸਨੇ ਫ਼ੋਨ ਕੀਤਾ। (na oh aayaa, na usne phone keetaa.) Neither "
"did he come, nor did he call. [ਨਾ...ਨਾ neither/nor] 12. ਜਾਂ ਤੁਸੀਂ ਆਓ, ਜਾਂ ਮੈਂ "
"ਆਵਾਂ। (jaan tusin aao, jaan main aavaan.) Either you come, or I will come. "
"[ਜਾਂ...ਜਾਂ either/or] 13. ਉਹ ਜਿੱਥੇ ਵੀ ਜਾਂਦਾ ਹੈ, ਲੋਕ ਉਸਨੂੰ ਪਿਆਰ ਕਰਦੇ ਹਨ। (oh "
"jitthe vi jaanda hai, lok usnun pyaar karde han.) Wherever he goes, people "
"love him. [ਜਿੱਥੇ ਵੀ wherever] 14. ਜਿਸ ਦਿਨ ਤੁਸੀਂ ਆਓਗੇ, ਪਾਰਟੀ ਹੋਵੇਗੀ। (jis din "
"tusin aaoge, party hovegi.) The day you come, there will be a party. [ਜਿਸ "
"relative time] 15. ਮੈਂ ਨੇ ਉਹ ਕਿਤਾਬ ਪੜ੍ਹੀ ਜਿਸ ਬਾਰੇ ਤੁਸੀਂ ਦੱਸਿਆ ਸੀ। (main ne oh "
"kitaab parhi jis baare tusin dassiyaa see.) I read the book about which you "
"told me. [ਜਿਸ oblique relative + ergative main clause]"
),
"how_it_works": (
"Complex sentences are two simple sentences joined by a connector, and the "
"connector tells you the relationship: ਕਿਉਂਕਿ (because) for reason, ਜਦੋਂ...ਤਾਂ "
"(when...then) for time, ਜੋ/ਜਿਹੜਾ/ਜਿਹੜੀ (who/which) for relatives - ਜੋ for "
"people, ਜਿਹੜਾ/ਜਿਹੜੀ agreeing with the noun's gender - ਕਿ (that) for reported "
"thoughts, ਜੇ...ਤਾਂ (if...then) for conditions, ਭਾਵੇਂ (although) for "
"concession, ਇੰਨਾ...ਕਿ (so...that) for result. Correlatives come in pairs: "
"ਜਦੋਂ with ਤਾਂ, ਜੇ with ਤਾਂ, ਨਾ with ਨਾ, ਜਾਂ with ਜਾਂ - learn them as pairs, "
"never alone. The relative clause sits right after its noun: ਉਹ ਮੁੰਡਾ ਜੋ ਬਾਹਰ "
"ਖੜ੍ਹਾ ਹੈ. Reported speech keeps the original tense logic: ਉਸਨੇ ਕਿਹਾ ਕਿ ਉਹ "
"ਆਵੇਗਾ (he said that he will come)."
),
"key_points": [
"15 parsed complex sentences with connectors labeled.",
"Connectors: ਕਿਉਂਕਿ, ਜਦੋਂ...ਤਾਂ, ਜੋ/ਜਿਹੜਾ/ਜਿਹੜੀ, ਕਿ, ਜੇ...ਤਾਂ, ਭਾਵੇਂ, ਇੰਨਾ...ਕਿ.",
"Correlatives come in pairs - learn both halves together.",
"Relative clause sits directly after its noun; ਜਿਹੜਾ/ਜਿਹੜੀ agrees in gender.",
"Reported speech with ਕਿ keeps future-in-the-past logic.",
],
"requirements": [
"Join ten simple-sentence pairs with a different connector each.",
"Write five relative clauses with ਜਿਹੜਾ/ਜਿਹੜੀ matched to noun gender.",
],
"standards": [
"Complex syntax per Bhatia 1993",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
"Gill, Harjit Singh and Gleason, Henry A. A Reference Grammar of Punjabi, 1969.",
],
"sig_lens": (
"His Signature reading: connectors are the binding clauses of the covenant - "
"ਕਿਉਂਕਿ the cause clause, ਜੇ...ਤਾਂ the condition clause, ਜੋ the witness "
"clause. The Signature Language Method builds sentences the way contracts are "
"built: main clause as the parties, connectors as the terms, and every "
"correlative pair signed in duplicate."),
},
# ------------------------------------------------------- 31 market dialogue
{
"key": "dialogue_market",
"name": "Punjabi Conversation at the Market",
"group": "dialogues",
"ladder_rank": 10,
"ladder_tier": "advanced",
"description": (
"A twenty-line bilingual dialogue at the vegetable market - customer (ਗਾਹਕ) "
"and shopkeeper (ਦੁਕਾਨਦਾਰ) - annotated with the skill each line teaches. "
"1. ਗਾਹਕ: ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਜੀ! (sat sri akaal ji!) Hello! [greeting + ਜੀ respect] "
"2. ਦੁਕਾਨਦਾਰ: ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ! ਦੱਸੋ, ਕੀ ਚਾਹੀਦਾ ਹੈ? (sat sri akaal! dasso, ki "
"chaheeda hai?) Hello! Tell me, what do you need? [return greeting, need-frame] "
"3. ਗਾਹਕ: ਟਮਾਟਰ ਕਿਸ ਭਾਅ ਹਨ? (tamaatar kis bhaa han?) What is the price of "
"tomatoes? [price question] 4. ਦੁਕਾਨਦਾਰ: ਅੱਸੀ ਰੁਪਏ ਕਿਲੋ, ਬਿਲਕੁਲ ਤਾਜ਼ੇ ਹਨ। (assi "
"rupaye kilo, bilkul taaze han.) Eighty rupees a kilo, absolutely fresh. "
"[price + quality claim] 5. ਗਾਹਕ: ਬਹੁਤ ਮਹਿੰਗੇ ਹਨ, ਸੱਠ ਲਗਾਓ। (bahut mahinge han, "
"satth lagaao.) Too expensive, make it sixty. [bargaining counter] 6. "
"ਦੁਕਾਨਦਾਰ: ਸੱਠ ਵਿੱਚ ਨਹੀਂ ਹੋਣਗੇ, ਸੱਤਰ ਆਖ਼ਰੀ ਭਾਅ ਹੈ। (satth vich nahin honge, "
"sattar aakhri bhaa hai.) Not possible at sixty, seventy is the final price. "
"[final price] 7. ਗਾਹਕ: ਚਲੋ, ਇੱਕ ਕਿਲੋ ਦੇ ਦਿਓ। (chalo, ikk kilo de dio.) OK, "
"give one kilo. [deal + order] 8. ਦੁਕਾਨਦਾਰ: ਹੋਰ ਕੁਝ? ਆਲੂ, ਪਿਆਜ਼? (hor kujh? "
"aaloo, piyaaz?) Anything else? Potatoes, onions? [upsell] 9. ਗਾਹਕ: ਅੱਧਾ ਕਿਲੋ "
"ਆਲੂ ਵੀ ਦੇ ਦਿਓ। (addhaa kilo aaloo vi de dio.) Give half a kilo of potatoes "
"too. [quantity order] 10. ਦੁਕਾਨਦਾਰ: ਇਹ ਲਓ, ਤੋਲ ਕੇ ਦਿੱਤੇ ਹਨ। (eh lao, tol ke "
"ditte han.) Here, weighed and given. [delivery] 11. ਗਾਹਕ: ਧਨੀਆ ਮੁਫ਼ਤ ਪਾ ਦਿਓ। "
"(dhaniyaa muft paa dio.) Add coriander free. [freebie ask] 12. ਦੁਕਾਨਦਾਰ: ਲਓ "
"ਜੀ, ਧਨੀਆ ਵੀ ਪਾ ਦਿੱਤਾ। (lao ji, dhaniyaa vi paa dittaa.) Here, added coriander "
"too. [goodwill] 13. ਗਾਹਕ: ਕੁੱਲ ਕਿੰਨਾ ਹੋਇਆ? (kull kinna hoyaa?) What is the "
"total? [total] 14. ਦੁਕਾਨਦਾਰ: ਇੱਕ ਸੌ ਦਸ ਰੁਪਏ। (ikk sau das rupaye.) One hundred "
"ten rupees. [total stated] 15. ਗਾਹਕ: ਇਹ ਲਓ ਦੋ ਸੌ, ਖੁੱਲ੍ਹੇ ਦੇ ਦਿਓ। (eh lao do "
"sau, khullhe de dio.) Here is two hundred, give change. [payment] 16. "
"ਦੁਕਾਨਦਾਰ: ਨੱਬੇ ਵਾਪਸ, ਗਿਣ ਲਓ। (nabbe vaapas, gin lao.) Ninety back, count it. "
"[change] 17. ਗਾਹਕ: ਸੌਦਾ ਪੱਕਾ, ਮਾਲ ਚੰਗਾ ਹੈ। (saudaa pakkaa, maal changa hai.) "
"Deal done, the goods are good. [seal + praise] 18. ਦੁਕਾਨਦਾਰ: ਅਗਲੀ ਵਾਰ ਫਿਰ "
"ਆਉਣਾ ਜੀ। (agli vaar phir aaunaa ji.) Do come again next time. [return "
"invitation] 19. ਗਾਹਕ: ਜ਼ਰੂਰ ਆਵਾਂਗਾ, ਰੱਬ ਰਾਖਾ! (zaroor aavaangaa, rabb raakha!) "
"I will surely come, goodbye! [promise + farewell] 20. ਦੁਕਾਨਦਾਰ: ਰੱਬ ਰਾਖਾ! "
"(rabb raakha!) Goodbye! [farewell]"
),
"how_it_works": (
"The market dialogue is a five-act play: greeting (lines 1-2), price discovery "
"(3-4), bargaining (5-6), the order and extras (7-12), payment and farewell "
"(13-20). Notice the ritual moves: ਆਖ਼ਰੀ ਭਾਅ (final price) ends bargaining, "
"ਮੁਫ਼ਤ ਧਨੀਆ (free coriander) is the traditional goodwill herb, ਖੁੱਲ੍ਹੇ ਪੈਸੇ "
"(change) is requested before paying, and ਸੌਦਾ ਪੱਕਾ seals it. Act it with a "
"partner, then swap roles - the shopkeeper's lines teach upselling (ਹੋਰ ਕੁਝ?) "
"and the customer's lines teach the full bargaining script from record 18."
),
"key_points": [
"20-line bilingual dialogue, annotated per line.",
"Five acts: greeting, price, bargaining, order, payment/farewell.",
"Ritual moves: ਆਖ਼ਰੀ ਭਾਅ, ਮੁਫ਼ਤ ਧਨੀਆ, ਖੁੱਲ੍ਹੇ ਪੈਸੇ, ਸੌਦਾ ਪੱਕਾ.",
"Total math in the dialogue: 70 + 40 = 110; 200 - 110 = 90 change.",
"Swap roles to learn both sides.",
],
"requirements": [
"Perform the dialogue aloud with a partner, twice, roles swapped.",
"Improvise a new market dialogue for fruit instead of vegetables.",
],
"standards": [
"Dialogue transcription: constructed teaching dialogue, public-harvest",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: the market dialogue is the exchange ritual performed "
"whole - twenty seals in order, none skipped. The Signature Language Method "
"stages it as theater because the bazaar is theater: learn your lines and "
"the crowd believes you belong."),
},
# ------------------------------------------------------- 32 friend dialogue
{
"key": "dialogue_friend",
"name": "Punjabi Conversation Meeting a Friend",
"group": "dialogues",
"ladder_rank": 10,
"ladder_tier": "advanced",
"description": (
"A twenty-line bilingual dialogue between two old friends, Simran and "
"Gurpreet, meeting after years - annotated. 1. ਸਿਮਰਨ: ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ! ਗੁਰਪ੍ਰੀਤ, "
"ਤੂੰ?! (sat sri akaal! Gurpreet, tun?!) Hello! Gurpreet, is that you?! "
"[surprised greeting, ਤੂੰ = intimacy] 2. ਗੁਰਪ੍ਰੀਤ: ਸਿਮਰਨ! ਕਿੰਨੇ ਸਾਲਾਂ ਬਾਅਦ! "
"(Simran! kinne saalaan baad!) Simran! After so many years! [joy] 3. ਸਿਮਰਨ: "
"ਤੂੰ ਕਿੱਥੇ ਸੀ ਇੰਨੇ ਸਾਲ? (tun kitthe see inne saal?) Where were you all these "
"years? [catch-up question] 4. ਗੁਰਪ੍ਰੀਤ: ਮੈਂ ਕੈਨੇਡਾ ਵਿੱਚ ਸੀ, ਹੁਣ ਵਾਪਸ ਆਇਆ ਹਾਂ। "
"(main Canada vich see, hun vaapas aayaa haan.) I was in Canada, now I have "
"returned. [life update] 5. ਸਿਮਰਨ: ਵਾਹ! ਕੈਨੇਡਾ ਕਿਵੇਂ ਲੱਗਾ? (vaah! Canada kiven "
"laggaa?) Wow! How did you like Canada? [reaction + question] 6. ਗੁਰਪ੍ਰੀਤ: "
"ਬਹੁਤ ਵਧੀਆ, ਪਰ ਪੰਜਾਬ ਦੀ ਯਾਦ ਆਉਂਦੀ ਸੀ। (bahut vadheeyaa, par Panjaab di yaad "
"aaundi see.) Very good, but I missed Punjab. [balanced answer] 7. ਸਿਮਰਨ: ਚਲ, "
"ਚਾਹ ਪੀਂਦੇ ਹਾਂ, ਬਹੁਤ ਗੱਲਾਂ ਕਰਨੀਆਂ ਹਨ। (chal, chaa peende haan, bahut gallaan "
"karniaan han.) Come, let us have tea, we have much to talk about. "
"[hospitality] 8. ਗੁਰਪ੍ਰੀਤ: ਹਾਂ, ਚਲ। ਤੇਰਾ ਪਰਿਵਾਰ ਕਿਵੇਂ ਹੈ? (haan, chal. tera "
"parivaar kiven hai?) Yes, let us go. How is your family? [family inquiry] 9. "
"ਸਿਮਰਨ: ਸਭ ਠੀਕ ਹਨ, ਮਾਂ ਤੈਨੂੰ ਯਾਦ ਕਰਦੀ ਹੈ। (sabh theek han, maan tainun yaad "
"kardi hai.) All fine, mother remembers you. [warmth] 10. ਗੁਰਪ੍ਰੀਤ: ਅਗਲੇ "
"ਹਫ਼ਤੇ ਮਿਲਣ ਆਵਾਂਗਾ। (agle hafte milan aavaangaa.) I will come to meet next "
"week. [promise] 11. ਸਿਮਰਨ: ਤੂੰ ਵਿਆਹ ਕਰਵਾ ਲਿਆ? (tun viaah karvaa liyaa?) Did "
"you get married? [personal question - intimates only] 12. ਗੁਰਪ੍ਰੀਤ: ਹਾਂ, ਦੋ "
"ਸਾਲ ਹੋ ਗਏ। (haan, do saal ho gaye.) Yes, two years now. [answer] 13. ਸਿਮਰਨ: "
"ਵਧਾਈ ਹੋਵੇ! ਭਾਬੀ ਨੂੰ ਮਿਲਣਾ ਪਵੇਗਾ। (vadhaai hove! bhaabi nun milnaa pavegaa.) "
"Congratulations! I must meet your wife. [congratulations] 14. ਗੁਰਪ੍ਰੀਤ: "
"ਜ਼ਰੂਰ, ਉਹ ਵੀ ਪੰਜਾਬਣ ਹੈ। (zaroor, oh vi Panjaaban hai.) Of course, she is "
"Punjabi too. [pride] 15. ਸਿਮਰਨ: ਤੂੰ ਪੰਜਾਬੀ ਨਹੀਂ ਭੁੱਲਿਆ! (tun Panjaabi nahin "
"bhulliyaa!) You have not forgotten Punjabi! [language praise] 16. ਗੁਰਪ੍ਰੀਤ: "
"ਮਾਂ ਬੋਲੀ ਕਦੇ ਨਹੀਂ ਭੁੱਲਦੀ। (maan boli kade nahin bhulldi.) One never forgets "
"the mother tongue. [proverb-like truth] 17. ਸਿਮਰਨ: ਸੱਚ ਕਿਹਾ! ਚਲ, ਫੋਟੋ ਖਿੱਚਦੇ "
"ਹਾਂ। (sachch kihaa! chal, photo khichde haan.) Truly said! Come, let us take "
"a photo. [agreement + fun] 18. ਗੁਰਪ੍ਰੀਤ: ਹਾਂ, ਯਾਦਗਾਰ ਬਣੇਗੀ। (haan, yaadgaar "
"banegi.) Yes, it will be a keepsake. [future] 19. ਸਿਮਰਨ: ਫਿਰ ਮਿਲਦੇ ਹਾਂ, "
"ਰੱਬ ਰਾਖਾ! (phir milde haan, rabb raakha!) See you again, goodbye! [farewell] "
"20. ਗੁਰਪ੍ਰੀਤ: ਰੱਬ ਰਾਖਾ, ਸਿਮਰਨ! (rabb raakha, Simran!) Goodbye, Simran! "
"[farewell]"
),
"how_it_works": (
"Friend dialogue runs on ਤੂੰ - the intimate pronoun is the whole point: "
"strangers meeting would use ਤੁਸੀਂ for all twenty lines. Watch the catch-up "
"arc: surprise (1-2), where-have-you-been (3-4), reaction (5-6), hospitality "
"(7), family news (8-10), personal news (11-14), shared value (15-16), fun "
"(17-18), farewell (19-20). ਮਾਂ ਬੋਲੀ (maan boli, 'mother tongue') is the "
"cultural key line - Punjabis call the language the mother's speech. Note "
"ਕਦੇ ਨਹੀਂ ਭੁੱਲਦੀ with feminine agreement to ਬੋਲੀ. Perform it with the ਤੂੰ "
"warmth - then redo it as strangers with ਤੁਸੀਂ to feel the register shift."
),
"key_points": [
"20-line bilingual dialogue, annotated per line.",
"ਤੂੰ throughout = intimacy; redo with ਤੁਸੀਂ to feel the register shift.",
"Catch-up arc: surprise, update, hospitality, news, values, farewell.",
"ਮਾਂ ਬੋਲੀ (mother tongue): the cultural key line.",
"Personal questions (ਵਿਆਹ) are intimates-only.",
],
"requirements": [
"Perform the dialogue with ਤੂੰ, then again as strangers with ਤੁਸੀਂ.",
"Improvise a reunion with your own life updates.",
],
"standards": [
"Dialogue transcription: constructed teaching dialogue, public-harvest",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: the reunion dialogue is the witness ceremony - two "
"old seals recognizing each other across years. The Signature Language "
"Method performs it as proof: ਤੂੰ is the password of the old friendship, "
"and ਮਾਂ ਬੋਲੀ the oath neither time nor distance can break."),
},
# ------------------------------------------------------- 33 problem dialogue
{
"key": "dialogue_problem",
"name": "Punjabi Conversation Solving a Problem",
"group": "dialogues",
"ladder_rank": 10,
"ladder_tier": "advanced",
"description": (
"A twenty-line bilingual dialogue: a traveler's phone is lost, and a "
"station officer helps - annotated. 1. ਯਾਤਰੀ: ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਜੀ, ਮੈਨੂੰ ਮਦਦ "
"ਚਾਹੀਦੀ ਹੈ। (sat sri akaal ji, mainun madad chaheedi hai.) Hello, I need help. "
"[formal help request] 2. ਅਧਿਕਾਰੀ: ਹਾਂ ਜੀ, ਦੱਸੋ ਕੀ ਹੋਇਆ? (haan ji, dasso ki "
"hoyaa?) Yes, tell me what happened? [official response] 3. ਯਾਤਰੀ: ਮੇਰਾ ਫ਼ੋਨ "
"ਗੁੰਮ ਹੋ ਗਿਆ ਹੈ। (mera phone gumm ho gayaa hai.) My phone is lost. [problem "
"stated] 4. ਅਧਿਕਾਰੀ: ਕਿੱਥੇ ਗੁੰਮ ਹੋਇਆ? (kitthe gumm hoyaa?) Where was it lost? "
"[location] 5. ਯਾਤਰੀ: ਸ਼ਾਇਦ ਬੱਸ ਵਿੱਚ ਰਹਿ ਗਿਆ। (shaayad bass vich reh gayaa.) "
"Probably left in the bus. [hypothesis] 6. ਅਧਿਕਾਰੀ: ਬੱਸ ਨੰਬਰ ਯਾਦ ਹੈ? (bass "
"number yaad hai?) Do you remember the bus number? [key detail] 7. ਯਾਤਰੀ: "
"ਨਹੀਂ ਜੀ, ਪਰ ਉਹ ਅੰਮ੍ਰਿਤਸਰ ਵਾਲੀ ਬੱਸ ਸੀ। (nahin ji, par oh Amritsar vaali bass "
"see.) No, but it was the Amritsar bus. [partial info] 8. ਅਧਿਕਾਰੀ: ਕੋਈ ਗੱਲ "
"ਨਹੀਂ, ਅਸੀਂ ਪਤਾ ਕਰਦੇ ਹਾਂ। (koi gall nahin, asin pataa karde haan.) No problem, "
"we will find out. [reassurance] 9. ਯਾਤਰੀ: ਫ਼ੋਨ ਵਿੱਚ ਮੇਰੀਆਂ ਫੋਟੋਆਂ ਅਤੇ ਨੰਬਰ "
"ਹਨ। (phone vich meriyaan photovaan ate number han.) My photos and numbers are "
"in the phone. [stakes] 10. ਅਧਿਕਾਰੀ: ਚਿੰਤਾ ਨਾ ਕਰੋ, ਰਿਪੋਰਟ ਲਿਖਦੇ ਹਾਂ। (chintaa "
"na karo, riport likhde haan.) Do not worry, we will file a report. [action] "
"11. ਯਾਤਰੀ: ਰਿਪੋਰਟ ਲਈ ਕੀ ਕੀ ਚਾਹੀਦਾ ਹੈ? (riport lai ki ki chaheeda hai?) What is "
"needed for the report? [procedure] 12. ਅਧਿਕਾਰੀ: ਨਾਂ, ਪਤਾ, ਅਤੇ ਫ਼ੋਨ ਦਾ ਮਾਡਲ। "
"(naan, pataa, ate phone da model.) Name, address, and the phone's model. "
"[requirements] 13. ਯਾਤਰੀ: ਮੇਰਾ ਨਾਂ ਰਵੀ ਹੈ, ਮਾਡਲ ਪਤਾ ਨਹੀਂ। (mera naan Ravi "
"hai, model pataa nahin.) My name is Ravi, I do not know the model. [honest "
"gap] 14. ਅਧਿਕਾਰੀ: ਕੋਈ ਗੱਲ ਨਹੀਂ, ਬਿੱਲ ਦੀ ਕਾਪੀ ਹੈ? (koi gall nahin, bill di "
"copy hai?) No problem, do you have a copy of the bill? [alternative] 15. "
"ਯਾਤਰੀ: ਹਾਂ, ਈਮੇਲ ਵਿੱਚ ਬਿੱਲ ਹੈ। (haan, email vich bill hai.) Yes, the bill is "
"in my email. [solution path] 16. ਅਧਿਕਾਰੀ: ਸ਼ਾਬਾਸ਼! ਫਿਰ ਤਾਂ ਮਿਲ ਜਾਵੇਗਾ। "
"(shaabaash! phir taan mil jaavegaa.) Excellent! Then it will be found. "
"[encouragement] 17. ਯਾਤਰੀ: ਕਿੰਨਾ ਸਮਾਂ ਲੱਗੇਗਾ? (kinna samaan laggegaa?) How "
"long will it take? [timeline] 18. ਅਧਿਕਾਰੀ: ਦੋ-ਤਿੰਨ ਦਿਨ, ਅਸੀਂ ਫ਼ੋਨ ਕਰਾਂਗੇ। "
"(do-tinn din, asin phone karaange.) Two-three days, we will call you. "
"[commitment] 19. ਯਾਤਰੀ: ਬਹੁਤ ਬਹੁਤ ਧੰਨਵਾਦ ਜੀ! (bahut bahut dhannvaad ji!) "
"Thank you very much! [gratitude] 20. ਅਧਿਕਾਰੀ: ਕੋਈ ਗੱਲ ਨਹੀਂ, ਖ਼ਿਆਲ ਰੱਖੋ। (koi "
"gall nahin, khiyaal rakkho.) No problem, take care. [close]"
),
"how_it_works": (
"Problem-solving dialogue is a six-step protocol: request help (ਮਦਦ ਚਾਹੀਦੀ "
"ਹੈ), state the problem (ਗੁੰਮ ਹੋ ਗਿਆ ਹੈ), give details (ਕਿੱਥੇ/ਕਦੋਂ), follow "
"the official's questions honestly (ਨਹੀਂ ਜੀ is fine - partial info beats "
"silence), accept the procedure (ਰਿਪੋਰਟ ਲਿਖਦੇ ਹਾਂ), and close with thanks. "
"Officials are addressed with ਜੀ throughout; reassurance comes as ਕੋਈ ਗੱਲ "
"ਨਹੀਂ and ਚਿੰਤਾ ਨਾ ਕਰੋ. The lost-thing verb is ਗੁੰਮ ਹੋਣਾ (gumm honaa, 'to "
"become lost'); the found-thing verb is ਮਿਲ ਜਾਣਾ (mil jaanaa, 'to get found'). "
"Timelines are ranges: ਦੋ-ਤਿੰਨ ਦਿਨ. Learn this dialogue cold - it is the one "
"you will actually need abroad."
),
"key_points": [
"20-line bilingual dialogue, annotated per line.",
"Six-step protocol: request, state, detail, answer, accept, thank.",
"Lost = ਗੁੰਮ ਹੋਣਾ; found = ਮਿਲ ਜਾਣਾ.",
"Officials get ਜੀ; reassurance is ਕੋਈ ਗੱਲ ਨਹੀਂ / ਚਿੰਤਾ ਨਾ ਕਰੋ.",
"Partial info beats silence: ਨਹੀਂ ਜੀ, ਪਰ...",
"Timelines as ranges: ਦੋ-ਤਿੰਨ ਦਿਨ.",
],
"requirements": [
"Perform the dialogue, then improvise a lost-wallet variant.",
"Explain a different problem (missed train) using the six steps.",
],
"standards": [
"Dialogue transcription: constructed teaching dialogue, public-harvest",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
],
"sig_lens": (
"His Signature reading: the problem dialogue is the emergency protocol - "
"the seal you break only when something is lost. The Signature Language "
"Method drills it as a fire drill: request, state, detail, answer, accept, "
"thank - six moves, no panic, and the system works for you."),
},
# ------------------------------------------------------- 34 mastery review
{
"key": "mastery",
"name": "Punjabi Mastery Review and Full Reference",
"group": "mastery",
"ladder_rank": 10,
"ladder_tier": "advanced",
"description": (
"The whole database in one teaching summary - the consolidated quick "
"reference. THE ALPHABET: the painti akhar, 35 letters in order: ਉ ਅ ੳ ਸ ਹ, ਕ "
"ਖ ਗ ਘ ਙ, ਚ ਛ ਜ ਝ ਞ, ਟ ਠ ਡ ਢ ਣ, ਤ ਥ ਦ ਧ ਨ, ਪ ਫ ਬ ਭ ਮ, ਯ ਰ ਲ ਵ ੜ; ten vowels "
"ਅ ਆ ਇ ਈ ਉ ਊ ਏ ਐ ਓ ਔ; vowel signs ਾ ਿ ੀ ੁ ੂ ੇ ੈ ੋ ੌ; addak ੱ, bindi/tippi "
"ਂ/ੰ, halant ੍; dotted loans ਖ਼ ਗ਼ ਜ਼ ਫ਼ ਲ਼; danda ।; numerals ੦੧੨੩੪੫੬੭੮੯. "
"200 CORE WORDS (Punjabi - transliteration - English): ਪਾਣੀ paani water, ਕਿਤਾਬ "
"kitaab book, ਘਰ ghar house, ਸਕੂਲ school school, ਰੋਟੀ roti bread, ਚਾਹ chaa tea, "
"ਦੋਸਤ dost friend, ਮਾਂ maan mother, ਪਿਉ pio father, ਭਰਾ bharaa brother, ਭੈਣ "
"bhain sister, ਬੱਚਾ baccha child, ਗੱਡੀ gaddi car, ਰਸਤਾ rastaa road, ਦੁਕਾਨ dukaan "
"shop, ਬਾਜ਼ਾਰ bazaar market, ਕੰਮ kamm work, ਖਾਣਾ khaana food, ਦੁੱਧ duddh milk, "
"ਸਬਜ਼ੀ sabzi vegetable, ਫਲ phal fruit, ਦਿਨ din day, ਰਾਤ raat night, ਸੂਰਜ sooraj "
"sun, ਚੰਨ chann moon, ਪੰਛੀ panchhi bird, ਕੁੱਤਾ kutta dog, ਬਿੱਲੀ billi cat, ਕਰਨਾ "
"karna to do, ਜਾਣਾ jaana to go, ਆਉਣਾ aauna to come, ਖਾਣਾ khaana to eat, ਪੀਣਾ "
"peena to drink, ਪੜ੍ਹਨਾ parhna to read/study, ਲਿਖਣਾ likhna to write, ਬੋਲਣਾ bolna "
"to speak, ਸੁਣਨਾ sunna to listen, ਦੇਖਣਾ dekhna to see, ਲੈਣਾ laina to take, ਦੇਣਾ "
"dena to give, ਬਣਾਉਣਾ banauna to make, ਬੈਠਣਾ baithna to sit, ਉੱਠਣਾ utthna to get "
"up, ਸੌਣਾ sauna to sleep, ਚੱਲਣਾ challna to walk, ਦੌੜਨਾ daurna to run, ਖਰੀਦਣਾ "
"khareedna to buy, ਵੇਚਣਾ vechna to sell, ਖੇਡਣਾ khedna to play, ਸਿੱਖਣਾ sikhna to "
"learn, ਸਿਖਾਉਣਾ sikhauna to teach, ਵੱਡਾ vadda big, ਛੋਟਾ chhota small, ਨਵਾਂ "
"navaan new, ਪੁਰਾਣਾ puraana old, ਅੱਛਾ acchha good, ਬੁਰਾ bura bad, ਗਰਮ garam "
"hot, ਠੰਡਾ thanda cold, ਮਿੱਠਾ mittha sweet, ਸੁੰਦਰ sundar beautiful, ਲੰਬਾ lamba "
"tall, ਖੁਸ਼ khush happy, ਉਦਾਸ udaas sad, ਤੇਜ਼ tez fast, ਸਾਫ਼ saaf clean, ਮੈਂ "
"main I, ਤੂੰ tun you (informal), ਤੁਸੀਂ tusin you (formal), ਉਹ oh he/she/they, "
"ਅਸੀਂ asin we, ਇਹ eh this, ਮੇਰਾ mera my, ਤੁਹਾਡਾ tuhada your (formal), ਸਾਡਾ saada "
"our, ਕੌਣ kaun who, ਕੀ ki what, ਕਿੱਥੇ kitthe where, ਕਦੋਂ kadon when, ਕਿਉਂ kion "
"why, ਕਿਵੇਂ kiven how, ਇੱਕ ikk one, ਦੋ do two, ਤਿੰਨ tinn three, ਚਾਰ chaar four, "
"ਪੰਜ panj five, ਛੇ chhe six, ਸੱਤ satt seven, ਅੱਠ atth eight, ਨੌਂ naun nine, ਦਸ "
"das ten, ਵੀਹ veeh twenty, ਸੌ sau hundred, ਹਜ਼ਾਰ hazaar thousand, ਸੋਮਵਾਰ somvaar "
"Monday, ਐਤਵਾਰ aitvaar Sunday, ਜਨਵਰੀ januari January, ਦਸੰਬਰ dasambar December, "
"ਬਹੁਤ bahut very, ਜਲਦੀ jaldi quickly, ਅੱਜ ajj today, ਕੱਲ੍ਹ kallh tomorrow, ਹੁਣ "
"hun now, ਹਮੇਸ਼ਾ hamesha always, ਇੱਥੇ itthe here, ਉੱਥੇ utthe there, ਸਵੇਰ saver "
"morning, ਸ਼ਾਮ shaam evening, ਸਮਾਂ samaan time, ਘੰਟਾ ghanta hour, ਸਾਲ saal year, "
"ਮਹੀਨਾ maheena month, ਹਫ਼ਤਾ hafta week, ਪੈਸਾ paisa money, ਰੁਪਿਆ rupaya rupee, "
"ਦਵਾਈ davaai medicine, ਡਾਕਟਰ daaktar doctor, ਹਸਪਤਾਲ haspataal hospital, ਸਿਰ sir "
"head, ਅੱਖ akkh eye, ਹੱਥ hath hand, ਪੈਰ pair foot, ਦਿਲ dil heart, ਪਿਆਰ pyaar "
"love, ਖੁਸ਼ੀ khushi happiness, ਗੁੱਸਾ gussaa anger, ਡਰ dar fear, ਮੌਸਮ mausam "
"weather, ਮੀਂਹ meenh rain, ਹਵਾ havaa wind, ਬਰਫ਼ baraf snow, ਦਰੱਖਤ darakht tree, "
"ਫੁੱਲ phull flower, ਖੇਤ khet field, ਗਾਂ gaan cow, ਸ਼ੇਰ sher lion, ਸੱਪ sapp snake, "
"ਫ਼ੋਨ phone phone, ਨੈੱਟ net internet, ਕੰਪਿਊਟਰ computer computer, ਸੁਨੇਹਾ sunehaa "
"message, ਫੋਟੋ photo photo, ਕੱਪੜਾ kaprhaa cloth, ਜੁੱਤੀ jutti shoe, ਸੋਨਾ sona "
"gold, ਚਾਂਦੀ chaandi silver, ਲੋਹਾ lohaa iron, ਲੱਕੜ lakkar wood, ਪੱਥਰ patthar "
"stone, ਅੱਗ agg fire, ਧਰਤੀ dharti earth, ਅਸਮਾਨ asmaan sky, ਤਾਰਾ taaraa star, "
"ਬੱਦਲ baddal cloud, ਨਦੀ nadi river, ਸਮੁੰਦਰ samundar ocean, ਪਹਾੜ pahaarh "
"mountain, ਜੰਗਲ jangal forest, ਪਿੰਡ pind village, ਸ਼ਹਿਰ shehar city, ਦੇਸ਼ desh "
"country, ਦੁਨੀਆਂ duniyaan world, ਜ਼ਿੰਦਗੀ zindagi life, ਮੌਤ maut death, ਸੱਚ "
"sachch truth, ਝੂਠ jhooth lie, ਇਨਸਾਫ਼ insaaf justice, ਮਦਦ madad help, ਕੋਸ਼ਿਸ਼ "
"koshish effort, ਸਫ਼ਲਤਾ safaltaa success, ਮੁਸੀਬਤ museebat trouble, ਖ਼ਤਰਾ khatraa "
"danger, ਸ਼ਾਂਤੀ shaanti peace, ਜੰਗ jang war, ਖੇਡ khed game, ਗਾਣਾ gaanaa song, "
"ਨਾਚ naach dance, ਫਿਲਮ film film, ਖ਼ਬਰ khabar news, ਚਿੱਠੀ chitthi letter, ਤੋਹਫ਼ਾ "
"tohfaa gift, ਵਿਆਹ viaah wedding, ਮੇਲਾ melaa fair, ਤਿਉਹਾਰ tihaar festival, "
"ਪਰਿਵਾਰ parivaar family, ਰਿਸ਼ਤਾ rishtaa relation, ਗੁਆਂਢੀ guaandhi neighbor, "
"ਮਹਿਮਾਨ mehmaan guest, ਨੌਕਰ naukar servant, ਮਾਲਕ maalk master, ਦਫ਼ਤਰ daftar "
"office, ਦੁਕਾਨ dukaan shop, ਹੋਟਲ hotal hotel, ਹਵਾਈ ਅੱਡਾ havaai addaa airport, "
"ਰੇਲ rel rail, ਬੱਸ bass bus, ਜਹਾਜ਼ jahaaz ship/plane, ਸਾਈਕਲ cycle bicycle, "
"ਮੋਟਰ motor engine, ਬਿਜਲੀ bijli electricity, ਮਸ਼ੀਨ machine machine, ਕਿਤਾਬਾਂ "
"kitaabaan books, ਅਖ਼ਬਾਰ akhbaar newspaper, ਕਲਮ kalam pen, ਕਾਗ਼ਜ਼ kaaghaz paper, "
"ਰੰਗ rang color, ਆਵਾਜ਼ aavaaz voice, ਖ਼ੁਸ਼ਬੂ khushboo fragrance, ਸੁਆਦ svaad "
"taste, ਭੁੱਖ bhukkh hunger, ਪਿਆਸ piyaas thirst, ਨੀਂਦ neend sleep, ਸੁਪਨਾ supnaa "
"dream, ਯਾਦ yaad memory, ਭੁੱਲ bhull forgetting, ਸਵਾਲ savaal question, ਜਵਾਬ "
"javaab answer, ਮਸਲਾ maslaa problem, ਹੱਲ hall solution, ਰਾਹ raah path, ਮੰਜ਼ਿਲ "
"manzil destination, ਸਫ਼ਰ safar journey, ਵਾਪਸੀ vaapsi return, ਸ਼ੁਰੂਆਤ shuruaat "
"beginning, ਅੰਤ ant end. KEY GRAMMAR: SOV order; two genders, two numbers; "
"adjectives agree (-ਾ/-ੀ/-ੇ); postpositions ਨੂੰ/ਨੇ/ਵਿੱਚ/ਉੱਤੇ/ਤੋਂ/ਨਾਲ/ਲਈ/ਦਾ; no "
"articles; negation ਨਹੀਂ after verb; questions front ਕੀ or content words; "
"present -ਦਾ + ਹੈ-family; completed past -ਇਆ with ਨੇ and object agreement; "
"future -ਾਂਗਾ; imperative stem/-ਓ; three tones; respect ladder ਤੂੰ < ਤੁਸੀਂ. "
"PHRASE TABLES: greetings - ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ, ਧੰਨਵਾਦ, ਮਾਫ਼ ਕਰੋ, ਕਿਰਪਾ ਕਰਕੇ, ਫਿਰ "
"ਮਿਲਾਂਗੇ; survival - ਮੈਨੂੰ ਮਦਦ ਚਾਹੀਦੀ ਹੈ, ਇਹ ਕਿੰਨੇ ਦਾ ਹੈ, ਕਿੱਥੇ ਹੈ, ਕੀ ਵਜੇ ਹਨ; "
"politeness - ਹਾਂ ਜੀ, ਜੀ ਆਇਆਂ ਨੂੰ, ਖੁਸ਼ ਰਹੋ; connectors - ਕਿਉਂਕਿ, ਜਦੋਂ...ਤਾਂ, "
"ਜੋ/ਜਿਹੜਾ, ਕਿ, ਜੇ...ਤਾਂ, ਭਾਵੇਂ. LADDER MAP: records 1-9 foundations (script, "
"sound, words), 10-20 compounded (grammar core, twenty-sentence life sets), "
"21-34 advanced (tenses, questions, commands, stories, idioms, dialogues, this "
"review). Study order: read 1-10 in order, live in 11-20 for two weeks, then "
"climb 21-34 one record a day."
),
"how_it_works": (
"Use this record as the daily drill sheet. Cover the Punjabi column and read "
"the transliteration and English; then cover the English and produce the "
"Punjabi from memory. The 200 words are the survival core - with them and the "
"key grammar block you can build thousands of sentences: SOV frame + a noun "
"from the list + a verb from the list + the right ending. Test yourself "
"weekly: pick twenty random words and use each in a sentence; any word you "
"miss goes on tomorrow's drill list. When all 200 sit in memory and the "
"grammar block runs without thought, the database has done its job - you "
"hold the language."
),
"key_points": [
"Consolidated reference: alphabet, 200 core words, key grammar, phrase tables.",
"200 words: the survival core - nouns, verbs, adjectives, pronouns, numbers, time, nature, society.",
"Grammar block: SOV, gender/number, postpositions, negation, questions, tenses, tones, register.",
"Phrase tables: greetings, survival, politeness, connectors.",
"Ladder map: 1-9 foundations, 10-20 compounded, 21-34 advanced.",
"Drill method: cover-and-recall, twenty random words weekly.",
],
"requirements": [
"Memorize all 200 words with cover-and-recall drills.",
"Rebuild the key grammar block from memory on a blank page.",
],
"standards": [
"Reference consolidation: this database, records 1-33",
],
"citations": [
"Bhatia, Tej K. Punjabi: A Cognitive-Descriptive Grammar, Routledge, 1993.",
"Shackle, Christopher. 'Punjabi.' In The Indo-Aryan Languages, Routledge, 2003.",
"The Unicode Standard - Gurmukhi block U+0A00-U+0A7F.",
],
"sig_lens": (
"His Signature reading: the mastery review is the bound volume - thirty-three "
"records gathered, sealed, and shelved as one. The Signature Language Method "
"ends where it began: the painti akhar first, the whole language last, and "
"the learner's own voice signing every page between."),
},
]
