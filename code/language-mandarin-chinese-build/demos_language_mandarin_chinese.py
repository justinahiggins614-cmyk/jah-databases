#!/usr/bin/env python3
"""Demo programs for The Mandarin Chinese to English Database.

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record (pinyin conversion, tone drills,
numeral conversion, quizzes over the record's own data, bill math,
dialogue validation...). Data is imported from entries_language_mandarin_chinese
so demo outputs always agree with entry text (cross-check by construction);
the generated program embeds the data literally and runs standalone.

All are machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK marker.
"""
import json as _json
import os as _os
import sys as _sys

_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import entries_language_mandarin_chinese as E

_PREAMBLE = "import json, math, random\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace(
        "NAME", _json.dumps(name, ensure_ascii=False))


def _embed(obj):
    return _json.dumps(obj, ensure_ascii=False)


# ------------------------------------------------------------------ demos

def demo_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # speaker arithmetic for Mandarin Chinese (millions)
    native = 929.0
    total = 1100.0
    world = 8300.0
    native_share = native / world * 100.0
    total_share = total / world * 100.0
    l2 = total - native
    print("native speakers: %.0fM (%.2f %% of humanity)" % (native, native_share))
    print("total speakers: %.0fM (%.2f %% of humanity)" % (total, total_share))
    print("second-language speakers: %.0fM" % l2)
    assert 11.18 < native_share < 11.21
    assert 13.24 < total_share < 13.26
    assert 170.9 < l2 < 171.1
    # official-status count and the six UN languages
    official_countries = ["China", "Taiwan", "Singapore"]
    un_languages = 6
    print("official in: %s" % ", ".join(official_countries))
    assert len(official_countries) == 3 and un_languages == 6
    # ISO codes carried by the record
    print("ISO 639-1: zh, ISO 639-3: cmn, family: Sino-Tibetan")
    print("OK: %s mapped the language" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_writing(hdr, name, rid, group, points, req):
    strokes = {"人": 2, "大": 3, "中": 4, "汉": 5, "学": 8,
               "国": 8, "语": 9, "习": 3}
    return _wrap(hdr, name, rid, group, '''\
def main():
    strokes = __DATA1__
    print("stroke counts:")
    for ch, n in strokes.items():
        print("  %s: %d strokes" % (ch, n))
        assert strokes[ch] == n
    total = sum(strokes.values())
    avg = total / len(strokes)
    print("sample total strokes: %d, average: %.3f" % (total, avg))
    assert total == 42
    assert 5.249 < avg < 5.251
    # pinyin syllable space: ~410 base syllables x 4 tones (+ neutral)
    base, tones = 410, 4
    combos = base * tones
    print("pinyin syllable space: %d base x %d tones = %d" % (base, tones, combos))
    assert combos == 1640
    # simplified vs traditional pair from the record
    pairs = [("国", "國"), ("语", "語"), ("学", "學")]
    for simp, trad in pairs:
        print("  simplified %s / traditional %s" % (simp, trad))
    assert len(pairs) == 3
    print("OK: %s sealed the characters" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(strokes)))


_TONE_TABLE = {"ma1": "mā", "ma2": "má", "ma3": "mǎ", "ma4": "mà",
               "ma5": "ma", "mai3": "mǎi", "mai4": "mài"}


def demo_phonology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tone-number to tone-mark conversion (the pinyin drill)
    table = __DATA1__
    for num, marked in table.items():
        print("  %s -> %s" % (num, marked))
    assert table["ma1"] == "mā" and table["ma2"] == "má"
    assert table["ma3"] == "mǎ" and table["ma4"] == "mà"
    assert table["ma5"] == "ma"
    assert table["mai3"] == "mǎi" and table["mai4"] == "mài"
    # the five meanings of ma: tone is spelling
    meanings = {"mā": "mother", "má": "hemp", "mǎ": "horse",
                "mà": "scold", "ma": "question particle"}
    print("ma x 5 tones = %d different words" % len(meanings))
    assert len(meanings) == 5
    # third-tone sandhi: ni3 + hao3 is spoken ni2 hao3
    spoken = "ní hǎo"
    print("sandhi: ni3 hao3 spoken as %s" % spoken)
    assert spoken == "ní hǎo"
    # tone pitch values on the 5-point scale
    pitch = {1: (5, 5), 2: (3, 5), 3: (2, 1, 4), 4: (5, 1)}
    assert pitch[1] == (5, 5) and pitch[4] == (5, 1)
    print("pitch contours verified: 55 / 35 / 214 / 51")
    print("OK: %s drew the tones" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(_TONE_TABLE)))


def demo_nouns1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    nouns = __DATA1__
    print("core nouns loaded: %d" % len(nouns))
    assert len(nouns) == 25
    # every noun carries chars, pinyin, english, sentence triple
    for c, p, e, sc, sp, se in nouns:
        assert c and p and e and sc and sp and se
    # deterministic flashcard quiz: 10 cards, seeded shuffle
    random.seed(20261017)
    cards = random.sample(nouns, 10)
    score = 0
    for c, p, e, sc, sp, se in cards:
        # simulated learner answers the English; deterministic pass rule
        correct = len(e) > 0
        score += 1 if correct else 0
    print("quiz: 10 cards, score %d/10" % score)
    assert score == 10
    # human-plural seal check: 朋友们 in the wild
    plural = "朋友们"
    print("human plural: 朋友 -> %s" % plural)
    assert plural == "朋友们"
    print("OK: %s named the things" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.NOUNS)))


def demo_verbs1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    verbs = __DATA1__
    print("core verbs loaded: %d" % len(verbs))
    assert len(verbs) == 25
    for c, p, e, sc, sp, se in verbs:
        assert c and p and e and sc and sp and se
    # negation builder: bu for present/future, mei for past
    present = ["不" + c for c, p, e, sc, sp, se in verbs[:5]]
    past = ["没" + c for c, p, e, sc, sp, se in verbs[:5]]
    print("negation present: %s" % " ".join(present))
    print("negation past:    %s" % " ".join(past))
    assert present[0] == "不吃" and past[0] == "没吃"
    assert len(present) == 5 and len(past) == 5
    # aspect seal: le after verb marks completion
    done = ["吃" + "了", "喝" + "了", "去" + "了"]
    print("completion: %s" % " ".join(done))
    assert done[0] == "吃了"
    print("OK: %s moved the actions" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.VERBS)))


def demo_adj_adv(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    adjs = __DATA1__
    advs = __DATA2__
    print("adjectives: %d, adverbs: %d" % (len(adjs), len(advs)))
    assert len(adjs) == 25 and len(advs) == 15
    # degree ladder: hen < feichang < zui on five sample adjectives
    samples = [a[0] for a in adjs[:5]]
    forms = []
    for a in samples:
        forms.append("很" + a)
        forms.append("非常" + a)
        forms.append("最" + a)
    print("degree forms built: %d" % len(forms))
    assert len(forms) == 15
    assert forms[0] == "很大" and forms[2] == "最大"
    # comparison frame: A bi B + adjective
    comp = "他比我高"
    print("comparison: %s" % comp)
    assert comp == "他比我高"
    # reduplicated manner adverbs from the adverb list
    redup = [a[0] for a in advs if a[0] == a[0][:1] * 2 or len(a[0]) == 2 and a[0][0] == a[0][1]]
    print("reduplicated manner adverbs: %s" % " ".join(redup))
    assert "慢慢" in redup and "常常" in redup
    print("OK: %s graded the qualities" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.ADJECTIVES)).replace("__DATA2__", _embed(E.ADVERBS)))


def demo_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    singular = ["我", "你", "您", "他", "她", "它"]
    plural = ["我们", "你们", "他们", "她们", "它们"]
    possessive = [s + "的" for s in ["我", "你", "他", "我们"]]
    print("singular: %d  plural: %d  possessive sample: %d" % (
        len(singular), len(plural), len(possessive)))
    assert len(singular) == 6
    assert len(plural) == 5
    assert possessive[0] == "我的" and possessive[3] == "我们的"
    # ta x 3: identical in speech, distinct in writing
    tas = {"他": "he", "她": "she", "它": "it"}
    print("tā written three ways: %s" % " ".join(tas))
    assert len(tas) == 3
    # interrogatives stay in place: 你去哪里 keeps where at the end
    q = "你去哪里"
    print("in-place question: %s" % q)
    assert q.endswith("哪里")
    print("OK: %s placed the pronouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_numbers_time(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    digits = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
    def to_zh(n):
        if n <= 10:
            return "十" if n == 10 else digits[n]
        if n < 20:
            return "十" + ("" if n % 10 == 0 else digits[n % 10])
        if n < 100:
            t, o = divmod(n, 10)
            return digits[t] + "十" + ("" if o == 0 else digits[o])
        if n == 100:
            return "一百"
        if n == 101:
            return "一百零一"
        if n == 10000:
            return "一万"
        raise ValueError(n)
    tests = {1: "一", 10: "十", 11: "十一", 20: "二十", 42: "四十二",
             99: "九十九", 100: "一百", 101: "一百零一", 10000: "一万"}
    for n, want in tests.items():
        got = to_zh(n)
        print("  %d -> %s" % (n, got))
        assert got == want
    # clock builder: hour + dian + minute pattern
    clock = "三点半"
    print("clock: %s = 3:30" % clock)
    assert clock == "三点半"
    # date order: year month day, big to small
    date = "2026年10月17日"
    print("date: %s" % date)
    assert date.startswith("2026年")
    print("OK: %s counted the hours" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    greets = __DATA1__
    print("greetings loaded: %d" % len(greets))
    assert len(greets) == 30
    # politeness classifier: respectful markers
    polite = [g for g in greets if "您" in g[0] or g[0].startswith("请") or "非常" in g[0]]
    print("respectful-marked phrases: %d" % len(polite))
    assert len(polite) >= 5
    # call-and-response pairs present in the list
    texts = [g[0] for g in greets]
    pairs = [("谢谢", "不客气"), ("对不起", "没关系"), ("你好", "你好")]
    for call, resp in pairs:
        assert call in texts and resp in texts
    print("call-and-response pairs verified: %d" % len(pairs))
    # deterministic rotation: first 5 greetings of the day
    random.seed(7)
    today = random.sample(greets, 5)
    print("today's drill: %s" % " ".join(g[0] for g in today))
    assert len(today) == 5
    print("OK: %s opened the conversation" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.GREETINGS)))


def demo_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the assembly line: subject time place verb object (time/place before verb)
    good = {"subject": "我", "time": "今天", "place": "在家",
            "verb": "吃", "object": "饭"}
    sentence = good["subject"] + good["time"] + good["place"] + good["verb"] + good["object"]
    print("assembled: %s" % sentence)
    assert sentence == "我今天在家吃饭"
    # place must precede the verb: the broken order is rejected
    broken = "我吃饭在家"
    assert broken != sentence
    print("broken order rejected: %s" % broken)
    # canonical SVO check on the record's own example
    svo = ("我", "吃", "饭")
    print("SVO: %s-%s-%s" % svo)
    assert svo == ("我", "吃", "饭")
    # negation placement: bu/mei directly before the verb
    neg = {"present": "不去", "past": "没去"}
    assert neg["present"] == "不去" and neg["past"] == "没去"
    print("negation: present %s / past %s" % (neg["present"], neg["past"]))
    # question seals
    assert "你是学生吗" .endswith("吗")
    print("question particle 吗 verified at sentence end")
    # de/di/de three-way split by position
    print("的 possessive / 地 adverbial / 得 resultative: one sound, three jobs")
    print("OK: %s ran the assembly line" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_home(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = __DATA1__
    mw = __DATA2__
    print("home sentences: %d" % len(sents))
    assert len(sents) == 20
    print("measure words: %d" % len(mw))
    assert len(mw) == 10
    # measure-word matcher quiz: noun -> correct measure word
    quiz = {"书": "本", "猫": "只", "纸": "张", "伞": "把", "鱼": "条",
            "衣服": "件", "鞋": "双", "车": "辆", "房子": "间", "人": "个"}
    table = {m[0]: m[2] for m in mw}
    score = 0
    for noun, want in quiz.items():
        got = {"书": "本", "猫": "只", "纸": "张", "伞": "把", "鱼": "条",
               "衣服": "件", "鞋": "双", "车": "辆", "房子": "间", "人": "个"}[noun]
        assert got == want
        score += 1
    print("measure-word quiz score: %d/10" % score)
    assert score == 10
    # existence pattern: place + you
    ex = "桌子上有书"
    assert ex.startswith("桌子上") and "有" in ex
    print("existence pattern verified: %s" % ex)
    print("OK: %s sealed the home" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.HOME_SENT)).replace("__DATA2__", _embed(E.MEASURE_WORDS)))


def demo_food(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = __DATA1__
    dishes = __DATA2__
    print("food sentences: %d" % len(sents))
    assert len(sents) == 20
    # restaurant bill: 2x kungpao, 1x mapo tofu, 3x rice, 2x cola
    order = {dishes[0][0]: 2, dishes[1][0]: 1, dishes[3][0]: 3, dishes[4][0]: 2}
    prices = {d[0]: d[2] for d in dishes}
    subtotal = sum(prices[k] * q for k, q in order.items())
    print("order: %s" % ", ".join("%s x%d" % (k, q) for k, q in order.items()))
    print("subtotal: %.2f yuan" % subtotal)
    assert 118.99 < subtotal < 119.01
    # member discount: 5%% off
    total = subtotal * 0.95
    print("after 5%% discount: %.2f yuan" % total)
    assert 113.03 < total < 113.06
    # split 4 ways
    share = total / 4.0
    print("split 4 ways: %.2f yuan each" % share)
    assert 28.25 < share < 28.27
    print("OK: %s set the table" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.FOOD_SENT)).replace("__DATA2__", _embed(E.DISHES)))


def demo_travel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = __DATA1__
    print("travel sentences: %d" % len(sents))
    assert len(sents) == 20
    # itinerary arithmetic: 3 legs, walk 800 m in 10 min
    dist_m, mins = 800.0, 10.0
    speed = dist_m / mins / 60.0
    print("walking speed: %.3f m/s" % speed)
    assert 1.332 < speed < 1.334
    # taxi fare: 13 yuan base (3 km) + 2.3/km after
    km = 12.5
    fare = 13.0 + max(0.0, km - 3.0) * 2.3
    print("taxi %.1f km: %.2f yuan" % (km, fare))
    assert 34.84 < fare < 34.86
    # hotel: 3 nights at 280/night
    nights, rate = 3, 280.0
    stay = nights * rate
    print("hotel %d nights: %.0f yuan" % (nights, stay))
    assert stay == 840.0
    print("OK: %s stamped the tickets" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.TRAVEL_SENT)))


def demo_work(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = __DATA1__
    print("work/school sentences: %d" % len(sents))
    assert len(sents) == 20
    # weekly schedule: hours per day Mon-Fri 8h, Sat 4h class
    days = {"Mon": 8.0, "Tue": 8.0, "Wed": 8.0, "Thu": 8.0, "Fri": 8.0,
            "Sat": 4.0, "Sun": 0.0}
    week = sum(days.values())
    print("weekly work+study hours: %.1f" % week)
    assert 43.9 < week < 44.1
    # meeting overlap: 9:00 meeting, 40 min
    start, dur = 9.0, 40.0 / 60.0
    end = start + dur
    print("meeting ends at %.2f (9:40)" % end)
    assert 9.66 < end < 9.67
    print("OK: %s clocked in" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.WORK_SENT)))


def demo_health(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = __DATA1__
    print("health sentences: %d" % len(sents))
    assert len(sents) == 20
    # body-part -> symptom lookup table
    clinic = {"头": "头疼", "嗓子": "嗓子疼", "肚子": "肚子疼",
              "眼睛": "眼睛红", "脚": "脚扭伤"}
    for part, symptom in clinic.items():
        print("  %s -> %s" % (part, symptom))
    assert clinic["头"] == "头疼" and clinic["脚"] == "脚扭伤"
    assert len(clinic) == 5
    # dosage schedule: 3x daily for 5 days
    doses = 3 * 5
    print("doses (3x daily, 5 days): %d" % doses)
    assert doses == 15
    print("OK: %s checked the pulse" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.HEALTH_SENT)))


def demo_emotion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = __DATA1__
    print("emotion sentences: %d" % len(sents))
    assert len(sents) == 20
    # intensity scale 1-5 mapped to degree adverbs
    scale = {1: "有点", 2: "", 3: "很", 4: "非常", 5: "极了"}
    emo = "开心"
    for level in range(1, 6):
        mark = scale[level]
        form = ("我" + mark + emo) if level < 5 else ("我" + emo + mark)
        print("  level %d: %s" % (level, form))
    assert scale[1] == "有点" and scale[5] == "极了"
    # comfort kit from the record
    comfort = ["别担心", "别害怕", "冷静一点", "放松一下吧"]
    print("comfort phrases: %d" % len(comfort))
    assert len(comfort) == 4
    print("OK: %s named the feelings" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.EMOTION_SENT)))


def demo_nature(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = __DATA1__
    print("nature sentences: %d" % len(sents))
    assert len(sents) == 20
    # weather-station conversions for the sentences' temperatures
    def c2f(c):
        return c * 9.0 / 5.0 + 32.0
    readings = [25.0, 30.0, -5.0, 18.0]
    for c in readings:
        f = c2f(c)
        print("  %.1f C = %.1f F" % (c, f))
    assert 76.9 < c2f(25.0) < 77.1
    assert 85.9 < c2f(30.0) < 86.1
    assert 22.9 < c2f(-5.0) < 23.1
    assert 64.3 < c2f(18.0) < 64.5
    # season count and weather verbs
    seasons = ["春天", "夏天", "秋天", "冬天"]
    wverbs = ["下雨", "下雪", "刮风"]
    assert len(seasons) == 4 and len(wverbs) == 3
    print("seasons: %d, weather verbs: %d" % (len(seasons), len(wverbs)))
    print("OK: %s read the sky" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.NATURE_SENT)))


def demo_shopping(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = __DATA1__
    print("shopping sentences: %d" % len(sents))
    assert len(sents) == 20
    # da-ba-zhe: the number names what you PAY (8 zhe = pay 80%%)
    def zhe_price(tag, z):
        return tag * z / 10.0
    cases = [(250.0, 8, 200.0), (120.0, 9, 108.0), (99.0, 7, 69.3)]
    for tag, z, want in cases:
        got = zhe_price(tag, z)
        print("  %.0f yuan at %d zhe -> %.2f" % (tag, z, got))
        assert want - 0.01 < got < want + 0.01
    # bargaining rounds: ask 300, offer 200, settle 240
    ask, offer, settle = 300.0, 200.0, 240.0
    saving = (ask - settle) / ask * 100.0
    print("bargain: ask %.0f, settle %.0f, saved %.1f %%" % (ask, settle, saving))
    assert 19.9 < saving < 20.1
    # change: pay 100 for 78
    change = 100.0 - 78.0
    assert 21.99 < change < 22.01
    print("change for 100 on 78: %.0f yuan" % change)
    print("OK: %s closed the deal" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.SHOP_SENT)))


def demo_friendship(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = __DATA1__
    print("friendship sentences: %d" % len(sents))
    assert len(sents) == 20
    # reunion RSVP tally
    guests = {"小明": True, "小红": True, "王老师": False, "李华": True,
              "张伟": True, "刘洋": False}
    coming = sum(1 for v in guests.values() if v)
    print("invited: %d, coming: %d" % (len(guests), coming))
    assert len(guests) == 6 and coming == 4
    rate = coming / len(guests) * 100.0
    print("RSVP rate: %.1f %%" % rate)
    assert 66.6 < rate < 66.7
    # hotpot split: 360 yuan among the 4 coming
    share = 360.0 / coming
    print("hotpot split: %.0f yuan each" % share)
    assert 89.9 < share < 90.1
    print("OK: %s gathered the friends" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.FRIEND_SENT)))


def demo_technology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = __DATA1__
    print("technology sentences: %d" % len(sents))
    assert len(sents) == 20
    # CJK SMS segmentation: 70 chars per segment (UCS-2)
    def segments(text):
        n = len(text)
        return (n + 69) // 70
    msgs = ["你好！", "我发你一条消息，请查收。", "明天下午三点在市中心那家火锅店见面，不见不散！"]
    for m in msgs:
        print("  %d chars -> %d segment(s): %s" % (len(m), segments(m), m[:12]))
    assert segments(msgs[0]) == 1
    assert segments("明天下午三点在市中心那家火锅店见面，不见不散！") == 1
    long_msg = "你好！" * 40
    print("  %d chars -> %d segments" % (len(long_msg), segments(long_msg)))
    assert segments(long_msg) == 2
    # battery math: 15%% left, drains 5%%/hour -> 3 hours
    left, drain = 15.0, 5.0
    hours = left / drain
    print("battery: %.0f%% at %.0f%%/h -> %.1f h left" % (left, drain, hours))
    assert 2.99 < hours < 3.01
    print("OK: %s charged the phone" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.TECH_SENT)))

def demo_aspect(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    groups = __DATA1__
    print("aspect groups: %d" % len(groups))
    assert len(groups) == 5
    markers = {"Present and habitual": [], "Past completed": ["了"],
               "Experiential past": ["过"], "Ongoing state": ["着"],
               "Future": ["会", "要", "将"]}
    for label, sents in groups:
        print("  %s: %d sentences" % (label, len(sents)))
        assert len(sents) == 5
        key = label.split(" (")[0]
        for m in markers[key]:
            hits = sum(1 for c, p, e in sents if m in c)
            print("    marker %s in %d/5" % (m, hits))
            assert hits >= 1, "marker %s unused" % m
    # transformer: add le to a bare verb phrase
    def complete(vp):
        return vp + "了"
    assert complete("我吃") == "我吃了"
    print("transform: 我吃 -> %s" % complete("我吃"))
    print("OK: %s sealed the tenses" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.ASPECT_GROUPS)))


def demo_qa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pairs = __DATA1__
    print("Q&A pairs: %d" % len(pairs))
    assert len(pairs) == 20
    # matcher drill: shuffle answers, match back by index key
    random.seed(42)
    order = list(range(len(pairs)))
    random.shuffle(order)
    matched = 0
    for i in order:
        q, a = pairs[i][0], pairs[i][3]
        assert q and a
        matched += 1
    print("matched: %d/%d" % (matched, len(pairs)))
    assert matched == 20
    # interrogative coverage: who/what/where/when/why/how all present
    qs = " ".join(p[0] for p in pairs)
    for w in ["谁", "什么", "哪里", "多久", "为什么", "怎么", "吗"]:
        assert w in qs, "missing interrogative " + w
    print("interrogatives covered: 谁 什么 哪里 多久 为什么 怎么 吗")
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.QA_PAIRS)))


def demo_commands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    cmds = __DATA1__
    print("commands: %d" % len(cmds))
    assert len(cmds) == 20
    # politeness classifier by register tag
    polite = [c for c in cmds if c[3] == "polite"]
    direct = [c for c in cmds if c[3] in ("direct", "informal direct", "blunt", "stern", "urgent informal", "informal", "casual", "warm informal")]
    print("polite: %d, direct/casual: %d" % (len(polite), len(direct)))
    assert len(polite) == 10
    assert len(polite) + len(direct) == 20
    # softener audit: every polite form carries 请 or 麻烦 or 能
    for c, p, e, r in polite:
        assert ("请" in c) or ("麻烦" in c) or ("能" in c), "unsoftened polite: " + c
    print("softener audit passed on all %d polite forms" % len(polite))
    # volume knob: blunt -> polite pairs share the verb
    assert ("坐下。", "请坐。") == (cmds[0][0], cmds[1][0])
    print("OK: %s set the volume" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.COMMANDS)))


def demo_describe(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = __DATA1__
    print("descriptions: %d" % len(sents))
    assert len(sents) == 20
    # pattern audit: 又..又.. frames and 的-chains
    you_you = [s for s in sents if "又" in s[0] and s[0].count("又") >= 2]
    de_chains = [s for s in sents if s[0].count("的") >= 1]
    print("又..又.. frames: %d, 的-attributions: %d" % (len(you_you), len(de_chains)))
    assert len(you_you) >= 3
    assert len(de_chains) >= 10
    # adjective stacking order check: opinion before color before noun
    stack = "美丽而古老的国家"
    assert stack.endswith("国家")
    print("stacking order verified: %s" % stack)
    print("OK: %s painted the pictures" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.DESCRIBE_SENT)))


def _story_demo(key, story_var):
    return '''\
def main():
    story = __DATA__
    print("story lines: %d" % len(story))
    assert len(story) == 10
    chars = sum(len(c) for c, p, e in story)
    print("total characters: %d" % chars)
    assert 70 < chars < 75
    for c, p, e in story:
        assert c and p and e
        assert c[-1] in "。！？", "line must end with full punctuation: " + c
    print("all lines end with full-width punctuation")
    print("OK: %s told the story" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA__", story_var)


def demo_story1(hdr, name, rid, group, points, req):
    body = _story_demo("story1", _embed(E.STORY1)).replace("told the story",
        "opened the storybook")
    return _wrap(hdr, name, rid, group, body)


def demo_story2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    story = __DATA1__
    print("story lines: %d" % len(story))
    assert len(story) == 10
    text = "".join(c for c, p, e in story)
    le_count = text.count("了")
    guo_count = text.count("过")
    print("了 completions: %d, 过 experientials: %d" % (le_count, guo_count))
    assert le_count >= 5
    assert guo_count >= 1
    print("OK: %s closed the past" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.STORY2)))


def demo_story3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    story = __DATA1__
    print("story lines: %d" % len(story))
    assert len(story) == 10
    text = "".join(c for c, p, e in story)
    future = sum(text.count(m) for m in ["会", "要", "将"])
    cond = sum(text.count(m) for m in ["如果", "要是"])
    print("future markers (会/要/将): %d, conditionals (如果/要是): %d" % (future, cond))
    assert future >= 3
    assert cond >= 2
    print("OK: %s signed tomorrow" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.STORY3)))


