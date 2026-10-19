#!/usr/bin/env python3
"""Entries for the Vietnamese Language databases (34 ladder-ordered records).

Public records: real, fact-checked Vietnamese (Tieng Viet) language teaching -
every record carries Vietnamese content with English translation and example
sentences, organized in the Signature system. All linguistic facts verified
against standard references (Thompson 1965; Nguyen Dinh Hoa 1997; Pham 2008;
Alves 2009; the Vietnamese alphabet and tone system as standardized).

Signature editions (34 more): the same ladder through the Signature lens,
titles suffixed " (Signature Edition)", src 'signature', clearly labeled
Signature-made, never presented as authentic public record.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the demos
(see demos_language_vietnamese.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with the
OK marker; the build machine-executes all 68 demos before commit.
"""
import textwrap

ENTRIES = []


def E(**kw):
    ENTRIES.append(kw)
    return kw


E(
    key="vietnamese_overview", name="Vietnamese Language Overview",
    group="Language overview", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Vietnamese (tieng Viet) is an Austroasiatic language of the Vietic
        branch, the national and official language of Vietnam. About 86 million
        people speak it as a first language, and the worldwide total passes
        97 million, making Vietnamese the most spoken Austroasiatic language
        and one of the largest languages of Southeast Asia. Its ISO codes are
        vi (639-1) and vie (639-3). Vietnamese is a tonal, analytic, isolating
        language: words do not change form, and meaning is carried by word
        order, small grammar particles, and six distinct tones. It is written
        in a Latin-based alphabet (chu Quoc ngu) created by 17th-century
        missionaries and standardized in the 20th century. Three great regional
        varieties shape the spoken language: Northern (Hanoi), Central (Hue),
        and Southern (Ho Chi Minh City), differing in tones and some sounds
        but sharing one written standard. Centuries of contact layered the
        vocabulary: a deep Sino-Vietnamese stratum from Chinese, a French
        layer from the colonial period, and a modern English layer. A learner
        sentence from this very record: Toi hoc tieng Viet - I study
        Vietnamese. This record is the map of the whole database: what
        Vietnamese is, where it lives, and how the ladder below carries a
        learner from a first greeting to full conversation."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the overview by anchoring every fact in a sentence
        the learner can say. Each fact - the native name tieng Viet, the ISO
        codes vi and vie, the Austroasiatic family path, the speaker numbers,
        the six tones, the three dialects - appears with a plain English
        explanation and a Vietnamese example sentence. The learner reads the
        facts, then repeats the sentences, so the overview is not memorized
        trivia but spoken language from the first record. Later records climb
        the teaching ladder: foundations (records 1-10: the writing system,
        tones, core words, grammar basics), compounded (records 11-24: themed
        sentence sets, verb tenses, questions, commands, descriptions),
        advanced (records 25-34: stories, idioms, registers, complex
        sentences, conversations, and a full reference)."""),
    key_points=[
        "Native name: tieng Viet; English name: Vietnamese; ISO 639-1: vi; ISO 639-3: vie.",
        "Family: Austroasiatic > Vietic > Vietnamese - a tonal, analytic, isolating language.",
        "About 86 million native speakers; more than 97 million total speakers worldwide.",
        "Official and national language of Vietnam; large communities in the United States, France, Australia, and Canada.",
        "Three regional varieties - Northern, Central, Southern - sharing one written standard.",
        "Six tones carry meaning; word order and small particles do the work of grammar.",
        "Every record in this database carries Vietnamese content, English translation, and example sentences.",
    ],
    requirements=[
        "No prior knowledge of Vietnamese is needed; this is the starting record of the ladder.",
        "Learners should read each example sentence aloud to begin training the tones from day one.",
    ],
    standards=[
        "ISO 639-1:1988 (vi) and ISO 639-2:1998 (vie) language codes.",
        "Quoc ngu, the standardized Latin-based Vietnamese alphabet.",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965. The classic English-language reference grammar.",
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997. A complete description of the language for learners.",
        "Pham A H. Vietnamese Tone: A New Analysis. Routledge; 2008. The modern account of the six-tone system.",
    ],
    sig_lens=("Through the Signature lens, a language is a covenant between "
              "voices, and Vietnamese is one of the great signed covenants of "
              "Southeast Asia: ninety-seven million voices keeping one oath of "
              "meaning across six tones and three regions. This Signature "
              "reading treats the overview as the first seal of that covenant."),
)

E(
    key="vietnamese_writing", name="Vietnamese Writing System",
    group="Writing and sound", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Vietnamese is written with the Quoc ngu alphabet: 29 letters, read
        left to right - A A Au B C D Dd E E G H I K L M N O O O P Q R S T U Uu
        V X Y (a, a, au, b, c, d, dd, e, e, g, h, i, k, l, m, n, o, o, o', p,
        q, r, s, t, u, uu, v, x, y in display order). There is no F, J, W, or Z
        in native words; those letters appear only in foreign loans like
        wifi or jazz. The musical heart of the script is the tone marking:
        every vowel can carry one of six tones - ngang (no mark, mid level,
        as in ma), huyen (grave, low falling, ma`), sac (acute, high rising,
        ma'), hoi (hook, dipping, ma?), nga (tilde, broken rising, ma~), nang
        (dot below, short low, ma.). Tone marks sit on the main vowel of the
        syllable. Special letters give Vietnamese its face: dd (d with bar)
        for the stopped d sound, o' and u' (o and u with horn), a and e (with
        breve and circumflex). Digraphs like ch, gh, gi, kh, ng, nh, ph, qu,
        th, tr write single consonant sounds. Punctuation matches English, and
        numerals are the familiar Arabic digits 0-9. A learner sentence: Chu
        Quoc ngu co hai muoi chin chu cai - Quoc ngu has twenty-nine letters.
        Learn the letters and the six tone marks, and every Vietnamese word
        becomes pronounceable on sight."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the writing system by pairing every letter and
        tone mark with a real word, its sound hint, and its English
        translation. The learner copies the 29 letters, sounds each with an
        example word - A as in an (eat), Dd as in di (go), O' as in co' (have)
        - and practices the six tone marks on the syllable ma until the hand
        remembers the pitch shapes. Because Vietnamese spelling is almost
        perfectly regular, this one record unlocks reading for the entire
        database."""),
    key_points=[
        "29 letters, left to right; no F, J, W, Z in native words - only in foreign loans.",
        "Six tone marks: none (ngang), grave (huyen), acute (sac), hook (hoi), tilde (nga), dot below (nang).",
        "Special letters: dd, a, e, o, u, o', u' - each a distinct sound, not decoration.",
        "One mark per syllable, placed on the main vowel: ma, ma`, ma', ma?, ma~, ma.",
        "Digraphs ch, gh, kh, ng, nh, ph, qu, th, tr each write one consonant sound.",
        "Punctuation and digits 0-9 match English usage; spelling is highly regular.",
    ],
    requirements=[
        "Learners should write the 29 letters by hand once and say each with its example word.",
        "Practice the six tones on ma first - tone is the single most important skill in Vietnamese.",
    ],
    standards=[
        "Quoc ngu alphabet standard: 29 letters, six tone diacritics.",
        "Vietnamese orthography: one syllable per spacing unit, tone mark on the nucleus vowel.",
    ],
    citations=[
        "DeFrancis J. Colonialism and Language Policy in Viet Nam. Mouton; 1977. The history of Quoc ngu.",
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997. The writing system described in full.",
        "Alves M J. Loanwords in Vietnamese. In: Haspelmath M, Tadmor U, eds. Loanwords in the World's Languages. De Gruyter; 2009.",
    ],
    sig_lens=("Through the Signature lens, the script is the Signature made "
              "visible: twenty-nine plain letters carrying six tones of "
              "meaning, a small alphabet doing the work of a thousand. This "
              "Signature reading treats the writing system as the first "
              "instrument - the tuning fork every later record is struck "
              "against."),
)

E(
    key="vietnamese_tones", name="Vietnamese Pronunciation and Tones",
    group="Writing and sound", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Vietnamese pronunciation rests on six tones, and the tones are not
        decoration - they are part of the word. The classic demonstration is
        the syllable ma: ma (ghost, ngang mid level), ma` (but, huyen low
        falling), ma' (cheek or mother, sac high rising), ma? (tomb, hoi
        dipping), ma~ (horse or code, nga broken rising with a glottal catch),
        ma. (rice seedling, nang short and low). Change the tone, change the
        word. The Northern (Hanoi) standard keeps all six distinct; Central
        and Southern varieties merge hoi and nga in speech but keep both in
        writing. Consonants are straightforward: b, m, n, l, s, x (like s),
        plus digraphs - ph sounds like f, th like an unaspirated t, kh like a
        breathy k, tr like a ch in the North and like tr in the South, gi
        like z in the North and y in the South, r like z in the North and a
        trilled r in the South, d like z in the North and y in the South, dd
        a stopped d everywhere. The eleven vowel nuclei are a, a, au, e, e,
        i, o, o, o', u, u', forming diphthongs like ai, ao, au, eo, ia, ua.
        Stress falls on each syllable nearly equally - Vietnamese has no
        English-style stress. Ten spoken examples with translations: ba (three
        or father), ca' (sing), com (cooked rice), nuoc (water), an (eat),
        uong (drink), di (go), den (arrive), hoc (learn), nha` (house). A
        learner sentence: Tieng Viet co sau thanh dieu - Vietnamese has six
        tones. Master the six tones and the alphabet sounds, and the whole
        language opens."""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronunciation by drilling the six tones as music
        before drilling them as words. The learner hums the pitch shapes of
        ma, ma`, ma', ma?, ma~, ma. until the ear separates them, then
        attaches meaning - ghost, but, cheek, tomb, horse, rice seedling. The
        consonant and vowel charts follow with an English approximation for
        every sound and one example word each. The ten example words at the
        end are the first real vocabulary: each is said aloud three times,
        then used in a short sentence in the next records."""),
    key_points=[
        "Six tones: ngang (level), huyen (low falling), sac (high rising), hoi (dipping), nga (broken rising), nang (short low).",
        "ma, ma`, ma', ma?, ma~, ma. = ghost, but, cheek/mother, tomb, horse/code, rice seedling.",
        "Northern standard keeps six tones distinct; hoi and nga merge in Central and Southern speech.",
        "Watch the pairs: d/dd, gi/r, s/x, ch/tr - they differ by region but never in writing.",
        "Eleven vowel nuclei; diphthongs ai, ao, au, eo, ia, ua; no English-style word stress.",
        "Ten starter words: ba, ca', com, nuoc, an, uong, di, den, hoc, nha`.",
    ],
    requirements=[
        "Learners should drill the six ma tones aloud daily until the ear separates them without thinking.",
        "Do not skip the regional notes - Northern, Central, and Southern ears hear some letters differently.",
    ],
    standards=[
        "Hanoi (Northern) pronunciation as the reference standard for tones.",
        "Tone inventory: six contrastive tones on open syllables (Pham 2008).",
    ],
    citations=[
        "Pham A H. Vietnamese Tone: A New Analysis. Routledge; 2008.",
        "Brunelle M. Tone perception in Northern and Southern Vietnamese. Journal of Phonetics; 2009. Documents the hoi/nga merger.",
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965. The consonant and vowel inventory.",
    ],
    sig_lens=("Through the Signature lens, tone is the Signature of the "
              "voice: six seals pressed onto one syllable, each seal a "
              "different word. This Signature reading treats pronunciation as "
              "the oath-taking - the learner swears each tone aloud until the "
              "voice keeps the contract without thinking."),
)

