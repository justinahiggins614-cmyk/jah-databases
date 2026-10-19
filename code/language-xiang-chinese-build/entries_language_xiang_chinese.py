#!/usr/bin/env python3
"""Entries for the Xiang Chinese to English databases (Manon's language project, 2026-10-17).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,602 databases) PLUS
every shard index title in jah-databases-data-1: zero 'language-xiang*'
slugs; ID prefixes JAH-LHSN- (public) and JAH-LHSNS- (signature) verified
free in the manifest id_prefix values AND in every shard index (zero zgrep
hits for 'JAH-LHSN' across all index.jsonl.gz files). Pre-authoring
whole-system dedupe-gate check over all 68 planned titles (34 records + 34
Signature Edition titles): zero collisions, zero refusals.

This build creates two NEW databases, 34 ladder-ordered records each:

  language-xiang-chinese           - The Xiang Chinese to English Database
                                     (public-harvest: real, fact-checked
                                     Xiang - overview, the Chinese-character
                                     writing system, Changsha phonology and
                                     the six tones, core vocabulary with
                                     sentences, grammar essentials, themed
                                     sentence sets, verb aspect, questions
                                     and answers, commands, descriptions,
                                     stories, idioms and proverbs,
                                     registers, complex sentences,
                                     conversations, mastery reference; every
                                     line in Chinese characters with
                                     pinyin-style reading and English;
                                     standard references Norman 1988, Wu
                                     2005, Bao & Chen 2005, Yuan 1960/1983,
                                     Ethnologue 26th ed., ISO 639-3 hsn)
  language-xiang-chinese-signature - The Xiang Chinese to English Signature
                                     Database (his original Signature
                                     Language Method: every character a sworn
                                     mark, every tone a sealed vow, every
                                     sentence a covenant of meaning; src
                                     signature, titles suffixed
                                     " (Signature Edition)", clearly labeled
                                     Signature-made, never presented as
                                     authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record carries Xiang Chinese content (Chinese characters) with
pinyin-style reading and English translation + example sentences. Sentences
are required in EVERY record - no vocabulary-list-only records.

Romanization note: Xiang has no single standard romanization (the Pinfa
system of Dr. C. F. Lau is adapted for Xiang on Omniglot). This database
gives a toneless pinyin-style reading as a learning bridge; the real pitch
follows the six Changsha tones in the phonology record, never Mandarin
tones. Documented Changsha IPA readings are quoted where the references
give them.

Fact-check rule: word-level vocabulary and grammar facts follow the
documented references. Example sentences are teaching illustrations
constructed from that documented vocabulary and grammar (Signature-built
teaching sentences, never passed off as field recordings).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_xiang_chinese.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and ends
with the OK marker; the build machine-executes all 68 demos before writing.

Build-time cross-check: every entry declares 'must_contain' strings and the
build asserts each one appears verbatim in the record description, so entry
text and demo outputs can never drift apart.

No website references. Screened per canon.
"""

SIG_TAIL = ("Signature original - his original Signature Language Method: "
            "every character a sworn mark, every tone a sealed vow, every "
            "sentence a covenant of meaning. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_ETH = ("Ethnologue (26th ed., 2023): Xiang Chinese [hsn], about 38 "
           "million native speakers (2021 figure).")
CIT_NORMAN = ("Norman J. Chinese. Cambridge University Press; 1988. "
              "Xiang among the central groups; Old Xiang keeps the "
              "three-way Middle Chinese obstruent distinction.")
CIT_WU = ("Wu Y. A synchronic and diachronic study of the grammar of the "
          "Chinese Xiang dialects. Mouton de Gruyter; 2005. The reference "
          "grammar of Xiang dialect grammar, including the aspect "
          "particles.")
CIT_BAOCHEN = ("Bao H, Chen H. Xiāngyǔ de fēnqū [The divisions of Xiang "
               "languages]. Fāngyán. 2005;(3):261-270. Five subgroups: "
               "Chang-Yi 17.8M, Lou-Shao 11.5M, Chen-Xu 3.4M, Hengzhou "
               "4.3M, Yong-Quan 6.5M speakers.")
CIT_YUAN = ("Yuan J. Hànyǔ fāngyán gàiyào [An introduction to Chinese "
            "dialects]. 1960/1983. The classic New Xiang / Old Xiang "
            "division: Changsha represents New Xiang, Shuangfeng Old Xiang.")
CIT_ISO = ("ISO 639-3: hsn (Xiang Chinese). Glottolog: xian1251. Xiang "
           "has no ISO 639-1 code.")
CIT_ZHWIKI = ("Changsha dialect vocabulary tables (kinship, body, verbs, "
              "打-compounds), zh.wikipedia.org/wiki/长沙话; field of "
              "documented Changsha words: 堂客 wife, 娭毑 grandmother, "
              "细伢子 child, 喫 to eat, 何解 why.")
CIT_ENWIKI = ("Xiang Chinese, en.wikipedia.org/wiki/Xiang_Chinese: "
              "subgroups, speaker geography, Nanchu ancestry, Tang and "
              "Ming migrations, Gan influence.")
CIT_PINFA = ("Omniglot: the Pinfa romanization system of Dr. C. F. Lau "
             "(Liu Zin Fad), developed for Hakka and adapted for Xiang "
             "and Gan.")
CIT_LL = ("Language Log (Mair V, 2020): Changsha speech [tsã˩˧ sɔ˧ ɣo˨˩]; "
          "Changsha not mutually intelligible with Standard Mandarin.")
CIT_TONE = ("Changsha six-tone description: old-style 23 initials, 45 "
            "finals, 6 tones; new-style 20 initials, 39 finals "
            "(lovingchinese.com); Old Xiang (Shuangfeng) 28 initials, 11 "
            "vowels, 5 tones, no final stops (standard dialectological "
            "accounts).")
CIT_HUNAN = ("Hunan cultural records: the Hunan spirit 吃得苦、霸得蛮、"
             "不怕死、耐得烦; the saying 无湘不成军; 四川人不怕辣，湖南"
             "人怕不辣; Hunan respectful 恁 (nia) from 你老人家.")


def _vlines(pairs):
    return "\n".join("  %s (%s) - %s" % p for p in pairs)


def _slines(pairs):
    return "\n".join("  %s (%s) - %s" % p for p in pairs)


SENT_NOTE = ("Example sentences are Signature-built teaching illustrations "
             "from documented Xiang vocabulary and grammar, never field "
             "recordings.")

