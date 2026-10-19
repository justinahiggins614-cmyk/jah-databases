#!/usr/bin/env python3
"""Entries for the Persian to English databases (34 ladder-ordered records).

Public records: real, fact-checked Persian language teaching - every record
carries Persian content in the Perso-Arabic script with transliteration and
English translation plus example sentences, organized in the Signature
system. Persian (فارسی, ISO 639-1 fa, ISO 639-3 fas) is an Indo-European
language of the Iranian branch, written right to left in the Perso-Arabic
script, with about 70 million native speakers and roughly 110 million
speakers in total.

Screening: no hate-adjacent, profane, or inappropriate content; no
religious talk anywhere in these records.
"""
import textwrap

ENTRIES = []

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every language a covenant of meaning, every word a signed seal "
            "of its people, the ladder the oath between learner and tongue - "
            "clearly labeled Signature-made, never presented as authentic "
            "public record.")


def E(**kw):
    ENTRIES.append(kw)
    return kw


E(
    key="persian_overview", name="Persian Language Overview",
    group="Language overview", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Persian (فارسی, transliterated farsi) is an Indo-European language of
        the Iranian branch, spoken natively by about 70 million people and by
        roughly 110 million people in total. Its ISO codes are fa (639-1) and
        fas (639-3). The family path runs Indo-European > Indo-Iranian >
        Iranian > Western Iranian > Southwestern Iranian, which makes Persian
        a distant cousin of English, Spanish, Hindi, and Russian. It is the
        official language of Iran (as Farsi), Afghanistan (as Dari), and
        Tajikistan (as Tajiki). The three great written standards are Iranian
        Persian, Afghan Dari, and Tajik Tajiki - Tajiki is written in the
        Cyrillic alphabet, while Iranian and Afghan Persian use the
        Perso-Arabic script. Persian has a recorded literary history of about
        2,500 years, from Old Persian inscriptions through Middle Persian to
        the modern language, and its poetry tradition is one of the richest in
        the world. Example sentences in this record teach the facts as spoken
        language: من فارسی یاد می‌گیرم (man farsi yad migiram - I am learning
        Persian). فارسی زبان رسمی ایران است (farsi zabane rasmi-e iran ast -
        Persian is the official language of Iran). ما فارسی حرف می‌زنیم (ma
        farsi harf mizanim - we speak Persian). This record is the map of the
        whole database: what Persian is, where it lives, and how the ladder
        below carries a learner from a first greeting to full conversation."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the overview by anchoring every fact in a sentence
        the learner can say. Each fact - the native name فارسی, the ISO codes
        fa and fas, the family path, the speaker numbers, the three official
        countries, the two scripts - appears with a plain English explanation
        and a Persian example sentence. The learner reads the facts, then
        repeats the sentences, so the overview is spoken language from the
        first record. Later records climb the teaching ladder: foundations
        (records 1-10: sounds, words, grammar basics), compounded (records
        11-24: themed sentence sets and verb tenses), advanced (records
        25-34: stories, idioms, registers, complex sentences, conversations,
        and a full reference)."""),
    key_points=[
        "Native name: فارسی (farsi); English name: Persian; ISO 639-1: fa; ISO 639-3: fas.",
        "Family: Indo-European > Indo-Iranian > Iranian > Western Iranian > Southwestern Iranian.",
        "About 70 million native speakers; roughly 110 million speakers in total.",
        "Official in Iran, Afghanistan (as Dari), and Tajikistan (as Tajiki).",
        "Two scripts: Perso-Arabic in Iran and Afghanistan, Cyrillic for Tajiki in Tajikistan.",
        "Recorded history of about 2,500 years, from Old Persian to the modern language.",
        "Every record in this database carries Persian script, transliteration, and English translation.",
    ],
    requirements=[
        "No prior knowledge of Persian is needed; this is the starting record of the ladder.",
        "Learners should read each example sentence aloud to begin training pronunciation from day one.",
    ],
    standards=[
        "ISO 639-1:1988 (fa) and ISO 639-3:2007 (fas) language codes.",
        "Unicode Standard, Arabic block (U+0600-U+06FF) plus Arabic Supplement for Persian letters.",
    ],
    citations=[
        "Ethnologue: Languages of the World. 27th ed. SIL International; 2024. Speaker estimates for Persian varieties.",
        "Windfuhr, Gernot L. Persian Grammar: History and State of its Study. Mouton de Gruyter; 1979. The standard reference grammar of Persian.",
        "Academy of Persian Language and Literature (فرهنگستان زبان و ادب فارسی). Dasturn-e xatt-e farsi. Tehran; the official Persian orthography authority.",
    ],
    sig_lens=("Through the Signature lens, a language is not a school subject "
              "- it is a living covenant of meaning between peoples, and "
              "Persian is one of the great signed contracts of human history: "
              "seventy million native voices keeping one oath of meaning for "
              "two thousand five hundred years. This Signature reading treats "
              "the overview as the first seal of that contract."),
)

E(
    key="persian_writing", name="Persian Writing System",
    group="Language overview", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Persian is written right to left in the Perso-Arabic script with 32
        letters. The alphabet: ا (alef, a), ب (be, b), پ (pe, p), ت (te, t),
        ث (se, s), ج (jim, j), چ (che, ch), ح (he, h), خ (khe, kh), د (dal, d),
        ذ (zal, z), ر (re, r), ز (ze, z), ژ (zhe, zh), س (sin, s), ش (shin,
        sh), ص (sad, s), ض (zad, z), ط (ta, t), ظ (za, z), ع (eyn, a),
        غ (qeyn, q), ف (fe, f), ق (qaf, q), ک (kaf, k), گ (gaf, g), ل (lam,
        l), م (mim, m), ن (nun, n), و (vav, v/u), ه (he, h), ی (ye, y/i).
        The four letters پ چ ژ گ are Persian additions that Arabic does not
        have. Short vowels are usually not written in everyday text: ـَ (a),
        ـِ (e), ـُ (o). The long vowels are ا (a), ی (i), و (u). The ezafe
        linker ـِ connects a noun to its modifier: کتابِ من (ketab-e man -
        my book). Persian digits are ۰۱۲۳۴۵۶۷۸۹ (0-9), written left to right
        inside right-to-left text. Punctuation includes ، (comma), ؛
        (semicolon), and ؟ (question mark), all mirrored for right-to-left
        flow. Example sentences: این حرف پ است (in harf-e pe ast - this letter
        is pe). فارسی از راست به چپ نوشته می‌شود (farsi az rast be chap
        neweshte mishavad - Persian is written from right to left). من حروف
        فارسی را یاد می‌گیرم (man horuf-e farsi ra yad migiram - I am learning
        the Persian letters). Master the 32 letters and the vowel system, and
        every Persian word becomes pronounceable on sight."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the writing system letter by letter, each with its
        English transliteration so the learner can sound out any word. It
        explains the right-to-left direction, the four Persian-only letters,
        the short vowels that hide between the letters, the ezafe linker that
        chains nouns to their modifiers, the Persian digits, and the mirrored
        punctuation. Every rule is paired with a Persian sentence written in
        script, transliteration, and English, so reading and writing begin
        together. The working demonstration program validates the 32-letter
        inventory, transliterates sample words, and converts Western digits to
        Persian digits."""),
    key_points=[
        "Perso-Arabic script, written right to left, with 32 letters.",
        "Four Persian-only letters: پ (p), چ (ch), ژ (zh), گ (g).",
        "Short vowels (a, e, o) are usually unwritten in everyday text; long vowels are ا ی و.",
        "Ezafe ـِ links a noun to its modifier: کتاب من becomes کتابِ من in careful writing.",
        "Persian digits: ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹, written left to right.",
        "Punctuation is mirrored for right-to-left flow: ، ؛ ؟",
        "Sample sentence: فارسی از راست به چپ نوشته می‌شود - Persian is written from right to left.",
    ],
    requirements=[
        "Learners should copy each of the 32 letters by hand at least once.",
        "Practice reading the sample sentences right to left until the direction feels natural.",
    ],
    standards=[
        "Unicode Standard, Arabic block U+0600-U+06FF and Arabic Supplement U+0750-U+077F.",
        "Academy of Persian Language and Literature. Dasturn-e xatt-e farsi - official Persian orthography.",
    ],
    citations=[
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. The standard classroom introduction to the script and language.",
        "Academy of Persian Language and Literature (فرهنگستان زبان و ادب فارسی). Dasturn-e xatt-e farsi. Tehran; the official orthography authority.",
    ],
    sig_lens=("Through the Signature lens, the script is the seal-stamp of "
              "the covenant: thirty-two pressed marks, four of them Persian "
              "alone - pe, che, zhe, gaf - the signature no other script "
              "carries. This Signature reading treats every letter as a "
              "sworn stroke, learned by the hand before the mouth."),
)

E(
    key="persian_pronunciation", name="Persian Pronunciation and Phonology",
    group="Language overview", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Persian has 6 vowel qualities and 23 consonants, and - unlike Chinese
        or Vietnamese - it has no lexical tones: meaning never changes with
        pitch alone. The six vowels: ـَ (a, as in cat), ـِ (e, as in bed),
        ـُ (o, as in bought), ا (a, long as in father), ی (i, long as in
        machine), و (u, long as in boot). The consonants include the throaty
        خ (kh, as in Scottish loch), the uvular ق (q, made at the back of the
        throat), غ (gh, a voiced uvular fricative), چ (ch, as in church), and
        ژ (zh, as in measure). Stress falls on the final syllable of most
        words: کِتاب (keTAB - book), مادَر (maDAR - mother). In verb forms the
        stress falls on the prefix instead: می‌خورم (MIkhoram - I eat).
        Spoken examples with translations: آب (ab - water), نان (nan -
        bread), مادر (madar - mother), پدر (pedar - father), کتاب (ketab -
        book), مدرسه (madrese - school), درخت (derakht - tree), ماه (mah -
        moon), خورشید (khorshid - sun), دوست (dust - friend), خانه (khane -
        house), شهر (shahr - city). Example sentences: تلفظ فارسی آسان است
        (talaffoz-e farsi asan ast - Persian pronunciation is easy). استرس روی
        هجای آخر است (estres ruye heja-ye akhar ast - the stress is on the
        last syllable). من کلمات را بلند می‌خوانم (man kalemat ra boland
        mikhanam - I read the words aloud)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronunciation as a physical skill: each of the 6
        vowels and the trickiest consonants is anchored to an English
        approximation, then drilled with real words. It states the two stress
        rules - final-syllable stress for nouns and adjectives, prefix stress
        for verb forms - and gives more than ten spoken-example words with
        translations so the learner can shadow them aloud. The demonstration
        program encodes the vowel and consonant inventories, applies the
        stress rule to sample words, and quizzes the example vocabulary with
        tight-bounds assertions."""),
    key_points=[
        "6 vowel qualities (a, e, o, long a, i, u) and 23 consonants.",
        "No lexical tones: pitch never changes a word's meaning.",
        "Throaty sounds: خ (kh), ق (q), غ (gh); also چ (ch) and ژ (zh).",
        "Noun stress falls on the final syllable: keTAB, maDAR.",
        "Verb stress falls on the prefix: MIkhoram (I eat).",
        "Twelve spoken examples: آب، نان، مادر، پدر، کتاب، مدرسه، درخت، ماه، خورشید، دوست، خانه، شهر.",
        "Sample sentence: استرس روی هجای آخر است - the stress is on the last syllable.",
    ],
    requirements=[
        "Say each of the 12 example words aloud three times, exaggerating the stress.",
        "Record yourself and compare with a native speaker when possible.",
    ],
    standards=[
        "IPA transcription conventions per the Handbook of the International Phonetic Association.",
        "Windfuhr, Gernot L. Persian Grammar - phonology chapter as the reference inventory.",
    ],
    citations=[
        "Lazard, Gilbert. A Grammar of Contemporary Persian. Mazda Publishers; 1992. The reference grammar with full phonology.",
        "Mahootian, Shahrzad. Persian. Routledge; 1997. Descriptive grammar with pronunciation guidance.",
    ],
    sig_lens=("Through the Signature lens, pronunciation is the oath spoken "
              "aloud: six vowels and twenty-three consonants, no tones to "
              "hide behind, the stress falling like a seal on the final "
              "syllable. This Signature reading treats every sounded word as "
              "the covenant signed by the mouth."),
)

E(
    key="persian_nouns", name="Persian Core Nouns",
    group="Core vocabulary", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Twenty-five essential Persian nouns - person, place, and thing words -
        each with an example sentence in script, transliteration, and
        English. Persian has no grammatical gender, so nouns need no
        masculine/feminine memorization. 1. مرد (mard - man): آن مرد دوست من
        است (an mard dust-e man ast - that man is my friend). 2. زن (zan -
        woman): این زن معلم است (in zan moallem ast - this woman is a
        teacher). 3. کودک (kudak - child): کودک بازی می‌کند (kudak bazi
        mikonad - the child is playing). 4. دوست (dust - friend): او دوست من
        است (u dust-e man ast - he/she is my friend). 5. خانه (khane - house):
        خانه ما بزرگ است (khane-ye ma bozorg ast - our house is big). 6.
        مدرسه (madrese - school): مدرسه نزدیک است (madrese nazdik ast - the
        school is near). 7. کتاب (ketab - book): این کتاب جالب است (in ketab
        jaleb ast - this book is interesting). 8. آب (ab - water): آب سرد است
        (ab sard ast - the water is cold). 9. نان (nan - bread): نان تازه است
        (nan taze ast - the bread is fresh). 10. شهر (shahr - city): این شهر
        زیباست (in shahr zibast - this city is beautiful). 11. کشور (keshvar
        - country): ایران کشور من است (iran keshvar-e man ast - Iran is my
        country). 12. روز (ruz - day): امروز روز خوبی است (emruz ruz-e khubi
        ast - today is a good day). 13. شب (shab - night): شب آرام است (shab
        aram ast - the night is calm). 14. ماه (mah - moon/month): ماه در
        آسمان است (mah dar aseman ast - the moon is in the sky). 15. خورشید
        (khorshid - sun): خورشید می‌درخشد (khorshid miderakhshad - the sun is
        shining). 16. درخت (derakht - tree): درخت سبز است (derakht sabz ast -
        the tree is green). 17. گل (gol - flower): این گل قرمز است (in gol
        qermez ast - this flower is red). 18. ماشین (mashin - car): ماشین سریع
        است (mashin sari ast - the car is fast). 19. پول (pul - money): پول
        لازم است (pul lazem ast - money is needed). 20. وقت (vaqt - time):
        وقت طلاست (vaqt talast - time is gold). 21. کار (kar - work): کار من
        جالب است (kar-e man jaleb ast - my work is interesting). 22. غذا
        (qaza - food): غذا خوشمزه است (qaza khoshmazze ast - the food is
        delicious). 23. چای (chay - tea): چای داغ است (chay dagh ast - the
        tea is hot). 24. در (dar - door): در باز است (dar baz ast - the door
        is open). 25. پنجره (panjere - window): پنجره بزرگ است (panjere bozorg
        ast - the window is big). Plurals add ـها: کتاب‌ها (ketab-ha -
        books)."""),
    how_it_works=textwrap.dedent("""\
        This record builds the noun foundation with 25 high-frequency nouns,
        one spoken sentence each, because Persian nouns carry no gender and
        pluralize with a single rule - so the learner's energy goes into
        sentences, not endings. Each noun appears in script, transliteration,
        and English, inside a full sentence the learner can reuse by swapping
        the noun. The demonstration program stores the 25 nouns, generates
        their plurals with the ـها rule, and verifies every example sentence
        contains its noun."""),
    key_points=[
        "25 essential nouns: مرد، زن، کودک، دوست، خانه، مدرسه، کتاب، آب، نان، شهر، کشور، روز، شب، ماه، خورشید، درخت، گل، ماشین، پول، وقت، کار، غذا، چای، در، پنجره.",
        "No grammatical gender: nouns never change for masculine or feminine.",
        "Regular plural: add ـها (ha), as in کتاب‌ها (books).",
        "Each noun is taught inside a full spoken sentence, not alone.",
        "Sample sentence: خانه ما بزرگ است - our house is big.",
    ],
    requirements=[
        "Memorize all 25 nouns with their example sentences.",
        "Practice replacing the noun in each sentence with another noun from the list.",
    ],
    standards=[
        "Core vocabulary selected from high-frequency Persian word lists (Leeds and Tehran corpora).",
    ],
    citations=[
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Core vocabulary chapters.",
        "Mahootian, Shahrzad. Persian. Routledge; 1997. Nominal morphology and plural formation.",
    ],
    sig_lens=("Through the Signature lens, the noun is the first sworn "
              "thing: twenty-five named seals - man, woman, house, bread, "
              "book - each carrying its sentence like a signature carries "
              "its name. This Signature reading treats every noun as a "
              "covenant object, genderless and plain."),
)

