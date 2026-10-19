#!/usr/bin/env python3
"""Entries for the Min Nan Chinese Language databases (34 ladder-ordered records).

Public records: real, fact-checked Min Nan (Southern Min / Hokkien;
Taiwanese / Tai-gi as the reference variety) language teaching - every
record carries Chinese characters with POJ-style romanization and English
translation plus example sentences, organized in the Signature system.

Romanization used throughout: POJ-style (Pehoeji/Tai-lo compatible) with
tone NUMBERS. The eight citation tones of the Quanzhang/Taiwanese standard:
  1 = 55 (yinping 阴平)   2 = 24 (yangping 阳平)   3 = 51 (yinshang 阴上)
  4 = 33 (yangshang 阳上) 5 = 21 (yinqu 阴去)      6 = 22 (yangqu 阳去)
  7 = 32 short (yinru 阴入) 8 = 4 short (yangru 阳入)
Tone numbers are given per syllable; connected speech applies the Min Nan
tone-sandhi chain (record 3). Quanzhou/Xiamen merge yangshang into yangqu
(7-tone system); Zhangzhou keeps all eight - the eight-tone set below is
the full descriptive system.
"""
import textwrap

ENTRIES = []


def E(**kw):
    ENTRIES.append(kw)
    return kw


E(
    key="nan_overview", name="Min Nan Chinese Language Overview",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Min Nan (闽南语, ban5-lam5-gi2) is a major branch of the Sinitic family
        within Sino-Tibetan, spoken natively by roughly 48 to 50 million
        people - and understood by tens of millions more across the Chinese
        diaspora. Its homeland is the southern coast of Fujian province:
        Xiamen (Amoy), Quanzhou, and Zhangzhou - the three city-regions whose
        speech gives Min Nan its other great name, Hokkien (福建话, hok4-kian3-ue7,
        "Fujian speech"). From Fujian it spread to Taiwan, where Taiwanese
        (Tai-gi, 台语) is spoken by most of the island's population and is a
        statutory national language; to eastern Guangdong (Chaoshan, whose
        Teochew / Chaozhou speech is a Min Nan variety); to Hainan (Hainanese);
        and to Southeast Asia - the Philippines, Malaysia, Singapore, and
        Indonesia - where Hokkien is the language of commerce and clan. Min
        Nan is not an official language in mainland China; Mandarin
        (Putonghua) holds that place. ISO 639-3 gives Min Nan the code nan
        (there is no ISO 639-1 code). The family path is Sino-Tibetan >
        Sinitic > Min > Min Nan. Its great divisions are Hokkien/Quanzhang
        (Xiamen, Quanzhou, Zhangzhou, Taiwan), Teochew/Chaoshan, Hainanese,
        and Leizhou. The Taiwanese variety (Tai-gi, 台语) is the reference
        standard of this database. Min Nan is famous among linguists for
        preserving the full set of Middle Chinese tones - eight of them -
        and for the most famous tone sandhi system in all of Chinese: almost
        every non-final syllable changes tone in connected speech. This
        record is the map of the whole database: what Min Nan is, where it
        lives, and how the ladder below carries a learner from a first 你好
        (li2-ho2, hello) to full conversation."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the overview by anchoring every fact in a
        sentence the learner can say. Each fact - the native name 闽南语, the
        ISO code nan, the Sino-Tibetan family path, the 48-million-plus
        speakers, the Xiamen-Quanzhou-Zhangzhou heartland, the Hokkien /
        Taiwanese / Teochew / Hainanese divisions - appears with a plain
        English explanation and a Min Nan example sentence in characters,
        romanization, and English. The learner reads the facts, then repeats
        the sentences, so the overview becomes spoken language from the
        first record. Later records climb the teaching ladder: foundations
        (records 1-10: writing, sounds, words, grammar basics), compounded
        (records 11-20: themed sentence sets), advanced (records 21-34:
        tenses, questions, stories, idioms, registers, complex sentences,
        conversations, and a full mastery reference)."""),
    key_points=[
        "Native name: 闽南语 (ban5-lam5-gi2); English names: Min Nan, Southern Min, Hokkien; ISO 639-3: nan; no ISO 639-1 code.",
        "Family: Sino-Tibetan > Sinitic > Min > Min Nan; about 48-50 million native speakers.",
        "Homeland: southern Fujian - Xiamen (Amoy), Quanzhou, Zhangzhou (the Quanzhang / Hokkien heartland).",
        "Taiwanese (Tai-gi, 台语) is spoken by most of Taiwan's people and is a statutory national language of Taiwan.",
        "Major divisions: Hokkien/Quanzhang, Teochew/Chaoshan, Hainanese, Leizhou.",
        "Southeast Asian diaspora: the Philippines, Malaysia, Singapore, Indonesia - Hokkien is the language of commerce and clan.",
        "Not official in mainland China; Mandarin is the official language there.",
        "Reference standard of this database: the Taiwanese variety (Tai-gi, 台语).",
        "Signature trait: Min Nan keeps all eight Middle Chinese tones - the richest tone system in Chinese.",
        "Every record in this database carries Chinese characters, POJ-style romanization with tone numbers, and English on every line.",
    ],
    requirements=[
        "No prior knowledge of Min Nan is needed; this is the starting record of the ladder.",
        "Learners should read each example sentence aloud to begin training Min Nan tones from day one.",
    ],
    standards=[
        "ISO 639-3:2007 (nan) language code for Min Nan Chinese.",
        "Ethnologue: Min Nan Chinese [nan] - Sino-Tibetan, Sinitic, Min, Southern Min.",
    ],
    citations=[
        "Norman J. Chinese. Cambridge University Press; 1988. Chapter on the Min dialects: classification, tone systems, the Min Nan division.",
        "Bodman N C. Spoken Amoy Hokkien. Government Language School; 1955-1958. The classic two-volume grammar of Xiamen speech.",
        "Eberhard D M, Simons G F, Fennig C D, editors. Ethnologue: Languages of the World. SIL International; 2024. Entry: Min Nan Chinese [nan], ~48.7 million speakers.",
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. The standard dictionary of Taiwanese (Tai-gi).",
    ],
    sig_lens=("Through the Signature lens, a language is not a school subject - it is a "
              "living covenant between a people and their sea, and Min Nan is one of the "
              "greatest signed covenants of the China coast: fifty million voices "
              "carrying one oath of meaning from Xiamen harbor to Taipei, Manila, and "
              "Singapore. This Signature reading treats the overview as the first seal "
              "of that covenant."),
)

E(
    key="nan_writing", name="Min Nan Chinese Writing System",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Min Nan is written with Chinese characters - the same script as
        Mandarin, written left to right in modern texts. There is no separate
        Min Nan alphabet: the writing system IS the character system, and
        Min Nan has its own beloved vernacular characters for words Mandarin
        writes differently or not at all. Learn these and Min Nan texts open
        up: 我 (gua2, I), 汝 (li2, you), 伊 (i1, he/she; also that), 阮
        (gun2, we excluding you), 咱 (lan2, we including you), 恁 (lin2, you
        plural), 怹 (in1, they), 媠 (sui2, pretty), 歹 (phainn2, bad), 毋
        (m7, not - the great negator), 无 (bo5, have not), 食 (tsiah8, to
        eat), 饮 (lim1, to drink), 睏 (khun3, to sleep), 厝 (tshu3, house),
        囝仔 (gin2-a2, child), 查埔 (tsa1-poo1, man), 查某 (tsa1-boo2,
        woman), 逐 (tak8, each/every), 搁 (koh4, again). Numerals are the
        standard characters with Min Nan readings: 一 (tsit8), 二 (ji7), 三
        (sann1), 四 (si3), 五 (goo7), 六 (lak8), 七 (tshit4), 八 (peh4), 九
        (kau2), 十 (tsap8), 百 (pah4), 千 (tshing1), 万 (ban7). Punctuation
        follows modern Chinese practice: 。 for the period, ， for the
        comma, ？ for questions, ！ for exclamations, 、 for list pauses,
        《》 for book titles. Digits 0-9 are used for Arabic numerals exactly
        as in Mandarin. For romanization, Min Nan has two standard systems:
        Peh-oe-ji (POJ, 白话字, 1830s missionary romanization) and Tai-lo
        (台罗, the Taiwan Ministry of Education system, near-identical to
        POJ). This database uses POJ-style spelling with tone NUMBERS
        (gua2, li2-ho2, lang5) so tones are machine-readable; the diacritic
        equivalents are: 1 = no mark (a), 2 = acute (a), 3 = grave (a),
        4 = circumflex (a), 5 = macron (a), 7 = vertical line above (a),
        8 = dot above (a). Because Min Nan shares the character script with
        Mandarin, a reader of Chinese can sound out Min Nan texts immediately
        - the characters are familiar, only the readings and the vernacular
        words are new."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the writing system by pairing every Min Nan
        vernacular character with its tone-numbered romanization, its
        Mandarin equivalent where one exists, and an English gloss - then a
        sentence showing the character alive in real speech. The learner
        studies the two romanization standards (POJ and Tai-lo), converts a
        tone-diacritic word into tone-number form and back, and reads the
        numeral table aloud. Because sentences require the script, the
        writing system is drilled as spoken lines, never as dead symbols."""),
    key_points=[
        "Script: Chinese characters, left to right; no separate Min Nan alphabet exists.",
        "Vernacular characters: 我 gua2 (I), 汝 li2 (you), 伊 i1 (he/she), 阮 gun2 (we-excl), 咱 lan2 (we-incl), 怹 in1 (they).",
        "The great negators: 毋 m7 (not) and 无 bo5 (have not) - written differently from Mandarin.",
        "Vernacular verbs: 食 tsiah8 (eat), 饮 lim1 (drink), 睏 khun3 (sleep) - not the Mandarin characters.",
        "Vernacular nouns: 厝 tshu3 (house), 囝仔 gin2-a2 (child), 查埔 tsa1-poo1 (man), 查某 tsa1-boo2 (woman).",
        "Numerals: 一 tsit8, 二 ji7, 三 sann1, 四 si3, 五 goo7, 六 lak8, 七 tshit4, 八 peh4, 九 kau2, 十 tsap8.",
        "Romanization: Peh-oe-ji (POJ) and Tai-lo; this database uses POJ-style spelling with tone numbers 1-8.",
        "Tone-diacritic equivalents: 2 = acute, 3 = grave, 4 = circumflex, 5 = macron, 7 = vertical above, 8 = dot above.",
        "Punctuation: 。 ， ？ ！ 、 《》 - modern Chinese practice; Arabic digits 0-9 as in Mandarin.",
        "Sentence drill: 我食饱矣 (gua2 tsiah8-pa2 ah4, I have eaten) shows characters, romanization, and English in one line.",
    ],
    requirements=[
        "Learners should write each vernacular character while saying its romanization aloud.",
        "Learners should convert five diacritic-marked words into tone-number form and back.",
    ],
    standards=[
        "Taiwan Ministry of Education 台罗拼音 (Tai-lo) romanization scheme.",
        "Peh-oe-ji (POJ) 白话字, the 1830s missionary romanization still used in dictionaries.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. Taipei; standard character choices for Taiwanese.",
        "Douglas C. Chinese-English Dictionary of the Vernacular or Spoken Language of Amoy. 1873; the classic Amoy dictionary and POJ source.",
        "Maryknoll Language Service Center. English-Amoy Dictionary; 1976. POJ romanization of Xiamen speech.",
    ],
    sig_lens=("Through the Signature lens, the writing system is the sealed "
              "vessel of the covenant: every vernacular character a stamp "
              "pressed by millions of hands across four centuries - 汝 for "
              "you, 毋 for not, 食 for eat - each one a signature no other "
              "Chinese tongue can counterfeit. This Signature reading seals "
              "the characters themselves."),
)

E(
    key="nan_phonology", name="Min Nan Chinese Pronunciation and Phonology",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Min Nan's sound system is the most conservative in Chinese - and the
        most musical. The initial consonants (with English approximations):
        p (unaspirated, like sPy), ph (aspirated p), b (voiced b, kept from
        old Chinese - as in 肉 bah4), m (m), t (sTay), th (aspirated t), d
        (voiced d, as in 毒 tok8), n (n), l (l), k (sKy), kh (aspirated
        k), g (voiced g, as in 语 gi2), ng (ng as in siNG), h (h), ts
        (caTS), tsh (aspirated ch), s (s), j (like dz, as in 日 jit8). The
        main vowels: a, e (eh), i (ee), o (aw), oo (like aw but rounder, as
        in 好 ho2), u (oo). Key diphthongs: ai, au, ia, iu, io, ua, ue, ui.
        Nasal vowels carry the superscript n in POJ (e.g., 人 lang5 is
        pronounced with a nasalized vowel). Min Nan has EIGHT citation
        tones - the full Middle Chinese set, which Mandarin reduced to
        four: T1 55 high level (yinping: 天 thinn1 sky, 三 sann1 three),
        T2 24 rising (yangping: 牛 gu5 ox, 来 lai5 come), T3 51 falling
        (yinshang: 去 khi3 go, 看 khuann3 see), T4 33 mid level (yangshang:
        马 be2 horse, 短 te2 short), T5 21 low falling (yinqu: 人 lang5
        person, 茶 te5 tea), T6 22 low level (yangqu: 大 tua7 big, 电
        tian7 electricity), T7 32 short checked (yinru: 一 tsit8 one, 食
        tsiah8 eat), T8 4 short checked (yangru: 日 jit8 sun/day, 月
        gueh8 moon). Two syllables never stay at citation tone in connected
        speech: the famous Min Nan tone sandhi. The chain: T1 becomes 7, T7
        becomes 3, T3 becomes 2, T2 becomes 1, T5 becomes 7 (Quanzhou/Xiamen;
        Zhangzhou uses 3), T4 becomes 2, T8 becomes 4 - while the FINAL
        syllable of a phrase keeps its citation tone. So 台北 Tai5-pak4 is
        spoken tai7-pak4: only the last syllable (pak4) stays. Stress is
        light and even; Min Nan is syllable-timed, and the sandhi melody is
        what makes it sound like singing. The neutral tone (轻声) exists for
        particles like 仔 a2, 诶 e5, 矣 ah4."""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronunciation by the drill-and-sandhi method.
        First the learner reads the eight-tone table aloud with the example
        words until each contour (55, 24, 51, 33, 21, 22, 32-short, 4-short)
        is distinct. Then the sandhi chain is practiced as a ring: 1-7-3-2-1
        and 5-7, 4-2, 8-4, always leaving the final syllable unchanged. Ten
        spoken example words are drilled in isolation and then in
        two-syllable phrases so the sandhi change is heard and felt. Because
        every later record's sentences depend on tones, this record is the
        engine room of the whole database."""),
    key_points=[
        "Eight citation tones - the full Middle Chinese set: T1 55, T2 24, T3 51, T4 33, T5 21, T6 22, T7 32 short, T8 4 short.",
        "T1 examples: 天 thinn1 (sky), 三 sann1 (three); T2: 牛 gu5 (ox), 来 lai5 (come).",
        "T3 examples: 去 khi3 (go), 看 khuann3 (see); T4: 马 be2 (horse), 短 te2 (short).",
        "T5 examples: 人 lang5 (person), 茶 te5 (tea); T6: 大 tua7 (big), 电 tian7 (electricity).",
        "T7 examples: 一 tsit8 (one), 食 tsiah8 (eat); T8: 日 jit8 (sun/day), 月 gueh8 (moon).",
        "Sandhi chain: 1 becomes 7, 7 becomes 3, 3 becomes 2, 2 becomes 1, 5 becomes 7, 4 becomes 2, 8 becomes 4.",
        "The FINAL syllable of a phrase keeps its citation tone: 台北 tai5-pak4 is spoken tai7-pak4.",
        "Voiced initials b, d, g, j are kept from old Chinese - Mandarin lost them.",
        "Nasal vowels (lang5 人) and the neutral tone for particles (仔 a2, 诶 e5, 矣 ah4).",
        "Syllable-timed rhythm; light even stress - the sandhi melody is the music of Min Nan.",
    ],
    requirements=[
        "Learners should chant the eight tones with the example words until each contour is distinct.",
        "Learners should practice the sandhi ring on two-syllable phrases, always keeping the final syllable at citation tone.",
    ],
    standards=[
        "Taiwan Ministry of Education Tai-lo tone numbering 1-8 for Taiwanese.",
        "Bodman 1955-1958: the standard description of Amoy (Xiamen) tones and sandhi.",
    ],
    citations=[
        "Bodman N C. Spoken Amoy Hokkien. Government Language School; 1955-1958. Tones and the sandhi circle.",
        "Yuan Jiahua 袁家骅 et al. 汉语方言概要. Language Reform Press; 1960. The Min Nan tone chapter.",
        "Taiwan Ministry of Education. 台湾闽南语罗马字拼音方案. The official Tai-lo scheme with tone numbers.",
    ],
    sig_lens=("Through the Signature lens, the eight tones are eight seals "
              "of breath, and the sandhi chain is the covenant's handshake: "
              "every non-final syllable bends its tone in loyalty to the "
              "phrase, and the final syllable stands straight, keeping its "
              "citation like a signature kept unbroken. This Signature "
              "reading seals the music of Min Nan."),
)