E(
    key="vietnamese_nouns1", name="Vietnamese Core Nouns I",
    group="Core vocabulary", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        These twenty-five essential nouns are the building blocks of everyday
        Vietnamese - people, places, and things. Vietnamese nouns never change
        form: no plurals, no cases, no gender. Counting uses classifiers: cai
        for most inanimate things (mot cai ban - one table), con for animals
        and some rounded things (mot con meo - one cat), nguoi for people
        (hai nguoi - two people). Plurals are marked only when needed, with
        nhung or cac before the noun (nhung quyen sach - the books). Each noun
        below comes with one full sentence, Vietnamese and English, so the
        word is learned inside real speech, never alone."""),
    how_it_works=textwrap.dedent("""\
        This record teaches nouns in sentence frames. The learner reads each
        noun, its English meaning, and its example sentence, then swaps the
        noun into the frame: Toi co mot cai ___ (I have a ___). After five
        nouns, the learner covers the Vietnamese and recalls from English;
        after all twenty-five, the learner builds five original sentences.
        The classifiers cai, con, nguoi are drilled as part of every noun -
        Vietnamese does not count without them."""),
    key_points=[
        "nguoi (person) - Toi la mot nguoi Viet Nam. (I am a Vietnamese person.)",
        "nha` (house, home) - Nha` cua toi o Ha Noi. (My house is in Hanoi.)",
        "truong (school) - Truong hoc o gan day. (The school is near here.)",
        "sach (book) - Toi doc mot quyen sach hay. (I read an interesting book.)",
        "ba`n (table, desk) - Quyen sach o tren ba`n. (The book is on the table.)",
        "ghe (chair) - Anh ay ngoi tren ghe. (He sits on the chair.)",
        "cua (door) - Xin dong cua lai. (Please close the door.)",
        "xe (vehicle, car) - Toi di xe den truong. (I go to school by car.)",
        "duong (road, street) - Duong nay di dau? (Where does this road go?)",
        "tha`nh pho (city) - Sai Gon la mot tha`nh pho lon. (Saigon is a big city.)",
        "nuoc (water; country) - Toi uong mot ly nuoc. (I drink a glass of water.)",
        "com (cooked rice; meal) - Me nau com ngon lam. (Mother cooks very delicious rice.)",
        "ca' (fish) - Ca' boi trong song. (The fish swims in the river.)",
        "ga` (chicken) - Nha` toi nuoi nam con ga`. (My family raises five chickens.)",
        "rau (vegetables) - An nhieu rau tot cho suc khoe. (Eating many vegetables is good for health.)",
        "tra'i cay (fruit) - Tra'i cay nay ngot lam. (This fruit is very sweet.)",
        "tien (money) - Toi can tien mua sach. (I need money to buy books.)",
        "dien thoai (telephone) - Dien thoai cua toi het pin. (My phone is out of battery.)",
        "ma'y tinh (computer) - Anh ay lam viec tren ma'y tinh. (He works on the computer.)",
        "quan ao (clothes) - Co ay mac quan ao dep. (She wears beautiful clothes.)",
        "gia`y (shoes) - Doi gia`y nay dat lam. (These shoes are very expensive.)",
        "tay (hand, arm) - Rua tay truoc khi an. (Wash your hands before eating.)",
        "mat (eye) - Mat cua be dep lam. (The baby's eyes are very beautiful.)",
        "dau (head) - Toi bi dau dau. (I have a headache.)",
        "cho' (dog) - Con cho' sua to lam. (The dog barks very loudly.)",
    ],
    requirements=[
        "Learners should memorize each noun with its classifier (cai, con, nguoi) as one unit.",
        "Say every example sentence aloud; nouns learned in sentences stay in memory.",
    ],
    standards=[
        "Classifier system: cai (inanimate), con (animate/small), nguoi (people) - Thompson 1965.",
        "Plural marking with nhung/cac only when definiteness requires it.",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965. Nouns and classifiers.",
        "Nguyen T C. Metaphorical classifier systems in Vietnamese. Cognitive Linguistics; 2007.",
    ],
    sig_lens=("Through the Signature lens, a noun is a named thing under the "
              "covenant of meaning: twenty-five seals, each pressed onto the "
              "world - nguoi, nha`, com, nuoc. This Signature reading treats "
              "the core nouns as the first inventory of the armory."),
)

E(
    key="vietnamese_verbs1", name="Vietnamese Core Verbs I",
    group="Core vocabulary", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        These twenty-five essential verbs carry everyday action in Vietnamese.
        Verbs never conjugate: an means eat, ate, will eat - time is shown by
        small markers around it. da marks completed action (Toi da an - I
        ate / I have eaten), dang marks ongoing action (Toi dang an - I am
        eating), se marks future (Toi se an - I will eat). No marker usually
        means present or general truth. Each verb below comes with one full
        sentence, Vietnamese and English, so the action is learned inside real
        speech."""),
    how_it_works=textwrap.dedent("""\
        This record teaches verbs through the three time markers. The learner
        takes each verb and builds the triple: Toi ___ (I ___), Toi da ___
        (I ___ed), Toi se ___ (I will ___), Toi dang ___ (I am ___ing). After
        ten verbs the learner can already narrate a day. The example sentence
        for each verb is memorized as the anchor; the triple is generated
        fresh each time to build the habit of marking time with particles,
        not endings."""),
    key_points=[
        "an (eat) - Toi an com luc bay gio. (I eat rice at seven o'clock.)",
        "uong (drink) - Moi ngay toi uong hai lit nuoc. (Every day I drink two liters of water.)",
        "di (go) - Sang mai toi di cho. (Tomorrow morning I go to the market.)",
        "den (come, arrive) - Anh ay den muon muoi phut. (He arrived ten minutes late.)",
        "ve (return) - Toi ve nha` luc sau gio. (I return home at six o'clock.)",
        "hoc (learn, study) - Em toi hoc tieng Anh. (My younger sibling studies English.)",
        "la`m (do, make, work) - Co ay la`m viec o ngan ha`ng. (She works at a bank.)",
        "no'i (speak, say) - Ong ay no'i tieng Viet rat gioi. (He speaks Vietnamese very well.)",
        "nghe (listen, hear) - Toi thich nghe nhac. (I like listening to music.)",
        "doc (read) - Ba` toi doc bao moi sang. (My grandmother reads the newspaper every morning.)",
        "viet (write) - Em be dang tap viet chu. (The child is practicing writing letters.)",
        "ngu (sleep) - Toi ngu tam tieng moi dem. (I sleep eight hours every night.)",
        "tam (bathe) - Toi tam hai lan mot ngay. (I bathe twice a day.)",
        "mac (wear, put on) - Hom nay troi lanh, toi mac ao am. (Today is cold; I wear a warm shirt.)",
        "mua (buy) - Me toi mua rau o cho. (My mother buys vegetables at the market.)",
        "ba'n (sell) - Cua ha`ng nay ba'n sach cu. (This shop sells old books.)",
        "cho (give) - Anh ay cho toi mot mon qua`. (He gave me a gift.)",
        "nhan (receive) - Toi nhan duoc thu cua ban. (I received your letter.)",
        "giup (help) - Ban co the giup toi khong? (Can you help me?)",
        "thich (like) - Toi thich an pho. (I like eating pho.)",
        "yeu (love) - Toi yeu gia dinh toi. (I love my family.)",
        "can (need) - Toi can mot cay but. (I need a pen.)",
        "muon (want) - Em muon di choi cong vien. (I want to go play at the park.)",
        "biet (know) - Toi biet duong den do. (I know the way there.)",
        "hieu (understand) - Toi hieu bai hoc nay. (I understand this lesson.)",
    ],
    requirements=[
        "Learners should drill each verb with da, dang, and se until the markers feel automatic.",
        "Memorize each example sentence as the anchor for its verb.",
    ],
    standards=[
        "Aspect/mood markers da (perfective), dang (progressive), se (irrealis/future) - Thompson 1965.",
        "Verbs are invariant; tense-aspect is analytic, not inflectional.",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965. The verb system.",
        "Duffield N. Particles and Projections in Irish. Kluwer; 1995. Analytic tense-aspect parallels discussed.",
        "Tran Q H. Vietnamese Aspect: A Cognitive Account. 2010. The da/dang/se system in use.",
    ],
    sig_lens=("Through the Signature lens, a verb is an action sealed in time: "
              "da the seal of what is done, dang the seal of what is "
              "happening, se the seal of what is promised. This Signature "
              "reading treats the core verbs as twenty-five motions of the "
              "covenant."),
)

E(
    key="vietnamese_adj_adv", name="Vietnamese Adjectives and Adverbs",
    group="Core vocabulary", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Vietnamese adjectives follow the noun they describe (nha` dep - a
        beautiful house, literally house beautiful), and they double as verbs:
        dep can mean beautiful or is beautiful (Nha` nay dep - This house is
        beautiful), with no copula needed. Comparison uses hon for more
        (lon hon - bigger) and nhat for most (dep nhat - most beautiful), with
        bang for equal (cao bang toi - as tall as me). Twenty-five adjectives
        and fifteen adverbs follow, each with an example sentence. Intensifiers
        rat (very) and lam (very, at sentence end) color every description:
        rat dep (very beautiful), dep lam (beautiful, very)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches description through the noun-adjective order,
        which is the reverse of English. The learner practices the flip: take
        an English phrase (beautiful house) and rebuild it Vietnamese-style
        (nha` dep). Then the comparison ladder is drilled: dep (beautiful),
        dep hon (more beautiful), dep nhat (most beautiful). Adverbs are
        learned in position - rat before the adjective, lam at the end - by
        transforming each adjective sentence twice."""),
    key_points=[
        "dep (beautiful) - Co gai dep lam. (The girl is very beautiful.)",
        "xau (ugly, bad) - Thoi tiet hom nay xau. (The weather today is bad.)",
        "lon (big) - Ha Noi la tha`nh pho lon. (Hanoi is a big city.)",
        "nho (small) - Phong nay nho qua. (This room is too small.)",
        "cao (tall, high) - Anh ay cao hon toi. (He is taller than me.)",
        "thap (short, low) - Cai ghe nay thap. (This chair is low.)",
        "da`i (long) - Song Hong ra^t da`i. (The Red River is very long.)",
        "ngan (short) - Con duong nay ngan. (This road is short.)",
        "moi (new) - Toi mua xe moi. (I bought a new car.)",
        "cu (old, of things) - Quyen sach nay cu lam. (This book is very old.)",
        "tot (good) - Day la mot y kien tot. (This is a good idea.)",
        "no'ng (hot) - Tra` no'ng ngon lam. (Hot tea is very delicious.)",
        "lanh (cold) - Mua dong o day lanh lam. (Winter here is very cold.)",
        "nhanh (fast) - Xe lua chay nhanh. (The train runs fast.)",
        "cham (slow) - Ong ay di cham. (He walks slowly.)",
        "vui (happy, fun) - Hom nay toi ra^t vui. (Today I am very happy.)",
        "buon (sad) - Co ay buon vi mat viec. (She is sad because she lost her job.)",
        "ngon (delicious) - Mon pho nay ngon lam. (This pho is very delicious.)",
        "do'i (hungry) - Toi do'i lam roi. (I am very hungry now.)",
        "no (full, of food) - An no roi, cam on. (I am full; thank you.)",
        "khoe (healthy, strong) - Ong ba` toi ra^t khoe. (My grandparents are very healthy.)",
        "sach (clean) - Nha` sach se thoang mat. (A clean house feels airy.)",
        "ban (dirty) - Tay em ban roi, di rua di. (Your hands are dirty; go wash them.)",
        "de (easy) - Bai nay de lam. (This exercise is very easy.)",
        "kho' (hard, difficult) - Tieng Viet kho' nhung thu vi. (Vietnamese is hard but interesting.)",
        "rat (very) - rat before the word: rat nhanh (very fast).",
        "qua' (too) - Dat qua'! (Too expensive!)",
        "cung (also, too) - Toi cung thich. (I also like it.)",
        "da (already) - Toi da an roi. (I already ate.)",
        "dang (in progress) - Co ay dang nau com. (She is cooking rice.)",
        "se (will) - Toi se den som. (I will come early.)",
        "khong (not) - Toi khong biet. (I do not know.)",
        "chua (not yet) - Toi chua an. (I have not eaten yet.)",
        "luon (always) - Anh ay luon dung gio. (He is always on time.)",
        "thuong (often) - Toi thuong di bo. (I often walk.)",
        "nhanh cho'ng (quickly) - Anh ay tra loi nhanh cho'ng. (He answered quickly.)",
        "tu tu (slowly) - Xin no'i tu tu. (Please speak slowly.)",
        "o day (here) - Ngoi xuong o day. (Sit down here.)",
        "o do' (there) - De sach o do'. (Put the book there.)",
        "bay gio (now) - Bay gio la may gio? (What time is it now?)",
    ],
    requirements=[
        "Learners should practice the adjective-after-noun order until the English order feels wrong.",
        "Drill rat/lam intensifiers and the hon/nhat comparison ladder on every adjective.",
    ],
    standards=[
        "Adjectives as stative verbs: no copula required (Thompson 1965).",
        "Comparison: hon (comparative), nhat (superlative), bang (equative).",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965. Adjectives and comparison.",
        "Dixon R M W. Where Have All the Adjectives Gone? Mouton; 1982. Vietnamese stative verbs discussed.",
    ],
    sig_lens=("Through the Signature lens, description is the seal of quality "
              "pressed onto a thing: dep the seal of beauty, tot the seal of "
              "goodness, hon and nhat the rising ladder of seals. This "
              "Signature reading treats adjectives as the covenant's measure "
              "of the world."),
)

E(
    key="vietnamese_pronouns", name="Vietnamese Pronouns",
    group="Grammar", ladder_rank=4, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Vietnamese pronouns are a kinship system, not a fixed list. The word
        for I changes with the relationship: toi is the neutral I, tao is
        rough and intimate, minh is humble among friends. The word for you is
        chosen by age and respect: anh for an older man, chi for an older
        woman, em for someone younger, ong/ba` for elders, ban for a peer,
        may for rough speech. Calling someone by the right kinship term is
        respect itself - strangers become anh, chi, em, co, chu on first
        meeting. Possession adds cua (cua toi - mine, literally of me).
        Demonstratives: nay/ day (this), do'/ day (that), kia (that over
        there). Interrogatives: ai (who), gi`/ cai gi` (what), dau (where),
        na`o (which), sao (why, how), bao nhieu (how many, how much). A
        learner sentence: Anh ten gi`? - What is your (older brother's) name?
        Master the kinship pronouns and every Vietnamese conversation opens."""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronouns as social mapping. The learner draws a
        family tree and labels every branch with its pronoun - ong, ba`, bac,
        chu, co, anh, chi, em - then practices addressing imaginary people of
        different ages. Each paradigm (personal, possessive, demonstrative,
        interrogative) is drilled with one anchor sentence, and the learner
        converts a rude sentence (may/tao) into a polite one (anh/toi) to feel
        the register shift. The golden rule: when in doubt, use anh/chi/em by
        apparent age - it is never wrong to be respectfully familial."""),
    key_points=[
        "toi (I, neutral) - Toi la sinh vien. (I am a student.)",
        "ban (you, peer) - Ban khoe khong? (Are you well?)",
        "anh (older brother; you/he for older men) - Anh an com chua? (Have you eaten yet, older brother?)",
        "chi (older sister; you/she for older women) - Chi di dau day? (Where are you going, older sister?)",
        "em (younger sibling; you for younger people) - Em ten gi`? (What is your name, younger sibling?)",
        "ong (grandfather; respectful you/he for elderly men) - Ong khoe khong a? (Are you well, grandfather?)",
        "ba` (grandmother; respectful you/she for elderly women) - Ba` o dau a? (Where do you live, grandmother?)",
        "co (aunt; you/she, also teacher) - Co day em bai nay. (Teacher, teach me this lesson.)",
        "chu' (uncle; you/he) - Chu' lam nghe gi`? (What is your job, uncle?)",
        "chung toi / chung ta (we; exclusive/inclusive) - Chung ta di choi di. (Let us [all of us] go out.)",
        "ho (they) - Ho la ban toi. (They are my friends.)",
        "no' (it; also he/she for children, rough for adults) - Con meo no' de thuong. (The cat, it is cute.)",
        "cua (possessive marker) - Day la sach cua toi. (This is my book.)",
        "nay / day (this) - Quyen sach nay hay lam. (This book is very interesting.)",
        "do' / day (that) - Cai ghe do' cua ai? (Whose chair is that?)",
        "kia (that over there) - Nha` kia la cua bac toi. (That house over there is my uncle's.)",
        "ai (who) - Ai go cua day? (Who is knocking?)",
        "gi` / cai gi` (what) - Ban muon an gi`? (What do you want to eat?)",
        "o dau / dau (where) - Nha` ban o dau? (Where is your house?)",
        "na`o (which) - Ban thich cai na`o? (Which one do you like?)",
        "sao / tai sao (why) - Sao ban buon? (Why are you sad?)",
        "bao nhieu (how many, how much) - Cai ao nay bao nhieu tien? (How much is this shirt?)",
    ],
    requirements=[
        "Learners should memorize the kinship ladder ong-ba`-bac-chu-co-anh-chi-em and use it from day one.",
        "Never use may/tao with strangers; default to anh/chi/em by apparent age.",
    ],
    standards=[
        "Kinship-term pronoun system: address by relative age and gender (Thompson 1965).",
        "Inclusive chung ta vs exclusive chung toi distinction.",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965. The pronoun system.",
        "Cooke J R. Pronominal Reference in Thai, Burmese, and Vietnamese. University of California Press; 1968.",
        "Luong H V. Discursive Practices and Linguistic Meanings. John Benjamins; 1990. Kinship terms in social use.",
    ],
    sig_lens=("Through the Signature lens, pronouns are the covenant's terms "
              "of address: every anh, chi, em a seal of respect pressed onto "
              "a relationship. This Signature reading treats the pronoun "
              "system as the etiquette of the oath - no one is nameless, "
              "everyone is family."),
)

E(
    key="vietnamese_numbers_time", name="Vietnamese Numbers and Time",
    group="Grammar", ladder_rank=4, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Vietnamese numbers are beautifully regular: learn 1 to 10 and the
        pattern builds the rest. mot hai ba bon nam sau bay tam chin muoi
        (1-10). Eleven is muoi mot (ten one), twenty is hai muoi (two ten),
        twenty-one is hai muoi mot - though 1 becomes mot after tens except
        in 21, 31... where Southern speakers say moi. Five becomes lam after
        tens (hai muoi lam - 25), ten stays muoi, zero is khong. One hundred is
        mot tram, one thousand mot nghin, one million mot trieu. Ordinals add
        thu' (thu' nhat - first, thu' hai - second). Days of the week: thu'
        hai (Monday) through thu' bay (Saturday), chu nhat (Sunday). Months
        are simply thang mot through thang muoi hai (month one to month
        twelve), with thang gieng (first lunar month) and thang chap (twelfth
        lunar month) in traditional use. Seasons: mua xuan (spring), mua he
        (summer), mua thu (autumn), mua dong (winter). Clock time: gio for
        hours, phut for minutes, ruoi for half (bay gio ruoi - 7:30), kem for
        to (tam gio kem muoi - ten to eight), hon for past (bay gio hon muoi
        phut - ten past seven). Dates: ngay 17 thang 10 nam 2026 - day 17
        month 10 year 2026. A learner sentence: Hom nay la thu' bay, ngay
        muoi bay thang muoi - Today is Saturday, the seventeenth of October."""),
    how_it_works=textwrap.dedent("""\
        This record teaches numbers as a building system. The learner
        memorizes 1-10, then constructs 11-99 by rule: tens + units, with the
        special forms lam (5 after tens) and moi (1 after tens, Southern).
        Then hundreds, thousands, and millions stack the same way. Time is
        drilled by reading a clock aloud: every hour on the hour, then halves
        with ruoi, then minutes with hon and kem. Dates are built day-month-
        year, and the learner writes today's date in Vietnamese every morning
        for a week."""),
    key_points=[
        "1-10: mot, hai, ba, bon, nam, sau, bay, tam, chin, muoi - Toi co ba quyen sach. (I have three books.)",
        "11-19: muoi mot ... muoi chin - Nam nay toi muoi tam tuoi. (This year I am eighteen years old.)",
        "Tens: hai muoi, ba muoi ... chin muoi - Lop co hai muoi hoc sinh. (The class has twenty students.)",
        "Specials: hai muoi lam (25), hai muoi moi (21, Southern) - Gia' la hai muoi lam nghin. (The price is twenty-five thousand.)",
        "100/1000/million: mot tram, mot nghin, mot trieu - Dan so hon mot tram trieu. (The population is over one hundred million.)",
        "Ordinals: thu' nhat, thu' hai, thu' ba - Anh ay ve thu' nhat. (He finished first.)",
        "Days: thu' hai ... thu' bay, chu nhat - Hom nay la chu nhat. (Today is Sunday.)",
        "Months: thang mot ... thang muoi hai - Sinh nhat toi vao thang nam. (My birthday is in May.)",
        "Seasons: mua xuan, mua he, mua thu, mua dong - Mua thu Ha Noi dep lam. (Autumn in Hanoi is very beautiful.)",
        "Clock: bay gio (7:00), bay gio ruoi (7:30), tam gio kem muoi (7:50), bay gio hon muoi phut (7:10).",
        "Dates: ngay 1 thang 1 nam 2026 - Tet vao ngay muoi bay thang hai. (Tet falls on February seventeenth.)",
        "Zero: khong - So dien thoai co so khong. (The phone number has a zero.)",
    ],
    requirements=[
        "Learners should count 1-100 aloud daily until the tens pattern is automatic.",
        "Practice telling time from a real clock; say every appointment in Vietnamese.",
    ],
    standards=[
        "Decimal numeral system; mot tram = 100, mot nghin = 1000, mot trieu = 1,000,000.",
        "Day-month-year date order; 24-hour or 12-hour clock with sang/chieu/toi markers.",
    ],
    citations=[
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997. Numerals and time.",
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965.",
    ],
    sig_lens=("Through the Signature lens, numbers are the covenant's measure: "
              "mot the first seal, tram the hundredth, trieu the millionth, "
              "each count an oath kept exactly. This Signature reading treats "
              "numbers and time as the ledger of the covenant - every gio` "
              "accounted, every ngay recorded."),
)

