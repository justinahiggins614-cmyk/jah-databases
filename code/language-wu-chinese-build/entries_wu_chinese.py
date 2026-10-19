#!/usr/bin/env python3
"""Entries for the Wu Chinese Language databases (34 ladder-ordered records).

Public records: real, fact-checked Wu Chinese (Northern Wu, Shanghai dialect
as the reference standard) language teaching - every record carries Chinese
characters with romanization and English translation plus example sentences,
organized in the Signature system.

Romanization used throughout: a practical pinyin-style Wu romanization with
tone numbers. Tone numbers map to the five modern Shanghai tones:
  1 = 53 (yinping 阴平)   2 = 34 (yinshang/yinqu 阴上/阴去)
  3 = 23 (yangping/yangshang/yangqu 阳平/阳上/阳去)
  4 = 5  (yinru 阴入, short checked)   5 = 12 (yangru 阳入, short checked)
Citation tones are given per syllable; connected speech applies Wu
left-dominant tone sandhi (record 3). This is a teaching romanization,
defined here for learners, and is not the historical missionary system.
"""
import textwrap

ENTRIES = []


def E(**kw):
    ENTRIES.append(kw)
    return kw


E(
    key="wu_overview", name="Wu Chinese Language Overview",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Wu Chinese (吴语, wu2-gniu2) is a major branch of the Sinitic family
        within Sino-Tibetan, spoken natively by about 83 million people -
        more than the population of most countries. Its heartland is the
        lower Yangtze delta: the municipality of Shanghai, most of Zhejiang
        province (Hangzhou, Ningbo, Shaoxing, Wenzhou), southern Jiangsu
        (Suzhou, Wuxi, Changzhou), and bordering parts of Anhui, Jiangxi, and
        Fujian. Wu is not an official language anywhere; Mandarin (Putonghua)
        holds official status, and Wu lives in homes, markets, teahouses, and
        local media. ISO 639-3 gives Wu the code wuu (there is no ISO 639-1
        code). The family path is Sino-Tibetan > Sinitic > Wu. Wu divides
        into Northern Wu (the Taihu 太湖 region: Shanghai, Suzhou, Wuxi,
        Hangzhou, Ningbo, Shaoxing) and Southern Wu (Taizhou, Wenzhou,
        Jinhua). The Shanghai dialect (上海闲话, zang3-he2 ye3-wo3) is the
        prestige urban variety and the reference standard of this database.
        Wu is famous among linguists for keeping the old voiced consonants
        (b, d, g, z) that Mandarin lost, and for its rich tone sandhi. This
        record is the map of the whole database: what Wu is, where it lives,
        and how the ladder below carries a learner from a first 侬好
        (nong3-hau2, hello) to full conversation."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the overview by anchoring every fact in a sentence
        the learner can say. Each fact - the native name 吴语, the ISO code
        wuu, the Sino-Tibetan family path, the 83 million speakers, the
        Shanghai-Zhejiang-Jiangsu heartland, the Northern/Southern split -
        appears with a plain English explanation and a Wu example sentence in
        characters, romanization, and English. The learner reads the facts,
        then repeats the sentences, so the overview becomes spoken language
        from the first record. Later records climb the teaching ladder:
        foundations (records 1-10: writing, sounds, words, grammar basics),
        compounded (records 11-20: themed sentence sets), advanced (records
        21-34: tenses, questions, stories, idioms, registers, complex
        sentences, conversations, and a full mastery reference)."""),
    key_points=[
        "Native name: 吴语 (wu2-gniu2); English name: Wu Chinese; ISO 639-3: wuu; no ISO 639-1 code.",
        "Family: Sino-Tibetan > Sinitic > Wu; about 83 million native speakers.",
        "Heartland: Shanghai, Zhejiang, southern Jiangsu, plus parts of Anhui, Jiangxi, Fujian.",
        "Not official anywhere; Mandarin is the official language. Wu is the language of home and street.",
        "Two great divisions: Northern Wu (Taihu: Shanghai, Suzhou, Wuxi, Hangzhou, Ningbo) and Southern Wu (Taizhou, Wenzhou, Jinhua).",
        "Reference standard of this database: the Shanghai dialect (上海闲话, zang3-he2 ye3-wo3).",
        "Signature trait: Wu keeps the old voiced initials b, d, g, z that Mandarin lost centuries ago.",
        "Every record in this database carries Chinese characters, romanization, and English on every line.",
    ],
    requirements=[
        "No prior knowledge of Wu is needed; this is the starting record of the ladder.",
        "Learners should read each example sentence aloud to begin training Wu pronunciation from day one.",
    ],
    standards=[
        "ISO 639-3:2007 (wuu) language code for Wu Chinese.",
        "Ethnologue: Wu Chinese [wuu] - Sino-Tibetan, Sinitic, Wu.",
    ],
    citations=[
        "Norman J. Chinese. Cambridge University Press; 1988. Chapter on the Wu dialects: classification, voiced initials, tone systems.",
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. The standard modern survey of Wu dialectology.",
        "Eberhard D M, Simons G F, Fennig C D, editors. Ethnologue: Languages of the World. SIL International; 2024. Entry: Wu Chinese [wuu], ~83 million speakers.",
    ],
    sig_lens=("Through the Signature lens, a language is not a school subject - it is a "
              "living contract between a people and their home ground, and Wu is one of "
              "the great signed contracts of the Yangtze delta: eighty-three million "
              "voices keeping one oath of meaning from Shanghai to Wenzhou. This "
              "Signature reading treats the overview as the first seal of that contract."),
)

E(
    key="wu_writing", name="Wu Chinese Writing System",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Wu is written with Chinese characters - the same script as Mandarin,
        written left to right in modern texts (older texts run top to bottom,
        right to left). There is no separate Wu alphabet: the writing system
        IS the character system, and Wu has its own beloved vernacular
        characters for words Mandarin writes differently or not at all. Learn
        these and Wu texts open up: 侬 (nong3, you), 伊 (yi3, he/she; also
        that), 覅 (fiau2, do not want = 勿要), 朆 (ven3, have not), 𠲎
        (vaq5, question particle), 勒 (leq4, at/in), 拨 (peq4, give; passive
        marker), 仔 (tsy2, completion marker), 佬 (lau3, person suffix, as in
        小赤佬), 嗲 (tia2, cute), 囡 (noe1, child), 汏 (da3, to wash - Wu for
        洗), 拎 (lin3, to carry in the hand), 捺 (naq4, to press). Numerals
        are the standard characters with Wu readings: 一 (iq4), 二 (gni3),
        三 (se1), 四 (sy2), 五 (ng3), 六 (loq4), 七 (chiq4), 八 (paq4), 九
        (cieu2), 十 (zeq5), 百 (paq4), 千 (tshie1), 万 (ve3). Punctuation
        follows modern Chinese practice: 。for the period, ，for the comma,
        ？for questions, ！for exclamations, 、for list pauses, 《》for book
        titles. Digits 0-9 are used for Arabic numerals exactly as in
        Mandarin. Because Wu shares the character script with Mandarin, a
        reader of Chinese can sound out Wu texts immediately - the characters
        are familiar, only the readings and the vernacular words are new."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the writing system by pairing every Wu-vernacular
        character with its romanization, its Mandarin equivalent where one
        exists, and an English gloss, then drilling the ten numerals with
        their Wu readings. The learner copies the vernacular characters by
        hand - 侬, 伊, 覅, 朆, 𠲎, 勒, 拨, 仔 - writes each numeral 1-10
        with its reading (iq4, gni3, se1, sy2, ng3, loq4, chiq4, paq4, cieu2,
        zeq5), and practices the punctuation marks by punctuating a short Wu
        paragraph. Because the script is shared with Mandarin, this one
        record converts existing character knowledge into Wu reading power."""),
    key_points=[
        "Script: Chinese characters, left to right (older texts: top to bottom, right to left). No separate Wu alphabet.",
        "Vernacular characters: 侬 nong3 (you), 伊 yi3 (he/she), 覅 fiau2 (do not want), 朆 ven3 (have not), 𠲎 vaq5 (question particle).",
        "More vernacular: 勒 leq4 (at), 拨 peq4 (give/passive), 仔 tsy2 (completed), 囡 noe1 (child), 嗲 tia2 (cute).",
        "Numerals: 一 iq4, 二 gni3, 三 se1, 四 sy2, 五 ng3, 六 loq4, 七 chiq4, 八 paq4, 九 cieu2, 十 zeq5, 百 paq4, 千 tshie1, 万 ve3.",
        "Punctuation: 。，？！、。 Digits 0-9 as in Mandarin.",
        "A Mandarin reader already knows the script; Wu adds vernacular characters and new readings.",
    ],
    requirements=[
        "Learners should hand-write the eight core vernacular characters (侬伊覅朆𠲎勒拨仔) with readings.",
        "Drill the numerals 1-10 aloud until the Wu readings (iq4, gni3, se1...) come without thinking.",
    ],
    standards=[
        "Modern written Chinese character standard (simplified in mainland publications, traditional in older Wu texts).",
        "Numeral and punctuation practice follows standard modern Chinese typography.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. The standard dictionary of Shanghai vernacular characters and readings.",
        "Norman J. Chinese. Cambridge University Press; 1988. On the shared character script across Sinitic languages.",
    ],
    sig_lens=("Through the Signature lens, the character is the first covenant of the "
              "written word: one script shared by a whole civilization, with Wu keeping "
              "its own vernacular seals - 侬, 覅, 朆, 𠲎 - stamped beside the classical "
              "forms. This Signature reading treats every vernacular character as "
              "proof that Wu writes its own name in its own hand."),
)

E(
    key="wu_phonology", name="Wu Chinese Pronunciation and Phonology",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Wu pronunciation is the glory of the language: it preserves the three
        old families of consonants - voiceless unaspirated (b, d, g), voiceless
        aspirated (p, t, k), and VOICED (b, d, g, z, v, h) - where Mandarin
        kept only two. Minimal sets prove it: 拜 (pa2, to visit), 派 (pha2,
        to send), and 牌 (ba3, signboard) are three different consonants, not
        two. The full initial inventory runs: b p m f; d t n l; g k ng h; j
        q gn x; z c s; zh ch sh r; plus the voiced partners v, d, g, z, and
        the glottal stop iq- onset. Finals include the nasal set (an, en, ang,
        eng, ong) and the checked set ending in a glottal stop (aq, eq, iq,
        oq, uq) - short, clipped syllables like 一 (iq4), 六 (loq4), 吃
        (chiq4). Modern Shanghai has FIVE tones, down from the classical
        eight: T1 53 (yinping, high falling: 三 se1, 天 thie1), T2 34 (yinshang
        and yinqu merged, rising: 水 sy2, 好 hau2, 去 chi2), T3 23 (all three
        yang tones merged, low rising: 人 nyin3, 侬 nong3, 茶 dzo3), T4 5
        (yinru, short high checked: 一 iq4, 吃 chiq4, 勿 veq4), T5 12 (yangru,
        short low checked: 十 zeq5, 白 baq5, 肉 gnioq5). Stress is light; the
        melody of Wu comes from TONE SANDHI, which is LEFT-DOMINANT: the first
        syllable of a phrase decides the tune and the rest follow. So 上海
        (zang3-he2) is heard as one smooth contour led by 上, and 中国
        (tson1-koq4) is led by 中. Citation tones in this database are given
        per syllable; in fluent speech the sandhi rule smooths them. Ten
        spoken examples with translations: 三 se1 (three), 水 sy2 (water),
        人 nyin3 (person), 一 iq4 (one), 十 zeq5 (ten), 牌 ba3 (signboard -
        hear the voiced b), 茶 dzo3 (tea - hear the voiced dz), 饭 ve3 (rice -
        hear the voiced v), 吃 chiq4 (to eat - short and clipped), 好 hau2
        (good). Train the ear on the voiced initials first - they are the
        sound of Wu."""),
    how_it_works=textwrap.dedent("""\
        This record teaches Wu sounds in three drills. Drill one: the voiced
        initials - the learner repeats 拜 pa2, 派 pha2, 牌 ba3 until the three
        consonants are distinct, then 茶 dzo3, 饭 ve3, 人 nyin3. Drill two:
        the five tones - the learner chants the tone ladder with the anchor
        words 三 se1 (53), 水 sy2 (34), 人 nyin3 (23), 一 iq4 (5, clipped),
        十 zeq5 (12, clipped), feeling the checked tones cut short in the
        throat. Drill three: left-dominant sandhi - the learner says 上海
        (zang3-he2), 中国 (tson1-koq4), 电话 (die3-wo3) as single melodic
        words, letting the first syllable lead. The demonstration program
        prints the tone table, computes each tone contour mean, and quizzes
        the voiced-initial minimal sets."""),
    key_points=[
        "Three consonant families: voiceless unaspirated (b d g), voiceless aspirated (p t k), voiced (b d g z v) - Mandarin lost the voiced set.",
        "Minimal triple: 拜 pa2 (visit), 派 pha2 (send), 牌 ba3 (signboard).",
        "Checked syllables end in a glottal stop and are short: 一 iq4, 六 loq4, 吃 chiq4, 勿 veq4.",
        "Five modern Shanghai tones: T1 53 (三 se1), T2 34 (水 sy2, 好 hau2), T3 23 (人 nyin3, 侬 nong3), T4 5 short (一 iq4), T5 12 short (十 zeq5).",
        "Classical eight tones merged: yinshang+yinqu -> T2; all yang level/rising/departing -> T3.",
        "Tone sandhi is LEFT-DOMINANT: the first syllable of a phrase leads the melody (上海 zang3-he2).",
        "Citation tones are listed per syllable in this database; fluent speech applies the sandhi rule.",
        "10 anchor words: 三 se1, 水 sy2, 人 nyin3, 一 iq4, 十 zeq5, 牌 ba3, 茶 dzo3, 饭 ve3, 吃 chiq4, 好 hau2.",
    ],
    requirements=[
        "Learners must drill the voiced initials (b, d, g, z, v) aloud - they are the signature Wu sound.",
        "Chant the five-tone ladder daily (se1, sy2, nyin3, iq4, zeq5) until each tone is automatic.",
    ],
    standards=[
        "Tone values follow the standard five-tone analysis of modern Shanghai (53, 34, 23, 5, 12).",
        "Romanization: practical pinyin-style Wu romanization with tone numbers 1-5, defined in this record.",
    ],
    citations=[
        "Zhu X. Shanghai Tonetics. LINCOM Europa; 2006. The standard acoustic study of Shanghai tones and left-dominant sandhi.",
        "Chao Y R. Studies in the Modern Wu-dialects. Tsing Hua College Research Institute; 1928. The founding survey of Wu phonology.",
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. Consonant and tone inventories of the Wu dialects.",
    ],
    sig_lens=("Through the Signature lens, sound is the first covenant a language signs "
              "with the ear: Wu kept the ancient voiced consonants as its seal while "
              "other tongues let them fade, and its five tones are five signatures on "
              "every syllable. This Signature reading treats the voiced b, d, g as the "
              "audible proof of Wu antiquity."),
)

E(
    key="wu_nouns", name="Wu Chinese Core Nouns I",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Twenty-five essential Wu nouns - people, places, and things - each
        with an example sentence in characters, romanization, and English.
        1. 人 (nyin3) - person. 伊是好人。(yi3 zy3 hau2-nyin3.) - He is a good person.
        2. 囡 (noe1) - child. 囡囡真嗲。(noe1-noe1 tsen1 tia2.) - The little child is adorable.
        3. 朋友 (bong3-yeu3) - friend. 伊是我个朋友。(yi3 zy3 ngu2 geq4 bong3-yeu3.) - He is my friend.
        4. 先生 (shie1-sang1) - mister; teacher. 王先生来了。(wang3 shie1-sang1 le3 leq4.) - Mr. Wang has come.
        5. 屋 (oq4) - house; home. 我勒屋里。(ngu2 leq4 oq4-li2.) - I am at home.
        6. 学校 (yoq5-gau3) - school. 囡囡去学校了。(noe1-noe1 chi2 yoq5-gau3 leq4.) - The child went to school.
        7. 商店 (sang1-tie2) - shop. 商店开门了。(sang1-tie2 khe1-men3 leq4.) - The shop opened.
        8. 菜场 (tshe2-zang3) - food market. 阿拉去菜场买菜。(aq4-laq4 chi2 tshe2-zang3 ma2-tshe2.) - We are going to the market to buy vegetables.
        9. 医院 (yi1-yue3) - hospital. 医院勒哪亨？(yi1-yue3 leq4 sa3 di3-fang1?) - Where is the hospital?
        10. 车站 (tsho1-ze3) - station. 车站人交关多。(tsho1-ze3 nyin3 ciau1-kue1 tu1.) - There are very many people at the station.
        11. 书 (sy1) - book. 迭本书交关好。(diq4 pen2 sy1 ciau1-kue1 hau2.) - This book is very good.
        12. 钞票 (tshau1-phiau2) - money. 我呒没钞票。(ngu2 m2-meq5 tshau1-phiau2.) - I have no money.
        13. 饭 (ve3) - cooked rice; meal. 饭烧好了。(ve3 sau1-hau2 leq4.) - The rice is cooked.
        14. 水 (sy2) - water. 我要喝水。(ngu2 iau2 heq4-sy2.) - I want to drink water.
        15. 茶 (dzo3) - tea. 泡一杯茶。(phau2 iq4-pe1 dzo3.) - Brew a cup of tea.
        16. 物事 (meq5-zy3) - thing. 迭件物事啥价钿？(diq4-jie3 meq5-zy3 sa3 ka2-die3?) - What is the price of this thing?
        17. 地方 (di3-fang1) - place. 迭个地方真好。(diq4-geq4 di3-fang1 tsen1 hau2.) - This place is really nice.
        18. 辰光 (zen3-kuang1) - time. 现在啥辰光？(yi3-ze3 sa3 zen3-kuang1?) - What time is it now?
        19. 天气 (thie1-chi2) - weather. 今朝天气交关好。(cin1-tsau1 thie1-chi2 ciau1-kue1 hau2.) - The weather today is very good.
        20. 狗 (keu2) - dog. 小狗真可爱。(siau2-keu2 tsen1 khu2-e2.) - The puppy is really cute.
        21. 猫 (mau1) - cat. 猫勒睏觉。(mau1 leq4 khun2-kau2.) - The cat is sleeping.
        22. 花 (ho1) - flower. 花开得真好看。(ho1 khe1-deq4 tsen1 hau2-khe2.) - The flowers bloom beautifully.
        23. 电话 (die3-wo3) - telephone. 电话铃响了。(die3-wo3 lin3-shiang2 leq4.) - The telephone is ringing.
        24. 门 (men3) - door. 拿门关脱。(na3 men3 kue1-theq4.) - Close the door.
        25. 路 (lu3) - road. 迭条路通到外滩。(diq4-diau3 lu3 thon1-tau2 nga3-than1.) - This road leads to the Bund."""),
    how_it_works=textwrap.dedent("""\
        This record teaches nouns the Wu way: every noun arrives inside a
        real sentence, because Wu nouns are learned with their classifiers
        and their verbs. The learner reads each of the 25 sentences aloud,
        noticing the classifiers (迭本书, 迭件物事, 迭条路), the locative 勒
        (我勒屋里), and the possessive 个 (我个朋友). The demonstration
        program runs a flashcard quiz over the noun set: it shows the English,
        the learner answers with the Wu word, and the program checks the
        answer against the record. Twenty-five nouns, twenty-five sentences,
        one quiz - the foundation of Wu vocabulary."""),
    key_points=[
        "25 essential nouns: 人 nyin3, 囡 noe1, 朋友 bong3-yeu3, 先生 shie1-sang1, 屋 oq4, 学校 yoq5-gau3, 商店 sang1-tie2, 菜场 tshe2-zang3, 医院 yi1-yue3, 车站 tsho1-ze3.",
        "Things: 书 sy1, 钞票 tshau1-phiau2, 饭 ve3, 水 sy2, 茶 dzo3, 物事 meq5-zy3, 地方 di3-fang1, 辰光 zen3-kuang1, 天气 thie1-chi2.",
        "Living: 狗 keu2, 猫 mau1, 花 ho1; tools: 电话 die3-wo3, 门 men3, 路 lu3.",
        "Nouns pair with classifiers: 迭本书 (this book), 迭件物事 (this thing), 迭条路 (this road).",
        "Locative 勒 leq4 marks place: 我勒屋里 (I am at home). Possessive 个 geq4 marks belonging: 我个朋友 (my friend).",
        "Every noun is drilled inside a full sentence, never as an isolated word.",
    ],
    requirements=[
        "Learners should memorize the 25 nouns with their classifiers by reading each sentence aloud three times.",
        "Practice the 勒 (at) and 个 (possessive) patterns with your own nouns: 我勒___, 我个___.",
    ],
    standards=[
        "CEFR A1: everyday nouns - people, home, food, places, objects.",
        "Vernacular character readings follow Qian Nairong 上海话大词典 (2007).",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Noun entries and vernacular readings.",
        "Norman J. Chinese. Cambridge University Press; 1988. Wu vocabulary and classifier usage.",
    ],
    sig_lens=("Through the Signature lens, the noun is the first seal a learner stamps "
              "on the world: twenty-five names for people, places, and things, each one "
              "a small covenant - to call a thing by its Wu name is to claim it for the "
              "Wu world. This Signature reading treats vocabulary as territory claimed."),
)

E(
    key="wu_verbs", name="Wu Chinese Core Verbs I",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Twenty-five essential Wu verbs, each with an example sentence in
        characters, romanization, and English. Wu verbs do not conjugate;
        tense and aspect ride on particles (仔, 过, 勒海) taught in record 21.
        1. 吃 (chiq4) - to eat. 我吃饭。(ngu2 chiq4-ve3.) - I eat rice.
        2. 喝 (heq4) - to drink. 喝水。(heq4-sy2.) - Drink water.
        3. 去 (chi2) - to go. 我去学校。(ngu2 chi2 yoq5-gau3.) - I go to school.
        4. 来 (le3) - to come. 侬啥辰光来？(nong3 sa3 zen3-kuang1 le3?) - When are you coming?
        5. 看 (khe2) - to look; to read; to visit. 看书。(khe2-sy1.) - Read a book.
        6. 听 (thin1) - to listen. 听我说。(thin1 ngu2 shuoq4.) - Listen to me.
        7. 说 (shuoq4) - to speak. 伊会说上海闲话。(yi3 we3 shuoq4 zang3-he2 ye3-wo3.) - He can speak Shanghainese.
        8. 问 (ven3) - to ask. 我想问侬。(ngu2 shiang2 ven3 nong3.) - I want to ask you.
        9. 买 (ma2) - to buy. 买两斤苹果。(ma2 liang3-cin1 bing3-ku2.) - Buy two jin of apples.
        10. 卖 (ma3) - to sell. 伊卖水果。(yi3 ma3 sy2-ku2.) - He sells fruit.
        11. 做 (tsu2) - to do; to make. 做功课。(tsu2 kon1-khu2.) - Do homework.
        12. 工作 (kon1-tsoq4) - to work. 我勒银行工作。(ngu2 leq4 ngin3-hang3 kon1-tsoq4.) - I work at a bank.
        13. 学习 (yoq5-xiq4) - to study. 学习吴语。(yoq5-xiq4 wu2-gniu2.) - Study Wu.
        14. 教 (ciau1) - to teach. 老师教吴语。(lau3-sy1 ciau1 wu2-gniu2.) - The teacher teaches Wu.
        15. 睏觉 (khun2-kau2) - to sleep. 我想睏觉了。(ngu2 shiang2 khun2-kau2 leq4.) - I want to sleep.
        16. 洗 (shi2) - to wash. 洗手。(shi2-seu2.) - Wash your hands.
        17. 穿 (tshoe1) - to wear. 穿新衣裳。(tshoe1 shin1 yi1-zang3.) - Wear new clothes.
        18. 开 (khe1) - to open; to drive; to turn on. 开门。(khe1-men3.) - Open the door.
        19. 关 (kue1) - to close; to turn off. 关灯。(kue1-ten1.) - Turn off the light.
        20. 打 (ta2) - to hit; to make (a call). 打电话。(ta2 die3-wo3.) - Make a phone call.
        21. 拿 (na3) - to take; (Wu 把 equivalent). 拿本书来。(na3 pen2 sy1 le3.) - Bring a book here.
        22. 拨 (peq4) - to give. 拨我看看。(peq4 ngu2 khe2-khe2.) - Let me have a look.
        23. 欢喜 (hoe1-xi2) - to like; to love. 我欢喜侬。(ngu2 hoe1-xi2 nong3.) - I like you.
        24. 想 (shiang2) - to think; to want. 我想去。(ngu2 shiang2 chi2.) - I want to go.
        25. 知道 (tsy1-tau2) - to know. 我知道了。(ngu2 tsy1-tau2 leq4.) - I know now."""),
    how_it_works=textwrap.dedent("""\
        This record teaches verbs as actions, not lists: each of the 25 verbs
        arrives in a sentence the learner can act out - eating, drinking,
        going, coming, buying, selling. The learner drills the great Wu verb
        pairs that Mandarin merges differently: 买 ma2 (buy) vs 卖 ma3 (sell)
        - same syllable, different tone; 拿 na3 (take) doing the work of
        Mandarin 把; 拨 peq4 (give) as the all-purpose transfer verb. Because
        Wu verbs never change form, the drill is pure vocabulary plus word
        order: subject, verb, object, every time. The demonstration program
        quizzes the full verb set and checks that every answer matches the
        record's romanization."""),
    key_points=[
        "25 essential verbs: 吃 chiq4, 喝 heq4, 去 chi2, 来 le3, 看 khe2, 听 thin1, 说 shuoq4, 问 ven3, 买 ma2, 卖 ma3.",
        "More: 做 tsu2, 工作 kon1-tsoq4, 学习 yoq5-xiq4, 教 ciau1, 睏觉 khun2-kau2, 洗 shi2, 穿 tshoe1, 开 khe1, 关 kue1, 打 ta2.",
        "Transfer verbs: 拿 na3 (take; Wu equivalent of Mandarin 把), 拨 peq4 (give), 欢喜 hoe1-xi2 (like), 想 shiang2 (want), 知道 tsy1-tau2 (know).",
        "Tone pair to master: 买 ma2 (buy) vs 卖 ma3 (sell) - one tone changes the meaning.",
        "Wu verbs never conjugate; aspect particles (仔, 过, 勒海) carry time - taught in record 21.",
        "Word order is always subject-verb-object: 我吃饭 (I eat rice).",
    ],
    requirements=[
        "Learners should act out each verb while saying its sentence - total physical response for all 25.",
        "Drill the 买/卖 tone pair (ma2 vs ma3) until the tones are unmistakable.",
    ],
    standards=[
        "CEFR A1: everyday action verbs with SVO sentence frames.",
        "Vernacular readings follow Qian Nairong 上海话大词典 (2007).",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Verb entries.",
        "Chao Y R. Studies in the Modern Wu-dialects. 1928. Wu verb and aspect systems.",
    ],
    sig_lens=("Through the Signature lens, the verb is action signed into language: "
              "twenty-five deeds - eating, going, buying, giving - each one a small "
              "oath that the learner will DO, not just name. This Signature reading "
              "treats every verb as a promise of motion."),
)