E(
    key="nan_nouns", name="Min Nan Chinese Core Nouns I",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        The twenty-five essential nouns of Min Nan - people, places, and
        things - each with its characters, tone-numbered romanization,
        English gloss, and a full spoken sentence. Min Nan nouns take no
        gender, no case, and no plural ending; number is shown with numerals
        and the classifiers of record 10. Learn these twenty-five and the
        world starts answering back: 人 lang5 (person): 伊是一个好人 (i1 si7
        tsit8-e5 ho2-lang5, he is a good person). 囝仔 gin2-a2 (child): 囝仔
        咧外口耍 (gin2-a2 teh4 gua7-khau2 sng2, the child is playing
        outside). 查埔 tsa1-poo1 (man), 查某 tsa1-boo2 (woman): 查埔查某拢
        有来 (tsa1-poo1 tsa1-boo2 long2 u7 lai5, men and women both came).
        朋友 ping5-iu2 (friend): 伊是我的朋友 (i1 si7 gua2-e5 ping5-iu2, he
        is my friend). 老父 lau7-pe7 (father), 老母 lau7-bu2 (mother): 老父
        老母身体真好 (lau7-pe7 lau7-bu2 sin1-the2 tsin1 ho2, father and
        mother are in very good health). 厝 tshu3 (house): 这是我的厝
        (tse2 si7 gua2-e5 tshu3, this is my house). 门 mng5 (door): 门关起来
        (mng5 kuainn1 khi2-lai5, close the door). 路 loo7 (road): 这条路真
        长 (tsit4-tiau5 loo7 tsin1 tng5, this road is very long). 车 tshia1
        (car): 伊买一台新车 (i1 be2 tsit8-tai5 sin1-tshia1, he bought a new
        car). 学校 hak8-hau7 (school): 囝仔去学校读书 (gin2-a2 khi3
        hak8-hau7 thak8-tsu1, the child goes to school to study). 市场
        tshi7-tiunn5 (market): 阿母去市场买菜 (a1-bu2 khi3 tshi7-tiunn5 be2
        tshai3, mother went to the market to buy vegetables). 医生
        i1-sing1 (doctor): 医生讲无要紧 (i1-sing1 kong2 bo5 iau3-kin2, the
        doctor says it is nothing serious). 钱 tsinn5 (money): 我无钱
        (gua2 bo5 tsinn5, I have no money). 饭 png7 (rice, meal): 食饭矣
        未 (tsiah8-png7 ah4 bue7, have you eaten yet). 水 tsui2 (water):
        我欲饮水 (gua2 beh4 lim1-tsui2, I want to drink water). 茶 te5
        (tea): 请饮茶 (tshiann2 lim1-te5, please have some tea). 鱼 hi5
        (fish), 肉 bah4 (meat): 今仔日食鱼，明仔载食肉 (kin1-a2-jit8
        tsiah8-hi5, bin5-a2-tsai3 tsiah8-bah4, today eat fish, tomorrow eat
        meat). 天 thinn1 (sky/day), 地 te7 (earth/ground): 天顶有云，地跤
        有水 (thinn1-ting2 u7 hun5, te7-kha1 u7 tsui2, there are clouds in
        the sky, water on the ground). 山 suann1 (mountain), 海 hai2
        (sea): 山真高，海真深 (suann1 tsin1 kuan5, hai2 tsin1 tshim1, the
        mountain is very high, the sea is very deep). 日 jit8 (sun/day),
        月 gueh8 (moon): 日出东方，月落西山 (jit8 tshut4 tong1-hong1,
        gueh8 loh8 se1-suann1, the sun rises in the east, the moon sets in
        the west). 书 tsu1 (book): 这本书真好看 (tsit4-pun2 tsu1 tsin1
        ho2-khuann3, this book is very good). 话 ue7 (speech): 伊讲的话我
        听无 (i1 kong2-e5 ue7 gua2 thiann1-bo5, I cannot understand what he
        says). 时间 si5-kan1 (time): 时间到矣 (si5-kan1 kau3 ah4, time is
        up)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches core nouns the Min Nan way: no gender drills, no
        case tables - just the word, its tone, and a sentence that puts it
        to work. Each of the twenty-five nouns is shown with characters,
        romanization, English, and one full translated sentence. The learner
        reads each sentence aloud, listens for the tones, and substitutes
        the possessives (我的 gua2-e5, 你的 li2-e5, 伊的 i1-e5) to make the
        nouns personal. Sentences are required in every record - no
        vocabulary-list-only records."""),
    key_points=[
        "人 lang5 (person): 伊是一个好人 (i1 si7 tsit8-e5 ho2-lang5, he is a good person).",
        "Family: 老父 lau7-pe7 (father), 老母 lau7-bu2 (mother), 囝仔 gin2-a2 (child), 朋友 ping5-iu2 (friend).",
        "查埔 tsa1-poo1 (man), 查某 tsa1-boo2 (woman) - the vernacular pair for man and woman.",
        "Places: 厝 tshu3 (house), 学校 hak8-hau7 (school), 市场 tshi7-tiunn5 (market), 路 loo7 (road).",
        "Food and drink: 饭 png7 (rice/meal), 水 tsui2 (water), 茶 te5 (tea), 鱼 hi5 (fish), 肉 bah4 (meat).",
        "Nature: 天 thinn1 (sky), 地 te7 (earth), 山 suann1 (mountain), 海 hai2 (sea), 日 jit8 (sun), 月 gueh8 (moon).",
        "Things: 车 tshia1 (car), 门 mng5 (door), 钱 tsinn5 (money), 书 tsu1 (book), 话 ue7 (speech).",
        "Doctor: 医生 i1-sing1 - 医生讲无要紧 (the doctor says it is nothing serious).",
        "Time: 时间 si5-kan1 - 时间到矣 (si5-kan1 kau3 ah4, time is up).",
        "No gender, no case, no plural endings on Min Nan nouns - number comes from numerals and classifiers.",
    ],
    requirements=[
        "Learners should read all twenty-five sentences aloud, keeping tones distinct.",
        "Learners should substitute possessives (我的, 你的, 伊的) into the noun sentences.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - standard character forms for each noun.",
        "Maryknoll English-Amoy Dictionary; 1976 - Amoy (Xiamen) noun glosses.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. Noun entries with standard characters.",
        "Douglas C. Chinese-English Dictionary of the Vernacular or Spoken Language of Amoy; 1873. Noun glosses.",
    ],
    sig_lens=("Through the Signature lens, each noun is a named seal of the "
              "covenant: 人 the person-seal, 厝 the house-seal, 海 the "
              "sea-seal - twenty-five names by which the Min Nan world "
              "signs itself into being. This Signature reading seals the "
              "naming of things."),
)

E(
    key="nan_verbs", name="Min Nan Chinese Core Verbs I",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        The twenty-five essential verbs of Min Nan - each with characters,
        tone-numbered romanization, English gloss, and a full translated
        sentence. Min Nan verbs never conjugate: one form serves past,
        present, and future, and time/aspect is carried by particles (record
        21). 食 tsiah8 (eat): 我食饱矣 (gua2 tsiah8-pa2 ah4, I have eaten).
        饮 lim1 (drink): 饮茶配话 (lim1-te5 phue3-ue7, drink tea and chat).
        去 khi3 (go): 我欲去学校 (gua2 beh4 khi3 hak8-hau7, I want to go
        to school). 来 lai5 (come): 你来我去 (li2 lai5 gua2 khi3, you come
        and I go). 看 khuann3 (see, look): 你看，海真水 (li2 khuann3, hai2
        tsin1 sui2, look, the sea is so beautiful). 听 thiann1 (listen):
        你听，鸟咧叫 (li2 thiann1, tsiau2 teh4 kio3, listen, the birds are
        singing). 讲 kong2 (speak): 伊讲闽南话 (i1 kong2 ban5-lam5-ue7, he
        speaks Min Nan). 写 sia2 (write): 写字爱用心 (sia2-ji7 ai3
        iong7-sim1, writing characters takes care). 读 thak8 (read, study):
        读册读一半 (thak8-tsheh4 thak8 tsit8-puann3, read half the book).
        行 kiann5 (walk): 行路爱看车 (kiann5-loo7 ai3 khuann3-tshia1, when
        walking watch the cars). 走 tsau2 (run): 紧走，时间到矣 (kin2-tsau2,
        si5-kan1 kau3 ah4, run fast, time is up). 坐 tse7 (sit): 请坐
        (tshiann2 tse7, please sit). 睏 khun3 (sleep): 囝仔去睏矣 (gin2-a2
        khi3 khun3 ah4, the child has gone to sleep). 起来 khi2-lai5
        (get up): 紧起来，食早顿 (kin2 khi2-lai5, tsiah8 tsa2-tng3, get up
        quickly, eat breakfast). 买 be2 (buy): 我欲买一本书 (gua2 beh4 be2
        tsit8-pun2 tsu1, I want to buy a book). 卖 bue7 (sell): 伊卖鱼
        (i1 bue7-hi5, he sells fish). 做 tso3 (do, make): 做人爱老实
        (tso3-lang5 ai3 lau2-sit8, be an honest person). 学 oh8 (learn): 学
        闽南话真趣味 (oh8 ban5-lam5-ue7 tsin1 tshu3-bi7, learning Min Nan
        is great fun). 教 ka3 (teach): 先生教阮读书 (sian1-sinn1 ka3 gun2
        thak8-tsu1, the teacher teaches us to read). 爱 ai3 (love): 我爱
        你 (gua2 ai3 li2, I love you). 欲 beh4 (want): 我欲食饭 (gua2 beh4
        tsiah8-png7, I want to eat). 会 e7 (can, will): 我会讲闽南话
        (gua2 e7 kong2 ban5-lam5-ue7, I can speak Min Nan). 知 tsai1
        (know): 我知影 (gua2 tsai1-iann2, I know). 想 siunn7 (think):
        我想你 (gua2 siunn7 li2, I miss you / I am thinking of you). 问
        mng7 (ask): 有问题爱问 (u7 bun7-te5 ai3 mng7, if you have a
        question, ask). 开 khui1 (open): 开门 (khui1-mng5, open the door)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches verbs as actions with sentences, never as bare
        glosses. Each verb appears with characters, romanization, English,
        and a full sentence showing it alive - and because Min Nan verbs
        never conjugate, the learner's job is simply to learn the verb's
        tone and meaning, then let the aspect particles of record 21 carry
        the time. The learner reads each sentence aloud and builds new
        sentences by swapping the subjects (我, 你, 伊, 阮)."""),
    key_points=[
        "食 tsiah8 (eat): 我食饱矣 (gua2 tsiah8-pa2 ah4, I have eaten).",
        "饮 lim1 (drink), 去 khi3 (go), 来 lai5 (come) - the motion and intake core.",
        "看 khuann3 (see), 听 thiann1 (listen), 讲 kong2 (speak), 写 sia2 (write), 读 thak8 (read/study).",
        "行 kiann5 (walk), 走 tsau2 (run), 坐 tse7 (sit), 睏 khun3 (sleep), 起来 khi2-lai5 (get up).",
        "买 be2 (buy), 卖 bue7 (sell) - a minimal tone pair: be2 vs bue7.",
        "做 tso3 (do/make), 学 oh8 (learn), 教 ka3 (teach) - the action of living and teaching.",
        "爱 ai3 (love), 欲 beh4 (want), 会 e7 (can/will) - desire and ability.",
        "知 tsai1 (know): 我知影 (gua2 tsai1-iann2, I know); 想 siunn7 (think/miss): 我想你.",
        "问 mng7 (ask): 有问题爱问 (u7 bun7-te5 ai3 mng7, if you have a question, ask).",
        "Min Nan verbs never conjugate - one form for past, present, future; aspect particles carry the time.",
    ],
    requirements=[
        "Learners should read all twenty-five sentences aloud with correct tones.",
        "Learners should swap subjects (我, 你, 伊, 阮) through five verb sentences each.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - standard verb characters.",
        "Bodman 1955-1958 - Amoy verb usage and aspect particles.",
    ],
    citations=[
        "Bodman N C. Spoken Amoy Hokkien; 1955-1958. Verb and aspect system.",
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. Verb entries.",
    ],
    sig_lens=("Through the Signature lens, each verb is a deed-seal of the "
              "covenant: 食 the eating-seal, 行 the walking-seal, 学 the "
              "learning-seal - twenty-five actions by which the Min Nan "
              "people sign their days. This Signature reading seals the "
              "doing of things."),
)

E(
    key="nan_adjectives", name="Min Nan Chinese Adjectives and Adverbs",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Twenty-five adjectives and fifteen adverbs - each with characters,
        romanization, English, and a full sentence. Min Nan adjectives take
        no agreement: 好 ho2 (good) never changes for gender or number, and
        the predicative pattern is simply subject + 真 tsin1 + adjective.
        好 ho2: 这真好 (tse2 tsin1 ho2, this is very good). 歹 phainn2
        (bad): 歹囝仔 (phainn2 gin2-a2, a bad child). 大 tua7 (big), 细
        se3 (small): 大厝，细房 (tua7-tshu3, se3-pang5, a big house, a
        small room). 新 sin1 (new), 旧 ku7 (old): 新衫，旧裤 (sin1-sann1,
        ku7-khoo3, a new shirt, old trousers). 长 tng5 (long), 短 te2
        (short): 这条路真长 (tsit4-tiau5 loo7 tsin1 tng5, this road is very
        long). 高 kuan5 (high/tall), 低 ke7 (low): 山真高 (suann1 tsin1
        kuan5, the mountain is very high). 远 hng7 (far), 近 kun7 (near):
        学校离厝真近 (hak8-hau7 li5 tshu3 tsin1 kun7, the school is very
        near the house). 快 khuai3 (fast), 慢 ban7 (slow): 伊走真快
        (i1 tsau2 tsin1 khuai3, he runs very fast). 热 juah8 (hot), 冷
        ling2 (cold): 今仔日真热 (kin1-a2-jit8 tsin1 juah8, today is very
        hot). 甜 tinn1 (sweet), 咸 kiam5 (salty), 酸 sng1 (sour), 苦 khoo2
        (bitter): 这粒果子真甜 (tsit4-liap8 kue2-tsi2 tsin1 tinn1, this
        fruit is very sweet). 媠 sui2 (pretty): 查某囝仔真媠 (tsa1-boo2
        gin2-a2 tsin1 sui2, the girl is very pretty). 勇 iong2 (brave):
        伊真勇 (i1 tsin1 iong2, he is very brave). 聪明 tshong1-bing5
        (smart): 囝仔真聪明 (gin2-a2 tsin1 tshong1-bing5, the child is very
        smart). 欢喜 huann1-hi2 (happy): 我真欢喜 (gua2 tsin1
        huann1-hi2, I am very happy). Adverbs: 真 tsin1 (very): 真好
        (tsin1 ho2, very good). 足 tsiok4 (quite, very): 足多人 (tsiok4
        ke7 lang5, quite a lot of people). 搁 koh4 (again, also): 搁来
        (koh4 lai5, come again). 犹原 iu5-guan5 (still): 伊犹原咧睏
        (i1 iu5-guan5 teh4 khun3, he is still sleeping). 已经 i7-king1
        (already): 我已经食饱 (gua2 i7-king1 tsiah8-pa2, I have already
        eaten). 拢 long2 (all): 拢总来 (long2-tsong2 lai5, all came). 逐
        tak8 (each): 逐家拢好 (tak8-ke1 long2 ho2, everyone is fine). 嘛
        ma7 (also): 我嘛去 (gua2 ma7 khi3, I am going too). 才 tsiah4
        (only then): 食饱才去 (tsiah8-pa2 tsiah4 khi3, go only after
        eating). 捌 bat4 (have experienced): 我捌去过 (gua2 bat4 khi3-kue3,
        I have been there). 快紧 kin2 (quickly): 快紧来 (kin2 lai5, come
        quickly). 慢慢 ban7-ban7 (slowly): 慢慢行 (ban7-ban7 kiann5, walk
        slowly). 定定 tiann7-tiann7 (often): 伊定定来 (i1 tiann7-tiann7
        lai5, he comes often). 罕得 han2-tit4 (rarely): 罕得看见 (han2-tit4
        khuann3-kinn3, rarely seen)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches description the Min Nan way: subject + degree
        adverb + adjective, with no agreement to memorize. Each adjective
        and adverb is shown in a full sentence, so the learner absorbs the
        word order (adjective after the noun for attributive use with 的
        e5, or predicative with 真 tsin1) by reading, not by rules alone.
        The learner drills the 真 tsin1 frame across all twenty-five
        adjectives, then rebuilds sentences swapping in 足, 搁, 嘛, and 拢."""),
    key_points=[
        "好 ho2 (good): 这真好 (tse2 tsin1 ho2, this is very good); 歹 phainn2 (bad) is its opposite.",
        "Size: 大 tua7 (big), 细 se3 (small); length: 长 tng5 (long), 短 te2 (short); height: 高 kuan5, 低 ke7.",
        "Distance: 远 hng7 (far), 近 kun7 (near); speed: 快 khuai3 (fast), 慢 ban7 (slow).",
        "Temperature: 热 juah8 (hot), 冷 ling2 (cold); tastes: 甜 tinn1, 咸 kiam5, 酸 sng1, 苦 khoo2.",
        "People: 媠 sui2 (pretty), 勇 iong2 (brave), 聪明 tshong1-bing5 (smart), 欢喜 huann1-hi2 (happy).",
        "No agreement: adjectives never change for gender or number.",
        "Degree adverbs: 真 tsin1 (very), 足 tsiok4 (quite), 嘛 ma7 (also), 拢 long2 (all), 逐 tak8 (each).",
        "Time adverbs: 搁 koh4 (again), 犹原 iu5-guan5 (still), 已经 i7-king1 (already), 才 tsiah4 (only then).",
        "Frequency: 定定 tiann7-tiann7 (often), 罕得 han2-tit4 (rarely); manner: 慢慢 ban7-ban7 (slowly).",
        "Experience: 捌 bat4 - 我捌去过 (gua2 bat4 khi3-kue3, I have been there).",
    ],
    requirements=[
        "Learners should drill the 真 tsin1 frame across all twenty-five adjectives aloud.",
        "Learners should rebuild five sentences swapping in 足, 搁, 嘛, and 拢.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - adjective and adverb entries.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. Adjective/adverb entries.",
        "Chung R F. The Descriptive Grammar of Taiwanese. Crane; 2006. Adjective predicates and degree adverbs.",
    ],
    sig_lens=("Through the Signature lens, adjectives are the covenant's "
              "colors and adverbs its rhythms: 好 the good-seal, 媠 the "
              "beauty-seal, 真 the very-seal that deepens every color. "
              "This Signature reading seals the describing of the world."),
)

E(
    key="nan_pronouns", name="Min Nan Chinese Pronouns",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        The full Min Nan pronoun paradigms - personal, possessive,
        demonstrative, and interrogative - each with example sentences.
        Personal: 我 gua2 (I), 汝 li2 (you), 伊 i1 (he/she/it), 阮 gun2
        (we, excluding you), 咱 lan2 (we, including you), 恁 lin2 (you
        plural), 怹 in1 (they). The 阮/咱 split is the pride of Min Nan:
        阮 gun2 excludes the listener, 咱 lan2 includes them - 我爱你，你
        爱我，咱做伙 (gua2 ai3 li2, li2 ai3 gua2, lan2 tso3-hue2, I love
        you, you love me, let us (you and I) be together). Possessive adds
        the particle 诶 e5: 我的 gua2-e5 (my/mine): 这是我的书 (tse2 si7
        gua2-e5 tsu1, this is my book). 你的 li2-e5 (your), 伊的 i1-e5
        (his/her), 阮的 gun2-e5 (our, excl.), 咱的 lan2-e5 (our, incl.),
        恁的 lin2-e5 (your pl.), 怹的 in1-e5 (their). Reflexive uses 家己
        ka1-ki7 (self): 家己做 (ka1-ki7 tso3, do it yourself). Demonstrative:
        这 tse2 (this), 彼 he2 (that), 遮 tsia2 (here), 遐 hia2 (there):
        这是我的，彼是你的 (tse2 si7 gua2-e5, he2 si7 li2-e5, this is mine,
        that is yours). 这边 tsit4-ping1 (this side), 彼边 hit4-ping1
        (that side). Interrogative: 啥 siann2 (what): 这是啥 (tse2 si7
        siann2, what is this). 啥人 siann2-lang5 (who): 啥人来 (siann2-lang5
        lai5, who came). 叨位 to2-ui7 (where): 你叨位去 (li2 to2-ui7
        khi3, where are you going). 当时 tang1-si5 (when): 你当时来
        (li2 tang1-si5 lai5, when are you coming). 按怎 an2-tsuann2 (how):
        按怎做 (an2-tsuann2 tso3, how to do it). 为啥物 ui7-siann2-mih8
        (why): 为啥物无来 (ui7-siann2-mih8 bo5 lai5, why did you not
        come). 偌济 gua7-tse7 (how many): 偌济钱 (gua7-tse7 tsinn5, how
        much money). 几 kui2 (how many, small numbers): 几个人 (kui2-e5
        lang5, how many people). 叨一个 to2-tsit8-e5 (which one): 你爱叨
        一个 (li2 ai3 to2-tsit8-e5, which one do you want). Min Nan pronouns
        never change for case: 我 is I, me, and my (before 诶); politeness
        is carried by tone of voice and the 您 lin2 respectful form."""),
    how_it_works=textwrap.dedent("""\
        This record teaches pronouns as a paradigm the learner can chant:
        我汝伊, 阮咱, 恁怹 - seven persons, one pattern, with the 阮/咱
        inclusive-exclusive split drilled through paired sentences (阮去,
        你免 vs 咱做伙). Possessives are built by adding 诶 e5, demonstratives
        by pointing (这/彼/遮/遐), interrogatives by question drills. Every
        pronoun gets its sentence, so the paradigm lives in speech, not in a
        table alone."""),
    key_points=[
        "我 gua2 (I), 汝 li2 (you), 伊 i1 (he/she/it) - the three singular persons.",
        "The 阮 gun2 / 咱 lan2 split: exclusive we vs inclusive we - the pride of Min Nan pronouns.",
        "恁 lin2 (you plural), 怹 in1 (they) - seven persons, one unchanging pattern.",
        "Possessive: add 诶 e5 - 我的 gua2-e5, 你的 li2-e5, 伊的 i1-e5, 咱的 lan2-e5.",
        "Reflexive: 家己 ka1-ki7 (self) - 家己做 (ka1-ki7 tso3, do it yourself).",
        "Demonstratives: 这 tse2 (this), 彼 he2 (that), 遮 tsia2 (here), 遐 hia2 (there).",
        "Interrogatives: 啥 siann2 (what), 啥人 siann2-lang5 (who), 叨位 to2-ui7 (where), 当时 tang1-si5 (when).",
        "按怎 an2-tsuann2 (how), 为啥物 ui7-siann2-mih8 (why), 偌济 gua7-tse7 (how many), 几 kui2 (how few).",
        "No case changes: 我 is I, me, and (with 诶) mine.",
        "Politeness: 您 lin2 as the respectful you; tone of voice carries the rest.",
    ],
    requirements=[
        "Learners should chant the seven personal pronouns with tones until automatic.",
        "Learners should drill 阮 vs 咱 in paired sentences until the split is natural.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - pronoun entries and the 阮/咱 distinction.",
    ],
    citations=[
        "Chung R F. The Descriptive Grammar of Taiwanese. Crane; 2006. Pronoun system.",
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 阮, 咱, 怹 entries.",
    ],
    sig_lens=("Through the Signature lens, pronouns are the covenant's "
              "circle of persons: 我 the I-seal, 咱 the we-together-seal "
              "that gathers speaker and listener into one signed name, 怹 "
              "the they-seal of the far shore. This Signature reading seals "
              "the naming of persons."),
)

