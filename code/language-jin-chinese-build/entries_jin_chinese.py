#!/usr/bin/env python3
"""Entries for the Jin Chinese Language databases (34 ladder-ordered records).

Public records: real, fact-checked Jin Chinese linguistics (Taiyuan dialect
of the Bingzhou group as the reference standard) - tones with the preserved
entering tone, phonology, core vocabulary, grammar, themed sentence sets,
stories, idioms, registers, complex sentences, conversations, mastery
reference; every record carrying Chinese characters with romanization and
English translation plus example sentences, organized in the Signature
system.

Romanization used throughout: a practical pinyin-style teaching
romanization with tone numbers. Tone numbers map to the Taiyuan tone
categories: 1 = 11 level (yinping; the old yangping has merged into this
tone), 2 = 53 (shangsheng), 3 = 45 (qusheng), 4 = entering tone, a short
syllable ending in a glottal stop, written with a trailing ʔ. Citation tones
are given per syllable. This is a teaching romanization defined here for
learners, and is not a historical missionary system. Recent phonetic work
describes the same five categories with slightly different values (ISCA
2024: 31, 52, 35, entering 41ʔ and 31ʔ); the classical values are used here
because they are the widely-cited textbook set.

Sources harvested: Li Rong 李荣 (1985) Jin proposal; Language Atlas of China
(1987; 2nd ed. Chinese Academy of Social Sciences, Commercial Press, 2012)
- 8 subgroups, 63.05 million speakers (2012); Norman J. Chinese (Cambridge,
1988); Hou Jingyi 侯精一 & Shen Ming 沈明 (2002) 现代汉语方言概论; Yan M.M.
(2006) Introduction to Chinese Dialectology, LINCOM; Kurpaska M. (2010)
Chinese Language(s), de Gruyter; Ethnologue: Jin Chinese [cjy], ISO 639-3;
Qiao Quansheng 乔全生 on Jin research; ISCA Speech Prosody 2024 Taiyuan tone
perception study.
"""
import textwrap

ENTRIES = []


def E(**kw):
    ENTRIES.append(kw)
    return kw


E(
    key="jin_overview", name="Jin Chinese Language Overview",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Jin Chinese (晋语, tɕin3-y1) is a Sinitic language within
        Sino-Tibetan, spoken natively by about 63 million people - roughly
        the population of a large European country. Its heartland is most of
        Shanxi province (except the lower Fen River valley), with adjoining
        areas in northern Shaanxi, western Hebei, northern Henan, and central
        Inner Mongolia (including Hohhot and Baotou). Jin is also called
        Shanxi speech (山西话, ʂan1-xi1-hua3). Jin is not an official language
        anywhere; Mandarin (Putonghua) holds official status, and Jin lives in
        homes, markets, noodle shops, and local stages. ISO 639-3 gives Jin
        the code cjy (there is no ISO 639-1 code); Glottolog: jiny1235. The
        family path is Sino-Tibetan > Sinitic > Jin. Until the 1980s Jin was
        counted as Mandarin; in 1985 the linguist Li Rong 李荣 proposed it as
        a separate top-level group like Yue or Wu, and the Language Atlas of
        China (1987) made it official. His main criterion was the entering
        tone: Jin alone among northern Chinese languages keeps the old
        checked syllables as a separate tone class, still ending in a glottal
        stop ʔ - the sound that split Jin from Mandarin. The Atlas divides
        Jin into 8 subgroups: Bingzhou 并州 (central Shanxi, including
        Taiyuan), Lüliang 吕梁 (western Shanxi, northern Shaanxi), Shangdang
        上党 (southeastern Shanxi, Changzhi), Wutai 五台 (northern Shanxi,
        central Inner Mongolia), Datong-Baotou 大包 (northern Shanxi,
        Baotou), Zhangjiakou-Hohhot 张呼 (northwestern Hebei, Hohhot),
        Handan-Xinxiang 邯新 (southeastern Shanxi, southern Hebei, northern
        Henan), and Zhidan-Yanchuan 志延 (northern Shaanxi). The Taiyuan
        dialect of the Bingzhou group is the reference standard of this
        database. This record is the map of the whole ladder: from a first
        你好 (niə2-hau3, hello) in Taiyuan to full conversation."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the overview by anchoring every fact in a sentence
        the learner can say. Each fact - the native name 晋语, the ISO code
        cjy, the Sino-Tibetan family path, the 63 million speakers, the
        Shanxi-centered heartland, the 8 subgroups, the 1985 Li Rong split,
        the entering-tone signature - appears with a plain English
        explanation and a Jin example sentence in characters, romanization,
        and English. The learner reads the facts, then repeats the sentences,
        so the overview becomes spoken language from the first record. Later
        records climb the teaching ladder: foundations (records 1-10:
        writing, sounds, words, grammar basics), compounded (records 11-20:
        themed sentence sets), advanced (records 21-34: tenses, questions,
        stories, idioms, registers, complex sentences, conversations, and a
        full mastery reference)."""),
    key_points=[
        "Native name: 晋语 (tɕin3-y1); English name: Jin Chinese; also called 山西话 Shanxi speech; ISO 639-3: cjy; no ISO 639-1 code.",
        "Family: Sino-Tibetan > Sinitic > Jin; about 63 million native speakers (2012 survey).",
        "Heartland: most of Shanxi, plus northern Shaanxi, western Hebei, northern Henan, central Inner Mongolia.",
        "Not official anywhere; Mandarin is the official language. Jin is the language of home, market, and noodle shop.",
        "Split from Mandarin in 1985: Li Rong proposed Jin as a separate top-level group; the Language Atlas of China (1987) adopted it.",
        "The diagnostic trait: the entering tone 入声 is preserved as a separate class with a final glottal stop ʔ - Mandarin merged it away.",
        "Eight subgroups: Bingzhou 并州, Lüliang 吕梁, Shangdang 上党, Wutai 五台, Datong-Baotou 大包, Zhangjiakou-Hohhot 张呼, Handan-Xinxiang 邯新, Zhidan-Yanchuan 志延.",
        "Reference standard of this database: the Taiyuan dialect (Bingzhou group), capital of Shanxi. Example: 你好 niə2-hau3, hello in Taiyuan.",
        "Every record in this database carries Chinese characters, romanization, and English on every line.",
    ],
    requirements=[
        "No prior knowledge of Jin is needed; this is the starting record of the ladder.",
        "Learners should read each example sentence aloud to begin training Jin pronunciation from day one.",
    ],
    standards=[
        "ISO 639-3:2007 (cjy) language code for Jin Chinese.",
        "Ethnologue: Jin Chinese [cjy] - Sino-Tibetan, Sinitic, Jin.",
    ],
    citations=[
        "Li Rong 李荣. 1985. Proposal of Jin as a separate top-level dialect group, adopted in the Language Atlas of China (1987).",
        "Chinese Academy of Social Sciences. 中国语言地图集(第2版):汉语方言卷 [Language Atlas of China, 2nd ed.]. Commercial Press; 2012. 8 Jin subgroups; 63.05 million speakers.",
        "Norman J. Chinese. Cambridge University Press; 1988. Classification of the Sinitic groups.",
        "Eberhard D M, Simons G F, Fennig C D, editors. Ethnologue: Languages of the World. SIL International; 2024. Entry: Jin Chinese [cjy].",
    ],
    sig_lens=("Through the Signature lens, a language is not a school subject - it is a "
              "living contract between a people and their home ground, and Jin is one of "
              "the great signed contracts of northern China: sixty-three million voices "
              "in Shanxi and beyond keeping the old entering tone like a seal pressed "
              "into every checked syllable. This Signature reading treats the overview "
              "as the first seal of that contract."),
)

E(
    key="jin_writing", name="Jin Chinese Writing System",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Jin is written with Chinese characters - the same script as Mandarin,
        written left to right in modern texts (older texts run top to bottom,
        right to left). There is no separate Jin alphabet: the writing system
        IS the character system, and Jin has its own beloved vernacular words
        that Mandarin writes differently or not at all. Learn these and Jin
        texts open up: 圪 (kəʔ4, the famous Jin derivational prefix), 甚
        (ʂən2, what - Shanxi says 甚 where Mandarin says 什么), 夜来
        (ie3-lai2, yesterday), 不赖 (puʔ4-lai3, not bad, good), 圪蛋
        (kəʔ4-tan3, egg), 入 (zuʔ4, the Jin prefix as in 入鬼 fool around),
        窟窿 (kʰuʔ4-luŋ1, hole, from 孔 by the Jin l-fission rule). Numerals
        are the standard characters with Jin readings: 一 (iəʔ4), 二 (ər3),
        三 (san1), 四 (sɿ3), 五 (u3), 六 (liəuʔ4), 七 (tsʰiəʔ4), 八 (paʔ4), 九
        (tɕiəu3), 十 (səʔ4), 百 (paʔ4), 千 (tsʰien1), 万 (uan3). Note how 一,
        六, 七, 八, 十, 百 are short checked syllables - the preserved
        entering tone made visible in the numerals. Punctuation follows modern
        Chinese practice: 。for the period, ，for the comma, ？for questions,
        ！for exclamations, 、for list pauses, 《》for book titles. Digits
        0-9 are used for Arabic numerals exactly as in Mandarin. Because Jin
        shares the character script with Mandarin, a reader of Chinese can
        sound out Jin texts immediately - the characters are familiar, only
        the readings and the vernacular words are new."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the writing system by pairing every Jin-vernacular
        word with its romanization, its Mandarin equivalent where one exists,
        and an English gloss, then drilling the ten numerals with their Jin
        readings - including the entering-tone readings 一 iəʔ4, 六 liəuʔ4,
        七 tsʰiəʔ4, 八 paʔ4, 十 səʔ4. The learner copies the vernacular words
        by hand - 圪, 甚, 夜来, 不赖, 圪蛋, 入, 窟窿 - writes each numeral
        1-10 with its reading, and practices the punctuation marks by
        punctuating a short Jin paragraph. Because the script is shared with
        Mandarin, this one record converts existing character knowledge into
        Jin reading power."""),
    key_points=[
        "Script: Chinese characters, left to right (older texts: top to bottom, right to left). No separate Jin alphabet.",
        "Vernacular words: 圪 kəʔ4 (prefix), 甚 ʂən2 (what), 夜来 ie3-lai2 (yesterday), 不赖 puʔ4-lai3 (good), 圪蛋 kəʔ4-tan3 (egg), 入 zuʔ4 (prefix), 窟窿 kʰuʔ4-luŋ1 (hole).",
        "Numerals: 一 iəʔ4, 二 ər3, 三 san1, 四 sɿ3, 五 u3, 六 liəuʔ4, 七 tsʰiəʔ4, 八 paʔ4, 九 tɕiəu3, 十 səʔ4, 百 paʔ4, 千 tsʰien1, 万 uan3.",
        "The numerals show the entering tone in action: 一, 六, 七, 八, 十, 百 are short checked syllables ending in ʔ.",
        "Punctuation: 。，？！、。 Digits 0-9 as in Mandarin.",
        "A Mandarin reader already knows the script; Jin adds vernacular words and new readings.",
    ],
    requirements=[
        "Learners should hand-write the seven core vernacular items (圪甚夜来不赖圪蛋入窟窿) with readings.",
        "Drill the numerals 1-10 aloud until the Jin readings (iəʔ4, ər3, san1...) come without thinking.",
    ],
    standards=[
        "Modern written Chinese character standard (simplified in mainland publications).",
        "Numeral and punctuation practice follows standard modern Chinese typography.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002. Jin phonology and the entering tone.",
        "Kurpaska M. Chinese Language(s): A Look Through the Prism of The Great Dictionary of Modern Chinese Dialects. de Gruyter; 2010. Jin features, pp. 68, 74-75.",
    ],
    sig_lens=("Through the Signature lens, the character is the first covenant of the "
              "written word: one script shared by a whole civilization, with Jin keeping "
              "its own vernacular seals - 圪, 甚, 夜来 - stamped beside the classical "
              "forms, and the entering tone living on in the very numerals."),
)

E(
    key="jin_phonology", name="Jin Chinese Pronunciation and Phonology",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Jin pronunciation is built on five citation tone categories (Taiyuan
        reference): Tone 1 = 11, a low level tone (yinping; the old yangping
        has merged into it - so 人 man and 三 mountain-height words share one
        level tone); Tone 2 = 53, a high falling tone (shangsheng - 好 hau2
        good); Tone 3 = 45, a high rising tone (qusheng - 大 ta3 big); Tone 4
        = the entering tone, a short syllable ending in a glottal stop ʔ (一
        iəʔ4 one, 十 səʔ4 ten, 吃 tsʰəʔ4 to eat, 喝 xəʔ4 to drink). This
        entering tone is the sound that made Jin a language: Mandarin lost it
        centuries ago, Jin kept it. Recent phonetic work (ISCA 2024) describes
        the same five categories as 31, 52, 35, and two checked tones 41ʔ and
        31ʔ, confirming the checked syllables as a separate class. The
        initials are close to Mandarin: b p m f, d t n l, g k h, z c s, zh ch
        sh r, j q x - plus the famous retained 疑母 ŋ- (我 ŋəʔ4 I, a sound
        Mandarin lost). Finals include the checked set ending in ʔ. Tone
        sandhi in Jin is famously complex: sandhi rules depend on the
        grammatical structure - an adjective-noun compound changes tones
        differently from a verb-object compound - and some tones that merge
        in isolation split apart again in sandhi. Ten spoken examples to
        drill: 三 san1 three, 水 ʂui2 water, 好 hau2 good, 大 ta3 big, 人
        zən1 person, 一 iəʔ4 one, 十 səʔ4 ten, 吃 tsʰəʔ4 to eat, 喝 xəʔ4 to
        drink, 太原 tʰai3-yøn2 Taiyuan."""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronunciation as a drill system. First the five
        tone categories with hand-on-throat practice for the entering tone -
        say 一 iəʔ4 and feel the glottal stop cut the syllable short, then
        compare 吃 tsʰəʔ4 with Mandarin chi to hear what Mandarin lost. Then
        the ŋ- initial: 我 ŋəʔ4 starts in the back of the throat like the end
        of English 'sing'. Then the ten example words are drilled in minimal
        sets (三/水/好/大 for the four smooth tones; 一/十/吃/喝 for the
        checked tone) until the learner can produce each category on demand.
        Sandhi is introduced as a listening skill: the same word changes tone
        by grammatical position, so learners drill two-word phrases in both
        adjective-noun and verb-object frames."""),
    key_points=[
        "Five citation tones (Taiyuan): 1 = 11 level (yinping; yangping merged in), 2 = 53 falling (shangsheng), 3 = 45 rising (qusheng), 4 = entering tone, short with final ʔ.",
        "The entering tone is Jin's signature: 一 iəʔ4, 十 səʔ4, 吃 tsʰəʔ4, 喝 xəʔ4 - syllables Mandarin pronounces long, Jin clips with a glottal stop.",
        "Recent phonetic work (ISCA 2024) confirms five contrastive tones in Taiyuan with two checked (ʔ-final) entering tones.",
        "Retained ŋ- initial: 我 ŋəʔ4 (I) - a sound Mandarin lost centuries ago.",
        "Tone sandhi is grammar-dependent: adjective-noun compounds and verb-object compounds follow different tone-change rules.",
        "Drill set: 三 san1, 水 ʂui2, 好 hau2, 大 ta3, 人 zən1, 一 iəʔ4, 十 səʔ4, 吃 tsʰəʔ4, 喝 xəʔ4, 太原 tʰai3-yøn2.",
    ],
    requirements=[
        "Learners must be able to produce the glottal stop in 一 iəʔ4 and 吃 tsʰəʔ4 before moving on.",
        "Practice the ŋ- initial in 我 ŋəʔ4 daily until it is automatic.",
    ],
    standards=[
        "Tone values follow the classical Taiyuan description (11, 53, 45, entering ʔ), with the ISCA 2024 phonetic values noted.",
        "IPA symbols used for the initials and the glottal stop ʔ follow standard phonetic transcription.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002. Taiyuan tone system and the entering tone.",
        "Liao et al. Perception of the Merging Tones in Taiyuan Jin Chinese. ISCA Speech Prosody; 2024. Five contrastive tones including two ʔ-final entering tones.",
        "Yan M.M. Introduction to Chinese Dialectology. LINCOM Europa; 2006. Jin as a separate group, pp. 60-61, 67-69.",
    ],
    sig_lens=("Through the Signature lens, the entering tone is the seal of Jin itself: "
              "where Mandarin let the old checked syllables dissolve, Jin pressed the "
              "glottal stop into every one - 一, 吃, 喝 - and signed its independence "
              "in sound. Every ʔ is a signature."),
)

E(
    key="jin_nouns", name="Jin Chinese Core Nouns I",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Twenty-five essential Jin nouns - people, places, and things - each
        with the Taiyuan teaching romanization, English, and an example
        sentence in characters, romanization, and English. 人 zən1 person: 这
        个人很好 (tsəʔ4-kə3 zən1 xən2-hau2, this person is very good). 娃娃
        ua3-ua3 child - Shanxi's warm word for a little one: 娃娃在睡觉
        (ua3-ua3 tsai3 ʂui3-tɕiau3, the child is sleeping). 朋友 pʰəŋ1-iəu3
        friend, 房子 faŋ1-tsɿ house, 学校 xɿəʔ4-xiau3 school, 书 ʂu1 book, 钱
        tsʰien1 money, 饭 fan3 rice/meal, 水 ʂui2 water, 茶 tsʰa1 tea, 东西
        tuŋ1-xi1 thing, 地方 ti3-faŋ1 place, 爸爸 pa3-pa? (pa4-pa), 妈妈
        ma1-ma, 老师 lau2-ʂɿ1 teacher, 学生 xɿəʔ4-ʂəŋ1 student, 商店 ʂaŋ1-tien3
        shop, 医院 i1-yøn3 hospital, 火车 xu1-tsʰə1 train, 汽车 tsʰi3-tsʰə1
        car, 电视 tien3-ʂɿ3 television, 电话 tien3-hua3 telephone, 门 mən2
        door, 路 lu3 road, 城 tsʰəŋ2 city, 村 tsʰun1 village. Each noun is a
        building block: learn the word, say the sentence, and the noun is
        yours. Note the entering tones hiding in 学校 (xɿəʔ4) - even everyday
        words carry the Jin seal."""),
    how_it_works=textwrap.dedent("""\
        This record teaches nouns by the say-it-three-ways method: every noun
        appears as character + romanization + English, then inside a full
        sentence with all three lines. The learner covers the English column,
        reads the Jin aloud, and uncovers to check - a flashcard drill built
        into the page. The twenty-five nouns are grouped (people, home,
        school, food, town) so memory hooks form naturally. The demo program
        quizzes twelve anchor nouns and asserts the score, so the learner can
        run it and prove the words are learned."""),
    key_points=[
        "人 zən1 (person): 这个人很好 tsəʔ4-kə3 zən1 xən2-hau2 - this person is very good.",
        "娃娃 ua3-ua3 (child): 娃娃在睡觉 ua3-ua3 tsai3 ʂui3-tɕiau3 - the child is sleeping.",
        "朋友 pʰəŋ1-iəu3 (friend): 他是我的朋友 tʰa1 ʂɿ3 uə2-tiəʔ4 pʰəŋ1-iəu3 - he is my friend.",
        "房子 faŋ1-tsɿ (house): 这房子很大 tsəʔ4 faŋ1-tsɿ xən2-ta3 - this house is very big.",
        "学校 xɿəʔ4-xiau3 (school): 学校在城里 xɿəʔ4-xiau3 tsai3 tsʰəŋ2-li2 - the school is in the city.",
        "书 ʂu1 (book): 这本书好看 tsəʔ4-pən2 ʂu1 hau2-kʰan3 - this book is good to read.",
        "钱 tsʰien1 (money): 我没有钱 uə2 mei2-iəu2 tsʰien1 - I have no money.",
        "饭 fan3 (rice/meal): 吃饭了 tsʰəʔ4-fan3-lə - time to eat (dinner is ready).",
        "水 ʂui2 (water): 喝水 xəʔ4-ʂui2 - drink water.",
        "茶 tsʰa1 (tea): 喝茶 xəʔ4-tsʰa1 - drink tea.",
        "东西 tuŋ1-xi1 (thing): 这是甚东西 tsəʔ4 ʂɿ3 ʂən2 tuŋ1-xi1 - what is this thing?",
        "地方 ti3-faŋ1 (place): 这个地方好 tsəʔ4-kə3 ti3-faŋ1 hau2 - this place is good.",
        "Also: 爸爸 (father), 妈妈 (mother), 老师 (teacher), 学生 (student), 商店 (shop), 医院 (hospital), 火车 (train), 汽车 (car), 电视 (television), 电话 (telephone), 门 (door), 路 (road), 城 (city).",
    ],
    requirements=[
        "Say every noun aloud with its tone number before reading the sentence.",
        "Run the demo quiz and score 12/12 before moving to verbs.",
    ],
    standards=[
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
        "Example sentences use standard SVO order shared across Sinitic languages.",
    ],
    citations=[
        "Qiao Quansheng 乔全生. 晋方言研究的历史、现状与未来. On Jin research; notes Taiyuan vocabulary is close to Mandarin dialects.",
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002. Jin lexicon overview.",
    ],
    sig_lens=("Through the Signature lens, every noun is a named thing sealed with a "
              "tone: 人, 娃娃, 朋友 - the people-words of Shanxi carry the entering "
              "tone in their school (xɿəʔ4) and their meals (fan3), and naming them "
              "aloud is the first act of the covenant."),
)

E(
    key="jin_verbs", name="Jin Chinese Core Verbs I",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Twenty-five essential Jin verbs - each with the Taiyuan teaching
        romanization, English, and an example sentence in characters,
        romanization, and English. 吃 tsʰəʔ4 to eat - the entering tone in
        the most daily verb: 我吃饭 uə2 tsʰəʔ4-fan3 (I eat). 喝 xəʔ4 to
        drink: 喝水 xəʔ4-ʂui2 (drink water). 去 tsʰɿ3 to go: 我去太原 uə2
        tsʰɿ3 tʰai3-yøn2 (I go to Taiyuan). 来 lai1 to come: 你来 ni2 lai1
        (you come). 看 kʰan3 to look/read: 看书 kʰan3-ʂu1 (read a book). 买
        mai2 to buy: 买东西 mai2 tuŋ1-xi1 (buy things). 卖 mai3 to sell: 他卖
        菜 tʰa1 mai3 tsʰai3 (he sells vegetables). 做 tsu3 to do/make: 做饭
        tsu3-fan3 (cook). 拿 na1 to take: 拿来 na1-lai1 (bring it here). 给
        kei3 to give: 给我 kei3-uə2 (give me). 喜欢 xi1-huan1 to like: 我喜欢
        你 uə2 xi1-huan1 ni2 (I like you). 知道 tsɿ1-tau3 to know: 我知道
        uə2 tsɿ1-tau3 (I know). 说 ʂuə1 to say, 听 tʰiŋ1 to listen, 走 tsəu2
        to walk, 跑 pʰau2 to run, 睡 ʂui3 to sleep, 起 tsʰi2 to rise, 坐 tsu3
        to sit, 站 tsan3 to stand, 笑 xiau3 to laugh, 哭 kʰu1 to cry, 问
        uən3 to ask, 学 xɿəʔ4 to learn, 教 tɕiau1 to teach. Verbs are the
        engine of every Jin sentence - master these twenty-five and you can
        move through a Shanxi day."""),
    how_it_works=textwrap.dedent("""\
        This record teaches verbs inside real sentences, never alone. Each
        verb gets one model sentence showing its natural frame: 吃 with 饭,
        去 with a destination, 给 with a recipient. The learner reads the Jin
        line aloud, checks the English, then makes one personal sentence with
        the same verb (我喝甚? - what do I drink?). The entering-tone verbs
        (吃 tsʰəʔ4, 喝 xəʔ4, 学 xɿəʔ4) are drilled as a set so the glottal stop
        becomes muscle memory. The demo quizzes twelve anchor verbs with a
        perfect-score assertion."""),
    key_points=[
        "吃 tsʰəʔ4 (to eat): 我吃饭 uə2 tsʰəʔ4-fan3 - I eat.",
        "喝 xəʔ4 (to drink): 喝水 xəʔ4-ʂui2 - drink water.",
        "去 tsʰɿ3 (to go): 我去太原 uə2 tsʰɿ3 tʰai3-yøn2 - I go to Taiyuan.",
        "来 lai1 (to come): 你来 ni2 lai1 - you come.",
        "看 kʰan3 (to look/read): 看书 kʰan3-ʂu1 - read a book.",
        "买 mai2 (to buy): 买东西 mai2 tuŋ1-xi1 - buy things.",
        "卖 mai3 (to sell): 他卖菜 tʰa1 mai3 tsʰai3 - he sells vegetables.",
        "做 tsu3 (to do/make): 做饭 tsu3-fan3 - cook a meal.",
        "拿 na1 (to take): 拿来 na1-lai1 - bring it here.",
        "给 kei3 (to give): 给我 kei3-uə2 - give it to me.",
        "喜欢 xi1-huan1 (to like): 我喜欢你 uə2 xi1-huan1 ni2 - I like you.",
        "知道 tsɿ1-tau3 (to know): 我知道 uə2 tsɿ1-tau3 - I know.",
        "Also: 说 (say), 听 (listen), 走 (walk), 跑 (run), 睡 (sleep), 起 (rise), 坐 (sit), 站 (stand), 笑 (laugh), 哭 (cry), 问 (ask), 学 (learn), 教 (teach).",
    ],
    requirements=[
        "Make one personal sentence per verb before moving on.",
        "Drill the entering-tone verbs (吃, 喝, 学) until the ʔ is automatic.",
    ],
    standards=[
        "Verb frames follow standard Sinitic SVO patterns.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002. Jin verb system and aspect markers.",
        "Kurpaska M. Chinese Language(s). de Gruyter; 2010. Jin grammatical features.",
    ],
    sig_lens=("Through the Signature lens, verbs are actions sealed in sound: 吃 and "
              "喝 carry the entering tone because eating and drinking are the oldest "
              "human acts, and Jin refuses to let them go soft. To speak a Jin verb "
              "is to sign the action with your throat."),
)

