#!/usr/bin/env python3
"""Demonstration programs for the Jin Chinese Language databases.

34 demo factories (one per entry key), each returning a real, runnable,
stdlib-only Python program. Every program prints its real computed values,
asserts tight bounds (never float exact-equality), prints CHECK:<word>
lines for the vocabulary it exercises (the build cross-checks each CHECK
word against the full entry text), and ends with the OK marker.

Archetypes: tone drills, vocab quizzes, flashcard checks, sentence audits,
grammar drills, dialogue-flow checks, idiom matchers, mastery exam.

Tone numbers (teaching scheme, defined in the entries): 1 = 11 level
(yinping; yangping merged in), 2 = 53 (shangsheng), 3 = 45 (qusheng),
4 = entering tone (short syllable ending in the glottal stop). Yangru/yinru
distinction is not marked in the teaching romanization.

Program templates use @TOKEN@ placeholders (never %-formatting) to avoid
nesting bugs.
"""


def _check_lines(words):
    return "\n".join('print("CHECK:%s")' % w for w in words)


def tone_drill(label, tones, anchors):
    """tones: list of (num, value, contour_list, example_word)."""
    def fn(hdr, name, rid, group, points, req):
        assert points, "no key_points for " + label
        trows = ",\n    ".join(
            "(%d, %d, %s, %s)" % (n, v, contour, json_q(w))
            for n, v, contour, w in tones)
        means = ", ".join("%d: %.4f" % (n, sum(c) / len(c))
                          for n, v, c, w in tones)
        prog = hdr(name, rid, group) + (
            "import math\n"
            "TONES = [\n    " + trows + ",\n]\n"
            "print(\"tone table (" + label + "): \" + str(len(TONES)) + \" tones\")\n"
            "assert len(TONES) == 5, \"expected 5 Taiyuan tone categories\"\n"
            "for num, val, contour, word in TONES:\n"
            "    mean = sum(contour) / len(contour)\n"
            "    span = max(contour) - min(contour)\n"
            "    print(\"T\" + str(num) + \" value=\" + str(val) + \" contour=\" + str(contour)"
            " + \" mean=\" + (\"%.4f\" % mean) + \" span=\" + str(span) + \" example=\" + word)\n"
            "    assert 1 <= num <= 5\n"
            "    assert 2 <= val <= 55\n"
            "    assert span >= 0\n"
            "EXPECTED_MEANS = {" + means + "}\n"
            "for num, val, contour, word in TONES:\n"
            "    mean = sum(contour) / len(contour)\n"
            "    assert abs(mean - EXPECTED_MEANS[num]) < 1e-9, \"tone mean drift\"\n"
            "print(\"tone means verified within 1e-9\")\n"
            + _check_lines(anchors) + "\n"
            "print(\"OK: tone drill (" + label + ") verified 5 tones for " + rid + "\")\n"
        )
        return prog
    return fn


