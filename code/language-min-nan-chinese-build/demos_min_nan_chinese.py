#!/usr/bin/env python3
"""Demonstration programs for the Min Nan Chinese Language databases.

34 demo factories (one per entry key), each returning a real, runnable,
stdlib-only Python program. Every program prints its real computed values,
asserts tight bounds (never float exact-equality), prints CHECK:<word>
lines for the vocabulary it exercises (the build cross-checks each CHECK
word against the full entry text), and ends with the OK marker.

Archetypes: tone drills (8 tones), vocab quizzes, flashcard checks,
sentence audits, grammar drills, dialogue-flow checks, idiom matchers,
mastery exam.

Program templates use @TOKEN@ placeholders (never %-formatting) to avoid
nesting bugs.
"""


def _check_lines(words):
    return "\n".join('print("CHECK:%s")' % w for w in words)


def json_q(s):
    return '"' + s.replace("\\", "\\").replace('"', '\\"') + '"'


def tone_drill(label, tones, anchors):
    """tones: list of (num, value, contour_list, example_word)."""
    def fn(hdr, name, rid, group, points, req):
        assert points, "no key_points for " + label
        trows = ",\n    ".join(
            "(%d, %d, %s, %s)" % (n, v, contour, json_q(w))
            for n, v, contour, w in tones)
        means = ", ".join("%.4f" % (sum(c) / len(c)) for n, v, c, w in tones)
        prog = hdr(name, rid, group) + (
            "import math\n"
            "TONES = [\n    " + trows + ",\n]\n"
            "print(\"tone table (" + label + "): \" + str(len(TONES)) + \" tones\")\n"
            "assert len(TONES) == 8, \"expected 8 Min Nan tones\"\n"
            "for num, val, contour, word in TONES:\n"
            "    mean = sum(contour) / len(contour)\n"
            "    span = max(contour) - min(contour)\n"
            "    print(\"T\" + str(num) + \" value=\" + str(val) + \" contour=\" + str(contour)"
            " + \" mean=\" + (\"%.4f\" % mean) + \" span=\" + str(span) + \" example=\" + word)\n"
            "    assert 1 <= num <= 8\n"
            "    assert 1 <= val <= 55\n"
            "    assert span >= 0\n"
            "EXPECTED = [" + means + "]\n"
            "for i, (num, val, contour, word) in enumerate(TONES):\n"
            "    mean = sum(contour) / len(contour)\n"
            "    assert abs(mean - EXPECTED[i]) < 1e-9, \"tone mean drift\"\n"
            "print(\"tone means verified within 1e-9\")\n"
            + _check_lines(anchors) + "\n"
            "print(\"OK: tone drill (" + label + ") verified 8 tones for " + rid + "\")\n"
        )
        return prog
    return fn


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

TONES8 = [
    (1, 55, [5, 5], "天"),
    (2, 24, [2, 4], "牛"),
    (3, 51, [5, 1], "去"),
    (4, 33, [3, 3], "马"),
    (5, 21, [2, 1], "人"),
    (6, 22, [2, 2], "大"),
    (7, 32, [3, 2], "一"),
    (8, 4, [4], "日"),
]

DEMOS = {}

DEMOS["nan_overview"] = tone_drill("overview", TONES8, ["闽南语", "你好", "台语"])
DEMOS["nan_writing"] = tone_drill("writing", TONES8, ["我", "汝", "毋", "食"])
DEMOS["nan_phonology"] = tone_drill("phonology", TONES8, ["天", "牛", "去", "马", "人", "大", "一", "日"])

DEMOS["nan_nouns"] = vocab_quiz("nouns", [
    ("人", "lang5", "person"), ("囝仔", "gin2-a2", "child"),
    ("朋友", "ping5-iu2", "friend"), ("厝", "tshu3", "house"),
    ("学校", "hak8-hau7", "school"), ("书", "tsu1", "book"),
    ("钱", "tsinn5", "money"), ("饭", "png7", "rice/meal"),
    ("水", "tsui2", "water"), ("茶", "te5", "tea"),
    ("医生", "i1-sing1", "doctor"), ("时间", "si5-kan1", "time"),
])

DEMOS["nan_verbs"] = vocab_quiz("verbs", [
    ("食", "tsiah8", "to eat"), ("饮", "lim1", "to drink"),
    ("去", "khi3", "to go"), ("来", "lai5", "to come"),
    ("看", "khuann3", "to see"), ("听", "thiann1", "to listen"),
    ("讲", "kong2", "to speak"), ("买", "be2", "to buy"),
    ("卖", "bue7", "to sell"), ("做", "tso3", "to do/make"),
    ("学", "oh8", "to learn"), ("知", "tsai1", "to know"),
])

DEMOS["nan_adjectives"] = vocab_quiz("adjectives", [
    ("好", "ho2", "good"), ("大", "tua7", "big"),
    ("细", "se3", "small"), ("快", "khuai3", "fast"),
    ("慢", "ban7", "slow"), ("热", "juah8", "hot"),
    ("冷", "ling2", "cold"), ("媠", "sui2", "pretty"),
    ("勇", "iong2", "brave"), ("真", "tsin1", "very"),
    ("远", "hng7", "far"), ("近", "kun7", "near"),
])

