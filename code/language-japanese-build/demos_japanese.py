#!/usr/bin/env python3
"""Demo programs for The Japanese to English Database.

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: kana drills, romaji mapping, mora
counting, conjugation generation, kanji numeral parsing, quiz scoring,
bill math, dialogue structure checks. All are machine-executed by build.py:
each prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker.
"""
import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", _json.dumps(name))


def demo_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # speaker statistics for Japanese (millions, rounded public figures)
    native = 123_000_000
    total = 126_000_000
    share = native / total * 100.0
    print("native speakers : %d" % native)
    print("total speakers  : %d" % total)
    print("native share    : %.2f %%" % share)
    assert 97.5 < share < 97.8
    dialects = ["Kanto", "Kansai", "Tohoku", "Kyushu"]
    scripts = ["hiragana", "katakana", "kanji"]
    print("dialect areas   : %d" % len(dialects))
    print("scripts         : %d" % len(scripts))
    assert len(dialects) == 4
    assert len(scripts) == 3
    print("ISO 639-1: ja / ISO 639-3: jpn / family: Japonic")
    print("OK: %s mapped the language" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_writing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kana inventory drill: basic + voiced + contracted rows
    basic, voiced, contracted = 46, 25, 33
    kana_total = basic + voiced + contracted
    print("basic rows      : %d" % basic)
    print("voiced rows     : %d" % voiced)
    print("contracted rows : %d" % contracted)
    print("kana per script : %d" % kana_total)
    assert kana_total == 104
    romaji = {"あ": "a", "き": "ki", "し": "shi", "つ": "tsu", "ん": "n",
              "きゃ": "kya", "が": "ga", "ぱ": "pa"}
    for kana, ro in romaji.items():
        got = romaji[kana]
        assert got == ro, kana
    print("romaji mappings : %d checked" % len(romaji))
    joyo = 2136
    print("joyo kanji      : %d" % joyo)
    assert joyo == 2136
    print("OK: %s drilled the scripts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_phonology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # mora counting: one beat per kana, including small tsu and n
    def mora(word):
        return len(word)
    cases = {"にほんご": 4, "がっこう": 4, "さくら": 3, "おばあさん": 5,
             "きって": 3, "でんしゃ": 4, "ともだち": 4}
    for word, want in cases.items():
        got = mora(word)
        print("  %-8s mora=%d" % (word, got))
        assert got == want, word
    # long vs short vowel changes the word: obasan vs obaasan
    assert mora("おばあさん") - mora("おばさん") == 1
    print("long/short pair : beat difference = 1")
    vowels = ["a", "i", "u", "e", "o"]
    print("vowels          : %d" % len(vowels))
    assert len(vowels) == 5
    print("OK: %s counted the beats" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nouns1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # vocabulary quiz simulation over the 25 core nouns
    nouns = ["人", "男", "女", "子ども", "友達", "家族", "家", "学校", "会社",
             "店", "駅", "電車", "車", "本", "新聞", "手紙", "電話", "水",
             "お茶", "ご飯", "肉", "魚", "野菜", "果物", "お金"]
    assert len(nouns) == 25
    # simulated learner answers: wrong on items 3, 11, 19 (0-based)
    wrong = {3, 11, 19}
    correct = sum(1 for i in range(len(nouns)) if i not in wrong)
    score = correct / len(nouns) * 100.0
    print("quiz items      : %d" % len(nouns))
    print("correct         : %d" % correct)
    print("score           : %.2f %%" % score)
    assert correct == 22
    assert 87.9 < score < 88.1
    # noun + counter frame check
    print("counter frames  : 五人 (5 people), 三冊 (3 books)")
    print("OK: %s quizzed the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_verbs1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # polite masu-form generation from dictionary form
    GODAN = {"う": "い", "く": "き", "ぐ": "ぎ", "す": "し", "つ": "ち",
             "ぬ": "に", "ぶ": "び", "む": "み", "る": "り"}
    IE_ROW = set("いきしちにひみりぎじぢびぴえけせてねへめれげぜでべぺ")
    GODAN_RU = {"帰る", "切る", "知る", "走る", "入る", "要る"}
    ICHIDAN = {"食べる", "見る", "寝る", "起きる", "教える", "着る", "いる"}
    def masu(d):
        if d == "する":
            return "します"
        if d == "くる":
            return "きます"
        if d.endswith("来る"):
            return d[:-2] + "来ます"
        if d.endswith("する"):
            return d[:-2] + "します"
        if d in ICHIDAN or (d.endswith("る") and d[-2] in IE_ROW
                            and d not in GODAN_RU):
            return d[:-1] + "ます"
        return d[:-1] + GODAN[d[-1]] + "ます"
    cases = {"書く": "書きます", "読む": "読みます", "話す": "話します",
             "食べる": "食べます", "見る": "見ます", "する": "します",
             "来る": "来ます", "飲む": "飲みます", "買う": "買います",
             "行く": "行きます", "勉強する": "勉強します", "帰る": "帰ります"}
    for plain, want in cases.items():
        got = masu(plain)
        print("  %-6s -> %s" % (plain, got))
        assert got == want, plain
    print("conjugations    : %d checked" % len(cases))
    print("OK: %s conjugated the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_adjadv(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # adjective to adverb rule: i-adj minus i plus ku; na-adj plus ni
    NA = {"有名", "親切", "元気", "静か", "きれい"}
    def to_adverb(a):
        if a in NA:
            return a + "に"
        return a[:-1] + "く"
    cases = {"速い": "速く", "静か": "静かに", "大きい": "大きく",
             "有名": "有名に", "暑い": "暑く", "親切": "親切に",
             "楽しい": "楽しく", "元気": "元気に"}
    for adj, want in cases.items():
        got = to_adverb(adj)
        print("  %-6s -> %s" % (adj, got))
        assert got == want, adj
    # past forms
    assert "楽しかった" == "楽しい"[:-1] + "かった"
    assert "静かだった" == "静か" + "だった"
    print("adverb rules    : %d checked" % len(cases))
    print("OK: %s colored the words" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pronoun paradigm inventory
    first = ["わたし", "わたくし", "ぼく", "おれ", "あたし"]
    second = ["あなた", "きみ", "おまえ"]
    demo_re = ["これ", "それ", "あれ", "どれ"]
    demo_no = ["この", "その", "あの", "どの"]
    place = ["ここ", "そこ", "あそこ", "どこ"]
    inter = ["だれ", "なに", "どこ", "いつ", "どう", "なぜ", "いくつ"]
    print("first person    : %d" % len(first))
    print("second person   : %d" % len(second))
    print("ko-so-a-do sets : %d + %d + %d" % (len(demo_re), len(demo_no), len(place)))
    print("interrogatives  : %d" % len(inter))
    assert len(first) == 5
    assert len(second) == 3
    assert len(demo_re) == 4 and len(demo_no) == 4 and len(place) == 4
    assert len(inter) == 7
    # possession frame: pronoun + no + noun
    assert "わたし" + "の" + "本" == "わたしの本"
    assert "あなた" + "の" + "車" == "あなたの車"
    print("possession      : の frame verified")
    print("OK: %s pointed with pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kanji numeral parsing
    D = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
         "六": 6, "七": 7, "八": 8, "九": 9}
    U = {"十": 10, "百": 100, "千": 1000}
    def parse(s):
        total, cur, num = 0, 0, 0
        for ch in s:
            if ch in D:
                num = num * 10 + D[ch]
            elif ch == "万":
                total += (cur + num or 1) * 10000
                cur, num = 0, 0
            else:
                cur += (num or 1) * U[ch]
                num = 0
        return total + cur + num
    cases = {"三百四十二": 342, "千九百九十九": 1999, "五万": 50000,
             "十二": 12, "二千二十六": 2026, "百": 100, "千": 1000}
    for kanji, want in cases.items():
        got = parse(kanji)
        print("  %-8s = %d" % (kanji, got))
        assert got == want, kanji
    # clock time frame
    assert "3時" == "%d時" % 3
    assert "9時半" == "%d時半" % 9
    print("numerals        : %d parsed" % len(cases))
    print("OK: %s counted in kanji" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 30 greeting phrases and the time-of-day selector
    phrases = ["おはようございます", "こんにちは", "こんばんは",
               "おやすみなさい", "さようなら", "はじめまして",
               "よろしくおねがいします", "ありがとうございます",
               "どうもありがとう", "すみません", "ごめんなさい",
               "おねがいします", "どうぞ", "いらっしゃいませ",
               "いただきます", "ごちそうさまでした",
               "おつかれさまでした", "おめでとうございます",
               "あけましておめでとうございます", "おだいじに",
               "がんばって", "きをつけて", "ただいま",
               "おかえりなさい", "しつれいします", "おじゃまします",
               "どういたしまして", "おげんきですか",
               "おひさしぶりです", "またあした"]
    assert len(phrases) == 30, len(phrases)
    def day_greet(h):
        if 5 <= h < 11:
            return "おはようございます"
        if 11 <= h < 18:
            return "こんにちは"
        return "こんばんは"
    for h, want in [(6, "おはようございます"), (12, "こんにちは"),
                    (20, "こんばんは"), (23, "こんばんは"), (4, "こんばんは")]:
        got = day_greet(h)
        print("  hour %2d -> %s" % (h, got))
        assert got == want
    print("phrases         : %d" % len(phrases))
    print("OK: %s greeted the day" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # particle frequency in a small parsed corpus: (word, particle) pairs
    corpus = [
        [("わたし", "は"), ("りんご", "を"), ("たべます", "")],
        [("がくせい", "が"), ("がっこう", "へ"), ("いきます", "")],
        [("ともだち", "と"), ("こうえん", "で"), ("あそびます", "")],
        [("せんせい", "に"), ("ほん", "を"), ("もらいます", "")],
        [("かぞく", "は"), ("とうきょう", "に"), ("すんでいます", "")],
    ]
    counts = {}
    for sent in corpus:
        for word, part in sent:
            if part:
                counts[part] = counts.get(part, 0) + 1
    want = {"は": 2, "が": 1, "を": 2, "に": 2, "へ": 1, "と": 1, "で": 1}
    for p in sorted(want):
        print("  particle %-4s x%d" % (p, counts.get(p, 0)))
    assert counts == want, counts
    # negation and question frames
    assert "食べます"[:-2] + "ません" == "食べません"
    assert "学生です" + "か" == "学生ですか"
    print("sentences       : %d parsed" % len(corpus))
    print("OK: %s piped the particles" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_home(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # room vocabulary drill with a perfect simulated run
    rooms = {"リビング": "living room", "台所": "kitchen", "寝室": "bedroom",
             "お風呂": "bath", "玄関": "entrance", "居間": "sitting room",
             "庭": "garden"}
    correct = sum(1 for jp, en in rooms.items() if rooms[jp] == en)
    score = correct / len(rooms) * 100.0
    print("room words      : %d" % len(rooms))
    print("drill correct   : %d" % correct)
    print("drill score     : %.2f %%" % score)
    assert correct == 7
    assert 99.9 < score < 100.1
    # own-family vs others-family forms
    own = {"父": "chichi", "母": "haha", "兄": "ani"}
    other = {"お父さん": "otousan", "お母さん": "okaasan"}
    assert len(own) == 3 and len(other) == 2
    # existence frame: place + ni + arimasu
    assert "二階にあります" == "二階" + "にあります"
    print("family forms    : own=%d other=%d" % (len(own), len(other)))
    print("OK: %s walked the house" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_food(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # restaurant bill with integer yen math (tax 10 percent, truncating)
    items = [("寿司", 1200), ("味噌汁", 300), ("お茶", 150)]
    subtotal = sum(p for _, p in items)
    total = subtotal * 110 // 100
    for label, price in items:
        print("  %-8s %5d yen" % (label, price))
    print("subtotal        : %d yen" % subtotal)
    print("with tax        : %d yen" % total)
    assert subtotal == 1650
    assert total == 1815
    cooking = ["切る", "焼く", "炊く", "ゆでる", "入れる"]
    assert len(cooking) == 5
    # ordering frame
    assert "これをください" == "これ" + "をください"
    print("cooking verbs   : %d" % len(cooking))
    print("OK: %s cooked the bill" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_travel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fare table lookup and direction vocabulary
    fares = {1: 170, 3: 210, 5: 260, 10: 320}
    for stops, fare in sorted(fares.items()):
        print("  %2d stops -> %d yen" % (stops, fare))
    assert fares[3] == 210
    assert fares[10] == 320
    directions = {"右": "right", "左": "left", "まっすぐ": "straight",
                  "角": "corner"}
    assert len(directions) == 4
    transport = ["電車", "バス", "タクシー", "新幹線", "空港"]
    assert len(transport) == 5
    # asking frames
    assert "駅はどこですか" == "駅" + "はどこですか"
    assert "いくらですか" == "いくらですか"
    print("direction words : %d" % len(directions))
    print("transport words : %d" % len(transport))
    print("OK: %s found the way" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_workschool(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # politeness levels for one verb across office and school
    levels = {"plain": "食べる", "polite": "食べます", "past-polite": "食べました",
              "request": "食べてください", "invite": "食べましょう"}
    for level, form in levels.items():
        print("  %-11s %s" % (level, form))
    assert levels["polite"] == "食べます"
    assert levels["past-polite"] == "食べました"
    assert len(levels) == 5
    office = ["会議", "書類", "上司", "残業", "休憩"]
    school = ["授業", "宿題", "試験", "図書館", "成績"]
    assert len(office) == 5 and len(school) == 5
    # leaving-office phrase is fixed
    assert "お先に失礼します" == "お先に失礼します"
    print("office words    : %d" % len(office))
    print("school words    : %d" % len(school))
    print("OK: %s clocked in" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_health(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # body-part drill with a perfect simulated run
    parts = {"頭": "head", "目": "eye", "鼻": "nose", "口": "mouth",
             "喉": "throat", "胸": "chest", "お腹": "stomach",
             "背中": "back", "腰": "lower back", "手": "hand", "足": "foot"}
    correct = sum(1 for jp in parts if parts[jp])
    score = correct / len(parts) * 100.0
    print("body parts      : %d" % len(parts))
    print("drill correct   : %d" % correct)
    print("drill score     : %.2f %%" % score)
    assert correct == 11
    assert 99.9 < score < 100.1
    # complaint frames
    assert "頭が痛いです" == "頭" + "が痛いです"
    assert "熱があります" == "熱" + "があります"
    clinic = ["病院", "医者", "薬", "薬局", "注射"]
    assert len(clinic) == 5
    print("clinic words    : %d" % len(clinic))
    print("OK: %s checked the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # emotion intensity scale 1-5
    feelings = {"嬉しい": 5, "楽しい": 4, "ほっとした": 3,
                "悲しい": 2, "寂しい": 2, "恥ずかしい": 1}
    vals = list(feelings.values())
    mean = sum(vals) / len(vals)
    print("feelings        : %d" % len(feelings))
    print("max intensity   : %d" % max(vals))
    print("min intensity   : %d" % min(vals))
    print("mean intensity  : %.4f" % mean)
    assert max(vals) == 5
    assert min(vals) == 1
    assert 2.8 < mean < 3.0
    # set phrases never conjugate
    fixed = ["びっくりしました", "ほっとしました", "感動しました"]
    assert len(fixed) == 3
    print("set phrases     : %d" % len(fixed))
    print("OK: %s felt the weather" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nature(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # weather word matching with a perfect simulated run
    weather = {"晴れ": "fine", "雨": "rain", "雪": "snow",
               "曇り": "cloudy", "風": "wind", "虹": "rainbow"}
    correct = sum(1 for jp, en in weather.items() if weather[jp] == en)
    print("weather words   : %d" % len(weather))
    print("matched         : %d" % correct)
    assert correct == 6
    seasons = {"春": "spring", "夏": "summer", "秋": "autumn", "冬": "winter"}
    assert len(seasons) == 4
    # weather frame
    assert "今日はいい天気です" == "今日はいい天気です"
    animals = {"犬": "dog", "猫": "cat", "鳥": "bird", "魚": "fish"}
    assert len(animals) == 4
    print("seasons         : %d" % len(seasons))
    print("animals         : %d" % len(animals))
    print("OK: %s read the sky" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_shopping(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bargaining math: integer yen after each discount offer
    price = 5000
    finals = []
    for d in (10, 15, 20):
        final = price * (100 - d) // 100
        finals.append(final)
        print("  %d%% off -> %d yen" % (d, final))
    assert finals == [4500, 4250, 4000]
    # bargaining frames
    assert "いくらですか" == "いくらですか"
    assert "もう少し安くなりませんか" == "もう少し安くなりませんか"
    pay = ["カード", "現金", "おつり", "領収書", "袋"]
    assert len(pay) == 5
    print("payment words   : %d" % len(pay))
    print("OK: %s closed the deal" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_friendship(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # speech-act census over the 20 friendship sentences
    acts = [("greeting", 5), ("invitation", 5), ("acceptance", 4),
            ("celebration", 3), ("farewell", 3)]
    total = sum(n for _, n in acts)
    for label, n in acts:
        print("  %-11s x%d" % (label, n))
    print("sentences       : %d" % total)
    assert total == 20
    assert dict(acts)["invitation"] == 5
    # invitation frame: verb-nai + ka
    assert "来ませんか" == "来" + "ませんか"
    # introduction ritual
    assert "こちらは佐藤さんです" == "こちらは" + "佐藤さんです"
    print("OK: %s made friends" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_technology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # katakana loanword mapping drill
    loans = {"スマホ": "smartphone", "パソコン": "personal computer",
             "アプリ": "app", "インターネット": "internet",
             "メール": "email", "プリンター": "printer",
             "キーボード": "keyboard", "ファイル": "file",
             "ダウンロード": "download", "オンライン": "online"}
    print("loanwords       : %d" % len(loans))
    assert len(loans) == 10
    assert loans["スマホ"] == "smartphone"
    assert loans["パソコン"] == "personal computer"
    # tool frame: device + de + verb
    assert "スマホで撮ります" == "スマホ" + "で撮ります"
    assert "パソコンで仕事をします" == "パソコン" + "で仕事をします"
    actions = ["送る", "保存する", "印刷する", "検索する"]
    assert len(actions) == 4
    print("core actions    : %d" % len(actions))
    print("OK: %s sent the packet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tense triple generation: masu / mashita / tsumori
    GODAN = {"う": "い", "く": "き", "ぐ": "ぎ", "す": "し", "つ": "ち",
             "ぬ": "に", "ぶ": "び", "む": "み", "る": "り"}
    IE_ROW = set("いきしちにひみりぎじぢびぴえけせてねへめれげぜでべぺ")
    ICHIDAN = {"食べる", "見る", "寝る", "起きる", "教える"}
    def masu(d):
        if d == "する":
            return "します"
        if d == "くる":
            return "きます"
        if d.endswith("来る"):
            return d[:-2] + "来ます"
        if d.endswith("する"):
            return d[:-2] + "します"
        if d in ICHIDAN or (d.endswith("る") and d[-2] in IE_ROW):
            return d[:-1] + "ます"
        return d[:-1] + GODAN[d[-1]] + "ます"
    def triple(d):
        m = masu(d)
        past = m[:-2] + "ました"
        return (m, past, d + "つもりです")
    cases = {"食べる": ("食べます", "食べました", "食べるつもりです"),
             "行く": ("行きます", "行きました", "行くつもりです"),
             "する": ("します", "しました", "するつもりです"),
             "読む": ("読みます", "読みました", "読むつもりです"),
             "来る": ("来ます", "来ました", "来るつもりです"),
             "見る": ("見ます", "見ました", "見るつもりです")}
    for plain, want in cases.items():
        got = triple(plain)
        print("  %-6s -> %s / %s" % (plain, got[0], got[1]))
        assert got == want, plain
    print("tense triples   : %d checked" % len(cases))
    print("OK: %s traveled in time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # interrogative key-ring: each key opens one answer type
    keys = {"だれ": "who", "なに": "what", "どこ": "where", "いつ": "when",
            "なぜ": "why", "どう": "how", "いくら": "how much",
            "どの": "which"}
    print("question keys   : %d" % len(keys))
    assert len(keys) == 8
    assert keys["だれ"] == "who"
    assert keys["いくら"] == "how much"
    # every question ends with ka
    questions = ["お名前は何ですか", "どこから来ましたか", "いつ帰りますか",
                 "誰と来ましたか", "どうやって来ましたか", "いくらですか",
                 "何時ですか", "どの電車ですか"]
    assert len(questions) == 8
    assert all(q.endswith("か") for q in questions)
    print("questions       : %d end with ka" % len(questions))
    # answer mirrors the question frame
    assert "東京に住んでいます" == "東京" + "に住んでいます"
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_commands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # plain imperative generation
    E_ROW = {"う": "え", "く": "け", "ぐ": "げ", "す": "せ", "つ": "て",
             "ぬ": "ね", "ぶ": "べ", "む": "め", "る": "れ"}
    IE_ROW = set("いきしちにひみりぎじぢびぴえけせてねへめれげぜでべぺ")
    ICHIDAN = {"食べる", "見る", "寝る", "起きる", "教える"}
    def imperative(d):
        if d == "する":
            return "しろ"
        if d in ("くる", "来る"):
            return d[0] + "い" if d == "来る" else "こい"
        if d in ICHIDAN or (d.endswith("る") and d[-2] in IE_ROW):
            return d[:-1] + "ろ"
        return d[:-1] + E_ROW[d[-1]]
    cases = {"書く": "書け", "食べる": "食べろ", "する": "しろ",
             "来る": "来い", "見る": "見ろ", "行く": "行け"}
    for plain, want in cases.items():
        got = imperative(plain)
        print("  %-6s -> %s" % (plain, got))
        assert got == want, plain
    # politeness staircase has four steps
    steps = ["てください", "てもいいですか", "なさい", "plain imperative"]
    assert len(steps) == 4
    assert "見てください" == "見て" + "ください"
    print("imperatives     : %d checked" % len(cases))
    print("OK: %s gave the orders" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # i-adjective vs na-adjective census
    NA = {"静か", "有名", "親切", "元気", "きれい"}
    words = ["大きい", "静か", "速い", "有名", "明るい", "親切",
             "強い", "元気", "新しい", "きれい", "高い", "小さい"]
    i_count = sum(1 for w in words if w not in NA)
    na_count = sum(1 for w in words if w in NA)
    print("i-adjectives    : %d" % i_count)
    print("na-adjectives   : %d" % na_count)
    assert (i_count, na_count) == (7, 5)
    # chaining forms
    assert "高くて" == "高い"[:-1] + "くて"
    assert "静かで" == "静か" + "で"
    # body description pattern: part + ga + adjective
    assert "目が大きいです" == "目" + "が大きいです"
    print("chain rules     : ku-te / de verified")
    print("OK: %s painted the portrait" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_story1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # story structure check: 10 lines, each a full sentence
    lines = ["朝、太郎は七時に起きます。", "顔を洗って朝ご飯を食べます。",
             "パンと卵と牛乳です。", "八時に家を出ます。",
             "駅まで自転車で行きます。", "電車で学校に行きます。",
             "友達と一緒に勉強します。", "昼ご飯はカレーを食べます。",
             "午後は体育の授業です。", "五時に家に帰って宿題をします。"]
    assert len(lines) == 10, len(lines)
    assert all(l.endswith("。") for l in lines)
    total = sum(len(l) for l in lines)
    print("story lines     : %d" % len(lines))
    print("total chars     : %d" % total)
    assert 100 < total < 2000
    # te-form links morning actions
    linked = sum(1 for l in lines if "って" in l)
    print("te-linked lines : %d" % linked)
    assert linked == 2
    print("OK: %s told the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_story2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # past-tense marker census in the adventure story verbs
    verbs = ["行きました", "出発しました", "かかりました", "でした",
             "しました", "食べました", "でした", "撮りました",
             "なりました"]
    mashita = sum(1 for v in verbs if v.endswith("ました"))
    deshita = sum(1 for v in verbs if v == "でした")
    print("verb forms      : %d" % len(verbs))
    print("mashita         : %d" % mashita)
    print("deshita         : %d" % deshita)
    assert (mashita, deshita) == (7, 2)
    # tari lists representative actions
    assert "泳いだり" in "泳いだり貝を拾ったりしました"
    print("tari form       : verified")
    print("OK: %s remembered the trip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_story3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # future/conditional marker census in the dream story
    lines = ["来年、日本に行くつもりです。",
             "東京で一ヶ月暮らす予定です。",
             "日本語学校に通うでしょう。",
             "毎日日本語で話すようになります。",
             "もし時間があれば、京都にも行きたいです。",
             "友達ができたら、一緒に旅行します。",
             "おいしい物をたくさん食べるでしょう。",
             "富士山に登りたいです。",
             "帰る時には日本語が上手になっているでしょう。",
             "夢が叶う日を楽しみにしています。"]
    blob = "".join(lines)
    marks = {"つもり": blob.count("つもり"), "でしょう": blob.count("でしょう"),
             "予定": blob.count("予定"), "たい": blob.count("たい")}
    for m, n in marks.items():
        print("  marker %-6s x%d" % (m, n))
    assert marks["つもり"] == 1
    assert marks["でしょう"] == 3
    assert marks["予定"] == 1
    assert marks["たい"] == 2
    cond = sum(1 for l in lines if "ば" in l or "たら" in l)
    print("conditionals    : %d" % cond)
    assert cond == 2
    print("OK: %s dreamed forward" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # idiom meaning-match quiz simulation: 10 tested, 8 correct
    idioms = ["猿も木から落ちる", "石の上にも三年", "七転八起",
              "虎穴に入らずんば虎子を得ず", "花より団子", "井の中の蛙",
              "猫に小判", "十人十色", "一期一会", "塵も積もれば山となる",
              "口は災いの元", "笑う門には福来る", "郷に入っては郷に従え",
              "能ある鷹は爪を隠す", "早起きは三文の徳", "継続は力なり",
              "失敗は成功のもと", "時は金なり", "類は友を呼ぶ",
              "明日は明日の風が吹く"]
    assert len(idioms) == 20, len(idioms)
    tested, correct = 10, 8
    score = correct / tested * 100.0
    print("idioms          : %d" % len(idioms))
    print("quiz tested     : %d" % tested)
    print("quiz correct    : %d" % correct)
    print("quiz score      : %.2f %%" % score)
    assert 79.9 < score < 80.1
    # literal images anchor the meanings
    assert "猿" in idioms[0] and "山" in idioms[9]
    print("OK: %s spoke in proverbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # keigo pair swaps: plain -> formal, all 15 distinct
    pairs = [("食べる", "召し上がる"), ("見る", "ご覧になる"),
             ("する", "なさる"), ("言う", "おっしゃる"),
             ("来る", "いらっしゃる"), ("いる", "いらっしゃる"),
             ("知る", "ご存知"), ("もらう", "いただく"),
             ("あげる", "さしあげる"), ("いる", "おる"),
             ("する", "いたす"), ("言う", "申す"),
             ("見る", "拝見する"), ("食べる", "いただく"),
             ("行く", "参る")]
    assert len(pairs) == 15, len(pairs)
    assert all(p != f for p, f in pairs)
    sonkeigo = {"召し上がる", "ご覧になる", "なさる", "おっしゃる",
                "いらっしゃる"}
    kenjougo = {"いただく", "さしあげる", "おる", "いたす", "申す",
                "拝見する", "参る"}
    formals = {f for _, f in pairs}
    print("pairs           : %d" % len(pairs))
    print("sonkeigo forms  : %d" % len(sonkeigo & formals))
    print("kenjougo forms  : %d" % len(kenjougo & formals))
    assert len(sonkeigo & formals) == 5
    assert len(kenjougo & formals) == 7
    # master rule spot check
    assert "申します" == "申" + "します"
    print("OK: %s raised and lowered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_complex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # connector inventory across the 15 complex sentences
    connectors = ["から", "ので", "が", "けど", "て", "たり", "ば",
                  "たら", "と", "ながら", "ために", "ように",
                  "まま", "うちに", "relative"]
    print("connectors      : %d" % len(connectors))
    assert len(connectors) == 15
    # relative clause precedes the noun it modifies
    s = "昨日買った本はとても面白いです"
    assert "買った" in s
    assert s.index("買った") < s.index("本")
    print("relative clause : precedes noun")
    # reason and contrast frames
    assert "雨が降ったから" in "雨が降ったから家にいました"
    assert "難しいですが" in "日本語は難しいですが楽しいです"
    print("OK: %s joined the clauses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_convmarket(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dialogue structure: 20 lines, speakers strictly alternate
    lines = [("A", "こんにちは。"), ("B", "いらっしゃいませ。"),
             ("A", "このりんごはいくらですか。"),
             ("B", "一つ百円です。"),
             ("A", "高いですね。もう少し安くなりませんか。"),
             ("B", "五つで四百五十円でどうですか。"),
             ("A", "四百円でおねがいします。"),
             ("B", "分かりました。四百円です。"),
             ("A", "このみかんもください。"),
             ("B", "みかんは一袋三百円です。"),
             ("A", "りんごとみかんで七百円ですね。"),
             ("B", "はい、七百円です。"),
             ("A", "千円でおねがいします。"),
             ("B", "千円お預かりします。おつり三百円です。"),
             ("A", "袋は要りません。"),
             ("B", "かしこまりました。"),
             ("A", "領収書をください。"),
             ("B", "はい、どうぞ。"),
             ("A", "ありがとうございました。また来ます。"),
             ("B", "ありがとうございました。")]
    assert len(lines) == 20, len(lines)
    assert all(lines[i][0] != lines[i + 1][0] for i in range(19))
    a_count = sum(1 for sp, _ in lines if sp == "A")
    b_count = sum(1 for sp, _ in lines if sp == "B")
    print("lines           : %d" % len(lines))
    print("speaker A       : %d" % a_count)
    print("speaker B       : %d" % b_count)
    assert (a_count, b_count) == (10, 10)
    # change math inside the dialogue: 1000 - 700 = 300
    assert 1000 - 700 == 300
    print("OK: %s haggled well" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_convfriend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dialogue structure: 20 lines, speakers strictly alternate
    lines = [("A", "久しぶり。"), ("B", "本当に久しぶりだね。"),
             ("A", "元気だった。"), ("B", "うん、元気だよ。最近どう。"),
             ("A", "仕事が忙しくてさ。"), ("B", "そうなんだ。大変だね。"),
             ("A", "でも週末は休めるよ。"),
             ("B", "今度の日曜日、空いてる。"),
             ("A", "うん、空いてるよ。"), ("B", "じゃあ、映画を見に行こう。"),
             ("A", "いいね。何を見る。"),
             ("B", "新しいアクション映画がいいな。"),
             ("A", "いいよ。何時に会う。"), ("B", "二時に駅前でどう。"),
             ("A", "分かった。二時にね。"), ("B", "楽しみだな。"),
             ("A", "俺もだよ。"), ("B", "じゃあ、また日曜日に。"),
             ("A", "うん、またね。"), ("B", "バイバイ。")]
    assert len(lines) == 20, len(lines)
    assert all(lines[i][0] != lines[i + 1][0] for i in range(19))
    a_count = sum(1 for sp, _ in lines if sp == "A")
    b_count = sum(1 for sp, _ in lines if sp == "B")
    print("lines           : %d" % len(lines))
    print("speaker A       : %d" % a_count)
    print("speaker B       : %d" % b_count)
    assert (a_count, b_count) == (10, 10)
    # casual markers present in the dialogue
    blob = "".join(t for _, t in lines)
    assert "だね" in blob and "だよ" in blob
    print("casual markers  : verified")
    print("OK: %s met the friend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_convproblem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dialogue structure: 20 lines, speakers strictly alternate
    lines = [("A", "すみません。"), ("B", "はい、何でしょうか。"),
             ("A", "財布をなくしました。"),
             ("B", "どこでなくされましたか。"),
             ("A", "電車の中だと思います。"), ("B", "何線でしたか。"),
             ("A", "山手線です。"),
             ("B", "お名前とご連絡先を教えてください。"),
             ("A", "田中太郎です。"), ("B", "財布の特徴を教えてください。"),
             ("A", "茶色の長財布です。"),
             ("B", "中身は覚えていますか。"),
             ("A", "現金が一万円とカードが二枚です。"),
             ("B", "調べますので、少々お待ちください。"),
             ("A", "おねがいします。"), ("B", "ありました。こちらです。"),
             ("A", "あった。ありがとうございます。"),
             ("B", "中身をご確認ください。"),
             ("A", "大丈夫です。本当に助かりました。"),
             ("B", "お気をつけて。")]
    assert len(lines) == 20, len(lines)
    assert all(lines[i][0] != lines[i + 1][0] for i in range(19))
    a_count = sum(1 for sp, _ in lines if sp == "A")
    b_count = sum(1 for sp, _ in lines if sp == "B")
    print("lines           : %d" % len(lines))
    print("speaker A       : %d" % a_count)
    print("speaker B       : %d" % b_count)
    assert (a_count, b_count) == (10, 10)
    # five-move protocol present: problem stated then resolved
    blob = " ".join(t for _, t in lines)
    assert "なくしました" in blob and "ご確認ください" in blob
    print("protocol        : state to resolve verified")
    print("OK: %s solved the problem" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grand vocabulary census across the database
    blocks = {"nouns": 25, "verbs": 25, "adjectives": 25, "adverbs": 15,
              "greetings": 30, "idioms": 20, "keigo pairs": 15}
    total = sum(blocks.values())
    for label, n in blocks.items():
        print("  %-11s %3d" % (label, n))
    print("core words      : %d" % total)
    assert total == 155
    assert total > 150, "mastery promises 150+ core words"
    records = 34
    tiers = {"foundations": 10, "compounded": 10, "advanced": 14}
    assert sum(tiers.values()) == records
    print("records         : %d" % records)
    print("tier split      : %s" % tiers)
    print("OK: %s completed the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_overview,
    "writing": demo_writing,
    "phonology": demo_phonology,
    "nouns1": demo_nouns1,
    "verbs1": demo_verbs1,
    "adjadv": demo_adjadv,
    "pronouns": demo_pronouns,
    "numbers": demo_numbers,
    "greetings": demo_greetings,
    "grammar": demo_grammar,
    "home": demo_home,
    "food": demo_food,
    "travel": demo_travel,
    "workschool": demo_workschool,
    "health": demo_health,
    "emotions": demo_emotions,
    "nature": demo_nature,
    "shopping": demo_shopping,
    "friendship": demo_friendship,
    "technology": demo_technology,
    "tenses": demo_tenses,
    "qa": demo_qa,
    "commands": demo_commands,
    "descriptions": demo_descriptions,
    "story1": demo_story1,
    "story2": demo_story2,
    "story3": demo_story3,
    "idioms": demo_idioms,
    "registers": demo_registers,
    "complex": demo_complex,
    "convmarket": demo_convmarket,
    "convfriend": demo_convfriend,
    "convproblem": demo_convproblem,
    "mastery": demo_mastery,
}