E(
    key="nan_numbers", name="Min Nan Chinese Numbers and Time",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Numbers 1-100, ordinals, days, months, seasons, clock time, and
        dates - each with example sentences. The digits: 一 tsit8 (1), 二
        ji7 (2), 三 sann1 (3), 四 si3 (4), 五 goo7 (5), 六 lak8 (6), 七
        tshit4 (7), 八 peh4 (8), 九 kau2 (9), 十 tsap8 (10), 百 pah4
        (100), 千 tshing1 (1000), 万 ban7 (10000). Eleven is 十一
        tsap8-it4, twenty is 二十 ji7-tsap8, twenty-five 二十五
        ji7-tsap8-goo7, one hundred 一百 tsit8-pah4, one thousand 一千
        tsit8-tshing1, ten thousand 一万 tsit8-ban7. For counting people
        and things, 二 is often 两 nng7: 两个人 nng7-e5 lang5 (two
        people). Ordinals add 第 te7: 第一 te7-it4 (first): 伊考第一名
        (i1 kho2 te7-it4 mia5, he ranked first). Days of the week use 礼拜
        le2-pai3: 礼拜一 le2-pai3-it4 (Monday), 礼拜二, 礼拜三, 礼拜四,
        礼拜五, 礼拜六, 礼拜日 le2-pai3-jit8 (Sunday): 礼拜日我歇困
        (le2-pai3-jit8 gua2 hioh4-khun3, I rest on Sunday). Months: 一月
        it4-gueh8 (January) through 十二月 tsap8-ji7-gueh8 (December); the
        lunar first month is 正月 tsiann1-gueh8: 正月拜年 (tsiann1-gueh8
        pai3-ni5, New Year visits in the first lunar month). Seasons: 春
        tshun1 (spring), 夏 ha7 (summer), 秋 tshiu1 (autumn), 冬 tang1
        (winter): 春天花开 (tshun1-thinn1 hue1 khui1, flowers bloom in
        spring). Clock time: 点 tiam2 (o'clock), 分 hun1 (minute), 半
        puann3 (half), 刻 khik4 (quarter): 三点 sann1-tiam2 (3 o'clock),
        三点半 sann1-tiam2-puann3 (3:30), 三点十五分 sann1-tiam2
        tsap8-goo7-hun1 (3:15): 现在几点 (hian7-tsai7 kui2-tiam2, what
        time is it now). Dates: year 年 ni5, month 月 gueh8, day 日 jit8
        or 号 ho7: 今仔日几月几日 (kin1-a2-jit8 kui2-gueh8 kui2-jit8,
        what is today's date). Time words: 今仔日 kin1-a2-jit8 (today),
        昨昏 tsa1-hng1 (yesterday), 明仔载 bin5-a2-tsai3 (tomorrow), 早起
        tsa2-khi2 (morning), 下晡 e7-poo1 (afternoon), 暗 am3 (evening),
        顶晡 ting2-poo1 (forenoon), 下昏 e7-hng1 (tonight): 明仔载早起我
        欲去台北 (bin5-a2-tsai3 tsa2-khi2 gua2 beh4 khi3 Tai5-pak4,
        tomorrow morning I am going to Taipei). Duration: 一个钟头
        tsit8-e5 tsing1-thau5 (one hour), 一分钟 tsit8-hun1-tsing1 (one
        minute)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches numbers as counting drills with real sentences.
        The learner counts 1-100 aloud until the tsit8-ji7-sann1-si3-goo7
        sequence is automatic, then builds compound numbers (二十五,
        一百, 一万) by the place-value rule. Ordinals, weekdays, months,
        clock time, and dates are each drilled with a question the learner
        answers aloud (现在几点, 今仔日几月几日). Every number gets its
        sentence, so counting becomes speaking."""),
    key_points=[
        "Digits: 一 tsit8, 二 ji7, 三 sann1, 四 si3, 五 goo7, 六 lak8, 七 tshit4, 八 peh4, 九 kau2, 十 tsap8.",
        "Compounds: 十一 tsap8-it4, 二十 ji7-tsap8, 二十五 ji7-tsap8-goo7, 一百 tsit8-pah4, 一千 tsit8-tshing1, 一万 tsit8-ban7.",
        "两 nng7 for counting things: 两个人 nng7-e5 lang5 (two people).",
        "Ordinals: 第 te7 - 第一 te7-it4 (first).",
        "Weekdays: 礼拜一 le2-pai3-it4 (Monday) through 礼拜日 le2-pai3-jit8 (Sunday).",
        "Months: 一月 it4-gueh8 to 十二月 tsap8-ji7-gueh8; lunar new year month: 正月 tsiann1-gueh8.",
        "Seasons: 春 tshun1, 夏 ha7, 秋 tshiu1, 冬 tang1.",
        "Clock: 点 tiam2, 分 hun1, 半 puann3, 刻 khik4 - 三点半 sann1-tiam2-puann3 (3:30).",
        "Ask the time: 现在几点 (hian7-tsai7 kui2-tiam2); ask the date: 今仔日几月几日.",
        "Time words: 今仔日 kin1-a2-jit8 (today), 昨昏 tsa1-hng1 (yesterday), 明仔载 bin5-a2-tsai3 (tomorrow).",
    ],
    requirements=[
        "Learners should count 1-100 aloud with correct tones until automatic.",
        "Learners should answer 现在几点 and 今仔日几月几日 aloud for the real time and date.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - numeral and time-word entries.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. Numerals, weekdays, time words.",
        "Bodman N C. Spoken Amoy Hokkien; 1955-1958. Number compounds.",
    ],
    sig_lens=("Through the Signature lens, numbers are the covenant's "
              "measure: 一 the one-seal of beginning, 十 the ten-seal of "
              "completion, 万 the ten-thousand-seal of multitude - and time "
              "words the calendar by which the covenant keeps its days. "
              "This Signature reading seals the counting of things."),
)

E(
    key="nan_greetings", name="Min Nan Chinese Greetings and Everyday Phrases",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        Thirty greetings, farewells, and politeness phrases - each with
        characters, romanization, English, and usage notes. The classic Min
        Nan greeting is not 你好 li2-ho2 (hello) but 食饱未 tsiah8-pa2-bue7
        (have you eaten yet) - care expressed as food. 你好 li2-ho2
        (hello, general). 食饱未 tsiah8-pa2-bue7 (have you eaten - the warm
        everyday greeting). 逐家好 tak8-ke1-ho2 (hello everyone). 早 tsa2
        (morning - the short dawn greeting). 暗安 am3-an1 (good evening).
        欢迎 huan1-ging5 (welcome). 请坐 tshiann2-tse7 (please sit). 请饮茶
        tshiann2 lim1-te5 (please have tea). 多谢 to7-sia7 (thank you). 劳力
        loo7-lat8 (thanks for your effort - to workers and helpers). 毋免
        客气 m7-bian2 kheh4-khi3 (you are welcome, don't stand on
        ceremony). 歹势 phainn2-se3 (sorry, excuse me - the all-purpose
        apology). 请问 tshiann2-mng7 (excuse me, may I ask). 借过 tsioh4-kue3
        (excuse me, passing through). 再会 tsai3-hue7 (goodbye, see you
        again). 慢走 ban7-tsau2 (go slowly - said to a departing guest). 顺
        行 sun7-kiann5 (safe travels). 保重 po2-tiong7 (take care). 有闲来
        坐 u7-ing5 lai5 tse7 (come sit when you are free - the open
        invitation). 恭喜 kiong1-hi2 (congratulations). 生日快乐
        sinn1-jit8 khuai3-lok8 (happy birthday). 新年快乐 sin1-ni5
        khuai3-lok8 (happy new year). 中秋节快乐 tiong1-tshiu1-tseh4
        khuai3-lok8 (happy Mid-Autumn Festival). 好久无看见 ho2-ku2 bo5
        khuann3-kinn3 (long time no see). 你好无 li2-ho2-bo5 (how are you -
        are you well). 身体好无 sin1-the2 ho2-bo5 (is your health good).
        头家好 thau5-ke1-ho2 (hello boss - respectful to shopkeepers).
        先生好 sian1-sinn1-ho2 (hello teacher/sir). 阿姨好 a1-i5-ho2
        (hello auntie). 无要紧 bo5 iau3-kin2 (it does not matter). 好啊
        ho2-ah4 (okay, fine). 知影 tsai1-iann2 (I see, got it). 安呢
        an2-ne1 (like this - the discourse glue of conversation)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches greetings as social scripts with usage notes, so
        the learner knows not just the words but when Min Nan speakers use
        them: 食饱未 for warmth, 歹势 for apology, 慢走 for farewell, 劳力
        for thanks-to-workers. Each phrase carries its note (who says it to
        whom, and when), and the learner practices full mini-exchanges:
        greeting, thanks, apology, farewell. Politeness in Min Nan is warm
        and food-centered - the phrases teach the culture with the
        language."""),
    key_points=[
        "你好 li2-ho2 (hello) - but the true Min Nan greeting is 食饱未 tsiah8-pa2-bue7 (have you eaten).",
        "逐家好 tak8-ke1-ho2 (hello everyone); 早 tsa2 (morning); 暗安 am3-an1 (good evening).",
        "Thanks: 多谢 to7-sia7; thanks for effort: 劳力 loo7-lat8; you are welcome: 毋免客气 m7-bian2 kheh4-khi3.",
        "Sorry/excuse me: 歹势 phainn2-se3; may I ask: 请问 tshiann2-mng7; passing through: 借过 tsioh4-kue3.",
        "Farewell: 再会 tsai3-hue7 (see you again); to a departing guest: 慢走 ban7-tsau2; safe travels: 顺行 sun7-kiann5.",
        "Take care: 保重 po2-tiong7; the open invitation: 有闲来坐 u7-ing5 lai5 tse7.",
        "Congratulations: 恭喜 kiong1-hi2; birthday: 生日快乐 sinn1-jit8 khuai3-lok8.",
        "Long time no see: 好久无看见 ho2-ku2 bo5 khuann3-kinn3; how are you: 你好无 li2-ho2-bo5.",
        "Respectful address: 头家好 thau5-ke1-ho2 (boss), 先生好 sian1-sinn1-ho2 (teacher/sir).",
        "Discourse glue: 安呢 an2-ne1 (like this); agreement: 好啊 ho2-ah4; I see: 知影 tsai1-iann2.",
    ],
    requirements=[
        "Learners should practice the four mini-exchanges (greet, thank, apologize, farewell) aloud with a partner.",
        "Learners should use 食饱未 as a greeting at least once in real conversation this week.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - greeting and politeness entries.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. Greetings, 食饱未, 歹势 entries.",
        "Maryknoll Language Service Center. English-Amoy Dictionary; 1976. Everyday phrases.",
    ],
    sig_lens=("Through the Signature lens, greetings are the covenant's "
              "daily renewals: 食饱未 the bread-seal asked at every "
              "meeting, 多谢 the thanks-seal, 再会 the "
              "until-we-meet-again seal - thirty small signatures by which "
              "the people re-sign their bond each day. This Signature "
              "reading seals the courtesies."),
)

E(
    key="nan_grammar", name="Min Nan Chinese Grammar Essentials",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=textwrap.dedent("""\
        The working grammar of Min Nan - word order, classifiers, negation,
        questions, comparison, and the passive - each rule with translated
        example sentences. Word order is SVO, as in Mandarin: 我食饭
        (gua2 tsiah8-png7, I eat rice). Topic-fronting is common: 饭我食饱
        矣 (png7 gua2 tsiah8-pa2 ah4, the rice - I have eaten it). There is
        no gender, no case, no verb conjugation. Number is shown with
        numerals + classifiers: 一个人 tsit8-e5 lang5 (one person), 一只狗
        tsit8-tsiah4 kau2 (one dog), 一条路 tsit8-tiau5 loo7 (one road),
        一张批 tsit8-tiunn1 phue1 (one letter), 一本书 tsit8-pun2 tsu1
        (one book), 一间厝 tsit8-king1 tshu3 (one house), 一台车
        tsit8-tai5 tshia1 (one car), 一杯茶 tsit8-pue1 te5 (one cup of tea).
        Articles: 这 tse2 (this) and 彼 he2 (that) do the work of the -
        这本书 tsit4-pun2 tsu1 (this book). Negation: 毋 m7 negates verbs
        (我毋去 gua2 m7 khi3, I am not going), 无 bo5 negates existence and
        past (我无去 gua2 bo5 khi3, I did not go; 我无钱 gua2 bo5 tsinn5, I
        have no money), 袂 bue7 means cannot (我袂去 gua2 bue7 khi3, I
        cannot go), 免 bian2 means need not (免去 bian2 khi3, no need to
        go), 莫 mai3 means do not (imperative: 莫吵 mai3 tsha2, do not make
        noise). Questions: yes-no with 敢 kam2 - 你敢欲去 (li2 kam2 beh4
        khi3, are you going); or with 咩 mih8 - 你食饱咩 (li2 tsiah8-pa2
        mih8, have you eaten); A-not-A: 好毋好 ho2-m7-ho2 (is it good or
        not); choice with 抑 iah8: 你欲食饭抑面 (li2 beh4 tsiah8-png7 iah8
        mi7, do you want rice or noodles). Question words sit in place:
        啥人来 siann2-lang5 lai5 (who came). Comparison: 较 khah4 (more) -
        伊较悬 i1 khah4 kuan5 (he is taller); 上 siong7 (most) - 上好
        siong7-ho2 (the best); 甲 kah4 (than) - 伊较我高
        i1 khah4 gua2 kuan5 (he is taller than me). Passive with 予 hoo7
        (by): 予人拍 hoo7-lang5 phah4 (beaten by someone). Disposal with
        共 ka7: 共门关起来 ka7-mng5 kuainn1 khi2-lai5 (close the door).
        Result complements with 到 kau3: 我听有 gua2 thiann1-u7 (I can hear
        and understand); potential with 会 e7 and 袂 bue7: 看会着
        khuann3-e7-tioh8 (can see), 看袂着 khuann3-bue7-tioh8 (cannot
        see). Sentence-final particles: 矣 ah4 (completed change), 咧
        teh4 (progressive), 啦 lah4 (emphasis), 呢 ne1 (softening), 喔
        ooh4 (informing)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches grammar as sentence patterns, not as tables.
        Each rule - SVO order, classifiers, the five negators (毋, 无, 袂,
        免, 莫), the four question types, comparison, passive - is shown in
        two or three full translated sentences, and the learner's drill is
        transformation: turn a statement into a 敢-question, into an
        A-not-A question, into a negated sentence, into a comparative. The
        patterns are the skeleton; the themed records 11-20 hang the flesh
        on them."""),
    key_points=[
        "Word order: SVO - 我食饭 (gua2 tsiah8-png7, I eat rice); topic-fronting is common.",
        "No gender, no case, no conjugation - number comes from numerals + classifiers.",
        "Classifiers: 个 e5, 只 tsiah4 (animals), 条 tiau5 (long), 张 tiunn1 (flat), 本 pun2 (books), 间 king1 (rooms), 台 tai5 (machines).",
        "Negation: 毋 m7 (not), 无 bo5 (have not / did not), 袂 bue7 (cannot), 免 bian2 (need not), 莫 mai3 (do not - imperative).",
        "Questions: 敢 kam2 (yes-no), A-not-A (好毋好 ho2-m7-ho2), 抑 iah8 (or-choice), question words in place.",
        "Comparison: 较 khah4 (more), 上 siong7 (most), 甲 kah4 (than) - 伊较我高 (he is taller than me).",
        "Passive: 予 hoo7 (by) - 予人拍 (beaten by someone); disposal: 共 ka7 - 共门关起来.",
        "Potential complements: 会 e7 / 袂 bue7 - 看会着 (can see), 看袂着 (cannot see).",
        "Result: 到 kau3 and 有 u7 - 我听有 (I understand by hearing).",
        "Particles: 矣 ah4 (change), 咧 teh4 (progressive), 啦 lah4 (emphasis), 呢 ne1 (softening), 喔 ooh4 (informing).",
    ],
    requirements=[
        "Learners should transform five statements into each question type aloud.",
        "Learners should drill the five negators in matched sentence pairs.",
    ],
    standards=[
        "Chung R F. The Descriptive Grammar of Taiwanese; 2006 - the standard reference grammar.",
        "Bodman 1955-1958 - Amoy sentence patterns.",
    ],
    citations=[
        "Chung R F. The Descriptive Grammar of Taiwanese. Crane Publishing; 2006. Word order, negation, questions, comparison.",
        "Bodman N C. Spoken Amoy Hokkien; 1955-1958. Classifiers and particles.",
    ],
    sig_lens=("Through the Signature lens, grammar is the covenant's "
              "architecture: SVO the straight road of the sentence, the "
              "five negators five gates that close it, 敢 the "
              "question-door, 较 the rising stair of comparison - every "
              "rule a beam in the house the people built to live in "
              "together. This Signature reading seals the structure."),
)

E(
    key="nan_home", name="Min Nan Chinese Home and Family Sentences",
    group="Compounded", ladder_rank=4, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences of home and family life - house, rooms, furniture,
        and family members - each in characters, romanization, and English.
        1. 这是我的厝 (tse2 si7 gua2-e5 tshu3, this is my house). 2. 厝里
        有三间房 (tshu3-lai7 u7 sann1-king1 pang5, the house has three
        rooms). 3. 客厅真大 (kheh4-thiann1 tsin1 tua7, the living room is
        very big). 4. 厨房咧后面 (tsu5-pang5 teh4 au7-bin7, the kitchen is
        at the back). 5. 眠床真软 (bin5-tshng5 tsin1 nng2, the bed is very
        soft). 6. 桌顶有一本书 (toh4-ting2 u7 tsit8-pun2 tsu1, there is a
        book on the table). 7. 椅仔坐四个人 (i2-a2 tse7 si3-e5 lang5, the
        chairs seat four people). 8. 电视开咧 (tian7-si7 khui1 teh4, the
        TV is on). 9. 冷气真冷 (ling2-khi3 tsin1 ling2, the air conditioner
        is very cold). 10. 门窗拢关好 (mng5-thang1 long2 kuainn1-ho2, the
        doors and windows are all closed). 11. 老父咧看报纸 (lau7-pe7 teh4
        khuann3 po3-tsua2, father is reading the newspaper). 12. 老母咧煮
        饭 (lau7-bu2 teh4 tsu2-png7, mother is cooking rice). 13. 阿公去
        公园运动 (a1-kong1 khi3 kong1-hng5 un7-tong7, grandfather went to
        the park to exercise). 14. 阿嬷咧唠囝仔 (a1-ma2 teh4 lo2 gin2-a2,
        grandmother is rocking the baby). 15. 阿兄比我大三岁 (a1-hiann1 pi2
        gua2 tua7 sann1-hue3, elder brother is three years older than me -
        note 比 pi2 borrowed in comparisons). 16. 阿姊嫁去台北 (a1-tsi2
        ke3 khi3 Tai5-pak4, elder sister married and moved to Taipei). 17.
        小弟咧学校读书 (sio2-ti7 teh4 hak8-hau7 thak8-tsu1, younger brother
        is studying at school). 18. 小妹真古锥 (sio2-mue7 tsin1 koo2-tsui1,
        younger sister is very cute). 19. 阮兜有五个人 (gun2-tau1 u7 goo7-e5
        lang5, our family has five people). 20. 一家人食饭真欢喜
        (tsit8-ke1-lang5 tsiah8-png7 tsin1 huann1-hi2, the whole family
        eating together is pure joy)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the vocabulary of home by living in it: the
        learner walks room by room - 客厅, 厨房, 眠床, 桌 - meeting each
        family member - 老父, 老母, 阿公, 阿嬷, 阿兄, 阿姊, 小弟, 小妹 -
        in sentences that describe what each one is doing. The drill is
        narration: the learner describes their own house and family in Min
        Nan, sentence by sentence, using these twenty as the model."""),
    key_points=[
        "Rooms: 客厅 kheh4-thiann1 (living room), 厨房 tsu5-pang5 (kitchen), 眠床 bin5-tshng5 (bed).",
        "Furniture: 桌 toh4 (table), 椅仔 i2-a2 (chair), 电视 tian7-si7 (TV), 门窗 mng5-thang1 (doors and windows).",
        "Parents: 老父 lau7-pe7 (father), 老母 lau7-bu2 (mother); grandparents: 阿公 a1-kong1, 阿嬷 a1-ma2.",
        "Siblings: 阿兄 a1-hiann1, 阿姊 a1-tsi2, 小弟 sio2-ti7, 小妹 sio2-mue7.",
        "阮兜 gun2-tau1 (our family/home) - the warm word for household.",
        "Adjectives of home: 大 tua7 (big), 软 nng2 (soft), 冷 ling2 (cold).",
        "Progressive 咧 teh4 shows ongoing home action: 老母咧煮饭.",
        "Sentence 20 is the heart: 一家人食饭真欢喜 - the family meal as joy.",
    ],
    requirements=[
        "Learners should narrate their own house and family in Min Nan, one sentence per room and person.",
        "Learners should read all twenty sentences aloud with correct tones.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - family and household terms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 厝, 兜, family terms.",
    ],
    sig_lens=("Through the Signature lens, home is the covenant's first "
              "temple: 厝 the house-seal, 阮兜 the our-home seal, and the "
              "family meal 一家人食饭 the daily re-signing of the bond. "
              "This Signature reading seals the household."),
)

E(
    key="nan_food", name="Min Nan Chinese Food and Cooking Sentences",
    group="Compounded", ladder_rank=4, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences of meals, ingredients, cooking actions, and the
        restaurant - each in characters, romanization, and English. 1. 食
        饭矣未 (tsiah8-png7 ah4 bue7, have you eaten yet). 2. 早顿食稀饭
        (tsa2-tng3 tsiah8 he1-png7, breakfast is congee). 3. 午顿食便当
        (tau3-tng3 tsiah8 pian7-tong1, lunch is a boxed meal). 4. 晚顿阮兜
        做伙食 (am3-tng3 gun2-tau1 tso3-hue2 tsiah8, dinner we eat
        together). 5. 这碗面真好吃 (tsit4-uann2 mi7 tsin1 ho2-tsiah8,
        this bowl of noodles is delicious). 6. 鱼爱新鲜才好吃 (hi5 ai3
        sin1-tshinn1 tsiah4 ho2-tsiah8, fish must be fresh to taste good).
        7. 肉切细细才好煮 (bah4 tshiat4 se3-se3 tsiah4 ho2-tsu2, cut the
        meat small to cook it well). 8. 菜先洗才炒 (tshai3 sing1 se2
        tsiah4 tsha2, wash the vegetables before stir-frying). 9. 饭煮伤
        软 (png7 tsu2 siunn1 nng2, the rice cooked too soft). 10. 汤头真
        好 (thng1-thau5 tsin1 ho2, the broth is excellent). 11. 加一点盐
        (ke1 tsit8-tiam2 iam5, add a little salt). 12. 莫放伤多味素
        (mai3 pang3 siunn1-tse7 bi7-soo3, do not add too much MSG). 13.
        这杯茶真芳 (tsit4-pue1 te5 tsin1 phang1, this cup of tea is very
        fragrant). 14. 水果爱洗才食 (tsui2-ko2 ai3 se2 tsiah4 tsiah8,
        wash fruit before eating). 15. 芒果真甜 (suainn7-ko2 tsin1 tinn1,
        the mango is very sweet). 16. 服务生，点菜 (hok8-bu7-sing1,
        tiam2-tshai3, waiter, we are ready to order). 17. 一份蚵仔煎
        (tsit8-hun7 o5-a2-tsian1, one oyster omelet). 18. 两碗牛肉面
        (nng7-uann2 gu5-bah4-mi7, two bowls of beef noodles). 19. 结账
        (kiat4-si3, the bill please). 20. 食饱矣，多谢招待
        (tsiah8-pa2 ah4, to7-sia7 tsiau1-tai7, I am full, thanks for the
        hospitality)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches food as the center of Min Nan social life: the
        three meals (早顿, 午顿, 晚顿), the cooking verbs (煮 tsu2, 炒
        tsha2, 切 tshiat4, 洗 se2, 放 pang3), the restaurant script (点菜,
        结账), and the flavors (甜, 咸, 芳 phang1 fragrant, 好吃
        ho2-tsiah8 delicious). The learner's drill is the meal: narrate a
        full day of eating in Min Nan, then role-play ordering at a
        restaurant with a partner."""),
    key_points=[
        "Three meals: 早顿 tsa2-tng3 (breakfast), 午顿 tau3-tng3 (lunch), 晚顿 am3-tng3 (dinner).",
        "好吃 ho2-tsiah8 (delicious) - the highest praise for food.",
        "Cooking verbs: 煮 tsu2 (cook/boil), 炒 tsha2 (stir-fry), 切 tshiat4 (cut), 洗 se2 (wash), 放 pang3 (add/put).",
        "Flavors: 甜 tinn1 (sweet), 咸 kiam5 (salty), 芳 phang1 (fragrant), 新鲜 sin1-tshinn1 (fresh).",
        "Restaurant: 点菜 tiam2-tshai3 (order), 服务生 hok8-bu7-sing1 (waiter), 结账 kiat4-si3 (bill).",
        "Signature dishes: 蚵仔煎 o5-a2-tsian1 (oyster omelet), 牛肉面 gu5-bah4-mi7 (beef noodles).",
        "莫 mai3 (do not) for kitchen prohibitions: 莫放伤多味素.",
        "The closing courtesy: 食饱矣，多谢招待 - I am full, thanks for the hospitality.",
    ],
    requirements=[
        "Learners should narrate a full day of meals in Min Nan aloud.",
        "Learners should role-play ordering a three-dish meal at a restaurant.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - food and cooking terms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. Food entries: 蚵仔煎, 便当, 顿.",
    ],
    sig_lens=("Through the Signature lens, food is the covenant's "
              "communion: 食饱未 the daily bread-seal, the shared 晚顿 "
              "the evening re-signing, 多谢招待 the gratitude-seal that "
              "closes every table. This Signature reading seals the "
              "table."),
)

E(
    key="nan_travel", name="Min Nan Chinese Travel and Directions Sentences",
    group="Compounded", ladder_rank=4, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences of transport, asking directions, tickets, and
        lodging - each in characters, romanization, and English. 1. 请问，
        车头叨位 (tshiann2-mng7, tshia1-thau5 to2-ui7, excuse me, where is
        the station). 2. 火车头直行 (hue2-tshia1-thau5 tit8-kiann5, the
        train station is straight ahead). 3. 转斡正手爿 (tng2-uat4
        tsiann3-tshiu2-ping5, turn to the right). 4. 倒手爿有一间银行
        (to2-tshiu2-ping5 u7 tsit8-king1 gin5-hang5, there is a bank on the
        left). 5. 离遮远无 (li5 tsia2 hng7-bo5, is it far from here). 6. 行
        路二十分钟 (kiann5-loo7 ji7-tsap8-hun1-tsing1, twenty minutes on
        foot). 7. 坐计程车较紧 (tse7 ke3-thing5-tshia1 khah4 kin2, the taxi
        is faster). 8. 计程车偌济钱 (ke3-thing5-tshia1 gua7-tse7 tsinn5,
        how much is the taxi). 9. 我欲买两张票 (gua2 beh4 be2 nng7-tiunn1
        phio3, I want to buy two tickets). 10. 票偌济一张 (phio3 gua7-tse7
        tsit8-tiunn1, how much is one ticket). 11. 火车几点开 (hue2-tshia1
        kui2-tiam2 khui1, what time does the train leave). 12. 飞机误点
        (hui1-ki1 goo7-tiam2, the flight is delayed). 13. 行李寄放叨位
        (hing5-li2 kia3-pang3 to2-ui7, where do I check the luggage). 14.
        护照共我看一下 (hoo7-tsiau3 ka7 gua2 khuann3 tsit8-e7, show me your
        passport please). 15. 我欲住一暗 (gua2 beh4 tu7 tsit8-am3, I want
        to stay one night). 16. 双人房偌济 (siang1-lang5-pang5 gua7-tse7,
        how much is a double room). 17. 有浴室无 (u7 ik8-sik4-bo5, does it
        have a bathroom). 18. 早顿几点食 (tsa2-tng3 kui2-tiam2 tsiah8,
        what time is breakfast). 19. 冷气袂冷 (ling2-khi3 bue7 ling2, the
        air conditioner is not cold). 20. 多谢，顺行 (to7-sia7, sun7-kiann5,
        thank you, safe travels)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches travel as four scripts: asking the way (叨位,
        直行, 转斡), riding (计程车, 火车, 飞机), ticketing (买票, 几点开),
        and lodging (住一暗, 双人房). Each sentence is a line the traveler
        actually says. The drill is role-play: one learner is the traveler,
        the other the station clerk or hotel desk, running all twenty lines
        in sequence."""),
    key_points=[
        "Asking the way: 请问，车头叨位; 直行 tit8-kiann5 (straight), 转斡 tng2-uat4 (turn), 正手爿/倒手爿 (right/left).",
        "Distance and time: 离遮远无; 行路二十分钟 (twenty minutes on foot).",
        "Taxi: 坐计程车较紧; 计程车偌济钱.",
        "Tickets: 我欲买两张票; 票偌济一张; 火车几点开.",
        "Airport: 飞机误点 (delayed); 行李寄放叨位; 护照共我看一下.",
        "Hotel: 我欲住一暗; 双人房偌济; 有浴室无; 早顿几点食.",
        "Complaints politely: 冷气袂冷 (the AC is not cold).",
        "The traveler's farewell: 多谢，顺行.",
    ],
    requirements=[
        "Learners should role-play traveler and clerk through all twenty lines.",
        "Learners should ask for directions to a real nearby place in Min Nan.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - transport and lodging terms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 车头, 计程车, 住 entries.",
    ],
    sig_lens=("Through the Signature lens, travel is the covenant "
              "on the road: every 叨位 a question-seal, every 顺行 a "
              "blessing-seal laid on the traveler's back - the people who "
              "crossed seas signing their journeys one sentence at a time. "
              "This Signature reading seals the road."),
)

E(
    key="nan_work", name="Min Nan Chinese Work and School Sentences",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences of jobs, the office, the classroom, and learning -
        each in characters, romanization, and English. 1. 你做什么头路
        (li2 tso3 siann2-mih8 thau5-loo7, what work do you do). 2. 我是
        先生 (gua2 si7 sian1-sinn1, I am a teacher). 3. 伊做医生 (i1 tso3
        i1-sing1, he is a doctor). 4. 阮是做生理的 (gun2 si7 tso3
        sing1-li2-e5, we are in business). 5. 几点上班 (kui2-tiam2
        siunn7-pan1, what time does work start). 6. 五点下班 (goo7-tiam2
        ha7-pan1, work ends at five). 7. 今仔日加班 (kin1-a2-jit8
        ka1-pan1, overtime today). 8. 头家真好 (thau5-ke1 tsin1 ho2, the
        boss is very good). 9. 同事做伙真欢喜 (tong5-su7 tso3-hue2 tsin1
        huann1-hi2, working with colleagues is joyful). 10. 会议几点开
        (hue7-gi7 kui2-tiam2 khui1, what time is the meeting). 11. 这份报告
        明仔载交 (tsit4-hun7 po3-ko3 bin5-a2-tsai3 kau1, this report is due
        tomorrow). 12. 薪水偌济 (sin1-sui2 gua7-tse7, how much is the
        salary). 13. 囝仔去学校矣 (gin2-a2 khi3 hak8-hau7 ah4, the child
        has gone to school). 14. 先生咧上课 (sian1-sinn1 teh4 siunn7-kho3,
        the teacher is in class). 15. 这题我袂晓 (tsit4-te5 gua2 bue7-hiau2,
        I cannot do this problem). 16. 请先生教我 (tshiann2 sian1-sinn1 ka3
        gua2, please teach me, teacher). 17. 功课写好矣 (kong1-kho3 sia2
        ho2 ah4, the homework is done). 18. 考试考第一名 (kho2-tshi3 kho2
        te7-it4 mia5, topped the exam). 19. 读书爱认真 (thak8-tsu1 ai3
        jin7-tsin1, study seriously). 20. 学无止境 (hak8 bo5 tsi2-king2,
        learning never ends)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches work and school as two halves of the striving
        life: the job interview (做什么头路), the office day (上班, 下班,
        加班, 会议), and the classroom (上课, 功课, 考试). Each sentence is
        drilled aloud, then the learner answers the personal questions in
        Min Nan: 你做什么头路, 几点上班. The closing proverb 学无止境 is
        memorized as the record's seal."""),
    key_points=[
        "Jobs: 先生 sian1-sinn1 (teacher), 医生 i1-sing1 (doctor), 做生理 tso3 sing1-li2 (in business).",
        "Ask the job: 你做什么头路 (li2 tso3 siann2-mih8 thau5-loo7).",
        "Workday: 上班 siunn7-pan1, 下班 ha7-pan1, 加班 ka1-pan1, 会议 hue7-gi7 (meeting).",
        "Office: 头家 thau5-ke1 (boss), 同事 tong5-su7 (colleague), 报告 po3-ko3 (report), 薪水 sin1-sui2 (salary).",
        "School: 上课 siunn7-kho3, 功课 kong1-kho3 (homework), 考试 kho2-tshi3 (exam).",
        "Ask for help: 这题我袂晓; 请先生教我.",
        "Study hard: 读书爱认真; 考试考第一名.",
        "The seal: 学无止境 (hak8 bo5 tsi2-king2, learning never ends).",
    ],
    requirements=[
        "Learners should answer 你做什么头路 and 几点上班 about their real life in Min Nan.",
        "Learners should memorize 学无止境 with correct tones.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - work and school terms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 头路, 上班, 功课 entries.",
    ],
    sig_lens=("Through the Signature lens, work is the covenant's "
              "daylight and school its lamp: 头路 the labor-seal, 功课 "
              "the study-seal, and 学无止境 the unending seal over both "
              "- the people signing each day with effort. This Signature "
              "reading seals the working day."),
)