E(
    key="jin_adjectives", name="Jin Chinese Adjectives and Adverbs",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Twenty-five adjectives and fifteen adverbs of Jin, each with the
        Taiyuan teaching romanization, English, and an example sentence. 好
        hau3 good: 很好 xən2-hau3 (very good). 大 ta3 big: 房子很大 faŋ1-tsɿ
        xən2-ta3 (the house is very big). 小 siau2 small, 快 kʰuai3 fast,
        慢 man3 slow, 热 zəʔ4 hot (entering tone - feel the ʔ), 冷 ləŋ2 cold,
        贵 kui3 expensive, 便宜 pʰien1-i1 cheap, 不赖 puʔ4-lai3 not bad -
        Shanxi's favorite compliment: 这刀削面不赖 tsəʔ4 tau1-xiau1-mien3
        puʔ4-lai3 (these knife-cut noodles are good). 远 yøn2 far, 近 tɕin3
        near, 高 kau1 tall, 矮 ai2 short, 长 tsʰaŋ2 long, 短 tuan2 short,
        新 xin1 new, 旧 tɕiəu3 old, 多 tu1 many, 少 ʂau2 few, 干净 kan1-tɕiŋ3
        clean, 漂亮 pʰiau3-liaŋ1 pretty, 聪明 tsʰuŋ1-miŋ1 smart, 老 lau2 old
        (of age), 年轻 nien2-tsʰiŋ1 young. Adverbs: 很 xən2 very, 太 tʰai3
        too, 都 tu1 all, 也 ie2 also, 就 tɕiəu3 then/just, 才 tsʰai2 only
        then, 还 xai2 still, 已经 i2-tɕiŋ1 already, 正在 tsəŋ3-tsai3 in
        progress, 常常 tsʰaŋ2-tsʰaŋ2 often, 慢慢 man3-man3 slowly, 快快
        kʰuai3-kʰuai3 quickly, 一起 iəʔ4-tsʰi2 together, 一点儿 iəʔ4-tier2 a
        little, 非常 fei1-tsʰaŋ2 extremely. Jin adjectives need no agreement -
        no gender, no number, no cases: 好 is 好 for every person and every
        thing, which makes Jin adjectives wonderfully simple after European
        languages. Intensify with 很, 太, or reduplication (慢慢儿)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches description as a game: take a noun from the noun
        record, add an adjective from this record, and make a true sentence
        about your world (我的房子大 - my house is big). The adverb set is
        taught as sentence seasoning - 很, 太, 都, 也, 就 - sprinkled into
        sentences the learner already knows. 不赖 gets special attention as
        the Shanxi signature compliment: learners practice deploying it the
        way locals do, after food. The demo quizzes twelve anchor
        adjectives/adverbs with a perfect-score assertion."""),
    key_points=[
        "好 hau3 (good): 很好 xən2-hau3 - very good.",
        "大 ta3 (big): 房子很大 faŋ1-tsɿ xən2-ta3 - the house is very big.",
        "小 siau2 (small): 小娃娃 siau2 ua3-ua3 - a small child.",
        "快 kʰuai3 (fast): 跑得快 pʰau2-təʔ4 kʰuai3 - runs fast.",
        "慢 man3 (slow): 慢点儿 man3-tier2 - a bit slower.",
        "热 zəʔ4 (hot): 水很热 ʂui2 xən2-zəʔ4 - the water is very hot.",
        "冷 ləŋ2 (cold): 夜来冷 ie3-lai2 ləŋ2 - yesterday was cold.",
        "贵 kui3 (expensive): 太贵了 tʰai3-kui3-lə - too expensive.",
        "便宜 pʰien1-i1 (cheap): 很便宜 xən2 pʰien1-i1 - very cheap.",
        "不赖 puʔ4-lai3 (not bad, good): 这刀削面不赖 tsəʔ4 tau1-xiau1-mien3 puʔ4-lai3 - these noodles are good.",
        "很 xən2 (very): 很好 xən2-hau3 - very good.",
        "远 yøn2 (far): 很远 xən2-yøn2 - very far.",
        "Also: 近 (near), 高 (tall), 矮 (short), 长 (long), 短 (short), 新 (new), 旧 (old), 多 (many), 少 (few), 干净 (clean), 漂亮 (pretty), 聪明 (smart), 老 (old), 年轻 (young); adverbs 太, 都, 也, 就, 才, 还, 已经, 正在, 常常, 慢慢, 快快, 一起, 一点儿, 非常.",
        "No agreement: Jin adjectives never change for gender, number, or case.",
    ],
    requirements=[
        "Describe five things in your room using 好/大/小/新/旧 before moving on.",
        "Use 不赖 in a food compliment the Shanxi way.",
    ],
    standards=[
        "Adjective predicates follow the Sinitic pattern (no copula needed: 房子大).",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002. Jin adjectival predicates.",
        "Yan M.M. Introduction to Chinese Dialectology. LINCOM Europa; 2006. Jin grammar sketch.",
    ],
    sig_lens=("Through the Signature lens, adjectives are judgments sealed with "
              "breath: 不赖 is Shanxi's handshake-word, a whole philosophy of "
              "'good enough to praise' in two clipped syllables. To call a thing "
              "好 in Jin is to stamp it approved."),
)

E(
    key="jin_pronouns", name="Jin Chinese Pronouns",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        The full Jin pronoun system - personal, possessive, demonstrative,
        and interrogative - with the Taiyuan teaching romanization and
        example sentences. Personal: 我 ŋəʔ4 I (with the famous retained ŋ-
        initial and the entering tone - the most Jin syllable there is): 我是
        学生 ŋəʔ4 ʂɿ3 xɿəʔ4-ʂəŋ1 (I am a student). 你 niə2 you: 你好
        niə2-hau2? niə2-hau3 (hello). 他 tʰa1 he/she: 他来了 tʰa1 lai2-lə (he
        has come). Plurals add 们 mən1: 我们 ŋəʔ4-mən1 we, 你们 niə2-mən1 you
        (plural), 他们 tʰa1-mən1 they. Possessive adds 的 tiəʔ4: 我的 ŋəʔ4-tiəʔ4
        my, 你的 niə2-tiəʔ4 your, 他的 tʰa1-tiəʔ4 his: 我的书 ŋəʔ4-tiəʔ4 ʂu1
        (my book). Demonstratives: 这 tsəʔ4 this, 那 na3 that - and some Jin
        dialects keep a three-way distinction (this / that / yonder), a rare
        treasure among Chinese languages: 这是甚 tsəʔ4 ʂɿ3 ʂən2 (what is
        this?). Interrogatives: 甚 ʂən2 what (Shanxi's signature question
        word), 甚人 ʂən2-zən1 who, 甚地方 ʂən2-ti3-faŋ1 where, 甚时候
        ʂən2-sɿ1-həu3 when: 你甚时候来 ni2 ʂən2-sɿ1-həu3 lai1 (when are you
        coming?). 您 nin2 is the polite you, used for elders and in formal
        speech. Reflexive 自己 tsɿ3-tɕi2 self: 我自己 ŋəʔ4 tsɿ3-tɕi2 (myself).
        Pronouns never change form - no cases, no conjugations: 我 is I, me,
        and my-stem all at once."""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronouns as a substitution drill. The learner
        takes a mastered sentence (我是学生) and swaps the pronoun through
        the whole paradigm - 你是学生, 他是学生, 我们是学生 - hearing how Jin
        holds the sentence frame still while the pronoun changes. The
        demonstrative pair 这/那 is drilled with pointing at real objects,
        and the interrogative set 甚/甚人/甚地方/甚时候 is drilled as
        question-formation: every pronoun question in this record gets asked
        to a real or imagined partner. The demo runs a grammar drill asserting
        each pronoun's position in its sentence."""),
    key_points=[
        "我 ŋəʔ4 (I): 我是学生 ŋəʔ4 ʂɿ3 xɿəʔ4-ʂəŋ1 - I am a student. The ŋ- initial is Jin's retained ancient sound.",
        "你 niə2 (you): 你好 niə2-hau3 - hello.",
        "他 tʰa1 (he/she): 他来了 tʰa1 lai2-lə - he has come.",
        "Plurals with 们 mən1: 我们 ŋəʔ4-mən1 (we), 你们 niə2-mən1 (you all), 他们 tʰa1-mən1 (they): 你们都来 ni2-mən1 tu1 lai1 - you all come.",
        "Possessive with 的 tiəʔ4: 我的书 ŋəʔ4-tiəʔ4 ʂu1 - my book.",
        "Demonstratives: 这 tsəʔ4 (this), 那 na3 (that); some Jin dialects keep a third yonder form - a documented three-way distinction.",
        "Interrogatives: 甚 ʂən2 (what): 这是甚 tsəʔ4 ʂɿ3 ʂən2 - what is this?",
        "甚人 ʂən2-zən1 (who), 甚地方 ʂən2-ti3-faŋ1 (where), 甚时候 ʂən2-sɿ1-həu3 (when): 你甚时候来 ni2 ʂən2-sɿ1-həu3 lai1 - when are you coming?",
        "Polite 您 nin2 for elders; reflexive 自己 tsɿ3-tɕi2 (self).",
        "No case changes: pronouns keep one form as subject, object, and possessor-stem.",
    ],
    requirements=[
        "Drill 我 ŋəʔ4 aloud until the ŋ- initial and glottal stop are natural.",
        "Ask and answer all four 甚-questions with a partner before moving on.",
    ],
    standards=[
        "Pronoun paradigms follow documented Jin usage; 的 tiəʔ4 is the standard possessive particle.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002. Jin pronoun system.",
        "Kurpaska M. Chinese Language(s). de Gruyter; 2010. Three-way demonstrative distinction in Jin dialects.",
    ],
    sig_lens=("Through the Signature lens, pronouns are the seals of the self: 我 "
              "ŋəʔ4 carries both the ancient ŋ- and the entering tone, two fossils "
              "of sound in a single syllable - the speaker signing their own name "
              "in the oldest ink Jin owns."),
)

E(
    key="jin_numbers", name="Jin Chinese Numbers and Time",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Numbers 1-100, ordinals, days, months, seasons, clock time, and dates
        in Jin - each with the Taiyuan teaching romanization and an example
        sentence. 1 一 iəʔ4, 2 二 ər3, 3 三 san1, 4 四 sɿ3, 5 五 u3, 6 六
        liəuʔ4, 7 七 tsʰiəʔ4, 8 八 paʔ4, 9 九 tɕiəu3, 10 十 səʔ4: 我有三本书
        ŋəʔ4 iəu2 san1-pən2 ʂu1 (I have three books). 11 十一 səʔ4-iəʔ4, 20 二十
        ər3-səʔ4, 100 一百 iəʔ4-paʔ4: 一百块 iəʔ4-paʔ4 kʰuai3 (one hundred
        yuan). Ordinals add 第 ti3: 第一 ti3-iəʔ4 (first). Days: 星期一
        xiŋ1-tsʰi1-iəʔ4 Monday, 今天 tɕin1-tʰien1 today, 夜来 ie3-lai2
        yesterday (Shanxi's own word), 明天 miŋ2-tʰien1 tomorrow. Months: 一月
        iəʔ4-yøʔ4 January (月 is entering: yøʔ4), 十二月 ʂɿ3-ər3-yøʔ4
        December. Seasons: 春天 tsʰun1-tʰien1 spring, 夏天 xia3-tʰien1 summer,
        秋天 tsʰiəu1-tʰien1 autumn, 冬天 tuŋ1-tʰien1 winter. Clock time: 点
        tien2 o'clock, 分 fən1 minute, 半 pan3 half: 三点半 san1-tien2-pan3
        (3:30): 现在三点半 xien3-tsai3 san1-tien2-pan3 (it is now 3:30).
        Dates: 2026年10月17日 ər3-liŋ2-ər3-liəuʔ4-nien2 səʔ4-yøʔ4 tsʰi2-tsʰi1
        zɿ3 (October 17, 2026). Counting in Jin is a daily entering-tone
        workout - half the digits are checked syllables."""),
    how_it_works=textwrap.dedent("""\
        This record teaches numbers as a chant: 1-10 forward, 10-1 backward,
        then by tens to 100, all aloud with the glottal stops crisp on 一,
        六, 七, 八, 十. Time phrases are taught as frames the learner fills:
        ___点___分 for clock time, ___月___日 for dates. The learner practices
        by narrating their real day in Jin (我七点起床 - I get up at seven).
        Ordinals are drilled with rankings (第一, 第二, 第三). The demo runs
        the tone drill over the number words, verifying all five tone
        categories appear in the digits."""),
    key_points=[
        "1-10: 一 iəʔ4, 二 ər3, 三 san1, 四 sɿ3, 五 u3, 六 liəuʔ4, 七 tsʰiəʔ4, 八 paʔ4, 九 tɕiəu3, 十 səʔ4.",
        "Compounds: 十一 səʔ4-iəʔ4 (11), 二十 ər3-səʔ4 (20), 一百 iəʔ4-paʔ4 (100): 一百块 iəʔ4-paʔ4 kʰuai3 - one hundred yuan.",
        "Ordinals with 第 ti3: 第一 ti3-iəʔ4 (first).",
        "Days: 今天 tɕin1-tʰien1 (today), 夜来 ie3-lai2 (yesterday - Shanxi's own word), 明天 miŋ2-tʰien1 (tomorrow), 星期一 xiŋ1-tsʰi1-iəʔ4 (Monday).",
        "Months: 一月 iəʔ4-yøʔ4 (January); 月 yøʔ4 is entering tone.",
        "Seasons: 春天 tsʰun1-tʰien1, 夏天 xia3-tʰien1, 秋天 tsʰiəu1-tʰien1, 冬天 tuŋ1-tʰien1.",
        "Clock time: 三点半 san1-tien2-pan3 (3:30): 现在三点半 xien3-tsai3 san1-tien2-pan3 - it is now 3:30.",
        "Dates: 2026年10月17日 - October 17, 2026, read digit by digit in Jin.",
        "Half the digits are entering-tone: counting is a daily ʔ workout.",
    ],
    requirements=[
        "Count 1-100 aloud in Jin without hesitation before moving on.",
        "Narrate your real day's schedule in Jin using 点/分/半.",
    ],
    standards=[
        "Numeral readings follow the documented Taiyuan system, including entering-tone digits.",
        "Date and time frames follow standard modern Chinese conventions.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002. Jin numerals and entering-tone readings.",
        "Chinese Academy of Social Sciences. 中国语言地图集(第2版). Commercial Press; 2012. Jin dialect areas.",
    ],
    sig_lens=("Through the Signature lens, numbers are the tally-seals of daily life: "
              "half the digits clipped short by the entering tone, every count a "
              "small drumbeat of ʔ - Jin counts the way it speaks, sealed and "
              "certain."),
)

E(
    key="jin_greetings", name="Jin Chinese Greetings and Everyday Phrases",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Thirty Jin greetings, farewells, and politeness phrases - each with
        the Taiyuan teaching romanization, English, and a usage note. 你好
        niə2-hau3 hello - the universal opener. 吃了没 ni2 tsʰəʔ4-lə mei2
        (have you eaten?) - Shanxi's warmest greeting, asked like family.
        谢谢 xie3-xie3 thank you, 多谢 tu1-xie3 many thanks (warmer), 再见
        tsai3-tɕien3 goodbye, 慢走 man3-tsəu2 go slowly (said to departing
        guests - the Shanxi farewell), 对不起 tui3-puʔ4-tsʰi3 sorry, 没关系
        mei2-kuan1-xi1 it doesn't matter, 请 tsʰiŋ2 please, 请问 tsʰiŋ2-uən3
        may I ask, 麻烦 ma1-fan1 excuse me / sorry to trouble you, 劳驾
        lau2-tɕia3 excuse me (passing by), 欢迎 huan1-iŋ1 welcome, 恭喜
        kuŋ1-xi1 congratulations, 晚安 uan2-an1 good night, 早 tsau2 morning
        (short and local), 好久不见 hau2-tɕiəu2-puʔ4-tɕien3 long time no see,
        最近怎么样 tsui3-tɕin3 tsən2-mə-iaŋ3 how have you been lately, 请坐
        tsʰiŋ2-tsu3 please sit, 请喝茶 tsʰiŋ2 xəʔ4-tsʰa1 please have some tea,
        别客气 pieʔ4-kʰəʔ4-tsʰi3 don't be polite (make yourself at home), 一路
        顺风 iəʔ4-lu3 ʂun3-fəŋ1 have a smooth journey, 生日快乐 ʂəŋ1-zɿ3
        kʰuai3-lə3 happy birthday, 新年好 xin1-nien2-hau3 happy new year, 注意
        身体 tsu3-i3 ʂən1-tʰi2 take care of your health, 回见 xui2-tɕien3 see
        you later, 明儿见 miər2-tɕien3 see you tomorrow, 谢谢你的帮助
        xie3-xie3 ni2-tiəʔ4 paŋ1-tsu3 thank you for your help, 不好意思
        puʔ4-hau3-i3-sɿ1 excuse me (apologizing), 久仰 tɕiəu2-iaŋ2 honored to
        meet you (formal). Usage notes: 吃了没 is for people you know; 请问
        opens any stranger question; 慢走 is the kindest Shanxi goodbye."""),
    how_it_works=textwrap.dedent("""\
        This record teaches phrases as social tools, not vocabulary: each
        phrase comes with WHEN to use it, because a greeting used wrong is
        worse than silence. The learner role-plays three scenes - meeting a
        friend (你好, 吃了没), thanking a host (谢谢, 别客气), leaving a shop
        (再见, 慢走) - saying both parts aloud. The ten anchor phrases are
        drilled to automaticity first; the other twenty are recognition plus
        the three scenes. The demo quizzes the ten anchors with a
        perfect-score assertion."""),
    key_points=[
        "你好 niə2-hau3 (hello): the universal opener, any time of day.",
        "吃了没 ni2 tsʰəʔ4-lə mei2 (have you eaten?): Shanxi's warmest greeting - asked like family.",
        "谢谢 xie3-xie3 (thank you); warmer: 多谢 tu1-xie3.",
        "再见 tsai3-tɕien3 (goodbye); kindest Shanxi farewell: 慢走 man3-tsəu2 (go slowly).",
        "对不起 tui3-puʔ4-tsʰi3 (sorry); answer: 没关系 mei2-kuan1-xi1 (it doesn't matter).",
        "请 tsʰiŋ2 (please); 请问 tsʰiŋ2-uən3 (may I ask) opens any stranger question.",
        "麻烦 ma1-fan1 (sorry to trouble you); 劳驾 lau2-tɕia3 (excuse me, passing by).",
        "晚安 uan2-an1 (good night); 早 tsau2 (morning, short and local).",
        "恭喜 kuŋ1-xi1 (congratulations); 欢迎 huan1-iŋ1 (welcome).",
        "Host phrases: 请坐 tsʰiŋ2-tsu3 (please sit), 请喝茶 tsʰiŋ2 xəʔ4-tsʰa1 (please have tea), 别客气 pieʔ4-kʰəʔ4-tsʰi3 (make yourself at home).",
        "Also: 好久不见 (long time no see), 最近怎么样 (how have you been), 一路顺风 (smooth journey), 生日快乐 (happy birthday), 新年好 (happy new year), 注意身体 (take care), 回见 (see you later), 明儿见 (see you tomorrow), 不好意思 (excuse me), 久仰 (honored to meet you).",
    ],
    requirements=[
        "Role-play the three scenes (meeting, thanking, leaving) aloud.",
        "Use 吃了没 with someone you know this week.",
    ],
    standards=[
        "Usage notes follow documented Shanxi social conventions.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Qiao Quansheng 乔全生. 晋方言研究的历史、现状与未来. On Jin sociolinguistic research.",
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002.",
    ],
    sig_lens=("Through the Signature lens, greetings are the daily seals of belonging: "
              "吃了没 asks after your stomach because in Shanxi care is food, and "
              "慢走 sends you off slowly because no one should leave in a hurry. "
              "Every greeting is a small covenant renewed."),
)