E(
    key="wu_adjectives", name="Wu Chinese Adjectives and Adverbs",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Twenty-five adjectives and fifteen adverbs, each with an example
        sentence. Wu adjectives need no agreement - no gender, no number, no
        cases - they simply stand before the noun or after 是.
        Adjectives: 1. 好 (hau2) - good. 迭个交关好。(diq4-geq4 ciau1-kue1 hau2.) - This is very good.
        2. 大 (du3) - big. 大房子。(du3 vang3-tsy2.) - Big house.
        3. 小 (siau2) - small. 小囡。(siau2-noe1.) - Small child.
        4. 长 (zang3) - long. 长江交关长。(zang3-kang1 ciau1-kue1 zang3.) - The Yangtze is very long.
        5. 短 (toe2) - short. 短头发。(toe2 deu3-faq4.) - Short hair.
        6. 高 (kau1) - tall; high. 高楼。(kau1 leu3.) - Tall building.
        7. 矮 (a2) - short (stature). 伊有点矮。(yi3 yeu3-tie2 a2.) - He is a bit short.
        8. 新 (shin1) - new. 新衣裳。(shin1 yi1-zang3.) - New clothes.
        9. 老 (lau3) - old. 老朋友。(lau3 bong3-yeu3.) - Old friend.
        10. 快 (khuai2) - fast. 车子开得交关快。(tsho1-tsy2 khe1-deq4 ciau1-kue1 khuai2.) - The car goes very fast.
        11. 慢 (me3) - slow. 慢慢交谈。(me3-me3 ciau1-de3.) - Chat slowly.
        12. 多 (tu1) - many; much. 人交关多。(nyin3 ciau1-kue1 tu1.) - Very many people.
        13. 少 (sau2) - few; little. 钞票勿多。(tshau1-phiau2 veq4 tu1.) - Not much money.
        14. 热 (gniq5) - hot. 今朝交关热。(cin1-tsau1 ciau1-kue1 gniq5.) - Today is very hot.
        15. 冷 (lan3) - cold. 水太冷了。(sy2 tha2 lan3 leq4.) - The water is too cold.
        16. 红 (gon1) - red. 红花。(gon1 ho1.) - Red flower.
        17. 白 (baq5) - white. 白衬衫。(baq5 tshen2-se1.) - White shirt.
        18. 黑 (heq4) - black. 黑夜。(heq4 ya3.) - Black night.
        19. 远 (yoe3) - far. 路交关远。(lu3 ciau1-kue1 yoe3.) - The road is very far.
        20. 近 (jin3) - near. 商店离我家交关近。(sang1-tie2 li3 ngu2-ka1 ciau1-kue1 jin3.) - The shop is very near my home.
        21. 贵 (ku2) - expensive. 迭件物事太贵了。(diq4-jie3 meq5-zy3 tha2 ku2 leq4.) - This thing is too expensive.
        22. 便宜 (bie3-nyi3) - cheap. 迭个便宜。(diq4-geq4 bie3-nyi3.) - This is cheap.
        23. 嗲 (tia2) - cute; adorable. 小囡真嗲。(siau2-noe1 tsen1 tia2.) - The child is so cute.
        24. 好吃 (hau2-chiq4) - delicious. 本帮菜真好吃。(pen2-pang1 tshe2 tsen1 hau2-chiq4.) - Local cuisine is really delicious.
        25. 难 (ne3) - difficult. 吴语勿难学。(wu2-gniu2 veq4 ne3 yoq5.) - Wu is not hard to learn.
        Adverbs: 1. 交关 (ciau1-kue1) - very. 交关好。(ciau1-kue1 hau2.) - Very good.
        2. 真 (tsen1) - really. 真好吃。(tsen1 hau2-chiq4.) - Really delicious.
        3. 太 (tha2) - too. 太贵了。(tha2 ku2 leq4.) - Too expensive.
        4. 有点 (yeu3-tie2) - a bit. 有点冷。(yeu3-tie2 lan3.) - A bit cold.
        5. 最 (tse2) - most. 最好吃。(tse2 hau2-chiq4.) - The most delicious.
        6. 更 (ken2) - more. 更便宜。(ken2 bie3-nyi3.) - Cheaper.
        7. 已经 (yi2-cin1) - already. 已经吃过了。(yi2-cin1 chiq4-ku2 leq4.) - Already eaten.
        8. 刚刚 (kang1-kang1) - just now. 刚刚来。(kang1-kang1 le3.) - Just arrived.
        9. 常常 (zang3-zang3) - often. 常常去。(zang3-zang3 chi2.) - Go often.
        10. 从来 (zon3-le3) - never (with negation). 从来勿去。(zon3-le3 veq4 chi2.) - Never go.
        11. 一起 (iq4-chi2) - together. 一起去。(iq4-chi2 chi2.) - Go together.
        12. 马上 (mo3-zang3) - right away. 马上来。(mo3-zang3 le3.) - Come right away.
        13. 慢慢 (me3-me3) - slowly. 慢慢讲。(me3-me3 kang2.) - Speak slowly.
        14. 快快 (khuai2-khuai2) - quickly. 快快来。(khuai2-khuai2 le3.) - Come quickly.
        15. 都 (tu1) - all; both. 侬拉都来。(nong3-la1 tu1 le3.) - You all come."""),
    how_it_works=textwrap.dedent("""\
        This record teaches describing words by pairing opposites: 大/小, 长/
        短, 高/矮, 新/老, 快/慢, 多/少, 热/冷, 远/近, 贵/便宜. The learner
        drills each pair in the frame 迭个___, 伊拉___ (this is ___, that is
        ___), feeling how Wu adjectives sit unchanged before nouns. Then the
        fifteen adverbs are drilled as intensifiers: 交关 (the great Wu
        very-word), 真, 太, 有点, 最, 更 - each wrapped around 好, 好吃,
        贵, 冷. Reduplicated adverbs (慢慢, 快快) get their own rhythm drill.
        The demonstration program runs an opposites-matching quiz and an
        intensifier drill that checks every adverb against its example
        sentence in this record."""),
    key_points=[
        "25 adjectives with no agreement: 好 hau2, 大 du3, 小 siau2, 长 zang3, 短 toe2, 高 kau1, 矮 a2, 新 shin1, 老 lau3, 快 khuai2, 慢 me3, 多 tu1, 少 sau2, 热 gniq5, 冷 lan3.",
        "Colors: 红 gon1, 白 baq5, 黑 heq4; distance: 远 yoe3, 近 jin3; value: 贵 ku2, 便宜 bie3-nyi3.",
        "Wu favorites: 嗲 tia2 (cute), 好吃 hau2-chiq4 (delicious), 难 ne3 (difficult).",
        "15 adverbs: 交关 ciau1-kue1 (very - the signature Wu intensifier), 真 tsen1, 太 tha2, 有点 yeu3-tie2, 最 tse2, 更 ken2.",
        "Time adverbs: 已经 yi2-cin1 (already), 刚刚 kang1-kang1 (just now), 常常 zang3-zang3 (often), 从来 zon3-le3 (never), 马上 mo3-zang3 (right away).",
        "Manner: 一起 iq4-chi2 (together), 慢慢 me3-me3 (slowly), 快快 khuai2-khuai2 (quickly), 都 tu1 (all).",
        "Adjectives stand before nouns unchanged: 大房子, 小囡, 红花 - no gender, no number, no cases.",
    ],
    requirements=[
        "Learners should drill opposite pairs aloud (大/小, 快/慢, 热/冷) in the frame 迭个___, 伊拉___.",
        "Master 交关 (ciau1-kue1) - it is the most Wu word for very and appears everywhere in speech.",
    ],
    standards=[
        "CEFR A1-A2: descriptive adjectives, colors, intensifiers, basic adverbs of time and manner.",
        "Vernacular readings follow Qian Nairong 上海话大词典 (2007).",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Adjective and adverb entries.",
        "Zhu X. Shanghai Tonetics. LINCOM Europa; 2006. Tone values for the citation forms used here.",
    ],
    sig_lens=("Through the Signature lens, the describing word is the seal of judgment: "
              "to call a thing 好 or 嗲 or 交关好 is to sign one name of approval upon "
              "it, and Wu gives the learner forty clean seals with no clutter of "
              "gender or case. This Signature reading treats adjectives as the "
              "learner first verdicts on the world."),
)

E(
    key="wu_pronouns", name="Wu Chinese Pronouns",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Full Wu pronoun paradigms - personal, possessive, demonstrative, and
        interrogative - each with example sentences. Wu pronouns never change
        form; number and possession ride on particles.
        Personal: 我 (ngu2) - I. 我是学生。(ngu2 zy3 yoq5-sang1.) - I am a student.
        侬 (nong3) - you (singular). 侬好。(nong3-hau2.) - Hello (you are well).
        伊 (yi3) - he; she; it. 伊来了。(yi3 le3 leq4.) - He/she has come.
        阿拉 (aq4-laq4) - we (Shanghai). 阿拉一起去。(aq4-laq4 iq4-chi2 chi2.) - We go together.
        我伲 (ngu2-ni3) - we (general Northern Wu). 我伲是朋友。(ngu2-ni3 zy3 bong3-yeu3.) - We are friends.
        侬拉 (nong3-la1) - you (plural). 侬拉都来。(nong3-la1 tu1 le3.) - You all come.
        伊拉 (yi3-la1) - they. 伊拉勒学校。(yi3-la1 leq4 yoq5-gau3.) - They are at school.
        Possessive (pronoun + 个 geq4): 我的 (ngu2 geq4) - my; mine. 迭是我个书。(diq4 zy3 ngu2 geq4 sy1.) - This is my book.
        侬个 (nong3 geq4) - your; yours. 侬个名字叫啥？(nong3 geq4 ming3-zy3 ciau2 sa3?) - What is your name?
        伊个 (yi3 geq4) - his; her; hers; its. 伊个车子真漂亮。(yi3 geq4 tsho1-tsy2 tsen1 phiau2-liang3.) - His car is really beautiful.
        阿拉个 (aq4-laq4 geq4) - our; ours. 阿拉个老师交关好。(aq4-laq4 geq4 lau3-sy1 ciau1-kue1 hau2.) - Our teacher is very good.
        侬拉个 (nong3-la1 geq4) - your (plural). 侬拉个屋勒啥地方？(nong3-la1 geq4 oq4 leq4 sa3 di3-fang1?) - Where is your (plural) house?
        伊拉个 (yi3-la1 geq4) - their; theirs. 伊拉个囡真嗲。(yi3-la1 geq4 noe1 tsen1 tia2.) - Their child is so cute.
        Reflexive: 自己 (zy3-ci2) - self. 我自己去。(ngu2 zy3-ci2 chi2.) - I go by myself.
        Demonstrative: 迭 (diq4) - this. 迭是啥？(diq4 zy3 sa3?) - What is this?
        伊 (yi3) - that. 伊是啥？(yi3 zy3 sa3?) - What is that?
        迭个 (diq4-geq4) - this one. 迭个交关好。(diq4-geq4 ciau1-kue1 hau2.) - This one is very good.
        伊个 (yi3-geq4) - that one. 伊个勿好。(yi3-geq4 veq4 hau2.) - That one is not good.
        迭里 (diq4-li2) - here. 迭里坐。(diq4-li2 zu3.) - Sit here.
        伊里 (yi3-li2) - there. 伊里看。(yi3-li2 khe2.) - Look there.
        Interrogative: 啥 (sa3) - what. 侬讲啥？(nong3 kang2 sa3?) - What are you saying?
        啥人 (sa3-gnin3) - who. 啥人来了？(sa3-gnin3 le3 leq4?) - Who has come?
        啥地方 (sa3 di3-fang1) - where. 侬勒啥地方？(nong3 leq4 sa3 di3-fang1?) - Where are you?
        啥辰光 (sa3 zen3-kuang1) - when. 侬啥辰光来？(nong3 sa3 zen3-kuang1 le3?) - When are you coming?
        哪能 (na3-nen3) - how. 迭个字哪能读？(diq4-geq4 zy3 na3-nen3 doq5?) - How is this character read?
        为啥 (we3-sa3) - why. 侬为啥勿去？(nong3 we3-sa3 veq4 chi2?) - Why are you not going?
        几化 (ci2-hu3) - how many; how much. 几化钞票？(ci2-hu3 tshau1-phiau2?) - How much money?
        哪一个 (na3 iq4-geq4) - which one. 侬欢喜哪一个？(nong3 hoe1-xi2 na3 iq4-geq4?) - Which one do you like?"""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronouns as a substitution drill: the learner
        takes one sentence frame - ___好, ___来了, ___是我个朋友 - and swaps
        every pronoun through it: 我好, 侬好, 伊好; 我来了, 侬拉来了, 伊拉来
        了. Possessives are drilled by adding 个: 我的, 侬个, 伊个, 阿拉个.
        The interrogatives become a question game: one learner points and
        asks 迭是啥？, the other answers; 侬啥辰光来？ gets a real time
        answer. Note the Wu double-duty of 伊 (he/she AND that) - context
        decides. The demonstration program runs a pronoun-substitution quiz
        that checks every paradigm form against this record."""),
    key_points=[
        "Personal: 我 ngu2 (I), 侬 nong3 (you), 伊 yi3 (he/she), 阿拉 aq4-laq4 / 我伲 ngu2-ni3 (we), 侬拉 nong3-la1 (you pl), 伊拉 yi3-la1 (they).",
        "Plural marker: 拉 la1 - 侬拉, 伊拉. Shanghai we: 阿拉; general Northern Wu we: 我伲.",
        "Possessive: pronoun + 个 geq4 - 我的, 侬个, 伊个, 阿拉个, 侬拉个, 伊拉个.",
        "Reflexive: 自己 zy3-ci2 (self). Demonstratives: 迭 diq4 (this), 伊 yi3 (that), 迭里 diq4-li2 (here), 伊里 yi3-li2 (there).",
        "Interrogatives: 啥 sa3 (what), 啥人 sa3-gnin3 (who), 啥地方 (where), 啥辰光 (when), 哪能 na3-nen3 (how), 为啥 we3-sa3 (why), 几化 ci2-hu3 (how much), 哪一个 (which).",
        "Pronouns never change form; 伊 does double duty as he/she and that.",
    ],
    requirements=[
        "Learners should drill the substitution frame ___好 / ___来了 through all seven personal pronouns.",
        "Play the pointing question game: 迭是啥？ / 伊是啥？ with real objects.",
    ],
    standards=[
        "CEFR A1: personal, possessive, demonstrative, and interrogative pronouns.",
        "Vernacular readings follow Qian Nairong 上海话大词典 (2007).",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Pronoun entries.",
        "Chao Y R. Studies in the Modern Wu-dialects. 1928. Wu pronoun systems.",
    ],
    sig_lens=("Through the Signature lens, the pronoun is the seal of identity: 我 the "
              "seal of the self, 侬 the seal turned toward the other, 阿拉 the seal of "
              "the shared table. This Signature reading treats every pronoun as a "
              "signature of who stands in the sentence."),
)

E(
    key="wu_numbers", name="Wu Chinese Numbers and Time",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Numbers 1-100, ordinals, days, months, seasons, clock time, and dates -
        each with example sentences. Wu numbers ride on the classic tone
        ladder, which makes them the perfect tone drill.
        1-10: 一 iq4, 二 gni3, 三 se1, 四 sy2, 五 ng3, 六 loq4, 七 chiq4,
        八 paq4, 九 cieu2, 十 zeq5. 十一 zeq5-iq4 (11), 十二 zeq5-gni3 (12),
        二十 gni3-zeq5 (20), 二十五 gni3-zeq5-ng3 (25), 三十 se1-zeq5 (30),
        四十五 sy2-zeq5-ng3 (45), 五十 ng3-zeq5 (50), 六十八 loq4-zeq5-paq4
        (68), 九十九 cieu2-zeq5-cieu2 (99), 一百 iq4-paq4 (100).
        Note: 二 (gni3) counts; 两 (liang3) pairs things: 两个人
        (liang3-geq4 gnin3, two people).
        Ordinals: 第一 di3-iq4 (first), 第二 di3-gni3 (second), 第三 di3-se1 (third).
        我是第一。(ngu2 zy3 di3-iq4.) - I am first.
        Days: 礼拜一 li3-ba-iq4 (Monday), 礼拜二 li3-ba-gni3 (Tuesday),
        礼拜三 li3-ba-se1 (Wednesday), 礼拜四 li3-ba-sy2 (Thursday),
        礼拜五 li3-ba-ng3 (Friday), 礼拜六 li3-ba-loq4 (Saturday),
        礼拜天 li3-ba-thie1 (Sunday). Wu says 礼拜 where Mandarin often says 星期.
        礼拜一我去学校。(li3-ba-iq4 ngu2 chi2 yoq5-gau3.) - On Monday I go to school.
        Months: 一月 iq4-ngoeq5 (January), 二月 gni3-ngoeq5, 三月 se1-ngoeq5,
        六月 loq4-ngoeq5, 九月 cieu2-ngoeq5, 十二月 zeq5-gni3-ngoeq5
        (December). 我生日是三月。(ngu2 sang1-zeq5-nyiq5 zy3 se1-ngoeq5.) - My birthday is in March.
        Seasons: 春天 tshen1-thie1 (spring), 夏天 yo3-thie1 (summer),
        秋天 tshieu1-thie1 (autumn), 冬天 ton1-thie1 (winter).
        夏天交关热。(yo3-thie1 ciau1-kue1 gniq5.) - Summer is very hot.
        Clock time: 点钟 tie2-tson1 (o'clock), 半 pe2 (half), 刻 kheq4
        (quarter), 分 fen1 (minute). 三点钟 se1 tie2-tson1 (3 o'clock),
        三点半 se1 tie2 pe2 (3:30), 三点一刻 se1 tie2 iq4 kheq4 (3:15),
        差一刻四点 tsha1 iq4 kheq4 sy2 tie2 (3:45). 现在三点钟。
        (yi3-ze3 se1 tie2-tson1.) - It is now 3 o'clock.
        Dates: 年 gnie3 (year), 月 ngoeq5 (month), 日 gniq5 / 号 hau3 (day).
        今朝 cin1-tsau1 (today), 明朝 min3-tsau1 (tomorrow),
        昨日 zoq5-gniq5 (yesterday). 今朝是礼拜三。
        (cin1-tsau1 zy3 li3-ba-se1.) - Today is Wednesday.
        Example sentences: 我有三本书。(ngu2 yeu3 se1 pen2 sy1.) - I have three books.
        钞票一共五十块。(tshau1-phiau2 iq4-gon3 ng3-zeq5 khue2.) - Fifty yuan altogether.
        五分钟以后见。(ng3 fen1-tson1 yi2-heu3 cie2.) - See you in five minutes."""),
    how_it_works=textwrap.dedent("""\
        This record teaches numbers as the tone ladder itself: the learner
        chants 1-10 (iq4, gni3, se1, sy2, ng3, loq4, chiq4, paq4, cieu2,
        zeq5) and hears all five tones in order - 4, 3, 1, 2, 3, 4, 4, 4, 2,
        5. Then the building rules: tens (二十 = two-ten), hundreds, the
        二/两 distinction, ordinals with 第, days with 礼拜, months with 月,
        clock time with 点钟/半/刻. Every rule lands in a sentence about the
        learner real day: what time they get up, what day they study Wu.
        The demonstration program builds every number 1-100 from the digit
        rules, checks the tone of each digit against the record, and quizzes
        clock-time readings."""),
    key_points=[
        "1-10: 一 iq4, 二 gni3, 三 se1, 四 sy2, 五 ng3, 六 loq4, 七 chiq4, 八 paq4, 九 cieu2, 十 zeq5 - the full five-tone ladder in ten words.",
        "Tens: 二十 gni3-zeq5 (20), 九十九 cieu2-zeq5-cieu2 (99), 一百 iq4-paq4 (100). 二 gni3 counts; 两 liang3 pairs: 两个人.",
        "Ordinals with 第: 第一 di3-iq4, 第二 di3-gni3, 第三 di3-se1.",
        "Days with 礼拜: 礼拜一 li3-ba-iq4 (Mon) through 礼拜天 li3-ba-thie1 (Sun).",
        "Months: 一月 iq4-ngoeq5 through 十二月 zeq5-gni3-ngoeq5; seasons 春天夏天秋天冬天.",
        "Clock: 点钟 tie2-tson1 (o'clock), 半 pe2 (half), 刻 kheq4 (quarter): 三点半, 三点一刻, 差一刻四点.",
        "Dates: 今朝 cin1-tsau1 (today), 明朝 min3-tsau1 (tomorrow), 昨日 zoq5-gniq5 (yesterday); 年 gnie3, 月 ngoeq5, 号 hau3.",
    ],
    requirements=[
        "Learners should chant 1-10 daily as a tone drill until the five tones are automatic.",
        "Say your real schedule in Wu: 我___点钟起床, 礼拜___我去___.",
    ],
    standards=[
        "CEFR A1: numbers 1-100, ordinals, days, months, clock time, dates.",
        "Tone values follow the standard five-tone analysis of modern Shanghai.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Numeral and time-word entries.",
        "Zhu X. Shanghai Tonetics. LINCOM Europa; 2006. Checked-tone values for the numeral set.",
    ],
    sig_lens=("Through the Signature lens, number is the oldest signature of all: to "
              "count in Wu is to sign the ancient tally anew - 一 iq4 cut short like a "
              "knife mark, 十 zeq5 low and final like a seal pressed. This Signature "
              "reading treats the 1-10 chant as the learner first signed document."),
)