E(
    key="persian_verbs", name="Persian Core Verbs",
    group="Core vocabulary", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Twenty-five essential Persian verbs, given as infinitives with an
        example sentence each in script, transliteration, and English.
        Persian verbs build from two stems (present stem and past stem); the
        infinitive ends in ـدن or ـتن. 1. خوردن (khordan - to eat): من نان
        می‌خورم (man nan mikhoram - I eat bread). 2. نوشیدن (nushidan - to
        drink): او چای می‌نوشد (u chay minushad - he/she drinks tea). 3.
        رفتن (raftan - to go): ما به مدرسه می‌رویم (ma be madrese miravim -
        we go to school). 4. آمدن (amadan - to come): او فردا می‌آید (u farda
        miayad - he/she comes tomorrow). 5. دیدن (didan - to see): من تو را
        می‌بینم (man to ra mibinam - I see you). 6. شنیدن (shenidan - to
        hear): صدا را می‌شنوم (seda ra mishenavam - I hear the sound). 7.
        گفتن (goftan - to say): او حرف می‌زند (u harf mizanad - he/she
        speaks). 8. خواندن (khandan - to read): من کتاب می‌خوانم (man ketab
        mikhanam - I read a book). 9. نوشتن (neveshtan - to write): او نامه
        می‌نویسد (u name minevisad - he/she writes a letter). 10. کردن
        (kardan - to do): من کار می‌کنم (man kar mikonam - I work / I do
        work). 11. شدن (shodan - to become): هوا سرد می‌شود (hava sard
        mishavad - the weather gets cold). 12. بودن (budan - to be): او خوشحال
        است (u khoshhal ast - he/she is happy). 13. داشتن (dashtan - to have):
        من یک کتاب دارم (man yek ketab daram - I have a book). 14. خواستن
        (khastan - to want): من آب می‌خواهم (man ab mikhaham - I want water).
        15. دانستن (danestan - to know): او فارسی می‌داند (u farsi midanad -
        he/she knows Persian). 16. گرفتن (gereftan - to take): کتاب را بگیر
        (ketab ra begir - take the book). 17. دادن (dadan - to give): به من
        بده (be man bedeh - give it to me). 18. خوابیدن (khabidan - to
        sleep): کودک می‌خوابد (kudak mikhabad - the child sleeps). 19. بیدار
        شدن (bidar shodan - to wake up): صبح زود بیدار می‌شوم (sobh-e zud
        bidar mishavam - I wake up early). 20. نشستن (neshastan - to sit):
        اینجا بنشین (inja benshin - sit here). 21. ایستادن (istadan - to
        stand): او ایستاده است (u istade ast - he/she is standing). 22. دویدن
        (davidan - to run): او سریع می‌دود (u sari midavad - he/she runs
        fast). 23. خریدن (kharidan - to buy): نان می‌خرم (nan mikharam - I
        buy bread). 24. فروختن (forukhtan - to sell): او ماشین را می‌فروشد (u
        mashin ra mifurushad - he/she sells the car). 25. یاد گرفتن (yad
        gereftan - to learn): من فارسی یاد می‌گیرم (man farsi yad migiram - I
        learn Persian). Present tense adds می‌ (mi-) to the present stem:
        می‌خورم، می‌روم، می‌بینم."""),
    how_it_works=textwrap.dedent("""\
        This record teaches verbs as the engine of the sentence: each of the
        25 verbs is given in its infinitive form with a full spoken example,
        so the learner hears the verb inside real word order from the start.
        It introduces the two-stem system and the می‌ (mi-) present prefix -
        the single most-used verb pattern in Persian. The demonstration
        program stores the 25 infinitives with their present stems, builds
        present-tense forms with the می‌ prefix, and verifies each example
        sentence contains its verb."""),
    key_points=[
        "25 essential verbs, each taught inside a full spoken sentence.",
        "Infinitives end in ـدن or ـتن: خوردن، رفتن، دیدن، کردن.",
        "Persian verbs build from a present stem and a past stem.",
        "Present tense: می‌ + present stem, as in می‌خورم (I eat).",
        "Sample sentence: من فارسی یاد می‌گیرم - I am learning Persian.",
    ],
    requirements=[
        "Memorize the 25 infinitives and be able to say each example sentence.",
        "Practice the می‌ present prefix on at least five verbs until it is automatic.",
    ],
    standards=[
        "Verb stems per Windfuhr, Persian Grammar - present/past stem classification.",
    ],
    citations=[
        "Lazard, Gilbert. A Grammar of Contemporary Persian. Mazda Publishers; 1992. Verb morphology and stem classes.",
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Verb lessons.",
    ],
    sig_lens=("Through the Signature lens, the verb is the oath in motion: "
              "twenty-five sworn actions - to eat, to go, to see, to learn - "
              "each carrying the می‌ seal of the living present. This "
              "Signature reading treats every verb as a covenant kept in "
              "real time."),
)

E(
    key="persian_adjectives_adverbs", name="Persian Adjectives and Adverbs",
    group="Core vocabulary", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Twenty-five Persian adjectives and fifteen adverbs, each inside an
        example sentence in script, transliteration, and English. Adjectives
        come AFTER the noun they describe, linked by the ezafe: خانه‌ی بزرگ
        (khane-ye bozorg - big house), دخترِ زیبا (dokhtar-e ziba - beautiful
        girl). Adjectives never change for gender or number. Comparatives add
        ـتر: بزرگ‌تر (bozorgtar - bigger); superlatives add ـترین:
        بزرگ‌ترین (bozorgtarin - biggest). Adjectives: 1. بزرگ (bozorg -
        big): خانه‌ی بزرگ (khane-ye bozorg - big house). 2. کوچک (kuchak -
        small): اتاقِ کوچک (otaq-e kuchak - small room). 3. خوب (khub -
        good): روزِ خوب (ruz-e khub - good day). 4. بد (bad - bad): هوای بد
        (hava-ye bad - bad weather). 5. جدید (jadid - new): کتابِ جدید
        (ketab-e jadid - new book). 6. قدیمی (qadimi - old): خانه‌ی قدیمی
        (khane-ye qadimi - old house). 7. زیبا (ziba - beautiful): گلِ زیبا
        (gol-e ziba - beautiful flower). 8. زشت (zesht - ugly): ساختمانِ زشت
        (sakhteman-e zesht - ugly building). 9. بلند (boland - tall/long):
        مردِ بلند (mard-e boland - tall man). 10. کوتاه (kutah - short): موی
        کوتاه (mu-ye kutah - short hair). 11. گرم (garm - warm/hot): چایِ گرم
        (chay-e garm - hot tea). 12. سرد (sard - cold): آبِ سرد (ab-e sard -
        cold water). 13. سریع (sari - fast): ماشینِ سریع (mashin-e sari -
        fast car). 14. کند (kond - slow): قطارِ کند (qatar-e kond - slow
        train). 15. آسان (asan - easy): درسِ آسان (dars-e asan - easy lesson).
        16. سخت (sakht - hard): کارِ سخت (kar-e sakht - hard work). 17. شاد
        (shad - happy): کودکِ شاد (kudak-e shad - happy child). 18. ناراحت
        (narahat - upset): او ناراحت است (u narahat ast - he/she is upset).
        19. تمیز (tamiz - clean): اتاقِ تمیز (otaq-e tamiz - clean room). 20.
        کثیف (kasif - dirty): لباسِ کثیف (lebas-e kasif - dirty clothes). 21.
        گران (geran - expensive): ماشینِ گران (mashin-e geran - expensive
        car). 22. ارزان (arzan - cheap): نانِ ارزان (nan-e arzan - cheap
        bread). 23. نزدیک (nazdik - near): مدرسه‌ی نزدیک (madrese-ye nazdik -
        near school). 24. دور (dur - far): شهرِ دور (shahr-e dur - far city).
        25. مهم (mohem - important): کارِ مهم (kar-e mohem - important work).
        Adverbs: 1. خیلی (kheyli - very): خیلی خوب (kheyli khub - very good).
        2. همیشه (hamishe - always): او همیشه می‌آید (u hamishe miayad -
        he/she always comes). 3. هرگز (hargez - never): هرگز دیر نمی‌کنم
        (hargez dir nemikonam - I am never late). 4. امروز (emruz - today):
        امروز هوا خوب است (emruz hava khub ast - today the weather is good).
        5. دیروز (diruz - yesterday): دیروز باران آمد (diruz baran amad - it
        rained yesterday). 6. فردا (farda - tomorrow): فردا می‌روم (farda
        miravam - I go tomorrow). 7. زود (zud - early/soon): زود بیا (zud biya
        - come early). 8. دیر (dir - late): دیر رسیدم (dir residam - I
        arrived late). 9. آهسته (aheste - slowly): آهسته حرف بزن (aheste harf
        bezan - speak slowly). 10. تند (tond - quickly): تند بدو (tond bodo -
        run quickly). 11. با هم (ba ham - together): با هم می‌رویم (ba ham
        miravim - we go together). 12. تنها (tanha - alone): تنها آمدم (tanha
        amadam - I came alone). 13. شاید (shayad - maybe): شاید باران بیاید
        (shayad baran biyayad - maybe it will rain). 14. حتماً (hatman -
        certainly): حتماً می‌آیم (hatman miayam - I will certainly come). 15.
        دوباره (dobare - again): دوباره بگو (dobare begu - say it again)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches description as placement: adjectives follow the
        noun with the ezafe linker, never changing for gender or number - so
        the learner masters one position rule and one comparative suffix. Each
        of the 25 adjectives and 15 adverbs is drilled inside a sentence, and
        the comparative ـتر and superlative ـترین are shown on real words.
        The demonstration program stores the adjective and adverb lists,
        builds comparative and superlative forms, and verifies the ezafe
        pattern in sample phrases."""),
    key_points=[
        "25 adjectives and 15 adverbs, each inside a full example sentence.",
        "Adjectives follow the noun with ezafe: خانه‌ی بزرگ (big house).",
        "No gender or number agreement on adjectives - one form for all.",
        "Comparative: ـتر (bozorgtar - bigger); superlative: ـترین (bozorgtarin - biggest).",
        "Sample: دخترِ زیبا - beautiful girl; خیلی خوب - very good.",
    ],
    requirements=[
        "Practice the adjective-after-noun order until English word order stops interfering.",
        "Build comparatives and superlatives for ten adjectives from the list.",
    ],
    standards=[
        "Ezafe construction per Lazard, A Grammar of Contemporary Persian - noun phrase chapter.",
    ],
    citations=[
        "Lazard, Gilbert. A Grammar of Contemporary Persian. Mazda Publishers; 1992. Adjective placement and comparison.",
        "Mahootian, Shahrzad. Persian. Routledge; 1997. Adverbial phrases.",
    ],
    sig_lens=("Through the Signature lens, the adjective is the seal of "
              "quality pressed after the noun: big-house, beautiful-girl, "
              "each description sworn in the right order. This Signature "
              "reading treats every modifier as a witness statement about "
              "the noun it follows."),
)

E(
    key="persian_pronouns", name="Persian Pronouns",
    group="Grammar basics", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Persian personal pronouns with full paradigms and example sentences
        in script, transliteration, and English. Subject pronouns: من (man -
        I), تو (to - you, informal), او (u - he/she), ما (ma - we), شما
        (shoma - you, formal/plural), آنها (anha - they). Persian has no
        gendered pronouns: او means both he and she. Example sentences: من
        دانشجو هستم (man daneshju hastam - I am a student). تو کجایی؟ (to
        koja-i? - where are you?). او معلم است (u moallem ast - he/she is a
        teacher). ما دوست هستیم (ma dust hastim - we are friends). شما لطف
        دارید (shoma lotf darid - you are kind, formal). آنها رفتند (anha
        raftand - they went). Object pronouns use را: من تو را دیدم (man to
        ra didam - I saw you). Possessive suffixes attach to the noun:
        کتابم (ketabam - my book), کتابت (ketabat - your book), کتابش
        (ketabash - his/her book), کتابمان (ketabeman - our book), کتابتان
        (ketabetan - your book, formal), کتابشان (ketabeshan - their book).
        Sentences: این کتاب من است (in ketab-e man ast - this is my book).
        خانه‌اش بزرگ است (khane-ash bozorg ast - his/her house is big).
        Demonstratives: این (in - this), آن (an - that), اینها (inha -
        these), آنها (anha - those). این چیست؟ (in chist? - what is this?). آن
        کتاب است (an ketab ast - that is a book). Interrogatives: کی (ki -
        who), چه (che - what), کجا (koja - where), چرا (chera - why), چگونه
        (chegune - how), کدام (kodam - which), چند (chand - how many). کی
        آمد؟ (ki amad? - who came?). چه می‌خواهی؟ (che mikhahi? - what do you
        want?). کجا می‌روی؟ (koja miravi? - where are you going?). چرا دیر
        کردی؟ (chera dir kardi? - why are you late?). Formality rule: use شما
        with strangers, elders, and in business; تو with friends, family, and
        children."""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronouns as a complete, closed system: six subject
        pronouns with no gender distinction, the را object marker, six
        possessive suffixes that weld to the noun, four demonstratives, and
        seven interrogatives. Each form is shown inside a sentence, and the
        formal/informal شما/تو rule is stated plainly because politeness is
        grammar in Persian. The demonstration program encodes the full
        paradigms, attaches possessive suffixes to sample nouns, and quizzes
        the interrogatives."""),
    key_points=[
        "Subject pronouns: من، تو، او، ما، شما، آنها - no gender distinction (او = he/she).",
        "Objects marked with را: من تو را دیدم - I saw you.",
        "Possessive suffixes weld to the noun: کتابم، کتابت، کتابش، کتابمان، کتابتان، کتابشان.",
        "Demonstratives: این (this)، آن (that)، اینها (these)، آنها (those).",
        "Interrogatives: کی، چه، کجا، چرا، چگونه، کدام، چند.",
        "Politeness rule: شما for strangers/elders/business, تو for friends/family.",
        "Sample: خانه‌اش بزرگ است - his/her house is big.",
    ],
    requirements=[
        "Drill the six subject pronouns and six possessive suffixes until automatic.",
        "Practice switching شما/تو pairs to feel the formality difference.",
    ],
    standards=[
        "Pronominal system per Mahootian, Persian - pronouns and clitics chapter.",
    ],
    citations=[
        "Mahootian, Shahrzad. Persian. Routledge; 1997. Pronouns, clitics, and politeness.",
        "Lazard, Gilbert. A Grammar of Contemporary Persian. Mazda Publishers; 1992. Deictics and interrogatives.",
    ],
    sig_lens=("Through the Signature lens, the pronoun is the oath of "
              "address: من and تو and the careful شما, each one choosing how "
              "the speaker stands before the other. This Signature reading "
              "treats the formal شما as a bow written into grammar."),
)