E(
    key="nan_health", name="Min Nan Chinese Health and Body Sentences",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences of body parts, symptoms, the doctor visit, and the
        pharmacy - each in characters, romanization, and English. 1. 头
        thau5 (head): 头疼 (thau5 thiann3, headache). 2. 目睭 bak8-tsiu1
        (eyes): 目睭花 (bak8-tsiu1 hue1, blurry vision). 3. 耳仔 hinn7-a2
        (ears): 耳仔听无 (hinn7-a2 thiann1-bo5, cannot hear well). 4. 嘴
        tshui3 (mouth): 嘴破 (tshui3 phua3, mouth sores). 5. 牙 ge5
        (teeth): 牙疼 (ge5 thiann3, toothache). 6. 喉 au5 (throat): 喉咙疼
        (au5-long5 thiann3, sore throat). 7. 肩头 king1-thau5 (shoulders):
        肩头酸 (king1-thau5 sng1, sore shoulders). 8. 手 tshiu2 (hands):
        手举袂高 (tshiu2 giah8 bue7 kuan5, cannot raise the hand high). 9.
        脚 kha1 (feet/legs): 脚扭着 (kha1 tsiu2-tioh8, sprained ankle). 10.
        心 sim1 (heart): 心跳真紧 (sim1 thiau3 tsin1 kin2, heart beating
        fast). 11. 肚 pat4-too2 (belly): 肚疼 (pat4-too2 thiann3,
        stomachache). 12. 我感冒矣 (gua2 kam2-mo7 ah4, I have a cold). 13.
        发烧 huat4-sio1 (fever): 有发烧无 (u7 huat4-sio1-bo5, do you have a
        fever). 14. 咳嗽 sa3-sau3 (cough): 咳嗽三日矣 (sa3-sau3 sann1-jit8
        ah4, coughing for three days). 15. 流鼻水 lau5 phinn7-tsui2 (runny
        nose). 16. 我欲看医生 (gua2 beh4 khuann3 i1-sing1, I want to see a
        doctor). 17. 叨位疼 (to2-ui7 thiann3, where does it hurt). 18. 医生
        开药仔 (i1-sing1 khui1 ioh8-a2, the doctor prescribed medicine).
        19. 一天食三摆 (tsit8-kang1 tsiah8 sann1-pai2, take three times a
        day). 20. 药房叨位 (ioh8-pang5 to2-ui7, where is the pharmacy)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the body from head to toe in symptom sentences:
        the learner points to each part - 头, 目睭, 耳仔, 嘴, 喉, 肩头,
        手, 脚, 心, 肚 - and says what hurts. Then the clinic script: 我欲
        看医生, 叨位疼, 医生开药仔, 一天食三摆, 药房叨位. The drill is the
        patient visit: one learner describes symptoms, the other plays the
        doctor, using all twenty lines."""),
    key_points=[
        "Head and face: 头 thau5, 目睭 bak8-tsiu1 (eyes), 耳仔 hinn7-a2 (ears), 嘴 tshui3 (mouth), 牙 ge5 (teeth), 喉 au5 (throat).",
        "Body: 肩头 king1-thau5 (shoulders), 手 tshiu2 (hands), 脚 kha1 (feet/legs), 心 sim1 (heart), 肚 pat4-too2 (belly).",
        "Pain pattern: X疼 (X thiann3 hurts) - 头疼, 牙疼, 肚疼.",
        "Illnesses: 感冒 kam2-mo7 (cold), 发烧 huat4-sio1 (fever), 咳嗽 sa3-sau3 (cough), 流鼻水 (runny nose).",
        "Clinic script: 我欲看医生; 叨位疼; 医生开药仔.",
        "Dosage: 一天食三摆 (tsit8-kang1 tsiah8 sann1-pai2, three times a day).",
        "Pharmacy: 药房 ioh8-pang5 - 药房叨位.",
        "Hearing and vision: 耳仔听无, 目睭花.",
    ],
    requirements=[
        "Learners should point to each body part and say its Min Nan name with tones.",
        "Learners should role-play the patient visit through all twenty lines.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - body and illness terms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 目睭, 感冒, 药房 entries.",
    ],
    sig_lens=("Through the Signature lens, the body is the covenant's "
              "first document: every 头疼 a small alarm-seal, every 我欲看 "
              "医生 a care-seal - the people tending the vessel that "
              "carries the language. This Signature reading seals the "
              "healing."),
)

E(
    key="nan_emotions", name="Min Nan Chinese Emotions and Feelings Sentences",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences of happy, sad, angry, afraid, love, and surprise -
        each in characters, romanization, and English. 1. 我真欢喜 (gua2
        tsin1 huann1-hi2, I am very happy). 2. 欢喜到欲哭 (huann1-hi2 kau3
        beh4 khau3, so happy I could cry). 3. 心内真甘 (sim1-lai7 tsin1
        kann1, sweet at heart). 4. 我真伤心 (gua2 tsin1 siong1-sim1, I am
        very sad). 5. 目屎流落来 (bak8-sai2 lau5 loh8-lai5, tears fall).
        6. 心酸酸 (sim1 sng1-sng1, heart aching). 7. 我真受气 (gua2 tsin1
        siu7-khi3, I am very angry). 8. 气到欲死 (khi3 kau3 beh4 si2, mad
        enough to die). 9. 莫受气 (mai3 siu7-khi3, do not be angry). 10.
        我真惊 (gua2 tsin1 kiann1, I am very afraid). 11. 惊到脚软 (kiann1
        kau3 kha1 nng2, scared weak in the knees). 12. 免惊，有我咧
        (bian2 kiann1, u7 gua2 teh4, do not be afraid, I am here). 13. 我爱
        你 (gua2 ai3 li2, I love you). 14. 爱到深处 (ai3 kau3 tshim1-tshu3,
        love to the depths). 15. 心肝宝贝 (sim1-kuann1 po2-pue3, darling -
        my heart and liver treasure). 16. 我真想你 (gua2 tsin1 siunn7 li2,
        I miss you so much). 17. 吓一跳 (hiann2 tsit8-tiau7, startled). 18.
        意外之喜 (i3-gua7 tsi1 hi2, a delightful surprise). 19. 放轻松
        (pang3 khin1-sang1, relax). 20. 心情真好 (sim1-tsing5 tsin1 ho2,
        in a very good mood)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches feelings as the heart's vocabulary: six
        emotions, each with three or four sentences moving from mild to
        intense - 欢喜 to 欢喜到欲哭, 伤心 to 目屎流落来, 受气 to 气到欲死,
        惊 to 惊到脚软, 爱 to 爱到深处. The 到 kau3 (to the point of) frame
        is drilled as the intensifier. The learner's drill is confession:
        say what you truly feel in Min Nan, one emotion at a time."""),
    key_points=[
        "Happy: 欢喜 huann1-hi2; intense: 欢喜到欲哭; sweet at heart: 心内真甘.",
        "Sad: 伤心 siong1-sim1; tears: 目屎流落来; aching: 心酸酸.",
        "Angry: 受气 siu7-khi3; intense: 气到欲死; calm it: 莫受气.",
        "Afraid: 惊 kiann1; intense: 惊到脚软; comfort: 免惊，有我咧.",
        "Love: 我爱你; deep: 爱到深处; darling: 心肝宝贝 sim1-kuann1 po2-pue3; miss: 我真想你.",
        "Surprise: 吓一跳 hiann2 tsit8-tiau7; 意外之喜.",
        "The intensifier: 到 kau3 (to the point of) - 欢喜到欲哭, 气到欲死, 惊到脚软.",
        "Calm: 放轻松 pang3 khin1-sang1; mood: 心情真好.",
    ],
    requirements=[
        "Learners should drill the 到 kau3 intensifier across all six emotions.",
        "Learners should speak three true feelings in Min Nan aloud.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - emotion terms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 欢喜, 受气, 心肝宝贝 entries.",
    ],
    sig_lens=("Through the Signature lens, emotions are the covenant's "
              "weather: 欢喜 its sunshine-seal, 目屎 its rain-seal, 爱 "
              "its deep-water seal - every feeling a signed confession "
              "that the people are alive together. This Signature reading "
              "seals the heart."),
)

