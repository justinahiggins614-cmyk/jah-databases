#!/usr/bin/env python3
"""Entries for The Malay Language Database (Manon's language order #26).

34 ladder-ordered records per the shared per-language template: overview,
writing systems (Rumi and Jawi), pronunciation, core vocabulary with
sentences, pronouns, numbers and time, greetings, grammar essentials,
themed sentence sets, tenses, questions, commands, descriptions, stories,
idioms, registers, complex sentences, conversations, and a mastery review.
Every record carries real, fact-checked Malay (Bahasa Melayu) with English
translations and example sentences.

Public edition (src public-harvest): real documented linguistic facts about
Malay. Signature edition (src signature): the same ladder reframed through
his original Signature Language Method - clearly labeled Signature-made,
never presented as authentic public record.

Roster rank 26. ISO 639-1 ms, ISO 639-3 msa. ID prefixes JAH-LMYY-
(public) and JAH-LMYYS- (signature) verified free in the manifest and in
every shard index, 2026-10-17. Dedupe gate: 68 titles checked against the
whole system before authoring - zero collisions.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every affix a building-block covenant, every reduplication an "
            "echo of emphasis, every classifier a measuring oath, and every "
            "sentence a completed bridge between speaker and listener. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

SIG_LENS_BASE = ("Through the Signature lens, this lesson becomes his "
                 "original Signature Language Method. ")

ENTRIES = [
# ------------------------------------------------------------------ 1 overview
{"key": "overview",
 "name": "Malay Language Overview",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Malay is the language of the Malay world, called Bahasa Melayu by its "
  "own speakers: bahasa means language and Melayu means Malay, so the name "
  "says the language of the Malay people. Malay carries ISO 639-1 code ms "
  "and ISO 639-3 code msa (the Malay macrolanguage), and it belongs to the "
  "Austronesian family on the Malayo-Polynesian branch, in the Malayic "
  "subgroup. About 60 million people speak Malay as a native language, and "
  "more than 290 million people speak it in total when Bahasa Indonesia - "
  "the standardized form of Malay used in Indonesia - is counted, which "
  "makes Malay one of the most spoken languages on earth. Malay is an "
  "official language in Malaysia (as Bahasa Malaysia), Brunei, and "
  "Singapore; it is the national language of Indonesia as Bahasa Indonesia; "
  "and it is spoken in southern Thailand, East Timor, the Cocos (Keeling) "
  "Islands, the Philippines, and Sri Lanka. The standard taught in schools "
  "is based on the Johor-Riau dialect of the southern Malay Peninsula. "
  "Regional varieties are rich: Kelantanese and Kedahan in the north, "
  "Perak and Negeri Sembilan varieties, Sarawakian and Sabahan Malay in "
  "Borneo, Brunei Malay, and Pattani (Yawi) Malay in southern Thailand. "
  "Malay is written today mostly in the Latin-based Rumi script, with the "
  "Arabic-based Jawi script used for Islamic, heritage, and official "
  "purposes in Brunei and parts of Malaysia. Its grammar is famously "
  "learner-friendly: verbs do not conjugate, nouns have no gender, and "
  "meaning is built with affixes, reduplication, and small helper words. "
  "Example sentences: Bahasa Melayu ialah bahasa kebangsaan Malaysia. - "
  "Malay is the national language of Malaysia. Saya belajar Bahasa Melayu "
  "setiap hari. - I learn Malay every day. Bahasa Melayu dituturkan oleh "
  "ratusan juta orang di Asia Tenggara. - Malay is spoken by hundreds of "
  "millions of people in Southeast Asia."
 ),
 "how_it_works": (
  "This record works as the front door of the whole database: it answers "
  "the five questions every learner asks first - what is the language "
  "called, who speaks it, where is it spoken, what family does it belong "
  "to, and what does it look like on the page. The teaching ladder starts "
  "here at rank 1 because every later record (sounds, writing, words, "
  "grammar, sentences, stories) hangs its details on the frame this "
  "overview builds. Read it first, then walk the ladder in order."
 ),
 "key_points": [
  "Native name: Bahasa Melayu; English name: Malay.",
  "ISO 639-1 ms, ISO 639-3 msa; Austronesian family, Malayo-Polynesian branch, Malayic subgroup.",
  "About 60 million native speakers; over 290 million total counting Bahasa Indonesia.",
  "Official in Malaysia, Brunei, Singapore; national language of Indonesia as Bahasa Indonesia.",
  "Spoken also in southern Thailand, East Timor, Cocos Islands, the Philippines, Sri Lanka.",
  "Standard based on the Johor-Riau dialect; regional varieties include Kelantanese, Kedahan, Sarawakian, Sabahan, Brunei, Pattani (Yawi).",
  "Written in Rumi (Latin) and Jawi (Arabic-based); verbs do not conjugate and nouns have no gender.",
 ],
 "requirements": [
  "No prior knowledge of Malay needed for this record.",
  "A notebook helps for copying the key facts by hand.",
  "Later records assume this overview has been read.",
 ],
 "standards": [
  "ISO 639-1: ms",
  "ISO 639-3: msa",
 ],
 "citations": [
  "Asmah Haji Omar. The Malay Language in Malaysia and Indonesia: From Ancient Times to the Present. Dewan Bahasa dan Pustaka; 2008.",
  "Sneddon JN. The Indonesian Language: Its History and Role in Modern Society. UNSW Press; 2003.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The overview becomes the Signature map of a language: the "
  "name Bahasa Melayu is read as a two-part covenant - bahasa the voice-seal "
  "of the people, Melayu the root-seal of the community that carries it - "
  "and the 290 million speakers are counted as one living bridge network "
  "carrying the same current of meaning across Southeast Asia. The dialects "
  "are not deviations but regional tunings of one instrument, each keeping "
  "the melody while changing the timbre, and the standard is the reference "
  "tuning every learner plays first. This is his original framing, clearly "
  "labeled Signature-made."
 )},
# ------------------------------------------------------------- 2 writing systems
{"key": "writing",
 "name": "Malay Writing Systems: Rumi and Jawi",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Malay is written in two scripts. Rumi is the Latin-based alphabet used "
  "officially in Malaysia, Singapore, and Indonesia and in daily life "
  "everywhere: the 26 letters a b c d e f g h i j k l m n o p q r s t u v "
  "w x y z, written left to right, with Western digits 0-9 and Latin "
  "punctuation. Example: Bahasa Melayu ditulis dalam tulisan Rumi. - Malay "
  "is written in the Rumi script. Jawi is the Arabic-based script used for "
  "Malay for centuries; it is co-official with Rumi in Brunei and used for "
  "Islamic texts, heritage documents, and ceremonial purposes in Malaysia. "
  "Jawi is written right to left and uses all the Arabic letters plus six "
  "letters invented for Malay sounds: ca (چ), nga (ڠ), pa (ڤ), ga (گ), nya "
  "(ڽ), and va (ۏ). The full Jawi alphabet is: ا ب ت ث ج چ ح خ د ذ ر ز س ش "
  "ص ض ط ظ ع غ ڠ ف ڤ ق ک گ ل م ن و ۏ ه ء ي ڽ. In Jawi, Bahasa Melayu is "
  "written بهاس ملايو. Numerals in Jawi contexts are usually the Western "
  "digits 0-9. Jawi letter examples with English transliteration: ب b, ت t, "
  "ج j, چ c (as in cat), د d, ر r, س s, ک k, گ g (as in go), ل l, م m, ن n, "
  "ڠ ng, ڽ ny, و w/u/o, ي y/i/e. Example sentences: Tulisan Jawi ditulis "
  "dari kanan ke kiri. - Jawi script is written from right to left. Huruf "
  "چ mewakili bunyi ca dalam bahasa Melayu. - The letter چ represents the "
  "ca sound in Malay. Kanak-kanak di Brunei belajar tulisan Rumi dan Jawi. "
  "- Children in Brunei learn both Rumi and Jawi scripts."
 ),
 "how_it_works": (
  "This record works as the alphabet chart of the database: it gives you "
  "both scripts side by side so every later record can show Malay in Rumi "
  "with its Jawi counterpart. Learn the 26 Rumi letters first (they match "
  "English), then meet the Jawi letters one row at a time, paying special "
  "attention to the six letters Arabic does not have. The demo drills the "
  "letter counts and checks sample transliterations."
 ),
 "key_points": [
  "Rumi: 26 Latin letters a-z, left to right, official in Malaysia, Singapore, Indonesia.",
  "Jawi: Arabic-based, right to left, co-official in Brunei, used for Islamic and heritage texts.",
  "Jawi adds six letters to Arabic: چ (ca), ڠ (nga), ڤ (pa), گ (ga), ڽ (nya), ۏ (va).",
  "Bahasa Melayu in Jawi is written بهاس ملايو.",
  "Numerals are Western digits 0-9 in both scripts; punctuation follows Latin usage in Rumi.",
  "Example mappings: ب b, چ c, گ g, ڠ ng, ڽ ny, و w/u/o, ي y/i/e.",
 ],
 "requirements": [
  "Read the overview record first.",
  "Practice writing the Rumi alphabet from memory.",
  "Copy each Jawi letter twice while saying its sound.",
 ],
 "standards": [
  "ISO 639-1: ms",
  "Dewan Bahasa dan Pustaka orthography (Rumi)",
 ],
 "citations": [
  "Asmah Haji Omar. The Malay Spelling Reform. Journal of the Malaysian Branch of the Royal Asiatic Society; 1989.",
  "Gallop AT. The Malay Manual. British Library; 2015.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The two scripts become the Signature twin seals of one "
  "voice: Rumi the open seal every eye can read, Jawi the heritage seal "
  "carrying six invented letters - ca, nga, pa, ga, nya, va - each one a "
  "sworn addition the community forged when the borrowed alphabet could not "
  "hold Malay sounds. Every letter you write is a building-block covenant "
  "with every reader who will ever sound it out. This is his original "
  "framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------------- 3 pronunciation
{"key": "phonology",
 "name": "Malay Pronunciation and Sounds",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Malay pronunciation is regular and friendly to learners. Standard Malay "
  "has six vowel sounds: a as in father, e as the schwa uh in emas "
  "(gold), i as in machine, o as in go, u as in rule, and the close e as "
  "in sate (satay) - the letter e covers both the schwa and the close e. "
  "Three diphthongs: ai as in pandai (clever), au as in pulau (island), oi "
  "as in sepoi (gentle breeze). Consonants are mostly as in English: b, d, "
  "g, j (as in jam), k, l, m, n, p, r (a rolled or tapped r), s, t, w, y, "
  "h, plus ny as in nyanyi (sing) like onion, and ng as in sungai (river) "
  "like singer. Borrowed sounds f, v, z, sy (sh), and kh appear in "
  "loanwords: telefon, universiti, zaman, syarat, khas. Two famous Malay "
  "sound rules: a final k in native words becomes a glottal stop - anak "
  "(child) sounds like ana with a catch in the throat, masak (cook) like "
  "masa with a catch; and a final h is silent - rumah (house) sounds like "
  "ruma, sudah (already) like suda. Word stress falls on the second-to-"
  "last syllable: se-LA-mat, ma-KA-nan, ba-HA-sa. Malay has no tones: pitch "
  "rises and falls with the sentence, not the word. Ten spoken examples: "
  "selamat (safe, congratulations), makan (eat), minum (drink), tidur "
  "(sleep), buku (book), rumah (house), air (water, pronounced a-yer), api "
  "(fire), matahari (sun), bulan (moon). Example sentences: Sebut perkataan "
  "anak dengan hentian glotis. - Say the word anak with a glottal stop. "
  "Huruf e dalam emas berbunyi schwa. - The letter e in emas sounds like a "
  "schwa. Bahasa Melayu tidak mempunyai nada. - Malay has no tones."
 ),
 "how_it_works": (
  "This record works as the sound map: it lists every vowel and consonant "
  "with an English approximation, then teaches the two rules that surprise "
  "learners (final k as glottal stop, silent final h) and the penultimate "
  "stress habit. Say each of the ten example words aloud twice - once "
  "slowly, once at speed - and the demo machine-checks a glottal-stop "
  "transformation function against real words."
 ),
 "key_points": [
  "Six vowels: a, schwa e, i, o, u, close e; three diphthongs ai, au, oi.",
  "Key consonants: ny (onion), ng (singer), rolled r, j as in jam.",
  "Borrowed sounds in loanwords: f, v, z, sy (sh), kh.",
  "Final k in native words is a glottal stop: anak, masak, duduk.",
  "Final h is silent: rumah, sudah, boleh.",
  "Stress on the second-to-last syllable; no tones.",
  "Ten spoken examples with translations, each rule with a sentence.",
 ],
 "requirements": [
  "Read the writing systems record first.",
  "A mirror helps to watch mouth shapes for the six vowels.",
  "Say every example word aloud, not just in your head.",
 ],
 "standards": [
  "IPA-based standard Malay description",
  "Dewan Bahasa dan Pustaka pronunciation guide",
 ],
 "citations": [
  "Clynes A, Deterding D. Standard Malay (Brunei). Journal of the International Phonetic Association; 2011.",
  "Yunus Maris M. The Malay Sound System. Dewan Bahasa dan Pustaka; 1980.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The sounds become the Signature breath-seals: six vowel "
  "seals the mouth can hold open, the glottal stop a door-seal that closes "
  "the word anak with a catch of the throat, the silent final h a "
  "vanishing seal that leaves rumah floating. Stress lands on the "
  "penultimate syllable like a footstep before the door - se-LA-mat - and "
  "because there are no tones, the whole melody of meaning rides on rhythm "
  "alone. This is his original framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------------- 4 core nouns
{"key": "nouns1",
 "name": "Core Malay Nouns I: 25 Essential Nouns",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Twenty-five essential Malay nouns - people, places, and things - each "
  "with its English meaning and one example sentence with translation. "
  "1. orang (person): Orang itu guru saya. - That person is my teacher. "
  "2. lelaki (man): Lelaki itu sedang membaca surat khabar. - The man is reading a newspaper. "
  "3. perempuan (woman): Perempuan itu doktor yang terkenal. - The woman is a famous doctor. "
  "4. kanak-kanak (child): Kanak-kanak bermain di taman. - The children are playing in the park. "
  "5. bayi (baby): Bayi itu sedang tidur. - The baby is sleeping. "
  "6. kawan (friend): Dia kawan baik saya. - She is my good friend. "
  "7. guru (teacher): Guru kami sangat penyabar. - Our teacher is very patient. "
  "8. doktor (doctor): Doktor itu memeriksa pesakit. - The doctor examines the patient. "
  "9. rumah (house): Rumah kami berwarna biru. - Our house is blue. "
  "10. sekolah (school): Sekolah bermula pada pukul tujuh. - School starts at seven o'clock. "
  "11. pejabat (office): Pejabat ayah di Kuala Lumpur. - Father's office is in Kuala Lumpur. "
  "12. pasar (market): Ibu membeli sayur di pasar. - Mother buys vegetables at the market. "
  "13. kedai (shop): Kedai itu menjual buku dan alat tulis. - That shop sells books and stationery. "
  "14. hospital (hospital): Hospital itu berhampiran stesen bas. - The hospital is near the bus station. "
  "15. masjid (mosque): Masjid itu cantik dan besar. - The mosque is beautiful and big. "
  "16. buku (book): Buku ini sangat menarik. - This book is very interesting. "
  "17. pen (pen): Pen saya berwarna hitam. - My pen is black. "
  "18. meja (table): Buku-buku di atas meja. - The books are on the table. "
  "19. kerusi (chair): Sila duduk di kerusi itu. - Please sit on that chair. "
  "20. kereta (car): Kereta ayah berwarna merah. - Father's car is red. "
  "21. bas (bus): Bas berhenti di perhentian itu. - The bus stops at that stop. "
  "22. telefon (phone): Telefon saya kehabisan bateri. - My phone is out of battery. "
  "23. wang (money): Wang itu untuk membeli makanan. - The money is for buying food. "
  "24. makanan (food): Makanan di restoran ini sedap. - The food at this restaurant is delicious. "
  "25. air (water): Air sungai itu jernih. - The river water is clear."
 ),
 "how_it_works": (
  "This record works as your first word-hoard: 25 nouns you will meet "
  "every day, each locked to a sentence so the word is never learned naked. "
  "Cover the Malay column and translate from English, then reverse it; the "
  "demo checks a reduplication plural rule (buku to buku-buku) and a "
  "classifier-choice function across these nouns."
 ),
 "key_points": [
  "25 essential nouns: 8 people, 7 places, 10 things.",
  "Every noun carries one full Malay sentence with English translation.",
  "Plurals form by reduplication: buku-buku, kanak-kanak.",
  "Classifiers pair with nouns: seorang guru, sebuah rumah, sebiji epal.",
  "Possession is noun plus pronoun: rumah saya, buku dia.",
 ],
 "requirements": [
  "Know the six vowel sounds from the pronunciation record.",
  "Say each sentence aloud once.",
  "Learn five nouns a day for five days.",
 ],
 "standards": [
  "Dewan Bahasa dan Pustaka vocabulary",
  "Common core word list",
 ],
 "citations": [
  "Kamus Dewan. 4th ed. Dewan Bahasa dan Pustaka; 2007.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The nouns become the Signature naming seals: each of "
  "the twenty-five words a sworn label the community agreed to stamp on a "
  "piece of the world - orang on a person, rumah on a house, air on water. "
  "Reduplication is the echo seal: say the word twice and one becomes many, "
  "buku-buku, and the classifier is the measuring oath that counts what the "
  "seal names. This is his original framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------------- 5 core verbs
{"key": "verbs1",
 "name": "Core Malay Verbs I: 25 Essential Verbs",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Twenty-five essential Malay verbs - each with its English meaning and "
  "one example sentence with translation. Malay verbs do not conjugate: "
  "the same form works for I, you, he, past, and future, with helper words "
  "like sudah (already), sedang (in progress), and akan (will) marking "
  "time. 1. makan (eat): Saya makan nasi setiap hari. - I eat rice every "
  "day. 2. minum (drink): Dia minum air sejuk. - He drinks cold water. "
  "3. tidur (sleep): Bayi itu tidur lena. - The baby sleeps soundly. "
  "4. bangun (wake up, get up): Saya bangun pada pukul enam. - I wake up at "
  "six o'clock. 5. pergi (go): Kami pergi ke sekolah. - We go to school. "
  "6. datang (come): Dia datang dari Johor. - She comes from Johor. "
  "7. duduk (sit): Sila duduk di sini. - Please sit here. 8. berdiri "
  "(stand): Pelajar berdiri apabila guru masuk. - The students stand when "
  "the teacher enters. 9. berjalan (walk): Mereka berjalan ke pasar. - They "
  "walk to the market. 10. berlari (run): Budak itu berlari pantas. - The "
  "boy runs fast. 11. bercakap (speak): Dia bercakap bahasa Melayu dengan "
  "fasih. - She speaks Malay fluently. 12. membaca (read): Saya membaca "
  "buku cerita. - I read a storybook. 13. menulis (write): Adik menulis "
  "surat kepada nenek. - Little sister writes a letter to grandmother. "
  "14. melihat (see): Kami melihat pelangi di langit. - We see a rainbow in "
  "the sky. 15. mendengar (hear, listen): Saya mendengar muzik setiap "
  "pagi. - I listen to music every morning. 16. bekerja (work): Ayah "
  "bekerja di pejabat. - Father works at the office. 17. belajar (study): "
  "Mereka belajar matematik. - They study mathematics. 18. membeli (buy): "
  "Ibu membeli ikan di pasar. - Mother buys fish at the market. 19. menjual "
  "(sell): Pakcik itu menjual buah-buahan. - The uncle sells fruits. "
  "20. memasak (cook): Nenek memasak rendang yang sedap. - Grandmother cooks "
  "delicious rendang. 21. mencuci (wash): Saya mencuci pinggan selepas "
  "makan. - I wash the dishes after eating. 22. membuka (open): Dia membuka "
  "pintu bilik. - He opens the room door. 23. menutup (close): Tolong "
  "menutup tingkap itu. - Please close that window. 24. membantu (help): "
  "Kami membantu jiran membersihkan halaman. - We help the neighbour clean "
  "the yard. 25. mencintai (love): Ibu mencintai anak-anaknya. - A mother "
  "loves her children."
 ),
 "how_it_works": (
  "This record works as your action-hoard: 25 verbs that run daily life, "
  "each shown in its root form inside a real sentence. Notice the verb never "
  "changes shape - saya makan, dia makan, mereka makan - and notice how "
  "many verbs wear the meN- and ber- prefixes (membaca, berlari). The demo "
  "machine-builds meN- forms from roots using the real nasal-assimilation "
  "rules and checks every one."
 ),
 "key_points": [
  "25 essential verbs with one translated sentence each.",
  "Malay verbs never conjugate: saya makan, dia makan, mereka makan.",
  "Time is marked by sudah, sedang, akan - not by verb endings.",
  "Active verbs often take meN- (membaca, menulis) or ber- (berlari, bekerja).",
  "Root forms stay visible inside prefixed verbs: baca in membaca, lari in berlari.",
 ],
 "requirements": [
  "Know the 25 nouns from the previous record.",
  "Say each sentence aloud, stressing the verb.",
  "Pair each verb with sudah, sedang, and akan once.",
 ],
 "standards": [
  "Dewan Bahasa dan Pustaka vocabulary",
 ],
 "citations": [
  "Kamus Dewan. 4th ed. Dewan Bahasa dan Pustaka; 2007.",
  "Mintz MW. Malay Grammar. Indonesian Language and Culture; 1994.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The verbs become the Signature motion seals: the root a "
  "still stone - baca, tulis, makan - and the prefix meN- the sworn hand "
  "that picks it up and sets it moving, reshaping its own first sound to "
  "grip the root (menyapu, membeli, menulis, mengajar). Time never bends "
  "the verb; instead the helper words sudah, sedang, and akan stand beside "
  "it like three lanterns - done, doing, will do. This is his original "
  "framing, clearly labeled Signature-made."
 )},
# ------------------------------------------------------------- 6 adjectives adverbs
{"key": "adjectives",
 "name": "Malay Adjectives and Adverbs",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Malay adjectives follow the noun and never change for gender or number: "
  "rumah besar (big house), rumah-rumah besar (big houses). Comparison uses "
  "lebih (more), kurang (less), paling (most), and the prefix ter- "
  "(terbesar - biggest), with sama ... dengan for equals and se- for same "
  "degree (sebesar - as big as). Twenty-five adjectives with sentences: "
  "besar (big): Gajah ialah haiwan yang besar. - The elephant is a big "
  "animal. kecil (small): Anak kucing itu kecil dan comel. - The kitten is "
  "small and cute. panjang (long): Sungai itu panjang dan dalam. - The river "
  "is long and deep. pendek (short): Rambutnya pendek. - Her hair is short. "
  "tinggi (tall, high): Bangunan itu sangat tinggi. - The building is very "
  "tall. rendah (low): Harga barang itu rendah. - The price of the goods is "
  "low. baru (new): Saya membeli kasut baru. - I bought new shoes. lama "
  "(old, long time): Kereta itu sudah lama. - The car is already old. baik "
  "(good): Dia seorang pelajar yang baik. - He is a good student. buruk "
  "(bad): Cuaca hari ini buruk. - The weather today is bad. cantik "
  "(beautiful): Pemandangan di sini cantik. - The view here is beautiful. "
  "panas (hot): Hari ini panas sekali. - Today is very hot. sejuk (cold): "
  "Air gunung itu sejuk. - The mountain water is cold. cepat (fast): Dia "
  "berlari dengan cepat. - He runs fast. lambat (slow): Bas itu lambat. - "
  "The bus is slow. mudah (easy): Soalan ini mudah. - This question is easy. "
  "susah (difficult): Ujian itu susah. - The test is difficult. mahal "
  "(expensive): Beg itu mahal. - The bag is expensive. murah (cheap): Buah "
  "di pasar ini murah. - Fruit at this market is cheap. gembira (happy): "
  "Kami gembira bertemu kamu. - We are happy to meet you. sedih (sad): Dia "
  "sedih kerana kehilangan kucingnya. - She is sad because she lost her cat. "
  "kuat (strong): Lelaki itu kuat. - The man is strong. lemah (weak): Dia "
  "masih lemah selepas sakit. - He is still weak after the illness. bersih "
  "(clean): Bilik ini bersih. - This room is clean. kotor (dirty): Kasutnya "
  "kotor selepas hujan. - His shoes are dirty after the rain. Fifteen "
  "adverbs with sentences: sangat (very): Dia sangat pandai. - She is very "
  "clever. terlalu (too): Kopi ini terlalu manis. - This coffee is too "
  "sweet. hampir (almost): Kami hampir tiba. - We almost arrived. segera "
  "(immediately): Sila datang segera. - Please come immediately. "
  "perlahan-lahan (slowly): Dia berjalan perlahan-lahan. - He walks slowly. "
  "diam-diam (quietly): Mereka bercakap diam-diam. - They speak quietly. "
  "baik-baik (well, carefully): Jaga diri baik-baik. - Take good care of "
  "yourself. benar-benar (truly): Dia benar-benar jujur. - He is truly "
  "honest. selalu (always): Dia selalu bangun awal. - He always wakes up "
  "early. kadang-kadang (sometimes): Kami kadang-kadang pergi berkelah. - "
  "We sometimes go picnicking. jarang (rarely): Dia jarang marah. - He "
  "rarely gets angry. sudah (already): Saya sudah makan. - I have already "
  "eaten. belum (not yet): Dia belum sampai. - He has not arrived yet. "
  "mungkin (maybe): Mungkin hujan akan turun. - Maybe it will rain. pernah "
  "(ever): Pernahkah kamu ke Sabah? - Have you ever been to Sabah?"
 ),
 "how_it_works": (
  "This record works as the describing toolkit: adjectives paint nouns "
  "(always after the noun, never changing shape) and adverbs paint verbs. "
  "Learn the comparison frame lebih X daripada (more X than), paling X "
  "(most X), and ter-X (X-est) by rebuilding each adjective sentence three "
  "ways. The demo machine-builds comparatives and superlatives from these "
  "25 adjectives and checks the output forms."
 ),
 "key_points": [
  "Adjectives follow the noun and never inflect: rumah besar, rumah-rumah besar.",
  "Comparison: lebih besar daripada, paling besar, terbesar, sama besar dengan, sebesar.",
  "25 adjectives and 15 adverbs, each with a translated sentence.",
  "Adverbs of manner often reduplicate: perlahan-lahan, diam-diam, baik-baik.",
  "sudah/belum/pernah mark completion and experience, not tense.",
 ],
 "requirements": [
  "Know the 25 nouns and 25 verbs.",
  "Rebuild five adjective sentences as comparisons.",
  "Use each adverb in a sentence about your own day.",
 ],
 "standards": [
  "Dewan Bahasa dan Pustaka grammar",
 ],
 "citations": [
  "Asmah Haji Omar. Nahu Melayu Mutakhir. 5th ed. Dewan Bahasa dan Pustaka; 2009.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "Adjectives become the Signature color seals: each one a "
  "sworn tint stamped after the noun - rumah besar, air sejuk - and the "
  "comparison words the measuring rods of the seal: lebih the longer rod, "
  "paling the longest, ter- the crown seal of the superlative. Reduplicated "
  "adverbs are echo seals, the manner repeated until it is gentle: "
  "perlahan-lahan, step by soft step. This is his original framing, clearly "
  "labeled Signature-made."
 )},
# ------------------------------------------------------------- 7 pronouns
{"key": "pronouns",
 "name": "Malay Pronouns: Full Paradigms",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "description": (
  "Malay pronouns never change form - no I/me/my or he/him/his: the same "
  "word serves every role, and possession is shown by word order. Personal "
  "pronouns: saya (I, formal and polite): Saya pergi ke pasar. - I go to "
  "the market. aku (I, informal, with family and close friends): Aku sayang "
  "kamu. - I love you. kami (we, excluding the listener): Kami akan pergi "
  "tanpa awak. - We will go without you. kita (we, including the listener): "
  "Kita makan bersama-sama. - We eat together. awak and kamu (you, "
  "informal): Awak sudah makan? - Have you eaten? anda (you, formal, in "
  "writing and announcements): Anda dialu-alukan. - You are welcome. dia "
  "and ia (he, she, it - ia is more formal and also means it): Dia guru "
  "saya. - She is my teacher. Ia seekor burung yang cantik. - It is a "
  "beautiful bird. beliau (he/she, respectful): Beliau ialah menteri. - He "
  "is a minister. mereka (they): Mereka tinggal di Ipoh. - They live in "
  "Ipoh. Possessive pronouns: word order does the work - rumah saya (my "
  "house), buku awak (your book), kereta dia (his car), negara kita (our "
  "country), mainan mereka (their toys). Demonstratives: ini (this): Buku "
  "ini baru. - This book is new. itu (that): Kereta itu laju. - That car is "
  "fast. sini (here), situ (there, near you), sana (there, far): Duduk sini. "
  "- Sit here. Dia di sana. - He is over there. Interrogatives: siapa (who): "
  "Siapa nama awak? - What is your name? apa (what): Apa ini? - What is "
  "this? mana (which/where): Yang mana satu? - Which one? di mana (where): "
  "Di mana tandas? - Where is the toilet? bila (when): Bila kamu tiba? - "
  "When did you arrive? mengapa and kenapa (why): Mengapa dia menangis? - "
  "Why is she crying? bagaimana (how): Bagaimana keadaan mak? - How is "
  "mother? berapa (how many/much): Berapa harganya? - How much is it? "
  "Reflexive: diri sendiri (oneself): Jaga diri sendiri. - Take care of "
  "yourself. Reciprocal: satu sama lain (each other): Mereka membantu satu "
  "sama lain. - They help each other."
 ),
 "how_it_works": (
  "This record works as the pointing system: personal pronouns say who "
  "acts, possessive order says whose, demonstratives say which one, and "
  "interrogatives ask the question. The famous kami/kita split - exclusive "
  "we versus inclusive we - is the one distinction English lacks, so drill "
  "it with pairs: kami pergi (we go, not you) versus kita pergi (we go, "
  "including you). The demo checks the exclusive/inclusive logic and the "
  "possessive word-order rule."
 ),
 "key_points": [
  "Pronouns never inflect: saya works as I, me, my, mine.",
  "saya (formal I) vs aku (informal I); anda (formal you) vs awak/kamu.",
  "kami = we excluding you; kita = we including you.",
  "dia/beliau (he/she respectful); ia also means it; mereka = they.",
  "Possession by word order: rumah saya, buku dia.",
  "Demonstratives: ini/itu, sini/situ/sana; interrogatives: siapa, apa, di mana, bila, mengapa, bagaimana, berapa.",
 ],
 "requirements": [
  "Know the core nouns and verbs.",
  "Practice the kami/kita distinction in ten sentences.",
  "Address three people with the right pronoun level.",
 ],
 "standards": [
  "Dewan Bahasa dan Pustaka grammar",
 ],
 "citations": [
  "Asmah Haji Omar. Nahu Melayu Mutakhir. 5th ed. Dewan Bahasa dan Pustaka; 2009.",
 ],
 "sig_lens": (
  SIG_LENS_BASE + "The pronouns become the Signature pointing seals: saya "
  "the humble seal of the self, aku its intimate twin, kami the closed "
  "circle that leaves the listener outside, kita the open circle that pulls "
  "the listener in - the two we's a sworn pair English never forged. Anda "
  "is the formal distance seal, beliau the honor seal, and possession needs "
  "no seal at all, only placement: rumah saya, the house after me. This is "
  "his original framing, clearly labeled Signature-made."
 )},