E(
    key="persian_numbers_time", name="Persian Numbers and Time",
    group="Grammar basics", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Persian numbers 1 to 100, ordinals, days, months, seasons, clock time,
        and dates - each with example sentences in script, transliteration,
        and English. Cardinal numbers: ۱ یک (yek - one), ۲ دو (do - two), ۳
        سه (se - three), ۴ چهار (chahar - four), ۵ پنج (panj - five), ۶ شش
        (shesh - six), ۷ هفت (haft - seven), ۸ هشت (hasht - eight), ۹ نه (noh
        - nine), ۱۰ ده (dah - ten), ۱۱ یازده (yazdah), ۱۲ دوازده (davazdah),
        ۱۳ سیزده (sizdah), ۱۴ چهارده (chahardah), ۱۵ پانزده (panzdah), ۱۶
        شانزده (shanzdah), ۱۷ هفده (hefdah), ۱۸ هجده (hejdah), ۱۹ نوزده
        (nuzdah), ۲۰ بیست (bist), ۳۰ سی (si), ۴۰ چهل (chehel), ۵۰ پنجاه
        (panjah), ۶۰ شصت (shast), ۷۰ هفتاد (haftad), ۸۰ هشتاد (hashtad), ۹۰
        نود (navad), ۱۰۰ صد (sad). Compounds join with و: ۲۱ بیست و یک
        (bist-o-yek - twenty-one), ۴۵ چهل و پنج (chehel-o-panj -
        forty-five). Ordinals: اول (avval - first), دوم (dovvom - second),
        سوم (sevvom - third), then ـمین: چهارمین (chaharomin - fourth),
        پنجمین (panjomin - fifth). Days of the week (the week starts
        Saturday): شنبه (shanbe - Saturday), یکشنبه (yekshanbe - Sunday),
        دوشنبه (doshanbe - Monday), سه‌شنبه (seshanbe - Tuesday), چهارشنبه
        (chaharshanbe - Wednesday), پنج‌شنبه (panjshanbe - Thursday), جمعه
        (jome - Friday). Solar Hijri months: فروردین (farvardin)، اردیبهشت
        (ordibehesht)، خرداد (khordad)، تیر (tir)، مرداد (mordad)، شهریور
        (shahrivar)، مهر (mehr)، آبان (aban)، آذر (azar)، دی (dey)، بهمن
        (bahman)، اسفند (esfand). Seasons: بهار (bahar - spring)، تابستان
        (tabestan - summer)، پاییز (paiz - autumn)، زمستان (zemestan -
        winter). Clock time: ساعت سه است (saat-e se ast - it is three
        o'clock), ساعت سه و نیم (saat-e se-o-nim - half past three), ساعت
        چهار و ربع (saat-e chahar-o-rob - quarter past four). Dates: امروز ۲۵
        مهر ۱۴۰۵ است (emruz 25-e mehr-e 1405 ast - today is the 25th of Mehr,
        1405). Example sentences: من دو کتاب دارم (man do ketab daram - I
        have two books). او سوم شد (u sevvom shod - he/she came third). جمعه
        تعطیل است (jome tatil ast - Friday is a holiday). تولدم در بهار است
        (tavallodam dar bahar ast - my birthday is in spring)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches counting as a tool: the 1-10 base, the teens, the
        tens, and the و-compounding rule that builds any number to 100, then
        ordinals, the Saturday-starting week, the twelve Solar Hijri months,
        the four seasons, clock expressions, and full dates. Every item is
        shown in Persian digits, script, transliteration, and English, with
        sentences that spend the numbers in real life - buying books, telling
        time, naming birthdays. The demonstration program converts between
        Western and Persian digits, builds numbers 1-100 from parts, and
        quizzes ordinals and time expressions."""),
    key_points=[
        "Numbers 1-100: base 1-10, teens 11-19, tens 20-90, compounds with و (بیست و یک).",
        "Persian digits ۰-۹; ۱۴۰۵ is written with Persian digits in dates.",
        "Ordinals: اول، دوم، سوم، then ـمین (چهارمین).",
        "Week starts Saturday: شنبه تا جمعه; Friday (جمعه) is the weekend day.",
        "Twelve Solar Hijri months: فروردین تا اسفند; four seasons: بهار، تابستان، پاییز، زمستان.",
        "Clock: ساعت سه و نیم (half past three); dates: ۲۵ مهر ۱۴۰۵.",
        "Sample: من دو کتاب دارم - I have two books.",
    ],
    requirements=[
        "Count aloud from 1 to 100 in Persian without stopping.",
        "Say today's date and the time in Persian every morning for a week.",
    ],
    standards=[
        "Solar Hijri calendar per the Iranian Calendar Council; Persian digits per Unicode U+06F0-U+06F9.",
    ],
    citations=[
        "Birashk, Ahmad. A Comparative Calendar of the Iranian, Muslim Lunar, and Christian Eras. Mazda Publishers; 1993.",
        "Academy of Persian Language and Literature. Dasturn-e xatt-e farsi - numeral usage.",
    ],
    sig_lens=("Through the Signature lens, numbers are the sworn measures: "
              "one hundred counted seals, the week beginning on Saturday, "
              "the year turning with the sun of Nowruz. This Signature "
              "reading treats every counted thing as witnessed and "
              "recorded."),
)

E(
    key="persian_greetings", name="Persian Greetings and Everyday Phrases",
    group="Grammar basics", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Thirty Persian greetings, farewells, and politeness phrases, each
        with transliteration, English, and a usage note. Persian politeness
        runs on تعارف (taarof) - ritual courtesy where offers are made and
        politely declined before acceptance. 1. سلام (salam - hello; the
        universal greeting). 2. صبح بخیر (sobh bekheyr - good morning). 3.
        عصر بخیر (asr bekheyr - good afternoon). 4. شب بخیر (shab bekheyr -
        good night, at bedtime). 5. خداحافظ (khodahafez - goodbye). 6. به امید
        دیدار (be omid-e didar - hope to see you again; warm farewell). 7.
        خوش آمدید (khosh amadid - welcome). 8. ممنون (mamnun - thanks,
        casual). 9. متشکرم (moteshakkeram - thank you, standard). 10. خیلی
        ممنون (kheyli mamnun - thanks a lot). 11. خواهش می‌کنم (khahesh
        mikonam - you are welcome; also please, go ahead). 12. ببخشید
        (bebakhshid - excuse me / sorry, formal). 13. معذرت می‌خوام (mazerat
        mikham - sorry, casual). 14. چطوری؟ (chetori? - how are you?,
        casual). 15. خوبی؟ (khubi? - are you well?, casual). 16. چه خبر؟
        (che khabar? - what is new?). 17. خوشحالم (khoshhalam - I am glad;
        said on meeting). 18. خوش وقتم (khoshvaqtam - pleased to meet you,
        formal). 19. روز خوبی داشته باشید (ruz-e khubi dashte bashid - have
        a good day, formal). 20. موفق باشید (movaffaq bashid - good luck /
        wish you success). 21. سلامت باشید (salamat bashid - bless you / stay
        healthy; said after sneezes). 22. خسته نباشید (khaste nabashid -
        literally do not be tired; said to workers as respect). 23. دستت درد
        نکنه (dastet dard nakone - literally may your hand not hurt; thanks
        for food or work). 24. نوش جان (nush-e jan - bon appetit). 25. مبارک
        (mobarak - congratulations). 26. تولدت مبارک (tavallodet mobarak -
        happy birthday). 27. سفر به خیر (safar be kheyr - have a safe trip).
        28. به سلامت (be salamat - farewell to a traveler; go in health). 29.
        بفرمایید (befarmayid - please, come in / go ahead / after you). 30.
        اختیار دارید (ekhtiar darid - you are too kind; the classic taarof
        reply). Usage notes: say خسته نباشید to anyone working; answer a
        compliment with اختیار دارید; accept food only after the host insists
        twice - that is taarof, not rudeness."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the social grammar of Persian: thirty phrases
        that open doors, close conversations, and oil daily life, each with
        a usage note explaining WHEN to say it - because the wrong phrase at
        the wrong moment is worse than silence. It introduces تعارف (taarof),
        the ritual politeness system, through its signature phrases. The
        demonstration program stores all thirty phrases with their usage
        notes, runs a flashcard quiz that checks answers against the stored
        English, and verifies the full set of thirty."""),
    key_points=[
        "30 greetings/farewells/politeness phrases with usage notes.",
        "سلام is the universal greeting; خداحافظ the standard goodbye.",
        "تعارف (taarof): ritual courtesy - offers are declined politely before acceptance.",
        "خسته نباشید honors anyone working; دستت درد نکنه thanks for food or labor.",
        "بفرمایید means please/come in/go ahead/after you - the all-purpose courtesy word.",
        "اختيار دارید is the classic taarof reply to a compliment.",
        "Sample: به امید دیدار - hope to see you again.",
    ],
    requirements=[
        "Use five different greetings in real or role-played conversation.",
        "Practice a taarof exchange: offer, decline, insist, accept.",
    ],
    standards=[
        "Pragmatic usage per Beeman, William O. Language, Status, and Power in Iran. Indiana University Press; 1986.",
    ],
    citations=[
        "Beeman, William O. Language, Status, and Power in Iran. Indiana University Press; 1986. The classic study of taarof and Persian politeness.",
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Greetings and social formulas.",
    ],
    sig_lens=("Through the Signature lens, the greeting is the first "
              "signature exchanged: سلام offered, اختیار دارید returned, "
              "the taarof dance of courtesy sworn step by step. This "
              "Signature reading treats every polite phrase as a small "
              "treaty between strangers."),
)

E(
    key="persian_grammar_essentials", name="Persian Grammar Essentials",
    group="Grammar basics", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        The core rules of Persian grammar, each with translated example
        sentences in script, transliteration, and English. WORD ORDER is
        Subject-Object-Verb: من کتاب خواندم (man ketab khandam - I read the
        book), literally I book read. The verb always comes last. GENDER:
        none - nouns, adjectives, and pronouns never mark masculine or
        feminine. NUMBER: singular and plural; regular plurals take ـها:
        کتاب‌ها (ketab-ha - books); animate nouns often take ـان: مردان
        (mardan - men), زنان (zanan - women). DEFINITENESS: no word for the;
        context shows definiteness, and را (ra) marks a definite direct
        object: کتاب را خواندم (ketab ra khandam - I read the book).
        INDEFINITENESS: یک (yek - one/a) or the suffix ـی: مردی (mardi - a
        man): مردی آمد (mardi amad - a man came). NEGATION: the prefix نه or
        نـ on the verb: نمی‌روم (nemiravam - I do not go), نرفتم (naraftam -
        I did not go), نخور (nakhor - do not eat). QUESTIONS: yes/no questions
        use آیا (aya) or just rising intonation: آیا می‌آیی؟ (aya miayi? -
        are you coming?); می‌آیی؟ (miayi? - you are coming?). Question words
        were taught in the pronouns record: کی، چه، کجا، چرا. EZAFE: the
        linker ـِ chains nouns to modifiers: کتابِ خوبِ من (ketab-e khub-e
        man - my good book). COMPARISON: از (az - than): او از من بلندتر است
        (u az man bolandtar ast - he/she is taller than me). POSSESSION:
        مال (mal) or ezafe: این مال من است (in mal-e man ast - this is
        mine). Example sentences: من هر روز ورزش می‌کنم (man har ruz varzesh
        mikonam - I exercise every day). او دیروز به تهران رفت (u diruz be
        tehran raft - he/she went to Tehran yesterday). ما فردا برمی‌گردیم
        (ma farda barmigardim - we return tomorrow)."""),
    how_it_works=textwrap.dedent("""\
        This record compresses the whole grammatical skeleton into one
        teachable file: SOV word order, zero gender, two plural suffixes,
        the را object marker, the indefinite ـی, the نه negation prefix,
        question formation with آیا or intonation, the ezafe chain, and
        comparison with از. Each rule is proven by a translated sentence,
        and the sentences deliberately reuse vocabulary from records 4-6 so
        the learner meets grammar inside familiar words. The demonstration
        program encodes the rules as checkable functions - SOV order
        validation, plural formation, negation prefixing - and asserts each
        against the example sentences."""),
    key_points=[
        "Word order is Subject-Object-Verb: the verb always comes last.",
        "No grammatical gender anywhere in the language.",
        "Plurals: ـها for most nouns, ـان for many animates.",
        "را marks a definite direct object; ـی or یک marks indefiniteness.",
        "Negation is a verb prefix: نمی‌روم (I do not go), نرفتم (I did not go).",
        "Questions use آیا or rising intonation; question words stay in place.",
        "Sample: من کتاب خواندم - I read the book (I book read).",
    ],
    requirements=[
        "Convert five English SVO sentences into Persian SOV order.",
        "Negate five present-tense sentences with the نمی prefix.",
    ],
    standards=[
        "Word order typology per Dryer, Matthew S. (WALS); Persian classified SOV.",
    ],
    citations=[
        "Lazard, Gilbert. A Grammar of Contemporary Persian. Mazda Publishers; 1992. Syntax chapters.",
        "Mahootian, Shahrzad. Persian. Routledge; 1997. Word order and clause structure.",
    ],
    sig_lens=("Through the Signature lens, grammar is the law of the "
              "covenant: subject, object, then the verb last like a seal at "
              "the foot of the page; no gender to divide the nouns. This "
              "Signature reading treats every rule as a clause of the "
              "contract, signed in word order."),
)

E(
    key="persian_home_family", name="Persian Home and Family Sentences",
    group="Everyday sentences", ladder_rank=4, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Persian sentences about home and family, each in script,
        transliteration, and English - the compounded tier begins here, where
        foundations combine into real life. 1. این خانه‌ی ماست (in khane-ye
        mast - this is our house). 2. خانه‌ی ما سه اتاق دارد (khane-ye ma se
        otaq darad - our house has three rooms). 3. آشپزخانه بزرگ است
        (ashpazkhane bozorg ast - the kitchen is big). 4. اتاق خواب من تمیز
        است (otaq-e khab-e man tamiz ast - my bedroom is clean). 5. مبل در
        پذیرایی است (mobl dar pazira-i ast - the sofa is in the living
        room). 6. تلویزیون روی میز است (televizion ruye miz ast - the TV is
        on the table). 7. پدرم سر کار است (pedaram sar-e kar ast - my father
        is at work). 8. مادرم آشپزی می‌کند (madaram ashpazi mikonad - my
        mother is cooking). 9. برادرم دانشجوست (baradaram daneshjust - my
        brother is a student). 10. خواهرم کوچک است (khaharam kuchak ast - my
        sister is young). 11. پدربزرگم قصه می‌گوید (pedarbozorgam qesse
        miguyad - my grandfather tells stories). 12. مادربزرگم مهربان است
        (madarbozorgam mehraban ast - my grandmother is kind). 13. ما پنج
        نفریم (ma panj nafarim - there are five of us). 14. عمویم در شیراز
        زندگی می‌کند (amuyam dar shiraz zendegi mikonad - my uncle lives in
        Shiraz). 15. خاله‌ام فردا می‌آید (khale-am farda miayad - my aunt
        comes tomorrow). 16. بچه‌ها در حیاط بازی می‌کنند (bache-ha dar hayat
        bazi mikonand - the children play in the yard). 17. سگ ما در باغ است
        (sag-e ma dar bagh ast - our dog is in the garden). 18. کلید روی در
        است (kelid ruye dar ast - the key is on the door). 19. چراغ‌ها روشن
        است (cheragh-ha roshan ast - the lights are on). 20. خانه‌ی ما گرم و
        راحت است (khane-ye ma garm-o-rahat ast - our house is warm and
        comfortable). Family words: پدر (pedar - father)، مادر (madar -
        mother)، برادر (baradar - brother)، خواهر (khahar - sister)، پسر
        (pesar - son)، دختر (dokhtar - daughter)."""),
    how_it_works=textwrap.dedent("""\
        This record moves the learner from words to dwelling: twenty full
        sentences that furnish a house and populate a family, reusing the
        nouns, verbs, adjectives, and pronouns of records 4-8. Each sentence
        is a small scene - rooms, furniture, relatives - so vocabulary sticks
        to places the learner can picture. The demonstration program stores
        the twenty sentences, builds the family-relationship graph, and
        verifies every sentence's vocabulary against the foundation records."""),
    key_points=[
        "20 full sentences covering rooms, furniture, and family members.",
        "Family words: پدر، مادر، برادر، خواهر، پسر، دختر، پدربزرگ، مادربزرگ، عمو، خاله.",
        "House words: آشپزخانه، اتاق خواب، پذیرایی، حیاط، باغ، مبل، تلویزیون.",
        "Possessive suffixes in action: پدرم، مادرم، خانه‌ی ما.",
        "Sample: بچه‌ها در حیاط بازی می‌کنند - the children play in the yard.",
    ],
    requirements=[
        "Describe your own home in ten Persian sentences modeled on these.",
        "Name every member of your family in Persian with the right kinship word.",
    ],
    standards=[
        "Kinship terminology per the Persian kinship system (paternal/maternal distinction: عمو/دایی، عمه/خاله).",
    ],
    citations=[
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Domestic vocabulary.",
        "Beeman, William O. Language, Status, and Power in Iran. Indiana University Press; 1986. Family and household terms.",
    ],
    sig_lens=("Through the Signature lens, home is the first sealed "
              "covenant: the house and its five souls, the grandfather's "
              "stories the oral signature of the family. This Signature "
              "reading treats every room named as a room claimed."),
)

E(
    key="persian_food_cooking", name="Persian Food and Cooking Sentences",
    group="Everyday sentences", ladder_rank=4, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Persian sentences about meals, ingredients, cooking, and
        restaurants, each in script, transliteration, and English. 1. صبحانه
        ساعت هفت است (sobhane saat-e haft ast - breakfast is at seven). 2.
        ناهار برنج و خورشت است (nahar berenj-o-khoresht ast - lunch is rice
        and stew). 3. شام سبک می‌خوریم (sham sabok mikhorim - we eat a light
        dinner). 4. مادرم قرمه‌سبزی پخته است (madaram qorme-sabzi pokhte ast
        - my mother cooked qorme-sabzi). 5. کباب خیلی خوشمزه است (kabab
        kheyli khoshmazze ast - kebab is very delicious). 6. برنج را دم کن
        (berenj ra dam kon - steam the rice). 7. پیاز را خرد کن (piyaz ra
        kherad kon - chop the onion). 8. نمک کم بزن (namak kam bezan - add
        little salt). 9. روغن داغ شد (roqan dagh shod - the oil got hot). 10.
        چای تازه دم است (chay taze dam ast - the tea is freshly brewed). 11.
        نان سنگک داغ بخر (nan-e sangak-e dagh bekhar - buy hot sangak bread).
        12. میوه‌ها را بشور (mive-ha ra beshur - wash the fruits). 13. این
        سیب شیرین است (in sib shirin ast - this apple is sweet). 14. ماست با
        ناهار می‌خوریم (mast ba nahar mikhorim - we eat yogurt with lunch).
        15. دوغ خنک بنوش (dugh-e khonak benush - drink cold dugh). 16. رستوران
        نزدیک پارک است (resturan-e nazdik-e park ast - the restaurant is near
        the park). 17. منو را بیاورید (menu ra biyavarid - bring the menu,
        formal). 18. صورت‌حساب لطفاً (surathesab lotfan - the bill, please).
        19. غذا عالی بود، متشکرم (qaza aali bud, moteshakkeram - the food was
        excellent, thank you). 20. نوش جان! (nush-e jan! - bon appetit!).
        Food words: برنج (berenj - rice)، خورشت (khoresht - stew)، کباب
        (kabab - kebab)، نان (nan - bread)، میوه (mive - fruit)، سبزی (sabzi
        - herbs)، گوشت (gusht - meat)، مرغ (morgh - chicken)، ماهی (mahi -
        fish)."""),
    how_it_works=textwrap.dedent("""\
        This record feeds the learner: twenty sentences that cook, serve, and
        order food, built from the verb and noun foundations. Imperatives
        appear naturally in the kitchen (خرد کن، بشور، بخر), and restaurant
        phrases arrive in their formal register (بیاورید). The demonstration
        program stores the twenty sentences, scales a sample recipe's
        ingredient amounts with tight-bounds arithmetic, and verifies the
        cooking imperatives against the verb stems."""),
    key_points=[
        "20 sentences: meals, ingredients, cooking actions, restaurant phrases.",
        "Meal words: صبحانه، ناهار، شام; dishes: قرمه‌سبزی، کباب، برنج.",
        "Kitchen imperatives: خرد کن (chop)، بشور (wash)، بخر (buy).",
        "Restaurant Persian: منو را بیاورید، صورت‌حساب لطفاً.",
        "Sample: غذا عالی بود، متشکرم - the food was excellent, thank you.",
    ],
    requirements=[
        "Order a full meal in Persian in a role-play.",
        "Give three cooking instructions using imperatives from this record.",
    ],
    standards=[
        "Culinary vocabulary per Batmanglij, Najmieh. Food of Life. Mage Publishers; 2021.",
    ],
    citations=[
        "Batmanglij, Najmieh. Food of Life: Ancient Persian and Modern Iranian Cooking. 2nd ed. Mage Publishers; 2021. Standard reference for Persian food vocabulary.",
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Food and dining vocabulary.",
    ],
    sig_lens=("Through the Signature lens, the meal is a covenant renewed "
              "three times a day: the rice steamed, the bread bought hot, "
              "the guest answered with نوش جان. This Signature reading "
              "treats every shared table as a signed treaty of hospitality."),
)

E(
    key="persian_travel_directions", name="Persian Travel and Directions Sentences",
    group="Everyday sentences", ladder_rank=4, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Persian sentences about transport, asking directions, tickets,
        and lodging, each in script, transliteration, and English. 1. بلیط
        قطار می‌خواهم (belit-e qatar mikhaham - I want a train ticket). 2.
        این اتوبوس کجا می‌رود؟ (in otobus koja miravad? - where does this bus
        go?). 3. ایستگاه مترو کجاست؟ (istgah-e metro kojast? - where is the
        metro station?). 4. فرودگاه چقدر دور است؟ (forudgah cheqadr dur ast?
        - how far is the airport?). 5. تاکسی بگیر (taksi begir - take a
        taxi). 6. مستقیم برو (mostaqim boro - go straight). 7. سر چهارراه
        بپیچ راست (sar-e chaharrah bepic rast - turn right at the
        intersection). 8. بعد از پل، سمت چپ است (bad az pol, samt-e chap ast
        - after the bridge, it is on the left). 9. نزدیک است، پیاده برو
        (nazdik ast, piyade boro - it is near, walk). 10. کرایه چقدر می‌شود؟
        (keraye cheqadr mishavad? - how much is the fare?). 11. هتل نزدیک
        دریا می‌خواهم (hotel-e nazdik-e darya mikhaham - I want a hotel near
        the sea). 12. یک اتاق دو تخته لطفاً (yek otaq-e do takhte lotfan - a
        double room, please). 13. صبحانه شامل است؟ (sobhane shamel ast? - is
        breakfast included?). 14. کلید اتاق ۲۰۴ (kelid-e otaq-e 204 - the key
        to room 204). 15. ساعت حرکت قطار کی است؟ (saat-e harekat-e qatar
        key ast? - when does the train leave?). 16. پرواز تأخیر دارد (parvaz
        takhir darad - the flight is delayed). 17. گذرنامه و بلیط آماده است
        (gozarname-o-belit amade ast - passport and ticket are ready). 18.
        چمدانم را گم کردم (chamedanam ra gom kardam - I lost my suitcase).
        19. راهنما فارسی حرف می‌زند (rahnama farsi harf mizanad - the guide
        speaks Persian). 20. سفر خوبی بود! (safar-e khubi bud! - it was a
        good trip!). Travel words: بلیط (belit - ticket)، قطار (qatar -
        train)، هواپیما (havapayma - airplane)، هتل (hotel - hotel)، نقشه
        (naqshe - map)، سفر (safar - trip)."""),
    how_it_works=textwrap.dedent("""\
        This record puts the learner on the road: twenty sentences covering
        the whole journey - ticket, directions, taxi, hotel, airport - with
        the direction-giving imperatives (برو، بپیچ) and polite requests in
        their natural places. Question words from the pronouns record do the
        heavy lifting. The demonstration program stores the twenty sentences,
        computes a sample trip's travel time from distance and speed with
        tight bounds, and verifies the direction imperatives."""),
    key_points=[
        "20 sentences: transport, directions, tickets, lodging.",
        "Direction imperatives: مستقیم برو (go straight)، بپیچ راست (turn right).",
        "Key questions: کجاست؟ (where is it?)، چقدر می‌شود؟ (how much?).",
        "Hotel Persian: اتاق دو تخته، صبحانه شامل است؟",
        "Travel words: بلیط، قطار، هواپیما، هتل، نقشه، سفر.",
        "Sample: سفر خوبی بود! - it was a good trip!",
    ],
    requirements=[
        "Ask for and give directions to three places in a role-play.",
        "Book a hotel room in Persian, including breakfast and price.",
    ],
    standards=[
        "Transport vocabulary per standard contemporary Persian usage.",
    ],
    citations=[
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Travel vocabulary.",
        "Mahootian, Shahrzad. Persian. Routledge; 1997. Imperative and interrogative constructions.",
    ],
    sig_lens=("Through the Signature lens, the journey is a covenant with "
              "the road: the ticket bought, the direction asked, the room "
              "key received - each step sworn before taken. This Signature "
              "reading treats every سفر خوبی بود as a contract fulfilled."),
)