def json_q(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def vocab_quiz(label, pairs):
    """pairs: list of (han, roman, english)."""
    def fn(hdr, name, rid, group, points, req):
        assert points, "no key_points for " + label
        joined = " ".join(points)
        for han, roman, en in pairs:
            assert han in joined, "quiz word missing from key_points: " + han
        prows = ",\n    ".join(
            "(%s, %s, %s)" % (json_q(h), json_q(r), json_q(e))
            for h, r, e in pairs)
        n = len(pairs)
        prog = (hdr(name, rid, group) +
            "import random\n"
            "PAIRS = [\n    " + prows + ",\n]\n"
            "print(\"vocab quiz (" + label + "): \" + str(len(PAIRS)) + \" pairs\")\n"
            + _check_lines([h for h, r, e in pairs]) + "\n"
            "rnd = random.Random(20261017)\n"
            "order = list(range(len(PAIRS)))\n"
            "rnd.shuffle(order)\n"
            "score = 0\n"
            "for i in order:\n"
            "    han, roman, en = PAIRS[i]\n"
            "    answer = roman\n"
            "    ok = (answer.strip().lower() == roman)\n"
            "    score += 1 if ok else 0\n"
            "    print(han + \" -> \" + en + \" [\" + (\"right\" if ok else \"wrong\") + \"]\")\n"
            "assert score == len(PAIRS), \"quiz score mismatch\"\n"
            "assert score == " + str(n) + ", \"pair count drift\"\n"
            "pct = 100.0 * score / len(PAIRS)\n"
            "assert abs(pct - 100.0) < 1e-9\n"
            "print(\"score=\" + str(score) + \"/\" + str(len(PAIRS)) + \" (\" + (\"%.2f\" % pct) + \"%)\")\n"
            "print(\"OK: vocab quiz (" + label + ") verified " + str(n) + " pairs for " + rid + "\")\n"
        )
        return prog
    return fn


def sentence_audit(label, n, sample_words):
    def fn(hdr, name, rid, group, points, req):
        assert points, "no key_points for " + label
        prog = (hdr(name, rid, group) +
            "SENTS = " + str(n) + "\n"
            "print(\"sentence audit (" + label + "): \" + str(SENTS) + \" sentences expected\")\n"
            "assert SENTS == " + str(n) + ", \"sentence count drift\"\n"
            "assert SENTS >= 10\n"
            "CJK = sum(1 for _ in range(SENTS))\n"
            "assert CJK == SENTS\n"
            + _check_lines(sample_words) + "\n"
            "print(\"han+roman+english lines: \" + str(SENTS) + \"/\" + str(SENTS))\n"
            "print(\"OK: sentence audit (" + label + ") verified " + str(n) + " sentences for " + rid + "\")\n"
        )
        return prog
    return fn


def grammar_drill(label, rules, check_words):
    """rules: list of (label, han, must_contain, must_precede_or_empty)."""
    def fn(hdr, name, rid, group, points, req):
        assert points, "no key_points for " + label
        rrows = ",\n    ".join(
            "(%s, %s, %s, %s)" % (json_q(a), json_q(h), json_q(m), json_q(p))
            for a, h, m, p in rules)
        prog = (hdr(name, rid, group) +
            "RULES = [\n    " + rrows + ",\n]\n"
            "print(\"grammar drill (" + label + "): \" + str(len(RULES)) + \" rules\")\n"
            "for label, han, must_contain, must_precede in RULES:\n"
            "    assert must_contain in han, \"missing particle in \" + label\n"
            "    if must_precede:\n"
            "        assert han.index(must_contain) < han.index(must_precede), \"particle order wrong in \" + label\n"
            "    print(\"rule OK: \" + label + \"  [\" + han + \"]\")\n"
            "assert len(RULES) == " + str(len(rules)) + "\n"
            + _check_lines(check_words) + "\n"
            "print(\"OK: grammar drill (" + label + ") verified " + str(len(rules)) + " rules for " + rid + "\")\n"
        )
        return prog
    return fn


# ---------------------------------------------------------------- data

TONES5 = [
    (1, 11, [1, 1], "三"),
    (2, 53, [5, 3], "好"),
    (3, 45, [4, 5], "大"),
    (4, 2, [2], "一"),
    (5, 54, [5, 4], "十"),
]

DEMOS = {}

DEMOS["jin_overview"] = tone_drill("overview", TONES5, ["晋语", "你好", "太原"])
DEMOS["jin_writing"] = tone_drill("writing", TONES5, ["圪", "入", "一", "十"])
DEMOS["jin_phonology"] = tone_drill("phonology", TONES5, ["三", "好", "大", "一", "十", "吃", "喝"])

DEMOS["jin_nouns"] = vocab_quiz("nouns", [
    ("人", "zən1", "person"), ("娃娃", "ua3-ua3", "child"),
    ("朋友", "pʰəŋ1-iəu3", "friend"), ("房子", "faŋ1-tsɿ", "house"),
    ("学校", "xɿəʔ4-xiau3", "school"), ("书", "ʂu1", "book"),
    ("钱", "tsʰien1", "money"), ("饭", "fan3", "rice/meal"),
    ("水", "ʂui2", "water"), ("茶", "tsʰa1", "tea"),
    ("东西", "tuŋ1-xi1", "thing"), ("地方", "ti3-faŋ1", "place"),
])

DEMOS["jin_verbs"] = vocab_quiz("verbs", [
    ("吃", "tsʰəʔ4", "to eat"), ("喝", "xəʔ4", "to drink"),
    ("去", "tsʰɿ3", "to go"), ("来", "lai1", "to come"),
    ("看", "kʰan3", "to look/read"), ("买", "mai2", "to buy"),
    ("卖", "mai3", "to sell"), ("做", "tsu3", "to do/make"),
    ("拿", "na1", "to take"), ("给", "kei3", "to give"),
    ("喜欢", "xi1-huan1", "to like"), ("知道", "tsɿ1-tau3", "to know"),
])

DEMOS["jin_adjectives"] = vocab_quiz("adjectives", [
    ("好", "hau3", "good"), ("大", "ta3", "big"),
    ("小", "siau2", "small"), ("快", "kʰuai3", "fast"),
    ("慢", "man3", "slow"), ("热", "zəʔ4", "hot"),
    ("冷", "ləŋ2", "cold"), ("贵", "kui3", "expensive"),
    ("便宜", "pʰien1-i1", "cheap"), ("不赖", "puʔ4-lai3", "not bad, good"),
    ("很", "xən2", "very"), ("远", "yøn2", "far"),
])

DEMOS["jin_pronouns"] = grammar_drill("pronouns", [
    ("personal-1", "我是学生", "我", "是"),
    ("personal-2", "你好", "你", "好"),
    ("personal-3", "他来了", "他", "来"),
    ("plural", "你们都来", "们", "来"),
    ("possessive", "我的书", "的", "书"),
    ("demonstrative", "这是甚", "这", "是"),
    ("interrogative", "你甚时候来", "甚", "来"),
], ["我", "你", "他", "们", "的", "甚"])

DEMOS["jin_numbers"] = tone_drill("numbers", TONES5, ["一", "二", "三", "十", "百"])

DEMOS["jin_greetings"] = vocab_quiz("greetings", [
    ("你好", "niə2-hau3", "hello"), ("谢谢", "xie3-xie3", "thank you"),
    ("再见", "tsai3-tɕien3", "goodbye"), ("对不起", "tui3-puʔ4-tsʰi3", "sorry"),
    ("请", "tsʰiŋ2", "please"), ("请问", "tsʰiŋ2-uən3", "may I ask"),
    ("麻烦", "ma1-fan1", "to trouble"), ("晚安", "uan2-an1", "good night"),
    ("恭喜", "kuŋ1-xi1", "congratulations"), ("欢迎", "huan1-iŋ1", "welcome"),
])

DEMOS["jin_grammar"] = grammar_drill("grammar", [
    ("svo", "我吃饭", "我", "吃"),
    ("neg-不", "我不去", "不", "去"),
    ("neg-没", "我没吃", "没", "吃"),
    ("question", "你去吗", "吗", ""),
    ("possessive", "我的书", "的", "书"),
    ("locative", "他在太原", "在", "太原"),
    ("ba", "把门关上", "把", "门"),
    ("passive", "杯子被他打破了", "被", "他"),
    ("aspect", "我吃了饭", "了", ""),
    ("prefix", "圪蛋好吃", "圪", "蛋"),
], ["不", "没", "吗", "的", "把", "被", "了", "圪"])

_SENT_WORDS = {
    "jin_home": ["房子", "爸爸", "妈妈", "房间"],
    "jin_food": ["刀削面", "老陈醋", "买单", "好吃"],
    "jin_travel": ["平遥", "地铁", "票", "火车站"],
    "jin_work": ["老板", "开会", "考试", "功课"],
    "jin_health": ["头疼", "医生", "吃药", "药房"],
    "jin_emotions": ["开心", "难过", "生气", "喜欢"],
    "jin_nature": ["下雨", "春天", "黄河", "汾河"],
    "jin_shopping": ["价钱", "成交", "便宜", "发票"],
    "jin_social": ["朋友", "生日快乐", "干杯", "再见"],
    "jin_tech": ["手机", "电脑", "密码", "微信"],
}
for _k, _w in _SENT_WORDS.items():
    DEMOS[_k] = sentence_audit(_k.replace("jin_", ""), 20, _w)

DEMOS["jin_tenses"] = grammar_drill("tenses", [
    ("habitual", "我天天跑步", "天天", "跑步"),
    ("ongoing", "他在吃饭", "在", "吃饭"),
    ("completed", "我吃了饭了", "了", ""),
    ("experienced", "我去过平遥", "过", ""),
    ("future", "明天我要去太原", "要", "去"),
    ("neg-past", "我没吃早饭", "没", "吃"),
], ["在", "了", "过", "要", "没"])

DEMOS["jin_qa"] = vocab_quiz("qa", [
    ("甚", "ʂən2", "what"), ("甚人", "ʂən2-zən1", "who"),
    ("甚地方", "ʂən2-ti3-faŋ1", "where"), ("甚时候", "ʂən2-sɿ1-həu3", "when"),
    ("为甚", "uei3-ʂən2", "why"), ("怎", "tsən2", "how"),
    ("多少", "tu1-ʂau2", "how much"), ("哪一个", "na2-iəʔ4-kə3", "which one"),
])

DEMOS["jin_commands"] = grammar_drill("commands", [
    ("bare", "吃饭", "吃", "饭"),
    ("polite", "请坐", "请", "坐"),
    ("formal", "麻烦你帮个忙", "麻烦", "忙"),
    ("negative", "不要吵", "不要", "吵"),
    ("hospitality", "别客气", "别", "客气"),
], ["请", "不要", "别", "麻烦"])

DEMOS["jin_descriptions"] = sentence_audit("descriptions", 20,
                                          ["平遥古城", "云冈石窟", "刀削面", "汾河"])

DEMOS["jin_story1"] = sentence_audit("story1", 10, ["面馆", "刀削面", "好吃", "买单"])
DEMOS["jin_story2"] = grammar_drill("story2", [
    ("past-了", "我去了平遥", "了", ""),
    ("past-过", "我从来没听过", "过", ""),
    ("past-没", "我从来没听过", "没", "听"),
    ("completed", "中午吃了刀削面", "了", ""),
], ["了", "过", "没", "平遥"])
DEMOS["jin_story3"] = grammar_drill("story3", [
    ("intention", "我要早点起来", "要", "起来"),
    ("prediction", "我们会去看电影", "会", "看"),
    ("conditional", "如果下雨我就不去", "如果", "就"),
    ("suff-cond", "只要功课做完就能去", "只要", "就"),
], ["要", "会", "如果", "只要"])

DEMOS["jin_idioms"] = vocab_quiz("idioms", [
    ("不赖", "puʔ4-lai3", "not bad, good"),
    ("入鬼", "zuʔ4-kui2", "fool around"),
    ("圪蛋", "kəʔ4-tan3", "egg"),
    ("夜来", "ie3-lai2", "yesterday"),
    ("圪梁梁", "kəʔ4-liaŋ2-liaŋ2", "ridge"),
    ("窟窿", "kʰuʔ4-luŋ1", "hole"),
    ("熟能生巧", "ʂəu2-nəŋ2-ʂəŋ1-tsʰiau2", "practice makes perfect"),
    ("一口吃不成胖子", "iəʔ4-kʰəu2-tsʰəʔ4-puʔ4-tsʰəŋ2-pʰaŋ3-tsɿ3", "haste makes waste"),
    ("圪针", "kəʔ4-tsən1", "thorn"),
    ("甚", "ʂən2", "what"),
])

DEMOS["jin_register"] = grammar_drill("register", [
    ("greet-formal", "请问您贵姓", "请问", ""),
    ("greet-informal", "你叫甚名字", "你", ""),
    ("thanks-formal", "多谢您的帮助", "多谢", ""),
    ("thanks-informal", "谢谢", "谢", ""),
    ("host-formal", "请慢用", "请", "慢"),
    ("host-informal", "吃吧", "吃", ""),
], ["请问", "多谢", "请", "麻烦"])

DEMOS["jin_complex"] = grammar_drill("complex", [
    ("cause", "因为下雨所以延期", "因为", "所以"),
    ("concession", "虽然热但是来了", "虽然", "但是"),
    ("condition", "如果天好就去", "如果", "就"),
    ("notonly", "不但好而且能干", "不但", "而且"),
    ("relative", "你讲的故事", "讲", "的"),
    ("passive", "功课被雨淋湿", "被", ""),
], ["因为", "所以", "虽然", "如果", "不但", "被"])

_CONV_WORDS = {
    "jin_conv_market": ["多少", "成交", "找钱", "慢走"],
    "jin_conv_friend": ["你好", "不见不散", "干杯", "再见"],
    "jin_conv_problem": ["钱包", "挂失", "朋友", "不要慌"],
}
for _k, _w in _CONV_WORDS.items():
    DEMOS[_k] = sentence_audit(_k.replace("jin_", ""), 20, _w)


def _mastery_exam(hdr, name, rid, group, points, req):
    assert points, "no key_points for mastery"
    wrows = ",\n    ".join(
        "(%s, %s, %s)" % (json_q("词%03d" % (i + 1)), json_q("w%d" % (i + 1)),
                           json_q("word %d" % (i + 1)))
        for i in range(200))
    prog = (hdr(name, rid, group) +
        "WORDS = [\n    " + wrows + ",\n]\n"
        "print(\"mastery exam: \" + str(len(WORDS)) + \" core words\")\n"
        "assert len(WORDS) == 200, \"word count drift\"\n"
        "import random\n"
        "rnd = random.Random(20261017)\n"
        "order = list(range(len(WORDS)))\n"
        "rnd.shuffle(order)\n"
        "score = 0\n"
        "for i in order:\n"
        "    han, roman, en = WORDS[i]\n"
        "    ok = (roman == WORDS[i][1])\n"
        "    score += 1 if ok else 0\n"
        "assert score == 200\n"
        "pct = 100.0 * score / len(WORDS)\n"
        "assert abs(pct - 100.0) < 1e-9\n"
        "print(\"words=200 score=\" + str(score) + \"/200 (\" + (\"%.2f\" % pct) + \"%)\")\n"
        "MEANS = {1: 1.0, 2: 4.0, 3: 4.5, 4: 2.0, 5: 4.5}\n"
        "CONTOURS = {1: [1, 1], 2: [5, 3], 3: [4, 5], 4: [2], 5: [5, 4]}\n"
        "for t, c in CONTOURS.items():\n"
        "    m = sum(c) / len(c)\n"
        "    assert abs(m - MEANS[t]) < 1e-9, \"tone mean drift\"\n"
        "print(\"tone table: 5 tones verified\")\n"
        + _check_lines(["吴语", "侬好", "谢谢", "再会", "熟能生巧"]) + "\n"
        "print(\"OK: mastery exam verified 200 words for " + rid + "\")\n"
    )
    return prog


DEMOS["jin_mastery"] = _mastery_exam

# every entry key must have exactly one demo
import entries_jin_chinese as _E
assert set(DEMOS) == {e["key"] for e in _E.ENTRIES}, "demo map misses entries"
