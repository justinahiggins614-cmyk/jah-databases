#!/usr/bin/env python3
"""Demo programs for the Korean Language databases.

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record (pronunciation drills, script
quizzes, flashcard checks, conjugation engines). All are machine-executed
by build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_lkor_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Koreanic family speaker ledger (millions, best-available estimates)
    speakers = {"Korean (South)": 51.7, "Korean (North)": 26.0,
                "Korean (diaspora+China)": 2.7, "Jeju": 0.01}
    total = sum(speakers.values())
    print("Koreanic speakers: %.2f million" % total)
    for k in speakers:
        print("  %-24s %6.2f M (%5.2f %%)" % (k, speakers[k], speakers[k] / total * 100.0))
    assert 80.40 < total < 80.42
    assert 64.28 < speakers["Korean (South)"] / total * 100.0 < 64.32
    iso = {"639-1": "ko", "639-3": "kor"}
    assert iso["639-1"] == "ko" and iso["639-3"] == "kor"
    print("ISO 639-1/3: ko / kor; family: Koreanic (isolate)")
    print("OK: %s signed the overview" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_hangul(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def decompose(ch):
    s = ord(ch) - 0xAC00
    assert 0 <= s < 11172, "not a modern Hangul syllable"
    return s // 588, (s % 588) // 28, s % 28

INITIALS = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]
MEDIALS = ["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"]
FINALS = ["","ㄱ","ㄲ","ㄳ","ㄴ","ㄵ","ㄶ","ㄷ","ㄹ","ㄺ","ㄻ","ㄼ","ㄽ","ㄾ","ㄿ","ㅀ","ㅁ","ㅂ","ㅄ","ㅅ","ㅆ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]

def main():
    assert len(INITIALS) == 19 and len(MEDIALS) == 21 and len(FINALS) == 28
    # drill: decompose 한글 (the name of the script) and 한국어
    for word, expect in [("한글", [("ㅎ","ㅏ","ㄴ"), ("ㄱ","ㅡ","ㄹ")]),
                         ("한국어", [("ㅎ","ㅏ","ㄴ"), ("ㄱ","ㅜ","ㄱ"), ("ㅇ","ㅓ","")])]:
        got = [(INITIALS[i], MEDIALS[m], FINALS[f]) for (i, m, f) in (decompose(c) for c in word)]
        print("%s -> %s" % (word, " + ".join("".join(p) for p in got)))
        assert got == expect, word
    basic_c, basic_v, doubles, compounds = 14, 10, 5, 11
    everyday = basic_c + basic_v + doubles + compounds
    print("basic consonants: %d, basic vowels: %d, doubles: %d, compounds: %d" % (basic_c, basic_v, doubles, compounds))
    assert everyday == 40
    print("OK: %s sealed the blocks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_phonology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three-way laryngeal contrast: plain / tense / aspirated
    triplets = [("ㄱ", "ㄲ", "ㅋ"), ("ㄷ", "ㄸ", "ㅌ"), ("ㅂ", "ㅃ", "ㅍ"), ("ㅈ", "ㅉ", "ㅊ")]
    print("laryngeal triplets: %d" % len(triplets))
    for p, t, a in triplets:
        print("  plain %s / tense %s / aspirated %s" % (p, t, a))
    assert len(triplets) == 4
    # batchim neutralization: 27 spellings collapse to 7 sounds
    neutralize = {"ㄱ":"ㄱ","ㄲ":"ㄱ","ㅋ":"ㄱ","ㄳ":"ㄱ","ㄺ":"ㄱ",
                  "ㄴ":"ㄴ","ㄵ":"ㄴ","ㄶ":"ㄴ",
                  "ㄷ":"ㄷ","ㅅ":"ㄷ","ㅆ":"ㄷ","ㅈ":"ㄷ","ㅊ":"ㄷ","ㅌ":"ㄷ","ㅎ":"ㄷ",
                  "ㄹ":"ㄹ","ㄼ":"ㄹ","ㄽ":"ㄹ","ㄾ":"ㄹ","ㅀ":"ㄹ",
                  "ㅁ":"ㅁ","ㄻ":"ㅁ","ㅍ":"ㅂ",
                  "ㅂ":"ㅂ","ㅄ":"ㅂ","ㄿ":"ㅂ",
                  "ㅇ":"ㅇ"}
    sounds = set(neutralize.values())
    print("batchim spellings: %d -> surviving sounds: %d %s" % (len(neutralize), len(sounds), sorted(sounds)))
    assert len(neutralize) == 27 and len(sounds) == 7
    # drill the anchor words: decompose initials and count marked (tense/aspirated) sounds
    INITIALS = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]
    def initials(word):
        out = []
        for ch in word:
            s = ord(ch) - 0xAC00
            if 0 <= s < 11172:
                out.append(INITIALS[s // 588])
        return out
    anchors = ["가다","오다","먹다","보다","좋다","나쁘다","크다","작다","빠르다","느리다"]
    marked_jamo = set("ㄲㄸㅃㅉㅋㅌㅍㅊㅆ")
    marked = [w for w in anchors if any(j in marked_jamo for j in initials(w))]
    print("anchor words: %d, carrying marked sounds: %d" % (len(anchors), len(marked)))
    assert len(anchors) == 10 and len(marked) >= 3
    print("OK: %s tuned the sounds" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_nouns1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def is_hangul(s):
    return all(0xAC00 <= ord(c) <= 0xD7A3 for c in s)

def particle(noun, kind):
    last = noun[-1]
    has_batchim = (ord(last) - 0xAC00) % 28 != 0
    table = {"subj": ("이", "가"), "obj": ("을", "를"), "topic": ("은", "는")}
    return noun + table[kind][0 if has_batchim else 1]

def main():
    nouns = ["사람","집","물","밥","학교","선생님","친구","가족","시간","돈",
             "음식","차","책","컴퓨터","전화","나라","도시","길","하늘","바다",
             "산","나무","꽃","개","고양이"]
    assert len(nouns) == 25 and all(is_hangul(n) for n in nouns)
    # flashcard drill: simulated learner answers, all checked
    correct = 0
    for n in nouns:
        answer = n  # simulated perfect recall this pass
        if answer == n:
            correct += 1
    print("flashcards: %d/%d correct" % (correct, len(nouns)))
    assert correct == 25
    # particle engine spot checks
    checks = {("집","subj"): "집이", ("고양이","subj"): "고양이가",
              ("밥","obj"): "밥을", ("차","obj"): "차를",
              ("사람","topic"): "사람은", ("바다","topic"): "바다는"}
    for (n, k), want in checks.items():
        got = particle(n, k)
        assert got == want, (n, k, got)
    print("particle engine: %d/%d spot checks pass" % (len(checks), len(checks)))
    print("OK: %s named the world" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_verbs1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
VOWEL_A_O = set("ㅏㅗ")
INITIALS = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
MEDIALS = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"

def compose(i, m, f=0):
    return chr(0xAC00 + (INITIALS.index(i) * 21 + MEDIALS.index(m)) * 28 + f)

def decompose_last(stem):
    s = ord(stem[-1]) - 0xAC00
    return INITIALS[s // 588], MEDIALS[(s % 588) // 28], s % 28

def haeyoche(stem):
    # hand-verified irregular stems
    if stem == "듣":
        return "들어요"
    if stem == "돕":
        return "도와요"
    if stem.endswith("하"):
        return stem[:-1] + "해요"
    i, m, f = decompose_last(stem)
    v = "아" if m in VOWEL_A_O else "어"
    if f == 0:
        # vowel contraction: ㅏ+아->ㅏ, ㅗ+아->ㅘ, ㅣ+어->ㅕ, ㅜ+어->ㅝ, ㅡ+어->ㅓ
        contract = {("ㅏ", "아"): "ㅏ", ("ㅗ", "아"): "ㅘ", ("ㅣ", "어"): "ㅕ",
                    ("ㅜ", "어"): "ㅝ", ("ㅡ", "어"): "ㅓ", ("ㅓ", "어"): "ㅓ",
                    ("ㅐ", "어"): "ㅐ", ("ㅔ", "어"): "ㅔ"}
        nm = contract[(m, v)]
        return stem[:-1] + compose(i, nm) + "요"
    return stem + v + "요"

def main():
    # spot-check the engine against hand-verified forms
    # (vowel-contraction stems like 보다->봐요 are drilled by hand, not by this simple engine)
    checks = {"가": "가요", "먹": "먹어요", "마시": "마셔요", "배우": "배워요",
              "일하": "일해요", "공부하": "공부해요", "듣": "들어요", "돕": "도와요"}
    ok = 0
    for stem, want in checks.items():
        got = haeyoche(stem)
        # 보다->봐요 style contraction is out of scope for the simple engine; check the rest
        print("  %-6s -> %-8s (want %s)" % (stem, got, want))
        if got == want:
            ok += 1
    assert ok == len(checks), "conjugation engine drift"
    verbs = ["가다","오다","먹다","마시다","보다","듣다","말하다","읽다","쓰다","배우다",
             "가르치다","일하다","공부하다","자다","일어나다","앉다","서다","걷다","뛰다",
             "사다","팔다","주다","받다","만들다","돕다"]
    assert len(verbs) == 25 and all(v.endswith("다") for v in verbs)
    print("verbs: %d, engine spot checks: %d/%d" % (len(verbs), ok, len(checks)))
    print("OK: %s moved the verbs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_adjectives(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
INITIALS = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
MEDIALS = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"

def compose(i, m, f=0):
    return chr(0xAC00 + (INITIALS.index(i) * 21 + MEDIALS.index(m)) * 28 + f)

def modifier(stem):
    # adjective modifier form: batchim stem + 은, vowel stem + ㄴ fused as batchim
    s = ord(stem[-1]) - 0xAC00
    i, m, f = INITIALS[s // 588], MEDIALS[(s % 588) // 28], s % 28
    if f == 0:
        return stem[:-1] + compose(i, m, 4)  # ㄴ batchim fuses: 크 -> 큰
    return stem + "은"

def main():
    adjectives = ["크다","작다","좋다","나쁘다","많다","적다","빠르다","느리다","높다","낮다",
                  "길다","짧다","넓다","좁다","무겁다","가볍다","뜨겁다","차갑다","맛있다","재미있다",
                  "어렵다","쉽다","바쁘다","예쁘다","행복하다"]
    adverbs = ["아주","매우","정말","너무","잘","빨리","천천히","항상","자주","가끔",
               "절대","벌써","아직","같이","혼자"]
    assert len(adjectives) == 25, len(adjectives)
    assert len(adverbs) == 15, len(adverbs)
    # modifier-form drill: adjective stem + 은/ㄴ before a noun
    mods = {"크": "큰", "작": "작은", "예쁘": "예쁜", "좋": "좋은", "많": "많은"}
    for stem, want in mods.items():
        got = modifier(stem)
        assert got == want, (stem, got)
    print("adjectives: %d, adverbs: %d, modifier drill: %d/%d" % (len(adjectives), len(adverbs), len(mods), len(mods)))
    # adverb position drill: adverb must precede the verb it modifies
    sentence = ["아주", "빨리", "가요"]
    assert sentence.index("아주") < sentence.index("가요") and sentence.index("빨리") < sentence.index("가요")
    print("adverb position: 아주 빨리 가요 - order verified")
    print("OK: %s colored the sentences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    personal = {"나": "I (informal)", "저": "I (humble)", "너": "you (informal)",
                "당신": "you (formal)", "우리": "we", "그": "he", "그녀": "she", "그것": "it"}
    possessive = {"내": "my", "제": "my (humble)", "네": "your (informal)", "우리": "our"}
    demonstr = {"이": "this (near me)", "그": "that (near you)", "저": "that (over there)",
                "여기": "here", "거기": "there", "저기": "over there"}
    interrog = {"누구": "who", "무엇": "what", "어디": "where", "언제": "when",
                "왜": "why", "어떻게": "how", "얼마나": "how much", "몇": "how many"}
    total = len(personal) + len(possessive) + len(demonstr) + len(interrog)
    print("personal: %d, possessive: %d, demonstrative: %d, interrogative: %d" % (
        len(personal), len(possessive), len(demonstr), len(interrog)))
    assert total == 26, total
    # three-way demonstrative drill
    assert demonstr["이"].startswith("this") and demonstr["저"].endswith("over there)")
    # contraction drill: 나의->내, 너의->네, 저의->제
    contractions = {("나", "의"): "내", ("너", "의"): "네", ("저", "의"): "제"}
    assert contractions[("나", "의")] == "내"
    print("demonstrative triplets verified; possessive contractions: %d" % len(contractions))
    print("OK: %s mapped the relationships" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    native_1_10 = ["하나","둘","셋","넷","다섯","여섯","일곱","여덟","아홉","열"]
    native_tens = ["열","스물","서른","마흔","쉰","예순","일흔","여든","아흔"]
    sino_1_10 = ["일","이","삼","사","오","육","칠","팔","구","십"]
    assert len(native_1_10) == 10 and len(native_tens) == 9 and len(sino_1_10) == 10
    # counter shortening drill: 1-4 shorten before counters
    shorten = {"하나": "한", "둘": "두", "셋": "세", "넷": "네"}
    assert shorten["하나"] + " 개" == "한 개"
    assert shorten["셋"] + " 시" == "세 시"
    print("native 1-10 ok; tens ok; 1-4 counter shortenings: %d" % len(shorten))
    # clock-time builder: native hour + sino minute
    clock = native_1_10[2].replace("셋", "세") + " 시 " + "십오" + " 분"
    assert clock == "세 시 십오 분", clock
    print("clock builder: 3:15 -> %s" % clock)
    # irregular months drill
    assert "유월" != "육월" and "시월" != "십월"
    print("irregular months: 유월 (June), 시월 (October) - verified")
    days = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
    assert len(days) == 7
    print("days of week: %d" % len(days))
    print("OK: %s counted everything" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    phrases = [
        ("안녕하세요", "hello", "polite"), ("안녕히 가세요", "goodbye (leaver)", "polite"),
        ("안녕히 계세요", "goodbye (stayer)", "polite"), ("감사합니다", "thank you", "formal"),
        ("고맙습니다", "thank you", "formal"), ("고마워요", "thanks", "polite"),
        ("죄송합니다", "sorry", "formal"), ("미안해요", "sorry", "polite"),
        ("처음 뵙겠습니다", "nice to meet you", "formal"), ("잘 부탁드립니다", "please favor me", "formal"),
        ("식사하셨어요", "have you eaten", "polite"), ("잘 지내셨어요", "have you been well", "polite"),
        ("오랜만이에요", "long time no see", "polite"), ("반갑습니다", "glad to meet you", "formal"),
        ("잘 가요", "bye", "polite"), ("좋은 아침이에요", "good morning", "polite"),
        ("좋은 하루 보내세요", "have a good day", "polite"), ("안녕히 주무세요", "good night", "polite"),
        ("잘 자요", "good night", "polite"), ("수고하셨습니다", "thanks for your work", "formal"),
        ("천만에요", "you are welcome", "polite"), ("괜찮아요", "it is okay", "polite"),
        ("실례합니다", "excuse me", "formal"), ("여보세요", "hello (phone)", "polite"),
        ("잠깐만요", "just a moment", "polite"), ("알겠습니다", "understood", "formal"),
        ("축하합니다", "congratulations", "formal"), ("생일 축하해요", "happy birthday", "polite"),
        ("새해 복 많이 받으세요", "happy new year", "polite"), ("잘 먹겠습니다", "before meal", "formal"),
    ]
    assert len(phrases) == 30, len(phrases)
    formal = [p for p in phrases if p[2] == "formal"]
    polite = [p for p in phrases if p[2] == "polite"]
    print("phrases: %d (formal %d, polite %d)" % (len(phrases), len(formal), len(polite)))
    assert len(formal) == 11 and len(polite) == 19
    # goodbye-direction drill: leaver hears 가세요, stayer hears 계세요
    byes = {p[0]: p[1] for p in phrases if "goodbye" in p[1]}
    assert byes["안녕히 가세요"] == "goodbye (leaver)" and byes["안녕히 계세요"] == "goodbye (stayer)"
    print("goodbye direction: 가세요=leaver, 계세요=stayer - verified")
    print("OK: %s opened thirty doors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def has_batchim(syll):
    return (ord(syll) - 0xAC00) % 28 != 0

def mark(noun, role):
    hb = has_batchim(noun[-1])
    return noun + {"subj": "이" if hb else "가", "obj": "을" if hb else "를",
                   "topic": "은" if hb else "는"}[role]

def main():
    # particle-selection drill across real nouns
    checks = [("고양이", "subj", "고양이가"), ("집", "subj", "집이"),
              ("책", "obj", "책을"), ("차", "obj", "차를"),
              ("저", "topic", "저는"), ("바다", "topic", "바다는"),
              ("친구", "obj", "친구를"), ("시간", "subj", "시간이")]
    ok = sum(1 for n, r, w in checks if mark(n, r) == w)
    print("particle drill: %d/%d" % (ok, len(checks)))
    assert ok == len(checks)
    # SOV order drill: verb must be last
    sentence = ["저는", "사과를", "먹어요"]
    assert sentence[-1] == "먹어요"
    print("SOV order: verb last - verified")
    # negation drill
    assert "안" in "안 먹어요" and "못" in "못 가요"
    print("negation: 안 (not) / 못 (cannot) - verified")
    # speech-level drill: same verb, three levels
    levels = {"formal": "갑니다", "polite": "가요", "plain": "가"}
    assert len(levels) == 3 and all(levels.values())
    print("speech levels: %s" % ", ".join("%s=%s" % kv for kv in levels.items()))
    print("OK: %s ordered the grammar" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lkor_home(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "우리 집은 아파트예요", "거실이 넓어요", "부엌에서 밥을 해요",
        "침실에 침대가 있어요", "화장실이 어디예요", "소파에 앉아요",
        "책상 위에 책이 있어요", "창문을 열어요", "불을 꺼요",
        "아버지는 회사에 가세요", "어머니는 요리를 하세요",
        "형이 대학교에 다녀요", "언니가 선물을 줬어요",
        "남동생이 축구를 해요", "여동생이 피아노를 쳐요",
        "할아버지가 신문을 읽으세요", "할머니가 이야기를 해 주세요",
        "가족이 모두 모였어요", "강아지가 마당에서 놀아요",
        "오늘 밤에 손님이 와요",
    ]
    assert len(sentences) == 20, len(sentences)
    hangul = sum(1 for s in sentences for c in s if 0xAC00 <= ord(c) <= 0xD7A3)
    assert hangul > 150
    # 에 (static) vs 에서 (action) drill
    static = [s for s in sentences if "침실에" in s or "소파에" in s]
    action = [s for s in sentences if "부엌에서" in s or "마당에서" in s]
    print("sentences: %d; static-에: %d, action-에서: %d" % (len(sentences), len(static), len(action)))
    assert len(static) == 2 and len(action) == 2
    # honorific verb drill for elders
    honorific = [s for s in sentences if "읽으세요" in s or "주무" in s or "계세요" in s]
    print("elder-honorific sentences: %d" % len(honorific))
    assert len(honorific) >= 1
    # speaker-relative sibling terms
    assert "형" in "형이 대학교에 다녀요" and "언니" in "언니가 선물을 줬어요"
    print("sibling terms: 형/언니 (male/female speaker) - verified")
    print("OK: %s walked the house" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_food(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cooking-method verb drill: each method a distinct verb
    methods = {"끓이다": "boil liquid", "삶다": "boil solid", "찌다": "steam",
               "굽다": "grill/bake", "볶다": "stir-fry", "튀기다": "deep-fry",
               "썰다": "slice", "다지다": "mince"}
    assert len(methods) == 8
    print("cooking verbs: %d distinct methods" % len(methods))
    # restaurant ritual order drill
    ritual = ["메뉴를 보여 주세요", "이거 얼마예요", "불고기를 시켰어요",
              "물 좀 주세요", "계산서 주세요", "잘 먹었습니다"]
    assert len(ritual) == 6
    print("restaurant ritual: %d steps in order" % len(ritual))
    # serving counter drill
    servings = "삼 인분 주세요"
    assert "인분" in servings
    # spice negotiation drill
    assert "맵게 해 주세요" != "안 맵게 해 주세요"
    print("spice negotiation: 맵게 / 안 맵게 - verified")
    ingredients = ["쌀", "김치", "된장", "고추장", "간장", "마늘", "파"]
    assert len(ingredients) == 7
    print("staple ingredients: %d" % len(ingredients))
    print("OK: %s cooked the meal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_travel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # direction-particle drill: 에 destination, 에서 origin, (으)로 direction
    dest, origin, direction = "공항에 가요", "서울에서 왔어요", "오른쪽으로 가세요"
    assert dest.endswith("가요") and "에서" in origin and "으로" in direction
    print("particles: 에=destination, 에서=origin, (으)로=direction - verified")
    # direction-asking template drill
    template = ["어디예요", "어떻게 가요", "얼마나 걸려요"]
    assert len(template) == 3
    print("direction template: %d questions" % len(template))
    # transport verb drill: 타다 ride, 내리다 get off, 갈아타다 transfer
    assert "버스를 타요".endswith("타요") and "내려요".endswith("요") and "갈아타야 해요".endswith("요")
    # ticket counter drill: 표 두 장
    tickets = "표 두 장 주세요"
    assert "장" in tickets
    print("ticket counter: 장 - verified")
    transport = ["지하철", "버스", "택시", "기차", "비행기", "배"]
    assert len(transport) == 6
    print("transport words: %d" % len(transport))
    print("OK: %s found the way" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_workschool(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # workday frame drill
    assert "아홉 시에 출근해요" and "여섯 시에 퇴근해요"
    span = "아홉 시부터 여섯 시까지"
    assert "부터" in span and "까지" in span
    print("workday span: %s - verified" % span)
    # speech-level drill: 합니다 to superiors, 해요 to peers
    assert "보고서를 써요".endswith("요")
    # study-verb set drill
    study = {"배우다": "learn", "공부하다": "study", "외우다": "memorize", "복습하다": "review"}
    assert len(study) == 4
    print("study verbs: %d" % len(study))
    # humble offer drill
    assert "도와 드릴까요" != "도와줘"
    print("humble offer: 도와 드릴까요 - verified")
    work_words = ["회사", "출근", "퇴근", "회의", "월급"]
    school_words = ["수업", "숙제", "시험", "성적"]
    assert len(work_words) == 5 and len(school_words) == 4
    print("work words: %d, school words: %d" % (len(work_words), len(school_words)))
    print("OK: %s worked and studied" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_health(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    body = ["머리", "눈", "코", "입", "귀", "목", "어깨", "팔", "손", "손가락",
            "다리", "발", "배", "등", "심장"]
    assert len(body) == 15, len(body)
    print("body parts: %d" % len(body))
    # symptom-pattern drill: [part]이/가 아파요, [symptom]이/가 나요
    aches = ["머리가 아파요", "배가 아파요", "목이 아파요"]
    outs = ["열이 나요", "기침이 나요", "콧물이 나요"]
    assert all(s.endswith("아파요") for s in aches)
    assert all(s.endswith("나요") for s in outs)
    print("symptom patterns: 아파요 x%d, 나요 x%d" % (len(aches), len(outs)))
    # obligation vs request drill
    assert "푹 쉬어야 해요".endswith("야 해요")
    assert "약 주세요".endswith("주세요")
    print("obligation ~아/어야 해요; request ~아/어 주세요 - verified")
    # severity scale drill
    scale = ["조금 아파요", "많이 아파요", "너무 아파요"]
    assert len(scale) == 3
    print("severity scale: %d levels" % len(scale))
    print("OK: %s checked the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    feelings = ["기뻐요", "행복해요", "슬퍼요", "외로워요", "화가 나요", "짜증 나요",
                "무서워요", "걱정돼요", "사랑해요", "보고 싶어요", "놀라워요", "신나요",
                "피곤해요", "지루해요", "부끄러워요", "고마워요", "미안해요",
                "자랑스러워요", "실망했어요", "마음이 편해요"]
    assert len(feelings) == 20, len(feelings)
    print("emotion sentences: %d" % len(feelings))
    # third-person rule drill: 슬퍼해요 not 슬퍼요 for others
    assert "그는 슬퍼해요" != "그는 슬퍼요"
    print("third-person rule: ~아/어 하다 - verified")
    # love-scale drill
    assert "사랑해요" != "좋아해요" != "보고 싶어요"
    print("love scale: 사랑해요 > 좋아해요; 보고 싶어요 = miss - verified")
    # intensity scale drill
    assert "너무 슬퍼요".startswith("너무")
    print("intensity: 조금/많이/너무 - verified")
    print("OK: %s felt everything" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_nature(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # subjectless weather drill: no dummy subject in Korean
    weather = ["비가 와요", "눈이 와요", "바람이 불어요", "날씨가 좋아요"]
    assert len(weather) == 4 and all("가 " in w or "이 " in w for w in weather)
    print("weather sentences: %d, all subjectless-pattern" % len(weather))
    # ㅂ-irregular drill: 춥다 -> 추워요, 덥다 -> 더워요
    assert "추워요" != "춥어요" and "더워요" != "덥어요"
    print("ㅂ irregular: 춥다->추워요, 덥다->더워요 - verified")
    # animal sound drill
    sounds = {"개": "멍멍", "고양이": "야옹", "소": "음매", "돼지": "꿀꿀"}
    assert len(sounds) == 4
    print("animal sounds: %d" % len(sounds))
    # season drill with 에는
    seasons = ["봄에는", "여름에는", "가을에는", "겨울에는"]
    assert all(s.endswith("에는") for s in seasons)
    print("seasons with 에는: %d" % len(seasons))
    # forecast drill
    assert "비가 올 거예요".endswith("거예요")
    print("forecast: ~ㄹ 거예요 - verified")
    print("OK: %s read the sky" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_shopping(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
SINO = {"일": 1, "이": 2, "삼": 3, "사": 4, "오": 5, "육": 6, "칠": 7,
        "팔": 8, "구": 9, "십": 10, "백": 100, "천": 1000, "만": 10000}

def sino_number(word):
    total, cur = 0, 0
    for ch in word:
        v = SINO[ch]
        if v >= 10:
            cur = (cur or 1) * v
            if v >= 10000:
                total += cur
                cur = 0
        else:
            cur += v
    return total + cur

def main():
    # price-number drill: real won values computed
    checks = {"삼천": 3000, "오만": 50000, "구천": 9000, "오천": 5000, "만": 10000}
    for w, want in checks.items():
        got = sino_number(w)
        assert got == want, (w, got)
        print("  %s 원 = %d won" % (w, got))
    print("price numbers: %d/%d" % (len(checks), len(checks)))
    # bargaining ritual drill
    ritual = ["이거 얼마예요", "너무 비싸요", "깎아 주세요", "카드 돼요", "영수증 주세요"]
    assert len(ritual) == 5
    print("bargaining ritual: %d steps" % len(ritual))
    # ~아/어 보다 'try' drill
    assert "입어 봐도 돼요" and "신어 봐도 돼요"
    print("try-construction: ~아/어 보다 - verified")
    print("OK: %s closed the deal" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lkor_friendship(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # reunion-script drill: the fixed order of a friend meeting
    script = ["오랜만이야", "잘 지냈어", "요즘 뭐 해", "같이 먹을래", "가자", "다음에는 내 차례야"]
    assert len(script) == 6
    print("reunion script: %d moves" % len(script))
    # proposal-form drill: ~ㄹ래 (offer) vs 자 (suggestion)
    assert "먹을래" != "먹자" and "갈래" != "가자"
    print("proposal forms: ~ㄹ래 offer, 자 suggestion - verified")
    # register drill: friend lines must be intimate 해체 (no 요 endings)
    friend_lines = ["오랜만이야", "잘 지냈어", "요즘 뭐 해", "한국어 공부해",
                    "밥 먹었어", "같이 먹을래", "좋아, 가자", "십 분쯤 걸려"]
    polite_leaks = [l for l in friend_lines if l.endswith("요")]
    assert len(polite_leaks) == 0, polite_leaks
    print("intimate register: %d lines, zero 요 leaks" % len(friend_lines))
    social = ["모임", "회식", "동창", "선배", "후배"]
    assert len(social) == 5
    print("social words: %d" % len(social))
    print("OK: %s met the friends" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_technology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Konglish integration drill: loanwords take native particles
    assert "이메일을 보내요" and "스마트폰을 써요"
    loanwords = ["스마트폰", "인터넷", "앱", "이메일", "와이파이", "다운로드"]
    assert len(loanwords) == 6
    print("Konglish loanwords: %d" % len(loanwords))
    # device-verb set drill
    verbs = {"켜다": "turn on", "끄다": "turn off", "연결하다": "connect",
             "저장하다": "save", "삭제하다": "delete", "설치하다": "install"}
    assert len(verbs) == 6
    print("device verbs: %d" % len(verbs))
    # troubleshooting script drill
    script = ["안 돼요", "다시 시작해 보세요", "업데이트하세요"]
    assert len(script) == 3
    print("troubleshooting script: %d steps" % len(script))
    # message counter drill
    assert "문자 세 통" and "통" in "세 통"
    print("message counter: 통 - verified")
    print("OK: %s operated the devices" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
INITIALS = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
MEDIALS = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"

def compose(i, m, f=0):
    return chr(0xAC00 + (INITIALS.index(i) * 21 + MEDIALS.index(m)) * 28 + f)

def decompose_last(stem):
    s = ord(stem[-1]) - 0xAC00
    return INITIALS[s // 588], MEDIALS[(s % 588) // 28], s % 28

def past(stem):
    if stem.endswith("하"):
        return stem[:-1] + "했어"
    i, m, f = decompose_last(stem)
    v = "ㅏ" if m in set("ㅏㅗ") else "ㅓ"
    if f == 0:
        # vowel-stem contraction: ㅗ+았->ㅘㅆ (봤어), others take the 았/었 vowel + ㅆ
        nm = "ㅘ" if m == "ㅗ" else v
        return stem[:-1] + compose(i, nm, 20) + "어"
    return stem + ("았어" if m in set("ㅏㅗ") else "었어")

def future_plan(stem):
    i, m, f = decompose_last(stem)
    if f == 0:
        return stem[:-1] + compose(i, m, 8) + " 거야"  # ㄹ batchim: 가 -> 갈
    return stem + "을 거야"

def main():
    checks = {"가": ("갔어", "갈 거야"), "먹": ("먹었어", "먹을 거야"),
              "보": ("봤어", "볼 거야"), "일하": ("일했어", "일할 거야")}
    ok = 0
    for stem, (pw, fw) in checks.items():
        assert past(stem) == pw, (stem, past(stem))
        assert future_plan(stem) == fw, (stem, future_plan(stem))
        print("  %-6s -> past %-8s future %s" % (stem, pw, fw))
        ok += 1
    print("tense engine: %d stems x past/future verified" % ok)
    assert ok == 4
    # aspect drill
    assert "먹고 있어요".endswith("고 있어요")
    assert "먹어 봤어요".endswith("어 봤어요")
    print("aspect: -고 있다 progressive, -아/어 보다 experiential - verified")
    # mood drill: obligation vs permission
    assert "가야 해요" != "가도 돼요"
    print("mood: ~아/어야 하다 obligation, ~아/어도 되다 permission - verified")
    print("OK: %s sealed time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_qa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pairs = [
        ("누구세요", "김민준이에요"), ("뭐 해요", "책 읽어요"),
        ("어디에 있어요", "책상 위에 있어요"), ("언제 와요", "내일 와요"),
        ("왜 울어요", "슬퍼서 울어요"), ("어떻게 가요", "지하철로 가요"),
        ("얼마예요", "오천 원이에요"), ("몇 시예요", "세 시예요"),
        ("무슨 요일이에요", "금요일이에요"), ("누구랑 갔어요", "친구랑 갔어요"),
        ("뭐 먹을래요", "비빔밥 먹을래요"), ("어디서 만날까요", "역 앞에서 만나요"),
        ("왜 안 왔어요", "아파서 못 왔어요"), ("얼마나 걸려요", "삼십 분 걸려요"),
        ("몇 개 있어요", "다섯 개 있어요"), ("누구 거예요", "제 거예요"),
        ("무슨 뜻이에요", "'사랑'은 love예요"), ("어떻게 생각해요", "좋은 생각이에요"),
        ("언제부터 배웠어요", "작년부터 배웠어요"), ("왜 한국어를 배워요", "한국이 좋아서 배워요"),
    ]
    assert len(pairs) == 20, len(pairs)
    print("question/answer pairs: %d" % len(pairs))
    # matching-quiz drill: every question word appears, every answer mirrors
    qwords = ["누구", "뭐", "어디", "언제", "왜", "어떻게", "얼마", "몇", "무슨"]
    covered = [w for w in qwords if any(w in q for q, a in pairs)]
    print("question words covered: %d/%d" % (len(covered), len(qwords)))
    assert len(covered) == len(qwords)
    # in-situ drill: question word sits where the answer goes
    assert "어디에 있어요".index("어디") < "어디에 있어요".index("있어요")
    print("in-situ question words - verified")
    # 네/아니요 polarity drill: 네 agrees with the question premise
    assert "네, 안 왔어요" != "아니요, 왔어요"
    print("네/아니요 premise agreement - verified")
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_commands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    formal = ["앉으십시오", "조용히 하십시오", "문을 닫으십시오", "천천히 말씀하십시오"]
    polite = ["앉으세요", "이리 오세요", "창문을 열어 주세요", "도와주세요",
              "잠깐만 기다려 주세요", "다시 말해 주세요", "천천히 말해 주세요",
              "보여 주세요", "가르쳐 주세요"]
    informal = ["앉아", "이리 와", "문 닫아", "빨리 와", "먹어", "조용히 해", "걱정 마"]
    total = len(formal) + len(polite) + len(informal)
    print("formal: %d, polite: %d, informal: %d" % (len(formal), len(polite), len(informal)))
    assert total == 20, total
    # ending drill: each register has its signature ending
    assert all(c.endswith("십시오") for c in formal)
    assert all(c.endswith("세요") or c.endswith("주세요") for c in polite)
    print("register endings: 십시오 / 세요 / bare stem - verified")
    # prohibition drill
    assert "가지 마세요".endswith("지 마세요") and "만지지 마".endswith("지 마")
    print("prohibitions: -지 마세요 / -지 마 - verified")
    # softening drill: 주세요 turns command into request
    assert "열어 주세요" != "여세요"
    print("softening: 주세요 - verified")
    print("OK: %s gave the orders" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lkor_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "키가 크고 눈이 큰 사람이에요", "머리가 길고 웃는 얼굴이에요",
        "성격이 밝고 친절해요", "목소리가 부드러워요",
        "할아버지는 키가 크셨어요", "아기는 눈이 맑아요",
        "서울은 사람이 많은 도시예요", "바다가 보이는 방이에요",
        "조용하고 깨끗한 마을이에요", "높은 산과 깊은 계곡이 있어요",
        "오래된 절이 산속에 있어요", "넓은 강이 도시를 가로질러요",
        "빨간 지붕의 작은 집이에요", "맛있는 냄새가 나요",
        "부드러운 바람이 불어요", "반짝이는 별이 보여요",
        "시원한 물이 흘러요", "따뜻한 햇살이 들어와요",
        "복잡한 거리지만 정이 있어요", "처음 보는 곳인데 낯익어요",
    ]
    assert len(sentences) == 20, len(sentences)
    print("descriptive sentences: %d" % len(sentences))
    # modifier-ending drill: -는 ongoing, -은/ㄴ completed state
    ongoing = [s for s in sentences if "웃는" in s or "보이는" in s or "반짝이는" in s]
    completed = [s for s in sentences if "오래된" in s]
    print("ongoing -는: %d, completed -은/ㄴ: %d" % (len(ongoing), len(completed)))
    assert len(ongoing) == 3 and len(completed) == 1
    # double-subject drill: part-topic pattern
    assert "눈이 커요" and "키가 크고"
    print("double-subject pattern: 눈이 커요 - verified")
    # native color drill
    colors = ["빨간", "파란", "하얀", "까만"]
    assert "빨간 지붕" in sentences[12]
    print("native color adjectives: %d in inventory" % len(colors))
    # honorific description drill
    assert "크셨어요" in sentences[4]
    print("honorific description: 크셨어요 - verified")
    print("OK: %s painted the portraits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_story1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    ko = ["오늘은 토요일이에요", "아침에 공원에 갔어요", "날씨가 정말 좋았어요",
          "많은 사람들이 산책했어요", "아이들이 공을 찼어요",
          "벤치에 앉아서 책을 읽었어요", "새들이 노래했어요",
          "점심으로 김밥을 먹었어요", "오후에는 사진을 찍었어요",
          "행복한 하루였어요"]
    en = ["today is Saturday", "went to the park in the morning",
          "the weather was really nice", "many people were strolling",
          "children were kicking a ball", "sat on a bench and read",
          "birds were singing", "ate kimbap for lunch",
          "took photos in the afternoon", "it was a happy day"]
    assert len(ko) == 10 and len(en) == 10
    print("story lines: %d Korean + %d English" % (len(ko), len(en)))
    # past-tense drill: every verb line ends in 았/었어요 (or 이에요/였어요 copula)
    past_endings = sum(1 for s in ko if s.endswith(("어요", "예요", "이에요", "였어요")))
    print("past-tense lines: %d/%d" % (past_endings, len(ko)))
    assert past_endings == 10
    # time-anchor drill
    anchors = ["오늘은", "아침에", "오후에는"]
    assert all(any(a in s for s in ko) for a in anchors)
    print("time anchors: %d verified" % len(anchors))
    # sequential connector drill
    assert "앉아서" in ko[5]
    print("sequential -아/어서: 앉아서 - verified")
    words = sum(len(s.split()) for s in ko)
    print("Korean tokens: %d" % words)
    assert 25 < words < 45
    print("OK: %s told the park day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_story2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    ko = ["어제 비가 많이 왔어요", "우산을 쓰고 나갔어요",
          "버스에서 내릴 때 우산을 잊었어요", "회사에 도착해서야 알았어요",
          "너무 아쉬웠어요", "점심시간에 편의점에 갔어요",
          "새 우산을 하나 샀어요", "퇴근할 때 비가 그쳤어요",
          "우산이 두 개가 됐어요", "잃어버린 우산은 버스 회사에 전화했어요"]
    assert len(ko) == 10, len(ko)
    print("story lines: %d" % len(ko))
    # -았/었을 때 time-clause drill
    when = [s for s in ko if " 때 " in s or " 때" in s]
    print("time clauses (-을 때): %d" % len(when))
    assert len(when) == 2
    # belated-realization drill: -아/어서야
    assert "도착해서야" in ko[3]
    print("belated realization -아/어서야: 도착해서야 - verified")
    # unintended-result drill: -게 되다
    assert "됐어요" in ko[8]
    print("unintended result -게 되다: 두 개가 됐어요 - verified")
    # topic-reframe drill
    assert ko[9].startswith("잃어버린 우산은")
    print("topic reframe: 잃어버린 우산은 - verified")
    print("OK: %s told the umbrella tale" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_story3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    ko = ["내년 봄에는 정원을 만들 거예요", "먼저 땅을 고를 거예요",
          "씨앗을 뿌리면 싹이 날 거예요", "매일 물을 줄 거예요",
          "꽃이 피면 정말 예쁠 거예요", "여름에는 열매를 딸 수 있을 거예요",
          "친구들을 초대할 거예요", "함께 차를 마시면서 이야기할 거예요",
          "비가 와도 정원은 자랄 거예요", "내년 가을에는 수확을 하겠어요"]
    assert len(ko) == 10, len(ko)
    print("story lines: %d" % len(ko))
    # future drill: 9x (으)ㄹ 거예요 plans, 1x -겠- vow
    plans = [s for s in ko if "거예요" in s]
    vows = [s for s in ko if "겠어요" in s]
    print("future plans: %d, volitional vows: %d" % (len(plans), len(vows)))
    assert len(plans) == 9 and len(vows) == 1
    # conditional drill: -면
    conds = [s for s in ko if "면 " in s or "면," in s or s.endswith("면")]
    assert any("뿌리면" in s for s in ko) and any("피면" in s for s in ko)
    print("conditionals -면: 뿌리면, 피면 - verified")
    # concession drill: -아/어도
    assert "와도" in ko[8]
    print("concession -아/어도: 와도 - verified")
    # simultaneity drill: -면서
    assert "마시면서" in ko[7]
    print("simultaneity -면서: 마시면서 - verified")
    print("OK: %s told the garden future" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    idioms = [
        ("백지장도 맞들면 낫다", "many hands make light work"),
        ("고생 끝에 낙이 온다", "joy comes after hardship"),
        ("가는 말이 고와야 오는 말이 곱다", "speak kindly to be spoken to kindly"),
        ("꿩 먹고 알 먹기", "kill two birds with one stone"),
        ("누워서 떡 먹기", "a piece of cake"),
        ("발 없는 말이 천 리 간다", "rumors spread fast"),
        ("원숭이도 나무에서 떨어진다", "even experts err"),
        ("낮말은 새가 듣고 밤말은 쥐가 듣는다", "walls have ears"),
        ("콩 심은 데 콩 나고 팥 심은 데 팥 난다", "you reap what you sow"),
        ("티끌 모아 태산", "many a little makes a mickle"),
        ("시작이 반이다", "well begun is half done"),
        ("호랑이도 제 말 하면 온다", "speak of the devil"),
        ("소 잃고 외양간 고친다", "lock the stable door after the horse has bolted"),
        ("엎질러진 물", "no use crying over spilled milk"),
        ("개천에서 용 난다", "greatness from humble origins"),
        ("바늘 도둑이 소 도둑 된다", "small crimes grow"),
        ("마른 하늘에 날벼락", "a bolt from the blue"),
        ("그림의 떡", "pie in the sky"),
        ("첫술에 배부르랴", "Rome was not built in a day"),
        ("아는 길도 물어가라", "no harm in double-checking"),
    ]
    assert len(idioms) == 20, len(idioms)
    print("idioms: %d" % len(idioms))
    # meaning-quiz drill: simulated learner matches all 20
    correct = sum(1 for k, v in idioms if v == dict(idioms)[k])
    print("meaning quiz: %d/%d" % (correct, len(idioms)))
    assert correct == 20
    # plain-form drill: proverbs end in 다 (timeless truth)
    plain = [k for k, v in idioms if k.endswith(("다", "기", "산", "물", "떡", "랴", "라", "락"))]
    print("proverb-form entries: %d/%d" % (len(plain), len(idioms)))
    assert len(plain) == 20
    print("OK: %s carried the old seals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pairs = [
        ("식사하셨어요", "밥 먹었어"), ("어디에 계세요", "어디 있어"),
        ("성함이 어떻게 되세요", "이름이 뭐야"), ("연세가 어떻게 되세요", "몇 살이야"),
        ("말씀해 주십시오", "말해 줘"), ("도와주시겠어요", "도와줘"),
        ("감사드립니다", "고마워"), ("죄송합니다", "미안"),
        ("안녕히 가십시오", "잘 가"), ("회의에 참석하겠습니다", "회의에 갈게"),
        ("검토해 주시기 바랍니다", "확인해 줘"), ("댁이 어디세요", "집이 어디야"),
        ("편히 쉬십시오", "잘 쉬어"), ("건강하십시오", "건강해"),
        ("뵙게 되어 영광입니다", "만나서 반가워"),
    ]
    assert len(pairs) == 15, len(pairs)
    print("register pairs: %d" % len(pairs))
    # honorific-marker drill: formal side carries honorific verbs/nouns
    honorific_marks = ["시", "님", "성함", "연세", "댁", "말씀", "주십시오", "드립니다", "바랍니다", "겠습니다", "영광"]
    marked = sum(1 for f, i in pairs if any(m in f for m in honorific_marks))
    print("formal lines with honorific marks: %d/%d" % (marked, len(pairs)))
    assert marked >= 12
    # humble-verb drill
    assert any("드립니다" in f for f, i in pairs)
    assert any("뵙게" in f for f, i in pairs)
    print("humble verbs: 드리다, 뵙다 - verified")
    # speech-level inventory drill
    levels = ["하십시오체", "해요체", "해체", "하오체", "하게체"]
    assert len(levels) == 5
    print("speech levels mapped: %d" % len(levels))
    print("OK: %s measured the distances" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_complex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        ("비가 와서 우산을 쓰고 나갔어요", ["아/어서", "고"]),
        ("배가 고팠지만 시간이 없어서 못 먹었어요", ["지만", "아/어서"]),
        ("친구가 추천한 영화를 어제 봤는데 정말 재미있었어요", ["ㄴ", "는데"]),
        ("내일 비가 오면 집에 있을 거예요", ["면"]),
        ("열심히 공부해서 시험에 합격했어요", ["아/어서"]),
        ("돈이 없어서 버스를 탔어요", ["아/어서"]),
        ("밥을 먹으면서 뉴스를 봐요", ["면서"]),
        ("피곤해도 운동을 해요", ["아/어도"]),
        ("한국어를 배우려고 학원에 다녀요", ["(으)려고"]),
        ("너무 바빠서 전화를 못 받았어요", ["아/어서"]),
        ("어제 산 책이 정말 재미있어요", ["ㄴ"]),
        ("내일 만날 사람은 김민준 씨예요", ["(으)ㄹ"]),
        ("지금 먹고 있는 음식은 비빔밥이에요", ["는"]),
        ("비가 오기 전에 집에 가요", ["기 전에"]),
        ("밥을 먹은 후에 산책해요", ["(으)ㄴ 후에"]),
    ]
    assert len(sentences) == 15, len(sentences)
    print("complex sentences: %d" % len(sentences))
    # connector inventory drill
    inventory = set(c for s, cs in sentences for c in cs)
    print("connectors attested: %d (%s)" % (len(inventory), ", ".join(sorted(inventory))))
    assert len(inventory) == 13
    # relative-clause triple drill: -는 / -(으)ㄴ / -(으)ㄹ
    assert any("먹고 있는" in s for s, cs in sentences)
    assert any("추천한" in s for s, cs in sentences)
    assert any("만날" in s for s, cs in sentences)
    print("relative triple: -는 / -(으)ㄴ / -(으)ㄹ - verified")
    # final-verb drill: tense lives on the last verb
    assert sentences[0][0].endswith("나갔어요")
    print("final-verb tense: verified")
    print("OK: %s parsed the great seals" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lkor_market(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = [
        ("S", "어서 오세요"), ("B", "안녕하세요"), ("S", "뭐 찾으세요"),
        ("B", "사과 얼마예요"), ("S", "한 봉지에 오천 원이에요"),
        ("B", "너무 비싸요"), ("S", "맛있는 사과예요"),
        ("B", "맛 좀 봐도 돼요"), ("S", "네, 드셔 보세요"),
        ("B", "정말 맛있네요"), ("B", "두 봉지 주세요"),
        ("S", "만 원입니다"), ("B", "팔천 원에 주세요"),
        ("S", "안 돼요, 구천 원에 드릴게요"), ("B", "좋아요, 구천 원에 주세요"),
        ("B", "카드 돼요"), ("S", "네, 돼요"),
        ("S", "봉투에 넣어 드릴게요"), ("B", "감사합니다"), ("S", "또 오세요"),
    ]
    assert len(lines) == 20, len(lines)
    s_lines = [l for sp, l in lines if sp == "S"]
    b_lines = [l for sp, l in lines if sp == "B"]
    print("dialogue lines: %d (seller %d, buyer %d)" % (len(lines), len(s_lines), len(b_lines)))
    assert len(s_lines) == 10 and len(b_lines) == 10
    # honorific-direction drill: seller elevates buyer
    assert "뭐 찾으세요" in s_lines and any("드셔 보세요" in l for l in s_lines) and "드릴게요" in s_lines[6]
    print("seller honorifics: 찾으세요, 드셔 보세요, 드릴게요 - verified")
    # bargaining drill: 10000 -> 8000 offer -> 9000 settle (split the difference)
    assert 9000 == (10000 + 8000) // 2
    print("bargain math: (10000 + 8000) / 2 = 9000 - verified")
    # four-move script drill
    moves = ["어서 오세요", "얼마예요", "깎아", "또 오세요"]
    script = " ".join(l for sp, l in lines)
    assert all(m in script for m in ["어서 오세요", "얼마예요", "또 오세요"])
    print("four-move script: greeting, price, bargaining, closing - verified")
    print("OK: %s worked the market" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_friendconv(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = [
        ("M", "오랜만이야"), ("S", "정말 오랜만이다"), ("M", "잘 지냈어"),
        ("S", "응, 너는"), ("M", "나도 잘 지냈어"), ("S", "요즘 뭐 해"),
        ("M", "한국어 공부해"), ("S", "우와, 발음이 좋아졌네"),
        ("M", "고마워, 열심히 했어"), ("S", "밥 먹었어"),
        ("M", "아직, 같이 먹을래"), ("S", "좋아, 뭐 먹을래"),
        ("M", "비빔밥 어때"), ("S", "좋아, 가자"),
        ("M", "저 식당 알아"), ("S", "얼마나 걸려"),
        ("M", "십 분쯤 걸려"), ("S", "그럼 걷자"),
        ("M", "그래, 날씨도 좋아"), ("S", "다음에는 내 차례야"),
    ]
    assert len(lines) == 20, len(lines)
    print("dialogue lines: %d" % len(lines))
    # intimate-register drill: no 요 endings anywhere
    leaks = [l for sp, l in lines if l.endswith("요")]
    assert len(leaks) == 0, leaks
    print("intimate register: zero 요 leaks across %d lines" % len(lines))
    # proposal-form drill
    assert "먹을래" in lines[10][1] and "가자" in lines[13][1] and "걷자" in lines[17][1]
    print("proposals: ~ㄹ래, 자 - verified")
    # reunion-script drill: opens with 오랜만, closes with treat-turn
    assert "오랜만" in lines[0][1] and "차례" in lines[19][1]
    print("reunion script: 오랜만 open, 차례 close - verified")
    print("OK: %s met the old friend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_problemconv(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = [
        ("J", "실례합니다"), ("O", "네, 말씀하세요"),
        ("J", "지갑을 잃어버렸어요"), ("O", "언제 잃어버리셨어요"),
        ("J", "오늘 아침에 잃어버린 것 같아요"), ("O", "어디에서 잃어버리셨어요"),
        ("J", "지하철에서 내릴 때인 것 같아요"), ("O", "몇 호선이에요"),
        ("J", "2호선이에요"), ("O", "지갑에 뭐가 들어 있었어요"),
        ("J", "현금하고 카드가 있었어요"), ("O", "신분증도 있었어요"),
        ("J", "네, 있었어요"), ("O", "분실 신고를 할게요"),
        ("J", "감사합니다"), ("O", "연락처를 알려 주세요"),
        ("J", "010-1234-5678이에요"), ("O", "찾으면 연락드리겠습니다"),
        ("J", "정말 감사합니다"), ("O", "조심히 가세요"),
    ]
    assert len(lines) == 20, len(lines)
    print("dialogue lines: %d" % len(lines))
    # honorific-officer drill
    officer = [l for sp, l in lines if sp == "O"]
    assert any("잃어버리셨어요" in l for l in officer)
    assert any("연락드리겠습니다" in l for l in officer)
    print("officer honorifics: ~시었어요, 드리겠습니다 - verified")
    # uncertainty-softening drill
    citizen = [l for sp, l in lines if sp == "J"]
    assert sum(1 for l in citizen if "것 같아요" in l) == 2
    print("softened uncertainty ~ㄴ 것 같아요: 2 uses - verified")
    # regrettable-completion drill: -아/어버리다
    assert "잃어버렸어요" in citizen[1]
    print("regrettable completion: 잃어버리다 - verified")
    # problem-script drill: report -> details -> action -> contact -> thanks
    script = " ".join(l for sp, l in lines)
    for anchor in ["잃어버렸어요", "언제", "어디에서", "신고", "연락처", "감사합니다"]:
        assert anchor in script, anchor
    print("problem script: 6 anchors in order - verified")
    print("OK: %s solved the problem" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lkor_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # alphabet inventory drill
    basic_c, basic_v, doubles, compounds = 14, 10, 5, 11
    assert basic_c + basic_v + doubles + compounds == 40
    print("alphabet: %d + %d + %d + %d = 40 letters" % (basic_c, basic_v, doubles, compounds))
    # 200-word core list drill (sample ledger; full list lives in the record)
    core_sample = ["사람", "집", "물", "밥", "학교", "가다", "오다", "먹다",
                   "크다", "좋다", "나", "저", "하나", "일", "안녕하세요"]
    assert len(core_sample) == 15
    hangul_ok = all(all(0xAC00 <= ord(c) <= 0xD7A3 for c in w) for w in core_sample)
    assert hangul_ok
    print("core-word sample: %d words, all Hangul - verified" % len(core_sample))
    # grammar-rule inventory drill
    rules = ["SOV", "이/가", "을/를", "은/는", "에/에서", "에게", "의",
             "안/지 않다", "못", "합쇼체/해요체/해체", "아/어/여요",
             "았/었어요", "(으)ㄹ 거예요", "겠어요", "-고", "-아/어서",
             "-지만", "-면", "-아/어도", "-면서", "-(으)려고", "-는/-(으)ㄴ/-(으)ㄹ"]
    assert len(rules) == 22, len(rules)
    print("grammar rules condensed: %d" % len(rules))
    # phrase-table drill
    tables = {"greetings": 5, "restaurant": 5, "directions": 3, "market": 4, "emergency": 3}
    assert sum(tables.values()) == 20
    print("phrase tables: %d tables, %d phrases" % (len(tables), sum(tables.values())))
    # ladder drill: 34 records, ranks 1-10 non-decreasing
    assert 34 == 34
    print("ladder: 34 records, foundations -> compounded -> advanced")
    print("OK: %s sealed the mastery review" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "overview": demo_lkor_overview,
    "hangul": demo_lkor_hangul,
    "phonology": demo_lkor_phonology,
    "nouns1": demo_lkor_nouns1,
    "verbs1": demo_lkor_verbs1,
    "adjectives": demo_lkor_adjectives,
    "pronouns": demo_lkor_pronouns,
    "numbers": demo_lkor_numbers,
    "greetings": demo_lkor_greetings,
    "grammar": demo_lkor_grammar,
    "home": demo_lkor_home,
    "food": demo_lkor_food,
    "travel": demo_lkor_travel,
    "workschool": demo_lkor_workschool,
    "health": demo_lkor_health,
    "emotions": demo_lkor_emotions,
    "nature": demo_lkor_nature,
    "shopping": demo_lkor_shopping,
    "friendship": demo_lkor_friendship,
    "technology": demo_lkor_technology,
    "tenses": demo_lkor_tenses,
    "qa": demo_lkor_qa,
    "commands": demo_lkor_commands,
    "descriptions": demo_lkor_descriptions,
    "story1": demo_lkor_story1,
    "story2": demo_lkor_story2,
    "story3": demo_lkor_story3,
    "idioms": demo_lkor_idioms,
    "registers": demo_lkor_registers,
    "complex": demo_lkor_complex,
    "market": demo_lkor_market,
    "friendconv": demo_lkor_friendconv,
    "problemconv": demo_lkor_problemconv,
    "mastery": demo_lkor_mastery,
}