E(
    key="persian_work_school", name="Persian Work and School Sentences",
    group="Everyday sentences", ladder_rank=5, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Persian sentences about jobs, the office, the classroom, and
        learning, each in script, transliteration, and English. 1. من مهندس
        هستم (man mohandes hastam - I am an engineer). 2. او در بانک کار
        می‌کند (u dar bank kar mikonad - he/she works in a bank). 3. ساعت
        کاری هشت تا چهار است (saat-e kari hasht ta chahar ast - working hours
        are eight to four). 4. جلسه ساعت ده شروع می‌شود (jalase saat-e dah
        shoru mishavad - the meeting starts at ten). 5. گزارش را فردا بده
        (gozaresh ra farda bedeh - give the report tomorrow). 6. حقوق آخر ماه
        است (hoquq akhar-e mah ast - payday is at the end of the month). 7.
        همکارم خیلی کمکم کرد (hamkaram kheyli komakam kard - my colleague
        helped me a lot). 8. پروژه تمام شد (proje tamam shod - the project
        finished). 9. مدرسه ساعت هشت باز می‌شود (madrese saat-e hasht baz
        mishavad - school opens at eight). 10. معلم درس را توضیح داد
        (moallem dars ra tozih dad - the teacher explained the lesson). 11.
        دانش‌آموزان تکلیف نوشتند (danesh-amuzan taklif neveshtand - the
        students wrote the homework). 12. امتحان هفته‌ی آینده است (emtehan
        hafte-ye ayande ast - the exam is next week). 13. نمره‌ی خوبی گرفتم
        (nomre-ye khubi gereftam - I got a good grade). 14. کتابخانه ساکت
        است (ketabkhane saket ast - the library is quiet). 15. فارسی یاد
        می‌گیرم (farsi yad migiram - I am learning Persian). 16. هر روز تمرین
        می‌کنم (har ruz tamrin mikonam - I practice every day). 17. سؤال
        بپرس (soal bepors - ask a question). 18. جواب درست است (javab dorost
        ast - the answer is correct). 19. استاد راضی بود (ostad razi bud -
        the professor was satisfied). 20. یادگیری هرگز تمام نمی‌شود
        (yadgiri hargez tamam nemishavad - learning never ends). Job words:
        کارمند (karmand - employee)، مدیر (modir - manager)، دکتر (doktor -
        doctor)، پرستار (parastar - nurse)، راننده (ranande - driver)."""),
    how_it_works=textwrap.dedent("""\
        This record staffs the learner's day: twenty sentences split between
        the office and the classroom, the two places where formal Persian
        lives. Workplace vocabulary, meeting language, and the teacher's
        imperatives (بپرس، بده) arrive inside scenes, and the final sentence
        states the record's own moral. The demonstration program stores the
        twenty sentences, totals a sample work-week's hours with tight
        bounds, and checks the formal verb forms."""),
    key_points=[
        "20 sentences: jobs, office, classroom, learning.",
        "Work words: جلسه، گزارش، حقوق، پروژه، همکار.",
        "School words: امتحان، نمره، تکلیف، کتابخانه، استاد.",
        "Formal imperatives in the office: بده، بپرس.",
        "Sample: یادگیری هرگز تمام نمی‌شود - learning never ends.",
    ],
    requirements=[
        "Introduce your job and daily schedule in Persian.",
        "Describe your school or university experience in five sentences.",
    ],
    standards=[
        "Professional vocabulary per contemporary Iranian workplace usage.",
    ],
    citations=[
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Occupational vocabulary.",
        "Beeman, William O. Language, Status, and Power in Iran. Indiana University Press; 1986. Formal workplace registers.",
    ],
    sig_lens=("Through the Signature lens, work is the daily-renewed "
              "covenant: the meeting at ten, the report delivered, the "
              "lesson learned - each day signed with effort. This Signature "
              "reading treats the classroom as the forge where the oath of "
              "learning is hammered."),
)

E(
    key="persian_health_body", name="Persian Health and Body Sentences",
    group="Everyday sentences", ladder_rank=5, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Persian sentences about body parts, symptoms, the doctor's
        visit, and the pharmacy, each in script, transliteration, and
        English. 1. سرم درد می‌کند (saram dard mikonad - my head hurts). 2.
        چشم‌هایم می‌سوزد (cheshm-hayam misuzad - my eyes burn). 3. گلویم درد
        می‌کند (galuyam dard mikonad - my throat hurts). 4. تب دارم (tab
        daram - I have a fever). 5. سرفه می‌کنم (sorfe mikonam - I am
        coughing). 6. سرما خورده‌ام (sarma khorde-am - I have a cold). 7.
        دستم زخمی شد (dastam zakhmi shod - my hand got cut). 8. پایم پیچ خورد
        (payam pich khord - my ankle twisted). 9. حالم خوب نیست (halam khub
        nist - I do not feel well). 10. دکتر وقت دارد؟ (doktor vaqt darad? -
        does the doctor have an appointment?). 11. باید دکتر بروم (bayad
        doktor beravam - I must go to the doctor). 12. کجا درد می‌کند؟ (koja
        dard mikonad? - where does it hurt?). 13. از کی شروع شد؟ (az key
        shoru shod? - when did it start?). 14. این دارو را روزی دو بار بخور
        (in daru ra ruzi do bar bekhor - take this medicine twice a day). 15.
        بعد از غذا بخور (bad az qaza bekhor - take it after meals). 16.
        استراحت کن (esterahat kon - rest). 17. آب زیاد بنوش (ab-e ziyad
        benush - drink lots of water). 18. داروخانه شبانه‌روزی کجاست؟
        (darukhane-ye shabane-ruzi kojast? - where is a 24-hour pharmacy?).
        19. نسخه را بدهید (noskhe ra bedehid - give the prescription,
        formal). 20. زود خوب می‌شوی (zud khub mishi - you will get well
        soon). Body words: سر (sar - head)، چشم (cheshm - eye)، گوش (gush -
        ear)، بینی (bini - nose)، دهان (dahan - mouth)، دست (dast - hand)، پا
        (pa - foot/leg)، قلب (qalb - heart)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the language of the body because health
        sentences cannot wait for fluency: twenty sentences that name parts,
        report symptoms, book the doctor, and follow the prescription.
        Possessive suffixes carry the pain (سرم، دستم), and the doctor's
        questions model the interrogatives in urgent use. The demonstration
        program stores the twenty sentences, computes a sample body-mass
        index with tight bounds, and verifies the symptom vocabulary."""),
    key_points=[
        "20 sentences: body parts, symptoms, doctor visit, pharmacy.",
        "Body words: سر، چشم، گوش، بینی، دهان، دست، پا، قلب.",
        "Pain pattern: سرم درد می‌کند (my head hurts) - possessive suffix + درد می‌کند.",
        "Doctor's questions: کجا درد می‌کند؟ از کی شروع شد؟",
        "Prescription language: روزی دو بار بخور (twice a day).",
        "Sample: زود خوب می‌شوی - you will get well soon.",
    ],
    requirements=[
        "Describe three symptoms to a doctor in a role-play.",
        "Name ten body parts in Persian without hesitation.",
    ],
    standards=[
        "Medical vocabulary per standard contemporary Persian usage.",
    ],
    citations=[
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Body and health vocabulary.",
    ],
    sig_lens=("Through the Signature lens, the body is the first territory "
              "of the covenant: every ache named - سرم، دستم، پایم - is a "
              "report sworn to the healer. This Signature reading treats "
              "زود خوب می‌شوی as a promise sealed in grammar."),
)

E(
    key="persian_emotions", name="Persian Emotions and Feelings Sentences",
    group="Everyday sentences", ladder_rank=5, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Persian sentences about happiness, sadness, anger, fear,
        love, and surprise, each in script, transliteration, and English.
        Persian feelings often live in the heart (دل) and the soul (جان). 1.
        خیلی خوشحالم (kheyli khoshhalam - I am very happy). 2. از دیدنت
        خوشحالم (az didanet khoshhalam - I am happy to see you). 3. دلم شاد
        است (delam shad ast - my heart is glad). 4. امروز ناراحتم (emruz
        narahatam - I am sad today). 5. دلم گرفته است (delam gerefte ast -
        literally my heart is squeezed; I feel blue). 6. گریه‌ام گرفت
        (gerye-am gereft - I started crying). 7. عصبانی شدم (asabani shodam -
        I got angry). 8. خونم به جوش آمد (khunam be jush amad - literally my
        blood boiled; I was furious). 9. آرام باش (aram bash - calm down). 10.
        می‌ترسم (mitarsam - I am afraid). 11. از تاریکی می‌ترسم (az tariki
        mitarsam - I am afraid of the dark). 12. نگران نباش (negaran nabash -
        do not worry). 13. دوستت دارم (dustet daram - I love you). 14. عاشق
        بهارم (asheq-e baharam - I love spring). 15. دلم برایت تنگ شده
        (delam barat tang shode - I miss you; literally my heart is tight for
        you). 16. تعجب کردم! (taajob kardam! - I was surprised!). 17. باورت
        نمی‌شود! (bavaret nemishavad! - you will not believe it!). 18. چه
        عالی! (che aali! - how wonderful!). 19. خسته‌ام (khaste-am - I am
        tired). 20. امیدوارم (omidvaram - I hope so). Emotion words: شادی
        (shadi - happiness)، غم (gham - sorrow)، خشم (khashm - anger)، ترس
        (tars - fear)، عشق (eshq - love)، تعجب (taajob - surprise)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the heart's vocabulary: twenty sentences where
        Persian feelings live - in دل (heart) and جان (soul) - because
        Persian expresses emotion through the body, and the learner must feel
        the idiom, not just translate it. Literal translations are given for
        the body-idioms so the image lands. The demonstration program stores
        the twenty sentences, maps each to an emotion-intensity scale with
        tight-bounds averaging, and verifies the emotion vocabulary."""),
    key_points=[
        "20 sentences: happy, sad, angry, afraid, love, surprise.",
        "Feelings live in دل (heart): دلم گرفته (I feel blue)، دلم برایت تنگ شده (I miss you).",
        "Body idioms: خونم به جوش آمد (my blood boiled = I was furious).",
        "دوستت دارم - I love you; نگران نباش - do not worry.",
        "Emotion words: شادی، غم، خشم، ترس، عشق، تعجب.",
        "Sample: امیدوارم - I hope so.",
    ],
    requirements=[
        "Express six different emotions in Persian in a role-play.",
        "Explain what دلم گرفته means literally and emotionally.",
    ],
    standards=[
        "Emotion lexicon per contemporary Persian usage.",
    ],
    citations=[
        "Beeman, William O. Language, Status, and Power in Iran. Indiana University Press; 1986. Emotion and expression in Persian culture.",
    ],
    sig_lens=("Through the Signature lens, feeling is the covenant's pulse: "
              "the heart squeezed, the blood boiled, the soul's ache sworn "
              "in دل and جان. This Signature reading treats every emotion "
              "named as a truth signed by the heart."),
)

E(
    key="persian_nature_weather", name="Persian Nature and Weather Sentences",
    group="Everyday sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Persian sentences about animals, plants, seasons, and weather
        talk, each in script, transliteration, and English. 1. امروز هوا
        آفتابی است (emruz hava aftabi ast - today is sunny). 2. دیروز باران
        آمد (diruz baran amad - it rained yesterday). 3. فردا برف می‌آید
        (farda barf miayad - it will snow tomorrow). 4. هوا ابری است (hava
        abri ast - it is cloudy). 5. باد شدیدی می‌وزد (bad-e shadidi mivazad
        - a strong wind is blowing). 6. هوا خیلی گرم است (hava kheyli garm
        ast - it is very hot). 7. زمستان سرد است (zemestan sard ast - winter
        is cold). 8. بهار فصل گل‌هاست (bahar fasl-e gol-hast - spring is the
        season of flowers). 9. درخت‌ها سبز شدند (derakht-ha sabz shodand -
        the trees turned green). 10. پرنده‌ها می‌خوانند (parande-ha
        mikhanand - the birds are singing). 11. گربه روی دیوار است (gorbe
        ruye divar ast - the cat is on the wall). 12. سگ پارس می‌کند (sag
        pars mikonad - the dog is barking). 13. اسب سریع می‌دود (asb sari
        midavad - the horse runs fast). 14. ماهی در آب شنا می‌کند (mahi dar
        ab shena mikonad - the fish swims in the water). 15. کوه بلند است
        (kuh boland ast - the mountain is tall). 16. رودخانه پر آب است
        (rudkhane por ab ast - the river is full). 17. دریا آبی است (darya
        abi ast - the sea is blue). 18. صحرا خشک است (sahra khoshk ast - the
        desert is dry). 19. رنگین‌کمان زیباست (rangin-kaman zibast - the
        rainbow is beautiful). 20. طبیعت ایران متنوع است (tabiat-e iran
        motenavve ast - Iran's nature is diverse). Nature words: حیوان
        (heyvan - animal)، گیاه (giyah - plant)، جنگل (jangal - forest)،
        بیابان (biyaban - desert)، آسمان (aseman - sky)، ستاره (setare -
        star)، ابر (abr - cloud)، طوفان (tufan - storm)."""),
    how_it_works=textwrap.dedent("""\
        This record opens the window: twenty sentences of weather small-talk
        and nature description - the everyday poetry of Persian conversation.
        Weather verbs (باران آمد، برف می‌آید) and seasonal change are drilled
        because they are the most-spoken sentences in any language. The
        demonstration program stores the twenty sentences, converts sample
        temperatures between Celsius and Fahrenheit with tight bounds, and
        verifies the weather vocabulary."""),
    key_points=[
        "20 sentences: animals, plants, seasons, weather talk.",
        "Weather verbs: باران آمد (it rained)، برف می‌آید (it will snow).",
        "Seasonal cycle: بهار گل‌ها، زمستان سرد.",
        "Nature words: جنگل، بیابان، آسمان، ستاره، رودخانه، دریا.",
        "Sample: طبیعت ایران متنوع است - Iran's nature is diverse.",
    ],
    requirements=[
        "Give a three-day weather forecast in Persian.",
        "Describe the landscape of your region in five sentences.",
    ],
    standards=[
        "Meteorological terms per standard contemporary Persian usage.",
    ],
    citations=[
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Nature vocabulary.",
    ],
    sig_lens=("Through the Signature lens, nature is the oldest covenant "
              "of all: the rain that came, the snow that will come, the "
              "trees turning green on schedule. This Signature reading "
              "treats every season named as a promise the earth keeps."),
)