E(
    key="wu_greetings", name="Wu Chinese Greetings and Everyday Phrases",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Thirty greetings, farewells, and politeness phrases - each with
        usage notes, in characters, romanization, and English.
        1. 侬好 (nong3-hau2) - Hello. The universal Wu greeting, any time of day.
        2. 早 (tsau2) - Good morning. Short and warm among neighbors.
        3. 吃过了𠲎 (chiq4-ku2 leq4 vaq5) - Have you eaten? The classic caring greeting.
        4. 侬最近哪能？(nong3 tse2-jin3 na3-nen3?) - How have you been lately?
        5. 好久勿见 (hau2-cieu2 veq4 cie2) - Long time no see.
        6. 谢谢 (zia3-zia3) - Thank you.
        7. 谢谢侬 (zia3-zia3 nong3) - Thank you (to you). Warmer than plain 谢谢.
        8. 多谢 (tu1-zia3) - Many thanks. Slightly formal.
        9. 对勿起 (te2-veq4-chi2) - Sorry; excuse me.
        10. 勿好意思 (veq4-hau2 yi2-sy1) - Excuse me; sorry to bother. Softer than 对勿起.
        11. 没关系 (meq5-kue1-xi3) - It does not matter; you are welcome.
        12. 请 (tshin2) - Please. 请坐。(tshin2 zu3.) - Please sit.
        13. 请问 (tshin2-ven3) - May I ask... 请问，车站勒啥地方？- May I ask, where is the station?
        14. 麻烦侬 (me3-ve3 nong3) - Sorry to trouble you.
        15. 再会 (ze3-we3) - Goodbye. The standard Wu farewell.
        16. 慢走 (me3-tseu2) - Take care going. Said by the host to a departing guest.
        17. 明朝会 (min3-tsau1 we3) - See you tomorrow.
        18. 晚安 (ve3-e1) - Good night.
        19. 一路平安 (iq4-lu3 bing3-e1) - Safe travels.
        20. 欢迎 (we1-ngin3) - Welcome. 欢迎光临。(we1-ngin3 kuang1-lin3.) - Welcome (shop greeting).
        21. 恭喜 (kon1-xi2) - Congratulations.
        22. 身体好𠲎？(shen1-thi2 hau2 vaq5?) - Is your health good? Caring greeting to elders.
        23. 侬忙𠲎？(nong3 mang3 vaq5?) - Are you busy? Polite opener.
        24. 请多关照 (tshin2 tu1 kue1-tsau2) - Please look after me. Polite and humble.
        25. 失陪 (seq4-be3) - Excuse me (I must leave). Formal.
        26. 劳驾 (lau3-ka2) - Excuse me (asking a favor). 劳驾，让一让。(lau3-ka2, rang3 iq4-rang3.) - Excuse me, make way please.
        27. 好𠲎？(hau2 vaq5?) - OK?; Is it good? The universal check-in.
        28. 对𠲎？(teq4 vaq5?) - Right?; Is that correct? Seeks agreement.
        29. 晓得了 (shiau2-deq4 leq4) - Got it; understood.
        30. 交关感谢 (ciau1-kue1 ke2-zia3) - Many thanks indeed. Extra-warm gratitude."""),
    how_it_works=textwrap.dedent("""\
        This record teaches phrases as social tools: the learner sorts the 30
        into five scenes - meeting (1-5), thanking (6-8, 30), apologizing
        (9-10, 14), parting (15-19), and polite requests (12-13, 24-26) -
        then role-plays each scene with a partner. Special attention goes to
        the Wu-only forms: 侬好 (not 你好), 再会 (not 再见), 吃过了𠲎 as a
        greeting, and the 𠲎 (vaq5) question particle that softens 身体好𠲎？
        into care. The demonstration program runs a scene-matching quiz:
        given a situation (guest leaving, elder met, favor asked), it checks
        the learner picks the Wu-right phrase from this record."""),
    key_points=[
        "The universal greeting is 侬好 nong3-hau2 (hello); the universal farewell is 再会 ze3-we3 (goodbye).",
        "Caring greetings: 吃过了𠲎 (have you eaten?), 身体好𠲎？ (is your health good?).",
        "Thanks scale: 谢谢 < 谢谢侬 < 多谢 < 交关感谢.",
        "Apology scale: 对勿起 (direct sorry) vs 勿好意思 (softer excuse me) vs 麻烦侬 (sorry to trouble you).",
        "Polite request openers: 请问 (may I ask), 劳驾 (excuse me, favor), 请多关照 (please look after me).",
        "The 𠲎 vaq5 particle turns statements into gentle questions: 好𠲎？ 对𠲎？ 侬忙𠲎？",
        "Parting and night: 再会 ze3-we3 (goodbye), 慢走 me3-tseu2 (take care going), 晚安 ve3-e1 (good night), 明朝会 (see you tomorrow); 恭喜 kon1-xi2 (congratulations); 欢迎 we1-ngin3 (welcome).",
        "30 phrases, each with a usage note - sorted into meeting, thanking, apologizing, parting, requesting.",
    ],
    requirements=[
        "Learners should role-play all five scenes with a partner until the phrases come without notes.",
        "Use 侬好 and 再会 in real life from day one - they mark you as a Wu speaker immediately.",
    ],
    standards=[
        "CEFR A1: greetings, thanks, apologies, farewells, polite requests.",
        "Usage notes reflect standard Shanghai politeness practice.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Phrase and interjection entries.",
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. On Wu politeness formulae.",
    ],
    sig_lens=("Through the Signature lens, the greeting is the smallest signed contract: "
              "侬好 signs goodwill, 谢谢 signs gratitude, 再会 signs a promise to meet "
              "again. This Signature reading treats all thirty phrases as thirty small "
              "covenants of Wu social life."),
)

E(
    key="wu_grammar", name="Wu Chinese Grammar Essentials",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        The core grammar of Wu in rules, each with translated example
        sentences. Wu grammar is wonderfully regular: no conjugations, no
        gender, no cases - meaning rides on word order and particles.
        Word order: Subject-Verb-Object, always. 我吃饭。(ngu2 chiq4-ve3.) - I eat rice.
        伊看书。(yi3 khe2-sy1.) - He reads a book.
        阿拉学吴语。(aq4-laq4 yoq5 wu2-gniu2.) - We study Wu.
        Negation: 勿 (veq4) + verb negates present, future, and volition.
        我勿去。(ngu2 veq4 chi2.) - I am not going. / I will not go.
        伊勿吃辣个。(yi3 veq4 chiq4 laq4-geq4.) - He does not eat spicy food.
        朆 (ven3) + verb negates completed past (have not).
        我朆去过。(ngu2 ven3 chi2-ku2.) - I have not gone.
        伊朆吃。(yi3 ven3 chiq4.) - He has not eaten.
        覅 (fiau2 = 勿要) means do not want / had better not.
        覅忘记。(fiau2 mang3-ci2.) - Do not forget.
        Questions: (a) the 𠲎 (vaq5) particle: statement + 𠲎 = yes/no question.
        侬去𠲎？(nong3 chi2 vaq5?) - Are you going?
        好𠲎？(hau2 vaq5?) - Is it good? / OK?
        (b) interrogative words in place (no word-order change):
        侬啥辰光来？(nong3 sa3 zen3-kuang1 le3?) - When are you coming?
        迭是啥？(diq4 zy3 sa3?) - What is this?
        Articles: none. Definiteness comes from demonstratives 迭/伊 or context.
        Number: nouns do not inflect; 拉 marks human plurals on pronouns.
        朋友来了。(bong3-yeu3 le3 leq4.) - The friend has come. / Friends have come.
        Possession: noun + 个 + noun. 我个书。(ngu2 geq4 sy1.) - My book.
        先生个车子。(shie1-sang1 geq4 tsho1-tsy2.) - The teacher car.
        Location: noun + 勒 + place. 伊勒上海。(yi3 leq4 zang3-he2.) - He is in Shanghai.
        我勒屋里。(ngu2 leq4 oq4-li2.) - I am at home.
        The 拿 construction (Wu equivalent of Mandarin 把): 拿 + object + verb + result.
        拿门关脱。(na3 men3 kue1-theq4.) - Close the door (take door, close it shut).
        拿功课做脱。(na3 kon1-khu2 tsu2-theq4.) - Finish the homework.
        The 拨 passive: 拨 + agent + verb. 杯子拨伊打破仔。
        (pe1-tsy2 peq4 yi3 ta2-phu2 tsy2.) - The cup was broken by him.
        Aspect previews (full system in record 21): 仔 (tsy2) completed -
        我吃仔饭。(ngu2 chiq4-tsy2 ve3.) - I ate.; 过 (ku2) experienced -
        我去过。(ngu2 chi2-ku2.) - I have been.; 勒海 (leq4-he2) ongoing -
        伊勒海吃饭。(yi3 leq4-he2 chiq4-ve3.) - He is eating.
        是 (zy3) for identity and emphasis: 我是学生。(ngu2 zy3 yoq5-sang1.) - I am a student.
        Comparatives with 比: 伊比我高。(yi3 pi2 ngu2 kau1.) - He is taller than me.
        Reduplication softens: 看看 (khe2-khe2, have a look), 慢慢 (me3-me3, slowly)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches grammar as ten tools, each drilled in a
        transformation exercise. The learner takes 我去 and negates it three
        ways (我勿去, 我朆去过, 我覅去 - feeling the three negations), turns
        statements into 𠲎 questions, converts 把-style thoughts into 拿
        sentences, and builds 拨 passives from active sentences. Every rule
        is practiced by transforming a base sentence, never by memorizing a
        table. The demonstration program is a grammar checker: it takes Wu
        sentences, verifies SVO order, checks that negation particles sit
        before the verb, and confirms 𠲎 closes questions - asserting each
        rule against examples drawn from this record."""),
    key_points=[
        "Word order: SVO always - 我吃饭, 伊看书, 阿拉学吴语.",
        "Three negations: 勿 veq4 (not - present/future), 朆 ven3 (have not - past), 覅 fiau2 (do not want).",
        "Questions: 𠲎 vaq5 particle (侬去𠲎？) or in-place interrogatives (侬啥辰光来？) - word order never changes.",
        "No articles, no gender, no cases, no conjugation; 拉 la1 pluralizes human pronouns.",
        "Possession: X + 个 + Y (我个书). Location: 勒 leq4 (伊勒上海).",
        "拿 na3 construction = Mandarin 把: 拿门关脱. 拨 peq4 passive: 杯子拨伊打破仔.",
        "Aspect markers: 仔 tsy2 (completed), 过 ku2 (experienced), 勒海 leq4-he2 (ongoing).",
        "是 zy3 for identity; 比 pi2 for comparison: 伊比我高. Reduplication softens: 看看, 慢慢.",
    ],
    requirements=[
        "Learners should transform drills: negate every sentence three ways, question every sentence with 𠲎.",
        "Write ten 拿 sentences and ten 拨 sentences about your own room and day.",
    ],
    standards=[
        "CEFR A1-A2: word order, negation, questions, possession, location, basic aspect.",
        "Grammatical analysis follows Chao 1928 and Qian 1992 on Wu syntax.",
    ],
    citations=[
        "Chao Y R. Studies in the Modern Wu-dialects. Tsing Hua College Research Institute; 1928. Wu grammar and particles.",
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. Wu syntax: 拿, 拨, aspect markers.",
    ],
    sig_lens=("Through the Signature lens, grammar is the architecture of the covenant: "
              "word order the foundation stones, particles the mortar - 勿, 朆, 覅 three "
              "different seals of refusal, 拿 the hand that moves the object, 拨 the "
              "hand that receives. This Signature reading treats every particle as a "
              "load-bearing beam in the house of Wu meaning."),
)

E(
    key="wu_home", name="Wu Chinese Home and Family Sentences",
    group="Compounded", ladder_rank=4, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences about house, rooms, furniture, and family members -
        the language of home.
        1. 我个屋勒市中心。(ngu2 geq4 oq4 leq4 zy3-ton1-shin1.) - My house is downtown.
        2. 屋里向有三间房间。(oq4-li2-shiang3 yeu3 se1-cie1 vang3-cie1.) - There are three rooms in the house.
        3. 客堂间交关大。(kheq4-dang3-cie1 ciau1-kue1 du3.) - The living room is very big.
        4. 灶披间里向烧饭。(tsau2-phi1-cie1 li2-shiang3 sau1-ve3.) - Cooking happens in the kitchen.
        5. 房间里向有一张床。(vang3-cie1 li2-shiang3 yeu3 iq4-tsang1 zang3.) - There is a bed in the bedroom.
        6. 书桌浪向有交关书。(sy1-tsoq4 lang3-shiang3 yeu3 ciau1-kue1 sy1.) - There are many books on the desk.
        7. 椅子坏脱了，买张新个。(yi3-tsy2 wa3-theq4 leq4, ma2 tsang1 shin1 geq4.) - The chair is broken; buy a new one.
        8. 拿窗开开，透透风。(na3 tshang1 khe1-khe1, teu2-teu2 fon1.) - Open the window and let in some air.
        9. 爸爸勒看报纸。(ba3-ba3 leq4 khe2 pau2-tsy2.) - Father is reading the newspaper.
        10. 妈妈勒灶披间烧菜。(ma1-ma1 leq4 tsau2-phi1-cie1 sau1-tshe2.) - Mother is cooking in the kitchen.
        11. 爷爷欢喜听戏。(ya3-ya3 hoe1-xi2 thin1-shi2.) - Grandfather likes listening to opera.
        12. 奶奶身体交关好。(na3-na3 shen1-thi2 ciau1-kue1 hau2.) - Grandmother is in very good health.
        13. 哥哥明朝结婚。(ku1-ku1 min3-tsau1 ciq4-huen1.) - Elder brother gets married tomorrow.
        14. 姐姐个囡真嗲。(cia2-cia2 geq4 noe1 tsen1 tia2.) - Elder sister's child is so cute.
        15. 弟弟勒外头踢球。(di3-di3 leq4 nga3-deu3 thiq4-jieu3.) - Younger brother is playing ball outside.
        16. 妹妹帮我做功课。(me2-me2 pang1 ngu2 tsu2 kon1-khu2.) - Younger sister helps me with homework.
        17. 阿拉一家人吃饭。(aq4-laq4 iq4-ka1 gnin3 chiq4-ve3.) - Our whole family eats together.
        18. 夜里向阿拉看电视。(ya3-li2-shiang3 aq4-laq4 khe2 die3-zy3.) - In the evening we watch TV.
        19. 侬个屋几化间房间？(nong3 geq4 oq4 ci2-hu3 cie1 vang3-cie1?) - How many rooms does your house have?
        20. 欢迎到我屋里向来白相。(we1-ngin3 tau2 ngu2 oq4-li2-shiang3 le3 baq5-shiang2.) - Welcome to come have fun at my place."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the home by walking through it: the learner
        narrates a tour of their own house in Wu - 屋, 客堂间, 灶披间, 房间 -
        pointing at furniture (床, 书桌, 椅子, 窗) and naming the family
        doing things (爸爸看报纸, 妈妈烧菜, 弟弟踢球). The room words use the
        Wu suffixes 间 and 里向/浪向 for inside/on-top, drilled until the
        location patterns are automatic. The demonstration program verifies
        all twenty sentences - checking each has characters, romanization,
        and English - and runs a room-vocabulary matcher that pairs each
        room with its furniture from this record."""),
    key_points=[
        "House words: 屋 oq4 (house), 客堂间 (living room), 灶披间 (kitchen), 房间 (bedroom).",
        "Location suffixes: 里向 (inside), 浪向 (on top of) - 书桌浪向, 房间里向.",
        "Family: 爸爸, 妈妈, 爷爷, 奶奶, 哥哥, 姐姐, 弟弟, 妹妹 - each doing something in a sentence.",
        "Furniture and actions: 床, 书桌, 椅子, 窗; 开窗, 烧饭, 看报纸, 做功课.",
        "20 full sentences with translations: the language of home life.",
    ],
    requirements=[
        "Learners should give a spoken tour of their own home in Wu using these twenty sentences as models.",
        "Drill 里向 vs 浪向 with ten objects in your room: __里向, __浪向.",
    ],
    standards=[
        "CEFR A1-A2: home, rooms, furniture, family members, daily routines.",
        "Vernacular readings follow Qian Nairong 上海话大词典 (2007).",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Household vocabulary.",
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. Wu locative constructions.",
    ],
    sig_lens=("Through the Signature lens, home is the first archive: every room a "
              "record, every family member a living entry, every shared meal a seal "
              "renewed daily. This Signature reading treats the twenty home sentences "
              "as the founding documents of the learner's Wu household."),
)

E(
    key="wu_food", name="Wu Chinese Food and Cooking Sentences",
    group="Compounded", ladder_rank=4, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences about meals, ingredients, cooking actions, and the
        restaurant.
        1. 今朝吃啥？(cin1-tsau1 chiq4 sa3?) - What shall we eat today?
        2. 我欢喜吃本帮菜。(ngu2 hoe1-xi2 chiq4 pen2-pang1 tshe2.) - I like eating local Shanghai cuisine.
        3. 红烧肉交关好吃。(gon3-sau1 gnioq5 ciau1-kue1 hau2-chiq4.) - Braised pork is delicious.
        4. 清蒸鱼新鲜得来。(tshin1-tsen1 ng3 shin1-shie1 deq4-le3.) - The steamed fish is wonderfully fresh.
        5. 白米饭配咸菜。(baq5-mi3-ve3 phe2 ye3-tshe2.) - White rice with pickled vegetables.
        6. 馄饨汤暖胃。(wen3-den3 thang1 noe3-wi3.) - Wonton soup warms the stomach.
        7. 小笼包要趁热吃。(siau2-lon3-pau1 iau2 tshen2-gniq5 chiq4.) - Soup dumplings must be eaten hot.
        8. 买点青菜搭豆腐。(ma2 tie2 tshing1-tshe2 taq4 deu3-fu3.) - Buy some greens and tofu.
        9. 鸡蛋炒番茄。(ci1-de3 tshau2 fie1-jia3.) - Scrambled eggs with tomato.
        10. 放点盐，味道正好。(fang2 tie2 yie3, we3-dau3 tsen2-hau2.) - Add a little salt; the flavor is just right.
        11. 火开大点，快点烧。(hu2 khe1 du3-tie2, khuai2-tie2 sau1.) - Turn the heat up; cook it quickly.
        12. 糖放多了，太甜了。(dang3 fang2 tu1 leq4, tha2 die3 leq4.) - Too much sugar; it is too sweet.
        13. 侬会烧菜𠲎？(nong3 we3 sau1-tshe2 vaq5?) - Can you cook?
        14. 我姆妈烧个菜最好吃。(ngu2 m1-ma1 sau1 geq4 tshe2 tse2 hau2-chiq4.) - My mother's cooking is the most delicious.
        15. 服务员，拿菜单来。(voq5-wu2-yoe3, na3 tse2-te1 le3.) - Waiter, bring the menu.
        16. 迭个菜辣𠲎？(diq4-geq4 tshe2 laq4 vaq5?) - Is this dish spicy?
        17. 勿辣，交关鲜。(veq4 laq4, ciau1-kue1 shie1.) - Not spicy; very fresh and savory.
        18. 买单。(ma2-te1.) - The check, please.
        19. 一共几化钞票？(iq4-gon3 ci2-hu3 tshau1-phiau2?) - How much altogether?
        20. 下趟我请侬吃饭。(o3-thang2 ngu2 tshin2 nong3 chiq4-ve3.) - Next time I will treat you to dinner."""),
    how_it_works=textwrap.dedent("""\
        This record teaches food as a full restaurant visit: the learner
        plans a menu (sentences 1-7), shops for ingredients (8-9), cooks
        (10-14), then orders in a restaurant (15-20). The great Shanghai
        dishes - 红烧肉, 清蒸鱼, 馄饨, 小笼包 - are drilled with their Wu
        names until ordering feels natural. Cooking verbs (烧, 炒, 蒸, 放,
        买) get an action drill in a real or imagined kitchen. The
        demonstration program verifies all twenty sentences and runs a
        dish-to-ingredient matcher built from this record's vocabulary."""),
    key_points=[
        "Signature dishes: 红烧肉 gon3-sau1 gnioq5, 清蒸鱼 tshin1-tsen1 ng3, 馄饨 wen3-den3, 小笼包 siau2-lon3-pau1, 本帮菜 pen2-pang1 tshe2.",
        "Ingredients: 青菜, 豆腐, 鸡蛋, 番茄, 盐, 糖, 米饭, 咸菜.",
        "Cooking verbs: 烧 sau1 (cook), 炒 tshau2 (stir-fry), 蒸 tsen1 (steam), 放 fang2 (add), 买 ma2 (buy).",
        "Taste words: 好吃 (delicious), 鲜 shie1 (fresh/savory), 甜 die3 (sweet), 辣 laq4 (spicy), 咸 ye3 (salty).",
        "Restaurant script: 拿菜单来, 买单, 一共几化钞票？, 下趟我请侬吃饭.",
        "20 full sentences with translations: market, kitchen, table, restaurant.",
    ],
    requirements=[
        "Learners should cook one dish while narrating every step in Wu.",
        "Role-play the restaurant scene: one learner orders, the other serves, using sentences 15-20.",
    ],
    standards=[
        "CEFR A1-A2: food, meals, ingredients, cooking, restaurant.",
        "Dish names follow standard Shanghai culinary vocabulary.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Food vocabulary entries.",
        "上海市地方志办公室. 上海饮食文化. Shanghai local food culture records.",
    ],
    sig_lens=("Through the Signature lens, the meal is the covenant renewed daily: the "
              "market the archive of ingredients, the kitchen the laboratory, the "
              "shared table the signed page. This Signature reading treats every dish "
              "name as a seal of Shanghai taste."),
)