ENTRIES = [
    {
        "key": "overview",
        "name": "Xiang Chinese Language Overview",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Xiang Chinese (湘语 xiāngyǔ, also called Hunanese or 湖南话 "
            "húnánhuà) is the Sinitic language of Hunan province in south "
            "central China. It carries ISO 639-3 code hsn (Glottolog "
            "xian1251; there is no ISO 639-1 code) and is one of the ten "
            "major groups of Chinese. About 38 million people speak it as a "
            "mother tongue (Ethnologue 26th ed., 2021 figure), which makes "
            "Xiang one of the largest Sinitic languages on earth. \n\n"
            "Where it is spoken. The heartland is central and southwestern "
            "Hunan - Changsha, Zhuzhou, Xiangtan, Yiyang, Loudi, Hengyang, "
            "Shaoyang - with Xiang-speaking pockets in northern Guangxi "
            "(Quanzhou, Guanyang, Ziyuan, Xing'an, Longsheng) and parts of "
            "Guizhou, Guangdong, Sichuan, Jiangxi, and Hubei. \n\n"
            "Official status. Xiang is not an official language; Putonghua "
            "(Standard Mandarin) is the official language of China. Xiang "
            "is the living regional language of Hunan homes, markets, and "
            "streets, and it is not mutually intelligible with Mandarin. \n\n"
            "Dialects. The classic division (Yuan Jiahua, 1960) is New "
            "Xiang versus Old Xiang: the Changsha dialect represents New "
            "Xiang, the Shuangfeng dialect represents Old Xiang. The "
            "five-subgroup scheme (Bao & Chen, 2005) counts Chang-Yi "
            "(New Xiang, 17.8M), Lou-Shao (Old Xiang, 11.5M), Chen-Xu "
            "(3.4M), Hengzhou (4.3M), and Yong-Quan (6.5M). The Language "
            "Atlas of China (1987) named them Chang-Yi, Lou-Shao, and "
            "Ji-Xu. Old Xiang still keeps the three-way Middle Chinese "
            "obstruent distinction - voiced stops, fricatives, and "
            "affricates survive there - while New Xiang has devoiced them. \n\n"
            "History in one breath. Yang Xiong's Fangyan (Han dynasty) "
            "records Southern Chu (Nanchu) speech in this region, the "
            "ancestor of Xiang; Tang-dynasty migration brought Middle "
            "Chinese into Hunan; Ming-dynasty settlers from Jiangxi "
            "(江西填湖广, Jiangxi filling Huguang) reshaped the east into "
            "New Xiang under Gan influence. Xiang-speaking Hunanese - Mao "
            "Zedong, Zuo Zongtang, Huang Xing among them - shaped modern "
            "Chinese history. \n\n"
            "What makes Xiang learnable. It is written in Chinese "
            "characters you may already know, the word order is the "
            "familiar subject-verb-object, and there are no verb "
            "conjugations - time rides on small aspect particles like 了 "
            "and 咖. Learn the six Changsha tones and the signature words, "
            "and Hunan opens like a door. (Word order: SVO.) \n\n"
            "First sentences in Xiang:\n"
            "  你好 (nihao) - Hello!\n"
            "  恰饭了冇 (qiafanle mao) - Have you eaten yet?\n"
            "  我是湖南人 (woshi hunanren) - I am a Hunan person.\n"
            "  我蛮喜欢湘语 (woban xihuan xiangyu) - I really like the Xiang language."
        ),
        "how_it_works": (
            "This record is the map of the whole database. It fixes the "
            "identity of the language - name (湘语, 湖南话), code (hsn), "
            "family (Sino-Tibetan, Sinitic, Chinese, Xiang), speaker scale "
            "(about 38 million native), territory (Hunan plus pockets in "
            "five neighboring provinces), standing (regional, not "
            "official), dialect landscape (New/Old Xiang; five subgroups), "
            "and the historical arc (Nanchu, Tang migration, Ming Jiangxi "
            "settlement). Every later record hangs facts on this frame. "
            "Work through the ladder in order and each record assumes only "
            "what earlier records taught."
        ),
        "key_points": [
            "Native names: 湘语 (xiāngyǔ), 湖南话 (húnánhuà); ISO 639-3 hsn.",
            "Family: Sino-Tibetan, Sinitic, Chinese, Xiang group.",
            "About 38 million native speakers (2021); heartland Hunan with pockets in Guangxi, Guizhou, Guangdong, Sichuan, Jiangxi, Hubei.",
            "Regional language, not official; not mutually intelligible with Mandarin.",
            "New Xiang (Changsha) vs Old Xiang (Shuangfeng); five subgroups per Bao & Chen 2005.",
            "Old Xiang keeps voiced Middle Chinese obstruents; New Xiang devoiced them.",
            "Nanchu ancestry; Tang and Ming migrations; Jiangxi/Gan influence on New Xiang.",
            "SVO word order; aspect particles carry time; six tones in Changsha.",
        ],
        "requirements": [
            "No prior knowledge of any Chinese language is assumed.",
            "Read the writing-system record before the phonology record; read phonology before vocabulary.",
        ],
        "standards": [
            "Speaker figures are rounded public estimates (Ethnologue-style reporting); stated as approximate.",
            "Dialect and history claims follow Norman 1988, Bao & Chen 2005, Yuan 1960/1983.",
            SENT_NOTE,
        ],
        "citations": [CIT_ETH, CIT_ISO, CIT_NORMAN, CIT_BAOCHEN, CIT_YUAN, CIT_ENWIKI, CIT_LL],
        "must_contain": ["hsn", "38 million", "Changsha", "Shuangfeng", "SVO", "恰饭了冇"],
        "sig_lens": (
            "Through the Signature lens this overview is a census of a "
            "living province of speakers: every headcount a sworn "
            "roll-call, every subgroup a branch of one river system, every "
            "migration a seal on the covenant that this language will be "
            "carried whole into the archive."
        ),
        "drill": {
            "native_m": 38.0, "iso3": "hsn", "glottolog": "xian1251",
            "subgroups": {"Chang-Yi": 17.8, "Lou-Shao": 11.5, "Chen-Xu": 3.4,
                          "Hengzhou": 4.3, "Yong-Quan": 6.5},
            "cities": ["Changsha", "Zhuzhou", "Xiangtan", "Yiyang", "Loudi",
                       "Hengyang", "Shaoyang"],
            "pocket_provinces": ["Guangxi", "Guizhou", "Guangdong", "Sichuan",
                                 "Jiangxi", "Hubei"],
            "official": False, "tones_changsha": 6,
        },
    },
    {
        "key": "writing",
        "name": "The Xiang Chinese Writing System",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Xiang is written in Chinese characters (汉字 hànzì), the same "
            "script as Mandarin. In mainland Hunan the simplified forms are "
            "standard (语, 话, 饭, 门); traditional forms (語, 話, 飯, 門) "
            "appear in older books and in Hong Kong/Taiwan materials. "
            "Modern writing runs left-to-right in horizontal lines; the old "
            "top-to-bottom, right-to-left columns survive on signs, "
            "couplets, and temple plaques. Punctuation and Arabic numerals "
            "0-9 match Mandarin usage. \n\n"
            "There is no native Xiang alphabet and no single standard "
            "romanization. Learners meet two bridges: Hanyu Pinyin, the "
            "Mandarin romanization everyone in China learns in school, and "
            "the Pinfa system of Dr. C. F. Lau (Liu Zin Fad), developed for "
            "Hakka and adapted for Xiang and Gan. This database uses a "
            "toneless pinyin-style reading on every line as a learning "
            "bridge - apply the six Changsha tones from the phonology "
            "record, never Mandarin tones. Documented Changsha IPA readings "
            "are quoted in the phonology record where the references give "
            "them. \n\n"
            "Chinese numerals, the counting backbone:\n"
            "  一 (yi) - one    二 (er) - two    三 (san) - three\n"
            "  四 (si) - four    五 (wu) - five    六 (liu) - six\n"
            "  七 (qi) - seven    八 (ba) - eight    九 (jiu) - nine\n"
            "  十 (shi) - ten    百 (bai) - hundred    千 (qian) - thousand\n\n"
            "Write these first signature words:\n"
            "  湘语 (xiangyu) - the Xiang language\n"
            "  湖南话 (hunanhua) - Hunan speech\n"
            "  堂客 (tangke) - wife\n"
            "  娭毑 (aijie) - grandmother\n"
            "  细伢子 (xiyazi) - child, kid\n"
            "  霸蛮 (baman) - the Hunan can-do spirit"
        ),
        "how_it_works": (
            "The script works exactly like written Mandarin: learn the "
            "characters and you can read Xiang on the page, because the "
            "writing system is shared even where the spoken words differ. "
            "Where speech diverges, characters are still used - 堂客 is "
            "written with ordinary characters even though Mandarin would "
            "say 妻子. Pinyin-style readings in this database are a "
            "pronunciation scaffold, not a phonetic transcript; the "
            "phonology record gives the real Changsha sounds. Stroke order "
            "follows standard hanzi rules, so any character dictionary "
            "works for lookup."
        ),
        "key_points": [
            "Script: Chinese characters (simplified standard in Hunan); left-to-right modern layout.",
            "No native alphabet; no single standard romanization for Xiang.",
            "Pinyin-style toneless readings used as a learning bridge; Pinfa exists as a scholarly alternative.",
            "Same punctuation and Arabic numerals as Mandarin.",
            "Spoken Xiang words are written with ordinary characters (堂客, 娭毑, 细伢子).",
            "Stroke order and radicals follow standard hanzi rules.",
        ],
        "requirements": [
            "Be able to recognize the 10 numerals before the numbers record.",
            "Do not read the pinyin-style syllables with Mandarin tones; wait for the phonology record.",
        ],
        "standards": [
            "Script facts follow the standard references (Norman 1988; Ethnologue).",
            "Romanization bridge is this database's teaching convention, stated openly.",
            SENT_NOTE,
        ],
        "citations": [CIT_NORMAN, CIT_ETH, CIT_PINFA, CIT_ZHWIKI],
        "must_contain": ["Chinese characters", "pinyin-style", "Pinfa", "left-to-right", "堂客", "娭毑"],
        "sig_lens": (
            "Through the Signature lens each character is a sworn mark "
            "pressed into the page: the same strokes Mandarin uses, "
            "re-sealed with Hunan meaning, so that 堂客 carries a whole "
            "household in two marks."
        ),
        "drill": {
            "script": "hanzi", "simplified": True, "direction": "left-to-right",
            "native_alphabet": False, "standard_romanization": False,
            "numerals": ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"],
            "test_words": ["湘语", "湖南话", "堂客", "娭毑", "细伢子", "霸蛮"],
        },
    },
    {
        "key": "phonology",
        "name": "Xiang Chinese Pronunciation and Phonology",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Xiang pronunciation rests on three pillars: a rich consonant "
            "inventory, a large vowel inventory, and tone - six tones in "
            "Changsha, five in Old Xiang. The rhythm is syllable-timed, "
            "each syllable getting its full weight. \n\n"
            "The six Changsha tones (New Xiang), in the standard "
            "description: 阴平 yinping 33 (high level), 阳平 yangping 13 "
            "(low rising), 上声 shangsheng 41 (high falling), 阴去 yinqu "
            "24 (mid rising), 阳去 yangqu 45 (high rising), 入声 rusheng "
            "21 (low falling, short). Changsha keeps the entering tone as "
            "a category, but the old stop endings are gone. Sources vary "
            "slightly on the exact values (some give shangsheng as 42); "
            "the category count of six is stable. Spoken Changsha sounds "
            "like this in IPA: 长沙话 [tsã˩˧ sɔ˧ ɣo˨˩], and 湘语 itself is "
            "[sian˧ y˦˩]. \n\n"
            "Consonants and vowels. Old-style Changsha counts 23 initials "
            "and 45 finals; new-style Changsha counts 20 initials and 39 "
            "finals. Old Xiang (Shuangfeng) is richer still: 28 initial "
            "consonants - the highest count of any major Sinitic language "
            "- 11 vowels, syllabic m and n, nasalized vowels, and final "
            "-n and -ng, but no final stops. The signature sound fact: Old "
            "Xiang preserves the voiced obstruents of Middle Chinese - a "
            "three-way distinction of voiceless unaspirated, voiceless "
            "aspirated, and voiced. New Xiang (Changsha) has devoiced "
            "them to plain voiceless. Compare 桃 (peach): Shuangfeng də2 "
            "(voiced), Changsha taɤ2 (voiceless); 坐 (sit): Shuangfeng "
            "dzu6, Changsha tso6; 共 (together): Shuangfeng gaŋ6, Changsha "
            "koŋ5/koŋ6; 白 (white): Shuangfeng piɛ6, Changsha pɤ7. \n\n"
            "Sound it out - ten spoken-example words (characters, "
            "pinyin-style reading, English):\n"
            "  人 (ren) - person\n"
            "  水 (shui) - water\n"
            "  饭 (fan) - rice, meal\n"
            "  山 (shan) - mountain\n"
            "  河 (he) - river\n"
            "  辣椒 (lajiao) - chili pepper\n"
            "  堂客 (tangke) - wife\n"
            "  娭毑 (aijie) - grandmother\n"
            "  晓得 (xiaode) - to know\n"
            "  霸蛮 (baman) - can-do spirit\n"
            "  湖南 (hunan) - Hunan"
        ),
        "how_it_works": (
            "Tone is part of the word: the same syllable on a different "
            "pitch pattern is a different word, so learners drill the six "
            "Changsha patterns (33, 13, 41, 24, 45, 21) until the ear "
            "hears them as different letters. Consonants are drilled in "
            "the Old/New contrast: hear Shuangfeng's voiced də2 against "
            "Changsha's voiceless taɤ2 and the whole voicing history of "
            "Xiang clicks into place. Finals carry nasalization in Old "
            "Xiang - let the air leak through the nose on words like "
            "tsã. Because the script never marks tone, every new word is "
            "learned as character plus tone pattern together."
        ),
        "key_points": [
            "Changsha: 6 tones - yinping 33, yangping 13, shangsheng 41, yinqu 24, yangqu 45, rusheng 21.",
            "Entering tone kept as a category in Changsha; stop endings lost.",
            "Old-style Changsha: 23 initials, 45 finals; new-style: 20 initials, 39 finals.",
            "Old Xiang (Shuangfeng): 28 initials, 11 vowels, 5 tones, syllabic m/n, nasalization, no final stops.",
            "Old Xiang preserves voiced Middle Chinese obstruents; New Xiang devoiced them.",
            "Documented minimal sets: 桃 də2/taɤ2, 坐 dzu6/tso6, 共 gaŋ6/koŋ6, 白 piɛ6/pɤ7.",
            "Syllable-timed rhythm; tone is never written in daily script.",
        ],
        "requirements": [
            "Say the six tone patterns aloud before learning vocabulary.",
            "Practice the voiced/voiceless pairs (də2 vs taɤ2) until the ear separates them.",
        ],
        "standards": [
            "Tone values follow the standard Changsha description; slight source variation is noted, not hidden.",
            "Voicing facts follow Norman 1988 and the standard dialectological accounts.",
            SENT_NOTE,
        ],
        "citations": [CIT_NORMAN, CIT_TONE, CIT_LL, CIT_WU],
        "must_contain": ["six", "33", "13", "41", "24", "45", "21", "voiced", "Shuangfeng", "taɤ2"],
        "sig_lens": (
            "Through the Signature lens the six tones are six sealed vows "
            "of pitch: each syllable sworn at its height, the voiced "
            "initials of Old Xiang kept like heirloom seals while New "
            "Xiang stamps them plain."
        ),
        "drill": {
            "changsha_tones": {"yinping": 33, "yangping": 13, "shangsheng": 41,
                               "yinqu": 24, "yangqu": 45, "rusheng": 21},
            "old_changsha": {"initials": 23, "finals": 45},
            "new_changsha": {"initials": 20, "finals": 39},
            "shuangfeng": {"initials": 28, "vowels": 11, "tones": 5},
            "voicing_pairs": [["də2", "taɤ2"], ["dzu6", "tso6"], ["gaŋ6", "koŋ6"],
                               ["piɛ6", "pɤ7"]],
            "example_words": 11,
        },
    },
    {
        "key": "nouns",
        "name": "Core Xiang Chinese Nouns I",
        "group": "Core Vocabulary",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five (25) essential Xiang nouns - people, body, home, and "
            "street - each with a sentence. Readings are pinyin-style; "
            "documented Changsha IPA is noted for the signature words. "
            "Nouns take no plural marking and no gender; number is shown "
            "with classifiers (个, 只, 条), taught in the grammar record. \n\n"
            + _vlines([
                ("堂客", "tangke", "wife [Changsha dan ke]"),
                ("娭毑", "aijie", "grandmother [Changsha ŋai ʨie]"),
                ("嗲嗲", "diadie", "grandfather [Changsha diɔ diɔ]"),
                ("爷", "ye", "dad [Changsha iɔ]"),
                ("姆妈", "muma", "mom"),
                ("细伢子", "xiyazi", "child, kid"),
                ("崽", "zai", "son"),
                ("细姑", "xigu", "younger paternal aunt"),
                ("脑壳", "naoke", "head [Changsha lau kʰo]"),
                ("眼睛", "yanjing", "eyes"),
                ("颈根", "jinggen", "neck"),
                ("膝头骨", "xitougu", "knee"),
                ("手巴子", "shoubazi", "arm, hand"),
                ("指码子", "zhimazi", "finger"),
                ("眼眨毛", "yanzhamao", "eyelashes"),
                ("饭", "fan", "rice, meal"),
                ("水", "shui", "water"),
                ("臭干子", "chouganzi", "stinky tofu"),
                ("辣椒", "lajiao", "chili pepper"),
                ("河西", "hexi", "west of the Xiang River"),
                ("样范", "yangfan", "appearance, manner"),
                ("路", "lu", "way, method"),
                ("泡泡子", "paopaozi", "lies, tall talk"),
                ("黑脑壳", "heinaoke", "unlicensed taxi"),
                ("人", "ren", "person"),
            ]) + "\n\n"
            "One sentence per noun:\n"
            + _slines([
                ("我堂客蛮好", "wotangke banhao", "My wife is really good."),
                ("娭毑身体好", "aijie shentihao", "Grandma is in good health."),
                ("嗲嗲爱讲故事", "diadie aijiang gushi", "Grandpa loves telling stories."),
                ("爷在屋里", "ye zai wuli", "Dad is at home."),
                ("姆妈去买菜了", "muma qu maicaile", "Mom went to buy vegetables."),
                ("细伢子在广场耍", "xiyazi zai guangchang shua", "The kid is playing in the square."),
                ("崽今年十岁", "zai jinnian shisui", "My son is ten this year."),
                ("细姑来看我们", "xigu lai kan women", "Younger aunt came to visit us."),
                ("我脑壳有点疼", "wonaoke youdian teng", "My head aches a bit."),
                ("你眼睛好大", "ni yanjing haoda", "Your eyes are so big."),
                ("颈根扭到了", "jinggen niudaole", "I twisted my neck."),
                ("膝头骨摔破了", "xitougu shuaipole", "I scraped my knee falling."),
                ("手巴子举起来", "shoubazi ju qilai", "Raise your arm."),
                ("指码子划破了", "zhimazi huapole", "I cut my finger."),
                ("眼眨毛好长", "yanzhamao haochang", "The eyelashes are so long."),
                ("恰饭了冇", "qiafanle mao", "Have you eaten yet?"),
                ("给我一杯水", "geiwo yibei shui", "Give me a glass of water."),
                ("坡子街有臭干子", "pozijie you chouganzi", "Pozi Street has stinky tofu."),
                ("湖南人爱恰辣椒", "hunanren ai qia lajiao", "Hunan people love eating chili."),
                ("岳麓山在河西", "yuelushan zai hexi", "Yuelu Mountain is west of the river."),
                ("他样范蛮好", "ta yangfan banhao", "He carries himself well."),
                ("已经冇别的路了", "yijing mao biede lule", "There is no other way left."),
                ("讲话莫一口泡泡子", "jianghua mo yikou paopaozi", "Do not talk full of lies."),
                ("街上好多黑脑壳", "jieshang haoduo heinaoke", "The street is full of unlicensed taxis."),
                ("湖南人热情好客", "hunanren reqing haoke", "Hunan people are warm and hospitable."),
            ])
        ),
        "how_it_works": (
            "Each noun is learned as a triple: characters, pinyin-style "
            "reading, English - plus one real sentence that puts it to "
            "work. Signature words (堂客, 娭毑, 细伢子, 脑壳, 臭干子) are "
            "the ones no Mandarin speaker would guess; they are drilled "
            "first because they pay off fastest in Hunan. Say each sentence "
            "aloud with the six Changsha tones; the pinyin-style reading "
            "is toneless on purpose, so your ear must supply the melody."
        ),
        "key_points": [
            "25 core nouns: kinship, body, food, street life.",
            "Signature Changsha words: 堂客 wife, 娭毑 grandmother, 嗲嗲 grandfather, 细伢子 kid, 崽 son.",
            "Body words: 脑壳 head, 颈根 neck, 膝头骨 knee, 手巴子 arm, 指码子 finger, 眼眨毛 eyelashes.",
            "Street words: 臭干子 stinky tofu, 黑脑壳 unlicensed taxi, 泡泡子 lies.",
            "No plural or gender marking on nouns.",
            "One working sentence per noun; readings are toneless pinyin-style.",
        ],
        "requirements": [
            "Master the six tones before drilling these sentences aloud.",
            "Learn the kinship set (堂客, 娭毑, 嗲嗲, 爷, 姆妈) as one family block.",
        ],
        "standards": [
            "Vocabulary follows the documented Changsha tables (zh.wikipedia 长沙话).",
            SENT_NOTE,
        ],
        "citations": [CIT_ZHWIKI, CIT_WU],
        "must_contain": ["堂客", "娭毑", "细伢子", "脑壳", "臭干子", "25"],
        "sig_lens": (
            "Through the Signature lens each noun is a sworn token of "
            "Hunan life: 堂客 seals a household, 臭干子 seals a street, "
            "and every sentence is a covenant that the word will be "
            "carried correctly."
        ),
        "drill": {
            "count": 25,
            "signature_words": ["堂客", "娭毑", "嗲嗲", "细伢子", "崽", "脑壳", "臭干子"],
            "kinship": ["堂客", "娭毑", "嗲嗲", "爷", "姆妈", "细姑", "崽"],
            "body": ["脑壳", "眼睛", "颈根", "膝头骨", "手巴子", "指码子", "眼眨毛"],
            "sentences": 25,
        },
    },
    {
        "key": "verbs",
        "name": "Core Xiang Chinese Verbs I",
        "group": "Core Vocabulary",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five essential Xiang verbs, each with a sentence. "
            "Verbs never conjugate - the same form serves past, present, "
            "and future; aspect particles (了, 咖, 着, 过) carry the time, "
            "taught in the aspect record. The 打-compound family is a "
            "Changsha signature: 打 plus a second character makes a whole "
            "world of everyday verbs. \n\n"
            + _vlines([
                ("喫", "qia", "to eat [the Hunan eat-word]"),
                ("晓得", "xiaode", "to know"),
                ("走", "zou", "to run (fast)"),
                ("行", "xing", "to walk"),
                ("讲", "jiang", "to speak, to talk"),
                ("来", "lai", "to come"),
                ("去", "qu", "to go"),
                ("买", "mai", "to buy"),
                ("卖", "mai", "to sell"),
                ("打望", "dawang", "to look around, to gaze"),
                ("打堆", "dadui", "to pile up"),
                ("打滞", "dazhi", "to overeat, to be stuffed"),
                ("打野", "daye", "to lose focus"),
                ("打流", "daliu", "to loiter, to wander"),
                ("打讲", "dajiang", "to have a heart-to-heart talk"),
                ("打止", "dazhi2", "to stop, to halt"),
                ("打哑", "daya", "to slack off, to be lazy"),
                ("架场", "jiachang", "to start, to kick off"),
                ("散棚", "sanpeng", "to end, to disperse"),
                ("捡场", "jianchang", "to prepare, to get ready"),
                ("愿神", "yuanshen", "to think, to ponder"),
                ("拐场", "guaichang", "to have an accident"),
                ("了难", "liaonan", "to solve a difficulty"),
                ("圆功", "yuangong", "to complete, to finish well"),
                ("睡", "shui", "to sleep"),
            ]) + "\n\n"
            "One sentence per verb:\n"
            + _slines([
                ("我喫了饭", "wo qiale fan", "I ate the meal."),
                ("你晓得啵", "ni xiaode bo", "Do you know?"),
                ("他走得好快", "ta zoude haokuai", "He runs so fast."),
                ("我们行路去", "women xinglu qu", "We go on foot."),
                ("来讲几句", "lai jiang jiju", "Come say a few words."),
                ("你几时来", "ni jishi lai", "When are you coming?"),
                ("我要去长沙", "wo yao qu changsha", "I am going to Changsha."),
                ("去买点辣椒", "qu mai dian lajiao", "Go buy some chili peppers."),
                ("他在卖臭干子", "ta zai mai chouganzi", "He is selling stinky tofu."),
                ("莫到处打望", "mo daochu dawang", "Do not gawk around everywhere."),
                ("把书打堆放好", "ba shu dadui fanghao", "Pile the books up neatly."),
                ("恰多了打滞了", "qiaduole dazhile", "Ate too much and got stuffed."),
                ("上课莫打野", "shangke mo daye", "Do not lose focus in class."),
                ("莫在街上打流", "mo zai jieshang daliu", "Do not loiter on the street."),
                ("我们打讲一下", "women dajiang yixia", "Let us have a heart-to-heart."),
                ("车子打止了", "chezi dazhile", "The car stopped."),
                ("做事莫打哑", "zuoshi mo daya", "Do not slack off at work."),
                ("会议架场了", "huiyi jiachangle", "The meeting kicked off."),
                ("戏散棚了", "xi sanpengle", "The show ended."),
                ("先把场捡好", "xian ba chang jianhao", "Prepare everything first."),
                ("让我愿神一下", "rang wo yuanshen yixia", "Let me think it over."),
                ("路上拐场了", "lushang guaichangle", "There was an accident on the road."),
                ("这个难了了", "zhege nan liaole", "This difficulty is solved."),
                ("工程圆功了", "gongcheng yuangongle", "The project finished well."),
                ("细伢子睡了", "xiyazi shuile", "The kid fell asleep."),
            ])
        ),
        "how_it_works": (
            "Each verb is learned bare - no conjugation tables exist - "
            "plus one sentence showing it in motion. The 打-family "
            "(打望, 打堆, 打滞, 打野, 打流, 打讲, 打止, 打哑) is drilled as "
            "a block: one prefix, eight everyday meanings. Note the "
            "Xiang motion split: 走 is to run, 行/行路 is to walk - the "
            "opposite emphasis from Mandarin's 走路. Aspect particles "
            "attach after the verb (喫了, 散棚了) and are drilled in the "
            "aspect record."
        ),
        "key_points": [
            "25 core verbs; verbs never conjugate.",
            "喫 is the Hunan eat-word; 晓得 is to know.",
            "走 = to run; 行/行路 = to walk (documented Xiang motion split).",
            "The 打-compound family: 打望, 打堆, 打滞, 打野, 打流, 打讲, 打止, 打哑.",
            "架场 start, 散棚 end, 捡场 prepare, 愿神 ponder, 了难 solve, 圆功 complete.",
            "One working sentence per verb.",
        ],
        "requirements": [
            "Do not attach Mandarin-style tense thinking to these verbs; time comes from aspect particles.",
            "Drill the 打-family as one block until each compound is instant.",
        ],
        "standards": [
            "Verb inventory follows the documented Changsha tables (zh.wikipedia 长沙话).",
            "The 走/行 split follows the documented Xiang dialectological account.",
            SENT_NOTE,
        ],
        "citations": [CIT_ZHWIKI, CIT_WU],
        "must_contain": ["喫", "晓得", "打望", "打堆", "架场", "散棚", "走", "行"],
        "sig_lens": (
            "Through the Signature lens each verb is a sworn action: 喫 "
            "seals the meal, 打讲 seals the confidence, and the 打-family "
            "is a covenant of eight everyday motions."
        ),
        "drill": {
            "count": 25,
            "da_family": ["打望", "打堆", "打滞", "打野", "打流", "打讲", "打止", "打哑"],
            "motion_split": {"zou": "run", "xing": "walk"},
            "sentences": 25,
        },
    },
]
ENTRIES += [
    {
        "key": "adjectives",
        "name": "Xiang Chinese Adjectives and Adverbs",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Twenty-five (25) adjectives and fifteen (15) adverbs, each with a "
            "sentence. Xiang adjectives take no agreement - the same form "
            "describes one person or ten. Degree is carried by adverbs: "
            "蛮 (very, the Hunan signature intensifier), 好 (quite), 太 "
            "(too), 最 (most). Reduplication (redup) softens or intensifies: "
            "慢慢 (slowly), 好好 (properly). \n\n"
            "Adjectives:\n"
            + _vlines([
                ("蛮", "man", "very [the Hunan intensifier]"),
                ("好", "hao", "good, quite"),
                ("霸蛮", "baman", "tough, can-do"),
                ("辣", "la", "spicy, fierce"),
                ("漂亮", "piaoliang", "pretty"),
                ("高", "gao", "tall, high"),
                ("矮", "ai", "short"),
                ("胖", "pang", "fat"),
                ("瘦", "shou", "thin"),
                ("快", "kuai", "fast"),
                ("慢", "man", "slow"),
                ("热", "re", "hot"),
                ("冷", "leng", "cold"),
                ("甜", "tian", "sweet"),
                ("咸", "xian", "salty"),
                ("苦", "ku", "bitter"),
                ("香", "xiang", "fragrant"),
                ("臭", "chou", "smelly"),
                ("干净", "ganjing", "clean"),
                ("新", "xin", "new"),
                ("旧", "jiu", "old (things)"),
                ("大", "da", "big"),
                ("小", "xiao", "small"),
                ("远", "yuan", "far"),
                ("近", "jin", "near"),
            ]) + "\n\n"
            "Adverbs:\n"
            + _vlines([
                ("蛮", "man", "very"),
                ("很", "hen", "very"),
                ("太", "tai", "too"),
                ("最", "zui", "most"),
                ("都", "dou", "all, both"),
                ("也", "ye", "also"),
                ("就", "jiu", "just, then"),
                ("才", "cai", "only then"),
                ("还", "hai", "still, yet"),
                ("再", "zai", "again"),
                ("又", "you", "again (past)"),
                ("不", "bu", "not"),
                ("冇", "mao", "not have, have not"),
                ("莫", "mo", "do not (prohibitive)"),
                ("先", "xian", "first"),
            ]) + "\n\n"
            "Sentences:\n"
            + _slines([
                ("今天蛮热", "jintian banre", "Today is very hot."),
                ("这个菜好辣", "zhege cai haola", "This dish is quite spicy."),
                ("湖南人霸蛮", "hunanren baman", "Hunan people are tough and can-do."),
                ("辣椒蛮辣", "lajiao banla", "The chilies are very hot."),
                ("妹子好漂亮", "meizi haopiaoliang", "The girl is so pretty."),
                ("岳麓山好高", "yuelushan haogao", "Yuelu Mountain is so tall."),
                ("细伢子长高了", "xiyazi zhanggaole", "The kid grew taller."),
                ("他走得蛮快", "ta zoude bankuai", "He runs very fast."),
                ("慢慢来莫急", "manmanlai moji", "Come slowly, do not rush."),
                ("冬天蛮冷", "dongtian banleng", "Winter is very cold."),
                ("臭干子闻起臭恰起香", "chouganzi wenqi chou qiaqi xiang", "Stinky tofu smells bad but tastes fragrant."),
                ("屋里打扫得蛮干净", "wuli dasaode banganjing", "The house is cleaned very tidily."),
                ("买了件新衣裳", "maile jian xinyishang", "Bought a new piece of clothing."),
                ("橘子洲好大", "juzizhou haoda", "Orange Isle is so big."),
                ("长沙离我家不远", "changsha li wojia buyuan", "Changsha is not far from my home."),
                ("他都晓得", "ta dou xiaode", "He knows it all."),
                ("我也要去", "wo ye yaoqu", "I want to go too."),
                ("太贵了买不起", "taiguile baimabuqi", "Too expensive, cannot afford it."),
                ("这是最好的", "zhe shi zuihaode", "This is the best one."),
                ("冇吃饭就先恰", "mao chifan jiu xianqia", "If you have not eaten, eat first."),
                ("莫讲泡泡子", "mo jiang paopaozi", "Do not talk lies."),
                ("你先走我随后到", "ni xianzou wo suihoudao", "You go first, I will follow."),
                ("他又来了", "ta youlai le", "He came again."),
                ("还冇散棚", "hai mao sanpeng", "It has not ended yet."),
                ("再来一碗饭", "zailai yiwan fan", "Another bowl of rice, please."),
            ])
        ),
        "how_it_works": (
            "Adjectives slot straight before nouns or after the subject "
            "with no copula fuss: 今天蛮热, 这个菜好辣. 蛮 is the "
            "signature Hunan intensifier - use it everywhere a Mandarin "
            "speaker would use 很 or 非常, and you will sound local at "
            "once. Adverbs sit before the verb they modify (都晓得, 莫讲, "
            "先走); 冇 negates possession and completed action, 不 negates "
            "general states, 莫 is the prohibitive do-not. Reduplicated "
            "forms (慢慢, 好好) soften commands into friendly advice."
        ),
        "key_points": [
            "25 adjectives + 15 adverbs; no agreement of any kind.",
            "蛮 is the signature Hunan intensifier (very).",
            "Degree adverbs: 蛮/很/太/最; scope adverbs: 都/也/就/才/还/再/又.",
            "Negation trio: 不 (general), 冇 (not have), 莫 (prohibitive).",
            "Reduplication softens: 慢慢, 好好.",
            "Every item carries a working sentence.",
        ],
        "requirements": [
            "Use 蛮 as the default intensifier in all practice sentences.",
            "Keep 不/冇/莫 straight: drill the negation trio daily.",
        ],
        "standards": [
            "Core vocabulary follows documented Changsha usage.",
            SENT_NOTE,
        ],
        "citations": [CIT_ZHWIKI, CIT_WU],
        "must_contain": ["蛮", "冇", "莫", "25", "15", "redup"],
        "sig_lens": (
            "Through the Signature lens 蛮 is the sworn seal of Hunan "
            "emphasis: stamp it before any adjective and the sentence "
            "stands taller, a covenant of intensity."
        ),
        "drill": {
            "adjectives": 25, "adverbs": 15,
            "intensifiers": ["蛮", "很", "太", "最"],
            "negation": ["不", "冇", "莫"],
            "sentences": 25,
        },
    },
    {
        "key": "pronouns",
        "name": "Xiang Chinese Pronouns",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The full Xiang pronoun system, with the Hunan signatures. "
            "New-style Changsha uses the familiar 我/你/他 set; the "
            "respectful 恁 (nia, from 你老人家) is pure Hunan; Old Xiang "
            "varieties keep 渠 for he/she. Plurals add 们. Possession uses "
            "的. Each form carries a sentence. \n\n"
            "Personal pronouns:\n"
            + _vlines([
                ("我", "wo", "I, me"),
                ("你", "ni", "you"),
                ("恁", "nin", "you (respectful, Hunan)"),
                ("他", "ta", "he, him"),
                ("她", "ta", "she, her"),
                ("它", "ta", "it"),
                ("渠", "qu", "he/she (Old Xiang)"),
                ("我们", "women", "we, us"),
                ("你们", "nimen", "you (plural)"),
                ("他们", "tamen", "they, them"),
            ]) + "\n\n"
            "Possessive, demonstrative, interrogative:\n"
            + _vlines([
                ("我的", "wode", "my, mine"),
                ("你的", "nide", "your, yours"),
                ("他的", "tade", "his"),
                ("这", "zhe", "this"),
                ("那", "na", "that"),
                ("这里", "zheli", "here"),
                ("那里", "nali", "there"),
                ("哪个", "nage", "which"),
                ("么子", "mezi", "what"),
                ("何解", "hejie", "why [Changsha ogai]"),
            ]) + "\n\n"
            "Sentences:\n"
            + _slines([
                ("我是湖南人", "wo shi hunanren", "I am a Hunan person."),
                ("你恰饭了冇", "ni qiafanle mao", "Have you eaten?"),
                ("恁慢走", "nin man zou", "Take care on your way (respectful)."),
                ("他是长沙人", "ta shi changsharen", "He is a Changsha person."),
                ("她是我堂客", "ta shi wo tangke", "She is my wife."),
                ("渠讲老湘语", "qu jiang laoxiangyu", "He speaks Old Xiang."),
                ("我们一起去", "women yiqi qu", "We go together."),
                ("你们几个人", "nimen jige ren", "How many of you are there?"),
                ("他们都晓得", "tamen dou xiaode", "They all know."),
                ("这是我的书", "zhe shi wode shu", "This is my book."),
                ("那是你的伢", "na shi nide ya", "That is your child."),
                ("他的辣椒蛮辣", "tade lajiao banla", "His chilies are very hot."),
                ("这里是长沙", "zheli shi changsha", "This is Changsha."),
                ("那里是湘江", "nali shi xiangjiang", "That is the Xiang River."),
                ("哪个是你的", "nage shi nide", "Which one is yours?"),
                ("你讲么子", "ni jiang mezi", "What are you saying?"),
                ("何解不来", "hejie bulai", "Why are you not coming?"),
                ("这条路通哪里", "zhe tiao lu tong nali", "Where does this road go?"),
                ("我自己去", "wo ziji qu", "I go by myself."),
                ("大家都好", "dajia dou hao", "Everyone is well."),
            ])
        ),
        "how_it_works": (
            "Pronouns work like Mandarin's: 我你他 + 们 for plurals, 的 "
            "for possession (我的书), 这/那 for this/that. The Hunan "
            "flavor comes from three spots: 恁 as the warm respectful "
            "you, 渠 surviving in Old Xiang speech, and the interrogative "
            "set 何解 (why) and 么子 (what) replacing Mandarin 为什么 and "
            "什么 in daily talk. Reflexive 自己 and collective 大家 round "
            "out the system. Drill the paradigm as a chant - 我你他, "
            "我们你们他们 - until it is automatic."
        ),
        "key_points": [
            "Personal: 我/你/他/她/它 + 们 plurals; Old Xiang 渠.",
            "Respectful 恁 (nia), pure Hunan, from 你老人家.",
            "Possessive with 的; demonstratives 这/那/这里/那里.",
            "Interrogatives: 哪个, 么子 (what), 何解 (why).",
            "Reflexive 自己; collective 大家.",
            "20 paradigm sentences, one per form.",
        ],
        "requirements": [
            "Chant the six personal pronouns until automatic.",
            "Use 恁 with elders and strangers; never with close friends.",
        ],
        "standards": [
            "Paradigm follows documented Changsha/Hunan usage; 恁 per Hunan cultural records.",
            SENT_NOTE,
        ],
        "citations": [CIT_HUNAN, CIT_WU, CIT_ZHWIKI],
        "must_contain": ["恁", "渠", "么子", "何解", "的", "们"],
        "sig_lens": (
            "Through the Signature lens pronouns are sworn pointers: 恁 "
            "is the sealed bow of respect, 渠 the heirloom pointer of Old "
            "Xiang, each one a covenant of whom the sentence serves."
        ),
        "drill": {
            "personal": ["我", "你", "他", "她", "它"],
            "plural": ["我们", "你们", "他们"],
            "hunan_marks": ["恁", "渠", "么子", "何解"],
            "sentences": 20,
        },
    },
    {
        "key": "numbers",
        "name": "Xiang Chinese Numbers and Time",
        "group": "Core Vocabulary",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Counting, ordinals, clock time, days, months, seasons, and "
            "dates - the full number-and-time toolkit. Xiang numbers match "
            "Mandarin characters; say them with Changsha tones. \n\n"
            "Numbers 1-10, 11-20, tens, hundreds:\n"
            + _vlines([
                ("一", "yi", "one"), ("二", "er", "two"), ("三", "san", "three"),
                ("四", "si", "four"), ("五", "wu", "five"), ("六", "liu", "six"),
                ("七", "qi", "seven"), ("八", "ba", "eight"), ("九", "jiu", "nine"),
                ("十", "shi", "ten"), ("十一", "shiyi", "eleven"), ("二十", "ershi", "twenty"),
                ("三十", "sanshi", "thirty"), ("一百", "yibai", "one hundred"),
                ("一千", "yiqian", "one thousand"), ("一万", "yiwan", "ten thousand"),
            ]) + "\n\n"
            "Time words:\n"
            + _vlines([
                ("今日子", "jinrizi", "today"),
                ("明日子", "mingrizi", "tomorrow"),
                ("前天", "qiantian", "the day before yesterday"),
                ("先前天", "xianqiantian", "three days ago"),
                ("晏后天", "yanhoutian", "three days later"),
                ("断黑", "duanhei", "dusk, nightfall"),
                ("夜嘎子", "yegazi", "night"),
                ("早上", "zaoshang", "morning"),
                ("中午", "zhongwu", "noon"),
                ("下午", "xiawu", "afternoon"),
                ("点", "dian", "o'clock"), ("分", "fen", "minute"), ("半", "ban", "half"),
                ("星期一", "xingqiyi", "Monday"), ("星期天", "xingqitian", "Sunday"),
                ("一月", "yiyue", "January"), ("十二月", "shieryue", "December"),
                ("春天", "chuntian", "spring"), ("夏天", "xiatian", "summer"),
                ("秋天", "qiutian", "autumn"), ("冬天", "dongtian", "winter"),
            ]) + "\n\n"
            "Sentences:\n"
            + _slines([
                ("一二三四五", "yiersansiwu", "One two three four five."),
                ("我有三个细伢子", "wo you sange xiyazi", "I have three kids."),
                ("好钱一斤", "haojian yijin", "How much is one jin?"),
                ("十块钱一碗", "shikuai qian yiwan", "Ten kuai a bowl."),
                ("第一名是湖南人", "diyiming shi hunanren", "First place is a Hunan person."),
                ("今日子天气好", "jinrizi tianqi hao", "The weather is good today."),
                ("明日子我来", "mingrizi wo lai", "I will come tomorrow."),
                ("断黑了回家恰饭", "duanheile huijia qiafan", "Night is falling, go home and eat."),
                ("夜嘎子早点睡", "yegazi zaodian shui", "Sleep early at night."),
                ("早上七点起床", "zaoshang qidian qichuang", "Get up at seven in the morning."),
                ("中午恰辣椒炒肉", "zhongwu qia lajiao chaorou", "At noon eat stir-fried pork with chilies."),
                ("下午三点半开会", "xiawu sandianban kaihui", "Meeting at half past three in the afternoon."),
                ("星期天去爬岳麓山", "xingqitian qu pa yuelushan", "On Sunday go climb Yuelu Mountain."),
                ("今年春节回长沙", "jinnian chunjie hui changsha", "This year return to Changsha for Spring Festival."),
                ("夏天蛮热冬天蛮冷", "xiatian banre dongtian banleng", "Summer is very hot, winter very cold."),
                ("九月开学", "jiuyue kaixue", "School starts in September."),
                ("我等了半个钟头", "wo dengle bange zhongtou", "I waited half an hour."),
                ("先前天落了雨", "xianqiantian luole yu", "It rained three days ago."),
                ("晏后天有空冇", "yanhoutian youkong mao", "Are you free three days from now?"),
                ("一九九九年出生", "yijiujiujiu nian chusheng", "Born in 1999."),
            ])
        ),
        "how_it_works": (
            "Numbers build by place value exactly like Mandarin: 二十 "
            "is two-ten, 三十五 is three-ten-five, 一百二十三 is "
            "one-hundred-two-ten-three. Ordinals add 第 (第一, 第二). "
            "Clock time is number + 点 + number + 分, with 半 for half "
            "and 刻 for quarter in older speech. The Xiang signature set "
            "is the day words: 今日子, 明日子, 先前天, 晏后天, 断黑, "
            "夜嘎子 - learn them as one block and your time talk turns "
            "Hunan overnight. Months are number + 月; seasons are the "
            "shared 春夏秋冬."
        ),
        "key_points": [
            "1-10, teens, tens, 百/千/万; ordinals with 第.",
            "Clock time: 点/分/半; dates: 年/月/日.",
            "Signature day words: 今日子, 明日子, 前天, 先前天, 晏后天, 断黑, 夜嘎子.",
            "Months: number + 月; weekdays: 星期 + number.",
            "Seasons 春夏秋冬; 20 time-use sentences.",
        ],
        "requirements": [
            "Count 1-100 aloud with Changsha tones before the time sentences.",
            "Learn the seven signature day words as one block.",
        ],
        "standards": [
            "Day words follow the documented Changsha tables.",
            SENT_NOTE,
        ],
        "citations": [CIT_ZHWIKI, CIT_WU],
        "must_contain": ["今日子", "明日子", "断黑", "夜嘎子", "点", "第"],
        "sig_lens": (
            "Through the Signature lens numbers are sworn tallies and "
            "day-words sealed appointments: 今日子 stamps today, 断黑 "
            "seals the dusk, each a covenant that time will be kept in "
            "Hunan measure."
        ),
        "drill": {
            "digits": 10, "day_words": ["今日子", "明日子", "前天", "先前天", "晏后天", "断黑", "夜嘎子"],
            "seasons": ["春天", "夏天", "秋天", "冬天"],
            "months": 12, "sentences": 20,
        },
    },
    {
        "key": "greetings",
        "name": "Xiang Chinese Greetings and Everyday Phrases",
        "group": "Core Vocabulary",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Thirty (30) greetings, farewells, and politeness phrases - the "
            "social oil of Hunan. The classic Hunan greeting is not 你好 "
            "but 恰饭了冇 (have you eaten?). Sentence-final 啵 turns "
            "statements into warm questions: 晓得啵 (you know, right?). \n\n"
            + _slines([
                ("你好", "nihao", "Hello!"),
                ("恰饭了冇", "qiafanle mao", "Have you eaten yet? [the Hunan hello]"),
                ("好久不见", "haojiebujian", "Long time no see."),
                ("早", "zao", "Morning!"),
                ("晚安", "wanan", "Good night."),
                ("再见", "zaijian", "Goodbye."),
                ("慢走", "manzou", "Take care (to a departing guest)."),
                ("一路顺风", "yilushunfeng", "Have a smooth trip."),
                ("谢谢", "xiexie", "Thank you."),
                ("多谢", "duoxie", "Many thanks."),
                ("对不起", "duibuqi", "Sorry."),
                ("不好意思", "buhaoyisi", "Excuse me / pardon."),
                ("冇关系", "mao guanxi", "It does not matter."),
                ("欢迎", "huanying", "Welcome."),
                ("请坐", "qingzuo", "Please sit."),
                ("请喝茶", "qing he cha", "Please have some tea."),
                ("晓得啵", "xiaode bo", "You know, right?"),
                ("好啵", "hao bo", "Is that OK?"),
                ("莫客气", "mo keqi", "Do not stand on ceremony."),
                ("恭喜", "gongxi", "Congratulations."),
                ("生日快乐", "shengrikuaile", "Happy birthday."),
                ("新年好", "xinnianhao", "Happy New Year."),
                ("恰好喝好", "qiahao hehao", "Eat and drink well."),
                ("有空来耍", "youkong lai shua", "Come visit when free."),
                ("路上小心", "lushang xiaoxin", "Be careful on the road."),
                ("身体保重", "shenti baozhong", "Take care of your health."),
                ("莫急", "moji", "Do not rush."),
                ("放心", "fangxin", "Rest assured."),
                ("要得", "yaode", "OK, deal."),
                ("下次再来", "xiaci zailai", "Come again next time."),
            ])
        ),
        "how_it_works": (
            "Greetings run on food and care: 恰饭了冇 asks after the "
            "stomach because in Hunan memory a full stomach was never "
            "guaranteed. 啵 is the warmth particle - append it to soften "
            "any question (晓得啵, 好啵). Farewells bless the journey "
            "(慢走, 一路顺风); thanks escalate from 谢谢 to 多谢; "
            "apologies run 对不起 for real faults and 不好意思 for small "
            "intrusions. 要得 seals agreement the Hunan way. Use 莫客气 "
            "the moment anyone thanks you."
        ),
        "key_points": [
            "30 greetings/farewells/politeness phrases with usage notes.",
            "恰饭了冇 is the signature Hunan greeting.",
            "啵 softens questions: 晓得啵, 好啵.",
            "Farewells: 慢走, 一路顺风, 下次再来.",
            "Thanks: 谢谢/多谢; apologies: 对不起/不好意思; answer: 莫客气.",
            "Agreement: 要得; reassurance: 放心, 莫急.",
        ],
        "requirements": [
            "Greet three people with 恰饭了冇 before using 你好 again.",
            "End every question with 啵 for one full day of practice.",
        ],
        "standards": [
            "Phrases follow documented Hunan/Changsha usage.",
            SENT_NOTE,
        ],
        "citations": [CIT_HUNAN, CIT_ZHWIKI],
        "must_contain": ["恰饭了冇", "啵", "慢走", "要得", "莫客气", "30"],
        "sig_lens": (
            "Through the Signature lens every greeting is a sworn "
            "welcome: 恰饭了冇 seals the table, 慢走 seals the road, and "
            "啵 is the warm wax stamp on every question."
        ),
        "drill": {
            "count": 30,
            "food_greetings": ["恰饭了冇", "恰好喝好"],
            "bo_questions": ["晓得啵", "好啵"],
            "farewells": ["慢走", "一路顺风", "下次再来"],
        },
    },
    {
        "key": "grammar",
        "name": "Xiang Chinese Grammar Essentials",
        "group": "Grammar Essentials",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The ten load-bearing rules of Xiang grammar, each with "
            "translated example sentences. No conjugations, no cases, no "
            "gender - the engine is word order plus particles. \n\n"
            "Rule 1 - SVO word order. Subject, verb, object, always:\n"
            "  我喫饭 (wo qia fan) - I eat rice.\n"
            "  他买辣椒 (ta mai lajiao) - He buys chilies.\n\n"
            "Rule 2 - No verb inflection. Time comes from aspect "
            "particles and time words:\n"
            "  我昨日喫了 (wo zuori qiale) - I ate yesterday.\n"
            "  我明日子喫 (wo mingrizi qia) - I will eat tomorrow.\n\n"
            "Rule 3 - Classifiers between number and noun:\n"
            "  一个人 (yige ren) - one person\n"
            "  一只鸡 (yizhi ji) - one chicken\n"
            "  一坨肉 (yituo rou) - one lump of meat [坨 is the Hunan lump-classifier]\n\n"
            "Rule 4 - Negation trio: 不 (general), 冇 (not have), 莫 "
            "(prohibitive):\n"
            "  我不去 (wo buqu) - I am not going.\n"
            "  我冇钱 (wo mao qian) - I have no money.\n"
            "  莫讲 (mo jiang) - Do not speak.\n\n"
            "Rule 5 - Questions: 吗/啵/呢 endings, or question words:\n"
            "  你去啵 (ni qu bo) - Are you going?\n"
            "  何解不来 (hejie bulai) - Why are you not coming?\n"
            "  好钱 (haojian) - How much money?\n\n"
            "Rule 6 - Aspect particles after the verb: 了 (completed), "
            "着 (durative), 过 (experiential), 咖 (perfective, Old Xiang):\n"
            "  喫了 (qiale) - ate\n"
            "  喫咖 (qiaga) - ate (Old Xiang perfective)\n"
            "  见过 (jianguo) - have seen\n\n"
            "Rule 7 - 的 for possession and attribution:\n"
            "  我的书 (wode shu) - my book\n"
            "  湖南的辣椒 (hunande lajiao) - Hunan's chilies\n\n"
            "Rule 8 - 把 moves the object before the verb:\n"
            "  把门关好 (ba men guanhao) - Shut the door well.\n"
            "  把饭恰了 (ba fan qiale) - Eat up the rice.\n\n"
            "Rule 9 - Comparison with 比:\n"
            "  辣椒比生姜辣 (lajiao bi shengjiang la) - Chilies are spicier than ginger.\n"
            "  长沙比我家大 (changsha bi wojia da) - Changsha is bigger than my hometown.\n\n"
            "Rule 10 - Sentence-final particles set the mood: 啵 "
            "(warm question), 咯 (obviousness), 撒 (suggestion), 啦 "
            "(change of state), 哒 (completion):\n"
            "  晓得啵 (xiaode bo) - You know, right?\n"
            "  就是咯 (jiushi lo) - Exactly, of course.\n"
            "  走撒 (zou sa) - Let us go, shall we?\n"
            "  落雨啦 (luoyu la) - It has started raining.\n"
            "  喫完哒 (qiwanda) - All eaten up."
        ),
        "how_it_works": (
            "The grammar engine has two moving parts: rigid SVO order and "
            "a cloud of little particles. Verbs never change shape; "
            "instead 了/咖/着/过 after the verb tell you done, ongoing, "
            "or experienced, while 不/冇/莫 before the verb tell you no. "
            "Classifiers (个/只/条/坨) are mandatory between numbers and "
            "nouns. Sentence-final particles (啵/咯/撒/啦/哒) are the "
            "emotional steering wheel - master them and your Xiang turns "
            "from textbook to human. Questions need no word-order change: "
            "add 啵 or a question word and the intonation does the rest."
        ),
        "key_points": [
            "Rule 1: strict SVO; Rule 2: no verb inflection.",
            "Rule 3: classifiers (个/只/条/坨) between number and noun.",
            "Rule 4: negation trio 不/冇/莫.",
            "Rule 5: questions via 吗/啵/呢 or question words (何解, 好钱).",
            "Rule 6: aspect particles 了/着/过/咖 (咖 = Old Xiang perfective).",
            "Rule 7: 的 possession/attribution; Rule 8: 把 construction.",
            "Rule 9: 比 comparison; Rule 10: final particles 啵/咯/撒/啦/哒.",
        ],
        "requirements": [
            "Build 10 SVO sentences before touching particles.",
            "Drill 不/冇/莫 and 啵/咯/撒/啦/哒 as two separate particle blocks.",
        ],
        "standards": [
            "Grammar follows Wu 2005, the reference grammar of Xiang dialects.",
            "Aspect particle 咖 per the documented Xiang aspect studies.",
            SENT_NOTE,
        ],
        "citations": [CIT_WU, CIT_NORMAN],
        "must_contain": ["SVO", "Classifiers", "冇", "莫", "咖", "啵", "把"],
        "sig_lens": (
            "Through the Signature lens grammar is the sworn machinery "
            "of meaning: SVO the straight rail, particles the sealed "
            "switches, and 啵 the warm bell that rings at the end of "
            "every kind question."
        ),
        "drill": {
            "rules": 10,
            "negation": ["不", "冇", "莫"],
            "aspect": ["了", "着", "过", "咖"],
            "final_particles": ["啵", "咯", "撒", "啦", "哒"],
            "classifiers": ["个", "只", "条", "坨"],
            "example_sentences": 26,
        },
    },
]
ENTRIES += [
    {
        "key": "home",
        "name": "Xiang Chinese Home and Family Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Twenty (20) sentences for house, rooms, furniture, and family - "
            "the first theme set. Family words reuse the kinship nouns; "
            "new home words are introduced inline. \n\n"
            + _slines([
                ("我家在长沙", "wojia zai changsha", "My home is in Changsha."),
                ("屋里有三间房", "wuli you sanjian fang", "The house has three rooms."),
                ("堂客在厨房恰饭", "tangke zai chufang qiafan", "My wife is eating in the kitchen."),
                ("娭毑坐在堂屋里", "aijie zuo zai tangwuli", "Grandma is sitting in the main hall."),
                ("嗲嗲爱看电视", "diadie ai kan dianshi", "Grandpa loves watching TV."),
                ("细伢子在房间做作业", "xiyazi zai fangjian zuo zuoye", "The kid is doing homework in the bedroom."),
                ("把桌子擦干净", "ba zhuozi ca ganjing", "Wipe the table clean."),
                ("椅子坏了买新的", "yizi huaile mai xinde", "The chair broke; buy a new one."),
                ("床蛮舒服", "chuang banshufu", "The bed is very comfortable."),
                ("门冇关好", "men mao guanhao", "The door is not shut well."),
                ("窗户打开透气", "chuanghu dakai touqi", "Open the window for air."),
                ("姆妈在洗衣服", "muma zai xi yifu", "Mom is washing clothes."),
                ("爷去上班了", "ye qu shangbanle", "Dad went to work."),
                ("我们一家五口人", "women yijia wukou ren", "Our family is five people."),
                ("晚上全家一起恰饭", "wanshang quanjia yiqi qiafan", "At night the whole family eats together."),
                ("细姑明天来看娭毑", "xigu mingtian lai kan aijie", "Younger aunt comes to see grandma tomorrow."),
                ("崽的房间蛮乱", "zaide fangjian banluan", "My son's room is very messy."),
                ("把垃圾倒了", "ba laji daole", "Take out the trash."),
                ("灯冇关", "deng mao guan", "The light is not off."),
                ("屋里好暖和", "wuli haonuanhuo", "The house is so warm and cozy."),
            ])
        ),
        "how_it_works": (
            "Theme sets recycle earlier vocabulary inside full sentences, "
            "so every new word arrives in a lived context. Home sentences "
            "lean on location with 在 (在长沙, 在厨房), existence with "
            "有 (有三间房), and the 把 construction for chores (把桌子擦"
            "干净). Kinship terms from the nouns record return as the "
            "cast of characters. Read each sentence, cover the English, "
            "and translate back before moving on."
        ),
        "key_points": [
            "20 home-and-family sentences, each translated.",
            "Location with 在; existence with 有; chores with 把.",
            "Kinship cast returns: 堂客, 娭毑, 嗲嗲, 细伢子, 崽, 细姑.",
            "Home words: 堂屋, 厨房, 房间, 桌子, 椅子, 床, 门, 窗户.",
            "Ladder step: first theme set, foundations tier.",
        ],
        "requirements": [
            "Know the kinship nouns before this record.",
            "Translate each sentence both directions before the next theme.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_ZHWIKI, CIT_WU],
        "must_contain": ["20", "在", "有", "把", "堂屋", "厨房"],
        "sig_lens": (
            "Through the Signature lens the home is the first sealed "
            "territory: every room a sworn chamber, every family sentence "
            "a covenant spoken under one roof."
        ),
        "drill": {"sentences": 20, "theme": "home-family", "new_words": 12},
    },
    {
        "key": "food",
        "name": "Xiang Chinese Food and Cooking Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty (20) sentences for meals, ingredients, cooking actions, and "
            "the restaurant - in the province that fears no spice. "
            "四川人不怕辣，湖南人怕不辣: Sichuan people do not fear "
            "spice, Hunan people fear the lack of it. \n\n"
            + _slines([
                ("恰饭了冇", "qiafanle mao", "Have you eaten yet?"),
                ("今日子恰么子", "jinrizi qia mezi", "What are we eating today?"),
                ("来碗辣椒炒肉", "lai wan lajiao chaorou", "A bowl of stir-fried pork with chilies."),
                ("这个菜蛮辣", "zhege cai banla", "This dish is very spicy."),
                ("少放点辣椒", "shao fang dian lajiao", "Put in less chili."),
                ("臭干子再来一份", "chouganzi zailai yifen", "One more serving of stinky tofu."),
                ("鱼要蒸起恰", "yu yao zhengqi qia", "The fish should be eaten steamed."),
                ("肉切细一点", "rou qie xidianyidian", "Cut the meat a bit thinner."),
                ("先把米洗干净", "xian ba mi xi ganjing", "Wash the rice clean first."),
                ("锅里倒点油", "guoli dao dian you", "Pour some oil in the wok."),
                ("火开大一点", "huo kaida yidian", "Turn the flame up a bit."),
                ("盐放多了", "yan fangduole", "Too much salt was added."),
                ("汤蛮鲜", "tang banxian", "The soup is very savory."),
                ("米饭煮熟了冇", "mifan zhushule mao", "Is the rice cooked?"),
                ("我不恰肥肉", "wo buqia feirou", "I do not eat fatty meat."),
                ("他爱恰酸的", "ta ai qia suande", "He likes sour food."),
                ("服务员买单", "fuwuyuan maidan", "Waiter, the bill please."),
                ("打包带走", "dabao daizou", "Pack it to go."),
                ("味道好极了", "weidao haojile", "The flavor is excellent."),
                ("下次还来恰", "xiaci hailai qia", "Will come eat here again."),
            ])
        ),
        "how_it_works": (
            "Food sentences drill the cooking verb chain - 洗 (wash), 切 "
            "(cut), 倒 (pour), 放 (add), 蒸 (steam), 煮 (boil), 炒 "
            "(stir-fry) - each appearing with its object, because Xiang "
            "cooking verbs are almost always transitive. Restaurant "
            "language (买单, 打包) and spice negotiation (少放点辣椒, "
            "蛮辣) are the survival core. The 把 construction organizes "
            "kitchen work: 把米洗干净, 把肉切细. Taste words run 辣/甜/"
            "咸/酸/苦/鲜."
        ),
        "key_points": [
            "20 food-and-cooking sentences, each translated.",
            "Cooking verb chain: 洗/切/倒/放/蒸/煮/炒.",
            "Spice talk: 蛮辣, 少放点辣椒; the Hunan spice pride line.",
            "Restaurant survival: 买单, 打包, 再来一份.",
            "Taste words: 辣/甜/咸/酸/苦/鲜.",
        ],
        "requirements": [
            "Know 喫/恰 and the negation trio before this record.",
            "Practice ordering a full meal aloud: dish, spice level, bill.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_HUNAN, CIT_ZHWIKI],
        "must_contain": ["20", "辣椒", "买单", "打包", "怕不辣", "炒"],
        "sig_lens": (
            "Through the Signature lens the Hunan table is a sworn "
            "feast: every chili a sealed flame, every 恰饭 a covenant "
            "that no guest leaves hungry."
        ),
        "drill": {"sentences": 20, "theme": "food-cooking",
                  "cooking_verbs": ["洗", "切", "倒", "放", "蒸", "煮", "炒"],
                  "tastes": ["辣", "甜", "咸", "酸", "苦", "鲜"]},
    },
    {
        "key": "travel",
        "name": "Xiang Chinese Travel and Directions Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty (20) sentences for transport, asking directions, tickets, "
            "and lodging - the traveler's survival set for Hunan. \n\n"
            + _slines([
                ("去岳麓山啷个走", "qu yuelushan langge zou", "How do I get to Yuelu Mountain?"),
                ("一直往前走", "yizhi wangqian zou", "Go straight ahead."),
                ("到红绿灯左转", "dao honglvdeng zuozhuan", "Turn left at the traffic light."),
                ("前面右转就到了", "qianmian youzhuan jiudaole", "Turn right ahead and you are there."),
                ("离这里远啵", "li zheli yuan bo", "Is it far from here?"),
                ("走路要半个钟头", "zoulu yao bange zhongtou", "On foot it takes half an hour."),
                ("坐地铁快些", "zuo ditie kuaixie", "The subway is faster."),
                ("几路车到火车站", "jilu che dao huochezhan", "Which bus goes to the railway station?"),
                ("打的要好多钱", "dade yao haoduo qian", "How much is a taxi?"),
                ("买两张去长沙的票", "mai liangzhang qu changshade piao", "Two tickets to Changsha."),
                ("车子几时开", "chezi jishi kai", "When does the bus leave?"),
                ("莫坐黑脑壳", "mo zuo heinaoke", "Do not take unlicensed taxis."),
                ("酒店在哪里", "jiudian zai nali", "Where is the hotel?"),
                ("订了一个房间", "dingle yige fangjian", "Booked a room."),
                ("有热水冇", "you reshui mao", "Is there hot water?"),
                ("退房是几时", "tuifang shi jishi", "When is checkout?"),
                ("我的行李在车上", "wode xingli zai cheshang", "My luggage is on the bus."),
                ("请帮我叫辆车", "qing bangwo jiao liangche", "Please call me a car."),
                ("路上小心", "lushang xiaoxin", "Be careful on the road."),
                ("到了给我打电话", "daole geiwo da dianhua", "Call me when you arrive."),
            ])
        ),
        "how_it_works": (
            "Direction sentences run on the motion verbs 来/去/走/转 "
            "plus landmarks (红绿灯, 火车站, 酒店). 啷个/啷个走 asks "
            "how-to-go; 好多钱 asks price; 几时 asks time - the three "
            "traveler questions. Transport words stack simply: 坐地铁, "
            "打的, 坐车. Warnings use 莫 (莫坐黑脑壳). Requests soften "
            "with 请. Drill by walking a real route in your head and "
            "narrating it in Xiang."
        ),
        "key_points": [
            "20 travel-and-direction sentences, each translated.",
            "Three traveler questions: 啷个 (how), 好多钱 (how much), 几时 (when).",
            "Direction verbs: 走/转/到; landmarks: 红绿灯/火车站/酒店.",
            "Transport: 坐地铁, 打的, 买票; lodging: 订房/退房/热水.",
            "Warning with 莫; requests with 请.",
        ],
        "requirements": [
            "Know the number and time words before this record.",
            "Narrate one real route in Xiang from memory.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_ZHWIKI],
        "must_contain": ["20", "啷个", "好多钱", "几时", "黑脑壳", "岳麓山"],
        "sig_lens": (
            "Through the Signature lens every journey is a sworn "
            "passage: each direction a sealed instruction, each ticket a "
            "covenant that the traveler will arrive."
        ),
        "drill": {"sentences": 20, "theme": "travel-directions",
                  "traveler_questions": ["啷个", "好多钱", "几时"]},
    },
    {
        "key": "work",
        "name": "Xiang Chinese Work and School Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twenty (20) sentences for jobs, the office, the classroom, and "
            "learning - work talk with the 霸蛮 spirit. \n\n"
            + _slines([
                ("你做么子工作", "ni zuo mezi gongzuo", "What work do you do?"),
                ("我在工厂上班", "wo zai gongchang shangban", "I work at a factory."),
                ("他是老师", "ta shi laoshi", "He is a teacher."),
                ("会议几时开", "huiyi jishi kai", "When is the meeting?"),
                ("把报告写好", "ba baogao xiehao", "Write the report well."),
                ("这个项目蛮重要", "zhege xiangmu banzhongyao", "This project is very important."),
                ("加班到夜嘎子", "jiaban dao yegazi", "Overtime until night."),
                ("工资几时发", "gongzi jishi fa", "When is payday?"),
                ("老板人蛮好", "laoban ren banhao", "The boss is very nice."),
                ("同事都蛮热情", "tongshi dou banreqing", "The colleagues are all warm."),
                ("细伢子在读书", "xiyazi zai dushu", "The kid is studying."),
                ("上课莫打野", "shangke mo daye", "Do not lose focus in class."),
                ("这道题啷个做", "zhe dao ti langge zuo", "How do you solve this problem?"),
                ("考试考得蛮好", "kaoshi kaode banhao", "The exam went very well."),
                ("老师讲得清楚", "laoshi jiangde qingchu", "The teacher explains clearly."),
                ("放学了回家恰饭", "fangxuele huijia qiafan", "School is out; go home and eat."),
                ("做事要霸蛮", "zuoshi yao baman", "At work, be tough and can-do."),
                ("吃得苦耐得烦", "chideku naidefan", "Endure hardship, endure tedium."),
                ("把事情圆功", "ba shiqing yuangong", "Finish the job well."),
                ("明天继续努力", "mingtian jixu nuli", "Keep working hard tomorrow."),
            ])
        ),
        "how_it_works": (
            "Work sentences pair job nouns (工厂, 会议, 报告, 项目, "
            "工资, 老板, 同事) with the 打-family and 霸蛮 verbs: 架场 "
            "a meeting, 圆功 a project, 莫打哑 at the desk. School "
            "sentences reuse 上课/放学/考试/作业 with classroom "
            "discipline in 莫打野. The Hunan work ethic lines (做事要霸"
            "蛮, 吃得苦耐得烦) are not decoration - they are how Hunan "
            "people actually talk about work. Drill by describing your "
            "own job in ten Xiang sentences."
        ),
        "key_points": [
            "20 work-and-school sentences, each translated.",
            "Job nouns: 工厂/会议/报告/项目/工资/老板/同事.",
            "霸蛮 work verbs: 架场, 圆功, 莫打哑.",
            "School: 上课/放学/考试/作业; discipline: 莫打野.",
            "Work-ethic lines: 做事要霸蛮, 吃得苦耐得烦.",
        ],
        "requirements": [
            "Know the verbs record before this record.",
            "Describe your own job in ten Xiang sentences.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_HUNAN, CIT_ZHWIKI],
        "must_contain": ["20", "霸蛮", "打野", "圆功", "工资", "考试"],
        "sig_lens": (
            "Through the Signature lens work is a sworn craft: every "
            "report a sealed document, every 圆功 a covenant that the job "
            "was finished properly."
        ),
        "drill": {"sentences": 20, "theme": "work-school",
                  "work_verbs": ["架场", "圆功", "打哑"]},
    },
    {
        "key": "health",
        "name": "Xiang Chinese Health and Body Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty (20) sentences for body parts, symptoms, the doctor visit, "
            "and the pharmacy - health talk that reuses the body nouns. \n\n"
            + _slines([
                ("我脑壳疼", "wo naoke teng", "My head hurts."),
                ("喉咙不舒服", "houlong bushufu", "My throat feels bad."),
                ("有点发烧", "youdian fashao", "I have a bit of a fever."),
                ("咳嗽了几天", "kesoule jitian", "I have coughed for days."),
                ("肚子疼得厉害", "duzi tengde lihai", "My stomach hurts badly."),
                ("膝头骨扭了", "xitougu niule", "I twisted my knee."),
                ("手巴子抬不起来", "shoubazi taibuqilai", "I cannot lift my arm."),
                ("眼睛发炎了", "yanjing fayenle", "My eyes are inflamed."),
                ("去医院看看", "qu yiyuan kankan", "Go see a doctor."),
                ("医生讲冇大事", "yisheng jiang mao dashi", "The doctor says it is nothing serious."),
                ("要打针啵", "yao dazhen bo", "Do I need an injection?"),
                ("开药给我恰", "kaiyao geiwo qia", "Prescribe medicine for me to take."),
                ("这个药啷个恰", "zhege yao langge qia", "How do I take this medicine?"),
                ("饭前恰还是饭后恰", "fanqian qia haishi fanhou qia", "Take before or after meals?"),
                ("多喝热水", "duo he reshui", "Drink more hot water."),
                ("好好休息几天", "haohao xiuxi jitian", "Rest well for a few days."),
                ("莫恰辛辣的", "mo qia xinlade", "Do not eat spicy food."),
                ("早点睡莫熬夜", "zaodian shui mo aoye", "Sleep early, do not stay up late."),
                ("身体好些了冇", "shenti haoxiele mao", "Are you feeling better?"),
                ("保重身体", "baozhong shenti", "Take care of your health."),
            ])
        ),
        "how_it_works": (
            "Symptom sentences follow the pattern body-part + 疼/不舒服/"
            "发炎: 我脑壳疼, 喉咙不舒服. Doctor-visit sentences use 看 "
            "(看看 = take a look), 开药 (prescribe), 打针 (injection). "
            "Dosage questions run 啷个恰 and 饭前/饭后. Advice uses 莫 "
            "plus the verb (莫恰辛辣的, 莫熬夜) and 好好 plus the verb "
            "(好好休息). The check-in question 身体好些了冇 carries the "
            "warm 冇 ending. Drill by describing one ailment fully in "
            "Xiang."
        ),
        "key_points": [
            "20 health-and-body sentences, each translated.",
            "Symptom pattern: body part + 疼/不舒服.",
            "Doctor visit: 看, 开药, 打针; dosage: 啷个恰, 饭前/饭后.",
            "Advice: 莫 + verb; 好好 + verb.",
            "Check-in: 身体好些了冇.",
        ],
        "requirements": [
            "Know the body nouns before this record.",
            "Describe one ailment fully in Xiang.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_ZHWIKI],
        "must_contain": ["20", "脑壳", "打针", "开药", "莫熬夜", "保重"],
        "sig_lens": (
            "Through the Signature lens health talk is sworn care: every "
            "symptom a sealed report, every 好好休息 a covenant of "
            "recovery."
        ),
        "drill": {"sentences": 20, "theme": "health-body",
                  "symptom_parts": ["脑壳", "喉咙", "肚子", "膝头骨", "手巴子", "眼睛"]},
    },
    {
        "key": "emotions",
        "name": "Xiang Chinese Emotions and Feelings Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty (20) sentences for happy, sad, angry, afraid, love, and "
            "surprise - feelings in Hunan color. \n\n"
            + _slines([
                ("我蛮开心", "wo ban kaixin", "I am very happy."),
                ("今日子有喜事", "jinrizi you xishi", "There is happy news today."),
                ("他笑得合不拢嘴", "ta xiaode hebunongzui", "He is grinning from ear to ear."),
                ("我好难过", "wo haonanguo", "I feel so sad."),
                ("莫哭了", "moku le", "Stop crying."),
                ("心里蛮委屈", "xinli banweiqu", "I feel so wronged inside."),
                ("我好生气", "wo haoshenqi", "I am so angry."),
                ("莫跟他呕气", "mo gen ta ouqi", "Do not sulk at him."),
                ("消消气", "xiaoxiaoqi", "Calm down."),
                ("我有点害怕", "wo youdian haipa", "I am a bit afraid."),
                ("莫怕有我在", "mopa youwo zai", "Do not fear, I am here."),
                ("我爱你", "wo aini", "I love you."),
                ("我蛮喜欢你", "wo banxihuan ni", "I like you very much."),
                ("好感动", "haogandong", "So touching."),
                ("吓我一跳", "xiawo yitiao", "You startled me."),
                ("真是没想到", "zhenshi meixiangdao", "Really did not expect it."),
                ("心里暖暖的", "xinli nuannuande", "My heart feels warm."),
                ("蛮有面子", "banyoumianzi", "It brings great honor."),
                ("莫往心里去", "mo wang xinli qu", "Do not take it to heart."),
                ("一切都会好的", "yiqie douhui haode", "Everything will be fine."),
            ])
        ),
        "how_it_works": (
            "Emotion sentences center on 心 (heart) as the seat of "
            "feeling: 心里暖暖的, 莫往心里去, 心里蛮委屈. Intensity "
            "runs on 蛮/好/有点: 我蛮开心, 我好生气, 有点害怕. "
            "Comfort uses 莫 + verb (莫哭了, 莫怕) and reassurance "
            "patterns (有我在, 都会好的). The social emotions - 面子 "
            "(face), 委屈 (grievance), 呕气 (sulking) - are drilled "
            "with their exact verbs. Say each feeling sentence with the "
            "matching face; the tones carry the emotion."
        ),
        "key_points": [
            "20 emotion sentences: happy, sad, angry, afraid, love, surprise.",
            "心 as the seat of feeling; intensity with 蛮/好/有点.",
            "Comfort: 莫 + verb; reassurance: 有我在, 都会好的.",
            "Social emotions: 面子, 委屈, 呕气, 感动.",
            "Tones carry the emotion - say each with feeling.",
        ],
        "requirements": [
            "Know the adjective/adverb intensifiers before this record.",
            "Say each sentence with the matching facial expression.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_WU],
        "must_contain": ["20", "心里", "蛮开心", "好生气", "我爱你", "莫哭"],
        "sig_lens": (
            "Through the Signature lens feelings are sworn weather of "
            "the heart: every 开心 a sealed sunrise, every 莫怕 a "
            "covenant of shelter."
        ),
        "drill": {"sentences": 20, "theme": "emotions-feelings",
                  "emotion_set": ["开心", "难过", "生气", "害怕", "爱", "惊讶"]},
    },
    {
        "key": "nature",
        "name": "Xiang Chinese Nature and Weather Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Twenty (20) sentences for animals, plants, seasons, and weather "
            "talk - Hunan's rivers, mountains, and rain. \n\n"
            + _slines([
                ("今日子天气蛮好", "jinrizi tianqi banhao", "The weather is very good today."),
                ("落雨了带伞", "luoyule dai san", "It is raining; bring an umbrella."),
                ("雨落得好大", "yu luode haoda", "The rain is falling hard."),
                ("天放晴了", "tian fangqingle", "The sky cleared up."),
                ("夏天蛮热", "xiatian banre", "Summer is very hot."),
                ("冬天下雪了", "dongtian xiaxuele", "It snowed in winter."),
                ("起风了多穿点", "qifengle duo chuan dian", "It is windy; wear more."),
                ("湘江的水好清", "xiangjiangde shui haoqing", "The Xiang River water is so clear."),
                ("岳麓山上蛮多树", "yuelushanshang banduo shu", "Yuelu Mountain has so many trees."),
                ("橘子洲头看江景", "juzizhoutou kan jiangjing", "Watch the river view at Orange Isle."),
                ("田里禾苗长得好", "tianli hemiao zhangde hao", "The rice seedlings grow well in the fields."),
                ("荷花开了", "hehua kaile", "The lotuses bloomed."),
                ("山上好多鸟叫", "shanshang haoduo niao jiao", "So many birds sing on the mountain."),
                ("水牛在田里", "shuiniu zai tianli", "The water buffalo is in the field."),
                ("鸡在院子里跑", "ji zai yuanzili pao", "The chickens run in the yard."),
                ("狗对到生人叫", "gou duidao shengren jiao", "The dog barks at strangers."),
                ("猫在晒太阳", "mao zai shai taiyang", "The cat is sunbathing."),
                ("鱼在水里游", "yu zai shuili you", "The fish swim in the water."),
                ("春天花都开了", "chuntian hua dou kaile", "In spring all the flowers bloomed."),
                ("秋天是丰收的季节", "qiutian shi fengshoude jijie", "Autumn is the harvest season."),
            ])
        ),
        "how_it_works": (
            "Weather sentences use the weather-word + verb pattern: 落雨 "
            "了 (rained), 天放晴了 (cleared), 起风了 (wind rose) - "
            "weather does the action, no dummy subject needed. Nature "
            "nouns (湘江, 岳麓山, 橘子洲, 田, 荷花) anchor every sentence "
            "in real Hunan geography. Animal sentences pair the animal "
            "with its signature verb: 鸟叫, 狗叫, 鱼游, 猫晒太阳. Season "
            "sentences reuse 春夏秋冬 with the weather they bring. Drill "
            "by describing today's actual weather in five Xiang sentences."
        ),
        "key_points": [
            "20 nature-and-weather sentences, each translated.",
            "Weather pattern: weather-word + verb (落雨了, 天放晴了).",
            "Hunan geography anchors: 湘江, 岳麓山, 橘子洲.",
            "Animal + signature verb: 鸟叫, 狗叫, 鱼游.",
            "Seasons with their weather; farm words: 田, 禾苗, 水牛.",
        ],
        "requirements": [
            "Know the season words before this record.",
            "Describe today's real weather in five Xiang sentences.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_ENWIKI],
        "must_contain": ["20", "落雨", "湘江", "岳麓山", "橘子洲", "禾苗"],
        "sig_lens": (
            "Through the Signature lens nature is the sworn backdrop: "
            "the 湘江 seals the province's pulse, every 落雨 a covenant "
            "that the fields will drink."
        ),
        "drill": {"sentences": 20, "theme": "nature-weather",
                  "hunan_places": ["湘江", "岳麓山", "橘子洲"],
                  "weather_verbs": ["落雨", "放晴", "起风", "下雪"]},
    },
    {
        "key": "shopping",
        "name": "Xiang Chinese Shopping and Money Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty (20) sentences for the market, prices, bargaining, and "
            "paying - including the signature price question 好钱. \n\n"
            + _slines([
                ("这个好钱", "zhege haojian", "How much is this?"),
                ("辣椒好钱一斤", "lajiao haojian yijin", "How much are chilies per jin?"),
                ("太贵了便宜点", "taiguile pianyi dian", "Too expensive; make it cheaper."),
                ("再少一点啵", "zaishao yidian bo", "A little less, OK?"),
                ("最低好多", "zuidi haoduo", "What is the lowest price?"),
                ("五块卖啵", "wukuai mai bo", "Sell it for five kuai?"),
                ("成交", "chengjiao", "Deal."),
                ("我买两斤", "wo mai liangjin", "I will buy two jin."),
                ("称高一点", "cheng gaoyidian", "Weigh a bit generously."),
                ("找我五块钱", "zhaowo wukuai qian", "Give me five kuai change."),
                ("可以刷卡啵", "keyi shuaka bo", "Can I pay by card?"),
                ("扫码付款", "saoma fukuan", "Pay by scanning the code."),
                ("现金冇带够", "xianjin mao daigou", "I did not bring enough cash."),
                ("开发票", "kai fapiao", "Issue a receipt."),
                ("这个新鲜啵", "zhege xinxian bo", "Is this fresh?"),
                ("刚摘的", "gangzhaide", "Just picked."),
                ("买点水果回去", "maidian shuiguo huiqu", "Buy some fruit to take home."),
                ("市场人蛮多", "shichang ren banduo", "The market is very crowded."),
                ("货比三家", "huobisanjia", "Compare goods at three stalls."),
                ("下次再来买", "xiaci zailai mai", "Will come buy again."),
            ])
        ),
        "how_it_works": (
            "Market talk runs on three moves: ask (好钱), bargain "
            "(便宜点, 再少一点啵), close (成交). 好钱 is the signature "
            "Hunan price question - use it, not 多少钱, and vendors hear "
            "a local. Bargaining softens with 啵 and 点: 再少一点啵 "
            "haggles without offense. Payment sentences cover cash, card, "
            "and code-scan; freshness questions (新鲜啵) and the answer "
            "刚摘的 complete the produce ritual. Drill by role-playing "
            "one full purchase."
        ),
        "key_points": [
            "20 shopping-and-money sentences, each translated.",
            "Signature price question: 好钱 (not 多少钱).",
            "Bargain trio: 便宜点, 再少一点啵, 最低好多.",
            "Close with 成交; pay by 现金/刷卡/扫码.",
            "Freshness ritual: 新鲜啵 / 刚摘的.",
        ],
        "requirements": [
            "Know numbers and 好钱 before this record.",
            "Role-play one full market purchase aloud.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_ZHWIKI],
        "must_contain": ["20", "好钱", "便宜点", "成交", "扫码", "新鲜"],
        "sig_lens": (
            "Through the Signature lens the market is a sworn exchange: "
            "every 好钱 a sealed inquiry, every 成交 a covenant stamped "
            "in coin."
        ),
        "drill": {"sentences": 20, "theme": "shopping-money",
                  "bargain_moves": ["便宜点", "再少一点啵", "最低好多"],
                  "pay_methods": ["现金", "刷卡", "扫码"]},
    },
    {
        "key": "friendship",
        "name": "Xiang Chinese Friendship and Social Life Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty (20) sentences for meeting people, invitations, and "
            "celebrations - Hunan social warmth in full. \n\n"
            + _slines([
                ("我们交个朋友", "women jiao ge pengyou", "Let us be friends."),
                ("你是哪里的", "ni shi nalide", "Where are you from?"),
                ("我是长沙人", "wo shi changsharen", "I am from Changsha."),
                ("有空来我家耍", "youkong lai wojia shua", "Come hang out at my place when free."),
                ("晚上一起恰饭", "wanshang yiqi qiafan", "Eat together tonight."),
                ("我请客", "wo qingke", "My treat."),
                ("莫跟我争", "mo gen wo zheng", "Do not fight me for the bill."),
                ("生日宴在酒店", "shengriyan zai jiudian", "The birthday banquet is at the hotel."),
                ("恭喜发财", "gongxi facai", "Wishing you prosperity."),
                ("干杯", "ganbei", "Cheers."),
                ("随意恰", "suiyi qia", "Eat as you like."),
                ("好久冇聚了", "haojie mao jule", "We have not gathered in ages."),
                ("老同学见面蛮开心", "laotongxue jianmian ban kaixin", "Old classmates meeting is such joy."),
                ("介绍一下这是我朋友", "jieshao yixia zhe shi wo pengyou", "Let me introduce my friend."),
                ("以后常联系", "yihou chang lianxi", "Keep in touch."),
                ("路上注意安全", "lushang zhuyi anquan", "Travel safe."),
                ("替我问候你屋里人", "tiwo wenhou ni wuliren", "Give my regards to your family."),
                ("有困难讲一声", "you kunnan jiang yisheng", "If in trouble, just say the word."),
                ("朋友多了路好走", "pengyou duole luhaozou", "More friends make the road easier."),
                ("下次我做东", "xiaci wo zuodong", "Next time it is my treat."),
            ])
        ),
        "how_it_works": (
            "Social sentences run on invitation and generosity: 有空来耍 "
            "opens the door, 我请客/莫跟我争 fights for the bill the "
            "Hunan way. Introductions use 介绍一下; partings use 以后常"
            "联系 and 替我问候. Celebration language (恭喜发财, 干杯, "
            "生日宴) is shared across China with Hunan warmth. The "
            "friendship proverb 朋友多了路好走 closes the set. Drill by "
            "hosting an imaginary dinner in Xiang from greeting to "
            "farewell."
        ),
        "key_points": [
            "20 friendship-and-social sentences, each translated.",
            "Invitations: 有空来耍, 晚上一起恰饭.",
            "Bill-fighting: 我请客, 莫跟我争, 下次我做东.",
            "Introductions and partings: 介绍一下, 以后常联系.",
            "Regards to family: 替我问候你屋里人.",
        ],
        "requirements": [
            "Know the greetings record before this record.",
            "Host one imaginary dinner in Xiang, start to finish.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_HUNAN],
        "must_contain": ["20", "我请客", "莫跟我争", "干杯", "介绍", "问候"],
        "sig_lens": (
            "Through the Signature lens friendship is a sworn bond: "
            "every 我请客 a sealed generosity, every 问候 a covenant "
            "carried to the family door."
        ),
        "drill": {"sentences": 20, "theme": "friendship-social",
                  "hosting": ["有空来耍", "我请客", "下次我做东"]},
    },
    {
        "key": "technology",
        "name": "Xiang Chinese Technology and Communication Sentences",
        "group": "Everyday Themes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Twenty (20) sentences for the phone, the internet, the computer, "
            "and messaging - modern life in Xiang. \n\n"
            + _slines([
                ("给我打个电话", "geiwo da ge dianhua", "Give me a call."),
                ("电话冇人接", "dianhua mao ren jie", "Nobody answered the phone."),
                ("信号不好", "xinhao buhao", "The signal is bad."),
                ("发个短信给我", "fa ge duanxin geiwo", "Send me a text."),
                ("加个微信", "jia ge weixin", "Add me on WeChat."),
                ("视频聊一下", "shipin liao yixia", "Video-chat a bit."),
                ("网速蛮慢", "wangsu banman", "The internet is very slow."),
                ("连上无线网了冇", "lianshang wuxianwang lemao", "Are you on the Wi-Fi?"),
                ("电脑死机了", "diannao siji le", "The computer froze."),
                ("重启一下", "chongqi yixia", "Restart it."),
                ("密码是好多", "mima shi haoduo", "What is the password?"),
                ("帮我充下话费", "bangwo chong xia huafei", "Top up my phone credit."),
                ("手机冇电了", "shouji mao dian le", "The phone is out of battery."),
                ("充电器借我用下", "chongdianqi jiewo yongxia", "Lend me your charger."),
                ("照片发给我", "zhaopian fageiwo", "Send me the photo."),
                ("这个软件啷个用", "zhege ruanjian langge yong", "How do you use this app?"),
                ("点这个按钮", "dian zhege anniu", "Tap this button."),
                ("下载好了冇", "xiazai haole mao", "Has it downloaded?"),
                ("网上买便宜些", "wangshang mai pianyi xie", "Buying online is cheaper."),
                ("莫信陌生短信", "mo xin mosheng duanxin", "Do not trust strange texts."),
            ])
        ),
        "how_it_works": (
            "Tech sentences reuse the core grammar on modern nouns: 打电"
            "话, 发短信, 加微信, 连无线网 - verb plus object, SVO as "
            "always. Troubleshooting runs 坏了/死机了/冇电了 plus the "
            "fix verb (重启, 充电). Questions use 啷个 (啷个用) and 好多 "
            "(密码是好多). Safety advice uses 莫 (莫信陌生短信). The set "
            "proves the grammar engine handles any century: new nouns, "
            "same particles. Drill by narrating your phone routine in "
            "Xiang."
        ),
        "key_points": [
            "20 technology sentences, each translated.",
            "Communication verbs: 打电话, 发短信, 加微信, 视频聊.",
            "Troubleshooting: 死机了, 冇电了, 重启, 充电.",
            "Questions: 啷个用, 好多; safety: 莫信陌生短信.",
            "Same grammar engine, modern nouns.",
        ],
        "requirements": [
            "Know the question words before this record.",
            "Narrate your phone routine in Xiang.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_WU],
        "must_contain": ["20", "微信", "无线网", "重启", "充电", "短信"],
        "sig_lens": (
            "Through the Signature lens technology is the sworn new "
            "wire: every 微信 a sealed letter, every 重启 a covenant "
            "that the machine will serve again."
        ),
        "drill": {"sentences": 20, "theme": "technology-communication",
                  "apps": ["微信", "短信", "视频"]},
    },
]
ENTRIES += [
    {
        "key": "aspect",
        "name": "Xiang Chinese Verb Aspect in Sentences",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Xiang verbs never conjugate; four aspect particles carry all "
            "of time. Five or more translated sentences per aspect, "
            "twenty-two (22) sentences total. \n\n"
            "了 le - completed action:\n"
            + _slines([
                ("我喫了饭", "wo qiale fan", "I ate (have eaten)."),
                ("他昨日来了", "ta zuori laile", "He came yesterday."),
                ("会议开完了", "huiyi kaiwanle", "The meeting finished."),
                ("我买了两斤辣椒", "wo maile liangjin lajiao", "I bought two jin of chilies."),
                ("细伢子睡了", "xiyazi shuile", "The kid fell asleep."),
                ("雨落了", "yu luole", "It rained."),
            ]) + "\n\n"
            "咖 ga - perfective in Old Xiang (documented in the Xiang "
            "aspect studies: 翻咖 = 翻了):\n"
            + _slines([
                ("他喫咖饭", "ta qiaga fan", "He ate the meal (Old Xiang)."),
                ("车子翻咖", "chezi fanga", "The cart tipped over."),
                ("我看咖了", "wo kanga le", "I have seen it."),
                ("门关咖", "men guanga", "The door got shut."),
                ("他走咖", "ta zouga", "He left (already gone)."),
            ]) + "\n\n"
            "着 zhe - durative, ongoing state:\n"
            + _slines([
                ("门开着", "men kaizhe", "The door is open."),
                ("灯亮着", "deng liangzhe", "The light is on."),
                ("他坐着恰饭", "ta zuozhe qiafan", "He eats sitting down."),
                ("墙上挂着画", "qiangshang guazhe hua", "A painting hangs on the wall."),
                ("我记着你", "wo jizhe ni", "I remember you."),
                ("水开着", "shui kaizhe", "The water is boiling."),
            ]) + "\n\n"
            "过 guo - experiential, have-ever:\n"
            + _slines([
                ("我去过北京", "wo quguo beijing", "I have been to Beijing."),
                ("你喫过臭干子冇", "ni qiaguo chouganzi mao", "Have you ever eaten stinky tofu?"),
                ("他见过毛主席", "ta jianguo maozhuxi", "He met Chairman Mao."),
                ("我学过湘语", "wo xueguo xiangyu", "I studied Xiang before."),
                ("你爬过岳麓山冇", "ni paguo yuelushan mao", "Have you climbed Yuelu Mountain?"),
            ])
        ),
        "how_it_works": (
            "Pick the verb, then pick the aspect: 了 seals it done, 咖 "
            "seals it done the Old Xiang way, 着 holds it ongoing, 过 "
            "marks it experienced. Time words (昨日, 明日子) set the "
            "frame; the particle sets the viewpoint. Negation pairs "
            "naturally: 冇 + verb + 了 for not-yet-done, 莫 + verb for "
            "do-not. Because the verb never changes shape, learners "
            "master four particles instead of four hundred conjugations. "
            "Drill by taking five verbs through all four aspects."
        ),
        "key_points": [
            "22 sentences: 6 with 了, 5 with 咖, 6 with 着, 5 with 过.",
            "了 completed; 咖 Old Xiang perfective (documented).",
            "着 durative/ongoing; 过 experiential.",
            "Time words set the frame; particles set the viewpoint.",
            "No conjugation - four particles replace all tense tables.",
        ],
        "requirements": [
            "Know the negation trio before this record.",
            "Run five verbs through all four aspects aloud.",
        ],
        "standards": [
            "Aspect system follows Wu 2005 and the Xiang aspect studies (咖 perfective).",
            SENT_NOTE,
        ],
        "citations": [CIT_WU],
        "must_contain": ["22", "咖", "着", "过", "了", "aspect"],
        "sig_lens": (
            "Through the Signature lens aspect is the sworn clock: 了 "
            "stamps it finished, 咖 stamps it the old way, 着 holds the "
            "seal open, 过 records the covenant of experience."
        ),
        "drill": {
            "aspects": {"了": 6, "咖": 5, "着": 6, "过": 5},
            "total": 22,
        },
    },
    {
        "key": "qa",
        "name": "Xiang Chinese Questions and Answers",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty (20) question-and-answer pairs covering who, what, "
            "where, when, why, and how - the full interrogative workout. \n\n"
            + _slines([
                ("你是哪位", "ni shi nawei", "Who are you? / 我是湖南人 (wo shi hunanren) - I am a Hunan person."),
                ("这是么子", "zhe shi mezi", "What is this? / 这是辣椒 (zhe shi lajiao) - These are chilies."),
                ("你去哪里", "ni qu nali", "Where are you going? / 我去长沙 (wo qu changsha) - I am going to Changsha."),
                ("几时开会", "jishi kaihui", "When is the meeting? / 下午三点 (xiawu sandian) - Three in the afternoon."),
                ("何解不来", "hejie bulai", "Why are you not coming? / 屋里有事 (wuli youshi) - Something came up at home."),
                ("啷个去岳麓山", "langge qu yuelushan", "How do I get to Yuelu Mountain? / 坐地铁去 (zuo ditie qu) - Take the subway."),
                ("好钱一斤", "haojian yijin", "How much per jin? / 十块钱 (shikuai qian) - Ten kuai."),
                ("你恰饭了冇", "ni qiafanle mao", "Have you eaten? / 恰了 (qiale) - Yes, eaten."),
                ("有热水冇", "you reshui mao", "Is there hot water? / 有 (you) - Yes."),
                ("你晓得啵", "ni xiaode bo", "Do you know? / 晓得 (xiaode) - I know."),
                ("哪个是你的", "nage shi nide", "Which is yours? / 这个 (zhege) - This one."),
                ("几个人去", "jige ren qu", "How many people going? / 五个人 (wuge ren) - Five people."),
                ("远啵", "yuan bo", "Is it far? / 不远 (buyuan) - Not far."),
                ("辣啵", "la bo", "Is it spicy? / 蛮辣 (banla) - Very spicy."),
                ("好恰啵", "haoqia bo", "Is it tasty? / 好恰得很 (haoqia dehen) - Delicious."),
                ("你忙啵", "ni mang bo", "Are you busy? / 不忙 (bumang) - Not busy."),
                ("明日来啵", "mingri lai bo", "Coming tomorrow? / 来 (lai) - Coming."),
                ("要帮忙啵", "yao bangmang bo", "Need help? / 要 (yao) - Yes please."),
                ("是长沙人啵", "shi changsharen bo", "Are you from Changsha? / 是的 (shide) - Yes."),
                ("累啵", "lei bo", "Tired? / 有点累 (youdian lei) - A bit tired."),
            ])
        ),
        "how_it_works": (
            "Questions form three ways: question words up front (哪个, "
            "么子, 何解, 好钱, 几时, 啷个), 啵/吗 at the end turning "
            "statements into yes-no questions, and 冇 at the end asking "
            "have-you (恰饭了冇, 有热水冇). Answers are short and "
            "practical: repeat the verb (恰了, 来), answer the word "
            "(十块钱, 下午三点), or plain 是/有. Note how 啵 does the "
            "heavy lifting - half the pairs end in it. Drill by "
            "interviewing a partner with all twenty."
        ),
        "key_points": [
            "20 Q&A pairs: who/what/where/when/why/how.",
            "Question words: 哪个/么子/何解/好钱/几时/啷个.",
            "Yes-no with 啵/吗; have-you with 冇.",
            "Short answers: repeat the verb, answer the word, 是/有.",
            "啵 carries half the questions.",
        ],
        "requirements": [
            "Know question words and 啵 before this record.",
            "Interview a partner with all twenty pairs.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_WU, CIT_ZHWIKI],
        "must_contain": ["20", "何解", "么子", "啷个", "好钱", "啵"],
        "sig_lens": (
            "Through the Signature lens each question is a sworn "
            "inquiry: 何解 seals the why, 好钱 seals the price, and the "
            "answer is the covenant returned."
        ),
        "drill": {
            "pairs": 20,
            "question_words": ["哪个", "么子", "何解", "好钱", "几时", "啷个"],
            "bo_questions": 10,
        },
    },
    {
        "key": "commands",
        "name": "Xiang Chinese Commands and Requests",
        "group": "Grammar in Action",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Twenty (20) imperatives and polite requests, formal versus "
            "informal. Commands are bare verbs; politeness comes from "
            "particles and 请. Prohibition is always 莫. \n\n"
            + _slines([
                ("来", "lai", "Come! [informal, direct]"),
                ("请进来", "qing jinlai", "Please come in. [formal]"),
                ("坐", "zuo", "Sit! [informal]"),
                ("请坐", "qingzuo", "Please sit. [formal]"),
                ("恰饭", "qiafan", "Eat! [informal]"),
                ("请慢用", "qing manyong", "Please enjoy your meal. [formal]"),
                ("莫讲", "mo jiang", "Do not talk. [prohibition]"),
                ("请安静", "qing anjing", "Please be quiet. [formal]"),
                ("快点", "kuaidian", "Hurry! [informal]"),
                ("请快一点", "qing kuai yidian", "Please hurry a bit. [formal]"),
                ("把门关好", "ba men guanhao", "Shut the door well. [firm]"),
                ("麻烦把门带一下", "mafan ba men dai yixia", "Would you mind closing the door? [polite]"),
                ("莫急", "moji", "Do not rush. [reassuring]"),
                ("请放心", "qing fangxin", "Please rest assured. [formal]"),
                ("走撒", "zou sa", "Let us go, shall we? [suggesting]"),
                ("我们一起去吧", "women yiqi qu ba", "Let us go together. [suggesting]"),
                ("莫客气", "mo keqi", "Do not stand on ceremony. [warm]"),
                ("请多指教", "qing duozhijiao", "Please guide me. [formal humble]"),
                ("小心点", "xiaoxin dian", "Be careful. [caring]"),
                ("一路平安", "yilu pingan", "Safe travels. [blessing]"),
            ])
        ),
        "how_it_works": (
            "The imperative is the bare verb: 来, 坐, 恰饭. Add 请 to "
            "formalize (请坐, 请进来); add 吧/撒 to suggest (走撒, 去"
            "吧); add 点/一下 to soften (快一点, 带一下). Prohibition "
            "never uses 不 - it is always 莫 (莫讲, 莫急, 莫客气). "
            "Blessings (一路平安) and humble forms (请多指教, 麻烦) "
            "complete the register ladder from street-direct to "
            "ceremony-formal. Drill by giving a whole day of orders, "
            "then re-saying each one formally."
        ),
        "key_points": [
            "20 commands/requests, formal vs informal marked.",
            "Bare verb = command; 请 = formal; 吧/撒 = suggestion.",
            "Softeners: 点, 一下, 麻烦.",
            "Prohibition is always 莫, never 不.",
            "Blessings and humble forms complete the ladder.",
        ],
        "requirements": [
            "Know 莫 and 请 before this record.",
            "Re-say each command in the opposite register.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_WU],
        "must_contain": ["20", "莫", "请", "撒", "吧", "一路平安"],
        "sig_lens": (
            "Through the Signature lens commands are sworn directives: "
            "the bare verb a sealed order, 请 the bow before it, 莫 the "
            "firm hand that holds the line."
        ),
        "drill": {
            "count": 20, "formal": 8, "informal": 7, "suggesting": 2,
            "prohibitions": 3, "prohibitive": "莫",
        },
    },
    {
        "key": "descriptions",
        "name": "Xiang Chinese Descriptions of People and Places",
        "group": "Grammar in Action",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Twenty (20) sentences describing people, places, and things "
            "in detail - the descriptive payoff of all the vocabulary. \n\n"
            + _slines([
                ("我堂客是个辣利婆", "wo tangke shi ge lalipo", "My wife is a capable, sharp Hunan woman."),
                ("娭毑头发全白了", "aijie toufa quanbaile", "Grandma's hair turned all white."),
                ("嗲嗲走路蛮稳", "diadie zoulu banwen", "Grandpa walks very steadily."),
                ("那个细伢子眼睛大大的", "nage xiyazi yanjing dada de", "That kid has big round eyes."),
                ("他个子高高的", "ta gezi gaogao de", "He is tall."),
                ("妹子讲起话来像爆豆子", "meizi jiangqi hualai xiang baodouzi", "The girl talks like popping beans - rapid fire."),
                ("长沙是座火辣的城市", "changsha shi zuo huolade chengshi", "Changsha is a fiery city."),
                ("湘江穿城而过", "xiangjiang chuancheng erguo", "The Xiang River runs through the city."),
                ("岳麓山满山是树", "yuelushan manshan shi shu", "Yuelu Mountain is covered in trees."),
                ("橘子洲头风景好", "juzizhoutou fengjing hao", "Orange Isle has beautiful scenery."),
                ("坡子街的小吃蛮多", "pozijiede xiaochi banduo", "Pozi Street has so many snacks."),
                ("臭干子闻起臭恰起香", "chouganzi wenqi chou qiaqi xiang", "Stinky tofu smells bad, tastes fragrant."),
                ("辣椒红红的挂满枝头", "lajiao honghong de guaman zhitou", "Red chilies hang heavy on the branches."),
                ("这栋楼好高", "zhe dong lou haogao", "This building is so tall."),
                ("房间收拾得干干净净", "fangjian shoushide ganganjingjing", "The room is tidied spotless."),
                ("他的字写得漂亮", "tade zi xiede piaoliang", "His handwriting is beautiful."),
                ("这首歌唱得好听", "zhe shou ge changde haoting", "This song is sung beautifully."),
                ("夜嘎子的长沙灯火辉煌", "yegazide changsha denghuo huihuang", "Changsha at night blazes with lights."),
                ("湖南人热情又霸蛮", "hunanren reqing you baman", "Hunan people are warm and can-do."),
                ("这里的生活有滋有味", "zhelide shenghuo youzi youwei", "Life here is full of flavor."),
            ])
        ),
        "how_it_works": (
            "Descriptions stack the grammar: 是 for identity (是座火辣"
            "的城市), degree complements with 得 (走得蛮稳, 写得漂亮, "
            "唱得好听), reduplicated adjectives for vividness (大大的, "
            "高高的, 红红的, 干干净净), and sensory verbs 闻起/恰起 "
            "for smell and taste. Place descriptions anchor in real "
            "Hunan geography (湘江, 岳麓山, 橘子洲, 坡子街). People "
            "descriptions use the kinship and body vocabulary at full "
            "stretch. Drill by describing three real people and three "
            "real places."
        ),
        "key_points": [
            "20 detailed descriptions: people, places, things.",
            "是 for identity; 得 complements for degree.",
            "Reduplicated adjectives: 大大的, 高高的, 干干净净.",
            "Sensory verbs: 闻起 (smell), 恰起 (taste).",
            "Anchored in real Hunan geography.",
        ],
        "requirements": [
            "Know adjectives, 得 complements, and place nouns first.",
            "Describe three real people and three real places.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_ZHWIKI, CIT_WU],
        "must_contain": ["20", "辣利婆", "橘子洲", "坡子街", "得", "干干净净"],
        "sig_lens": (
            "Through the Signature lens description is sworn portraiture: "
            "every 得-complement a sealed brushstroke, every reduplicated "
            "adjective a double-stamped color."
        ),
        "drill": {"sentences": 20, "people": 6, "places": 6, "things": 8,
                  "de_complements": 5},
    },
    {
        "key": "story1",
        "name": "Xiang Chinese Short Story I: A Simple Day",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A 10-sentence simple story in Xiang, line-by-line English "
            "translation. Present-tense, everyday words, the whole "
            "foundations vocabulary at work. \n\n"
            "Title: 我的一天 (My Day)\n"
            + _slines([
                ("早上七点我起床", "zaoshang qidian wo qichuang", "At seven in the morning I get up."),
                ("姆妈在厨房做早饭", "muma zai chufang zuo zaofan", "Mom makes breakfast in the kitchen."),
                ("我恰一碗米粉", "wo qia yiwan mifen", "I eat a bowl of rice noodles."),
                ("米粉里放好多辣椒", "mifen li fang haoduo lajiao", "The noodles have lots of chili in them."),
                ("恰完饭我去上班", "qiawanfan wo qu shangban", "After eating I go to work."),
                ("路上碰到老同学", "lushang pengdao laotongxue", "On the road I meet an old classmate."),
                ("我们站在路边打讲", "women zhanzai lubian dajiang", "We stand by the road having a heart-to-heart."),
                ("中午一起恰辣椒炒肉", "zhongwu yiqi qia lajiao chaorou", "At noon we eat stir-fried pork with chilies together."),
                ("下午我把报告写完", "xiawu wo ba baogao xiewan", "In the afternoon I finish writing the report."),
                ("夜嘎子回家一家人恰饭", "yegazi huijia yijiaren qiafan", "At night I go home and the family eats together."),
            ])
        ),
        "how_it_works": (
            "The story is the ladder's payoff: ten sentences using only "
            "foundations and theme vocabulary, each glossed line by line. "
            "Read the Xiang line, guess the meaning, then check the "
            "English. Notice the grammar in the wild: time words fronted "
            "(早上七点, 中午, 下午), 把 moving the object (把报告写完), "
            "result complements (写完, 恰完). Retell the story from memory "
            "in Xiang before moving to story two."
        ),
        "key_points": [
            "10-sentence story, line-by-line translation.",
            "Present-tense, foundations vocabulary only.",
            "Time words fronted; 把 construction; result complements.",
            "Retell-from-memory drill.",
            "Title: 我的一天.",
        ],
        "requirements": [
            "Read all theme records before the stories.",
            "Retell story one from memory before story two.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_WU],
        "must_contain": ["10", "我的一天", "米粉", "打讲", "把报告", "line-by-line"],
        "sig_lens": (
            "Through the Signature lens the simple day is a sworn diary: "
            "ten sentences, ten seals, each hour of the Hunan day kept "
            "in covenant."
        ),
        "drill": {"sentences": 10, "title": "我的一天", "tense": "present"},
    },
    {
        "key": "story2",
        "name": "Xiang Chinese Short Story II: A Journey in the Past",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A 10-sentence story using past forms - 了, 咖, 过 - line-"
            "by-line English translation. \n\n"
            "Title: 上个月的旅行 (Last Month's Trip)\n"
            + _slines([
                ("上个月我去了凤凰", "shanggeyue wo qule fenghuang", "Last month I went to Fenghuang."),
                ("我坐高铁去的", "wo zuo gaotie qude", "I went by high-speed rail."),
                ("到了那边先恰了臭干子", "daole nabian xian qiale chouganzi", "Arriving there, I first ate stinky tofu."),
                ("古城的房子蛮有样范", "guchengde fangzi banyou yangfan", "The old town's houses have great character."),
                ("我在沱江边打望了好久", "wo zai tuojiangbian dawang le haojie", "I gazed along the Tuo River for a long time."),
                ("还买了些姜糖回去", "hai maile xie jiangtang huiqu", "I also bought some ginger candy to take home."),
                ("路上拐场耽误了时间", "lushang guaichang dangele shijian", "An accident on the road delayed us."),
                ("好在莫出大事", "haozai mo chu dashi", "Luckily nothing serious happened."),
                ("我去过三次了", "wo quguo sanci le", "I have been three times now."),
                ("下次要带堂客一起去", "xiaci yao dai tangke yiqi qu", "Next time I will bring my wife along."),
            ])
        ),
        "how_it_works": (
            "Story two is the aspect showcase: 了 marks each completed "
            "event (去了, 恰了, 买了), 过 marks experience (去过三次), "
            "and the narrative chains events with 先...还...好在. Past "
            "time words (上个月, 到了) set the frame once; particles do "
            "the rest. Fenghuang's old town gives the journey real Hunan "
            "geography. Retell it emphasizing every particle choice."
        ),
        "key_points": [
            "10-sentence past-tense story, line-by-line translation.",
            "了 for completed events; 过 for experience.",
            "Narrative chain: 先...还...好在.",
            "Real geography: 凤凰, 沱江.",
            "Title: 上个月的旅行.",
        ],
        "requirements": [
            "Know the aspect record cold before this story.",
            "Retell emphasizing every particle choice.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_WU],
        "must_contain": ["10", "上个月的旅行", "凤凰", "沱江", "去过", "line-by-line"],
        "sig_lens": (
            "Through the Signature lens the journey is a sworn travel "
            "log: every 了 a sealed footprint, every 过 a covenant that "
            "the road was truly walked."
        ),
        "drill": {"sentences": 10, "title": "上个月的旅行", "tense": "past",
                  "le_count": 6, "guo_count": 1},
    },
    {
        "key": "story3",
        "name": "Xiang Chinese Short Story III: Plans for Tomorrow",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A 10-sentence story using future and conditional forms - "
            "要, 会, 如果...就 - line-by-line English translation. \n\n"
            "Title: 明年的计划 (Next Year's Plans)\n"
            + _slines([
                ("明年我要学好湘语", "mingnian wo yao xuehao xiangyu", "Next year I will learn Xiang well."),
                ("如果有时间我会去长沙", "ruguo youshijian wo hui qu changsha", "If I have time I will go to Changsha."),
                ("我要爬岳麓山看橘子洲", "wo yao pa yuelushan kan juzizhou", "I will climb Yuelu Mountain and see Orange Isle."),
                ("还要恰遍坡子街的小吃", "haiyao qiabian pozijiede xiaochi", "And eat through all of Pozi Street's snacks."),
                ("要是落雨就带把伞", "yaoshi luoyu jiu da ba san", "If it rains, bring an umbrella."),
                ("堂客讲她也要去", "tangke jiang ta ye yaoqu", "My wife says she wants to go too."),
                ("细伢子会蛮开心", "xiyazi hui ban kaixin", "The kid will be very happy."),
                ("我们会住在河西", "women hui zhu zai hexi", "We will stay west of the river."),
                ("只要霸蛮冇么子难得到我", "zhiyao baman mao mezi nande dao wo", "As long as I am can-do, nothing can stump me."),
                ("明年见", "mingnian jian", "See you next year."),
            ])
        ),
        "how_it_works": (
            "Story three is the future/conditional showcase: 要 for "
            "intention, 会 for prediction, 如果...就 and 要是...就 for "
            "conditions, 只要 for as-long-as. No future tense exists - "
            "intention words plus time words (明年) do the work. The "
            "closing line 只要霸蛮冇么子难得到我 ties the Hunan spirit "
            "into the grammar. Retell it as your own plan, swapping in "
            "your details."
        ),
        "key_points": [
            "10-sentence future/conditional story, line-by-line translation.",
            "要 intention; 会 prediction; 如果...就 conditions.",
            "No future tense - intention words plus time words.",
            "Closes on the 霸蛮 spirit line.",
            "Title: 明年的计划.",
        ],
        "requirements": [
            "Know the complex-sentence connectors before this story.",
            "Retell as your own plan with your details.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_WU],
        "must_contain": ["10", "明年的计划", "如果", "要是", "只要", "line-by-line"],
        "sig_lens": (
            "Through the Signature lens plans are sworn vows: every 要 "
            "a sealed intention, every 如果 a covenant with tomorrow."
        ),
        "drill": {"sentences": 10, "title": "明年的计划", "tense": "future",
                  "conditionals": 3},
    },
    {
        "key": "idioms",
        "name": "Xiang Chinese Idioms and Proverbs",
        "group": "Stories and Idioms",
        "ladder_rank": 9,
        "ladder_tier": "compounded",
        "description": (
            "Twenty (20) idioms and proverbs - literal translation, real "
            "meaning, and an example sentence each. Hunan's own sayings "
            "lead; shared Chinese wisdom follows. \n\n"
            + _slines([
                ("吃得苦、霸得蛮、不怕死、耐得烦", "chideku bademan bupasinaidefan", "Endure hardship, be can-do, fear no death, endure tedium. [the Hunan spirit] - 做事要吃得苦霸得蛮 (At work, endure hardship and be can-do)."),
                ("无湘不成军", "wuxiang buchengjun", "Without Hunan there is no army. [Hunan's military fame] - 自古无湘不成军 (Since ancient times, no army without Hunan)."),
                ("四川人不怕辣，湖南人怕不辣", "sicuanren bupala hunanren pabula", "Sichuan people do not fear spice; Hunan people fear its absence. - 他是湖南人怕不辣 (He is Hunanese: he fears no spice, only its lack)."),
                ("姜是老的辣", "jiang shi laode la", "Old ginger is spicier: experience counts. - 姜是老的辣，听娭毑的冇错 (Old ginger is spicier; listen to grandma)."),
                ("一方水土养一方人", "yifang shuitu yang yifang ren", "Each land raises its own people. - 一方水土养一方人，湖南出霸蛮人 (Each land raises its own; Hunan raises can-do people)."),
                ("入乡随俗", "ruxiang suisu", "Follow local customs. - 到了长沙入乡随俗恰辣椒 (In Changsha, follow custom and eat chilies)."),
                ("心急吃不了热豆腐", "xinji chibuliao redoufu", "Haste cannot eat hot tofu: patience. - 莫急，心急吃不了热豆腐 (Do not rush; haste cannot eat hot tofu)."),
                ("滴水穿石", "dishui chuanshi", "Dripping water pierces stone: persistence. - 学习要滴水穿石 (Study takes dripping-water persistence)."),
                ("众人拾柴火焰高", "zhongren shichai huoyangao", "Many hands make flames high. - 大家一起干，众人拾柴火焰高 (All pitch in; many hands make flames high)."),
                ("有志者事竟成", "youzhizhe shijingcheng", "Where there is will, there is a way. - 有志者事竟成，湘语学得好 (Where there is will, Xiang can be learned)."),
                ("吃一堑长一智", "chiyiqian zhangyizhi", "A fall in the pit, a gain in wit. - 上当一次，吃一堑长一智 (Fooled once; a gain in wit)."),
                ("失败是成功之母", "shibai shi chenggong zhimu", "Failure is the mother of success. - 莫怕失败，失败是成功之母 (Fear no failure; it is success's mother)."),
                ("熟能生巧", "shuneng shengqiao", "Practice makes skill. - 多讲多练，熟能生巧 (Speak and drill more; practice makes skill)."),
                ("患难见真情", "huannan jian zhenqing", "Hardship reveals true feelings. - 患难见真情，朋友要交心的 (Hardship reveals true feelings; befriend the sincere)."),
                ("远亲不如近邻", "yuanqin buru jinlin", "A near neighbor beats a distant kin. - 有事喊邻居，远亲不如近邻 (Call neighbors in need; near beats far)."),
                ("好事多磨", "haoshi duomo", "Good things take grinding. - 莫急，好事多磨 (Do not rush; good things take grinding)."),
                ("笑一笑十年少", "xiaoyixiao shinian shao", "A laugh takes ten years off. - 开心点，笑一笑十年少 (Cheer up; a laugh takes ten years off)."),
                ("若要人不知除非己莫为", "ruoyao renbuzhi chufei jimo wei", "To hide it, do it not. - 若要人不知，除非己莫为 (To keep it unknown, do it not)."),
                ("前人栽树后人乘凉", "qianren zaishu houren chengliang", "Forerunners plant trees; followers enjoy shade. - 感谢前人栽树后人乘凉 (Thanks to those who planted before us)."),
                ("路遥知马力日久见人心", "luyao zhimali rijiu jianrenxin", "Long roads test horses; long days test hearts. - 路遥知马力，朋友处久了才晓得 (Long roads test horses; friends prove over time)."),
            ])
        ),
        "how_it_works": (
            "Each idiom is learned in three layers: the literal picture "
            "(dripping water, old ginger), the real meaning (persistence, "
            "experience), and one sentence putting it to work. The Hunan "
            "set (吃得苦霸得蛮, 无湘不成军, 怕不辣) is drilled first - "
            "they are identity, not decoration. Shared proverbs follow the "
            "same three-layer method. Use one idiom per day in real "
            "speech until all twenty are natural."
        ),
        "key_points": [
            "20 idioms/proverbs: literal + meaning + example sentence.",
            "Hunan identity set first: 霸蛮 spirit, 无湘不成军, 怕不辣.",
            "Three-layer learning: picture, meaning, use.",
            "One-idiom-per-day speaking drill.",
        ],
        "requirements": [
            "Know the stories before the idioms.",
            "Use one idiom per day in real speech.",
        ],
        "standards": [
            "Hunan sayings per Hunan cultural records; shared proverbs are pan-Chinese.",
            SENT_NOTE,
        ],
        "citations": [CIT_HUNAN],
        "must_contain": ["20", "无湘不成军", "怕不辣", "姜是老的辣", "滴水穿石", "literal"],
        "sig_lens": (
            "Through the Signature lens proverbs are sworn heirlooms: "
            "every 吃得苦 a sealed inheritance, every 无湘不成军 a "
            "covenant stamped by generations."
        ),
        "drill": {"count": 20, "hunan_set": 3, "layers": 3},
    },
]
ENTRIES += [
    {
        "key": "registers",
        "name": "Xiang Chinese Formal and Polite Registers",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen (15) formal-versus-informal pairs for letters, "
            "business, and elders - the register ladder from street to "
            "ceremony. \n\n"
            + _slines([
                ("你来", "ni lai", "You come. [informal] / 恁请过来 (nin qing guolai) - Please come over. [formal]"),
                ("坐", "zuo", "Sit. [informal] / 请坐 (qingzuo) - Please be seated. [formal]"),
                ("恰饭", "qiafan", "Eat. [informal] / 请慢用 (qing manyong) - Please enjoy. [formal]"),
                ("莫讲", "mo jiang", "Do not talk. [informal] / 请保持安静 (qing baochi anjing) - Please keep quiet. [formal]"),
                ("快点", "kuaidian", "Hurry. [informal] / 麻烦快一点 (mafan kuai yidian) - Please hurry a bit. [formal]"),
                ("给我", "geiwo", "Give me. [informal] / 麻烦你给我一下 (mafan ni geiwo yixia) - Could you hand it to me. [formal]"),
                ("晓得啵", "xiaode bo", "Know? [informal] / 请问您晓得啵 (qingwen nin xiaode bo) - May I ask if you know. [formal]"),
                ("好多钱", "haoduo qian", "How much? [informal] / 请问这个好多钱 (qingwen zhege haoduo qian) - May I ask the price. [formal]"),
                ("再见", "zaijian", "Bye. [informal] / 恁慢走 (nin manzou) - Take care. [formal respectful]"),
                ("谢谢", "xiexie", "Thanks. [informal] / 多谢恁 (duoxie nin) - Many thanks to you. [formal]"),
                ("对不起", "duibuqi", "Sorry. [informal] / 实在不好意思 (shizai buhaoyisi) - I am truly sorry. [formal]"),
                ("我走了", "wo zoule", "I am off. [informal] / 我先告辞了 (wo xian gaocile) - I take my leave. [formal]"),
                ("你讲", "ni jiang", "You speak. [informal] / 请恁讲几句 (qing nin jiang jiju) - Please say a few words. [formal]"),
                ("莫客气", "mo keqi", "Do not mention it. [informal] / 应该的 (yinggaide) - It is only proper. [formal]"),
                ("有空来耍", "youkong lai shua", "Come hang out. [informal] / 欢迎恁随时来做客 (huanying nin suishi lai zuoke) - You are welcome anytime. [formal]"),
            ])
        ),
        "how_it_works": (
            "Register shifts on three levers: pronouns (你 to 恁/您), "
            "openers (bare verb to 请/麻烦/请问), and closers (再见 to "
            "恁慢走, 我走了 to 我先告辞了). Elders get 恁 and 请问; "
            "business gets 麻烦 and 实在; letters get 告辞 and 做客. "
            "The informal column is never rude - it is warm Hunan "
            "directness for friends and family. Drill by converting a "
            "whole conversation up and down the ladder."
        ),
        "key_points": [
            "15 formal/informal pairs with context notes.",
            "Three levers: pronouns, openers, closers.",
            "Elders: 恁/请问; business: 麻烦/实在; letters: 告辞/做客.",
            "Informal is warm directness, not rudeness.",
            "Full-conversation register conversion drill.",
        ],
        "requirements": [
            "Know pronouns and commands before this record.",
            "Convert one conversation up and down the ladder.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_HUNAN, CIT_WU],
        "must_contain": ["15", "恁", "请问", "麻烦", "告辞", "register"],
        "sig_lens": (
            "Through the Signature lens register is sworn courtesy: 恁 "
            "the sealed bow, 请问 the knock before entering, each level "
            "a covenant of respect."
        ),
        "drill": {"pairs": 15, "levers": ["pronouns", "openers", "closers"]},
    },
    {
        "key": "complex",
        "name": "Xiang Chinese Compound and Complex Sentences",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fifteen (15) long sentences with clauses, connectors, and "
            "relative clauses - parsed and translated. \n\n"
            + _slines([
                ("因为落雨所以冇去", "yinwei luoyu suoyi maoqu", "Because it rained, we did not go. [cause]"),
                ("虽然蛮累但是蛮开心", "suiran banlei danshi ban kaixin", "Although very tired, very happy. [contrast]"),
                ("如果明日子有空我们就去", "ruguo mingrizi youkong women jiuqu", "If free tomorrow, we will go. [condition]"),
                ("不但会讲还会写", "budan hui jiang hai hui xie", "Not only can speak, can also write. [not only]"),
                ("既便宜又好吃", "ji pianyi you haoqia", "Both cheap and tasty. [both]"),
                ("只要努力就能学会", "zhiyao nuli jiu neng xuehui", "As long as you work hard, you can learn. [as long as]"),
                ("除了辣椒还放了蒜", "chule lajiao hai fangle suan", "Besides chilies, added garlic too. [besides]"),
                ("随着年纪增长越来越霸蛮", "suizhe nianji zengzhang yuelaiyue baman", "With age, ever more can-do. [with]"),
                ("把饭恰完才能走", "ba fan qiawan caineng zou", "Finish the rice before leaving. [把]"),
                ("杯子被细伢子打烂了", "beizi bei xiyazi dalanle", "The cup was smashed by the kid. [passive]"),
                ("我昨日买的那本书蛮好", "wo zuori maide na ben shu banhao", "The book I bought yesterday is very good. [relative]"),
                ("讲湘语的人越来越少了", "jiang xiangyude ren yuelaiyue shaole", "Xiang speakers grow fewer. [relative]"),
                ("他一回来我们就开饭", "ta yihuilai women jiu kaifan", "The moment he returns, we eat. [as soon as]"),
                ("越辣越想恰", "yue la yue xiang qia", "The spicier, the more I crave it. [the more]"),
                ("无论啷个样都要坚持", "wulun langgeyang dou yao jianchi", "No matter what, persist. [no matter]"),
            ])
        ),
        "how_it_works": (
            "Complex sentences are parsed into frames: 因为...所以 "
            "(cause), 虽然...但是 (contrast), 如果...就 (condition), "
            "不但...还 (not only), 只要...就 (as long as), 越...越 "
            "(the more). Relative clauses stack before the noun with 的 "
            "(我昨日买的书). The passive runs 被. The moment-pattern "
            "一...就 chains events. Learn each frame as a mold, then pour "
            "your own words in. Drill by expanding five simple sentences "
            "into complex ones."
        ),
        "key_points": [
            "15 complex sentences, parsed and translated.",
            "Connector frames: 因为/虽然/如果/不但/既/只要/除了/随着/无论.",
            "Relative clauses with 的 before the noun.",
            "Passive with 被; moment-pattern 一...就; 越...越.",
            "Frame-as-mold learning method.",
        ],
        "requirements": [
            "Know all basic grammar before this record.",
            "Expand five simple sentences into complex ones.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_WU],
        "must_contain": ["15", "因为", "虽然", "如果", "被", "越"],
        "sig_lens": (
            "Through the Signature lens complex sentences are sworn "
            "architecture: every connector a sealed joint, every clause "
            "a covenant holding the meaning together."
        ),
        "drill": {"count": 15, "frames": 9, "relative_clauses": 2},
    },
    {
        "key": "conv_market",
        "name": "Xiang Chinese Conversation: At the Market",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A 20-line bilingual market dialogue (Xiang + English), "
            "annotated. A buyer haggles for chilies and stinky tofu. \n\n"
            "买家 Buyer (B) / 卖家 Seller (S):\n"
            + _slines([
                ("B: 辣椒好钱一斤", "lajiao haojian yijin", "How much are chilies per jin?"),
                ("S: 八块钱", "bakuai qian", "Eight kuai."),
                ("B: 太贵了，便宜点啵", "taiguile pianyi dian bo", "Too pricey; cheaper, OK?"),
                ("S: 已经最便宜了", "yijing zui pianyi le", "Already the cheapest."),
                ("B: 五块卖啵", "wukuai mai bo", "Five kuai, deal?"),
                ("S: 五块要亏本了", "wukuai yao kuiben le", "Five kuai and I lose money."),
                ("B: 那六块，称两斤", "na liukuai cheng liangjin", "Then six kuai; weigh two jin."),
                ("S: 好，六块两斤", "hao liukuai liangjin", "OK, six kuai for two jin."),
                ("B: 称高一点", "cheng gaoyidian", "Weigh generously."),
                ("S: 放心，秤不会错", "fangxin cheng buhui cuo", "Rest assured, the scale is honest."),
                ("B: 臭干子好钱", "chouganzi haojian", "How much is stinky tofu?"),
                ("S: 十块钱一份", "shikuai qian yifen", "Ten kuai a portion."),
                ("B: 来两份，打包", "lai liangfen dabao", "Two portions, to go."),
                ("S: 好嘞，马上好", "haolei mashang hao", "Coming right up."),
                ("B: 可以扫码啵", "keyi saoma bo", "Can I scan to pay?"),
                ("S: 可以，这边扫", "keyi zhebian sao", "Yes, scan here."),
                ("B: 付好了", "fuhau le", "Paid."),
                ("S: 找你零钱", "zhaoni lingqian", "Here is your change. [if cash]"),
                ("B: 下次再来", "xiaci zailai", "Will come again."),
                ("S: 慢走，欢迎再来", "manzou huanying zailai", "Take care; welcome back."),
            ])
        ),
        "how_it_works": (
            "The dialogue is the bargaining drill in the wild: 好钱 "
            "opens, 便宜点/五块卖啵 haggles, 成交-style acceptance "
            "closes, then the payment ritual (扫码/付好/找零) and the "
            "warm farewell (慢走). Annotations mark each move. Read both "
            "roles aloud, then replay it with different goods and prices. "
            "The whole shopping record's vocabulary earns its keep here."
        ),
        "key_points": [
            "20-line bilingual market dialogue, annotated.",
            "Full bargain arc: ask, haggle, close, pay, farewell.",
            "Moves marked: 好钱/便宜点/成交/扫码/慢走.",
            "Replay drill with different goods and prices.",
        ],
        "requirements": [
            "Know the shopping record before this dialogue.",
            "Read both roles aloud; replay with new goods.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_ZHWIKI],
        "must_contain": ["20", "好钱", "便宜点", "扫码", "慢走", "dialogue"],
        "sig_lens": (
            "Through the Signature lens the market dialogue is a sworn "
            "negotiation: every 好钱 a sealed bid, every 慢走 a covenant "
            "of return custom."
        ),
        "drill": {"lines": 20, "roles": 2, "moves": 5},
    },
    {
        "key": "conv_friend",
        "name": "Xiang Chinese Conversation: Meeting a Friend",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A 20-line bilingual dialogue (Xiang + English), annotated. "
            "Two old friends meet and plan dinner. \n\n"
            "阿明 A-Ming (A) / 阿红 A-Hong (H):\n"
            + _slines([
                ("A: 好久不见", "haojiebujian", "Long time no see."),
                ("H: 是啊，好几年了", "shia haojinian le", "Yes, several years."),
                ("A: 你还好啵", "ni haihao bo", "Are you well?"),
                ("H: 蛮好，你呢", "banhao nine", "Very well; and you?"),
                ("A: 我也蛮好", "wo ye banhao", "I am well too."),
                ("H: 恰饭了冇", "qiafanle mao", "Have you eaten?"),
                ("A: 还冇，正想去恰", "hai mao zheng xiangqu qia", "Not yet; was just going to."),
                ("H: 那一起去，我请客", "na yiqi qu wo qingke", "Then come along; my treat."),
                ("A: 莫跟我争，这次我来", "mo gen wo zheng zheci wo lai", "Do not fight me; this time is mine."),
                ("H: 下次你再请", "xiaci ni zaiqing", "Next time you treat."),
                ("A: 去坡子街啷个样", "qu pozijie langgeyang", "How about Pozi Street?"),
                ("H: 要得，那里小吃多", "yaode nali xiaochi duo", "Deal; lots of snacks there."),
                ("A: 你屋里人都好啵", "ni wuliren dou hao bo", "Is your family well?"),
                ("H: 都好，细伢子长好高了", "dou hao xiyazi zhang haogaole", "All well; the kid grew so tall."),
                ("A: 有空带来耍", "youkong dailai shua", "Bring him around when free."),
                ("H: 要得，有困难讲一声", "yaode you kunnan jiang yisheng", "Deal; if in trouble, say the word."),
                ("A: 朋友多了路好走", "pengyou duole luhaozou", "More friends, easier road."),
                ("H: 走撒，恰饭去", "zou sa qiafan qu", "Let us go eat."),
                ("A: 走", "zou", "Go."),
                ("H: 下次再聚", "xiaci zaiju", "Until next time."),
            ])
        ),
        "how_it_works": (
            "The dialogue is the friendship record in motion: greeting "
            "(好久不见), welfare check (恰饭了冇), the bill fight (我请"
            "客/莫跟我争), planning (去坡子街啷个样/要得), family news "
            "(细伢子长好高了), and the warm close (下次再聚). Annotations "
            "mark each social move. Perform it with a partner, swapping "
            "roles, then improvise a third meeting."
        ),
        "key_points": [
            "20-line bilingual friend dialogue, annotated.",
            "Social arc: greet, check, bill-fight, plan, news, close.",
            "Moves marked: 好久不见/我请客/莫跟我争/要得/下次再聚.",
            "Partner performance + improvisation drill.",
        ],
        "requirements": [
            "Know greetings and friendship records first.",
            "Perform with a partner; improvise a third meeting.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_HUNAN],
        "must_contain": ["20", "好久不见", "我请客", "莫跟我争", "要得", "dialogue"],
        "sig_lens": (
            "Through the Signature lens the reunion is a sworn renewal: "
            "every 好久不见 a seal broken open with joy, every 下次再聚 "
            "a covenant of meetings to come."
        ),
        "drill": {"lines": 20, "roles": 2, "moves": 6},
    },
    {
        "key": "conv_problem",
        "name": "Xiang Chinese Conversation: Solving a Problem",
        "group": "Conversation and Registers",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A 20-line bilingual dialogue (Xiang + English), annotated. "
            "A traveler lost near Yuelu Mountain gets help. \n\n"
            "旅客 Traveler (T) / 路人 Passerby (P):\n"
            + _slines([
                ("T: 请问，去岳麓山啷个走", "qingwen qu yuelushan langge zou", "Excuse me, how do I get to Yuelu Mountain?"),
                ("P: 你走错方向了", "ni zoucuo fangxiangle", "You went the wrong way."),
                ("T: 何解，我跟着导航走的", "hejie wo genzhe daohang zoude", "Why? I followed the navigation."),
                ("P: 导航有时候不灵光", "daohang youshihou bulingguang", "Navigation is sometimes off."),
                ("T: 那现在啷个办", "na xianzai langge ban", "What do I do now?"),
                ("P: 莫急，我跟你讲", "moji wo gen ni jiang", "Do not worry; I will tell you."),
                ("T: 麻烦你了", "mafan ni le", "Sorry to trouble you."),
                ("P: 冇事，你往回走", "maoshi ni wanghui zou", "No trouble; head back."),
                ("T: 走好远", "zou haoyuan", "Walk how far?"),
                ("P: 走一里路就到", "zou yili lu jiudao", "One li and you are there."),
                ("T: 路上好找啵", "lushang haozhao bo", "Is it easy to find?"),
                ("P: 好找，一直往前", "haozhao yizhi wangqian", "Easy; straight ahead."),
                ("T: 要走好久", "yao zou haojie", "How long a walk?"),
                ("P: 二十分钟左右", "ershifen zhong zuoyou", "About twenty minutes."),
                ("T: 多谢你", "duoxie ni", "Thank you so much."),
                ("P: 莫客气，出门在外", "mo keqi chumenzaiwai", "Do not mention it; we are all travelers."),
                ("T: 湖南人真热情", "hunanren zhen reqing", "Hunan people are truly warm."),
                ("P: 应该的，慢走", "yinggaide manzou", "Of course; take care."),
                ("T: 再见", "zaijian", "Goodbye."),
                ("P: 一路顺风", "yilu shunfeng", "Smooth travels."),
            ])
        ),
        "how_it_works": (
            "The dialogue is problem-solving in the wild: ask (请问...啷"
            "个走), diagnose (走错方向了), troubleshoot (导航不灵光), "
            "instruct (往回走, 一直往前), confirm (好找啵/要走好久), "
            "thank (多谢/莫客气), bless (一路顺风). Annotations mark each "
            "move. It reuses travel, direction, and politeness records at "
            "once. Perform it, then improvise being lost somewhere else."
        ),
        "key_points": [
            "20-line bilingual problem-solving dialogue, annotated.",
            "Arc: ask, diagnose, troubleshoot, instruct, confirm, thank, bless.",
            "Moves marked: 请问/走错/莫急/往回走/多谢/一路顺风.",
            "Reuses travel + politeness records together.",
        ],
        "requirements": [
            "Know travel, directions, and commands records first.",
            "Perform it; improvise being lost elsewhere.",
        ],
        "standards": [SENT_NOTE],
        "citations": [CIT_WU],
        "must_contain": ["20", "啷个走", "走错", "莫急", "一路顺风", "dialogue"],
        "sig_lens": (
            "Through the Signature lens the rescue is a sworn kindness: "
            "every 往回走 a sealed correction, every 一路顺风 a covenant "
            "that the stranger arrives safe."
        ),
        "drill": {"lines": 20, "roles": 2, "moves": 7},
    },
    {
        "key": "mastery",
        "name": "Xiang Chinese Mastery Review and Full Reference",
        "group": "Mastery Reference",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The whole database in one teaching summary: the six tones, "
            "200 core words, the grammar rules, and the phrase tables - "
            "the mastery checkpoint. \n\n"
            "Six Changsha tones: 阴平33, 阳平13, 上声41, 阴去24, 阳去45, "
            "入声21. Old Xiang: 5 tones. Initials: Changsha old-style 23, "
            "new-style 20; Shuangfeng 28. Finals: Changsha old-style 45, "
            "new-style 39; Shuangfeng 11 vowels. \n\n"
            "200 core words (characters + pinyin-style + English), the "
            "database's full word-hoard in one table:\n"
            "人 ren person, 水 shui water, 饭 fan rice/meal, 山 shan mountain, "
            "河 he river, 天 tian sky/day, 地 di earth/ground, 日 ri sun/day, "
            "月 yue moon/month, 星 xing star, 风 feng wind, 雨 yu rain, "
            "雪 xue snow, 雷 lei thunder, 云 yun cloud, 雾 wu fog, "
            "火 huo fire, 烟 yan smoke, 土 tu soil, "
            "石 shi stone, 金 jin gold/metal, "
            "铁 tie iron, 玉 yu jade, "
            "花 hua flower, 草 cao grass, 树 shu tree, 叶 ye leaf, "
            "根 gen root, 竹 zhu bamboo, 松 song pine, 梅 mei plum, "
            "稻 dao rice plant, 麦 mai wheat, 豆 dou bean, 瓜 gua melon, "
            "果 guo fruit, 桃 tao peach, 李 li plum, "
            "梨 li pear, 椒 jiao pepper, "
            "姜 jiang ginger, 葱 cong scallion, 蒜 suan garlic, "
            "盐 yan salt, 糖 tang sugar, 醋 cu vinegar, 酱 jiang sauce, "
            "油 you oil, 茶 cha tea, 酒 jiu wine, 汤 tang soup, "
            "粥 zhou porridge, 面 mian noodles, 粉 fen rice noodles, "
            "饼 bing cake, 馒 mantou steamed bun, 饺 jiao dumpling, "
            "包 bao bun, 粽 zong rice dumpling, 糕 gao cake, "
            "鸡 ji chicken, 鸭 ya duck, 鹅 e goose, 猪 zhu pig, "
            "牛 niu cow, 羊 yang sheep, 马 ma horse, 驴 lv donkey, "
            "狗 gou dog, 猫 mao cat, 鼠 shu rat, 兔 tu rabbit, "
            "虎 hu tiger, 狼 lang wolf, 熊 xiong bear, 猴 hou monkey, "
            "鸟 niao bird, 鱼 yu fish, 虾 xia shrimp, 蟹 xie crab, "
            "蛇 she snake, 虫 chong insect, "
            "蜂 feng bee, 蛙 wa frog, "
            "龙 long dragon, 爷 ye dad, 姆妈 muma mom, "
            "嗲嗲 diadie grandpa, 娭毑 aijie grandma, 堂客 tangke wife, "
            "细伢子 xiyazi kid, 崽 zai son, 细姑 xigu young aunt, "
            "朋友 pengyou friend, 同学 tongxue classmate, 同事 tongshi colleague, "
            "老师 laoshi teacher, 学生 xuesheng student, 医生 yisheng doctor, "
            "老板 laoban boss, 客人 keren guest, 主人 zhuren host, "
            "头 tou head, 脑壳 naoke head (Xiang), 眼 yan eye, 眼睛 yanjing eyes, "
            "耳 er ear, 鼻 bi nose, 口 kou mouth, 嘴 zui mouth, "
            "牙 ya tooth, 舌 she tongue, 喉 houlong throat, 颈根 jinggen neck, "
            "肩 jian shoulder, 手巴子 shoubazi arm, 手 shou hand, "
            "指码子 zhimazi finger, 膝头骨 xitougu knee, 腿 tui leg, "
            "脚 jiao foot, 心 xin heart, 肝 gan liver, 胃 wei stomach, "
            "肠 chang intestines, 血 xue blood, 骨 gu bone, 肉 rou meat, "
            "皮 pi skin, 毛 mao hair/fur, 眼眨毛 yanzhamao eyelashes, "
            "屋 wu house, 房 fang room, 堂屋 tangwu main hall, 厨房 chufang kitchen, "
            "门 men door, 窗 chuang window, 墙 qiang wall, 顶 ding roof, "
            "桌 zhuo table, 椅 yi chair, 床 chuang bed, 柜 gui cabinet, "
            "箱 xiang box, 包 bao bag, 灯 deng lamp, 镜 jing mirror, "
            "钟 zhong clock, 伞 san umbrella, 鞋 xie shoes, 衣 yi clothes, "
            "裤 ku pants, 帽 mao hat, 袜 wa socks, 被 bei quilt, "
            "枕 zhen pillow, 席 xi mat, 锅 guo wok, 碗 wan bowl, "
            "盘 pan plate, 杯 bei cup, 筷 kuai chopsticks, 勺 shao spoon, "
            "刀 dao knife, 桶 tong bucket, 盆 pen basin, 瓶 ping bottle, "
            "绳 sheng rope, 线 xian thread, 针 zhen needle, "
            "笔 bi pen, 纸 zhi paper, 书 shu book, 字 zi character, "
            "画 hua painting, 琴 qin instrument, 棋 qi chess, 诗 shi poem, "
            "车 che vehicle, 船 chuan boat, 飞机 feiji airplane, 火车 huoche train, "
            "地铁 ditie subway, 路 lu road, 桥 qiao bridge, 街 jie street, "
            "市 shi market/city, 店 dian shop, 厂 chang factory, "
            "校 xiao school, 院 yuan courtyard/institute, 寺 si temple, "
            "城 cheng city wall/town, 乡 xiang countryside, "
            "村 cun village, 镇 zhen town, 县 xian county, 省 sheng province, "
            "国 guo country, 世界 shijie world, \n\n"
            "Key grammar rules: SVO order; no verb inflection; classifiers "
            "个/只/条/坨; negation 不/冇/莫; questions with 啵/吗/冇 and "
            "question words 何解/么子/好钱/几时/啷个; aspect 了/咖/着/过; "
            "possession with 的; 把 construction; 比 comparison; final "
            "particles 啵/咯/撒/啦/哒. \n\n"
            "Phrase tables: greetings (恰饭了冇, 你好, 慢走), price (好钱, "
            "便宜点, 成交), directions (啷个走, 一直往前), time (今日子, "
            "明日子, 断黑), feelings (蛮开心, 好生气), farewells (一路顺"
            "风, 下次再来). \n\n"
            "Mastery drill: say all six tones; recite the 200 words; build "
            "ten sentences using ten different grammar rules; hold a "
            "three-minute market conversation; retell all three stories."
        ),
        "how_it_works": (
            "The mastery record is the final exam and the lifelong "
            "reference in one: the tone table for the ear, the 200-word "
            "table for the memory, the rule list for the grammar, the "
            "phrase tables for the tongue. Work it as a checklist - "
            "every item you cannot produce on demand goes back into "
            "daily drilling. The database is complete when this record "
            "is easy."
        ),
        "key_points": [
            "Full reference: tones, 200 core words, grammar rules, phrase tables.",
            "Six Changsha tones + Old Xiang five; initial/final counts.",
            "200-word table: characters + pinyin-style + English.",
            "All ten grammar rules restated; all phrase tables restated.",
            "Mastery drill: tones, words, rules, market talk, stories.",
        ],
        "requirements": [
            "Complete records 1-33 before the mastery drill.",
            "Every unproducible item returns to daily drilling.",
        ],
        "standards": [
            "Reference values repeat the phonology record exactly.",
            "Word table consolidates the database's vocabulary.",
            SENT_NOTE,
        ],
        "citations": [CIT_ETH, CIT_ISO, CIT_NORMAN, CIT_WU, CIT_BAOCHEN, CIT_ZHWIKI],
        "must_contain": ["200", "33", "13", "41", "24", "45", "21", "SVO", "咖", "phrase tables"],
        "sig_lens": (
            "Through the Signature lens mastery is the sworn seal of "
            "the whole ladder: 200 words, six tones, ten rules - one "
            "covenant that Xiang is carried complete."
        ),
        "drill": {
            "core_words": 200, "tones": 6, "grammar_rules": 10,
            "phrase_tables": 6,
        },
    },
]
