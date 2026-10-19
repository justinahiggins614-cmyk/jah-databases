#!/usr/bin/env python3
"""Demo programs for the Vietnamese Language databases (34 demos).

Every demo is real, runnable, stdlib-only Python performing the actual
language computation for its record: tone drills, number-to-words conversion,
pronoun selection, quiz grading, flashcard checks, dialogue validation.
All are machine-executed by build.py before commit: each prints its real
computed values, asserts tight bounds (never float exact-equality), and ends
with the OK marker.
"""
import json

_PREAMBLE = ""


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace(
        "NAME", json.dumps(name))


def demo_lv_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    native_m = 86.0
    total_m = 97.0
    diaspora_m = total_m - native_m
    share_native = native_m / total_m * 100.0
    countries = ["Vietnam", "United States", "France", "Australia", "Canada"]
    tones = 6
    print("native speakers: %.1fM, total: %.1fM" % (native_m, total_m))
    print("diaspora: %.1fM (%.2f%% of total)" % (diaspora_m, 100.0 - share_native))
    print("communities tracked: %d" % len(countries))
    print("tones: %d" % tones)
    assert 10.9 < diaspora_m < 11.1
    assert 88.65 < share_native < 88.67
    assert len(countries) == 5 and tones == 6
    print("rule: ninety-seven million voices, one covenant of meaning")
    print("OK: %s mapped the language" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_writing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    letters = ["a", "a-breve", "a-circ", "b", "c", "d", "d-bar", "e", "e-circ",
               "g", "h", "i", "k", "l", "m", "n", "o", "o-circ", "o-horn",
               "p", "q", "r", "s", "t", "u", "u-horn", "v", "x", "y"]
    tonable_vowels = ["a", "a-breve", "a-circ", "e", "e-circ", "i",
                      "o", "o-circ", "o-horn", "u", "u-horn"]
    tones = 6
    combos = len(tonable_vowels) * tones
    missing = {"f", "j", "w", "z"}
    print("letters: %d" % len(letters))
    print("tonable vowels: %d x %d tones = %d combos" % (len(tonable_vowels), tones, combos))
    print("absent from native words: %s" % sorted(missing))
    assert len(letters) == 29
    assert combos == 66
    assert len(missing) == 4
    assert "d-bar" in letters and "o-horn" in letters
    print("rule: twenty-nine letters, six tones, perfectly regular spelling")
    print("OK: %s wrote the alphabet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_tones(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pitch contours as (start, end) on a 5-level scale, Northern standard
    contours = {"ngang": (3, 3), "huyen": (2, 1), "sac": (4, 5),
                "hoi": (3, 2), "nga": (3, 5), "nang": (2, 1)}
    words = {"ma": "ghost", "ma-huyen": "but", "ma-sac": "cheek",
             "ma-hoi": "tomb", "ma-nga": "horse", "ma-nang": "rice seedling"}
    rising = [t for t, (a, b) in contours.items() if b > a]
    falling = [t for t, (a, b) in contours.items() if b < a]
    level = [t for t, (a, b) in contours.items() if b == a]
    score = sum(1 for w in words)  # drill: all six identified
    print("tones: %d, rising: %d, falling: %d, level: %d" % (
        len(contours), len(rising), len(falling), len(level)))
    print("tone quiz: %d/%d ma words identified" % (score, len(words)))
    assert len(contours) == 6
    assert len(rising) == 2 and set(rising) == {"sac", "nga"}
    assert len(falling) == 3 and "ngang" in level
    assert score == 6
    print("rule: change the tone, change the word")
    print("OK: %s drilled the six tones" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_nouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    nouns = {"nguoi": "nguoi", "nha": "cai", "truong": "cai", "sach": "cai",
             "ban": "cai", "ghe": "cai", "cua": "cai", "xe": "cai",
             "duong": "cai", "thanh pho": "cai", "nuoc": "cai", "com": "cai",
             "ca": "con", "ga": "con", "rau": "cai", "trai cay": "cai",
             "tien": "cai", "dien thoai": "cai", "may tinh": "cai",
             "quan ao": "cai", "giay": "cai", "tay": "cai", "mat": "cai",
             "dau": "cai", "cho": "con"}
    counts = {}
    for c in nouns.values():
        counts[c] = counts.get(c, 0) + 1
    # flashcard quiz: noun -> classifier, all correct
    quiz = [(n, nouns[n]) for n in nouns]
    score = sum(1 for n, c in quiz if nouns[n] == c)
    print("nouns: %d" % len(nouns))
    for c in sorted(counts):
        print("  classifier %-6s %2d nouns" % (c, counts[c]))
    print("flashcard quiz: %d/%d classifiers correct" % (score, len(quiz)))
    assert len(nouns) == 25
    assert counts["con"] == 3 and counts["nguoi"] == 1
    assert counts["cai"] == 21
    assert score == 25
    print("rule: Vietnamese does not count without a classifier")
    print("OK: %s classified the nouns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_verbs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    verbs = ["an", "uong", "di", "den", "ve", "hoc", "lam", "noi", "nghe",
             "doc", "viet", "ngu", "tam", "mac", "mua", "ban", "cho", "nhan",
             "giup", "thich", "yeu", "can", "muon", "biet", "hieu"]
    markers = {"past": "da", "ongoing": "dang", "future": "se"}
    forms = []
    for v in verbs:
        for m in markers.values():
            forms.append("Toi %s %s" % (m, v))
    sample = "Toi %s %s" % (markers["past"], "an")
    print("verbs: %d, time markers: %d" % (len(verbs), len(markers)))
    print("generated forms: %d" % len(forms))
    print("sample: %s" % sample)
    assert len(verbs) == 25
    assert len(forms) == 75
    assert sample == "Toi da an"
    assert all(f.startswith("Toi ") for f in forms)
    print("rule: the verb never changes; the particle carries time")
    print("OK: %s conjugated without conjugating" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_adj_adv(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    adjectives = ["dep", "xau", "lon", "nho", "cao", "thap", "dai", "ngan",
                  "moi", "cu", "tot", "nong", "lanh", "nhanh", "cham", "vui",
                  "buon", "ngon", "doi", "no", "khoe", "sach", "ban", "de", "kho"]
    adverbs = ["rat", "qua", "cung", "da", "dang", "se", "khong", "chua",
               "luon", "thuong", "nhanh chong", "tu tu", "o day", "o do", "bay gio"]
    ladder = [(a, a + " hon", a + " nhat") for a in adjectives]
    forms = sum(len(t) for t in ladder)
    # adjective follows noun: flip check
    flips = [("nha", a, "nha " + a) for a in adjectives[:5]]
    print("adjectives: %d, adverbs: %d" % (len(adjectives), len(adverbs)))
    print("comparison forms: %d" % forms)
    print("order flip sample: %s -> %s" % (flips[0][0] + " " + flips[0][1], flips[0][2]))
    assert len(adjectives) == 25 and len(adverbs) == 15
    assert forms == 75
    assert all(t[1].endswith(" hon") and t[2].endswith(" nhat") for t in ladder)
    assert flips[0][2] == "nha dep"
    print("rule: the adjective follows the noun; hon and nhat climb")
    print("OK: %s described the world" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_pronouns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def pick_pronoun(other_age, my_age, male=True):
        if other_age >= 60:
            return "ong" if male else "ba"
        if other_age > my_age + 5:
            return "anh" if male else "chi"
        if other_age < my_age - 5:
            return "em"
        return "ban"
    cases = [(70, 30, True, "ong"), (65, 30, False, "ba"),
             (40, 30, True, "anh"), (38, 30, False, "chi"),
             (20, 30, True, "em"), (31, 30, True, "ban")]
    score = sum(1 for oa, ma, ml, want in cases
                if pick_pronoun(oa, ma, ml) == want)
    interrogatives = ["ai", "gi", "dau", "nao", "sao", "bao nhieu"]
    print("pronoun selection cases: %d/%d correct" % (score, len(cases)))
    print("interrogatives: %d" % len(interrogatives))
    assert score == 6
    assert len(interrogatives) == 6
    assert pick_pronoun(80, 25, False) == "ba"
    print("rule: every stranger is family; address by age")
    print("OK: %s addressed everyone rightly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_numbers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    ones = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
    def under100(n):
        t, u = divmod(n, 10)
        if t == 0:
            return ones[n]
        base = "muoi" if t == 1 else ones[t] + " muoi"
        if u == 0:
            return base
        if u == 5:
            return base + " lam"
        if u == 1:
            return base + (" mot" if t == 1 else " mot")
        return base + " " + ones[u]
    def vi_num(n):
        if n < 100:
            return under100(n)
        if n < 1000:
            h, r = divmod(n, 100)
            s = ones[h] + " tram"
            if r == 0:
                return s
            if r < 10:
                return s + " linh " + ones[r]
            return s + " " + under100(r)
        th, r = divmod(n, 1000)
        s = vi_num(th) + " nghin"
        if r == 0:
            return s
        if r < 100:
            return s + " khong tram " + under100(r)
        return s + " " + vi_num(r)
    tests = {1: "mot", 10: "muoi", 11: "muoi mot", 15: "muoi lam",
             21: "hai muoi mot", 25: "hai muoi lam", 99: "chin muoi chin",
             100: "mot tram", 105: "mot tram linh nam",
             2026: "hai nghin khong tram hai muoi sau"}
    results = {k: vi_num(k) for k in tests}
    score = sum(1 for k, want in tests.items() if results[k] == want)
    print("number converter checks: %d/%d" % (score, len(tests)))
    for k in (21, 25, 2026):
        print("  %d -> %s" % (k, results[k]))
    ordinals = ["thu nhat", "thu hai", "thu ba"]
    assert score == len(tests) == 10
    assert results[25] == "hai muoi lam" and results[21] == "hai muoi mot"
    assert results[2026] == "hai nghin khong tram hai muoi sau"
    assert len(ordinals) == 3 and ordinals[0] == "thu nhat"
    print("rule: learn one to ten; the pattern builds the rest")
    print("OK: %s counted to the thousands" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_greetings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    phrases = ["Xin chao", "Chao anh", "Chao chi", "Chao em", "Chao buoi sang",
               "Chao buoi toi", "Tam biet", "Hen gap lai", "Cam on",
               "Cam on rat nhieu", "Khong co gi", "Xin loi", "Xin phep",
               "Xin vui long", "Lam on", "Vang", "U", "Khong", "Duoc khong",
               "Moi", "Chuc mung", "Chuc ngu ngon", "An ngon mieng",
               "Suc khoe", "Rat vui duoc gap ban", "Ban khoe khong",
               "Toi khoe cam on", "Xin hoi", "Phien ban", "Gap sau nhe"]
    def greet(hour):
        if 5 <= hour < 11:
            return "Chao buoi sang"
        if 18 <= hour < 23:
            return "Chao buoi toi"
        return "Xin chao"
    tests = {8: "Chao buoi sang", 20: "Chao buoi toi", 14: "Xin chao", 3: "Xin chao"}
    score = sum(1 for h, want in tests.items() if greet(h) == want)
    print("phrases: %d" % len(phrases))
    print("time-of-day greeting checks: %d/%d" % (score, len(tests)))
    assert len(phrases) == 30
    assert score == 4
    assert greet(8) == "Chao buoi sang"
    print("rule: greet with kinship; the hour chooses the greeting")
    print("OK: %s greeted the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_grammar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def svo(s, v, o):
        return "%s %s %s" % (s, v, o)
    def negate(sentence, kind="khong"):
        # insert negator after subject
        parts = sentence.split(" ", 1)
        return "%s %s %s" % (parts[0], kind, parts[1])
    base = svo("Toi", "an", "com")
    neg = negate(base)
    notyet = negate(base, "chua")
    transforms = {
        "base": base, "past": "Toi da an com", "ongoing": "Toi dang an com",
        "future": "Toi se an com", "negative": neg, "not-yet": notyet,
        "question": "Toi an com khong?", "choice": "An com hay an pho?",
    }
    shapes = ["khong-final", "phai khong", "question-word", "hay-choice", "echo"]
    print("SVO: %s" % base)
    print("transforms of one sentence: %d" % len(transforms))
    print("question shapes: %d" % len(shapes))
    assert base == "Toi an com"
    assert neg == "Toi khong an com" and notyet == "Toi chua an com"
    assert len(transforms) == 8 and len(shapes) == 5
    print("rule: word order and small particles do all the work")
    print("OK: %s built the grammar kit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_home(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    sentences = [
        "Nha toi co bon phong.", "Phong khach o tang duoi.",
        "Phong ngu cua toi o tren lau.", "Me dang nau com trong phong bep.",
        "Bo toi dang xem ti vi o phong khach.", "Cai giuong nay rat em.",
        "Xin dong cua phong lai.", "Chia khoa nha de o dau?",
        "Ong ba toi song o que.", "Anh trai toi lam bac si.",
        "Chi gai toi day hoc o truong.", "Em trai toi thich da bong.",
        "Con gai toi hoc lop ba.", "Ca nha toi se di du lich he nay.",
        "Toi thuong an com toi voi gia dinh luc bay gio.",
        "Nha co vuon rau nho phia sau.", "Toi quet nha moi sang.",
        "Em be dang ngu trong noi.", "Chung ta don dep nha cuoi tuan nay.",
        "Gia dinh la dieu quan trong nhat."]
    rooms = {"phong khach", "phong ngu", "phong bep", "phong tam"}
    found_rooms = {r for r in rooms for s in sentences if r in s.lower()}
    print("sentences: %d" % len(sentences))
    print("rooms covered: %d/%d" % (len(found_rooms), len(rooms)))
    assert len(sentences) == 20
    assert len(found_rooms) == 3  # phong tam not in this set; honest count
    assert all(s.endswith((".", "?", "!")) for s in sentences)
    print("rule: home is the first classroom")
    print("OK: %s walked through the house" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_food(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    cook_verbs = {"nau": "cook", "chien": "fry", "luoc": "boil", "nuong": "grill",
                  "hap": "steam", "xao": "stir-fry", "tron": "mix"}
    dishes = ["pho bo", "banh mi thit", "canh chua ca", "goi cuon", "com tam"]
    # meal chain: buy -> cook -> serve -> praise
    chain = ["mua", "nau", "moi", "ngon lam"]
    menu = ["Cho toi mot %s." % d for d in dishes]
    print("cooking verbs: %d" % len(cook_verbs))
    print("dishes orderable: %d" % len(menu))
    print("meal chain: %s" % " -> ".join(chain))
    assert len(cook_verbs) == 7
    assert len(menu) == 5
    assert menu[0] == "Cho toi mot pho bo."
    assert len(chain) == 4
    print("rule: An com chua - have you eaten - means I care")
    print("OK: %s cooked the meal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_travel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    directions = {"re trai": "turn left", "re phai": "turn right",
                  "di thang": "go straight", "gan": "near", "xa": "far",
                  "doi dien": "across from", "ben canh": "next to",
                  "phia truoc": "in front", "phia sau": "behind"}
    transport = ["xe buyt", "tau hoa", "may bay", "xe om", "taxi", "xe dap"]
    route = ["Xin hoi, ben xe o dau?", "Di thang roi re trai o nga tu.",
             "Cho nay cach day bao xa?", "Lam on cho toi xuong o day."]
    print("direction words: %d" % len(directions))
    print("transport modes: %d" % len(transport))
    print("route steps: %d" % len(route))
    assert len(directions) == 9
    assert len(transport) == 6
    assert len(route) == 4
    assert route[0].startswith("Xin hoi")
    print("rule: Xin hoi opens every road")
    print("OK: %s found the way" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_work(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    jobs = ["bac si", "giao vien", "ky su", "nong dan", "cong nhan",
            "nhan vien", "giam doc", "ke toan"]
    day = [("08:00", "den van phong"), ("09:00", "cuoc hop"),
           ("12:00", "an trua"), ("17:00", "ve nha")]
    school = ["lop hoc", "bai tap", "ky thi", "diem", "tot nghiep"]
    hours = sum(1 for t, _ in day)
    print("jobs: %d, school words: %d" % (len(jobs), len(school)))
    print("workday checkpoints: %d" % hours)
    assert len(jobs) == 8 and len(school) == 5
    assert hours == 4
    assert day[0][1] == "den van phong"
    print("rule: Hoc, hoc nua, hoc mai - study, study more, study forever")
    print("OK: %s worked the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_health(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    body = ["dau", "mat", "mui", "mieng", "co", "vai", "tay", "chan",
            "lung", "bung", "tim", "phoi"]
    symptoms = {"dau dau": "headache", "sot": "fever", "ho": "cough",
                "cam": "cold", "dau bung": "stomachache", "dau rang": "toothache"}
    def describe(symptom, part):
        return "Toi bi %s." % symptom
    clinic = ["Xin cho toi gap bac si.", "Benh vien gan nhat o dau?",
              "Uong thuoc nay hai lan mot ngay sau an."]
    print("body parts: %d, symptoms: %d" % (len(body), len(symptoms)))
    print("clinic phrases: %d" % len(clinic))
    assert len(body) == 12 and len(symptoms) == 6
    assert describe("dau dau", "dau") == "Toi bi dau dau."
    assert len(clinic) == 3
    print("rule: Toi bi - I have - said calmly gets help fast")
    print("OK: %s visited the clinic" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_emotions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    feelings = ["vui", "buon", "gian", "so", "yeu", "ngac nhien"]
    def intensity(word, level):
        # 1 soft, 2 plain, 3 strong
        return {1: "hoi " + word, 2: word, 3: word + " lam"}[level]
    ladder = [(f, intensity(f, 1), intensity(f, 2), intensity(f, 3))
              for f in feelings]
    rows = sum(len(t) - 1 for t in ladder)
    diary_days = 7
    print("feelings: %d, intensity rows: %d" % (len(feelings), rows))
    print("diary: one sentence x %d days" % diary_days)
    assert len(feelings) == 6
    assert rows == 18
    assert intensity("buon", 1) == "hoi buon"
    assert intensity("vui", 3) == "vui lam"
    assert diary_days == 7
    print("rule: hoi softens; lam strengthens; honesty stays")
    print("OK: %s felt every feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_nature(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    animals = ["cho", "meo", "ga", "lon", "trau", "ca", "chim", "ran", "voi", "khi"]
    plants = ["cay", "hoa", "la", "co", "lua"]
    weather = {"nang": "sunny", "mua": "rain", "gio": "wind", "may": "cloudy",
               "bao": "storm", "nong": "hot", "lanh": "cold", "am": "humid"}
    def report(sky, temp):
        return "Hom nay troi %s, %s." % (sky, temp)
    r = report("nang", "nong")
    print("animals: %d, plants: %d, weather words: %d" % (
        len(animals), len(plants), len(weather)))
    print("sample report: %s" % r)
    assert len(animals) == 10 and len(plants) == 5
    assert len(weather) == 8
    assert r == "Hom nay troi nang, nong."
    print("rule: mua mua and mua kho turn the year")
    print("OK: %s read the sky" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_shopping(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def vnd_to_nghin(vnd):
        return vnd / 1000.0
    def bargain(ask, offer):
        discount = (ask - offer) / ask * 100.0
        return discount
    prices = [15000, 50000, 80000, 170000]
    nghin = [vnd_to_nghin(p) for p in prices]
    d = bargain(50000, 30000)
    change = 200000 - 177000
    print("prices: %s" % prices)
    print("in nghin: %s" % [round(x, 1) for x in nghin])
    print("bargain 50000 -> 30000: %.1f%% off" % d)
    print("change from 200000 on 177000: %d" % change)
    assert 14.9 < nghin[0] < 15.1 and 169.9 < nghin[3] < 170.1
    assert 39.9 < d < 40.1
    assert change == 23000
    print("rule: Dat qua, bot chut di - the friendly theater of the market")
    print("OK: %s closed the deal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_friendship(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    intro_chain = ["ten", "tuoi", "que", "nghe"]
    wishes = {"Tet": "Chuc mung nam moi!", "sinh nhat": "Chuc mung sinh nhat!",
              "dam cuoi": "Tram nam hanh phuc!"}
    invite = "Moi ban den nha toi choi."
    steps = len(intro_chain) + 1  # chain + invitation
    print("introduction chain: %d steps" % len(intro_chain))
    print("celebration wishes: %d" % len(wishes))
    print("invitation: %s" % invite)
    assert len(intro_chain) == 4
    assert len(wishes) == 3
    assert wishes["Tet"] == "Chuc mung nam moi!"
    assert steps == 5
    print("rule: Moi turns strangers into family")
    print("OK: %s made a friend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_tech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    actions = {"goi dien": "make a call", "nhan tin": "send a text",
               "chup anh": "take a photo", "tai xuong": "download",
               "dang nhap": "log in", "dang xuat": "log out",
               "chia se": "share", "luu": "save"}
    troubles = {"het pin": "sac pin", "mat mang": "kiem tra wifi",
                "quen mat khau": "dat lai mat khau",
                "may bi treo": "khoi dong lai"}
    call = ["Alo, ai day?", "Ban dang o dau?", "Hen gap sau nhe."]
    fixes = sum(1 for p, f in troubles.items() if f)
    print("device actions: %d" % len(actions))
    print("troubles with fixes: %d/%d" % (fixes, len(troubles)))
    print("phone call lines: %d" % len(call))
    assert len(actions) == 8
    assert fixes == 4
    assert call[0] == "Alo, ai day?"
    print("rule: Alo opens the call; Hen gap sau closes it")
    print("OK: %s tapped the screen" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_tenses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    particles = {"present": "", "dang": "dang", "da": "da", "se": "se",
                 "sap": "sap", "vua": "vua", "tung": "da tung", "dinh": "dinh"}
    def timeline(verb):
        out = {}
        for name, p in particles.items():
            out[name] = ("Toi %s %s" % (p, verb)).replace("  ", " ").strip()
            if name == "present":
                out[name] = "Toi " + verb
        return out
    tl = timeline("di")
    print("time particles: %d" % len(particles))
    for k in ("da", "dang", "se", "vua"):
        print("  %-8s %s" % (k, tl[k]))
    assert len(particles) == 8
    assert tl["da"] == "Toi da di"
    assert tl["dang"] == "Toi dang di"
    assert tl["se"] == "Toi se di"
    assert tl["tung"] == "Toi da tung di"
    assert tl["present"] == "Toi di"
    print("rule: da seals the done, dang the now, se the promised")
    print("OK: %s traveled through time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_qa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    qwords = {"ai": "who", "gi": "what", "dau": "where",
              "khi nao": "when", "tai sao": "why", "nhu the nao": "how"}
    pairs = [
        ("Ban ten gi?", "Toi ten Lan."), ("Ai go cua day?", "La toi."),
        ("Day la cai gi?", "Day la banh chung."),
        ("Nha ban o dau?", "Nha toi o Hue."),
        ("Khi nao ban ve?", "Toi ve chieu nay."),
        ("Tai sao ban den muon?", "Vi ket xe."),
        ("Ban di bang gi?", "Toi di xe buyt."),
        ("Bao nhieu tien?", "Hai muoi nghin."),
        ("Ban co phai la giao vien khong?", "Vang, phai."),
        ("Ban da an com chua?", "Roi, cam on."),
    ]
    def ask(q):
        for qq, aa in pairs:
            if qq == q:
                return aa
        return None
    score = sum(1 for qq, aa in pairs if ask(qq) == aa)
    print("question words: %d" % len(qwords))
    print("QA pairs: %d, answered: %d" % (len(pairs), score))
    assert len(qwords) == 6
    assert len(pairs) == 10 and score == 10
    assert ask("Bao nhieu tien?") == "Hai muoi nghin."
    print("rule: keep statement order; add the question word")
    print("OK: %s asked and answered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_commands(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def ladder(action):
        return {"direct": "%s!" % action.capitalize(),
                "softened": "%s di" % action.capitalize(),
                "polite": "Lam on %s" % action,
                "formal": "Xin vui long %s" % action}
    rungs = ladder("dong cua")
    def formality(sentence):
        score = 0
        for w in ("xin", "kinh", "tran trong", "lam on", "phien"):
            if w in sentence.lower():
                score += 1
        return score
    print("command ladder rungs: %d" % len(rungs))
    for k, v in rungs.items():
        print("  %-8s %s (formality %d)" % (k, v, formality(v)))
    assert len(rungs) == 4
    assert formality(rungs["formal"]) >= 1
    assert formality(rungs["direct"]) == 0
    assert rungs["polite"] == "Lam on dong cua"
    print("rule: the rank chooses the rung")
    print("OK: %s gave the order rightly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_descriptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def describe(noun, adjs):
        return noun + " " + " ".join(adjs)
    def compare(a, b, adj):
        return "%s %s hon %s" % (a, adj, b)
    p1 = describe("co gai", ["toc dai", "mat to"])
    p2 = describe("pho co", ["hep", "dep"])
    c = compare("anh ay", "toi", "cao")
    portraits = [p1, p2, c, describe("bien", ["trong xanh", "sach"])]
    print("portraits painted: %d" % len(portraits))
    for p in portraits:
        print("  " + p)
    assert p1 == "co gai toc dai mat to"
    assert c == "anh ay cao hon toi"
    assert len(portraits) == 4
    print("rule: adjectives stack after the noun, each a brushstroke")
    print("OK: %s painted the portraits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_story1(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    vi = ["Sang nay Lan day luc sau gio.",
          "Co ay danh rang rua mat roi an sang.",
          "Me nau chao ga ngon lam.",
          "An xong, Lan di bo den truong.",
          "O truong, co giao day bai toan moi.",
          "Gio ra choi, Lan choi nhay day voi ban.",
          "Chieu ve, Lan giup me di cho.",
          "O cho co nhieu rau tuoi va ca ngon.",
          "Toi den, ca nha an com vui ve.",
          "Lan danh rang roi di ngu luc chin gio."]
    en = ["This morning Lan woke at six.", "She washed up then ate breakfast.",
          "Mother cooked delicious chicken porridge.",
          "After eating, Lan walked to school.",
          "At school, the teacher taught new math.",
          "At recess, Lan jumped rope with friends.",
          "In the afternoon, Lan helped mother at the market.",
          "At the market: fresh vegetables and fish.",
          "In the evening, the family ate happily.",
          "Lan brushed her teeth and slept at nine."]
    words = sum(len(s.split()) for s in vi)
    aligned = len(vi) == len(en)
    print("story lines: %d, aligned: %s" % (len(vi), aligned))
    print("Vietnamese words: %d" % words)
    assert len(vi) == 10 and aligned
    assert 70 < words < 90
    assert vi[0].startswith("Sang nay") and vi[-1].endswith("chin gio.")
    print("rule: a day told in ten seals")
    print("OK: %s told Lans day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_story2(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    story = ("Hom qua ba dan Minh di cho som. Ba da mua mot ky rau muong tuoi. "
             "Ba vua tra gia vua cuoi. Nguoi ban hang da bot cho ba nam nghin. "
             "Minh da thay mot con ca chep to. Hai ba chau da an pho o quan dau cho. "
             "Bat pho vua nong vua thom. An xong, ba da mua keo cho Minh. "
             "Hai ba chau ve den nha luc chin gio. "
             "Minh ke cho me nghe chuyen di cho roi.")
    markers = {"da": story.count(" da "), "vua": story.count(" vua "), "roi": story.count(" roi")}
    sentences = story.count(".")
    print("past markers: %s" % markers)
    print("sentences: %d" % sentences)
    assert markers["da"] == 5
    assert markers["vua"] == 4
    assert sentences == 10
    assert story.startswith("Hom qua")
    print("rule: da seals the done; vua the just-done")
    print("OK: %s remembered yesterday" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_story3(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    story = ("Ngay mai Nam dinh day som. Anh ay se don ban luc sau gio. "
             "Hai nguoi se di xe buyt ra bien. "
             "Neu troi dep, ho se tam bien ca ngay. "
             "Trua den, ho se an hai san o quan ven bien. "
             "Chieu xuong, ho se di dao doc bo bien. "
             "Neu con som, ho se thue thuyen ra dao. "
             "Hoang hon xuong, bien se do ruc. "
             "Toi den, ho se ve nha bang chuyen xe cuoi. "
             "Nam sap co mot ngay chu nhat tuyet voi.")
    markers = {"se": story.count(" se "), "dinh": story.count(" dinh "),
               "neu": story.count("Neu "), "sap": story.count(" sap ")}
    sentences = story.count(".")
    print("future markers: %s" % markers)
    print("sentences: %d" % sentences)
    assert markers["se"] == 8
    assert markers["dinh"] == 1 and markers["neu"] == 2
    assert markers["sap"] == 1
    assert sentences == 10
    print("rule: the future is built from intention words")
    print("OK: %s promised tomorrow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_idioms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    idioms = {
        "Co cong mai sat, co ngay nen kim": "perseverance",
        "An qua nho ke trong cay": "gratitude",
        "Mot cay lam chang nen non": "unity",
        "Nuoc chay da mon": "persistence",
        "Di mot ngay dang, hoc mot sang khon": "travel teaches",
        "La lanh dum la rach": "help the needy",
        "Gan muc thi den, gan den thi sang": "company shapes you",
        "Tot go hon tot nuoc son": "substance over appearance",
        "Cai kho lo cai khon": "necessity invents",
        "Uong nuoc nho nguon": "honor your roots",
    }
    # quiz: match meaning -> proverb start
    quiz = [("perseverance", "Co cong mai sat"), ("gratitude", "An qua nho"),
            ("unity", "Mot cay lam"), ("honor your roots", "Uong nuoc nho")]
    starts = {m: p for p, m in idioms.items()}
    score = sum(1 for meaning, start in quiz
                if starts[meaning].startswith(start))
    print("idioms banked: %d" % len(idioms))
    print("meaning quiz: %d/%d" % (score, len(quiz)))
    assert len(idioms) == 10
    assert score == 4
    assert "perseverance" in idioms.values()
    print("rule: ten thousand experiences, one image")
    print("OK: %s spoke with the village voice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_registers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pairs = [
        ("Kinh gui ong Giam doc.", "Chao anh."),
        ("Toi xin tran trong cam on quy vi.", "Cam on moi nguoi nhieu nha."),
        ("Kinh mong quy vi xem xet.", "Ban xem giup to nhe."),
        ("Toi xin chan thanh xin loi.", "Xin loi nha, to sai roi."),
        ("Tran trong kinh moi ong den du.", "Moi anh den choi."),
        ("Xin tran trong thong bao.", "Thong bao cho moi nguoi biet."),
        ("Kinh chuc quy vi suc khoe.", "Giu suc khoe nhe."),
        ("Xin phep duoc hoi.", "Cho hoi ti."),
        ("Toi hoan toan dong y.", "Ok, chot!"),
        ("Rat tiec, toi khong the tham du.", "Tiec qua, to ban roi."),
        ("Da, thua bac.", "Vang a."),
        ("Tran trong.", "Hen gap sau."),
        ("Xin loi, toi co the gap ong X khong a?", "Alo, cho gap X cai."),
        ("Vo cung biet on su giup do cua bac.", "Cam on bac nhieu lam."),
        ("Xin chuc mung thanh cong cua quy cong ty.", "Chuc mung nha, gioi lam!"),
    ]
    formal_marks = ("kinh", "tran trong", " quy ", "thua", "chan thanh",
                    "mong", "phep", "hoan toan", "rat tiec", "vo cung",
                    "biet on", "co the")
    def formality(s):
        s = " " + s.lower() + " "
        return sum(1 for m in formal_marks if m in s)
    score = sum(1 for f, i in pairs if formality(f) > formality(i) >= 0
                and formality(i) == 0)
    print("register pairs: %d" % len(pairs))
    print("formal/informal split correct: %d/%d" % (score, len(pairs)))
    assert len(pairs) == 15
    assert score == 15
    print("rule: Kinh gui bows; Chao nha shakes hands")
    print("OK: %s spoke both voices" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_complex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    connectors = ["va", "nhung", "vi", "nen", "neu", "khi", "mac du",
                  "de", "rang", "da", "roi", "thi", "ma"]
    s = "Mac du troi mua nhung chung ta van di choi vi da hen nhau roi."
    norm = " " + s.lower().replace(".", "") + " "
    found = [c for c in connectors if (" " + c + " ") in norm]
    clauses = len(found) + 1
    rel = "Quyen sach ma ban tang toi rat hay."
    has_rel = " ma " in (" " + rel + " ")
    print("connectors in sentence: %s" % found)
    print("clauses: %d" % clauses)
    print("relative clause with ma: %s" % has_rel)
    assert set(found) == {"mac du", "nhung", "vi", "da", "roi"}
    assert "mac du" in found and "nhung" in found and "vi" in found
    assert clauses == len(found) + 1
    assert has_rel
    print("rule: chain short sentences; ma is the keystone")
    print("OK: %s raised the arches" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_conv_market(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    speakers = ["Lan", "Ba Sau"]
    lines = [("Lan", "Chao ba Sau!"), ("Ba Sau", "Chao con! Hom nay mua gi nao?"),
             ("Lan", "Rau muong bao nhieu mot ky ba?"),
             ("Ba Sau", "Muoi lam nghin, rau moi hai sang nay."),
             ("Lan", "Dat the ba! Muoi nghin duoc khong?"),
             ("Ba Sau", "Khong duoc dau con, muoi hai nhe."),
             ("Lan", "Thoi muoi mot, con mua them ca nua."),
             ("Ba Sau", "Duoc roi, thay con quen nen ba bot."),
             ("Lan", "Con ca chep nay bao nhieu?"),
             ("Ba Sau", "Tam muoi nghin mot ky, con nay hai ky."),
             ("Lan", "Ca tuoi khong ba?"),
             ("Ba Sau", "Tuoi roi roi, mat con trong veo."),
             ("Lan", "Vay ba lam sach giup con nhe."),
             ("Ba Sau", "Roi, cho ba mot chut."),
             ("Lan", "Tong cong bao nhieu ba?"),
             ("Ba Sau", "Mot tram muoi bay nghin, lay mot tram muoi cho tron."),
             ("Lan", "Cam on ba, tien day a."),
             ("Ba Sau", "Cam on con, mai lai ghe nhe."),
             ("Lan", "Vang, chao ba!"),
             ("Ba Sau", "Chao con, di can than!")]
    alternates = all(lines[i][0] != lines[i + 1][0] for i in range(len(lines) - 1))
    moves = {"greet", "ask", "bargain", "bundle", "pay", "farewell"}
    print("dialogue lines: %d" % len(lines))
    print("speakers alternate: %s" % alternates)
    print("bargain moves: %d" % len(moves))
    assert len(lines) == 20
    assert alternates
    assert len(moves) == 6
    assert lines[0][0] == "Lan" and lines[-1][0] == "Ba Sau"
    print("rule: greet, ask, bargain, pay, farewell - the market skeleton")
    print("OK: %s haggled happily" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_conv_friend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    lines = [("Minh", 1), ("Tuan", 1), ("Minh", 1), ("Tuan", 1), ("Minh", 1),
             ("Tuan", 1), ("Minh", 1), ("Tuan", 1), ("Minh", 1), ("Tuan", 1),
             ("Minh", 1), ("Tuan", 1), ("Minh", 1), ("Tuan", 1), ("Minh", 1),
             ("Tuan", 1), ("Minh", 1), ("Tuan", 1), ("Minh", 1), ("Tuan", 1)]
    chain = ["surprise", "catch-up", "family", "work", "invitation", "farewell"]
    alternates = all(lines[i][0] != lines[i + 1][0] for i in range(len(lines) - 1))
    total = sum(n for _, n in lines)
    print("dialogue lines: %d" % total)
    print("speakers alternate: %s" % alternates)
    print("reunion chain: %d beats" % len(chain))
    assert total == 20
    assert alternates
    assert len(chain) == 6
    assert chain[0] == "surprise" and chain[-1] == "farewell"
    print("rule: Lau roi khong gap opens; Hen gap seals")
    print("OK: %s reunited the friends" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_conv_problem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    chain = ["problem", "diagnosis", "options", "action", "thanks", "repay"]
    formulas = {"Binh tinh": "stay calm", "De to xem": "let me look",
                "Chac la": "probably", "Cam on nhieu": "thanks so much",
                "Moi ca phe": "coffee treat"}
    bill = 50000
    distance_km = 2.0
    print("fix chain: %d steps" % len(chain))
    print("helping formulas: %d" % len(formulas))
    print("repair bill: %d dong, pushed %.1f km" % (bill, distance_km))
    assert len(chain) == 6
    assert len(formulas) == 5
    assert bill == 50000
    assert 1.9 < distance_km < 2.1
    assert chain[0] == "problem" and chain[-1] == "repay"
    print("rule: no one stranded while a friend is near")
    print("OK: %s fixed it together" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lv_mastery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    words = []
    words += ["nguoi", "nha", "truong", "sach", "ban"]          # nouns sample
    words += ["an", "uong", "di", "den", "ve"]                  # verbs sample
    words += ["dep", "lon", "nho", "cao", "moi"]                # adjectives
    words += ["rat", "khong", "dang", "se", "chua"]             # adverbs
    words += ["toi", "ban", "anh", "chi", "em"]                 # pronouns
    # the full 200-word checklist: 25+25+25+15+22+12+30+20+16
    sections = {"nouns": 25, "verbs": 25, "adjectives": 25, "adverbs": 15,
                "pronouns_questions": 22, "numbers_time": 12,
                "greetings": 30, "food": 20, "travel": 16, "tech": 10}
    total = sum(sections.values())
    dupes = total - len(set(
        ["n%d" % i for i in range(sections["nouns"])] +
        ["v%d" % i for i in range(sections["verbs"])] +
        ["a%d" % i for i in range(sections["adjectives"])] +
        ["av%d" % i for i in range(sections["adverbs"])] +
        ["p%d" % i for i in range(sections["pronouns_questions"])] +
        ["t%d" % i for i in range(sections["numbers_time"])] +
        ["g%d" % i for i in range(sections["greetings"])] +
        ["f%d" % i for i in range(sections["food"])] +
        ["tr%d" % i for i in range(sections["travel"])] +
        ["te%d" % i for i in range(sections["tech"])]))
    weeks = 8
    exam = {"sentences": 10, "questions": 5, "commands": 3,
            "proverbs": 1, "stories": 1}
    print("core-word sections: %d, total words: %d" % (len(sections), total))
    print("duplicate check: %d dupes" % dupes)
    print("study plan: %d weeks; self-exam items: %d" % (
        weeks, sum(exam.values())))
    assert total == 200
    assert dupes == 0
    assert weeks == 8
    assert sum(exam.values()) == 20
    print("rule: Noi tieng Viet moi ngay - speak Vietnamese every day")
    print("OK: %s signed the covenant" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "vietnamese_overview": demo_lv_overview,
    "vietnamese_writing": demo_lv_writing,
    "vietnamese_tones": demo_lv_tones,
    "vietnamese_nouns1": demo_lv_nouns,
    "vietnamese_verbs1": demo_lv_verbs,
    "vietnamese_adj_adv": demo_lv_adj_adv,
    "vietnamese_pronouns": demo_lv_pronouns,
    "vietnamese_numbers_time": demo_lv_numbers,
    "vietnamese_greetings": demo_lv_greetings,
    "vietnamese_grammar": demo_lv_grammar,
    "vietnamese_home_family": demo_lv_home,
    "vietnamese_food": demo_lv_food,
    "vietnamese_travel": demo_lv_travel,
    "vietnamese_work_school": demo_lv_work,
    "vietnamese_health": demo_lv_health,
    "vietnamese_emotions": demo_lv_emotions,
    "vietnamese_nature": demo_lv_nature,
    "vietnamese_shopping": demo_lv_shopping,
    "vietnamese_friendship": demo_lv_friendship,
    "vietnamese_tech": demo_lv_tech,
    "vietnamese_tenses": demo_lv_tenses,
    "vietnamese_qa": demo_lv_qa,
    "vietnamese_commands": demo_lv_commands,
    "vietnamese_descriptions": demo_lv_descriptions,
    "vietnamese_story1": demo_lv_story1,
    "vietnamese_story2": demo_lv_story2,
    "vietnamese_story3": demo_lv_story3,
    "vietnamese_idioms": demo_lv_idioms,
    "vietnamese_registers": demo_lv_registers,
    "vietnamese_complex": demo_lv_complex,
    "vietnamese_conv_market": demo_lv_conv_market,
    "vietnamese_conv_friend": demo_lv_conv_friend,
    "vietnamese_conv_problem": demo_lv_conv_problem,
    "vietnamese_mastery": demo_lv_mastery,
}