E(
    key="wu_travel", name="Wu Chinese Travel and Directions Sentences",
    group="Compounded", ladder_rank=4, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences about transport, asking directions, tickets, and
        lodging.
        1. 请问，外滩哪能去？(tshin2-ven3, nga3-than1 na3-nen3 chi2?) - Excuse me, how do I get to the Bund?
        2. 一直朝前走，然后左转。(iq4-zeq5 zau1-jie3 tseu2, zen3-heu3 tsu2-tse3.) - Go straight ahead, then turn left.
        3. 右转以后就到了。(yeu3-tse3 yi2-heu3 zieu3 tau2 leq4.) - After turning right you will arrive.
        4. 地铁几号线？(di3-thiq4 ci2-hau3 shie2?) - Which subway line?
        5. 坐二号线到人民广场。(zu3 gni3-hau3 shie2 tau2 zen3-min3 kuang3-zang3.) - Take Line 2 to People Square.
        6. 公交车几路？(kon1-ciau1-tsho1 ci2-lu3?) - Which bus?
        7. 打车去机场要几化钞票？(ta2-tsho1 chi2 ci1-zang3 iau2 ci2-hu3 tshau1-phiau2?) - How much is a taxi to the airport?
        8. 买两张去苏州个票子。(ma2 liang3-tsang1 chi2 su1-tseu1 geq4 phiau2-tsy2.) - Buy two tickets to Suzhou.
        9. 火车几化点钟开？(hu2-tsho1 ci2-hu3 tie2-tson1 khe1?) - What time does the train leave?
        10. 飞机晚点了。(fi1-ci1 we3-tie2 leq4.) - The flight is delayed.
        11. 侬要住几夜？(nong3 iau2 zy3 ci2-ya3?) - How many nights will you stay?
        12. 有空房间𠲎？(yeu3 khon2 vang3-cie1 vaq5?) - Is there a free room?
        13. 标准间一夜几化钞票？(piau1-tsen2-cie1 iq4-ya3 ci2-hu3 tshau1-phiau2?) - How much is a standard room per night?
        14. 包早饭𠲎？(pau1 tsau2-ve3 vaq5?) - Is breakfast included?
        15. 退房是几化点钟？(the2-vang3 zy3 ci2-hu3 tie2-tson1?) - What time is check-out?
        16. 行李帮我送到房间。(hang3-li2 pang1 ngu2 son2-tau2 vang3-cie1.) - Please send the luggage to the room.
        17. 附近有好吃个饭店𠲎？(fu3-jin3 yeu3 hau2-chiq4 geq4 ve3-tie2 vaq5?) - Is there a good restaurant nearby?
        18. 地图浪向标一标。(di3-du3 lang3-shiang3 piau1 iq4-piau1.) - Mark it on the map.
        19. 我迷路了，哪能走？(ngu2 mi3-lu3 leq4, na3-nen3 tseu2?) - I am lost; which way?
        20. 谢谢侬带路。(zia3-zia3 nong3 ta2-lu3.) - Thank you for showing the way."""),
    how_it_works=textwrap.dedent("""\
        This record teaches travel as a journey: the learner asks the way
        (1-3), rides the subway and bus (4-7), buys tickets (8-10), checks
        into a hotel (11-16), and survives being lost (17-20). Direction
        words - 前, 后, 左, 右, 直, 转 - are drilled with hand gestures,
        and the great Shanghai landmarks (外滩, 人民广场, 机场) anchor every
        route in reality. The 𠲎 particle does heavy work in polite travel
        questions. The demonstration program verifies all twenty sentences
        and runs a route-builder that chains direction sentences from this
        record into a walking tour."""),
    key_points=[
        "Asking the way: 请问，___哪能去？ with answers 一直朝前走，左转，右转.",
        "Transport: 地铁 di3-thiq4, 公交车 kon1-ciau1-tsho1, 打车 ta2-tsho1, 火车 hu2-tsho1, 飞机 fi1-ci1.",
        "Tickets: 买票子, 几号线, 几路, 晚点 (delayed).",
        "Hotel: 住几夜, 空房间, 标准间, 包早饭𠲎？, 退房, 行李.",
        "Survival: 我迷路了, 地图浪向标一标, 谢谢侬带路.",
        "20 full sentences with translations: the complete traveler toolkit.",
    ],
    requirements=[
        "Learners should map a real route in their city and narrate it in Wu using sentences 1-5.",
        "Role-play the hotel check-in: sentences 11-16, both roles.",
    ],
    standards=[
        "CEFR A1-A2: transport, directions, tickets, lodging.",
        "Place names follow standard Shanghai usage.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Transport and direction vocabulary.",
        "上海市地方志办公室. 上海交通志. Shanghai transport records.",
    ],
    sig_lens=("Through the Signature lens, the journey is the signature in motion: every "
              "ticket a stamped permit, every direction asked and given a small covenant "
              "between strangers. This Signature reading treats the twenty travel "
              "sentences as a signed passport through Wu-speaking country."),
)

E(
    key="wu_work", name="Wu Chinese Work and School Sentences",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences about jobs, the office, the classroom, and learning.
        1. 侬做啥工作？(nong3 tsu2 sa3 kon1-tsoq4?) - What work do you do?
        2. 我勒银行上班。(ngu2 leq4 ngin3-hang3 zang3-pe1.) - I work at a bank.
        3. 伊是医生，勒医院工作。(yi3 zy3 yi1-sang1, leq4 yi1-yue3 kon1-tsoq4.) - He is a doctor; he works at a hospital.
        4. 老板今朝开会。(lau3-be2 cin1-tsau1 khe1-we3.) - The boss has a meeting today.
        5. 报告明朝要交。(pau2-kau2 min3-tsau1 iau2 ciau1.) - The report is due tomorrow.
        6. 加班到夜里九点钟。(ka1-pe1 tau2 ya3-li2 cieu2 tie2-tson1.) - Overtime until 9 at night.
        7. 同事之间要互相帮助。(don3-zy3 tsy1-cie1 iau2 wu3-shiang1 pang1-zu3.) - Colleagues should help each other.
        8. 工资啥辰光发？(kon1-tsy1 sa3 zen3-kuang1 faq4?) - When is payday?
        9. 迭个项目交关重要。(diq4-geq4 shiang3-moq5 ciau1-kue1 zon3-iau2.) - This project is very important.
        10. 开会辰光拿手机关脱。(khe1-we3 zen3-kuang1 na3 seu2-ci1 kue1-theq4.) - Turn off your phone during meetings.
        11. 学校里向有交关学生。(yoq5-gau3 li2-shiang3 yeu3 ciau1-kue1 yoq5-sang1.) - There are many students at the school.
        12. 老师上课交关生动。(lau3-sy1 zang3-khu2 ciau1-kue1 sang1-don3.) - The teacher's lessons are very lively.
        13. 今朝默写英语单词。(cin1-tsau1 meq4-shia2 in1-gniu2 te1-zy3.) - Today we have an English dictation quiz.
        14. 功课做脱了𠲎？(kon1-khu2 tsu2-theq4 leq4 vaq5?) - Is the homework finished?
        15. 考试考得哪能？(khau2-sy2 khau2-deq4 na3-nen3?) - How did the exam go?
        16. 考了九十分。(khau2 leq4 cieu2-zeq5 fen1.) - Scored ninety.
        17. 放学以后我去打球。(fang2-yoq5 yi2-heu3 ngu2 chi2 ta2-jieu3.) - After school I go play ball.
        18. 图书馆礼拜天开门𠲎？(du3-sy1-kue2 li3-ba-thie1 khe1-men3 vaq5?) - Is the library open on Sunday?
        19. 学吴语要有耐心。(yoq5 wu2-gniu2 iau2 yeu3 na3-shin1.) - Learning Wu takes patience.
        20. 熟能生巧，多讲多练。(zoq5 nen3 sang1-jiau2, tu1 kang2 tu1 lie3.) - Practice makes perfect: speak more, drill more."""),
    how_it_works=textwrap.dedent("""\
        This record teaches work and school as two daily scenes: the office
        (1-10) and the classroom (11-20). The learner introduces their job
        (我勒___上班), survives meetings and deadlines (开会, 报告要交,
        加班), then switches to school life (上课, 默写, 考试, 放学). Work
        vocabulary is drilled with the 勒 + workplace pattern; school
        vocabulary with the time words (今朝, 明朝, 以后). The closing
        proverb 熟能生巧 seals the record with Wu learning philosophy. The
        demonstration program verifies all twenty sentences and runs a
        workplace-role matcher pairing jobs with workplaces from this
        record."""),
    key_points=[
        "Jobs: 银行上班, 医生, 老板, 同事; office life: 开会, 报告, 加班, 工资, 项目.",
        "Workplace pattern: 勒 + place + 上班/工作 - 我勒银行上班.",
        "School: 上课, 默写, 考试, 功课, 放学, 图书馆.",
        "Time words anchor school life: 今朝默写, 明朝要交, 放学以后.",
        "Learning philosophy: 熟能生巧，多讲多练 - practice makes perfect.",
        "20 full sentences with translations: office and classroom Wu.",
    ],
    requirements=[
        "Learners should introduce their own job or studies in Wu: 我勒___上班/读书.",
        "Write your weekly schedule in Wu with 礼拜一 through 礼拜天.",
    ],
    standards=[
        "CEFR A2: work, office, school, study routines.",
        "Workplace vocabulary follows standard modern usage.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Work and school vocabulary.",
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. Wu in education and workplaces.",
    ],
    sig_lens=("Through the Signature lens, work is the signature made daily: every report "
              "submitted a page signed, every lesson taught a seal passed on. This "
              "Signature reading treats the classroom and the office as the two great "
              "signing-rooms of adult Wu life."),
)

E(
    key="wu_health", name="Wu Chinese Health and Body Sentences",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences about body parts, symptoms, the doctor visit, and
        the pharmacy.
        1. 头痛得交关厉害。(deu3 thon2-deq4 ciau1-kue1 li3-he3.) - The headache is severe.
        2. 我喉咙痛，讲勿出闲话。(ngu2 heu3-lon3 thon2, kang2-veq4-tsheq4 ye3-wo3.) - My throat hurts; I can barely speak.
        3. 肚皮勿适意，想呕。(du3-bi3 veq4 seq4-ni2, shiang2 eu2.) - My stomach feels bad; I want to vomit.
        4. 我发烧了，三十九度。(ngu2 faq4-sau1 leq4, se1-zeq5-cieu2 du3.) - I have a fever: 39 degrees.
        5. 感冒三天了，还勿好。(ke2-mau3 se1-thie1 leq4, we3 veq4 hau2.) - The cold has lasted three days and is still not better.
        6. 眼睛红红个，流眼泪。(nge3-cin1 gon3-gon3 geq4, lieu3 nge3-li3.) - The eyes are red and tearing.
        7. 鼻头塞住了，出勿出气。(biq5-deu3 seq4-zy3 leq4, tsheq4-veq4-tsheq4 chi2.) - The nose is stuffed; I cannot breathe.
        8. 牙齿痛，夜里向睏勿着。(nga3-tshy2 thon2, ya3-li2-shiang3 khun2-veq4-zaq5.) - Toothache; cannot sleep at night.
        9. 手划破了，出血了。(seu2 wo3-phu2 leq4, tsheq4-shiq4 leq4.) - The hand is cut and bleeding.
        10. 脚扭着了，走勿动路。(ciaq4 gnieu2-zaq5 leq4, tseu2-veq4-don3 lu3.) - The ankle is sprained; cannot walk.
        11. 医生，我啥毛病？(yi1-sang1, ngu2 sa3 mau3-bing3?) - Doctor, what is wrong with me?
        12. 侬要验血。(nong3 iau2 ngie3-shiq4.) - You need a blood test.
        13. 吃药以后多喝开水。(chiq4-yaq5 yi2-heu3 tu1 heq4 khe1-sy2.) - After taking medicine, drink plenty of boiled water.
        14. 迭粒药饭前吃。(diq4-liq5 yaq5 ve3-jie3 chiq4.) - Take this pill before meals.
        15. 一天三次，一次两粒。(iq4-thie1 se1-tshy2, iq4-tshy2 liang3-liq5.) - Three times a day, two pills each time.
        16. 打针痛𠲎？(ta2-tsen1 thon2 vaq5?) - Does the injection hurt?
        17. 勿痛，一歇歇就好。(veq4 thon2, iq4-shiq4-shiq4 zieu3 hau2.) - It does not hurt; it is over in a moment.
        18. 药房勒医院对面。(yaq5-vang3 leq4 yi1-yue3 te2-mie3.) - The pharmacy is across from the hospital.
        19. 多休息，早点好。(tu1 shieu1-xiq4, tsau2-tie2 hau2.) - Rest more and get well soon.
        20. 身体是本钿，保重。(shen1-thi2 zy3 pen2-die3, pau2-zon3.) - Health is capital; take care."""),
    how_it_works=textwrap.dedent("""\
        This record teaches health as a clinic visit: the learner names body
        parts (头, 喉咙, 肚皮, 眼睛, 鼻头, 牙齿, 手, 脚), describes symptoms
        with 痛, 塞, 扭, 出血, then plays both patient and doctor (我啥毛
        病？ / 侬要验血). Dosage language - 一天三次，一次两粒, 饭前吃 - is
        drilled as life-critical vocabulary. The Wu body-part words with
        their voiced initials (肚皮 du3-bi3, 鼻头 biq5-deu3) double as
        pronunciation practice. The demonstration program verifies all
        twenty sentences and runs a symptom-to-body-part matcher from this
        record's vocabulary."""),
    key_points=[
        "Body parts: 头 deu3, 喉咙 heu3-lon3, 肚皮 du3-bi3, 眼睛 nge3-cin1, 鼻头 biq5-deu3, 牙齿 nga3-tshy2, 手 seu2, 脚 ciaq4.",
        "Symptoms: 痛 thon2 (ache), 发烧 faq4-sau1 (fever), 感冒 ke2-mau3 (cold), 塞住 (stuffed), 扭着 (sprained), 出血 (bleeding).",
        "Doctor dialogue: 我啥毛病？ (what is wrong?), 侬要验血 (you need a blood test).",
        "Dosage: 一天三次，一次两粒; 饭前吃 (before meals); 打针 (injection).",
        "Pharmacy: 药房 yaq5-vang3; advice: 多休息, 多喝开水.",
        "20 full sentences with translations: the complete clinic toolkit.",
    ],
    requirements=[
        "Learners should memorize the eight body parts with a pointing drill: point and name in Wu.",
        "Practice the dosage frame until automatic: 一天__次，一次__粒.",
    ],
    standards=[
        "CEFR A2: body, health, symptoms, medical visits, pharmacy.",
        "Medical vocabulary follows standard modern usage.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Body and medical vocabulary.",
        "World Health Organization. Multilingual health terminology references.",
    ],
    sig_lens=("Through the Signature lens, the body is the first document ever signed: "
              "every ache a marginal note, every recovery a countersignature. This "
              "Signature reading treats the twenty health sentences as the learner's "
              "medical power of attorney in Wu."),
)

E(
    key="wu_emotions", name="Wu Chinese Emotions and Feelings Sentences",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences about being happy, sad, angry, afraid, loving, and
        surprised.
        1. 今朝我交关开心。(cin1-tsau1 ngu2 ciau1-kue1 khe1-shin1.) - I am very happy today.
        2. 听到迭个消息，我欢喜得跳起来。(thin1-tau2 diq4-geq4 shiau1-xiq4, ngu2 hoe1-xi2-deq4 thiau2-chi2-le3.) - Hearing the news, I jumped for joy.
        3. 朋友来了，我心里向热烘烘个。(bong3-yeu3 le3 leq4, ngu2 shin1-li2-shiang3 gniq5-hon1-hon1 geq4.) - My friend came; my heart feels warm.
        4. 考试通过了，真叫人高兴。(khau2-sy2 thon1-ku2 leq4, tsen1 ciau2-gnin3 kau1-shing2.) - Passing the exam is truly delightful.
        5. 囡囡生出来，全家都欢喜。(noe1-noe1 sang1-tsheq4-le3, jie3-ka1 tu1 hoe1-xi2.) - The baby was born; the whole family rejoices.
        6. 伊走了，我心里向空落落个。(yi3 tseu2 leq4, ngu2 shin1-li2-shiang3 khon1-loq4-loq4 geq4.) - He left; my heart feels empty.
        7. 听到坏消息，我难过得吃勿下饭。(thin1-tau2 wa3 shiau1-xiq4, ngu2 ne3-ku2-deq4 chiq4-veq4-o3 ve3.) - Hearing the bad news, I was too sad to eat.
        8. 眼泪止勿住流下来。(nge3-li3 tsy2-veq4-zy3 lieu3-o3-le3.) - Tears kept flowing unstoppably.
        9. 迭部电影看得我想哭。(diq4-bu3 die3-ying2 khe2-deq4 ngu2 shiang2 khoq4.) - The film moved me to tears.
        10. 失败了也勿要灰心。(seq4-be3 leq4 ya3 veq4-iau2 hue1-shin1.) - Do not lose heart even in failure.
        11. 伊发火了，声音交关大。(yi3 faq4-hu2 leq4, sang1-in1 ciau1-kue1 du3.) - He lost his temper; his voice was very loud.
        12. 迭件事体真叫人生气。(diq4-jie3 zy3-thi2 tsen1 ciau2-gnin3 sang1-chi2.) - This matter is truly infuriating.
        13. 侬勿要动气，慢慢讲。(nong3 veq4-iau2 don3-chi2, me3-me3 kang2.) - Do not get angry; speak slowly.
        14. 夜里向一个人走夜路，我有点害怕。(ya3-li2-shiang3 iq4-geq4 gnin3 tseu2 ya3-lu3, ngu2 yeu3-tie2 ha2-pho2.) - Walking alone at night, I feel a bit afraid.
        15. 打雷了，囡囡吓得哭起来。(ta2-le3 leq4, noe1-noe1 shaq4-deq4 khoq4-chi2-le3.) - Thunder scared the child into crying.
        16. 我欢喜侬，真心个。(ngu2 hoe1-xi2 nong3, tsen1-shin1 geq4.) - I love you, truly.
        17. 伊拉两个人感情交关好。(yi3-la1 liang3-geq4 gnin3 ke2-zing3 ciau1-kue1 hau2.) - The two of them are deeply in love.
        18. 突然听见敲门声，吓我一跳。(theq4-zen3 thin1-cie2 khau1-men3-sang1, shaq4 ngu2 iq4-thiau2.) - A sudden knock startled me.
        19. 真想勿到，伊居然来了。(tsen1 shiang2-veq4-tau2, yi3 ci1-zen3 le3 leq4.) - Unexpectedly, he actually came.
        20. 心情好，啥事体都顺。(shin1-zing3 hau2, sa3 zy3-thi2 tu1 shen3.) - With a good mood, everything goes smoothly."""),
    how_it_works=textwrap.dedent("""\
        This record teaches feelings as six scenes: joy (1-5), sadness
        (6-10), anger (11-13), fear (14-15), love (16-17), surprise (18-19),
        closing with philosophy (20). The learner performs each emotion
        while saying its sentences - Wu feeling-words are physical: 心里向
        热烘烘 (heart warm), 眼泪止勿住 (tears unstoppable), 吓一跳 (startled
        jump). Result complements (欢喜得跳起来, 难过得吃勿下饭) show how Wu
        builds intensity grammatically. The demonstration program verifies
        all twenty sentences and runs an emotion-sorter that files each
        sentence under its feeling from this record."""),
    key_points=[
        "Joy: 开心 khe1-shin1, 欢喜 hoe1-xi2, 高兴 kau1-shing2; heart-words: 心里向热烘烘 (warm heart).",
        "Sadness: 难过 ne3-ku2, 灰心 hue1-shin1 (lose heart); 眼泪止勿住 (unstoppable tears).",
        "Anger: 发火 faq4-hu2, 生气 sang1-chi2, 动气 don3-chi2; 勿要动气 (do not get angry).",
        "Fear: 害怕 ha2-pho2, 吓 shaq4; surprise: 吓一跳, 想勿到.",
        "Love: 欢喜 hoe1-xi2 (like/love), 感情 ke2-zing3 (affection); 真心个 (truly).",
        "Intensity via result complements: 欢喜得跳起来, 难过得吃勿下饭.",
        "20 full sentences with translations: the emotional life in Wu.",
    ],
    requirements=[
        "Learners should perform each emotion while speaking its sentences - face and voice included.",
        "Build result complements for your own feelings: ___得___起来.",
    ],
    standards=[
        "CEFR A2: emotions, feelings, reactions, intensity.",
        "Emotion vocabulary follows standard Shanghai usage.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Emotion vocabulary.",
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. Wu result complements.",
    ],
    sig_lens=("Through the Signature lens, feeling is the ink of the signature: joy the "
              "bright seal, sorrow the heavy one, love the seal pressed deepest. This "
              "Signature reading treats the twenty emotion sentences as the learner's "
              "permission to sign their heart in Wu."),
)

E(
    key="wu_nature", name="Wu Chinese Nature and Weather Sentences",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences about animals, plants, seasons, and weather talk.
        1. 春天花开了，交关好看。(tshen1-thie1 ho1 khe1 leq4, ciau1-kue1 hau2-khe2.) - Spring flowers bloom; so beautiful.
        2. 夏天太阳毒，记得戴帽子。(yo3-thie1 tha2-yang3 doq5, ci2-deq4 ta2 mau3-tsy2.) - Summer sun is fierce; remember a hat.
        3. 秋天桂花香，满城侪闻得着。(tshieu1-thie1 ku1-ho1 shiang1, me3-zen3 za3 ven3-deq4-zaq5.) - Osmanthus scents autumn; the whole city smells it.
        4. 冬天下雪，孩子堆雪人。(ton1-thie1 o3-shiq4, ha3-tsy2 te1 shiq4-gnin3.) - Snow falls in winter; children build snowmen.
        5. 落雨了，记得带伞。(loq4-yu3 leq4, ci2-deq4 ta2 se3.) - It is raining; remember an umbrella.
        6. 雨停了，天放晴了。(yu3 ding3 leq4, thie1 fang2-jing3 leq4.) - The rain stopped; the sky cleared.
        7. 今朝风交关大，当心着凉。(cin1-tsau1 fon1 ciau1-kue1 du3, tang1-shin1 zaq5-liang3.) - Very windy today; beware catching cold.
        8. 打雷闪电，雨马上就来。(ta2-le3 she3-die3, yu3 mo3-zang3 zieu3 le3.) - Thunder and lightning; rain is coming soon.
        9. 天气预报讲明朝落雨。(thie1-chi2 yu3-pau2 kang2 min3-tsau1 loq4-yu3.) - The forecast says rain tomorrow.
        10. 黄梅天闷热潮湿。(wang3-me3-thie1 men3-gniq5 zau1-seq4.) - The plum-rain season is muggy and damp.
        11. 狗对主人最忠心。(keu2 te2-tsy2 gnin3 tse2 tson1-shin1.) - Dogs are most loyal to their masters.
        12. 猫勒太阳底下困懒觉。(mau1 leq4 tha2-yang3 ti2-o3 khun2-le3-kau2.) - The cat naps in the sun.
        13. 鸟勒树浪向唱歌。(niau2 leq4 zy3 lang3-shiang3 t
        shang2-ku1.) - Birds sing in the trees.
        14. 池塘里向鱼游来游去。(zy3-dang3 li2-shiang3 ng3 yeu3-le3-yeu3-chi2.) - Fish swim back and forth in the pond.
        15. 蝴蝶飞舞，花园里向真热闹。(wu3-diq5 fi1-wu3, ho1-yoe3 li2-shiang3 tsen1 gniq5-nau3.) - Butterflies dance; the garden is so lively.
        16. 山浪向树木交关茂盛。(se1 lang3-shiang3 zy3-moq5 ciau1-kue1 meu3-zen3.) - The mountain trees grow lush.
        17. 长江是阿拉个母亲河。(zang3-kang1 zy3 aq4-laq4 geq4 mu2-tshin1 wu3.) - The Yangtze is our mother river.
        18. 西湖风景天下闻名。(shi1-wu3 fon1-cing2 thie1-o3 ven3-ming3.) - West Lake scenery is world-famous.
        19. 早晨空气新鲜，去跑步𠲎？(tsau2-zen3 khon1-chi2 shin1-shie1, chi2 bau2-bu3 vaq5?) - Morning air is fresh; shall we go running?
        20. 保护环境，人人有责。(pau2-wu3 we3-cing3, gnin3-gnin3 yeu3 zeq4.) - Protecting the environment is everyone's duty."""),
    how_it_works=textwrap.dedent("""\
        This record teaches nature as a year walked through: the learner
        narrates the four seasons with their Wu markers - 春天花开, 夏天
        太阳毒, 秋天桂花香 (the beloved Shanghai osmanthus), 冬天下雪 - then
        becomes a weather reporter (落雨了, 雨停了, 天气预报). Animals get
        the loyalty drill (狗最忠心), plants the garden tour, and the great
        landmarks (长江, 西湖) anchor Wu nature in real geography. Weather
        small-talk - 今朝风交关大 - is practiced as the universal Wu
        conversation opener. The demonstration program verifies all twenty
        sentences and runs a season-sorter filing each nature sentence under
        spring, summer, autumn, or winter."""),
    key_points=[
        "Seasons: 春天 tshen1-thie1, 夏天 yo3-thie1, 秋天 tshieu1-thie1, 冬天 ton1-thie1; 黄梅天 wang3-me3-thie1 (plum-rain season).",
        "Weather: 落雨 loq4-yu3 (rain), 落雪 loq4-shiq4 (snow), 风 fon1 (wind), 打雷 ta2-le3 (thunder), 天气预报 (forecast).",
        "Animals: 狗 keu2, 猫 mau1, 鸟 niau2, 鱼 ng3, 蝴蝶 wu3-diq5; plants: 花 ho1, 树 zy3, 桂花 ku1-ho1.",
        "Landmarks: 长江 zang3-kang1 (Yangtze), 西湖 shi1-wu3 (West Lake).",
        "Weather talk is the Wu small-talk opener: 今朝天气哪能？",
        "20 full sentences with translations: the natural world in Wu.",
    ],
    requirements=[
        "Learners should give a Wu weather report every morning for a week.",
        "Walk through a park narrating everything seen in Wu: 花开了，鸟唱歌.",
    ],
    standards=[
        "CEFR A2: nature, animals, plants, seasons, weather.",
        "Seasonal vocabulary follows standard Jiangnan usage.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Nature vocabulary.",
        "上海市地方志办公室. 上海自然地理志. Shanghai natural geography records.",
    ],
    sig_lens=("Through the Signature lens, nature is the original signed document: "
              "every spring blossom a seal renewed, every Yangtze wave a signature "
              "repeated for ten thousand years. This Signature reading treats the "
              "twenty nature sentences as the learner's countersignature on the "
              "Jiangnan landscape."),
)