E(
    key="jin_grammar", name="Jin Chinese Grammar Essentials",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        The essential grammar of Jin - word order, number, negation, questions,
        aspect, and Jin's famous derivational prefixes - each rule with
        translated example sentences. Word order is SVO: 我吃饭 ŋəʔ4 tsʰəʔ4-fan3
        (I eat). No gender, no cases, no verb conjugations. Number: nouns
        don't inflect; add 们 mən1 for human plurals (朋友们 pʰəŋ1-iəu3-mən1,
        friends). Negation: 不 puʔ4 for present/future (我不去 ŋəʔ4 puʔ4-tsʰɿ3,
        I won't go), 没 mei2 for past/possession (我没吃 ŋəʔ4 mei2-tsʰəʔ4, I
        didn't eat). Questions: 吗 ma (你去吗 ni2 tsʰɿ3 ma, are you going?),
        吧 pa (suggestion: 走吧 tsəu2-pa, let's go), 呢 nə (and you?: 你呢
        ni2-nə). Aspect: 了 lə completed (我吃了 ŋəʔ4 tsʰəʔ4-lə, I ate), 过
        kuə3 experienced (我去过 ŋəʔ4 tsʰɿ3-kuə3, I have been), 着 tsə
        durative (门开着 mən2 kʰai1-tsə, the door is open). 把 pa construction:
        把门关上 pa2 mən2 kuan1-ʂaŋ3 (close the door). Passive with 被 pei3:
        杯子被他打破了 pei1-tsɿ pei3 tʰa1 ta2-pʰuə3-lə (the cup was broken by
        him). Locative 在 tsai3: 他在太原 tʰa1 tsai3 tʰai3-yøn2 (he is in
        Taiyuan). And Jin's glory - the derivational prefixes 圪 /kəʔ4/,
        忽 /xəʔ4/, 入 /zuʔ4/: 入鬼 zuʔ4-kui2 fool around (from 鬼 kui2 ghost),
        圪蛋 kəʔ4-tan3 egg, and the l-fission rule that splits one syllable
        into two with an /l/ infix: 蹦 pəŋ3 hop becomes /pəʔ4-ləŋ1/, 拖
        tʰuɤ1 drag becomes /tʰəʔ4-luɤ1/, 刮 kua1 scrape becomes /kuəʔ4-la1/,
        巷 xɒ̃3 street becomes /xəʔ4-lɒ̃1/, 孔 kʰoːŋ1 hole becomes 窟窿
        /kʰuʔ4-luŋ1/. These are Jin's fingerprints - documented, famous, and
        found almost nowhere else."""),
    how_it_works=textwrap.dedent("""\
        This record teaches grammar as sentence patterns, not rules to
        memorize: each pattern is a frame with one slot to fill (我___饭 for
        verbs, ___吗 for questions). The learner generates ten sentences per
        pattern by filling the slots with known words. The prefixes 圪/忽/入
        and the l-fission rule are taught as Jin's special effects - the
        learner practices splitting 蹦 into /pəʔ4-ləŋ1/ aloud until the
        rhythm feels natural. The demo runs a grammar drill asserting each
        particle sits in its correct position."""),
    key_points=[
        "SVO order, no inflections: 我吃饭 ŋəʔ4 tsʰəʔ4-fan3 - I eat.",
        "Negation: 不 puʔ4 (present/future): 我不去 ŋəʔ4 puʔ4-tsʰɿ3 - I won't go; 没 mei2 (past): 我没吃 ŋəʔ4 mei2-tsʰəʔ4 - I didn't eat.",
        "Questions: 吗 ma (你去吗 ni2 tsʰɿ3 ma - are you going?), 吧 pa (走吧 tsəu2-pa - let's go), 呢 nə (你呢 ni2-nə - and you?).",
        "Aspect: 了 lə completed (我吃了 ŋəʔ4 tsʰəʔ4-lə), 过 kuə3 experienced (我去过 ŋəʔ4 tsʰɿ3-kuə3), 着 tsə durative (门开着 mən2 kʰai1-tsə).",
        "把 pa: 把门关上 pa2 mən2 kuan1-ʂaŋ3 - close the door.",
        "Passive 被 pei3: 杯子被他打破了 pei1-tsɿ pei3 tʰa1 ta2-pʰuə3-lə - the cup was broken by him.",
        "Locative 在 tsai3: 他在太原 tʰa1 tsai3 tʰai3-yøn2 - he is in Taiyuan.",
        "Possessive 的 tiəʔ4: 我的书 ŋəʔ4-tiəʔ4 ʂu1 - my book.",
        "Prefixes 圪 /kəʔ4/, 忽 /xəʔ4/, 入 /zuʔ4/: 入鬼 zuʔ4-kui2 (fool around) < 鬼 kui2 (ghost).",
        "L-fission: 蹦→/pəʔ4-ləŋ1/, 拖→/tʰəʔ4-luɤ1/, 刮→/kuəʔ4-la1/, 巷→/xəʔ4-lɒ̃1/, 孔→窟窿/kʰuʔ4-luŋ1/ - Jin's documented signature sound change.",
    ],
    requirements=[
        "Generate ten sentences per pattern by filling the frames.",
        "Practice the l-fission pairs aloud until the rhythm is natural.",
    ],
    standards=[
        "Prefix and fission forms follow the documented Jin examples (kəʔ4, xəʔ4, zuʔ4; pəʔ4-ləŋ1 etc.).",
        "Aspect and construction patterns follow standard Sinitic grammar as realized in Jin.",
    ],
    citations=[
        "Documented Jin grammar: derivational prefixes 圪 /kəʔ/, 忽 /xəʔ/, 入 /zəʔ/ and l-fission examples (蹦→/pəʔ ləŋ/, 拖→/tʰəʔ luɤ/, 刮→/kuəʔ la/, 巷→/xəʔ lɒ̃/, 孔→窟窿/kʰuəʔ luŋ/).",
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002.",
        "Yan M.M. Introduction to Chinese Dialectology. LINCOM Europa; 2006.",
    ],
    sig_lens=("Through the Signature lens, grammar is the architecture of the covenant: "
              "SVO is the straight road, and the prefixes 圪/忽/入 are Jin's carved "
              "doorways - no other northern language builds words this way. To use "
              "them is to build in the Jin style."),
)

E(
    key="jin_home", name="Jin Chinese Home and Family Sentences",
    group="Compounded", ladder_rank=4, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Jin sentences about house, rooms, furniture, and family -
        each in characters, romanization, and English. 这是我的家 tsəʔ4 ʂɿ3
        ŋəʔ4-tiəʔ4 tɕia1 (this is my home). 我家有五口人 ŋəʔ4-tɕia1 iəu2 u3-kʰəu2
        zən1 (my family has five people). 爸爸在客厅 pa4-pa tsai3 kʰəʔ4-tʰiŋ1
        (father is in the living room). 妈妈在做饭 ma1-ma tsai3 tsu3-fan3
        (mother is cooking). 我的房间很干净 ŋəʔ4-tiəʔ4 faŋ2-tɕien1 xən2
        kan1-tɕiŋ3 (my room is very clean). 桌子上有本书 tsuəʔ4-tsɿ ʂaŋ3 iəu2
        pən2 ʂu1 (there is a book on the table). 椅子坏了 i2-tsɿ xuai3-lə (the
        chair is broken). 灯很亮 təŋ1 xən2-liaŋ3 (the lamp is very bright). 窗户
        开着 tsʰuaŋ1-xu3 kʰai1-tsə (the window is open). 床很舒服 tsʰuaŋ2 xən2
        ʂu1-fuʔ4 (the bed is comfortable). 厨房在后面 tsʰu2-faŋ2 tsai3
        xəu3-mien3 (the kitchen is in the back). 厕所在哪里 tsʰəʔ4-suə2 tsai3
        na2-li2 (where is the bathroom?). 这是爷爷 tsəʔ4 ʂɿ3 ie2-ie (this is
        grandfather). 这是奶奶 tsəʔ4 ʂɿ3 nai2-nai (this is grandmother).
        哥哥在上班 kə1-kə tsai3 ʂaŋ3-pan1 (elder brother is at work). 姐姐在
        学校 tɕie2-tɕie tsai3 xɿəʔ4-xiau3 (elder sister is at school). 弟弟还小
        ti3-ti xai2 siau2 (younger brother is still small). 妹妹很漂亮 mei3-mei
        xən2 pʰiau3-liaŋ1 (younger sister is very pretty). 我们一家人很幸福
        ŋəʔ4-mən1 iəʔ4-tɕia1-zən1 xən2 xiŋ3-fuʔ4 (our whole family is very
        happy). 晚上一起吃饭 uan2-ʂaŋ3 iəʔ4-tsʰi2 tsʰəʔ4-fan3 (in the evening
        we eat together). 家是最小的国 tɕia1 ʂɿ3 tsui3-siau2-tiəʔ4 kuəʔ4
        (home is the smallest country). Twenty sentences, one home."""),
    how_it_works=textwrap.dedent("""\
        This record teaches home vocabulary inside the sentences where it
        lives: rooms get 在-sentences (爸爸在客厅), family members get 这是-
        introductions, furniture gets 有/在 descriptions. The learner walks
        through their own home naming everything in Jin, then introduces
        their own family with 这是___. The demo audits that all twenty
        sentences are present and checks anchor words (房子, 爸爸, 妈妈,
        房间) against the record text."""),
    key_points=[
        "这是我的家 tsəʔ4 ʂɿ3 ŋəʔ4-tiəʔ4 tɕia1 - this is my home.",
        "我家有五口人 ŋəʔ4-tɕia1 iəu2 u3-kʰəu2 zən1 - my family has five people.",
        "爸爸在客厅 pa4-pa tsai3 kʰəʔ4-tʰiŋ1 - father is in the living room.",
        "妈妈在做饭 ma1-ma tsai3 tsu3-fan3 - mother is cooking.",
        "我的房间很干净 ŋəʔ4-tiəʔ4 faŋ2-tɕien1 xən2 kan1-tɕiŋ3 - my room is very clean.",
        "桌子上有本书 tsuəʔ4-tsɿ ʂaŋ3 iəu2 pən2 ʂu1 - there is a book on the table.",
        "椅子坏了 i2-tsɿ xuai3-lə - the chair is broken.",
        "灯很亮 təŋ1 xən2-liaŋ3 - the lamp is very bright.",
        "窗户开着 tsʰuaŋ1-xu3 kʰai1-tsə - the window is open.",
        "床很舒服 tsʰuaŋ2 xən2 ʂu1-fuʔ4 - the bed is comfortable.",
        "厨房在后面 tsʰu2-faŋ2 tsai3 xəu3-mien3 - the kitchen is in the back.",
        "厕所在哪里 tsʰəʔ4-suə2 tsai3 na2-li2 - where is the bathroom?",
        "这是爷爷 tsəʔ4 ʂɿ3 ie2-ie - this is grandfather; 这是奶奶 tsəʔ4 ʂɿ3 nai2-nai - this is grandmother.",
        "哥哥在上班 kə1-kə tsai3 ʂaŋ3-pan1 - elder brother is at work.",
        "姐姐在学校 tɕie2-tɕie tsai3 xɿəʔ4-xiau3 - elder sister is at school.",
        "弟弟还小 ti3-ti xai2 siau2 - younger brother is still small.",
        "妹妹很漂亮 mei3-mei xən2 pʰiau3-liaŋ1 - younger sister is very pretty.",
        "我们一家人很幸福 ŋəʔ4-mən1 iəʔ4-tɕia1-zən1 xən2 xiŋ3-fuʔ4 - our whole family is very happy.",
        "晚上一起吃饭 uan2-ʂaŋ3 iəʔ4-tsʰi2 tsʰəʔ4-fan3 - in the evening we eat together.",
        "家是最小的国 tɕia1 ʂɿ3 tsui3-siau2-tiəʔ4 kuəʔ4 - home is the smallest country.",
    ],
    requirements=[
        "Walk through your home naming rooms and furniture in Jin.",
        "Introduce your family with 这是___ sentences.",
    ],
    standards=[
        "Locative 在 and existential 有 follow standard Sinitic patterns.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002.",
    ],
    sig_lens=("Through the Signature lens, home is the first sealed room of the "
              "covenant: every 家 has its 爸爸 and 妈妈, every 房间 its own tone. "
              "To name your home in Jin is to deed it in the old language."),
)