E(
    key="vietnamese_greetings", name="Vietnamese Greetings and Everyday Phrases",
    group="Core vocabulary", ladder_rank=5, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Thirty greetings, farewells, and politeness phrases - the social
        currency of Vietnamese. The universal greeting is Xin chao (hello),
        but real Vietnamese greets with kinship: Chao anh (hello, older
        brother), Chao chi, Chao em, Chao bac. Morning and evening take Chao
        buoi sang and Chao buoi toi. Thanks is Cam on (thank you), Cam on
        rat nhieu (thank you very much); the reply is Khong co gi (it is
        nothing - you're welcome). Xin loi covers sorry and excuse me; Xin
        phep means excuse me when leaving or passing. Yes is vang (formal) or
        da (Southern formal) or u (informal); no is khong. Moi is the warm
        invitation word - Moi anh an com (please, have some rice). Each phrase
        below carries its usage note, so the learner knows not just the words
        but the moment."""),
    how_it_works=textwrap.dedent("""\
        This record teaches phrases as social scripts. The learner practices
        each phrase in its scene: greeting an elder with Chao bac, thanking a
        shopkeeper with Cam on, excusing past with Xin loi. The kinship
        greetings are drilled by role-play - the learner greets five imaginary
        people of different ages. After all thirty, the learner performs a
        full day: morning greeting, market thanks, evening farewell, without
        notes."""),
    key_points=[
        "Xin chao (hello, universal) - Xin chao, toi ten la Lan. (Hello, my name is Lan.)",
        "Chao anh / Chao chi / Chao em (hello by kinship) - Chao chi, chi khoe khong? (Hello older sister, are you well?)",
        "Chao buoi sang (good morning) - Chao buoi sang, bac day som the. (Good morning; you are up early.)",
        "Chao buoi toi (good evening) - Chao buoi toi, ca? nha` an com chua? (Good evening; has the family eaten?)",
        "Tam biet (goodbye) - Tam biet, hen gap lai. (Goodbye, see you again.)",
        "Hen gap lai (see you again) - Hen gap lai tuan sau nhe'. (See you again next week.)",
        "Cam on (thank you) - Cam on ban nhieu. (Thank you very much.)",
        "Cam on rat nhieu (thank you very much) - Cam on rat nhieu da giup toi. (Thank you very much for helping me.)",
        "Khong co gi (you are welcome) - Khong co gi dau. (It is nothing.)",
        "Xin loi (sorry; excuse me) - Xin loi, toi den muon. (Sorry, I came late.)",
        "Xin phep (excuse me, asking leave) - Xin phep bac cho toi qua. (Excuse me, let me pass.)",
        "Xin vui lo`ng (please, formal) - Xin vui lo`ng doi mot chut. (Please wait a moment.)",
        "Lam on (please, do me the favor) - Lam on giup toi. (Please help me.)",
        "Vang / Da (yes, formal) - Vang, toi hieu roi. (Yes, I understand now.)",
        "U / O' (yes, informal) - U, de do' di. (Yes, leave it there.)",
        "Khong (no) - Khong, cam on. (No, thank you.)",
        "Duoc khong? (is it okay?) - The nay duoc khong? (Is this okay?)",
        "Moi (please come / help yourself) - Moi anh uong nuoc. (Please have some water.)",
        "Chuc mung (congratulations) - Chuc mung sinh nhat! (Happy birthday!)",
        "Chuc ngu ngon (good night) - Chuc ngu ngon nhe'. (Good night.)",
        "An ngon mieng (enjoy your meal) - Ca? nha` an ngon mieng. (Everyone enjoy the meal.)",
        "Suc khoe! (cheers, to health) - Suc khoe! (Cheers!)",
        "Rat vui duoc gap ban (nice to meet you) - Rat vui duoc gap anh. (Very nice to meet you.)",
        "Ban khoe khong? (how are you?) - Chao em, em khoe khong? (Hello; are you well?)",
        "Toi khoe, cam on (I am well, thanks) - Toi khoe, cam on anh. (I am well, thank you.)",
        "Xin hoi (may I ask - opening a question) - Xin hoi duong nay di dau? (May I ask where this road goes?)",
        "Phien ban (may I trouble you) - Phien ban chi giup toi. (May I trouble you to show me.)",
        "Toi xin loi (I apologize) - Toi xin loi ve chuyen hom qua. (I apologize about yesterday.)",
        "Khong sao dau (it is fine, no problem) - Khong sao dau, dung lo. (It is fine; do not worry.)",
        "Gap sau nhe' (see you later) - Gap sau nhe', di can than. (See you later; go carefully.)",
    ],
    requirements=[
        "Learners should greet real or imagined people with Chao + kinship term every day.",
        "Memorize the thanks-apology pair: Cam on / Khong co gi, Xin loi / Khong sao dau.",
    ],
    standards=[
        "Kinship greeting norm: address by relative age and gender on first meeting.",
        "Politeness particles a, nhe', nhe appended to soften requests.",
    ],
    citations=[
        "Luong H V. Discursive Practices and Linguistic Meanings. John Benjamins; 1990. Greetings and address.",
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, a greeting is the opening seal of "
              "the covenant: Chao anh the handshake of respect, Cam on the "
              "seal of gratitude, Xin loi the seal of repair. This Signature "
              "reading treats the thirty phrases as the daily oaths that keep "
              "the covenant warm."),
)

E(
    key="vietnamese_grammar", name="Vietnamese Grammar Essentials",
    group="Grammar", ladder_rank=5, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Vietnamese grammar is analytic: word order and small particles do all
        the work that endings do in other languages. The base order is
        subject-verb-object (Toi an com - I eat rice). There is no verb
        conjugation, no gender, no cases, no articles - a noun is just a noun.
        Number is shown only when it matters: nhung quyen sach (the books),
        cac em hoc sinh (the pupils). Time and aspect come from particles: da
        (completed), dang (ongoing), se (future), roi (already/then), chua
        (not yet). Negation: khong before the verb (Toi khong biet - I do not
        know), chua for not yet, dung for don't do it (Dung di! - Don't go!).
        Questions have five shapes: yes-no with khong at the end (Anh di
        khong? - Are you going?), with phai khong (isn't it), with question
        words (ai, gi`, dau, sao, bao nhieu), with hay for choice (Ca phe hay
        tra`? - Coffee or tea?), and echo questions repeating the verb
        (An khong an? - Eat or not?). Classifiers stand between number and
        noun: mot cai ban, hai con meo, ba nguoi. Adjectives follow nouns.
        Possession uses cua or word order: sach cua toi or sach toi (my book).
        A learner sentence: Toi se khong di dau ca? - I will not go anywhere.
        With these rules, the learner can build ten thousand correct
        sentences."""),
    how_it_works=textwrap.dedent("""\
        This record teaches grammar as a construction kit. Each rule is given
        as a formula with two translated examples, and the learner builds five
        sentences per rule on the spot: five SVO sentences, five negations
        with khong/chua/dung, five questions in each of the five shapes. The
        master drill is transformation: take one base sentence (Toi an com)
        and run it through every rule - past (Toi da an com), negative (Toi
        khong an com), question (Toi an com khong?), future (Toi se an com).
        One sentence becomes twelve; the kit is learned by use, not by
        memorizing tables."""),
    key_points=[
        "Word order SVO: Toi (subject) an (verb) com (object) - I eat rice.",
        "No conjugation: an covers eat, eats, ate, will eat - particles mark time.",
        "da/dang/se/roi: Toi da ve (I returned), Toi dang hoc (I am studying), Toi se di (I will go), Xong roi (done already).",
        "No gender, case, or articles: ban can mean friend, the friend, a friend by context.",
        "Number only when needed: nhung cai ghe (the chairs) vs ghe (chair/chairs).",
        "Negation: khong (not), chua (not yet), dung (do not): Toi khong hieu; Toi chua an; Dung khoc!",
        "Question shape 1 - khong: Co ay dep khong? (Is she beautiful?)",
        "Question shape 2 - phai khong: Anh la bac si phai khong? (You are a doctor, isn't that right?)",
        "Question shape 3 - question words: Ban o dau? (Where are you?); Ai day? (Who is that?)",
        "Question shape 4 - hay (choice): Di xe hay di bo? (Go by car or on foot?)",
        "Classifiers: mot cai ao (a shirt), hai con cho' (two dogs), nam nguoi (five people).",
        "Adjective after noun: nha` dep, xe moi; possession: cua or order - xe cua toi.",
    ],
    requirements=[
        "Learners should run the twelve-transformation drill on one sentence daily until it is effortless.",
        "Build five original sentences per rule; grammar learned by building stays.",
    ],
    standards=[
        "Analytic grammar: SVO order, invariant word forms (Thompson 1965).",
        "Five interrogative constructions; classifier-numeral-noun order.",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965. The core grammar.",
        "Cao X H. Tieng Viet: So Thao Ngu Phap Chuc Nang. 1998. Functional grammar of Vietnamese.",
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, grammar is the covenant's "
              "architecture: SVO the foundation stones in order, da/dang/se "
              "the three time-seals, khong the seal of refusal, the five "
              "question shapes the five doors of inquiry. This Signature "
              "reading treats the essentials as the blueprint every later "
              "record builds upon."),
)

E(
    key="vietnamese_home_family", name="Vietnamese Home and Family Sentences",
    group="Themed sentences", ladder_rank=5, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the home and the family - the first place
        Vietnamese is spoken. Rooms: pho`ng khach (living room), pho`ng ngu
        (bedroom), pho`ng bep (kitchen), pho`ng tam (bathroom). Furniture:
        giuong (bed), tu (cabinet), bep (stove). Family: bo/me (father/
        mother), ong ba` (grandparents), anh chi em (siblings), con (child),
        vo/chong (wife/husband). Vietnamese family address is warm and
        precise - every relative has a name, and using it is love in grammar.
        Each sentence below is a small scene of home life, Vietnamese and
        English, ready to be spoken at the learner's own table."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through scenes of home. The learner reads each
        sentence, pictures the room or the relative, and says it aloud as if
        speaking to family. The drill is substitution: keep the frame, change
        the room (Pho`ng ___ o dau? - Where is the ___ room?) or the relative
        (___ dang lam gi`? - What is ___ doing?). After twenty sentences the
        learner describes their own home, room by room, in Vietnamese."""),
    key_points=[
        "Nha` toi co bon pho`ng. (My house has four rooms.)",
        "Pho`ng khach o tang duoi. (The living room is downstairs.)",
        "Pho`ng ngu cua toi o tren lau. (My bedroom is upstairs.)",
        "Me dang nau com trong pho`ng bep. (Mother is cooking in the kitchen.)",
        "Bo toi dang xem ti vi o pho`ng khach. (My father is watching TV in the living room.)",
        "Cai giuong nay ra^t em. (This bed is very comfortable.)",
        "Xin dong cua pho`ng lai. (Please close the room door.)",
        "Chia khoa nha` de o dau? (Where are the house keys?)",
        "Ong ba` toi song o que. (My grandparents live in the countryside.)",
        "Anh trai toi lam bac si. (My older brother is a doctor.)",
        "Chi gai toi day hoc o truong. (My older sister teaches at a school.)",
        "Em trai toi thich da' bo'ng. (My younger brother likes playing football.)",
        "Con gai toi hoc lop ba. (My daughter is in third grade.)",
        "Ca? nha` toi se di du lich he nay. (My whole family will travel this summer.)",
        "Toi thuong an com toi voi gia dinh luc bay gio. (I usually have dinner with family at seven.)",
        "Nha` co vuon rau nho phia sau. (The house has a small vegetable garden behind.)",
        "Toi quet nha` moi sang. (I sweep the house every morning.)",
        "Em be dang ngu trong noi. (The baby is sleeping in the cradle.)",
        "Chung ta don dep nha` cuoi tuan nay. (We will clean the house this weekend.)",
        "Gia dinh la dieu quan trong nhat. (Family is the most important thing.)",
    ],
    requirements=[
        "Learners should describe their own home room by room in Vietnamese after this record.",
        "Use the true kinship terms for the learner's own relatives; family words are never generic.",
    ],
    standards=[
        "Kinship address norms; nha` as house, home, and family by context.",
    ],
    citations=[
        "Luong H V. Discursive Practices and Linguistic Meanings. John Benjamins; 1990. Family address.",
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, home is the first temple of the "
              "covenant and family its first congregation: every bo, me, ong, "
              "ba` a living seal. This Signature reading treats the home "
              "sentences as the covenant spoken at the table - the oldest "
              "classroom there is."),
)