E(
    key="nan_nature", name="Min Nan Chinese Nature and Weather Sentences",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences of animals, plants, seasons, and weather talk -
        each in characters, romanization, and English. 1. 狗 kau2 (dog):
        狗咧吠 (kau2 teh4 pui7, the dog is barking). 2. 猫 niau1 (cat):
        猫咧睏 (niau1 teh4 khun3, the cat is sleeping). 3. 鸟 tsiau2
        (bird): 鸟咧飞 (tsiau2 teh4 pue1, the birds are flying). 4. 鱼
        hi5 (fish): 鱼咧水底游 (hi5 teh4 tsui2-te2 iu5, fish swim in the
        water). 5. 蝴蝶 oo7-tiap8 (butterfly): 蝴蝶真水 (oo7-tiap8 tsin1
        sui2, the butterfly is beautiful). 6. 蜜蜂 bit8-phang1 (bee): 莫
        去弄蜜蜂 (mai3 khi3 long7 bit8-phang1, do not tease the bees). 7.
        树 tshiu7 (tree): 树顶有鸟岫 (tshiu7-ting2 u7 tsiau2-siu7, there is
        a bird nest in the tree). 8. 花 hue1 (flower): 花开真芳
        (hue1 khui1 tsin1 phang1, the flowers bloom fragrant). 9. 草
        tshau2 (grass): 草青青 (tshau2 tshenn1-tshenn1, the grass is green).
        10. 竹 tik4 (bamboo): 竹节悬 (tik4-tsat4 kuan5, the bamboo grows
        tall). 11. 春天 tshun1-thinn1 (spring): 春天真好 (tshun1-thinn1
        tsin1 ho2, spring is lovely). 12. 热天 juah8-thinn1 (summer): 热
        天真热 (juah8-thinn1 tsin1 juah8, summer is very hot). 13. 秋天
        tshiu1-thinn1 (autumn): 秋天凉凉 (tshiu1-thinn1 liang5-liang5,
        autumn is cool). 14. 寒天 kuann5-thinn1 (winter): 寒天真冷
        (kuann5-thinn1 tsin1 ling2, winter is very cold). 15. 落雨 loh8-hoo7
        (rain): 外口落雨 (gua7-khau2 loh8-hoo7, it is raining outside). 16.
        出日 tshut4-jit8 (sunshine): 出日矣 (tshut4-jit8 ah4, the sun is
        out). 17. 起风 khi2-hong1 (wind): 起风矣，紧收衫 (khi2-hong1 ah4,
        kin2 siu1-sann1, the wind is up, bring in the laundry). 18. 打雷
        tanna2-lui5 (thunder): 打雷闪电 (tanna2-lui5 siam2-tian7, thunder
        and lightning). 19. 天气 thiann1-khi3 (weather): 今仔日天气按怎
        (kin1-a2-jit8 thiann1-khi3 an2-tsuann2, how is the weather today).
        20. 好天气 ho2 thiann1-khi3 (fine weather): 好天气出去行行
        (ho2 thiann1-khi3 tshut4-khi3 kiann5-kiann5, fine weather - go out
        for a walk)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches nature as weather talk - the small conversation
        Min Nan speakers have every day. Animals and plants are met in
        action sentences (狗咧吠, 花开真芳), the four seasons named in their
        Min Nan forms (春天, 热天, 秋天, 寒天), and weather described the
        way farmers and fishers do: 落雨, 出日, 起风, 打雷. The drill is
        the daily report: the learner describes today's weather and one
        living thing seen, in Min Nan."""),
    key_points=[
        "Animals: 狗 kau2 (dog), 猫 niau1 (cat), 鸟 tsiau2 (bird), 鱼 hi5 (fish), 蝴蝶 oo7-tiap8 (butterfly), 蜜蜂 bit8-phang1 (bee).",
        "Plants: 树 tshiu7 (tree), 花 hue1 (flower), 草 tshau2 (grass), 竹 tik4 (bamboo).",
        "Seasons in Min Nan: 春天, 热天 juah8-thinn1 (summer), 秋天, 寒天 kuann5-thinn1 (winter).",
        "Rain: 落雨 loh8-hoo7; sun: 出日 tshut4-jit8; wind: 起风 khi2-hong1; thunder: 打雷 tanna2-lui5.",
        "Weather question: 今仔日天气按怎.",
        "The action frame: animal + 咧 + verb - 狗咧吠, 猫咧睏, 鸟咧飞.",
        "Fragrance: 芳 phang1 - 花开真芳.",
        "Advice with weather: 起风矣，紧收衫 (wind is up, bring in the laundry).",
    ],
    requirements=[
        "Learners should give today's weather report in Min Nan aloud.",
        "Learners should name six animals and four plants with tones.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - nature and weather terms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 落雨, 热天, 寒天 entries.",
    ],
    sig_lens=("Through the Signature lens, nature is the covenant's "
              "great witness: 落雨 its rain-seal, 出日 its sun-seal, the "
              "four seasons four seals turning over the fields the people "
              "have farmed for a thousand years. This Signature reading "
              "seals the sky and earth."),
)

E(
    key="nan_shopping", name="Min Nan Chinese Shopping and Money Sentences",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences of the market, prices, bargaining, and paying -
        each in characters, romanization, and English. 1. 头家，早
        (thau5-ke1, tsa2, morning, boss). 2. 这粒偌济 (tsit4-liap8
        gua7-tse7, how much is this one). 3. 一斤偌济 (tsit8-kin1
        gua7-tse7, how much per catty). 4. 伤贵矣 (siunn1 kui3 ah4, too
        expensive). 5. 算较俗咧 (sng3 khah4 sio7 leh4, make it cheaper).
        6. 俗一点啦 (sio7 tsit8-tiam2 lah4, a little cheaper, come on). 7.
        好啦，成交 (ho2 lah4, sing5-kau1, okay, deal). 8. 有卡俗的无
        (u7 khah4 sio7-e5-bo5, do you have a cheaper one). 9. 这件我欲
        看 (tsit4-kiann7 gua2 beh4 khuann3, I want to look at this one).
        10. 有大号的无 (u7 tua7-ho7-e5-bo5, do you have a larger size).
        11. 会使试穿无 (e7-sai2 tshi3-tshing7-bo5, may I try it on). 12.
        袋仔共我包起来 (te7-a2 ka7 gua2 pau1 khi2-lai5, bag it up for me).
        13. 找我五箍 (tsaue7 gua2 goo7-khoo1, give me five dollars change -
        箍 khoo1 is the Min Nan dollar). 14. 信用卡会使无 (sin3-iong7-khah4
        e7-sai2-bo5, can I use a credit card). 15. 现金付款 (hian7-kim1
        hoo7-khuan2, pay in cash). 16. 开发票 (khui1 huat4-phio3, issue a
        receipt). 17. 打折 (tann2-tsiat4, give a discount). 18. 买一送一
        (be2 tsit8 sang3 tsit8, buy one get one free). 19. 这是正版的
        (tse2 si7 tsiann3-pan2-e5, this is the genuine article). 20. 多谢
        惠顾 (to7-sia7 hui7-koo3, thank you for your patronage)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the market as a bargaining play in three acts:
        greeting the boss (头家，早), asking the price (这粒偌济, 一斤偌济),
        and the bargain dance (伤贵矣, 算较俗咧, 好啦，成交). Then the
        clothing shop (试穿, 大号), the till (找钱, 信用卡, 现金), and the
        farewell (多谢惠顾). The drill is the full market scene: learners
        pair up as buyer and boss and haggle through all twenty lines."""),
    key_points=[
        "Open: 头家，早 - greet the boss in the morning.",
        "Ask the price: 这粒偌济; per catty: 一斤偌济.",
        "Bargain: 伤贵矣 (too expensive); 算较俗咧 (make it cheaper); 好啦，成交 (deal).",
        "Money word: 箍 khoo1 is the Min Nan dollar - 找我五箍.",
        "Clothes: 有大号的无; 会使试穿无.",
        "Bag it: 袋仔共我包起来.",
        "Pay: 信用卡会使无; 现金付款; 开发票.",
        "Deals: 打折 (discount); 买一送一 (buy one get one free); 这是正版的.",
        "Close: 多谢惠顾 (to7-sia7 hui7-koo3, thank you for your patronage).",
    ],
    requirements=[
        "Learners should haggle a full market scene with a partner using all twenty lines.",
        "Learners should drill the bargain trio: 伤贵矣, 算较俗咧, 好啦，成交.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - market and money terms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 箍, 俗, 成交 entries.",
    ],
    sig_lens=("Through the Signature lens, the market is the covenant's "
              "trading floor: 偌济 the price-seal, 成交 the deal-seal "
              "struck with a handshake, 多谢惠顾 the gratitude-seal that "
              "keeps the customer returning for forty years. This "
              "Signature reading seals the marketplace."),
)

E(
    key="nan_social", name="Min Nan Chinese Friendship and Social Life Sentences",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences of meeting people, invitations, and celebrations -
        each in characters, romanization, and English. 1. 你好，我叫阿明
        (li2-ho2, gua2 kio3 A1-bing5, hello, I am called A-bing). 2. 幸会
        幸会 (hing7-hue7 hing7-hue7, pleased to meet you). 3. 你叨位人
        (li2 to2-ui7-lang5, where are you from). 4. 我是台南人 (gua2 si7
        Tai5-lam5-lang5, I am from Tainan). 5. 几岁 (kui2-hue3, how old are
        you). 6. 我今年二十五 (gua2 kin1-ni5 ji7-tsap8-goo7, I am
        twenty-five this year). 7. 交个朋友 (kau1-e5 ping5-iu2, make a
        friend). 8. 有闲来坐 (u7-ing5 lai5 tse7, come visit when free). 9.
        礼拜日有闲无 (le2-pai3-jit8 u7-ing5-bo5, are you free Sunday). 10.
        做伙去食饭 (tso3-hue2 khi3 tsiah8-png7, let's eat together). 11.
        我请客 (gua2 tshiann2-kheh4, my treat). 12. 毋免客气 (m7-bian2
        kheh4-khi3, don't stand on ceremony). 13. 生日快乐 (sinn1-jit8
        khuai3-lok8, happy birthday). 14. 恭喜发财 (kiong1-hi2 huat4-tsai5,
        wishing prosperity). 15. 新婚快乐 (sin1-hun1 khuai3-lok8, happy
        wedding). 16. 满月酒请你来 (mua2-gueh8-tsiu2 tshiann2 li2 lai5,
        come to the full-moon banquet). 17. 大家干杯 (tai7-ke1 kan1-pue1,
        cheers everyone). 18. 食饱饮足 (tsiah8-pa2 lim1-tsiok4, ate and
        drank to the full). 19. 下摆换我请 (e7-pai2 uann7 gua2 tshiann2,
        next time it's my treat). 20. 再会，有闲搁来 (tsai3-hue7, u7-ing5
        koh4 lai5, goodbye, come again when free)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches social life as the sequence of a Min Nan
        gathering: the introduction (我叫, 你叨位人), the invitation (有闲来
        坐, 做伙去食饭), the treating (我请客, 下摆换我请), and the
        celebration (生日快乐, 干杯, 满月酒). The drill is hosting: the
        learner introduces themselves, invites a partner to dinner, treats,
        toasts, and farewells - all in Min Nan."""),
    key_points=[
        "Introduce: 你好，我叫阿明; pleased to meet: 幸会 hing7-hue7.",
        "Where from: 你叨位人; answer: 我是台南人.",
        "Age: 几岁 kui2-hue3; 我今年二十五.",
        "Invite: 有闲来坐; 礼拜日有闲无; 做伙去食饭.",
        "Treat: 我请客; answer: 毋免客气; return: 下摆换我请.",
        "Celebrate: 生日快乐, 恭喜发财, 新婚快乐, 满月酒.",
        "Toast: 大家干杯; full: 食饱饮足.",
        "Farewell: 再会，有闲搁来.",
    ],
    requirements=[
        "Learners should host a full gathering script with a partner in Min Nan.",
        "Learners should introduce themselves with name, home, and age in Min Nan.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - social terms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 幸会, 请客, 干杯 entries.",
    ],
    sig_lens=("Through the Signature lens, friendship is the covenant "
              "renewed at the table: 我请客 the treating-seal, 干杯 the "
              "toast-seal, 下摆换我请 the returning-seal - each gathering "
              "another signature on the bond of the people. This Signature "
              "reading seals the fellowship."),
)

E(
    key="nan_tech", name="Min Nan Chinese Technology and Communication Sentences",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=textwrap.dedent("""\
        Twenty sentences of phone, internet, computer, and messaging - each
        in characters, romanization, and English. 1. 电话 tian7-ue7
        (telephone): 电话响矣 (tian7-ue7 hiang2 ah4, the phone is ringing).
        2. 接电话 (tsiap4 tian7-ue7, answer the phone). 3. 喂，你好
        (ui3, li2-ho2, hello on the phone). 4. 你叨位，我听无 (li2
        to2-ui7, gua2 thiann1-bo5, where are you, I cannot hear you). 5.
        讯号真歹 (sin3-ho7 tsin1 phainn2, the signal is bad). 6. 等一下，我
        打互你 (tan2 tsit8-e7, gua2 phah4 hoo7 li2, wait a moment, I will
        call you). 7. 手机 tshi2-ki1 (mobile phone): 手机无电矣 (tshi2-ki1
        bo5 tian7 ah4, the phone is out of battery). 8. 充电 (tshiong1-tian7,
        charge): 紧充电 (kin2 tshiong1-tian7, charge it quickly). 9. 传简讯
        (thng5 kan2-sin3, send a text): 我传简讯互你 (gua2 thng5 kan2-sin3
        hoo7 li2, I will text you). 10. 上网 tsiunn7-bang7 (go online):
        网络真慢 (bang7-loo7 tsin1 ban7, the internet is slow). 11. 电脑
        tian7-nau2 (computer): 电脑开袂起来 (tian7-nau2 khui1 bue7 khi2-lai5,
        the computer will not start). 12. 滑鼠 ku2-tshu2 (mouse): 滑鼠歹去
        (ku2-tshu2 phainn2-khi3, the mouse is broken). 13. 键盘 kian7-puann5
        (keyboard): 键盘拍无字 (kian7-puann5 phah4 bo5 ji7, the keyboard
        types no characters). 14. 寄电子邮件 (kia3 tian7-tsu2 iu5-kiann7,
        send an email). 15. 视讯 si7-sin3 (video call): 咱视讯 (lan2
        si7-sin3, let's video-call). 16. 照片传互我看 (siau3-phinn3 thng5
        hoo7 gua2 khuann3, send me the photo). 17. 按赞 (an3 tsan3, like a
        post). 18. 分享 (hun1-hiong2, share). 19. 密码记袂起来 (bit8-be2
        ki3 bue7 khi2-lai5, cannot remember the password). 20. 关机
        (kuainn1-ki1, power off): 紧关机睏 (kin2 kuainn1-ki1 khun3, power
        off and sleep)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches technology as the modern extension of Min Nan
        speech: the phone call (喂, 接电话, 讯号真歹), the mobile (手机无电,
        充电, 传简讯), the computer (电脑开袂起来, 滑鼠歹去), and the
        network (上网, 视讯, 按赞). Each sentence names the device and its
        trouble or use. The drill is the tech support call: one learner
        reports the problem, the other solves it - in Min Nan."""),
    key_points=[
        "Phone: 电话 tian7-ue7; answer: 接电话; hello: 喂 ui3.",
        "Bad signal: 讯号真歹; call back: 我打互你.",
        "Mobile: 手机 tshi2-ki1; out of battery: 手机无电矣; charge: 充电.",
        "Text: 传简讯; online: 上网 tsiunn7-bang7; slow net: 网络真慢.",
        "Computer: 电脑 tian7-nau2; mouse: 滑鼠 ku2-tshu2; keyboard: 键盘 kian7-puann5.",
        "Email: 寄电子邮件; video call: 视讯 si7-sin3.",
        "Social: 按赞 (like), 分享 (share); photo: 照片传互我看.",
        "Password trouble: 密码记袂起来; power off: 关机.",
    ],
    requirements=[
        "Learners should make a mock phone call in Min Nan covering all the phone lines.",
        "Learners should describe their own device troubles in Min Nan.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - technology terms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 手机, 电脑, 上网 entries.",
    ],
    sig_lens=("Through the Signature lens, technology is the covenant "
              "given new voice: the telephone carrying 食饱未 across "
              "oceans, the 视讯 screen a window between harbors - the old "
              "oath of meaning now signed in light. This Signature reading "
              "seals the modern voice."),
)

E(
    key="nan_tenses", name="Min Nan Chinese Verb Tenses in Sentences",
    group="Advanced", ladder_rank=7, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Min Nan verbs never conjugate - time and aspect are carried by
        particles and helpers. Five or more translated sentences per
        pattern. Present habitual with 定定 or 会 e7: 我定定去公园
        (gua2 tiann7-tiann7 khi3 kong1-hng5, I often go to the park); 伊会
        讲闽南话 (i1 e7 kong2 ban5-lam5-ue7, he can/speaks Min Nan); 鸟会飞
        (tsiau2 e7 pue1, birds fly). Progressive with 咧 teh4: 伊咧食饭
        (i1 teh4 tsiah8-png7, he is eating); 雨咧落 (hoo7 teh4 loh8, it is
        raining); 囝仔咧哭 (gin2-a2 teh4 khau3, the child is crying); 阮咧
        开会 (gun2 teh4 khui1 hue7-gi7, we are in a meeting); 你咧创啥
        (li2 teh4 tshong3 siann2, what are you doing). Completed with 矣
        ah4: 我食饱矣 (gua2 tsiah8-pa2 ah4, I have eaten); 伊来矣 (i1 lai5
        ah4, he has come); 雨停矣 (hoo7 thing5 ah4, the rain has stopped);
        电影开始矣 (tian7-iann2 khai1-si2 ah4, the movie has started); 天暗
        矣 (thinn1 am3 ah4, it has gotten dark). Past experience with 捌
        bat4 and 过 kue3: 我捌去过北京 (gua2 bat4 khi3-kue3 Pak4-kiann1, I
        have been to Beijing); 伊捌食过 (i1 bat4 tsiah8-kue3, he has eaten
        it before); 阮捌见过面 (gun2 bat4 kinn3-kue3 bin7, we have met
        before); 你捌听过这条歌无 (li2 bat4 thiann1-kue3 tsit4-tiau5 kua1-bo5,
        have you heard this song); 我无去过 (gua2 bo5 khi3-kue3, I have
        never been). Past completed with 有 u7: 我有去 (gua2 u7 khi3, I
        went); 伊有讲 (i1 u7 kong2, he said it); 阮有食 (gun2 u7 tsiah8, we
        ate); 你有看见无 (li2 u7 khuann3-kinn3-bo5, did you see it); 伊有
        来 (i1 u7 lai5, he came). Future with 欲 beh4 and 会 e7: 我欲去
        (gua2 beh4 khi3, I am going to go); 明仔载会落雨 (bin5-a2-tsai3 e7
        loh8-hoo7, it will rain tomorrow); 伊欲买车 (i1 beh4 be2 tshia1, he
        wants to buy a car); 阮会成功 (gun2 e7 sing5-kong1, we will
        succeed); 你会来无 (li2 e7 lai5-bo5, will you come). Negative
        futures: 我袂去 (gua2 bue7 khi3, I cannot/will not go); 明仔载袂
        落雨 (bin5-a2-tsai3 bue7 loh8-hoo7, it will not rain tomorrow).
        Imperative with 莫 mai3 and 紧 kin2: 莫吵 (mai3 tsha2, do not make
        noise); 紧来 (kin2 lai5, come quickly); 坐下 (tse7-he7, sit down);
        听好 (thiann1-ho2, listen well); 慢慢讲 (ban7-ban7 kong2, speak
        slowly)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the aspect system as the engine of Min Nan time:
        咧 for ongoing, 矣 for completed, 捌...过 for experienced, 有 for
        past-done, 欲/会 for future - each with five living sentences. The
        drill is the time machine: take one verb (食, 去, 来, 看) and run it
        through all six patterns, so the learner feels how Min Nan tells
        time without ever changing the verb."""),
    key_points=[
        "Habitual: 定定 tiann7-tiann7 (often), 会 e7 (can/always) - 我定定去公园.",
        "Progressive: 咧 teh4 - 伊咧食饭 (he is eating); 你咧创啥 (what are you doing).",
        "Completed: 矣 ah4 - 我食饱矣; 伊来矣; 天暗矣.",
        "Experience: 捌 bat4 ... 过 kue3 - 我捌去过北京; negative: 我无去过.",
        "Past done: 有 u7 - 我有去 (I went); 你有看见无 (did you see).",
        "Future: 欲 beh4 (going to/want), 会 e7 (will) - 我欲去; 明仔载会落雨.",
        "Negative future: 袂 bue7 - 我袂去; 明仔载袂落雨.",
        "Imperative: 莫 mai3 (do not), 紧 kin2 (quickly) - 莫吵; 紧来.",
        "The verb never changes - particles carry all the time.",
    ],
    requirements=[
        "Learners should run four verbs through all six aspect patterns aloud.",
        "Learners should narrate yesterday, today, and tomorrow in Min Nan using the right particles.",
    ],
    standards=[
        "Chung R F. The Descriptive Grammar of Taiwanese; 2006 - aspect system.",
        "Bodman 1955-1958 - Amoy aspect particles.",
    ],
    citations=[
        "Chung R F. The Descriptive Grammar of Taiwanese. Crane; 2006. Aspect: 咧, 矣, 捌, 有, 欲.",
        "Bodman N C. Spoken Amoy Hokkien; 1955-1958. Tense and aspect.",
    ],
    sig_lens=("Through the Signature lens, aspect is the covenant's "
              "handling of time: 咧 the now-seal, 矣 the done-seal, 捌 "
              "the lived-seal, 欲 the will-seal - the verb standing "
              "unmoved like a pillar while time flows around it in signed "
              "particles. This Signature reading seals time itself."),
)