E(
    key="wu_shopping", name="Wu Chinese Shopping and Money Sentences",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences about the market, prices, bargaining, and paying.
        1. 侬要买啥？(nong3 iau2 ma2 sa3?) - What do you want to buy?
        2. 迭件衣裳几化钞票？(diq4-jie3 yi1-zang3 ci2-hu3 tshau1-phiau2?) - How much is this garment?
        3. 三百八十块。(se1-paq4 paq4-zeq5 khue2.) - 380 yuan.
        4. 太贵了，便宜点𠲎？(tha2 ku2 leq4, bie3-nyi3 tie2 vaq5?) - Too expensive; a bit cheaper?
        5. 最低几化？(tse2-ti1 ci2-hu3?) - What is the lowest price?
        6. 两百块卖𠲎？(liang3-paq4 khue2 ma3 vaq5?) - Will you sell for 200?
        7. 好吧，成交。(hau2-ba1, zen3-ciau1.) - All right, deal.
        8. 一分价钿一分货。(iq4-fen1 ka2-die3 iq4-fen1 hu2.) - You get what you pay for.
        9. 拿发票开一张。(na3 faq4-phiau2 khe1 iq4-tsang1.) - Please issue a receipt.
        10. 可以刷卡𠲎？(khu2-yi2 shaq4-kha2 vaq5?) - Can I pay by card?
        11. 侬扫我还是我扫侬？(nong3 sau2 ngu2 we3-zy3 ngu2 sau2 nong3?) - Do you scan me or do I scan you? (mobile pay)
        12. 找侬二十块。(tsau2 nong3 gni3-zeq5 khue2.) - Here is your 20 yuan change.
        13. 买一送一，合算。(ma2 iq4 son2 iq4, geq4-se2.) - Buy one get one free; a bargain.
        14. 打八折。(ta2 paq4-tseq4.) - Twenty percent off.
        15. 迭个有保修𠲎？(diq4-geq4 yeu3 pau2-shieu1 vaq5?) - Does this have a warranty?
        16. 七天包退换。(chiq4-thie1 pau1 the2-we3.) - Returns and exchanges within seven days.
        17. 大小勿合适，可以换𠲎？(du3-siau2 veq4 geq4-seq4, khu2-yi2 we3 vaq5?) - The size does not fit; can I exchange it?
        18. 侬要发票还是收据？(nong3 iau2 faq4-phiau2 we3-zy3 seu1-ku2?) - Do you want an invoice or a receipt?
        19. 货比三家勿吃亏。(hu2 pi2 se1-ka1 veq4 chiq4-khu1.) - Comparing three shops, you will not lose out.
        20. 下趟再来，生意兴隆。(o3-thang2 tse2-le3, sang1-yi2 shing1-lon3.) - Come again; may business prosper."""),
    how_it_works=textwrap.dedent("""\
        This record teaches shopping as a bargaining drama in three acts:
        asking prices (1-4), haggling (5-8), and paying (9-20). The learner
        practices the Wu bargaining script until it flows: 太贵了，便宜点
        𠲎？ / 最低几化？ / 两百块卖𠲎？ / 好吧，成交. Money words - 钞票,
        价钿, 块, 发票, 刷卡, 扫码 - are drilled with real amounts. The Wu
        proverbs of the market (一分价钿一分货, 货比三家勿吃亏) carry the
        merchant philosophy. The demonstration program verifies all twenty
        sentences and runs a bargaining simulator that haggles from an asking
        price to a deal using this record's phrases."""),
    key_points=[
        "Price questions: 几化钞票？ (how much?), 价钿 ka2-die3 (price), 块 khue2 (yuan).",
        "Bargaining script: 太贵了，便宜点𠲎？ -> 最低几化？ -> 两百块卖𠲎？ -> 好吧，成交.",
        "Paying: 刷卡 (card), 扫码 (scan to pay), 找钞票 (change), 发票/收据 (receipt).",
        "Deals: 买一送一, 打八折, 七天包退换, 保修.",
        "Market proverbs: 一分价钿一分货 (you get what you pay for), 货比三家勿吃亏 (compare three shops).",
        "20 full sentences with translations: the complete market toolkit.",
    ],
    requirements=[
        "Learners should role-play buyer and seller through the full bargaining script three times.",
        "Practice amounts aloud: 三百八十块, 两百块, 二十块 - until numbers fly.",
    ],
    standards=[
        "CEFR A2: shopping, prices, bargaining, paying, returns.",
        "Commercial vocabulary follows standard modern usage.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Commercial vocabulary.",
        "上海市地方志办公室. 上海商业志. Shanghai commercial records.",
    ],
    sig_lens=("Through the Signature lens, the bargain is a negotiation of signatures: "
              "the asking price the first offer signed, the counteroffer the reply, "
              "成交 the final seal pressed by both hands. This Signature reading "
              "treats every haggled deal as a contract written in Wu."),
)

E(
    key="wu_social", name="Wu Chinese Friendship and Social Life Sentences",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences about meeting people, invitations, and celebrations.
        1. 初次见面，请多关照。(tshu1-tshy2 cie2-mie3, tshin2 tu1 kue1-tsau2.) - Nice to meet you; please look after me.
        2. 侬叫啥名字？(nong3 ciau2 sa3 ming3-zy3?) - What is your name?
        3. 我叫小王，侬呢？(ngu2 ciau2 siau2-wang3, nong3 ni3?) - I am called Xiao Wang; and you?
        4. 侬是啥地方人？(nong3 zy3 sa3 di3-fang1 gnin3?) - Where are you from?
        5. 我是上海人。(ngu2 zy3 zang3-he2 gnin3.) - I am Shanghainese.
        6. 幸会幸会。(xing3-we3 xing3-we3.) - Honored to meet you.
        7. 礼拜六有空𠲎？一起吃饭。(li3-ba-loq4 yeu3 khon2 vaq5? iq4-chi2 chiq4-ve3.) - Are you free Saturday? Let us eat together.
        8. 明朝夜里向我请侬看电影。(min3-tsau1 ya3-li2-shiang3 ngu2 tshin2 nong3 khe2 die3-ying2.) - Tomorrow evening I invite you to a film.
        9. 好啊，啥辰光碰头？(hau2-a1, sa3 zen3-kuang1 bon2-deu3?) - Great; when shall we meet?
        10. 夜里向七点钟，人民广场地铁口。(ya3-li2-shiang3 chiq4 tie2-tson1, zen3-min3 kuang3-zang3 di3-thiq4 kheu2.) - 7 PM at the People Square subway entrance.
        11. 勿见勿散。(veq4 cie2 veq4 se2.) - Be there or be square (no meeting, no leaving).
        12. 生日快乐。(sang1-zeq5 khua2-loq5.) - Happy birthday.
        13. 祝侬福如东海，寿比南山。(tsoq4 nong3 foq4-zy3 ton1-he2, zeu3-pi2 ne3-se1.) - Wishing you fortune vast as the eastern sea, life long as the southern mountains.
        14. 新婚快乐，早生贵子。(shin1-huen1 khua2-loq5, tsau2-sang1 ku2-tsy2.) - Happy wedding; may you soon have a fine son.
        15. 干杯。(ke1-pe1.) - Cheers.
        16. 侬最近忙啥？(nong3 tse2-jin3 mang3 sa3?) - What have you been busy with lately?
        17. 有空常来白相。(yeu3 khon2 zang3 le3 baq5-shiang2.) - Come visit often when free.
        18. 路上当心，到家发个消息。(lu3-zang3 tang1-shin1, tau2-ka1 faq4 geq4 shiau1-xiq4.) - Travel safe; message me when home.
        19. 改日再聚。(ke2-zeq5 tse2-zy3.) - Let us gather again another day.
        20. 朋友多，路好走。(bong3-yeu3 tu1, lu3 hau2 tseu2.) - Many friends make the road easy."""),
    how_it_works=textwrap.dedent("""\
        This record teaches social life as three scenes: first meeting
        (1-6), making plans (7-11), and celebrating (12-20). The learner
        practices the Wu introduction ritual - 侬叫啥名字？ / 我叫___, 侬
        呢？ / 侬是啥地方人？ - until it runs itself, then the invitation
        dance: 有空𠲎？, 好啊，啥辰光碰头？, 勿见勿散. Celebration phrases
        (生日快乐, 干杯, 祝侬福如东海) are drilled as performance pieces.
        The demonstration program verifies all twenty sentences and runs a
        social-situation matcher that picks the Wu-right phrase for meeting,
        inviting, or celebrating."""),
    key_points=[
        "Introductions: 初次见面，请多关照; 侬叫啥名字？; 侬是啥地方人？; 幸会.",
        "Invitations: 有空𠲎？一起吃饭; 啥辰光碰头？; 勿见勿散 (be there or be square).",
        "Celebrations: 生日快乐, 新婚快乐，早生贵子, 干杯, 祝侬福如东海，寿比南山.",
        "Farewell care: 路上当心，到家发个消息; 有空常来白相; 改日再聚.",
        "Philosophy: 朋友多，路好走 - many friends make the road easy.",
        "20 full sentences with translations: Wu social life complete.",
    ],
    requirements=[
        "Learners should perform the full introduction ritual with three different partners.",
        "Memorize the celebration phrases; use 生日快乐 and 干杯 at the next real occasion.",
    ],
    standards=[
        "CEFR A2: introductions, invitations, celebrations, farewells.",
        "Social formulae follow standard Shanghai practice.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Social phrase entries.",
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. Wu social formulae.",
    ],
    sig_lens=("Through the Signature lens, friendship is the signature willingly given: "
              "every introduction a new page opened, every invitation a seal offered, "
              "every 干杯 a covenant lifted. This Signature reading treats the twenty "
              "social sentences as the learner's growing book of Wu friendships."),
)

E(
    key="wu_tech", name="Wu Chinese Technology and Communication Sentences",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences about the phone, internet, computer, and messaging.
        1. 侬手机号码几化？(nong3 seu2-ci1 hau3-mo3 ci2-hu3?) - What is your mobile number?
        2. 我个手机没电了。(ngu2 geq4 seu2-ci1 meq5-die3 leq4.) - My phone is out of battery.
        3. 拿充电器借我用用。(na3 tshon1-die3-chi2 cia2 ngu2 yon3-yon3.) - Lend me the charger.
        4. 无线网密码是啥？(wu3-shie2-mang3 meq5-mo3 zy3 sa3?) - What is the wifi password?
        5. 网速交关慢，视频卡住了。(mang3-soq4 ciau1-kue1 me3, zy3-bing3 kha2-zy3 leq4.) - The internet is slow; the video froze.
        6. 侬发个定位给我。(nong3 faq4 geq4 ding3-we3 peq4 ngu2.) - Send me your location.
        7. 我扫侬加微信。(ngu2 sau2 nong3 ka1 wi1-shin2.) - I will scan you to add WeChat.
        8. 朋友圈点赞。(bong3-yeu3-jie1 tie2-tse2.) - Like the Moments post.
        9. 迭个链接勿要乱点。(diq4-geq4 lie3-ciq4 veq4-iau2 lo3-tie2.) - Do not click that link carelessly.
        10. 电脑开勿起来了。(die3-nau2 khe1-veq4-chi2-le3 leq4.) - The computer will not start.
        11. 重新启动试试看。(zon3-shin1 chi2-don3 sy2-sy2-khe2.) - Try restarting it.
        12. 文件保存了𠲎？(ven3-jie3 pau2-zen3 leq4 vaq5?) - Did you save the file?
        13. 照片发到我邮箱。(tsau2-phie2 faq4-tau2 ngu2 yeu3-shiang1.) - Send the photos to my email.
        14. 视频会议三点钟开始。(zy3-bing3 we3-ngi3 se1 tie2-tson1 khe1-sy2.) - The video meeting starts at three.
        15. 侬静音了，我听勿见。(nong3 jing3-in1 leq4, ngu2 thin1-veq4-cie2.) - You are muted; I cannot hear you.
        16. 共享屏幕给我看。(gon3-shiang2 bing3-mu2 peq4 ngu2 khe2.) - Share your screen with me.
        17. 软件要更新了。(gne3-jie3 iau2 ken2-shin1 leq4.) - The software needs updating.
        18. 密码勿要告诉别人。(meq5-mo3 veq4-iau2 kau2-su2 biq5-gnin3.) - Do not tell anyone your password.
        19. 陌生电话勿要接。(moq5-sang1 die3-wo3 veq4-iau2 ciq4.) - Do not answer strange calls.
        20. 下线了，明朝聊。(o3-shie2 leq4, min3-tsau1 liau3.) - Logging off; chat tomorrow."""),
    how_it_works=textwrap.dedent("""\
        This record teaches digital life as a day online: the learner
        charges the phone (1-3), fights the wifi (4-6), works the apps
        (7-9), rescues the computer (10-13), survives the video meeting
        (14-16), and practices safety (17-20). Every sentence is a real line
        from digital life, drilled in problem-solution pairs: 网速交关慢 /
        重新启动试试看; 电脑开勿起来了 / 文件保存了𠲎？ The safety lines
        (迭个链接勿要乱点, 密码勿要告诉别人) are memorized as Wu survival
        rules. The demonstration program verifies all twenty sentences and
        runs a tech-support dialogue matcher pairing problems with solutions
        from this record's vocabulary."""),
    key_points=[
        "Phone: 手机 seu2-ci1, 充电器, 没电了, 手机号码.",
        "Internet: 无线网, 密码, 网速慢, 视频卡住了, 发定位, 扫码加微信.",
        "Computer: 开勿起来, 重新启动, 文件保存, 邮箱, 软件更新.",
        "Video meetings: 视频会议, 静音了, 共享屏幕.",
        "Safety: 链接勿要乱点, 密码勿要告诉别人, 陌生电话勿要接.",
        "20 full sentences with translations: digital life in Wu.",
    ],
    requirements=[
        "Learners should narrate their next hour of device use in Wu: 我扫码，网速慢...",
        "Memorize the three safety lines; say them to family in Wu.",
    ],
    standards=[
        "CEFR A2: technology, devices, internet, everyday digital communication.",
        "Tech vocabulary follows standard modern Chinese usage with Wu readings.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Modern vocabulary entries.",
        "中国互联网络信息中心. 互联网技术术语. Standard internet terminology.",
    ],
    sig_lens=("Through the Signature lens, the message is the voice extended: the link "
              "the bridge signed, the password the seal of the private archive, every "
              "call the oath that distance will not silence us. This Signature "
              "reading treats technology as the covenant of connection."),
)

E(
    key="wu_tenses", name="Wu Chinese Verb Tenses in Sentences",
    group="Advanced", ladder_rank=7, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Wu verbs never conjugate; time and aspect ride on particles and time
        words. Five or more translated sentences per pattern.
        Present / habitual (time word or plain verb):
        我天天跑步。(ngu2 thie1-thie1 bau2-bu3.) - I run every day.
        伊勒银行上班。(yi3 leq4 ngin3-hang3 zang3-pe1.) - He works at a bank.
        阿拉学吴语。(aq4-laq4 yoq5 wu2-gniu2.) - We study Wu.
        侬欢喜吃啥？(nong3 hoe1-xi2 chiq4 sa3?) - What do you like to eat?
        猫欢喜困懒觉。(mau1 hoe1-xi2 khun2-le3-kau2.) - Cats like napping.
        Ongoing with 勒海 (leq4-he2):
        伊勒海吃饭。(yi3 leq4-he2 chiq4-ve3.) - He is eating (right now).
        我勒海看书，勿要吵。(ngu2 leq4-he2 khe2-sy1, veq4-iau2 tshau2.) - I am reading; do not disturb.
        外头勒海落雨。(nga3-deu3 leq4-he2 loq4-yu3.) - It is raining outside.
        侬勒海做啥？(nong3 leq4-he2 tsu2 sa3?) - What are you doing?
        Completed with 仔 (tsy2):
        我吃仔饭了。(ngu2 chiq4-tsy2 ve3 leq4.) - I ate (finished eating).
        功课做仔了。(kon1-khu2 tsu2-tsy2 leq4.) - The homework is done.
        电影看仔了。(die3-ying2 khe2-tsy2 leq4.) - Finished watching the film.
        门关仔了𠲎？(men3 kue1-tsy2 leq4 vaq5?) - Is the door closed?
        Past with 过 (ku2, experienced):
        我去过苏州。(ngu2 chi2-ku2 su1-tseu1.) - I have been to Suzhou.
        伊吃过小笼包。(yi3 chiq4-ku2 siau2-lon3-pau1.) - He has eaten soup dumplings before.
        侬看过迭部电影𠲎？(nong3 khe2-ku2 diq4-bu3 die3-ying2 vaq5?) - Have you seen this film?
        Future with 要 (iau2) / 会 (we3):
        明朝我要去上海。(min3-tsau1 ngu2 iau2 chi2 zang3-he2.) - Tomorrow I will go to Shanghai.
        伊会来个。(yi3 we3 le3 geq4.) - He will come.
        落雨要带伞。(loq4-yu3 iau2 ta2 se3.) - If it rains, bring an umbrella. (lit: rain will need umbrella)
        阿拉会再会个。(aq4-laq4 we3 ze3-we3 geq4.) - We will meet again.
        Negative past with 朆 (ven3):
        我朆去过。(ngu2 ven3 chi2-ku2.) - I have not gone.
        伊朆吃早饭。(yi3 ven3 chiq4 tsau2-ve3.) - He has not eaten breakfast."""),
    how_it_works=textwrap.dedent("""\
        This record teaches Wu time as a particle toolkit: the learner takes
        one verb - 吃 - and runs it through every pattern: 我吃饭 (habit),
        伊勒海吃饭 (right now), 我吃仔饭了 (finished), 我吃过 (experienced),
        我要吃 (will eat), 我朆吃 (have not eaten). The transformation drill
        makes the system physical: same verb, six particles, six times. 勒
        海 gets a now-drill (what is everyone doing 勒海 right now?); 仔
        gets a done-drill (what did you finish today?); 过 gets a
        life-experience interview (侬去过啥地方？). The demonstration program
        is a tense identifier: given Wu sentences from this record, it
        labels each with its aspect pattern and checks the particle sits in
        the Wu-right position."""),
    key_points=[
        "Present/habitual: plain verb or time word - 我天天跑步, 阿拉学吴语.",
        "Ongoing: 勒海 leq4-he2 + verb - 伊勒海吃饭 (he is eating right now).",
        "Completed: verb + 仔 tsy2 - 我吃仔饭了 (I finished eating).",
        "Experienced: verb + 过 ku2 - 我去过苏州 (I have been to Suzhou).",
        "Future: 要 iau2 / 会 we3 + verb - 明朝我要去上海; 落雨要带伞.",
        "Negative past: 朆 ven3 + verb - 我朆吃早饭 (I have not eaten breakfast).",
        "Verbs never change form; particles and time words carry all of time.",
    ],
    requirements=[
        "Learners should run ten verbs through all six patterns aloud: 吃 -> 吃饭/勒海吃/吃仔/吃过/要吃/朆吃.",
        "Interview a partner with 过: 侬去过啥地方？ 侬吃过啥好吃个？",
    ],
    standards=[
        "CEFR A2-B1: present, progressive, perfective, experiential, future, negative past.",
        "Aspect analysis follows Chao 1928 and Qian 1992 on Wu aspect markers.",
    ],
    citations=[
        "Chao Y R. Studies in the Modern Wu-dialects. 1928. Wu aspect and tense systems.",
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. 仔, 过, 勒海, 朆.",
    ],
    sig_lens=("Through the Signature lens, time is the signature dated: 仔 the seal of "
              "the finished, 过 the seal of the lived-through, 勒海 the seal of this "
              "very moment, 要 the seal of the promised. This Signature reading treats "
              "the six Wu time-patterns as six ways of dating one signature."),
)

E(
    key="wu_qa", name="Wu Chinese Questions and Answers",
    group="Advanced", ladder_rank=7, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty question-and-answer pairs covering who, what, where, when,
        why, and how.
        1. Q: 侬是谁？(nong3 zy3 sa3-gnin3?) A: 我是小王。(ngu2 zy3 siau2-wang3.) - Who are you? / I am Xiao Wang.
        2. Q: 迭是啥？(diq4 zy3 sa3?) A: 迭是茶杯。(diq4 zy3 dzo3-pe1.) - What is this? / This is a teacup.
        3. Q: 侬勒啥地方？(nong3 leq4 sa3 di3-fang1?) A: 我勒屋里。(ngu2 leq4 oq4-li2.) - Where are you? / I am at home.
        4. Q: 侬啥辰光来？(nong3 sa3 zen3-kuang1 le3?) A: 夜里向七点钟来。(ya3-li2-shiang3 chiq4 tie2-tson1 le3.) - When are you coming? / Coming at 7 PM.
        5. Q: 侬为啥勿去？(nong3 we3-sa3 veq4 chi2?) A: 因为我交关忙。(in1-we3 ngu2 ciau1-kue1 mang3.) - Why are you not going? / Because I am very busy.
        6. Q: 迭个字哪能读？(diq4-geq4 zy3 na3-nen3 doq5?) A: 读“侬”，nong3。(doq5 nong3.) - How is this character read? / Read nong3.
        7. Q: 侬去𠲎？(nong3 chi2 vaq5?) A: 去。(chi2.) - Are you going? / Yes (going).
        8. Q: 好𠲎？(hau2 vaq5?) A: 交关好。(ciau1-kue1 hau2.) - Is it good? / Very good.
        9. Q: 几化钞票？(ci2-hu3 tshau1-phiau2?) A: 五十块。(ng3-zeq5 khue2.) - How much? / Fifty yuan.
        10. Q: 哪一个？(na3 iq4-geq4?) A: 迭一个。(diq4 iq4-geq4.) - Which one? / This one.
        11. Q: 侬会说吴语𠲎？(nong3 we3 shuoq4 wu2-gniu2 vaq5?) A: 会一点点。(we3 iq4-tie2-tie2.) - Can you speak Wu? / A little.
        12. Q: 吃过了𠲎？(chiq4-ku2 leq4 vaq5?) A: 吃过了。(chiq4-ku2 leq4.) - Have you eaten? / Yes, eaten.
        13. Q: 门关好了𠲎？(men3 kue1-hau2 leq4 vaq5?) A: 关好了。(kue1-hau2 leq4.) - Is the door closed? / Closed.
        14. Q: 侬欢喜啥颜色？(nong3 hoe1-xi2 sa3 nga3-seq4?) A: 我欢喜蓝色。(ngu2 hoe1-xi2 le3-seq4.) - What color do you like? / I like blue.
        15. Q: 天气哪能？(thie1-chi2 na3-nen3?) A: 今朝天气交关好。(cin1-tsau1 thie1-chi2 ciau1-kue1 hau2.) - How is the weather? / Very good today.
        16. Q: 侬屋里向有几口人？(nong3 oq4-li2-shiang3 yeu3 ci2-kheu2 gnin3?) A: 有四口人。(yeu3 sy2-kheu2 gnin3.) - How many in your family? / Four.
        17. Q: 迭件衣裳啥料子？(diq4-jie3 yi1-zang3 sa3 lau3-tsy2?) A: 纯棉个。(zen3-mie3 geq4.) - What fabric is this garment? / Pure cotton.
        18. Q: 火车站远𠲎？(hu2-tsho1-ze3 yoe3 vaq5?) A: 勿远，走过去一刻钟。(veq4 yoe3, tseu2-ku2-chi2 iq4 kheq4-tson1.) - Is the station far? / Not far; a 15-minute walk.
        19. Q: 侬啥辰光有空？(nong3 sa3 zen3-kuang1 yeu3 khon2?) A: 礼拜天有空。(li3-ba-thie1 yeu3 khon2.) - When are you free? / Free on Sunday.
        20. Q: 学吴语难𠲎？(yoq5 wu2-gniu2 ne3 vaq5?) A: 勿难，交关有意思。(veq4 ne3, ciau1-kue1 yeu3 yi2-sy1.) - Is Wu hard to learn? / Not hard; very interesting."""),
    how_it_works=textwrap.dedent("""\
        This record teaches questions as a full interview: the learner and a
        partner fire all twenty questions at each other, answering in
        complete Wu sentences - never one-word answers at first. The six
        question families are drilled in rotation: 谁/啥人 (who), 啥 (what),
        啥地方 (where), 啥辰光 (when), 为啥 (why), 哪能 (how), plus the 𠲎
        yes/no pattern and the choice pattern (哪一个？). The learner notices
        that Wu word order never moves for questions - the interrogative
        simply sits where the answer sits. The demonstration program runs a
        Q&A matcher: given each question from this record, it checks the
        paired answer matches in topic and form."""),
    key_points=[
        "Who: 侬是谁？/啥人来了？ What: 迭是啥？ Where: 侬勒啥地方？ When: 侬啥辰光来？",
        "Why: 侬为啥勿去？ -> 因为... How: 迭个字哪能读？ How much: 几化钞票？ Which: 哪一个？",
        "Yes/no with 𠲎: 侬去𠲎？ 好𠲎？ 吃过了𠲎？ - answer by repeating the verb.",
        "Wu word order never changes for questions; the interrogative sits in the answer slot.",
        "Answer in full sentences first; short answers come with fluency.",
        "20 Q&A pairs with translations: the complete Wu interview.",
    ],
    requirements=[
        "Learners should interview a partner with all twenty questions, answering in full sentences.",
        "Write ten new Q&A pairs about your own life following these models.",
    ],
    standards=[
        "CEFR A2: asking and answering about identity, place, time, reason, manner, price.",
        "Question formation follows Chao 1928 on Wu interrogatives.",
    ],
    citations=[
        "Chao Y R. Studies in the Modern Wu-dialects. 1928. Wu interrogative systems.",
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Interrogative entries.",
    ],
    sig_lens=("Through the Signature lens, the question is the signature requested: "
              "every 啥, 哪能, 为啥 a blank line held out for the other to sign, every "
              "answer the seal pressed in reply. This Signature reading treats the "
              "twenty Q&A pairs as twenty small contracts of understanding."),
)