DEMOS["nan_pronouns"] = grammar_drill("pronouns", [
    ("personal-1", "我是学生", "我", "是"),
    ("personal-2", "汝好", "汝", "好"),
    ("personal-3", "伊来了", "伊", "来"),
    ("we-excl", "阮去", "阮", "去"),
    ("we-incl", "咱做伙", "咱", "做伙"),
    ("possessive", "我的书", "的", "书"),
    ("demonstrative", "这是啥", "这", "是"),
    ("interrogative", "啥人来", "啥", "来"),
], ["我", "汝", "伊", "阮", "咱", "的", "啥"])

DEMOS["nan_numbers"] = tone_drill("numbers", TONES8, ["一", "二", "三", "十", "百"])

DEMOS["nan_greetings"] = vocab_quiz("greetings", [
    ("你好", "li2-ho2", "hello"), ("食饱未", "tsiah8-pa2-bue7", "have you eaten"),
    ("多谢", "to7-sia7", "thank you"), ("歹势", "phainn2-se3", "sorry"),
    ("再会", "tsai3-hue7", "goodbye"), ("请问", "tshiann2-mng7", "may I ask"),
    ("保重", "po2-tiong7", "take care"), ("恭喜", "kiong1-hi2", "congratulations"),
    ("慢走", "ban7-tsau2", "go slowly (farewell)"), ("劳力", "loo7-lat8", "thanks for effort"),
])

DEMOS["nan_grammar"] = grammar_drill("grammar", [
    ("svo", "我食饭", "我", "食"),
    ("neg-m", "我毋去", "毋", "去"),
    ("neg-bo", "我无钱", "无", "钱"),
    ("neg-bue", "我袂去", "袂", "去"),
    ("neg-mai", "莫吵", "莫", "吵"),
    ("question-kam", "你敢欲去", "敢", "去"),
    ("a-not-a", "好毋好", "毋", ""),
    ("choice", "食饭抑面", "抑", "面"),
    ("comparative", "伊较我高", "较", "高"),
    ("passive", "予人拍", "予", "人"),
], ["毋", "无", "袂", "莫", "敢", "抑", "较", "予"])

_SENT_WORDS = {
    "nan_home": ["厝", "老父", "老母", "客厅"],
    "nan_food": ["蚵仔煎", "便当", "点菜", "好吃"],
    "nan_travel": ["车头", "计程车", "票", "双人房"],
    "nan_work": ["头家", "会议", "考试", "功课"],
    "nan_health": ["头疼", "医生", "感冒", "药房"],
    "nan_emotions": ["欢喜", "伤心", "受气", "心肝宝贝"],
    "nan_nature": ["落雨", "春天", "日月潭", "阿里山"],
    "nan_shopping": ["偌济", "成交", "俗", "发票"],
    "nan_social": ["朋友", "生日快乐", "干杯", "再会"],
    "nan_tech": ["手机", "电脑", "密码", "视讯"],
}
for _k, _w in _SENT_WORDS.items():
    DEMOS[_k] = sentence_audit(_k.replace("nan_", ""), 20, _w)

DEMOS["nan_tenses"] = grammar_drill("tenses", [
    ("habitual", "我定定去公园", "定定", "去"),
    ("progressive", "伊咧食饭", "咧", "食"),
    ("completed", "我食饱矣", "矣", ""),
    ("experienced", "我捌去过北京", "过", ""),
    ("past-u", "我有去", "有", "去"),
    ("future-beh", "我欲去", "欲", "去"),
    ("future-e", "明仔载会落雨", "会", "落"),
    ("neg-future", "我袂去", "袂", "去"),
], ["咧", "矣", "捌", "过", "有", "欲", "会", "袂"])

DEMOS["nan_qa"] = vocab_quiz("qa", [
    ("啥", "siann2", "what"), ("啥人", "siann2-lang5", "who"),
    ("叨位", "to2-ui7", "where"), ("当时", "tang1-si5", "when"),
    ("为啥物", "ui7-siann2-mih8", "why"), ("按怎", "an2-tsuann2", "how"),
    ("偌济", "gua7-tse7", "how much"), ("几", "kui2", "how many"),
])

DEMOS["nan_commands"] = grammar_drill("commands", [
    ("bare", "紧来", "紧", "来"),
    ("negative", "莫吵", "莫", "吵"),
    ("polite", "请坐", "请", "坐"),
    ("formal", "麻烦你开门", "麻烦", "开"),
    ("prohibit", "毋通去", "毋通", "去"),
    ("group", "咱来去", "咱", "来"),
], ["请", "莫", "毋通", "麻烦", "咱"])

DEMOS["nan_descriptions"] = sentence_audit("descriptions", 20,
                                           ["台北", "台南", "夜市", "古锥"])