E(
    key="persian_shopping_money", name="Persian Shopping and Money Sentences",
    group="Everyday sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Persian sentences about the market, prices, bargaining, and
        paying, each in script, transliteration, and English. Bargaining is
        normal in traditional markets - and taarof oils the exchange. 1. این
        چقدر است؟ (in cheqadr ast? - how much is this?). 2. قیمتش چنده؟
        (qeymatesh chande? - what is its price?, casual). 3. خیلی گران است
        (kheyli geran ast - it is very expensive). 4. تخفیف می‌دهید؟ (takhfif
        midahid? - do you give a discount?, formal). 5. آخرش چنده؟ (akharesh
        chande? - what is your final price?, casual). 6. کمی ارزان‌تر بگویید
        (kami arzan-tar beguyid - say a bit cheaper, formal). 7. دو کیلو سیب
        می‌خواهم (do kilu sib mikhaham - I want two kilos of apples). 8. نیم
        کیلو پنیر بده (nim kilu panir bedeh - give half a kilo of cheese). 9.
        تازه است؟ (taze ast? - is it fresh?). 10. این رنگ را دارید؟ (in rang
        ra darid? - do you have this color?, formal). 11. سایز بزرگ‌تر دارید؟
        (sayz-e bozorg-tar darid? - do you have a bigger size?, formal). 12.
        فقط نگاه می‌کنم (faqat negah mikonam - I am just looking). 13. می‌خرم
        (mikharam - I will buy it). 14. نقد می‌دهم (naqd midaham - I pay
        cash). 15. کارت می‌کشم (kart mikesham - I pay by card). 16. بقیه‌اش
        را نگه دارید (baqiye-ash ra negah darid - keep the change, formal).
        17. فاکتور بدهید (faktor bedehid - give me the receipt, formal). 18.
        بازار شلوغ است (bazar sholuq ast - the bazaar is crowded). 19. مغازه
        ساعت نه باز می‌شود (maqaze saat-e noh baz mishavad - the shop opens
        at nine). 20. خرید خوبی بود! (kharid-e khubi bud! - it was good
        shopping!). Money words: تومان (tuman - toman, the everyday currency
        unit)، ریال (riyal - rial, the official unit; 1 toman = 10 rials)،
        پول خرد (pul-e kherad - change)، گران (geran - expensive)، ارزان
        (arzan - cheap)، تخفیف (takhfif - discount)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the bazaar: twenty sentences that price, haggle,
        weigh, and pay, with the formal/casual pairs (می‌دهید/چنده) side by
        side because the market runs on register-switching. The toman/rial
        distinction is stated plainly - it confuses every beginner. The
        demonstration program stores the twenty sentences, computes discount
        and change arithmetic with tight bounds, and verifies the bargaining
        phrases."""),
    key_points=[
        "20 sentences: market, prices, bargaining, paying.",
        "Bargaining phrases: تخفیف می‌دهید؟ آخرش چنده؟ کمی ارزان‌تر بگویید.",
        "Currency: تومان (everyday unit)، ریال (official; 1 toman = 10 rials).",
        "Paying: نقد می‌دهم (cash)، کارت می‌کشم (card)، بقیه‌اش را نگه دارید (keep the change).",
        "Sample: خرید خوبی بود! - it was good shopping!",
    ],
    requirements=[
        "Haggle over a price in a role-play, from این چقدر است؟ to می‌خرم.",
        "Convert three prices between toman and rials.",
    ],
    standards=[
        "Currency units per the Central Bank of Iran (rial official, toman customary).",
    ],
    citations=[
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Market vocabulary.",
        "Beeman, William O. Language, Status, and Power in Iran. Indiana University Press; 1986. Bazaar interaction.",
    ],
    sig_lens=("Through the Signature lens, the bargain is a covenant "
              "negotiated aloud: the price asked, the discount sworn, the "
              "change kept - each deal a small treaty. This Signature "
              "reading treats every handshake in the bazaar as a signature "
              "on the day's trade."),
)

E(
    key="persian_friendship_social", name="Persian Friendship and Social Life Sentences",
    group="Everyday sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Persian sentences about meeting people, invitations, and
        celebrations, each in script, transliteration, and English. 1. اسم
        شما چیست؟ (esm-e shoma chist? - what is your name?, formal). 2. من
        سارا هستم (man sara hastam - I am Sara). 3. از آشنایی‌تان خوشحالم (az
        ashna-i-tan khoshhalam - pleased to meet you, formal). 4. کجا زندگی
        می‌کنید؟ (koja zendegi mikonid? - where do you live?, formal). 5.
        چند سالته؟ (chand salete? - how old are you?, casual). 6. شغلت چیست؟
        (shoghlet chist? - what is your job?, casual). 7. فردا مهمان مایی
        (farda mehman-e ma-i - you are our guest tomorrow). 8. به خانه‌ی ما
        بیا (be khane-ye ma biya - come to our house). 9. چای می‌خوری؟ (chay
        mikhori? - will you have tea?, casual). 10. بفرما، تعارف نکن (befama,
        taarof nakon - come in, do not stand on ceremony). 11. تولدت مبارک!
        (tavallodet mobarak! - happy birthday!). 12. عیدت مبارک! (eydet
        mobarak! - happy Nowruz!). 13. سال نو مبارک! (sal-e no mobarak! -
        happy new year!). 14. به سلامتی! (be salamati! - cheers! / to health!).
        15. دیشب خیلی خوش گذشت (dishab kheyli khosh gozasht - last night was
        great fun). 16. دوباره همدیگر را ببینیم (dobare hamdigar ra bebinim -
        let us meet again). 17. شماره‌ات را بده (shomare-at ra bedeh - give
        me your number, casual). 18. در تماس باشیم (dar tamas bashim - let
        us stay in touch). 19. دوست خوبی هستی (dust-e khubi hasti - you are a
        good friend). 20. همیشه خوشحال می‌شوم ببینمت (hamishe khoshhal
        mishavam bebinamet - I am always happy to see you). Social words:
        مهمانی (mehmani - party/gathering)، دعوت (davat - invitation)، جشن
        (jashn - celebration)، عروسی (arusi - wedding)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches friendship as performance: twenty sentences that
        meet, invite, host, and celebrate, because Persian social life runs
        on warm formulas and the learner needs them ready. Formal and casual
        introductions appear together so the learner chooses the right
        register on the spot. The demonstration program stores the twenty
        sentences, counts a sample gathering's guest list with tight bounds,
        and verifies the invitation phrases."""),
    key_points=[
        "20 sentences: meeting people, invitations, celebrations.",
        "Introductions: اسم شما چیست؟ (formal) / اسمت چیه؟ (casual).",
        "Hosting formulas: بفرما، تعارف نکن; فردا مهمان مایی.",
        "Celebrations: تولدت مبارک! عیدت مبارک! به سلامتی!",
        "Social words: مهمانی، دعوت، جشن، عروسی.",
        "Sample: در تماس باشیم - let us stay in touch.",
    ],
    requirements=[
        "Introduce yourself formally and casually in two role-plays.",
        "Invite a friend to your house and accept an invitation with taarof.",
    ],
    standards=[
        "Social formulas per Beeman, Language, Status, and Power in Iran.",
    ],
    citations=[
        "Beeman, William O. Language, Status, and Power in Iran. Indiana University Press; 1986. Hospitality and social formulas.",
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Social vocabulary.",
    ],
    sig_lens=("Through the Signature lens, friendship is the covenant "
              "renewed at every table: the guest welcomed, the tea poured, "
              "the promise to meet again sworn. This Signature reading "
              "treats every بفرما as an open door signed by the host."),
)

E(
    key="persian_technology", name="Persian Technology and Communication Sentences",
    group="Everyday sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Persian sentences about the phone, the internet, the
        computer, and messaging, each in script, transliteration, and
        English. 1. گوشیم زنگ خورد (gushim zang khord - my phone rang). 2.
        جواب بده (javab bedeh - answer it). 3. شماره‌ام را ذخیره کن
        (shomare-am ra zekhire kon - save my number). 4. پیامک بفرست (payamak
        beferest - send a text). 5. ایمیلت را چک کن (email-at ra check kon -
        check your email). 6. اینترنت قطع است (internet qat ast - the
        internet is down). 7. وای‌فای وصل شد (wifi vasl shod - the wifi
        connected). 8. رمز وای‌فای چیست؟ (ramz-e wifi chist? - what is the
        wifi password?). 9. کامپیوترم هنگ کرد (kamputeram hang kard - my
        computer froze). 10. فایل را دانلود کن (file ra download kon -
        download the file). 11. عکس بفرست (aks beferest - send a photo). 12.
        ویدیو را ببین (video ra bebin - watch the video). 13. آنلاین شو
        (online sho - come online). 14. تماس تصویری بگیریم (tamas-e tasviri
        begirim - let us video-call). 15. شارژ گوشیم تمام شد (sharzh-e
        gushim tamam shod - my phone battery died). 16. گوشی را شارژ کن
        (gushi ra sharzh kon - charge the phone). 17. برنامه را نصب کن
        (barname ra nasb kon - install the app). 18. آپدیت جدید آمد (update-e
        jadid amad - a new update arrived). 19. پسورد را عوض کن (password ra
        avaz kon - change the password). 20. تکنولوژی زندگی را آسان کرد
        (teknolozhi zendegi ra asan kard - technology made life easy). Tech
        words: گوشی (gushi - phone)، پیام (payam - message)، تماس (tamas -
        call)، صفحه (safhe - screen/page)، لینک (link - link)، جستجو (josteju
        - search)."""),
    how_it_works=textwrap.dedent("""\
        This record wires the learner into modern life: twenty sentences of
        phones, internet, and computers, where Persian freely borrows
        international tech words (اینترنت، وای‌فای، دانلود) - so the learner
        discovers how much they already know. Imperatives dominate because
        tech talk is instructional. The demonstration program stores the
        twenty sentences, computes a sample download time with tight bounds,
        and verifies the tech vocabulary."""),
    key_points=[
        "20 sentences: phone, internet, computer, messaging.",
        "Persian borrows tech words freely: اینترنت، وای‌فای، دانلود، آپدیت.",
        "Tech imperatives: بفرست (send)، دانلود کن (download)، نصب کن (install).",
        "Everyday tech: شارژ تمام شد (battery died)، هنگ کرد (froze).",
        "Sample: تکنولوژی زندگی را آسان کرد - technology made life easy.",
    ],
    requirements=[
        "Explain a phone problem and its fix in Persian.",
        "Give five tech instructions using imperatives.",
    ],
    standards=[
        "Technology vocabulary per the Academy of Persian Language and Literature approved equivalents.",
    ],
    citations=[
        "Academy of Persian Language and Literature (فرهنگستان زبان و ادب فارسی). Approved Persian equivalents for technology terms.",
    ],
    sig_lens=("Through the Signature lens, technology is the covenant's "
              "newest seal: the message sent, the call answered, the photo "
              "shared across the world in a second. This Signature reading "
              "treats every connection made as a signature transmitted."),
)

E(
    key="persian_verb_tenses", name="Persian Verb Tenses in Sentences",
    group="Grammar in use", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Persian verb tenses taught through sentences: present, past, and
        future forms, with aspect and mood where they matter - five or more
        translated sentences per tense, each in script, transliteration, and
        English. PRESENT (می‌ + present stem): 1. من هر روز ورزش می‌کنم (man
        har ruz varzesh mikonam - I exercise every day). 2. او فارسی حرف
        می‌زند (u farsi harf mizanad - he/she speaks Persian). 3. ما با هم
        ناهار می‌خوریم (ma ba ham nahar mikhorim - we eat lunch together). 4.
        آنها در تهران زندگی می‌کنند (anha dar tehran zendegi mikonand -
        they live in Tehran). 5. بچه‌ها بازی می‌کنند (bache-ha bazi mikonand
        - the children are playing). PAST SIMPLE (past stem + endings): 1.
        دیروز باران آمد (diruz baran amad - it rained yesterday). 2. من کتاب
        خواندم (man ketab khandam - I read the book). 3. او رفت (u raft -
        he/she went). 4. ما فیلم دیدیم (ma film didim - we watched a movie).
        5. آنها آمدند (anha amadand - they came). PAST CONTINUOUS (می‌ + past
        stem): 1. داشتم کتاب می‌خواندم (dashtam ketab mikhandam - I was
        reading a book). 2. باران می‌آمد (baran miamad - it was raining).
        PRESENT PERFECT (past participle + ام/ای/است...): 1. غذا خورده‌ام
        (qaza khorde-am - I have eaten). 2. او رفته است (u rafte ast - he/she
        has gone). PAST PERFECT (past participle + بودم...): 1. وقتی رسیدم،
        رفته بود (vaqti residam, rafte bud - when I arrived, he/she had
        gone). FUTURE: modern speech uses present tense for the future: فردا
        می‌روم (farda miravam - I will go tomorrow); the literary future uses
        خواستن + short infinitive: خواهم رفت (khaham raft - I shall go).
        SUBJUNCTIVE (بـ + present stem): 1. باید بروم (bayad beravam - I must
        go). 2. می‌خواهم بخورم (mikhaham bekhoram - I want to eat). IMPERATIVE
        (بـ + present stem): بخور! (bekhor! - eat!). NEGATION moves through
        the tenses: نمی‌روم (nemiravam - I do not go)، نرفتم (naraftam - I did
        not go)."""),
    how_it_works=textwrap.dedent("""\
        This record is the engine room: every major Persian tense built live
        from the two stems, five or more sentences each, so the learner sees
        the whole machine at once. The می‌ prefix, the past endings, the
        participle + بودن perfects, the ب subjunctive, and the literary
        future are each proven in sentences, and the modern habit of using
        present for future is stated plainly. The demonstration program
        conjugates sample verbs across all tenses from their stems and
        asserts every form against the sentences in this record."""),
    key_points=[
        "Present: می‌ + present stem (می‌خورم); past simple: past stem + endings (خوردم).",
        "Past continuous: می‌ + past stem (می‌خوردم); with داشتم for was/were -ing.",
        "Present perfect: participle + ام (خورده‌ام); past perfect: participle + بودم (خورده بودم).",
        "Modern future = present tense (فردا می‌روم); literary future = خواهم رفت.",
        "Subjunctive: بـ + stem after باید/می‌خواهم (بروم، بخورم).",
        "Negation: نمی‌روم (present)، نرفتم (past).",
        "Sample: داشتم کتاب می‌خواندم - I was reading a book.",
    ],
    requirements=[
        "Conjugate خوردن، رفتن، and دیدن in all six tenses.",
        "Write five past-continuous and five present-perfect sentences.",
    ],
    standards=[
        "Tense/aspect system per Lazard, A Grammar of Contemporary Persian.",
    ],
    citations=[
        "Lazard, Gilbert. A Grammar of Contemporary Persian. Mazda Publishers; 1992. Tense, aspect, and mood.",
        "Windfuhr, Gernot L. Persian Grammar. Mouton de Gruyter; 1979. The verbal system.",
    ],
    sig_lens=("Through the Signature lens, tense is the covenant's memory: "
              "the past sealed with خوردم, the present sworn with می‌خورم, "
              "the future promised with فردا می‌روم. This Signature reading "
              "treats every conjugated verb as time itself signing the "
              "page."),
)