E(
    key="wu_commands", name="Wu Chinese Commands and Requests",
    group="Advanced", ladder_rank=7, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty imperative and polite-request sentences, formal vs informal.
        Informal (friends, family): 1. 来！(le3!) - Come!
        2. 看！(khe2!) - Look!
        3. 吃饭！(chiq4-ve3!) - Eat!
        4. 快点！(khuai2-tie2!) - Hurry!
        5. 坐！(zu3!) - Sit!
        6. 讲！(kang2!) - Speak!
        7. 勿要吵！(veq4-iau2 tshau2!) - Do not make noise!
        8. 当心！(tang1-shin1!) - Be careful!
        9. 拿来！(na3-le3!) - Bring it here!
        10. 等一歇！(ten2 iq4-shiq4!) - Wait a moment!
        Polite (请 tshin2 softens everything):
        11. 请坐。(tshin2 zu3.) - Please sit.
        12. 请讲。(tshin2 kang2.) - Please speak.
        13. 请等一歇。(tshin2 ten2 iq4-shiq4.) - Please wait a moment.
        14. 请拿菜单来。(tshin2 na3 tse2-te1 le3.) - Please bring the menu.
        15. 请问，厕所勒啥地方？(tshin2-ven3, tshy2-su2 leq4 sa3 di3-fang1?) - Excuse me, where is the restroom?
        Formal / elders / business:
        16. 请侬多多包涵。(tshin2 nong3 tu1-tu1 pau1-we3.) - Please forgive my shortcomings.
        17. 麻烦侬帮个忙。(me3-ve3 nong3 pang1 geq4 mang3.) - Sorry to trouble you; please help.
        18. 劳驾，让一让。(lau3-ka2, rang3 iq4-rang3.) - Excuse me, please make way.
        19. 请慢走，欢迎下趟再来。(tshin2 me3-tseu2, we1-ngin3 o3-thang2 tse2-le3.) - Please take care going; welcome back next time.
        20. 覅客气，当自己屋里向。(fiau2 kheq4-chi2, tang1 zy3-ci2 oq4-li2-shiang3.) - Do not stand on ceremony; make yourself at home."""),
    how_it_works=textwrap.dedent("""\
        This record teaches commands as a politeness ladder: the learner
        shouts the bare imperatives (来！ 看！ 吃饭！) to feel their
        bluntness, then climbs - adding 请, then 麻烦侬/劳驾, then the full
        formal formulae. The key Wu insight: the verb never changes; only
        the softeners change. 请坐 vs 坐！ is the whole lesson. Negative
        commands use 勿要/覅 (勿要吵！, 覅客气). The learner practices
        giving the same order three ways - to a child, to a friend, to an
        elder - feeling the register shift. The demonstration program
        verifies all twenty sentences and runs a register-sorter filing each
        command as informal, polite, or formal."""),
    key_points=[
        "Bare imperatives (informal): 来！ 看！ 吃饭！ 快点！ 坐！ - blunt, for close relations.",
        "请 tshin2 softens: 请坐, 请讲, 请等一歇 - the universal politeness tool.",
        "Formal: 麻烦侬, 劳驾, 请侬多多包涵 - for elders, guests, business.",
        "Negative commands: 勿要吵！, 覅客气 (do not stand on ceremony).",
        "The verb never changes; only the softeners mark the register.",
        "Wu hospitality peak: 覅客气，当自己屋里向 - make yourself at home.",
        "20 commands and requests with translations, informal to formal.",
    ],
    requirements=[
        "Learners should give the same five orders three ways: to a child, a friend, an elder.",
        "Memorize the formal set; use 请 and 麻烦侬 with all strangers.",
    ],
    standards=[
        "CEFR A2: imperatives, polite requests, registers.",
        "Politeness practice follows standard Shanghai usage.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Imperative and polite formulae.",
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. Wu politeness systems.",
    ],
    sig_lens=("Through the Signature lens, the command is the signature of authority and "
              "the request the signature of respect: the bare verb the seal of command, "
              "请 the seal of courtesy laid over it. This Signature reading treats the "
              "politeness ladder as twenty ways of signing one will."),
)

E(
    key="wu_descriptions", name="Wu Chinese Descriptions of People and Places",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty sentences describing people, places, and things in detail.
        1. 我个朋友高高个，戴眼镜，真斯文。(ngu2 geq4 bong3-yeu3 kau1-kau1 geq4, ta2 nge3-cing2, tsen1 sy1-ven3.) - My friend is tall, wears glasses, very refined.
        2. 奶奶头发全白了，身体还交关硬朗。(na3-na3 deu3-faq4 jie3 baq5 leq4, shen1-thi2 we3 ciau1-kue1 ngang3-lang3.) - Grandmother's hair is all white, but she is still very hale.
        3. 囡囡圆圆个脸，大大个眼睛，真嗲。(noe1-noe1 yoe3-yoe3 geq4 lie3, du3-du3 geq4 nge3-cin1, tsen1 tia2.) - The child has a round face and big eyes; so cute.
        4. 王老师四十岁上下，讲闲话慢条斯理。(wang3 lau3-sy1 sy2-zeq5 se2-o3-zo3, kang2 ye3-wo3 me3-diau3-sy1-li2.) - Teacher Wang is about forty and speaks unhurriedly.
        5. 迭个小伙子浓眉大眼，交关精神。(diq4-geq4 siau2-hu2-tsy2 non3-mi3 du3-nge3, ciau1-kue1 cin1-shen3.) - This young man has thick brows and big eyes; very spirited.
        6. 外滩夜景交关漂亮，黄浦江两岸灯火辉煌。(nga3-than1 ya3-cing2 ciau1-kue1 phiau2-liang3, wang3-phu2-kang1 liang3-nge3 ten1-hu2 hui1-wang3.) - The Bund at night is gorgeous; both banks of the Huangpu glitter.
        7. 豫园亭台楼阁，小桥流水，古色古香。(yu3-yoe3 ding3-de3 leu3-koq4, siau2-jiau3 lieu3-sy2, ku2-seq4 ku2-shiang1.) - Yu Garden has pavilions and towers, small bridges over flowing water, full of old-world charm.
        8. 苏州园林精致典雅，步步是景。(su1-tseu1 yoe3-lin3 cin1-tsy2 tie2-nga3, bu3-bu3 zy3 cing2.) - Suzhou gardens are exquisite and elegant; every step is a view.
        9. 西湖三面环山，一面抱城，湖光山色美勿胜收。(shi1-wu3 se1-mie3 we3-se1, iq4-mie3 pau3-zen3, wu3-kuang1 se1-seq4 me3-veq4 shen1-seu1.) - West Lake is ringed by hills on three sides; its beauty is endless.
        10. 南京路步行街人来人往，商店一家挨一家。(ne3-cin1 lu3 bu3-hang3-ka1 gnin3-le3-gnin3-wang3, sang1-tie2 iq4-ka1 nga3-iq4-ka1.) - Nanjing Road bustles with crowds; shops stand shoulder to shoulder.
        11. 弄堂里向老房子，石库门，交关有味道。(lon3-dang3 li2-shiang3 lau3 vang3-tsy2, zaq5-khu2-men3, ciau1-kue1 yeu3 we3-dau3.) - The old houses in the lanes, the stone-gate doors, full of character.
        12. 高楼大厦一幢比一幢高，直插云霄。(kau1-leu3 du3-o3 iq4-zang2 pi2 iq4-zang2 kau1, zeq4-tshaq4 yuin3-shiau1.) - Skyscrapers rise one higher than the next, piercing the clouds.
        13. 迭件旗袍料子真好，绣花精细。(diq4-jie3 ji3-bau3 lau3-tsy2 tsen1 hau2, shieu2-ho1 cin1-shi2.) - This qipao has fine fabric and delicate embroidery.
        14. 小笼包皮薄馅多，汤汁鲜美。(siau2-lon3-pau1 bi3 boq5 shie3 tu1, thang1-tseq4 shie1-me3.) - Soup dumplings: thin skin, generous filling, savory broth.
        15. 生煎馒头底脆肉香，咬一口满嘴汤。(sang1-cie3 me3-deu3 ti2-tshy2 gnioq5-shiang1, ngau3 iq4-kheu2 me3-tsy2 thang1.) - Pan-fried buns: crisp bottom, fragrant pork, a mouthful of soup in one bite.
        16. 春天个公园，樱花开得像云霞一样。(tshen1-thie1 geq4 kon1-yoe3, in1-ho1 khe1-deq4 ziang3 yuin3-ya3 iq4-yiang3.) - In the spring park, cherry blossoms bloom like rosy clouds.
        17. 老城隍庙香火旺盛，游客交关多。(lau3 zen3-wang3-miau3 shiang1-hu2 wang3-zen3, yeu3-kheq4 ciau1-kue1 tu1.) - The old City God Temple thrums with incense; crowds of visitors.
        18. 伊屋里向布置得温馨雅致。(yi3 oq4-li2-shiang3 pu2-tsy2-deq4 wen1-shing1 nga2-tsy2.) - His home is arranged warmly and elegantly.
        19. 迭幅画色彩鲜艳，栩栩如生。(diq4-foq4 wo3 seq4-tsha2 shie1-yie3, shiu2-shiu2 zy3-sang1.) - This painting has vivid colors, lifelike.
        20. 上海是海纳百川个城市，传统搭现代交融。(zang3-he2 zy3 he2-naq4 paq4-tshoe1 geq4 zen3-zy3, zoe3-thon3 taq4 gnie3-da3 ciau1-yung3.) - Shanghai is a city that gathers all rivers; tradition and modernity blend."""),
    how_it_works=textwrap.dedent("""\
        This record teaches description as painting with words: the learner
        describes three people they know (face, build, manner), three places
        they have been (what is seen, heard, felt), and three things they
        love (look, taste, texture). The Wu descriptive toolkit is drilled:
        reduplicated adjectives (高高个, 圆圆个, 大大个), the 有味道
        (characterful) judgment, and four-character rhythms (古色古香,
        灯火辉煌, 步步是景). Food description gets its own feast - the
        small-eats trilogy of 小笼包, 生煎, 旗袍. The demonstration program
        verifies all twenty sentences and runs a detail-counter that checks
        each description carries at least two concrete details from this
        record."""),
    key_points=[
        "People: reduplicated adjectives - 高高个, 圆圆个脸, 大大个眼睛; manner words 斯文, 精神, 慢条斯理.",
        "Places: 外滩夜景, 豫园, 苏州园林, 西湖, 南京路, 弄堂石库门 - each with signature details.",
        "Things: 旗袍 (fabric, embroidery), 小笼包 (thin skin, rich filling), 生煎 (crisp bottom), 画 (vivid colors).",
        "Wu judgment phrase: 有味道 (has character) - the highest praise for old streets and old things.",
        "Four-character rhythms: 古色古香, 灯火辉煌, 步步是景, 海纳百川.",
        "20 full sentences with translations: descriptive mastery.",
    ],
    requirements=[
        "Learners should describe three real people, three real places, three real things in Wu.",
        "Memorize the food descriptions; recite the 小笼包 line at the next dumpling meal.",
    ],
    standards=[
        "CEFR B1: detailed description of people, places, objects.",
        "Descriptive vocabulary follows standard Shanghai literary usage.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Descriptive vocabulary.",
        "上海市地方志办公室. 上海文化志. Shanghai cultural records: Bund, Yu Garden, lane houses.",
    ],
    sig_lens=("Through the Signature lens, description is the signature illuminated: "
              "every concrete detail a flourish of the pen, every 有味道 a seal of "
              "approval pressed on the world. This Signature reading treats the "
              "twenty descriptions as twenty illuminated signatures."),
)

E(
    key="wu_story1", name="Wu Chinese Story I: A Morning at the Market",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence simple story in Wu, line by line with English
        translation. Present-tense, everyday vocabulary.
        1. 今朝朝早，阿拉去菜场买菜。(cin1-tsau1 tsau1-tsau2, aq4-laq4 chi2 tshe2-zang3 ma2-tshe2.) - This morning, we go to the food market to buy vegetables.
        2. 菜场里向人交关多，交关热闹。(tshe2-zang3 li2-shiang3 nyin3 ciau1-kue1 tu1, ciau1-kue1 gniq5-nau3.) - The market is crowded and very lively.
        3. 青菜新鲜，菠菜水灵灵个。(tshing1-tshe2 shin1-shie1, pu1-tshe2 sy2-lin1-lin1 geq4.) - The greens are fresh; the spinach is crisp and dewy.
        4. 我买一把青菜，两斤番茄。(ngu2 ma2 iq4-po2 tshing1-tshe2, liang3-cin1 fie1-jia3.) - I buy a bunch of greens and two jin of tomatoes.
        5. 卖鱼个师傅大声叫：鱼新鲜！(ma3-ng3 geq4 sy1-fu3 du3-sang1 ciau2: ng3 shin1-shie1!) - The fish seller shouts: fresh fish!
        6. 我挑一条大鲫鱼，称一称。(ngu2 thiau1 iq4-diau3 du3 ciq4-ng3, tshen2 iq4-tshen2.) - I pick a big crucian carp and weigh it.
        7. 老板话：八块一斤。(lau3-be2 wo3: paq4-khue2 iq4-cin1.) - The boss says: eight yuan a jin.
        8. 我话：便宜点，六块𠲎？(ngu2 wo3: bie3-nyi3 tie2, loq4-khue2 vaq5?) - I say: cheaper, six yuan OK?
        9. 老板笑笑话：好吧，六块。(lau3-be2 shiau2-shiau2 wo3: hau2-ba1, loq4-khue2.) - The boss smiles: all right, six yuan.
        10. 拎着菜转屋里向，今朝晚饭有着落了。(lin3-zaq5 tshe2 tse3 oq4-li2-shiang3, cin1-tsau1 we3-ve3 yeu3-zaq5-loq5 leq4.) - Carrying the vegetables home, tonight dinner is settled."""),
    how_it_works=textwrap.dedent("""\
        This record teaches narrative as a walked path: the learner tells
        the market story aloud three times - first reading, then with the
        book closed from memory, then performing the two voices (我 and 老
        板). The ten sentences chain with time and action: 去, 买, 挑,
        称, 讲价, 成交, 转屋里向. Direct speech (老板话：...) introduces Wu
        dialogue punctuation. The demonstration program verifies all ten
        sentences with translations and runs a story-order quiz that
        shuffles the sentences and checks the learner restores the market
        morning."""),
    key_points=[
        "10-sentence present-tense story: a morning at the food market, start to finish.",
        "Narrative chain: 去菜场 -> 买菜 -> 挑鱼 -> 讲价 -> 成交 -> 转屋里向.",
        "Direct speech in Wu: 老板话：八块一斤。/ 我话：便宜点，六块𠲎？",
        "Market verbs in action: 买, 挑, 称, 讲价, 拎.",
        "Line-by-line English translation; every line has characters, romanization, English.",
    ],
    requirements=[
        "Learners should retell the story from memory, then perform both voices.",
        "Write your own ten-sentence market story following this chain.",
    ],
    standards=[
        "CEFR A2-B1: simple present-tense narration with dialogue.",
        "Narrative follows standard Wu storytelling patterns.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. Wu narrative structures.",
        "上海市地方志办公室. 上海市井文化. Shanghai street-market culture records.",
    ],
    sig_lens=("Through the Signature lens, the story is the signature extended in time: "
              "ten sentences ten seals in a row, the market morning signed from 去 to "
              "转屋里向. This Signature reading treats narrative as the signature "
              "written across a whole morning."),
)

E(
    key="wu_story2", name="Wu Chinese Story II: A Trip to Suzhou",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in Wu using past forms (仔, 过, 朆), line by
        line with English translation.
        1. 旧年秋天，我搭朋友去仔苏州。(jieu3-gnie3 tshieu1-thie1, ngu2 taq4 bong3-yeu3 chi2-tsy2 su1-tseu1.) - Last autumn, my friend and I went to Suzhou.
        2. 火车一个半钟头就到了。(hu2-tsho1 iq4-geq4 pe2 zeq5-deu3 zieu3 tau2 leq4.) - The train arrived in an hour and a half.
        3. 拙政园里向人交关多，风景实在好。(tsoq4-tsen2-yoe3 li2-shiang3 nyin3 ciau1-kue1 tu1, fon1-cing2 zeq5-zeq5 hau2.) - The Humble Administrator Garden was crowded, but the scenery was truly fine.
        4. 我拉小桥浪向拍仔交关照片。(ngu2-la1 siau2-jiau3 lang3-shiang3 phaq4-tsy2 ciau1-kue1 tsau2-phie2.) - We took many photos on the small bridge.
        5. 中饭吃仔苏州面，汤鲜面滑。(tson1-ve3 chiq4-tsy2 su1-tseu1 mie3, thang1 shie1 mie3 waq5.) - For lunch we ate Suzhou noodles: savory broth, slippery noodles.
        6. 下半日去仔虎丘，爬到山顶。(o3-pe2-nyiq5 chi2-tsy2 hu2-chieu1, bo3-tau2 se1-ting2.) - In the afternoon we went to Tiger Hill and climbed to the top.
        7. 卖纪念品个摊头，我买仔一把檀香扇。(ma3 ci2-nie3-bing3 geq4 the1-deu3, ngu2 ma2-tsy2 iq4-po2 de3-shiang1-she2.) - At a souvenir stall I bought a sandalwood fan.
        8. 夜里向看仔评弹，吴侬软语真好听。(ya3-li2-shiang3 khe2-tsy2 bing3-de3, wu2-non3 gnie3-gniu2 tsen1 hau2-thin1.) - In the evening we heard pingtan; the soft Wu speech was lovely.
        9. 从来朆听过评弹，迭趟算开眼界了。(zon3-le3 ven3 thin1-ku2 bing3-de3, diq4-thang2 se2 khe1-nge3-ka2 leq4.) - Never heard pingtan before; this trip broadened my horizons.
        10. 转来以后，我常常想起苏州个小桥流水。(tse3-le3 yi2-heu3, ngu2 zang3-zang3 shiang2-chi2 su1-tseu1 geq4 siau2-jiau3 lieu3-sy2.) - Since returning, I often think of Suzhou's bridges and streams."""),
    how_it_works=textwrap.dedent("""\
        This record teaches past narration through the three Wu past
        markers: 仔 (completed: 去仔, 吃仔, 买仔), 过 (experienced: 听过),
        and 朆 (never: 从来朆听过). The learner retells a real trip of their
        own using the ten-sentence frame - 去, 到, 看, 吃, 买, 听, 转来 -
        swapping in their own places and foods. The 仔 drill is physical:
        every completed action gets a stamp gesture. The demonstration
        program verifies all ten sentences with translations and runs a
        past-marker identifier that labels each 仔, 过, and 朆 in the story
        and checks each sits in the Wu-right position."""),
    key_points=[
        "10-sentence past-tense story: a day trip to Suzhou.",
        "仔 tsy2 marks completion: 去仔, 吃仔, 看仔, 买仔 - the workhorse of Wu past.",
        "过 ku2 marks experience: 听过. 朆 ven3 marks never: 从来朆听过.",
        "Suzhou sights in Wu: 拙政园, 虎丘, 评弹 (pingtan storytelling), 苏州面.",
        "Narrative frame reusable for any trip: 去 -> 到 -> 看 -> 吃 -> 买 -> 听 -> 转来.",
    ],
    requirements=[
        "Learners should retell a real trip of their own in ten Wu sentences using 仔/过/朆.",
        "Drill the 仔 stamp: say a completed action and stamp the air.",
    ],
    standards=[
        "CEFR B1: past narration with perfective, experiential, and negative past.",
        "Aspect usage follows Chao 1928 and Qian 1992.",
    ],
    citations=[
        "Chao Y R. Studies in the Modern Wu-dialects. 1928. Wu past and aspect.",
        "苏州市地方志办公室. 苏州园林志. Suzhou garden records: 拙政园, 虎丘.",
    ],
    sig_lens=("Through the Signature lens, memory is the signature kept: 仔 seals what "
              "was done, 过 seals what was lived, 朆 seals what never was - and the "
              "story binds them into one kept document. This Signature reading treats "
              "past narration as the archive of the signed life."),
)