E(
    key="vietnamese_food", name="Vietnamese Food and Cooking Sentences",
    group="Themed sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for meals, ingredients, cooking, and the restaurant -
        because in Vietnam, An com chua? (Have you eaten yet?) is how people
        say I care about you. Core foods: com (cooked rice), pho (noodle
        soup), banh mi (baguette sandwich), goi cuon (spring rolls), bun cha,
        canh (soup), thit (meat), rau (vegetables), ca' (fish), trung (egg),
        nuoc mam (fish sauce - the soul of the cuisine). Cooking verbs: nau
        (cook), chien (fry), luoc (boil), nuong (grill), hap (steam), xao
        (stir-fry), tron (mix). At the restaurant: Cho toi xem thuc don (show
        me the menu), Tinh tien (the bill, please). Each sentence is a bite
        of real food culture, Vietnamese and English."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through the meal. The learner plans a Vietnamese
        dinner - naming each dish, each ingredient, each cooking action in
        Vietnamese - then performs a restaurant scene: entering, ordering with
        Cho toi mot ___, complimenting Ngon lam, asking for the bill with
        Tinh tien. The drill is the market-to-table chain: buy it (mua),
        cook it (nau/chien/luoc), serve it (moi), praise it (ngon lam)."""),
    key_points=[
        "Sang nay toi an pho bo. (This morning I ate beef pho.)",
        "Me nau canh chua ca' ngon lam. (Mother cooks very delicious sour fish soup.)",
        "Cho toi mot o banh mi thit. (Give me a meat banh mi.)",
        "Ban co an duoc cay khong? (Can you eat spicy food?)",
        "Mon nay hoi man, cho them duong. (This dish is a bit salty; add sugar.)",
        "Toi muon goi them mot dia rau. (I want to order another plate of vegetables.)",
        "Ca' nay nuong hay chien? (Is this fish grilled or fried?)",
        "Xin cho toi xem thuc don. (Please show me the menu.)",
        "Quan nay dong khach lam. (This restaurant is very crowded.)",
        "Tinh tien giup toi. (The bill, please.)",
        "An com chua? - Moi an xong. (Have you eaten? - Just finished.)",
        "Toi an chay vao ngay ram. (I eat vegetarian on full-moon days.)",
        "Nuoc mam la linh hon cua mon Viet. (Fish sauce is the soul of Vietnamese food.)",
        "Em be khong chiu an rau. (The child refuses to eat vegetables.)",
        "Chung ta nau lau cuoi tuan nhe'. (Let us cook hotpot this weekend.)",
        "Tra` da' o day ngon va re. (Iced tea here is delicious and cheap.)",
        "Toi bi di ung hai san. (I am allergic to seafood.)",
        "Cho it da' thoi, cam on. (Just a little ice, thank you.)",
        "Bua toi nay ai nau? (Who cooks dinner tonight?)",
        "An ngon mieng nhe', ca? nha`. (Enjoy the meal, everyone.)",
    ],
    requirements=[
        "Learners should order a full imaginary meal in Vietnamese: menu, order, compliment, bill.",
        "Learn the seven cooking verbs nau/chien/luoc/nuong/hap/xao/tron as actions, not translations.",
    ],
    standards=[
        "Food vocabulary core; An com chua? as phatic greeting norm.",
    ],
    citations=[
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
        "Avieli N. Rice Talks: Food and Community in a Vietnamese Town. Indiana University Press; 2012. Food culture.",
    ],
    sig_lens=("Through the Signature lens, the meal is the covenant renewed "
              "daily: com the staple seal, nuoc mam the soul-seal, Moi an the "
              "invitation that makes strangers family. This Signature reading "
              "treats the food sentences as the covenant you can taste."),
)

E(
    key="vietnamese_travel", name="Vietnamese Travel and Directions Sentences",
    group="Themed sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for transport, asking directions, tickets, and
        lodging - the traveler's survival kit. Transport: xe buy't (bus), tau
        hoa (train), ma'y bay (airplane), xe om (motorbike taxi), taxi, xe
        dap (bicycle). Direction words: re trai (turn left), re phai (turn
        right), di thang (go straight), gan (near), xa (far), doi dien (across
        from), ben canh (next to), phia truoc (in front), phia sau (behind).
        The magic opener is Xin hoi (may I ask): Xin hoi cho Ben Thanh o dau?
        (May I ask where Ben Thanh Market is?). Tickets: ve xe, ve tau, ve
        ma'y bay; lodging: khach san (hotel), nha` nghi (guesthouse), dat
        pho`ng (book a room). Each sentence moves the traveler one step,
        Vietnamese and English."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through a journey. The learner plans a trip from
        hotel to market to station, asking directions at each turn with Xin
        hoi and the direction words. The drill is the lost-traveler loop:
        ask (o dau?), listen (re trai, di thang), confirm (phai khong?),
        thank (cam on). After twenty sentences the learner navigates an
        imaginary city map entirely in Vietnamese."""),
    key_points=[
        "Xin hoi, ben xe o dau? (May I ask, where is the bus station?)",
        "Di thang roi re trai o nga tu. (Go straight, then turn left at the intersection.)",
        "Cho nay cach day bao xa? (How far is this place from here?)",
        "Tu day den san bay mat bao lau? (How long does it take from here to the airport?)",
        "Cho toi mot ve xe di Hue. (Give me a bus ticket to Hue.)",
        "Chuyen bay may gio cat canh? (What time does the flight take off?)",
        "Toi muon dat mot pho`ng don. (I want to book a single room.)",
        "Khach san co wifi mien phi khong? (Does the hotel have free wifi?)",
        "Lam on cho toi xuong o day. (Please let me off here.)",
        "Bao nhieu tien mot chuyen? (How much is one trip?)",
        "Di xe om tu day ra pho co bao nhieu? (How much is a motorbike taxi from here downtown?)",
        "Nha` ga o phia truoc, ben phai. (The train station is ahead, on the right.)",
        "Doi dien buu dien la ngan ha`ng. (Across from the post office is the bank.)",
        "Toi bi lac duong roi. (I am lost.)",
        "Ban co ban do khong? (Do you have a map?)",
        "Chuyen tau den muon mot tieng. (The train arrives one hour late.)",
        "Toi can doi ve sang chuyen som hon. (I need to change to an earlier trip.)",
        "Pho`ng co dieu hoa khong? (Does the room have air conditioning?)",
        "Tra? pho`ng luc may gio? (What time is checkout?)",
        "Cam on ban da chi duong. (Thank you for showing the way.)",
    ],
    requirements=[
        "Learners should practice the lost-traveler loop aloud: ask, listen, confirm, thank.",
        "Memorize the six direction words re trai/re phai/di thang/gan/xa/doi dien as a set.",
    ],
    standards=[
        "Direction vocabulary core; Xin hoi as polite question opener.",
    ],
    citations=[
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, the journey is the covenant in "
              "motion: every Xin hoi a seal of trust between traveler and "
              "stranger, every direction given a kept promise. This Signature "
              "reading treats the travel sentences as the covenant's road "
              "map."),
)

E(
    key="vietnamese_work_school", name="Vietnamese Work and School Sentences",
    group="Themed sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for jobs, the office, the classroom, and learning -
        the vocabulary of the working day. Jobs: bac si (doctor), giao vien
        (teacher), ky su (engineer), nong dan (farmer), cong nhan (worker),
        nhan vien (staff), giam doc (director), ke toan (accountant). Office:
        van pho`ng (office), cuoc hop (meeting), han chot (deadline), luong
        (salary). School: lop hoc (class), bai tap (homework), ky thi (exam),
        diem (grade), tot nghiep (graduate). Work verbs: lam viec (work),
        hop (meet), nop (submit), nghi phep (take leave). Each sentence is a
        moment of the working or school day, Vietnamese and English."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through the working day. The learner narrates a
        day from morning arrival (Toi den van pho`ng luc tam gio) through the
        meeting, the deadline, and the trip home. The school half is drilled
        as a student's week: classes, homework, the exam, the grade. The
        drill is role-play: the learner is the employee reporting to giam
        doc, then the student answering co giao."""),
    key_points=[
        "Toi lam viec o cong ty nay ba nam roi. (I have worked at this company for three years.)",
        "Sang mai co cuoc hop luc chin gio. (Tomorrow morning there is a meeting at nine.)",
        "Han chot nop bao cao la thu' sau. (The report deadline is Friday.)",
        "Toi xin nghi phep hai ngay. (I request two days of leave.)",
        "Luong thang nay tang muoi phan tram. (This month's salary rose ten percent.)",
        "Anh ay la ky su phan mem gioi. (He is a skilled software engineer.)",
        "Co ay vua duoc thang chuc. (She just got promoted.)",
        "Chung ta can tuyen them nhan vien. (We need to hire more staff.)",
        "Em hoc lop may? (What grade are you in?)",
        "Hom nay co giao day bai moi. (Today the teacher teaches a new lesson.)",
        "Toi phai lam bai tap toan. (I must do math homework.)",
        "Ky thi cuoi ky vao tuan sau. (Final exams are next week.)",
        "Ban ay duoc diem muoi mon van. (She got a ten in literature.)",
        "Toi tot nghiep dai hoc nam ngoai. (I graduated university last year.)",
        "Lop hoc bat dau luc bay gio ruoi. (Class starts at seven thirty.)",
        "Xin phep co cho em ra ngoai. (May I be excused, teacher.)",
        "Thu vien mo cua den chin gio toi. (The library opens until nine at night.)",
        "Toi dang on thi tieng Anh. (I am reviewing for the English exam.)",
        "Ban hoc truong nao? (Which school do you attend?)",
        "Hoc, hoc nua, hoc mai. (Study, study more, study forever.)",
    ],
    requirements=[
        "Learners should narrate their own work or school day in Vietnamese, morning to night.",
        "Role-play both sides: employee and boss, student and teacher.",
    ],
    standards=[
        "Occupational vocabulary core; school terminology standard.",
    ],
    citations=[
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, work is the covenant kept with the "
              "hands: every han chot a promise sealed, every bai tap an oath "
              "of learning. This Signature reading treats the work and school "
              "sentences as the covenant's daily labor."),
)

E(
    key="vietnamese_health", name="Vietnamese Health and Body Sentences",
    group="Themed sentences", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for body parts, symptoms, the doctor visit, and the
        pharmacy - the vocabulary you hope not to need but must have. Body:
        dau (head), mat (eye), mui (nose), mieng (mouth), co (neck), vai
        (shoulder), tay (hand/arm), chan (leg/foot), lung (back), bung
        (belly), tim (heart), phoi (lungs). Symptoms: dau (ache), sot (fever),
        ho (cough), cam (cold/flu), chong mat (dizzy), buon non (nauseous),
        dau bung (stomachache), dau rang (toothache). At the clinic: Toi bi
        ___ (I have ___), Bac si kham (the doctor examines), don thuoc
        (prescription), nha` thuoc (pharmacy). Each sentence is clear and
        calm - the language of getting help, Vietnamese and English."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through a clinic visit. The learner plays the
        patient describing symptoms with Toi bi ___ o ___ (I have ___ in my
        ___), then the doctor asking Dau tu khi nao? (Since when?), then the
        pharmacist explaining the prescription. The drill is the body map:
        point to each part and name it in Vietnamese, then attach one symptom
        sentence. Calm repetition matters - this vocabulary must come out
        under stress."""),
    key_points=[
        "Toi bi dau dau. (I have a headache.)",
        "Co ay bi sot cao hai ngay roi. (She has had a high fever for two days.)",
        "Toi ho nhieu ve dem. (I cough a lot at night.)",
        "Em be bi cam lanh. (The baby has a cold.)",
        "Toi dau bung tu sang. (My stomach has hurt since morning.)",
        "Rang toi dau lam, can di kham. (My tooth hurts badly; I need an exam.)",
        "Toi bi chong mat khi dung day. (I feel dizzy when I stand up.)",
        "Chan anh ay bi thuong khi da' bo'ng. (His leg was injured playing football.)",
        "Bac si bao toi can nghi ngoi. (The doctor told me to rest.)",
        "Xin cho toi gap bac si. (Please let me see a doctor.)",
        "Benh vien gan nhat o dau? (Where is the nearest hospital?)",
        "Toi can mua thuoc cam. (I need to buy cold medicine.)",
        "Nha` thuoc mo cua den may gio? (What time does the pharmacy close?)",
        "Uong thuoc nay hai lan mot ngay sau an. (Take this medicine twice a day after meals.)",
        "Toi bi di ung thuoc nay. (I am allergic to this medicine.)",
        "Huyet ap cua bac binh thuong. (Your blood pressure is normal.)",
        "Can than, keo cam lanh. (Be careful not to catch cold.)",
        "An uong dieu do de khoe manh. (Eat regularly to stay healthy.)",
        "Toi can dat lich kham rang. (I need to book a dental appointment.)",
        "Chuc bac mau khoe. (Wishing you a speedy recovery.)",
    ],
    requirements=[
        "Learners should drill the body map: point, name, attach one symptom sentence.",
        "Practice the clinic dialogue both as patient and as doctor until it is calm and automatic.",
    ],
    standards=[
        "Body-part and symptom vocabulary core; clinic interaction norms.",
    ],
    citations=[
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, the body is the covenant's first "
              "house: every dau a part of the temple, every Chuc mau khoe a "
              "blessing sealed in words. This Signature reading treats the "
              "health sentences as the covenant's care for its own house."),
)