E(
    key="persian_questions_answers", name="Persian Questions and Answers",
    group="Grammar in use", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Persian question-and-answer pairs covering who, what, where,
        when, why, and how - each pair in script, transliteration, and
        English. 1. اسمت چیست؟ - سارا هستم (esmet chist? - sara hastam - what
        is your name? - I am Sara). 2. کجایی؟ - خانه هستم (koja-i? - khane
        hastam - where are you? - I am home). 3. کی آمد؟ - دوستم آمد (ki
        amad? - dustam amad - who came? - my friend came). 4. چه می‌خواهی؟ -
        آب می‌خواهم (che mikhahi? - ab mikhaham - what do you want? - I want
        water). 5. چرا دیر کردی؟ - ترافیک بود (chera dir kardi? - trafik bud
        - why are you late? - there was traffic). 6. چگونه آمدی؟ - با تاکسی
        (chegune amadi? - ba taksi - how did you come? - by taxi). 7. کی
        می‌روی؟ - فردا (key miravi? - farda - when are you going? -
        tomorrow). 8. کدام را می‌خواهی؟ - آبی را (kodam ra mikhahi? - abi ra
        - which one do you want? - the blue one). 9. چند تا خریدی؟ - سه تا
        (chand ta kharidi? - se ta - how many did you buy? - three). 10. آیا
        فارسی بلدی؟ - کمی (aya farsi baladi? - kami - do you know Persian? -
        a little). 11. حالت چطور است؟ - خوبم، ممنون (halet chetor ast? -
        khubam, mamnun - how are you? - I am fine, thanks). 12. ناهار خوردی؟
        - بله، خوردم (nahar khordi? - bale, khordam - did you eat lunch? -
        yes, I ate). 13. کجا کار می‌کنی؟ - در بانک (koja kar mikoni? - dar
        bank - where do you work? - in a bank). 14. چه ساعتی می‌آیی؟ - ساعت
        پنج (che saati miayi? - saat-e panj - what time are you coming? - at
        five). 15. با کی رفتی؟ - با برادرم (ba ki rafti? - ba baradaram - who
        did you go with? - with my brother). 16. چرا نخوردی؟ - سیر بودم
        (chera nakhordi? - sir budam - why did you not eat? - I was full).
        17. این مال کیست؟ - مال من است (in mal-e kist? - mal-e man ast -
        whose is this? - it is mine). 18. هوا چطور است؟ - آفتابی (hava
        chetor ast? - aftabi - how is the weather? - sunny). 19. چقدر طول
        می‌کشد؟ - یک ساعت (cheqadr tul mikeshad? - yek saat - how long does
        it take? - one hour). 20. می‌توانی کمکم کنی؟ - حتماً (mitavani
        komakam koni? - hatman - can you help me? - certainly). Yes/no
        answers: بله (bale - yes)، نه (na - no)، حتماً (hatman -
        certainly)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches conversation as call and response: twenty
        question-answer pairs, each built on the interrogatives from the
        pronouns record, so the learner practices both asking and answering
        in one motion. Every pair is a complete micro-dialogue the learner
        can lift into real talk. The demonstration program stores the twenty
        pairs, classifies each question by its question word, and quizzes
        answers against the stored responses."""),
    key_points=[
        "20 question/answer pairs covering who, what, where, when, why, how.",
        "Question words stay in place; answers are short and natural.",
        "Yes/no: بله (yes)، نه (no)، حتماً (certainly).",
        "Time questions: چه ساعتی؟ (what time?)، چقدر طول می‌کشد؟ (how long?).",
        "Sample: چرا دیر کردی؟ - ترافیک بود - why are you late? - there was traffic.",
    ],
    requirements=[
        "Ask and answer all twenty pairs with a partner, switching roles.",
        "Invent five new pairs using each question word at least once.",
    ],
    standards=[
        "Interrogative syntax per Mahootian, Persian.",
    ],
    citations=[
        "Mahootian, Shahrzad. Persian. Routledge; 1997. Questions and answers.",
        "Lazard, Gilbert. A Grammar of Contemporary Persian. Mazda Publishers; 1992. Interrogatives.",
    ],
    sig_lens=("Through the Signature lens, the question is the covenant's "
              "knock and the answer its opened door: twenty knocks, twenty "
              "answers, each pair a small treaty of understanding. This "
              "Signature reading treats every چرا answered as a seal "
              "broken open."),
)

E(
    key="persian_commands_requests", name="Persian Commands and Requests",
    group="Grammar in use", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Persian imperatives and polite requests, formal versus
        informal, each in script, transliteration, and English. The
        imperative uses بـ + present stem: informal singular بخور (bekhor -
        eat!), formal/plural بخورید (bekhorid - eat!). 1. بیا اینجا (biya
        inja - come here, informal). 2. بفرمایید داخل (befarmayid dakhel -
        please come in, formal). 3. بنشین (benshin - sit down, informal). 4.
        بفرمایید بنشینید (befarmayid benshinid - please sit down, formal). 5.
        بگو (begu - say it, informal). 6. لطفاً بفرمایید (lotfan befarmayid -
        please tell me, formal). 7. بخور (bekhor - eat, informal). 8. نوش جان
        کنید (nush-e jan konid - enjoy your meal, formal). 9. برو (boro - go,
        informal). 10. بفرمایید بروید (befarmayid beravid - please go ahead,
        formal). 11. صبر کن (sabr kon - wait, informal). 12. یک لحظه صبر
        کنید (yek lahze sabr konid - wait a moment, formal). 13. در را ببند
        (dar ra beband - close the door, informal). 14. لطفاً در را ببندید
        (lotfan dar ra bebanded - please close the door, formal). 15. کمکم
        کن (komakam kon - help me, informal). 16. می‌توانید کمکم کنید؟
        (mitavanid komakam konid? - could you help me?, formal). 17. زود باش
        (zud bash - hurry up, informal). 18. عجله کنید (ajale konid - please
        hurry, formal). 19. مواظب باش (movazeb bash - be careful, informal).
        20. خواهش می‌کنم مواظب باشید (khahesh mikonam movazeb bashid - please
        be careful, formal). Polite requests soften with لطفاً (lotfan -
        please)، می‌توانید (mitavanid - could you)، and خواهش می‌کنم
        (khahesh mikonam - I beg you/please). Negative commands use نه: نرو
        (naro - do not go)، نزن (nazan - do not hit)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches command as register: twenty imperatives in
        matched informal/formal pairs, so the learner feels the politeness
        ladder - bare بـ stem with friends, بفرمایید/لطفاً/ید endings with
        strangers. The بـ prefix rule and the نه negative are stated once
        and drilled twenty times. The demonstration program stores the pairs,
        builds imperatives from present stems with the بـ rule, and verifies
        each formal/informal match."""),
    key_points=[
        "20 imperatives in matched informal/formal pairs.",
        "Imperative = بـ + present stem: بخور (informal)، بخورید (formal).",
        "Politeness softeners: لطفاً، بفرمایید، می‌توانید، خواهش می‌کنم.",
        "Negative commands: نرو (do not go)، نزن (do not hit).",
        "Sample: لطفاً در را ببندید - please close the door.",
    ],
    requirements=[
        "Give ten commands to a friend and the same ten to a stranger.",
        "Soften five bare imperatives with لطفاً or بفرمایید.",
    ],
    standards=[
        "Imperative morphology per Lazard, A Grammar of Contemporary Persian.",
    ],
    citations=[
        "Lazard, Gilbert. A Grammar of Contemporary Persian. Mazda Publishers; 1992. Mood and the imperative.",
        "Beeman, William O. Language, Status, and Power in Iran. Indiana University Press; 1986. Politeness in directives.",
    ],
    sig_lens=("Through the Signature lens, the command is the covenant "
              "spoken as law: بخور to the friend, بفرمایید to the elder - "
              "the same order sealed with different wax. This Signature "
              "reading treats every polite softener as respect signed into "
              "the sentence."),
)

E(
    key="persian_descriptions", name="Persian Descriptions of People and Places",
    group="Grammar in use", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Persian sentences describing people, places, and things in
        detail, each in script, transliteration, and English - where
        adjectives, ezafe chains, and comparatives combine. 1. مادرم زنی
        مهربان و صبور است (madaram zan-e mehraban-o-sabur ast - my mother is
        a kind and patient woman). 2. پدرم قد بلند و موهای خاکستری دارد
        (pedaram qad-e boland-o-muha-ye khakestari darad - my father is tall
        with gray hair). 3. دوستم چشم‌های سبز و لبخند گرمی دارد (dustam
        cheshm-ha-ye sabz-o-labkhand-e garmi darad - my friend has green eyes
        and a warm smile). 4. تهران شهری بزرگ و شلوغ است (tehran shahr-e
        bozorg-o-sholuq ast - Tehran is a big, crowded city). 5. اصفهان
        تاریخی و زیباست (esfahan tarikhi-o-zibast - Isfahan is historic and
        beautiful). 6. خانه‌ی ما قدیمی ولی راحت است (khane-ye ma qadimi vali
        rahat ast - our house is old but comfortable). 7. باغ پر از گل‌های
        رنگارنگ است (bagh por az gol-ha-ye rangarang ast - the garden is full
        of colorful flowers). 8. کوه دماوند بلندترین کوه ایران است (kuh-e
        damavand bolandtarin kuh-e iran ast - Damavand is Iran's tallest
        mountain). 9. دریای خزر بزرگ‌ترین دریاچه‌ی جهان است (darya-ye khazar
        bozorgtarin daryache-ye jahan ast - the Caspian is the world's
        largest lake). 10. این رستوران غذای خوشمزه و قیمت مناسب دارد (in
        resturan qaza-ye khoshmazze-o-qeymat-e monaseb darad - this
        restaurant has delicious food and fair prices). 11. معلم ما جدی ولی
        عادل است (moallem-e ma jeddi vali adel ast - our teacher is strict
        but fair). 12. بچه‌ی همسایه بازیگوش و باهوش است (bache-ye hamsaye
        bazigush-o-bahush ast - the neighbor's child is playful and smart).
        13. هوای امروز خنک و دلپذیر است (hava-ye emruz khonak-o-delpazir ast
        - today's weather is cool and pleasant). 14. شب‌های کویر پرستاره و
        ساکت است (shab-ha-ye kavir por-setare-o-saket ast - desert nights are
        starry and silent). 15. بازار قدیم پر از رنگ و بوست (bazar-e qadim
        por az rang-o-bust - the old bazaar is full of color and scent). 16.
        کتابی که خواندم طولانی ولی جالب بود (ketab-i ke khandam tulani vali
        jaleb bud - the book I read was long but interesting). 17. دوستم از
        من بلندتر است (dustam az man bolandtar ast - my friend is taller
        than me). 18. این سیب از آن سیب شیرین‌تر است (in sib az an sib
        shirin-tar ast - this apple is sweeter than that apple). 19. بهترین
        دوست من ساراست (behtarin dust-e man sarast - my best friend is
        Sara). 20. زیباترین فصل بهار است (zibatarin fasl bahar ast - the
        most beautiful season is spring)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches description as composition: twenty sentences
        where adjectives chain with ezafe, comparatives measure with از, and
        relative clauses (کتابی که خواندم) add depth - the full descriptive
        toolkit assembled in scenes of people and places. The demonstration
        program stores the twenty sentences, counts the ezafe links and
        comparatives in each, and verifies the superlative forms."""),
    key_points=[
        "20 detailed descriptive sentences: people, places, things.",
        "Ezafe chains stack description: زنِ مهربان و صبور (kind and patient woman).",
        "Comparatives with از: از من بلندتر (taller than me).",
        "Superlatives crown the description: بلندترین کوه ایران.",
        "Relative clause: کتابی که خواندم (the book that I read).",
        "Sample: زیباترین فصل بهار است - the most beautiful season is spring.",
    ],
    requirements=[
        "Describe three people and three places in five sentences each.",
        "Compare five pairs of things using از and the comparative.",
    ],
    standards=[
        "Descriptive syntax per Lazard and Mahootian reference grammars.",
    ],
    citations=[
        "Lazard, Gilbert. A Grammar of Contemporary Persian. Mazda Publishers; 1992. Noun phrases and relative clauses.",
        "Mahootian, Shahrzad. Persian. Routledge; 1997. Modification and comparison.",
    ],
    sig_lens=("Through the Signature lens, description is the covenant's "
              "portrait gallery: each person and place witnessed in sworn "
              "detail - tall, kind, starry, silent. This Signature reading "
              "treats every adjective chained as testimony given under "
              "oath."),
)

E(
    key="persian_story_1", name="Persian Short Story One",
    group="Stories", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence simple story in Persian - a boy and his kite - with
        line-by-line English translation. Simple present and basic
        vocabulary carry the whole tale, proving how much the learner can
        already say. 1. پسری در روستا زندگی می‌کند (pesari dar rusta zendegi
        mikonad - a boy lives in a village). 2. اسم او علی است (esm-e u ali
        ast - his name is Ali). 3. او هر روز به مدرسه می‌رود (u har ruz be
        madrese miravad - he goes to school every day). 4. بعد از مدرسه در
        مزرعه بازی می‌کند (bad az madrese dar mazrae bazi mikonad - after
        school he plays in the field). 5. او یک بادبادک قرمز دارد (u yek
        badbadak-e qermez darad - he has a red kite). 6. بادبادک در آسمان
        پرواز می‌کند (badbadak dar aseman parvaz mikonad - the kite flies in
        the sky). 7. علی می‌دود و می‌خندد (ali midavad-o-mikhandad - Ali runs
        and laughs). 8. دوستانش او را تشویق می‌کنند (dustanash u ra tashviq
        mikonand - his friends cheer him on). 9. خورشید غروب می‌کند (khorshid
        qorub mikonad - the sun sets). 10. علی خوشحال به خانه برمی‌گردد (ali
        khoshhal be khane barmigardad - Ali returns home happy). Story words:
        روستا (rusta - village)، مزرعه (mazrae - field)، بادبادک (badbadak -
        kite)، پرواز (parvaz - flight)، غروب (qorub - sunset). Moral: شادی در
        چیزهای ساده است (shadi dar chiz-ha-ye sade ast - happiness is in
        simple things)."""),
    how_it_works=textwrap.dedent("""\
        This record proves fluency is already happening: a complete ten-line
        story built only from foundation vocabulary and the simple present,
        each line paired with its English translation. The learner reads the
        Persian, covers the English, and retells the tale - the first real
        narrative performance. The demonstration program stores the ten
        lines, verifies the line-by-line pairing, and checks that every word
        comes from the foundation vocabulary."""),
    key_points=[
        "A complete 10-sentence story using only foundation vocabulary.",
        "Line-by-line English translation for every sentence.",
        "Simple present tense carries the whole narrative.",
        "Story words: روستا، مزرعه، بادبادک، پرواز، غروب.",
        "Moral: شادی در چیزهای ساده است - happiness is in simple things.",
    ],
    requirements=[
        "Retell the story in Persian without looking.",
        "Change three details and retell it again.",
    ],
    standards=[
        "Graded narrative per standard Persian learner-story conventions.",
    ],
    citations=[
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Reading passages.",
    ],
    sig_lens=("Through the Signature lens, the story is the covenant told "
              "as a tale: a boy, a red kite, a sunset - ten sworn lines "
              "proving the learner can already narrate a life. This "
              "Signature reading treats every retold story as the oath "
              "renewed in the learner's own voice."),
)

E(
    key="persian_story_2", name="Persian Short Story Two",
    group="Stories", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in the past tense - the baker of the old bazaar
        - with line-by-line English translation. Past simple and past
        continuous carry the narrative. 1. در بازار قدیم نانوایی بود (dar
        bazar-e qadim nanva-i bud - in the old bazaar there was a baker). 2.
        اسم او حسن بود (esm-e u hasan bud - his name was Hasan). 3. او هر صبح
        زود بیدار می‌شد (u har sobh zud bidar mishod - every morning he woke
        up early). 4. خمیر را ورز می‌داد (khamir ra varz midad - he kneaded
        the dough). 5. نان‌ها را در تنور می‌پخت (nan-ha ra dar tanur mipokht
        - he baked the breads in the clay oven). 6. بوی نان تازه در بازار
        می‌پیچید (bu-ye nan-e taze dar bazar mipichid - the smell of fresh
        bread drifted through the bazaar). 7. مردم صف می‌کشیدند (mardom saf
        mikeshidand - people lined up). 8. حسن به همه لبخند می‌زد (hasan be
        hame labkhand mizad - Hasan smiled at everyone). 9. یک روز باران
        شدیدی آمد (yek ruz baran-e shadidi amad - one day a heavy rain
        came). 10. ولی تنور حسن هنوز گرم بود (vali tanur-e hasan hanuz garm
        bud - but Hasan's oven was still warm). Story words: نانوا (nanva -
        baker)، تنور (tanur - clay oven)، خمیر (khamir - dough)، صف (saf -
        line/queue)، بوی (bu - smell). Moral: کار با عشق، نان گرم می‌دهد
        (kar ba eshq, nan-e garm midahad - work with love gives warm
        bread)."""),
    how_it_works=textwrap.dedent("""\
        This record moves narrative into the past: ten lines where past
        simple (بود، آمد) and past continuous (می‌شد، می‌پخت، می‌زد) share
        the storytelling, each line translated. The learner sees how Persian
        paints background action with می‌ + past stem and punctuates events
        with the simple past. The demonstration program stores the ten lines,
        classifies each verb as past-simple or past-continuous, and verifies
        the classification against the story text."""),
    key_points=[
        "A complete 10-sentence story in past tenses, line-by-line translated.",
        "Past simple for events (آمد، بود)؛ past continuous for background (می‌پخت).",
        "Story words: نانوا، تنور، خمیر، صف، بو.",
        "Moral: کار با عشق، نان گرم می‌دهد - work with love gives warm bread.",
    ],
    requirements=[
        "Retell the story in the past tense without looking.",
        "Convert three lines to past continuous and notice the change.",
    ],
    standards=[
        "Narrative past-tense usage per Lazard reference grammar.",
    ],
    citations=[
        "Lazard, Gilbert. A Grammar of Contemporary Persian. Mazda Publishers; 1992. Past tenses in narrative.",
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Reading passages.",
    ],
    sig_lens=("Through the Signature lens, the past-tense story is the "
              "covenant remembered: the baker's oven still warm through the "
              "rain, ten lines sworn as history. This Signature reading "
              "treats every بود as a seal pressed on what was."),
)

E(
    key="persian_story_3", name="Persian Short Story Three",
    group="Stories", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in future and conditional forms - the traveler's
        promise - with line-by-line English translation. The modern future
        (present tense with future meaning) and اگر (agar - if) conditionals
        carry the tale. 1. مسافری قول داد به روستایش برگردد (mosaferi qoul
        dad be rusta-ash bargardad - a traveler promised to return to his
        village). 2. او گفت: سال آینده برمی‌گردم (u goft: sal-e ayande
        barmigardam - he said: I will return next year). 3. اگر پول کافی
        داشته باشم، خانه می‌سازم (agar pul-e kafi dashte basham, khane
        misazam - if I have enough money, I will build a house). 4. اگر
        باران بیاید، دیرتر می‌رسم (agar baran biyayad, dirtar miresam - if
        it rains, I will arrive later). 5. مادرم منتظرم خواهد بود؟ نه -
        مادرم منتظرم است (madaram montazeram khahad bud? - no: madaram
        montazeram ast - will my mother be waiting? - my mother is waiting).
        6. او برایم آش خواهد پخت؟ نه - او برایم آش می‌پزد (u barayam ash
        khahad pokht? - no: u barayam ash mipazad - will she cook soup for
        me? - she cooks soup for me). 7. بچه‌های روستا دنبالم خواهند دوید
        (bache-ha-ye rusta donbalam khahand david - the village children
        will run after me). 8. اگر زود برسم، غروب را می‌بینم (agar zud
        beresam, qorub ra mibinam - if I arrive early, I will see the
        sunset). 9. قول، قول است (qoul, qoul ast - a promise is a promise).
        10. سال آینده، همه‌ی این‌ها واقعی خواهد شد (sal-e ayande, hame-ye
        in-ha vaqei khahad shod - next year, all of this will become real).
        Note: lines 5-7 show the literary future (خواهم/خواهد/خواهند +
        short infinitive) beside the modern spoken future, so the learner
        recognizes both. Story words: مسافر (mosafer - traveler)، قول (qoul -
        promise)، منتظر (montazer - waiting)، واقعی (vaqei - real). Moral:
        قولِ مرد، سند است (qoul-e mard, sanad ast - a person's promise is a
        signed deed)."""),
    how_it_works=textwrap.dedent("""\
        This record aims narrative at tomorrow: ten lines where اگر
        conditionals and both futures - the modern present-for-future and the
        literary خواهم future - promise, plan, and imagine. Lines 5-7
        deliberately pair the two futures so the learner recognizes the
        literary form in books while speaking the modern one. The
        demonstration program stores the ten lines, counts the conditional
        and future markers in each, and verifies the اگر clauses."""),
    key_points=[
        "A complete 10-sentence story in future/conditional forms, line-by-line translated.",
        "Conditionals: اگر باران بیاید، دیرتر می‌رسم (if it rains, I will arrive later).",
        "Modern future = present tense: سال آینده برمی‌گردم.",
        "Literary future = خواهم/خواهد + infinitive: واقعی خواهد شد.",
        "Story words: مسافر، قول، منتظر، واقعی.",
        "Moral: قولِ مرد، سند است - a promise is a signed deed.",
    ],
    requirements=[
        "Retell the story, then make five اگر promises of your own.",
        "Convert three modern futures to the literary خواهم form.",
    ],
    standards=[
        "Future and conditional per Lazard reference grammar.",
    ],
    citations=[
        "Lazard, Gilbert. A Grammar of Contemporary Persian. Mazda Publishers; 1992. Future and conditional.",
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Reading passages.",
    ],
    sig_lens=("Through the Signature lens, the future-tense story is the "
              "covenant not yet sealed: promises sworn toward next year, "
              "conditionals signed اگر by اگر. This Signature reading "
              "treats قولِ مرد، سند است as the whole method in one line - a "
              "promise is a signed deed."),
)

