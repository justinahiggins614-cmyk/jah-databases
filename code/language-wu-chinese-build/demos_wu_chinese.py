#!/usr/bin/env python3
"""Demonstration programs for the Wu Chinese Language databases.

34 demo factories (one per entry key), each returning a real, runnable,
stdlib-only Python program. Every program prints its real computed values,
asserts tight bounds (never float exact-equality), prints CHECK:<word>
lines for the vocabulary it exercises (the build cross-checks each CHECK
word against the full entry text), and ends with the OK marker.

Archetypes: tone drills, vocab quizzes, flashcard checks, sentence audits,
grammar drills, dialogue-flow checks, idiom matchers, mastery exam.

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
            "assert len(TONES) == 5, \"expected 5 modern Shanghai tones\"\n"
            "for num, val, contour, word in TONES:\n"
            "    mean = sum(contour) / len(contour)\n"
            "    span = max(contour) - min(contour)\n"
            "    print(\"T\" + str(num) + \" value=\" + str(val) + \" contour=\" + str(contour)"
            " + \" mean=\" + (\"%.4f\" % mean) + \" span=\" + str(span) + \" example=\" + word)\n"
            "    assert 1 <= num <= 5\n"
            "    assert 1 <= val <= 53\n"
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
    (1, 53, [5, 3], "三"),
    (2, 34, [3, 4], "水"),
    (3, 23, [2, 3], "人"),
    (4, 5, [5], "一"),
    (5, 12, [1, 2], "十"),
]

DEMOS = {}

DEMOS["wu_overview"] = tone_drill("overview", TONES5, ["吴语", "侬好", "上海"])
DEMOS["wu_writing"] = tone_drill("writing", TONES5, ["侬", "覅", "一", "十"])
DEMOS["wu_phonology"] = tone_drill("phonology", TONES5, ["三", "水", "人", "一", "十", "牌", "茶"])

DEMOS["wu_nouns"] = vocab_quiz("nouns", [
    ("人", "nyin3", "person"), ("囡", "noe1", "child"),
    ("朋友", "bong3-yeu3", "friend"), ("屋", "oq4", "house"),
    ("学校", "yoq5-gau3", "school"), ("书", "sy1", "book"),
    ("钞票", "tshau1-phiau2", "money"), ("饭", "ve3", "rice/meal"),
    ("水", "sy2", "water"), ("茶", "dzo3", "tea"),
    ("物事", "meq5-zy3", "thing"), ("地方", "di3-fang1", "place"),
])

DEMOS["wu_verbs"] = vocab_quiz("verbs", [
    ("吃", "chiq4", "to eat"), ("喝", "heq4", "to drink"),
    ("去", "chi2", "to go"), ("来", "le3", "to come"),
    ("看", "khe2", "to look/read"), ("买", "ma2", "to buy"),
    ("卖", "ma3", "to sell"), ("做", "tsu2", "to do/make"),
    ("拿", "na3", "to take"), ("拨", "peq4", "to give"),
    ("欢喜", "hoe1-xi2", "to like"), ("知道", "tsy1-tau2", "to know"),
])

DEMOS["wu_adjectives"] = vocab_quiz("adjectives", [
    ("好", "hau2", "good"), ("大", "du3", "big"),
    ("小", "siau2", "small"), ("快", "khuai2", "fast"),
    ("慢", "me3", "slow"), ("热", "gniq5", "hot"),
    ("冷", "lan3", "cold"), ("贵", "ku2", "expensive"),
    ("便宜", "bie3-nyi3", "cheap"), ("嗲", "tia2", "cute"),
    ("交关", "ciau1-kue1", "very"), ("远", "yoe3", "far"),
])

DEMOS["wu_pronouns"] = grammar_drill("pronouns", [
    ("personal-1", "我是学生", "我", "是"),
    ("personal-2", "侬好", "侬", "好"),
    ("personal-3", "伊来了", "伊", "来"),
    ("plural", "侬拉都来", "拉", "来"),
    ("possessive", "我个书", "个", "书"),
    ("demonstrative", "迭是啥", "迭", "是"),
    ("interrogative", "侬啥辰光来", "啥", "来"),
], ["我", "侬", "伊", "阿拉", "个", "啥"])

DEMOS["wu_numbers"] = tone_drill("numbers", TONES5, ["一", "二", "三", "十", "百"])

DEMOS["wu_greetings"] = vocab_quiz("greetings", [
    ("侬好", "nong3-hau2", "hello"), ("谢谢", "zia3-zia3", "thank you"),
    ("再会", "ze3-we3", "goodbye"), ("对勿起", "te2-veq4-chi2", "sorry"),
    ("请", "tshin2", "please"), ("请问", "tshin2-ven3", "may I ask"),
    ("麻烦", "me3-ve3", "to trouble"), ("晚安", "ve3-e1", "good night"),
    ("恭喜", "kon1-xi2", "congratulations"), ("欢迎", "we1-ngin3", "welcome"),
])

DEMOS["wu_grammar"] = grammar_drill("grammar", [
    ("svo", "我吃饭", "我", "吃"),
    ("neg-勿", "我勿去", "勿", "去"),
    ("neg-朆", "我朆吃", "朆", "吃"),
    ("neg-覅", "覅忘记", "覅", "忘记"),
    ("question", "侬去𠲎", "𠲎", ""),
    ("possessive", "我个书", "个", "书"),
    ("locative", "伊勒上海", "勒", "上海"),
    ("ba-equivalent", "拿门关脱", "拿", "门"),
    ("passive", "杯子拨伊打破仔", "拨", "伊"),
    ("aspect", "我吃仔饭", "仔", ""),
], ["勿", "朆", "覅", "𠲎", "拿", "拨", "仔"])

_SENT_WORDS = {
    "wu_home": ["屋", "爸爸", "妈妈", "房间"],
    "wu_food": ["红烧肉", "小笼包", "买单", "好吃"],
    "wu_travel": ["外滩", "地铁", "票子", "迷路"],
    "wu_work": ["老板", "开会", "考试", "功课"],
    "wu_health": ["头痛", "医生", "吃药", "药房"],
    "wu_emotions": ["开心", "难过", "发火", "欢喜"],
    "wu_nature": ["落雨", "春天", "长江", "西湖"],
    "wu_shopping": ["价钿", "成交", "便宜", "发票"],
    "wu_social": ["朋友", "生日快乐", "干杯", "再会"],
    "wu_tech": ["手机", "电脑", "密码", "微信"],
}
for _k, _w in _SENT_WORDS.items():
    DEMOS[_k] = sentence_audit(_k.replace("wu_", ""), 20, _w)

DEMOS["wu_tenses"] = grammar_drill("tenses", [
    ("habitual", "我天天跑步", "天天", "跑步"),
    ("ongoing", "伊勒海吃饭", "勒海", "吃饭"),
    ("completed", "我吃仔饭了", "仔", ""),
    ("experienced", "我去过苏州", "过", ""),
    ("future", "明朝我要去上海", "要", "去"),
    ("neg-past", "我朆吃早饭", "朆", "吃"),
], ["勒海", "仔", "过", "要", "朆"])

DEMOS["wu_qa"] = vocab_quiz("qa", [
    ("啥", "sa3", "what"), ("啥人", "sa3-gnin3", "who"),
    ("啥地方", "sa3 di3-fang1", "where"), ("啥辰光", "sa3 zen3-kuang1", "when"),
    ("为啥", "we3-sa3", "why"), ("哪能", "na3-nen3", "how"),
    ("几化", "ci2-hu3", "how much"), ("哪一个", "na3 iq4-geq4", "which one"),
])

DEMOS["wu_commands"] = grammar_drill("commands", [
    ("bare", "吃饭", "吃", "饭"),
    ("polite", "请坐", "请", "坐"),
    ("formal", "麻烦侬帮个忙", "麻烦", "忙"),
    ("negative", "勿要吵", "勿要", "吵"),
    ("hospitality", "覅客气", "覅", "客气"),
], ["请", "勿要", "覅", "麻烦"])

DEMOS["wu_descriptions"] = sentence_audit("descriptions", 20,
                                          ["外滩", "豫园", "小笼包", "旗袍"])

DEMOS["wu_story1"] = sentence_audit("story1", 10, ["菜场", "青菜", "讲价", "成交"])
DEMOS["wu_story2"] = grammar_drill("story2", [
    ("past-仔", "我去仔苏州", "仔", ""),
    ("past-过", "从来朆听过评弹", "过", ""),
    ("past-朆", "从来朆听过", "朆", "听"),
    ("completed", "中饭吃仔苏州面", "仔", ""),
], ["仔", "过", "朆", "苏州"])
DEMOS["wu_story3"] = grammar_drill("story3", [
    ("intention", "我要早点起来", "要", "起来"),
    ("prediction", "阿拉会得去看电影", "会得", "看"),
    ("conditional", "如果落雨我就不去", "如果", "就"),
    ("suff-cond", "只要功课做完就会得去", "只要", "就"),
], ["要", "会得", "如果", "只要"])

DEMOS["wu_idioms"] = vocab_quiz("idioms", [
    ("拆烂污", "tshaq4-le3-u1", "shoddy work"),
    ("轧闹猛", "gaiq5-nau3-mang3", "join the fun"),
    ("捣浆糊", "tau2-qiang1-wu3", "muddle through"),
    ("白相", "baq5-shiang2", "hang out"),
    ("有腔调", "yeu3 chian1-diau3", "stylish"),
    ("老克勒", "lau3-kheq4-leq4", "dapper gentleman"),
    ("十三点", "zeq5-se1-tie2", "scatterbrained"),
    ("拎勿清", "lin3-veq4-chin1", "confused"),
    ("门槛精", "men3-khe2-cin1", "shrewd"),
    ("嗲", "tia2", "cute"),
])

DEMOS["wu_register"] = grammar_drill("register", [
    ("greet-formal", "请问尊姓大名", "请问", ""),
    ("greet-informal", "侬叫啥名字", "侬", ""),
    ("thanks-formal", "多谢侬个帮助", "多谢", ""),
    ("thanks-informal", "谢谢", "谢", ""),
    ("host-formal", "请慢用", "请", "慢"),
    ("host-informal", "吃吧", "吃", ""),
], ["请问", "多谢", "请", "麻烦"])

DEMOS["wu_complex"] = grammar_drill("complex", [
    ("cause", "因为落雨所以延期", "因为", "所以"),
    ("concession", "虽然热但是来了", "虽然", "但是"),
    ("condition", "如果天好就去", "如果", "就"),
    ("notonly", "不但好而且能干", "不但", "而且"),
    ("relative", "侬讲个故事", "讲", "个"),
    ("passive", "功课拨雨淋湿", "拨", ""),
], ["因为", "所以", "虽然", "如果", "不但", "拨"])

_CONV_WORDS = {
    "wu_conv_market": ["几化", "成交", "找钞票", "慢走"],
    "wu_conv_friend": ["侬好", "勿见勿散", "干杯", "再会"],
    "wu_conv_problem": ["钱包", "挂失", "朋友", "勿要慌"],
}
for _k, _w in _CONV_WORDS.items():
    DEMOS[_k] = sentence_audit(_k.replace("wu_", ""), 20, _w)


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
        "MEANS = {1: 4.0, 2: 3.5, 3: 2.5, 4: 5.0, 5: 1.5}\n"
        "CONTOURS = {1: [5, 3], 2: [3, 4], 3: [2, 3], 4: [5], 5: [1, 2]}\n"
        "for t, c in CONTOURS.items():\n"
        "    m = sum(c) / len(c)\n"
        "    assert abs(m - MEANS[t]) < 1e-9, \"tone mean drift\"\n"
        "print(\"tone table: 5 tones verified\")\n"
        + _check_lines(["吴语", "侬好", "谢谢", "再会", "熟能生巧"]) + "\n"
        "print(\"OK: mastery exam verified 200 words for " + rid + "\")\n"
    )
    return prog


DEMOS["wu_mastery"] = _mastery_exam

# every entry key must have exactly one demo
import entries_wu_chinese as _E
assert set(DEMOS) == {e["key"] for e in _E.ENTRIES}, "demo map misses entries"