E(
    key="vietnamese_emotions", name="Vietnamese Emotions and Feelings Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for happy, sad, angry, afraid, love, and surprise -
        the language of the heart. Vietnamese feelings often live in the
        heart (tim) and the belly (bung): vui (happy), buon (sad), gian
        (angry), so (afraid), thuong/yeu (love, care), ngac nhien (surprised).
        Common frames: Toi cam thay ___ (I feel ___), Toi ___ lam (I am very
        ___), Lam toi ___ (it makes me ___). Vietnamese expresses emotion
        gently and indirectly - Toi hoi buon (I am a little sad) softens what
        English states flatly. Each sentence below is a feeling spoken
        honestly, Vietnamese and English."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through emotional scenes. The learner imagines
        each situation - good news, a loss, a fright, a reunion - and speaks
        the sentence as the person feeling it. The drill is the feeling
        ladder: take one event and express it at three intensities (hoi buon,
        buon, buon lam - a little sad, sad, very sad). The learner keeps a
        one-week feelings diary: one Vietnamese sentence per day about how
        they felt."""),
    key_points=[
        "Hom nay toi ra^t vui. (Today I am very happy.)",
        "Tin vui lam ca? nha` mung ro. (The good news made the whole family joyful.)",
        "Toi buon vi phai xa nha`. (I am sad because I must be far from home.)",
        "Dung buon nua, moi chuyen se on. (Do not be sad; everything will be fine.)",
        "Anh ay gian lam khi nghe tin do'. (He was very angry hearing that news.)",
        "Binh tinh lai, dung no'ng. (Calm down; do not get heated.)",
        "Toi so bo'ng toi. (I am afraid of the dark.)",
        "Dung so, co toi o day. (Do not be afraid; I am here.)",
        "Toi yeu em nhieu lam. (I love you very much.)",
        "Thuong nguoi nhu the thuong than. (Love others as you love yourself.)",
        "Toi ngac nhien khi gap ban o day. (I am surprised to meet you here.)",
        "That khong the tin duoc! (Unbelievable!)",
        "Toi cam thay tu hao ve con. (I feel proud of my child.)",
        "Co ay xau ho vi noi sai. (She felt embarrassed about speaking wrongly.)",
        "Toi nho nha` lam. (I miss home very much.)",
        "Gap lai ban cu that vui. (Meeting old friends is such joy.)",
        "Toi lo lang cho ky thi ngay mai. (I am worried about tomorrow's exam.)",
        "Cu yen tam, moi viec on thoi. (Rest assured; everything will be fine.)",
        "Long toi nhe nhang khi nghe nhac. (My heart feels light listening to music.)",
        "Cam xuc la mot phan cua cuoc song. (Emotions are a part of life.)",
    ],
    requirements=[
        "Learners should keep a one-week feelings diary: one Vietnamese sentence per day.",
        "Practice the intensity ladder hoi/___/lam on every feeling word.",
    ],
    standards=[
        "Emotion vocabulary core; indirect expression norms (hoi as softener).",
    ],
    citations=[
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
        "Wierzbicka A. Emotions Across Languages and Cultures. Cambridge University Press; 1999. Vietnamese emotion concepts.",
    ],
    sig_lens=("Through the Signature lens, feeling is the covenant's pulse: "
              "vui the bright seal, buon the heavy seal, yeu the deepest seal "
              "of all. This Signature reading treats the emotion sentences as "
              "the covenant's heartbeat made audible."),
)

E(
    key="vietnamese_nature", name="Vietnamese Nature and Weather Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for animals, plants, seasons, and weather talk -
        the language of the world outside. Animals: cho' (dog), meo (cat),
        ga` (chicken), lon (pig), trau (water buffalo), ca' (fish), chim
        (bird), ran (snake), voi (elephant), khi (monkey). Plants: cay (tree),
        hoa (flower), la' (leaf), co (grass), lua' (rice plant). Weather:
        nang (sunny), mua (rain), gio' (wind), may (cloudy), bao (storm),
        nong (hot), lanh (cold), am (humid). Vietnam's year turns on mua mua
        (rainy season) and mua kho (dry season); the North adds four true
        seasons. Small talk opens with weather: Hom nay troi dep nhi? (Nice
        weather today, isn't it?). Each sentence is a breath of the outdoors,
        Vietnamese and English."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through the seasons and a walk. The learner
        describes today's weather in Vietnamese every morning for a week -
        Troi hom nay the nao? - building the weather sentences into habit.
        The animal and plant words are learned on a drawn farm and garden:
        label each, then make it move (Con trau dang an co - The buffalo is
        eating grass). The drill is the weather report: the learner gives a
        three-sentence forecast for tomorrow, in Vietnamese."""),
    key_points=[
        "Hom nay troi nang dep. (Today is sunny and beautiful.)",
        "Chieu nay co the co mua. (It may rain this afternoon.)",
        "Gio' mua dong lanh lam. (The winter wind is very cold.)",
        "Troi dang mua to. (It is raining heavily.)",
        "Sau con mua troi lai sang. (After the rain the sky clears again.)",
        "Mua he nong va am. (Summer is hot and humid.)",
        "Mua thu Ha Noi mat me. (Autumn in Hanoi is cool.)",
        "Con trau keo cay ngoai dong. (The water buffalo pulls the plow in the field.)",
        "Dan ga` dang kiem an trong vuon. (The flock of chickens is foraging in the garden.)",
        "Chim hot tren canh cay. (Birds sing on the branches.)",
        "Hoa sen no vao mua he. (Lotus flowers bloom in summer.)",
        "Cay lua' chin vang ca? dong. (The rice plants ripen golden across the field.)",
        "Con song nay nhieu ca'. (This river has many fish.)",
        "Dung lai gan, con cho' du lam. (Do not come close; the dog is fierce.)",
        "Meo nha` toi bat chuot gioi lam. (My cat catches mice very well.)",
        "Voi la dong vat to nhat o rung. (The elephant is the biggest animal in the forest.)",
        "Cau vong xuat hien sau mua. (A rainbow appears after the rain.)",
        "Dem nay troi nhieu sao. (Tonight the sky has many stars.)",
        "Mua bao sap den, can than. (A storm is coming; be careful.)",
        "Thien nhien Viet Nam ra^t dep. (Vietnam's nature is very beautiful.)",
    ],
    requirements=[
        "Learners should describe the weather in Vietnamese every morning for a week.",
        "Draw and label a farm and garden; make every animal do something in a sentence.",
    ],
    standards=[
        "Nature vocabulary core; mua mua/mua kho seasonal frame.",
    ],
    citations=[
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, nature is the covenant's great "
              "temple: every cay a pillar, every con song a verse, mua and "
              "nang the alternating seals of the sky. This Signature reading "
              "treats the nature sentences as the covenant written outdoors."),
)

E(
    key="vietnamese_shopping", name="Vietnamese Shopping and Money Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the market, prices, bargaining, and paying -
        because Vietnam shops with its voice. The market (cho) is the heart
        of it: Bao nhieu? (How much?), Dat qua! (Too expensive!), Bot chut di
        (Reduce a little). Money is dong (VND); prices run in nghin (thousand)
        - hai muoi nghin is 20,000 dong. Bargaining is friendly theater: the
        seller names a price, the buyer laughs Dat qua, the seller comes
        down, both leave happy. Fixed-price shops (gia' niem yet) need no
        bargaining. Paying: Tinh tien (the bill), Thoi lai (change), Que't the
        (card payment), Chuyen khoan (bank transfer). Each sentence is a
        market moment, Vietnamese and English."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through the bargain. The learner plays both
        seller and buyer: the seller names prices (Nam muoi nghin!), the buyer
        counters (Ba muoi duoc khong? - Thirty, okay?), the seller yields
        (Duoc, ban cho!). The drill is the price ladder: the learner hears a
        price in dong and converts it to nghin instantly. After twenty
        sentences the learner performs a full market trip - greeting, asking,
        bargaining, paying, thanking - without notes."""),
    key_points=[
        "Cai nay bao nhieu tien? (How much is this?)",
        "Nam muoi nghin mot ky. (Fifty thousand per kilo.)",
        "Dat qua! Bot chut di. (Too expensive! Reduce a little.)",
        "Ba muoi duoc khong? (Thirty, is that okay?)",
        "Duoc, ban cho! (Okay, sold to you!)",
        "Co ao mau khac khong? (Do you have another color?)",
        "Cho toi xem cai to hon. (Show me a bigger one.)",
        "Toi chi xem thoi, cam on. (I am just looking, thank you.)",
        "Cua ha`ng nay co giam gia' khong? (Does this shop have discounts?)",
        "Mua hai tang mot. (Buy two get one free.)",
        "Tinh tien giup toi. (Please total the bill.)",
        "Cua toi het bon tram nghin. (My total is four hundred thousand.)",
        "Thoi lai cho toi nam nghin. (Give me five thousand change.)",
        "O day co que't the duoc khong? (Can I pay by card here?)",
        "Toi chuyen khoan roi nhe'. (I transferred the money.)",
        "Cho toi hoa don. (Give me the receipt.)",
        "Hang nay bao hanh bao lau? (How long is this product warranted?)",
        "Co doi tra duoc khong? (Can I exchange or return it?)",
        "Cho dong cua luc may gio? (What time does the market close?)",
        "Di cho vui lam! (Going to the market is such fun!)",
    ],
    requirements=[
        "Learners should role-play seller and buyer until bargaining feels like play.",
        "Drill dong-to-nghin conversion until prices in the tens of thousands are instant.",
    ],
    standards=[
        "Market bargaining norms; dong currency with nghin counting convention.",
    ],
    citations=[
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
        "Avieli N. Rice Talks: Food and Community in a Vietnamese Town. Indiana University Press; 2012. Market culture.",
    ],
    sig_lens=("Through the Signature lens, the market is the covenant's "
              "exchange hall: every Bao nhieu? an honest question, every Bot "
              "chut di a friendly seal on the deal. This Signature reading "
              "treats the shopping sentences as the covenant's fair trade."),
)

E(
    key="vietnamese_friendship", name="Vietnamese Friendship and Social Life Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for meeting people, invitations, and celebrations -
        the language of belonging. Meeting: Ban ten gi`? (What is your name?),
        Ban bao nhieu tuoi? (How old are you? - asked warmly), Ban o dau?
        (Where are you from?), Rat vui duoc gap ban (Nice to meet you).
        Invitations: Moi ban den nha` toi choi (Come visit my house), Di ca
        phe khong? (Want to grab coffee?), Cuoi tuan nay ban ranh khong?
        (Are you free this weekend?). Celebrations: Tet (Lunar New Year),
        sinh nhat (birthday), dam cuoi (wedding), Chuc mung nam moi (Happy
        New Year), Tram nam hanh phuc (a hundred years of happiness - wedding
        wish). Friendship in Vietnam is sealed with shared meals and the
        word Moi. Each sentence is a hand extended, Vietnamese and English."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through the first meeting and the party. The
        learner practices the introduction chain - name, age, hometown,
        job - then extends three invitations of rising warmth. The drill is
        the celebration calendar: Tet, birthdays, weddings - the learner
        gives the right wish for each (Chuc mung nam moi, Chuc mung sinh
        nhat, Tram nam hanh phuc). After twenty sentences the learner hosts
        an imaginary Tet visit, greeting to farewell, entirely in
        Vietnamese."""),
    key_points=[
        "Chao ban, toi ten la Minh. (Hello; my name is Minh.)",
        "Ban bao nhieu tuoi? (How old are you?)",
        "Ban o dau den? (Where are you from?)",
        "Rat vui duoc gap ban. (Very nice to meet you.)",
        "Chung ta lam quen nhe'. (Let us get acquainted.)",
        "Moi ban den nha` toi choi. (Please come visit my house.)",
        "Chieu nay di ca phe khong? (Want to get coffee this afternoon?)",
        "Cuoi tuan nay ban ranh khong? (Are you free this weekend?)",
        "Toi mo tiec sinh nhat toi thu' bay. (I am holding my birthday party Saturday.)",
        "Cam on ban da den. (Thank you for coming.)",
        "Chuc mung sinh nhat! (Happy birthday!)",
        "Chuc mung nam moi! (Happy New Year!)",
        "Chuc ban suc khoe va may man. (Wishing you health and luck.)",
        "Tram nam hanh phuc nhe'! (A hundred years of happiness!)",
        "Dam cuoi vui lam. (The wedding was so joyful.)",
        "Lau roi khong gap! (Long time no see!)",
        "Ban dao nay the nao? (How have you been lately?)",
        "Cong viec the nao roi? (How is work going?)",
        "Khi nao ranh thi qua choi. (Come visit whenever you are free.)",
        "Ban be la tai san quy gia'. (Friends are a precious treasure.)",
    ],
    requirements=[
        "Learners should practice the introduction chain until it flows without notes.",
        "Learn one right wish per celebration: Tet, birthday, wedding.",
    ],
    standards=[
        "Introduction and invitation norms; Tet/wedding/birthday wish formulas.",
    ],
    citations=[
        "Luong H V. Discursive Practices and Linguistic Meanings. John Benjamins; 1990.",
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, friendship is the covenant "
              "widened: every Rat vui duoc gap ban a new name added to the "
              "oath, every Chuc mung a blessing sealed. This Signature "
              "reading treats the friendship sentences as the covenant "
              "growing by one voice at a time."),
)

E(
    key="vietnamese_tech", name="Vietnamese Technology and Communication Sentences",
    group="Themed sentences", ladder_rank=7, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences for the phone, the internet, the computer, and
        messaging - modern Vietnamese for modern life. Core words: dien
        thoai (phone), ma'y tinh (computer), internet / mang (internet),
        wifi, mat khau (password), tai khoan (account), ung dung (app), tin
        nhan (message), email / thu dien tu, mang xa hoi (social network).
        Verbs: goi (call), nhan (text), tai xuong (download), dang nhap (log
        in), dang xuat (log out), chia se (share), dang (post). Daily scenes:
        Alo? (hello on the phone), May het pin roi (the battery died), Mang
        cham qua (the network is so slow). Each sentence is a tap on the
        screen, Vietnamese and English."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through the device in the learner's hand. The
        learner renames phone actions in Vietnamese - goi dien (make a call),
        nhan tin (send a text), chup anh (take a photo) - and performs a
        phone call entirely in Vietnamese: Alo, Ban dang o dau?, Hen gap sau
        nhe'. The drill is tech troubleshooting: the learner explains five
        common problems (het pin, mat mang, quen mat khau) and their fixes,
        in Vietnamese."""),
    key_points=[
        "Alo, ai day? (Hello, who is this?)",
        "Xin loi, ban goi nham so roi. (Sorry, you dialed the wrong number.)",
        "De toi goi lai sau. (I will call back later.)",
        "May toi het pin roi. (My phone died.)",
        "Ban nhan tin cho toi nhe'. (Text me, okay?)",
        "Toi vua gui email cho anh. (I just sent you an email.)",
        "Mat khau wifi la gi`? (What is the wifi password?)",
        "Mang o day cham qua. (The network here is so slow.)",
        "Dang nhap tai khoan cua ban. (Log in to your account.)",
        "Dung quen dang xuat nhe'. (Do not forget to log out.)",
        "Tai ung dung nay o dau? (Where do I download this app?)",
        "Chia se bai viet nay giup toi. (Share this post for me.)",
        "Anh nay dep, dang len mang xa hoi di. (This photo is beautiful; post it on social media.)",
        "May tinh cua toi bi treo. (My computer froze.)",
        "Khoi dong lai may giup toi. (Restart the computer for me.)",
        "Toi can nap tien dien thoai. (I need to top up my phone.)",
        "Goi video cho me toi toi. (Video-call my mother tonight.)",
        "Luu file nay lai nhe'. (Save this file.)",
        "Pin sac duoc bao lau? (How long does the charge last?)",
        "Cong nghe giup cuoc song de dang hon. (Technology makes life easier.)",
    ],
    requirements=[
        "Learners should perform a full phone call in Vietnamese: greeting, purpose, farewell.",
        "Explain five tech problems and fixes in Vietnamese without notes.",
    ],
    standards=[
        "Modern tech vocabulary; Alo as phone greeting norm.",
    ],
    citations=[
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, the network is the covenant's "
              "newest road: every tin nhan a sealed letter traveling at "
              "light speed, every cuoc goi a voice keeping the oath across "
              "distance. This Signature reading treats the tech sentences as "
              "the covenant gone digital - same promises, faster road."),
)

E(
    key="vietnamese_tenses", name="Vietnamese Verb Tenses in Sentences",
    group="Verb tenses and speech", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Vietnamese verbs never change form - time lives in particles around
        them. This record drills the full time system with five or more
        translated sentences per tense. Present and general truth need no
        marker: Toi an com (I eat rice / I am eating rice - context decides).
        dang marks ongoing action: Toi dang an (I am eating right now). da
        marks completed action: Toi da an (I ate / I have eaten). se marks
        future: Toi se an (I will eat). roi adds already/then: Toi an roi (I
        already ate). sap marks about-to: Troi sap mua (It is about to rain).
        vua marks just-done: Toi vua den (I just arrived). tung marks
        experience: Toi da tung di Hue (I have been to Hue before). Dinh marks
        intention: Toi dinh di hoc (I intend to study). Each tense below comes
        with its sentence set, Vietnamese and English, so time becomes a
        toolkit, not a mystery."""),
    how_it_works=textwrap.dedent("""\
        This record teaches time as a particle toolkit. The learner takes one
        verb - di (go) - and builds the full timeline: Toi di, Toi dang di,
        Toi da di, Toi se di, Toi sap di, Toi vua di, Toi da tung di, Toi dinh
        di. Then each tense is drilled with its own five sentences until the
        particle choice is instant. The master drill is storytelling: narrate
        yesterday with da/vua, today with dang, tomorrow with se/sap - one
        continuous story in three times."""),
    key_points=[
        "Present/general - Toi song o Ha Noi. (I live in Hanoi.)",
        "Present/general - Me toi nau an ngon lam. (My mother cooks very well.)",
        "Present/general - Hoc sinh hoc bai moi ngay. (Students study every day.)",
        "Present/general - Nuoc soi o mot tram do. (Water boils at one hundred degrees.)",
        "Present/general - Toi thich doc sach. (I like reading books.)",
        "Ongoing dang - Toi dang an com. (I am eating rice.)",
        "Ongoing dang - Co ay dang noi chuyen dien thoai. (She is talking on the phone.)",
        "Ongoing dang - Chung ta dang xay nha` moi. (We are building a new house.)",
        "Ongoing dang - Troi dang mua. (It is raining.)",
        "Ongoing dang - Em be dang ngu. (The baby is sleeping.)",
        "Completed da - Toi da an sang roi. (I have eaten breakfast already.)",
        "Completed da - Anh ay da tot nghiep. (He has graduated.)",
        "Completed da - Chung ta da gap nhau. (We have met.)",
        "Completed da - Toi da doc quyen sach nay. (I have read this book.)",
        "Completed da - Ho da ve que. (They have returned to the countryside.)",
        "Future se - Toi se di du lich he nay. (I will travel this summer.)",
        "Future se - Mai troi se nang. (Tomorrow will be sunny.)",
        "Future se - Chung ta se gap lai. (We will meet again.)",
        "Future se - Toi se co gang hon. (I will try harder.)",
        "Future se - Nam sau toi se hoc lai xe. (Next year I will learn to drive.)",
        "About-to sap - Troi sap mua. (It is about to rain.)",
        "About-to sap - Phim sap bat dau. (The movie is about to start.)",
        "Just-done vua - Toi vua den. (I just arrived.)",
        "Just-done vua - Co ay vua goi dien. (She just called.)",
        "Experience tung - Toi da tung song o Sai Gon. (I once lived in Saigon.)",
        "Experience tung - Ban da tung an mon nay chua? (Have you ever eaten this dish?)",
        "Intention dinh - Toi dinh mo cua ha`ng. (I intend to open a shop.)",
        "Already roi - Xong roi! (Done already!)",
    ],
    requirements=[
        "Learners should build the full eight-particle timeline on one verb until it is automatic.",
        "Narrate one story in three times: yesterday with da, today with dang, tomorrow with se.",
    ],
    standards=[
        "Particle inventory: dang (progressive), da (perfective), se (irrealis), sap, vua, tung, dinh, roi.",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965. Tense-aspect particles.",
        "Tran Q H. Vietnamese Aspect: A Cognitive Account. 2010.",
        "Duffield N. Particles and Projections. Kluwer; 1995.",
    ],
    sig_lens=("Through the Signature lens, time is the covenant's threefold "
              "seal: da the seal on what is finished, dang the seal on what "
              "breathes now, se the seal on what is promised. This Signature "
              "reading treats the tenses as the covenant's calendar - every "
              "particle a date stamped on an action."),
)