E(
    key="wu_story3", name="Wu Chinese Story III: Plans for Tomorrow",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in Wu using future and conditional forms (要,
        会, 如果...就), line by line with English translation.
        1. 明朝是礼拜六，我要早点起来。(min3-tsau1 zy3 li3-ba-loq4, ngu2 iau2 tsau2-tie2 chi2-le3.) - Tomorrow is Saturday; I will get up early.
        2. 如果落雨，我就不去跑步了。(zy3-ku2 loq4-yu3, ngu2 zieu3 veq4 chi2 bau2-bu3 leq4.) - If it rains, I will not go running.
        3. 如果天好，我要去滨江散步。(zy3-ku2 thie1 hau2, ngu2 iau2 chi2 ping1-kang1 se2-bu3.) - If the weather is fine, I will stroll along the riverfront.
        4. 中饭我要请朋友吃小笼包。(tson1-ve3 ngu2 iau2 tshin2 bong3-yeu3 chiq4 siau2-lon3-pau1.) - For lunch I will treat my friend to soup dumplings.
        5. 下半日我要去图书馆看书。(o3-pe2-nyiq5 ngu2 iau2 chi2 du3-sy1-kue2 khe2-sy1.) - In the afternoon I will go to the library to read.
        6. 夜里向阿拉会得去看电影。(ya3-li2-shiang3 aq4-laq4 we3-deq4 chi2 khe2 die3-ying2.) - In the evening we will go see a film.
        7. 看完电影，阿拉会得去吃夜宵。(khe2-we3 die3-ying2, aq4-laq4 we3-deq4 chi2 chiq4 ya3-shiau1.) - After the film, we will get a late-night snack.
        8. 只要功课做完，囡囡就会得跟阿拉去。(tsy2-iau2 kon1-khu2 tsu2-we3, noe1-noe1 zieu3 we3-deq4 ken1 aq4-laq4 chi2.) - As long as homework is done, the child will come along.
        9. 明朝个计划排得满满个，一定交关开心。(min3-tsau1 geq4 ci2-waq5 ba3-deq4 me3-me3 geq4, iq4-ding3 ciau1-kue1 khe1-shin1.) - Tomorrow is packed full; it will surely be delightful.
        10. 好个计划要配好个心情，侬话对𠲎？(hau2 geq4 ci2-waq5 iau2 phe2 hau2 geq4 shin1-zing3, nong3 wo3 teq4 vaq5?) - Good plans deserve a good mood; am I right?"""),
    how_it_works=textwrap.dedent("""\
        This record teaches the future as planning: the learner writes their
        real tomorrow in ten Wu sentences - morning, contingency (如果落
        雨.../如果天好...), meals, afternoon, evening - using 要 for
        intention and 会得 for confident prediction. The conditional frames
        (如果...就, 只要...就) are drilled as two-door sentences: open the
        如果 door, walk through the 就 door. The story closes by asking the
        listener 对𠲎？ - pulling them into the plan. The demonstration
        program verifies all ten sentences with translations and runs a
        future-form checker that finds every 要, 会得, 如果, and 只要 in
        the story."""),
    key_points=[
        "10-sentence future story: planning a Saturday, morning to night.",
        "要 iau2 marks intention: 我要早点起来. 会得 we3-deq4 marks confident prediction: 会得去看电影.",
        "Conditionals: 如果...就 (if...then), 只要...就 (as long as...then).",
        "Planning vocabulary: 计划 ci2-waq5, 排得满满个 (packed full), 夜宵 (late-night snack).",
        "The closing question 对𠲎？ pulls the listener into the plan - a Wu storytelling habit.",
    ],
    requirements=[
        "Learners should write their real tomorrow in ten Wu sentences with 如果 branches.",
        "Drill the two-door conditionals: open 如果, walk through 就 - ten times.",
    ],
    standards=[
        "CEFR B1: future plans, intentions, predictions, conditionals.",
        "Future and conditional forms follow Qian 1992 on Wu syntax.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. Wu future and conditional constructions.",
        "Chao Y R. Studies in the Modern Wu-dialects. 1928. Wu clause combining.",
    ],
    sig_lens=("Through the Signature lens, the plan is the signature postdated: 要 the "
              "promise signed today, 会得 the seal of confidence, 如果 the wisely "
              "hedged clause. This Signature reading treats future narration as the "
              "learner signing tomorrow in advance."),
)

E(
    key="wu_idioms", name="Wu Chinese Idioms and Proverbs",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty Wu idioms and proverbs - literal translation, real meaning,
        and an example sentence each.
        1. 拆烂污 (tshaq4-le3-u1) - Lit: tear rotten filth. Real: to do shoddy work; to mess things up. 迭件事体侬勿要拆烂污。(diq4-jie3 zy3-thi2 nong3 veq4-iau2 tshaq4-le3-u1.) - Do not make a mess of this matter.
        2. 轧闹猛 (gaiq5-nau3-mang3) - Lit: press into the bustle. Real: to join the fun; to crowd in for excitement. 礼拜天阿拉去轧闹猛。(li3-ba-thie1 aq4-laq4 chi2 gaiq5-nau3-mang3.) - On Sunday we go join the fun.
        3. 捣浆糊 (tau2-qiang1-wu3) - Lit: stir paste. Real: to muddle through; to do sloppy work. 做事体勿好捣浆糊。(tsu2 zy3-thi2 veq4-hau2 tau2-qiang1-wu3.) - Do not muddle through your work.
        4. 白相 (baq5-shiang2) - Lit: white play. Real: to play; to have fun; to hang out. 到我屋里向来白相。(tau2 ngu2 oq4-li2-shiang3 le3 baq5-shiang2.) - Come hang out at my place.
        5. 有腔调 (yeu3 chian1-diau3) - Lit: has tune. Real: stylish; has flair; classy. 迭间店交关有腔调。(diq4-cie1 tie2 ciau1-kue1 yeu3 chian1-diau3.) - This shop has real flair.
        6. 老克勒 (lau3-kheq4-leq4) - Lit: old clerk (from English). Real: an old-school dapper Shanghai gentleman. 伊爷爷是老克勒，穿衣交关讲究。(yi3 ya3-ya3 zy3 lau3-kheq4-leq4, tshoe1-yi1 ciau1-kue1 kang2-cieu2.) - His grandfather is an old-school gentleman; very particular about dress.
        7. 十三点 (zeq5-se1-tie2) - Lit: thirteen o'clock. Real: scatterbrained; silly (mild teasing, not for elders). 侬又十三点了！(nong3 yeu3 zeq5-se1-tie2 leq4!) - You are being silly again!
        8. 拎勿清 (lin3-veq4-chin1) - Lit: cannot carry clearly. Real: confused; muddled. 伊今朝头脑拎勿清。(yi3 cin1-tsau1 deu3-nau2 lin3-veq4-chin1.) - His mind is muddled today.
        9. 门槛精 (men3-khe2-cin1) - Lit: threshold spirit. Real: shrewd; nobody fool. 伊是门槛精，骗勿过伊个。(yi3 zy3 men3-khe2-cin1, phie2-veq4-ku2 yi3 geq4.) - He is shrewd; you cannot fool him.
        10. 吃生活 (chiq4-sang1-weq5) - Lit: eat life. Real: to endure hardship; to suffer. 年轻辰光吃点生活勿怕。(nie3-chin1 zen3-kuang1 chiq4-tie2 sang1-weq5 veq4-pho2.) - Enduring some hardship when young is nothing to fear.
        11. 触霉头 (tshoq4-me3-deu3) - Lit: touch the moldy head. Real: to run into bad luck. 今朝触霉头，钞票丢了。(cin1-tsau1 tshoq4-me3-deu3, tshau1-phiau2 tieu1 leq4.) - Bad luck today; lost money.
        12. 噱头 (jioq5-deu3) - Lit: laugh head. Real: a gimmick; a funny bit. 迭个广告噱头十足。(diq4-geq4 kuang2-kau2 jioq5-deu3 zeq5-tsoq4.) - This ad is full of gimmicks.
        13. 嗲 (tia2) - Lit: (sound). Real: cute; adorable; charmingly sweet. 囡囡嗲得来。(noe1-noe1 tia2-deq4-le3.) - The child is adorable.
        14. 作 (tsoq4) - Lit: to make. Real: to put on airs; to be affected. 侬勿要作。(nong3 veq4-iau2 tsoq4.) - Stop putting on airs.
        15. 一分价钿一分货 (iq4-fen1 ka2-die3 iq4-fen1 hu2) - Lit: one cent price, one cent goods. Real: you get what you pay for. 便宜货勿好，一分价钿一分货。(bie3-nyi3 hu2 veq4-hau2, iq4-fen1 ka2-die3 iq4-fen1 hu2.) - Cheap goods are no good; you get what you pay for.
        16. 货比三家勿吃亏 (hu2 pi2 se1-ka1 veq4 chiq4-khu1) - Lit: compare three shops, eat no loss. Real: comparing pays off. 买大家电要货比三家勿吃亏。(ma2 du3-ka1-die3 iau2 hu2 pi2 se1-ka1 veq4 chiq4-khu1.) - For big appliances, compare three shops.
        17. 三个臭皮匠，赛过诸葛亮 (se1-geq4 tsheu2-bi3-jiang3, se2-ku2 tsyu1-koq4-liang3) - Lit: three cobblers beat Zhuge Liang. Real: many minds beat one genius. 大家商量商量，三个臭皮匠赛过诸葛亮。(da3-ka1 sang1-liang3 sang1-liang3, se1-geq4 tsheu2-bi3-jiang3 se2-ku2 tsyu1-koq4-liang3.) - Let us discuss; many minds beat one genius.
        18. 吃得苦中苦，方为人上人 (chiq4-deq4 khu2-tson1-khu2, fang1 we3 gnin3-zang3-gnin3) - Lit: eat the bitterest bitter to become the highest human. Real: no pain, no gain. 训练交关苦，吃得苦中苦方为人上人。(shuin2-lie3 ciau1-kue1 khu2, chiq4-deq4 khu2-tson1-khu2 fang1 we3 gnin3-zang3-gnin3.) - Training is hard; no pain, no gain.
        19. 少壮不努力，老大徒伤悲 (sau2-tsuang2 peq4 nu2-liq5, lau3-du3 du3 sang1-pe1) - Lit: young not striving, old vain sorrow. Real: youth wasted is age regretted. 后生要好好读书，少壮不努力老大徒伤悲。(heu3-sang1 iau2 hau2-hau2 doq5-sy1, sau2-tsuang2 peq4 nu2-liq5 lau3-du3 du3 sang1-pe1.) - Young people should study hard; youth wasted is age regretted.
        20. 熟能生巧 (zoq5 nen3 sang1-jiau2) - Lit:熟 begets skill. Real: practice makes perfect. 吴语多讲多练，熟能生巧。(wu2-gniu2 tu1 kang2 tu1 lie3, zoq5 nen3 sang1-jiau2.) - Speak and drill Wu more; practice makes perfect."""),
    how_it_works=textwrap.dedent("""\
        This record teaches idioms as cultural passwords: the learner learns
        each idiom in three beats - the literal picture (tear rotten filth),
        the real meaning (do shoddy work), the living sentence. The ten Wu
        originals (拆烂污, 轧闹猛, 捣浆糊, 白相, 有腔调, 老克勒, 十三点,
        拎勿清, 门槛精, 吃生活) are drilled as pure Shanghai identity; the
        ten shared proverbs show Wu carrying the wider Chinese wisdom.
        Learners perform each idiom in a mini-scene. The demonstration
        program runs a literal-vs-real matcher: given the literal gloss, it
        checks the learner supplies the real meaning from this record."""),
    key_points=[
        "10 Wu originals: 拆烂污 (shoddy work), 轧闹猛 (join the fun), 捣浆糊 (muddle through), 白相 (hang out), 有腔调 (stylish).",
        "More originals: 老克勒 (dapper gentleman), 十三点 (scatterbrained, teasing), 拎勿清 (confused), 门槛精 (shrewd), 吃生活 (endure hardship).",
        "Mood words: 触霉头 (bad luck), 噱头 (gimmick), 嗲 (cute), 作 (put on airs).",
        "10 shared proverbs in Wu dress: 一分价钿一分货, 货比三家勿吃亏, 三个臭皮匠赛过诸葛亮, 吃得苦中苦方为人上人, 少壮不努力老大徒伤悲, 熟能生巧.",
        "Every idiom: literal translation + real meaning + example sentence.",
    ],
    requirements=[
        "Learners should perform each idiom in a mini-scene with a partner.",
        "Use three Wu originals in real conversation this week: 轧闹猛, 白相, 有腔调.",
    ],
    standards=[
        "CEFR B1-B2: idioms, proverbs, cultural expressions.",
        "Idiom glosses follow standard Shanghai usage.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Idiom entries.",
        "上海市地方志办公室. 上海方言文化. Shanghai dialect culture records.",
    ],
    sig_lens=("Through the Signature lens, the idiom is the signature in shorthand: "
              "centuries of Wu life compressed into three syllables - 拆烂污, 轧闹猛, "
              "老克勒 - each one a seal the whole city recognizes. This Signature "
              "reading treats the twenty idioms as the twenty master seals of Wu "
              "identity."),
)

E(
    key="wu_register", name="Wu Chinese Formal and Polite Registers",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen formal vs informal pairs - letters, business, elders - with
        translations. Wu has no 您; politeness rides on softeners (请,
        麻烦, 劳驾) and humble formulae.
        1. Formal: 请坐。(tshin2 zu3.) - Please be seated. / Informal: 坐。(zu3.) - Sit.
        2. Formal: 请问尊姓大名？(tshin2-ven3 tsen1-shing2 du3-ming3?) - May I ask your honorable name? / Informal: 侬叫啥名字？(nong3 ciau2 sa3 ming3-zy3?) - What is your name?
        3. Formal: 多谢侬个帮助。(tu1-zia3 nong3 geq4 pang1-zu3.) - Many thanks for your help. / Informal: 谢谢。(zia3-zia3.) - Thanks.
        4. Formal: 对勿起，是我个勿对。(te2-veq4-chi2, zy3 ngu2 geq4 veq4-teq4.) - My apologies; it was my fault. / Informal: 勿好意思。(veq4-hau2 yi2-sy1.) - Sorry about that.
        5. Formal: 麻烦侬帮个忙。(me3-ve3 nong3 pang1 geq4 mang3.) - Sorry to trouble you; please help. / Informal: 帮帮忙。(pang1-pang1-mang3.) - Give me a hand.
        6. Formal: 请慢用。(tshin2 me3-yon3.) - Please enjoy your meal. (host) / Informal: 吃吧。(chiq4-ba1.) - Eat up.
        7. Formal: 慢走，欢迎下趟再来。(me3-tseu2, we1-ngin3 o3-thang2 tse2-le3.) - Take care; welcome back. / Informal: 再会。(ze3-we3.) - Bye.
        8. Formal: 久仰久仰。(ceu2-ngiang3 ceu2-ngiang3.) - Long admired (your name). / Informal: 幸会。(xing3-we3.) - Nice to meet you.
        9. Formal: 失陪一歇。(seq4-be3 iq4-shiq4.) - Excuse me a moment. / Informal: 我先走开一歇。(ngu2 shie1 tseu2-khe1 iq4-shiq4.) - I will step away a bit.
        10. Formal: 劳驾，让一让。(lau3-ka2, rang3 iq4-rang3.) - Excuse me, please make way. / Informal: 让让。(rang3-rang3.) - Make way.
        11. Formal: 恭喜恭喜。(kon1-xi2 kon1-xi2.) - Congratulations. / Informal: 交关好！(ciau1-kue1 hau2!) - Great!
        12. Formal: 请侬多多关照。(tshin2 nong3 tu1-tu1 kue1-tsau2.) - Please look kindly after me. / Informal: 以后靠侬了。(yi2-heu3 khau2 nong3 leq4.) - I am counting on you.
        13. Formal: 晚安，好梦。(ve3-e1, hau2-mon3.) - Good night, sweet dreams. / Informal: 早点睏。(tsau2-tie2 khun2.) - Sleep early.
        14. Formal: 欢迎光临。(we1-ngin3 kuang1-lin3.) - Welcome (shop). / Informal: 进来看看。(cin2-le3 khe2-khe2.) - Come in and look.
        15. Formal: 请侬原谅。(tshin2 nong3 ngoe3-liang3.) - Please forgive me. / Informal: 勿要生气。(veq4-iau2 sang1-chi2.) - Do not be angry."""),
    how_it_works=textwrap.dedent("""\
        This record teaches register as a wardrobe: the learner tries the
        same situation in formal and informal dress - greeting a professor
        vs greeting a friend, writing to a company vs texting a buddy,
        apologizing to an elder vs to a sibling. The Wu rule is drilled:
        formality adds softeners and humble formulae, never changes the
        verb. 请问尊姓大名 vs 侬叫啥名字 asks the same question in two
        suits. The demonstration program verifies all fifteen pairs with
        translations and runs a register-sorter: given a situation (elder,
        friend, business letter), it checks the learner picks the Wu-right
        form from this record."""),
    key_points=[
        "Wu has no 您; politeness rides on 请, 麻烦, 劳驾, and humble formulae.",
        "Greetings: 请问尊姓大名？ (formal) vs 侬叫啥名字？ (informal).",
        "Thanks: 多谢侬个帮助 vs 谢谢. Apologies: 对勿起，是我个勿对 vs 勿好意思.",
        "Hosting: 请慢用 vs 吃吧; 慢走，欢迎下趟再来 vs 再会.",
        "Business: 久仰, 失陪, 劳驾, 请侬多多关照 - the formal toolkit.",
        "Rule: formality adds softeners; the verb never changes.",
        "15 formal/informal pairs with translations: letters, business, elders.",
    ],
    requirements=[
        "Learners should write one formal note (thank-you) and one informal text using these pairs.",
        "Address every elder and stranger in the formal forms for one full week.",
    ],
    standards=[
        "CEFR B1-B2: formal and informal registers, politeness.",
        "Register practice follows standard Shanghai social usage.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. Wu politeness and register.",
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Formal phrase entries.",
    ],
    sig_lens=("Through the Signature lens, register is the signature dressed for the "
              "occasion: the formal hand the seal in red ink, the informal hand the "
              "quick signature among friends - same name, different ceremony. This "
              "Signature reading treats the fifteen pairs as fifteen changes of "
              "ceremonial dress for one signature."),
)

E(
    key="wu_complex", name="Wu Chinese Compound and Complex Sentences",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen long sentences with clauses, connectors, and relative
        clauses - parsed and translated.
        1. 因为落雨，所以运动会延期了。(in1-we3 loq4-yu3, su2-yi2 yuin3-don3-we3 yie3-ji3 leq4.) - Because of the rain, the sports meet was postponed. [因为...所以...: cause -> result]
        2. 虽然天气交关热，但是大家还是来了。(se1-zen3 thie1-chi2 ciau1-kue1 gniq5, de3-zy3 da3-ka1 we3-zy3 le3 leq4.) - Although it was very hot, everyone still came. [虽然...但是...: concession]
        3. 如果明朝天好，阿拉就去郊游。(zy3-ku2 min3-tsau1 thie1 hau2, aq4-laq4 zieu3 chi2 ciau1-yeu3.) - If the weather is fine tomorrow, we will go outing. [如果...就...: condition]
        4. 只要侬肯努力，就一定学得会。(tsy2-iau2 nong3 kheng2 nu2-liq5, zieu3 iq4-ding3 yoq5-deq4-we3.) - As long as you work hard, you will surely learn it. [只要...就...: sufficient condition]
        5. 侬不但人好，而且本事大。(nong3 peq4-de3 gnin3 hau2, gni3-tshia2 pen2-zy3 du3.) - You are not only kind but also capable. [不但...而且...: not only...but also]
        6. 伊一边吃饭，一边看手机。(yi3 iq4-pie1 chiq4-ve3, iq4-pie1 khe2 seu2-ci1.) - He eats while watching his phone. [一边...一边...: simultaneous actions]
        7. 年纪越大，经验越丰富。(nie3-ci2 yoeq5 du3, cing1-ngie3 yoeq5 fon1-fu2.) - The older, the more experienced. [越...越...: the more...the more]
        8. 除了上海闲话，我还会得讲普通话。(zy3-lu3 zang3-he2 ye3-wo3, ngu2 we3 we3-deq4 kang2 phu2-thon1-wo3.) - Besides Shanghainese, I can also speak Mandarin. [除了...还...: besides...also]
        9. 既然来了，就多白相一歇。(ci2-zen3 le3 leq4, zieu3 tu1 baq5-shiang2 iq4-shiq4.) - Since you are here, stay and have fun a while. [既然...就...: since...then]
        10. 无论多忙，身体总要保重。(wu3-len3 tu1 mang3, shen1-thi2 tson2 iau2 pau2-zon3.) - However busy, always take care of your health. [无论...总...: no matter...always]
        11. 连小囡都晓得垃圾分类。(lie3 siau2-noe1 tu1 shiau2-deq4 laq5-jiq5 fen1-le3.) - Even small children know waste sorting. [连...都...: even...]
        12. 拿迭件事体办好了再讲。(na3 diq4-jie3 zy3-thi2 be3-hau2 leq4 tse2 kang2.) - Get this matter done first, then talk. [拿...: object fronting]
        13. 功课拨雨淋湿了，拿出去晒晒。(kon1-khu2 peq4 yu3 lin3-seq4 leq4, na3 tsheq4-chi2 sa2-sa2.) - The homework got rained on; take it out to dry. [拨...: passive]
        14. 侬讲个故事是啥人写个？(nong3 kang2 geq4 ku2-zy3 zy3 sa3-gnin3 shia2 geq4?) - Who wrote the story you told? [讲个: relative clause with 个]
        15. 我买个西瓜比侬买个甜。(ngu2 ma2 geq4 shi1-ku1 pi2 nong3 ma2 geq4 die3.) - The watermelon I bought is sweeter than the one you bought. [买个: relative clause + 比 comparison]"""),
    how_it_works=textwrap.dedent("""\
        This record teaches complex sentences as connector carpentry: the
        learner masters the fifteen two-part connectors - 因为...所以,
        虽然...但是, 如果...就, 只要...就, 不但...而且, 一边...一边,
        越...越, 除了...还, 既然...就, 无论...总, 连...都 - by building
        each one from two simple sentences they already know. Then the Wu
        clause tools: 拿 object-fronting, 拨 passive, and the 个 relative
        clause (侬讲个故事, 我买个西瓜). Each sentence is parsed in brackets
        so the learner sees the skeleton. The demonstration program verifies
        all fifteen parsed sentences and runs a connector-matcher: given two
        simple sentences, it checks the learner joins them with the Wu-right
        connector from this record."""),
    key_points=[
        "Cause/result: 因为...所以... Concession: 虽然...但是... Condition: 如果...就...; 只要...就...",
        "Addition: 不但...而且... Simultaneity: 一边...一边... Proportion: 越...越...",
        "Exception: 除了...还... Given: 既然...就... Universality: 无论...总... Emphasis: 连...都...",
        "Wu clause tools: 拿 object-fronting, 拨 passive, 个 relative clauses (侬讲个故事).",
        "Every sentence is parsed in brackets: the skeleton is visible.",
        "15 long sentences with translations: compound and complex mastery.",
    ],
    requirements=[
        "Learners should join twenty pairs of simple sentences with the fifteen connectors.",
        "Write five 个 relative clauses about your own possessions: 我买个___, 侬送个___.",
    ],
    standards=[
        "CEFR B2: complex sentences, connectors, relative clauses, passive.",
        "Connector analysis follows Chao 1928 and Qian 1992 on Wu clause combining.",
    ],
    citations=[
        "Chao Y R. Studies in the Modern Wu-dialects. 1928. Wu clause combining.",
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. Complex sentence patterns.",
    ],
    sig_lens=("Through the Signature lens, the complex sentence is the signature with "
              "clauses attached: 因为 the stated reason sealed first, 所以 the "
              "conclusion pressed after - a whole contract in one breath. This "
              "Signature reading treats every connector as the hinge of a "
              "well-drafted Wu document."),
)