E(
    key="jin_food", name="Jin Chinese Food and Cooking Sentences",
    group="Compounded", ladder_rank=4, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Jin sentences about meals, ingredients, cooking, and
        restaurants - each in characters, romanization, and English. Shanxi
        is noodle country, and this record eats like a local. 我爱吃刀削面
        ŋəʔ4 ai3 tsʰəʔ4 tau1-xiau1-mien3 (I love knife-cut noodles). 这刀削面
        不赖 tsəʔ4 tau1-xiau1-mien3 puʔ4-lai3 (these noodles are good - the
        Shanxi compliment). 山西老陈醋很有名 ʂan1-xi1 lau2-tsʰən2-tsʰu3 xən2
        iəu2-miŋ2 (Shanxi aged vinegar is very famous). 吃面加醋 tsʰəʔ4-mien3
        tɕia1-tsʰu3 (add vinegar to noodles). 妈妈做饭好吃 ma1-ma tsu3-fan3
        hau2-tsʰəʔ4 (mother's cooking is delicious). 今天吃甚 tɕin1-tʰien1
        tsʰəʔ4 ʂən2 (what are we eating today?). 买点儿菜 mai2-tier2 tsʰai3
        (buy some vegetables). 肉多少钱 zəuʔ4 tu1-ʂau2 tsʰien2 (how much is
        the meat?). 鸡蛋很有营养 tɕi1-tan3 xən2 iəu2 iŋ2-iaŋ2 (eggs are very
        nutritious). 圪蛋炒了 kəʔ4-tan3 tsʰau2-lə (the eggs are scrambled -
        with the Jin word 圪蛋). 水开了 ʂui2 kʰai1-lə (the water is boiling).
        下面条 xia3 mien3-tʰiau2 (cook noodles). 火太大 xu1 tʰai3-ta3 (the
        fire is too big). 盐放少了 ien2 faŋ3 ʂau2-lə (too little salt was
        added). 好香啊 hau2-xiaŋ1-a (smells so good). 我吃饱了 ŋəʔ4 tsʰəʔ4-pau2-lə
        (I'm full). 服务员，买单 fu2-u3-yøn2, mai2-tan1 (waiter, the bill).
        这家饭店不错 tsəʔ4-tɕia1 fan3-tien3 puʔ4-tsʰuə3 (this restaurant is
        not bad). 打包带走 ta2-pau1 tai3-tsəu2 (pack it to go). 下次还来
        xia3-tsʰɿ3 xai2 lai1 (I'll come again next time). 民以食为天
        min2-i2 ʂəʔ4 uei2-tʰien1 (food is the people's heaven). Twenty
        sentences, one full Shanxi meal."""),
    how_it_works=textwrap.dedent("""\
        This record teaches food language as a meal in order: shopping (买点儿
        菜), cooking (下面条, 火太大), eating (我吃饱了), paying (买单). The
        learner cooks a real or imagined meal narrating each step in Jin.
        The Shanxi signatures - 刀削面, 老陈醋, 不赖, 圪蛋 - are drilled as
        cultural passwords: say them right and you're family. The demo
        audits all twenty sentences and checks anchor words (刀削面, 老陈醋,
        买单, 好吃) against the record text."""),
    key_points=[
        "我爱吃刀削面 ŋəʔ4 ai3 tsʰəʔ4 tau1-xiau1-mien3 - I love knife-cut noodles.",
        "这刀削面不赖 tsəʔ4 tau1-xiau1-mien3 puʔ4-lai3 - these noodles are good.",
        "山西老陈醋很有名 ʂan1-xi1 lau2-tsʰən2-tsʰu3 xən2 iəu2-miŋ2 - Shanxi aged vinegar is very famous.",
        "吃面加醋 tsʰəʔ4-mien3 tɕia1-tsʰu3 - add vinegar to noodles.",
        "妈妈做饭好吃 ma1-ma tsu3-fan3 hau2-tsʰəʔ4 - mother's cooking is delicious.",
        "今天吃甚 tɕin1-tʰien1 tsʰəʔ4 ʂən2 - what are we eating today?",
        "买点儿菜 mai2-tier2 tsʰai3 - buy some vegetables.",
        "肉多少钱 zəuʔ4 tu1-ʂau2 tsʰien2 - how much is the meat?",
        "鸡蛋很有营养 tɕi1-tan3 xən2 iəu2 iŋ2-iaŋ2 - eggs are very nutritious.",
        "圪蛋炒了 kəʔ4-tan3 tsʰau2-lə - the eggs are scrambled.",
        "水开了 ʂui2 kʰai1-lə - the water is boiling.",
        "下面条 xia3 mien3-tʰiau2 - cook noodles.",
        "火太大 xu1 tʰai3-ta3 - the fire is too big.",
        "盐放少了 ien2 faŋ3 ʂau2-lə - too little salt was added.",
        "好香啊 hau2-xiaŋ1-a - smells so good.",
        "我吃饱了 ŋəʔ4 tsʰəʔ4-pau2-lə - I'm full.",
        "服务员，买单 fu2-u3-yøn2, mai2-tan1 - waiter, the bill please.",
        "这家饭店不错 tsəʔ4-tɕia1 fan3-tien3 puʔ4-tsʰuə3 - this restaurant is not bad.",
        "打包带走 ta2-pau1 tai3-tsəu2 - pack it to go.",
        "下次还来 xia3-tsʰɿ3 xai2 lai1 - I'll come again next time.",
    ],
    requirements=[
        "Narrate cooking a meal in Jin, step by step.",
        "Order a full meal in a role-play using 买单 at the end.",
    ],
    standards=[
        "Food vocabulary follows documented Shanxi usage (刀削面, 老陈醋, 圪蛋, 不赖).",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Documented Shanxi food culture: 刀削面 knife-cut noodles, 老陈醋 aged vinegar; Jin 圪蛋 (egg), 不赖 (good).",
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002.",
    ],
    sig_lens=("Through the Signature lens, food is the tastiest seal of identity: "
              "no one says 不赖 over 刀削面 with 老陈醋 and stays a stranger. "
              "Shanxi sealed its covenant in vinegar and wheat, and every meal "
              "re-signs it."),
)

E(
    key="jin_travel", name="Jin Chinese Travel and Directions Sentences",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Jin sentences for transport, directions, tickets, and lodging
        - each in characters, romanization, and English. 火车站在哪里
        xu1-tsʰə1-tsan3 tsai3 na2-li2 (where is the train station?). 去平遥
        怎么走 tsʰɿ3 pʰiŋ2-iau2 tsən2-mə tsəu2 (how do I get to Pingyao?).
        一直走 iəʔ4-tsɿ3 tsəu2 (go straight). 往左拐 uaŋ2-tsu1 kuai2 (turn
        left). 往右拐 uaŋ2-iəu3 kuai2 (turn right). 在前面 tsai3 tsʰien2-mien3
        (it's ahead). 很远吗 xən2-yøn2 ma (is it far?). 打车去 ta2-tsʰə1
        tsʰɿ3 (go by taxi). 坐地铁去 tsu3 ti3-tʰieʔ4 tsʰɿ3 (go by subway).
        买两张票 mai2 liaŋ2-tsaŋ1 pʰiau3 (buy two tickets). 票多少钱
        pʰiau3 tu1-ʂau2 tsʰien2 (how much is the ticket?). 几点的车
        tɕi2-tien2-tiəʔ4 tsʰə1 (what time is the train?). 车晚点了 tsʰə1
        uan2-tien2-lə (the train is late). 我迷路了 ŋəʔ4 mi2-lu3-lə (I'm
        lost). 请问，厕所在哪里 tsʰiŋ2-uən3, tsʰəʔ4-suə2 tsai3 na2-li2
        (excuse me, where is the bathroom?). 附近有酒店吗 fu3-tɕin3 iəu2
        tɕiəu2-tien3 ma (is there a hotel nearby?). 住一晚多少钱 tsu3
        iəʔ4-uan2 tu1-ʂau2 tsʰien2 (how much for one night?). 有热水吗 iəu2
        zəʔ4-ʂui2 ma (is there hot water?). 明天几点出发 miŋ2-tʰien1
        tɕi2-tien2 tsʰu1-faʔ4 (what time do we leave tomorrow?). 路上小心
        lu3-ʂaŋ3 siau2-xin1 (be careful on the road). Twenty sentences, one
        Shanxi journey."""),
    how_it_works=textwrap.dedent("""\
        This record teaches travel language as a journey in order: asking
        directions, taking transport, buying tickets, finding a hotel. The
        learner plans a real trip to Pingyao or Datong narrating each step in
        Jin. Direction words (左, 右, 前面, 一直) are drilled with hand
        gestures; transport words (地铁, 火车, 打车) with a mock ticket
        counter. The demo audits all twenty sentences and checks anchor words
        (平遥, 地铁, 票, 火车站) against the record text."""),
    key_points=[
        "火车站在哪里 xu1-tsʰə1-tsan3 tsai3 na2-li2 - where is the train station?",
        "去平遥怎么走 tsʰɿ3 pʰiŋ2-iau2 tsən2-mə tsəu2 - how do I get to Pingyao?",
        "一直走 iəʔ4-tsɿ3 tsəu2 - go straight.",
        "往左拐 uaŋ2-tsu1 kuai2 - turn left; 往右拐 uaŋ2-iəu3 kuai2 - turn right.",
        "在前面 tsai3 tsʰien2-mien3 - it's ahead.",
        "很远吗 xən2-yøn2 ma - is it far?",
        "打车去 ta2-tsʰə1 tsʰɿ3 - go by taxi.",
        "坐地铁去 tsu3 ti3-tʰieʔ4 tsʰɿ3 - go by subway.",
        "买两张票 mai2 liaŋ2-tsaŋ1 pʰiau3 - buy two tickets.",
        "票多少钱 pʰiau3 tu1-ʂau2 tsʰien2 - how much is the ticket?",
        "几点的车 tɕi2-tien2-tiəʔ4 tsʰə1 - what time is the train?",
        "车晚点了 tsʰə1 uan2-tien2-lə - the train is late.",
        "我迷路了 ŋəʔ4 mi2-lu3-lə - I'm lost.",
        "请问，厕所在哪里 tsʰiŋ2-uən3, tsʰəʔ4-suə2 tsai3 na2-li2 - excuse me, where is the bathroom?",
        "附近有酒店吗 fu3-tɕin3 iəu2 tɕiəu2-tien3 ma - is there a hotel nearby?",
        "住一晚多少钱 tsu3 iəʔ4-uan2 tu1-ʂau2 tsʰien2 - how much for one night?",
        "有热水吗 iəu2 zəʔ4-ʂui2 ma - is there hot water?",
        "明天几点出发 miŋ2-tʰien1 tɕi2-tien2 tsʰu1-faʔ4 - what time do we leave tomorrow?",
        "路上小心 lu3-ʂaŋ3 siau2-xin1 - be careful on the road.",
        "平遥古城值得去 pʰiŋ2-iau2 ku2-tsʰəŋ2 tsɿ3-təʔ4 tsʰɿ3 - the Pingyao ancient city is worth visiting.",
    ],
    requirements=[
        "Plan a real or imagined Shanxi trip narrating each step in Jin.",
        "Drill direction words with hand gestures until automatic.",
    ],
    standards=[
        "Direction and transport frames follow standard Sinitic patterns.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002.",
    ],
    sig_lens=("Through the Signature lens, travel sentences are road-seals: every "
              "问路 is a small trust, every 慢走 a blessing on the road. Jin "
              "walks its own province and signs each mile in the old tones."),
)

E(
    key="jin_work", name="Jin Chinese Work and School Sentences",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Jin sentences about jobs, the office, the classroom, and
        learning - each in characters, romanization, and English. 你做甚工作
        ni2 tsu3 ʂən2 kuŋ1-tsuəʔ4 (what work do you do?). 我是老师 ŋəʔ4 ʂɿ3
        lau2-ʂɿ1 (I am a teacher). 老板很忙 lau2-pan2 xən2 maŋ2 (the boss is
        very busy). 九点开会 tɕiəu2-tien2 kʰai1-xui3 (meeting at nine).
        这个项目很重要 tsəʔ4-kə3 xiaŋ3-mu3 xən2 tsuŋ3-iau3 (this project is
        very important). 加油干 tɕia1-iəu2 kan3 (work hard, keep going).
        下班了 xia3-pan1-lə (off work). 今天累了 tɕin1-tʰien1 lei3-lə (tired
        today). 工资发了 kuŋ1-tsɿ1 faʔ4-lə (wages are paid). 我在学校
        ŋəʔ4 tsai3 xɿəʔ4-xiau3 (I am at school). 上课了 ʂaŋ3-kʰə3-lə (class
        has started). 老师讲得好 lau2-ʂɿ1 tɕiaŋ2-təʔ4-hau2 (the teacher
        explains well). 这道题很难 tsəʔ4-tau3 tʰi2 xən2 nan2 (this problem is
        very hard). 功课做完了 kuŋ1-kʰə3 tsu3-uan2-lə (homework is done).
        明天考试 miŋ2-tʰien1 kʰau2-ʂɿ3 (exam tomorrow). 好好学习 hau2-hau2
        xɿəʔ4-xi2 (study hard). 考试考得不错 kʰau2-ʂɿ3 kʰau2-təʔ4 puʔ4-tsʰuə3
        (the exam went well). 放学了 faŋ3-xɿəʔ4-lə (school is out). 同学们再见
        tʰuŋ2-xɿəʔ4-mən1 tsai3-tɕien3 (goodbye, classmates). 学习晋语很有意思
        xɿəʔ4-xi2 tɕin3-y1 xən2 iəu2 i3-sɿ1 (learning Jin is very interesting).
        Twenty sentences, one working day."""),
    how_it_works=textwrap.dedent("""\
        This record teaches work and school language as a day in order:
        morning meeting, the work itself, quitting time; then the school
        parallel: class, homework, exam. The learner describes their own job
        or studies with 你做甚工作 as the opener. Office words (老板, 开会,
        项目) and school words (考试, 功课, 同学) are drilled as two teams.
        The demo audits all twenty sentences and checks anchor words (老板,
        开会, 考试, 功课) against the record text."""),
    key_points=[
        "你做甚工作 ni2 tsu3 ʂən2 kuŋ1-tsuəʔ4 - what work do you do?",
        "我是老师 ŋəʔ4 ʂɿ3 lau2-ʂɿ1 - I am a teacher.",
        "老板很忙 lau2-pan2 xən2 maŋ2 - the boss is very busy.",
        "九点开会 tɕiəu2-tien2 kʰai1-xui3 - meeting at nine.",
        "这个项目很重要 tsəʔ4-kə3 xiaŋ3-mu3 xən2 tsuŋ3-iau3 - this project is very important.",
        "加油干 tɕia1-iəu2 kan3 - work hard, keep going.",
        "下班了 xia3-pan1-lə - off work.",
        "今天累了 tɕin1-tʰien1 lei3-lə - tired today.",
        "工资发了 kuŋ1-tsɿ1 faʔ4-lə - wages are paid.",
        "我在学校 ŋəʔ4 tsai3 xɿəʔ4-xiau3 - I am at school.",
        "上课了 ʂaŋ3-kʰə3-lə - class has started.",
        "老师讲得好 lau2-ʂɿ1 tɕiaŋ2-təʔ4-hau2 - the teacher explains well.",
        "这道题很难 tsəʔ4-tau3 tʰi2 xən2 nan2 - this problem is very hard.",
        "功课做完了 kuŋ1-kʰə3 tsu3-uan2-lə - homework is done.",
        "明天考试 miŋ2-tʰien1 kʰau2-ʂɿ3 - exam tomorrow.",
        "好好学习 hau2-hau2 xɿəʔ4-xi2 - study hard.",
        "考试考得不错 kʰau2-ʂɿ3 kʰau2-təʔ4 puʔ4-tsʰuə3 - the exam went well.",
        "放学了 faŋ3-xɿəʔ4-lə - school is out.",
        "同学们再见 tʰuŋ2-xɿəʔ4-mən1 tsai3-tɕien3 - goodbye, classmates.",
        "学习晋语很有意思 xɿəʔ4-xi2 tɕin3-y1 xən2 iəu2 i3-sɿ1 - learning Jin is very interesting.",
    ],
    requirements=[
        "Describe your own job or studies in Jin using five sentences.",
        "Drill office words and school words as two teams.",
    ],
    standards=[
        "Work and school frames follow standard Sinitic patterns.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002.",
    ],
    sig_lens=("Through the Signature lens, work sentences are the seals of the day's "
              "labor: 开会, 下班, 考试 - each a stamp in the ledger. Jin honors "
              "work the way it honors food: plainly, warmly, and sealed with "
              "effort."),
)

E(
    key="jin_health", name="Jin Chinese Health and Body Sentences",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Jin sentences about body parts, symptoms, the doctor visit,
        and the pharmacy - each in characters, romanization, and English.
        我头疼 ŋəʔ4 tʰəu2-tʰəŋ2 (my head aches). 我发烧了 ŋəʔ4 faʔ4-ʂau1-lə
        (I have a fever). 嗓子疼 saŋ2-tsɿ tʰəŋ2 (sore throat). 肚子疼
        tu3-tsɿ tʰəŋ2 (stomachache). 感冒了 kan2-mau3-lə (caught a cold).
        咳嗽了 kʰə2-səu3-lə (coughing). 流鼻涕 liəu2 pi2-tʰi3 (runny nose).
        哪里不舒服 na2-li2 puʔ4-ʂu1-fuʔ4 (where does it hurt?). 去看医生
        tsʰɿ3 kʰan3 i1-ʂəŋ1 (go see a doctor). 医生说 i1-ʂəŋ1 ʂuə1 (the doctor
        says). 多喝水 tu1 xəʔ4-ʂui2 (drink more water). 多休息 tu1 xiəu1-xiʔ4
        (rest more). 吃药 tsʰəʔ4-iau3 (take medicine). 一天三次 iəʔ4-tʰien1
        san1-tsʰɿ3 (three times a day). 饭后吃 fan3-xəu3 tsʰəʔ4 (take after
        meals). 药房在哪里 iau3-faŋ2 tsai3 na2-li2 (where is the pharmacy?).
        买点感冒药 mai2-tier2 kan2-mau3-iau3 (buy some cold medicine).
        好点儿了没 hau2-tier2-lə mei2 (feeling better?). 好多了 hau2-tu1-lə
        (much better). 注意身体 tsu3-i3 ʂən1-tʰi2 (take care of your health).
        早日康复 tsau2-zɿ3 kʰaŋ1-fuʔ4 (get well soon). Twenty sentences, one
        prescription for Jin health talk."""),
    how_it_works=textwrap.dedent("""\
        This record teaches health language as a clinic visit in order:
        symptoms (我头疼), the doctor's questions (哪里不舒服), advice (多喝
        水), the pharmacy (药房在哪里). Body parts are drilled by pointing;
        symptoms by describing. The learner practices the full visit as a
        role-play, both parts. The demo audits all twenty sentences and
        checks anchor words (头疼, 医生, 吃药, 药房) against the record
        text."""),
    key_points=[
        "我头疼 ŋəʔ4 tʰəu2-tʰəŋ2 - my head aches.",
        "我发烧了 ŋəʔ4 faʔ4-ʂau1-lə - I have a fever.",
        "嗓子疼 saŋ2-tsɿ tʰəŋ2 - sore throat.",
        "肚子疼 tu3-tsɿ tʰəŋ2 - stomachache.",
        "感冒了 kan2-mau3-lə - caught a cold.",
        "咳嗽了 kʰə2-səu3-lə - coughing.",
        "流鼻涕 liəu2 pi2-tʰi3 - runny nose.",
        "哪里不舒服 na2-li2 puʔ4-ʂu1-fuʔ4 - where does it hurt?",
        "去看医生 tsʰɿ3 kʰan3 i1-ʂəŋ1 - go see a doctor.",
        "医生说 i1-ʂəŋ1 ʂuə1 - the doctor says.",
        "多喝水 tu1 xəʔ4-ʂui2 - drink more water.",
        "多休息 tu1 xiəu1-xiʔ4 - rest more.",
        "吃药 tsʰəʔ4-iau3 - take medicine.",
        "一天三次 iəʔ4-tʰien1 san1-tsʰɿ3 - three times a day.",
        "饭后吃 fan3-xəu3 tsʰəʔ4 - take after meals.",
        "药房在哪里 iau3-faŋ2 tsai3 na2-li2 - where is the pharmacy?",
        "买点感冒药 mai2-tier2 kan2-mau3-iau3 - buy some cold medicine.",
        "好点儿了没 hau2-tier2-lə mei2 - feeling better?",
        "好多了 hau2-tu1-lə - much better.",
        "注意身体 tsu3-i3 ʂən1-tʰi2 - take care of your health; 早日康复 tsau2-zɿ3 kʰaŋ1-fuʔ4 - get well soon.",
    ],
    requirements=[
        "Role-play a full clinic visit in Jin, both parts.",
        "Point and name ten body parts in Jin.",
    ],
    standards=[
        "Symptom descriptions follow standard Sinitic patterns.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002.",
    ],
    sig_lens=("Through the Signature lens, health sentences are the body's own "
              "testimony: 头疼, 发烧 - the flesh speaks plainly, and Jin answers "
              "plainly. To say 注意身体 in Jin is to sign a small covenant of "
              "care."),
)

E(
    key="jin_emotions", name="Jin Chinese Emotions and Feelings Sentences",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Jin sentences for happy, sad, angry, afraid, love, and
        surprise - each in characters, romanization, and English. 我很开心
        ŋəʔ4 xən2 kʰai1-xin1 (I'm very happy). 太高兴了 tʰai3 kau1-xiŋ3-lə
        (so happy). 我很难过 ŋəʔ4 xən2 nan2-kuə3 (I'm very sad). 别哭 pieʔ4
        kʰu1 (don't cry). 他生气了 tʰa1 ʂəŋ1-tsʰi3-lə (he's angry). 别生气
        pieʔ4 ʂəŋ1-tsʰi3 (don't be angry). 我有点害怕 ŋəʔ4 iəu2-tier2
        xai3-pʰa3 (I'm a little scared). 别怕 pieʔ4 pʰa3 (don't be afraid).
        我爱你 ŋəʔ4 ai3 ni2 (I love you). 我喜欢你 ŋəʔ4 xi1-huan1 ni2 (I like
        you). 真的吗 tsən1-tiəʔ4 ma (really?). 太惊讶了 tʰai3 tɕiŋ1-ia3-lə
        (so surprising). 没想到 mei2 xiaŋ2-tau3 (didn't expect it). 放心吧
        faŋ3-xin1 pa (relax, don't worry). 别担心 pieʔ4 tan1-xin1 (don't
        worry). 我很感动 ŋəʔ4 xən2 kan2-tuŋ3 (I'm deeply moved). 谢谢你
        xie3-xie3 ni2 (thank you). 对不起 tui3-puʔ4-tsʰi3 (I'm sorry). 没关系
        mei2 kuan1-xi1 (it's okay). 加油 tɕia1-iəu2 (you can do it). Twenty
        sentences, one full human heart in Jin."""),
    how_it_works=textwrap.dedent("""\
        This record teaches feelings as situations: each emotion gets a
        mini-scene (good news → 我很开心, bad news → 我很难过, a friend
        crying → 别哭). The learner acts each scene with face and voice,
        because emotions live in the body first. Comfort phrases (别怕,
        放心吧, 加油) are drilled as a first-aid kit - the sentences you
        say to someone hurting. The demo audits all twenty sentences and
        checks anchor words (开心, 难过, 生气, 喜欢) against the record
        text."""),
    key_points=[
        "我很开心 ŋəʔ4 xən2 kʰai1-xin1 - I'm very happy.",
        "太高兴了 tʰai3 kau1-xiŋ3-lə - so happy.",
        "我很难过 ŋəʔ4 xən2 nan2-kuə3 - I'm very sad.",
        "别哭 pieʔ4 kʰu1 - don't cry.",
        "他生气了 tʰa1 ʂəŋ1-tsʰi3-lə - he's angry.",
        "别生气 pieʔ4 ʂəŋ1-tsʰi3 - don't be angry.",
        "我有点害怕 ŋəʔ4 iəu2-tier2 xai3-pʰa3 - I'm a little scared.",
        "别怕 pieʔ4 pʰa3 - don't be afraid.",
        "我爱你 ŋəʔ4 ai3 ni2 - I love you.",
        "我喜欢你 ŋəʔ4 xi1-huan1 ni2 - I like you.",
        "真的吗 tsən1-tiəʔ4 ma - really?",
        "太惊讶了 tʰai3 tɕiŋ1-ia3-lə - so surprising.",
        "没想到 mei2 xiaŋ2-tau3 - didn't expect it.",
        "放心吧 faŋ3-xin1 pa - relax, don't worry.",
        "别担心 pieʔ4 tan1-xin1 - don't worry.",
        "我很感动 ŋəʔ4 xən2 kan2-tuŋ3 - I'm deeply moved.",
        "谢谢你 xie3-xie3 ni2 - thank you; 对不起 tui3-puʔ4-tsʰi3 - I'm sorry; 没关系 mei2 kuan1-xi1 - it's okay.",
        "加油 tɕia1-iəu2 - you can do it.",
        "Emotions need no special grammar - the same sentence frames carry every feeling.",
        "Comfort phrases (别怕, 放心吧, 加油) are the emotional first-aid kit.",
    ],
    requirements=[
        "Act each emotion scene with face and voice, not just words.",
        "Comfort a (real or imagined) friend using 别怕/放心吧/加油.",
    ],
    standards=[
        "Emotion vocabulary follows documented Shanxi usage.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002.",
    ],
    sig_lens=("Through the Signature lens, feelings are the heart's own seals: "
              "开心, 难过, 生气 - Jin does not dress them up, it says them "
              "straight. To say 我爱你 in Jin is to sign the oldest contract "
              "there is."),
)

E(
    key="jin_nature", name="Jin Chinese Nature and Weather Sentences",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Jin sentences about animals, plants, seasons, and weather -
        each in characters, romanization, and English. 下雨了 xia3-y1-lə
        (it's raining). 出太阳了 tsʰu1 tʰai3-iaŋ2-lə (the sun is out). 今天
        很热 tɕin1-tʰien1 xən2 zəʔ4 (today is very hot). 夜来下雪了 ie3-lai2
        xia3-xɿəʔ4-lə (it snowed yesterday). 刮风了 kua1-fəŋ1-lə (it's windy).
        春天来了 tsʰun1-tʰien1 lai2-lə (spring has come). 花开了 xua1 kʰai1-lə
        (the flowers are blooming). 树叶绿了 ʂu3-ie3 ly3-lə (the leaves are
        green). 黄河很长 xuaŋ2-xə2 xən2 tsʰaŋ2 (the Yellow River is very
        long). 汾河穿过太原 fən2-xə2 tsʰuan1-kuə3 tʰai3-yøn2 (the Fen River
        runs through Taiyuan). 山上很凉快 ʂan1-ʂaŋ3 xən2 liaŋ2-kʰuai3 (it's
        cool on the mountain). 狗在叫 kəu2 tsai3 tɕiau3 (the dog is barking).
        猫在睡觉 mau1 tsai3 ʂui3-tɕiau3 (the cat is sleeping). 鸟在唱歌
        niau2 tsai3 tsʰaŋ3-kə1 (the birds are singing). 马跑得快 ma2 pʰau2-təʔ4
        kʰuai3 (horses run fast). 羊在吃草 iaŋ2 tsai3 tsʰəʔ4-tsʰau2 (sheep are
        eating grass). 麦子黄了 məʔ4-tsɿ xuaŋ2-lə (the wheat has turned
        yellow). 苹果熟了 pʰiŋ2-kuə2 ʂəu2-lə (the apples are ripe). 天气不错
        tʰien1-tsʰi3 puʔ4-tsʰuə3 (the weather is nice). 明天会下雨吗
        miŋ2-tʰien1 xui3 xia3-y1 ma (will it rain tomorrow?). Twenty
        sentences, one Shanxi sky."""),
    how_it_works=textwrap.dedent("""\
        This record teaches nature language as weather-watching: the learner
        looks out the window and narrates the sky in Jin (下雨了, 出太阳了).
        Seasons get a year-wheel drill; animals get sound-and-motion pairing
        (狗在叫 with a bark). The Yellow River and Fen River sentences root
        the language in Shanxi's real geography - Jin is spoken where these
        rivers run. The demo audits all twenty sentences and checks anchor
        words (下雨, 春天, 黄河, 汾河) against the record text."""),
    key_points=[
        "下雨了 xia3-y1-lə - it's raining.",
        "出太阳了 tsʰu1 tʰai3-iaŋ2-lə - the sun is out.",
        "今天很热 tɕin1-tʰien1 xən2 zəʔ4 - today is very hot.",
        "夜来下雪了 ie3-lai2 xia3-xɿəʔ4-lə - it snowed yesterday.",
        "刮风了 kua1-fəŋ1-lə - it's windy.",
        "春天来了 tsʰun1-tʰien1 lai2-lə - spring has come.",
        "花开了 xua1 kʰai1-lə - the flowers are blooming.",
        "树叶绿了 ʂu3-ie3 ly3-lə - the leaves are green.",
        "黄河很长 xuaŋ2-xə2 xən2 tsʰaŋ2 - the Yellow River is very long.",
        "汾河穿过太原 fən2-xə2 tsʰuan1-kuə3 tʰai3-yøn2 - the Fen River runs through Taiyuan.",
        "山上很凉快 ʂan1-ʂaŋ3 xən2 liaŋ2-kʰuai3 - it's cool on the mountain.",
        "狗在叫 kəu2 tsai3 tɕiau3 - the dog is barking.",
        "猫在睡觉 mau1 tsai3 ʂui3-tɕiau3 - the cat is sleeping.",
        "鸟在唱歌 niau2 tsai3 tsʰaŋ3-kə1 - the birds are singing.",
        "马跑得快 ma2 pʰau2-təʔ4 kʰuai3 - horses run fast.",
        "羊在吃草 iaŋ2 tsai3 tsʰəʔ4-tsʰau2 - sheep are eating grass.",
        "麦子黄了 məʔ4-tsɿ xuaŋ2-lə - the wheat has turned yellow.",
        "苹果熟了 pʰiŋ2-kuə2 ʂəu2-lə - the apples are ripe.",
        "天气不错 tʰien1-tsʰi3 puʔ4-tsʰuə3 - the weather is nice.",
        "明天会下雨吗 miŋ2-tʰien1 xui3 xia3-y1 ma - will it rain tomorrow?",
    ],
    requirements=[
        "Narrate the sky outside your window in Jin every day for a week.",
        "Name ten animals and five plants in Jin.",
    ],
    standards=[
        "Weather and nature frames follow standard Sinitic patterns.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002.",
    ],
    sig_lens=("Through the Signature lens, nature sentences are the land's own "
              "testimony: 黄河, 汾河 - the rivers that raised the Jin people. "
              "To speak of them in Jin is to sign the deed of the homeland."),
)

E(
    key="jin_shopping", name="Jin Chinese Shopping and Money Sentences",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Jin sentences for the market, prices, bargaining, and paying -
        each in characters, romanization, and English. 多少钱 tu1-ʂau2
        tsʰien2 (how much?). 太贵了 tʰai3 kui3-lə (too expensive). 便宜点儿
        pʰien1-i1-tier2 (cheaper, please). 能便宜吗 nəŋ2 pʰien1-i1 ma (can it
        be cheaper?). 成交 tsʰəŋ2-tɕiau1 (deal). 我买了 ŋəʔ4 mai2-lə (I'll
        take it). 不要了 puʔ4-iau3-lə (don't want it). 再看看 tsai3 kʰan3-kʰan3
        (just looking). 有新的吗 iəu2 xin1-tiəʔ4 ma (do you have new ones?).
        这个好吃吗 tsəʔ4-kə3 hau2-tsʰəʔ4 ma (is this tasty?). 称两斤
        tsʰəŋ3 liaŋ2-tɕin1 (weigh two jin). 找钱 tsau2-tsʰien2 (give change).
        一共多少 iəʔ4-kuŋ3 tu1-ʂau2 (how much altogether?). 可以刷卡吗
        kʰə2-i2 ʂuaʔ4-kʰa2 ma (can I pay by card?). 开发票 kʰai1 faʔ4-pʰiau3
        (issue a receipt). 这是找你的 tsəʔ4 ʂɿ3 tsau2 ni2-tiəʔ4 (here's your
        change). 谢谢惠顾 xie3-xie3 xui3-ku3 (thanks for your patronage).
        欢迎再来 huan1-iŋ1 tsai3-lai1 (come again). 价钱公道 tɕia3-tsʰien2
        kuŋ1-tau3 (fair price). 童叟无欺 tʰuŋ2-səu2 u2-tsʰi1 (honest to young
        and old). Twenty sentences, one Shanxi market."""),
    how_it_works=textwrap.dedent("""\
        This record teaches shopping as a bargaining dance in three moves:
        ask (多少钱), counter (便宜点儿), close (成交 / 不要了). The learner
        role-plays both shopkeeper and customer, because in Shanxi markets
        both sides enjoy the dance. Money words (块, 毛, 价钱) are drilled
        with real or play cash. The demo audits all twenty sentences and
        checks anchor words (价钱, 成交, 便宜, 发票) against the record
        text."""),
    key_points=[
        "多少钱 tu1-ʂau2 tsʰien2 - how much?",
        "太贵了 tʰai3 kui3-lə - too expensive.",
        "便宜点儿 pʰien1-i1-tier2 - cheaper, please.",
        "能便宜吗 nəŋ2 pʰien1-i1 ma - can it be cheaper?",
        "成交 tsʰəŋ2-tɕiau1 - deal.",
        "我买了 ŋəʔ4 mai2-lə - I'll take it.",
        "不要了 puʔ4-iau3-lə - don't want it.",
        "再看看 tsai3 kʰan3-kʰan3 - just looking.",
        "有新的吗 iəu2 xin1-tiəʔ4 ma - do you have new ones?",
        "这个好吃吗 tsəʔ4-kə3 hau2-tsʰəʔ4 ma - is this tasty?",
        "称两斤 tsʰəŋ3 liaŋ2-tɕin1 - weigh two jin.",
        "找钱 tsau2-tsʰien2 - give change.",
        "一共多少 iəʔ4-kuŋ3 tu1-ʂau2 - how much altogether?",
        "可以刷卡吗 kʰə2-i2 ʂuaʔ4-kʰa2 ma - can I pay by card?",
        "开发票 kʰai1 faʔ4-pʰiau3 - issue a receipt.",
        "这是找你的 tsəʔ4 ʂɿ3 tsau2 ni2-tiəʔ4 - here's your change.",
        "谢谢惠顾 xie3-xie3 xui3-ku3 - thanks for your patronage.",
        "欢迎再来 huan1-iŋ1 tsai3-lai1 - come again.",
        "价钱公道 tɕia3-tsʰien2 kuŋ1-tau3 - fair price.",
        "童叟无欺 tʰuŋ2-səu2 u2-tsʰi1 - honest to young and old.",
    ],
    requirements=[
        "Role-play a full market bargaining in Jin, both sides.",
        "Practice money amounts 1-1000 until instant.",
    ],
    standards=[
        "Bargaining frames follow documented northern market conventions.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Qiao Quansheng 乔全生. 晋方言研究的历史、现状与未来. On Jin sociolinguistic research.",
    ],
    sig_lens=("Through the Signature lens, the market is where Jin seals its "
              "deals aloud: 多少钱, 成交 - every bargain a spoken contract, "
              "every 找钱 exact. Shanxi merchants built fortunes on such "
              "seals."),
)

E(
    key="jin_social", name="Jin Chinese Friendship and Social Life Sentences",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Jin sentences for meeting people, invitations, and
        celebrations - each in characters, romanization, and English. 你叫甚
        名字 ni2 tɕiau3 ʂən2 miŋ2-tsɿ (what's your name?). 我叫___ ŋəʔ4
        tɕiau3 ___ (my name is ___). 很高兴认识你 xən2 kau1-xiŋ3 zən3-ʂəʔ4
        ni2 (nice to meet you). 你是哪里人 ni2 ʂɿ3 na2-li2 zən1 (where are you
        from?). 我是太原人 ŋəʔ4 ʂɿ3 tʰai3-yøn2 zən1 (I'm from Taiyuan). 交个朋友
        tɕiau1-kə3 pʰəŋ1-iəu3 (let's be friends). 有空来玩 iəu2-kʰuŋ3 lai2
        uan2 (come visit when free). 来我家吃饭 lai2 ŋəʔ4-tɕia1 tsʰəʔ4-fan3
        (come eat at my home). 干杯 kan1-pei1 (cheers). 生日快乐 ʂəŋ1-zɿ3
        kʰuai3-lə3 (happy birthday). 祝你健康 tsu3 ni2 tɕien3-kʰaŋ1 (wish you
        health). 新婚快乐 xin1-xun1 kʰuai3-lə3 (happy wedding). 恭喜发财
        kuŋ1-xi1 faʔ4-tsʰai2 (wishing prosperity). 大家一起玩 ta3-tɕia1
        iəʔ4-tsʰi2 uan2 (everyone have fun together). 唱个歌 tsʰaŋ3-kə3 kə1
        (sing a song). 跳个舞 tʰiau3-kə3 u2 (dance a dance). 照张相 tsau3-tsaŋ1
        xiaŋ3 (take a photo). 玩得开心 uan2-təʔ4 kʰai1-xin1 (have fun). 下次再聚
        xia3-tsʰɿ3 tsai3 tɕy3 (let's gather again). 再见 tsai3-tɕien3
        (goodbye). Twenty sentences, one Shanxi friendship."""),
    how_it_works=textwrap.dedent("""\
        This record teaches social language as a party in order: introductions
        (你叫甚名字), warming up (交个朋友), toasting (干杯), celebrating
        (生日快乐), parting (下次再聚, 再见). The learner hosts an imaginary
        gathering, greeting each guest in Jin. Name-asking and hometown
        sentences are drilled as the two questions every Shanxi meeting
        starts with. The demo audits all twenty sentences and checks anchor
        words (朋友, 生日快乐, 干杯, 再见) against the record text."""),
    key_points=[
        "你叫甚名字 ni2 tɕiau3 ʂən2 miŋ2-tsɿ - what's your name?",
        "我叫___ ŋəʔ4 tɕiau3 ___ - my name is ___.",
        "很高兴认识你 xən2 kau1-xiŋ3 zən3-ʂəʔ4 ni2 - nice to meet you.",
        "你是哪里人 ni2 ʂɿ3 na2-li2 zən1 - where are you from?",
        "我是太原人 ŋəʔ4 ʂɿ3 tʰai3-yøn2 zən1 - I'm from Taiyuan.",
        "交个朋友 tɕiau1-kə3 pʰəŋ1-iəu3 - let's be friends.",
        "有空来玩 iəu2-kʰuŋ3 lai2 uan2 - come visit when free.",
        "来我家吃饭 lai2 ŋəʔ4-tɕia1 tsʰəʔ4-fan3 - come eat at my home.",
        "干杯 kan1-pei1 - cheers.",
        "生日快乐 ʂəŋ1-zɿ3 kʰuai3-lə3 - happy birthday.",
        "祝你健康 tsu3 ni2 tɕien3-kʰaŋ1 - wish you health.",
        "新婚快乐 xin1-xun1 kʰuai3-lə3 - happy wedding.",
        "恭喜发财 kuŋ1-xi1 faʔ4-tsʰai2 - wishing prosperity.",
        "大家一起玩 ta3-tɕia1 iəʔ4-tsʰi2 uan2 - everyone have fun together.",
        "唱个歌 tsʰaŋ3-kə3 kə1 - sing a song.",
        "跳个舞 tʰiau3-kə3 u2 - dance a dance.",
        "照张相 tsau3-tsaŋ1 xiaŋ3 - take a photo.",
        "玩得开心 uan2-təʔ4 kʰai1-xin1 - have fun.",
        "下次再聚 xia3-tsʰɿ3 tsai3 tɕy3 - let's gather again.",
        "再见 tsai3-tɕien3 - goodbye.",
    ],
    requirements=[
        "Host an imaginary gathering, greeting each guest in Jin.",
        "Learn to ask the two opener questions (name, hometown) fluently.",
    ],
    standards=[
        "Social frames follow documented Shanxi conventions.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Qiao Quansheng 乔全生. 晋方言研究的历史、现状与未来. On Jin sociolinguistic research.",
    ],
    sig_lens=("Through the Signature lens, friendship sentences are the social "
              "seals: 干杯, 交个朋友 - every toast a small oath, every "
              "introduction a door opened. Shanxi friendship is sealed in "
              "noodles and toasts."),
)

E(
    key="jin_tech", name="Jin Chinese Technology and Communication Sentences",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty Jin sentences for phone, internet, computer, and messaging -
        each in characters, romanization, and English. 我的手机 ŋəʔ4-tiəʔ4
        ʂəu2-tɕi1 (my phone). 手机没电了 ʂəu2-tɕi1 mei2-tien3-lə (the phone is
        out of battery). 充电 tsʰuŋ1-tien3 (charge it). 打电话 ta2-tien3-hua3
        (make a call). 接电话 tɕie1-tien3-hua3 (answer the call). 喂，你好
        uei3, ni2-hau3 (hello, on the phone). 信号不好 xin3-xau3 puʔ4-hau2
        (bad signal). 发个微信 faʔ4-kə3 uei1-xin3 (send a WeChat message).
        加个微信 tɕia1-kə3 uei1-xin3 (add me on WeChat). 密码是甚 mi3-ma2 ʂɿ3
        ʂən2 (what's the password?). 连上网了 lien2-ʂaŋ3 uaŋ2-lə (connected to
        the internet). 网速很快 uaŋ2-su3 xən2 kʰuai3 (fast internet). 打开电脑
        ta2-kʰai1 tien3-nau2 (turn on the computer). 关机 kuan1-tɕi1 (shut
        down). 下载好了 xia3-tsai3 hau2-lə (downloaded). 发邮件 faʔ4
        iəu2-tɕien3 (send an email). 看视频 kʰan3 ʂɿ3-pʰin2 (watch videos).
        拍照 tsau3-xiaŋ3 (take a photo). 录像 lu3-xiaŋ3 (record video). 手机
        支付 ʂəu2-tɕi1 tsɿ1-fu3 (pay by phone). 二维码 ər3-uei2-ma2 (QR code).
        Twenty sentences, one connected Shanxi."""),
    how_it_works=textwrap.dedent("""\
        This record teaches tech language as tasks: the learner performs each
        phone/computer action narrating in Jin (打开电脑, 发个微信). Phone-call
        phrases (喂, 信号不好) are drilled as a call role-play. The modern
        words (微信, 二维码, 密码) show Jin alive in the digital age - the old
        tones carrying new meanings. The demo audits all twenty sentences and
        checks anchor words (手机, 电脑, 密码, 微信) against the record
        text."""),
    key_points=[
        "我的手机 ŋəʔ4-tiəʔ4 ʂəu2-tɕi1 - my phone.",
        "手机没电了 ʂəu2-tɕi1 mei2-tien3-lə - the phone is out of battery.",
        "充电 tsʰuŋ1-tien3 - charge it.",
        "打电话 ta2-tien3-hua3 - make a call.",
        "接电话 tɕie1-tien3-hua3 - answer the call.",
        "喂，你好 uei3, ni2-hau3 - hello, on the phone.",
        "信号不好 xin3-xau3 puʔ4-hau2 - bad signal.",
        "发个微信 faʔ4-kə3 uei1-xin3 - send a WeChat message.",
        "加个微信 tɕia1-kə3 uei1-xin3 - add me on WeChat.",
        "密码是甚 mi3-ma2 ʂɿ3 ʂən2 - what's the password?",
        "连上网了 lien2-ʂaŋ3 uaŋ2-lə - connected to the internet.",
        "网速很快 uaŋ2-su3 xən2 kʰuai3 - fast internet.",
        "打开电脑 ta2-kʰai1 tien3-nau2 - turn on the computer.",
        "关机 kuan1-tɕi1 - shut down.",
        "下载好了 xia3-tsai3 hau2-lə - downloaded.",
        "发邮件 faʔ4 iəu2-tɕien3 - send an email.",
        "看视频 kʰan3 ʂɿ3-pʰin2 - watch videos.",
        "拍照 tsau3-xiaŋ3 - take a photo; 录像 lu3-xiaŋ3 - record video.",
        "手机支付 ʂəu2-tɕi1 tsɿ1-fu3 - pay by phone; 二维码 ər3-uei2-ma2 - QR code.",
        "Jin carries modern life in the old tones - the language is fully alive.",
    ],
    requirements=[
        "Narrate each phone/computer action in Jin as you do it.",
        "Role-play a phone call with 喂 and 信号不好.",
    ],
    standards=[
        "Tech vocabulary follows current mainland Chinese usage in Jin pronunciation.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002.",
    ],
    sig_lens=("Through the Signature lens, tech sentences prove the covenant is "
              "alive: the thousand-year tones now carry 微信 and 二维码 without "
              "breaking. Jin signs the future with the same seal it used for "
              "the past."),
)

E(
    key="jin_tenses", name="Jin Chinese Verb Tenses in Sentences",
    group="Advanced", ladder_rank=7, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Jin verb tenses and aspects in sentences - five or more translated
        sentences per tense. Jin verbs don't conjugate; time is marked by
        aspect particles and time words. Habitual (天天 every day, 常常
        often): 我天天跑步 ŋəʔ4 tʰien1-tʰien1 pʰau2-pu3 (I run every day);
        他常常来 tʰa1 tsʰaŋ2-tsʰaŋ2 lai1 (he often comes); 我每天喝茶
        ŋəʔ4 mei2-tʰien1 xəʔ4-tsʰa1 (I drink tea daily); 她天天做饭 tʰa1
        tʰien1-tʰien1 tsu3-fan3 (she cooks daily); 我们常常见面 ŋəʔ4-mən1
        tsʰaŋ2-tsʰaŋ2 tɕien3-mien3 (we meet often). Ongoing (在, 正在): 他在吃饭
        tʰa1 tsai3 tsʰəʔ4-fan3 (he is eating); 我在看书 ŋəʔ4 tsai3 kʰan3-ʂu1
        (I am reading); 她正在开会 tʰa1 tsəŋ3-tsai3 kʰai1-xui3 (she is in a
        meeting); 孩子们在玩 xai2-tsɿ-mən1 tsai3 uan2 (the children are
        playing); 正在下雨 tsəŋ3-tsai3 xia3-y1 (it is raining).
        Completed (了): 我吃了 ŋəʔ4 tsʰəʔ4-lə (I ate); 他走了 tʰa1 tsəu2-lə
        (he left); 功课做完了 kuŋ1-kʰə3 tsu3-uan2-lə (homework is done); 电影
        看完了 tien3-iŋ2 kʰan3-uan2-lə (finished the movie); 饭做好了
        fan3 tsu3-hau2-lə (the meal is ready). Experienced (过): 我去过平遥
        ŋəʔ4 tsʰɿ3-kuə3 pʰiŋ2-iau2 (I have been to Pingyao); 我吃过刀削面
        ŋəʔ4 tsʰəʔ4-kuə3 tau1-xiau1-mien3 (I have eaten knife-cut noodles);
        你看过吗 ni2 kʰan3-kuə3 ma (have you seen it?); 他来过 tʰa1
        lai2-kuə3 (he has been here); 我没去过 ŋəʔ4 mei2 tsʰɿ3-kuə3 (I have
        never been). Future (要, 会, 明天): 明天我要去太原 miŋ2-tʰien1 ŋəʔ4
        iau3 tsʰɿ3 tʰai3-yøn2 (tomorrow I will go to Taiyuan); 会下雨 xui3
        xia3-y1 (it will rain); 我要买书 ŋəʔ4 iau3 mai2 ʂu1 (I will buy books);
        他会来 tʰa1 xui3 lai1 (he will come); 明年见 miŋ2-nien2 tɕien3 (see
        you next year). Negative past (没): 我没吃早饭 ŋəʔ4 mei2 tsʰəʔ4
        tsau2-fan3 (I didn't eat breakfast); 他没来 tʰa1 mei2 lai1 (he didn't
        come). Time lives in particles, not in the verb."""),
    how_it_works=textwrap.dedent("""\
        This record teaches tense as six toolboxes: habitual, ongoing,
        completed, experienced, future, negative-past. The learner takes one
        verb (吃) and runs it through all six boxes (我天天吃, 我在吃,
        我吃了, 我吃过, 我要吃, 我没吃) - feeling how Jin keeps the verb
        still and moves time around it. Each box gets five model sentences,
        then the learner converts: given 我吃饭, produce all six forms. The
        demo runs a grammar drill asserting each aspect particle's position."""),
    key_points=[
        "Habitual (天天/常常): 我天天跑步 ŋəʔ4 tʰien1-tʰien1 pʰau2-pu3 - I run every day.",
        "Ongoing (在/正在): 他在吃饭 tʰa1 tsai3 tsʰəʔ4-fan3 - he is eating.",
        "Completed (了): 我吃了 ŋəʔ4 tsʰəʔ4-lə - I ate.",
        "Experienced (过): 我去过平遥 ŋəʔ4 tsʰɿ3-kuə3 pʰiŋ2-iau2 - I have been to Pingyao.",
        "Future (要/会): 明天我要去太原 miŋ2-tʰien1 ŋəʔ4 iau3 tsʰɿ3 tʰai3-yøn2 - tomorrow I will go to Taiyuan.",
        "Negative past (没): 我没吃早饭 ŋəʔ4 mei2 tsʰəʔ4 tsau2-fan3 - I didn't eat breakfast.",
        "Verbs never conjugate - time is marked by particles and time words.",
        "Convert drill: one verb through all six boxes.",
        "在 marks ongoing action; 正在 emphasizes right-now.",
        "过 marks life experience - 我吃过刀削面 is a badge of honor.",
    ],
    requirements=[
        "Run five verbs through all six tense boxes.",
        "Tell your yesterday in Jin using 了/过/没 correctly.",
    ],
    standards=[
        "Aspect particles (了/过/着/在) follow documented Jin usage.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002. Jin aspect system.",
        "Yan M.M. Introduction to Chinese Dialectology. LINCOM Europa; 2006.",
    ],
    sig_lens=("Through the Signature lens, tense is time sealed in particles: 了 "
              "closes the past like a stamp, 过 keeps experience like a scar, "
              "要 opens the future like a door. Jin does not bend its verbs - "
              "it frames time around them, steady as stone."),
)

E(
    key="jin_qa", name="Jin Chinese Questions and Answers",
    group="Advanced", ladder_rank=7, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty Jin question-and-answer pairs covering who, what, where, when,
        why, and how - each in characters, romanization, and English. 你是
        甚人? ni2 ʂɿ3 ʂən2-zən1 - who are you? / 我是学生 ŋəʔ4 ʂɿ3 xɿəʔ4-ʂəŋ1
        - I am a student. 这是甚? tsəʔ4 ʂɿ3 ʂən2 - what is this? / 这是书
        tsəʔ4 ʂɿ3 ʂu1 - this is a book. 你去甚地方? ni2 tsʰɿ3 ʂən2-ti3-faŋ1 -
        where are you going? / 我去学校 ŋəʔ4 tsʰɿ3 xɿəʔ4-xiau3 - I'm going to
        school. 你甚时候来? ni2 ʂən2-sɿ1-həu3 lai1 - when are you coming? /
        明天来 miŋ2-tʰien1 lai1 - coming tomorrow. 为甚不去? uei3-ʂən2
        puʔ4-tsʰɿ3 - why not go? / 太忙了 tʰai3 maŋ2-lə - too busy. 怎么做?
        tsən2-mə tsu3 - how to do it? / 这样做 tsəʔ4-iaŋ3 tsu3 - do it like
        this. 多少? tu1-ʂau2 - how much? / 五块 u3-kʰuai3 - five yuan. 哪一个?
        na2-iəʔ4-kə3 - which one? / 这个 tsəʔ4-kə3 - this one. 好吃吗?
        hau2-tsʰəʔ4 ma - tasty? / 好吃 hau2-tsʰəʔ4 - tasty. 你去吗? ni2 tsʰɿ3
        ma - are you going? / 去 tsʰɿ3 - going. 甚意思? ʂən2 i3-sɿ1 - what
        does it mean? / 就是这个意思 tɕiəu3 ʂɿ3 tsəʔ4-kə3 i3-sɿ1 - it means
        just this. 几个人? tɕi2-kə3 zən1 - how many people? / 三个人
        san1-kə3 zən1 - three people. 甚时候走? ʂən2-sɿ1-həu3 tsəu2 - when to
        leave? / 现在走 xien3-tsai3 tsəu2 - leave now. 为甚学晋语? uei3-ʂən2
        xɿəʔ4 tɕin3-y1 - why learn Jin? / 因为好听 in1-uei3 hau2-tʰiŋ1 -
        because it sounds good. 你会说吗? ni2 xui3 ʂuə1 ma - can you speak
        it? / 会一点 xui3 iəʔ4-tier2 - a little. 明白吗? miŋ2-pəʔ4 ma - do
        you understand? / 明白 miŋ2-pəʔ4 - understood. 二十问答, one curious
        mind."""),
    how_it_works=textwrap.dedent("""\
        This record teaches questions as a detective game: the learner gets
        the answer and must build the question (answer: 我是学生 → question:
        你是甚人?). The six question words (甚, 甚人, 甚地方, 甚时候, 为甚,
        怎/怎么做) are drilled as the six keys that open every conversation.
        吗/吧/呢 question particles are practiced by converting statements to
        questions. The demo quizzes the eight anchor question words with a
        perfect-score assertion."""),
    key_points=[
        "甚 ʂən2 (what): 这是甚 tsəʔ4 ʂɿ3 ʂən2 - what is this? / 这是书 tsəʔ4 ʂɿ3 ʂu1 - this is a book.",
        "甚人 ʂən2-zən1 (who): 你是甚人 ni2 ʂɿ3 ʂən2-zən1 - who are you? / 我是学生 ŋəʔ4 ʂɿ3 xɿəʔ4-ʂəŋ1 - I am a student.",
        "甚地方 ʂən2-ti3-faŋ1 (where): 你去甚地方 ni2 tsʰɿ3 ʂən2-ti3-faŋ1 - where are you going? / 我去学校 ŋəʔ4 tsʰɿ3 xɿəʔ4-xiau3 - I'm going to school.",
        "甚时候 ʂən2-sɿ1-həu3 (when): 你甚时候来 ni2 ʂən2-sɿ1-həu3 lai1 - when are you coming? / 明天来 miŋ2-tʰien1 lai1 - coming tomorrow.",
        "为甚 uei3-ʂən2 (why): 为甚不去 uei3-ʂən2 puʔ4-tsʰɿ3 - why not go? / 太忙了 tʰai3 maŋ2-lə - too busy.",
        "怎 tsən2 / 怎么做 tsən2-mə tsu3 (how): 怎么做 tsən2-mə tsu3 - how to do it? / 这样做 tsəʔ4-iaŋ3 tsu3 - do it like this.",
        "多少 tu1-ʂau2 (how much): 多少 tu1-ʂau2 - how much? / 五块 u3-kʰuai3 - five yuan.",
        "哪一个 na2-iəʔ4-kə3 (which one): 哪一个 na2-iəʔ4-kə3 - which one? / 这个 tsəʔ4-kə3 - this one.",
        "Particles: 吗 ma (yes/no), 吧 pa (suggestion), 呢 nə (follow-up).",
        "Detective drill: given the answer, build the question.",
    ],
    requirements=[
        "Build questions from ten given answers.",
        "Hold a 5-minute Q&A entirely in Jin.",
    ],
    standards=[
        "Question words follow documented Jin usage (甚-series).",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002. Jin interrogatives.",
        "Kurpaska M. Chinese Language(s). de Gruyter; 2010.",
    ],
    sig_lens=("Through the Signature lens, questions are the open seals: 甚, "
              "为甚 - every question an unsealed envelope handed to another "
              "mind. Jin asks straight, the Shanxi way, and every answer "
              "re-seals the bond."),
)

E(
    key="jin_commands", name="Jin Chinese Commands and Requests",
    group="Advanced", ladder_rank=7, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty Jin imperatives and polite requests, formal vs informal -
        each in characters, romanization, and English. Bare commands: 吃饭
        tsʰəʔ4-fan3 (eat!), 坐 tsu3 (sit!), 来 lai1 (come!), 看 kʰan3 (look!),
        快点 kʰuai3-tier2 (hurry!). Polite with 请: 请坐 tsʰiŋ2-tsu3 (please
        sit), 请喝茶 tsʰiŋ2 xəʔ4-tsʰa1 (please have tea), 请进 tsʰiŋ2-tɕin3
        (please come in), 请慢用 tsʰiŋ2 man3-iəuŋ3 (please enjoy your meal).
        Formal requests: 麻烦你帮个忙 ma2-fan1 ni2 paŋ1-kə3 maŋ2 (could you
        help me?), 请问一下 tsʰiŋ2-uən3 iəʔ4-xia3 (may I ask something?),
        劳驾让一下 lau2-tɕia3 zaŋ3 iəʔ4-xia3 (excuse me, let me pass).
        Negative commands: 不要吵 puʔ4-iau3 tsʰau2 (don't make noise), 别动
        pieʔ4 tuŋ3 (don't move), 别客气 pieʔ4-kʰəʔ4-tsʰi3 (don't stand on
        ceremony). Suggestions: 走吧 tsəu2-pa (let's go), 吃吧 tsʰəʔ4-pa
        (let's eat), 歇会儿吧 xie1-xuər3 pa (let's rest a bit). Hospitality:
        多吃点儿 tu1 tsʰəʔ4-tier2 (eat more), 再喝一杯 tsai3 xəʔ4 iəʔ4-pei1
        (have another cup). Formal vs informal: 请问您贵姓 tsʰiŋ2-uən3 nin2
        kui3-xiŋ3 (may I ask your honorable name?) vs 你叫甚名字 ni2 tɕiau3
        ʂən2 miŋ2-tsɿ (what's your name?). Twenty orders, given kindly."""),
    how_it_works=textwrap.dedent("""\
        This record teaches commands as a politeness ladder: bare verb ( Sit!),
        请 + verb (please sit), 麻烦/劳驾 frames (formal requests). The
        learner practices giving orders to family (bare), requests to friends
        (请), and formal asks to strangers (麻烦你). Negative commands (不要,
        别) are drilled as the stop-signs. The hospitality set (多吃点儿,
        再喝一杯) is practiced as hosting - because in Shanxi, ordering
        guests to eat more is love. The demo runs a grammar drill asserting
        each politeness marker's position."""),
    key_points=[
        "Bare: 吃饭 tsʰəʔ4-fan3 (eat!), 快点 kʰuai3-tier2 (hurry!).",
        "Polite 请: 请坐 tsʰiŋ2-tsu3 (please sit), 请喝茶 tsʰiŋ2 xəʔ4-tsʰa1 (please have tea).",
        "Formal: 麻烦你帮个忙 ma2-fan1 ni2 paŋ1-kə3 maŋ2 (could you help me?).",
        "Negative: 不要吵 puʔ4-iau3 tsʰau2 (don't make noise), 别动 pieʔ4 tuŋ3 (don't move).",
        "Suggestions: 走吧 tsəu2-pa (let's go), 歇会儿吧 xie1-xuər3 pa (let's rest a bit).",
        "Hospitality: 多吃点儿 tu1 tsʰəʔ4-tier2 (eat more), 再喝一杯 tsai3 xəʔ4 iəʔ4-pei1 (have another cup).",
        "Formal vs informal: 请问您贵姓 (formal) vs 你叫甚名字 (casual).",
        "Politeness ladder: bare verb < 请 < 麻烦/劳驾.",
        "别客气 pieʔ4-kʰəʔ4-tsʰi3 (don't stand on ceremony) - the host's kindest order.",
        "Commands need no subject - the verb alone is the order.",
    ],
    requirements=[
        "Give orders on the politeness ladder: family, friend, stranger.",
        "Host someone using the hospitality set.",
    ],
    standards=[
        "Imperative and request frames follow documented northern conventions.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Qiao Quansheng 乔全生. 晋方言研究的历史、现状与未来. On Jin sociolinguistic research.",
    ],
    sig_lens=("Through the Signature lens, commands are seals of authority given "
              "kindly: 请坐 opens the door, 麻烦你 signs the request with "
              "respect, 多吃点儿 seals love in food. Every order in Jin "
              "carries its politeness like a stamp."),
)

E(
    key="jin_descriptions", name="Jin Chinese Descriptions of People and Places",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty Jin sentences describing people, places, and things in detail -
        each in characters, romanization, and English. 平遥古城很美
        pʰiŋ2-iau2 ku2-tsʰəŋ2 xən2 mei2 (the Pingyao ancient city is beautiful).
        古城墙很高 ku2-tsʰəŋ2-tsʰiaŋ2 xən2 kau1 (the old city wall is very
        tall). 云冈石窟很壮观 yn2-kaŋ1 ʂəʔ4-kʰu1 xən2 tsuaŋ3-kuan1 (the Yungang
        Grottoes are spectacular). 大佛很慈祥 ta3-fəʔ4 xən2 tsʰɿ2-xiaŋ2 (the
        great Buddha is very kind-faced). 刀削面很好吃 tau1-xiau1-mien3 xən2
        hau2-tsʰəʔ4 (knife-cut noodles are delicious). 老陈醋很香
        lau2-tsʰən2-tsʰu3 xən2 xiaŋ1 (aged vinegar smells wonderful). 汾河水很
        清 fən2-xə2 ʂui2 xən2 tsʰiŋ1 (the Fen River water is very clear).
        太原是山西的省会 tʰai3-yøn2 ʂɿ3 ʂan1-xi1-tiəʔ4 ʂəŋ2-xui3 (Taiyuan is
        Shanxi's capital). 街道很干净 tɕie1-tau3 xən2 kan1-tɕiŋ3 (the streets
        are very clean). 夜晚的灯很亮 ie3-uan2-tiəʔ4 təŋ1 xən2 liaŋ3 (the
        night lights are very bright). 他个子很高 tʰa1 kə3-tsɿ xən2 kau1 (he
        is very tall). 她眼睛很大 tʰa1 ien2-tɕiŋ1 xən2 ta3 (her eyes are very
        big). 老人很和蔼 lau2-zən1 xən2 xə2-ai2 (the old man is very kind).
        小孩很可爱 siau2-xai2 xən2 kʰə2-ai3 (the child is very cute). 这件衣服
        很漂亮 tsəʔ4-tɕien3 i1-fuʔ4 xən2 pʰiau3-liaŋ1 (this clothing is very
        pretty). 房子很宽敞 faŋ1-tsɿ xən2 kʰuan1-tsʰaŋ2 (the house is very
        spacious). 院子里的花开了 yøn3-tsɿ-li2-tiəʔ4 xua1 kʰai1-lə (the
        courtyard flowers are blooming). 山上的雪很白 ʂan1-ʂaŋ3-tiəʔ4 xɿəʔ4
        xən2 pəʔ4 (the mountain snow is very white). 这里的人很热情
        tsəʔ4-li2-tiəʔ4 zən1 xən2 zəʔ4-tsʰiŋ2 (the people here are very warm).
        山西是个好地方 ʂan1-xi1 ʂɿ3-kə3 hau2 ti3-faŋ1 (Shanxi is a good
        place). Twenty brushstrokes, one Shanxi portrait."""),
    how_it_works=textwrap.dedent("""\
        This record teaches description as painting: each sentence adds one
        brushstroke (color, size, feeling) to a person or place. The learner
        describes their own town, then a person they love, using the
        很 + adjective frame and the detail patterns (的-phrases, 在-phrases).
        Shanxi landmarks (平遥古城, 云冈石窟, 汾河) are described first as
        models, then the learner's own world. The demo audits all twenty
        sentences and checks anchor words (平遥古城, 云冈石窟, 刀削面,
        汾河) against the record text."""),
    key_points=[
        "平遥古城很美 pʰiŋ2-iau2 ku2-tsʰəŋ2 xən2 mei2 - the Pingyao ancient city is beautiful.",
        "古城墙很高 ku2-tsʰəŋ2-tsʰiaŋ2 xən2 kau1 - the old city wall is very tall.",
        "云冈石窟很壮观 yn2-kaŋ1 ʂəʔ4-kʰu1 xən2 tsuaŋ3-kuan1 - the Yungang Grottoes are spectacular.",
        "大佛很慈祥 ta3-fəʔ4 xən2 tsʰɿ2-xiaŋ2 - the great Buddha is very kind-faced.",
        "刀削面很好吃 tau1-xiau1-mien3 xən2 hau2-tsʰəʔ4 - knife-cut noodles are delicious.",
        "老陈醋很香 lau2-tsʰən2-tsʰu3 xən2 xiaŋ1 - aged vinegar smells wonderful.",
        "汾河水很清 fən2-xə2 ʂui2 xən2 tsʰiŋ1 - the Fen River water is very clear.",
        "太原是山西的省会 tʰai3-yøn2 ʂɿ3 ʂan1-xi1-tiəʔ4 ʂəŋ2-xui3 - Taiyuan is Shanxi's capital.",
        "街道很干净 tɕie1-tau3 xən2 kan1-tɕiŋ3 - the streets are very clean.",
        "夜晚的灯很亮 ie3-uan2-tiəʔ4 təŋ1 xən2 liaŋ3 - the night lights are very bright.",
        "他个子很高 tʰa1 kə3-tsɿ xən2 kau1 - he is very tall.",
        "她眼睛很大 tʰa1 ien2-tɕiŋ1 xən2 ta3 - her eyes are very big.",
        "老人很和蔼 lau2-zən1 xən2 xə2-ai2 - the old man is very kind.",
        "小孩很可爱 siau2-xai2 xən2 kʰə2-ai3 - the child is very cute.",
        "这件衣服很漂亮 tsəʔ4-tɕien3 i1-fuʔ4 xən2 pʰiau3-liaŋ1 - this clothing is very pretty.",
        "房子很宽敞 faŋ1-tsɿ xən2 kʰuan1-tsʰaŋ2 - the house is very spacious.",
        "院子里的花开了 yøn3-tsɿ-li2-tiəʔ4 xua1 kʰai1-lə - the courtyard flowers are blooming.",
        "山上的雪很白 ʂan1-ʂaŋ3-tiəʔ4 xɿəʔ4 xən2 pəʔ4 - the mountain snow is very white.",
        "这里的人很热情 tsəʔ4-li2-tiəʔ4 zən1 xən2 zəʔ4-tsʰiŋ2 - the people here are very warm.",
        "山西是个好地方 ʂan1-xi1 ʂɿ3-kə3 hau2 ti3-faŋ1 - Shanxi is a good place.",
    ],
    requirements=[
        "Describe your town in ten Jin sentences.",
        "Describe a person you love in five Jin sentences.",
    ],
    standards=[
        "Descriptive frames follow standard Sinitic patterns.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Documented Shanxi landmarks: 平遥古城 (Pingyao ancient city), 云冈石窟 (Yungang Grottoes), 汾河 (Fen River).",
    ],
    sig_lens=("Through the Signature lens, descriptions are portraits sealed in "
              "words: 平遥古城, 云冈石窟 - to describe Shanxi's wonders in Jin "
              "is to hang the province's portrait in its own gallery, signed "
              "in the old tones."),
)

E(
    key="jin_story1", name="Jin Chinese Story I: The Noodle Shop",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence simple story in Jin - present tense, everyday words -
        with line-by-line English translation. 太原有一家面馆 tʰai3-yøn2
        iəu2 iəʔ4-tɕia1 mien3-kuan2 (in Taiyuan there is a noodle shop).
        面馆很小，但是人很多 mien3-kuan2 xən2 siau2, tan3-ʂɿ3 zən1 xən2 tu1
        (the shop is small, but there are many people). 老板姓王
        lau2-pan2 xiŋ3 uaŋ2 (the boss's surname is Wang). 他做的刀削面很好吃
        tʰa1 tsu3-tiəʔ4 tau1-xiau1-mien3 xən2 hau2-tsʰəʔ4 (his knife-cut
        noodles are delicious). 中午大家都来吃面 tsuŋ1-u2 ta3-tɕia1 tu1
        lai2 tsʰəʔ4-mien3 (at noon everyone comes to eat noodles). 一碗面十块钱
        iəʔ4-uan2 mien3 səʔ4-kʰuai3 tsʰien2 (a bowl of noodles is ten yuan).
        吃面要加醋 tsʰəʔ4-mien3 iau3 tɕia1-tsʰu3 (eating noodles needs
        vinegar). 山西人爱吃醋 ʂan1-xi1 zən1 ai3 tsʰəʔ4-tsʰu3 (Shanxi people
        love vinegar). 吃完买单 tsʰəʔ4-uan2 mai2-tan1 (after eating, pay the
        bill). 大家都说不赖 ta3-tɕia1 tu1 ʂuə1 puʔ4-lai3 (everyone says it's
        good). Ten sentences, one steaming bowl."""),
    how_it_works=textwrap.dedent("""\
        This record teaches reading through story: the learner reads each Jin
        line, covers the English, and retells the line in their own words.
        The story uses only present-tense frames and known vocabulary, so it
        is readable end-to-end after the foundations. New words (面馆, 碗) are
        glossed in place. The learner then continues the story with two
        sentences of their own. The demo audits all ten sentences and checks
        anchor words (面馆, 刀削面, 好吃, 买单) against the record text."""),
    key_points=[
        "太原有一家面馆 tʰai3-yøn2 iəu2 iəʔ4-tɕia1 mien3-kuan2 - in Taiyuan there is a noodle shop.",
        "面馆很小，但是人很多 mien3-kuan2 xən2 siau2, tan3-ʂɿ3 zən1 xən2 tu1 - the shop is small, but there are many people.",
        "老板姓王 lau2-pan2 xiŋ3 uaŋ2 - the boss's surname is Wang.",
        "他做的刀削面很好吃 tʰa1 tsu3-tiəʔ4 tau1-xiau1-mien3 xən2 hau2-tsʰəʔ4 - his knife-cut noodles are delicious.",
        "中午大家都来吃面 tsuŋ1-u2 ta3-tɕia1 tu1 lai2 tsʰəʔ4-mien3 - at noon everyone comes to eat noodles.",
        "一碗面十块钱 iəʔ4-uan2 mien3 səʔ4-kʰuai3 tsʰien2 - a bowl of noodles is ten yuan.",
        "吃面要加醋 tsʰəʔ4-mien3 iau3 tɕia1-tsʰu3 - eating noodles needs vinegar.",
        "山西人爱吃醋 ʂan1-xi1 zən1 ai3 tsʰəʔ4-tsʰu3 - Shanxi people love vinegar.",
        "吃完买单 tsʰəʔ4-uan2 mai2-tan1 - after eating, pay the bill.",
        "大家都说不赖 ta3-tɕia1 tu1 ʂuə1 puʔ4-lai3 - everyone says it's good.",
        "Reading method: Jin line first, English covered, retell in your own words.",
        "New words glossed in place: 面馆 (noodle shop), 碗 (bowl).",
    ],
    requirements=[
        "Read the story aloud end-to-end without stopping.",
        "Continue the story with two sentences of your own.",
    ],
    standards=[
        "Story uses present-tense frames and foundations vocabulary only.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Documented Shanxi food culture: 刀削面, 老陈醋, 不赖.",
    ],
    sig_lens=("Through the Signature lens, a story is a sealed scroll: ten "
              "sentences, one noodle shop, and the whole of Shanxi inside. "
              "To read it aloud in Jin is to unroll the scroll with your own "
              "voice."),
)

E(
    key="jin_story2", name="Jin Chinese Story II: The Pingyao Trip",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in Jin using past tenses and aspects - 了, 过,
        没 - with line-by-line English translation. 夜来我去了平遥
        ie3-lai2 ŋəʔ4 tsʰɿ3-lə pʰiŋ2-iau2 (yesterday I went to Pingyao).
        我坐火车去的 ŋəʔ4 tsu3 xu1-tsʰə1 tsʰɿ3-tiəʔ4 (I went by train).
        古城墙真高 ku2-tsʰəŋ2-tsʰiaŋ2 tsən1 kau1 (the old city wall is really
        tall). 我从来没见过这么老的城 ŋəʔ4 tsʰuŋ2-lai2 mei2 tɕien3-kuə3
        tsəʔ4-mə lau2-tiəʔ4 tsʰəŋ2 (I had never seen such an old city).
        中午吃了刀削面 tsuŋ1-u2 tsʰəʔ4-lə tau1-xiau1-mien3 (at noon I ate
        knife-cut noodles). 还买了老陈醋 xai2 mai2-lə lau2-tsʰən2-tsʰu3
        (also bought aged vinegar). 下午去了票号博物馆 xia3-u2 tsʰɿ3-lə
        pʰiau3-xau3 pəuʔ4-u3-kuan2 (in the afternoon I visited the draft-bank
        museum). 晋商真了不起 tɕin3-ʂaŋ1 tsən1 liau2-puʔ4-tsʰi2 (the Shanxi
        merchants were truly remarkable). 我拍了很多照片 ŋəʔ4 pʰai1-lə
        xən2-tu1 tsau3-pʰien3 (I took many photos). 这次旅行很难忘
        tsəʔ4-tsʰɿ3 ly2-xiŋ2 xən2 nan2-uaŋ3 (this trip is unforgettable). Ten
        sentences, one journey into the past."""),
    how_it_works=textwrap.dedent("""\
        This record teaches past narration: every sentence models 了
        (completed), 过 (experienced), or 没 (negative past) in a travel
        story. The learner underlines each aspect particle, then retells
        their own last trip using the same three particles. The Pingyao
        setting (古城墙, 票号, 晋商) teaches Shanxi history inside the grammar
        - the draft banks of Pingyao were China's first banks. The demo runs
        a grammar drill asserting each past marker's position."""),
    key_points=[
        "夜来我去了平遥 ie3-lai2 ŋəʔ4 tsʰɿ3-lə pʰiŋ2-iau2 - yesterday I went to Pingyao (了 completed).",
        "我坐火车去的 ŋəʔ4 tsu3 xu1-tsʰə1 tsʰɿ3-tiəʔ4 - I went by train (的 past emphasis).",
        "古城墙真高 ku2-tsʰəŋ2-tsʰiaŋ2 tsən1 kau1 - the old city wall is really tall.",
        "我从来没见过这么老的城 ŋəʔ4 tsʰuŋ2-lai2 mei2 tɕien3-kuə3 tsəʔ4-mə lau2-tiəʔ4 tsʰəŋ2 - I had never seen such an old city (没...过).",
        "中午吃了刀削面 tsuŋ1-u2 tsʰəʔ4-lə tau1-xiau1-mien3 - at noon I ate knife-cut noodles.",
        "还买了老陈醋 xai2 mai2-lə lau2-tsʰən2-tsʰu3 - also bought aged vinegar.",
        "下午去了票号博物馆 xia3-u2 tsʰɿ3-lə pʰiau3-xau3 pəuʔ4-u3-kuan2 - in the afternoon I visited the draft-bank museum.",
        "晋商真了不起 tɕin3-ʂaŋ1 tsən1 liau2-puʔ4-tsʰi2 - the Shanxi merchants were truly remarkable.",
        "我拍了很多照片 ŋəʔ4 pʰai1-lə xən2-tu1 tsau3-pʰien3 - I took many photos.",
        "这次旅行很难忘 tsəʔ4-tsʰɿ3 ly2-xiŋ2 xən2 nan2-uaŋ3 - this trip is unforgettable.",
        "Past markers: 了 completed, 过 experienced, 没 negative past, 的 past emphasis.",
        "Pingyao's 票号 were China's first banks - history inside the grammar.",
    ],
    requirements=[
        "Underline every aspect particle in the story.",
        "Retell your own last trip using 了/过/没.",
    ],
    standards=[
        "Past narration follows documented Jin aspect usage.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Documented Shanxi history: 平遥票号 (Pingyao draft banks), 晋商 (Shanxi merchants).",
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002.",
    ],
    sig_lens=("Through the Signature lens, the past is a sealed archive: 了 "
              "stamps each finished act, 过 keeps the experiences that made "
              "you. To tell your Pingyao trip in Jin is to file it in the "
              "oldest archive there is - memory, sealed in tone."),
)

E(
    key="jin_story3", name="Jin Chinese Story III: The Datong Plan",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story in Jin using future and conditional forms - 要,
        会, 如果, 只要 - with line-by-line English translation. 明年我要去大同
        miŋ2-nien2 ŋəʔ4 iau3 tsʰɿ3 ta3-tʰuŋ2 (next year I will go to Datong).
        我要早点起来 ŋəʔ4 iau3 tsau2-tier2 tsʰi2-lai1 (I will get up early).
        我们会去看云冈石窟 ŋəʔ4-mən1 xui3 tsʰɿ3 kʰan3 yn2-kaŋ1 ʂəʔ4-kʰu1 (we
        will visit the Yungang Grottoes). 如果下雨我就不去 zu2-kuə2 xia3-y1
        ŋəʔ4 tɕiəu3 puʔ4-tsʰɿ3 (if it rains I won't go). 只要天好就能去 tsɿ2-iau3 tʰien1 hau2
        tɕiəu3 nəŋ2 tsʰɿ3 (if the weather is good we can go). 我会带相机
        ŋəʔ4 xui3 tai3 xiaŋ3-tɕi1 (I will bring a camera). 到了大同先吃刀削面
        tau3-lə ta3-tʰuŋ2 xien1 tsʰəʔ4 tau1-xiau1-mien3 (arriving in Datong,
        first eat knife-cut noodles). 然后去看大佛 zan2-xəu3 tsʰɿ3 kʰan3
        ta3-fəʔ4 (then see the great Buddha). 这次旅行一定很棒 tsəʔ4-tsʰɿ3
        ly2-xiŋ2 iəʔ4-tiŋ3 xən2 paŋ3 (this trip will surely be wonderful).
        你会跟我一起去吗 ni2 xui3 kən1 ŋəʔ4 iəʔ4-tsʰi2 tsʰɿ3 ma (will you come
        with me?). Ten sentences, one future unfolding."""),
    how_it_works=textwrap.dedent("""\
        This record teaches future and conditional as planning: the learner
        plans a real future trip using 要 (intention), 会 (prediction), 如果
        (condition), 只要 (sufficient condition). Each form gets a frame to
        fill with the learner's own plans. The Datong/Yungang setting teaches
        northern Shanxi geography inside the grammar. The demo runs a grammar
        drill asserting each future/conditional marker's position."""),
    key_points=[
        "明年我要去大同 miŋ2-nien2 ŋəʔ4 iau3 tsʰɿ3 ta3-tʰuŋ2 - next year I will go to Datong (要 intention).",
        "我要早点起来 ŋəʔ4 iau3 tsau2-tier2 tsʰi2-lai1 - I will get up early.",
        "我们会去看云冈石窟 ŋəʔ4-mən1 xui3 tsʰɿ3 kʰan3 yn2-kaŋ1 ʂəʔ4-kʰu1 - we will visit the Yungang Grottoes (会 prediction).",
        "如果下雨我就不去 zu2-kuə2 xia3-y1 ŋəʔ4 tɕiəu3 puʔ4-tsʰɿ3 - if it rains I won't go (如果 condition).",
        "只要天好就能去 tsɿ2-iau3 tʰien1 hau2 tɕiəu3 nəŋ2 tsʰɿ3 - if the weather is good we can go (只要 sufficient condition).",
        "我会带相机 ŋəʔ4 xui3 tai3 xiaŋ3-tɕi1 - I will bring a camera.",
        "到了大同先吃刀削面 tau3-lə ta3-tʰuŋ2 xien1 tsʰəʔ4 tau1-xiau1-mien3 - arriving in Datong, first eat knife-cut noodles.",
        "然后去看大佛 zan2-xəu3 tsʰɿ3 kʰan3 ta3-fəʔ4 - then see the great Buddha.",
        "这次旅行一定很棒 tsəʔ4-tsʰɿ3 ly2-xiŋ2 iəʔ4-tiŋ3 xən2 paŋ3 - this trip will surely be wonderful.",
        "你会跟我一起去吗 ni2 xui3 kən1 ŋəʔ4 iəʔ4-tsʰi2 tsʰɿ3 ma - will you come with me?",
        "Future markers: 要 intention, 会 prediction; conditionals: 如果, 只要.",
        "Plan a real trip with these frames.",
    ],
    requirements=[
        "Plan a real future trip using 要/会/如果/只要.",
        "Convert the Pingyao past story into a future plan.",
    ],
    standards=[
        "Future and conditional frames follow standard Sinitic patterns.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Documented Shanxi geography: 大同 (Datong), 云冈石窟 (Yungang Grottoes).",
    ],
    sig_lens=("Through the Signature lens, the future is an unsealed scroll: 要 "
              "is the hand reaching for the brush, 如果 the fork in the road. "
              "To plan in Jin is to write tomorrow in the old tones before it "
              "happens."),
)

E(
    key="jin_idioms", name="Jin Chinese Idioms and Proverbs",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty Jin idioms, proverbs, and colloquial sayings - each with
        literal translation, real meaning, and an example sentence. 不赖
        puʔ4-lai3 - lit. 'not bad'; real meaning: good, fine, worthy of
        praise - Shanxi's signature compliment: 这刀削面不赖 (these noodles
        are good). 入鬼 zuʔ4-kui2 - lit. 'enter-ghost'; real meaning: to fool
        around, mess about - documented Jin with the 入 /zəʔ/ prefix: 别入鬼
        了 (stop fooling around). 圪蛋 kəʔ4-tan3 - lit. 'ge-egg'; real
        meaning: egg - the famous 圪 prefix in daily life: 圪蛋炒了 (the eggs
        are scrambled). 夜来 ie3-lai2 - lit. 'night-come'; real meaning:
        yesterday - Shanxi's own word for it: 夜来下雨了 (it rained
        yesterday). 圪梁梁 kəʔ4-liaŋ2-liaŋ2 - lit. 'ge-ridge-ridge'; real
        meaning: a ridge, a raised strip - documented Shanxi word: 圪梁梁上
        长草了 (grass grows on the ridge). 窟窿 kʰuʔ4-luŋ1 - lit. 'hole-hole'
        (from 孔 by l-fission); real meaning: a hole: 墙上有个窟窿 (there's a
        hole in the wall). 圪针 kəʔ4-tsən1 - lit. 'ge-needle'; real meaning: a
        thorn: 小心圪针 (watch out for thorns). 甚 ʂən2 - lit. 'what';
        Shanxi's all-purpose question word, the soul of Jin curiosity. 熟能生巧
        ʂəu2-nəŋ2-ʂəŋ1-tsʰiau2 - lit. 'skill begets dexterity'; real meaning:
        practice makes perfect. 一口吃不成胖子 iəʔ4-kʰəu2-tsʰəʔ4-puʔ4-tsʰəŋ2-pʰaŋ3-tsɿ3
        - lit. 'one bite can't make a fat man'; real meaning: haste makes
        waste, be patient. 吃得苦中苦，方为人上人 tsʰəʔ4-təʔ4 kʰu2-tsuŋ1-kʰu2,
        faŋ1 uei2 zən1-ʂaŋ3-zən1 - lit. 'eat the bitterest of the bitter to
        become above others'; real meaning: no pain, no gain. 心急吃不了热豆腐
        xin1-tɕi2 tsʰəʔ4-puʔ4-liau2 zəʔ4-təu3-fu - lit. 'a hasty heart can't
        eat hot tofu'; real meaning: patience wins. 好事多磨 hau2-ʂɿ3 tu1-mu2
        - good things take time. 入乡随俗 zuʔ4-xiaŋ1 suei2-səu2 - when in
        Rome. 百闻不如一见 pəʔ4-uən2 puʔ4-zu2 iəʔ4-tɕien3 - seeing is
        believing. 活到老学到老 xuəʔ4-tau3 lau2 xɿəʔ4-tau3 lau2 - never too
        old to learn. 众人拾柴火焰高 tsuŋ3-zən1 ʂəʔ4-tsʰai2 xu1-ien3 kau1 -
        many hands make light work. 滴水穿石 ti1-ʂui2 tsʰuan1-ʂəʔ4 -
        persistence breaks stone. 前人栽树后人乘凉 tsʰien2-zən1 tsai1-ʂu3
        xəu3-zən1 tsʰəŋ2-liaŋ2 - one generation plants, the next rests in
        shade. 二十谚语, one Shanxi philosophy."""),
    how_it_works=textwrap.dedent("""\
        This record teaches idioms as compressed stories: each gets literal
        translation first (the joke inside), then the real meaning, then a
        living sentence. The Jin-born words (不赖, 入鬼, 圪蛋, 夜来, 圪梁梁,
        窟窿, 圪针) are drilled as identity passwords - say them and you're
        Shanxi. The pan-Chinese proverbs (熟能生巧, 一口吃不成胖子) are
        practiced as advice to give friends. The learner picks three favorites
        and uses each in a real conversation this week. The demo quizzes ten
        anchor idioms with a perfect-score assertion."""),
    key_points=[
        "不赖 puʔ4-lai3 - lit. 'not bad'; means good, praiseworthy: 这刀削面不赖 - these noodles are good.",
        "入鬼 zuʔ4-kui2 - lit. 'enter-ghost'; means to fool around (documented Jin 入-prefix): 别入鬼了 - stop fooling around.",
        "圪蛋 kəʔ4-tan3 - lit. 'ge-egg'; means egg: 圪蛋炒了 - the eggs are scrambled.",
        "夜来 ie3-lai2 - lit. 'night-come'; means yesterday: 夜来下雨了 - it rained yesterday.",
        "圪梁梁 kəʔ4-liaŋ2-liaŋ2 - lit. 'ge-ridge-ridge'; means a ridge: 圪梁梁上长草了 - grass grows on the ridge.",
        "窟窿 kʰuʔ4-luŋ1 - lit. 'hole-hole' (from 孔 by l-fission); means a hole: 墙上有个窟窿 - there's a hole in the wall.",
        "圪针 kəʔ4-tsən1 - lit. 'ge-needle'; means a thorn: 小心圪针 - watch out for thorns.",
        "甚 ʂən2 - Shanxi's all-purpose 'what', the soul of Jin curiosity.",
        "熟能生巧 ʂəu2-nəŋ2-ʂəŋ1-tsʰiau2 - practice makes perfect.",
        "一口吃不成胖子 iəʔ4-kʰəu2-tsʰəʔ4-puʔ4-tsʰəŋ2-pʰaŋ3-tsɿ3 - one bite can't make a fat man; haste makes waste.",
        "Also: 吃得苦中苦方为人上人 (no pain no gain), 心急吃不了热豆腐 (patience wins), 好事多磨 (good things take time), 入乡随俗 (when in Rome), 百闻不如一见 (seeing is believing), 活到老学到老 (never too old to learn), 众人拾柴火焰高 (many hands), 滴水穿石 (persistence), 前人栽树后人乘凉 (plant for the next generation).",
        "Literal translation first reveals the joke inside each idiom.",
    ],
    requirements=[
        "Use three favorite idioms in real conversations this week.",
        "Explain the literal joke inside five idioms to someone.",
    ],
    standards=[
        "Jin-born words (圪-series, 入鬼, 夜来, 不赖) follow documented Shanxi usage.",
        "Proverbs are pan-Chinese sayings current in Shanxi speech.",
    ],
    citations=[
        "Documented Jin: 入鬼 'fool around' (入 /zəʔ/ prefix), 窟窿 /kʰuəʔ luŋ/ (l-fission of 孔).",
        "Documented Shanxi: 圪蛋, 圪梁梁, 夜来, 不赖, 甚.",
    ],
    sig_lens=("Through the Signature lens, idioms are the master seals of a "
              "people: 不赖 seals approval, 入鬼 seals mischief, 熟能生巧 "
              "seals the work ethic. Twenty small stamps, one great "
              "philosophy of Shanxi."),
)

E(
    key="jin_register", name="Jin Chinese Formal and Polite Registers",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen formal-vs-informal pairs for letters, business, and elders -
        each with translations. Greeting an elder: 请问您贵姓 tsʰiŋ2-uən3
        nin2 kui3-xiŋ3 (may I ask your honorable surname?) vs 你姓甚 ni2
        xiŋ3 ʂən2 (what's your surname?). Thanks: 多谢您的帮助 tu1-xie3
        nin2-tiəʔ4 paŋ1-tsu3 (thank you so much for your help) vs 谢谢
        xie3-xie3 (thanks). Request: 麻烦您帮个忙 ma2-fan1 nin2 paŋ1-kə3
        maŋ2 (could I trouble you to help?) vs 帮我一下 paŋ1 ŋəʔ4 iəʔ4-xia3
        (help me out). Hosting: 请慢用 tsʰiŋ2 man3-iəuŋ3 (please enjoy your
        meal) vs 多吃点儿 tu1 tsʰəʔ4-tier2 (eat more). Apology: 实在对不起
        ʂəʔ4-tsai3 tui3-puʔ4-tsʰi3 (I'm truly sorry) vs 对不起
        tui3-puʔ4-tsʰi3 (sorry). Farewell: 一路顺风 iəʔ4-lu3 ʂun3-fəŋ1 (have
        a smooth journey) vs 慢走 man3-tsəu2 (take care going). Meeting: 久仰
        大名 tɕiəu2-iaŋ3 ta3-miŋ2 (honored to know your great name) vs 很高兴
        认识你 xən2 kau1-xiŋ3 zən3-ʂəʔ4 ni2 (nice to meet you). Business
        letter: 敬请指教 tɕiŋ3-tsʰiŋ2 tsɿ2-tɕiau3 (respectfully ask your
        guidance) vs 请多帮忙 tsʰiŋ2 tu1 paŋ1-maŋ2 (please help more).
        Invitation: 敬请光临 tɕiŋ3-tsʰiŋ2 kuaŋ1-lin2 (we respectfully invite
        your presence) vs 有空来玩 iəu2-kʰuŋ3 lai2 uan2 (come visit when free).
        Declining: 实在抽不出时间 ʂəʔ4-tsai3 tsʰəu1-puʔ4-tsʰu1 ʂɿ2-tɕien1 (I
        truly can't find the time) vs 没空 mei2-kʰuŋ3 (no time). Praise:
        您过奖了 nin2 kuə3-tɕiaŋ2-lə (you flatter me) vs 哪里哪里 na2-li2
        na2-li2 (not at all). Toast: 敬您一杯 tɕiŋ3 nin2 iəʔ4-pei1 (a toast
        to you) vs 干杯 kan1-pei1 (cheers). Condolence: 请节哀顺变
        tsʰiŋ2 tɕie1-ai1 ʂun3-pien3 (please take care in grief) vs 别太难过
        pieʔ4 tʰai3 nan2-kuə3 (don't grieve too much). Congratulations: 恭喜
        恭喜 kuŋ1-xi1 kuŋ1-xi1 (congratulations) vs 不赖啊 puʔ4-lai3 a (nice!).
        Fifteen pairs, one ladder of respect."""),
    how_it_works=textwrap.dedent("""\
        This record teaches register as a ladder: the learner takes one
        situation (thanking) and climbs from 谢谢 to 多谢您的帮助, feeling
        the added weight of each step. 您 vs 你 is drilled as the master
        switch - flip it and the whole sentence changes temperature. The
        learner writes a formal invitation and a casual one, then role-plays
        meeting an elder vs meeting a friend. The demo runs a grammar drill
        asserting each formal marker's position."""),
    key_points=[
        "Elder greeting: 请问您贵姓 tsʰiŋ2-uən3 nin2 kui3-xiŋ3 (formal) vs 你姓甚 ni2 xiŋ3 ʂən2 (casual).",
        "Thanks: 多谢您的帮助 tu1-xie3 nin2-tiəʔ4 paŋ1-tsu3 (formal) vs 谢谢 xie3-xie3 (casual).",
        "Request: 麻烦您帮个忙 ma2-fan1 nin2 paŋ1-kə3 maŋ2 (formal) vs 帮我一下 paŋ1 ŋəʔ4 iəʔ4-xia3 (casual).",
        "Hosting: 请慢用 tsʰiŋ2 man3-iəuŋ3 (formal) vs 多吃点儿 tu1 tsʰəʔ4-tier2 (casual).",
        "Apology: 实在对不起 ʂəʔ4-tsai3 tui3-puʔ4-tsʰi3 (formal) vs 对不起 tui3-puʔ4-tsʰi3 (casual).",
        "Farewell: 一路顺风 iəʔ4-lu3 ʂun3-fəŋ1 (formal) vs 慢走 man3-tsəu2 (casual).",
        "Meeting: 久仰大名 tɕiəu2-iaŋ3 ta3-miŋ2 (formal) vs 很高兴认识你 xən2 kau1-xiŋ3 zən3-ʂəʔ4 ni2 (casual).",
        "Business: 敬请指教 tɕiŋ3-tsʰiŋ2 tsɿ2-tɕiau3 (formal) vs 请多帮忙 tsʰiŋ2 tu1 paŋ1-maŋ2 (casual).",
        "Invitation: 敬请光临 tɕiŋ3-tsʰiŋ2 kuaŋ1-lin2 (formal) vs 有空来玩 iəu2-kʰuŋ3 lai2 uan2 (casual).",
        "Declining: 实在抽不出时间 (formal) vs 没空 mei2-kʰuŋ3 (casual).",
        "Praise: 您过奖了 nin2 kuə3-tɕiaŋ2-lə (formal) vs 哪里哪里 na2-li2 na2-li2 (casual).",
        "Toast: 敬您一杯 tɕiŋ3 nin2 iəʔ4-pei1 (formal) vs 干杯 kan1-pei1 (casual).",
        "Condolence: 请节哀顺变 (formal) vs 别太难过 pieʔ4 tʰai3 nan2-kuə3 (casual).",
        "Congrats: 恭喜恭喜 kuŋ1-xi1 kuŋ1-xi1 (formal) vs 不赖啊 puʔ4-lai3 a (casual).",
        "Master switch: 您 vs 你 changes the temperature of the whole sentence.",
    ],
    requirements=[
        "Write one formal and one casual invitation.",
        "Role-play meeting an elder, then a friend.",
    ],
    standards=[
        "Formal frames follow standard Chinese polite conventions in Jin pronunciation.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Qiao Quansheng 乔全生. 晋方言研究的历史、现状与未来. On Jin sociolinguistic research.",
    ],
    sig_lens=("Through the Signature lens, register is respect sealed in syllables: "
              "您 is a bow made of sound, 敬请 a kowtow in four characters. "
              "Jin honors its elders the old way - every formal phrase a "
              "seal of deference."),
)

E(
    key="jin_complex", name="Jin Chinese Compound and Complex Sentences",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen long Jin sentences with clauses, connectors, and relative
        clauses - parsed and translated. Cause: 因为下雨，所以延期了
        in1-uei3 xia3-y1, su2-i2 ien2-tsʰi2-lə (because of rain, it was
        postponed). Concession: 虽然很热，但是他来了 sui1-zan2 xən2 zəʔ4,
        tan3-ʂɿ3 tʰa1 lai2-lə (although it was hot, he came). Condition: 如果
        天好，我们就去 zu2-kuə2 tʰien1 hau2, ŋəʔ4-mən1 tɕiəu3 tsʰɿ3 (if the
        weather is good, we'll go). Not only: 他不但会说晋语，而且会唱歌
        tʰa1 puʔ4-tan3 xui3 ʂuə1 tɕin3-y1, ər2-tsʰie2 xui3 tsʰaŋ3-kə1 (he not
        only speaks Jin but also sings). Relative: 你讲的故事很有意思 ni2
        tɕiaŋ2-tiəʔ4 ku3-ʂɿ3 xən2 iəu2 i3-sɿ1 (the story you told is very
        interesting). Passive: 功课被雨淋湿了 kuŋ1-kʰə3 pei3 y1 lin2-ʂəʔ4-lə
        (the homework got wet in the rain). Time clause: 吃完饭我们就走
        tsʰəʔ4-uan2 fan3 ŋəʔ4-mən1 tɕiəu3 tsəu2 (after eating we'll leave).
        Purpose: 为了学好晋语，我天天练习 uei3-lə xɿəʔ4-hau2 tɕin3-y1, ŋəʔ4
        tʰien1-tʰien1 lien3-xi2 (in order to learn Jin well, I practice daily).
        Comparison: 太原比大同大 tʰai3-yøn2 pi2 ta3-tʰuŋ2 ta3 (Taiyuan is
        bigger than Datong). Choice: 你喝茶还是喝水 ni2 xəʔ4-tsʰa1 xai2-ʂɿ3
        xəʔ4-ʂui2 (tea or water?). Sequence: 先买票，再上车 xien1 mai2
        pʰiau3, tsai3 ʂaŋ3-tsʰə1 (first buy tickets, then board). Contrast: 他
        喜欢面食，我喜欢米饭 tʰa1 xi1-huan1 mien3-ʂəʔ4, ŋəʔ4 xi1-huan1
        mi2-fan3 (he likes wheat food, I like rice). Reason-result: 因为努力，
        所以成功了 in1-uei3 nu2-li3, su2-i2 tsʰəŋ2-kuŋ1-lə (through effort,
        success came). Supposition: 要是早点儿来就好了 iau3-ʂɿ3 tsau2-tier2
        lai1 tɕiəu3 hau2-lə (if only you'd come earlier). Summary: 学了这么久，
        终于会说了 xɿəʔ4-lə tsəʔ4-mə tɕiəu2, tsuŋ1-y2 xui3 ʂuə1-lə (after
        studying so long, I can finally speak). Fifteen engines of thought."""),
    how_it_works=textwrap.dedent("""\
        This record teaches complex sentences as connector frames: each
        connector pair (因为...所以, 虽然...但是, 如果...就, 不但...而且)
        is a mold the learner pours their own content into. The parse shows
        which clause is which and where the connector sits - Jin connectors
        frame the clause they open. The learner takes five simple sentences
        from earlier records and upgrades each with a connector. The demo
        runs a grammar drill asserting each connector's position."""),
    key_points=[
        "Cause: 因为下雨，所以延期了 in1-uei3 xia3-y1, su2-i2 ien2-tsʰi2-lə - because of rain, it was postponed.",
        "Concession: 虽然很热，但是他来了 sui1-zan2 xən2 zəʔ4, tan3-ʂɿ3 tʰa1 lai2-lə - although hot, he came.",
        "Condition: 如果天好，我们就去 zu2-kuə2 tʰien1 hau2, ŋəʔ4-mən1 tɕiəu3 tsʰɿ3 - if the weather is good, we'll go.",
        "Not only: 他不但会说晋语，而且会唱歌 tʰa1 puʔ4-tan3 xui3 ʂuə1 tɕin3-y1, ər2-tsʰie2 xui3 tsʰaŋ3-kə1 - he not only speaks Jin but sings.",
        "Relative: 你讲的故事很有意思 ni2 tɕiaŋ2-tiəʔ4 ku3-ʂɿ3 xən2 iəu2 i3-sɿ1 - the story you told is very interesting.",
        "Passive: 功课被雨淋湿了 kuŋ1-kʰə3 pei3 y1 lin2-ʂəʔ4-lə - the homework got wet in the rain.",
        "Time: 吃完饭我们就走 tsʰəʔ4-uan2 fan3 ŋəʔ4-mən1 tɕiəu3 tsəu2 - after eating we'll leave.",
        "Purpose: 为了学好晋语，我天天练习 uei3-lə xɿəʔ4-hau2 tɕin3-y1, ŋəʔ4 tʰien1-tʰien1 lien3-xi2 - to learn Jin well, I practice daily.",
        "Comparison: 太原比大同大 tʰai3-yøn2 pi2 ta3-tʰuŋ2 ta3 - Taiyuan is bigger than Datong.",
        "Choice: 你喝茶还是喝水 ni2 xəʔ4-tsʰa1 xai2-ʂɿ3 xəʔ4-ʂui2 - tea or water?",
        "Sequence: 先买票，再上车 xien1 mai2 pʰiau3, tsai3 ʂaŋ3-tsʰə1 - first tickets, then board.",
        "Contrast: 他喜欢面食，我喜欢米饭 tʰa1 xi1-huan1 mien3-ʂəʔ4, ŋəʔ4 xi1-huan1 mi2-fan3 - he likes wheat food, I like rice.",
        "Supposition: 要是早点儿来就好了 iau3-ʂɿ3 tsau2-tier2 lai1 tɕiəu3 hau2-lə - if only you'd come earlier.",
        "Result: 学了这么久，终于会说了 xɿəʔ4-lə tsəʔ4-mə tɕiəu2, tsuŋ1-y2 xui3 ʂuə1-lə - after so long studying, I can finally speak.",
        "Connector frames: 因为...所以, 虽然...但是, 如果...就, 不但...而且 - molds to pour content into.",
    ],
    requirements=[
        "Upgrade five simple sentences with connectors.",
        "Parse each sentence: name the clauses and the connector.",
    ],
    standards=[
        "Connector pairs follow standard Sinitic patterns in Jin.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Hou Jingyi 侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education Press; 2002. Jin complex sentences.",
    ],
    sig_lens=("Through the Signature lens, complex sentences are the great "
              "seals of thought: 因为...所以 forges cause into effect, "
              "虽然...但是 holds two truths at once. To build them in Jin is "
              "to think in the old architecture."),
)

E(
    key="jin_conv_market", name="Jin Chinese Conversation: At the Market",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue at a Shanxi market - Jin with
        romanization and English, annotated with usage notes. A: 你好，买点儿
        甚? ni2-hau3, mai2-tier2 ʂən2 (hello, buying something?). B: 买点菜，
        菜新鲜吗? mai2-tier2 tsʰai3, tsʰai3 xin1-xien1 ma (some vegetables -
        are they fresh?). A: 新鲜，夜来刚到的 xin1-xien1, ie3-lai2 kaŋ1
        tau3-tiəʔ4 (fresh, just arrived yesterday). B: 多少钱一斤? tu1-ʂau2
        tsʰien2 iəʔ4-tɕin1 (how much per jin?). A: 三块 san1-kʰuai3 (three
        yuan). B: 太贵了，便宜点儿 tʰai3 kui3-lə, pʰien1-i1-tier2 (too
        expensive, cheaper please). A: 两块五，不能再少了 liaŋ2-kʰuai3-u2,
        puʔ4-nəŋ2 tsai3 ʂau2-lə (two-fifty, can't go lower). B: 成交，称两斤
        tsʰəŋ2-tɕiau1, tsʰəŋ3 liaŋ2-tɕin1 (deal, weigh two jin). A: 好嘞
        hau2-lei (coming right up). B: 再来点鸡蛋 tsai3 lai2-tier2 tɕi1-tan3
        (also some eggs). A: 圪蛋五块一斤 kəʔ4-tan3 u3-kʰuai3 iəʔ4-tɕin1
        (eggs five yuan a jin). B: 来一斤 lai2 iəʔ4-tɕin1 (one jin). A: 一共
        十块 iəʔ4-kuŋ3 səʔ4-kʰuai3 (ten total). B: 给你二十 kei3 ni2 ər3-səʔ4 (here's twenty). A: 找你十块 tsau2 ni2 səʔ4-kʰuai3
        (ten change). B: 谢谢 xie3-xie3 (thanks). A: 慢走，欢迎再来 man3-tsəu2,
        huan1-iŋ1 tsai3-lai1 (take care, come again). Twenty lines, one
        market morning. Notes: 夜来 (yesterday) and 圪蛋 (eggs) mark the
        speaker as Shanxi; 成交 seals the bargain; 慢走 is the kind farewell."""),
    how_it_works=textwrap.dedent("""\
        This record teaches conversation as theater: the learner plays both
        parts, standing for the shopkeeper, sitting for the customer, saying
        all twenty lines aloud. Annotations explain WHY each line works -
        why 夜来 instead of 昨天, why 成交 ends the dance. The learner then
        improvises the same scene with different goods. The demo audits all
        twenty lines and checks anchor words (多少, 成交, 找钱, 慢走) against
        the record text."""),
    key_points=[
        "Opener: 你好，买点儿甚? ni2-hau3, mai2-tier2 ʂən2 - hello, buying something?",
        "Freshness: 菜新鲜吗? tsʰai3 xin1-xien1 ma - are the vegetables fresh? / 夜来刚到的 ie3-lai2 kaŋ1 tau3-tiəʔ4 - just arrived yesterday.",
        "Price: 多少钱一斤? tu1-ʂau2 tsʰien2 iəʔ4-tɕin1 - how much per jin? / 三块 san1-kʰuai3 - three yuan.",
        "Bargain: 太贵了，便宜点儿 tʰai3 kui3-lə, pʰien1-i1-tier2 - too expensive, cheaper please.",
        "Counter: 两块五，不能再少了 liaŋ2-kʰuai3-u2, puʔ4-nəŋ2 tsai3 ʂau2-lə - two-fifty, can't go lower.",
        "Deal: 成交，称两斤 tsʰəŋ2-tɕiau1, tsʰəŋ3 liaŋ2-tɕin1 - deal, weigh two jin.",
        "Add-on: 再来点鸡蛋 tsai3 lai2-tier2 tɕi1-tan3 - also some eggs; 圪蛋五块一斤 kəʔ4-tan3 u3-kʰuai3 iəʔ4-tɕin1 - eggs five yuan a jin.",
        "Pay: 一共十块 iəʔ4-kuŋ3 səʔ4-kʰuai3 - ten total; 给你二十 kei3 ni2 ər3-səʔ4 - here's twenty; 找你十块 tsau2 ni2 səʔ4-kʰuai3 - ten change.",
        "Farewell: 慢走，欢迎再来 man3-tsəu2, huan1-iŋ1 tsai3-lai1 - take care, come again.",
        "Markers: 夜来 and 圪蛋 mark Shanxi speech; 成交 seals the bargain.",
        "Theater method: play both parts, stand for the shopkeeper.",
        "Improvise the same scene with different goods.",
    ],
    requirements=[
        "Perform all twenty lines aloud, both parts.",
        "Improvise the scene with different goods.",
    ],
    standards=[
        "Market dialogue follows documented northern bargaining conventions.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Documented Shanxi market speech: 夜来, 圪蛋, 成交, 慢走.",
    ],
    sig_lens=("Through the Signature lens, the market dialogue is commerce "
              "sealed aloud: every 多少钱 a question, every 成交 a handshake "
              "in sound. Shanxi's merchant soul speaks here - the Jin "
              "bargain is a covenant both sides enjoy signing."),
)

E(
    key="jin_conv_friend", name="Jin Chinese Conversation: Meeting a Friend",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue meeting a friend at the Taiyuan
        train station - Jin with romanization and English, annotated. A:
        你好! 好久不见! ni2-hau3! hau2-tɕiəu2 puʔ4-tɕien3! (hello! long time
        no see!). B: 好久不见! 你怎么样? hau2-tɕiəu2 puʔ4-tɕien3! ni2
        tsən2-mə-iaŋ3? (long time no see! how are you?). A: 不赖，你呢?
        puʔ4-lai3, ni2-nə? (good, and you?). B: 也很好 ie2 xən2-hau2 (also
        good). A: 甚时候到的? ʂən2-sɿ1-həu3 tau3-tiəʔ4? (when did you
        arrive?). B: 刚到，火车晚点了 kaŋ1 tau3, xu1-tsʰə1 uan2-tien2-lə
        (just arrived, the train was late). A: 累了吧? lei3-lə pa? (tired?).
        B: 有点儿 iəu2-tier2 (a little). A: 走，先去吃饭 tsəu2, xien1 tsʰɿ3
        tsʰəʔ4-fan3 (come, let's eat first). B: 好啊，吃甚? hau2-a, tsʰəʔ4
        ʂən2? (good, eat what?). A: 刀削面，怎么样? tau1-xiau1-mien3,
        tsən2-mə-iaŋ3? (knife-cut noodles, how about it?). B: 太好了，我最爱
        吃 tʰai3 hau2-lə, ŋəʔ4 tsui3-ai3 tsʰəʔ4 (great, my favorite). A:
        那家面馆不赖 na3-tɕia1 mien3-kuan2 puʔ4-lai3 (that noodle shop is
        good). B: 走吧 tsəu2-pa (let's go). A: 吃完去看电影 tsʰəʔ4-uan2 tsʰɿ3
        kʰan3 tien3-iŋ2 (after eating let's see a movie). B: 好主意 hau2
        tsu2-i3 (good idea). A: 不见不散 puʔ4-tɕien3 puʔ4-san3 (don't stand
        me up - lit. no see no scatter). B: 不见不散! 再见! puʔ4-tɕien3
        puʔ4-san3! tsai3-tɕien3! (it's a deal! goodbye!). Twenty lines, one
        reunion. Notes: 不赖 as 'I'm good' is pure Shanxi; 不见不散 seals the
        plan like a pinky promise."""),
    how_it_works=textwrap.dedent("""\
        This record teaches friendly conversation as reunion theater: the
        learner plays both friends with different voices, walking the station
        meeting, the noodle invitation, the movie plan. Annotations explain
        the warmth markers - 好久不见, 不赖, 不见不散 - and when each fits.
        The learner then replays the scene with their own real friend's name.
        The demo audits all twenty lines and checks anchor words (你好,
        不见不散, 干杯, 再见) against the record text."""),
    key_points=[
        "Reunion: 你好! 好久不见! ni2-hau3! hau2-tɕiəu2 puʔ4-tɕien3! - hello! long time no see!",
        "How are you: 你怎么样? ni2 tsən2-mə-iaŋ3? / 不赖，你呢? puʔ4-lai3, ni2-nə? - good, and you?",
        "Arrival: 甚时候到的? ʂən2-sɿ1-həu3 tau3-tiəʔ4? - when did you arrive? / 刚到，火车晚点了 kaŋ1 tau3, xu1-tsʰə1 uan2-tien2-lə - just arrived, train was late.",
        "Care: 累了吧? lei3-lə pa? - tired? / 有点儿 iəu2-tier2 - a little.",
        "Invitation: 走，先去吃饭 tsəu2, xien1 tsʰɿ3 tsʰəʔ4-fan3 - come, let's eat first.",
        "Food: 刀削面，怎么样? tau1-xiau1-mien3, tsən2-mə-iaŋ3? - knife-cut noodles, how about it? / 太好了，我最爱吃 tʰai3 hau2-lə, ŋəʔ4 tsui3-ai3 tsʰəʔ4 - great, my favorite.",
        "Plan: 吃完去看电影 tsʰəʔ4-uan2 tsʰɿ3 kʰan3 tien3-iŋ2 - after eating let's see a movie. / 好主意 hau2 tsu2-i3 - good idea.",
        "Promise: 不见不散 puʔ4-tɕien3 puʔ4-san3 - don't stand me up (lit. no see no scatter).",
        "Parting: 再见 tsai3-tɕien3 - goodbye.",
        "不赖 as 'I'm good' is pure Shanxi.",
        "Replay with your own friend's name.",
        "Warmth markers: 好久不见, 不赖, 不见不散.",
    ],
    requirements=[
        "Perform all twenty lines with two different voices.",
        "Replay the scene with a real friend's name.",
    ],
    standards=[
        "Friendly dialogue follows documented Shanxi social conventions.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Qiao Quansheng 乔全生. 晋方言研究的历史、现状与未来. On Jin sociolinguistic research.",
    ],
    sig_lens=("Through the Signature lens, the reunion dialogue is friendship "
              "re-sealed: 好久不见 opens the old envelope, 不见不散 signs the "
              "next meeting before this one ends. In Jin, friends don't just "
              "meet - they re-sign."),
)

E(
    key="jin_conv_problem", name="Jin Chinese Conversation: Solving a Problem",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue solving a problem - a lost wallet at
        the station, solved with a friend's help - Jin with romanization and
        English, annotated. A: 坏了! 我的钱包不见了 xuai3-lə! ŋəʔ4-tiəʔ4
        tsʰien2-pau1 puʔ4-tɕien3-lə! (oh no! my wallet is gone!). B: 别慌，
        甚时候丢的? pieʔ4-xuaŋ1, ʂən2-sɿ1-həu3 tiəu1-tiəʔ4? (don't panic, when
        did you lose it?). A: 可能在火车上 kʰə2-nəŋ2 tsai3 xu1-tsʰə1-ʂaŋ3
        (maybe on the train). B: 里面有甚? li2-mien3 iəu2 ʂən2? (what's
        inside?). A: 身份证，银行卡，还有钱 ʂən1-fən3-tsəŋ3, in2-xaŋ2-kʰa2,
        xai2-iəu2 tsʰien2 (ID card, bank cards, and cash). B: 先挂失银行卡
        xien1 kua3-ʂəʔ4 in2-xaŋ2-kʰa2 (first freeze the bank cards). A: 怎么
        挂失? tsən2-mə kua3-ʂəʔ4? (how?). B: 打银行电话，用我的手机 ta2
        in2-xaŋ2 tien3-hua3, iəuŋ3 ŋəʔ4-tiəʔ4 ʂəu2-tɕi1 (call the bank, use my
        phone). A: 好，我打 hau2, ŋəʔ4 ta2 (okay, I'll call). B: 再去问问
        失物招领 tsai3 tsʰɿ3 uən3-uən3 ʂəʔ4-u3-tsau1-liŋ2 (also ask lost and
        found). A: 在哪里? tsai3 na2-li2? (where?). B: 出站口旁边
        tsʰu1-tsan3-kʰəu2 pʰaŋ2-pien1 (next to the exit). A: 找到了! 有人交
        过去了 tsau2-tau3-lə! iəu2-zən1 tɕiau1-kuə3-tsʰɿ3-lə (found it!
        someone turned it in!). B: 太好了，虚惊一场 tʰai3 hau2-lə, xi1-tɕiŋ1
        iəʔ4-tsʰaŋ2 (great, a false alarm). A: 谢谢你，要不是你... xie3-xie3
        ni2, iau3-puʔ4-ʂɿ3 ni2... (thank you, if not for you...). B: 朋友之间
        别客气 pʰəŋ1-iəu3 tsɿ1-tɕien1 pieʔ4-kʰəʔ4-tsʰi3 (don't be polite between
        friends). A: 我请你吃饭 ŋəʔ4 tsʰiŋ2 ni2 tsʰəʔ4-fan3 (dinner's on me).
        B: 好，不见不散 hau2, puʔ4-tɕien3 puʔ4-san3 (deal, it's a date).
        Twenty lines, one crisis solved. Notes: 别慌 opens every Shanxi
        rescue; 挂失 (freeze cards) is the first practical move; the wallet's
        return shows the Shanxi honesty ethic."""),
    how_it_works=textwrap.dedent("""\
        This record teaches problem-solving as a rescue in order: panic (坏
        了!), calm (别慌), diagnose (甚时候丢的?), act (挂失, 问失物招领),
        resolve (找到了!), thanks (我请你吃饭). The learner practices staying
        calm in Jin - the language of the rescue matters as much as the
        steps. Each practical word (钱包, 挂失, 失物招领) is drilled as
        emergency vocabulary. The demo audits all twenty lines and checks
        anchor words (钱包, 挂失, 朋友, 不要慌) against the record text."""),
    key_points=[
        "Panic: 坏了! 我的钱包不见了 xuai3-lə! ŋəʔ4-tiəʔ4 tsʰien2-pau1 puʔ4-tɕien3-lə! - oh no! my wallet is gone!",
        "Calm: 别慌，甚时候丢的? pieʔ4-xuaŋ1, ʂən2-sɿ1-həu3 tiəu1-tiəʔ4? - don't panic, when did you lose it?",
        "Diagnose: 可能在火车上 kʰə2-nəŋ2 tsai3 xu1-tsʰə1-ʂaŋ3 - maybe on the train; 里面有甚? li2-mien3 iəu2 ʂən2? - what's inside?",
        "Act: 先挂失银行卡 xien1 kua3-ʂəʔ4 in2-xaŋ2-kʰa2 - first freeze the bank cards.",
        "How: 怎么挂失? tsən2-mə kua3-ʂəʔ4? - how? / 打银行电话，用我的手机 ta2 in2-xaŋ2 tien3-hua3, iəuŋ3 ŋəʔ4-tiəʔ4 ʂəu2-tɕi1 - call the bank, use my phone.",
        "Lost and found: 再去问问失物招领 tsai3 tsʰɿ3 uən3-uən3 ʂəʔ4-u3-tsau1-liŋ2 - also ask lost and found; 出站口旁边 tsʰu1-tsan3-kʰəu2 pʰaŋ2-pien1 - next to the exit.",
        "Resolve: 找到了! 有人交过去了 tsau2-tau3-lə! iəu2-zən1 tɕiau1-kuə3-tsʰɿ3-lə - found it! someone turned it in!",
        "Relief: 太好了，虚惊一场 tʰai3 hau2-lə, xi1-tɕiŋ1 iəʔ4-tsʰaŋ2 - great, a false alarm.",
        "Thanks: 谢谢你，要不是你... xie3-xie3 ni2, iau3-puʔ4-ʂɿ3 ni2... - thank you, if not for you...",
        "Friendship: 朋友之间别客气 pʰəŋ1-iəu3 tsɿ1-tɕien1 pieʔ4-kʰəʔ4-tsʰi3 - don't be polite between friends.",
        "Reward: 我请你吃饭 ŋəʔ4 tsʰiŋ2 ni2 tsʰəʔ4-fan3 - dinner's on me; 好，不见不散 hau2, puʔ4-tɕien3 puʔ4-san3 - deal, it's a date.",
        "Rescue order: panic, calm, diagnose, act, resolve, thanks.",
        "Emergency vocabulary: 钱包, 挂失, 失物招领.",
    ],
    requirements=[
        "Perform the rescue in order, staying calm in Jin.",
        "Memorize the emergency vocabulary cold.",
    ],
    standards=[
        "Problem-solving dialogue follows realistic service conventions.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Qiao Quansheng 乔全生. 晋方言研究的历史、现状与未来. On Jin sociolinguistic research.",
    ],
    sig_lens=("Through the Signature lens, the rescue dialogue is the covenant "
              "in action: 别慌 is the first seal of help, 有人交过去了 the "
              "proof that Shanxi honesty holds. To solve a problem in Jin is "
              "to prove the contract works when it matters."),
)

E(
    key="jin_mastery", name="Jin Chinese Mastery Review and Full Reference",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        The whole database in one teaching summary: the tone table, 200 core
        words, key grammar, and all phrase tables.
        TONE TABLE (Taiyuan, citation tones per syllable):
        T1 11 level (yinping; yangping merged): 三 san1, 天 tʰien1, 书 ʂu1, 高 kau1, 来 lai1, 茶 tsʰa1.
        T2 53 falling (shangsheng): 好 hau2, 水 ʂui2, 买 mai2, 请 tsʰiŋ2, 甚 ʂən2.
        T3 45 rising (qusheng): 大 ta3, 去 tsʰɿ3, 饭 fan3, 贵 kui3, 晋 tɕin3.
        T4 entering (short, final ʔ): 一 iəʔ4, 吃 tsʰəʔ4, 喝 xəʔ4, 十 səʔ4, 我 ŋəʔ4, 不 puʔ4, 月 yøʔ4.
        Note: some analyses split T4 into yinru 2 and yangru 54; recent
        phonetic work (ISCA 2024) gives 31, 52, 35, 41ʔ, 31ʔ. Sandhi is
        grammar-dependent: adjective-noun and verb-object compounds change
        tones differently.
        200 CORE WORDS (word, romanization, English):
        People: 我 ŋəʔ4 I, 你 niə2 you, 他 tʰa1 he/she, 您 nin2 polite you,
        我们 ŋəʔ4-mən1 we, 你们 niə2-mən1 you (pl), 他们 tʰa1-mən1 they,
        朋友 pʰəŋ1-iəu3 friend, 爸爸 pa4-pa father, 妈妈 ma1-ma mother,
        娃娃 ua3-ua3 child, 哥哥 kə1-kə elder brother, 姐姐 tɕie2-tɕie elder
        sister, 弟弟 ti3-ti younger brother, 妹妹 mei3-mei younger sister,
        老师 lau2-ʂɿ1 teacher, 学生 xɿəʔ4-ʂəŋ1 student, 医生 i1-ʂəŋ1 doctor,
        老板 lau2-pan2 boss, 大家 ta3-tɕia1 everyone.
        Verbs: 吃 tsʰəʔ4 eat, 喝 xəʔ4 drink, 去 tsʰɿ3 go, 来 lai1 come,
        看 kʰan3 look/read, 听 tʰiŋ1 listen, 说 ʂuə1 speak, 问 uən3 ask,
        买 mai2 buy, 卖 mai3 sell, 做 tsu3 do/make, 拿 na1 take,
        给 kei3 give, 喜欢 xi1-huan1 like, 知道 tsɿ1-tau3 know, 想 xiaŋ2 want,
        学 xɿəʔ4 learn, 教 tɕiau1 teach, 工作 kuŋ1-tsuəʔ4 work, 学习 xɿəʔ4-xi2
        study, 睡 ʂui3 sleep, 起 tsʰi2 rise, 走 tsəu2 walk, 跑 pʰau2 run,
        坐 tsu3 sit, 笑 xiau3 laugh, 哭 kʰu1 cry, 开 kʰai1 open, 关 kuan1 close.
        Things: 书 ʂu1 book, 钱 tsʰien1 money, 饭 fan3 rice/meal, 水 ʂui2 water,
        茶 tsʰa1 tea, 东西 tuŋ1-xi1 thing, 地方 ti3-faŋ1 place, 时间 ʂɿ2-tɕien1
        time, 天气 tʰien1-tsʰi3 weather, 电话 tien3-hua3 telephone, 门 mən2 door,
        路 lu3 road, 房子 faŋ1-tsɿ house, 房间 faŋ2-tɕien1 room, 学校
        xɿəʔ4-xiau3 school, 商店 ʂaŋ1-tien3 shop, 市场 ʂɿ3-tsʰaŋ2 market,
        医院 i1-yøn3 hospital, 车站 tsʰə1-tsan3 station, 桌子 tsuəʔ4-tsɿ table,
        椅子 i2-tsɿ chair, 窗户 tsʰuaŋ1-xu3 window, 照片 tsau3-pʰien3 photo.
        Food: 菜 tsʰai3 vegetable/dish, 肉 zəuʔ4 meat, 鱼 y2 fish, 面 mien3
        noodles, 米 mi2 rice, 圪蛋 kəʔ4-tan3 egg, 糖 tʰaŋ2 sugar, 盐 ien2 salt,
        油 iəu2 oil, 酒 tɕiəu2 wine, 醋 tsʰu3 vinegar, 饭店 fan3-tien3
        restaurant, 刀削面 tau1-xiau1-mien3 knife-cut noodles, 老陈醋
        lau2-tsʰən2-tsʰu3 aged vinegar, 水果 ʂui2-kuə2 fruit, 苹果 pʰiŋ2-kuə2
        apple.
        Body: 头 tʰəu2 head, 眼睛 ien2-tɕiŋ1 eyes, 耳朵 ər2-tu1 ears, 鼻子
        pi2-tsɿ nose, 嘴 tsui2 mouth, 手 ʂəu2 hand, 脚 tɕiau2 foot, 肚子 tu3-tsɿ
        belly, 心 xin1 heart, 身体 ʂən1-tʰi2 body/health, 药 iau3 medicine.
        Adjectives: 好 hau3 good, 大 ta3 big, 小 siau2 small, 长 tsʰaŋ2 long,
        短 tuan2 short, 高 kau1 tall, 新 xin1 new, 老 lau2 old, 快 kʰuai3 fast,
        慢 man3 slow, 多 tu1 many, 少 ʂau2 few, 热 zəʔ4 hot, 冷 ləŋ2 cold,
        红 xuŋ2 red, 白 pəʔ4 white, 黑 xəʔ4 black, 远 yøn2 far, 近 tɕin3 near,
        贵 kui3 expensive, 便宜 pʰien1-i1 cheap, 不赖 puʔ4-lai3 not bad,
        漂亮 pʰiau3-liaŋ1 pretty, 干净 kan1-tɕiŋ3 clean, 难 nan2 difficult,
        香 xiaŋ1 fragrant.
        Adverbs and particles: 很 xən2 very, 太 tʰai3 too, 真 tsən1 really,
        最 tsui3 most, 都 tu1 all, 也 ie2 also, 就 tɕiəu3 then, 才 tsʰai2 only
        then, 还 xai2 still, 已经 i2-tɕiŋ1 already, 常常 tsʰaŋ2-tsʰaŋ2 often,
        一起 iəʔ4-tsʰi2 together, 慢慢 man3-man3 slowly, 不 puʔ4 not,
        没 mei2 not (past), 吗 ma question, 吧 pa suggestion, 呢 nə follow-up,
        的 tiəʔ4 possessive, 了 lə completed, 过 kuə3 experienced, 着 tsə
        durative, 在 tsai3 at/ongoing, 把 pa2 disposal, 被 pei3 passive.
        Numbers and time: 一 iəʔ4 one, 二 ər3 two, 三 san1 three, 四 sɿ3 four,
        五 u3 five, 六 liəuʔ4 six, 七 tsʰiəʔ4 seven, 八 paʔ4 eight,
        九 tɕiəu3 nine, 十 səʔ4 ten, 百 paʔ4 hundred, 千 tsʰien1 thousand,
        万 uan3 ten thousand, 今天 tɕin1-tʰien1 today, 夜来 ie3-lai2 yesterday,
        明天 miŋ2-tʰien1 tomorrow, 现在 xien3-tsai3 now, 点 tien2 o'clock,
        半 pan3 half, 星期 xiŋ1-tsʰi1 week, 年 nien2 year, 月 yøʔ4 month,
        天 tʰien1 day, 春天 tsʰun1-tʰien1 spring, 冬天 tuŋ1-tʰien1 winter.
        Nature: 狗 kəu2 dog, 猫 mau1 cat, 鸟 niau2 bird, 花 xua1 flower,
        树 ʂu3 tree, 山 ʂan1 mountain, 河 xə2 river, 黄河 xuaŋ2-xə2 Yellow
        River, 汾河 fən2-xə2 Fen River, 雨 y1 rain, 雪 xɿəʔ4 snow, 风 fəŋ1 wind,
        太阳 tʰai3-iaŋ2 sun, 月亮 yøʔ4-liaŋ3 moon.
        Social: 你好 niə2-hau3 hello, 谢谢 xie3-xie3 thank you, 再见
        tsai3-tɕien3 goodbye, 对不起 tui3-puʔ4-tsʰi3 sorry, 请 tsʰiŋ2 please,
        请问 tsʰiŋ2-uən3 may-I-ask, 甚 ʂən2 what, 甚人 ʂən2-zən1 who,
        欢迎 huan1-iŋ1 welcome, 恭喜 kuŋ1-xi1 congratulations, 干杯 kan1-pei1
        cheers, 慢走 man3-tsəu2 take care, 加油 tɕia1-iəu2 you can do it.
        KEY GRAMMAR: SVO order; no inflections; 们 plural; 的 possessive;
        不/没 negation; 吗/吧/呢 questions; 了/过/着/在 aspects; 要/会 future;
        把 disposal; 被 passive; 在 locative; prefixes 圪/忽/入; l-fission
        (蹦→/pəʔ4-ləŋ1/); three-way demonstratives in some dialects.
        PHRASE TABLES: greetings (你好, 吃了没, 谢谢, 再见, 慢走); market
        (多少钱, 便宜点儿, 成交); travel (怎么走, 买票, 酒店); health (头疼,
        看医生, 吃药); 15 formal/informal pairs; 20 idioms; 3 conversations;
        3 stories. 熟能生巧 - practice makes perfect: the whole ladder in one
        page."""),
    how_it_works=textwrap.dedent("""\
        This record is the final examination and the permanent reference. The
        learner reads the tone table aloud, then works through the 200 words
        as flashcards, then recites the key grammar from memory, then uses
        the phrase tables as a phrasebook. The demo program runs a 200-word
        mastery exam with a perfect-score assertion and re-verifies the tone
        table means. Keep this record open beside you whenever you speak Jin
        - it is the whole database distilled."""),
    key_points=[
        "Tone table: T1 11 level (yinping, yangping merged), T2 53 falling, T3 45 rising, T4 entering ʔ (short).",
        "晋语 tɕin3-y1: the native name; 你好 niə2-hau3 hello; 谢谢 xie3-xie3 thank you; 再见 tsai3-tɕien3 goodbye.",
        "熟能生巧 ʂəu2-nəŋ2-ʂəŋ1-tsʰiau2 - practice makes perfect: the motto of this ladder.",
        "200 core words: people, verbs, things, food, body, adjectives, adverbs/particles, numbers/time, nature, social - all above.",
        "Key grammar: SVO; 们; 的; 不/没; 吗/吧/呢; 了/过/着/在; 要/会; 把; 被; 圪/忽/入 prefixes; l-fission.",
        "Jin signatures: entering tone ʔ, 甚, 夜来, 不赖, 圪蛋, 入鬼, 窟窿.",
        "Phrase tables: greetings, market, travel, health, registers, idioms, conversations, stories.",
        "Exam method: tone table aloud, 200 flashcards, grammar from memory.",
        "Keep this record as your permanent Jin phrasebook.",
    ],
    requirements=[
        "Score 200/200 on the demo mastery exam.",
        "Recite the tone table and key grammar from memory.",
    ],
    standards=[
        "Reference values follow the classical Taiyuan description with ISCA 2024 noted.",
        "All readings use the database's Taiyuan teaching romanization with tone numbers 1-4.",
    ],
    citations=[
        "Li Rong 李荣 (1985); Language Atlas of China (1987; 2nd ed. 2012); Norman (1988); Hou & Shen (2002); Yan (2006); Kurpaska (2010); Ethnologue [cjy]; ISCA Speech Prosody 2024.",
    ],
    sig_lens=("Through the Signature lens, the mastery page is the great seal "
              "of the whole ladder: 200 words, five tones, one covenant. "
              "熟能生巧 - the learner who climbs all 34 rungs has signed "
              "their name beside sixty-three million others, in the old "
              "tones of Shanxi."),
)

SIG_TAIL = ("Signature editions are his original Signature language work - "
            "clearly labeled Signature-made, never presented as authentic "
            "public record.")