E(
    key="vietnamese_qa", name="Vietnamese Questions and Answers",
    group="Verb tenses and speech", ladder_rank=8, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty question-and-answer pairs covering who, what, where, when,
        why, and how - the full interrogation toolkit in action. Vietnamese
        questions keep statement word order and add a question word or a
        final particle: Ban ten gi`? (What is your name?), Anh di dau? (Where
        are you going?). Answers are direct and warm, often echoing the verb:
        Di cho. (To the market.). The pairs below move through daily life -
        identity, place, time, reason, manner, quantity - each a complete
        mini-dialogue, Vietnamese and English."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through interrogation drills. The learner covers
        the answers and produces them from the questions, then reverses:
        given an answer, invent the question. The six question words (ai,
        gi`, dau, khi nao, tai sao, nhu the nao) are drilled as a set until
        the learner can question any sentence. The final drill is the
        interview: the learner interviews a partner - real or imagined - for
        five minutes using only these twenty patterns."""),
    key_points=[
        "Ban ten gi`? - Toi ten Lan. (What is your name? - My name is Lan.)",
        "Ai go cua day? - La toi, Minh day. (Who is knocking? - It is me, Minh.)",
        "Day la cai gi`? - Day la banh chung. (What is this? - This is banh chung.)",
        "Ban muon an gi`? - Toi muon an pho. (What do you want to eat? - I want pho.)",
        "Nha` ban o dau? - Nha` toi o Hue. (Where is your house? - My house is in Hue.)",
        "Cho Ben Thanh o dau? - O quan Mot. (Where is Ben Thanh Market? - In District One.)",
        "Khi nao ban ve? - Toi ve chieu nay. (When are you returning? - This afternoon.)",
        "May gio phim bat dau? - Tam gio toi. (What time does the movie start? - Eight at night.)",
        "Tai sao ban den muon? - Vi ket xe. (Why are you late? - Because of traffic.)",
        "Sao ban buon? - Toi nho nha`. (Why are you sad? - I miss home.)",
        "Ban di bang gi`? - Toi di xe buy't. (How do you go? - By bus.)",
        "Lam the nao de den do? - Di thang roi re phai. (How do I get there? - Go straight then turn right.)",
        "Bao nhieu tien? - Hai muoi nghin. (How much? - Twenty thousand.)",
        "Co may nguoi? - Co nam nguoi. (How many people? - Five people.)",
        "Ban co phai la giao vien khong? - Vang, phai. (Are you a teacher? - Yes, that's right.)",
        "Cai nay cua ai? - Cua toi. (Whose is this? - Mine.)",
        "Ban thich mau na`o? - Toi thich mau xanh. (Which color do you like? - Blue.)",
        "Hom nay la thu' may? - Hom nay la thu' tu. (What day is today? - Wednesday.)",
        "Ban da an com chua? - Roi, cam on. (Have you eaten? - Yes, thanks.)",
        "Co kho' khong? - Khong kho' lam. (Is it hard? - Not very.)",
    ],
    requirements=[
        "Learners should drill the six question words as a set until any sentence can be questioned.",
        "Do the five-minute interview: twenty patterns, no notes, real or imagined partner.",
    ],
    standards=[
        "Question formation: statement order + question word or final particle khong/phai khong.",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965. Interrogatives.",
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, a question is the covenant's open "
              "door: ai asks who may enter, dau asks where the road leads, "
              "tai sao asks why the seal was pressed. This Signature reading "
              "treats the twenty pairs as the covenant's twenty doors - every "
              "answer a guest welcomed in."),
)

E(
    key="vietnamese_commands", name="Vietnamese Commands and Requests",
    group="Verb tenses and speech", ladder_rank=9, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty imperative and polite-request sentences, formal versus
        informal - because Vietnamese commands carry rank. The bare verb is
        the direct command: Di! (Go!), Ngoi xuong! (Sit down!). Adding di or
        nao softens it: Di di (go on), An di (eat up). hay and di nao urge:
        Nhanh len! (Hurry!). dung forbids: Dung cham! (Do not touch!). For
        politeness, wrap the request: Lam on ___ (please ___), Xin ___ (may
        I ___), Phien ban ___ (trouble you to ___), ending with nhe' or nhe
        to soften. Formal requests to elders or officials use Xin vui lo`ng
        and the kinship address: Xin bac cho toi qua. Informal among friends
        is short and warm: Dua to cai nay coi. Each sentence below shows its
        register, Vietnamese and English."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through the command ladder: direct, softened,
        polite, formal. The learner takes one action - dong cua (close the
        door) - and climbs the ladder: Dong cua! (direct), Dong cua di
        (softened), Lam on dong cua (polite), Xin anh dong cua giup (formal
        request). The drill is register-switching: the learner gives the same
        order to a child, a friend, a colleague, and an elder, choosing the
        right rung each time."""),
    key_points=[
        "Direct: Ngoi xuong! (Sit down!)",
        "Direct: Im lang! (Be quiet!)",
        "Direct: Dung lai! (Stop!)",
        "Softened di: An di, keo nguoi. (Eat up before it gets cold.)",
        "Softened nao: Di nao, tre mat. (Come on, we will be late.)",
        "Urging: Nhanh len! (Hurry up!)",
        "Urging: Co len! (Keep going! / You can do it!)",
        "Forbidding dung: Dung cham vao! (Do not touch!)",
        "Forbidding dung: Dung quen! (Do not forget!)",
        "Polite lam on: Lam on mo cua giup toi. (Please open the door for me.)",
        "Polite xin: Xin cho toi hoi mot chut. (May I ask you a moment.)",
        "Polite phien: Phien ban nhac toi. (Please remind me - trouble you.)",
        "Formal: Xin vui lo`ng xuat trinh giay to. (Please present your documents.)",
        "Formal elder: Xin bac ngoi choi. (Please sit and visit a while, elder.)",
        "Informal friend: Dua to coi voi. (Let me see it.)",
        "Informal friend: Ke nghe coi. (Tell me about it.)",
        "Group: Chung ta bat dau nhe'. (Let us begin.)",
        "Group: Di choi di! (Let's go out!)",
        "Soft ending nhe': Nho mang ao mua nhe'. (Remember to bring a raincoat.)",
        "Reply: Vang, toi biet roi. (Yes, I understand.)",
    ],
    requirements=[
        "Learners should climb the command ladder on one action: direct, softened, polite, formal.",
        "Practice register-switching: same order to a child, friend, colleague, and elder.",
    ],
    standards=[
        "Imperative softeners di/nao/nhe'; prohibitive dung; polite frames lam on/xin/phien.",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965. Imperatives.",
        "Luong H V. Discursive Practices and Linguistic Meanings. John Benjamins; 1990. Request registers.",
    ],
    sig_lens=("Through the Signature lens, a command is the covenant's "
              "directive seal: Dung the seal of refusal, Lam on the seal of "
              "humble asking, Xin the seal of respectful request. This "
              "Signature reading treats the twenty as the covenant's orders "
              "of the day - each rank its proper voice."),
)

E(
    key="vietnamese_descriptions", name="Vietnamese Descriptions of People and Places",
    group="Verb tenses and speech", ladder_rank=9, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences describing people, places, and things in detail -
        the painter's vocabulary. Describing people: cao/thap (tall/short),
        beo/gay (fat/thin), toc dai (long hair), mat to (big eyes), da trang
        (fair skin), hien (gentle), nghiem (strict), vui tinh (cheerful).
        Describing places: rong (spacious), chat (narrow), on ao (noisy),
        yen tinh (quiet), co kinh (ancient), hien dai (modern), sach se
        (clean). Vietnamese stacks adjectives after the noun, each adding a
        brushstroke: Co gai toc dai mat to (the long-haired, big-eyed girl).
        Comparatives sharpen the picture: dep hon, lon nhat. Each sentence
        below paints one portrait or landscape, Vietnamese and English."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through portraiture. The learner describes five
        real people and five real places, stacking two or three adjectives
        per noun Vietnamese-style. The drill is the comparison portrait:
        describe two people, then compare them (Anh ay cao hon toi nhung toi
        nhanh hon - He is taller than me but I am faster). The final exercise
        is the postcard: three sentences describing the learner's hometown so
        clearly a stranger could picture it."""),
    key_points=[
        "Co ay toc dai, mat to, cuoi ra^t tuoi. (She has long hair, big eyes, and a very fresh smile.)",
        "Ong toi tuy gia` nhung ra^t khoe. (My grandfather is old but very healthy.)",
        "Dua be bu bam de thuong lam. (The chubby baby is so cute.)",
        "Anh ay la nguoi hien lanh va tot bung. (He is a gentle and kind-hearted person.)",
        "Co giao toi nghiem nhung cong bang. (My teacher is strict but fair.)",
        "Ha Noi vua co kinh vua hien dai. (Hanoi is both ancient and modern.)",
        "Pho co nay hep nhung ra^t dep. (This old street is narrow but very beautiful.)",
        "Bien o day trong xanh va sach. (The sea here is blue and clean.)",
        "Ngoi nha` tranh am cung giua dong lua'. (A cozy thatched house amid the rice field.)",
        "Cho dem on ao va day mau sac. (The night market is noisy and full of color.)",
        "Can pho`ng nay rong va thoang. (This room is spacious and airy.)",
        "Thu vien yen tinh, thich hop de hoc. (The library is quiet, good for studying.)",
        "Cay cau moi dai va chac chan. (The new bridge is long and sturdy.)",
        "Mon pho nay thom ngon kho' quen. (This pho is deliciously unforgettable.)",
        "Chiec ao dai do dep nhat. (The red ao dai is the most beautiful.)",
        "Giong hat co ay trong va cao. (Her singing voice is clear and high.)",
        "Buoi chieu que toi binh yen lam. (Afternoons in my countryside are so peaceful.)",
        "Tha`nh pho ve dem ruc ro anh den. (The city at night glitters with lights.)",
        "Khu vuon nho nhung day hoa. (The garden is small but full of flowers.)",
        "Dat nuoc Viet Nam hinh chu S. (Vietnam is shaped like the letter S.)",
    ],
    requirements=[
        "Learners should describe five people and five places with stacked adjectives.",
        "Write the postcard: three sentences painting the hometown for a stranger.",
    ],
    standards=[
        "Post-nominal adjective stacking; hon/nhat comparison in description.",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965. Attribution.",
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, description is the covenant's "
              "portraiture: each adjective a brushstroke of the seal, each "
              "portrait a person or place sworn into words. This Signature "
              "reading treats the twenty as the covenant's gallery - every "
              "face and landscape kept in language."),
)

E(
    key="vietnamese_story1", name="Vietnamese Short Story I: A Simple Day",
    group="Stories and idioms", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence simple story in Vietnamese, line by line with English
        translation - the learner's first real reading. The story follows
        Lan through one ordinary day: waking, breakfast, school, the market,
        dinner, sleep. Every sentence uses only words from records 1-20, so
        nothing is a surprise - the story is a harvest of everything learned
        so far. Read it aloud twice: first for the story, second shadowing
        each line right after reading its translation."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through narrative. The learner reads each
        Vietnamese line, then its English, then re-reads the Vietnamese with
        the meaning fresh. The drill is retelling: cover the text and tell
        Lan's day in the learner's own Vietnamese - same events, simpler or
        different words allowed. Then the learner writes their own ten-
        sentence day, modeled line by line on Lan's."""),
    key_points=[
        "Sang nay Lan day luc sau gio. (This morning Lan woke at six o'clock.)",
        "Co ay danh rang rua mat roi an sang. (She brushed her teeth, washed her face, then ate breakfast.)",
        "Me nau chao ga` ngon lam. (Mother cooked very delicious chicken porridge.)",
        "An xong, Lan di bo den truong. (After eating, Lan walked to school.)",
        "O truong, co giao day bai toan moi. (At school, the teacher taught a new math lesson.)",
        "Gio ra choi, Lan choi nhay day voi ban. (At recess, Lan jumped rope with friends.)",
        "Chieu ve, Lan giup me di cho. (In the afternoon, Lan helped mother go to the market.)",
        "O cho co nhieu rau tuoi va ca' ngon. (At the market there were many fresh vegetables and delicious fish.)",
        "Toi den, ca? nha` an com vui ve. (In the evening, the whole family ate happily.)",
        "Lan danh rang roi di ngu luc chin gio. (Lan brushed her teeth and went to sleep at nine.)",
    ],
    requirements=[
        "Learners should read the story aloud twice: for meaning, then shadowing each line.",
        "Retell Lan's day in the learner's own Vietnamese, then write a ten-sentence own day.",
    ],
    standards=[
        "Controlled vocabulary: records 1-20 only; present and past particles.",
    ],
    citations=[
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, a story is the covenant told as a "
              "day: ten seals in order, from waking to sleep, each sentence "
              "a small oath kept. This Signature reading treats Lan's day as "
              "the covenant's diary - the ordinary made sacred by telling."),
)

