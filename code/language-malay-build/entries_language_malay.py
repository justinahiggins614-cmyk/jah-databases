#!/usr/bin/env python3
"""Entries for the Malay to English databases (language orders, roster: Malay).

Roster: language-malay. Slug verified free in manifest (2,400+ databases)
and in all shard index files. 68 titles (34 public + 34 Signature Edition)
run through code/dedupe_gate.py against the whole system before authoring:
zero refusals.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-malay                 - The Malay to English Database
                                   (public-harvest: real, fact-checked Malay
                                   linguistics - every record carrying Malay
                                   content with English translation and example
                                   sentences, taught progressively along the
                                   teaching ladder from overview to mastery
                                   review)
  language-malay-signature       - The Malay to English Signature Database
                                   (his original Signature Word Method;
                                   src signature, titles suffixed " (Signature
                                   Edition)", clearly labeled Signature-made,
                                   never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LMYY- (public) and JAH-LMYYS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero
hits across all index files).

Numerical/linguistic cores: all hand-authored 2026-10-17, machine-verified
by the demos (see demos_language_malay.py): speaker arithmetic, script
counts, stress checkers, meN- affix rules, classifier selectors,
number-to-word converters, aspect classifiers, and vocabulary quizzes.
Every demo prints its real computed values, asserts tight bounds (never
float exact-equality), and ends with the OK marker; the build
machine-executes all 68 demos.

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

CIT_KAMUS = ("Dewan Bahasa dan Pustaka. Kamus Dewan. 4th ed. Kuala Lumpur: "
             "Dewan Bahasa dan Pustaka; 2017.")
CIT_TATA = ("Nik Safiah Karim et al. Tatabahasa Dewan: Edisi Ketiga. Kuala "
            "Lumpur: Dewan Bahasa dan Pustaka; 2015. (The standard reference "
            "grammar of Malay: affixation, reduplication, word order, "
            "classifiers, sentence types.)")
CIT_MABBIM = ("Majlis Bahasa Brunei Darussalam-Indonesia-Malaysia (MABBIM). "
              "Pedoman Umum Ejaan Bahasa Melayu. (The 1972 New Rumi Spelling "
              "standard shared by Malaysia, Brunei, and Indonesia.)")
CIT_ETHNO = ("Eberhard DM, Simons GF, Fennig CD, eds. Ethnologue: Languages "
             "of the World. 28th ed. Dallas: SIL International; 2025. "
             "(Malay macrolanguage: ISO 639-3 msa; about 77 million "
             "first-language speakers.)")
CIT_SNEd = ("Sneddon JN. Indonesian: A Comprehensive Grammar. 2nd ed. "
            "London: Routledge; 2010. (Indonesian is the standardized Malay "
            "of Indonesia; its grammar is the same Malayic system taught "
            "here.)")
CIT_HIST = ("Old Malay inscriptions in Pallava-derived script (Kedukan "
            "Bukit, 683 CE); Classical Malay of the Malacca sultanate; the "
            "Jawi script spread with trade and literacy from the 1300s; the "
            "1972 Ejaan Rumi Baharu spelling reform aligned Malaysian, "
            "Bruneian, and Indonesian spelling; Bahasa Malaysia is the "
            "national language of Malaysia and Brunei, a national language "
            "of Singapore, and the working language of East Timor.")

ENTRIES = [
    {
        "key": "overview",
        "name": "Malay Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Malay, called Bahasa Melayu by its speakers, is the national "
            "language of Malaysia and Brunei, one of the four official "
            "languages of Singapore, and the basis of Bahasa Indonesia, the "
            "official language of Indonesia. Its codes are ISO 639-1 ms and "
            "ISO 639-3 msa (macrolanguage). It belongs to the Austronesian "
            "family, Malayo-Polynesian branch, Malayic group - a cousin of "
            "Javanese, Sundanese, and Tagalog. About 77 million people "
            "speak Malay as a first language, and more than 270 million "
            "speak it in total when Indonesian, the standardized Malay of "
            "Indonesia, is counted. Malay is the language of the historic "
            "Malacca sultanate, the trade tongue of the archipelago for "
            "centuries, and one of the working languages of ASEAN. The "
            "oldest Malay writing is the Kedukan Bukit inscription of 683 "
            "CE. Dialects include Johor-Riau (the basis of the standard), "
            "Kelantan-Pattani, Terengganu, Kedah, Minangkabau, and "
            "Bruneian Malay. The standard is guided by the Dewan Bahasa "
            "dan Pustaka in Malaysia and Brunei and Badan Bahasa in "
            "Indonesia. Example sentences: Bahasa Melayu ialah bahasa "
            "kebangsaan Malaysia. (Malay is the national language of "
            "Malaysia.) Saya belajar bahasa Melayu setiap hari. (I study "
            "Malay every day.) Bahasa Indonesia berasal daripada bahasa "
            "Melayu. (Indonesian comes from Malay.)"
        ),
        "how_it_works": (
            "Malay works as an agglutinative Austronesian language: meaning "
            "is built by adding prefixes, suffixes, and circumfixes to a "
            "root word, and verbs never conjugate for person or tense. A "
            "beginner sentence follows subject-verb-object order, the same "
            "as English: Saya makan nasi. (I eat rice.) Time is carried by "
            "small helper words - sudah/telah for completed action, sedang "
            "for ongoing action, akan for future action - not by changing "
            "the verb: Saya sudah makan. (I have eaten.) Saya sedang makan. "
            "(I am eating.) Saya akan makan. (I will eat.) Negation uses "
            "tidak before verbs and adjectives, bukan before nouns: Saya "
            "tidak lapar. (I am not hungry.) Ini bukan buku saya. (This is "
            "not my book.) Everything in this database builds on these "
            "mechanics: sounds first, then words, then the sentences that "
            "carry them."
        ),
        "key_points": [
            "Malay (Bahasa Melayu, ISO ms/msa) is an Austronesian Malayic language with about 77 million native speakers and over 270 million total speakers counting Indonesian.",
            "It is the national language of Malaysia and Brunei, an official language of Singapore, and the base of Bahasa Indonesia.",
            "Verbs never conjugate for person or tense; time is marked by helper words: sudah (completed), sedang (ongoing), akan (future).",
            "Negation splits two ways: tidak before verbs and adjectives, bukan before nouns.",
            "The modern standard rests on Johor-Riau dialect, the 1972 spelling reform, and the Dewan Bahasa dan Pustaka.",
        ],
        "requirements": [
            "Know the names: Bahasa Melayu, ISO codes ms (639-1) and msa (639-3), Austronesian > Malayo-Polynesian > Malayic.",
            "Know the scale: about 77 million native speakers, over 270 million total with Indonesian.",
            "Name the four official-status countries: Malaysia, Brunei, Singapore, Indonesia.",
            "Read and write the three example sentences with their English translations from memory.",
            "Explain in one paragraph how Malay marks time without conjugating verbs.",
        ],
        "standards": [
            "Speaker figures follow Ethnologue 28th ed. 2025 for the Malay macrolanguage.",
            "Language-family classification follows the standard Austronesian account (Malayo-Polynesian > Malayic).",
            "ISO 639-1 ms and ISO 639-3 msa are the registered identifiers for Malay.",
        ],
        "citations": [CIT_ETHNO, CIT_KAMUS, CIT_HIST],
        "sig_lens": (
            "The Signature read: Malay is a signed tongue - a trade "
            "language that sealed bargains across a thousand islands for "
            "centuries. Where public linguistics counts speakers, the "
            "Signature Word Method counts witnesses: every speaker a living "
            "seal that the word means what it says."
        ),
    },
    {
        "key": "writing",
        "name": "Malay Writing System and Alphabet",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Malay is written in two scripts. Rumi, the Latin script, is "
            "the everyday script: 26 letters a b c d e f g h i j k l m n o "
            "p q r s t u v w x y z, written left to right, with the letter "
            "names a, bi, si, di, i, ef, ji, eic, ai, je, ke, el, em, en, o, "
            "pi, kiu, ar, es, ti, iu, vi, dabeliu, eks, wai, zed. Jawi, the "
            "Arabic-derived script, is the traditional script: written "
            "right to left, it keeps the 28 Arabic letters and adds six "
            "for Malay sounds - ca, nga, pa, ga, nya, and va - for 34 "
            "letters in all. Jawi remains in use for religious schooling, "
            "Brunei official signage, and classical literature. The letter "
            "e does double duty in Rumi, spelling both the open e (as in "
            "bela) and the schwa pepet sound (as in emas); only Jawi "
            "distinguishes them. The 1972 Ejaan Rumi Baharu spelling reform "
            "aligned Malaysian and Indonesian spelling: c for the ch sound "
            "(cuba), sy for sh (syarat), ny for the palatal nasal (nyanyi), "
            "ng for the velar nasal (dengan), kh for the guttural (khas). "
            "Numerals are the Latin 0-9: 0 sifar/kosong, 1 satu, 2 dua, 3 "
            "tiga, 4 empat, 5 lima, 6 enam, 7 tujuh, 8 lapan, 9 sembilan. "
            "Punctuation follows Latin conventions. Example sentences: "
            "Bahasa Melayu ditulis dengan huruf Rumi. (Malay is written in "
            "the Rumi script.) Jawi ditulis dari kanan ke kiri. (Jawi is "
            "written right to left.) Ejaan baharu diselaraskan pada tahun "
            "1972. (The new spelling was standardized in 1972.)"
        ),
        "how_it_works": (
            "Malay spelling is almost perfectly phonetic: each Rumi letter "
            "maps to one sound, so a word is pronounced exactly as it is "
            "spelled - with two exceptions to learn. First, final k, p, "
            "and t are unreleased: duduk is pronounced dudu(k) with the "
            "throat closing on the k. Second, the letter e hides two "
            "sounds: the full e of meja and the schwa pepet of emas. "
            "Capitalization, commas, periods, and question marks work as "
            "in English. To read Jawi, learn the six extra letters first, "
            "then the vowel signs: Malay vowels are written with alif, wau, "
            "and ya. Practice by writing your name in both scripts, then "
            "transliterate the five example words of this record."
        ),
        "key_points": [
            "Rumi (Latin, 26 letters, left to right) is the everyday script; Jawi (Arabic-derived, right to left) is the traditional script.",
            "Jawi adds six letters to the Arabic set for Malay sounds: ca, nga, pa, ga, nya, va.",
            "Malay spelling is phonetic: words are pronounced as spelled, except unreleased final k/p/t and the two sounds of e.",
            "The 1972 Ejaan Rumi Baharu reform standardized spelling across Malaysia, Brunei, and Indonesia.",
            "Numerals 0-9 and Latin punctuation are shared with English.",
        ],
        "requirements": [
            "Write the 26 Rumi letters with their Malay letter names from memory.",
            "Name the six extra Jawi letters and the sounds they carry.",
            "Transliterate five Rumi words into Jawi and back without a reference.",
            "Explain the two exceptions to phonetic spelling (final stops, the letter e).",
            "Write the digits 0-9 with their Malay names from memory.",
        ],
        "standards": [
            "Letter inventory follows the MABBIM Pedoman Umum Ejaan Bahasa Melayu.",
            "Jawi letter inventory follows the standard Brunei/Malaysia Jawi orthography.",
            "Word lists follow Kamus Dewan 4th ed. 2017.",
        ],
        "citations": [CIT_MABBIM, CIT_KAMUS, CIT_HIST],
        "sig_lens": (
            "The Signature read: two scripts, one covenant - Rumi the open "
            "hand, Jawi the sealed letter. Where public orthography lists "
            "letters, the Signature Word Method signs them: every stroke a "
            "witness that sound and letter keep faith."
        ),
    },
    {
        "key": "phonology",
        "name": "Malay Pronunciation and Phonology",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Malay has six vowel sounds: a (as in father: mata - eye), i "
            "(as in machine: ikan - fish), u (as in flute: buku - book), e "
            "taling (as in bed: meja - table), e pepet the schwa (as in "
            "about: emas - gold), and o (as in more: orang - person). Three "
            "diphthongs complete the set: ai (pandai - clever), au (pulau "
            "- island), oi (amboi - wow). The consonants are p, b, t, d, "
            "k, g, c (ch as in church: cuba - try), j (as in judge: jalan "
            "- road), s, h, m, n, ny (canyon: nyanyi - sing), ng (singer: "
            "dengan - with), l, r (trilled: rumah - house), w, y. Three "
            "pronunciation rules shape every word. First, word stress falls "
            "on the second-to-last syllable: MAkan, miNUM, ruMAH, beSAR. "
            "Second, final k, p, and t are unreleased - the airflow stops "
            "instead of bursting: duduk sounds like dudu(k), sedap like "
            "seda(p), ingat like inga(t). Third, a final h is silent and "
            "final a often softens toward the schwa in Johor-Riau speech: "
            "rumah is pronounced ruma(h). Malay has no tones - pitch never "
            "changes a word's meaning. Ten spoken-example words: mata "
            "(eye), ikan (fish), rumah (house), makan (eat), minum (drink), "
            "besar (big), kecil (small), jalan (walk/road), air (water), "
            "api (fire). Example sentences: Tekanan suku kata jatuh pada "
            "suku kata kedua terakhir. (Word stress falls on the "
            "second-to-last syllable.) Bahasa Melayu tidak mempunyai nada. "
            "(Malay has no tones.) Huruf r disebut dengan getaran. (The "
            "letter r is pronounced with a trill.)"
        ),
        "how_it_works": (
            "Pronouncing Malay is a three-step drill: find the "
            "second-to-last syllable and stress it, close the throat "
            "instead of releasing final k/p/t, and trill the r. Break "
            "words into syllables - ma-kan, mi-num, ru-mah - and tap the "
            "stressed one. Minimal practice pairs sharpen the ear: bela "
            "(defend) with open e against emas (gold) with pepet; sudah "
            "(already) against sedap (delicious). Because spelling is "
            "phonetic, reading aloud is the fastest path to correct "
            "pronunciation: every sentence in this database is a "
            "pronunciation exercise waiting to be spoken."
        ),
        "key_points": [
            "Six vowels (a, i, u, open e, schwa pepet, o) and three diphthongs (ai, au, oi).",
            "Stress always falls on the second-to-last syllable: MAkan, beSAR.",
            "Final k, p, t are unreleased; final h is silent; Malay has no tones.",
            "The trilled r and the palatal ny and velar ng are the three sounds English speakers practice most.",
            "Spelling is phonetic, so reading aloud drills pronunciation automatically.",
        ],
        "requirements": [
            "Pronounce the six vowels and three diphthongs with the example words from memory.",
            "Mark the stressed syllable in ten new words with 90 percent accuracy.",
            "Pronounce final k/p/t unreleased in duduk, sedap, and ingat.",
            "Distinguish bela (open e) from emas (pepet) by ear and by mouth.",
            "Read the ten example words aloud with correct stress in one pass.",
        ],
        "standards": [
            "Sound inventory follows the standard account in Tatabahasa Dewan: Edisi Ketiga.",
            "Penultimate stress is the standard Johor-Riau pronunciation taught in Malaysia.",
            "Example vocabulary follows Kamus Dewan 4th ed. 2017.",
        ],
        "citations": [CIT_TATA, CIT_KAMUS],
        "sig_lens": (
            "The Signature read: six vowels, one covenant of breath - "
            "stress the penultimate, seal the final stop. Where public "
            "phonetics charts sounds, the Signature Word Method sounds "
            "them: every syllable witnessed, every stress sworn."
        ),
    },
    {
        "key": "nouns",
        "name": "Malay Core Nouns I",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Malay nouns, each with an example "
            "sentence. 1. orang (person): Orang itu guru saya. (That person "
            "is my teacher.) 2. lelaki (man): Lelaki itu ayah saya. (That "
            "man is my father.) 3. perempuan (woman): Perempuan itu ibu "
            "saya. (That woman is my mother.) 4. kanak-kanak (child): "
            "Kanak-kanak itu bermain. (The child is playing.) 5. rumah "
            "(house): Rumah saya besar. (My house is big.) 6. pintu (door): "
            "Tutup pintu itu. (Close that door.) 7. tingkap (window): Buka "
            "tingkap itu. (Open that window.) 8. meja (table): Buku ada di "
            "atas meja. (The book is on the table.) 9. kerusi (chair): "
            "Duduk di kerusi ini. (Sit on this chair.) 10. katil (bed): "
            "Katil saya selesa. (My bed is comfortable.) 11. buku (book): "
            "Saya membaca buku. (I read a book.) 12. pen (pen): Ini pen "
            "saya. (This is my pen.) 13. kereta (car): Kereta itu laju. "
            "(That car is fast.) 14. bas (bus): Saya menaiki bas. (I ride "
            "the bus.) 15. kapal terbang (airplane): Kapal terbang itu "
            "tinggi. (That airplane is high.) 16. sekolah (school): Sekolah "
            "saya dekat. (My school is near.) 17. guru (teacher): Guru itu "
            "baik. (That teacher is kind.) 18. doktor (doctor): Doktor itu "
            "sibuk. (That doctor is busy.) 19. hospital (hospital): Hospital "
            "itu jauh. (That hospital is far.) 20. kedai (shop): Kedai itu "
            "buka. (That shop is open.) 21. pasar (market): Pasar itu "
            "sesak. (The market is crowded.) 22. wang (money): Saya ada "
            "wang. (I have money.) 23. makanan (food): Makanan ini sedap. "
            "(This food is delicious.) 24. air (water): Saya minum air. (I "
            "drink water.) 25. masa (time): Masa itu berharga. (Time is "
            "precious.)"
        ),
        "how_it_works": (
            "Malay nouns never change form: no plural endings, no gender, "
            "no cases. Plurality is shown by reduplication (buku-buku - "
            "books), by a number with a classifier (tiga buah buku - three "
            "books), or by context alone (buku can mean book or books). "
            "Possession attaches to the noun: buku saya (my book), kereta "
            "dia (his/her car), rumah kami (our house). The demonstratives "
            "ini (this) and itu (that) follow the noun: buku ini (this "
            "book), rumah itu (that house). Learn each noun with its "
            "classifier now - seorang for people, sebuah for things, "
            "seekor for animals - because the classifier, not the noun, "
            "carries the counting."
        ),
        "key_points": [
            "Malay nouns never inflect: no plurals, no gender, no cases.",
            "Plurals come from reduplication (buku-buku), number + classifier (tiga buah buku), or context.",
            "Possessives follow the noun: buku saya, kereta dia, rumah kami.",
            "Demonstratives follow the noun: buku ini (this book), rumah itu (that house).",
            "Every noun travels with a classifier: seorang (person), sebuah (thing), seekor (animal).",
        ],
        "requirements": [
            "Translate all 25 nouns Malay-to-English and back with 90 percent accuracy.",
            "Write the example sentence for each noun from memory with its translation.",
            "Form the plural of ten nouns by reduplication.",
            "Attach the correct classifier to ten nouns (seorang/sebuah/seekor).",
            "Build five new sentences pairing a noun with ini/itu and a possessive.",
        ],
        "standards": [
            "Noun forms follow Kamus Dewan 4th ed. 2017.",
            "Classifier usage follows Tatabahasa Dewan: Edisi Ketiga.",
            "Pluralization rules follow the standard grammar account.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: twenty-five names, each a signed "
            "instrument - the noun never bends, never breaks. Where public "
            "vocabulary lists words, the Signature Word Method seals them: "
            "one form, every number, the classifier keeping count."
        ),
    },
]

ENTRIES += [
    {
        "key": "verbs",
        "name": "Malay Core Verbs I",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Malay verbs, each with an example "
            "sentence. Malay verbs never conjugate - one form serves every "
            "person and every tense. 1. makan (eat): Saya makan nasi. (I "
            "eat rice.) 2. minum (drink): Dia minum air. (He/She drinks "
            "water.) 3. tidur (sleep): Bayi itu tidur. (The baby sleeps.) "
            "4. bangun (wake up/get up): Saya bangun awal. (I wake up "
            "early.) 5. pergi (go): Kami pergi ke sekolah. (We go to "
            "school.) 6. datang (come): Dia datang esok. (He/She comes "
            "tomorrow.) 7. duduk (sit): Sila duduk. (Please sit.) 8. "
            "berdiri (stand): Mereka berdiri. (They stand.) 9. berjalan "
            "(walk): Kami berjalan kaki. (We walk on foot.) 10. berlari "
            "(run): Budak itu berlari. (The boy runs.) 11. bercakap (speak): "
            "Dia bercakap Melayu. (He/She speaks Malay.) 12. mendengar "
            "(listen/hear): Saya mendengar muzik. (I listen to music.) 13. "
            "melihat (see): Saya melihat burung. (I see a bird.) 14. "
            "membaca (read): Dia membaca surat khabar. (He/She reads the "
            "newspaper.) 15. menulis (write): Saya menulis surat. (I write "
            "a letter.) 16. belajar (study/learn): Kami belajar sains. (We "
            "study science.) 17. bekerja (work): Ayah bekerja keras. (Father "
            "works hard.) 18. bermain (play): Mereka bermain bola. (They "
            "play ball.) 19. membeli (buy): Ibu membeli sayur. (Mother buys "
            "vegetables.) 20. menjual (sell): Dia menjual buah. (He/She "
            "sells fruit.) 21. memasak (cook): Nenek memasak kari. "
            "(Grandmother cooks curry.) 22. mencuci (wash): Saya mencuci "
            "pinggan. (I wash the dishes.) 23. memandu (drive): Abang "
            "memandu kereta. (Brother drives the car.) 24. menaiki (ride/"
            "board): Kami menaiki bas. (We board the bus.) 25. memberi "
            "(give): Guru memberi nasihat. (The teacher gives advice.)"
        ),
        "how_it_works": (
            "The Malay verb engine is the meN- prefix: it turns a root "
            "into an active verb, reshaping the root's first sound - tulis "
            "becomes menulis, sapu becomes menyapu, pukul becomes memukul, "
            "cari becomes mencari, ajar becomes mengajar. The ber- prefix "
            "marks states and habitual actions: kerja becomes bekerja (to "
            "work), jalan becomes berjalan (to walk). The di- prefix makes "
            "the passive: dimakan (eaten), dibaca (read). Because the verb "
            "never changes for person or tense, Saya makan, Dia makan, and "
            "Mereka makan all use makan - only the pronoun changes. Learn "
            "each verb as a pair: the bare root and its meN- form."
        ),
        "key_points": [
            "Malay verbs never conjugate: one form for every person, number, and tense.",
            "The meN- prefix builds active verbs and reshapes the root's first sound: tulis to menulis, sapu to menyapu.",
            "The ber- prefix marks states and habitual action: kerja to bekerja, jalan to berjalan.",
            "The di- prefix builds the passive: dimakan (eaten), dibaca (read).",
            "Time rides on helper words, not the verb: sudah (completed), sedang (ongoing), akan (future).",
        ],
        "requirements": [
            "Translate all 25 verbs Malay-to-English and back with 90 percent accuracy.",
            "Write the example sentence for each verb from memory with its translation.",
            "Derive the meN- form of ten new roots using the first-sound rules.",
            "Build five sentences each with sudah, sedang, and akan plus one verb.",
            "Convert five active meN- verbs into di- passives.",
        ],
        "standards": [
            "Verb forms follow Kamus Dewan 4th ed. 2017.",
            "Affixation rules follow Tatabahasa Dewan: Edisi Ketiga.",
            "Aspect helpers follow the standard grammar account.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: twenty-five actions, each a signed deed - "
            "the verb never bends for king or servant. Where public "
            "grammar conjugates, the Signature Word Method keeps one form: "
            "the action sealed, time carried by witnesses."
        ),
    },
    {
        "key": "adjectives",
        "name": "Malay Adjectives and Adverbs",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five Malay adjectives and fifteen adverbs, each with an "
            "example sentence. Malay adjectives never agree with the noun "
            "- one form fits all. ADJECTIVES: 1. besar (big): Rumah itu "
            "besar. (That house is big.) 2. kecil (small): Kucing itu "
            "kecil. (That cat is small.) 3. panjang (long): Jalan ini "
            "panjang. (This road is long.) 4. pendek (short): Cerita itu "
            "pendek. (That story is short.) 5. tinggi (tall/high): Bangunan "
            "itu tinggi. (That building is tall.) 6. rendah (low): Harga "
            "itu rendah. (That price is low.) 7. baru (new): Kereta itu "
            "baru. (That car is new.) 8. lama (old/long time): Rumah itu "
            "lama. (That house is old.) 9. baik (good/kind): Dia baik. "
            "(He/She is kind.) 10. buruk (bad): Cuaca itu buruk. (The "
            "weather is bad.) 11. cantik (beautiful): Bunga itu cantik. "
            "(That flower is beautiful.) 12. tampan (handsome): Pelakon itu "
            "tampan. (That actor is handsome.) 13. panas (hot): Kopi ini "
            "panas. (This coffee is hot.) 14. sejuk (cold): Air ini sejuk. "
            "(This water is cold.) 15. cepat (fast): Dia berlari cepat. "
            "(He/She runs fast.) 16. lambat (slow): Bas itu lambat. (That "
            "bus is slow.) 17. kuat (strong): Dia kuat. (He/She is strong.) "
            "18. lemah (weak): Dia lemah. (He/She is weak.) 19. mahal "
            "(expensive): Beg itu mahal. (That bag is expensive.) 20. murah "
            "(cheap): Beg ini murah. (This bag is cheap.) 21. bersih "
            "(clean): Bilik ini bersih. (This room is clean.) 22. kotor "
            "(dirty): Kasut itu kotor. (Those shoes are dirty.) 23. terang "
            "(bright): Lampu itu terang. (That lamp is bright.) 24. gelap "
            "(dark): Malam ini gelap. (Tonight is dark.) 25. senang (easy/"
            "happy): Kerja ini senang. (This work is easy.) ADVERBS: 1. "
            "sangat (very): Dia sangat pandai. (He/She is very clever.) 2. "
            "terlalu (too): Ini terlalu mahal. (This is too expensive.) 3. "
            "agak (quite): Dia agak penat. (He/She is quite tired.) 4. "
            "sedikit (a little): Saya faham sedikit. (I understand a "
            "little.) 5. selalu (always): Dia selalu datang awal. (He/She "
            "always comes early.) 6. jarang (rarely): Kami jarang berjumpa. "
            "(We rarely meet.) 7. kadang-kadang (sometimes): Kadang-kadang "
            "dia lewat. (Sometimes he/she is late.) 8. perlahan-lahan "
            "(slowly): Bercakap perlahan-lahan. (Speak slowly.) 9. "
            "cepat-cepat (quickly): Datang cepat-cepat. (Come quickly.) "
            "10. betul-betul (really): Saya betul-betul lapar. (I am really "
            "hungry.) 11. bersama-sama (together): Kami pergi bersama-sama. "
            "(We go together.) 12. tiba-tiba (suddenly): Tiba-tiba hujan "
            "turun. (Suddenly the rain fell.) 13. hampir (almost): Dia "
            "hampir jatuh. (He/She almost fell.) 14. masih (still): Dia "
            "masih tidur. (He/She is still sleeping.) 15. hanya (only): "
            "Hanya saya yang datang. (Only I came.)"
        ),
        "how_it_works": (
            "Malay adjectives follow the noun they describe - the reverse "
            "of English: rumah besar (house big = big house), kereta merah "
            "(car red = red car). They never change for number or gender: "
            "rumah besar, rumah-rumah besar - the adjective stays besar. "
            "Comparison is built with helpers: lebih (more), paling "
            "or ter- (most), kurang (less), sama (same as): lebih besar "
            "(bigger), paling besar or terbesar (biggest), sebesar (as big "
            "as). Adverbs usually follow the verb or adjective they "
            "modify, and many are formed by reduplicating the adjective: "
            "perlahan becomes perlahan-lahan, cepat becomes cepat-cepat. "
            "Degree adverbs like sangat and terlalu come before the "
            "adjective: sangat cantik (very beautiful)."
        ),
        "key_points": [
            "Adjectives follow the noun: rumah besar (big house), never change for number or gender.",
            "Comparison uses helpers: lebih (more), paling/ter- (most), kurang (less), sama (as).",
            "Many adverbs are reduplicated adjectives: perlahan-lahan (slowly), cepat-cepat (quickly).",
            "Degree words come before the adjective: sangat cantik, terlalu mahal.",
            "Frequency adverbs (selalu, jarang, kadang-kadang) usually come before the verb.",
        ],
        "requirements": [
            "Translate all 25 adjectives and 15 adverbs both directions with 90 percent accuracy.",
            "Place ten adjectives after their nouns correctly in new sentences.",
            "Build the comparative and superlative of ten adjectives (lebih/paling/ter-).",
            "Form five adverbs by reduplication from adjectives.",
            "Write five sentences each using sangat, terlalu, and kadang-kadang.",
        ],
        "standards": [
            "Adjective forms follow Kamus Dewan 4th ed. 2017.",
            "Comparison and reduplication rules follow Tatabahasa Dewan: Edisi Ketiga.",
            "Word order follows the standard noun-adjective account.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the quality follows the thing - never "
            "before, never bending. Where public grammar agrees and "
            "declines, the Signature Word Method stands the adjective "
            "behind its noun: one form, every degree, sealed by helpers."
        ),
    },
    {
        "key": "pronouns",
        "name": "Malay Pronouns",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The full Malay pronoun system with example sentences. PERSONAL: "
            "saya (I, formal/polite): Saya tinggal di Kuala Lumpur. (I "
            "live in Kuala Lumpur.) aku (I, informal/intimate): Aku sayang "
            "kamu. (I love you.) awak (you, polite among peers): Awak sudah "
            "makan? (Have you eaten?) kamu (you, familiar): Kamu dari mana? "
            "(Where are you from?) anda (you, formal/written): Anda dialu-"
            "alukan. (You are welcome.) dia (he/she): Dia doktor. (He/She "
            "is a doctor.) ia (it/formal he/she): Ia penting. (It is "
            "important.) beliau (he/she, respectful): Beliau menteri. "
            "(He/She is a minister.) kita (we, inclusive of listener): Kita "
            "pergi sekarang. (We - you and I - go now.) kami (we, exclusive "
            "of listener): Kami pergi dulu. (We - not you - go first.) "
            "mereka (they): Mereka pelajar. (They are students.) POSSESSIVE "
            "suffixes: -ku (my, informal): bukuku (my book); -mu (your, "
            "informal): bukumu (your book); -nya (his/her/its/the): bukunya "
            "(his/her book / the book). Full possessives: buku saya (my "
            "book), kereta awak (your car), rumah mereka (their house). "
            "DEMONSTRATIVE: ini (this): Buku ini baru. (This book is new.) "
            "itu (that): Rumah itu jauh. (That house is far.) sini (here), "
            "situ (there, near listener), sana (there, far): Duduk sini. "
            "(Sit here.) Dia di sana. (He/She is over there.) "
            "INTERROGATIVE: apa (what): Apa ini? (What is this?) siapa "
            "(who): Siapa nama awak? (What is your name?) mana (where/which): "
            "Di mana tandas? (Where is the toilet?) bila (when): Bila awak "
            "datang? (When are you coming?) mengapa/kenapa (why): Mengapa "
            "awak lewat? (Why are you late?) bagaimana (how): Bagaimana "
            "cara ke sana? (How do I get there?) berapa (how many/much): "
            "Berapa harganya? (How much is it?)"
        ),
        "how_it_works": (
            "Malay pronouns are chosen by relationship, not by grammar: "
            "saya for respect, aku for intimacy, awak for peers, anda for "
            "formal writing. The famous split is kita versus kami - kita "
            "includes the listener, kami excludes them: Kita makan (let us "
            "- you and me - eat) against Kami makan (we - not you - eat). "
            "Mastering this split is mastering Malay politeness. Possession "
            "clips onto the noun as -ku, -mu, -nya for the informal set, "
            "while saya/awak/mereka stand as separate words. There is no "
            "he/she split: dia covers both, and context tells which. "
            "Practice by retelling your day three ways: formal (saya/"
            "awak), intimate (aku/kamu), and written (anda/beliau)."
        ),
        "key_points": [
            "Choose pronouns by relationship: saya (polite), aku (intimate), awak (peer), anda (formal written).",
            "kita includes the listener; kami excludes the listener - the politeness split of Malay.",
            "dia means he or she; context decides; beliau is the respectful form.",
            "Possessives are suffixes (-ku, -mu, -nya) or separate words (saya, awak, mereka).",
            "Interrogatives: apa, siapa, mana, bila, mengapa/kenapa, bagaimana, berapa.",
        ],
        "requirements": [
            "Produce the full personal pronoun chart from memory.",
            "Use kita and kami correctly in ten sentence pairs.",
            "Attach -ku, -mu, -nya to ten nouns and translate each.",
            "Write seven questions using each interrogative pronoun.",
            "Retell one event in formal (saya), intimate (aku), and written (anda) register.",
        ],
        "standards": [
            "Pronoun forms follow Kamus Dewan 4th ed. 2017.",
            "Usage distinctions follow Tatabahasa Dewan: Edisi Ketiga.",
            "Register guidance follows standard Malaysian usage.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the pronoun is a seal of relationship - "
            "saya the open hand, aku the bared heart, kita the shared "
            "covenant. Where public grammar lists persons, the Signature "
            "Word Method weighs them: include or exclude, and mean it."
        ),
    },
    {
        "key": "numbers",
        "name": "Malay Numbers and Time",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Malay numbers 1-100, ordinals, days, months, seasons, clock "
            "time, and dates, each with example sentences. CARDINALS: 1 "
            "satu, 2 dua, 3 tiga, 4 empat, 5 lima, 6 enam, 7 tujuh, 8 lapan "
            "(Indonesian: delapan), 9 sembilan, 10 sepuluh, 11 sebelas, 12 "
            "dua belas, 13 tiga belas, 20 dua puluh, 21 dua puluh satu, 30 "
            "tiga puluh, 40 empat puluh, 50 lima puluh, 100 seratus, 101 "
            "seratus satu, 200 dua ratus, 1000 seribu, 2000 dua ribu, "
            "1000000 sejuta. The pattern: teens are X belas, tens are X "
            "puluh, and se- replaces satu before ratus/ribu/juta (seratus, "
            "not satu ratus). Saya ada dua puluh ringgit. (I have twenty "
            "ringgit.) ORDINALS: pertama (first), kedua (second), ketiga "
            "(third) - ke- plus the cardinal: Bilik kedua. (The second "
            "room.) DAYS: Isnin (Monday), Selasa (Tuesday), Rabu "
            "(Wednesday), Khamis (Thursday), Jumaat (Friday), Sabtu "
            "(Saturday), Ahad (Sunday). Hari ini hari Isnin. (Today is "
            "Monday.) MONTHS: Januari, Februari, Mac, April, Mei, Jun, "
            "Julai, Ogos, September, Oktober, November, Disember. Saya lahir "
            "pada bulan Mei. (I was born in May.) SEASONS: Malaysia has two "
            "- musim hujan (rainy season) and musim kemarau (dry season) - "
            "plus the four-season words musim bunga (spring), musim panas "
            "(summer), musim luruh (autumn), musim sejuk (winter) for "
            "temperate lands. CLOCK: pukul marks the hour - pukul tiga (3 "
            "o'clock): Mesyuarat pada pukul tiga. (The meeting is at 3 "
            "o'clock.) Halves and quarters: pukul tiga setengah (3:30), "
            "pukul tiga suku (3:15), pukul empat kurang suku (3:45). Pagi "
            "(morning), tengah hari (midday), petang (afternoon), malam "
            "(night) disambiguate: pukul lapan malam (8 PM). DATES: 17 "
            "Oktober 2026 - tujuh belas Oktober dua ribu dua puluh enam."
        ),
        "how_it_works": (
            "Malay numbers build by strict pattern: units, then belas for "
            "11-19, puluh for tens, ratus for hundreds, ribu for thousands, "
            "juta for millions - and the se- form replaces satu before "
            "belas/ratus/ribu/juta (sebelas, seratus, seribu, sejuta). "
            "Counting nouns requires a classifier between number and noun: "
            "tiga buah buku (three books), lima orang pelajar (five "
            "students), dua ekor kucing (two cats). Time is pukul plus the "
            "number, with setengah for half past and suku for quarter. "
            "Dates run day-month-year: 17 Oktober 2026. Drill by counting "
            "everything you see - stairs, coins, minutes - in Malay, always "
            "with the classifier."
        ),
        "key_points": [
            "Teens are X belas, tens X puluh; se- replaces satu: sebelas, seratus, seribu, sejuta.",
            "Counting nouns needs a classifier: tiga buah buku, lima orang pelajar.",
            "Ordinals are ke- + cardinal, except pertama for first.",
            "Clock time is pukul + number + setengah/suku; pagi/petang/malam disambiguate.",
            "Days run Isnin to Ahad; months Januari to Disember; dates are day-month-year.",
        ],
        "requirements": [
            "Count 1-100 in Malay from memory with correct belas/puluh forms.",
            "Convert ten Arabic numerals to Malay words including ribu and juta.",
            "Give the seven days and twelve months in order.",
            "Tell six clock times including half past and quarter past.",
            "Write five dates in day-month-year Malay.",
        ],
        "standards": [
            "Number forms follow Kamus Dewan 4th ed. 2017.",
            "Classifier rules follow Tatabahasa Dewan: Edisi Ketiga.",
            "Month and day names follow the standard Malaysian usage.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: number is the first covenant - se- the "
            "seal of oneness before belas, ratus, ribu, juta. Where public "
            "arithmetic counts, the Signature Word Method witnesses: every "
            "noun counted with its classifier, every hour sealed with "
            "pukul."
        ),
    },
]

ENTRIES += [
    {
        "key": "greetings",
        "name": "Malay Greetings and Everyday Phrases",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Thirty Malay greetings, farewells, and politeness phrases with "
            "usage notes. TIME GREETINGS: 1. Selamat pagi (Good morning - "
            "until about 11 AM). 2. Selamat tengah hari (Good midday). 3. "
            "Selamat petang (Good afternoon/evening - until sunset). 4. "
            "Selamat malam (Good night - after dark, a greeting, not a "
            "farewell). 5. Selamat tidur (Sleep well - the actual bedtime "
            "farewell). CHECKING IN: 6. Apa khabar? (How are you? - "
            "literally what news?). 7. Khabar baik. (Good news - I am "
            "fine.) 8. Sihat? (Healthy? - casual how-are-you.) THANKS AND "
            "SORRY: 9. Terima kasih. (Thank you.) 10. Terima kasih "
            "banyak-banyak. (Thank you very much.) 11. Sama-sama. (You are "
            "welcome - literally same-same.) 12. Maaf. (Sorry/excuse me.) "
            "13. Maafkan saya. (Forgive me - stronger apology.) 14. Tidak "
            "mengapa. (It is nothing - never mind.) PLEASE: 15. Tolong. "
            "(Please - for requests.) 16. Silakan. (Please - offering or "
            "inviting: after you.) 17. Silakan masuk. (Please come in.) 18. "
            "Silakan duduk. (Please sit down.) FAREWELLS: 19. Jumpa lagi. "
            "(See you again.) 20. Selamat tinggal (Goodbye - said TO the "
            "person staying behind.) 21. Selamat jalan (Goodbye - said TO "
            "the person leaving.) WELCOME AND PRAISE: 22. Selamat datang. "
            "(Welcome.) 23. Tahniah. (Congratulations.) 24. Syabas. (Well "
            "done.) 25. Selamat hari jadi. (Happy birthday.) 26. Semoga "
            "berjaya. (Good luck - may you succeed.) INTRODUCTIONS: 27. "
            "Senang berjumpa dengan awak. (Nice to meet you.) 28. Nama saya "
            "... (My name is ...) 29. Saya dari ... (I am from ...) 30. "
            "Boleh saya bantu? (May I help? - the shopkeeper's question.) "
            "Usage note: strangers are greeted with a time-selamat plus a "
            "smile; Apa khabar? expects Khabar baik, never a complaint. "
            "Always say terima kasih - gratitude is the social currency of "
            "the archipelago."
        ),
        "how_it_works": (
            "Malay greetings are time-stamped: the selamat changes with "
            "the sun, so pagi, tengah hari, petang, and malam are not "
            "interchangeable - saying Selamat pagi at 3 PM marks you a "
            "beginner instantly. Tolong asks for help; silakan gives "
            "permission - never swap them. The two farewells split by "
            "who moves: the leaver says Selamat tinggal to the stayer, "
            "the stayer says Selamat jalan to the leaver. Practice by "
            "greeting the day in Malay from waking to sleep: Selamat pagi "
            "at breakfast, Selamat petang at tea, Selamat malam at dusk, "
            "Selamat tidur at bed."
        ),
        "key_points": [
            "Greetings are time-stamped: pagi, tengah hari, petang, malam follow the sun.",
            "Apa khabar? is answered with Khabar baik - never a complaint.",
            "Tolong requests help; silakan offers or invites - never swapped.",
            "Selamat tinggal is said to the stayer; Selamat jalan to the leaver.",
            "Terima kasih and sama-sama are the social currency - use them constantly.",
        ],
        "requirements": [
            "Produce all 30 phrases with English meanings from memory.",
            "Choose the correct selamat for six times of day.",
            "Demonstrate tinggal vs jalan in two farewell scenes.",
            "Hold a three-turn greeting exchange (greet, reply, thank).",
            "Introduce yourself fully: name, origin, nice-to-meet-you.",
        ],
        "standards": [
            "Phrase forms follow Kamus Dewan 4th ed. 2017.",
            "Usage notes follow standard Malaysian social convention.",
            "Time-greeting boundaries follow common Malaysian practice.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: every selamat a seal upon the hour - the "
            "greeting witnesses the sun. Where public phrasebooks list "
            "words, the Signature Word Method keeps the appointment: right "
            "greeting, right hour, gratitude sealed with terima kasih."
        ),
    },
    {
        "key": "grammar",
        "name": "Malay Grammar Essentials",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "The essential rules of Malay grammar, each with translated "
            "example sentences. WORD ORDER: subject-verb-object, as in "
            "English: Saya membaca buku. (I read a book.) Adjectives follow "
            "nouns: rumah besar (big house). Possessors follow nouns: buku "
            "saya (my book). GENDER: none - dia is he or she, guru is a "
            "male or female teacher. NUMBER: shown by reduplication or "
            "context, never by endings: buku-buku (books). ARTICLES: none "
            "- itu and ini often do the work of the: Buku itu mahal. (The "
            "book is expensive.) AFFIXES: meN- makes active verbs (tulis to "
            "menulis - to write), di- makes passives (ditulis - written), "
            "ber- marks states (kerja to bekerja - to work), ter- marks the "
            "accidental or superlative (terjatuh - fell accidentally; "
            "terbesar - biggest), peN- makes agent nouns (ajar to pengajar "
            "- teacher), -an makes nouns (makan to makanan - food), -kan "
            "and -i make causatives (duduk to dudukkan - to seat someone), "
            "ke-...-an makes abstracts (baik to kebaikan - goodness). "
            "NEGATION: tidak before verbs and adjectives - Saya tidak "
            "pergi. (I do not go.); bukan before nouns and pronouns - Ini "
            "bukan saya. (This is not me.) QUESTIONS: intonation alone "
            "(Awak lapar?), the -kah particle (Siapakah nama awak? - What "
            "is your name?), or question words (Di mana? - Where?). "
            "RELATIVE CLAUSES: yang introduces them - Buku yang saya baca "
            "itu menarik. (The book that I read is interesting.) Example "
            "summary sentences: Saya tidak makan daging. (I do not eat "
            "meat.) Buku yang merah itu saya punya. (The red book is mine.) "
            "Siapakah guru awak? (Who is your teacher?)"
        ),
        "how_it_works": (
            "Malay grammar is a small machine with few moving parts: one "
            "word order (SVO), no gender, no conjugation, no articles - and "
            "one big affix engine that builds verbs, nouns, and adjectives "
            "from roots. To say anything, pick the root, choose the affix "
            "for the job (meN- to do, di- to be done to, ber- to be, ter- "
            "for accident or most, peN- for the doer, -an for the thing), "
            "add tidak or bukan for no, and finish with -kah or a question "
            "word for questions. The yang clause is the sentence stretcher: "
            "anything you can say in a simple sentence, yang lets you bolt "
            "onto a noun. Practice by taking ten roots and running each "
            "through the full affix wheel."
        ),
        "key_points": [
            "Word order is SVO; adjectives, possessors, and demonstratives follow the noun.",
            "No gender, no conjugation, no articles - affixes do the grammatical work.",
            "The affix wheel: meN- (active), di- (passive), ber- (state), ter- (accidental/superlative), peN- (agent), -an (noun), -kan/-i (causative), ke-...-an (abstract).",
            "tidak negates verbs/adjectives; bukan negates nouns/pronouns.",
            "Questions use intonation, -kah, or question words; yang builds relative clauses.",
        ],
        "requirements": [
            "Diagram five sentences marking SVO order and post-noun modifiers.",
            "Run ten roots through the full affix wheel with translations.",
            "Negate ten sentences choosing tidak vs bukan correctly.",
            "Form five questions three ways: intonation, -kah, question word.",
            "Build five yang relative clauses from pairs of simple sentences.",
        ],
        "standards": [
            "Grammar rules follow Tatabahasa Dewan: Edisi Ketiga.",
            "Affix inventories follow the standard MABBIM-compatible account.",
            "Example forms follow Kamus Dewan 4th ed. 2017.",
        ],
        "citations": [CIT_TATA, CIT_MABBIM, CIT_KAMUS],
        "sig_lens": (
            "The Signature read: few parts, one engine - the affix wheel "
            "turns the root into every office of speech. Where public "
            "grammar memorizes tables, the Signature Word Method turns the "
            "wheel: root in, sealed word out."
        ),
    },
    {
        "key": "home_family",
        "name": "Malay Home and Family Sentences",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Malay sentences for house, rooms, furniture, and family "
            "members. 1. Ini rumah saya. (This is my house.) 2. Rumah kami "
            "ada empat bilik. (Our house has four rooms.) 3. Dapur kami "
            "besar dan bersih. (Our kitchen is big and clean.) 4. Bilik "
            "tidur saya di tingkat atas. (My bedroom is upstairs.) 5. Ruang "
            "tamu kami selesa. (Our living room is comfortable.) 6. Bilik "
            "air ada di sebelah dapur. (The bathroom is next to the "
            "kitchen.) 7. Meja makan diperbuat daripada kayu. (The dining "
            "table is made of wood.) 8. Sofa itu empuk. (That sofa is "
            "soft.) 9. Lampu bilik saya terang. (My room lamp is bright.) "
            "10. Tingkap itu menghadap taman. (That window faces the "
            "garden.) 11. Ayah saya bekerja di pejabat. (My father works "
            "in an office.) 12. Ibu saya pandai memasak. (My mother cooks "
            "well.) 13. Abang saya belajar di universiti. (My elder "
            "brother studies at university.) 14. Kakak saya sudah "
            "berkahwin. (My elder sister is married.) 15. Adik saya masih "
            "bersekolah. (My younger sibling still goes to school.) 16. "
            "Datuk dan nenek tinggal bersama kami. (Grandfather and "
            "grandmother live with us.) 17. Kami makan malam bersama-sama. "
            "(We eat dinner together.) 18. Anak saudara saya suka bermain "
            "di halaman. (My nephew/niece likes playing in the yard.) 19. "
            "Bilik adik saya kemas. (My younger sibling's room is tidy.) "
            "20. Keluarga saya bahagia. (My family is happy.) Family "
            "vocabulary notes: ayah/bapa (father), ibu/emak (mother), "
            "abang (elder brother), kakak (elder sister), adik (younger "
            "sibling), datuk (grandfather), nenek (grandmother), anak "
            "saudara (nephew/niece), sepupu (cousin), suami (husband), "
            "isteri (wife), anak (child)."
        ),
        "how_it_works": (
            "Home sentences run on location words - di (at/in), ke (to), "
            "dari (from) - plus the room nouns: Saya di dapur (I am in the "
            "kitchen), Dia ke bilik tidur (He/She goes to the bedroom). "
            "Family terms encode birth order: abang and kakak are always "
            "older than you, adik always younger - using them correctly "
            "shows respect and gets you treated as family. Possession is "
            "post-noun: bilik adik saya (my younger sibling's room, "
            "literally room younger-sibling my). Practice by drawing your "
            "house plan and labeling every room in Malay, then describing "
            "who does what in each room."
        ),
        "key_points": [
            "Room nouns: dapur, bilik tidur, ruang tamu, bilik air, halaman.",
            "Location prepositions: di (at), ke (to), dari (from).",
            "Family terms encode age rank: abang/kakak (elder), adik (younger).",
            "Possession stacks after the noun: bilik adik saya.",
            "Furniture adjectives follow the noun: meja makan, sofa empuk.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Label a house plan with ten Malay room and furniture words.",
            "Introduce your family using correct age-rank terms.",
            "Write five di/ke/dari location sentences about your home.",
            "Describe three rooms using post-noun adjectives.",
        ],
        "standards": [
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
            "Kinship terms follow standard Malay usage.",
            "Grammar follows Tatabahasa Dewan: Edisi Ketiga.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the house a sealed covenant - every room "
            "named, every elder ranked. Where public vocabulary furnishes, "
            "the Signature Word Method houses: abang above, adik below, "
            "the family sealed under one roof."
        ),
    },
    {
        "key": "food_cooking",
        "name": "Malay Food and Cooking Sentences",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Malay sentences for meals, ingredients, cooking actions, "
            "and restaurants. 1. Nasi ialah makanan ruji kami. (Rice is our "
            "staple food.) 2. Saya sarapan pada pukul tujuh. (I have "
            "breakfast at seven.) 3. Kami makan tengah hari di kantin. (We "
            "have lunch at the canteen.) 4. Ibu memasak rendang untuk makan "
            "malam. (Mother cooks rendang for dinner.) 5. Sambal ini pedas "
            "sangat. (This sambal is very spicy.) 6. Tolong tambahkan gula "
            "dalam teh. (Please add sugar to the tea.) 7. Saya tidak makan "
            "daging babi. (I do not eat pork.) 8. Ayam goreng ini rangup. "
            "(This fried chicken is crispy.) 9. Potong bawang dan cili. "
            "(Chop the onions and chilies.) 10. Tumis rempah hingga wangi. "
            "(Saute the spices until fragrant.) 11. Rebus telur selama "
            "sepuluh minit. (Boil the eggs for ten minutes.) 12. Kukus ikan "
            "dengan halia. (Steam the fish with ginger.) 13. Bakar sate di "
            "atas arang. (Grill the satay over charcoal.) 14. Hidangan ini "
            "cukup untuk lima orang. (This dish is enough for five people.) "
            "15. Boleh saya lihat menu? (May I see the menu?) 16. Saya mahu "
            "nasi lemak sebungkus. (I want one packet of nasi lemak.) 17. "
            "Teh tarik kurang manis, ya. (Teh tarik, less sweet, please.) "
            "18. Minta bil, tolong. (The bill, please.) 19. Makanan di sini "
            "halal. (The food here is halal.) 20. Jamuan itu meriah. (The "
            "feast was lively.) Cooking verbs: potong (cut), tumis (saute), "
            "rebus (boil), kukus (steam), bakar (grill/bake), goreng "
            "(fry), kacau (stir), hidang (serve)."
        ),
        "how_it_works": (
            "Food sentences are imperative-friendly: the bare verb plus "
            "the ingredient is a complete recipe step - Potong bawang "
            "(chop the onions). Restaurant Malay runs on three frames: "
            "Saya mahu ... (I want ...), Boleh saya ...? (May I ...?), and "
            "Berapa harganya? (How much?). Dietary needs are stated flatly "
            "with tidak: Saya tidak makan daging (I do not eat meat). "
            "Spice levels are negotiated with kurang/lebih: kurang pedas "
            "(less spicy). Practice by translating your favorite recipe "
            "into Malay imperatives, then ordering a full meal - drink, "
            "dish, bill - in a role-play."
        ),
        "key_points": [
            "Nasi is the staple; meals are sarapan, makan tengah hari, makan malam.",
            "Recipe steps are bare imperatives: Potong bawang, Tumis rempah.",
            "Restaurant frames: Saya mahu ..., Boleh saya ...?, Berapa harganya?",
            "Dietary needs use tidak: Saya tidak makan daging.",
            "Spice and sweetness are negotiated: kurang pedas, kurang manis.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Write a five-step recipe in Malay imperatives.",
            "Order a full meal in a role-play: drink, dish, bill.",
            "Name ten ingredients and eight cooking verbs from memory.",
            "State three dietary restrictions in polite Malay.",
        ],
        "standards": [
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
            "Food terms follow standard Malaysian usage.",
            "Imperative forms follow Tatabahasa Dewan: Edisi Ketiga.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the kitchen a sealed hearth - potong, "
            "tumis, hidang, each step witnessed. Where public menus list "
            "dishes, the Signature Word Method serves them: the recipe "
            "sealed in imperatives, the feast sealed in gratitude."
        ),
    },
]

ENTRIES += [
    {
        "key": "travel",
        "name": "Malay Travel and Directions Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Malay sentences for transport, asking directions, "
            "tickets, and lodging. 1. Di mana stesen bas? (Where is the bus "
            "station?) 2. Bagaimana cara ke Menara Kuala Lumpur? (How do I "
            "get to the Kuala Lumpur Tower?) 3. Jalan terus, kemudian belok "
            "kiri. (Go straight, then turn left.) 4. Berapa tambang ke "
            "lapangan terbang? (What is the fare to the airport?) 5. Saya "
            "mahu sewa kereta. (I want to rent a car.) 6. Bila bas "
            "seterusnya bertolak? (When does the next bus leave?) 7. "
            "Tiket ke Pulau Pinang berapa? (How much is a ticket to "
            "Penang?) 8. Saya mahu tiket pergi balik. (I want a return "
            "ticket.) 9. Kereta api itu tiba pukul sembilan. (The train "
            "arrives at nine.) 10. Teksi! Tolong hantar saya ke hotel ini. "
            "(Taxi! Please take me to this hotel.) 11. Berhenti di sini, "
            "tolong. (Stop here, please.) 12. Hotel ini ada bilik kosong? "
            "(Does this hotel have a vacant room?) 13. Berapa harga "
            "semalam? (What is the price per night?) 14. Saya mahu bilik "
            "dengan penghawa dingin. (I want a room with air "
            "conditioning.) 15. Pukul berapa daftar keluar? (What time is "
            "check-out?) 16. Di mana tandas awam? (Where is the public "
            "toilet?) 17. Bolehkah saya lihat peta? (May I see the map?) "
            "18. Tempat ini cantik sangat. (This place is very beautiful.) "
            "19. Saya sesat. Tolong tunjukkan jalan. (I am lost. Please "
            "show me the way.) 20. Selamat bercuti! (Have a good holiday!) "
            "Transport words: kapal terbang (airplane), kereta api "
            "(train), bas (bus), teksi (taxi), feri (ferry), motosikal "
            "(motorcycle), beca (trishaw), LRT/MRT (light rail)."
        ),
        "how_it_works": (
            "Direction Malay is built on three question frames - Di mana "
            "...? (Where is ...?), Bagaimana cara ke ...? (How to get to "
            "...?), Berapa ...? (How much ...?) - and three answer verbs: "
            "jalan terus (go straight), belok kiri/kanan (turn left/right), "
            "berhenti (stop). Tickets and rooms are negotiated with Saya "
            "mahu ... (I want ...) plus the classifier: sebuah bilik (a "
            "room), sekeping tiket (a ticket). Politeness rides on tolong "
            "and boleh: Berhenti di sini, tolong never fails. Practice by "
            "planning a real trip on a map and narrating every leg in "
            "Malay - transport, fare, arrival, room."
        ),
        "key_points": [
            "Three question frames cover all travel: Di mana ...?, Bagaimana cara ke ...?, Berapa ...?.",
            "Direction verbs: jalan terus, belok kiri/kanan, berhenti.",
            "Tickets and rooms use Saya mahu ... with classifiers: sekeping tiket, sebuah bilik.",
            "Tolong and boleh carry all politeness in travel Malay.",
            "Transport nouns: kapal terbang, kereta api, bas, teksi, feri, motosikal.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Ask for and give directions in a three-turn exchange.",
            "Buy a ticket and book a room in a role-play.",
            "Name eight transport modes from memory.",
            "Narrate a trip leg: transport, fare, arrival time.",
        ],
        "standards": [
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
            "Question frames follow Tatabahasa Dewan: Edisi Ketiga.",
            "Place-name usage follows standard Malaysian convention.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the road a signed covenant - di mana the "
            "question, jalan terus the answer. Where public phrasebooks "
            "point, the Signature Word Method travels: every fare sealed, "
            "every arrival witnessed."
        ),
    },
    {
        "key": "work_school",
        "name": "Malay Work and School Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Malay sentences for jobs, office, classroom, and "
            "learning. 1. Saya bekerja sebagai jurutera. (I work as an "
            "engineer.) 2. Pejabat saya di tingkat sepuluh. (My office is "
            "on the tenth floor.) 3. Mesyuarat bermula pukul sembilan. "
            "(The meeting starts at nine.) 4. Sila hantar laporan esok. "
            "(Please send the report tomorrow.) 5. Bos saya baik hati. (My "
            "boss is kind.) 6. Gaji dibayar setiap bulan. (Salary is paid "
            "every month.) 7. Saya ada temu duga esok. (I have an interview "
            "tomorrow.) 8. Kerja ini mencabar. (This work is challenging.) "
            "9. Rakan sekerja saya membantu. (My colleague is helpful.) "
            "10. Waktu rehat pada pukul satu. (Break time is at one.) 11. "
            "Saya belajar di sekolah menengah. (I study at secondary "
            "school.) 12. Cikgu mengajar matematik. (The teacher teaches "
            "mathematics.) 13. Murid-murid membaca buku teks. (The pupils "
            "read the textbook.) 14. Peperiksaan bermula minggu depan. (The "
            "examination starts next week.) 15. Saya mendapat markah "
            "tinggi. (I got high marks.) 16. Kerja rumah mesti siap malam "
            "ini. (Homework must be finished tonight.) 17. Perpustakaan "
            "buka sehingga pukul lima. (The library opens until five.) 18. "
            "Kelas bermula pada pukul lapan pagi. (Class starts at eight in "
            "the morning.) 19. Saya suka subjek sains. (I like the science "
            "subject.) 20. Belajar rajin-rajin untuk berjaya. (Study hard "
            "to succeed.) Job words: doktor (doctor), guru/cikgu (teacher), "
            "jurutera (engineer), peguam (lawyer), jururawat (nurse), "
            "polis (police), petani (farmer), nelayan (fisherman), peniaga "
            "(trader), penulis (writer)."
        ),
        "how_it_works": (
            "Work Malay is formal-register Malay: saya and anda replace "
            "aku and kamu, and requests wear sila or tolong - Sila hantar "
            "laporan (Please send the report). School Malay runs on the "
            "trio belajar/mengajar/peperiksaan (learn/teach/examination) "
            "and the time frame pada pukul (at o'clock). Job titles are "
            "built with peN-: ajar to pengajar, tulis to penulis, niaga to "
            "peniaga - the agent prefix turns the action into the actor. "
            "Practice by writing your CV headline in Malay, then "
            "describing your school day hour by hour."
        ),
        "key_points": [
            "Work Malay is formal: saya/anda, requests with sila or tolong.",
            "Job titles use peN-: pengajar, penulis, peniaga.",
            "School runs on belajar/mengajar/peperiksaan and pada pukul time frames.",
            "Meetings, reports, salary: mesyuarat, laporan, gaji.",
            "Encouragement is reduplication: rajin-rajin, baik-baik.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Write a CV headline and three job duties in Malay.",
            "Describe a school day hour by hour in Malay.",
            "Derive five job titles with peN- from verbs.",
            "Make five formal requests with sila/tolong in office scenes.",
        ],
        "standards": [
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
            "Affixation follows Tatabahasa Dewan: Edisi Ketiga.",
            "Register notes follow standard Malaysian formal usage.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the work a sealed deed - peN- the seal "
            "that turns the action into the actor. Where public CVs list "
            "titles, the Signature Word Method earns them: every duty "
            "witnessed, every lesson sealed."
        ),
    },
    {
        "key": "health_body",
        "name": "Malay Health and Body Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Malay sentences for body parts, symptoms, doctor "
            "visits, and pharmacy. BODY: 1. Kepala saya sakit. (My head "
            "hurts - I have a headache.) 2. Mata saya pedih. (My eyes "
            "sting.) 3. Tangan saya luka. (My hand is cut.) 4. Kaki saya "
            "bengkak. (My leg is swollen.) 5. Perut saya memulas. (My "
            "stomach cramps.) 6. Jantung berdegup kencang. (The heart beats "
            "fast.) SYMPTOMS: 7. Saya demam sejak semalam. (I have had a "
            "fever since yesterday.) 8. Saya batuk dan selsema. (I have a "
            "cough and a cold.) 9. Tekak saya perit. (My throat is sore.) "
            "10. Saya pening. (I feel dizzy.) 11. Badan saya lemah. (My "
            "body is weak.) DOCTOR: 12. Saya perlu jumpa doktor. (I need "
            "to see a doctor.) 13. Di mana klinik terdekat? (Where is the "
            "nearest clinic?) 14. Sudah berapa lama sakit? (How long has it "
            "hurt?) 15. Doktor memberi ubat. (The doctor gave medicine.) "
            "16. Saya alah kepada penisilin. (I am allergic to penicillin.) "
            "PHARMACY: 17. Di mana farmasi? (Where is the pharmacy?) 18. "
            "Makan ubat tiga kali sehari. (Take the medicine three times a "
            "day.) 19. Ubat ini sebelum makan. (This medicine before "
            "meals.) 20. Saya sudah sihat. (I am well now.) Body parts: "
            "kepala (head), rambut (hair), muka (face), mata (eye), hidung "
            "(nose), mulut (mouth), gigi (tooth), telinga (ear), leher "
            "(neck), bahu (shoulder), tangan (hand/arm), jari (finger), "
            "dada (chest), perut (stomach), belakang (back), kaki (leg/"
            "foot), lutut (knee)."
        ),
        "how_it_works": (
            "Symptom Malay is adjective Malay: the body part plus the "
            "feeling - Kepala saya sakit, Perut saya memulas. Duration "
            "uses sejak (since) and selama (for): sejak semalam, selama "
            "tiga hari. Medicine instructions are imperatives with "
            "frequency: Makan ubat tiga kali sehari, Ubat ini sebelum "
            "makan. Allergies are stated with alah kepada. Practice by "
            "describing a full clinic visit in order: symptom, duration, "
            "doctor's question, prescription, pharmacy pickup - twenty "
            "sentences, one visit."
        ),
        "key_points": [
            "Symptoms are body part + adjective: Kepala saya sakit.",
            "Duration uses sejak (since) and selama (for).",
            "Medicine instructions are imperatives with frequency: tiga kali sehari.",
            "Allergies: Saya alah kepada ...; the clinic question is Sudah berapa lama?",
            "Body parts: kepala to kaki - learn them head to toe in order.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Name fifteen body parts head to toe from memory.",
            "Describe five symptoms with duration (sejak/selama).",
            "Give three medicine instructions as imperatives.",
            "Role-play a full clinic visit in Malay.",
        ],
        "standards": [
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
            "Anatomical terms follow standard Malay usage.",
            "Imperative forms follow Tatabahasa Dewan: Edisi Ketiga.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the body a sealed vessel - kepala to "
            "kaki, every part named. Where public medicine charts symptoms, "
            "the Signature Word Method witnesses them: the pain spoken, "
            "the cure sealed."
        ),
    },
    {
        "key": "emotions",
        "name": "Malay Emotions and Feelings Sentences",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Malay sentences for happy, sad, angry, afraid, love, "
            "and surprise. HAPPY: 1. Saya gembira hari ini. (I am happy "
            "today.) 2. Dia tersenyum lebar. (He/She smiles broadly.) 3. "
            "Berita itu menggembirakan. (The news is delightful.) SAD: 4. "
            "Saya sedih mendengarnya. (I am sad to hear it.) 5. Dia menangis "
            "tersedu-sedu. (He/She weeps sobbingly.) 6. Hati saya hancur. "
            "(My heart is broken.) ANGRY: 7. Jangan marah. (Do not be "
            "angry.) 8. Dia naik angin. (He/She flared up - idiom: rose "
            "in wind.) 9. Saya bengang dengan dia. (I am annoyed with "
            "him/her - colloquial.) AFRAID: 10. Saya takut gelap. (I am "
            "afraid of the dark.) 11. Jangan takut, saya di sini. (Do not "
            "be afraid, I am here.) 12. Dia gementar. (He/She trembles.) "
            "LOVE: 13. Saya sayang awak. (I love you.) 14. Mereka saling "
            "mencintai. (They love each other.) 15. Cinta itu buta. (Love "
            "is blind.) SURPRISE AND MORE: 16. Saya terkejut! (I am "
            "surprised!) 17. Dia hairan melihat itu. (He/She is puzzled to "
            "see that.) 18. Saya bangga dengan awak. (I am proud of you.) "
            "19. Dia malu bertemu orang. (He/She is shy meeting people.) "
            "20. Tenanglah, semuanya baik-baik saja. (Calm down, everything "
            "is fine.) Feeling words: gembira (happy), sedih (sad), marah "
            "(angry), takut (afraid), sayang/cinta (love), terkejut "
            "(surprised), hairan (puzzled), bangga (proud), malu (shy/"
            "ashamed), tenang (calm), cemas (anxious), rindu (miss/long "
            "for)."
        ),
        "how_it_works": (
            "Emotion Malay centers on hati (heart/liver) as the seat of "
            "feeling: Hati saya hancur (my heart is broken), sakit hati (a "
            "wounded heart = resentment). Intensity is tuned with ter- "
            "(terkejut - startled, the accidental prefix doing emotional "
            "work) and reduplication (tersedu-sedu - sobbingly, "
            "baik-baik saja - just fine). Sayang is warm everyday love; "
            "cinta is the deep literary word. Comfort is imperative: "
            "Jangan takut, Tenanglah. Practice by keeping a one-line Malay "
            "feelings diary for a week - Saya gembira kerana ... - and "
            "watching the ter- forms multiply."
        ),
        "key_points": [
            "Hati is the seat of feeling: Hati saya hancur, sakit hati.",
            "ter- marks sudden emotion: terkejut, tergamam.",
            "sayang is everyday love; cinta is deep/literary love.",
            "Reduplication tunes intensity: tersedu-sedu, baik-baik saja.",
            "Comfort is imperative: Jangan takut, Tenanglah.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Name twelve feeling words with an example each.",
            "Build five hati idioms with translations.",
            "Write a seven-day feelings diary in Malay.",
            "Comfort a friend in three Malay sentences.",
        ],
        "standards": [
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
            "Idiom usage follows standard Malay convention.",
            "Affix forms follow Tatabahasa Dewan: Edisi Ketiga.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the heart the seal of feeling - hati "
            "hancur, hati tenang, every state witnessed. Where public "
            "psychology labels, the Signature Word Method feels: the "
            "emotion spoken, the comfort sealed."
        ),
    },
]

ENTRIES += [
    {
        "key": "nature_weather",
        "name": "Malay Nature and Weather Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Malay sentences for animals, plants, seasons, and "
            "weather talk. ANIMALS: 1. Kucing itu mengejar tikus. (The cat "
            "chases the mouse.) 2. Anjing menyalak kuat. (The dog barks "
            "loudly.) 3. Burung terbang tinggi. (The bird flies high.) 4. "
            "Gajah ialah haiwan terbesar di darat. (The elephant is the "
            "largest land animal.) 5. Harimau belang itu garang. (The "
            "striped tiger is fierce.) 6. Ikan berenang di sungai. (Fish "
            "swim in the river.) PLANTS: 7. Pokok kelapa tinggi melangit. "
            "(The coconut tree towers skyward.) 8. Bunga raya ialah bunga "
            "kebangsaan. (The hibiscus is the national flower.) 9. Padi "
            "menguning di sawah. (The rice yellows in the paddy field.) "
            "10. Daun gugur ditiup angin. (Fallen leaves are blown by the "
            "wind.) WEATHER: 11. Hari ini panas terik. (Today is scorching "
            "hot.) 12. Hujan turun dengan lebatnya. (The rain falls "
            "heavily.) 13. Langit mendung. (The sky is overcast.) 14. "
            "Petir berdentum. (Thunder rumbles.) 15. Pelangi muncul selepas "
            "hujan. (The rainbow appears after the rain.) 16. Angin "
            "sepoi-sepoi bahasa. (A gentle breeze blows.) SEASONS AND LAND: "
            "17. Musim hujan tiba. (The rainy season arrives.) 18. Banjir "
            "melanda kampung itu. (Flood struck that village.) 19. Gunung "
            "itu dilitupi kabus. (The mountain is covered in mist.) 20. "
            "Pantai ini bersih dan cantik. (This beach is clean and "
            "beautiful.) Nature words: hutan (forest), sungai (river), "
            "tasik (lake), laut (sea), pulau (island), bukit (hill), gunung "
            "(mountain), padang (field), langit (sky), bintang (star), "
            "bulan (moon), matahari (sun)."
        ),
        "how_it_works": (
            "Weather Malay is event Malay: the noun does the verb's work - "
            "Hujan turun (rain falls), Petir berdentum (thunder rumbles), "
            "Angin bertiup (wind blows). Intensity comes from reduplication "
            "and helpers: lebat (heavy), renyai (drizzle), terik "
            "(scorching), sepoi-sepoi (gentle). Animal sentences love the "
            "active meN- verbs: mengejar, menyalak, berenang. The famous "
            "weather small talk is Cuaca panas hari ini (hot weather today) "
            "- answered with agreement, never debate. Practice by narrating "
            "the sky each morning in three Malay sentences."
        ),
        "key_points": [
            "Weather is event Malay: Hujan turun, Petir berdentum, Angin bertiup.",
            "Intensity words: lebat, renyai, terik, sepoi-sepoi.",
            "Animal actions use active meN- verbs: mengejar, menyalak, berenang.",
            "Bunga raya is the national flower; padi/sawah anchor rural vocabulary.",
            "Two seasons: musim hujan and musim kemarau.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Name twelve animals and ten nature nouns from memory.",
            "Describe the weather in five sentences using intensity words.",
            "Write a morning-sky narration for seven days.",
            "Build five animal-action sentences with meN- verbs.",
        ],
        "standards": [
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
            "Nature terms follow standard Malay usage.",
            "Verb forms follow Tatabahasa Dewan: Edisi Ketiga.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the sky a signed witness - hujan turun, "
            "petir berdentum, every event sealed. Where public forecasts "
            "predict, the Signature Word Method beholds: the land named, "
            "the weather witnessed."
        ),
    },
    {
        "key": "shopping_money",
        "name": "Malay Shopping and Money Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Malay sentences for market, prices, bargaining, and "
            "paying. 1. Berapa harga baju ini? (How much is this shirt?) "
            "2. Lima puluh ringgit. (Fifty ringgit.) 3. Mahal sangat! "
            "Boleh kurang? (Too expensive! Can it be less?) 4. Harga "
            "terakhir berapa? (What is the final price?) 5. Boleh bagi "
            "diskaun? (Can you give a discount?) 6. Saya ambil dua helai. "
            "(I will take two pieces.) 7. Ada saiz lebih besar? (Is there a "
            "bigger size?) 8. Boleh cuba? (May I try it on?) 9. Warna merah "
            "ada? (Is there a red one?) 10. Ini terlalu kecil. (This is too "
            "small.) 11. Saya bayar dengan tunai. (I pay in cash.) 12. "
            "Boleh bayar dengan kad? (Can I pay by card?) 13. Beri saya "
            "resit, tolong. (Give me a receipt, please.) 14. Bakinya simpan "
            "sahaja. (Keep the change.) 15. Pasar malam buka setiap Sabtu. "
            "(The night market opens every Saturday.) 16. Sayur-sayur ini "
            "segar. (These vegetables are fresh.) 17. Ikan ini ditangkap "
            "pagi tadi. (This fish was caught this morning.) 18. Timbang "
            "sekilo, ya. (Weigh one kilo, please.) 19. Jumlahnya lapan "
            "belas ringgit. (The total is eighteen ringgit.) 20. Terima "
            "kasih, datang lagi! (Thank you, come again!) Money words: "
            "wang (money), ringgit (Malaysian dollar), sen (cent), harga "
            "(price), diskaun (discount), murah (cheap), mahal "
            "(expensive), tunai (cash), kad (card), resit (receipt), baki "
            "(change/balance), jumlah (total)."
        ),
        "how_it_works": (
            "Market Malay is bargaining Malay: Berapa harga ...? opens, "
            "Mahal sangat! counters, Boleh kurang? presses, and Harga "
            "terakhir berapa? closes. Quantities travel with classifiers: "
            "dua helai (two pieces of cloth/clothing), sekilo (one kilo), "
            "sebungkus (one packet). Paying is Saya bayar dengan ... "
            "(tunai/kad). The seller's close is Terima kasih, datang lagi "
            "- always smile, always return. Practice by haggling a full "
            "transaction in role-play: ask, counter twice, agree, pay, "
            "take the receipt."
        ),
        "key_points": [
            "The bargaining chain: Berapa harga? to Mahal sangat! to Boleh kurang? to Harga terakhir?",
            "Clothing uses helai; weight uses kilo; packets use bungkus.",
            "Payment frames: Saya bayar dengan tunai/kad; Beri saya resit.",
            "Night markets (pasar malam) are the bargaining arena.",
            "The seller closes with Terima kasih, datang lagi.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Haggle a full transaction in role-play with two counters.",
            "Name ten money and price words from memory.",
            "Buy three items using correct classifiers.",
            "Pay three ways: cash, card, keep-the-change.",
        ],
        "standards": [
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
            "Bargaining phrases follow standard Malaysian market usage.",
            "Classifier rules follow Tatabahasa Dewan: Edisi Ketiga.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the bargain a sealed covenant - asked, "
            "countered, closed. Where public markets haggle, the Signature "
            "Word Method trades: every price witnessed, every deal sealed "
            "with datang lagi."
        ),
    },
    {
        "key": "friendship",
        "name": "Malay Friendship and Social Life Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Malay sentences for meeting people, invitations, and "
            "celebrations. MEETING: 1. Hai! Lama tidak jumpa. (Hi! Long "
            "time no see.) 2. Senang berjumpa dengan awak. (Nice to meet "
            "you.) 3. Awak tinggal di mana? (Where do you live?) 4. Sudah "
            "berapa lama di sini? (How long have you been here?) 5. Kami "
            "sekampung. (We are from the same village.) 6. Dia kawan baik "
            "saya. (He/She is my good friend.) INVITATIONS: 7. Jom minum "
            "petang! (Let us have tea! - jom is the friendly let's.) 8. "
            "Datanglah ke rumah saya Sabtu ini. (Come to my house this "
            "Saturday.) 9. Saya jemput awak ke majlis kami. (I invite you "
            "to our event.) 10. Boleh bawa kawan? (May I bring a friend?) "
            "11. Pukul berapa mula? (What time does it start?) "
            "CELEBRATIONS: 12. Selamat hari jadi! (Happy birthday!) 13. "
            "Tahniah atas kejayaan awak! (Congratulations on your "
            "success!) 14. Selamat pengantin baharu! (Congratulations to "
            "the newlyweds!) 15. Rumah terbuka kami meriah. (Our open "
            "house was lively.) 16. Jamuannya sedap sangat. (The feast was "
            "very delicious.) SOCIAL GLUE: 17. Jom! (Let's go! - the "
            "friendliest word in Malay.) 18. Lepak jom. (Let's hang out.) "
            "19. Ceritalah. (Tell me about it.) 20. Kita jumpa lagi minggu "
            "depan. (We will meet again next week.) Social notes: friends "
            "are kawan; best friends kawan baik/rapat; hanging out is "
            "lepak; the open house (rumah terbuka) during festivals is the "
            "heart of Malay hospitality."
        ),
        "how_it_works": (
            "Friendship Malay runs on jom - the warm, irresistible let's "
            "that turns any plan into a shared one: Jom makan! (Let's "
            "eat!). Invitations soften with -lah: Datanglah (do come). "
            "Meeting someone new follows the script: greeting, name, "
            "origin (Dari mana?), common ground (Sekampung? Sekelas?). "
            "Celebrations have fixed formulas - Selamat hari jadi, "
            "Tahniah, Selamat pengantin baharu - delivered with both hands "
            "and a smile. Practice by inviting a friend to three events - "
            "tea, open house, birthday - and accepting one invitation with "
            "grace."
        ),
        "key_points": [
            "jom is the friendly let's: Jom makan!, Jom! - the warmest word in Malay.",
            "Invitations soften with -lah: Datanglah ke rumah saya.",
            "Meeting script: greeting, name, Dari mana?, common ground.",
            "Celebration formulas: Selamat hari jadi, Tahniah, Selamat pengantin baharu.",
            "Rumah terbuka (open house) is the heart of Malay hospitality.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Issue three invitations with jom and -lah.",
            "Run the meeting-someone-new script in role-play.",
            "Deliver the three celebration formulas correctly.",
            "Describe a rumah terbuka in five sentences.",
        ],
        "standards": [
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
            "Social formulas follow standard Malaysian convention.",
            "Imperative softening follows Tatabahasa Dewan: Edisi Ketiga.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: friendship the shared seal - jom the "
            "covenant of going together. Where public small talk passes "
            "time, the Signature Word Method keeps company: every "
            "invitation witnessed, every feast sealed."
        ),
    },
    {
        "key": "technology",
        "name": "Malay Technology and Communication Sentences",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Malay sentences for phone, internet, computer, and "
            "messaging. 1. Telefon saya kehabisan bateri. (My phone is out "
            "of battery.) 2. Ada Wi-Fi di sini? (Is there Wi-Fi here?) 3. "
            "Apakah kata laluannya? (What is the password?) 4. Internet "
            "lambat sangat. (The internet is very slow.) 5. Saya hantar "
            "mesej tadi. (I sent a message just now.) 6. Tolong angkat "
            "telefon. (Please pick up the phone.) 7. Talian sibuk. Cuba "
            "lagi. (The line is busy. Try again.) 8. Nombor awak berapa? "
            "(What is your number?) 9. Saya akan hubungi awak nanti. (I "
            "will contact you later.) 10. Panggilan video bermula pukul "
            "lapan. (The video call starts at eight.) 11. Komputer saya "
            "rosak. (My computer is broken.) 12. Fail itu sudah dimuat "
            "turun. (The file has been downloaded.) 13. Muat naik gambar "
            "itu. (Upload that picture.) 14. Skrin terlalu terang. (The "
            "screen is too bright.) 15. Papan kekunci tidak berfungsi. (The "
            "keyboard is not working.) 16. Saya terlupa kata laluan. (I "
            "forgot the password.) 17. Emel sudah dihantar. (The email has "
            "been sent.) 18. Balas mesej saya cepat. (Reply to my message "
            "quickly.) 19. Aplikasi ini mesra pengguna. (This app is "
            "user-friendly.) 20. Matikan telefon semasa mesyuarat. (Switch "
            "off phones during the meeting.) Tech words: telefon bimbit/"
            "telefon pintar (mobile/smartphone), komputer riba (laptop), "
            "internet, laman web (website), emel (email), mesej (message), "
            "aplikasi (app), kata laluan (password), muat turun (download), "
            "muat naik (upload), skrin (screen), papan kekunci (keyboard), "
            "tetikus (mouse)."
        ),
        "how_it_works": (
            "Tech Malay is built from Malay roots doing modern work: muat "
            "turun (load down = download), muat naik (load up = upload), "
            "kata laluan (word path = password), laman web (web page = "
            "website). Troubleshooting follows the symptom-cause-request "
            "chain: Komputer saya rosak (symptom), Internet lambat sangat "
            "(cause), Tolong baiki (request). The passive di- reports "
            "completed tech events: Fail sudah dimuat turun, Emel sudah "
            "dihantar. Practice by writing a three-step tech support "
            "script - problem, diagnosis, fix - entirely in Malay."
        ),
        "key_points": [
            "Tech terms are Malay-built: muat turun, muat naik, kata laluan, laman web.",
            "Troubleshooting chain: symptom, cause, request - Komputer rosak, tolong baiki.",
            "The di- passive reports completed events: sudah dimuat turun, sudah dihantar.",
            "Phone essentials: kehabisan bateri, talian sibuk, angkat telefon.",
            "Meeting etiquette: Matikan telefon semasa mesyuarat.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Name fifteen tech terms from memory.",
            "Write a three-step tech support script in Malay.",
            "Report five completed tech events with the di- passive.",
            "Ask for Wi-Fi and the password in a role-play.",
        ],
        "standards": [
            "Tech vocabulary follows Kamus Dewan 4th ed. 2017 and DBP tech term lists.",
            "Passive forms follow Tatabahasa Dewan: Edisi Ketiga.",
            "Usage follows standard Malaysian convention.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the signal a sealed thread - muat turun, "
            "muat naik, every packet witnessed. Where public tech "
            "borrows, the Signature Word Method builds: Malay roots, "
            "modern work, the message sealed."
        ),
    },
]

ENTRIES += [
    {
        "key": "verb_tenses",
        "name": "Malay Verb Tenses in Sentences",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Malay has no verb conjugation - aspect helper words carry all "
            "time meaning. PRESENT/HABITUAL (bare verb): 1. Saya makan nasi "
            "setiap hari. (I eat rice every day.) 2. Dia bekerja di bank. "
            "(He/She works at a bank.) 3. Mereka bermain bola petang ini. "
            "(They play ball this evening.) 4. Burung berkicau pada waktu "
            "pagi. (Birds chirp in the morning.) 5. Saya biasa bangun awal. "
            "(I usually wake up early.) PAST COMPLETED (sudah/telah + "
            "verb): 6. Saya sudah makan. (I have eaten.) 7. Dia telah tiba "
            "semalam. (He/She arrived yesterday.) 8. Kami sudah menonton "
            "filem itu. (We have watched that film.) 9. Mereka telah "
            "berkahwin. (They got married.) 10. Hujan sudah berhenti. (The "
            "rain has stopped.) ONGOING (sedang + verb, tengah in speech): "
            "11. Saya sedang membaca. (I am reading.) 12. Dia sedang "
            "memasak di dapur. (He/She is cooking in the kitchen.) 13. "
            "Mereka sedang berbincang. (They are discussing.) 14. Anak-anak "
            "sedang bermain. (The children are playing.) 15. Kami tengah "
            "makan - jangan ganggu. (We are eating - do not disturb. - "
            "colloquial.) FUTURE (akan + verb): 16. Saya akan pergi esok. "
            "(I will go tomorrow.) 17. Dia akan datang pukul tiga. (He/She "
            "will come at three.) 18. Kami akan bercuti bulan depan. (We "
            "will holiday next month.) 19. Harga akan naik. (Prices will "
            "rise.) 20. Saya akan hubungi awak. (I will contact you.) "
            "EXTRA SHADES: baru saja (just now - Saya baru saja sampai: I "
            "just arrived), masih belum (still not - Dia masih belum makan: "
            "He/She still has not eaten), pernah (ever - Pernahkah awak ke "
            "sana?: Have you ever been there?)."
        ),
        "how_it_works": (
            "The Malay time machine has four levers and no gears: leave "
            "the verb bare for present or habit, add sudah/telah for "
            "completed past, sedang for right-now ongoing, akan for "
            "future. The verb itself never moves - Saya makan stays Saya "
            "makan while the helper does the time travel. sudah is the "
            "everyday completed marker; telah is its formal written twin. "
            "tengah is the spoken twin of sedang. Stack pernah for life "
            "experience and baru saja for just-now. Practice by taking ten "
            "verbs and running each through all four levers plus the three "
            "extra shades - forty sentences, one unchanging verb."
        ),
        "key_points": [
            "Four levers, no conjugation: bare (present/habit), sudah/telah (completed), sedang (ongoing), akan (future).",
            "sudah is everyday; telah is formal written; tengah is spoken sedang.",
            "baru saja (just now), masih belum (still not), pernah (ever) add fine shades.",
            "The verb never changes - Saya makan in every tense frame.",
            "Time adverbs (semalam, esok, setiap hari) reinforce the helper.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Run ten verbs through all four levers with translations.",
            "Distinguish sudah/telah/tengah in five sentence pairs.",
            "Build five sentences each with baru saja, masih belum, pernah.",
            "Narrate yesterday, today, and tomorrow using only one verb root.",
        ],
        "standards": [
            "Aspect markers follow Tatabahasa Dewan: Edisi Ketiga.",
            "Usage distinctions follow standard Malay grammar.",
            "Example forms follow Kamus Dewan 4th ed. 2017.",
        ],
        "citations": [CIT_TATA, CIT_KAMUS, CIT_SNEd],
        "sig_lens": (
            "The Signature read: time the four-sealed lever - bare, "
            "sudah, sedang, akan. Where public grammar conjugates, the "
            "Signature Word Method keeps the verb unmoved: the helper "
            "witnesses the hour, the action stands sealed."
        ),
    },
    {
        "key": "questions_answers",
        "name": "Malay Questions and Answers",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Malay question-and-answer pairs covering who, what, "
            "where, when, why, and how. 1. Q: Siapa nama awak? (What is "
            "your name?) A: Nama saya Ahmad. (My name is Ahmad.) 2. Q: Apa "
            "ini? (What is this?) A: Ini buku. (This is a book.) 3. Q: Di "
            "mana awak tinggal? (Where do you live?) A: Saya tinggal di "
            "Johor. (I live in Johor.) 4. Q: Bila awak datang? (When are "
            "you coming?) A: Saya datang esok pagi. (I am coming tomorrow "
            "morning.) 5. Q: Mengapa awak lewat? (Why are you late?) A: "
            "Bas rosak. (The bus broke down.) 6. Q: Bagaimana awak ke sana? "
            "(How did you get there?) A: Saya menaiki teksi. (I took a "
            "taxi.) 7. Q: Berapa harganya? (How much is it?) A: Dua puluh "
            "ringgit. (Twenty ringgit.) 8. Q: Berapa orang datang? (How "
            "many people came?) A: Tiga puluh orang. (Thirty people.) 9. Q: "
            "Awak sudah makan? (Have you eaten?) A: Sudah, terima kasih. "
            "(Yes I have, thank you.) 10. Q: Dia datang ke? (Is he/she "
            "coming? - colloquial ke) A: Ya, dia datang. (Yes, he/she is "
            "coming.) 11. Q: Buku yang mana? (Which book?) A: Yang merah "
            "itu. (The red one.) 12. Q: Pukul berapa? (At what time?) A: "
            "Pukul tiga petang. (At 3 PM.) 13. Q: Kenapa tidak datang "
            "semalam? (Why did you not come yesterday?) A: Saya sakit. (I "
            "was sick.) 14. Q: Boleh saya duduk sini? (May I sit here?) A: "
            "Silakan. (Please do.) 15. Q: Awak faham? (Do you understand?) "
            "A: Faham sedikit. (I understand a little.) 16. Q: Ini punya "
            "siapa? (Whose is this?) A: Punya saya. (It is mine.) 17. Q: "
            "Berapa lama? (How long?) A: Dua jam. (Two hours.) 18. Q: "
            "Macam mana? (How? - colloquial) A: Macam ini. (Like this.) "
            "19. Q: Betul ke? (Really? - colloquial) A: Betul. (Really.) "
            "20. Q: Nak ikut? (Want to come along? - colloquial) A: Nak! "
            "(Yes!) Question tools: question words, the -kah particle "
            "(Siapakah? Apakah?), rising intonation, and colloquial ke."
        ),
        "how_it_works": (
            "Malay questions are built four ways: a question word up "
            "front (Siapa, Apa, Di mana), the -kah particle on the "
            "questioned word (Siapakah nama awak?), plain rising "
            "intonation (Awak lapar?), or the colloquial ke tag (Dia "
            "datang ke?). Answers are short and complete: Sudah for yes "
            "to a sudah-question, Belum for not yet, Tidak for no. "
            "Echo answers repeat the verb: Q: Awak pergi? A: Pergi. "
            "Practice by turning ten statements into questions all four "
            "ways, then answering each."
        ),
        "key_points": [
            "Four question builders: question words, -kah, intonation, colloquial ke.",
            "Answers echo the verb: Q: Awak pergi? A: Pergi.",
            "Sudah/Belum/Tidak answer completed-action questions.",
            "mana covers where and which: Di mana? Yang mana?",
            "Colloquial set: ke tag, macam mana, betul ke, nak.",
        ],
        "requirements": [
            "Translate all 20 Q/A pairs both directions.",
            "Turn ten statements into questions all four ways.",
            "Answer ten questions with echo, Sudah/Belum, and Tidak.",
            "Ask and answer where/which with mana in five pairs.",
            "Hold a five-turn information interview in Malay.",
        ],
        "standards": [
            "Question formation follows Tatabahasa Dewan: Edisi Ketiga.",
            "Colloquial forms are labeled as spoken Malay.",
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
        ],
        "citations": [CIT_TATA, CIT_KAMUS],
        "sig_lens": (
            "The Signature read: the question a seal broken open - siapa, "
            "apa, di mana, each a key. Where public drills interrogate, "
            "the Signature Word Method inquires: the question witnessed, "
            "the answer sealed."
        ),
    },
    {
        "key": "commands",
        "name": "Malay Commands and Requests",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Malay imperatives and polite requests, formal versus "
            "informal. FORMAL/POLITE (sila, tolong, -lah softener): 1. Sila "
            "duduk. (Please sit.) 2. Tolong tutup pintu. (Please close the "
            "door.) 3. Sila isi borang ini. (Please fill in this form.) 4. "
            "Tolong hantar saya ke lapangan terbang. (Please take me to "
            "the airport.) 5. Bacalah buku ini. (Do read this book. - "
            "-lah softens the command.) 6. Dengarlah nasihat ibu. (Do heed "
            "mother's advice.) 7. Jangan lupa bawa payung. (Do not forget "
            "to bring an umbrella.) 8. Sila tunggu sebentar. (Please wait "
            "a moment.) 9. Tolong beritahu saya. (Please tell me.) 10. "
            "Minumlah air banyak. (Do drink plenty of water.) INFORMAL/"
            "DIRECT (bare verb, friends and family): 11. Duduk! (Sit!) 12. "
            "Makan! (Eat!) 13. Cepat! (Hurry!) 14. Diam! (Be quiet!) 15. "
            "Tutup lampu. (Turn off the light.) 16. Buka tingkap. (Open "
            "the window.) 17. Datang sini. (Come here.) 18. Pergi sana. "
            "(Go there.) 19. Jangan main! (Do not play around!) 20. Sabar! "
            "(Be patient!) PROHIBITION: jangan + verb forbids - Jangan "
            "merokok (No smoking), Jangan masuk (Do not enter). The scale "
            "of softness: bare verb (order), -lah (urging), tolong (asking "
            "help), sila (formal inviting)."
        ),
        "how_it_works": (
            "The Malay command is the bare verb - Duduk!, Makan! - and "
            "softness is layered on: -lah turns an order into urging "
            "(Duduklah), tolong turns it into a request for help (Tolong "
            "duduk), sila turns it into formal invitation (Sila duduk). "
            "Jangan is the universal no: Jangan + any verb forbids it. "
            "Choose the layer by relationship: bare verbs for children and "
            "close friends, -lah for warm urging, tolong for strangers "
            "whose help you need, sila for offices and ceremonies. "
            "Practice by giving the same five orders at all four softness "
            "levels."
        ),
        "key_points": [
            "The command is the bare verb: Duduk!, Makan!, Tutup lampu.",
            "Softness scale: bare (order), -lah (urging), tolong (request), sila (formal).",
            "Jangan + verb is the universal prohibition: Jangan merokok.",
            "Choose the layer by relationship: bare for intimates, sila for ceremonies.",
            "Minumlah, Dengarlah - -lah attaches directly to the verb.",
        ],
        "requirements": [
            "Translate all 20 commands both directions.",
            "Give five orders at all four softness levels.",
            "Prohibit ten actions with jangan.",
            "Soften five bare commands with -lah.",
            "Direct a helper through a task using only tolong requests.",
        ],
        "standards": [
            "Imperative forms follow Tatabahasa Dewan: Edisi Ketiga.",
            "Register guidance follows standard Malaysian usage.",
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
        ],
        "citations": [CIT_TATA, CIT_KAMUS],
        "sig_lens": (
            "The Signature read: the command a sealed order - bare the "
            "verb, layered the mercy. Where public imperatives bark, the "
            "Signature Word Method measures: order, urging, request, "
            "invitation - each sealed to its station."
        ),
    },
    {
        "key": "descriptions",
        "name": "Malay Descriptions of People and Places",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty Malay sentences describing people, places, and things "
            "in detail. PEOPLE: 1. Dia seorang gadis yang cantik dan "
            "bijak. (She is a beautiful and clever girl.) 2. Lelaki tua "
            "itu berjanggut putih. (That old man has a white beard.) 3. "
            "Kanak-kanak itu bermata bulat. (The child has round eyes.) 4. "
            "Dia tinggi lampai dan berbadan tegap. (He/She is tall, slim, "
            "and sturdy.) 5. Senyumannya manis. (His/Her smile is sweet.) "
            "6. Suaranya lantang. (His/Her voice is loud and clear.) 7. Dia "
            "memakai baju batik biru. (He/She wears a blue batik shirt.) "
            "8. Rambutnya panjang dan hitam. (His/Her hair is long and "
            "black.) PLACES: 9. Kuala Lumpur ialah bandar yang sibuk. "
            "(Kuala Lumpur is a busy city.) 10. Kampung saya tenang dan "
            "damai. (My village is calm and peaceful.) 11. Pantai itu "
            "berpasir putih. (The beach has white sand.) 12. Hutan itu "
            "tebal dan gelap. (The forest is thick and dark.) 13. Sungai "
            "ini jernih. (This river is clear.) 14. Bangunan itu tinggi "
            "mencakar langit. (The building scrapes the sky.) THINGS: 15. "
            "Kereta baharu itu berkilat. (The new car gleams.) 16. Kuih ini "
            "manis dan lembut. (This cake is sweet and soft.) 17. Bau "
            "durian itu kuat. (The durian smell is strong.) 18. Kain songket "
            "ini berkilauan emas. (This songket cloth glitters gold.) 19. "
            "Rumah itu besar tetapi kosong. (The house is big but empty.) "
            "20. Malam ini dingin dan sunyi. (Tonight is cold and quiet.) "
            "Description tools: yang clauses (gadis yang cantik), ber- "
            "possession (berjanggut, bermata, berpasir), reduplicated "
            "softeners, tetapi contrasts."
        ),
        "how_it_works": (
            "Rich Malay description stacks three tools: the yang clause "
            "for defining detail (gadis yang cantik dan bijak), the ber- "
            "prefix for possessed features (berjanggut putih, bermata "
            "bulat, berpasir putih), and the tetapi pivot for contrast "
            "(besar tetapi kosong). Adjectives still follow their nouns; "
            "yang lets you chain as many as you like. Senses all get "
            "verbs: berkilat (gleams), berkilauan (glitters), manis "
            "(sweet). Practice by describing one person, one place, and "
            "one thing you love, each in five sentences using all three "
            "tools."
        ),
        "key_points": [
            "yang clauses chain detail: gadis yang cantik dan bijak.",
            "ber- marks possessed features: berjanggut, bermata, berpasir.",
            "tetapi pivots to contrast: besar tetapi kosong.",
            "Sense verbs enrich things: berkilat, berkilauan, manis.",
            "Adjectives still follow the noun, however long the chain.",
        ],
        "requirements": [
            "Translate all 20 sentences both directions.",
            "Describe a person in five sentences using yang and ber-.",
            "Describe a place in five sentences with a tetapi pivot.",
            "Describe a thing appealing to three senses.",
            "Expand five simple descriptions with yang clauses.",
        ],
        "standards": [
            "Description patterns follow Tatabahasa Dewan: Edisi Ketiga.",
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
            "Usage follows standard Malaysian descriptive convention.",
        ],
        "citations": [CIT_TATA, CIT_KAMUS],
        "sig_lens": (
            "The Signature read: description the sealed portrait - yang "
            "the brush, ber- the frame. Where public adjectives decorate, "
            "the Signature Word Method portrays: every feature witnessed, "
            "every contrast sealed."
        ),
    },
]

ENTRIES += [
    {
        "key": "story1",
        "name": "Malay Story I: A Day at the Market",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence simple story in Malay, present tense, with "
            "line-by-line English translation. 1. Pagi ini saya pergi ke "
            "pasar. (This morning I go to the market.) 2. Pasar itu sesak "
            "dengan orang. (The market is crowded with people.) 3. Saya "
            "membeli ikan, sayur, dan buah. (I buy fish, vegetables, and "
            "fruit.) 4. Penjual itu ramah dan murah hati. (The seller is "
            "friendly and generous.) 5. Saya tawar harga mangga. (I haggle "
            "over the price of the mangoes.) 6. Dia memberi diskaun "
            "sedikit. (He/She gives a small discount.) 7. Saya membayar "
            "dengan wang tunai. (I pay in cash.) 8. Dia membungkus barang "
            "dengan kemas. (He/She wraps the goods neatly.) 9. Saya "
            "mengucapkan terima kasih. (I say thank you.) 10. Saya pulang "
            "dengan hati gembira. (I return home happy.) Reading notes: "
            "every verb is bare present - pergi, membeli, membayar - "
            "because the story lives in the now. The closing line uses the "
            "classic dengan hati gembira (with a happy heart) story "
            "ending. Retell the story in your own words, then change one "
            "detail per sentence and retell again."
        ),
        "how_it_works": (
            "A present-tense story is a chain of bare verbs in time order: "
            "pergi, membeli, tawar, membayar, pulang. Malay needs no "
            "connectors between the links - sequence is meaning. Notice "
            "how the story teaches without teaching: sesak dengan orang "
            "(crowded with people) shows dengan doing with-work, memberi "
            "diskaun shows the verb + noun gift pattern, membungkus dengan "
            "kemas shows dengan doing manner-work. Read each line aloud, "
            "cover the English, translate, uncover, check. Then perform "
            "the story as a monologue."
        ),
        "key_points": [
            "Ten sentences, present tense, bare verbs in time order.",
            "dengan does double work: with (people) and manner (neatly).",
            "Market verbs in the wild: tawar, membayar, membungkus.",
            "The classic story closing: dengan hati gembira.",
            "Retell with changed details to own the pattern.",
        ],
        "requirements": [
            "Read the story aloud with correct stress throughout.",
            "Translate all ten lines both directions from memory.",
            "Retell the story changing one detail per sentence.",
            "Identify the function of dengan in each appearance.",
            "Write a parallel ten-sentence story about your morning.",
        ],
        "standards": [
            "Narrative forms follow standard Malay storytelling convention.",
            "Verb forms follow Tatabahasa Dewan: Edisi Ketiga.",
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
        ],
        "citations": [CIT_TATA, CIT_KAMUS],
        "sig_lens": (
            "The Signature read: the market day a sealed round - pergi to "
            "pulang, every link witnessed. Where public readers decode, "
            "the Signature Word Method walks: the story lived, the telling "
            "sealed."
        ),
    },
    {
        "key": "story2",
        "name": "Malay Story II: The Lost Wallet",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in Malay using past forms (sudah/telah), "
            "with line-by-line English translation. 1. Semalam saya telah "
            "kehilangan dompet. (Yesterday I lost my wallet.) 2. Saya sudah "
            "mencari di merata tempat. (I had searched everywhere.) 3. "
            "Hati saya cemas. (My heart was anxious.) 4. Tiba-tiba telefon "
            "berbunyi. (Suddenly the phone rang.) 5. Seorang lelaki telah "
            "menjumpai dompet saya. (A man had found my wallet.) 6. Dia "
            "menunggu di kedai kopi. (He was waiting at the coffee shop.) "
            "7. Saya berlari ke sana. (I ran there.) 8. Dia memulangkan "
            "dompet dengan senyuman. (He returned the wallet with a "
            "smile.) 9. Saya mengucapkan terima kasih banyak-banyak. (I "
            "thanked him very much.) 10. Kebaikan itu tidak akan saya "
            "lupakan. (I will never forget that kindness.) Reading notes: "
            "telah/sudah mark the completed past - telah kehilangan, sudah "
            "mencari. Tiba-tiba pivots the plot. The closing line uses the "
            "formal tidak akan ... lupakan vow pattern. Retell the story "
            "shifting every verb into the present, then back to past."
        ),
        "how_it_works": (
            "A past-tense story runs on sudah/telah plus time anchors: "
            "Semalam ... telah kehilangan sets the frame, and every "
            "completed action wears its marker. telah is the written "
            "formal marker - perfect for stories - while sudah is the "
            "spoken twin. Sequence words move the plot: tiba-tiba (plot "
            "twist), kemudian (then), akhirnya (finally). The moral "
            "closes with a vow: tidak akan ... lupakan. Practice by "
            "converting this story's ten lines between past and present "
            "until the markers feel automatic."
        ),
        "key_points": [
            "Past stories run on sudah/telah + time anchors like Semalam.",
            "telah is the formal story marker; sudah is its spoken twin.",
            "Tiba-tiba pivots the plot; akhirnya closes it.",
            "Passive di-/telah forms report found and returned things.",
            "The moral closes with a vow: tidak akan ... lupakan.",
        ],
        "requirements": [
            "Read the story aloud with correct stress throughout.",
            "Translate all ten lines both directions from memory.",
            "Convert the story between past and present twice.",
            "Mark every sudah/telah and state its function.",
            "Write a ten-sentence past-tense story of your own.",
        ],
        "standards": [
            "Narrative forms follow standard Malay storytelling convention.",
            "Aspect markers follow Tatabahasa Dewan: Edisi Ketiga.",
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
        ],
        "citations": [CIT_TATA, CIT_KAMUS],
        "sig_lens": (
            "The Signature read: the lost wallet a sealed parable - "
            "kehilangan to memulangkan, kindness witnessed. Where public "
            "readers follow plot, the Signature Word Method keeps faith: "
            "the loss sealed in memory, the kindness sealed in vow."
        ),
    },
    {
        "key": "story3",
        "name": "Malay Story III: Plans for Next Year",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A ten-sentence story in Malay using future and conditional "
            "forms, with line-by-line English translation. 1. Tahun depan "
            "saya akan melancong ke Sabah. (Next year I will travel to "
            "Sabah.) 2. Saya akan mendaki Gunung Kinabalu. (I will climb "
            "Mount Kinabalu.) 3. Jika cuaca baik, kami akan berkhemah. (If "
            "the weather is good, we will camp.) 4. Kalau hujan, kita akan "
            "menunggu di pondok. (If it rains, we will wait at the hut.) "
            "5. Saya akan membawa kamera baharu. (I will bring a new "
            "camera.) 6. Kami akan mencuba makanan tempatan. (We will try "
            "the local food.) 7. Saya harap perjalanan lancar. (I hope the "
            "journey goes smoothly.) 8. Mungkin kami akan menyelam di "
            "Sipadan. (Maybe we will dive at Sipadan.) 9. Semua ini akan "
            "menjadi kenangan indah. (All this will become beautiful "
            "memories.) 10. Saya tidak sabar menunggu! (I cannot wait!) "
            "Reading notes: akan marks every future verb - akan "
            "melancong, akan mendaki. Jika/kalau open conditions; harap "
            "and mungkin soften plans into hopes. The exclamation Saya "
            "tidak sabar menunggu is the classic eager closing. Retell "
            "the story as your own plan, swapping Sabah for your "
            "destination."
        ),
        "how_it_works": (
            "A future story is akan repeated down the plan list - akan "
            "melancong, akan mendaki, akan membawa - with jika/kalau "
            "branching the conditions and mungkin/harap softening the "
            "certainty. Malay future needs no will/shall split: one akan "
            "does it all. Conditionals pair jika with akan in the result "
            "clause. Practice by planning your own next year in ten "
            "akan-sentences, then adding one jika branch and one mungkin "
            "hedge."
        ),
        "key_points": [
            "Future stories chain akan: akan melancong, akan mendaki, akan membawa.",
            "Jika/kalau open conditions; the result clause keeps akan.",
            "Mungkin and harap soften plans into hopes.",
            "One akan does all future work - no will/shall split.",
            "Saya tidak sabar menunggu is the eager closing.",
        ],
        "requirements": [
            "Read the story aloud with correct stress throughout.",
            "Translate all ten lines both directions from memory.",
            "Plan your next year in ten akan-sentences.",
            "Add one jika branch and one mungkin hedge to the plan.",
            "Retell the story with a different destination.",
        ],
        "standards": [
            "Narrative forms follow standard Malay storytelling convention.",
            "Future and conditional forms follow Tatabahasa Dewan: Edisi Ketiga.",
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
        ],
        "citations": [CIT_TATA, CIT_KAMUS],
        "sig_lens": (
            "The Signature read: the plan a sealed promise - akan the "
            "witness of tomorrow. Where public futures hedge, the "
            "Signature Word Method vows: the journey sealed in hope, the "
            "memory sealed in advance."
        ),
    },
]

ENTRIES += [
    {
        "key": "idioms",
        "name": "Malay Idioms and Proverbs",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty Malay idioms and proverbs - literal translation, real "
            "meaning, and an example sentence each. 1. Seperti katak di "
            "bawah tempurung. (Like a frog under a coconut shell.) Means: "
            "narrow-minded, knowing little of the world. Dia seperti katak "
            "di bawah tempurung, tidak tahu perkembangan luar. 2. Bagai aur "
            "dengan tebing. (Like bamboo and riverbank.) Means: mutual help "
            "and dependence. Kita harus bagai aur dengan tebing. 3. Ada "
            "udang di sebalik batu. (There is a prawn behind the rock.) "
            "Means: a hidden motive. Tawarannya ada udang di sebalik "
            "batu. 4. Berat sama dipikul, ringan sama dijinjing. (Heavy "
            "loads carried together, light ones lifted together.) Means: "
            "share burdens fairly. 5. Hangat-hangat tahi ayam. (As warm as "
            "chicken droppings.) Means: short-lived enthusiasm. Semangatnya "
            "hangat-hangat tahi ayam sahaja. 6. Kacang lupakan kulit. (The "
            "peanut forgets its shell.) Means: ungrateful, forgetting "
            "one's origins. Jangan jadi kacang lupakan kulit. 7. Nasi sudah "
            "menjadi bubur. (The rice has become porridge.) Means: too late "
            "to fix. Nasi sudah menjadi bubur, terimalah. 8. Sediakan payung "
            "sebelum hujan. (Prepare the umbrella before the rain.) Means: "
            "prepare for trouble in advance. 9. Malu bertanya sesat jalan. "
            "(Too shy to ask, lost on the road.) Means: ask or go astray. "
            "10. Tong kosong nyaring bunyinya. (The empty barrel sounds "
            "loudest.) Means: empty vessels make the most noise. 11. "
            "Ikut resmi padi, makin berisi makin tunduk. (Follow the "
            "custom of rice: the fuller, the lower it bows.) Means: the "
            "wiser, the humbler. 12. Bulat air kerana pembetung, bulat "
            "manusia kerana muafakat. (Water is round because of its "
            "container; humans are united through consensus.) Means: unity "
            "through agreement. 13. Pagar makan padi. (The fence eats the "
            "rice.) Means: betrayal by a guardian. 14. Duri dalam daging. "
            "(A thorn in the flesh.) Means: a hidden enemy within. 15. "
            "Anjing menyalak bukit, takkan runtuh. (A dog barking at a "
            "hill will never topple it.) Means: futile opposition. 16. "
            "Gajah mati meninggalkan gading. (The dead elephant leaves its "
            "tusks.) Means: a legacy outlives the person. 17. Carik-carik "
            "bulu ayam, lama-lama bercantum juga. (Chicken feathers torn "
            "apart will join again.) Means: family quarrels heal. 18. Ukur "
            "baju di badan sendiri. (Measure the shirt on your own body.) "
            "Means: know your own limits. 19. Lidah tidak bertulang. (The "
            "tongue has no bone.) Means: words are cheap; the tongue wags "
            "freely. 20. Masuk bakul angkat sendiri. (Climbing into the "
            "basket to lift oneself.) Means: praising oneself."
        ),
        "how_it_works": (
            "Malay proverbs (peribahasa) compress whole philosophies into "
            "village images - frogs, rice, fences, barrels. Use them to "
            "season speech, never to start an argument: drop the proverb, "
            "let it land, move on. The classic frames are bagai/seperti "
            "(like) for similes and the bare statement for proverbs. Many "
            "pair opposites - berat/ringan, penuh/kosong - to balance the "
            "thought. Learn five at a time, use one per day in real "
            "conversation, and retire it once it feels natural."
        ),
        "key_points": [
            "Peribahasa compress philosophy into village images: frogs, rice, fences, barrels.",
            "Bagai/seperti frame similes; bare statements carry proverbs.",
            "Opposite-pairing balances thought: berat/ringan, penuh/kosong.",
            "Drop the proverb, let it land, move on - never argue with one.",
            "Five at a time, one per day in real conversation.",
        ],
        "requirements": [
            "Give all 20 idioms with literal meaning, real meaning, and example.",
            "Use five idioms correctly in conversation this week.",
            "Explain the image behind ten idioms.",
            "Match ten situations to their idioms.",
            "Write three original sentences using bagai/seperti frames.",
        ],
        "standards": [
            "Idiom forms follow standard Malay peribahasa collections.",
            "Meanings follow Kamus Dewan 4th ed. 2017 usage.",
            "Examples follow standard grammatical patterns.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the proverb a sealed chest - village "
            "image outside, whole philosophy within. Where public speech "
            "explains, the Signature Word Method seals: the image "
            "witnessed, the wisdom kept."
        ),
    },
    {
        "key": "registers",
        "name": "Malay Formal and Polite Registers",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen formal versus informal Malay pairs for letters, "
            "business, and elders, with translations. 1. Formal: Saya "
            "ingin memohon cuti. (I wish to apply for leave.) Informal: "
            "Aku nak cuti. (I wanna take leave.) 2. Formal: Terima kasih "
            "di atas kerjasama tuan. (Thank you for your cooperation, "
            "sir.) Informal: Terima kasih banyak. (Thanks a lot.) 3. "
            "Formal: Dengan hormatnya saya merujuk perkara di atas. (With "
            "respect I refer to the above matter. - the classic letter "
            "opening.) Informal: Pasal benda tu ... (About that thing "
            "...). 4. Formal: Sila ambil perhatian. (Please take note.) "
            "Informal: Ambil perhatian, ya. (Take note, okay.) 5. Formal: "
            "Saya tidak bersetuju. (I disagree.) Informal: Aku tak setuju. "
            "(I do not agree.) 6. Formal: Sudah (already). Informal: Dah. "
            "7. Formal: Tidak (no/not). Informal: Tak. 8. Formal: Belum "
            "(not yet). Informal: Lum. 9. Formal: Awak (you). Informal: "
            "Kau. 10. Formal: Saya (I). Informal: Aku. 11. Formal: "
            "Bagaimanakah keadaan kesihatan datuk? (How is grandfather's "
            "health?) Informal: Datuk sihat? (Grandpa healthy?) 12. "
            "Formal: Jemputlah datang ke majlis kami. (Do grace our event "
            "with your presence.) Informal: Jom datang! (Come along!) 13. "
            "Formal: Maafkan saya atas kelewatan. (Forgive me for the "
            "delay.) Informal: Maaf lambat. (Sorry late.) 14. Formal: Saya "
            "akan menghubungi pihak tuan. (I will contact your office.) "
            "Informal: Nanti aku telefon. (I will call later.) 15. Formal: "
            "Sekian, terima kasih. (That is all, thank you. - letter "
            "closing.) Informal: Okay, jumpa lagi. (Okay, see you.) "
            "Register rules: saya/anda/beliau and full forms for elders, "
            "officials, and writing; aku/kau and clipped forms (dah, tak, "
            "lum, nak) for peers, juniors, and intimates; never mix them "
            "in one sentence."
        ),
        "how_it_works": (
            "Malay register is a wardrobe: formal Malay (bahasa baku) for "
            "letters, ceremonies, and elders - full words, saya/anda, "
            "dengan hormatnya openings, sekian closings; colloquial Malay "
            "for friends - clipped words, aku/kau, lah particles. The "
            "shift is systematic: sudah to dah, tidak to tak, belum to "
            "lum, hendak to nak. Switching mid-sentence is the classic "
            "learner error - pick the wardrobe and wear it through the "
            "whole exchange. Practice by writing the same message twice: "
            "once to your boss, once to your best friend."
        ),
        "key_points": [
            "Formal: full words, saya/anda, dengan hormatnya ... sekian, terima kasih.",
            "Informal: clipped words (dah, tak, lum, nak), aku/kau, lah particles.",
            "Elders and officials always get the formal wardrobe.",
            "Never mix registers mid-sentence.",
            "The shift is systematic: sudah/dah, tidak/tak, belum/lum, hendak/nak.",
        ],
        "requirements": [
            "Translate all 15 pairs both directions.",
            "Write one message twice: to a boss and to a friend.",
            "Convert five formal sentences to colloquial.",
            "Address an elder correctly in a three-turn exchange.",
            "Open and close a formal letter correctly.",
        ],
        "standards": [
            "Formal forms follow standard bahasa baku convention.",
            "Letter formulas follow Malaysian official correspondence style.",
            "Colloquial forms are labeled as spoken Malay.",
        ],
        "citations": [CIT_TATA, CIT_KAMUS],
        "sig_lens": (
            "The Signature read: register the sealed wardrobe - baku for "
            "the elder, cakap for the friend. Where public speech dresses "
            "by habit, the Signature Word Method dresses by honor: the "
            "station witnessed, the word sealed to fit."
        ),
    },
    {
        "key": "complex",
        "name": "Malay Compound and Complex Sentences",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen long Malay sentences with clauses, connectors, and "
            "relative clauses - parsed and translated. 1. Saya pergi ke "
            "pasar kerana sayur di rumah sudah habis. (I go to the market "
            "because the vegetables at home are finished. - kerana = "
            "cause.) 2. Dia pandai tetapi malas. (He/She is clever but "
            "lazy. - tetapi = contrast.) 3. Walaupun hujan, kami tetap "
            "pergi. (Although it rained, we still went. - walaupun = "
            "concession.) 4. Buku yang saya beli semalam sangat menarik. "
            "(The book that I bought yesterday is very interesting. - yang "
            "= relative.) 5. Apabila dia tiba, kami makan bersama. (When "
            "he/she arrived, we ate together. - apabila = time.) 6. Belajar "
            "rajin-rajin supaya lulus peperiksaan. (Study hard so that you "
            "pass the examination. - supaya = purpose.) 7. Jika awak sakit, "
            "rehatlah di rumah. (If you are sick, rest at home. - jika = "
            "condition.) 8. Dia bekerja sementara anak-anak tidur. (He/She "
            "works while the children sleep. - sementara = simultaneous.) "
            "9. Kami tiba sebelum hujan turun. (We arrived before the rain "
            "fell. - sebelum = before.) 10. Dia menangis selepas menonton "
            "filem itu. (He/She cried after watching that film. - selepas "
            "= after.) 11. Harga naik, oleh itu kami berjimat. (Prices "
            "rose; therefore we economize. - oleh itu = result.) 12. Saya "
            "suka kopi manakala dia suka teh. (I like coffee whereas "
            "he/she likes tea. - manakala = whereas.) 13. Bukan sahaja dia "
            "pandai, malah dia rajin. (Not only is he/she clever, he/she "
            "is also hardworking. - bukan sahaja ... malah = not only ... "
            "but also.) 14. Semakin dia berlatih, semakin dia mahir. (The "
            "more he/she practices, the more skilled he/she becomes. - "
            "semakin ... semakin = the more ... the more.) 15. Walaupun "
            "penat, dia tetap tersenyum kerana tetamu sudah tiba. (Although "
            "tired, he/she still smiled because the guests had arrived. - "
            "triple connector: concession + cause.) Connector set: kerana/"
            "sebab (because), tetapi (but), walaupun (although), yang "
            "(that/which), apabila/ketika (when), supaya/agar (so that), "
            "jika/kalau (if), sementara (while), sebelum (before), selepas "
            "(after), oleh itu (therefore), manakala (whereas)."
        ),
        "how_it_works": (
            "Complex Malay sentences are built by bolting clauses together "
            "with connectors: pick the relationship (cause, contrast, "
            "time, condition, purpose), choose its connector, and place "
            "the subordinate clause before or after the main clause - "
            "Malay allows both. yang is the noun-bolter: it attaches a "
            "whole clause to a noun. semakin ... semakin builds the "
            "proportional pair. The triple-connector sentence is the "
            "mastery move: Walaupun penat (concede), dia tetap tersenyum "
            "(assert), kerana tetamu sudah tiba (explain). Practice by "
            "taking five simple sentence pairs and joining them with a "
            "different connector each time."
        ),
        "key_points": [
            "Connectors name the relationship: kerana (cause), tetapi (contrast), walaupun (concession).",
            "yang bolts a clause onto a noun: Buku yang saya beli.",
            "Subordinate clauses sit before or after the main clause.",
            "semakin ... semakin builds the more-the-more pair.",
            "The triple-connector sentence is the mastery move.",
        ],
        "requirements": [
            "Parse all 15 sentences naming each connector and clause.",
            "Join five sentence pairs with five different connectors.",
            "Build three yang relative clauses from scratch.",
            "Write two semakin ... semakin sentences.",
            "Compose one triple-connector sentence.",
        ],
        "standards": [
            "Connector usage follows Tatabahasa Dewan: Edisi Ketiga.",
            "Complex sentence patterns follow the standard grammar account.",
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
        ],
        "citations": [CIT_TATA, CIT_KAMUS],
        "sig_lens": (
            "The Signature read: the complex sentence a sealed chain - "
            "kerana the cause-link, tetapi the turn-link, yang the "
            "noun-link. Where public syntax diagrams, the Signature Word "
            "Method forges: every clause witnessed, the whole sealed."
        ),
    },
]

ENTRIES += [
    {
        "key": "conv_market",
        "name": "Malay Conversation: At the Market",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue at the market, annotated. "
            "Aina (buyer), Mak Cik Ros (seller). 1. Aina: Selamat pagi, mak "
            "cik! (Good morning, auntie! - mak cik is the respectful "
            "address for an older woman seller.) 2. Mak Cik: Selamat pagi, "
            "dik. (Good morning, dear. - dik softens to a younger "
            "customer.) 3. Aina: Mangga ini berapa sekilo? (How much are "
            "these mangoes per kilo?) 4. Mak Cik: Lapan ringgit sekilo, "
            "dik. Manis! (Eight ringgit a kilo, dear. Sweet!) 5. Aina: "
            "Mahal sangat. Enam ringgit boleh? (Too expensive. Six ringgit, "
            "can?) 6. Mak Cik: Enam tak boleh. Tujuh, harga terakhir. (Six "
            "cannot. Seven, final price.) 7. Aina: Baiklah, saya ambil dua "
            "kilo. (Alright, I will take two kilos.) 8. Mak Cik: Nah, pilih "
            "yang masak. (Here, choose the ripe ones. - nah hands "
            "over.) 9. Aina: Yang ini dan yang ini. (This one and this "
            "one.) 10. Mak Cik: Pandai pilih! (Good at choosing!) 11. Aina: "
            "Ikan kembung ada? (Any mackerel? - ada asks existence.) 12. "
            "Mak Cik: Ada, baru sampai pagi tadi. (There is, just arrived "
            "this morning.) 13. Aina: Berapa seekor? (How much each? - "
            "seekor, the animal classifier.) 14. Mak Cik: Tiga ringgit "
            "seekor. Ambil tiga, lapan ringgit. (Three ringgit each. Take "
            "three, eight ringgit.) 15. Aina: Baik, tiga ekor. (Good, "
            "three.) 16. Mak Cik: Jumlah lima belas ringgit. (Total fifteen "
            "ringgit.) 17. Aina: Nah, dua puluh. Bakinya simpan. (Here, "
            "twenty. Keep the change.) 18. Mak Cik: Wah, murah hati! Terima "
            "kasih, dik. (Wow, generous! Thank you, dear.) 19. Aina: "
            "Sama-sama. Saya pergi dulu, mak cik. (You are welcome. I will "
            "go first, auntie. - pergi dulu is the polite leavetaking.) 20. "
            "Mak Cik: Hati-hati, dik! Datang lagi! (Take care, dear! Come "
            "again!) Annotations cover: mak cik/dik address terms, nah "
            "handover, ada existence, seekor classifier, pergi dulu "
            "leavetaking, and the three-step bargain."
        ),
        "how_it_works": (
            "A market dialogue is a ritual in four moves: greet with the "
            "time-selamat plus the kinship address (mak cik, pak cik, "
            "dik), ask with Berapa ...?, bargain with Mahal sangat / "
            "Boleh kurang?, and close with Nah (handover), payment, and "
            "Datang lagi. The kinship addresses do the politeness work - "
            "never call a seller awak in a market. Perform this dialogue "
            "with a partner, then improvise the same four moves buying "
            "something else."
        ),
        "key_points": [
            "Four ritual moves: greet, ask, bargain, close.",
            "Kinship addresses (mak cik, pak cik, dik) do the politeness work.",
            "nah hands things over; ada asks existence; pergi dulu takes leave.",
            "seekor counts animals; sekilo weighs produce.",
            "The close is payment plus Datang lagi.",
        ],
        "requirements": [
            "Perform the dialogue with a partner, both roles.",
            "Translate all 20 lines both directions.",
            "Improvise the four moves buying a different item.",
            "Use mak cik/pak cik/dik correctly in three scenes.",
            "Bargain a price down twice in role-play.",
        ],
        "standards": [
            "Dialogue follows standard Malaysian market convention.",
            "Forms follow Tatabahasa Dewan: Edisi Ketiga.",
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the market talk a sealed ritual - greet, "
            "ask, bargain, close. Where public dialogues rehearse, the "
            "Signature Word Method trades: every move witnessed, the deal "
            "sealed with datang lagi."
        ),
    },
    {
        "key": "conv_friend",
        "name": "Malay Conversation: Meeting a Friend",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue meeting a friend, annotated. "
            "Hakim and Siti, old schoolmates. 1. Hakim: Eh, Siti! Lama "
            "tidak jumpa! (Hey, Siti! Long time no see! - eh is the warm "
            "surprise particle.) 2. Siti: Hakim! Ya Allah, dah lama! "
            "(Hakim! My goodness, it has been long! - colloquial dah.) 3. "
            "Hakim: Apa khabar? Sihat? (How are you? Healthy?) 4. Siti: "
            "Khabar baik. Awak pula? (Good news. And you?) 5. Hakim: Baik "
            "juga. Sekarang kerja di mana? (Good too. Where do you work "
            "now?) 6. Siti: Di hospital. Awak pula? (At the hospital. And "
            "you?) 7. Hakim: Saya di bank. Dah kahwin? (At the bank. "
            "Married yet? - dah ... ? asks completed life events.) 8. Siti: "
            "Dah, anak dua. (Yes, two children. - dah answers completed.) "
            "9. Hakim: Wah, cepat! Jom minum petang. (Wow, fast! Let us "
            "have tea. - jom moves to plans.) 10. Siti: Jom! Kedai mana? "
            "(Let us! Which shop?) 11. Hakim: Kedai Pak Mat, dekat sini. "
            "(Pak Mat's shop, near here.) 12. Siti: Oh, yang sedap tu. "
            "(Oh, the delicious one.) 13. Hakim: Bila awak lapang? (When "
            "are you free?) 14. Siti: Sabtu petang boleh? (Saturday "
            "afternoon, can?) 15. Hakim: Boleh. Pukul tiga. (Can. Three "
            "o'clock.) 16. Siti: Nanti saya bawa kuih. (Later I will bring "
            "cakes.) 17. Hakim: Wah, rajin! (Wow, industrious!) 18. Siti: "
            "Sikit-sikit sahaja. (Just a little. - the humble deflect.) "
            "19. Hakim: Okay, jumpa Sabtu! (Okay, see you Saturday!) 20. "
            "Siti: Jumpa Sabtu! Kirim salam keluarga! (See you Saturday! "
            "Send my regards to the family! - kirim salam is the warm "
            "close.) Annotations cover: eh surprise, dah/tak colloquial "
            "set, jom planning, the humble deflect, kirim salam closing."
        ),
        "how_it_works": (
            "A reunion dialogue runs the catch-up script: surprise (Eh!), "
            "health check (Apa khabar? Sihat?), life update (Kerja di "
            "mana? Dah kahwin?), plan (Jom minum petang), fix the time "
            "(Pukul tiga), close warm (Kirim salam). The colloquial set - "
            "dah, tak, jom - marks this as friends' talk, not office "
            "talk. The humble deflect (Sikit-sikit sahaja) answers praise "
            "without pride. Perform it, then run the same script meeting "
            "your own old friend."
        ),
        "key_points": [
            "The catch-up script: surprise, health, life update, plan, time, warm close.",
            "dah/tak/jom mark friends' talk, not office talk.",
            "Dah kahwin? asks completed life events; dah answers them.",
            "The humble deflect answers praise: Sikit-sikit sahaja.",
            "Kirim salam closes warmly.",
        ],
        "requirements": [
            "Perform the dialogue with a partner, both roles.",
            "Translate all 20 lines both directions.",
            "Run the catch-up script with a real or imagined friend.",
            "Use the colloquial set correctly in five sentences.",
            "Close three conversations with kirim salam.",
        ],
        "standards": [
            "Dialogue follows standard Malaysian social convention.",
            "Colloquial forms are labeled as spoken Malay.",
            "Forms follow Tatabahasa Dewan: Edisi Ketiga.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the reunion a sealed circle - eh the "
            "spark, jom the bond, kirim salam the close. Where public "
            "dialogues chat, the Signature Word Method reunites: every "
            "year witnessed, the friendship sealed."
        ),
    },
    {
        "key": "conv_problem",
        "name": "Malay Conversation: Solving a Problem",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A twenty-line bilingual dialogue solving a problem - a flat "
            "tire - annotated. Amir (driver), Encik Lee (mechanic). 1. "
            "Amir: Tolong! Tayar kereta saya pancit. (Help! My car tire is "
            "flat. - tolong opens emergencies.) 2. Encik Lee: Bertenang. "
            "Di mana sekarang? (Calm down. Where are you now? - bertenang "
            "is the calming command.) 3. Amir: Di tepi jalan, dekat "
            "simpang. (At the roadside, near the junction.) 4. Encik Lee: "
            "Okay, jangan alih kereta. (Okay, do not move the car.) 5. "
            "Amir: Berapa lama sampai? (How long until you arrive?) 6. "
            "Encik Lee: Dua puluh minit. (Twenty minutes.) 7. Amir: "
            "Berapa cajnya? (What is the charge?) 8. Encik Lee: Lima puluh "
            "ringgit termasuk tayar ganti. (Fifty ringgit including the "
            "spare tire.) 9. Amir: Boleh. Tolong cepat. (Okay. Please "
            "hurry.) 10. Encik Lee: Saya dalam perjalanan. (I am on the "
            "way.) 11. Amir: Encik sudah sampai? (Are you here yet?) 12. "
            "Encik Lee: Sudah. Buka bonet. (Yes. Open the trunk. - bonet "
            "holds the spare.) 13. Amir: Nah, kunci. (Here is the key.) "
            "14. Encik Lee: Tayar ini koyak teruk. (This tire is badly "
            "torn.) 15. Amir: Boleh baiki atau kena ganti? (Can it be "
            "repaired or must it be replaced?) 16. Encik Lee: Kena ganti. "
            "Nasib baik ada stok. (Must replace. Luckily there is stock. - "
            "nasib baik = luckily.) 17. Amir: Berapa lama baiki? (How long "
            "to fix?) 18. Encik Lee: Setengah jam siap. (Half an hour to "
            "finish.) 19. Amir: Terima kasih banyak, encik. (Thank you very "
            "much, sir.) 20. Encik Lee: Sama-sama. Pandu baik-baik! (You "
            "are welcome. Drive carefully! - baik-baik is the caring "
            "reduplication.) Annotations cover: tolong emergency open, "
            "bertenang calming, jangan alih instruction, nasib baik "
            "relief, baik-baik caring close."
        ),
        "how_it_works": (
            "A problem dialogue is a five-move rescue: cry for help "
            "(Tolong!), locate (Di mana?), diagnose (Berapa lama? Berapa "
            "caj?), direct (Jangan alih, Buka bonet), and thank "
            "(Terima kasih banyak). Questions stay short under stress; "
            "imperatives stay clear. The mechanic's bertenang and the "
            "driver's tolong frame the whole exchange in mutual respect - "
            "even in crisis, Malay stays polite. Practice by solving "
            "three problems - flat tire, lost phone, locked door - each "
            "in the five-move frame."
        ),
        "key_points": [
            "Five-move rescue: help, locate, diagnose, direct, thank.",
            "Tolong opens emergencies; bertenang calms them.",
            "Questions stay short under stress; imperatives stay clear.",
            "nasib baik marks relief; baik-baik marks caring.",
            "Politeness survives crisis: encik, tolong, terima kasih.",
        ],
        "requirements": [
            "Perform the dialogue with a partner, both roles.",
            "Translate all 20 lines both directions.",
            "Solve three problems in the five-move frame.",
            "Give five clear instructions under imagined pressure.",
            "Thank and close three rescue scenes correctly.",
        ],
        "standards": [
            "Dialogue follows standard Malaysian usage.",
            "Imperative forms follow Tatabahasa Dewan: Edisi Ketiga.",
            "Vocabulary follows Kamus Dewan 4th ed. 2017.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA],
        "sig_lens": (
            "The Signature read: the rescue a sealed covenant - tolong "
            "the cry, bertenang the answer. Where public phrasebooks "
            "panic, the Signature Word Method steadies: the problem "
            "witnessed, the solution sealed."
        ),
    },
    {
        "key": "mastery",
        "name": "Malay Mastery Review and Full Reference",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The consolidated quick-reference for the whole database: "
            "alphabet, 200 core words, key grammar, all phrase tables - "
            "the ladder in one teaching summary. ALPHABET: 26 Rumi letters "
            "a to z with Malay names (a, bi, si, di, i, ef, ji, eic, ai, "
            "je, ke, el, em, en, o, pi, kiu, ar, es, ti, iu, vi, dabeliu, "
            "eks, wai, zed); Jawi adds six letters (ca, nga, pa, ga, nya, "
            "va) to the Arabic set. 200 CORE WORDS: people (20): orang, "
            "lelaki, perempuan, kanak-kanak, ayah, ibu, abang, kakak, adik, "
            "datuk, nenek, anak, suami, isteri, kawan, guru, doktor, "
            "pelajar, jiran, tetamu; home (20): rumah, pintu, tingkap, "
            "meja, kerusi, katil, dapur, bilik, lampu, cermin, bantal, "
            "selimut, sofa, almari, dapur gas, peti sejuk, halaman, bumbung, "
            "tangga, kunci; food (20): nasi, air, makan, minum, lauk, "
            "sayur, buah, ikan, ayam, daging, telur, roti, gula, garam, "
            "sambal, kopi, teh, susu, kuih, restoran; verbs (30): makan, "
            "minum, tidur, bangun, pergi, datang, duduk, berdiri, berjalan, "
            "berlari, bercakap, mendengar, melihat, membaca, menulis, "
            "belajar, bekerja, bermain, membeli, menjual, memasak, mencuci, "
            "memandu, menaiki, memberi, mengambil, membuka, menutup, "
            "membawa, menunggu; adjectives (20): besar, kecil, panjang, "
            "pendek, tinggi, rendah, baru, lama, baik, buruk, cantik, "
            "panas, sejuk, cepat, lambat, kuat, mahal, murah, bersih, "
            "senang; adverbs (10): sangat, terlalu, selalu, jarang, "
            "kadang-kadang, perlahan-lahan, cepat-cepat, tiba-tiba, "
            "hampir, masih; pronouns (15): saya, aku, awak, kamu, anda, "
            "dia, ia, beliau, kita, kami, mereka, ini, itu, apa, siapa; "
            "numbers (15): satu, dua, tiga, empat, lima, enam, tujuh, "
            "lapan, sembilan, sepuluh, sebelas, dua puluh, seratus, seribu, "
            "sejuta; time (15): hari, minggu, bulan, tahun, pagi, petang, "
            "malam, pukul, Isnin, Jumaat, Ahad, Januari, Disember, semalam, "
            "esok; nature (15): air, api, tanah, langit, matahari, bulan, "
            "bintang, hujan, angin, pokok, bunga, hutan, sungai, laut, "
            "gunung; question words (10): apa, siapa, mana, bila, mengapa, "
            "kenapa, bagaimana, berapa, yang mana, macam mana; connectors "
            "(10): dan, tetapi, kerana, walaupun, jika, supaya, sebelum, "
            "selepas, sementara, oleh itu. KEY GRAMMAR: SVO order; "
            "adjectives/possessives/demonstratives follow the noun; no "
            "conjugation - sudah/telah (completed), sedang (ongoing), akan "
            "(future); tidak vs bukan; -kah questions; yang relatives; "
            "affix wheel meN-/di-/ber-/ter-/peN-/-an/-kan/-i/ke-...-an; "
            "reduplication for plurals; classifiers seorang/sebuah/seekor/"
            "sehelai/sebiji/sekeping. PHRASE TABLES: greetings (Selamat "
            "pagi, Selamat petang, Apa khabar?, Terima kasih, Sama-sama, "
            "Maaf, Tolong, Silakan, Jumpa lagi, Selamat jalan); travel (Di "
            "mana?, Berapa harganya?, Saya mahu ..., Tolong hantar saya "
            "...); feelings (Saya gembira, Saya sedih, Jangan marah, Saya "
            "takut, Saya sayang awak). Study counsel: read one record "
            "daily in ladder order, speak every sentence aloud, write ten "
            "new sentences per record, and retest with the demos until "
            "each prints OK."
        ),
        "how_it_works": (
            "Mastery is the ladder walked twice: first for exposure, "
            "second for ownership. Use this record as the map: the "
            "alphabet for spelling, the 200 words for recognition, the "
            "grammar for construction, the phrase tables for survival. "
            "Test yourself in rounds: round one, translate the 200 words "
            "both directions; round two, run the 30 verbs through the "
            "four time levers; round three, rebuild the 15 complex "
            "sentences from their connectors; round four, perform the "
            "three dialogues from memory. The demos are the examiners: "
            "each prints real computed values - affix derivations, stress "
            "placements, quiz scores - and every OK is a seal on that "
            "rung. When all 34 records read, all 68 demos pass, and the "
            "three stories retell in your own words, the ladder is "
            "climbed: you hold Malay from its alphabet to its arguments."
        ),
        "key_points": [
            "The 200 core words above are the recognition floor - translate them both directions.",
            "The 30 verbs through four time levers are the engine - run them until automatic.",
            "The phrase tables are survival Malay: greetings, travel, feelings, on demand.",
            "The 15 complex sentences are the ceiling: rebuild each from its connector.",
            "Climb the ladder twice: once for exposure, once for ownership - then retell the three stories.",
        ],
        "requirements": [
            "Translate all 200 core words Malay-to-English and back with 95 percent accuracy.",
            "Run the 30 core verbs through bare/sudah/sedang/akan.",
            "Perform the three dialogues from memory with a partner.",
            "Rebuild the 15 complex sentences from their connectors alone.",
            "Retell all three stories in your own words, keeping each story's tense spine.",
        ],
        "standards": [
            "Word lists consolidate the Kamus Dewan entries taught across records 1-33.",
            "Grammar summary consolidates the Tatabahasa Dewan rules taught across records 1-33.",
            "Reference tables follow the MABBIM spelling standard.",
        ],
        "citations": [CIT_KAMUS, CIT_TATA, CIT_MABBIM, CIT_ETHNO],
        "sig_lens": (
            "The Signature read: mastery is the fully signed covenant - "
            "the alphabet the first seal, the argument the last. Where "
            "public courses issue certificates, the Signature Word Method "
            "issues fluency: every word witnessed, every lever sworn, the "
            "whole tongue sealed in the learner's keeping."
        ),
    },
]