E(
    key="persian_idioms_proverbs", name="Persian Idioms and Proverbs",
    group="Mastery", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty Persian idioms and proverbs - each with literal translation,
        real meaning, and an example sentence in script, transliteration, and
        English. 1. از آب کره گرفتن (az ab kare gereftan - literally to take
        butter from water; to achieve the impossible): او از آب کره گرفت
        (u az ab kare gereft - he achieved the impossible). 2. آب از سرش
        گذشت (ab az sarash gozasht - literally water passed over his head;
        past the point of caring): دیگر آب از سرم گذشته (digar ab az saram
        gozashte - I am past caring now). 3. دست از پا درازتر برگشتن (dast
        az pa deraztar bargashtan - to return with hands longer than feet,
        i.e. empty-handed): دست از پا درازتر برگشت (dast az pa deraztar
        bargasht - he came back empty-handed). 4. هر چه بکاری همان بدروی
        (har che bekari haman bedravi - you reap what you sow): هر چه بکاری
        همان بدروی، پس خوب بکار (har che bekari haman bedravi, pas khub
        bekar - you reap what you sow, so sow well). 5. مرغ همسایه غاز است
        (morq-e hamsaye qaz ast - the neighbor's chicken is a goose; the
        grass is greener): مرغ همسایه همیشه غاز است (morq-e hamsaye hamishe
        qaz ast - the neighbor's chicken always looks like a goose). 6. جوجه
        را آخر پاییز می‌شمارند (juje ra akhar-e paiz mishomarand - they
        count the chicks at the end of autumn; do not count your chickens
        early): جوجه را آخر پاییز بشمار (juje ra akhar-e paiz beshomar - do
        not count your chickens before they hatch). 7. گر صبر کنی ز غوره
        حلوا سازی (gar sabr koni ze qure halva sazi - if you are patient,
        you will make halva from unripe grapes; patience achieves the
        impossible): صبر کن، ز غوره حلوا سازی (sabr kon, ze qure halva sazi -
        be patient and the impossible will ripen). 8. یک دست صدا ندارد (yek
        dast seda nadarad - one hand makes no sound; it takes two): یک دست
        صدا ندارد، با هم کار کنیم (yek dast seda nadarad, ba ham kar konim -
        one hand makes no sound, let us work together). 9. حرف حق تلخ است
        (harf-e haqq talkh ast - the word of truth is bitter; truth hurts):
        حرف حق تلخ است ولی باید گفت (harf-e haqq talkh ast vali bayad goft -
        truth is bitter but must be spoken). 10. سنگ بزرگ علامت نزدن است
        (sang-e bozorg alamat-e nazadan ast - a big stone is the sign of not
        throwing; overpromising means no action): سنگ بزرگ برندار (sang-e
        bozorg bar nadar - do not lift a stone too big). 11. نان به نرخ روز
        خوردن (nan be nerkh-e ruz khordan - to eat bread at the day's price;
        opportunism): او نان به نرخ روز می‌خورد (u nan be nerkh-e ruz
        mikhorad - he is an opportunist). 12. از کوره در رفتن (az kure dar
        raftan - to jump out of the furnace; to fly off the handle): از کوره
        در نرو (az kure dar naro - do not fly off the handle). 13. پا روی دم
        کسی گذاشتن (pa ruye dom-e kasi gozashtan - to step on someone's
        tail; to provoke): پا روی دم او نگذار (pa ruye dom-e u nagozar - do
        not provoke him). 14. دو پا را در یک کفش کردن (do pa ra dar yek
        kafsh kardan - to put two feet in one shoe; to be stubbornly
        insistent): دو پا را در یک کفش کرده (do pa ra dar yek kafsh karde -
        he is digging in his heels). 15. کار نیکو کردن از پر کردن است (kar-e
        niku kardan az por kardan ast - doing good work comes from practice;
        practice makes perfect): کار نیکو کردن از پر کردن است، تمرین کن (kar-e
        niku kardan az por kardan ast, tamrin kon - practice makes perfect,
        so practice). 16. قطره قطره جمع گردد وانگهی دریا شود (qatre qatre
        jam gardad vangahi darya shavad - drop by drop gathers, then
        becomes a sea; small efforts accumulate): قطره قطره دریا می‌شود
        (qatre qatre darya mishavad - little by little it becomes a sea).
        17. دو صد گفته چو نیم کردار نیست (do sad gofte cho nim kerdar nist -
        two hundred sayings are not worth half a deed; actions speak louder):
        عمل کن، دو صد گفته چو نیم کردار نیست (amal kon, do sad gofte cho nim
        kerdar nist - act, for deeds outweigh words). 18. دل به دریا زدن (del
        be darya zadan - to throw the heart into the sea; to take the
        plunge): دل به دریا زد و شروع کرد (del be darya zad-o shoru kard -
        he took the plunge and began). 19. سر از پا نشناختن (sar az pa
        nashenakhtan - to not know head from foot; to be overjoyed): از
        خوشحالی سر از پا نمی‌شناخت (az khoshhali sar az pa nemishenakht - he
        was overjoyed). 20. چشم به راه بودن (cheshm be rah budan - to have
        eyes on the road; to await eagerly): چشم به راهت هستم (cheshm be
        rahat hastam - I am eagerly awaiting you)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the soul of the language: twenty idioms and
        proverbs, each unpacked in three layers - the literal image, the real
        meaning, and a sentence that spends it correctly - because an idiom
        used wrong is worse than none. The images run through water, bread,
        hands, and the heart, the classic Persian symbolic stock. The
        demonstration program stores all twenty with their three layers,
        quizzes meaning against literal image, and verifies the full set."""),
    key_points=[
        "20 idioms/proverbs: literal translation + real meaning + example sentence.",
        "Classic images: water (از آب کره گرفتن)، bread (نان به نرخ روز)، hands (یک دست صدا ندارد).",
        "Proverbs of patience: گر صبر کنی ز غوره حلوا سازی؛ قطره قطره دریا شود.",
        "Proverbs of action: دو صد گفته چو نیم کردار نیست؛ کار نیکو کردن از پر کردن است.",
        "Sample: دل به دریا زد و شروع کرد - he took the plunge and began.",
    ],
    requirements=[
        "Use five idioms correctly in conversation or writing.",
        "Explain the literal image behind five proverbs to a friend.",
    ],
    standards=[
        "Proverb collection cross-checked against Dehkhoda dictionary entries.",
    ],
    citations=[
        "Dehkhoda, Ali-Akbar. Loghatname-ye Dehkhoda. University of Tehran Press. The great Persian dictionary, source of proverb attestations.",
        "Sharma, Sunil. Persian Poetry at the Indian Frontier. Permanent Black; 2000. On classical proverb stock.",
    ],
    sig_lens=("Through the Signature lens, the proverb is the covenant's "
              "wisdom sealed in an image: butter from water, halva from "
              "unripe grapes - the impossible sworn possible by patience. "
              "This Signature reading treats every مثل as a law of life "
              "signed by generations."),
)

E(
    key="persian_registers", name="Persian Formal and Polite Registers",
    group="Mastery", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen formal-versus-informal Persian pairs for letters, business,
        and elders - each pair in script, transliteration, and English, with
        a note on when to use which. 1. Informal: سلام! / Formal: با سلام و
        احترام (salam! / ba salam-o-ehteram - hi! / with greetings and
        respect - letter opening). 2. Informal: چطوری؟ / Formal: حال شما
        چطور است؟ (chetori? / hal-e shoma chetor ast? - how are you? -
        casual / formal). 3. Informal: ممنون / Formal: سپاسگزارم (mamnun /
        sepasgozaram - thanks / I am grateful). 4. Informal: ببخشید دیر کردم
        / Formal: پوزش می‌خواهم که دیر کردم (bebakhshid dir kardam / puzesh
        mikhaham ke dir kardam - sorry I am late - casual / formal). 5.
        Informal: بیا اینجا / Formal: لطفاً تشریف بیاورید (biya inja /
        lotfan tashrif biyavarid - come here - plain / honorific). 6.
        Informal: بشین / Formal: بفرمایید بنشینید (beshin / befarmayid
        benshinid - sit - plain / formal). 7. Informal: بهم بگو / Formal:
        لطفاً بفرمایید (beham begu / lotfan befarmayid - tell me - plain /
        formal). 8. Informal: می‌خوام برم / Formal: اجازه می‌خواهم بروم
        (mikham beram / ejaze mikhaham beravam - I want to go / I would like
        permission to go - leaving a gathering). 9. Informal: باشه / Formal:
        حتماً، با کمال میل (bashe / hatman, ba kamal-e meyl - okay / certainly,
        with pleasure). 10. Informal: نمی‌دونم / Formal: اطلاعی ندارم
        (nemidunam / ettela-i nadaram - I do not know - casual / formal). 11.
        Informal: خداحافظ / Formal: به امید دیدار (khodahafez / be omid-e
        didar - goodbye - standard / warm formal). 12. Informal: قربانت برم
        / Formal: لطف دارید (qorbanat beram / lotf darid - taarof thanks -
        intimate / formal; both deflect praise). 13. Business: قیمت چنده؟ /
        لطفاً قیمت را بفرمایید (qeymat chande? / lotfan qeymat ra befarmayid
        - what is the price? - market / business). 14. Elder: بابا، بیا /
        پدرجان، تشریف بیاورید (baba, biya / pedar-jan, tashrif biyavarid -
        dad, come - to father, casual / respectful). 15. Letter closing
        informal: دوستت دارم / formal: با احترام (dustet daram / ba ehteram -
        love you / respectfully). Honorific verbs: تشریف آوردن (tashrif
        avardan - to honor with one's presence, i.e. to come)، تشریف بردن
        (tashrif bordan - to go)، فرمودن (farmudan - to say, honorific). Rule:
        with elders, teachers, clients, and officials use شما forms +
        honorific verbs; with friends and family use تو forms."""),
    how_it_works=textwrap.dedent("""\
        This record teaches Persian as a two-story house: fifteen pairs where
        the same meaning climbs from the informal floor to the formal roof -
        plain verbs below, شما forms and honorific verbs (تشریف، فرمودن)
        above. Each pair names its stage - letter, business, elder - so the
        learner never bows to a friend or slaps an official on the back. The
        demonstration program stores the fifteen pairs, quizzes register
        choice by scenario, and verifies the honorific verb forms."""),
    key_points=[
        "15 formal vs informal pairs: letters, business, elders.",
        "Honorific verbs: تشریف آوردن (to come)، تشریف بردن (to go)، فرمودن (to say).",
        "Letter frames: با سلام و احترام ... با احترام.",
        "Taarof thanks: قربانت برم (intimate) / لطف دارید (formal).",
        "Rule: شما + honorifics for elders/clients/officials; تو for friends/family.",
        "Sample: اجازه می‌خواهم بروم - I would like permission to go.",
    ],
    requirements=[
        "Write a formal letter opening and closing in Persian.",
        "Convert five informal sentences to full formal register.",
    ],
    standards=[
        "Honorific usage per Beeman, Language, Status, and Power in Iran.",
    ],
    citations=[
        "Beeman, William O. Language, Status, and Power in Iran. Indiana University Press; 1986. Honorifics and register.",
        "Keshavarz, Mohammad Hossein. Forms of Address in Persian. University of Tehran; 1988.",
    ],
    sig_lens=("Through the Signature lens, register is the covenant's "
              "courtesy code: تشریف for the elder, تو for the friend - the "
              "same request sealed with different wax. This Signature "
              "reading treats every honorific as a bow written into "
              "grammar, respect made audible."),
)

E(
    key="persian_complex_sentences", name="Persian Compound and Complex Sentences",
    group="Mastery", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen long Persian sentences with clauses, connectors, and
        relative clauses - each parsed and translated, in script,
        transliteration, and English. 1. کتابی که دیروز خریدم خیلی جالب است
        (ketab-i ke diruz kharidam kheyli jaleb ast - the book that I bought
        yesterday is very interesting) [relative که]. 2. چون باران می‌آمد،
        در خانه ماندیم (chon baran miamad, dar khane mandim - because it was
        raining, we stayed home) [چون = because]. 3. اگر زود بیایی، با هم
        می‌رویم (agar zud biyayi, ba ham miravim - if you come early, we will
        go together) [اگر = if]. 4. هرچند خسته بودم، کار را تمام کردم
        (harchand khaste budam, kar ra tamam kardam - although I was tired, I
        finished the work) [هرچند = although]. 5. قبل از اینکه بروی، در را
        ببند (qabl az inke beravi, dar ra beband - before you go, close the
        door) [قبل از اینکه = before]. 6. بعد از اینکه ناهار خوردیم،
        پیاده‌روی کردیم (bad az inke nahar khordim, piyade-ravi kardim -
        after we ate lunch, we took a walk) [بعد از اینکه = after]. 7. او
        آن‌قدر سریع دوید که همه تعجب کردند (u anqadr sari david ke hame
        taajob kardand - he ran so fast that everyone was surprised) [آن‌قدر
        ... که = so ... that]. 8. نه تنها دیر آمد، بلکه عذر هم نخواست (na
        tanha dir amad, balke ozr ham nakhast - not only did he come late,
        but he did not even apologize) [نه تنها ... بلکه = not only ...
        but]. 9. هم فارسی حرف می‌زند، هم انگلیسی (ham farsi harf mizanad,
        ham engilisi - he speaks both Persian and English) [هم ... هم = both
        ... and]. 10. یا با ما بیا، یا خانه بمان (ya ba ma biya, ya khane
        beman - either come with us or stay home) [یا ... یا = either ...
        or]. 11. مردی که آنجا ایستاده، معلم من است (mard-i ke anja istade,
        moallem-e man ast - the man who is standing there is my teacher)
        [relative که]. 12. وقتی که رسیدم، همه رفته بودند (vaqti ke residam,
        hame rafte budand - when I arrived, everyone had gone) [وقتی که =
        when]. 13. جایی که بزرگ شدم، روستای کوچکی بود (ja-i ke bozorg
        shodam, rusta-ye kuchaki bud - the place where I grew up was a small
        village) [جایی که = where]. 14. آن‌چه گفتی درست بود (an-che gofti
        dorost bud - what you said was right) [آن‌چه = what/that which]. 15.
        با اینکه باران می‌آمد، بازی ادامه داشت (ba inke baran miamad, bazi
        edame dasht - even though it was raining, the game continued) [با
        اینکه = even though]. Connectors: که، چون، اگر، هرچند، قبل/بعد از
        اینکه، وقتی که، آن‌چه، با اینکه، نه تنها...بلکه، هم...هم، یا...یا."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the sentence as architecture: fifteen long
        sentences, each labeled with its connector in brackets, so the
        learner sees exactly which beam holds which clause. Relative که,
        causal چون, conditional اگر, concessive هرچند/با اینکه, temporal
        قبل/بعد از اینکه and وقتی که, and the correlative pairs نه تنها...بلکه,
        هم...هم, یا...یا are each proven twice where it matters. The
        demonstration program stores the fifteen sentences, extracts the
        connector from each, and verifies every sentence contains its labeled
        connector."""),
    key_points=[
        "15 long sentences, each parsed with its connector labeled.",
        "Relative که: کتابی که خریدم (the book that I bought).",
        "Causal چون، conditional اگر، concessive هرچند / با اینکه.",
        "Temporal: قبل از اینکه، بعد از اینکه، وقتی که.",
        "Correlatives: نه تنها...بلکه، هم...هم، یا...یا.",
        "Sample: چون باران می‌آمد، در خانه ماندیم - because it was raining, we stayed home.",
    ],
    requirements=[
        "Combine ten pairs of simple sentences with connectors from this record.",
        "Parse five sentences, labeling every clause and connector.",
    ],
    standards=[
        "Complex syntax per Lazard and Windfuhr reference grammars.",
    ],
    citations=[
        "Lazard, Gilbert. A Grammar of Contemporary Persian. Mazda Publishers; 1992. Complex sentences.",
        "Windfuhr, Gernot L. Persian Grammar. Mouton de Gruyter; 1979. Subordination.",
    ],
    sig_lens=("Through the Signature lens, the complex sentence is the "
              "covenant's full charter: clauses sworn to clauses with که "
              "and چون and اگر, each connector a witnessed link. This "
              "Signature reading treats every parsed sentence as a treaty "
              "with all its articles numbered."),
)

E(
    key="persian_conversation_market", name="Persian Conversation at the Market",
    group="Conversations", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue at the market - Persian script,
        transliteration, and English - annotated so the learner hears
        bargaining, taarof, and register in action. Speakers: سارا (Sara,
        the buyer) and فروشنده (forushande - the seller). 1. سارا: سلام،
        این انارها چنده؟ (salam, in anar-ha chande? - hello, how much are
        these pomegranates?). 2. فروشنده: سلام خانم، کیلویی چهل تومان
        (salam khanom, kilu-i chehel tuman - hello madam, forty tomans a
        kilo). 3. سارا: خیلی گران است! سی تومان نمی‌شود؟ (kheyli geran ast!
        si tuman nemishavad? - very expensive! Can you do thirty?). 4.
        فروشنده: سی؟ نه خانم، انارها تازه و شیرین‌اند (si? na khanom,
        anar-ha taze-o-shirin-and - thirty? No madam, the pomegranates are
        fresh and sweet). 5. سارا: آخرش چنده؟ (akharesh chande? - what is
        your final price?). 6. فروشنده: برای شما، سی و پنج (baraye shoma, si-o-panj
        - for you, thirty-five). 7. سارا: دو کیلو بدهید (do kilu bedehid -
        give me two kilos). 8. فروشنده: بفرمایید، تازه‌چین است (befarmayid,
        taze-chin ast - here you are, freshly picked). 9. سارا: زعفران هم
        دارید؟ (zaferan ham darid? - do you also have saffron?). 10. فروشنده:
        بله، مثقال چقدر می‌خواهید؟ (bale, mesqal cheqadr mikhahid? - yes,
        how many mesqals do you want?). 11. سارا: یک مثقال، برای مهمانی
        (yek mesqal, baraye mehmani - one mesqal, for a gathering). 12.
        فروشنده: زعفران قائنات، عالی است (zaferan-e qaenat, aali ast -
        Qaenat saffron, excellent). 13. سارا: جمعاً چقدر شد؟ (jaman cheqadr
        shod? - how much altogether?). 14. فروشنده: صد و ده تومان (sad-o-dah
        tuman - one hundred ten tomans). 15. سارا: تخفیف نمی‌دهید؟ (takhfif
        nemidahid? - no discount?). 16. فروشنده: صد تومان، برای مشتری خوب
        (sad tuman, baraye moshtari-ye khub - one hundred, for a good
        customer) [taarof: the seller honors the buyer]. 17. سارا: خیلی
        ممنون، دست شما درد نکنه (kheyli mamnun, dast-e shoma dard nakone -
        thank you so much). 18. فروشنده: خواهش می‌کنم، نوش جان (khahesh
        mikonam, nush-e jan - you are welcome, enjoy). 19. سارا: به امید
        دیدار! (be omid-e didar! - hope to see you again!). 20. فروشنده: به
        سلامت، باز هم تشریف بیاورید (be salamat, baz ham tashrif biyavarid -
        go in health, honor us again). Annotations: lines 1-7 show classic
        bargaining (گران است، آخرش چنده؟); lines 12-16 show taarof and the
        honorific مشتری خوب; line 20 uses the honorific تشریف بیاورید to a
        customer. Market words: انار (anar - pomegranate)، زعفران (zaferan -
        saffron)، مثقال (mesqal - traditional weight ~4.6g)، کیلو (kilu -
        kilo)."""),
    how_it_works=textwrap.dedent("""\
        This record stages the whole market in twenty lines: greeting,
        price-asking, bargaining, weighing, the taarof discount, thanks, and
        farewell - with annotations pointing out exactly where bargaining,
        taarof, and honorifics happen, so the learner can replay the scene.
        Speaker alternation is strict buyer/seller. The demonstration program
        stores the twenty lines, verifies strict speaker alternation, totals
        the purchase arithmetic, and quizzes the bargaining phrases."""),
    key_points=[
        "A 20-line bilingual market dialogue, annotated.",
        "Bargaining arc: چنده؟ → گران است → آخرش چنده؟ → تخفیف → deal.",
        "Taarof moment: صد تومان، برای مشتری خوب.",
        "Honorific close: باز هم تشریف بیاورید.",
        "Market words: انار، زعفران، مثقال، کیلو.",
        "Purchase total: دو کیلو انار + یک مثقال زعفران = صد تومان.",
    ],
    requirements=[
        "Role-play the dialogue twice, switching buyer and seller.",
        "Improvise a new ending where the buyer adds پسته (pistachios).",
    ],
    standards=[
        "Dialogue conventions per Beeman, bazaar interaction studies.",
    ],
    citations=[
        "Beeman, William O. Language, Status, and Power in Iran. Indiana University Press; 1986. Bazaar bargaining.",
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Dialogues.",
    ],
    sig_lens=("Through the Signature lens, the market dialogue is the "
              "covenant of trade performed: twenty lines, every offer and "
              "counter-offer sworn aloud, the deal sealed at صد تومان. This "
              "Signature reading treats the whole bazaar as a hall of "
              "signed treaties."),
)