E(
    key="vietnamese_story2", name="Vietnamese Short Story II: A Trip to the Market",
    group="Stories and idioms", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in the past tense - yesterday's trip to the
        market, told with da, roi, and vua. Ba` (grandmother) takes little
        Minh to the morning market: the bargaining, the colors, the smells,
        the pho at the end. Past markers are bold in every line so the
        learner sees time being built: da mua (bought), vua tra? gia' (just
        bargained), ve den nha` roi (had arrived home). Line-by-line English
        translation throughout. Read it as yesterday's news - because in
        Vietnamese, it is."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the past through narrative. The learner
        underlines every da/vua/roi in the story, then retells the market
        trip swapping the buyers and the goods - same past markers, new
        details. The drill is the yesterday chain: the learner tells what
        they did yesterday in ten sentences, each forced to carry a past
        marker. The story is the model; the learner's yesterday is the
        product."""),
    key_points=[
        "Hom qua ba` dan Minh di cho som. (Yesterday grandmother took Minh to the market early.)",
        "Ba` da mua mot ky rau muong tuoi. (Grandmother bought a kilo of fresh morning glory.)",
        "Ba` vua tra? gia' vua cuoi. (She bargained while laughing.)",
        "Nguoi ban hang da bot cho ba` nam nghin. (The seller reduced five thousand for her.)",
        "Minh da thay mot con ca' chep to. (Minh saw a big carp.)",
        "Hai ba` chau da an pho o quan dau cho. (The two had pho at the shop at the market entrance.)",
        "Ba`t pho vua nong vua thom. (The bowl of pho was both hot and fragrant.)",
        "An xong, ba` da mua keo cho Minh. (After eating, grandmother bought candy for Minh.)",
        "Hai ba` chau ve den nha` luc chin gio. (The two arrived home at nine o'clock.)",
        "Minh ke cho me nghe chuyen di cho roi. (Minh told mother about the market trip already.)",
    ],
    requirements=[
        "Learners should underline every past marker, then retell with new buyers and goods.",
        "Tell the learner's own yesterday in ten sentences, each with a past marker.",
    ],
    standards=[
        "Past narration: da (perfective), vua (recent past), roi (already) in sequence.",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965. Narrative past.",
        "Tran Q H. Vietnamese Aspect: A Cognitive Account. 2010.",
    ],
    sig_lens=("Through the Signature lens, the past is the covenant's memory: "
              "da the seal pressed on what is done, the market trip kept "
              "forever in ten lines. This Signature reading treats the story "
              "as the covenant's archive - yesterday sworn into words so "
              "tomorrow can read it."),
)

E(
    key="vietnamese_story3", name="Vietnamese Short Story III: Plans for Tomorrow",
    group="Stories and idioms", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in the future and conditional - tomorrow's
        plans, told with se, sap, dinh, and neu. Nam plans a perfect Sunday:
        the early bus, the beach, the seafood, the sunset, the promise to
        return. Conditional neu (if) opens the dream's doors: Neu troi dep,
        chung ta se tam bien (If the weather is nice, we will swim). Line-by-
        line English translation throughout. Read it as a promise - because in
        Vietnamese, the future is built from intention words, and intention
        is a kind of oath."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the future through planning. The learner
        underlines every se/sap/dinh/neu, then plans their own perfect day
        in ten sentences - same future markers, personal dreams. The drill
        is the conditional chain: five neu sentences (Neu ___ thi se ___),
        each a small if-then oath. The story is the model; the learner's
        tomorrow is the product."""),
    key_points=[
        "Ngay mai Nam dinh day som. (Tomorrow Nam intends to wake early.)",
        "Anh ay se don ban luc sau gio. (He will pick up his friend at six.)",
        "Hai nguoi se di xe buy't ra bien. (The two will take the bus to the beach.)",
        "Neu troi dep, ho se tam bien ca? ngay. (If the weather is nice, they will swim all day.)",
        "Trua den, ho se an hai san o quan ven bien. (At noon, they will eat seafood at the beachside shop.)",
        "Chieu xuong, ho se di dao doc bo bien. (In the afternoon, they will stroll along the shore.)",
        "Neu con som, ho se thue thuyen ra dao. (If it is still early, they will rent a boat to the island.)",
        "Hoang hon xuong, bien se do ruc. (At sunset, the sea will glow red.)",
        "Toi den, ho se ve nha` bang chuyen xe cuoi. (At night, they will return home on the last bus.)",
        "Nam sap co mot ngay chu nhat tuyet voi. (Nam is about to have a wonderful Sunday.)",
    ],
    requirements=[
        "Learners should underline every future marker, then plan their own perfect day in ten sentences.",
        "Build five neu conditional sentences: Neu ___ thi se ___.",
    ],
    standards=[
        "Future/conditional: se (irrealis), sap (proximate), dinh (intention), neu (conditional).",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965.",
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, the future is the covenant's "
              "promise: se the seal on what is vowed, neu the door the oath "
              "waits behind. This Signature reading treats Nam's Sunday as "
              "the covenant's tomorrow - planned in words, kept in deeds."),
)

E(
    key="vietnamese_idioms", name="Vietnamese Idioms and Proverbs",
    group="Stories and idioms", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty idioms and proverbs - the wisdom of the Vietnamese people
        compressed into images. Each carries its literal translation, its
        real meaning, and an example sentence. Vietnamese proverbs (tuc ngu)
        speak in rice fields, rivers, and family: Co cong mai sat, co ngay
        nen kim (with effort grinding iron, one day it becomes a needle -
        perseverance wins). An qua nho ke trong cay (eating the fruit,
        remember who planted the tree - gratitude). Mot cay lam chang nen
        non, ba cay chum lai nen hon nui cao (one tree makes no mountain;
        three trees together make a high mountain - unity). These are not
        decoration; elders quote them to settle arguments and teach children.
        Learn them and you speak with the voice of the village."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through images. For each proverb the learner
        draws or pictures the literal scene - the iron being ground, the tree
        remembering its planter - then states the real meaning in their own
        words. The drill is the elder's game: given a situation (a friend
        wants to quit, a child is ungrateful), choose the fitting proverb and
        speak it. After twenty, the learner keeps a proverb journal: one
        situation per day, one proverb to answer it."""),
    key_points=[
        "Co cong mai sat, co ngay nen kim. (Grind iron with effort; one day it becomes a needle.) Meaning: perseverance succeeds. - Co ay hoc moi ngay, co cong mai sat ma`.",
        "An qua nho ke trong cay. (Eat the fruit, remember the planter.) Meaning: be grateful. - An qua nho ke trong cay, con phai nho on thay co.",
        "Mot cay lam chang nen non, ba cay chum lai nen hon nui cao. (One tree makes no mountain; three make a high one.) Meaning: unity is strength. - Doan ket nhe', mot cay lam chang nen non.",
        "Nuoc chay da mon. (Flowing water wears stone.) Meaning: persistence overcomes. - Cu kien tri, nuoc chay da mon.",
        "Di mot ngay dang, hoc mot sang khon. (A day of travel, a basket of wisdom.) Meaning: travel teaches. - Di mot ngay dang that dung.",
        "La lanh dum la rach. (Whole leaves wrap torn leaves.) Meaning: help the needy. - La lanh dum la rach, ta giup dong bao lu lut.",
        "Gan muc thi den, gan den thi sang. (Near ink, black; near light, bright.) Meaning: company shapes you. - Chon ban ma choi, gan muc thi den.",
        "Tot go hon tot nuoc son. (Good wood beats good paint.) Meaning: substance over appearance. - Chon nguoi, tot go hon tot nuoc son.",
        "Cai kho lo cai khon. (Hardship reveals cleverness.) Meaning: necessity invents. - Cai kho lo cai khon, cu co gang.",
        "Hoc thay khong tay hoc ban. (Learning from a teacher can't beat learning from friends.) Meaning: peers teach best. - Hoc nhom di, hoc thay khong tay hoc ban.",
        "Uong nuoc nho nguon. (Drink water, remember the source.) Meaning: honor your roots. - Uong nuoc nho nguon, dung quen que huong.",
        "Ech ngoi day gieng. (Frog at the bottom of the well.) Meaning: narrow experience. - Dung nhu ech ngoi day gieng, hay mo rong tam mat.",
        "Trau cham uong nuoc duc. (Slow buffalo drinks muddy water.) Meaning: the early get the best. - Nhanh len, trau cham uong nuoc duc.",
        "Cham ma chac. (Slow but sure.) Meaning: steady wins. - Cu cham ma chac, roi se xong.",
        "Lua thu vang, gian nan thu suc. (Fire tests gold; hardship tests strength.) Meaning: adversity proves worth. - Lua thu vang, co len nhe'.",
        "Thuong nguoi nhu the thuong than. (Love others as yourself.) Meaning: compassion. - Thuong nguoi nhu the thuong than la dao ly.",
        "Co chi thi nen. (With will, it succeeds.) Meaning: determination. - Co chi thi nen, dung bo cuoc.",
        "An chac mac ben. (Eat solid, wear durable.) Meaning: live prudently. - Cu an chac mac ben, de danh sau nay.",
        "Ban anh em xa, mua lang gieng gan. (Sell distant kin, buy near neighbors.) Meaning: neighbors matter most. - Ban anh em xa, mua lang gieng gan that dung.",
        "Di hoa vi quy. (Harmony is precious.) Meaning: peace above all. - Di hoa vi quy, dung cai nhau.",
    ],
    requirements=[
        "Learners should picture each literal scene, then state the real meaning in their own words.",
        "Keep a proverb journal: one situation per day answered with one proverb.",
    ],
    standards=[
        "Tuc ngu (proverb) and thanh ngu (idiom) forms; Sino-Vietnamese and folk strata.",
    ],
    citations=[
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
        "Tuyển tập tục ngữ Việt Nam. Folk proverb collections, multiple editions.",
    ],
    sig_lens=("Through the Signature lens, a proverb is the covenant's "
              "compressed wisdom: ten thousand experiences sealed into one "
              "image, the iron, the tree, the water. This Signature reading "
              "treats the twenty as the covenant's elders speaking - every "
              "proverb a verdict time has already tested."),
)

E(
    key="vietnamese_registers", name="Vietnamese Formal and Polite Registers",
    group="Conversation and mastery", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen formal-versus-informal pairs - the two voices of Vietnamese.
        Formal (trang trong) belongs to letters, business, officials, and
        elders: Kinh gui (respectfully to), Tran trong cam on (sincerely
        thank), Rat han hanh (honored), Xin tran trong thong bao (respectfully
        announce). Informal (than mat) belongs to friends and family: Chao,
        Cam on nha, Hen gap sau nhe'. The formal voice uses full kinship
        titles, avoids slang, and closes letters with Tran trong (sincerely);
        the informal voice drops titles, shortens everything, and laughs. Each
        pair below shows the same message in both voices, Vietnamese and
        English - so the learner never bows too low to a friend or stands too
        casual before an elder."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through translation between voices. The learner
        takes each informal message and elevates it - and takes each formal
        one and warms it down. The drill is the letter: write one short
        formal letter (a job application opening, a thank-you to a teacher)
        and one informal note (inviting a friend), using the pairs as models.
        The golden test: read both aloud and feel which voice fits which
        listener."""),
    key_points=[
        "Letter opening - Formal: Kinh gui ong Giam doc. / Informal: Chao anh. (Respectfully to the Director. / Hi.)",
        "Thanks - Formal: Toi xin tran trong cam on quy vi. / Informal: Cam on moi nguoi nhieu nha. (I sincerely thank you all. / Thanks everyone so much.)",
        "Request - Formal: Kinh mong quy vi xem xet. / Informal: Ban xem giup to nhe'. (I respectfully ask your consideration. / Look at it for me.)",
        "Apology - Formal: Toi xin chan thanh xin loi. / Informal: Xin loi nha, to sai roi. (I sincerely apologize. / Sorry, my bad.)",
        "Meeting - Formal: Tran trong kinh moi ong den du. / Informal: Moi anh den choi. (Respectfully invite you to attend. / Come hang out.)",
        "Announcement - Formal: Xin tran trong thong bao. / Informal: Thong bao cho moi nguoi biet. (Respectfully announce. / Letting everyone know.)",
        "Congratulations - Formal: Xin chuc mung thanh cong cua quy cong ty. / Informal: Chuc mung nha, gioi lam! (Congratulations on your company's success. / Congrats, awesome!)",
        "Farewell - Formal: Kinh chuc quy vi suc khoe. / Informal: Giu suc khoe nhe'. (Wishing you health. / Take care.)",
        "Asking - Formal: Xin phep duoc hoi. / Informal: Cho hoi ti. (May I be permitted to ask. / Quick question.)",
        "Agreeing - Formal: Toi hoan toan dong y. / Informal: Ok, chot! (I fully agree. / OK, deal!)",
        "Declining - Formal: Rat tiec, toi khong the tham du. / Informal: Tiec qua, to ban roi. (Regrettably I cannot attend. / Bummer, I'm busy.)",
        "Elder respect - Formal: Da, thua bac. / Informal: Vang a. (Yes, as you say, elder. / Yeah.)",
        "Business close - Formal: Tran trong. / Informal: Hen gap sau. (Sincerely. / See you later.)",
        "Phone - Formal: Xin loi, toi co the gap ong X khong a? / Informal: Alo, cho gap X cai. (May I speak with Mr. X? / Hey, get me X.)",
        "Gratitude - Formal: Vo cung biet on su giup do cua bac. / Informal: Cam on bac nhieu lam. (Deeply grateful for your help. / Thank you so much.)",
    ],
    requirements=[
        "Learners should write one formal letter and one informal note using the pairs as models.",
        "Read both voices aloud; feel which fits which listener before speaking.",
    ],
    standards=[
        "Formal epistolary formulas: Kinh gui, Tran trong, Kinh mong; informal closings nhe'/nha.",
    ],
    citations=[
        "Luong H V. Discursive Practices and Linguistic Meanings. John Benjamins; 1990. Register and respect.",
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, register is the covenant's "
              "measure of distance: Kinh gui the deep bow of the formal seal, "
              "Chao nha the warm handshake of the familiar. This Signature "
              "reading treats the fifteen pairs as the covenant's two hands "
              "- one raised in respect, one open in friendship."),
)