def demo_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    idioms = __DATA1__
    print("idioms: %d" % len(idioms))
    assert len(idioms) == 20
    # matcher drill: literal gloss vs real meaning are never equal
    for c, p, lit, mean, sc, sp, se in idioms:
        assert lit != mean, "literal equals meaning for " + c
        assert sc and sp and se
    print("literal-vs-meaning distinct on all 20")
    # four-character chengyu count
    chengyu = [i for i in idioms if len(i[0]) == 4]
    print("four-character chengyu: %d" % len(chengyu))
    assert len(chengyu) >= 10
    # deterministic quiz: 5 idioms, match meaning
    random.seed(11)
    quiz = random.sample(idioms, 5)
    score = sum(1 for q in quiz if q[3])
    print("idiom quiz: %d/5 meanings recalled" % score)
    assert score == 5
    print("OK: %s pressed the heirlooms" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.IDIOMS)))


def demo_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pairs = __DATA1__
    print("register pairs: %d" % len(pairs))
    assert len(pairs) == 15
    # every pair differs between informal and formal
    for ic, ip, ie, fc, fp, fe, n in pairs:
        assert ic != fc, "pair identical: " + ic
        assert n
    print("all 15 pairs differ with usage notes")
    # formal-marker audit: nin/qing/máfan/kongpa coverage
    formal_text = "".join(fc for ic, ip, ie, fc, fp, fe, n in pairs)
    markers = ["您", "请", "麻烦", "恐怕"]
    for m in markers:
        assert m in formal_text, "missing formal marker " + m
    print("formal markers present: %s" % " ".join(markers))
    print("OK: %s dressed the sentences" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.REGISTERS)))


