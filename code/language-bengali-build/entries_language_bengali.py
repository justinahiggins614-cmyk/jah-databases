#!/usr/bin/env python3
"""Entries for the Bengali to English databases (Manon's language orders #10-11, 2026-10-17).

Roster rank 6. Bengali (বাংলা), ISO 639-1 bn, Indo-European > Indo-Iranian > Indo-Aryan.

Two databases, 34 ladder-ordered records each:

  language-bengali             - The Bengali to English Database
                                 (public-harvest: real, fact-checked Bengali -
                                 script, sounds, words, grammar, sentences,
                                 stories, idioms, conversations - every record
                                 carrying Bengali script + transliteration +
                                 English + example sentences; standard
                                 references ISO 639-1:2002 bn; ISO 639-3:2007
                                 ben; The Unicode Standard Version 15.0 Bengali
                                 block U+0980-U+09FF; Chatterji 1926; Radice
                                 1994; Ethnologue 27th ed 2024)
  language-bengali-signature   - The Bengali to English Signature Database
                                 (his original Signature Language Method: every
                                 word a sealed sound, every sentence a covenant
                                 of meaning, the learner's voice the Signature
                                 itself; src signature, titles suffixed
                                 " (Signature Edition)", never presented as
                                 authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LBEN- (public) and JAH-LBENS- (signature), verified free in
the manifest id_prefix values and in every shard index (zero hits).

Screening: nothing hate-adjacent, profane, or inappropriate; no religious talk;
nothing on neutralizing or defeating military or defense-grade systems.
Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: every "
            "word a sealed sound, every sentence a covenant of meaning, the "
            "learner's voice the Signature itself - clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_ISO = ("ISO 639-1:2002. Codes for the representation of names of languages - "
           "Part 1: Alpha-2 code. International Organization for Standardization; "
           "2002. Bengali: bn.")
CIT_ISO3 = ("ISO 639-3:2007. Codes for the representation of names of languages - "
            "Part 3: Alpha-3 code. International Organization for Standardization; "
            "2007. Bengali: ben.")
CIT_UNI = ("The Unicode Standard, Version 15.0, Chapter 9: South and Central "
           "Asia - II. Unicode Consortium; 2022. Bengali block U+0980-U+09FF.")
CIT_CHAT = ("Chatterji, Suniti Kumar. The Origin and Development of the Bengali "
            "Language. Calcutta University Press; 1926.")
CIT_RAD = ("Radice, William. Teach Yourself Bengali. Hodder and Stoughton; 1994.")
CIT_ETH = ("Ethnologue: Languages of the World, 27th edition. SIL International; "
           "2024. Bengali language entry.")

STD_CORE = ["ISO 639-1:2002 - language code bn",
            "ISO 639-3:2007 - language code ben",
            "The Unicode Standard, Version 15.0 - Bengali block U+0980-U+09FF"]

ENTRIES = [
{
"key": "overview",
"name": "Bengali Language Overview",
"group": "Foundations",
"ladder_rank": 1, "ladder_tier": "foundations",
"description":
"Bengali (বাংলা, pronounced Bangla) is an Eastern Indo-Aryan language of the Indo-European family. "
"ISO codes: 639-1 bn, 639-3 ben. About 241 million native speakers make it the seventh most spoken "
"native language in the world, with roughly 300 million total speakers. It is the national and official "
"language of Bangladesh, an official language of the Indian states of West Bengal and Tripura, and an "
"additional official language in parts of Assam. Large Bengali-speaking communities live across the "
"world. Bengali is written in the Bengali-Assamese script (Eastern Nagari), an abugida written left to "
"right. Its basic word order is subject-object-verb. Standard Bengali is based on the Nadia (Nadia-Shantipur) "
"dialect of West Bengal, while eastern Bangladesh speaks Bangal dialects; linguists also note distinct "
"varieties such as Sylheti and Chittagonian. Bengali has a celebrated literary tradition and a rich "
"modern culture of song, film, and poetry. Example sentences: বাংলা একটি সুন্দর ভাষা। "
"(Bangla ekti shundor bhasha.) - Bengali is a beautiful language. আমি বাংলা শিখছি। "
"(Ami Bangla shikhchhi.) - I am learning Bengali. বাংলাদেশের ভাষা বাংলা। "
"(Bangladesher bhasha Bangla.) - The language of Bangladesh is Bengali. কলকাতায় বাংলা বলা হয়। "
"(Kolkatay Bangla bola hoy.) - Bengali is spoken in Kolkata. বাংলা আমার প্রিয় ভাষা। "
"(Bangla amar priyo bhasha.) - Bengali is my favorite language.",
"how_it_works":
"Start here before any other record: read the facts once, then speak each example sentence aloud three "
"times - first reading the Bengali script slowly, then the transliteration, then saying the English meaning. "
"Keep a notebook page titled with the native name বাংলা and copy each sentence into it. Move on only when "
"you can say all five sentences from memory.",
"key_points": [
"Native name বাংলা (Bangla); ISO 639-1 bn, 639-3 ben",
"Indo-European > Indo-Iranian > Indo-Aryan > Eastern zone",
"About 241 million native speakers; about 300 million total speakers",
"Official in Bangladesh, West Bengal, Tripura; additional official in parts of Assam",
"Written in the Bengali-Assamese script, left to right; basic word order SOV",
"Standard dialect based on Nadia; eastern Bangal dialects in Bangladesh",
],
"requirements": [
"Read the five example sentences aloud three times each",
"Copy the native name বাংলা into a notebook by hand",
"Memorize the speaker count and the ISO codes",
"Say the five sentences from memory before moving on",
],
"standards": STD_CORE,
"citations": [CIT_ISO, CIT_ISO3, CIT_ETH, CIT_CHAT],
"sig_lens":
"Signature original interpretation: Bengali enters the Signature system as a covenant tongue - 241 "
"million native voices carrying one sealed sound-pattern across two nations. The overview is the "
"Signature oath of scope: know the language's reach before you claim a single word of it.",
},
{
"key": "writing",
"name": "Bengali Writing System",
"group": "Foundations",
"ladder_rank": 1, "ladder_tier": "foundations",
"description":
"Bengali is written in the Bengali-Assamese script (Eastern Nagari), an abugida written left to right. "
"Every consonant carries an inherent vowel অ (o). The 11 vowels (স্বরবর্ণ): অ (o), আ (a), ই (i), ঈ (ii), "
"উ (u), ঊ (uu), ঋ (ri), এ (e), ঐ (oi), ও (o), ঔ (ou). The 39 consonants (ব্যঞ্জনবর্ণ), in five rows of five "
"plus extras: ক (k) খ (kh) গ (g) ঘ (gh) ঙ (ng); চ (ch) ছ (chh) জ (j) ঝ (jh) ঞ (ny); ট (t) ঠ (th) ড (d) ঢ "
"(dh) ণ (n); ত (t) থ (th) দ (d) ধ (dh) ন (n); প (p) ফ (ph) ব (b) ভ (bh) ম (m); then য (j) র (r) ল (l); "
"শ (sh) ষ (sh) স (s) হ (h); ড় (r) ঢ় (rh) য় (y); plus ং (ng), ঃ (h), ঁ (nasalization), ৎ (t). Vowel signs (কার) attach to consonants: া ি ী ু ূ ৃ ে "
"ৈ ো ৌ - for example ক + া = কা (ka). The hasanta (্) kills the inherent vowel and joins consonants: "
"ন্ + ত = ন্ত. Bengali numerals: ০ ১ ২ ৩ ৪ ৫ ৬ ৭ ৮ ৯ (0-9). The danda । is the full stop. Example "
"sentences: এটা বাংলা অক্ষর। (Eta Bangla okkhor.) - This is a Bengali letter. ক খ গ ঘ পড়ো। "
"(Ko kho go gho poro.) - Read ka kha ga gha. ১ ২ ৩ লেখো। (Ek dui tin lekho.) - Write 1 2 3. "
"বাংলা বাম থেকে ডানে লেখা হয়। (Bangla bam theke dane lekha hoy.) - Bengali is written left to right. "
"দাঁড়ি দিয়ে বাক্য শেষ হয়। (Dari diye bakko shesh hoy.) - A sentence ends with a danda.",
"how_it_works":
"Copy the vowel row and the five consonant rows by hand, saying each letter's sound as you write it. "
"Then practice the vowel signs on ক: কা কি কী কু কূ কৃ কে কৈ কো কৌ. Write the numerals ০-৯ twice. Finish "
"by writing the five example sentences and reading them aloud.",
"key_points": [
"Abugida script, left to right; every consonant carries inherent vowel অ",
"11 vowels, 39 consonants, 10 numerals - memorize the counts first",
"Vowel signs (কার) reshape consonants: কা কি কী কু কূ কৃ কে কৈ কো কৌ",
"Hasanta (্) joins consonants into clusters like ন্ত",
"Danda । ends a sentence; numerals ০-৯ differ from Western digits",
],
"requirements": [
"Hand-copy the 11 vowels and 39 consonants with their sounds",
"Write ক with all ten vowel signs from memory",
"Write numerals ০-৯ twice without looking",
"Read the five example sentences aloud",
],
"standards": STD_CORE,
"citations": [CIT_UNI, CIT_ISO, CIT_RAD],
"sig_lens":
"Signature original interpretation: the script is the Signature seal-press - 50 letter-seals and 10 "
"number-seals that stamp meaning onto the page. The learner's hand must cut each seal cleanly before "
"any word can be trusted.",
},
{
"key": "phonology",
"name": "Bengali Pronunciation and Phonology",
"group": "Foundations",
"ladder_rank": 2, "ladder_tier": "foundations",
"description":
"Bengali has 7 oral vowel phonemes (অ আ ই উ এ ও plus অ্যা ae) with nasalized counterparts, and 29 "
"consonant phonemes including aspirated pairs (ক/খ, গ/ঘ, চ/ছ, জ/ঝ, ট/ঠ, ড/ঢ, ত/থ, দ/ধ, প/ফ, ব/ভ). "
"There is no lexical tone. Stress usually falls on the first syllable. The inherent vowel অ is often "
"silent at the end of a word: কথা is pronounced kotha (word), not kothao. English approximations: অ like "
"the o in hot, আ like a in father, ই like ee in see, উ like oo in soon, এ like e in bed, ও like o in go. "
"খ is a breathy kh, ঘ a breathy gh, ছ a breathy chh, ঝ a breathy jh, ঠ a breathy hard t, ঢ a breathy hard d, "
"থ a breathy soft t, ধ a breathy soft d, ফ a breathy ph, ভ a breathy bh. Spoken examples: জল (jol) water, "
"মাছ (machh) fish, ভাত (bhat) cooked rice, ঘর (ghor) house, বই (boi) book, পানি (pani) water, রাত (rat) "
"night, দিন (din) day, ফুল (phul) flower, মাটি (mati) soil, কথা (kotha) word, গান (gan) song. Sentences: "
"জোরে বলো। (Jore bolo.) - Speak loudly. আস্তে বলো। (Aste bolo.) - Speak slowly. ঠিক উচ্চারণ করো। "
"(Thik uchcharon koro.) - Pronounce correctly. শব্দটা আবার বলো। (Shobdota abar bolo.) - Say the word "
"again. কান দিয়ে শোনো। (Kan diye shono.) - Listen with your ears.",
"how_it_works":
"Work in pairs of plain and aspirated consonants: say ক then খ, গ then ঘ, and so on down the rows, "
"feeling the extra breath. Read the twelve example words aloud, then cover the Bengali and say each word "
"from its transliteration. Record yourself if possible and compare with the five sentences.",
"key_points": [
"7 oral vowel phonemes plus nasalized forms; 29 consonant phonemes",
"Aspirated pairs: kh gh chh jh th dh th dh ph bh - feel the breath",
"No lexical tone; stress normally on the first syllable",
"Final inherent অ is usually silent: কথা = kotha",
"অ sounds like o in hot; আ like a in father",
],
"requirements": [
"Drill all ten aspirated pairs aloud, plain then aspirated",
"Say the twelve example words from transliteration alone",
"Read the five sentences aloud with first-syllable stress",
"Write each example word in Bengali script from memory",
],
"standards": STD_CORE,
"citations": [CIT_CHAT, CIT_RAD, CIT_UNI],
"sig_lens":
"Signature original interpretation: pronunciation is the Signature tuning - the breath behind খ ঘ ছ ঝ "
"is the seal of authenticity on every spoken word. A mistuned seal breaks the covenant of meaning, so "
"the ear is trained before the tongue is trusted.",
},
{
"key": "nouns1",
"name": "Bengali Core Nouns I",
"group": "Foundations",
"ladder_rank": 2, "ladder_tier": "foundations",
"description":
"25 essential nouns, each with Bengali script, transliteration, English, and one example sentence. "
"1. মানুষ (manush) person - মানুষ হাসে। (Manush hashe.) A person laughs. "
"2. বাড়ি (bari) house - আমার বাড়ি বড়। (Amar bari boro.) My house is big. "
"3. বই (boi) book - আমি বই পড়ি। (Ami boi pori.) I read a book. "
"4. জল (jol) water - জল খাও। (Jol khao.) Drink water. "
"5. ভাত (bhat) cooked rice - আমি ভাত খাই। (Ami bhat khai.) I eat rice. "
"6. মাছ (machh) fish - মাছ তাজা। (Machh taja.) The fish is fresh. "
"7. মাংস (mangsho) meat - মাংস রান্না করো। (Mangsho ranna koro.) Cook the meat. "
"8. ছেলে (chhele) boy - ছেলেটা খেলে। (Chheleta khele.) The boy plays. "
"9. মেয়ে (meye) girl - মেয়েটা গান গায়। (Meyeta gan gay.) The girl sings. "
"10. বাবা (baba) father - বাবা কাজে যান। (Baba kaje jan.) Father goes to work. "
"11. মা (ma) mother - মা রান্না করেন। (Ma ranna koren.) Mother cooks. "
"12. বন্ধু (bondhu) friend - আমার বন্ধু আসছে। (Amar bondhu ashchhe.) My friend is coming. "
"13. শহর (shohor) city - শহরটা বড়। (Shohorta boro.) The city is big. "
"14. গ্রাম (gram) village - গ্রাম শান্ত। (Gram shanto.) The village is peaceful. "
"15. রাস্তা (rasta) road - রাস্তা লম্বা। (Rasta lomba.) The road is long. "
"16. গাড়ি (gari) car - গাড়িটা দ্রুত। (Garita druto.) The car is fast. "
"17. টাকা (taka) money - টাকা দরকার। (Taka dorkar.) Money is needed. "
"18. সময় (shomoy) time - সময় কম। (Shomoy kom.) Time is short. "
"19. দিন (din) day - আজ সুন্দর দিন। (Aj shundor din.) Today is a beautiful day. "
"20. রাত (rat) night - রাত অন্ধকার। (Rat ondhokar.) The night is dark. "
"21. হাত (hat) hand - হাত ধোও। (Hat dhowo.) Wash your hands. "
"22. চোখ (chokh) eye - চোখ খোলো। (Chokh kholo.) Open your eyes. "
"23. মাথা (matha) head - মাথা ব্যথা করছে। (Matha byatha korchhe.) My head aches. "
"24. স্কুল (skul) school - ছেলেরা স্কুলে যায়। (Chhelera skule jay.) The boys go to school. "
"25. কাজ (kaj) work - কাজ শেষ। (Kaj shesh.) The work is finished.",
"how_it_works":
"Learn five nouns a day. For each, cover the English, look at the Bengali, and say the example sentence "
"aloud. Then reverse: read the English sentence and produce the Bengali noun. Test yourself at day's end "
"by writing all 25 from memory.",
"key_points": [
"25 nouns covering people, places, food, body, time, and daily life",
"Every noun appears in a full translated sentence - never a bare list",
"Definite nouns take -টা/-টি: ছেলেটা (the boy), মেয়েটা (the girl)",
"Plurals and cases come later; first own these 25 cold",
"Say each sentence aloud - nouns stick through speech, not staring",
],
"requirements": [
"Learn five nouns per day with their sentences",
"Recite each sentence aloud from the Bengali script",
"Reverse-test: English sentence to Bengali noun",
"Write all 25 nouns from memory at the end",
],
"standards": STD_CORE,
"citations": [CIT_RAD, CIT_ETH],
"sig_lens":
"Signature original interpretation: these 25 nouns are the first Signature stones - person, house, book, "
"water, rice - the load-bearing words of daily life. Each stone is sealed with a sentence so it can bear "
"weight in real speech.",
},
{
"key": "verbs1",
"name": "Bengali Core Verbs I",
"group": "Foundations",
"ladder_rank": 2, "ladder_tier": "foundations",
"description":
"25 essential verbs in dictionary form with first-person present sentences. "
"1. খাওয়া (khaowa) eat - আমি ভাত খাই। (Ami bhat khai.) I eat rice. "
"2. পান করা (pan kora) drink - আমি জল পান করি। (Ami jol pan kori.) I drink water. "
"3. যাওয়া (jaowa) go - আমি স্কুলে যাই। (Ami skule jai.) I go to school. "
"4. আসা (asha) come - আমি বাড়ি আসি। (Ami bari ashi.) I come home. "
"5. করা (kora) do - আমি কাজ করি। (Ami kaj kori.) I do the work. "
"6. বলা (bola) say - আমি কথা বলি। (Ami kotha boli.) I speak. "
"7. পড়া (pora) read/study - আমি বই পড়ি। (Ami boi pori.) I read a book. "
"8. লেখা (lekha) write - আমি চিঠি লিখি। (Ami chithi likhi.) I write a letter. "
"9. দেখা (dekha) see - আমি ছবি দেখি। (Ami chhobi dekhi.) I see the picture. "
"10. শোনা (shona) listen - আমি গান শুনি। (Ami gan shuni.) I listen to songs. "
"11. ঘুমানো (ghumano) sleep - আমি রাতে ঘুমাই। (Ami rate ghumai.) I sleep at night. "
"12. ওঠা (otha) get up - আমি সকালে উঠি। (Ami shokale uthi.) I get up in the morning. "
"13. বসা (bosha) sit - আমি চেয়ারে বসি। (Ami cheyare boshi.) I sit on the chair. "
"14. দাঁড়ানো (darano) stand - আমি দাঁড়াই। (Ami darai.) I stand. "
"15. হাঁটা (hata) walk - আমি পার্কে হাঁটি। (Ami parke hati.) I walk in the park. "
"16. দৌড়ানো (dourano) run - আমি মাঠে দৌড়াই। (Ami mathe dourai.) I run in the field. "
"17. দেওয়া (deowa) give - আমি বই দিই। (Ami boi dii.) I give the book. "
"18. নেওয়া (neowa) take - আমি টাকা নিই। (Ami taka nii.) I take the money. "
"19. কেনা (kena) buy - আমি ফল কিনি। (Ami phol kini.) I buy fruit. "
"20. বেচা (becha) sell - আমি বই বেচি। (Ami boi bechi.) I sell books. "
"21. জানা (jana) know - আমি বাংলা জানি। (Ami Bangla jani.) I know Bengali. "
"22. চাওয়া (chaowa) want - আমি জল চাই। (Ami jol chai.) I want water. "
"23. ভালোবাসা (bhalobasha) love - আমি মাকে ভালোবাসি। (Ami make bhalobashi.) I love mother. "
"24. খেলা (khela) play - আমি ফুটবল খেলি। (Ami football kheli.) I play football. "
"25. রান্না করা (ranna kora) cook - আমি ভাত রান্না করি। (Ami bhat ranna kori.) I cook rice.",
"how_it_works":
"Verbs are the engine of every sentence. Learn the dictionary form (খাওয়া) and the আমি form (খাই) as a "
"pair. Act out each verb while saying its sentence - stand for দাঁড়ানো, sit for বসা. Five verbs a day, "
"then combine each with a noun from the nouns record to build your own sentences.",
"key_points": [
"25 verbs covering motion, senses, daily actions, and communication",
"Dictionary form ends in -ওয়া/-া; আমি present form is the working form",
"Every verb drilled in a full first-person sentence",
"করা (do) combines with nouns to make hundreds of verbs: রান্না করা, পান করা",
"Physical acting locks verbs into memory faster than reading",
],
"requirements": [
"Learn dictionary form plus আমি form as a pair",
"Act out each verb while saying its sentence",
"Combine each new verb with a noun from the nouns record",
"Build five original sentences using আমি + verb + object",
],
"standards": STD_CORE,
"citations": [CIT_RAD, CIT_CHAT],
"sig_lens":
"Signature original interpretation: verbs are the Signature engines - 25 moving parts that drive every "
"covenant of meaning. করা is the master engine: bolt it to any noun and it pulls a new verb into the "
"train.",
},
{
"key": "adjadv",
"name": "Bengali Adjectives and Adverbs",
"group": "Foundations",
"ladder_rank": 2, "ladder_tier": "foundations",
"description":
"25 adjectives and 15 adverbs, each in a translated sentence. Adjectives come before the noun and do not "
"change for gender or number. Adjectives: 1. ভালো (bhalo) good - এটা ভালো বই। (Eta bhalo boi.) This is a "
"good book. 2. খারাপ (kharap) bad - আবহাওয়া খারাপ। (Abhawa kharap.) The weather is bad. 3. বড় (boro) "
"big - বড় গাছ। (Boro gachh.) A big tree. 4. ছোট (chhoto) small - ছোট ঘর। (Chhoto ghor.) A small room. "
"5. নতুন (notun) new - নতুন জামা। (Notun jama.) New clothes. 6. পুরনো (purono) old - পুরনো বাড়ি। "
"(Purono bari.) An old house. 7. সুন্দর (shundor) beautiful - সুন্দর ফুল। (Shundor phul.) A beautiful "
"flower. 8. লম্বা (lomba) tall - লম্বা ছেলে। (Lomba chhele.) A tall boy. 9. খাটো (khato) short - খাটো "
"মেয়ে। (Khato meye.) A short girl. 10. ভারী (bhari) heavy - ভারী বাক্স। (Bhari baksho.) A heavy box. "
"11. হালকা (halka) light - হালকা ব্যাগ। (Halka byag.) A light bag. 12. গরম (gorom) hot - গরম চা। "
"(Gorom cha.) Hot tea. 13. ঠান্ডা (thanda) cold - ঠান্ডা জল। (Thanda jol.) Cold water. 14. মিষ্টি (mishti) "
"sweet - মিষ্টি আম। (Mishti am.) A sweet mango. 15. টক (tok) sour - টক লেবু। (Tok lebu.) A sour lemon. "
"16. নরম (norom) soft - নরম বালিশ। (Norom balish.) A soft pillow. 17. শক্ত (shokto) hard - শক্ত পাথর। "
"(Shokto pathor.) A hard stone. 18. সহজ (shohoj) easy - সহজ প্রশ্ন। (Shohoj proshno.) An easy question. "
"19. কঠিন (kothin) difficult - কঠিন কাজ। (Kothin kaj.) Difficult work. 20. দ্রুত (druto) fast - দ্রুত "
"ট্রেন। (Druto tren.) A fast train. 21. ধীর (dhir) slow - ধীর গাড়ি। (Dhir gari.) A slow car. 22. "
"পরিষ্কার (porishkar) clean - পরিষ্কার ঘর। (Porishkar ghor.) A clean room. 23. নোংরা (nongra) dirty - "
"নোংরা জামা। (Nongra jama.) Dirty clothes. 24. সত্যি (shotti) true - সত্যি কথা। (Shotti kotha.) A true "
"statement. 25. মিথ্যা (mittha) false - মিথ্যা খবর। (Mittha khobor.) False news. Adverbs: 1. খুব (khub) "
"very - আমি খুব খুশি। (Ami khub khushi.) I am very happy. 2. একটু (ektu) a little - একটু বসো। (Ektu "
"bosho.) Sit a little. 3. এখন (ekhon) now - এখন যাও। (Ekhon jao.) Go now. 4. পরে (pore) later - পরে "
"আসবো। (Pore ashbo.) I will come later. 5. আজ (aj) today - আজ বৃষ্টি হচ্ছে। (Aj brishti hochchhe.) It is "
"raining today. 6. কাল (kal) tomorrow/yesterday - কাল স্কুল বন্ধ। (Kal skul bondho.) School is closed "
"tomorrow. 7. এখানে (ekhane) here - এখানে বসো। (Ekhane bosho.) Sit here. 8. ওখানে (okhane) there - "
"ওখানে যাও। (Okhane jao.) Go there. 9. সবসময় (shobshomoy) always - সে সবসময় হাসে। (She shobshomoy "
"hashe.) He always smiles. 10. কখনো (kokhono) sometimes - আমি কখনো দেরি করি। (Ami kokhono deri kori.) I "
"am sometimes late. 11. দ্রুত (druto) quickly - দ্রুত এসো। (Druto esho.) Come quickly. 12. আস্তে (aste) "
"slowly - আস্তে হাঁটো। (Aste hato.) Walk slowly. 13. ভালোভাবে (bhalobhabe) well - ভালোভাবে পড়ো। "
"(Bhalobhabe poro.) Study well. 14. একসাথে (ekshathe) together - একসাথে খেলি। (Ekshathe kheli.) We play "
"together. 15. শীঘ্রই (shighroi) soon - শীঘ্রই আসছি। (Shighroi ashchhi.) I am coming soon.",
"how_it_works":
"Adjectives are the easiest win in Bengali: no gender, no number changes - just place before the noun. "
"Learn them in opposite pairs (বড়/ছোট, গরম/ঠান্ডা, ভালো/খারাপ). For adverbs, note position: খুব goes "
"before the adjective, time words like এখন and আজ often start the sentence.",
"key_points": [
"Adjectives never inflect for gender or number - one form fits all",
"Adjectives stand before the noun: ভালো বই, বড় গাছ",
"Learn adjectives in opposite pairs for double speed",
"খুব intensifies adjectives; একটু softens requests",
"Time adverbs (এখন, আজ, কাল) usually open the sentence",
],
"requirements": [
"Memorize the 25 adjectives in opposite pairs",
"Place each adjective before three different nouns aloud",
"Use খুব with ten adjectives in spoken sentences",
"Write all 15 adverbs with one original sentence each",
],
"standards": STD_CORE,
"citations": [CIT_RAD, CIT_CHAT],
"sig_lens":
"Signature original interpretation: adjectives are the Signature polish - one unchanging seal pressed "
"before any noun, never bent for gender or number. Adverbs are the Signature timing gears: খুব, এখন, "
"আস্তে set the speed and pressure of every action.",
},
{
"key": "pronouns",
"name": "Bengali Pronouns",
"group": "Foundations",
"ladder_rank": 3, "ladder_tier": "foundations",
"description":
"Full pronoun paradigms with sentences. Personal: আমি (ami) I - আমি ছাত্র। (Ami chhatro.) I am a "
"student. আমরা (amra) we - আমরা বন্ধু। (Amra bondhu.) We are friends. তুই (tui) you, intimate - তুই "
"কোথায়? (Tui kothay?) Where are you? তুমি (tumi) you, familiar - তুমি কেমন আছো? (Tumi kemon achho?) How "
"are you? আপনি (apni) you, formal - আপনি কেমন আছেন? (Apni kemon achhen?) How are you? সে (she) he/she - "
"সে ভালো। (She bhalo.) He/she is good. তিনি (tini) he/she, formal - তিনি শিক্ষক। (Tini shikkhok.) He/she "
"is a teacher. Demonstrative: এটা (eta) this - এটা বই। (Eta boi.) This is a book. ওটা (ota) that - ওটা "
"কলম। (Ota kolom.) That is a pen. এরা (era) these people - এরা ছাত্র। (Era chhatro.) These are students. "
"ওরা (ora) those people - ওরা খেলছে। (Ora khelchhe.) They are playing. Possessive: আমার (amar) my - "
"আমার নাম রহিম। (Amar nam Rohim.) My name is Rahim. আমাদের (amader) our - আমাদের বাড়ি। (Amader bari.) "
"Our house. তোমার (tomar) your - তোমার বই। (Tomar boi.) Your book. আপনার (apnar) your, formal - আপনার "
"নাম কী? (Apnar nam ki?) What is your name? তার (tar) his/her - তার গাড়ি। (Tar gari.) His/her car. "
"তাদের (tader) their - তাদের স্কুল। (Tader skul.) Their school. Interrogative: কে (ke) who - কে আসছে? "
"(Ke ashchhe?) Who is coming? কী (ki) what - এটা কী? (Eta ki?) What is this? কোন (kon) which - কোন বই? "
"(Kon boi?) Which book? কত (koto) how much/many - কত টাকা? (Koto taka?) How much money? Reflexive: নিজে "
"(nije) self - নিজে করো। (Nije koro.) Do it yourself. Three levels of you: তুই for close friends and "
"children, তুমি for peers, আপনি for elders and strangers - using আপনি shows respect.",
"how_it_works":
"Master the three yous first - this is the social key to Bengali. Drill the personal set aloud in order: "
"আমি আমরা তুই তুমি আপনি সে তিনি. Then attach possessives: আমার আমাদের তোমার আপনার তার তাদের. Quiz "
"yourself: point at objects and say এটা আমার, ওটা তোমার.",
"key_points": [
"Three levels of you: তুই intimate, তুমি familiar, আপনি formal - respect lives here",
"সে covers he and she; তিনি is the formal he/she",
"Possessives add -র/-দের: আমার, তোমার, তার, আমাদের, তাদের",
"এটা/ওটা for things; এরা/ওরা for people",
"কী asks what, কে asks who, কোন asks which, কত asks how much",
],
"requirements": [
"Recite আমি আমরা তুই তুমি আপনি সে তিনি from memory",
"Use আপনি in five spoken sentences to practice respect",
"Point at ten objects saying এটা আমার or ওটা তোমার",
"Ask and answer all four interrogative pronouns aloud",
],
"standards": STD_CORE,
"citations": [CIT_RAD, CIT_CHAT],
"sig_lens":
"Signature original interpretation: pronouns are the Signature address seals - আপনি, তুমি, তুই are three "
"grades of the same seal, and pressing the wrong grade breaks the social covenant. The learner seals every "
"relationship correctly before speaking.",
},
{
"key": "numbers",
"name": "Bengali Numbers and Time",
"group": "Foundations",
"ladder_rank": 3, "ladder_tier": "foundations",
"description":
"Numbers 1-20: এক (ek) 1, দুই (dui) 2, তিন (tin) 3, চার (char) 4, পাঁচ (panch) 5, ছয় (chhoy) 6, সাত (shat) "
"7, আট (at) 8, নয় (noy) 9, দশ (dosh) 10, এগারো (egaro) 11, বারো (baro) 12, তেরো (tero) 13, চৌদ্দ (chouddo) "
"14, পনেরো (ponero) 15, ষোলো (sholo) 16, সতেরো (shotero) 17, আঠারো (atharo) 18, উনিশ (unish) 19, বিশ "
"(bish) 20. Tens: ত্রিশ (trish) 30, চল্লিশ (chollish) 40, পঞ্চাশ (ponchash) 50, ষাট (shat) 60, সত্তর "
"(shottor) 70, আশি (ashi) 80, নব্বই (nobboi) 90, একশো (eksho) 100. Ordinals: প্রথম (prothom) first, "
"দ্বিতীয় (ditiyo) second, তৃতীয় (tritiyo) third. Days: রবিবার (robibar) Sunday, সোমবার (shombar) Monday, "
"মঙ্গলবার (mongolbar) Tuesday, বুধবার (budhbar) Wednesday, বৃহস্পতিবার (brihoshpotibar) Thursday, "
"শুক্রবার (shukrobar) Friday, শনিবার (shonibar) Saturday. Months: বৈশাখ (boishakh), জ্যৈষ্ঠ (jyoshtho), "
"আষাঢ় (asharh), শ্রাবণ (srabon), ভাদ্র (bhadro), আশ্বিন (ashwin), কার্তিক (kartik), অগ্রহায়ণ (ogrohayon), "
"পৌষ (poush), মাঘ (magh), ফাল্গুন (falgun), চৈত্র (choitro). Seasons: গ্রীষ্ম (grishsho) summer, বর্ষা "
"(borsha) monsoon, শরৎ (shorot) autumn, হেমন্ত (hemonto) late autumn, শীত (shit) winter, বসন্ত (boshonto) "
"spring. Clock time: তিনটা (tinta) 3 o'clock, সাড়ে তিনটা (share tinta) 3:30, সোয়া তিনটা (shoa tinta) "
"3:15, পৌনে চারটা (poune chartta) 3:45. Example sentences: আমার দুইটা বই আছে। (Amar duita boi achhe.) I "
"have two books. আজ সোমবার। (Aj shombar.) Today is Monday. এখন তিনটা বাজে। (Ekhon tinta baje.) It is 3 "
"o'clock now. সে প্রথম হয়েছে। (She prothom hoyechhe.) He came first. বর্ষাকালে বৃষ্টি হয়। (Borshakale "
"brishti hoy.) It rains in the monsoon season.",
"how_it_works":
"Count aloud 1-20 daily until automatic, then add the tens. Learn the days by saying today's day each "
"morning. Practice clock time by announcing the real time in Bengali every hour: এখন চারটা বাজে. Write "
"three dates in Bengali each day.",
"key_points": [
"1-20 by heart first; tens follow the pattern trish chollish ponchash shat shottor ashi nobboi",
"টা marks o'clock: তিনটা; সাড়ে half past, সোয়া quarter past, পৌনে quarter to",
"12 Bengali months; 6 seasons including the monsoon বর্ষা",
"Ordinals প্রথম দ্বিতীয় তৃতীয় for rankings",
"Counters: -টা for things (দুইটা বই), -জন for people",
],
"requirements": [
"Count 1-20 aloud without hesitation",
"Say the current time in Bengali every hour for a day",
"Name all seven days and twelve months from memory",
"Write five sentences using numbers with -টা counters",
],
"standards": STD_CORE,
"citations": [CIT_RAD, CIT_ETH],
"sig_lens":
"Signature original interpretation: numbers are the Signature measure-marks - 100 sealed steps from এক "
"to একশো, each a calibrated weight. Time words are the Signature clock: সাড়ে, সোয়া, পৌনে divide the "
"hour the way a seal divides wax.",
},
{
"key": "greetings",
"name": "Bengali Greetings and Everyday Phrases",
"group": "Foundations",
"ladder_rank": 3, "ladder_tier": "foundations",
"description":
"30 greetings and everyday phrases with usage notes. 1. নমস্কার (nomoskar) - hello, formal, all-purpose. "
"2. আদাব (adab) - respectful greeting. 3. আসসালামু আলাইকুম (assalamu alaikum) - peace greeting. 4. শুভ "
"সকাল (shubho shokal) - good morning. 5. শুভ দুপুর (shubho dupur) - good afternoon. 6. শুভ সন্ধ্যা "
"(shubho shondha) - good evening. 7. শুভ রাত্রি (shubho ratri) - good night. 8. কেমন আছেন? (kemon "
"achhen?) - how are you, formal. 9. কেমন আছো? (kemon achho?) - how are you, familiar. 10. ভালো আছি। "
"(bhalo achhi.) - I am well. 11. ধন্যবাদ। (dhonnobad.) - thank you. 12. অনেক ধন্যবাদ। (onek dhonnobad.) "
"- thank you very much. 13. দুঃখিত। (dukkhito.) - sorry. 14. মাফ করবেন। (maph korben.) - excuse me, "
"formal. 15. বিদায়। (biday.) - farewell. 16. আবার দেখা হবে। (abar dekha hobe.) - see you again. 17. "
"স্বাগতম। (shagotom.) - welcome. 18. দয়া করে। (doya kore.) - please. 19. অভিনন্দন। (obhinondon.) - "
"congratulations. 20. শুভ জন্মদিন। (shubho jonmodin.) - happy birthday. 21. ঈদ মোবারক। (eid mubarak.) - "
"Blessed Eid. 22. শুভ নববর্ষ। (shubho noboborsho.) - happy new year. 23. কেমন চলছে? (kemon cholchhe?) - "
"how is it going? 24. অনেকদিন পর। (onekdin por.) - long time no see. 25. আপনার সাথে দেখা করে ভালো "
"লাগলো। (apnar shathe dekha kore bhalo laglo.) - nice to meet you. 26. খোদা হাফেজ। (khoda hafez.) - "
"goodbye. 27. চলি তাহলে। (choli tahole.) - bye, informal. 28. বুঝতে পারছি না। (bujhte parchhi na.) - I "
"do not understand. 29. আস্তে বলুন। (aste bolun.) - please speak slowly. 30. সাহায্য করুন। (shahajjo "
"korun.) - please help. Extra survival lines: ঠিক আছে। (thik achhe.) OK. হ্যাঁ। (hya.) Yes. না। (na.) No. "
"কিছু মনে করবেন না। (kichhu mone korben na.) Do not mind.",
"how_it_works":
"Greetings are muscle memory: greet everyone you meet for a week using only these. Practice the formal "
"and familiar pairs side by side (কেমন আছেন / কেমন আছো). Role-play meeting, thanking, apologizing, and "
"leaving with a partner or aloud to yourself.",
"key_points": [
"নমস্কার works everywhere; কেমন আছেন shows respect, কেমন আছো warmth",
"দয়া করে softens every request; ধন্যবাদ closes every favor",
"দুঃখিত repairs; মাফ করবেন opens a stranger's attention",
"শুভ সকাল/দুপুর/সন্ধ্যা/রাত্রি cover the whole day",
"বুঝতে পারছি না and আস্তে বলুন are survival tools - use them freely",
],
"requirements": [
"Greet in Bengali only for one full week",
"Role-play meeting, thanking, apologizing, and leaving",
"Drill formal/familiar pairs until the switch is automatic",
"Memorize all 30 with correct usage notes",
],
"standards": STD_CORE,
"citations": [CIT_RAD, CIT_ETH],
"sig_lens":
"Signature original interpretation: greetings are the Signature handshake seals - 30 polished impressions "
"that open every door. নমস্কার is the master seal: pressed with palms together, it signs respect into "
"every first meeting.",
},
{
"key": "grammar",
"name": "Bengali Grammar Essentials",
"group": "Foundations",
"ladder_rank": 3, "ladder_tier": "foundations",
"description":
"The essential grammar in one record, each rule with translated sentences. Word order: subject-object-verb "
"- আমি ভাত খাই। (Ami bhat khai.) I eat rice. সে বই পড়ে। (She boi pore.) He reads a book. Gender: none - "
"adjectives and verbs never change for gender. সে covers he and she. Articles: the definite article is a "
"suffix - -টা/-টি for things, -জন for people: বইটা (boita) the book, ছেলেটা (chheleta) the boy, মেয়েটি "
"(meyeti) the girl, লোকজন (lokjon) people. Indefinite: একটা (ekta) a: একটা বই (ekta boi) a book. Number: "
"plurals take -গুলো/-গুলি for things and -রা for people: বইগুলো (boigulo) the books, ছেলেরা (chhelera) "
"the boys. Cases: -কে marks the object or direction: মাকে (make) to mother; -র/-এর marks possession: "
"রহিমের (rohimer) Rahim's; -এ/-তে marks location: বাড়িতে (barite) at home, স্কুলে (skule) at school; "
"-থেকে means from: ঢাকা থেকে (Dhaka theke) from Dhaka. Negation: না follows the verb - আমি যাই না। (Ami "
"jai na.) I do not go. With আছে use নেই: টাকা নেই। (Taka nei.) There is no money. Questions: use question "
"words (কে কী কোথায় কখন কেন কেমন) - তুমি কোথায় যাও? (Tumi kothay jao?) Where are you going? For yes/no "
"questions add কি at the end - তুমি যাবে কি? (Tumi jabe ki?) Will you go? Be-verbs: আমি হই/আছি, তুমি "
"হও/আছো, সে হয়/আছে: আমি ছাত্র। (Ami chhatro.) I am a student. সে বাড়িতে আছে। (She barite achhe.) He is "
"at home.",
"how_it_works":
"Do not memorize rules in isolation - for each rule, write three of your own sentences and say them aloud. "
"Build a personal sentence bank: 5 SOV sentences, 5 with -টা, 5 with -কে, 5 negatives, 5 questions. Read "
"the bank daily for a week.",
"key_points": [
"SOV word order: আমি ভাত খাই - the verb always closes the sentence",
"No grammatical gender anywhere",
"Articles are suffixes: -টা/-টি things, -জন people; plurals -গুলো/-রা",
"Cases: -কে object/to, -র of, -এ/-তে in/at, -থেকে from",
"না negates verbs; নেই negates existence; কি ends yes/no questions",
],
"requirements": [
"Write three original sentences per rule and speak them",
"Build a 25-sentence personal grammar bank",
"Read the bank aloud daily for one week",
"Convert five statements into questions with কি",
],
"standards": STD_CORE,
"citations": [CIT_CHAT, CIT_RAD],
"sig_lens":
"Signature original interpretation: grammar is the Signature frame-shop - SOV the fixed frame, -টা -কে -র "
"the corner brackets, না the eraser seal. Every sentence is framed identically so meaning hangs straight "
"every time.",
},
]

ENTRIES += [
{
"key": "home",
"name": "Bengali Home and Family Sentences",
"group": "Foundations",
"ladder_rank": 3, "ladder_tier": "foundations",
"description":
"20 sentences about the house, rooms, furniture, and family. 1. এটা আমার বাড়ি। (Eta amar bari.) This "
"is my house. 2. বাড়িতে তিনটা ঘর আছে। (Barite tinta ghor achhe.) There are three rooms in the house. 3. "
"এটা বসার ঘর। (Eta boshar ghor.) This is the living room. 4. রান্নাঘরে মা রান্না করছেন। (Rannaghore ma "
"ranna korchhen.) Mother is cooking in the kitchen. 5. শোবার ঘরে বিছানা আছে। (Shobar ghore bichhana "
"achhe.) There is a bed in the bedroom. 6. বাথরুমটা পরিষ্কার। (Bathrumta porishkar.) The bathroom is clean. "
"7. টেবিলে বই রাখো। (Tabile boi rakho.) Put the book on the table. 8. চেয়ারে বসো। (Cheyare bosho.) Sit on "
"the chair. 9. জানালা খোলো। (Janala kholo.) Open the window. 10. দরজা বন্ধ করো। (Dorja bondho koro.) Close "
"the door. 11. আমার বাবা ডাক্তার। (Amar baba daktar.) My father is a doctor. 12. আমার মা শিক্ষক। (Amar ma "
"shikkhok.) My mother is a teacher. 13. আমার এক ভাই আছে। (Amar ek bhai achhe.) I have one brother. 14. "
"আমার বোন ছোট। (Amar bon chhoto.) My sister is young. 15. দাদা কলকাতায় থাকেন। (Dada Kolkatay thaken.) "
"Grandfather lives in Kolkata. 16. দাদি গল্প বলেন। (Dadi golpo bolen.) Grandmother tells stories. 17. "
"আমরা একসাথে খাই। (Amra ekshathe khai.) We eat together. 18. পরিবারটা সুখী। (Poribarta sukhi.) The family "
"is happy. 19. ছাদে কাপড় শুকাচ্ছে। (Chhade kapor shukachchhe.) Clothes are drying on the roof. 20. বাগানে "
"ফুল ফুটেছে। (Bagane phul phutechhe.) Flowers have bloomed in the garden.",
"how_it_works":
"Walk through your own home naming each room and object in Bengali: এটা রান্নাঘর, এটা টেবিল. Describe "
"your family members with one sentence each. Say all 20 sentences while pointing at the real things - "
"the room becomes the classroom.",
"key_points": [
"Room words: বসার ঘর, রান্নাঘর, শোবার ঘর, বাথরুম",
"Location marker -তে/-এ: বাড়িতে, রান্নাঘরে, বাগানে",
"Family: বাবা মা ভাই বোন দাদা দাদি",
"আছে states existence: বিছানা আছে, তিনটা ঘর আছে",
"Continuous -ছ- form appears: রান্না করছেন, শুকাচ্ছে",
],
"requirements": [
"Name every room and five objects in your home in Bengali",
"Describe each family member in one Bengali sentence",
"Say all 20 sentences pointing at real things",
"Write five new sentences about your own house",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: the home record is the Signature floor-plan - every room sealed with "
"its true name, every family member a load-bearing wall. Speak the house and the house holds the "
"language.",
},
{
"key": "food",
"name": "Bengali Food and Cooking Sentences",
"group": "Foundations",
"ladder_rank": 3, "ladder_tier": "foundations",
"description":
"20 sentences about meals, ingredients, cooking, and restaurants. 1. আমি ভাত খাই। (Ami bhat khai.) I eat "
"rice. 2. মা ডাল রান্না করছেন। (Ma dal ranna korchhen.) Mother is cooking lentils. 3. মাছ ভাজি খেতে মজা। "
"(Machh bhaji khete moja.) Fried fish is tasty to eat. 4. রুটি গরম আছে। (Ruti gorom achhe.) The bread is "
"hot. 5. চায়ে চিনি দাও। (Chaye chini dao.) Put sugar in the tea. 6. আমি মিষ্টি পছন্দ করি। (Ami mishti "
"pochhondo kori.) I like sweets. 7. বাজারে তাজা সবজি আছে। (Bajare taja shobji achhe.) There are fresh "
"vegetables in the market. 8. আম পেকেছে। (Am pekechhe.) The mangoes are ripe. 9. দুধ ফুটছে। (Dudh "
"phutchhe.) The milk is boiling. 10. ডিম সিদ্ধ করো। (Dim shiddho koro.) Boil the eggs. 11. রেস্তোরাঁয় "
"খাবার ভালো। (Restoray khabar bhalo.) The food at the restaurant is good. 12. ওয়েটার, মেনু দিন। "
"(Oyatar, menu din.) Waiter, give the menu. 13. বিলটা দিন। (Bilta din.) Give the bill. 14. ঝাল কম দেবেন। "
"(Jhal kom deben.) Please make it less spicy. 15. আমি শাকসবজি খাই। (Ami shakshobji khai.) I eat vegetables. "
"16. পানি ঠান্ডা। (Pani thanda.) The water is cold. 17. নাস্তায় পরোটা খেলাম। (Nastay porota khelam.) I "
"ate paratha for breakfast. 18. দুপুরে ভাত খাবো। (Dupure bhat khabo.) I will eat rice at noon. 19. রাতে "
"হালকা খাবার খাই। (Rate halka khabar khai.) I eat light food at night. 20. খাবারটা খুব সুস্বাদু। "
"(Khabarta khub shushshadu.) The food is very delicious.",
"how_it_works":
"Cook one Bengali meal narrating each step in Bengali: পানি ফুটছে, ডাল দিচ্ছি. Order food in Bengali at "
"a restaurant or in role-play: মেনু দিন, বিলটা দিন. Taste words (ঝাল মিষ্টি টক) get learned fastest at "
"the table - say them as you taste.",
"key_points": [
"ভাত ডাল মাছ: the heart of the Bengali plate",
"রান্না করা + object builds any cooking sentence",
"Restaurant chain: মেনু দিন -> খাবার -> বিলটা দিন",
"ঝাল কম দেবেন - the polite spice control",
"Perfect -েছে form: পেকেছে, ফুটছে for completed/ongoing cooking",
],
"requirements": [
"Narrate cooking one full meal in Bengali",
"Role-play ordering and paying at a restaurant",
"Describe five tastes in Bengali while tasting",
"Write your own five-sentence meal description",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: food is the Signature hearth - ভাত ডাল মাছ the three sealed staples, "
"every cooking verb a flame under the pot. The learner who can order, cook, and praise a meal in Bengali "
"holds the hearth-seal.",
},
{
"key": "travel",
"name": "Bengali Travel and Directions Sentences",
"group": "Compounded",
"ladder_rank": 4, "ladder_tier": "compounded",
"description":
"20 sentences for transport, directions, tickets, and lodging. 1. স্টেশন কোথায়? (Steshon kothay?) Where "
"is the station? 2. ঢাকা কত দূর? (Dhaka koto dur?) How far is Dhaka? 3. টিকিট কত টাকা? (Tikit koto taka?) "
"How much is the ticket? 4. বাস কখন ছাড়বে? (Bash kokhon chharbe?) When will the bus leave? 5. ট্রেন দেরি "
"করছে। (Tren deri korchhe.) The train is late. 6. ডানে যান। (Dane jan.) Go right. 7. বামে ঘুরুন। (Bame "
"ghurun.) Turn left. 8. সোজা যান। (Shoja jan.) Go straight. 9. হোটেলটা কাছে। (Hotelta kachhe.) The hotel "
"is near. 10. একটা রুম চাই। (Ekta rum chai.) I want a room. 11. ভাড়া কত? (Bhara koto?) What is the fare? "
"12. ট্যাক্সি ডাকুন। (Taxy dakun.) Call a taxi. 13. বিমানবন্দর যাবো। (Bimanbondor jabo.) I will go to the "
"airport. 14. নৌকায় নদী পার হবো। (Nou kay nodi par hobo.) I will cross the river by boat. 15. রিকশায় "
"চড়ো। (Rikshay choro.) Ride the rickshaw. 16. মানচিত্র দেখুন। (Manchitro dekhun.) Look at the map. 17. "
"আমি হারিয়ে গেছি। (Ami hariye gechhi.) I am lost. 18. সাহায্য করুন। (Shahajjo korun.) Please help. 19. "
"পাসপোর্ট দেখান। (Pashport dekhan.) Show the passport. 20. যাত্রা শুভ হোক। (Jatra shubho hok.) Have a safe "
"journey.",
"how_it_works":
"Draw a simple map and give directions in Bengali: ডানে, বামে, সোজা. Role-play buying a ticket, asking "
"the fare, and checking into a hotel. Memorize the lost-and-help pair (আমি হারিয়ে গেছি / সাহায্য করুন) "
"cold - those two buy safety anywhere.",
"key_points": [
"কোথায় opens every location question; কত দূর asks distance",
"ডানে বামে সোজা: the three direction seals",
"Transport verbs: যাবো (will go), পার হবো (will cross), চড়ো (ride)",
"Lodging chain: একটা রুম চাই -> ভাড়া কত -> টাকা দিন",
"আমি হারিয়ে গেছি + সাহায্য করুন = safety pair",
],
"requirements": [
"Give directions on a drawn map using ডানে বামে সোজা",
"Role-play ticket buying and hotel check-in",
"Memorize the safety pair perfectly",
"Write a five-sentence travel plan in Bengali",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: travel sentences are the Signature road-marks - ডানে বামে সোজা "
"sealed arrows, ভাড়া কত the toll seal. The traveler who can ask, pay, and find shelter in Bengali carries "
"the road-seal in his pocket.",
},
{
"key": "work",
"name": "Bengali Work and School Sentences",
"group": "Compounded",
"ladder_rank": 4, "ladder_tier": "compounded",
"description":
"20 sentences about jobs, the office, the classroom, and learning. 1. আমি অফিসে কাজ করি। (Ami ofishe "
"kaj kori.) I work in an office. 2. সে শিক্ষক। (She shikkhok.) He is a teacher. 3. ছাত্ররা পড়ছে। "
"(Chhatrora porchhe.) The students are studying. 4. ক্লাস সকাল নয়টায়। (Klash shokal noytay.) Class is at "
"nine in the morning. 5. বই খোলো। (Boi kholo.) Open the book. 6. হোমওয়ার্ক শেষ করো। (Homework shesh "
"koro.) Finish the homework. 7. পরীক্ষা কাল। (Porikkha kal.) The exam is tomorrow. 8. আমি পাস করেছি। "
"(Ami pash korechhi.) I have passed. 9. বস মিটিং ডেকেছেন। (Bosh miting dekechhen.) The boss has called a "
"meeting. 10. বেতন মাসে দেন। (Beton mashe den.) They pay salary monthly. 11. ছুটি চাই। (Chhuti chai.) I "
"want leave. 12. কলমটা দিন। (Kolomta din.) Give the pen. 13. কম্পিউটার চালু করো। (Kompiutar chalu koro.) "
"Turn on the computer. 14. ফাইলটা পাঠাও। (Failta pathao.) Send the file. 15. আমি ইঞ্জিনিয়ার। (Ami "
"injiniar.) I am an engineer. 16. দোকানে কাজ করি। (Dokane kaj kori.) I work at a shop. 17. স্কুলে যাও। "
"(Skule jao.) Go to school. 18. শিক্ষক প্রশ্ন করলেন। (Shikkhok proshno korlen.) The teacher asked a "
"question. 19. আমরা খেলার মাঠে খেলি। (Amra khelar mathe kheli.) We play on the playground. 20. "
"পড়াশোনা মন দিয়ে করো। (Porashona mon diye koro.) Study attentively.",
"how_it_works":
"Describe your own job or school day in ten Bengali sentences using these as models. Practice the formal "
"register with workplace sentences (বস মিটিং ডেকেছেন). Drill classroom commands (বই খোলো, পড়ো, লেখো) "
"until they come without thinking.",
"key_points": [
"Workplace nouns: অফিস, বস, মিটিং, বেতন, ছুটি",
"School nouns: ক্লাস, পরীক্ষা, হোমওয়ার্ক, শিক্ষক, ছাত্র",
"Formal verb forms for the workplace: ডেকেছেন, করলেন",
"Time + -টায়: সকাল নয়টায় pins events to the clock",
"মন দিয়ে (with attention) upgrades any study sentence",
],
"requirements": [
"Describe your job or school day in ten sentences",
"Use formal forms in five workplace sentences",
"Drill classroom commands until automatic",
"Write a weekly class schedule in Bengali",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: work and school are the Signature workshops - অফিস and ক্লাস the two "
"benches where the language earns its keep. Formal verb endings are the workshop uniform: ডেকেছেন and "
"করলেন signal rank.",
},
{
"key": "health",
"name": "Bengali Health and Body Sentences",
"group": "Compounded",
"ladder_rank": 4, "ladder_tier": "compounded",
"description":
"20 sentences about body parts, symptoms, the doctor visit, and the pharmacy. 1. আমার মাথা ব্যথা করছে। "
"(Amar matha byatha korchhe.) My head aches. 2. চোখ লাল হয়েছে। (Chokh lal hoyechhe.) My eyes are red. 3. "
"হাতে ব্যথা। (Hate byatha.) My hand hurts. 4. পা মচকেছে। (Pa mochkechhe.) My leg is sprained. 5. জ্বর "
"এসেছে। (Jor eshechhe.) I have a fever. 6. কাশি হচ্ছে। (Kashi hochchhe.) I am coughing. 7. ঠান্ডা লেগেছে। "
"(Thanda legechhe.) I have caught a cold. 8. পেট ব্যথা করছে। (Pet byatha korchhe.) My stomach aches. 9. "
"ডাক্তার দেখান। (Daktar dekhan.) See a doctor. 10. ওষুধ খাও। (Oshudh khao.) Take the medicine. 11. "
"ফার্মেসি কোথায়? (Farmesi kothay?) Where is the pharmacy? 12. বিশ্রাম নাও। (Bishram nao.) Take rest. 13. "
"পানি বেশি খাও। (Pani beshi khao.) Drink more water. 14. রক্তচাপ মাপুন। (Roktochap mapun.) Measure the "
"blood pressure. 15. হাসপাতালে যান। (Hashpatale jan.) Go to the hospital. 16. আমি সুস্থ আছি। (Ami "
"shustho achhi.) I am healthy. 17. ব্যায়াম করো। (Byayam koro.) Exercise. 18. দাঁত ব্যথা করছে। (Dant "
"byatha korchhe.) My tooth aches. 19. চশমা পরো। (Choshma poro.) Wear glasses. 20. তাড়াতাড়ি সুস্থ হও। "
"(Taratari shustho how.) Get well soon.",
"how_it_works":
"Point to each body part saying its name: মাথা চোখ নাক কান মুখ হাত পা. Then practice the symptom pattern "
"X ব্যথা করছে with five body parts. Role-play a doctor visit: describe symptoms, hear ওষুধ খাও and "
"বিশ্রাম নাও, and repeat them back.",
"key_points": [
"ব্যথা করছে = hurts/aches: attach to any body part",
"এসেছে/লেগেছে/হয়েছে: fever comes, cold catches, eyes become red",
"Doctor chain: ডাক্তার দেখান -> ওষুধ খাও -> বিশ্রাম নাও",
"ফার্মেসি কোথায় and হাসপাতালে যান are emergency tools",
"তাড়াতাড়ি সুস্থ হও: the kind farewell to the sick",
],
"requirements": [
"Name ten body parts pointing at yourself",
"Build five X ব্যথা করছে sentences",
"Role-play a full doctor visit in Bengali",
"Write three health-advice sentences",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: health sentences are the Signature body-chart - every ache sealed to "
"its true location, every remedy a stamped instruction. ব্যথা করছে is the diagnostic seal the doctor "
"reads first.",
},
{
"key": "emotions",
"name": "Bengali Emotions and Feelings Sentences",
"group": "Compounded",
"ladder_rank": 5, "ladder_tier": "compounded",
"description":
"20 sentences covering happy, sad, angry, afraid, love, and surprise. 1. আমি খুব খুশি। (Ami khub khushi.) "
"I am very happy. 2. সে দুঃখিত। (She dukkhito.) He is sad. 3. রাগ কোরো না। (Rag koro na.) Do not be "
"angry. 4. আমি ভয় পাচ্ছি। (Ami bhoy pachchhi.) I am afraid. 5. তাকে ভালোবাসি। (Take bhalobashi.) I love "
"him/her. 6. অবাক হলাম। (Obak holam.) I was surprised. 7. চিন্তা কোরো না। (Chinta koro na.) Do not worry. "
"8. আমি ক্লান্ত। (Ami klanto.) I am tired. 9. মন খারাপ। (Mon kharap.) I feel down. 10. আনন্দে নাচছে। "
"(Anonde nachchhe.) He is dancing with joy. 11. হাসি পাচ্ছে। (Hashi pachchhe.) I feel like laughing. 12. "
"কান্না পাচ্ছে। (Kanna pachchhe.) I feel like crying. 13. লজ্জা পেলাম। (Lojja pelam.) I felt shy. 14. "
"গর্বিত বোধ করছি। (Gorbito bodh korchhi.) I feel proud. 15. শান্ত থাকো। (Shanto thako.) Stay calm. 16. "
"উৎসাহিত হলাম। (Utshahito holam.) I felt encouraged. 17. হতাশ হয়ো না। (Hotash hoyo na.) Do not be "
"disappointed. 18. কৃতজ্ঞ আছি। (Kritoggo achhi.) I am grateful. 19. ঈর্ষা কোরো না। (Irsha koro na.) Do not "
"be jealous. 20. ভালোবাসা সুন্দর। (Bhalobasha shundor.) Love is beautiful.",
"how_it_works":
"Feelings are learned through the face: say each sentence in a mirror matching the expression. Pair "
"opposites: খুশি/দুঃখিত, হাসি/কান্না. Keep a one-line Bengali feeling diary for a week: আজ আমি খুশি "
"কারণ...",
"key_points": [
"খুশি দুঃখিত রাগ ভয় ভালোবাসা অবাক: the big six",
"পাচ্ছি pattern: হাসি পাচ্ছে, কান্না পাচ্ছে, ভয় পাচ্ছি",
"কোরো না gives gentle negative advice: রাগ কোরো না, চিন্তা কোরো না",
"মন খারাপ: the everyday phrase for feeling down",
"Diary practice turns feelings into fluent sentences",
],
"requirements": [
"Say each sentence in a mirror with matching expression",
"Keep a one-line Bengali feeling diary for a week",
"Drill the পাচ্ছি pattern with five new feelings",
"Comfort a friend in Bengali using চিন্তা কোরো না",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: emotions are the Signature weather-seals of the heart - খুশি the sun "
"seal, দুঃখিত the rain seal, ভালোবাসা the master seal over all. The learner presses each honestly; a "
"forged feeling-seal fools no one.",
},
{
"key": "nature",
"name": "Bengali Nature and Weather Sentences",
"group": "Compounded",
"ladder_rank": 5, "ladder_tier": "compounded",
"description":
"20 sentences about animals, plants, seasons, and weather talk. 1. আকাশ নীল। (Akash nil.) The sky is "
"blue. 2. সূর্য উঠেছে। (Shurjo uthechhe.) The sun has risen. 3. চাঁদ সুন্দর। (Chand shundor.) The moon is "
"beautiful. 4. তারা জ্বলছে। (Tara jolchhe.) The stars are shining. 5. বৃষ্টি হচ্ছে। (Brishti hochchhe.) It "
"is raining. 6. বাতাস বইছে। (Batash boichhe.) The wind is blowing. 7. গাছে পাখি বসেছে। (Gachhe pakhi "
"boshechhe.) A bird sits on the tree. 8. নদীতে মাছ আছে। (Nodite machh achhe.) There are fish in the river. "
"9. বনে বাঘ থাকে। (Bone bagh thake.) Tigers live in the forest. 10. ফুল ফুটেছে। (Phul phutechhe.) Flowers "
"have bloomed. 11. পাহাড় উঁচু। (Pahar unchu.) The mountain is high. 12. সমুদ্র বিশাল। (Shomudro bishal.) "
"The sea is vast. 13. শীতকালে ঠান্ডা পড়ে। (Shitkale thanda pore.) It gets cold in winter. 14. গ্রীষ্মে "
"গরম পড়ে। (Grishme gorom pore.) It gets hot in summer. 15. বর্ষায় বন্যা হয়। (Borshay bonna hoy.) There "
"are floods in the monsoon. 16. বসন্তে কোকিল ডাকে। (Boshonte kokil dake.) The cuckoo calls in spring. 17. "
"গরু মাঠে ঘাস খায়। (Goru mathe ghash khay.) The cow eats grass in the field. 18. বিড়াল দুধ খায়। (Biral "
"dudh khay.) The cat drinks milk. 19. কুকুর ঘেউ ঘেউ করে। (Kukur gheu gheu kore.) The dog barks. 20. "
"প্রজাপতি উড়ছে। (Projapoti urchhe.) The butterfly is flying.",
"how_it_works":
"Weather talk is daily small talk: start every day by announcing the sky in Bengali. Walk outside naming "
"ten things you see: গাছ ফুল পাখি আকাশ. Learn the six seasons with their signature event: বর্ষায় বৃষ্টি, "
"বসন্তে কোকিল.",
"key_points": [
"Weather verbs: বৃষ্টি হচ্ছে, বাতাস বইছে, ঠান্ডা পড়ে",
"Six seasons: গ্রীষ্ম বর্ষা শরৎ হেমন্ত শীত বসন্ত",
"Animal sounds and habits: কুকুর ঘেউ ঘেউ করে, কোকিল ডাকে",
"Sky set: আকাশ সূর্য চাঁদ তারা",
"-তে location: নদীতে, বনে, মাঠে, গাছে",
],
"requirements": [
"Announce the weather in Bengali every morning",
"Name ten outdoor things on a walk",
"Describe each season in one sentence",
"Write a five-sentence nature walk description",
],
"standards": STD_CORE,
"citations": [CIT_RAD, CIT_ETH],
"sig_lens":
"Signature original interpretation: nature sentences are the Signature landscape-seals - sky, river, "
"forest, and field each pressed in true color. বর্ষা the monsoon seal is the mightiest: it commands the "
"whole Bengali year.",
},
{
"key": "shopping",
"name": "Bengali Shopping and Money Sentences",
"group": "Compounded",
"ladder_rank": 6, "ladder_tier": "compounded",
"description":
"20 sentences for the market, prices, bargaining, and paying. 1. বাজারে যাই। (Bajare jai.) I go to the "
"market. 2. এটার দাম কত? (Etar dam koto?) What is the price of this? 3. দাম বেশি। (Dam beshi.) The price "
"is high. 4. একটু কমান। (Ektu koman.) Reduce a little. 5. ঠিক দাম বলুন। (Thik dam bolun.) Tell the right "
"price. 6. আমি কিনবো। (Ami kinbo.) I will buy. 7. কিনবো না। (Kinbo na.) I will not buy. 8. টাকা দিন। "
"(Taka din.) Give the money. 9. খুচরা আছে? (Khuchra achhe?) Do you have change? 10. বিল দিন। (Bil din.) "
"Give the bill. 11. ছাড় আছে? (Chhar achhe?) Is there a discount? 12. জিনিসটা ভালো। (Jinis ta bhalo.) "
"The item is good. 13. অন্য রঙ দেখান। (Onno rong dekhan.) Show another color. 14. বড় সাইজ আছে? (Boro "
"saiz achhe?) Do you have a bigger size? 15. দোকান কখন খোলে? (Dokan kokhon khole?) When does the shop "
"open? 16. ব্যাংকে যাবো। (Banke jabo.) I will go to the bank. 17. টাকা জমা দিন। (Taka joma din.) Deposit "
"the money. 18. এটিএম কোথায়? (ATM kothay?) Where is the ATM? 19. কার্ডে পেমেন্ট করবো। (Karde pement "
"korbo.) I will pay by card. 20. রসিদটা রাখুন। (Roshidta rakhun.) Keep the receipt.",
"how_it_works":
"Bargaining is a scripted dance - memorize the sequence: দাম কত -> দাম বেশি -> একটু কমান -> ঠিক দাম বলুন "
"-> কিনবো/কিনবো না. Role-play both shopkeeper and customer. Practice numbers 1-100 with টাকা until prices "
"come fast.",
"key_points": [
"Bargain chain: দাম কত, দাম বেশি, একটু কমান, ঠিক দাম বলুন",
"কিনবো vs কিনবো না: the walk-away seal that wins bargains",
"খুচরা (change) and ছাড় (discount) complete the money set",
"Formal -ন endings with shopkeepers: কমান, বলুন, দেখান",
"রসিদটা রাখুন: always keep the receipt",
],
"requirements": [
"Role-play a full bargaining session both sides",
"Quote prices 1-1000 in Bengali without pausing",
"Practice the bargain chain until fluent",
"Write a market shopping list in Bengali",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: shopping sentences are the Signature trade-seals - দাম কত the opening "
"bid, একটু কমান the counter-seal, কিনবো না the walk-away that seals the deal. Every taka is counted in "
"the open.",
},
{
"key": "friendship",
"name": "Bengali Friendship and Social Life Sentences",
"group": "Compounded",
"ladder_rank": 6, "ladder_tier": "compounded",
"description":
"20 sentences for meeting people, invitations, and celebrations. 1. আমার অনেক বন্ধু আছে। (Amar onek "
"bondhu achhe.) I have many friends. 2. চলো, বেড়াতে যাই। (Cholo, berate jai.) Come, let us go out. 3. "
"তোমাকে দাওয়াত দিলাম। (Tomake dawat dilam.) I invited you. 4. জন্মদিনে এসো। (Jonmodine esho.) Come on "
"the birthday. 5. উপহারটা নাও। (Upoharta nao.) Take the gift. 6. অনেকদিন পর দেখা। (Onekdin por dekha.) "
"Long time no see. 7. কেমন কাটছে? (Kemon katchhe?) How is it going? 8. বসো, চা খাও। (Bosho, cha khao.) "
"Sit, have tea. 9. গল্প করি। (Golpo kori.) Let us chat. 10. একসাথে ছবি তুলি। (Ekshathe chhobi tuli.) Let "
"us take a photo together. 11. তোমার সাথে দেখা করে ভালো লাগলো। (Tomar shathe dekha kore bhalo laglo.) "
"Nice to meet you. 12. ফোন নম্বরটা দাও। (Phon nomborta dao.) Give your phone number. 13. আবার দেখা হবে। "
"(Abar dekha hobe.) We will meet again. 14. শুভেচ্ছা রইলো। (Shubhechchha roilo.) Best wishes. 15. "
"অভিনন্দন! (Obhinondon!) Congratulations! 16. বিয়েতে এসো। (Biyete esho.) Come to the wedding. 17. উৎসবে "
"মজা করি। (Utshobe moja kori.) Let us have fun at the festival. 18. বন্ধুত্ব চিরকাল। (Bondhutto "
"chirokal.) Friendship forever. 19. তুমি আমার প্রিয় বন্ধু। (Tumi amar priyo bondhu.) You are my dear "
"friend. 20. বিদায়, ভালো থেকো। (Biday, bhalo theko.) Goodbye, stay well.",
"how_it_works":
"Social Bengali is warm and direct: invite, insist, celebrate. Practice the invitation set (দাওয়াত "
"দিলাম, এসো, বসো চা খাও) until offering feels natural. Learn the celebration words (অভিনন্দন, শুভেচ্ছা) "
"and use them on real occasions.",
"key_points": [
"বসো, চা খাও: hospitality in three words",
"Invitation verbs: দাওয়াত দিলাম, এসো, চলো",
"Celebration set: অভিনন্দন, শুভেচ্ছা, শুভ জন্মদিন",
"ভালো থেকো: the warm goodbye between friends",
"চলো + verb invites joint action: চলো বেড়াতে যাই",
],
"requirements": [
"Invite a friend to something in Bengali",
"Use three celebration words on real occasions",
"Practice hospitality lines until natural",
"Write a Bengali invitation message",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: friendship sentences are the Signature bond-seals - দাওয়াত the "
"invitation seal, বসো চা খাও the hospitality seal, বন্ধুত্ব চিরকাল the forever seal. Pressed warmly, "
"they bind people.",
},
{
"key": "technology",
"name": "Bengali Technology and Communication Sentences",
"group": "Compounded",
"ladder_rank": 6, "ladder_tier": "compounded",
"description":
"20 sentences about the phone, internet, computer, and messaging. 1. ফোনটা চার্জে দাও। (Phonta charge "
"dao.) Put the phone on charge. 2. ইন্টারনেট চলছে না। (Internet cholchhe na.) The internet is not working. "
"3. ওয়াইফাই পাসওয়ার্ড কী? (Waifai pashword ki?) What is the Wi-Fi password? 4. মেসেজ পাঠাও। (Mesej "
"pathao.) Send a message. 5. কল করো। (Kol koro.) Make a call. 6. ভিডিও কল করি। (Vidio kol kori.) Let us "
"video call. 7. ছবি তোলো। (Chhobi tolo.) Take a photo. 8. কম্পিউটার চালু করো। (Kompiutar chalu koro.) Turn "
"on the computer. 9. ইমেইল পাঠিয়েছি। (Email pathiyechhi.) I have sent an email. 10. অ্যাপটা ডাউনলোড "
"করো। (Apta download koro.) Download the app. 11. পাসওয়ার্ড ভুলে গেছি। (Pashword bhule gechhi.) I forgot "
"the password. 12. স্ক্রিন ভেঙে গেছে। (Skrin bhenge gechhe.) The screen is broken. 13. ব্যাটারি শেষ। "
"(Byatari shesh.) The battery is dead. 14. চার্জারটা দাও। (Charjarta dao.) Give the charger. 15. অনলাইনে "
"কেনাকাটা করি। (Online kenakata kori.) I shop online. 16. ভিডিওটা দেখো। (Vidiota dekho.) Watch the video. "
"17. গানটা ডাউনলোড করো। (Ganta download koro.) Download the song. 18. প্রিন্ট করো। (Print koro.) Print it. "
"19. ফাইলটা সেভ করো। (Failta sev koro.) Save the file. 20. কম্পিউটার বন্ধ করো। (Kompiutar bondho koro.) "
"Turn off the computer.",
"how_it_works":
"Change your phone language to Bengali for a week and narrate every tech action: মেসেজ পাঠাচ্ছি, ছবি "
"তুলছি. The loanwords (ইন্টারনেট, পাসওয়ার্ড, ডাউনলোড) are already familiar - anchor the Bengali verbs "
"around them.",
"key_points": [
"Tech loanwords stay: ইন্টারনেট, পাসওয়ার্ড, ডাউনলোড, অ্যাপ",
"করো builds commands: কল করো, প্রিন্ট করো, সেভ করো",
"চালু/বন্ধ: on/off for every device",
"Problem set: চলছে না, ভেঙে গেছে, শেষ, ভুলে গেছি",
"পাঠাও/পাঠিয়েছি: send / have sent",
],
"requirements": [
"Set phone language to Bengali for one week",
"Narrate every tech action in Bengali",
"Give five tech commands to a partner",
"Write tech troubleshooting steps in Bengali",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: technology sentences are the Signature circuit-seals - চালু the power "
"seal, বন্ধ the sleep seal, পাঠাও the transmit seal. The modern tongue solders Bengali verbs onto world "
"loanwords without losing the seal.",
},
{
"key": "tenses",
"name": "Bengali Verb Tenses in Sentences",
"group": "Compounded",
"ladder_rank": 6, "ladder_tier": "compounded",
"description":
"Present, past, future, and continuous with the verb খাওয়া (eat) and করা (do), five sentences per tense. "
"Present (I/you/he/formal): আমি খাই। (Ami khai.) I eat. তুমি খাও। (Tumi khao.) You eat. সে খায়। (She "
"khay.) He eats. আপনি খান। (Apni khan.) You eat, formal. Sentences: আমি ভাত খাই। (Ami bhat khai.) I eat "
"rice. তুমি বই পড়ো। (Tumi boi poro.) You read books. সে স্কুলে যায়। (She skule jay.) He goes to school. "
"আপনি কোথায় থাকেন? (Apni kothay thaken?) Where do you live? আমরা বাংলা শিখি। (Amra Bangla shikhi.) We "
"learn Bengali. Past: আমি খেলাম। (Ami khelam.) I ate. তুমি খেলে। (Tumi khele.) You ate. সে খেল। (She "
"khelo.) He ate. আপনি খেলেন। (Apni khelen.) You ate, formal. Sentences: আমি ভাত খেলাম। (Ami bhat khelam.) "
"I ate rice. তুমি কাল এসেছিলে। (Tumi kal eshechhile.) You came yesterday. সে বই পড়লো। (She boi porlo.) He "
"read the book. আপনি কী বললেন? (Apni ki bollen?) What did you say? আমরা খেললাম। (Amra khellam.) We "
"played. Future: আমি খাবো। (Ami khabo.) I will eat. তুমি খাবে। (Tumi khabe.) You will eat. সে খাবে। (She "
"khabe.) He will eat. আপনি খাবেন। (Apni khaben.) You will eat, formal. Sentences: আমি কাল যাবো। (Ami kal "
"jabo.) I will go tomorrow. তুমি পাস করবে। (Tumi pash korbe.) You will pass. সে আসবে। (She ashbe.) He "
"will come. আপনি সাহায্য করবেন? (Apni shahajjo korben?) Will you help? আমরা জিতবো। (Amra jitbo.) We will "
"win. Continuous: আমি খাচ্ছি। (Ami khachchhi.) I am eating. তুমি খাচ্ছো। (Tumi khachchho.) You are eating. "
"সে খাচ্ছে। (She khachchhe.) He is eating. আপনি খাচ্ছেন। (Apni khachchhen.) You are eating, formal. "
"Sentences: আমি পড়ছি। (Ami porchhi.) I am reading. তুমি কী করছো? (Tumi ki korchho?) What are you doing? "
"সে ঘুমাচ্ছে। (She ghumachchhe.) He is sleeping. আপনি শুনছেন? (Apni shunchhen?) Are you listening? মা "
"রান্না করছেন। (Ma ranna korchhen.) Mother is cooking.",
"how_it_works":
"Take one verb (খাওয়া) and march it through all four tenses aloud: খাই খেলাম খাবো খাচ্ছি. Then do করা: "
"করি করলাম করবো করছি. Build a tense grid on paper with আমি তুমি সে আপনি rows and present/past/future "
"columns, and fill it for five verbs from memory.",
"key_points": [
"Present: খাই খাও খায় খান - the -ই -ও -য় -ন ladder",
"Past: খেলাম খেলে খেল/খেলো খেলেন - the -লাম -লে -ল -লেন ladder",
"Future: খাবো খাবে খাবে খাবেন - the -বো -বে -বে -বেন ladder",
"Continuous: -ছি -ছো -ছে -ছেন on the stem",
"Formal আপনি always takes -ন/-েন endings",
],
"requirements": [
"March খাওয়া and করা through all tenses aloud",
"Fill a tense grid for five verbs from memory",
"Write five sentences per tense about your day",
"Convert ten present sentences to past and future",
],
"standards": STD_CORE,
"citations": [CIT_CHAT, CIT_RAD],
"sig_lens":
"Signature original interpretation: tenses are the Signature time-seals - present the now-seal, past the "
"done-seal, future the will-seal, continuous the still-seal. Four impressions of the same verb, each "
"dated and signed by its ending.",
},
{
"key": "qa",
"name": "Bengali Questions and Answers",
"group": "Compounded",
"ladder_rank": 6, "ladder_tier": "compounded",
"description":
"20 question-and-answer pairs covering who, what, where, when, why, and how. 1. তোমার নাম কী? - আমার "
"নাম রহিম। (Tomar nam ki? - Amar nam Rohim.) What is your name? - My name is Rahim. 2. তুমি কোথায় থাকো? "
"- আমি ঢাকায় থাকি। (Tumi kothay thako? - Ami Dhakay thaki.) Where do you live? - I live in Dhaka. 3. "
"এটা কী? - এটা বই। (Eta ki? - Eta boi.) What is this? - This is a book. 4. কে আসছে? - আমার বন্ধু আসছে। "
"(Ke ashchhe? - Amar bondhu ashchhe.) Who is coming? - My friend is coming. 5. কখন যাবে? - কাল যাবো। "
"(Kokhon jabe? - Kal jabo.) When will you go? - I will go tomorrow. 6. কেন কাঁদছো? - মন খারাপ। (Keno "
"kandchho? - Mon kharap.) Why are you crying? - I feel sad. 7. কেমন আছো? - ভালো আছি। (Kemon achho? - "
"Bhalo achhi.) How are you? - I am well. 8. কত টাকা? - পঞ্চাশ টাকা। (Koto taka? - Ponchash taka.) How "
"much? - Fifty taka. 9. কোথায় যাচ্ছো? - বাজারে যাচ্ছি। (Kothay jachchho? - Bajare jachchhi.) Where are "
"you going? - I am going to the market. 10. তুমি কি ছাত্র? - হ্যাঁ, আমি ছাত্র। (Tumi ki chhatro? - Hya, "
"ami chhatro.) Are you a student? - Yes, I am a student. 11. বাংলা জানো? - একটু জানি। (Bangla jano? - "
"Ektu jani.) Do you know Bengali? - I know a little. 12. বয়স কত? - আমার বয়স বিশ। (Boyosh koto? - Amar "
"boyosh bish.) How old are you? - I am twenty. 13. কী খাবে? - ভাত খাবো। (Ki khabe? - Bhat khabo.) What "
"will you eat? - I will eat rice. 14. কবে আসবে? - শুক্রবার আসবো। (Kobe ashbe? - Shukrobar ashbo.) When "
"will you come? - I will come Friday. 15. এটা কার? - এটা আমার। (Eta kar? - Eta amar.) Whose is this? - "
"This is mine. 16. কোনটা ভালো? - লালটা ভালো। (Konta bhalo? - Lalta bhalo.) Which is good? - The red one "
"is good. 17. কয়টা বাজে? - তিনটা বাজে। (Koyta baje? - Tinta baje.) What time is it? - It is three "
"o'clock. 18. তুমি কি যাবে? - হ্যাঁ, যাবো। (Tumi ki jabe? - Hya, jabo.) Will you go? - Yes, I will go. "
"19. কেন দেরি? - ট্রাফিক ছিল। (Keno deri? - Trafik chhilo.) Why late? - There was traffic. 20. কী করছো? "
"- বই পড়ছি। (Ki korchho? - Boi porchhi.) What are you doing? - I am reading a book.",
"how_it_works":
"Questions are the fastest path to conversation. Learn the six question words (কে কী কোথায় কখন কেন "
"কেমন) then practice the yes/no কি pattern. Do timed Q&A with a partner: they ask from this list, you "
"answer, then swap. Speed matters more than perfection.",
"key_points": [
"কে কী কোথায় কখন কেন কেমন: the six keys that open any conversation",
"কত asks price and quantity; কোন asks which; কার asks whose",
"কি at the end turns a statement into a yes/no question",
"Answers mirror the question's verb: যাবে -> যাবো",
"হ্যাঁ/না plus a short answer is always enough",
],
"requirements": [
"Memorize the six question words with examples",
"Do timed Q&A drills with a partner",
"Answer all 20 questions about yourself aloud",
"Ask five strangers-or-friends real questions in Bengali",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: questions are the Signature pick-locks - কে কী কোথায় কখন কেন কেমন "
"six master keys, কি the skeleton key for yes and no. Every answer given is a door sealed open.",
},
]

ENTRIES += [
{
"key": "commands",
"name": "Bengali Commands and Requests",
"group": "Compounded",
"ladder_rank": 6, "ladder_tier": "compounded",
"description":
"20 imperative and polite-request sentences, each in familiar and formal form. 1. বসো। / বসুন। (Bosho. / "
"Boshun.) Sit. / Sit, formal. 2. এসো। / আসুন। (Esho. / Ashun.) Come. / Come, formal. 3. যাও। / যান। "
"(Jao. / Jan.) Go. / Go, formal. 4. খাও। / খান। (Khao. / Khan.) Eat. / Eat, formal. 5. পড়ো। / পড়ুন। "
"(Poro. / Porun.) Read. / Read, formal. 6. লেখো। / লিখুন। (Lekho. / Likhun.) Write. / Write, formal. 7. "
"দাঁড়াও। / দাঁড়ান। (Darao. / Daran.) Stop. / Stop, formal. 8. চুপ করো। / চুপ করুন। (Chup koro. / Chup "
"korun.) Be quiet. / Be quiet, formal. 9. দরজা খোলো। / দরজা খুলুন। (Dorja kholo. / Dorja khulun.) Open the "
"door. / Open the door, formal. 10. জানালা বন্ধ করো। / জানালা বন্ধ করুন। (Janala bondho koro. / Janala "
"bondho korun.) Close the window. / Close the window, formal. 11. আমাকে সাহায্য করো। / আমাকে সাহায্য "
"করুন। (Amake shahajjo koro. / Amake shahajjo korun.) Help me. / Help me, formal. 12. একটু অপেক্ষা করো। / "
"একটু অপেক্ষা করুন। (Ektu opekkha koro. / Ektu opekkha korun.) Wait a little. / Wait a little, formal. 13. "
"তাড়াতাড়ি এসো। / তাড়াতাড়ি আসুন। (Taratari esho. / Taratari ashun.) Come quickly. / Come quickly, "
"formal. 14. এদিকে এসো। / এদিকে আসুন। (Edike esho. / Edike ashun.) Come here. / Come here, formal. 15. "
"ওটা দাও। / ওটা দিন। (Ota dao. / Ota din.) Give that. / Give that, formal. 16. মন দিয়ে শোনো। / মন দিয়ে "
"শুনুন। (Mon diye shono. / Mon diye shunun.) Listen carefully. / Listen carefully, formal. 17. আস্তে বলো। "
"/ আস্তে বলুন। (Aste bolo. / Aste bolun.) Speak slowly. / Speak slowly, formal. 18. ভেতরে এসো। / ভেতরে "
"আসুন। (Bhetore esho. / Bhetore ashun.) Come inside. / Come inside, formal. 19. বাইরে যাও। / বাইরে যান। "
"(Baire jao. / Baire jan.) Go outside. / Go outside, formal. 20. ভালো থেকো। / ভালো থাকুন। (Bhalo theko. / "
"Bhalo thakun.) Stay well. / Stay well, formal. Polite requests add দয়া করে at the front: দয়া করে "
"বসুন। (Doya kore boshun.) Please sit down.",
"how_it_works":
"Commands are the muscle of daily Bengali. Drill the pairs side by side until the -o/-un switch is "
"instant. Practice giving five commands to family (familiar) and five to a respected elder (formal). "
"Soften any command with দয়া করে to make it a request.",
"key_points": [
"Familiar imperatives end in -o: বসো, এসো, খাও, পড়ো",
"Formal imperatives end in -un/-n: বসুন, আসুন, খান, পড়ুন",
"দয়া করে + formal command = polite request",
"Negative commands: কোরো না / করবেন না",
"ভালো থেকো/থাকুন: the kindest command of all",
],
"requirements": [
"Drill all 20 pairs until the switch is instant",
"Give five familiar and five formal commands aloud",
"Soften ten commands with দয়া করে",
"Write five polite requests for real situations",
],
"standards": STD_CORE,
"citations": [CIT_RAD, CIT_CHAT],
"sig_lens":
"Signature original interpretation: commands are the Signature order-seals - বসো the familiar stamp, "
"বসুন the formal stamp, দয়া করে the velvet pad that softens the impression. Right seal, right person, "
"every time.",
},
{
"key": "descriptions",
"name": "Bengali Descriptions of People and Places",
"group": "Compounded",
"ladder_rank": 6, "ladder_tier": "compounded",
"description":
"20 sentences describing people, places, and things in detail. 1. রহিম লম্বা ও সুদর্শন ছেলে। (Rohim lomba "
"o shudorshon chhele.) Rahim is a tall and handsome boy. 2. তার চোখ কালো। (Tar chokh kalo.) His eyes are "
"black. 3. মেয়েটার চুল লম্বা। (Meyetar chul lomba.) The girl's hair is long. 4. ঢাকা বড় শহর। (Dhaka boro "
"shohor.) Dhaka is a big city. 5. পদ্মা বিশাল নদী। (Podda bishal nodi.) The Padma is a vast river. 6. "
"সুন্দরবন ঘন বন। (Shundorbon ghono bon.) The Sundarbans is a dense forest. 7. বাড়িটা পুরনো কিন্তু সুন্দর। "
"(Barita purono kintu shundor.) The house is old but beautiful. 8. বইটা মোটা ও ভারী। (Boita mota o bhari.) "
"The book is thick and heavy. 9. চাটা গরম ও মিষ্টি। (Chata gorom o mishti.) The tea is hot and sweet. 10. "
"আকাশ পরিষ্কার ও নীল। (Akash porishkar o nil.) The sky is clear and blue. 11. রাতটা শান্ত ও ঠান্ডা। "
"(Ratta shanto o thanda.) The night is calm and cold. 12. বাজারটা ভিড় ও কোলাহলপূর্ণ। (Bajarta bhir o "
"kolaholpurno.) The market is crowded and noisy. 13. গ্রামটা সবুজ ও শান্ত। (Gramta shobuj o shanto.) The "
"village is green and peaceful. 14. শিক্ষক কঠোর কিন্তু ন্যায়পরায়ণ। (Shikkhok kothor kintu nyayporayon.) "
"The teacher is strict but just. 15. শিশুটি চঞ্চল ও হাসিখুশি। (Shishuti chonchol o hashikhushi.) The "
"child is lively and cheerful. 16. পাহাড়টা উঁচু ও বরফে ঢাকা। (Paharta unchu o borofe dhaka.) The mountain "
"is high and snow-covered. 17. ফুলগুলো রঙিন ও সুগন্ধি। (Phulgulo rongin o shugondhi.) The flowers are "
"colorful and fragrant. 18. নদীর জল স্বচ্ছ। (Nodir jol swochchho.) The river water is clear. 19. রাস্তাটা "
"চওড়া ও পরিষ্কার। (Rastata chowra o porishkar.) The road is wide and clean. 20. সন্ধ্যাটা মনোরম। "
"(Shondhata monorom.) The evening is pleasant.",
"how_it_works":
"Description stacks adjectives: learn the X ও Y pattern (লম্বা ও সুদর্শন) and the X কিন্তু Y pattern "
"(পুরনো কিন্তু সুন্দর). Describe five people and five places you know, each with two adjectives. Add a "
"কিন্তু twist to three of them.",
"key_points": [
"ও joins matching adjectives: লম্বা ও সুদর্শন",
"কিন্তু adds contrast: পুরনো কিন্তু সুন্দর",
"তার/মেয়েটার + noun: possession in descriptions",
"Place descriptions use -টা: বাজারটা, গ্রামটা, রাতটা",
"Two adjectives per sentence is the fluency target",
],
"requirements": [
"Describe five people with two adjectives each",
"Describe five places with two adjectives each",
"Use কিন্তু in three contrast sentences",
"Write a ten-sentence portrait of your town",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: descriptions are the Signature portrait-seals - two adjectives pressed "
"side by side, ও the joining wax, কিন্তু the chisel that carves contrast. A true portrait needs both.",
},
{
"key": "story1",
"name": "Bengali Story I: A Day in the Village",
"group": "Advanced",
"ladder_rank": 7, "ladder_tier": "advanced",
"description":
"A 10-sentence simple story in the present tense, line by line with English. 1. সকালে সূর্য ওঠে। "
"(Shokale shurjo othe.) In the morning the sun rises. 2. রহিম ঘুম থেকে ওঠে। (Rohim ghum theke othe.) "
"Rahim wakes up from sleep. 3. সে মুখ ধোয়। (She mukh dhoy.) He washes his face. 4. মা নাস্তা বানান। (Ma "
"nasta banan.) Mother makes breakfast. 5. রহিম স্কুলে যায়। (Rohim skule jay.) Rahim goes to school. 6. "
"স্কুলে সে পড়ে ও খেলে। (Skule she pore o khele.) At school he studies and plays. 7. দুপুরে সে বাড়ি "
"ফেরে। (Dupure she bari phere.) At noon he returns home. 8. বিকেলে সে মাঠে খেলে। (Bikele she mathe "
"khele.) In the afternoon he plays in the field. 9. সন্ধ্যায় সে পড়তে বসে। (Shondhay she porte boshe.) "
"In the evening he sits down to study. 10. রাতে সে তাড়াতাড়ি ঘুমায়। (Rate she taratari ghumay.) At "
"night he sleeps early. The story uses only present-tense verbs and the time words সকালে দুপুরে বিকেলে "
"সন্ধ্যায় রাতে. Notice the day arc: waking, school, play, study, sleep - the same arc as your own day.",
"how_it_works":
"Read the story aloud twice, then retell it without looking - first in English, then in Bengali. Replace "
"রহিম with your own name and retell your own day following the same ten-step arc. This is how stories "
"become yours.",
"key_points": [
"Ten sentences, all present tense - the simplest story engine",
"Time words frame each step: সকালে, দুপুরে, বিকেলে, সন্ধ্যায়, রাতে",
"Day arc: wake -> school -> play -> study -> sleep",
"Retelling without looking builds narrative memory",
"Personalize: swap রহিম for your name",
],
"requirements": [
"Read the story aloud twice",
"Retell it in English, then in Bengali, without looking",
"Retell your own day on the same ten-step arc",
"Write a new ten-sentence present-tense story",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: the first story is the Signature day-seal - ten impressions from "
"sunrise to sleep, each hour stamped in the present tense. The learner who can seal his own day in "
"Bengali owns the present.",
},
{
"key": "story2",
"name": "Bengali Story II: The River Journey",
"group": "Advanced",
"ladder_rank": 7, "ladder_tier": "advanced",
"description":
"A 10-sentence story in the past tense, line by line with English. 1. গতকাল আমরা নদীতে গিয়েছিলাম। "
"(Gotokal amra nodite giyechhilam.) Yesterday we went to the river. 2. নৌকা ঘাটে অপেক্ষা করছিল। (Nouka "
"ghate opekkha korchhilo.) The boat was waiting at the pier. 3. আমরা নৌকায় উঠলাম। (Amra noukay uthlam.) "
"We got on the boat. 4. মাঝি নৌকা চালালো। (Majhi nouka chalalo.) The boatman rowed the boat. 5. নদীর জল "
"স্বচ্ছ ছিল। (Nodir jol swochchho chhilo.) The river water was clear. 6. আকাশে সাদা মেঘ ভাসছিল। (Akashe "
"shada megh bhashchhilo.) White clouds floated in the sky. 7. আমরা গান গাইলাম। (Amra gan gailam.) We sang "
"songs. 8. দুপুরে আমরা তীরে নামলাম। (Dupure amra tire namlam.) At noon we got down on the bank. 9. মা "
"খাবার বের করলেন। (Ma khabar ber korlen.) Mother took out the food. 10. সন্ধ্যায় আমরা খুশি মনে বাড়ি "
"ফিরলাম। (Shondhay amra khushi mone bari phirlam.) In the evening we returned home happily. Past forms "
"used: গিয়েছিলাম (had gone), করছিল (was doing), উঠলাম (got on), চালালো (rowed), ছিল (was), ভাসছিল (was "
"floating), গাইলাম (sang), নামলাম (got down), বের করলেন (took out), ফিরলাম (returned).",
"how_it_works":
"Circle every past-tense verb and name its form (simple past -লাম, past continuous -ছিল, past perfect "
"গিয়েছিলাম). Retell the journey in the present tense, then in the future tense - the same story, three "
"time-seals. Then write your own past-tense journey.",
"key_points": [
"Simple past -লাম/-লো: উঠলাম, চালালো, গাইলাম",
"Past continuous -ছিল: অপেক্ষা করছিল, ভাসছিল",
"Past perfect গিয়েছিলাম for the earlier action",
"ছিল: the past of আছে/হয়",
"One story retold in three tenses = tense mastery",
],
"requirements": [
"Circle and name every past verb form",
"Retell the story in present and future tenses",
"Write your own ten-sentence past-tense journey",
"Tell a real memory in Bengali past tense",
],
"standards": STD_CORE,
"citations": [CIT_CHAT, CIT_RAD],
"sig_lens":
"Signature original interpretation: the river story is the Signature past-seal - the journey already "
"sailed, every oar-stroke stamped -লাম and -ছিল. The past is a sealed logbook; the learner learns to "
"read it and write his own.",
},
{
"key": "story3",
"name": "Bengali Story III: The Dream Shop",
"group": "Advanced",
"ladder_rank": 8, "ladder_tier": "advanced",
"description":
"A 10-sentence story in the future and conditional, line by line with English. 1. আমি একদিন বড় দোকান "
"খুলবো। (Ami ekdin boro dokan khulbo.) One day I will open a big shop. 2. দোকানে বই ও খেলনা থাকবে। "
"(Dokane boi o khelna thakbe.) The shop will have books and toys. 3. শিশুরা সেখানে আসবে। (Shishura "
"shekhane ashbe.) Children will come there. 4. আমি তাদের গল্প শোনাবো। (Ami tader golpo shonabo.) I will "
"tell them stories. 5. যদি বৃষ্টি হয়, আমরা ভেতরে বসবো। (Jodi brishti hoy, amra bhetore boshbo.) If it "
"rains, we will sit inside. 6. যদি রোদ ওঠে, আমরা বাগানে খেলবো। (Jodi rod othe, amra bagane khelbo.) If "
"the sun shines, we will play in the garden. 7. মা দোকানে সাহায্য করবেন। (Ma dokane shahajjo korben.) "
"Mother will help in the shop. 8. বাবা হিসাব রাখবেন। (Baba hishab rakhben.) Father will keep the "
"accounts. 9. দোকানটা শহরের সেরা হবে। (Dokanta shohorer shera hobe.) The shop will be the best in the "
"city. 10. স্বপ্ন সত্যি হলে আমি খুব খুশি হবো। (Shopno shotti hole ami khub khushi hobo.) I will be very "
"happy if the dream comes true. Future forms: খুলবো, থাকবে, আসবে, শোনাবো, বসবো, খেলবো, করবেন, রাখবেন, "
"হবে, হবো. Conditionals: যদি...হয়, ...হলে.",
"how_it_works":
"Dreams are the natural home of the future tense. Write your own dream in ten future-tense sentences: "
"আমি ... করবো. Add two যদি conditions. Read it aloud as a promise to yourself - the future tense is a "
"vow, and vows are remembered.",
"key_points": [
"Future -বো/-বে/-বেন: খুলবো, আসবে, করবেন",
"যদি + present, future result: যদি বৃষ্টি হয়, বসবো",
"...হলে conditional: স্বপ্ন সত্যি হলে",
"হবে/হবো: will be - the copula of dreams",
"Dreams make the future tense unforgettable",
],
"requirements": [
"Write your dream in ten future-tense sentences",
"Add two যদি conditions to the dream",
"Read the dream aloud as a promise",
"Convert the river story to future tense",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: the dream shop is the Signature future-seal - vows stamped -বো and "
"-বেন, conditions hinged on যদি. A dream told in the future tense is a contract with tomorrow, signed "
"in Bengali.",
},
{
"key": "idioms",
"name": "Bengali Idioms and Proverbs",
"group": "Advanced",
"ladder_rank": 8, "ladder_tier": "advanced",
"description":
"20 idioms and proverbs with literal translation, real meaning, and an example sentence. 1. অল্প বিদ্যা "
"ভয়ংকরী। (Olpo bidda bhoyongkori.) Literally: little learning is terrifying. Meaning: a little learning "
"is a dangerous thing. Example: অল্প বিদ্যা ভয়ংকরী, তাই ভালো করে পড়ো। (Olpo bidda bhoyongkori, tai bhalo "
"kore poro.) A little learning is dangerous, so study well. 2. জলে কুমির ডাঙায় বাঘ। (Jole kumir dangay "
"bagh.) Literally: crocodile in water, tiger on land. Meaning: danger on every side. Example: দুই দিকেই "
"বিপদ, জলে কুমির ডাঙায় বাঘ। (Dui dikei bipod, jole kumir dangay bagh.) Danger on both sides - crocodile "
"in water, tiger on land. 3. ঘরের শত্রু বিভীষণ। (Ghorer shotru Bibhishon.) Literally: Bibhishana is the "
"enemy of the house. Meaning: the enemy within. Example: সাবধান, ঘরের শত্রু বিভীষণ। (Shabdhan, ghorer "
"shotru Bibhishon.) Beware, the enemy is within the house. 4. দুধের সাধ ঘোলে মেটানো। (Dudher shadh ghole "
"metano.) Literally: satisfying the craving for milk with whey. Meaning: settling for a poor substitute. "
"5. নাচতে না জানলে উঠান বাঁকা। (Nachte na janle uthan banka.) Literally: if you cannot dance, the "
"courtyard is crooked. Meaning: a bad worker blames his tools. 6. অতি ভক্তি চোরের লক্ষণ। (Oti bhokti "
"chorer lokkhon.) Literally: too much devotion is the sign of a thief. Meaning: excessive flattery hides "
"a motive. 7. এক হাতে তালি বাজে না। (Ek hate tali baje na.) Literally: you cannot clap with one hand. "
"Meaning: it takes two to quarrel or to succeed together. 8. কাটা ঘায়ে নুনের ছিটা। (Kata ghaye nuner "
"chhita.) Literally: salt sprinkled on a cut wound. Meaning: adding insult to injury. 9. চোরের মার বড় "
"গলা। (Chorer mar boro gola.) Literally: the beaten thief has the loudest voice. Meaning: the guilty "
"protest the most. 10. ভাত ছড়ালে কাকের অভাব হয় না। (Bhat chhorale kaker obhab hoy na.) Literally: if you "
"scatter rice, crows will not be lacking. Meaning: generosity attracts friends. 11. কাঁচায় না নোয়ালে "
"বাঁশ, পাকলে করে ঠাস ঠাস। (Kanchay na noale bansh, pakle kore thash thash.) Literally: bend the bamboo "
"while green, or it cracks when ripe. Meaning: train children young. 12. যেমন কর্ম তেমন ফল। (Jemon kormo "
"temon phol.) Literally: as the deed, so the fruit. Meaning: you reap what you sow. 13. দাঁত থাকতে "
"দাঁতের মর্যাদা বোঝা যায় না। (Dant thakte danter morjada bojha jay na.) Literally: you do not know the "
"value of teeth while you have them. Meaning: we value things only after losing them. 14. লোভে পাপ পাপে "
"মৃত্যু। (Lobhe pap pape mrittu.) Literally: in greed is sin, in sin is death. Meaning: greed destroys. "
"15. সৎ সঙ্গে স্বর্গবাস। (Shot shonge shorgobash.) Literally: dwelling in heaven with good company. "
"Meaning: good company uplifts. 16. নিজের চরকায় তেল দাও। (Nijer chorkay tel dao.) Literally: oil your own "
"spinning wheel. Meaning: mind your own business. 17. চাঁদেও কলঙ্ক আছে। (Chadeo kolonko achhe.) "
"Literally: even the moon has spots. Meaning: nobody is perfect. 18. বনের বাঘে খায় না মনের বাঘে খায়। "
"(Boner baghe khay na moner baghe khay.) Literally: the forest tiger does not eat you, the mind's tiger "
"does. Meaning: fear itself is the killer. 19. ঢাল নেই তলোয়ার নেই নিধিরাম সর্দার। (Dhal nei toloar nei "
"Nidhiram shordar.) Literally: no shield, no sword, yet Commander Nidhiram. Meaning: empty boasting. 20. "
"মোল্লার দৌড় মসজিদ পর্যন্ত। (Mollar dour moshjid porjonto.) Literally: the mullah's run ends at the "
"mosque. Meaning: everyone has limits to their reach.",
"how_it_works":
"Idioms are cultural passwords - learn five a week and drop one into real conversation. For each, say the "
"literal image first (crocodile in water, tiger on land), then the meaning, then the example. Never "
"translate idioms word-for-word to outsiders; explain the meaning.",
"key_points": [
"20 authentic proverbs with literal image + real meaning + example",
"Nature images dominate: কুমির, বাঘ, বাঁশ, চাঁদ",
"Moral seals: যেমন কর্ম তেমন ফল, লোভে পাপ পাপে মৃত্যু",
"Use one idiom per conversation - seasoning, not the meal",
"Never translate idioms literally to non-speakers",
],
"requirements": [
"Learn five idioms per week with literal and real meanings",
"Use one idiom in real conversation each week",
"Explain three idioms to a friend in English",
"Write five original sentences using idioms",
],
"standards": STD_CORE,
"citations": [CIT_CHAT, CIT_RAD],
"sig_lens":
"Signature original interpretation: idioms are the Signature wisdom-seals - centuries of village judgment "
"pressed into one line. জলে কুমির ডাঙায় বাঘ seals a whole philosophy of danger in seven words. The "
"learner who wields them speaks with the ancestors.",
},
{
"key": "registers",
"name": "Bengali Formal and Polite Registers",
"group": "Advanced",
"ladder_rank": 8, "ladder_tier": "advanced",
"description":
"15 formal vs informal pairs for letters, business, and elders. 1. Informal: কেমন আছো? (Kemon achho?) "
"Formal: কেমন আছেন? (Kemon achhen?) How are you? 2. Informal: বসো। (Bosho.) Formal: বসুন। (Boshun.) Sit. "
"3. Informal: তোমার নাম কী? (Tomar nam ki?) Formal: আপনার নাম কী? (Apnar nam ki?) What is your name? 4. "
"Informal: ধন্যবাদ। (Dhonnobad.) Formal: আপনাকে অনেক ধন্যবাদ। (Apnake onek dhonnobad.) Thank you very "
"much. 5. Informal: চলি। (Choli.) Formal: আমি এখন আসি। (Ami ekhon ashi.) I take my leave now. 6. "
"Informal: এটা দাও। (Eta dao.) Formal: এটা দেবেন কি? (Eta deben ki?) Would you give this? 7. Informal: "
"বুঝলাম না। (Bujhlam na.) Formal: বুঝতে পারলাম না। (Bujhte parlam na.) I could not understand. 8. "
"Informal: দেরি হলো। (Deri holo.) Formal: দেরির জন্য দুঃখিত। (Derir jonno dukkhito.) Sorry for the delay. "
"9. Informal: ভালো। (Bhalo.) Formal: খুব ভালো হয়েছে। (Khub bhalo hoyechhe.) It has turned out very "
"well. 10. Informal: আসবো। (Ashbo.) Formal: অবশ্যই আসবো। (Obosshoi ashbo.) I will certainly come. 11. "
"Informal: খেয়েছো? (Kheyechho?) Formal: খেয়েছেন? (Kheyechhen?) Have you eaten? 12. Informal: কোথায় "
"যাচ্ছো? (Kothay jachchho?) Formal: কোথায় যাচ্ছেন? (Kothay jachchhen?) Where are you going? 13. "
"Informal: ফোন করো। (Phon koro.) Formal: ফোন করবেন। (Phon korben.) Please call. 14. Informal: দেখা হবে। "
"(Dekha hobe.) Formal: আবার দেখা হবে। (Abar dekha hobe.) We will meet again. 15. Informal: ঠিক আছে। "
"(Thik achhe.) Formal: ঠিক আছে, ধন্যবাদ। (Thik achhe, dhonnobad.) All right, thank you. Rules: use আপনি "
"and -ন/-েন verb endings with elders, strangers, and in business; use তুমি with peers and friends; "
"reserve তুই for the closest bonds and children. In letters, open with শ্রদ্ধেয় (shroddheyo, respected) "
"for elders and প্রিয় (priyo, dear) for friends.",
"how_it_works":
"Register mistakes are social mistakes - drill the pairs until আপনি is your default with strangers. Write "
"two short letters: one to an elder (শ্রদ্ধেয় ... দেবেন কি ... ধন্যবাদ) and one to a friend (প্রিয় ... "
"দাও ... চলি). Read both aloud and feel the distance change.",
"key_points": [
"আপনি + -ন/-েন = formal; তুমি + -ও = familiar; তুই = intimate",
"Formal softens requests: দেবেন কি instead of দাও",
"দেরির জন্য দুঃখিত: the formal apology formula",
"Letters: শ্রদ্ধেয় for elders, প্রিয় for friends",
"When unsure, go formal - respect never offends",
],
"requirements": [
"Make আপনি the default with all strangers",
"Write a formal letter and an informal letter",
"Convert ten familiar sentences to formal",
"Practice the formal apology formula aloud",
],
"standards": STD_CORE,
"citations": [CIT_RAD, CIT_CHAT],
"sig_lens":
"Signature original interpretation: registers are the Signature distance-seals - আপনি the long seal for "
"elders and strangers, তুমি the near seal for friends, তুই the skin-close seal. Pressing the wrong "
"distance breaks the social wax.",
},
{
"key": "complex",
"name": "Bengali Compound and Complex Sentences",
"group": "Advanced",
"ladder_rank": 9, "ladder_tier": "advanced",
"description":
"15 long sentences with clauses and connectors, parsed and translated. 1. আমি বাজারে গেলাম কারণ সবজি "
"দরকার ছিল। (Ami bajare gelam karon shobji dorkar chhilo.) I went to the market because vegetables were "
"needed. [কারণ = because] 2. বৃষ্টি হচ্ছিল কিন্তু আমরা বের হলাম। (Brishti hochchhilo kintu amra ber holam.) "
"It was raining but we went out. [কিন্তু = but] 3. যদি তুমি পড়ো, তুমি পাস করবে। (Jodi tumi poro, tumi "
"pash korbe.) If you study, you will pass. [যদি = if] 4. যখন সূর্য উঠলো, পাখিরা গান গাইলো। (Jokhon shurjo "
"uthlo, pakhira gan gailo.) When the sun rose, the birds sang. [যখন = when] 5. যেহেতু সে অসুস্থ, সে স্কুলে "
"যায়নি। (Jehetu she oshustho, she skule jayni.) Since he is sick, he did not go to school. [যেহেতু = "
"since] 6. সে কঠোর পরিশ্রম করলো তাই সফল হলো। (She kothor porishrom korlo tai shofol holo.) He worked hard "
"so he succeeded. [তাই = so] 7. আমি ভাত এবং ডাল খেলাম। (Ami bhat ebong dal khelam.) I ate rice and "
"lentils. [এবং = and] 8. চা অথবা কফি নাও। (Cha othoba kophi nao.) Take tea or coffee. [অথবা = or] 9. "
"তাড়াতাড়ি এসো যাতে ট্রেন না মিস হয়। (Taratari esho jate tren na mis hoy.) Come quickly so that the train "
"is not missed. [যাতে = so that] 10. যদিও সে ছোট, সে সাহসী। (Jodio she chhoto, she shahoshi.) Although he "
"is small, he is brave. [যদিও = although] 11. প্রথমে পড়ো, তারপর খেলো। (Prothome poro, tarpor khelo.) "
"First study, then play. [তারপর = then] 12. খাওয়ার আগে হাত ধোও। (Khawar age hat dhowo.) Wash your hands "
"before eating. [আগে = before] 13. স্কুলের পরে আমরা খেলি। (Skuler pore amra kheli.) After school we play. "
"[পরে = after] 14. যত পড়বে, তত জানবে। (Joto porbe, toto janbe.) The more you read, the more you will "
"know. [যত...তত = the more...the more] 15. যে ছেলেটা দৌড়াচ্ছে, সে আমার ভাই। (Je chheleta dourachchhe, "
"she amar bhai.) The boy who is running is my brother. [যে...সে = who...he, relative clause]",
"how_it_works":
"Connectors are sentence glue - learn them one at a time, building a two-clause sentence with each. Parse "
"practice: take each of the 15, draw a line under the connector, and label both clauses. Then combine "
"pairs of your own simple sentences with কারণ, কিন্তু, and যদি.",
"key_points": [
"কারণ কিন্তু যদি যখন যেহেতু তাই: the six core connectors",
"যাতে expresses purpose: so that",
"যদিও concedes: although",
"যত...তত builds comparisons: the more...the more",
"যে...সে builds relative clauses: the boy who...",
],
"requirements": [
"Build one two-clause sentence per connector",
"Parse all 15: underline connector, label clauses",
"Combine ten simple-sentence pairs with connectors",
"Write a five-sentence paragraph using three connectors",
],
"standards": STD_CORE,
"citations": [CIT_CHAT, CIT_RAD],
"sig_lens":
"Signature original interpretation: connectors are the Signature hinges - কারণ the reason-hinge, কিন্তু "
"the pivot-hinge, যদি the maybe-hinge. Simple sentences are planks; connectors hinge them into doors "
"that open onto real thought.",
},
{
"key": "market",
"name": "Bengali Conversation: At the Market",
"group": "Advanced",
"ladder_rank": 9, "ladder_tier": "advanced",
"description":
"A 20-line bilingual market dialogue, annotated. A: নমস্কার! (Nomoskar!) Hello! [greeting] B: নমস্কার! কী "
"কিনবেন? (Nomoskar! Ki kinben?) Hello! What will you buy? [formal কী + -বেন] A: তাজা মাছ আছে? (Taja "
"machh achhe?) Do you have fresh fish? [আছে = is there] B: হ্যাঁ, আজকের মাছ খুব তাজা। (Hya, ajker machh "
"khub taja.) Yes, today's fish is very fresh. [আজকের = today's] A: কেজি কত? (Keji koto?) How much per "
"kilo? [কত asks price] B: তিনশো টাকা কেজি। (Tinsho taka keji.) Three hundred taka per kilo. A: দাম বেশি। "
"দুইশো দেবো। (Dam beshi. Duisho debo.) The price is high. I will pay two hundred. [opening bargain] B: "
"দুইশোতে হবে না। আড়াইশো দিন। (Duishote hobe na. Araisho din.) Two hundred will not do. Give two hundred "
"fifty. [counter-offer] A: ঠিক আছে, আড়াইশো। এক কেজি দিন। (Thik achhe, araisho. Ek keji din.) OK, two "
"fifty. Give one kilo. [deal] B: আর কিছু লাগবে? (Ar kichhu lagbe?) Do you need anything else? [upsell] A: "
"হ্যাঁ, আধা কেজি চিংড়ি দিন। (Hya, adha keji chingri din.) Yes, give half a kilo of prawns. B: চিংড়ি "
"চারশো টাকা কেজি। (Chingri charsho taka keji.) Prawns are four hundred taka per kilo. A: ঠিক আছে, দিন। "
"(Thik achhe, din.) OK, give them. B: মোট সাড়ে চারশো টাকা। (Mot share charsho taka.) Total four hundred "
"fifty taka. [মোট = total] A: এই নিন পাঁচশো টাকা। (Ei nin pashsho taka.) Here, take five hundred taka. "
"[এই নিন = here, take] B: এই নিন পঞ্চাশ টাকা ফেরত। (Ei nin ponchash taka pherot.) Here is fifty taka "
"change. [ফেরত = change] A: ধন্যবাদ! (Dhonnobad!) Thank you! B: আবার আসবেন! (Abar ashben!) Come again! "
"[formal farewell] A: অবশ্যই আসবো। (Obosshoi ashbo.) I will surely come. B: শুভ দিন! (Shubho din!) Have "
"a good day!",
"how_it_works":
"Act out the dialogue with a partner, swapping roles. Cover the English and translate each line aloud; "
"cover the Bengali and rebuild from English. Then improvise: change the items, prices, and quantities and "
"run the bargaining scene again with your own numbers.",
"key_points": [
"Full bargain arc: greeting -> price -> haggle -> deal -> pay -> farewell",
"কেজি কত / দাম বেশি / একটু কমান: the haggling trio",
"আড়াইশো, সাড়ে চারশো: half-hundreds in real prices",
"এই নিন: the handing-over phrase",
"Formal -বেন/-ন with the shopkeeper throughout",
],
"requirements": [
"Perform the dialogue swapping roles",
"Translate each line both directions aloud",
"Improvise with new items and prices",
"Run the scene entirely from memory",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: the market dialogue is the Signature trade-contract - twenty sealed "
"lines from নমস্কার to শুভ দিন, every taka accounted, every haggle honored. Perform it and the market "
"is yours.",
},
{
"key": "friend",
"name": "Bengali Conversation: Meeting a Friend",
"group": "Advanced",
"ladder_rank": 9, "ladder_tier": "advanced",
"description":
"A 20-line bilingual reunion dialogue, annotated. A: আরে! কেমন আছো? (Are! Kemon achho?) Hey! How are "
"you? [আরে = hey, familiar] B: ভালো আছি! তুমি কেমন? (Bhalo achhi! Tumi kemon?) I am well! How are you? "
"A: আমিও ভালো। অনেকদিন পর দেখা! (Amio bhalo. Onekdin por dekha!) I am well too. Long time no see! B: "
"হ্যাঁ, প্রায় এক বছর! (Hya, pray ek bochhor!) Yes, almost a year! [প্রায় = almost] A: কোথায় ছিলে "
"এতদিন? (Kothay chhile etodin?) Where were you all this time? [past -ছিলে] B: চট্টগ্রামে ছিলাম, চাকরির "
"জন্য। (Chottograme chhilam, chakrir jonno.) I was in Chittagong, for work. [জন্য = for] A: চাকরি কেমন "
"চলছে? (Chakri kemon cholchhe?) How is the job going? B: ভালোই চলছে। তুমি কী করছো? (Bhaloi cholchhe. "
"Tumi ki korchho?) Going well. What are you doing? A: আমি এখন শিক্ষক। (Ami ekhon shikkhok.) I am a "
"teacher now. B: বাহ! অভিনন্দন! (Bah! Obhinondon!) Wow! Congratulations! [বাহ = wow] A: ধন্যবাদ! বসো, চা "
"খাও। (Dhonnobad! Bosho, cha khao.) Thanks! Sit, have tea. [hospitality] B: চলো, পার্কে হাঁটি। (Cholo, "
"parke hati.) Come, let us walk in the park. [চলো invites] A: ভালো আইডিয়া! চলো। (Bhalo aidia! Cholo.) "
"Good idea! Let us go. B: তোমার পরিবার কেমন? (Tomar poribar kemon?) How is your family? A: সবাই ভালো "
"আছে। (Shobai bhalo achhe.) Everyone is well. [সবাই = everyone] B: মাকে আমার সালাম দিও। (Make amar salam "
"dio.) Give my regards to mother. [সালাম = regards] A: অবশ্যই দেবো। (Obosshoi debo.) I surely will. B: "
"তাহলে আবার দেখা হবে! (Tahole abar dekha hobe!) Then we will meet again! A: হ্যাঁ, ফোনে কথা হবে! (Hya, "
"phone kotha hobe!) Yes, we will talk on the phone! B: বিদায়! (Biday!) Goodbye!",
"how_it_works":
"Friendship dialogue runs on তুমি - warm, familiar, fast. Practice the reunion arc: greeting -> catching "
"up -> news -> invitation -> regards -> farewell. Then call a real friend and open with আরে! কেমন আছো? "
"- the hardest line is the first one.",
"key_points": [
"তুমি register: warm and familiar throughout",
"Reunion arc: greeting -> where were you -> news -> plan -> farewell",
"চলো + verb: the joint-action invitation",
"মাকে সালাম দিও: regards to family seal the bond",
"বাহ, আরে: the interjections of real friendship",
],
"requirements": [
"Perform the dialogue with a partner",
"Practice the reunion arc from memory",
"Open a real call with আরে! কেমন আছো?",
"Write a reunion dialogue about your own friend",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: the reunion dialogue is the Signature friendship-bond - twenty lines "
"from আরে to বিদায়, sealed with চা, সালাম, and চলো. Friendship pressed in Bengali holds for years.",
},
{
"key": "problem",
"name": "Bengali Conversation: Solving a Problem",
"group": "Advanced",
"ladder_rank": 10, "ladder_tier": "advanced",
"description":
"A 20-line bilingual problem-solving dialogue (a lost phone), annotated. A: সমস্যা হয়েছে! (Shomossha "
"hoyechhe!) There is a problem! [সমস্যা = problem] B: কী হয়েছে? শান্ত হও। (Ki hoyechhe? Shanto how.) "
"What happened? Calm down. [শান্ত হও = calm down] A: আমার ফোন হারিয়ে গেছে! (Amar phon hariye gechhe!) "
"I have lost my phone! [হারিয়ে গেছে = is lost] B: কোথায় শেষ দেখেছিলে? (Kothay shesh dekhechhile?) Where "
"did you last see it? [diagnostic question] A: বাজারে, দোকানের সামনে। (Bajare, dokaner shamne.) At the "
"market, in front of the shop. B: চলো, সেখানে ফিরে যাই। (Cholo, shekhane phire jai.) Come, let us go back "
"there. [plan] A: দোকানদারকে জিজ্ঞেস করি। (Dokandarke jiggesh kori.) Let us ask the shopkeeper. B: ভাই, "
"একটা ফোন পেয়েছেন? (Bhai, ekta phon peyechhen?) Brother, did you find a phone? [formal -ছেন] C: হ্যাঁ, "
"এই নিন। টেবিলে ছিল। (Hya, ei nin. Tabile chhilo.) Yes, here. It was on the table. [resolution] A: এটাই "
"আমার ফোন! অনেক ধন্যবাদ! (Etai amar phon! Onek dhonnobad!) This is my phone! Thank you so much! C: "
"সাবধানে রাখবেন। (Shabdhane rakhben.) Keep it carefully. [advice] A: হাঁফ ছেড়ে বাঁচলাম! (Haph chhere "
"banchlam!) What a relief! [idiom of relief] B: দেখলে? শান্ত থাকলে সমস্যার সমাধান হয়। (Dekhle? Shanto "
"thakle shomosshar shomadhan hoy.) See? Staying calm solves problems. [moral] A: তুমি ঠিক বলেছো। (Tumi "
"thik bolechho.) You are right. B: এখন ফোনে পাসওয়ার্ড দাও। (Ekhon phone pashword dao.) Now put a password "
"on the phone. [prevention] A: ভালো পরামর্শ! (Bhalo poramorsho!) Good advice! B: চলো, চা খাই। (Cholo, "
"cha khai.) Come, let us have tea. [recovery ritual] A: আজকের চা আমার তরফ থেকে! (Ajker cha amar torof "
"theke!) Today the tea is on me! B: হা হা, ঠিক আছে! (Ha ha, thik achhe!) Ha ha, OK! A: বন্ধু থাকলে ভয় "
"কী! (Bondhu thakle bhoy ki!) With a friend around, what fear! [closing bond]",
"how_it_works":
"Problems follow an arc: alarm -> calm -> diagnose -> plan -> resolve -> prevent. Memorize the crisis "
"line (সমস্যা হয়েছে!) and the calming line (শান্ত হও). Then invent your own problem - a missed train, a "
"lost wallet - and solve it in 20 Bengali lines.",
"key_points": [
"Crisis arc: alarm -> calm -> diagnose -> plan -> resolve -> prevent",
"হারিয়ে গেছে: the lost-thing formula",
"শান্ত হও: first aid for panic",
"Formal -ছেন with strangers even in crisis: পেয়েছেন?",
"চা after the crisis: the recovery ritual",
],
"requirements": [
"Memorize the crisis and calming lines",
"Perform the dialogue with three roles",
"Invent and solve your own problem in 20 lines",
"Give prevention advice in Bengali",
],
"standards": STD_CORE,
"citations": [CIT_RAD],
"sig_lens":
"Signature original interpretation: the problem dialogue is the Signature rescue-seal - alarm, calm, "
"diagnosis, plan, resolution, prevention, six impressions in order. The learner who can lose and find a "
"phone in Bengali can survive anything.",
},
{
"key": "mastery",
"name": "Bengali Mastery Review and Full Reference",
"group": "Advanced",
"ladder_rank": 10, "ladder_tier": "advanced",
"description":
"The whole database in one teaching summary. Alphabet: 11 vowels অ আ ই ঈ উ ঊ ঋ এ ঐ ও ঔ; 39 consonants ক "
"খ গ ঘ ঙ চ ছ জ ঝ ঞ ট ঠ ড ঢ ণ ত থ দ ধ ন প ফ ব ভ ম য র ল শ ষ স হ ড় ঢ় য়; numerals ০-৯; danda । ends "
"sentences. 200 core words: People - মানুষ (manush) person, ছেলে (chhele) boy, মেয়ে (meye) girl, বাবা "
"(baba) father, মা (ma) mother, ভাই (bhai) brother, বোন (bon) sister, বন্ধু (bondhu) friend, শিশু (shishu) "
"child, বৃদ্ধ (briddho) old man. Home - বাড়ি (bari) house, ঘর (ghor) room, দরজা (dorja) door, জানালা "
"(janala) window, টেবিল (tabil) table, চেয়ার (cheyar) chair, বিছানা (bichhana) bed, রান্নাঘর (rannaghor) "
"kitchen, বাথরুম (bathrum) bathroom, ছাদ (chhad) roof. Food - ভাত (bhat) rice, ডাল (dal) lentils, মাছ "
"(machh) fish, মাংস (mangsho) meat, ডিম (dim) egg, দুধ (dudh) milk, রুটি (ruti) bread, চা (cha) tea, পানি "
"(pani) water, মিষ্টি (mishti) sweet. Nature - গাছ (gachh) tree, ফুল (phul) flower, নদী (nodi) river, "
"পাহাড় (pahar) mountain, সমুদ্র (shomudro) sea, আকাশ (akash) sky, সূর্য (shurjo) sun, চাঁদ (chand) moon, "
"তারা (tara) star, মাটি (mati) soil. Animals - কুকুর (kukur) dog, বিড়াল (biral) cat, গরু (goru) cow, পাখি "
"(pakhi) bird, মাছ (machh) fish, বাঘ (bagh) tiger, হাতি (hati) elephant, ঘোড়া (ghora) horse, সাপ (shap) "
"snake, প্রজাপতি (projapoti) butterfly. Body - মাথা (matha) head, চোখ (chokh) eye, নাক (nak) nose, কান "
"(kan) ear, মুখ (mukh) mouth, হাত (hat) hand, পা (pa) foot, দাঁত (dant) tooth, চুল (chul) hair, হৃদয় "
"(hridoy) heart. Verbs - খাওয়া (khaowa) eat, পান করা (pan kora) drink, যাওয়া (jaowa) go, আসা (asha) "
"come, করা (kora) do, বলা (bola) speak, পড়া (pora) read, লেখা (lekha) write, দেখা (dekha) see, শোনা "
"(shona) listen, ঘুমানো (ghumano) sleep, ওঠা (otha) wake, বসা (bosha) sit, দাঁড়ানো (darano) stand, হাঁটা "
"(hata) walk, দৌড়ানো (dourano) run, দেওয়া (deowa) give, নেওয়া (neowa) take, কেনা (kena) buy, বেচা "
"(becha) sell, জানা (jana) know, চাওয়া (chaowa) want, ভালোবাসা (bhalobasha) love, খেলা (khela) play, "
"রান্না করা (ranna kora) cook, হাসা (hasha) laugh, কাঁদা (kanda) cry, ভাবা (bhaba) think, বোঝা (bojha) "
"understand, শেখা (shekha) learn. Adjectives - ভালো (bhalo) good, খারাপ (kharap) bad, বড় (boro) big, "
"ছোট (chhoto) small, নতুন (notun) new, পুরনো (purono) old, সুন্দর (shundor) beautiful, লম্বা (lomba) tall, "
"গরম (gorom) hot, ঠান্ডা (thanda) cold, ভারী (bhari) heavy, হালকা (halka) light, সহজ (shohoj) easy, কঠিন "
"(kothin) difficult, দ্রুত (druto) fast, ধীর (dhir) slow, পরিষ্কার (porishkar) clean, নোংরা (nongra) dirty, "
"সত্যি (shotti) true, মিষ্টি (mishti) sweet. Adverbs - খুব (khub) very, একটু (ektu) a little, এখন (ekhon) "
"now, পরে (pore) later, আজ (aj) today, কাল (kal) tomorrow, এখানে (ekhane) here, ওখানে (okhane) there, "
"সবসময় (shobshomoy) always, একসাথে (ekshathe) together. Pronouns - আমি (ami) I, আমরা (amra) we, তুমি "
"(tumi) you, আপনি (apni) you formal, সে (she) he/she, তিনি (tini) he/she formal, এটা (eta) this, ওটা (ota) "
"that, আমার (amar) my, তার (tar) his/her. Numbers - এক (ek) 1, দুই (dui) 2, তিন (tin) 3, চার (char) 4, "
"পাঁচ (panch) 5, ছয় (chhoy) 6, সাত (shat) 7, আট (at) 8, নয় (noy) 9, দশ (dosh) 10, এগারো (egaro) 11, বারো "
"(baro) 12, তেরো (tero) 13, চৌদ্দ (chouddo) 14, পনেরো (ponero) 15, ষোলো (sholo) 16, সতেরো (shotero) 17, "
"আঠারো (atharo) 18, উনিশ (unish) 19, বিশ (bish) 20. Time - দিন (din) day, রাত (rat) night, সকাল (shokal) "
"morning, দুপুর (dupur) noon, সন্ধ্যা (shondha) evening, সপ্তাহ (shoptaho) week, মাস (mash) month, বছর "
"(bochhor) year, আজ (aj) today, কাল (kal) tomorrow. Days - রবিবার (robibar) Sunday, সোমবার (shombar) "
"Monday, মঙ্গলবার (mongolbar) Tuesday, বুধবার (budhbar) Wednesday, বৃহস্পতিবার (brihoshpotibar) Thursday, "
"শুক্রবার (shukrobar) Friday, শনিবার (shonibar) Saturday, সময় (shomoy) time, কাজ (kaj) work, টাকা (taka) "
"money. Places - শহর (shohor) city, গ্রাম (gram) village, রাস্তা (rasta) road, বাজার (bajar) market, স্কুল "
"(skul) school, হাসপাতাল (hashpatal) hospital, স্টেশন (steshon) station, বিমানবন্দর (bimanbondor) airport, "
"হোটেল (hotel) hotel, দোকান (dokan) shop. Things - বই (boi) book, কলম (kolom) pen, কাগজ (kagoj) paper, "
"চিঠি (chithi) letter, ছবি (chhobi) picture, গান (gan) song, খবর (khobor) news, প্রশ্ন (proshno) question, "
"উত্তর (uttor) answer, ভাষা (bhasha) language. Question words - কে (ke) who, কী (ki) what, কোথায় (kothay) "
"where, কখন (kokhon) when, কেন (keno) why, কেমন (kemon) how, কত (koto) how much, কোন (kon) which, হ্যাঁ "
"(hya) yes, না (na) no. Grammar recap: SOV order; no gender; articles -টা/-টি/-জন; plurals -গুলো/-রা; "
"cases -কে -র -এ -থেকে; না negates verbs, নেই negates existence; কি ends yes/no questions. Verb endings: "
"present খাই খাও খায় খান; past খেলাম খেলে খেল খেলেন; future খাবো খাবে খাবে খাবেন; continuous খাচ্ছি "
"খাচ্ছো খাচ্ছে খাচ্ছেন. Three yous: তুই তুমি আপনি. Greeting master key: নমস্কার. Farewell: বিদায়, ভালো "
"থেকো. Review method: read this record weekly; any word you miss goes back into daily drills.",
"how_it_works":
"Use this record as the weekly audit: read the 200 words aloud, marking any you miss. Missed words return "
"to daily drills; mastered words stay in weekly review. Retell all three stories from memory. Hold one "
"full conversation - market, friend, or problem - without notes. When all of that is clean, the ladder "
"is climbed.",
"key_points": [
"200 core words in 20 groups of 10 - the working vocabulary",
"Full alphabet, numerals, and grammar in one reference",
"Weekly audit: missed words return to daily drills",
"Retell all three stories from memory",
"One full unscripted conversation = graduation",
],
"requirements": [
"Read all 200 words aloud weekly, marking misses",
"Return missed words to daily drills",
"Retell the three stories from memory",
"Hold one full conversation without notes",
"Teach five words to someone else",
],
"standards": STD_CORE,
"citations": [CIT_ISO, CIT_ISO3, CIT_UNI, CIT_CHAT, CIT_RAD, CIT_ETH],
"sig_lens":
"Signature original interpretation: the mastery review is the Signature final seal - 200 word-stones, the "
"whole alphabet, the grammar frame, three stories, twenty idioms, pressed into one covenant page. The "
"learner who passes the audit carries the Signature in his voice forever.",
},
]