E(
    key="nan_qa", name="Min Nan Chinese Questions and Answers",
    group="Advanced", ladder_rank=7, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty question-and-answer pairs covering who, what, where, when,
        why, and how - each in characters, romanization, and English. 1. Q:
        你是谁 (li2 si7 siann2-lang5, who are you) A: 我是阿明 (gua2 si7
        A1-bing5, I am A-bing). 2. Q: 这是啥 (tse2 si7 siann2, what is this)
        A: 这是茶 (tse2 si7 te5, this is tea). 3. Q: 啥人来 (siann2-lang5
        lai5, who came) A: 阿母来 (a1-bu2 lai5, mother came). 4. Q: 你欲食
        啥 (li2 beh4 tsiah8 siann2, what do you want to eat) A: 我欲食面
        (gua2 beh4 tsiah8 mi7, I want noodles). 5. Q: 车头叨位
        (tshia1-thau5 to2-ui7, where is the station) A: 直行就到
        (tit8-kiann5 to7 kau3, straight ahead and you arrive). 6. Q: 你叨位
        去 (li2 to2-ui7 khi3, where are you going) A: 我去市场 (gua2 khi3
        tshi7-tiunn5, I am going to the market). 7. Q: 厕所叨位
        (tshik4-soo2 to2-ui7, where is the restroom) A: 倒手爿 (to2-tshiu2-ping5,
        on the left). 8. Q: 你当时来 (li2 tang1-si5 lai5, when are you
        coming) A: 明仔载早起 (bin5-a2-tsai3 tsa2-khi2, tomorrow morning).
        9. Q: 几点开会 (kui2-tiam2 khui1 hue7-gi7, what time is the meeting)
        A: 三点 (sann1-tiam2, three o'clock). 10. Q: 你几岁 (li2 kui2-hue3,
        how old are you) A: 我三十岁 (gua2 sann1-tsap8 hue3, I am thirty).
        11. Q: 为啥物哭 (ui7-siann2-mih8 khau3, why are you crying) A:
        目睭疼 (bak8-tsiu1 thiann3, my eyes hurt). 12. Q: 为啥物无来
        (ui7-siann2-mih8 bo5 lai5, why did you not come) A: 我病矣 (gua2
        pinn7 ah4, I was sick). 13. Q: 按怎去 (an2-tsuann2 khi3, how do I
        get there) A: 坐计程车 (tse7 ke3-thing5-tshia1, take a taxi). 14. Q:
        这按怎用 (tse2 an2-tsuann2 iong7, how do you use this) A: 按呢用
        (an2-ne1 iong7, use it like this). 15. Q: 偌济钱 (gua7-tse7 tsinn5,
        how much) A: 一百箍 (tsit8-pah4 khoo1, one hundred dollars). 16. Q:
        你敢会晓 (li2 kam2 e7-hiau2, do you know how) A: 我会晓 (gua2
        e7-hiau2, yes I do). 17. Q: 好食无 (ho2-tsiah8-bo5, is it tasty) A:
        真好吃 (tsin1 ho2-tsiah8, very tasty). 18. Q: 你食饱未
        (li2 tsiah8-pa2-bue7, have you eaten) A: 食饱矣，多谢 (tsiah8-pa2
        ah4, to7-sia7, yes, thanks). 19. Q: 欲去抑毋 (beh4 khi3 iah8 m7,
        going or not) A: 欲去 (beh4 khi3, going). 20. Q: 听有无
        (thiann1-u7-bo5, do you understand) A: 听有 (thiann1-u7, I
        understand)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches questioning as the six interrogative families -
        啥人 (who), 啥 (what), 叨位 (where), 当时 (when), 为啥物 (why),
        按怎 (how) - plus the yes-no frames (敢, 咩, A-not-A, 抑). Each
        pair is a complete exchange; the learner drills both roles, asking
        and answering, until the question words sit naturally in place (Min
        Nan never moves them to the front)."""),
    key_points=[
        "Who: 啥人 siann2-lang5 - 你是谁; 啥人来.",
        "What: 啥 siann2 - 这是啥; 你欲食啥.",
        "Where: 叨位 to2-ui7 - 车头叨位; 你叨位去; 厕所叨位.",
        "When: 当时 tang1-si5 - 你当时来; 几点开会.",
        "Why: 为啥物 ui7-siann2-mih8 - 为啥物哭; 为啥物无来.",
        "How: 按怎 an2-tsuann2 - 按怎去; 这按怎用.",
        "How much/many: 偌济 gua7-tse7; 几 kui2 - 你几岁.",
        "Yes-no: 敢 kam2; 咩 mih8; A-not-A; 抑 iah8 - 你敢会晓; 欲去抑毋.",
        "Question words stay in place - Min Nan never fronts them.",
        "The polite check: 听有无 - do you understand.",
    ],
    requirements=[
        "Learners should drill all twenty pairs in both roles aloud.",
        "Learners should ask and answer six original questions in Min Nan.",
    ],
    standards=[
        "Chung R F. The Descriptive Grammar of Taiwanese; 2006 - interrogatives.",
    ],
    citations=[
        "Chung R F. The Descriptive Grammar of Taiwanese. Crane; 2006. Question formation.",
        "Bodman N C. Spoken Amoy Hokkien; 1955-1958. Interrogative patterns.",
    ],
    sig_lens=("Through the Signature lens, questions are the covenant's "
              "open doors: 啥人 the who-door, 叨位 the where-door, 为啥物 "
              "the why-door - every question an invitation-seal, every "
              "answer a gift-seal laid in the asker's hand. This Signature "
              "reading seals the asking."),
)

E(
    key="nan_commands", name="Min Nan Chinese Commands and Requests",
    group="Advanced", ladder_rank=7, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty imperative and polite-request sentences - formal versus
        informal - each in characters, romanization, and English. Informal
        commands are direct: 紧来 (kin2 lai5, come quickly). 莫吵 (mai3
        tsha2, do not make noise). 坐下 (tse7-he7, sit down). 看 (khuann3,
        look). 听 (thiann1, listen). 紧食 (kin2 tsiah8, eat up). 出去
        (tshut4-khi3, go out). 关门 (kuainn1-mng5, close the door). 开灯
        (khui1-ting1, turn on the light). 返来 (tng2-lai5, come back). The
        softened command adds 咧 or 啦: 紧来啦 (kin2 lai5 lah4, come on
        now). 坐啦 (tse7 lah4, do sit). Polite requests use 请 tshiann2 and
        麻烦 ma5-huan5: 请你帮我一下 (tshiann2 li2 pang1 gua2 tsit8-e7,
        please help me a moment). 麻烦你开门 (ma5-huan5 li2 khui1-mng5,
        excuse me, open the door please). Formal requests add 您 lin2 and
        敢 kam2: 您敢会当帮我 (lin2 kam2 e7-tang3 pang1 gua2, could you help
        me). 请问路按怎行 (tshiann2-mng7 loo7 an2-tsuann2 kiann5, may I ask
        the way). 劳烦你 (loo7-huan5 li2, sorry to trouble you). Invitations
        soften with 来 and 坐: 入来坐 (jip8-lai5 tse7, come in and sit).
        请饮茶 (tshiann2 lim1-te5, please have tea). The prohibitive: 毋通
        m7-thang1 (must not) is stronger than 莫: 毋通去 (m7-thang1 khi3,
        you must not go). 毋通讲 (m7-thang1 kong2, do not say it). Group
        commands use 咱 lan2 and 来 lai5: 咱来去 (lan2 lai5-khi3, let's go).
        咱做伙 (lan2 tso3-hue2, let's do it together)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the three levels of telling: the bare command
        (紧来, 莫吵) for family and close friends, the softened command
        with 啦 and 请 for polite daily life, and the formal request with
        您, 麻烦, 劳烦 for strangers and elders. Each level is drilled in
        matched pairs (关门 vs 麻烦你关门 vs 劳烦您关门), so the learner
        feels the politeness ladder in the mouth, not just in a rule."""),
    key_points=[
        "Direct: 紧来, 莫吵, 坐下, 看, 听 - for family and close friends.",
        "Softened: add 啦 lah4 - 紧来啦; 坐啦.",
        "Polite: 请 tshiann2 - 请你帮我一下; 麻烦 ma5-huan5 - 麻烦你开门.",
        "Formal: 您 lin2, 敢 kam2 - 您敢会当帮我; 劳烦你 loo7-huan5 li2.",
        "Asking the way: 请问路按怎行.",
        "Invitation: 入来坐; 请饮茶.",
        "Strong prohibition: 毋通 m7-thang1 - 毋通去; 毋通讲.",
        "Group: 咱 lan2 + 来 - 咱来去; 咱做伙.",
        "Three levels drilled in matched pairs: 关门 / 麻烦你关门 / 劳烦您关门.",
    ],
    requirements=[
        "Learners should drill the three politeness levels in matched pairs aloud.",
        "Learners should give five commands and five polite requests from real life.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - imperative and politeness forms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 莫, 毋通, 麻烦 entries.",
        "Chung R F. The Descriptive Grammar of Taiwanese; 2006. Imperatives.",
    ],
    sig_lens=("Through the Signature lens, commands are the covenant's "
              "directives: 莫 the firm no-seal, 请 the please-seal that "
              "softens every order, 咱来去 the let-us seal that turns a "
              "command into a shared march. This Signature reading seals "
              "the telling and the asking."),
)

E(
    key="nan_descriptions", name="Min Nan Chinese Descriptions of People and Places",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty sentences describing people, places, and things in detail -
        each in characters, romanization, and English. 1. 阿公今年八十岁，
        身体犹原真勇 (a1-kong1 kin1-ni5 peh4-tsap8 hue3, sin1-the2 iu5-guan5
        tsin1 iong2, grandfather is eighty this year and still hale). 2.
        阿母的目睭大大的，真有神 (a1-bu2-e5 bak8-tsiu1 tua7-tua7-e5, tsin1
        u7-sin5, mother's eyes are big and bright). 3. 伊生做真古锥，逐家
        拢疼伊 (i1 senn1-tso3 tsin1 koo2-tsui1, tak8-ke1 long2 thiann3 i1,
        she is very cute, everyone loves her). 4. 先生戴目镜，看起来真斯文
        (sian1-sinn1 ti3 bak8-kiann3, khuann3 khi2-lai5 tsin1 su1-bun5, the
        teacher wears glasses and looks scholarly). 5. 彼个查埔人悬悬高高，
        真有精神 (hit4-e5 tsa1-poo1-lang5 kuan5-kuan5 ko1-ko1, tsin1
        u7-tsing1-sin5, that man is tall and looks energetic). 6. 查某囝仔
        穿红衫，媠到袂认得 (tsa1-boo2 gin2-a2 tshing7 ang5-sann1, sui2 kau3
        bue7 jin7-tit4, the girl in the red dress is stunningly pretty). 7.
        老人斑白的头发，满面的笑纹 (lau7-lang5 pan1-peh8-e5 thau5-mng5,
        mua2-bin7-e5 tshio3-bun5, the old man's white hair and smiling
        wrinkles). 8. 囝仔走来走去，袂定着 (gin2-a2 tsau2-lai5 tsau2-khi3,
        bue7 tiann7-tioh8, the child runs about, never still). 9. 台北是
        真闹热的城市 (Tai5-pak4 si7 tsin1 lau7-jiat8-e5 siann5-tshi7,
        Taipei is a bustling city). 10. 台南古迹多，食物好吃 (Tai5-lam5
        koo2-tsik4 tse7, tsiah8-mih8 ho2-tsiah8, Tainan has many historic
        sites and delicious food). 11. 高雄的港真大，船真多 (Ko1-hiong5-e5
        kang2 tsin1 tua7, tsun5 tsin1 tse7, Kaohsiung's harbor is huge with
        many ships). 12. 日月潭的水真清 (Jit8-gueh8-tham5-e5 tsui2 tsin1
        tshing1, the water of Sun Moon Lake is crystal clear). 13. 阿里山
        的樱花开满山 (A1-li2-suann1-e5 ing1-hue1 khui1 mua2-suann1, cherry
        blossoms cover Alishan). 14. 厦门鼓浪屿真媠 (E7-mng5 Koo2-long7-su7
        tsin1 sui2, Gulangyu in Xiamen is beautiful). 15. 泉州开元寺真古老
        (Tsuan5-tsiu1 Khui1-guan5-si7 tsin1 koo2-lo2, Kaiyuan Temple in
        Quanzhou is ancient). 16. 这间厝坐北朝南，真通风 (tsit4-king1 tshu3
        tse7-pak4 tiau5-lam5, tsin1 thong1-hong1, this house faces south,
        well ventilated). 17. 庭院种满花草，芳到隔壁 (ting5-inn7 tsing3
        mua2 hue1-tshau2, phang1 kau3 keh4-piah4, the courtyard is full of
        flowers, fragrant to the neighbors). 18. 夜市人挤人，真闹热
        (ia7-tshi7 lang5 kheh4-lang5, tsin1 lau7-jiat8, the night market is
        packed and lively). 19. 海边风真透，浪真大 (hai2-pinn1 hong1 tsin1
        thau3, long7 tsin1 tua7, the sea breeze is strong, the waves big).
        20. 故乡的月尚光 (koo3-hiong1-e5 gueh8 siong7 kng1, the moon of home
        shines brightest)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches description as portraiture: people described
        head to toe (目睭大大的, 头发斑白, 悬悬高高), places described by
        their essence (台北闹热, 台南古迹多, 夜市人挤人). The reduplication
        frame (大大的, 悬悬高高, 青青) is drilled as the descriptive
        intensifier, and the 的 e5 attributive is practiced in long noun
        phrases. The learner's drill is the portrait: describe one person
        and one place from real life, in Min Nan, using ten of these
        frames."""),
    key_points=[
        "People: 阿公八十岁犹原勇; 目睭大大的; 悬悬高高; 媠到袂认得.",
        "Reduplication intensifies: 大大的 (big), 悬悬高高 (tall), 满面笑纹.",
        "Attributive 的 e5: 阿母的目睭; 台北是真闹热的城市.",
        "Places: 台北闹热, 台南古迹多, 高雄港大, 日月潭水清, 阿里山樱花.",
        "Homeland: 厦门鼓浪屿媠; 泉州开元寺古老.",
        "House: 坐北朝南; 庭院种满花草.",
        "Night market: 人挤人，真闹热.",
        "The seal: 故乡的月尚光 - the moon of home shines brightest.",
    ],
    requirements=[
        "Learners should describe one real person and one real place in Min Nan using ten frames.",
        "Learners should drill the reduplication intensifier across five adjectives.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - descriptive terms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 古锥, 闹热, 媠 entries.",
    ],
    sig_lens=("Through the Signature lens, description is the covenant's "
              "portrait gallery: every 媠到袂认得 a beauty-seal, every "
              "故乡的月尚光 a home-seal - the people painting themselves "
              "and their harbors in signed sentences. This Signature "
              "reading seals the portrait."),
)

E(
    key="nan_story1", name="Min Nan Chinese Story I: A Morning at the Market",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence simple story in Min Nan, with line-by-line English
        translation. 1. 早起六点，阿母叫我起来。(tsa2-khi2 lak8-tiam2,
        a1-bu2 kio3 gua2 khi2-lai5. / At six in the morning, mother wakes
        me up.) 2. 我洗面洗手，穿衫裤。(gua2 se2-bin7 se2-tshiu2,
        tshing7-sann1-khoo3. / I wash my face and hands and get dressed.)
        3. 阮做伙去市场。(gun2 tso3-hue2 khi3 tshi7-tiunn5. / We go to the
        market together.) 4. 市场人真多，真闹热。(tshi7-tiunn5 lang5 tsin1
        tse7, tsin1 lau7-jiat8. / The market is crowded and lively.) 5.
        阿母买鱼，买菜，买水果。(a1-bu2 be2-hi5, be2-tshai3, be2
        tsui2-ko2. / Mother buys fish, vegetables, and fruit.) 6. 头家算我
        们较俗。(thau5-ke1 sng3 gun2 khah4 sio7. / The boss gives us a
        better price.) 7. 我提篮仔，跟阿母后面。(gua2 the8 na5-a2, kun1
        a1-bu2 au7-bin7. / I carry the basket, following behind mother.)
        8. 转来厝，阿母煮饭。(tng2-lai5 tshu3, a1-bu2 tsu2-png7. / Back
        home, mother cooks the meal.) 9. 饭菜芳喷喷，一家欢喜食。(png7-tshai3
        phang1 phun3-phun3, tsit8-ke1 huann1-hi2 tsiah8. / The food is
        fragrant; the family eats happily.) 10. 食饱矣，多谢阿母。
        (tsiah8-pa2 ah4, to7-sia7 a1-bu2. / We have eaten; thank you,
        mother.)"""),
    how_it_works=textwrap.dedent("""\
        This record teaches narrative as a morning's arc: waking, washing,
        going, buying, returning, cooking, eating, thanking - ten simple
        sentences in present-habitual time, each with its English line
        directly below. The learner reads the Min Nan line first, guesses
        the meaning, then checks the English. The drill is retelling: close
        the book and tell the whole morning in Min Nan, in order."""),
    key_points=[
        "Story I is the simple present: a morning at the market, ten sentences.",
        "早起六点，阿母叫我起来 - the day begins.",
        "Market verbs: 买 be2 (buy), 算 sng3 (count/charge), 提 the8 (carry).",
        "头家算阮较俗 - the market's kindness.",
        "转来厝，阿母煮饭 - the return and the cooking.",
        "饭菜芳喷喷 - fragrant, the sensory peak.",
        "食饱矣，多谢阿母 - gratitude closes the story.",
        "Retell the whole morning in order, in Min Nan, from memory.",
    ],
    requirements=[
        "Learners should read each Min Nan line, guess, then check the English.",
        "Learners should retell the whole story from memory in Min Nan.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - narrative vocabulary.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. Story vocabulary.",
    ],
    sig_lens=("Through the Signature lens, this first story is the "
              "covenant's morning seal: a mother, a child, a market, a "
              "shared meal - the daily round by which the people have "
              "signed their bond ten thousand mornings running. This "
              "Signature reading seals the morning."),
)