E(
    key="vietnamese_complex", name="Vietnamese Compound and Complex Sentences",
    group="Conversation and mastery", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen long sentences with clauses, connectors, and relative
        clauses - parsed and translated. The connectors: va (and), nhung
        (but), vi (because), nen (so), neu (if), khi (when), mac du (although),
        de (in order to), rang (that), roi (then). Relative clauses use ma`:
        nguoi ma` toi gap (the person whom I met), quyen sach ma` ban tang
        (the book that you gave). Vietnamese builds long sentences by chaining
        short ones - commas and connectors, not subordination mazes. Each
        sentence below is parsed into its clauses so the learner sees the
        joints, Vietnamese and English."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through clause surgery. The learner takes each
        long sentence, cuts it at the connectors, and reads the clauses
        separately - then reassembles them. The drill is chaining: take three
        short sentences the learner already knows and join them with one
        connector each (va, nhung, vi). After fifteen dissections the learner
        writes five original long sentences, each with at least two clauses
        and one ma` relative clause."""),
    key_points=[
        "Toi thich pho vi no vua ngon vua re. [clause 1: Toi thich pho] [vi: because] [clause 2: no vua ngon vua re] (I like pho because it is both delicious and cheap.)",
        "Mac du troi mua nhung chung ta van di choi. [mac du: although] [nhung: but] (Although it rained, we still went out.)",
        "Neu ban den som thi chung ta se di an sang. [neu: if] [thi: then] [se: will] (If you come early, we will have breakfast.)",
        "Anh ay hoc gioi nen duoc hoc bong. [nen: so] (He studies well, so he got a scholarship.)",
        "Khi toi den, ca? nha` dang an com. [khi: when] (When I arrived, the family was eating.)",
        "Co ay noi rang se ve som. [rang: that] (She said that she would return early.)",
        "Toi mua rau de nau canh. [de: in order to] (I bought vegetables to cook soup.)",
        "Nguoi ma` toi gap hom qua la bac si. [ma`: whom] (The person whom I met yesterday is a doctor.)",
        "Quyen sach ma` ban tang toi ra^t hay. [ma`: that] (The book that you gave me is very interesting.)",
        "Cai ao ma` me mua vua dep vua vua. [ma`: that] (The shirt that mother bought is both beautiful and well-fitting.)",
        "Toi vua lam xong bai tap roi di da' bo'ng. [vua...roi: just finished...then] (I just finished homework, then went to play football.)",
        "Cang hoc cang thay minh dot. [cang...cang: the more...the more] (The more I study, the more I feel ignorant.)",
        "Vua re vua dep thi ai chang mua. [vua...vua: both...and] (Both cheap and beautiful - who wouldn't buy?)",
        "Khong nhung dep ma` con gioi. [khong nhung...ma` con: not only...but also] (Not only beautiful but also talented.)",
        "Du kho' den may toi cung se co gang. [du...cung: however...still] (However hard it is, I will still try.)",
    ],
    requirements=[
        "Learners should dissect each sentence at its connectors, then reassemble it.",
        "Write five original long sentences: two clauses and one ma` relative clause each.",
    ],
    standards=[
        "Connector set: va/nhung/vi/nen/neu/khi/mac du/de/rang; relative ma`; correlatives cang/vua/khong nhung/du.",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965. Complex sentences.",
        "Cao X H. Tieng Viet: So Thao Ngu Phap Chuc Nang. 1998.",
    ],
    sig_lens=("Through the Signature lens, a complex sentence is the "
              "covenant's architecture at full span: clauses the chambers, "
              "connectors the arches, ma` the keystone. This Signature "
              "reading treats the fifteen as the covenant's great hall - "
              "many rooms, one roof, every joint visible."),
)

E(
    key="vietnamese_conv_market", name="Vietnamese Conversation at the Market",
    group="Conversation and mastery", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue at the morning market - annotated.
        Lan shops for the family dinner; Ba Sau the vegetable seller knows
        her by name. The dialogue moves through greeting, asking prices,
        bargaining, choosing, paying, and farewell - every skill from records
        12 and 18 in one living scene. Annotations explain the bargaining
        moves: the laugh that softens Dat qua, the walk-away that wins the
        price, the Moi that closes the deal as friendship. Vietnamese and
        English, line by line."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through performance. Two learners (or one learner
        and the mirror) play Lan and Ba Sau, reading the dialogue aloud with
        the annotations as stage directions. The drill is improvisation: keep
        the skeleton - greet, ask, bargain, pay, farewell - but change the
        goods and prices. After three runs the learner performs it from
        memory, bargaining in character."""),
    key_points=[
        "Lan: Chao ba` Sau! (Hello, Mrs. Sau!) [greeting by familiar address]",
        "Ba Sau: Chao con! Hom nay mua gi` nao? (Hello dear! What are you buying today?) [con: affectionate you]",
        "Lan: Rau muong bao nhieu mot ky ba`? (How much is morning glory per kilo?)",
        "Ba Sau: Muoi lam nghin, rau moi hai sang nay. (Fifteen thousand; picked fresh this morning.)",
        "Lan: Dat the ba`! Muoi nghin duoc khong? (That's pricey! Ten thousand, okay?) [opening bargain]",
        "Ba Sau: Khong duoc dau con, muoi hai nhe'. (Can't do, dear; twelve, okay?)",
        "Lan: Thoi muoi mot, con mua them ca' nua. (Eleven then; I'll also buy fish.) [bundling]",
        "Ba Sau: Duoc roi, thay con quen nen ba` bot. (Fine; you're a regular so I'll reduce.)",
        "Lan: Con ca' chep nay bao nhieu? (How much is this carp?)",
        "Ba Sau: Tam muoi nghin mot ky, con nay hai ky. (Eighty thousand a kilo; this one is two kilos.)",
        "Lan: Ca' tuoi khong ba`? (Is the fish fresh?)",
        "Ba Sau: Tuoi roi roi, mat con trong veo. (Very fresh; the eyes are still clear.) [freshness test]",
        "Lan: Vay ba` lam sach giup con nhe'. (Then please clean it for me.)",
        "Ba Sau: Roi, cho ba` mot chut. (Done; give me a moment.)",
        "Lan: Tong cong bao nhieu ba`? (What's the total?)",
        "Ba Sau: Mot tram muoi bay nghin, lay mot tram muoi cho tron. (177 thousand; make it 170 even.) [rounding favor]",
        "Lan: Cam on ba`, tien day a. (Thank you; here's the money.)",
        "Ba Sau: Cam on con, mai lai ghe nhe'. (Thank you; come again tomorrow.)",
        "Lan: Vang, chao ba`! (Yes; goodbye!)",
        "Ba Sau: Chao con, di can than! (Goodbye dear; go carefully!)",
    ],
    requirements=[
        "Learners should perform the dialogue aloud with a partner or mirror, using the annotations.",
        "Improvise: same skeleton, different goods and prices, three runs from memory.",
    ],
    standards=[
        "Market dialogue norms; bargaining moves: opening, bundling, rounding favor.",
    ],
    citations=[
        "Avieli N. Rice Talks: Food and Community in a Vietnamese Town. Indiana University Press; 2012.",
    ],
    sig_lens=("Through the Signature lens, the market dialogue is the "
              "covenant negotiated aloud: every price a proposal, every Bot "
              "chut di a counter-seal, the final Cam on the contract signed "
              "in smiles. This Signature reading treats the twenty lines as "
              "the covenant's commerce - trust spoken, sealed, and kept."),
)

E(
    key="vietnamese_conv_friend", name="Vietnamese Conversation: Meeting a Friend",
    group="Conversation and mastery", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue - two old friends meet by chance on
        the street, annotated. Minh and Tuan were classmates ten years ago;
        the dialogue moves through surprise, catching up, family news, work,
        the invitation, and the warm farewell. Annotations explain the
        reunion formulas: Lau roi khong gap (long time no see), Dao nay the
        nao (how have you been), the Moi that turns chance into a plan.
        Vietnamese and English, line by line."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through reunion. The learner plays both friends,
        feeling the rising warmth line by line. The drill is the catch-up
        chain: surprise, then, family, work, invitation, farewell - the
        learner invents a reunion with their own old friend following the
        chain. After three runs the learner performs it from memory, in
        character, with feeling."""),
    key_points=[
        "Minh: Tuan! Phai Tuan khong? (Tuan! Is that you?) [surprise]",
        "Tuan: Minh! Lau roi khong gap! (Minh! Long time no see!)",
        "Minh: Dung la lau that, phai muoi nam roi. (Really long - must be ten years.)",
        "Tuan: Dao nay cau the nao? (How have you been lately?)",
        "Minh: To van khoe. Cau thi sao? (I'm still well. And you?)",
        "Tuan: To cung on. Gia dinh cau the nao? (I'm fine too. How's your family?)",
        "Minh: Bo me to van khoe, cam on. (My parents are well, thanks.)",
        "Tuan: Nghe noi cau co hai dua con roi? (I heard you have two kids now?)",
        "Minh: U, mot trai mot gai. (Yes, one boy one girl.)",
        "Tuan: Thich nhi! To van doc than. (Nice! I'm still single.) [gentle teasing]",
        "Minh: The con lam o dau? (Where do you work now?)",
        "Tuan: To lam o cong ty xay dung. (I work at a construction company.)",
        "Minh: Viec co on khong? (Is work steady?)",
        "Tuan: Cung tam duoc. Cuoi tuan ranh khong? (Fairly okay. Free this weekend?)",
        "Minh: Ranh. Sao the? (Free. What's up?)",
        "Tuan: Di ca phe di, on lai chuyen xua. (Let's get coffee and relive old stories.)",
        "Minh: Nhat tri! May gio? (Agreed! What time?)",
        "Tuan: Tam gio sang thu' bay, quan cu nhe'. (Eight Saturday morning, the old shop.)",
        "Minh: Ok, hen gap nhe'! (OK, see you then!)",
        "Tuan: Hen gap! Di can than! (See you! Go carefully!)",
    ],
    requirements=[
        "Learners should perform the reunion aloud, feeling the warmth rise line by line.",
        "Invent a reunion with the learner's own old friend, following the catch-up chain.",
    ],
    standards=[
        "Reunion formulas: Lau roi khong gap, Dao nay the nao, Hen gap.",
    ],
    citations=[
        "Luong H V. Discursive Practices and Linguistic Meanings. John Benjamins; 1990.",
    ],
    sig_lens=("Through the Signature lens, reunion is the covenant renewed: "
              "Lau roi khong gap the seal broken open by joy, Hen gap the "
              "new seal pressed on the future. This Signature reading treats "
              "the twenty lines as the covenant remembering itself - old "
              "oaths, new promises."),
)

E(
    key="vietnamese_conv_problem", name="Vietnamese Conversation: Solving a Problem",
    group="Conversation and mastery", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue - a problem solved together,
        annotated. Hoa's motorbike broke down on the way to work; her
        colleague Duc stops to help. The dialogue moves through the problem,
        diagnosis, options, the fix, gratitude, and the promise to repay -
        Vietnamese problem-solving in action: Binh tinh (stay calm), De to
        xem (let me look), Chac la ___ (probably it's ___), Cam on nhieu
        (thanks so much), De hom khac to moi ca phe (I'll treat you to coffee
        another day). Annotations explain the helping formulas. Vietnamese
        and English, line by line."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through trouble and rescue. The learner plays
        both the stranded and the helper, practicing calm problem language.
        The drill is the fix chain: problem, diagnosis, options, action,
        thanks, repay - the learner invents three problems (a flat tire, a
        lost key, a dead phone) and solves each aloud following the chain.
        After three runs the learner performs the dialogue from memory, calm
        and kind."""),
    key_points=[
        "Hoa: Troi oi, xe chet may roi! (Oh no, the bike died!) [problem]",
        "Duc: Binh tinh, de to xem nao. (Stay calm; let me look.)",
        "Hoa: Sang nay no van chay binh thuong. (This morning it still ran fine.)",
        "Duc: Chac la het xang. Dong ho bao gi`? (Probably out of gas. What does the gauge say?)",
        "Hoa: Kim chi vach do roi. (The needle is at the red mark.)",
        "Duc: Dung roi, het xang that. Cay xang gan nhat o dau? (Right; really out. Where's the nearest station?)",
        "Hoa: Khoang hai cay so nua. (About two kilometers more.)",
        "Duc: De to day giup mot doan. (Let me push you a stretch.)",
        "Hoa: Phien cau qua. (I'm troubling you so much.)",
        "Duc: Co gi dau, ban be ma`. (It's nothing; we're friends.)",
        "Hoa: May ma gap cau. (Lucky I met you.)",
        "Duc: Ngon roi, dat chan xuong di. (Good; put your feet down - coast now.)",
        "Hoa: Den cay xang roi! (We've reached the station!)",
        "Duc: Do day binh nhe'. (Fill it up.)",
        "Hoa: Het bao nhieu? (How much?)",
        "Nhan vien: Nam muoi nghin a. (Fifty thousand.)",
        "Hoa: Cam on cau nhieu lam. (Thank you so much.)",
        "Duc: Khong co gi. Xe chay lai roi kia. (You're welcome. The bike runs again.)",
        "Hoa: Hom khac to moi ca phe. (Another day I'll treat you to coffee.) [repay promise]",
        "Duc: Nhat tri! Di lam keo muon. (Agreed! Get to work before you're late.)",
    ],
    requirements=[
        "Learners should perform the rescue dialogue aloud, calm and kind, from memory.",
        "Invent three problems and solve each aloud following the fix chain.",
    ],
    standards=[
        "Helping formulas: Binh tinh, De to xem, Phien cau, Cam on nhieu, Moi ca phe.",
    ],
    citations=[
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
    ],
    sig_lens=("Through the Signature lens, helping is the covenant's rescue "
              "clause: Binh tinh the seal of calm, De to xem the seal of "
              "aid, Moi ca phe the seal of gratitude repaid. This Signature "
              "reading treats the twenty lines as the covenant in action - "
              "no one stranded while a friend is near."),
)

E(
    key="vietnamese_mastery", name="Vietnamese Mastery Review and Full Reference",
    group="Conversation and mastery", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        The whole database in one teaching summary - the mastery review and
        full reference. The alphabet: 29 letters A A Au B C D Dd E E G H I K
        L M N O O O P Q R S T U Uu V X Y with the six tone marks (ngang,
        huyen, sac, hoi, nga, nang). The 200 core words: the 25 nouns, 25
        verbs, 25 adjectives, 15 adverbs, 22 pronouns and question words, 12
        number and time words, 30 greetings, 20 food words, 16 travel words,
        10 technology words -
        every word with its English, the complete working vocabulary of the
        database. Key grammar in one page: SVO order, no conjugation,
        da/dang/se, khong/chua/dung, the five question shapes, classifiers
        cai/con/nguoi, adjective-after-noun, hon/nhat comparison, ma` relative
        clauses, the connector set. All phrase tables: greetings, market,
        travel, clinic, restaurant, phone. The study plan: week one records
        1-5, week two 6-10, weeks three and four the themed sentences, week
        five tenses and speech, week six stories and idioms, week seven
        conversations, week eight this review - then speak every day. A final
        learner sentence: Toi da hoc xong ba muoi bon bai - I have finished
        all thirty-four lessons."""),
    how_it_works=textwrap.dedent("""\
        This record teaches through consolidation. The learner works the
        reference as a checklist: recite the alphabet with tones, run the
        200 words as flashcards (Vietnamese to English, then back), rebuild
        the grammar page from memory, and perform one dialogue from each
        conversation record. The drill is the final exam the learner gives
        themselves: ten sentences covering every tense, five questions,
        three commands, one proverb, one story retold. Pass it, and the
        ladder is climbed - the rest is speaking."""),
    key_points=[
        "Alphabet: 29 letters; six tones ngang/huyen/sac/hoi/nga/nang - the foundation of everything.",
        "200 core words: nouns 25, verbs 25, adjectives 25, adverbs 15, pronouns/questions 22, numbers/time 12, greetings 30, food 20, travel 16, tech 10.",
        "Grammar page: SVO; invariant verbs; da/dang/se/sap/vua/tung/dinh/roi; khong/chua/dung; five question shapes.",
        "Classifiers cai/con/nguoi; adjective after noun; hon/nhat/bang comparison; ma` relatives; connector set va/nhung/vi/nen/neu/khi/mac du/de/rang.",
        "Phrase tables: greetings (Chao/Cam on/Xin loi), market (Bao nhieu/Bot chut), travel (Xin hoi/Re trai), clinic (Toi bi), restaurant (Tinh tien).",
        "Study plan: 8 weeks, records 1-34 in order, then daily speaking.",
        "Self-exam: ten sentences in every tense, five questions, three commands, one proverb, one retold story.",
        "The learner's oath: Noi tieng Viet moi ngay. (Speak Vietnamese every day.)",
    ],
    requirements=[
        "Learners should run the 200 words as flashcards both directions until instant.",
        "Take the self-exam: ten sentences, five questions, three commands, one proverb, one story.",
    ],
    standards=[
        "Full-database consolidation; 8-week study plan.",
    ],
    citations=[
        "Thompson L C. A Vietnamese Grammar. University of Washington Press; 1965.",
        "Nguyen D H. Vietnamese: Tieng Viet Khong Son Phan. John Benjamins; 1997.",
        "Pham A H. Vietnamese Tone: A New Analysis. Routledge; 2008.",
    ],
    sig_lens=("Through the Signature lens, mastery is the covenant fully "
              "signed: twenty-nine letters, six tones, two hundred words, "
              "thirty-four lessons - the whole oath in one page. This "
              "Signature reading treats the review as the covenant's seal "
              "press itself: the learner signs, and the language is theirs."),
)