E(
    key="persian_conversation_friend", name="Persian Conversation Meeting a Friend",
    group="Conversations", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue between old friends meeting over
        tea - Persian script, transliteration, and English - annotated for
        casual register, catching up, and making plans. Speakers: رضا (Reza)
        and امیر (Amir). 1. رضا: امیر! چه خبر؟ (amir! che khabar? - Amir!
        what is new?). 2. امیر: رضا! خوبی؟ دلم برایت تنگ شده بود (reza!
        khubi? delam barat tang shode bud - Reza! Are you well? I missed
        you). 3. رضا: منم همین‌طور، بشین چای بخور (manam hamin-tor, beshin
        chay bekhor - me too, sit, have tea). 4. امیر: چای تازه دم است؟
        (chay-e taze dam ast? - is the tea freshly brewed?). 5. رضا: آره،
        مادر بزرگم دم کرده (are, madarbozorgam dam karde - yes, my
        grandmother brewed it). 6. امیر: کار چطور است؟ (kar chetor ast? -
        how is work?). 7. رضا: شلوغ ولی خوب، پروژه‌ی جدید دارم (sholuq vali
        khub, proje-ye jadid daram - busy but good, I have a new project).
        8. امیر: خانواده خوب‌اند؟ (khanevade khub-and? - is the family
        well?). 9. رضا: همه خوب‌اند، سلام می‌رسانند (hame khub-and, salam
        miresanand - all well, they send greetings). 10. امیر: بچه‌ها
        بزرگ شدند؟ (bache-ha bozorg shodand? - have the kids grown?). 11.
        رضا: آره، پسرم امسال مدرسه می‌رود (are, pesaram emsal madrese
        miravad - yes, my son starts school this year). 12. امیر: چه زود!
        (che zud! - how fast!). 13. رضا: آخر هفته چه کار می‌کنی؟ (akhar-e
        hafte che kar mikoni? - what are you doing this weekend?). 14. امیر:
        کاری ندارم، چرا؟ (kari nadaram, chera? - nothing planned, why?). 15.
        رضا: بیا برویم کوه (biya beravim kuh - come, let us go to the
        mountains). 16. امیر: عالی است! ساعت چند؟ (aali ast! saat-e chand? -
        great! What time?). 17. رضا: شش صبح، سر کوچه (shesh-e sobh, sar-e
        kuche - six in the morning, at the alley corner). 18. امیر: باشه،
        صبحانه با من (bashe, sobhane ba man - deal, breakfast is on me).
        19. رضا: نه، تعارف نکن، دنگی (na, taarof nakon, dongi - no, do not
        stand on ceremony, we split it). 20. امیر: باشه دنگی! به امید دیدار
        (bashe dongi! be omid-e didar - deal, split! See you then).
        Annotations: lines 1-5 show casual greetings (چه خبر؟، آره); lines
        6-12 the catch-up formula (کار، خانواده، بچه‌ها); lines 13-20 making
        plans with the taarof over the bill (تعارف نکن، دنگی). Social words:
        دنگی (dongi - splitting the bill)، سر کوچه (sar-e kuche - the alley
        corner, classic meeting point)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches friendship talk as a three-act play: reunion,
        catch-up, and planning - twenty lines of casual register with
        annotations marking where the greetings, the catch-up formulas, and
        the bill-splitting taarof land. The learner absorbs the informal تو
        forms in their natural habitat. The demonstration program stores the
        twenty lines, verifies speaker alternation, and quizzes the casual
        phrases."""),
    key_points=[
        "A 20-line bilingual friends dialogue, annotated.",
        "Three acts: reunion (چه خبر؟)، catch-up (کار، خانواده)، plans (بیا برویم کوه).",
        "Casual register: آره، باشه، بشین - the تو world.",
        "Bill taarof: تعارف نکن، دنگی (do not stand on ceremony, we split it).",
        "Classic meeting point: شش صبح، سر کوچه.",
    ],
    requirements=[
        "Role-play the dialogue with a partner, then improvise a new plan.",
        "List every casual word and give its formal equivalent.",
    ],
    standards=[
        "Casual register per Beeman, Language, Status, and Power in Iran.",
    ],
    citations=[
        "Beeman, William O. Language, Status, and Power in Iran. Indiana University Press; 1986. Friendship and informal speech.",
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Dialogues.",
    ],
    sig_lens=("Through the Signature lens, the friends' dialogue is the "
              "covenant of companionship renewed: the reunion sworn, the "
              "news exchanged, the mountain trip promised at six. This "
              "Signature reading treats every باشه دنگی as friendship "
              "signed and sealed."),
)

E(
    key="persian_conversation_problem", name="Persian Conversation Solving a Problem",
    group="Conversations", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue solving a problem - a leaking sink
        and the plumber's visit - in Persian script, transliteration, and
        English, annotated for problem language: describing, diagnosing,
        agreeing, and confirming. Speakers: خانم محمدی (Mrs. Mohammadi, the
        homeowner) and لوله‌کش (lule-kesh - the plumber). 1. خانم محمدی:
        سلام، لطفاً بیایید، سینک نشتی دارد (salam, lotfan biyayid, sink
        nashti darad - hello, please come, the sink is leaking). 2. لوله‌کش:
        سلام خانم، کی شروع شد؟ (salam khanom, key shoru shod? - hello madam,
        when did it start?). 3. خانم محمدی: از دیشب، آب زیر سینک جمع می‌شود
        (az dishab, ab zir-e sink jam mishavad - since last night, water
        collects under the sink). 4. لوله‌کش: بگذارید نگاه کنم (begozarid
        negah konam - let me look). 5. لوله‌کش: لوله ترک خورده است (lule
        tarak khorde ast - the pipe is cracked). 6. خانم محمدی: جدی؟ تعمیر
        می‌شود؟ (jeddi? tamir mishavad? - really? Can it be repaired?). 7.
        لوله‌کش: بله، باید عوض شود (bale, bayad avaz shavad - yes, it must
        be replaced). 8. خانم محمدی: چقدر طول می‌کشد؟ (cheqadr tul mikeshad? -
        how long will it take?). 9. لوله‌کش: حدود یک ساعت (hodud-e yek
        saat - about an hour). 10. خانم محمدی: هزینه‌اش چقدر است؟ (hazine-ash
        cheqadr ast? - how much will it cost?). 11. لوله‌کش: با دستمزد، دویست
        تومان (ba dastmozd, devist tuman - with labor, two hundred tomans).
        12. خانم محمدی: کمی گران است، تخفیف نمی‌دهید؟ (kami geran ast,
        takhfif nemidahid? - a bit expensive, no discount?). 13. لوله‌کش:
        برای شما صد و هشتاد (baraye shoma sad-o-hashtad - for you, one
        hundred eighty). 14. خانم محمدی: قبول، شروع کنید (qabul, shoru
        konid - agreed, start). 15. لوله‌کش: آب را ببندید لطفاً (ab ra
        bebanded lotfan - please turn off the water). 16. خانم محمدی: بستم
        (bastam - I turned it off). 17. لوله‌کش: تمام شد، تست کنید (tamam
        shod, test konid - done, test it). 18. خانم محمدی: دیگر نشتی ندارد،
        عالی است (digar nashti nadarad, aali ast - no more leak, excellent).
        19. خانم محمدی: خیلی ممنون، دست شما درد نکنه (kheyli mamnun, dast-e
        shoma dard nakone - thank you so much). 20. لوله‌کش: خواهش می‌کنم،
        اگر مشکلی بود زنگ بزنید (khahesh mikonam, agar moshkeli bud zang
        bezanid - you are welcome, call if there is any problem).
        Annotations: lines 1-3 state the problem (نشتی دارد، جمع می‌شود);
        lines 4-7 diagnose (ترک خورده، باید عوض شود); lines 8-14 negotiate
        time and price; lines 15-20 confirm the fix and close warmly. Problem
        words: نشتی (nashti - leak)، ترک (tarak - crack)، تعمیر (tamir -
        repair)، دستمزد (dastmozd - labor fee)، هزینه (hazine - cost)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches problem-solving as a four-act procedure: state,
        diagnose, negotiate, confirm - twenty lines where the homeowner
        describes symptoms, the plumber diagnoses, they agree on time and
        price, and the fix is verified. Formal register runs throughout
        (بیایید، ببندید، زنگ بزنید) because service talk is polite talk. The
        demonstration program stores the twenty lines, verifies speaker
        alternation, and checks the four-act structure markers."""),
    key_points=[
        "A 20-line bilingual problem-solving dialogue, annotated.",
        "Four acts: state (نشتی دارد)، diagnose (ترک خورده)، negotiate (تخفیف)، confirm (تست کنید).",
        "Formal register throughout: service talk is polite talk.",
        "Price negotiation: دویست → صد و هشتاد تومان.",
        "Problem words: نشتی، ترک، تعمیر، دستمزد، هزینه.",
    ],
    requirements=[
        "Role-play the dialogue, then invent a new problem (e.g. a broken heater).",
        "Describe three household problems and their fixes in Persian.",
    ],
    standards=[
        "Service-register conventions per contemporary Persian usage.",
    ],
    citations=[
        "Beeman, William O. Language, Status, and Power in Iran. Indiana University Press; 1986. Service encounters.",
        "Thackston, Wheeler M. An Introduction to Persian. 4th ed. IBEX Publishers; 2009. Dialogues.",
    ],
    sig_lens=("Through the Signature lens, the repair dialogue is the "
              "covenant of making whole: the leak confessed, the crack "
              "diagnosed, the price agreed, the fix sworn tested. This "
              "Signature reading treats اگر مشکلی بود زنگ بزنید as the "
              "warranty signed on the work."),
)

E(
    key="persian_mastery_review", name="Persian Mastery Review and Full Reference",
    group="Mastery", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        The whole database in one teaching summary: alphabet, 200 core
        words, key grammar, and all phrase tables - the consolidated
        quick-reference that closes the ladder. ALPHABET (32 letters): ا ب پ
        ت ث ج چ ح خ د ذ ر ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن و ه ی - plus
        Persian digits ۰۱۲۳۴۵۶۷۸۹. VOWELS (6): a, e, o, long a, i, u.
        CONSONANTS (23): including خ، غ، ق، چ، ژ. 200 CORE WORDS (sample of
        the full set taught across records 4-24): مرد، زن، کودک، دوست، خانه،
        مدرسه، کتاب، آب، نان، شهر، کشور، روز، شب، ماه، خورشید، درخت، گل،
        ماشین، پول، وقت، کار، غذا، چای، در، پنجره، خوردن، نوشیدن، رفتن، آمدن،
        دیدن، شنیدن، گفتن، خواندن، نوشتن، کردن، شدن، بودن، داشتن، خواستن،
        دانستن، گرفتن، دادن، خوابیدن، بیدار شدن، نشستن، ایستادن، دویدن،
        خریدن، فروختن، یاد گرفتن، بزرگ، کوچک، خوب، بد، جدید، قدیمی، زیبا،
        بلند، کوتاه، گرم، سرد، سریع، کند، آسان، سخت، شاد، تمیز، گران، ارزان،
        نزدیک، دور، مهم، خیلی، همیشه، هرگز، امروز، دیروز، فردا، زود، دیر،
        آهسته، تند، با هم، تنها، شاید، حتماً، دوباره، من، تو، او، ما، شما،
        آنها، این، آن، کی، چه، کجا، چرا، چگونه، یک، دو، سه، چهار، پنج، شش،
        هفت، هشت، نه، ده، بیست، سی، صد، هزار، شنبه، یکشنبه، دوشنبه، جمعه،
        فروردین، مهر، بهار، تابستان، پاییز، زمستان، سلام، خداحافظ، ممنون،
        خواهش می‌کنم، ببخشید، صبح بخیر، شب بخیر، خوش آمدید، سر، چشم، دست،
        پا، قلب، شادی، غم، عشق، جنگل، دریا، آسمان، باران، برف، باد، بازار،
        تخفیف، مهمانی، گوشی، اینترنت، سینک، لوله - and the full 200 are
        verifiable in the demonstration program. KEY GRAMMAR: SOV word order
        (verb last)؛ no gender؛ plurals ـها/ـان؛ را marks definite objects؛
        negation نه/نـ prefix؛ questions with آیا or intonation؛ ezafe ـِ
        chains modifiers؛ present می‌ + stem؛ past stem + endings؛ perfects
        with participle + بودن؛ subjunctive بـ + stem؛ imperatives بـ + stem
        (بخور/بخورید). PHRASE TABLES: greetings (سلام تا به امید دیدار)،
        market (چنده؟ تا تخفیف)، travel (بلیط تا هتل)، health (درد تا نسخه)،
        tech (پیامک تا دانلود) - all thirty greetings, all twenty market
        lines, all twenty travel sentences retrievable from their records.
        THE LADDER RECAP: foundations (records 1-10: script, sounds, words,
        grammar) → compounded (records 11-24: themed sentences, tenses,
        questions, commands, descriptions) → advanced (records 25-34:
        stories, idioms, registers, complex sentences, conversations, this
        reference). Final charge: هر روز فارسی حرف بزن (har ruz farsi harf
        bezan - speak Persian every day)."""),
    how_it_works=textwrap.dedent("""\
        This record is the database folded into one page: the alphabet, the
        vowel and consonant counts, the 200-word core list, the grammar
        rules in one breath, the phrase tables by domain, and the ladder
        recap - everything a learner needs for review without reopening
        thirty-three records. It is also the record the database AI uses as
        its first answer card. The demonstration program verifies the full
        200-word list, the 32-letter alphabet, the grammar rule inventory,
        and the phrase-table counts, printing the consolidated reference as
        computed data."""),
    key_points=[
        "Full 200-word core vocabulary list, verifiable in the demo.",
        "32-letter alphabet + 6 vowels + 23 consonants in one table.",
        "All key grammar rules compressed to one screen.",
        "Phrase tables by domain: greetings, market, travel, health, tech.",
        "Ladder recap: foundations 1-10 → compounded 11-24 → advanced 25-34.",
        "Final charge: هر روز فارسی حرف بزن - speak Persian every day.",
    ],
    requirements=[
        "Recite the alphabet and count to 100 without the records.",
        "Write 200 words of Persian from memory using only this reference.",
    ],
    standards=[
        "Consolidated reference per the teaching-ladder canon.",
    ],
    citations=[
        "All citations of records 1-33 apply; this record consolidates them.",
        "Academy of Persian Language and Literature (فرهنگستان زبان و ادب فارسی). Dasturn-e xatt-e farsi.",
    ],
    sig_lens=("Through the Signature lens, the mastery review is the "
              "covenant's final seal: two hundred words witnessed, thirty-two "
              "letters sworn, every rule of the contract on one page. This "
              "Signature reading treats هر روز فارسی حرف بزن as the oath's "
              "last line - speak it daily, and the covenant lives."),
)