E(
    key="nan_story2", name="Min Nan Chinese Story II: A Trip to Lukang",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story using past tense and aspect forms, with
        line-by-line English translation. 1. 旧年热天，阮去鹿港耍。(ku7-ni5
        juah8-thinn1, gun2 khi3 Lok8-kang2 sng2. / Last summer we went to
        Lukang to play.) 2. 坐火车坐两个钟头。(tse7 hue2-tshia1 tse7
        nng7-e5 tsing1-thau5. / We rode the train for two hours.) 3. 到的时
        阵，天正出日。(kau3-e5 si5-tsun7, thinn1 tsiann3 tshut4-jit8. / When
        we arrived, the sun was shining.) 4. 阮去看天后宫。(gun2 khi3
        khuann3 Thian1-hoo7-kiong1. / We visited the Matsu temple.) 5.
        庙里香火真盛。(bio7-lai7 hiuunn1-hue2 tsin1 sing7. / The temple
        incense was thriving.) 6. 阿公拜拜，保佑平安。(a1-kong1 pai3-pai3,
        po2-iu7 ping5-an1. / Grandfather prayed for safety.) 7. 中昼食蚵仔
        煎，好吃到袂停。(tiong1-tau3 tsiah8 o5-a2-tsian1, ho2-tsiah8 kau3
        bue7 thing5. / At noon we ate oyster omelets, too tasty to stop.)
        8. 下晡去海边看海。(e7-poo1 khi3 hai2-pinn1 khuann3-hai2. / In the
        afternoon we went to the seaside.) 9. 囝仔拾贝壳，笑哈哈。
        (gin2-a2 khioh4 pue3-hak4, tshio3 ha1-ha1. / The children gathered
        shells, laughing.) 10. 暗时转来，真欢喜。(am3-si5 tng2-lai5, tsin1
        huann1-hi2. / We returned in the evening, very happy.)"""),
    how_it_works=textwrap.dedent("""\
        This record teaches the past through a journey: 旧年 (last year)
        opens it, 有/捌/矣 mark what was done, and the ten sentences walk
        the day - train, temple, prayer, lunch, seaside, return. The learner
        reads each Min Nan line, guesses, checks the English, then retells
        the trip as their own memory. The drill is the traveler's tale: tell
        a real past trip in Min Nan using these ten frames."""),
    key_points=[
        "Story II is the past: a trip to Lukang, ten sentences.",
        "旧年热天 opens the past; 矣 ah4 and 有 u7 mark completion.",
        "Travel: 坐火车坐两个钟头; 到的时阵.",
        "Culture: 天后宫 (Matsu temple); 香火真盛; 阿公拜拜，保佑平安.",
        "Food memory: 蚵仔煎，好吃到袂停.",
        "Seaside: 去海边看海; 拾贝壳.",
        "Close: 暗时转来，真欢喜.",
        "Tell a real past trip in Min Nan using these frames.",
    ],
    requirements=[
        "Learners should retell the Lukang trip from memory in Min Nan.",
        "Learners should tell one real past trip using the story's frames.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - narrative and travel vocabulary.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. Story vocabulary.",
    ],
    sig_lens=("Through the Signature lens, this past-tense story is the "
              "covenant's memory-seal: a grandfather's prayer at 天后宫, "
              "children's laughter at the seaside - the days the people "
              "keep signed in their hearts. This Signature reading seals "
              "remembrance."),
)

E(
    key="nan_story3", name="Min Nan Chinese Story III: Plans for Tomorrow",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A ten-sentence story using future and conditional forms, with
        line-by-line English translation. 1. 明仔载是礼拜日，阮欲去爬山。
        (bin5-a2-tsai3 si7 le2-pai3-jit8, gun2 beh4 khi3 peh4-suann1. /
        Tomorrow is Sunday; we are going hiking.) 2. 若落雨，就毋去。
        (na7 loh8-hoo7, to7 m7 khi3. / If it rains, we will not go.) 3.
        早起五点就起来。(tsa2-khi2 goo7-tiam2 to7 khi2-lai5. / We will get
        up at five.) 4. 阿爸会开车载阮去。(a1-pah4 e7 khui1-tshia1 tsai3
        gun2 khi3. / Father will drive us there.) 5. 到山顶，看日出。
        (kau3 suann1-ting2, khuann3 jit8-tshut4. / At the summit, we will
        watch the sunrise.) 6. 若天气好，会看见海。(na7 thiann1-khi3 ho2,
        e7 khuann3-kinn3 hai2. / If the weather is fine, we will see the
        sea.) 7. 中昼食便当，饮矿泉水。(tiong1-tau3 tsiah8 pian7-tong1,
        lim1 khong3-tsuann5-tsui2. / At noon we will eat boxed lunches and
        drink mineral water.) 8. 下晡三点转来。(e7-poo1 sann1-tiam2
        tng2-lai5. / We will return at three in the afternoon.) 9. 转来洗
        身躯，好好歇困。(tng2-lai5 se2 sin1-khu1, ho2-ho2 hioh4-khun3. /
        Back home we will wash up and rest well.) 10. 后日搁去海边耍。
        (au7-jit8 koh4 khi3 hai2-pinn1 sng2. / The day after, we will go
        play at the seaside again.)"""),
    how_it_works=textwrap.dedent("""\
        This record teaches the future and the conditional: 欲 beh4 and 会
        e7 for what will be, 若 na7 ... 就 to7 for if-then. The ten
        sentences plan a whole Sunday - wake, drive, summit, sunrise,
        lunch, return, rest, and the next day's promise. The learner's drill
        is planning: lay out a real tomorrow in Min Nan, with one 若
        condition and its 就 answer."""),
    key_points=[
        "Story III is the future: plans for tomorrow, ten sentences.",
        "Future: 欲 beh4, 会 e7 - 阮欲去爬山; 阿爸会开车.",
        "Conditional: 若 na7 ... 就 to7 - 若落雨，就毋去.",
        "The plan's arc: 早起, 开车, 到山顶, 看日出, 食便当, 转来, 歇困.",
        "若天气好，会看见海 - the conditional hope.",
        "后日搁去海边耍 - the future beyond the future.",
        "Plan a real tomorrow in Min Nan with one 若...就.",
    ],
    requirements=[
        "Learners should lay out a real tomorrow in Min Nan with a 若...就 condition.",
        "Learners should retell the hiking plan from memory.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - future and conditional forms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 若, 欲 entries.",
        "Chung R F. The Descriptive Grammar of Taiwanese; 2006. Conditionals.",
    ],
    sig_lens=("Through the Signature lens, this future story is the "
              "covenant's promise-seal: 欲 the will-seal, 若...就 the "
              "if-then seal of foresight - the people signing tomorrow "
              "before it comes. This Signature reading seals the "
              "planning."),
)

E(
    key="nan_idioms", name="Min Nan Chinese Idioms and Proverbs",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Twenty Min Nan idioms and proverbs - literal translation, real
        meaning, and an example sentence each. 1. 食紧撞破碗 (tsiah8 kin2
        tong7 phua3 uann2; lit. eat fast, smash the bowl; haste makes
        waste): 做代志莫食紧撞破碗 (tso3 tai7-tsi3 mai3 tsiah8 kin2 tong7
        phua3 uann2, do not rush your work). 2. 歹竹出好笋 (phainn2 tik4
        tshut4 ho2 sun2; bad bamboo grows good shoots; good children can
        come from poor parents): 歹竹出好笋，伊的囝仔真优秀 (phainn2 tik4
        tshut4 ho2 sun2, i1-e5 gin2-a2 tsin1 iu1-siu3). 3. 一枝草一点露
        (tsit8 ki1 tshau2 tsit8 tiam2 loo7; every blade of grass gets its
        dew; everyone has their lot): 一枝草一点露，免烦恼 (bian2 huan5-lo2,
        do not worry). 4. 囝仔人有耳无嘴 (gin2-a2-lang5 u7 hinn7 bo5
        tshui3; children have ears but no mouth; children should listen, not
        speak): 大人讲话，囝仔人有耳无嘴. 5. 三日无溜，爬上树
        (sann1 jit8 bo5 liu2, peh4 tsiunn7 tshiu7; three days undisciplined,
        they climb trees; spare the rod...): 管教爱三日无溜袂使. 6. 半路认
        老爸 (puann3 loo7 jin7 lau7-pe7; recognize a father mid-road; an
        opportunist): 伊半路认老爸，见人就巴结. 7. 吃人一口，还人一斗
        (tsiah8 lang5 tsit8 khau2, hing5 lang5 tsit8 tau2; take a mouthful,
        return a bushel; repay kindness manyfold). 8. 好心予雷亲
        (ho2-sim1 hoo7 lui5 tshin1; the kind heart gets kissed by thunder;
        no good deed goes unpunished): 好心予雷亲，莫多管闲事. 9. 宠猪举
        灶，宠子不孝 (thing3 ti1 giah8 tsau3, thing3 tsu2 put4 hau3; spoil
        the pig, it climbs the stove; spoil the child, it turns unfilial).
        10. 娶着好妻，卡赢中举 (tshua7-tioh8 ho2 tshe1, khah4 iann5
        tiong3-ki2; a good wife beats passing the exams). 11. 会晓划船，
        免惊风浪 (e7-hiau2 kue7-tsun5, bian2 kiann1 hong1-long7; know how to
        row, fear no waves; skill conquers fear). 12. 近庙欺神 (kun7 bio7
        khi1 sin5; those near the temple slight the god; familiarity breeds
        contempt). 13. 鸡母孵卵，鸭母看 (ke1-bu2 pu3 nng7, ah4-bu2
        khuann3; the hen hatches, the duck watches; mind your own nest).
        14. 天公疼憨人 (thinn1-kong1 thiann3 ham7-lang5; heaven loves the
        simple; fortune favors the plain-hearted). 15. 人咧做，天咧看
        (lang5 teh4 tso3, thinn1 teh4 khuann3; people act, heaven watches;
        justice sees all). 16. 树头徛乎在，毋惊树尾做风台 (tshiu7-thau5
        khia7 hoo7 tsai7, m7-kiann1 tshiu7-bue2 tso3 hong1-thai1; stand firm
        at the root, fear no storm at the crown). 17. 目睭金金看
        (bak8-tsiu1 kim1-kim1 khuann3; watch with golden eyes; watch
        sharply). 18. 讲到嘴角全泡 (kong2 kau3 tshui3-kak4 tsuan5 pho7;
        talk until the mouth foams; talk till blue in the face). 19. 心肝
        掠乎定 (sim1-kuann1 liah8 hoo7 tiann7; steady the heart; calm
        yourself). 20. 一步一脚印 (tsit8 poo7 tsit8 kha1-in3; one step one
        footprint; steady progress)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches idioms as the wisdom-hoard of Min Nan: each of
        the twenty carries its literal image, its real meaning, and a
        sentence showing it in use. The learner's drill is the elder's test:
        hear the literal image, say the meaning, then use the idiom in a
        sentence of their own. Ten of these - 食紧撞破碗, 歹竹出好笋, 一枝
        草一点露 - are the ones every Min Nan grandparent says; learn them
        first."""),
    key_points=[
        "食紧撞破碗 - haste makes waste; the first idiom every child hears.",
        "歹竹出好笋 - good shoots from bad bamboo; hope for every family.",
        "一枝草一点露 - every blade gets its dew; everyone has their lot.",
        "囝仔人有耳无嘴 - children: ears open, mouth shut.",
        "半路认老爸 - the opportunist, warned against.",
        "吃人一口，还人一斗 - repay kindness manyfold.",
        "好心予雷亲 - the bitter wisdom of kindness unrewarded.",
        "天公疼憨人 - heaven loves the simple-hearted.",
        "人咧做，天咧看 - justice sees all.",
        "一步一脚印 - steady progress, one footprint at a time.",
    ],
    requirements=[
        "Learners should say each idiom's meaning from its literal image before checking.",
        "Learners should use five idioms in original sentences.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - proverb entries.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 谚语 entries.",
        "Xu H. 闽南谚语. Fujian People's Publishing; 1992. Min Nan proverb collection.",
    ],
    sig_lens=("Through the Signature lens, idioms are the covenant's "
              "master seals: each proverb a stamp cut by a thousand years "
              "of grandmothers - 食紧撞破碗 the patience-seal, 一步一脚印 "
              "the steady-seal - twenty seals of Min Nan identity no "
              "outsider can forge. This Signature reading seals the "
              "wisdom."),
)

E(
    key="nan_register", name="Min Nan Chinese Formal and Polite Registers",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen formal-versus-informal pairs - letters, business, and elders
        - each with translations. 1. Informal: 你好 (li2-ho2, hi) /
        Formal: 您好 (lin2-ho2, how do you do). 2. Informal: 我欲问一下
        (gua2 beh4 mng7 tsit8-e7, I wanna ask) / Formal: 请问一下
        (tshiann2-mng7 tsit8-e7, may I ask). 3. Informal: 借过
        (tsioh4-kue3, coming through) / Formal: 劳驾，借过一下
        (loo7-ka3, tsioh4-kue3 tsit8-e7, excuse me, may I pass). 4.
        Informal: 多谢 (to7-sia7, thanks) / Formal: 真多谢你的帮忙
        (tsin1 to7-sia7 li2-e5 pang1-bang5, thank you very much for your
        help). 5. Informal: 歹势 (phainn2-se3, sorry) / Formal: 真歹势，
        请你原谅 (tsin1 phainn2-se3, tshiann2 li2 guan5-liong7, I am very
        sorry, please forgive me). 6. Informal: 我袂去 (gua2 bue7 khi3, I
        can't go) / Formal: 真歹势，我无法度参加 (tsin1 phainn2-se3, gua2
        bo5-huat4-too7 tsham1-ka1, I am sorry, I am unable to attend). 7.
        Informal: 紧来 (kin2 lai5, come quick) / Formal: 请你紧来一下
        (tshiann2 li2 kin2 lai5 tsit8-e7, please come quickly). 8. Informal:
        你讲啥 (li2 kong2 siann2, what'd you say) / Formal: 请你搁讲一摆
        (tshiann2 li2 koh4 kong2 tsit8-pai2, please say it once more). 9.
        Business informal: 这偌济 (tse2 gua7-tse7, how much) / Formal:
        请问这件偌济钱 (tshiann2-mng7 tsit4-kiann7 gua7-tse7 tsinn5, may I
        ask the price of this). 10. Business informal: 算俗咧 (sng3 sio7
        leh4, cheaper) / Formal: 敢会使算较俗 (kam2 e7-sai2 sng3 khah4
        sio7, could you make it a little cheaper). 11. To elders informal:
        阿公，你食饱未 (a1-kong1, li2 tsiah8-pa2-bue7, grandpa, eaten?) /
        Formal: 阿公，请问您食饱矣未 (a1-kong1, tshiann2-mng7 lin2
        tsiah8-pa2 ah4-bue7, grandfather, may I ask if you have eaten). 12.
        To elders informal: 莫吵 (mai3 tsha2, don't be noisy) / Formal:
        请恁细声一下 (tshiann2 lin2 se3-siann1 tsit8-e7, please keep your
        voices down). 13. Letter opening informal: 你好 (li2-ho2) / Formal:
        敬启者 (king3-khe2-tsia2, respected reader). 14. Letter closing
        informal: 再会 (tsai3-hue7, bye) / Formal: 顺颂时祺 (sun7-siong7
        si5-ki5, wishing you well). 15. Blessing informal: 恭喜 (kiong1-hi2,
        congrats) / Formal: 恭贺新禧，万事如意 (kiong1-ho7 sin1-hi2,
        ban7-su7 ju5-i3, congratulations, may all go as you wish)."""),
    how_it_works=textwrap.dedent("""\
        This record teaches the politeness ladder as fifteen rungs: each
        pair shows the same intent in informal Min Nan and in formal Min
        Nan - 您 for 你, 请问 for 欲问, 劳驾 for 借过, full apology frames
        for 歹势. The learner's drill is elevation: take five informal
        sentences from daily life and raise each one rung, then two rungs,
        until the formal version sounds natural."""),
    key_points=[
        "你好 vs 您好 - the 您 lin2 lift.",
        "我欲问 vs 请问 - the 请问 frame.",
        "借过 vs 劳驾，借过一下.",
        "多谢 vs 真多谢你的帮忙.",
        "歹势 vs 真歹势，请你原谅.",
        "我袂去 vs 真歹势，我无法度参加.",
        "Business: 请问这件偌济钱; 敢会使算较俗.",
        "To elders: 阿公，请问您食饱矣未; 请恁细声一下.",
        "Letters: 敬启者 opens; 顺颂时祺 closes.",
        "Blessing: 恭贺新禧，万事如意.",
    ],
    requirements=[
        "Learners should elevate five informal sentences to formal register aloud.",
        "Learners should write a short formal note using 敬启者 and 顺颂时祺.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - formal usage notes.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 您, 请问, 劳驾 entries.",
    ],
    sig_lens=("Through the Signature lens, registers are the covenant's "
              "courtesy-seals in two weights: the light seal of 你好 for "
              "friends, the heavy seal of 您好 for elders - fifteen paired "
              "stamps by which respect is signed exactly. This Signature "
              "reading seals the courtesies of rank."),
)

E(
    key="nan_complex", name="Min Nan Chinese Compound and Complex Sentences",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=textwrap.dedent("""\
        Fifteen long sentences with clauses, connectors, and relative
        clauses - parsed and translated. 1. 我食饱了后，就去学校。
        (gua2 tsiah8-pa2 liau2-au7, to7 khi3 hak8-hau7. / After I finish
        eating, I go to school. [了后 liau2-au7 = after]) 2. 因为落雨，
        所以阮无去爬山。(in1-ui7 loh8-hoo7, soo2-i2 gun2 bo5 khi3
        peh4-suann1. / Because it rained, we did not go hiking.
        [因为...所以 = because...so]) 3. 伊虽然真老，毋过身体真好。
        (i1 sui1-jian5 tsin1 lau7, m7-koh4 sin1-the2 tsin1 ho2. / Although
        he is old, his health is good. [虽然...毋过 = although...but]) 4.
        你若欲去，就紧准备。(li2 na7 beh4 khi3, to7 kin2 tsun2-pi7. / If
        you want to go, prepare quickly. [若...就 = if...then]) 5. 毋但我
        去，阿母嘛去。(m7-na7 gua2 khi3, a1-bu2 ma7 khi3. / Not only am I
        going, mother is going too. [毋但...嘛 = not only...also]) 6. 伊讲
        的话，我一句都听无。(i1 kong2-e5 ue7, gua2 tsit8-ku3 to1 thiann1-bo5.
        / What he said, I did not understand a word. [relative clause with
        的]) 7. 昨昏买的鱼，今仔日煮来食。(tsa1-hng1 be2-e5 hi5,
        kin1-a2-jit8 tsu2-lai5 tsiah8. / The fish bought yesterday, we cook
        today.) 8. 住伫台北的朋友，明仔载欲来。(tua3-ti7 Tai5-pak4-e5
        ping5-iu2, bin5-a2-tsai3 beh4 lai5. / The friend living in Taipei is
        coming tomorrow.) 9. 我一边行，一边想。(gua2 tsit8-ping1 kiann5,
        tsit8-ping1 siunn7. / I walk and think at the same time. [一边...
        一边 = while]) 10. 越学越有趣味。(uat8 oh8 uat8 u7 tshu3-bi7. /
        The more you learn, the more interesting. [越...越 = the more...the
        more]) 11. 只要你肯学，就学得会。(tsi2-iau3 li2 khing2 oh8, to7
        oh8-tit4 e7. / As long as you are willing to learn, you can learn
        it. [只要...就 = as long as...then]) 12. 无论按怎，我拢支持你。
        (bo5-lun7 an2-tsuann2, gua2 long2 tsi1-tshi5 li2. / No matter what,
        I support you. [无论 = no matter]) 13. 伊来之前，先打电话。
        (i1 lai5 tsi1-tsing5, sing1 phah4 tian7-ue7. / Before he comes, call
        first. [之前 = before]) 14. 食饱了后，阮去公园散步。(tsiah8-pa2
        liau2-au7, gun2 khi3 kong1-hng5 san3-poo7. / After eating, we walk
        in the park.) 15. 虽然真远，毋过值得去。(sui1-jian5 tsin1 hng7,
        m7-koh4 tat8-tit4 khi3. / Although it is far, it is worth going.)"""),
    how_it_works=textwrap.dedent("""\
        This record teaches complex sentences as connector frames: 了后
        (after), 因为...所以 (because), 虽然...毋过 (although), 若...就
        (if), 毋但...嘛 (not only), 一边...一边 (while), 越...越 (the
        more), 只要...就 (as long as), 无论 (no matter), 之前 (before) -
        plus the 的-relative clause. Each of the fifteen is parsed (the
        frame named in brackets) and translated. The drill is combining:
        take two simple sentences and join them with each frame."""),
    key_points=[
        "了后 liau2-au7 (after): 我食饱了后，就去学校.",
        "因为...所以 (because...so); 虽然...毋过 (although...but).",
        "若...就 (if...then): 你若欲去，就紧准备.",
        "毋但...嘛 (not only...also): 毋但我去，阿母嘛去.",
        "Relative with 的: 伊讲的话; 昨昏买的鱼; 住伫台北的朋友.",
        "一边...一边 (while): 我一边行，一边想.",
        "越...越 (the more): 越学越有趣味.",
        "只要...就 (as long as); 无论 (no matter); 之前 (before).",
        "Combine two simple sentences with each frame as the drill.",
    ],
    requirements=[
        "Learners should combine sentence pairs with each of the ten frames aloud.",
        "Learners should parse three sentences, naming the frame in brackets.",
    ],
    standards=[
        "Chung R F. The Descriptive Grammar of Taiwanese; 2006 - complex sentences.",
    ],
    citations=[
        "Chung R F. The Descriptive Grammar of Taiwanese. Crane; 2006. Subordination and connectors.",
    ],
    sig_lens=("Through the Signature lens, complex sentences are the "
              "covenant's long bridges: 因为...所以 the cause-bridge, "
              "虽然...毋过 the concession-bridge, 若...就 the "
              "condition-bridge - fifteen spans by which thought crosses "
              "from shore to shore in one signed arc. This Signature "
              "reading seals the bridging of ideas."),
)