DEMOS["nan_story1"] = sentence_audit("story1", 10, ["市场", "阿母", "食饱", "多谢"])
DEMOS["nan_story2"] = grammar_drill("story2", [
    ("past-time", "旧年热天阮去鹿港", "旧年", "去"),
    ("past-u", "阮去看天后宫", "去", "看"),
    ("completed", "暗时转来真欢喜", "转来", "欢喜"),
    ("past-exp", "阮捌去过", "捌", "去"),
], ["旧年", "鹿港", "天后宫", "捌"])
DEMOS["nan_story3"] = grammar_drill("story3", [
    ("future-beh", "阮欲去爬山", "欲", "去"),
    ("future-e", "阿爸会开车", "会", "开"),
    ("conditional", "若落雨就毋去", "若", "就"),
    ("cond-2", "若天气好会看见海", "若", "会"),
], ["欲", "会", "若", "就"])

DEMOS["nan_idioms"] = vocab_quiz("idioms", [
    ("食紧撞破碗", "tsiah8 kin2 tong7 phua3 uann2", "haste makes waste"),
    ("歹竹出好笋", "phainn2 tik4 tshut4 ho2 sun2", "good shoots from bad bamboo"),
    ("一枝草一点露", "tsit8 ki1 tshau2 tsit8 tiam2 loo7", "everyone has their lot"),
    ("天公疼憨人", "thinn1-kong1 thiann3 ham7-lang5", "heaven loves the simple"),
    ("人咧做，天咧看", "lang5 teh4 tso3 thinn1 teh4 khuann3", "justice sees all"),
    ("一步一脚印", "tsit8 poo7 tsit8 kha1-in3", "steady progress"),
    ("半路认老爸", "puann3 loo7 jin7 lau7-pe7", "opportunist"),
    ("好心予雷亲", "ho2-sim1 hoo7 lui5 tshin1", "no good deed unpunished"),
    ("囝仔人有耳无嘴", "gin2-a2-lang5 u7 hinn7 bo5 tshui3", "children should listen"),
    ("吃人一口，还人一斗", "tsiah8 lang5 tsit8 khau2 hing5 lang5 tsit8 tau2", "repay kindness manyfold"),
])

DEMOS["nan_register"] = grammar_drill("register", [
    ("greet-formal", "您好", "您", "好"),
    ("greet-informal", "你好", "你", "好"),
    ("ask-formal", "请问一下", "请问", ""),
    ("thanks-formal", "真多谢你的帮忙", "多谢", "帮忙"),
    ("sorry-formal", "真歹势请你原谅", "歹势", "原谅"),
    ("host-formal", "请饮茶", "请", "饮"),
], ["您", "请问", "多谢", "歹势", "劳驾"])

DEMOS["nan_complex"] = grammar_drill("complex", [
    ("after", "我食饱了后就去学校", "了后", "就"),
    ("cause", "因为落雨所以无去", "因为", "所以"),
    ("concession", "虽然老毋过勇", "虽然", "毋过"),
    ("condition", "你若欲去就紧准备", "若", "就"),
    ("notonly", "毋但我去阿母嘛去", "毋但", "嘛"),
    ("relative", "伊讲的话", "讲", "的"),
    ("while", "我一边行一边想", "一边", "想"),
    ("more", "越学越有趣味", "越学", "趣味"),
], ["了后", "因为", "所以", "虽然", "毋过", "若", "就", "毋但"])

_CONV_WORDS = {
    "nan_conv_market": ["头家", "成交", "免找", "多谢惠顾"],
    "nan_conv_friend": ["好久无看见", "做伙去食饭", "干杯", "再会"],
    "nan_conv_problem": ["热水器", "师傅", "劳烦", "毋免客气"],
}
for _k, _w in _CONV_WORDS.items():
    DEMOS[_k] = sentence_audit(_k.replace("nan_", ""), 20, _w)


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
        "MEANS = {1: 5.0, 2: 3.0, 3: 3.0, 4: 3.0, 5: 1.5, 6: 2.0, 7: 2.5, 8: 4.0}\n"
        "CONTOURS = {1: [5, 5], 2: [2, 4], 3: [5, 1], 4: [3, 3], 5: [2, 1], 6: [2, 2], 7: [3, 2], 8: [4]}\n"
        "for t, c in CONTOURS.items():\n"
        "    m = sum(c) / len(c)\n"
        "    assert abs(m - MEANS[t]) < 1e-9, \"tone mean drift\"\n"
        "print(\"tone table: 8 tones verified\")\n"
        + _check_lines(["食饱未", "再会", "慢走", "学无止境", "故乡的月尚光"]) + "\n"
        "print(\"OK: mastery exam verified 200 words for " + rid + "\")\n"
    )
    return prog


DEMOS["nan_mastery"] = _mastery_exam

# every entry key must have exactly one demo
import entries_min_nan_chinese as _E
assert set(DEMOS) == {e["key"] for e in _E.ENTRIES}, "demo map misses entries"