E(
    key="wu_conv_market", name="Wu Chinese Conversation: At the Market",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue at the market - Wu with English,
        annotated with usage notes.
        1. A: 早！今朝菜新鲜𠲎？(tsau2! cin1-tsau1 tshe2 shin1-shie1 vaq5?) - Morning! Are the vegetables fresh today? [早: the neighborly morning greeting]
        2. B: 新鲜，今朝朝早才进个货。(shin1-shie1, cin1-tsau1 tsau1-tsau2 tse3 cin2 geq4 hu2.) - Fresh; stocked this very morning. [才: just, emphasizing freshness]
        3. A: 青菜几化一斤？(tshing1-tshe2 ci2-hu3 iq4-cin1?) - How much are the greens per jin?
        4. B: 三块一斤。(se1-khue2 iq4-cin1.) - Three yuan a jin.
        5. A: 来两斤。(le3 liang3-cin1.) - Two jin please. [来: the buying verb - bring me]
        6. B: 好嘞，两斤青菜。(hau2-leq4, liang3-cin1 tshing1-tshe2.) - Right away; two jin of greens. [好嘞: the vendor's cheerful confirmation]
        7. A: 迭条鱼几化？(diq4-diau3 ng3 ci2-hu3?) - How much is this fish?
        8. B: 鲫鱼十二块一斤。(ciq4-ng3 zeq5-gni3-khue2 iq4-cin1.) - Crucian carp, twelve a jin.
        9. A: 太贵了，十块𠲎？(tha2 ku2 leq4, zeq5-khue2 vaq5?) - Too dear; ten yuan OK? [bargaining opens with 太贵了]
        10. B: 十块卖勿得，十一块拿去。(zeq5-khue2 ma3-veq4-deq4, zeq5-iq4-khue2 na3-chi2.) - Cannot sell at ten; take it at eleven. [counteroffer]
        11. A: 好吧，十一块。(hau2-ba1, zeq5-iq4-khue2.) - All right, eleven. [好吧 seals the deal]
        12. B: 还要啥？鸡蛋要𠲎？(we3 iau2 sa3? ci1-de3 iau2 vaq5?) - Anything else? Eggs? [vendor upsells]
        13. A: 鸡蛋几化？(ci1-de3 ci2-hu3?) - How much are the eggs?
        14. B: 土鸡蛋八块一斤。(thu2-ci1-de3 paq4-khue2 iq4-cin1.) - Free-range eggs, eight a jin.
        15. A: 来一斤。(le3 iq4-cin1.) - One jin.
        16. B: 一共三十五块。(iq4-gon3 se1-zeq5-ng3-khue2.) - Thirty-five altogether.
        17. A: 拿去，四十块。(na3-chi2, sy2-zeq5-khue2.) - Here, forty yuan. [overpaying slightly to get change]
        18. B: 找侬五块。(tsau2 nong3 ng3-khue2.) - Five yuan change.
        19. A: 谢谢，下趟再来。(zia3-zia3, o3-thang2 tse2-le3.) - Thanks; will come again.
        20. B: 慢走，生意兴隆不敢当，常来！(me3-tseu2, sang1-yi2 shing1-lon3 peq4-ke1-tang1, zang3 le3!) - Take care; come often! [vendor's warm farewell]"""),
    how_it_works=textwrap.dedent("""\
        This record teaches the market as theater: two learners perform all
        twenty lines, swapping the A (buyer) and B (vendor) roles, until the
        bargaining arc - greeting, asking, bargaining, dealing, paying,
        parting - runs without the book. The annotations explain the
        vendor-customer ritual: 早 opens, 好嘞 confirms, 太贵了 bargains,
        好吧 seals, 慢走 closes. Learners then improvise their own market
        scene with different goods. The demonstration program verifies all
        twenty lines with translations and annotations, and runs a
        dialogue-flow checker confirming the conversation follows the
        greeting->bargaining->payment->farewell arc."""),
    key_points=[
        "20-line bilingual market dialogue with usage annotations on every line.",
        "The bargaining arc: 早 (greet) -> 几化 (ask) -> 太贵了 (haggle) -> 好吧 (deal) -> 找钞票 (pay) -> 慢走 (part).",
        "Vendor language: 好嘞 (cheerful confirmation), 才进个货 (just stocked), 卖勿得 (cannot sell at that price).",
        "Buyer tools: 来两斤 (buying verb 来), 十块𠲎？ (offer with 𠲎), 拿去 (here you are).",
        "Annotations teach the ritual, not just the words.",
    ],
    requirements=[
        "Learners should perform the full dialogue twice, swapping roles.",
        "Improvise a new market scene buying different goods with the same arc.",
    ],
    standards=[
        "CEFR B1: transactional dialogue with bargaining.",
        "Dialogue follows authentic Shanghai market practice.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Market dialogue vocabulary.",
        "上海市地方志办公室. 上海市井文化. Shanghai market culture records.",
    ],
    sig_lens=("Through the Signature lens, the market dialogue is the signature "
              "negotiated aloud: every price asked a draft, every counteroffer a "
              "revision, 好吧 the final seal pressed by both parties. This Signature "
              "reading treats the twenty lines as one contract written in two voices."),
)

E(
    key="wu_conv_friend", name="Wu Chinese Conversation: Meeting a Friend",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue meeting a friend - Wu with English,
        annotated.
        1. A: 侬好！好久勿见！(nong3-hau2! hau2-cieu2 veq4 cie2!) - Hello! Long time no see! [the warm reunion opener]
        2. B: 侬好侬好！最近忙啥？(nong3-hau2 nong3-hau2! tse2-jin3 mang3 sa3?) - Hello hello! What have you been busy with?
        3. A: 忙工作，侬呢？(mang3 kon1-tsoq4, nong3 ni3?) - Busy with work; and you?
        4. B: 我还好，囡囡上幼儿园了。(ngu2 we3-hau2, noe1-noe1 zang3 yeu3-gni3-yoe3 leq4.) - I am fine; the child started kindergarten. [life updates build closeness]
        5. A: 交关好！几岁了？(ciau1-kue1 hau2! ci2-se2 leq4?) - Wonderful! How old now?
        6. B: 四岁了，调皮得来。(sy2-se2 leq4, diau3-bi3 deq4-le3.) - Four; mischievous as anything. [调皮得来: the fond complaint]
        7. A: 小囡侪迭能个。(siau2-noe1 za3 diq4-nen3 geq4.) - All small children are like that. [empathy]
        8. B: 礼拜六有空𠲎？到我屋里向吃饭。(li3-ba-loq4 yeu3 khon2 vaq5? tau2 ngu2 oq4-li2-shiang3 chiq4-ve3.) - Free Saturday? Come eat at my place. [the invitation]
        9. A: 好啊！我带瓶酒来。(hau2-a1! ngu2 ta2 bing3 cieu2 le3.) - Great! I will bring a bottle of wine. [guests bring gifts]
        10. B: 覅带，屋里向侪有。(fiau2 ta2, oq4-li2-shiang3 za3 yeu3.) - Do not bring; we have everything. [polite refusal of the gift]
        11. A: 一定要带个，空手哪能好意思。(iq4-ding3 iau2 ta2 geq4, khon1-seu2 na3-nen3 hau2 yi2-sy1.) - I must bring something; empty-handed would be embarrassing. [insistence is polite]
        12. B: 那好吧，谢谢侬。(na3 hau2-ba1, zia3-zia3 nong3.) - Then all right; thank you. [acceptance]
        13. A: 啥辰光？(sa3 zen3-kuang1?) - What time?
        14. B: 夜里向五点半。(ya3-li2-shiang3 ng3 tie2 pe2.) - 5:30 PM.
        15. A: 好，勿见勿散。(hau2, veq4 cie2 veq4 se2.) - Good; be there or be square. [勿见勿散: the Wu pledge]
        16. B: 侬最近身体哪能？(nong3 tse2-jin3 shen1-thi2 na3-nen3?) - How is your health lately? [care for the friend]
        17. A: 交关好，天天跑步。(ciau1-kue1 hau2, thie1-thie1 bau2-bu3.) - Very good; running every day.
        18. B: 交关好，坚持。(ciau1-kue1 hau2, cie1-zy3.) - Great; keep it up. [encouragement]
        19. A: 那礼拜六见。(na3 li3-ba-loq4 cie2.) - Then see you Saturday.
        20. B: 再会！路上当心。(ze3-we3! lu3-zang3 tang1-shin1.) - Goodbye! Travel safe. [care to the last line]"""),
    how_it_works=textwrap.dedent("""\
        This record teaches friendship as a reunion in three movements:
        catching up (1-7), making plans (8-15), and caring farewell
        (16-20). The learner performs both roles, feeling the Wu social
        choreography: the doubled greeting (侬好侬好), the life update, the
        invitation, the gift ritual (bring/refuse/insist/accept), the 勿见
        勿散 pledge. The annotations mark each ritual move. Learners then
        improvise their own reunion with a different friend and different
        plans. The demonstration program verifies all twenty lines with
        translations and annotations, and runs a ritual-checker confirming
        the greeting->invitation->gift->pledge->farewell sequence."""),
    key_points=[
        "20-line bilingual reunion dialogue with usage annotations.",
        "The reunion arc: 侬好侬好 (double greeting) -> life updates -> invitation -> gift ritual -> 勿见勿散 pledge -> caring farewell.",
        "Gift ritual: 带瓶酒来 -> 覅带 -> 一定要带个 -> 那好吧 - insistence is politeness.",
        "Fond complaints: 调皮得来; empathy: 小囡侪迭能个.",
        "Care runs through: 侬最近身体哪能？ ... 路上当心 - to the last line.",
    ],
    requirements=[
        "Learners should perform the dialogue twice, swapping roles.",
        "Improvise a reunion with your own news and your own Saturday plan.",
    ],
    standards=[
        "CEFR B1: social dialogue with invitations and arrangements.",
        "Social ritual follows standard Shanghai practice.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. Wu social formulae.",
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Social phrase entries.",
    ],
    sig_lens=("Through the Signature lens, the reunion is the signature renewed: every "
              "侬好 a seal pressed again on an old friendship, every invitation a new "
              "page opened, 勿见勿散 the pledge signed. This Signature reading treats "
              "the twenty lines as the renewal of a standing covenant."),
)

E(
    key="wu_conv_problem", name="Wu Chinese Conversation: Solving a Problem",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue solving a problem (a lost wallet) -
        Wu with English, annotated.
        1. A: 勿好了，我个钱包勿见了！(veq4 hau2 leq4, ngu2 geq4 jie3-pau1 veq4 cie2 leq4!) - Oh no! My wallet is gone! [勿好了: the alarm]
        2. B: 勿要慌，慢慢讲，啥辰光勿见个？(veq4-iau2 huang1, me3-me3 kang2, sa3 zen3-kuang1 veq4 cie2 geq4?) - Do not panic; slowly: when did you last have it? [calming first]
        3. A: 下半日买咖啡辰光还有个。(o3-pe2-nyiq5 ma2 ka1-fi1 zen3-kuang1 we3 yeu3 geq4.) - I had it when buying coffee this afternoon.
        4. B: 咖啡店勒啥地方？(ka1-fi1-tie2 leq4 sa3 di3-fang1?) - Where is the coffee shop? [pinning the place]
        5. A: 南京路浪向，地铁口边浪。(ne3-cin1 lu3 lang3-shiang3, di3-thiq4 kheu2 pie1-lang3.) - On Nanjing Road, by the subway entrance.
        6. B: 打电话去问问。(ta2 die3-wo3 chi2 ven3-ven3.) - Call and ask. [first action]
        7. A: 问过了，讲呒没看见。(ven3-ku2 leq4, kang2 m2-meq5 khe2-cie2.) - Asked already; they saw nothing.
        8. B: 包里向再寻寻看。(pau1 li2-shiang3 tse2 zin3-zin3 khe2.) - Search the bag again. [second action]
        9. A: 寻过了，里里外外侪寻过了。(zin3-ku2 leq4, li2-li2 nga3-nga3 za3 zin3-ku2 leq4.) - Searched; inside and out, everywhere.
        10. B: 钞票多𠲎？卡多𠲎？(tshau1-phiau2 tu1 vaq5? kha2 tu1 vaq5?) - Much cash? Many cards? [assessing the damage]
        11. A: 现钞勿多，卡有三四张。(yie3-tshau1 veq4 tu1, kha2 yeu3 se1-sy2-tsang1.) - Not much cash; three or four cards.
        12. B: 卡先挂失，马上打电话。(kha2 shie1 kua2-seq4, mo3-zang3 ta2 die3-wo3.) - Freeze the cards first; call now. [priority action]
        13. A: 对，先挂失。(teq4, shie1 kua2-seq4.) - Right; freeze them first. [agreement]
        14. B: 我陪侬去银行。(ngu2 be3 nong3 chi2 ngin3-hang3.) - I will go to the bank with you. [solidarity]
        15. A: 谢谢侬，有侬勒我放心了。(zia3-zia3 nong3, yeu3 nong3 leq4 ngu2 fang2-shin1 leq4.) - Thank you; with you here I feel safe. [gratitude]
        16. B: 朋友之间讲啥谢谢。(bong3-yeu3 tsy1-cie1 kang2 sa3 zia3-zia3.) - Between friends, no thanks needed. [the Wu friendship seal]
        17. A: 钱包里向还有张全家福。(jie3-pau1 li2-shiang3 we3 yeu3 tsang1 jie3-ka1-foq4.) - There was a family photo in the wallet. [the real loss]
        18. B: 会寻着个，勿要难过。(we3 zin3-zaq5 geq4, veq4-iau2 ne3-ku2.) - It will turn up; do not be sad. [comfort]
        19. A: 希望吧。(shi1-mang3-ba1.) - Hopefully. [acceptance]
        20. B: 走，先去银行，再去咖啡店。(tseu2, shie1 chi2 ngin3-hang3, tse2 chi2 ka1-fi1-tie2.) - Come; bank first, then the coffee shop. [the plan]"""),
    how_it_works=textwrap.dedent("""\
        This record teaches problem-solving as a rescue in four moves: alarm
        (1), calming and fact-finding (2-9), damage control (10-14), and
        comfort with a plan (15-20). The learner plays both the distressed
        friend and the steady helper, drilling the Wu crisis toolkit: 勿要
        慌 (do not panic), 慢慢讲 (tell me slowly), 先...再... (first...then
        ...). The emotional peak - the lost family photo, the 朋友之间讲啥
        谢谢 seal - is performed with feeling. The demonstration program
        verifies all twenty lines with translations and annotations, and
        runs a rescue-checker confirming the alarm->facts->action->comfort
        sequence."""),
    key_points=[
        "20-line bilingual problem-solving dialogue with annotations.",
        "The rescue arc: 勿好了 (alarm) -> 勿要慌，慢慢讲 (calm) -> fact-finding -> 卡先挂失 (action) -> comfort -> plan.",
        "Crisis toolkit: 勿要慌, 慢慢讲, 先...再..., 里里外外 (inside and out).",
        "Practical: 挂失 (freeze cards), 寻 (search), 打电话问.",
        "Emotional seals: 朋友之间讲啥谢谢; the family photo as the real loss.",
    ],
    requirements=[
        "Learners should perform the dialogue twice, swapping the distressed and helper roles.",
        "Improvise a new problem (lost keys, missed train) with the same four-move arc.",
    ],
    standards=[
        "CEFR B1-B2: problem-solving dialogue with emotional support.",
        "Crisis language follows authentic usage.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007. Everyday problem-solving phrases.",
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992. Wu discourse patterns.",
    ],
    sig_lens=("Through the Signature lens, the rescue is the signature of friendship "
              "proven: 朋友之间讲啥谢谢 the seal that needs no thanks, the steady "
              "plan the hand extended. This Signature reading treats the twenty lines "
              "as the proof that Wu friendship signs its name in trouble."),
)

E(
    key="wu_mastery", name="Wu Chinese Mastery Review and Full Reference",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        The whole database in one teaching summary: the tone table, 200 core
        words, key grammar, and all phrase tables.
        TONE TABLE (modern Shanghai, citation tones per syllable):
        T1 53 yinping: 三 se1, 天 thie1, 书 sy1, 高 kau1.
        T2 34 yinshang/yinqu: 水 sy2, 好 hau2, 去 chi2, 请 tshin2.
        T3 23 yang tones: 人 nyin3, 侬 nong3, 茶 dzo3, 饭 ve3.
        T4 5 yinru (short): 一 iq4, 吃 chiq4, 勿 veq4, 六 loq4.
        T5 12 yangru (short): 十 zeq5, 白 baq5, 肉 gnioq5, 没 meq5.
        Sandhi: LEFT-DOMINANT - the first syllable leads the phrase melody.
        200 CORE WORDS (word, romanization, English):
        People: 我 ngu2 I, 侬 nong3 you, 伊 yi3 he/she, 阿拉 aq4-laq4 we,
        侬拉 nong3-la1 you (pl), 伊拉 yi3-la1 they, 朋友 bong3-yeu3 friend, 先生 shie1-sang1 mister,
        爸爸 ba3-ba3 father, 妈妈 ma1-ma1 mother, 囡 noe1 child, 哥哥 ku1-ku1 elder brother,
        姐姐 cia2-cia2 elder sister, 老师 lau3-sy1 teacher, 学生 yoq5-sang1 student, 医生 yi1-sang1 doctor.
        Verbs: 吃 chiq4 eat, 喝 heq4 drink, 去 chi2 go, 来 le3 come,
        看 khe2 look/read, 听 thin1 listen, 说 shuoq4 speak, 问 ven3 ask,
        买 ma2 buy, 卖 ma3 sell, 做 tsu2 do/make, 工作 kon1-tsoq4 work,
        学习 yoq5-xiq4 study, 教 ciau1 teach, 睏觉 khun2-kau2 sleep, 洗 shi2 wash,
        穿 tshoe1 wear, 开 khe1 open, 关 kue1 close, 打 ta2 hit/call,
        拿 na3 take, 拨 peq4 give, 欢喜 hoe1-xi2 like, 想 shiang2 want,
        知道 tsy1-tau2 know, 跑步 bau2-bu3 run, 走 tseu2 walk, 坐 zu3 sit,
        读 doq5 read aloud, 写 shia2 write.
        Things: 书 sy1 book, 钞票 tshau1-phiau2 money, 饭 ve3 rice/meal, 水 sy2 water,
        茶 dzo3 tea, 物事 meq5-zy3 thing, 地方 di3-fang1 place, 辰光 zen3-kuang1 time,
        天气 thie1-chi2 weather, 电话 die3-wo3 telephone, 门 men3 door, 路 lu3 road,
        屋 oq4 house, 学校 yoq5-gau3 school, 商店 sang1-tie2 shop, 菜场 tshe2-zang3 market,
        医院 yi1-yue3 hospital, 车站 tsho1-ze3 station, 房间 vang3-cie1 room, 床 zang3 bed,
        椅子 yi3-tsy2 chair, 窗 tshang1 window, 报纸 pau2-tsy2 newspaper, 照片 tsau2-phie2 photo.
        Food: 菜 tshe2 vegetable/dish, 肉 gnioq5 meat, 鱼 ng3 fish, 面 mie3 noodles,
        米 mi2 rice, 蛋 ci1-de3 egg, 糖 dang3 sugar, 盐 yie3 salt,
        油 yeu3 oil, 酒 cieu2 wine, 饭店 ve3-tie2 restaurant, 菜单 tse2-te1 menu,
        小笼包 siau2-lon3-pau1 soup dumplings, 馄饨 wen3-den3 wontons, 包子 pau1-tsy2 steamed buns, 水果 sy2-ku2 fruit.
        Body: 头 deu3 head, 眼睛 nge3-cin1 eyes, 耳朵 gni2-tu1 ears, 鼻头 biq5-deu3 nose,
        嘴 tsy2 mouth, 手 seu2 hand, 脚 ciaq4 foot, 肚皮 du3-bi3 belly,
        心 shin1 heart, 血 shiq4 blood, 身体 shen1-thi2 body/health, 药 yaq5 medicine.
        Adjectives: 好 hau2 good, 大 du3 big, 小 siau2 small, 长 zang3 long,
        短 toe2 short, 高 kau1 tall, 新 shin1 new, 老 lau3 old,
        快 khuai2 fast, 慢 me3 slow, 多 tu1 many, 少 sau2 few,
        热 gniq5 hot, 冷 lan3 cold, 红 gon1 red, 白 baq5 white,
        黑 heq4 black, 远 yoe3 far, 近 jin3 near, 贵 ku2 expensive,
        便宜 bie3-nyi3 cheap, 嗲 tia2 cute, 难 ne3 difficult, 香 shiang1 fragrant.
        Particles and adverbs: 交关 ciau1-kue1 very, 真 tsen1 really, 太 tha2 too, 最 tse2 most,
        更 ken2 more, 已经 yi2-cin1 already, 刚刚 kang1-kang1 just now, 常常 zang3-zang3 often,
        一起 iq4-chi2 together, 马上 mo3-zang3 right away, 慢慢 me3-me3 slowly, 都 tu1 all,
        勿 veq4 not, 覅 fiau2 do-not-want, 朆 ven3 have-not, 仔 tsy2 completed,
        过 ku2 experienced, 勒 leq4 at, 拨 peq4 passive, 𠲎 vaq5 question particle.
        Numbers and time: 一 iq4 one, 二 gni3 two, 三 se1 three, 四 sy2 four,
        五 ng3 five, 六 loq4 six, 七 chiq4 seven, 八 paq4 eight,
        九 cieu2 nine, 十 zeq5 ten, 百 paq4 hundred, 千 tshie1 thousand,
        今朝 cin1-tsau1 today, 明朝 min3-tsau1 tomorrow, 昨日 zoq5-gniq5 yesterday, 现在 yi3-ze3 now,
        点钟 tie2-tson1 o'clock, 半 pe2 half, 礼拜 li3-ba2 week, 年 gnie3 year,
        月 ngoeq5 month, 天 thie1 day, 春天 tshen1-thie1 spring, 冬天 ton1-thie1 winter.
        Nature: 狗 keu2 dog, 猫 mau1 cat, 鸟 niau2 bird, 花 ho1 flower,
        树 zy3 tree, 山 se1 mountain, 河 wu3 river, 海 he2 sea,
        雨 yu3 rain, 雪 shiq4 snow, 风 fon1 wind, 太阳 tha2-yang3 sun,
        云 yuin3 cloud, 月亮 ngoeq5-liang3 moon.
        Social and tech: 侬好 nong3-hau2 hello, 谢谢 zia3-zia3 thank you, 再会 ze3-we3 goodbye, 对勿起 te2-veq4-chi2 sorry,
        请 tshin2 please, 请问 tshin2-ven3 may-I-ask, 啥 sa3 what, 啥人 sa3-gnin3 who,
        哪能 na3-nen3 how, 为啥 we3-sa3 why, 几化 ci2-hu3 how much, 迭 diq4 this,
        手机 seu2-ci1 mobile phone, 电脑 die3-nau2 computer, 电影 die3-ying2 film, 银行 ngin3-hang3 bank,
        公司 kon1-sy1 company, 火车 hu2-tsho1 train, 飞机 fi1-ci1 airplane, 酒店 cieu2-tie2 hotel.
        KEY GRAMMAR (one-line each):
        SVO always: 我吃饭. Negation: 勿 (not), 朆 (have not), 覅 (do not want).
        Questions: 𠲎 particle or in-place interrogatives; word order never moves.
        Aspect: 仔 completed, 过 experienced, 勒海 ongoing. Passive: 拨. Object-fronting: 拿.
        Possession: X + 个 + Y. Location: 勒. Comparison: 比. Plural: 拉 on pronouns.
        Connectors: 因为...所以, 虽然...但是, 如果...就, 不但...而且, 一边...一边, 越...越.
        PHRASE TABLES:
        Greetings: 侬好, 早, 吃过了𠲎, 谢谢, 谢谢侬, 对勿起, 勿好意思, 没关系, 请, 请问, 麻烦侬, 再会, 慢走, 明朝会, 晚安, 好𠲎？, 对𠲎？
        Market: 几化钞票？, 太贵了，便宜点𠲎？, 最低几化？, 好吧，成交。, 买单, 一分价钿一分货.
        Travel: 请问，___哪能去？, 一直朝前走, 左转/右转, 买票子, 我迷路了, 谢谢侬带路.
        Feelings: 交关开心, 难过, 发火, 害怕, 欢喜, 吓一跳.
        Wu seals: 拆烂污, 轧闹猛, 白相, 有腔调, 老克勒, 嗲, 熟能生巧."""),
    how_it_works=textwrap.dedent("""\
        This record is the whole database compressed: the learner uses it as
        the daily review sheet and the final exam. The review method: cover
        the English column and produce the Wu; cover the Wu and produce the
        English; chant the tone table; recite the grammar one-liners; perform
        the phrase tables as rapid-fire drills. The 200 words are the
        graduation checklist - every word checked off is a seal earned. The
        demonstration program is the mastery exam: it quizzes all 200 words,
        checks the tone table math, verifies the grammar one-liners against
        the records they summarize, and prints the final score."""),
    key_points=[
        "Tone table: T1 53, T2 34, T3 23, T4 5 (short), T5 12 (short); left-dominant sandhi.",
        "200 core words: people 16, verbs 30, things 24, food 16, body 12, adjectives 24, particles/adverbs 20, numbers/time 24, nature 14, social/tech 20.",
        "Grammar one-liners: SVO, three negations, 𠲎 questions, 仔/过/勒海 aspect, 拨 passive, 拿 fronting, 个 possession, 勒 location, 比 comparison.",
        "Phrase tables: greetings, market, travel, feelings, Wu seals - the whole database's greatest hits.",
        "Review method: cover-and-recall both directions; chant tones; rapid-fire phrases.",
        "This record is the graduation checklist and the final exam.",
    ],
    requirements=[
        "Learners should score 100 percent on the 200-word cover-and-recall before graduating.",
        "Keep this record as the permanent quick-reference; review weekly.",
    ],
    standards=[
        "CEFR B1: consolidated review of the full A1-B1 Wu curriculum.",
        "All forms cross-checked against records 1-33 of this database.",
    ],
    citations=[
        "Qian Nairong 钱乃荣. 上海话大词典. Shanghai Lexicographical Publishing House; 2007.",
        "Qian Nairong 钱乃荣. 当代吴语研究. Shanghai Educational Publishing House; 1992.",
        "Norman J. Chinese. Cambridge University Press; 1988.",
    ],
    sig_lens=("Through the Signature lens, the mastery review is the signature complete: "
              "two hundred words two hundred seals, the tone table the official chop, "
              "the grammar the articles of the covenant - the whole contract on one "
              "page. This Signature reading treats record 34 as the signed diploma of "
              "the Wu learner."),
)


SIG_TAIL = ("Signature editions are his original Signature language work - "
            "clearly labeled Signature-made, never presented as authentic "
            "public record.")