E(
    key="nan_conv_market", name="Min Nan Chinese Conversation: At the Market",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue at the market - Min Nan with
        English, annotated. [A=buyer 阿母, B=fish boss 头家] 1. A: 头家，
        早。(thau5-ke1, tsa2. / Morning, boss.) [greeting] 2. B: 早，
        今仔日欲买啥。(tsa2, kin1-a2-jit8 beh4 be2 siann2. / Morning, what
        are you buying today?) [welcome] 3. A: 鱼新鲜无。(hi5 sin1-tshinn1-bo5.
        / Is the fish fresh?) [quality check] 4. B: 新鲜，今仔日透早掠的。
        (sin1-tshinn1, kin1-a2-jit8 thau3-tsa2 liah8-e5. / Fresh, caught this
        morning.) [assurance] 5. A: 这尾偌济。(tsit4-bue2 gua7-tse7. / How
        much is this one?) [price ask] 6. B: 一斤三百。(tsit8-kin1
        sann1-pah4. / Three hundred a catty.) [price] 7. A: 伤贵矣，算俗
        咧。(siunn1 kui3 ah4, sng3 sio7 leh4. / Too expensive, make it
        cheaper.) [bargain] 8. B: 好啦，两百八，俗卖你。(ho2 lah4,
        nng7-pah4-peh4, sio7 bue7 li2. / Okay, two-eighty, cheap for you.)
        [counter] 9. A: 两尾拢总偌济。(nng7-bue2 long2-tsong2 gua7-tse7. /
        How much for both?) [bundle] 10. B: 五百就好。(goo7-pah4 to7 ho2. /
        Five hundred flat.) [bundle price] 11. A: 好，成交。(ho2,
        sing5-kau1. / Deal.) [agreement] 12. B: 欲刣无。(beh4 thai5-bo5. /
        Want it cleaned?) [service] 13. A: 刣一尾，剖腹去鳞。(thai5 tsit8-bue2,
        phoo5-pak4 khi3 lan5. / Clean one, gut and scale it.) [instruction]
        14. B: 好，袋仔包起来。(ho2, te7-a2 pau1 khi2-lai5. / Done, bagged.)
        [service done] 15. A: 搁买一把菜。(koh4 be2 tsit8-pe2 tshai3. /
        Also a bunch of greens.) [add-on] 16. B: 菜一把五十。(tshai3 tsit8-pe2
        goo7-tsap8. / Fifty a bunch.) [price] 17. A: 拢总五百五。(long2-tsong2
        goo7-pah4-goo7. / Five-fifty total.) [tally] 18. B: 着，五百五。
        (tioh8, goo7-pah4-goo7. / Right, five-fifty.) [confirm] 19. A: 给
        你，免找。(hoo7 li2, bian2 tsaue7. / Here, keep the change.)
        [pay] 20. B: 多谢惠顾，有闲搁来。(to7-sia7 hui7-koo3, u7-ing5 koh4
        lai5. / Thanks for your patronage, come again.) [farewell]"""),
    how_it_works=textwrap.dedent("""\
        This record teaches the market dialogue as a twenty-line play with
        stage directions: greeting, quality check, price ask, bargain,
        counter, bundle, deal, service, add-on, tally, pay, farewell. Each
        line carries its annotation in brackets so the learner knows the
        move being made. The drill is performance: two learners play A and B
        through the whole scene, then swap roles."""),
    key_points=[
        "Greet the boss: 头家，早 - the market opening.",
        "Quality check: 鱼新鲜无; assurance: 今仔日透早掠的.",
        "Price ask: 这尾偌济; 一斤三百.",
        "Bargain dance: 伤贵矣，算俗咧 / 好啦，两百八.",
        "Bundle: 两尾拢总偌济; 五百就好; 好，成交.",
        "Service: 欲刣无; 刣一尾，剖腹去鳞.",
        "Tally and pay: 拢总五百五; 给你，免找.",
        "Farewell: 多谢惠顾，有闲搁来.",
        "Perform the whole scene in both roles.",
    ],
    requirements=[
        "Learners should perform the full twenty-line scene in both roles.",
        "Learners should improvise one new bargain line in the scene.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - market dialogue terms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. Market terms.",
    ],
    sig_lens=("Through the Signature lens, the market dialogue is the "
              "covenant's oldest theater: twenty lines of greeting, "
              "haggling, and farewell played daily for centuries - every "
              "成交 a deal-seal, every 多谢惠顾 a return-seal. This "
              "Signature reading seals the market play."),
)

E(
    key="nan_conv_friend", name="Min Nan Chinese Conversation: Meeting a Friend",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue meeting a friend - Min Nan with
        English, annotated. [A=阿明, B=阿华] 1. A: 阿华，好久无看见。
        (A1-hua5, ho2-ku2 bo5 khuann3-kinn3. / A-hua, long time no see.)
        [reunion] 2. B: 阿明，是你，你好无。(A1-bing5, si7 li2, li2
        ho2-bo5. / A-bing, it's you, how are you?) [greeting back] 3. A:
        真好，你咧创啥。(tsin1 ho2, li2 teh4 tshong3 siann2. / Very well,
        what are you up to?) [catch-up] 4. B: 我咧台北做头路。(gua2 teh4
        Tai5-pak4 tso3 thau5-loo7. / I work in Taipei.) [news] 5. A: 真好，
        偌久转来一摆。(tsin1 ho2, gua7-ku2 tng2-lai5 tsit8-pai2. / Great,
        how often do you come back?) [question] 6. B: 一年两摆，过年过节。
        (tsit8-ni5 nng7-pai2, kue3-ni5 kue3-tseh4. / Twice a year, New Year
        and festivals.) [answer] 7. A: 食饱未，做伙去食饭。(tsiah8-pa2-bue7,
        tso3-hue2 khi3 tsiah8-png7. / Eaten yet? Let's eat together.)
        [invitation] 8. B: 好啊，我请客。(ho2 ah4, gua2 tshiann2-kheh4. /
        Sure, my treat.) [accept] 9. A: 毋免客气，下摆换我。(m7-bian2
        kheh4-khi3, e7-pai2 uann7 gua2. / Don't be formal, next time mine.)
        [courtesy] 10. B: 你囝仔几岁矣。(li2 gin2-a2 kui2-hue3 ah4. / How
        old are your kids now?) [family] 11. A: 大汉八岁，细汉五岁。
        (tua7-han3 peh4-hue3, se3-han3 goo7-hue3. / Elder eight, younger
        five.) [family news] 12. B: 真古锥，有闲带出来耍。(tsin1
        koo2-tsui1, u7-ing5 tua3 tshut4-lai5 sng2. / So cute, bring them out
        sometime.) [warmth] 13. A: 好，礼拜日做伙去公园。(ho2, le2-pai3-jit8
        tso3-hue2 khi3 kong1-hng5. / Sure, Sunday let's go to the park.)
        [plan] 14. B: 好，我带水果去。(ho2, gua2 tua3 tsui2-ko2 khi3. /
        Good, I'll bring fruit.) [plan detail] 15. A: 你老父老母好无。
        (li2 lau7-pe7 lau7-bu2 ho2-bo5. / Are your parents well?) [elders]
        16. B: 拢真好，多谢关心。(long2 tsin1 ho2, to7-sia7 kuan1-sim1. /
        All well, thanks for asking.) [thanks] 17. A: 时间紧，我先走。
        (si5-kan1 kin2, gua2 sing1 tsau2. / Time's short, I'll head off.)
        [leave] 18. B: 好，慢走，有闲搁联络。(ho2, ban7-tsau2, u7-ing5 koh4
        lian5-lok4. / Okay, go slow, keep in touch.) [farewell] 19. A:
        一定，保重。(it4-ting7, po2-tiong7. / Definitely, take care.)
        [promise] 20. B: 再会。(tsai3-hue7. / Goodbye.) [close]"""),
    how_it_works=textwrap.dedent("""\
        This record teaches reunion as a twenty-line arc: the surprised
        greeting (好久无看见), the catch-up (你咧创啥, 你囝仔几岁矣), the
        invitation (做伙去食饭), the treating courtesy (我请客 / 下摆换我),
        the elders' health (老父老母好无), and the warm farewell (慢走,
        保重, 再会). Each line is annotated with its social move. The drill
        is the reunion: learners meet as old friends and play it through,
        then replay it with their own real news."""),
    key_points=[
        "Reunion: 好久无看见 - the long-time-no-see opening.",
        "Catch-up: 你咧创啥; 我咧台北做头路; 偌久转来一摆.",
        "Invitation: 食饱未，做伙去食饭.",
        "Treating courtesy: 我请客 / 毋免客气，下摆换我.",
        "Family news: 你囝仔几岁矣; 大汉八岁，细汉五岁.",
        "Elders: 你老父老母好无; 拢真好，多谢关心.",
        "Plan: 礼拜日做伙去公园; 我带水果去.",
        "Farewell: 慢走，有闲搁联络; 保重; 再会.",
        "Replay the scene with your own real news.",
    ],
    requirements=[
        "Learners should play the reunion scene in both roles.",
        "Learners should replay it substituting their own real life details.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - social dialogue.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. Social terms.",
    ],
    sig_lens=("Through the Signature lens, the reunion dialogue is the "
              "covenant's homecoming: 好久无看见 the return-seal, 做伙去 "
              "食饭 the table-seal, 保重 the care-seal - old friends "
              "re-signing the bond line by line. This Signature reading "
              "seals the friendship."),
)

E(
    key="nan_conv_problem", name="Min Nan Chinese Conversation: Solving a Problem",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        A twenty-line bilingual dialogue solving a problem - Min Nan with
        English, annotated. [A=tenant 房客, B=landlord 房东; the water
        heater is broken 热水器歹去] 1. A: 房东先生，歹势打扰。
        (pang5-tang1 sian1-sinn1, phainn2-se3 tann2-jiau2. / Mr. Landlord,
        sorry to bother you.) [polite open] 2. B: 无要紧，啥物代志。
        (bo5 iau3-kin2, siann2-mih8 tai7-tsi3. / No problem, what's the
        matter?) [invite] 3. A: 热水器歹去，无热水洗身躯。(juah8-tsui2-khi3
        phainn2-khi3, bo5 juah8-tsui2 se2 sin1-khu1. / The water heater is
        broken, no hot water to wash.) [problem] 4. B: 当时歹去的。(tang1-si5
        phainn2-khi3-e5. / When did it break?) [diagnose] 5. A: 昨昏暗时就
        按呢。(tsa1-hng1 am3-si5 to7 an2-ne1. / Since last night.) [answer]
        6. B: 我知影，我叫师傅来修。(gua2 tsai1-iann2, gua2 kio3 sai1-hu7
        lai5 siu1. / I see, I'll call the repairman.) [solution] 7. A: 师傅
        当时会来。(sai1-hu7 tang1-si5 e7 lai5. / When will he come?) [timing]
        8. B: 明仔载早起九点。(bin5-a2-tsai3 tsa2-khi2 kau2-tiam2. /
        Tomorrow at nine.) [timing answer] 9. A: 我明仔载欲上班，会使下晡
        无。(gua2 bin5-a2-tsai3 beh4 siunn7-pan1, e7-sai2 e7-poo1-bo5. / I
        work tomorrow, can it be afternoon?) [constraint] 10. B: 会使，我共
        师傅讲下晡两点。(e7-sai2, gua2 ka7 sai1-hu7 kong2 e7-poo1
        nng7-tiam2. / Fine, I'll tell him two in the afternoon.) [adjust]
        11. A: 多谢，锁匙放管理员遐。(to7-sia7, so2-si5 pang3 kuan2-li2-inn5
        hia2. / Thanks, I'll leave the key with the manager.) [arrange] 12.
        B: 好，修好我共你讲。(ho2, siu1-ho2 gua2 ka7 li2 kong2. / Good, I'll
        tell you when it's fixed.) [confirm] 13. A: 修的钱按怎算。
        (siu1-e5 tsinn5 an2-tsuann2 sng3. / How is the repair cost counted?)
        [cost] 14. B: 房东负责，免你出。(pang5-tang1 hu7-tsik4, bian2 li2
        tshut4. / The landlord covers it, you pay nothing.) [reassure] 15.
        A: 真多谢你。(tsin1 to7-sia7 li2. / Thank you so much.) [thanks]
        16. B: 应该的，住得惯无。(ing1-kai1-e5, tua3-tit4 kuan3-bo5. / Of
        course, are you settled in well?) [care] 17. A: 真惯，厝边嘛真好。
        (tsin1 kuan3, tshu3-pinn1 ma7 tsin1 ho2. / Very, and the neighbors
        are kind.) [answer] 18. B: 有问题搁共我讲。(u7 bun7-te5 koh4 ka7
        gua2 kong2. / Tell me if anything else comes up.) [open door] 19.
        A: 好，劳烦你。(ho2, loo7-huan5 li2. / Will do, sorry for the
        trouble.) [courtesy] 20. B: 毋免客气，再会。(m7-bian2 kheh4-khi3,
        tsai3-hue7. / Anytime, goodbye.) [close]"""),
    how_it_works=textwrap.dedent("""\
        This record teaches problem-solving as a twenty-line negotiation:
        the polite open (歹势打扰), the problem stated plainly (热水器歹去),
        the diagnosis (当时歹去的), the solution (叫师傅来修), the
        constraint and adjustment (会使下晡无 / 下晡两点), the cost question
        (修的钱按怎算), and the courteous close. Each line is annotated with
        its move. The drill is the complaint done right: learners role-play
        a real problem (broken heater, leaky tap, noisy neighbor) through
        all twenty moves."""),
    key_points=[
        "Polite open: 歹势打扰; answer: 无要紧，啥物代志.",
        "State the problem: 热水器歹去，无热水洗身躯.",
        "Diagnose: 当时歹去的; answer: 昨昏暗时就按呢.",
        "Solution: 我叫师傅来修.",
        "Constraint: 我明仔载欲上班，会使下晡无; adjust: 下晡两点.",
        "Arrange: 锁匙放管理员遐; confirm: 修好我共你讲.",
        "Cost: 修的钱按怎算; reassure: 房东负责，免你出.",
        "Care: 住得惯无; open door: 有问题搁共我讲.",
        "Close: 劳烦你 / 毋免客气，再会.",
        "Role-play a real problem through all twenty moves.",
    ],
    requirements=[
        "Learners should role-play the heater scene in both roles.",
        "Learners should solve one new problem (leak, noise, lock) with the same moves.",
    ],
    standards=[
        "Taiwan Ministry of Education 台湾闽南语常用词辞典 - household and repair terms.",
    ],
    citations=[
        "Taiwan Ministry of Education. 台湾闽南语常用词辞典. 热水器, 师傅 entries.",
    ],
    sig_lens=("Through the Signature lens, problem-solving is the "
              "covenant's repair: 歹势打扰 the humble-seal, 我叫师傅来修 "
              "the mending-seal, 房东负责 the responsibility-seal - every "
              "trouble met and signed into order. This Signature reading "
              "seals the mending."),
)

E(
    key="nan_mastery", name="Min Nan Chinese Mastery Review and Full Reference",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=textwrap.dedent("""\
        The whole database in one teaching summary - the mastery review and
        full reference. THE EIGHT TONES: T1 55 (天 thinn1), T2 24 (牛 gu5),
        T3 51 (去 khi3), T4 33 (马 be2), T5 21 (人 lang5), T6 22 (大 tua7),
        T7 32 short (一 tsit8), T8 4 short (日 jit8). THE SANDHI CHAIN:
        1 becomes 7, 7 becomes 3, 3 becomes 2, 2 becomes 1, 5 becomes 7,
        4 becomes 2, 8 becomes 4; the final syllable keeps its citation
        tone. THE SEVEN PRONOUNS: 我 gua2, 汝 li2, 伊 i1, 阮 gun2
        (excl.), 咱 lan2 (incl.), 恁 lin2, 怹 in1; possessive with 诶 e5.
        THE FIVE NEGATORS: 毋 m7, 无 bo5, 袂 bue7, 免 bian2, 莫 mai3.
        THE ASPECT PARTICLES: 咧 teh4 (progressive), 矣 ah4 (completed),
        捌 bat4...过 kue3 (experienced), 有 u7 (past done), 欲 beh4 / 会
        e7 (future). THE QUESTION FRAMES: 敢 kam2, A-not-A, 抑 iah8,
        啥 siann2, 啥人, 叨位, 当时, 按怎, 为啥物. THE CLASSIFIERS: 个
        e5, 只 tsiah4, 条 tiau5, 张 tiunn1, 本 pun2, 间 king1, 台 tai5,
        杯 pue1, 碗 uann2. THE CONNECTOR FRAMES: 了后, 因为...所以,
        虽然...毋过, 若...就, 毋但...嘛, 一边...一边, 越...越,
        只要...就, 无论, 之前. TWO HUNDRED CORE WORDS (condensed): 人
        lang5, 囝仔 gin2-a2, 查埔 tsa1-poo1, 查某 tsa1-boo2, 朋友 ping5-iu2,
        老父 lau7-pe7, 老母 lau7-bu2, 厝 tshu3, 门 mng5, 路 loo7, 车 tshia1,
        学校 hak8-hau7, 市场 tshi7-tiunn5, 医生 i1-sing1, 钱 tsinn5, 饭
        png7, 水 tsui2, 茶 te5, 鱼 hi5, 肉 bah4, 天 thinn1, 地 te7, 山
        suann1, 海 hai2, 日 jit8, 月 gueh8, 书 tsu1, 话 ue7, 时间 si5-kan1,
        食 tsiah8, 饮 lim1, 去 khi3, 来 lai5, 看 khuann3, 听 thiann1, 讲
        kong2, 写 sia2, 读 thak8, 行 kiann5, 走 tsau2, 坐 tse7, 睏 khun3,
        买 be2, 卖 bue7, 做 tso3, 学 oh8, 教 ka3, 爱 ai3, 欲 beh4, 会 e7,
        知 tsai1, 想 siunn7, 问 mng7, 开 khui1, 好 ho2, 歹 phainn2, 大 tua7,
        细 se3, 新 sin1, 旧 ku7, 长 tng5, 短 te2, 高 kuan5, 低 ke7, 远
        hng7, 近 kun7, 快 khuai3, 慢 ban7, 热 juah8, 冷 ling2, 甜 tinn1,
        咸 kiam5, 酸 sng1, 苦 khoo2, 媠 sui2, 勇 iong2, 聪明 tshong1-bing5,
        欢喜 huann1-hi2, 真 tsin1, 足 tsiok4, 搁 koh4, 犹原 iu5-guan5,
        已经 i7-king1, 拢 long2, 逐 tak8, 嘛 ma7, 才 tsiah4, 捌 bat4, 一
        tsit8, 二 ji7, 三 sann1, 四 si3, 五 goo7, 六 lak8, 七 tshit4, 八
        peh4, 九 kau2, 十 tsap8, 百 pah4, 千 tshing1, 万 ban7, 今仔日
        kin1-a2-jit8, 昨昏 tsa1-hng1, 明仔载 bin5-a2-tsai3, 早起 tsa2-khi2,
        下晡 e7-poo1, 暗 am3, 点 tiam2, 分 hun1, 头 thau5, 目睭 bak8-tsiu1,
        耳仔 hinn7-a2, 嘴 tshui3, 手 tshiu2, 脚 kha1, 心 sim1, 狗 kau2, 猫
        niau1, 鸟 tsiau2, 树 tshiu7, 花 hue1, 落雨 loh8-hoo7, 出日
        tshut4-jit8, 起风 khi2-hong1, 电话 tian7-ue7, 手机 tshi2-ki1,
        电脑 tian7-nau2, 上网 tsiunn7-bang7 - and the hundred more in
        records 4-20. THE GREETING: 食饱未 tsiah8-pa2-bue7. THE FAREWELL:
        再会 tsai3-hue7, 慢走 ban7-tsau2. THE IDIOMS: 食紧撞破碗, 歹竹出好
        笋, 一枝草一点露, 天公疼憨人, 一步一脚印. THE SEAL SENTENCES:
        学无止境 (learning never ends), 故乡的月尚光 (home's moon shines
        brightest), 一家人食饭真欢喜 (the family meal is joy). The
        examination: say the eight tones, chant the sandhi chain, run one
        verb through all aspects, ask six questions, bargain at the market,
        tell the Lukang story, and close with 食饱未."""),
    how_it_works=textwrap.dedent("""\
        This record is the whole ladder in one climb: tones, sandhi,
        pronouns, negators, aspects, questions, classifiers, connectors,
        two hundred core words, greetings, idioms, and the seal sentences -
        everything the thirty-three records taught, compressed into a single
        reference the learner can carry. The drill is the mastery
        examination: perform each listed feat in order, in Min Nan, without
        the book. Pass it, and the ladder is climbed."""),
    key_points=[
        "The eight tones and the sandhi chain - say them, chant the ring.",
        "The seven pronouns with the 阮/咱 split; the five negators.",
        "The aspect particles: 咧, 矣, 捌...过, 有, 欲/会.",
        "The question frames and the classifiers.",
        "The connector frames: 了后 through 之前.",
        "Two hundred core words condensed - the working vocabulary.",
        "The greeting 食饱未; the farewells 再会, 慢走.",
        "The idioms: 食紧撞破碗, 歹竹出好笋, 一枝草一点露, 一步一脚印.",
        "The seal sentences: 学无止境; 故乡的月尚光; 一家人食饭真欢喜.",
        "The mastery examination: perform every feat in order, in Min Nan, without the book.",
    ],
    requirements=[
        "Learners should perform the full mastery examination aloud without the book.",
        "Learners should keep this record as the daily quick reference.",
    ],
    standards=[
        "The full canon of records 1-33, consolidated.",
    ],
    citations=[
        "All citations of records 1-33 apply; this record consolidates them.",
    ],
    sig_lens=("Through the Signature lens, the mastery review is the "
              "covenant's great seal pressed over all thirty-four rungs: "
              "every tone, every word, every story gathered into one "
              "signed page - the learner now a signatory of the Min Nan "
              "covenant, able to speak the oath in full. This Signature "
              "reading seals the graduate."),
)

SIG_TAIL = ("His Signature editions: the Min Nan ladder read through the "
            "Signature lens - every record a signed covenant of meaning, "
            "clearly labeled Signature-made, never presented as authentic "
            "public record.")