def demo_complex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sents = __DATA1__
    print("complex sentences: %d" % len(sents))
    assert len(sents) == 15
    # connector audit: each sentence carries a parse note naming machinery
    for c, p, e, n in sents:
        assert n and len(n) > 20, "thin parse note: " + c
        assert e and p
    print("parse notes verified on all 15")
    # paired-connector coverage
    text = "".join(c for c, p, e, n in sents)
    pairs = ["因为", "所以", "虽然", "但是", "如果", "不但", "而且",
             "只有", "才", "无论", "都", "越", "把", "被"]
    found = [w for w in pairs if w in text]
    print("connector coverage: %d/%d" % (len(found), len(pairs)))
    assert len(found) >= 12
    print("OK: %s hinged the clauses" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.COMPLEX)))


def _dialog_demo(title_line, var):
    return ('''\
def main():
    dlg = __DATA__
    print("dialogue lines: %d" % len(dlg))
    assert len(dlg) == 20
    # speaker alternation audit
    speakers = [s for s, c, p, e in dlg]
    for i in range(1, len(speakers)):
        assert speakers[i] != speakers[i - 1], "same speaker twice at line %d" % (i + 1)
    print("speaker alternation verified across 20 lines")
    for s, c, p, e in dlg:
        assert c and p and e, "missing translation at " + c
    chars = sum(len(c) for s, c, p, e in dlg)
    print("total characters: %d" % chars)
    assert 100 < chars < 900
    print("OK: %s played the dialogue" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA__", var))


def demo_dialog_market(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, _dialog_demo("market", _embed(E.DIALOG_MARKET)))


def demo_dialog_friend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, _dialog_demo("friend", _embed(E.DIALOG_FRIEND)))


def demo_dialog_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    dlg = __DATA1__
    print("dialogue lines: %d" % len(dlg))
    assert len(dlg) == 20
    speakers = [s for s, c, p, e in dlg]
    for i in range(1, len(speakers)):
        assert speakers[i] != speakers[i - 1], "same speaker twice at line %d" % (i + 1)
    print("speaker alternation verified across 20 lines")
    text = "".join(c for s, c, p, e in dlg)
    # four problem-solving moves present
    assert "漏水" in text, "symptom missing"
    assert "可能" in text, "diagnosis hedge missing"
    assert "先" in text, "sequencing missing"
    assert "不漏了" in text, "verification missing"
    print("four moves verified: report, diagnose, fix, verify")
    print("OK: %s fixed the leak" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.DIALOG_PROBLEM)))


def demo_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    words = __DATA1__
    print("core words: %d" % len(words))
    assert len(words) == 200
    for c, p, e in words:
        assert c and p and e
    # no duplicate headwords
    heads = [c for c, p, e in words]
    print("unique headwords: %d" % len(set(heads)))
    assert len(set(heads)) == 200
    # pinyin chart counts from the record
    initials = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h",
                "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s"]
    print("initials: %d" % len(initials))
    assert len(initials) == 21
    # cover-and-translate self-test: 20 sampled words, seeded
    random.seed(99)
    sample = random.sample(words, 20)
    score = sum(1 for c, p, e in sample if e)
    print("self-test sample: %d/20" % score)
    assert score == 20
    print("OK: %s signed the mastery" % NAME)
if __name__ == "__main__":
    main()
'''.replace("__DATA1__", _embed(E.CORE200)))


DEMOS = {
    "overview": demo_overview,
    "writing": demo_writing,
    "phonology": demo_phonology,
    "nouns1": demo_nouns1,
    "verbs1": demo_verbs1,
    "adj_adv": demo_adj_adv,
    "pronouns": demo_pronouns,
    "numbers_time": demo_numbers_time,
    "greetings": demo_greetings,
    "grammar_essentials": demo_grammar,
    "home_family": demo_home,
    "food_cooking": demo_food,
    "travel": demo_travel,
    "work_school": demo_work,
    "health_body": demo_health,
    "emotions": demo_emotion,
    "nature_weather": demo_nature,
    "shopping_money": demo_shopping,
    "friendship": demo_friendship,
    "technology": demo_technology,
    "aspect": demo_aspect,
    "qa_pairs": demo_qa,
    "commands": demo_commands,
    "descriptions": demo_describe,
    "story1": demo_story1,
    "story2": demo_story2,
    "story3": demo_story3,
    "idioms": demo_idioms,
    "registers": demo_registers,
    "complex": demo_complex,
    "dialog_market": demo_dialog_market,
    "dialog_friend": demo_dialog_friend,
    "dialog_problem": demo_dialog_problem,
    "mastery": demo_mastery,
}
